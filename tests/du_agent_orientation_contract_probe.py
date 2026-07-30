#!/usr/bin/env python3
"""Validate Dynamic Unity's live authority and cold-start contract.

This is a repository-governance probe. Passing establishes routing consistency,
reference integrity, WIP discipline, schema conformance, and cold-start
recoverability only. It establishes no physics, theorem, ontology, novelty,
prediction, scientific grade, or paper readiness.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import unicodedata
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CURRENT_PATH = ROOT / "CURRENT-RESEARCH.yaml"
SCHEMA_PATH = ROOT / "CURRENT-RESEARCH.schema.json"
LANES_PATH = ROOT / "LANES.yaml"
COUNTER_REGISTER = ROOT / "COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md"
ARTIFACT_PATH = ROOT / "tests" / "artifacts" / "du_agent_orientation_contract_result.json"
FOUNDATIONS_PATH = ROOT / "docs" / "quantum-foundations-orientation-surface.md"
CONCEPT_REGISTER_PATH = ROOT / "explorations" / "concept-register.md"

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
CHARTER_COPIES = ("start", "agents", "readme", "program")
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
EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS = 317
CURRENT_AUTHORITY_NAME = CURRENT_PATH.name

SEMANTIC_MARKERS = {
    "start": (
        "Dynamic Unity adopts minimal scientific realism",
        "Keep three coordinates independent",
        "Observer-indexed means indexed to a physical subsystem's records",
        "Public certification means jointly action-available",
        "Beginning reconstruction from records is an epistemic method",
    ),
    "agents": (
        "methodological physical realism",
        "Observer-indexed does not mean subjective",
        "Public does not mean globally complete",
        "Record-relative determinacy or internal underivability is not source issuance",
    ),
    "program": (
        "Perspective and ontology contract",
        "The act of constructing a scientific ontology is epistemic",
        "Public or composition-global finality is not the observer-independent global ontology",
        "first-person or internal underivability does not by itself prove issuance",
        "EPR completeness question seriously",
    ),
    "foundations": (
        "Perspective, ontology, and the EPR completeness question",
        "Einstein--Podolsky--Rosen paper",
        "Bohr's reply",
        "They do not by themselves refute observer-independent reality",
        "perspective_scope: local_system | regional_public | global_completion",
        "formation_status: disclosure | candidate_issuance | undecided",
    ),
    "concepts": (
        "Perspective and status guard",
        "record-relative determinacy and candidate physical formation",
        "This formal core does not decide whether the proposition pre-existed",
    ),
}


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"{path.name} must parse as a YAML mapping")
    return value


def normalized_prose(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


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


def missing_semantic_markers(semantic_texts: dict[str, str]) -> list[str]:
    missing: list[str] = []
    for name, markers in SEMANTIC_MARKERS.items():
        normalized_text = normalized_prose(semantic_texts[name])
        for marker in markers:
            if normalized_prose(marker) not in normalized_text:
                missing.append(f"{name}:{marker}")
    return missing


def validate_json_schema(current: dict[str, Any]) -> str:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise AssertionError("schema must declare JSON Schema draft 2020-12")
    if importlib.util.find_spec("jsonschema") is None:
        return "schema parsed; semantic fallback used because jsonschema is unavailable"

    import jsonschema

    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(current)
    return "validated with jsonschema Draft202012Validator"


def validate_authority(
    current: dict[str, Any],
    lanes: dict[str, Any],
    stable_texts: dict[str, str],
    historical_texts: dict[str, str],
    semantic_texts: dict[str, str],
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{check_id}: {detail}")
        checks.append({"id": check_id, "pass": True, "detail": detail})

    schema_detail = validate_json_schema(current)
    check(
        "json_schema_contract",
        current.get("schema_ref") == SCHEMA_PATH.name,
        schema_detail,
    )
    check(
        "current_contract_identity",
        current.get("current_research_contract_version") == "1.2"
        and isinstance(current.get("state_revision"), int)
        and current.get("scope", "").startswith("Sole mutable authority"),
        "current authority has contract version 1.2, a revision, and exclusive scope",
    )

    rules = current.get("rules", {})
    status_enums = current.get("status_enums", {})
    programs = current.get("programs", [])
    check(
        "current_schema_roots",
        isinstance(rules, dict)
        and isinstance(status_enums, dict)
        and isinstance(programs, list)
        and bool(programs)
        and isinstance(current.get("transition_protocol"), dict)
        and isinstance(current.get("run_home_contract"), dict),
        "rules, enums, transition/run-home contracts, and a program portfolio exist",
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
    allowed_target_type = set(status_enums.get("dependency_target_type", []))
    check(
        "enum_contract",
        allowed_portfolio
        == {"active", "ready", "parked", "blocked", "complete", "external_custody"}
        and allowed_execution == {"executable", "prepared", "none"}
        and allowed_dependency
        == {"requires", "tests", "extracts_from", "external_dependency", "does_not_block"}
        and allowed_target_type
        == {"program", "result", "premise", "prediction", "requirement", "external_work"},
        "portfolio, execution, dependency, and dependency-target enums are exact",
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
    successor = current.get("successor_selection", {})
    quiescent = successor.get("status") == "no_ready"
    decision = current.get("current_decision", {})
    check(
        "active_or_quiescent_scientific_program",
        (
            quiescent
            and rules.get("quiescent_no_ready_allowed") is True
            and not active_science
            and not executable
            and decision.get("active_scientific_program_id") is None
            and decision.get("executable_action_id") is None
        )
        or (
            not quiescent
            and len(active_science) == 1
            and len(executable) == 1
            and executable[0]["id"] == active_science[0]["id"]
        ),
        (
            "one active executable flagship or an explicit no-ready "
            "quiescent state; "
            f"active={[p['id'] for p in active_science]} "
            f"executable={[p['id'] for p in executable]}"
        ),
    )

    active = active_science[0] if active_science else None
    check(
        "decision_matches_portfolio",
        (
            (
                quiescent
                and decision.get("active_scientific_program_id") is None
                and decision.get("executable_action_id") is None
            )
            or (
                active is not None
                and decision.get("active_scientific_program_id") == active["id"]
                and decision.get("executable_action_id") == active.get("active_work_id")
            )
        )
        and decision.get("selected_successor_id") is None,
        "decision derives its active program/action or explicit quiescence from the portfolio",
    )

    publication = program_by_id.get(decision.get("prepared_publication_program_id"))
    check(
        "prepared_publication_contract",
        publication is not None
        and publication.get("kind") == "publication"
        and publication.get("execution_status") == "prepared"
        and isinstance(publication.get("candidate_id"), str)
        and bool(publication["candidate_id"]),
        "the separate prepared publication slot names one nonempty candidate",
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
        "primary_lane_id",
        "supporting_lane_ids",
        "channel_ids",
        "target",
        "current_grade",
        "evidence_grade",
        "maximum_grade",
        "maximum_evidence_grade",
        "premise_status",
        "completed_dependencies",
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
        f"every program has normalized lanes/grades and control fields; missing={incomplete_programs}",
    )

    actual_lanes = {str(item["id"]): item["title"] for item in lanes.get("lanes", [])}
    actual_channels = {
        item["id"]: item["title"] for item in lanes.get("work_channels", [])
    }
    actual_grades = {
        item["grade"]: item["label"] for item in lanes.get("evidence_grades", [])
    }
    topology_errors: list[str] = []
    grade_errors: list[str] = []
    for program in programs:
        primary = str(program.get("primary_lane_id"))
        supporting = [str(item) for item in program.get("supporting_lane_ids", [])]
        channels = program.get("channel_ids", [])
        if (
            primary not in actual_lanes
            or primary in supporting
            or len(supporting) != len(set(supporting))
            or any(item not in actual_lanes for item in supporting)
            or any(item not in actual_channels for item in channels)
        ):
            topology_errors.append(program["id"])
        for field in ("evidence_grade", "maximum_evidence_grade"):
            value = program.get(field)
            if value is not None and (
                not isinstance(value, int) or isinstance(value, bool) or value not in actual_grades
            ):
                grade_errors.append(f"{program['id']}:{field}={value!r}")
        current_grade = program.get("evidence_grade")
        maximum_grade = program.get("maximum_evidence_grade")
        if (
            current_grade is not None
            and maximum_grade is not None
            and current_grade > maximum_grade
        ):
            grade_errors.append(f"{program['id']}:current-exceeds-maximum")
    check(
        "normalized_lane_and_channel_refs",
        not topology_errors,
        f"primary/supporting lanes and channels resolve without overlap; errors={topology_errors}",
    )
    check(
        "normalized_grade_contract",
        not grade_errors,
        f"normalized grades are null or declared integers and do not exceed maxima; errors={grade_errors}",
    )

    dependency_errors: list[str] = []
    internal_edges: dict[str, set[str]] = {program_id: set() for program_id in program_ids}
    for program in programs:
        for dependency in program.get("typed_dependencies", []):
            dependency_type = dependency.get("type")
            target = dependency.get("target")
            target_type = dependency.get("target_type")
            if (
                dependency_type not in allowed_dependency
                or target_type not in allowed_target_type
                or not isinstance(target, str)
                or not target
            ):
                dependency_errors.append(f"{program['id']}:{dependency}")
                continue
            if dependency_type == "external_dependency" and not dependency.get("owner_repo"):
                dependency_errors.append(f"{program['id']}:external-without-owner:{target}")
            if target_type == "program" and target not in program_by_id:
                dependency_errors.append(f"{program['id']}:missing-program:{target}")
            if (
                dependency_type == "requires"
                and target_type == "program"
                and target in program_by_id
            ):
                internal_edges[program["id"]].add(target)
    check(
        "typed_dependencies_valid",
        not dependency_errors,
        f"dependency relations and target namespaces are explicit; errors={dependency_errors}",
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
        packet = program.get("execution_packet")
        if packet:
            refs.append(packet.get("source_locator", {}).get("path"))
            refs.extend(item.get("path") for item in packet.get("required_inputs", []))
        for ref in refs:
            ref_count += 1
            if not isinstance(ref, str) or not (ROOT / ref).exists():
                missing_refs.append(f"{program['id']}:{ref}")
    check(
        "current_evidence_refs_resolve",
        ref_count >= 10 and not missing_refs,
        f"{ref_count} current evidence, action, and input references resolve; missing={missing_refs}",
    )

    packet: dict[str, Any] = {}
    packet_errors: list[str] = []
    if active is not None:
        packet = active.get("execution_packet", {})
        source_locator = packet.get("source_locator", {})
        source_path = ROOT / str(source_locator.get("path", ""))
        source_heading = source_locator.get("heading", "")
        packet_controls = packet.get("uses_program_controls", [])
        if packet.get("action_id") != active.get("active_work_id"):
            packet_errors.append("action mismatch")
        if not str(packet.get("exact_question", "")).strip():
            packet_errors.append("missing exact question")
        if not source_path.is_file() or source_heading not in source_path.read_text(
            encoding="utf-8"
        ):
            packet_errors.append("source locator does not resolve to its heading")
        for key in (
            "required_inputs",
            "unchanged_ledger_fields",
            "arena_roles",
            "expected_return_classes",
            "observer_index_return_classes",
        ):
            if not packet.get(key):
                packet_errors.append(f"missing {key}")
        for key in packet_controls:
            if not str(active.get(key, "")).strip():
                packet_errors.append(f"control {key} is absent from active program")
        if not str(packet.get("durable_output", "")).strip():
            packet_errors.append("missing durable output")
        if not str(packet.get("local_method", "")).strip():
            packet_errors.append("missing local method")
    elif any(program.get("execution_packet") for program in programs):
        packet_errors.append("quiescent portfolio retains an execution packet")
    check(
        "execution_packet_contract",
        not packet_errors,
        (
            "an active action has one complete embedded packet, or a "
            f"quiescent portfolio has none; errors={packet_errors}"
        ),
    )

    check(
        "successor_state_contract",
        (
            quiescent
            and successor.get("blocked_by") is None
            and successor.get("selected_successor_id") is None
        )
        or (
            not quiescent
            and successor.get("status") == "blocked"
            and successor.get("blocked_by") == decision.get("executable_action_id")
            and successor.get("selected_successor_id") is None
        ),
        "successor selection is blocked by the active action or explicitly no-ready",
    )
    check(
        "anomaly_intake_non_wip",
        current.get("anomaly_intake", {}).get("status") == "open_non_wip"
        and "never" in current["anomaly_intake"].get("activation_rule", "").lower(),
        "anomaly intake remains open without creating standing parallel work",
    )

    transition = current.get("transition_protocol", {})
    check(
        "state_transition_protocol",
        len(transition.get("steps", [])) >= 5
        and "increment" in " ".join(transition["steps"]).lower()
        and "never rewrite" in transition.get("history_rule", "").lower(),
        "live-state changes have an ordered revision, validation, and additive-history protocol",
    )

    run_homes = current.get("run_home_contract", {})
    legacy_readme = (ROOT / "runs" / "README.md").read_text(encoding="utf-8")
    check(
        "run_home_contract",
        run_homes.get("governed_run_home") == "lab/process/runs/"
        and run_homes.get("legacy_run_home") == "runs/"
        and "non-routing" in legacy_readme
        and "lab/process/runs/" in legacy_readme,
        "governed and legacy run homes are explicit without moving history",
    )

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
        name for name, text in stable_texts.items() if CURRENT_AUTHORITY_NAME not in text
    ]
    check(
        "stable_surfaces_route_current_authority",
        not missing_authority_pointers,
        f"every stable entrypoint points to the live authority; missing={missing_authority_pointers}",
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

    charter = lanes.get("program_charter", {})
    charter_errors: list[str] = []
    for charter_key in ("purpose", "vision", "mission", "north_star", "operating_principle"):
        expected = normalized_prose(str(charter.get(charter_key, "")))
        if not expected:
            charter_errors.append(f"structured:{charter_key}")
            continue
        for name in CHARTER_COPIES:
            if expected not in normalized_prose(stable_texts[name]):
                charter_errors.append(f"{name}:{charter_key}")
    check(
        "stable_charter_parity",
        lanes.get("charter_authority") == "program_charter" and not charter_errors,
        f"all stable charter copies match LANES.yaml program_charter; errors={charter_errors}",
    )

    semantic_missing = missing_semantic_markers(semantic_texts)
    check(
        "perspective_ontology_semantic_contract",
        not semantic_missing,
        (
            "cold-start and durable surfaces preserve independent perspective, "
            "ontic/epistemic, and disclosure/issuance coordinates; "
            f"missing={semantic_missing}"
        ),
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

    context_program = active or next(
        (
            program
            for program in programs
            if program.get("portfolio_status") == "complete"
            and program.get("kind") == "flagship"
        ),
        {},
    )
    dependency_classes = {
        dependency.get("target_type")
        for dependency in context_program.get("typed_dependencies", [])
    }
    isolated_recoveries = {
        "purpose_and_north_star": bool(charter.get("purpose") and charter.get("north_star")),
        "honest_evidence_boundary": (
            "has not established" in stable_texts["start"].lower()
            and bool(context_program.get("current_grade"))
        ),
        "perspective_ontology_contract": (
            "minimal scientific realism" in stable_texts["start"].lower()
            and "observer-indexed does not mean subjective"
            in stable_texts["agents"].lower()
            and "public certification means jointly action-available"
            in stable_texts["start"].lower()
        ),
        "active_or_quiescent_state": (
            quiescent
            and decision.get("active_scientific_program_id") is None
            and decision.get("executable_action_id") is None
        )
        or (
            active is not None
            and decision.get("active_scientific_program_id") == active.get("id")
            and decision.get("executable_action_id") == packet.get("action_id")
        ),
        "completed_and_remaining": bool(
            context_program.get("completed_dependencies")
            and (
                context_program.get("remaining_obligations")
                or quiescent
            )
        ),
        "execution_ceiling_and_output": bool(
            context_program.get("primary_lane_id")
            and context_program.get("channel_ids")
            and context_program.get("maximum_evidence_grade") is not None
            and context_program.get("strongest_absorber")
            and context_program.get("cheapest_kill")
            and context_program.get("stop_rule")
            and (packet.get("durable_output") or quiescent)
        ),
        "typed_dependencies": bool(dependency_classes),
        "local_boundary": bool(context_program.get("local_computation_boundary")),
    }
    check(
        "context_isolated_cold_start_recovery",
        all(isolated_recoveries.values()),
        (
            "the seven required answers are recoverable from only "
            f"AGENTS/START/CURRENT/LANES: {isolated_recoveries}"
        ),
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


def replace_identifiers(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, dict):
        return {
            key: replace_identifiers(item, replacements) for key, item in value.items()
        }
    if isinstance(value, list):
        return [replace_identifiers(item, replacements) for item in value]
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
    return value


def mutated_state_fixture(current: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    decision = current["current_decision"]
    publication = next(
        program
        for program in current["programs"]
        if program["id"] == decision["prepared_publication_program_id"]
    )
    routed_program_id = decision["active_scientific_program_id"] or next(
        program["id"]
        for program in current["programs"]
        if program.get("portfolio_status") == "complete"
        and program.get("kind") == "flagship"
    )
    replacements = {
        routed_program_id: "FIXTURE-SCIENTIFIC-PROGRAM",
        decision["prepared_publication_program_id"]: "FIXTURE-PUBLICATION-PROGRAM",
        publication["candidate_id"]: "FIXTURE-PUBLICATION-CANDIDATE",
    }
    if decision["executable_action_id"] is not None:
        replacements[decision["executable_action_id"]] = "FIXTURE-EXECUTABLE-ACTION"
    return replace_identifiers(deepcopy(current), replacements), replacements


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
    semantic_texts = {
        "start": stable_texts["start"],
        "agents": stable_texts["agents"],
        "program": stable_texts["program"],
        "foundations": FOUNDATIONS_PATH.read_text(encoding="utf-8"),
        "concepts": CONCEPT_REGISTER_PATH.read_text(encoding="utf-8"),
    }

    report = validate_authority(
        current, lanes, stable_texts, historical_texts, semantic_texts
    )
    mutated, replacements = mutated_state_fixture(current)
    mutated_report = validate_authority(
        mutated, lanes, stable_texts, historical_texts, semantic_texts
    )
    original_payload = json.dumps(current, sort_keys=True)
    mutated_payload = json.dumps(mutated, sort_keys=True)
    if any(old in mutated_payload for old in replacements):
        raise AssertionError("mutated_state_genericity: an original identifier survived")
    if not all(new in mutated_payload for new in replacements.values()):
        raise AssertionError("mutated_state_genericity: a fixture identifier is missing")
    if mutated_report["status"] != "PASS" or mutated_payload == original_payload:
        raise AssertionError("mutated_state_genericity: structurally equivalent state failed")
    report["checks"].append(
        {
            "id": "mutated_state_genericity",
            "pass": True,
            "detail": (
                "scientific-program, any active action, publication-program, "
                "and candidate IDs were mutated in memory and the unchanged "
                "validator passed"
            ),
        }
    )
    semantic_mutation_failures: list[str] = []
    for name, markers in SEMANTIC_MARKERS.items():
        marker = markers[0]
        mutated_semantics = dict(semantic_texts)
        mutated_semantics[name] = mutated_semantics[name].replace(
            marker, "REMOVED_SEMANTIC_CONTRACT_MARKER", 1
        )
        missing = missing_semantic_markers(mutated_semantics)
        if not any(item.startswith(f"{name}:") for item in missing):
            semantic_mutation_failures.append(name)
    if semantic_mutation_failures:
        raise AssertionError(
            "perspective_contract_negative_mutations: "
            f"mutations escaped={semantic_mutation_failures}"
        )
    report["checks"].append(
        {
            "id": "perspective_contract_negative_mutations",
            "pass": True,
            "detail": (
                "removing one required marker from each cold-start, durable, "
                "foundations, and concept surface was rejected"
            ),
        }
    )
    report["checks_passed"] = len(report["checks"])
    return report


def artifact_summary(report: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in report.items()
        if key != "checks"
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the compact deterministic result to tests/artifacts",
    )
    args = parser.parse_args()
    report = run()
    if args.write_artifact:
        ARTIFACT_PATH.write_text(
            json.dumps(artifact_summary(report), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
