#!/usr/bin/env python3
"""Exact regression controls for HC-DU-103.

This probe preserves elementary controls for:

1. finite causal-order reconstruction from a sound, cover-saturating response
   graph;
2. exact failure when one cover relation is not detected;
3. robust threshold recovery under a declared positive response margin;
4. the sharp-Huygens failure of direct timelike response in 3+1-dimensional
   massless Minkowski propagation;
5. repair by a sampled null intermediary, which is unavailable in the
   corresponding two-event packet; and
6. equal skew-spectrum data with different labeled response incidence.

Passing establishes no selected spacetime localization, local QFT
realization, formed instrument, causal saturation of a physical carrier
family, continuum conformal reconstruction, full metric, novel physics,
prediction, or evidence grade.
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
    / "du_operational_localization_causal_saturation_result.json"
)

Node = str
Edge = tuple[Node, Node]
Event = tuple[Fraction, Fraction, Fraction, Fraction]


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


def cover_relations(nodes: Iterable[Node], order: set[Edge]) -> set[Edge]:
    node_tuple = tuple(nodes)
    return {
        (left, right)
        for left, right in order
        if not any(
            (left, middle) in order and (middle, right) in order
            for middle in node_tuple
        )
    }


def interval_squared(source: Event, readout: Event) -> Fraction:
    delta = tuple(
        target - origin
        for origin, target in zip(source, readout, strict=True)
    )
    return delta[0] ** 2 - sum(component**2 for component in delta[1:])


def causally_precedes(source: Event, readout: Event) -> bool:
    return readout[0] > source[0] and interval_squared(source, readout) >= 0


def sharp_huygens_direct_response(source: Event, readout: Event) -> bool:
    """Point-support control for the 3+1 massless retarded propagator."""

    return readout[0] > source[0] and interval_squared(source, readout) == 0


def skew_incidence(vector: tuple[int, int, int]) -> tuple[tuple[int, ...], ...]:
    """Return the 3x3 cross-product matrix associated with ``vector``."""

    first, second, third = vector
    return (
        (0, -third, second),
        (third, 0, -first),
        (-second, first, 0),
    )


def nonzero_upper_incidence(matrix: tuple[tuple[int, ...], ...]) -> set[tuple[int, int]]:
    return {
        (row, column)
        for row in range(len(matrix))
        for column in range(row + 1, len(matrix))
        if matrix[row][column] != 0
    }


def main() -> None:
    nodes = ("a", "b", "c", "d")
    true_order: set[Edge] = {
        ("a", "b"),
        ("a", "c"),
        ("a", "d"),
        ("b", "d"),
        ("c", "d"),
    }
    covers = cover_relations(nodes, true_order)
    assert covers == {
        ("a", "b"),
        ("a", "c"),
        ("b", "d"),
        ("c", "d"),
    }

    # Soundness plus every cover edge is sufficient for exact finite recovery.
    detected_saturating = set(covers)
    recovered_order = transitive_closure(nodes, detected_saturating)
    assert detected_saturating <= true_order
    assert recovered_order == true_order

    # The missing cover cannot be manufactured by transitive closure.
    detected_incomplete = detected_saturating - {("c", "d")}
    incomplete_closure = transitive_closure(nodes, detected_incomplete)
    assert ("c", "d") not in incomplete_closure
    assert incomplete_closure != true_order

    # A two-sided zero/signal gap with error less than gamma/2 gives exact
    # threshold recovery. Fractions keep the regression exact.
    gamma = Fraction(2, 5)
    epsilon = Fraction(3, 20)
    threshold = gamma / 2
    assert epsilon < threshold
    all_pairs = {
        (left, right)
        for left in nodes
        for right in nodes
        if left != right
    }
    true_responses = {
        pair: (gamma if pair in detected_saturating else Fraction(0))
        for pair in all_pairs
    }
    estimated_responses = {
        pair: (
            value - epsilon
            if pair in detected_saturating
            else epsilon
        )
        for pair, value in true_responses.items()
    }
    thresholded = {
        pair
        for pair, value in estimated_responses.items()
        if abs(value) > threshold
    }
    assert thresholded == detected_saturating
    assert transitive_closure(nodes, thresholded) == true_order

    # Sharp Huygens control. The two endpoints are strictly timelike but the
    # massless 3+1 direct response is supported only on the null cone.
    event_a: Event = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )
    event_n: Event = (
        Fraction(1),
        Fraction(1),
        Fraction(0),
        Fraction(0),
    )
    event_b: Event = (
        Fraction(2),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )
    assert interval_squared(event_a, event_b) == 4
    assert causally_precedes(event_a, event_b)
    assert not sharp_huygens_direct_response(event_a, event_b)
    assert sharp_huygens_direct_response(event_a, event_n)
    assert sharp_huygens_direct_response(event_n, event_b)

    sparse_nodes = ("a", "b")
    sparse_edges: set[Edge] = set()
    sparse_true_order = {("a", "b")}
    assert transitive_closure(sparse_nodes, sparse_edges) != sparse_true_order

    dense_nodes = ("a", "n", "b")
    dense_edges = {("a", "n"), ("n", "b")}
    dense_true_order = {("a", "n"), ("n", "b"), ("a", "b")}
    assert transitive_closure(dense_nodes, dense_edges) == dense_true_order

    # For a 3x3 real skew matrix K(v), the characteristic polynomial is
    # lambda * (lambda^2 + ||v||^2). Equal vector norm therefore gives the
    # same spectrum. These two exact integer controls have different labeled
    # nonzero incidence, so spectrum alone cannot recover event relations.
    spectral_vector_a = (5, 0, 0)
    spectral_vector_b = (3, 4, 0)
    norm_squared_a = sum(value * value for value in spectral_vector_a)
    norm_squared_b = sum(value * value for value in spectral_vector_b)
    assert norm_squared_a == norm_squared_b == 25
    spectral_matrix_a = skew_incidence(spectral_vector_a)
    spectral_matrix_b = skew_incidence(spectral_vector_b)
    incidence_a = nonzero_upper_incidence(spectral_matrix_a)
    incidence_b = nonzero_upper_incidence(spectral_matrix_b)
    assert incidence_a != incidence_b

    result = {
        "probe": "du_operational_localization_causal_saturation_probe",
        "status": "PASS",
        "claim_id": "HC-DU-103",
        "checks": {
            "finite_poset": {
                "nodes": len(nodes),
                "true_order_edges": len(true_order),
                "cover_edges": len(covers),
                "sound_cover_saturation_recovers_order": True,
                "one_missing_cover_breaks_reconstruction": True,
            },
            "uniform_margin": {
                "gamma": str(gamma),
                "epsilon": str(epsilon),
                "threshold": str(threshold),
                "exact_recovery": True,
            },
            "sharp_huygens": {
                "endpoint_interval_squared": str(
                    interval_squared(event_a, event_b)
                ),
                "endpoint_causally_ordered": True,
                "endpoint_direct_response": False,
                "sampled_null_intermediary_repairs_transitive_order": True,
                "two_event_packet_does_not": True,
            },
            "spectrum_loses_labeled_incidence": {
                "common_characteristic_polynomial": "lambda*(lambda^2+25)",
                "incidence_a": sorted(list(pair) for pair in incidence_a),
                "incidence_b": sorted(list(pair) for pair in incidence_b),
                "different": True,
            },
        },
        "scope_warning": (
            "Exact finite order, margin, point-support Huygens, and spectral "
            "controls only. No selected localization, local QFT realization, "
            "formed instrument, physical causal saturation, continuum "
            "conformal geometry, full metric, novel physics, or prediction "
            "is established."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS: HC-DU-103 finite saturation theorem, missing-cover kill, "
        "margin recovery, Huygens counterexample, and spectral-loss control"
    )


if __name__ == "__main__":
    main()
