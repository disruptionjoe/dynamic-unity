#!/usr/bin/env python3
"""Exact positive and hostile controls for the GU theory-payload receiver."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GU_ROOT = ROOT.parent / "gu-formalization"
SCHEMA_PATH = ROOT / "lab/process/gu-du-theory-payload-v0.1.schema.json"
CURRENT_PATH = ROOT / "lab/process/gu-du-theory-payload-current.json"
GU_PASSPORT = GU_ROOT / "lab/specifications/theory-passport/gu-geometry-first-v0.1.yaml"
ARTIFACT_PATH = ROOT / "tests/artifacts/du_gu_theory_payload_receiver_result.json"

BURDENS = ["action_causal_closure", "physical_state_space", "observable_export"]
PAYLOAD_FIELDS = [
    "qualified_action_and_domain",
    "physical_state_space_certificate",
    "observable_process_map",
    "frozen_parameters_and_held_out_test",
    "truth_grade_and_live_null",
]
PROGRAMS = {
    "DU-FOUR-DIMENSIONAL-QFT-COMPLETION",
    "DU-INFRARED-EMPIRICAL-QUANTUM-GRAVITY",
}


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"{path}: root must be an object"
    return value


def schema_errors(record: dict) -> list[str]:
    schema = load(SCHEMA_PATH)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    if importlib.util.find_spec("jsonschema") is None:
        return []
    from jsonschema import Draft202012Validator
    Draft202012Validator.check_schema(schema)
    return [error.message for error in Draft202012Validator(schema).iter_errors(record)]


def ready_for_local_verification(record: dict) -> bool:
    return (
        record.get("source", {}).get("export_status") == "ready"
        and [row.get("id") for row in record.get("burdens", [])] == BURDENS
        and all(
            row.get("status") == "satisfied" and bool(row.get("evidence_refs"))
            for row in record.get("burdens", [])
        )
        and set(record.get("required_payload", {})) == set(PAYLOAD_FIELDS)
        and all(isinstance(record["required_payload"][name], dict) for name in PAYLOAD_FIELDS)
        and not record.get("missing_conditions")
    )


def violations(record: dict) -> list[str]:
    errors = schema_errors(record)
    source = record.get("source", {})
    if source.get("repository") != "gu-formalization" or len(source.get("revision", "")) != 40:
        errors.append("source provenance incomplete")
    if [row.get("id") for row in record.get("burdens", [])] != BURDENS:
        errors.append("burden order changed")
    destination = record.get("du_destination", {})
    if set(destination.get("program_ids", [])) != PROGRAMS:
        errors.append("destination program set changed")
    for effect in ("routing_effect", "wip_effect", "grade_effect"):
        if destination.get(effect) != "none":
            errors.append(f"forbidden DU {effect}")
    if record.get("receiver_decision") == "ADMIT_FOR_LOCAL_VERIFICATION" and not ready_for_local_verification(record):
        errors.append("premature source admission")
    if record.get("receiver_decision") == "REJECT_NOT_READY" and not record.get("missing_conditions"):
        errors.append("rejection lacks missing conditions")
    if len(record.get("scientific_nonclaims", [])) < 5:
        errors.append("scientific nonclaims incomplete")
    return errors


def synthetic_ready(current: dict) -> dict:
    ready = deepcopy(current)
    ready["source"]["export_status"] = "ready"
    ready["source"]["truth_grade"] = "scoped_source_evidence"
    ready["source"]["claim_effect"] = "qualified_payload_only"
    for burden in ready["burdens"]:
        burden["status"] = "satisfied"
        burden["evidence_refs"] = [f"gu-formalization#synthetic/{burden['id']}"]
    ready["required_payload"] = {
        name: {
            "claim_summary": f"synthetic positive control for {name}",
            "evidence_refs": [f"gu-formalization#synthetic/{name}"],
        }
        for name in PAYLOAD_FIELDS
    }
    ready["receiver_decision"] = "ADMIT_FOR_LOCAL_VERIFICATION"
    ready["missing_conditions"] = []
    return ready


def main() -> int:
    current = load(CURRENT_PATH)
    passport = load(GU_PASSPORT)
    assert not violations(current), violations(current)
    assert current["source"]["passport_id"] == passport["passport_id"]
    assert current["source"]["passport_schema_version"] == passport["schema_version"]
    assert current["source"]["export_status"] == passport["export_contract"]["status"]
    assert current["source"]["truth_grade"] == passport["truth_status"]["grade"]
    assert current["source"]["claim_effect"] == passport["truth_status"]["claim_effect"]
    assert [row["id"] for row in current["burdens"]] == [row["id"] for row in passport["critical_path"]]
    assert [row["status"] for row in current["burdens"]] == [row["status"] for row in passport["critical_path"]]
    assert not ready_for_local_verification(current)
    assert current["receiver_decision"] == "REJECT_NOT_READY"

    positive = synthetic_ready(current)
    assert not violations(positive), violations(positive)
    assert ready_for_local_verification(positive)

    mutations: list[dict] = []
    case = deepcopy(current); case["receiver_decision"] = "ADMIT_FOR_LOCAL_VERIFICATION"; mutations.append(case)
    case = deepcopy(current); case["du_destination"]["routing_effect"] = "activate"; mutations.append(case)
    case = deepcopy(current); case["du_destination"]["wip_effect"] = "scientific_flagship"; mutations.append(case)
    case = deepcopy(current); case["du_destination"]["grade_effect"] = "promote"; mutations.append(case)
    case = deepcopy(current); case["source"]["revision"] = ""; mutations.append(case)
    case = deepcopy(current); case["burdens"].reverse(); mutations.append(case)
    case = deepcopy(current); case["missing_conditions"] = []; mutations.append(case)
    case = deepcopy(current); case["scientific_nonclaims"] = []; mutations.append(case)
    case = deepcopy(positive); case["burdens"][1]["evidence_refs"] = []; mutations.append(case)
    case = deepcopy(positive); case["required_payload"]["truth_grade_and_live_null"] = None; mutations.append(case)
    case = deepcopy(positive); case["missing_conditions"] = ["hidden_gap"]; mutations.append(case)
    case = deepcopy(positive); case["du_destination"]["program_ids"][0] = "DU-Q0063-DECOHERENCE-NULL-AUDIT-LAYER-CONFRONTATION"; mutations.append(case)

    for index, mutation in enumerate(mutations, 1):
        assert violations(mutation), f"hostile mutation {index} escaped"

    result = {
        "status": "PASS",
        "current_receiver_decision": "REJECT_NOT_READY",
        "current_gu_ready_for_local_verification": False,
        "synthetic_ready_positive_control": True,
        "hostile_mutations_rejected": len(mutations),
        "du_effects": {"routing": "none", "wip": "none", "grade": "none"},
        "scientific_nonclaim": "Receiver validation establishes interface behavior only, not GU or Dynamic Unity physics."
    }
    assert load(ARTIFACT_PATH) == result
    print(f"PASS GU→DU receiver: current rejected; synthetic ready accepted; {len(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
