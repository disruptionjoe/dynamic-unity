#!/usr/bin/env python3
"""Exact finite controls for typed recursive regional composition.

This probe starts after record interfaces have been independently formed.  It
does not select a cover, interface, observer, or physical record law.

It establishes a finite mixed composition contract:

* the largest independently warranted identity relation at a declared type is
  an intersection of equivalence kernels;
* typed identity discrepancies compose by a tight total-variation triangle
  bound;
* compatible marginals glue automatically on a join tree, but exact overlap
  agreement and individually valid pair records do not imply a global
  extension on a cycle;
* approximate action-factorization defects compose by a tight triangle bound;
* an action-sufficient certificate may disclose only a history-class
  statement rather than the underlying history; and
* benign relay subdivision preserves the exact obstruction class while a
  naive per-edge scalar compatibility distance changes.

The component mathematics is standard equivalence-relation, junction-tree,
parity-polytope, approximate-sufficiency, zero-knowledge/access-structure, and
logical-code terrain.  The result is a program contract and counterexample
suite, not a new physical law or a quantum-strength selection principle.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_recursive_record_composition_result.json"
)
RUN_ID = "RUN-20260725-100452-record-formation-certified-composition"

Item = str
Partition = tuple[tuple[Item, ...], ...]
Relation = frozenset[tuple[Item, Item]]
PairDistribution = dict[tuple[int, int], Fraction]


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [jsonable(item) for item in sorted(value)]
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


def normalized_partition(blocks: Iterable[Iterable[Item]]) -> Partition:
    normalized = tuple(
        sorted(
            (
                tuple(sorted(block))
                for block in blocks
                if tuple(block)
            ),
            key=lambda block: block[0],
        )
    )
    return normalized


def relation_from_partition(partition: Partition) -> Relation:
    return frozenset(
        (left, right)
        for block in partition
        for left in block
        for right in block
    )


def partition_from_signature(
    items: Sequence[Item],
    signature: Mapping[Item, Any],
) -> Partition:
    blocks: dict[Any, list[Item]] = {}
    for item in items:
        blocks.setdefault(signature[item], []).append(item)
    return normalized_partition(blocks.values())


def all_partitions(items: Sequence[Item]) -> tuple[Partition, ...]:
    """Enumerate every set partition in a deterministic canonical order."""

    partitions: list[Partition] = [()]
    for item in items:
        successors: set[Partition] = set()
        for partition in partitions:
            successors.add(normalized_partition(partition + ((item,),)))
            for index in range(len(partition)):
                blocks = [tuple(block) for block in partition]
                blocks[index] = tuple(sorted(blocks[index] + (item,)))
                successors.add(normalized_partition(blocks))
        partitions = sorted(successors)
    return tuple(partitions)


def relation_intersection(*relations: Relation) -> Relation:
    if not relations:
        return frozenset()
    result = set(relations[0])
    for relation in relations[1:]:
        result.intersection_update(relation)
    return frozenset(result)


def typed_identity_relation(
    items: Sequence[Item],
    evidence_partition: Partition,
    signatures: Mapping[str, Mapping[Item, Any]],
    required_types: Sequence[str],
) -> Relation:
    relations = [relation_from_partition(evidence_partition)]
    for identity_type in required_types:
        relations.append(
            relation_from_partition(
                partition_from_signature(items, signatures[identity_type])
            )
        )
    return relation_intersection(*relations)


def relation_blocks(items: Sequence[Item], relation: Relation) -> Partition:
    unseen = set(items)
    blocks = []
    while unseen:
        root = min(unseen)
        block = tuple(sorted(item for item in items if (root, item) in relation))
        blocks.append(block)
        unseen.difference_update(block)
    return normalized_partition(blocks)


def typed_overlap_identity_control() -> dict[str, Any]:
    items = ("qnd_A", "qnd_B", "post_record_flip", "other_origin")
    evidence_partition = (
        ("qnd_A", "qnd_B", "post_record_flip"),
        ("other_origin",),
    )
    signatures = {
        "effect": {
            "qnd_A": "Z_effect",
            "qnd_B": "Z_effect",
            "post_record_flip": "Z_effect",
            "other_origin": "X_effect",
        },
        "selective_instrument": {
            "qnd_A": "QND_Z",
            "qnd_B": "QND_Z",
            "post_record_flip": "Z_then_X",
            "other_origin": "X_measurement",
        },
        "multitime_history": {
            "qnd_A": "repeat_Z",
            "qnd_B": "repeat_Z",
            "post_record_flip": "reverse_Z",
            "other_origin": "repeat_X",
        },
        "upper_action": {
            "qnd_A": "next_Z_same",
            "qnd_B": "next_Z_same",
            "post_record_flip": "next_Z_reversed",
            "other_origin": "next_X",
        },
    }
    required_type_sets = {
        "effect_only": ("effect",),
        "instrument": ("effect", "selective_instrument"),
        "history": (
            "effect",
            "selective_instrument",
            "multitime_history",
        ),
        "action": (
            "effect",
            "selective_instrument",
            "multitime_history",
            "upper_action",
        ),
    }
    all_candidate_partitions = all_partitions(items)
    results = {}
    maximality_failures = []
    evidence_relation = relation_from_partition(evidence_partition)
    for claim_type, required_types in required_type_sets.items():
        maximal = typed_identity_relation(
            items,
            evidence_partition,
            signatures,
            required_types,
        )
        type_kernels = tuple(
            relation_from_partition(
                partition_from_signature(items, signatures[name])
            )
            for name in required_types
        )
        admissible_relations = []
        for partition in all_candidate_partitions:
            candidate = relation_from_partition(partition)
            if (
                candidate <= evidence_relation
                and all(candidate <= kernel for kernel in type_kernels)
            ):
                admissible_relations.append(candidate)
                if not candidate <= maximal:
                    maximality_failures.append(
                        {
                            "claim_type": claim_type,
                            "partition": partition,
                        }
                    )
        results[claim_type] = {
            "required_types": required_types,
            "maximal_warranted_blocks": relation_blocks(items, maximal),
            "identified_ordered_pair_count": len(maximal),
            "admissible_equivalence_relation_count": len(admissible_relations),
            "is_unique_maximum_by_relation_inclusion": all(
                relation <= maximal for relation in admissible_relations
            ),
        }

    return {
        "items": items,
        "independently_formed_evidence_partition": evidence_partition,
        "typed_signatures": signatures,
        "typed_relations": results,
        "set_partition_count": len(all_candidate_partitions),
        "maximality_failures": maximality_failures,
        "theorem": (
            "For an independently formed equivalence E and predeclared "
            "typed signatures sigma_t, E intersected with every kernel "
            "ker(sigma_t) is the unique greatest equivalence contained in E "
            "whose identifications are sound at those types."
        ),
        "weakest_claim_interpretation": (
            "Use the least committal identity type needed by the next "
            "composition. Effect identity does not promote itself to "
            "instrument, history, provenance, or action identity."
        ),
        "boundary": (
            "The construction filters an independently supplied evidence "
            "relation. It does not physically select E or a regional cover."
        ),
    }


def bernoulli_tv(left: Fraction, right: Fraction) -> Fraction:
    return abs(left - right)


def binary_symmetric_channel(
    probability_one: Fraction,
    error: Fraction,
) -> Fraction:
    return error + (1 - 2 * error) * probability_one


def identity_composition_control() -> dict[str, Any]:
    signatures = (Fraction(0), Fraction(1, 4), Fraction(1, 2))
    first = bernoulli_tv(signatures[0], signatures[1])
    second = bernoulli_tv(signatures[1], signatures[2])
    endpoint = bernoulli_tv(signatures[0], signatures[2])
    error = Fraction(1, 4)
    postprocessed = tuple(
        binary_symmetric_channel(value, error) for value in signatures
    )
    post_endpoint = bernoulli_tv(postprocessed[0], postprocessed[2])
    subdivided_path = (
        signatures[0],
        signatures[1],
        signatures[1],
        signatures[2],
    )
    subdivided_sum = sum(
        (
            bernoulli_tv(left, right)
            for left, right in zip(
                subdivided_path,
                subdivided_path[1:],
            )
        ),
        start=Fraction(0),
    )
    return {
        "typed_bernoulli_signatures": signatures,
        "edge_defects": (first, second),
        "endpoint_defect": endpoint,
        "triangle_upper_bound": first + second,
        "bound_is_tight": endpoint == first + second,
        "common_bsc_error": error,
        "postprocessed_signatures": postprocessed,
        "postprocessed_endpoint_defect": post_endpoint,
        "expected_contraction": (1 - 2 * error) * endpoint,
        "common_postprocessing_contracts_identity_defect": (
            post_endpoint <= endpoint
            and post_endpoint == (1 - 2 * error) * endpoint
        ),
        "zero_defect_relay_subdivision_path": subdivided_path,
        "subdivided_path_bound": subdivided_sum,
        "subdivision_preserves_bound": subdivided_sum == first + second,
        "theorem": (
            "For a fixed typed record test and total variation, chained "
            "identity discrepancy is at most the sum of seam discrepancies. "
            "The bound is tight and common stochastic postprocessing cannot "
            "increase it."
        ),
    }


def pair_distribution(relation: str) -> PairDistribution:
    if relation not in {"equal", "unequal"}:
        raise ValueError(relation)
    return {
        (left, right): (
            Fraction(1, 2)
            if ((left == right) == (relation == "equal"))
            else Fraction(0)
        )
        for left, right in itertools.product((0, 1), repeat=2)
    }


def pair_marginal(
    distribution: Mapping[tuple[int, int], Fraction],
    index: int,
) -> dict[int, Fraction]:
    return {
        value: sum(
            (
                probability
                for assignment, probability in distribution.items()
                if assignment[index] == value
            ),
            start=Fraction(0),
        )
        for value in (0, 1)
    }


def glue_pair_chain(
    left: Mapping[tuple[int, int], Fraction],
    right: Mapping[tuple[int, int], Fraction],
) -> dict[tuple[int, int, int], Fraction]:
    overlap_left = pair_marginal(left, 1)
    overlap_right = pair_marginal(right, 0)
    if overlap_left != overlap_right:
        raise ValueError("overlap_marginals_do_not_match")
    joint = {}
    for a, b, c in itertools.product((0, 1), repeat=3):
        if overlap_left[b] == 0:
            probability = Fraction(0)
        else:
            probability = left[(a, b)] * right[(b, c)] / overlap_left[b]
        joint[(a, b, c)] = probability
    return joint


def marginalize_triple(
    joint: Mapping[tuple[int, int, int], Fraction],
    indexes: tuple[int, int],
) -> PairDistribution:
    return {
        pair: sum(
            (
                probability
                for state, probability in joint.items()
                if (state[indexes[0]], state[indexes[1]]) == pair
            ),
            start=Fraction(0),
        )
        for pair in itertools.product((0, 1), repeat=2)
    }


def satisfies_cycle(state: Sequence[int], parities: Sequence[int]) -> bool:
    return all(
        (state[index] ^ state[(index + 1) % len(state)]) == parity
        for index, parity in enumerate(parities)
    )


def cycle_control(parities: Sequence[int]) -> dict[str, Any]:
    n = len(parities)
    if n < 3 or any(value not in (0, 1) for value in parities):
        raise ValueError("binary cycle with at least three edges required")
    syndrome = sum(parities) % 2
    assignments = tuple(
        state
        for state in itertools.product((0, 1), repeat=n)
        if satisfies_cycle(state, parities)
    )
    if syndrome:
        repaired_vertices = tuple(
            tuple(
                bit ^ int(edge == flipped)
                for edge, bit in enumerate(parities)
            )
            for flipped in range(n)
        )
        average = tuple(
            sum(
                (Fraction(vertex[index]) for vertex in repaired_vertices),
                start=Fraction(0),
            )
            / n
            for index in range(n)
        )
        max_shift = max(
            abs(average[index] - parities[index]) for index in range(n)
        )
        repaired_even = all(sum(vertex) % 2 == 0 for vertex in repaired_vertices)
    else:
        repaired_vertices = (tuple(parities),)
        average = tuple(Fraction(value) for value in parities)
        max_shift = Fraction(0)
        repaired_even = True
    return {
        "edge_count": n,
        "parities": tuple(parities),
        "z2_cycle_syndrome": syndrome,
        "global_assignment_count": len(assignments),
        "global_extension_exists": bool(assignments),
        "nearest_even_vertex_mixture": average,
        "constructive_linf_edge_edit": max_shift,
        "exact_linf_distance_to_even_parity_polytope": Fraction(syndrome, n),
        "lower_bound": (
            "the violated odd-set functional changes by at most n*epsilon "
            "under an L-infinity edge edit"
        ),
        "upper_bound": (
            "the uniform mixture of the n even vectors obtained by flipping "
            "one edge is exactly 1/n away"
        ),
        "repair_vertices_are_even": repaired_even,
        "distance_bound_is_tight": max_shift == Fraction(syndrome, n),
    }


def acyclic_and_cyclic_compatibility_control() -> dict[str, Any]:
    left = {
        (0, 0): Fraction(1, 4),
        (0, 1): Fraction(1, 4),
        (1, 0): Fraction(1, 8),
        (1, 1): Fraction(3, 8),
    }
    right = {
        (0, 0): Fraction(1, 8),
        (0, 1): Fraction(1, 4),
        (1, 0): Fraction(1, 2),
        (1, 1): Fraction(1, 8),
    }
    chain_joint = glue_pair_chain(left, right)
    chain_exact = (
        sum(chain_joint.values(), start=Fraction(0)) == 1
        and marginalize_triple(chain_joint, (0, 1)) == left
        and marginalize_triple(chain_joint, (1, 2)) == right
    )

    equal = pair_distribution("equal")
    unequal = pair_distribution("unequal")
    overlap_marginals = (
        pair_marginal(equal, 0),
        pair_marginal(equal, 1),
        pair_marginal(unequal, 0),
        pair_marginal(unequal, 1),
    )
    frustrated_triangle = cycle_control((0, 0, 1))

    return {
        "join_tree_positive_control": {
            "contexts": ("AB", "BC"),
            "overlap": "B",
            "overlap_marginals_match": (
                pair_marginal(left, 1) == pair_marginal(right, 0)
            ),
            "constructed_joint": chain_joint,
            "joint_normalized_and_reproduces_both_marginals": chain_exact,
            "theorem": (
                "Finite normalized context distributions on a join tree "
                "with matching separator marginals glue by conditional "
                "multiplication, with zero-mass separators handled by zero."
            ),
        },
        "cycle_counterexample": {
            "contexts": {
                "AB": equal,
                "BC": equal,
                "CA": unequal,
            },
            "every_context_normalized": all(
                sum(distribution.values(), start=Fraction(0)) == 1
                for distribution in (equal, equal, unequal)
            ),
            "all_one_variable_overlap_marginals_equal": (
                len(
                    {
                        tuple(sorted(marginal.items()))
                        for marginal in overlap_marginals
                    }
                )
                == 1
            ),
            "every_pair_record_is_sharp_relation": True,
            "full_cover_global_extension_exists": frustrated_triangle[
                "global_extension_exists"
            ],
            "global_obstruction": frustrated_triangle,
            "counterexample": (
                "exact pairwise overlap agreement plus individually valid "
                "sharp pair records does not imply a global extension on a "
                "cyclic cover"
            ),
        },
        "composition_rule": (
            "Join-tree covers may use local overlap receipts. Cyclic or "
            "higher-order covers require a full-cover primal/dual or "
            "equivalent obstruction receipt after the identity map is frozen."
        ),
    }


def benign_refinement_control() -> dict[str, Any]:
    flat_original = cycle_control((0, 0, 0))
    flat_subdivided = cycle_control((0, 0, 0, 0))
    frustrated_original = cycle_control((0, 0, 1))
    frustrated_subdivided = cycle_control((0, 0, 0, 1))
    return {
        "declared_benign_morphism": (
            "replace edge C--A by C--R--A with R a deterministic, "
            "zero-cost, zero-latency, inaccessible identity relay and no "
            "new intervention"
        ),
        "flat_original": flat_original,
        "flat_subdivided": flat_subdivided,
        "frustrated_original": frustrated_original,
        "frustrated_subdivided": frustrated_subdivided,
        "extension_verdict_preserved": (
            flat_original["global_extension_exists"]
            == flat_subdivided["global_extension_exists"]
            and frustrated_original["global_extension_exists"]
            == frustrated_subdivided["global_extension_exists"]
        ),
        "solution_count_preserved": (
            flat_original["global_assignment_count"]
            == flat_subdivided["global_assignment_count"]
            and frustrated_original["global_assignment_count"]
            == frustrated_subdivided["global_assignment_count"]
        ),
        "z2_obstruction_class_preserved": (
            flat_original["z2_cycle_syndrome"]
            == flat_subdivided["z2_cycle_syndrome"]
            and frustrated_original["z2_cycle_syndrome"]
            == frustrated_subdivided["z2_cycle_syndrome"]
        ),
        "naive_scalar_distance_changes": (
            frustrated_original[
                "exact_linf_distance_to_even_parity_polytope"
            ]
            != frustrated_subdivided[
                "exact_linf_distance_to_even_parity_polytope"
            ]
        ),
        "naive_distance_before": frustrated_original[
            "exact_linf_distance_to_even_parity_polytope"
        ],
        "naive_distance_after": frustrated_subdivided[
            "exact_linf_distance_to_even_parity_polytope"
        ],
        "counterexample": (
            "For a deterministic odd n-cycle, the raw per-edge L-infinity "
            "distance to the even-parity polytope is exactly 1/n. An inert "
            "subdivision changes 1/3 to 1/4 while preserving the Z2 "
            "obstruction. Therefore that scalar is not refinement-natural."
        ),
        "naturality_rule": (
            "Carry the extension/dual or cohomological obstruction through "
            "the declared refinement morphism. Compute any scalar cost only "
            "after collapsing benign relays or assigning physical weights."
        ),
    }


def optimal_binary_action_defect(
    states: Sequence[Item],
    summary: Mapping[Item, Any],
    response_probability: Mapping[Item, Fraction],
) -> Fraction:
    defects = []
    for label in sorted(set(summary.values()), key=str):
        values = tuple(
            response_probability[state]
            for state in states
            if summary[state] == label
        )
        defects.append((max(values) - min(values)) / 2)
    return max(defects, default=Fraction(0))


def action_composition_control() -> dict[str, Any]:
    states = ("s0", "s1")
    actual = {"s0": Fraction(0), "s1": Fraction(1)}
    first_summary = {"s0": "u", "s1": "v"}
    first_approximation = {"u": Fraction(1, 4), "v": Fraction(3, 4)}
    second_summary = {"u": "z", "v": "z"}
    second_approximation = {"z": Fraction(1, 2)}
    first_defect = max(
        bernoulli_tv(
            actual[state],
            first_approximation[first_summary[state]],
        )
        for state in states
    )
    second_defect = max(
        bernoulli_tv(
            first_approximation[label],
            second_approximation[second_summary[label]],
        )
        for label in first_approximation
    )
    composite_defect = max(
        bernoulli_tv(
            actual[state],
            second_approximation[
                second_summary[first_summary[state]]
            ],
        )
        for state in states
    )
    direct_optimal = optimal_binary_action_defect(
        states,
        {state: "z" for state in states},
        actual,
    )
    return {
        "actual_binary_response_probabilities": actual,
        "first_summary": first_summary,
        "first_approximation": first_approximation,
        "second_summary": second_summary,
        "second_approximation": second_approximation,
        "first_stage_defect": first_defect,
        "second_stage_defect": second_defect,
        "composite_defect": composite_defect,
        "recursive_upper_bound": first_defect + second_defect,
        "bound_is_tight": (
            composite_defect == first_defect + second_defect
        ),
        "direct_optimal_composite_defect": direct_optimal,
        "zero_defect_relay_changes_nothing": True,
        "theorem": (
            "If an actual response is alpha-close to a first summary "
            "simulator and that simulator is beta-close to a second summary "
            "simulator in worst-case total variation, the composite is at "
            "most alpha+beta close. The bound is tight."
        ),
    }


def fibers(
    domain: Sequence[Any],
    mapping: Callable[[Any], Any],
) -> dict[Any, tuple[Any, ...]]:
    result: dict[Any, list[Any]] = {}
    for item in domain:
        result.setdefault(mapping(item), []).append(item)
    return {
        key: tuple(value)
        for key, value in sorted(result.items(), key=lambda row: str(row[0]))
    }


def certificate_without_disclosure_control() -> dict[str, Any]:
    histories = tuple(itertools.product((0, 1), repeat=3))

    def parity(history: tuple[int, int, int]) -> int:
        return history[0] ^ history[1] ^ history[2]

    def first_certificate(
        history: tuple[int, int, int],
    ) -> tuple[int, int]:
        return parity(history), history[0]

    def outer_certificate(
        certificate: tuple[int, int],
    ) -> int:
        return certificate[0]

    first_values = {history: first_certificate(history) for history in histories}
    outer_values = {
        history: outer_certificate(first_values[history])
        for history in histories
    }
    parity_action = {history: Fraction(parity(history)) for history in histories}
    hidden_action = {history: Fraction(history[2]) for history in histories}
    first_fibers = fibers(histories, first_certificate)
    outer_fibers = fibers(
        histories,
        lambda history: outer_certificate(first_certificate(history)),
    )
    parity_first_defect = optimal_binary_action_defect(
        tuple(str(history) for history in histories),
        {str(history): first_values[history] for history in histories},
        {str(history): parity_action[history] for history in histories},
    )
    parity_outer_defect = optimal_binary_action_defect(
        tuple(str(history) for history in histories),
        {str(history): outer_values[history] for history in histories},
        {str(history): parity_action[history] for history in histories},
    )
    hidden_outer_defect = optimal_binary_action_defect(
        tuple(str(history) for history in histories),
        {str(history): outer_values[history] for history in histories},
        {str(history): hidden_action[history] for history in histories},
    )
    return {
        "history_count": len(histories),
        "first_certificate": "(parity class, first-bit tag)",
        "outer_certificate": "parity class only",
        "first_certificate_fiber_sizes": tuple(
            len(fiber) for fiber in first_fibers.values()
        ),
        "outer_certificate_fiber_sizes": tuple(
            len(fiber) for fiber in outer_fibers.values()
        ),
        "first_certificate_is_history_injective": (
            all(len(fiber) == 1 for fiber in first_fibers.values())
        ),
        "outer_certificate_is_history_injective": (
            all(len(fiber) == 1 for fiber in outer_fibers.values())
        ),
        "parity_action_defect_at_first_certificate": parity_first_defect,
        "parity_action_defect_after_recursive_outer_certificate": (
            parity_outer_defect
        ),
        "hidden_history_action_defect_after_outer_certificate": (
            hidden_outer_defect
        ),
        "certificate_content": (
            "a publicly checkable history-class statement: parity class"
        ),
        "disclosed_history": False,
        "recursive_composition_succeeds_for_declared_action": (
            parity_first_defect == 0 and parity_outer_defect == 0
        ),
        "same_certificate_is_not_universally_action_sufficient": (
            hidden_outer_defect == Fraction(1, 2)
        ),
        "theorem": (
            "For maps H->C1->C2 and an upper response Y, if Y factors "
            "through C1 and the induced response on C1 factors through C2, "
            "then Y factors through the composite certificate. Neither map "
            "need be injective on histories."
        ),
        "scope": (
            "Exact functional non-disclosure only. No commitment hiding, "
            "zero-knowledge simulator, soundness reduction, cryptographic "
            "setup, adversarial security, or physical secrecy is proved."
        ),
    }


def defect_independence_control() -> dict[str, Any]:
    rows = []
    for identity_bad, marginal_bad, action_bad in itertools.product(
        (False, True),
        repeat=3,
    ):
        rows.append(
            {
                "identity_case": (
                    "typed seam mismatch" if identity_bad else "typed seam exact"
                ),
                "marginal_case": (
                    "odd cycle obstruction"
                    if marginal_bad
                    else "flat compatible cover"
                ),
                "action_case": (
                    "aliased binary action"
                    if action_bad
                    else "action factors exactly"
                ),
                "defect_vector": {
                    "identity_tv": Fraction(int(identity_bad)),
                    "marginal_obstruction_class": int(marginal_bad),
                    "action_tv": (
                        Fraction(1, 2) if action_bad else Fraction(0)
                    ),
                },
            }
        )
    vectors = {
        (
            row["defect_vector"]["identity_tv"],
            row["defect_vector"]["marginal_obstruction_class"],
            row["defect_vector"]["action_tv"],
        )
        for row in rows
    }
    return {
        "product_fixture_rows": rows,
        "all_eight_zero_nonzero_patterns_realized": len(vectors) == 8,
        "interpretation": (
            "Inside the finite product class, no coordinate implies either "
            "of the others. A scalar norm can flag nonzero total defect but "
            "cannot identify the required repair."
        ),
        "boundary": (
            "Logical independence in a product fixture is not evidence that "
            "the coordinates vary independently in a physical system."
        ),
    }


def recursive_vector_contract(
    identity: Mapping[str, Any],
    compatibility: Mapping[str, Any],
    action: Mapping[str, Any],
) -> dict[str, Any]:
    identity_bound = min(
        Fraction(1),
        sum(identity["edge_defects"], start=Fraction(0)),
    )
    action_bound = min(
        Fraction(1),
        action["first_stage_defect"] + action["second_stage_defect"],
    )
    cycle = compatibility["cycle_counterexample"]
    return {
        "vector_type": (
            "typed identity total-variation bound",
            "full-cover marginal primal/dual or obstruction class",
            "upper-action total-variation bound",
        ),
        "recursive_vector": {
            "identity_endpoint_defect": identity["endpoint_defect"],
            "identity_path_upper_bound": identity_bound,
            "marginal_global_extension_exists": cycle[
                "full_cover_global_extension_exists"
            ],
            "marginal_obstruction_class": cycle["global_obstruction"][
                "z2_cycle_syndrome"
            ],
            "action_composite_defect": action["composite_defect"],
            "action_path_upper_bound": action_bound,
        },
        "mixed_composition_law": (
            "Identity and action coordinates have subadditive path bounds. "
            "The marginal coordinate must be recomputed on the full glued "
            "cover after typed identities are frozen; it is not the sum of "
            "local compatibility verdicts."
        ),
        "exact_descent_condition": (
            "The vector must be zero at the identity type needed by the "
            "upper task, carry a full-cover global extension, and have zero "
            "action defect, in addition to separately declared adversarial "
            "safety, liveness, provenance, and resource gates."
        ),
        "no_scalar_corollary": (
            "There is no representation-independent scalar composition law "
            "from local identity/action errors and pairwise compatibility "
            "alone: cyclic compatibility is a global receipt, and a naive "
            "compatibility distance changes under inert subdivision."
        ),
    }


def gpt_and_instrument_bridge() -> dict[str, Any]:
    return {
        "probability_level_result": (
            "This branch supplies no principle stronger than probability-"
            "level exclusivity or Local Orthogonality and makes no claim to "
            "exclude almost-quantum correlations."
        ),
        "formed_interface_result": (
            "Formed interfaces and typed overlap identity license which "
            "occurrences may be glued. They do not make pairwise records "
            "globally composable."
        ),
        "specker_absorber": (
            "For general POVMs/instruments, pairwise compatibility need not "
            "imply joint compatibility. For finite sharp projective records "
            "represented by pairwise commuting PVMs on one Hilbert space, "
            "standard spectral theory already supplies the joint observable."
        ),
        "open_stronger_principle": (
            "A genuinely stronger instrument-level pairwise-to-global law "
            "would need independently justified sharpness, repeatability, "
            "common-system identity, nondisturbance, and composition "
            "conditions, then show a consequence not already absorbed by "
            "joint measurability, Specker contextuality, process tensors, "
            "QEC, or Local Orthogonality."
        ),
        "claim": "EXPLICIT BRIDGE/ABSORBER CHECK ONLY",
    }


def run() -> dict[str, Any]:
    overlap = typed_overlap_identity_control()
    identity = identity_composition_control()
    compatibility = acyclic_and_cyclic_compatibility_control()
    refinement = benign_refinement_control()
    action = action_composition_control()
    certificate = certificate_without_disclosure_control()
    independence = defect_independence_control()
    vector = recursive_vector_contract(identity, compatibility, action)
    bridge = gpt_and_instrument_bridge()

    effect_blocks = overlap["typed_relations"]["effect_only"][
        "maximal_warranted_blocks"
    ]
    instrument_blocks = overlap["typed_relations"]["instrument"][
        "maximal_warranted_blocks"
    ]
    checks = {
        "all_15_partitions_on_four_occurrences_enumerated": (
            overlap["set_partition_count"] == 15
        ),
        "typed_identity_intersection_is_unique_maximum": (
            not overlap["maximality_failures"]
            and all(
                row["is_unique_maximum_by_relation_inclusion"]
                for row in overlap["typed_relations"].values()
            )
        ),
        "effect_identity_is_strictly_weaker_than_instrument_identity": (
            effect_blocks != instrument_blocks
            and any(
                set(block)
                == {"qnd_A", "qnd_B", "post_record_flip"}
                for block in effect_blocks
            )
            and any(
                set(block) == {"qnd_A", "qnd_B"}
                for block in instrument_blocks
            )
        ),
        "identity_triangle_bound_is_tight": identity["bound_is_tight"],
        "identity_common_postprocessing_contracts": identity[
            "common_postprocessing_contracts_identity_defect"
        ],
        "identity_zero_relay_preserves_path_bound": identity[
            "subdivision_preserves_bound"
        ],
        "join_tree_overlap_marginals_glue_exactly": compatibility[
            "join_tree_positive_control"
        ]["joint_normalized_and_reproduces_both_marginals"],
        "cycle_has_exact_pairwise_overlap_agreement": compatibility[
            "cycle_counterexample"
        ]["all_one_variable_overlap_marginals_equal"],
        "cycle_pairwise_records_do_not_glue_globally": (
            not compatibility["cycle_counterexample"][
                "full_cover_global_extension_exists"
            ]
        ),
        "odd_triangle_linf_defect_is_one_third": (
            compatibility["cycle_counterexample"]["global_obstruction"][
                "exact_linf_distance_to_even_parity_polytope"
            ]
            == Fraction(1, 3)
        ),
        "cycle_distance_constructive_bound_is_exact": compatibility[
            "cycle_counterexample"
        ]["global_obstruction"]["distance_bound_is_tight"],
        "benign_subdivision_preserves_extension_verdict": refinement[
            "extension_verdict_preserved"
        ],
        "benign_subdivision_preserves_solution_count": refinement[
            "solution_count_preserved"
        ],
        "benign_subdivision_preserves_obstruction_class": refinement[
            "z2_obstruction_class_preserved"
        ],
        "naive_compatibility_scalar_fails_naturality": (
            refinement["naive_scalar_distance_changes"]
            and refinement["naive_distance_before"] == Fraction(1, 3)
            and refinement["naive_distance_after"] == Fraction(1, 4)
        ),
        "action_composition_bound_is_tight": action["bound_is_tight"],
        "certificate_chain_preserves_declared_action": certificate[
            "recursive_composition_succeeds_for_declared_action"
        ],
        "certificate_chain_does_not_disclose_history": (
            not certificate["first_certificate_is_history_injective"]
            and not certificate["outer_certificate_is_history_injective"]
            and not certificate["disclosed_history"]
        ),
        "certificate_action_sufficiency_is_task_relative": certificate[
            "same_certificate_is_not_universally_action_sufficient"
        ],
        "all_identity_marginal_action_patterns_realized": independence[
            "all_eight_zero_nonzero_patterns_realized"
        ],
        "recursive_vector_keeps_global_marginal_receipt_separate": (
            vector["recursive_vector"]["marginal_obstruction_class"] == 1
            and not vector["recursive_vector"][
                "marginal_global_extension_exists"
            ]
        ),
        "gpt_bridge_does_not_claim_almost_quantum_exclusion": (
            "no claim to exclude almost-quantum"
            in bridge["probability_level_result"]
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": (
            "dynamic-unity/recursive-record-composition/v0.1"
        ),
        "run_id": RUN_ID,
        "probe": "du_recursive_record_composition_probe",
        "claim_grade": (
            "EXACT FINITE TYPED-IDENTITY / JOIN-TREE / CYCLIC-"
            "COUNTEREXAMPLE / REFINEMENT-NATURALITY / ACTION-BOUND "
            "CONTROLS / COMPONENT MATHEMATICS KNOWN / PHYSICAL "
            "REGIONAL COMPOSITION OPEN"
        ),
        "formed_interface_precondition": (
            "All region, record, certificate, provenance, and boundary "
            "interfaces are independently fixed inputs. No result here "
            "selects or forms them."
        ),
        "typed_overlap_identity": overlap,
        "identity_composition": identity,
        "marginal_compatibility": compatibility,
        "benign_refinement": refinement,
        "action_composition": action,
        "certificate_without_history_disclosure": certificate,
        "defect_coordinate_independence": independence,
        "recursive_vector_contract": vector,
        "gpt_and_instrument_bridge": bridge,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "TYPED_RECURSIVE_COMPOSITION_CONTRACT_INSTALLED / "
            "IDENTITY_AND_ACTION_BOUNDS_TIGHT / GLOBAL_MARGINAL_RECEIPT_"
            "NONLOCAL_TO_COMPOSITION / NAIVE_SCALAR_REFINEMENT_"
            "NATURALITY_REFUTED / CERTIFICATE_CONTENT_SEPARATED_FROM_"
            "HISTORY_DISCLOSURE"
        ),
        "novelty_grade": {
            "known": (
                "equivalence-kernel intersections",
                "total-variation triangle and data processing",
                "join-tree/Vorobev/sheaf gluing",
                "parity-polytope and cohomological cycle obstruction",
                "approximate sufficient-statistic bounds",
                "certificate/disclosure separation in zero-knowledge, "
                "access-structure, provenance, and QEC terrain",
                "pairwise-versus-joint compatibility/Specker terrain",
            ),
            "dynamic_unity_increment": (
                "one mixed typed recursive contract that requires formed "
                "identity, full-cover marginal, and action receipts "
                "separately; an exact relay-subdivision counterexample to a "
                "naive scalar compatibility defect; and explicit "
                "certificate-content versus history-disclosure typing"
            ),
            "search_status": (
                "PROGRAM-LEVEL SYNTHESIS / CLAIM-SPECIFIC NOVELTY SEARCH "
                "NOT PERFORMED / NO PAPER OR PHYSICAL-LAW CLAIM"
            ),
        },
        "does_not_establish": (
            "physical selection or formation of regions and interfaces",
            "a general robust stochastic descent theorem",
            "a new sheaf, database, consensus, or QEC theorem",
            "zero-knowledge cryptographic security",
            "pairwise-to-global composition for general quantum instruments",
            "exclusion of almost-quantum or PR correlations",
            "beyond-standard quantum dynamics",
            "public finality, emergent geometry, or record-first ontology",
        ),
    }


def main() -> None:
    result = run()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    if result["failure_count"]:
        raise SystemExit(
            f"{result['failure_count']}/{result['check_count']} checks failed: "
            f"{result['failures']}"
        )
    print(
        f"{result['check_count']}/{result['check_count']} checks passed: "
        f"{ARTIFACT}"
    )


if __name__ == "__main__":
    main()
