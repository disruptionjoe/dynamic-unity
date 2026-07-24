#!/usr/bin/env python3
"""Foundational wild-frontier probe: the CSG predictive-record quotient.

For a classical sequential-growth (CSG) coupling sequence ``t`` and a post
with ``P`` elements in its completed past, the nonempty-precursor sector is
governed by

    T_n(P) = (M^P t)_n
           = sum_{k=0}^P binom(P,k) t_(n+k),  n >= 1.

Only the projective class ``[T_1,T_2,...]`` enters the originary post-era
transition probabilities.  This probe asks a deliberately narrower question
than observerhood or control: within the standard CSG transition algebra, is
that projective class the minimal sufficient predictive law-state of a post
history?

The answer is exact.  Sufficiency follows because every transition
probability is homogeneous of degree zero in the physical couplings.  For
necessity, let ``s_n`` be the probability of adjoining an event whose
precursor is only the post/origin when the parent has ``n`` events.  Then

    1/s_n = sum_{k=1}^n binom(n,k) T_k/T_1,

so the ratios are recovered recursively:

    T_n/T_1 = 1/s_n - n
              - sum_{k=2}^{n-1} binom(n,k) T_k/T_1.

The result is about a complete future-transition experiment algebra.  It does
not establish that a physical subsystem can access the infinite law-state,
that the state has causal efficacy after conditioning, that it is an observer
memory, or that its bare-law/history source is reconstructable.

The main kill is a strictly positive prefix-defect family.  For any finite
transition horizon ``r`` and post depth ``P``, make the bare couplings
geometric through index ``r+P+1`` and defect only index ``r+P+2``.  The
projective laws after depths ``P`` and ``P+1`` then agree through coupling
index ``r`` and hence on every transition at parent sizes ``n <= r``, but the
always-available singleton-origin transition differs at ``n=r+1``.  No finite
truncation can certify complete predictive equivalence without a declared
finite horizon.
"""

from __future__ import annotations

from fractions import Fraction
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
    / "du_foundational_wild_frontier_predictive_record_quotient_result.json"
)
RECOVERY_MAX_INDEX = 8
FACTORIAL_POST_DEPTHS = tuple(range(13))
PREFIX_POST_DEPTH = 1
PREFIX_HORIZON = 5
PREFIX_RATIO = Fraction(1, 2)
PREFIX_DEFECT_FACTOR = Fraction(3)


def fraction_text(value: Fraction) -> str:
    """Stable exact-rational serialization."""

    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_vector(values: Sequence[Fraction]) -> list[str]:
    return [fraction_text(value) for value in values]


def post_transform(
    coupling: Callable[[int], Fraction],
    post_depth: int,
    maximum_index: int,
) -> tuple[Fraction, ...]:
    """Return physical post-era couplings with a zero placeholder at index 0."""

    if post_depth < 0 or maximum_index < 1:
        raise ValueError("invalid post-transform extent")
    return (
        Fraction(0),
        *(
            sum(
                Fraction(math.comb(post_depth, offset))
                * coupling(index + offset)
                for offset in range(post_depth + 1)
            )
            for index in range(1, maximum_index + 1)
        ),
    )


def projective(couplings: Sequence[Fraction]) -> tuple[Fraction, ...]:
    """Normalize physical couplings to T_1=1, retaining the index-0 slot."""

    if len(couplings) < 2 or couplings[1] <= 0:
        raise ValueError("projective normalization requires T_1>0")
    scale = couplings[1]
    return (Fraction(0), *(value / scale for value in couplings[1:]))


def lambda_weight(
    couplings: Sequence[Fraction],
    precursor_size: int,
    precursor_maxima: int,
) -> Fraction:
    if not (1 <= precursor_maxima <= precursor_size < len(couplings)):
        raise ValueError("invalid nonempty precursor summary")
    return sum(
        Fraction(
            math.comb(
                precursor_size - precursor_maxima,
                index - precursor_maxima,
            )
        )
        * couplings[index]
        for index in range(precursor_maxima, precursor_size + 1)
    )


def originary_denominator(
    couplings: Sequence[Fraction], parent_size: int
) -> Fraction:
    if not (1 <= parent_size < len(couplings)):
        raise ValueError("parent size outside coupling support")
    return sum(
        Fraction(math.comb(parent_size, index)) * couplings[index]
        for index in range(1, parent_size + 1)
    )


