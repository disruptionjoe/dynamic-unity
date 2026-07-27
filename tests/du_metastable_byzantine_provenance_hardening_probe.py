#!/usr/bin/env python3
"""Exact regression certificate for HC-DU-049.

The analytic result is in:
  explorations/metastable-to-byzantine-hardening-and-provenance-lift-2026-07-27.md

This probe uses exact finite sets, rational arithmetic, and idealized
cryptographic labels. It is a proof/regression certificate, not an Avalanche,
BFT, HotStuff, threshold-signature, DKG, ZK, MPC, or physical implementation.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from json import dumps
from math import comb
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
    rows: Iterable[object],
    observable: Callable[[object], Hashable],
) -> dict[Hashable, Fraction]:
    rows = tuple(rows)
    counts = Counter(observable(row) for row in rows)
    return {key: Fraction(count, len(rows)) for key, count in counts.items()}


def bayes_binary_error(
    rows: Iterable[object],
    target: Callable[[object], int],
    observable: Callable[[object], Hashable],
) -> Fraction:
    rows = tuple(rows)
    joint = Counter((target(row), observable(row)) for row in rows)
    values = {observable(row) for row in rows}
    return sum(
        Fraction(min(joint[(0, value)], joint[(1, value)]), len(rows))
        for value in values
    )


def factorizes(
    rows: Iterable[object],
    certificate: Callable[[object], Hashable],
    target: Callable[[object], Hashable],
) -> bool:
    value_by_certificate: dict[Hashable, Hashable] = {}
    for row in rows:
        cert = certificate(row)
        target_value = target(row)
        if cert in value_by_certificate and value_by_certificate[cert] != target_value:
            return False
        value_by_certificate[cert] = target_value
    return True


def canonical_digest(value: object) -> str:
    encoded = dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


# 1. Exact Avalanche-like sampling control.
N = 7
F = 2
K = 3
ALPHA = 2
BETA = 3
wrong_nodes = frozenset({0, 1})
samples = tuple(combinations(range(N), K))
wrong_samples = tuple(
    sample for sample in samples if len(set(sample) & wrong_nodes) >= ALPHA
)
single_wrong_probability = Fraction(len(wrong_samples), len(samples))
formula_probability = Fraction(
    sum(
        comb(F, wrong_count) * comb(N - F, K - wrong_count)
        for wrong_count in range(ALPHA, K + 1)
        if wrong_count <= F and K - wrong_count <= N - F
    ),
    comb(N, K),
)
record(
    "exact_wrong_sample_probability_is_one_seventh",
    single_wrong_probability == formula_probability == Fraction(1, 7),
    {
        "wrong_samples": len(wrong_samples),
        "all_samples": len(samples),
        "probability": fraction_text(single_wrong_probability),
    },
)
record(
    "three_independent_wrong_samples_have_probability_one_over_343",
    single_wrong_probability**BETA == Fraction(1, 343),
    fraction_text(single_wrong_probability**BETA),
)
record(
    "reused_correlated_neighborhood_does_not_multiply_confidence",
    single_wrong_probability != single_wrong_probability**BETA
    and single_wrong_probability == Fraction(1, 7),
    "one sampled neighborhood repeated three times remains one draw",
)
record(
    "complete_eclipse_makes_wrong_local_confidence_certain",
    all(sum(response for response in (1, 1, 1)) >= ALPHA for _ in range(BETA)),
    "all three rounds return three wrong-preference responses",
)
left_partition_rounds = ((0, 0, 0),) * BETA
right_partition_rounds = ((1, 1, 1),) * BETA
record(
    "partitioned_views_can_reach_opposite_local_confidence",
    all(sum(value == 0 for value in sample) >= ALPHA for sample in left_partition_rounds)
    and all(
        sum(value == 1 for value in sample) >= ALPHA
        for sample in right_partition_rounds
    ),
    "local confidence is not a global conflicting-certificate exclusion",
)


# 2. Exact quorum intersection, lock, and liveness controls.
Q = 5
validators = tuple(range(N))
quorums = tuple(combinations(validators, Q))
minimum_intersection = min(
    len(set(left) & set(right)) for left, right in product(quorums, repeat=2)
)
record(
    "five_of_seven_quorums_intersect_in_at_least_three",
    minimum_intersection == 2 * Q - N == 3,
    {"minimum_intersection": minimum_intersection, "fault_bound": F},
)
record(
    "every_quorum_pair_has_an_honest_intersection_under_two_faults",
    all(
        any(
            signer not in byzantine
            for signer in set(left) & set(right)
        )
        for byzantine in combinations(validators, F)
        for left, right in product(quorums, repeat=2)
    ),
    "intersection size 3 exceeds the two-validator Byzantine budget",
)
record(
    "honest_non_conflicting_lock_excludes_two_conflicting_quorums",
    not any(
        (set(left) & set(right)).issubset(set(byzantine))
        for byzantine in combinations(validators, F)
        for left, right in product(quorums, repeat=2)
    ),
    "two conflicting certificates would require an honest double-sign",
)
same_quorum = quorums[0]
unlocked_conflicting_authorizations = (
    {"proposal": 0, "signers": same_quorum},
    {"proposal": 1, "signers": same_quorum},
)
record(
    "threshold_count_without_a_lock_does_not_exclude_conflicting_certificates",
    len({item["proposal"] for item in unlocked_conflicting_authorizations}) == 2
    and all(
        len(item["signers"]) >= Q
        for item in unlocked_conflicting_authorizations
    ),
    {
        "authorizations": unlocked_conflicting_authorizations,
        "missing_premise": "correct validators must not sign conflicting locked proposals",
    },
)
partition = (set(range(4)), set(range(4, 7)))
record(
    "four_three_partition_preserves_safety_but_blocks_liveness",
    all(len(component) < Q for component in partition),
    {"component_sizes": tuple(len(component) for component in partition), "quorum": Q},
)
honest_validators = set(range(5))
record(
    "five_available_honest_validators_can_form_a_quorum",
    len(honest_validators) == Q,
    "the two Byzantine validators may withhold without preventing this certificate",
)
record(
    "one_more_honest_outage_plus_byzantine_withholding_blocks_progress",
    len(honest_validators - {4}) == Q - 1,
    "four available honest votes are below the five-vote quorum",
)


# 3. Matched source-bound and null proposal/certificate worlds.
# Rows are (physical target, share 1, share 2).
source_bound_rows = tuple((target, pad, target ^ pad) for target, pad in product((0, 1), repeat=2))
null_rows = tuple(product((0, 1), repeat=3))


def proposal(row: tuple[int, int, int]) -> tuple:
    _, left, right = row
    declared = left ^ right
    return (
        "epoch-0",
        "height-0",
        canonical_digest(("source-1", left)),
        canonical_digest(("source-2", right)),
        declared,
        "xor-relation-v1",
    )


def explicit_qc(row: tuple[int, int, int]) -> tuple:
    return proposal(row), quorums[0], "locked-qc-valid"


record(
    "source_bound_and_null_worlds_have_the_same_proposal_law",
    distribution(source_bound_rows, proposal) == distribution(null_rows, proposal),
    "the complete pair and its declared XOR have the same law",
)
record(
    "source_bound_and_null_worlds_have_the_same_hardened_certificate_law",
    distribution(source_bound_rows, explicit_qc)
    == distribution(null_rows, explicit_qc),
    "fixed validators, votes, lock, and certificate depend only on the proposal",
)
record(
    "declared_xor_validity_passes_in_both_source_worlds",
    all((row[1] ^ row[2]) == proposal(row)[4] for row in source_bound_rows + null_rows),
    "proposal validity is not physical target binding",
)
record(
    "physical_target_binding_is_exact_only_in_the_source_bound_world",
    bayes_binary_error(source_bound_rows, lambda row: row[0], proposal) == 0
    and bayes_binary_error(null_rows, lambda row: row[0], proposal)
    == Fraction(1, 2),
    {
        "source_bound_error": "0/1",
        "null_error": "1/2",
    },
)
record(
    "five_validator_endorsements_do_not_improve_null_source_truth",
    bayes_binary_error(null_rows, lambda row: row[0], explicit_qc)
    == Fraction(1, 2),
    "agreement hardens the declared proposal, not the omitted physical relation",
)


# 4. Validator quorum is distinct from source/controller independence.
controller_histories = (
    {
        "artifact": ("source-key-1", "source-key-2", quorums[0]),
        "controller_map": (("source-key-1", "device-a"), ("source-key-2", "device-b")),
    },
    {
        "artifact": ("source-key-1", "source-key-2", quorums[0]),
        "controller_map": (("source-key-1", "device-a"), ("source-key-2", "device-a")),
    },
)


def controller_rank(row: dict[str, object]) -> int:
    return len({controller for _, controller in row["controller_map"]})


record(
    "explicit_validator_and_source_key_sets_do_not_identify_controller_rank",
    not factorizes(
        controller_histories,
        lambda row: row["artifact"],
        controller_rank,
    ),
    {
        "same_artifact": controller_histories[0]["artifact"],
        "controller_ranks": tuple(controller_rank(row) for row in controller_histories),
    },
)
record(
    "validator_quorum_size_is_not_source_evidence_rank",
    all(len(row["artifact"][2]) == Q for row in controller_histories)
    and {controller_rank(row) for row in controller_histories} == {1, 2},
    "five validators can endorse one or two physically controlled source keys",
)


# 5. Explicit, bitmap, threshold, and accountable certificate projections.
signing_histories = (
    {"message": "m", "signers": (0, 1, 2, 3, 4)},
    {"message": "m", "signers": (0, 1, 2, 3, 5)},
)


def signer_bitmap(signers: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(int(index in signers) for index in validators)


def explicit_certificate(row: dict[str, object]) -> tuple:
    return row["message"], row["signers"], "individual-signatures-valid"


def bitmap_certificate(row: dict[str, object]) -> tuple:
    return row["message"], signer_bitmap(row["signers"]), "aggregate-valid"


def threshold_verification_record(row: dict[str, object]) -> tuple:
    # This is the public semantic verification record, not a claim that raw
    # randomized threshold-signature bytes are equal across signing sessions.
    return "group-public-key", row["message"], "group-signature-valid"


def accountable_threshold_record(row: dict[str, object]) -> tuple:
    return threshold_verification_record(row), row["signers"]


record(
    "explicit_qc_reconstructs_declared_signer_subset",
    factorizes(signing_histories, explicit_certificate, lambda row: row["signers"]),
    "individual signatures retain signer identity",
)
record(
    "bitmap_bearing_aggregate_reconstructs_declared_signer_subset",
    factorizes(signing_histories, bitmap_certificate, lambda row: row["signers"]),
    "signature compression plus a retained bitmap preserves the set",
)
record(
    "ordinary_compressed_threshold_verification_omits_signer_subset",
    not factorizes(
        signing_histories,
        threshold_verification_record,
        lambda row: row["signers"],
    ),
    "two different five-signer transcripts verify under the same group-key semantics",
)
record(
    "accountable_threshold_sidecar_repairs_signer_subset",
    factorizes(
        signing_histories,
        accountable_threshold_record,
        lambda row: row["signers"],
    ),
    "accountability is additional certificate structure",
)


# 6. Clean and equivocating histories with the same final QC.
base_semantic_events = (
    ("source", "s1"),
    ("source", "s2"),
    ("proposal", "m"),
    ("vote-set", signing_histories[0]["signers"]),
    ("decision", "m"),
)
clean_history = {
    "decision": "m",
    "signers": signing_histories[0]["signers"],
    "events": base_semantic_events,
    "equivocation": False,
}
equivocating_history = {
    "decision": "m",
    "signers": signing_histories[0]["signers"],
    "events": base_semantic_events + (("conflicting-proposal", "m-prime"),),
    "equivocation": True,
}
equivocation_histories = (clean_history, equivocating_history)


def plain_qc(row: dict[str, object]) -> tuple:
    return row["decision"], row["signers"], "qc-valid"


def semantic_provenance_lift(row: dict[str, object]) -> tuple:
    return plain_qc(row), canonical_digest(tuple(sorted(row["events"])))


record(
    "plain_final_qc_does_not_reconstruct_rejected_equivocation",
    not factorizes(equivocation_histories, plain_qc, lambda row: row["equivocation"]),
    "clean and forked histories share the final decision and signer set",
)
record(
    "semantic_provenance_lift_reconstructs_encountered_equivocation",
    factorizes(
        equivocation_histories,
        semantic_provenance_lift,
        lambda row: row["equivocation"],
    ),
    "the committed semantic event set distinguishes the signed fork",
)
record(
    "fork_audit_requires_available_conflicting_branch_openings",
    "conflicting-proposal" not in {event[0] for event in clean_history["events"]}
    and "conflicting-proposal"
    in {event[0] for event in equivocating_history["events"]},
    "a root binds an event set; an accusation still needs the two branch openings",
)


# 7. Benign relay subdivision and semantic provenance.
semantic_events = (
    ("source", "s1"),
    ("source", "s2"),
    ("proposal", "m"),
    ("decision", "m"),
)
direct_transport_events = semantic_events + (
    ("transport", "s1-to-proposal"),
    ("transport", "s2-to-proposal"),
)
relayed_transport_events = semantic_events + (
    ("transport", "s1-to-relay-a"),
    ("transport", "relay-a-to-proposal"),
    ("transport", "s2-to-relay-b"),
    ("transport", "relay-b-to-proposal"),
)


def semantic_projection(events: tuple[tuple[str, object], ...]) -> tuple:
    return tuple(event for event in events if event[0] != "transport")


record(
    "raw_transport_root_changes_under_benign_relay_subdivision",
    canonical_digest(direct_transport_events)
    != canonical_digest(relayed_transport_events),
    "a root over every relay hop is representation-sensitive",
)
record(
    "canonical_semantic_root_survives_benign_relay_subdivision",
    semantic_projection(direct_transport_events)
    == semantic_projection(relayed_transport_events)
    == semantic_events
    and canonical_digest(semantic_projection(direct_transport_events))
    == canonical_digest(semantic_projection(relayed_transport_events)),
    {
        "direct_semantic_projection": semantic_projection(direct_transport_events),
        "relayed_semantic_projection": semantic_projection(
            relayed_transport_events
        ),
    },
)
record(
    "separate_route_log_can_retain_the_subdivision_when_the_action_needs_it",
    direct_transport_events != relayed_transport_events,
    "semantic finality and route forensics are different certificate targets",
)


# 8. Membership churn and epoch binding.
membership_histories = (
    {
        "group_key": "group-public-key",
        "message": "m",
        "epoch": "epoch-0",
        "membership": tuple(range(7)),
    },
    {
        "group_key": "group-public-key",
        "message": "m",
        "epoch": "epoch-1",
        "membership": tuple(range(7, 14)),
    },
)


def group_only_record(row: dict[str, object]) -> tuple:
    return row["group_key"], row["message"], "group-signature-valid"


def epoch_bound_record(row: dict[str, object]) -> tuple:
    return (
        group_only_record(row),
        row["epoch"],
        canonical_digest(row["membership"]),
    )


record(
    "group_key_signature_alone_does_not_identify_membership_epoch",
    not factorizes(
        membership_histories,
        group_only_record,
        lambda row: (row["epoch"], row["membership"]),
    ),
    "the same group-key semantics is compatible with two disjoint memberships",
)
record(
    "epoch_and_membership_root_repair_membership_provenance",
    factorizes(
        membership_histories,
        epoch_bound_record,
        lambda row: (row["epoch"], row["membership"]),
    ),
    "the signed statement must bind its membership context",
)


# 9. Mobile corruption and proactive-refresh typing.
mobile_corruptions = ({0, 1}, {2, 3}, {4, 5})
persistent_compromised_shares = set().union(*mobile_corruptions)
record(
    "persistent_shares_accumulate_past_threshold_under_mobile_corruption",
    all(len(epoch_set) <= F for epoch_set in mobile_corruptions)
    and len(persistent_compromised_shares) >= Q,
    {
        "per_epoch_corruptions": tuple(sorted(epoch_set) for epoch_set in mobile_corruptions),
        "accumulated_distinct_shares": len(persistent_compromised_shares),
        "threshold": Q,
    },
)
refreshed_share_tokens = tuple(
    {(epoch, signer) for signer in epoch_set}
    for epoch, epoch_set in enumerate(mobile_corruptions)
)
record(
    "epoch_refreshed_shares_do_not_form_one_same_epoch_threshold",
    all(len(epoch_tokens) < Q for epoch_tokens in refreshed_share_tokens),
    "refresh and erasure are additional premises; this is only an ideal epoch-typing control",
)


# 10. ZK/VSS/MPC statement semantics versus physical source truth.
def private_relation_record(row: tuple[int, int, int]) -> tuple:
    prop = proposal(row)
    statement = (prop[2], prop[3], prop[4], prop[5])
    return (
        canonical_digest(("ideal-zk-proof", statement)),
        canonical_digest(("ideal-vss", prop[4])),
        ("ideal-mpc-output", prop[4]),
    )


record(
    "private_verification_and_computation_artifact_laws_match_across_source_worlds",
    distribution(source_bound_rows, private_relation_record)
    == distribution(null_rows, private_relation_record),
    "the committed pair and declared parity have the same law",
)
record(
    "zk_vss_mpc_stack_does_not_attest_unmodeled_physical_target",
    bayes_binary_error(null_rows, lambda row: row[0], private_relation_record)
    == Fraction(1, 2),
    "verification and computation preserve the admitted source relation",
)
record(
    "mpc_parity_enables_declared_value_access_without_share_disclosure",
    all(private_relation_record(row)[2][1] == (row[1] ^ row[2]) for row in null_rows),
    "the output is correct for the declared inputs even when unrelated to physical T",
)


# 11. Capability-indexed certificate sufficiency.
record(
    "compressed_threshold_record_is_sufficient_for_decision_value",
    factorizes(
        signing_histories,
        threshold_verification_record,
        lambda row: row["message"],
    ),
    "an execution action depending only on the certified message can close",
)
record(
    "the_same_threshold_record_is_insufficient_for_accountability",
    not factorizes(
        signing_histories,
        threshold_verification_record,
        lambda row: row["signers"],
    ),
    "a signer-audit action reopens the certificate fibre",
)
record(
    "the_same_plain_qc_is_insufficient_for_equivocation_audit",
    not factorizes(equivocation_histories, plain_qc, lambda row: row["equivocation"]),
    "a fork-audit action needs the provenance lift",
)
record(
    "even_explicit_qc_is_insufficient_for_physical_controller_audit",
    not factorizes(
        controller_histories,
        lambda row: row["artifact"],
        controller_rank,
    ),
    "declared keys and physical control remain distinct",
)
record(
    "hardened_protocol_certificate_is_insufficient_for_physical_source_truth",
    bayes_binary_error(null_rows, lambda row: row[0], explicit_qc)
    == Fraction(1, 2),
    "physical adjudication needs an independently admitted attestation channel",
)


# 12. Eight-premise scoped composition contract and first-failure controls.
COMPOSITION_PREMISES = (
    "source_adequacy",
    "validity_adequacy",
    "preference_accounting",
    "conflict_safety",
    "liveness",
    "certificate_sufficiency",
    "epoch_setup_integrity",
    "archive_availability",
)


def composition_disposition(contract: dict[str, bool]) -> str:
    for premise in COMPOSITION_PREMISES:
        if not contract[premise]:
            return f"FAIL:{premise}"
    return "SCOPED_LAYERED_FINALITY_COMPOSITION"


complete_contract = {premise: True for premise in COMPOSITION_PREMISES}
record(
    "complete_typed_contract_returns_scoped_composition",
    composition_disposition(complete_contract)
    == "SCOPED_LAYERED_FINALITY_COMPOSITION",
    tuple(COMPOSITION_PREMISES),
)
first_failure_controls = {}
for failed_premise in COMPOSITION_PREMISES:
    hostile_contract = dict(complete_contract)
    hostile_contract[failed_premise] = False
    first_failure_controls[failed_premise] = composition_disposition(hostile_contract)
record(
    "each_missing_premise_returns_its_first_typed_failure",
    all(
        disposition == f"FAIL:{premise}"
        for premise, disposition in first_failure_controls.items()
    ),
    first_failure_controls,
)


passed = sum(bool(check["passed"]) for check in CHECKS)
result = {
    "claim_id": "HC-DU-049",
    "run_id": "N5-SCF-P3",
    "status": "PASS" if passed == len(CHECKS) else "FAIL",
    "checks_passed": passed,
    "checks_total": len(CHECKS),
    "frozen_control": {
        "validators": N,
        "byzantine_bound": F,
        "quorum": Q,
        "sample_size": K,
        "sample_threshold": ALPHA,
        "confidence_rounds": BETA,
        "wrong_sample_probability": fraction_text(single_wrong_probability),
        "independent_three_round_probability": fraction_text(
            single_wrong_probability**BETA
        ),
        "correlated_three_round_probability": fraction_text(
            single_wrong_probability
        ),
        "minimum_quorum_intersection": minimum_intersection,
    },
    "return": (
        "SCOPED_LAYERED_FINALITY_COMPOSITION_WITH_"
        "CAPABILITY_INDEXED_PROVENANCE_LIFT"
    ),
    "first_identifiable_layer": {
        "local_preference": "sample transcript under its routing/dependence model",
        "conflict_safety": "quorum intersection plus correct non-conflicting lock",
        "decision_value": "valid quorum or threshold certificate",
        "declared_signer_subset": "explicit votes, bitmap, or accountable threshold sidecar",
        "encountered_equivocation": "available openings bound by the semantic provenance lift",
        "membership_epoch": "epoch and membership root bound into the signed statement",
        "physical_controller_independence": "not identified by declared keys alone",
        "physical_source_truth": "not identified without an independently admitted formation/attestation channel",
    },
    "local_model_gate": {
        "disposition": "PROOF_CERTIFICATE_OUTSIDE_RESEARCH_MODEL_ADMISSION",
        "reason": (
            "the analytic finite theorems and counterexamples are stated independently; "
            "the script only preserves exact combinatorics, factorization fibres, "
            "certificate projections, and first-failure controls"
        ),
    },
    "next_work": "N5-SCF-P4",
    "checks": CHECKS,
}

artifact = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_metastable_byzantine_provenance_hardening_result.json"
)
artifact.write_text(dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    "HC-DU-049 metastable/Byzantine provenance hardening certificate: "
    f"{passed}/{len(CHECKS)} passed"
)
