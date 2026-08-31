#!/usr/bin/env python3
"""Exact controls for the Bell prescription/execution boundary.

This probe uses only the standard Pauli-frame algebra.  It does not validate
the Arenskoetter et al. experiment or infer an unreported physical feed-forward
operation.  It checks what follows from retaining, ignoring, actively
correcting, or terminally consuming a Bell-outcome correction label.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_bell_prescription_execution_result.json"

OBSERVABLES = ("X", "Y", "Z")
PAULIS = ("I", "X", "Y", "Z")

# Sign of P O P for Pauli P and traceless Pauli observable O.
CONJUGATION_SIGN = {
    "I": {"X": 1, "Y": 1, "Z": 1},
    "X": {"X": 1, "Y": -1, "Z": -1},
    "Y": {"X": -1, "Y": 1, "Z": -1},
    "Z": {"X": -1, "Y": -1, "Z": 1},
}


def conjugate_bloch(pauli: str, bloch: dict[str, int]) -> dict[str, int]:
    return {
        observable: CONJUGATION_SIGN[pauli][observable] * bloch[observable]
        for observable in OBSERVABLES
    }


def average_bloch(branches: list[dict[str, int]]) -> dict[str, float]:
    return {
        observable: sum(branch[observable] for branch in branches) / len(branches)
        for observable in OBSERVABLES
    }


def run() -> dict[str, object]:
    # A generic non-axis-aligned state keeps every Pauli component live.
    initial = {"X": 2, "Y": -3, "Z": 5}
    conditional = {pauli: conjugate_bloch(pauli, initial) for pauli in PAULIS}

    # If the Bell label is discarded, uniform Pauli branches erase every
    # traceless Bloch component: the unconditional target is maximally mixed.
    ignored = average_bloch(list(conditional.values()))
    assert ignored == {"X": 0.0, "Y": 0.0, "Z": 0.0}

    # If the label is consumed by an active Pauli correction, applying the same
    # Pauli twice restores the input branchwise (global phases are irrelevant).
    active_recovery = {
        pauli: conjugate_bloch(pauli, conditional[pauli]) for pauli in PAULIS
    }
    assert all(recovered == initial for recovered in active_recovery.values())

    # At a terminal Pauli measurement, hardware correction can be deferred:
    # measuring P O P on the uncorrected branch has the same expectation as
    # measuring O on the corrected state.  This requires consuming the label.
    terminal_rows = []
    for pauli in PAULIS:
        for observable in OBSERVABLES:
            branch_expectation = conditional[pauli][observable]
            frame_sign = CONJUGATION_SIGN[pauli][observable]
            recovered_expectation = frame_sign * branch_expectation
            assert recovered_expectation == initial[observable]
            terminal_rows.append(
                {
                    "branch": pauli,
                    "observable": observable,
                    "uncorrected_expectation": branch_expectation,
                    "frame_sign": frame_sign,
                    "recovered_expectation": recovered_expectation,
                }
            )

    # Hostile continuation: |0> has Z=+1.  The X branch has Z=-1 under a fixed
    # nonadaptive Z readout.  Classical sign correction can recover this
    # terminal statistic, but cannot restore a live target state for a later
    # arbitrary quantum continuation.
    hostile = {
        "input_z": 1,
        "x_branch_fixed_z_readout": CONJUGATION_SIGN["X"]["Z"],
        "x_branch_frame_corrected_terminal_z": (
            CONJUGATION_SIGN["X"]["Z"] * CONJUGATION_SIGN["X"]["Z"]
        ),
    }
    assert hostile["x_branch_fixed_z_readout"] == -1
    assert hostile["x_branch_frame_corrected_terminal_z"] == 1

    return {
        "source_scope": {
            "citation": "Arenskoetter et al., Phys. Rev. Research 6, 023061 (2024)",
            "doi": "10.1103/PhysRevResearch.6.023061",
            "source_claims_validated_by_probe": False,
            "manual_source_audit": {
                "formed_eight_outcome_bell_record": True,
                "outcome_conditioned_process_tomography": True,
                "correction_prescription_derived": True,
                "outcome_conditioned_physical_pauli_gate_reported": False,
                "arbitrary_downstream_adaptive_controller_reported": False,
            },
        },
        "pauli_conjugation_signs": CONJUGATION_SIGN,
        "generic_input_bloch": initial,
        "conditional_uncorrected_bloch": conditional,
        "ignored_record_average_bloch": ignored,
        "active_branchwise_recovery": active_recovery,
        "terminal_frame_rows": terminal_rows,
        "hostile_fixed_continuation": hostile,
        "typed_boundary": {
            "formed_record": "Bell outcome is physically acquired and retained for evaluation",
            "prescription": "outcome labels which Pauli would recover the input",
            "terminal_equivalence": "record-conditioned Pauli-frame interpretation recovers compatible terminal observables",
            "enacted_continuation": "a physical controller must consume the record to correct or adapt arbitrary later quantum operations",
        },
        "verdict": "PRESCRIPTION_AND_TERMINAL_EQUIVALENCE_DO_NOT_BY_THEMSELVES_ESTABLISH_ENACTED_ARBITRARY_CONTINUATION",
        "scientific_boundary": {
            "proves": [
                "discarding a uniform Bell label depolarizes the unconditional ideal target",
                "active branchwise Pauli correction exactly restores the ideal input",
                "record-conditioned terminal Pauli-frame interpretation is statistically equivalent",
                "fixed nonadaptive continuation can fail when the correction label is not consumed",
            ],
            "does_not_prove": [
                "validity of the source experiment",
                "that the source physically applied a Pauli correction",
                "selection of an observer or continuation algebra",
                "arbitrary downstream capability from a correction prescription alone",
                "new physics or ontology priority",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
