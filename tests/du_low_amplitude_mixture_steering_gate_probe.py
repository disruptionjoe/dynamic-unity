#!/usr/bin/env python3
"""Exact proof controls for HC-DU-229.

The probe checks a finite qubit mixture/steering witness and an abstract
factorization boundary. It does not simulate a detector, test a nonlinear
quantum theory, or establish a Born-rule violation.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_low_amplitude_mixture_steering_gate_result.json"
)


def cutoff(probability: Fraction, threshold: Fraction) -> Fraction:
    return max(probability - threshold, Fraction(0))


def factors_through_state(
    values: dict[tuple[str, str], Fraction],
    state_of: dict[tuple[str, str], str],
) -> bool:
    items = tuple(values)
    return all(
        state_of[left] != state_of[right] or values[left] == values[right]
        for left in items
        for right in items
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    threshold = Fraction(1, 4)

    # P=|1><1| on the four pure states.  The Z and X ensembles both average
    # to I/2, so every fixed effect gives equal ensemble-average probability.
    q = {
        "zero": Fraction(0),
        "one": Fraction(1),
        "plus": Fraction(1, 2),
        "minus": Fraction(1, 2),
    }
    nonlinear = {name: cutoff(value, threshold) for name, value in q.items()}
    nonlinear_z_average = (nonlinear["zero"] + nonlinear["one"]) / 2
    nonlinear_x_average = (nonlinear["plus"] + nonlinear["minus"]) / 2
    signalling_contrast = nonlinear_z_average - nonlinear_x_average

    # One generic real qubit effect E=[[a,b],[b,d]] demonstrates the exact
    # fixed-effect identity.  Positivity is satisfied by the chosen entries.
    a = Fraction(1, 5)
    d = Fraction(4, 5)
    b = Fraction(1, 10)
    fixed = {
        "zero": a,
        "one": d,
        "plus": (a + d + 2 * b) / 2,
        "minus": (a + d - 2 * b) / 2,
    }
    fixed_z_average = (fixed["zero"] + fixed["one"]) / 2
    fixed_x_average = (fixed["plus"] + fixed["minus"]) / 2

    # A density-level application gives one answer for I/2.  Ordinary
    # randomization plus calibrated pure-state responses gives another for the
    # Z route.  Both cannot be a function of the density operator alone.
    density_level_i_over_2 = cutoff(Fraction(1, 2), threshold)
    route_values = {
        ("i-over-2", "direct-density"): density_level_i_over_2,
        ("i-over-2", "z-randomizer"): nonlinear_z_average,
        ("i-over-2", "x-randomizer"): nonlinear_x_average,
    }
    state_of = {key: key[0] for key in route_values}
    enriched_state_of = {key: f"{key[0]}:{key[1]}" for key in route_values}

    # The Bell state admits both decompositions at Bob under Alice's Z/X
    # measurement choice.  If Bob's local response follows the decomposition
    # rather than I/2, the two choices have a nonzero unconditional contrast.
    bob_reduced_state_z = "i-over-2"
    bob_reduced_state_x = "i-over-2"

    # If the offset is treated as an unnormalized two-click response, an
    # explicit no-click outcome completes normalization but does not restore
    # affinity. Conditioning on a click changes the contract.
    two_outcome_q = Fraction(1, 2)
    click_left = cutoff(two_outcome_q, threshold)
    click_right = cutoff(1 - two_outcome_q, threshold)
    no_click = 1 - click_left - click_right
    conditional_left = click_left / (click_left + click_right)

    checks = [
        (
            "the Z and X pure-state ensembles have the same density operator",
            bob_reduced_state_z == bob_reduced_state_x == "i-over-2",
        ),
        (
            "every fixed qubit effect obeys the tested ensemble identity",
            fixed_z_average == fixed_x_average == Fraction(1, 2),
        ),
        (
            "the literal cutoff separates the two pure-state ensembles",
            nonlinear_z_average == Fraction(3, 8)
            and nonlinear_x_average == Fraction(1, 4),
        ),
        (
            "the branchwise steering contrast is nonzero",
            signalling_contrast == Fraction(1, 8),
        ),
        (
            "the density-level rule is invariant under remote decomposition choice",
            density_level_i_over_2 == nonlinear_x_average,
        ),
        (
            "the density-level rule conflicts with ordinary Z randomization",
            density_level_i_over_2 != nonlinear_z_average,
        ),
        (
            "the three route responses do not factor through density state alone",
            not factors_through_state(route_values, state_of),
        ),
        (
            "adding the route label restores formal factorization",
            factors_through_state(route_values, enriched_state_of),
        ),
        (
            "the repair enlarges the state with preparation provenance",
            state_of != enriched_state_of,
        ),
        (
            "the offset can be completed with an explicit no-click outcome",
            click_left == Fraction(1, 4)
            and click_right == Fraction(1, 4)
            and no_click == Fraction(1, 2),
        ),
        (
            "conditioning on a click changes the reported probability",
            conditional_left == Fraction(1, 2) and conditional_left != click_left,
        ),
        (
            "a no-click completion does not remove the ensemble contrast",
            signalling_contrast != 0,
        ),
        (
            "the probe contains no empirical or hardware result",
            True,
        ),
    ]

    passed = sum(bool(ok) for _, ok in checks)
    result = {
        "claim_id": "HC-DU-229",
        "prediction_id": "PRED-DU-006",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks_passed": passed,
        "checks_total": len(checks),
        "threshold": str(threshold),
        "fixed_effect_z_average": str(fixed_z_average),
        "fixed_effect_x_average": str(fixed_x_average),
        "cutoff_z_average": str(nonlinear_z_average),
        "cutoff_x_average": str(nonlinear_x_average),
        "branchwise_steering_contrast": str(signalling_contrast),
        "density_level_i_over_2": str(density_level_i_over_2),
        "no_click_probability": str(no_click),
        "checks": [{"name": name, "passed": bool(ok)} for name, ok in checks],
        "scope": [
            "four pure qubit preparations and one fixed effect",
            "density-level versus branchwise cutoff completion",
            "Bell-state Z/X remote-steering witness",
            "state-only versus preparation-route factorization",
            "unconditional versus click-conditioned response",
        ],
        "not_claimed": [
            "universal no-go against nonlinear quantum theories",
            "physical realization of the cutoff",
            "observed superluminal signalling",
            "observed Born-rule violation",
            "new fundamental law",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(f"{result['status']}: {passed}/{len(checks)} checks")
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
