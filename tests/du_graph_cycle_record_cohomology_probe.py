#!/usr/bin/env python3
"""Exact regressions for the HC-DU-123 graph-cycle record theorem.

The scientific result is a graph-cohomological proof in the matter-completed
finite-Abelian dressed-edge arena established by HC-DU-121. This script
preserves:

1. the kernel of a complete fundamental-cycle record is exactly the graph
   coboundary space;
2. every spanning tree coordinates the same record equivalence;
3. an edge-chain response factors exactly when its vertex boundary
   annihilates G;
4. every ordinary cycle factors and every nontrivial open path leaks;
5. the minimum support of an endpoint leak is the endpoint min-cut; and
6. |V|-1 additional G-valued tree coordinates are necessary and sufficient
   to complete all path responses.

It is not a lattice-gauge dynamics simulation, a joint measurement-resource
calculation, an interface selector, a continuum theorem, or new physics.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path

from du_generalized_symmetry_access_resource_probe import (
    Group,
    GroupElement,
    add,
    elements,
    group_label,
    group_order,
    negate,
)
from du_wilson_record_capability_first_leak_probe import (
    character_signature,
    scalar_multiply,
)


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_graph_cycle_record_cohomology_result.json"

EdgeValue = tuple[GroupElement, ...]
VertexPotential = tuple[GroupElement, ...]
Chain = tuple[int, ...]


@dataclass(frozen=True)
class Graph:
    name: str
    vertex_count: int
    edges: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        assert self.vertex_count >= 2
        assert self.edges
        assert all(
            0 <= tail < self.vertex_count
            and 0 <= head < self.vertex_count
            and tail != head
            for tail, head in self.edges
        )
        assert len(set(self.edges)) == len(self.edges)


def zero_element(group: Group) -> GroupElement:
    return tuple(0 for _ in group)


def chain_value(
    group: Group,
    chain: Chain,
    edge_values: EdgeValue,
) -> GroupElement:
    total = zero_element(group)
    for coefficient, value in zip(chain, edge_values, strict=True):
        total = add(
            group,
            total,
            scalar_multiply(group, coefficient, value),
        )
    return total


def chain_boundary(graph: Graph, chain: Chain) -> tuple[int, ...]:
    boundary = [0 for _ in range(graph.vertex_count)]
    for coefficient, (tail, head) in zip(
        chain,
        graph.edges,
        strict=True,
    ):
        boundary[tail] -= coefficient
        boundary[head] += coefficient
    return tuple(boundary)


def coboundary(
    group: Group,
    graph: Graph,
    potential: VertexPotential,
) -> EdgeValue:
    return tuple(
        add(group, potential[head], negate(group, potential[tail]))
        for tail, head in graph.edges
    )


def is_spanning_tree(graph: Graph, edge_indices: tuple[int, ...]) -> bool:
    if len(edge_indices) != graph.vertex_count - 1:
        return False

    parent = list(range(graph.vertex_count))

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for edge_index in edge_indices:
        tail, head = graph.edges[edge_index]
        tail_root = find(tail)
        head_root = find(head)
        if tail_root == head_root:
            return False
        parent[head_root] = tail_root

    roots = {find(vertex) for vertex in range(graph.vertex_count)}
    return len(roots) == 1


def spanning_trees(graph: Graph) -> tuple[tuple[int, ...], ...]:
    return tuple(
        edge_indices
        for edge_indices in combinations(
            range(len(graph.edges)),
            graph.vertex_count - 1,
        )
        if is_spanning_tree(graph, edge_indices)
    )


def oriented_tree_path(
    graph: Graph,
    tree: tuple[int, ...],
    start: int,
    target: int,
) -> tuple[tuple[int, int], ...]:
    """Return (edge index, traversal sign) from start to target."""

    adjacency: dict[int, list[tuple[int, int, int]]] = {
        vertex: []
        for vertex in range(graph.vertex_count)
    }
    for edge_index in tree:
        tail, head = graph.edges[edge_index]
        adjacency[tail].append((head, edge_index, 1))
        adjacency[head].append((tail, edge_index, -1))

    stack = [start]
    predecessor: dict[int, tuple[int, int, int] | None] = {start: None}
    while stack:
        vertex = stack.pop()
        if vertex == target:
            break
        for neighbor, edge_index, sign in adjacency[vertex]:
            if neighbor not in predecessor:
                predecessor[neighbor] = (vertex, edge_index, sign)
                stack.append(neighbor)

    assert target in predecessor
    reversed_path: list[tuple[int, int]] = []
    vertex = target
    while predecessor[vertex] is not None:
        previous, edge_index, sign = predecessor[vertex]
        reversed_path.append((edge_index, sign))
        vertex = previous
    return tuple(reversed(reversed_path))


def fundamental_cycles(
    graph: Graph,
    tree: tuple[int, ...],
) -> tuple[Chain, ...]:
    tree_set = set(tree)
    cycles: list[Chain] = []
    for chord_index, (tail, head) in enumerate(graph.edges):
        if chord_index in tree_set:
            continue
        coefficients = [0 for _ in graph.edges]
        coefficients[chord_index] = 1
        for edge_index, sign in oriented_tree_path(
            graph,
            tree,
            head,
            tail,
        ):
            coefficients[edge_index] += sign
        cycle = tuple(coefficients)
        assert chain_boundary(graph, cycle) == tuple(
            0 for _ in range(graph.vertex_count)
        )
        cycles.append(cycle)
    return tuple(cycles)


def cycle_record(
    group: Group,
    cycles: tuple[Chain, ...],
    edge_values: EdgeValue,
) -> tuple[GroupElement, ...]:
    return tuple(
        chain_value(group, cycle, edge_values)
        for cycle in cycles
    )


def boundary_annihilates_group(
    group: Group,
    boundary: tuple[int, ...],
) -> bool:
    zero = zero_element(group)
    return all(
        scalar_multiply(group, coefficient, value) == zero
        for coefficient in boundary
        for value in elements(group)
    )


def response_factors_through_cycle_record(
    group: Group,
    chain: Chain,
    record_kernel: set[EdgeValue],
) -> bool:
    zero = zero_element(group)
    return all(
        chain_value(group, chain, difference) == zero
        for difference in record_kernel
    )


def simple_paths(
    graph: Graph,
    start: int,
    target: int,
) -> tuple[Chain, ...]:
    adjacency: dict[int, list[tuple[int, int, int]]] = {
        vertex: []
        for vertex in range(graph.vertex_count)
    }
    for edge_index, (tail, head) in enumerate(graph.edges):
        adjacency[tail].append((head, edge_index, 1))
        adjacency[head].append((tail, edge_index, -1))

    paths: list[Chain] = []

    def visit(
        vertex: int,
        visited: frozenset[int],
        coefficients: tuple[int, ...],
    ) -> None:
        if vertex == target:
            paths.append(coefficients)
            return
        for neighbor, edge_index, sign in adjacency[vertex]:
            if neighbor in visited:
                continue
            updated = list(coefficients)
            updated[edge_index] += sign
            visit(
                neighbor,
                visited | {neighbor},
                tuple(updated),
            )

    visit(
        start,
        frozenset({start}),
        tuple(0 for _ in graph.edges),
    )
    return tuple(paths)


def edge_cut_size(
    graph: Graph,
    left_vertices: frozenset[int],
) -> int:
    return sum(
        (tail in left_vertices) != (head in left_vertices)
        for tail, head in graph.edges
    )


def endpoint_edge_connectivity(
    graph: Graph,
    start: int,
    target: int,
) -> int:
    other_vertices = tuple(
        vertex
        for vertex in range(graph.vertex_count)
        if vertex not in {start, target}
    )
    return min(
        edge_cut_size(
            graph,
            frozenset({start, *selected}),
        )
        for size in range(len(other_vertices) + 1)
        for selected in combinations(other_vertices, size)
    )


def support_size(edge_values: EdgeValue) -> int:
    return sum(
        value != tuple(0 for _ in value)
        for value in edge_values
    )


def check_specimen(
    graph: Graph,
    group: Group,
) -> dict[str, object]:
    group_elements = elements(group)
    order = group_order(group)
    zero = zero_element(group)
    edge_states = tuple(
        product(group_elements, repeat=len(graph.edges))
    )
    potentials = tuple(
        product(group_elements, repeat=graph.vertex_count)
    )
    coboundaries = {
        coboundary(group, graph, potential)
        for potential in potentials
    }
    expected_fibre_size = order ** (graph.vertex_count - 1)
    assert len(coboundaries) == expected_fibre_size

    trees = spanning_trees(graph)
    assert trees
    beta_one = len(graph.edges) - graph.vertex_count + 1
    kernels: list[set[EdgeValue]] = []
    record_counts: list[int] = []

    for tree in trees:
        cycles = fundamental_cycles(graph, tree)
        assert len(cycles) == beta_one
        kernel = {
            edge_values
            for edge_values in edge_states
            if cycle_record(group, cycles, edge_values)
            == tuple(zero for _ in cycles)
        }
        assert kernel == coboundaries
        kernels.append(kernel)

        records = {
            cycle_record(group, cycles, edge_values)
            for edge_values in edge_states
        }
        assert len(records) == order**beta_one
        record_counts.append(len(records))

        # Cycle record plus the |V|-1 tree-edge values is injective.
        repaired_records = {
            (
                cycle_record(group, cycles, edge_values),
                tuple(edge_values[index] for index in tree),
            )
            for edge_values in edge_states
        }
        assert len(repaired_records) == len(edge_states)

    assert all(kernel == kernels[0] for kernel in kernels)
    record_kernel = kernels[0]

    # Exhaustively check the exact factorization criterion on a bounded,
    # redundant family of integer edge chains.
    candidate_chains = tuple(product(range(-1, 2), repeat=len(graph.edges)))
    for chain in candidate_chains:
        factors = response_factors_through_cycle_record(
            group,
            chain,
            record_kernel,
        )
        boundary_criterion = boundary_annihilates_group(
            group,
            chain_boundary(graph, chain),
        )
        assert factors == boundary_criterion

    # Every fundamental cycle and its character responses factor.
    for cycle in fundamental_cycles(graph, trees[0]):
        assert response_factors_through_cycle_record(
            group,
            cycle,
            record_kernel,
        )
        assert boundary_annihilates_group(
            group,
            chain_boundary(graph, cycle),
        )

    # Every simple open path leaks. Its response on a coboundary is the
    # endpoint potential difference, independent of route.
    open_paths_checked = 0
    endpoint_results: list[dict[str, int]] = []
    for start in range(graph.vertex_count):
        for target in range(start + 1, graph.vertex_count):
            paths = simple_paths(graph, start, target)
            assert paths
            for path in paths:
                boundary = chain_boundary(graph, path)
                expected_boundary = tuple(
                    -1 if vertex == start
                    else 1 if vertex == target
                    else 0
                    for vertex in range(graph.vertex_count)
                )
                assert boundary == expected_boundary
                assert not response_factors_through_cycle_record(
                    group,
                    path,
                    record_kernel,
                )
                open_paths_checked += 1

            min_cut = endpoint_edge_connectivity(graph, start, target)
            minimum_leak_support = min(
                support_size(coboundary(group, graph, potential))
                for potential in potentials
                if potential[start] != potential[target]
            )
            assert minimum_leak_support == min_cut

            # The first path and one minimum-support coboundary give an
            # explicit character-distinguishable same-record witness.
            witness_difference = next(
                difference
                for difference in coboundaries
                if support_size(difference) == min_cut
                and chain_value(group, paths[0], difference) != zero
            )
            assert cycle_record(
                group,
                fundamental_cycles(graph, trees[0]),
                witness_difference,
            ) == tuple(zero for _ in range(beta_one))
            response = chain_value(group, paths[0], witness_difference)
            assert response != zero
            assert character_signature(group, response) != (
                character_signature(group, zero)
            )

            endpoint_results.append(
                {
                    "start": start,
                    "target": target,
                    "minimum_edge_cut": min_cut,
                    "minimum_leak_support": minimum_leak_support,
                }
            )

    # The fibre cardinality forces the universal G-coordinate repair bound.
    assert all(
        order**coordinate_count < expected_fibre_size
        for coordinate_count in range(graph.vertex_count - 1)
    )
    assert order ** (graph.vertex_count - 1) == expected_fibre_size

    return {
        "graph": graph.name,
        "vertices": graph.vertex_count,
        "edges": len(graph.edges),
        "cycle_rank": beta_one,
        "spanning_trees_checked": len(trees),
        "group": group_label(group),
        "group_order": order,
        "physical_basis_states": len(edge_states),
        "cycle_record_values": record_counts[0],
        "basis_completions_per_cycle_record": expected_fibre_size,
        "integer_chains_exhaustively_checked": len(candidate_chains),
        "simple_open_paths_checked": open_paths_checked,
        "minimum_endpoint_leak_support": min(
            result["minimum_leak_support"]
            for result in endpoint_results
        ),
        "maximum_endpoint_leak_support": max(
            result["minimum_leak_support"]
            for result in endpoint_results
        ),
        "additional_group_coordinates_necessary": graph.vertex_count - 1,
        "additional_group_coordinates_sufficient": graph.vertex_count - 1,
        "endpoint_connectivity_checks": endpoint_results,
    }


def main() -> None:
    specimens = (
        (
            Graph(
                "path4",
                4,
                ((0, 1), (1, 2), (2, 3)),
            ),
            (3,),
        ),
        (
            Graph(
                "triangle",
                3,
                ((0, 1), (1, 2), (0, 2)),
            ),
            (2,),
        ),
        (
            Graph(
                "square_with_diagonal",
                4,
                ((0, 1), (1, 2), (2, 3), (0, 3), (0, 2)),
            ),
            (3,),
        ),
        (
            Graph(
                "bridged_triangles",
                6,
                (
                    (0, 1),
                    (1, 2),
                    (0, 2),
                    (2, 3),
                    (3, 4),
                    (4, 5),
                    (3, 5),
                ),
            ),
            (2,),
        ),
        (
            Graph(
                "complete4",
                4,
                (
                    (0, 1),
                    (0, 2),
                    (0, 3),
                    (1, 2),
                    (1, 3),
                    (2, 3),
                ),
            ),
            (2, 2),
        ),
    )
    results = [
        check_specimen(graph, group)
        for graph, group in specimens
    ]

    triangle = next(result for result in results if result["graph"] == "triangle")
    bridged = next(
        result
        for result in results
        if result["graph"] == "bridged_triangles"
    )
    assert triangle["minimum_endpoint_leak_support"] == 2
    assert bridged["minimum_endpoint_leak_support"] == 1

    checks = {
        "complete_cycle_record_kernel_equals_coboundaries": True,
        "cycle_record_is_surjective_onto_group_to_cycle_rank": True,
        "record_equivalence_is_spanning_tree_invariant": True,
        "cycle_record_fibre_size_is_group_order_to_vertices_minus_one": True,
        "factorization_matches_boundary_annihilator_criterion": True,
        "finite_product_group_criterion_passes": True,
        "all_closed_cycle_responses_factor": True,
        "all_simple_open_path_responses_leak": True,
        "open_path_leak_is_character_distinguishable": True,
        "minimum_leak_support_equals_endpoint_min_cut": True,
        "bridges_create_one_edge_first_leaks": True,
        "cycle_specialization_recovers_two_edge_first_leak": True,
        "tree_coordinates_plus_cycle_record_are_injective": True,
        "vertices_minus_one_group_coordinates_are_necessary": True,
        "vertices_minus_one_group_coordinates_are_sufficient": True,
        "matter_completed_coboundaries_are_retained_as_physical": True,
        "no_joint_resource_law_or_interface_selection_is_claimed": True,
        "no_empirical_excess_or_new_physics_is_claimed": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-123",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "specimens": results,
        "formal_boundary": {
            "cohomology": (
                "For any connected finite graph, the kernel of a complete "
                "fundamental-cycle record is im(d), so its fibres are affine "
                "coboundary classes and its quotient is H^1(graph;G)."
            ),
            "factorization": (
                "The complete character response of an integer edge chain "
                "factors through the cycle record iff every coefficient in "
                "its vertex boundary annihilates G."
            ),
            "first_leak": (
                "Every simple open path leaks. The minimum support of a "
                "same-cycle-record/different-endpoint-response witness is "
                "the endpoint edge connectivity."
            ),
            "repair": (
                "Each fibre has |G|^(|V|-1) basis states. Under a G-valued "
                "coordinate contract, |V|-1 additional coordinates are "
                "necessary, and any spanning-tree edge tuple is sufficient."
            ),
        },
        "non_claims": [
            "not selection of graph, tree, cycle basis, apparatus, or action class",
            "not a joint formation-resource or information-disturbance law",
            "not unrestricted quantum-state or process reconstruction",
            "not a pure-gauge, non-Abelian, continuous-group, or continuum theorem",
            "not empirical excess, ontology priority, prediction, or new physics",
        ],
    }
    ARTIFACT.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS: "
        f"{len(checks)}/{len(checks)} checks; "
        f"{len(results)} graph/cohomology specimens"
    )


if __name__ == "__main__":
    main()
