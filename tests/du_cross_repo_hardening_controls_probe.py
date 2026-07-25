#!/usr/bin/env python3
"""Deterministic finite controls for the cross-repo hardening contract.

The fixtures recheck control shapes only.  They do not import sibling claim
grades, prove physical realizability, or promote a DU hypothesis.
"""

from __future__ import annotations

import hashlib
import json
from collections import deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "tests" / "artifacts" / "du_cross_repo_hardening_controls_result.json"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def reachability(vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]) -> dict[str, list[str]]:
    adjacency = {vertex: [] for vertex in vertices}
    for source, target in edges:
        adjacency[source].append(target)
    result: dict[str, list[str]] = {}
    for source in vertices:
        seen = {source}
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for target in adjacency[current]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        result[source] = sorted(seen)
    return result


def shortest_hops(
    source: str, target: str, edges: tuple[tuple[str, str], ...]
) -> int | None:
    adjacency: dict[str, list[str]] = {}
    for left, right in edges:
        adjacency.setdefault(left, []).append(right)
    queue = deque([(source, 0)])
    seen = {source}
    while queue:
        current, distance = queue.popleft()
        if current == target:
            return distance
        for successor in adjacency.get(current, []):
            if successor not in seen:
                seen.add(successor)
                queue.append((successor, distance + 1))
    return None


def capability_verdict(before: dict[str, Any], after: dict[str, Any]) -> str:
    frame_keys = (
        "system_count",
        "execution_time",
        "controls",
        "prior_information",
        "readout_access",
        "decoder",
        "error_budget",
        "resource_budget",
    )
    if any(before[key] != after[key] for key in frame_keys):
        return "FRAME_CHANGED"
    before_tasks = set(before["certified_tasks"])
    after_tasks = set(after["certified_tasks"])
    if before_tasks < after_tasks:
        return "CAPABILITY_INCREASE"
    if before_tasks == after_tasks:
        return "NO_STRICT_CAPABILITY_CHANGE"
    return "NONMONOTONE_TASK_CHANGE"


