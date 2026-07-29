#!/usr/bin/env python3
"""Proportional controls for HC-DU-107.

The scientific result is analytic. This probe preserves:

1. the regular-tetrahedron detector geometry;
2. the uniform lower-Lipschitz bound on the frozen compact event region;
3. deterministic point-separation controls; and
4. exact same-record/different-event witnesses when detector clock offsets
   are allowed to refit.

Passing establishes no nonlinear interaction, source formation, event
association, detector selection, calibrated clock, retained record,
Lorentzian reconstruction, new physics, prediction, or evidence grade.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_tetrahedral_interaction_arrival_localization_result.json"
)

Event = tuple[float, float, float, float]
Vector3 = tuple[float, float, float]


SIGNS: tuple[tuple[int, int, int], ...] = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def vertices() -> tuple[Vector3, ...]:
    scale = 1.0 / math.sqrt(3.0)
    return tuple(
        tuple(scale * coordinate for coordinate in sign)  # type: ignore[misc]
        for sign in SIGNS
    )


def detectors(radius: float) -> tuple[Vector3, ...]:
    return tuple(
        tuple(-radius * coordinate for coordinate in vertex)  # type: ignore[misc]
        for vertex in vertices()
    )


def norm(values: tuple[float, ...]) -> float:
    return math.sqrt(sum(value * value for value in values))


def subtract(left: tuple[float, ...], right: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def arrivals(
    event: Event,
    radius: float,
    offsets: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
) -> tuple[float, float, float, float]:
    time = event[0]
    position = event[1:]
    return tuple(
        time
        + norm(subtract(position, detector))
        + offset
        for detector, offset in zip(detectors(radius), offsets, strict=True)
    )


def lower_margin(radius: float, event_radius: float) -> float:
    center_sigma_min = 2.0 / math.sqrt(3.0)
    perturbation_bound = 4.0 * event_radius / (radius - event_radius)
    return center_sigma_min - perturbation_bound


def close(left: tuple[float, ...], right: tuple[float, ...]) -> bool:
    return all(
        math.isclose(a, b, rel_tol=0.0, abs_tol=1.0e-12)
        for a, b in zip(left, right, strict=True)
    )


def main() -> None:
    radius = 20.0
    event_radius = radius / 20.0
    margin = lower_margin(radius, event_radius)

    # Exact sign identities imply
    # J(0)^T J(0) = diag(4, 4/3, 4/3, 4/3).
    for spatial_axis in range(3):
        assert sum(sign[spatial_axis] for sign in SIGNS) == 0
    for left_axis in range(3):
        for right_axis in range(3):
            value = sum(
                sign[left_axis] * sign[right_axis] for sign in SIGNS
            )
            assert value == (4 if left_axis == right_axis else 0)

    assert math.isclose(
        margin,
        2.0 / math.sqrt(3.0) - 4.0 / 19.0,
        rel_tol=0.0,
        abs_tol=1.0e-15,
    )
    assert margin > 0.94

    # The proof is analytic; this finite set is only a deterministic
    # implementation regression over time and every spatial axis.
    events: tuple[Event, ...] = (
        (-0.5, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.5, 0.0, 0.0, 0.0),
        (0.0, event_radius, 0.0, 0.0),
        (0.0, -event_radius, 0.0, 0.0),
        (0.0, 0.0, event_radius, 0.0),
        (0.0, 0.0, -event_radius, 0.0),
        (0.0, 0.0, 0.0, event_radius),
        (0.0, 0.0, 0.0, -event_radius),
    )
    minimum_observed_ratio = float("inf")
    for first, second in combinations(events, 2):
        event_distance = norm(subtract(first, second))
        response_distance = norm(
            subtract(arrivals(first, radius), arrivals(second, radius))
        )
        ratio = response_distance / event_distance
        minimum_observed_ratio = min(minimum_observed_ratio, ratio)
        assert response_distance + 1.0e-12 >= margin * event_distance

    # Per-detector offset refit: every alternative event can reproduce the
    # same four arrival readings by changing the four clock offsets.
    reference: Event = (0.0, 0.0, 0.0, 0.0)
    alternative: Event = (0.02, 0.10, -0.08, 0.04)
    reference_record = arrivals(reference, radius)
    alternative_unshifted = arrivals(alternative, radius)
    refitted_offsets = tuple(
        observed - unshifted
        for observed, unshifted in zip(
            reference_record,
            alternative_unshifted,
            strict=True,
        )
    )
    assert reference != alternative
    assert close(
        reference_record,
        arrivals(alternative, radius, refitted_offsets),
    )

    # Even one common unknown clock offset confounds absolute event time.
    later: Event = (0.3, 0.0, 0.0, 0.0)
    common_offset = (-0.3, -0.3, -0.3, -0.3)
    assert close(reference_record, arrivals(later, radius, common_offset))

    result = {
        "claim_id": "HC-DU-107",
        "status": "PASS",
        "controls": {
            "detector_count": 4,
            "event_spacetime_dimension": 4,
            "detector_radius": radius,
            "event_region_radius": event_radius,
            "center_gram_diagonal": ["4", "4/3", "4/3", "4/3"],
            "center_sigma_min": 2.0 / math.sqrt(3.0),
            "jacobian_perturbation_bound": 4.0 / 19.0,
            "uniform_lower_lipschitz_margin": margin,
            "deterministic_event_count": len(events),
            "minimum_observed_pair_ratio": minimum_observed_ratio,
            "per_detector_offset_same_record_different_event": True,
            "common_offset_absolute_time_confounding": True,
        },
        "noise_corollary": (
            "If every arrival coordinate has absolute error at most epsilon, "
            "two compatible events are at most 4*epsilon/margin apart."
        ),
        "boundary": (
            "Regression only: no nonlinear interaction, source formation, "
            "event association, detector selection, calibrated clock, "
            "retained record, Lorentzian reconstruction, new physics, "
            "prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-107 controls: tetrahedral arrival localization margin "
        "and calibration counterexamples"
    )


if __name__ == "__main__":
    main()
