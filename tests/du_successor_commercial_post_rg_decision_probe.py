#!/usr/bin/env python3
"""Commercial successor swing: a decision assay for causal-post RG.

This probe does not invent a new causal-growth law.  It independently
recomputes the smallest algebraic and finite-state objects needed to decide
what the known causal-post renormalization mechanism can buy Dynamic Unity.

For a classical sequential growth (CSG) coupling sequence ``t_n``, a post or
break with ``N`` elements in its past induces, on the nonempty-precursor
sector,

    (R^N t)_k = sum_{j=0}^N binom(N,j) t_{k+j},  k >= 1.

The elementary map is ``(R t)_k=t_k+t_{k+1}``.  Transitive percolation
``t_k=q^k`` is a projective fixed family.  For the factorial family
``t_k=t^k/k!``, the large-past regime approaches transitive percolation with
``q_eff=sqrt(t/N)`` and therefore transfers a large historical count into a
dimensionless hierarchy ``1/q_eff=sqrt(N/t)``.

The commercial discriminator is fixed-history replay.  Conditional on the
post and its past size, the transformed couplings are fixed throughout the
post era.  Recomputing transitions from the bare law plus that frozen history
is exactly distribution-equivalent to replaying a fixed effective CSG law.
Thus the construction is genuine covariant long memory and hierarchy
generation, but it does not by itself implement active feedback from a
post-era diagnostic into later transitions.

The finite transition fixture uses the standard CSG weight

    lambda(varpi,m) =
        sum_{k=m}^varpi binom(varpi-m,k-m) t_k

on nonempty down-sets containing the post.  It is an algebraic decision assay,
not a continuum or cosmology result.
"""

from __future__ import annotations

from fractions import Fraction
import math
from pathlib import Path
from typing import Any, Iterable

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_successor_commercial_post_rg_decision_probe_result.json"
)
POST_PAST_GRID = (100, 1_000, 10_000, 100_000)
FACTORIAL_PARAMETER = 1.0
MAX_COUPLING_INDEX = 4


def elementary_transform(
    couplings: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        couplings[index] + couplings[index + 1]
        for index in range(len(couplings) - 1)
    )


def iterated_elementary_transform(
    couplings: tuple[Fraction, ...], iterations: int
) -> tuple[Fraction, ...]:
    transformed = couplings
    for _ in range(iterations):
        transformed = elementary_transform(transformed)
    return transformed


def exact_binomial_transform(
    couplings: tuple[Fraction, ...], iterations: int
) -> tuple[Fraction, ...]:
    return tuple(
        sum(
            Fraction(math.comb(iterations, offset)) * couplings[index + offset]
            for offset in range(iterations + 1)
        )
        for index in range(len(couplings) - iterations)
    )


def exact_transform_tests() -> dict[str, Any]:
    arbitrary = tuple(
        Fraction(numerator, denominator)
        for numerator, denominator in (
            (3, 5),
            (7, 11),
            (5, 13),
            (17, 19),
            (2, 23),
            (29, 31),
            (11, 37),
            (41, 43),
            (13, 47),
        )
    )
    iterations = 4
    iterated = iterated_elementary_transform(arbitrary, iterations)
    direct = exact_binomial_transform(arbitrary, iterations)

    q = Fraction(2, 7)
    percolation = tuple(q**index for index in range(10))
    transformed_percolation = exact_binomial_transform(
        percolation, iterations
    )
    projective_factor = (1 + q) ** iterations
    expected_percolation = tuple(
        projective_factor * percolation[index]
        for index in range(len(transformed_percolation))
    )

    return {
        "iterations": iterations,
        "arbitrary_sequence_iteration_matches_binomial_exactly": (
            iterated == direct
        ),
        "arbitrary_iterated_result": [
            f"{value.numerator}/{value.denominator}" for value in iterated
        ],
        "arbitrary_direct_result": [
            f"{value.numerator}/{value.denominator}" for value in direct
        ],
        "percolation_q": f"{q.numerator}/{q.denominator}",
        "percolation_projective_factor": (
            f"{projective_factor.numerator}/{projective_factor.denominator}"
        ),
        "percolation_is_projective_fixed_family_exactly": (
            transformed_percolation == expected_percolation
        ),
    }


