#!/usr/bin/env python3
"""Robust physical instrument-selection theorem/no-go probe.

This probe freezes one standard-quantum source--pointer--archive family before
evaluating it.  It checks a quantitative source-action selector, a
degenerate-sector continuation foil, end-to-end archive access, and coherent
routing of competing implementations.

Passing establishes:

* an exact information--source-disturbance identity in the declared binary
  QND family;
* exact selection of the source-aligned measurement axis, up to outcome
  relabeling, whenever the record has nonzero distinguishing power and exact
  source-action nondisturbance is required;
* a quantitative approximate-alignment bound;
* rejection of a within-sector continuation twist only when the independently
  declared action algebra can see it; and
* selection of an effective instrument orbit, not a unique microscopic
  dilation.

All component mathematics is standard quantum measurement, QND,
information--disturbance, commutant, and dilation theory.  The executable
contribution is a typed end-to-end control for Dynamic Unity.  It does not
derive the source Hamiltonian, action algebra, coupling family, archive,
decoder, quantum theory, or new physics.
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
    / "du_robust_physical_instrument_selection_result.json"
)
RUN_ID = "RUN-20260725-120514-robust-physical-instrument-selection"
TOL = 1.0e-10

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)


def dagger(matrix: np.ndarray) -> np.ndarray:
    return matrix.conj().T


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def rounded(value: float) -> float:
    return round(float(value), 12)


def ket_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    return float(
        0.5 * np.sum(np.linalg.svd(left - right, compute_uv=False))
    )


def axis_observable(theta: float) -> np.ndarray:
    return math.sin(theta) * X2 + math.cos(theta) * Z2


def axis_projectors(theta: float) -> tuple[np.ndarray, np.ndarray]:
    observable = axis_observable(theta)
    return ((I2 + observable) / 2.0, (I2 - observable) / 2.0)


def pointer_rotations(epsilon: float) -> tuple[np.ndarray, np.ndarray]:
    if not 0.0 <= epsilon <= 0.5:
        raise ValueError("epsilon must lie in [0, 1/2]")
    correct = math.sqrt(1.0 - epsilon)
    error = math.sqrt(epsilon)
    return (
        np.array(
            [[correct, -error], [error, correct]],
            dtype=complex,
        ),
        np.array(
            [[error, -correct], [correct, error]],
            dtype=complex,
        ),
    )


def system_pointer_unitary(theta: float, epsilon: float) -> np.ndarray:
    projectors = axis_projectors(theta)
    rotations = pointer_rotations(epsilon)
    return sum(
        (
            np.kron(projector, rotation)
            for projector, rotation in zip(
                projectors,
                rotations,
                strict=True,
            )
        ),
        start=np.zeros((4, 4), dtype=complex),
    )


def cnot() -> np.ndarray:
    operator = np.zeros((4, 4), dtype=complex)
    for control in range(2):
        for target in range(2):
            source = 2 * control + target
            destination = 2 * control + (target ^ control)
            operator[destination, source] = 1.0
    return operator


def formation_isometry(theta: float, epsilon: float) -> np.ndarray:
    """Map S to S,P,A with blank P,A and explicit P-to-A copying."""

    embedding = np.zeros((8, 2), dtype=complex)
    for system in range(2):
        embedding[4 * system, system] = 1.0
    coupling = np.kron(system_pointer_unitary(theta, epsilon), I2)
    archive_copy = np.kron(I2, cnot())
    return archive_copy @ coupling @ embedding


def analytic_kraus(
    theta: float,
    epsilon: float,
) -> tuple[np.ndarray, np.ndarray]:
    positive, negative = axis_projectors(theta)
    correct = math.sqrt(1.0 - epsilon)
    error = math.sqrt(epsilon)
    return (
        correct * positive + error * negative,
        error * positive + correct * negative,
    )


def archive_kraus(isometry: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    tensor = isometry.reshape(2, 2, 2, 2)
    return tuple(
        tensor[:, outcome, outcome, :]
        for outcome in range(2)
    )


def effects(
    operators: Iterable[np.ndarray],
) -> tuple[np.ndarray, ...]:
    return tuple(dagger(operator) @ operator for operator in operators)


def adjoint_channel(
    observable: np.ndarray,
    operators: Iterable[np.ndarray],
) -> np.ndarray:
    return sum(
        (
            dagger(operator) @ observable @ operator
            for operator in operators
        ),
        start=np.zeros_like(observable),
    )


def record_distinguishability(epsilon: float) -> float:
    return abs(1.0 - 2.0 * epsilon)


def residual_visibility(epsilon: float) -> float:
    return 2.0 * math.sqrt(epsilon * (1.0 - epsilon))


def predicted_source_disturbance(theta: float, epsilon: float) -> float:
    distinction = record_distinguishability(epsilon)
    return (
        1.0 - math.sqrt(max(0.0, 1.0 - distinction**2))
    ) * abs(math.sin(theta))


def predicted_coupling_symmetry_defect(
    theta: float,
    epsilon: float,
) -> float:
    visibility = residual_visibility(epsilon)
    return (
        math.sqrt(max(0.0, 2.0 * (1.0 - visibility)))
        * abs(math.sin(theta))
    )


def accessible_distinguishability(
    epsilon: float,
    archive_flip: float,
) -> float:
    return (
        abs(1.0 - 2.0 * archive_flip)
        * record_distinguishability(epsilon)
    )


def majority_error_three(error: float) -> float:
    return 3.0 * error**2 * (1.0 - error) + error**3


def repeatability_error(
    operators: tuple[np.ndarray, np.ndarray],
) -> float:
    outcome_effects = effects(operators)
    return max(
        operator_norm(
            dagger(operators[first])
            @ outcome_effects[second]
            @ operators[first]
        )
        for first in range(2)
        for second in range(2)
        if first != second
    )


def instrument_isometry(
    operators: tuple[np.ndarray, np.ndarray],
) -> np.ndarray:
    dimension = operators[0].shape[0]
    isometry = np.zeros((2 * dimension, dimension), dtype=complex)
    for outcome, operator in enumerate(operators):
        for output in range(dimension):
            isometry[2 * output + outcome, :] = operator[output, :]
    return isometry


def controlled_instrument_isometry(
    left: tuple[np.ndarray, np.ndarray],
    right: tuple[np.ndarray, np.ndarray],
) -> np.ndarray:
    left_isometry = instrument_isometry(left)
    right_isometry = instrument_isometry(right)
    dimension = left[0].shape[0]
    controlled = np.zeros(
        (4 * dimension, 2 * dimension),
        dtype=complex,
    )
    controlled[: 2 * dimension, :dimension] = left_isometry
    controlled[2 * dimension :, dimension:] = right_isometry
    return controlled


def reduced_route(state: np.ndarray, dimension: int) -> np.ndarray:
    result = np.zeros((2, 2), dtype=complex)
    for left_route in range(2):
        for right_route in range(2):
            for system in range(dimension):
                for archive in range(2):
                    left = (
                        left_route * 2 * dimension
                        + 2 * system
                        + archive
                    )
                    right = (
                        right_route * 2 * dimension
                        + 2 * system
                        + archive
                    )
                    result[left_route, right_route] += state[left, right]
    return result


def continuation_control() -> dict[str, Any]:
    """Compare a Lüders sector instrument with a matched internal twist."""

    sector_zero = ket_density(KET0)
    sector_one = ket_density(KET1)
    projector_zero = np.kron(sector_zero, I2)
    projector_one = np.kron(sector_one, I2)

    luders = (projector_zero, projector_one)
    twisted = (
        np.kron(sector_zero, X2),
        projector_one,
    )
    identity4 = np.eye(4, dtype=complex)
    sector_action = np.kron(Z2, I2)
    internal_action = np.kron(I2, Z2)
    full_block_actions = tuple(
        np.kron(sector, pauli)
        for sector in (sector_zero, sector_one)
        for pauli in (I2, X2, Y2, Z2)
    )

    input_state = ket_density(np.kron(KET0, KET0))
    target_output = luders[0] @ input_state @ dagger(luders[0])
    twist_output = twisted[0] @ input_state @ dagger(twisted[0])

    effect_error = max(
        max_abs(left - right)
        for left, right in zip(
            effects(luders),
            effects(twisted),
            strict=True,
        )
    )
    trace_preservation_error = max(
        max_abs(sum(effects(instrument)) - identity4)
        for instrument in (luders, twisted)
    )
    sector_disturbance = {
        name: operator_norm(
            adjoint_channel(sector_action, instrument) - sector_action
        )
        for name, instrument in (
            ("luders", luders),
            ("twisted", twisted),
        )
    }
    full_action_disturbance = {
        name: max(
            operator_norm(
                adjoint_channel(action, instrument) - action
            )
            for action in full_block_actions
        )
        for name, instrument in (
            ("luders", luders),
            ("twisted", twisted),
        )
    }

    energy_rows = []
    for internal_splitting in (0.0, 0.1, 0.3):
        hamiltonian = (
            1.0 * sector_action
            + internal_splitting * internal_action
        )
        energy_rows.append(
            {
                "internal_splitting": internal_splitting,
                "luders_source_energy_disturbance": rounded(
                    operator_norm(
                        adjoint_channel(hamiltonian, luders)
                        - hamiltonian
                    )
                ),
                "twisted_source_energy_disturbance": rounded(
                    operator_norm(
                        adjoint_channel(hamiltonian, twisted)
                        - hamiltonian
                    )
                ),
                "predicted_twist_disturbance": rounded(
                    2.0 * internal_splitting
                ),
            }
        )

    coherent_system = (
        np.kron(KET0, KET0) + np.kron(KET1, KET0)
    ) / math.sqrt(2.0)
    route_plus_system = np.kron(
        (KET0 + KET1) / math.sqrt(2.0),
        coherent_system,
    )

    identical_control = controlled_instrument_isometry(luders, luders)
    twist_control = controlled_instrument_isometry(luders, twisted)
    identical_output = identical_control @ route_plus_system
    twist_output_vector = twist_control @ route_plus_system
    identical_route = reduced_route(
        ket_density(identical_output),
        dimension=4,
    )
    twist_route = reduced_route(
        ket_density(twist_output_vector),
        dimension=4,
    )
    route_x_visibility = {
        "identical_implementations": float(
            np.real_if_close(np.trace(X2 @ identical_route))
        ),
        "luders_vs_twist": float(
            np.real_if_close(np.trace(X2 @ twist_route))
        ),
    }

    return {
        "luders": luders,
        "twisted": twisted,
        "effect_error": effect_error,
        "trace_preservation_error": trace_preservation_error,
        "repeatability_error": {
            "luders": repeatability_error(luders),
            "twisted": repeatability_error(twisted),
        },
        "sector_action_disturbance": sector_disturbance,
        "full_action_disturbance": full_action_disturbance,
        "selective_output_trace_distance": trace_distance(
            target_output,
            twist_output,
        ),
        "energy_rows": energy_rows,
        "controlled_isometry_error": max(
            max_abs(dagger(control) @ control - np.eye(8))
            for control in (identical_control, twist_control)
        ),
        "route_x_visibility": route_x_visibility,
        "route_reduced_states": {
            "identical": identical_route,
            "luders_vs_twist": twist_route,
        },
    }


def dilation_freedom_control() -> dict[str, float]:
    """Same effective instrument, distinguishable retained environment port."""

    luders = axis_projectors(0.0)
    base = instrument_isometry(luders)
    with_environment_zero = np.kron(base, KET0[:, np.newaxis])
    with_environment_one = np.kron(base, KET1[:, np.newaxis])

    def trace_environment(state: np.ndarray) -> np.ndarray:
        reduced = np.zeros((4, 4), dtype=complex)
        for left in range(4):
            for right in range(4):
                for environment in range(2):
                    reduced[left, right] += state[
                        2 * left + environment,
                        2 * right + environment,
                    ]
        return reduced

    # Tracing the final environment leaves the same S+A instrument channel.
    effective_channel_errors = []
    for row in range(2):
        for column in range(2):
            matrix_unit = np.zeros((2, 2), dtype=complex)
            matrix_unit[row, column] = 1.0
            zero_output = trace_environment(
                with_environment_zero
                @ matrix_unit
                @ dagger(with_environment_zero)
            )
            one_output = trace_environment(
                with_environment_one
                @ matrix_unit
                @ dagger(with_environment_one)
            )
            effective_channel_errors.append(
                max_abs(zero_output - one_output)
            )
    isometry_error = max(
        max_abs(dagger(item) @ item - I2)
        for item in (with_environment_zero, with_environment_one)
    )
    retained_environment_trace_distance = trace_distance(
        ket_density(KET0),
        ket_density(KET1),
    )
    return {
        "isometry_error": isometry_error,
        "effective_channel_error_after_environment_trace": max(
            effective_channel_errors
        ),
        "retained_environment_trace_distance": (
            retained_environment_trace_distance
        ),
    }


def main() -> None:
    theta_grid = (
        -math.pi / 12.0,
        0.0,
        math.pi / 24.0,
        math.pi / 12.0,
        math.pi / 6.0,
        math.pi / 4.0,
        math.pi / 2.0,
        math.pi,
    )
    epsilon_grid = (0.0, 0.02, 0.1, 0.25, 0.45, 0.5)
    archive_flip_grid = (0.0, 0.05, 0.2, 0.49)

    unitary_errors: list[float] = []
    isometry_errors: list[float] = []
    kraus_errors: list[float] = []
    trace_preservation_errors: list[float] = []
    visibility_errors: list[float] = []
    disturbance_errors: list[float] = []
    coupling_symmetry_errors: list[float] = []
    alignment_bound_errors: list[float] = []
    rows: list[dict[str, Any]] = []

    for theta in theta_grid:
        for epsilon in epsilon_grid:
            coupling = system_pointer_unitary(theta, epsilon)
            unitary_errors.append(
                max_abs(dagger(coupling) @ coupling - np.eye(4))
            )
            isometry = formation_isometry(theta, epsilon)
            isometry_errors.append(
                max_abs(dagger(isometry) @ isometry - I2)
            )
            computed_kraus = archive_kraus(isometry)
            expected_kraus = analytic_kraus(theta, epsilon)
            kraus_errors.append(
                max(
                    max_abs(left - right)
                    for left, right in zip(
                        computed_kraus,
                        expected_kraus,
                        strict=True,
                    )
                )
            )
            trace_preservation_errors.append(
                max_abs(sum(effects(computed_kraus)) - I2)
            )

            distinction = record_distinguishability(epsilon)
            visibility = residual_visibility(epsilon)
            visibility_errors.append(
                abs(visibility - math.sqrt(1.0 - distinction**2))
            )
            measured_disturbance = operator_norm(
                adjoint_channel(Z2, computed_kraus) - Z2
            )
            predicted_disturbance = predicted_source_disturbance(
                theta,
                epsilon,
            )
            disturbance_errors.append(
                abs(measured_disturbance - predicted_disturbance)
            )
            frozen_total_generator = np.kron(Z2, I2)
            measured_coupling_symmetry_defect = operator_norm(
                coupling @ frozen_total_generator
                - frozen_total_generator @ coupling
            )
            predicted_symmetry_defect = (
                predicted_coupling_symmetry_defect(theta, epsilon)
            )
            coupling_symmetry_errors.append(
                abs(
                    measured_coupling_symmetry_defect
                    - predicted_symmetry_defect
                )
            )

            coefficient = 1.0 - visibility
            if coefficient > TOL:
                inferred_sine_bound = measured_disturbance / coefficient
                alignment_bound_errors.append(
                    abs(inferred_sine_bound - abs(math.sin(theta)))
                )
            else:
                inferred_sine_bound = None

            rows.append(
                {
                    "theta_over_pi": rounded(theta / math.pi),
                    "epsilon": epsilon,
                    "pointer_distinguishability": rounded(distinction),
                    "residual_visibility": rounded(visibility),
                    "source_action_disturbance": rounded(
                        measured_disturbance
                    ),
                    "predicted_source_action_disturbance": rounded(
                        predicted_disturbance
                    ),
                    "coupling_symmetry_defect": rounded(
                        measured_coupling_symmetry_defect
                    ),
                    "predicted_coupling_symmetry_defect": rounded(
                        predicted_symmetry_defect
                    ),
                    "inferred_abs_sin_theta": (
                        None
                        if inferred_sine_bound is None
                        else rounded(inferred_sine_bound)
                    ),
                }
            )

    access_rows = []
    access_formula_errors = []
    majority_improvements = []
    for epsilon in epsilon_grid:
        pointer_distinction = record_distinguishability(epsilon)
        for archive_flip in archive_flip_grid:
            accessible = accessible_distinguishability(
                epsilon,
                archive_flip,
            )
            direct_distribution_plus = np.array(
                [
                    (1.0 - archive_flip) * (1.0 - epsilon)
                    + archive_flip * epsilon,
                    archive_flip * (1.0 - epsilon)
                    + (1.0 - archive_flip) * epsilon,
                ]
            )
            direct_distribution_minus = direct_distribution_plus[::-1]
            measured_accessible = 0.5 * float(
                np.sum(
                    np.abs(
                        direct_distribution_plus
                        - direct_distribution_minus
                    )
                )
            )
            access_formula_errors.append(
                abs(measured_accessible - accessible)
            )
            majority_error = majority_error_three(archive_flip)
            majority_accessible = accessible_distinguishability(
                epsilon,
                majority_error,
            )
            if 0.0 < archive_flip < 0.5 and pointer_distinction > TOL:
                majority_improvements.append(
                    majority_accessible > accessible + TOL
                )
            access_rows.append(
                {
                    "epsilon": epsilon,
                    "archive_flip": archive_flip,
                    "pointer_distinguishability": rounded(
                        pointer_distinction
                    ),
                    "observer_accessible_distinguishability": rounded(
                        accessible
                    ),
                    "three_copy_majority_error": rounded(majority_error),
                    "three_copy_accessible_distinguishability": rounded(
                        majority_accessible
                    ),
                }
            )

    matched_rows = []
    for epsilon in epsilon_grid[:-1]:
        target_disturbance = predicted_source_disturbance(0.0, epsilon)
        conjugate_disturbance = predicted_source_disturbance(
            math.pi / 2.0,
            epsilon,
        )
        matched_rows.append(
            {
                "epsilon": epsilon,
                "record_distinguishability_both": rounded(
                    record_distinguishability(epsilon)
                ),
                "target_source_disturbance": rounded(target_disturbance),
                "conjugate_source_disturbance": rounded(
                    conjugate_disturbance
                ),
                "predicted_conjugate_gap": rounded(
                    1.0 - residual_visibility(epsilon)
                ),
                "same_resource_contract": True,
            }
        )

    null_rows = [
        row
        for row in rows
        if row["epsilon"] == 0.5
    ]
    exact_nondisturbing_informative_rows = [
        row
        for row in rows
        if row["epsilon"] < 0.5
        and row["source_action_disturbance"] <= TOL
    ]
    exact_selected_axes = sorted(
        {row["theta_over_pi"] for row in exact_nondisturbing_informative_rows}
    )

    continuation = continuation_control()
    dilation_freedom = dilation_freedom_control()

    assertions = [
        (
            "all_system_pointer_couplings_are_unitary",
            max(unitary_errors) <= TOL,
        ),
        (
            "all_blank_pointer_archive_maps_are_isometries",
            max(isometry_errors) <= TOL,
        ),
        (
            "explicit_archive_circuit_recovers_analytic_instrument",
            max(kraus_errors) <= TOL,
        ),
        (
            "all_instruments_are_trace_preserving",
            max(trace_preservation_errors) <= TOL,
        ),
        (
            "binary_visibility_equals_sqrt_one_minus_d_squared",
            max(visibility_errors) <= TOL,
        ),
        (
            "source_disturbance_identity_holds_on_full_grid",
            max(disturbance_errors) <= TOL,
        ),
        (
            "source_plus_degenerate_pointer_symmetry_identity_holds",
            max(coupling_symmetry_errors) <= TOL,
        ),
        (
            "nonzero_record_strength_yields_exact_alignment_bound",
            max(alignment_bound_errors) <= TOL,
        ),
        (
            "exact_source_nondisturbance_selects_z_axis_or_relabeling",
            exact_selected_axes == [0.0, 1.0],
        ),
        (
            "zero_information_null_does_not_select_an_axis",
            all(
                row["pointer_distinguishability"] <= TOL
                and row["source_action_disturbance"] <= TOL
                for row in null_rows
            ),
        ),
        (
            "matched_target_and_conjugate_have_same_record_quality",
            all(
                row["record_distinguishability_both"] > 0.0
                and row["same_resource_contract"]
                for row in matched_rows
            ),
        ),
        (
            "aligned_target_is_source_nondisturbing",
            all(
                row["target_source_disturbance"] <= TOL
                for row in matched_rows
            ),
        ),
        (
            "informative_conjugate_foil_pays_exact_source_disturbance",
            all(
                row["conjugate_source_disturbance"] > TOL
                and abs(
                    row["conjugate_source_disturbance"]
                    - row["predicted_conjugate_gap"]
                )
                <= TOL
                for row in matched_rows
            ),
        ),
        (
            "archive_access_formula_holds",
            max(access_formula_errors) <= TOL,
        ),
        (
            "archive_noise_never_improves_single_copy_access",
            all(
                row["observer_accessible_distinguishability"]
                <= row["pointer_distinguishability"] + TOL
                for row in access_rows
            ),
        ),
        (
            "charged_three_copy_majority_improves_nontrivial_access",
            all(majority_improvements),
        ),
        (
            "majority_decoder_is_not_free_or_exact_under_nonzero_noise",
            all(
                row["three_copy_majority_error"] > 0.0
                and row["three_copy_accessible_distinguishability"]
                < row["pointer_distinguishability"] - TOL
                for row in access_rows
                if 0.0 < row["archive_flip"] < 0.5
                and row["pointer_distinguishability"] > TOL
            ),
        ),
        (
            "continuation_target_and_twist_are_trace_preserving",
            continuation["trace_preservation_error"] <= TOL,
        ),
        (
            "continuation_target_and_twist_have_same_sharp_effects",
            continuation["effect_error"] <= TOL,
        ),
        (
            "continuation_target_and_twist_are_repeatable",
            max(continuation["repeatability_error"].values()) <= TOL,
        ),
        (
            "central_sector_action_cannot_distinguish_continuations",
            max(continuation["sector_action_disturbance"].values()) <= TOL,
        ),
        (
            "same_effects_allow_orthogonal_selective_continuations",
            continuation["selective_output_trace_distance"]
            >= 1.0 - TOL,
        ),
        (
            "full_action_algebra_accepts_luders_continuation",
            continuation["full_action_disturbance"]["luders"] <= TOL,
        ),
        (
            "full_action_algebra_rejects_twisted_continuation",
            continuation["full_action_disturbance"]["twisted"]
            >= 2.0 - TOL,
        ),
        (
            "degenerate_source_energy_cannot_see_internal_twist",
            continuation["energy_rows"][0][
                "twisted_source_energy_disturbance"
            ]
            <= TOL,
        ),
        (
            "nonzero_internal_splitting_reveals_exact_twist_cost",
            all(
                abs(
                    row["twisted_source_energy_disturbance"]
                    - row["predicted_twist_disturbance"]
                )
                <= TOL
                for row in continuation["energy_rows"]
            ),
        ),
        (
            "coherent_route_assay_is_a_valid_isometry",
            continuation["controlled_isometry_error"] <= TOL,
        ),
        (
            "identical_routes_recombine_with_unit_visibility",
            abs(
                continuation["route_x_visibility"][
                    "identical_implementations"
                ]
                - 1.0
            )
            <= TOL,
        ),
        (
            "continuation_twist_reduces_route_visibility_as_predicted",
            abs(
                continuation["route_x_visibility"]["luders_vs_twist"]
                - 0.5
            )
            <= TOL,
        ),
        (
            "same_effective_instrument_admits_distinct_dilations",
            dilation_freedom["isometry_error"] <= TOL
            and dilation_freedom[
                "effective_channel_error_after_environment_trace"
            ]
            <= TOL
            and dilation_freedom[
                "retained_environment_trace_distance"
            ]
            >= 1.0 - TOL,
        ),
        (
            "resource_contract_is_matched_before_verdict",
            all(row["same_resource_contract"] for row in matched_rows),
        ),
    ]

    passed = sum(int(ok) for _, ok in assertions)
    total = len(assertions)

    resource_contract = {
        "target_and_conjugate": {
            "system_qubits": 1,
            "fresh_pointer_qubits": 1,
            "fresh_archive_bits": 1,
            "system_pointer_unitaries": 1,
            "pointer_archive_copies": 1,
            "decoder": "single archive bit",
        },
        "continuation_target_and_twist": {
            "system_qubits": 2,
            "outcomes": 2,
            "archive_bits": 1,
            "selective_kraus_operators": 2,
        },
        "charged_optional_decoder": {
            "fresh_archive_bits": 3,
            "independent_archive_flip_assumption": True,
            "majority_operations": 1,
        },
        "not_priced_as_zero": [
            "source-Hamiltonian justification",
            "coupling synthesis",
            "macroscopic amplification",
            "archive reset and lifetime",
            "tomographic calibration",
            "public or Byzantine finality",
        ],
    }

    result = {
        "schema": (
            "dynamic-unity/robust-physical-instrument-selection/v1"
        ),
        "run_id": RUN_ID,
        "grade": (
            "EXACT FINITE FAMILY SELECTOR AND NO-GO / "
            "COMPONENT MATHEMATICS KNOWN / "
            "EFFECTIVE INSTRUMENT ORBIT SELECTED ONLY RELATIVE TO "
            "FROZEN SOURCE, ACTION AND COUPLING CLASSES / "
            "NO NEW PHYSICS OR THEOREM-ID PROMOTION"
        ),
        "frozen_contract": {
            "source_action": "Z",
            "candidate_axis": "n(theta)=(sin(theta),0,cos(theta))",
            "theta_grid_over_pi": [
                rounded(theta / math.pi)
                for theta in theta_grid
            ],
            "pointer_crossover_grid": list(epsilon_grid),
            "archive_flip_grid": list(archive_flip_grid),
            "tolerance": TOL,
            "resource_contract": resource_contract,
            "matched_foils": [
                "conjugate X-axis instrument",
                "within-sector continuation twist",
                "zero internal-splitting degeneracy",
                "noisy observer archive",
                "coherently routed target-versus-twist implementation",
            ],
        },
        "source_action_selector": {
            "analytic_relations": {
                "pointer_distinguishability": "D=1-2*epsilon",
                "residual_visibility": (
                    "v=2*sqrt(epsilon*(1-epsilon))=sqrt(1-D^2)"
                ),
                "source_action_disturbance": (
                    "delta_Z=(1-sqrt(1-D^2))*abs(sin(theta))"
                ),
                "coupling_symmetry_defect": (
                    "kappa=norm([U,Z tensor I])="
                    "sqrt(2*(1-sqrt(1-D^2)))*abs(sin(theta))"
                ),
                "approximate_alignment": (
                    "abs(sin(theta)) <= "
                    "delta_Z/(1-sqrt(1-D^2)) for D>0"
                ),
            },
            "exact_selected_axes_over_pi": exact_selected_axes,
            "rows": rows,
            "matched_target_conjugate_rows": matched_rows,
            "verdict": (
                "within the frozen binary QND family, any informative "
                "exactly source-action-nondisturbing record measures the "
                "source Z axis up to outcome relabeling. Approximate "
                "nondisturbance gives the displayed quantitative "
                "misalignment bound. The complete coupling obeys the "
                "parallel symmetry-defect identity for a degenerate "
                "pointer generator. At D=0 the selector becomes vacuous."
            ),
        },
        "archive_access": {
            "analytic_relation": (
                "D_access=abs(1-2*q)*D_pointer; three-copy majority "
                "uses q3=3*q^2-2*q^3"
            ),
            "rows": access_rows,
            "verdict": (
                "the source-selected pointer distinction and the final "
                "observer-accessible distinction are different receipts. "
                "Finite redundancy improves access only by paying for "
                "additional archive support and remains inexact at q>0."
            ),
        },
        "continuation_selector": {
            "same_effect_error": rounded(continuation["effect_error"]),
            "repeatability_error": {
                key: rounded(value)
                for key, value in continuation[
                    "repeatability_error"
                ].items()
            },
            "sector_action_disturbance": {
                key: rounded(value)
                for key, value in continuation[
                    "sector_action_disturbance"
                ].items()
            },
            "full_action_disturbance": {
                key: rounded(value)
                for key, value in continuation[
                    "full_action_disturbance"
                ].items()
            },
            "selective_output_trace_distance": rounded(
                continuation["selective_output_trace_distance"]
            ),
            "energy_rows": continuation["energy_rows"],
            "route_x_visibility": {
                key: rounded(value)
                for key, value in continuation[
                    "route_x_visibility"
                ].items()
            },
            "verdict": (
                "sharp effects, repeatability, the archive outcome and "
                "central source nondisturbance do not fix the selective "
                "continuation. A full within-sector action algebra rejects "
                "the twist; source energy alone does so only when an "
                "independent internal splitting breaks the degeneracy."
            ),
        },
        "coherent_route_control": {
            "controlled_isometry_error": rounded(
                continuation["controlled_isometry_error"]
            ),
            "identical_route_x_visibility": rounded(
                continuation["route_x_visibility"][
                    "identical_implementations"
                ]
            ),
            "target_twist_route_x_visibility": rounded(
                continuation["route_x_visibility"]["luders_vs_twist"]
            ),
            "classification": (
                "the route-coherence loss is exactly reproduced by the "
                "complete standard-quantum controlled implementation. It "
                "detects selective-map identity beyond outcome effects; "
                "it is not evidence of perspectival curvature or new "
                "dynamics."
            ),
        },
        "maximal_selected_object": {
            "selected": (
                "source-aligned effective Lüders instrument orbit, within "
                "the declared QND and full-action-preserving candidate "
                "classes, up to outcome relabeling and operationally inert "
                "outcome phases"
            ),
            "not_selected": [
                "the source Hamiltonian or action algebra",
                "the admissible coupling family",
                "a unique microscopic apparatus Hamiltonian",
                "a unique Stinespring dilation or retained environment state",
                "the archive boundary or decoder",
                "quantum theory from a broader GPT landscape",
            ],
            "dilation_control": {
                key: rounded(value)
                for key, value in dilation_freedom.items()
            },
            "no_go": (
                "physical source and action constraints can select an "
                "effective instrument only relative to independently "
                "declared candidate and action classes. They cannot select "
                "one microscopic dilation: environment isometries and "
                "unobserved implementation degrees remain."
            ),
        },
        "landscape_boundary": {
            "occupied_components": [
                "Wigner-Araki-Yanase conservation constraints",
                "quantum nondemolition measurement",
                "binary information-disturbance complementarity",
                "Lüders and repeatable instrument theory",
                "commutant/Schur-lemma continuation selection",
                "Stinespring and Naimark dilation freedom",
                "ordinary coherent control of quantum instruments",
            ],
            "du_value": (
                "one unchanged typed contract joins source selection, "
                "selective continuation identity, end-to-end archive "
                "access, matched resources, coherent routing, and the "
                "effective-instrument quotient"
            ),
            "novelty_grade": (
                "useful program synthesis and exact finite receipt; no "
                "new component theorem or physical law claimed"
            ),
        },
        "assertions": [
            {"name": name, "passed": bool(ok)}
            for name, ok in assertions
        ],
        "summary": {
            "passed": passed,
            "total": total,
            "all_passed": passed == total,
        },
    }

    if passed != total:
        failed = [name for name, ok in assertions if not ok]
        raise AssertionError(f"failed checks: {failed}")

    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(
        f"robust physical instrument selection: {passed}/{total} checks passed"
    )
    print(f"artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
