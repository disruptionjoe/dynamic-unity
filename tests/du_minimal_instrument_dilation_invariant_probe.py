#!/usr/bin/env python3
"""Exact finite controls for HC-DU-165.

Passing proves only the two-rank separation, Kraus-basis freedom, redundant
realization, and finite fixed-algebra controls declared by the governed audit.
It does not identify a physical apparatus, archive, carrier, provenance chain,
reset protocol, observer boundary, realized outcome, or new physics.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_minimal_instrument_dilation_invariant_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]


def exact_rank(matrix: Matrix) -> int:
    """Return matrix rank by exact rational row reduction."""
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    pivot_row = 0
    for column in range(n_cols):
        pivot = next(
            (
                row
                for row in range(pivot_row, n_rows)
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def zero_matrix(rows: int, columns: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def freeze(matrix: list[list[Fraction]]) -> Matrix:
    return tuple(tuple(row) for row in matrix)


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column] for inner in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix))) for column in range(len(matrix[0])))


def matrix_unit(row: int, column: int, dimension: int = 2) -> Matrix:
    return tuple(
        tuple(Fraction(int(i == row and j == column)) for j in range(dimension))
        for i in range(dimension)
    )


def apply_kraus(kraus: tuple[Matrix, ...], operator: Matrix) -> Matrix:
    result = freeze(zero_matrix(len(operator), len(operator)))
    for item in kraus:
        result = matrix_add(
            result,
            matrix_multiply(matrix_multiply(item, operator), matrix_transpose(item)),
        )
    return result


def projective_liouville(outcome: int) -> Matrix:
    selected = 0 if outcome == 0 else 3
    return tuple(
        tuple(
            Fraction(int(row == selected and column == selected))
            for column in range(4)
        )
        for row in range(4)
    )


def projective_choi(outcome: int) -> Matrix:
    selected = 0 if outcome == 0 else 3
    return tuple(
        tuple(
            Fraction(int(row == selected and column == selected))
            for column in range(4)
        )
        for row in range(4)
    )


def coin_liouville() -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column), 2) for column in range(4))
        for row in range(4)
    )


def coin_choi() -> Matrix:
    vectorized_identity = (1, 0, 0, 1)
    return tuple(
        tuple(
            Fraction(
                vectorized_identity[row] * vectorized_identity[column],
                2,
            )
            for column in range(4)
        )
        for row in range(4)
    )


def replacer_liouville() -> Matrix:
    return (
        (Fraction(1, 2), 0, 0, Fraction(1, 2)),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (Fraction(1, 2), 0, 0, Fraction(1, 2)),
    )


def replacer_choi() -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column), 2) for column in range(4))
        for row in range(4)
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    product_lr = matrix_multiply(left, right)
    product_rl = matrix_multiply(right, left)
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(product_lr, product_rl)
    )


def commutes(left: Matrix, right: Matrix) -> bool:
    return all(
        value == 0
        for row in commutator(left, right)
        for value in row
    )


def commutant_constraint_matrix(
    dimension: int,
    generators: tuple[Matrix, ...],
) -> Matrix:
    """Linear equations for A G - G A = 0 in row-major A coordinates."""
    constraints: list[tuple[Fraction, ...]] = []
    for generator in generators:
        for output_row in range(dimension):
            for output_column in range(dimension):
                coefficients: list[Fraction] = []
                for variable_row in range(dimension):
                    for variable_column in range(dimension):
                        coefficient = Fraction(0)
                        if output_row == variable_row:
                            coefficient += generator[variable_column][output_column]
                        if output_column == variable_column:
                            coefficient -= generator[output_row][variable_row]
                        coefficients.append(coefficient)
                constraints.append(tuple(coefficients))
    return tuple(constraints)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    rank_table = {
        "ideal_0": {
            "liouville_rank": exact_rank(projective_liouville(0)),
            "choi_rank": exact_rank(projective_choi(0)),
        },
        "ideal_1": {
            "liouville_rank": exact_rank(projective_liouville(1)),
            "choi_rank": exact_rank(projective_choi(1)),
        },
        "coin_identity_outcome": {
            "liouville_rank": exact_rank(coin_liouville()),
            "choi_rank": exact_rank(coin_choi()),
        },
        "depolarizing_replacer": {
            "liouville_rank": exact_rank(replacer_liouville()),
            "choi_rank": exact_rank(replacer_choi()),
        },
    }

    projector_zero = matrix_unit(0, 0)
    projector_one = matrix_unit(1, 1)
    original_dephasing_kraus = (projector_zero, projector_one)
    rotated_dephasing_kraus = (
        (
            (Fraction(3, 5), 0),
            (0, Fraction(4, 5)),
        ),
        (
            (Fraction(-4, 5), 0),
            (0, Fraction(3, 5)),
        ),
    )
    kraus_rotation_equal = all(
        apply_kraus(original_dephasing_kraus, matrix_unit(row, column))
        == apply_kraus(rotated_dephasing_kraus, matrix_unit(row, column))
        for row in range(2)
        for column in range(2)
    )

    # E(X)=X/2 has one-dimensional Choi support, but this two-coordinate
    # Kraus list realizes it exactly and is therefore nonminimal.
    redundant_coin_kraus = (
        (
            (Fraction(1, 2), 0),
            (0, Fraction(1, 2)),
        ),
        (
            (Fraction(1, 2), 0),
            (0, Fraction(1, 2)),
        ),
    )
    redundant_coin_equal = all(
        apply_kraus(redundant_coin_kraus, matrix_unit(row, column))
        == tuple(
            tuple(value / 2 for value in output_row)
            for output_row in matrix_unit(row, column)
        )
        for row in range(2)
        for column in range(2)
    )

    # Sector profile (1, 2). The first generator separates outcome sectors;
    # the latter two generate the full two-dimensional within-sector algebra.
    sector_sign = (
        (-1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    sector_swap = (
        (1, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
    )
    sector_phase = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, -1),
    )
    generators = (sector_sign, sector_swap, sector_phase)
    constraints = commutant_constraint_matrix(3, generators)
    fixed_algebra_dimension = 9 - exact_rank(constraints)

    first_outcome_identity = (
        (1, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
    )
    second_outcome_identity = (
        (0, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    within_sector_non_scalar = (
        (0, 0, 0),
        (0, 1, 0),
        (0, 0, 0),
    )
    cross_sector_operator = (
        (0, 1, 0),
        (0, 0, 0),
        (0, 0, 0),
    )

    projective_profile = (
        rank_table["ideal_0"]["choi_rank"],
        rank_table["ideal_1"]["choi_rank"],
    )
    coin_profile = (
        rank_table["coin_identity_outcome"]["choi_rank"],
        rank_table["coin_identity_outcome"]["choi_rank"],
    )
    replacer_profile = (
        rank_table["depolarizing_replacer"]["choi_rank"],
    )

    checks = {
        "ideal_outcomes_have_rank_pair_1_1": (
            rank_table["ideal_0"] == {"liouville_rank": 1, "choi_rank": 1}
            and rank_table["ideal_1"] == {"liouville_rank": 1, "choi_rank": 1}
        ),
        "coin_identity_separates_operational_and_kraus_rank": (
            rank_table["coin_identity_outcome"]
            == {"liouville_rank": 4, "choi_rank": 1}
        ),
        "replacer_separates_kraus_and_operational_rank": (
            rank_table["depolarizing_replacer"]
            == {"liouville_rank": 1, "choi_rank": 4}
        ),
        "rational_within_sector_kraus_rotation_preserves_map": (
            kraus_rotation_equal
        ),
        "redundant_kraus_coordinates_preserve_coin_map": (
            redundant_coin_equal
        ),
        "fixed_algebra_dimension_equals_outcome_count": (
            fixed_algebra_dimension == 2
        ),
        "outcome_sector_identities_are_fixed": all(
            commutes(operator, generator)
            for operator in (first_outcome_identity, second_outcome_identity)
            for generator in generators
        ),
        "within_sector_basis_token_is_not_fixed": not all(
            commutes(within_sector_non_scalar, generator)
            for generator in generators
        ),
        "cross_sector_token_is_not_fixed": not all(
            commutes(cross_sector_operator, generator)
            for generator in generators
        ),
        "minimal_normal_dimension_profiles_follow_choi_ranks": (
            sum(projective_profile) == 2
            and sum(coin_profile) == 2
            and sum(replacer_profile) == 4
        ),
        "minimality_does_not_equal_operational_label_sufficiency": (
            rank_table["coin_identity_outcome"]["choi_rank"] == 1
            and rank_table["coin_identity_outcome"]["liouville_rank"] == 4
            and rank_table["depolarizing_replacer"]["choi_rank"] == 4
            and rank_table["depolarizing_replacer"]["liouville_rank"] == 1
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"minimal-instrument controls failed: {failed}")

    result = {
        "probe": "du_minimal_instrument_dilation_invariant_probe",
        "status": "PASS",
        "claim_id": "HC-DU-165",
        "scope": (
            "finite-dimensional rank separation, minimal normal apparatus "
            "multiplicity, Kraus gauge, and fixed-algebra controls"
        ),
        "rank_table": rank_table,
        "minimal_normal_apparatus_profiles": {
            "projective_two_outcome": {
                "sector_choi_ranks": list(projective_profile),
                "total_dimension": sum(projective_profile),
            },
            "coin_two_outcome": {
                "sector_choi_ranks": list(coin_profile),
                "total_dimension": sum(coin_profile),
            },
            "one_outcome_depolarizing_replacer": {
                "sector_choi_ranks": list(replacer_profile),
                "total_dimension": sum(replacer_profile),
            },
        },
        "gauge_controls": {
            "rational_kraus_rotation_preserves_map": kraus_rotation_equal,
            "redundant_two_coordinate_coin_realization_preserves_map": (
                redundant_coin_equal
            ),
            "sector_profile": [1, 2],
            "ambient_operator_dimension": 9,
            "constraint_rank": exact_rank(constraints),
            "fixed_algebra_dimension": fixed_algebra_dimension,
            "fixed_basis": [
                "identity_on_outcome_sector_0",
                "identity_on_outcome_sector_1",
            ],
        },
        "checks": checks,
        "boundary": (
            "The exact controls distinguish operational response rank from "
            "minimal Kraus multiplicity and show that only outcome-sector "
            "scalars are pointwise fixed under the tested full sector gauge. "
            "They do not select a material realization."
        ),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
