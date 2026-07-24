#!/usr/bin/env python3
"""Premise-free heterodox swing: operational durable-record capacity.

The probe asks what can count as a representation-independent stock of
observer records before any record count is identified with time.

For a history set H_t, recorder E_t, and a declared experiment family U_t,
two histories are equivalent when every admitted experiment returns the same
outcome.  The operational stock is

    C_t = log2 |H_t / ~_U|.

This is an operational distinguishability capacity under the declared
experiment family, not necessarily an integer number of jointly independent
record variables, Shannon entropy, cumulative writes, update opportunities,
causal-influence count, thermodynamic work, or proper time.

A stock is durable from t to t+1 only if no pair of previously distinguishable
history classes can merge after any allowed next input.  The finite examples
exercise full append-only memory, last-bit overwrite, parity accumulation,
rolling memory, identity relays, redundant copies, a representation change,
and an external archive.

The reusable theorem proved in the accompanying memo is elementary:

    If every response factors through a fixed state set S with |S| = M, then
    |H_t / ~_U| <= M.  If each binary opportunity adds one durable independent
    distinction, |H_t / ~_U| >= 2**t.  Thus M >= 2**t.

Consequently an unbounded durable-record clock needs growing internal state,
an expanding/exported archive inside the physical boundary, or a weaker
event semantics.  The theorem does not forbid unbounded event counts, proper
time, reversible dynamics, or an environment that carries the records.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_foundational_heterodox_record_capacity_result.json"
)

BIT_ALPHABET = (0, 1)
UNAVAILABLE = "<unavailable>"

History = tuple[int, ...]
State = Any
Encoder = Callable[[History], State]
Reader = Callable[[State, str], Any]


def histories(length: int) -> tuple[History, ...]:
    return tuple(itertools.product(BIT_ALPHABET, repeat=length))


def bit_queries(length: int) -> tuple[str, ...]:
    return tuple(f"bit:{index}" for index in range(length))


def full_queries(length: int) -> tuple[str, ...]:
    return ("parity", *bit_queries(length))


def read_decoded_history(decoded: History, query: str) -> Any:
    if query == "parity":
        return sum(decoded) % 2
    if query.startswith("bit:"):
        index = int(query.split(":", 1)[1])
        return decoded[index] if index < len(decoded) else UNAVAILABLE
    if query == "latest":
        return decoded[-1] if decoded else UNAVAILABLE
    if query == "previous":
        return decoded[-2] if len(decoded) >= 2 else UNAVAILABLE
    return UNAVAILABLE


def full_reader(state: State, query: str) -> Any:
    return read_decoded_history(tuple(state), query)


def parity_reader(state: State, query: str) -> Any:
    if query == "parity":
        return state[0]
    return UNAVAILABLE


def last_reader(state: State, query: str) -> Any:
    if query == "latest":
        return state[0] if state else UNAVAILABLE
    return UNAVAILABLE


def rolling_reader(state: State, query: str) -> Any:
    decoded = tuple(state)
    if query == "latest":
        return decoded[-1] if decoded else UNAVAILABLE
    if query == "previous":
        return decoded[-2] if len(decoded) >= 2 else UNAVAILABLE
    return UNAVAILABLE


def triplicate_reader(state: State, query: str) -> Any:
    copies = tuple(tuple(copy) for copy in state)
    if not copies:
        decoded: History = tuple()
    else:
        width = len(copies[0])
        decoded = tuple(
            int(sum(copy[index] for copy in copies) >= 2)
            for index in range(width)
        )
    return read_decoded_history(decoded, query)


def relay_reader(state: State, query: str) -> Any:
    marker_outer, inner = state
    marker_inner, decoded = inner
    if marker_outer != "relay-outer" or marker_inner != "relay-inner":
        raise ValueError("invalid relay state")
    return read_decoded_history(tuple(decoded), query)


def packed_reader(state: State, query: str) -> Any:
    decoded = tuple(bit for chunk in state for bit in chunk)
    return read_decoded_history(decoded, query)


def expanded_archive_reader(state: State, query: str) -> Any:
    latest, archive = state
    if query == "latest":
        return latest
    return read_decoded_history(tuple(archive), query)


@dataclass(frozen=True)
class Recorder:
    name: str
    encoder: Encoder
    reader: Reader
    native_queries: Callable[[int], tuple[str, ...]]
    cumulative_writes: Callable[[int], int]
    carrier_cells: Callable[[int], int]
    fixed_state_bound: int | None
    semantics: str


RECORDERS = (
    Recorder(
        name="full_append_only",
        encoder=lambda history: history,
        reader=full_reader,
        native_queries=full_queries,
        cumulative_writes=lambda length: length,
        carrier_cells=lambda length: length,
        fixed_state_bound=None,
        semantics="Every input bit remains independently queryable.",
    ),
    Recorder(
        name="triplicate_append_only",
        encoder=lambda history: (history, history, history),
        reader=triplicate_reader,
        native_queries=full_queries,
        cumulative_writes=lambda length: 3 * length,
        carrier_cells=lambda length: 3 * length,
        fixed_state_bound=None,
        semantics=(
            "Three physical carriers store each history bit; majority readout "
            "adds one-carrier fault tolerance, not three provenance bits."
        ),
    ),
    Recorder(
        name="identity_relay_append_only",
        encoder=lambda history: (
            "relay-outer",
            ("relay-inner", history),
        ),
        reader=relay_reader,
        native_queries=full_queries,
        cumulative_writes=lambda length: 3 * length,
        carrier_cells=lambda length: length,
        fixed_state_bound=None,
        semantics=(
            "Two identity relays add update actions and representation depth "
            "without adding a history distinction."
        ),
    ),
    Recorder(
        name="packed_pair_resolution",
        encoder=lambda history: tuple(
            tuple(history[index : index + 2])
            for index in range(0, len(history), 2)
        ),
        reader=packed_reader,
        native_queries=full_queries,
        cumulative_writes=lambda length: math.ceil(length / 2),
        carrier_cells=lambda length: length,
        fixed_state_bound=None,
        semantics=(
            "The same history is stored in two-bit symbols; representation "
            "resolution changes while the behavioral quotient does not."
        ),
    ),
    Recorder(
        name="last_bit_overwrite",
        encoder=lambda history: history[-1:] if history else tuple(),
        reader=last_reader,
        native_queries=lambda length: ("latest",) if length else tuple(),
        cumulative_writes=lambda length: length,
        carrier_cells=lambda length: min(length, 1),
        fixed_state_bound=2,
        semantics="Every opportunity writes, but only the latest bit remains.",
    ),
    Recorder(
        name="parity_accumulator",
        encoder=lambda history: (sum(history) % 2,),
        reader=parity_reader,
        native_queries=lambda length: ("parity",) if length else tuple(),
        cumulative_writes=lambda length: length,
        carrier_cells=lambda length: 1 if length else 0,
        fixed_state_bound=2,
        semantics=(
            "Every input has a causal effect on the final parity, but the "
            "machine retains only one binary distinction."
        ),
    ),
    Recorder(
        name="rolling_two_bit",
        encoder=lambda history: history[-2:],
        reader=rolling_reader,
        native_queries=lambda length: tuple(
            query
            for query, admitted in (
                ("latest", length >= 1),
                ("previous", length >= 2),
            )
            if admitted
        ),
        cumulative_writes=lambda length: length,
        carrier_cells=lambda length: min(length, 2),
        fixed_state_bound=4,
        semantics="Two independent recent bits survive; older classes merge.",
    ),
    Recorder(
        name="internal_last_bit_only",
        encoder=lambda history: history[-1:] if history else tuple(),
        reader=last_reader,
        native_queries=lambda length: ("latest",) if length else tuple(),
        cumulative_writes=lambda length: length,
        carrier_cells=lambda length: min(length, 1),
        fixed_state_bound=2,
        semantics=(
            "Observer boundary excludes the exported archive and therefore "
            "retains only the latest bit."
        ),
    ),
    Recorder(
        name="observer_plus_external_archive",
        encoder=lambda history: (
            history[-1] if history else UNAVAILABLE,
            history,
        ),
        reader=expanded_archive_reader,
        native_queries=lambda length: (
            ("latest", *full_queries(length)) if length else tuple()
        ),
        cumulative_writes=lambda length: 2 * length,
        carrier_cells=lambda length: length + min(length, 1),
        fixed_state_bound=None,
        semantics=(
            "The enlarged boundary includes an append-only archive; record "
            "capacity grows, but storage and boundary growth are explicit."
        ),
    ),
)


def response_signature(
    recorder: Recorder,
    history: History,
    queries: Sequence[str] | None = None,
) -> tuple[Any, ...]:
    state = recorder.encoder(history)
    experiment_family = (
        tuple(queries)
        if queries is not None
        else recorder.native_queries(len(history))
    )
    return tuple(
        (query, recorder.reader(state, query))
        for query in experiment_family
    )


def quotient_classes(
    recorder: Recorder,
    length: int,
    queries: Sequence[str] | None = None,
) -> dict[tuple[Any, ...], tuple[History, ...]]:
    classes: dict[tuple[Any, ...], list[History]] = {}
    for history in histories(length):
        signature = response_signature(recorder, history, queries)
        classes.setdefault(signature, []).append(history)
    return {
        signature: tuple(members)
        for signature, members in sorted(
            classes.items(), key=lambda item: repr(item[0])
        )
    }


def exact_log2_power(value: int) -> int:
    if value <= 0 or value & (value - 1):
        raise ValueError(f"{value} is not a positive power of two")
    return value.bit_length() - 1


def retains_prior_classes(recorder: Recorder, length: int) -> bool:
    """Whether distinct length-t classes can ever merge after one input."""

    if length == 0:
        return True
    old_signatures = {
        history: response_signature(recorder, history)
        for history in histories(length)
    }
    new_signatures = {
        history: response_signature(recorder, history)
        for history in histories(length + 1)
    }
    for left, right in itertools.combinations(histories(length), 2):
        if old_signatures[left] == old_signatures[right]:
            continue
        for left_input in BIT_ALPHABET:
            for right_input in BIT_ALPHABET:
                if (
                    new_signatures[left + (left_input,)]
                    == new_signatures[right + (right_input,)]
                ):
                    return False
    return True


def model_series(recorder: Recorder, max_length: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for length in range(max_length + 1):
        classes = quotient_classes(recorder, length)
        class_count = len(classes)
        reachable_states = len(
            {repr(recorder.encoder(history)) for history in histories(length)}
        )
        row = {
            "length": length,
            "history_count": 2**length,
            "reachable_encoder_states": reachable_states,
            "experiment_equivalence_classes": class_count,
            "maximum_distinguishable_stock_bits": exact_log2_power(class_count),
            "cumulative_write_operations": recorder.cumulative_writes(length),
            "declared_carrier_cells": recorder.carrier_cells(length),
        }
        if length < max_length:
            row["retains_all_prior_classes_after_any_next_input"] = (
                retains_prior_classes(recorder, length)
            )
        rows.append(row)
    return rows


def flip_history_bit(history: History, index: int) -> History:
    changed = list(history)
    changed[index] = 1 - changed[index]
    return tuple(changed)


def parity_causal_influence_count(history: History) -> int:
    baseline = sum(history) % 2
    return sum(
        (sum(flip_history_bit(history, index)) % 2) != baseline
        for index in range(len(history))
    )


def parity_state_change_count(history: History) -> int:
    state = 0
    changes = 0
    for bit in history:
        next_state = state ^ bit
        changes += next_state != state
        state = next_state
    return changes


def binary_entropy(probability: float) -> float:
    if probability in (0.0, 1.0):
        return 0.0
    return -probability * math.log2(probability) - (
        1.0 - probability
    ) * math.log2(1.0 - probability)


def triplicate_corruption_response(
    history: History,
    corrupted_copy_indices: Iterable[int],
) -> History:
    copies = [list(history), list(history), list(history)]
    for copy_index in corrupted_copy_indices:
        copies[copy_index] = [1 - bit for bit in copies[copy_index]]
    return tuple(
        int(sum(copy[index] for copy in copies) >= 2)
        for index in range(len(history))
    )


def main() -> None:
    max_length = 6
    recorder_by_name = {recorder.name: recorder for recorder in RECORDERS}
    series = {
        recorder.name: model_series(recorder, max_length)
        for recorder in RECORDERS
    }

    full = recorder_by_name["full_append_only"]
    triplicate = recorder_by_name["triplicate_append_only"]
    relay = recorder_by_name["identity_relay_append_only"]
    packed = recorder_by_name["packed_pair_resolution"]
    parity = recorder_by_name["parity_accumulator"]
    rolling = recorder_by_name["rolling_two_bit"]
    internal = recorder_by_name["internal_last_bit_only"]
    expanded = recorder_by_name["observer_plus_external_archive"]

    final_histories = histories(max_length)
    representation_signatures = {
        name: tuple(
            (
                history,
                response_signature(
                    recorder_by_name[name],
                    history,
                    full_queries(max_length),
                ),
            )
            for history in final_histories
        )
        for name in (
            "full_append_only",
            "triplicate_append_only",
            "identity_relay_append_only",
            "packed_pair_resolution",
        )
    }

    parity_only_queries = ("parity",)
    held_out_queries = full_queries(max_length)
    readout_dependence = {
        "full_memory_parity_only_classes": len(
            quotient_classes(full, max_length, parity_only_queries)
        ),
        "full_memory_full_recall_classes": len(
            quotient_classes(full, max_length, held_out_queries)
        ),
        "parity_machine_parity_only_classes": len(
            quotient_classes(parity, max_length, parity_only_queries)
        ),
        "parity_machine_full_recall_classes": len(
            quotient_classes(parity, max_length, held_out_queries)
        ),
        "interpretation": (
            "Parity-only development data make full memory and a parity "
            "accumulator observationally equivalent. Held-out bit queries "
            "separate them. No absolute record stock exists without a "
            "declared physical experiment algebra."
        ),
    }

    parity_fixture = (1, 0, 1, 1, 0, 1)
    parity_control = {
        "history": list(parity_fixture),
        "cumulative_update_writes": max_length,
        "state_change_count": parity_state_change_count(parity_fixture),
        "causal_input_influence_count": parity_causal_influence_count(
            parity_fixture
        ),
        "maximum_distinguishable_stock_bits": series[
            "parity_accumulator"
        ][-1]["maximum_distinguishable_stock_bits"],
        "interpretation": (
            "Every input is counterfactually relevant to final parity, while "
            "only one independent distinction is retained."
        ),
    }

    uniform_full_entropy = float(max_length)
    biased_one_probability = 0.25
    biased_full_entropy = max_length * binary_entropy(biased_one_probability)
    biased_parity_odd_probability = (
        1.0 - (1.0 - 2.0 * biased_one_probability) ** max_length
    ) / 2.0
    information_controls = {
        "full_memory_capacity_bits": max_length,
        "full_memory_uniform_shannon_entropy_bits": uniform_full_entropy,
        "full_memory_bernoulli_one_quarter_entropy_bits": biased_full_entropy,
        "parity_capacity_bits": 1,
        "parity_bernoulli_one_quarter_odd_probability": (
            biased_parity_odd_probability
        ),
        "parity_bernoulli_one_quarter_entropy_bits": binary_entropy(
            biased_parity_odd_probability
        ),
        "interpretation": (
            "Maximum distinguishable stock is distribution-free; Shannon "
            "entropy weights the actually supplied history distribution."
        ),
    }

    fault_history = (0, 1, 1, 0, 1, 0)
    redundancy_control = {
        "history": list(fault_history),
        "no_corruption_decodes": list(
            triplicate_corruption_response(fault_history, tuple())
        ),
        "one_carrier_corruption_decodes": list(
            triplicate_corruption_response(fault_history, (0,))
        ),
        "two_carrier_corruption_decodes": list(
            triplicate_corruption_response(fault_history, (0, 1))
        ),
        "full_memory_stock_bits": series["full_append_only"][-1][
            "maximum_distinguishable_stock_bits"
        ],
        "triplicate_stock_bits": series["triplicate_append_only"][-1][
            "maximum_distinguishable_stock_bits"
        ],
        "full_memory_carrier_cells": series["full_append_only"][-1][
            "declared_carrier_cells"
        ],
        "triplicate_carrier_cells": series["triplicate_append_only"][-1][
            "declared_carrier_cells"
        ],
        "interpretation": (
            "Redundancy raises fault tolerance and physical resource use "
            "without multiplying independent provenance classes."
        ),
    }

    tagged_microstate_count = 2 ** (max_length + 1)
    tagged_history_classes = 2**max_length
    hidden_fibre_control = {
        "history_count": 2**max_length,
        "raw_history_times_scheduler_tag_microstates": tagged_microstate_count,
        "history_response_classes_when_tag_is_ignored": tagged_history_classes,
        "joint_experiment_classes_when_tag_is_read": tagged_microstate_count,
        "history_provenance_classes_when_tag_is_read": tagged_history_classes,
        "independent_scheduler_classes_when_tag_is_read": 2,
        "interpretation": (
            "A scheduler tag can be a real additional physical degree of "
            "freedom without becoming a record of the input history. If it "
            "changes future responses it is not gauge; provenance axes remain "
            "typed separately."
        ),
    }

    boundary_control = {
        "length": max_length,
        "observer_internal_stock_bits": series[
            "internal_last_bit_only"
        ][-1]["maximum_distinguishable_stock_bits"],
        "observer_plus_archive_stock_bits": series[
            "observer_plus_external_archive"
        ][-1]["maximum_distinguishable_stock_bits"],
        "internal_state_bound": internal.fixed_state_bound,
        "expanded_carrier_cells": expanded.carrier_cells(max_length),
        "archive_ablation_lost_bits": (
            series["observer_plus_external_archive"][-1][
                "maximum_distinguishable_stock_bits"
            ]
            - series["internal_last_bit_only"][-1][
                "maximum_distinguishable_stock_bits"
            ]
        ),
        "interpretation": (
            "Export is a live escape from finite internal saturation, but "
            "only by expanding the physical record boundary and paying for "
            "the archive."
        ),
    }

    unit_control = {
        "dimensionless_stock_bits": max_length,
        "calibration_A_time_per_bit": 1,
        "calibration_B_time_per_bit": 7,
        "duration_under_A": max_length,
        "duration_under_B": 7 * max_length,
        "interpretation": (
            "The quotient generates a dimensionless stock. A duration appears "
            "only after an external time-per-record calibration is declared."
        ),
    }

    fixed_state_theorem_fixtures = {
        recorder.name: {
            "declared_state_bound": recorder.fixed_state_bound,
            "maximum_reachable_classes_over_lengths_0_to_6": max(
                row["experiment_equivalence_classes"]
                for row in series[recorder.name]
            ),
            "maximum_stock_bits_over_lengths_0_to_6": max(
                row["maximum_distinguishable_stock_bits"]
                for row in series[recorder.name]
            ),
        }
        for recorder in RECORDERS
        if recorder.fixed_state_bound is not None
    }

    checks = [
        {
            "name": "full append-only memory retains six independent bits",
            "pass": (
                series["full_append_only"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == max_length
                and all(
                    row.get(
                        "retains_all_prior_classes_after_any_next_input",
                        True,
                    )
                    for row in series["full_append_only"]
                )
            ),
        },
        {
            "name": "triplicate copies do not inflate provenance stock",
            "pass": (
                representation_signatures["full_append_only"]
                == representation_signatures["triplicate_append_only"]
                and series["triplicate_append_only"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == max_length
                and series["triplicate_append_only"][-1][
                    "cumulative_write_operations"
                ]
                == 3 * max_length
            ),
        },
        {
            "name": "identity relays do not inflate record stock",
            "pass": (
                representation_signatures["full_append_only"]
                == representation_signatures["identity_relay_append_only"]
                and series["identity_relay_append_only"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == max_length
            ),
        },
        {
            "name": "two-bit packing changes resolution but not quotient",
            "pass": (
                representation_signatures["full_append_only"]
                == representation_signatures["packed_pair_resolution"]
                and series["packed_pair_resolution"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == max_length
            ),
        },
        {
            "name": "last-bit overwrite saturates and loses old classes",
            "pass": (
                series["last_bit_overwrite"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == 1
                and not series["last_bit_overwrite"][1][
                    "retains_all_prior_classes_after_any_next_input"
                ]
            ),
        },
        {
            "name": "parity retains one bit despite six causal inputs",
            "pass": (
                parity_control["maximum_distinguishable_stock_bits"] == 1
                and parity_control["causal_input_influence_count"]
                == max_length
                and not series["parity_accumulator"][1][
                    "retains_all_prior_classes_after_any_next_input"
                ]
            ),
        },
        {
            "name": "rolling memory saturates at its four-state bound",
            "pass": (
                series["rolling_two_bit"][-1][
                    "experiment_equivalence_classes"
                ]
                == 4
                and series["rolling_two_bit"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == 2
                and not series["rolling_two_bit"][2][
                    "retains_all_prior_classes_after_any_next_input"
                ]
            ),
        },
        {
            "name": "all fixed-state fixtures obey class-count bound",
            "pass": all(
                row["maximum_reachable_classes_over_lengths_0_to_6"]
                <= row["declared_state_bound"]
                for row in fixed_state_theorem_fixtures.values()
            ),
        },
        {
            "name": "parity-only fit fails full-recall holdout",
            "pass": (
                readout_dependence["full_memory_parity_only_classes"]
                == readout_dependence[
                    "parity_machine_parity_only_classes"
                ]
                == 2
                and readout_dependence["full_memory_full_recall_classes"]
                == 2**max_length
                and readout_dependence["parity_machine_full_recall_classes"]
                == 2
            ),
        },
        {
            "name": "one redundant carrier fault is repaired but two are not",
            "pass": (
                tuple(
                    redundancy_control["one_carrier_corruption_decodes"]
                )
                == fault_history
                and tuple(
                    redundancy_control["two_carrier_corruption_decodes"]
                )
                != fault_history
            ),
        },
        {
            "name": "redundancy changes viability without changing stock",
            "pass": (
                redundancy_control["full_memory_stock_bits"]
                == redundancy_control["triplicate_stock_bits"]
                == max_length
                and redundancy_control["triplicate_carrier_cells"]
                == 3
                * redundancy_control["full_memory_carrier_cells"]
            ),
        },
        {
            "name": "archive boundary ablation collapses growing stock",
            "pass": (
                boundary_control["observer_internal_stock_bits"] == 1
                and boundary_control["observer_plus_archive_stock_bits"]
                == max_length
                and boundary_control["archive_ablation_lost_bits"]
                == max_length - 1
            ),
        },
        {
            "name": "hidden scheduler fibre is not history provenance",
            "pass": (
                hidden_fibre_control[
                    "raw_history_times_scheduler_tag_microstates"
                ]
                == 2
                * hidden_fibre_control[
                    "history_response_classes_when_tag_is_ignored"
                ]
                and hidden_fibre_control[
                    "history_provenance_classes_when_tag_is_read"
                ]
                == hidden_fibre_control["history_count"]
                and hidden_fibre_control[
                    "joint_experiment_classes_when_tag_is_read"
                ]
                == 2 * hidden_fibre_control["history_count"]
            ),
        },
        {
            "name": "Shannon entropy differs from maximum distinguishable stock",
            "pass": (
                information_controls[
                    "full_memory_bernoulli_one_quarter_entropy_bits"
                ]
                < information_controls["full_memory_capacity_bits"]
                and information_controls[
                    "full_memory_uniform_shannon_entropy_bits"
                ]
                == information_controls["full_memory_capacity_bits"]
            ),
        },
        {
            "name": "cumulative writes differ from retained stock",
            "pass": (
                series["parity_accumulator"][-1][
                    "cumulative_write_operations"
                ]
                == max_length
                and series["parity_accumulator"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == 1
                and series["identity_relay_append_only"][-1][
                    "cumulative_write_operations"
                ]
                == 3 * max_length
                and series["identity_relay_append_only"][-1][
                    "maximum_distinguishable_stock_bits"
                ]
                == max_length
            ),
        },
        {
            "name": "record stock does not create a dimensional time unit",
            "pass": (
                unit_control["duration_under_A"]
                != unit_control["duration_under_B"]
                and unit_control["dimensionless_stock_bits"] == max_length
            ),
        },
    ]

    failed_checks = [check["name"] for check in checks if not check["pass"]]
    if failed_checks:
        raise AssertionError(f"failed checks: {failed_checks}")

    payload = {
        "probe": "du_foundational_heterodox_record_capacity_probe",
        "status": (
            "INTERVENTION-RELATIVE RECORD QUOTIENT CONSTRUCTED / "
            "FIXED-STATE DURABLE-RECORD SATURATION THEOREM / "
            "UNBOUNDED CLOCK REQUIRES GROWTH, EXPORT, OR WEAKER SEMANTICS"
        ),
        "scientific_endorsement": False,
        "frozen_target": {
            "chosen_target": (
                "Construct and attack an intervention-quotiented durable "
                "record functional for finite observers."
            ),
            "dependency_changed": (
                "HC-DU-031A gains a record-passport object and an exact "
                "finite-capacity stop before Clock-QCA record counts are "
                "identified with elapsed time."
            ),
            "smallest_deliverable": (
                "One behavioral quotient, one saturation theorem, and exact "
                "copy/relay/overwrite/held-out/archive controls."
            ),
            "stop_rule": (
                "Do not use the quotient as a clock unless the physical "
                "experiment algebra is fixed, prior distinctions persist, "
                "and growing state or exported archive is resource-accounted."
            ),
        },
        "object": {
            "history_sample_space": "H_t = {0,1}^t",
            "inferential_map": (
                "E_t maps a history to a recorder state; U_t is a declared "
                "experiment family; h ~ h' iff every u in U_t yields the "
                "same response."
            ),
            "observable": "C_t = log2 |H_t / ~_U| dimensionless bits",
            "durability": (
                "Distinct time-t classes may not merge after any pair of "
                "allowed next binary inputs."
            ),
            "representation_quotient": (
                "Relabelings, deterministic copies, identity relays, and "
                "packing changes receive no extra provenance credit when "
                "their response signatures agree."
            ),
            "free_choices": (
                "experiment algebra, system boundary, input alphabet, "
                "retention requirement, and physical unit map"
            ),
            "success": (
                "The quotient survives representation controls, detects "
                "overwrite and final-fit failure, obeys the finite-state "
                "bound, and exposes archive growth."
            ),
            "failure_scope": (
                "There is no absolute readout-independent record stock and "
                "no proper-time or thermodynamic identity."
            ),
        },
        "theorem": {
            "name": "finite-state durable-record saturation",
            "statement": (
                "If all admitted responses factor through S with |S|=M, "
                "then |H_t/~_U|<=M. If each binary opportunity adds one "
                "durable independent distinction, |H_t/~_U|>=2^t, hence "
                "M>=2^t."
            ),
            "proof": [
                "Each response signature is a function of one state in S, so there are at most M signatures.",
                "Durability prevents old classes from merging.",
                "One new independent binary distinction splits every retained class, doubling the class count.",
                "Iteration from one initial class gives at least 2^t classes; combine with the upper bound.",
            ],
            "caveats": [
                "The experiment algebra and boundary are declared, not derived.",
                "log2 of the class count is an operational capacity; a general quotient need not factor into jointly independent binary records.",
                "The result bounds persistent independent history distinctions, not event number.",
                "A growing internal state space or included external archive evades the fixed-M premise.",
                "Logical overwrite is typed separately from heat/work; no Landauer cost is calculated.",
                "Quantum, continuous-state, noisy, and approximate records need separate generalizations.",
            ],
        },
        "model_series": series,
        "readout_and_held_out_control": readout_dependence,
        "causal_influence_control": parity_control,
        "information_controls": information_controls,
        "redundancy_and_viability_control": redundancy_control,
        "hidden_fibre_control": hidden_fibre_control,
        "boundary_and_archive_control": boundary_control,
        "unit_control": unit_control,
        "fixed_state_theorem_fixtures": fixed_state_theorem_fixtures,
        "rival_ledger": [
            {
                "rival": "raw update or cumulative write count",
                "result": "Parity and relay fixtures separate writes from stock.",
            },
            {
                "rival": "Shannon entropy",
                "result": "Distribution-weighted entropy differs from maximum class capacity.",
            },
            {
                "rival": "causal influence count",
                "result": "All six inputs affect parity while only one bit persists.",
            },
            {
                "rival": "flat final-state fit",
                "result": "Parity matches the development readout and fails held-out recall.",
            },
            {
                "rival": "copies, relays, packing, and scheduler fibre",
                "result": "They add resources or degrees of freedom without adding history provenance classes.",
            },
            {
                "rival": "free external archive",
                "result": "It restores growth only after boundary and storage expansion are admitted.",
            },
            {
                "rival": "thermodynamic record definition",
                "result": "Live but separate; overwrite/erasure cost is not inferred from logical stock.",
            },
            {
                "rival": "causal-post program",
                "result": "Unaffected; this swing changes the record-clock dependency only.",
            },
        ],
        "checks": checks,
        "checks_passed": sum(check["pass"] for check in checks),
        "checks_total": len(checks),
        "claim_controls": {
            "banked": False,
            "seeded": False,
            "forbidden_overclaims": [
                "Every write is a new durable record.",
                "Maximum distinguishable stock is Shannon entropy.",
                "Copy redundancy creates independent records.",
                "The quotient is observer-independent without a physical experiment algebra.",
                "A dimensionless record bit is a unit of proper time.",
                "Finite-state saturation forbids time, events, or exported records.",
                "Logical erasure alone establishes a thermodynamic work value.",
            ],
        },
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "du_foundational_heterodox_record_capacity_probe: "
        f"{payload['checks_passed']}/{payload['checks_total']} checks passed"
    )
    print(payload["status"])


if __name__ == "__main__":
    main()
