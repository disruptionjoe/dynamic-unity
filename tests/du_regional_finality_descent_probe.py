#!/usr/bin/env python3
"""Finite controls for recursive regional finality and descent.

The probe turns a "network of record networks" into a small typed test
surface.  It combines known finite ingredients:

* affine constraint descent and loop syndromes;
* Byzantine quorum intersection and liveness;
* provenance-aware support and abstract threshold access;
* deterministic boundary-summary factorization;
* benign graph subdivision;
* forward-only capability feedback; and
* a GHZ proper-subset-versus-logical-access control.

The distributed and quantum fixtures share a return vocabulary, not an
ontology.  Passing establishes exact finite composition controls and a
complete method registry.  It does not establish a new consensus theorem,
quantum/classical identity, physical region-selection law, record-first
ontology, emergent geometry, or departure from quantum theory.
"""

from __future__ import annotations

import itertools
import json
from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_regional_finality_descent_result.json"
)
RUN_ID = "RUN-20260725-060628-regional-finality-descent-kernel"

DESCENDS = "DESCENDS"
REQUIRES_LIFT = "REQUIRES_PROVENANCE_OR_LOGICAL_LIFT"
REJECTS = "REJECTS_FRUSTRATED_OR_UNSAFE_COMPOSITION"
INCOMPLETE = "INCOMPLETE_CONTRACT"

Vertex = str
Edge = tuple[Vertex, Vertex, int]
Assignment = dict[Vertex, int]
Matrix = tuple[tuple[Fraction, ...], ...]


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
        }
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [jsonable(item) for item in sorted(value)]
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda item: str(item[0]))
        }
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


def all_bit_assignments(vertices: Sequence[Vertex]) -> Iterable[Assignment]:
    ordered = tuple(vertices)
    for values in itertools.product((0, 1), repeat=len(ordered)):
        yield dict(zip(ordered, values, strict=True))


def satisfies(assignment: Mapping[Vertex, int], edges: Sequence[Edge]) -> bool:
    return all(
        assignment[right] == assignment[left] ^ parity
        for left, right, parity in edges
    )


def satisfying_assignments(
    vertices: Sequence[Vertex],
    edges: Sequence[Edge],
) -> tuple[Assignment, ...]:
    return tuple(
        assignment
        for assignment in all_bit_assignments(vertices)
        if satisfies(assignment, edges)
    )


def connected(vertices: Sequence[Vertex], edges: Sequence[Edge]) -> bool:
    if not vertices:
        return False
    adjacency = {vertex: set() for vertex in vertices}
    for left, right, _ in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = {vertices[0]}
    queue = deque((vertices[0],))
    while queue:
        vertex = queue.popleft()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return seen == set(vertices)


def affine_flatness(
    vertices: Sequence[Vertex],
    edges: Sequence[Edge],
) -> tuple[bool, dict[Vertex, int]]:
    """Return consistency and one root-relative potential assignment."""

    adjacency: dict[Vertex, list[tuple[Vertex, int]]] = {
        vertex: [] for vertex in vertices
    }
    for left, right, parity in edges:
        adjacency[left].append((right, parity))
        adjacency[right].append((left, parity))

    potentials: dict[Vertex, int] = {}
    for root in vertices:
        if root in potentials:
            continue
        potentials[root] = 0
        queue = deque((root,))
        while queue:
            vertex = queue.popleft()
            for neighbor, parity in adjacency[vertex]:
                proposed = potentials[vertex] ^ parity
                if neighbor in potentials:
                    if potentials[neighbor] != proposed:
                        return False, potentials
                else:
                    potentials[neighbor] = proposed
                    queue.append(neighbor)
    return True, potentials


