#!/usr/bin/env python3
"""Hostile finite controls for the paper-grade CSG post-tail theorem.

The analytic theorem requires a precursor window ``n=o(b_P)``.  This probe
checks two load-bearing seams that the earlier finite controls did not:

1. changing an arbitrary finite prefix of an eventually positive coupling
   sequence does not change the tail asymptotic; and
2. the ``o(b_P)`` restriction is substantive.  In the factorial class
   ``r_m=1/(m+1)``, a precursor ``n~c b_P`` changes the normalized response
   from 1 to the positive solution of ``x(c+x)=1``.

The calculations are finite diagnostics.  They do not replace the analytic
proof, establish novelty, select a CSG law, or give the tail scale physical
units.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from du_csg_post_tail_uniformity_probe import (
    build_log_couplings,
    effective_ratio,
    implicit_scale,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_csg_post_tail_paper_hardening_result.json"
)

POST_SIZES = (4096, 16384, 65536)
PREFIX_POST_SIZES = (256, 1024, 4096)


def factorial_log_ratio(index: int) -> float:
    return -math.log(index + 1.0)


def proportional_precursor_control() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for post_size in POST_SIZES:
        scale = implicit_scale(post_size, factorial_log_ratio)
        logs = build_log_couplings(
            post_size + 3 * scale + 16,
            factorial_log_ratio,
        )
        cases = []
        for c in (0.5, 1.0, 2.0):
            precursor = max(1, int(c * scale))
            observed = (
                effective_ratio(post_size, precursor, logs)
                / (scale / post_size)
            )
            predicted = (math.sqrt(c * c + 4.0) - c) / 2.0
            cases.append(
                {
                    "c": c,
                    "precursor": precursor,
                    "observed_normalized_response": observed,
                    "predicted_limit": predicted,
                    "absolute_error": abs(observed - predicted),
                }
            )
        subscale_precursor = max(1, int(math.sqrt(scale)))
        subscale_observed = (
            effective_ratio(post_size, subscale_precursor, logs)
            / (scale / post_size)
        )
        rows.append(
            {
                "post_size": post_size,
                "implicit_scale": scale,
                "subscale_precursor": subscale_precursor,
                "subscale_normalized_response": subscale_observed,
                "proportional_cases": cases,
            }
        )
    return {
        "family": "t_m=1/m!",
        "balance_scale": "P/((b+1)b) approximately 1",
        "proportional_limit_equation": "x(c+x)=1",
        "rows": rows,
    }


def altered_prefix_logs(
    maximum_index: int,
    variant: str,
    prefix_length: int = 5,
) -> list[float]:
    logs = [-math.lgamma(index + 1.0) for index in range(maximum_index + 1)]
    if variant == "zero_prefix":
        for index in range(prefix_length):
            logs[index] = -math.inf
    elif variant == "large_irregular_prefix":
        replacements = (27.0, -math.inf, 19.0, -7.0, 23.0)
        for index, value in enumerate(replacements):
            logs[index] = value
    elif variant != "unaltered":
        raise ValueError(f"unknown prefix variant: {variant}")
    return logs


def finite_prefix_control() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for post_size in PREFIX_POST_SIZES:
        maximum_index = post_size + 8
        scale = implicit_scale(post_size, factorial_log_ratio)
        target = scale / post_size
        variants = {}
        for variant in (
            "unaltered",
            "zero_prefix",
            "large_irregular_prefix",
        ):
            logs = altered_prefix_logs(maximum_index, variant)
            response = effective_ratio(post_size, 1, logs)
            variants[variant] = {
                "response": response,
                "response_over_b_over_P": response / target,
            }
        rows.append(
            {
                "post_size": post_size,
                "implicit_scale": scale,
                "variants": variants,
                "maximum_pairwise_response_delta": max(
                    abs(
                        left["response_over_b_over_P"]
                        - right["response_over_b_over_P"]
                    )
                    for left in variants.values()
                    for right in variants.values()
                ),
            }
        )
    return {
        "shared_tail": "t_m=1/m! for every m>=5",
        "rows": rows,
    }


def run() -> dict[str, object]:
    proportional = proportional_precursor_control()
    prefix = finite_prefix_control()
    proportional_rows = proportional["rows"]
    prefix_rows = prefix["rows"]
    terminal_proportional = proportional_rows[-1]["proportional_cases"]

    checks = {
        "subscale_window_moves_toward_one": (
            abs(
                proportional_rows[-1]["subscale_normalized_response"] - 1.0
            )
            < abs(
                proportional_rows[0]["subscale_normalized_response"] - 1.0
            )
        ),
        "proportional_window_matches_distinct_limit": all(
            case["absolute_error"] < 0.002
            for case in terminal_proportional
        ),
        "proportional_limit_is_not_the_subscale_limit": all(
            abs(case["predicted_limit"] - 1.0) > 0.15
            for case in terminal_proportional
        ),
        "finite_prefix_effect_decreases": (
            prefix_rows[-1]["maximum_pairwise_response_delta"]
            < prefix_rows[0]["maximum_pairwise_response_delta"]
        ),
        "finite_prefix_effect_is_terminally_negligible": (
            prefix_rows[-1]["maximum_pairwise_response_delta"] < 1e-9
        ),
    }
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    payload = {
        "probe": "du_csg_post_tail_paper_hardening_probe",
        "claim_grade": (
            "finite hostile controls for the precursor-window and "
            "eventual-positivity seams"
        ),
        "proportional_precursor_control": proportional,
        "finite_prefix_control": prefix,
        "checks": checks,
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "limits": [
            "Finite calculations are not the asymptotic proof.",
            "The proportional-window formula is proved separately.",
            "No CSG coupling sequence, post occurrence, or continuum limit is selected.",
            "The probe does not establish novelty or physical interpretation.",
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
                "checks": (
                    f"{result['checks_passed']}/{result['checks_total']}"
                ),
                "artifact": str(ARTIFACT.relative_to(ROOT)),
            },
            indent=2,
        )
    )
