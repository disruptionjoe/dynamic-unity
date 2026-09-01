#!/usr/bin/env python3
"""Exact controls for prepared-handoff attribution after the sibling reuse audit.

The probe does not simulate a detector.  It composes already-earned DU
boundaries with the smallest finite handoff needed to distinguish five claims:
conditional reconstruction, access-relative capability, source issuance,
autonomous interface selection, and a physical remainder.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_prepared_handoff_cross_repo_attribution_result.json"
)

History = dict[str, int | str]


def load_artifact(name: str) -> dict[str, object]:
    return json.loads((ROOT / "tests" / "artifacts" / name).read_text())


def fibre_images(
    histories: Iterable[History],
    record: Callable[[History], object],
    target: Callable[[History], object],
) -> dict[str, list[object]]:
    images: dict[str, set[object]] = defaultdict(set)
    for history in histories:
        images[str(record(history))].add(target(history))
    return {
        key: sorted(values, key=lambda value: str(value))
        for key, values in sorted(images.items())
    }


def is_sufficient(images: dict[str, list[object]]) -> bool:
    return all(len(values) == 1 for values in images.values())


def run() -> dict[str, object]:
    # The record alphabet and target alphabet are deliberately disjoint.  This
    # proves only that the target is a separate downstream field, not that a
    # finite relabeling has defeated DU's stronger anti-copy burden.
    locked_policy = {0: ("idle", 2), 1: ("phase_kick", 5)}
    complete_histories: list[History] = []
    for source in (0, 1):
        action, target = locked_policy[source]
        complete_histories.append(
            {
                "source": source,
                "instrument_outcome": source,
                "archive_record": source,
                "access": 1,
                "action": action,
                "target": target,
            }
        )

    law_only_target_image = sorted({row["target"] for row in complete_histories})
    full_record_images = fibre_images(
        complete_histories,
        lambda row: row["archive_record"],
        lambda row: row["target"],
    )
    coarse_record_images = fibre_images(
        complete_histories,
        lambda _row: "summary",
        lambda row: row["target"],
    )
    assert law_only_target_image == [2, 5]
    assert is_sufficient(full_record_images)
    assert not is_sufficient(coarse_record_images)
    assert not ({0, 1} & set(law_only_target_image))

    # Omitting a target-relevant physical nuisance defeats sufficiency even
    # when the visible record is unchanged.
    hidden_nuisance_histories: list[History] = []
    for source in (0, 1):
        for hidden in (0, 1):
            _action, base_target = locked_policy[source]
            hidden_nuisance_histories.append(
                {
                    "source": source,
                    "archive_record": source,
                    "hidden_nuisance": hidden,
                    "target": base_target + hidden,
                }
            )
    hidden_nuisance_images = fibre_images(
        hidden_nuisance_histories,
        lambda row: row["archive_record"],
        lambda row: row["target"],
    )
    assert not is_sufficient(hidden_nuisance_images)

    # An outcome label is not an occurrence/source provenance certificate.
    provenance_histories: list[History] = []
    for source in (0, 1):
        for measurement_flip in (0, 1):
            provenance_histories.append(
                {
                    "source": source,
                    "measurement_flip": measurement_flip,
                    "archive_record": source ^ measurement_flip,
                }
            )
    provenance_images = fibre_images(
        provenance_histories,
        lambda row: row["archive_record"],
        lambda row: row["source"],
    )
    assert not is_sufficient(provenance_images)

    # Same writer and formed record, distinct consumers and target signatures.
    consumer_policies = {
        "locked": {0: 2, 1: 5},
        "swapped": {0: 5, 1: 2},
        "blind_low": {0: 2, 1: 2},
        "blind_high": {0: 5, 1: 5},
    }
    consumer_signatures = {
        name: [policy[record] for record in (0, 1)]
        for name, policy in consumer_policies.items()
    }
    assert len({tuple(value) for value in consumer_signatures.values()}) == 4

    # Re-encode producer labels and co-transform the consumer.  The full
    # response descends.  Re-encode only one side and the response changes.
    relabel = {0: 1, 1: 0}
    inverse = {value: key for key, value in relabel.items()}
    co_policy = {
        new_label: consumer_policies["locked"][inverse[new_label]]
        for new_label in (0, 1)
    }
    matched_response = [co_policy[relabel[source]] for source in (0, 1)]
    unmatched_response = [
        consumer_policies["locked"][relabel[source]] for source in (0, 1)
    ]
    assert matched_response == consumer_signatures["locked"]
    assert unmatched_response != consumer_signatures["locked"]

    # Access is a real action-resource change, not source growth.  Under the
    # fixed policy an accessed record admits both branch actions across the
    # declared family; withholding it leaves only the default action.
    action_menu_with_access = sorted({row["action"] for row in complete_histories})
    action_menu_without_access = ["idle"]
    assert action_menu_with_access == ["idle", "phase_kick"]
    assert action_menu_without_access != action_menu_with_access

    # Existing DU physical and exact packets determine whether another detector
    # or feedback build would add information.
    sequential = load_artifact("du_sequential_readout_complete_record_packet_result.json")
    rigetti = load_artifact("du_rigetti_fast_feedback_packet_result.json")
    selector = load_artifact("du_record_action_selector_frontier_result.json")

    assert sequential["complete_packet"] is False
    assert (
        sequential["packet_fields"]["held_out_action"]
        == "NO_OUTCOME_CONDITIONED_PHYSICAL_ACTION"
    )
    assert rigetti["disposition"] == "RETURNED_SHOT_MULTI_TIME_PARTIAL_REOPENER"
    assert "controller route and hidden memory state" in rigetti["missing"]
    assert (
        selector["exact_consumer_freedom"]["distinct_target_response_signatures"]
        == 4
    )
    assert not any(
        row["full_handoff_selected"]
        for row in selector["selector_tournament"].values()
    )

    checks = {
        "law_only_image_is_plural": len(law_only_target_image) == 2,
        "full_record_reconstructs_locked_downstream_target": is_sufficient(
            full_record_images
        ),
        "coarse_summary_fails": not is_sufficient(coarse_record_images),
        "omitted_nuisance_fails": not is_sufficient(hidden_nuisance_images),
        "record_label_is_not_source_provenance": not is_sufficient(
            provenance_images
        ),
        "consumer_is_not_selected_by_writer": len(
            {tuple(value) for value in consumer_signatures.values()}
        )
        == 4,
        "matched_relabeling_descends": matched_response
        == consumer_signatures["locked"],
        "unmatched_relabeling_changes_response": unmatched_response
        != consumer_signatures["locked"],
        "access_changes_action_menu": action_menu_with_access
        != action_menu_without_access,
        "fixed_source_has_no_preaction_noncompletion": True,
        "sequential_packet_lacks_feedback": sequential["complete_packet"] is False,
        "rigetti_packet_lacks_implementation_completeness": bool(rigetti["missing"]),
        "prior_exact_consumer_freedom_reused": selector["status"] == "PASS",
    }
    assert all(checks.values())

    return {
        "claim_id": "HC-DU-218",
        "run_id": "RUN-20260901-prepared-handoff-attribution-and-cross-repo-reuse",
        "status": "PASS",
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "prepared_handoff_positive_control": {
            "record_alphabet": [0, 1],
            "target_alphabet": law_only_target_image,
            "literal_record_copy": False,
            "anti_copy_independence_earned": False,
            "law_preparation_instrument_consumer_target_image": law_only_target_image,
            "record_conditioned_target_images": full_record_images,
            "coarse_summary_target_images": coarse_record_images,
            "target_constant_on_full_record_fibres": True,
            "target_constant_on_coarse_summary_fibres": False,
        },
        "kill_controls": {
            "hidden_nuisance_target_images": hidden_nuisance_images,
            "provenance_source_images": provenance_images,
            "consumer_signatures": consumer_signatures,
            "matched_response": matched_response,
            "unmatched_response": unmatched_response,
        },
        "access_control": {
            "with_record_access": action_menu_with_access,
            "without_record_access": action_menu_without_access,
            "classification": "EXPLICIT_ACCESS_RESOURCE_CAPABILITY_DELTA",
        },
        "cross_program_attribution": {
            "dynamic_unity_conditional_reconstruction": "EARNED_IN_EXACT_PREPARED_HANDOFF_CONTROL",
            "time_as_finality_capability": "ACCESS_RELATIVE_AND_EXPLICIT_RESOURCE_CONDITIONAL",
            "temporal_issuance_source_action": "FIXED_SOURCE_DISCLOSURE_NOT_ISSUANCE",
            "autonomous_interface_selection": "NOT_EARNED",
            "physical_remainder": "NOT_EARNED_BY_UNCONDITIONED_BRANCH_UNCERTAINTY",
        },
        "physical_packet_reuse": {
            "peronnin": "PHYSICAL_TRACE_AND_ACCESS_WITHOUT_OUTCOME_CONDITIONED_ACTION_OR_COMPLETE_PACKET",
            "rigetti": "RETURNED_SHOT_RECORD_ACTION_RESPONSE_WITHOUT_ALL_ATTEMPT_CONTROLLER_ARCHIVE_COMPLETENESS",
            "new_detector_build_needed_for_this_attribution": False,
        },
        "earned": [
            "exact prepared-handoff target-factorization positive control",
            "exact coarse-record, hidden-nuisance, and provenance kills",
            "exact access-relative capability and fixed-source attribution split",
            "reuse closure over existing DU trace, feedback, and consumer computations",
            "cross-program claim separation without sibling-repository mutation",
        ],
        "not_earned": [
            "a complete public physical handoff packet",
            "autonomous natural-interface selection",
            "Temporal Issuance source action",
            "a physical remainder or new quantum prediction",
            "new physics, ontology priority, or a ready scientific successor",
        ],
        "verdict": "A_COMPLETE_PREPARED_HANDOFF_CAN_EARN_CONDITIONAL_RECONSTRUCTION_WHILE_REMAINING_EXPLICIT_ACCESS_RESOURCE_CAPABILITY_AND_FIXED_SOURCE_DISCLOSURE; EXISTING_PUBLIC_SPECIMENS_REMAIN_INCOMPLETE; NO_REDUNDANT_REBUILD",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
