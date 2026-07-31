#!/usr/bin/env python3
"""Exact finite controls for HC-DU-176.

The probe checks only partition/factorization and target-relative persistence
facts behind the stage–resource–persistence separation result. Passing does
not select a physical stage, symmetry resource, material archive, observer,
causal-response functional, dynamics, ontology, or empirical prediction.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_stage_resource_persistence_separation_result.json"
)

History = tuple[int, ...]
Value = Hashable


def kernel(
    histories: tuple[History, ...],
    mapping: dict[History, Value],
) -> set[tuple[History, History]]:
    return {
        (left, right)
        for left in histories
        for right in histories
        if mapping[left] == mapping[right]
    }


def sufficient(
    histories: tuple[History, ...],
    record: dict[History, Value],
    target: dict[History, Value],
) -> bool:
    return kernel(histories, record) <= kernel(histories, target)


def assignment(
    histories: tuple[History, ...],
    values: Iterable[Value],
) -> dict[History, Value]:
    return dict(zip(histories, values, strict=True))


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    histories: tuple[History, ...] = tuple(
        itertools.product((0, 1), repeat=2)
    )
    stage = {history: history[0] for history in histories}
    character = {history: history[1] for history in histories}
    joint = {history: history for history in histories}

    # Exhaustively check the typed conjunction theorem over every labelled
    # four-output record. Repeated assignments include every partition, with
    # harmless label redundancy.
    assignment_count = 0
    conjunction_equivalence = True
    for values in itertools.product(range(4), repeat=len(histories)):
        record = assignment(histories, values)
        joint_ok = sufficient(histories, record, joint)
        component_ok = sufficient(histories, record, stage) and sufficient(
            histories, record, character
        )
        conjunction_equivalence = conjunction_equivalence and (
            joint_ok == component_ok
        )
        assignment_count += 1
    checks.append(
        {
            "name": "joint_kernel_criterion_equals_component_conjunction",
            "passed": conjunction_equivalence and assignment_count == 256,
            "assignments_checked": assignment_count,
        }
    )

    # Stage and persistence can be present while the relational-character
    # target is omitted.
    stage_archive = dict(stage)
    checks.append(
        {
            "name": "stage_plus_persistence_does_not_imply_character",
            "passed": sufficient(histories, stage_archive, stage)
            and not sufficient(histories, stage_archive, character)
            and not sufficient(histories, stage_archive, joint),
        }
    )

    # A pre-existing stable relational resource can persist while carrying no
    # formation-stage provenance.
    character_archive = dict(character)
    checks.append(
        {
            "name": "character_plus_persistence_does_not_imply_stage",
            "passed": sufficient(histories, character_archive, character)
            and not sufficient(histories, character_archive, stage)
            and not sufficient(histories, character_archive, joint),
        }
    )

    # The complete distinction can exist at a marked intermediate stage and
    # be erased from the declared horizon archive.
    intermediate_archive = dict(joint)
    erased_horizon = {history: 0 for history in histories}
    checks.append(
        {
            "name": "stage_plus_character_does_not_imply_horizon_persistence",
            "passed": sufficient(histories, intermediate_archive, joint)
            and not sufficient(histories, erased_horizon, joint),
        }
    )

    # The supplied all-three architecture is the exact positive control.
    retained_joint_archive = dict(joint)
    checks.append(
        {
            "name": "supplied_stage_character_persistence_positive_control",
            "passed": sufficient(histories, retained_joint_archive, joint),
            "horizon_classes": len(set(retained_joint_archive.values())),
        }
    )

    # This ordinary marked classical record is exact for its invariant
    # occurrence target and needs no nontrivial character resource. It kills
    # the universal form of the proposed ladder.
    ordinary_target = dict(stage)
    ordinary_record = dict(stage)
    checks.append(
        {
            "name": "symmetry_resource_is_not_universal_record_requirement",
            "passed": sufficient(histories, ordinary_record, ordinary_target)
            and not sufficient(histories, ordinary_record, character),
        }
    )

    # Persistence is target-relative rather than global injectivity. Erasing
    # a nuisance coordinate is harmless when the declared target survives.
    rich_histories: tuple[History, ...] = tuple(
        itertools.product((0, 1), repeat=3)
    )
    rich_target = {
        history: (history[0], history[1]) for history in rich_histories
    }
    rich_stage_archive = {history: history for history in rich_histories}
    nuisance_erased_horizon = dict(rich_target)
    checks.append(
        {
            "name": "noninjective_horizon_map_can_preserve_target",
            "passed": sufficient(
                rich_histories,
                rich_stage_archive,
                rich_target,
            )
            and sufficient(
                rich_histories,
                nuisance_erased_horizon,
                rich_target,
            )
            and len(set(nuisance_erased_horizon.values()))
            < len(set(rich_stage_archive.values())),
            "stage_classes": len(set(rich_stage_archive.values())),
            "horizon_classes": len(set(nuisance_erased_horizon.values())),
        }
    )

    # Merging distinct target classes is exactly the persistence failure.
    parity_horizon = {
        history: history[0] ^ history[1] for history in rich_histories
    }
    checks.append(
        {
            "name": "merging_target_classes_kills_persistence",
            "passed": not sufficient(
                rich_histories,
                parity_horizon,
                rich_target,
            ),
            "horizon_classes": len(set(parity_horizon.values())),
            "target_classes": len(set(rich_target.values())),
        }
    )

    # A persistent preloaded bit is not a record of whether a write occurred:
    # stale and freshly written histories share the same terminal value.
    write_histories: tuple[History, ...] = ((0, 1), (1, 1))
    write_occurred = {
        write_histories[0]: 0,
        write_histories[1]: 1,
    }
    terminal_value = {
        write_histories[0]: 1,
        write_histories[1]: 1,
    }
    checks.append(
        {
            "name": "persistent_terminal_value_does_not_certify_formation",
            "passed": not sufficient(
                write_histories,
                terminal_value,
                write_occurred,
            ),
        }
    )

    # Verify target-relative persistence equivalence exhaustively for every
    # horizon relabelling of an exact stage archive.
    persistence_equivalence = True
    persistence_assignments = 0
    for values in itertools.product(range(4), repeat=len(histories)):
        horizon = assignment(histories, values)
        direct = sufficient(histories, horizon, joint)
        target_class_preserved = all(
            horizon[left] != horizon[right]
            for left in histories
            for right in histories
            if joint[left] != joint[right]
        )
        persistence_equivalence = persistence_equivalence and (
            direct == target_class_preserved
        )
        persistence_assignments += 1
    checks.append(
        {
            "name": "target_relative_persistence_equivalence",
            "passed": persistence_equivalence
            and persistence_assignments == 256,
            "assignments_checked": persistence_assignments,
        }
    )

    passed = all(bool(check["passed"]) for check in checks)
    result: dict[str, object] = {
        "claim_id": "HC-DU-176",
        "passed": passed,
        "check_count": len(checks),
        "checks": checks,
        "earned": {
            "joint_record_criterion": (
                "ker(record) subset ker(stage) intersection ker(character)"
            ),
            "persistence_criterion": (
                "the horizon map may erase nuisance detail but may not merge "
                "declared target classes"
            ),
            "independence": (
                "stage, nontrivial relational resource, and persistence are "
                "logically independent target conditions in this abstract fixture"
            ),
            "universal_ladder": (
                "not licensed by the three differently scoped typed results"
            ),
        },
        "not_earned": [
            "physical stage selection",
            "symmetry-resource selection",
            "material archive selection",
            "common causal response object",
            "hyperbolic dynamics",
            "observer or finality selection",
            "new physics or empirical excess",
            "independent physical realizability of all three conditions",
        ],
    }
    return result


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