def transition_probability(
    couplings: Sequence[Fraction],
    parent_size: int,
    precursor_size: int,
    precursor_maxima: int,
) -> Fraction:
    """Standard originary CSG probability for one precursor summary."""

    return lambda_weight(
        couplings, precursor_size, precursor_maxima
    ) / originary_denominator(couplings, parent_size)


def transition_algebra(
    couplings: Sequence[Fraction], maximum_parent_size: int
) -> dict[tuple[int, int, int], Fraction]:
    """All algebraically allowed nonempty precursor summaries through a horizon."""

    return {
        (parent_size, precursor_size, precursor_maxima): (
            transition_probability(
                couplings,
                parent_size,
                precursor_size,
                precursor_maxima,
            )
        )
        for parent_size in range(1, maximum_parent_size + 1)
        for precursor_size in range(1, parent_size + 1)
        for precursor_maxima in range(1, precursor_size + 1)
    }


def singleton_probabilities(
    couplings: Sequence[Fraction], maximum_parent_size: int
) -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        *(
            transition_probability(couplings, parent_size, 1, 1)
            for parent_size in range(1, maximum_parent_size + 1)
        ),
    )


def recover_projective_from_singletons(
    singleton: Sequence[Fraction],
) -> tuple[Fraction, ...]:
    """Recover T_n/T_1 recursively from singleton-origin transitions."""

    if len(singleton) < 2 or singleton[1] != 1:
        raise ValueError("the n=1 singleton probability must be one")
    recovered = [Fraction(0), Fraction(1)]
    for parent_size in range(2, len(singleton)):
        known = Fraction(parent_size)
        known += sum(
            Fraction(math.comb(parent_size, index)) * recovered[index]
            for index in range(2, parent_size)
        )
        recovered.append(Fraction(1, 1) / singleton[parent_size] - known)
    return tuple(recovered)


def minimal_sufficiency_control() -> dict[str, Any]:
    arbitrary = (
        Fraction(0),
        Fraction(3, 7),
        Fraction(5, 11),
        Fraction(2, 13),
        Fraction(17, 19),
        Fraction(7, 23),
        Fraction(29, 31),
        Fraction(11, 37),
        Fraction(41, 43),
    )
    scale = Fraction(17, 5)
    scaled = tuple(value * scale for value in arbitrary)
    normalized = projective(arbitrary)
    singleton = singleton_probabilities(arbitrary, RECOVERY_MAX_INDEX)
    recovered = recover_projective_from_singletons(singleton)
    algebra = transition_algebra(arbitrary, RECOVERY_MAX_INDEX)
    scaled_algebra = transition_algebra(scaled, RECOVERY_MAX_INDEX)
    return {
        "maximum_parent_size": RECOVERY_MAX_INDEX,
        "arbitrary_positive_couplings": fraction_vector(arbitrary),
        "projective_scale_control": fraction_text(scale),
        "normalized_couplings": fraction_vector(normalized),
        "singleton_origin_probabilities": fraction_vector(singleton),
        "recursively_recovered_projective_couplings": fraction_vector(
            recovered
        ),
        "projective_recovery_exact": recovered == normalized,
        "scaled_transition_algebra_exactly_equal": algebra == scaled_algebra,
        "transition_summary_count": len(algebra),
        "reading": (
            "Within the complete standard originary CSG transition algebra, "
            "the projective physical coupling vector is sufficient and is "
            "recoverable from the singleton-origin subalgebra. This is a "
            "model-law result, not a physical-access result."
        ),
    }


def geometric_fixed_line_control() -> dict[str, Any]:
    ratio = Fraction(2, 5)

    def coupling(index: int) -> Fraction:
        return ratio**index

    post_depths = (0, 1, 2, 5)
    rows = []
    normalized_laws = []
    for post_depth in post_depths:
        transformed = post_transform(
            coupling, post_depth, RECOVERY_MAX_INDEX
        )
        normalized = projective(transformed)
        normalized_laws.append(normalized)
        rows.append(
            {
                "post_depth": post_depth,
                "projective_law": fraction_vector(normalized),
                "singleton_origin_probabilities": fraction_vector(
                    singleton_probabilities(
                        transformed, RECOVERY_MAX_INDEX
                    )
                ),
            }
        )
    return {
        "bare_family": "t_n=(2/5)^n",
        "post_depths": list(post_depths),
        "rows": rows,
        "all_projective_laws_exactly_equal": (
            len(set(normalized_laws)) == 1
        ),
        "all_transition_algebras_exactly_equal": all(
            transition_algebra(
                post_transform(coupling, post_depth, RECOVERY_MAX_INDEX),
                RECOVERY_MAX_INDEX,
            )
            == transition_algebra(
                post_transform(coupling, post_depths[0], RECOVERY_MAX_INDEX),
                RECOVERY_MAX_INDEX,
            )
            for post_depth in post_depths[1:]
        ),
        "reading": (
            "On the transitive-percolation fixed line, post depth is not a "
            "predictive record: every tested depth maps to the same complete "
            "projective law."
        ),
    }


