#!/usr/bin/env python3
"""Independent-route finite controls for the CSG post-tail proof.

The original proof used a shifted-binomial expectation.  This audit starts
instead from the simpler exact identity

    T_(n+1)(P) / T_n(P) = E[r_(n+K)]

under weights proportional to binom(P,k)t_(n+k).  It then checks the
ratio-defined saddle concentration numerically across several regular-ratio
families.  The probe supports a second proof route; it is not an independent
human proof review or a novelty result.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path
from typing import Callable

from du_csg_post_tail_uniformity_probe import (
    build_log_couplings,
    implicit_scale,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_csg_post_tail_second_method_result.json"
)


def exact_post_sum(
    source: tuple[Fraction, ...], post_size: int, precursor: int
) -> Fraction:
    return sum(
        (
            Fraction(math.comb(post_size, k))
            * source[precursor + k]
            for k in range(post_size + 1)
        ),
        start=Fraction(0),
    )


def exact_identity_control() -> dict[str, object]:
    source = tuple(
        Fraction(value)
        for value in (3, 5, 11, 7, 19, 13, 29, 17, 31, 23, 37, 41)
    )
    rows = []
    for post_size in range(1, 6):
        for precursor in range(0, len(source) - post_size - 1):
            denominator = exact_post_sum(source, post_size, precursor)
            numerator = exact_post_sum(source, post_size, precursor + 1)
            transform_ratio = numerator / denominator

            direct_expectation = sum(
                (
                    Fraction(math.comb(post_size, k))
                    * source[precursor + k]
                    / denominator
                    * source[precursor + k + 1]
                    / source[precursor + k]
                    for k in range(post_size + 1)
                ),
                start=Fraction(0),
            )

            shifted_expectation = sum(
                (
                    Fraction(math.comb(post_size, k))
                    * source[precursor + k]
                    / denominator
                    * Fraction(k, post_size - k + 1)
                    for k in range(post_size + 1)
                ),
                start=Fraction(0),
            )
            endpoint = source[precursor + post_size + 1] / denominator
            rows.append(
                {
                    "post_size": post_size,
                    "precursor": precursor,
                    "transform_ratio": str(transform_ratio),
                    "direct_ratio_expectation": str(direct_expectation),
                    "shifted_expectation_plus_endpoint": str(
                        shifted_expectation + endpoint
                    ),
                    "direct_identity_exact": (
                        transform_ratio == direct_expectation
                    ),
                    "shifted_identity_exact": (
                        transform_ratio == shifted_expectation + endpoint
                    ),
                }
            )
    return {
        "source": [str(value) for value in source],
        "rows": rows,
        "all_direct_exact": all(
            bool(row["direct_identity_exact"]) for row in rows
        ),
        "all_shifted_exact": all(
            bool(row["shifted_identity_exact"]) for row in rows
        ),
    }


def logaddexp(left: float, right: float) -> float:
    if left == -math.inf:
        return right
    if right == -math.inf:
        return left
    if left < right:
        left, right = right, left
    return left + math.log1p(math.exp(right - left))


def normalized_weight_summary(
    post_size: int,
    precursor: int,
    scale: int,
    log_couplings: list[float],
    log_ratio: Callable[[int], float],
) -> dict[str, float | int]:
    log_weights = []
    log_binomial = 0.0
    for k in range(post_size + 1):
        if k:
            log_binomial += math.log(post_size - k + 1) - math.log(k)
        log_weights.append(log_binomial + log_couplings[precursor + k])

    normalizer = -math.inf
    for value in log_weights:
        normalizer = logaddexp(normalizer, value)
    probabilities = [math.exp(value - normalizer) for value in log_weights]
    lower = (1.0 - 0.25) * scale
    upper = (1.0 + 0.25) * scale
    outside_mass = sum(
        probability
        for k, probability in enumerate(probabilities)
        if k < lower or k > upper
    )
    expectation_ratio = sum(
        probability * math.exp(log_ratio(precursor + k))
        for k, probability in enumerate(probabilities)
    )
    mean_k = sum(
        k * probability for k, probability in enumerate(probabilities)
    )
    modal_k = max(range(len(probabilities)), key=probabilities.__getitem__)
    return {
        "post_size": post_size,
        "precursor": precursor,
        "implicit_scale": scale,
        "modal_k": modal_k,
        "mean_k_over_scale": mean_k / scale,
        "mass_outside_25_percent_scale_window": outside_mass,
        "direct_expectation_over_b_over_P": (
            expectation_ratio / (scale / post_size)
        ),
    }


def concentration_control() -> dict[str, object]:
    families: dict[str, object] = {}
    post_sizes = (256, 1024, 4096)
    for alpha in (0.5, 1.0, 2.0):
        log_ratio = lambda index, exponent=alpha: (
            -exponent * math.log(index + 1.0)
        )
        log_couplings = build_log_couplings(
            max(post_sizes) + 64, log_ratio
        )
        rows = []
        for post_size in post_sizes:
            scale = implicit_scale(post_size, log_ratio)
            precursor = max(1, int(math.sqrt(scale)))
            rows.append(
                normalized_weight_summary(
                    post_size,
                    precursor,
                    scale,
                    log_couplings,
                    log_ratio,
                )
            )
        families[str(alpha)] = {
            "alpha": alpha,
            "rows": rows,
            "outside_mass_decreases": (
                rows[-1]["mass_outside_25_percent_scale_window"]
                < rows[0]["mass_outside_25_percent_scale_window"]
            ),
            "terminal_ratio_error": abs(
                rows[-1]["direct_expectation_over_b_over_P"] - 1.0
            ),
        }
    return {"window_fraction": 0.25, "families": families}


def run() -> dict[str, object]:
    identities = exact_identity_control()
    concentration = concentration_control()
    checks = {
        "direct_expectation_identity_exact": identities["all_direct_exact"],
        "prior_shifted_identity_also_exact": identities["all_shifted_exact"],
        "all_regular_ratio_families_concentrate_more": all(
            family["outside_mass_decreases"]
            for family in concentration["families"].values()
        ),
        "all_terminal_modes_track_scale": all(
            abs(
                family["rows"][-1]["modal_k"]
                / family["rows"][-1]["implicit_scale"]
                - 1.0
            )
            < 0.2
            for family in concentration["families"].values()
        ),
        "all_terminal_expectations_track_theorem": all(
            family["terminal_ratio_error"] < 0.15
            for family in concentration["families"].values()
        ),
    }
    passed = sum(bool(value) for value in checks.values())
    if passed != len(checks):
        raise AssertionError(
            f"failed checks: {[name for name, ok in checks.items() if not ok]}"
        )
    payload = {
        "probe": "du_csg_post_tail_second_method_probe",
        "claim_grade": (
            "finite second-route proof controls; analytic proof and "
            "independent review remain separate"
        ),
        "exact_identities": identities,
        "concentration": concentration,
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "limits": [
            "Finite controls are not the asymptotic proof.",
            "The audit was produced in the same research session and is not independent peer review.",
            "No causal-set dynamics is selected and no physical scale is derived.",
            "The proof method lies in known regular-variation and discrete-saddle terrain.",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(payload, indent=2) + "\n")
    return payload


if __name__ == "__main__":
    result = run()
    print(
        json.dumps(
            {
                "verdict": "PASS",
                "checks": f"{result['checks_passed']}/{result['checks_total']}",
                "artifact": str(ARTIFACT.relative_to(ROOT)),
            },
            indent=2,
        )
    )
