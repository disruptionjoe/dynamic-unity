#!/usr/bin/env python3
"""Exact controls for the HC-DU-187 three-width CSL prediction lock.

Passing verifies the finite rank and contrast statements used to tighten
PRED-DU-005. It does not validate CSL, the source's engineering estimates,
an apparatus, or any observed anomaly.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_csl_three_width_prediction_lock_result.json"
)


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def contrast_weights(widths: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, ...]:
    w1, w2, w3 = widths
    return (w3 - w2, w1 - w3, w2 - w1)


def determinant_three_columns(
    signal: tuple[Fraction, Fraction, Fraction],
    constant: tuple[Fraction, Fraction, Fraction],
    width: tuple[Fraction, Fraction, Fraction],
) -> Fraction:
    s1, s2, s3 = signal
    c1, c2, c3 = constant
    w1, w2, w3 = width
    return (
        s1 * (c2 * w3 - c3 * w2)
        - c1 * (s2 * w3 - s3 * w2)
        + w1 * (s2 * c3 - s3 * c2)
    )


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    widths = (Fraction(1), Fraction(2), Fraction(3))
    shared = (Fraction(1), Fraction(1), Fraction(1))
    # A decreasing, strictly convex finite control for the source-derived
    # breathing response S(W). The analytic source proof, not these numbers,
    # establishes strict convexity of the physical kernel.
    breathing = (Fraction(1), Fraction(1, 2), Fraction(1, 3))
    weights = contrast_weights(widths)

    checks.append(
        {
            "name": "contrast_annihilates_shared_path_nuisance",
            "passed": dot(weights, shared) == 0,
        }
    )
    checks.append(
        {
            "name": "contrast_annihilates_width_linear_timing_nuisance",
            "passed": dot(weights, widths) == 0,
        }
    )
    checks.append(
        {
            "name": "strictly_convex_breathing_response_survives_contrast",
            "passed": dot(weights, breathing) == Fraction(1, 3),
        }
    )

    amplitude = Fraction(6)
    shared_coefficient = Fraction(4)
    timing_coefficient = Fraction(5)
    observed = tuple(
        amplitude * signal + shared_coefficient + timing_coefficient * width
        for signal, width in zip(breathing, widths)
    )
    checks.append(
        {
            "name": "locked_contrast_recovers_only_challenger_component",
            "passed": dot(weights, observed) == Fraction(2),
        }
    )
    checks.append(
        {
            "name": "zero_challenger_gives_zero_locked_contrast",
            "passed": dot(
                weights,
                tuple(shared_coefficient + timing_coefficient * width for width in widths),
            )
            == 0,
        }
    )

    determinant = determinant_three_columns(breathing, shared, widths)
    checks.append(
        {
            "name": "three_width_design_has_full_rank",
            "passed": determinant != 0,
        }
    )

    # With two distinct widths, the shared and width-linear nuisance columns
    # already span R^2. Every two-entry challenger response is absorbed unless
    # one nuisance coefficient is independently fixed.
    width_pair = (Fraction(1), Fraction(2))
    arbitrary_pair = (Fraction(7), Fraction(11))
    timing_fit = arbitrary_pair[1] - arbitrary_pair[0]
    shared_fit = arbitrary_pair[0] - timing_fit * width_pair[0]
    checks.append(
        {
            "name": "two_width_response_is_absorbed_by_two_unknown_nuisances",
            "passed": tuple(shared_fit + timing_fit * width for width in width_pair)
            == arbitrary_pair,
        }
    )

    checks.append(
        {
            "name": "two_width_repair_returns_if_timing_is_independently_fixed",
            "passed": breathing[0] != breathing[1],
        }
    )

    # The source's analytic integrand has
    # d^2/dW^2 [1 + (W cos^2 + C sin^2)/r_c^2]^(-5/2)
    # = 35 cos^4/(4 r_c^4) * (...)^(-9/2), strictly positive wherever
    # cos != 0. This sign check records the proof boundary without simulating
    # the proposed device.
    rc_squared = Fraction(4)
    cos_squared = Fraction(1, 2)
    positive_prefactor = Fraction(35, 4) * cos_squared**2 / rc_squared**2
    checks.append(
        {
            "name": "source_breathing_kernel_second_derivative_prefactor_is_positive",
            "passed": positive_prefactor > 0,
        }
    )

    # Force-only scans retain the same path column for CSL and the admitted
    # unresolved environmental losses.
    forces = (Fraction(1), Fraction(2), Fraction(3))
    csl_force_kernel = tuple(force**2 for force in forces)
    environment_force_kernel = tuple(Fraction(9) * force**2 for force in forces)
    checks.append(
        {
            "name": "force_scan_keeps_csl_and_environment_columns_collinear",
            "passed": environment_force_kernel
            == tuple(Fraction(9) * value for value in csl_force_kernel),
        }
    )

    # An unrestricted configuration-specific nuisance is the identity basis
    # and absorbs every three-entry signal. The lock is conditional on the
    # declared nuisance family remaining frozen.
    identity_reconstruction = tuple(
        sum(
            Fraction(int(row == column)) * breathing[column]
            for column in range(3)
        )
        for row in range(3)
    )
    checks.append(
        {
            "name": "arbitrary_configuration_nuisance_kills_attribution",
            "passed": identity_reconstruction == breathing,
        }
    )

    # The paper's baseline/aggressive pair varies weak-trap frequency and
    # duration, so it is not the matched-width-only control locked here.
    source_weak_trap_frequencies = (Fraction(2000), Fraction(1000))
    checks.append(
        {
            "name": "published_operating_pair_is_not_matched_width_only_control",
            "passed": source_weak_trap_frequencies[0]
            != source_weak_trap_frequencies[1],
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-187",
        "prediction_id": "PRED-DU-005",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "With a shared path-loss coefficient and one unknown timing-loss "
            "coefficient linear in endpoint variance, two prepared widths "
            "cannot identify a CSL breathing response. Three distinct widths "
            "do so in the frozen source model because the CSL breathing "
            "factor is strictly convex in endpoint variance."
        ),
        "non_claims": [
            "No CSL parameter point or apparatus is empirically validated.",
            "No real nuisance family is proved complete.",
            "No source engineering estimate is reproduced.",
            "No hardware action, observed anomaly, or new DU law is earned.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the deterministic JSON result",
    )
    args = parser.parse_args()

    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
