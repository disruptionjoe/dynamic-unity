#!/usr/bin/env python3
"""Proportional controls for HC-DU-109.

The scientific result is analytic. This probe preserves:

1. nullness and full rank of one fixed four-front Minkowski architecture;
2. exact recovery of several target events from continuously varied phases;
3. the exact spectrum and conditioning margin of the phase matrix;
4. the one-dimensional fibre left by three scalar phase channels;
5. the finite-codebook count boundary; and
6. a same-command/different-event source-latency witness.

Passing establishes no nonlinear PDE interaction, detectable outgoing
singularity, physical source selection, source timing honesty, finite exact
continuum control, curved-spacetime controllability, event association,
complete acquisition, regional geometry, new physics, prediction, or evidence
grade.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_fixed_null_front_interaction_formation_result.json"
)

Vector = tuple[Fraction, Fraction, Fraction, Fraction]
Matrix = tuple[Vector, Vector, Vector, Vector]

L: Matrix = (
    (Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(-1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(1)),
)

TARGETS: tuple[Vector, ...] = (
    (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    ),
    (
        Fraction(1, 3),
        Fraction(1, 7),
        Fraction(-2, 9),
        Fraction(4, 11),
    ),
    (
        Fraction(-3, 5),
        Fraction(2, 13),
        Fraction(5, 17),
        Fraction(-7, 19),
    ),
    (
        Fraction(2),
        Fraction(-1, 4),
        Fraction(3, 8),
        Fraction(5, 16),
    ),
)


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def recover_event(control: Vector) -> Vector:
    c1, c2, c3, c4 = control
    time = (c1 + c2) / 2
    space_x = (c1 - c2) / 2
    space_y = c3 - time
    space_z = c4 - time
    return (time, space_x, space_y, space_z)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(
        (a + b for a, b in zip(left, right, strict=True))
    )  # type: ignore[return-value]


def subtract(left: Vector, right: Vector) -> Vector:
    return tuple(
        (a - b for a, b in zip(left, right, strict=True))
    )  # type: ignore[return-value]


def euclidean_norm(vector: tuple[float, ...]) -> float:
    return math.sqrt(sum(value * value for value in vector))


def to_float(vector: Vector) -> tuple[float, ...]:
    return tuple(float(value) for value in vector)


def determinant_4(matrix: Matrix) -> Fraction:
    rows = [list(row) for row in matrix]
    determinant = Fraction(1)
    sign = 1
    for column in range(4):
        pivot = next(
            row
            for row in range(column, 4)
            if rows[row][column] != 0
        )
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            sign *= -1
        pivot_value = rows[column][column]
        determinant *= pivot_value
        rows[column] = [entry / pivot_value for entry in rows[column]]
        for row in range(column + 1, 4):
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    rows[row],
                    rows[column],
                    strict=True,
                )
            ]
    return determinant * sign


def main() -> None:
    minkowski_norms = tuple(
        -(row[0] ** 2) + sum(value**2 for value in row[1:])
        for row in L
    )
    assert minkowski_norms == (0, 0, 0, 0)
    assert determinant_4(L) == -2

    controls = tuple(matvec(L, target) for target in TARGETS)
    recovered = tuple(recover_event(control) for control in controls)
    assert recovered == TARGETS
    assert len(set(controls)) == len(TARGETS)

    # L^T L has eigenvalues 2, 1, and the roots of
    # lambda^2 - 5 lambda + 2. This makes the exact smallest squared singular
    # value (5-sqrt(17))/2.
    smallest_squared_singular = (5.0 - math.sqrt(17.0)) / 2.0
    largest_squared_singular = (5.0 + math.sqrt(17.0)) / 2.0
    squared_singular_values = (
        smallest_squared_singular,
        1.0,
        2.0,
        largest_squared_singular,
    )
    assert math.isclose(
        sum(squared_singular_values),
        8.0,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert math.isclose(
        math.prod(squared_singular_values),
        4.0,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    smallest_singular = math.sqrt(smallest_squared_singular)
    assert smallest_singular > 0.66

    phase_errors: tuple[Vector, ...] = (
        (
            Fraction(1, 100),
            Fraction(-1, 100),
            Fraction(1, 200),
            Fraction(-1, 200),
        ),
        (
            Fraction(1, 50),
            Fraction(1, 100),
            Fraction(-1, 125),
            Fraction(1, 250),
        ),
    )
    for phase_error in phase_errors:
        event_error = recover_event(phase_error)
        assert (
            euclidean_norm(to_float(event_error))
            <= euclidean_norm(to_float(phase_error)) / smallest_singular
            + 1.0e-12
        )

    # The first three rows annihilate the z direction. A fourth independent
    # scalar phase is necessary for local event uniqueness.
    three_channel_kernel: Vector = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    assert tuple(dot(row, three_channel_kernel) for row in L[:3]) == (
        0,
        0,
        0,
    )
    assert dot(L[3], three_channel_kernel) == 1

    # Because L is bijective, a finite exact control codebook reaches exactly
    # as many event points as it contains distinct codewords.
    finite_codebook = controls + (
        (
            Fraction(5, 2),
            Fraction(3, 2),
            Fraction(9, 4),
            Fraction(7, 4),
        ),
    )
    formed_events = tuple(recover_event(control) for control in finite_codebook)
    assert len(set(formed_events)) == len(set(finite_codebook)) == 5

    # Same retained command, two distinct physically realized events. Unknown
    # positive per-channel latencies absorb the difference.
    command: Vector = (
        Fraction(1),
        Fraction(1),
        Fraction(1),
        Fraction(1),
    )
    event_a: Vector = (
        Fraction(2),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )
    event_b: Vector = (
        Fraction(21, 10),
        Fraction(1, 10),
        Fraction(0),
        Fraction(0),
    )
    latency_a = subtract(matvec(L, event_a), command)
    latency_b = subtract(matvec(L, event_b), command)
    assert all(value > 0 for value in latency_a)
    assert all(value > 0 for value in latency_b)
    assert recover_event(add(command, latency_a)) == event_a
    assert recover_event(add(command, latency_b)) == event_b
    assert event_a != event_b

    result = {
        "claim_id": "HC-DU-109",
        "status": "PASS",
        "controls": {
            "fixed_null_front_count": 4,
            "all_covectors_null": True,
            "phase_matrix_determinant": "-2",
            "target_event_count_checked": len(TARGETS),
            "all_targets_exactly_recovered": True,
            "squared_singular_values": [
                "(5-sqrt(17))/2",
                "1",
                "2",
                "(5+sqrt(17))/2",
            ],
            "smallest_singular_value": smallest_singular,
            "phase_to_event_condition_number": (
                math.sqrt(largest_squared_singular) / smallest_singular
            ),
            "three_channel_kernel_dimension_at_least": 1,
            "finite_codebook_exact_event_count": len(set(formed_events)),
            "same_command_different_positive_latency_event_witness": True,
        },
        "boundary": (
            "Regression only: no nonlinear PDE interaction, detectable "
            "outgoing singularity, physical source selection, source timing "
            "honesty, finite exact continuum control, curved-spacetime "
            "controllability, event association, complete acquisition, "
            "regional geometry, new physics, prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-109 controls: fixed null-front event formation "
        "controllability and rank/precision/latency boundaries"
    )


if __name__ == "__main__":
    main()
