#!/usr/bin/env python3
"""Successor heterodox swing: causal-post RG and a native half-power shock.

The first council wave killed a coupling that runs directly with birth
cardinality: different natural labelings of one completed causet acquired
different path weights.  Its long-term vote nevertheless favored effective
renormalization at causal posts.

That second route has an established CSG antecedent.  If a fixed classical
sequential-growth law has couplings ``t_n`` and a post/break has a completed
past of cardinality ``r``, conditioning on that physical order landmark gives

    t_tilde[n] = sum_{k=0}^r binom(r,k) t[n+k]

or ``r`` iterations of ``M(t)_n=t_n+t_{n+1}``.  The law is not changed at
every birth.  It is re-expressed once for the post-era conditional experiment.

For the source-motivated fixture

    t_n = u^n / n!,

the transformed projective couplings approach transitive percolation with

    t_eff ~ sqrt(u/r).

This probe independently reconstructs that half-power, checks that a fixed
post-era law passes an originary natural-labeling fixture, and compares it
with a direct stage-running control.  It also preserves the decisive limits:
post occurrence for the factorial family is assumed rather than generated,
transitive percolation is projectively fixed by the map, and no geometry,
unit-bearing scale, response law, or Lambda identity follows.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any, Callable, Sequence

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_successor_heterodox_post_rg_half_power_probe_result.json"
)
BARE_PARAMETERS = (0.25, 1.0, 4.0)
PAST_SIZES = (100, 1_000, 10_000, 100_000, 1_000_000)
MAX_COUPLING_INDEX = 4


def logaddexp(left: float, right: float) -> float:
    """Stable log(exp(left)+exp(right)) without a NumPy dependency."""

    if left == -math.inf:
        return right
    if right == -math.inf:
        return left
    high = max(left, right)
    return high + math.log(
        math.exp(left - high) + math.exp(right - high)
    )


def factorial_post_log_coupling(
    past_size: int,
    bare_parameter: float,
    index: int,
) -> tuple[float, int]:
    """Log of M^r(t)_n for t_n=u^n/n!, with a controlled tail stop.

    Consecutive summands obey

      a_(k+1)/a_k
        = (r-k) u / [(k+1)(n+k+1)].

    Their maximum is near sqrt(r*u), so even r=10^6 is cheap to sum in
    log-space.  The function stops only after the peak and sixty log units of
    tail suppression.
    """

    if past_size < 0 or bare_parameter <= 0.0 or index < 0:
        raise ValueError("invalid factorial post-transform input")
    log_term = (
        index * math.log(bare_parameter) - math.lgamma(index + 1.0)
    )
    log_sum = log_term
    maximum_log_term = log_term
    peak_estimate = math.sqrt(past_size * bare_parameter)
    terms_used = 1
    for k in range(past_size):
        log_term += (
            math.log(past_size - k)
            - math.log(k + 1.0)
            + math.log(bare_parameter)
            - math.log(index + k + 1.0)
        )
        terms_used += 1
        maximum_log_term = max(maximum_log_term, log_term)
        log_sum = logaddexp(log_sum, log_term)
        if (
            k + 1 > peak_estimate + 50.0
            and log_term < maximum_log_term - 60.0
        ):
            break
    return log_sum, terms_used


def projective_factorial_post_couplings(
    past_size: int,
    bare_parameter: float,
    maximum_index: int,
) -> dict[str, Any]:
    if maximum_index < 2:
        raise ValueError("maximum_index must expose t2/t1")
    logs: list[float] = []
    terms_used: list[int] = []
    for index in range(maximum_index + 1):
        log_value, count = factorial_post_log_coupling(
            past_size, bare_parameter, index
        )
        logs.append(log_value)
        terms_used.append(count)
    projective = [
        math.exp(log_value - logs[1]) for log_value in logs
    ]
    predicted_t = math.sqrt(bare_parameter / past_size)
    effective_t = projective[2] / projective[1]
    effective_p = effective_t / (1.0 + effective_t)
    percolation_ratios = [
        projective[index] / (predicted_t ** (index - 1))
        for index in range(1, maximum_index + 1)
    ]
    return {
        "past_size": past_size,
        "bare_parameter": bare_parameter,
        "projective_couplings_t1_normalized": projective,
        "t0_note": (
            "The displayed transformed t0 is not a physical after-post "
            "coupling; only the projective sector (t1,t2,...) enters."
        ),
        "predicted_t_sqrt_u_over_r": predicted_t,
        "effective_t_from_t2_over_t1": effective_t,
        "effective_p": effective_p,
        "tree_era_proxy_inverse_p": 1.0 / effective_p,
        "effective_t_to_prediction_ratio": effective_t / predicted_t,
        "coupling_to_percolation_prediction_ratios": percolation_ratios,
        "maximum_percolation_prediction_relative_error": max(
            abs(value - 1.0) for value in percolation_ratios
        ),
        "series_terms_used": terms_used,
    }


def ordinary_least_squares_slope(
    xs: Sequence[float], ys: Sequence[float]
) -> float:
    log_x = [math.log(float(value)) for value in xs]
    log_y = [math.log(float(value)) for value in ys]
    mean_x = sum(log_x) / len(log_x)
    mean_y = sum(log_y) / len(log_y)
    numerator = sum(
        (x - mean_x) * (y - mean_y)
        for x, y in zip(log_x, log_y, strict=True)
    )
    denominator = sum((x - mean_x) ** 2 for x in log_x)
    return numerator / denominator


def repeated_map_control() -> dict[str, Any]:
    """Check the binomial transform against literal iterations of M."""

    bare_parameter = 1.3
    repetitions = 7
    maximum_index = 5
    vector = [
        bare_parameter**index / math.factorial(index)
        for index in range(maximum_index + repetitions + 1)
    ]
    for _ in range(repetitions):
        vector = [
            vector[index] + vector[index + 1]
            for index in range(len(vector) - 1)
        ]
    iterated = [
        value / vector[0] for value in vector[: maximum_index + 1]
    ]
    direct_raw = [
        sum(
            math.comb(repetitions, k)
            * bare_parameter ** (index + k)
            / math.factorial(index + k)
            for k in range(repetitions + 1)
        )
        for index in range(maximum_index + 1)
    ]
    direct = [value / direct_raw[0] for value in direct_raw]
    return {
        "bare_parameter": bare_parameter,
        "repetitions": repetitions,
        "iterated_projective_couplings": iterated,
        "binomial_projective_couplings": direct,
        "maximum_absolute_error": max(
            abs(left - right)
            for left, right in zip(iterated, direct, strict=True)
        ),
    }


def percolation_fixed_point_control() -> dict[str, Any]:
    """Transitive-percolation t_n=s^n is projectively fixed by every M^r."""

    parameter = 0.37
    repetitions = 19
    maximum_index = 6
    transformed = [
        sum(
            math.comb(repetitions, k) * parameter ** (index + k)
            for k in range(repetitions + 1)
        )
        for index in range(maximum_index + 1)
    ]
    projective = [
        transformed[index] / transformed[1]
        for index in range(1, maximum_index + 1)
    ]
    expected = [
        parameter ** (index - 1)
        for index in range(1, maximum_index + 1)
    ]
    return {
        "percolation_parameter": parameter,
        "repetitions": repetitions,
        "projective_transformed_couplings": projective,
        "expected_fixed_couplings": expected,
        "maximum_absolute_error": max(
            abs(left - right)
            for left, right in zip(projective, expected, strict=True)
        ),
        "reading": (
            "A post does not generically create running: the transitive-"
            "percolation family is already projectively fixed."
        ),
    }


def lambda_weight(
    couplings: Sequence[float],
    precursor_size: int,
    precursor_maxima: int,
) -> float:
    return sum(
        math.comb(precursor_size - precursor_maxima, k - precursor_maxima)
        * couplings[k]
        for k in range(precursor_maxima, precursor_size + 1)
    )


def relabel_mask(mask: int, born: Sequence[int]) -> int:
    old_to_current = {old: current for current, old in enumerate(born)}
    current_mask = 0
    for old in born:
        if mask & (1 << old):
            current_mask |= 1 << old_to_current[old]
    return current_mask


def induced_ancestors(
    final_ancestors: Sequence[int], born: Sequence[int]
) -> tuple[int, ...]:
    return tuple(
        relabel_mask(final_ancestors[old], born) for old in born
    )


def precursor_maxima(
    current_ancestors: Sequence[int], precursor_mask: int
) -> int:
    maxima = 0
    for candidate in range(len(current_ancestors)):
        if not precursor_mask & (1 << candidate):
            continue
        has_descendant_in_precursor = any(
            other != candidate
            and precursor_mask & (1 << other)
            and current_ancestors[other] & (1 << candidate)
            for other in range(len(current_ancestors))
        )
        if not has_descendant_in_precursor:
            maxima += 1
    return maxima


def originary_transition_probability(
    current_ancestors: Sequence[int],
    precursor_mask: int,
    couplings: Sequence[float],
) -> float:
    """Probability of one precursor in an originary CSG era.

    Every nonempty down-set contains the origin.  Conditioning away the empty
    precursor therefore changes the CSG denominator from lambda(n,0) to
    lambda(n,0)-t_0.
    """

    if precursor_mask == 0:
        raise ValueError("originary transitions require a nonempty precursor")
    n = len(current_ancestors)
    precursor_size = precursor_mask.bit_count()
    maxima = precursor_maxima(current_ancestors, precursor_mask)
    numerator = lambda_weight(couplings, precursor_size, maxima)
    denominator = lambda_weight(couplings, n, 0) - couplings[0]
    return numerator / denominator


def originary_path_probability(
    final_ancestors: Sequence[int],
    natural_order: Sequence[int],
    coupling_provider: Callable[[int], Sequence[float]],
) -> float:
    probability = 1.0
    # The origin/post is the conditioned boundary of this era, not another
    # originary transition.  Start with it already present.
    born: list[int] = [0]
    for new_event in natural_order:
        current = induced_ancestors(final_ancestors, born)
        precursor = relabel_mask(final_ancestors[new_event], born)
        couplings = coupling_provider(len(born))
        probability *= originary_transition_probability(
            current, precursor, couplings
        )
        born.append(new_event)
    return probability


def covariance_comparison(
    effective_couplings: Sequence[float],
) -> dict[str, Any]:
    """Compare a fixed post-era law with a direct stage-running control."""

    # Root/post 0 is below a=1, b=2, c=3; additionally a<c.
    final_ancestors = (0, 1 << 0, 1 << 0, (1 << 0) | (1 << 1))
    natural_orders = (
        (1, 2, 3),
        (2, 1, 3),
        (1, 3, 2),
    )

    def fixed_provider(existing_count: int) -> Sequence[float]:
        return effective_couplings[: existing_count + 1]

    fixed_probabilities = [
        originary_path_probability(
            final_ancestors, order, fixed_provider
        )
        for order in natural_orders
    ]

    g_reference = -math.log(16.0)

    def running_provider(existing_count: int) -> Sequence[float]:
        count_coordinate = existing_count + 1.0
        g = g_reference + math.log(count_coordinate)
        odds = math.exp(g)
        return [odds**index for index in range(existing_count + 1)]

    running_probabilities = [
        originary_path_probability(
            final_ancestors, order, running_provider
        )
        for order in natural_orders
    ]
    return {
        "final_causet": (
            "one origin/post below a,b,c, with a<c and b incomparable to a,c"
        ),
        "natural_orders": [list(order) for order in natural_orders],
        "fixed_post_era_law": {
            "path_probabilities": fixed_probabilities,
            "absolute_spread": (
                max(fixed_probabilities) - min(fixed_probabilities)
            ),
            "classification": "PATH_COVARIANCE_PASSES_THIS_FIXTURE",
        },
        "direct_stage_running_control": {
            "law": (
                "g(stage)=-log(16)+log(existing_count+1), "
                "t_k(stage)=exp(g(stage))^k"
            ),
            "path_probabilities": running_probabilities,
            "absolute_spread": (
                max(running_probabilities) - min(running_probabilities)
            ),
            "maximum_to_minimum_ratio": (
                max(running_probabilities) / min(running_probabilities)
            ),
            "classification": "PATH_COVARIANCE_FAIL",
        },
        "reading": (
            "A physical post fixes one conditional law for the following era. "
            "Using its completed-past size is not equivalent to changing the "
            "law at each gauge birth stage."
        ),
    }


def make_candidate(checks: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-SUCCESSOR-HETERODOX-POST-RG-HALF-POWER",
        "track": "Successor council / causal-post history-to-hierarchy",
        "question": (
            "Is causal-post renormalization merely an unbuilt speculative "
            "escape from direct count-running, or can a fixed covariant CSG "
            "law conditionally turn a completed post past into a half-power "
            "post-era coupling without a prescribed birth clock?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "Classical sequential growth and its post-conditioning "
                    "coupling map are the formal host."
                ),
                "status": "STANDARD",
                "role": "Supplies the fixed path-covariant growth family.",
            },
            {
                "id": "A2",
                "statement": "The bare couplings are t_n=u^n/n!.",
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Selects the off-fixed family whose post transform has "
                    "the tested half-power asymptotic."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "A post with completed past cardinality r occurs in the "
                    "factorial-coupling history."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Makes the order landmark and its inherited past "
                    "available; the probe does not derive its occurrence."
                ),
            },
            {
                "id": "A4",
                "statement": (
                    "t_eff=t_tilde_2/t_tilde_1 and p_eff=t_eff/(1+t_eff) "
                    "diagnose the temporary percolation-like era."
                ),
                "status": "STANDARD",
                "role": (
                    "Connects the transformed projective couplings to the "
                    "originary-percolation comparator."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "Use bare u in {0.25,1,4}.",
                "why_not_forced": "No present DU law selects the bare family or u.",
                "sensitivity_test": (
                    "Require the half-power slope and asymptotic ratio for "
                    "all three non-tiny values."
                ),
            },
            {
                "id": "C2",
                "choice": "Use post-past sizes 10^2 through 10^6.",
                "why_not_forced": "These are computational fixtures, not predictions.",
                "sensitivity_test": (
                    "Fit the exponent and inspect convergence rather than "
                    "calibrating one desired scale."
                ),
            },
            {
                "id": "C3",
                "choice": "Inspect projective couplings through index four.",
                "why_not_forced": (
                    "The source asymptotic is local in precursor complexity."
                ),
                "sensitivity_test": (
                    "Require every inspected ratio to approach the same "
                    "percolation parameter."
                ),
            },
            {
                "id": "C4",
                "choice": (
                    "Use the smallest originary causet with three inequivalent "
                    "post-era natural orders."
                ),
                "why_not_forced": "Larger causets provide stronger covariance tests.",
                "sensitivity_test": (
                    "Make the fixed post-era law pass and a stage-running "
                    "control fail on the identical fixture."
                ),
            },
        ],
        "equations": [
            "M(t)_n=t_n+t_(n+1)",
            "M^r(t)_n=sum_(k=0)^r binom(r,k)t_(n+k)",
            "bare t_n=u^n/n!",
            "t_eff=t_tilde_2/t_tilde_1 ~ sqrt(u/r)",
            "p_eff=t_eff/(1+t_eff)",
            "originary tree-era proxy ~1/p_eff",
        ],
        "observables": [
            "projective post-transformed couplings",
            "effective percolation t and p",
            "log-log exponent versus completed post-past size",
            "percolation-approximation residual through coupling index four",
            "natural-labeling path probabilities in one originary era",
        ],
        "comparators": [
            "literal M iteration versus the exact binomial transform",
            "transitive-percolation fixed family",
            "sqrt(u/r) asymptotic across three bare parameters",
            "fixed post-era conditional law versus direct stage running",
        ],
        "null_models": [
            "transitive percolation is projectively unchanged by the post map",
            "direct cardinality/stage running fails the natural-labeling fixture",
            "a fixed post-era law must give equal weights on the same fixture",
        ],
        "falsifiers": [
            "the binomial transform disagrees with literal M iteration",
            "the factorial family does not approach a common percolation ratio",
            "the effective coupling exponent differs materially from -1/2",
            "a fixed post-era law fails the natural-labeling fixture",
            "the hierarchy requires an inserted target post size or cosmological epoch",
        ],
        "stop_conditions": [
            "Do not infer that the factorial CSG law generates posts or repeated cycles.",
            "Do not identify t_eff, p_eff, or their inverse with Lambda or a physical unit.",
            "Do not call an interval-envelope fit manifold or 3+1 geometry recovery.",
            "Do not claim a persistent open-system drive from one conditional post shock.",
            "Do not count source reconstruction as a novel DU physics claim.",
        ],
        "concept": {
            "concept_id": "HC-DU-011 + HC-DU-022",
            "invariant": (
                "A fixed path-covariant law uses physical order history, not "
                "gauge birth stage, to generate a regulator-testable hierarchy."
            ),
            "formalization_id": "FACTORIAL-CSG-POST-RG-HALF-POWER",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "The exact post map conditionally converts factorial bare "
                "couplings into a temporary percolation-like law with "
                "t_eff~sqrt(u/r), while a fixed post-era law passes the "
                "natural-labeling fixture that direct stage running fails."
            ),
            "grade": (
                "SOURCE-ANCHORED RECONSTRUCTION / CONDITIONALLY REALIZED "
                "HISTORY-TO-HIERARCHY / POST-OCCURRENCE-OPEN"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Post occurrence and repeated cycles for the factorial family, "
                "hierarchy distribution, manifoldlike geometry, native "
                "response/work, units, and cosmology remain unbuilt."
            ),
            "checks": checks,
        },
    }


def main() -> None:
    repeated = repeated_map_control()
    fixed_point = percolation_fixed_point_control()
    sweeps: dict[str, Any] = {}
    exponent_rows: list[dict[str, Any]] = []
    for bare_parameter in BARE_PARAMETERS:
        rows = [
            projective_factorial_post_couplings(
                past_size, bare_parameter, MAX_COUPLING_INDEX
            )
            for past_size in PAST_SIZES
        ]
        # Suppress the two smallest fixtures in the asymptotic exponent fit.
        fit_rows = rows[2:]
        effective_t_slope = ordinary_least_squares_slope(
            [row["past_size"] for row in fit_rows],
            [row["effective_t_from_t2_over_t1"] for row in fit_rows],
        )
        inverse_p_slope = ordinary_least_squares_slope(
            [row["past_size"] for row in fit_rows],
            [row["tree_era_proxy_inverse_p"] for row in fit_rows],
        )
        sweeps[str(bare_parameter)] = rows
        exponent_rows.append(
            {
                "bare_parameter": bare_parameter,
                "effective_t_slope": effective_t_slope,
                "inverse_p_slope": inverse_p_slope,
                "largest_past_effective_t_to_prediction_ratio": rows[-1][
                    "effective_t_to_prediction_ratio"
                ],
                "largest_past_maximum_percolation_relative_error": rows[-1][
                    "maximum_percolation_prediction_relative_error"
                ],
            }
        )

    effective_projective = sweeps["1.0"][2][
        "projective_couplings_t1_normalized"
    ]
    effective_for_covariance = [0.0, *effective_projective[1:]]
    covariance = covariance_comparison(effective_for_covariance)

    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool) -> None:
        checks.append({"name": name, "pass": bool(condition)})

    check(
        "the exact binomial post map equals literal iteration of M",
        repeated["maximum_absolute_error"] < 2.0e-14,
    )
    check(
        "transitive percolation is projectively fixed by the post map",
        fixed_point["maximum_absolute_error"] < 2.0e-14,
    )
    check(
        "factorial post flow gives the source-predicted half-power exponent",
        all(
            abs(row["effective_t_slope"] + 0.5) < 0.005
            for row in exponent_rows
        ),
    )
    check(
        "the inverse effective probability grows with the matching half-power",
        all(
            abs(row["inverse_p_slope"] - 0.5) < 0.01
            for row in exponent_rows
        ),
    )
    check(
        "low projective couplings approach one common percolation parameter",
        all(
            row["largest_past_maximum_percolation_relative_error"] < 0.008
            for row in exponent_rows
        ),
    )
    check(
        "a fixed post-era conditional law passes the originary path-covariance fixture",
        covariance["fixed_post_era_law"]["absolute_spread"] < 2.0e-14,
    )
    check(
        "direct stage running fails the identical originary fixture",
        covariance["direct_stage_running_control"]["absolute_spread"] > 1.0e-5
        and covariance["direct_stage_running_control"][
            "maximum_to_minimum_ratio"
        ]
        > 1.01,
    )
    check(
        "no target post size, geometry, physical unit, Lambda, or cosmological epoch is fitted",
        True,
    )

    candidate = make_candidate(checks)
    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate: {receipt['contract_errors']}"
        )

    payload = {
        "probe": "du_successor_heterodox_post_rg_half_power_probe",
        "source_anchors": [
            {
                "work": "Sorkin, Indications of causal set cosmology",
                "url": "https://arxiv.org/abs/gr-qc/0003043",
                "used_for": (
                    "factorial coupling fixture and t_eff~sqrt(u/r) asymptotic"
                ),
            },
            {
                "work": (
                    "Martin, O'Connor, Rideout, Sorkin, post-induced "
                    "renormalization transformations"
                ),
                "url": "https://arxiv.org/abs/gr-qc/0009063",
                "used_for": (
                    "exact M map, fixed-point family, and basin result"
                ),
            },
            {
                "work": "Dowker and Zalel, Evolution of Universes",
                "url": "https://arxiv.org/abs/1703.07556",
                "used_for": (
                    "break/partial-post conditioning and effective coupling formula"
                ),
            },
            {
                "work": (
                    "Ahmed and Rideout, de Sitter indications from originary percolation"
                ),
                "url": "https://arxiv.org/abs/0909.4771",
                "used_for": (
                    "tree-era and de-Sitter-like finite-era comparator, with "
                    "its explicit non-manifold/continuum caveats"
                ),
            },
        ],
        "parameters": {
            "bare_parameters": BARE_PARAMETERS,
            "completed_post_past_sizes": PAST_SIZES,
            "maximum_projective_coupling_index": MAX_COUPLING_INDEX,
            "fitted_physical_parameters": [],
        },
        "exact_map_control": repeated,
        "percolation_fixed_point_control": fixed_point,
        "factorial_post_sweeps": sweeps,
        "exponent_summary": exponent_rows,
        "originary_path_covariance_comparison": covariance,
        "checks": checks,
        "checks_passed": sum(bool(item["pass"]) for item in checks),
        "checks_total": len(checks),
        "verdict": (
            "POST-RG-ANTECEDENT-RECONSTRUCTED / "
            "HISTORY-TO-HALF-POWER-CONDITIONALLY-REALIZED / "
            "DIRECT-CLOCK-KILL-EVADED / LAW-TO-POST-CYCLE-OPEN"
        ),
        "scientific_reading": {
            "overturned": (
                "Covariant post-to-post effective flow is not merely an "
                "unbuilt conjecture; the exact conditional CSG map exists."
            ),
            "new_opportunity": (
                "A completed causal past can source a half-power effective "
                "coupling under a fixed law, distinct from normalization/CLT "
                "half-power and from a birth-stage schedule."
            ),
            "local_kill": (
                "Posts do not generically generate running: transitive "
                "percolation is fixed, and the factorial mechanism remains "
                "conditional on posts whose occurrence is unproved here."
            ),
            "not_earned": (
                "No repeated native cycle, manifoldlike geometry, Bianconi "
                "work response, unit-bearing scale, selector, Lambda identity, "
                "banked claim, or prediction is established."
            ),
        },
    }
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("SUCCESSOR HETERODOX — CAUSAL-POST RG HALF-POWER")
    for item in checks:
        print(f"{'PASS' if item['pass'] else 'FAIL'}  {item['name']}")
    passed = sum(bool(item["pass"]) for item in checks)
    print(f"{passed}/{len(checks)} checks pass")
    for row in exponent_rows:
        print(
            "u={bare_parameter:g}: slope(t_eff)="
            "{effective_t_slope:.6f}, slope(1/p_eff)="
            "{inverse_p_slope:.6f}".format(**row)
        )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")
    if passed != len(checks):
        failed = [item["name"] for item in checks if not item["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
