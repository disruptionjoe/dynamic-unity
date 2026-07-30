#!/usr/bin/env python3
"""Validate the physical-descent ten-swing campaign contract.

Passing establishes method completeness, conditional ordering, and live
Swing-1 routing only. It establishes no physics, theorem, novelty, prediction,
scientific grade, paper readiness, or authorization beyond the active action.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN = (
    ROOT
    / "explorations"
    / "physical-descent-selected-interface-ten-swing-campaign-2026-07-30.md"
)
CURRENT = ROOT / "CURRENT-RESEARCH.yaml"
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_physical_descent_ten_swing_campaign_result.json"
)
PROGRAM_ID = "CCR-PHYSICAL-RECORD-INTERFACE-SELECTION"
ACTION_ID = "PDSI-01-PHYSICAL-APPARATUS-CLASS-EXTRACTION"

EXPECTED_TITLES = [
    "physical apparatus class extraction",
    "admissible tangent and response-span compiler",
    "uniform apparatus-descent theorem or lawful counterexample",
    "no-refit held-out apparatus transfer",
    "complete relational probability closure",
    "equivariant interface selection or nonselection theorem",
    "direct-action versus field first leak",
    "formation and provenance intervention",
    "regional composition and perspectival curvature",
    "flagship synthesis and North-Star adjudication",
]
REQUIRED_CARD_FIELDS = [
    "**Exact question.**",
    "**Activation.**",
    "**Efficient method.**",
    "**Positive.**",
    "**Cheapest kill.**",
    "**Durable return.**",
    "**Next.**",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    text = CAMPAIGN.read_text(encoding="utf-8")
    flat_text = re.sub(r"\s+", " ", text)
    current = yaml.safe_load(CURRENT.read_text(encoding="utf-8"))
    checks: list[dict[str, object]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{check_id}: {detail}")
        checks.append({"id": check_id, "pass": True, "detail": detail})

    headings = re.findall(r"^## Swing (\d+) — (.+)$", text, flags=re.MULTILINE)
    check(
        "ten_ordered_swings",
        [int(number) for number, _ in headings] == list(range(1, 11))
        and [title.strip() for _, title in headings] == EXPECTED_TITLES,
        "campaign has the exact ten ordered swing titles",
    )

    card_errors: list[str] = []
    for index, (number, _) in enumerate(headings):
        start = text.index(f"## Swing {number} —")
        end = (
            text.index(f"## Swing {int(number) + 1} —")
            if index + 1 < len(headings)
            else text.index("## Transition logic")
        )
        card = text[start:end]
        missing = [field for field in REQUIRED_CARD_FIELDS if field not in card]
        if missing:
            card_errors.append(f"S{number}:{missing}")
    check(
        "complete_swing_cards",
        not card_errors,
        f"every swing has question, activation, method, positive, kill, return, and next; errors={card_errors}",
    )

    lens_markers = [
        "Counterfactual statistician",
        "Category/naturality theorist",
        "Control/identifiability theorist",
        "Adjoint-sensitivity specialist",
        "Value-of-information experimental designer",
        "Gauge/QFT physicist",
        "Direct-action theorist",
        "Metrologist",
        "Adversarial proof engineer",
        "Overbuild-protection champion",
    ]
    check(
        "divergent_method_coverage",
        all(marker in text for marker in lens_markers),
        "all ten divergent specialist lenses are present",
    )
    check(
        "triple_diamond_and_convergence",
        all(
            marker in text
            for marker in (
                "### Diamond 1 — purpose",
                "### Diamond 2 — architecture",
                "### Diamond 3 — assurance",
                "The converged method stack is:",
            )
        ),
        "purpose, architecture, and assurance diamonds converge explicitly",
    )
    check(
        "anti_bruteforce_contract",
        all(
            marker in text
            for marker in (
                "Brute-force controller enumeration",
                "One adjoint response solve",
                "maximal expected rank/discrimination",
                "If direct analysis already decides the boundary, computation is disallowed.",
            )
        ),
        "symmetry, adjoint, value-of-information, and local-learning shortcuts replace brute force",
    )
    check(
        "conditional_transition_contract",
        "Only Swing 1 is executable" in flat_text
        and "Swings 2--10 are prepared but blocked by typed returns" in flat_text
        and "The chair may skip a later swing" in flat_text,
        "only Swing 1 is live and every later swing is conditional",
    )
    check(
        "typed_and_grade_guards",
        all(
            marker in text
            for marker in (
                "Shared campaign contract",
                "Council agreement is not evidence.",
                "No paper, prediction, hardware run",
            )
        ),
        "typed ledger, evidence-grade, and external-action guards are explicit",
    )

    programs = {program["id"]: program for program in current["programs"]}
    program = programs[PROGRAM_ID]
    decision = current["current_decision"]
    successor = current["successor_selection"]
    check(
        "live_swing_one_routing",
        program["portfolio_status"] == "active"
        and program["execution_status"] == "executable"
        and program["active_work_id"] == ACTION_ID
        and decision["active_scientific_program_id"] == PROGRAM_ID
        and decision["executable_action_id"] == ACTION_ID
        and program["execution_packet"]["action_id"] == ACTION_ID,
        "current authority routes exactly the selected program and Swing 1",
    )
    check(
        "later_swings_blocked",
        successor["status"] == "blocked"
        and successor["blocked_by"] == ACTION_ID
        and successor["selected_successor_id"] is None,
        "successor selection is blocked by the live Swing-1 return",
    )
    check(
        "source_locator_resolves",
        program["execution_packet"]["source_locator"]["path"]
        == str(CAMPAIGN.relative_to(ROOT))
        and program["execution_packet"]["source_locator"]["heading"] in text,
        "the embedded execution packet resolves to the Swing-1 card",
    )

    result = {
        "probe": "du_physical_descent_ten_swing_campaign_probe",
        "status": "PASS",
        "checks": checks,
        "scientific_claim": "none",
        "active_program": PROGRAM_ID,
        "active_action": ACTION_ID,
        "prepared_swings": 10,
        "executable_swings": 1,
        "limitations": [
            "Does not validate any physical model or scientific claim.",
            "Does not authorize Swings 2-10, hardware, publication, or contact.",
            "Does not establish novelty, paper readiness, or a North-Star result.",
        ],
    }
    if args.write_artifact:
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
