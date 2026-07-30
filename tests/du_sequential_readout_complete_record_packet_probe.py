#!/usr/bin/env python3
"""Exact controls for HC-DU-162.

Passing proves only the finite compression, archive-policy, lineage, and
approximate-reset boundaries declared for the source-pinned sequential-readout
packet. It does not establish the experimental facts, a complete physical
record, reconstruction, a remainder, a new law, or new physics.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_sequential_readout_complete_record_packet_result.json"
)

Trace = tuple[Fraction, ...]


def dot(left: Trace, right: Trace) -> Fraction:
    if len(left) != len(right):
        raise ValueError("trace and weight must have equal dimension")
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def classify(beta: Fraction) -> str:
    """Finite stand-in for membership in the calibrated decision region."""
    return "g" if beta >= 0 else "e"


def aggregate(attempts: Iterable[dict[str, object]]) -> dict[str, object]:
    attempts = tuple(attempts)
    label_counts = Counter(str(item["label"]) for item in attempts)
    paired = tuple(item for item in attempts if "repeat_label" in item)
    agreements = sum(
        item["label"] == item["repeat_label"]
        for item in paired
    )
    return {
        "label_counts": dict(sorted(label_counts.items())),
        "repeat_pairs": len(paired),
        "repeat_agreements": agreements,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    # Two distinct raw traces differ by a nonzero component in the kernel of
    # the calibrated linear statistic. The fourth sample is also completely
    # invisible to this particular weight.
    weight = (
        Fraction(1),
        Fraction(2),
        Fraction(-1),
        Fraction(0),
    )
    trace_left = (
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )
    kernel_delta = (
        Fraction(2),
        Fraction(-1),
        Fraction(0),
        Fraction(3),
    )
    trace_right = tuple(
        value + change
        for value, change in zip(trace_left, kernel_delta)
    )
    beta_left = dot(trace_left, weight)
    beta_right = dot(trace_right, weight)

    compression_twin = {
        "weight": [str(value) for value in weight],
        "trace_left": [str(value) for value in trace_left],
        "trace_right": [str(value) for value in trace_right],
        "kernel_delta": [str(value) for value in kernel_delta],
        "delta_is_nonzero": any(value != 0 for value in kernel_delta),
        "delta_is_in_weight_kernel": dot(kernel_delta, weight) == 0,
        "beta_left": str(beta_left),
        "beta_right": str(beta_right),
        "same_beta": beta_left == beta_right,
        "same_binary_label": classify(beta_left) == classify(beta_right),
    }

    # The full and streaming policies see the same attempt stream and return
    # the same summary. Only the full policy retains the lineage-bearing rows.
    attempts = (
        {
            "trial_id": "A-001",
            "preparation": "g",
            "trace": trace_left,
            "beta": beta_left,
            "label": "g",
            "repeat_label": "g",
        },
        {
            "trial_id": "A-002",
            "preparation": "e",
            "trace": tuple(-x for x in trace_left),
            "beta": -beta_left,
            "label": "e",
            "repeat_label": "e",
        },
        {
            "trial_id": "A-003",
            "preparation": "g",
            "trace": trace_right,
            "beta": beta_right,
            "label": "g",
            "repeat_label": "e",
        },
        {
            "trial_id": "A-004",
            "preparation": "e",
            "trace": tuple(-x for x in trace_right),
            "beta": -beta_right,
            "label": "e",
            "repeat_label": "e",
        },
    )
    full_archive = {
        "retained_attempts": attempts,
        "summary": aggregate(attempts),
    }
    streaming_archive = {
        "retained_attempts": (),
        "summary": aggregate(attempts),
    }
    archive_twin = {
        "same_declared_summary": (
            full_archive["summary"] == streaming_archive["summary"]
        ),
        "different_retained_lineage": (
            full_archive["retained_attempts"]
            != streaming_archive["retained_attempts"]
        ),
        "full_retained_attempt_count": len(full_archive["retained_attempts"]),
        "streaming_retained_attempt_count": len(
            streaming_archive["retained_attempts"]
        ),
        "summary": full_archive["summary"],
    }

    # Source-reported cross-errors make a binary label non-identifying for the
    # prepared history. These are reported empirical inputs, not derived here.
    excited_to_ground_label_error = Fraction(34, 1000)
    ground_to_excited_label_error = Fraction(16, 1000)
    lineage_ambiguity = {
        "p_label_g_given_prepared_e": str(
            excited_to_ground_label_error
        ),
        "p_label_g_given_prepared_g": str(
            1 - ground_to_excited_label_error
        ),
        "same_label_has_both_preparation_histories": (
            excited_to_ground_label_error > 0
            and 1 - ground_to_excited_label_error > 0
        ),
    }

    release_efficiency = Fraction(91, 100)
    qnd_agreement = Fraction(95, 100)
    reset_boundary = {
        "reported_release_efficiency": str(release_efficiency),
        "reported_release_inefficiency": str(1 - release_efficiency),
        "reported_qnd_agreement": str(qnd_agreement),
        "reported_qnd_mismatch": str(1 - qnd_agreement),
        "release_is_not_exact_blank": release_efficiency < 1,
        "qnd_repeat_is_not_exact": qnd_agreement < 1,
        "probe_reset_does_not_define_archive_reset": True,
    }

    packet_fields = {
        "blank_to_written_trace": "PHYSICALLY_REALIZED",
        "one_run_operational_outcome": "CALIBRATION_CONDITIONAL",
        "retained_archive": "USED_BUT_RETENTION_SEMANTICS_UNSELECTED",
        "causal_provenance": "NOT_IDENTIFIED",
        "observer_access": "PHYSICALLY_REALIZED_BUT_BOUNDARY_SUPPLIED",
        "reset": "APPROXIMATE_PROBE_RESET_ARCHIVE_RESET_UNSPECIFIED",
        "held_out_action": "NO_OUTCOME_CONDITIONED_PHYSICAL_ACTION",
    }
    complete_packet = all(
        value == "PHYSICALLY_REALIZED_AND_SELECTED"
        for value in packet_fields.values()
    )

    checks = {
        "nonzero_trace_kernel_witness": (
            compression_twin["delta_is_nonzero"]
            and compression_twin["delta_is_in_weight_kernel"]
        ),
        "distinct_traces_same_beta_and_label": (
            trace_left != trace_right
            and compression_twin["same_beta"]
            and compression_twin["same_binary_label"]
        ),
        "same_summary_different_archive_lineage": (
            archive_twin["same_declared_summary"]
            and archive_twin["different_retained_lineage"]
        ),
        "binary_label_does_not_identify_preparation_history": (
            lineage_ambiguity["same_label_has_both_preparation_histories"]
        ),
        "reported_reset_controls_are_approximate": (
            reset_boundary["release_is_not_exact_blank"]
            and reset_boundary["qnd_repeat_is_not_exact"]
        ),
        "complete_packet_not_earned": not complete_packet,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"complete-packet controls failed: {failed}")

    result = {
        "probe": "du_sequential_readout_complete_record_packet_probe",
        "status": "PASS",
        "claim_id": "HC-DU-162",
        "scope": "peronnin_sequential_readout_complete_packet_boundary",
        "source": {
            "title": "Sequential dispersive measurement of a superconducting qubit",
            "arxiv": "1904.04635",
            "journal": "Physical Review Letters 124, 180502 (2020)",
        },
        "compression_twin": compression_twin,
        "archive_twin": archive_twin,
        "lineage_ambiguity": lineage_ambiguity,
        "reset_boundary": reset_boundary,
        "packet_fields": packet_fields,
        "complete_packet": complete_packet,
        "checks": checks,
        "disclaimer": (
            "Passing establishes only finite logical controls around the "
            "source audit; it establishes no experimental fact, complete "
            "physical record, reconstruction, remainder, new law, or new "
            "physics."
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
