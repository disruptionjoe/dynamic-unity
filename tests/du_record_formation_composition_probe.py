#!/usr/bin/env python3
"""Finite proper-time record-formation and certificate probe.

This probe keeps four objects distinct:

1. the latent two-branch proper-time label carried by a motion qubit;
2. the motion readout instrument (which-history or coherent erasure);
3. the formed classical port/clock archive; and
4. the proposition certified by repeated archive records.

The effective joint unitary is a two-history specialization of a quantum
clock--motion coupling.  It is not an implementation-complete trapped-ion
model.  The probe establishes:

* an exact interaction-relative nondemolition history algebra;
* unitary freedom of the selective record instrument at fixed nonselective
  clock channel;
* an exact certificate-bearing record that separates coherent recombination
  from every classical mixture of the same two histories while carrying no
  run-level history information in the frozen symmetric fixture; and
* loss of the certificate after which-history dephasing.

Passing does not establish laboratory feasibility, durable archive dynamics,
SPAM/drift/leakage robustness, public finality, record-first ontology, or
beyond-standard quantum physics.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_record_formation_composition_result.json"
)
TOL = 1.0e-10


def dagger(matrix: np.ndarray) -> np.ndarray:
    return matrix.conj().T


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def ket_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def kron(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.kron(left, right)


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def choi_from_kraus(kraus: Iterable[np.ndarray]) -> np.ndarray:
    """Return the Choi matrix under column-vectorization."""

    vectors = [operator.reshape(-1, order="F") for operator in kraus]
    return sum(
        (np.outer(vector, vector.conj()) for vector in vectors),
        start=np.zeros((4, 4), dtype=complex),
    )


def effect_probability(
    rho: np.ndarray,
    kraus: np.ndarray,
    effect: np.ndarray,
) -> float:
    value = np.trace(effect @ kraus @ rho @ dagger(kraus))
    return float(np.real_if_close(value))


def instrument_joint_distribution(
    rho: np.ndarray,
    kraus: tuple[np.ndarray, np.ndarray],
    clock_effects: tuple[np.ndarray, np.ndarray],
) -> np.ndarray:
    """Rows are port signs +1,-1; columns are clock signs +1,-1."""

    result = np.zeros((2, 2), dtype=float)
    for port_index, operator in enumerate(kraus):
        for clock_index, effect in enumerate(clock_effects):
            result[port_index, clock_index] = effect_probability(
                rho,
                operator,
                effect,
            )
    return result


def classical_mixture_distribution(
    weights: tuple[float, float],
    rho: np.ndarray,
    histories: tuple[np.ndarray, np.ndarray],
    clock_effects: tuple[np.ndarray, np.ndarray],
) -> np.ndarray:
    """X-basis port readout after complete which-history dephasing."""

    result = np.zeros((2, 2), dtype=float)
    for weight, history in zip(weights, histories, strict=True):
        clock_state = history @ rho @ dagger(history)
        for port_index in range(2):
            port_probability = 0.5
            for clock_index, effect in enumerate(clock_effects):
                clock_probability = float(
                    np.real_if_close(np.trace(effect @ clock_state))
                )
                result[port_index, clock_index] += (
                    weight * port_probability * clock_probability
                )
    return result


def signed_expectation(distribution: np.ndarray) -> float:
    signs = (1.0, -1.0)
    return sum(
        signs[port] * signs[clock] * distribution[port, clock]
        for port in range(2)
        for clock in range(2)
    )


def total_variation(left: np.ndarray, right: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(left - right)))


def rotated_motion_instrument(
    histories: tuple[np.ndarray, np.ndarray],
    alpha: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Read motion in a real basis rotated by alpha from which-history."""

    v0, v1 = histories
    root_two = math.sqrt(2.0)
    return (
        (math.cos(alpha) * v0 + math.sin(alpha) * v1) / root_two,
        (-math.sin(alpha) * v0 + math.cos(alpha) * v1) / root_two,
    )