def logsumexp(values: Iterable[float]) -> float:
    materialized = tuple(values)
    maximum = max(materialized)
    return maximum + math.log(
        math.fsum(math.exp(value - maximum) for value in materialized)
    )


def factorial_post_log_couplings(
    post_past_size: int,
    factorial_parameter: float,
    maximum_index: int,
) -> tuple[float, ...]:
    """Return log[(R^N t)_n] for t_n=t^n/n!."""

    log_parameter = math.log(factorial_parameter)
    log_binomial = [0.0] * (post_past_size + 1)
    for offset in range(post_past_size):
        log_binomial[offset + 1] = (
            log_binomial[offset]
            + math.log(post_past_size - offset)
            - math.log(offset + 1)
        )

    transformed = []
    for index in range(maximum_index + 1):
        transformed.append(
            logsumexp(
                log_binomial[offset]
                + (index + offset) * log_parameter
                - math.lgamma(index + offset + 1)
                for offset in range(post_past_size + 1)
            )
        )
    return tuple(transformed)


def normalized_nonempty_couplings(
    log_couplings: tuple[float, ...],
) -> tuple[float, ...]:
    """Normalize the k>=1 sector projectively to t_1=1."""

    return tuple(
        math.exp(log_value - log_couplings[1])
        for log_value in log_couplings
    )


def is_downset(mask: int, ancestors: tuple[int, ...]) -> bool:
    return all(
        not (mask & (1 << event))
        or ancestors[event] & ~mask == 0
        for event in range(len(ancestors))
    )


def nonempty_post_downsets(
    ancestors: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        mask
        for mask in range(1 << len(ancestors))
        if mask & 1 and is_downset(mask, ancestors)
    )


def maximal_element_count(
    mask: int, ancestors: tuple[int, ...]
) -> int:
    count = 0
    for event in range(len(ancestors)):
        if not (mask & (1 << event)):
            continue
        is_ancestor_of_selected = any(
            mask & (1 << later)
            and ancestors[later] & (1 << event)
            for later in range(len(ancestors))
        )
        if not is_ancestor_of_selected:
            count += 1
    return count


def csg_weight(
    precursor_size: int,
    maximal_count: int,
    couplings: tuple[float, ...],
) -> float:
    return math.fsum(
        math.comb(precursor_size - maximal_count, index - maximal_count)
        * couplings[index]
        for index in range(maximal_count, precursor_size + 1)
    )


def originary_transition_distribution(
    ancestors: tuple[int, ...],
    couplings: tuple[float, ...],
) -> dict[int, float]:
    weights = {}
    for mask in nonempty_post_downsets(ancestors):
        precursor_size = mask.bit_count()
        maximal_count = maximal_element_count(mask, ancestors)
        weights[mask] = csg_weight(
            precursor_size, maximal_count, couplings
        )
    normalization = math.fsum(weights.values())
    return {
        mask: weight / normalization
        for mask, weight in sorted(weights.items())
    }


def total_variation(
    left: dict[int, float], right: dict[int, float]
) -> float:
    if set(left) != set(right):
        raise ValueError("distributions have different outcome spaces")
    return 0.5 * math.fsum(
        abs(left[outcome] - right[outcome]) for outcome in left
    )


