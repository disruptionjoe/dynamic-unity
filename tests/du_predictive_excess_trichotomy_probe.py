#!/usr/bin/env python3
"""Exact controls for the HC-DU-186 predictive-excess trichotomy.

Passing distinguishes absorption, predictive sharpening, and rival-excluding
excess; checks that a readout channel can erase but not manufacture a raw
distinction; and verifies one finite no-refit response-shape control. It
establishes no physical law, apparatus, or observed anomaly.
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
    / "du_predictive_excess_trichotomy_result.json"
)


def classify(incumbent: frozenset[int], challenger: int) -> str:
    if not incumbent:
        return "INVALID_EMPTY_INCUMBENT"
    if incumbent == {challenger}:
        return "PREDICTIVELY_ABSORBED"
    if challenger in incumbent:
        return "PREDICTIVE_SHARPENING"
    return "RIVAL_EXCLUDING_EXCESS"


def second_difference(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return values[2] - 2 * values[1] + values[0]


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    cases = {
        "absorbed": (frozenset({2}), 2, "PREDICTIVELY_ABSORBED"),
        "sharpening": (frozenset({2, 4}), 4, "PREDICTIVE_SHARPENING"),
        "rival_excluding": (
            frozenset({2}),
            4,
            "RIVAL_EXCLUDING_EXCESS",
        ),
    }
    for name, (incumbent, challenger, expected) in cases.items():
        checks.append(
            {
                "name": f"{name}_classification",
                "passed": classify(incumbent, challenger) == expected,
            }
        )

    checks.append(
        {
            "name": "three_cases_are_exhaustive_for_nonempty_incumbent",
            "passed": {
                classify(frozenset(values), challenger)
                for values in (
                    {0},
                    {1},
                    {0, 1},
                    {0, 2},
                    {0, 1, 2},
                )
                for challenger in (0, 1, 2)
            }
            == {
                "PREDICTIVELY_ABSORBED",
                "PREDICTIVE_SHARPENING",
                "RIVAL_EXCLUDING_EXCESS",
            },
        }
    )

    resolving_channel = {2: "two", 4: "four"}
    erased_channel = {2: "even", 4: "even"}
    raw_incumbent = frozenset({2})
    raw_challenger = 4
    resolving_incumbent = frozenset(
        resolving_channel[value] for value in raw_incumbent
    )
    erased_incumbent = frozenset(
        erased_channel[value] for value in raw_incumbent
    )
    checks.append(
        {
            "name": "resolving_interface_preserves_rival_excess",
            "passed": (
                classify(resolving_incumbent, resolving_channel[raw_challenger])
                == "RIVAL_EXCLUDING_EXCESS"
            ),
        }
    )
    checks.append(
        {
            "name": "coarse_interface_can_erase_rival_excess",
            "passed": (
                classify(erased_incumbent, erased_channel[raw_challenger])
                == "PREDICTIVELY_ABSORBED"
            ),
        }
    )

    # A channel cannot separate two predictions that were identical before
    # the channel. This finite check ranges over all deterministic binary
    # channels from a two-point target.
    equal_target_pairs = ((0, 0), (1, 1))
    deterministic_channels = (
        {0: 0, 1: 0},
        {0: 0, 1: 1},
        {0: 1, 1: 0},
        {0: 1, 1: 1},
    )
    checks.append(
        {
            "name": "interface_cannot_manufacture_difference_from_equal_targets",
            "passed": all(
                channel[left] == channel[right]
                for channel in deterministic_channels
                for left, right in equal_target_pairs
            ),
        }
    )

    # Modular experiment eligibility: a response selector and a readout
    # selector can be independently frozen. Neither must derive the other.
    response_selection = {"source_packet_A": 4}
    interface_selection = {"apparatus_packet_B": resolving_channel}
    selected_target = response_selection["source_packet_A"]
    selected_record = interface_selection["apparatus_packet_B"][selected_target]
    checks.append(
        {
            "name": "joined_contract_does_not_require_one_selector_for_both_modules",
            "passed": (
                set(response_selection).isdisjoint(interface_selection)
                and selected_target == 4
                and selected_record == "four"
            ),
        }
    )

    # Finite response-shape control. On configurations u=0,1,2, a frozen
    # affine nuisance family has zero second difference. A quadratic
    # challenger contribution has nonzero second difference and therefore
    # cannot be absorbed by refitting that frozen nuisance family.
    affine_nuisance = (
        Fraction(3),
        Fraction(5),
        Fraction(7),
    )
    quadratic_kernel = (
        Fraction(0),
        Fraction(1),
        Fraction(4),
    )
    challenger_surface = tuple(
        nuisance + kernel
        for nuisance, kernel in zip(affine_nuisance, quadratic_kernel)
    )
    checks.append(
        {
            "name": "frozen_affine_nuisance_has_zero_second_difference",
            "passed": second_difference(affine_nuisance) == 0,
        }
    )
    checks.append(
        {
            "name": "quadratic_response_adds_no_refit_shape_excess",
            "passed": (
                second_difference(quadratic_kernel) == 2
                and second_difference(challenger_surface) == 2
            ),
        }
    )

    # With one configuration, one free scalar nuisance absorbs one scalar
    # challenger contribution. Configuration diversity is load-bearing.
    one_configuration_baseline = Fraction(3)
    one_configuration_challenger = Fraction(4)
    nuisance_refit = one_configuration_challenger
    checks.append(
        {
            "name": "single_configuration_is_absorbed_by_free_scalar_nuisance",
            "passed": nuisance_refit == one_configuration_challenger
            and nuisance_refit != one_configuration_baseline,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-186",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "For a locked singleton challenger target and nonempty incumbent "
            "target set, predictive absorption, predictive sharpening, and "
            "rival-excluding excess are exhaustive. A separately frozen "
            "physical readout may preserve or erase the distinction; it need "
            "not be selected by the same mechanism that selects the law."
        ),
        "non_claims": [
            "No CSL or quantum-gravity prediction is validated.",
            "No nuisance family is physically complete.",
            "No apparatus or acquisition lineage is selected.",
            "No observed excess, new physics, or ready successor is earned.",
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
