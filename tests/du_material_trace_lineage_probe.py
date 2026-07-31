#!/usr/bin/env python3
"""Exact finite controls for the HC-DU-179 material-trace lineage boundary.

The probe distinguishes a retained set of marked detector sites from a
partition of those sites into source paths and from an orientation of those
paths. Passing proves only finite factorization and path-cover facts. It does
not model nuclear-emulsion chemistry, select a physical track, identify a
particle, establish an event time, or supply new physics.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_material_trace_lineage_result.json"

Vertex = int
Edge = frozenset[Vertex]
Matching = frozenset[Edge]


def perfect_matchings(
    vertices: frozenset[Vertex],
    allowed_edges: frozenset[Edge],
) -> frozenset[Matching]:
    """Enumerate perfect matchings of a finite simple graph exactly."""

    if not vertices:
        return frozenset({frozenset()})

    first = min(vertices)
    results: set[Matching] = set()
    for edge in allowed_edges:
        if first not in edge or len(edge) != 2:
            continue
        second = next(vertex for vertex in edge if vertex != first)
        if second not in vertices:
            continue
        remainder = vertices - edge
        for submatching in perfect_matchings(remainder, allowed_edges):
            results.add(frozenset({edge}) | submatching)
    return frozenset(results)


def kernel_sufficient(
    histories: tuple[str, ...],
    record: dict[str, object],
    target: dict[str, object],
) -> bool:
    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in histories
        for right in histories
    )


def run_probe() -> dict[str, object]:
    vertices = frozenset({0, 1, 2, 3})

    # The cycle C4 is the smallest occupied-site graph with two distinct
    # perfect path covers: horizontal and vertical pairings of one square.
    cycle_edges = frozenset(
        {
            frozenset({0, 1}),
            frozenset({1, 2}),
            frozenset({2, 3}),
            frozenset({3, 0}),
        }
    )
    cycle_matchings = perfect_matchings(vertices, cycle_edges)
    matching_labels = tuple(
        sorted(
            (
                tuple(
                    sorted(tuple(sorted(edge)) for edge in matching)
                )
                for matching in cycle_matchings
            )
        )
    )
    history_names = ("cover_a", "cover_b")
    material_record = {name: tuple(sorted(vertices)) for name in history_names}
    lineage_target = {
        name: matching_labels[index]
        for index, name in enumerate(history_names)
    }

    checks: list[dict[str, object]] = []
    checks.append(
        {
            "name": "c4_has_two_admissible_path_covers",
            "passed": len(cycle_matchings) == 2,
            "matching_count": len(cycle_matchings),
        }
    )
    checks.append(
        {
            "name": "same_marked_grains_different_lineage",
            "passed": material_record["cover_a"] == material_record["cover_b"]
            and lineage_target["cover_a"] != lineage_target["cover_b"],
        }
    )
    checks.append(
        {
            "name": "occupancy_record_does_not_factor_lineage",
            "passed": not kernel_sufficient(
                history_names,
                material_record,
                lineage_target,
            ),
        }
    )

    # The material marks still exactly record which local sites were altered.
    local_mark_target = dict(material_record)
    checks.append(
        {
            "name": "material_trace_factors_local_mark_pattern",
            "passed": kernel_sufficient(
                history_names,
                material_record,
                local_mark_target,
            ),
        }
    )

    # A physically retained edge tag is the exact provenance repair.
    edge_tagged_record = dict(lineage_target)
    checks.append(
        {
            "name": "edge_tag_repairs_lineage_factorization",
            "passed": kernel_sufficient(
                history_names,
                edge_tagged_record,
                lineage_target,
            ),
        }
    )

    # A restricted admissibility class can repair uniqueness without adding a
    # new record field. Removing one cycle edge leaves a path graph P4 with one
    # perfect matching.
    path_edges = cycle_edges - {frozenset({3, 0})}
    path_matchings = perfect_matchings(vertices, path_edges)
    checks.append(
        {
            "name": "unique_path_cover_is_conditional_on_admissibility",
            "passed": len(path_matchings) == 1,
            "matching_count": len(path_matchings),
        }
    )

    # A time-insensitive trace carries an undirected segment, not an arrow.
    direction_histories = ("zero_to_one", "one_to_zero")
    unordered_segment = {
        history: frozenset({0, 1}) for history in direction_histories
    }
    direction_target = {
        "zero_to_one": (0, 1),
        "one_to_zero": (1, 0),
    }
    checks.append(
        {
            "name": "time_insensitive_segment_does_not_factor_direction",
            "passed": not kernel_sufficient(
                direction_histories,
                unordered_segment,
                direction_target,
            ),
        }
    )
    ordered_record = dict(direction_target)
    checks.append(
        {
            "name": "ordered_endpoint_tag_repairs_direction",
            "passed": kernel_sufficient(
                direction_histories,
                ordered_record,
                direction_target,
            ),
        }
    )

    # Deterministic development or scanning of the same latent point field
    # cannot recover a target already varying inside its fibre.
    developed_record = {
        history: ("developed", material_record[history])
        for history in history_names
    }
    checks.append(
        {
            "name": "downstream_deterministic_readout_cannot_restore_lineage",
            "passed": not kernel_sufficient(
                history_names,
                developed_record,
                lineage_target,
            ),
        }
    )

    passed = all(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-179",
        "passed": passed,
        "check_count": len(checks),
        "checks": checks,
        "earned": {
            "material_positive": (
                "a marked-site field can exactly retain the local material "
                "trace target"
            ),
            "lineage_boundary": (
                "site occupancy does not determine a source-path partition "
                "when multiple admissible path covers exist"
            ),
            "direction_boundary": (
                "an unordered time-insensitive segment does not determine its "
                "temporal orientation"
            ),
            "repairs": (
                "retain edge/order tags or independently restrict the physical "
                "admissibility class until the path cover is unique"
            ),
        },
        "not_earned": [
            "nuclear-emulsion chemistry",
            "physical existence of the finite C4 specimen",
            "particle or source identity",
            "event time",
            "track direction",
            "selected readout or archive",
            "new physics or empirical excess",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the canonical JSON regression artifact",
    )
    args = parser.parse_args()

    result = run_probe()
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.write_artifact:
        ARTIFACT.write_text(rendered + "\n", encoding="utf-8")
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
