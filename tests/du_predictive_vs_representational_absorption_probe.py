#!/usr/bin/env python3
"""Exact controls for the HC-DU-185 absorption-gate correction.

Passing separates a framework's ability to represent a law from an
incumbent theory's ability to predict a held-out target. It also checks the
coordinate stability of the first nonzero response difference under a
nonsingular source reparameterization. It establishes no new physical law.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_predictive_vs_representational_absorption_result.json"
)


def evaluate(coefficients: tuple[Fraction, ...], value: Fraction) -> Fraction:
    return sum(
        coefficient * value**power
        for power, coefficient in enumerate(coefficients)
    )


def first_nonzero_order(coefficients: tuple[Fraction, ...]) -> int | None:
    for order, coefficient in enumerate(coefficients):
        if coefficient != 0:
            return order
    return None


def compose_through_quartic(
    outer: tuple[Fraction, ...],
    inner: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Return coefficients of outer(inner(s)) through degree four."""

    result = [Fraction(0) for _ in range(5)]
    power = [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    for outer_coefficient in outer:
        for index, coefficient in enumerate(power):
            result[index] += outer_coefficient * coefficient
        next_power = [Fraction(0) for _ in range(5)]
        for left_index, left_coefficient in enumerate(power):
            for right_index, right_coefficient in enumerate(inner):
                degree = left_index + right_index
                if degree <= 4:
                    next_power[degree] += left_coefficient * right_coefficient
        power = next_power
    return tuple(result)


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    linear = (Fraction(0), Fraction(1), Fraction(0))
    quadratic = (Fraction(0), Fraction(0), Fraction(1))
    incumbent_family = (linear, quadratic)
    training_inputs = (Fraction(0), Fraction(1))
    held_out_input = Fraction(2)

    training_packets = {
        law: tuple(evaluate(law, value) for value in training_inputs)
        for law in incumbent_family
    }
    checks.append(
        {
            "name": "two_representable_laws_share_training_packet",
            "passed": (
                training_packets[linear] == training_packets[quadratic]
                == (Fraction(0), Fraction(1))
            ),
        }
    )

    held_out_targets = {
        law: evaluate(law, held_out_input)
        for law in incumbent_family
    }
    checks.append(
        {
            "name": "same_training_packet_has_different_held_out_targets",
            "passed": (
                held_out_targets[linear] == 2
                and held_out_targets[quadratic] == 4
            ),
        }
    )

    representational_absorption = quadratic in incumbent_family
    predictive_absorption = len(set(held_out_targets.values())) == 1
    checks.append(
        {
            "name": "representation_does_not_imply_prediction",
            "passed": representational_absorption and not predictive_absorption,
        }
    )

    challenger_selected = quadratic
    checks.append(
        {
            "name": "target_blind_selection_adds_a_locked_prediction",
            "passed": (
                held_out_targets[challenger_selected] == 4
                and not predictive_absorption
            ),
        }
    )

    restricted_incumbent = (quadratic,)
    restricted_targets = {
        law: evaluate(law, held_out_input)
        for law in restricted_incumbent
    }
    checks.append(
        {
            "name": "target_constant_incumbent_fibre_is_predictive_absorption",
            "passed": set(restricted_targets.values()) == {Fraction(4)},
        }
    )

    # Choosing the quadratic law only after revealing the held-out value is
    # a fit, not a prediction.
    locked_before_reveal = False
    after_fact_choice_matches = held_out_targets[quadratic] == 4
    checks.append(
        {
            "name": "after_fact_refit_does_not_count_as_predictive_absorption",
            "passed": after_fact_choice_matches and not locked_before_reveal,
        }
    )

    # Difference between y=x+x^2 and y=x first appears at second order.
    response_difference = (
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    checks.append(
        {
            "name": "first_nonzero_response_difference_is_well_typed",
            "passed": first_nonzero_order(response_difference) == 2,
        }
    )

    nonsingular_source_change = (
        Fraction(0),
        Fraction(1),
        Fraction(1),
    )
    composed_nonsingular = compose_through_quartic(
        response_difference,
        nonsingular_source_change,
    )
    checks.append(
        {
            "name": "nonsingular_source_change_preserves_first_difference_order",
            "passed": first_nonzero_order(composed_nonsingular) == 2,
        }
    )

    singular_source_change = (
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    composed_singular = compose_through_quartic(
        response_difference,
        singular_source_change,
    )
    checks.append(
        {
            "name": "singular_source_change_can_alter_response_order",
            "passed": first_nonzero_order(composed_singular) == 4,
        }
    )

    # A selected physical packet and a selected response law are independent
    # duties. Neither fixture field is derivable from the other.
    completions = ("same_law_tagged", "same_law_untagged")
    law_record = {completion: "quadratic" for completion in completions}
    interface_target = {
        "same_law_tagged": "formed_tag",
        "same_law_untagged": "no_tag",
    }
    interface_record = {
        "same_law_tagged": "formed_tag",
        "same_law_untagged": "no_tag",
    }
    law_target = {completion: "quadratic" for completion in completions}
    law_factors_interface = all(
        law_record[left] != law_record[right]
        or interface_target[left] == interface_target[right]
        for left in completions
        for right in completions
    )
    interface_factors_law = all(
        interface_record[left] != interface_record[right]
        or law_target[left] == law_target[right]
        for left in completions
        for right in completions
    )
    checks.append(
        {
            "name": "law_selection_does_not_select_interface_while_interface_can_retain_law",
            "passed": not law_factors_interface and interface_factors_law,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-185",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "A universal response framework can represent target-distinct "
            "laws without predicting which held-out target occurs. Scientific "
            "absorption requires target constancy on the frozen incumbent "
            "completion fibre, not mere encodability or after-fact refitting."
        ),
        "non_claims": [
            "No process tensor or effective-action theorem is refuted.",
            "No higher-response coefficient is physically selected.",
            "No detector interface follows from law selection.",
            "No new physics or ready successor is established.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the deterministic JSON result",
    )
    args = parser.parse_args()

    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