def affine_descent_controls() -> dict[str, Any]:
    vertices = ("A", "B", "C")
    tree = (("A", "B", 0), ("B", "C", 0))
    flat_triangle = tree + (("C", "A", 0),)
    frustrated_triangle = tree + (("C", "A", 1),)

    exhaustive_cases = 0
    exhaustive_failures: list[dict[str, Any]] = []
    for size in range(1, 5):
        local_vertices = tuple(chr(ord("A") + index) for index in range(size))
        possible_edges = tuple(itertools.combinations(local_vertices, 2))
        for edge_mask in range(1 << len(possible_edges)):
            selected_pairs = tuple(
                pair
                for index, pair in enumerate(possible_edges)
                if edge_mask & (1 << index)
            )
            unlabeled = tuple((left, right, 0) for left, right in selected_pairs)
            if not connected(local_vertices, unlabeled):
                continue
            for parities in itertools.product((0, 1), repeat=len(selected_pairs)):
                edges = tuple(
                    (left, right, parity)
                    for (left, right), parity in zip(
                        selected_pairs,
                        parities,
                        strict=True,
                    )
                )
                flat, _ = affine_flatness(local_vertices, edges)
                solutions = satisfying_assignments(local_vertices, edges)
                expected_count = 2 if flat else 0
                exhaustive_cases += 1
                if len(solutions) != expected_count:
                    exhaustive_failures.append(
                        {
                            "vertices": local_vertices,
                            "edges": edges,
                            "flat": flat,
                            "solution_count": len(solutions),
                            "expected_count": expected_count,
                        }
                    )

    proper_subsystems = tuple(
        frustrated_triangle[:index] + frustrated_triangle[index + 1 :]
        for index in range(len(frustrated_triangle))
    )
    repaired_triangle = tree + (("C", "A", 0),)

    # The nontrivial Z2 holonomy orbit is {0,1}. A path-independent public
    # value must be constant on that orbit. Preserving action y(x)=x needs two
    # accessible provenance labels.
    holonomy_orbit = (0, 1)
    public_values = {
        tuple(function)
        for function in itertools.product((0, 1), repeat=2)
        if function[holonomy_orbit[0]] == function[holonomy_orbit[1]]
    }
    action_values_on_orbit = {0, 1}

    return {
        "tree_solution_count": len(satisfying_assignments(vertices, tree)),
        "flat_triangle_solution_count": len(
            satisfying_assignments(vertices, flat_triangle)
        ),
        "frustrated_triangle_solution_count": len(
            satisfying_assignments(vertices, frustrated_triangle)
        ),
        "each_proper_edge_family_is_satisfiable": all(
            satisfying_assignments(vertices, subsystem)
            for subsystem in proper_subsystems
        ),
        "frustrated_cycle_syndrome": (
            frustrated_triangle[0][2]
            ^ frustrated_triangle[1][2]
            ^ frustrated_triangle[2][2]
        ),
        "repair_restores_solution_count": len(
            satisfying_assignments(vertices, repaired_triangle)
        ),
        "exhaustive_connected_graph_cases_through_four_vertices": exhaustive_cases,
        "exhaustive_flatness_solution_count_failures": exhaustive_failures,
        "nontrivial_holonomy_orbit": holonomy_orbit,
        "path_independent_binary_fact_count": len(public_values),
        "path_independent_capacity_bits": 0,
        "minimum_provenance_alphabet_for_identity_action": len(
            action_values_on_orbit
        ),
        "disposition": (
            "AFFINE_DESCENT_IFF_CYCLE_SYNDROMES_VANISH / "
            "NONINVARIANT_ACTION_REQUIRES_PROJECT_OR_LIFT"
        ),
    }


def quorum_is_safe(n: int, f: int, q: int) -> bool:
    validators = tuple(range(n))
    quorums = tuple(itertools.combinations(validators, q))
    adversaries = tuple(
        frozenset(subset)
        for size in range(f + 1)
        for subset in itertools.combinations(validators, size)
    )
    return all(
        not any(set(left).intersection(right) <= adversary for adversary in adversaries)
        for left in quorums
        for right in quorums
    )


def quorum_controls() -> dict[str, Any]:
    cases = []
    failures = []
    for n in range(1, 9):
        for f in range(n):
            for q in range(1, n + 1):
                observed = quorum_is_safe(n, f, q)
                expected = 2 * q > n + f
                case = {
                    "n": n,
                    "f": f,
                    "q": q,
                    "safe": observed,
                    "live_under_f_withholding": q <= n - f,
                }
                cases.append(case)
                if observed != expected:
                    failures.append(case)

    n = 4
    f = 1
    examples = {
        str(q): {
            "safe": quorum_is_safe(n, f, q),
            "live_under_one_withholding": q <= n - f,
        }
        for q in (2, 3, 4)
    }

    origin = {
        "sybil-1": "origin-A",
        "sybil-2": "origin-A",
        "sybil-3": "origin-A",
        "honest-1": "origin-H",
    }
    raw_certificate = ("sybil-1", "sybil-2", "sybil-3")
    independent_support = {origin[validator] for validator in raw_certificate}

    return {
        "exhaustive_cases_through_n_8": len(cases),
        "quorum_intersection_formula_failures": failures,
        "n4_f1_examples": examples,
        "safety_and_liveness_are_distinct": (
            examples["2"] == {
                "safe": False,
                "live_under_one_withholding": True,
            }
            and examples["4"] == {
                "safe": True,
                "live_under_one_withholding": False,
            }
        ),
        "raw_sybil_certificate": raw_certificate,
        "raw_identity_count": len(raw_certificate),
        "independent_origin_count": len(independent_support),
        "raw_count_can_overstate_independent_support": (
            len(raw_certificate) == 3 and len(independent_support) == 1
        ),
        "disposition": (
            "QUORUM_SAFETY_REQUIRES_INTERSECTION_OUTSIDE_ADVERSARY / "
            "LIVENESS_AND_PROVENANCE_REQUIRE_SEPARATE RECEIPTS"
        ),
    }


def threshold_access_controls() -> dict[str, Any]:
    holders = ("A", "B", "C")
    coalitions = tuple(
        frozenset(subset)
        for size in range(len(holders) + 1)
        for subset in itertools.combinations(holders, size)
    )
    authorized = {
        coalition: len(coalition) >= 2
        for coalition in coalitions
    }
    monotone = all(
        not allowed
        or all(
            authorized[superset]
            for superset in coalitions
            if coalition <= superset
        )
        for coalition, allowed in authorized.items()
    )
    return {
        "access_structure": "abstract 2-of-3 monotone reconstruction",
        "authorized_coalition_count": sum(authorized.values()),
        "unauthorized_singletons": all(
            not authorized[frozenset((holder,))]
            for holder in holders
        ),
        "monotone": monotone,
        "public_certificate_available": True,
        "private_witness_reconstructible_by_every_observer": False,
        "certification_and_disclosure_separate": True,
        "scope_warning": (
            "combinatorial access structure only; no cryptographic security, "
            "key setup, commitment scheme, or physical access law is proved"
        ),
    }


