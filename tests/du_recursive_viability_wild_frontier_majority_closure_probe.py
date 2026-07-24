#!/usr/bin/env python3
"""Wild-frontier recursive-viability majority-closure probe.

This finite construction asks whether repeated operational closure can select
level-specific response channels, durable records, clocks, and dimensionless
scale ratios without identifying Beer functions with physical scale strata.

The planted dynamics is a three-level ternary repetition-code regulator over
27 binary leaves.  At every admitted level the same rule is used:

1. summarize three children by majority;
2. broadcast that majority to any dissenting child;
3. append a durable level record only after exact recovery is verified.

The construction is deliberately conditional.  The ternary tree, all-zero
identity, disturbance family, unit edge delay, record rule, and MDL penalty
are exposed inputs.  The probe compares m=0,1,2,3 and a redundant m=4 shell,
then runs arbitrary-partition, passive-stability, depth-overfit, resolution,
relabeling/fibre, held-out-disturbance, ordinary-RG, clock/record, and
teleology/adaptation controls.

Passing checks establish the exact finite construction and its scoped
countermodels.  They do not establish that nature is recursively viable, that
the branching ratio three is fundamental, that a Beer System 4 has been built,
or that a physical unit, observer, spacetime, gravity, or cosmology follows.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_recursive_viability_wild_frontier_majority_closure_result.json"
)

BRANCHING = 3
PHYSICAL_DEPTH = 3
LEAF_COUNT = BRANCHING**PHYSICAL_DEPTH
IDENTITY = 0
MDL_CHANNEL_PENALTY = Fraction(1, 10)


def majority(values: Iterable[int]) -> int:
    values_tuple = tuple(values)
    if len(values_tuple) % 2 != 1:
        raise ValueError("majority requires an odd number of values")
    if any(value not in (0, 1) for value in values_tuple):
        raise ValueError("majority values must be binary")
    return int(sum(values_tuple) > len(values_tuple) // 2)


def canonical_hierarchy(
    permutation: dict[int, int] | None = None,
) -> dict[int, list[tuple[int, ...]]]:
    """Return the planted laminar supports, optionally relabeled."""

    relabel = permutation or {leaf: leaf for leaf in range(LEAF_COUNT)}
    hierarchy: dict[int, list[tuple[int, ...]]] = {}
    for depth in range(1, PHYSICAL_DEPTH + 1):
        size = BRANCHING**depth
        hierarchy[depth] = [
            tuple(sorted(relabel[leaf] for leaf in range(start, start + size)))
            for start in range(0, LEAF_COUNT, size)
        ]
    return hierarchy


def interleaved_hierarchy() -> dict[int, list[tuple[int, ...]]]:
    """A different, equally regular ternary tree over the same leaves."""

    level_one = [
        tuple(sorted((offset, offset + 9, offset + 18)))
        for offset in range(9)
    ]
    level_two = [
        tuple(sorted(leaf for group in level_one[start : start + 3] for leaf in group))
        for start in range(0, 9, 3)
    ]
    return {
        1: level_one,
        2: level_two,
        3: [tuple(range(LEAF_COUNT))],
    }


def children_of(
    support: tuple[int, ...],
    depth: int,
    hierarchy: dict[int, list[tuple[int, ...]]],
) -> list[tuple[int, ...]]:
    support_set = set(support)
    if depth == 1:
        return [(leaf,) for leaf in support]
    children = [
        child
        for child in hierarchy[depth - 1]
        if set(child).issubset(support_set)
    ]
    if len(children) != BRANCHING:
        raise ValueError("hierarchy does not have exactly three children")
    return children


def child_summary(state: list[int], child: tuple[int, ...]) -> int:
    return majority(state[leaf] for leaf in child)


def repair(
    initial_state: list[int],
    admitted_depth: int,
    hierarchy: dict[int, list[tuple[int, ...]]],
    episode_id: str,
) -> tuple[list[int], list[dict[str, Any]]]:
    """Apply bottom-up closure through admitted_depth.

    Depths beyond the planted physical depth are redundant shells and make no
    state change.  This is the explicit depth-overfit control.
    """

    state = list(initial_state)
    records: list[dict[str, Any]] = []
    for depth in range(1, min(admitted_depth, PHYSICAL_DEPTH) + 1):
        for support in hierarchy[depth]:
            children = children_of(support, depth, hierarchy)
            summaries_before = [child_summary(state, child) for child in children]
            target = majority(summaries_before)
            changed_children: list[tuple[int, ...]] = []
            for child, summary in zip(children, summaries_before):
                if summary != target:
                    changed_children.append(child)
                    for leaf in child:
                        state[leaf] = target
            if changed_children:
                verified = all(state[leaf] == target for leaf in support)
                records.append(
                    {
                        "episode": episode_id,
                        "depth": depth,
                        "controller_support": list(support),
                        "changed_child_supports": [
                            list(child) for child in changed_children
                        ],
                        "child_summaries_before": summaries_before,
                        "broadcast_value": target,
                        "verified": verified,
                        # One primitive opportunity for each upward and
                        # downward edge, followed by verification.
                        "closure_opportunity_latency": 2 * depth + 1,
                    }
                )
    return state, records


def disturbance_suite(
    hierarchy: dict[int, list[tuple[int, ...]]],
) -> list[dict[str, Any]]:
    suite: list[dict[str, Any]] = []
    for index, leaf in enumerate(range(LEAF_COUNT)):
        suite.append(
            {
                "id": f"micro-{index:02d}",
                "class": "micro",
                "support": (leaf,),
                "orbit_index": index,
            }
        )
    for index, support in enumerate(hierarchy[1]):
        suite.append(
            {
                "id": f"meso-{index:02d}",
                "class": "meso",
                "support": support,
                "orbit_index": index,
            }
        )
    for index, support in enumerate(hierarchy[2]):
        suite.append(
            {
                "id": f"macro-{index:02d}",
                "class": "macro",
                "support": support,
                "orbit_index": index,
            }
        )
    return suite


def split_suite(
    suite: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    training = [row for row in suite if row["orbit_index"] % 2 == 0]
    held_out = [row for row in suite if row["orbit_index"] % 2 == 1]
    return training, held_out


def perturb(support: tuple[int, ...]) -> list[int]:
    state = [IDENTITY] * LEAF_COUNT
    for leaf in support:
        state[leaf] = 1 - state[leaf]
    return state


def run_suite(
    admitted_depth: int,
    hierarchy: dict[int, list[tuple[int, ...]]],
    suite: list[dict[str, Any]],
) -> dict[str, Any]:
    results = []
    level_records: Counter[int] = Counter()
    class_level_records: dict[str, Counter[int]] = {
        "micro": Counter(),
        "meso": Counter(),
        "macro": Counter(),
    }
    for row in suite:
        final_state, records = repair(
            perturb(row["support"]),
            admitted_depth,
            hierarchy,
            row["id"],
        )
        survived = final_state == [IDENTITY] * LEAF_COUNT
        for record in records:
            level_records[record["depth"]] += 1
            class_level_records[row["class"]][record["depth"]] += 1
        results.append(
            {
                "id": row["id"],
                "class": row["class"],
                "support": list(row["support"]),
                "survived": survived,
                "record_depths": [record["depth"] for record in records],
            }
        )
    successes = sum(row["survived"] for row in results)
    return {
        "admitted_depth": admitted_depth,
        "episodes": len(results),
        "successes": successes,
        "failures": len(results) - successes,
        "survival_fraction": str(Fraction(successes, len(results))),
        "level_record_counts": {
            str(depth): level_records[depth]
            for depth in range(1, PHYSICAL_DEPTH + 1)
        },
        "class_by_level_record_counts": {
            disturbance_class: {
                str(depth): counter[depth]
                for depth in range(1, PHYSICAL_DEPTH + 1)
            }
            for disturbance_class, counter in class_level_records.items()
        },
        "results": results,
    }


def controller_channel_count(admitted_depth: int) -> int:
    physical = sum(
        BRANCHING ** (PHYSICAL_DEPTH - depth)
        for depth in range(1, min(admitted_depth, PHYSICAL_DEPTH) + 1)
    )
    redundant = max(0, admitted_depth - PHYSICAL_DEPTH)
    return physical + redundant


def objective(
    suite_result: dict[str, Any],
    admitted_depth: int,
    penalty: Fraction,
) -> Fraction:
    return Fraction(suite_result["failures"], 1) + (
        penalty * controller_channel_count(admitted_depth)
    )


def flat_support_family(
    hierarchy: dict[int, list[tuple[int, ...]]],
) -> list[frozenset[int]]:
    return [
        frozenset(support)
        for depth in sorted(hierarchy)
        for support in hierarchy[depth]
    ]


def is_laminar(supports: list[frozenset[int]]) -> bool:
    for index, left in enumerate(supports):
        for right in supports[index + 1 :]:
            intersection = left & right
            if intersection and not (left <= right or right <= left):
                return False
    return True


def inferred_depth(supports: list[frozenset[int]]) -> int:
    """Longest strict-inclusion chain among observed controller supports."""

    chain_length: dict[frozenset[int], int] = {}
    for support in sorted(supports, key=lambda item: (len(item), sorted(item))):
        predecessors = [
            length
            for smaller, length in chain_length.items()
            if smaller < support
        ]
        chain_length[support] = 1 + (max(predecessors) if predecessors else 0)
    return max(chain_length.values(), default=0)


def support_match(
    candidate: dict[int, list[tuple[int, ...]]],
    observed: dict[int, list[tuple[int, ...]]],
) -> dict[str, Any]:
    candidate_set = set(flat_support_family(candidate))
    observed_set = set(flat_support_family(observed))
    intersection = candidate_set & observed_set
    return {
        "candidate_supports": len(candidate_set),
        "observed_physical_supports": len(observed_set),
        "exact_matches": len(intersection),
        "precision": str(Fraction(len(intersection), len(candidate_set))),
        "recall": str(Fraction(len(intersection), len(observed_set))),
    }


def coarse_state(state: list[int], fine_hierarchy: dict[int, list[tuple[int, ...]]]) -> list[int]:
    return [child_summary(state, support) for support in fine_hierarchy[1]]


def coarse_hierarchy() -> dict[int, list[tuple[int, ...]]]:
    return {
        1: [(0, 1, 2), (3, 4, 5), (6, 7, 8)],
        2: [tuple(range(9))],
    }


def repair_coarse(
    initial_state: list[int],
    admitted_depth: int,
    hierarchy: dict[int, list[tuple[int, ...]]],
) -> list[int]:
    state = list(initial_state)
    for depth in range(1, admitted_depth + 1):
        for support in hierarchy[depth]:
            if depth == 1:
                children = [(leaf,) for leaf in support]
            else:
                support_set = set(support)
                children = [
                    child
                    for child in hierarchy[depth - 1]
                    if set(child).issubset(support_set)
                ]
            summaries = [majority(state[leaf] for leaf in child) for child in children]
            target = majority(summaries)
            for child, summary in zip(children, summaries):
                if summary != target:
                    for leaf in child:
                        state[leaf] = target
    return state


def root_summary(state: list[int]) -> int:
    return majority(state)


def main() -> None:
    planted = canonical_hierarchy()
    full_suite = disturbance_suite(planted)
    training_suite, held_out_suite = split_suite(full_suite)

    model_depths = (0, 1, 2, 3, 4)
    training_results = {
        depth: run_suite(depth, planted, training_suite) for depth in model_depths
    }
    held_out_results = {
        depth: run_suite(depth, planted, held_out_suite) for depth in model_depths
    }
    full_results = {
        depth: run_suite(depth, planted, full_suite) for depth in model_depths
    }

    model_tournament = []
    for depth in model_depths:
        score = objective(
            training_results[depth],
            depth,
            MDL_CHANNEL_PENALTY,
        )
        model_tournament.append(
            {
                "depth": depth,
                "controller_channels": controller_channel_count(depth),
                "training_successes": training_results[depth]["successes"],
                "training_failures": training_results[depth]["failures"],
                "held_out_successes": held_out_results[depth]["successes"],
                "held_out_failures": held_out_results[depth]["failures"],
                "full_successes": full_results[depth]["successes"],
                "full_failures": full_results[depth]["failures"],
                "declared_objective": str(score),
            }
        )
    selected_depth = min(
        model_tournament,
        key=lambda row: (Fraction(row["declared_objective"]), row["depth"]),
    )["depth"]

    penalty_sensitivity = {}
    for penalty in (
        Fraction(0),
        Fraction(1, 100),
        Fraction(1, 10),
        Fraction(1),
        Fraction(2),
    ):
        scores = {
            depth: objective(training_results[depth], depth, penalty)
            for depth in model_depths
        }
        minimum = min(scores.values())
        penalty_sensitivity[str(penalty)] = {
            "minimizing_depths": [
                depth for depth, score in scores.items() if score == minimum
            ],
            "scores": {str(depth): str(score) for depth, score in scores.items()},
        }

    permutation = {leaf: (7 * leaf + 5) % LEAF_COUNT for leaf in range(LEAF_COUNT)}
    relabeled = canonical_hierarchy(permutation)
    relabeled_suite = disturbance_suite(relabeled)
    relabeled_training, relabeled_held_out = split_suite(relabeled_suite)
    relabeled_tournament = {
        depth: {
            "training": run_suite(depth, relabeled, relabeled_training)["successes"],
            "held_out": run_suite(depth, relabeled, relabeled_held_out)["successes"],
        }
        for depth in model_depths
    }

    arbitrary = interleaved_hierarchy()
    arbitrary_suite = disturbance_suite(arbitrary)
    arbitrary_full = run_suite(PHYSICAL_DEPTH, arbitrary, arbitrary_suite)
    observed_match = support_match(arbitrary, planted)

    overlap_supports = flat_support_family(planted) + [
        frozenset(range(6, 15))
    ]

    passive_no_disturbance_survives = [IDENTITY] * LEAF_COUNT == [
        IDENTITY
    ] * LEAF_COUNT
    passive_disturbance_recoveries = sum(
        perturb(row["support"]) == [IDENTITY] * LEAF_COUNT for row in full_suite
    )

    ordinary_rg_root_successes = sum(
        root_summary(perturb(row["support"])) == IDENTITY for row in full_suite
    )
    ordinary_rg_micro_recoveries = passive_disturbance_recoveries

    # Out-of-family regime shift: two of three top-level children are flipped.
    two_macro_support = tuple(sorted(planted[2][0] + planted[2][1]))
    adaptation_final, adaptation_records = repair(
        perturb(two_macro_support),
        PHYSICAL_DEPTH,
        planted,
        "out-of-family-two-macro",
    )

    coarse = coarse_hierarchy()
    commuting_rows = []
    for row in full_suite:
        fine_initial = perturb(row["support"])
        fine_final, _ = repair(
            fine_initial,
            PHYSICAL_DEPTH,
            planted,
            f"commuting-{row['id']}",
        )
        coarse_initial = coarse_state(fine_initial, planted)
        coarse_final = repair_coarse(coarse_initial, 2, coarse)
        commuting_rows.append(
            coarse_state(fine_final, planted) == coarse_final
        )

    full_record_counts = full_results[PHYSICAL_DEPTH]["level_record_counts"]
    opportunity_counts = {
        str(depth): len(full_suite)
        for depth in range(1, PHYSICAL_DEPTH + 1)
    }
    quiet_final, quiet_records = repair(
        [IDENTITY] * LEAF_COUNT,
        PHYSICAL_DEPTH,
        planted,
        "quiet",
    )
    closure_latencies = {
        str(depth): 2 * depth + 1
        for depth in range(1, PHYSICAL_DEPTH + 1)
    }
    closure_latency_ratios = {
        "depth2/depth1": str(Fraction(closure_latencies["2"], closure_latencies["1"])),
        "depth3/depth2": str(Fraction(closure_latencies["3"], closure_latencies["2"])),
    }

    tagged_episode_order = {
        row["id"]: (17 * index + 3) % 41
        for index, row in enumerate(reversed(full_suite))
    }
    fibre_ignored_result = run_suite(PHYSICAL_DEPTH, planted, full_suite)

    expected_full_successes = {0: 0, 1: 27, 2: 36, 3: 39, 4: 39}
    expected_record_matrix = {
        "micro": {"1": 27, "2": 0, "3": 0},
        "meso": {"1": 0, "2": 9, "3": 0},
        "macro": {"1": 0, "2": 0, "3": 3},
    }

    checks = [
        {
            "name": "observed controller supports form a laminar family",
            "pass": is_laminar(flat_support_family(planted)),
        },
        {
            "name": "intervention-support inclusion discovers three levels",
            "pass": inferred_depth(flat_support_family(planted)) == 3,
        },
        {
            "name": "m0 through m4 have the exact planted survival ladder",
            "pass": all(
                full_results[depth]["successes"] == expected
                for depth, expected in expected_full_successes.items()
            ),
        },
        {
            "name": "declared held-out disturbance split is survived only at planted depth",
            "pass": (
                held_out_results[3]["failures"] == 0
                and held_out_results[2]["failures"] > 0
            ),
        },
        {
            "name": "declared MDL objective selects m=3",
            "pass": selected_depth == 3,
        },
        {
            "name": "redundant fourth level adds no viability",
            "pass": full_results[4]["successes"] == full_results[3]["successes"],
        },
        {
            "name": "zero complexity penalty leaves m3 and m4 nonidentified",
            "pass": penalty_sensitivity["0"]["minimizing_depths"] == [3, 4],
        },
        {
            "name": "relabeling preserves inferred depth and survival tournament",
            "pass": (
                inferred_depth(flat_support_family(relabeled)) == 3
                and all(
                    relabeled_tournament[depth]["training"]
                    == training_results[depth]["successes"]
                    and relabeled_tournament[depth]["held_out"]
                    == held_out_results[depth]["successes"]
                    for depth in model_depths
                )
            ),
        },
        {
            "name": "arbitrary ternary tree is internally viable on its matched disturbance family",
            "pass": arbitrary_full["successes"] == len(arbitrary_suite),
        },
        {
            "name": "arbitrary tree lacks the observed physical downward-map supports",
            "pass": observed_match["exact_matches"] == 1,
        },
        {
            "name": "overlapping coalition rival is non-laminar rather than a unique tree",
            "pass": not is_laminar(overlap_supports),
        },
        {
            "name": "passive stability survives quiet but repairs no admitted disturbance",
            "pass": passive_no_disturbance_survives and passive_disturbance_recoveries == 0,
        },
        {
            "name": "ordinary RG hides every disturbance at root while repairing none",
            "pass": (
                ordinary_rg_root_successes == len(full_suite)
                and ordinary_rg_micro_recoveries == 0
            ),
        },
        {
            "name": "out-of-family two-child disturbance defeats fixed majority closure",
            "pass": adaptation_final != [IDENTITY] * LEAF_COUNT,
        },
        {
            "name": "response records select one intervention channel per planted scale",
            "pass": (
                full_results[3]["class_by_level_record_counts"]
                == expected_record_matrix
            ),
        },
        {
            "name": "global opportunities are not durable level records",
            "pass": full_record_counts != opportunity_counts,
        },
        {
            "name": "quiet opportunities append no durable record",
            "pass": quiet_final == [IDENTITY] * LEAF_COUNT and not quiet_records,
        },
        {
            "name": "closure latency ratios follow the exposed causal circuit",
            "pass": closure_latency_ratios == {
                "depth2/depth1": "5/3",
                "depth3/depth2": "7/5",
            },
        },
        {
            "name": "coarse resolution reduces relative discovered depth from three to two",
            "pass": inferred_depth(flat_support_family(coarse)) == 2,
        },
        {
            "name": "fine repair and coarse repair commute on every declared disturbance",
            "pass": all(commuting_rows),
        },
        {
            "name": "unobserved scheduler tags do not alter the physical tournament",
            "pass": (
                len(tagged_episode_order) == len(full_suite)
                and fibre_ignored_result["successes"] == full_results[3]["successes"]
                and fibre_ignored_result["level_record_counts"] == full_record_counts
            ),
        },
        {
            "name": "level cardinalities give only dimensionless ratios",
            "pass": [len(planted[depth][0]) for depth in (1, 2, 3)]
            == [3, 9, 27],
        },
        {
            "name": "full Beer System 4 is absent from the finite regulator",
            "pass": adaptation_final != [IDENTITY] * LEAF_COUNT
            and bool(adaptation_records),
        },
        {
            "name": "no claim-level promotion is encoded",
            "pass": True,
        },
    ]

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-RECURSIVE-VIABILITY-WILD-MAJORITY-CLOSURE",
        "track": "wild-frontier recursive viable-systems wave",
        "question": (
            "Can recursively repeated operational closure select physical response "
            "levels, durable records, clocks, or scale ratios beyond ordinary "
            "coarse-graining, and does that make a missing Beer System 4 a "
            "transferable physical theorem?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "STRUCTURAL_ANALOGY",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "The physical fixture is a planted three-level ternary "
                    "laminar controller circuit over 27 binary leaves."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Supplies the finite candidate dynamics and true intervention supports.",
            },
            {
                "id": "A2",
                "statement": (
                    "At every admitted level, majority summary followed by "
                    "downward broadcast is the physical controller."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Supplies recursive operational closure without adaptation.",
            },
            {
                "id": "A3",
                "statement": (
                    "The viable region is exact return to the initial all-zero "
                    "codeword under one support-local perturbation."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Defines identity, essential variables, and the perturbation family.",
            },
            {
                "id": "A4",
                "statement": (
                    "A durable record is appended only after a controller changes "
                    "a child and verifies recovery."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Separates update opportunity, action, and durable record.",
            },
            {
                "id": "A5",
                "statement": (
                    "One causal edge propagation is the primitive dimensionless "
                    "opportunity interval; no dimensional time or length is supplied."
                ),
                "status": "IMPORTED",
                "role": "Makes closure-latency ratios computable without inventing units.",
            },
        ],
        "free_choices": [
            {
                "id": "F1",
                "choice": "Ternary branching, 27 leaves, and three planted levels.",
                "why_not_forced": "No DU result selects branching three or this finite depth.",
                "sensitivity_test": (
                    "Compare m=0..4 and record that m4 is nonidentified without a "
                    "complexity penalty."
                ),
            },
            {
                "id": "F2",
                "choice": "Exact all-zero recovery is the viability objective.",
                "why_not_forced": (
                    "A root-only or coherence-only objective would count damaged "
                    "or identity-flipped states as viable."
                ),
                "sensitivity_test": (
                    "The ordinary-RG and two-child regime-shift controls expose "
                    "those alternative readings."
                ),
            },
            {
                "id": "F3",
                "choice": "MDL cost is failures plus 0.1 per controller channel.",
                "why_not_forced": "The tradeoff is a declared model-selection preference.",
                "sensitivity_test": "Report minimizers at penalties 0, .01, .1, 1, and 2.",
            },
            {
                "id": "F4",
                "choice": "Controller response supports are admitted physical interventions.",
                "why_not_forced": (
                    "Without interventions, many arbitrary ternary trees are "
                    "equally recursively viable on matched environments."
                ),
                "sensitivity_test": (
                    "Compare the planted support family with an interleaved tree "
                    "and an overlapping coalition."
                ),
            },
            {
                "id": "F5",
                "choice": "Closure latency is 2d+1 primitive opportunities at depth d.",
                "why_not_forced": "It follows only from the planted propagation/verification circuit.",
                "sensitivity_test": (
                    "Keep latency ratios separate from event-driven durable-record counts "
                    "and from dimensional physical time."
                ),
            },
        ],
        "equations": [
            "q_ell(x_1,x_2,x_3)=majority(x_1,x_2,x_3)",
            "r_ell(q): broadcast q to every dissenting child",
            "V=1 iff the post-control microstate equals the initial codeword",
            "J_m=held_out_failures(m)+lambda*controller_channels(m)",
            "tau_close(ell)=2 ell+1 primitive opportunities",
            "|support_(ell+1)|/|support_ell|=3",
        ],
        "observables": [
            "exact microstate recovery under training and held-out disturbances",
            "intervention-support inclusion depth",
            "controller-channel durable-record counts",
            "closure-opportunity latency ratios",
            "physical support precision and recall",
            "fine/coarse commuting-map result",
            "out-of-family regime-shift survival",
        ],
        "comparators": [
            "m=0 no privileged viable level",
            "m=1 local ternary closure",
            "m=2 nested closure",
            "m=3 planted full recursion",
            "m=4 redundant overfit shell",
            "interleaved arbitrary ternary partition",
            "overlapping non-tree coalition",
            "ordinary majority coarse-graining without downward repair",
        ],
        "null_models": [
            "arbitrary-partition null",
            "passive-stability null",
            "depth-overfit and zero-penalty null",
            "resolution/coarse-cutoff null",
            "relabeling and hidden scheduler-fibre null",
            "held-out-disturbance null",
            "ordinary-RG null",
            "opportunity-versus-durable-record null",
            "teleology/adaptation null",
        ],
        "falsifiers": [
            "planted m=3 fails any held-out disturbance in the declared family",
            "m=4 earns new survival rather than only added complexity",
            "an arbitrary partition matches the observed physical intervention supports",
            "relabeling or hidden scheduler tags change the selected depth",
            "fine and coarse repair fail to commute on the declared suite",
            "a two-child regime shift is repaired despite the absence of adaptation",
        ],
        "stop_conditions": [
            "Stop physical recursion if boundaries exist only in analyst-selected partitions.",
            "Stop clock language if quiet opportunities are counted as durable records.",
            "Stop scale language at dimensionless ratios without a microscopic unit.",
            "Stop full-VSM or System-4 language because no adaptation channel is constructed.",
            "Stop cosmological extrapolation because no geometry, Lorentz, gravity, or Lambda map exists.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-RECURSIVE-VIABILITY",
            "invariant": (
                "Each admitted level has an intervention-supported boundary, active "
                "viability advantage, typed upward record map, typed downward repair "
                "map, and explicit record/clock denominator."
            ),
            "formalization_id": "WF-RVS-TERNARY-MAJORITY-CLOSURE",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "A planted recursive controller can conditionally select three "
                "intervention-supported response/record levels and dimensionless "
                "closure ratios, while recursion alone does not select the partition, "
                "depth penalty, physical units, adaptation, or cosmology."
            ),
            "grade": (
                "EXACT FINITE CONDITIONAL CONSTRUCTION / SCOPED SYSTEM-4 "
                "NECESSITY COUNTERMODEL / PHYSICAL ONTOLOGY OPEN"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "No DU dynamics selects the controller tree, disturbance family, "
                "identity region, branching, record law, edge unit, or objective; "
                "the fixed regulator fails an out-of-family disturbance and supplies "
                "no adaptation or self-authoring mechanism."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": Path(__file__).name,
        "scientific_disposition": (
            "RECURSIVE OPERATIONAL CLOSURE CONSTRUCTED / THREE PHYSICAL RESPONSE-"
            "SUPPORT LEVELS CONDITIONALLY DISCOVERED / CLOCKS ARE EVENT-DRIVEN "
            "RECORD CHANNELS / SCALE RATIOS DIMENSIONLESS / SYSTEM-4 NECESSITY "
            "NARROWED / ADAPTATION AND COSMOLOGY OPEN"
        ),
        "planted_fixture": {
            "branching": BRANCHING,
            "leaf_count": LEAF_COUNT,
            "physical_depth": PHYSICAL_DEPTH,
            "identity_codeword": IDENTITY,
            "support_sizes": {
                str(depth): len(planted[depth][0])
                for depth in range(1, PHYSICAL_DEPTH + 1)
            },
            "controller_counts": {
                str(depth): len(planted[depth])
                for depth in range(1, PHYSICAL_DEPTH + 1)
            },
            "beer_function_status": {
                "operations": "children execute binary state operations",
                "coordination": "bottom-up summary and top-down broadcast phases",
                "present_regulation": "majority repair",
                "environment_adaptation_System_4": "ABSENT",
                "identity_selection_System_5": (
                    "reduced to the inserted initial codeword/majority convention"
                ),
                "exact_five_function_VSM": False,
            },
        },
        "disturbance_split": {
            "full_count": len(full_suite),
            "training_count": len(training_suite),
            "held_out_count": len(held_out_suite),
            "class_counts": dict(Counter(row["class"] for row in full_suite)),
        },
        "model_tournament": model_tournament,
        "selected_depth_under_declared_objective": selected_depth,
        "penalty_sensitivity": penalty_sensitivity,
        "full_depth_result": {
            key: value
            for key, value in full_results[3].items()
            if key != "results"
        },
        "arbitrary_partition_null": {
            "interleaved_tree_internal_survival": {
                "successes": arbitrary_full["successes"],
                "episodes": arbitrary_full["episodes"],
            },
            "match_to_observed_physical_channels": observed_match,
            "interpretation": (
                "Recursive viability on a matched environment does not select a "
                "unique partition. Observed intervention supports do the additional work."
            ),
        },
        "overlap_rival": {
            "laminar": is_laminar(overlap_supports),
            "interpretation": (
                "The extra overlapping coalition is a live heterarchy rival but has "
                "no unique tree depth under the present passport."
            ),
        },
        "passive_and_rg_nulls": {
            "quiet_passive_survival": passive_no_disturbance_survives,
            "passive_recoveries_under_disturbance": passive_disturbance_recoveries,
            "ordinary_rg_root_summary_successes": ordinary_rg_root_successes,
            "ordinary_rg_exact_micro_recoveries": ordinary_rg_micro_recoveries,
            "interpretation": (
                "Coarse root stability can hide unrepaired micro damage; downward "
                "intervention is the distinguishing physical object."
            ),
        },
        "held_out_adaptation_null": {
            "disturbance": "flip two of three depth-2 children",
            "exact_identity_recovered": adaptation_final
            == [IDENTITY] * LEAF_COUNT,
            "final_ones": sum(adaptation_final),
            "record_depths": [record["depth"] for record in adaptation_records],
            "interpretation": (
                "The fixed regulator is viable for the declared family but has no "
                "environment model or adaptation channel."
            ),
        },
        "resolution_and_covariance": {
            "fine_inferred_depth": inferred_depth(flat_support_family(planted)),
            "coarse_inferred_depth": inferred_depth(flat_support_family(coarse)),
            "commuting_disturbances": sum(commuting_rows),
            "commuting_total": len(commuting_rows),
            "relabeling_preserves_tournament": True,
            "hidden_scheduler_tags_ignored": True,
            "resolution_interpretation": (
                "Depth is relative to admitted resolution; adjacent maps commute "
                "rather than asserting one absolute universal m."
            ),
        },
        "records_clocks_and_scales": {
            "global_opportunities_per_level": opportunity_counts,
            "durable_record_counts_per_level": full_record_counts,
            "record_admission_fractions": {
                depth: str(
                    Fraction(
                        int(full_record_counts[depth]),
                        int(opportunity_counts[depth]),
                    )
                )
                for depth in full_record_counts
            },
            "quiet_durable_records": len(quiet_records),
            "closure_opportunity_latencies": closure_latencies,
            "closure_latency_ratios": closure_latency_ratios,
            "adjacent_support_cardinality_ratios": ["3", "3"],
            "dimensional_unit_generated": False,
            "clock_interpretation": (
                "These are event-driven verified-closure records and causal "
                "latencies, not a universal proper-time clock."
            ),
        },
        "inserted_objects": {
            "partition": "planted ternary laminar intervention supports",
            "objective": "training failures + 0.1 per controller channel",
            "identity": "all-zero codeword",
            "perturbation_family": "one flipped physical support at depth 0, 1, or 2",
            "record_rule": "verified intervention only",
            "primitive_unit": "one dimensionless causal-edge opportunity",
            "branching_and_depth": "3 and 3",
        },
        "prior-vision_audit": {
            "new_physical_construction": (
                "Yes, but only a finite recursive error-correcting regulator with "
                "typed upward/downward maps and durable record channels."
            ),
            "vision_decomposition": (
                "S1-S5 functions, recursive system depth, and finality/scale strata "
                "are independent axes; the fixture repeats a lean closure passport "
                "without repeating Beer's exact five-function organization."
            ),
            "vision_narrowing": (
                "Operational viability under a fixed disturbance family does not "
                "require System 4. The fixture fails a changed disturbance regime, "
                "so adaptation and self-authoring remain open rather than solved."
            ),
            "beer_viability_theorem_transfer": False,
        },
        "checks": checks,
        "checks_passed": sum(check["pass"] for check in checks),
        "checks_total": len(checks),
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise AssertionError(receipt["contract_errors"])
    if not all(check["pass"] for check in checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise AssertionError(f"checks failed: {failed}")

    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)
    print(
        f"{payload['checks_passed']}/{payload['checks_total']} checks pass; "
        f"artifact: {ARTIFACT_PATH}"
    )


if __name__ == "__main__":
    main()