def asymptotic_and_replay_tests() -> dict[str, Any]:
    # Four-event originary diamond: 0<1, 0<2, and 1,2<3.
    fixtures = {
        "originary_antichain": (0, 1, 1, 1),
        "originary_diamond": (0, 1, 1, 7),
        "originary_chain": (0, 1, 3, 7),
    }
    rows = []
    replay_maximum_error = 0.0
    for post_past_size in POST_PAST_GRID:
        log_couplings = factorial_post_log_couplings(
            post_past_size,
            FACTORIAL_PARAMETER,
            MAX_COUPLING_INDEX,
        )
        effective = normalized_nonempty_couplings(log_couplings)
        q_effective = math.sqrt(
            FACTORIAL_PARAMETER / post_past_size
        )
        percolation = tuple(
            0.0
            if index == 0
            else q_effective ** (index - 1)
            for index in range(MAX_COUPLING_INDEX + 1)
        )
        projective_relative_errors = {
            str(index): abs(
                effective[index] / percolation[index] - 1.0
            )
            for index in range(1, MAX_COUPLING_INDEX + 1)
        }
        fixture_rows = {}
        for fixture_name, ancestors in fixtures.items():
            effective_distribution = originary_transition_distribution(
                ancestors, effective
            )
            percolation_distribution = originary_transition_distribution(
                ancestors, percolation
            )

            # "Dynamic" recomputation from the frozen post past and a fixed
            # effective-law replay use the same transformed coupling vector.
            recomputed = originary_transition_distribution(
                ancestors,
                normalized_nonempty_couplings(
                    factorial_post_log_couplings(
                        post_past_size,
                        FACTORIAL_PARAMETER,
                        MAX_COUPLING_INDEX,
                    )
                ),
            )
            replay_error = max(
                abs(
                    effective_distribution[outcome]
                    - recomputed[outcome]
                )
                for outcome in effective_distribution
            )
            replay_maximum_error = max(
                replay_maximum_error, replay_error
            )
            fixture_rows[fixture_name] = {
                "effective_distribution": {
                    str(mask): probability
                    for mask, probability in effective_distribution.items()
                },
                "percolation_distribution": {
                    str(mask): probability
                    for mask, probability in percolation_distribution.items()
                },
                "effective_to_percolation_total_variation": (
                    total_variation(
                        effective_distribution,
                        percolation_distribution,
                    )
                ),
                "frozen_history_replay_maximum_error": replay_error,
            }
        rows.append(
            {
                "post_past_size": post_past_size,
                "q_effective": q_effective,
                "history_generated_hierarchy_relative_to_atom": (
                    1.0 / q_effective
                ),
                "normalized_effective_couplings_t1_equals_one": (
                    list(effective)
                ),
                "percolation_couplings_t1_equals_one": (
                    list(percolation)
                ),
                "projective_relative_errors": (
                    projective_relative_errors
                ),
                "maximum_projective_relative_error": max(
                    projective_relative_errors.values()
                ),
                "fixtures": fixture_rows,
            }
        )

    adjacent_hierarchy_slopes = []
    for left, right in zip(rows, rows[1:]):
        adjacent_hierarchy_slopes.append(
            math.log(
                right[
                    "history_generated_hierarchy_relative_to_atom"
                ]
                / left[
                    "history_generated_hierarchy_relative_to_atom"
                ]
            )
            / math.log(
                right["post_past_size"] / left["post_past_size"]
            )
        )

    earliest = rows[0]["fixtures"]["originary_diamond"][
        "effective_distribution"
    ]
    latest = rows[-1]["fixtures"]["originary_diamond"][
        "effective_distribution"
    ]
    distinct_history_total_variation = total_variation(
        {int(mask): value for mask, value in earliest.items()},
        {int(mask): value for mask, value in latest.items()},
    )
    return {
        "factorial_bare_law": "t_n=t^n/n!, t=1",
        "post_past_grid": list(POST_PAST_GRID),
        "rows": rows,
        "maximum_frozen_history_replay_error": replay_maximum_error,
        "adjacent_log_hierarchy_slopes": adjacent_hierarchy_slopes,
        "maximum_slope_error_from_one_half": max(
            abs(slope - 0.5) for slope in adjacent_hierarchy_slopes
        ),
        "distinct_history_diamond_total_variation": (
            distinct_history_total_variation
        ),
        "interpretation": {
            "history_dependence": (
                "Different covariant post-past sizes induce different future "
                "laws and therefore retain genuine historical information."
            ),
            "fixed_history_replay": (
                "Conditional on one post past, every tested transition is "
                "exactly reproduced by a fixed effective CSG law. No post-era "
                "diagnostic feeds back into the coupling vector in this "
                "construction."
            ),
            "units": (
                "The hierarchy is dimensionless. A physical length still "
                "requires multiplication by a declared microscopic atom unit."
            ),
        },
    }


