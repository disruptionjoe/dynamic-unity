#!/usr/bin/env python3
"""Exact controls for the HC-DU-182 time-resolved TPC packet boundary.

The probe separates a one-carrier arrival timestamp from an absolute event
time and drift depth, proves the exact two-carrier rank repair, and separates
raw acquired hits from physical event membership. Passing establishes only
finite factorization and rank facts. It does not model a TPC, select a
trigger, prove head-tail sense, identify a source, or establish new physics.
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
    / "du_time_resolved_tpc_record_packet_result.json"
)


def factors(
    histories: tuple[str, ...],
    record: dict[str, object],
    target: dict[str, object],
) -> bool:
    """Return whether the target is constant on every record fibre."""

    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in histories
        for right in histories
    )


def arrivals(
    event_time: Fraction,
    depth: Fraction,
    velocities: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(event_time + depth / velocity for velocity in velocities)


def reconstruct_two_carrier(
    first_arrival: Fraction,
    second_arrival: Fraction,
    first_velocity: Fraction,
    second_velocity: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return (event_time, depth) for distinct calibrated velocities."""

    denominator = Fraction(1, first_velocity) - Fraction(1, second_velocity)
    if denominator == 0:
        raise ValueError("two-carrier reconstruction needs distinct velocities")
    depth = (first_arrival - second_arrival) / denominator
    event_time = first_arrival - depth / first_velocity
    return event_time, depth


def as_pair(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def run_probe() -> dict[str, object]:
    histories = ("early_deep", "late_shallow")
    event_time = {
        "early_deep": Fraction(0),
        "late_shallow": Fraction(1),
    }
    depth = {
        "early_deep": Fraction(6),
        "late_shallow": Fraction(4),
    }

    # One carrier at velocity 2 gives arrival time 3 in both histories.
    one_carrier_record = {
        history: arrivals(
            event_time[history],
            depth[history],
            (Fraction(2),),
        )
        for history in histories
    }

    checks: list[dict[str, object]] = []
    checks.append(
        {
            "name": "one_carrier_arrival_does_not_factor_event_time",
            "passed": (
                len(set(one_carrier_record.values())) == 1
                and not factors(histories, one_carrier_record, event_time)
            ),
        }
    )
    checks.append(
        {
            "name": "one_carrier_arrival_does_not_factor_depth",
            "passed": not factors(histories, one_carrier_record, depth),
        }
    )

    first_velocity = Fraction(2)
    second_velocity = Fraction(3)
    determinant = Fraction(1, second_velocity) - Fraction(1, first_velocity)
    two_carrier_record = {
        history: arrivals(
            event_time[history],
            depth[history],
            (first_velocity, second_velocity),
        )
        for history in histories
    }
    checks.append(
        {
            "name": "distinct_carrier_velocities_have_full_clock_depth_rank",
            "passed": determinant != 0,
            "determinant": as_pair(determinant),
        }
    )

    reconstructed = {
        history: reconstruct_two_carrier(
            two_carrier_record[history][0],
            two_carrier_record[history][1],
            first_velocity,
            second_velocity,
        )
        for history in histories
    }
    checks.append(
        {
            "name": "two_carrier_packet_exactly_reconstructs_time_and_depth",
            "passed": all(
                reconstructed[history]
                == (event_time[history], depth[history])
                for history in histories
            )
            and factors(histories, two_carrier_record, event_time)
            and factors(histories, two_carrier_record, depth),
        }
    )

    equal_velocity_record = {
        history: arrivals(
            event_time[history],
            depth[history],
            (Fraction(2), Fraction(2)),
        )
        for history in histories
    }
    checks.append(
        {
            "name": "duplicate_carrier_speed_does_not_repair_rank",
            "passed": (
                len(set(equal_velocity_record.values())) == 1
                and not factors(histories, equal_velocity_record, event_time)
                and not factors(histories, equal_velocity_record, depth)
            ),
        }
    )

    # A raw acquired hit stream can be identical under distinct occurrence
    # partitions. Event building is therefore a separately typed target.
    partitions = ("one_occurrence", "two_occurrences")
    raw_hits = (
        ("p00", Fraction(10), Fraction(4)),
        ("p01", Fraction(11), Fraction(3)),
        ("p10", Fraction(20), Fraction(5)),
        ("p11", Fraction(21), Fraction(2)),
    )
    raw_packet = {history: raw_hits for history in partitions}
    event_partition = {
        "one_occurrence": (("p00", "p01", "p10", "p11"),),
        "two_occurrences": (("p00", "p01"), ("p10", "p11")),
    }
    checks.append(
        {
            "name": "raw_hit_packet_does_not_factor_event_membership",
            "passed": not factors(partitions, raw_packet, event_partition),
        }
    )

    acquired_event_tags = {
        "one_occurrence": tuple(
            (hit[0], "event-A", hit[1], hit[2]) for hit in raw_hits
        ),
        "two_occurrences": tuple(
            (
                hit[0],
                "event-A" if index < 2 else "event-B",
                hit[1],
                hit[2],
            )
            for index, hit in enumerate(raw_hits)
        ),
    }
    checks.append(
        {
            "name": "physically_retained_event_tag_repairs_partition_fixture",
            "passed": factors(
                partitions,
                acquired_event_tags,
                event_partition,
            ),
        }
    )

    # A deterministic clustering rule applied only to the common raw packet
    # produces one answer on both histories and therefore cannot be an exact
    # decoder for both physical occurrence partitions.
    clustering_output = {
        history: (("p00", "p01"), ("p10", "p11"))
        for history in partitions
    }
    checks.append(
        {
            "name": "algorithmic_clustering_does_not_create_event_provenance",
            "passed": (
                clustering_output["one_occurrence"]
                == clustering_output["two_occurrences"]
                and not factors(partitions, raw_packet, event_partition)
            ),
        }
    )

    # Removing the minority-carrier time returns the exact one-carrier
    # ambiguity even when the majority packet is archived losslessly.
    archived_majority_only = dict(one_carrier_record)
    checks.append(
        {
            "name": "lossless_archive_cannot_repair_missing_minority_peak",
            "passed": (
                archived_majority_only == one_carrier_record
                and not factors(
                    histories,
                    archived_majority_only,
                    event_time,
                )
                and not factors(
                    histories,
                    archived_majority_only,
                    depth,
                )
            ),
        }
    )

    # The joined packet can retain coordinates, times, and charge while
    # leaving source identity outside its exact fibres.
    source_histories = ("neutron_source", "background_source")
    complete_same_packet = {
        history: acquired_event_tags["two_occurrences"]
        for history in source_histories
    }
    source_identity = {
        "neutron_source": "neutron",
        "background_source": "background",
    }
    checks.append(
        {
            "name": "joined_acquisition_packet_need_not_factor_source_identity",
            "passed": not factors(
                source_histories,
                complete_same_packet,
                source_identity,
            ),
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-182",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "One carrier records event-time-plus-depth only. Two distinct "
            "calibrated carrier velocities give a full-rank exact repair. "
            "Raw acquired hits still do not select event membership or "
            "source identity, and lossless storage cannot add an absent "
            "carrier or provenance tag."
        ),
        "non_claims": [
            "No TPC dynamics or detector efficiency is simulated.",
            "No trigger, event builder, archive, or observer is selected.",
            "No head-tail sense or source identity is certified.",
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