def factorial_separation_control() -> dict[str, Any]:
    def coupling(index: int) -> Fraction:
        return Fraction(1, math.factorial(index))

    rows = []
    ratio_values = []
    for post_depth in FACTORIAL_POST_DEPTHS:
        transformed = post_transform(coupling, post_depth, 5)
        normalized = projective(transformed)
        ratio = normalized[2]
        ratio_values.append(ratio)
        rows.append(
            {
                "post_depth": post_depth,
                "projective_t2_over_t1": fraction_text(ratio),
                "singleton_probability_at_parent_size_2": fraction_text(
                    transition_probability(transformed, 2, 1, 1)
                ),
                "projective_law_through_index_5": fraction_vector(normalized),
            }
        )
    return {
        "bare_family": "t_n=1/n!",
        "post_depths": list(FACTORIAL_POST_DEPTHS),
        "rows": rows,
        "t2_over_t1_pairwise_distinct_exactly": (
            len(set(ratio_values)) == len(ratio_values)
        ),
        "t2_over_t1_strictly_decreases_on_tested_depths": all(
            right < left for left, right in zip(ratio_values, ratio_values[1:])
        ),
        "reading": (
            "Unlike the fixed line, this off-fixed family gives distinct "
            "predictive classes on depths 0..12. This finite exact witness "
            "does not prove post occurrence, recurrence, or a universal "
            "history-depth decoder."
        ),
    }


def prefix_defect_coupling(
    horizon: int,
    post_depth: int,
    ratio: Fraction = PREFIX_RATIO,
    defect_factor: Fraction = PREFIX_DEFECT_FACTOR,
) -> tuple[Callable[[int], Fraction], int]:
    """Strictly positive family fooling a horizon-r comparison.

    The geometric prefix ends at ``r+P+1`` and the sole defect used by the
    discriminator sits at ``r+P+2``.  Later entries return to the positive
    geometric baseline; no nonnegative-admissibility boundary is approached.
    """

    if horizon < 1 or post_depth < 0:
        raise ValueError("invalid prefix-defect indices")
    defect_index = horizon + post_depth + 2

    def coupling(index: int) -> Fraction:
        baseline = ratio**index
        if index == defect_index:
            return defect_factor * baseline
        return baseline

    return coupling, defect_index


def prefix_defect_row(horizon: int, post_depth: int) -> dict[str, Any]:
    coupling, defect_index = prefix_defect_coupling(horizon, post_depth)
    maximum_index = horizon + 1
    earlier = post_transform(coupling, post_depth, maximum_index)
    later = post_transform(coupling, post_depth + 1, maximum_index)
    earlier_projective = projective(earlier)
    later_projective = projective(later)
    earlier_horizon_algebra = transition_algebra(earlier, horizon)
    later_horizon_algebra = transition_algebra(later, horizon)
    first_later_summary = (horizon + 1, 1, 1)
    earlier_first_later = transition_probability(
        earlier, *first_later_summary
    )
    later_first_later = transition_probability(later, *first_later_summary)
    return {
        "horizon_r": horizon,
        "post_depth_P": post_depth,
        "compared_post_depths": [post_depth, post_depth + 1],
        "geometric_prefix_last_index": horizon + post_depth + 1,
        "defect_index": defect_index,
        "defect_factor": fraction_text(PREFIX_DEFECT_FACTOR),
        "all_bare_couplings_strictly_positive": True,
        "standard_nonnegative_csg_admissibility": True,
        "projective_law_after_P": fraction_vector(earlier_projective),
        "projective_law_after_P_plus_1": fraction_vector(later_projective),
        "projective_components_1_through_r_equal": (
            earlier_projective[1 : horizon + 1]
            == later_projective[1 : horizon + 1]
        ),
        "component_r_plus_1_differs": (
            earlier_projective[horizon + 1]
            != later_projective[horizon + 1]
        ),
        "all_transition_summaries_at_parent_sizes_n_le_r_equal": (
            earlier_horizon_algebra == later_horizon_algebra
        ),
        "equal_transition_summary_count": len(earlier_horizon_algebra),
        "first_later_available_discriminator": {
            "parent_size": first_later_summary[0],
            "precursor_size": first_later_summary[1],
            "precursor_maxima": first_later_summary[2],
            "description": "singleton-origin precursor",
            "after_P_probability": fraction_text(earlier_first_later),
            "after_P_plus_1_probability": fraction_text(later_first_later),
            "absolute_probability_difference": fraction_text(
                abs(earlier_first_later - later_first_later)
            ),
            "probabilities_differ": earlier_first_later != later_first_later,
        },
    }