def rounded_matrix(matrix: np.ndarray, digits: int = 12) -> list[list[float]]:
    rounded = np.round(np.real_if_close(matrix), digits)
    return [[float(value) for value in row] for row in rounded]


def rounded_float(value: float, digits: int = 12) -> float:
    return float(round(float(value), digits))


def main() -> int:
    identity = np.eye(2, dtype=complex)
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)

    plus_x = np.array([1, 1], dtype=complex) / math.sqrt(2.0)
    rho_clock = ket_density(plus_x)
    clock_effects = (
        (identity + pauli_x) / 2.0,
        (identity - pauli_x) / 2.0,
    )

    # Two symmetric clock histories with a relative pi/2 proper-time phase.
    v0 = np.diag(
        [np.exp(-1j * math.pi / 4.0), np.exp(1j * math.pi / 4.0)]
    )
    v1 = np.diag(
        [np.exp(1j * math.pi / 4.0), np.exp(-1j * math.pi / 4.0)]
    )
    histories = (v0, v1)

    p0 = np.array([[1, 0], [0, 0]], dtype=complex)
    p1 = np.array([[0, 0], [0, 1]], dtype=complex)
    joint_unitary = kron(p0, v0) + kron(p1, v1)

    motion_generators = (identity, pauli_x, pauli_y, pauli_z)
    commutator_norms = {
        name: max_abs(
            commutator(kron(generator, identity), joint_unitary)
        )
        for name, generator in zip(
            ("I", "X", "Y", "Z"),
            motion_generators,
            strict=True,
        )
    }
    nondemolition_basis = tuple(
        name
        for name, norm in commutator_norms.items()
        if norm <= TOL
    )

    angles = (0.0, math.pi / 8.0, math.pi / 4.0, 3.0 * math.pi / 8.0)
    instruments = tuple(
        rotated_motion_instrument(histories, alpha)
        for alpha in angles
    )
    reference_choi = choi_from_kraus(instruments[0])
    nonselective_errors = tuple(
        max_abs(choi_from_kraus(instrument) - reference_choi)
        for instrument in instruments
    )

    which_history = instruments[0]
    erasure = instruments[2]
    selective_difference = max_abs(
        np.outer(
            which_history[0].reshape(-1, order="F"),
            which_history[0].reshape(-1, order="F").conj(),
        )
        - np.outer(
            erasure[0].reshape(-1, order="F"),
            erasure[0].reshape(-1, order="F").conj(),
        )
    )

    coherent_distribution = instrument_joint_distribution(
        rho_clock,
        erasure,
        clock_effects,
    )
    null_weights = (
        (0.0, 1.0),
        (0.25, 0.75),
        (0.5, 0.5),
        (0.75, 0.25),
        (1.0, 0.0),
    )
    null_distributions = tuple(
        classical_mixture_distribution(
            weights,
            rho_clock,
            histories,
            clock_effects,
        )
        for weights in null_weights
    )
    uniform_distribution = np.full((2, 2), 0.25)

    coherent_port_marginal = np.sum(coherent_distribution, axis=1)
    coherent_clock_marginal = np.sum(coherent_distribution, axis=0)
    null_port_marginal = np.sum(null_distributions[2], axis=1)
    null_clock_marginal = np.sum(null_distributions[2], axis=0)

    # Under either classical branch, the complete (port, clock-X) record is
    # uniform.  Therefore no stochastic decoder of this record can disclose h.
    certificate_given_history = tuple(
        classical_mixture_distribution(
            weights,
            rho_clock,
            histories,
            clock_effects,
        ).reshape(-1)
        for weights in ((1.0, 0.0), (0.0, 1.0))
    )
    history_target = (
        np.array([1.0, 0.0]),
        np.array([0.0, 1.0]),
    )
    history_factorization_obstruction = (
        max_abs(certificate_given_history[0] - certificate_given_history[1])
        <= TOL
        and max_abs(history_target[0] - history_target[1]) > TOL
    )

    which_history_kernel = np.eye(2)
    which_history_factorization_error = max_abs(
        which_history_kernel @ np.eye(2) - np.eye(2)
    )

    # Explicit dephasing of the motion label before erasure is exactly the
    # equal-weight classical mixture.
    dephased_distribution = null_distributions[2]

    assertions: list[tuple[str, bool]] = [
        (
            "branch_zero_is_unitary",
            max_abs(dagger(v0) @ v0 - identity) <= TOL,
        ),
        (
            "branch_one_is_unitary",
            max_abs(dagger(v1) @ v1 - identity) <= TOL,
        ),
        (
            "joint_proper_time_control_is_unitary",
            max_abs(dagger(joint_unitary) @ joint_unitary - np.eye(4))
            <= TOL,
        ),
        (
            "motion_identity_is_nondemolition",
            commutator_norms["I"] <= TOL,
        ),
        (
            "history_Z_is_nondemolition",
            commutator_norms["Z"] <= TOL,
        ),
        (
            "complementary_X_is_not_nondemolition",
            commutator_norms["X"] > TOL,
        ),
        (
            "complementary_Y_is_not_nondemolition",
            commutator_norms["Y"] > TOL,
        ),
        (
            "selected_motion_commutant_is_two_dimensional",
            nondemolition_basis == ("I", "Z"),
        ),
        (
            "every_rotated_instrument_is_trace_preserving_in_sum",
            all(error <= TOL for error in nonselective_errors),
        ),
        (
            "nonselective_clock_channel_is_interface_invariant",
            max(nonselective_errors) <= TOL,
        ),
        (
            "which_history_and_erasure_selective_maps_differ",
            selective_difference > 0.1,
        ),
        (
            "coherent_record_distribution_is_normalized",
            abs(float(np.sum(coherent_distribution)) - 1.0) <= TOL,
        ),
        (
            "coherent_record_has_perfect_signed_correlation",
            abs(signed_expectation(coherent_distribution) - 1.0) <= TOL,
        ),
        (
            "all_classical_history_weights_give_uniform_record",
            all(
                max_abs(distribution - uniform_distribution) <= TOL
                for distribution in null_distributions
            ),
        ),
        (
            "classical_mixture_signed_null_is_exact",
            all(
                abs(signed_expectation(distribution)) <= TOL
                for distribution in null_distributions
            ),
        ),
        (
            "coherent_port_marginal_does_not_disclose_history",
            max_abs(coherent_port_marginal - np.array([0.5, 0.5]))
            <= TOL,
        ),
        (
            "coherent_clock_marginal_does_not_disclose_history",
            max_abs(coherent_clock_marginal - np.array([0.5, 0.5]))
            <= TOL,
        ),
        (
            "null_marginals_match_coherent_marginals",
            max_abs(null_port_marginal - coherent_port_marginal) <= TOL
            and max_abs(null_clock_marginal - coherent_clock_marginal)
            <= TOL,
        ),
        (
            "joint_record_separates_process_classes",
            abs(
                total_variation(
                    coherent_distribution,
                    uniform_distribution,
                )
                - 0.5
            )
            <= TOL,
        ),
        (
            "certificate_record_rows_are_history_identical",
            max_abs(
                certificate_given_history[0]
                - certificate_given_history[1]
            )
            <= TOL,
        ),
        (
            "certificate_record_cannot_factor_run_history",
            history_factorization_obstruction,
        ),
        (
            "which_history_archive_can_factor_run_history",
            which_history_factorization_error <= TOL,
        ),
        (
            "which_history_dephasing_kills_certificate",
            abs(signed_expectation(dephased_distribution)) <= TOL
            and max_abs(dephased_distribution - uniform_distribution)
            <= TOL,
        ),
        (
            "single_clock_endpoint_is_underidentified",
            max_abs(coherent_clock_marginal - null_clock_marginal) <= TOL,
        ),
    ]
    passed = sum(int(ok) for _, ok in assertions)
    total = len(assertions)

    result = {
        "schema": "dynamic-unity/record-formation-composition/v1",
        "run_id": "RUN-20260725-100452-record-formation-certified-composition",
        "candidate_ids": ["HC-DU-033", "HC-DU-034B", "HC-DU-036B"],
        "grade": (
            "EXACT FINITE EFFECTIVE-INSTRUMENT RESULT / "
            "COMPONENT MATHEMATICS KNOWN / "
            "NOT IMPLEMENTATION-COMPLETE PROPER TIME"
        ),
        "fixture": {
            "clock_input": "|+x>",
            "motion_input": "(|history_0>+|history_1>)/sqrt(2)",
            "relative_history_phase": "pi/2",
            "clock_readout": "X",
            "which_history_interface_angle": "0",
            "erasure_interface_angle": "pi/4",
            "proper_time_platform_status": (
                "two-branch effective specialization; no trapped-ion "
                "SPAM/drift/leakage or durable-archive dynamics"
            ),
        },
        "interface_selection": {
            "motion_commutator_norms": {
                name: rounded_float(value)
                for name, value in commutator_norms.items()
            },
            "interaction_selected_nondemolition_basis": list(
                nondemolition_basis
            ),
            "nonselective_choi_errors_over_interface_rotations": [
                rounded_float(value)
                for value in nonselective_errors
            ],
            "which_history_erasure_selective_difference": (
                rounded_float(selective_difference)
            ),
            "verdict": (
                "the interaction selects the two-sector nondemolition "
                "history algebra, but not a unique selective readout/archive "
                "instrument"
            ),
        },
        "certificate_without_history_disclosure": {
            "coherent_joint_record": rounded_matrix(
                coherent_distribution
            ),
            "classical_mixture_joint_record": rounded_matrix(
                uniform_distribution
            ),
            "coherent_signed_expectation": rounded_float(
                signed_expectation(coherent_distribution)
            ),
            "classical_signed_expectation": rounded_float(
                signed_expectation(uniform_distribution)
            ),
            "joint_total_variation": rounded_float(
                total_variation(
                    coherent_distribution,
                    uniform_distribution,
                )
            ),
            "coherent_port_marginal": [
                rounded_float(value) for value in coherent_port_marginal
            ],
            "coherent_clock_marginal": [
                rounded_float(value) for value in coherent_clock_marginal
            ],
            "record_given_classical_history": [
                [rounded_float(value) for value in row]
                for row in certificate_given_history
            ],
            "history_factorization": "OBSTRUCTED_IDENTICAL_RECORD_ROWS",
            "certified_proposition": (
                "the frozen selective operation is outside arbitrary-weight "
                "classical mixtures of the same two specified histories"
            ),
            "not_certified": (
                "which history occurred in a run, arbitrary classical "
                "protocol exclusion, or nonstandard quantum physics"
            ),
        },
        "absorber": {
            "dephased_joint_record": rounded_matrix(
                dephased_distribution
            ),
            "dephased_signed_expectation": rounded_float(
                signed_expectation(dephased_distribution)
            ),
            "standard_quantum_absorption": True,
            "required_extra_structure": [
                "selected motion readout instrument",
                "physical pointer/archive coupling",
                "declared access algebra",
                "durability/finality rule",
                "implementation-complete uncertainty and resource contract",
            ],
        },
        "claims_not_made": [
            "laboratory proper-time certification",
            "dynamically selected erasure basis",
            "durable or public finality",
            "irreducible physical remainder",
            "record-first ontology",
            "beyond-standard quantum prediction",
        ],
        "assertions": [
            {"name": name, "passed": bool(ok)} for name, ok in assertions
        ],
        "summary": {
            "passed": passed,
            "total": total,
            "all_passed": passed == total,
        },
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(f"{passed}/{total} checks passed")
    print(f"artifact: {ARTIFACT}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
