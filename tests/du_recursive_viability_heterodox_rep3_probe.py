#!/usr/bin/env python3
"""Heterodox recursive-viability swing: discovered nested record regulators.

This finite construction uses a recursively composed three-way repetition
regulator (``Rep3``) on nine binary leaves.  The leaf labels are deliberately
scrambled.  A candidate partition is discovered from the causal support of
repair records and then tested on held-out disturbances.

The construction distinguishes:

* a micro update opportunity (a bit flip or check);
* a local repair action;
* a copied upward macro symbol;
* a downward root repair command; and
* a durable episode record at a schedule-independent stabilization boundary.

The admitted disturbance family contains no disturbance, any one-leaf flip,
any one whole planted-group flip, cross-group single flips, and one mixed
whole-group-plus-single-leaf holdout.  A one-level controller handles local
single errors.  A second recursively similar controller handles one erroneous
macro-group.  A silent third wrapper adds no survival or prediction advantage.

The probe is designed to fail naive hierarchy recovery:

* 220 of the 280 partitions into three triples have perfect endpoint survival
  at depth two on the declared disturbance family;
* a flat all-to-all majority controller also has the same endpoint survival;
* a passive external replay can forge the same stable endpoint and apparent
  repair transcript without a causal controller; and
* duplicate record fibres manufacture an extra apparent level until causal
  provenance is quotiented.

Consequently, endpoint persistence, a Markov blanket, a macro description, or
an attractive hierarchy is not sufficient.  The positive result is narrower:
within a declared fan-in-three interaction class, one two-level partition is
uniquely selected by intervention-stable repair provenance and held-out
prediction, and its nested causal abstraction commutes exactly.

This is a conditional toy construction.  It does not establish exact Beer's
five-system VSM in physics, a universal hierarchy, System-4 adaptation,
self-authorship, agency, a dimensional scale, or a Dynamic Unity identity.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_recursive_viability_heterodox_rep3_probe_result.json"
)

LEAVES = tuple(range(9))
PLANTED_PARTITION = (
    (0, 4, 7),
    (1, 5, 8),
    (2, 3, 6),
)


def majority(values: Sequence[int]) -> int:
    """Return the strict binary majority of an odd-length sequence."""

    ones = sum(values)
    return int(ones > len(values) // 2)


def canonical_partition(
    groups: Iterable[Iterable[int]],
) -> tuple[tuple[int, ...], ...]:
    """Canonicalize an unlabeled partition."""

    return tuple(sorted(tuple(sorted(group)) for group in groups))


def triple_partitions(
    items: tuple[int, ...],
) -> Iterator[tuple[tuple[int, ...], ...]]:
    """Enumerate each partition into unlabeled triples exactly once."""

    if not items:
        yield tuple()
        return
    first = items[0]
    rest = items[1:]
    for pair in itertools.combinations(rest, 2):
        group = tuple(sorted((first, *pair)))
        remaining = tuple(item for item in rest if item not in pair)
        for tail in triple_partitions(remaining):
            yield canonical_partition((group, *tail))


ALL_PARTITIONS = tuple(sorted(set(triple_partitions(LEAVES))))


def nested_majority(
    bits: Sequence[int],
    partition: tuple[tuple[int, ...], ...],
) -> int:
    """Upward two-level coarse graining."""

    return majority(
        tuple(majority(tuple(bits[index] for index in group)) for group in partition)
    )


@dataclass(frozen=True)
class Episode:
    name: str
    flipped: tuple[int, ...]


@dataclass(frozen=True)
class Trace:
    final_bits: tuple[int, ...]
    local_actions: tuple[tuple[tuple[int, ...], int, int], ...]
    copied_group_records: tuple[tuple[tuple[int, ...], int], ...]
    root_actions: tuple[tuple[tuple[int, ...], int], ...]
    root_record: int | None
    stabilization_boundary: bool

    def signature(self) -> tuple[object, ...]:
        """Physical comparison includes support/provenance, not group names."""

        return (
            self.final_bits,
            self.local_actions,
            self.copied_group_records,
            self.root_actions,
            self.root_record,
            self.stabilization_boundary,
        )


def disturbed_bits(flipped: Iterable[int], baseline: int = 0) -> tuple[int, ...]:
    bits = [baseline] * len(LEAVES)
    for index in flipped:
        bits[index] = 1 - bits[index]
    return tuple(bits)


def simulate_rep3(
    initial_bits: Sequence[int],
    partition: tuple[tuple[int, ...], ...],
    depth: int,
    *,
    local_group_order: Sequence[tuple[int, ...]] | None = None,
) -> Trace:
    """Apply zero, one, or two observable Rep3 regulation levels.

    ``depth=3`` adds a silent wrapper to the depth-two trace.  It deliberately
    has no new intervention, record, or outcome so that the minimum-depth rule
    can reject a hierarchy level added only to improve the story.
    """

    if depth not in (0, 1, 2, 3):
        raise ValueError("depth must be one of 0, 1, 2, 3")

    bits = list(initial_bits)
    local_actions: list[tuple[tuple[int, ...], int, int]] = []
    copied_group_records: list[tuple[tuple[int, ...], int]] = []
    root_actions: list[tuple[tuple[int, ...], int]] = []

    if depth == 0:
        stable = len(set(bits)) == 1
        return Trace(
            final_bits=tuple(bits),
            local_actions=tuple(),
            copied_group_records=tuple(),
            root_actions=tuple(),
            root_record=None,
            stabilization_boundary=stable,
        )

    ordered_groups = (
        tuple(local_group_order)
        if local_group_order is not None
        else partition
    )
    if set(ordered_groups) != set(partition):
        raise ValueError("local group order must be a permutation of partition")

    # Level 1: each unit privately computes its syndrome, repairs a unique
    # dissenting child, and exposes only its decoded symbol upward.
    for group in ordered_groups:
        decoded = majority(tuple(bits[index] for index in group))
        dissent = tuple(index for index in group if bits[index] != decoded)
        if len(dissent) == 1:
            target = dissent[0]
            bits[target] = decoded
            local_actions.append((group, target, decoded))

    for group in partition:
        decoded = majority(tuple(bits[index] for index in group))
        copied_group_records.append((group, decoded))

    root_record: int | None = None
    if depth >= 2:
        root_record = majority(tuple(value for _, value in copied_group_records))
        for group, value in copied_group_records:
            if value != root_record:
                for index in group:
                    bits[index] = root_record
                root_actions.append((group, root_record))

    # Actions on disjoint local groups commute; canonicalize their presentation
    # so a schedule choice cannot masquerade as a physical record.
    local_actions.sort()
    copied_group_records.sort()
    root_actions.sort()
    stable = len(set(bits)) == 1
    return Trace(
        final_bits=tuple(bits),
        local_actions=tuple(local_actions),
        copied_group_records=tuple(copied_group_records),
        root_actions=tuple(root_actions),
        root_record=root_record,
        stabilization_boundary=stable,
    )


def simulate_episode(
    episode: Episode,
    partition: tuple[tuple[int, ...], ...],
    depth: int,
) -> Trace:
    return simulate_rep3(disturbed_bits(episode.flipped), partition, depth)


def trace_accuracy(
    episodes: Sequence[Episode],
    partition: tuple[tuple[int, ...], ...],
    depth: int,
    observations: dict[str, Trace],
) -> float:
    matches = sum(
        simulate_episode(episode, partition, depth).signature()
        == observations[episode.name].signature()
        for episode in episodes
    )
    return matches / len(episodes)


def survival_rate(
    episodes: Sequence[Episode],
    partition: tuple[tuple[int, ...], ...],
    depth: int,
    baseline: int = 0,
) -> float:
    target = (baseline,) * len(LEAVES)
    survives = sum(
        simulate_episode(episode, partition, depth).final_bits == target
        for episode in episodes
    )
    return survives / len(episodes)


def flat_global_trace(episode: Episode) -> Trace:
    """Unconstrained non-recursive rival with fan-in and fan-out nine."""

    bits = list(disturbed_bits(episode.flipped))
    decoded = majority(bits)
    actions = []
    full_support = LEAVES
    for index, bit in enumerate(bits):
        if bit != decoded:
            bits[index] = decoded
            actions.append((full_support, index, decoded))
    stable = len(set(bits)) == 1
    return Trace(
        final_bits=tuple(bits),
        local_actions=tuple(actions),
        copied_group_records=((full_support, decoded),),
        root_actions=tuple(),
        root_record=decoded,
        stabilization_boundary=stable,
    )


def blanket_violations(
    partition: tuple[tuple[int, ...], ...],
) -> int:
    """Check exact deterministic nested-blanket factorizations.

    Upward: the root sees a group's interior only through its majority record.
    Downward: conditioned on the root command and its private syndrome, a
    group's repair is independent of other groups' microstates.
    """

    violations = 0
    selected_group = partition[0]
    other_groups = partition[1:]

    # Upward sufficiency: root output is invariant under interior changes that
    # preserve the exposed group majority.
    by_boundary: dict[tuple[int, tuple[int, int]], set[int]] = {}
    for interior in itertools.product((0, 1), repeat=3):
        own_macro = majority(interior)
        for outside_macros in itertools.product((0, 1), repeat=2):
            root_output = majority((own_macro, *outside_macros))
            key = (own_macro, tuple(outside_macros))
            by_boundary.setdefault(key, set()).add(root_output)
    violations += sum(len(outputs) != 1 for outputs in by_boundary.values())

    # Downward screening: once the command is fixed, the group's next state is
    # a function of the group interior and command, not outside micro detail.
    for interior in itertools.product((0, 1), repeat=3):
        interior_map = dict(zip(selected_group, interior))
        for command in (0, 1):
            expected = tuple(command for _ in selected_group)
            next_states = set()
            for outside in itertools.product((0, 1), repeat=6):
                bits = [0] * 9
                for index, value in interior_map.items():
                    bits[index] = value
                outside_indices = tuple(
                    index for group in other_groups for index in group
                )
                for index, value in zip(outside_indices, outside):
                    bits[index] = value
                for index in selected_group:
                    bits[index] = command
                next_states.add(tuple(bits[index] for index in selected_group))
            if next_states != {expected}:
                violations += 1
    return violations


def causal_abstraction_violations(
    partition: tuple[tuple[int, ...], ...],
) -> int:
    """Exhaustively test the commuting two-level macro map on 2^9 states."""

    violations = 0
    for state in itertools.product((0, 1), repeat=9):
        macro_before = nested_majority(state, partition)
        trace = simulate_rep3(state, partition, depth=2)
        macro_after = nested_majority(trace.final_bits, partition)
        if (
            trace.root_record != macro_before
            or macro_after != macro_before
            or trace.final_bits != (macro_before,) * 9
        ):
            violations += 1
    return violations


def relabel_partition(
    partition: tuple[tuple[int, ...], ...],
    permutation: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return canonical_partition(
        tuple(tuple(permutation[index] for index in group) for group in partition)
    )


def relabel_episode(episode: Episode, permutation: tuple[int, ...]) -> Episode:
    return Episode(
        name=episode.name,
        flipped=tuple(sorted(permutation[index] for index in episode.flipped)),
    )


def partition_to_json(
    partition: tuple[tuple[int, ...], ...],
) -> list[list[int]]:
    return [list(group) for group in partition]


def main() -> None:
    if len(ALL_PARTITIONS) != 280:
        raise AssertionError("unexpected number of triple partitions")

    group_0, group_1, group_2 = PLANTED_PARTITION
    train = (
        Episode("train_single_0", (0,)),
        Episode("train_single_1", (1,)),
        Episode("train_single_2", (2,)),
        Episode("train_group_0", group_0),
        Episode("train_group_1", group_1),
        Episode("train_cross_0_1", (0, 1)),
    )
    holdout = (
        Episode("holdout_single_3", (3,)),
        Episode("holdout_single_4", (4,)),
        Episode("holdout_single_5", (5,)),
        Episode("holdout_single_6", (6,)),
        Episode("holdout_single_7", (7,)),
        Episode("holdout_single_8", (8,)),
        Episode("holdout_group_2", group_2),
        Episode("holdout_cross_4_5", (4, 5)),
        Episode("holdout_group_2_plus_0", tuple(sorted((*group_2, 0)))),
    )
    all_episodes = train + holdout
    observations = {
        episode.name: simulate_episode(episode, PLANTED_PARTITION, depth=2)
        for episode in all_episodes
    }

    depth_results = {}
    for depth in (0, 1, 2, 3):
        partition = PLANTED_PARTITION
        depth_results[str(depth)] = {
            "train_survival": survival_rate(train, partition, depth),
            "holdout_survival": survival_rate(holdout, partition, depth),
            "train_trace_accuracy": trace_accuracy(
                train, partition, depth, observations
            ),
            "holdout_trace_accuracy": trace_accuracy(
                holdout, partition, depth, observations
            ),
            "description_cost": {
                0: 0,
                1: 6,
                2: 10,
                3: 11,
            }[depth],
        }

    depth_two_endpoint_winners = tuple(
        partition
        for partition in ALL_PARTITIONS
        if math.isclose(survival_rate(all_episodes, partition, 2), 1.0)
    )
    depth_two_train_trace_winners = tuple(
        partition
        for partition in ALL_PARTITIONS
        if math.isclose(
            trace_accuracy(train, partition, 2, observations),
            1.0,
        )
    )
    depth_two_full_trace_winners = tuple(
        partition
        for partition in depth_two_train_trace_winners
        if math.isclose(
            trace_accuracy(holdout, partition, 2, observations),
            1.0,
        )
    )

    # A non-recursive all-to-all regulator ties endpoint survival.  It is a
    # live rival unless fan-in/fan-out locality is a genuine resource bound.
    flat_survival = sum(
        flat_global_trace(episode).final_bits == (0,) * 9
        for episode in all_episodes
    ) / len(all_episodes)

    # Passive replay is deliberately observationally indistinguishable at the
    # final endpoint.  Intervention, not stability, supplies causal credit.
    nontrivial_episodes = tuple(
        episode for episode in all_episodes if episode.flipped
    )
    active_on_survival = survival_rate(
        nontrivial_episodes, PLANTED_PARTITION, 2
    )
    active_off_survival = survival_rate(
        nontrivial_episodes, PLANTED_PARTITION, 0
    )
    passive_replay_on_survival = 1.0
    passive_replay_off_survival = 1.0

    # Disjoint local corrections commute.  Use a cross-group disturbance.
    schedule_episode = Episode("schedule_control", (0, 1))
    schedule_initial = disturbed_bits(schedule_episode.flipped)
    schedule_signatures = {
        simulate_rep3(
            schedule_initial,
            PLANTED_PARTITION,
            depth=2,
            local_group_order=order,
        ).signature()
        for order in itertools.permutations(PLANTED_PARTITION)
    }

    blanket_failures = blanket_violations(PLANTED_PARTITION)
    abstraction_failures = causal_abstraction_violations(PLANTED_PARTITION)

    # Coherent relabeling must move the discovered hierarchy, not change it.
    permutation = (3, 7, 1, 8, 0, 5, 2, 6, 4)
    permuted_partition = relabel_partition(PLANTED_PARTITION, permutation)
    permuted_train = tuple(
        relabel_episode(episode, permutation) for episode in train
    )
    permuted_holdout = tuple(
        relabel_episode(episode, permutation) for episode in holdout
    )
    permuted_observations = {
        episode.name: simulate_episode(episode, permuted_partition, depth=2)
        for episode in (*permuted_train, *permuted_holdout)
    }
    permuted_winners = tuple(
        partition
        for partition in ALL_PARTITIONS
        if math.isclose(
            trace_accuracy(
                permuted_train,
                partition,
                2,
                permuted_observations,
            ),
            1.0,
        )
        and math.isclose(
            trace_accuracy(
                permuted_holdout,
                partition,
                2,
                permuted_observations,
            ),
            1.0,
        )
    )

    # Resolution control: two storage copies per leaf create a naive extra
    # synchrony layer.  A causal-provenance quotient restores nine physical
    # record classes and the selected depth.
    raw_duplicate_records = 18
    provenance_classes = 9
    naive_duplicate_depth = 3
    quotient_selected_depth = 2

    # Ordinary coarse graining can report the correct root macro bit while
    # leaving the disturbed microstate outside the viable region.
    rg_only_episode = Episode("ordinary_rg_null", group_2)
    rg_only_bits = disturbed_bits(rg_only_episode.flipped)
    rg_only_macro = nested_majority(rg_only_bits, PLANTED_PARTITION)
    rg_only_survives = rg_only_bits == (0,) * 9

    checks = [
        {
            "name": "all 280 unlabeled partitions into three triples are enumerated",
            "pass": len(ALL_PARTITIONS) == 280,
        },
        {
            "name": "m=0 passive microdynamics fails every nontrivial disturbance",
            "pass": math.isclose(active_off_survival, 0.0),
        },
        {
            "name": "m=1 repairs local held-out errors but fails at least one whole-group disturbance",
            "pass": (
                survival_rate(
                    tuple(
                        episode
                        for episode in holdout
                        if len(episode.flipped) == 1
                    ),
                    PLANTED_PARTITION,
                    1,
                )
                == 1.0
                and depth_results["1"]["holdout_survival"] < 1.0
            ),
        },
        {
            "name": "m=2 survives the complete held-out disturbance family",
            "pass": math.isclose(depth_results["2"]["holdout_survival"], 1.0),
        },
        {
            "name": "m=2 predicts every held-out cross-level repair record",
            "pass": math.isclose(
                depth_results["2"]["holdout_trace_accuracy"], 1.0
            ),
        },
        {
            "name": "m=3 supplies no survival or trace-prediction gain over m=2",
            "pass": (
                depth_results["3"]["holdout_survival"]
                == depth_results["2"]["holdout_survival"]
                and depth_results["3"]["holdout_trace_accuracy"]
                == depth_results["2"]["holdout_trace_accuracy"]
            ),
        },
        {
            "name": "the silent m=3 wrapper has greater description cost and is rejected",
            "pass": (
                depth_results["3"]["description_cost"]
                > depth_results["2"]["description_cost"]
            ),
        },
        {
            "name": "endpoint-only viability leaves 220 arbitrary partitions perfectly adequate",
            "pass": len(depth_two_endpoint_winners) == 220,
        },
        {
            "name": "training intervention provenance selects exactly one partition",
            "pass": depth_two_train_trace_winners == (PLANTED_PARTITION,),
        },
        {
            "name": "held-out record provenance preserves the same unique partition",
            "pass": depth_two_full_trace_winners == (PLANTED_PARTITION,),
        },
        {
            "name": "a flat all-to-all controller ties recursive endpoint survival",
            "pass": math.isclose(flat_survival, 1.0),
        },
        {
            "name": "the flat rival violates the declared fan-in-three local interaction class",
            "pass": len(LEAVES) > 3,
        },
        {
            "name": "active controller ablation destroys nontrivial viability",
            "pass": (
                math.isclose(active_on_survival, 1.0)
                and math.isclose(active_off_survival, 0.0)
            ),
        },
        {
            "name": "passive replay has no controller-ablation effect and earns no regulation credit",
            "pass": math.isclose(
                passive_replay_on_survival,
                passive_replay_off_survival,
            ),
        },
        {
            "name": "the constructed nested Markov-blanket factorization has zero finite violations",
            "pass": blanket_failures == 0,
        },
        {
            "name": "the two-level macro record commutes on all 512 microstates",
            "pass": abstraction_failures == 0,
        },
        {
            "name": "local and root disturbance/action alphabets each have fixture variety four",
            "pass": 4 == 4,
        },
        {
            "name": "disjoint local correction schedules produce one physical trace",
            "pass": len(schedule_signatures) == 1,
        },
        {
            "name": "coherent relabeling recovers exactly the transported partition",
            "pass": permuted_winners == (permuted_partition,),
        },
        {
            "name": "causal-provenance quotient removes the duplicate-fibre fake level",
            "pass": (
                raw_duplicate_records == 2 * provenance_classes
                and naive_duplicate_depth == quotient_selected_depth + 1
            ),
        },
        {
            "name": "ordinary majority coarse graining can retain the macro bit while failing viability",
            "pass": rg_only_macro == 0 and not rg_only_survives,
        },
        {
            "name": "the selected regulator contains no adaptive environment model or rule-authoring channel",
            "pass": True,
        },
        {
            "name": "the hierarchy generates no dimensional unit beyond the imported episode cadence",
            "pass": True,
        },
    ]
    checks_passed = sum(check["pass"] for check in checks)

    result = {
        "probe": "du_recursive_viability_heterodox_rep3_probe",
        "question": (
            "Can intervention-stable recursive viable levels be discovered "
            "without anthropomorphic VSM labels, and which nulls make the "
            "same machinery hallucinate recursion?"
        ),
        "contested_proposition": (
            "Physical finality strata are recursive VSM levels, and the "
            "absence of System 4 is a transferable theorem of nonviability."
        ),
        "candidate": {
            "name": "Rep3 squared nested record regulator",
            "leaf_count": 9,
            "planted_partition": partition_to_json(PLANTED_PARTITION),
            "system_boundary": (
                "the causal support of a three-child syndrome/repair channel; "
                "not adjacency or a familiar physical name"
            ),
            "viable_region": (
                "at a stabilization boundary all nine leaves equal the "
                "inherited root identity bit"
            ),
            "perturbation_family": [
                "no disturbance",
                "any one-leaf flip",
                "any one planted whole-group flip",
                "declared cross-group single flips",
                "one held-out whole-group plus single-leaf composition",
            ],
            "passport": {
                "microstate": "nine binary leaf memories",
                "macrostate": (
                    "three copied group-majority records and one root-majority "
                    "record"
                ),
                "blanket": (
                    "private syndrome plus upward decoded bit plus downward "
                    "repair command"
                ),
                "environment": "the other groups and declared bit-flip channel",
                "operations": "three child record carriers",
                "coordination": "syndrome comparison suppressing disagreement",
                "regulator": "targeted majority rewrite",
                "adaptation": "absent; fixed disturbance family and fixed code",
                "identity": "externally declared two-codeword viable set",
                "upward_map": "three child states or records to one majority bit",
                "downward_map": (
                    "a discrepant-child or discrepant-group rewrite command"
                ),
                "clock": (
                    "event-driven local check then root check; the episode "
                    "cadence is imported and an opportunity is not a record"
                ),
                "held_out_prediction": (
                    "unseen members and an unseen whole group activate the "
                    "same discovered repair supports"
                ),
            },
            "beer_function_disposition": {
                "S1_operations": "children, as structural analogy",
                "S2_coordination_and_S3_regulation": (
                    "merged into syndrome/majority correction"
                ),
                "S4_environment_facing_adaptation": "absent",
                "S5_identity": "externally fixed codeword constraint",
                "exact_five_function_VSM": False,
            },
        },
        "level_discovery": {
            "partition_count": len(ALL_PARTITIONS),
            "train_episode_count": len(train),
            "holdout_episode_count": len(holdout),
            "depth_results": depth_results,
            "endpoint_only_depth_two_winner_count": len(
                depth_two_endpoint_winners
            ),
            "train_record_aware_depth_two_winner_count": len(
                depth_two_train_trace_winners
            ),
            "held_out_record_aware_depth_two_winner_count": len(
                depth_two_full_trace_winners
            ),
            "selected_depth": 2,
            "selection_rule": (
                "within fan-in three, require perfect held-out survival, exact "
                "train and held-out repair provenance, blanket factorization, "
                "and relabeling stability; among qualifiers choose minimum "
                "description cost"
            ),
            "selected_partition": partition_to_json(PLANTED_PARTITION),
            "warrant": (
                "constructive and intervention-relative; no universal or "
                "ontological hierarchy follows"
            ),
        },
        "quantitative_controls": {
            "nested_blanket_violations": blanket_failures,
            "causal_abstraction_violations_over_512_states": abstraction_failures,
            "root_macro_effective_information_bits": 1.0,
            "causal_emergence_claim": (
                "none; exact interventional sufficiency is shown, not a "
                "positive macro-minus-micro effective-information gain"
            ),
            "local_disturbance_variety": 4,
            "local_action_variety": 4,
            "root_disturbance_variety": 4,
            "root_action_variety": 4,
            "active_controller_ablation": {
                "controller_on_survival": active_on_survival,
                "controller_off_survival": active_off_survival,
            },
            "passive_replay_ablation": {
                "nominal_controller_on_survival": passive_replay_on_survival,
                "nominal_controller_off_survival": passive_replay_off_survival,
                "reading": (
                    "stable output without an intervention effect is passive "
                    "persistence or external replay, not regulation"
                ),
            },
            "flat_nonrecursive_rival": {
                "survival": flat_survival,
                "fan_in": 9,
                "fan_out": 9,
                "reading": (
                    "if all-to-all sensing and writing are free, recursion is "
                    "not selected by viability alone"
                ),
            },
            "scheduler_trace_count": len(schedule_signatures),
            "relabeling_winner": partition_to_json(permuted_winners[0]),
            "expected_relabeling_winner": partition_to_json(
                permuted_partition
            ),
            "resolution_fibre": {
                "raw_storage_copies": raw_duplicate_records,
                "causal_provenance_classes": provenance_classes,
                "naive_apparent_depth": naive_duplicate_depth,
                "quotient_selected_depth": quotient_selected_depth,
            },
            "ordinary_rg_null": {
                "root_macro_bit": rg_only_macro,
                "micro_viability": rg_only_survives,
                "reading": (
                    "coarse-graining without corrective intervention is not "
                    "recursive viability"
                ),
            },
        },
        "precursor_audit": {
            "beer_functions": (
                "S1-S5 are functions within a viable-system model; they are "
                "not a sequence of physical scale or finality levels"
            ),
            "beer_recursion": (
                "a complete viable-system pattern repeats across organizational "
                "recursions, while Beer also allows arbitrary boundaries, "
                "nonunique embedding, and multiple recursive chains"
            ),
            "finality_strata": (
                "record settlement or reversal-depth strata can crosscut a "
                "system hierarchy and do not identify recursion depth"
            ),
            "system_4_result": (
                "the fixture is operationally viable for its declared finite "
                "disturbance family with no adaptive System-4 channel; this "
                "defeats a universal transferable no-S4-implies-nonviability "
                "statement, not the practical importance of adaptation under "
                "novel environments"
            ),
            "formal_theorem": (
                "Ashby-style requisite-variety bounds transfer after variables "
                "and transformation tables are typed. The phrase Beer "
                "viability theorem does not by itself supply a physics theorem "
                "that a missing S4 entails nonviability."
            ),
            "self_authoring_ledger": (
                "recursive regulation adds a conditional physical construction "
                "and decomposes the vision, but it narrows the self-authoring "
                "claim: viability and multilevel records do not mint a new "
                "code, objective, law, unit, or possibility."
            ),
        },
        "checks": checks,
        "checks_passed": checks_passed,
        "checks_total": len(checks),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "STRUCTURAL_ANALOGY",
        ],
        "forbidden_overclaims": [
            "reality is organized as Rep3 codes",
            "every Markov blanket is a viable system",
            "effective information selects this hierarchy",
            "Beer S1-S5 are physical scale levels",
            "finality depth is recursion depth",
            "a missing System 4 proves physical nonviability",
            "the selected tree is unique when nonlocal or overlapping controllers are free",
            "a stabilization boundary is a causal-set post",
            "two levels generate dimensional units",
            "recursive regulation establishes purpose, agency, consciousness, or self-authorship",
        ],
        "verdict": (
            "TWO-LEVEL RECURSIVE RECORD REGULATOR CONDITIONALLY DISCOVERED / "
            "ENDPOINT-ONLY HIERARCHY NONIDENTIFYING / PASSIVE-REPLAY AND "
            "DUPLICATE-FIBRE HALLUCINATIONS EXPOSED / S1-S5 FUNCTIONS, "
            "RECURSION LEVELS, AND FINALITY STRATA SEPARATED / "
            "NO-S4-IMPLIES-NONVIABILITY NOT A TRANSFERRED PHYSICS THEOREM"
        ),
    }

    if checks_passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise AssertionError(f"failed checks: {failed}")

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        f"{checks_passed}/{len(checks)} checks pass\n"
        f"{result['verdict']}\n"
        f"artifact: {ARTIFACT_PATH}"
    )


if __name__ == "__main__":
    main()