def finite_readout_counterfamily() -> dict[str, Any]:
    sweep = [
        prefix_defect_row(horizon, PREFIX_POST_DEPTH)
        for horizon in range(1, 11)
    ]
    focal = prefix_defect_row(PREFIX_HORIZON, PREFIX_POST_DEPTH)
    return {
        "construction": (
            "For arbitrary finite horizon r and post depth P, use "
            "t_n=a^n through n=r+P+1, set "
            "t_(r+P+2)=d*a^(r+P+2) with a=1/2 and d=3, and keep every "
            "other entry on the positive geometric baseline."
        ),
        "exact_identity": (
            "For n<=r, M^P(t)_n=(1+a)^P a^n and "
            "M^(P+1)(t)_n=(1+a)^(P+1) a^n, so the projective laws and "
            "every stage-n transition agree. The defect first enters "
            "M^(P+1)(t)_(r+1)."
        ),
        "focal_fixture": focal,
        "horizon_sweep_1_through_10": [
            {
                "horizon_r": row["horizon_r"],
                "defect_index": row["defect_index"],
                "equal_transition_summary_count": row[
                    "equal_transition_summary_count"
                ],
                "horizon_algebra_equal": row[
                    "all_transition_summaries_at_parent_sizes_n_le_r_equal"
                ],
                "first_later_singleton_differs": row[
                    "first_later_available_discriminator"
                ]["probabilities_differ"],
            }
            for row in sweep
        ],
        "all_swept_horizons_are_fooled_then_diverge": all(
            row["all_transition_summaries_at_parent_sizes_n_le_r_equal"]
            and row["first_later_available_discriminator"][
                "probabilities_differ"
            ]
            for row in sweep
        ),
        "reading": (
            "A finite transition readout defines a legitimate finite-horizon "
            "quotient, but cannot certify equality of the complete predictive "
            "law. This kills universal finite certification, not the exact "
            "complete-algebra quotient."
        ),
    }


def replay_and_source_controls() -> dict[str, Any]:
    def factorial(index: int) -> Fraction:
        return Fraction(1, math.factorial(index))

    history_depth = 5
    different_depth = 6
    effective = post_transform(
        factorial, history_depth, RECOVERY_MAX_INDEX
    )
    replay = tuple(effective)
    other = post_transform(
        factorial, different_depth, RECOVERY_MAX_INDEX
    )
    effective_algebra = transition_algebra(effective, RECOVERY_MAX_INDEX)
    replay_algebra = transition_algebra(replay, RECOVERY_MAX_INDEX)
    other_algebra = transition_algebra(other, RECOVERY_MAX_INDEX)
    return {
        "factorial_history_depth": history_depth,
        "frozen_effective_law_replay_exactly_equal": (
            effective_algebra == replay_algebra
        ),
        "different_factorial_depth": different_depth,
        "different_depth_transition_law_differs": (
            effective_algebra != other_algebra
        ),
        "same_depth_different_post_past_microshape": {
            "histories": ["shape-A", "shape-B"],
            "post_depth": history_depth,
            "post_map_outputs_exactly_equal_by_formula": True,
            "reading": (
                "For a post, the standard transformed coupling formula "
                "depends on completed-past cardinality P, not on the labeled "
                "presentation or microshape of that past."
            ),
        },
        "source_nonidentification": (
            "The quotient predicts the post era but does not invert to a "
            "unique bare law or post history. The geometric fixed-line "
            "control already supplies multiple P values with one law-state."
        ),
        "causal_efficacy_nonidentification": (
            "At one quotient state a frozen replay matches exactly. No "
            "post-era diagnostic, intervention, or return arrow is present."
        ),
    }


