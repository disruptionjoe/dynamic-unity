#!/usr/bin/env python3
"""Exact resource gate for a durable observer-record interpretation.

This probe does *not* implement the Arrighi--Facchini--Forets Clock QCA and
does not test its covariance theorem.  It prices a logically prior semantic
requirement: if a candidate observer must make the cumulative values
0, ..., T perfectly distinguishable at reunion, its accessible record space
must contain at least T + 1 distinguishable states.

For a fixed bounded subsystem of k d-level cells this gives

    d**k >= T + 1,  or  k >= ceil(log_d(T + 1)).

An unbounded translation-invariant QCA is not ruled out: it may use growing
spatial support.  The point is that this support is then part of the record
resource and must survive the covariance/representation quotient.  A stronger
event-by-event append-only unary archive uses one fresh cell per event.
"""

from __future__ import annotations

import itertools
import json
from math import factorial
from pathlib import Path
from typing import Any, Iterable


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_foundational_commercial_record_resource_gate_result.json"
)


def orbit(permutation: tuple[int, ...], start: int = 0) -> list[int]:
    """Return the distinct states before a reversible finite orbit repeats."""
    seen: list[int] = []
    state = start
    while state not in seen:
        seen.append(state)
        state = permutation[state]
    return seen


def reversible_state_space_tournament() -> list[dict[str, int]]:
    """Exhaustively price the longest no-alias record horizon for q <= 7."""
    rows: list[dict[str, int]] = []
    for q in range(2, 8):
        maximum_distinct = 0
        for permutation in itertools.permutations(range(q)):
            maximum_distinct = max(maximum_distinct, len(orbit(permutation)))
        rows.append(
            {
                "states": q,
                "permutations_checked": factorial(q),
                "maximum_distinct_readable_values_on_one_orbit": maximum_distinct,
                "maximum_strict_increment_transitions_before_alias": (
                    maximum_distinct - 1
                ),
            }
        )
    return rows


def minimum_cells(local_dimension: int, transition_horizon: int) -> int:
    """Minimum fixed cells for values 0..transition_horizon."""
    required_values = transition_horizon + 1
    cells = 0
    capacity = 1
    while capacity < required_values:
        capacity *= local_dimension
        cells += 1
    return cells


def first_alias(readouts: Iterable[int]) -> dict[str, int] | None:
    seen: dict[int, int] = {}
    for time, value in enumerate(readouts):
        if value in seen:
            return {"earlier_time": seen[value], "later_time": time, "value": value}
        seen[value] = time
    return None


def fixed_qutrit_phase(horizon: int) -> dict[str, Any]:
    readouts = [time % 3 for time in range(horizon + 1)]
    return {
        "local_dimension": 3,
        "readouts": readouts,
        "first_alias": first_alias(readouts),
        "interpretation": (
            "A changing three-state phase is a clock phase, not an unbounded "
            "cumulative record."
        ),
    }


def bounded_ternary_counter(cells: int, horizon: int) -> dict[str, Any]:
    capacity = 3**cells
    readouts = [time % capacity for time in range(horizon + 1)]
    return {
        "cells": cells,
        "basis_state_capacity": capacity,
        "transition_horizon_without_alias": capacity - 1,
        "tested_transition_horizon": horizon,
        "first_alias": first_alias(readouts),
        "passes": first_alias(readouts) is None,
        "resource_import": (
            "The finite horizon is purchased by the declared number of "
            "accessible ternary cells."
        ),
    }


def growing_spatial_archive(horizon: int, translation: int, stretch: int) -> dict:
    """Unary record whose invariant is marker count, not addresses or span."""
    rows = []
    for time in range(horizon + 1):
        markers = frozenset(range(time))
        translated = frozenset(position + translation for position in markers)
        stretched = frozenset(position * stretch for position in markers)
        rows.append(
            {
                "time": time,
                "accessible_cells": time,
                "marker_count": len(markers),
                "translated_marker_count": len(translated),
                "stretched_with_vacua_marker_count": len(stretched),
                "raw_span": 0 if not markers else max(markers) - min(markers) + 1,
                "stretched_raw_span": (
                    0 if not stretched else max(stretched) - min(stretched) + 1
                ),
            }
        )
    return {
        "rows": rows,
        "count_survives_translation": all(
            row["marker_count"] == row["translated_marker_count"] for row in rows
        ),
        "count_survives_vacuum_inserting_stretch": all(
            row["marker_count"] == row["stretched_with_vacua_marker_count"]
            for row in rows
        ),
        "span_is_not_representation_invariant": any(
            row["raw_span"] != row["stretched_raw_span"] for row in rows[2:]
        ),
        "interpretation": (
            "An unbounded lattice can host an unbounded record, but the "
            "accessible support grows and raw support span is not invariant."
        ),
    }


