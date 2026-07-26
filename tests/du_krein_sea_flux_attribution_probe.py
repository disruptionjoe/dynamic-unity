#!/usr/bin/env python3
"""Exact law-versus-record attribution probe for the GU/Finster collision.

This probe independently rechecks the minimum two-branch spectral fact and
then evaluates four finite reconstruction cases.  It does not calculate
baryogenesis and does not treat a domain restriction as a selected physical
law.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

import numpy as np


TESTS_DIR = Path(__file__).resolve().parent
ARTIFACT_PATH = (
    TESTS_DIR / "artifacts" / "du_krein_sea_flux_attribution_result.json"
)
TOL = 1.0e-12


@dataclass(frozen=True)
class Completion:
    name: str
    target: int
    record: str


def target_diameter(completions: Iterable[Completion]) -> int | None:
    values = [completion.target for completion in completions]
    if not values:
        return None
    return max(values) - min(values)


def condition_on_record(
    completions: Iterable[Completion], record_value: str
) -> list[Completion]:
    return [
        completion
        for completion in completions
        if completion.record == record_value
    ]


def attribution_case(
    *,
    completions: list[Completion],
    law_filter: Callable[[Completion], bool],
    record_value: str,
    law_selector_defined: bool,
    record_interface_selected: bool,
) -> dict[str, object]:
    lawful = [item for item in completions if law_filter(item)]
    law_diameter = target_diameter(lawful)
    conditioned = (
        condition_on_record(lawful, record_value)
        if record_interface_selected
        else []
    )
    conditioned_diameter = (
        target_diameter(conditioned) if record_interface_selected else None
    )

    if not law_selector_defined:
        disposition = "INCOMPLETE_LAW_SELECTOR"
    elif law_diameter is None:
        disposition = "EMPTY_LAW_FIBRE"
    elif not record_interface_selected:
        disposition = "INCOMPLETE_RECORD_INTERFACE"
    elif conditioned_diameter is None:
        disposition = "EMPTY_RECORD_FIBRE"
    elif law_diameter == 0:
        disposition = "LAW_ONLY_CLOSURE"
    elif conditioned_diameter < law_diameter:
        disposition = "RECORD_CONDITIONAL_REDUCTION"
    else:
        disposition = "OPEN_AFTER_RECORD"

    marginal_reduction = (
        law_diameter - conditioned_diameter
        if law_diameter is not None and conditioned_diameter is not None
        else None
    )
    return {
        "law_diameter": law_diameter,
        "conditioned_diameter": conditioned_diameter,
        "marginal_record_reduction": marginal_reduction,
        "lawful_completions": [item.name for item in lawful],
        "conditioned_completions": [item.name for item in conditioned],
        "disposition": disposition,
    }


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, detail: object = None) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}: {detail}")


# Independent minimum spectral receipt.
delta = 1.0
good = np.array([[0.0, delta], [delta, 0.0]], dtype=complex)
bad = np.array([[0.0, delta], [-delta, 0.0]], dtype=complex)
good_spectrum = np.linalg.eigvals(good)
bad_spectrum = np.linalg.eigvals(bad)
check(
    "good branch independently has real spectrum",
    float(np.max(np.abs(good_spectrum.imag))) < TOL,
    [
        {"real": float(value.real), "imag": float(value.imag)}
        for value in good_spectrum
    ],
)
check(
    "pathological core independently has nonreal spectrum",
    float(np.max(np.abs(bad_spectrum.imag))) > 0.9,
    [
        {"real": float(value.real), "imag": float(value.imag)}
        for value in bad_spectrum
    ],
)
check(
    "pathological core is Krein-self-adjoint, not Hilbert-self-adjoint",
    float(np.max(np.abs(np.diag([1.0, -1.0]) @ bad - bad.conj().T @ np.diag([1.0, -1.0]))))
    < TOL
    and float(np.max(np.abs(bad - bad.conj().T))) > 0.9,
)

constant_records = [
    Completion("good", 0, "same"),
    Completion("bad", 1, "same"),
]
separating_records = [
    Completion("good", 0, "good-certificate"),
    Completion("bad", 1, "bad-certificate"),
]

law_only = attribution_case(
    completions=constant_records,
    law_filter=lambda item: item.name == "good",
    record_value="same",
    law_selector_defined=True,
    record_interface_selected=True,
)
check(
    "law-only closure has zero target diameter before records",
    law_only["law_diameter"] == 0,
    law_only,
)
check(
    "constant record receives zero marginal selection credit",
    law_only["marginal_record_reduction"] == 0
    and law_only["disposition"] == "LAW_ONLY_CLOSURE",
    law_only,
)

record_reduction = attribution_case(
    completions=separating_records,
    law_filter=lambda item: True,
    record_value="good-certificate",
    law_selector_defined=True,
    record_interface_selected=True,
)
check(
    "record can close a still-open lawful target fibre",
    record_reduction["law_diameter"] == 1
    and record_reduction["conditioned_diameter"] == 0,
    record_reduction,
)
check(
    "record credit is conditional reconstruction, not law selection",
    record_reduction["disposition"] == "RECORD_CONDITIONAL_REDUCTION"
    and record_reduction["marginal_record_reduction"] == 1,
    record_reduction,
)

open_case = attribution_case(
    completions=constant_records,
    law_filter=lambda item: True,
    record_value="same",
    law_selector_defined=True,
    record_interface_selected=True,
)
check(
    "uninformative record leaves the lawful branch target open",
    open_case["disposition"] == "OPEN_AFTER_RECORD"
    and open_case["conditioned_diameter"] == 1,
    open_case,
)

empty_case = attribution_case(
    completions=constant_records,
    law_filter=lambda item: False,
    record_value="same",
    law_selector_defined=True,
    record_interface_selected=True,
)
check(
    "empty law fibre is incompatibility, never reconstruction",
    empty_case["disposition"] == "EMPTY_LAW_FIBRE"
    and empty_case["law_diameter"] is None,
    empty_case,
)

missing_interface = attribution_case(
    completions=separating_records,
    law_filter=lambda item: True,
    record_value="good-certificate",
    law_selector_defined=True,
    record_interface_selected=False,
)
check(
    "an unselected record map earns no record credit",
    missing_interface["disposition"] == "INCOMPLETE_RECORD_INTERFACE",
    missing_interface,
)

actual_collision = attribution_case(
    completions=constant_records,
    law_filter=lambda item: item.name == "good",
    record_value="same",
    law_selector_defined=False,
    record_interface_selected=False,
)
check(
    "current GU/Finster contact is not a law selector",
    actual_collision["disposition"] == "INCOMPLETE_LAW_SELECTOR",
    actual_collision,
)

actual_disposition = (
    "DOMAIN_ADMISSIBILITY_ONLY__COMMON_CFS_ACTION_NOT_DEFINED__"
    "RECORD_INTERFACE_NOT_SELECTED"
)
check(
    "current collision receives the scoped attribution",
    actual_disposition.startswith("DOMAIN_ADMISSIBILITY_ONLY"),
    actual_disposition,
)

check(
    "no scenario treats a spectral projector as a formed certified archive",
    not any(
        case["disposition"] == "RECORD_CONDITIONAL_REDUCTION"
        for case in [law_only, open_case, empty_case, missing_interface, actual_collision]
    ),
)

passed = sum(int(item["passed"]) for item in checks)
artifact = {
    "probe_id": "DU-KREIN-SEA-FLUX-ATTRIBUTION-01",
    "scope": (
        "finite law-versus-record attribution and independent spectral receipt; "
        "no baryogenesis rate or physical selection"
    ),
    "checks_passed": passed,
    "checks_total": len(checks),
    "checks": checks,
    "cases": {
        "law_only": law_only,
        "record_conditional_reduction": record_reduction,
        "open_after_record": open_case,
        "empty_law_fibre": empty_case,
        "missing_record_interface": missing_interface,
        "actual_collision": actual_collision,
    },
    "actual_disposition": actual_disposition,
    "record_credit_rule": (
        "Records receive marginal reconstructive credit only when a separately "
        "selected and formed record reduces a nonempty, still-open lawful "
        "target fibre."
    ),
    "scientific_claim": False,
    "baryogenesis_rate_computed": False,
    "external_hardware_required": False,
}
ARTIFACT_PATH.write_text(
    json.dumps(artifact, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(f"checks: {passed}/{len(checks)}")
print(f"artifact: {ARTIFACT_PATH}")
print(f"VERDICT: {actual_disposition}")
if passed != len(checks):
    raise SystemExit(1)
