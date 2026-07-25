#!/usr/bin/env python3
"""Deterministic controls for CSG post-tail uniformity.

For a nonnegative classical-sequential-growth coupling sequence ``t_n``, a
post with ``P`` ancestors induces

    T_n(P) = sum_{k=0}^P binom(P,k) t_{n+k}.

The paper candidate classifies the projective ratios ``T_(n+1)/T_n`` when the
adjacent bare ratios ``r_m=t_(m+1)/t_m`` have a regularly varying tail.  This
probe is finite evidence for the analytic proof; it is not the proof and does
not establish post recurrence, manifoldlikeness, a physical scale, or Lambda.

Only the Python standard library is used.  Every displayed curve is generated
from finite binomial sums or exact rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path
from typing import Callable, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_csg_post_tail_uniformity_result.json"
)

POST_SIZES = (256, 1024, 4096, 16384, 65536)
POWER_ALPHAS = (0.5, 1.0, 2.0)
POWER_U = 1.0
LOG_ALPHA = 1.0
LOG_GAMMA = 2.0
FINITE_SUPPORT_MAX = 9
SPARSE_SCAN_MAX = 32768


def logaddexp(a: float, b: float) -> float:
    if a == -math.inf:
        return b
    if b == -math.inf:
        return a
    if a < b:
        a, b = b, a
    return a + math.log1p(math.exp(b - a))


def build_log_couplings(
    maximum_index: int,
    log_ratio: Callable[[int], float],
) -> list[float]:
    """Build log(t_m) with t_0=1 and supplied log(t_(m+1)/t_m)."""

    values = [0.0]
    for index in range(maximum_index):
        values.append(values[-1] + log_ratio(index))
    return values


def log_post_sum(
    post_size: int,
    precursor_index: int,
    log_couplings: list[float],
) -> float:
    """Stable log of the exact finite binomial post transform."""

    if precursor_index + post_size >= len(log_couplings):
        raise ValueError("coupling table is too short")
    log_binomial = 0.0
    total = log_couplings[precursor_index]
    for k in range(post_size):
        log_binomial += (
            math.log(post_size - k) - math.log(k + 1.0)
        )
        total = logaddexp(
            total,
            log_binomial + log_couplings[precursor_index + k + 1],
        )
    return total


def effective_ratio(
    post_size: int,
    precursor_index: int,
    log_couplings: list[float],
) -> float:
    return math.exp(
        log_post_sum(post_size, precursor_index + 1, log_couplings)
        - log_post_sum(post_size, precursor_index, log_couplings)
    )


def implicit_scale(
    post_size: int,
    log_ratio: Callable[[int], float],
) -> int:
    """Return the integer b minimizing |log(P r_b / b)|.

    The theorem's scale is any b_P for which P r_(b_P)/b_P -> 1.  A
    deterministic scan avoids inserting the desired exponent into the finite
    control.
    """

    best_index = 1
    best_error = math.inf
    for index in range(1, post_size + 1):
        error = abs(
            math.log(post_size)
            + log_ratio(index)
            - math.log(index)
        )
        if error < best_error:
            best_error = error
            best_index = index
    return best_index


def sampled_precursors(scale: int) -> tuple[int, ...]:
    """Indices extending to floor(sqrt(b)), a finite n=o(b) control."""

    upper = max(1, int(math.sqrt(scale)))
    candidates = {1, 2, 3, upper // 2, upper}
    return tuple(sorted(index for index in candidates if 1 <= index <= upper))


def exact_semigroup_control() -> dict[str, object]:
    source = tuple(
        Fraction(value)
        for value in (1, 3, 2, 5, 7, 11, 13, 17, 19)
    )
    post_size = 4

    def one_step(sequence: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
        return tuple(
            sequence[index] + sequence[index + 1]
            for index in range(len(sequence) - 1)
        )

    iterated = source
    for _ in range(post_size):
        iterated = one_step(iterated)
    direct = tuple(
        sum(
            Fraction(math.comb(post_size, k)) * source[index + k]
            for k in range(post_size + 1)
        )
        for index in range(len(source) - post_size)
    )
    return {
        "post_size": post_size,
        "source": [str(value) for value in source],
        "iterated": [str(value) for value in iterated],
        "direct": [str(value) for value in direct],
        "exact_match": iterated == direct,
    }


def power_tail_control() -> dict[str, object]:
    families: dict[str, object] = {}
    maximum_index = max(POST_SIZES) + 64
    for alpha in POWER_ALPHAS:
        log_ratio = lambda m, a=alpha: (
            math.log(POWER_U) - a * math.log(m + 1.0)
        )
        logs = build_log_couplings(maximum_index, log_ratio)
        rows = []
        for post_size in POST_SIZES:
            scale = implicit_scale(post_size, log_ratio)
            target = scale / post_size
            ratios = {
                str(index): effective_ratio(post_size, index, logs)
                for index in sampled_precursors(scale)
            }
            errors = {
                key: abs(value / target - 1.0)
                for key, value in ratios.items()
            }
            rows.append(
                {
                    "post_size": post_size,
                    "implicit_scale": scale,
                    "implicit_target_b_over_P": target,
                    "sampled_precursor_indices": [
                        int(key) for key in ratios
                    ],
                    "effective_ratios": ratios,
                    "relative_errors": errors,
                    "maximum_relative_error": max(errors.values()),
                    "pure_power_target": (
                        POWER_U ** (1.0 / (alpha + 1.0))
                        * post_size ** (-alpha / (alpha + 1.0))
                    ),
                }
            )
        fit_rows = rows[-4:]
        slope = linear_slope(
            [math.log(float(row["post_size"])) for row in fit_rows],
            [
                math.log(float(row["effective_ratios"]["1"]))
                for row in fit_rows
            ],
        )
        families[str(alpha)] = {
            "alpha": alpha,
            "predicted_exponent": -alpha / (alpha + 1.0),
            "fitted_exponent": slope,
            "absolute_exponent_error": abs(
                slope + alpha / (alpha + 1.0)
            ),
            "rows": rows,
        }
    return {
        "family": "t_m=u^m/(m!)^alpha",
        "u": POWER_U,
        "families": families,
    }


def log_corrected_control() -> dict[str, object]:
    def log_ratio(index: int) -> float:
        argument = index + math.e
        return (
            -LOG_ALPHA * math.log(index + 1.0)
            + LOG_GAMMA * math.log(math.log(argument))
        )

    maximum_index = max(POST_SIZES) + 64
    logs = build_log_couplings(maximum_index, log_ratio)
    rows = []
    for post_size in POST_SIZES:
        scale = implicit_scale(post_size, log_ratio)
        target = scale / post_size
        ratio = effective_ratio(post_size, 1, logs)
        pure_power_target = post_size ** (
            -LOG_ALPHA / (LOG_ALPHA + 1.0)
        )
        rows.append(
            {
                "post_size": post_size,
                "implicit_scale": scale,
                "effective_ratio_n1": ratio,
                "implicit_target_b_over_P": target,
                "ratio_over_implicit_target": ratio / target,
                "ratio_over_pure_power_without_log": (
                    ratio / pure_power_target
                ),
            }
        )
    return {
        "family": (
            "r_m=(log(m+e))^gamma/(m+1)^alpha, "
            "t_(m+1)=r_m t_m"
        ),
        "alpha": LOG_ALPHA,
        "gamma": LOG_GAMMA,
        "rows": rows,
    }


def finite_support_control() -> dict[str, object]:
    """Exact rational endpoint: finite support gives the P^-1 boundary."""

    rows = []
    for post_size in (64, 256, 1024, 4096):
        for precursor_index in (1, 3, 5):
            def transformed(index: int) -> int:
                upper = FINITE_SUPPORT_MAX - index
                if upper < 0:
                    return 0
                return sum(
                    math.comb(post_size, k)
                    for k in range(upper + 1)
                )

            numerator = transformed(precursor_index + 1)
            denominator = transformed(precursor_index)
            ratio = Fraction(numerator, denominator)
            leading_target = Fraction(
                FINITE_SUPPORT_MAX - precursor_index,
                post_size,
            )
            rows.append(
                {
                    "post_size": post_size,
                    "precursor_index": precursor_index,
                    "exact_ratio": str(ratio),
                    "ratio_float": float(ratio),
                    "p_times_ratio_over_M_minus_n": (
                        float(ratio / leading_target)
                    ),
                }
            )
    return {
        "family": (
            f"t_m=1 for 0<=m<={FINITE_SUPPORT_MAX}, t_m=0 afterward"
        ),
        "asymptotic": "T_(n+1)/T_n~(M-n)/P",
        "rows": rows,
    }


def log_binomial(post_size: int, k: int) -> float:
    if k < 0 or k > post_size:
        return -math.inf
    return (
        math.lgamma(post_size + 1.0)
        - math.lgamma(k + 1.0)
        - math.lgamma(post_size - k + 1.0)
    )


def sparse_post_sum(post_size: int, precursor_index: int) -> float:
    """Martin--O'Connor--Rideout--Sorkin sparse counterexample."""

    lower = precursor_index
    upper = precursor_index + post_size
    power = 1
    total = -math.inf
    while power < lower:
        power *= 2
    while power <= upper:
        k = power - precursor_index
        total = logaddexp(
            total,
            log_binomial(post_size, k) + math.log(float(power)),
        )
        power *= 2
    return total


