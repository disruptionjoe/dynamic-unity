#!/usr/bin/env python3
"""Exact controls for HC-DU-175.

The probe checks a two-region U(1) symmetry-reduction model. Passing
establishes only the finite standard-quantum controls behind the analytic
result. It does not select a material record, archive, provenance relation,
observer, finality rule, or new dynamics.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_relational_reference_symmetry_reduction_result.json"
)
TOL = 1e-10

I2 = np.eye(2, dtype=complex)
NUMBER = np.diag([0.0, 1.0]).astype(complex)
N_A = np.kron(NUMBER, I2)
N_B = np.kron(I2, NUMBER)
N_TOTAL = N_A + N_B

KET_01 = np.array([0.0, 1.0, 0.0, 0.0], dtype=complex)
KET_10 = np.array([0.0, 0.0, 1.0, 0.0], dtype=complex)
RHO_10 = np.outer(KET_10, KET_10.conjugate())
SINGLE_PROJECTOR = (
    np.outer(KET_01, KET_01.conjugate())
    + np.outer(KET_10, KET_10.conjugate())
)


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def close(left: complex | float, right: complex | float) -> bool:
    return bool(abs(left - right) <= TOL)


def density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conjugate())


def local_phase(alpha: float, beta: float) -> np.ndarray:
    phases = [
        1.0,
        cmath.exp(-1j * beta),
        cmath.exp(-1j * alpha),
        cmath.exp(-1j * (alpha + beta)),
    ]
    return np.diag(phases).astype(complex)


def exchange_hamiltonian(phi: float, coupling: float = 1.0) -> np.ndarray:
    return coupling * (
        cmath.exp(1j * phi)
        * np.outer(KET_10, KET_01.conjugate())
        + cmath.exp(-1j * phi)
        * np.outer(KET_01, KET_10.conjugate())
    )


def exchange_unitary(phi: float, tau: float) -> np.ndarray:
    """Return exp(-i H_phi t) with tau=Jt."""
    normalized_h = exchange_hamiltonian(phi, coupling=1.0)
    return (
        np.eye(4, dtype=complex)
        + (math.cos(tau) - 1.0) * SINGLE_PROJECTOR
        - 1j * math.sin(tau) * normalized_h
    )


def relative_coherence(state: np.ndarray) -> complex:
    return complex(state[2, 1])


def local_dephase(state: np.ndarray) -> np.ndarray:
    diagonal = np.zeros_like(state)
    np.fill_diagonal(diagonal, np.diag(state))
    return diagonal


def partial_trace_two_qubits(
    state: np.ndarray,
    keep: str,
) -> np.ndarray:
    tensor = state.reshape(2, 2, 2, 2)
    if keep == "A":
        return np.trace(tensor, axis1=1, axis2=3)
    if keep == "B":
        return np.trace(tensor, axis1=0, axis2=2)
    raise ValueError(f"unknown subsystem {keep}")


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    # The input has no local phase orientation: its density matrix is fixed
    # by every independent local U(1)^2 rephasing.
    invariance_errors = []
    for alpha, beta in ((0.3, -0.7), (1.1, 0.2), (-0.4, 2.0)):
        frame = local_phase(alpha, beta)
        invariance_errors.append(
            max_abs(frame @ RHO_10 @ frame.conjugate().T - RHO_10)
        )
    checks.append(
        {
            "name": "input_is_invariant_under_independent_local_phases",
            "passed": max(invariance_errors) <= TOL,
            "max_error": max(invariance_errors),
        }
    )

    # Identity and independent local twirling are full-G covariant controls.
    # Neither creates the nontrivial |10><01| character mode.
    identity_coherence = relative_coherence(RHO_10)
    dephased_coherence = relative_coherence(local_dephase(RHO_10))
    checks.append(
        {
            "name": "full_local_covariance_no_generation_controls",
            "passed": close(identity_coherence, 0j)
            and close(dephased_coherence, 0j),
            "identity_coherence_abs": abs(identity_coherence),
            "dephased_coherence_abs": abs(dephased_coherence),
        }
    )

    # The exchange Hamiltonian conserves total excitation but not either
    # local excitation separately. Its physical symmetry is the diagonal
    # U(1), not U(1)^2.
    phi = 0.37
    hamiltonian = exchange_hamiltonian(phi)
    total_commutator = hamiltonian @ N_TOTAL - N_TOTAL @ hamiltonian
    local_commutator = hamiltonian @ N_A - N_A @ hamiltonian
    checks.append(
        {
            "name": "exchange_reduces_local_symmetry_to_diagonal_u1",
            "passed": max_abs(total_commutator) <= TOL
            and max_abs(local_commutator) > 0.5,
            "total_number_commutator_norm": max_abs(total_commutator),
            "local_number_commutator_norm": max_abs(local_commutator),
        }
    )

    # The exact evolution generates relational coherence at intermediate
    # times while retaining locally diagonal reduced states.
    tau = math.pi / 4
    unitary = exchange_unitary(phi, tau)
    evolved = unitary @ RHO_10 @ unitary.conjugate().T
    coherence = relative_coherence(evolved)
    expected_coherence = 0.5j * cmath.exp(1j * phi)
    local_a = partial_trace_two_qubits(evolved, "A")
    local_b = partial_trace_two_qubits(evolved, "B")
    checks.append(
        {
            "name": "exchange_creates_purely_relational_coherence",
            "passed": close(coherence, expected_coherence)
            and close(local_a[0, 1], 0j)
            and close(local_b[0, 1], 0j),
            "coherence_real": coherence.real,
            "coherence_imag": coherence.imag,
            "coherence_abs": abs(coherence),
            "local_a_off_diagonal_abs": abs(local_a[0, 1]),
            "local_b_off_diagonal_abs": abs(local_b[0, 1]),
        }
    )

    # The created mode follows sin(2 tau)/2 and vanishes at the endpoints:
    # formation is coherent and reversible, not a record-finality process.
    time_controls = []
    for control_tau in (0.0, math.pi / 4, math.pi / 2, math.pi):
        control_u = exchange_unitary(phi, control_tau)
        control_state = control_u @ RHO_10 @ control_u.conjugate().T
        observed = abs(relative_coherence(control_state))
        predicted = abs(math.sin(2.0 * control_tau)) / 2.0
        time_controls.append((control_tau, observed, predicted))
    checks.append(
        {
            "name": "relational_coherence_is_reversible_not_final",
            "passed": all(
                close(observed, predicted)
                for _, observed, predicted in time_controls
            ),
            "time_controls": [
                {
                    "tau": control_tau,
                    "observed": observed,
                    "predicted": predicted,
                }
                for control_tau, observed, predicted in time_controls
            ],
        }
    )

    # A local basis change moves the coupling phase and the state together.
    # No absolute phase origin is selected.
    alpha, beta = 0.61, -0.23
    frame = local_phase(alpha, beta)
    transformed_phi = phi - alpha + beta
    transformed_h = exchange_hamiltonian(transformed_phi)
    h_covariance_error = max_abs(
        frame @ hamiltonian @ frame.conjugate().T - transformed_h
    )
    transformed_u = exchange_unitary(transformed_phi, tau)
    transformed_state = transformed_u @ RHO_10 @ transformed_u.conjugate().T
    state_covariance_error = max_abs(
        frame @ evolved @ frame.conjugate().T - transformed_state
    )
    checks.append(
        {
            "name": "coupling_and_state_rephase_covariantly",
            "passed": h_covariance_error <= TOL
            and state_covariance_error <= TOL,
            "hamiltonian_error": h_covariance_error,
            "state_error": state_covariance_error,
        }
    )

    # A common phase is still gauge on the one-excitation sector.
    global_frame = local_phase(0.73, 0.73)
    global_error = max_abs(
        global_frame @ evolved @ global_frame.conjugate().T - evolved
    )
    checks.append(
        {
            "name": "absolute_global_phase_remains_unselected",
            "passed": global_error <= TOL,
            "max_error": global_error,
        }
    )

    # Actual unresolved run-to-run coupling phases erase the system-only
    # character mode. This is an ensemble/access statement, not collapse of
    # a fixed but merely unknown phase.
    phase_grid = tuple(turn * math.pi / 2 for turn in range(4))
    phase_states = []
    for phase in phase_grid:
        phase_u = exchange_unitary(phase, tau)
        phase_states.append(phase_u @ RHO_10 @ phase_u.conjugate().T)
    averaged_state = sum(phase_states) / len(phase_states)
    checks.append(
        {
            "name": "unresolved_physical_phase_randomization_erases_system_mode",
            "passed": close(relative_coherence(averaged_state), 0j),
            "averaged_coherence_abs": abs(relative_coherence(averaged_state)),
        }
    )

    # Keeping the phase relation as a joined label restores a common
    # character coordinate, but the label/archive is supplied in this model.
    conditioned_modes = [
        cmath.exp(-1j * phase) * relative_coherence(state)
        for phase, state in zip(phase_grid, phase_states)
    ]
    checks.append(
        {
            "name": "retained_phase_relation_restores_conditioned_mode",
            "passed": all(close(mode, 0.5j) for mode in conditioned_modes),
            "conditioned_modes": [
                {"real": mode.real, "imag": mode.imag}
                for mode in conditioned_modes
            ],
        }
    )

    # A stable physical coupling can embody the relation for a bounded
    # prepare-and-invert task. An explicit numerical phase record is not
    # required when the same coupling is reused; a mismatched coupling leaks.
    mismatch_controls = []
    for mismatch in (0.0, 0.2, 0.7, math.pi):
        prepare = exchange_unitary(phi, tau)
        decode = exchange_unitary(phi + mismatch, tau).conjugate().T
        final_state = decode @ prepare @ KET_10
        observed = abs(np.vdot(KET_10, final_state)) ** 2
        predicted = math.cos(mismatch / 2.0) ** 2
        mismatch_controls.append((mismatch, observed, predicted))
    checks.append(
        {
            "name": "stable_coupling_embodies_action_relative_reference",
            "passed": all(
                close(observed, predicted)
                for _, observed, predicted in mismatch_controls
            ),
            "mismatch_controls": [
                {
                    "phase_mismatch": mismatch,
                    "return_probability": observed,
                    "predicted": predicted,
                }
                for mismatch, observed, predicted in mismatch_controls
            ],
        }
    )

    # The interaction does not form an archive: prepare-and-invert can return
    # every admitted degree of freedom to the initial state.
    round_trip = unitary.conjugate().T @ evolved @ unitary
    checks.append(
        {
            "name": "coherent_reference_generation_does_not_form_record",
            "passed": max_abs(round_trip - RHO_10) <= TOL,
            "round_trip_error": max_abs(round_trip - RHO_10),
        }
    )

    passed = all(bool(check["passed"]) for check in checks)
    return {
        "probe": "du_relational_reference_symmetry_reduction_probe",
        "claim_id": "HC-DU-175",
        "status": "PASS" if passed else "FAIL",
        "checks_passed": sum(bool(check["passed"]) for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "theorem_surface": {
            "no_generation": (
                "A U(1)^2-invariant input stays invariant under every "
                "U(1)^2-covariant channel, so its nontrivial relative "
                "character mode remains zero."
            ),
            "positive_control": (
                "A total-number-conserving exchange interaction reduces "
                "U(1)^2 to diagonal U(1) and creates relative coherence "
                "with no local coherence or absolute phase."
            ),
            "embodied_reference": (
                "Reusing the same stable coupling closes a bounded "
                "prepare/invert task; mismatch delta gives return "
                "probability cos^2(delta/2)."
            ),
        },
        "duplicate_guard": (
            "Generic phase-orbit selection, oriented-reference necessity, "
            "GHZ threshold/pooling, and cycle holonomy are prior DU results. "
            "This probe checks only the symmetry-reduction bridge."
        ),
        "interpretation": (
            "A relational reference need not be an absolute frame or a "
            "separate classical label. It can be embodied in a stable "
            "cross-region interaction. Portability, provenance, retention, "
            "and public certification remain additional physical questions."
        ),
        "scope_limit": (
            "Standard symmetry, asymmetry-resource, quantum-reference-frame, "
            "and exchange-interaction physics. No record, archive, observer, "
            "finality rule, empirical excess, or new physics is selected."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
