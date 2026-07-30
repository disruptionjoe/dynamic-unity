#!/usr/bin/env python3
"""Exact reduced-QRF loop-defect and path-order fixture for HC-DU-155.

Passing establishes only:

1. an invertible full transformation can close exactly while its
   discard-and-refresh reduced loop does not;
2. the reduced-loop defect is exactly the information removed by the
   intermediate access reduction;
3. two trace-preserving conditional expectations onto noncommuting qubit
   algebras can be path-order dependent; and
4. the path-order statistic is invariant when states, access maps, and
   readout are transformed together.

It does not realize a laboratory quantum-reference-frame loop, select a
reference, factorization, assignment, access boundary, record algebra,
archive, certification rule, or physical reconciliation path.  It does not
establish perspectival curvature, new dynamics, empirical excess, hardware
need, or paper readiness.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_qrf_reduced_loop_curvature_gate_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def matrix(rows: Iterable[Iterable[int | Fraction]]) -> Matrix:
    return tuple(tuple(Fraction(entry) for entry in row) for row in rows)


def zeros(rows: int, columns: int) -> Matrix:
    return tuple(
        tuple(Fraction(0) for _ in range(columns)) for _ in range(rows)
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column] for row in range(len(value)))
        for column in range(len(value[0]))
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                left[row][inner] * right[inner][column]
                for inner in range(len(right))
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def apply_unitary(unitary: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(unitary, rho), transpose(unitary))


def trace(value: Matrix) -> Fraction:
    return sum(value[index][index] for index in range(len(value)))


def expectation(effect: Matrix, rho: Matrix) -> Fraction:
    return trace(matmul(effect, rho))


def trace_out_second_qubit(rho: Matrix) -> Matrix:
    # Basis order is |system, carrier>.
    return tuple(
        tuple(
            sum(
                rho[2 * system + carrier][2 * other_system + carrier]
                for carrier in range(2)
            )
            for other_system in range(2)
        )
        for system in range(2)
    )


def permutation_matrix(
    dimension: int, mapping: Callable[[int], int]
) -> Matrix:
    rows = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    images = [mapping(index) for index in range(dimension)]
    if sorted(images) != list(range(dimension)):
        raise AssertionError(f"mapping is not a permutation: {images}")
    for source, target in enumerate(images):
        rows[target][source] = Fraction(1)
    return tuple(tuple(row) for row in rows)


def basis_matrix(row: int, column: int, dimension: int = 2) -> Matrix:
    return tuple(
        tuple(
            Fraction(1) if (i, j) == (row, column) else Fraction(0)
            for j in range(dimension)
        )
        for i in range(dimension)
    )


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(a * b for a, b in zip(left, right, strict=True))


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(tuple(a * b for b in right) for a in left)


def matvec(operator: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(operator[row][column] * vector[column] for column in range(len(vector)))
        for row in range(len(operator))
    )


def compose(left: Matrix, right: Matrix) -> Matrix:
    return matmul(left, right)


def rotate(rotation: Matrix, vector: Vector) -> Vector:
    return matvec(rotation, vector)


def probability_from_bloch(readout_axis: Vector, state_vector: Vector) -> Fraction:
    return (Fraction(1) + dot(readout_axis, state_vector)) / 2


def as_json(value: Fraction | Matrix | Vector) -> object:
    if isinstance(value, Fraction):
        return (
            int(value)
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        )
    if value and isinstance(value[0], tuple):
        return [[as_json(entry) for entry in row] for row in value]  # type: ignore[arg-type]
    return [as_json(entry) for entry in value]  # type: ignore[arg-type]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    zero = matrix(((1, 0), (0, 0)))
    plus = matrix(
        (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(1, 2)),
        )
    )
    maximally_mixed = matrix(
        (
            (Fraction(1, 2), 0),
            (0, Fraction(1, 2)),
        )
    )

    cnot = permutation_matrix(
        4,
        lambda index: 2 * (index // 2) + ((index % 2) ^ (index // 2)),
    )
    identity_four = matrix(
        tuple(
            tuple(1 if row == column else 0 for column in range(4))
            for row in range(4)
        )
    )

    initial_joint = kron(plus, zero)
    forward_joint = apply_unitary(cnot, initial_joint)
    retained_return_joint = apply_unitary(cnot, forward_joint)
    retained_return = trace_out_second_qubit(retained_return_joint)

    reduced_after_forward = trace_out_second_qubit(forward_joint)
    refreshed_joint = kron(reduced_after_forward, zero)
    reduced_return_joint = apply_unitary(cnot, refreshed_joint)
    reduced_return = trace_out_second_qubit(reduced_return_joint)

    x_plus_probability_before = expectation(plus, plus)
    x_plus_probability_after_reduced_loop = expectation(plus, reduced_return)
    reduced_loop_probability_defect = (
        x_plus_probability_before - x_plus_probability_after_reduced_loop
    )

    # Verify the exact assignment/reduction loop identity on a basis of the
    # complete input operator space:
    #
    # L - id = R U (J R - id) U J.
    loop_identity_residuals: list[Matrix] = []
    for row in range(2):
        for column in range(2):
            input_operator = basis_matrix(row, column)
            assigned = kron(input_operator, zero)
            forward = apply_unitary(cnot, assigned)
            reduced = trace_out_second_qubit(forward)
            reassigned = kron(reduced, zero)
            loop_output = trace_out_second_qubit(
                apply_unitary(cnot, reassigned)
            )
            discarded_component = subtract(reassigned, forward)
            loss_term = trace_out_second_qubit(
                apply_unitary(cnot, discarded_component)
            )
            loop_identity_residuals.append(
                subtract(subtract(loop_output, input_operator), loss_term)
            )

    zero_two = zeros(2, 2)

    # Each Bloch projection is the trace-preserving conditional expectation
    # onto span{I, axis.sigma}.  Nonparallel, nonorthogonal axes yield
    # noncommuting reductions.
    axis_z: Vector = (Fraction(0), Fraction(0), Fraction(1))
    axis_b: Vector = (Fraction(3, 5), Fraction(0), Fraction(4, 5))
    axis_x: Vector = (Fraction(1), Fraction(0), Fraction(0))
    input_bloch = axis_z
    readout_x = axis_x

    dephase_z = outer(axis_z, axis_z)
    dephase_b = outer(axis_b, axis_b)
    dephase_x = outer(axis_x, axis_x)

    path_z_then_b = matvec(compose(dephase_b, dephase_z), input_bloch)
    path_b_then_z = matvec(compose(dephase_z, dephase_b), input_bloch)
    path_difference = tuple(
        left - right
        for left, right in zip(path_z_then_b, path_b_then_z, strict=True)
    )
    probability_z_then_b = probability_from_bloch(readout_x, path_z_then_b)
    probability_b_then_z = probability_from_bloch(readout_x, path_b_then_z)
    path_probability_difference = probability_z_then_b - probability_b_then_z
    if path_difference[1:] != (Fraction(0), Fraction(0)):
        raise AssertionError("fixture trace-distance shortcut requires an x-only difference")
    path_trace_distance = abs(path_difference[0]) / 2

    noncommuting_reduction_commutator = subtract(
        compose(dephase_b, dephase_z),
        compose(dephase_z, dephase_b),
    )
    commuting_identical = compose(dephase_z, dephase_z) == dephase_z
    commuting_orthogonal = (
        compose(dephase_x, dephase_z) == compose(dephase_z, dephase_x)
    )

    # A common 90-degree y-axis rotation: (x,y,z) -> (z,y,-x).
    representation_rotation = matrix(((0, 0, 1), (0, 1, 0), (-1, 0, 0)))
    rotated_z = rotate(representation_rotation, axis_z)
    rotated_b = rotate(representation_rotation, axis_b)
    rotated_input = rotate(representation_rotation, input_bloch)
    rotated_readout = rotate(representation_rotation, readout_x)
    rotated_dephase_z = outer(rotated_z, rotated_z)
    rotated_dephase_b = outer(rotated_b, rotated_b)
    rotated_path_z_then_b = matvec(
        compose(rotated_dephase_b, rotated_dephase_z), rotated_input
    )
    rotated_path_b_then_z = matvec(
        compose(rotated_dephase_z, rotated_dephase_b), rotated_input
    )
    rotated_probability_z_then_b = probability_from_bloch(
        rotated_readout, rotated_path_z_then_b
    )
    rotated_probability_b_then_z = probability_from_bloch(
        rotated_readout, rotated_path_b_then_z
    )

    checks = {
        "full_transform_is_an_involution": matmul(cnot, cnot) == identity_four,
        "retained_lineage_full_loop_closes": retained_return_joint == initial_joint,
        "retained_lineage_accessible_state_closes": retained_return == plus,
        "intermediate_reduction_dephases_coherent_input": (
            reduced_after_forward == maximally_mixed
        ),
        "discard_and_refresh_reduced_loop_fails": reduced_return == maximally_mixed,
        "reduced_loop_x_probability_defect_is_one_half": (
            reduced_loop_probability_defect == Fraction(1, 2)
        ),
        "loop_defect_equals_discarded_lineage_term": all(
            residual == zero_two for residual in loop_identity_residuals
        ),
        "noncommuting_axes_are_unit_and_nonexceptional": (
            dot(axis_b, axis_b) == 1
            and dot(axis_z, axis_b) == Fraction(4, 5)
        ),
        "z_then_b_output_is_exact": (
            path_z_then_b
            == (Fraction(12, 25), Fraction(0), Fraction(16, 25))
        ),
        "b_then_z_output_is_exact": (
            path_b_then_z
            == (Fraction(0), Fraction(0), Fraction(16, 25))
        ),
        "path_difference_is_exact": (
            path_difference
            == (Fraction(12, 25), Fraction(0), Fraction(0))
        ),
        "path_readout_difference_is_six_twenty_fifths": (
            path_probability_difference == Fraction(6, 25)
        ),
        "path_trace_distance_is_six_twenty_fifths": (
            path_trace_distance == Fraction(6, 25)
        ),
        "conditional_expectations_do_not_commute": (
            noncommuting_reduction_commutator != zeros(3, 3)
        ),
        "identical_conditional_expectations_are_idempotent": commuting_identical,
        "orthogonal_pauli_conditional_expectations_commute": commuting_orthogonal,
        "covariant_path_outputs_rotate_together": (
            rotated_path_z_then_b
            == rotate(representation_rotation, path_z_then_b)
            and rotated_path_b_then_z
            == rotate(representation_rotation, path_b_then_z)
        ),
        "covariant_readout_probabilities_are_invariant": (
            rotated_probability_z_then_b == probability_z_then_b
            and rotated_probability_b_then_z == probability_b_then_z
        ),
    }

    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    result = {
        "claim_id": "HC-DU-155",
        "return": (
            "REDUCED_LOOP_DEFECT_FROM_DISCARDED_LINEAGE"
            "+NONCOMMUTING_REDUCTION_PATH_DEPENDENCE"
            "+REPRESENTATION_COVARIANT_STATISTICS"
            "+STANDARD_QM_COARSE_GRAINING_ABSORPTION"
            "+NO_READY_SUCCESSOR"
        ),
        "checks": checks,
        "forward_return_fixture": {
            "full_transform_squared": as_json(matmul(cnot, cnot)),
            "initial_accessible_state": as_json(plus),
            "retained_lineage_return_state": as_json(retained_return),
            "discard_and_refresh_return_state": as_json(reduced_return),
            "x_plus_probability_before": as_json(x_plus_probability_before),
            "x_plus_probability_after_reduced_loop": as_json(
                x_plus_probability_after_reduced_loop
            ),
            "probability_defect": as_json(reduced_loop_probability_defect),
        },
        "path_order_fixture": {
            "axis_a": as_json(axis_z),
            "axis_b": as_json(axis_b),
            "axis_overlap": as_json(dot(axis_z, axis_b)),
            "z_then_b_output": as_json(path_z_then_b),
            "b_then_z_output": as_json(path_b_then_z),
            "path_difference": as_json(path_difference),
            "x_plus_probability_z_then_b": as_json(probability_z_then_b),
            "x_plus_probability_b_then_z": as_json(probability_b_then_z),
            "probability_difference": as_json(path_probability_difference),
            "trace_distance": as_json(path_trace_distance),
            "conditional_expectation_commutator": as_json(
                noncommuting_reduction_commutator
            ),
        },
        "scope": [
            "Full reversible frame transformations and reduced access channels are different typed objects.",
            "A reduced loop defect can be caused entirely by discarded lineage.",
            "Noncommuting access reductions can create ordinary path-order dependence.",
            "Perspectival curvature requires an invariant excess after complete lineage and representation controls.",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