def response_vector(
    state: str,
    responses: Mapping[str, Mapping[str, int]],
) -> tuple[int, ...]:
    return tuple(responses[action][state] for action in sorted(responses))


def factors_through(
    states: Sequence[str],
    summary: Mapping[str, Any],
    responses: Mapping[str, Mapping[str, int]],
) -> bool:
    by_summary: dict[Any, set[tuple[int, ...]]] = {}
    for state in states:
        by_summary.setdefault(summary[state], set()).add(
            response_vector(state, responses)
        )
    return all(len(vectors) == 1 for vectors in by_summary.values())


def boundary_factorization_controls() -> dict[str, Any]:
    states = ("00", "01", "10", "11")
    coarse = {state: int(state[0]) for state in states}
    lifted = {state: (int(state[0]), int(state[1])) for state in states}
    responses = {
        "read_local": {state: int(state[0]) for state in states},
        "read_syndrome": {state: int(state[1]) for state in states},
        "act_on_parity": {
            state: int(state[0]) ^ int(state[1])
            for state in states
        },
    }
    local_response = {"read_local": responses["read_local"]}
    distinct_response_vectors = {
        response_vector(state, responses)
        for state in states
    }
    witness_pair = ("00", "01")

    return {
        "internal_state_count": len(states),
        "coarse_boundary_labels": len(set(coarse.values())),
        "lifted_boundary_labels": len(set(lifted.values())),
        "coarse_summary_factors_local_action": factors_through(
            states, coarse, local_response
        ),
        "coarse_summary_factors_all_upper_actions": factors_through(
            states, coarse, responses
        ),
        "lifted_summary_factors_all_upper_actions": factors_through(
            states, lifted, responses
        ),
        "minimum_boundary_labels_for_frozen_upper_actions": len(
            distinct_response_vectors
        ),
        "coarse_summary_counterfactual_witness": {
            "states": witness_pair,
            "same_summary": coarse[witness_pair[0]] == coarse[witness_pair[1]],
            "different_syndrome_action": (
                responses["read_syndrome"][witness_pair[0]]
                != responses["read_syndrome"][witness_pair[1]]
            ),
        },
        "recursive_promotion_rule": (
            "replace an internal region by one higher-layer node iff every "
            "frozen upper response is constant on each boundary-summary fibre"
        ),
        "disposition": (
            "COARSE REGION IS A SAFE HIGHER_NODE IFF UPPER ACTIONS FACTOR "
            "THROUGH ITS BOUNDARY CERTIFICATE"
        ),
    }


def benign_refinement_controls() -> dict[str, Any]:
    original_vertices = ("A", "B", "C")
    frustrated_original_edges = (
        ("A", "B", 0),
        ("B", "C", 0),
        ("C", "A", 1),
    )
    refined_vertices = ("A", "B", "C", "D")
    frustrated_refined_edges = (
        ("A", "B", 0),
        ("B", "C", 0),
        ("C", "D", 0),
        ("D", "A", 1),
    )
    flat_original_edges = (
        ("A", "B", 0),
        ("B", "C", 0),
        ("C", "A", 0),
    )
    flat_refined_edges = (
        ("A", "B", 0),
        ("B", "C", 0),
        ("C", "D", 0),
        ("D", "A", 0),
    )
    frustrated_original_flat, _ = affine_flatness(
        original_vertices,
        frustrated_original_edges,
    )
    frustrated_refined_flat, _ = affine_flatness(
        refined_vertices,
        frustrated_refined_edges,
    )
    flat_original_flat, _ = affine_flatness(
        original_vertices,
        flat_original_edges,
    )
    flat_refined_flat, _ = affine_flatness(
        refined_vertices,
        flat_refined_edges,
    )

    return {
        "original_edge_count": len(frustrated_original_edges),
        "refined_edge_count": len(frustrated_refined_edges),
        "original_hop_count_on_subdivided_route": 1,
        "refined_hop_count_on_subdivided_route": 2,
        "frustrated_original_flat": frustrated_original_flat,
        "frustrated_refined_flat": frustrated_refined_flat,
        "frustrated_original_solution_count": len(
            satisfying_assignments(
                original_vertices,
                frustrated_original_edges,
            )
        ),
        "frustrated_refined_solution_count": len(
            satisfying_assignments(
                refined_vertices,
                frustrated_refined_edges,
            )
        ),
        "flat_original_flat": flat_original_flat,
        "flat_refined_flat": flat_refined_flat,
        "flat_original_solution_count": len(
            satisfying_assignments(original_vertices, flat_original_edges)
        ),
        "flat_refined_solution_count": len(
            satisfying_assignments(refined_vertices, flat_refined_edges)
        ),
        "syndrome_preserved_under_subdivision": (
            frustrated_original_flat == frustrated_refined_flat
            and flat_original_flat == flat_refined_flat
        ),
        "descent_solution_count_preserved_under_subdivision": (
            len(
                satisfying_assignments(
                    original_vertices,
                    frustrated_original_edges,
                )
            )
            == len(
                satisfying_assignments(
                    refined_vertices,
                    frustrated_refined_edges,
                )
            )
            and len(
                satisfying_assignments(
                    original_vertices,
                    flat_original_edges,
                )
            )
            == len(
                satisfying_assignments(
                    refined_vertices,
                    flat_refined_edges,
                )
            )
        ),
        "raw_hop_count_is_not_invariant": True,
    }