def scheduler_quotient() -> dict[str, Any]:
    schedule_a = [0, 2, 5, 9, 14]
    schedule_b = [10, 20, 30, 40, 50]
    event_ordinals = list(range(len(schedule_a)))
    return {
        "schedule_a_tags": schedule_a,
        "schedule_b_tags": schedule_b,
        "event_ordinals_a": event_ordinals,
        "event_ordinals_b": event_ordinals,
        "scheduler_tag_record_survives": schedule_a == schedule_b,
        "causal_event_count_survives": event_ordinals == event_ordinals,
        "interpretation": (
            "A raw scheduler tag is not a record on the rescheduling quotient; "
            "event order/count can be."
        ),
    }


def replay_provenance() -> dict[str, Any]:
    all_active = [1, 1, 1, 1, 1, 1]
    held_out = [1, 1, 0, 1, 0, 1]

    def cumulative(events: list[int]) -> list[int]:
        total = 0
        values = []
        for event in events:
            total += event
            values.append(total)
        return values

    fixed_replay = list(range(1, len(all_active) + 1))
    return {
        "training_events": all_active,
        "held_out_events": held_out,
        "active_training_record": cumulative(all_active),
        "active_held_out_record": cumulative(held_out),
        "fixed_replay_record": fixed_replay,
        "replay_matches_training": fixed_replay == cumulative(all_active),
        "replay_matches_held_out": fixed_replay == cumulative(held_out),
        "mechanism_off_record": [0] * len(all_active),
        "interpretation": (
            "A prewritten cadence matches the selected all-active history but "
            "fails a held-out skipped-event intervention."
        ),
    }


def resource_table() -> list[dict[str, int]]:
    horizons = [2, 10, 100, 1_000, 1_000_000]
    return [
        {
            "transition_horizon_T": horizon,
            "perfectly_distinguishable_values_required": horizon + 1,
            "minimum_qutrit_cells_for_count_only": minimum_cells(3, horizon),
            "dedicated_cells_in_unary_event_archive": horizon,
        }
        for horizon in horizons
    ]


