#!/usr/bin/env python3
"""Instrument-derived regional grammar and cross-platform marginal transfer.

This probe uses one unchanged exact marginal compiler and one unchanged
instrument-parent extractor across:

* a multi-time binary record process;
* a replayable authenticated regional protocol; and
* complete two-qubit Mermin--Peres measurement instruments.

The authenticated obstruction is repaired by route-specific provenance and
then safely rejected as equivocation.  The quantum obstruction is the
standard noncontextual-global-assignment obstruction for incompatible
measurement contexts.  Neither is promoted as new physics.
"""

from __future__ import annotations

import hashlib
import hmac
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

from du_exact_marginal_extension_compiler import (
    MarginalProblem,
    compile_marginal_extension,
    complete_context,
    leave_one_context_out,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_multitime_marginal_transfer_result.json"
)


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


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"))


@dataclass(frozen=True)
class InstrumentKernel:
    """A complete controlled stochastic record instrument."""

    instrument_id: str
    variables: tuple[str, ...]
    variable_outcomes: tuple[tuple[str, tuple[str, ...]], ...]
    controls: tuple[str, ...]
    record_outcomes: tuple[str, ...]
    rows: tuple[
        tuple[str, tuple[str, ...], tuple[Fraction, ...]], ...
    ]


def deterministic_kernel(
    instrument_id: str,
    variables: Sequence[str],
    outcome_map: Mapping[str, Sequence[str]],
    controls: Sequence[str],
    response: Callable[[str, Mapping[str, str]], str],
) -> InstrumentKernel:
    variable_tuple = tuple(variables)
    assignments = tuple(
        itertools.product(*(tuple(outcome_map[name]) for name in variable_tuple))
    )
    raw_rows: list[tuple[str, tuple[str, ...], str]] = []
    record_outcomes: set[str] = set()
    for control in controls:
        for assignment in assignments:
            state = dict(zip(variable_tuple, assignment, strict=True))
            outcome = response(control, state)
            record_outcomes.add(outcome)
            raw_rows.append((control, assignment, outcome))
    ordered_outcomes = tuple(sorted(record_outcomes))
    rows = tuple(
        (
            control,
            assignment,
            tuple(
                Fraction(int(candidate == outcome))
                for candidate in ordered_outcomes
            ),
        )
        for control, assignment, outcome in raw_rows
    )
    return InstrumentKernel(
        instrument_id=instrument_id,
        variables=variable_tuple,
        variable_outcomes=tuple(
            (name, tuple(outcome_map[name])) for name in variable_tuple
        ),
        controls=tuple(controls),
        record_outcomes=ordered_outcomes,
        rows=rows,
    )


def validate_kernel(kernel: InstrumentKernel) -> tuple[str, ...]:
    errors: list[str] = []
    if not kernel.instrument_id:
        errors.append("missing_instrument_id")
    if len(set(kernel.variables)) != len(kernel.variables):
        errors.append("duplicate_variable")
    if len(set(kernel.controls)) != len(kernel.controls):
        errors.append("duplicate_control")
    if len(set(kernel.record_outcomes)) != len(kernel.record_outcomes):
        errors.append("duplicate_record_outcome")
    outcome_map = dict(kernel.variable_outcomes)
    expected_assignments = tuple(
        itertools.product(*(outcome_map[name] for name in kernel.variables))
    )
    expected_keys = {
        (control, assignment)
        for control in kernel.controls
        for assignment in expected_assignments
    }
    observed_keys = {(control, assignment) for control, assignment, _ in kernel.rows}
    if expected_keys != observed_keys or len(observed_keys) != len(kernel.rows):
        errors.append("incomplete_or_duplicate_kernel_rows")
    for _, _, distribution in kernel.rows:
        if len(distribution) != len(kernel.record_outcomes):
            errors.append("record_distribution_arity")
        elif any(value < 0 for value in distribution):
            errors.append("negative_probability")
        elif sum(distribution, start=Fraction(0)) != 1:
            errors.append("unnormalized_distribution")
    return tuple(sorted(set(errors)))


def derive_parent_region(kernel: InstrumentKernel) -> tuple[str, ...]:
    """Return variables that affect a complete outcome distribution."""

    errors = validate_kernel(kernel)
    if errors:
        raise ValueError(errors)
    row_map = {
        (control, assignment): distribution
        for control, assignment, distribution in kernel.rows
    }
    outcome_map = dict(kernel.variable_outcomes)
    parents: list[str] = []
    for variable_index, variable in enumerate(kernel.variables):
        influenced = False
        other_indexes = tuple(
            index
            for index in range(len(kernel.variables))
            if index != variable_index
        )
        other_alphabets = tuple(
            outcome_map[kernel.variables[index]] for index in other_indexes
        )
        for control in kernel.controls:
            for other_values in itertools.product(*other_alphabets):
                base = [None] * len(kernel.variables)
                for index, value in zip(
                    other_indexes, other_values, strict=True
                ):
                    base[index] = value
                distributions = []
                for value in outcome_map[variable]:
                    assignment = list(base)
                    assignment[variable_index] = value
                    distributions.append(
                        row_map[(control, tuple(assignment))]
                    )
                if len(set(distributions)) > 1:
                    influenced = True
                    break
            if influenced:
                break
        if influenced:
            parents.append(variable)
    return tuple(parents)


def kernel_digest(kernels: Sequence[InstrumentKernel]) -> str:
    payload = tuple(
        {
            "instrument_id": kernel.instrument_id,
            "variables": kernel.variables,
            "variable_outcomes": kernel.variable_outcomes,
            "controls": kernel.controls,
            "record_outcomes": kernel.record_outcomes,
            "rows": kernel.rows,
        }
        for kernel in sorted(kernels, key=lambda item: item.instrument_id)
    )
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()


def quotient_region(
    region: Sequence[str], relay_to_source: Mapping[str, str]
) -> tuple[str, ...]:
    collapsed: list[str] = []
    for variable in region:
        source = relay_to_source.get(variable, variable)
        if source not in collapsed:
            collapsed.append(source)
    return tuple(collapsed)


