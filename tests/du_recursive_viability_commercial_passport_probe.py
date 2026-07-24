#!/usr/bin/env python3
"""Exact finite probe for a recursive-viability commercial passport.

The fixture is deliberately engineered and small.  Nine binary sites form
three three-site repetition blocks.  The three block values additionally
satisfy an even-parity relation.  This permits exact comparisons among:

* no regulator (m=0),
* three local repetition regulators (m=1),
* local regulators plus one upper parity regulator (m=2),
* one flat global codebook regulator,
* arbitrary partitions,
* an overcomplete overlapping cover, and
* passive ordinary coarse-graining.

The probe tests recovery on training and held-out interventions, and then
applies hard nulls for passive stability, depth overfit, resolution,
relabeling, ordinary coarse-graining, record certification, and teleology.
It makes no claim that this engineered hierarchy is fundamental physics.
"""

from __future__ import annotations

import hashlib
import json
from itertools import combinations, product
from pathlib import Path
from typing import Callable, Iterable, Sequence


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_recursive_viability_commercial_passport_probe_result.json"
)

State = tuple[int, ...]
Partition = tuple[tuple[int, ...], ...]
Controller = Callable[[State], State]

PLANTED_ROWS: Partition = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
ARBITRARY_COLUMNS: Partition = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
ARBITRARY_SHUFFLE: Partition = ((0, 1, 3), (2, 4, 6), (5, 7, 8))
RELABELING = (8, 7, 6, 5, 4, 3, 2, 1, 0)


def logical_words() -> tuple[State, ...]:
    return tuple(
        bits for bits in product((0, 1), repeat=3) if bits[0] ^ bits[1] ^ bits[2] == 0
    )


def encode(logical: Sequence[int], partition: Partition = PLANTED_ROWS) -> State:
    state = [0] * 9
    for value, group in zip(logical, partition):
        for index in group:
            state[index] = int(value)
    return tuple(state)


LOGICAL_WORDS = logical_words()
CODEWORDS = tuple(encode(word) for word in LOGICAL_WORDS)
CODEWORD_SET = frozenset(CODEWORDS)


def hamming(left: State, right: State) -> int:
    return sum(a != b for a, b in zip(left, right))


def flip(state: State, positions: Iterable[int]) -> State:
    result = list(state)
    for position in positions:
        result[position] ^= 1
    return tuple(result)


def majority(state: State, group: Sequence[int]) -> int:
    return int(sum(state[index] for index in group) >= 2)


def decoded_payload(state: State, partition: Partition = PLANTED_ROWS) -> State:
    return tuple(majority(state, group) for group in partition)


def in_viable_region(state: State) -> bool:
    return state in CODEWORD_SET


def passive(state: State) -> State:
    return state


def local_regulator(partition: Partition) -> Controller:
    def regulate(state: State) -> State:
        return encode(decoded_payload(state, partition), partition)

    return regulate


def recursive_regulator(partition: Partition) -> Controller:
    """Local majority regulation with one parity-mediated downward correction.

    A local group exports two typed summaries: its majority bit and whether
    its three leaves disagree.  If upper parity fails and exactly one local
    group reports disagreement, the upper regulator can infer that group's
    intended bit from the other two and send a correction downward.
    """

    def regulate(state: State) -> State:
        macro = list(decoded_payload(state, partition))
        alarms = [
            int(any(state[index] != macro[group_index] for index in group))
            for group_index, group in enumerate(partition)
        ]
        if macro[0] ^ macro[1] ^ macro[2]:
            alarmed = [index for index, alarm in enumerate(alarms) if alarm]
            if len(alarmed) == 1:
                target = alarmed[0]
                other = [index for index in range(3) if index != target]
                macro[target] = macro[other[0]] ^ macro[other[1]]
        return encode(macro, partition)

    return regulate


def flat_codebook_regulator(state: State) -> State:
    """One global regulator with unrestricted access to the full codebook."""

    return min(CODEWORDS, key=lambda word: (hamming(state, word), word))


def ordinary_coarse_grain(state: State) -> State:
    """Observe row majorities but provide no downward repair action."""

    _ = decoded_payload(state)
    return state


def permute_state(state: State, permutation: Sequence[int]) -> State:
    result = [0] * len(state)
    for old_index, new_index in enumerate(permutation):
        result[new_index] = state[old_index]
    return tuple(result)


def permute_partition(
    partition: Partition, permutation: Sequence[int]
) -> Partition:
    return tuple(
        tuple(permutation[index] for index in group) for group in partition
    )


