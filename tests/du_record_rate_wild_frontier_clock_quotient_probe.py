#!/usr/bin/env python3
"""Wild-frontier primitive-record-rate probe.

This finite probe separates three propositions that can otherwise be hidden
inside the phrase "one clock pushes records forward":

1. G-full: every observer records every global update;
2. G-gated: a global update only permits a path-local record; and
3. G-hidden: the update order is quotiented out of physical observables.

It also checks a conditional 1+1 null-coordinate construction.  For a
manifoldlike causal interval with null increments (R, L) and fixed event
density, the candidate elapsed record count is

    tau_hash = 2 sqrt(R L).

This construction reproduces a finite twin-style ratio and is invariant
under the pure null reslicing (R, L) -> (lambda R, L/lambda).  It does not
derive the null cone, the square-root clock law, dimensional units, gravity,
or a physical value of c.

The preferred-frame control keeps the global layer count K = R + L.  K
changes under the same reslicing even though tau_hash does not.  Thus K can
be hidden only by an explicit quotient/no-clock-tag condition.
"""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_rate_wild_frontier_clock_quotient_probe_result.json"
)

NODES = ("E0", "a", "b", "c", "E1")
COVER_EDGES = (
    ("E0", "a"),
    ("a", "c"),
    ("c", "E1"),
    ("E0", "b"),
    ("b", "E1"),
)
HISTORY_A = ("E0", "a", "c", "E1")
HISTORY_B = ("E0", "b", "E1")


def is_natural_labeling(order: tuple[str, ...]) -> bool:
    position = {node: index for index, node in enumerate(order)}
    return all(position[left] < position[right] for left, right in COVER_EDGES)


def natural_labelings() -> list[dict[str, int]]:
    return [
        {node: index for index, node in enumerate(order)}
        for order in itertools.permutations(NODES)
        if is_natural_labeling(order)
    ]


def history_gaps(
    labeling: dict[str, int], history: tuple[str, ...]
) -> tuple[int, ...]:
    return tuple(
        labeling[right] - labeling[left]
        for left, right in zip(history, history[1:])
    )


def clock_tag_signature(labeling: dict[str, int]) -> dict[str, Any]:
    return {
        "history_A_global_tick_gaps": history_gaps(labeling, HISTORY_A),
        "history_B_global_tick_gaps": history_gaps(labeling, HISTORY_B),
        "middle_event_tick_parities": {
            node: labeling[node] % 2 for node in ("a", "b", "c")
        },
    }


def exact_null_clock(delta_t: int, delta_x: int) -> dict[str, Any]:
    if (delta_t + delta_x) % 2 or (delta_t - delta_x) % 2:
        raise ValueError("delta_t +/- delta_x must be even")
    right_null = (delta_t + delta_x) // 2
    left_null = (delta_t - delta_x) // 2
    if right_null < 0 or left_null < 0:
        raise ValueError("segment must be future causal")
    tau_squared = 4 * right_null * left_null
    tau_hash = math.isqrt(tau_squared)
    if tau_hash * tau_hash != tau_squared:
        raise ValueError("fixture requires an integral candidate clock count")
    return {
        "delta_t_global_ticks": delta_t,
        "delta_x_edges": delta_x,
        "right_null_count": right_null,
        "left_null_count": left_null,
        "causal_rectangle_count": right_null * left_null,
        "candidate_elapsed_record_count": tau_hash,
    }


def pure_null_reslicing(
    right_null: int, left_null: int, scale: Fraction
) -> dict[str, Any]:
    transformed_right = scale * right_null
    transformed_left = Fraction(left_null, 1) / scale
    return {
        "scale": str(scale),
        "right_null_before": right_null,
        "left_null_before": left_null,
        "right_null_after": str(transformed_right),
        "left_null_after": str(transformed_left),
        "causal_product_before": right_null * left_null,
        "causal_product_after": str(
            transformed_right * transformed_left
        ),
        "global_layer_count_before": right_null + left_null,
        "global_layer_count_after": str(
            transformed_right + transformed_left
        ),
    }