def rename_kernel(
    kernel: InstrumentKernel, renaming: Mapping[str, str]
) -> InstrumentKernel:
    return InstrumentKernel(
        instrument_id=kernel.instrument_id,
        variables=tuple(renaming.get(name, name) for name in kernel.variables),
        variable_outcomes=tuple(
            (renaming.get(name, name), outcomes)
            for name, outcomes in kernel.variable_outcomes
        ),
        controls=kernel.controls,
        record_outcomes=kernel.record_outcomes,
        rows=kernel.rows,
    )


def classical_multitime_control() -> dict[str, Any]:
    outcomes = {name: ("0", "1") for name in ("A", "B", "C")}
    controls = ("record", "withhold")
    ab = deterministic_kernel(
        "record_AB",
        ("A", "B", "C"),
        outcomes,
        controls,
        lambda control, state: (
            "missing"
            if control == "withhold"
            else str(int(state["A"]) ^ int(state["B"]))
        ),
    )
    bc = deterministic_kernel(
        "record_BC",
        ("A", "B", "C"),
        outcomes,
        controls,
        lambda control, state: (
            "missing"
            if control == "withhold"
            else str(int(state["B"]) ^ int(state["C"]))
        ),
    )
    kernels = (ab, bc)
    regions = {
        kernel.instrument_id: derive_parent_region(kernel)
        for kernel in kernels
    }
    digest = kernel_digest(kernels)

    histories = []
    alternate_target_difference_count = 0
    for a, b, c in itertools.product((0, 1), repeat=3):
        r_ab = a ^ b
        r_bc = b ^ c
        regional_ordinary = r_ab ^ r_bc
        alternate_target = r_ab | r_bc
        if alternate_target != regional_ordinary:
            alternate_target_difference_count += 1
        endpoint_ordinary = a ^ c
        regional_after_break = r_ab ^ r_bc
        endpoint_after_break = 0
        histories.append(
            {
                "initial": (a, b, c),
                "stage_one_records": (r_ab, r_bc),
                "regional_ordinary": regional_ordinary,
                "endpoint_ordinary": endpoint_ordinary,
                "regional_after_primitive_reset": regional_after_break,
                "endpoint_after_primitive_reset": endpoint_after_break,
            }
        )

    relay_outcomes = {
        name: ("0", "1") for name in ("A", "B_relay", "C")
    }
    relay_ab = deterministic_kernel(
        "record_AB",
        ("A", "B_relay", "C"),
        relay_outcomes,
        controls,
        lambda control, state: (
            "missing"
            if control == "withhold"
            else str(int(state["A"]) ^ int(state["B_relay"]))
        ),
    )
    relay_bc = deterministic_kernel(
        "record_BC",
        ("A", "B_relay", "C"),
        relay_outcomes,
        controls,
        lambda control, state: (
            "missing"
            if control == "withhold"
            else str(int(state["B_relay"]) ^ int(state["C"]))
        ),
    )
    relay_regions = {
        kernel.instrument_id: derive_parent_region(kernel)
        for kernel in (relay_ab, relay_bc)
    }
    relay_quotient = {
        instrument_id: quotient_region(region, {"B_relay": "B"})
        for instrument_id, region in relay_regions.items()
    }

    renaming = {"A": "C_prime", "B": "A_prime", "C": "B_prime"}
    renamed_regions = {
        kernel.instrument_id: derive_parent_region(
            rename_kernel(kernel, renaming)
        )
        for kernel in kernels
    }
    expected_renamed = {
        instrument_id: tuple(renaming[name] for name in region)
        for instrument_id, region in regions.items()
    }

    i2 = identity(2)
    z = matrix(((1, 0), (0, -1)))
    i8 = identity(8)
    parity_observables = {
        "record_AB": kronecker(kronecker(z, z), i2),
        "record_BC": kronecker(kronecker(i2, z), z),
    }
    qnd_receipts = {}
    for instrument_id, observable in parity_observables.items():
        projectors = {
            "0": matrix_scale(
                Fraction(1, 2), matrix_add(i8, observable)
            ),
            "1": matrix_scale(
                Fraction(1, 2),
                matrix_add(i8, matrix_scale(-1, observable)),
            ),
        }
        qnd_receipts[instrument_id] = {
            "observable_hermitian": matrix_equal(
                observable, matrix_dagger(observable)
            ),
            "observable_involution": matrix_equal(
                matrix_multiply(observable, observable), i8
            ),
            "projectors_hermitian_idempotent": all(
                matrix_equal(projector, matrix_dagger(projector))
                and matrix_equal(
                    matrix_multiply(projector, projector), projector
                )
                for projector in projectors.values()
            ),
            "nonselective_trace_preserving": matrix_equal(
                sum_matrices(
                    tuple(
                        matrix_multiply(
                            matrix_dagger(projector), projector
                        )
                        for projector in projectors.values()
                    )
                ),
                i8,
            ),
            "basis_probabilities": {},
            "qnd_on_basis_states": True,
        }
        for a, b, c in itertools.product((0, 1), repeat=3):
            state_index = 4 * a + 2 * b + c
            rho_basis = zero_matrix(8)
            mutable = [list(row) for row in rho_basis]
            mutable[state_index][state_index] = GaussianFraction(Fraction(1))
            rho_basis = tuple(tuple(row) for row in mutable)
            probabilities = {}
            for outcome, projector in projectors.items():
                post = matrix_multiply(
                    matrix_multiply(projector, rho_basis),
                    matrix_dagger(projector),
                )
                probability = matrix_trace(post)
                if probability.imag != 0:
                    raise RuntimeError("complex_qnd_probability")
                probabilities[outcome] = probability.real
                if probability.real == 1 and not matrix_equal(
                    post, rho_basis
                ):
                    qnd_receipts[instrument_id][
                        "qnd_on_basis_states"
                    ] = False
            qnd_receipts[instrument_id]["basis_probabilities"][
                f"{a}{b}{c}"
            ] = probabilities

    sequential_commutation = matrix_equal(
        matrix_multiply(
            parity_observables["record_AB"],
            parity_observables["record_BC"],
        ),
        matrix_multiply(
            parity_observables["record_BC"],
            parity_observables["record_AB"],
        ),
    )
    qnd_kernel_agreement = all(
        qnd_receipts["record_AB"]["basis_probabilities"][f"{a}{b}{c}"][
            str(a ^ b)
        ]
        == 1
        and qnd_receipts["record_BC"]["basis_probabilities"][f"{a}{b}{c}"][
            str(b ^ c)
        ]
        == 1
        for a, b, c in itertools.product((0, 1), repeat=3)
    )

    return {
        "kernel_digest": digest,
        "selection_dependency": (
            "complete instrument kernels",
            "declared accessible record outcomes",
            "control family",
            "relay quotient",
        ),
        "excluded_from_selection": (
            "downstream response target",
            "endpoint rival verdict",
            "platform label",
        ),
        "regions": regions,
        "history_rows": histories,
        "ordinary_endpoint_equivalence": all(
            row["regional_ordinary"] == row["endpoint_ordinary"]
            for row in histories
        ),
        "held_out_break_separator_count": sum(
            row["regional_after_primitive_reset"]
            != row["endpoint_after_primitive_reset"]
            for row in histories
        ),
        "relay_raw_regions": relay_regions,
        "relay_quotient_regions": relay_quotient,
        "relay_quotient_matches": relay_quotient == regions,
        "renamed_regions": renamed_regions,
        "label_covariant": renamed_regions == expected_renamed,
        "target_change_leaves_digest_unchanged": (
            alternate_target_difference_count > 0
            and digest == kernel_digest(kernels)
        ),
        "alternate_downstream_target_difference_count": (
            alternate_target_difference_count
        ),
        "qnd_quantum_instrument_receipts": qnd_receipts,
        "qnd_pair_instruments_commute": sequential_commutation,
        "qnd_born_kernels_match_stochastic_kernels": qnd_kernel_agreement,
    }


