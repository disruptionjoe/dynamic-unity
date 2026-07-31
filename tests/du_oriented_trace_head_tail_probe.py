#!/usr/bin/env python3
"""Exact finite controls for the HC-DU-180 oriented-trace boundary.

The probe distinguishes an unoriented spatial axis from a reflection-odd
material-response profile and distinguishes bounded-error head-tail
information from zero-error certification. Passing proves only finite
factorization, binary-testing, and data-processing facts. It does not model a
time-projection chamber, identify a particle, select a readout or archive,
establish an event time, or supply new physics.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Hashable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_oriented_trace_head_tail_result.json"
)

Outcome = Hashable
Law = dict[Outcome, Fraction]
Kernel = dict[Outcome, dict[Outcome, Fraction]]


def kernel_sufficient(
    histories: tuple[str, ...],
    record: dict[str, object],
    target: dict[str, object],
) -> bool:
    """Return whether the target factors through the finite record map."""

    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in histories
        for right in histories
    )


def total_variation(left: Law, right: Law) -> Fraction:
    outcomes = set(left) | set(right)
    return sum(
        abs(left.get(outcome, Fraction(0)) - right.get(outcome, Fraction(0)))
        for outcome in outcomes
    ) / 2


def bayes_error_equal_priors(left: Law, right: Law) -> Fraction:
    return (1 - total_variation(left, right)) / 2


def pushforward(law: Law, kernel: Kernel) -> Law:
    """Push a finite law through a stochastic readout kernel exactly."""

    result: Law = {}
    for source, source_probability in law.items():
        row = kernel[source]
        if sum(row.values()) != 1:
            raise ValueError(f"kernel row for {source!r} is not normalized")
        for target, conditional_probability in row.items():
            result[target] = (
                result.get(target, Fraction(0))
                + source_probability * conditional_probability
            )
    return result


def reflection_odd_moment(profile: tuple[int, ...]) -> int:
    """A centered first moment that changes sign under path reversal."""

    center_twice = len(profile) - 1
    return sum(
        (2 * index - center_twice) * weight
        for index, weight in enumerate(profile)
    )


def as_json_fraction(value: Fraction) -> dict[str, int]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def run_probe() -> dict[str, object]:
    histories = ("forward", "reverse")
    direction = {"forward": 1, "reverse": -1}
    axis_only = {history: frozenset({0, 1, 2}) for history in histories}
    asymmetric_profile = {
        "forward": (3, 2, 1),
        "reverse": (1, 2, 3),
    }
    symmetric_profile = {
        "forward": (1, 2, 1),
        "reverse": (1, 2, 1),
    }

    checks: list[dict[str, object]] = []
    checks.append(
        {
            "name": "unoriented_axis_does_not_factor_direction",
            "passed": not kernel_sufficient(histories, axis_only, direction),
        }
    )
    checks.append(
        {
            "name": "asymmetric_profile_factors_noiseless_direction",
            "passed": kernel_sufficient(
                histories,
                asymmetric_profile,
                direction,
            ),
        }
    )
    checks.append(
        {
            "name": "reflection_odd_moment_changes_sign",
            "passed": (
                reflection_odd_moment(asymmetric_profile["forward"]) != 0
                and reflection_odd_moment(asymmetric_profile["forward"])
                == -reflection_odd_moment(asymmetric_profile["reverse"])
            ),
            "forward_moment": reflection_odd_moment(
                asymmetric_profile["forward"]
            ),
            "reverse_moment": reflection_odd_moment(
                asymmetric_profile["reverse"]
            ),
        }
    )
    checks.append(
        {
            "name": "reflection_symmetric_profile_carries_no_direction",
            "passed": (
                not kernel_sufficient(
                    histories,
                    symmetric_profile,
                    direction,
                )
                and reflection_odd_moment(symmetric_profile["forward"]) == 0
            ),
        }
    )

    # A noisy physical head-tail profile contains useful information but has
    # overlapping orientation-conditioned laws.
    noisy_forward: Law = {
        "forward_heavy": Fraction(4, 5),
        "reverse_heavy": Fraction(1, 5),
    }
    noisy_reverse: Law = {
        "forward_heavy": Fraction(1, 5),
        "reverse_heavy": Fraction(4, 5),
    }
    noisy_tv = total_variation(noisy_forward, noisy_reverse)
    noisy_error = bayes_error_equal_priors(noisy_forward, noisy_reverse)
    checks.append(
        {
            "name": "overlapping_laws_give_bounded_not_zero_error",
            "passed": noisy_tv == Fraction(3, 5)
            and noisy_error == Fraction(1, 5),
            "total_variation": as_json_fraction(noisy_tv),
            "minimum_equal_prior_error": as_json_fraction(noisy_error),
        }
    )

    # Exact orientation requires disjoint supports in this finite setting.
    exact_forward: Law = {"forward_heavy": Fraction(1)}
    exact_reverse: Law = {"reverse_heavy": Fraction(1)}
    exact_tv = total_variation(exact_forward, exact_reverse)
    exact_error = bayes_error_equal_priors(exact_forward, exact_reverse)
    checks.append(
        {
            "name": "disjoint_laws_give_zero_error_orientation",
            "passed": exact_tv == 1 and exact_error == 0,
            "total_variation": as_json_fraction(exact_tv),
            "minimum_equal_prior_error": as_json_fraction(exact_error),
        }
    )

    # Diffusion/digitization is represented by a noisy two-output channel.
    # It degrades the existing orientation information.
    readout: Kernel = {
        "forward_heavy": {
            "observed_forward_heavy": Fraction(3, 4),
            "observed_reverse_heavy": Fraction(1, 4),
        },
        "reverse_heavy": {
            "observed_forward_heavy": Fraction(1, 4),
            "observed_reverse_heavy": Fraction(3, 4),
        },
    }
    observed_forward = pushforward(noisy_forward, readout)
    observed_reverse = pushforward(noisy_reverse, readout)
    observed_tv = total_variation(observed_forward, observed_reverse)
    observed_error = bayes_error_equal_priors(
        observed_forward,
        observed_reverse,
    )
    checks.append(
        {
            "name": "downstream_readout_cannot_increase_orientation_tv",
            "passed": observed_tv == Fraction(3, 10)
            and observed_tv <= noisy_tv
            and observed_error == Fraction(7, 20),
            "upstream_total_variation": as_json_fraction(noisy_tv),
            "downstream_total_variation": as_json_fraction(observed_tv),
            "downstream_minimum_equal_prior_error": as_json_fraction(
                observed_error
            ),
        }
    )

    # Complete coarse-graining to an axis-only signal destroys head-tail
    # information rather than creating an orientation.
    axis_readout: Kernel = {
        "forward_heavy": {"axis_seen": Fraction(1)},
        "reverse_heavy": {"axis_seen": Fraction(1)},
    }
    coarse_forward = pushforward(noisy_forward, axis_readout)
    coarse_reverse = pushforward(noisy_reverse, axis_readout)
    checks.append(
        {
            "name": "axis_coarse_graining_erases_head_tail_information",
            "passed": total_variation(coarse_forward, coarse_reverse) == 0
            and bayes_error_equal_priors(
                coarse_forward,
                coarse_reverse,
            )
            == Fraction(1, 2),
        }
    )

    # A known calibration-source direction can make the joint packet
    # perfectly informative even when the physical detector response alone is
    # identical. This is imported side information, not an intrinsic tag.
    uninformative_response = {
        "forward": "same_signal",
        "reverse": "same_signal",
    }
    source_label = {
        "forward": "+z_source",
        "reverse": "-z_source",
    }
    joint_packet = {
        history: (
            uninformative_response[history],
            source_label[history],
        )
        for history in histories
    }
    checks.append(
        {
            "name": "known_source_label_is_imported_orientation_information",
            "passed": (
                not kernel_sufficient(
                    histories,
                    uninformative_response,
                    direction,
                )
                and kernel_sufficient(histories, joint_packet, direction)
            ),
        }
    )

    passed = all(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-180",
        "passed": passed,
        "check_count": len(checks),
        "checks": checks,
        "earned": {
            "noiseless_boundary": (
                "a reflection-asymmetric retained profile can factor an "
                "orientation that an unoriented axis cannot"
            ),
            "statistical_boundary": (
                "equal-prior optimal head-tail error is "
                "(1-TV(mu_plus,mu_minus))/2"
            ),
            "readout_boundary": (
                "a downstream stochastic readout cannot increase total "
                "variation between the orientation-conditioned laws"
            ),
            "side_information_boundary": (
                "a known source direction may repair the joint packet "
                "without becoming intrinsic detector provenance"
            ),
        },
        "not_earned": [
            "time-projection-chamber physics",
            "material persistence after the transient ionization field",
            "zero-error event-by-event head-tail certification in an experiment",
            "track membership in a multi-event exposure",
            "event time or upstream particle identity",
            "selected calibration, readout, archive, or observer access",
            "an unabsorbed higher-response law",
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
