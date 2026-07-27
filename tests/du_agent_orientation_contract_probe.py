#!/usr/bin/env python3
"""Deterministic cold-start orientation contract for Dynamic Unity.

This is a governance/orientation check, not a scientific assay. It verifies
that an incoming agent can recover one consistent program identity, active
dependency topology, method-channel map, evidence posture, current
bottleneck, and read path without conversational context.

Passing does not establish any physics, ontology, theorem, hypothesis,
prediction, novelty claim, paper readiness, or publication state.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
COUNTER_REGISTER = ROOT / "COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md"

FILES = {
    "start": ROOT / "START-HERE.md",
    "readme": ROOT / "README.md",
    "agents": ROOT / "AGENTS.md",
    "lanes": ROOT / "LANES.yaml",
    "program": ROOT / "docs" / "certified-causal-reality-research-program.md",
    "docs_index": ROOT / "docs" / "README.md",
    "connections": ROOT / "CONNECTIONS.md",
}

PURPOSE = (
    "Make physical reality intelligible as one coherent, "
    "evidence-accountable whole."
)
VISION = (
    "Build a living, ontology-neutral architecture in which quantum dynamics, "
    "records, observers, capabilities, spacetime, fields, particles, "
    "thermodynamics, and cosmology are related at their honestly earned "
    "evidentiary grades—and use the unresolved seams to locate, classify, "
    "dissolve, or decisively test the tensions in present physics."
)
MISSION = (
    "Construct, formalize, stress-test, and prepare for publication faithful "
    "representations, reconstruction theorems, countermodels, no-go results, "
    "and empirical discriminators that connect—or sharply separate—those "
    "layers."
)
NORTH_STAR = (
    "Determine whether independently selected, observer-indexed certified "
    "causal records reconstruct all observer-accessible time, geometry, "
    "fields, and capability—and identify a finite physical remainder "
    "wherever they do not."
)
OPERATING_PRINCIPLE = (
    "Whole-picture purpose. Seam-by-seam mission. Theorem-grade North Star."
)

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
CURRENT_COMPLETED_RESULT = "HC-DU-056"
CURRENT_EXECUTABLE_WORK = "N5-PF-P4"
EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS = 208


def normalize(value: str) -> str:
    """Normalize Markdown/YAML wrapping without erasing meaningful punctuation."""

    value = re.sub(r"[*_`>#]", "", value)
    return " ".join(value.split()).strip().lower()


def slice_between(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError as exc:
        raise AssertionError(f"missing topology delimiter: {start!r} / {end!r}") from exc


def parse_topology_entries(block: str) -> list[tuple[str, str, str]]:
    """Return (id, title, complete chunk) for one top-level YAML list block."""

    matches = list(re.finditer(r"(?m)^- id: (.+?)\n", block))
    entries: list[tuple[str, str, str]] = []
    for index, match in enumerate(matches):
        finish = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        chunk = block[match.start() : finish]
        raw_id = match.group(1).strip().strip("'\"")
        title_match = re.search(r"(?m)^  title: (.+)$", chunk)
        if title_match is None:
            raise AssertionError(f"topology entry {raw_id!r} has no title")
        title = title_match.group(1).strip().strip("'\"")
        entries.append((raw_id, title, chunk))
    return entries


def local_markdown_targets(path: Path, text: str) -> list[Path]:
    """Resolve ordinary local Markdown links in one entrypoint."""

    targets: list[Path] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if (
            not target
            or target.startswith(("#", "http://", "https://", "mailto:"))
        ):
            continue
        target = target.split("#", 1)[0]
        targets.append((path.parent / target).resolve())
    return targets


def run() -> dict[str, object]:
    texts = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}
    counter_register = COUNTER_REGISTER.read_text(encoding="utf-8")
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    canonical_surfaces = ("start", "readme", "agents", "lanes", "program")
    for label, statement in (
        ("purpose", PURPOSE),
        ("vision", VISION),
        ("mission", MISSION),
        ("north_star", NORTH_STAR),
        ("operating_principle", OPERATING_PRINCIPLE),
    ):
        expected = normalize(statement)
        missing = [
            surface
            for surface in canonical_surfaces
            if expected not in normalize(texts[surface])
        ]
        check(
            f"charter_{label}",
            not missing,
            f"canonical statement present on all five authority surfaces; missing={missing}",
        )

    for surface in ("readme", "agents", "program", "docs_index", "connections"):
        check(
            f"{surface}_routes_start_here",
            "START-HERE.md" in texts[surface],
            f"{surface} points to the cold-start surface",
        )

    for surface in ("start", "readme", "agents", "lanes", "program"):
        check(
            f"{surface}_current_handoff",
            CURRENT_COMPLETED_RESULT in texts[surface]
            and CURRENT_EXECUTABLE_WORK in texts[surface],
            (
                f"{surface} identifies {CURRENT_COMPLETED_RESULT} as the completed "
                f"result and routes work to {CURRENT_EXECUTABLE_WORK}"
            ),
        )

    counter_ids = [
        line.split("|")[1].strip().strip("`")
        for line in counter_register.splitlines()
        if line.startswith("|")
        and len(line.split("|")) > 1
        and line.split("|")[1].strip().strip("`").startswith("NI-")
    ]
    check(
        "counter_assumptive_register_count",
        len(counter_ids) == EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS
        and len(counter_ids) == len(set(counter_ids))
        and str(EXPECTED_COUNTER_ASSUMPTIVE_FINDINGS) in texts["start"],
        (
            "counter-assumptive register has the advertised unique source-pinned "
            f"row count; found={len(counter_ids)} "
            f"unique={len(set(counter_ids))}"
        ),
    )

    start_headings = (
        "## Ratified program charter",
        "## The scientific architecture",
        "## Honest current standing",
        "### The live bottleneck",
        "## Dependency lanes",
        "## Work channels",
        "## First ten minutes",
        "## Selecting and scoping work",
        "## Where durable work goes",
        "## Vocabulary and failure traps",
    )
    missing_headings = [heading for heading in start_headings if heading not in texts["start"]]
    check(
        "cold_start_sections",
        not missing_headings,
        f"orientation sections complete; missing={missing_headings}",
    )

    outcomes = (
        "record_first_reconstruction",
        "operational_duality",
        "physics_first_remainder",
    )
    missing_outcomes = [item for item in outcomes if item not in texts["lanes"]]
    check(
        "three_outcomes_open",
        not missing_outcomes and "No outcome is presumed" in texts["lanes"],
        f"three outcomes present and no outcome presumed; missing={missing_outcomes}",
    )

    for grade in (
        "vocabulary",
        "compatibility",
        "representation",
        "reconstruction",
        "selection_or_necessity",
        "remainder_or_prediction",
    ):
        check(
            f"grade_{grade}",
            f"label: {grade}" in texts["lanes"],
            f"evidence grade {grade} is machine-readable",
        )

    channel_block = slice_between(texts["lanes"], "work_channels:\n", "lanes:\n")
    lane_block = slice_between(
        texts["lanes"],
        "lanes:\n",
        "active_hardening_program_ref:",
    )
    channel_entries = parse_topology_entries(channel_block)
    lane_entries = parse_topology_entries(lane_block)

    actual_channels = {entry_id: title for entry_id, title, _ in channel_entries}
    actual_lanes = {entry_id: title for entry_id, title, _ in lane_entries}
    check(
        "active_channel_set",
        actual_channels == EXPECTED_CHANNELS,
        f"active channel map exact: {actual_channels}",
    )
    check(
        "active_lane_set",
        actual_lanes == EXPECTED_LANES,
        f"active dependency lane map exact: {actual_lanes}",
    )

    for lane_id, _, chunk in lane_entries:
        missing_fields = [
            field
            for field in (
                "  purpose:",
                "  depends_on:",
                "  current_objective:",
                "  success_signal:",
                "  default_channel_ids:",
                "  canonical_refs:",
                "  do_not:",
            )
            if field not in chunk
        ]
        referenced_channels = set(re.findall(r"(?m)^  - (CH-[A-Z]+)$", chunk))
        check(
            f"lane_{lane_id}_contract",
            not missing_fields
            and bool(referenced_channels)
            and referenced_channels <= set(EXPECTED_CHANNELS),
            (
                f"lane {lane_id} has complete routing contract; "
                f"missing={missing_fields}; channels={sorted(referenced_channels)}"
            ),
        )
        refs_block = slice_between(chunk, "  canonical_refs:\n", "  do_not:")
        refs = [
            value.strip()
            for value in re.findall(r"(?m)^  - (.+)$", refs_block)
        ]
        missing_refs = [value for value in refs if not (ROOT / value).exists()]
        check(
            f"lane_{lane_id}_canonical_refs",
            bool(refs) and not missing_refs and len(refs) == len(set(refs)),
            (
                f"lane {lane_id} canonical refs resolve without duplicates; "
                f"refs={refs}; missing={missing_refs}"
            ),
        )

    for channel_id, _, chunk in channel_entries:
        missing_fields = [
            field
            for field in ("  purpose:", "  required_receipt:")
            if field not in chunk
        ]
        check(
            f"channel_{channel_id}_contract",
            not missing_fields,
            f"channel {channel_id} declares purpose and receipt; missing={missing_fields}",
        )

    check(
        "one_north_star_lane",
        lane_block.count("  north_star: true") == 1
        and lane_block.count("  north_star: false") == 7,
        "exactly one active North-Star lane and seven non-North-Star lanes",
    )
    check(
        "legacy_topologies_not_active",
        "legacy_lanes_revision_17:" in texts["lanes"]
        and "legacy_lanes_revision_38:" in texts["lanes"]
        and texts["lanes"].index("lanes:\n")
        < texts["lanes"].index("legacy_lanes_revision_17:"),
        "active topology is concise and precedes both preserved legacy snapshots",
    )

    bottleneck_terms = (
        "implementation-complete",
        "physical process",
        "interventional",
        "selective instrument",
        "finite-shot",
    )
    for surface in ("start", "lanes", "program"):
        missing_terms = [
            term for term in bottleneck_terms if term not in texts[surface].lower()
        ]
        check(
            f"{surface}_bottleneck",
            not missing_terms,
            (
                f"{surface} carries the implementation-complete physical "
                f"interventional-sufficiency bottleneck; missing={missing_terms}"
            ),
        )

    check(
        "no_old_mode_lane_authority",
        "Lanes are organized by JOB / MODE" not in texts["agents"]
        and "Lanes are organized by JOB / MODE" not in lane_block,
        "current governance no longer presents method/mode lanes as active authority",
    )
    check(
        "forward_inverse_visible",
        "FORWARD / REPRESENTATION" in texts["start"]
        and "INVERSE / NORTH-STAR TEST" in texts["start"]
        and "## Whole-picture and inverse-test architecture" in texts["program"],
        "forward coherent picture and inverse adjudication are both explicit",
    )

    missing_links: list[str] = []
    link_count = 0
    for surface, path in FILES.items():
        for target in local_markdown_targets(path, texts[surface]):
            link_count += 1
            if not target.exists():
                missing_links.append(f"{surface}: {target}")
    check(
        "entrypoint_local_links",
        not missing_links,
        f"{link_count} local entrypoint links resolve; missing={missing_links}",
    )
    check(
        "orientation_link_depth",
        link_count >= 15,
        f"cold-start entrypoints expose a navigable local link surface; count={link_count}",
    )

    check(
        "historical_receipt_guard",
        "Do not edit dated receipts" in texts["start"]
        and "legacy_lanes_revision_38" in texts["lanes"],
        "historical work is preserved additively rather than retroactively rewritten",
    )
    check(
        "scientific_nonpromotion",
        "No scientific claim, theorem, hypothesis" in texts["lanes"],
        "revision receipt explicitly denies scientific promotion",
    )

    return {
        "probe": "du_agent_orientation_contract_probe",
        "status": "PASS",
        "scope": "governance_and_cold_start_orientation_only",
        "checks_passed": len(checks),
        "checks": checks,
        "disclaimer": (
            "Passing establishes entrypoint and routing consistency only; "
            "it establishes no scientific result."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