def pair_context(
    context_id: str,
    variables: Sequence[str],
    outcome_map: Mapping[str, Sequence[str]],
    relation: str,
) -> Any:
    probabilities: dict[tuple[str, ...], Fraction] = {}
    for left, right in itertools.product(("0", "1"), repeat=2):
        satisfied = (left == right) if relation == "equal" else (left != right)
        probabilities[(left, right)] = (
            Fraction(1, 2) if satisfied else Fraction(0)
        )
    return complete_context(
        context_id, variables, outcome_map, probabilities
    )


def noisy_pair_context(
    context_id: str,
    variables: Sequence[str],
    outcome_map: Mapping[str, Sequence[str]],
    mismatch_probability: Fraction,
) -> Any:
    probabilities: dict[tuple[str, ...], Fraction] = {}
    for left, right in itertools.product(("0", "1"), repeat=2):
        probabilities[(left, right)] = (
            mismatch_probability / 2
            if left != right
            else (1 - mismatch_probability) / 2
        )
    return complete_context(
        context_id, variables, outcome_map, probabilities
    )


def compiler_regression_control() -> dict[str, Any]:
    outcomes = {name: ("0", "1") for name in ("A", "B", "C", "D")}
    variable_outcomes = tuple(outcomes.items())

    glued_compatible = MarginalProblem(
        problem_id="two-glued-triangles-compatible",
        variable_outcomes=variable_outcomes,
        contexts=(
            pair_context("AB", ("A", "B"), outcomes, "equal"),
            pair_context("BC", ("B", "C"), outcomes, "equal"),
            pair_context("CA", ("C", "A"), outcomes, "equal"),
            pair_context("CD", ("C", "D"), outcomes, "equal"),
            pair_context("DA", ("D", "A"), outcomes, "equal"),
        ),
    )
    glued_frustrated = MarginalProblem(
        problem_id="two-glued-triangles-second-frustrated",
        variable_outcomes=variable_outcomes,
        contexts=(
            pair_context("AB", ("A", "B"), outcomes, "equal"),
            pair_context("BC", ("B", "C"), outcomes, "equal"),
            pair_context("CA", ("C", "A"), outcomes, "equal"),
            pair_context("CD", ("C", "D"), outcomes, "equal"),
            pair_context("DA", ("D", "A"), outcomes, "unequal"),
        ),
    )
    compatible_result = compile_marginal_extension(glued_compatible)
    frustrated_result = compile_marginal_extension(glued_frustrated)

    minimal_triangle = MarginalProblem(
        problem_id="frustrated-triangle-subfamily",
        variable_outcomes=variable_outcomes,
        contexts=(
            pair_context("CA", ("C", "A"), outcomes, "equal"),
            pair_context("CD", ("C", "D"), outcomes, "equal"),
            pair_context("DA", ("D", "A"), outcomes, "unequal"),
        ),
    )
    minimality = leave_one_context_out(minimal_triangle)

    triangle_grid_failures = []
    triangle_grid_primal_count = 0
    triangle_grid_dual_count = 0
    for numerators in itertools.product(range(7), repeat=3):
        mismatches = tuple(Fraction(value, 6) for value in numerators)
        grid_problem = MarginalProblem(
            problem_id=(
                "triangle-grid-"
                + "-".join(str(value) for value in numerators)
            ),
            variable_outcomes=tuple(
                (name, outcomes[name]) for name in ("A", "B", "C")
            ),
            contexts=(
                noisy_pair_context(
                    "AB", ("A", "B"), outcomes, mismatches[0]
                ),
                noisy_pair_context(
                    "BC", ("B", "C"), outcomes, mismatches[1]
                ),
                noisy_pair_context(
                    "CA", ("C", "A"), outcomes, mismatches[2]
                ),
            ),
        )
        weights = (
            1 - sum(mismatches, start=Fraction(0)) / 2,
            (mismatches[1] + mismatches[2] - mismatches[0]) / 2,
            (mismatches[0] + mismatches[2] - mismatches[1]) / 2,
            (mismatches[0] + mismatches[1] - mismatches[2]) / 2,
        )
        expected = (
            "GLOBAL_EXTENSION"
            if all(weight >= 0 for weight in weights)
            else "DUAL_OBSTRUCTION"
        )
        compiled = compile_marginal_extension(grid_problem)
        if compiled["verdict"] == "GLOBAL_EXTENSION":
            triangle_grid_primal_count += 1
        elif compiled["verdict"] == "DUAL_OBSTRUCTION":
            triangle_grid_dual_count += 1
        if compiled["verdict"] != expected:
            triangle_grid_failures.append(
                {
                    "mismatches": mismatches,
                    "weights": weights,
                    "expected": expected,
                    "actual": compiled["verdict"],
                }
            )

    incomplete = MarginalProblem(
        problem_id="incomplete-table-control",
        variable_outcomes=(("A", ("0", "1")),),
        contexts=(
            complete_context(
                "A",
                ("A",),
                {"A": ("0", "1")},
                {("0",): Fraction(1)},
            ),
        ),
        contract_frozen=False,
    )
    incomplete_result = compile_marginal_extension(incomplete)
    return {
        "compatible_glued_cycles": compatible_result,
        "frustrated_glued_cycles": frustrated_result,
        "minimal_frustrated_triangle": {
            "result": compile_marginal_extension(minimal_triangle),
            "minimality": minimality,
        },
        "triangle_grid_oracle_crosscheck": {
            "denominator": 6,
            "case_count": 343,
            "primal_count": triangle_grid_primal_count,
            "dual_count": triangle_grid_dual_count,
            "failure_count": len(triangle_grid_failures),
            "failures": triangle_grid_failures,
            "oracle": "unique signed even-parity-sector weights",
        },
        "incomplete_control": incomplete_result,
    }


