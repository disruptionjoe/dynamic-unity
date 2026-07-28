#!/usr/bin/env python3
"""Exact finite controls for HC-DU-077.

The probe separates:

1. the modular flow intrinsic to a commutative record algebra;
2. modular flow on a noncommutative ambient algebra;
3. agreement on every observable in the record algebra;
4. disagreement on ambient modular dynamics; and
5. dimensionless modular parameter from physical clock calibration.

It is a finite operator-algebra certificate.  It does not model a Type-III
AQFT algebra, derive proper time, select a physical state, or reconstruct
spacetime.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_commutative_record_modular_time_result.json"
)
TOL = 1e-10


def density_power_it(rho: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(rho)
    if np.min(values) <= 0:
        raise ValueError("modular control requires a faithful density matrix")
    phases = np.exp(1j * time * np.log(values))
    return vectors @ np.diag(phases) @ vectors.conj().T


def modular_action(
    rho: np.ndarray, observable: np.ndarray, time: float
) -> np.ndarray:
    unitary = density_power_it(rho, time)
    return unitary @ observable @ unitary.conj().T


def hs_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix))


def expectation(rho: np.ndarray, observable: np.ndarray) -> complex:
    return complex(np.trace(rho @ observable))


def normalized_power(rho: np.ndarray, alpha: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(rho)
    powered = vectors @ np.diag(values**alpha) @ vectors.conj().T
    return powered / np.trace(powered)


def main() -> None:
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    e01 = np.array([[0, 1], [0, 0]], dtype=complex)
    p0 = np.array([[1, 0], [0, 0]], dtype=complex)
    p1 = np.array([[0, 0], [0, 1]], dtype=complex)

    # The complete classical record algebra is D = span{I,Z}.
    record_basis = [identity, z]

    rho_tracial = identity / 2.0
    coherence = 3.0 / 5.0
    rho_coherent = (identity + coherence * x) / 2.0
    rho_diagonal = np.diag([4.0 / 5.0, 1.0 / 5.0]).astype(complex)

    time = 1.0
    trace_flow_z = modular_action(rho_tracial, z, time)
    coherent_flow_z = modular_action(rho_coherent, z, time)
    diagonal_flow_x = modular_action(rho_diagonal, x, time)
    diagonal_flow_z = modular_action(rho_diagonal, z, time)
    diagonal_flow_e01 = modular_action(rho_diagonal, e01, time)

    # On D itself every faithful state is tracial because D is commutative.
    # The finite density representative commutes with every element of D.
    record_state = np.diag([4.0 / 5.0, 1.0 / 5.0]).astype(complex)
    record_flow_p0 = modular_action(record_state, p0, time)
    record_flow_p1 = modular_action(record_state, p1, time)

    same_record_restriction = all(
        abs(expectation(rho_tracial, observable)
            - expectation(rho_coherent, observable))
        < TOL
        for observable in record_basis
    )

    expected_phase = np.exp(1j * np.log(4.0))
    actual_phase = diagonal_flow_e01[0, 1]

    rho_power_two = normalized_power(rho_diagonal, 2.0)
    rescaled_flow = modular_action(rho_power_two, x, 0.5)

    group_left = modular_action(
        rho_coherent,
        modular_action(rho_coherent, y, 0.37),
        0.61,
    )
    group_right = modular_action(rho_coherent, y, 0.98)

    checks: dict[str, bool] = {
        "tracial_state_is_faithful": (
            np.min(np.linalg.eigvalsh(rho_tracial)) > 0
        ),
        "coherent_state_is_faithful": (
            np.min(np.linalg.eigvalsh(rho_coherent)) > 0
        ),
        "diagonal_state_is_faithful": (
            np.min(np.linalg.eigvalsh(rho_diagonal)) > 0
        ),
        "ambient_states_agree_on_complete_record_algebra": (
            same_record_restriction
        ),
        "ambient_states_are_not_equal": (
            hs_norm(rho_tracial - rho_coherent) > 0.4
        ),
        "tracial_ambient_modular_flow_is_trivial": (
            hs_norm(trace_flow_z - z) < TOL
        ),
        "coherent_ambient_modular_flow_is_nontrivial": (
            hs_norm(coherent_flow_z - z) > 0.5
        ),
        "coherent_ambient_flow_leaves_record_algebra": (
            abs(coherent_flow_z[0, 1]) > 0.1
        ),
        "commutative_record_projector_zero_is_fixed": (
            hs_norm(record_flow_p0 - p0) < TOL
        ),
        "commutative_record_projector_one_is_fixed": (
            hs_norm(record_flow_p1 - p1) < TOL
        ),
        "diagonal_ambient_state_fixes_record_algebra": (
            hs_norm(diagonal_flow_z - z) < TOL
        ),
        "diagonal_ambient_state_has_nontrivial_offdiagonal_flow": (
            hs_norm(diagonal_flow_x - x) > 0.5
        ),
        "modular_phase_matches_log_eigenvalue_ratio": (
            abs(actual_phase - expected_phase) < TOL
        ),
        "modular_flow_preserves_its_state": (
            hs_norm(
                modular_action(rho_coherent, rho_coherent, time)
                - rho_coherent
            )
            < TOL
        ),
        "modular_automorphisms_obey_group_law": (
            hs_norm(group_left - group_right) < TOL
        ),
        "normalized_state_power_rescales_modular_parameter": (
            hs_norm(rescaled_flow - diagonal_flow_x) < TOL
        ),
        "record_statistics_do_not_fix_ambient_modular_flow": (
            same_record_restriction
            and hs_norm(coherent_flow_z - trace_flow_z) > 0.5
        ),
        "record_algebra_is_commutative": all(
            hs_norm(left @ right - right @ left) < TOL
            for left in record_basis
            for right in record_basis
        ),
        "ambient_algebra_is_noncommutative": hs_norm(x @ z - z @ x) > 1.0,
    }

    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "claim_id": "HC-DU-077",
        "status": "PASS" if not failures else "FAIL",
        "checks_passed": len(checks) - len(failures),
        "checks_total": len(checks),
        "failures": failures,
        "exact_fixture": {
            "record_algebra": "D = span{I,Z}",
            "record_expectations_tracial": [
                expectation(rho_tracial, observable).real
                for observable in record_basis
            ],
            "record_expectations_coherent": [
                expectation(rho_coherent, observable).real
                for observable in record_basis
            ],
            "ambient_state_distance_hilbert_schmidt": hs_norm(
                rho_tracial - rho_coherent
            ),
            "same_record_different_flow_margin": hs_norm(
                coherent_flow_z - trace_flow_z
            ),
            "coherent_flow_offdiagonal_magnitude": float(
                abs(coherent_flow_z[0, 1])
            ),
            "diagonal_state_eigenvalue_ratio": 4.0,
            "offdiagonal_modular_phase": [
                float(actual_phase.real),
                float(actual_phase.imag),
            ],
            "state_power_rescaling_error": hs_norm(
                rescaled_flow - diagonal_flow_x
            ),
        },
        "scope": (
            "Finite certificate that a commutative record algebra has "
            "trivial intrinsic modular flow and that its complete state "
            "does not determine ambient modular dynamics. No physical "
            "state, time calibration, Type-III algebra, geometry, record "
            "formation, or new law is selected."
        ),
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"{result['status']}: {result['checks_passed']}/"
        f"{result['checks_total']} checks"
    )
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
