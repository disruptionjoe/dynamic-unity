#!/usr/bin/env python3
"""Exact regression controls for HC-DU-105.

The scientific result is analytic. This probe preserves:

1. Boolean Möbius isolation of a four-source joint interaction from all
   lower-order source-subset responses;
2. necessity of every Boolean source context in that frozen query model;
3. the sharp 2^k worst-case context-error amplification;
4. linear finite-amplitude contamination from one fifth-order term; and
5. same-joint-provenance/different-site nonidentification under one aggregate
   readout, repaired by a full-rank two-readout packet.

Passing establishes no physical nonlinear field, selected source channels,
repeatable completion, interaction occurrence, localized event, formed
record, finite QFT instrument, conformal reconstruction, new physics,
prediction, or evidence grade.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_nonlinear_interaction_provenance_localization_result.json"
)

SourceSet = frozenset[int]


def power_set(source_count: int) -> tuple[SourceSet, ...]:
    sources = tuple(range(source_count))
    return tuple(
        frozenset(subset)
        for size in range(source_count + 1)
        for subset in combinations(sources, size)
    )


def multiaffine_boolean_value(
    coefficients: dict[SourceSet, Fraction],
    active: SourceSet,
) -> Fraction:
    return sum(
        coefficient
        for source_set, coefficient in coefficients.items()
        if source_set <= active
    )


def mobius_top(values: dict[SourceSet, Fraction], source_count: int) -> Fraction:
    return sum(
        (-1) ** (source_count - len(active)) * value
        for active, value in values.items()
    )


def analytic_interaction_estimate(
    joint_coefficient: Fraction,
    fifth_order_coefficient: Fraction,
    amplitude: Fraction,
    source_count: int,
) -> Fraction:
    """Exact divided difference for c*prod(e_i)+d*prod(e_i)*sum(e_i)."""

    contexts = power_set(source_count)
    values: dict[SourceSet, Fraction] = {}
    for active in contexts:
        if len(active) < source_count:
            values[active] = Fraction(0)
            continue
        product = amplitude**source_count
        values[active] = (
            joint_coefficient * product
            + fifth_order_coefficient
            * product
            * source_count
            * amplitude
        )
    return mobius_top(values, source_count) / amplitude**source_count


def matrix_vector(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        sum(entry * value for entry, value in zip(row, vector, strict=True))
        for row in matrix
    )


def main() -> None:
    source_count = 4
    contexts = power_set(source_count)
    full_set = frozenset(range(source_count))

    coefficients = {
        active: Fraction((len(active) + 1) * (sum(active) + 2), 3)
        for active in contexts
    }
    coefficients[full_set] = Fraction(17, 5)
    values = {
        active: multiaffine_boolean_value(coefficients, active)
        for active in contexts
    }
    recovered_joint = mobius_top(values, source_count)
    assert recovered_joint == coefficients[full_set]
    assert len(contexts) == 2**source_count == 16

    # If any Boolean vertex is omitted, the zero response and the Boolean
    # delta at that vertex agree on every observed context. The delta's top
    # Möbius coefficient is nonzero, so the pure joint term is not identified.
    omitted_context_failures = 0
    for omitted in contexts:
        delta_values = {
            active: Fraction(int(active == omitted))
            for active in contexts
        }
        top_coefficient = mobius_top(delta_values, source_count)
        assert top_coefficient in {Fraction(1), Fraction(-1)}
        observed = {
            active: value
            for active, value in delta_values.items()
            if active != omitted
        }
        assert all(value == 0 for value in observed.values())
        omitted_context_failures += 1
    assert omitted_context_failures == 16

    epsilon = Fraction(1, 1000)
    adversarial_errors = {
        active: Fraction((-1) ** (source_count - len(active))) * epsilon
        for active in contexts
    }
    amplified_error = abs(mobius_top(adversarial_errors, source_count))
    assert amplified_error == 2**source_count * epsilon

    joint_coefficient = Fraction(7, 3)
    fifth_order_coefficient = Fraction(5, 2)
    coarse_amplitude = Fraction(1, 10)
    fine_amplitude = Fraction(1, 20)
    coarse_estimate = analytic_interaction_estimate(
        joint_coefficient,
        fifth_order_coefficient,
        coarse_amplitude,
        source_count,
    )
    fine_estimate = analytic_interaction_estimate(
        joint_coefficient,
        fifth_order_coefficient,
        fine_amplitude,
        source_count,
    )
    coarse_tail = coarse_estimate - joint_coefficient
    fine_tail = fine_estimate - joint_coefficient
    assert coarse_tail == source_count * fifth_order_coefficient * coarse_amplitude
    assert fine_tail == source_count * fifth_order_coefficient * fine_amplitude
    assert fine_tail * 2 == coarse_tail

    site_p = (Fraction(1), Fraction(0))
    site_q = (Fraction(0), Fraction(1))
    aggregate_readout = ((Fraction(1), Fraction(1)),)
    assert matrix_vector(aggregate_readout, site_p) == matrix_vector(
        aggregate_readout, site_q
    )

    separating_readouts = (
        (Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(-1)),
    )
    response_p = matrix_vector(separating_readouts, site_p)
    response_q = matrix_vector(separating_readouts, site_q)
    assert response_p != response_q
    assert response_p == (Fraction(1), Fraction(1))
    assert response_q == (Fraction(1), Fraction(-1))

    result = {
        "claim_id": "HC-DU-105",
        "status": "PASS",
        "controls": {
            "source_count": source_count,
            "boolean_context_count": len(contexts),
            "mobius_joint_coefficient": str(recovered_joint),
            "strict_subset_query_failures": omitted_context_failures,
            "worst_case_error_amplification": str(amplified_error / epsilon),
            "analytic_tail_halves_with_amplitude": True,
            "aggregate_readout_same_record_different_site": True,
            "full_rank_two_readout_repair": True,
        },
        "boundary": (
            "Regression only: no physical nonlinear field, selected source "
            "interface, repeatability, formed interaction record, event "
            "localization, finite QFT acquisition, geometry reconstruction, "
            "new physics, or prediction."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-105 controls: four-source Möbius provenance, context "
        "lower bound, noise/tail tradeoff, and localization rank gate"
    )


if __name__ == "__main__":
    main()