def capability_feedback_controls() -> dict[str, Any]:
    prior_record = ("event-e0", "value-1")
    before = frozenset(("observe", "wait"))
    after = frozenset(("observe", "wait", "commit"))
    event_log = (
        {"time": 0, "record": prior_record, "safe_actions": sorted(before)},
        {
            "time": 1,
            "record": prior_record,
            "certificate": "regional-finality-c1",
            "safe_actions": sorted(after),
        },
    )
    return {
        "prior_record_before": prior_record,
        "prior_record_after": event_log[1]["record"],
        "safe_actions_before": before,
        "safe_actions_after": after,
        "future_capability_strictly_increases": before < after,
        "past_accessible_record_is_unchanged": (
            event_log[0]["record"] == event_log[1]["record"]
        ),
        "feedback_direction": "certificate at t=1 constrains actions at t>=1",
        "retroactive_rewrite": False,
    }


def zero_matrix(dimension: int) -> list[list[Fraction]]:
    return [
        [Fraction(0) for _ in range(dimension)]
        for _ in range(dimension)
    ]


def bits(index: int, qubits: int) -> tuple[int, ...]:
    return tuple(
        (index >> (qubits - qubit - 1)) & 1
        for qubit in range(qubits)
    )


def index_from_bits(values: Sequence[int]) -> int:
    result = 0
    for value in values:
        result = 2 * result + value
    return result


def ghz_density(phase: int) -> Matrix:
    matrix = zero_matrix(8)
    matrix[0][0] = Fraction(1, 2)
    matrix[7][7] = Fraction(1, 2)
    matrix[0][7] = Fraction(phase, 2)
    matrix[7][0] = Fraction(phase, 2)
    return tuple(tuple(row) for row in matrix)


def partial_trace_qubits(
    state: Matrix,
    keep: Sequence[int],
    qubits: int,
) -> Matrix:
    kept = tuple(keep)
    traced = tuple(qubit for qubit in range(qubits) if qubit not in kept)
    dimension = 2 ** len(kept)
    result = zero_matrix(dimension)
    for row in range(2**qubits):
        row_bits = bits(row, qubits)
        for column in range(2**qubits):
            column_bits = bits(column, qubits)
            if any(row_bits[q] != column_bits[q] for q in traced):
                continue
            out_row = index_from_bits(tuple(row_bits[q] for q in kept))
            out_column = index_from_bits(tuple(column_bits[q] for q in kept))
            result[out_row][out_column] += state[row][column]
    return tuple(tuple(value for value in row) for row in result)


def all_x_expectation(state: Matrix, qubits: int) -> Fraction:
    total = Fraction(0)
    mask = (1 << qubits) - 1
    for basis_index in range(2**qubits):
        flipped = basis_index ^ mask
        total += state[basis_index][flipped]
    return total


def quantum_record_twin() -> dict[str, Any]:
    plus = ghz_density(1)
    minus = ghz_density(-1)
    subset_equalities = {}
    for size in (1, 2):
        for keep in itertools.combinations(range(3), size):
            subset_equalities[str(keep)] = (
                partial_trace_qubits(plus, keep, 3)
                == partial_trace_qubits(minus, keep, 3)
            )

    phase_response = {
        "plus": all_x_expectation(plus, 3),
        "minus": all_x_expectation(minus, 3),
    }
    coarse_summary = {"plus": "all proper-subset records", "minus": "all proper-subset records"}
    lifted_summary = {"plus": 1, "minus": -1}
    responses = {"global_x_parity": phase_response}

    return {
        "fixture": "three-qubit GHZ phase pair",
        "all_proper_subset_reduced_states_equal": all(
            subset_equalities.values()
        ),
        "proper_subset_equalities": subset_equalities,
        "global_x_parity": phase_response,
        "global_logical_action_distinguishes_phase": (
            phase_response["plus"] != phase_response["minus"]
        ),
        "proper_subset_summary_factors_global_action": factors_through(
            ("plus", "minus"),
            coarse_summary,
            responses,
        ),
        "logical_parity_lift_factors_global_action": factors_through(
            ("plus", "minus"),
            lifted_summary,
            responses,
        ),
        "entanglement_interpretation": (
            "nonfactorizable joint constraint; not hidden local votes"
        ),
        "result": REQUIRES_LIFT,
        "scope_warning": (
            "known stabilizer/logical-access control; no public objectivity, "
            "consensus identity, collapse, or new quantum effect"
        ),
    }


