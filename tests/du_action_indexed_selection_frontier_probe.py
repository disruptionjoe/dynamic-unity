#!/usr/bin/env python3
"""Exact finite controls for HC-DU-160.

Passing proves only the declared finite candidate-key antichains and the
two qubit measurement-model deletion witnesses. It establishes no universal
physical selector, formed record, observer, ontology, new physics, prediction,
or empirical result.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Hashable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_action_indexed_selection_frontier_result.json"

Completion = tuple[int, int]
Coordinate = Callable[[Completion], Hashable]
Matrix = tuple[Fraction, Fraction, Fraction, Fraction]


def powerset(names: tuple[str, ...]) -> list[tuple[str, ...]]:
    return [
        subset
        for size in range(len(names) + 1)
        for subset in itertools.combinations(names, size)
    ]


def selects(
    completions: tuple[Completion, ...],
    coordinates: dict[str, Coordinate],
    subset: tuple[str, ...],
    target: Coordinate,
) -> bool:
    for left in completions:
        for right in completions:
            same_antecedent = all(
                coordinates[name](left) == coordinates[name](right)
                for name in subset
            )
            if same_antecedent and target(left) != target(right):
                return False
    return True


def minimal_selectors(
    selecting: list[tuple[str, ...]],
) -> list[tuple[str, ...]]:
    return [
        subset
        for subset in selecting
        if not any(set(other) < set(subset) for other in selecting)
    ]


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(a + b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def scale(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(value * item for item in matrix)  # type: ignore[return-value]


def z_pointer_instrument(rho: Matrix) -> tuple[Matrix, Matrix]:
    a, _, _, d = rho
    return (a, Fraction(0), Fraction(0), Fraction(0)), (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        d,
    )


def x_pointer_instrument(rho: Matrix) -> tuple[Matrix, Matrix]:
    a, b, c, d = rho
    return scale(Fraction(1, 2), rho), (
        a / 2,
        -b / 2,
        -c / 2,
        d / 2,
    )


def phase_isometry_z_pointer_instrument(rho: Matrix) -> tuple[Matrix, Matrix]:
    """Instrument from V=(I⊗|0>+Z⊗|1>)/sqrt(2) and a Z pointer PVM."""
    a, b, c, d = rho
    return scale(Fraction(1, 2), rho), (
        a / 2,
        -b / 2,
        -c / 2,
        d / 2,
    )


def trace(matrix: Matrix) -> Fraction:
    return matrix[0] + matrix[3]


def serial_matrix(matrix: Matrix) -> list[str]:
    return [str(item) for item in matrix]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    completions = tuple(itertools.product((0, 1), repeat=2))
    coordinate_names = ("b", "c", "w")
    coordinates: dict[str, Coordinate] = {
        "b": lambda item: item[0],
        "c": lambda item: item[1],
        "w": lambda item: item[0] ^ item[1],
    }
    targets: dict[str, Coordinate] = {
        "no_access": lambda _: 0,
        "outcome_access": lambda item: item[0],
        "audit_access": lambda item: item,
    }

    frontiers: dict[str, list[tuple[str, ...]]] = {}
    selecting_families: dict[str, list[tuple[str, ...]]] = {}
    all_subsets = powerset(coordinate_names)
    for name, target in targets.items():
        selecting = [
            subset
            for subset in all_subsets
            if selects(completions, coordinates, subset, target)
        ]
        selecting_families[name] = selecting
        frontiers[name] = minimal_selectors(selecting)

    expected_frontiers = {
        "no_access": [()],
        "outcome_access": [("b",), ("c", "w")],
        "audit_access": [("b", "c"), ("b", "w"), ("c", "w")],
    }

    states: dict[str, Matrix] = {
        "zero": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "one": (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
        "plus": (
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1, 2),
        ),
        "mixed": (
            Fraction(2, 3),
            Fraction(1, 6),
            Fraction(1, 6),
            Fraction(1, 3),
        ),
    }

    same_unlabelled = True
    pointer_changes_instrument = False
    isometry_changes_instrument = False
    specimen: dict[str, object] = {}
    for name, rho in states.items():
        z_outputs = z_pointer_instrument(rho)
        x_outputs = x_pointer_instrument(rho)
        phase_outputs = phase_isometry_z_pointer_instrument(rho)
        same_unlabelled &= add(*z_outputs) == add(*x_outputs)
        pointer_changes_instrument |= z_outputs != x_outputs
        isometry_changes_instrument |= (
            z_outputs != phase_outputs
            and add(*z_outputs) == add(*phase_outputs)
        )
        specimen[name] = {
            "z_pointer_probabilities": [str(trace(item)) for item in z_outputs],
            "x_pointer_probabilities": [str(trace(item)) for item in x_outputs],
            "copy_unlabelled": serial_matrix(add(*z_outputs)),
            "phase_isometry_unlabelled": serial_matrix(add(*phase_outputs)),
        }

    selecting_sets = {
        name: {frozenset(item) for item in family}
        for name, family in selecting_families.items()
    }
    action_refinement_antitone = (
        selecting_sets["audit_access"]
        <= selecting_sets["outcome_access"]
        <= selecting_sets["no_access"]
    )

    checks = {
        "frontiers_exact": frontiers == expected_frontiers,
        "selecting_families_upper_closed": all(
            not selects(completions, coordinates, lower, target)
            or selects(completions, coordinates, upper, target)
            for target in targets.values()
            for lower in all_subsets
            for upper in all_subsets
            if set(lower) <= set(upper)
        ),
        "action_refinement_antitone": action_refinement_antitone,
        "same_copy_isometry_different_pointer_same_unlabelled_channel": (
            same_unlabelled and pointer_changes_instrument
        ),
        "same_z_pointer_different_isometry_same_unlabelled_channel": (
            isometry_changes_instrument
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"action-indexed selection-frontier checks failed: {failed}")

    result = {
        "probe": "du_action_indexed_selection_frontier_probe",
        "status": "PASS",
        "claim_id": "HC-DU-160",
        "scope": "finite_action_indexed_frontier_and_qubit_measurement_model_controls",
        "frontiers": {
            name: [list(item) for item in values]
            for name, values in frontiers.items()
        },
        "selecting_bundle_counts": {
            name: len(values) for name, values in selecting_families.items()
        },
        "qubit_specimen": specimen,
        "checks": checks,
        "disclaimer": (
            "Passing establishes only the exact finite controls; it establishes "
            "no universal physical selector, formed record, ontology, new "
            "physics, prediction, or empirical result."
        ),
    }
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