def make_case(
    family: str, original: State, positions: Sequence[int]
) -> dict[str, object]:
    return {
        "family": family,
        "original": original,
        "disturbed": flip(original, positions),
        "positions": tuple(positions),
    }


def build_cases() -> dict[str, tuple[dict[str, object], ...]]:
    families: dict[str, list[dict[str, object]]] = {
        "passive_stability": [],
        "train_single_leaf": [],
        "heldout_two_same_group": [],
        "heldout_two_cross_group": [],
        "out_of_family_whole_group": [],
        "hard_null_valid_alias": [],
    }
    for original in CODEWORDS:
        families["passive_stability"].append(
            make_case("passive_stability", original, ())
        )
        for position in range(9):
            families["train_single_leaf"].append(
                make_case("train_single_leaf", original, (position,))
            )
        for group in PLANTED_ROWS:
            for positions in combinations(group, 2):
                families["heldout_two_same_group"].append(
                    make_case("heldout_two_same_group", original, positions)
                )
            families["out_of_family_whole_group"].append(
                make_case("out_of_family_whole_group", original, group)
            )
        for left, right in combinations(PLANTED_ROWS, 2):
            for first in left:
                for second in right:
                    families["heldout_two_cross_group"].append(
                        make_case(
                            "heldout_two_cross_group",
                            original,
                            (first, second),
                        )
                    )
            families["hard_null_valid_alias"].append(
                make_case(
                    "hard_null_valid_alias",
                    original,
                    tuple(left) + tuple(right),
                )
            )
    return {name: tuple(cases) for name, cases in families.items()}


CASES = build_cases()


def ratio(numerator: int, denominator: int) -> dict[str, object]:
    return {
        "count": numerator,
        "total": denominator,
        "rate": numerator / denominator,
    }


def evaluate(controller: Controller, cases: Sequence[dict[str, object]]) -> dict:
    exact = 0
    payload = 0
    root_relation = 0
    certified = 0
    false_certificates = 0
    for case in cases:
        original = tuple(case["original"])
        disturbed = tuple(case["disturbed"])
        output = controller(disturbed)
        is_exact = output == original
        is_payload = decoded_payload(output) == decoded_payload(original)
        has_root_relation = (
            decoded_payload(output)[0]
            ^ decoded_payload(output)[1]
            ^ decoded_payload(output)[2]
        ) == 0
        is_certified = in_viable_region(output)
        exact += int(is_exact)
        payload += int(is_payload)
        root_relation += int(has_root_relation)
        certified += int(is_certified)
        false_certificates += int(is_certified and not is_exact)
    total = len(cases)
    return {
        "exact_original_recovery": ratio(exact, total),
        "logical_payload_recovery": ratio(payload, total),
        "root_even_parity": ratio(root_relation, total),
        "internal_codeword_certificate": ratio(certified, total),
        "false_certificate": ratio(false_certificates, total),
    }


CONTROLLERS: dict[str, tuple[Controller, dict[str, object]]] = {
    "m0_passive": (
        passive,
        {
            "recursive_levels": 0,
            "partition": None,
            "upper_interface_width": 0,
            "leaf_memberships": 0,
            "has_downward_action": False,
        },
    ),
    "m1_planted_local": (
        local_regulator(PLANTED_ROWS),
        {
            "recursive_levels": 1,
            "partition": PLANTED_ROWS,
            "upper_interface_width": 0,
            "leaf_memberships": 9,
            "has_downward_action": True,
        },
    ),
    "m2_planted_recursive": (
        recursive_regulator(PLANTED_ROWS),
        {
            "recursive_levels": 2,
            "partition": PLANTED_ROWS,
            "upper_interface_width": 6,
            "leaf_memberships": 9,
            "has_downward_action": True,
        },
    ),
    "flat_global_codebook": (
        flat_codebook_regulator,
        {
            "recursive_levels": 1,
            "partition": None,
            "upper_interface_width": 9,
            "leaf_memberships": 9,
            "has_downward_action": True,
        },
    ),
    "m2_arbitrary_columns": (
        recursive_regulator(ARBITRARY_COLUMNS),
        {
            "recursive_levels": 2,
            "partition": ARBITRARY_COLUMNS,
            "upper_interface_width": 6,
            "leaf_memberships": 9,
            "has_downward_action": True,
        },
    ),
    "m2_arbitrary_shuffle": (
        recursive_regulator(ARBITRARY_SHUFFLE),
        {
            "recursive_levels": 2,
            "partition": ARBITRARY_SHUFFLE,
            "upper_interface_width": 6,
            "leaf_memberships": 9,
            "has_downward_action": True,
        },
    ),
    "m2_overlap_cover": (
        recursive_regulator(PLANTED_ROWS),
        {
            "recursive_levels": 2,
            "partition": {
                "regulating_groups": PLANTED_ROWS,
                "extra_overlap_groups": ARBITRARY_COLUMNS,
            },
            "upper_interface_width": 12,
            "leaf_memberships": 18,
            "has_downward_action": True,
        },
    ),
    "ordinary_rg_no_control": (
        ordinary_coarse_grain,
        {
            "recursive_levels": 1,
            "partition": PLANTED_ROWS,
            "upper_interface_width": 3,
            "leaf_memberships": 9,
            "has_downward_action": False,
        },
    ),
}


