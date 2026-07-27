#!/usr/bin/env python3
"""Exact regression certificate for N5-RS-P3 / HC-DU-052.

The analytic result lives in:
  explorations/3-plus-1-law-filtered-record-assisted-reconstruction-and-causal-exterior-remainder-2026-07-27.md

This is not a spacetime solver, numerical-relativity calculation, detector
model, CFS model, or proof of hyperbolic existence. It preserves the exact
finite response-matrix consequences of the frozen analytic solution family:

* local scalar/vector records reconstruct their three source coefficients;
* two incoming TT modes lie in the local-record kernel;
* both TT modes change a held-out gauge-invariant future target;
* no-incoming-radiation closes the target by law/source restriction; and
* adding the full incoming characteristic archive closes it only by
  resource-expanded injective tomography.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_3plus1_lawful_causal_remainder_result.json"
)

Vector = tuple[Fraction, ...]
Matrix = tuple[Vector, ...]
CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def matrix_text(matrix: Matrix) -> list[list[str]]:
    return [[fraction_text(value) for value in row] for row in matrix]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((entry * value for entry, value in zip(row, vector, strict=True)), Fraction())
        for row in matrix
    )


def stack(*matrices: Matrix) -> Matrix:
    return tuple(row for matrix in matrices for row in matrix)


def rref(matrix: Matrix) -> tuple[Matrix, tuple[int, ...]]:
    rows = [list(row) for row in matrix]
    if not rows:
        return (), ()
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("ragged matrix")

    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(width):
        candidate = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column] != 0),
            None,
        )
        if candidate is None:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor != 0:
                rows[row] = [
                    entry - factor * pivot
                    for entry, pivot in zip(rows[row], rows[pivot_row], strict=True)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return tuple(tuple(row) for row in rows), tuple(pivot_columns)


def rank(matrix: Matrix) -> int:
    return len(rref(matrix)[1])


def nullspace(matrix: Matrix) -> tuple[Vector, ...]:
    reduced, pivots = rref(matrix)
    width = len(matrix[0]) if matrix else 0
    free_columns = [column for column in range(width) if column not in pivots]
    basis: list[Vector] = []
    for free in free_columns:
        vector = [Fraction() for _ in range(width)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        basis.append(tuple(vector))
    return tuple(basis)


def solve_square(matrix: Matrix, output: Vector) -> Vector:
    if len(matrix) != len(output) or any(len(row) != len(output) for row in matrix):
        raise ValueError("square system required")
    augmented = tuple(
        tuple(row) + (value,) for row, value in zip(matrix, output, strict=True)
    )
    reduced, pivots = rref(augmented)
    if pivots[: len(output)] != tuple(range(len(output))):
        raise ValueError("singular system")
    return tuple(reduced[index][-1] for index in range(len(output)))


def all_zero(values: Iterable[Fraction]) -> bool:
    return all(value == 0 for value in values)


def main() -> int:
    # Coordinates: scalar source a, scalar source b, vector/current c,
    # incoming plus polarization, incoming cross polarization.
    record_matrix: Matrix = (
        (Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1, 4), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    )
    target_matrix: Matrix = (
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    incoming_archive: Matrix = target_matrix
    plus_witness: Vector = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
        Fraction(0),
    )
    cross_witness: Vector = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )

    record_rank = rank(record_matrix)
    joined_rank = rank(stack(record_matrix, target_matrix))
    record_kernel = nullspace(record_matrix)

    record("record_rank_three", record_rank == 3, record_rank)
    record("record_nullity_two", len(record_kernel) == 2, len(record_kernel))
    record(
        "record_kernel_is_exactly_radiative",
        set(record_kernel) == {plus_witness, cross_witness},
        [list(map(fraction_text, vector)) for vector in record_kernel],
    )
    record(
        "plus_is_record_null",
        all_zero(matvec(record_matrix, plus_witness)),
        list(map(fraction_text, matvec(record_matrix, plus_witness))),
    )
    record(
        "cross_is_record_null",
        all_zero(matvec(record_matrix, cross_witness)),
        list(map(fraction_text, matvec(record_matrix, cross_witness))),
    )
    record(
        "plus_changes_target",
        matvec(target_matrix, plus_witness) == (Fraction(1), Fraction(0)),
        list(map(fraction_text, matvec(target_matrix, plus_witness))),
    )
    record(
        "cross_changes_target",
        matvec(target_matrix, cross_witness) == (Fraction(0), Fraction(1)),
        list(map(fraction_text, matvec(target_matrix, cross_witness))),
    )
    record("record_plus_target_rank_five", joined_rank == 5, joined_rank)
    record(
        "local_record_does_not_factor_target",
        joined_rank > record_rank,
        {"record_rank": record_rank, "joined_rank": joined_rank},
    )

    # The scalar/vector block is invertible: records genuinely assist rather
    # than merely restating law-only closure.
    local_block: Matrix = tuple(tuple(row[:3]) for row in record_matrix)
    sample_sources: Vector = (Fraction(2), Fraction(-1), Fraction(3))
    sample_record = matvec(local_block, sample_sources)
    recovered_sources = solve_square(local_block, sample_record)
    record(
        "local_source_sector_reconstructed",
        recovered_sources == sample_sources,
        {
            "record": list(map(fraction_text, sample_record)),
            "recovered": list(map(fraction_text, recovered_sources)),
        },
    )

    # Adding the complete incoming characteristic archive is injective
    # resource expansion, not a repair by the original local record.
    augmented = stack(record_matrix, incoming_archive)
    record(
        "incoming_archive_is_injective_completion",
        rank(augmented) == 5 and not nullspace(augmented),
        {"rank": rank(augmented), "nullity": len(nullspace(augmented))},
    )
    record(
        "incoming_archive_directly_contains_target",
        incoming_archive == target_matrix,
        matrix_text(incoming_archive),
    )

    # Under the no-incoming-radiation subspace p_+=p_x=0, the target is
    # identically zero before records are consulted.
    no_incoming_basis: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    )
    no_incoming_target = tuple(
        matvec(target_matrix, vector) for vector in no_incoming_basis
    )
    record(
        "no_incoming_radiation_gives_law_only_closure",
        all(all_zero(values) for values in no_incoming_target),
        [list(map(fraction_text, values)) for values in no_incoming_target],
    )

    # A one-polarization restriction is the smallest exact remainder.
    one_polarization_matrix: Matrix = tuple(
        tuple(row[index] for index in (0, 1, 2, 3)) for row in record_matrix
    )
    one_polarization_target: Matrix = (
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    record(
        "one_polarization_is_smallest_witness",
        rank(one_polarization_matrix) == 3
        and rank(stack(one_polarization_matrix, one_polarization_target)) == 4,
        {
            "record_rank": rank(one_polarization_matrix),
            "joined_rank": rank(stack(one_polarization_matrix, one_polarization_target)),
        },
    )

    verdict = "LAWFUL_SAME_RECORD_DIFFERENT_TARGET"
    passed = all(bool(check["passed"]) for check in CHECKS)
    artifact = {
        "schema_version": "1.0",
        "work_id": "N5-RS-P3",
        "claim_id": "HC-DU-052",
        "verdict": verdict,
        "attribution": "CAUSAL_EXTERIOR_OPEN_BOUNDARY_REMAINDER",
        "coordinate_order": ["a", "b", "c", "p_plus", "p_cross"],
        "record_matrix": matrix_text(record_matrix),
        "target_matrix": matrix_text(target_matrix),
        "record_rank": record_rank,
        "record_nullity": len(record_kernel),
        "joined_rank": joined_rank,
        "law_only_target_dimension": 2,
        "record_conditioned_target_dimension": 2,
        "controls": {
            "no_incoming_radiation": "LAW_ONLY_TARGET_CLOSURE",
            "full_characteristic_archive": "INJECTIVE_TOMOGRAPHY_ONLY",
            "local_scalar_vector_sector": "STRICT_RECORD_ASSISTED_RECONSTRUCTION",
        },
        "checks": CHECKS,
        "passed": passed,
        "scope": [
            "exact finite response-matrix regression",
            "linearized 3+1 Einstein--matter analytic solution family",
            "known hyperbolic and characteristic-Cauchy mathematics",
            "not a spacetime simulation",
            "not new physics or a prediction",
        ],
    }
    ARTIFACT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n")

    print(
        f"{verdict}: {sum(bool(check['passed']) for check in CHECKS)}/{len(CHECKS)} checks"
    )
    print(f"artifact: {ARTIFACT.relative_to(ROOT)}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