def sparse_counterexample_control() -> dict[str, object]:
    windows = []
    start = 64
    while start < SPARSE_SCAN_MAX:
        end = min(2 * start - 1, SPARSE_SCAN_MAX)
        minimum = (math.inf, -1)
        maximum = (-math.inf, -1)
        for post_size in range(start, end + 1):
            ratio = math.exp(
                sparse_post_sum(post_size, 2)
                - sparse_post_sum(post_size, 1)
            )
            if ratio < minimum[0]:
                minimum = (ratio, post_size)
            if ratio > maximum[0]:
                maximum = (ratio, post_size)
        windows.append(
            {
                "post_size_window": [start, end],
                "minimum_ratio": minimum[0],
                "argmin": minimum[1],
                "maximum_ratio": maximum[0],
                "argmax": maximum[1],
            }
        )
        start *= 2
    return {
        "family": "t_m=m at powers of two and 0 otherwise",
        "literature_role": (
            "published counterexample showing unrestricted post flows "
            "need not converge"
        ),
        "windows": windows,
    }


def exponential_fixed_point_control() -> dict[str, object]:
    u = 0.37
    maximum_index = max(POST_SIZES) + 16
    logs = [index * math.log(u) for index in range(maximum_index + 1)]
    rows = []
    for post_size in POST_SIZES:
        for precursor_index in (1, 2, 5):
            ratio = effective_ratio(post_size, precursor_index, logs)
            rows.append(
                {
                    "post_size": post_size,
                    "precursor_index": precursor_index,
                    "ratio": ratio,
                    "absolute_error": abs(ratio - u),
                }
            )
    return {
        "family": "t_m=u^m",
        "u": u,
        "rows": rows,
    }


