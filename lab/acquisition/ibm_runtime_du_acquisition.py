#!/usr/bin/env python3
"""Hardware-ready acquisition bridge for DU-PAPER-007.

The module deliberately separates three things:

1. a frozen QND-memory/held-out-continuation circuit manifest;
2. a provider-facing, shot-resolved capture; and
3. the stricter Dynamic Unity physical-sufficiency packet.

The local ``simulate`` command validates circuit construction and register
lineage only. It always emits ``synthetic_provider_control``. The ``submit``
command is guarded because it creates an external quantum-hardware job and
must never be run by an agent without exact Joe-direct-chat authorization.

Qiskit is an optional acquisition dependency. The semantic validator and
claim-ceiling classifier use only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import io
import json
import math
import os
import random
import sys
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "du-provider-capture/0.1"
PROTOCOL_ID = "du-qnd-memory-causal-break/0.1"
ANALYSIS_CODE_VERSION = "du-acquisition-bridge/0.1"
RUN_ID = "RUN-20260726-070222-hardware-acquisition-bridge"
CIRCUIT_ORDER_SEED = 271828
SIMULATOR_SEED = 314159
DEFAULT_POINTER_ANGLE = math.pi / 2
SYNTHETIC_START = "2000-01-01T00:00:00+00:00"
SYNTHETIC_STOP = "2000-01-01T00:00:01+00:00"
MINIMUM_AUTHORIZATION_ID_LENGTH = 16

REGISTER_WIDTHS = {
    "pointer": 1,
    "environment": 1,
    "reset_witness": 3,
    "output": 1,
}

TOP_REQUIRED = {
    "schema_version",
    "capture_id",
    "evidence_kind",
    "provider",
    "freeze",
    "protocol",
    "circuits",
    "execution_spans",
    "shot_rows",
    "missingness",
    "reset_scope",
    "attachments",
}

PROVIDER_REQUIRED = {
    "name",
    "interface",
    "client_versions",
    "backend_id",
    "job_id",
    "job_status",
    "calibration_id",
    "created_at",
    "started_at",
    "ended_at",
    "capture_created_at",
    "execution_options",
    "backend_properties_sha256",
}

FREEZE_REQUIRED = {
    "frozen_at",
    "protocol_id",
    "circuit_manifest_sha256",
    "analysis_code_version",
    "attempt_population_claim",
    "returned_shot_policy",
    "invalid_attempt_visibility",
    "holdout_policy",
}

PROTOCOL_REQUIRED = {
    "protocol_id",
    "system_qubit_count",
    "qubit_roles",
    "register_roles",
    "candidate_record",
    "completion_records",
    "intervention_ids",
    "qnd_pointer_angle_radians",
    "circuit_order_seed",
    "shots_per_circuit",
    "predeclared_expected_branch",
}

CIRCUIT_REQUIRED = {
    "circuit_id",
    "circuit_index",
    "role",
    "history_id",
    "intervention_id",
    "analysis_role",
    "preparation_id",
    "causal_break",
    "calibration_target",
    "calibration_prepared_value",
    "register_map",
    "source_qpy_sha256",
    "transpiled_qpy_sha256",
    "expected_shots",
}

SPAN_REQUIRED = {
    "span_id",
    "start",
    "stop",
    "precision",
    "warrant",
}

SHOT_REQUIRED = {
    "circuit_id",
    "circuit_index",
    "shot_index",
    "span_id",
    "registers",
    "provider_valid",
    "provider_rejection_reason",
    "raw_register_sha256",
}

MISSING_REQUIRED = {
    "circuits_submitted",
    "shots_requested",
    "shots_returned",
    "all_requested_shots_returned",
    "provider_discard_count_known",
    "provider_declared_discarded_shots",
    "invalid_attempt_rows_exposed",
    "filtering_policy",
}

RESET_REQUIRED = {
    "memories",
    "causal_break_circuit_ids",
    "witness_register",
    "all_reset_required_memories_witnessed",
    "unobserved_provider_memory_present",
}


@dataclass(frozen=True)
class CircuitSpec:
    """Target-independent semantic identity of one acquisition circuit."""

    circuit_id: str
    role: str
    history_id: str | None
    intervention_id: str | None
    analysis_role: str
    preparation_id: str
    causal_break: bool
    calibration_target: str | None = None
    calibration_prepared_value: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "circuit_id": self.circuit_id,
            "role": self.role,
            "history_id": self.history_id,
            "intervention_id": self.intervention_id,
            "analysis_role": self.analysis_role,
            "preparation_id": self.preparation_id,
            "causal_break": self.causal_break,
            "calibration_target": self.calibration_target,
            "calibration_prepared_value": self.calibration_prepared_value,
        }


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_timestamp(value: str | None) -> datetime | None:
    if value is None:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def exact_keyset(value: Any, required: set[str], label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label}_NOT_OBJECT"]
    missing = sorted(required - set(value))
    extra = sorted(set(value) - required)
    codes: list[str] = []
    if missing:
        codes.append(f"{label}_MISSING:{','.join(missing)}")
    if extra:
        codes.append(f"{label}_EXTRA:{','.join(extra)}")
    return codes


def build_circuit_specs() -> list[CircuitSpec]:
    """Return the complete preregistered suite in deterministic shuffled order."""

    specs: list[CircuitSpec] = []

    for register in ("pointer", "environment", "output"):
        for prepared in (0, 1):
            specs.append(
                CircuitSpec(
                    circuit_id=f"cal-{register}-{prepared}",
                    role="readout_calibration",
                    history_id=None,
                    intervention_id=None,
                    analysis_role="calibration",
                    preparation_id=f"prepare-{register}-{prepared}",
                    causal_break=False,
                    calibration_target=register,
                    calibration_prepared_value=prepared,
                )
            )

    for qubit in range(3):
        specs.append(
            CircuitSpec(
                circuit_id=f"cal-reset-q{qubit}",
                role="reset_calibration",
                history_id=None,
                intervention_id=None,
                analysis_role="calibration",
                preparation_id=f"prepare-q{qubit}-one-then-reset",
                causal_break=True,
                calibration_target=f"reset_witness[{qubit}]",
                calibration_prepared_value=0,
            )
        )

    for analysis_role in ("training", "held_out"):
        for history in (0, 1):
            for intervention in ("identity_z", "flip_z"):
                specs.append(
                    CircuitSpec(
                        circuit_id=(
                            f"exp-{analysis_role}-h{history}-{intervention}"
                        ),
                        role="experiment",
                        history_id=f"h{history}",
                        intervention_id=intervention,
                        analysis_role=analysis_role,
                        preparation_id=f"prepare-system-{history}",
                        causal_break=False,
                    )
                )

    for history in (0, 1):
        specs.append(
            CircuitSpec(
                circuit_id=f"exp-causal-break-h{history}",
                role="experiment",
                history_id=f"h{history}",
                intervention_id="causal_break_identity_z",
                analysis_role="causal_break",
                preparation_id=f"prepare-system-{history}",
                causal_break=True,
            )
        )

    rng = random.Random(CIRCUIT_ORDER_SEED)
    rng.shuffle(specs)
    return specs


def semantic_manifest(
    specs: Iterable[CircuitSpec],
    *,
    shots: int,
    pointer_angle: float,
) -> dict[str, Any]:
    return {
        "protocol_id": PROTOCOL_ID,
        "shots_per_circuit": shots,
        "qnd_pointer_angle_radians": pointer_angle,
        "circuit_order_seed": CIRCUIT_ORDER_SEED,
        "circuits": [spec.to_dict() for spec in specs],
    }


def qpy_sha256(circuit: Any) -> str:
    """Hash one Qiskit circuit without making Qiskit a module import dependency."""

    from qiskit import qpy

    buffer = io.BytesIO()
    qpy.dump(circuit, buffer)
    return sha256_bytes(buffer.getvalue())


def build_qiskit_circuits(
    specs: list[CircuitSpec],
    *,
    pointer_angle: float,
) -> list[Any]:
    """Construct the three-qubit QND-memory and causal-break suite."""

    from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister

    circuits: list[Any] = []
    for spec in specs:
        qubits = QuantumRegister(3, "q")
        pointer = ClassicalRegister(1, "pointer")
        environment = ClassicalRegister(1, "environment")
        reset_witness = ClassicalRegister(3, "reset_witness")
        output = ClassicalRegister(1, "output")
        circuit = QuantumCircuit(
            qubits,
            pointer,
            environment,
            reset_witness,
            output,
            name=spec.circuit_id,
        )

        if spec.role == "readout_calibration":
            register_to_qubit = {
                "pointer": 2,
                "environment": 1,
                "output": 0,
            }
            target_qubit = register_to_qubit[spec.calibration_target or ""]
            if spec.calibration_prepared_value == 1:
                circuit.x(target_qubit)
            if spec.calibration_target == "pointer":
                circuit.measure(target_qubit, pointer[0])
            elif spec.calibration_target == "environment":
                circuit.measure(target_qubit, environment[0])
            else:
                circuit.measure(target_qubit, output[0])

        elif spec.role == "reset_calibration":
            target_qubit = int((spec.calibration_target or "")[-2])
            circuit.x(target_qubit)
            circuit.reset(target_qubit)
            circuit.measure(target_qubit, reset_witness[target_qubit])

        else:
            history = int((spec.history_id or "h0")[1:])
            if history == 1:
                circuit.x(0)

            # The environment retains a formed history syndrome. The pointer
            # is a deliberately incomplete QND-like candidate record.
            circuit.cx(0, 1)
            circuit.cry(pointer_angle, 0, 2)
            circuit.measure(2, pointer[0])

            if spec.causal_break:
                for qubit in range(3):
                    circuit.reset(qubit)
                circuit.measure(qubits, reset_witness)
                for qubit in range(3):
                    circuit.reset(qubit)
                circuit.measure(1, environment[0])
                circuit.measure(0, output[0])
            else:
                if spec.intervention_id == "flip_z":
                    circuit.x(0)
                circuit.measure(1, environment[0])
                circuit.measure(0, output[0])

        circuit.metadata = {
            **spec.to_dict(),
            "protocol_id": PROTOCOL_ID,
            "candidate_record": "pointer",
            "formed_completion": "environment",
            "register_widths": REGISTER_WIDTHS,
        }
        circuits.append(circuit)

    return circuits


def protocol_object(*, shots: int, pointer_angle: float) -> dict[str, Any]:
    return {
        "protocol_id": PROTOCOL_ID,
        "system_qubit_count": 3,
        "qubit_roles": {
            "system": 0,
            "environment": 1,
            "pointer": 2,
        },
        "register_roles": {
            "pointer": "candidate_record",
            "environment": "formed_completion",
            "reset_witness": "causal_break_verification",
            "output": "held_out_binary_response",
        },
        "candidate_record": "pointer",
        "completion_records": ["environment"],
        "intervention_ids": [
            "identity_z",
            "flip_z",
            "causal_break_identity_z",
        ],
        "qnd_pointer_angle_radians": pointer_angle,
        "circuit_order_seed": CIRCUIT_ORDER_SEED,
        "shots_per_circuit": shots,
        "predeclared_expected_branch": (
            "TOLERANCE_BOUNDED_REFINED_RECONSTRUCTION"
        ),
    }


def reset_scope(
    specs: Iterable[CircuitSpec],
    *,
    hardware: bool,
) -> dict[str, Any]:
    return {
        "memories": [
            {
                "memory_id": "q_system",
                "kind": "quantum",
                "inside_declared_boundary": True,
                "reset_required_for_remainder": True,
            },
            {
                "memory_id": "q_environment",
                "kind": "environment",
                "inside_declared_boundary": True,
                "reset_required_for_remainder": True,
            },
            {
                "memory_id": "q_pointer",
                "kind": "quantum",
                "inside_declared_boundary": True,
                "reset_required_for_remainder": True,
            },
            {
                "memory_id": "classical_pointer_archive",
                "kind": "archive",
                "inside_declared_boundary": True,
                "reset_required_for_remainder": False,
            },
            {
                "memory_id": "provider_controller_and_environment",
                "kind": "controller",
                "inside_declared_boundary": False,
                "reset_required_for_remainder": True,
            },
        ],
        "causal_break_circuit_ids": [
            spec.circuit_id for spec in specs if spec.analysis_role == "causal_break"
        ],
        "witness_register": "reset_witness",
        "all_reset_required_memories_witnessed": not hardware,
        "unobserved_provider_memory_present": hardware,
    }


def bit_rows(value: Any, width: int) -> list[list[int]]:
    """Convert a Qiskit BitArray or bool ndarray to shot-major integer rows."""

    if hasattr(value, "to_bool_array"):
        array = value.to_bool_array(order="little")
    else:
        array = value
    if hasattr(array, "tolist"):
        rows = array.tolist()
    else:
        rows = list(array)
    normalized: list[list[int]] = []
    for row in rows:
        if not isinstance(row, list):
            row = [row]
        bits = [int(bool(bit)) for bit in row]
        if len(bits) != width:
            raise ValueError(
                f"register width mismatch: expected {width}, got {len(bits)}"
            )
        normalized.append(bits)
    return normalized


def provider_time_window(
    result: Any,
    *,
    synthetic: bool,
    pub_shot_counts: list[int],
) -> tuple[list[dict[str, Any]], dict[tuple[int, int], str], str, str]:
    if synthetic:
        span = {
            "span_id": "span-synthetic-fixed",
            "start": SYNTHETIC_START,
            "stop": SYNTHETIC_STOP,
            "precision": "synthetic_fixed_window",
            "warrant": "Deterministic local-control timestamp; not hardware timing.",
        }
        assignments = {
            (pub_index, shot_index): span["span_id"]
            for pub_index, count in enumerate(pub_shot_counts)
            for shot_index in range(count)
        }
        return [span], assignments, SYNTHETIC_START, SYNTHETIC_STOP

    metadata = getattr(result, "metadata", {}) or {}
    execution = metadata.get("execution", {}) if isinstance(metadata, dict) else {}
    provider_spans = (
        execution.get("execution_spans") if isinstance(execution, dict) else None
    )
    if provider_spans is not None and len(provider_spans) > 0:
        rows: list[dict[str, Any]] = []
        assignments: dict[tuple[int, int], str] = {}
        for span_index, provider_span in enumerate(provider_spans):
            start = getattr(provider_span, "start", None)
            stop = getattr(provider_span, "stop", None)
            if start is None or stop is None:
                raise ValueError("provider execution span lacks start or stop")
            span_id = f"span-provider-{span_index:04d}"
            rows.append(
                {
                    "span_id": span_id,
                    "start": start.isoformat(),
                    "stop": stop.isoformat(),
                    "precision": "provider_execution_span",
                    "warrant": (
                        "Provider span plus PUB/shot mask. This bounds the "
                        "referenced returned shots; it is not an exact "
                        "per-shot timestamp."
                    ),
                }
            )
            for pub_index, shot_count in enumerate(pub_shot_counts):
                mask = provider_span.mask(pub_index)
                if hasattr(mask, "reshape"):
                    flat_mask = mask.reshape(-1).tolist()
                elif hasattr(mask, "tolist"):
                    flat_mask = mask.tolist()
                else:
                    flat_mask = list(mask)
                if len(flat_mask) != shot_count:
                    raise ValueError(
                        "execution-span mask does not join to the PUB shot axis"
                    )
                for shot_index, included in enumerate(flat_mask):
                    if not bool(included):
                        continue
                    key = (pub_index, shot_index)
                    if key in assignments:
                        raise ValueError(
                            "one returned shot is assigned to multiple "
                            "execution spans"
                        )
                    assignments[key] = span_id

        expected = {
            (pub_index, shot_index)
            for pub_index, count in enumerate(pub_shot_counts)
            for shot_index in range(count)
        }
        if set(assignments) != expected:
            raise ValueError(
                "provider execution spans do not cover every returned shot"
            )
        return (
            rows,
            assignments,
            min(row["start"] for row in rows),
            max(row["stop"] for row in rows),
        )

    now = utc_now()
    span = {
        "span_id": "span-job-window-fallback",
        "start": now,
        "stop": now,
        "precision": "job_window",
        "warrant": (
            "Provider execution spans unavailable; capture time is a weak "
            "fallback and blocks fine-grained drift claims."
        ),
    }
    assignments = {
        (pub_index, shot_index): span["span_id"]
        for pub_index, count in enumerate(pub_shot_counts)
        for shot_index in range(count)
    }
    return [span], assignments, now, now


def circuit_rows(
    specs: list[CircuitSpec],
    source_circuits: list[Any],
    transpiled_circuits: list[Any],
    *,
    shots: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index, (spec, source, transpiled) in enumerate(
        zip(specs, source_circuits, transpiled_circuits, strict=True)
    ):
        rows.append(
            {
                **spec.to_dict(),
                "circuit_index": index,
                "register_map": deepcopy(REGISTER_WIDTHS),
                "source_qpy_sha256": qpy_sha256(source),
                "transpiled_qpy_sha256": qpy_sha256(transpiled),
                "expected_shots": shots,
            }
        )
    return rows


def result_registers(pub_result: Any) -> dict[str, list[list[int]]]:
    data = getattr(pub_result, "data", None)
    if data is None:
        raise ValueError("sampler result has no data bin")
    output: dict[str, list[list[int]]] = {}
    for register, width in REGISTER_WIDTHS.items():
        value = getattr(data, register, None)
        if value is None:
            raise ValueError(f"sampler result missing register {register}")
        output[register] = bit_rows(value, width)
    counts = {len(rows) for rows in output.values()}
    if len(counts) != 1:
        raise ValueError("classical register shot axes are not joinable")
    return output


def sampler_capture(
    *,
    specs: list[CircuitSpec],
    source_circuits: list[Any],
    transpiled_circuits: list[Any],
    result: Any,
    shots: int,
    pointer_angle: float,
    provider_info: dict[str, Any],
    synthetic: bool,
    frozen_at: str | None = None,
) -> dict[str, Any]:
    if not synthetic and frozen_at is None:
        raise ValueError("hardware capture requires a pre-acquisition freeze time")

    circuits = circuit_rows(
        specs,
        source_circuits,
        transpiled_circuits,
        shots=shots,
    )
    manifest = semantic_manifest(specs, shots=shots, pointer_angle=pointer_angle)
    pub_results = list(result)
    joined_registers = [result_registers(pub_result) for pub_result in pub_results]
    pub_shot_counts = [
        len(registers["output"]) for registers in joined_registers
    ]
    spans, span_assignments, started_at, ended_at = provider_time_window(
        result,
        synthetic=synthetic,
        pub_shot_counts=pub_shot_counts,
    )

    shot_rows: list[dict[str, Any]] = []
    for circuit_index, (spec, registers) in enumerate(
        zip(specs, joined_registers, strict=True)
    ):
        row_count = len(registers["output"])
        for shot_index in range(row_count):
            shot_registers = {
                key: registers[key][shot_index] for key in REGISTER_WIDTHS
            }
            shot_rows.append(
                {
                    "circuit_id": spec.circuit_id,
                    "circuit_index": circuit_index,
                    "shot_index": shot_index,
                    "span_id": span_assignments[(circuit_index, shot_index)],
                    "registers": shot_registers,
                    "provider_valid": True,
                    "provider_rejection_reason": None,
                    "raw_register_sha256": sha256_json(shot_registers),
                }
            )

    requested = shots * len(specs)
    returned = len(shot_rows)
    created_at = provider_info.get("created_at")
    capture_created_at = provider_info.get("capture_created_at") or (
        SYNTHETIC_STOP if synthetic else utc_now()
    )
    provider_info = {
        **provider_info,
        "created_at": created_at,
        "started_at": provider_info.get("started_at") or started_at,
        "ended_at": provider_info.get("ended_at") or ended_at,
        "capture_created_at": capture_created_at,
    }

    backend_digest = provider_info["backend_properties_sha256"]
    raw_digest = sha256_json(shot_rows)
    circuit_digest = sha256_json(circuits)
    capture = {
        "schema_version": SCHEMA_VERSION,
        "capture_id": (
            "du-synthetic-qnd-memory-v0.1"
            if synthetic
            else f"du-hardware-{provider_info['job_id']}"
        ),
        "evidence_kind": (
            "synthetic_provider_control"
            if synthetic
            else "hardware_provider_capture"
        ),
        "provider": provider_info,
        "freeze": {
            "frozen_at": (
                SYNTHETIC_START if synthetic else frozen_at
            ),
            "protocol_id": PROTOCOL_ID,
            "circuit_manifest_sha256": sha256_json(manifest),
            "analysis_code_version": ANALYSIS_CODE_VERSION,
            "attempt_population_claim": (
                "all_physical_triggers_visible"
                if synthetic
                else "all_provider_returned_shots_visible"
            ),
            "returned_shot_policy": (
                "Every simulator invocation is returned."
                if synthetic
                else (
                    "Every shot exposed by the provider result is retained; "
                    "unexposed lower-level retries or filtering are not invented."
                )
            ),
            "invalid_attempt_visibility": (
                "all_invalid_attempts_joined"
                if synthetic
                else "detectable_protocol_invalids_only"
            ),
            "holdout_policy": (
                "Distinct preregistered circuit identities separate training, "
                "held-out, calibration, and causal-break arms."
            ),
        },
        "protocol": protocol_object(shots=shots, pointer_angle=pointer_angle),
        "circuits": circuits,
        "execution_spans": spans,
        "shot_rows": shot_rows,
        "missingness": {
            "circuits_submitted": len(specs),
            "shots_requested": requested,
            "shots_returned": returned,
            "all_requested_shots_returned": requested == returned,
            "provider_discard_count_known": synthetic,
            "provider_declared_discarded_shots": 0 if synthetic else None,
            "invalid_attempt_rows_exposed": synthetic,
            "filtering_policy": (
                "No simulator filtering."
                if synthetic
                else (
                    "Provider result boundary only; hidden provider-side "
                    "selection is outside the observed packet."
                )
            ),
        },
        "reset_scope": reset_scope(specs, hardware=not synthetic),
        "attachments": [
            {
                "attachment_id": "circuit-manifest",
                "path": "embedded://circuit-manifest",
                "media_type": "application/json",
                "sha256": circuit_digest,
            },
            {
                "attachment_id": "raw-register-rows",
                "path": "embedded://shot-rows",
                "media_type": "application/json",
                "sha256": raw_digest,
            },
            {
                "attachment_id": "backend-properties",
                "path": "embedded://backend-properties",
                "media_type": "application/json",
                "sha256": backend_digest,
            },
        ],
    }
    return capture


def validate_capture(capture: Any) -> list[str]:
    """Return exact refusal codes for provider-capture structural defects."""

    codes = exact_keyset(capture, TOP_REQUIRED, "TOP")
    if codes:
        return codes
    if capture["schema_version"] != SCHEMA_VERSION:
        codes.append("SCHEMA_VERSION_UNSUPPORTED")
    if capture["evidence_kind"] not in {
        "hardware_provider_capture",
        "synthetic_provider_control",
    }:
        codes.append("EVIDENCE_KIND_INVALID")

    codes.extend(exact_keyset(capture["provider"], PROVIDER_REQUIRED, "PROVIDER"))
    codes.extend(exact_keyset(capture["freeze"], FREEZE_REQUIRED, "FREEZE"))
    codes.extend(exact_keyset(capture["protocol"], PROTOCOL_REQUIRED, "PROTOCOL"))
    codes.extend(
        exact_keyset(capture["missingness"], MISSING_REQUIRED, "MISSINGNESS")
    )
    codes.extend(exact_keyset(capture["reset_scope"], RESET_REQUIRED, "RESET"))
    if codes:
        return sorted(set(codes))

    provider = capture["provider"]
    freeze = capture["freeze"]
    protocol = capture["protocol"]
    missingness = capture["missingness"]
    reset = capture["reset_scope"]

    for field in ("backend_properties_sha256",):
        value = provider.get(field)
        if (
            not isinstance(value, str)
            or len(value) != 64
            or any(char not in "0123456789abcdef" for char in value)
        ):
            codes.append(f"PROVIDER_{field.upper()}_INVALID")

    if freeze["protocol_id"] != protocol["protocol_id"]:
        codes.append("PROTOCOL_ID_JOIN_BROKEN")
    if protocol["protocol_id"] != PROTOCOL_ID:
        codes.append("PROTOCOL_ID_UNSUPPORTED")
    if protocol["shots_per_circuit"] < 1:
        codes.append("SHOTS_PER_CIRCUIT_INVALID")
    if protocol["system_qubit_count"] != 3:
        codes.append("QUBIT_COUNT_INVALID")
    if protocol["register_roles"] != {
        "pointer": "candidate_record",
        "environment": "formed_completion",
        "reset_witness": "causal_break_verification",
        "output": "held_out_binary_response",
    }:
        codes.append("REGISTER_ROLE_REFIT")
    if protocol["candidate_record"] != "pointer":
        codes.append("CANDIDATE_RECORD_REFIT")
    if protocol["completion_records"] != ["environment"]:
        codes.append("COMPLETION_RECORD_REFIT")
    if protocol["intervention_ids"] != [
        "identity_z",
        "flip_z",
        "causal_break_identity_z",
    ]:
        codes.append("INTERVENTION_SET_REFIT")
    if protocol["circuit_order_seed"] != CIRCUIT_ORDER_SEED:
        codes.append("CIRCUIT_ORDER_SEED_REFIT")
    if protocol["predeclared_expected_branch"] != (
        "TOLERANCE_BOUNDED_REFINED_RECONSTRUCTION"
    ):
        codes.append("EXPECTED_BRANCH_REFIT")

    circuits = capture["circuits"]
    if not isinstance(circuits, list) or not circuits:
        codes.append("CIRCUITS_EMPTY")
        return sorted(set(codes))

    circuit_ids: set[str] = set()
    circuit_by_id: dict[str, dict[str, Any]] = {}
    for circuit in circuits:
        row_codes = exact_keyset(circuit, CIRCUIT_REQUIRED, "CIRCUIT")
        codes.extend(row_codes)
        if row_codes:
            continue
        circuit_id = circuit["circuit_id"]
        if circuit_id in circuit_ids:
            codes.append("CIRCUIT_ID_DUPLICATE")
        circuit_ids.add(circuit_id)
        circuit_by_id[circuit_id] = circuit
        if circuit["register_map"] != REGISTER_WIDTHS:
            codes.append("CIRCUIT_REGISTER_MAP_INVALID")
        for digest_field in ("source_qpy_sha256", "transpiled_qpy_sha256"):
            digest = circuit[digest_field]
            if (
                not isinstance(digest, str)
                or len(digest) != 64
                or any(char not in "0123456789abcdef" for char in digest)
            ):
                codes.append(f"CIRCUIT_{digest_field.upper()}_INVALID")
        if circuit["expected_shots"] != protocol["shots_per_circuit"]:
            codes.append("CIRCUIT_SHOT_CONTRACT_MISMATCH")

    indices = sorted(
        circuit["circuit_index"]
        for circuit in circuits
        if isinstance(circuit, dict) and "circuit_index" in circuit
    )
    if indices != list(range(len(circuits))):
        codes.append("CIRCUIT_INDEX_NOT_CONTIGUOUS")

    ordered_circuits = sorted(
        (
            circuit
            for circuit in circuits
            if isinstance(circuit, dict)
            and not exact_keyset(circuit, CIRCUIT_REQUIRED, "CIRCUIT")
        ),
        key=lambda circuit: circuit["circuit_index"],
    )
    expected_specs = build_circuit_specs()
    observed_semantics = [
        {
            key: circuit[key]
            for key in (
                "circuit_id",
                "role",
                "history_id",
                "intervention_id",
                "analysis_role",
                "preparation_id",
                "causal_break",
                "calibration_target",
                "calibration_prepared_value",
            )
        }
        for circuit in ordered_circuits
    ]
    if observed_semantics != [spec.to_dict() for spec in expected_specs]:
        codes.append("CIRCUIT_SEMANTIC_MANIFEST_REFIT")
    reconstructed_manifest = {
        "protocol_id": protocol["protocol_id"],
        "shots_per_circuit": protocol["shots_per_circuit"],
        "qnd_pointer_angle_radians": protocol["qnd_pointer_angle_radians"],
        "circuit_order_seed": protocol["circuit_order_seed"],
        "circuits": observed_semantics,
    }
    if sha256_json(reconstructed_manifest) != freeze["circuit_manifest_sha256"]:
        codes.append("FROZEN_CIRCUIT_MANIFEST_HASH_MISMATCH")

    spans = capture["execution_spans"]
    if not isinstance(spans, list) or not spans:
        codes.append("EXECUTION_SPANS_EMPTY")
        span_ids: set[str] = set()
        spans = []
    else:
        span_ids = set()
        for span in spans:
            row_codes = exact_keyset(span, SPAN_REQUIRED, "SPAN")
            codes.extend(row_codes)
            if row_codes:
                continue
            if span["span_id"] in span_ids:
                codes.append("SPAN_ID_DUPLICATE")
            span_ids.add(span["span_id"])
            start = parse_timestamp(span["start"])
            stop = parse_timestamp(span["stop"])
            if start is None or stop is None:
                codes.append("SPAN_TIMESTAMP_INVALID")
            elif stop < start:
                codes.append("SPAN_NEGATIVE_DURATION")

    shot_rows = capture["shot_rows"]
    if not isinstance(shot_rows, list) or not shot_rows:
        codes.append("SHOT_ROWS_EMPTY")
        shot_rows = []

    seen_shots: set[tuple[str, int]] = set()
    shot_counts: dict[str, int] = {circuit_id: 0 for circuit_id in circuit_ids}
    for shot in shot_rows:
        row_codes = exact_keyset(shot, SHOT_REQUIRED, "SHOT")
        codes.extend(row_codes)
        if row_codes:
            continue
        circuit_id = shot["circuit_id"]
        if circuit_id not in circuit_by_id:
            codes.append("SHOT_CIRCUIT_JOIN_BROKEN")
            continue
        circuit = circuit_by_id[circuit_id]
        if shot["circuit_index"] != circuit["circuit_index"]:
            codes.append("SHOT_CIRCUIT_INDEX_JOIN_BROKEN")
        key = (circuit_id, shot["shot_index"])
        if key in seen_shots:
            codes.append("SHOT_ID_DUPLICATE")
        seen_shots.add(key)
        shot_counts[circuit_id] += 1
        if shot["span_id"] not in span_ids:
            codes.append("SHOT_SPAN_JOIN_BROKEN")
        registers = shot["registers"]
        if not isinstance(registers, dict) or set(registers) != set(REGISTER_WIDTHS):
            codes.append("SHOT_REGISTER_SET_INVALID")
            continue
        for register, width in REGISTER_WIDTHS.items():
            bits = registers[register]
            if (
                not isinstance(bits, list)
                or len(bits) != width
                or any(bit not in (0, 1) for bit in bits)
            ):
                codes.append(f"SHOT_REGISTER_{register.upper()}_INVALID")
        if sha256_json(registers) != shot["raw_register_sha256"]:
            codes.append("SHOT_RAW_HASH_MISMATCH")
        if shot["provider_valid"] and shot["provider_rejection_reason"] is not None:
            codes.append("VALID_SHOT_HAS_REJECTION_REASON")
        if (
            not shot["provider_valid"]
            and not isinstance(shot["provider_rejection_reason"], str)
        ):
            codes.append("INVALID_SHOT_MISSING_REJECTION_REASON")

    expected_each = protocol["shots_per_circuit"]
    if any(count != expected_each for count in shot_counts.values()):
        codes.append("CIRCUIT_RETURNED_SHOT_COUNT_MISMATCH")
    for circuit_id in circuit_ids:
        observed_indices = sorted(
            shot["shot_index"]
            for shot in shot_rows
            if isinstance(shot, dict)
            and shot.get("circuit_id") == circuit_id
            and isinstance(shot.get("shot_index"), int)
        )
        if observed_indices != list(range(expected_each)):
            codes.append("SHOT_INDEX_NOT_CONTIGUOUS")
            break
    expected_total = len(circuits) * expected_each
    if missingness["circuits_submitted"] != len(circuits):
        codes.append("MISSINGNESS_CIRCUIT_COUNT_MISMATCH")
    if missingness["shots_requested"] != expected_total:
        codes.append("MISSINGNESS_REQUEST_COUNT_MISMATCH")
    if missingness["shots_returned"] != len(shot_rows):
        codes.append("MISSINGNESS_RETURN_COUNT_MISMATCH")
    if missingness["all_requested_shots_returned"] != (
        expected_total == len(shot_rows)
    ):
        codes.append("MISSINGNESS_COMPLETENESS_FLAG_FALSE")
    if missingness["provider_discard_count_known"]:
        discarded = missingness["provider_declared_discarded_shots"]
        if discarded is None:
            codes.append("KNOWN_DISCARD_COUNT_MISSING")
        elif len(shot_rows) + discarded != expected_total:
            codes.append("KNOWN_DISCARD_ACCOUNTING_MISMATCH")
    elif missingness["provider_declared_discarded_shots"] is not None:
        codes.append("UNKNOWN_DISCARD_COUNT_HAS_VALUE")

    if freeze["attempt_population_claim"] == "all_physical_triggers_visible":
        if (
            freeze["invalid_attempt_visibility"] != "all_invalid_attempts_joined"
            or not missingness["invalid_attempt_rows_exposed"]
            or not missingness["provider_discard_count_known"]
        ):
            codes.append("ALL_ATTEMPTS_CLAIM_UNSUPPORTED")

    calibration_targets = {
        (circuit["calibration_target"], circuit["calibration_prepared_value"])
        for circuit in circuits
        if circuit.get("role") == "readout_calibration"
    }
    required_calibrations = {
        (register, prepared)
        for register in ("pointer", "environment", "output")
        for prepared in (0, 1)
    }
    if calibration_targets != required_calibrations:
        codes.append("READOUT_CALIBRATION_COVERAGE_INCOMPLETE")

    reset_cal_targets = {
        circuit["calibration_target"]
        for circuit in circuits
        if circuit.get("role") == "reset_calibration"
    }
    if reset_cal_targets != {
        "reset_witness[0]",
        "reset_witness[1]",
        "reset_witness[2]",
    }:
        codes.append("RESET_CALIBRATION_COVERAGE_INCOMPLETE")

    causal_break_ids = {
        circuit["circuit_id"]
        for circuit in circuits
        if circuit.get("analysis_role") == "causal_break"
    }
    if set(reset["causal_break_circuit_ids"]) != causal_break_ids:
        codes.append("CAUSAL_BREAK_CIRCUIT_JOIN_BROKEN")
    if reset["witness_register"] != "reset_witness":
        codes.append("RESET_WITNESS_REGISTER_INVALID")

    attachments = capture["attachments"]
    if not isinstance(attachments, list):
        codes.append("ATTACHMENTS_NOT_ARRAY")
        attachments = []
    attachment_ids: set[str] = set()
    for attachment in attachments:
        if not isinstance(attachment, dict):
            codes.append("ATTACHMENT_NOT_OBJECT")
            continue
        required = {"attachment_id", "path", "media_type", "sha256"}
        if set(attachment) != required:
            codes.append("ATTACHMENT_FIELDS_INVALID")
            continue
        if attachment["attachment_id"] in attachment_ids:
            codes.append("ATTACHMENT_ID_DUPLICATE")
        attachment_ids.add(attachment["attachment_id"])
        digest = attachment["sha256"]
        if (
            not isinstance(digest, str)
            or len(digest) != 64
            or any(char not in "0123456789abcdef" for char in digest)
        ):
            codes.append("ATTACHMENT_HASH_INVALID")
    attachment_by_id = {
        attachment["attachment_id"]: attachment
        for attachment in attachments
        if isinstance(attachment, dict)
        and set(attachment)
        == {"attachment_id", "path", "media_type", "sha256"}
    }
    if set(attachment_by_id) != {
        "circuit-manifest",
        "raw-register-rows",
        "backend-properties",
    }:
        codes.append("ATTACHMENT_SET_INVALID")
    else:
        if attachment_by_id["circuit-manifest"]["sha256"] != sha256_json(circuits):
            codes.append("CIRCUIT_ATTACHMENT_HASH_MISMATCH")
        if attachment_by_id["raw-register-rows"]["sha256"] != sha256_json(
            shot_rows
        ):
            codes.append("SHOT_ATTACHMENT_HASH_MISMATCH")
        if (
            attachment_by_id["backend-properties"]["sha256"]
            != provider["backend_properties_sha256"]
        ):
            codes.append("BACKEND_ATTACHMENT_HASH_MISMATCH")

    freeze_time = parse_timestamp(freeze["frozen_at"])
    started_time = parse_timestamp(provider["started_at"])
    if freeze_time is None:
        codes.append("FREEZE_TIMESTAMP_INVALID")
    elif started_time is not None and freeze_time > started_time:
        codes.append("FREEZE_AFTER_ACQUISITION")
    span_start_times = [
        parse_timestamp(span.get("start"))
        for span in spans
        if isinstance(span, dict)
    ]
    span_start_times = [time for time in span_start_times if time is not None]
    if (
        freeze_time is not None
        and span_start_times
        and freeze_time > min(span_start_times)
    ):
        codes.append("FREEZE_AFTER_EXECUTION_SPAN")

    return sorted(set(codes))


def assess_capture(capture: Any) -> dict[str, Any]:
    """Classify structural readiness separately from scientific claim ceiling."""

    try:
        codes = validate_capture(capture)
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        # The semantic validator assumes schema-typed fields. An arbitrary
        # external JSON document must still fail closed instead of crashing
        # the CLI or being partially interpreted.
        codes = ["MALFORMED_PROVIDER_CAPTURE"]
    if codes:
        return {
            "structural_status": "INCOMPLETE_PROVIDER_CAPTURE",
            "claim_ceiling": "NO_SCIENTIFIC_ADJUDICATION",
            "du_packet_mapping_eligible": False,
            "physical_remainder_eligible": False,
            "refusal_codes": codes,
        }

    if capture["evidence_kind"] == "synthetic_provider_control":
        return {
            "structural_status": "PROVIDER_CAPTURE_READY",
            "claim_ceiling": "SYNTHETIC_CONTROL_ONLY",
            "du_packet_mapping_eligible": False,
            "physical_remainder_eligible": False,
            "refusal_codes": [],
        }

    freeze = capture["freeze"]
    missingness = capture["missingness"]
    reset = capture["reset_scope"]
    visibility_complete = (
        freeze["attempt_population_claim"] == "all_physical_triggers_visible"
        and freeze["invalid_attempt_visibility"] == "all_invalid_attempts_joined"
        and missingness["invalid_attempt_rows_exposed"]
        and missingness["provider_discard_count_known"]
    )

    if not visibility_complete:
        return {
            "structural_status": "PROVIDER_CAPTURE_READY",
            "claim_ceiling": "RETURNED_SHOT_CONDITIONAL_ONLY",
            "du_packet_mapping_eligible": False,
            "physical_remainder_eligible": False,
            "refusal_codes": ["PHYSICAL_ATTEMPT_POPULATION_NOT_VISIBLE"],
        }

    if (
        not reset["all_reset_required_memories_witnessed"]
        or reset["unobserved_provider_memory_present"]
    ):
        return {
            "structural_status": "PROVIDER_CAPTURE_READY",
            "claim_ceiling": "ALL_ATTEMPTS_OBSERVED_NO_REMAINDER",
            "du_packet_mapping_eligible": True,
            "physical_remainder_eligible": False,
            "refusal_codes": ["COMPLETE_MEMORY_RESET_NOT_WITNESSED"],
        }

    return {
        "structural_status": "PROVIDER_CAPTURE_READY",
        "claim_ceiling": "IMPLEMENTATION_COMPLETE_MAPPING_ELIGIBLE",
        "du_packet_mapping_eligible": True,
        "physical_remainder_eligible": True,
        "refusal_codes": [],
    }


def provider_info_for_simulator(*, shots: int) -> dict[str, Any]:
    try:
        import qiskit
        import qiskit_aer

        versions = {
            "qiskit": qiskit.__version__,
            "qiskit-aer": qiskit_aer.__version__,
        }
    except ImportError:
        versions = {"qiskit": "unavailable", "qiskit-aer": "unavailable"}
    backend_properties = {
        "backend": "aer_simulator",
        "seed": SIMULATOR_SEED,
        "scientific_status": "synthetic_contract_control",
    }
    return {
        "name": "Qiskit Aer",
        "interface": "qiskit.primitives.BackendSamplerV2",
        "client_versions": versions,
        "backend_id": "aer_simulator",
        "job_id": "synthetic-aer-fixed",
        "job_status": "DONE",
        "calibration_id": None,
        "created_at": SYNTHETIC_START,
        "started_at": SYNTHETIC_START,
        "ended_at": SYNTHETIC_STOP,
        "capture_created_at": SYNTHETIC_STOP,
        "execution_options": {
            "shots_per_circuit": shots,
            "init_qubits": True,
            "measurement_level": "classified",
            "error_mitigation": "none",
            "seed": SIMULATOR_SEED,
        },
        "backend_properties_sha256": sha256_json(backend_properties),
    }


def simulate_capture(*, shots: int, pointer_angle: float) -> dict[str, Any]:
    from qiskit import transpile
    from qiskit.primitives import BackendSamplerV2
    from qiskit_aer import AerSimulator

    specs = build_circuit_specs()
    source_circuits = build_qiskit_circuits(specs, pointer_angle=pointer_angle)
    backend = AerSimulator(seed_simulator=SIMULATOR_SEED)
    transpiled = transpile(
        source_circuits,
        backend=backend,
        optimization_level=1,
        seed_transpiler=SIMULATOR_SEED,
    )
    sampler = BackendSamplerV2(
        backend=backend,
        options={
            "default_shots": shots,
            "seed_simulator": SIMULATOR_SEED,
        },
    )
    result = sampler.run(transpiled, shots=shots).result()
    return sampler_capture(
        specs=specs,
        source_circuits=source_circuits,
        transpiled_circuits=transpiled,
        result=result,
        shots=shots,
        pointer_angle=pointer_angle,
        provider_info=provider_info_for_simulator(shots=shots),
        synthetic=True,
    )


def hardware_capture(
    *,
    backend_name: str,
    shots: int,
    pointer_angle: float,
    authorization_id: str,
    expected_authorization_id: str | None = None,
) -> dict[str, Any]:
    """Submit one guarded IBM Quantum job and return its provider capture."""

    expected_authorization_id = expected_authorization_id or os.environ.get(
        "DU_IBM_EXPECTED_AUTHORIZATION_ID",
        "",
    )
    if (
        len(authorization_id) < MINIMUM_AUTHORIZATION_ID_LENGTH
        or len(expected_authorization_id) < MINIMUM_AUTHORIZATION_ID_LENGTH
        or not hmac.compare_digest(authorization_id, expected_authorization_id)
    ):
        raise PermissionError(
            "Hardware submission refused: a run-specific direct-chat "
            "authorization ID must be supplied separately and match "
            "DU_IBM_EXPECTED_AUTHORIZATION_ID."
        )

    # This timestamp freezes the semantic circuit manifest and analysis
    # contract before the provider job exists. Provider-created timestamps are
    # evidence about execution, not a substitute for preregistration.
    contract_frozen_at = utc_now()

    from qiskit import __version__ as qiskit_version
    from qiskit.transpiler import generate_preset_pass_manager
    from qiskit_ibm_runtime import (
        QiskitRuntimeService,
        SamplerV2,
        __version__ as runtime_version,
    )

    service = QiskitRuntimeService()
    backend = service.backend(backend_name)
    if not getattr(backend.status(), "operational", False):
        raise RuntimeError(f"backend {backend_name} is not operational")
    supported = set(getattr(getattr(backend, "target", None), "operation_names", []))
    supported.update(getattr(backend, "supported_instructions", []))
    if not {"measure", "reset"}.issubset(supported):
        raise RuntimeError(
            f"backend {backend_name} does not expose the required mid-circuit "
            "measurement/reset instructions"
        )

    specs = build_circuit_specs()
    source_circuits = build_qiskit_circuits(specs, pointer_angle=pointer_angle)
    pass_manager = generate_preset_pass_manager(
        backend=backend,
        optimization_level=1,
        seed_transpiler=CIRCUIT_ORDER_SEED,
    )
    transpiled = pass_manager.run(source_circuits)

    sampler = SamplerV2(mode=backend)
    sampler.options.execution.init_qubits = True
    sampler.options.execution.meas_type = "classified"
    job = sampler.run(transpiled, shots=shots)
    result = job.result()

    metrics = job.metrics() or {}
    timestamps = metrics.get("timestamps", {}) if isinstance(metrics, dict) else {}
    properties = job.properties()
    if hasattr(properties, "to_dict"):
        properties_data = properties.to_dict()
    else:
        properties_data = {"available": properties is not None}

    provider_info = {
        "name": "IBM Quantum",
        "interface": "qiskit_ibm_runtime.SamplerV2",
        "client_versions": {
            "qiskit": qiskit_version,
            "qiskit-ibm-runtime": runtime_version,
        },
        "backend_id": backend.name,
        "job_id": job.job_id(),
        "job_status": str(job.status()),
        "calibration_id": getattr(backend, "calibration_id", None),
        "created_at": _timestamp_text(timestamps.get("created")),
        "started_at": _timestamp_text(timestamps.get("running")),
        "ended_at": _timestamp_text(timestamps.get("finished")),
        "capture_created_at": utc_now(),
        "execution_options": {
            "shots_per_circuit": shots,
            "init_qubits": True,
            "measurement_level": "classified",
            "error_mitigation": "none_requested",
            "seed": None,
        },
        "backend_properties_sha256": sha256_json(properties_data),
    }
    return sampler_capture(
        specs=specs,
        source_circuits=source_circuits,
        transpiled_circuits=transpiled,
        result=result,
        shots=shots,
        pointer_angle=pointer_angle,
        provider_info=provider_info,
        synthetic=False,
        frozen_at=contract_frozen_at,
    )


def _timestamp_text(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat()
    return str(value)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        json.dumps(value, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    )


def plan_payload(*, shots: int, pointer_angle: float) -> dict[str, Any]:
    specs = build_circuit_specs()
    manifest = semantic_manifest(specs, shots=shots, pointer_angle=pointer_angle)
    return {
        "run_id": RUN_ID,
        "protocol": protocol_object(shots=shots, pointer_angle=pointer_angle),
        "semantic_manifest": manifest,
        "semantic_manifest_sha256": sha256_json(manifest),
        "circuit_count": len(specs),
        "requested_shots": len(specs) * shots,
        "external_action": (
            "NOT_PERFORMED: plan construction is local; submit requires exact "
            "Joe-direct-chat authorization."
        ),
    }


def cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan = subparsers.add_parser("plan", help="Print the frozen local plan.")
    plan.add_argument("--shots", type=int, default=2048)
    plan.add_argument("--pointer-angle", type=float, default=DEFAULT_POINTER_ANGLE)
    plan.add_argument("--output", type=Path)

    simulate = subparsers.add_parser(
        "simulate",
        help="Run the circuit lineage locally; never physical evidence.",
    )
    simulate.add_argument("--shots", type=int, default=128)
    simulate.add_argument(
        "--pointer-angle",
        type=float,
        default=DEFAULT_POINTER_ANGLE,
    )
    simulate.add_argument("--output", type=Path, required=True)

    assess = subparsers.add_parser(
        "assess",
        help="Validate and classify an existing provider capture.",
    )
    assess.add_argument("--capture", type=Path, required=True)

    submit = subparsers.add_parser(
        "submit",
        help="Submit one externally authorized IBM Quantum job.",
    )
    submit.add_argument("--backend", required=True)
    submit.add_argument("--shots", type=int, default=2048)
    submit.add_argument(
        "--pointer-angle",
        type=float,
        default=DEFAULT_POINTER_ANGLE,
    )
    submit.add_argument("--output", type=Path, required=True)
    submit.add_argument(
        "--authorization-id",
        default="",
    )

    args = parser.parse_args(argv)
    if getattr(args, "shots", 1) < 1:
        parser.error("--shots must be positive")
    if hasattr(args, "pointer_angle") and not (
        0 < args.pointer_angle < math.pi
    ):
        parser.error("--pointer-angle must lie strictly between 0 and pi")

    if args.command == "plan":
        payload = plan_payload(
            shots=args.shots,
            pointer_angle=args.pointer_angle,
        )
        if args.output:
            write_json(args.output, payload)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    if args.command == "simulate":
        capture = simulate_capture(
            shots=args.shots,
            pointer_angle=args.pointer_angle,
        )
        write_json(args.output, capture)
        print(json.dumps(assess_capture(capture), indent=2, sort_keys=True))
        return 0

    if args.command == "assess":
        capture = json.loads(args.capture.read_text(encoding="utf-8"))
        assessment = assess_capture(capture)
        print(json.dumps(assessment, indent=2, sort_keys=True))
        return 0 if not assessment["refusal_codes"] else 2

    if args.command == "submit":
        capture = hardware_capture(
            backend_name=args.backend,
            shots=args.shots,
            pointer_angle=args.pointer_angle,
            authorization_id=args.authorization_id,
        )
        write_json(args.output, capture)
        print(json.dumps(assess_capture(capture), indent=2, sort_keys=True))
        return 0

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(cli())
    except PermissionError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(3) from exc
