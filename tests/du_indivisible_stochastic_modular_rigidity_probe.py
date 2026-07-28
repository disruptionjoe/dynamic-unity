#!/usr/bin/env python3
"""Exact finite controls for HC-DU-079.

The probe collides the HC-DU-078 tilted-CHSH law with Barandes's native
indivisible-stochastic representation:

1. the four setting pairs are initial configurations and the four joint
   outcomes are target configurations, so Gamma[(a,b),(x,y)] = p(a,b|x,y);
2. the complete labeled Gamma is unchanged under a Schur-Hadamard phase lift;
3. an allowed one-parameter row-phase family changes the reduced-state
   spectrum relative to a fixed supplied A x B factor;
4. the all-positive lift happens to reproduce 3 + 2 sqrt(2), while the
   phi=pi lift gives 3, proving that the match is not stochastic-native; and
5. a binary three-time pair has identical base-time transition families but
   opposite intermediate temporal facts.

The executable validates the finite arithmetic.  The scope statements about
the stochastic-quantum correspondence and tilted-CHSH self-testing are
literature claims, not proved by this script.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_indivisible_stochastic_modular_rigidity_result.json"
)
TOL = 1e-10


def expectation(state: np.ndarray, observable: np.ndarray) -> float:
    return float(np.real_if_close(state.conj() @ observable @ state))


def projector(observable: np.ndarray, outcome: int) -> np.ndarray:
    identity = np.eye(observable.shape[0], dtype=complex)
    return (identity + outcome * observable) / 2.0


def conditional_law(
    state: np.ndarray,
    alice: list[np.ndarray],
    bob: list[np.ndarray],
) -> dict[tuple[int, int, int, int], float]:
    law: dict[tuple[int, int, int, int], float] = {}
    for x, alice_observable in enumerate(alice):
        for y, bob_observable in enumerate(bob):
            for a in (-1, 1):
                for b in (-1, 1):
                    joint = np.kron(
                        projector(alice_observable, a),
                        projector(bob_observable, b),
                    )
                    law[(x, y, a, b)] = expectation(state, joint)
    return law


def transition_matrix(
    law: dict[tuple[int, int, int, int], float],
) -> np.ndarray:
    setting_order = [(0, 0), (0, 1), (1, 0), (1, 1)]
    outcome_order = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    return np.array(
        [
            [law[(x, y, a, b)] for x, y in setting_order]
            for a, b in outcome_order
        ],
        dtype=float,
    )


def reduced_alice(state: np.ndarray) -> np.ndarray:
    reshaped = state.reshape(2, 2, 2, 2)
    return np.trace(reshaped, axis1=1, axis2=3)


def modular_ratio(state: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(state)
    if eigenvalues[0] <= 0:
        raise ValueError("modular ratio requires a faithful state")
    return float(eigenvalues[-1] / eigenvalues[0])


def tilted_score(
    law: dict[tuple[int, int, int, int], float],
    alpha: float,
) -> float:
    alice_mean = sum(
        a * law[(0, 0, a, b)] for a in (-1, 1) for b in (-1, 1)
    )

    def correlator(x: int, y: int) -> float:
        return sum(
            a * b * law[(x, y, a, b)]
            for a in (-1, 1)
            for b in (-1, 1)
        )

    return (
        alpha * alice_mean
        + correlator(0, 0)
        + correlator(0, 1)
        + correlator(1, 0)
        - correlator(1, 1)
    )


def max_no_signalling_error(
    law: dict[tuple[int, int, int, int], float],
) -> float:
    errors: list[float] = []
    for x in (0, 1):
        for a in (-1, 1):
            errors.append(
                abs(
                    sum(law[(x, 0, a, b)] for b in (-1, 1))
                    - sum(law[(x, 1, a, b)] for b in (-1, 1))
                )
            )
    for y in (0, 1):
        for b in (-1, 1):
            errors.append(
                abs(
                    sum(law[(0, y, a, b)] for a in (-1, 1))
                    - sum(law[(1, y, a, b)] for a in (-1, 1))
                )
            )
    return max(errors)


def phase_lift(
    gamma: np.ndarray,
    phase: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return potential, output density, and fixed-factor Alice reduction."""
    diagonal_phase = np.diag(
        [1.0, 1.0, 1.0, np.exp(1j * phase)]
    ).astype(complex)
    potential = diagonal_phase @ np.sqrt(gamma).astype(complex)
    initial_density = np.eye(4, dtype=complex) / 4.0
    output_density = potential @ initial_density @ potential.conj().T
    return potential, output_density, reduced_alice(output_density)


