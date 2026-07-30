#!/usr/bin/env python3
"""Validate retention and gating of the minimal-antecedent campaign.

Passing establishes only that the campaign preserves its declared seeds,
contains ten ordered conditional swing cards, and exposes one explicit first
activation packet. It establishes no theorem, selector, record, ontology,
reconstruction, remainder, new law, prediction, or paper readiness.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN = (
    ROOT
    / "explorations"
    / "minimal-physical-antecedent-to-finite-remainder-coherent-campaign-2026-07-30.md"
)
CONCEPTS = ROOT / "explorations" / "concept-register.md"
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_minimal_antecedent_campaign_result.json"
)
SEEDS = tuple(f"SEED-DU-MPA-{index:02d}" for index in range(1, 18))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    campaign_text = CAMPAIGN.read_text(encoding="utf-8")
    concept_text = CONCEPTS.read_text(encoding="utf-8")

    campaign_seed_counts = {
        seed: campaign_text.count(seed)
        for seed in SEEDS
    }
    concept_seed_counts = {
        seed: concept_text.count(seed)
        for seed in SEEDS
    }
    swing_numbers = [
        int(value)
        for value in re.findall(
            r"^## Swing ([1-9]|10) —",
            campaign_text,
            flags=re.MULTILINE,
        )
    ]

    checks = {
        "all_seeds_in_campaign": all(
            count >= 1 for count in campaign_seed_counts.values()
        ),
        "all_seeds_in_concept_register": all(
            count >= 1 for count in concept_seed_counts.values()
        ),
        "ten_ordered_swing_cards": swing_numbers == list(range(1, 11)),
        "single_executable_gate_declared": (
            "Only Swing 1 is executable." in campaign_text
            and "Swings 2--10 are prepared, not preauthorized." in campaign_text
        ),
        "transition_automaton_present": "## Transition automaton" in campaign_text,
        "activation_packet_present": "## Swing 1 activation packet" in campaign_text,
        "grade_zero_boundary_present": "This scaffold is Grade 0." in campaign_text,
        "concept_family_open": (
            "## CONCEPT-DU-019" in concept_text
            and "CONCEPT-OPEN" in concept_text
            and "SEED-DU-MPA-17" in concept_text
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"minimal-antecedent campaign checks failed: {failed}")

    result = {
        "probe": "du_minimal_antecedent_campaign_probe",
        "status": "PASS",
        "scope": "campaign_retention_and_gating_only",
        "seed_count": len(SEEDS),
        "swing_count": len(swing_numbers),
        "checks": checks,
        "disclaimer": (
            "Passing establishes campaign preservation and gating only; "
            "it establishes no scientific result."
        ),
    }
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
