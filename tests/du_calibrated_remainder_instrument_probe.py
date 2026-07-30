#!/usr/bin/env python3
"""Exact finite controls for HC-DU-167's calibrated remainder instrument.

Passing establishes a finite identifiability theorem, its nested-envelope
calibration curve, and two counterexamples to a causal-direction
classification of reconstruction remainder. It establishes no physical
ontology, quantum result, empirical prediction, or scientific successor.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from itertools import product
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT / "tests" / "artifacts" / "du_calibrated_remainder_instrument_result.json"
)


@dataclass(frozen=True, order=True)
class World:
    render: int
    near_collision: int
    remote_collision: int
    nav_policy: int
    authority: int


WORLDS = tuple(World(*bits) for bits in product((0, 1), repeat=5))
COORDINATES = tuple(World.__dataclass_fields__)


def look(world: World) -> tuple[str, int]:
    """Downstream-only visual readout; the action does not alter the bit."""
    return ("render", world.render)


def push_near(world: World) -> tuple[str, int]:
    return ("near_blocked", world.near_collision)


def toggle_remote_state(world: World) -> World:
    return replace(world, remote_collision=1 - world.remote_collision)


def toggle_remote(world: World) -> tuple[str, int, int]:
    """An admitted remote action both reads and modifies this component."""
    changed = toggle_remote_state(world)
    return ("remote_before_after", world.remote_collision, changed.remote_collision)


def watch_npc(world: World) -> tuple[str, int]:
    return ("npc_route", world.nav_policy)


def force_conflict(world: World) -> tuple[str, int]:
    return ("authority_correction", world.authority)


ACTIONS: dict[str, Callable[[World], tuple[object, ...]]] = {
    "push_near": push_near,
    "look": look,
    "watch_npc": watch_npc,
    "toggle_remote": toggle_remote,
    "force_conflict": force_conflict,
}

ENVELOPES: dict[str, tuple[str, ...]] = {
    "near_capability": ("push_near",),
    "plus_visual": ("push_near", "look"),
    "plus_npc": ("push_near", "look", "watch_npc"),
    "plus_remote": ("push_near", "look", "watch_npc", "toggle_remote"),
    "complete": (
        "push_near",
        "look",
        "watch_npc",
        "toggle_remote",
        "force_conflict",
    ),
}


def signature(world: World, envelope: Iterable[str]) -> tuple[tuple[object, ...], ...]:
    return tuple(ACTIONS[action](world) for action in envelope)


def fibres(envelope: Iterable[str]) -> dict[tuple[tuple[object, ...], ...], tuple[World, ...]]:
    grouped: dict[tuple[tuple[object, ...], ...], list[World]] = {}
    for world in WORLDS:
        grouped.setdefault(signature(world, envelope), []).append(world)
    return {key: tuple(value) for key, value in grouped.items()}


def coordinate_is_reconstructed(coordinate: str, envelope: Iterable[str]) -> bool:
    return all(
        len({getattr(world, coordinate) for world in fibre}) == 1
        for fibre in fibres(envelope).values()
    )


def partition(envelope: Iterable[str]) -> frozenset[frozenset[World]]:
    return frozenset(frozenset(fibre) for fibre in fibres(envelope).values())


def refines(finer: frozenset[frozenset[World]], coarser: frozenset[frozenset[World]]) -> bool:
    return all(any(fine_block <= coarse_block for coarse_block in coarser) for fine_block in finer)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    checks: list[tuple[str, bool]] = []
    expected = {
        "near_capability": (2, 16, ("render", "remote_collision", "nav_policy", "authority")),
        "plus_visual": (4, 8, ("remote_collision", "nav_policy", "authority")),
        "plus_npc": (8, 4, ("remote_collision", "authority")),
        "plus_remote": (16, 2, ("authority",)),
        "complete": (32, 1, ()),
    }
    curve: dict[str, dict[str, object]] = {}

    for name, envelope in ENVELOPES.items():
        grouped = fibres(envelope)
        unresolved = tuple(
            coordinate
            for coordinate in COORDINATES
            if not coordinate_is_reconstructed(coordinate, envelope)
        )
        class_count = len(grouped)
        max_fibre = max(map(len, grouped.values()))
        expected_classes, expected_max_fibre, expected_unresolved = expected[name]
        checks.extend(
            [
                (f"{name}_class_count", class_count == expected_classes),
                (f"{name}_max_fibre", max_fibre == expected_max_fibre),
                (f"{name}_unresolved", unresolved == expected_unresolved),
            ]
        )
        curve[name] = {
            "actions": list(envelope),
            "equivalence_classes": class_count,
            "maximum_fibre_size": max_fibre,
            "unresolved_coordinates": list(unresolved),
        }

    ordered_names = tuple(ENVELOPES)
    for earlier, later in zip(ordered_names, ordered_names[1:]):
        checks.append(
            (
                f"nested_refinement_{earlier}_to_{later}",
                refines(partition(ENVELOPES[later]), partition(ENVELOPES[earlier])),
            )
        )

    # Repeating an unchanged deterministic query adds samples but no structural
    # distinction.
    repeated_near = ("push_near", "push_near", "push_near")
    checks.append(
        (
            "repetition_does_not_shrink_structural_fibre",
            partition(repeated_near) == partition(ENVELOPES["near_capability"]),
        )
    )

    # The render bit is downstream-only in this model, yet direct visual
    # access makes it constant on every certified-record fibre.
    checks.append(
        (
            "downstream_only_not_sufficient_for_remainder",
            coordinate_is_reconstructed("render", ENVELOPES["plus_visual"]),
        )
    )

    # The remote collision bit has a genuine state-changing intervention in
    # the full model, but remains unresolved while that action is outside the
    # current envelope.
    checks.append(
        (
            "action_coupled_not_sufficient_for_reconstruction",
            not coordinate_is_reconstructed(
                "remote_collision", ENVELOPES["plus_visual"]
            )
            and coordinate_is_reconstructed(
                "remote_collision", ENVELOPES["plus_remote"]
            ),
        )
    )
    checks.append(
        (
            "remote_action_is_state_changing_and_involutive",
            all(toggle_remote_state(world) != world for world in WORLDS)
            and all(
                toggle_remote_state(toggle_remote_state(world)) == world
                for world in WORLDS
            ),
        )
    )

    # A signed/authenticated render value cannot bind an independent collision
    # value. The same signed representation occurs in both action worlds.
    signed_render_twins = [
        world
        for world in WORLDS
        if world.render == 1
        and world.remote_collision in (0, 1)
        and world.near_collision == 0
        and world.nav_policy == 0
        and world.authority == 0
    ]
    checks.append(
        (
            "signed_render_does_not_bind_remote_collision",
            len(signed_render_twins) == 2
            and len({world.render for world in signed_render_twins}) == 1
            and len({world.remote_collision for world in signed_render_twins}) == 2,
        )
    )

    # Full source access is the calibration positive control.
    checks.append(
        (
            "complete_envelope_is_injective",
            len({signature(world, ENVELOPES["complete"]) for world in WORLDS})
            == len(WORLDS),
        )
    )

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    result = {
        "claim_id": "HC-DU-167",
        "run_id": "RUN-20260730-140913-calibrated-remainder-instrument",
        "status": "PASS",
        "world_count": len(WORLDS),
        "coordinate_count": len(COORDINATES),
        "checks_passed": len(checks),
        "calibration_curve": curve,
        "downstream_only_conjecture": "KILLED",
        "selected_remainder_criterion": (
            "A target lies outside the structural remainder exactly when it is "
            "constant on every fibre of the frozen action-observation signature."
        ),
        "example_world": asdict(WORLDS[-1]),
        "scientific_nonclaim": (
            "This exact finite control calibrates a reconstruction method. It "
            "establishes no game-engine ontology, quantum result, physical "
            "record selector, empirical prediction, or scientific successor."
        ),
    }

    if args.write_artifact:
        ARTIFACT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(
        "PASS:",
        f"{len(checks)}/{len(checks)} checks;",
        "32-world calibration curve 2->4->8->16->32;",
        "downstream-only conjecture killed",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
