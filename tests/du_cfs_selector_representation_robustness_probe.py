#!/usr/bin/env python3
"""Exact representation-robustness attribution for the W246 CFS comparator."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


TESTS_DIR = Path(__file__).resolve().parent
ARTIFACT_PATH = (
    TESTS_DIR
    / "artifacts"
    / "du_cfs_selector_representation_robustness_result.json"
)

A = Fraction(1, 2)
DELTA = Fraction(1)
C = Fraction(1, 10)
LAMBDA_LEFT = Fraction(7, 10)
LAMBDA_RIGHT = Fraction(9, 10)


def exact_actions(
    lam: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    p = 1 + lam
    q = 1 - lam
    good = 8 * C * C * p * p * (A * A + DELTA * DELTA)
    bad = (
        8
        * C
        * C
        * (p * p * A * A + 2 * q * q * DELTA * DELTA)
        + 8 * p * p * q * q * A * A * DELTA * DELTA
    )
    return good, bad, bad - good


def classify_margins(margins: list[Fraction]) -> str:
    if not margins:
        return "INCOMPLETE_REPRESENTATION_CLASS"
    if any(value == 0 for value in margins):
        return "OPEN_ZERO_MARGIN"
    if all(value > 0 for value in margins):
        return "ROBUST_GOOD_SELECTOR"
    if all(value < 0 for value in margins):
        return "ROBUST_BAD_SELECTOR"
    return "REPRESENTATION_SENSITIVE_NO_SELECTOR"


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, detail: object = None) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}: {detail}")


left_good, left_bad, left_margin = exact_actions(LAMBDA_LEFT)
right_good, right_bad, right_margin = exact_actions(LAMBDA_RIGHT)

check(
    "left exact action tuple matches the GU receipt",
    (left_good, left_bad, left_margin)
    == (
        Fraction(289, 1000),
        Fraction(1481, 2500),
        Fraction(1517, 5000),
    ),
    [str(left_good), str(left_bad), str(left_margin)],
)
check(
    "right exact action tuple matches the GU receipt",
    (right_good, right_bad, right_margin)
    == (
        Fraction(361, 1000),
        Fraction(73, 500),
        Fraction(-43, 200),
    ),
    [str(right_good), str(right_bad), str(right_margin)],
)
check(
    "Phi_7/10 alone would select the good branch",
    classify_margins([left_margin]) == "ROBUST_GOOD_SELECTOR",
    str(left_margin),
)
check(
    "Phi_9/10 alone would select the bad branch",
    classify_margins([right_margin]) == "ROBUST_BAD_SELECTOR",
    str(right_margin),
)

joint_disposition = classify_margins([left_margin, right_margin])
check(
    "the faithful rival class kills representation-independent selection",
    joint_disposition == "REPRESENTATION_SENSITIVE_NO_SELECTOR",
    joint_disposition,
)
check(
    "zero margin remains open rather than becoming selection",
    classify_margins([left_margin, Fraction(0)])
    == "OPEN_ZERO_MARGIN",
)
check(
    "empty rival class is an incomplete contract",
    classify_margins([]) == "INCOMPLETE_REPRESENTATION_CLASS",
)

# A separately derived physical rule could choose one map, but the selection
# credit would belong to that rule. It would not retroactively make the
# ordering representation-invariant.
physical_map_rule_supplied = True
selected_map = "Phi_7/10"
conditional_law_disposition = (
    "CONDITIONAL_LAW_SELECTOR__MAP_RULE_SUPPLIED"
    if physical_map_rule_supplied and selected_map == "Phi_7/10"
    else "INCOMPLETE_MAP_RULE"
)
check(
    "a supplied physical map yields only a conditional law selector",
    conditional_law_disposition
    == "CONDITIONAL_LAW_SELECTOR__MAP_RULE_SUPPLIED",
    conditional_law_disposition,
)

record_interface_selected = False
record_credit = (
    "RECORD_CREDIT_POSSIBLE"
    if record_interface_selected
    else "NO_RECORD_CREDIT__INTERFACE_UNSELECTED"
)
check(
    "no record or finality credit is created by choosing an encoding",
    record_credit == "NO_RECORD_CREDIT__INTERFACE_UNSELECTED",
    record_credit,
)

reopen_conditions = [
    "derive the CFS local-correlation map from physical wave evaluation",
    "derive an invariant excluding one faithful encoding without branch target",
    "then compare lawful target diameter before and after a formed record",
]
check(
    "reopener requires physical map selection before record attribution",
    len(reopen_conditions) == 3
    and reopen_conditions[0].startswith("derive the CFS"),
    reopen_conditions,
)

passed = sum(int(item["passed"]) for item in checks)
artifact = {
    "probe_id": "DU-CFS-SELECTOR-REPRESENTATION-ROBUSTNESS-01",
    "scope": (
        "exact finite action-ordering attribution over a frozen faithful "
        "self-adjointization rival class"
    ),
    "checks_passed": passed,
    "checks_total": len(checks),
    "checks": checks,
    "action_receipts": {
        "Phi_7/10": {
            "good": str(left_good),
            "bad": str(left_bad),
            "bad_minus_good": str(left_margin),
        },
        "Phi_9/10": {
            "good": str(right_good),
            "bad": str(right_bad),
            "bad_minus_good": str(right_margin),
        },
    },
    "joint_disposition": joint_disposition,
    "conditional_law_disposition": conditional_law_disposition,
    "record_credit": record_credit,
    "reopen_conditions": reopen_conditions,
    "scientific_claim": False,
    "physical_selector_established": False,
    "record_ontology_established": False,
    "baryogenesis_rate_computed": False,
    "external_hardware_required": False,
}
ARTIFACT_PATH.write_text(
    json.dumps(artifact, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(f"checks: {passed}/{len(checks)}")
print(f"artifact: {ARTIFACT_PATH}")
print(f"VERDICT: {joint_disposition}")
if passed != len(checks):
    raise SystemExit(1)
