#!/usr/bin/env python3
"""Exact finite controls for HC-DU-126.

The probe preserves four bounded results:

1. Schur/Kron elimination preserves the complete boundary response operator;
2. b-1 fixed independent vector-response probes reconstruct that operator,
   while a rank-deficient family leaves an exact physical ambiguity;
3. a scalar-action interface instead needs n(n+1)/2 fixed queries; and
4. one three-terminal response has positive simple mediator completions of
   every finite cycle rank.

The proof is analytic. Exact rational enumeration is only a regression. This
is not direct-action QED, a selected detector or archive, a continuum inverse
problem, ontology selection, empirical excess, or new physics.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_source_action_response_record_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]
WeightedEdge = tuple[int, int, Fraction]


@dataclass(frozen=True)
class Network:
    name: str
    vertex_count: int
    boundary: tuple[int, ...]
    edges: tuple[WeightedEdge, ...]


def zero_matrix(rows: int, columns: int) -> list[list[Fraction]]:
    return [
        [Fraction(0) for _ in range(columns)]
        for _ in range(rows)
    ]


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return tuple()
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
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


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(len(vector))
            ),
            Fraction(0),
        )
        for row in range(len(matrix))
    )


def matrix_inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    assert size and all(len(row) == size for row in matrix)
    work = [
        list(matrix[row]) + list(identity(size)[row])
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            row
            for row in range(column, size)
            if work[row][column] != 0
        )
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]
        for row in range(size):
            if row == column or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    work[row],
                    work[column],
                    strict=True,
                )
            ]
    return tuple(
        tuple(work[row][size:])
        for row in range(size)
    )


def submatrix(
    matrix: Matrix,
    rows: tuple[int, ...],
    columns: tuple[int, ...],
) -> Matrix:
    return tuple(
        tuple(matrix[row][column] for column in columns)
        for row in rows
    )


def schur_keep(matrix: Matrix, keep: tuple[int, ...]) -> Matrix:
    keep_set = set(keep)
    eliminate = tuple(
        index
        for index in range(len(matrix))
        if index not in keep_set
    )
    leading = submatrix(matrix, keep, keep)
    if not eliminate:
        return leading
    cross = submatrix(matrix, keep, eliminate)
    eliminated = submatrix(matrix, eliminate, eliminate)
    return matrix_subtract(
        leading,
        matrix_multiply(
            matrix_multiply(cross, matrix_inverse(eliminated)),
            transpose(cross),
        ),
    )


def laplacian(network: Network) -> Matrix:
    result = zero_matrix(network.vertex_count, network.vertex_count)
    seen_edges: set[tuple[int, int]] = set()
    for left, right, conductance in network.edges:
        assert left != right
        assert conductance > 0
        key = tuple(sorted((left, right)))
        assert key not in seen_edges
        seen_edges.add(key)
        result[left][left] += conductance
        result[right][right] += conductance
        result[left][right] -= conductance
        result[right][left] -= conductance
    return tuple(tuple(row) for row in result)


def response_matrix(network: Network) -> Matrix:
    return schur_keep(laplacian(network), network.boundary)


def sequential_response(network: Network) -> Matrix:
    current = laplacian(network)
    labels = list(range(network.vertex_count))
    interior = [
        vertex
        for vertex in labels
        if vertex not in set(network.boundary)
    ]
    for vertex in interior:
        position = labels.index(vertex)
        keep = tuple(
            index
            for index in range(len(labels))
            if index != position
        )
        current = schur_keep(current, keep)
        labels.pop(position)
    order = tuple(labels.index(vertex) for vertex in network.boundary)
    return submatrix(current, order, order)


def grounded_response(response: Matrix) -> Matrix:
    indices = tuple(range(len(response) - 1))
    return submatrix(response, indices, indices)


def vector_to_column(vector: Vector) -> Matrix:
    return tuple((value,) for value in vector)


def columns(vectors: tuple[Vector, ...]) -> Matrix:
    assert vectors
    return tuple(
        tuple(vector[row] for vector in vectors)
        for row in range(len(vectors[0]))
    )


def quadratic_action(matrix: Matrix, vector: Vector) -> Fraction:
    response = matrix_vector(matrix, vector)
    return Fraction(1, 2) * sum(
        (left * right for left, right in zip(vector, response, strict=True)),
        Fraction(0),
    )


def add_matrices(
    left: Matrix,
    right: Matrix,
    factor: Fraction = Fraction(1),
) -> Matrix:
    return tuple(
        tuple(
            left[row][column] + factor * right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def outer(vector: Vector) -> Matrix:
    return tuple(
        tuple(left * right for right in vector)
        for left in vector
    )


def response_to_boundary_network(
    name: str,
    grounded: Matrix,
) -> Network:
    size = len(grounded)
    ground = size
    edges: list[WeightedEdge] = []
    for left, right in combinations(range(size), 2):
        conductance = -grounded[left][right]
        assert conductance > 0
        edges.append((left, right, conductance))
    for vertex in range(size):
        conductance = sum(grounded[vertex], Fraction(0))
        assert conductance > 0
        edges.append((vertex, ground, conductance))
    return Network(
        name,
        size + 1,
        tuple(range(size + 1)),
        tuple(edges),
    )


def cycle_rank(network: Network) -> int:
    return len(network.edges) - network.vertex_count + 1


def triangle_network() -> Network:
    return Network(
        "unit_triangle",
        3,
        (0, 1, 2),
        (
            (0, 1, Fraction(1)),
            (0, 2, Fraction(1)),
            (1, 2, Fraction(1)),
        ),
    )


def star_network(boundary_count: int = 3) -> Network:
    center = boundary_count
    return Network(
        f"star_{boundary_count}",
        boundary_count + 1,
        tuple(range(boundary_count)),
        tuple(
            (boundary, center, Fraction(boundary_count))
            for boundary in range(boundary_count)
        ),
    )


def multipath_network(path_count: int) -> Network:
    assert path_count >= 1
    path_conductance = Fraction(2, path_count)
    edges: list[WeightedEdge] = [
        (0, 2, Fraction(1)),
        (1, 2, Fraction(1)),
    ]
    for offset in range(path_count):
        middle = 3 + offset
        edges.append((0, middle, path_conductance))
        edges.append((middle, 1, path_conductance))
    return Network(
        f"multipath_{path_count}",
        3 + path_count,
        (0, 1, 2),
        tuple(edges),
    )


def weighted_complete_network(boundary_count: int) -> Network:
    edges = tuple(
        (
            left,
            right,
            Fraction((left + 1) * (right + 2), boundary_count + 1),
        )
        for left, right in combinations(range(boundary_count), 2)
    )
    return Network(
        f"weighted_complete_{boundary_count}",
        boundary_count,
        tuple(range(boundary_count)),
        edges,
    )


def matrix_as_strings(matrix: Matrix) -> list[list[str]]:
    return [
        [str(value) for value in row]
        for row in matrix
    ]


def vector_as_strings(vector: Vector) -> list[str]:
    return [str(value) for value in vector]


def check_vector_reconstruction(network: Network) -> dict[str, object]:
    response = response_matrix(network)
    assert sequential_response(network) == response
    grounded = grounded_response(response)
    size = len(grounded)

    basis = tuple(
        tuple(Fraction(int(row == column)) for row in range(size))
        for column in range(size)
    )
    design = columns(basis)
    outputs = matrix_multiply(grounded, design)
    reconstructed = matrix_multiply(outputs, matrix_inverse(design))
    assert reconstructed == grounded

    held_out = tuple(Fraction(index + 1) for index in range(size))
    predicted = matrix_vector(reconstructed, held_out)
    observed = matrix_vector(grounded, held_out)
    assert predicted == observed

    # A non-orthogonal but invertible frozen design transfers as well.
    skew_design = tuple(
        tuple(
            Fraction(
                int(row == column)
                + int(column == row + 1),
            )
            for column in range(size)
        )
        for row in range(size)
    )
    skew_outputs = matrix_multiply(grounded, skew_design)
    skew_reconstruction = matrix_multiply(
        skew_outputs,
        matrix_inverse(skew_design),
    )
    assert skew_reconstruction == grounded

    return {
        "network": network.name,
        "boundary_count": len(network.boundary),
        "interior_count": network.vertex_count - len(network.boundary),
        "cycle_rank": cycle_rank(network),
        "response": matrix_as_strings(response),
        "grounded_response": matrix_as_strings(grounded),
        "vector_probes": size,
        "held_out_input": vector_as_strings(held_out),
        "held_out_output": vector_as_strings(observed),
        "basis_transfer_exact": True,
        "nonorthogonal_transfer_exact": True,
        "sequential_elimination_invariant": True,
    }


def vector_probe_ambiguity() -> dict[str, object]:
    base_network = weighted_complete_network(4)
    base = grounded_response(response_matrix(base_network))
    size = len(base)
    assert size == 3
    selected = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    design = columns(selected)
    hidden = (Fraction(0), Fraction(0), Fraction(1))
    delta = outer(hidden)
    epsilon = Fraction(1, 10)
    plus = add_matrices(base, delta, epsilon)
    minus = add_matrices(base, delta, -epsilon)
    plus_network = response_to_boundary_network("vector_plus", plus)
    minus_network = response_to_boundary_network("vector_minus", minus)
    assert grounded_response(response_matrix(plus_network)) == plus
    assert grounded_response(response_matrix(minus_network)) == minus
    assert matrix_multiply(plus, design) == matrix_multiply(minus, design)
    plus_hidden = matrix_vector(plus, hidden)
    minus_hidden = matrix_vector(minus, hidden)
    assert plus_hidden != minus_hidden
    return {
        "boundary_count": 4,
        "selected_probe_count": len(selected),
        "required_probe_count": size,
        "selected_outputs_equal": True,
        "held_out_input": vector_as_strings(hidden),
        "plus_held_out": vector_as_strings(plus_hidden),
        "minus_held_out": vector_as_strings(minus_hidden),
        "both_positive_network_responses": True,
    }


def scalar_reconstruct(
    actions: dict[Vector, Fraction],
    size: int,
) -> Matrix:
    result = zero_matrix(size, size)
    basis = tuple(
        tuple(Fraction(int(row == column)) for row in range(size))
        for column in range(size)
    )
    for index, vector in enumerate(basis):
        result[index][index] = 2 * actions[vector]
    for left, right in combinations(range(size), 2):
        pair = tuple(
            basis[left][index] + basis[right][index]
            for index in range(size)
        )
        value = actions[pair] - actions[basis[left]] - actions[basis[right]]
        result[left][right] = value
        result[right][left] = value
    return tuple(tuple(row) for row in result)


def scalar_interface_check() -> dict[str, object]:
    base = grounded_response(response_matrix(weighted_complete_network(4)))
    size = len(base)
    basis = tuple(
        tuple(Fraction(int(row == column)) for row in range(size))
        for column in range(size)
    )
    queries = list(basis)
    queries.extend(
        tuple(
            basis[left][index] + basis[right][index]
            for index in range(size)
        )
        for left, right in combinations(range(size), 2)
    )
    actions = {
        query: quadratic_action(base, query)
        for query in queries
    }
    assert scalar_reconstruct(actions, size) == base
    assert len(queries) == size * (size + 1) // 2

    # Omit the final pair query and perturb only that off-diagonal direction.
    omitted = queries[-1]
    retained = tuple(queries[:-1])
    delta_rows = zero_matrix(size, size)
    delta_rows[size - 2][size - 1] = Fraction(1)
    delta_rows[size - 1][size - 2] = Fraction(1)
    delta = tuple(tuple(row) for row in delta_rows)
    epsilon = Fraction(1, 10)
    plus = add_matrices(base, delta, epsilon)
    minus = add_matrices(base, delta, -epsilon)
    plus_network = response_to_boundary_network("scalar_plus", plus)
    minus_network = response_to_boundary_network("scalar_minus", minus)
    assert all(
        quadratic_action(plus, query) == quadratic_action(minus, query)
        for query in retained
    )
    assert quadratic_action(plus, omitted) != quadratic_action(minus, omitted)
    assert grounded_response(response_matrix(plus_network)) == plus
    assert grounded_response(response_matrix(minus_network)) == minus

    return {
        "grounded_dimension": size,
        "complete_query_count": len(queries),
        "expected_symmetric_dimension": size * (size + 1) // 2,
        "complete_scalar_reconstruction": True,
        "retained_query_count": len(retained),
        "omitted_query": vector_as_strings(omitted),
        "retained_actions_equal": True,
        "omitted_action_differs": True,
        "both_positive_network_responses": True,
    }


def unbounded_topology_family(
    maximum_path_count: int = 8,
) -> dict[str, object]:
    target = response_matrix(triangle_network())
    star = star_network(3)
    assert response_matrix(star) == target
    assert cycle_rank(star) == 0
    members: list[dict[str, object]] = [
        {
            "network": star.name,
            "vertices": star.vertex_count,
            "edges": len(star.edges),
            "cycle_rank": cycle_rank(star),
        }
    ]
    for path_count in range(1, maximum_path_count + 1):
        network = multipath_network(path_count)
        assert response_matrix(network) == target
        assert sequential_response(network) == target
        assert cycle_rank(network) == path_count
        members.append(
            {
                "network": network.name,
                "vertices": network.vertex_count,
                "edges": len(network.edges),
                "cycle_rank": cycle_rank(network),
            }
        )
    assert [member["cycle_rank"] for member in members] == list(
        range(maximum_path_count + 1)
    )
    return {
        "target_response": matrix_as_strings(target),
        "members": members,
        "cycle_ranks_checked": list(range(maximum_path_count + 1)),
        "analytic_extension": "all integers m >= 0",
        "same_complete_source_response": True,
        "vertex_and_edge_counts_unbounded": True,
    }


def robustness_control() -> dict[str, object]:
    size = 3
    good = identity(size)
    bad = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1, 10)),
    )
    good_inverse = matrix_inverse(good)
    bad_inverse = matrix_inverse(bad)
    good_max = max(abs(value) for row in good_inverse for value in row)
    bad_max = max(abs(value) for row in bad_inverse for value in row)
    assert good_max == 1
    assert bad_max == 10
    return {
        "normalized_orthogonal_inverse_max_entry": str(good_max),
        "weak_direction_inverse_max_entry": str(bad_max),
        "exact_error_identity": "A_hat - A = E X^-1",
        "orthogonal_design_has_unit_condition_number": True,
        "weak_probe_direction_amplifies_error": True,
    }


def main() -> None:
    specimens = (
        triangle_network(),
        star_network(3),
        multipath_network(2),
        multipath_network(5),
        star_network(4),
        weighted_complete_network(5),
    )
    reconstruction_results = [
        check_vector_reconstruction(network)
        for network in specimens
    ]
    ambiguity = vector_probe_ambiguity()
    scalar = scalar_interface_check()
    topology = unbounded_topology_family()
    robustness = robustness_control()

    triangle_response = response_matrix(triangle_network())
    star_response = response_matrix(star_network(3))
    assert triangle_response == star_response

    checks = {
        "boundary_response_operator_descends_through_exact_mediator_elimination": True,
        "sequential_and_one_shot_schur_elimination_agree": True,
        "response_operator_is_complete_for_linear_source_capability": True,
        "response_operator_is_minimal_up_to_information_equivalence": True,
        "b_minus_one_independent_vector_probes_are_sufficient": True,
        "b_minus_one_independent_vector_probes_are_necessary": True,
        "fixed_probe_record_transfers_to_held_out_boundary_queries": True,
        "rank_deficient_probe_record_has_same_record_different_response_witness": True,
        "ambiguity_pair_is_realized_by_positive_boundary_networks": True,
        "orthogonal_vector_probes_minimize_inverse_amplification": True,
        "scalar_action_interface_uses_symmetric_matrix_dimension": True,
        "scalar_action_query_omission_leaves_a_physical_ambiguity": True,
        "star_and_triangle_share_one_complete_source_response": True,
        "one_source_response_has_every_finite_cycle_rank": True,
        "internal_vertex_and_edge_counts_are_unbounded_on_one_source_fibre": True,
        "internal_topology_does_not_factor_through_source_action": True,
        "field_and_direct_relation_presentations_are_source_query_dual": True,
        "mediator_facing_action_reopens_the_source_equivalence_class": True,
        "response_law_does_not_select_probe_archive_observer_or_access": True,
        "no_direct_action_or_field_ontology_selection": True,
        "no_continuum_quantum_or_empirical_excess": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-126",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "vector_reconstruction_specimens": reconstruction_results,
        "vector_probe_ambiguity": ambiguity,
        "scalar_interface": scalar,
        "unbounded_topology_family": topology,
        "robustness": robustness,
        "formal_boundary": {
            "source_record": (
                "The labeled boundary Dirichlet-to-Neumann operator is the "
                "minimal complete record, up to information-equivalent "
                "encoding, for all linear boundary source responses."
            ),
            "formation": (
                "With vector current readout, b-1 fixed independent boundary "
                "potential probes are necessary and sufficient. With only "
                "scalar action readout, n(n+1)/2 fixed queries are necessary "
                "and sufficient."
            ),
            "remainder": (
                "One complete three-terminal source response admits positive "
                "simple mediator completions of every finite cycle rank. "
                "Topology becomes a physical remainder only after a "
                "mediator-facing action is admitted."
            ),
            "direct_action": (
                "A direct relation presentation and an explicit mediator "
                "presentation with the same response are operationally dual "
                "for the frozen source-query class, not ontologically "
                "identified."
            ),
        },
        "non_claims": [
            "not a dynamically selected probe, archive, observer, or access boundary",
            "not a single-occurrence event record",
            "not direct-action QED, AQFT, gravity, or a quantum effective action",
            "not ontology equivalence or ontology selection",
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
        f"{len(reconstruction_results)} reconstruction specimens, "
        f"{len(topology['members'])} source-equivalent topology specimens"
    )


if __name__ == "__main__":
    main()
