#!/usr/bin/env python3
"""Deterministic four-table screen of public physical evidence candidates.

This is an evidence-routing probe, not a scientific analysis of the source
experiments.  Its inputs are frozen, source-cited observations from a bounded
public screen.  A candidate is ingestible only when every required table is
explicitly available at the needed granularity; inference from a paper figure,
aggregate probability, or reconstructed model is forbidden.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_public_physical_evidence_screen_result.json"
)

GATE_FIELDS = (
    "trial_table",
    "calibration_table",
    "process_schema",
    "multitime_table",
)
ALLOWED = {"PASS", "PARTIAL", "FAIL", "UNAVAILABLE", "UNVERIFIED"}

CANDIDATES: tuple[dict[str, Any], ...] = (
    {
        "candidate_id": "xiang-2025-oqe-rb",
        "title": "Learning and forecasting open quantum dynamics with correlated noise",
        "publication_url": "https://www.nature.com/articles/s42005-025-01944-2",
        "public_packet_url": "https://github.com/guochu/pt_recovery",
        "source_observations": [
            "The paper identifies the GitHub repository as its experimental-data and code packet.",
            "Repository README blob 08acfaae30ca332a60f5b6fdc1b1cb1262482546 says experiment_data contains raw data and reconstructed process tensors.",
            "split_rb_data.jl blob 63875ce93997ce23fc7dc334e8754df2d994c5c3 reduces each public row to cl_ops plus aggregate p0, then creates train/test splits.",
            "two_qubit_model_rb_unitary.jl blob dd40e6b7e1ac4e1291578684afaa85de5f523f5a consumes those train/test pairs and fits an OQE model.",
        ],
        "trial_table": "PARTIAL",
        "trial_reason": (
            "Public sequence identity and aggregate p0 exist, but the inspected "
            "schema does not expose per-shot outcomes, rejection reasons, or "
            "calibration-block linkage."
        ),
        "calibration_table": "UNVERIFIED",
        "calibration_reason": (
            "No preparation/readout confusion model, joint uncertainty object, "
            "or controller-version join was located in the inspected packet."
        ),
        "process_schema": "PARTIAL",
        "process_reason": (
            "Code and reconstructed OQE/process-tensor objects exist, but the "
            "raw-row-to-complete-selective-map convention required by the DU "
            "gate is not present in the inspected schema."
        ),
        "multitime_table": "PARTIAL",
        "multitime_reason": (
            "Long gate sequences and held-out/future prediction exist; explicit "
            "repeat, reset, and causal-break rows are not exposed by the "
            "inspected schema."
        ),
        "routing_verdict": "PROMISING_PARTIAL_NOT_INGESTIBLE",
    },
    {
        "candidate_id": "white-2020-restricted-process-tensor",
        "title": "Demonstration of non-Markovian process characterisation and control on a quantum processor",
        "publication_url": "https://www.nature.com/articles/s41467-020-20113-3",
        "public_packet_url": None,
        "source_observations": [
            "The paper reconstructs four-time restricted process tensors on IBM Quantum devices.",
            "The paper states that available operations span only a unitary-control subspace, not a complete CP-map basis.",
            "Its Data availability and Code availability statements say materials are available from the corresponding author on reasonable request.",
        ],
        "trial_table": "UNAVAILABLE",
        "trial_reason": "No public row-level data packet; author request is external.",
        "calibration_table": "UNAVAILABLE",
        "calibration_reason": "No public calibration-linked packet.",
        "process_schema": "PARTIAL",
        "process_reason": (
            "The published process is explicitly restricted to the span of "
            "available unitary controls rather than a complete selective "
            "instrument."
        ),
        "multitime_table": "PARTIAL",
        "multitime_reason": (
            "Four-time experiments and out-of-basis predictions are reported, "
            "but no public reset/causal-break row table is available."
        ),
        "routing_verdict": "EXTERNAL_REQUEST_REQUIRED_NOT_INGESTIBLE",
    },
    {
        "candidate_id": "white-2022-process-tensor-tomography",
        "title": "Non-Markovian Quantum Process Tomography",
        "publication_url": "https://arxiv.org/abs/2106.11722",
        "public_packet_url": None,
        "source_observations": [
            "The paper supplies full process-tensor-tomography requirements, maximum-likelihood reconstruction, and positive causal projection.",
            "It reports IBM Quantum validation and multi-time predictive control.",
            "The bounded public screen did not locate a linked row-level experimental and calibration packet.",
        ],
        "trial_table": "UNVERIFIED",
        "trial_reason": "No public row-level packet was located in the bounded screen.",
        "calibration_table": "UNVERIFIED",
        "calibration_reason": "No calibration join was located in the bounded screen.",
        "process_schema": "PASS",
        "process_reason": (
            "The publication gives the needed complete process-tensor schema "
            "and physicality constraints at method level."
        ),
        "multitime_table": "PARTIAL",
        "multitime_reason": (
            "Multi-time reconstruction and validation are reported, but a "
            "public repeat/reset/held-out row table was not located."
        ),
        "routing_verdict": "METHOD_REFERENCE_NO_INGESTIBLE_PUBLIC_PACKET",
    },
    {
        "candidate_id": "stricker-2022-trapped-ion-instrument",
        "title": "Experimental single-qubit quantum process instrument",
        "publication_url": "https://doi.org/10.1103/PRXQuantum.3.030318",
        "public_packet_url": "https://doi.org/10.5281/zenodo.6901982",
        "source_observations": [
            "The published platform implements a real trapped-ion quantum instrument.",
            "The linked Zenodo record is figure-source data rather than a trial-, calibration-, controller-, provenance-, and multitime-resolved packet.",
        ],
        "trial_table": "FAIL",
        "trial_reason": "Figure-source summaries are not trial rows.",
        "calibration_table": "FAIL",
        "calibration_reason": "The public packet lacks the required calibration join.",
        "process_schema": "PARTIAL",
        "process_reason": (
            "The publication identifies an instrument, but the linked packet "
            "does not expose complete selective maps with uncertainty and a "
            "row-to-map convention."
        ),
        "multitime_table": "FAIL",
        "multitime_reason": "The linked packet is not an ordered multitime assay.",
        "routing_verdict": "FIGURE_SOURCE_NOT_INGESTIBLE",
    },
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def candidate_score(candidate: dict[str, Any]) -> tuple[int, int, str]:
    weights = {
        "PASS": 4,
        "PARTIAL": 2,
        "UNVERIFIED": 1,
        "UNAVAILABLE": 0,
        "FAIL": 0,
    }
    statuses = [candidate[field] for field in GATE_FIELDS]
    public_packet_bonus = 2 if candidate["public_packet_url"] else 0
    return (
        sum(weights[status] for status in statuses) + public_packet_bonus,
        sum(status == "PASS" for status in statuses),
        candidate["candidate_id"],
    )


def run() -> dict[str, Any]:
    checks: dict[str, bool] = {}
    checks["candidate_ids_unique"] = len(
        {item["candidate_id"] for item in CANDIDATES}
    ) == len(CANDIDATES)
    checks["all_gate_values_typed"] = all(
        candidate[field] in ALLOWED
        for candidate in CANDIDATES
        for field in GATE_FIELDS
    )
    checks["all_observations_source_linked"] = all(
        candidate["publication_url"] and candidate["source_observations"]
        for candidate in CANDIDATES
    )

    ingestible = [
        candidate["candidate_id"]
        for candidate in CANDIDATES
        if all(candidate[field] == "PASS" for field in GATE_FIELDS)
    ]
    checks["no_false_ingestion"] = not ingestible
    ranked = sorted(CANDIDATES, key=candidate_score, reverse=True)
    checks["xiang_is_strongest_public_reopener"] = (
        ranked[0]["candidate_id"] == "xiang-2025-oqe-rb"
    )
    checks["xiang_not_promoted_from_aggregates"] = (
        CANDIDATES[0]["trial_table"] == "PARTIAL"
        and CANDIDATES[0]["routing_verdict"]
        == "PROMISING_PARTIAL_NOT_INGESTIBLE"
    )
    checks["author_request_not_treated_as_public"] = (
        CANDIDATES[1]["trial_table"] == "UNAVAILABLE"
        and CANDIDATES[1]["public_packet_url"] is None
    )
    checks["method_schema_not_treated_as_data"] = (
        CANDIDATES[2]["process_schema"] == "PASS"
        and CANDIDATES[2]["trial_table"] == "UNVERIFIED"
    )
    checks["figure_source_not_treated_as_trials"] = (
        CANDIDATES[3]["trial_table"] == "FAIL"
    )

    passed = sum(checks.values())
    if passed != len(checks):
        raise AssertionError(
            f"failed checks: {[name for name, ok in checks.items() if not ok]}"
        )

    payload = {
        "probe": "du_public_physical_evidence_screen_probe",
        "screen_date": "2026-07-25",
        "claim_grade": (
            "bounded public-evidence routing audit; no physical sufficiency "
            "or new-physics verdict"
        ),
        "gate": {
            "trial_table": (
                "trial/order, preparation, instrument outcome, output setting "
                "and result, validity/rejection, calibration block"
            ),
            "calibration_table": (
                "preparation model, readout confusion, joint uncertainty, "
                "controller/decoder version"
            ),
            "process_schema": (
                "selective-map convention, normalization, physicality "
                "projection, raw-row-to-map rule"
            ),
            "multitime_table": (
                "repeat index, reset or causal break, held-out continuation"
            ),
        },
        "ingestion_rule": "all four fields must be PASS",
        "ingestible_candidates": ingestible,
        "strongest_reopener": ranked[0]["candidate_id"],
        "ranking": [
            {
                "candidate_id": candidate["candidate_id"],
                "screen_score_not_scientific_priority": candidate_score(
                    candidate
                )[0],
                "routing_verdict": candidate["routing_verdict"],
            }
            for candidate in ranked
        ],
        "candidates": CANDIDATES,
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "screen_digest": hashlib.sha256(
            canonical_json(CANDIDATES).encode()
        ).hexdigest(),
        "next_action": (
            "Do not run a sufficiency verdict. Audit whether Xiang et al. have "
            "a public shot/calibration sidecar outside the inspected schema; "
            "otherwise design or locate a new four-table experiment."
        ),
        "limits": [
            "The screen is bounded and does not prove that unlocated files do not exist.",
            "Repository file schemas were inspected, but the large raw JSON was not reinterpreted beyond its public preprocessing code.",
            "No author was contacted and no external action was taken.",
            "A screen score is evidence readiness, not scientific merit.",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(payload, indent=2) + "\n")
    return payload


if __name__ == "__main__":
    result = run()
    print(
        json.dumps(
            {
                "verdict": "PASS",
                "checks": f"{result['checks_passed']}/{result['checks_total']}",
                "ingestible_candidates": result["ingestible_candidates"],
                "strongest_reopener": result["strongest_reopener"],
                "artifact": str(ARTIFACT.relative_to(ROOT)),
            },
            indent=2,
        )
    )
