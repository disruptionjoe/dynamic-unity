#!/usr/bin/env python3
"""Successor wild-frontier probe: tail-class test of CSG post running.

For a classical sequential-growth (CSG) coupling sequence ``t_n``, a post
with ``P`` ancestors induces the projective effective couplings

    T_n(P) = sum_{k=0}^P binom(P,k) t_{n+k}.

The factorial family used in the old causal-set cosmology argument,

    t_n = u^n / n!,

has an after-post transitive-percolation regime with effective coupling
``u_eff ~ sqrt(u/P)`` for fixed small precursor size.  This probe asks whether
the half-power belongs to the covariant post map itself or to the tail class
of the bare coupling sequence.

It evaluates the *finite* binomial transform for the wider family

    t_n = u^n / (n!)^alpha

and compares the ratios ``T_(n+1)/T_n`` with the saddle prediction

    u_eff ~ u^(1/(alpha+1)) P^(-alpha/(alpha+1)).

The finite calculation is a sensitivity/cheap-kill receipt.  It does not
establish repeated posts, a continuum geometry, a unit map, or a Lambda
identity.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_successor_wild_frontier_post_tail_probe_result.json"
)

POST_PAST_SIZES = (256, 1024, 4096, 16384, 65536)
ALPHAS = (0.0, 0.5, 1.0, 2.0)
# Subsequent to a post, no allowed birth has an empty past. T_0 is therefore
# physically irrelevant, and the effective projective coupling sequence starts
# at T_1. The primary percolation ratio is T_2/T_1 (index=1), not T_1/T_0.
FIXED_PRECURSOR_INDICES = (1, 2, 3, 4)
PRIMARY_U = 1.0
U_SENSITIVITY = (0.25, 1.0, 4.0)


def logaddexp(a: float, b: float) -> float:
    """Stable log(exp(a)+exp(b)) without a SciPy dependency."""

    if a == -math.inf:
        return b
    if b == -math.inf:
        return a
    if a < b:
        a, b = b, a
    return a + math.log1p(math.exp(b - a))


def log_post_coupling(
    post_past_size: int,
    index: int,
    u: float,
    alpha: float,
) -> float:
    """Return log T_index(P) from the exact finite binomial transform."""

    if post_past_size < 0 or index < 0:
        raise ValueError("post_past_size and index must be nonnegative")
    if u <= 0.0 or alpha < 0.0:
        raise ValueError("u must be positive and alpha nonnegative")

    # k=0 term: u^index/(index!)^alpha.
    log_term = index * math.log(u) - alpha * math.lgamma(index + 1.0)
    log_total = log_term
    for k in range(post_past_size):
        # term_(k+1)/term_k =
        #   [(P-k)/(k+1)] * u/(index+k+1)^alpha.
        log_term += (
            math.log(post_past_size - k)
            - math.log(k + 1.0)
            + math.log(u)
            - alpha * math.log(index + k + 1.0)
        )
        log_total = logaddexp(log_total, log_term)
    return log_total


def effective_ratios(
    post_past_size: int,
    u: float,
    alpha: float,
    indices: Iterable[int] = FIXED_PRECURSOR_INDICES,
) -> dict[int, float]:
    requested = tuple(indices)
    logs = {
        index: log_post_coupling(post_past_size, index, u, alpha)
        for index in range(max(requested) + 2)
    }
    return {
        index: math.exp(logs[index + 1] - logs[index])
        for index in requested
    }


def linear_slope(xs: list[float], ys: list[float]) -> float:
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    numerator = sum(
        (x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)
    )
    denominator = sum((x - mean_x) ** 2 for x in xs)
    return numerator / denominator


def predicted_exponent(alpha: float) -> float:
    return -alpha / (alpha + 1.0)


def predicted_ratio(post_past_size: int, u: float, alpha: float) -> float:
    return (
        u ** (1.0 / (alpha + 1.0))
        * post_past_size ** predicted_exponent(alpha)
    )


def alpha_sweep() -> dict[str, Any]:
    output: dict[str, Any] = {}
    for alpha in ALPHAS:
        rows = []
        primary_ratios = []
        for post_past_size in POST_PAST_SIZES:
            ratios = effective_ratios(
                post_past_size, PRIMARY_U, alpha
            )
            theory = predicted_ratio(
                post_past_size, PRIMARY_U, alpha
            )
            values = list(ratios.values())
            rows.append(
                {
                    "post_past_size": post_past_size,
                    "physical_effective_ratios_n_1_to_4": {
                        str(index): value
                        for index, value in ratios.items()
                    },
                    "predicted_asymptotic_ratio": theory,
                    "n1_over_prediction": ratios[1] / theory,
                    "fixed_n_relative_spread": (
                        max(values) - min(values)
                    )
                    / (sum(values) / len(values)),
                }
            )
            primary_ratios.append(ratios[1])
        fitted = linear_slope(
            [math.log(float(value)) for value in POST_PAST_SIZES[-4:]],
            [math.log(value) for value in primary_ratios[-4:]],
        )
        output[str(alpha)] = {
            "alpha": alpha,
            "predicted_exponent": predicted_exponent(alpha),
            "fitted_large_P_exponent": fitted,
            "absolute_exponent_error": abs(
                fitted - predicted_exponent(alpha)
            ),
            "rows": rows,
        }
    return output


def u_sweep() -> dict[str, Any]:
    post_past_size = POST_PAST_SIZES[-1]
    output: dict[str, Any] = {}
    for alpha in (0.5, 1.0, 2.0):
        rows = []
        for u in U_SENSITIVITY:
            ratio = effective_ratios(
                post_past_size, u, alpha, (1,)
            )[1]
            theory = predicted_ratio(post_past_size, u, alpha)
            rows.append(
                {
                    "u": u,
                    "physical_effective_ratio_n1": ratio,
                    "predicted_asymptotic_ratio": theory,
                    "ratio_over_prediction": ratio / theory,
                }
            )
        fitted_u_exponent = linear_slope(
            [math.log(row["u"]) for row in rows],
            [math.log(row["physical_effective_ratio_n1"]) for row in rows],
        )
        output[str(alpha)] = {
            "alpha": alpha,
            "predicted_u_exponent": 1.0 / (alpha + 1.0),
            "fitted_u_exponent": fitted_u_exponent,
            "absolute_u_exponent_error": abs(
                fitted_u_exponent - 1.0 / (alpha + 1.0)
            ),
            "rows": rows,
        }
    return {
        "post_past_size": post_past_size,
        "families": output,
    }


def main() -> None:
    alpha_results = alpha_sweep()
    u_results = u_sweep()

    alpha_zero_rows = alpha_results["0.0"]["rows"]
    alpha_one = alpha_results["1.0"]
    alpha_two = alpha_results["2.0"]
    largest_rows = {
        key: value["rows"][-1] for key, value in alpha_results.items()
    }

    checks = [
        {
            "name": (
                "transitive-percolation fixed-point family alpha=0 has "
                "no post-induced running"
            ),
            "pass": all(
                abs(
                    row["physical_effective_ratios_n_1_to_4"][str(index)]
                    - PRIMARY_U
                )
                < 2.0e-10
                for row in alpha_zero_rows
                for index in FIXED_PRECURSOR_INDICES
            ),
        },
        {
            "name": (
                "factorial family alpha=1 approaches the reported "
                "post-induced half-power"
            ),
            "pass": (
                alpha_one["absolute_exponent_error"] < 0.02
                and abs(
                    largest_rows["1.0"]["n1_over_prediction"] - 1.0
                )
                < 0.02
            ),
        },
        {
            "name": (
                "superfactorial family alpha=2 approaches a two-thirds "
                "rather than half-power"
            ),
            "pass": (
                alpha_two["absolute_exponent_error"] < 0.03
                and abs(
                    largest_rows["2.0"]["n1_over_prediction"] - 1.0
                )
                < 0.04
            ),
        },
        {
            "name": (
                "every tested alpha matches its distinct saddle exponent "
                "-alpha/(alpha+1)"
            ),
            "pass": all(
                result["absolute_exponent_error"] < 0.035
                for result in alpha_results.values()
            ),
        },
        {
            "name": (
                "effective ratios become precursor-index independent in "
                "the fixed-small-precursor regime"
            ),
            "pass": all(
                row["fixed_n_relative_spread"] < 0.08
                for key, row in largest_rows.items()
                if key != "0.0"
            ),
        },
        {
            "name": (
                "bare-amplitude sensitivity matches "
                "u^(1/(alpha+1))"
            ),
            "pass": all(
                result["absolute_u_exponent_error"] < 0.025
                for result in u_results["families"].values()
            ),
        },
        {
            "name": "the half-power is not universal across the tested tail classes",
            "pass": (
                abs(
                    alpha_results["0.0"]["fitted_large_P_exponent"]
                )
                < 1.0e-8
                and abs(
                    alpha_results["0.5"]["fitted_large_P_exponent"]
                    + 1.0 / 3.0
                )
                < 0.035
                and abs(
                    alpha_results["1.0"]["fitted_large_P_exponent"]
                    + 0.5
                )
                < 0.02
                and abs(
                    alpha_results["2.0"]["fitted_large_P_exponent"]
                    + 2.0 / 3.0
                )
                < 0.03
            ),
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    payload = {
        "probe": "du_successor_wild_frontier_post_tail_probe",
        "question": (
            "Does the exact CSG post-renormalization map generically produce "
            "a half-power, or does the exponent encode the tail class of the "
            "bare coupling sequence?"
        ),
        "exact_map": (
            "T_n(P)=sum_{k=0}^P binom(P,k)t_(n+k), projectively"
        ),
        "physical_indexing": (
            "After a post T_0 is irrelevant because empty-past births are "
            "excluded; the physical projective sequence begins at T_1 and "
            "the primary effective percolation ratio is T_2/T_1."
        ),
        "tested_family": "t_n=u^n/(n!)^alpha",
        "analytic_saddle": {
            "term_ratio": (
                "a_(k+1)/a_k=[(P-k)/(k+1)] "
                "u/(n+k+1)^alpha"
            ),
            "dominant_index": "k_*~(P u)^(1/(alpha+1))",
            "effective_ratio": (
                "T_(n+1)/T_n~u^(1/(alpha+1)) "
                "P^(-alpha/(alpha+1))"
            ),
            "factorial_special_case": (
                "alpha=1 gives u_eff~sqrt(u/P)"
            ),
        },
        "parameters": {
            "post_past_sizes": POST_PAST_SIZES,
            "alphas": ALPHAS,
            "fixed_precursor_indices": FIXED_PRECURSOR_INDICES,
            "primary_u": PRIMARY_U,
            "u_sensitivity": U_SENSITIVITY,
            "fitted_physical_parameters": [],
        },
        "alpha_sweep": alpha_results,
        "u_sweep": u_results,
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "POST_HALF_POWER_REAL_BUT_TAIL_CLASS_CONDITIONAL / "
            "FACTORIAL_ALPHA_ONE_REPRODUCED / "
            "UNIVERSAL_POST_HALF_POWER_OVERTURNED"
        ),
        "warrant": [
            "DERIVED for the saddle exponent under the declared family",
            "CONSTRUCTIVELY_REALIZED by exact finite binomial transforms",
            "STRUCTURAL_ANALOGY only for any relation to Lambda",
        ],
        "scope": {
            "earned": [
                "the exact post map produces no running for alpha=0",
                "the factorial alpha=1 family approaches a half-power",
                "different coupling-tail classes produce different exponents",
            ],
            "not_earned": [
                "that the alpha=1 family is selected",
                "that repeated posts occur for the selected family",
                "that after-post percolation recovers continuum geometry",
                "a unit-bearing physical scale or Lambda identity",
                "universality under the full admissible CSG coupling space",
            ],
        },
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("SUCCESSOR WILD FRONTIER — CSG POST TAIL-CLASS PROBE")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    for key, result in alpha_results.items():
        print(
            f"alpha={key}: predicted={result['predicted_exponent']:.6f}, "
            f"fitted={result['fitted_large_P_exponent']:.6f}"
        )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