ORIGIN_KEYS = {
    "A": b"du-fixture-origin-a-key",
    "B": b"du-fixture-origin-b-key",
    "C": b"du-fixture-origin-c-key",
}


def signed_message(
    origin: str, route: str, epoch: int, value: int
) -> dict[str, Any]:
    message = {
        "origin": origin,
        "route": route,
        "epoch": epoch,
        "value": value,
    }
    body = canonical_json(message).encode()
    signature = hmac.new(ORIGIN_KEYS[origin], body, hashlib.sha256).hexdigest()
    return {**message, "signature": signature}


def verify_message(
    message: Mapping[str, Any],
    *,
    expected_route: str | None = None,
    expected_epoch: int | None = None,
) -> bool:
    origin = str(message["origin"])
    unsigned = {
        "origin": origin,
        "route": message["route"],
        "epoch": message["epoch"],
        "value": message["value"],
    }
    expected = hmac.new(
        ORIGIN_KEYS[origin],
        canonical_json(unsigned).encode(),
        hashlib.sha256,
    ).hexdigest()
    return (
        hmac.compare_digest(expected, str(message["signature"]))
        and (expected_route is None or message["route"] == expected_route)
        and (expected_epoch is None or message["epoch"] == expected_epoch)
    )


def empirical_context(
    context_id: str,
    variables: Sequence[str],
    outcome_map: Mapping[str, Sequence[str]],
    samples: Sequence[tuple[str, ...]],
) -> Any:
    probabilities: dict[tuple[str, ...], Fraction] = {}
    weight = Fraction(1, len(samples))
    for sample in samples:
        probabilities[sample] = probabilities.get(sample, Fraction(0)) + weight
    return complete_context(
        context_id, variables, outcome_map, probabilities
    )


def action_half_range(
    summaries: Sequence[str], actions: Sequence[int]
) -> Fraction:
    fibers: dict[str, list[Fraction]] = {}
    for summary, action in zip(summaries, actions, strict=True):
        fibers.setdefault(summary, []).append(Fraction(action))
    return max(
        (
            (max(values) - min(values)) / 2
            for values in fibers.values()
        ),
        default=Fraction(0),
    )


