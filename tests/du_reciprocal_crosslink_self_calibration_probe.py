#!/usr/bin/env python3
"""Proportional controls for HC-DU-108.

The scientific result is analytic. This probe preserves:

1. reciprocal two-way recovery of range and relative clock offset;
2. exact regular-tetrahedron distance-geometry rank;
3. composition with a held-out event packet up to time-origin gauge;
4. a same-transcript/different-clock-and-directed-delay witness;
5. a same-transcript/different-scale-and-hardware-latency witness.

Passing establishes no physical source formation, honest timestamping,
propagation reciprocity, clock-rate selection, hardware calibration, event
association, complete acquisition, Lorentzian geometry, new physics,
prediction, or evidence grade.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_reciprocal_crosslink_self_calibration_result.json"
)

Point = tuple[Fraction, Fraction, Fraction]

POSITIONS: tuple[Point, ...] = (
    (Fraction(1), Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(-1), Fraction(-1)),
    (Fraction(-1), Fraction(1), Fraction(-1)),
    (Fraction(-1), Fraction(-1), Fraction(1)),
)

BIASES: tuple[Fraction, ...] = (
    Fraction(1, 4),
    Fraction(-1, 2),
    Fraction(3, 4),
    Fraction(5, 4),
)


def squared_distance(left: Point, right: Point) -> Fraction:
    return sum(
        (a - b) ** 2 for a, b in zip(left, right, strict=True)
    )


def reciprocal_pseudorange(
    distance: float,
    sender_bias: Fraction,
    receiver_bias: Fraction,
) -> float:
    return distance + float(receiver_bias - sender_bias)


def matrix_rank(matrix: tuple[tuple[Fraction, ...], ...]) -> int:
    rows = [list(row) for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
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


def euclidean_norm(values: tuple[float, ...]) -> float:
    return math.sqrt(sum(value * value for value in values))


def event_arrivals(
    event_time: float,
    event_position: tuple[float, float, float],
    biases: tuple[Fraction, ...],
) -> tuple[float, ...]:
    return tuple(
        event_time
        + euclidean_norm(
            tuple(
                coordinate - float(site_coordinate)
                for coordinate, site_coordinate in zip(
                    event_position,
                    site,
                    strict=True,
                )
            )
        )
        + float(bias)
        for site, bias in zip(POSITIONS, biases, strict=True)
    )


def close(left: tuple[float, ...], right: tuple[float, ...]) -> bool:
    return all(
        math.isclose(a, b, rel_tol=0.0, abs_tol=1.0e-12)
        for a, b in zip(left, right, strict=True)
    )


def main() -> None:
    pair_squared_distances = {
        (left, right): squared_distance(POSITIONS[left], POSITIONS[right])
        for left, right in combinations(range(len(POSITIONS)), 2)
    }
    assert set(pair_squared_distances.values()) == {Fraction(8)}
    distance = math.sqrt(8.0)

    recovered_ranges: dict[tuple[int, int], float] = {}
    recovered_bias_differences: dict[tuple[int, int], float] = {}
    pseudoranges: dict[tuple[int, int], float] = {}
    for left, right in combinations(range(len(POSITIONS)), 2):
        forward = reciprocal_pseudorange(
            distance,
            BIASES[left],
            BIASES[right],
        )
        reverse = reciprocal_pseudorange(
            distance,
            BIASES[right],
            BIASES[left],
        )
        pseudoranges[(left, right)] = forward
        pseudoranges[(right, left)] = reverse
        recovered_ranges[(left, right)] = (forward + reverse) / 2.0
        recovered_bias_differences[(left, right)] = (
            forward - reverse
        ) / 2.0
        assert math.isclose(
            recovered_ranges[(left, right)],
            distance,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        assert math.isclose(
            recovered_bias_differences[(left, right)],
            float(BIASES[right] - BIASES[left]),
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )

    # Anchored distance Gram matrix:
    # G_ij=(d_0i^2+d_0j^2-d_ij^2)/2.
    gram = tuple(
        tuple(
            (
                squared_distance(POSITIONS[0], POSITIONS[left])
                + squared_distance(POSITIONS[0], POSITIONS[right])
                - squared_distance(POSITIONS[left], POSITIONS[right])
            )
            / 2
            for right in range(1, 4)
        )
        for left in range(1, 4)
    )
    assert gram == (
        (Fraction(8), Fraction(4), Fraction(4)),
        (Fraction(4), Fraction(8), Fraction(4)),
        (Fraction(4), Fraction(4), Fraction(8)),
    )
    assert matrix_rank(gram) == 3

    # Fix the time gauge by setting detector zero's recovered bias to zero.
    relative_biases = tuple(bias - BIASES[0] for bias in BIASES)
    event_time = 0.2
    event_position = (0.05, -0.03, 0.02)
    observed = event_arrivals(event_time, event_position, BIASES)
    corrected = tuple(
        value - float(relative_bias)
        for value, relative_bias in zip(
            observed,
            relative_biases,
            strict=True,
        )
    )
    gauge_shifted_ideal = event_arrivals(
        event_time + float(BIASES[0]),
        event_position,
        (Fraction(0),) * 4,
    )
    assert close(corrected, gauge_shifted_ideal)

    # Directed-delay gauge: p_ij=a_ij+b_j-b_i is invariant under
    # b_i'=b_i+c_i and a_ij'=a_ij+c_i-c_j.
    clock_changes = (0.02, -0.01, 0.015, -0.005)
    alternative_biases = tuple(
        float(bias) + change
        for bias, change in zip(BIASES, clock_changes, strict=True)
    )
    directed_delays = {
        (sender, receiver): distance
        + clock_changes[sender]
        - clock_changes[receiver]
        for sender in range(4)
        for receiver in range(4)
        if sender != receiver
    }
    alternative_pseudoranges = {
        (sender, receiver): directed_delays[(sender, receiver)]
        + alternative_biases[receiver]
        - alternative_biases[sender]
        for sender in range(4)
        for receiver in range(4)
        if sender != receiver
    }
    assert all(value > 0.0 for value in directed_delays.values())
    assert all(
        math.isclose(
            pseudoranges[key],
            alternative_pseudoranges[key],
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for key in pseudoranges
    )

    # Unknown per-link hardware latency confounds a scaled regular
    # tetrahedron with the original one.
    original_latency = 0.2
    range_change = 0.1
    alternative_distance = distance + range_change
    alternative_latency = original_latency - range_change
    assert alternative_latency > 0.0
    assert math.isclose(
        distance + original_latency,
        alternative_distance + alternative_latency,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )

    # One unknown common clock rate confounds spatial scale.
    clock_rate = 1.0
    alternative_clock_rate = 2.0
    scaled_distance = distance / 2.0
    assert math.isclose(
        clock_rate * distance,
        alternative_clock_rate * scaled_distance,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )

    result = {
        "claim_id": "HC-DU-108",
        "status": "PASS",
        "controls": {
            "node_count": 4,
            "directed_crosslink_count": 12,
            "undirected_range_count": 6,
            "regular_tetrahedron_squared_edge_length": "8",
            "anchored_gram_matrix": [
                [str(value) for value in row] for row in gram
            ],
            "anchored_gram_rank": matrix_rank(gram),
            "reciprocal_range_recovery": True,
            "relative_clock_offset_recovery": True,
            "event_packet_composes_up_to_common_time_origin": True,
            "directed_delay_clock_gauge_witness": True,
            "hardware_latency_range_confounding_witness": True,
            "clock_rate_spatial_scale_confounding_witness": True,
        },
        "boundary": (
            "Regression only: no physical source formation, honest "
            "timestamping, propagation reciprocity, clock-rate selection, "
            "hardware calibration, event association, complete acquisition, "
            "Lorentzian geometry, new physics, prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-108 controls: reciprocal crosslink self-calibration "
        "and delay/latency/scale counterexamples"
    )


if __name__ == "__main__":
    main()
