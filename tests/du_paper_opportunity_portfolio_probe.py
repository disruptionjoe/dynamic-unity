#!/usr/bin/env python3
"""Validate Dynamic Unity's upstream paper-opportunity portfolio.

This probe checks inventory integrity, Factory-seed field completeness, and
the confirmed source-to-Factory intake mapping.  It does not evaluate
scientific truth, novelty, manuscript quality, Factory priority, production
activation, or publication readiness.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "papers" / "paper-opportunity-portfolio.json"
OUTPUT = ROOT / "tests" / "artifacts" / "du_paper_opportunity_portfolio_result.json"

REQUIRED_FIELDS = {
    "id",
    "title",
    "source_owner",
    "family",
    "contribution",
    "audience",
    "current_grade",
    "evidence_refs",
    "factory_snapshot",
    "factory_state",
    "hardening_request",
    "seed_status",
    "seed_swings_estimate",
    "seed_work_remaining",
    "manuscript_distance",
    "manuscript_swings_estimate",
    "manuscript_load_bearing_gaps",
    "novelty_boundary",
    "negative_result_value",
    "overlap_ids",
    "recommended_action",
}


def all_coverage_ids(coverage: dict[str, Any]) -> set[str]:
    found: set[str] = set()
    for value in coverage.values():
        if isinstance(value, list):
            found.update(value)
        elif isinstance(value, dict):
            for nested in value.values():
                found.update(nested)
        else:
            raise TypeError(f"unsupported coverage value: {type(value)!r}")
    return found


def build_result() -> dict[str, Any]:
    portfolio = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
    candidates = portfolio["candidates"]
    candidate_ids = [candidate["id"] for candidate in candidates]
    candidate_id_set = set(candidate_ids)
    expected_ids = {f"DU-PAPER-{index:03d}" for index in range(1, 28)}
    seed_statuses = set(portfolio["seed_status_definitions"])
    distance_classes = set(portfolio["manuscript_distance_definitions"])
    coverage_ids = all_coverage_ids(portfolio["coverage_map"])
    concept_keys = set(portfolio["coverage_map"]["concept_register"])
    expected_concepts = {f"CONCEPT-DU-{index:03d}" for index in range(1, 11)}
    candidate_by_id = {candidate["id"]: candidate for candidate in candidates}
    proposal_batch = portfolio["factory_proposal_batch_if_separately_authorized"]
    proposed_ids = set(proposal_batch["standalone_proposals"]) | set(
        proposal_batch["merge_review_proposals"]
    )
    proposal_complete_ids = {
        candidate["id"]
        for candidate in candidates
        if candidate["seed_status"] == "proposal_complete_not_sent"
    }
    factory_intake = portfolio["factory_intake_2026_07_24"]
    intake_seed_map = {
        **factory_intake["standalone_seed_map"],
        **factory_intake["merge_review_seed_map"],
    }
    expected_intake_seed_map = {
        "DU-PAPER-003": "DU-SEED-COVARIANT-RECORD-COST",
        "DU-PAPER-004": "DU-SEED-BOUNDARY-RELOCATION",
        "DU-PAPER-007": "DU-SEED-INTERVENTIONAL-RECORD-SUFFICIENCY",
        "DU-PAPER-009": "DU-SEED-HIGHER-ORDER-PUBLIC-FINALITY",
        "DU-PAPER-013": "DU-SEED-CSG-POST-TAIL-CLASSES",
        "DU-PAPER-015": "DU-SEED-GLOBAL-CLOCK-GAUGE-WITNESS",
        "DU-PAPER-016": "DU-SEED-NO-PRIVILEGED-DEPTH",
        "DU-PAPER-017": "DU-SEED-FINITE-RECORD-OPENNESS",
        "DU-PAPER-024": "DU-SEED-CONDITIONAL-FINALITY-DEVIATION",
    }

    missing_fields = {
        candidate["id"]: sorted(REQUIRED_FIELDS - set(candidate))
        for candidate in candidates
        if REQUIRED_FIELDS - set(candidate)
    }
    missing_evidence = {
        candidate["id"]: [
            reference
            for reference in candidate["evidence_refs"]
            if not (ROOT / reference).is_file()
        ]
        for candidate in candidates
        if any(
            not (ROOT / reference).is_file()
            for reference in candidate["evidence_refs"]
        )
    }
    invalid_overlap_ids = {
        candidate["id"]: [
            overlap
            for overlap in candidate["overlap_ids"]
            if overlap not in candidate_id_set or overlap == candidate["id"]
        ]
        for candidate in candidates
        if any(
            overlap not in candidate_id_set or overlap == candidate["id"]
            for overlap in candidate["overlap_ids"]
        )
    }
    proposal_field_failures = {
        candidate["id"]: {
            "seed_swings_estimate": candidate["seed_swings_estimate"],
            "seed_work_remaining": candidate["seed_work_remaining"],
            "factory_state": candidate["factory_state"],
            "hardening_request": candidate["hardening_request"],
        }
        for candidate in candidates
        if candidate["seed_status"] == "proposal_complete_not_sent"
        and (
            candidate["seed_swings_estimate"] != "0"
            or candidate["seed_work_remaining"]
            or candidate["factory_state"] != "unselected"
            or candidate["hardening_request"] != "none"
        )
    }
    factory_intake_state_failures = {
        candidate_id: {
            "factory_snapshot": candidate_by_id[candidate_id]["factory_snapshot"],
            "factory_state": candidate_by_id[candidate_id]["factory_state"],
            "seed_status": candidate_by_id[candidate_id]["seed_status"],
        }
        for candidate_id, seed_id in intake_seed_map.items()
        if (
            seed_id not in candidate_by_id[candidate_id]["factory_snapshot"]
            or (
                candidate_id in factory_intake["standalone_seed_map"]
                and not (
                    (
                        candidate_by_id[candidate_id]["factory_state"]
                        == "existing_seed_unselected"
                        and candidate_by_id[candidate_id]["seed_status"]
                        == "factory_seeded_unselected"
                    )
                    or (
                        candidate_by_id[candidate_id]["factory_state"]
                        == "factory_post_ready"
                        and candidate_by_id[candidate_id]["seed_status"]
                        == "already_factory_post_ready"
                    )
                )
            )
            or (
                candidate_id in factory_intake["merge_review_seed_map"]
                and (
                    candidate_by_id[candidate_id]["factory_state"]
                    != "existing_seed_merge_review"
                    or candidate_by_id[candidate_id]["seed_status"]
                    != "factory_seeded_merge_review"
                )
            )
        )
    }

    checks = {
        "portfolio_has_27_candidates": len(candidates) == 27,
        "ids_are_unique_and_contiguous": (
            len(candidate_ids) == len(candidate_id_set)
            and candidate_id_set == expected_ids
            and all(
                re.fullmatch(r"DU-PAPER-\d{3}", candidate_id)
                for candidate_id in candidate_ids
            )
        ),
        "all_required_candidate_fields_are_present": not missing_fields,
        "all_local_evidence_pointers_exist": not missing_evidence,
        "all_seed_statuses_are_declared": all(
            candidate["seed_status"] in seed_statuses for candidate in candidates
        ),
        "all_manuscript_distances_are_declared": all(
            candidate["manuscript_distance"] in distance_classes
            for candidate in candidates
        ),
        "all_overlap_ids_are_valid": not invalid_overlap_ids,
        "all_ten_concepts_are_covered": concept_keys == expected_concepts,
        "every_candidate_is_represented_in_coverage_map": (
            coverage_ids == candidate_id_set
        ),
        "prior_top_three_are_preserved": set(
            portfolio["coverage_map"]["prior_repo_wide_top_three"]
        )
        == {"DU-PAPER-003", "DU-PAPER-007", "DU-PAPER-009"},
        "existing_factory_du_entries_are_not_duplicated": {
            candidate["id"]: candidate["seed_status"]
            for candidate in candidates
            if candidate["id"] in {"DU-PAPER-001", "DU-PAPER-002"}
        }
        == {
            "DU-PAPER-001": "already_factory_post_ready",
            "DU-PAPER-002": "already_factory_seeded",
        },
        "confirmed_factory_intake_maps_nine_unique_seeds": (
            intake_seed_map == expected_intake_seed_map
            and len(set(intake_seed_map.values())) == 9
        ),
        "confirmed_factory_intake_matches_candidate_states": (
            not factory_intake_state_failures
        ),
        "factory_custody_coverage_is_complete": set(
            portfolio["coverage_map"]["factory_dynamic_unity_custody"]
        )
        == {
            "DU-PAPER-001",
            "DU-PAPER-002",
            *expected_intake_seed_map,
        },
        "proposal_batch_matches_all_complete_unsent_proposals": (
            proposed_ids == proposal_complete_ids
        ),
        "no_complete_unsent_proposals_remain": not proposal_complete_ids,
        "proposal_complete_records_need_no_more_seed_fields": (
            not proposal_field_failures
        ),
        "merge_candidates_name_valid_overlap": all(
            bool(candidate["overlap_ids"])
            for candidate in candidates
            if candidate["seed_status"] == "merge_candidate_not_standalone"
        ),
        "transfers_leave_dynamic_unity_ownership": all(
            candidate["source_owner"] != "dynamic-unity"
            for candidate in candidates
            if candidate["seed_status"] == "transfer_to_other_owner"
        ),
        "no_factory_hardening_request_is_invented": all(
            candidate["hardening_request"] == "none" for candidate in candidates
        ),
    }

    seed_counts = Counter(candidate["seed_status"] for candidate in candidates)
    manuscript_counts = Counter(
        candidate["manuscript_distance"] for candidate in candidates
    )
    near_manuscript_ids = [
        candidate["id"]
        for candidate in candidates
        if candidate["manuscript_distance"]
        in {"factory_post_ready", "one_source_hardening_swing"}
    ]

    return {
        "probe": "du_paper_opportunity_portfolio_probe",
        "date": "2026-07-24",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "claim_grade": (
            "PORTFOLIO INTEGRITY AND CONFIRMED FACTORY-CUSTODY AUDIT / "
            "NO SCIENTIFIC, NOVELTY, MANUSCRIPT, FACTORY-PRIORITY, "
            "PRODUCTION-ACTIVATION, SUBMISSION, OR PUBLICATION VERDICT"
        ),
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "candidate_count": len(candidates),
        "seed_status_counts": dict(sorted(seed_counts.items())),
        "manuscript_distance_counts": dict(sorted(manuscript_counts.items())),
        "factory_intake": factory_intake,
        "proposal_batch": proposal_batch,
        "near_manuscript_ids": near_manuscript_ids,
        "diagnostics": {
            "missing_fields": missing_fields,
            "missing_evidence": missing_evidence,
            "invalid_overlap_ids": invalid_overlap_ids,
            "factory_intake_state_failures": factory_intake_state_failures,
            "proposal_field_failures": proposal_field_failures,
        },
        "nonclaims": [
            "the inventory is exhaustive over future ideas",
            "a complete seed is scientifically supported",
            "Factory custody is production activation",
            "the initial Factory review order is immutable",
            "a manuscript-distance estimate is a schedule commitment",
            "a paper has been drafted, submitted, or published",
        ],
    }


def main() -> None:
    result = build_result()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"{result['status']}: {result['checks_passed']}/"
        f"{result['checks_total']} checks; "
        f"{result['candidate_count']} candidates; wrote {OUTPUT.relative_to(ROOT)}"
    )
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
