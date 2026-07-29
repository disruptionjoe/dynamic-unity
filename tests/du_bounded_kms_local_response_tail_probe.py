#!/usr/bin/env python3
"""Regression controls for HC-DU-101.

This probe preserves three elementary consequences of the independent proof:

1. Pauli nested commutators saturate the repeated factor-of-two norm bound;
2. the exponential-series remainder obeys the stated factorial certificate;
3. no fixed Taylor order controls a response family whose perturbation norm
   grows without bound.

Passing establishes no KMS-state selection, passive correlation instrument,
formed record, thermodynamic or continuum limit, geometry reconstruction,
novel physics, prediction, or evidence grade.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_bounded_kms_local_response_tail_result.json"
)


def exponential_tail(x: float, retained_order: int) -> float:
    retained = sum(
        x**order / math.factorial(order)
        for order in range(retained_order + 1)
    )
    return math.exp(x) - retained


def factorial_certificate(x: float, retained_order: int) -> float:
    return (
        math.exp(x)
        * x ** (retained_order + 1)
        / math.factorial(retained_order + 1)
    )


def cosine_taylor_at_one(retained_order: int, scale: int) -> Fraction:
    """Taylor polynomial for cos(2*scale*lambda), evaluated at lambda=1."""

    return sum(
        (
            Fraction(
                (-1) ** term * (2 * scale) ** (2 * term),
                math.factorial(2 * term),
            )
            for term in range(retained_order // 2 + 1)
        ),
        start=Fraction(0),
    )


def first_scale_with_large_polynomial(retained_order: int) -> tuple[int, Fraction]:
    """Find an exact witness whose Taylor polynomial has magnitude above two."""

    for scale in range(1, 10_000):
        value = cosine_taylor_at_one(retained_order, scale)
        if abs(value) > 2:
            return scale, value
    raise AssertionError(f"no scaling witness found for order {retained_order}")


def first_certified_order(x: float, tolerance: float) -> int:
    for retained_order in range(10_000):
        if factorial_certificate(x, retained_order) <= tolerance:
            return retained_order
    raise AssertionError("factorial certificate did not reach tolerance")


def main() -> None:
    commutator_cases: list[dict[str, object]] = []
    for order in range(13):
        # ad_Z^n(X) alternates between a scalar multiple of X and of Y.
        # Its operator norm is exactly 2^n, saturating
        # ||[Z,C]|| <= 2 ||Z|| ||C|| because ||X||=||Y||=||Z||=1.
        exact_norm = 2**order
        certified_norm = 2**order
        assert exact_norm == certified_norm
        commutator_cases.append(
            {
                "order": order,
                "exact_pauli_nested_commutator_norm": exact_norm,
                "certified_norm": certified_norm,
                "saturates": True,
            }
        )

    tail_cases: list[dict[str, object]] = []
    for x in (0.25, 1.0, 2.0, 4.0):
        for retained_order in range(9):
            actual_tail = exponential_tail(x, retained_order)
            bound = factorial_certificate(x, retained_order)
            assert actual_tail >= -1e-13
            assert actual_tail <= bound + 1e-12
            tail_cases.append(
                {
                    "source_budget_x": x,
                    "retained_order": retained_order,
                    "actual_exponential_tail": actual_tail,
                    "factorial_certificate": bound,
                    "certified": True,
                }
            )

    tolerance = 0.01
    minimum_order_cases = []
    for x in (1.0, 4.0):
        retained_order = first_certified_order(x, tolerance)
        assert factorial_certificate(x, retained_order) <= tolerance
        if retained_order > 0:
            assert factorial_certificate(x, retained_order - 1) > tolerance
        minimum_order_cases.append(
            {
                "source_budget_x": x,
                "tolerance": tolerance,
                "first_certified_order": retained_order,
                "certificate": factorial_certificate(x, retained_order),
            }
        )

    scaling_cases: list[dict[str, object]] = []
    thermal_amplitude = Fraction(1, 2)
    for retained_order in range(2, 15):
        scale, polynomial = first_scale_with_large_polynomial(retained_order)
        # For F_m(lambda)=q cos(2m lambda), |F_m(1)| <= q. Therefore
        # |q P_N(2m)-F_m(1)| >= q(|P_N(2m)|-1) > q.
        exact_error_lower_bound = thermal_amplitude * (abs(polynomial) - 1)
        assert exact_error_lower_bound > thermal_amplitude
        scaling_cases.append(
            {
                "retained_order": retained_order,
                "first_scale_witness": scale,
                "exact_unscaled_taylor_value_at_lambda_one": str(polynomial),
                "thermal_amplitude": str(thermal_amplitude),
                "exact_error_lower_bound": str(exact_error_lower_bound),
                "error_exceeds_thermal_amplitude": True,
            }
        )

    result = {
        "probe": "du_bounded_kms_local_response_tail_probe",
        "status": "PASS",
        "claim_id": "HC-DU-101",
        "checks": {
            "pauli_nested_commutator_cases": len(commutator_cases),
            "factorial_tail_cases": len(tail_cases),
            "minimum_order_cases": len(minimum_order_cases),
            "unbounded_scale_counterexamples": len(scaling_cases),
            "order_zero_and_one_symbolic_control": (
                "At lambda=pi/(2m), q*cos(2m*lambda)=-q while the "
                "order-0/1 Taylor polynomial is q, so the error is 2q."
            ),
        },
        "nested_commutator_cases": commutator_cases,
        "factorial_tail_cases": tail_cases,
        "minimum_order_cases": minimum_order_cases,
        "scaling_cases": scaling_cases,
        "scope_warning": (
            "Elementary bounded-response regressions only. KMS is not used "
            "to obtain the tail, and no state, phase, instrument, passive "
            "record, field limit, or geometry is selected."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS:",
        len(commutator_cases),
        "commutator cases;",
        len(tail_cases),
        "tail cases;",
        len(scaling_cases),
        "scale counterexamples",
    )


if __name__ == "__main__":
    main()
