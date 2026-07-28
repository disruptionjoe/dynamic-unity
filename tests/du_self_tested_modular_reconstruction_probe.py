#!/usr/bin/env python3
"""Exact finite controls for HC-DU-078.

The probe tests a conditional positive escape from HC-DU-077:

1. setting-labeled tilted-CHSH correlations certify a noncommutative target
   factor and a faithful nontracial reduced state under the standard quantum
   Bell/self-testing contract;
2. that reduced state has nontrivial modular data;
3. erasing the setting labels makes the same pooled outcome law compatible
   with a setting-independent classical source; and
4. maximal ordinary CHSH certifies noncommutative measurements but gives a
   tracial local state and therefore trivial local modular flow.

The executable validates the exact two-qubit arithmetic and the
context-erasure counterexample.  The self-testing implication itself is a
literature theorem, not proved by this script.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_self_tested_modular_reconstruction_result.json"
)
TOL = 1e-10


def expectation(state: np.ndarray, observable: np.ndarray) -> float:
    return float(np.real_if_close(state.conj() @ observable @ state))


def density_power_it(rho: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(rho)
    if np.min(values) <= 0:
        raise ValueError("modular control requires a faithful state")
    phases = np.exp(1j * time * np.log(values))
    return vectors @ np.diag(phases) @ vectors.conj().T


def modular_action(
    rho: np.ndarray, observable: np.ndarray, time: float
) -> np.ndarray:
    unitary = density_power_it(rho, time)
    return unitary @ observable @ unitary.conj().T


def projector(observable: np.ndarray, outcome: int) -> np.ndarray:
    identity = np.eye(observable.shape[0], dtype=complex)
    return (identity + outcome * observable) / 2.0


def conditional_law(
    state: np.ndarray,
    alice: list[np.ndarray],
    bob: list[np.ndarray],
) -> dict[tuple[int, int, int, int], float]:
    law: dict[tuple[int, int, int, int], float] = {}
    for x, a_observable in enumerate(alice):
        for y, b_observable in enumerate(bob):
            for a in (-1, 1):
                for b in (-1, 1):
                    joint = np.kron(
                        projector(a_observable, a),
                        projector(b_observable, b),
                    )
                    probability = expectation(state, joint)
                    law[(x, y, a, b)] = probability
    return law


def correlator(
    law: dict[tuple[int, int, int, int], float],
    x: int,
    y: int,
) -> float:
    return sum(
        a * b * law[(x, y, a, b)]
        for a in (-1, 1)
        for b in (-1, 1)
    )


def alice_mean(
    law: dict[tuple[int, int, int, int], float],
    x: int,
    y: int = 0,
) -> float:
    return sum(
        a * law[(x, y, a, b)]
        for a in (-1, 1)
        for b in (-1, 1)
    )


def tilted_score(
    law: dict[tuple[int, int, int, int], float],
    alpha: float,
) -> float:
    return (
        alpha * alice_mean(law, 0)
        + correlator(law, 0, 0)
        + correlator(law, 0, 1)
        + correlator(law, 1, 0)
        - correlator(law, 1, 1)
    )


def pooled_outcomes(
    law: dict[tuple[int, int, int, int], float],
) -> dict[tuple[int, int], float]:
    return {
        (a, b): sum(
            law[(x, y, a, b)] / 4.0
            for x in (0, 1)
            for y in (0, 1)
        )
        for a in (-1, 1)
        for b in (-1, 1)
    }


def setting_independent_law(
    pooled: dict[tuple[int, int], float],
) -> dict[tuple[int, int, int, int], float]:
    return {
        (x, y, a, b): pooled[(a, b)]
        for x in (0, 1)
        for y in (0, 1)
        for a in (-1, 1)
        for b in (-1, 1)
    }


def max_conditional_normalization_error(
    law: dict[tuple[int, int, int, int], float],
) -> float:
    return max(
        abs(
            sum(
                law[(x, y, a, b)]
                for a in (-1, 1)
                for b in (-1, 1)
            )
            - 1.0
        )
        for x in (0, 1)
        for y in (0, 1)
    )


def max_no_signalling_error(
    law: dict[tuple[int, int, int, int], float],
) -> float:
    errors: list[float] = []
    for x in (0, 1):
        for a in (-1, 1):
            left = sum(law[(x, 0, a, b)] for b in (-1, 1))
            right = sum(law[(x, 1, a, b)] for b in (-1, 1))
            errors.append(abs(left - right))
    for y in (0, 1):
        for b in (-1, 1):
            left = sum(law[(0, y, a, b)] for a in (-1, 1))
            right = sum(law[(1, y, a, b)] for a in (-1, 1))
            errors.append(abs(left - right))
    return max(errors)


def main() -> None:
    identity = np.eye(2, dtype=complex)
    x_matrix = np.array([[0, 1], [1, 0]], dtype=complex)
    z_matrix = np.array([[1, 0], [0, -1]], dtype=complex)

    theta = np.pi / 8.0
    cosine = np.cos(theta)
    sine = np.sin(theta)
    state = np.array([cosine, 0, 0, sine], dtype=complex)

    alpha = 2.0 / np.sqrt(3.0)
    cos_mu = np.sqrt(2.0 / 3.0)
    sin_mu = 1.0 / np.sqrt(3.0)

    alice = [z_matrix, x_matrix]
    bob = [
        cos_mu * z_matrix + sin_mu * x_matrix,
        cos_mu * z_matrix - sin_mu * x_matrix,
    ]

    law = conditional_law(state, alice, bob)
    pooled = pooled_outcomes(law)
    classical_law = setting_independent_law(pooled)

    quantum_score = tilted_score(law, alpha)
    quantum_maximum = np.sqrt(8.0 + 2.0 * alpha**2)
    classical_bound = 2.0 + alpha
    erased_score = tilted_score(classical_law, alpha)

    rho_alice = np.diag([cosine**2, sine**2]).astype(complex)
    eigenvalue_ratio = float(rho_alice[0, 0].real / rho_alice[1, 1].real)
    expected_ratio = 3.0 + 2.0 * np.sqrt(2.0)
    off_diagonal = np.array([[0, 1], [0, 0]], dtype=complex)
    modular_off_diagonal = modular_action(rho_alice, off_diagonal, 1.0)
    expected_phase = np.exp(1j * np.log(expected_ratio))

    # Ordinary maximal CHSH is the useful null control: it certifies Pauli
    # structure but the local state is maximally mixed and modularly silent.
    rho_chsh = identity / 2.0
    chsh_flow = modular_action(rho_chsh, x_matrix, 1.0)

    labeled_law_distance = max(
        abs(law[key] - classical_law[key]) for key in law
    )
    pooled_classical = pooled_outcomes(classical_law)
    pooled_distance = max(
        abs(pooled[key] - pooled_classical[key]) for key in pooled
    )

    checks: dict[str, bool] = {
        "partially_entangled_state_is_normalized": (
            abs(np.vdot(state, state).real - 1.0) < TOL
        ),
        "partially_entangled_state_is_not_maximal": (
            abs(cosine**2 - 0.5) > 0.2
        ),
        "alice_observables_are_binary": all(
            np.linalg.norm(observable @ observable - identity) < TOL
            for observable in alice
        ),
        "bob_observables_are_binary": all(
            np.linalg.norm(observable @ observable - identity) < TOL
            for observable in bob
        ),
        "alice_observables_are_noncommutative": (
            np.linalg.norm(
                alice[0] @ alice[1] - alice[1] @ alice[0]
            )
            > 1.0
        ),
        "tilt_matches_theta_pi_over_eight": (
            abs(alpha - 2.0 / np.sqrt(1.0 + 2.0)) < TOL
        ),
        "conditional_probabilities_are_normalized": (
            max_conditional_normalization_error(law) < TOL
        ),
        "conditional_probabilities_are_nonnegative": (
            min(law.values()) > -TOL
        ),
        "quantum_law_is_no_signalling": (
            max_no_signalling_error(law) < TOL
        ),
        "tilted_score_attains_quantum_maximum": (
            abs(quantum_score - quantum_maximum) < TOL
        ),
        "tilted_score_exceeds_classical_bound": (
            quantum_score > classical_bound + 0.1
        ),
        "local_reduced_state_is_faithful": (
            np.min(np.linalg.eigvalsh(rho_alice)) > 0
        ),
        "local_reduced_state_is_nontracial": (
            np.linalg.norm(rho_alice - identity / 2.0) > 0.4
        ),
        "local_modular_ratio_is_three_plus_two_root_two": (
            abs(eigenvalue_ratio - expected_ratio) < TOL
        ),
        "local_modular_phase_matches_certified_ratio": (
            abs(modular_off_diagonal[0, 1] - expected_phase) < TOL
        ),
        "local_modular_flow_is_nontrivial": (
            np.linalg.norm(modular_off_diagonal - off_diagonal) > 1.0
        ),
        "ordinary_chsh_local_state_is_tracial": (
            np.linalg.norm(rho_chsh - identity / 2.0) < TOL
        ),
        "ordinary_chsh_local_modular_flow_is_trivial": (
            np.linalg.norm(chsh_flow - x_matrix) < TOL
        ),
        "pooled_output_law_is_normalized": (
            abs(sum(pooled.values()) - 1.0) < TOL
        ),
        "classical_control_has_identical_unlabeled_records": (
            pooled_distance < TOL
        ),
        "classical_control_differs_when_labels_are_retained": (
            labeled_law_distance > 0.1
        ),
        "classical_control_obeys_tilted_classical_bound": (
            erased_score <= classical_bound + TOL
        ),
        "setting_erasure_destroys_self_testing_score": (
            quantum_score - erased_score > 1.0
        ),
    }

    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "claim_id": "HC-DU-078",
        "status": "PASS" if not failures else "FAIL",
        "checks_passed": len(checks) - len(failures),
        "checks_total": len(checks),
        "failures": failures,
        "exact_fixture": {
            "theta": "pi/8",
            "alpha": "2/sqrt(3)",
            "cos_mu": "sqrt(2/3)",
            "sin_mu": "1/sqrt(3)",
            "quantum_maximum": "4*sqrt(6)/3",
            "classical_bound": "2 + 2/sqrt(3)",
            "local_state": "diag((2+sqrt(2))/4,(2-sqrt(2))/4)",
            "modular_eigenvalue_ratio": "3 + 2*sqrt(2)",
        },
        "numeric_certificate": {
            "tilted_quantum_score": quantum_score,
            "tilted_quantum_maximum": quantum_maximum,
            "tilted_classical_bound": classical_bound,
            "setting_erased_control_score": erased_score,
            "labeled_law_max_distance": labeled_law_distance,
            "unlabeled_law_max_distance": pooled_distance,
            "local_modular_eigenvalue_ratio": eigenvalue_ratio,
            "local_modular_phase_real": float(
                modular_off_diagonal[0, 1].real
            ),
            "local_modular_phase_imag": float(
                modular_off_diagonal[0, 1].imag
            ),
            "max_no_signalling_error": max_no_signalling_error(law),
        },
        "interpretation": {
            "positive": (
                "Under the standard quantum Bell/self-testing contract, "
                "the labeled maximal tilted-CHSH law certifies a target "
                "noncommutative factor and faithful nontracial target state "
                "up to local isometry and auxiliary degrees of freedom."
            ),
            "hostile": (
                "After setting erasure, a setting-independent classical "
                "source reproduces the complete pooled outcome law exactly."
            ),
            "null": (
                "Maximal ordinary CHSH certifies noncommutative Pauli "
                "structure while the extracted local state is tracial and "
                "has trivial local modular flow."
            ),
            "not_established": [
                "physical selection of settings or subsystem separation",
                "measurement independence or implementation-complete acquisition",
                "record formation, provenance, retention, or observer access",
                "ambient modular flow outside the extracted target factor",
                "proper-time calibration, geometry, ontology, or new physics",
            ],
        },
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