def temporal_realizer(correlated: bool) -> np.ndarray:
    """P(x1,x2|x0) with uniform x1 and correlated/anticorrelated x2."""
    result = np.zeros((2, 2, 2), dtype=float)
    for x0 in (0, 1):
        for x1 in (0, 1):
            x2 = x1 if correlated else 1 - x1
            result[x0, x1, x2] = 0.5
    return result


def base_transition_at(
    realizer: np.ndarray,
    target_axis: int,
) -> np.ndarray:
    """Return Gamma(target <- x0), with target_axis 1 or 2."""
    if target_axis == 1:
        return np.sum(realizer, axis=2).T
    if target_axis == 2:
        return np.sum(realizer, axis=1).T
    raise ValueError("target_axis must be 1 or 2")


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
    law = conditional_law(
        state,
        [z_matrix, x_matrix],
        [
            cos_mu * z_matrix + sin_mu * x_matrix,
            cos_mu * z_matrix - sin_mu * x_matrix,
        ],
    )
    gamma = transition_matrix(law)

    potential_zero, density_zero, reduced_zero = phase_lift(gamma, 0.0)
    potential_pi, density_pi, reduced_pi = phase_lift(gamma, np.pi)

    gamma_zero = np.abs(potential_zero) ** 2
    gamma_pi = np.abs(potential_pi) ** 2
    output_probabilities_zero = np.real(np.diag(density_zero))
    output_probabilities_pi = np.real(np.diag(density_pi))

    expected_reduced_zero = np.array(
        [
            [0.5 - np.sqrt(2.0) / 8.0, np.sqrt(6.0) / 8.0],
            [np.sqrt(6.0) / 8.0, 0.5 + np.sqrt(2.0) / 8.0],
        ],
        dtype=complex,
    )
    expected_reduced_pi = np.array(
        [
            [0.5 - np.sqrt(2.0) / 8.0, -np.sqrt(2.0) / 8.0],
            [-np.sqrt(2.0) / 8.0, 0.5 + np.sqrt(2.0) / 8.0],
        ],
        dtype=complex,
    )
    expected_eigenvalues_zero = np.array(
        [(2.0 - np.sqrt(2.0)) / 4.0, (2.0 + np.sqrt(2.0)) / 4.0]
    )
    expected_eigenvalues_pi = np.array([0.25, 0.75])
    expected_ratio_zero = 3.0 + 2.0 * np.sqrt(2.0)
    expected_ratio_pi = 3.0

    phase_grid = np.linspace(0.0, np.pi, 33)
    observed_grid: list[float] = []
    expected_grid: list[float] = []
    for phase in phase_grid:
        _, _, reduction = phase_lift(gamma, float(phase))
        observed_grid.append(modular_ratio(reduction))
        radical = np.sqrt(6.0 + 2.0 * np.cos(phase))
        expected_grid.append((4.0 + radical) / (4.0 - radical))

    # D(pi) = diag(1,1,1,-1) is controlled-Z in the supplied A x B
    # factor.  Its operator realignment has rank 2, so it is not a product
    # unitary even though it is a diagonal configuration rephasing.
    controlled_z = np.diag([1.0, 1.0, 1.0, -1.0]).astype(complex)
    realigned = controlled_z.reshape(2, 2, 2, 2).transpose(
        0, 2, 1, 3
    ).reshape(4, 4)
    controlled_z_operator_schmidt_rank = int(
        np.linalg.matrix_rank(realigned, tol=TOL)
    )

    correlated = temporal_realizer(correlated=True)
    anticorrelated = temporal_realizer(correlated=False)
    correlated_t1 = base_transition_at(correlated, 1)
    correlated_t2 = base_transition_at(correlated, 2)
    anticorrelated_t1 = base_transition_at(anticorrelated, 1)
    anticorrelated_t2 = base_transition_at(anticorrelated, 2)
    equality_correlated = float(
        sum(correlated[:, x, x].sum() for x in (0, 1)) / 2.0
    )
    equality_anticorrelated = float(
        sum(anticorrelated[:, x, x].sum() for x in (0, 1)) / 2.0
    )

    quantum_score = tilted_score(law, alpha)
    quantum_maximum = np.sqrt(8.0 + 2.0 * alpha**2)

    checks: dict[str, bool] = {
        "tilted_law_has_four_setting_columns": gamma.shape == (4, 4),
        "tilted_law_is_column_stochastic": (
            np.max(np.abs(np.sum(gamma, axis=0) - 1.0)) < TOL
        ),
        "tilted_law_is_nonnegative": np.min(gamma) > -TOL,
        "tilted_law_is_no_signalling": max_no_signalling_error(law) < TOL,
        "tilted_score_attains_quantum_maximum": (
            abs(quantum_score - quantum_maximum) < TOL
        ),
        "transition_matrix_is_not_directly_unistochastic": (
            np.max(np.abs(np.sum(gamma, axis=1) - 1.0)) > 0.5
        ),
        "zero_phase_lift_recovers_complete_gamma": (
            np.max(np.abs(gamma_zero - gamma)) < TOL
        ),
        "pi_phase_lift_recovers_complete_gamma": (
            np.max(np.abs(gamma_pi - gamma)) < TOL
        ),
        "phase_lifts_have_identical_labeled_transition_objects": (
            np.max(np.abs(gamma_zero - gamma_pi)) < TOL
        ),
        "phase_lifts_have_identical_output_probabilities": (
            np.max(
                np.abs(output_probabilities_zero - output_probabilities_pi)
            )
            < TOL
        ),
        "phase_lifts_have_identical_global_density_spectra": (
            np.max(
                np.abs(
                    np.linalg.eigvalsh(density_zero)
                    - np.linalg.eigvalsh(density_pi)
                )
            )
            < TOL
        ),
        "zero_phase_reduction_matches_exact_matrix": (
            np.linalg.norm(reduced_zero - expected_reduced_zero) < TOL
        ),
        "pi_phase_reduction_matches_exact_matrix": (
            np.linalg.norm(reduced_pi - expected_reduced_pi) < TOL
        ),
        "zero_phase_reduced_spectrum_matches_exact_values": (
            np.max(
                np.abs(
                    np.linalg.eigvalsh(reduced_zero)
                    - expected_eigenvalues_zero
                )
            )
            < TOL
        ),
        "pi_phase_reduced_spectrum_matches_exact_values": (
            np.max(
                np.abs(
                    np.linalg.eigvalsh(reduced_pi)
                    - expected_eigenvalues_pi
                )
            )
            < TOL
        ),
        "zero_phase_ratio_matches_self_tested_ratio": (
            abs(modular_ratio(reduced_zero) - expected_ratio_zero) < TOL
        ),
        "pi_phase_ratio_is_three": (
            abs(modular_ratio(reduced_pi) - expected_ratio_pi) < TOL
        ),
        "fixed_factor_modular_ratio_is_not_gauge_invariant": (
            abs(modular_ratio(reduced_zero) - modular_ratio(reduced_pi)) > 2.0
        ),
        "phase_family_matches_exact_ratio_curve": (
            np.max(np.abs(np.array(observed_grid) - np.array(expected_grid)))
            < TOL
        ),
        "phase_family_varies_continuously_between_distinct_ratios": (
            abs(observed_grid[0] - expected_ratio_zero) < TOL
            and abs(observed_grid[-1] - expected_ratio_pi) < TOL
            and all(
                observed_grid[index] >= observed_grid[index + 1] - TOL
                for index in range(len(observed_grid) - 1)
            )
        ),
        "pi_phase_is_nonlocal_relative_to_supplied_output_factor": (
            controlled_z_operator_schmidt_rank == 2
        ),
        "temporal_realizers_share_t1_base_transition": (
            np.max(np.abs(correlated_t1 - anticorrelated_t1)) < TOL
        ),
        "temporal_realizers_share_t2_base_transition": (
            np.max(np.abs(correlated_t2 - anticorrelated_t2)) < TOL
        ),
        "correlated_realizer_has_certain_temporal_equality": (
            abs(equality_correlated - 1.0) < TOL
        ),
        "anticorrelated_realizer_has_impossible_temporal_equality": (
            abs(equality_anticorrelated) < TOL
        ),
    }

    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "claim_id": "HC-DU-079",
        "status": "PASS" if not failures else "FAIL",
        "checks_passed": len(checks) - len(failures),
        "checks_total": len(checks),
        "failures": failures,
        "native_stochastic_object": {
            "configuration_count": 4,
            "initial_configuration_semantics": "(x,y)",
            "target_configuration_semantics": "(a,b)",
            "transition_type": "Gamma[(a,b),(x,y)] = p(a,b|x,y)",
            "conditioning_times": ["0"],
            "target_times": ["0", "1"],
            "division_events": ["0"],
        },
        "exact_counterexample": {
            "phase_family": "D(phi)=diag(1,1,1,exp(i phi))",
            "potential_family": "Theta_phi=D(phi)*sqrt(Gamma)",
            "fixed_factor_reduced_eigenvalues": (
                "1/2 +/- sqrt(6 + 2 cos(phi))/8"
            ),
            "fixed_factor_modular_ratio": (
                "(4 + sqrt(6 + 2 cos(phi)))"
                "/(4 - sqrt(6 + 2 cos(phi)))"
            ),
            "ratio_at_phi_zero": "3 + 2*sqrt(2)",
            "ratio_at_phi_pi": "3",
            "pi_phase_relative_to_supplied_factor": "controlled-Z",
        },
        "numeric_certificate": {
            "tilted_quantum_score": quantum_score,
            "tilted_quantum_maximum": quantum_maximum,
            "maximum_gamma_difference_across_phase_lifts": float(
                np.max(np.abs(gamma_zero - gamma_pi))
            ),
            "maximum_output_probability_difference": float(
                np.max(
                    np.abs(
                        output_probabilities_zero - output_probabilities_pi
                    )
                )
            ),
            "zero_phase_fixed_factor_modular_ratio": modular_ratio(
                reduced_zero
            ),
            "pi_phase_fixed_factor_modular_ratio": modular_ratio(reduced_pi),
            "ratio_curve_maximum_error": float(
                np.max(
                    np.abs(np.array(observed_grid) - np.array(expected_grid))
                )
            ),
            "controlled_z_operator_schmidt_rank": (
                controlled_z_operator_schmidt_rank
            ),
            "same_base_realizer_temporal_equality_probabilities": [
                equality_correlated,
                equality_anticorrelated,
            ],
        },
        "interpretation": {
            "negative": (
                "The complete labeled indivisible-stochastic transition "
                "object does not determine fixed-factor modular data across "
                "its admitted Schur-Hadamard realization freedom."
            ),
            "conditional_positive": (
                "After separately imposing the standard quantum-local Bell "
                "realization class, maximal tilted-CHSH self-testing still "
                "fixes the extracted target spectrum and modular ratio."
            ),
            "multi_time": (
                "Base-time first-order transition families do not determine "
                "intermediate temporal relations or a complete process."
            ),
            "finality_guard": (
                "A division event is an admitted conditioning time, not by "
                "itself a formed, retained, accessible, certified, or final "
                "physical record."
            ),
            "not_established": [
                "physical selection of the configuration semantics or factor",
                "physical selection of quantum locality or Bell instruments",
                "complete multi-time or interventionally complete dynamics",
                "record formation, provenance, access, or regional finality",
                "ambient modular flow, calibrated time, geometry, or ontology",
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
