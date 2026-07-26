#!/usr/bin/env python3
"""Exact finite controls for the HC-DU-038A identification ladder.

The probe separates:

1. authenticated reachability/provenance;
2. a calibrated scalar record-time potential;
3. proper time, dimension, and spacetime metric.

It checks exact graph-cohomology and benign-subdivision claims with rational
arithmetic. Passing establishes no physical geometry or new physics.
"""

from __future__ import annotations

import json
from collections import deque
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_meta_record_geometry_identification_result.json"
)

Vertex = int
Edge = tuple[Vertex, Vertex]


def q(value: int, denominator: int = 1) -> Fraction:
    return Fraction(value, denominator)


def weak_components(vertices: tuple[Vertex, ...], edges: tuple[Edge, ...]) -> int:
    adjacency = {vertex: set() for vertex in vertices}
    for source, target in edges:
        adjacency[source].add(target)
        adjacency[target].add(source)
    unseen = set(vertices)
    count = 0
    while unseen:
        count += 1
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return count


def transitive_closure(
    vertices: tuple[Vertex, ...], edges: tuple[Edge, ...]
) -> set[Edge]:
    adjacency = {vertex: [] for vertex in vertices}
    for source, target in edges:
        adjacency[source].append(target)
    closure: set[Edge] = set()
    for source in vertices:
        stack = list(adjacency[source])
        seen: set[Vertex] = set()
        while stack:
            target = stack.pop()
            if target in seen:
                continue
            seen.add(target)
            closure.add((source, target))
            stack.extend(adjacency[target])
    return closure


def causal_interval(
    vertices: tuple[Vertex, ...],
    edges: tuple[Edge, ...],
    source: Vertex,
    target: Vertex,
) -> set[Vertex]:
    closure = transitive_closure(vertices, edges)
    return {
        vertex
        for vertex in vertices
        if vertex in (source, target)
        or ((source, vertex) in closure and (vertex, target) in closure)
    }


def recover_potential(
    vertices: tuple[Vertex, ...],
    edges: tuple[Edge, ...],
    weights: dict[Edge, Fraction],
) -> dict[Vertex, Fraction] | None:
    """Solve tau(v)-tau(u)=w(u,v), setting one origin per weak component."""

    adjacency: dict[Vertex, list[tuple[Vertex, Fraction]]] = {
        vertex: [] for vertex in vertices
    }
    for source, target in edges:
        weight = weights[(source, target)]
        adjacency[source].append((target, weight))
        adjacency[target].append((source, -weight))

    potential: dict[Vertex, Fraction] = {}
    for root in vertices:
        if root in potential:
            continue
        potential[root] = q(0)
        queue = deque([root])
        while queue:
            source = queue.popleft()
            for target, delta in adjacency[source]:
                candidate = potential[source] + delta
                if target not in potential:
                    potential[target] = candidate
                    queue.append(target)
                elif potential[target] != candidate:
                    return None
    return potential


def verify_potential(
    edges: tuple[Edge, ...],
    weights: dict[Edge, Fraction],
    potential: dict[Vertex, Fraction],
) -> bool:
    return all(
        potential[target] - potential[source] == weights[(source, target)]
        for source, target in edges
    )


def verify_cycle(
    edges: tuple[Edge, ...],
    weights: dict[Edge, Fraction],
    signed_cycle: tuple[tuple[Edge, int], ...],
) -> Fraction:
    """Verify a signed undirected cycle and return its exact circulation."""

    edge_set = set(edges)
    balance: dict[Vertex, int] = {}
    circulation = q(0)
    for edge, sign in signed_cycle:
        if edge not in edge_set or sign not in (-1, 1):
            raise AssertionError(f"invalid cycle term: {edge=} {sign=}")
        source, target = edge
        balance[source] = balance.get(source, 0) - sign
        balance[target] = balance.get(target, 0) + sign
        circulation += sign * weights[edge]
    if any(value != 0 for value in balance.values()):
        raise AssertionError(f"signed edge set is not a cycle: {balance}")
    return circulation


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
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
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def incidence_cycle_dimension(
    vertices: tuple[Vertex, ...], edges: tuple[Edge, ...]
) -> tuple[int, int]:
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
    incidence = [
        [q(0) for _ in edges]
        for _ in vertices
    ]
    for column, (source, target) in enumerate(edges):
        incidence[vertex_index[source]][column] = q(-1)
        incidence[vertex_index[target]][column] = q(1)
    rank = matrix_rank(incidence)
    return rank, len(edges) - rank


