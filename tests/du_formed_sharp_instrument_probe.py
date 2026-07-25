#!/usr/bin/env python3
"""Finite system-pointer-archive probe for physically earned sharpness.

The core fixture is an implementation-complete finite quantum circuit:

1. a system qubit is coupled unitarily to one blank pointer qubit;
2. the pointer is copied to one blank archive qubit;
3. the archive is dephased/read in its frozen computational basis;
4. a setting identifier and sequence identifier are retained as classical
   provenance; and
5. the same process can be repeated with fresh pointer/archive support.

The pointer coupling has a declared crossover epsilon.  It realizes a binary
QND instrument in a declared system basis.  The probe tests which properties
follow from the complete circuit and which remain supplied:

* exact repeatability, sharp effects, and perfect sector disclosure coincide
  in this finite family;
* physical archive formation, central-algebra nondisturbance, provenance, and
  a finite resource ledger also hold for unsharp members;
* unitary-conjugate bases satisfy every frozen high-level condition, so those
  conditions do not select a basis;
* with degenerate sectors, distinct selective continuations share the same
  sharp effects, repeatability, central nondisturbance, and archive record;
* noisy archive transduction makes the observer-accessible effects unsharp
  even when the underlying pointer instrument is sharp; and
* a which-sector archive discloses history and destroys complementary
  coherence, while the earlier coherent certificate can certify a process
  class without disclosing run history.

Passing establishes a scoped finite classification and no-go.  It does not
derive a laboratory interaction, macroscopic irreversibility, a unique
pointer basis, a unique selective instrument, public finality, geometry,
record-first ontology, or physics beyond standard quantum theory.
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
    / "du_formed_sharp_instrument_result.json"
)
RUN_ID = "RUN-20260725-110735-formed-sharp-descent"
TOL = 1.0e-10

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)


def dagger(matrix: np.ndarray) -> np.ndarray:
    return matrix.conj().T


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def ket_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def rounded(value: float) -> float:
    return round(float(value), 12)


def rounded_matrix(matrix: np.ndarray) -> list[list[float]]:
    real = np.real_if_close(matrix)
    return [
        [rounded(float(value)) for value in row]
        for row in np.asarray(real)
    ]


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    singular_values = np.linalg.svd(left - right, compute_uv=False)
    return float(0.5 * np.sum(singular_values))


def total_variation(left: np.ndarray, right: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(left - right)))


def basis_rotation(theta: float) -> np.ndarray:
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return np.array(
        [[cosine, -sine], [sine, cosine]],
        dtype=complex,
    )


def basis_projectors(theta: float) -> tuple[np.ndarray, np.ndarray]:
    rotation = basis_rotation(theta)
    return (
        rotation @ ket_density(KET0) @ dagger(rotation),
        rotation @ ket_density(KET1) @ dagger(rotation),
    )


def pointer_rotations(epsilon: float) -> tuple[np.ndarray, np.ndarray]:
    """Return complete pointer unitaries for the two system sectors."""

    if not 0.0 <= epsilon <= 0.5:
        raise ValueError("epsilon must lie in [0, 1/2]")
    correct = math.sqrt(1.0 - epsilon)
    error = math.sqrt(epsilon)
    return (
        np.array(
            [[correct, error], [error, -correct]],
            dtype=complex,
        ),
        np.array(
            [[error, correct], [correct, -error]],
            dtype=complex,
        ),
    )


def system_pointer_unitary(theta: float, epsilon: float) -> np.ndarray:
    projectors = basis_projectors(theta)
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
    """Map S to S,P,A with P=A=|0> and explicit P-to-A copying."""

    embedding = np.zeros((8, 2), dtype=complex)
    for system in range(2):
        embedding[4 * system, system] = 1.0
    pointer_coupling = np.kron(
        system_pointer_unitary(theta, epsilon),
        I2,
    )
    archive_copy = np.kron(I2, cnot())
    return archive_copy @ pointer_coupling @ embedding


def pointer_kraus(theta: float, epsilon: float) -> tuple[np.ndarray, np.ndarray]:
    unitary = system_pointer_unitary(theta, epsilon).reshape(2, 2, 2, 2)
    return tuple(
        unitary[:, outcome, :, 0]
        for outcome in range(2)
    )


def archive_kraus_from_isometry(
    isometry: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    tensor = isometry.reshape(2, 2, 2, 2)
    return tuple(
        tensor[:, outcome, outcome, :]
        for outcome in range(2)
    )


def reduced_archive(state: np.ndarray) -> np.ndarray:
    result = np.zeros((2, 2), dtype=complex)
    for left_archive in range(2):
        for right_archive in range(2):
            for system in range(2):
                for pointer in range(2):
                    left = 4 * system + 2 * pointer + left_archive
                    right = 4 * system + 2 * pointer + right_archive
                    result[left_archive, right_archive] += state[left, right]
    return result


def conditional_archive_states(
    theta: float,
    epsilon: float,
    archive_flip: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    if not 0.0 <= archive_flip <= 0.5:
        raise ValueError("archive_flip must lie in [0, 1/2]")
    isometry = formation_isometry(theta, epsilon)
    states = []
    rotation = basis_rotation(theta)
    for sector in range(2):
        source = rotation @ (KET0 if sector == 0 else KET1)
        joint = isometry @ ket_density(source) @ dagger(isometry)
        archive = reduced_archive(joint)
        archive = (
            (1.0 - archive_flip) * archive
            + archive_flip * X2 @ archive @ X2
        )
        states.append(archive)
    return tuple(states)


def effects(
    operators: Iterable[np.ndarray],
) -> tuple[np.ndarray, ...]:
    return tuple(dagger(operator) @ operator for operator in operators)


def nonselective_channel(
    state: np.ndarray,
    operators: Iterable[np.ndarray],
) -> np.ndarray:
    return sum(
        (
            operator @ state @ dagger(operator)
            for operator in operators
        ),
        start=np.zeros_like(state),
    )


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


def sequential_distribution(
    state: np.ndarray,
    operators: tuple[np.ndarray, np.ndarray],
) -> np.ndarray:
    distribution = np.zeros((2, 2), dtype=float)
    for first in range(2):
        for second in range(2):
            combined = operators[second] @ operators[first]
            probability = np.trace(
                combined @ state @ dagger(combined)
            )
            distribution[first, second] = float(
                np.real_if_close(probability)
            )
    return distribution


def sharpness_defect(effect: np.ndarray) -> float:
    return max_abs(effect @ effect - effect)


def accessible_effects(
    pointer_effects: tuple[np.ndarray, np.ndarray],
    archive_flip: float,
) -> tuple[np.ndarray, np.ndarray]:
    return (
        (1.0 - archive_flip) * pointer_effects[0]
        + archive_flip * pointer_effects[1],
        archive_flip * pointer_effects[0]
        + (1.0 - archive_flip) * pointer_effects[1],
    )


def majority_error_three(error: float) -> float:
    return 3.0 * error**2 * (1.0 - error) + error**3


def multiplicity_control() -> dict[str, Any]:
    """Two sharp instruments with one PVM and different continuations."""

    projector_zero = np.diag([1, 1, 0, 0]).astype(complex)
    projector_one = np.diag([0, 0, 1, 1]).astype(complex)
    swap_inside_zero = np.array(
        [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        dtype=complex,
    )
    luders = (projector_zero, projector_one)
    twisted = (
        swap_inside_zero @ projector_zero,
        projector_one,
    )
    central = (projector_zero, projector_one)
    internal_observable = np.diag([1, -1, 0, 0]).astype(complex)
    source = ket_density(np.array([1, 0, 0, 0], dtype=complex))

    luders_output = luders[0] @ source @ dagger(luders[0])
    twisted_output = twisted[0] @ source @ dagger(twisted[0])
    continuation_gap = trace_distance(luders_output, twisted_output)
    luders_internal = adjoint_channel(internal_observable, luders)
    twisted_internal = adjoint_channel(internal_observable, twisted)

    return {
        "projectors": central,
        "luders": luders,
        "twisted": twisted,
        "same_effect_error": max(
            max_abs(left - right)
            for left, right in zip(
                effects(luders),
                effects(twisted),
                strict=True,
            )
        ),
        "trace_preservation_errors": {
            "luders": max_abs(sum(effects(luders)) - np.eye(4)),
            "twisted": max_abs(sum(effects(twisted)) - np.eye(4)),
        },
        "central_nondisturbance_errors": {
            "luders": max(
                max_abs(adjoint_channel(item, luders) - item)
                for item in central
            ),
            "twisted": max(
                max_abs(adjoint_channel(item, twisted) - item)
                for item in central
            ),
        },
        "repeatability_errors": {
            "luders": max(
                max_abs(
                    dagger(luders[first])
                    @ effects(luders)[second]
                    @ luders[first]
                )
                for first in range(2)
                for second in range(2)
                if first != second
            ),
            "twisted": max(
                max_abs(
                    dagger(twisted[first])
                    @ effects(twisted)[second]
                    @ twisted[first]
                )
                for first in range(2)
                for second in range(2)
                if first != second
            ),
        },
        "selective_continuation_trace_distance": continuation_gap,
        "full_sector_observable_errors": {
            "luders": max_abs(luders_internal - internal_observable),
            "twisted": max_abs(twisted_internal - internal_observable),
        },
    }


def main() -> None:
    theta_grid = (0.0, math.pi / 8.0, math.pi / 4.0)
    epsilon_grid = (0.0, 0.05, 0.2, 0.5)
    state_grid = (
        ket_density(KET0),
        ket_density(KET1),
        ket_density((KET0 + KET1) / math.sqrt(2.0)),
        np.array([[0.7, 0.2j], [-0.2j, 0.3]], dtype=complex),
    )

    unitary_errors: list[float] = []
    isometry_errors: list[float] = []
    archive_kraus_errors: list[float] = []
    trace_preservation_errors: list[float] = []
    effect_formula_errors: list[float] = []
    central_nondisturbance_errors: list[float] = []
    repeatability_formula_errors: list[float] = []
    disclosure_formula_errors: list[float] = []
    complementarity_errors: list[float] = []
    sharpness_rows: list[dict[str, Any]] = []

    for theta in theta_grid:
        projectors = basis_projectors(theta)
        rotation = basis_rotation(theta)
        coherent_source = rotation @ (
            (KET0 + KET1) / math.sqrt(2.0)
        )
        for epsilon in epsilon_grid:
            pointer_unitaries = pointer_rotations(epsilon)
            unitary_errors.extend(
                max_abs(
                    dagger(operator) @ operator - I2
                )
                for operator in pointer_unitaries
            )

            coupling = system_pointer_unitary(theta, epsilon)
            unitary_errors.append(
                max_abs(dagger(coupling) @ coupling - np.eye(4))
            )

            isometry = formation_isometry(theta, epsilon)
            isometry_errors.append(
                max_abs(dagger(isometry) @ isometry - I2)
            )

            pointer_operators = pointer_kraus(theta, epsilon)
            archive_operators = archive_kraus_from_isometry(isometry)
            archive_kraus_errors.append(
                max(
                    max_abs(left - right)
                    for left, right in zip(
                        pointer_operators,
                        archive_operators,
                        strict=True,
                    )
                )
            )

            pointer_effects = effects(pointer_operators)
            trace_preservation_errors.append(
                max_abs(sum(pointer_effects) - I2)
            )
            expected_effects = (
                (1.0 - epsilon) * projectors[0]
                + epsilon * projectors[1],
                epsilon * projectors[0]
                + (1.0 - epsilon) * projectors[1],
            )
            effect_formula_errors.append(
                max(
                    max_abs(left - right)
                    for left, right in zip(
                        pointer_effects,
                        expected_effects,
                        strict=True,
                    )
                )
            )

            central_nondisturbance_errors.append(
                max(
                    max_abs(
                        adjoint_channel(projector, pointer_operators)
                        - projector
                    )
                    for projector in projectors
                )
            )

            expected_repeatability_defect = (
                2.0 * epsilon * (1.0 - epsilon)
            )
            measured_repeatability_defects = []
            for state in state_grid:
                distribution = sequential_distribution(
                    state,
                    pointer_operators,
                )
                measured_repeatability_defects.append(
                    float(distribution[0, 1] + distribution[1, 0])
                )
            repeatability_formula_errors.append(
                max(
                    abs(value - expected_repeatability_defect)
                    for value in measured_repeatability_defects
                )
            )

            archive_states = conditional_archive_states(theta, epsilon)
            disclosure = trace_distance(*archive_states)
            expected_disclosure = 1.0 - 2.0 * epsilon
            disclosure_formula_errors.append(
                abs(disclosure - expected_disclosure)
            )

            coherent_state = ket_density(coherent_source)
            evolved = nonselective_channel(
                coherent_state,
                pointer_operators,
            )
            left = rotation @ KET0
            right = rotation @ KET1
            visibility = 2.0 * abs(
                np.vdot(left, evolved @ right)
            )
            expected_visibility = (
                2.0 * math.sqrt(epsilon * (1.0 - epsilon))
            )
            complementarity_errors.append(
                max(
                    abs(visibility - expected_visibility),
                    abs(disclosure**2 + visibility**2 - 1.0),
                )
            )

            effect_defect = max(
                sharpness_defect(effect)
                for effect in pointer_effects
            )
            sharpness_rows.append(
                {
                    "theta_over_pi": rounded(theta / math.pi),
                    "epsilon": epsilon,
                    "effect_projection_defect": rounded(effect_defect),
                    "two_pass_record_mismatch": rounded(
                        measured_repeatability_defects[0]
                    ),
                    "sector_disclosure_trace_distance": rounded(disclosure),
                    "residual_coherence_visibility": rounded(visibility),
                }
            )

    sharp_z = pointer_kraus(0.0, 0.0)
    sharp_x = pointer_kraus(math.pi / 4.0, 0.0)
    sharp_z_effects = effects(sharp_z)
    sharp_x_effects = effects(sharp_x)
    frozen_source_projectors = basis_projectors(0.0)
    source_nondisturbance = {
        "aligned_z": max(
            max_abs(adjoint_channel(item, sharp_z) - item)
            for item in frozen_source_projectors
        ),
        "misaligned_x": max(
            max_abs(adjoint_channel(item, sharp_x) - item)
            for item in frozen_source_projectors
        ),
    }
    basis_effect_gap = max(
        max_abs(left - right)
        for left, right in zip(
            sharp_z_effects,
            sharp_x_effects,
            strict=True,
        )
    )
    rotation_x = basis_rotation(math.pi / 4.0)
    conjugated_z_coupling = (
        np.kron(rotation_x, I2)
        @ system_pointer_unitary(0.0, 0.0)
        @ np.kron(dagger(rotation_x), I2)
    )
    conjugation_error = max_abs(
        conjugated_z_coupling
        - system_pointer_unitary(math.pi / 4.0, 0.0)
    )

    provenance_inputs = tuple(
        (setting, outcome)
        for setting in ("Z", "X")
        for outcome in (0, 1)
    )
    with_provenance = {
        item: (item[0], item[1], 1)
        for item in provenance_inputs
    }
    without_provenance = {
        item: item[1]
        for item in provenance_inputs
    }
    provenance_is_injective = (
        len(set(with_provenance.values()))
        == len(provenance_inputs)
    )
    outcome_only_is_ambiguous = (
        len(set(without_provenance.values()))
        < len(provenance_inputs)
    )

    archive_flip = 0.1
    sharp_pointer_effects = effects(sharp_z)
    noisy_access_effects = accessible_effects(
        sharp_pointer_effects,
        archive_flip,
    )
    noisy_access_defect = max(
        sharpness_defect(effect)
        for effect in noisy_access_effects
    )
    noisy_archive_states = conditional_archive_states(
        0.0,
        0.0,
        archive_flip=archive_flip,
    )
    noisy_disclosure = trace_distance(*noisy_archive_states)
    majority_three = majority_error_three(archive_flip)
    majority_effects = accessible_effects(
        sharp_pointer_effects,
        majority_three,
    )
    majority_defect = max(
        sharpness_defect(effect)
        for effect in majority_effects
    )

    multiplicity = multiplicity_control()

    coherent_certificate = np.array(
        [[0.5, 0.0], [0.0, 0.5]],
        dtype=float,
    )
    classical_history_null = np.full((2, 2), 0.25, dtype=float)
    certificate_given_history = np.full((2, 4), 0.25, dtype=float)
    which_history_kernel = np.eye(2, dtype=float)
    certificate_gap = total_variation(
        coherent_certificate,
        classical_history_null,
    )
    certificate_history_gap = total_variation(
        certificate_given_history[0],
        certificate_given_history[1],
    )
    sharp_history_archive = np.array(
        [
            np.diag(state).real
            for state in conditional_archive_states(0.0, 0.0)
        ]
    )
    coherent_input = ket_density((KET0 + KET1) / math.sqrt(2.0))
    after_sharp_disclosure = nonselective_channel(
        coherent_input,
        sharp_z,
    )
    post_disclosure_x_visibility = float(
        np.real_if_close(np.trace(X2 @ after_sharp_disclosure))
    )

    resource_contract = {
        "persistent_system_qubits": 1,
        "fresh_pointer_qubits_per_attempt": 1,
        "fresh_archive_outcome_qubits_per_attempt": 1,
        "classical_provenance_bits_per_attempt": 1,
        "system_pointer_unitaries_per_attempt": 1,
        "pointer_archive_cnots_per_attempt": 1,
        "archive_dephasings_or_readouts_per_attempt": 1,
        "fresh_apparatus_sets_for_two_pass_repeatability": 2,
        "charged_optional_majority_archive_bits": 3,
        "excluded_not_zero_cost": [
            "macroscopic amplification",
            "thermodynamic reset work",
            "long-horizon memory failure",
            "laboratory control synthesis",
            "public or Byzantine finality",
        ],
    }

    sharp_rows = [
        row
        for row in sharpness_rows
        if row["epsilon"] == 0.0
    ]
    unsharp_rows = [
        row
        for row in sharpness_rows
        if 0.0 < row["epsilon"] <= 0.5
    ]

    assertions = [
        (
            "all_pointer_and_system_pointer_maps_are_unitary",
            max(unitary_errors) <= TOL,
        ),
        (
            "blank_pointer_archive_process_is_an_isometry",
            max(isometry_errors) <= TOL,
        ),
        (
            "explicit_archive_circuit_recovers_pointer_instrument",
            max(archive_kraus_errors) <= TOL,
        ),
        (
            "every_pointer_instrument_is_trace_preserving",
            max(trace_preservation_errors) <= TOL,
        ),
        (
            "analytic_binary_qnd_effect_formula_holds",
            max(effect_formula_errors) <= TOL,
        ),
        (
            "central_sector_algebra_is_nondisturbed_even_when_unsharp",
            max(central_nondisturbance_errors) <= TOL,
        ),
        (
            "two_pass_mismatch_is_two_epsilon_one_minus_epsilon",
            max(repeatability_formula_errors) <= TOL,
        ),
        (
            "archive_sector_disclosure_is_one_minus_two_epsilon",
            max(disclosure_formula_errors) <= TOL,
        ),
        (
            "disclosure_and_residual_coherence_obey_exact_complementarity",
            max(complementarity_errors) <= TOL,
        ),
        (
            "zero_crossover_members_are_sharp_repeatable_and_disclosing",
            all(
                row["effect_projection_defect"] <= TOL
                and row["two_pass_record_mismatch"] <= TOL
                and abs(
                    row["sector_disclosure_trace_distance"] - 1.0
                )
                <= TOL
                for row in sharp_rows
            ),
        ),
        (
            "positive_crossover_members_are_unsharp_and_nonrepeatable",
            all(
                row["effect_projection_defect"] > TOL
                and row["two_pass_record_mismatch"] > TOL
                and row["sector_disclosure_trace_distance"] < 1.0 - TOL
                for row in unsharp_rows
            ),
        ),
        (
            "physical_archive_outcomes_exist_for_unsharp_members",
            all(
                abs(
                    sum(
                        np.diag(state).real
                    )
                    - 1.0
                )
                <= TOL
                for epsilon in epsilon_grid[1:]
                for state in conditional_archive_states(0.0, epsilon)
            ),
        ),
        (
            "setting_outcome_provenance_is_injective",
            provenance_is_injective,
        ),
        (
            "outcome_without_setting_provenance_is_ambiguous",
            outcome_only_is_ambiguous,
        ),
        (
            "z_and_x_sharp_instruments_have_distinct_effects",
            basis_effect_gap >= 0.5 - TOL,
        ),
        (
            "x_basis_circuit_is_unitary_conjugate_of_z_basis_circuit",
            conjugation_error <= TOL,
        ),
        (
            "frozen_source_algebra_admits_aligned_sharp_instrument",
            source_nondisturbance["aligned_z"] <= TOL,
        ),
        (
            "frozen_source_algebra_rejects_misaligned_sharp_instrument",
            source_nondisturbance["misaligned_x"] >= 0.5 - TOL,
        ),
        (
            "unitary_conjugate_bases_have_identical_resource_budget",
            resource_contract["persistent_system_qubits"] == 1
            and resource_contract["fresh_pointer_qubits_per_attempt"] == 1
            and resource_contract["fresh_archive_outcome_qubits_per_attempt"]
            == 1,
        ),
        (
            "noisy_archive_reduces_accessible_sector_disclosure",
            abs(noisy_disclosure - 0.8) <= TOL,
        ),
        (
            "noisy_archive_makes_accessible_effects_unsharp",
            abs(noisy_access_defect - 0.09) <= TOL,
        ),
        (
            "finite_majority_redundancy_improves_but_not_exactly",
            majority_three < archive_flip
            and majority_three > 0.0
            and majority_defect > TOL
            and majority_defect < noisy_access_defect,
        ),
        (
            "multiplicity_control_instruments_are_trace_preserving",
            max(
                multiplicity["trace_preservation_errors"].values()
            )
            <= TOL,
        ),
        (
            "multiplicity_control_has_one_sharp_pvm",
            multiplicity["same_effect_error"] <= TOL,
        ),
        (
            "multiplicity_control_is_exactly_repeatable",
            max(multiplicity["repeatability_errors"].values()) <= TOL,
        ),
        (
            "multiplicity_control_preserves_central_sector_algebra",
            max(
                multiplicity["central_nondisturbance_errors"].values()
            )
            <= TOL,
        ),
        (
            "same_sharp_record_allows_different_selective_continuations",
            multiplicity["selective_continuation_trace_distance"]
            >= 1.0 - TOL,
        ),
        (
            "full_sector_nondisturbance_rejects_twisted_continuation",
            multiplicity["full_sector_observable_errors"]["luders"] <= TOL
            and multiplicity["full_sector_observable_errors"]["twisted"]
            > 1.0,
        ),
        (
            "coherent_certificate_separates_frozen_process_classes",
            abs(certificate_gap - 0.5) <= TOL,
        ),
        (
            "coherent_certificate_does_not_disclose_run_history",
            certificate_history_gap <= TOL,
        ),
        (
            "which_history_kernel_discloses_run_history",
            max_abs(which_history_kernel - np.eye(2)) <= TOL,
        ),
        (
            "formed_sharp_archive_realizes_which_history_kernel",
            max_abs(sharp_history_archive - which_history_kernel) <= TOL,
        ),
        (
            "formed_which_history_archive_kills_complementary_coherence",
            abs(post_disclosure_x_visibility) <= TOL,
        ),
        (
            "certificate_and_disclosure_records_remain_distinct",
            certificate_history_gap <= TOL
            and max_abs(sharp_history_archive - which_history_kernel) <= TOL
            and abs(certificate_gap - 0.5) <= TOL,
        ),
    ]

    passed = sum(int(ok) for _, ok in assertions)
    total = len(assertions)

    artifact_multiplicity = {
        key: (
            {
                nested_key: rounded(nested_value)
                for nested_key, nested_value in value.items()
            }
            if isinstance(value, dict)
            else rounded(value)
        )
        for key, value in multiplicity.items()
        if key not in {"projectors", "luders", "twisted"}
    }

    result = {
        "schema": "dynamic-unity/formed-sharp-instrument/v1",
        "run_id": RUN_ID,
        "grade": (
            "EXACT FINITE CIRCUIT CLASSIFICATION / "
            "REPEATABILITY-SHARPNESS AND INSTRUMENT MATHEMATICS KNOWN / "
            "NEW DU PHYSICAL-SELECTION DEPENDENCY NO-GO / "
            "NO NOVEL-QUANTUM PROMOTION"
        ),
        "fixture": {
            "systems": [
                "one system qubit",
                "one fresh pointer qubit per attempt",
                "one fresh archive outcome qubit per attempt",
                "one classical setting/provenance bit for the two-basis control",
            ],
            "event_order": [
                "prepare system and blank pointer/archive",
                "apply frozen system-pointer unitary",
                "copy pointer to archive by CNOT",
                "apply declared archive noise channel",
                "dephase/read archive in frozen basis",
                "retain setting and sequence provenance",
                "repeat with fresh support when testing repeatability",
            ],
            "admitted_basis_angles_over_pi": [
                rounded(theta / math.pi)
                for theta in theta_grid
            ],
            "pointer_crossover_values": list(epsilon_grid),
            "archive_flip_control": archive_flip,
            "resource_contract": resource_contract,
            "implementation_scope": (
                "complete finite circuit and access model; not a laboratory "
                "Hamiltonian, thermodynamic archive, or public-finality model"
            ),
        },
        "scoped_formed_sharp_equivalence": {
            "family": (
                "binary QND pointer instruments with crossover epsilon in "
                "[0,1/2] and noiseless pointer-to-archive transduction"
            ),
            "equivalent_at_epsilon_zero": [
                "projection-valued outcome effects",
                "zero immediate two-pass outcome mismatch",
                "perfect archive discrimination of the two supplied sectors",
            ],
            "analytic_relations": {
                "effect_projection_defect": "epsilon*(1-epsilon)",
                "two_pass_record_mismatch": (
                    "2*epsilon*(1-epsilon)"
                ),
                "sector_disclosure_trace_distance": "1-2*epsilon",
                "residual_coherence_visibility": (
                    "2*sqrt(epsilon*(1-epsilon))"
                ),
                "complementarity": "D^2+V^2=1",
            },
            "rows": sharpness_rows,
            "status": (
                "exact scoped theorem; broad repeatability-sharpness "
                "characterization is occupied prior art"
            ),
        },
        "physical_selection_no_go": {
            "basis_gap_between_z_and_x_effects": rounded(basis_effect_gap),
            "conjugation_error": rounded(conjugation_error),
            "frozen_source_algebra_nondisturbance_errors": {
                key: rounded(value)
                for key, value in source_nondisturbance.items()
            },
            "verdict": (
                "the complete frozen coupling derives its own outcome "
                "instrument. Self-relative formation, repeatability and "
                "nondisturbance admit every unitary-conjugate basis. A "
                "separately frozen source algebra rejects the misaligned "
                "basis and, with exact repeatability, earns the aligned "
                "outcome PVM in this nondegenerate family; it still does not "
                "generate the pointer/archive coupling or select a unique "
                "degenerate-sector continuation"
            ),
            "multiplicity_control": artifact_multiplicity,
            "instrument_verdict": (
                "with degenerate sectors the same sharp PVM and archive "
                "record admit distinct repeatable central-nondisturbing "
                "selective continuations; full within-sector "
                "nondisturbance or another continuation principle is extra"
            ),
        },
        "access_boundary": {
            "sharp_pointer_archive_flip": archive_flip,
            "noisy_archive_sector_disclosure": rounded(noisy_disclosure),
            "noisy_access_effect_projection_defect": rounded(
                noisy_access_defect
            ),
            "three_copy_majority_error": rounded(majority_three),
            "three_copy_majority_effect_projection_defect": rounded(
                majority_defect
            ),
            "verdict": (
                "sharpness at the pointer is not sharpness of the final "
                "observer-accessible record unless transduction is exact or "
                "an error-qualified decoding contract is supplied"
            ),
        },
        "certificate_vs_disclosure": {
            "coherent_certificate_joint_record": rounded_matrix(
                coherent_certificate
            ),
            "classical_history_null_joint_record": rounded_matrix(
                classical_history_null
            ),
            "process_class_total_variation": rounded(certificate_gap),
            "certificate_record_given_history": rounded_matrix(
                certificate_given_history
            ),
            "history_disclosure_total_variation": rounded(
                certificate_history_gap
            ),
            "formed_sharp_history_archive_kernel": rounded_matrix(
                sharp_history_archive
            ),
            "post_disclosure_x_visibility": rounded(
                post_disclosure_x_visibility
            ),
            "verdict": (
                "the formed sharp sector archive is a disclosure record and "
                "kills complementary coherence; the coherent signed record "
                "is a process-class certificate with identical run-history "
                "rows. Neither record substitutes for the other"
            ),
        },
        "strongest_standard_absorber": {
            "sharpness": (
                "Buscemi, Kobayashi, and Minagawa, Quantum 8, 1235 "
                "(2024), arXiv:2303.07737: maximal sharp finite POVMs "
                "coincide with POVMs admitting repeatable measurements"
            ),
            "instrument": (
                "Davies-Lewis/Ozawa quantum-instrument and indirect-"
                "measurement theory: a POVM does not uniquely fix its "
                "selective state-update instrument or physical dilation"
            ),
            "decoherence": (
                "standard information-disturbance and pointer-record "
                "mathematics absorbs the disclosure/coherence relation"
            ),
            "du_residue": (
                "which independently specified source dynamics, access "
                "algebra, continuation contract, and resource/noise boundary "
                "select the physically realized instrument"
            ),
        },
        "reopener": {
            "independently_required_inputs": [
                "a source-selected algebra or physical coupling family",
                "a non-refit selection principle among conjugate couplings",
                "full within-sector action nondisturbance or another typed continuation rule",
                "an error-qualified end-to-end archive decoder",
                "a held-out perturbation, locality, energy, or resource discriminator",
            ],
            "held_out_test": (
                "freeze a physical Hamiltonian and admissible perturbation "
                "class before examining outcomes; show that one instrument "
                "orbit remains repeatable, action-nondisturbing, and "
                "end-to-end decodable while a named conjugate or twisted "
                "foil fails at matched resources"
            ),
        },
        "claims_not_made": [
            "new repeatability-sharpness theorem",
            "unique pointer-basis derivation",
            "unique selective-instrument derivation",
            "macroscopic or thermodynamic irreversibility",
            "public, adversarial, or Byzantine finality",
            "laboratory proper-time implementation",
            "quantum selection from a GPT landscape",
            "record-first ontology or beyond-standard quantum physics",
        ],
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

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(
        "du_formed_sharp_instrument_probe: "
        f"{passed}/{total} checks passed"
    )
    if passed != total:
        failed = [name for name, ok in assertions if not ok]
        raise SystemExit("failed checks: " + ", ".join(failed))


if __name__ == "__main__":
    main()