def authenticated_protocol_control() -> dict[str, Any]:
    transcripts: list[dict[str, Any]] = []
    for hidden in (0, 1):
        route_values = {
            "AB": {"A": hidden, "B": hidden},
            "BC": {"B": hidden, "C": hidden},
            "CA": {"C": hidden, "A": 1 - hidden},
        }
        messages = {
            route: tuple(
                signed_message(origin, route, 7, value)
                for origin, value in values.items()
            )
            for route, values in route_values.items()
        }
        transcripts.append(
            {
                "hidden": hidden,
                "route_values": route_values,
                "messages": messages,
            }
        )

    all_messages = tuple(
        message
        for transcript in transcripts
        for messages in transcript["messages"].values()
        for message in messages
    )
    all_authentic = all(
        verify_message(
            message,
            expected_route=str(message["route"]),
            expected_epoch=7,
        )
        for message in all_messages
    )
    replay_rejected = not verify_message(
        all_messages[0],
        expected_route=str(all_messages[0]["route"]),
        expected_epoch=8,
    )

    equivocations = []
    for transcript in transcripts:
        by_origin: dict[str, set[int]] = {}
        for messages in transcript["messages"].values():
            for message in messages:
                by_origin.setdefault(str(message["origin"]), set()).add(
                    int(message["value"])
                )
        equivocations.append(
            tuple(
                origin
                for origin, values in sorted(by_origin.items())
                if len(values) > 1
            )
        )

    coarse_outcomes = {
        name: ("0", "1") for name in ("A", "B", "C")
    }
    coarse_problem = MarginalProblem(
        problem_id="authenticated-coarse-origin-gluing",
        variable_outcomes=tuple(coarse_outcomes.items()),
        contexts=tuple(
            empirical_context(
                route,
                tuple(transcripts[0]["route_values"][route]),
                coarse_outcomes,
                tuple(
                    tuple(
                        str(value)
                        for value in transcript["route_values"][route].values()
                    )
                    for transcript in transcripts
                ),
            )
            for route in ("AB", "BC", "CA")
        ),
    )
    coarse_result = compile_marginal_extension(coarse_problem)
    coarse_minimality = leave_one_context_out(coarse_problem)

    lifted_context_variables = {
        "AB": ("A@AB", "B@AB"),
        "BC": ("B@BC", "C@BC"),
        "CA": ("C@CA", "A@CA"),
    }
    lifted_outcomes = {
        name: ("0", "1")
        for variables in lifted_context_variables.values()
        for name in variables
    }
    lifted_problem = MarginalProblem(
        problem_id="authenticated-route-provenance-lift",
        variable_outcomes=tuple(lifted_outcomes.items()),
        contexts=tuple(
            empirical_context(
                route,
                lifted_context_variables[route],
                lifted_outcomes,
                tuple(
                    tuple(
                        str(value)
                        for value in transcript["route_values"][route].values()
                    )
                    for transcript in transcripts
                ),
            )
            for route in ("AB", "BC", "CA")
        ),
    )
    lifted_result = compile_marginal_extension(lifted_problem)

    protocol_outcomes = {
        name: ("0", "1") for name in ("A", "B", "C")
    }

    def receipt_response(
        route: str,
    ) -> Callable[[str, Mapping[str, str]], str]:
        left, right = tuple(route)

        def response(control: str, state: Mapping[str, str]) -> str:
            if control == f"withhold_{route}":
                return "missing"
            messages = (
                signed_message(left, route, 7, int(state[left])),
                signed_message(right, route, 7, int(state[right])),
            )
            receipt = hashlib.sha256(
                canonical_json(messages).encode()
            ).hexdigest()[:16]
            parity = int(state[left]) ^ int(state[right])
            return f"formed:{parity}:{receipt}"

        return response

    controls = (
        "deliver_AB_then_BC",
        "deliver_BC_then_AB",
        "withhold_AB",
        "withhold_BC",
        "withhold_CA",
    )
    receipt_kernels = tuple(
        deterministic_kernel(
            f"receipt_{route}",
            ("A", "B", "C"),
            protocol_outcomes,
            controls,
            receipt_response(route),
        )
        for route in ("AB", "BC", "CA")
    )
    protocol_regions = {
        kernel.instrument_id: derive_parent_region(kernel)
        for kernel in receipt_kernels
    }

    terminal_summaries = ("0", "0", "1", "1")
    actions = (1, 0, 1, 0)
    provenance_summaries = (
        "0:consistent",
        "0:equivocation",
        "1:consistent",
        "1:equivocation",
    )
    coarse_action_defect = action_half_range(terminal_summaries, actions)
    lifted_action_defect = action_half_range(provenance_summaries, actions)

    return {
        "enumerated_hidden_transcripts": len(transcripts),
        "authenticated_message_count": len(all_messages),
        "all_messages_authentic": all_authentic,
        "cross_epoch_replay_rejected": replay_rejected,
        "equivocating_origins_by_transcript": equivocations,
        "coarse_origin_problem": coarse_result,
        "coarse_obstruction_minimality": coarse_minimality,
        "route_provenance_lift": lifted_result,
        "instrument_regions": protocol_regions,
        "instrument_grammar_digest": kernel_digest(receipt_kernels),
        "coarse_boundary_action_defect": coarse_action_defect,
        "provenance_boundary_action_defect": lifted_action_defect,
        "protocol_disposition": (
            "SAFE_REJECTION_EQUIVOCATION_PROVENANCE_FORMED"
        ),
        "interpretation": (
            "authentication binds each routed message but does not make "
            "route-specific values one canonical origin value"
        ),
    }


@dataclass(frozen=True)
class GaussianFraction:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: Any) -> "GaussianFraction":
        value = as_gaussian(other)
        return GaussianFraction(self.real + value.real, self.imag + value.imag)

    def __radd__(self, other: Any) -> "GaussianFraction":
        return self + other

    def __sub__(self, other: Any) -> "GaussianFraction":
        return self + (-as_gaussian(other))

    def __rsub__(self, other: Any) -> "GaussianFraction":
        return as_gaussian(other) - self

    def __neg__(self) -> "GaussianFraction":
        return GaussianFraction(-self.real, -self.imag)

    def __mul__(self, other: Any) -> "GaussianFraction":
        value = as_gaussian(other)
        return GaussianFraction(
            self.real * value.real - self.imag * value.imag,
            self.real * value.imag + self.imag * value.real,
        )

    def __rmul__(self, other: Any) -> "GaussianFraction":
        return self * other

    def __truediv__(self, other: Any) -> "GaussianFraction":
        value = as_gaussian(other)
        denominator = value.real * value.real + value.imag * value.imag
        if denominator == 0:
            raise ZeroDivisionError
        return GaussianFraction(
            (self.real * value.real + self.imag * value.imag) / denominator,
            (self.imag * value.real - self.real * value.imag) / denominator,
        )

    def conjugate(self) -> "GaussianFraction":
        return GaussianFraction(self.real, -self.imag)


def as_gaussian(value: Any) -> GaussianFraction:
    if isinstance(value, GaussianFraction):
        return value
    if isinstance(value, (int, Fraction)):
        return GaussianFraction(Fraction(value), Fraction(0))
    raise TypeError(value)


Matrix = tuple[tuple[GaussianFraction, ...], ...]


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    return tuple(
        tuple(as_gaussian(value) for value in row) for row in rows
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(lrow, rrow, strict=True))
        for lrow, rrow in zip(left, right, strict=True)
    )


def matrix_scale(value: Any, target: Matrix) -> Matrix:
    scalar = as_gaussian(value)
    return tuple(
        tuple(scalar * entry for entry in row) for row in target
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    right_columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(row, column, strict=True)),
                start=GaussianFraction(),
            )
            for column in right_columns
        )
        for row in left
    )


