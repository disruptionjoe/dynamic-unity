#!/usr/bin/env python3
"""Implementation-complete physical-sufficiency acquisition gate.

The probe has two jobs:

1. refuse aggregate, unjoined, or incompletely reset evidence packets before
   they reach the Certified Causal Reconstruction trichotomy; and
2. exercise a conservative finite-shot binary-response specialization on
   deterministic synthetic controls.

Synthetic controls validate the contract and classifier only. They are never
reported as physical evidence. A physical result requires a packet whose
``evidence_kind`` is ``physical_shot_packet`` and whose complete source,
calibration, route, invalid-attempt, multi-time, and reset joins pass first.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import random
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = (
    ROOT
    / "specs"
    / "physical-sufficiency-acquisition-packet-v0.1.schema.json"
)
AGGREGATE_FIXTURE = (
    ROOT
    / "tests"
    / "fixtures"
    / "physical-sufficiency-acquisition"
    / "xiang-aggregate-only-control.json"
)
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_physical_sufficiency_acquisition_gate_result.json"
)
RUN_ID = "RUN-20260726-010042-physical-sufficiency-acquisition-gate"

TOP_REQUIRED = {
    "schema_version",
    "packet_id",
    "evidence_kind",
    "source",
    "freeze",
    "contract",
    "process_schema",
    "attempt_count",
    "trial_rows",
    "calibration_rows",
    "multitime_rows",
    "reset_receipts",
    "route_rows",
}

SOURCE_REQUIRED = {
    "title",
    "primary_uri",
    "repository_commit",
    "hardware_id",
    "protocol_id",
    "acquisition_started_at",
    "acquisition_ended_at",
    "packet_created_at",
    "raw_attachment_manifest",
}

ATTACHMENT_REQUIRED = {
    "path",
    "sha256",
    "media_type",
}

FREEZE_REQUIRED = {
    "contract_frozen_at",
    "record_selection_warrant",
    "completion_selection_warrant",
    "analysis_code_version",
    "holdout_policy",
    "blinded_fields",
}

CONTRACT_REQUIRED = {
    "observer_id",
    "access_boundary",
    "outcome_alphabet",
    "intervention_ids",
    "candidate_record_field",
    "target_response",
    "metric",
    "equivalence_tolerance",
    "familywise_alpha",
    "completion_class",
    "memory_registers",
    "minimum_heldout_shots_per_cell",
}

PROCESS_REQUIRED = {
    "selective_map_convention",
    "outcome_normalization",
    "physicality_projection",
    "tomography_scope",
    "row_to_map_rule_id",
    "row_to_map_rule_sha256",
    "raw_to_probability_rule",
}

COMPLETION_REQUIRED = {
    "completion_id",
    "refinement_field",
    "formation_warrant",
    "target_independent",
    "resources",
}

MEMORY_REQUIRED = {
    "memory_id",
    "kind",
    "boundary_status",
    "reset_required_for_remainder",
}

TRIAL_REQUIRED = {
    "attempt_index",
    "trial_id",
    "history_id",
    "sequence_id",
    "repeat_index",
    "trial_order",
    "timestamp",
    "preparation_id",
    "intervention_id",
    "candidate_record_id",
    "refinement_labels",
    "selective_outcome",
    "output_setting_id",
    "output_result",
    "valid",
    "rejection_reason",
    "calibration_block_id",
    "controller_version",
    "decoder_version",
    "route_id",
    "provenance_sha256",
    "analysis_role",
    "causal_break_id",
}

CALIBRATION_REQUIRED = {
    "calibration_block_id",
    "valid_from",
    "valid_to",
    "controller_version",
    "decoder_version",
    "preparation_model_id",
    "readout_model_id",
    "prepared_0_observed_1",
    "prepared_1_observed_0",
    "joint_uncertainty_method",
    "joint_spam_drift_tv_bound",
    "joint_spam_drift_bound_warrant",
    "raw_attachment_sha256",
    "preparation_calibration_sha256",
    "joint_uncertainty_attachment_sha256",
}

MULTITIME_REQUIRED = {
    "trial_id",
    "event_index",
    "event_id",
    "intervention_id",
    "instrument_outcome",
    "prior_record_id",
    "causal_break_applied",
    "held_out_continuation",
    "reset_receipt_ids",
}

RESET_REQUIRED = {
    "reset_receipt_id",
    "trial_id",
    "reset_protocol_id",
    "memory_register_ids",
    "success",
    "verification_method",
    "verification_result",
    "timestamp",
}

ROUTE_REQUIRED = {
    "route_id",
    "source",
    "reference",
    "processor",
    "pointer",
    "archive",
    "detector",
    "environment",
    "controller",
    "decoder",
    "ordered_ports",
    "resources",
}

PUBLIC_SIDECAR_AUDIT = {
    "source": "https://github.com/guochu/pt_recovery",
    "commit": "47d67598a304bb72c315bf05ddfadcda5f4be290",
    "recursive_tree_file_count": 1128,
    "representative_directory": (
        "experiment_data/RB_data_20230104/len40/idle100/rb_data_0.1"
    ),
    "inspected_blobs": {
        "README.md": "08acfaae30ca332a60f5b6fdc1b1cb1262482546",
        "split_rb_data.jl": "63875ce93997ce23fc7dc334e8754df2d994c5c3",
        "data_process.ipynb": "a65156052d5f9380eab7c279338da5d0fccd4c4a",
        "rb_data_0.1.npy": "0d6a8c2742a7d6cf5d13bdca68235d5a0d013126",
        "standard_rb_1q_full_data.json": "8ef973b3197f062326b75c9cc55b20647c8f3615",
        "Q67_flux_sq_rb_script.py": "e0f650f0e01d4cdf3fdaa3170efb709dba4a2304",
    },
    "representative_findings": {
        "standard_rb_1q_full_data.json": {
            "rows": 7800,
            "keys": ["cl_ops", "p0"],
        },
        "rb_data_0.1.npy": {
            "arrays": 200,
            "shape_each": [39],
            "dtype": "float64",
            "meaning": "one already calibrated p0 value per RB sequence",
        },
        "data_process.ipynb": (
            "joins schedule-generated Clifford sequences to the 200x39 p0 "
            "array and writes only cl_ops plus p0"
        ),
        "Q67_flux_sq_rb_script.py": (
            "forms complex acquisition averages, uses the last two values as "
            "cal0/cal1, rotates to a calibrated axis, discards those two "
            "calibration values, and saves p0 arrays"
        ),
        "article_protocol_note": (
            "the article states 1024 measurement outcomes per reported f, "
            "while the representative acquisition script configures 2048 "
            "repetitions; no row-level run-version join resolves the scope"
        ),
    },
    "filename_sidecar_keyword_hits": 0,
    "verdict": "NO_JOINED_SHOT_LEVEL_SIDECAR",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(contains_key(item, key) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False


class Receipt:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(self, name: str, condition: bool, detail: str) -> None:
        self.checks.append(
            {"name": name, "passed": bool(condition), "detail": detail}
        )

    def close(self) -> dict[str, Any]:
        passed = sum(item["passed"] for item in self.checks)
        return {
            "all_passed": passed == len(self.checks),
            "passed": passed,
            "total": len(self.checks),
            "checks": self.checks,
        }


class Errors:
    def __init__(self) -> None:
        self.items: dict[str, str] = {}

    def add(self, code: str, detail: str) -> None:
        self.items.setdefault(code, detail)

    def finish(self) -> list[dict[str, str]]:
        return [
            {"code": code, "detail": self.items[code]}
            for code in sorted(self.items)
        ]


def require_exact_fields(
    errors: Errors,
    label: str,
    value: dict[str, Any],
    required: set[str],
) -> None:
    missing = required - set(value)
    unknown = set(value) - required
    if missing:
        errors.add(f"{label}_FIELDS_MISSING", str(sorted(missing)))
    if unknown:
        errors.add(f"{label}_FIELDS_UNKNOWN", str(sorted(unknown)))


def validate_packet(packet: Any) -> list[dict[str, str]]:
    """Validate semantic joins that JSON Schema alone cannot express."""

    errors = Errors()
    if not isinstance(packet, dict):
        return [{"code": "PACKET_NOT_OBJECT", "detail": "packet must be an object"}]

    missing_top = TOP_REQUIRED - set(packet)
    for key in sorted(missing_top):
        errors.add(f"MISSING_{key.upper()}", f"missing top-level field {key}")
    if contains_key(packet, "p0") and "trial_rows" not in packet:
        errors.add(
            "AGGREGATE_PROBABILITY_FORBIDDEN",
            "an aggregate p0 cannot be expanded into shot rows",
        )
    if missing_top:
        return errors.finish()

    if packet["schema_version"] != "du-physical-sufficiency-packet/0.1":
        errors.add("SCHEMA_VERSION_UNSUPPORTED", str(packet["schema_version"]))
    if packet["evidence_kind"] not in {
        "physical_shot_packet",
        "synthetic_contract_control",
    }:
        errors.add("EVIDENCE_KIND_INVALID", str(packet["evidence_kind"]))

    source = packet["source"]
    freeze = packet["freeze"]
    contract = packet["contract"]
    process_schema = packet["process_schema"]
    trials = packet["trial_rows"]
    calibrations = packet["calibration_rows"]
    multitime = packet["multitime_rows"]
    resets = packet["reset_receipts"]
    routes = packet["route_rows"]

    for name, value in [
        ("source", source),
        ("freeze", freeze),
        ("contract", contract),
        ("process_schema", process_schema),
    ]:
        if not isinstance(value, dict):
            errors.add(f"{name.upper()}_NOT_OBJECT", f"{name} must be an object")
    for name, value in [
        ("trial_rows", trials),
        ("calibration_rows", calibrations),
        ("multitime_rows", multitime),
        ("reset_receipts", resets),
        ("route_rows", routes),
    ]:
        if not isinstance(value, list) or not value:
            errors.add(f"{name.upper()}_EMPTY", f"{name} must be a nonempty list")
    if errors.items:
        return errors.finish()

    require_exact_fields(errors, "SOURCE", source, SOURCE_REQUIRED)
    require_exact_fields(errors, "FREEZE", freeze, FREEZE_REQUIRED)
    require_exact_fields(errors, "CONTRACT", contract, CONTRACT_REQUIRED)
    require_exact_fields(errors, "PROCESS", process_schema, PROCESS_REQUIRED)
    attachments_shape = source.get("raw_attachment_manifest", [])
    if not isinstance(attachments_shape, list) or not attachments_shape:
        errors.add(
            "RAW_ATTACHMENT_MANIFEST_EMPTY",
            "raw_attachment_manifest must be a nonempty list",
        )
        attachments_shape = []
    for index, row in enumerate(attachments_shape):
        if not isinstance(row, dict):
            errors.add("ATTACHMENT_ROW_NOT_OBJECT", f"attachment row {index}")
        else:
            require_exact_fields(errors, "ATTACHMENT", row, ATTACHMENT_REQUIRED)
    for index, row in enumerate(trials):
        if not isinstance(row, dict):
            errors.add("TRIAL_ROW_NOT_OBJECT", f"trial row {index}")
        else:
            require_exact_fields(errors, "TRIAL", row, TRIAL_REQUIRED)
    for index, row in enumerate(calibrations):
        if not isinstance(row, dict):
            errors.add("CALIBRATION_ROW_NOT_OBJECT", f"calibration row {index}")
        else:
            require_exact_fields(errors, "CALIBRATION", row, CALIBRATION_REQUIRED)
    for index, row in enumerate(multitime):
        if not isinstance(row, dict):
            errors.add("MULTITIME_ROW_NOT_OBJECT", f"multitime row {index}")
        else:
            require_exact_fields(errors, "MULTITIME", row, MULTITIME_REQUIRED)
    for index, row in enumerate(resets):
        if not isinstance(row, dict):
            errors.add("RESET_ROW_NOT_OBJECT", f"reset row {index}")
        else:
            require_exact_fields(errors, "RESET", row, RESET_REQUIRED)
    for index, row in enumerate(routes):
        if not isinstance(row, dict):
            errors.add("ROUTE_ROW_NOT_OBJECT", f"route row {index}")
        else:
            require_exact_fields(errors, "ROUTE", row, ROUTE_REQUIRED)
    completion_shape = contract.get("completion_class")
    memory_shape = contract.get("memory_registers")
    if not isinstance(completion_shape, list) or not completion_shape:
        errors.add(
            "COMPLETION_CLASS_EMPTY",
            "completion_class must be a nonempty list",
        )
        completion_shape = []
    if not isinstance(memory_shape, list) or not memory_shape:
        errors.add(
            "MEMORY_REGISTER_CLASS_EMPTY",
            "memory_registers must be a nonempty list",
        )
        memory_shape = []
    for index, row in enumerate(completion_shape):
        if not isinstance(row, dict):
            errors.add("COMPLETION_ROW_NOT_OBJECT", f"completion row {index}")
        else:
            require_exact_fields(errors, "COMPLETION", row, COMPLETION_REQUIRED)
    for index, row in enumerate(memory_shape):
        if not isinstance(row, dict):
            errors.add("MEMORY_ROW_NOT_OBJECT", f"memory row {index}")
        else:
            require_exact_fields(errors, "MEMORY", row, MEMORY_REQUIRED)
    if errors.items:
        return errors.finish()

    try:
        frozen_at = parse_time(freeze["contract_frozen_at"])
        acquired_at = parse_time(source["acquisition_started_at"])
        ended_at = parse_time(source["acquisition_ended_at"])
        created_at = parse_time(source["packet_created_at"])
        if not frozen_at < acquired_at <= ended_at <= created_at:
            errors.add(
                "FREEZE_ORDER_INVALID",
                "contract freeze must precede acquisition and packet creation",
            )
    except (KeyError, TypeError, ValueError) as exc:
        errors.add("FREEZE_TIMESTAMP_INVALID", str(exc))

    attachments = source.get("raw_attachment_manifest", [])
    attachment_paths = [
        row["path"] for row in attachments if isinstance(row.get("path"), str)
    ]
    attachment_hashes = {
        row.get("sha256")
        for row in attachments
        if isinstance(row, dict) and isinstance(row.get("sha256"), str)
    }
    if not attachment_hashes:
        errors.add("RAW_ATTACHMENT_MANIFEST_EMPTY", "no immutable raw attachments")
    if len(attachment_paths) != len(set(attachment_paths)):
        errors.add("ATTACHMENT_PATH_DUPLICATE", "attachment paths must be unique")
    for row in attachments:
        digest = row["sha256"]
        if (
            len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
            or not row["path"]
            or not row["media_type"]
        ):
            errors.add("ATTACHMENT_IDENTITY_INVALID", str(row))

    interventions_value = contract["intervention_ids"]
    if (
        not isinstance(interventions_value, list)
        or not interventions_value
        or any(not isinstance(value, str) or not value for value in interventions_value)
        or len(interventions_value) != len(set(interventions_value))
    ):
        errors.add(
            "INTERVENTION_FAMILY_INVALID",
            "intervention_ids must be unique nonempty strings",
        )
        interventions_value = []
    epsilon = contract["equivalence_tolerance"]
    alpha = contract["familywise_alpha"]
    minimum_shots = contract["minimum_heldout_shots_per_cell"]
    if (
        isinstance(epsilon, bool)
        or not isinstance(epsilon, (int, float))
        or not 0.0 <= epsilon < 1.0
    ):
        errors.add("EQUIVALENCE_TOLERANCE_INVALID", str(epsilon))
    if (
        isinstance(alpha, bool)
        or not isinstance(alpha, (int, float))
        or not 0.0 < alpha < 1.0
    ):
        errors.add("FAMILYWISE_ALPHA_INVALID", str(alpha))
    if type(minimum_shots) is not int or minimum_shots < 1:
        errors.add("MINIMUM_SHOTS_INVALID", str(minimum_shots))
        minimum_shots = 1
    if (
        contract["outcome_alphabet"] != [0, 1]
        or contract["candidate_record_field"] != "candidate_record_id"
        or contract["target_response"]
        != "P(output_result=1 | history_id, intervention_id)"
        or contract["metric"] != "binary_total_variation"
    ):
        errors.add(
            "RESPONSE_CONTRACT_INVALID",
            "binary response contract constants do not match v0.1",
        )

    if type(packet["attempt_count"]) is not int or packet["attempt_count"] < 1:
        errors.add("ATTEMPT_COUNT_INVALID", str(packet["attempt_count"]))
    elif packet["attempt_count"] != len(trials):
        errors.add(
            "ATTEMPT_LEDGER_INCOMPLETE",
            f"attempt_count={packet['attempt_count']}; rows={len(trials)}",
        )

    trial_ids: list[str] = []
    attempt_indices: list[int] = []
    trial_orders: list[int] = []
    interventions = set(interventions_value)
    completions = contract.get("completion_class", [])
    completion_fields = {
        row.get("completion_id"): row.get("refinement_field")
        for row in completions
        if isinstance(row, dict)
    }
    completion_ids = [row["completion_id"] for row in completions]
    if len(completion_ids) != len(set(completion_ids)):
        errors.add("COMPLETION_ID_DUPLICATE", "completion_id must be unique")
    for row in completions:
        resources = row["resources"]
        if (
            not row["completion_id"]
            or not row["refinement_field"]
            or not row["formation_warrant"]
            or row["target_independent"] is not True
            or not isinstance(resources, dict)
            or not resources
            or any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or value < 0
                for value in resources.values()
            )
        ):
            errors.add("COMPLETION_CONTRACT_INVALID", str(row["completion_id"]))

    memories = contract["memory_registers"]
    memory_ids = [row["memory_id"] for row in memories]
    if len(memory_ids) != len(set(memory_ids)):
        errors.add("MEMORY_ID_DUPLICATE", "memory_id must be unique")
    for row in memories:
        if (
            not row["memory_id"]
            or row["kind"]
            not in {
                "quantum",
                "classical",
                "controller",
                "decoder",
                "environment",
                "archive",
                "route",
            }
            or row["boundary_status"]
            not in {
                "inside_candidate_record",
                "inside_admissible_completion",
                "outside_observer_access_but_physically_retained",
            }
            or type(row["reset_required_for_remainder"]) is not bool
        ):
            errors.add("MEMORY_CONTRACT_INVALID", str(row["memory_id"]))

    for index, row in enumerate(trials):
        if not isinstance(row, dict):
            errors.add("TRIAL_ROW_NOT_OBJECT", f"trial row {index}")
            continue
        missing = TRIAL_REQUIRED - set(row)
        if missing:
            errors.add(
                "TRIAL_FIELDS_MISSING",
                f"trial row {index}: {sorted(missing)}",
            )
            continue
        unknown = set(row) - TRIAL_REQUIRED
        if unknown:
            errors.add(
                "TRIAL_FIELDS_UNKNOWN",
                f"trial row {index}: {sorted(unknown)}",
            )
        if not isinstance(row["trial_id"], str) or not row["trial_id"]:
            errors.add("TRIAL_ID_INVALID", f"trial row {index}")
        else:
            trial_ids.append(row["trial_id"])
        if type(row["attempt_index"]) is not int or row["attempt_index"] < 1:
            errors.add("ATTEMPT_INDEX_INVALID", f"trial row {index}")
        else:
            attempt_indices.append(row["attempt_index"])
        if type(row["trial_order"]) is not int or row["trial_order"] < 1:
            errors.add("TRIAL_ORDER_INVALID", f"trial row {index}")
        else:
            trial_orders.append(row["trial_order"])
        if type(row["valid"]) is not bool:
            errors.add("TRIAL_VALIDITY_INVALID", str(row["trial_id"]))
        if row["analysis_role"] not in {"training", "held_out", "causal_break"}:
            errors.add("ANALYSIS_ROLE_INVALID", str(row["trial_id"]))
        if row["intervention_id"] not in interventions:
            errors.add(
                "INTERVENTION_OUTSIDE_FROZEN_FAMILY",
                str(row["intervention_id"]),
            )
        if row["valid"]:
            if type(row["output_result"]) is not int or row["output_result"] not in {
                0,
                1,
            }:
                errors.add(
                    "SHOT_RESULT_NOT_BINARY",
                    f"trial {row['trial_id']} has {row['output_result']!r}",
                )
            if row["rejection_reason"] is not None:
                errors.add(
                    "VALID_TRIAL_HAS_REJECTION_REASON",
                    str(row["trial_id"]),
                )
        else:
            if row["output_result"] is not None or not row["rejection_reason"]:
                errors.add(
                    "INVALID_TRIAL_SEMANTICS_BROKEN",
                    str(row["trial_id"]),
                )
        if row["provenance_sha256"] not in attachment_hashes:
            errors.add(
                "TRIAL_PROVENANCE_ATTACHMENT_MISSING",
                str(row["trial_id"]),
            )
        labels = row["refinement_labels"]
        if not isinstance(labels, dict):
            errors.add("REFINEMENT_LABELS_INVALID", str(row["trial_id"]))
        else:
            for completion_id, field in completion_fields.items():
                if (
                    not field
                    or field not in labels
                    or not isinstance(labels[field], str)
                    or not labels[field]
                ):
                    errors.add(
                        "REFINEMENT_LABEL_MISSING",
                        f"trial={row['trial_id']}; completion={completion_id}",
                    )

    if errors.items:
        return errors.finish()

    if len(trial_ids) != len(set(trial_ids)):
        errors.add("TRIAL_ID_DUPLICATE", "trial_id must be unique")
    expected_attempts = list(range(1, len(trials) + 1))
    if sorted(attempt_indices) != expected_attempts:
        errors.add("ATTEMPT_INDEX_GAP", "attempt indices must cover 1..attempt_count")
    if sorted(trial_orders) != expected_attempts:
        errors.add("TRIAL_ORDER_GAP", "trial order must cover 1..attempt_count")

    calibration_by_id: dict[str, dict[str, Any]] = {}
    calibration_ids: list[str] = []
    for index, row in enumerate(calibrations):
        if not isinstance(row, dict):
            errors.add("CALIBRATION_ROW_NOT_OBJECT", f"calibration row {index}")
            continue
        missing = CALIBRATION_REQUIRED - set(row)
        if missing:
            errors.add(
                "CALIBRATION_FIELDS_MISSING",
                f"calibration row {index}: {sorted(missing)}",
            )
            continue
        calibration_ids.append(row["calibration_block_id"])
        calibration_by_id[row["calibration_block_id"]] = row
        for count_field in [
            "prepared_0_observed_1",
            "prepared_1_observed_0",
        ]:
            counts = row[count_field]
            if (
                not isinstance(counts, dict)
                or type(counts.get("shots")) is not int
                or type(counts.get("errors")) is not int
                or counts["shots"] < 1
                or not 0 <= counts["errors"] <= counts["shots"]
            ):
                errors.add(
                    "CALIBRATION_COUNTS_INVALID",
                    f"{row['calibration_block_id']}:{count_field}",
                )
        if row["joint_uncertainty_method"] != (
            "simultaneous_hoeffding_bonferroni_from_raw_counts"
        ):
            errors.add(
                "UNCERTAINTY_METHOD_UNFROZEN",
                str(row["calibration_block_id"]),
            )
        systematic = row["joint_spam_drift_tv_bound"]
        if (
            isinstance(systematic, bool)
            or not isinstance(systematic, (int, float))
            or not 0.0 <= systematic < 1.0
            or not row["joint_spam_drift_bound_warrant"]
        ):
            errors.add(
                "JOINT_SYSTEMATIC_BOUND_INVALID",
                str(row["calibration_block_id"]),
            )
        for field in [
            "raw_attachment_sha256",
            "preparation_calibration_sha256",
            "joint_uncertainty_attachment_sha256",
        ]:
            if row[field] not in attachment_hashes:
                errors.add(
                    "CALIBRATION_ATTACHMENT_MISSING",
                    f"{row['calibration_block_id']}:{field}",
                )
    if len(calibration_ids) != len(set(calibration_ids)):
        errors.add(
            "CALIBRATION_ID_DUPLICATE",
            "calibration_block_id must be unique",
        )

    route_ids = [row["route_id"] for row in routes]
    if len(route_ids) != len(set(route_ids)):
        errors.add("ROUTE_ID_DUPLICATE", "route_id must be unique")
    route_by_id = {row["route_id"]: row for row in routes}
    trial_by_id = {
        row.get("trial_id"): row for row in trials if isinstance(row, dict)
    }

    history_records: dict[str, set[str]] = {}
    history_refinements: dict[tuple[str, str], set[str]] = {}
    heldout_counts: dict[tuple[str, str], int] = {}
    for row in trials:
        if not isinstance(row, dict) or not TRIAL_REQUIRED <= set(row):
            continue
        calibration = calibration_by_id.get(row["calibration_block_id"])
        if calibration is None:
            errors.add(
                "CALIBRATION_JOIN_MISSING",
                f"trial={row['trial_id']}; block={row['calibration_block_id']}",
            )
        else:
            if (
                row["controller_version"] != calibration["controller_version"]
                or row["decoder_version"] != calibration["decoder_version"]
            ):
                errors.add(
                    "CALIBRATION_VERSION_MISMATCH",
                    str(row["trial_id"]),
                )
            try:
                timestamp = parse_time(row["timestamp"])
                if not (
                    parse_time(calibration["valid_from"])
                    <= timestamp
                    <= parse_time(calibration["valid_to"])
                ):
                    errors.add(
                        "CALIBRATION_TIME_JOIN_INVALID",
                        str(row["trial_id"]),
                    )
            except (TypeError, ValueError) as exc:
                errors.add("TRIAL_TIMESTAMP_INVALID", str(exc))
        if row["route_id"] not in route_by_id:
            errors.add("ROUTE_JOIN_MISSING", str(row["trial_id"]))
        history_records.setdefault(row["history_id"], set()).add(
            row["candidate_record_id"]
        )
        for completion_id, field in completion_fields.items():
            if field in row["refinement_labels"]:
                history_refinements.setdefault(
                    (row["history_id"], completion_id), set()
                ).add(row["refinement_labels"][field])
        if row["valid"] and row["analysis_role"] == "held_out":
            key = (row["history_id"], row["intervention_id"])
            heldout_counts[key] = heldout_counts.get(key, 0) + 1

    if any(len(labels) != 1 for labels in history_records.values()):
        errors.add(
            "CANDIDATE_RECORD_CHANGES_WITHIN_HISTORY",
            "candidate record must be stable within history",
        )
    if any(len(labels) != 1 for labels in history_refinements.values()):
        errors.add(
            "REFINEMENT_LABEL_CHANGES_WITHIN_HISTORY",
            "completion labels must be stable within history",
        )

    record_to_histories: dict[str, set[str]] = {}
    for history, labels in history_records.items():
        if len(labels) == 1:
            record_to_histories.setdefault(next(iter(labels)), set()).add(history)
    if not any(len(histories) >= 2 for histories in record_to_histories.values()):
        errors.add(
            "BASE_RECORD_HAS_NO_NONTRIVIAL_COLLISION",
            "at least two histories must share one candidate record",
        )

    minimum_shots = contract.get("minimum_heldout_shots_per_cell", 0)
    histories = set(history_records)
    for history in histories:
        for intervention in interventions:
            observed = heldout_counts.get((history, intervention), 0)
            if observed < minimum_shots:
                errors.add(
                    "HELDOUT_CELL_UNDERSAMPLED",
                    (
                        f"history={history}; intervention={intervention}; "
                        f"n={observed}; minimum={minimum_shots}"
                    ),
                )

    multitime_by_trial: dict[str, list[dict[str, Any]]] = {}
    reset_id_list = [row["reset_receipt_id"] for row in resets]
    reset_ids = set(reset_id_list)
    if len(reset_id_list) != len(reset_ids):
        errors.add(
            "RESET_RECEIPT_ID_DUPLICATE",
            "reset_receipt_id must be unique",
        )
    event_ids: list[str] = []
    for index, row in enumerate(multitime):
        if not isinstance(row, dict):
            errors.add("MULTITIME_ROW_NOT_OBJECT", f"multitime row {index}")
            continue
        missing = MULTITIME_REQUIRED - set(row)
        if missing:
            errors.add(
                "MULTITIME_FIELDS_MISSING",
                f"multitime row {index}: {sorted(missing)}",
            )
            continue
        if row["trial_id"] not in trial_by_id:
            errors.add("MULTITIME_TRIAL_JOIN_MISSING", str(row["trial_id"]))
        if any(receipt_id not in reset_ids for receipt_id in row["reset_receipt_ids"]):
            errors.add("MULTITIME_RESET_JOIN_MISSING", str(row["trial_id"]))
        event_ids.append(row["event_id"])
        multitime_by_trial.setdefault(row["trial_id"], []).append(row)
    if len(event_ids) != len(set(event_ids)):
        errors.add("EVENT_ID_DUPLICATE", "event_id must be unique")

    for row in trials:
        if isinstance(row, dict) and row.get("valid"):
            if row["trial_id"] not in multitime_by_trial:
                errors.add("MULTITIME_EVENT_MISSING", str(row["trial_id"]))

    required_memory = {
        row["memory_id"]
        for row in contract.get("memory_registers", [])
        if row.get("reset_required_for_remainder")
    }
    successful_reset_by_trial: dict[str, set[str]] = {}
    for row in resets:
        if not isinstance(row, dict):
            continue
        if row.get("trial_id") not in trial_by_id:
            errors.add("RESET_TRIAL_JOIN_MISSING", str(row.get("trial_id")))
        if row.get("success"):
            successful_reset_by_trial.setdefault(row["trial_id"], set()).update(
                row.get("memory_register_ids", [])
            )

    causal_break_rows = [
        row
        for row in trials
        if isinstance(row, dict)
        and row.get("valid")
        and row.get("analysis_role") == "causal_break"
    ]
    if not causal_break_rows:
        errors.add(
            "CAUSAL_BREAK_ARM_MISSING",
            "at least one implementation-complete causal-break arm is required",
        )
    for row in causal_break_rows:
        if not row.get("causal_break_id"):
            errors.add("CAUSAL_BREAK_ID_MISSING", str(row["trial_id"]))
        covered = successful_reset_by_trial.get(row["trial_id"], set())
        if not required_memory <= covered:
            errors.add(
                "RESET_SCOPE_INCOMPLETE",
                (
                    f"trial={row['trial_id']}; missing="
                    f"{sorted(required_memory - covered)}"
                ),
            )
        events = multitime_by_trial.get(row["trial_id"], [])
        if not any(event.get("causal_break_applied") for event in events):
            errors.add(
                "CAUSAL_BREAK_EVENT_UNRECORDED",
                str(row["trial_id"]),
            )

    if process_schema.get("raw_to_probability_rule") != (
        "count valid binary shot rows; never expand aggregate probabilities"
    ):
        errors.add(
            "RAW_TO_PROBABILITY_RULE_INVALID",
            str(process_schema.get("raw_to_probability_rule")),
        )
    if process_schema.get("row_to_map_rule_sha256") not in attachment_hashes:
        errors.add(
            "ROW_TO_MAP_ATTACHMENT_MISSING",
            str(process_schema.get("row_to_map_rule_sha256")),
        )

    return errors.finish()


def hoeffding_interval(
    successes: int,
    shots: int,
    simultaneous_terms: int,
    alpha: float,
) -> tuple[float, float]:
    radius = math.sqrt(
        math.log(2.0 * simultaneous_terms / alpha) / (2.0 * shots)
    )
    estimate = successes / shots
    return max(0.0, estimate - radius), min(1.0, estimate + radius)


def corrected_probability_interval(
    observed: tuple[float, float],
    false_positive: tuple[float, float],
    false_negative: tuple[float, float],
) -> tuple[float, float]:
    """Conservative interval division for q=e0+(1-e0-e1)p."""

    q_low, q_high = observed
    e0_low, e0_high = false_positive
    e1_low, e1_high = false_negative
    denominator_low = 1.0 - e0_high - e1_high
    denominator_high = 1.0 - e0_low - e1_low
    if denominator_low <= 0.0:
        raise ValueError("readout calibration is not invertible over its interval")
    if q_high < e0_low or q_low > 1.0 - e1_low:
        raise ValueError(
            "response and readout-calibration intervals have no physical overlap"
        )
    numerator_low = q_low - e0_high
    numerator_high = q_high - e0_low
    low = 0.0 if numerator_low <= 0.0 else numerator_low / denominator_high
    high = (
        1.0
        if numerator_high >= denominator_low
        else numerator_high / denominator_low
    )
    low = min(1.0, max(0.0, low))
    high = min(1.0, max(0.0, high))
    if low > high:
        raise ValueError("empty calibrated response interval")
    return low, high


def response_intervals(
    packet: dict[str, Any],
) -> tuple[dict[tuple[str, str], tuple[float, float]], dict[str, Any]]:
    heldout = [
        row
        for row in packet["trial_rows"]
        if row["valid"] and row["analysis_role"] == "held_out"
    ]
    block_cells: dict[tuple[str, str, str], list[int]] = {}
    for row in heldout:
        key = (
            row["history_id"],
            row["intervention_id"],
            row["calibration_block_id"],
        )
        counts = block_cells.setdefault(key, [0, 0])
        counts[0] += int(row["output_result"])
        counts[1] += 1

    calibration_by_id = {
        row["calibration_block_id"]: row for row in packet["calibration_rows"]
    }
    terms = len(block_cells) + 2 * len(calibration_by_id)
    alpha = packet["contract"]["familywise_alpha"]
    calibrated_blocks: dict[str, dict[str, tuple[float, float]]] = {}
    for block_id, row in calibration_by_id.items():
        e0 = row["prepared_0_observed_1"]
        e1 = row["prepared_1_observed_0"]
        calibrated_blocks[block_id] = {
            "false_positive": hoeffding_interval(
                e0["errors"], e0["shots"], terms, alpha
            ),
            "false_negative": hoeffding_interval(
                e1["errors"], e1["shots"], terms, alpha
            ),
        }

    block_intervals: dict[
        tuple[str, str, str], tuple[tuple[float, float], int]
    ] = {}
    for key, (successes, shots) in block_cells.items():
        block_id = key[2]
        observed = hoeffding_interval(successes, shots, terms, alpha)
        calibration = calibrated_blocks[block_id]
        corrected = corrected_probability_interval(
            observed,
            calibration["false_positive"],
            calibration["false_negative"],
        )
        systematic = calibration_by_id[block_id]["joint_spam_drift_tv_bound"]
        corrected = (
            max(0.0, corrected[0] - systematic),
            min(1.0, corrected[1] + systematic),
        )
        block_intervals[key] = (corrected, shots)

    by_cell: dict[tuple[str, str], list[tuple[tuple[float, float], int]]] = {}
    for (history, intervention, _), value in block_intervals.items():
        by_cell.setdefault((history, intervention), []).append(value)

    combined: dict[tuple[str, str], tuple[float, float]] = {}
    for key, parts in by_cell.items():
        total = sum(shots for _, shots in parts)
        low = sum(interval[0] * shots for interval, shots in parts) / total
        high = sum(interval[1] * shots for interval, shots in parts) / total
        combined[key] = (low, high)
    metadata = {
        "method": "simultaneous Hoeffding-Bonferroni with interval readout inversion",
        "familywise_alpha": alpha,
        "simultaneous_terms": terms,
        "response_cells": len(by_cell),
        "response_block_cells": len(block_cells),
        "calibration_blocks": len(calibration_by_id),
    }
    return combined, metadata


def history_partition(
    packet: dict[str, Any],
    refinement_field: str | None,
) -> dict[str, str]:
    partition: dict[str, str] = {}
    for row in packet["trial_rows"]:
        history = row["history_id"]
        label = (
            row["candidate_record_id"]
            if refinement_field is None
            else row["refinement_labels"][refinement_field]
        )
        partition.setdefault(history, label)
    return partition


def classify_quotient(
    packet: dict[str, Any],
    intervals: dict[tuple[str, str], tuple[float, float]],
    refinement_field: str | None,
) -> dict[str, Any]:
    partition = history_partition(packet, refinement_field)
    interventions = packet["contract"]["intervention_ids"]
    epsilon = packet["contract"]["equivalence_tolerance"]
    groups: dict[str, list[str]] = {}
    for history, label in partition.items():
        groups.setdefault(label, []).append(history)

    pair_receipts: list[dict[str, Any]] = []
    for label, histories in sorted(groups.items()):
        for left, right in itertools.combinations(sorted(histories), 2):
            for intervention in interventions:
                left_interval = intervals[(left, intervention)]
                right_interval = intervals[(right, intervention)]
                difference = (
                    left_interval[0] - right_interval[1],
                    left_interval[1] - right_interval[0],
                )
                equivalent = max(abs(difference[0]), abs(difference[1])) <= epsilon
                separated = difference[0] > epsilon or difference[1] < -epsilon
                pair_receipts.append(
                    {
                        "record_label": label,
                        "history_pair": [left, right],
                        "intervention_id": intervention,
                        "difference_interval": list(difference),
                        "equivalent_within_tolerance": equivalent,
                        "separated_beyond_tolerance": separated,
                    }
                )

    if any(row["separated_beyond_tolerance"] for row in pair_receipts):
        status = "CERTIFIED_FAILS"
    elif all(row["equivalent_within_tolerance"] for row in pair_receipts):
        status = "CERTIFIED_FACTORS"
    else:
        status = "INCONCLUSIVE"
    return {
        "status": status,
        "refinement_field": refinement_field,
        "equivalence_tolerance": epsilon,
        "nontrivial_pair_count": len(pair_receipts),
        "identity_like": len(pair_receipts) == 0,
        "separating_witnesses": [
            row for row in pair_receipts if row["separated_beyond_tolerance"]
        ][:4],
        "inconclusive_pairs": [
            row
            for row in pair_receipts
            if not row["separated_beyond_tolerance"]
            and not row["equivalent_within_tolerance"]
        ][:4],
        "worst_equivalence_width": max(
            (
                max(abs(row["difference_interval"][0]), abs(row["difference_interval"][1]))
                for row in pair_receipts
            ),
            default=0.0,
        ),
    }


def pareto_minimal(
    completions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    def dominates(left: dict[str, float], right: dict[str, float]) -> bool:
        keys = set(left) | set(right)
        leq = all(left.get(key, 0.0) <= right.get(key, 0.0) for key in keys)
        strict = any(left.get(key, 0.0) < right.get(key, 0.0) for key in keys)
        return leq and strict

    survivors = []
    for candidate in completions:
        if not any(
            other is not candidate
            and dominates(other["resources"], candidate["resources"])
            for other in completions
        ):
            survivors.append(candidate)
    return survivors


def assess_packet(packet: dict[str, Any]) -> dict[str, Any]:
    errors = validate_packet(packet)
    if errors:
        return {
            "verdict": "INCOMPLETE_CONTRACT",
            "scientific_verdict": False,
            "errors": errors,
        }

    try:
        intervals, uncertainty = response_intervals(packet)
    except ValueError as exc:
        return {
            "verdict": "INCOMPLETE_CONTRACT",
            "scientific_verdict": False,
            "errors": [
                {
                    "code": "CALIBRATION_IDENTIFICATION_FAILED",
                    "detail": str(exc),
                }
            ],
        }
    base = classify_quotient(packet, intervals, None)
    completion_results = []
    for completion in packet["contract"]["completion_class"]:
        classification = classify_quotient(
            packet,
            intervals,
            completion["refinement_field"],
        )
        completion_results.append(
            {
                "completion_id": completion["completion_id"],
                "resources": completion["resources"],
                "classification": classification,
            }
        )

    if base["status"] == "CERTIFIED_FACTORS":
        verdict = "TOLERANCE_BOUNDED_BASE_RECONSTRUCTION"
        minimal_repairs: list[dict[str, Any]] = []
    elif base["status"] == "CERTIFIED_FAILS":
        factoring = [
            row
            for row in completion_results
            if row["classification"]["status"] == "CERTIFIED_FACTORS"
        ]
        if factoring:
            verdict = "TOLERANCE_BOUNDED_REFINED_RECONSTRUCTION"
            minimal_repairs = pareto_minimal(factoring)
        elif all(
            row["classification"]["status"] == "CERTIFIED_FAILS"
            for row in completion_results
        ):
            verdict = "TOLERANCE_BOUNDED_CLASS_RELATIVE_REMAINDER_CANDIDATE"
            minimal_repairs = []
        else:
            verdict = "INCONCLUSIVE_FINITE_SHOT"
            minimal_repairs = []
    else:
        verdict = "INCONCLUSIVE_FINITE_SHOT"
        minimal_repairs = []

    physical = packet["evidence_kind"] == "physical_shot_packet"
    return {
        "verdict": verdict,
        "scientific_verdict": physical,
        "evidence_kind": packet["evidence_kind"],
        "packet_hash": canonical_hash(packet),
        "contract_hash": canonical_hash(packet["contract"]),
        "uncertainty": uncertainty,
        "base": base,
        "completion_results": completion_results,
        "pareto_minimal_repairs": minimal_repairs,
        "errors": [],
        "interpretation": (
            "eligible physical classification"
            if physical
            else "synthetic contract/classifier control only"
        ),
    }


def synthetic_probability(mode: str, history: str, intervention: str) -> float:
    environment = "E0" if history.startswith("h0") else "E1"
    if mode == "base":
        return 0.35 if intervention == "do_x" else 0.65
    if mode == "refined":
        if intervention == "do_x":
            return 0.20 if environment == "E0" else 0.80
        return 0.30 if environment == "E0" else 0.70
    if mode == "remainder":
        values = {
            "h0a": (0.10, 0.15),
            "h0b": (0.90, 0.85),
            "h1a": (0.20, 0.25),
            "h1b": (0.80, 0.75),
        }
        return values[history][0 if intervention == "do_x" else 1]
    if mode == "ambiguous":
        if intervention == "do_x":
            return 0.42 if environment == "E0" else 0.58
        return 0.43 if environment == "E0" else 0.57
    raise ValueError(mode)


def build_synthetic_packet(mode: str) -> dict[str, Any]:
    """Build raw-row controls without writing them to the repository."""

    hash_a = "a" * 64
    hash_b = "b" * 64
    hash_c = "c" * 64
    hash_d = "d" * 64
    hash_e = "e" * 64
    hash_f = "f" * 64
    histories = {
        "h0a": "E0",
        "h0b": "E0",
        "h1a": "E1",
        "h1b": "E1",
    }
    interventions = ["do_x", "do_z"]
    shots_per_cell = 1200
    false_positive = 0.005
    false_negative = 0.005

    packet: dict[str, Any] = {
        "schema_version": "du-physical-sufficiency-packet/0.1",
        "packet_id": f"synthetic-{mode}-control",
        "evidence_kind": "synthetic_contract_control",
        "source": {
            "title": f"deterministic {mode} schema/classifier control",
            "primary_uri": "internal://schema-control",
            "repository_commit": "synthetic-control-v1",
            "hardware_id": "none-synthetic",
            "protocol_id": "du-binary-multitime-control-v1",
            "acquisition_started_at": "2026-01-02T00:00:00Z",
            "acquisition_ended_at": "2026-01-02T01:00:00Z",
            "packet_created_at": "2026-01-02T02:00:00Z",
            "raw_attachment_manifest": [
                {"path": "trials.jsonl", "sha256": hash_a, "media_type": "application/jsonl"},
                {"path": "readout-counts.json", "sha256": hash_b, "media_type": "application/json"},
                {"path": "joint-uncertainty.json", "sha256": hash_c, "media_type": "application/json"},
                {"path": "preparation-calibration.json", "sha256": hash_d, "media_type": "application/json"},
                {"path": "route-passport.json", "sha256": hash_e, "media_type": "application/json"},
                {"path": "row-to-map.py", "sha256": hash_f, "media_type": "text/x-python"},
            ],
        },
        "freeze": {
            "contract_frozen_at": "2026-01-01T00:00:00Z",
            "record_selection_warrant": "candidate record fixed from apparatus archive field",
            "completion_selection_warrant": "environment and route fields fixed before holdout",
            "analysis_code_version": "du-acquisition-gate-v0.1",
            "holdout_policy": "all response shots below are held out from record selection",
            "blinded_fields": ["output_result"],
        },
        "contract": {
            "observer_id": "external-laboratory-agent",
            "access_boundary": "candidate archive plus declared conditional continuations",
            "outcome_alphabet": [0, 1],
            "intervention_ids": interventions,
            "candidate_record_field": "candidate_record_id",
            "target_response": "P(output_result=1 | history_id, intervention_id)",
            "metric": "binary_total_variation",
            "equivalence_tolerance": 0.22,
            "familywise_alpha": 0.05,
            "completion_class": [
                {
                    "completion_id": "formed-environment-record",
                    "refinement_field": "environment_record",
                    "formation_warrant": "independently archived environment syndrome",
                    "target_independent": True,
                    "resources": {"memory_bits": 1, "readout_channels": 1},
                },
                {
                    "completion_id": "formed-route-record",
                    "refinement_field": "route_record",
                    "formation_warrant": "independently authenticated route field",
                    "target_independent": True,
                    "resources": {"memory_bits": 2, "readout_channels": 2},
                },
            ],
            "memory_registers": [
                {
                    "memory_id": "candidate_archive",
                    "kind": "archive",
                    "boundary_status": "inside_candidate_record",
                    "reset_required_for_remainder": False,
                },
                {
                    "memory_id": "environment_memory",
                    "kind": "environment",
                    "boundary_status": "inside_admissible_completion",
                    "reset_required_for_remainder": True,
                },
                {
                    "memory_id": "controller_memory",
                    "kind": "controller",
                    "boundary_status": "outside_observer_access_but_physically_retained",
                    "reset_required_for_remainder": True,
                },
                {
                    "memory_id": "decoder_memory",
                    "kind": "decoder",
                    "boundary_status": "outside_observer_access_but_physically_retained",
                    "reset_required_for_remainder": True,
                },
            ],
            "minimum_heldout_shots_per_cell": shots_per_cell,
        },
        "process_schema": {
            "selective_map_convention": "CPTNI Choi, output-input ordering",
            "outcome_normalization": "trace gives selective outcome probability",
            "physicality_projection": "frozen constrained maximum likelihood",
            "tomography_scope": "declared binary held-out response slice plus full external adapter",
            "row_to_map_rule_id": "du-row-to-map-v0.1",
            "row_to_map_rule_sha256": hash_f,
            "raw_to_probability_rule": "count valid binary shot rows; never expand aggregate probabilities",
        },
        "attempt_count": 0,
        "trial_rows": [],
        "calibration_rows": [
            {
                "calibration_block_id": "cal-0",
                "valid_from": "2026-01-02T00:00:00Z",
                "valid_to": "2026-01-02T01:00:00Z",
                "controller_version": "controller-v1",
                "decoder_version": "decoder-v1",
                "preparation_model_id": "prep-v1",
                "readout_model_id": "readout-v1",
                "prepared_0_observed_1": {"shots": 10000, "errors": 50},
                "prepared_1_observed_0": {"shots": 10000, "errors": 50},
                "joint_uncertainty_method": "simultaneous_hoeffding_bonferroni_from_raw_counts",
                "joint_spam_drift_tv_bound": 0.0,
                "joint_spam_drift_bound_warrant": "zero by synthetic construction",
                "raw_attachment_sha256": hash_b,
                "preparation_calibration_sha256": hash_d,
                "joint_uncertainty_attachment_sha256": hash_c,
            }
        ],
        "multitime_rows": [],
        "reset_receipts": [],
        "route_rows": [
            {
                "route_id": "route-0",
                "source": "prepared source",
                "reference": "calibrated phase/readout reference",
                "processor": "declared process unit",
                "pointer": "selective binary pointer",
                "archive": "candidate archive",
                "detector": "binary detector",
                "environment": "declared environment port",
                "controller": "controller-v1",
                "decoder": "decoder-v1",
                "ordered_ports": ["source", "processor", "pointer", "archive", "detector"],
                "resources": {"shots": 1, "controller_calls": 1, "archive_bits": 1},
            }
        ],
    }

    trial_index = 0
    for history, environment in histories.items():
        for intervention in interventions:
            true_probability = synthetic_probability(mode, history, intervention)
            observed_probability = (
                false_positive
                + (1.0 - false_positive - false_negative) * true_probability
            )
            outcomes = [1] * round(observed_probability * shots_per_cell)
            outcomes += [0] * (shots_per_cell - len(outcomes))
            random.Random(f"{mode}:{history}:{intervention}").shuffle(outcomes)
            for result in outcomes:
                trial_index += 1
                trial_id = f"trial-{trial_index:06d}"
                row = {
                    "attempt_index": trial_index,
                    "trial_id": trial_id,
                    "history_id": history,
                    "sequence_id": f"sequence-{trial_index:06d}",
                    "repeat_index": 1,
                    "trial_order": trial_index,
                    "timestamp": "2026-01-02T00:30:00Z",
                    "preparation_id": "prep-0",
                    "intervention_id": intervention,
                    "candidate_record_id": "R-shared",
                    "refinement_labels": {
                        "environment_record": environment,
                        "route_record": environment,
                    },
                    "selective_outcome": environment,
                    "output_setting_id": "binary-output",
                    "output_result": result,
                    "valid": True,
                    "rejection_reason": None,
                    "calibration_block_id": "cal-0",
                    "controller_version": "controller-v1",
                    "decoder_version": "decoder-v1",
                    "route_id": "route-0",
                    "provenance_sha256": hash_a,
                    "analysis_role": "held_out",
                    "causal_break_id": None,
                }
                packet["trial_rows"].append(row)
                packet["multitime_rows"].append(
                    {
                        "trial_id": trial_id,
                        "event_index": 0,
                        "event_id": f"event-{trial_index:06d}",
                        "intervention_id": intervention,
                        "instrument_outcome": environment,
                        "prior_record_id": "R-shared",
                        "causal_break_applied": False,
                        "held_out_continuation": True,
                        "reset_receipt_ids": [],
                    }
                )

    required_memory = [
        "environment_memory",
        "controller_memory",
        "decoder_memory",
    ]
    for history, environment in histories.items():
        for intervention in interventions:
            trial_index += 1
            trial_id = f"trial-{trial_index:06d}"
            reset_id = f"reset-{trial_index:06d}"
            packet["trial_rows"].append(
                {
                    "attempt_index": trial_index,
                    "trial_id": trial_id,
                    "history_id": history,
                    "sequence_id": f"causal-break-{trial_index:06d}",
                    "repeat_index": 2,
                    "trial_order": trial_index,
                    "timestamp": "2026-01-02T00:45:00Z",
                    "preparation_id": "prep-0",
                    "intervention_id": intervention,
                    "candidate_record_id": "R-shared",
                    "refinement_labels": {
                        "environment_record": environment,
                        "route_record": environment,
                    },
                    "selective_outcome": "post-reset",
                    "output_setting_id": "binary-output",
                    "output_result": 0,
                    "valid": True,
                    "rejection_reason": None,
                    "calibration_block_id": "cal-0",
                    "controller_version": "controller-v1",
                    "decoder_version": "decoder-v1",
                    "route_id": "route-0",
                    "provenance_sha256": hash_a,
                    "analysis_role": "causal_break",
                    "causal_break_id": "complete-break-v1",
                }
            )
            packet["reset_receipts"].append(
                {
                    "reset_receipt_id": reset_id,
                    "trial_id": trial_id,
                    "reset_protocol_id": "complete-break-v1",
                    "memory_register_ids": required_memory,
                    "success": True,
                    "verification_method": "independent reset witness",
                    "verification_result": "all declared retained memories reset",
                    "timestamp": "2026-01-02T00:44:59Z",
                }
            )
            packet["multitime_rows"].append(
                {
                    "trial_id": trial_id,
                    "event_index": 0,
                    "event_id": f"event-{trial_index:06d}",
                    "intervention_id": intervention,
                    "instrument_outcome": "post-reset",
                    "prior_record_id": "R-shared",
                    "causal_break_applied": True,
                    "held_out_continuation": True,
                    "reset_receipt_ids": [reset_id],
                }
            )

    trial_index += 1
    packet["trial_rows"].append(
        {
            "attempt_index": trial_index,
            "trial_id": f"trial-{trial_index:06d}",
            "history_id": "h0a",
            "sequence_id": f"invalid-{trial_index:06d}",
            "repeat_index": 0,
            "trial_order": trial_index,
            "timestamp": "2026-01-02T00:50:00Z",
            "preparation_id": "prep-0",
            "intervention_id": "do_x",
            "candidate_record_id": "R-shared",
            "refinement_labels": {
                "environment_record": "E0",
                "route_record": "E0",
            },
            "selective_outcome": "invalid",
            "output_setting_id": "binary-output",
            "output_result": None,
            "valid": False,
            "rejection_reason": "synthetic invalid-attempt retention control",
            "calibration_block_id": "cal-0",
            "controller_version": "controller-v1",
            "decoder_version": "decoder-v1",
            "route_id": "route-0",
            "provenance_sha256": hash_a,
            "analysis_role": "training",
            "causal_break_id": None,
        }
    )
    packet["attempt_count"] = len(packet["trial_rows"])
    return packet


def run() -> dict[str, Any]:
    receipt = Receipt()

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    definition_contracts = {
        "source": SOURCE_REQUIRED,
        "freeze": FREEZE_REQUIRED,
        "contract": CONTRACT_REQUIRED,
        "processSchema": PROCESS_REQUIRED,
        "trialRow": TRIAL_REQUIRED,
        "calibrationRow": CALIBRATION_REQUIRED,
        "multitimeRow": MULTITIME_REQUIRED,
        "resetReceipt": RESET_REQUIRED,
        "routeRow": ROUTE_REQUIRED,
        "completion": COMPLETION_REQUIRED,
        "memoryRegister": MEMORY_REQUIRED,
        "rawAttachment": ATTACHMENT_REQUIRED,
    }
    receipt.check(
        "versioned_schema_is_valid_json_and_has_four_linked_table_defs",
        schema["properties"]["trial_rows"]
        and schema["properties"]["calibration_rows"]
        and schema["properties"]["multitime_rows"]
        and schema["properties"]["reset_receipts"]
        and all(
            set(schema["$defs"][name]["required"]) == required
            for name, required in definition_contracts.items()
        ),
        (
            f"schema={SCHEMA.relative_to(ROOT)}; "
            f"definitions={sorted(definition_contracts)}"
        ),
    )
    receipt.check(
        "schema_requires_raw_attempt_calibration_process_route_and_reset_surfaces",
        set(schema["required"]) == TOP_REQUIRED,
        f"required={schema['required']}",
    )

    aggregate = json.loads(AGGREGATE_FIXTURE.read_text(encoding="utf-8"))
    aggregate_result = assess_packet(aggregate)
    aggregate_codes = {row["code"] for row in aggregate_result["errors"]}
    receipt.check(
        "xiang_style_aggregate_packet_is_refused",
        aggregate_result["verdict"] == "INCOMPLETE_CONTRACT"
        and "AGGREGATE_PROBABILITY_FORBIDDEN" in aggregate_codes
        and "MISSING_TRIAL_ROWS" in aggregate_codes
        and "MISSING_CALIBRATION_ROWS" in aggregate_codes,
        f"codes={sorted(aggregate_codes)}",
    )

    base_packet = build_synthetic_packet("base")
    base_result = assess_packet(base_packet)
    receipt.check(
        "complete_base_factorization_control_classifies",
        base_result["verdict"] == "TOLERANCE_BOUNDED_BASE_RECONSTRUCTION",
        base_result["verdict"],
    )

    refined_packet = build_synthetic_packet("refined")
    refined_result = assess_packet(refined_packet)
    minimal_ids = {
        row["completion_id"] for row in refined_result["pareto_minimal_repairs"]
    }
    receipt.check(
        "complete_minimal_refinement_control_classifies",
        refined_result["verdict"]
        == "TOLERANCE_BOUNDED_REFINED_RECONSTRUCTION"
        and minimal_ids == {"formed-environment-record"},
        f"verdict={refined_result['verdict']}; minimal={sorted(minimal_ids)}",
    )

    remainder_packet = build_synthetic_packet("remainder")
    remainder_result = assess_packet(remainder_packet)
    receipt.check(
        "completion_class_relative_remainder_control_classifies",
        remainder_result["verdict"]
        == "TOLERANCE_BOUNDED_CLASS_RELATIVE_REMAINDER_CANDIDATE",
        remainder_result["verdict"],
    )

    ambiguous_packet = build_synthetic_packet("ambiguous")
    ambiguous_result = assess_packet(ambiguous_packet)
    receipt.check(
        "finite_shot_overlap_returns_inconclusive",
        ambiguous_result["verdict"] == "INCONCLUSIVE_FINITE_SHOT",
        ambiguous_result["verdict"],
    )

    missing_reset = copy.deepcopy(remainder_packet)
    missing_reset["reset_receipts"][0]["memory_register_ids"].remove(
        "controller_memory"
    )
    missing_reset_result = assess_packet(missing_reset)
    missing_reset_codes = {row["code"] for row in missing_reset_result["errors"]}
    receipt.check(
        "unreset_retained_memory_blocks_remainder",
        missing_reset_result["verdict"] == "INCOMPLETE_CONTRACT"
        and "RESET_SCOPE_INCOMPLETE" in missing_reset_codes,
        f"codes={sorted(missing_reset_codes)}",
    )

    missing_calibration = copy.deepcopy(base_packet)
    missing_calibration["trial_rows"][0]["calibration_block_id"] = "absent"
    missing_calibration_result = assess_packet(missing_calibration)
    missing_calibration_codes = {
        row["code"] for row in missing_calibration_result["errors"]
    }
    receipt.check(
        "unjoined_calibration_blocks_adjudication",
        missing_calibration_result["verdict"] == "INCOMPLETE_CONTRACT"
        and "CALIBRATION_JOIN_MISSING" in missing_calibration_codes,
        f"codes={sorted(missing_calibration_codes)}",
    )

    missing_attempt = copy.deepcopy(base_packet)
    missing_attempt["attempt_count"] += 1
    missing_attempt_result = assess_packet(missing_attempt)
    missing_attempt_codes = {row["code"] for row in missing_attempt_result["errors"]}
    receipt.check(
        "missing_attempts_block_selection_bias",
        missing_attempt_result["verdict"] == "INCOMPLETE_CONTRACT"
        and "ATTEMPT_LEDGER_INCOMPLETE" in missing_attempt_codes,
        f"codes={sorted(missing_attempt_codes)}",
    )

    receipt.check(
        "all_statistical_controls_remain_nonphysical",
        not any(
            result["scientific_verdict"]
            for result in [
                base_result,
                refined_result,
                remainder_result,
                ambiguous_result,
            ]
        ),
        "evidence_kind=synthetic_contract_control on every statistical branch",
    )
    receipt.check(
        "public_audit_closes_only_the_bounded_sidecar_route",
        PUBLIC_SIDECAR_AUDIT["verdict"] == "NO_JOINED_SHOT_LEVEL_SIDECAR"
        and PUBLIC_SIDECAR_AUDIT["filename_sidecar_keyword_hits"] == 0,
        (
            f"commit={PUBLIC_SIDECAR_AUDIT['commit']}; "
            f"files={PUBLIC_SIDECAR_AUDIT['recursive_tree_file_count']}"
        ),
    )

    final_receipt = receipt.close()
    result = {
        "run_id": RUN_ID,
        "status": (
            "PASS_PROSPECTIVE_GATE_READY"
            if final_receipt["all_passed"]
            else "FAIL"
        ),
        "scientific_grade": (
            "PUBLIC SIDECAR AUDIT PLUS PROSPECTIVE ACQUISITION CONTRACT AND "
            "FINITE-SHOT CLASSIFIER CONTROLS / NO PHYSICAL FACTORIZATION, "
            "REMAINDER, ONTOLOGY, OR NEW-PHYSICS VERDICT"
        ),
        "north_star_outcome": "PROSPECTIVE_GATE_READY",
        "plain_english": (
            "The strongest public reopener still lacks the joined shot, "
            "calibration, provenance, selective-history, and complete-reset "
            "record needed for a physical verdict. Dynamic Unity now has a "
            "versioned packet contract and executable finite-shot gate that "
            "refuses those omissions and distinguishes base reconstruction, "
            "minimal refinement, class-relative remainder, and honest "
            "finite-shot inconclusiveness on nonphysical controls."
        ),
        "public_sidecar_audit": PUBLIC_SIDECAR_AUDIT,
        "schema": str(SCHEMA.relative_to(ROOT)),
        "schema_sha256": hashlib.sha256(SCHEMA.read_bytes()).hexdigest(),
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "finite_shot_method": {
            "response": "binary held-out response cells",
            "coverage": "simultaneous Hoeffding-Bonferroni",
            "calibration": "conservative interval inversion of binary readout confusion",
            "factorization": (
                "all same-record history-pair difference intervals lie "
                "inside the frozen total-variation tolerance"
            ),
            "separation": (
                "at least one same-record pair is separated beyond the "
                "frozen tolerance"
            ),
            "inconclusive": (
                "confidence region overlaps both factoring and separating "
                "possibilities"
            ),
        },
        "control_results": {
            "aggregate_refusal": aggregate_result,
            "base_reconstruction": base_result,
            "refined_reconstruction": refined_result,
            "class_relative_remainder": remainder_result,
            "finite_shot_inconclusive": ambiguous_result,
            "unreset_memory_refusal": missing_reset_result,
            "calibration_join_refusal": missing_calibration_result,
            "attempt_ledger_refusal": missing_attempt_result,
        },
        "remaining_physical_gate": (
            "Acquire one packet under the versioned schema, retain every "
            "attempt and raw shot, attach preparation/readout/joint "
            "calibration objects, preserve selective multi-time outcomes and "
            "route provenance, verify a causal break over every admitted "
            "retained memory, and freeze record/completion/tolerance/holdout "
            "before revealing response outcomes."
        ),
        "receipt": final_receipt,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Run the deterministic DU acquisition-gate controls, or assess "
            "one prospective packet without writing an artifact."
        )
    )
    parser.add_argument(
        "--packet",
        type=Path,
        help="JSON packet conforming to the v0.1 acquisition schema",
    )
    args = parser.parse_args()
    if args.packet is not None:
        packet = json.loads(args.packet.read_text(encoding="utf-8"))
        assessment = assess_packet(packet)
        assessment["packet_path"] = str(args.packet)
        assessment["schema"] = str(SCHEMA.relative_to(ROOT))
        assessment["probe_sha256"] = hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest()
        print(canonical_json(assessment), end="")
        if assessment["verdict"] == "INCOMPLETE_CONTRACT":
            raise SystemExit(2)
        return

    result = run()
    payload = canonical_json(result)
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    print(
        f"{result['status']}: "
        f"{result['receipt']['passed']}/{result['receipt']['total']} checks"
    )
    print(f"artifact={ARTIFACT.relative_to(ROOT)}")
    print(f"sha256={digest}")
    if not result["receipt"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
