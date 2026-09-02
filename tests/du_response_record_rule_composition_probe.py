#!/usr/bin/env python3
"""Exact finite controls for HC-DU-226.

This probe verifies a finite support-overlap reconstruction criterion and
smallest counterexamples separating selected response, material record value,
transition rule, and provenance.  It is not a device simulation or a new
physical prediction.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_response_record_rule_composition_result.json"
)


def nonempty_subsets(items: tuple[Hashable, ...]) -> tuple[frozenset[Hashable], ...]:
    return tuple(
        frozenset(item for item, keep in zip(items, mask) if keep)
        for mask in product((False, True), repeat=len(items))
        if any(mask)
    )


def support_decoder_exists(
    domain: Iterable[Hashable],
    target: Callable[[Hashable], Hashable],
    supports: dict[Hashable, frozenset[Hashable]],
) -> bool:
    domain = tuple(domain)
    return all(
        target(left) == target(right) or supports[left].isdisjoint(supports[right])
        for left in domain
        for right in domain
    )


def construct_decoder(
    domain: Iterable[Hashable],
    target: Callable[[Hashable], Hashable],
    supports: dict[Hashable, frozenset[Hashable]],
) -> dict[Hashable, Hashable] | None:
    if not support_decoder_exists(domain, target, supports):
        return None
    decoder: dict[Hashable, Hashable] = {}
    for item in domain:
        for observation in supports[item]:
            decoder[observation] = target(item)
    return decoder


def factors_through(
    domain: Iterable[Hashable],
    view: Callable[[Hashable], Hashable],
    target: Callable[[Hashable], Hashable],
) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for item in domain:
        key = view(item)
        value = target(item)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def path_support(
    start: int,
    steps: frozenset[int],
    horizon: int,
    states: frozenset[int],
) -> frozenset[tuple[int, ...]]:
    paths = {(start,)}
    for _ in range(horizon):
        extended: set[tuple[int, ...]] = set()
        for path in paths:
            for step in steps:
                endpoint = path[-1] + step
                if endpoint in states:
                    extended.add(path + (endpoint,))
        paths = extended
    return frozenset(paths)


def total_variation(
    left: dict[Hashable, Fraction], right: dict[Hashable, Fraction]
) -> Fraction:
    outcomes = set(left) | set(right)
    return Fraction(1, 2) * sum(
        abs(left.get(outcome, Fraction(0)) - right.get(outcome, Fraction(0)))
        for outcome in outcomes
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    # Exhaustive binary-target/three-output support theorem: 7 x 7 cases.
    outputs = ("a", "b", "c")
    support_families = nonempty_subsets(outputs)
    exhaustive_cases = 0
    exhaustive_matches = True
    for left in support_families:
        for right in support_families:
            supports = {0: left, 1: right}
            decoder = construct_decoder((0, 1), lambda item: item, supports)
            expected = left.isdisjoint(right)
            exhaustive_cases += 1
            exhaustive_matches &= (decoder is not None) == expected

    # Positive stochastic composition: randomness is harmless when target
    # classes have disjoint support.
    positive_supports = {
        0: frozenset(("cold", "cool")),
        1: frozenset(("hot",)),
    }
    positive_decoder = construct_decoder(
        (0, 1), lambda item: item, positive_supports
    )

    # Response sufficiency without a write: both source values yield blank.
    response_domain = (0, 1)
    blank_supports = {0: frozenset(("blank",)), 1: frozenset(("blank",))}

    # A stable formed carrier can be independent of the source target.
    formed_supports = {
        0: frozenset(("latched-0", "latched-1")),
        1: frozenset(("latched-0", "latched-1")),
    }
    formed_transition = {
        "latched-0": "latched-0",
        "latched-1": "latched-1",
    }

    # HC-DU-225 shadow. Even charge admits no-jump, single, and double slips;
    # odd charge admits no-jump and double slips. The transition graphs differ,
    # but the all-zero path is shared at every finite horizon.
    fluxoids = frozenset(range(-8, 9))
    even_steps = frozenset((-2, -1, 0, 1, 2))
    odd_steps = frozenset((-2, 0, 2))
    endpoint_supports = {
        0: frozenset(step for step in even_steps if step in fluxoids),
        1: frozenset(step for step in odd_steps if step in fluxoids),
    }
    finite_path_supports = {
        horizon: {
            0: path_support(0, even_steps, horizon, fluxoids),
            1: path_support(0, odd_steps, horizon, fluxoids),
        }
        for horizon in range(1, 6)
    }

    # Uniform one-step law is only an identifiability control, not a device
    # prediction. It makes the nonzero Bayes error exact.
    even_law = {
        value: Fraction(1, len(endpoint_supports[0])) for value in endpoint_supports[0]
    }
    odd_law = {
        value: Fraction(1, len(endpoint_supports[1])) for value in endpoint_supports[1]
    }
    tv = total_variation(even_law, odd_law)
    bayes_error = Fraction(1, 2) * (1 - tv)

    charges = tuple(range(-4, 5))
    charge_parity = lambda charge: charge % 2
    downstream_supports = {
        charge: endpoint_supports[charge_parity(charge)] for charge in charges
    }

    # Formation route is deliberately excluded from the process law. It is
    # therefore not reconstructible as provenance from any path in this model.
    histories = tuple((parity, route) for parity in (0, 1) for route in ("A", "B"))
    history_supports = {
        history: finite_path_supports[2][history[0]] for history in histories
    }

    checks = [
        (
            "exhaustive binary-target three-output support theorem holds",
            exhaustive_cases == 49 and exhaustive_matches,
        ),
        (
            "disjoint stochastic supports admit an exact decoder",
            positive_decoder
            == {"cold": 0, "cool": 0, "hot": 1},
        ),
        (
            "selected response can be target-sufficient before any material write",
            factors_through(response_domain, lambda item: item, lambda item: item),
        ),
        (
            "target-sufficient response does not make a constant blank a record",
            not support_decoder_exists(
                response_domain, lambda item: item, blank_supports
            ),
        ),
        (
            "stable formed carrier can remain target-insufficient",
            all(formed_transition[value] == value for value in formed_transition)
            and not support_decoder_exists(
                response_domain, lambda item: item, formed_supports
            ),
        ),
        (
            "distinct transition rules do not imply disjoint endpoint support",
            even_steps != odd_steps
            and not endpoint_supports[0].isdisjoint(endpoint_supports[1]),
        ),
        (
            "selected transition rule does not imply exact endpoint decoding",
            not support_decoder_exists((0, 1), lambda item: item, endpoint_supports),
        ),
        (
            "finite process records retain an overlapping all-zero path",
            all(
                (0,) * (horizon + 1)
                in finite_path_supports[horizon][0].intersection(
                    finite_path_supports[horizon][1]
                )
                for horizon in finite_path_supports
            ),
        ),
        (
            "finite path observation is not a zero-error parity certificate",
            all(
                not support_decoder_exists(
                    (0, 1), lambda item: item, supports
                )
                for supports in finite_path_supports.values()
            ),
        ),
        (
            "a single-slip event is only a one-sided certificate",
            any(value % 2 for value in endpoint_supports[0])
            and all(value % 2 == 0 for value in endpoint_supports[1]),
        ),
        (
            "overlapping one-step laws have nonzero equal-prior Bayes error",
            tv == Fraction(2, 5) and bayes_error == Fraction(3, 10),
        ),
        (
            "charge parity factors through the selected transition rule",
            factors_through(
                charges,
                charge_parity,
                lambda charge: tuple(
                    sorted(even_steps if charge_parity(charge) == 0 else odd_steps)
                ),
            )
            and factors_through(
                charges,
                lambda charge: tuple(
                    sorted(even_steps if charge_parity(charge) == 0 else odd_steps)
                ),
                charge_parity,
            ),
        ),
        (
            "full signed charge is lost before the transition rule",
            not support_decoder_exists(charges, lambda charge: charge, downstream_supports),
        ),
        (
            "downstream processing cannot repair the charge-parity quotient",
            any(
                left != right
                and charge_parity(left) == charge_parity(right)
                and downstream_supports[left] == downstream_supports[right]
                for left in charges
                for right in charges
            ),
        ),
        (
            "same parity process law does not reconstruct formation route",
            not support_decoder_exists(histories, lambda history: history[1], history_supports),
        ),
        (
            "same parity histories remain process-equivalent across routes",
            all(
                history_supports[(parity, "A")] == history_supports[(parity, "B")]
                for parity in (0, 1)
            ),
        ),
    ]

    result = {
        "claim_id": "HC-DU-226",
        "run_id": "RUN-20260902-response-record-rule-composition-boundary",
        "disposition": [
            "THREE_LAYER_SEPARATION_PROVED",
            "EXACT_HANDOFF_SUPPORT_CRITERION",
            "FIRST_LEAK_LOCALIZED",
            "KNOWN_MATHEMATICS_ABSORPTION",
            "DU_TYPED_COMPOSITION_SURVIVES",
            "NOVEL_THEOREM_NOT_ESTABLISHED",
            "PAPER_STATUS_UNCHANGED",
            "NO_READY_SUCCESSOR",
        ],
        "exhaustive_support_cases": exhaustive_cases,
        "positive_decoder": positive_decoder,
        "fluxoid_endpoint_supports": {
            str(key): sorted(value) for key, value in endpoint_supports.items()
        },
        "finite_path_overlap_counts": {
            str(horizon): len(supports[0].intersection(supports[1]))
            for horizon, supports in finite_path_supports.items()
        },
        "uniform_one_step_total_variation": str(tv),
        "uniform_one_step_bayes_error": str(bayes_error),
        "checks": [{"name": name, "passed": passed} for name, passed in checks],
        "passed": sum(1 for _, passed in checks if passed),
        "total": len(checks),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"{result['passed']}/{result['total']} checks passed")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