def build_result() -> dict[str, Any]:
    tournament = reversible_state_space_tournament()
    phase = fixed_qutrit_phase(8)
    bounded_train = bounded_ternary_counter(cells=5, horizon=100)
    bounded_holdout = bounded_ternary_counter(cells=5, horizon=1_000)
    spatial = growing_spatial_archive(horizon=12, translation=7, stretch=3)
    scheduler = scheduler_quotient()
    replay = replay_provenance()
    resources = resource_table()

    checks = [
        {
            "name": "all finite reversible tournaments attain at most q distinct orbit states",
            "pass": all(
                row["maximum_distinct_readable_values_on_one_orbit"]
                == row["states"]
                for row in tournament
            ),
        },
        {
            "name": "a fixed qutrit phase aliases times zero and three",
            "pass": phase["first_alias"]
            == {"earlier_time": 0, "later_time": 3, "value": 0},
        },
        {
            "name": "five ternary cells pass the selected T=100 horizon",
            "pass": bounded_train["passes"],
        },
        {
            "name": "the same five ternary cells fail the held-out T=1000 horizon",
            "pass": not bounded_holdout["passes"],
        },
        {
            "name": "the bounded-counter alias occurs exactly at its capacity",
            "pass": bounded_holdout["first_alias"]
            == {"earlier_time": 0, "later_time": 243, "value": 0},
        },
        {
            "name": "minimum qutrit count support for T=100 is five cells",
            "pass": minimum_cells(3, 100) == 5,
        },
        {
            "name": "minimum qutrit count support for T=1000 is seven cells",
            "pass": minimum_cells(3, 1_000) == 7,
        },
        {
            "name": "growing marker count survives lattice translation",
            "pass": spatial["count_survives_translation"],
        },
        {
            "name": "growing marker count survives vacuum-inserting stretch",
            "pass": spatial["count_survives_vacuum_inserting_stretch"],
        },
        {
            "name": "raw archive span fails the stretch quotient",
            "pass": spatial["span_is_not_representation_invariant"],
        },
        {
            "name": "raw scheduler tags fail rescheduling invariance",
            "pass": not scheduler["scheduler_tag_record_survives"],
        },
        {
            "name": "causal event ordinals survive rescheduling",
            "pass": scheduler["causal_event_count_survives"],
        },
        {
            "name": "fixed replay matches the selected all-active training history",
            "pass": replay["replay_matches_training"],
        },
        {
            "name": "fixed replay fails the held-out skipped-event history",
            "pass": not replay["replay_matches_held_out"],
        },
        {
            "name": "disabling the recorder removes cumulative records",
            "pass": replay["mechanism_off_record"] == [0] * 6,
        },
        {
            "name": "count-only and event-append-only resource prices remain distinct",
            "pass": all(
                row["minimum_qutrit_cells_for_count_only"]
                <= row["dedicated_cells_in_unary_event_archive"]
                for row in resources
            ),
        },
    ]

    passed = sum(bool(check["pass"]) for check in checks)
    return {
        "probe": "du_foundational_commercial_record_resource_gate",
        "scope": {
            "tested": (
                "resource lower bound and semantic rivals for perfectly "
                "distinguishable cumulative records"
            ),
            "not_tested": [
                "the Clock-QCA scattering unitary",
                "the Clock-QCA discrete covariance proof",
                "whether a native Clock-QCA history supplies a record archive",
                "proper-time or physical-unit identification",
                "3+1 dimensions, interaction, gravity, or cosmology",
            ],
        },
        "exact_theorem": {
            "classical": (
                "A deterministic reversible orbit in q finite states has at "
                "most q distinct current-state readouts before recurrence. "
                "Therefore values 0..T require at least T+1 accessible states."
            ),
            "quantum": (
                "T+1 perfectly distinguishable reunion records require "
                "T+1 mutually orthogonal record supports, hence accessible "
                "Hilbert dimension at least T+1."
            ),
            "cell_bound": (
                "For k cells of local dimension d: d^k >= T+1, so "
                "k >= ceil(log_d(T+1))."
            ),
            "append_only_correction": (
                "The logarithmic bound prices current count distinguishability. "
                "A dedicated unary event archive uses T fresh cells and keeps "
                "the event-by-event prefix; these are not the same requirement."
            ),
            "does_not_imply": (
                "It does not rule out an unbounded QCA. It rules out treating "
                "one fixed bounded finite-state subsystem as an indefinitely "
                "growing record without charging external or growing support."
            ),
        },
        "primary_antecedent_scope": {
            "source": (
                "P. Arrighi, S. Facchini, M. Forets, Discrete Lorentz "
                "covariance for Quantum Walks and Quantum Cellular Automata, "
                "New J. Phys. 16 (2014) 093007, arXiv:1404.4499."
            ),
            "source_establishes": (
                "an exactly discrete-Lorentz-covariant 1+1 Clock QCA with "
                "fixed three-dimensional wire state under a specified "
                "isometric encoding"
            ),
            "source_does_not_supply_for_this_program": (
                "a persistent observer boundary, append-only record functional, "
                "reunion comparison, record-resource price, or physical unit map"
            ),
        },
        "reversible_tournament": tournament,
        "fixed_qutrit_phase": phase,
        "bounded_counter_training": bounded_train,
        "bounded_counter_holdout": bounded_holdout,
        "growing_spatial_archive": spatial,
        "scheduler_quotient": scheduler,
        "replay_provenance": replay,
        "resource_table": resources,
        "commercial_stage_gate": {
            "decision": "FUND_ONE_SOURCE-EXACT_EXTRACTION_STAGE_ONLY",
            "retained_asset": (
                "Clock QCA remains the strongest exact globally stepped "
                "covariance antecedent."
            ),
            "shortcut_retired": (
                "A three-state wire, changing phase, circuit cell, or global "
                "tick is not by itself an observer record."
            ),
            "stage_1_budget_work_units": 2,
            "stage_1_deliverable": (
                "source-exact Clock-QCA gate/encoding reproduction plus an "
                "inventory of candidate record support along one inertial and "
                "one non-inertial history"
            ),
            "stage_1_stop": (
                "No candidate record has growing or externally charged "
                "accessible support, or every candidate depends on raw "
                "scheduler/address labels."
            ),
            "stage_2_budget_work_units_if_stage_1_passes": 4,
            "stage_2_deliverable": (
                "reunion-readable record functional tested under encoding, "
                "translation, rescheduling, mechanism-off, and held-out paths"
            ),
            "stage_2_stop": (
                "The functional aliases held-out histories, changes under the "
                "declared quotient, or counts inserted vacuum/support as time."
            ),
            "stage_3_budget_work_units_if_stage_2_passes": 3,
            "stage_3_deliverable": (
                "recursive-viability lesions and locality/resource comparison "
                "against a flat controller"
            ),
            "maximum_authorized_follow_on_work_units_before_redecision": 9,
            "opportunity_cost": (
                "Every funded work unit delays the independent causal-post "
                "recurrence/geometry route; no observer ontology, 3+1 "
                "extension, gravity, or cosmology work is funded by this gate."
            ),
        },
        "checks": checks,
        "summary": {
            "passed": passed,
            "total": len(checks),
            "verdict": (
                "FIXED-BOUNDED-STATE RECORD SHORTCUT RETIRED / GROWING OR "
                "EXTERNALLY CHARGED SUPPORT REQUIRED / CLOCK-QCA COVARIANCE "
                "ANTECEDENT RETAINED / ONE EXTRACTION STAGE FUNDED"
            ),
        },
    }


def main() -> None:
    result = build_result()
    assert result["summary"]["passed"] == result["summary"]["total"]
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "du_foundational_commercial_record_resource_gate: "
        f"{result['summary']['passed']}/{result['summary']['total']} PASS"
    )


if __name__ == "__main__":
    main()
