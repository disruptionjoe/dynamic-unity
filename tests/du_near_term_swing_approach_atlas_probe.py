#!/usr/bin/env python3
"""Validate the near-term Dynamic Unity research-swing approach atlas.

This is a deterministic method, coverage, and routing check. It does not
evaluate scientific truth, theorem validity, novelty, priority, paper
readiness, Factory activation, or publication status.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = (
    ROOT
    / "explorations"
    / "near-term-research-swing-approach-atlas-2026-07-25.md"
)
PORTFOLIO = ROOT / "papers" / "paper-opportunity-portfolio.json"
METHOD_REGISTRY = (
    ROOT
    / "explorations"
    / "ten-lens-hypothesis-efficient-approach-registry-2026-07-24.md"
)
START_HERE = ROOT / "START-HERE.md"
LANES = ROOT / "LANES.yaml"
CURRENT_RESEARCH = ROOT / "CURRENT-RESEARCH.yaml"
OUTPUT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_near_term_swing_approach_atlas_result.json"
)

EXPECTED_FAMILIES = {
    "AF-01": {"DU-PAPER-005", "DU-PAPER-007", "DU-PAPER-008"},
    "AF-02": {"DU-PAPER-013"},
    "AF-03": {"DU-PAPER-006", "DU-PAPER-009", "DU-PAPER-022"},
    "AF-04": {"DU-PAPER-010", "DU-PAPER-021"},
    "AF-05": {"DU-PAPER-003", "DU-PAPER-004", "DU-PAPER-015"},
    "AF-06": {"DU-PAPER-016", "DU-PAPER-023"},
    "AF-07": {"DU-PAPER-017"},
    "AF-08": {"DU-PAPER-002", "DU-PAPER-018"},
    "AF-09": {"DU-PAPER-014"},
    "AF-10": {"DU-PAPER-011", "DU-PAPER-027"},
    "AF-11": {"DU-PAPER-019"},
    "AF-12": {"DU-PAPER-020"},
    "AF-13": {"DU-PAPER-001", "DU-PAPER-024"},
    "AF-14": {"DU-PAPER-012"},
    "AF-15": {"DU-PAPER-025", "DU-PAPER-026"},
}

REQUIRED_CARD_FIELDS = (
    "**Home and gate.**",
    "**CFS — decision and counterfactual.**",
    "**CAT — structure and gauge.**",
    "**MET — specimen and null.**",
    "**FPE — proof and verifier.**",
    "**VOI — first move, reusable output, scale, stop/reopen.**",
    "**Maximum grade.**",
)

MARKER = re.compile(
    r"<!-- approach-family: (?P<family>AF-\d{2}); "
    r"papers: (?P<papers>[^;]+); "
    r"lanes: (?P<lanes>[^;]+); "
    r"mode: (?P<mode>[^ ]+) -->"
)


def run() -> dict[str, object]:
    atlas_text = ATLAS.read_text(encoding="utf-8")
    atlas_flat = " ".join(atlas_text.split())
    portfolio = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
    start_text = START_HERE.read_text(encoding="utf-8")
    lanes_text = LANES.read_text(encoding="utf-8")
    current_text = CURRENT_RESEARCH.read_text(encoding="utf-8")
    matches = list(MARKER.finditer(atlas_text))
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    parsed: dict[str, dict[str, object]] = {}
    for index, match in enumerate(matches):
        family = match.group("family")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(
            atlas_text
        )
        body = atlas_text[match.end() : end]
        parsed[family] = {
            "papers": {
                value.strip() for value in match.group("papers").split(",")
            },
            "lanes": {
                value.strip() for value in match.group("lanes").split(",")
            },
            "mode": match.group("mode"),
            "body": body,
        }

    check(
        "family_ids_exact",
        set(parsed) == set(EXPECTED_FAMILIES),
        f"15 expected family IDs present: {sorted(parsed)}",
    )
    check(
        "family_mapping_exact",
        all(
            parsed[family]["papers"] == papers
            for family, papers in EXPECTED_FAMILIES.items()
        ),
        "each family has the expected portfolio membership",
    )

    actual_candidate_ids = [
        candidate["id"] for candidate in portfolio["candidates"]
    ]
    expected_candidate_ids = {
        f"DU-PAPER-{index:03d}" for index in range(1, 28)
    }
    flattened = [
        paper
        for family in sorted(parsed)
        for paper in sorted(parsed[family]["papers"])
    ]
    counts = Counter(flattened)
    check(
        "portfolio_is_complete",
        set(actual_candidate_ids) == expected_candidate_ids
        and len(actual_candidate_ids) == 27,
        "machine portfolio contains exactly DU-PAPER-001 through DU-PAPER-027",
    )
    check(
        "candidate_coverage_exact_once",
        set(flattened) == expected_candidate_ids
        and all(count == 1 for count in counts.values()),
        "all 27 candidates occur in exactly one approach family",
    )

    missing_fields = {
        family: [
            field
            for field in REQUIRED_CARD_FIELDS
            if field not in str(card["body"])
        ]
        for family, card in parsed.items()
        if any(
            field not in str(card["body"]) for field in REQUIRED_CARD_FIELDS
        )
    }
    check(
        "five_lens_card_contract",
        not missing_fields,
        f"all cards carry gate, five lenses, and ceiling; missing={missing_fields}",
    )

    lane_coverage = {
        lane
        for card in parsed.values()
        for lane in card["lanes"]
    }
    check(
        "active_lane_coverage",
        lane_coverage == {"1", "2", "3", "4", "5", "6", "7", "A"},
        f"every active dependency lane is represented: {sorted(lane_coverage)}",
    )
    check(
        "modes_declared",
        all(str(card["mode"]).strip() for card in parsed.values()),
        "every family declares its activation/routing mode",
    )

    check(
        "method_registry_reused",
        METHOD_REGISTRY.is_file()
        and METHOD_REGISTRY.name in atlas_text
        and "all 36 technical hypothesis IDs" in atlas_text,
        "the 36-hypothesis registry is linked rather than copied",
    )
    local_targets = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", atlas_text):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        local_targets.append((ATLAS.parent / target).resolve())
    missing_targets = [
        str(target.relative_to(ROOT))
        for target in local_targets
        if not target.is_file()
    ]
    check(
        "atlas_local_links_resolve",
        bool(local_targets) and not missing_targets,
        f"{len(local_targets)} local atlas links resolve; missing={missing_targets}",
    )
    check(
        "no_reranking_or_activation",
        "does **not** rank the families" in atlas_text
        and "It is not an execution queue." in atlas_flat
        and "No claim, theorem, prediction, paper priority" in atlas_text,
        "atlas explicitly changes method preparation only",
    )
    check(
        "two_horizon_state_preserved",
        "`DU-PAPER-013` is the nearer paper route" in atlas_text
        and "`DU-PAPER-007` the higher-ceiling" in atlas_text,
        "current nearer-paper and flagship distinction remains visible",
    )
    check(
        "four_scientific_returns",
        all(
            outcome in atlas_text
            for outcome in (
                "`FACTORIZATION`",
                "`MINIMAL_REFINEMENT`",
                "`CLASS_RELATIVE_REMAINDER`",
                "`INCOMPLETE_CONTRACT`",
            )
        ),
        "record-sufficiency return contract is explicit",
    )
    check(
        "nonoperationalization_guard",
        "## No-current-operationalization flags" in atlas_text
        and "Not yet operationalized" in atlas_text,
        "live concepts without a specimen or unit-bearing effect are gated",
    )
    check(
        "markdown_first_paper_rule",
        "Canonical paper hardening remains in Markdown" in atlas_flat
        and "Do not create TeX, PDF" in atlas_flat,
        "paper preparation honors the canonical-Markdown preference",
    )
    check(
        "non_authoritative_method_atlas",
        ATLAS.name not in start_text
        and ATLAS.name not in lanes_text
        and "CURRENT-RESEARCH.yaml" in start_text
        and "CURRENT-RESEARCH.yaml" in lanes_text
        and "near-term-research-swing-approach-atlas" not in current_text,
        "dated approach atlas remains available without routing current work",
    )
    check(
        "ownership_boundaries",
        portfolio["candidates"][24]["source_owner"] == "gu-formalization"
        and portfolio["candidates"][25]["source_owner"] == "ai-epistemology"
        and "transfer only" in atlas_text,
        "non-DU candidates retain their source owners",
    )

    result: dict[str, object] = {
        "artifact_type": "method_coverage_and_routing_check",
        "atlas": str(ATLAS.relative_to(ROOT)),
        "approach_family_count": len(parsed),
        "candidate_count": len(actual_candidate_ids),
        "claim_grade": (
            "METHOD AND APPROACH PREPARATION / NO SCIENTIFIC CLAIM, "
            "PRIORITY, FACTORY, OR EXECUTION PROMOTION"
        ),
        "lane_coverage": sorted(lane_coverage),
        "checks": checks,
        "checks_passed": len(checks),
        "all_passed": True,
    }
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = run()
    print(
        "PASS "
        f"{result['checks_passed']}/{result['checks_passed']} "
        f"families={result['approach_family_count']} "
        f"candidates={result['candidate_count']}"
    )
    print(f"artifact={OUTPUT.relative_to(ROOT)}")
    print(
        "GRADE: method/routing integrity only; no scientific, novelty, "
        "priority, Factory, manuscript, or publication verdict"
    )


if __name__ == "__main__":
    main()
