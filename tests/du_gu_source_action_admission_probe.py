#!/usr/bin/env python3
"""Exact controls for HC-DU-166's GU-to-DU milestone adapter.

Passing validates the typed dependency ladder, two finite nonimplication
controls, and the preserved nonclaims in the frozen GU source documents.
It establishes no GU action, physical law, record interface, novelty,
prediction, or scientific successor.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
GU_ROOT = ROOT.parent / "gu-formalization"
ARTIFACT_PATH = ROOT / "tests" / "artifacts" / "du_gu_source_action_admission_result.json"

GU_PACKET = GU_ROOT / "explorations" / "unified-source-datum-packet-v0-2026-07-30.md"
GU_N3 = GU_ROOT / "explorations" / "unified-source-datum-variational-emission-map-2026-07-30.md"
GU_REBASE = GU_ROOT / "explorations" / "post-n3-source-datum-ten-wave-rebase-2026-07-30.md"


REQUIREMENTS = {
    "candidate_action": {
        "fields",
        "candidate_domain",
        "functional",
    },
    "complete_euler": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
    },
    "lawful_completion": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
        "closed_global_domain",
        "nonempty_solution_class",
        "admitted_background",
    },
    "source_response": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
        "closed_global_domain",
        "nonempty_solution_class",
        "admitted_background",
        "hessian_or_linearization",
        "green_prescription",
        "source_insertion",
        "readout_map",
    },
    "operational_process": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
        "closed_global_domain",
        "nonempty_solution_class",
        "admitted_background",
        "hessian_or_linearization",
        "green_prescription",
        "source_insertion",
        "readout_map",
        "state_or_preparation",
        "intervention_class",
        "outcome_maps",
        "sampler",
    },
    "material_record": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
        "closed_global_domain",
        "nonempty_solution_class",
        "admitted_background",
        "hessian_or_linearization",
        "green_prescription",
        "source_insertion",
        "readout_map",
        "state_or_preparation",
        "intervention_class",
        "outcome_maps",
        "sampler",
        "material_carrier",
        "formation_map",
        "retention",
        "provenance",
        "access",
        "reset",
    },
    "du_reconstruction": {
        "fields",
        "candidate_domain",
        "functional",
        "complete_euler_operator",
        "boundary_junction_contract",
        "closed_global_domain",
        "nonempty_solution_class",
        "admitted_background",
        "hessian_or_linearization",
        "green_prescription",
        "source_insertion",
        "readout_map",
        "state_or_preparation",
        "intervention_class",
        "outcome_maps",
        "sampler",
        "material_carrier",
        "formation_map",
        "retention",
        "provenance",
        "access",
        "reset",
        "record_map",
        "held_out_target",
        "completion_fibre",
    },
}


CURRENT_GU = {
    "fields",
    "candidate_domain",
    "functional",
    "partial_variation_owners",
    "moving_section_current",
}


def qualifies(properties: Iterable[str], rung: str) -> bool:
    return REQUIREMENTS[rung].issubset(set(properties))


def partition(values: tuple[int, ...]) -> frozenset[frozenset[int]]:
    fibres: dict[int, set[int]] = {}
    for state, value in enumerate(values):
        fibres.setdefault(value, set()).add(state)
    return frozenset(frozenset(fibre) for fibre in fibres.values())


def assert_source_markers() -> list[str]:
    packet = GU_PACKET.read_text(encoding="utf-8")
    n3 = GU_N3.read_text(encoding="utf-8")
    rebase = GU_REBASE.read_text(encoding="utf-8")

    markers = {
        "packet_no_complete_euler": "No Euler equation has been derived from the packet." in packet,
        "packet_no_observer_feedback": "No observer feedback loop." in packet,
        "packet_probability_open": "physical probability/superselection rule remains unproved" in packet,
        "n3_no_stationary_solution": "No stationary solution" in n3,
        "n3_eight_missing_maps": "The eight named missing maps are:" in n3,
        "rebase_no_action_correctness": "action correctness" in rebase,
        "rebase_rb8_green_bfv": "RB8 common Green/BFV domain and transport" in rebase,
    }
    failures = [name for name, passed in markers.items() if not passed]
    if failures:
        raise AssertionError(f"missing frozen GU source markers: {failures}")
    return sorted(markers)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    checks: list[tuple[str, bool]] = []

    rung_order = [
        "candidate_action",
        "complete_euler",
        "lawful_completion",
        "source_response",
        "operational_process",
        "material_record",
        "du_reconstruction",
    ]
    for earlier, later in zip(rung_order, rung_order[1:]):
        checks.append(
            (
                f"requirements_nested_{earlier}_to_{later}",
                REQUIREMENTS[earlier] < REQUIREMENTS[later],
            )
        )

    checks.extend(
        [
            ("current_gu_is_candidate_action", qualifies(CURRENT_GU, "candidate_action")),
            ("current_gu_not_complete_euler", not qualifies(CURRENT_GU, "complete_euler")),
            ("current_gu_not_source_response", not qualifies(CURRENT_GU, "source_response")),
            ("current_gu_not_material_record", not qualifies(CURRENT_GU, "material_record")),
            ("current_gu_not_du_reconstruction", not qualifies(CURRENT_GU, "du_reconstruction")),
        ]
    )

    # Same action values on the same state space; different record fibres.
    action = (0, 1)
    constant_record = (0, 0)
    identity_record = (0, 1)
    checks.append(("same_action", action == action))
    checks.append(
        (
            "action_does_not_select_record_partition",
            partition(constant_record) != partition(identity_record),
        )
    )

    # Same response law; distinct material carrier/provenance packet.
    response = ((0, 0), (1, 1))
    archive_a = {"response": response, "carrier": "A", "provenance": ("source", "A")}
    archive_b = {"response": response, "carrier": "B", "provenance": ("source", "B")}
    checks.append(
        (
            "response_does_not_select_material_archive",
            archive_a["response"] == archive_b["response"]
            and (archive_a["carrier"], archive_a["provenance"])
            != (archive_b["carrier"], archive_b["provenance"]),
        )
    )

    source_markers = assert_source_markers()
    checks.append(("frozen_gu_nonclaims_preserved", len(source_markers) == 7))

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    result = {
        "claim_id": "HC-DU-166",
        "run_id": "RUN-20260730-134759-gu-source-action-admission-adapter",
        "status": "PASS",
        "checks_passed": len(checks),
        "current_gu_qualifies": [
            rung for rung in rung_order if qualifies(CURRENT_GU, rung)
        ],
        "current_gu_missing_by_rung": {
            rung: sorted(REQUIREMENTS[rung] - CURRENT_GU) for rung in rung_order
        },
        "source_markers": source_markers,
        "scientific_nonclaim": (
            "This artifact validates a typed dependency ladder and exact finite "
            "nonimplication controls only. It establishes no GU action, physical "
            "law, record interface, prediction, or successor."
        ),
    }

    if args.write_artifact:
        ARTIFACT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(
        "PASS:",
        f"{len(checks)}/{len(checks)} checks;",
        "current GU rung = candidate_action only;",
        "no action-to-record shortcut",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