def build_result() -> dict[str, Any]:
    checks: dict[str, bool] = {}

    # XH-01: one immutable stage-zero object can pre-encode both the realized
    # path and a full finite counterfactual response tree.
    oracle = {
        "options": ["L", "R"],
        "realized_path": ["L", "R"],
        "response_tree": {
            "": {"L": "sL", "R": "sR"},
            "L": {"L": "sLL", "R": "sLR"},
            "R": {"L": "sRL", "R": "sRR"},
        },
    }
    oracle_hash_before = digest(oracle)
    realized_replay = [
        oracle["response_tree"][""]["L"],
        oracle["response_tree"]["L"]["R"],
    ]
    counterfactual_replay = oracle["response_tree"]["R"]["L"]
    oracle_hash_after = digest(oracle)
    checks["XH01_fixed_source_replays_realized_path"] = realized_replay == ["sL", "sLR"]
    checks["XH01_fixed_source_contains_counterfactual_response"] = (
        counterfactual_replay == "sRL"
    )
    checks["XH01_source_remains_stage_fixed"] = oracle_hash_before == oracle_hash_after

    # XH-02: every declared local statistic and local intervention agrees,
    # while a separately declared boundary-crossing read separates capability.
    global_left = {"record": 0, "environment": 0}
    global_right = {"record": 0, "environment": 1}
    local_interventions = (
        lambda state: state["record"],
        lambda state: 1 - state["record"],
        lambda state: state["record"] ^ 1,
    )
    local_left = [operation(global_left) for operation in local_interventions]
    local_right = [operation(global_right) for operation in local_interventions]
    boundary_action_left = global_left["environment"]
    boundary_action_right = global_right["environment"]
    checks["XH02_local_record_and_interventions_are_isomorphic"] = (
        local_left == local_right
    )
    checks["XH02_declared_boundary_crossing_separates_capability"] = (
        boundary_action_left != boundary_action_right
    )

    # XH-03: subdividing one physical support can inflate raw fragment count
    # without changing independently audited support or the objectivity verdict.
    support_before = {"fragment_a": "support_1", "fragment_b": "support_2"}
    support_after = {
        "fragment_a1": "support_1",
        "fragment_a2": "support_1",
        "fragment_b": "support_2",
    }
    independent_before = sorted(set(support_before.values()))
    independent_after = sorted(set(support_after.values()))
    public_before = len(independent_before) >= 2
    public_after = len(independent_after) >= 2
    checks["XH03_raw_fragment_count_changes_under_support_split"] = (
        len(support_before) != len(support_after)
    )
    checks["XH03_audited_support_and_verdict_are_absorbed"] = (
        independent_before == independent_after and public_before == public_after
    )

    # XH-04: benign relay subdivision preserves projected reachability but not
    # hop count. Relabeling the relay also leaves projected reachability fixed.
    coarse_edges = (("A", "B"),)
    refined_edges = (("A", "X"), ("X", "B"))
    relabeled_edges = (("A", "Y"), ("Y", "B"))
    coarse_reach = reachability(("A", "B"), coarse_edges)
    refined_reach = reachability(("A", "X", "B"), refined_edges)
    relabeled_reach = reachability(("A", "Y", "B"), relabeled_edges)
    projected_refined = {
        endpoint: [value for value in refined_reach[endpoint] if value in {"A", "B"}]
        for endpoint in ("A", "B")
    }
    projected_relabeled = {
        endpoint: [value for value in relabeled_reach[endpoint] if value in {"A", "B"}]
        for endpoint in ("A", "B")
    }
    checks["XH04_projected_reachability_is_refinement_natural"] = (
        coarse_reach == projected_refined == projected_relabeled
    )
    checks["XH04_hop_count_is_not_benign_refinement_invariant"] = (
        shortest_hops("A", "B", coarse_edges)
        != shortest_hops("A", "B", refined_edges)
    )

    # XH-05: improved raw performance under a changed instrument is not a
    # normalized capability verdict; strict task enlargement at one frame is.
    base_frame = {
        "system_count": 2,
        "execution_time": 1.0,
        "controls": ["prepare", "read"],
        "prior_information": "uniform",
        "readout_access": "local",
        "decoder": "D0",
        "error_budget": 0.01,
        "resource_budget": 10,
        "certified_tasks": ["resolve_bit"],
        "precision": 0.90,
    }
    changed_instrument = {
        **base_frame,
        "system_count": 4,
        "precision": 0.99,
    }
    matched_capability = {
        **base_frame,
        "certified_tasks": ["resolve_bit", "resolve_phase"],
        "precision": 0.90,
    }
    checks["XH05_changed_instrument_blocks_normalized_capability_verdict"] = (
        capability_verdict(base_frame, changed_instrument) == "FRAME_CHANGED"
    )
    checks["XH05_matched_frame_detects_strict_task_enlargement"] = (
        capability_verdict(base_frame, matched_capability) == "CAPABILITY_INCREASE"
    )

    # XH-06: the sibling constructor list is a proper baseline subset, and DU
    # retains additional adversaries rather than asserting finite closure.
    baseline_constructors = {
        "seed",
        "boundary",
        "resource",
        "access",
        "hidden_state",
        "history",
        "provenance",
        "relabeling_or_gauge",
        "whole_family_containment",
    }
    du_extensions = {
        "fixed_future_correlated_oracle",
        "departed_environment",
        "routed_implementation",
        "adaptive_controller_or_scheduler",
        "alternative_record_instrument",
        "decoder_or_observer_boundary",
    }
    completion_inventory = baseline_constructors | du_extensions
    checks["XH06_baseline_is_nonempty_proper_subset"] = (
        bool(baseline_constructors)
        and baseline_constructors < completion_inventory
    )
    checks["XH06_du_specific_adversaries_are_retained"] = (
        du_extensions <= completion_inventory
    )

    bindings = {
        "XH-01": ["HC-DU-014", "HC-DU-024", "HC-DU-036B", "Lane-1.2"],
        "XH-02": ["H-CCR-05", "H-CCR-06", "HC-DU-036B", "HC-DU-037", "B1", "B6"],
        "XH-03": ["H-CCR-04", "HC-DU-035B", "HC-DU-037", "B4"],
        "XH-04": ["H-CCR-08", "H-CCR-13", "HC-DU-038"],
        "XH-05": ["H-CCR-06", "H-CCR-07", "HC-DU-037"],
        "XH-06": ["HC-DU-036B", "B6"],
    }
    checks["all_six_controls_have_existing_program_bindings"] = set(bindings) == {
        f"XH-0{index}" for index in range(1, 7)
    }

    source_grades = {
        "XH-01": "sibling mathematical countermodel; physical realizability unclaimed",
        "XH-02": "sibling finite quantum fixture; adopted boundary; hostile review queued",
        "XH-03": "sibling finite-family factorization; no universal SBS theorem",
        "XH-04": "sibling finite refinement gates for one declared morphism class",
        "XH-05": "sibling argument plus deterministic classification; no new measurement",
        "XH-06": "sibling exploratory coarse finite theorem; inventory nonexhaustive",
    }

    return {
        "probe": "du_cross_repo_hardening_controls_probe",
        "date": "2026-07-24",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "claim_grade": (
            "FINITE CONTROL-SHAPE RECHECK / NO PHYSICAL REALIZABILITY, "
            "CLAIM, HYPOTHESIS, PREDICTION, ONTOLOGY, OR SEED PROMOTION"
        ),
        "corrected_discriminator": (
            "For an independently frozen, nonempty class of causally available, "
            "future-independent, physically realizable, and resource-bounded "
            "completions: do record-isomorphic processes support the same admitted "
            "predictions and capabilities; if not, what finite intervention "
            "identifies the minimal omitted structure?"
        ),
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "bindings": bindings,
        "source_grades": source_grades,
        "nonclaims": [
            "stage-fixedness establishes physical novelty",
            "computational non-reducibility defines physical novelty",
            "the observer boundary is physically selected",
            "SBS absorbs every public-finality theory",
            "reachability is the only physical topology invariant",
            "raw performance is capability",
            "the listed completion constructors are exhaustive",
        ],
    }


def main() -> None:
    result = build_result()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"{result['status']}: {result['checks_passed']}/"
        f"{result['checks_total']} checks; wrote {OUTPUT.relative_to(ROOT)}"
    )
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