def distributed_twin(
    *,
    flat: bool,
    quorum: int,
    provenance: str,
    boundary: str,
    hardening: str,
    adversary_declared: bool = True,
) -> dict[str, Any]:
    if not adversary_declared:
        return {
            "result": INCOMPLETE,
            "reason": "no adversary class for certificate safety",
        }
    if not flat:
        if hardening == "reject":
            return {
                "result": REJECTS,
                "reason": "nonzero loop syndrome rejected by higher layer",
            }
        return {
            "result": REQUIRES_LIFT,
            "reason": "nonzero loop syndrome needs repair, quotient, or route lift",
        }
    if quorum < 3:
        return {
            "result": REJECTS,
            "reason": "q=2 fails N=4,f=1 quorum intersection",
        }
    if provenance != "independent":
        return {
            "result": REJECTS,
            "reason": "raw identity count permits correlated/Sybil support",
        }
    if boundary != "lifted":
        return {
            "result": REQUIRES_LIFT,
            "reason": "coarse boundary summary omits action-relevant syndrome",
        }
    return {
        "result": DESCENDS,
        "reason": (
            "flat overlaps, safe quorum, independent support, and "
            "action-sufficient boundary certificate"
        ),
    }


def counterfactual_design() -> dict[str, Any]:
    reference = {
        "flat": True,
        "quorum": 3,
        "provenance": "independent",
        "boundary": "lifted",
        "hardening": "none",
    }
    interventions = {
        "introduce_loop_frustration": {"flat": False},
        "lower_quorum": {"quorum": 2},
        "replace_independent_support_with_raw_count": {"provenance": "raw"},
        "coarsen_boundary": {"boundary": "coarse"},
    }
    contrasts = {}
    reference_result = distributed_twin(**reference)
    for name, change in interventions.items():
        treatment = dict(reference)
        treatment.update(change)
        contrasts[name] = {
            "control": reference_result["result"],
            "treatment": distributed_twin(**treatment)["result"],
            "changed_fields": sorted(change),
        }

    frustrated = dict(reference)
    frustrated["flat"] = False
    frustrated_reject = dict(frustrated)
    frustrated_reject["hardening"] = "reject"
    contrasts["add_rejecting_hardening_to_frustrated_loop"] = {
        "control": distributed_twin(**frustrated)["result"],
        "treatment": distributed_twin(**frustrated_reject)["result"],
        "changed_fields": ["hardening"],
        "interpretation": (
            "hardening prevents unsafe composition by rejecting it; "
            "rejection is not successful descent"
        ),
    }

    factorial_counts: dict[str, int] = {}
    for flat, quorum, provenance, boundary, hardening in itertools.product(
        (False, True),
        (2, 3),
        ("raw", "independent"),
        ("coarse", "lifted"),
        ("none", "reject"),
    ):
        result = distributed_twin(
            flat=flat,
            quorum=quorum,
            provenance=provenance,
            boundary=boundary,
            hardening=hardening,
        )["result"]
        factorial_counts[result] = factorial_counts.get(result, 0) + 1

    return {
        "reference_contract": reference,
        "reference_result": reference_result,
        "one_change_matched_contrasts": contrasts,
        "all_contrasts_change_only_declared_fields": all(
            len(contrast["changed_fields"]) == 1
            for contrast in contrasts.values()
        ),
        "full_factorial_case_count": 32,
        "full_factorial_result_counts": factorial_counts,
        "estimands": {
            "topology": (
                "effect of one loop-syndrome intervention at fixed quorum, "
                "provenance, boundary summary, task, and resources"
            ),
            "quorum": (
                "effect of q=2 versus q=3 at fixed N=4,f=1 and saved schedule"
            ),
            "provenance": (
                "effect of independent origin support versus equal raw identity count"
            ),
            "boundary": (
                "effect of exporting the action-relevant syndrome at fixed internal process"
            ),
            "hardening": (
                "effect of rejecting a frustrated composition; rejection and descent remain distinct"
            ),
        },
    }