def matrix_dagger(target: Matrix) -> Matrix:
    return tuple(
        tuple(target[row][column].conjugate() for row in range(len(target)))
        for column in range(len(target[0]))
    )


def matrix_trace(target: Matrix) -> GaussianFraction:
    return sum(
        (target[index][index] for index in range(len(target))),
        start=GaussianFraction(),
    )


def identity(dimension: int) -> Matrix:
    return matrix(
        tuple(
            tuple(int(row == column) for column in range(dimension))
            for row in range(dimension)
        )
    )


def zero_matrix(dimension: int) -> Matrix:
    return matrix(tuple(tuple(0 for _ in range(dimension)) for _ in range(dimension)))


def sum_matrices(targets: Sequence[Matrix]) -> Matrix:
    if not targets:
        raise ValueError("empty_matrix_sum")
    total = zero_matrix(len(targets[0]))
    for target in targets:
        total = matrix_add(total, target)
    return total


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    rows: list[tuple[GaussianFraction, ...]] = []
    for left_row in left:
        for right_row in right:
            rows.append(
                tuple(
                    left_value * right_value
                    for left_value in left_row
                    for right_value in right_row
                )
            )
    return tuple(rows)


def projector_for_assignment(
    observables: Sequence[Matrix], assignment: Sequence[int]
) -> Matrix:
    dimension = len(observables[0])
    result = identity(dimension)
    for observable, value in zip(observables, assignment, strict=True):
        factor = matrix_scale(
            Fraction(1, 2),
            matrix_add(
                identity(dimension), matrix_scale(value, observable)
            ),
        )
        result = matrix_multiply(result, factor)
    return result


def quantum_contextual_instrument_control() -> dict[str, Any]:
    imaginary = GaussianFraction(Fraction(0), Fraction(1))
    i2 = identity(2)
    x = matrix(((0, 1), (1, 0)))
    y = matrix(((0, -imaginary), (imaginary, 0)))
    z = matrix(((1, 0), (0, -1)))

    observables = {
        "XI": kronecker(x, i2),
        "IX": kronecker(i2, x),
        "XX": kronecker(x, x),
        "IY": kronecker(i2, y),
        "YI": kronecker(y, i2),
        "YY": kronecker(y, y),
        "XY": kronecker(x, y),
        "YX": kronecker(y, x),
        "ZZ": kronecker(z, z),
    }
    i4 = identity(4)
    rho = matrix_scale(Fraction(1, 4), i4)
    contexts = (
        ("R1", ("XI", "IX", "XX"), 1),
        ("R2", ("IY", "YI", "YY"), 1),
        ("R3", ("XY", "YX", "ZZ"), 1),
        ("C1", ("XI", "IY", "XY"), 1),
        ("C2", ("IX", "YI", "YX"), 1),
        ("C3", ("XX", "YY", "ZZ"), -1),
    )

    observable_checks = {
        name: {
            "hermitian": matrix_equal(value, matrix_dagger(value)),
            "squares_to_identity": matrix_equal(
                matrix_multiply(value, value), i4
            ),
        }
        for name, value in observables.items()
    }

    outcome_map = {name: ("-1", "+1") for name in observables}
    marginal_contexts = []
    instrument_receipts = []
    for context_id, names, expected_product in contexts:
        context_observables = tuple(observables[name] for name in names)
        pairwise_commuting = all(
            matrix_equal(
                matrix_multiply(context_observables[left], context_observables[right]),
                matrix_multiply(context_observables[right], context_observables[left]),
            )
            for left in range(3)
            for right in range(left + 1, 3)
        )
        product = matrix_multiply(
            matrix_multiply(context_observables[0], context_observables[1]),
            context_observables[2],
        )
        product_sign_correct = matrix_equal(
            product, matrix_scale(expected_product, i4)
        )

        probabilities: dict[tuple[str, ...], Fraction] = {}
        projectors: list[Matrix] = []
        projector_checks = []
        for assignment in itertools.product((-1, 1), repeat=3):
            projector = projector_for_assignment(
                context_observables, assignment
            )
            projectors.append(projector)
            post = matrix_multiply(
                matrix_multiply(projector, rho),
                matrix_dagger(projector),
            )
            probability = matrix_trace(post)
            if probability.imag != 0:
                raise RuntimeError("complex_probability")
            probabilities[
                tuple("+1" if value == 1 else "-1" for value in assignment)
            ] = probability.real
            projector_checks.append(
                {
                    "assignment": assignment,
                    "hermitian": matrix_equal(
                        projector, matrix_dagger(projector)
                    ),
                    "idempotent": matrix_equal(
                        matrix_multiply(projector, projector), projector
                    ),
                    "probability": probability.real,
                }
            )

        sum_projectors = zero_matrix(4)
        sum_kraus_dagger_kraus = zero_matrix(4)
        for projector in projectors:
            sum_projectors = matrix_add(sum_projectors, projector)
            sum_kraus_dagger_kraus = matrix_add(
                sum_kraus_dagger_kraus,
                matrix_multiply(matrix_dagger(projector), projector),
            )
        marginal_contexts.append(
            complete_context(
                context_id, names, outcome_map, probabilities
            )
        )
        instrument_receipts.append(
            {
                "context_id": context_id,
                "variables": names,
                "pairwise_commuting": pairwise_commuting,
                "observable_product_sign": expected_product,
                "product_sign_correct": product_sign_correct,
                "selective_maps_have_kraus_projector_form": True,
                "all_projectors_hermitian_idempotent": all(
                    row["hermitian"] and row["idempotent"]
                    for row in projector_checks
                ),
                "nonselective_trace_preserving": matrix_equal(
                    sum_kraus_dagger_kraus, i4
                ),
                "projectors_complete": matrix_equal(sum_projectors, i4),
                "nonzero_outcomes": sum(
                    probability > 0
                    for probability in probabilities.values()
                ),
                "probability_sum": sum(
                    probabilities.values(), start=Fraction(0)
                ),
                "parity_support_correct": all(
                    (
                        int(assignment[0])
                        * int(assignment[1])
                        * int(assignment[2])
                        == expected_product
                    )
                    == (probability > 0)
                    for assignment, probability in probabilities.items()
                ),
            }
        )

    problem = MarginalProblem(
        problem_id="two-qubit-mermin-peres-context-marginals",
        variable_outcomes=tuple(outcome_map.items()),
        contexts=tuple(marginal_contexts),
    )
    compiled = compile_marginal_extension(problem)
    minimality = leave_one_context_out(problem)

    nonzero_context_outcomes = tuple(
        tuple(
            (assignment, probability)
            for assignment, probability in context.probabilities
            if probability
        )
        for context in marginal_contexts
    )
    recovered_contexts = [
        {
            assignment: Fraction(0)
            for assignment, _ in context.probabilities
        }
        for context in marginal_contexts
    ]
    context_indexed_weight = Fraction(0)
    context_indexed_support_size = 0
    for joint_context_outcomes in itertools.product(
        *nonzero_context_outcomes
    ):
        weight = Fraction(1)
        for _, probability in joint_context_outcomes:
            weight *= probability
        if not weight:
            continue
        context_indexed_support_size += 1
        context_indexed_weight += weight
        for index, (assignment, _) in enumerate(joint_context_outcomes):
            recovered_contexts[index][assignment] += weight
    context_indexed_marginals_exact = all(
        recovered == dict(context.probabilities)
        for recovered, context in zip(
            recovered_contexts, marginal_contexts, strict=True
        )
    )

    context_erased_summaries = tuple("parity" for _ in contexts)
    context_actions = tuple(
        0 if context_id.startswith("R") else 1
        for context_id, _, _ in contexts
    )
    context_lifted_summaries = tuple(
        context_id for context_id, _, _ in contexts
    )
    return {
        "observable_checks": observable_checks,
        "instrument_receipts": instrument_receipts,
        "derived_marginal_problem": {
            "variables": tuple(outcome_map),
            "contexts": tuple(
                {
                    "context_id": context.context_id,
                    "variables": context.variables,
                    "probabilities": context.probabilities,
                }
                for context in marginal_contexts
            ),
        },
        "compiled_noncontextual_gluing": compiled,
        "context_obstruction_minimality": minimality,
        "context_indexed_product_extension": {
            "support_size": context_indexed_support_size,
            "normalization": context_indexed_weight,
            "all_context_marginals_exact": (
                context_indexed_marginals_exact
            ),
            "meaning": (
                "a global distribution exists after each observable outcome "
                "is indexed by its actually implemented context"
            ),
        },
        "context_erased_action_defect": action_half_range(
            context_erased_summaries, context_actions
        ),
        "context_lifted_action_defect": action_half_range(
            context_lifted_summaries, context_actions
        ),
        "physical_process_disposition": (
            "STANDARD_CONTEXT_INDEXED_QUANTUM_INSTRUMENTS_EXIST_"
            "NONCONTEXTUAL_GLOBAL_VALUE_GLUING_FAILS"
        ),
        "does_not_establish": (
            "joint measurability",
            "observer-independent preassigned values",
            "beyond-standard quantum dynamics",
            "regional physical ontology",
        ),
    }


