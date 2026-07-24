"""Shared contract and artifact helpers for conditional and abductive DU probes.

This module is deliberately a comparison instrument, not a scientific gate.  It
checks that a candidate exposes the assumptions and discriminators needed to
interpret a result.  It does not rank warrant types or infer that a numerically
passing probe is physically true.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = "du-conditional-candidate-v1"

# These are different epistemic relations, not an ordinal ladder.
WARRANT_TYPES = {
    "DERIVED",
    "CONDITIONALLY_ENTAILED",
    "CONSTRUCTIVELY_REALIZED",
    "ABDUCTIVELY_PREFERRED",
    "STRUCTURAL_ANALOGY",
}

ASSUMPTION_STATUSES = {
    "STANDARD",
    "PROJECT_NATIVE",
    "CONDITIONAL_POSIT",
    "IMPORTED",
}

ADMISSION_STATES = {
    "EXPLORATION",
    "CONDITIONAL_CANDIDATE",
    "FORMALIZATION_FALSIFIED",
    "CONCEPT_SUPPORTED",
    "CONCEPT_OPEN",
    "CONCEPT_FALSIFIED",
    "BANK_REVIEW_ONLY",
}

_ID_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9_.-]*$")


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _require_text(
    obj: Mapping[str, Any], key: str, path: str, errors: list[str]
) -> None:
    if not _nonempty_text(obj.get(key)):
        errors.append(f"{path}.{key}: required non-empty text")


def _require_nonempty_list(
    obj: Mapping[str, Any], key: str, path: str, errors: list[str]
) -> list[Any]:
    value = obj.get(key)
    if not isinstance(value, list) or not value:
        errors.append(f"{path}.{key}: required non-empty list")
        return []
    return value


def validate_candidate_contract(candidate: Mapping[str, Any]) -> list[str]:
    """Return contract-shape errors; an empty list means contract-complete.

    Completeness means the candidate is legible and comparable.  It is not a
    scientific endorsement and must never be reported as one.
    """

    errors: list[str] = []
    if candidate.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version: expected {SCHEMA_VERSION!r}, "
            f"got {candidate.get('schema_version')!r}"
        )

    for key in ("candidate_id", "track", "question"):
        _require_text(candidate, key, "candidate", errors)

    candidate_id = candidate.get("candidate_id")
    if _nonempty_text(candidate_id) and not _ID_PATTERN.fullmatch(candidate_id):
        errors.append(
            "candidate.candidate_id: use uppercase letters, digits, '.', '_' or '-'"
        )

    warrants = _require_nonempty_list(candidate, "warrants", "candidate", errors)
    unknown_warrants = sorted(
        {warrant for warrant in warrants if warrant not in WARRANT_TYPES}
    )
    if unknown_warrants:
        errors.append(f"candidate.warrants: unknown values {unknown_warrants}")

    assumptions = _require_nonempty_list(
        candidate, "assumptions", "candidate", errors
    )
    for index, assumption in enumerate(assumptions):
        path = f"candidate.assumptions[{index}]"
        if not isinstance(assumption, Mapping):
            errors.append(f"{path}: expected object")
            continue
        for key in ("id", "statement", "status", "role"):
            _require_text(assumption, key, path, errors)
        if (
            _nonempty_text(assumption.get("status"))
            and assumption["status"] not in ASSUMPTION_STATUSES
        ):
            errors.append(
                f"{path}.status: unknown value {assumption['status']!r}"
            )

    free_choices = _require_nonempty_list(
        candidate, "free_choices", "candidate", errors
    )
    for index, choice in enumerate(free_choices):
        path = f"candidate.free_choices[{index}]"
        if not isinstance(choice, Mapping):
            errors.append(f"{path}: expected object")
            continue
        for key in ("id", "choice", "why_not_forced", "sensitivity_test"):
            _require_text(choice, key, path, errors)

    for section in (
        "equations",
        "observables",
        "comparators",
        "null_models",
        "falsifiers",
        "stop_conditions",
    ):
        entries = _require_nonempty_list(candidate, section, "candidate", errors)
        for index, entry in enumerate(entries):
            if not _nonempty_text(entry):
                errors.append(
                    f"candidate.{section}[{index}]: required non-empty text"
                )

    concept = candidate.get("concept")
    if concept is not None:
        if not isinstance(concept, Mapping):
            errors.append("candidate.concept: expected object when supplied")
        else:
            for key in (
                "concept_id",
                "invariant",
                "formalization_id",
                "failure_scope",
            ):
                _require_text(concept, key, "candidate.concept", errors)
            failure_scope = concept.get("failure_scope")
            if (
                _nonempty_text(failure_scope)
                and failure_scope not in {"FORMALIZATION", "CONCEPT"}
            ):
                errors.append(
                    "candidate.concept.failure_scope: expected FORMALIZATION or CONCEPT"
                )

    result = candidate.get("result")
    if not isinstance(result, Mapping):
        errors.append("candidate.result: required object")
    else:
        for key in ("claim", "grade", "admission", "remaining_uncertainty"):
            _require_text(result, key, "candidate.result", errors)
        admission = result.get("admission")
        if _nonempty_text(admission) and admission not in ADMISSION_STATES:
            errors.append(
                f"candidate.result.admission: unknown value {admission!r}"
            )
        checks = result.get("checks")
        if not isinstance(checks, list) or not checks:
            errors.append("candidate.result.checks: required non-empty list")
        else:
            for index, check in enumerate(checks):
                path = f"candidate.result.checks[{index}]"
                if not isinstance(check, Mapping):
                    errors.append(f"{path}: expected object")
                    continue
                _require_text(check, "name", path, errors)
                if not isinstance(check.get("pass"), bool):
                    errors.append(f"{path}.pass: required boolean")

    return errors


def comparison_receipt(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return a small, deterministic comparison summary for a result artifact."""

    errors = validate_candidate_contract(candidate)
    result = candidate.get("result", {})
    checks: Sequence[Mapping[str, Any]] = (
        result.get("checks", []) if isinstance(result, Mapping) else []
    )
    return {
        "instrument": SCHEMA_VERSION,
        "contract_status": "COMPLETE" if not errors else "INCOMPLETE",
        "contract_errors": errors,
        "candidate_id": candidate.get("candidate_id"),
        "warrants": candidate.get("warrants", []),
        "assumption_count": len(candidate.get("assumptions", [])),
        "free_choice_count": len(candidate.get("free_choices", [])),
        "observable_count": len(candidate.get("observables", [])),
        "null_model_count": len(candidate.get("null_models", [])),
        "falsifier_count": len(candidate.get("falsifiers", [])),
        "checks_passed": sum(bool(check.get("pass")) for check in checks),
        "checks_total": len(checks),
        "admission": result.get("admission") if isinstance(result, Mapping) else None,
        "scientific_endorsement": False,
        "note": (
            "Contract completeness means legible and comparable, not physically true. "
            "Warrant types are non-ordinal; computation or formal argument disposes."
        ),
    }


def write_candidate_artifact(
    path: Path, candidate: Mapping[str, Any], payload: Mapping[str, Any]
) -> None:
    """Validate and write a deterministic JSON result artifact."""

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        joined = "\n".join(receipt["contract_errors"])
        raise ValueError(f"candidate contract incomplete:\n{joined}")

    artifact = {
        "candidate_contract": dict(candidate),
        "comparison_receipt": receipt,
        "results": dict(payload),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
