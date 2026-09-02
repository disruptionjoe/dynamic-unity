#!/usr/bin/env python3
"""Exact finite controls for HC-DU-223.

Passing verifies only the frozen charge/flux factorization, strict compression,
upstream target/provenance leaks, and downstream write-preservation boundary.
It proves no new QED result, autonomous detector, material record, prediction,
or new physics.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_dirac_maxwell_charge_flux_constraint_witness_result.json"
)


@dataclass(frozen=True)
class Completion:
    charge: int
    spin: str
    distribution: str
    provenance: str
    crossings: tuple[int, ...]


CHARGE_HISTORIES = {
    -2: ((-1, -1), (-1, 1, -1, -1)),
    -1: ((-1,), (-1, 1, -1)),
    0: ((), (1, -1)),
    1: ((1,), (1, -1, 1)),
    2: ((1, 1), (1, -1, 1, 1)),
}


COMPLETIONS = tuple(
    Completion(charge, spin, distribution, provenance, crossings)
    for charge, history_options in CHARGE_HISTORIES.items()
    for crossings in history_options
    for spin in ("up", "down")
    for distribution in ("left", "right")
    for provenance in ("preloaded", "transported")
)


def noether_charge(item: Completion) -> int:
    return item.charge


def gauss_flux(item: Completion) -> int:
    # Natural units and a fixed outward orientation: Phi = Q.
    return item.charge


def calibrated_write(item: Completion) -> int:
    return gauss_flux(item)


def magnitude_only_write(item: Completion) -> int:
    return abs(gauss_flux(item))


def factors_through(
    domain: Iterable[Completion],
    view: Callable[[Completion], Hashable],
    target: Callable[[Completion], Hashable],
) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for item in domain:
        key = view(item)
        value = target(item)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def witness(
    domain: Iterable[Completion],
    view: Callable[[Completion], Hashable],
    target: Callable[[Completion], Hashable],
) -> tuple[Completion, Completion] | None:
    items = tuple(domain)
    for index, left in enumerate(items):
        for right in items[index + 1 :]:
            if view(left) == view(right) and target(left) != target(right):
                return left, right
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    charge_through_current = factors_through(
        COMPLETIONS, noether_charge, lambda item: item.charge
    )
    charge_through_flux = factors_through(
        COMPLETIONS, gauss_flux, lambda item: item.charge
    )
    charge_through_calibrated_write = factors_through(
        COMPLETIONS, calibrated_write, lambda item: item.charge
    )
    charge_through_magnitude_write = factors_through(
        COMPLETIONS, magnitude_only_write, lambda item: item.charge
    )

    spin_leak = witness(COMPLETIONS, gauss_flux, lambda item: item.spin)
    distribution_leak = witness(
        COMPLETIONS, gauss_flux, lambda item: item.distribution
    )
    provenance_leak = witness(
        COMPLETIONS, gauss_flux, lambda item: item.provenance
    )
    crossing_leak = witness(COMPLETIONS, gauss_flux, lambda item: item.crossings)
    magnitude_leak = witness(
        COMPLETIONS, magnitude_only_write, lambda item: item.charge
    )

    flux_classes = {gauss_flux(item) for item in COMPLETIONS}
    completion_classes = set(COMPLETIONS)

    checks = [
        (
            "every crossing history has the declared net charge",
            all(sum(item.crossings) == item.charge for item in COMPLETIONS),
        ),
        ("charge factors through action-selected current", charge_through_current),
        ("charge factors through Gauss boundary flux", charge_through_flux),
        (
            "charge response is strictly compressive",
            len(flux_classes) < len(completion_classes),
        ),
        ("spin leaks upstream of charge response", spin_leak is not None),
        (
            "interior distribution leaks upstream of charge response",
            distribution_leak is not None,
        ),
        (
            "provenance leaks upstream of endpoint response",
            provenance_leak is not None,
        ),
        (
            "crossing history leaks upstream of endpoint response",
            crossing_leak is not None,
        ),
        (
            "calibrated identity write preserves charge target",
            charge_through_calibrated_write,
        ),
        (
            "magnitude-only write loses charge sign",
            not charge_through_magnitude_write and magnitude_leak is not None,
        ),
        (
            "constraint witness does not identify occurrence",
            provenance_leak is not None,
        ),
    ]

    result = {
        "claim_id": "HC-DU-223",
        "run_id": "RUN-20260902-dirac-maxwell-charge-flux-constraint-witness",
        "domain": {
            "completion_count": len(COMPLETIONS),
            "charge_flux_class_count": len(flux_classes),
            "strictly_compressive": len(flux_classes) < len(COMPLETIONS),
        },
        "factorization": {
            "charge_through_noether_current": charge_through_current,
            "charge_through_gauss_flux": charge_through_flux,
            "charge_through_calibrated_write": charge_through_calibrated_write,
            "charge_through_magnitude_only_write": charge_through_magnitude_write,
        },
        "first_leaks": {
            "spin": [asdict(item) for item in spin_leak] if spin_leak else None,
            "interior_distribution": (
                [asdict(item) for item in distribution_leak]
                if distribution_leak
                else None
            ),
            "provenance": (
                [asdict(item) for item in provenance_leak]
                if provenance_leak
                else None
            ),
            "crossing_history": (
                [asdict(item) for item in crossing_leak]
                if crossing_leak
                else None
            ),
            "magnitude_only_write": (
                [asdict(item) for item in magnitude_leak]
                if magnitude_leak
                else None
            ),
        },
        "checks": [
            {"name": name, "passed": passed} for name, passed in checks
        ],
        "passed": sum(passed for _, passed in checks),
        "total": len(checks),
        "verdict": (
            "ACTION_SELECTED_CHARGE_RESPONSE + COMPRESSIVE_TARGET_SUFFICIENCY "
            "+ GAUSS_CONSTRAINT_WITNESS + UPSTREAM_MICROSTATE_AND_PROVENANCE_LEAK "
            "+ CALIBRATED_WRITE_CAN_PRESERVE_TARGET "
            "+ DOWNSTREAM_WRITE_CAN_DESTROY_SUFFICIENCY "
            "+ CONSTRAINT_WITNESS_IS_NOT_MATERIAL_RECORD + NO_READY_SUCCESSOR"
        ),
        "maximum_grade": (
            "Scoped Grade 4 exact typed composition and first-leak localization; "
            "no new QED theorem, autonomous material record, empirical excess, "
            "prediction, or new physics"
        ),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"checks: {result['passed']}/{result['total']}")
    print(f"verdict: {result['verdict']}")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