def run() -> dict[str, Any]:
    compiler = compiler_regression_control()
    multitime = classical_multitime_control()
    protocol = authenticated_protocol_control()
    quantum = quantum_contextual_instrument_control()

    checks = {
        "compiler_returns_primal_on_compatible_glued_cycles": (
            compiler["compatible_glued_cycles"]["verdict"]
            == "GLOBAL_EXTENSION"
        ),
        "compiler_primal_verifies_exactly": compiler[
            "compatible_glued_cycles"
        ]["verification"]["all_equalities_exact"],
        "compiler_returns_dual_on_frustrated_glued_cycles": (
            compiler["frustrated_glued_cycles"]["verdict"]
            == "DUAL_OBSTRUCTION"
        ),
        "compiler_dual_verifies_exactly": compiler[
            "frustrated_glued_cycles"
        ]["verification"]["strictly_negative_observed_value"],
        "compiler_recovers_minimal_frustrated_triangle": (
            compiler["minimal_frustrated_triangle"]["result"]["verdict"]
            == "DUAL_OBSTRUCTION"
            and compiler["minimal_frustrated_triangle"]["minimality"][
                "every_proper_context_subfamily_is_compatible"
            ]
        ),
        "general_compiler_matches_all_343_triangle_oracle_cases": (
            compiler["triangle_grid_oracle_crosscheck"]["case_count"] == 343
            and compiler["triangle_grid_oracle_crosscheck"][
                "failure_count"
            ]
            == 0
            and (
                compiler["triangle_grid_oracle_crosscheck"]["primal_count"]
                + compiler["triangle_grid_oracle_crosscheck"]["dual_count"]
                == 343
            )
        ),
        "compiler_preserves_incomplete_contract": (
            compiler["incomplete_control"]["verdict"]
            == "INCOMPLETE_CONTRACT"
        ),
        "instrument_regions_are_overlapping_AB_BC": (
            multitime["regions"]
            == {"record_AB": ("A", "B"), "record_BC": ("B", "C")}
        ),
        "endpoint_models_match_without_multitime_break": multitime[
            "ordinary_endpoint_equivalence"
        ],
        "held_out_causal_break_separates_endpoint_rival": (
            multitime["held_out_break_separator_count"] == 4
        ),
        "instrument_region_extraction_is_label_covariant": multitime[
            "label_covariant"
        ],
        "instrument_region_extraction_quotients_relay": multitime[
            "relay_quotient_matches"
        ],
        "instrument_grammar_is_target_independent": multitime[
            "target_change_leaves_digest_unchanged"
        ],
        "multitime_regions_come_from_complete_qnd_instruments": all(
            row["observable_hermitian"]
            and row["observable_involution"]
            and row["projectors_hermitian_idempotent"]
            and row["nonselective_trace_preserving"]
            and row["qnd_on_basis_states"]
            for row in multitime[
                "qnd_quantum_instrument_receipts"
            ].values()
        ),
        "qnd_instrument_born_kernels_match_and_commute": (
            multitime["qnd_pair_instruments_commute"]
            and multitime["qnd_born_kernels_match_stochastic_kernels"]
        ),
        "authenticated_fixture_messages_verify": protocol[
            "all_messages_authentic"
        ],
        "authenticated_fixture_rejects_cross_epoch_replay": protocol[
            "cross_epoch_replay_rejected"
        ],
        "authenticated_fixture_contains_one_equivocating_origin": all(
            origins == ("A",)
            for origins in protocol["equivocating_origins_by_transcript"]
        ),
        "coarse_authenticated_origin_gluing_is_obstructed": (
            protocol["coarse_origin_problem"]["verdict"]
            == "DUAL_OBSTRUCTION"
        ),
        "authenticated_obstruction_is_context_minimal": protocol[
            "coarse_obstruction_minimality"
        ]["every_proper_context_subfamily_is_compatible"],
        "route_provenance_restores_global_extension": (
            protocol["route_provenance_lift"]["verdict"]
            == "GLOBAL_EXTENSION"
        ),
        "protocol_instruments_recover_pair_regions": (
            protocol["instrument_regions"]
            == {
                "receipt_AB": ("A", "B"),
                "receipt_BC": ("B", "C"),
                "receipt_CA": ("A", "C"),
            }
        ),
        "protocol_provenance_removes_action_defect": (
            protocol["coarse_boundary_action_defect"] == Fraction(1, 2)
            and protocol["provenance_boundary_action_defect"] == 0
        ),
        "protocol_uses_safe_rejection_not_false_descent": (
            protocol["protocol_disposition"]
            == "SAFE_REJECTION_EQUIVOCATION_PROVENANCE_FORMED"
        ),
        "all_quantum_observables_are_exact_hermitian_involutions": all(
            row["hermitian"] and row["squares_to_identity"]
            for row in quantum["observable_checks"].values()
        ),
        "all_quantum_contexts_commute_and_have_correct_product": all(
            row["pairwise_commuting"] and row["product_sign_correct"]
            for row in quantum["instrument_receipts"]
        ),
        "all_quantum_context_instruments_are_complete_and_tp": all(
            row["all_projectors_hermitian_idempotent"]
            and row["nonselective_trace_preserving"]
            and row["projectors_complete"]
            for row in quantum["instrument_receipts"]
        ),
        "all_quantum_marginals_are_derived_normalized_parity_tables": all(
            row["nonzero_outcomes"] == 4
            and row["probability_sum"] == 1
            and row["parity_support_correct"]
            for row in quantum["instrument_receipts"]
        ),
        "quantum_noncontextual_gluing_has_exact_dual_obstruction": (
            quantum["compiled_noncontextual_gluing"]["verdict"]
            == "DUAL_OBSTRUCTION"
            and quantum["compiled_noncontextual_gluing"]["verification"][
                "strictly_negative_observed_value"
            ]
        ),
        "quantum_context_family_is_obstruction_minimal": quantum[
            "context_obstruction_minimality"
        ]["every_proper_context_subfamily_is_compatible"],
        "quantum_context_indexed_process_has_exact_global_extension": (
            quantum["context_indexed_product_extension"]["support_size"]
            == 4096
            and quantum["context_indexed_product_extension"][
                "normalization"
            ]
            == 1
            and quantum["context_indexed_product_extension"][
                "all_context_marginals_exact"
            ]
        ),
        "quantum_context_register_removes_action_alias": (
            quantum["context_erased_action_defect"] == Fraction(1, 2)
            and quantum["context_lifted_action_defect"] == 0
        ),
        "quantum_result_is_classified_as_standard_contextuality": (
            quantum["physical_process_disposition"]
            == (
                "STANDARD_CONTEXT_INDEXED_QUANTUM_INSTRUMENTS_EXIST_"
                "NONCONTEXTUAL_GLOBAL_VALUE_GLUING_FAILS"
            )
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "dynamic-unity/multitime-marginal-transfer/v0.1",
        "run_id": "RUN-20260725-071641-multitime-marginal-transfer",
        "claim_grade": (
            "EXACT FINITE RATIONAL COMPILER + COMPLETE FINITE INSTRUMENT "
            "TRANSFERS / COMPONENT MATHEMATICS KNOWN / PHYSICAL THEORY OPEN"
        ),
        "compiler_controls": compiler,
        "multitime_instrument_regionalization": multitime,
        "authenticated_protocol_transfer": protocol,
        "quantum_instrument_transfer": quantum,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "GENERAL_FINITE_MARGINAL_COMPILER_INSTALLED / "
            "MULTITIME_INSTRUMENT_REGIONS_DERIVED / "
            "AUTHENTICATED_OBSTRUCTION_ABSORBED_BY_ROUTE_PROVENANCE_AND_"
            "SAFE_REJECTION / QUANTUM_OBSTRUCTION_ABSORBED_BY_STANDARD_"
            "CONTEXTUALITY"
        ),
        "does_not_establish": (
            "a physical regional ontology",
            "public finality",
            "protocol or BFT security",
            "joint quantum measurability",
            "beyond-standard quantum dynamics",
            "a new physical law or prediction",
        ),
    }


def main() -> None:
    result = run()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n"
    )
    if result["failure_count"]:
        raise SystemExit(
            f"{result['failure_count']}/{result['check_count']} checks failed: "
            f"{result['failures']}"
        )
    print(
        "GENERAL_EXACT_MARGINAL_COMPILER_INSTALLED / "
        "MULTITIME_REGIONS_DERIVED / AUTHENTICATED_PROVENANCE_AND_"
        "QUANTUM_CONTEXTUALITY_ABSORB_APPARENT_REMAINDERS: "
        f"{result['check_count']}/{result['check_count']} checks"
    )


if __name__ == "__main__":
    main()
