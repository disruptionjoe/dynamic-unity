#!/usr/bin/env python3
"""Finite identifiability probe for primitive local and global record clocks.

The probe keeps four model classes separate:

* L: observers carry local record chains with no global synchronization;
* G-full: every observer adds exactly one record at every global tick K;
* G-gated: K opens an opportunity and an additional gate chooses records;
* G-hidden: a linear extension of the causal order is posited but may or may
  not enter any observable transition law.

It tests a deliberately narrow proposition: whether finite local records,
causal/message edges, echo data, and reunion counts identify which class is
fundamental.  Arbitrary G-gating can compile any finite acyclic local-record
trace, while G-full cannot reproduce unequal record counts at reunion.
Whether a hidden scheduler is gauge or hidden physical structure depends on
the full transition law, not on its absence from one observed transcript.

No proper-time metric, Lorentz factor, physical distance, invariant signal
speed, thermodynamic irreversibility, or observer ontology is derived here.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_rate_philosopher_clock_ontology_probe_result.json"
)


def respects_edges(
    order: tuple[str, ...], edges: Iterable[tuple[str, str]]
) -> bool:
    positions = {node: index for index, node in enumerate(order)}
    return all(positions[left] < positions[right] for left, right in edges)


def topological_orders(
    nodes: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> list[tuple[str, ...]]:
    return [
        order
        for order in itertools.permutations(nodes)
        if respects_edges(order, edges)
    ]


def compile_gated_schedule(
    order: tuple[str, ...],
    record_owners: dict[str, tuple[str, ...]],
    observers: tuple[str, ...],
) -> list[dict[str, Any]]:
    """Compile a finite causal trace into global opportunities plus gates."""
    schedule = []
    for global_tick, event in enumerate(order):
        owners = record_owners[event]
        schedule.append(
            {
                "K": global_tick,
                "event": event,
                "opportunity_offered_to": list(observers),
                "record_admitted_for": list(owners),
            }
        )
    return schedule


def local_projection(
    schedule: list[dict[str, Any]], observer: str
) -> list[str]:
    return [
        row["event"]
        for row in schedule
        if observer in row["record_admitted_for"]
    ]


def causal_scheduler_fixture() -> dict[str, Any]:
    nodes = ("E0", "A1", "B1", "E1")
    edges = (
        ("E0", "A1"),
        ("E0", "B1"),
        ("A1", "E1"),
        ("B1", "E1"),
    )
    owners = {
        "E0": ("A", "B"),
        "A1": ("A",),
        "B1": ("B",),
        "E1": ("A", "B"),
    }
    observers = ("A", "B")
    orders = topological_orders(nodes, edges)
    schedules = [
        compile_gated_schedule(order, owners, observers) for order in orders
    ]
    projections = [
        {
            observer: local_projection(schedule, observer)
            for observer in observers
        }
        for schedule in schedules
    ]

    scheduler_insensitive_probability = [0.5 for _ in orders]
    scheduler_sensitive_probability = [
        0.75 if order.index("A1") < order.index("B1") else 0.25
        for order in orders
    ]

    return {
        "causal_nodes": list(nodes),
        "causal_edges": [list(edge) for edge in edges],
        "linear_extensions": [list(order) for order in orders],
        "linear_extension_count": len(orders),
        "compiled_global_schedules": schedules,
        "local_record_projections": projections,
        "all_projections_equal": all(
            projection == projections[0] for projection in projections
        ),
        "scheduler_intervention": {
            "intervention": (
                "Exchange the K-order of spacelike A1 and B1 while preserving "
                "the causal partial order and local record projections."
            ),
            "scheduler_insensitive_next_outcome_probabilities": (
                scheduler_insensitive_probability
            ),
            "scheduler_sensitive_next_outcome_probabilities": (
                scheduler_sensitive_probability
            ),
            "insensitive_difference": max(
                scheduler_insensitive_probability
            )
            - min(scheduler_insensitive_probability),
            "sensitive_difference": max(scheduler_sensitive_probability)
            - min(scheduler_sensitive_probability),
            "reading": (
                "A scheduler is gauge only when all physical observables and "
                "transition probabilities factor through the causal-order "
                "quotient. One unchanged transcript establishes only "
                "nonidentification. A scheduler-sensitive future kernel makes "
                "the hidden order physical and interventionally testable."
            ),
        },
        "general_finite_compiler": (
            "Every finite DAG has a topological ordering. Assign its events "
            "successive K values, offer every observer an opportunity at each "
            "K, and admit exactly the records attached to that event. Thus an "
            "unrestricted G-gated model reproduces every finite L trace."
        ),
    }


def echo_fixture() -> dict[str, Any]:
    n_send = 10
    m_reflect = 17
    n_return = 24
    round_trip = n_return - n_send
    radar_time = (n_send + n_return) / 2.0
    radar_distance = round_trip / 2.0

    synchronization_family = []
    for epsilon in range(-6, 7):
        forward_latency = radar_distance + epsilon
        return_latency = radar_distance - epsilon
        reflection_coordinate_time = n_send + forward_latency
        b_clock_offset = m_reflect - reflection_coordinate_time
        reconstructed_return = (
            reflection_coordinate_time + return_latency
        )
        synchronization_family.append(
            {
                "epsilon": epsilon,
                "forward_latency": forward_latency,
                "return_latency": return_latency,
                "B_offset_relative_to_A_coordinate": b_clock_offset,
                "reflection_A_coordinate_time": (
                    reflection_coordinate_time
                ),
                "reconstructed_A_return": reconstructed_return,
                "observed_local_records": [
                    n_send,
                    m_reflect,
                    n_return,
                ],
            }
        )

    dimensional_calibrations = []
    for length_per_count_time in (0.5, 1.0, 3.0):
        dimensional_calibrations.append(
            {
                "independent_length_per_count_time": length_per_count_time,
                "calibrated_distance": (
                    radar_distance * length_per_count_time
                ),
                "candidate_dimensional_signal_speed": (
                    length_per_count_time
                ),
            }
        )

    return {
        "records": {
            "A_send_n_s": n_send,
            "B_reflect_m_b": m_reflect,
            "A_return_n_r": n_return,
        },
        "defined_from_A_records": {
            "round_trip_latency": round_trip,
            "radar_time": radar_time,
            "radar_distance_in_record_count_time_units": radar_distance,
            "radar_signal_slope_by_definition": 1.0,
        },
        "synchronization_family": synchronization_family,
        "synchronization_family_size_sampled": len(
            synchronization_family
        ),
        "continuous_family": (
            "-7 < epsilon < 7 preserves positive one-way latencies; "
            "d_forward=7+epsilon, d_return=7-epsilon, and B_offset=-epsilon"
        ),
        "round_trip_invariant_across_family": all(
            row["forward_latency"] + row["return_latency"] == round_trip
            for row in synchronization_family
        ),
        "local_records_invariant_across_family": all(
            row["observed_local_records"]
            == [n_send, m_reflect, n_return]
            for row in synchronization_family
        ),
        "delay_only_null": {
            "raw_round_trip": round_trip,
            "modeled_forward_plus_return_delay": round_trip,
            "delay_subtracted_residual": 0.0,
            "reading": (
                "The echo measures round-trip latency. After exact travel-time "
                "subtraction, it supplies no differential elapsed-record "
                "effect."
            ),
        },
        "dimensional_calibration_family": dimensional_calibrations,
        "reading": (
            "The records define radar coordinates under a synchronization "
            "convention. They do not separately identify one-way latency, "
            "B's offset, independent spatial distance, or a dimensional "
            "invariant speed."
        ),
    }


def reunion_fixture() -> dict[str, Any]:
    global_ticks = 20
    target_a = 20
    target_b = 16
    beta = 3.0 / 5.0
    lorentz_gate_target = math.sqrt(1.0 - beta * beta)

    periodic_skips = (5, 10, 15, 20)
    early_skips = (1, 2, 3, 4)
    late_skips = (17, 18, 19, 20)
    gate_patterns = {
        "periodic": periodic_skips,
        "early": early_skips,
        "late": late_skips,
    }

    def admitted_count(skips: tuple[int, ...], through: int) -> int:
        return sum(
            tick not in skips for tick in range(1, through + 1)
        )

    pattern_rows = []
    for name, skips in gate_patterns.items():
        pattern_rows.append(
            {
                "name": name,
                "skipped_K": list(skips),
                "B_records_at_K10": admitted_count(skips, 10),
                "B_records_at_reunion_K20": admitted_count(
                    skips, global_ticks
                ),
            }
        )

    return {
        "shared_endpoints": ["E0", "E1"],
        "signal_delay_at_shared_endpoints": 0,
        "declared_target": {
            "A_records": target_a,
            "B_records": target_b,
            "B_to_A_ratio": target_b / target_a,
            "illustrative_beta": beta,
            "sqrt_one_minus_beta_squared": lorentz_gate_target,
        },
        "branch_L": {
            "local_chain_lengths": {"A": target_a, "B": target_b},
            "status": (
                "compatible but unexplained until local dynamics selects both "
                "chain densities and connects them to a metric"
            ),
        },
        "branch_G_full": {
            "global_ticks": global_ticks,
            "predicted_records": {
                "A": global_ticks,
                "B": global_ticks,
            },
            "matches_target": (
                global_ticks == target_a and global_ticks == target_b
            ),
        },
        "branch_G_gated": {
            "A_gate": "admit every K",
            "B_gate_example": (
                "admit every K except K in {5,10,15,20}"
            ),
            "predicted_records": {"A": target_a, "B": target_b},
            "matches_target": True,
            "gate_mean": target_b / global_ticks,
            "illustrative_Lorentz_factor_was_input_not_derived": (
                lorentz_gate_target
            ),
            "endpoint_equivalent_B_gate_pattern_count": math.comb(20, 4),
            "nonuniform_cadence_control": pattern_rows,
        },
        "delay_only_null": {
            "endpoint_latency": 0,
            "observed_record_difference": target_a - target_b,
            "difference_after_latency_subtraction": target_a - target_b,
            "reading": (
                "Distance-dependent message delay cannot produce an elapsed "
                "record-count difference at shared reunion endpoints."
            ),
        },
    }


def main() -> None:
    scheduler = causal_scheduler_fixture()
    echo = echo_fixture()
    reunion = reunion_fixture()

    checks = [
        {
            "name": "the diamond causal order has two global linear extensions",
            "pass": scheduler["linear_extension_count"] == 2,
        },
        {
            "name": "both global extensions preserve identical local record projections",
            "pass": scheduler["all_projections_equal"],
        },
        {
            "name": "a scheduler-insensitive transition law factors through the causal quotient",
            "pass": scheduler["scheduler_intervention"][
                "insensitive_difference"
            ]
            == 0.0,
        },
        {
            "name": "a scheduler-sensitive transition law exposes the hidden order",
            "pass": scheduler["scheduler_intervention"][
                "sensitive_difference"
            ]
            == 0.5,
        },
        {
            "name": "the echo leaves a synchronization and one-way-latency family",
            "pass": (
                echo["synchronization_family_size_sampled"] == 13
                and echo["round_trip_invariant_across_family"]
                and echo["local_records_invariant_across_family"]
            ),
        },
        {
            "name": "exact echo-delay subtraction leaves no elapsed-clock residual",
            "pass": echo["delay_only_null"]["delay_subtracted_residual"]
            == 0.0,
        },
        {
            "name": "radar c=1 admits multiple dimensional calibrations",
            "pass": len(
                {
                    row["candidate_dimensional_signal_speed"]
                    for row in echo["dimensional_calibration_family"]
                }
            )
            == 3,
        },
        {
            "name": "G-full fails the unequal reunion-count target",
            "pass": not reunion["branch_G_full"]["matches_target"],
        },
        {
            "name": "G-gated can compile the reunion target only with an extra gate",
            "pass": (
                reunion["branch_G_gated"]["matches_target"]
                and reunion["branch_G_gated"]["gate_mean"] == 0.8
            ),
        },
        {
            "name": "endpoint reunion counts underidentify the gated cadence history",
            "pass": (
                reunion["branch_G_gated"][
                    "endpoint_equivalent_B_gate_pattern_count"
                ]
                == 4845
                and len(
                    {
                        row["B_records_at_K10"]
                        for row in reunion["branch_G_gated"][
                            "nonuniform_cadence_control"
                        ]
                    }
                )
                == 3
                and all(
                    row["B_records_at_reunion_K20"] == 16
                    for row in reunion["branch_G_gated"][
                        "nonuniform_cadence_control"
                    ]
                )
            ),
        },
        {
            "name": "reunion delay subtraction leaves the unequal count intact",
            "pass": reunion["delay_only_null"][
                "difference_after_latency_subtraction"
            ]
            == 4,
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    payload = {
        "probe": "du_record_rate_philosopher_clock_ontology_probe",
        "contested_proposition": (
            "Finite local records, causal/message edges, echo data, and "
            "reunion counts can identify whether fundamental succession is "
            "Branch L local or a single Branch G global clock."
        ),
        "definitions_used": {
            "observer": (
                "A causally persistent subsystem represented here only by a "
                "local transition chain, stable record labels, and message "
                "ports; physical realization is assumed, not derived."
            ),
            "record": (
                "A typed stable memory transition in the model. No-retraction "
                "bookkeeping represents irreversibility but does not derive "
                "thermodynamic irreversibility."
            ),
            "record_equivalence": (
                "Equivalence under a shared operational discriminator and "
                "retention protocol; cross-observer equivalence is assumed."
            ),
            "local_order": "Predecessor order on one observer's records.",
            "causal_precedence": (
                "The invariant DAG relation, distinct from any total "
                "scheduler order."
            ),
            "logical_clock_order": (
                "A counter or topological extension consistent with causal "
                "precedence; it is not metric time."
            ),
            "branch_L_cadence_denominator": (
                "One predecessor-indexed local update opportunity. This "
                "dimensionless rule imports neither global nor proper time "
                "and supplies no physical duration by itself."
            ),
            "branch_G_cadence_denominator": (
                "One primitive global update interval delta_K, declared as a "
                "microscopic coordinate-time unit."
            ),
            "message": (
                "A directed payload-preserving edge from a send record to a "
                "receipt/reflection record; it does not by itself define "
                "distance."
            ),
            "global_clock_status_options": [
                "observable",
                "hidden but physical",
                "gauge after an invariance quotient",
                "operationally nonidentified by the present data",
            ],
        },
        "causal_scheduler_fixture": scheduler,
        "echo_fixture": echo,
        "reunion_fixture": reunion,
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "CONTESTED PROPOSITION NARROWED/OVERTURNED BY MODEL CLASS. "
            "Unequal reunion counts exactly reject G-full and reject a "
            "delay-only explanation. They do not identify L against "
            "unrestricted G-gated or G-hidden: every finite causal record DAG "
            "admits a global topological scheduler and a gate compilation. "
            "A hidden K is gauge only if the complete dynamics and all "
            "observables are invariant under rescheduling; otherwise it is "
            "merely nonidentified and a scheduler-sensitive intervention can "
            "expose it. G-gated becomes explanatory only when an independently "
            "constrained gate law predicts multiple held-out observables."
        ),
        "not_derived": [
            "observer or detector ontology",
            "thermodynamic irreversibility",
            "proper time or coordinate time from record count",
            "spatial distance from latency",
            "Lorentz transformations or an invariant dimensional speed",
            "the Lorentz gating factor",
            "a gauge quotient for hidden global order",
            "a dynamical law selecting Branch L or Branch G",
        ],
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("PHILOSOPHER — PRIMITIVE RECORD-CLOCK IDENTIFIABILITY")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['verdict']}")
    if passed != len(checks):
        failures = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failures}")


if __name__ == "__main__":
    main()
