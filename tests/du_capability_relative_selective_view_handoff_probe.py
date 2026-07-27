#!/usr/bin/env python3
"""Exact regression certificate for HC-DU-050.

The analytic result is in:
  explorations/capability-relative-selective-views-and-regional-handoff-2026-07-27.md

This probe exhausts finite history spaces and view projections. It is a
proof/regression certificate, not a database, MMO, consensus, cryptographic,
networking, or physical implementation.
"""

from __future__ import annotations

from itertools import combinations, product
from json import dumps
from pathlib import Path
from typing import Callable, Hashable, Iterable


CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})
    if not passed:
        raise AssertionError(f"{name}: {detail}")


def factorizes(
    rows: Iterable[dict[str, object]],
    view: Callable[[dict[str, object]], Hashable],
    target: Callable[[dict[str, object]], Hashable],
) -> bool:
    value_by_view: dict[Hashable, Hashable] = {}
    for row in rows:
        visible = view(row)
        target_value = target(row)
        if visible in value_by_view and value_by_view[visible] != target_value:
            return False
        value_by_view[visible] = target_value
    return True


def projection(fields: tuple[str, ...]) -> Callable[[dict[str, object]], tuple]:
    return lambda row: tuple(row[field] for field in fields)


def all_subsets(fields: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(
        subset
        for size in range(len(fields) + 1)
        for subset in combinations(fields, size)
    )


def minimal_sufficient_bundles(
    rows: tuple[dict[str, object], ...],
    fields: tuple[str, ...],
    target: Callable[[dict[str, object]], Hashable],
) -> tuple[tuple[str, ...], ...]:
    sufficient = {
        subset
        for subset in all_subsets(fields)
        if factorizes(rows, projection(subset), target)
    }
    minimal = tuple(
        subset
        for subset in sufficient
        if not any(
            set(other) < set(subset)
            for other in sufficient
        )
    )
    return tuple(sorted(minimal, key=lambda item: (len(item), item)))


def equivalence_partition(
    rows: tuple[dict[str, object], ...],
    targets: tuple[Callable[[dict[str, object]], Hashable], ...],
) -> tuple[tuple[int, ...], ...]:
    classes: dict[tuple[Hashable, ...], list[int]] = {}
    for index, row in enumerate(rows):
        signature = tuple(target(row) for target in targets)
        classes.setdefault(signature, []).append(index)
    return tuple(sorted(tuple(indices) for indices in classes.values()))


def refines(
    fine: tuple[tuple[int, ...], ...],
    coarse: tuple[tuple[int, ...], ...],
) -> bool:
    coarse_sets = tuple(set(block) for block in coarse)
    return all(
        any(set(fine_block).issubset(coarse_block) for coarse_block in coarse_sets)
        for fine_block in fine
    )


# 1. Frozen action-independent history space.
#
# The independently formed source attestation is intentionally typed apart
# from every distributed-protocol field. It equals the physical target only
# in this positive source-bound control.
history_rows = tuple(
    {
        "tentative_preference": tentative,
        "decision": decision,
        "certificate_valid": certificate_valid,
        "epoch_current": epoch_current,
        "signer_subset": ("A", "B", "C", "D", signer_variant),
        "fork_committed": fork_committed,
        "sidecar_available": sidecar_available,
        "physical_target": physical_target,
        "source_attestation": physical_target,
        "route": route,
    }
    for (
        tentative,
        decision,
        certificate_valid,
        epoch_current,
        signer_variant,
        fork_committed,
        sidecar_available,
        physical_target,
        route,
    ) in product(
        (0, 1),
        (0, 1),
        (False, True),
        (False, True),
        ("E", "F"),
        (False, True),
        (False, True),
        (0, 1),
        ("direct", "relayed"),
    )
)

VIEW_FIELDS = (
    "tentative_preference",
    "decision",
    "certificate_valid",
    "epoch_current",
    "signer_subset",
    "fork_committed",
    "sidecar_available",
    "source_attestation",
    "route",
)


def tentative_response(row: dict[str, object]) -> object:
    return row["tentative_preference"]


def safe_execution(row: dict[str, object]) -> object:
    if row["certificate_valid"] and row["epoch_current"]:
        return ("EXECUTE", row["decision"])
    return ("HOLD",)


def signer_accountability(row: dict[str, object]) -> object:
    if row["certificate_valid"]:
        return ("CERTIFIED_SIGNERS", row["signer_subset"])
    return ("NO_VALID_CERTIFICATE",)


def equivocation_proof_ready(row: dict[str, object]) -> object:
    return bool(row["fork_committed"] and row["sidecar_available"])


def physical_source_truth(row: dict[str, object]) -> object:
    return row["physical_target"]


expected_minima = {
    "tentative_response": (("tentative_preference",),),
    "safe_execution": (
        ("decision", "certificate_valid", "epoch_current"),
    ),
    "signer_accountability": (
        ("certificate_valid", "signer_subset"),
    ),
    "equivocation_proof_ready": (
        ("fork_committed", "sidecar_available"),
    ),
    "physical_source_truth": (("source_attestation",),),
}
computed_minima = {
    "tentative_response": minimal_sufficient_bundles(
        history_rows, VIEW_FIELDS, tentative_response
    ),
    "safe_execution": minimal_sufficient_bundles(
        history_rows, VIEW_FIELDS, safe_execution
    ),
    "signer_accountability": minimal_sufficient_bundles(
        history_rows, VIEW_FIELDS, signer_accountability
    ),
    "equivocation_proof_ready": minimal_sufficient_bundles(
        history_rows, VIEW_FIELDS, equivocation_proof_ready
    ),
    "physical_source_truth": minimal_sufficient_bundles(
        history_rows, VIEW_FIELDS, physical_source_truth
    ),
}
record(
    "exhaustive_minimum_views_match_the_five_frozen_action_classes",
    computed_minima == expected_minima,
    computed_minima,
)
record(
    "route_is_not_required_for_any_frozen_action",
    all(
        all("route" not in bundle for bundle in bundles)
        for bundles in computed_minima.values()
    ),
    "route forensics is a separate action target, not universal payload",
)


# 2. Multiple incomparable implementations can realize one semantic action
# quotient. The unique object is the target partition, not one wire format.
def explicit_qc_view(row: dict[str, object]) -> tuple:
    return (
        row["decision"],
        row["certificate_valid"],
        row["epoch_current"],
        ("individual-signatures", row["signer_subset"]),
    )


def threshold_qc_view(row: dict[str, object]) -> tuple:
    return (
        row["decision"],
        row["certificate_valid"],
        row["epoch_current"],
        "group-signature-valid",
    )


record(
    "explicit_and_threshold_certificates_both_support_execution",
    factorizes(history_rows, explicit_qc_view, safe_execution)
    and factorizes(history_rows, threshold_qc_view, safe_execution),
    "two different payload schemas implement the same execution quotient",
)
record(
    "threshold_execution_view_does_not_support_signer_accountability",
    not factorizes(history_rows, threshold_qc_view, signer_accountability),
    "execution sufficiency does not imply audit sufficiency",
)
record(
    "explicit_qc_view_supports_signer_accountability",
    factorizes(history_rows, explicit_qc_view, signer_accountability),
    "retaining individual signer identities changes the audit capability",
)


# 3. Capability expansion refines finality.
execution_partition = equivalence_partition(history_rows, (safe_execution,))
execution_audit_partition = equivalence_partition(
    history_rows,
    (safe_execution, signer_accountability, equivocation_proof_ready),
)
full_capability_partition = equivalence_partition(
    history_rows,
    (
        safe_execution,
        signer_accountability,
        equivocation_proof_ready,
        physical_source_truth,
    ),
)
record(
    "adding_audit_capabilities_strictly_refines_execution_equivalence",
    refines(execution_audit_partition, execution_partition)
    and len(execution_audit_partition) > len(execution_partition),
    {
        "execution_classes": len(execution_partition),
        "execution_plus_audit_classes": len(execution_audit_partition),
    },
)
record(
    "adding_physical_adjudication_strictly_refines_protocol_audit_equivalence",
    refines(full_capability_partition, execution_audit_partition)
    and len(full_capability_partition) > len(execution_audit_partition),
    {
        "protocol_capability_classes": len(execution_audit_partition),
        "physical_capability_classes": len(full_capability_partition),
    },
)


# 4. Selective regional views can be locally sufficient without reconstructing
# one globally replicated history.
def region_execution_view(row: dict[str, object]) -> tuple:
    return (
        row["decision"],
        row["certificate_valid"],
        row["epoch_current"],
    )


def region_audit_view(row: dict[str, object]) -> tuple:
    return (
        row["fork_committed"],
        row["sidecar_available"],
    )


def full_history_target(row: dict[str, object]) -> tuple:
    return tuple(row[key] for key in sorted(row))


record(
    "region_execution_view_is_locally_action_sufficient",
    factorizes(history_rows, region_execution_view, safe_execution),
    "the region need not replicate signer, fork, route, or source fields",
)
record(
    "region_audit_view_is_locally_action_sufficient",
    factorizes(history_rows, region_audit_view, equivocation_proof_ready),
    "the audit region need not replicate decision or route fields",
)
record(
    "neither_local_view_reconstructs_the_global_history",
    not factorizes(history_rows, region_execution_view, full_history_target)
    and not factorizes(history_rows, region_audit_view, full_history_target),
    "local action closure is weaker than global history reconstruction",
)


def attributable_fork_target(row: dict[str, object]) -> object:
    if equivocation_proof_ready(row) and row["certificate_valid"]:
        return ("ATTRIBUTABLE_FORK", row["signer_subset"])
    return ("NO_ATTRIBUTABLE_FORK_PACKET",)


def region_joint_view(row: dict[str, object]) -> tuple:
    return region_execution_view(row), explicit_qc_view(row), region_audit_view(row)


record(
    "individual_regional_views_are_insufficient_for_attributable_fork_audit",
    not factorizes(history_rows, region_execution_view, attributable_fork_target)
    and not factorizes(history_rows, region_audit_view, attributable_fork_target),
    "individual insufficiency does not settle joint sufficiency",
)
record(
    "joined_regional_views_support_attributable_fork_audit",
    factorizes(history_rows, region_joint_view, attributable_fork_target),
    "complementary views can create a stronger joint capability",
)


# 5. Commitment binding and evidence availability are distinct.
availability_histories = (
    {
        "certificate": ("m", "qc-valid"),
        "provenance_root": "root-with-fork",
        "sidecar_available": False,
        "can_produce_proof": False,
    },
    {
        "certificate": ("m", "qc-valid"),
        "provenance_root": "root-with-fork",
        "sidecar_available": True,
        "can_produce_proof": True,
    },
)
record(
    "same_certificate_and_commitment_do_not_identify_proof_availability",
    not factorizes(
        availability_histories,
        lambda row: (row["certificate"], row["provenance_root"]),
        lambda row: row["can_produce_proof"],
    ),
    "binding is not retrieval",
)
record(
    "availability_bit_repairs_the_frozen_proof_production_target",
    factorizes(
        availability_histories,
        lambda row: (
            row["certificate"],
            row["provenance_root"],
            row["sidecar_available"],
        ),
        lambda row: row["can_produce_proof"],
    ),
    "the receiver still needs an access path and valid openings in a real protocol",
)


# 6. Epoch and membership context are part of a safe handoff.
epoch_histories = (
    {
        "group_record": ("group-key", "m", "valid"),
        "signed_epoch": 0,
        "receiver_epoch": 0,
        "receiver_decoder": True,
    },
    {
        "group_record": ("group-key", "m", "valid"),
        "signed_epoch": 0,
        "receiver_epoch": 1,
        "receiver_decoder": True,
    },
)


def handoff_execution_target(row: dict[str, object]) -> object:
    if row["receiver_decoder"] and row["signed_epoch"] == row["receiver_epoch"]:
        return ("EXECUTE", "m")
    return ("HOLD",)


record(
    "compact_group_record_without_epoch_context_is_not_handoff_sufficient",
    not factorizes(
        epoch_histories,
        lambda row: row["group_record"],
        handoff_execution_target,
    ),
    "the same group-key verification record can be current or stale",
)
record(
    "epoch_bound_record_plus_receiver_context_is_handoff_sufficient",
    factorizes(
        epoch_histories,
        lambda row: (
            row["group_record"],
            row["signed_epoch"],
            row["receiver_epoch"],
            row["receiver_decoder"],
        ),
        handoff_execution_target,
    ),
    "receiver context is part of the factorization domain",
)


# 7. A feedback-selected interest view can be self-confirming.
adaptive_histories = (
    {
        "initial_preference": 0,
        "events": (("support", 0),),
        "correct_action": 0,
    },
    {
        "initial_preference": 0,
        "events": (("support", 0), ("correction", 1)),
        "correct_action": 1,
    },
)


def self_confirming_filter(row: dict[str, object]) -> tuple:
    preference = row["initial_preference"]
    return tuple(event for event in row["events"] if event[1] == preference)


def complete_declared_effect_filter(row: dict[str, object]) -> tuple:
    return tuple(row["events"])


record(
    "adaptive_self_confirming_filter_hides_the_corrective_event",
    not factorizes(
        adaptive_histories,
        self_confirming_filter,
        lambda row: row["correct_action"],
    )
    and self_confirming_filter(adaptive_histories[0])
    == self_confirming_filter(adaptive_histories[1]),
    "a policy driven by its current preference can create an eclipse",
)
record(
    "complete_action_relevant_effect_view_repairs_this_hostile_pair",
    factorizes(
        adaptive_histories,
        complete_declared_effect_filter,
        lambda row: row["correct_action"],
    ),
    "this is a frozen finite control, not a universal interest-management rule",
)


# 8. Monotone positive evidence and nonmonotone absence.
signed_a = ("signed", "height-0", "A")
signed_b = ("signed", "height-0", "B")
history_chain = (
    frozenset(),
    frozenset({signed_a}),
    frozenset({signed_a, signed_b}),
)


def has_positive_fork(events: frozenset[tuple[str, str, str]]) -> bool:
    values = {event[2] for event in events if event[:2] == ("signed", "height-0")}
    return len(values) >= 2


def no_fork_seen(events: frozenset[tuple[str, str, str]]) -> bool:
    return not has_positive_fork(events)


def monotone_on_extensions(predicate: Callable[[frozenset], bool]) -> bool:
    return all(
        not predicate(left) or predicate(right)
        for left in history_chain
        for right in history_chain
        if left.issubset(right)
    )


record(
    "positive_signed_equivocation_evidence_is_monotone_under_extension",
    monotone_on_extensions(has_positive_fork),
    "later records cannot erase an already witnessed signed fork",
)
record(
    "absence_of_equivocation_is_not_monotone_under_extension",
    not monotone_on_extensions(no_fork_seen),
    "a later conflicting branch can reopen an earlier clean-looking view",
)


# 9. Capability/interest expansion reveals the first omitted distinction.
small_interest_view = lambda row: (row["initial_preference"], self_confirming_filter(row))
expanded_interest_view = lambda row: (
    row["initial_preference"],
    complete_declared_effect_filter(row),
)
record(
    "interest_expansion_strictly_refines_the_hostile_pair",
    small_interest_view(adaptive_histories[0])
    == small_interest_view(adaptive_histories[1])
    and expanded_interest_view(adaptive_histories[0])
    != expanded_interest_view(adaptive_histories[1]),
    {
        "small_view": small_interest_view(adaptive_histories[0]),
        "expanded_views": tuple(expanded_interest_view(row) for row in adaptive_histories),
    },
)


# 10. Local prediction, rollback, and cross-shard invariant controls.
motion_histories = (
    {
        "last_position": 0,
        "last_velocity": 1,
        "hidden_acceleration": 0,
        "next_position": 1,
    },
    {
        "last_position": 0,
        "last_velocity": 1,
        "hidden_acceleration": 1,
        "next_position": 2,
    },
)
record(
    "dead_reckoning_view_is_not_exact_next_state_finality",
    not factorizes(
        motion_histories,
        lambda row: (row["last_position"], row["last_velocity"]),
        lambda row: row["next_position"],
    ),
    "equal position and velocity can hide a target-changing acceleration",
)
record(
    "authoritative_acceleration_handoff_repairs_the_motion_pair",
    factorizes(
        motion_histories,
        lambda row: (
            row["last_position"],
            row["last_velocity"],
            row["hidden_acceleration"],
        ),
        lambda row: row["next_position"],
    ),
    "a local predictor may remain useful for reversible display before correction",
)

rollback_histories = (
    {
        "tentative_preference": 0,
        "certified_decision": 0,
        "certificate_valid": True,
    },
    {
        "tentative_preference": 0,
        "certified_decision": 1,
        "certificate_valid": True,
    },
)
record(
    "tentative_view_closes_reversible_response_not_irreversible_handoff",
    factorizes(
        rollback_histories,
        lambda row: row["tentative_preference"],
        lambda row: ("DISPLAY", row["tentative_preference"]),
    )
    and not factorizes(
        rollback_histories,
        lambda row: row["tentative_preference"],
        lambda row: ("EXECUTE", row["certified_decision"]),
    )
    and factorizes(
        rollback_histories,
        lambda row: (
            row["tentative_preference"],
            row["certified_decision"],
            row["certificate_valid"],
        ),
        lambda row: (
            "ROLLBACK_REQUIRED",
            row["tentative_preference"] != row["certified_decision"],
        ),
    ),
    "handoff can preserve local responsiveness by making rollback explicit",
)

shard_histories = tuple(
    {
        "shard_a_allocation": shard_a,
        "shard_b_allocation": shard_b,
    }
    for shard_a, shard_b in product((0, 1), repeat=2)
)
global_quota_safe = lambda row: (
    row["shard_a_allocation"] + row["shard_b_allocation"] <= 1
)
record(
    "partitioned_shards_do_not_close_a_nonlocal_quota_without_joint_state",
    not factorizes(
        shard_histories,
        lambda row: row["shard_a_allocation"],
        global_quota_safe,
    )
    and not factorizes(
        shard_histories,
        lambda row: row["shard_b_allocation"],
        global_quota_safe,
    )
    and factorizes(
        shard_histories,
        lambda row: (
            row["shard_a_allocation"],
            row["shard_b_allocation"],
        ),
        global_quota_safe,
    ),
    "local closure is action-relative; a cross-shard invariant can still require coordination",
)


# 11. Physical truth remains outside every protocol-only selective view.
null_source_rows = tuple(
    {
        "physical_target": physical_target,
        "decision": left ^ right,
        "certificate": ("qc-valid", left, right, left ^ right),
        "signers": ("A", "B", "C", "D", "E"),
        "epoch": 0,
        "provenance_root": ("root", left, right),
        "sidecar_available": True,
    }
    for physical_target, left, right in product((0, 1), repeat=3)
)


def complete_protocol_view(row: dict[str, object]) -> tuple:
    return (
        row["decision"],
        row["certificate"],
        row["signers"],
        row["epoch"],
        row["provenance_root"],
        row["sidecar_available"],
    )


record(
    "complete_protocol_selective_view_does_not_adjudicate_null_physical_target",
    not factorizes(
        null_source_rows,
        complete_protocol_view,
        lambda row: row["physical_target"],
    ),
    "no downstream handoff can mint a source relation absent from its admitted input",
)


# 12. Typed handoff theorem and first-failure controls.
HANDOFF_PREMISES = (
    "sender_action_sufficiency",
    "certificate_semantics_aligned",
    "epoch_membership_bound",
    "commitment_binding",
    "required_evidence_available",
    "receiver_decoder_and_access",
    "capability_contract_frozen",
    "target_present_in_admitted_input",
)


def handoff_disposition(contract: dict[str, bool]) -> str:
    for premise in HANDOFF_PREMISES:
        if not contract[premise]:
            return f"FAIL:{premise}"
    return "CAPABILITY_RELATIVE_SAFE_REGIONAL_HANDOFF"


complete_contract = {premise: True for premise in HANDOFF_PREMISES}
record(
    "complete_typed_contract_returns_capability_relative_safe_handoff",
    handoff_disposition(complete_contract)
    == "CAPABILITY_RELATIVE_SAFE_REGIONAL_HANDOFF",
    HANDOFF_PREMISES,
)
first_failure_controls = {}
for failed_premise in HANDOFF_PREMISES:
    hostile_contract = dict(complete_contract)
    hostile_contract[failed_premise] = False
    first_failure_controls[failed_premise] = handoff_disposition(hostile_contract)
record(
    "each_missing_handoff_premise_returns_its_first_typed_failure",
    all(
        disposition == f"FAIL:{premise}"
        for premise, disposition in first_failure_controls.items()
    ),
    first_failure_controls,
)


passed = sum(bool(check["passed"]) for check in CHECKS)
result = {
    "claim_id": "HC-DU-050",
    "run_id": "N5-SCF-P4",
    "status": "PASS" if passed == len(CHECKS) else "FAIL",
    "checks_passed": passed,
    "checks_total": len(CHECKS),
    "history_rows_exhausted": len(history_rows),
    "minimum_views": {
        action: [list(bundle) for bundle in bundles]
        for action, bundles in computed_minima.items()
    },
    "capability_equivalence_classes": {
        "execution": len(execution_partition),
        "execution_plus_protocol_audit": len(execution_audit_partition),
        "execution_protocol_audit_plus_physical_adjudication": len(
            full_capability_partition
        ),
    },
    "return": (
        "CAPABILITY_RELATIVE_SELECTIVE_VIEW_AND_REGIONAL_HANDOFF_THEOREM_"
        "WITH_AVAILABILITY_EPOCH_AND_MONOTONICITY_BOUNDARIES"
    ),
    "first_identifiable_layer": {
        "tentative_response": ["tentative_preference"],
        "conflict_safe_execution": [
            "decision",
            "certificate_valid",
            "epoch_current",
        ],
        "signer_accountability": ["certificate_valid", "signer_subset"],
        "equivocation_proof_production": [
            "fork_committed",
            "sidecar_available",
        ],
        "physical_source_adjudication": ["independent_source_attestation"],
        "regional_handoff": list(HANDOFF_PREMISES),
    },
    "local_model_gate": {
        "disposition": "PROOF_CERTIFICATE_OUTSIDE_RESEARCH_MODEL_ADMISSION",
        "reason": (
            "the finite factorization statements and explicit counterexamples "
            "are analytic; the script only exhausts their fibres, view bundles, "
            "equivalence refinements, and first-failure controls"
        ),
    },
    "next_work": "N5-SCF-P5",
    "checks": CHECKS,
}

artifact = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_capability_relative_selective_view_handoff_result.json"
)
artifact.write_text(dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    "HC-DU-050 capability-relative selective-view/handoff certificate: "
    f"{passed}/{len(CHECKS)} passed"
)