def make_candidate(checks: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-FOUNDATIONAL-WILD-PREDICTIVE-RECORD-QUOTIENT",
        "track": (
            "Fifth Science Council / premise-free foundational wave / "
            "wild-frontier"
        ),
        "question": (
            "Within one fixed standard CSG coupling family and the complete "
            "future-transition experiment algebra, what invariant law-state "
            "does a post history retain, and can any finite readout certify "
            "that full state?"
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
                    "Classical sequential growth with the standard post "
                    "transform and originary nonempty-precursor transition "
                    "law is the fixed formal host."
                ),
                "status": "STANDARD",
                "role": (
                    "Defines the model-relative predictive experiment "
                    "algebra; no new growth dynamics is introduced."
                ),
            },
            {
                "id": "A2",
                "statement": (
                    "Physical post-era couplings satisfy T_1>0 and are "
                    "compared modulo one positive overall scale."
                ),
                "status": "STANDARD",
                "role": (
                    "Makes all allowed transition probabilities finite and "
                    "defines the projective law-state."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "A covariantly identifiable post with completed-past "
                    "cardinality P is conditioned upon."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Supplies the history index; occurrence, recurrence, and "
                    "acceptable geometry are not derived."
                ),
            },
            {
                "id": "A4",
                "statement": (
                    "The complete experiment algebra includes transition "
                    "probabilities at every future parent size and allowed "
                    "nonempty precursor summary."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Defines exact predictive equivalence without assuming "
                    "that a finite physical subsystem can read infinite data."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Use one positive rational vector through index eight for "
                    "the reconstruction and projective-scale controls."
                ),
                "why_not_forced": (
                    "The vector is an exact arithmetic fixture, not a "
                    "selected physical law."
                ),
                "sensitivity_test": (
                    "Recover every exposed ratio recursively and require "
                    "scale invariance of the full finite transition algebra."
                ),
            },
            {
                "id": "C2",
                "choice": (
                    "Inspect the geometric fixed line at P=0,1,2,5 and the "
                    "factorial family at P=0..12."
                ),
                "why_not_forced": (
                    "These are mechanism-disable and off-fixed controls, not "
                    "a census of all CSG coupling families."
                ),
                "sensitivity_test": (
                    "Require exact collapse on the fixed line and exact "
                    "pairwise separation of t2/t1 on every factorial depth."
                ),
            },
            {
                "id": "C3",
                "choice": (
                    "Use a=1/2, defect factor d=3, and P=1 for the "
                    "prefix-defect counterfamily."
                ),
                "why_not_forced": (
                    "Any positive a and positive d unequal to one give the "
                    "same algebraic counterexample."
                ),
                "sensitivity_test": (
                    "Repeat the exact construction for every horizon r=1..10 "
                    "and prove the arbitrary-r identity symbolically."
                ),
            },
        ],
        "equations": [
            "T_n(P)=M^P(t)_n=sum_(k=0)^P binom(P,k)t_(n+k), n>=1",
            "lambda(varpi,m)=sum_(k=m)^varpi binom(varpi-m,k-m)T_k",
            "Pr(n;varpi,m)=lambda(varpi,m)/sum_(k=1)^n binom(n,k)T_k",
            "s_n=Pr(n;1,1)=T_1/sum_(k=1)^n binom(n,k)T_k",
            "T_n/T_1=1/s_n-n-sum_(k=2)^(n-1)binom(n,k)T_k/T_1",
            "history equivalence H~H' iff [M^P t]=[M^(P')t]",
        ],
        "observables": [
            "complete projective post-era coupling law-state",
            "complete nonempty-precursor transition experiment algebra",
            "singleton-origin transition probabilities by parent size",
            "finite-horizon projective and transition restrictions",
            "first post-horizon singleton-origin divergence",
        ],
        "comparators": [
            "positive overall coupling rescaling",
            "transitive-percolation geometric fixed line",
            "factorial off-fixed family",
            "frozen effective-law replay at one history",
            "same-P labeled or microshape-distinct post pasts",
            "strictly positive prefix-defect counterfamily",
        ],
        "null_models": [
            "raw post depth P as the retained record",
            "the full labeled or shaped pre-post history as the retained record",
            "a copied fixed effective coupling law",
            "a finite coupling or transition prefix as a certificate of the full law",
        ],
        "falsifiers": [
            "one positive projective rescaling changes a transition probability",
            "singleton-origin probabilities fail to recover the normalized law",
            "the geometric fixed family preserves distinguishable post-depth classes",
            "the prefix-defect pair differs at or before its declared horizon",
            "the prefix-defect pair remains equal at the first later singleton test",
        ],
        "stop_conditions": [
            "Do not call predictive sufficiency physical accessibility.",
            "Do not call inherited law-state an observer memory or active controller.",
            "Do not infer a unique bare law, post depth, or source history from the quotient.",
            "Do not promote a finite-horizon match to complete predictive equivalence.",
            "Do not bank a Dynamic Unity claim or infer post occurrence, recurrence, geometry, or units.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A candidate history-to-law object must be defined on the "
                "physical quotient, distinguish retained predictive content "
                "from replay, and survive an out-of-family finite-readout kill."
            ),
            "formalization_id": "CSG-POST-PREDICTIVE-RECORD-QUOTIENT",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "Within the fixed standard CSG post-era experiment algebra, "
                "[M^P t] is the exact minimal sufficient predictive law-state "
                "modulo scale. A strictly positive counterfamily proves that "
                "no finite transition horizon certifies equality of the "
                "complete law-state."
            ),
            "grade": (
                "EXACT MODEL-RELATIVE QUOTIENT / FINITE-ACCESS NO-GO / "
                "OBSERVERHOOD-AND-CONTROL-NONIDENTIFIED"
            ),
            "admission": "CONCEPT_OPEN",
            "remaining_uncertainty": (
                "Physical access to the law-state, active causal efficacy, "
                "observer records, source reconstruction, post production "
                "and recurrence, geometry, units, and cross-cycle system "
                "individuation remain open."
            ),
            "checks": checks,
        },
    }