def linear_slope(xs: Iterable[float], ys: Iterable[float]) -> float:
    x_values = list(xs)
    y_values = list(ys)
    mean_x = sum(x_values) / len(x_values)
    mean_y = sum(y_values) / len(y_values)
    return sum(
        (x - mean_x) * (y - mean_y)
        for x, y in zip(x_values, y_values)
    ) / sum((x - mean_x) ** 2 for x in x_values)


def main() -> None:
    semigroup = exact_semigroup_control()
    power = power_tail_control()
    log_corrected = log_corrected_control()
    finite_support = finite_support_control()
    sparse = sparse_counterexample_control()
    fixed_point = exponential_fixed_point_control()

    power_families = power["families"]
    largest_power_rows = {
        key: value["rows"][-1]
        for key, value in power_families.items()
    }
    log_rows = log_corrected["rows"]
    finite_rows = finite_support["rows"]
    sparse_last = sparse["windows"][-1]

    checks = [
        {
            "name": "exact N-fold post map equals N elementary transforms",
            "pass": semigroup["exact_match"],
        },
        {
            "name": "transitive-percolation ratios are exact projective fixed points",
            "pass": max(
                row["absolute_error"] for row in fixed_point["rows"]
            ) < 2.0e-10,
        },
        {
            "name": (
                "all power-ratio tails converge toward the independently "
                "defined implicit scale b_P/P"
            ),
            "pass": all(
                row["maximum_relative_error"] < 0.16
                for row in largest_power_rows.values()
            ),
        },
        {
            "name": (
                "bounded-precursor uniformity error decreases across the "
                "finite post-size grid"
            ),
            "pass": all(
                family["rows"][-1]["maximum_relative_error"]
                < family["rows"][0]["maximum_relative_error"]
                for family in power_families.values()
            ),
        },
        {
            "name": (
                "distinct factorial-power tails recover their distinct "
                "-alpha/(alpha+1) exponents"
            ),
            "pass": all(
                family["absolute_exponent_error"] < 0.035
                for family in power_families.values()
            ),
        },
        {
            "name": (
                "a logarithmic tail correction is captured by the implicit "
                "scale rather than a pure-power prefactor"
            ),
            "pass": (
                abs(log_rows[-1]["ratio_over_implicit_target"] - 1.0)
                < 0.14
                and log_rows[-1]["ratio_over_pure_power_without_log"]
                > log_rows[0]["ratio_over_pure_power_without_log"]
            ),
        },
        {
            "name": "finite support reaches the P^-1 endpoint",
            "pass": max(
                abs(row["p_times_ratio_over_M_minus_n"] - 1.0)
                for row in finite_rows
                if row["post_size"] == 4096
            ) < 0.01,
        },
        {
            "name": (
                "the published sparse boundary counterfamily retains "
                "widely separated post-ratio subsequences"
            ),
            "pass": (
                sparse_last["minimum_ratio"] < 0.65
                and sparse_last["maximum_ratio"] > 1.65
            ),
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)
    payload = {
        "probe": "du_csg_post_tail_uniformity_probe",
        "claim_grade": (
            "LOCAL ANALYTIC THEOREM WITH DETERMINISTIC FINITE CONTROLS; "
            "CAUSAL-SET NOVELTY PROVISIONAL"
        ),
        "question": (
            "Which tail property of a CSG coupling sequence determines the "
            "post-conditioned effective percolation ratio, uniformly over "
            "an early bounded-precursor sector?"
        ),
        "frozen_object": {
            "post_map": (
                "T_n(P)=sum_(k=0)^P binom(P,k)t_(n+k)"
            ),
            "physical_projective_sector": (
                "n>=1; T_0 is irrelevant after a post"
            ),
            "tail_class": (
                "eventually positive nonincreasing adjacent ratios "
                "r_m=t_(m+1)/t_m, regularly varying with index -alpha<0"
            ),
            "scale": (
                "b_P chosen independently by P r_(b_P)/b_P -> 1"
            ),
            "uniform_window": "1<=n<=h(P), h(P)=o(b_P)",
        },
        "analytic_result": {
            "general": (
                "sup_(1<=n<=h(P)) "
                "|[T_(n+1)(P)/T_n(P)]/[b_P/P]-1| -> 0"
            ),
            "power_ratio_corollary": (
                "r_m~u m^-alpha implies "
                "T_(n+1)/T_n~u^(1/(alpha+1)) "
                "P^(-alpha/(alpha+1)) uniformly"
            ),
            "factorial_half_power": (
                "t_m=u^m/m! is alpha=1 and gives sqrt(u/P)"
            ),
        },
        "controls": {
            "exact_semigroup": semigroup,
            "exponential_fixed_point": fixed_point,
            "power_tails": power,
            "log_corrected_tail": log_corrected,
            "finite_support_endpoint": finite_support,
            "sparse_nonconvergent_boundary": sparse,
        },
        "figure_data": {
            "figure_1_power_tail_collapse": {
                key: [
                    {
                        "post_size": row["post_size"],
                        "ratio_n1": row["effective_ratios"]["1"],
                        "implicit_target": row[
                            "implicit_target_b_over_P"
                        ],
                    }
                    for row in family["rows"]
                ]
                for key, family in power_families.items()
            },
            "figure_2_boundary_classes": {
                "log_corrected": log_rows,
                "finite_support": finite_rows,
                "sparse_windows": sparse["windows"],
            },
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "PAPER_CORE_SURVIVES / HALF_POWER_IS_ONE "
            "REGULAR-RATIO TAIL CLASS / GENERAL CSG UNIVERSALITY FALSE"
        ),
        "not_earned": [
            "selection of a physical CSG coupling sequence",
            "generation or recurrence of posts",
            "manifoldlike geometry or a continuum limit",
            "a unit-bearing physical scale",
            "a cosmological-constant identity",
            "a quantum causal-set result",
            "final causal-set literature novelty",
        ],
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("DU CSG POST-TAIL UNIFORMITY PROBE")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    for key, family in power_families.items():
        print(
            f"alpha={key}: predicted={family['predicted_exponent']:.6f}, "
            f"fitted={family['fitted_exponent']:.6f}, "
            f"largest-P max-uniform-error="
            f"{family['rows'][-1]['maximum_relative_error']:.6f}"
        )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")
    if passed != len(checks):
        failed = [
            check["name"] for check in checks if not check["pass"]
        ]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