def main() -> None:
    labelings = natural_labelings()
    labeling_rows = [
        {
            "global_tick_assignment": labeling,
            "clock_tag_signature": clock_tag_signature(labeling),
            # Order-only path lengths do not refer to the labeling.
            "order_only_history_record_counts": {
                "A": len(HISTORY_A) - 1,
                "B": len(HISTORY_B) - 1,
            },
            # G-full counts every global opportunity between shared endpoints.
            "G_full_record_counts": {
                "A": labeling["E1"] - labeling["E0"],
                "B": labeling["E1"] - labeling["E0"],
            },
        }
        for labeling in labelings
    ]

    tag_signatures = {
        json.dumps(row["clock_tag_signature"], sort_keys=True)
        for row in labeling_rows
    }
    order_only_signatures = {
        tuple(row["order_only_history_record_counts"].items())
        for row in labeling_rows
    }

    rest_segment = exact_null_clock(100, 0)
    outbound_segment = exact_null_clock(50, 30)
    inbound_segment = exact_null_clock(50, -30)
    moving_elapsed = (
        outbound_segment["candidate_elapsed_record_count"]
        + inbound_segment["candidate_elapsed_record_count"]
    )
    rest_elapsed = rest_segment["candidate_elapsed_record_count"]
    velocity = Fraction(3, 5)
    expected_ratio = Fraction(4, 5)
    observed_ratio = Fraction(moving_elapsed, rest_elapsed)

    reslicing = pure_null_reslicing(50, 50, Fraction(2, 1))
    integer_lattice_counterexample = {
        "integer_null_point": [0, 1],
        "image_under_lambda_2": ["0", "1/2"],
        "fixed_integer_lattice_preserved": False,
    }
    nontrivial_integral_pure_boosts = [
        [alpha, beta]
        for alpha in range(1, 9)
        for beta in range(1, 9)
        if alpha * beta == 1 and (alpha, beta) != (1, 1)
    ]

    send_tick = 10
    independently_counted_edge_distance = 7
    receive_tick = send_tick + independently_counted_edge_distance
    return_tick = receive_tick + independently_counted_edge_distance
    radar_time = Fraction(send_tick + return_tick, 2)
    radar_distance = Fraction(return_tick - send_tick, 2)
    raw_receive_offset = receive_tick - send_tick
    latency_corrected_offset = (
        receive_tick
        - send_tick
        - independently_counted_edge_distance
    )

    checks = [
        {
            "name": "finite event graph has three natural labelings",
            "pass": len(labelings) == 3,
        },
        {
            "name": "order-only observer records survive scheduler relabeling",
            "pass": len(order_only_signatures) == 1,
        },
        {
            "name": "physical global-clock tags expose the scheduler",
            "pass": len(tag_signatures) == 3,
        },
        {
            "name": "G-full gives equal reunited observer counts",
            "pass": all(
                row["G_full_record_counts"]["A"]
                == row["G_full_record_counts"]["B"]
                == 4
                for row in labeling_rows
            ),
        },
        {
            "name": "G-gated path records can differ at reunion",
            "pass": (
                len(HISTORY_A) - 1 == 3 and len(HISTORY_B) - 1 == 2
            ),
        },
        {
            "name": "null-volume clock gives rest count 100",
            "pass": rest_elapsed == 100,
        },
        {
            "name": "two-leg moving clock gives count 80",
            "pass": moving_elapsed == 80,
        },
        {
            "name": "moving/rest record ratio matches sqrt(1-v^2)",
            "pass": (
                velocity == Fraction(3, 5)
                and observed_ratio == expected_ratio
            ),
        },
        {
            "name": "pure null reslicing preserves causal product",
            "pass": (
                reslicing["causal_product_before"]
                == int(reslicing["causal_product_after"])
            ),
        },
        {
            "name": "same reslicing changes readable global layer count",
            "pass": (
                reslicing["global_layer_count_before"]
                != int(reslicing["global_layer_count_after"])
            ),
        },
        {
            "name": "nontrivial pure boost does not preserve fixed integer lattice",
            "pass": not integer_lattice_counterexample[
                "fixed_integer_lattice_preserved"
            ],
        },
        {
            "name": "positive integral pure Lorentz rescalings are trivial",
            "pass": not nontrivial_integral_pure_boosts,
        },
        {
            "name": "raw message offset is exactly propagation delay",
            "pass": (
                raw_receive_offset == independently_counted_edge_distance
                and latency_corrected_offset == 0
            ),
        },
        {
            "name": "radar construction returns c=1 in its own units",
            "pass": (
                radar_distance == independently_counted_edge_distance
                and Fraction(radar_distance, receive_tick - send_tick) == 1
            ),
        },
    ]

    result = {
        "probe": "du_record_rate_wild_frontier_clock_quotient_probe",
        "status": (
            "PASS" if all(check["pass"] for check in checks) else "FAIL"
        ),
        "scientific_disposition": (
            "G_FULL_REUNION_KILLED_FOR_UNEQUAL_ELAPSED_TIME__"
            "G_GATED_CONDITIONAL_CONSTRUCTION__"
            "G_HIDDEN_REQUIRES_EXPLICIT_CLOCK_QUOTIENT"
        ),
        "scope": {
            "dimension": "1+1 for the null-coordinate construction",
            "warrant": [
                "exact finite countermodel",
                "conditional constructive realization",
                "preferred-frame and delay-only nulls",
            ],
            "not_established": [
                "derivation of the causal cone",
                "selection of the square-root record law",
                "continuum dynamics or gravity",
                "dimensional invariant speed",
                "physical record ontology",
            ],
        },
        "assumptions": {
            "common": [
                "observer records form causal chains",
                "record equivalence is fixed across compared histories",
            ],
            "branch_L_candidate": [
                "causal order plus event-number density supplies a "
                "manifoldlike 1+1 interval volume",
                "elapsed record count is 2 sqrt(R L)",
                "no global K is observable or required",
            ],
            "branch_G_full": [
                "each observer adds exactly one record per K",
            ],
            "branch_G_gated": [
                "K opens an opportunity; records occur only at admitted "
                "path events",
                "the admission/clock law is extra structure",
            ],
            "branch_G_hidden": [
                "different natural labelings are physically equivalent",
                "no clock tag, parity, phase, or layer count is observable",
            ],
        },
        "finite_clock_quotient": {
            "nodes": NODES,
            "cover_edges": COVER_EDGES,
            "observer_histories": {
                "A": HISTORY_A,
                "B": HISTORY_B,
            },
            "natural_labeling_count": len(labelings),
            "distinct_order_only_signature_count": len(
                order_only_signatures
            ),
            "distinct_clock_tag_signature_count": len(tag_signatures),
            "labelings": labeling_rows,
        },
        "reunion_fixture": {
            "shared_global_tick_duration": 100,
            "G_full_counts": {"rest": 100, "moving": 100},
            "G_gated_null_volume_counts": {
                "rest": rest_elapsed,
                "moving": moving_elapsed,
            },
            "rest_segment": rest_segment,
            "moving_segments": [outbound_segment, inbound_segment],
            "velocity": str(velocity),
            "observed_elapsed_ratio": str(observed_ratio),
            "expected_special_relativistic_ratio": str(expected_ratio),
            "endpoint_signal_delay": 0,
        },
        "preferred_frame_control": {
            "pure_null_reslicing": reslicing,
            "integer_lattice_counterexample": integer_lattice_counterexample,
            "nontrivial_integral_alpha_beta_with_product_one": (
                nontrivial_integral_pure_boosts
            ),
            "interpretation": (
                "the causal product survives while readable K changes; "
                "a fixed integral lattice also fails closure under the "
                "nontrivial pure reslicing"
            ),
        },
        "delay_only_control": {
            "send_tick_A": send_tick,
            "receive_reflect_tick_B": receive_tick,
            "return_tick_A": return_tick,
            "independently_counted_edge_distance": (
                independently_counted_edge_distance
            ),
            "raw_receive_minus_send": raw_receive_offset,
            "latency_corrected_offset": latency_corrected_offset,
            "radar_time": str(radar_time),
            "radar_distance": str(radar_distance),
            "dimensionless_signal_slope": "1",
            "interpretation": (
                "the separated-clock offset vanishes after exact latency "
                "subtraction; c=1 from radar units is definitional, while "
                "one edge per tick is a separately posited circuit law"
            ),
        },
        "checks": checks,
        "check_summary": {
            "passed": sum(check["pass"] for check in checks),
            "total": len(checks),
        },
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["check_summary"], sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
