#!/usr/bin/env python3
"""Exact proportional controls for HC-DU-106.

The scientific result is analytic. This probe preserves:

1. simultaneous recovery of a three-parameter target from one four-source
   Boolean context design with three retained response channels;
2. the distinction between 16 source configurations and 48 retained scalar
   values;
3. full-rank point/tangent separation in the positive control; and
4. a same-packet/different-target witness when two response channels are used
   for a three-dimensional target.

Passing establishes no Lorentzian metric, nonlinear field, selected model
class, physical source or readout, formed event, record, geometry, novel
physics, prediction, or evidence grade.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_finite_dimensional_nonlinear_packet_result.json"
)

SourceSet = frozenset[int]
Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def power_set(source_count: int) -> tuple[SourceSet, ...]:
    sources = tuple(range(source_count))
    return tuple(
        frozenset(subset)
        for size in range(source_count + 1)
        for subset in combinations(sources, size)
    )


def vector_add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def vector_scale(scale: Fraction, vector: Vector) -> Vector:
    return tuple(scale * value for value in vector)


def multiaffine_context_values(
    theta: Vector,
    source_count: int,
) -> dict[SourceSet, Vector]:
    contexts = power_set(source_count)
    target_dimension = len(theta)
    coefficients: dict[SourceSet, Vector] = {}
    for source_set in contexts:
        if len(source_set) == source_count:
            coefficients[source_set] = theta
            continue
        coefficients[source_set] = tuple(
            Fraction(
                (channel + 1)
                * (len(source_set) + 1)
                * (sum(source_set) + 2),
                11,
            )
            for channel in range(target_dimension)
        )

    values: dict[SourceSet, Vector] = {}
    zero = tuple(Fraction(0) for _ in range(target_dimension))
    for active in contexts:
        value = zero
        for source_set, coefficient in coefficients.items():
            if source_set <= active:
                value = vector_add(value, coefficient)
        values[active] = value
    return values


def mobius_top(
    values: dict[SourceSet, Vector],
    source_count: int,
) -> Vector:
    target_dimension = len(next(iter(values.values())))
    result = tuple(Fraction(0) for _ in range(target_dimension))
    for active, value in values.items():
        sign = Fraction((-1) ** (source_count - len(active)))
        result = vector_add(result, vector_scale(sign, value))
    return result


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(entry * value for entry, value in zip(row, vector, strict=True))
        for row in matrix
    )


def matrix_rank(matrix: Matrix) -> int:
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
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    rows[row],
                    rows[pivot_row],
                    strict=True,
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def main() -> None:
    source_count = 4
    target_dimension = 3
    theta = (Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13))
    contexts = power_set(source_count)
    values = multiaffine_context_values(theta, source_count)
    recovered = mobius_top(values, source_count)
    assert recovered == theta
    assert len(contexts) == 16
    assert len(contexts) * target_dimension == 48

    full_packet: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    assert matrix_rank(full_packet) == target_dimension
    assert matrix_vector(full_packet, recovered) == theta

    rank_deficient_packet: Matrix = (
        (Fraction(1), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(1)),
    )
    assert matrix_rank(rank_deficient_packet) == 2
    theta_plus = (Fraction(1), Fraction(1), Fraction(3))
    theta_minus = (Fraction(3), Fraction(3), Fraction(1))
    assert theta_plus != theta_minus
    assert matrix_vector(rank_deficient_packet, theta_plus) == matrix_vector(
        rank_deficient_packet,
        theta_minus,
    )
    assert matrix_vector(rank_deficient_packet, theta_plus) == (
        Fraction(4),
        Fraction(4),
    )

    result = {
        "claim_id": "HC-DU-106",
        "status": "PASS",
        "controls": {
            "source_count": source_count,
            "source_configuration_count": len(contexts),
            "simultaneous_response_channels": target_dimension,
            "retained_scalar_value_count": len(contexts) * target_dimension,
            "exact_target_recovery": True,
            "full_packet_rank": matrix_rank(full_packet),
            "rank_deficient_packet_rank": matrix_rank(rank_deficient_packet),
            "same_packet_different_target": True,
        },
        "boundary": (
            "Regression only: no Lorentzian metric, nonlinear field, selected "
            "model class, physical source/readout, formed event, record, "
            "geometry, new physics, prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-106 controls: finite-dimensional nonlinear packet, "
        "configuration/data separation, and dimension-deficit witness"
    )


if __name__ == "__main__":
    main()
