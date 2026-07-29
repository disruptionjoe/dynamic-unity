#!/usr/bin/env python3
"""Proportional regression controls for HC-DU-104.

The scientific result is analytic. This probe only preserves:

1. the first positive zero of the massive 3+1 Klein--Gordon interior
   point-response tail;
2. a zero-free short-range interval before that root;
3. failure of a short-range response rule on a long direct comparison; and
4. recovery of that comparison after *formed* short-range relay events are
   admitted.

Passing establishes no physical point detector, selected field mass,
localized instrument, continuum response margin, formed relay mechanism,
complete acquisition, conformal reconstruction, new physics, prediction, or
evidence grade.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_massive_tail_formed_relay_result.json"
)

Node = str
Edge = tuple[Node, Node]


def bessel_j1(value: float) -> float:
    """Evaluate J_1 by its convergent power series for the bounded controls."""

    term = value / 2.0
    total = term
    for index in range(1, 200):
        term *= -(value * value / 4.0) / (index * (index + 1))
        updated = total + term
        if abs(term) <= 1e-16 * max(1.0, abs(updated)):
            return updated
        total = updated
    raise AssertionError("J1 series did not converge in the control interval")


def bisect_root(left: float, right: float, iterations: int = 100) -> float:
    left_value = bessel_j1(left)
    right_value = bessel_j1(right)
    assert left_value * right_value < 0.0
    for _ in range(iterations):
        midpoint = (left + right) / 2.0
        midpoint_value = bessel_j1(midpoint)
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value
    return (left + right) / 2.0


def massive_tail(mass: float, proper_time: float) -> float:
    """Absolute normalization of the timelike interior point-response tail."""

    assert mass > 0.0
    assert proper_time > 0.0
    return mass * bessel_j1(mass * proper_time) / (
        4.0 * math.pi * proper_time
    )


def transitive_closure(nodes: Iterable[Node], edges: set[Edge]) -> set[Edge]:
    node_tuple = tuple(nodes)
    closure = set(edges)
    changed = True
    while changed:
        changed = False
        for left in node_tuple:
            for middle in node_tuple:
                if (left, middle) not in closure:
                    continue
                for right in node_tuple:
                    if (middle, right) in closure and (left, right) not in closure:
                        closure.add((left, right))
                        changed = True
    return closure


def local_edges(
    positions: dict[Node, float],
    formed_nodes: set[Node],
    maximum_step: float,
) -> set[Edge]:
    return {
        (left, right)
        for left, left_position in positions.items()
        for right, right_position in positions.items()
        if left in formed_nodes
        and right in formed_nodes
        and 0.0 < right_position - left_position <= maximum_step
    }


def main() -> None:
    first_root = bisect_root(3.0, 4.0)
    assert abs(first_root - 3.8317059702075125) < 1e-12
    assert abs(bessel_j1(first_root)) < 1e-14
    assert abs(massive_tail(1.0, first_root)) < 1e-14

    # J1 is positive before its first positive root. The grid is only a
    # regression witness for the analytic zero-free interval used in the
    # evidence note.
    short_range_samples = [
        massive_tail(1.0, 0.1 + 2.9 * index / 100)
        for index in range(101)
    ]
    sampled_short_range_margin = min(short_range_samples)
    assert sampled_short_range_margin > 0.0

    positions = {
        "a": 0.0,
        "r1": 2.0,
        "r2": 4.0,
        "r3": 6.0,
        "b": 8.0,
    }
    original_nodes = {"a", "b"}
    original_order = {("a", "b")}
    maximum_step = 2.0

    # Merely imagining subdivision points does not add response edges.
    sparse_edges = local_edges(positions, original_nodes, maximum_step)
    assert sparse_edges == set()
    assert (
        transitive_closure(original_nodes, sparse_edges) & original_order
        != original_order
    )

    # Once the relays are admitted as formed events, the same local response
    # rule generates a path whose closure recovers the original comparison.
    formed_nodes = set(positions)
    formed_edges = local_edges(positions, formed_nodes, maximum_step)
    formed_closure = transitive_closure(formed_nodes, formed_edges)
    assert ("a", "b") in formed_closure
    assert formed_closure & original_order == original_order

    result = {
        "claim_id": "HC-DU-104",
        "status": "PASS",
        "controls": {
            "first_positive_j1_root": first_root,
            "point_tail_zero_at_first_root": abs(
                massive_tail(1.0, first_root)
            ),
            "sampled_short_range_margin": sampled_short_range_margin,
            "long_direct_edge_without_formed_relays": False,
            "long_order_recovered_with_formed_relays": True,
            "formed_relay_count": 3,
            "maximum_local_step": maximum_step,
        },
        "boundary": (
            "Regression only: no selected field, point detector, uniform "
            "continuum margin, physical relay formation, acquisition, "
            "geometry reconstruction, new physics, or prediction."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-104 controls: Bessel blind shell, short-range interval, "
        "and formed-relay closure"
    )


if __name__ == "__main__":
    main()