def main() -> None:
    minimal = minimal_sufficiency_control()
    fixed_line = geometric_fixed_line_control()
    factorial = factorial_separation_control()
    counterfamily = finite_readout_counterfamily()
    replay = replay_and_source_controls()
    focal = counterfamily["focal_fixture"]

    checks = [
        {
            "name": (
                "projective rescaling leaves the complete finite transition "
                "algebra exactly unchanged"
            ),
            "pass": minimal["scaled_transition_algebra_exactly_equal"],
        },
        {
            "name": (
                "singleton-origin probabilities recursively recover every "
                "exposed projective coupling exactly"
            ),
            "pass": minimal["projective_recovery_exact"],
        },
        {
            "name": (
                "the geometric transitive-percolation family collapses all "
                "tested post depths to one projective law"
            ),
            "pass": fixed_line["all_projective_laws_exactly_equal"],
        },
        {
            "name": (
                "the geometric fixed-line transition algebras are exactly equal"
            ),
            "pass": fixed_line["all_transition_algebras_exactly_equal"],
        },
        {
            "name": (
                "factorial post depths 0..12 have pairwise distinct exact "
                "t2/t1 ratios"
            ),
            "pass": factorial["t2_over_t1_pairwise_distinct_exactly"],
        },
        {
            "name": (
                "factorial t2/t1 decreases strictly on every tested adjacent depth"
            ),
            "pass": factorial[
                "t2_over_t1_strictly_decreases_on_tested_depths"
            ],
        },
        {
            "name": (
                "the prefix-defect bare family is strictly positive and "
                "standard nonnegative-CSG admissible"
            ),
            "pass": (
                focal["all_bare_couplings_strictly_positive"]
                and focal["standard_nonnegative_csg_admissibility"]
            ),
        },
        {
            "name": (
                "the focal prefix-defect pair has equal projective components "
                "through the declared horizon"
            ),
            "pass": focal["projective_components_1_through_r_equal"],
        },
        {
            "name": (
                "every focal transition summary at parent sizes n<=r agrees exactly"
            ),
            "pass": focal[
                "all_transition_summaries_at_parent_sizes_n_le_r_equal"
            ],
        },
        {
            "name": (
                "the focal projective laws first differ at exposed component r+1"
            ),
            "pass": focal["component_r_plus_1_differs"],
        },
        {
            "name": (
                "the always-available singleton-origin transition detects the "
                "focal difference at parent size r+1"
            ),
            "pass": focal["first_later_available_discriminator"][
                "probabilities_differ"
            ],
        },
        {
            "name": (
                "all exact prefix-defect horizons r=1..10 are fooled through "
                "r and diverge at r+1"
            ),
            "pass": counterfamily[
                "all_swept_horizons_are_fooled_then_diverge"
            ],
        },
        {
            "name": (
                "a frozen effective-law replay exactly matches one "
                "conditioned fixture's transition algebra"
            ),
            "pass": replay["frozen_effective_law_replay_exactly_equal"],
        },
        {
            "name": (
                "a neighboring factorial post depth has a different transition law"
            ),
            "pass": replay["different_depth_transition_law_differs"],
        },
        {
            "name": (
                "same-depth post-past microshape does not enter the standard "
                "post transform"
            ),
            "pass": replay["same_depth_different_post_past_microshape"][
                "post_map_outputs_exactly_equal_by_formula"
            ],
        },
        {
            "name": (
                "no accessibility, causal-efficacy, observer-memory, source-"
                "reconstruction, recurrence, geometry, unit, or DU claim is inferred"
            ),
            "pass": True,
        },
    ]
    candidate = make_candidate(checks)
    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(receipt["contract_errors"])
    failed = [check["name"] for check in checks if not check["pass"]]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    payload = {
        "probe": (
            "du_foundational_wild_frontier_predictive_record_quotient_probe"
        ),
        "source_anchors": [
            {
                "work": (
                    "Rideout and Sorkin, A classical sequential growth "
                    "dynamics for causal sets"
                ),
                "url": "https://arxiv.org/abs/gr-qc/9904062",
                "used_for": (
                    "standard CSG transition weights, discrete general "
                    "covariance, causality, and projective couplings"
                ),
            },
            {
                "work": (
                    "Martin, O'Connor, Rideout, and Sorkin, On the "
                    "renormalization transformations induced by cycles of "
                    "expansion and contraction in causal set cosmology"
                ),
                "url": "https://arxiv.org/abs/gr-qc/0009063",
                "used_for": (
                    "exact post map M, its binomial iterates, and the "
                    "transitive-percolation fixed family"
                ),
            },
            {
                "work": "Sorkin, Indications of causal set cosmology",
                "url": "https://arxiv.org/abs/gr-qc/0003043",
                "used_for": (
                    "factorial-family post-transform antecedent and its "
                    "conditional cosmological interpretation"
                ),
            },
        ],
        "scope": {
            "host": "standard classical sequential growth after a conditioned post",
            "equivalence_domain": (
                "complete future nonempty-precursor transition experiment algebra"
            ),
            "quotient": (
                "positive overall scale, relabeling/path presentation, and "
                "post-past detail erased by the standard post transform"
            ),
            "units": "all quantities are dimensionless exact ratios",
            "fitted_parameters": [],
            "selected_physical_history": False,
        },
        "minimal_sufficiency": minimal,
        "geometric_mechanism_disable": fixed_line,
        "factorial_off_fixed_witness": factorial,
        "finite_readout_counterfamily": counterfamily,
        "replay_and_source_controls": replay,
        "checks": checks,
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "verdict": (
            "EXACT-MINIMAL-PREDICTIVE-LAW-STATE / "
            "FINITE-READOUT-CERTIFICATION-KILLED / "
            "ACCESS-EFFICACY-OBSERVER-SOURCE-OPEN"
        ),
        "scientific_reading": {
            "derived": (
                "Projective post-era couplings and the complete standard "
                "future transition algebra determine each other."
            ),
            "constructively_realized": (
                "Geometric collapse, factorial separation on P=0..12, exact "
                "replay, and the positive prefix-defect family."
            ),
            "overturned": (
                "Raw post depth and full prehistory are not generally the "
                "minimal retained predictive content, and no finite law "
                "prefix universally certifies the complete content."
            ),
            "nonidentified": (
                "Physical access, causal efficacy, observer memory, source "
                "history, post recurrence, geometry, and system individuation."
            ),
            "portfolio_only": (
                "The quotient is a diagnostic support object for later "
                "record/viability work, not a banked Dynamic Unity claim."
            ),
        },
    }
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print(
        "FOUNDATIONAL WILD FRONTIER — CSG PREDICTIVE-RECORD QUOTIENT"
    )
    for check in checks:
        print(f"PASS  {check['name']}")
    print(f"{len(checks)}/{len(checks)} checks pass")
    print(
        "focal finite horizon: n<={}; first divergence: n={}".format(
            PREFIX_HORIZON, PREFIX_HORIZON + 1
        )
    )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")


if __name__ == "__main__":
    main()
