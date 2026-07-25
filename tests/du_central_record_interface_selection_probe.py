#!/usr/bin/env python3
"""Exact finite probe for central record-interface selection.

The probe classifies finite abelian random-unitary channels with an explicit
branch environment.  It keeps two certificates separate:

1. the fixed/noiseless algebra and its canonical classical center; and
2. distinguishability of the corresponding conditional environment states.

For a uniform full-group abelian twirl, character orthogonality makes the
environment exactly record the character-sector center.  Multiplicity spaces
inside one character sector remain quantum and their bases are not selected.
A matched noncommuting Pauli trio then separates finite-time observable
stability from complementary-environment record formation.

Passing establishes a finite representation-theoretic specialization and
hostile controls.  It does not derive a physical channel, system/environment
cut, observer, public finality, proper time, geometry, ontology, or new law.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_central_record_interface_selection_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), sort_keys=True, indent=2) + "\n"


def fraction_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                left - factor * right
                for left, right in zip(
                    rows[row], rows[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(row) for row in zip(*matrix, strict=True))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    right_t = transpose(right)
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(left_row, right_column, strict=True)),
                start=Fraction(0),
            )
            for right_column in right_t
        )
        for left_row in left
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            a + b
            for a, b in zip(left_row, right_row, strict=True)
        )
        for left_row, right_row in zip(left, right, strict=True)
    )


def matrix_scale(scale: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scale * value for value in row)
        for row in matrix
    )


def identity(dimension: int) -> Matrix:
    return tuple(
        tuple(
            Fraction(int(row == column))
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def matrix_unit(dimension: int, row: int, column: int) -> Matrix:
    return tuple(
        tuple(
            Fraction(int((i, j) == (row, column)))
            for j in range(dimension)
        )
        for i in range(dimension)
    )


def max_abs(matrix: Matrix) -> Fraction:
    return max(abs(value) for row in matrix for value in row)


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matmul(left, right), matrix_scale(-1, matmul(right, left)))


def commutant_dimension(generators: Sequence[Matrix]) -> int:
    dimension = len(generators[0])
    equations: list[list[Fraction]] = []
    for generator in generators:
        for row in range(dimension):
            for column in range(dimension):
                equation = [Fraction(0) for _ in range(dimension**2)]
                for index in range(dimension):
                    equation[row * dimension + index] += generator[index][column]
                    equation[index * dimension + column] -= generator[row][index]
                equations.append(equation)
    return dimension**2 - fraction_rank(equations)


def fixed_space_dimension(
    generators: Sequence[Matrix],
    weights: Sequence[Fraction],
) -> int:
    dimension = len(generators[0])
    equations: list[list[Fraction]] = []
    for out_row in range(dimension):
        for out_column in range(dimension):
            equation = [Fraction(0) for _ in range(dimension**2)]
            for generator, weight in zip(generators, weights, strict=True):
                for in_row in range(dimension):
                    for in_column in range(dimension):
                        equation[in_row * dimension + in_column] += (
                            weight
                            * generator[in_row][out_row]
                            * generator[in_column][out_column]
                        )
            equation[out_row * dimension + out_column] -= 1
            equations.append(equation)
    return dimension**2 - fraction_rank(equations)


def fixed_error(
    observable: Matrix,
    generators: Sequence[Matrix],
    weights: Sequence[Fraction],
) -> Fraction:
    evolved = tuple(
        tuple(Fraction(0) for _ in observable)
        for _ in observable
    )
    for generator, weight in zip(generators, weights, strict=True):
        conjugated = matmul(
            transpose(generator),
            matmul(observable, generator),
        )
        evolved = matrix_add(evolved, matrix_scale(weight, conjugated))
    return max_abs(matrix_add(evolved, matrix_scale(-1, observable)))


def character(label: int, group_element: int) -> int:
    return -1 if (label & group_element).bit_count() % 2 else 1


def diagonal_character_unitary(
    labels: Sequence[int],
    group_element: int,
) -> Matrix:
    return tuple(
        tuple(
            Fraction(
                character(label, group_element)
                if row == column
                else 0
            )
            for column, _ in enumerate(labels)
        )
        for row, label in enumerate(labels)
    )


def support_signatures(
    labels: Sequence[int],
    weights: Sequence[Fraction],
) -> tuple[tuple[int, ...], ...]:
    support = [
        group_element
        for group_element, weight in enumerate(weights)
        if weight > 0
    ]
    return tuple(
        tuple(character(label, group_element) for group_element in support)
        for label in labels
    )


def partition_by_signature(
    signatures: Sequence[tuple[int, ...]],
) -> tuple[tuple[int, ...], ...]:
    blocks: dict[tuple[int, ...], list[int]] = {}
    for index, signature in enumerate(signatures):
        blocks.setdefault(signature, []).append(index)
    return tuple(tuple(indices) for indices in blocks.values())


def environment_overlap(
    left_label: int,
    right_label: int,
    weights: Sequence[Fraction],
) -> Fraction:
    return sum(
        (
            weight
            * character(left_label, group_element)
            * character(right_label, group_element)
            for group_element, weight in enumerate(weights)
        ),
        start=Fraction(0),
    )


def classify_abelian_interface(
    model_id: str,
    group_rank: int,
    labels: Sequence[int],
    weights: Sequence[Fraction],
) -> dict[str, Any]:
    group_size = 2**group_rank
    if len(weights) != group_size:
        raise ValueError("weights must cover Z2^rank")
    if sum(weights, start=Fraction(0)) != 1:
        raise ValueError("weights must sum to one")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be nonnegative")
    if any(label < 0 or label >= group_size for label in labels):
        raise ValueError("invalid character label")

    signatures = support_signatures(labels, weights)
    blocks = partition_by_signature(signatures)
    positive_generators = tuple(
        diagonal_character_unitary(labels, group_element)
        for group_element, weight in enumerate(weights)
        if weight > 0
    )
    positive_weights = tuple(weight for weight in weights if weight > 0)
    block_representatives = [labels[block[0]] for block in blocks]
    overlap_matrix = tuple(
        tuple(
            environment_overlap(left, right, weights)
            for right in block_representatives
        )
        for left in block_representatives
    )
    distance_squared = tuple(
        tuple(1 - overlap * overlap for overlap in row)
        for row in overlap_matrix
    )
    off_diagonal = [
        overlap_matrix[row][column]
        for row in range(len(blocks))
        for column in range(len(blocks))
        if row != column
    ]

    center_dimension = len(blocks)
    if center_dimension == 1:
        formation_grade = "NO_NONTRIVIAL_CLASSICAL_CENTER"
    elif all(overlap == 0 for overlap in off_diagonal):
        formation_grade = "EXACT_CENTER_RECORD"
    elif all(abs(overlap) == 1 for overlap in off_diagonal):
        formation_grade = "NO_ENVIRONMENT_RECORD"
    else:
        formation_grade = "PARTIAL_CENTER_RECORD"

    stable_dimension = sum(len(block) ** 2 for block in blocks)
    return {
        "model_id": model_id,
        "group": f"Z2^{group_rank}",
        "character_labels": tuple(labels),
        "weights": tuple(weights),
        "positive_support": tuple(
            index for index, weight in enumerate(weights) if weight > 0
        ),
        "support_signatures": signatures,
        "sector_blocks": blocks,
        "sector_multiplicities": tuple(len(block) for block in blocks),
        "fixed_algebra_dimension_formula": stable_dimension,
        "commutant_dimension_exact": commutant_dimension(positive_generators),
        "fixed_space_dimension_exact": fixed_space_dimension(
            positive_generators, positive_weights
        ),
        "center_dimension": center_dimension,
        "fully_classical": all(len(block) == 1 for block in blocks),
        "environment_overlap_matrix": overlap_matrix,
        "environment_trace_distance_squared": distance_squared,
        "formation_grade": formation_grade,
    }


def uniform_character_orthogonality(max_rank: int = 3) -> dict[str, Any]:
    checks = 0
    maximum_error = Fraction(0)
    for rank in range(1, max_rank + 1):
        size = 2**rank
        weights = tuple(Fraction(1, size) for _ in range(size))
        for left in range(size):
            for right in range(size):
                overlap = environment_overlap(left, right, weights)
                expected = Fraction(int(left == right))
                maximum_error = max(maximum_error, abs(overlap - expected))
                checks += 1
    return {
        "ranks_checked": tuple(range(1, max_rank + 1)),
        "character_pairs_checked": checks,
        "maximum_orthogonality_error": maximum_error,
    }


def degeneracy_nonselection_receipt() -> dict[str, Any]:
    labels = (0, 0, 1, 1)
    branch_z = diagonal_character_unitary(labels, 1)
    swap_first_block: Matrix = (
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    central_first = matrix_add(matrix_unit(4, 0, 0), matrix_unit(4, 1, 1))
    internal_rank_one = matrix_unit(4, 0, 0)
    rotated_center = matmul(
        transpose(swap_first_block),
        matmul(central_first, swap_first_block),
    )
    rotated_internal = matmul(
        transpose(swap_first_block),
        matmul(internal_rank_one, swap_first_block),
    )
    return {
        "block_rotation_commutator_error": max_abs(
            commutator(swap_first_block, branch_z)
        ),
        "central_projector_rotation_error": max_abs(
            matrix_add(rotated_center, matrix_scale(-1, central_first))
        ),
        "internal_rank_one_moves": rotated_internal != internal_rank_one,
        "internal_projector_before": internal_rank_one,
        "internal_projector_after": rotated_internal,
    }


def coordinate_naturality_receipt() -> dict[str, Any]:
    identity_two = identity(2)
    z_matrix: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    rotation: Matrix = (
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(-4, 5), Fraction(3, 5)),
    )
    conjugated_z = matmul(rotation, matmul(z_matrix, transpose(rotation)))
    projector = matrix_unit(2, 0, 0)
    conjugated_projector = matmul(
        rotation, matmul(projector, transpose(rotation))
    )
    weights = (Fraction(1, 2), Fraction(1, 2))
    return {
        "rotation_orthogonality_error": max_abs(
            matrix_add(
                matmul(rotation, transpose(rotation)),
                matrix_scale(-1, identity_two),
            )
        ),
        "original_fixed_dimension": fixed_space_dimension(
            (identity_two, z_matrix), weights
        ),
        "conjugated_fixed_dimension": fixed_space_dimension(
            (identity_two, conjugated_z), weights
        ),
        "conjugated_projector_fixed_error": fixed_error(
            conjugated_projector,
            (identity_two, conjugated_z),
            weights,
        ),
        "conjugated_projector": conjugated_projector,
    }


def noncommuting_perturbation_receipt() -> dict[str, Any]:
    identity_two = identity(2)
    z_matrix: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    x_matrix: Matrix = (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )
    epsilon = Fraction(1, 1000)
    unperturbed_generators = (identity_two, z_matrix)
    unperturbed_weights = (Fraction(1, 2), Fraction(1, 2))
    perturbed_generators = (identity_two, z_matrix, x_matrix)
    perturbed_weights = (
        Fraction(1, 2) - epsilon,
        Fraction(1, 2),
        epsilon,
    )
    return {
        "epsilon": epsilon,
        "unperturbed_fixed_dimension": fixed_space_dimension(
            unperturbed_generators, unperturbed_weights
        ),
        "unperturbed_commutant_dimension": commutant_dimension(
            unperturbed_generators
        ),
        "perturbed_fixed_dimension": fixed_space_dimension(
            perturbed_generators, perturbed_weights
        ),
        "perturbed_commutant_dimension": commutant_dimension(
            perturbed_generators
        ),
        "exact_center_destroyed": (
            fixed_space_dimension(
                unperturbed_generators, unperturbed_weights
            )
            > fixed_space_dimension(
                perturbed_generators, perturbed_weights
            )
        ),
    }


def environment_gauge_receipt(
    labels: Sequence[int],
    weights: Sequence[Fraction],
) -> dict[str, Any]:
    original = tuple(
        tuple(
            environment_overlap(left, right, weights)
            for right in labels
        )
        for left in labels
    )
    permutation = tuple(reversed(range(len(weights))))
    permuted_weights = tuple(weights[index] for index in permutation)

    def permuted_character(label: int, position: int) -> int:
        return character(label, permutation[position])

    permuted = tuple(
        tuple(
            sum(
                (
                    permuted_weights[position]
                    * permuted_character(left, position)
                    * permuted_character(right, position)
                    for position in range(len(weights))
                ),
                start=Fraction(0),
            )
            for right in labels
        )
        for left in labels
    )
    return {
        "branch_permutation": permutation,
        "gram_matrix_invariant": original == permuted,
        "original_gram_matrix": original,
        "permuted_gram_matrix": permuted,
    }


def coherent_environment_access_receipt(
    group_rank: int = 2,
) -> dict[str, Any]:
    size = 2**group_rank
    weights = tuple(Fraction(1, size) for _ in range(size))
    decoded_kernel = tuple(
        tuple(
            sum(
                (
                    weights[group_element]
                    * character(input_label, group_element)
                    * character(output_label, group_element)
                    for group_element in range(size)
                ),
                start=Fraction(0),
            )
            for output_label in range(size)
        )
        for input_label in range(size)
    )
    branch_population_kernel = tuple(weights for _ in range(size))
    coherent_distance_squared = tuple(
        tuple(
            1
            - environment_overlap(left, right, weights) ** 2
            for right in range(size)
        )
        for left in range(size)
    )
    dephased_distance_squared = tuple(
        tuple(
            (
                sum(
                    (
                        abs(left_probability - right_probability)
                        for left_probability, right_probability in zip(
                            branch_population_kernel[left],
                            branch_population_kernel[right],
                            strict=True,
                        )
                    ),
                    start=Fraction(0),
                )
                / 2
            )
            ** 2
            for right in range(size)
        )
        for left in range(size)
    )
    return {
        "group": f"Z2^{group_rank}",
        "declared_coherent_decoder": "normalized Walsh character transform",
        "decoded_label_kernel": decoded_kernel,
        "branch_population_kernel_after_dephasing": (
            branch_population_kernel
        ),
        "coherent_environment_trace_distance_squared": (
            coherent_distance_squared
        ),
        "dephased_environment_trace_distance_squared": (
            dephased_distance_squared
        ),
        "interpretation": (
            "the exact sector code is readable with coherent environment "
            "access; branch-basis dephasing erases it before decoding"
        ),
    }


def repeated_fragment_receipt(
    overlap: Fraction,
    target_distance_squared: Fraction,
) -> dict[str, Any]:
    fragment_count = 1
    while 1 - overlap ** (2 * fragment_count) < target_distance_squared:
        fragment_count += 1
    return {
        "single_fragment_overlap": overlap,
        "target_trace_distance_squared": target_distance_squared,
        "minimum_independent_fragments": fragment_count,
        "achieved_trace_distance_squared": (
            1 - overlap ** (2 * fragment_count)
        ),
        "previous_trace_distance_squared": (
            0
            if fragment_count == 1
            else 1 - overlap ** (2 * (fragment_count - 1))
        ),
        "complementarity_identity_error": (
            overlap ** (2 * fragment_count)
            + (1 - overlap ** (2 * fragment_count))
            - 1
        ),
    }


def exact_fraction_sqrt(value: Fraction) -> Fraction | None:
    numerator_root = math.isqrt(value.numerator)
    denominator_root = math.isqrt(value.denominator)
    if (
        numerator_root**2 != value.numerator
        or denominator_root**2 != value.denominator
    ):
        return None
    return Fraction(numerator_root, denominator_root)


def pauli_fixed_algebra_dimension(
    weights: Sequence[Fraction],
) -> int:
    active_nonidentity = sum(
        int(weight > 0) for weight in weights[1:]
    )
    if active_nonidentity == 0:
        return 4
    if active_nonidentity == 1:
        return 2
    return 1


def pauli_z_interface_receipt(
    model_id: str,
    weights: Sequence[Fraction],
    horizon: int,
) -> dict[str, Any]:
    if len(weights) != 4:
        raise ValueError("Pauli weights use I, X, Y, Z order")
    if sum(weights, start=Fraction(0)) != 1:
        raise ValueError("Pauli weights must sum to one")
    if any(weight < 0 for weight in weights):
        raise ValueError("Pauli weights must be nonnegative")
    if horizon < 1:
        raise ValueError("horizon must be positive")

    weight_i, weight_x, weight_y, weight_z = weights
    lambda_x = weight_i + weight_x - weight_y - weight_z
    lambda_y = weight_i - weight_x + weight_y - weight_z
    lambda_z = weight_i - weight_x - weight_y + weight_z

    product_no_flip = weight_i * weight_z
    product_flip = weight_x * weight_y
    cross_root = exact_fraction_sqrt(
        product_no_flip * product_flip
    )
    if cross_root is None:
        distance_squared: Fraction | str = (
            "4*(wI*wZ+wX*wY+2*sqrt(wI*wZ*wX*wY))"
        )
    else:
        distance_squared = 4 * (
            product_no_flip + product_flip + 2 * cross_root
        )

    if distance_squared == 1:
        formation_grade = "EXACT_Z_INPUT_RECORD"
    elif distance_squared == 0:
        formation_grade = "NO_Z_INPUT_RECORD"
    else:
        formation_grade = "PARTIAL_Z_INPUT_RECORD"

    horizon_survival = lambda_z**horizon
    branch_populations_zero = tuple(weights)
    branch_populations_one = tuple(weights)
    branch_dephased_distance = sum(
        (
            abs(left - right)
            for left, right in zip(
                branch_populations_zero,
                branch_populations_one,
                strict=True,
            )
        ),
        start=Fraction(0),
    ) / 2
    return {
        "model_id": model_id,
        "weights_i_x_y_z": tuple(weights),
        "pauli_eigenvalues_x_y_z": (
            lambda_x,
            lambda_y,
            lambda_z,
        ),
        "fixed_algebra_dimension": pauli_fixed_algebra_dimension(weights),
        "z_is_exactly_fixed": lambda_z == 1,
        "one_step_z_trace_distance": abs(lambda_z),
        "one_step_system_helstrom_error": (
            1 - abs(lambda_z)
        ) / 2,
        "horizon": horizon,
        "horizon_z_trace_distance": abs(horizon_survival),
        "horizon_system_helstrom_error": (
            1 - abs(horizon_survival)
        ) / 2,
        "environment_z_trace_distance_squared": distance_squared,
        "environment_formation_grade": formation_grade,
        "branch_population_kernel_z_inputs": (
            branch_populations_zero,
            branch_populations_one,
        ),
        "branch_dephased_environment_trace_distance_squared": (
            branch_dephased_distance**2
        ),
        "environment_distance_formula": (
            "D_E=2*(sqrt(wI*wZ)+sqrt(wX*wY))"
        ),
    }


def approximate_pauli_separation_receipt() -> dict[str, Any]:
    horizon = 4
    models = {
        "no_environment_record": pauli_z_interface_receipt(
            "no_environment_record",
            (
                Fraction(0),
                Fraction(1, 8),
                Fraction(0),
                Fraction(7, 8),
            ),
            horizon,
        ),
        "partial_environment_record": pauli_z_interface_receipt(
            "partial_environment_record",
            (
                Fraction(3, 8),
                Fraction(1, 8),
                Fraction(0),
                Fraction(1, 2),
            ),
            horizon,
        ),
        "exact_environment_record": pauli_z_interface_receipt(
            "exact_environment_record",
            (
                Fraction(7, 16),
                Fraction(1, 16),
                Fraction(1, 16),
                Fraction(7, 16),
            ),
            horizon,
        ),
    }
    return {
        "matched_contract": (
            "same scalar exact fixed algebra, one-use Z signal, "
            "four-use Z signal, and system Z-readout error"
        ),
        "models": models,
        "matched_one_step_z_trace_distance": Fraction(3, 4),
        "matched_horizon_z_trace_distance": Fraction(81, 256),
        "environment_distance_squared_range": (
            Fraction(0),
            Fraction(3, 4),
            Fraction(1),
        ),
        "interpretation": (
            "fixed-algebra and finite-time Z-stability receipts do not "
            "determine complementary-environment formation"
        ),
    }


def pauli_stability_formation_rectangle_receipt() -> dict[str, Any]:
    stability_values = (
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
    )
    split_values = (
        Fraction(0),
        Fraction(1, 10),
        Fraction(1, 4),
        Fraction(1, 2),
    )
    rows: list[dict[str, Any]] = []
    for stability in stability_values:
        no_flip_total = (1 + stability) / 2
        flip_total = (1 - stability) / 2
        for split in split_values:
            weights = (
                no_flip_total * split,
                flip_total * split,
                flip_total * (1 - split),
                no_flip_total * (1 - split),
            )
            receipt = pauli_z_interface_receipt(
                (
                    f"rectangle_s_{stability.numerator}_"
                    f"{stability.denominator}_r_{split.numerator}_"
                    f"{split.denominator}"
                ),
                weights,
                horizon=3,
            )
            receipt["target_stability"] = stability
            receipt["split_parameter"] = split
            receipt["target_environment_distance_squared"] = (
                4 * split * (1 - split)
            )
            rows.append(receipt)
    return {
        "constructive_family": (
            "a=(1+s)/2, b=(1-s)/2; "
            "(wI,wX,wY,wZ)=(ar,br,b(1-r),a(1-r))"
        ),
        "analytic_result": (
            "lambda_Z=s and D_E^2=4r(1-r), so for every "
            "0<s<1 the attainable D_E interval is [0,1]"
        ),
        "stability_values": stability_values,
        "split_values": split_values,
        "rows": rows,
    }


def run() -> dict[str, Any]:
    models = {
        "identity": classify_abelian_interface(
            "identity",
            1,
            (0, 1),
            (Fraction(1), Fraction(0)),
        ),
        "deterministic_z": classify_abelian_interface(
            "deterministic_z",
            1,
            (0, 1),
            (Fraction(0), Fraction(1)),
        ),
        "uniform_z2": classify_abelian_interface(
            "uniform_z2",
            1,
            (0, 1),
            (Fraction(1, 2), Fraction(1, 2)),
        ),
        "biased_z2": classify_abelian_interface(
            "biased_z2",
            1,
            (0, 1),
            (Fraction(3, 4), Fraction(1, 4)),
        ),
        "collective_parity": classify_abelian_interface(
            "collective_parity",
            1,
            (0, 0, 1, 1),
            (Fraction(1, 2), Fraction(1, 2)),
        ),
        "uniform_z2_squared": classify_abelian_interface(
            "uniform_z2_squared",
            2,
            (0, 1, 2, 3),
            tuple(Fraction(1, 4) for _ in range(4)),
        ),
    }
    orthogonality = uniform_character_orthogonality()
    degeneracy = degeneracy_nonselection_receipt()
    naturality = coordinate_naturality_receipt()
    perturbation = noncommuting_perturbation_receipt()
    environment_gauge = environment_gauge_receipt(
        (0, 1, 2, 3),
        tuple(Fraction(1, 4) for _ in range(4)),
    )
    coherent_access = coherent_environment_access_receipt()
    repeated_fragments = repeated_fragment_receipt(
        Fraction(1, 2), Fraction(99, 100)
    )
    approximate_pauli = approximate_pauli_separation_receipt()
    pauli_models = approximate_pauli["models"]
    pauli_rectangle = pauli_stability_formation_rectangle_receipt()
    rectangle_rows = pauli_rectangle["rows"]

    checks = {
        "formula_matches_commutant_all_models": all(
            model["fixed_algebra_dimension_formula"]
            == model["commutant_dimension_exact"]
            for model in models.values()
        ),
        "formula_matches_fixed_space_all_models": all(
            model["fixed_algebra_dimension_formula"]
            == model["fixed_space_dimension_exact"]
            for model in models.values()
        ),
        "identity_has_no_nontrivial_center": (
            models["identity"]["center_dimension"] == 1
            and models["identity"]["formation_grade"]
            == "NO_NONTRIVIAL_CLASSICAL_CENTER"
        ),
        "deterministic_unitary_forms_no_environment_record": (
            models["deterministic_z"]["center_dimension"] == 2
            and models["deterministic_z"]["formation_grade"]
            == "NO_ENVIRONMENT_RECORD"
        ),
        "uniform_z2_selects_exact_bit": (
            models["uniform_z2"]["center_dimension"] == 2
            and models["uniform_z2"]["formation_grade"]
            == "EXACT_CENTER_RECORD"
        ),
        "biased_z2_same_center_partial_record": (
            models["biased_z2"]["center_dimension"] == 2
            and models["biased_z2"]["formation_grade"]
            == "PARTIAL_CENTER_RECORD"
            and models["biased_z2"]["environment_overlap_matrix"][0][1]
            == Fraction(1, 2)
            and models["biased_z2"][
                "environment_trace_distance_squared"
            ][0][1]
            == Fraction(3, 4)
        ),
        "collective_parity_records_center_only": (
            models["collective_parity"]["sector_multiplicities"] == (2, 2)
            and models["collective_parity"]["center_dimension"] == 2
            and models["collective_parity"][
                "fixed_algebra_dimension_formula"
            ]
            == 8
            and not models["collective_parity"]["fully_classical"]
            and models["collective_parity"]["formation_grade"]
            == "EXACT_CENTER_RECORD"
        ),
        "z2_squared_records_four_sectors": (
            models["uniform_z2_squared"]["center_dimension"] == 4
            and models["uniform_z2_squared"]["fully_classical"]
            and models["uniform_z2_squared"]["formation_grade"]
            == "EXACT_CENTER_RECORD"
        ),
        "character_orthogonality_exact": (
            orthogonality["character_pairs_checked"] == 84
            and orthogonality["maximum_orthogonality_error"] == 0
        ),
        "block_rotation_commutes_with_dynamics": (
            degeneracy["block_rotation_commutator_error"] == 0
        ),
        "block_rotation_preserves_center": (
            degeneracy["central_projector_rotation_error"] == 0
        ),
        "block_rotation_moves_internal_basis": degeneracy[
            "internal_rank_one_moves"
        ],
        "coordinate_rotation_is_exact": (
            naturality["rotation_orthogonality_error"] == 0
        ),
        "fixed_dimension_is_coordinate_natural": (
            naturality["original_fixed_dimension"]
            == naturality["conjugated_fixed_dimension"]
            == 2
        ),
        "conjugated_projector_is_fixed": (
            naturality["conjugated_projector_fixed_error"] == 0
        ),
        "noncommuting_perturbation_destroys_exact_center": (
            perturbation["unperturbed_fixed_dimension"] == 2
            and perturbation["unperturbed_commutant_dimension"] == 2
            and perturbation["perturbed_fixed_dimension"] == 1
            and perturbation["perturbed_commutant_dimension"] == 1
            and perturbation["exact_center_destroyed"]
        ),
        "environment_branch_gauge_preserves_gram": environment_gauge[
            "gram_matrix_invariant"
        ],
        "walsh_decoder_recovers_sector_label": (
            coherent_access["decoded_label_kernel"]
            == tuple(
                tuple(
                    Fraction(int(row == column))
                    for column in range(4)
                )
                for row in range(4)
            )
        ),
        "branch_dephasing_erases_abelian_sector_label": all(
            value == 0
            for row in coherent_access[
                "dephased_environment_trace_distance_squared"
            ]
            for value in row
        ),
        "coherent_access_not_branch_population_access": (
            len(
                set(
                    coherent_access[
                        "branch_population_kernel_after_dephasing"
                    ]
                )
            )
            == 1
            and any(
                coherent_access[
                    "coherent_environment_trace_distance_squared"
                ][row][column]
                == 1
                for row in range(4)
                for column in range(4)
                if row != column
            )
        ),
        "four_fragments_cross_ninety_nine_percent": (
            repeated_fragments["minimum_independent_fragments"] == 4
            and repeated_fragments["previous_trace_distance_squared"]
            < Fraction(99, 100)
            <= repeated_fragments["achieved_trace_distance_squared"]
        ),
        "fragment_complementarity_exact": (
            repeated_fragments["complementarity_identity_error"] == 0
        ),
        "approximate_pauli_fixed_algebra_matched": all(
            model["fixed_algebra_dimension"] == 1
            for model in pauli_models.values()
        ),
        "approximate_pauli_z_signal_matched": all(
            model["one_step_z_trace_distance"] == Fraction(3, 4)
            for model in pauli_models.values()
        ),
        "approximate_pauli_horizon_signal_matched": all(
            model["horizon_z_trace_distance"] == Fraction(81, 256)
            for model in pauli_models.values()
        ),
        "approximate_pauli_environment_records_separate": (
            tuple(
                model["environment_z_trace_distance_squared"]
                for model in pauli_models.values()
            )
            == (Fraction(0), Fraction(3, 4), Fraction(1))
        ),
        "approximate_stability_does_not_imply_formation": (
            pauli_models["no_environment_record"][
                "one_step_z_trace_distance"
            ]
            == Fraction(3, 4)
            and pauli_models["no_environment_record"][
                "environment_formation_grade"
            ]
            == "NO_Z_INPUT_RECORD"
        ),
        "formation_does_not_imply_exact_fixedness": (
            not pauli_models["exact_environment_record"][
                "z_is_exactly_fixed"
            ]
            and pauli_models["exact_environment_record"][
                "environment_formation_grade"
            ]
            == "EXACT_Z_INPUT_RECORD"
        ),
        "pauli_rectangle_fixed_algebra_scalar": all(
            row["fixed_algebra_dimension"] == 1
            for row in rectangle_rows
        ),
        "pauli_rectangle_stability_coordinate_exact": all(
            row["one_step_z_trace_distance"]
            == row["target_stability"]
            for row in rectangle_rows
        ),
        "pauli_rectangle_formation_coordinate_exact": all(
            row["environment_z_trace_distance_squared"]
            == row["target_environment_distance_squared"]
            for row in rectangle_rows
        ),
        "pauli_rectangle_axes_independent_on_grid": all(
            {
                row["environment_z_trace_distance_squared"]
                for row in rectangle_rows
                if row["target_stability"] == stability
            }
            == {Fraction(0), Fraction(9, 25), Fraction(3, 4), Fraction(1)}
            for stability in pauli_rectangle["stability_values"]
        ),
        "pauli_branch_dephasing_erases_environment_evidence": all(
            row["branch_dephased_environment_trace_distance_squared"] == 0
            for row in rectangle_rows
        ),
    }
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "schema_version": "1.0",
        "probe": "du_central_record_interface_selection_probe",
        "claim_grade": (
            "EXACT FINITE RANDOM-UNITARY SPECIALIZATION AND MATCHED "
            "PAULI CONTROL / "
            "NO NOVEL-PHYSICS PROMOTION"
        ),
        "theorem_scope": (
            "finite Z2^k central-record theorem plus matched qubit Pauli "
            "finite-time controls with explicit branch environments"
        ),
        "models": models,
        "uniform_character_orthogonality": orthogonality,
        "degeneracy_nonselection": degeneracy,
        "coordinate_naturality": naturality,
        "noncommuting_perturbation": perturbation,
        "environment_gauge": environment_gauge,
        "coherent_environment_access": coherent_access,
        "repeated_fragments": repeated_fragments,
        "approximate_pauli_separation": approximate_pauli,
        "pauli_stability_formation_rectangle": pauli_rectangle,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "CENTRAL_RECORD_INTERFACE_AND_PAULI_RECTANGLE_PASS"
            if not failures
            else "SCOPED_THEOREM_OR_CONTROL_FAILED"
        ),
        "does_not_establish": (
            "a derived physical channel",
            "a selected system/environment cut",
            "natural or dephasing-robust coherent environment access",
            "an observer or public finality",
            "proper time or geometry",
            "robust approximate selection",
            "record-first ontology",
            "a new theorem component or physical law",
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    return result


if __name__ == "__main__":
    receipt = run()
    print(
        f"{receipt['verdict']}: "
        f"{receipt['check_count'] - receipt['failure_count']}/"
        f"{receipt['check_count']} checks"
    )
    raise SystemExit(1 if receipt["failures"] else 0)