def partition_discovery() -> dict[str, object]:
    candidates = {
        "planted_rows": PLANTED_ROWS,
        "arbitrary_columns": ARBITRARY_COLUMNS,
        "arbitrary_shuffle": ARBITRARY_SHUFFLE,
    }
    scores = {}
    for name, partition in candidates.items():
        controller = local_regulator(partition)
        baseline = evaluate(controller, CASES["passive_stability"])
        training = evaluate(controller, CASES["train_single_leaf"])
        scores[name] = {
            "baseline_integrity_rate": baseline["exact_original_recovery"]["rate"],
            "training_recovery_rate": training["exact_original_recovery"]["rate"],
            "fixed_leaf_memberships": 9,
        }
    ranking = sorted(
        scores,
        key=lambda name: (
            -scores[name]["training_recovery_rate"],
            -scores[name]["baseline_integrity_rate"],
            name,
        ),
    )
    best_score = (
        scores[ranking[0]]["training_recovery_rate"],
        scores[ranking[0]]["baseline_integrity_rate"],
    )
    winners = [
        name
        for name in ranking
        if (
            scores[name]["training_recovery_rate"],
            scores[name]["baseline_integrity_rate"],
        )
        == best_score
    ]
    return {"scores": scores, "ranking": ranking, "winners": winners}


def relabeling_check() -> dict[str, object]:
    permuted_partition = permute_partition(PLANTED_ROWS, RELABELING)
    controller = recursive_regulator(permuted_partition)
    family_rates = {}
    all_match = True
    original_controller = recursive_regulator(PLANTED_ROWS)
    for family, cases in CASES.items():
        permuted_cases = tuple(
            {
                "family": case["family"],
                "original": permute_state(tuple(case["original"]), RELABELING),
                "disturbed": permute_state(tuple(case["disturbed"]), RELABELING),
                "positions": tuple(RELABELING[index] for index in case["positions"]),
            }
            for case in cases
        )
        original_metrics = evaluate(original_controller, cases)
        permuted_metrics = evaluate(controller, permuted_cases)
        matches = original_metrics == permuted_metrics
        all_match = all_match and matches
        family_rates[family] = {
            "matches": matches,
            "exact_original_recovery_rate": permuted_metrics[
                "exact_original_recovery"
            ]["rate"],
        }
    return {
        "permutation": RELABELING,
        "all_family_metrics_match": all_match,
        "families": family_rates,
    }


def supported_exact_rate(candidate_metrics: dict[str, dict]) -> float:
    supported = (
        "train_single_leaf",
        "heldout_two_same_group",
        "heldout_two_cross_group",
    )
    recovered = sum(
        candidate_metrics[family]["exact_original_recovery"]["count"]
        for family in supported
    )
    total = sum(
        candidate_metrics[family]["exact_original_recovery"]["total"]
        for family in supported
    )
    return recovered / total


