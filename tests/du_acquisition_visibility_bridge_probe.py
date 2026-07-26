#!/usr/bin/env python3
"""Exact controls for the provider-capture bridge and visibility ceiling.

This probe does not run a quantum simulator or contact a provider. It checks:

1. the frozen 19-circuit provider-capture contract;
2. exact corruption refusals and claim-ceiling classifications; and
3. the finite acquisition-visibility factorization lemma.

The probability result is elementary conditional-probability algebra. Its
value here is a claim boundary: factorization on provider-returned shots does
not imply factorization on the complete attempted physical process.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "lab" / "acquisition" / "ibm_runtime_du_acquisition.py"
SCHEMA_PATH = (
    ROOT / "specs" / "physical-sufficiency-provider-capture-v0.1.schema.json"
)
ARTIFACT = (
    ROOT / "tests" / "artifacts" / "du_acquisition_visibility_bridge_result.json"
)
RUN_ID = "RUN-20260726-070222-hardware-acquisition-bridge"
SHOTS = 2


def load_bridge() -> Any:
    spec = importlib.util.spec_from_file_location("du_acquisition_bridge", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load acquisition bridge")
    module = importlib.util.module_from_spec(spec)
    # Dataclasses inspect sys.modules while decorating the imported class.
    import sys

    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BRIDGE = load_bridge()


def sha256_json(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("utf-8")
    ).hexdigest()


def stable_hash(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def make_valid_capture() -> dict[str, Any]:
    specs = BRIDGE.build_circuit_specs()
    circuits: list[dict[str, Any]] = []
    shot_rows: list[dict[str, Any]] = []
    span_id = "span-fixture"

    for circuit_index, spec in enumerate(specs):
        circuit = {
            **spec.to_dict(),
            "circuit_index": circuit_index,
            "register_map": copy.deepcopy(BRIDGE.REGISTER_WIDTHS),
            "source_qpy_sha256": stable_hash(f"source:{spec.circuit_id}"),
            "transpiled_qpy_sha256": stable_hash(
                f"transpiled:{spec.circuit_id}"
            ),
            "expected_shots": SHOTS,
        }
        circuits.append(circuit)
        for shot_index in range(SHOTS):
            registers = {
                "pointer": [(circuit_index + shot_index) % 2],
                "environment": [(circuit_index // 2 + shot_index) % 2],
                "reset_witness": [0, 0, 0],
                "output": [(circuit_index + 2 * shot_index) % 2],
            }
            shot_rows.append(
                {
                    "circuit_id": spec.circuit_id,
                    "circuit_index": circuit_index,
                    "shot_index": shot_index,
                    "span_id": span_id,
                    "registers": registers,
                    "provider_valid": True,
                    "provider_rejection_reason": None,
                    "raw_register_sha256": sha256_json(registers),
                }
            )

    backend_digest = stable_hash("synthetic-backend-properties")
    manifest = BRIDGE.semantic_manifest(
        specs,
        shots=SHOTS,
        pointer_angle=BRIDGE.DEFAULT_POINTER_ANGLE,
    )
    capture = {
        "schema_version": BRIDGE.SCHEMA_VERSION,
        "capture_id": "du-provider-contract-fixture",
        "evidence_kind": "synthetic_provider_control",
        "provider": {
            "name": "Deterministic contract fixture",
            "interface": "standard-library",
            "client_versions": {"python": "standard-library"},
            "backend_id": "fixture",
            "job_id": "fixture-no-job",
            "job_status": "DONE",
            "calibration_id": None,
            "created_at": BRIDGE.SYNTHETIC_START,
            "started_at": BRIDGE.SYNTHETIC_START,
            "ended_at": BRIDGE.SYNTHETIC_STOP,
            "capture_created_at": BRIDGE.SYNTHETIC_STOP,
            "execution_options": {
                "shots_per_circuit": SHOTS,
                "init_qubits": True,
                "measurement_level": "classified",
                "error_mitigation": "none",
                "seed": BRIDGE.SIMULATOR_SEED,
            },
            "backend_properties_sha256": backend_digest,
        },
        "freeze": {
            "frozen_at": BRIDGE.SYNTHETIC_START,
            "protocol_id": BRIDGE.PROTOCOL_ID,
            "circuit_manifest_sha256": sha256_json(manifest),
            "analysis_code_version": BRIDGE.ANALYSIS_CODE_VERSION,
            "attempt_population_claim": "all_physical_triggers_visible",
            "returned_shot_policy": "All fixture attempts are present.",
            "invalid_attempt_visibility": "all_invalid_attempts_joined",
            "holdout_policy": "Distinct frozen circuit identities.",
        },
        "protocol": BRIDGE.protocol_object(
            shots=SHOTS,
            pointer_angle=BRIDGE.DEFAULT_POINTER_ANGLE,
        ),
        "circuits": circuits,
        "execution_spans": [
            {
                "span_id": span_id,
                "start": BRIDGE.SYNTHETIC_START,
                "stop": BRIDGE.SYNTHETIC_STOP,
                "precision": "synthetic_fixed_window",
                "warrant": "Deterministic structural fixture only.",
            }
        ],
        "shot_rows": shot_rows,
        "missingness": {
            "circuits_submitted": len(circuits),
            "shots_requested": len(shot_rows),
            "shots_returned": len(shot_rows),
            "all_requested_shots_returned": True,
            "provider_discard_count_known": True,
            "provider_declared_discarded_shots": 0,
            "invalid_attempt_rows_exposed": True,
            "filtering_policy": "No filtering in the structural fixture.",
        },
        "reset_scope": BRIDGE.reset_scope(specs, hardware=False),
        "attachments": [],
    }
    capture["attachments"] = [
        {
            "attachment_id": "circuit-manifest",
            "path": "embedded://circuit-manifest",
            "media_type": "application/json",
            "sha256": sha256_json(circuits),
        },
        {
            "attachment_id": "raw-register-rows",
            "path": "embedded://shot-rows",
            "media_type": "application/json",
            "sha256": sha256_json(shot_rows),
        },
        {
            "attachment_id": "backend-properties",
            "path": "embedded://backend-properties",
            "media_type": "application/json",
            "sha256": backend_digest,
        },
    ]
    return capture


def as_hardware_returned_only(capture: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(capture)
    mutated["capture_id"] = "du-hardware-returned-only-fixture"
    mutated["evidence_kind"] = "hardware_provider_capture"
    mutated["provider"]["name"] = "Provider boundary fixture"
    mutated["freeze"][
        "attempt_population_claim"
    ] = "all_provider_returned_shots_visible"
    mutated["freeze"][
        "invalid_attempt_visibility"
    ] = "detectable_protocol_invalids_only"
    mutated["missingness"]["provider_discard_count_known"] = False
    mutated["missingness"]["provider_declared_discarded_shots"] = None
    mutated["missingness"]["invalid_attempt_rows_exposed"] = False
    mutated["missingness"][
        "filtering_policy"
    ] = "Only rows crossing the provider result boundary are visible."
    mutated["reset_scope"] = BRIDGE.reset_scope(
        BRIDGE.build_circuit_specs(),
        hardware=True,
    )
    return mutated


def as_all_attempts_visible(capture: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(capture)
    mutated["freeze"][
        "attempt_population_claim"
    ] = "all_physical_triggers_visible"
    mutated["freeze"]["invalid_attempt_visibility"] = "all_invalid_attempts_joined"
    mutated["missingness"]["provider_discard_count_known"] = True
    mutated["missingness"]["provider_declared_discarded_shots"] = 0
    mutated["missingness"]["invalid_attempt_rows_exposed"] = True
    mutated["missingness"][
        "filtering_policy"
    ] = "Every physical trigger and invalid-attempt row is joined."
    return mutated


Joint = tuple[Fraction, Fraction, Fraction, Fraction]


def integer_compositions(total: int, cells: int) -> Iterable[tuple[int, ...]]:
    if cells == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in integer_compositions(total - first, cells - 1):
            yield (first, *tail)


def finite_joint_kernels(denominator: int = 2) -> list[Joint]:
    return [
        tuple(Fraction(value, denominator) for value in counts)  # type: ignore[misc]
        for counts in integer_compositions(denominator, 4)
    ]


def cell(joint: Joint, selection: int, outcome: int) -> Fraction:
    return joint[selection * 2 + outcome]


def selection_probability(joint: Joint, selection: int) -> Fraction:
    return cell(joint, selection, 0) + cell(joint, selection, 1)


def full_joint_factors(left: Joint, right: Joint) -> bool:
    return left == right


def component_kernels_factor(left: Joint, right: Joint) -> bool:
    for selection in (0, 1):
        left_selection = selection_probability(left, selection)
        right_selection = selection_probability(right, selection)
        if left_selection != right_selection:
            return False
        if left_selection == 0:
            continue
        for outcome in (0, 1):
            if (
                cell(left, selection, outcome) / left_selection
                != cell(right, selection, outcome) / right_selection
            ):
                return False
    return True


def accepted_stratum_equal(left: Joint, right: Joint) -> bool:
    left_probability = selection_probability(left, 1)
    right_probability = selection_probability(right, 1)
    if left_probability == 0 or right_probability == 0:
        return False
    return all(
        cell(left, 1, outcome) / left_probability
        == cell(right, 1, outcome) / right_probability
        for outcome in (0, 1)
    )


class Receipt:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(self, check_id: str, passed: bool, detail: str) -> None:
        self.checks.append(
            {"check_id": check_id, "passed": bool(passed), "detail": detail}
        )

    def close(self) -> dict[str, Any]:
        passed = sum(check["passed"] for check in self.checks)
        return {
            "all_passed": passed == len(self.checks),
            "passed": passed,
            "total": len(self.checks),
            "checks": self.checks,
        }


def run() -> dict[str, Any]:
    receipt = Receipt()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    base = make_valid_capture()
    malformed = copy.deepcopy(base)
    malformed["protocol"]["shots_per_circuit"] = "two"
    malformed_assessment = BRIDGE.assess_capture(malformed)

    receipt.check(
        "schema_is_strict_draft_2020_12",
        schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
        and schema.get("additionalProperties") is False
        and set(schema.get("required", [])) == BRIDGE.TOP_REQUIRED
        and malformed_assessment["refusal_codes"]
        == ["MALFORMED_PROVIDER_CAPTURE"],
        "provider-capture root is strict; malformed external JSON fails closed",
    )
    receipt.check(
        "frozen_suite_has_all_roles",
        len(base["circuits"]) == 19
        and {
            circuit["analysis_role"] for circuit in base["circuits"]
        }
        == {"calibration", "training", "held_out", "causal_break"},
        "19 circuits cover calibration, training, held-out, and causal-break arms",
    )

    class FakeSpan:
        def __init__(
            self,
            start_second: int,
            masks: dict[int, list[bool]],
        ) -> None:
            self.start = datetime(
                2000, 1, 1, 0, 0, start_second, tzinfo=timezone.utc
            )
            self.stop = datetime(
                2000, 1, 1, 0, 0, start_second + 1, tzinfo=timezone.utc
            )
            self._masks = masks

        def mask(self, pub_index: int) -> list[bool]:
            return self._masks[pub_index]

    class FakeResult:
        def __init__(self, spans: list[FakeSpan]) -> None:
            self.metadata = {"execution": {"execution_spans": spans}}

    fake_spans = [
        FakeSpan(0, {0: [True, False], 1: [False, True]}),
        FakeSpan(1, {0: [False, True], 1: [True, False]}),
    ]
    span_rows, span_assignments, _, _ = BRIDGE.provider_time_window(
        FakeResult(fake_spans),
        synthetic=False,
        pub_shot_counts=[2, 2],
    )
    duplicate_span_refused = False
    try:
        BRIDGE.provider_time_window(
            FakeResult(
                [
                    FakeSpan(0, {0: [True], 1: [True]}),
                    FakeSpan(1, {0: [True], 1: [False]}),
                ]
            ),
            synthetic=False,
            pub_shot_counts=[1, 1],
        )
    except ValueError:
        duplicate_span_refused = True
    receipt.check(
        "provider_span_masks_join_exactly_once",
        len(span_rows) == 2
        and set(span_assignments) == {(0, 0), (0, 1), (1, 0), (1, 1)}
        and len(set(span_assignments.values())) == 2
        and duplicate_span_refused,
        "PUB/shot masks cover each returned row exactly once; overlap is refused",
    )
    receipt.check(
        "valid_structural_capture",
        BRIDGE.validate_capture(base) == [],
        f"codes={BRIDGE.validate_capture(base)}",
    )
    synthetic_assessment = BRIDGE.assess_capture(base)
    receipt.check(
        "synthetic_never_promotes",
        synthetic_assessment["claim_ceiling"] == "SYNTHETIC_CONTROL_ONLY"
        and not synthetic_assessment["du_packet_mapping_eligible"]
        and not synthetic_assessment["physical_remainder_eligible"],
        str(synthetic_assessment),
    )

    returned_only = as_hardware_returned_only(base)
    returned_assessment = BRIDGE.assess_capture(returned_only)
    receipt.check(
        "returned_shots_are_conditional_only",
        BRIDGE.validate_capture(returned_only) == []
        and returned_assessment["claim_ceiling"]
        == "RETURNED_SHOT_CONDITIONAL_ONLY"
        and returned_assessment["refusal_codes"]
        == ["PHYSICAL_ATTEMPT_POPULATION_NOT_VISIBLE"],
        str(returned_assessment),
    )

    all_attempts = as_all_attempts_visible(returned_only)
    all_attempt_assessment = BRIDGE.assess_capture(all_attempts)
    receipt.check(
        "complete_attempts_without_complete_reset_stop_remainder",
        BRIDGE.validate_capture(all_attempts) == []
        and all_attempt_assessment["claim_ceiling"]
        == "ALL_ATTEMPTS_OBSERVED_NO_REMAINDER"
        and all_attempt_assessment["du_packet_mapping_eligible"]
        and not all_attempt_assessment["physical_remainder_eligible"],
        str(all_attempt_assessment),
    )

    complete = copy.deepcopy(all_attempts)
    complete["reset_scope"]["all_reset_required_memories_witnessed"] = True
    complete["reset_scope"]["unobserved_provider_memory_present"] = False
    complete_assessment = BRIDGE.assess_capture(complete)
    receipt.check(
        "only_full_visibility_and_reset_reach_mapping_gate",
        BRIDGE.validate_capture(complete) == []
        and complete_assessment["claim_ceiling"]
        == "IMPLEMENTATION_COMPLETE_MAPPING_ELIGIBLE"
        and complete_assessment["physical_remainder_eligible"],
        str(complete_assessment),
    )

    broken_manifest = copy.deepcopy(base)
    broken_manifest["circuits"][0]["history_id"] = "refit-history"
    broken_manifest["attachments"][0]["sha256"] = sha256_json(
        broken_manifest["circuits"]
    )
    manifest_codes = BRIDGE.validate_capture(broken_manifest)
    receipt.check(
        "manifest_refit_refused",
        "CIRCUIT_SEMANTIC_MANIFEST_REFIT" in manifest_codes
        and "FROZEN_CIRCUIT_MANIFEST_HASH_MISMATCH" in manifest_codes,
        f"codes={manifest_codes}",
    )

    broken_row = copy.deepcopy(base)
    broken_row["shot_rows"][0]["registers"]["output"] = [1]
    row_codes = BRIDGE.validate_capture(broken_row)
    receipt.check(
        "raw_row_mutation_refused",
        "SHOT_RAW_HASH_MISMATCH" in row_codes
        and "SHOT_ATTACHMENT_HASH_MISMATCH" in row_codes,
        f"codes={row_codes}",
    )

    missing_shot = copy.deepcopy(base)
    missing_shot["shot_rows"].pop()
    missing_codes = BRIDGE.validate_capture(missing_shot)
    receipt.check(
        "missing_shot_refused",
        "CIRCUIT_RETURNED_SHOT_COUNT_MISMATCH" in missing_codes
        and "SHOT_INDEX_NOT_CONTIGUOUS" in missing_codes
        and "MISSINGNESS_RETURN_COUNT_MISMATCH" in missing_codes,
        f"codes={missing_codes}",
    )

    late_freeze = copy.deepcopy(base)
    late_freeze["freeze"]["frozen_at"] = "2000-01-01T00:00:02+00:00"
    late_codes = BRIDGE.validate_capture(late_freeze)
    receipt.check(
        "post_acquisition_freeze_refused",
        "FREEZE_AFTER_ACQUISITION" in late_codes
        and "FREEZE_AFTER_EXECUTION_SPAN" in late_codes,
        f"codes={late_codes}",
    )

    unauthorized_refused = False
    try:
        BRIDGE.hardware_capture(
            backend_name="never-contact-provider",
            shots=1,
            pointer_angle=BRIDGE.DEFAULT_POINTER_ANGLE,
            authorization_id="",
            expected_authorization_id="",
        )
    except PermissionError:
        unauthorized_refused = True
    receipt.check(
        "hardware_submission_is_guarded",
        unauthorized_refused,
        "empty authorization is refused before provider imports or calls",
    )

    kernels = finite_joint_kernels()
    pair_count = 0
    equivalence_holds = True
    for left in kernels:
        for right in kernels:
            pair_count += 1
            if full_joint_factors(left, right) != component_kernels_factor(
                left, right
            ):
                equivalence_holds = False
    receipt.check(
        "finite_visibility_factorization_equivalence",
        pair_count == 100 and equivalence_holds,
        (
            "all 100 denominator-two kernel pairs satisfy: full joint "
            "factorization iff selection and every supported stratum factor"
        ),
    )

    # Cell order is (S=0,Y=0), (S=0,Y=1), (S=1,Y=0), (S=1,Y=1).
    history_zero: Joint = (
        Fraction(1, 2),
        Fraction(0),
        Fraction(1, 2),
        Fraction(0),
    )
    history_one: Joint = (
        Fraction(0),
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(0),
    )
    counterexample_passes = (
        selection_probability(history_zero, 1)
        == selection_probability(history_one, 1)
        and accepted_stratum_equal(history_zero, history_one)
        and not full_joint_factors(history_zero, history_one)
        and not component_kernels_factor(history_zero, history_one)
    )
    receipt.check(
        "accepted_rows_plus_acceptance_rate_do_not_identify_full_process",
        counterexample_passes,
        (
            "same candidate record, acceptance probability, and accepted "
            "outcome; different rejected stratum and full attempted process"
        ),
    )

    final_receipt = receipt.close()
    return {
        "run_id": RUN_ID,
        "status": "PASS_HARDWARE_BRIDGE_READY" if final_receipt["all_passed"] else "FAIL",
        "north_star_outcome": "HARDWARE_BRIDGE_READY",
        "scientific_grade": (
            "EXACT ACQUISITION-VISIBILITY CLAIM CEILING PLUS HARDWARE-READY "
            "PROVIDER CONTRACT / NO HARDWARE RUN, PHYSICAL FACTORIZATION, "
            "REMAINDER, RECORD-FUNDAMENTALITY, OR NEW-PHYSICS VERDICT"
        ),
        "plain_english": (
            "A shot-resolved provider result can validate the circuit and "
            "returned-shot analysis path, but it cannot by itself certify the "
            "complete attempted physical process. Complete-process "
            "factorization additionally requires the selection mechanism and "
            "every supported selected and rejected response stratum to factor "
            "through the same candidate record."
        ),
        "factorization_lemma": {
            "statement": (
                "P(S,Y|h,a) factors through (R(h),a) iff P(S|h,a) and, for "
                "each supported s, P(Y|S=s,h,a) factor through (R(h),a)."
            ),
            "known_math_status": (
                "Finite conditional-probability decomposition; not claimed as "
                "a new statistics theorem."
            ),
            "finite_audit_denominator": 2,
            "finite_audit_kernel_pairs": pair_count,
        },
        "selection_counterexample": {
            "history_zero_joint_counts_over_two": [1, 0, 1, 0],
            "history_one_joint_counts_over_two": [0, 1, 1, 0],
            "cell_order": ["S0Y0", "S0Y1", "S1Y0", "S1Y1"],
            "same_acceptance_probability": True,
            "same_accepted_response": True,
            "different_rejected_response": True,
            "full_process_factors": False,
        },
        "claim_ceiling_controls": {
            "synthetic": synthetic_assessment,
            "provider_returned_only": returned_assessment,
            "all_attempts_incomplete_reset": all_attempt_assessment,
            "complete_mapping_gate": complete_assessment,
        },
        "hardware_suite": {
            "circuit_count": len(base["circuits"]),
            "shots_in_structural_fixture": len(base["shot_rows"]),
            "roles": sorted(
                {circuit["analysis_role"] for circuit in base["circuits"]}
            ),
            "external_job_submitted": False,
        },
        "schema": str(SCHEMA_PATH.relative_to(ROOT)),
        "schema_sha256": hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest(),
        "bridge_sha256": hashlib.sha256(MODULE_PATH.read_bytes()).hexdigest(),
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "remaining_physical_gate": (
            "Run the frozen suite only with direct authorization. Treat a "
            "standard provider result as returned-shot-conditional evidence. "
            "A physical-remainder claim additionally needs a platform contract "
            "that exposes every physical trigger, invalid/rejected attempt, "
            "selection reason, and every admitted retained-memory reset."
        ),
        "receipt": final_receipt,
    }


def main() -> None:
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
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
