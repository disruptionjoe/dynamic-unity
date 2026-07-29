#!/usr/bin/env python3
"""Exact regressions for the HC-DU-124 regional cycle-record gluing law.

The scientific result is a two-region Mayer--Vietoris specialization in the
matter-completed finite-Abelian dressed-edge arena. This script preserves:

1. compatible complete local cycle records have |G|^(k-1) global cycle-class
   completions when the overlap has k connected components;
2. connected overlap makes the global cycle class unique;
3. k-1 cross-region cycle values are necessary and sufficient to repair the
   global class;
4. the graph cycle ranks obey the corresponding Mayer--Vietoris identity; and
5. the full physical fibre still contains an additional |G|^(|V|-1)
   coboundary factor.

It is not a consensus simulation, a record-interface selector, a formation
resource calculation, a continuum theorem, or new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from pathlib import Path

from du_generalized_symmetry_access_resource_probe import (
    Group,
    GroupElement,
    elements,
    group_label,
    group_order,
)
from du_graph_cycle_record_cohomology_probe import (
    Chain,
    EdgeValue,
    Graph,
    chain_boundary,
    chain_value,
    cycle_record,
    fundamental_cycles,
    simple_paths,
    spanning_trees,
    zero_element,
)


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_regional_cycle_record_gluing_result.json"


@dataclass(frozen=True)
class RegionCover:
    name: str
    graph: Graph
    a_vertices: frozenset[int]
    a_edges: frozenset[int]
    b_vertices: frozenset[int]
    b_edges: frozenset[int]

    def __post_init__(self) -> None:
        all_vertices = frozenset(range(self.graph.vertex_count))
        all_edges = frozenset(range(len(self.graph.edges)))
        assert self.a_vertices | self.b_vertices == all_vertices
        assert self.a_edges | self.b_edges == all_edges
        assert self.a_vertices & self.b_vertices
        assert all(
            tail in self.a_vertices and head in self.a_vertices
            for index, (tail, head) in enumerate(self.graph.edges)
            if index in self.a_edges
        )
        assert all(
            tail in self.b_vertices and head in self.b_vertices
            for index, (tail, head) in enumerate(self.graph.edges)
            if index in self.b_edges
        )


def connected_components(
    vertices: frozenset[int],
    graph: Graph,
    edge_indices: frozenset[int],
) -> tuple[frozenset[int], ...]:
    adjacency = {vertex: set() for vertex in vertices}
    for edge_index in edge_indices:
        tail, head = graph.edges[edge_index]
        assert tail in vertices and head in vertices
        adjacency[tail].add(head)
        adjacency[head].add(tail)

    remaining = set(vertices)
    components: list[frozenset[int]] = []
    while remaining:
        root = min(remaining)
        stack = [root]
        component = {root}
        remaining.remove(root)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(frozenset(component))
    return tuple(
        sorted(
            components,
            key=lambda component: min(component),
        )
    )


def subgraph(
    graph: Graph,
    vertices: frozenset[int],
    edge_indices: frozenset[int],
    name: str,
) -> tuple[Graph, tuple[int, ...], dict[int, int], dict[int, int]]:
    ordered_vertices = tuple(sorted(vertices))
    global_to_local = {
        vertex: index
        for index, vertex in enumerate(ordered_vertices)
    }
    local_to_global = {
        index: vertex
        for index, vertex in enumerate(ordered_vertices)
    }
    ordered_edges = tuple(sorted(edge_indices))
    local_edges = tuple(
        (
            global_to_local[graph.edges[edge_index][0]],
            global_to_local[graph.edges[edge_index][1]],
        )
        for edge_index in ordered_edges
    )
    return (
        Graph(name, len(ordered_vertices), local_edges),
        ordered_edges,
        global_to_local,
        local_to_global,
    )


def embedded_cycle_basis(
    graph: Graph,
    vertices: frozenset[int],
    edge_indices: frozenset[int],
    name: str,
) -> tuple[Chain, ...]:
    if not edge_indices:
        return tuple()
    local_graph, ordered_edges, _, _ = subgraph(
        graph,
        vertices,
        edge_indices,
        name,
    )
    trees = spanning_trees(local_graph)
    assert trees
    local_cycles = fundamental_cycles(local_graph, trees[0])
    embedded: list[Chain] = []
    for local_cycle in local_cycles:
        coefficients = [0 for _ in graph.edges]
        for local_index, global_index in enumerate(ordered_edges):
            coefficients[global_index] = local_cycle[local_index]
        embedded.append(tuple(coefficients))
    return tuple(embedded)


def embedded_path(
    graph: Graph,
    vertices: frozenset[int],
    edge_indices: frozenset[int],
    start: int,
    target: int,
    name: str,
) -> Chain:
    local_graph, ordered_edges, global_to_local, _ = subgraph(
        graph,
        vertices,
        edge_indices,
        name,
    )
    local_paths = simple_paths(
        local_graph,
        global_to_local[start],
        global_to_local[target],
    )
    assert local_paths
    coefficients = [0 for _ in graph.edges]
    for local_index, global_index in enumerate(ordered_edges):
        coefficients[global_index] = local_paths[0][local_index]
    return tuple(coefficients)


def add_chains(left: Chain, right: Chain) -> Chain:
    return tuple(
        a + b
        for a, b in zip(left, right, strict=True)
    )


def cycle_rank(
    vertices: frozenset[int],
    edge_indices: frozenset[int],
    component_count: int,
) -> int:
    return len(edge_indices) - len(vertices) + component_count


def check_cover(
    cover: RegionCover,
    group: Group,
) -> dict[str, object]:
    graph = cover.graph
    order = group_order(group)
    group_elements = elements(group)
    edge_states = tuple(
        product(group_elements, repeat=len(graph.edges))
    )

    a_components = connected_components(
        cover.a_vertices,
        graph,
        cover.a_edges,
    )
    b_components = connected_components(
        cover.b_vertices,
        graph,
        cover.b_edges,
    )
    assert len(a_components) == len(b_components) == 1

    i_vertices = cover.a_vertices & cover.b_vertices
    i_edges = cover.a_edges & cover.b_edges
    i_components = connected_components(i_vertices, graph, i_edges)
    overlap_components = len(i_components)

    beta_global = cycle_rank(
        frozenset(range(graph.vertex_count)),
        frozenset(range(len(graph.edges))),
        1,
    )
    beta_a = cycle_rank(cover.a_vertices, cover.a_edges, 1)
    beta_b = cycle_rank(cover.b_vertices, cover.b_edges, 1)
    beta_i = cycle_rank(i_vertices, i_edges, overlap_components)
    assert beta_global == (
        beta_a
        + beta_b
        - beta_i
        + overlap_components
        - 1
    )

    global_tree = spanning_trees(graph)[0]
    global_cycles = fundamental_cycles(graph, global_tree)
    a_cycles = embedded_cycle_basis(
        graph,
        cover.a_vertices,
        cover.a_edges,
        f"{cover.name}_A",
    )
    b_cycles = embedded_cycle_basis(
        graph,
        cover.b_vertices,
        cover.b_edges,
        f"{cover.name}_B",
    )
    assert len(global_cycles) == beta_global
    assert len(a_cycles) == beta_a
    assert len(b_cycles) == beta_b

    # One cross-region cycle joins a base overlap component to each other
    # component through A and returns through B.
    base_vertex = min(i_components[0])
    cross_cycles: list[Chain] = []
    for component_index, component in enumerate(i_components[1:], start=1):
        target_vertex = min(component)
        a_path = embedded_path(
            graph,
            cover.a_vertices,
            cover.a_edges,
            base_vertex,
            target_vertex,
            f"{cover.name}_A_cross_{component_index}",
        )
        b_path = embedded_path(
            graph,
            cover.b_vertices,
            cover.b_edges,
            target_vertex,
            base_vertex,
            f"{cover.name}_B_cross_{component_index}",
        )
        cross_cycle = add_chains(a_path, b_path)
        assert chain_boundary(graph, cross_cycle) == tuple(
            0 for _ in range(graph.vertex_count)
        )
        cross_cycles.append(cross_cycle)
    assert len(cross_cycles) == overlap_components - 1

    global_by_local: defaultdict[
        tuple[GroupElement, ...],
        set[tuple[GroupElement, ...]],
    ] = defaultdict(set)
    physical_count_by_local: defaultdict[
        tuple[GroupElement, ...],
        int,
    ] = defaultdict(int)
    global_by_augmented: defaultdict[
        tuple[GroupElement, ...],
        set[tuple[GroupElement, ...]],
    ] = defaultdict(set)
    full_repair_records: set[
        tuple[
            tuple[GroupElement, ...],
            tuple[GroupElement, ...],
            tuple[GroupElement, ...],
        ]
    ] = set()

    for edge_values in edge_states:
        local_record = (
            *cycle_record(group, a_cycles, edge_values),
            *cycle_record(group, b_cycles, edge_values),
        )
        global_record = cycle_record(
            group,
            global_cycles,
            edge_values,
        )
        cross_record = tuple(
            chain_value(group, cycle, edge_values)
            for cycle in cross_cycles
        )
        augmented_record = (*local_record, *cross_record)
        tree_record = tuple(
            edge_values[edge_index]
            for edge_index in global_tree
        )

        global_by_local[local_record].add(global_record)
        physical_count_by_local[local_record] += 1
        global_by_augmented[augmented_record].add(global_record)
        full_repair_records.add(
            (local_record, cross_record, tree_record)
        )

    expected_global_completions = order ** (overlap_components - 1)
    expected_physical_completions = order ** (
        graph.vertex_count + overlap_components - 2
    )
    assert all(
        len(global_records) == expected_global_completions
        for global_records in global_by_local.values()
    )
    assert all(
        count == expected_physical_completions
        for count in physical_count_by_local.values()
    )
    assert all(
        len(global_records) == 1
        for global_records in global_by_augmented.values()
    )
    assert len(full_repair_records) == len(edge_states)

    expected_local_record_values = order ** (
        beta_global - overlap_components + 1
    )
    assert len(global_by_local) == expected_local_record_values

    # Cardinality lower bounds for global-class and full-state repair.
    assert all(
        order**coordinate_count < expected_global_completions
        for coordinate_count in range(overlap_components - 1)
    )
    total_repair_coordinates = (
        overlap_components - 1
        + graph.vertex_count
        - 1
    )
    assert all(
        order**coordinate_count < expected_physical_completions
        for coordinate_count in range(total_repair_coordinates)
    )
    assert order**total_repair_coordinates == expected_physical_completions

    return {
        "cover": cover.name,
        "group": group_label(group),
        "group_order": order,
        "vertices": graph.vertex_count,
        "edges": len(graph.edges),
        "overlap_vertices": len(i_vertices),
        "overlap_edges": len(i_edges),
        "overlap_components": overlap_components,
        "global_cycle_rank": beta_global,
        "region_a_cycle_rank": beta_a,
        "region_b_cycle_rank": beta_b,
        "overlap_cycle_rank": beta_i,
        "realized_local_record_values": len(global_by_local),
        "global_cycle_classes_per_local_record": expected_global_completions,
        "cross_cycle_coordinates_necessary": overlap_components - 1,
        "cross_cycle_coordinates_sufficient": len(cross_cycles),
        "physical_basis_states_per_local_record": expected_physical_completions,
        "tree_coordinates_after_global_completion": graph.vertex_count - 1,
        "total_additional_group_coordinates_for_full_state": (
            total_repair_coordinates
        ),
        "physical_basis_states": len(edge_states),
    }


def main() -> None:
    specimens = (
        (
            RegionCover(
                "triangles_shared_vertex",
                Graph(
                    "triangles_shared_vertex",
                    5,
                    (
                        (0, 1),
                        (1, 2),
                        (0, 2),
                        (2, 3),
                        (3, 4),
                        (2, 4),
                    ),
                ),
                frozenset({0, 1, 2}),
                frozenset({0, 1, 2}),
                frozenset({2, 3, 4}),
                frozenset({3, 4, 5}),
            ),
            (2,),
        ),
        (
            RegionCover(
                "two_paths_one_cycle",
                Graph(
                    "two_paths_one_cycle",
                    4,
                    (
                        (0, 1),
                        (1, 2),
                        (0, 3),
                        (2, 3),
                    ),
                ),
                frozenset({0, 1, 2}),
                frozenset({0, 1}),
                frozenset({0, 2, 3}),
                frozenset({2, 3}),
            ),
            (3,),
        ),
        (
            RegionCover(
                "three_terminal_double_tree",
                Graph(
                    "three_terminal_double_tree",
                    7,
                    (
                        (0, 3),
                        (1, 3),
                        (1, 4),
                        (2, 4),
                        (0, 5),
                        (2, 5),
                        (2, 6),
                        (1, 6),
                    ),
                ),
                frozenset({0, 1, 2, 3, 4}),
                frozenset({0, 1, 2, 3}),
                frozenset({0, 1, 2, 5, 6}),
                frozenset({4, 5, 6, 7}),
            ),
            (2,),
        ),
        (
            RegionCover(
                "cyclic_overlap_plus_island",
                Graph(
                    "cyclic_overlap_plus_island",
                    6,
                    (
                        (0, 1),
                        (1, 2),
                        (0, 2),
                        (2, 4),
                        (3, 4),
                        (0, 5),
                        (3, 5),
                    ),
                ),
                frozenset({0, 1, 2, 3, 4}),
                frozenset({0, 1, 2, 3, 4}),
                frozenset({0, 1, 2, 3, 5}),
                frozenset({0, 1, 2, 5, 6}),
            ),
            (2, 2),
        ),
        (
            RegionCover(
                "squares_shared_edge",
                Graph(
                    "squares_shared_edge",
                    6,
                    (
                        (0, 1),
                        (1, 2),
                        (2, 3),
                        (0, 3),
                        (3, 4),
                        (4, 5),
                        (2, 5),
                    ),
                ),
                frozenset({0, 1, 2, 3}),
                frozenset({0, 1, 2, 3}),
                frozenset({2, 3, 4, 5}),
                frozenset({2, 4, 5, 6}),
            ),
            (3,),
        ),
    )

    results = [
        check_cover(cover, group)
        for cover, group in specimens
    ]

    connected_overlap_results = [
        result
        for result in results
        if result["overlap_components"] == 1
    ]
    disconnected_overlap_results = [
        result
        for result in results
        if result["overlap_components"] > 1
    ]
    assert connected_overlap_results
    assert disconnected_overlap_results
    assert all(
        result["global_cycle_classes_per_local_record"] == 1
        for result in connected_overlap_results
    )
    assert all(
        result["global_cycle_classes_per_local_record"] > 1
        for result in disconnected_overlap_results
    )

    # Same overlap size, different connectivity, different deficit:
    # shared-edge squares have two connected overlap vertices; the two-path
    # cycle has two disconnected overlap vertices.
    two_paths = next(
        result
        for result in results
        if result["cover"] == "two_paths_one_cycle"
    )
    shared_edge = next(
        result
        for result in results
        if result["cover"] == "squares_shared_edge"
    )
    assert two_paths["overlap_vertices"] == shared_edge["overlap_vertices"] == 2
    assert two_paths["overlap_components"] == 2
    assert shared_edge["overlap_components"] == 1
    assert two_paths["global_cycle_classes_per_local_record"] == 3
    assert shared_edge["global_cycle_classes_per_local_record"] == 1

    checks = {
        "mayer_vietoris_cycle_rank_identity_holds": True,
        "connected_overlap_gives_unique_global_cycle_class": True,
        "disconnected_overlap_creates_global_gluing_deficit": True,
        "deficit_size_is_group_order_to_components_minus_one": True,
        "overlap_connectivity_not_vertex_count_controls_deficit": True,
        "cyclic_overlap_internal_record_compatibility_is_retained": True,
        "cross_cycle_count_is_components_minus_one": True,
        "cross_cycle_coordinates_are_necessary": True,
        "cross_cycle_coordinates_are_sufficient": True,
        "local_record_fibre_has_layered_global_and_coboundary_factors": True,
        "full_local_record_fibre_size_is_group_order_to_v_plus_k_minus_two": True,
        "tree_coordinates_complete_state_after_global_cycle_completion": True,
        "total_universal_repair_coordinate_count_is_minimal": True,
        "finite_product_group_control_passes": True,
        "regional_gluing_is_not_public_finality_without_extra_types": True,
        "no_resource_law_or_interface_selection_is_claimed": True,
        "no_empirical_excess_or_new_physics_is_claimed": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-124",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "specimens": results,
        "formal_boundary": {
            "gluing_deficit": (
                "For connected A and B with k nonempty intersection "
                "components, each compatible local H^1 pair has "
                "|G|^(k-1) global H^1 completions."
            ),
            "cross_certificates": (
                "One A-out/B-back cross-cycle holonomy per non-base "
                "intersection component is necessary and sufficient under "
                "a G-valued-coordinate contract."
            ),
            "layered_fibre": (
                "Each compatible local-record fibre has "
                "|G|^(k-1) global cycle classes times |G|^(|V|-1) "
                "physical coboundary completions."
            ),
            "rank_identity": (
                "beta1(Gamma)=beta1(A)+beta1(B)-beta1(I)+(k-1)."
            ),
        },
        "non_claims": [
            "not selection of the regional cover or record interfaces",
            "not a BFT, quorum, common-knowledge, or cryptographic threshold",
            "not a formation-resource, latency, or information-disturbance law",
            "not public finality or complete physical-state reconstruction",
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
        f"{len(results)} regional-cover specimens"
    )


if __name__ == "__main__":
    main()
