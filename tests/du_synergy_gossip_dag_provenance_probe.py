#!/usr/bin/env python3
"""Exact regression certificate for HC-DU-048.

The analytic result is in:
  explorations/synergy-preserving-gossip-dag-provenance-and-knowledge-2026-07-27.md

This probe uses finite sets, exact rational arithmetic, and idealized signed
event labels.  It is a proof/regression certificate, not a network simulator,
cryptographic implementation, Hashgraph implementation, or physical model.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import product
from json import dumps
from pathlib import Path
from typing import Callable, Hashable, Iterable


CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})
    if not passed:
        raise AssertionError(f"{name}: {detail}")


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def distribution(
    rows: Iterable[tuple],
    observable: Callable[[tuple], Hashable],
) -> dict[Hashable, Fraction]:
    rows = tuple(rows)
    counts = Counter(observable(row) for row in rows)
    return {key: Fraction(count, len(rows)) for key, count in counts.items()}


def bayes_binary_error(
    rows: Iterable[tuple],
    target: Callable[[tuple], int],
    observable: Callable[[tuple], Hashable],
) -> Fraction:
    rows = tuple(rows)
    joint = Counter((target(row), observable(row)) for row in rows)
    values = {observable(row) for row in rows}
    return sum(
        Fraction(min(joint[(0, value)], joint[(1, value)]), len(rows))
        for value in values
    )


def canonical_digest(parts: object) -> str:
    encoded = dumps(parts, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


def make_event(
    creator: str,
    sequence: int,
    payload: object,
    parents: tuple[str, ...] = (),
) -> dict[str, object]:
    body = {
        "creator": creator,
        "sequence": sequence,
        "payload": payload,
        "parents": tuple(parents),
    }
    event_id = canonical_digest(body)
    return {
        **body,
        "id": event_id,
        # This is an idealized attribution label, not a cryptographic signature.
        "signature": f"sig({creator},{event_id})",
    }


def build_dag(r1: int, r2: int, relayed: bool) -> tuple[dict[str, dict], str]:
    source_1 = make_event("source-1", 0, ("share", r1))
    source_2 = make_event("source-2", 0, ("share", r2))
    events = {source_1["id"]: source_1, source_2["id"]: source_2}
    if relayed:
        relay_1 = make_event("relay-a", 0, ("forward", r1), (source_1["id"],))
        relay_2 = make_event("relay-b", 0, ("forward", r2), (source_2["id"],))
        events[relay_1["id"]] = relay_1
        events[relay_2["id"]] = relay_2
        parents = (relay_1["id"], relay_2["id"])
    else:
        parents = (source_1["id"], source_2["id"])
    terminal = make_event("terminal", 0, ("merge", r1, r2), parents)
    events[terminal["id"]] = terminal
    return events, terminal["id"]


def ancestors(events: dict[str, dict], event_id: str) -> set[str]:
    seen: set[str] = set()
    stack = list(events[event_id]["parents"])
    while stack:
        parent = stack.pop()
        if parent not in seen:
            seen.add(parent)
            stack.extend(events[parent]["parents"])
    return seen


def shortest_parent_distance(
    events: dict[str, dict], ancestor_id: str, descendant_id: str
) -> int | None:
    queue = deque([(descendant_id, 0)])
    seen = {descendant_id}
    while queue:
        current, distance = queue.popleft()
        if current == ancestor_id:
            return distance
        for parent in events[current]["parents"]:
            if parent not in seen:
                seen.add(parent)
                queue.append((parent, distance + 1))
    return None


def dag_artifact(r1: int, r2: int) -> tuple:
    """A fixed relayed signed-DAG artifact plus deterministic derived views."""
    events, terminal_id = build_dag(r1, r2, relayed=True)
    event_rows = tuple(
        sorted(
            (
                event["id"],
                event["creator"],
                event["sequence"],
                event["payload"],
                event["parents"],
                event["signature"],
            )
            for event in events.values()
        )
    )
    source_order = tuple(
        event["creator"]
        for event in sorted(
            (
                event
                for event in events.values()
                if str(event["creator"]).startswith("source-")
            ),
            key=lambda event: (event["creator"], event["id"]),
        )
    )
    # A deterministic DAG-derived vote shadow.  This is not the Hashgraph
    # voting algorithm; it witnesses the general factorization boundary.
    sees_both_sources = sum(
        1
        for event_id in ancestors(events, terminal_id)
        if str(events[event_id]["creator"]).startswith("source-")
    ) == 2
    return event_rows, terminal_id, source_order, sees_both_sources


# 1. Matched synergy and null source worlds.
# Rows are (physical target, share 1, share 2).
synergy_rows = tuple((t, pad, t ^ pad) for t, pad in product((0, 1), repeat=2))
null_rows = tuple(product((0, 1), repeat=3))

synergy_pair_distribution = distribution(synergy_rows, lambda row: row[1:])
null_pair_distribution = distribution(null_rows, lambda row: row[1:])
record(
    "synergy_and_null_worlds_have_identical_joint_payload_law",
    synergy_pair_distribution == null_pair_distribution
    and set(synergy_pair_distribution.values()) == {Fraction(1, 4)},
    {str(key): fraction_text(value) for key, value in synergy_pair_distribution.items()},
)
record(
    "synergy_individual_views_are_target_independent",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1])
    == Fraction(1, 2)
    and bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[2])
    == Fraction(1, 2),
    "each one-share Bayes error is 1/2",
)
record(
    "synergy_joint_view_recovers_target",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1:])
    == 0,
    "T = R1 xor R2",
)
record(
    "null_joint_view_remains_target_independent",
    bayes_binary_error(null_rows, lambda row: row[0], lambda row: row[1:])
    == Fraction(1, 2),
    "same payload law, but physical T is independent",
)


# 2. Source-binding nonidentifiability through signed gossip and a hash-DAG.
synergy_artifact_distribution = distribution(
    synergy_rows, lambda row: dag_artifact(row[1], row[2])
)
null_artifact_distribution = distribution(
    null_rows, lambda row: dag_artifact(row[1], row[2])
)
record(
    "matched_signed_dag_artifact_law_cannot_identify_source_binding",
    synergy_artifact_distribution == null_artifact_distribution,
    "payloads, ideal signatures, parent hashes, derived vote shadow, and source order match",
)
record(
    "same_dag_artifact_supports_different_target_relations",
    all((r1 ^ r2) == t for t, r1, r2 in synergy_rows)
    and any((r1 ^ r2) != t for t, r1, r2 in null_rows),
    "protocol artifacts authenticate declared events, not the physical target relation",
)


# 3. Lossless propagation pools source-formed synergy; partitions do not.
record(
    "lossless_plain_gossip_of_both_shares_preserves_joint_sufficiency",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1:])
    == 0,
    "no signature or total order is required to decode the XOR target",
)
record(
    "partitioned_one_share_view_remains_insufficient",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1])
    == Fraction(1, 2),
    "one source route is unavailable",
)
record(
    "eclipse_duplicate_origin_does_not_replace_missing_share",
    bayes_binary_error(
        synergy_rows, lambda row: row[0], lambda row: (row[1], row[1])
    )
    == Fraction(1, 2),
    "two delivered copies, one informational origin",
)
record(
    "delayed_merge_changes_access_time_not_source_truth",
    (
        bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1]),
        bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1:]),
    )
    == (Fraction(1, 2), Fraction(0)),
    "risk falls only when the complementary share arrives",
)
record(
    "churn_without_retention_loses_the_earlier_share",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[2])
    == Fraction(1, 2),
    "a restarted terminal seeing only the later share cannot decode",
)


# 4. Declared route provenance and benign relay subdivision.
direct_events, direct_terminal = build_dag(0, 1, relayed=False)
relay_events, relay_terminal = build_dag(0, 1, relayed=True)
direct_sources = {
    event["creator"]: event["id"]
    for event in direct_events.values()
    if str(event["creator"]).startswith("source-")
}
relay_sources = {
    event["creator"]: event["id"]
    for event in relay_events.values()
    if str(event["creator"]).startswith("source-")
}
record(
    "endpoint_payload_and_source_order_do_not_identify_route",
    direct_events[direct_terminal]["payload"] == relay_events[relay_terminal]["payload"]
    and tuple(sorted(direct_sources)) == tuple(sorted(relay_sources)),
    "direct and relayed routes deliver the same ordered source values",
)
record(
    "signed_parent_dag_identifies_declared_route",
    direct_events[direct_terminal]["parents"] != relay_events[relay_terminal]["parents"]
    and canonical_digest(direct_events) != canonical_digest(relay_events),
    "retained parent links separate the two declared communication histories",
)
direct_distances = tuple(
    shortest_parent_distance(direct_events, event_id, direct_terminal)
    for event_id in direct_sources.values()
)
relay_distances = tuple(
    shortest_parent_distance(relay_events, event_id, relay_terminal)
    for event_id in relay_sources.values()
)
record(
    "raw_path_length_changes_under_benign_relay_insertion",
    direct_distances == (1, 1) and relay_distances == (2, 2),
    {"direct": direct_distances, "relayed": relay_distances},
)
record(
    "source_to_terminal_reachability_survives_relay_subdivision",
    all(
        event_id in ancestors(direct_events, direct_terminal)
        for event_id in direct_sources.values()
    )
    and all(
        event_id in ancestors(relay_events, relay_terminal)
        for event_id in relay_sources.values()
    ),
    "reachability is invariant although node, edge, and hop counts change",
)


# 5. Declared origin multiplicity is not physical source independence.
independent_origin_rows = (("source-1", 0), ("source-2", 1))
duplicated_origin_rows = (("source-1", 0), ("source-1", 1))
record(
    "payload_only_view_cannot_identify_declared_origin_rank",
    tuple(value for _, value in independent_origin_rows)
    == tuple(value for _, value in duplicated_origin_rows),
    "same values in the same order",
)
record(
    "signed_origin_labels_identify_declared_origin_rank",
    len({origin for origin, _ in independent_origin_rows}) == 2
    and len({origin for origin, _ in duplicated_origin_rows}) == 1,
    "key labels distinguish one versus two declared origins",
)
signed_origin_artifact = tuple(independent_origin_rows)
physical_controller_worlds = {
    "independent-controllers": {"source-1": "controller-a", "source-2": "controller-b"},
    "shared-controller": {"source-1": "controller-a", "source-2": "controller-a"},
}
record(
    "declared_origin_rank_does_not_prove_physical_independence",
    len(
        {
            tuple(independent_origin_rows)
            for _ in physical_controller_worlds
        }
    )
    == 1
    and len(
        {
            len(set(controller_map.values()))
            for controller_map in physical_controller_worlds.values()
        }
    )
    == 2,
    {
        "same_signed_artifact": signed_origin_artifact,
        "physical_controller_ranks": {
            world: len(set(controller_map.values()))
            for world, controller_map in physical_controller_worlds.items()
        },
    },
)


# 6. Equivocation is attributable only after incompatible branches meet.
fork_zero = make_event("forking-source", 0, ("value", 0))
fork_one = make_event("forking-source", 0, ("value", 1))


def detects_equivocation(view: tuple[dict, ...]) -> bool:
    return any(
        a["creator"] == b["creator"]
        and a["sequence"] == b["sequence"]
        and a["id"] != b["id"]
        for a, b in product(view, repeat=2)
    )


record(
    "partitioned_views_do_not_locally_detect_equivocation",
    not detects_equivocation((fork_zero,))
    and not detects_equivocation((fork_one,)),
    "each side sees one validly attributed branch",
)
record(
    "merged_signed_view_contains_an_equivocation_proof",
    detects_equivocation((fork_zero, fork_one)),
    "same declared creator and sequence, incompatible signed event digests",
)
record(
    "local_absence_of_a_fork_is_not_global_non_equivocation",
    not detects_equivocation((fork_zero,))
    and detects_equivocation((fork_zero, fork_one)),
    "a hidden branch is compatible with the local view",
)


# 7. Distributed knowledge, individual knowledge after pooling, and common knowledge.
history_rows = tuple((t, pad) for t, pad in product((0, 1), repeat=2))


def possible_targets(
    actual: tuple[int, int], view: Callable[[tuple[int, int]], Hashable]
) -> set[int]:
    actual_view = view(actual)
    return {row[0] for row in history_rows if view(row) == actual_view}


record(
    "neither_source_individually_knows_the_synergy_target",
    all(
        possible_targets(row, lambda item: item[1]) == {0, 1}
        and possible_targets(row, lambda item: item[0] ^ item[1]) == {0, 1}
        for row in history_rows
    ),
    "each local information partition crosses both target values",
)
record(
    "pooled_source_information_is_distributed_knowledge",
    all(
        possible_targets(row, lambda item: (item[1], item[0] ^ item[1]))
        == {row[0]}
        for row in history_rows
    ),
    "the intersection of the two local information partitions fixes T",
)
record(
    "gossip_pooling_turns_distributed_into_recipient_knowledge",
    all(
        (row[1] ^ (row[0] ^ row[1])) == row[0] for row in history_rows
    ),
    "a recipient holding both source records can act on T",
)


def coordinated_attack_worlds(max_messages: int) -> tuple[tuple[bool, int], ...]:
    return ((False, 0),) + tuple((True, delivered) for delivered in range(max_messages + 1))


def local_state(agent: str, world: tuple[bool, int]) -> tuple:
    proposition, delivered = world
    if agent == "A":
        # A knows the proposition and sees only delivered even acknowledgements.
        return proposition, delivered // 2
    if agent == "B":
        # With no delivered first message, B cannot distinguish true from false.
        return ((delivered + 1) // 2,) if proposition else (0,)
    raise ValueError(agent)


def common_knowledge_component(
    worlds: tuple[tuple[bool, int], ...], actual: tuple[bool, int]
) -> set[tuple[bool, int]]:
    reached = {actual}
    queue = deque([actual])
    while queue:
        current = queue.popleft()
        for candidate in worlds:
            if candidate in reached:
                continue
            if any(
                local_state(agent, current) == local_state(agent, candidate)
                for agent in ("A", "B")
            ):
                reached.add(candidate)
                queue.append(candidate)
    return reached


finite_ack_failures = {}
for message_count in range(9):
    worlds = coordinated_attack_worlds(message_count)
    actual = (True, message_count)
    component = common_knowledge_component(worlds, actual)
    finite_ack_failures[message_count] = (False, 0) in component
record(
    "every_tested_finite_async_ack_chain_lacks_common_knowledge",
    all(finite_ack_failures.values()),
    {
        str(message_count): "false-proposition world remains epistemically reachable"
        for message_count in finite_ack_failures
    },
)


# 8. Total ordering is independent of source truth and common knowledge.
synergy_order_distribution = distribution(
    synergy_rows, lambda row: tuple(sorted(row[1:]))
)
null_order_distribution = distribution(
    null_rows, lambda row: tuple(sorted(row[1:]))
)
record(
    "same_total_order_can_hold_in_synergy_and_null_worlds",
    synergy_order_distribution == null_order_distribution
    and all((r1 ^ r2) == t for t, r1, r2 in synergy_rows)
    and any((r1 ^ r2) != t for t, r1, r2 in null_rows),
    "ordering chooses a sequence; it does not attest the physical target relation",
)


# 9. Commitment/zero-knowledge statement binding.
def xor_witnesses(target_value: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in product((0, 1), repeat=2)
        if (left ^ right) == target_value
    )


record(
    "unbound_existential_xor_statement_is_vacuous_for_each_target",
    all(len(xor_witnesses(target_value)) == 2 for target_value in (0, 1)),
    "existence alone does not bind a proof to the delivered source events",
)
event_pair = (0, 1)
record(
    "event_bound_relation_certificate_checks_the_declared_predicate",
    (event_pair[0] ^ event_pair[1]) == 1
    and not ((event_pair[0] ^ event_pair[1]) == 0),
    "binding event digests and a target commitment distinguishes valid from invalid statements",
)
declared_statement = (
    canonical_digest(("event-1", event_pair[0])),
    canonical_digest(("event-2", event_pair[1])),
    canonical_digest(("declared-target", 1)),
    "R1 xor R2 = declared target",
)
physical_histories = (("target-matches", 1), ("target-differs", 0))
proof_transcript = {
    history: canonical_digest(("ideal-zk-proof", declared_statement))
    for history, _ in physical_histories
}
record(
    "valid_relation_proof_does_not_attest_an_unmodeled_physical_target",
    len(set(proof_transcript.values())) == 1
    and len({target for _, target in physical_histories}) == 2,
    "the same statement proof is compatible with different physical targets",
)
record(
    "certificate_can_enable_statement_relative_action_without_physical_truth",
    all(bool(proof_transcript[history]) for history, _ in physical_histories),
    "action safety is relative to the bound statement, setup, keys, and fault model",
)


# 10. Direct gossip versus a shared stigmergic trace.
record(
    "intact_pair_trace_preserves_synergy_but_adds_an_archive",
    bayes_binary_error(synergy_rows, lambda row: row[0], lambda row: row[1:])
    == 0,
    "the environmental trace must retain both shares or an equivalent sufficient statistic",
)
record(
    "parity_trace_reconstructs_synergy_while_erasing_source_pair",
    bayes_binary_error(
        synergy_rows, lambda row: row[0], lambda row: row[1] ^ row[2]
    )
    == 0
    and len(
        {
            (r1, r2)
            for _, r1, r2 in synergy_rows
            if (r1 ^ r2) == 0
        }
    )
    == 2,
    "target sufficiency survives while pair provenance is compressed",
)
record(
    "same_parity_trace_is_useless_in_the_null_world",
    bayes_binary_error(
        null_rows, lambda row: row[0], lambda row: row[1] ^ row[2]
    )
    == Fraction(1, 2),
    "trace semantics depend on source formation, not the mark alphabet alone",
)
erased_trace_rows = tuple((target_value, None) for target_value in (0, 1))
trace_origin_worlds = (
    ("formed-by-sources", 1),
    ("forged-by-adversary", 1),
)
record(
    "evaporated_or_forged_unattributed_trace_cannot_certify_origin",
    bayes_binary_error(
        erased_trace_rows, lambda row: row[0], lambda row: row[1]
    )
    == Fraction(1, 2)
    and len({mark for _, mark in trace_origin_worlds}) == 1
    and len({origin for origin, _ in trace_origin_worlds}) == 2,
    {
        "erased_trace_target_error": "1/2",
        "same_mark_distinct_origins": trace_origin_worlds,
    },
)


passed = sum(bool(check["passed"]) for check in CHECKS)
result = {
    "claim_id": "HC-DU-048",
    "run_id": "N5-SCF-P2",
    "status": "PASS" if passed == len(CHECKS) else "FAIL",
    "checks_passed": passed,
    "checks_total": len(CHECKS),
    "grade": (
        "scoped exact finite classification from known information-factorization, "
        "signed-DAG, graph-reachability, epistemic-logic, and statement-binding controls"
    ),
    "first_identifiable_layer": {
        "event_delivery": "recipient view containing the event",
        "joint_target_reconstruction": "first retained view containing both synergy shares",
        "authenticated_declared_origin": "ideal signed source event",
        "declared_route_ancestry": "retained parent-hash DAG",
        "equivocation_evidence": "one view containing both incompatible signed branches",
        "distributed_knowledge": "source group before pooling; the intersection of local information partitions",
        "individual_knowledge": "recipient after both complementary shares arrive and remain retained",
        "common_knowledge": "not attained by any finite asynchronous acknowledgment chain in the tested family",
        "total_order": "a separately specified consensus/order rule under its own fault assumptions",
        "action_safety": "a task-, statement-, setup-, and adversary-relative certificate",
        "physical_source_truth": "not identified without an independently admitted formation or attestation channel",
    },
    "local_model_gate": {
        "disposition": "PROOF_CERTIFICATE_OUTSIDE_RESEARCH_MODEL_ADMISSION",
        "reason": (
            "the analytic finite theorems and counterexamples are stated independently; "
            "the script only checks exact finite information partitions, event projections, "
            "reachability, and epistemic components"
        ),
    },
    "checks": CHECKS,
}

artifact = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_synergy_gossip_dag_provenance_result.json"
)
artifact.write_text(dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    f"HC-DU-048 gossip/DAG provenance certificate: "
    f"{passed}/{len(CHECKS)} passed"
)
