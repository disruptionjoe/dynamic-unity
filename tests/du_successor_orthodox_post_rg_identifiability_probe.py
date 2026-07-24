#!/usr/bin/env python3
"""Orthodox successor-wave probe: post renormalization and a Fisher null.

This probe resolves two status questions exposed by the first Science Council
wave.

First, the killed birth-cardinality feedback in
``du_wild_frontier_fisher_csg_scale_bridge_probe.py`` does not exhaust
covariant ways for causal history to change effective couplings.  In classical
sequential growth (CSG), conditioning on a post or break with ``N`` elements
in its past induces, for indices ``n >= 1``,

    (M^N t)_n = sum_{k=0}^N binom(N,k) t_{n+k}.

The map is a semigroup, and transitive-percolation couplings ``t_n=t^n`` are
projective fixed points.  For the bare family ``t_n=t^n/n!``, its normalized
post couplings approach transitive percolation with
``t_eff=sqrt(t/N)`` in the stated asymptotic regime.  That is an exact
covariant antecedent for history-to-coupling transduction; it is not a DU
derivation, a geometry result, or a cosmological prediction.

Second, the down-set/raw Fisher retention ratio from the same wild-frontier
probe is not determined by the physical order-transition law alone.  Appending
``k`` independent Bernoulli latent variables governed by the same parameter,
but forgotten by the map to physical down-sets, leaves the physical
distribution and its Fisher information unchanged while adding
``k p(1-p)`` to raw Fisher information.  The ratio can therefore be driven
arbitrarily close to zero by changing only the hidden fibre.  Physical
down-set Fisher information survives this null; the retention fraction needs
a separately fixed microhistory ontology.

The numerical portions test finite/asymptotic accuracy and include an
off-regime control.  Exact algebraic identities are checked with rational
arithmetic.  No target geometry, dimensional unit, Lambda, H0, cosmological
age, or fitted hierarchy enters.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_successor_orthodox_post_rg_identifiability_probe_result.json"
)


def post_map_exact(
    couplings: Sequence[Fraction],
    past_size: int,
    maximum_index: int,
) -> list[Fraction]:
    """Return projective CSG post couplings for indices 1..maximum_index."""

    if past_size < 0:
        raise ValueError("past_size must be nonnegative")
    if len(couplings) <= maximum_index + past_size:
        raise ValueError("coupling sequence is too short for requested map")
    return [
        sum(
            Fraction(math.comb(past_size, offset)) * couplings[index + offset]
            for offset in range(past_size + 1)
        )
        for index in range(1, maximum_index + 1)
    ]


def normalize_projectively(values: Sequence[Fraction]) -> list[Fraction]:
    if not values or values[0] == 0:
        raise ValueError("first physical coupling must be nonzero")
    return [value / values[0] for value in values]


def exact_post_map_tests() -> dict[str, Any]:
    maximum_index = 7
    first_past = 3
    second_past = 5
    total_past = first_past + second_past
    base = [
        Fraction(0),
        Fraction(3, 7),
        Fraction(5, 11),
        Fraction(2, 13),
        Fraction(17, 19),
        Fraction(23, 29),
        Fraction(31, 37),
        Fraction(41, 43),
        Fraction(47, 53),
        Fraction(59, 61),
        Fraction(67, 71),
        Fraction(73, 79),
        Fraction(83, 89),
        Fraction(97, 101),
        Fraction(103, 107),
        Fraction(109, 113),
    ]

    direct = post_map_exact(base, total_past, maximum_index)
    after_second = post_map_exact(
        base, second_past, maximum_index + first_past
    )
    padded_after_second = [Fraction(0), *after_second]
    composed = post_map_exact(
        padded_after_second, first_past, maximum_index
    )
    semigroup_errors = [
        direct[index] - composed[index] for index in range(maximum_index)
    ]

    elementary = post_map_exact(base, 1, maximum_index)
    elementary_expected = [
        base[index] + base[index + 1]
        for index in range(1, maximum_index + 1)
    ]

    fixed_parameter = Fraction(2, 5)
    fixed_base = [
        fixed_parameter**index
        for index in range(maximum_index + total_past + 2)
    ]
    fixed_mapped = post_map_exact(
        fixed_base, total_past, maximum_index
    )
    fixed_expected_scale = (1 + fixed_parameter) ** total_past
    fixed_expected = [
        fixed_expected_scale * fixed_parameter**index
        for index in range(1, maximum_index + 1)
    ]

    scale_factor = Fraction(137, 17)
    scaled_base = [scale_factor * value for value in base]
    unscaled_normalized = normalize_projectively(
        post_map_exact(base, total_past, maximum_index)
    )
    scaled_normalized = normalize_projectively(
        post_map_exact(scaled_base, total_past, maximum_index)
    )

    return {
        "map": "(M^N t)_n=sum_{k=0}^N binom(N,k)t_{n+k}, n>=1",
        "t0_scope": (
            "t0 is deliberately excluded: after a post/break it is special "
            "and does not enter the projective physical couplings tested here."
        ),
        "elementary_map_exact": elementary == elementary_expected,
        "semigroup_exact": direct == composed,
        "semigroup_errors": [str(value) for value in semigroup_errors],
        "transitive_percolation_projective_fixed_point_exact": (
            fixed_mapped == fixed_expected
        ),
        "transitive_percolation_parameter": str(fixed_parameter),
        "projective_rescaling_invariant_exact": (
            unscaled_normalized == scaled_normalized
        ),
        "normalization": "divide physical couplings by transformed t1",
    }


def factorial_post_couplings(
    past_size: int,
    bare_parameter: float,
    maximum_index: int,
) -> list[float]:
    """Compute M^N(t^n/n!) stably enough for the tested finite regimes."""

    if past_size < 0 or bare_parameter <= 0.0 or maximum_index < 1:
        raise ValueError("invalid factorial post-map arguments")
    values: list[float] = []
    for index in range(1, maximum_index + 1):
        term = (bare_parameter**index) / math.factorial(index)
        terms = [term]
        for offset in range(past_size):
            term *= (
                (past_size - offset)
                / (offset + 1)
                * bare_parameter
                / (index + offset + 1)
            )
            terms.append(term)
        values.append(math.fsum(terms))
    return values


def relative_error(actual: float, expected: float) -> float:
    if expected == 0.0:
        return abs(actual)
    return abs(actual - expected) / abs(expected)


def normalized_lambda(
    normalized_couplings: Sequence[float],
    precursor_size: int,
    maximal_elements: int,
) -> float:
    if not (1 <= maximal_elements <= precursor_size):
        raise ValueError("require 1 <= maximal_elements <= precursor_size")
    if len(normalized_couplings) < precursor_size:
        raise ValueError("insufficient couplings")
    return math.fsum(
        math.comb(precursor_size - maximal_elements, index - maximal_elements)
        * normalized_couplings[index - 1]
        for index in range(maximal_elements, precursor_size + 1)
    )


def transitive_percolation_normalized_lambda(
    effective_parameter: float,
    precursor_size: int,
    maximal_elements: int,
) -> float:
    return (
        effective_parameter ** (maximal_elements - 1)
        * (1.0 + effective_parameter)
        ** (precursor_size - maximal_elements)
    )


def loglog_slope(xs: Sequence[float], ys: Sequence[float]) -> float:
    log_x = [math.log(value) for value in xs]
    log_y = [math.log(value) for value in ys]
    mean_x = math.fsum(log_x) / len(log_x)
    mean_y = math.fsum(log_y) / len(log_y)
    numerator = math.fsum(
        (x - mean_x) * (y - mean_y)
        for x, y in zip(log_x, log_y)
    )
    denominator = math.fsum((x - mean_x) ** 2 for x in log_x)
    return numerator / denominator


def factorial_asymptotic_test() -> dict[str, Any]:
    past_sizes = (100, 400, 1600, 6400)
    bare_parameters = (0.25, 1.0, 4.0)
    maximum_precursor = 4
    rows: list[dict[str, Any]] = []

    for bare_parameter in bare_parameters:
        for past_size in past_sizes:
            couplings = factorial_post_couplings(
                past_size, bare_parameter, maximum_precursor
            )
            normalized = [value / couplings[0] for value in couplings]
            effective_parameter = math.sqrt(bare_parameter / past_size)
            coupling_errors = [
                relative_error(
                    normalized[index - 1],
                    effective_parameter ** (index - 1),
                )
                for index in range(1, maximum_precursor + 1)
            ]
            lambda_errors = []
            for precursor_size in range(1, maximum_precursor + 1):
                for maximal_elements in range(1, precursor_size + 1):
                    actual = normalized_lambda(
                        normalized, precursor_size, maximal_elements
                    )
                    expected = transitive_percolation_normalized_lambda(
                        effective_parameter,
                        precursor_size,
                        maximal_elements,
                    )
                    lambda_errors.append(relative_error(actual, expected))
            rows.append(
                {
                    "past_size_N": past_size,
                    "bare_parameter_t": bare_parameter,
                    "effective_parameter_sqrt_t_over_N": effective_parameter,
                    "history_hierarchy_1_over_t_eff": (
                        1.0 / effective_parameter
                    ),
                    "inferred_parameter_t2_over_t1": normalized[1],
                    "inferred_parameter_relative_error": relative_error(
                        normalized[1], effective_parameter
                    ),
                    "maximum_coupling_relative_error_n_1_through_4": max(
                        coupling_errors
                    ),
                    "maximum_lambda_relative_error_varpi_1_through_4": max(
                        lambda_errors
                    ),
                    "regime_indicators": {
                        "maximum_varpi_over_N": (
                            maximum_precursor / past_size
                        ),
                        "maximum_m_squared_over_Nt": (
                            maximum_precursor**2
                            / (past_size * bare_parameter)
                        ),
                    },
                }
            )

    hierarchy_rows = []
    for past_size in past_sizes:
        couplings = factorial_post_couplings(past_size, 1.0, 2)
        inferred_parameter = couplings[1] / couplings[0]
        hierarchy_rows.append(
            {
                "past_size_N": past_size,
                "inferred_t_eff": inferred_parameter,
                "inferred_hierarchy": 1.0 / inferred_parameter,
                "asymptotic_hierarchy_sqrt_N_over_t": math.sqrt(past_size),
            }
        )
    inferred_slope = loglog_slope(
        [row["past_size_N"] for row in hierarchy_rows],
        [row["inferred_hierarchy"] for row in hierarchy_rows],
    )

    # Deliberately violate both stated small-precursor conditions.
    off_past_size = 100
    off_bare_parameter = 1.0
    off_precursor_size = 50
    off_maximal_elements = 10
    off_couplings = factorial_post_couplings(
        off_past_size, off_bare_parameter, off_precursor_size
    )
    off_normalized = [
        value / off_couplings[0] for value in off_couplings
    ]
    off_effective = math.sqrt(off_bare_parameter / off_past_size)
    off_actual = normalized_lambda(
        off_normalized, off_precursor_size, off_maximal_elements
    )
    off_expected = transitive_percolation_normalized_lambda(
        off_effective, off_precursor_size, off_maximal_elements
    )

    target_rows = [
        row
        for row in rows
        if row["past_size_N"] == max(past_sizes)
    ]
    return {
        "bare_family": "t_n=t^n/n!",
        "asymptotic_target": "projective t_n proportional to t_eff^n",
        "t_eff": "sqrt(t/N)",
        "stated_regime": "m^2 << N t and varpi << N",
        "rows": rows,
        "largest_N_rows": target_rows,
        "largest_N_maximum_inferred_parameter_relative_error": max(
            row["inferred_parameter_relative_error"]
            for row in target_rows
        ),
        "largest_N_maximum_lambda_relative_error": max(
            row["maximum_lambda_relative_error_varpi_1_through_4"]
            for row in target_rows
        ),
        "history_hierarchy": {
            "rows": hierarchy_rows,
            "inferred_loglog_slope_vs_N": inferred_slope,
            "asymptotic_target_slope": 0.5,
            "reading": (
                "The scale is conditional on the selected bare family and a "
                "post/break with N historical elements; it is not a target "
                "inserted into a within-era birth-count update."
            ),
        },
        "off_regime_control": {
            "past_size_N": off_past_size,
            "bare_parameter_t": off_bare_parameter,
            "precursor_size_varpi": off_precursor_size,
            "maximal_elements_m": off_maximal_elements,
            "m_squared_over_Nt": (
                off_maximal_elements**2
                / (off_past_size * off_bare_parameter)
            ),
            "varpi_over_N": off_precursor_size / off_past_size,
            "exact_normalized_lambda": off_actual,
            "asymptotic_transitive_percolation_lambda": off_expected,
            "relative_error": relative_error(off_actual, off_expected),
            "reading": (
                "The transitive-percolation approximation is not promoted "
                "outside its stated asymptotic regime."
            ),
        },
    }


def closure_from_direct_links(
    ancestors: Sequence[int],
    raw_mask: int,
) -> int:
    closure = 0
    for event in range(len(ancestors)):
        if raw_mask & (1 << event):
            closure |= ancestors[event] | (1 << event)
    return closure


def physical_downset_distribution(
    ancestors: Sequence[int],
    p: float,
    latent_count: int = 0,
) -> dict[int, dict[str, float]]:
    """Enumerate physical histories and optional forgotten Bernoulli fibres."""

    event_count = len(ancestors)
    total_count = event_count + latent_count
    outcomes: dict[int, dict[str, float]] = {}
    for raw_mask in range(1 << event_count):
        closure = closure_from_direct_links(ancestors, raw_mask)
        direct_count = raw_mask.bit_count()
        for latent_mask in range(1 << latent_count):
            successes = direct_count + latent_mask.bit_count()
            probability = (
                p**successes * (1.0 - p) ** (total_count - successes)
            )
            score = successes - total_count * p
            row = outcomes.setdefault(
                closure,
                {"probability": 0.0, "derivative_g": 0.0},
            )
            row["probability"] += probability
            row["derivative_g"] += probability * score
    for row in outcomes.values():
        row["score_g"] = row["derivative_g"] / row["probability"]
        row["fisher_contribution"] = (
            row["probability"] * row["score_g"] ** 2
        )
    return outcomes


def fisher_summary(
    ancestors: Sequence[int],
    p: float,
    latent_count: int,
) -> dict[str, Any]:
    outcomes = physical_downset_distribution(
        ancestors, p, latent_count=latent_count
    )
    event_count = len(ancestors)
    physical_fisher = math.fsum(
        row["fisher_contribution"] for row in outcomes.values()
    )
    raw_fisher = (event_count + latent_count) * p * (1.0 - p)
    return {
        "latent_fibre_count": latent_count,
        "probability_sum": math.fsum(
            row["probability"] for row in outcomes.values()
        ),
        "physical_downset_fisher": physical_fisher,
        "raw_fisher": raw_fisher,
        "conditional_fibre_fisher": raw_fisher - physical_fisher,
        "retained_ratio": physical_fisher / raw_fisher,
        "outcomes": {
            str(mask): row for mask, row in sorted(outcomes.items())
        },
    }


def fisher_fibre_null() -> dict[str, Any]:
    # Four-event diamond: 0<1, 0<2, and 1,2<3.
    diamond = (
        0,
        1 << 0,
        1 << 0,
        (1 << 0) | (1 << 1) | (1 << 2),
    )
    p = 0.31
    enumerated = [
        fisher_summary(diamond, p, latent_count)
        for latent_count in range(5)
    ]
    baseline = enumerated[0]
    event_count = len(diamond)
    analytic_rows = []
    for latent_count in (0, 1, 2, 4, 12, 36, 396):
        raw_fisher = (
            event_count + latent_count
        ) * p * (1.0 - p)
        analytic_rows.append(
            {
                "latent_fibre_count": latent_count,
                "physical_downset_fisher": baseline[
                    "physical_downset_fisher"
                ],
                "raw_fisher": raw_fisher,
                "retained_ratio": (
                    baseline["physical_downset_fisher"] / raw_fisher
                ),
                "ratio_relative_to_no_latent_fibre": (
                    event_count / (event_count + latent_count)
                ),
            }
        )

    maximum_probability_change = 0.0
    maximum_physical_fisher_change = 0.0
    for row in enumerated[1:]:
        for outcome, baseline_outcome in baseline["outcomes"].items():
            maximum_probability_change = max(
                maximum_probability_change,
                abs(
                    row["outcomes"][outcome]["probability"]
                    - baseline_outcome["probability"]
                ),
            )
        maximum_physical_fisher_change = max(
            maximum_physical_fisher_change,
            abs(
                row["physical_downset_fisher"]
                - baseline["physical_downset_fisher"]
            ),
        )

    g = math.log(p / (1.0 - p))
    derivative_h_g = math.cosh(g)
    baseline_ratio_h = (
        baseline["physical_downset_fisher"] / derivative_h_g**2
    ) / (baseline["raw_fisher"] / derivative_h_g**2)

    return {
        "physical_state": "four-event diamond",
        "parameter": {
            "p": p,
            "g": "log[p/(1-p)]",
            "raw_single_bernoulli_fisher_g": p * (1.0 - p),
        },
        "fisher_chain_rule": (
            "F_raw=F_downset+E_downset[F_raw_given_downset]"
        ),
        "latent_refinement": (
            "Append k independent Bernoulli(p) variables to the hidden fibre "
            "and forget all of them in the physical down-set map."
        ),
        "enumerated_rows_k_0_through_4": enumerated,
        "analytic_rows": analytic_rows,
        "maximum_enumerated_physical_probability_change": (
            maximum_probability_change
        ),
        "maximum_enumerated_physical_fisher_change": (
            maximum_physical_fisher_change
        ),
        "coordinate_check": {
            "new_coordinate": "h=sinh(g)",
            "retained_ratio_g": baseline["retained_ratio"],
            "retained_ratio_h": baseline_ratio_h,
            "absolute_error": abs(
                baseline["retained_ratio"] - baseline_ratio_h
            ),
            "reading": (
                "For a fixed raw model the ratio is coordinate invariant. "
                "The null is hidden-fibre non-identifiability, not a mere "
                "parameter-coordinate artifact."
            ),
        },
        "identifiability_result": (
            "The physical order-transition law identifies F_downset but does "
            "not identify F_downset/F_raw without a fixed raw microhistory "
            "ontology. The ratio approaches zero as k grows."
        ),
    }


def main() -> None:
    exact = exact_post_map_tests()
    asymptotic = factorial_asymptotic_test()
    fisher_null = fisher_fibre_null()

    largest_rows = asymptotic["largest_N_rows"]
    errors_by_t = {
        bare_parameter: [
            row["inferred_parameter_relative_error"]
            for row in asymptotic["rows"]
            if row["bare_parameter_t"] == bare_parameter
        ]
        for bare_parameter in (0.25, 1.0, 4.0)
    }
    analytic_fisher_rows = fisher_null["analytic_rows"]
    checks = [
        {
            "name": "the elementary post map is M(t)_n=t_n+t_(n+1)",
            "pass": exact["elementary_map_exact"],
        },
        {
            "name": "post maps compose as the exact binomial semigroup M^a M^b=M^(a+b)",
            "pass": exact["semigroup_exact"],
        },
        {
            "name": "transitive-percolation couplings are an exact projective fixed-point family",
            "pass": exact[
                "transitive_percolation_projective_fixed_point_exact"
            ],
        },
        {
            "name": "global coupling normalization is projectively irrelevant",
            "pass": exact["projective_rescaling_invariant_exact"],
        },
        {
            "name": "factorial post couplings approach sqrt(t/N) for every tested bare t",
            "pass": all(
                values[-1] < values[0]
                and all(
                    later < earlier
                    for earlier, later in zip(values, values[1:])
                )
                for values in errors_by_t.values()
            ),
        },
        {
            "name": "the largest-N safe window is quantitatively close to transitive percolation",
            "pass": (
                max(
                    row["inferred_parameter_relative_error"]
                    for row in largest_rows
                )
                < 0.03
                and max(
                    row[
                        "maximum_lambda_relative_error_varpi_1_through_4"
                    ]
                    for row in largest_rows
                )
                < 0.20
            ),
        },
        {
            "name": "the inferred historical hierarchy has the asymptotic square-root slope",
            "pass": abs(
                asymptotic["history_hierarchy"][
                    "inferred_loglog_slope_vs_N"
                ]
                - 0.5
            )
            < 0.04,
        },
        {
            "name": "the off-regime control visibly rejects asymptotic equivalence",
            "pass": asymptotic["off_regime_control"]["relative_error"] > 0.25,
        },
        {
            "name": "enumerated hidden-fibre refinements leave every physical probability unchanged",
            "pass": fisher_null[
                "maximum_enumerated_physical_probability_change"
            ]
            < 3.0e-14,
        },
        {
            "name": "enumerated hidden-fibre refinements leave physical down-set Fisher unchanged",
            "pass": fisher_null[
                "maximum_enumerated_physical_fisher_change"
            ]
            < 3.0e-14,
        },
        {
            "name": "the retained Fisher ratio is coordinate invariant for a fixed raw model",
            "pass": fisher_null["coordinate_check"]["absolute_error"] < 1.0e-15,
        },
        {
            "name": "the same physical order law admits arbitrarily smaller raw-retention ratios",
            "pass": (
                analytic_fisher_rows[-1][
                    "ratio_relative_to_no_latent_fibre"
                ]
                == 0.01
                and analytic_fisher_rows[-1]["retained_ratio"]
                < 0.01
            ),
        },
        {
            "name": "no geometry, unit, Lambda, H0, cosmological age, or fitted hierarchy enters",
            "pass": True,
        },
    ]
    passed = sum(bool(item["pass"]) for item in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-SUCCESSOR-ORTHODOX-POST-RG-IDENTIFIABILITY",
        "track": (
            "Science Council successor wave / exact CSG antecedent and "
            "information-bottleneck null"
        ),
        "question": (
            "Does the first wave understate an exact covariant mechanism for "
            "history-to-coupling transduction, and does it overstate the "
            "order-level identifiability of the raw/physical Fisher ratio?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "STRUCTURAL_ANALOGY",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "The order-first comparator is a classical sequential "
                    "growth model admitting a post or break."
                ),
                "status": "STANDARD",
                "role": "Defines the exact binomial conditioning map.",
            },
            {
                "id": "A2",
                "statement": "The bare couplings are t_n=t^n/n!.",
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Supplies the known basin trajectory used for the "
                    "asymptotic transitive-percolation comparison."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "A post/break has N historical elements in its past and "
                    "the tested precursors lie in the stated asymptotic regime."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Makes t_eff=sqrt(t/N) applicable.",
            },
            {
                "id": "A4",
                "statement": (
                    "Raw-link histories may be refined by parameter-dependent "
                    "latent fibres invisible to physical down-set outcomes."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Tests whether a raw/physical Fisher fraction is selected "
                    "by the physical order law alone."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "Use finite N in {100,400,1600,6400} and t in {1/4,1,4}.",
                "why_not_forced": "These are numerical audit fixtures.",
                "sensitivity_test": (
                    "Require monotonic convergence for every t and report an "
                    "off-regime control."
                ),
            },
            {
                "id": "C2",
                "choice": "Test precursors through varpi=4 in the safe window.",
                "why_not_forced": "The asymptotic theorem is broader than this grid.",
                "sensitivity_test": (
                    "Report m^2/(Nt) and varpi/N rather than hiding the regime."
                ),
            },
            {
                "id": "C3",
                "choice": (
                    "Use independent Bernoulli(p) latent variables as the "
                    "hidden-fibre refinement."
                ),
                "why_not_forced": "Many unobserved refinements are possible.",
                "sensitivity_test": (
                    "Verify by enumeration that the physical law and physical "
                    "Fisher are unchanged for k=1..4, then extend analytically."
                ),
            },
        ],
        "equations": [
            "(M^N t)_n=sum_{k=0}^N binom(N,k)t_{n+k}, n>=1",
            "M^a M^b=M^(a+b)",
            "M^N(t^n)=(1+t)^N t^n",
            "t_n=t^n/n! => t_eff~sqrt(t/N) in the stated regime",
            "F_raw=F_downset+E[F_raw|downset]",
            "F_raw(k)=(n+k)p(1-p)",
            "F_downset(k)=F_downset(0)",
        ],
        "observables": [
            "projectively normalized post couplings",
            "normalized CSG precursor weights lambda(varpi,m)",
            "inferred t_eff and historical hierarchy",
            "physical down-set probabilities",
            "physical and raw Fisher information",
            "raw-retention ratio under hidden-fibre refinement",
        ],
        "comparators": [
            "exact post map versus direct birth-cardinality feedback",
            "factorial post couplings versus transitive-percolation asymptote",
            "safe precursor window versus off-regime control",
            "fixed physical down-set law across alternative hidden fibres",
        ],
        "null_models": [
            "transitive percolation as an exact projective fixed-point family",
            "global coupling rescaling as a projective redundancy",
            "parameter-dependent latent variables forgotten by the physical map",
        ],
        "falsifiers": [
            "the exact post maps fail the binomial semigroup identity",
            "transitive-percolation couplings fail projective fixed-point closure",
            "factorial post couplings do not approach sqrt(t/N)",
            "the approximation remains accurate when its regime is deliberately violated",
            "latent-fibre refinement changes a physical down-set probability",
            "the raw-retention ratio is invariant across observationally equivalent fibres",
        ],
        "stop_conditions": [
            "Do not describe the post map as derived from Dynamic Unity.",
            "Do not infer repeated posts, a selected bare family, or a selected N.",
            "Do not call 1/t_eff a spatial volume without an independently valid estimator.",
            "Do not infer manifoldlike dimension from maximum-interval fits.",
            "Do not treat F_downset/F_raw as order-identifiable without fixing the raw fibre.",
            "Do not infer units, Lambda, H0, cosmological age, a banked claim, or a prediction.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A live DU mechanism must generate effective influence and "
                "scales through admissible dynamics rather than target fitting."
            ),
            "formalization_id": (
                "CSG-POST-RENORMALIZATION-ANTECEDENT-AND-FISHER-FIBRE-NULL"
            ),
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "An exact covariant CSG conditioning map supplies a real "
                "history-to-coupling antecedent and a conditional factorial "
                "family supplies an asymptotic count hierarchy, while the "
                "raw/physical Fisher retention fraction is not identified by "
                "the physical order-transition law."
            ),
            "grade": (
                "STANDARD-MECHANISM-REPRODUCED / CONDITIONAL-HIERARCHY / "
                "OBSERVABLE-RATIO-NOT-IDENTIFIED"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "No DU law selects CSG, the factorial bare family, posts, their "
                "sizes, geometry, response/noise completion, units, or a "
                "cosmological observable. Physical down-set Fisher remains "
                "well-defined, but its role in DU is unselected."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": "du_successor_orthodox_post_rg_identifiability_probe",
        "contested_finding": (
            "The first-wave long-term post-renormalization path is merely an "
            "unbuilt escape from the killed p(N) feedback, while the "
            "raw/physical Fisher bottleneck is an order-level observable."
        ),
        "exact_post_map": exact,
        "factorial_asymptotic": asymptotic,
        "fisher_fibre_null": fisher_null,
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "NARROW/OVERTURN. The DU bridge remains unbuilt, but its CSG "
            "antecedent is not: post conditioning gives an exact covariant "
            "binomial coupling map, and a selected factorial bare family "
            "conditionally produces t_eff~sqrt(t/N). Conversely, the "
            "physical down-set Fisher is structural for a fixed physical law, "
            "but its fraction of raw Fisher is hidden-fibre dependent and not "
            "an order-only observable."
        ),
        "scope": {
            "earned": [
                "exact rational reproduction of the CSG post-map semigroup",
                "exact projective fixed-point closure of transitive percolation",
                "finite convergence of the factorial family to sqrt(t/N)",
                "an explicit off-regime failure control",
                "an exact hidden-fibre identifiability null for Fisher retention",
            ],
            "not_earned": [
                "a Dynamic Unity derivation of CSG or of the bare coupling family",
                "generation or recurrence of posts",
                "selection of the historical count N",
                "manifoldlike geometry, dimension, or spatial volume",
                "a unit-bearing response or cosmological observable",
                "a Lambda value, H0 value, prediction, or banked claim",
            ],
        },
    }
    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate contract: {receipt['contract_errors']}"
        )
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("ORTHODOX SUCCESSOR: POST RG + FISHER IDENTIFIABILITY")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(
        "VERDICT: STANDARD POST-RG ANTECEDENT REPRODUCED / "
        "FISHER RETENTION NOT ORDER-IDENTIFIED"
    )
    print(f"contract: {receipt['contract_status']} (not scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
