#!/usr/bin/env python3
"""Exact finite controls for the Certified Causal Reconstruction spine.

The probe tests an autonomous record-state normal form.  For a finite
controlled selective kernel

    K_a(s, y, h' | h),

a deterministic record r(h) has a well-defined controlled quotient exactly
when, for every action a, acquisition stratum s, response y, and next-record
class q', the aggregate probability

    sum_{h': r(h') = q'} K_a(s, y, h' | h)

depends on h only through r(h).  This is labelled controlled strong
lumpability / probabilistic bisimulation.  It is stronger than predictive
sufficiency for one fixed finite tester family.

All arithmetic is exact.  The two platform anchors are finite operational
shadows, not physical implementations or evidence of new physics.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT / "tests" / "artifacts" / "du_certified_causal_spine_result.json"
)
RUN_ID = "RUN-20260726-144910-certified-causal-spine"
F = Fraction


def q(numerator: int, denominator: int = 1) -> Fraction:
    return F(numerator, denominator)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


@dataclass(frozen=True)
class Branch:
    selection: str
    response: str
    next_state: str
    probability: Fraction


@dataclass(frozen=True)
class ControlledRecordModel:
    model_id: str
    states: tuple[str, ...]
    actions: tuple[str, ...]
    records: Mapping[str, str]
    kernel: Mapping[tuple[str, str], tuple[Branch, ...]]
    interpretation: str

    def validate(self) -> None:
        if not self.states or not self.actions:
            raise ValueError(f"{self.model_id}: empty state or action set")
        if set(self.records) != set(self.states):
            raise ValueError(f"{self.model_id}: record domain mismatch")
        for state in self.states:
            for action in self.actions:
                branches = self.kernel.get((state, action))
                if branches is None:
                    raise ValueError(
                        f"{self.model_id}: missing row {(state, action)}"
                    )
                if any(branch.next_state not in self.states for branch in branches):
                    raise ValueError(
                        f"{self.model_id}: branch leaves the state space"
                    )
                if any(branch.probability < 0 for branch in branches):
                    raise ValueError(
                        f"{self.model_id}: negative branch probability"
                    )
                if sum(
                    (branch.probability for branch in branches), q(0)
                ) != q(1):
                    raise ValueError(
                        f"{self.model_id}: row {(state, action)} is not normalized"
                    )


SelectiveRow = dict[tuple[str, str, str], Fraction]


def record_blocks(
    model: ControlledRecordModel,
    records: Mapping[str, str] | None = None,
) -> dict[str, tuple[str, ...]]:
    selected = records or model.records
    blocks: dict[str, list[str]] = {}
    for state in model.states:
        blocks.setdefault(selected[state], []).append(state)
    return {
        record: tuple(states)
        for record, states in sorted(blocks.items())
    }


def selective_row(
    model: ControlledRecordModel,
    state: str,
    action: str,
    records: Mapping[str, str] | None = None,
) -> SelectiveRow:
    selected = records or model.records
    row: SelectiveRow = {}
    for branch in model.kernel[(state, action)]:
        key = (
            branch.selection,
            branch.response,
            selected[branch.next_state],
        )
        row[key] = row.get(key, q(0)) + branch.probability
    return dict(sorted(row.items()))


def event_marginal(row: SelectiveRow) -> dict[tuple[str, str], Fraction]:
    result: dict[tuple[str, str], Fraction] = {}
    for (selection, response, _), probability in row.items():
        key = (selection, response)
        result[key] = result.get(key, q(0)) + probability
    return dict(sorted(result.items()))


def next_record_marginal(row: SelectiveRow) -> dict[str, Fraction]:
    result: dict[str, Fraction] = {}
    for (_, _, next_record), probability in row.items():
        result[next_record] = result.get(next_record, q(0)) + probability
    return dict(sorted(result.items()))


def selective_congruence_failures(
    model: ControlledRecordModel,
    records: Mapping[str, str] | None = None,
) -> list[dict[str, Any]]:
    selected = records or model.records
    failures: list[dict[str, Any]] = []
    for record, states in record_blocks(model, selected).items():
        if len(states) < 2:
            continue
        reference = states[0]
        for rival in states[1:]:
            for action in model.actions:
                left = selective_row(model, reference, action, selected)
                right = selective_row(model, rival, action, selected)
                if left != right:
                    failures.append(
                        {
                            "record": record,
                            "left_state": reference,
                            "right_state": rival,
                            "action": action,
                            "left_row": left,
                            "right_row": right,
                        }
                    )
    return failures


def weak_marginals_factor(
    model: ControlledRecordModel,
    left_state: str,
    right_state: str,
    action: str,
) -> bool:
    left = selective_row(model, left_state, action)
    right = selective_row(model, right_state, action)
    return (
        event_marginal(left) == event_marginal(right)
        and next_record_marginal(left) == next_record_marginal(right)
    )


def quotient_kernel(
    model: ControlledRecordModel,
    records: Mapping[str, str] | None = None,
) -> dict[tuple[str, str], SelectiveRow]:
    selected = records or model.records
    failures = selective_congruence_failures(model, selected)
    if failures:
        raise ValueError("selective congruence fails")
    result: dict[tuple[str, str], SelectiveRow] = {}
    for record, states in record_blocks(model, selected).items():
        for action in model.actions:
            result[(record, action)] = selective_row(
                model, states[0], action, selected
            )
    return result


Trace = tuple[tuple[str, str, str], ...]


def trace_distribution(
    model: ControlledRecordModel,
    start_state: str,
    action_word: Sequence[str],
    records: Mapping[str, str] | None = None,
) -> dict[Trace, Fraction]:
    selected = records or model.records
    frontier: dict[tuple[str, Trace], Fraction] = {
        (start_state, ()): q(1)
    }
    for action in action_word:
        next_frontier: dict[tuple[str, Trace], Fraction] = {}
        for (state, trace), prefix_probability in frontier.items():
            for branch in model.kernel[(state, action)]:
                event = (
                    branch.selection,
                    branch.response,
                    selected[branch.next_state],
                )
                key = (branch.next_state, trace + (event,))
                next_frontier[key] = (
                    next_frontier.get(key, q(0))
                    + prefix_probability * branch.probability
                )
        frontier = next_frontier
    collapsed: dict[Trace, Fraction] = {}
    for (_, trace), probability in frontier.items():
        collapsed[trace] = collapsed.get(trace, q(0)) + probability
    return dict(sorted(collapsed.items()))


def action_words(actions: Sequence[str], max_depth: int) -> Iterable[tuple[str, ...]]:
    for depth in range(max_depth + 1):
        yield from itertools.product(actions, repeat=depth)


def traces_factor_through_record(
    model: ControlledRecordModel,
    max_depth: int,
    records: Mapping[str, str] | None = None,
) -> bool:
    selected = records or model.records
    for _, states in record_blocks(model, selected).items():
        for left, right in itertools.combinations(states, 2):
            for word in action_words(model.actions, max_depth):
                if trace_distribution(model, left, word, selected) != (
                    trace_distribution(model, right, word, selected)
                ):
                    return False
    return True


def deterministic_model(
    model_id: str,
    records: Mapping[str, str],
    transitions: Mapping[str, str],
    responses: Mapping[str, str],
) -> ControlledRecordModel:
    states = tuple(records)
    return ControlledRecordModel(
        model_id=model_id,
        states=states,
        actions=("step",),
        records=records,
        kernel={
            (state, "step"): (
                Branch(
                    "returned",
                    responses[state],
                    transitions[state],
                    q(1),
                ),
            )
            for state in states
        },
        interpretation="deterministic labelled-transition control",
    )


def positive_quotient_control() -> ControlledRecordModel:
    return ControlledRecordModel(
        model_id="nontrivial_positive_quotient",
        states=("a", "b", "c"),
        actions=("step", "hold"),
        records={"a": "q0", "b": "q0", "c": "q1"},
        kernel={
            ("a", "step"): (
                Branch("returned", "stay", "a", q(1, 2)),
                Branch("returned", "advance", "c", q(1, 2)),
            ),
            ("b", "step"): (
                Branch("returned", "stay", "b", q(1, 2)),
                Branch("returned", "advance", "c", q(1, 2)),
            ),
            ("c", "step"): (
                Branch("returned", "done", "c", q(1)),
            ),
            ("a", "hold"): (
                Branch("returned", "held", "a", q(1)),
            ),
            ("b", "hold"): (
                Branch("returned", "held", "b", q(1)),
            ),
            ("c", "hold"): (
                Branch("returned", "held", "c", q(1)),
            ),
        },
        interpretation=(
            "hidden a/b identity survives while every labelled next-record "
            "probability is quotient autonomous"
        ),
    )


def minimum_endpoint_counterexample() -> dict[str, Any]:
    canonical = deterministic_model(
        "minimum_endpoint_counterexample",
        {"h0": "q0", "h1": "q0", "v": "q1"},
        {"h0": "h0", "h1": "v", "v": "v"},
        {"h0": "y0", "h1": "y0", "v": "y1"},
    )

    def witness_exists(state_count: int) -> bool:
        states = tuple(range(state_count))
        for record_values in itertools.product(range(state_count), repeat=state_count):
            if len(set(record_values)) < 2:
                continue
            for responses in itertools.product((0, 1), repeat=state_count):
                if any(
                    record_values[left] == record_values[right]
                    and responses[left] != responses[right]
                    for left, right in itertools.product(states, repeat=2)
                ):
                    continue
                for transitions in itertools.product(states, repeat=state_count):
                    if any(
                        record_values[left] == record_values[right]
                        and record_values[transitions[left]]
                        != record_values[transitions[right]]
                        for left, right in itertools.product(states, repeat=2)
                    ):
                        return True
        return False

    return {
        "model": canonical,
        "current_response_factors": True,
        "selective_congruence_fails": bool(
            selective_congruence_failures(canonical)
        ),
        "two_state_exhaustive_witness_exists": witness_exists(2),
        "three_state_exhaustive_witness_exists": witness_exists(3),
    }


def selective_correlation_counterexample() -> ControlledRecordModel:
    return ControlledRecordModel(
        model_id="weak_stochastic_marginals_fail",
        states=("h0", "h1", "v"),
        actions=("attempt",),
        records={"h0": "q0", "h1": "q0", "v": "q1"},
        kernel={
            ("h0", "attempt"): (
                Branch("s0", "y0", "h0", q(1, 2)),
                Branch("s1", "y0", "v", q(1, 2)),
            ),
            ("h1", "attempt"): (
                Branch("s0", "y0", "v", q(1, 2)),
                Branch("s1", "y0", "h1", q(1, 2)),
            ),
            ("v", "attempt"): (
                Branch("s1", "y1", "v", q(1)),
            ),
        },
        interpretation=(
            "event and next-record marginals agree for h0/h1, but their "
            "joint selective correlations are opposite"
        ),
    )


def returned_only_counterexample() -> ControlledRecordModel:
    return ControlledRecordModel(
        model_id="returned_only_misses_rejected_stratum",
        states=("h0", "h1"),
        actions=("attempt",),
        records={"h0": "q", "h1": "q"},
        kernel={
            ("h0", "attempt"): (
                Branch("rejected", "y0", "h0", q(1, 2)),
                Branch("accepted", "y0", "h0", q(1, 2)),
            ),
            ("h1", "attempt"): (
                Branch("rejected", "y1", "h1", q(1, 2)),
                Branch("accepted", "y0", "h1", q(1, 2)),
            ),
        },
        interpretation=(
            "same acceptance rate and accepted response; different rejected "
            "response and full attempted process"
        ),
    )


def accepted_view(model: ControlledRecordModel, state: str) -> dict[str, Any]:
    row = selective_row(model, state, "attempt")
    accepted = {
        response: probability
        for (selection, response, _), probability in row.items()
        if selection == "accepted"
    }
    probability = sum(accepted.values(), q(0))
    conditional = {
        response: value / probability
        for response, value in accepted.items()
    }
    return {
        "acceptance_probability": probability,
        "conditional_response": conditional,
    }


def reset_model() -> ControlledRecordModel:
    states = ("x0m0", "x0m1", "x1m0", "x1m1")
    x_value = {
        "x0m0": 0,
        "x0m1": 0,
        "x1m0": 1,
        "x1m1": 1,
    }
    memory = {
        "x0m0": 0,
        "x0m1": 1,
        "x1m0": 0,
        "x1m1": 1,
    }
    by_pair = {
        (0, 0): "x0m0",
        (0, 1): "x0m1",
        (1, 0): "x1m0",
        (1, 1): "x1m1",
    }
    kernel: dict[tuple[str, str], tuple[Branch, ...]] = {}
    for state in states:
        m = memory[state]
        kernel[(state, "system_reset")] = (
            Branch("returned", "reset", by_pair[(0, m)], q(1)),
        )
        kernel[(state, "full_reset")] = (
            Branch("returned", "reset", by_pair[(0, 0)], q(1)),
        )
        kernel[(state, "couple_read")] = (
            Branch("returned", str(m), by_pair[(m, m)], q(1)),
        )
    return ControlledRecordModel(
        model_id="reset_scope_control",
        states=states,
        actions=("system_reset", "full_reset", "couple_read"),
        records={state: f"x{x_value[state]}" for state in states},
        kernel=kernel,
        interpretation=(
            "system reset clears the visible bit but retains memory; full "
            "reset clears both before a recoupling readout"
        ),
    )


def quantum_anchor() -> tuple[ControlledRecordModel, dict[str, str]]:
    states = ("qnd0", "qnd1", "flip0", "flip1")
    bit = {"qnd0": 0, "qnd1": 1, "flip0": 0, "flip1": 1}
    implementation = {
        "qnd0": "qnd",
        "qnd1": "qnd",
        "flip0": "flip",
        "flip1": "flip",
    }
    kernel: dict[tuple[str, str], tuple[Branch, ...]] = {}
    for state in states:
        kernel[(state, "read_archive")] = (
            Branch("returned", str(bit[state]), state, q(1)),
        )
        repeat = (
            bit[state]
            if implementation[state] == "qnd"
            else 1 - bit[state]
        )
        kernel[(state, "repeat_system")] = (
            Branch("returned", str(repeat), state, q(1)),
        )
    model = ControlledRecordModel(
        model_id="binary_quantum_instrument_shadow",
        states=states,
        actions=("read_archive", "repeat_system"),
        records={state: f"archive_{bit[state]}" for state in states},
        kernel=kernel,
        interpretation=(
            "exact finite shadow of QND versus flip-after-record "
            "measure-and-prepare instruments with the same formed archive"
        ),
    )
    refinement = {
        state: f"archive_{bit[state]}__instrument_{implementation[state]}"
        for state in states
    }
    return model, refinement


def distributed_anchor() -> tuple[ControlledRecordModel, dict[str, str]]:
    model = ControlledRecordModel(
        model_id="authenticated_layered_consensus_shadow",
        states=("metastable_final", "bft_final", "pending"),
        actions=("read_public", "late_conflict"),
        records={
            "metastable_final": "public_final",
            "bft_final": "public_final",
            "pending": "public_pending",
        },
        kernel={
            ("metastable_final", "read_public"): (
                Branch("returned", "final", "metastable_final", q(1)),
            ),
            ("bft_final", "read_public"): (
                Branch("returned", "final", "bft_final", q(1)),
            ),
            ("pending", "read_public"): (
                Branch("returned", "pending", "pending", q(1)),
            ),
            ("metastable_final", "late_conflict"): (
                Branch("authenticated", "reopened", "pending", q(1)),
            ),
            ("bft_final", "late_conflict"): (
                Branch("authenticated", "held", "bft_final", q(1)),
            ),
            ("pending", "late_conflict"): (
                Branch("authenticated", "remains_pending", "pending", q(1)),
            ),
        },
        interpretation=(
            "same public endpoint value at a metastable and a BFT-hardened "
            "layer; an authenticated late-conflict continuation separates them"
        ),
    )
    refinement = {
        "metastable_final": "public_final__layer_metastable",
        "bft_final": "public_final__layer_bft",
        "pending": "public_pending__layer_pending",
    }
    return model, refinement


def pareto_minimal_repairs(
    candidates: Sequence[dict[str, Any]],
) -> tuple[str, ...]:
    eligible = [
        candidate
        for candidate in candidates
        if candidate["admissible"] and candidate["exact"]
    ]
    minimal: list[str] = []
    for candidate in eligible:
        cost = candidate["resource_vector"]
        dominated = any(
            rival["candidate_id"] != candidate["candidate_id"]
            and all(
                rival_value <= value
                for rival_value, value in zip(
                    rival["resource_vector"], cost, strict=True
                )
            )
            and any(
                rival_value < value
                for rival_value, value in zip(
                    rival["resource_vector"], cost, strict=True
                )
            )
            for rival in eligible
        )
        if not dominated:
            minimal.append(candidate["candidate_id"])
    return tuple(sorted(minimal))


def target_coded_repair_control() -> dict[str, Any]:
    model = ControlledRecordModel(
        model_id="target_coded_repair",
        states=("h0", "h1"),
        actions=("target_read",),
        records={"h0": "base", "h1": "base"},
        kernel={
            ("h0", "target_read"): (
                Branch("returned", "0", "h0", q(1)),
            ),
            ("h1", "target_read"): (
                Branch("returned", "1", "h1", q(1)),
            ),
        },
        interpretation="the target itself is appended to the candidate record",
    )
    target_refinement = {"h0": "base__target_0", "h1": "base__target_1"}
    exact = not selective_congruence_failures(model, target_refinement)
    return {
        "base_exact": not selective_congruence_failures(model),
        "target_refinement_exact": exact,
        "admissible": False,
        "refusal_reason": "target_fitted_completion",
    }


def representation_selector_control() -> dict[str, Any]:
    representations = {
        "phi0": {"good": q(0), "bad": q(1)},
        "phi1": {"good": q(1), "bad": q(0)},
    }
    selected = {
        representation: min(values, key=values.get)
        for representation, values in representations.items()
    }
    return {
        "selected_by_representation": selected,
        "descends_to_equivalence_class": len(set(selected.values())) == 1,
        "classification": "REPRESENTATION_SENSITIVE_NO_SELECTOR",
    }


def run() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(check_id: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{check_id}: {detail}")
        checks.append({"check_id": check_id, "passed": True, "detail": detail})

    positive = positive_quotient_control()
    endpoint = minimum_endpoint_counterexample()
    correlation = selective_correlation_counterexample()
    returned = returned_only_counterexample()
    reset = reset_model()
    quantum, quantum_refinement = quantum_anchor()
    distributed, distributed_refinement = distributed_anchor()
    for model in (
        positive,
        endpoint["model"],
        correlation,
        returned,
        reset,
        quantum,
        distributed,
    ):
        model.validate()

    positive_quotient = quotient_kernel(positive)
    check(
        "selective_lumpability_defines_autonomous_quotient",
        not selective_congruence_failures(positive)
        and bool(positive_quotient),
        "the labelled next-record row is independent of hidden representative",
    )
    check(
        "selective_lumpability_preserves_all_tested_traces",
        traces_factor_through_record(positive, max_depth=5),
        "all action words through depth five have equal trace laws within each record block",
    )
    check(
        "endpoint_factorization_needs_continuation_congruence",
        endpoint["current_response_factors"]
        and endpoint["selective_congruence_fails"],
        "equal current response does not determine the labelled next record",
    )
    check(
        "three_states_are_minimal_for_deterministic_endpoint_witness",
        not endpoint["two_state_exhaustive_witness_exists"]
        and endpoint["three_state_exhaustive_witness_exists"],
        "exhaustive deterministic search finds no two-state witness and a three-state witness",
    )
    check(
        "weak_stochastic_marginals_miss_selective_correlation",
        weak_marginals_factor(correlation, "h0", "h1", "attempt")
        and bool(selective_congruence_failures(correlation)),
        "event and next-record marginals agree while their joint distribution differs",
    )

    accepted_h0 = accepted_view(returned, "h0")
    accepted_h1 = accepted_view(returned, "h1")
    check(
        "returned_only_misses_rejected_stratum",
        accepted_h0 == accepted_h1
        and bool(selective_congruence_failures(returned)),
        "same acceptance rate and accepted response coexist with a different rejected response",
    )

    system_reset_left = trace_distribution(
        reset, "x1m0", ("system_reset", "couple_read")
    )
    system_reset_right = trace_distribution(
        reset, "x1m1", ("system_reset", "couple_read")
    )
    full_reset_left = trace_distribution(
        reset, "x1m0", ("full_reset", "couple_read")
    )
    full_reset_right = trace_distribution(
        reset, "x1m1", ("full_reset", "couple_read")
    )
    check(
        "system_reset_does_not_reset_hidden_memory",
        system_reset_left != system_reset_right,
        "a later recoupling distinguishes histories after visible-system reset",
    )
    check(
        "complete_reset_removes_residual",
        full_reset_left == full_reset_right,
        "resetting visible and retained memory equalizes the held-out continuation",
    )

    observed_record = "q_missing"
    observed_fibre = tuple(
        state
        for state in positive.states
        if positive.records[state] == observed_record
    )
    vacuous_target_constancy = len(set()) <= 1
    check(
        "realizability_precedes_target_constancy",
        not observed_fibre and vacuous_target_constancy,
        "an empty fibre is UNREALIZABLE, never a vacuous reconstruction success",
    )

    target_repair = target_coded_repair_control()
    check(
        "target_coded_repair_is_refused",
        not target_repair["base_exact"]
        and target_repair["target_refinement_exact"]
        and not target_repair["admissible"],
        "an exact target-derived split is a diagnostic, not an independently formed repair",
    )

    representation = representation_selector_control()
    check(
        "selector_must_descend_across_representation_class",
        not representation["descends_to_equivalence_class"],
        "equivalent admitted representations select opposite candidates",
    )

    quantum_base_failures = selective_congruence_failures(quantum)
    quantum_refined_failures = selective_congruence_failures(
        quantum, quantum_refinement
    )
    distributed_base_failures = selective_congruence_failures(distributed)
    distributed_refined_failures = selective_congruence_failures(
        distributed, distributed_refinement
    )
    check(
        "quantum_anchor_exposes_one_heldout_continuation",
        any(
            failure["action"] == "repeat_system"
            for failure in quantum_base_failures
        ),
        "QND and flip-after-record share the archive but differ under repeat",
    )
    check(
        "quantum_selective_map_refinement_repairs_quotient",
        not quantum_refined_failures,
        "the independently declared instrument tag makes the finite anchor autonomous",
    )
    check(
        "distributed_anchor_exposes_one_late_conflict",
        any(
            failure["action"] == "late_conflict"
            for failure in distributed_base_failures
        ),
        "metastable and BFT-hardened endpoints differ under an authenticated late conflict",
    )
    check(
        "distributed_layer_provenance_repairs_quotient",
        not distributed_refined_failures,
        "authenticated layer provenance makes the finite anchor autonomous",
    )

    candidate_repairs = {
        "quantum": (
            {
                "candidate_id": "base_archive",
                "admissible": True,
                "exact": False,
                "resource_vector": (0, 0),
            },
            {
                "candidate_id": "instrument_receipt",
                "admissible": True,
                "exact": True,
                "resource_vector": (1, 1),
            },
            {
                "candidate_id": "target_coded",
                "admissible": False,
                "exact": True,
                "resource_vector": (0, 1),
            },
        ),
        "distributed": (
            {
                "candidate_id": "public_endpoint",
                "admissible": True,
                "exact": False,
                "resource_vector": (0, 0),
            },
            {
                "candidate_id": "authenticated_layer_receipt",
                "admissible": True,
                "exact": True,
                "resource_vector": (1, 1),
            },
            {
                "candidate_id": "future_response_label",
                "admissible": False,
                "exact": True,
                "resource_vector": (0, 1),
            },
        ),
    }
    quantum_pareto = pareto_minimal_repairs(candidate_repairs["quantum"])
    distributed_pareto = pareto_minimal_repairs(
        candidate_repairs["distributed"]
    )
    check(
        "finite_quantum_repair_class_has_pareto_minimum",
        quantum_pareto == ("instrument_receipt",),
        "minimality is earned only inside the frozen finite admissible class",
    )
    check(
        "finite_distributed_repair_class_has_pareto_minimum",
        distributed_pareto == ("authenticated_layer_receipt",),
        "the same finite Pareto rule is reused without platform-specific refitting",
    )

    relabelled_records = {
        state: {"q0": "alpha", "q1": "beta"}[record]
        for state, record in endpoint["model"].records.items()
    }
    check(
        "pure_record_relabeling_preserves_failure",
        len(
            selective_congruence_failures(
                endpoint["model"], relabelled_records
            )
        )
        == len(selective_congruence_failures(endpoint["model"])),
        "a bijective record-label change cannot manufacture a quotient",
    )
    check(
        "one_unchanged_schema_serves_both_anchors",
        isinstance(quantum, ControlledRecordModel)
        and isinstance(distributed, ControlledRecordModel)
        and set(quantum.actions)
        and set(distributed.actions),
        (
            "both anchors use states, actions, selection, response, next "
            "state, record, and exact probability"
        ),
    )

    outcome = "KNOWN_MATHEMATICS__INTEGRATED_ASSURANCE_ONLY"
    result = {
        "artifact_type": (
            "exact_finite_certified_causal_autonomous_record_quotient_controls"
        ),
        "run_id": RUN_ID,
        "convergence_outcome": outcome,
        "theorem": {
            "name": "Finite selective autonomous-record quotient criterion",
            "condition": (
                "For all record-equivalent h,h', admitted actions a, "
                "acquisition strata s, responses y, and next-record classes "
                "q', the aggregate K_a(s,y,q'|h) equals K_a(s,y,q'|h')."
            ),
            "necessity": (
                "Any well-defined quotient selective kernel must assign one "
                "row to the common current record, so representative rows agree."
            ),
            "sufficiency": (
                "The common row defines the quotient kernel; induction on "
                "action words preserves every finite labelled-record trace, "
                "including record-adaptive policies."
            ),
            "bounded_failure_witness": (
                "A failed condition supplies one current record, two hidden "
                "representatives, one action, one stratum-response cell, and "
                "one next-record class. General trace-equivalence searches "
                "need an independently frozen finite-state/rank bound."
            ),
            "scope_boundary": (
                "This is necessary and sufficient for an autonomous record "
                "state. Predictive sufficiency for a fixed tester family is "
                "the weaker Blackwell factorization of that bundled experiment "
                "and need not imply bisimulation."
            ),
            "absorber": (
                "labelled controlled strong lumpability / probabilistic "
                "bisimulation, with Blackwell sufficiency for fixed response "
                "families and process tensors/combs for quantum multi-time behavior"
            ),
        },
        "hostile_controls": {
            "endpoint_minimum": {
                key: value
                for key, value in endpoint.items()
                if key != "model"
            },
            "selective_correlation_failure": {
                "weak_marginals_factor": weak_marginals_factor(
                    correlation, "h0", "h1", "attempt"
                ),
                "full_selective_failures": selective_congruence_failures(
                    correlation
                ),
            },
            "returned_only": {
                "h0": accepted_h0,
                "h1": accepted_h1,
                "full_selective_failures": selective_congruence_failures(
                    returned
                ),
            },
            "reset": {
                "system_only_equal": system_reset_left == system_reset_right,
                "complete_equal": full_reset_left == full_reset_right,
            },
            "empty_fibre": {
                "observed_record": observed_record,
                "fibre": observed_fibre,
                "classification": "UNREALIZABLE",
            },
            "target_coded_repair": target_repair,
            "representation_selector": representation,
        },
        "anchors": {
            "quantum_instrument": {
                "evidence_level": (
                    "exact finite classical shadow of standard binary "
                    "measure-and-prepare instrument behavior"
                ),
                "base_failure_actions": tuple(
                    sorted(
                        {
                            failure["action"]
                            for failure in quantum_base_failures
                        }
                    )
                ),
                "refined_failure_count": len(quantum_refined_failures),
                "minimum_discriminator": "repeat_system",
                "pareto_repairs": quantum_pareto,
            },
            "authenticated_distributed_process": {
                "evidence_level": (
                    "exact finite authenticated layered-consensus shadow"
                ),
                "base_failure_actions": tuple(
                    sorted(
                        {
                            failure["action"]
                            for failure in distributed_base_failures
                        }
                    )
                ),
                "refined_failure_count": len(distributed_refined_failures),
                "minimum_discriminator": "late_conflict",
                "pareto_repairs": distributed_pareto,
            },
            "semantic_refit": False,
        },
        "assurance_contract": {
            "freeze_before_target": (
                "observer boundary, completion class, record, representation "
                "class, action/tester family, all acquisition strata, resources, "
                "reset scope, and admissible refinements"
            ),
            "retain": (
                "joint subnormalized stratum-response-next-record behavior; "
                "never normalized returned rows alone"
            ),
            "reset_receipt": (
                "system, environment/ancilla, pointer/detector, controller, "
                "decoder, route/scheduler, acquisition buffer, and intended archive"
            ),
            "empirical_boundary": (
                "finite data supports calibrated epsilon-sufficiency or an "
                "insufficiency witness, not exact equality"
            ),
            "typed_verdicts": (
                "BASE_QUOTIENT",
                "PARETO_REPAIR",
                "CLASS_RELATIVE_FAILURE",
                "UNREALIZABLE",
                "INCONCLUSIVE",
                "INCOMPLETE_CONTRACT",
            ),
        },
        "campaign_decision": {
            "swing_1": (
                "succeeds as an absorbed formal and assurance spine; it does "
                "not earn a new theorem or physical record ontology"
            ),
            "next_bottleneck": (
                "physical formation and interface selection: determine which "
                "record/refinement is independently produced, accessible, "
                "stable, provenance-bearing, and representation robust"
            ),
            "hardware": (
                "not required; no external-hardware path should be opened from "
                "this finite result"
            ),
        },
        "candidate_repairs": candidate_repairs,
        "checks": checks,
        "checks_passed": len(checks),
        "all_passed": True,
        "limits": (
            "The theorem is established finite quotient mathematics.",
            (
                "The quantum and distributed anchors are exact operational "
                "shadows, not hardware data."
            ),
            "The probe does not select a physically privileged record or admissible refinement.",
            "Pareto minimality is only relative to the explicitly finite candidate classes.",
            (
                "No ontology, physical remainder, new law, new physics, "
                "paper promotion, or external action is established."
            ),
        ),
    }
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = run()
    print(
        f"PASS {result['checks_passed']}/{result['checks_passed']} "
        f"run_id={result['run_id']}"
    )
    print(f"artifact={ARTIFACT.relative_to(ROOT)}")
    print(
        "OUTCOME: known controlled-lumpability/bisimulation mathematics; "
        "integrated DU assurance spine retained"
    )


if __name__ == "__main__":
    main()
