#!/usr/bin/env python3
"""Exact regression certificate for N5-RS-P4 / HC-DU-053.

The analytic result lives in:
  explorations/3-plus-1-causally-closed-noninjective-transfer-and-first-recoupling-2026-07-27.md

This is not a numerical-relativity calculation, detector simulation, proof of
characteristic existence, or independent physical-record formation model. It
preserves the exact finite consequences of the frozen two-polarization
transport contract:

* the complete incoming variable family is inside the completion class;
* a quadratic intensity record is strictly noninjective but predicts a later
  polarization-insensitive response under every admitted orthogonal transport;
* an orientation-sensitive capability exposes a same-record interior
  remainder;
* a one-component record transfers under aligned propagation and fails at the
  first hidden-to-visible polarization recoupling; and
* full two-polarization repair is injective tomography.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_3plus1_closed_noninjective_transfer_result.json"
)

Vector = tuple[Fraction, ...]
Matrix = tuple[Vector, ...]
CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def vector_text(vector: Vector) -> list[str]:
    return [fraction_text(value) for value in vector]


def matrix_text(matrix: Matrix) -> list[list[str]]:
    return [vector_text(row) for row in matrix]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (entry * value for entry, value in zip(row, vector, strict=True)),
            Fraction(),
        )
        for row in matrix
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return ()
    columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(row, column, strict=True)),
                Fraction(),
            )
            for column in columns
        )
        for row in left
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(column) for column in zip(*matrix, strict=True))


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
                    for entry, pivot in zip(
                        rows[row], rows[pivot_row], strict=True
                    )
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


def determinant_2(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def quadratic_norm(vector: Vector) -> Fraction:
    return sum((value * value for value in vector), Fraction())


def linear_factors(record_matrix: Matrix, target_matrix: Matrix) -> bool:
    return rank(stack(record_matrix, target_matrix)) == rank(record_matrix)


def law_only_box_diameter(row: Vector) -> Fraction:
    """Diameter of row*x over x in [-1,1]^2."""

    return Fraction(2) * sum((abs(value) for value in row), Fraction())


def conditioned_box_diameter(row: Vector) -> Fraction:
    """Diameter after fixing x_plus for the record R=(1,0)."""

    return Fraction(2) * abs(row[1])


def main() -> int:
    # Complete incoming characteristic variables in the frozen finite packet
    # sector: plus and cross TT amplitudes.
    identity: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    aligned_transport: Matrix = identity
    mixed_transport: Matrix = (
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(-4, 5), Fraction(3, 5)),
    )
    plus_readout: Matrix = ((Fraction(1), Fraction(0)),)
    plus_record: Matrix = plus_readout
    full_incoming_archive: Matrix = identity

    e_plus: Vector = (Fraction(1), Fraction(0))
    minus_e_plus: Vector = (Fraction(-1), Fraction(0))
    e_cross: Vector = (Fraction(0), Fraction(1))
    zero: Vector = (Fraction(0), Fraction(0))

    aligned_target = matmul(plus_readout, aligned_transport)
    mixed_target = matmul(plus_readout, mixed_transport)
    aligned_recoupling = matvec(aligned_target, e_cross)[0]
    mixed_recoupling = matvec(mixed_target, e_cross)[0]

    record(
        "incoming_characteristic_family_is_two_dimensional_and_complete_in_sector",
        rank(full_incoming_archive) == 2,
        {"rank": rank(full_incoming_archive), "variables": ["p_plus", "p_cross"]},
    )
    record(
        "aligned_transport_is_orthogonal",
        matmul(transpose(aligned_transport), aligned_transport) == identity,
        matrix_text(matmul(transpose(aligned_transport), aligned_transport)),
    )
    record(
        "mixed_transport_is_orthogonal",
        matmul(transpose(mixed_transport), mixed_transport) == identity,
        matrix_text(matmul(transpose(mixed_transport), mixed_transport)),
    )
    record(
        "mixed_transport_preserves_orientation",
        determinant_2(mixed_transport) == 1,
        fraction_text(determinant_2(mixed_transport)),
    )

    # Primary noninjective record: normalized quadratic polarization
    # intensity. Orthogonal transport preserves it exactly.
    specimens = (
        zero,
        e_plus,
        minus_e_plus,
        e_cross,
        (Fraction(1), Fraction(1)),
        (Fraction(1, 2), Fraction(-1, 3)),
    )
    intensity_invariant = all(
        quadratic_norm(matvec(transport, vector)) == quadratic_norm(vector)
        for transport in (aligned_transport, mixed_transport)
        for vector in specimens
    )
    record(
        "quadratic_intensity_is_transport_invariant",
        intensity_invariant,
        {
            "transports": ["aligned", "mixed"],
            "specimens": [vector_text(vector) for vector in specimens],
        },
    )
    record(
        "intensity_record_is_strictly_noninjective",
        e_plus != e_cross
        and quadratic_norm(e_plus) == quadratic_norm(e_cross) == 1,
        {
            "plus": vector_text(e_plus),
            "cross": vector_text(e_cross),
            "common_record": fraction_text(quadratic_norm(e_plus)),
        },
    )
    record(
        "law_only_intensity_target_varies",
        quadratic_norm(zero) == 0 and quadratic_norm((Fraction(1), Fraction(1))) == 2,
        {"diameter_on_box": "2/1"},
    )
    record(
        "one_decoder_transfers_intensity_without_refit",
        all(
            quadratic_norm(matvec(transport, vector)) == quadratic_norm(vector)
            for transport in (aligned_transport, mixed_transport)
            for vector in specimens
        ),
        "decoder(q)=q for aligned and mixed transport",
    )
    record(
        "intensity_record_closes_polarization_insensitive_target",
        intensity_invariant,
        {"law_only_diameter": "2/1", "record_conditioned_diameter": "0/1"},
    )

    # Capability enlargement: the same intensity record does not reconstruct
    # an oriented signed response.
    oriented_plus = matvec(mixed_target, e_plus)[0]
    oriented_minus = matvec(mixed_target, minus_e_plus)[0]
    record(
        "orientation_sensitive_capability_reopens_intensity_fibre",
        quadratic_norm(e_plus) == quadratic_norm(minus_e_plus)
        and oriented_plus != oriented_minus,
        {
            "common_intensity": "1/1",
            "target_plus": fraction_text(oriented_plus),
            "target_minus": fraction_text(oriented_minus),
        },
    )

    # Linear positive and hostile controls. The plus record transfers under
    # aligned propagation. A lawful polarization rotation recouples the
    # hidden cross direction into the later plus response.
    plus_rank = rank(plus_record)
    plus_kernel = nullspace(plus_record)
    record("plus_record_rank_one", plus_rank == 1, plus_rank)
    record(
        "plus_record_hidden_direction_is_cross",
        plus_kernel == (e_cross,),
        [vector_text(vector) for vector in plus_kernel],
    )
    record(
        "aligned_plus_target_factors_through_record",
        linear_factors(plus_record, aligned_target),
        {
            "record_rank": plus_rank,
            "joined_rank": rank(stack(plus_record, aligned_target)),
        },
    )
    record(
        "aligned_hidden_to_visible_block_is_zero",
        aligned_recoupling == 0,
        fraction_text(aligned_recoupling),
    )
    record(
        "aligned_transfer_is_strictly_noninjective_and_not_law_only",
        plus_rank < 2
        and rank(aligned_target) == 1
        and conditioned_box_diameter(aligned_target[0]) == 0,
        {
            "state_dimension": 2,
            "record_rank": plus_rank,
            "law_only_diameter": fraction_text(
                law_only_box_diameter(aligned_target[0])
            ),
            "record_conditioned_diameter": fraction_text(
                conditioned_box_diameter(aligned_target[0])
            ),
        },
    )
    record(
        "mixed_plus_target_does_not_factor_through_record",
        not linear_factors(plus_record, mixed_target),
        {
            "record_rank": plus_rank,
            "joined_rank": rank(stack(plus_record, mixed_target)),
        },
    )
    record(
        "mixed_hidden_to_visible_block_is_four_fifths",
        mixed_recoupling == Fraction(4, 5),
        fraction_text(mixed_recoupling),
    )
    record(
        "mixed_cross_witness_changes_target",
        matvec(plus_record, e_cross) == (Fraction(0),)
        and matvec(mixed_target, e_cross) == (Fraction(4, 5),),
        {
            "record": vector_text(matvec(plus_record, e_cross)),
            "target": vector_text(matvec(mixed_target, e_cross)),
        },
    )
    record(
        "mixed_target_has_positive_conditioned_diameter",
        law_only_box_diameter(mixed_target[0]) == Fraction(14, 5)
        and conditioned_box_diameter(mixed_target[0]) == Fraction(8, 5),
        {
            "law_only_diameter": fraction_text(
                law_only_box_diameter(mixed_target[0])
            ),
            "record_conditioned_diameter": fraction_text(
                conditioned_box_diameter(mixed_target[0])
            ),
        },
    )

    # Strong controls: the full archive is injective; replacing the old
    # record by the back-propagated target row repairs only by target-specific
    # interface refit.
    record(
        "full_incoming_archive_is_injective_tomography",
        rank(full_incoming_archive) == 2 and not nullspace(full_incoming_archive),
        {"rank": rank(full_incoming_archive), "nullity": len(nullspace(full_incoming_archive))},
    )
    record(
        "full_output_capability_exceeds_plus_record",
        not linear_factors(plus_record, mixed_transport),
        {
            "record_rank": plus_rank,
            "joined_rank": rank(stack(plus_record, mixed_transport)),
        },
    )
    target_fitted_record = mixed_target
    record(
        "back_propagated_target_row_repairs_only_by_interface_change",
        linear_factors(target_fitted_record, mixed_target)
        and target_fitted_record != plus_record,
        {
            "old_record": matrix_text(plus_record),
            "fitted_record": matrix_text(target_fitted_record),
        },
    )

    verdict = "STRICT_NONINJECTIVE_TRANSFER_WITH_INTERIOR_FIRST_RECOUPLING"
    passed = all(bool(check["passed"]) for check in CHECKS)
    artifact = {
        "schema_version": "1.0",
        "work_id": "N5-RS-P4",
        "claim_id": "HC-DU-053",
        "verdict": verdict,
        "attribution": "CAUSALLY_CLOSED_TARGET_AND_CAPABILITY_RELATIVE",
        "coordinate_order": ["p_plus", "p_cross"],
        "transports": {
            "aligned": matrix_text(aligned_transport),
            "mixed": matrix_text(mixed_transport),
        },
        "primary_record": "I=p_plus^2+p_cross^2",
        "primary_target": "downstream normalized polarization-insensitive quadratic response",
        "primary_law_only_target_diameter": "2/1",
        "primary_record_conditioned_target_diameter": "0/1",
        "linear_control": {
            "record_matrix": matrix_text(plus_record),
            "aligned_target": matrix_text(aligned_target),
            "mixed_target": matrix_text(mixed_target),
            "aligned_first_recoupling": fraction_text(aligned_recoupling),
            "mixed_first_recoupling": fraction_text(mixed_recoupling),
            "mixed_law_only_diameter": fraction_text(
                law_only_box_diameter(mixed_target[0])
            ),
            "mixed_record_conditioned_diameter": fraction_text(
                conditioned_box_diameter(mixed_target[0])
            ),
        },
        "controls": {
            "primary_intensity_target": "STRICT_RECORD_RECONSTRUCTION",
            "orientation_sensitive_capability": "CAPABILITY_RELATIVE_REMAINDER",
            "aligned_plus_transfer": "STRICT_RECORD_RECONSTRUCTION",
            "mixed_plus_transfer": "SAME_RECORD_DIFFERENT_TARGET",
            "full_characteristic_archive": "INJECTIVE_TOMOGRAPHY",
            "back_propagated_target_row": "TARGET_CODED_INTERFACE_REFIT",
        },
        "interface_grade": "SUPPLIED_TARGET_INDEPENDENT_PROBE_LIMIT_ARCHIVE",
        "checks": CHECKS,
        "passed": passed,
        "scope": [
            "exact finite factorization and rational matrix regression",
            "complete two-polarization incoming family within a frozen geometric-optics packet sector",
            "known 3+1 general-relativistic polarization transport",
            "record formation coupling supplied rather than Einstein-selected",
            "not a numerical-relativity or detector simulation",
            "not a new GR theorem, new physics, ontology, or prediction",
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
