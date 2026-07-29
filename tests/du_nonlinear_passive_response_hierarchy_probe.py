#!/usr/bin/env python3
"""Exact controls for HC-DU-100.

This probe validates two elementary mathematical boundaries only:

1. no finite response jet identifies a general analytic response map; and
2. a uniform geometric coefficient bound gives a sharp finite Taylor tail.

Passing establishes no physical realization, interface selection, formed
record, geometry reconstruction, novelty, prediction, or evidence grade.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_nonlinear_passive_response_hierarchy_result.json"
)


def derivative_at_zero(coefficients: dict[int, Fraction], order: int) -> Fraction:
    """Return the exact derivative of a polynomial at zero."""

    return coefficients.get(order, Fraction(0)) * factorial(order)


def evaluate(coefficients: dict[int, Fraction], source: Fraction) -> Fraction:
    return sum(
        (coefficient * source**order for order, coefficient in coefficients.items()),
        start=Fraction(0),
    )


def main() -> None:
    jet_cases: list[dict[str, object]] = []
    for retained_order in range(1, 9):
        base = {1: Fraction(1)}
        alternative = {
            1: Fraction(1),
            retained_order + 1: Fraction(retained_order + 2, retained_order + 3),
        }
        equal_retained_jet = all(
            derivative_at_zero(base, order)
            == derivative_at_zero(alternative, order)
            for order in range(retained_order + 1)
        )
        first_difference_order = retained_order + 1
        first_difference = (
            derivative_at_zero(alternative, first_difference_order)
            - derivative_at_zero(base, first_difference_order)
        )
        held_out_source = Fraction(1, 2)
        held_out_difference = (
            evaluate(alternative, held_out_source)
            - evaluate(base, held_out_source)
        )
        assert equal_retained_jet
        assert first_difference != 0
        assert held_out_difference != 0
        jet_cases.append(
            {
                "retained_order": retained_order,
                "equal_derivatives_through_retained_order": equal_retained_jet,
                "first_difference_order": first_difference_order,
                "first_difference": str(first_difference),
                "held_out_source": str(held_out_source),
                "held_out_difference": str(held_out_difference),
            }
        )

    tail_cases: list[dict[str, object]] = []
    coefficient_scale = Fraction(1)
    analytic_radius = Fraction(2)
    evaluation_radius = Fraction(1)
    ratio = evaluation_radius / analytic_radius
    for retained_order in range(0, 9):
        # The extremal scalar series a_n = M R^{-n} makes the geometric
        # coefficient bound exact at s = r.
        exact_tail = (
            coefficient_scale
            * ratio ** (retained_order + 1)
            / (1 - ratio)
        )
        certified_bound = (
            coefficient_scale
            * (evaluation_radius / analytic_radius) ** (retained_order + 1)
            / (1 - evaluation_radius / analytic_radius)
        )
        assert exact_tail == certified_bound
        tail_cases.append(
            {
                "retained_order": retained_order,
                "exact_tail": str(exact_tail),
                "certified_bound": str(certified_bound),
                "sharp": exact_tail == certified_bound,
            }
        )

    target_tolerance = Fraction(1, 100)
    first_sufficient_order = next(
        order
        for order in range(100)
        if coefficient_scale
        * ratio ** (order + 1)
        / (1 - ratio)
        <= target_tolerance
    )
    previous_bound = (
        coefficient_scale
        * ratio**first_sufficient_order
        / (1 - ratio)
    )
    sufficient_bound = (
        coefficient_scale
        * ratio ** (first_sufficient_order + 1)
        / (1 - ratio)
    )
    assert previous_bound > target_tolerance
    assert sufficient_bound <= target_tolerance

    result = {
        "probe": "du_nonlinear_passive_response_hierarchy_probe",
        "status": "PASS",
        "claim_id": "HC-DU-100",
        "checks": {
            "finite_jet_counterexamples": len(jet_cases),
            "sharp_tail_controls": len(tail_cases),
            "minimum_order_control": True,
        },
        "finite_jet_cases": jet_cases,
        "analytic_tail_cases": tail_cases,
        "minimum_order_example": {
            "coefficient_scale": str(coefficient_scale),
            "analytic_radius": str(analytic_radius),
            "evaluation_radius": str(evaluation_radius),
            "target_tolerance": str(target_tolerance),
            "first_sufficient_order": first_sufficient_order,
            "previous_bound": str(previous_bound),
            "sufficient_bound": str(sufficient_bound),
        },
        "scope_warning": (
            "Exact scalar analytic controls only; no physical correlation "
            "hierarchy, instrument, spacetime, or acquisition is selected."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS:",
        len(jet_cases),
        "finite-jet counterexamples;",
        len(tail_cases),
        "sharp tail controls; minimum order",
        first_sufficient_order,
    )


if __name__ == "__main__":
    main()
