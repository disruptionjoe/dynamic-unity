#!/usr/bin/env python3
"""Validate Dynamic Unity's current-research authority and cold-start contract.

This is a repository-governance probe. Passing establishes routing consistency,
reference integrity, WIP discipline, and cold-start recoverability only. It
establishes no physics, theorem, ontology, novelty, prediction, or paper grade.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CURRENT_PATH = ROOT / "CURRENT-RESEARCH.yaml"
LANES_PATH = ROOT / "LANES.yaml"
COUNTER_REGISTER = ROOT / "COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md"

STABLE_FILES = {
    "start": ROOT / "START-HERE.md",
    "agents": ROOT / "AGENTS.md",
    "readme": ROOT / "README.md",
    "lanes": LANES_PATH,
    "program": ROOT / "docs" / "certified-causal-reality-research-program.md",
    "docs_index": ROOT / "docs" / "README.md",
    "connections": ROOT / "CONNECTIONS.md",
    "explorations_index": ROOT / "explorations" / "README.md",
}
HISTORICAL_FILES = {
    "results_history": ROOT / "EARNED-RESULTS-INDEX.md",
    "lanes_history": ROOT / "LANES-HISTORY.yaml",
}

EXPECTED_LANES = {
    "1": "North-Star adjudication",
    "2": "Forward representation and coherence",
    "3": "Physical record formation and selection",
    "4": "Observer access, certification and capability",
    "5": "Regional finality and recursive composition",
    "6": "Time, geometry, fields and physical reconstruction",
    "7": "Remainders, predictions and publishable results",
    "A": "Stewardship",
}
EXPECTED_CHANNELS = {
    "CH-SYN": "Synthesis and compatibility atlas",
    "CH-FORMAL": "Formal proof and reconstruction",
    "CH-MODEL": "Executable models and counterexamples",
    "CH-COLLIDE": "Literature and novelty collision",
    "CH-EMPIRICAL": "Experimental discriminators",
    "CH-PAPER": "Paper production",
    "CH-FRONTIER": "Speculative frontier",
}
EXPECTED_GRADES = {
    0: "vocabulary",
    1: "compatibility",
    2: "representation",
    3: "reconstruction",
    4: "selection_or_necessity",
    5: "remainder_or_prediction",
}
EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS = 212
CURRENT_AUTHORITY_NAME = "CURRENT-RESEARCH.yaml"
EXPECTED_EXECUTABLE_ACTION = "N5-PF-P5"
EXPECTED_PUBLICATION_CANDIDATE = "DU-PAPER-013"


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must parse as a YAML mapping")
    return value


def local_markdown_targets(path: Path, text: str) -> list[Path]:
    targets: list[Path] = []
    for raw_target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = raw_target.strip().strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        targets.append((path.parent / target).resolve())
    return targets


def assert_acyclic(edges: dict[str, set[str]]) -> None:
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(node: str) -> None:
        if node in permanent:
            return
        if node in temporary:
            raise AssertionError(f"program dependency cycle reaches {node}")
        temporary.add(node)
        for child in edges.get(node, set()):
            visit(child)
        temporary.remove(node)
        permanent.add(node)

    for node in edges:
        visit(node)


def run() -> dict[str, Any]:
    current = load_yaml(CURRENT_PATH)
    lanes = load_yaml(LANES_PATH)
    stable_texts = {
        name: path.read_text(encoding="utf-8") for name, path in STABLE_FILES.items()
    }
    historical_texts = {
        name: path.read_text(encoding="utf-8")
        for name, path in HISTORICAL_FILES.items()
    }
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{check_id}: {detail}")
        checks.append({"id": check_id, "pass": True, "detail": detail})

    check(
        "current_contract_identity",
        current.get("current_research_contract_version") == "1.0"
        and isinstance(current.get("state_revision"), int)
        and current.get("scope", "").startswith("Sole mutable authority"),
        "current authority has a version, revision and exclusive scope",
    )

    rules = current.get("rules", {})
    status_enums = current.get("status_enums", {})
    programs = current.get("programs", [])
    check(
        "current_schema_roots",
        isinstance(rules, dict)
        and isinstance(status_enums, dict)
        and isinstance(programs, list)
        and bool(programs),
        "rules, enums and a nonempty program portfolio are present",
    )

    program_ids = [program.get("id") for program in programs]
    check(
        "program_ids_unique",
        all(isinstance(value, str) and value for value in program_ids)
        and len(program_ids) == len(set(program_ids)),
        f"program IDs are nonempty and unique: {program_ids}",
    )
    program_by_id = {program["id"]: program for program in programs}

    allowed_portfolio = set(status_enums.get("portfolio_status", []))
    allowed_execution = set(status_enums.get("execution_status", []))
    allowed_dependency = set(status_enums.get("dependency_type", []))
    check(
        "enum_contract",
        allowed_portfolio
        == {"active", "ready", "parked", "blocked", "complete", "external_custody"}
        and allowed_execution == {"executable", "prepared", "none"}
        and allowed_dependency
        == {"requires", "tests", "extracts_from", "external_dependency", "does_not_block"},
        "portfolio, execution and dependency enums are exact",
    )

    invalid_statuses = [
        program["id"]
        for program in programs
        if program.get("portfolio_status") not in allowed_portfolio
        or program.get("execution_status") not in allowed_execution
    ]
    check(
        "program_statuses_valid",
        not invalid_statuses,
        f"all programs use declared statuses; invalid={invalid_statuses}",
    )

    executable = [
        program for program in programs if program.get("execution_status") == "executable"
    ]
    active_science = [
        program
        for program in programs
        if program.get("portfolio_status") == "active"
        and program.get("wip_slot") == "scientific_flagship"
    ]
    check(
        "one_active_scientific_program",
        len(active_science) == 1
        and len(executable) == 1
        and executable[0]["id"] == active_science[0]["id"],
        (
            "exactly one active scientific flagship is executable; "
            f"active={[p['id'] for p in active_science]} "
            f"executable={[p['id'] for p in executable]}"
        ),
    )

    decision = current.get("current_decision", {})
    active = active_science[0]
    check(
        "decision_matches_portfolio",
        decision.get("active_scientific_program_id") == active["id"]
        and decision.get("executable_action_id") == active.get("active_work_id")
        and decision.get("executable_action_id") == EXPECTED_EXECUTABLE_ACTION
        and decision.get("selected_successor_id") is None,
        "decision points to the active program/action and leaves successor unselected",
    )

    publication = program_by_id.get(decision.get("publication_program_id"))
    check(
        "publication_exact_candidate",
        publication is not None
        and publication.get("kind") == "publication"
        and publication.get("execution_status") == "prepared"
        and publication.get("candidate_id") == EXPECTED_PUBLICATION_CANDIDATE,
        "the separate prepared publication slot names one exact candidate",
    )
    slot_counts = Counter(
        program.get("wip_slot")
        for program in programs
        if program.get("portfolio_status") in {"active", "ready"}
        and program.get("wip_slot") != "none"
    )
    check(
        "wip_limits",
        slot_counts["scientific_flagship"] <= rules["scientific_flagship_wip_limit"]
        and slot_counts["publication"] <= rules["publication_wip_limit"]
        and slot_counts["bounded_side_probe"] <= rules["bounded_side_probe_wip_limit"],
        f"WIP slots satisfy declared limits: {dict(slot_counts)}",
    )

    parked_errors: list[str] = []
    for program in programs:
        if program.get("portfolio_status") != "parked":
            continue
        if (
            program.get("execution_status") != "none"
            or program.get("next_action") is not None
            or program.get("next_action_ref") is not None
            or not str(program.get("reopen_rule", "")).strip()
        ):
            parked_errors.append(program["id"])
    check(
        "parked_program_contract",
        not parked_errors,
        f"parked programs have no action and exact reopeners; invalid={parked_errors}",
    )

    required_program_fields = {
        "id",
        "kind",
        "owner_repo",
        "portfolio_status",
        "execution_status",
        "wip_slot",
        "target",
        "current_grade",
        "maximum_grade",
        "premise_status",
        "remaining_obligations",
        "typed_dependencies",
        "cheapest_kill",
        "stop_rule",
        "reopen_rule",
        "local_computation_boundary",
        "next_action",
        "next_action_ref",
        "canonical_evidence_refs",
    }
    incomplete_programs: dict[str, list[str]] = {}
    for program in programs:
        missing = sorted(required_program_fields - set(program))
        if missing:
            incomplete_programs[program["id"]] = missing
    check(
        "program_contract_completeness",
        not incomplete_programs,
        f"every program has grade, premise, dependency, kill/stop/reopen and local-boundary fields; missing={incomplete_programs}",
    )

    dependency_errors: list[str] = []
    internal_edges: dict[str, set[str]] = {program_id: set() for program_id in program_ids}
    for program in programs:
        for dependency in program.get("typed_dependencies", []):
            dependency_type = dependency.get("type")
            target = dependency.get("target")
            if dependency_type not in allowed_dependency or not isinstance(target, str):
                dependency_errors.append(f"{program['id']}:{dependency}")
                continue
            if dependency_type == "external_dependency" and not dependency.get("owner_repo"):
                dependency_errors.append(f"{program['id']}:external-without-owner:{target}")
            if dependency_type == "requires" and target in program_by_id:
                internal_edges[program["id"]].add(target)
    check(
        "typed_dependencies_valid",
        not dependency_errors,
        f"dependency types and external owners are valid; errors={dependency_errors}",
    )
    assert_acyclic(internal_edges)
    check(
        "internal_dependencies_acyclic",
        True,
        f"program-level requires graph is acyclic: {internal_edges}",
    )

    missing_refs: list[str] = []
    ref_count = 0
    for program in programs:
        refs = list(program.get("canonical_evidence_refs", []))
        refs.extend(
            dependency.get("evidence_ref")
            for dependency in program.get("completed_dependencies", [])
            if dependency.get("evidence_ref")
        )
        if program.get("next_action_ref"):
            refs.append(program["next_action_ref"])
        for ref in refs:
            ref_count += 1
            if not (ROOT / ref).exists():
                missing_refs.append(f"{program['id']}:{ref}")
    check(
        "current_evidence_refs_resolve",
        ref_count >= 10 and not missing_refs,
        f"{ref_count} current evidence and action references resolve; missing={missing_refs}",
    )

    check(
        "successor_blocked_by_current_action",
        current.get("successor_selection", {}).get("status") == "blocked"
        and current["successor_selection"].get("blocked_by")
        == decision.get("executable_action_id")
        and current["successor_selection"].get("selected_successor_id") is None,
        "successor selection waits for the current executable return",
    )
    check(
        "anomaly_intake_non_wip",
        current.get("anomaly_intake", {}).get("status") == "open_non_wip"
        and "never" in current["anomaly_intake"].get("activation_rule", "").lower(),
        "anomaly intake remains open without creating standing parallel work",
    )

    actual_lanes = {
        str(item["id"]): item["title"] for item in lanes.get("lanes", [])
    }
    actual_channels = {
        item["id"]: item["title"] for item in lanes.get("work_channels", [])
    }
    actual_grades = {
        item["grade"]: item["label"] for item in lanes.get("evidence_grades", [])
    }
    check(
        "stable_lane_topology",
        actual_lanes == EXPECTED_LANES,
        f"stable lane map exact: {actual_lanes}",
    )
    check(
        "stable_channel_topology",
        actual_channels == EXPECTED_CHANNELS,
        f"stable channel map exact: {actual_channels}",
    )
    check(
        "stable_grade_topology",
        actual_grades == EXPECTED_GRADES,
        f"evidence grades exact: {actual_grades}",
    )
    check(
        "lanes_have_no_current_objective",
        "current_objective" not in lanes
        and "current_objective:" not in stable_texts["lanes"]
        and lanes.get("current_research_ref") == CURRENT_AUTHORITY_NAME,
        "stable lane topology contains no mutable current objective",
    )

    missing_authority_pointers = [
        name
        for name, text in stable_texts.items()
        if CURRENT_AUTHORITY_NAME not in text
    ]
    check(
        "stable_surfaces_route_current_authority",
        not missing_authority_pointers,
        f"every stable entrypoint points to the live authority; missing={missing_authority_pointers}",
    )

    forbidden_live_assertions = (
        "Only `N5-PF-P5` is executable",
        "N5-PF-P5 is the sole executable",
        "N5-PF-P5 alone is executable",
        "sole executable position",
    )
    duplicated_live_assertions = [
        f"{name}:{phrase}"
        for name, text in stable_texts.items()
        for phrase in forbidden_live_assertions
        if phrase in text
    ]
    check(
        "no_duplicated_mutable_routing_assertion",
        not duplicated_live_assertions,
        f"stable surfaces do not copy executable status; duplicates={duplicated_live_assertions}",
    )
    mutable_tokens = set(program_ids)
    mutable_tokens.add(str(decision.get("executable_action_id")))
    copied_mutable_tokens = [
        f"{name}:{token}"
        for name, text in stable_texts.items()
        for token in mutable_tokens
        if token and token in text
    ]
    check(
        "no_copied_current_program_or_action_ids",
        not copied_mutable_tokens,
        f"stable surfaces point to live state without copying its IDs; copies={copied_mutable_tokens}",
    )

    check(
        "historical_snapshot_guards",
        "historical_snapshot" in historical_texts["results_history"]
        and CURRENT_AUTHORITY_NAME in historical_texts["results_history"]
        and "historical_snapshot: true" in historical_texts["lanes_history"]
        and CURRENT_AUTHORITY_NAME in historical_texts["lanes_history"],
        "preserved historical surfaces are explicitly non-routing",
    )

    counter_text = COUNTER_REGISTER.read_text(encoding="utf-8")
    counter_ids = [
        line.split("|")[1].strip().strip("`")
        for line in counter_text.splitlines()
        if line.startswith("|")
        and len(line.split("|")) > 1
        and line.split("|")[1].strip().strip("`").startswith("NI-")
    ]
    check(
        "counter_assumptive_register_count",
        len(counter_ids) == EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS
        and len(counter_ids) == len(set(counter_ids)),
        (
            "counter-assumptive register retains its source-pinned unique row "
            f"count; found={len(counter_ids)} unique={len(set(counter_ids))}"
        ),
    )

    missing_links: list[str] = []
    link_count = 0
    for name, path in STABLE_FILES.items():
        for target in local_markdown_targets(path, stable_texts[name]):
            link_count += 1
            if not target.exists():
                missing_links.append(f"{name}:{target}")
    check(
        "entrypoint_links_resolve",
        link_count >= 15 and not missing_links,
        f"{link_count} stable-entrypoint links resolve; missing={missing_links}",
    )

    cold_start_paths = (
        ROOT / "AGENTS.md",
        ROOT / "START-HERE.md",
        CURRENT_PATH,
        LANES_PATH,
    )
    cold_start_words = sum(
        len(path.read_text(encoding="utf-8").split()) for path in cold_start_paths
    )
    check(
        "cold_start_budget",
        cold_start_words <= 6000,
        f"required cold-start surfaces total {cold_start_words} words (limit 6000)",
    )

    check(
        "scientific_nonpromotion",
        "no scientific result" in (
            CURRENT_PATH.parent
            / "lab"
            / "process"
            / "runs"
            / "RUN-20260727-162657-current-research-authority-migration"
            / "run-plan.md"
        ).read_text(encoding="utf-8").lower(),
        "migration run explicitly makes no scientific promotion",
    )

    return {
        "probe": "du_agent_orientation_contract_probe",
        "status": "PASS",
        "scope": "current_research_authority_and_cold_start_governance_only",
        "authority": CURRENT_AUTHORITY_NAME,
        "active_scientific_program": decision["active_scientific_program_id"],
        "executable_action": decision["executable_action_id"],
        "prepared_publication_candidate": publication["candidate_id"],
        "cold_start_words": cold_start_words,
        "checks_passed": len(checks),
        "checks": checks,
        "disclaimer": (
            "Passing establishes repository routing consistency only; it "
            "establishes no scientific result."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
