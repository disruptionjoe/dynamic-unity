#!/usr/bin/env python3
"""Exact controls for the HC-DU-184 joined depth/head-tail boundary.

The probe separates a joined per-event depth and orientation-statistic packet
from event-level orientation certification. Passing establishes finite rank,
binary-testing, and factorization facts only. It does not simulate DRIFT,
validate its systematics, or establish new physics.
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
    / "du_drift_joined_depth_head_tail_result.json"
)


def factors(
    histories: tuple[str, ...],
    record: dict[str, object],
    target: dict[str, object],
) -> bool:
    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in histories
        for right in histories
    )


def total_variation(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right)) / 2


def mean(
    values: tuple[int, ...],
    law: tuple[Fraction, ...],
) -> Fraction:
    return sum(Fraction(value) * probability for value, probability in zip(values, law))


def as_pair(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    # The same event packet contains two carrier times and a track-asymmetry
    # statistic. This fixture represents joined coordinates, not DRIFT data.
    histories = ("forward", "reverse")
    joined_packet = {
        "forward": {
            "minority_time": Fraction(2),
            "main_time": Fraction(5),
            "asymmetry": Fraction(1, 4),
        },
        "reverse": {
            "minority_time": Fraction(2),
            "main_time": Fraction(5),
            "asymmetry": Fraction(-1, 4),
        },
    }
    checks.append(
        {
            "name": "one_packet_can_join_depth_timing_and_orientation_statistic",
            "passed": (
                joined_packet["forward"]["minority_time"]
                == joined_packet["reverse"]["minority_time"]
                and joined_packet["forward"]["main_time"]
                == joined_packet["reverse"]["main_time"]
                and joined_packet["forward"]["asymmetry"]
                != joined_packet["reverse"]["asymmetry"]
            ),
        }
    )

    first_velocity = Fraction(2)
    second_velocity = Fraction(1)
    determinant = Fraction(1, second_velocity) - Fraction(1, first_velocity)
    checks.append(
        {
            "name": "distinct_carrier_velocities_retain_full_depth_rank",
            "passed": determinant != 0,
            "determinant": as_pair(determinant),
        }
    )

    # An unresolved or missing minority peak returns the one-carrier
    # event-time/depth ambiguity.
    clock_depth_histories = ("early_deep", "late_shallow")
    one_peak_record = {
        "early_deep": Fraction(3),
        "late_shallow": Fraction(3),
    }
    depth_target = {
        "early_deep": Fraction(6),
        "late_shallow": Fraction(4),
    }
    checks.append(
        {
            "name": "missing_minority_peak_restores_depth_ambiguity",
            "passed": not factors(
                clock_depth_histories,
                one_peak_record,
                depth_target,
            ),
        }
    )

    # A signed ensemble mean can reverse with physical orientation while the
    # one-event laws still overlap strongly.
    statistic_values = (-1, 0, 1)
    forward_law = (
        Fraction(0),
        Fraction(3, 4),
        Fraction(1, 4),
    )
    reverse_law = (
        Fraction(1, 4),
        Fraction(3, 4),
        Fraction(0),
    )
    forward_mean = mean(statistic_values, forward_law)
    reverse_mean = mean(statistic_values, reverse_law)
    checks.append(
        {
            "name": "ensemble_mean_tracks_reversal",
            "passed": (
                forward_mean == Fraction(1, 4)
                and reverse_mean == Fraction(-1, 4)
            ),
            "forward_mean": as_pair(forward_mean),
            "reverse_mean": as_pair(reverse_mean),
        }
    )

    tv = total_variation(forward_law, reverse_law)
    one_event_error = (1 - tv) / 2
    checks.append(
        {
            "name": "ensemble_asymmetry_does_not_give_zero_error_event_sense",
            "passed": tv == Fraction(1, 4) and one_event_error == Fraction(3, 8),
            "total_variation": as_pair(tv),
            "minimum_equal_prior_error": as_pair(one_event_error),
        }
    )

    # In this fixture an informative nonzero outcome reveals the direction,
    # while the shared zero outcome remains ambiguous. Independent samples
    # therefore improve aggregate detection without repairing one event.
    four_event_error = Fraction(1, 2) * Fraction(3, 4) ** 4
    checks.append(
        {
            "name": "replication_strengthens_ensemble_detection_only",
            "passed": (
                four_event_error == Fraction(81, 512)
                and four_event_error < one_event_error
                and one_event_error > 0
            ),
            "four_event_equal_prior_error": as_pair(four_event_error),
        }
    )

    disjoint_forward = (Fraction(0), Fraction(0), Fraction(1))
    disjoint_reverse = (Fraction(1), Fraction(0), Fraction(0))
    checks.append(
        {
            "name": "disjoint_orientation_laws_are_zero_error_positive_control",
            "passed": (
                total_variation(disjoint_forward, disjoint_reverse) == 1
            ),
        }
    )

    # A known source placement labels the calibration run. It enlarges the
    # record rather than making source-free event direction intrinsic.
    same_statistic = {
        "forward": Fraction(0),
        "reverse": Fraction(0),
    }
    orientation = {
        "forward": "forward",
        "reverse": "reverse",
    }
    source_tagged_record = {
        "forward": ("source-at-positive-z", Fraction(0)),
        "reverse": ("source-at-negative-z", Fraction(0)),
    }
    checks.append(
        {
            "name": "known_source_geometry_repairs_ambiguous_event_by_side_information",
            "passed": (
                not factors(histories, same_statistic, orientation)
                and factors(histories, source_tagged_record, orientation)
            ),
        }
    )

    # Even a joined depth/asymmetry packet can be compatible with several
    # recoil species or upstream causes.
    source_histories = ("carbon_recoil", "fluorine_recoil")
    same_complete_packet = {
        history: joined_packet["forward"]
        for history in source_histories
    }
    species = {
        "carbon_recoil": "carbon",
        "fluorine_recoil": "fluorine",
    }
    checks.append(
        {
            "name": "joined_depth_head_tail_packet_need_not_factor_species",
            "passed": not factors(
                source_histories,
                same_complete_packet,
                species,
            ),
        }
    )

    # A trigger tag can retain one waveform acquisition without proving that
    # the selected asymmetry is an exact upstream direction certificate.
    triggered_record = {
        history: ("trigger-7", same_statistic[history])
        for history in histories
    }
    checks.append(
        {
            "name": "triggered_acquisition_does_not_force_event_orientation",
            "passed": not factors(histories, triggered_record, orientation),
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-184",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "One physical packet can join absolute-depth carriers and a "
            "head-tail statistic. A reversal-sensitive ensemble mean does "
            "not imply zero-error orientation for one event; event-level "
            "certification requires disjoint laws or an explicit error."
        ),
        "non_claims": [
            "No DRIFT detector response or calibration is simulated.",
            "No reported systematic effect is resolved.",
            "No event source or recoil species is certified.",
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
