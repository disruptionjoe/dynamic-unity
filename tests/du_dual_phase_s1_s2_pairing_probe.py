#!/usr/bin/env python3
"""Exact controls for the HC-DU-183 dual-phase S1/S2 pairing boundary.

The probe separates acquired prompt and delayed peaks from their physical
event pairing. Passing establishes finite matching and factorization facts
only. It does not simulate xenon response, select an event builder, certify
an interaction source, or establish new physics.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_dual_phase_s1_s2_pairing_result.json"
)


def factors(
    histories: tuple[str, ...],
    record: dict[str, object],
    target: dict[str, object],
) -> bool:
    """Return whether target is constant on every record fibre."""

    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in histories
        for right in histories
    )


def admissible_matchings(
    s1_times: tuple[int, ...],
    s2_times: tuple[int, ...],
    minimum_delay: int,
    maximum_delay: int,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    """Enumerate perfect S1/S2 matchings allowed by a drift-time window."""

    matchings: list[tuple[tuple[int, int], ...]] = []
    for permutation in itertools.permutations(range(len(s2_times))):
        pairs = tuple((index, permutation[index]) for index in range(len(s1_times)))
        if all(
            minimum_delay
            <= s2_times[s2_index] - s1_times[s1_index]
            <= maximum_delay
            for s1_index, s2_index in pairs
        ):
            matchings.append(pairs)
    return tuple(matchings)


def depths(
    matching: tuple[tuple[int, int], ...],
    s1_times: tuple[int, ...],
    s2_times: tuple[int, ...],
    drift_velocity: Fraction,
) -> tuple[Fraction, ...]:
    return tuple(
        drift_velocity * (s2_times[s2_index] - s1_times[s1_index])
        for s1_index, s2_index in matching
    )


def total_variation(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right)) / 2


def as_pair(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    # Every cross-pair lies inside the declared drift window. The same
    # triggerless peak stream therefore admits two perfect event matchings.
    s1_times = (0, 1)
    s2_times = (3, 4)
    ambiguous_matchings = admissible_matchings(s1_times, s2_times, 2, 4)
    checks.append(
        {
            "name": "drift_window_can_admit_multiple_exact_s1_s2_matchings",
            "passed": len(ambiguous_matchings) == 2,
            "matching_count": len(ambiguous_matchings),
        }
    )

    histories = ("direct_pairing", "cross_pairing")
    common_peak_stream = {
        history: (("S1", s1_times), ("S2", s2_times))
        for history in histories
    }
    event_pairing = {
        history: ambiguous_matchings[index]
        for index, history in enumerate(histories)
    }
    checks.append(
        {
            "name": "raw_triggerless_peaks_do_not_factor_event_pairing",
            "passed": not factors(histories, common_peak_stream, event_pairing),
        }
    )

    drift_velocity = Fraction(2)
    paired_depths = {
        history: depths(
            event_pairing[history],
            s1_times,
            s2_times,
            drift_velocity,
        )
        for history in histories
    }
    checks.append(
        {
            "name": "raw_triggerless_peaks_do_not_factor_paired_depths",
            "passed": (
                paired_depths["direct_pairing"]
                != paired_depths["cross_pairing"]
                and not factors(histories, common_peak_stream, paired_depths)
            ),
        }
    )

    # A physical tag that travels with both channels enlarges the record and
    # repairs this fixture. It is not supplied by an untagged time window.
    tagged_packet = {
        "direct_pairing": (
            ("event-A", "S1", 0),
            ("event-A", "S2", 3),
            ("event-B", "S1", 1),
            ("event-B", "S2", 4),
        ),
        "cross_pairing": (
            ("event-A", "S1", 0),
            ("event-A", "S2", 4),
            ("event-B", "S1", 1),
            ("event-B", "S2", 3),
        ),
    }
    checks.append(
        {
            "name": "retained_common_event_tag_repairs_pairing_fixture",
            "passed": (
                factors(histories, tagged_packet, event_pairing)
                and factors(histories, tagged_packet, paired_depths)
            ),
        }
    )

    # A source-pinned low-rate or topology-restricted class can instead make
    # the compatibility graph uniquely matchable. That narrows completions.
    unique_s1 = (0, 5)
    unique_s2 = (2, 9)
    unique_matchings = admissible_matchings(unique_s1, unique_s2, 2, 4)
    checks.append(
        {
            "name": "unique_compatibility_graph_conditionally_selects_pairing",
            "passed": unique_matchings == (((0, 0), (1, 1)),),
            "matching_count": len(unique_matchings),
        }
    )

    unique_depths = depths(
        unique_matchings[0],
        unique_s1,
        unique_s2,
        drift_velocity,
    )
    checks.append(
        {
            "name": "correctly_paired_s1_s2_delay_reconstructs_depth",
            "passed": unique_depths == (Fraction(4), Fraction(8)),
        }
    )

    # S2 alone retains arrival time but loses the prompt origin. Two
    # time/depth histories can therefore share the same delayed peak.
    s2_only_histories = ("early_deep", "late_shallow")
    s2_only_record = {
        "early_deep": 6,
        "late_shallow": 6,
    }
    absolute_depth = {
        "early_deep": 6,
        "late_shallow": 4,
    }
    event_time = {
        "early_deep": 0,
        "late_shallow": 2,
    }
    checks.append(
        {
            "name": "s2_only_peak_does_not_factor_event_time_or_depth",
            "passed": (
                not factors(s2_only_histories, s2_only_record, absolute_depth)
                and not factors(s2_only_histories, s2_only_record, event_time)
            ),
        }
    )

    # Storing every peak losslessly preserves acquisition but not the missing
    # pairing coordinate.
    archived_stream = dict(common_peak_stream)
    checks.append(
        {
            "name": "lossless_triggerless_archive_does_not_create_pairing",
            "passed": (
                archived_stream == common_peak_stream
                and not factors(histories, archived_stream, event_pairing)
            ),
        }
    )

    # S2/S1 response is useful for statistical recoil discrimination but
    # overlapping laws do not certify the class of one event with zero error.
    electronic_recoil_law = (
        Fraction(3, 5),
        Fraction(2, 5),
        Fraction(0),
    )
    nuclear_recoil_law = (
        Fraction(0),
        Fraction(2, 5),
        Fraction(3, 5),
    )
    tv = total_variation(electronic_recoil_law, nuclear_recoil_law)
    equal_prior_error = (1 - tv) / 2
    checks.append(
        {
            "name": "overlapping_s2_s1_laws_are_not_zero_error_certificates",
            "passed": tv == Fraction(3, 5) and equal_prior_error == Fraction(1, 5),
            "total_variation": as_pair(tv),
            "minimum_equal_prior_error": as_pair(equal_prior_error),
        }
    )

    source_histories = ("signal_source", "background_source")
    same_complete_event_packet = {
        history: tagged_packet["direct_pairing"]
        for history in source_histories
    }
    source_identity = {
        "signal_source": "signal",
        "background_source": "background",
    }
    checks.append(
        {
            "name": "complete_detector_event_packet_need_not_factor_source_identity",
            "passed": not factors(
                source_histories,
                same_complete_event_packet,
                source_identity,
            ),
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-183",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "A dual-phase prompt-delayed packet conditionally reconstructs "
            "depth only after S1/S2 event pairing is fixed. A drift-time "
            "window can admit multiple perfect matchings, so lossless "
            "triggerless acquisition does not itself certify event identity."
        ),
        "non_claims": [
            "No xenon detector response or accidental-coincidence rate is simulated.",
            "No event builder, archive, source, or observer is selected.",
            "No recoil class is certified with zero error.",
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