def source_digest(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(canonical).hexdigest()


def main() -> None:
    metrics = {
        name: {
            "model": metadata,
            "families": {
                family: evaluate(controller, cases)
                for family, cases in CASES.items()
            },
        }
        for name, (controller, metadata) in CONTROLLERS.items()
    }
    discovery = partition_discovery()
    relabeling = relabeling_check()

    m1 = metrics["m1_planted_local"]["families"]
    m2 = metrics["m2_planted_recursive"]["families"]
    flat = metrics["flat_global_codebook"]["families"]
    overlap = metrics["m2_overlap_cover"]["families"]
    m0 = metrics["m0_passive"]["families"]
    rg = metrics["ordinary_rg_no_control"]["families"]

    checks = {
        "four_even_parity_logical_words": len(LOGICAL_WORDS) == 4,
        "code_minimum_distance_is_six": min(
            hamming(left, right)
            for left, right in combinations(CODEWORDS, 2)
        )
        == 6,
        "family_cardinalities_exact": {
            name: len(cases) for name, cases in CASES.items()
        }
        == {
            "passive_stability": 4,
            "train_single_leaf": 36,
            "heldout_two_same_group": 36,
            "heldout_two_cross_group": 108,
            "out_of_family_whole_group": 12,
            "hard_null_valid_alias": 12,
        },
        "m1_passes_training": m1["train_single_leaf"][
            "exact_original_recovery"
        ]["rate"]
        == 1.0,
        "m1_fails_same_group_holdout": m1["heldout_two_same_group"][
            "exact_original_recovery"
        ]["rate"]
        == 0.0,
        "m1_passes_cross_group_holdout": m1["heldout_two_cross_group"][
            "exact_original_recovery"
        ]["rate"]
        == 1.0,
        "m2_passes_all_supported_interventions": supported_exact_rate(m2) == 1.0,
        "flat_matches_m2_on_supported_interventions": supported_exact_rate(flat)
        == supported_exact_rate(m2)
        == 1.0,
        "overlap_matches_m2_but_costs_more": supported_exact_rate(overlap)
        == supported_exact_rate(m2)
        and metrics["m2_overlap_cover"]["model"]["leaf_memberships"]
        > metrics["m2_planted_recursive"]["model"]["leaf_memberships"],
        "planted_partition_is_unique_training_winner": discovery["winners"]
        == ["planted_rows"],
        "m2_cannot_recover_unlocated_whole_group_fault": m2[
            "out_of_family_whole_group"
        ]["exact_original_recovery"]["rate"]
        == 0.0,
        "valid_alias_is_undetectable_to_m2": m2["hard_null_valid_alias"][
            "exact_original_recovery"
        ]["rate"]
        == 0.0
        and m2["hard_null_valid_alias"]["internal_codeword_certificate"]["rate"]
        == 1.0,
        "flat_also_false_certifies_valid_alias": flat["hard_null_valid_alias"][
            "exact_original_recovery"
        ]["rate"]
        == 0.0
        and flat["hard_null_valid_alias"]["internal_codeword_certificate"]["rate"]
        == 1.0,
        "passive_stability_is_not_active_regulation": m0["passive_stability"][
            "exact_original_recovery"
        ]["rate"]
        == 1.0
        and m0["train_single_leaf"]["exact_original_recovery"]["rate"] == 0.0,
        "ordinary_coarse_graining_is_not_downward_control": rg[
            "train_single_leaf"
        ]["logical_payload_recovery"]["rate"]
        == 1.0
        and rg["train_single_leaf"]["exact_original_recovery"]["rate"] == 0.0,
        "relabeling_invariant_when_support_is_relabelled": relabeling[
            "all_family_metrics_match"
        ],
        "resolution_changes_the_apparent_result": m0["train_single_leaf"][
            "logical_payload_recovery"
        ]["rate"]
        == 1.0
        and m0["train_single_leaf"]["exact_original_recovery"]["rate"] == 0.0,
    }

    nulls = {
        "arbitrary_partition": {
            "verdict": "PASSED",
            "result": "The planted partition is the unique training winner among the three fixed partitions; labels alone do not select it.",
        },
        "passive_stability": {
            "verdict": "PASSED",
            "result": "No-disturbance survival is perfect for m=0, while one-leaf exact restoration is zero.",
        },
        "depth_overfit_and_overlap": {
            "verdict": "PASSED",
            "result": "The overlap cover exactly duplicates m=2 recovery while doubling leaf memberships and upper summaries.",
        },
        "resolution": {
            "verdict": "PASSED",
            "result": "At logical-payload resolution m=0 survives every training single flip; at exact-codeword resolution it survives none.",
        },
        "relabeling_and_fibre": {
            "verdict": "PASSED",
            "result": "All m=2 family metrics are invariant when leaves and the intervention-supported partition are relabelled together.",
        },
        "heldout_disturbance": {
            "verdict": "PASSED_WITH_NONUNIQUENESS",
            "result": "m=2 repairs the held-out same-group double flips that kill m=1, but a flat global codebook matches it exactly.",
        },
        "ordinary_rg": {
            "verdict": "PASSED",
            "result": "Row-majority compression preserves the training logical payload but restores zero perturbed microstates without a down map.",
        },
        "clock_and_record": {
            "verdict": "PASSED_AS_A_WARNING",
            "result": "A durable record is counted only after codeword verification; valid aliases are still falsely certified because the original history is absent.",
        },
        "teleology": {
            "verdict": "PASSED_BY_EXPLICIT_TYPING",
            "result": "The codebook, viable region, perturbations, and repair objective are engineered assay inputs; no purpose, agency, or physical finality is inferred.",
        },
    }

    payload = {
        "probe": "du_recursive_viability_commercial_passport_probe",
        "version": 1,
        "contested_proposition": (
            "Held-out viability and bounded interface cost uniquely identify "
            "the number and shape of recursive viable-system levels."
        ),
        "fixture": {
            "micro_sites": 9,
            "planted_partition": PLANTED_ROWS,
            "logical_words": LOGICAL_WORDS,
            "codewords": CODEWORDS,
            "rule": (
                "Each three-site row repeats one logical bit; the three logical "
                "bits obey even parity."
            ),
            "upward_map": "row majority plus local disagreement alarm",
            "downward_map": (
                "local repetition repair; when one alarmed row violates upper "
                "parity, infer its logical bit from the other two"
            ),
            "clock_denominator": (
                "one declared disturbance-and-repair opportunity; it is not "
                "identified with physical time"
            ),
            "record_semantics": (
                "emit an internal certificate only when the output is one of "
                "the four declared codewords"
            ),
        },
        "case_counts": {name: len(cases) for name, cases in CASES.items()},
        "candidate_results": metrics,
        "partition_discovery": discovery,
        "relabeling_check": relabeling,
        "comparisons": {
            "m1_supported_exact_rate": supported_exact_rate(m1),
            "m2_supported_exact_rate": supported_exact_rate(m2),
            "flat_supported_exact_rate": supported_exact_rate(flat),
            "overlap_supported_exact_rate": supported_exact_rate(overlap),
            "m2_vs_flat": (
                "Behavioral tie. m=2 uses a six-summary declared upper "
                "interface; flat uses unrestricted access to all nine leaves. "
                "No winner exists until that access pattern is physically "
                "supported or commercially priced."
            ),
            "m2_vs_overlap": (
                "m=2 strictly dominates the behaviorally identical overlap "
                "cover on declared memberships and upper-interface width."
            ),
        },
        "nulls": nulls,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "passport_disposition": {
            "boundary": "engineered nine-site code and declared environment",
            "essential_variables": (
                "full two-bit logical payload, exact codeword membership, and "
                "the upper even-parity relation"
            ),
            "viable_region": "the four codewords",
            "operations": "three local repetition regulators",
            "coordination": "upper even-parity comparison",
            "resource_or_regulator": (
                "six typed local summaries for m=2, or unrestricted nine-leaf "
                "access for the flat rival"
            ),
            "adaptation_channel": None,
            "identity": "declared codeword family; not an inferred observer",
            "recursive_closure": (
                "conditional for the supported disturbance family; fails "
                "unlocated whole-group and valid-alias interventions"
            ),
            "invariance": "exact under joint leaf/support relabeling",
            "depth": (
                "m=2 is useful but not uniquely selected against a flat global "
                "regulator; extra overlap is rejected"
            ),
            "status": "CONSTRUCTIVELY_REALIZED / CONDITIONALLY_ENTAILED",
        },
        "commercial_decision": {
            "classification": "OVERLAY_PASSPORT",
            "separate_program": False,
            "gate_scope": (
                "Gate only claims of recursive autonomous viability, not the "
                "HC-DU-031A record-clock or HC-DU-011A causal-post routes."
            ),
            "integration": (
                "Attach the passport to surviving record-clock and causal-post "
                "fixtures; stop if no intervention-supported boundary, down "
                "map, or held-out advantage appears."
            ),
        },
        "verdict": (
            "NESTED REGULATION CAN EARN HELD-OUT VALUE, BUT VIABILITY ALONE "
            "DOES NOT IDENTIFY RECURSION: A FLAT GLOBAL REGULATOR TIES, AN "
            "OVERLAP RIVAL OVERFITS, AND OUT-OF-FAMILY VALID ALIASES DEFEAT "
            "EVERY FIXED DECODER. RVS IS AN OVERLAY PASSPORT, NOT A SEPARATE "
            "PROGRAM."
        ),
    }
    payload["canonical_payload_sha256"] = source_digest(payload)

    assert all(checks.values()), checks
    assert payload["checks_passed"] == payload["checks_total"]

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
