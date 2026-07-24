#!/usr/bin/env python3
"""Philosopher-successor probe for causal-post scale identifiability.

This probe separates four claims that are easy to collapse:

1. a causal post induces an exact, projectively defined conditional coupling
   map;
2. the conditional future law depends on the invariant size of the post's
   past;
3. that dependence constitutes active, online feedback; and
4. the resulting half-power is a physical cosmological-constant identity.

For classical sequential-growth couplings ``t_n``, conditioning on a post
with ``p`` ancestors gives

    tilde(t)_n^(p) = sum_{k=0}^p binom(p,k) t_{n+k}.

Only projective ratios of the post-era couplings matter.  For the family

    t_n = t^n / (n!)^alpha,

a saddle estimate predicts

    tilde(t)_{n+1}/tilde(t)_n
        ~ t^(1/(alpha+1)) p^(-alpha/(alpha+1))

in the appropriate large-p, fixed-n regime.  The famous half-power is the
``alpha=1`` member, not a consequence of post conditioning alone.

The identifiability countermodel is exact.  At one observed post-past size
``p0``, a model whose future law is obtained by post conditioning and a model
whose frozen fundamental law is set equal to that same projective effective
law have identical post-era transition measures.  A fixed-history replay
therefore cannot identify the origin of the law.  Changing the invariant past
while holding the bare family fixed does distinguish them.  Conversely,
freezing the already conditioned law within one era defeats an *online active
feedback* interpretation without defeating history dependence.

No Lambda, physical units, sign, stress tensor, geometry recovery, or
cosmological calibration enters this probe.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_successor_philosopher_post_rg_identifiability_probe_result.json"
)


def logsumexp(values: Iterable[float]) -> float:
    rows = list(values)
    if not rows:
        raise ValueError("logsumexp requires at least one value")
    maximum = max(rows)
    return maximum + math.log(sum(math.exp(value - maximum) for value in rows))


def log_binomial(n: int, k: int) -> float:
    if not 0 <= k <= n:
        raise ValueError("binomial index out of range")
    return (
        math.lgamma(n + 1.0)
        - math.lgamma(k + 1.0)
        - math.lgamma(n - k + 1.0)
    )


def log_bare_coupling(
    n: int,
    *,
    t: float,
    alpha: float,
    projective_log_scale: float = 0.0,
) -> float:
    if n < 1 or t <= 0.0 or alpha < 0.0:
        raise ValueError("n>=1, t>0, and alpha>=0 are required")
    return (
        projective_log_scale
        + n * math.log(t)
        - alpha * math.lgamma(n + 1.0)
    )


def log_post_coupling(
    n: int,
    post_past: int,
    *,
    t: float,
    alpha: float,
    projective_log_scale: float = 0.0,
) -> float:
    if post_past < 0:
        raise ValueError("post_past must be nonnegative")
    return logsumexp(
        log_binomial(post_past, k)
        + log_bare_coupling(
            n + k,
            t=t,
            alpha=alpha,
            projective_log_scale=projective_log_scale,
        )
        for k in range(post_past + 1)
    )


def projective_law(
    post_past: int,
    *,
    t: float,
    alpha: float,
    maximum_n: int,
    projective_log_scale: float = 0.0,
) -> list[float]:
    logs = [
        log_post_coupling(
            n,
            post_past,
            t=t,
            alpha=alpha,
            projective_log_scale=projective_log_scale,
        )
        for n in range(1, maximum_n + 1)
    ]
    anchor = logs[0]
    return [math.exp(value - anchor) for value in logs]


def effective_ratios(
    post_past: int,
    *,
    t: float,
    alpha: float,
    maximum_n: int,
) -> list[float]:
    logs = [
        log_post_coupling(n, post_past, t=t, alpha=alpha)
        for n in range(1, maximum_n + 2)
    ]
    return [
        math.exp(logs[index + 1] - logs[index])
        for index in range(maximum_n)
    ]


def regression_slope(xs: list[float], ys: list[float]) -> float:
    log_x = [math.log(value) for value in xs]
    log_y = [math.log(value) for value in ys]
    mean_x = sum(log_x) / len(log_x)
    mean_y = sum(log_y) / len(log_y)
    numerator = sum(
        (x - mean_x) * (y - mean_y) for x, y in zip(log_x, log_y)
    )
    denominator = sum((x - mean_x) ** 2 for x in log_x)
    return numerator / denominator


def family_sweep() -> dict[str, Any]:
    t = 1.0
    post_pasts = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
    rows: dict[str, Any] = {}
    for alpha in (0.0, 1.0, 2.0):
        effective = [
            effective_ratios(
                post_past,
                t=t,
                alpha=alpha,
                maximum_n=1,
            )[0]
            for post_past in post_pasts
        ]
        predicted_exponent = -alpha / (alpha + 1.0)
        predicted_prefactor = t ** (1.0 / (alpha + 1.0))
        scaled = [
            ratio
            / (
                predicted_prefactor
                * post_past ** predicted_exponent
            )
            for post_past, ratio in zip(post_pasts, effective)
        ]
        rows[str(int(alpha))] = {
            "alpha": alpha,
            "post_pasts": post_pasts,
            "effective_ratio_t2_over_t1": effective,
            "measured_loglog_slope_last_five": regression_slope(
                [float(value) for value in post_pasts[-5:]],
                effective[-5:],
            ),
            "predicted_exponent": predicted_exponent,
            "asymptotic_scaled_ratio": scaled,
            "last_scaled_ratio": scaled[-1],
        }
    return {
        "bare_family": "t_n=t^n/(n!)^alpha",
        "t": t,
        "rows": rows,
        "reading": (
            "Post conditioning supplies a common exact map, but the running "
            "exponent is selected by the bare coupling family. Alpha=1 gives "
            "the half-power; alpha=0 gives no running; alpha=2 tends -2/3."
        ),
    }


def identifiability_countermodel() -> dict[str, Any]:
    t = 1.0
    alpha = 1.0
    p0 = 4096
    p1 = 16384
    maximum_n = 6

    historical_at_p0 = projective_law(
        p0, t=t, alpha=alpha, maximum_n=maximum_n
    )
    historical_at_p1 = projective_law(
        p1, t=t, alpha=alpha, maximum_n=maximum_n
    )

    # The theoretical frozen-law countermodel is assigned the full infinite
    # effective projective sequence at p0:
    #
    #   Q_F = (tilde_t_n^(p0)/tilde_t_1^(p0))_(n>=1).
    #
    # Its equality at that history is exact by definition and expresses
    # observational underdetermination, not a fit-quality claim.  This
    # executable fixture represents and checks only n=1..maximum_n.
    frozen_fundamental_at_p0 = list(historical_at_p0)
    within_history_difference = max(
        abs(left - right)
        for left, right in zip(
            historical_at_p0, frozen_fundamental_at_p0
        )
    )
    cross_history_difference = max(
        abs(left - right)
        for left, right in zip(historical_at_p0, historical_at_p1)
    )

    ratios_p0 = effective_ratios(
        p0, t=t, alpha=alpha, maximum_n=maximum_n - 1
    )
    ratios_p1 = effective_ratios(
        p1, t=t, alpha=alpha, maximum_n=maximum_n - 1
    )
    q0 = ratios_p0[0]
    q1 = ratios_p1[0]

    percolation_replay = [q0 ** (n - 1) for n in range(1, maximum_n + 1)]
    percolation_relative_errors = [
        abs(replay / historical - 1.0)
        for replay, historical in zip(
            percolation_replay, historical_at_p0
        )
    ]

    bare_projective = [
        math.exp(
            log_bare_coupling(n, t=t, alpha=alpha)
            - log_bare_coupling(1, t=t, alpha=alpha)
        )
        for n in range(1, maximum_n + 1)
    ]
    bare_replay_difference = max(
        abs(left - right)
        for left, right in zip(historical_at_p0, bare_projective)
    )

    return {
        "historical_model": {
            "bare_family": "t_n=t^n/n!",
            "post_map": (
                "tilde_t_n^(p)=sum_k binom(p,k)t_(n+k), projectivized at n=1"
            ),
            "p0": p0,
            "p1": p1,
            "projective_law_at_p0": historical_at_p0,
            "projective_law_at_p1": historical_at_p1,
            "effective_ratios_at_p0": ratios_p0,
            "effective_ratios_at_p1": ratios_p1,
            "q_effective_at_p0": q0,
            "q_effective_at_p1": q1,
            "q_ratio_p1_over_p0": q1 / q0,
            "half_power_prediction_for_ratio": math.sqrt(p0 / p1),
        },
        "frozen_law_countermodel": {
            "law": (
                "Take Q_F=(tilde_t_n^(p0)/tilde_t_1^(p0))_(n>=1) as the "
                "fundamental post-era law, with no edge from prehistory."
            ),
            "full_infinite_law_definition": (
                "Q_F=(tilde_t_n^(p0)/tilde_t_1^(p0))_(n>=1)"
            ),
            "represented_numeric_sector": f"n=1..{maximum_n}",
            "projective_law_at_p0": frozen_fundamental_at_p0,
            "represented_sector_max_difference": (
                within_history_difference
            ),
            "cross_history_intervention_max_difference": (
                cross_history_difference
            ),
        },
        "one_parameter_percolation_replay": {
            "q_frozen_from_first_effective_ratio": q0,
            "projective_law": percolation_replay,
            "relative_errors_by_n": percolation_relative_errors,
            "maximum_relative_error": max(percolation_relative_errors),
            "reading": (
                "A one-parameter percolation replay is only asymptotically "
                "close; the complete frozen effective vector is exactly "
                "observationally equivalent within the chosen era."
            ),
        },
        "bare_law_replay": {
            "projective_law": bare_projective,
            "maximum_absolute_difference_from_conditioned_law": (
                bare_replay_difference
            ),
            "reading": (
                "Resetting to the bare factorial law is a history intervention "
                "and changes the future measure; freezing the already "
                "conditioned law is not."
            ),
        },
        "identifiability": {
            "identified_by_one_fixed_history_replay": [
                "whether online coupling updates are needed within that era",
            ],
            "not_identified_by_one_fixed_history_replay": [
                "whether the frozen law was fundamental or inherited from prehistory",
                "whether invariant post-past cardinality changes conditional future probabilities",
                "whether the half-power is a Lambda identity",
            ],
            "minimum_discriminator": (
                "prehistory access or matched post ensembles with different "
                "invariant past cardinalities, bare family held fixed"
            ),
        },
    }


def main() -> None:
    sweep = family_sweep()
    countermodel = identifiability_countermodel()

    gauge_reference = projective_law(
        257, t=0.7, alpha=1.0, maximum_n=6
    )
    gauge_rescaled = projective_law(
        257,
        t=0.7,
        alpha=1.0,
        maximum_n=6,
        projective_log_scale=math.log(37.0),
    )
    gauge_error = max(
        abs(left - right)
        for left, right in zip(gauge_reference, gauge_rescaled)
    )

    alpha_rows = sweep["rows"]
    checks = [
        {
            "name": "common coupling rescaling is removed by projectivization",
            "pass": gauge_error < 2.0e-13,
        },
        {
            "name": "geometric bare couplings alpha=0 have no post-past running",
            "pass": abs(
                alpha_rows["0"]["measured_loglog_slope_last_five"]
            )
            < 2.0e-10,
        },
        {
            "name": "factorial bare couplings alpha=1 approach a half-power",
            "pass": abs(
                alpha_rows["1"]["measured_loglog_slope_last_five"] + 0.5
            )
            < 0.035,
        },
        {
            "name": "squared-factorial bare couplings alpha=2 approach a two-thirds power",
            "pass": abs(
                alpha_rows["2"]["measured_loglog_slope_last_five"]
                + 2.0 / 3.0
            )
            < 0.04,
        },
        {
            "name": "the post-induced exponent changes across admissible nonnegative coupling families",
            "pass": (
                alpha_rows["0"]["measured_loglog_slope_last_five"]
                - alpha_rows["2"]["measured_loglog_slope_last_five"]
                > 0.60
            ),
        },
        {
            "name": "the represented sector exactly matches the full-law frozen countermodel definition",
            "pass": countermodel["frozen_law_countermodel"][
                "represented_sector_max_difference"
            ]
            == 0.0,
        },
        {
            "name": "changing invariant post prehistory changes the conditional projective law",
            "pass": countermodel["frozen_law_countermodel"][
                "cross_history_intervention_max_difference"
            ]
            > 1.0e-4,
        },
        {
            "name": "the factorial effective coupling follows the predicted cross-history half-power ratio",
            "pass": abs(
                countermodel["historical_model"]["q_ratio_p1_over_p0"]
                - countermodel["historical_model"][
                    "half_power_prediction_for_ratio"
                ]
            )
            < 0.02,
        },
        {
            "name": "resetting to the bare law is distinguishable from freezing the conditioned law",
            "pass": countermodel["bare_law_replay"][
                "maximum_absolute_difference_from_conditioned_law"
            ]
            > 0.1,
        },
        {
            "name": "a one-parameter percolation replay is close but not identical on the finite fixture",
            "pass": (
                0.0
                < countermodel["one_parameter_percolation_replay"][
                    "maximum_relative_error"
                ]
                < 0.10
            ),
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    payload = {
        "probe": "du_successor_philosopher_post_rg_identifiability_probe",
        "contested_proposition": (
            "A fixed-history replay can by itself adjudicate whether "
            "causal-post renormalization genuinely generates an active scale."
        ),
        "primary_source_equations_recomputed": [
            "tilde_t_n^(p)=sum_(k=0)^p binom(p,k)t_(n+k)",
            "M(t)_n=t_n+t_(n+1)",
            "t_n=t^n/n! gives t_effective~sqrt(t/p) in its declared regime",
        ],
        "projective_gauge": {
            "reference": gauge_reference,
            "common_scale_times_37": gauge_rescaled,
            "maximum_difference": gauge_error,
        },
        "family_sweep": sweep,
        "identifiability_countermodel": countermodel,
        "typed_result": {
            "post_past_cardinality": (
                "INVARIANT PROPERTY OF THE ORDER, once a post and its past "
                "are specified; not a birth-label coordinate"
            ),
            "post_status": (
                "GLOBAL HISTORY CONDITION involving the future; an online "
                "trigger requires a separately observable finite-stem event"
            ),
            "effective_couplings": (
                "PROJECTIVE CONDITIONAL LAW / sufficient summary of excluded "
                "prehistory, not a demonstrated new fundamental law"
            ),
            "memory": (
                "SUPPORTED: changing matched invariant prehistory changes the "
                "conditional future measure"
            ),
            "online_feedback_within_era": (
                "NOT SUPPORTED: the complete conditioned law can be frozen "
                "without changing that era's transition measure"
            ),
            "generated_hierarchy": (
                "CONDITIONALLY REALIZED AS HISTORICAL LARGE-NUMBER "
                "TRANSDUCTION; exponent and value remain bare-family/history dependent"
            ),
            "physical_scale": (
                "NOT IDENTIFIED: a microscopic unit, geometry map, and "
                "observable identity are absent"
            ),
            "lambda_identity": (
                "NOT IDENTIFIED: exponent coincidence supplies neither units, "
                "sign, coefficient, stress response, nor observable equality"
            ),
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "CONTESTED PROPOSITION NARROWED. Fixed-history replay can defeat "
            "an online-feedback interpretation within one post era, but it "
            "cannot identify whether the frozen effective law was fundamental "
            "or inherited from invariant prehistory. Cross-history "
            "interventions recover the latter distinction. The half-power is "
            "factorial-family-conditional and is not a Lambda identity."
        ),
        "forbidden_overclaims": [
            "the vote establishes the mechanism",
            "post conditioning changes the fundamental CSG law",
            "a global post is necessarily available as an online trigger",
            "historical large-number transduction is parameter-free scale creation",
            "sqrt(1/p) is Lambda because the exponent matches",
            "finite originary-percolation de Sitter fits establish continuum recovery",
        ],
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("PHILOSOPHER SUCCESSOR — POST-RG IDENTIFIABILITY")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    for key in ("0", "1", "2"):
        row = alpha_rows[key]
        print(
            f"alpha={key}: slope="
            f"{row['measured_loglog_slope_last_five']:.6f}, "
            f"predicted={row['predicted_exponent']:.6f}"
        )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