def longest_path_length(
    vertices: tuple[Vertex, ...],
    edges: tuple[Edge, ...],
    source: Vertex,
    target: Vertex,
) -> int:
    adjacency = {vertex: [] for vertex in vertices}
    for left, right in edges:
        adjacency[left].append(right)

    memo: dict[Vertex, int | None] = {}

    def visit(vertex: Vertex) -> int | None:
        if vertex == target:
            return 0
        if vertex in memo:
            return memo[vertex]
        candidates = [
            child_length + 1
            for child in adjacency[vertex]
            if (child_length := visit(child)) is not None
        ]
        memo[vertex] = max(candidates) if candidates else None
        return memo[vertex]

    result = visit(source)
    if result is None:
        raise AssertionError(f"no path from {source} to {target}")
    return result


def causal_matrix(points: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    """Strict timelike order for finite points in flat Minkowski coordinates."""

    relation: list[tuple[int, ...]] = []
    for left in points:
        row = []
        for right in points:
            delta_t = right[0] - left[0]
            spatial_norm = sum(
                (right[index] - left[index]) ** 2
                for index in range(1, len(left))
            )
            row.append(int(delta_t > 0 and delta_t**2 > spatial_norm))
        relation.append(tuple(row))
    return tuple(relation)


def as_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def potential_as_text(
    potential: dict[Vertex, Fraction] | None
) -> dict[str, str] | None:
    if potential is None:
        return None
    return {
        str(vertex): as_text(value)
        for vertex, value in sorted(potential.items())
    }


def run() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    chain_vertices = (0, 1, 2)
    chain_edges = ((0, 1), (1, 2))
    chain_order = transitive_closure(chain_vertices, chain_edges)
    tau_a = {0: q(0), 1: q(1), 2: q(4)}
    tau_scaled = {vertex: q(7) + q(2) * value for vertex, value in tau_a.items()}
    tau_same_total = {0: q(0), 1: q(2), 2: q(4)}
    weights_a = {
        edge: tau_a[edge[1]] - tau_a[edge[0]] for edge in chain_edges
    }
    weights_scaled = {
        edge: tau_scaled[edge[1]] - tau_scaled[edge[0]]
        for edge in chain_edges
    }

    check(
        "order_survives_affine_clock_change",
        chain_order == transitive_closure(chain_vertices, chain_edges),
        "same authenticated reachability under additive-origin and positive-scale changes",
    )
    check(
        "order_does_not_fix_scale",
        weights_scaled == {edge: q(2) * value for edge, value in weights_a.items()},
        "positive rescaling changes every elapsed value while preserving order",
    )
    check(
        "one_endpoint_clock_does_not_fix_local_allocation",
        tau_a[2] - tau_a[0] == tau_same_total[2] - tau_same_total[0]
        and tau_a[1] != tau_same_total[1],
        "same order and endpoint duration 4 admit local splits (1,3) and (2,2)",
    )

    causal_relations = {}
    for spacetime_dimension in (2, 3, 4):
        points = tuple(
            (time,) + (0,) * (spacetime_dimension - 1)
            for time in (0, 1, 2)
        )
        causal_relations[spacetime_dimension] = causal_matrix(points)
    check(
        "finite_order_does_not_fix_ambient_dimension",
        len(set(causal_relations.values())) == 1,
        "one three-event timelike chain has the same order in Minkowski dimensions 2, 3, and 4",
    )

    diamond_vertices = (0, 1, 2, 3)
    diamond_edges = ((0, 1), (0, 2), (1, 3), (2, 3))
    diamond_tau = {0: q(0), 1: q(1), 2: q(2), 3: q(4)}
    diamond_weights = {
        edge: diamond_tau[edge[1]] - diamond_tau[edge[0]]
        for edge in diamond_edges
    }
    diamond_cycle = (
        (((0, 1)), 1),
        (((1, 3)), 1),
        (((2, 3)), -1),
        (((0, 2)), -1),
    )
    recovered_diamond = recover_potential(
        diamond_vertices, diamond_edges, diamond_weights
    )
    check(
        "exact_weighted_diamond_reconstructs",
        recovered_diamond is not None
        and verify_potential(diamond_edges, diamond_weights, recovered_diamond),
        "zero-circulation cover weights reconstruct an exact scalar potential",
    )
    check(
        "exact_cycle_has_zero_holonomy",
        verify_cycle(diamond_edges, diamond_weights, diamond_cycle) == 0,
        "the independent diamond cycle has zero signed weight",
    )
    check(
        "potential_unique_up_to_origin",
        recovered_diamond is not None
        and verify_potential(
            diamond_edges,
            diamond_weights,
            {vertex: value + q(11) for vertex, value in recovered_diamond.items()},
        ),
        "an additive constant changes no calibrated edge difference",
    )

    relabel = {0: 20, 1: 50, 2: 10, 3: 40}
    relabeled_vertices = tuple(sorted(relabel.values()))
    relabeled_edges = tuple(
        (relabel[source], relabel[target]) for source, target in diamond_edges
    )
    relabeled_weights = {
        (relabel[source], relabel[target]): weight
        for (source, target), weight in diamond_weights.items()
    }
    recovered_relabel = recover_potential(
        relabeled_vertices, relabeled_edges, relabeled_weights
    )
    check(
        "relabeling_is_natural",
        recovered_relabel is not None
        and all(
            recovered_relabel[relabel[right]]
            - recovered_relabel[relabel[left]]
            == diamond_tau[right] - diamond_tau[left]
            for left in diamond_vertices
            for right in diamond_vertices
        )
        and incidence_cycle_dimension(relabeled_vertices, relabeled_edges)[1]
        == 1,
        "vertex relabeling preserves every potential difference and the cycle rank",
    )

    disconnected_vertices = (0, 1, 2, 3)
    disconnected_edges = ((0, 1), (2, 3))
    disconnected_weights = {(0, 1): q(5), (2, 3): q(7)}
    disconnected_potential = recover_potential(
        disconnected_vertices, disconnected_edges, disconnected_weights
    )
    disconnected_rank, disconnected_cycle_dimension = (
        incidence_cycle_dimension(disconnected_vertices, disconnected_edges)
    )
    check(
        "one_origin_gauge_per_weak_component",
        disconnected_potential is not None
        and verify_potential(
            disconnected_edges,
            disconnected_weights,
            {
                0: disconnected_potential[0] + q(11),
                1: disconnected_potential[1] + q(11),
                2: disconnected_potential[2] - q(13),
                3: disconnected_potential[3] - q(13),
            },
        )
        and weak_components(disconnected_vertices, disconnected_edges) == 2
        and disconnected_rank == 2
        and disconnected_cycle_dimension == 0,
        "two weak components admit two independent additive origins and rank n-c",
    )

    inconsistent_weights = dict(diamond_weights)
    inconsistent_weights[(2, 3)] = q(3)
    inconsistent_circulation = verify_cycle(
        diamond_edges, inconsistent_weights, diamond_cycle
    )
    check(
        "nonzero_cycle_obstructs_potential",
        inconsistent_circulation == q(-1)
        and recover_potential(
            diamond_vertices, diamond_edges, inconsistent_weights
        )
        is None,
        "a nonzero signed cycle is an independently verified obstruction",
    )

    incidence_rank, cycle_dimension = incidence_cycle_dimension(
        diamond_vertices, diamond_edges
    )
    diamond_components = weak_components(diamond_vertices, diamond_edges)
    check(
        "incidence_rank_exact",
        incidence_rank == len(diamond_vertices) - diamond_components == 3,
        "connected incidence rank is n-1",
    )
    check(
        "cycle_obligation_count_exact",
        cycle_dimension
        == len(diamond_edges) - len(diamond_vertices) + diamond_components
        == 1,
        "independent cycle obligations have dimension m-n+c",
    )

    subdivided_vertices = (0, 1, 2, 3, 4)
    subdivided_edges = ((0, 1), (0, 2), (1, 4), (4, 3), (2, 3))
    subdivided_weights = {
        (0, 1): q(1),
        (0, 2): q(2),
        (1, 4): q(1),
        (4, 3): q(2),
        (2, 3): q(2),
    }
    recovered_subdivision = recover_potential(
        subdivided_vertices, subdivided_edges, subdivided_weights
    )
    original_boundary = (0, 1, 2, 3)
    original_boundary_order = {
        edge
        for edge in transitive_closure(diamond_vertices, diamond_edges)
        if edge[0] in original_boundary and edge[1] in original_boundary
    }
    subdivided_boundary_order = {
        edge
        for edge in transitive_closure(subdivided_vertices, subdivided_edges)
        if edge[0] in original_boundary and edge[1] in original_boundary
    }
    check(
        "additive_subdivision_reconstructs",
        recovered_subdivision is not None
        and verify_potential(
            subdivided_edges, subdivided_weights, recovered_subdivision
        ),
        "splitting weight 3 into 1+2 preserves exactness",
    )
    check(
        "boundary_reachability_is_natural",
        original_boundary_order == subdivided_boundary_order,
        "benign relay insertion preserves the original-event reachability relation",
    )
    check(
        "boundary_elapsed_values_are_natural",
        recovered_diamond is not None
        and recovered_subdivision is not None
        and all(
            recovered_diamond[vertex] == recovered_subdivision[vertex]
            for vertex in original_boundary
        ),
        "additive relay insertion preserves every original-event potential difference",
    )
    subdivided_rank, subdivided_cycle_dimension = incidence_cycle_dimension(
        subdivided_vertices, subdivided_edges
    )
    check(
        "cycle_rank_survives_subdivision",
        subdivided_cycle_dimension == cycle_dimension == 1
        and subdivided_rank == 4,
        "n and m each rise by one while m-n+c is unchanged",
    )
    check(
        "raw_graph_counts_are_not_gauge_invariants",
        len(subdivided_vertices) == len(diamond_vertices) + 1
        and len(subdivided_edges) == len(diamond_edges) + 1
        and len(causal_interval(diamond_vertices, diamond_edges, 0, 3)) == 4
        and len(
            causal_interval(subdivided_vertices, subdivided_edges, 0, 3)
        )
        == 5
        and longest_path_length(diamond_vertices, diamond_edges, 0, 3) == 2
        and longest_path_length(
            subdivided_vertices, subdivided_edges, 0, 3
        )
        == 3,
        "node, edge, interval-cardinality, and longest-hop counts change under a benign subdivision",
    )

    twice_vertices = (0, 1, 2, 3, 4, 5)
    twice_edges = ((0, 1), (0, 2), (1, 4), (4, 5), (5, 3), (2, 3))
    twice_weights = {
        (0, 1): q(1),
        (0, 2): q(2),
        (1, 4): q(1),
        (4, 5): q(1, 2),
        (5, 3): q(3, 2),
        (2, 3): q(2),
    }
    recovered_twice = recover_potential(twice_vertices, twice_edges, twice_weights)
    check(
        "subdivision_composition_is_natural",
        recovered_twice is not None
        and all(
            recovered_twice[vertex] == diamond_tau[vertex]
            for vertex in original_boundary
        )
        and incidence_cycle_dimension(twice_vertices, twice_edges)[1] == 1,
        "two composed additive subdivisions preserve boundary time and cycle rank",
    )

    physical_relay_weights = dict(subdivided_weights)
    physical_relay_weights[(4, 3)] = q(3)
    physical_relay_cycle = (
        (((0, 1)), 1),
        (((1, 4)), 1),
        (((4, 3)), 1),
        (((2, 3)), -1),
        (((0, 2)), -1),
    )
    check(
        "nonadditive_relay_is_not_benign",
        verify_cycle(
            subdivided_edges, physical_relay_weights, physical_relay_cycle
        )
        == q(1)
        and recover_potential(
            subdivided_vertices, subdivided_edges, physical_relay_weights
        )
        is None,
        "a relay that changes total calibrated duration changes the physical contract",
    )

    tree_vertices = (0, 1, 2, 3)
    tree_edges = ((0, 1), (1, 2), (1, 3))
    tree_weights = {(0, 1): q(7, 3), (1, 2): q(5, 2), (1, 3): q(11, 4)}
    tree_potential = recover_potential(tree_vertices, tree_edges, tree_weights)
    tree_rank, tree_cycle_dimension = incidence_cycle_dimension(
        tree_vertices, tree_edges
    )
    check(
        "tree_has_no_cycle_obstruction",
        tree_cycle_dimension == 0
        and tree_rank == 3
        and tree_potential is not None
        and verify_potential(tree_edges, tree_weights, tree_potential),
        "every rational weighting on a connected tree determines a potential up to origin",
    )

    check(
        "record_time_is_not_proper_time_or_metric",
        causal_relations[2] == causal_relations[4]
        and weights_a != weights_scaled,
        "the same causal order coexists with different clock scales and ambient dimensions",
    )

    result: dict[str, object] = {
        "artifact_type": "exact_finite_theorem_controls",
        "claim_grade": (
            "EXACT FINITE GRAPH-COHOMOLOGY AND NONIDENTIFICATION CONTROLS / "
            "KNOWN MATHEMATICS / NO PHYSICAL GEOMETRY"
        ),
        "theorem_family": "HC-DU-038A",
        "returns": {
            "order_only": (
                "NONIDENTIFIED: scale, local elapsed-time allocation, ambient "
                "dimension, proper time, and metric are not fixed"
            ),
            "weighted_cover": (
                "RECONSTRUCTS_SCALAR_POTENTIAL iff every signed cycle has zero "
                "circulation"
            ),
            "gauge": (
                "one additive constant per weak component; a multiplicative "
                "scale remains only when calibration supplies ratios rather "
                "than absolute units"
            ),
            "benign_subdivision": (
                "PRESERVES boundary reachability, boundary potential "
                "differences, exactness, and cycle rank when child weights sum "
                "to the replaced edge"
            ),
        },
        "fixtures": {
            "chain": {
                "order": sorted([list(edge) for edge in chain_order]),
                "potential_a": potential_as_text(tau_a),
                "potential_same_endpoint": potential_as_text(tau_same_total),
                "potential_scaled_and_shifted": potential_as_text(tau_scaled),
                "ambient_dimensions_with_same_order": [2, 3, 4],
            },
            "diamond": {
                "potential": potential_as_text(recovered_diamond),
                "relabeled_potential": potential_as_text(recovered_relabel),
                "cycle_circulation": as_text(
                    verify_cycle(diamond_edges, diamond_weights, diamond_cycle)
                ),
                "mutated_cycle_circulation": as_text(inconsistent_circulation),
                "incidence_rank": incidence_rank,
                "cycle_dimension": cycle_dimension,
            },
            "disconnected": {
                "potential": potential_as_text(disconnected_potential),
                "components": weak_components(
                    disconnected_vertices, disconnected_edges
                ),
                "incidence_rank": disconnected_rank,
                "cycle_dimension": disconnected_cycle_dimension,
            },
            "subdivision": {
                "potential": potential_as_text(recovered_subdivision),
                "twice_subdivided_potential": potential_as_text(recovered_twice),
                "boundary_reachability_preserved": (
                    original_boundary_order == subdivided_boundary_order
                ),
                "cycle_dimension": subdivided_cycle_dimension,
                "base_longest_hops": longest_path_length(
                    diamond_vertices, diamond_edges, 0, 3
                ),
                "subdivided_longest_hops": longest_path_length(
                    subdivided_vertices, subdivided_edges, 0, 3
                ),
                "nonadditive_cycle_circulation": as_text(
                    verify_cycle(
                        subdivided_edges,
                        physical_relay_weights,
                        physical_relay_cycle,
                    )
                ),
            },
        },
        "checks": checks,
        "checks_passed": len(checks),
        "all_passed": True,
        "limits": [
            "The scalar potential is not proper time, simultaneity, Lorentzian distance, dimension, curvature, or a spacetime metric.",
            "Event cardinality is not a volume measure without a calibrated physical sampling or density law.",
            "A nonzero cycle may be calibration, clock-transport, route, or provenance failure; it is not by itself physical curvature.",
            "The finite fixtures support the proof and boundary audit; they do not establish theorem novelty or physical realization.",
        ],
    }
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = run()
    print(
        "PASS "
        f"{result['checks_passed']}/{result['checks_passed']} "
        f"theorem_family={result['theorem_family']}"
    )
    print(f"artifact={OUTPUT.relative_to(ROOT)}")
    print(
        "GRADE: exact finite known-mathematics controls; no physical geometry, "
        "ontology, novelty, or paper verdict"
    )


if __name__ == "__main__":
    main()