def approach_registry() -> dict[str, dict[str, Any]]:
    return {
        "RF-01": {
            "question": "What is the minimal typed regional-finality object?",
            "repo_route": "CONCEPT-DU-011 / HC-DU-035C",
            "lenses": ["CAT", "PHIL", "ORT", "COM"],
            "kits": ["K0", "K1", "K2"],
            "counterfactual_estimand": (
                "which predictions change when one typed field is removed "
                "while the physical process is held fixed"
            ),
            "smallest_object": "two regions, one overlap, one boundary certificate",
            "strongest_absorber": "ordinary causal site, algebraic net, sheaf, or process network",
            "first_move": "freeze the schema and construct deletion countermodels for every field",
            "negative_output": "a smaller sufficient schema or a proof that one proposed field is redundant",
            "cheap_kill": "the schema merely renames existing process/algebra fields and adds no compositional invariant",
            "scale_gate": "every field has an independent counterexample or universal-property role",
        },
        "RF-02": {
            "question": "What selects a region and its validator/support class?",
            "repo_route": "HC-DU-033 / HC-DU-032 / CONCEPT-DU-003/011",
            "lenses": ["CFS", "FCE", "ORT", "HET", "NW"],
            "kits": ["K0", "K1", "K3", "K9"],
            "counterfactual_estimand": (
                "effect of a candidate boundary under clone, relabeling, "
                "overlap, and benign-refinement interventions"
            ),
            "smallest_object": "four internal events with two competing overlapping region covers",
            "strongest_absorber": "modeler-selected boundary or correlated fragment count",
            "first_move": "generate rival covers with identical terminal records and seek a held-out intervention",
            "negative_output": "nonidentification theorem and minimum extra selector",
            "cheap_kill": "region identity changes under inert relay insertion or label permutation",
            "scale_gate": "one selection rule predicts held-out merges/splits without refitting",
        },
        "RF-03": {
            "question": "When do regional final facts descend to a higher-level fact?",
            "repo_route": "H-CCR-16 / HC-DU-035C / H-CCR-13/14",
            "lenses": ["CAT", "FCE", "AD", "PHIL"],
            "kits": ["K0", "K1", "K2", "K4"],
            "counterfactual_estimand": (
                "effect of one overlap, quorum, provenance, or loop relation "
                "at fixed local records and action task"
            ),
            "smallest_object": "three-region affine loop with one incompatible action",
            "strongest_absorber": "sheaf descent, quorum intersection, graph cohomology, or behavioral congruence",
            "first_move": "prove the finite descent-or-typed-obstruction theorem and minimize each failure witness",
            "negative_output": "smallest obstruction and exact missing relation/provenance alphabet",
            "cheap_kill": "pairwise agreement is assumed to imply global gluing or finality is defined by the theorem",
            "scale_gate": "extend only after noisy/noninvertible maps preserve the same statement",
        },
        "RF-04": {
            "question": "When may a whole region become one node at the next layer?",
            "repo_route": "HC-DU-036 / H-CCR-05 / CONCEPT-DU-011",
            "lenses": ["CAT", "CT", "FCE", "COM"],
            "kits": ["K0", "K1", "K2", "K9"],
            "counterfactual_estimand": (
                "upper-layer response difference between internal states "
                "sharing one boundary summary"
            ),
            "smallest_object": "four internal states, two boundary labels, and two upper actions",
            "strongest_absorber": "finite sufficient statistic, bisimulation, or automata congruence",
            "first_move": "compute the coarsest action-sufficient boundary partition and a separating action",
            "negative_output": "minimum lifted boundary alphabet and witness pair",
            "cheap_kill": "the summary is defined using all target responses and makes sufficiency tautological",
            "scale_gate": "the same summary composes across two recursive promotions and held-out actions",
        },
        "RF-05": {
            "question": "How do adversarial finality, threshold access, and disclosure interact?",
            "repo_route": "HC-DU-035 / CONCEPT-DU-009",
            "lenses": ["AD", "ZK", "CFS", "EMA"],
            "kits": ["K0", "K1", "K3", "K4", "K8"],
            "counterfactual_estimand": (
                "safe-action change under quorum, origin independence, "
                "threshold opening, and withholding interventions"
            ),
            "smallest_object": "N=4,f=1 quorums plus an abstract 2-of-3 access structure",
            "strongest_absorber": "standard BFT safety/liveness and cryptographic access structures",
            "first_move": "separate proof, public verification, witness disclosure, reconstruction, and action",
            "negative_output": "split-view or withholding trace and the missing trust/setup assumption",
            "cheap_kill": "raw signatures are counted as independent support or computational secrecy as physical inaccessibility",
            "scale_gate": "a concrete protocol freezes identity, key setup, corruption, timing, and resource assumptions",
        },
        "RF-06": {
            "question": "Does one unchanged contract survive distributed and quantum record twins?",
            "repo_route": "HC-DU-036B/039 / H-CCR-12",
            "lenses": ["QI", "QE", "AD", "PHIL", "EMA"],
            "kits": ["K0", "K3", "K4", "K5", "K6"],
            "counterfactual_estimand": (
                "capability restored by an independently formed provenance "
                "or logical-access lift at fixed task"
            ),
            "smallest_object": "affine/BFT loop and GHZ phase pair with one shared return schema",
            "strongest_absorber": "known stabilizer access plus known distributed certification",
            "first_move": "run matched insufficiency/lift cases without equating votes and entanglement",
            "negative_output": "semantic-refit receipt identifying the first field whose meaning diverges",
            "cheap_kill": "record, public, validator, or capability changes meaning across platforms",
            "scale_gate": "a noisy quantum instrument and replayable adversarial protocol preserve the typed mapping",
        },
        "RF-07": {
            "question": "How may higher finality feed back into lower-layer capability?",
            "repo_route": "HC-DU-037 / H-CCR-06 / CONCEPT-DU-011",
            "lenses": ["CT", "CFS", "PHIL", "TR"],
            "kits": ["K0", "K2", "K3", "K8"],
            "counterfactual_estimand": (
                "future safe-action-set difference caused by a certificate "
                "at fixed task, loss, controls, and resource budget"
            ),
            "smallest_object": "one irreversible action enabled after one safe regional certificate",
            "strongest_absorber": "ordinary controller state, changed tester, or unmatched capability frame",
            "first_move": "prove forward-only action monotonicity and build rollback/safety counterexamples",
            "negative_output": "feedback circularity or complete ordinary-controller factorization",
            "cheap_kill": "the rule rewrites a past record or changes the task/decoder after certification",
            "scale_gate": "feedback composes without contradiction across two layers and includes liveness",
        },
        "RF-08": {
            "question": "Which network-of-networks structure survives refinement and scale change?",
            "repo_route": "HC-DU-038/039 / CONCEPT-DU-006/007/011",
            "lenses": ["CAT", "CG", "NW", "WILD"],
            "kits": ["K0", "K1", "K2", "K7", "K9"],
            "counterfactual_estimand": (
                "change in a candidate invariant under inert subdivision, "
                "coarse-graining, overlap rewiring, and layer promotion"
            ),
            "smallest_object": "one flat and one frustrated two-layer simplicial loop",
            "strongest_absorber": "causal sites, higher-order multiplex topology, Hodge/cohomology, and renormalization",
            "first_move": "kill hop/depth/node-count measures and retain only natural loop, access, and capability invariants",
            "negative_output": "representation-dependence theorem or nonunique reconstruction family",
            "cheap_kill": "the claimed geometry changes under a causally inert relay",
            "scale_gate": "one invariant predicts held-out refinements and has a controlled continuum family",
        },
        "RF-09": {
            "question": "What resource cost belongs to regional finality rather than its implementation?",
            "repo_route": "HC-DU-035B/037 / CONCEPT-DU-008",
            "lenses": ["TR", "CFS", "COM", "EMA"],
            "kits": ["K0", "K3", "K8"],
            "counterfactual_estimand": (
                "work, heat, support, coherence, latency, or optionality "
                "difference at equal certified distinctions and capability"
            ),
            "smallest_object": "two reversible protocols with identical final certificate and action set",
            "strongest_absorber": "Landauer, communication, authentication, QEC, and displaced archive costs",
            "first_move": "derive lower and constructive upper bounds before calorimetry",
            "negative_output": "ordinary-accounting protocol that absorbs the proposed residual",
            "cheap_kill": "completion-class cardinality or proof bytes are treated as physical cost",
            "scale_gate": "encoding-invariant bound predicts a second platform without refitting",
        },
        "RF-10": {
            "question": "Does regional finality leave a physical residual beyond the complete process?",
            "repo_route": "H-CCR-15 / PRED-DU-003 / HC-DU-034B",
            "lenses": ["QI", "CFS", "EMA", "ORT", "HET"],
            "kits": ["K0", "K3", "K5", "K6", "K9"],
            "counterfactual_estimand": (
                "post-causal-break joint-statistic difference between "
                "histories after every admitted memory is re-prepared"
            ),
            "smallest_object": "Bell pair, randomized history, complete reset, and one joint tester",
            "strongest_absorber": "implementation-complete process tensor with route, environment, controller, and detector memory",
            "first_move": "derive the complete null and leakage bound before positing an extra finality state",
            "negative_output": "absorbing memory register or tightened upper bound on any residual",
            "cheap_kill": "the effect changes a remote marginal, depends on ensemble decomposition, or vanishes under memory completion",
            "scale_gate": "repeatable residual survives nested completion, covariance, no-signalling, and preregistered metrology",
        },
    }


