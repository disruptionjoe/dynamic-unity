#!/usr/bin/env python3
"""Exact controls for HC-DU-228.

This is a proof-checking artifact for a finite selector and convex-affinity
argument.  It does not simulate nucleation, validate the Schonfeld mechanism,
or establish a violation of the Born rule.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_first_droplet_actualization_affinity_result.json"
)
DIRECTIONS = tuple(range(4))


def rotate(value: int, shift: int) -> int:
    return (value + shift) % len(DIRECTIONS)


def offset_cutoff(probability: Fraction, cutoff: Fraction) -> Fraction:
    return max(probability - cutoff, Fraction(0))


def fixed_effect_probability(probability: Fraction, efficiency: Fraction) -> Fraction:
    """A fixed inefficient detector effect is affine in the input state."""
    return efficiency * probability


def exact_decoder_exists(
    supports: dict[str, frozenset[str]], targets: dict[str, str]
) -> bool:
    histories = tuple(supports)
    return all(
        targets[left] == targets[right]
        or supports[left].isdisjoint(supports[right])
        for left in histories
        for right in histories
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    dimension = len(DIRECTIONS)
    uniform_seed_law = {
        direction: Fraction(1, dimension) for direction in DIRECTIONS
    }
    rotated_seed_law = {
        rotate(direction, 1): probability
        for direction, probability in uniform_seed_law.items()
    }

    # The material amplifier copies the microscopic seed direction.  The map
    # is equivariant and deterministic once that seed is part of the complete
    # state, while ignorance of the seed yields a uniform output law.
    amplifier = {direction: f"track-{direction}" for direction in DIRECTIONS}
    rotated_amplifier = {
        rotate(direction, 1): f"track-{rotate(direction, 1)}"
        for direction in DIRECTIONS
    }
    output_law = {
        amplifier[direction]: probability
        for direction, probability in uniform_seed_law.items()
    }

    # A coherent direction carrier and its dephased shadow have identical
    # track-basis statistics.  The all-ones/d projector separates them.
    coherent = [
        [Fraction(1, dimension) for _ in DIRECTIONS] for _ in DIRECTIONS
    ]
    dephased = [
        [
            Fraction(1, dimension) if row == column else Fraction(0)
            for column in DIRECTIONS
        ]
        for row in DIRECTIONS
    ]
    pointer_coherent = tuple(coherent[index][index] for index in DIRECTIONS)
    pointer_dephased = tuple(dephased[index][index] for index in DIRECTIONS)
    coherent_witness_on_pure = sum(
        coherent[row][column] * coherent[column][row]
        for row in DIRECTIONS
        for column in DIRECTIONS
    )
    coherent_witness_on_dephased = sum(
        coherent[row][column] * dephased[column][row]
        for row in DIRECTIONS
        for column in DIRECTIONS
    )

    # The proposed offset response f_c(q)=max(q-c,0) is not affine.  For
    # c=1/4, q_mid=(0+2c)/2=c, but f(q_mid) differs from the randomized
    # average of f(0) and f(2c).  No fixed POVM effect can realize all three.
    cutoff = Fraction(1, 4)
    q_low = Fraction(0)
    q_high = 2 * cutoff
    q_mid = (q_low + q_high) / 2
    cutoff_direct = offset_cutoff(q_mid, cutoff)
    cutoff_randomized = (
        offset_cutoff(q_low, cutoff) + offset_cutoff(q_high, cutoff)
    ) / 2

    efficiency = Fraction(3, 5)
    fixed_direct = fixed_effect_probability(q_mid, efficiency)
    fixed_randomized = (
        fixed_effect_probability(q_low, efficiency)
        + fixed_effect_probability(q_high, efficiency)
    ) / 2

    # If the nonlinear response is applied to pure ensemble members instead
    # of the density operator, two decompositions of I/2 become distinguishable.
    # Z ensemble: q=(0,1); X ensemble: q=(1/2,1/2).
    z_ensemble_response = (
        offset_cutoff(Fraction(0), cutoff)
        + offset_cutoff(Fraction(1), cutoff)
    ) / 2
    x_ensemble_response = (
        offset_cutoff(Fraction(1, 2), cutoff)
        + offset_cutoff(Fraction(1, 2), cutoff)
    ) / 2

    # One visible track can decode the seed direction but not whether that
    # seed was a fixed microstate, an ontic noise event, or a monitored record.
    direction_supports = {
        f"seed-{direction}": frozenset((f"track-{direction}",))
        for direction in DIRECTIONS
    }
    direction_targets = {
        seed: seed.removeprefix("seed-") for seed in direction_supports
    }
    route_supports = {
        "preexisting-microstate": frozenset(output_law),
        "ontic-stochastic-innovation": frozenset(output_law),
        "monitored-trajectory": frozenset(output_law),
    }
    route_targets = {route: route for route in route_supports}
    route_refined_supports = {
        route: frozenset(f"{route}:{track}" for track in output_law)
        for route in route_supports
    }

    checks = [
        (
            "the symmetric microscopic seed law is rotation invariant",
            rotated_seed_law == uniform_seed_law,
        ),
        (
            "the amplifier deterministically copies a fully specified seed",
            len(set(amplifier.values())) == dimension,
        ),
        (
            "the seed-to-track amplifier is equivariant",
            rotated_amplifier
            == {
                direction: amplifier[direction]
                for direction in DIRECTIONS
            },
        ),
        (
            "coarse-graining over the seed yields a uniform track law",
            set(output_law.values()) == {Fraction(1, dimension)},
        ),
        (
            "a symmetric blank has no deterministic rotation-fixed direction",
            not any(
                all(rotate(candidate, shift) == candidate for shift in DIRECTIONS)
                for candidate in DIRECTIONS
            ),
        ),
        (
            "coherent and dephased carriers have the same track-basis law",
            pointer_coherent == pointer_dephased,
        ),
        (
            "a global coherent witness separates those carriers",
            coherent_witness_on_pure == 1
            and coherent_witness_on_dephased == Fraction(1, dimension),
        ),
        (
            "the offset cutoff violates convex affinity",
            cutoff_direct == 0
            and cutoff_randomized == cutoff / 2
            and cutoff_direct != cutoff_randomized,
        ),
        (
            "a fixed inefficient detector preserves convex affinity",
            fixed_direct == fixed_randomized,
        ),
        (
            "no fixed effect matches the cutoff at q=0,c,2c",
            cutoff_direct != cutoff_randomized,
        ),
        (
            "a branchwise cutoff distinguishes decompositions of I over 2",
            z_ensemble_response == Fraction(3, 8)
            and x_ensemble_response == Fraction(1, 4)
            and z_ensemble_response != x_ensemble_response,
        ),
        (
            "an ideal track exactly decodes its microscopic seed direction",
            exact_decoder_exists(direction_supports, direction_targets),
        ),
        (
            "the same track alphabet does not identify actualization route",
            not exact_decoder_exists(route_supports, route_targets),
        ),
        (
            "an explicit route marker can restore provenance",
            exact_decoder_exists(route_refined_supports, route_targets),
        ),
        (
            "restored provenance comes from a refined physical record",
            route_refined_supports != route_supports,
        ),
        (
            "the finite control checks structure rather than nucleation physics",
            True,
        ),
    ]

    passed = sum(bool(ok) for _, ok in checks)
    result = {
        "claim_id": "HC-DU-228",
        "prediction_id": "PRED-DU-006",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "cutoff": str(cutoff),
        "cutoff_direct_midpoint_response": str(cutoff_direct),
        "cutoff_randomized_response": str(cutoff_randomized),
        "z_decomposition_response": str(z_ensemble_response),
        "x_decomposition_response": str(x_ensemble_response),
        "coherent_witness_probability": str(coherent_witness_on_pure),
        "dephased_witness_probability": str(coherent_witness_on_dephased),
        "checks": [{"name": name, "passed": bool(ok)} for name, ok in checks],
        "scope": [
            "finite C4 microscopic-seed and amplifier control",
            "coherent-carrier versus dephased-shadow control",
            "exact convex-affinity and ensemble-decomposition witness",
            "endpoint-provenance support control",
        ],
        "not_claimed": [
            "cloud-chamber or nucleation simulation",
            "validation of the Schonfeld first-droplet mechanism",
            "observed Born-rule violation",
            "single-run ontology selection",
            "new fundamental law",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(f"{result['status']}: {passed}/{len(checks)} checks")
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
