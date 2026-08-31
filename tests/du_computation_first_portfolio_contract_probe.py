#!/usr/bin/env python3
"""Validate the computation-first closed-transition hypothesis portfolio.

This is a governance and completeness control.  It is not scientific evidence
for any hypothesis in the portfolio.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_PATH = (
    ROOT
    / "lab"
    / "process"
    / "computation-first-closed-transition-hypothesis-portfolio.json"
)
ARTIFACT_PATH = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_computation_first_portfolio_contract_result.json"
)

EXPECTED_HYPOTHESES = {f"CTS-H{index}" for index in range(1, 9)}
REQUIRED_HYPOTHESIS_FIELDS = {
    "id",
    "title",
    "statement",
    "role",
    "status",
    "evidence_grade",
    "maximum_evidence_grade",
    "warrants",
    "depends_on",
    "closest_du_results",
    "strongest_absorbers",
    "decisive_question",
    "cheapest_kill",
    "advancement_gate",
}


def load_portfolio() -> dict[str, Any]:
    with PORTFOLIO_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def dependency_cycle(
    hypothesis_id: str,
    dependencies: dict[str, list[str]],
    visiting: set[str],
    visited: set[str],
) -> bool:
    if hypothesis_id in visiting:
        return True
    if hypothesis_id in visited:
        return False
    visiting.add(hypothesis_id)
    for dependency in dependencies[hypothesis_id]:
        if dependency_cycle(dependency, dependencies, visiting, visited):
            return True
    visiting.remove(hypothesis_id)
    visited.add(hypothesis_id)
    return False


def run_checks(portfolio: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    hypotheses = portfolio.get("hypotheses", [])
    hypothesis_ids = [item.get("id") for item in hypotheses]
    hypothesis_id_set = set(hypothesis_ids)
    check(
        "eight_unique_hypothesis_families",
        len(hypotheses) == 8
        and len(hypothesis_ids) == len(hypothesis_id_set)
        and hypothesis_id_set == EXPECTED_HYPOTHESES,
        f"ids={sorted(hypothesis_id_set)}",
    )

    missing_fields = {
        item.get("id", f"index-{index}"): sorted(
            REQUIRED_HYPOTHESIS_FIELDS - set(item)
        )
        for index, item in enumerate(hypotheses)
        if REQUIRED_HYPOTHESIS_FIELDS - set(item)
    }
    check(
        "hypothesis_contract_complete",
        not missing_fields,
        f"missing={missing_fields}",
    )

    ungraded_or_promoted = [
        item["id"]
        for item in hypotheses
        if item.get("status") != "open_conditional"
        or item.get("evidence_grade") != 0
        or item.get("maximum_evidence_grade") not in {4, 5}
    ]
    check(
        "conditional_grade_boundary",
        not ungraded_or_promoted,
        f"invalid={ungraded_or_promoted}",
    )

    empty_controls = [
        item["id"]
        for item in hypotheses
        if not item.get("closest_du_results")
        or not item.get("strongest_absorbers")
        or not str(item.get("decisive_question", "")).strip()
        or not str(item.get("cheapest_kill", "")).strip()
        or not str(item.get("advancement_gate", "")).strip()
    ]
    check(
        "absorber_falsifier_and_gate_present",
        not empty_controls,
        f"invalid={empty_controls}",
    )

    dependencies = {
        item["id"]: list(item.get("depends_on", [])) for item in hypotheses
    }
    unknown_dependencies = {
        hypothesis_id: sorted(set(items) - hypothesis_id_set)
        for hypothesis_id, items in dependencies.items()
        if set(items) - hypothesis_id_set
    }
    check(
        "dependencies_resolve",
        not unknown_dependencies,
        f"unknown={unknown_dependencies}",
    )

    visited: set[str] = set()
    has_cycle = any(
        dependency_cycle(hypothesis_id, dependencies, set(), visited)
        for hypothesis_id in sorted(hypothesis_id_set)
    )
    check("dependency_graph_acyclic", not has_cycle, f"cycle={has_cycle}")

    lenses = portfolio.get("lens_mappings", [])
    lens_names = [item.get("lens") for item in lenses]
    check(
        "twenty_unique_lenses",
        len(lenses) == 20 and len(lens_names) == len(set(lens_names)),
        f"count={len(lenses)} unique={len(set(lens_names))}",
    )

    bad_lens_mappings = [
        item.get("lens")
        for item in lenses
        if len(item.get("hypothesis_ids", [])) != 2
        or len(set(item.get("hypothesis_ids", []))) != 2
        or not set(item.get("hypothesis_ids", [])).issubset(hypothesis_id_set)
        or not str(item.get("obvious_shape", "")).strip()
    ]
    check(
        "forty_valid_lens_mappings",
        not bad_lens_mappings
        and sum(len(item.get("hypothesis_ids", [])) for item in lenses) == 40,
        f"invalid={bad_lens_mappings}",
    )

    mapped_ids = {
        hypothesis_id
        for item in lenses
        for hypothesis_id in item.get("hypothesis_ids", [])
    }
    check(
        "every_hypothesis_has_lens_support",
        mapped_ids == hypothesis_id_set,
        f"mapped={sorted(mapped_ids)}",
    )

    campaign = portfolio.get("campaign", [])
    positions = [item.get("position") for item in campaign]
    action_ids = [item.get("action_id") for item in campaign]
    executable = [
        item.get("action_id")
        for item in campaign
        if item.get("status") == "executable"
    ]
    check(
        "five_ordered_campaign_positions",
        positions == [1, 2, 3, 4, 5]
        and len(action_ids) == len(set(action_ids)),
        f"positions={positions}",
    )
    check(
        "sole_executable_next_action",
        executable == ["CTS-A2-COMMON-VIEW-CLOSURE-SELECTOR-OR-OBSTRUCTION"]
        and campaign[0].get("status") == "complete"
        and all(
            item.get("status") == "conditional"
            for item in campaign
            if item.get("position") not in {1, 2}
        ),
        f"executable={executable}",
    )

    campaign_ids = {
        hypothesis_id
        for item in campaign
        for hypothesis_id in item.get("hypothesis_ids", [])
    }
    invalid_campaign_ids = campaign_ids - hypothesis_id_set
    check(
        "campaign_covers_all_hypotheses_once_or_more",
        campaign_ids == hypothesis_id_set and not invalid_campaign_ids,
        f"covered={sorted(campaign_ids)}",
    )

    check(
        "anti_vacuity_contract_present",
        len(portfolio.get("anti_vacuity_rules", [])) >= 6
        and len(portfolio.get("standard_nulls", [])) >= 5
        and "external interpreter" in " ".join(
            portfolio.get("anti_vacuity_rules", [])
        ).lower(),
        (
            f"rules={len(portfolio.get('anti_vacuity_rules', []))} "
            f"nulls={len(portfolio.get('standard_nulls', []))}"
        ),
    )

    passed = sum(1 for item in checks if item["passed"])
    return {
        "probe": "du_computation_first_portfolio_contract_probe",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "program_id": portfolio.get("program_id"),
        "hypothesis_count": len(hypotheses),
        "lens_count": len(lenses),
        "lens_hypothesis_mapping_count": sum(
            len(item.get("hypothesis_ids", [])) for item in lenses
        ),
        "campaign_position_count": len(campaign),
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "scientific_boundary": (
            "Portfolio completeness and routing only; no hypothesis, physical "
            "law, ontology, prediction, or evidence grade is established."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="Write the deterministic result under tests/artifacts/.",
    )
    args = parser.parse_args()

    result = run_checks(load_portfolio())
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write_artifact:
        ARTIFACT_PATH.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
