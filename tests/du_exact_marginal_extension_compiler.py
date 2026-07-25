#!/usr/bin/env python3
"""Exact finite rational marginal-extension compiler.

The compiler accepts arbitrary finite variables, arbitrary context
hypergraphs, and complete exact-rational local marginal tables.  It returns
one of:

* ``GLOBAL_EXTENSION`` with an explicit sparse joint distribution;
* ``DUAL_OBSTRUCTION`` with a Farkas vector ``y`` satisfying
  ``A^T y >= 0`` and ``b^T y < 0``; or
* ``INCOMPLETE_CONTRACT`` with validation failures.

The solver is an exact Phase-I simplex over ``fractions.Fraction``.  It uses
Bland entering/leaving rules and independently verifies every returned
certificate.  This is a finite compatibility adjudicator, not a claim that
the supplied variables are jointly measurable, physically identical across
contexts, or the correct ontology.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable, Mapping, Sequence


Assignment = tuple[str, ...]


@dataclass(frozen=True)
class MarginalContext:
    """One complete local marginal table on an ordered variable context."""

    context_id: str
    variables: tuple[str, ...]
    probabilities: tuple[tuple[Assignment, Fraction], ...]


@dataclass(frozen=True)
class MarginalProblem:
    """A frozen finite marginal-extension problem."""

    problem_id: str
    variable_outcomes: tuple[tuple[str, tuple[str, ...]], ...]
    contexts: tuple[MarginalContext, ...]
    contract_frozen: bool = True


def _product(values: Sequence[Sequence[str]]) -> tuple[Assignment, ...]:
    return tuple(itertools.product(*values))


def validate_problem(problem: MarginalProblem) -> tuple[str, ...]:
    errors: list[str] = []
    if not problem.contract_frozen:
        errors.append("contract_not_frozen")
    if not problem.problem_id:
        errors.append("missing_problem_id")
    if not problem.variable_outcomes:
        errors.append("empty_variable_set")

    variables = tuple(name for name, _ in problem.variable_outcomes)
    if len(set(variables)) != len(variables):
        errors.append("duplicate_variable")

    outcome_map: dict[str, tuple[str, ...]] = {}
    for name, outcomes in problem.variable_outcomes:
        if not name:
            errors.append("empty_variable_id")
        if not outcomes:
            errors.append(f"empty_outcome_alphabet:{name}")
        if len(set(outcomes)) != len(outcomes):
            errors.append(f"duplicate_outcome:{name}")
        outcome_map[name] = outcomes

    if not problem.contexts:
        errors.append("empty_context_set")
    context_ids = tuple(context.context_id for context in problem.contexts)
    if len(set(context_ids)) != len(context_ids):
        errors.append("duplicate_context_id")

    for context in problem.contexts:
        if not context.context_id:
            errors.append("empty_context_id")
        if not context.variables:
            errors.append(f"empty_context:{context.context_id}")
            continue
        if len(set(context.variables)) != len(context.variables):
            errors.append(f"duplicate_context_variable:{context.context_id}")
        unknown = tuple(
            variable
            for variable in context.variables
            if variable not in outcome_map
        )
        if unknown:
            errors.append(
                f"unknown_context_variables:{context.context_id}:{unknown}"
            )
            continue

        expected = set(
            _product(tuple(outcome_map[name] for name in context.variables))
        )
        supplied_assignments = tuple(
            assignment for assignment, _ in context.probabilities
        )
        supplied = set(supplied_assignments)
        if len(supplied) != len(supplied_assignments):
            errors.append(f"duplicate_assignment:{context.context_id}")
        if supplied != expected:
            missing = sorted(expected - supplied)
            extra = sorted(supplied - expected)
            errors.append(
                f"incomplete_table:{context.context_id}:"
                f"missing={missing}:extra={extra}"
            )
        if any(probability < 0 for _, probability in context.probabilities):
            errors.append(f"negative_probability:{context.context_id}")
        if (
            sum(
                (probability for _, probability in context.probabilities),
                start=Fraction(0),
            )
            != 1
        ):
            errors.append(f"not_normalized:{context.context_id}")

    return tuple(sorted(set(errors)))


def enumerate_global_states(problem: MarginalProblem) -> tuple[Assignment, ...]:
    return _product(
        tuple(outcomes for _, outcomes in problem.variable_outcomes)
    )


def build_marginal_system(
    problem: MarginalProblem,
) -> dict[str, Any]:
    """Build ``A q = b`` for the global joint distribution ``q``."""

    variables = tuple(name for name, _ in problem.variable_outcomes)
    variable_index = {name: index for index, name in enumerate(variables)}
    states = enumerate_global_states(problem)

    rows: list[tuple[Fraction, ...]] = []
    rhs: list[Fraction] = []
    row_ids: list[str] = []
    row_contexts: list[str] = []
    row_assignments: list[Assignment] = []

    for context in problem.contexts:
        indexes = tuple(variable_index[name] for name in context.variables)
        for assignment, probability in context.probabilities:
            row = tuple(
                Fraction(
                    tuple(state[index] for index in indexes) == assignment
                )
                for state in states
            )
            label = ",".join(
                f"{name}={value}"
                for name, value in zip(
                    context.variables, assignment, strict=True
                )
            )
            rows.append(row)
            rhs.append(probability)
            row_ids.append(f"{context.context_id}|{label}")
            row_contexts.append(context.context_id)
            row_assignments.append(assignment)

    return {
        "states": states,
        "rows": tuple(rows),
        "rhs": tuple(rhs),
        "row_ids": tuple(row_ids),
        "row_contexts": tuple(row_contexts),
        "row_assignments": tuple(row_assignments),
    }


def _dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def _phase_one_exact(
    matrix: Sequence[Sequence[Fraction]],
    rhs: Sequence[Fraction],
) -> dict[str, Any]:
    """Solve ``A x=b, x>=0`` and retain a primal or Farkas certificate."""

    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    if row_count == 0 or column_count == 0:
        raise ValueError("phase_one_requires_nonempty_matrix")
    if any(len(row) != column_count for row in matrix):
        raise ValueError("ragged_matrix")
    if len(rhs) != row_count:
        raise ValueError("rhs_arity")

    signs = tuple(Fraction(1) if value >= 0 else Fraction(-1) for value in rhs)
    normalized_rhs = [sign * value for sign, value in zip(signs, rhs, strict=True)]
    total_columns = column_count + row_count
    tableau: list[list[Fraction]] = []
    for row_index, row in enumerate(matrix):
        normalized = [signs[row_index] * value for value in row]
        normalized.extend(
            Fraction(int(row_index == artificial_index))
            for artificial_index in range(row_count)
        )
        tableau.append(normalized)

    basis = [column_count + index for index in range(row_count)]
    costs = [Fraction(0)] * column_count + [Fraction(-1)] * row_count
    iteration = 0
    maximum_iterations = 20 * total_columns * max(1, row_count)

    while True:
        basis_set = set(basis)
        basis_costs = [costs[index] for index in basis]
        reduced = [
            costs[column]
            - sum(
                (
                    basis_costs[row] * tableau[row][column]
                    for row in range(row_count)
                ),
                start=Fraction(0),
            )
            for column in range(total_columns)
        ]
        entering_candidates = [
            column
            for column in range(total_columns)
            if column not in basis_set and reduced[column] > 0
        ]
        if not entering_candidates:
            break

        entering = min(entering_candidates)
        leaving_candidates: list[tuple[Fraction, int, int]] = []
        for row_index in range(row_count):
            direction = tableau[row_index][entering]
            if direction > 0:
                leaving_candidates.append(
                    (
                        normalized_rhs[row_index] / direction,
                        basis[row_index],
                        row_index,
                    )
                )
        if not leaving_candidates:
            raise RuntimeError("phase_one_unbounded_internal_error")
        _, _, leaving_row = min(leaving_candidates)

        pivot = tableau[leaving_row][entering]
        tableau[leaving_row] = [
            value / pivot for value in tableau[leaving_row]
        ]
        normalized_rhs[leaving_row] /= pivot
        for row_index in range(row_count):
            if row_index == leaving_row:
                continue
            factor = tableau[row_index][entering]
            if factor == 0:
                continue
            tableau[row_index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(
                    tableau[row_index],
                    tableau[leaving_row],
                    strict=True,
                )
            ]
            normalized_rhs[row_index] -= (
                factor * normalized_rhs[leaving_row]
            )
        basis[leaving_row] = entering
        iteration += 1
        if iteration > maximum_iterations:
            raise RuntimeError("phase_one_iteration_bound")

    basis_costs = [costs[index] for index in basis]
    objective = _dot(basis_costs, normalized_rhs)
    if objective == 0:
        solution = [Fraction(0)] * column_count
        for row_index, basic_column in enumerate(basis):
            if basic_column < column_count:
                solution[basic_column] = normalized_rhs[row_index]
        return {
            "feasible": True,
            "solution": tuple(solution),
            "phase_one_objective": objective,
            "iterations": iteration,
            "basis": tuple(basis),
        }

    if objective > 0:
        raise RuntimeError("phase_one_positive_objective_internal_error")

    dual_normalized = tuple(
        sum(
            (
                basis_costs[row] * tableau[row][column_count + original_row]
                for row in range(row_count)
            ),
            start=Fraction(0),
        )
        for original_row in range(row_count)
    )
    dual = tuple(
        sign * value
        for sign, value in zip(signs, dual_normalized, strict=True)
    )
    return {
        "feasible": False,
        "dual": dual,
        "phase_one_objective": objective,
        "iterations": iteration,
        "basis": tuple(basis),
    }


def _normalized_integer_vector(
    values: Sequence[Fraction],
) -> tuple[int, ...]:
    denominator_lcm = 1
    for value in values:
        denominator_lcm = math.lcm(denominator_lcm, value.denominator)
    integers = [
        value.numerator * (denominator_lcm // value.denominator)
        for value in values
    ]
    divisor = 0
    for value in integers:
        divisor = math.gcd(divisor, abs(value))
    if divisor:
        integers = [value // divisor for value in integers]
    return tuple(integers)


def verify_primal(
    matrix: Sequence[Sequence[Fraction]],
    rhs: Sequence[Fraction],
    solution: Sequence[Fraction],
) -> dict[str, Any]:
    residuals = tuple(
        _dot(row, solution) - expected
        for row, expected in zip(matrix, rhs, strict=True)
    )
    return {
        "nonnegative": all(value >= 0 for value in solution),
        "all_equalities_exact": all(value == 0 for value in residuals),
        "maximum_absolute_residual": max(
            (abs(value) for value in residuals), default=Fraction(0)
        ),
        "normalization": sum(solution, start=Fraction(0)),
    }


def verify_dual(
    matrix: Sequence[Sequence[Fraction]],
    rhs: Sequence[Fraction],
    dual: Sequence[Fraction],
) -> dict[str, Any]:
    column_values = tuple(
        sum(
            (
                dual[row] * matrix[row][column]
                for row in range(len(matrix))
            ),
            start=Fraction(0),
        )
        for column in range(len(matrix[0]))
    )
    rhs_value = _dot(dual, rhs)
    return {
        "all_global_state_coefficients_nonnegative": all(
            value >= 0 for value in column_values
        ),
        "minimum_global_state_coefficient": min(column_values),
        "weighted_observed_value": rhs_value,
        "strictly_negative_observed_value": rhs_value < 0,
    }


def compile_marginal_extension(problem: MarginalProblem) -> dict[str, Any]:
    errors = validate_problem(problem)
    if errors:
        return {
            "schema": "dynamic-unity/exact-marginal-extension/v0.1",
            "problem_id": problem.problem_id,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": errors,
        }

    system = build_marginal_system(problem)
    result = _phase_one_exact(system["rows"], system["rhs"])
    common = {
        "schema": "dynamic-unity/exact-marginal-extension/v0.1",
        "problem_id": problem.problem_id,
        "variable_count": len(problem.variable_outcomes),
        "global_state_count": len(system["states"]),
        "context_count": len(problem.contexts),
        "constraint_count": len(system["rows"]),
        "simplex_iterations": result["iterations"],
        "solver": "exact_fraction_phase_one_simplex_bland",
    }

    if result["feasible"]:
        verification = verify_primal(
            system["rows"], system["rhs"], result["solution"]
        )
        if not (
            verification["nonnegative"]
            and verification["all_equalities_exact"]
            and verification["normalization"] == 1
        ):
            raise RuntimeError("invalid_primal_certificate")
        support = tuple(
            {
                "state": state,
                "probability": probability,
            }
            for state, probability in zip(
                system["states"], result["solution"], strict=True
            )
            if probability
        )
        return {
            **common,
            "verdict": "GLOBAL_EXTENSION",
            "support": support,
            "support_size": len(support),
            "verification": verification,
        }

    dual = result["dual"]
    verification = verify_dual(system["rows"], system["rhs"], dual)
    if not (
        verification["all_global_state_coefficients_nonnegative"]
        and verification["strictly_negative_observed_value"]
    ):
        raise RuntimeError("invalid_dual_certificate")
    integer_dual = _normalized_integer_vector(dual)
    sparse_dual = tuple(
        {
            "row_id": row_id,
            "context_id": context_id,
            "coefficient": coefficient,
        }
        for row_id, context_id, coefficient in zip(
            system["row_ids"],
            system["row_contexts"],
            integer_dual,
            strict=True,
        )
        if coefficient
    )
    integer_verification = verify_dual(
        system["rows"],
        system["rhs"],
        tuple(Fraction(value) for value in integer_dual),
    )
    if not (
        integer_verification[
            "all_global_state_coefficients_nonnegative"
        ]
        and integer_verification["strictly_negative_observed_value"]
    ):
        raise RuntimeError("invalid_normalized_integer_dual")
    return {
        **common,
        "verdict": "DUAL_OBSTRUCTION",
        "sparse_integer_dual": sparse_dual,
        "dual_support_size": len(sparse_dual),
        "verification": integer_verification,
    }


def restrict_problem(
    problem: MarginalProblem,
    context_ids: Iterable[str],
    *,
    suffix: str,
) -> MarginalProblem:
    retained = frozenset(context_ids)
    return MarginalProblem(
        problem_id=f"{problem.problem_id}:{suffix}",
        variable_outcomes=problem.variable_outcomes,
        contexts=tuple(
            context
            for context in problem.contexts
            if context.context_id in retained
        ),
        contract_frozen=problem.contract_frozen,
    )


def leave_one_context_out(problem: MarginalProblem) -> dict[str, Any]:
    """Check whether the full obstruction is inclusion-minimal by context."""

    results: dict[str, str] = {}
    all_ids = tuple(context.context_id for context in problem.contexts)
    for omitted in all_ids:
        restricted = restrict_problem(
            problem,
            (context_id for context_id in all_ids if context_id != omitted),
            suffix=f"without:{omitted}",
        )
        results[omitted] = compile_marginal_extension(restricted)["verdict"]
    return {
        "omission_verdicts": results,
        "every_proper_context_subfamily_is_compatible": all(
            verdict == "GLOBAL_EXTENSION" for verdict in results.values()
        ),
        "logic": (
            "every proper subfamily is contained in at least one "
            "compatible one-context deletion"
        ),
    }


def complete_context(
    context_id: str,
    variables: Sequence[str],
    outcome_map: Mapping[str, Sequence[str]],
    probabilities: Mapping[Assignment, Fraction],
) -> MarginalContext:
    assignments = _product(
        tuple(tuple(outcome_map[name]) for name in variables)
    )
    return MarginalContext(
        context_id=context_id,
        variables=tuple(variables),
        probabilities=tuple(
            (assignment, probabilities.get(assignment, Fraction(0)))
            for assignment in assignments
        ),
    )
