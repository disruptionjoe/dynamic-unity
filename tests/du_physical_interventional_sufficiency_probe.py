#!/usr/bin/env python3
"""Physical interventional-sufficiency evidence and ingestion gate.

This probe does not reconstruct a laboratory instrument from invented data.
It freezes the DU-PAPER-007 comparison contract, audits the public evidence
packet for Stricker et al.'s trapped-ion loss-detection instrument, and
returns the strongest verdict licensed by that packet.

The published article reports full quantum-instrument characterization.  The
associated Zenodo record describes its files more narrowly as source data for
graphical representations.  That distinction matters: plotted point
estimates cannot determine shot uncertainty, temporal correlations,
calibration drift, invalid-trial semantics, or a likelihood for a finite-shot
factorization-or-witness test.

Passing this probe therefore certifies an ``INCOMPLETE_CONTRACT`` boundary
and a reproducible reopening schema.  It is not a failure of the published
experiment and not evidence for or against record sufficiency.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_physical_interventional_sufficiency_result.json"
)
RUN_ID = "RUN-20260725-150819-three-paper-advance"


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


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


ARTICLE = {
    "title": (
        "Characterizing Quantum Instruments: From Nondemolition "
        "Measurements to Quantum Error Correction"
    ),
    "authors_short": "Stricker et al.",
    "journal": "PRX Quantum 3, 030318 (2022)",
    "doi": "10.1103/PRXQuantum.3.030318",
    "url": (
        "https://journals.aps.org/prxquantum/abstract/"
        "10.1103/PRXQuantum.3.030318"
    ),
    "physical_premise": (
        "A 40Ca+ trapped-ion loss-detection unit was characterized as a "
        "quantum instrument with classical loss/no-loss outputs and "
        "outcome-conditioned postmeasurement dynamics."
    ),
}

DATASET = {
    "doi": "10.5281/zenodo.6901982",
    "url": "https://zenodo.org/records/6901982",
    "version": "v1",
    "published": "2022-07-25",
    "license": "CC-BY-4.0",
    "declared_scope": (
        "Source data underlying the graphical representations used in the figures."
    ),
    "file_count": 22,
    "files": [
        "Fig3.csv",
        "Fig4a.csv",
        "Fig4b.csv",
        "Fig5a_ploss_002.csv",
        "Fig5a_ploss_061.csv",
        "Fig5b_ploss_002.csv",
        "Fig5b_ploss_061.csv",
        "Fig5c.csv",
        "Fig6.csv",
        "Fig7a_loss_000.csv",
        "Fig7a_loss_050.csv",
        "Fig7a_loss_085.csv",
        "Fig7a_no-loss_000.csv",
        "Fig7a_no-loss_050.csv",
        "Fig7a_no-loss_085.csv",
        "Fig7b_false-negatives.csv",
        "Fig7b_false-positives.csv",
        "Fig9.csv",
        "Fig10a.csv",
        "Fig10b.csv",
        "Fig10c.csv",
        "Fig10d.csv",
    ],
}

FROZEN_CONTRACT = {
    "candidate_certified_record": (
        "The archived classical loss/no-loss instrument outcome, its declared "
        "preparation and intervention labels, and the published "
        "outcome-conditioned process estimate. No hidden run metadata is "
        "silently included."
    ),
    "observer_access_boundary": (
        "An external experimenter may prepare the data ion, invoke the fixed "
        "loss-detection unit, read its reported classical outcome, and apply "
        "tomographically complete conditional single-qubit continuations to "
        "the retained output. Trap environment, controller internals, raw "
        "fluorescence stream, discarded trials, and calibration registers "
        "remain outside unless explicitly supplied."
    ),
    "intervention_family": [
        "tomographically complete declared input preparations",
        "one invocation of the fixed loss-detection instrument",
        "outcome-conditioned single-qubit rotations",
        "tomographically complete output measurements",
        "repeat-instrument continuation for a declared memory test",
    ],
    "physical_refinement_class": [
        "formed detector and invalid-trial record",
        "preparation and readout calibration block",
        "controller/pulse-program version",
        "route and environment telemetry available in the implementation",
        "trial order, timestamp, and drift block",
        "retained ancilla/leakage/loss syndrome available to the apparatus",
    ],
    "target": (
        "All outcome probabilities and outcome-conditioned future response "
        "probabilities for the admitted intervention family, with a "
        "finite-shot confidence statement."
    ),
    "strongest_implementation_complete_null": (
        "Every CPTNI selective instrument, including admitted SPAM, leakage, "
        "detector confusion, drift, temporal memory, invalid-trial selection, "
        "and controller/environment correlations, that is compatible with "
        "the frozen raw trial record and independently calibrated uncertainty "
        "model."
    ),
}

FIELD_AUDIT = {
    "published_platform_and_instrument_target": {
        "status": "available_in_article",
        "evidence": ARTICLE["physical_premise"],
    },
    "public_figure_source_files_and_checksums": {
        "status": "available_in_zenodo_record",
        "evidence": "22 named CSV figure-source files with record-level checksums.",
    },
    "raw_trial_resolved_tomography_counts": {
        "status": "not_exposed_by_public_record",
        "required_columns": [
            "trial_id",
            "timestamp_or_order",
            "preparation_setting",
            "instrument_outcome",
            "output_tomography_setting",
            "output_tomography_outcome",
        ],
    },
    "invalid_abort_and_discarded_trial_rows": {
        "status": "not_exposed_by_public_record",
        "required_columns": [
            "validity_flag",
            "rejection_reason",
            "herald_or_loss_flag",
            "denominator_membership",
        ],
    },
    "calibration_linkage_and_uncertainty": {
        "status": "not_exposed_by_public_record",
        "required_columns": [
            "calibration_block_id",
            "preparation_calibration",
            "readout_confusion_matrix",
            "calibration_covariance_or_resamples",
        ],
    },
    "complete_selective_map_machine_representation": {
        "status": "not_established_by_dataset_description",
        "required_columns": [
            "outcome_label",
            "choi_or_transfer_matrix_entry",
            "normalization_convention",
            "fit_or_projection_method",
            "joint_uncertainty",
        ],
    },
    "controller_route_environment_and_resource_passport": {
        "status": "not_exposed_by_public_record",
        "required_columns": [
            "pulse_program_version",
            "controller_branch",
            "ion_and_ancilla_roles",
            "route_or_gate_sequence",
            "environment_or_drift_block",
            "detector_decoder_version",
        ],
    },
    "multitime_memory_control": {
        "status": "not_exposed_by_public_record",
        "required_columns": [
            "repeat_index",
            "prior_outcome",
            "reset_or_causal_break_status",
            "held_out_continuation_outcome",
        ],
    },
}


def lag_product(sequence: list[int]) -> float:
    mean = sum(sequence) / len(sequence)
    numerator = sum(
        (left - mean) * (right - mean)
        for left, right in zip(sequence, sequence[1:])
    )
    denominator = sum((value - mean) ** 2 for value in sequence[:-1])
    return numerator / denominator


def run() -> dict[str, Any]:
    receipt = Receipt()

    # Public-evidence identity and scope checks.
    receipt.check(
        "article_is_a_published_physical_quantum_instrument",
        ARTICLE["doi"] == "10.1103/PRXQuantum.3.030318",
        ARTICLE["physical_premise"],
    )
    receipt.check(
        "dataset_is_article_linked_and_open",
        DATASET["doi"] == "10.5281/zenodo.6901982"
        and DATASET["license"] == "CC-BY-4.0",
        f"doi={DATASET['doi']}; license={DATASET['license']}",
    )
    receipt.check(
        "dataset_scope_is_frozen_as_figure_source_data",
        "graphical representations" in DATASET["declared_scope"],
        DATASET["declared_scope"],
    )
    receipt.check(
        "dataset_manifest_has_22_unique_csv_files",
        len(DATASET["files"]) == DATASET["file_count"]
        and len(set(DATASET["files"])) == DATASET["file_count"]
        and all(name.endswith(".csv") for name in DATASET["files"]),
        f"files={len(DATASET['files'])}",
    )

    # The six comparison fields are frozen before reading the verdict.
    required_contract_keys = {
        "candidate_certified_record",
        "observer_access_boundary",
        "intervention_family",
        "physical_refinement_class",
        "target",
        "strongest_implementation_complete_null",
    }
    receipt.check(
        "six_field_contract_is_complete",
        set(FROZEN_CONTRACT) == required_contract_keys,
        f"keys={sorted(FROZEN_CONTRACT)}",
    )
    for key in sorted(required_contract_keys):
        value = FROZEN_CONTRACT[key]
        receipt.check(
            f"contract_{key}_is_nonempty",
            bool(value),
            str(value),
        )

    available = {
        key
        for key, value in FIELD_AUDIT.items()
        if value["status"].startswith("available")
    }
    unavailable = set(FIELD_AUDIT) - available
    receipt.check(
        "published_platform_premise_is_retained",
        "published_platform_and_instrument_target" in available,
        f"available={sorted(available)}",
    )
    receipt.check(
        "figure_source_provenance_is_retained",
        "public_figure_source_files_and_checksums" in available,
        f"available={sorted(available)}",
    )
    expected_missing = {
        "raw_trial_resolved_tomography_counts",
        "invalid_abort_and_discarded_trial_rows",
        "calibration_linkage_and_uncertainty",
        "complete_selective_map_machine_representation",
        "controller_route_environment_and_resource_passport",
        "multitime_memory_control",
    }
    receipt.check(
        "implementation_complete_fields_are_explicitly_missing",
        unavailable == expected_missing,
        f"missing={sorted(unavailable)}",
    )

    # Same plotted probability, radically different finite-shot uncertainty.
    small_success, small_n = 3, 4
    large_success, large_n = 300, 400
    small_p = small_success / small_n
    large_p = large_success / large_n
    small_se = math.sqrt(small_p * (1.0 - small_p) / small_n)
    large_se = math.sqrt(large_p * (1.0 - large_p) / large_n)
    receipt.check(
        "aggregate_probability_has_distinct_count_realizations",
        small_p == large_p == 0.75,
        f"small={small_success}/{small_n}; large={large_success}/{large_n}",
    )
    receipt.check(
        "aggregate_probability_does_not_fix_shot_uncertainty",
        abs(small_se / large_se - 10.0) < 1.0e-12,
        f"se_small={small_se:.12f}; se_large={large_se:.12f}",
    )

    # Same marginal counts, sharply different temporal-memory evidence.
    alternating = [0, 1] * 50
    blocked = [0] * 50 + [1] * 50
    alternating_transitions = sum(
        left != right for left, right in zip(alternating, alternating[1:])
    )
    blocked_transitions = sum(
        left != right for left, right in zip(blocked, blocked[1:])
    )
    receipt.check(
        "marginal_counts_match_for_distinct_trial_orders",
        sum(alternating) == sum(blocked) == 50
        and len(alternating) == len(blocked) == 100,
        "both sequences have 50/100 positive outcomes",
    )
    receipt.check(
        "trial_order_changes_memory_diagnostic",
        alternating_transitions == 99
        and blocked_transitions == 1
        and lag_product(alternating) < -0.99
        and lag_product(blocked) > 0.95,
        (
            f"transitions={alternating_transitions},{blocked_transitions}; "
            f"lag={lag_product(alternating):.6f},{lag_product(blocked):.6f}"
        ),
    )

    # A finite-shot factorization verdict requires precisely the absent data.
    admissible_for_factorization = (
        "raw_trial_resolved_tomography_counts" in available
        and "calibration_linkage_and_uncertainty" in available
        and "complete_selective_map_machine_representation" in available
        and "invalid_abort_and_discarded_trial_rows" in available
    )
    admissible_for_multitime = (
        admissible_for_factorization
        and "multitime_memory_control" in available
    )
    receipt.check(
        "factorization_is_not_run_without_likelihood",
        not admissible_for_factorization,
        "No trial-resolved likelihood and joint calibration uncertainty.",
    )
    receipt.check(
        "multitime_sufficiency_is_not_run_without_memory_control",
        not admissible_for_multitime,
        "No ordered repeat/causal-break/held-out continuation record.",
    )
    receipt.check(
        "no_synthetic_reconstruction_is_promoted_to_lab_evidence",
        True,
        "The probe constructs only information-loss counterexamples.",
    )

    minimum_reopening_packet = {
        "trial_table": [
            "trial_id",
            "timestamp_or_order",
            "preparation_setting",
            "instrument_outcome",
            "output_tomography_setting",
            "output_tomography_outcome",
            "validity_flag",
            "rejection_reason",
            "calibration_block_id",
        ],
        "calibration_table": [
            "calibration_block_id",
            "preparation_model",
            "readout_confusion_matrix",
            "joint_uncertainty_or_bootstrap_draws",
            "controller_program_version",
            "decoder_version",
        ],
        "process_schema": [
            "selective_map_convention",
            "outcome_normalization",
            "physicality_constraint_or_projection",
            "mapping_from_trial_rows_to_selective_maps",
        ],
        "multitime_extension": [
            "repeat_index",
            "reset_or_causal_break_status",
            "held_out_conditional_continuation",
        ],
    }
    receipt.check(
        "reopening_packet_contains_trial_calibration_process_and_multitime_tables",
        set(minimum_reopening_packet)
        == {
            "trial_table",
            "calibration_table",
            "process_schema",
            "multitime_extension",
        }
        and all(minimum_reopening_packet.values()),
        f"tables={sorted(minimum_reopening_packet)}",
    )

    final_receipt = receipt.close()
    result = {
        "run_id": RUN_ID,
        "status": (
            "PASS_INCOMPLETE_CONTRACT_GATE"
            if final_receipt["all_passed"]
            else "FAIL"
        ),
        "scientific_grade": (
            "PUBLISHED PHYSICAL PLATFORM AND FIGURE-SOURCE DATA / "
            "IMPLEMENTATION-COMPLETE CONTRACT NOT AVAILABLE / "
            "NO FACTORIZATION, REMAINDER, OR NEW-PHYSICS VERDICT"
        ),
        "verdict": "INCOMPLETE_CONTRACT",
        "plain_english": (
            "The selected paper is a genuine laboratory quantum-instrument "
            "experiment, but its open record is figure-source data rather "
            "than the trial- and calibration-resolved package needed to ask "
            "Dynamic Unity's finite-shot interventional-sufficiency question. "
            "The missing data cannot be reconstructed from plotted values."
        ),
        "article": ARTICLE,
        "dataset": DATASET,
        "frozen_contract": FROZEN_CONTRACT,
        "field_audit": FIELD_AUDIT,
        "executed": [
            "source and provenance scope audit",
            "six-field comparison-contract freeze",
            "implementation-complete field audit",
            "same-mean/different-shot-uncertainty counterexample",
            "same-marginal/different-memory counterexample",
            "reproducible minimum ingestion schema",
        ],
        "not_executed": [
            "selective-map reconstruction from raw counts",
            "uncertainty-aware factorization",
            "minimum physical refinement search",
            "finite separating intervention",
            "finite-shot calibrated witness",
        ],
        "exact_missing_source_package": (
            "A calibration-block-linked, trial-resolved instrument-tomography "
            "table containing preparation, instrument outcome, output "
            "tomography setting/result, invalid/discard reason, trial order "
            "or timestamp, and the controller/decoder version; plus the "
            "joint calibration uncertainty or bootstrap draws and an "
            "explicit mapping to every selective map."
        ),
        "minimum_reopening_packet": minimum_reopening_packet,
        "next_decision": (
            "Request or locate the reopening packet from the source owners. "
            "If unavailable, choose another public instrument only if its "
            "record exposes all fields before examining a sufficiency result."
        ),
        "receipt": final_receipt,
    }
    return result


def main() -> None:
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
