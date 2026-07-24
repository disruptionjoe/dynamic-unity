#!/usr/bin/env python3
"""Build the commercial comparison surface for SWING-DU-SCI-01.

The script aggregates candidate contracts and results without turning metadata,
check counts, or persona agreement into a scientific score.  Each underlying
probe owns its scientific grade; this surface makes the three grades and their
epistemic costs comparable.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    validate_candidate_contract,
)


TESTS_DIR = Path(__file__).resolve().parent
ARTIFACTS = (
    TESTS_DIR / "artifacts" / "du_bianconi_completion_robustness_probe_result.json",
    TESTS_DIR / "artifacts" / "du_influence_redistribution_abduction_probe_result.json",
    TESTS_DIR / "artifacts" / "du_conditional_finality_knee_probe_result.json",
)
OUTPUT = (
    TESTS_DIR
    / "artifacts"
    / "du_science_council_three_track_comparison_result.json"
)


def load_artifact(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    candidate = data.get("candidate_contract")
    receipt = data.get("comparison_receipt")
    if not isinstance(candidate, dict) or not isinstance(receipt, dict):
        raise ValueError(f"{path}: missing candidate_contract or comparison_receipt")
    errors = validate_candidate_contract(candidate)
    if errors:
        raise ValueError(f"{path}: contract errors: {errors}")
    if receipt.get("contract_status") != "COMPLETE":
        raise ValueError(f"{path}: stored receipt is not COMPLETE")
    return data


def comparison_row(path: Path, artifact: dict[str, Any]) -> dict[str, Any]:
    candidate = artifact["candidate_contract"]
    receipt = artifact["comparison_receipt"]
    result = candidate["result"]
    concept = candidate.get("concept")
    return {
        "artifact": str(path.relative_to(TESTS_DIR.parent)),
        "candidate_id": candidate["candidate_id"],
        "track": candidate["track"],
        "warrants": candidate["warrants"],
        "admission": result["admission"],
        "grade": result["grade"],
        "claim": result["claim"],
        "remaining_uncertainty": result["remaining_uncertainty"],
        "assumption_count": receipt["assumption_count"],
        "free_choice_count": receipt["free_choice_count"],
        "observable_count": receipt["observable_count"],
        "null_model_count": receipt["null_model_count"],
        "falsifier_count": receipt["falsifier_count"],
        "checks": {
            "passed": receipt["checks_passed"],
            "total": receipt["checks_total"],
        },
        "concept_failure_scope": (
            concept.get("failure_scope") if isinstance(concept, dict) else None
        ),
        "stop_conditions": candidate["stop_conditions"],
        "scientific_endorsement": receipt["scientific_endorsement"],
    }


def main() -> None:
    loaded = [(path, load_artifact(path)) for path in ARTIFACTS]
    rows = [comparison_row(path, artifact) for path, artifact in loaded]

    candidate_ids = [row["candidate_id"] for row in rows]
    warrant_counts = Counter(
        warrant for row in rows for warrant in row["warrants"]
    )
    checks = [
        {
            "name": "all three candidate contracts are complete",
            "pass": len(rows) == 3,
        },
        {
            "name": "candidate identifiers are unique",
            "pass": len(set(candidate_ids)) == len(candidate_ids),
        },
        {
            "name": "no comparison receipt claims scientific endorsement",
            "pass": all(not row["scientific_endorsement"] for row in rows),
        },
        {
            "name": "every track exposes a null, falsifier, and stop condition",
            "pass": all(
                row["null_model_count"] > 0
                and row["falsifier_count"] > 0
                and bool(row["stop_conditions"])
                for row in rows
            ),
        },
        {
            "name": "no track silently promotes itself to bank review",
            "pass": all(row["admission"] != "BANK_REVIEW_ONLY" for row in rows),
        },
    ]

    output = {
        "swing": "SWING-DU-SCI-01",
        "instrument": SCHEMA_VERSION,
        "aggregation_rule": (
            "No scalar score, vote, or automatic winner. Compare typed warrants, "
            "free choices, null absorption, robustness, and stop conditions. "
            "Scientific grades remain owned by the underlying probes."
        ),
        "rows": rows,
        "warrant_coverage": dict(sorted(warrant_counts.items())),
        "checks": checks,
        "checks_passed": sum(bool(check["pass"]) for check in checks),
        "checks_total": len(checks),
        "scientific_endorsement": False,
        "admission_boundary": (
            "The surface is ready for human/scientific synthesis when all contracts "
            "are complete. It cannot bank, seed, or promote any candidate."
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for row in rows:
        print(
            f"{row['candidate_id']}: {row['admission']} | "
            f"{row['free_choice_count']} free choices | "
            f"{row['checks']['passed']}/{row['checks']['total']} checks"
        )
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    passed = sum(bool(check["pass"]) for check in checks)
    print(f"{passed}/{len(checks)} comparison-surface checks pass")
    print("No scalar ranking or scientific endorsement was produced.")
    print(f"artifact: {OUTPUT}")
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"comparison surface failed: {failed}")


if __name__ == "__main__":
    main()