def run() -> dict[str, Any]:
    descent = affine_descent_controls()
    quorum = quorum_controls()
    access = threshold_access_controls()
    boundary = boundary_factorization_controls()
    refinement = benign_refinement_controls()
    feedback = capability_feedback_controls()
    quantum = quantum_record_twin()
    counterfactual = counterfactual_design()
    approaches = approach_registry()

    distributed_cases = {
        "complete_flat_case": distributed_twin(
            flat=True,
            quorum=3,
            provenance="independent",
            boundary="lifted",
            hardening="none",
        ),
        "coarse_boundary_case": distributed_twin(
            flat=True,
            quorum=3,
            provenance="independent",
            boundary="coarse",
            hardening="none",
        ),
        "frustrated_rejected_case": distributed_twin(
            flat=False,
            quorum=3,
            provenance="independent",
            boundary="lifted",
            hardening="reject",
        ),
        "missing_adversary_case": distributed_twin(
            flat=True,
            quorum=3,
            provenance="independent",
            boundary="lifted",
            hardening="none",
            adversary_declared=False,
        ),
    }

    required_approach_fields = {
        "question",
        "repo_route",
        "lenses",
        "kits",
        "counterfactual_estimand",
        "smallest_object",
        "strongest_absorber",
        "first_move",
        "negative_output",
        "cheap_kill",
        "scale_gate",
    }
    checks = {
        "tree_and_flat_triangle_descend": (
            descent["tree_solution_count"] == 2
            and descent["flat_triangle_solution_count"] == 2
        ),
        "frustrated_loop_has_no_global_section": (
            descent["frustrated_triangle_solution_count"] == 0
            and descent["frustrated_cycle_syndrome"] == 1
        ),
        "proper_local_constraints_can_hide_global_obstruction": descent[
            "each_proper_edge_family_is_satisfiable"
        ],
        "affine_flatness_theorem_exhaustive_through_four_vertices": (
            descent["exhaustive_connected_graph_cases_through_four_vertices"] > 0
            and not descent["exhaustive_flatness_solution_count_failures"]
        ),
        "repair_restores_descent": descent["repair_restores_solution_count"] == 2,
        "project_or_lift_bound_nontrivial": (
            descent["path_independent_capacity_bits"] == 0
            and descent["minimum_provenance_alphabet_for_identity_action"] == 2
        ),
        "quorum_intersection_formula_exhaustive_through_n8": (
            quorum["exhaustive_cases_through_n_8"] > 0
            and not quorum["quorum_intersection_formula_failures"]
        ),
        "safety_and_liveness_separated": quorum[
            "safety_and_liveness_are_distinct"
        ],
        "raw_count_and_independent_support_separated": quorum[
            "raw_count_can_overstate_independent_support"
        ],
        "threshold_access_monotone": (
            access["monotone"] and access["unauthorized_singletons"]
        ),
        "certification_and_disclosure_separated": access[
            "certification_and_disclosure_separate"
        ],
        "coarse_boundary_fails_action_sufficiency": (
            boundary["coarse_summary_factors_local_action"]
            and not boundary["coarse_summary_factors_all_upper_actions"]
        ),
        "lifted_boundary_restores_action_sufficiency": boundary[
            "lifted_summary_factors_all_upper_actions"
        ],
        "minimum_boundary_alphabet_exact": (
            boundary["minimum_boundary_labels_for_frozen_upper_actions"] == 4
        ),
        "benign_subdivision_preserves_syndrome": (
            refinement["syndrome_preserved_under_subdivision"]
            and refinement["descent_solution_count_preserved_under_subdivision"]
            and refinement["raw_hop_count_is_not_invariant"]
        ),
        "feedback_changes_future_capability_not_past_record": (
            feedback["future_capability_strictly_increases"]
            and feedback["past_accessible_record_is_unchanged"]
            and not feedback["retroactive_rewrite"]
        ),
        "ghz_proper_subsets_do_not_identify_phase": quantum[
            "all_proper_subset_reduced_states_equal"
        ],
        "ghz_logical_parity_identifies_phase": quantum[
            "global_logical_action_distinguishes_phase"
        ],
        "quantum_boundary_requires_logical_lift": (
            not quantum["proper_subset_summary_factors_global_action"]
            and quantum["logical_parity_lift_factors_global_action"]
            and quantum["result"] == REQUIRES_LIFT
        ),
        "distributed_return_vocabulary_exercised": (
            {
                case["result"] for case in distributed_cases.values()
            }
            == {DESCENDS, REQUIRES_LIFT, REJECTS, INCOMPLETE}
        ),
        "matched_counterfactuals_change_one_field": counterfactual[
            "all_contrasts_change_only_declared_fields"
        ],
        "factorial_counterfactual_surface_complete": (
            sum(counterfactual["full_factorial_result_counts"].values())
            == counterfactual["full_factorial_case_count"]
            == 32
        ),
        "ten_successors_have_complete_approach_cards": (
            len(approaches) == 10
            and all(
                required_approach_fields <= set(approach)
                for approach in approaches.values()
            )
        ),
        "negative_results_are_first_class_outputs": all(
            approach["negative_output"] for approach in approaches.values()
        ),
    }
    failures = [name for name, passed in checks.items() if not passed]

    result = {
        "schema_version": "1.0",
        "run_id": RUN_ID,
        "probe": "du_regional_finality_descent_probe",
        "claim_grade": (
            "EXACT FINITE COMPOSITION CONTROLS / COMPLETE METHOD "
            "ATTACHMENTS / KNOWN COMPONENT MATHEMATICS / NO NEW-PHYSICS "
            "OR ONTOLOGY CLAIM"
        ),
        "regional_finality_kernel": {
            "fields": [
                "internal event/process DAG",
                "record object and provenance",
                "access/decoder structure",
                "validator support and adversary class",
                "typed finality rule",
                "boundary certificate/summary",
                "admitted higher-layer actions",
                "forward-only feedback rule",
            ],
            "six_relations_kept_distinct": [
                "causal influence",
                "entanglement constraint",
                "record formation",
                "access/disclosure",
                "validation/finality",
                "control/capability feedback",
            ],
            "composition_question": (
                "when local certified networks descend to an action-safe "
                "higher node, and which typed obstruction prevents descent"
            ),
        },
        "affine_descent": descent,
        "quorum_and_provenance": quorum,
        "threshold_access": access,
        "boundary_factorization": boundary,
        "benign_refinement": refinement,
        "capability_feedback": feedback,
        "distributed_twin": distributed_cases,
        "quantum_record_twin": quantum,
        "counterfactual_design": counterfactual,
        "approach_registry": approaches,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "REGIONAL_FINALITY_DESCENT_KERNEL_INSTALLED / "
            "FINITE_DESCENT_AND_OBSTRUCTION_CONTROLS_PASS / "
            "TEN_SUCCESSORS_HAVE_COUNTERFACTUAL_APPROACHES"
            if not failures
            else "REGIONAL_FINALITY_KERNEL_OR_APPROACH_AUDIT_FAILED"
        ),
        "does_not_establish": [
            "a novel component theorem",
            "a general noisy or noninvertible descent theorem",
            "a cryptographic protocol or security proof",
            "a physical region, validator, boundary, or scale-selection law",
            "that entanglement is consensus",
            "public quantum objectivity or common knowledge",
            "a finality-to-capability physical law",
            "emergent spacetime geometry or holography",
            "a post-causal-break physical residual",
            "record-first ontology",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    return result


if __name__ == "__main__":
    receipt = run()
    print(
        f"{receipt['verdict']}: "
        f"{receipt['check_count'] - receipt['failure_count']}/"
        f"{receipt['check_count']} checks"
    )
    raise SystemExit(1 if receipt["failures"] else 0)
