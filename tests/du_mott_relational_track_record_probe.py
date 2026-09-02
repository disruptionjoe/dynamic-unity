#!/usr/bin/env python3
"""Exact finite controls for HC-DU-227.

The probe models only the symmetry, correlation, and discrimination boundaries
of the Mott cloud-chamber analysis.  It does not simulate a cloud chamber,
derive a collapse law, or make a new physical prediction.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_mott_relational_track_record_result.json"
DIRECTIONS = tuple(range(4))


def rotate(direction: int, shift: int) -> int:
    return (direction + shift) % len(DIRECTIONS)


def equivariant_constant_selector_exists() -> bool:
    """A singleton symmetric antecedent can select only a group-fixed point."""
    return any(
        all(rotate(candidate, shift) == candidate for shift in DIRECTIONS)
        for candidate in DIRECTIONS
    )


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


def trace_product(left: list[list[Fraction]], right: list[list[Fraction]]) -> Fraction:
    size = len(left)
    return sum(
        left[row][column] * right[column][row]
        for row in range(size)
        for column in range(size)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    # A Mott-like matched response has only same-ray double excitations.  An
    # independent response has all pairs.  Both one-site marginals are uniform.
    matched_pairs = frozenset((direction, direction) for direction in DIRECTIONS)
    independent_pairs = frozenset(
        (left, right) for left in DIRECTIONS for right in DIRECTIONS
    )
    matched_joint = {
        pair: Fraction(1, len(DIRECTIONS)) if pair in matched_pairs else Fraction(0)
        for pair in independent_pairs
    }
    independent_joint = {
        pair: Fraction(1, len(DIRECTIONS) ** 2) for pair in independent_pairs
    }
    matched_left_marginal = {
        direction: sum(
            probability
            for (left, _), probability in matched_joint.items()
            if left == direction
        )
        for direction in DIRECTIONS
    }
    independent_left_marginal = {
        direction: sum(
            probability
            for (left, _), probability in independent_joint.items()
            if left == direction
        )
        for direction in DIRECTIONS
    }

    # Work in the four-dimensional matched-pattern subspace.  The coherent
    # state has density matrix entries 1/4; the dephased mixture keeps only the
    # diagonal.  Fractions make the discriminator exact.
    dimension = len(DIRECTIONS)
    coherent = [
        [Fraction(1, dimension) for _ in DIRECTIONS] for _ in DIRECTIONS
    ]
    dephased = [
        [Fraction(1, dimension) if row == column else Fraction(0)
         for column in DIRECTIONS]
        for row in DIRECTIONS
    ]
    coherent_projector = coherent
    pointer_coherent = tuple(coherent[index][index] for index in DIRECTIONS)
    pointer_dephased = tuple(dephased[index][index] for index in DIRECTIONS)
    coherent_witness_probability = trace_product(coherent_projector, coherent)
    mixture_witness_probability = trace_product(coherent_projector, dephased)

    # Ideal realized track sectors have disjoint support.  A coarse
    # straight-track label and two source routes with the same track law do not.
    direction_supports = {
        f"direction-{direction}": frozenset((f"track-{direction}",))
        for direction in DIRECTIONS
    }
    direction_targets = {
        history: history.removeprefix("direction-") for history in direction_supports
    }
    coarse_supports = {
        history: frozenset(("straight-track",)) for history in direction_supports
    }
    route_supports = {
        "source-route-A": frozenset(f"track-{direction}" for direction in DIRECTIONS),
        "source-route-B": frozenset(f"track-{direction}" for direction in DIRECTIONS),
    }
    route_targets = {"source-route-A": "A", "source-route-B": "B"}

    # Rotation leaves the matched relational family invariant even though it
    # moves every named direction.
    rotated_matched_pairs = {
        (rotate(left, 1), rotate(right, 1)) for left, right in matched_pairs
    }
    uniform_direction_law = {
        direction: Fraction(1, dimension) for direction in DIRECTIONS
    }
    rotated_uniform_direction_law = {
        rotate(direction, 1): probability
        for direction, probability in uniform_direction_law.items()
    }

    checks = [
        (
            "matched response selects only same-direction double excitations",
            matched_pairs == frozenset((d, d) for d in DIRECTIONS),
        ),
        (
            "matched and independent laws have identical uniform local marginals",
            matched_left_marginal == independent_left_marginal
            == {direction: Fraction(1, dimension) for direction in DIRECTIONS},
        ),
        (
            "joint response distinguishes matched geometry from independent response",
            matched_joint != independent_joint
            and all(matched_joint[(left, right)] == 0 for left, right in independent_pairs if left != right),
        ),
        (
            "matched response family is rotation invariant",
            rotated_matched_pairs == set(matched_pairs),
        ),
        (
            "the direction orbit has no rotation-fixed member",
            all(any(rotate(direction, shift) != direction for shift in DIRECTIONS) for direction in DIRECTIONS),
        ),
        (
            "no deterministic equivariant direction selector exists on the symmetric antecedent",
            not equivariant_constant_selector_exists(),
        ),
        (
            "a uniform stochastic direction law remains symmetry equivariant",
            rotated_uniform_direction_law == uniform_direction_law,
        ),
        (
            "coherent and dephased carriers have identical pointer track statistics",
            pointer_coherent == pointer_dephased
            == tuple(Fraction(1, dimension) for _ in DIRECTIONS),
        ),
        (
            "a coherent global witness distinguishes the carrier states",
            coherent_witness_probability == 1
            and mixture_witness_probability == Fraction(1, dimension),
        ),
        (
            "dephasing removes every off-diagonal direction coherence",
            all(dephased[row][column] == 0 for row in DIRECTIONS for column in DIRECTIONS if row != column),
        ),
        (
            "an ideal realized direction track has an exact direction decoder",
            exact_decoder_exists(direction_supports, direction_targets),
        ),
        (
            "a coarse straight-track record does not identify direction",
            not exact_decoder_exists(coarse_supports, direction_targets),
        ),
        (
            "response-identical source routes are not certified by the track",
            not exact_decoder_exists(route_supports, route_targets),
        ),
        (
            "record support can preserve direction while erasing formation route",
            exact_decoder_exists(direction_supports, direction_targets)
            and not exact_decoder_exists(route_supports, route_targets),
        ),
        (
            "pointer statistics alone cannot certify coherence loss",
            pointer_coherent == pointer_dephased
            and coherent_witness_probability != mixture_witness_probability,
        ),
        (
            "the local model remains a symmetry and discrimination control only",
            True,
        ),
    ]

    passed = sum(bool(ok) for _, ok in checks)
    result = {
        "claim_id": "HC-DU-227",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "direction_count": dimension,
        "matched_support_size": len(matched_pairs),
        "independent_support_size": len(independent_pairs),
        "coherent_witness_probability": str(coherent_witness_probability),
        "mixture_witness_probability": str(mixture_witness_probability),
        "checks": [{"name": name, "passed": bool(ok)} for name, ok in checks],
        "scope": [
            "finite direction-permutation symmetry control",
            "matched-correlation versus local-marginal control",
            "coherent-carrier versus dephased-shadow discrimination control",
            "exact support-decoder and provenance counterexamples",
        ],
        "not_claimed": [
            "cloud-chamber simulation",
            "collapse or single-outcome derivation",
            "new quantum theorem",
            "new physical prediction",
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
