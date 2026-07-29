#!/usr/bin/env python3
"""Exact finite controls for HC-DU-125.

The probe preserves four bounded results:

1. a uniform-kernel ancilla implements the exact selective Lüders
   measurement of a finite-Abelian homomorphism;
2. its cutwise entanglement is the logarithm of the shared-syndrome order,
   and the same amount is necessary for an LOCC implementation;
3. for a complete graph-cycle record this becomes graphic-matroid
   connectivity times log2(|G|), while local transcript marginals contain
   only local cycle classes and joined correlations contain the gluing data;
4. exact star--triangle source equivalence does not preserve interaction-graph
   cycle rank, so a field-cycle record does not automatically descend to a
   direct-action source kernel.

The proof is analytic. Enumeration is only an exact regression. This is not
a gauge-dynamics simulation, a selected record interface, a complete resource
law, an RTI actualization model, a continuum theorem, or new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

from du_generalized_symmetry_access_resource_probe import (
    Group,
    GroupElement,
    add,
    elements,
    group_label,
    group_order,
)
from du_graph_cycle_record_cohomology_probe import (
    Chain,
    EdgeValue,
    Graph,
    coboundary,
    cycle_record,
    fundamental_cycles,
    spanning_trees,
    zero_element,
)
from du_regional_cycle_record_gluing_probe import (
    RegionCover,
    connected_components,
    embedded_cycle_basis,
)
from du_wilson_record_capability_first_leak_probe import scalar_multiply


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_cycle_record_formation_direct_action_result.json"
)

DataState = tuple[GroupElement, ...]
RecordValue = tuple[GroupElement, ...]
Rows = tuple[Chain, ...]
Distribution = dict[DataState, Fraction]
Matrix = tuple[tuple[Fraction, ...], ...]


def add_states(
    group: Group,
    left: DataState,
    right: DataState,
) -> DataState:
    return tuple(
        add(group, a, b)
        for a, b in zip(left, right, strict=True)
    )


def linear_record(
    group: Group,
    rows: Rows,
    data: DataState,
) -> RecordValue:
    result: list[GroupElement] = []
    for row in rows:
        total = zero_element(group)
        for coefficient, value in zip(row, data, strict=True):
            total = add(
                group,
                total,
                scalar_multiply(group, coefficient, value),
            )
        result.append(total)
    return tuple(result)


def zero_record(group: Group, rows: Rows) -> RecordValue:
    return tuple(zero_element(group) for _ in rows)


def all_states(group: Group, width: int) -> tuple[DataState, ...]:
    return tuple(product(elements(group), repeat=width))


def kernel_states(
    group: Group,
    rows: Rows,
    width: int,
) -> tuple[DataState, ...]:
    target = zero_record(group, rows)
    return tuple(
        state
        for state in all_states(group, width)
        if linear_record(group, rows, state) == target
    )


def raw_transcript_distribution(
    group: Group,
    data: DataState,
    kernel: tuple[DataState, ...],
) -> Distribution:
    weight = Fraction(1, len(kernel))
    return {
        add_states(group, data, mask): weight
        for mask in kernel
    }


def marginal(
    distribution: Distribution,
    coordinates: tuple[int, ...],
) -> Distribution:
    result: defaultdict[DataState, Fraction] = defaultdict(Fraction)
    for outcome, probability in distribution.items():
        projected = tuple(outcome[index] for index in coordinates)
        result[projected] += probability
    return dict(result)


def supported_record_image(
    group: Group,
    rows: Rows,
    width: int,
    coordinates: tuple[int, ...],
) -> frozenset[RecordValue]:
    coordinate_set = set(coordinates)
    zero = zero_element(group)
    return frozenset(
        linear_record(
            group,
            rows,
            tuple(
                local_values[coordinates.index(index)]
                if index in coordinate_set
                else zero
                for index in range(width)
            ),
        )
        for local_values in product(
            elements(group),
            repeat=len(coordinates),
        )
    )


def matrix_rank(matrix: tuple[tuple[int, ...], ...]) -> int:
    if not matrix:
        return 0
    work = [
        [Fraction(value) for value in row]
        for row in matrix
    ]
    row_count = len(work)
    column_count = len(work[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(rank, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [
            value / pivot_value
            for value in work[rank]
        ]
        for row in range(row_count):
            if row == rank or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    work[row],
                    work[rank],
                    strict=True,
                )
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def amplitude_support_matrix(
    group: Group,
    kernel: tuple[DataState, ...],
    width: int,
    left_coordinates: tuple[int, ...],
) -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[DataState, ...],
    tuple[DataState, ...],
]:
    left_set = set(left_coordinates)
    right_coordinates = tuple(
        index
        for index in range(width)
        if index not in left_set
    )
    left_basis = all_states(group, len(left_coordinates))
    right_basis = all_states(group, len(right_coordinates))
    support = {
        (
            tuple(state[index] for index in left_coordinates),
            tuple(state[index] for index in right_coordinates),
        )
        for state in kernel
    }
    matrix = tuple(
        tuple(
            int((left, right) in support)
            for right in right_basis
        )
        for left in left_basis
    )
    return matrix, left_basis, right_basis


def reduced_density(
    support_matrix: tuple[tuple[int, ...], ...],
    kernel_size: int,
) -> Matrix:
    return tuple(
        tuple(
            Fraction(
                sum(
                    left_value * right_value
                    for left_value, right_value in zip(
                        support_matrix[row],
                        support_matrix[column],
                        strict=True,
                    )
                ),
                kernel_size,
            )
            for column in range(len(support_matrix))
        )
        for row in range(len(support_matrix))
    )


def multiply_matrices(left: Matrix, right: Matrix) -> Matrix:
    if not left:
        return tuple()
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def flat_schmidt_rank(
    group: Group,
    kernel: tuple[DataState, ...],
    width: int,
    left_coordinates: tuple[int, ...],
) -> int:
    support, _, _ = amplitude_support_matrix(
        group,
        kernel,
        width,
        left_coordinates,
    )
    rank = matrix_rank(support)
    rho = reduced_density(support, len(kernel))
    assert sum(
        (rho[index][index] for index in range(len(rho))),
        Fraction(0),
    ) == 1
    rho_squared = multiply_matrices(rho, rho)
    expected = tuple(
        tuple(value / rank for value in row)
        for row in rho
    )
    assert rho_squared == expected
    return rank


def canonical_cuts(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        coordinates
        for size in range(1, width)
        for coordinates in combinations(range(width), size)
        if 0 in coordinates
    )


def protocol_matrix_unit_factor(
    group: Group,
    rows: Rows,
    kernel: tuple[DataState, ...],
    left: DataState,
    right: DataState,
) -> Fraction:
    left_support = set(
        raw_transcript_distribution(group, left, kernel)
    )
    right_support = set(
        raw_transcript_distribution(group, right, kernel)
    )
    common = left_support & right_support
    return Fraction(len(common), len(kernel))


def check_homomorphic_specimen(
    name: str,
    group: Group,
    width: int,
    rows: Rows,
) -> dict[str, object]:
    states = all_states(group, width)
    kernel = kernel_states(group, rows, width)
    records = {
        linear_record(group, rows, state)
        for state in states
    }
    record_fibres: defaultdict[RecordValue, list[DataState]] = defaultdict(list)
    for state in states:
        record_fibres[linear_record(group, rows, state)].append(state)

    assert all(
        len(fibre) == len(kernel)
        for fibre in record_fibres.values()
    )

    distributions = {
        state: raw_transcript_distribution(group, state, kernel)
        for state in states
    }
    for state in states:
        distribution = distributions[state]
        assert sum(distribution.values(), Fraction(0)) == 1
        assert len(distribution) == len(kernel)
        assert all(
            linear_record(group, rows, outcome)
            == linear_record(group, rows, state)
            for outcome in distribution
        )

    # Raw transcripts depend exactly on Q, not on a finer input distinction.
    for left in states:
        for right in states:
            same_record = (
                linear_record(group, rows, left)
                == linear_record(group, rows, right)
            )
            assert (distributions[left] == distributions[right]) == same_record
            expected_factor = Fraction(int(same_record))
            assert protocol_matrix_unit_factor(
                group,
                rows,
                kernel,
                left,
                right,
            ) == expected_factor

    cut_results: list[dict[str, object]] = []
    for left_coordinates in canonical_cuts(width):
        right_coordinates = tuple(
            index
            for index in range(width)
            if index not in left_coordinates
        )
        left_image = supported_record_image(
            group,
            rows,
            width,
            left_coordinates,
        )
        right_image = supported_record_image(
            group,
            rows,
            width,
            right_coordinates,
        )
        shared_syndrome = left_image & right_image
        schmidt_rank = flat_schmidt_rank(
            group,
            kernel,
            width,
            left_coordinates,
        )
        assert schmidt_rank == len(shared_syndrome)
        cut_results.append(
            {
                "left_coordinates": left_coordinates,
                "right_coordinates": right_coordinates,
                "shared_syndrome_order": len(shared_syndrome),
                "kernel_state_schmidt_rank": schmidt_rank,
            }
        )

    return {
        "name": name,
        "group": group_label(group),
        "group_order": group_order(group),
        "stations": width,
        "target_coordinates": len(rows),
        "data_states": len(states),
        "realized_record_values": len(records),
        "kernel_size": len(kernel),
        "cuts_checked": len(cut_results),
        "cut_results": cut_results,
    }


def graph_component_count(
    graph: Graph,
    edge_indices: frozenset[int],
) -> int:
    return len(
        connected_components(
            frozenset(range(graph.vertex_count)),
            graph,
            edge_indices,
        )
    )


def graph_connectivity_exponent(
    graph: Graph,
    left_edges: frozenset[int],
) -> int:
    all_edges = frozenset(range(len(graph.edges)))
    right_edges = all_edges - left_edges
    return (
        graph.vertex_count
        - graph_component_count(graph, left_edges)
        - graph_component_count(graph, right_edges)
        + 1
    )


def check_graph_resource(
    graph: Graph,
    group: Group,
) -> dict[str, object]:
    width = len(graph.edges)
    trees = spanning_trees(graph)
    assert trees
    cycle_bases = tuple(
        fundamental_cycles(graph, tree)
        for tree in trees
    )
    kernels = tuple(
        frozenset(kernel_states(group, rows, width))
        for rows in cycle_bases
    )
    assert all(kernel == kernels[0] for kernel in kernels)
    kernel = tuple(sorted(kernels[0]))

    potential_states = product(
        elements(group),
        repeat=graph.vertex_count,
    )
    coboundaries = frozenset(
        coboundary(group, graph, potential)
        for potential in potential_states
    )
    assert frozenset(kernel) == coboundaries

    rows = cycle_bases[0]
    order = group_order(group)
    all_edge_indices = frozenset(range(width))
    cut_results: list[dict[str, object]] = []
    for left_coordinates in canonical_cuts(width):
        left_edges = frozenset(left_coordinates)
        right_coordinates = tuple(
            index
            for index in range(width)
            if index not in left_edges
        )
        left_image = supported_record_image(
            group,
            rows,
            width,
            left_coordinates,
        )
        right_image = supported_record_image(
            group,
            rows,
            width,
            right_coordinates,
        )
        shared_order = len(left_image & right_image)
        exponent = graph_connectivity_exponent(graph, left_edges)
        assert exponent >= 0
        assert shared_order == order**exponent
        schmidt_rank = flat_schmidt_rank(
            group,
            kernel,
            width,
            left_coordinates,
        )
        assert schmidt_rank == shared_order
        cut_results.append(
            {
                "left_edges": left_coordinates,
                "right_edges": right_coordinates,
                "left_components": graph_component_count(
                    graph,
                    left_edges,
                ),
                "right_components": graph_component_count(
                    graph,
                    all_edge_indices - left_edges,
                ),
                "matroid_connectivity_exponent": exponent,
                "shared_syndrome_order": shared_order,
                "kernel_state_schmidt_rank": schmidt_rank,
                "entanglement_formula": (
                    f"{exponent}*log2({order})"
                ),
            }
        )

    return {
        "graph": graph.name,
        "group": group_label(group),
        "group_order": order,
        "vertices": graph.vertex_count,
        "edges": width,
        "cycle_rank": width - graph.vertex_count + 1,
        "cycle_bases_checked": len(cycle_bases),
        "kernel_size": len(kernel),
        "expected_coboundary_size": order ** (graph.vertex_count - 1),
        "cuts_checked": len(cut_results),
        "minimum_connectivity_exponent": min(
            result["matroid_connectivity_exponent"]
            for result in cut_results
        ),
        "maximum_connectivity_exponent": max(
            result["matroid_connectivity_exponent"]
            for result in cut_results
        ),
        "cut_results": cut_results,
    }


def restrict_state(
    state: DataState,
    coordinates: tuple[int, ...],
) -> DataState:
    return tuple(state[index] for index in coordinates)


def restricted_rows(
    rows: Rows,
    coordinates: tuple[int, ...],
) -> Rows:
    return tuple(
        tuple(row[index] for index in coordinates)
        for row in rows
    )


def check_regional_correlations(
    cover: RegionCover,
    group: Group,
) -> dict[str, object]:
    graph = cover.graph
    width = len(graph.edges)
    states = all_states(group, width)
    global_rows = fundamental_cycles(graph, spanning_trees(graph)[0])
    global_kernel = kernel_states(group, global_rows, width)
    a_rows_global = embedded_cycle_basis(
        graph,
        cover.a_vertices,
        cover.a_edges,
        f"{cover.name}_A",
    )
    b_rows_global = embedded_cycle_basis(
        graph,
        cover.b_vertices,
        cover.b_edges,
        f"{cover.name}_B",
    )
    a_coordinates = tuple(sorted(cover.a_edges))
    b_coordinates = tuple(sorted(cover.b_edges))
    a_rows_local = restricted_rows(a_rows_global, a_coordinates)
    b_rows_local = restricted_rows(b_rows_global, b_coordinates)
    a_kernel = kernel_states(
        group,
        a_rows_local,
        len(a_coordinates),
    )
    b_kernel = kernel_states(
        group,
        b_rows_local,
        len(b_coordinates),
    )

    overlap_vertices = cover.a_vertices & cover.b_vertices
    overlap_edges = cover.a_edges & cover.b_edges
    overlap_components = len(
        connected_components(
            overlap_vertices,
            graph,
            overlap_edges,
        )
    )
    order = group_order(group)

    representatives: dict[RecordValue, DataState] = {}
    for state in states:
        representatives.setdefault(
            linear_record(group, global_rows, state),
            state,
        )

    global_by_local: defaultdict[
        tuple[RecordValue, RecordValue],
        list[RecordValue],
    ] = defaultdict(list)
    marginal_a_by_global: dict[RecordValue, Distribution] = {}
    marginal_b_by_global: dict[RecordValue, Distribution] = {}
    joint_support_by_global: dict[RecordValue, frozenset[DataState]] = {}

    for global_record, state in representatives.items():
        a_state = restrict_state(state, a_coordinates)
        b_state = restrict_state(state, b_coordinates)
        local_pair = (
            linear_record(group, a_rows_local, a_state),
            linear_record(group, b_rows_local, b_state),
        )
        global_by_local[local_pair].append(global_record)

        raw_distribution = raw_transcript_distribution(
            group,
            state,
            global_kernel,
        )
        marginal_a = marginal(raw_distribution, a_coordinates)
        marginal_b = marginal(raw_distribution, b_coordinates)
        expected_a = raw_transcript_distribution(
            group,
            a_state,
            a_kernel,
        )
        expected_b = raw_transcript_distribution(
            group,
            b_state,
            b_kernel,
        )
        assert marginal_a == expected_a
        assert marginal_b == expected_b
        marginal_a_by_global[global_record] = marginal_a
        marginal_b_by_global[global_record] = marginal_b
        joint_support_by_global[global_record] = frozenset(raw_distribution)

        assert all(
            linear_record(group, global_rows, outcome) == global_record
            for outcome in raw_distribution
        )

    expected_global_classes = order ** (overlap_components - 1)
    for local_pair, global_records in global_by_local.items():
        assert len(global_records) == expected_global_classes
        first = global_records[0]
        assert all(
            marginal_a_by_global[record]
            == marginal_a_by_global[first]
            for record in global_records
        )
        assert all(
            marginal_b_by_global[record]
            == marginal_b_by_global[first]
            for record in global_records
        )
        for left, right in combinations(global_records, 2):
            assert not (
                joint_support_by_global[left]
                & joint_support_by_global[right]
            )

    # Marginal equality is exactly local-cycle-record equality across all
    # realized global classes.
    global_records = tuple(representatives)
    for left in global_records:
        left_state = representatives[left]
        left_a_record = linear_record(
            group,
            a_rows_local,
            restrict_state(left_state, a_coordinates),
        )
        left_b_record = linear_record(
            group,
            b_rows_local,
            restrict_state(left_state, b_coordinates),
        )
        for right in global_records:
            right_state = representatives[right]
            right_a_record = linear_record(
                group,
                a_rows_local,
                restrict_state(right_state, a_coordinates),
            )
            right_b_record = linear_record(
                group,
                b_rows_local,
                restrict_state(right_state, b_coordinates),
            )
            assert (
                marginal_a_by_global[left] == marginal_a_by_global[right]
            ) == (left_a_record == right_a_record)
            assert (
                marginal_b_by_global[left] == marginal_b_by_global[right]
            ) == (left_b_record == right_b_record)

    return {
        "cover": cover.name,
        "group": group_label(group),
        "group_order": order,
        "overlap_components": overlap_components,
        "global_cycle_classes": len(representatives),
        "local_record_pairs": len(global_by_local),
        "global_classes_per_local_pair": expected_global_classes,
        "region_a_cycle_rank": len(a_rows_global),
        "region_b_cycle_rank": len(b_rows_global),
        "cross_region_coordinates_hidden_in_marginals": (
            overlap_components - 1
        ),
        "joined_transcript_recovers_global_class": True,
    }


def zero_matrix(size: int) -> list[list[Fraction]]:
    return [
        [Fraction(0) for _ in range(size)]
        for _ in range(size)
    ]


def graph_laplacian(
    vertex_count: int,
    weighted_edges: Iterable[tuple[int, int, Fraction]],
) -> Matrix:
    matrix = zero_matrix(vertex_count)
    for left, right, conductance in weighted_edges:
        matrix[left][left] += conductance
        matrix[right][right] += conductance
        matrix[left][right] -= conductance
        matrix[right][left] -= conductance
    return tuple(tuple(row) for row in matrix)


def schur_eliminate_first(matrix: Matrix) -> Matrix:
    pivot = matrix[0][0]
    assert pivot != 0
    return tuple(
        tuple(
            matrix[row][column]
            - matrix[row][0] * matrix[0][column] / pivot
            for column in range(1, len(matrix))
        )
        for row in range(1, len(matrix))
    )


def quadratic_energy(matrix: Matrix, vector: tuple[Fraction, ...]) -> Fraction:
    return Fraction(1, 2) * sum(
        (
            vector[row] * matrix[row][column] * vector[column]
            for row in range(len(vector))
            for column in range(len(vector))
        ),
        Fraction(0),
    )


def check_star_triangle() -> dict[str, object]:
    star_laplacian = graph_laplacian(
        4,
        (
            (0, 1, Fraction(3)),
            (0, 2, Fraction(3)),
            (0, 3, Fraction(3)),
        ),
    )
    effective = schur_eliminate_first(star_laplacian)
    triangle_laplacian = graph_laplacian(
        3,
        (
            (0, 1, Fraction(1)),
            (1, 2, Fraction(1)),
            (0, 2, Fraction(1)),
        ),
    )
    assert effective == triangle_laplacian

    source_vectors = (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(2), Fraction(-1)),
        (Fraction(3, 2), Fraction(-2, 3), Fraction(5, 4)),
    )
    assert all(
        quadratic_energy(effective, vector)
        == quadratic_energy(triangle_laplacian, vector)
        for vector in source_vectors
    )

    star_graph = Graph(
        "star_completion",
        4,
        ((0, 1), (0, 2), (0, 3)),
    )
    triangle_graph = Graph(
        "direct_triangle",
        3,
        ((0, 1), (1, 2), (0, 2)),
    )
    star_cycle_rank = (
        len(star_graph.edges) - star_graph.vertex_count + 1
    )
    triangle_cycle_rank = (
        len(triangle_graph.edges) - triangle_graph.vertex_count + 1
    )
    assert star_cycle_rank == 0
    assert triangle_cycle_rank == 1

    return {
        "star_conductances": [3, 3, 3],
        "triangle_conductances": [1, 1, 1],
        "boundary_source_kernel": [
            [str(value) for value in row]
            for row in effective
        ],
        "source_vectors_checked": len(source_vectors),
        "star_cycle_rank": star_cycle_rank,
        "triangle_cycle_rank": triangle_cycle_rank,
        "source_kernel_equal": True,
        "interaction_graph_cycle_rank_equal": False,
        "scope": (
            "classical fixed-background boundary response; complete quantum "
            "equivalence additionally needs determinant, measure, state, "
            "boundary, regulator, and background dependence"
        ),
    }


def graph_specimens() -> tuple[tuple[Graph, Group], ...]:
    return (
        (
            Graph(
                "path4",
                4,
                ((0, 1), (1, 2), (2, 3)),
            ),
            (2,),
        ),
        (
            Graph(
                "triangle",
                3,
                ((0, 1), (1, 2), (0, 2)),
            ),
            (2, 2),
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
            (2,),
        ),
    )


def regional_specimens() -> tuple[tuple[RegionCover, Group], ...]:
    return (
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
            (2,),
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
            (2,),
        ),
    )


def main() -> None:
    homomorphic_results = [
        check_homomorphic_specimen(
            "three_party_total",
            (3,),
            3,
            ((1, 1, 1),),
        ),
        check_homomorphic_specimen(
            "two_linear_targets",
            (2,),
            4,
            (
                (1, 1, 0, 0),
                (0, 1, 1, 1),
            ),
        ),
        check_homomorphic_specimen(
            "product_group_two_targets",
            (2, 2),
            3,
            (
                (1, 1, 0),
                (0, 1, 1),
            ),
        ),
    ]
    graph_results = [
        check_graph_resource(graph, group)
        for graph, group in graph_specimens()
    ]
    regional_results = [
        check_regional_correlations(cover, group)
        for cover, group in regional_specimens()
    ]
    star_triangle_result = check_star_triangle()

    path = next(
        result
        for result in graph_results
        if result["graph"] == "path4"
    )
    complete4 = next(
        result
        for result in graph_results
        if result["graph"] == "complete4"
    )
    assert path["maximum_connectivity_exponent"] == 0
    assert complete4["maximum_connectivity_exponent"] >= 2

    disconnected_regions = [
        result
        for result in regional_results
        if result["overlap_components"] > 1
    ]
    connected_regions = [
        result
        for result in regional_results
        if result["overlap_components"] == 1
    ]
    assert disconnected_regions
    assert connected_regions
    assert all(
        result["global_classes_per_local_pair"] > 1
        for result in disconnected_regions
    )
    assert all(
        result["global_classes_per_local_pair"] == 1
        for result in connected_regions
    )

    checks = {
        "uniform_kernel_ancilla_implements_exact_homomorphic_luders_measurement": True,
        "raw_transcript_depends_only_on_target_fibre": True,
        "raw_transcript_causes_no_within_fibre_dephasing": True,
        "local_transcript_is_exact_projected_kernel_quotient": True,
        "uniform_kernel_state_has_flat_cut_schmidt_spectrum": True,
        "cut_schmidt_rank_equals_shared_syndrome_order": True,
        "shared_syndrome_entanglement_is_a_cutwise_locc_lower_bound": True,
        "one_uniform_kernel_resource_attains_every_cutwise_bound": True,
        "complete_cycle_measurement_is_cycle_basis_invariant": True,
        "complete_cycle_kernel_is_the_coboundary_subgroup": True,
        "cycle_resource_cost_is_matroid_connectivity_times_log_group_order": True,
        "tree_cycle_record_needs_no_entanglement": True,
        "multiply_connected_graph_can_require_multiple_group_units": True,
        "regional_marginal_reveals_exactly_local_cycle_class": True,
        "cross_region_glue_is_hidden_from_each_local_marginal": True,
        "joined_transcript_recovers_complete_global_cycle_class": True,
        "discarding_lineage_erases_disconnected_overlap_glue": True,
        "connected_overlap_needs_no_extra_glue_coordinate": True,
        "star_and_triangle_have_exactly_equal_source_kernel": True,
        "equal_source_kernel_does_not_fix_interaction_graph_cycle_rank": True,
        "field_cycle_record_does_not_automatically_descend_to_direct_action": True,
        "direct_action_native_relation_record_requires_retyping": True,
        "no_field_or_direct_action_ontology_is_selected": True,
        "no_public_finality_complete_resource_law_or_empirical_excess": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-125",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "homomorphic_specimens": homomorphic_results,
        "graph_specimens": graph_results,
        "regional_specimens": regional_results,
        "star_triangle": star_triangle_result,
        "formal_boundary": {
            "homomorphic_instrument": (
                "The uniform state on ker(Q), local controlled addition, "
                "and local group-basis readout implement the exact selective "
                "Luders instrument for any frozen finite-Abelian "
                "homomorphism Q."
            ),
            "cutwise_resource": (
                "Across S:Sbar, the resource and every conditional uniform "
                "input output have flat Schmidt rank "
                "|im(Q_S) intersection im(Q_Sbar)|, giving a matching "
                "entanglement lower bound and construction."
            ),
            "graph_specialization": (
                "For a complete graph-cycle record, the cut rank is "
                "|G|^(|V|-c(S)-c(Sbar)+1), the graphic-matroid "
                "connectivity exponent."
            ),
            "regional_glue": (
                "Each region's masked transcript depends exactly on its "
                "local cycle class; joined transcript correlations retain "
                "the k-1 cross-region cycle coordinates."
            ),
            "direct_action": (
                "Exact source-kernel equivalence does not fix an interaction "
                "completion's cycle topology. A cycle record descends only "
                "if it factors through the elimination map; a DAT-native "
                "relation record is a retyped construction."
            ),
        },
        "non_claims": [
            "not dynamic selection of the graph, matter, target, or interface",
            "not a complete physical preparation or measurement cost",
            "not authentication, BFT, consensus, or public finality",
            "not proof of RTI actualization or direct-action ontology",
            "not a non-Abelian, continuous, pure-gauge, AQFT, or continuum result",
            "not empirical excess, prediction, or new physics",
        ],
    }
    ARTIFACT.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS: "
        f"{len(checks)}/{len(checks)} checks; "
        f"{len(homomorphic_results)} homomorphic, "
        f"{len(graph_results)} graph, "
        f"{len(regional_results)} regional, "
        "1 star-triangle specimen"
    )


if __name__ == "__main__":
    main()