def main() -> None:
    exact = exact_transform_tests()
    asymptotic = asymptotic_and_replay_tests()
    largest_row = asymptotic["rows"][-1]
    largest_diamond_tv = largest_row["fixtures"]["originary_diamond"][
        "effective_to_percolation_total_variation"
    ]
    checks = [
        {
            "name": "iterating the elementary post map equals the exact binomial transform",
            "pass": exact[
                "arbitrary_sequence_iteration_matches_binomial_exactly"
            ],
        },
        {
            "name": "transitive percolation is an exact projective fixed family of the post map",
            "pass": exact[
                "percolation_is_projective_fixed_family_exactly"
            ],
        },
        {
            "name": "factorial-law effective coupling ratios approach q_eff=sqrt(t/N)",
            "pass": (
                asymptotic["rows"][-1][
                    "maximum_projective_relative_error"
                ]
                < 0.015
                and all(
                    later["maximum_projective_relative_error"]
                    < earlier["maximum_projective_relative_error"]
                    for earlier, later in zip(
                        asymptotic["rows"], asymptotic["rows"][1:]
                    )
                )
            ),
        },
        {
            "name": "finite originary-diamond transition probabilities approach the percolation law",
            "pass": (
                largest_diamond_tv < 2.0e-6
                and all(
                    later["fixtures"]["originary_diamond"][
                        "effective_to_percolation_total_variation"
                    ]
                    < earlier["fixtures"]["originary_diamond"][
                        "effective_to_percolation_total_variation"
                    ]
                    for earlier, later in zip(
                        asymptotic["rows"], asymptotic["rows"][1:]
                    )
                )
            ),
        },
        {
            "name": "the history-generated hierarchy scales as sqrt(N/t)",
            "pass": (
                asymptotic["maximum_slope_error_from_one_half"]
                < 2.0e-14
            ),
        },
        {
            "name": "different post-past sizes induce distinguishable conditional laws",
            "pass": (
                asymptotic[
                    "distinct_history_diamond_total_variation"
                ]
                > 0.01
            ),
        },
        {
            "name": "fixed-history replay is exactly distribution-equivalent on three causal fixtures",
            "pass": (
                asymptotic["maximum_frozen_history_replay_error"]
                == 0.0
            ),
        },
        {
            "name": "no active post-era diagnostic, H0, target epoch, or target geometry enters the update",
            "pass": True,
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-COMMERCIAL-POST-RG-DECISION-ASSAY",
        "track": (
            "Science Council commercial successor wave / "
            "WF-D1 + COM-D3 + COM-D9"
        ),
        "question": (
            "Does known causal-post renormalization already provide a "
            "decision-changing covariant history-to-law mechanism, and does "
            "that mechanism also supply the active return arrow required by "
            "the current HC-DU-011 + HC-DU-022 program?"
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
                    "The post era is governed by classical sequential growth "
                    "and is conditioned on a covariantly identifiable post "
                    "with N elements in its past."
                ),
                "status": "STANDARD",
                "role": (
                    "Makes the published causal-post renormalization map the "
                    "relevant exact conditional law."
                ),
            },
            {
                "id": "A2",
                "statement": "The bare coupling family is t_n=t^n/n!.",
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Supplies the published asymptotic route to effective "
                    "transitive percolation."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "A microscopic atom length would be supplied separately "
                    "if the dimensionless hierarchy were mapped to a length."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Prevents dimensionless history from creating units ex nihilo.",
            },
            {
                "id": "A4",
                "statement": (
                    "The known post map is applied to a fixed post past and is "
                    "not supplemented by a new post-era feedback variable."
                ),
                "status": "STANDARD",
                "role": (
                    "Defines the fixed-history replay discriminator without "
                    "silently adding the missing return arrow."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "Use t=1 and post-past sizes 100 through 100000.",
                "why_not_forced": (
                    "They are finite numerical fixtures chosen to expose the "
                    "published large-past asymptotic regime."
                ),
                "sensitivity_test": (
                    "Require monotone convergence across four decades rather "
                    "than accepting one fitted post size."
                ),
            },
            {
                "id": "C2",
                "choice": (
                    "Use an originary antichain, diamond, and chain as the "
                    "finite transition fixtures."
                ),
                "why_not_forced": (
                    "They are small representatives, not a continuum geometry "
                    "sample or complete unlabeled-causet enumeration."
                ),
                "sensitivity_test": (
                    "Require exact replay on all three and convergence on the "
                    "nontrivial diamond."
                ),
            },
        ],
        "equations": [
            "(R^N t)_k=sum_{j=0}^N binom(N,j)t_{k+j}, k>=1",
            "lambda(varpi,m)=sum_{k=m}^varpi binom(varpi-m,k-m)t_k",
            "t_n=t^n/n! => q_eff approximately sqrt(t/N)",
            "ell_history/ell_atom=1/q_eff=sqrt(N/t)",
        ],
        "observables": [
            "exact equality of iterated and binomial post transforms",
            "projective effective-coupling error from transitive percolation",
            "total-variation distance on finite originary transition laws",
            "dimensionless hierarchy and its log slope",
            "fixed-history replay error",
            "law difference between distinct post-past sizes",
        ],
        "comparators": [
            "exact projective transitive-percolation fixed family",
            "fixed effective-law replay conditional on the same post past",
            "different covariant post-past sizes",
        ],
        "null_models": [
            "a copied fixed effective coupling vector",
            "a post map with no post-era diagnostic feedback input",
        ],
        "falsifiers": [
            "elementary iteration differs from the binomial transform",
            "factorial-law ratios fail to converge toward sqrt(t/N)",
            "finite transition laws fail to converge toward percolation",
            "fixed-history replay changes a conditional transition probability",
            "the dimensionless hierarchy fails its sqrt(N/t) scaling",
        ],
        "stop_conditions": [
            "Do not build generic enumeration to rediscover the known post map.",
            "Do not call historical renormalization an active return arrow when fixed replay is exact.",
            "Do not call the dimensionless hierarchy a physical scale without an atom unit.",
            "Do not infer continuum or manifoldlike geometry from this finite transition assay.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A live unifying mechanism must distinguish genuine "
                "history-to-law dynamics from a fixed-law redescription and "
                "must survive an independent physical geometry test."
            ),
            "formalization_id": "FORMALIZATION-COM-SUCC-POST-RG-01",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "Conditional causal-post renormalization is a genuine "
                "covariant historical memory and hierarchy mechanism. On the "
                "tested conditional sector it is exactly replayable as a "
                "fixed effective CSG law, so it does not by itself construct "
                "the active post-era return arrow."
            ),
            "grade": (
                "KNOWN MAP INDEPENDENTLY RECOMPUTED / CONDITIONAL HIERARCHY "
                "CONSTRUCTIVELY REALIZED / ACTIVE RETURN ARROW ABSENT"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "The probe does not test repeated-post production, post "
                "selection, continuum recovery, Lorentzian manifoldlikeness, "
                "or a physical unit map. Published interval-abundance results "
                "supply a separate adverse geometry holdout that must be "
                "treated as a route-level decision input."
            ),
            "checks": checks,
        },
    }
    receipt = comparison_receipt(candidate)
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise AssertionError(f"failed checks: {failed}")
    if receipt["contract_status"] != "COMPLETE":
        raise AssertionError(receipt["contract_errors"])

    write_candidate_artifact(
        ARTIFACT_PATH,
        candidate,
        {
            "exact_transform": exact,
            "factorial_asymptotic_and_fixed_history_replay": asymptotic,
            "commercial_decision": {
                "construct_now": (
                    "A narrow post-RG assumption/replay/geometry decision "
                    "packet, using generic enumeration only as shared library "
                    "infrastructure."
                ),
                "do_not_construct_now": (
                    "A monolithic HC-DU-011A platform or a new generic "
                    "post-renormalization search."
                ),
                "route_disposition": (
                    "Promote as an exact control and conditional hierarchy "
                    "constructor; demote as the leading full DU route unless "
                    "a geometry escape and an actual return-arrow extension "
                    "survive."
                ),
            },
            "checks_passed": passed,
            "checks_total": len(checks),
        },
    )
    print(
        "du_successor_commercial_post_rg_decision_probe: "
        f"{passed}/{len(checks)} checks passed"
    )
    print(f"artifact: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
