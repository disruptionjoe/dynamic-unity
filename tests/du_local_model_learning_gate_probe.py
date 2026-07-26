#!/usr/bin/env python3
"""Deterministic controls for the repository-wide local model learning gate.

This probe classifies proposed research builds.  It does not build a model,
run a simulation, establish novelty, or make a physical claim.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT / "tests" / "artifacts" / "du_local_model_learning_gate_result.json"
)
RUN_ID = "RUN-20260726-100135-local-model-learning-gate"

REQUIRED_FIELDS = {
    "question",
    "research_only_baseline",
    "local_learning_delta",
    "generated_not_encoded",
    "pre_hardware_checkpoint",
    "decision_changed",
    "minimal_build",
    "stop_and_hardware_boundary",
}

ADMIT = "ADMIT_LOCAL_LEARNING_BUILD"
DESK_FIRST = "DESK_RESEARCH_FIRST"
EXTERNAL_STOP = "EXTERNAL_PAYOFF_ONLY_STOP"
INCOMPLETE = "INCOMPLETE_LEARNING_CONTRACT"
NO_VALUE = "NO_DECISION_VALUE_STOP"
REDUCE = "REDUCE_BEFORE_ADMISSION"
STOP_NO_LEARNING = "STOP_NO_LOCAL_LEARNING"


def complete_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def missing_contract_fields(proposal: dict[str, Any]) -> list[str]:
    missing = sorted(REQUIRED_FIELDS - set(proposal))
    text_fields = REQUIRED_FIELDS - {
        "generated_not_encoded",
        "decision_changed",
    }
    missing.extend(
        sorted(
            field
            for field in text_fields
            if field in proposal and not complete_text(proposal[field])
        )
    )
    if "generated_not_encoded" in proposal and not isinstance(
        proposal["generated_not_encoded"], bool
    ):
        missing.append("generated_not_encoded")
    decisions = proposal.get("decision_changed")
    if not (
        isinstance(decisions, dict)
        and set(decisions) == {"positive", "negative", "null"}
        and all(isinstance(value, bool) for value in decisions.values())
    ):
        missing.append("decision_changed")
    return sorted(set(missing))


def classify(proposal: dict[str, Any]) -> str:
    if missing_contract_fields(proposal):
        return INCOMPLETE
    if not proposal.get("pre_hardware_learning_available", False):
        return EXTERNAL_STOP
    if proposal.get("research_only_same_grade", False):
        return DESK_FIRST
    if not proposal["generated_not_encoded"]:
        return DESK_FIRST
    if not any(proposal["decision_changed"].values()):
        return NO_VALUE
    if not proposal.get("is_minimal", False):
        return REDUCE
    return ADMIT


def checkpoint(
    proposal: dict[str, Any],
    *,
    learning_obtained: bool,
    decision_changing_null: bool = False,
    external_dependency_arrived_early: bool = False,
) -> str:
    if classify(proposal) != ADMIT:
        return "NOT_ADMITTED"
    if external_dependency_arrived_early:
        return EXTERNAL_STOP
    if learning_obtained:
        return "BANK_LOCAL_LEARNING"
    if decision_changing_null:
        return "BANK_DECISION_CHANGING_NULL"
    return STOP_NO_LEARNING


def base_proposal() -> dict[str, Any]:
    return {
        "question": "What is the minimum same-record separating process pair?",
        "research_only_baseline": (
            "Finite factorization theory guarantees a witness but does not "
            "supply the smallest specimen in the frozen completion class."
        ),
        "local_learning_delta": (
            "Generate the exact smallest counterexample and theorem boundary."
        ),
        "generated_not_encoded": True,
        "pre_hardware_checkpoint": (
            "Exact minimal pair and its separating intervention."
        ),
        "decision_changed": {
            "positive": True,
            "negative": True,
            "null": True,
        },
        "minimal_build": "Exhaustive exact-rational search over the frozen class.",
        "stop_and_hardware_boundary": (
            "Stop after minimality proof; hardware may later instantiate the pair."
        ),
        "pre_hardware_learning_available": True,
        "research_only_same_grade": False,
        "is_minimal": True,
    }


def scenarios() -> list[dict[str, Any]]:
    counterexample = base_proposal()

    published_curve = {
        **base_proposal(),
        "question": "Does a published dephasing model reproduce its published curve?",
        "research_only_same_grade": True,
        "local_learning_delta": "Reproduce the already published curve.",
    }
    provider_adapter = {
        **base_proposal(),
        "question": "What result will a provider return from a real device?",
        "pre_hardware_learning_available": False,
        "pre_hardware_checkpoint": "Adapter imports and validates.",
        "local_learning_delta": "First informative result arrives from hardware.",
    }
    minimum_experiment = {
        **base_proposal(),
        "question": "What is the minimum intervention basis and shot margin?",
        "local_learning_delta": (
            "Compute the exact basis and sample-complexity boundary locally."
        ),
        "pre_hardware_checkpoint": "Minimum basis and finite-shot bound.",
        "stop_and_hardware_boundary": (
            "Stop at experimental-theory result; hardware may estimate parameters."
        ),
    }
    target_encoded = {
        **base_proposal(),
        "question": "Does a target-coded fixture return its encoded target?",
        "generated_not_encoded": False,
    }
    no_decision_value = {
        **base_proposal(),
        "question": "Can a larger fixture produce more examples?",
        "decision_changed": {
            "positive": False,
            "negative": False,
            "null": False,
        },
    }
    oversized = {
        **base_proposal(),
        "question": "Can a large neural surrogate find the finite counterexample?",
        "minimal_build": "Train a large surrogate before exact enumeration.",
        "is_minimal": False,
    }
    missing_baseline = base_proposal()
    del missing_baseline["research_only_baseline"]

    return [
        {
            "id": "finite_counterexample_search",
            "proposal": counterexample,
            "expected": ADMIT,
        },
        {
            "id": "published_curve_reproduction",
            "proposal": published_curve,
            "expected": DESK_FIRST,
        },
        {
            "id": "provider_adapter_first_payoff_external",
            "proposal": provider_adapter,
            "expected": EXTERNAL_STOP,
        },
        {
            "id": "minimum_discriminating_experiment",
            "proposal": minimum_experiment,
            "expected": ADMIT,
        },
        {
            "id": "target_encoded_fixture",
            "proposal": target_encoded,
            "expected": DESK_FIRST,
        },
        {
            "id": "no_decision_value",
            "proposal": no_decision_value,
            "expected": NO_VALUE,
        },
        {
            "id": "oversized_before_minimal",
            "proposal": oversized,
            "expected": REDUCE,
        },
        {
            "id": "missing_research_baseline",
            "proposal": missing_baseline,
            "expected": INCOMPLETE,
        },
    ]


def build_result() -> dict[str, Any]:
    cases = scenarios()
    outcomes = [
        {
            "id": case["id"],
            "expected": case["expected"],
            "actual": classify(case["proposal"]),
        }
        for case in cases
    ]
    admitted = {
        case["id"]: case["proposal"]
        for case in cases
        if classify(case["proposal"]) == ADMIT
    }

    checks = {
        "all_eight_contract_fields_are_required": len(REQUIRED_FIELDS) == 8,
        "all_scenarios_match_expected_disposition": all(
            outcome["actual"] == outcome["expected"] for outcome in outcomes
        ),
        "finite_counterexample_search_is_admitted": (
            classify(cases[0]["proposal"]) == ADMIT
        ),
        "published_result_reproduction_routes_to_research": (
            classify(cases[1]["proposal"]) == DESK_FIRST
        ),
        "hardware_first_adapter_is_stopped": (
            classify(cases[2]["proposal"]) == EXTERNAL_STOP
        ),
        "minimum_experiment_design_is_admitted": (
            classify(cases[3]["proposal"]) == ADMIT
        ),
        "target_encoded_fixture_is_not_learning": (
            classify(cases[4]["proposal"]) == DESK_FIRST
        ),
        "no_decision_value_is_stopped": (
            classify(cases[5]["proposal"]) == NO_VALUE
        ),
        "oversized_build_is_reduced_first": (
            classify(cases[6]["proposal"]) == REDUCE
        ),
        "missing_research_baseline_is_incomplete": (
            classify(cases[7]["proposal"]) == INCOMPLETE
        ),
        "positive_local_checkpoint_banks_learning": (
            checkpoint(
                admitted["finite_counterexample_search"],
                learning_obtained=True,
            )
            == "BANK_LOCAL_LEARNING"
        ),
        "decision_changing_null_is_bankable": (
            checkpoint(
                admitted["minimum_discriminating_experiment"],
                learning_obtained=False,
                decision_changing_null=True,
            )
            == "BANK_DECISION_CHANGING_NULL"
        ),
        "failed_learning_checkpoint_stops_build": (
            checkpoint(
                admitted["finite_counterexample_search"],
                learning_obtained=False,
            )
            == STOP_NO_LEARNING
        ),
        "early_hardware_dependency_stops_build": (
            checkpoint(
                admitted["minimum_discriminating_experiment"],
                learning_obtained=False,
                external_dependency_arrived_early=True,
            )
            == EXTERNAL_STOP
        ),
        "hardware_may_extend_but_not_originate_learning": (
            all(
                proposal["pre_hardware_learning_available"]
                and "hardware may" in proposal["stop_and_hardware_boundary"].lower()
                for proposal in admitted.values()
            )
        ),
        "research_model_gate_does_not_claim_literature_novelty": True,
    }

    return {
        "run_id": RUN_ID,
        "contract_id": "LMLG-01",
        "claim_grade": (
            "LOCAL RESEARCH-MODEL ROUTING CONTROL; NO MODEL, NOVELTY, "
            "HARDWARE, OR PHYSICAL VERDICT"
        ),
        "rule": (
            "A local research build must generate decision-relevant learning "
            "before hardware and beyond the bounded research-only baseline."
        ),
        "scenario_outcomes": outcomes,
        "checkpoint_dispositions": {
            "learning_obtained": "BANK_LOCAL_LEARNING",
            "decision_changing_null": "BANK_DECISION_CHANGING_NULL",
            "no_local_learning": STOP_NO_LEARNING,
            "external_dependency_before_checkpoint": EXTERNAL_STOP,
        },
        "checks": checks,
        "summary": {
            "passed": sum(checks.values()),
            "total": len(checks),
            "all_passed": all(checks.values()),
        },
    }


def main() -> int:
    result = build_result()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = result["summary"]
    print(
        f"{summary['passed']}/{summary['total']} checks passed; "
        f"contract={result['contract_id']}"
    )
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
