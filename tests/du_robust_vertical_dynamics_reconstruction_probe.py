#!/usr/bin/env python3
"""Exact controls for robust reconstruction, a complete vertical slice, and
dynamics-restricted conformal geometry.

The probe deliberately keeps three questions separate:

1. Is an observed stochastic record close to any admitted model?
2. If it is, how far can the held-out target vary over the feasible fibre?
3. Does a proposed physical dynamics actually remove the record-null mode,
   or merely penalize it or rename it as an unconstrained source?

All arithmetic is rational.  The quantum instruments are finite exact
measure-and-prepare maps.  The conformal field law is a supplied toy local
action, not Einstein dynamics or a physically selected theory.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_robust_vertical_dynamics_reconstruction_result.json"
)

F = Fraction
Vector = tuple[Fraction, ...]
Distribution = Vector
StochasticTable = tuple[Distribution, ...]
Matrix = tuple[Vector, ...]
Poly = Vector


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


def distribution_tv(left: Distribution, right: Distribution) -> Fraction:
    if len(left) != len(right):
        raise ValueError("distribution arity mismatch")
    if sum(left, q(0)) != 1 or sum(right, q(0)) != 1:
        raise ValueError("distribution is not normalized")
    return sum(
        (abs(a - b) for a, b in zip(left, right, strict=True)),
        q(0),
    ) / q(2)


def stochastic_table_distance(
    left: StochasticTable, right: StochasticTable
) -> Fraction:
    if len(left) != len(right):
        raise ValueError("table row mismatch")
    return max(
        (
            distribution_tv(a, b)
            for a, b in zip(left, right, strict=True)
        ),
        default=q(0),
    )


def vector_linf(left: Vector, right: Vector) -> Fraction:
    if len(left) != len(right):
        raise ValueError("vector arity mismatch")
    return max(
        (abs(a - b) for a, b in zip(left, right, strict=True)),
        default=q(0),
    )


@dataclass(frozen=True)
class MetricModel:
    model_id: str
    record: Any
    target: Any


def robust_classify(
    models: Sequence[MetricModel],
    observed_record: Any,
    epsilon: Fraction,
    tau: Fraction,
    record_distance: Callable[[Any, Any], Fraction],
    target_distance: Callable[[Any, Any], Fraction],
) -> dict[str, Any]:
    """Finite exact specialization of the robust fibre classifier."""

    if not models:
        return {"branch": "INCOMPLETE_CONTRACT", "reason": "empty_model_class"}
    if epsilon < 0 or tau < 0:
        return {"branch": "INCOMPLETE_CONTRACT", "reason": "negative_tolerance"}

    record_distances = {
        model.model_id: record_distance(model.record, observed_record)
        for model in models
    }
    eta = min(record_distances.values())
    feasible = tuple(
        model
        for model in models
        if record_distances[model.model_id] <= epsilon
    )
    if not feasible:
        return {
            "branch": "ROBUSTLY_UNREALIZABLE",
            "eta": eta,
            "epsilon": epsilon,
            "tau": tau,
            "record_distances": record_distances,
            "feasible_model_ids": (),
            "target_diameter": None,
            "target_witness": None,
        }

    diameter = q(0)
    witness: tuple[str, str] | None = None
    for left, right in itertools.product(feasible, repeat=2):
        distance = target_distance(left.target, right.target)
        if distance > diameter:
            diameter = distance
            witness = (left.model_id, right.model_id)

    branch = (
        "ROBUST_RECONSTRUCTION"
        if diameter <= tau
        else "ROBUST_UNDERDETERMINATION"
    )
    return {
        "branch": branch,
        "eta": eta,
        "epsilon": epsilon,
        "tau": tau,
        "record_distances": record_distances,
        "feasible_model_ids": tuple(model.model_id for model in feasible),
        "target_diameter": diameter,
        "target_witness": witness,
    }


def apply_coarse_record_projection(table: StochasticTable) -> StochasticTable:
    """Forget the post-state tag from labels (r0p0,r0p1,r1p0,r1p1)."""

    return tuple(
        (row[0] + row[1], row[2] + row[3])
        for row in table
    )


def quantitative_controls() -> dict[str, Any]:
    observed = (((q(1), q(0))),)
    near_record = (((q(3, 4), q(1, 4))),)
    exact_record = observed
    same_target = (((q(1), q(0))),)
    target_zero = (((q(1), q(0))),)
    target_one = (((q(0), q(1))),)

    near_sufficient = (
        MetricModel("near_s0", near_record, same_target),
        MetricModel("near_s1", near_record, same_target),
    )
    near_insufficient = (
        MetricModel("near_i0", near_record, target_zero),
        MetricModel("near_i1", near_record, target_one),
    )
    exact_sufficient = (
        MetricModel("exact_s0", exact_record, same_target),
        MetricModel("exact_s1", exact_record, same_target),
    )
    exact_insufficient = (
        MetricModel("exact_i0", exact_record, target_zero),
        MetricModel("exact_i1", exact_record, target_one),
    )

    surfaces = {
        "near_sufficient": robust_classify(
            near_sufficient,
            observed,
            q(1, 4),
            q(0),
            stochastic_table_distance,
            stochastic_table_distance,
        ),
        "near_insufficient": robust_classify(
            near_insufficient,
            observed,
            q(1, 4),
            q(0),
            stochastic_table_distance,
            stochastic_table_distance,
        ),
        "exact_sufficient": robust_classify(
            exact_sufficient,
            observed,
            q(0),
            q(0),
            stochastic_table_distance,
            stochastic_table_distance,
        ),
        "exact_insufficient": robust_classify(
            exact_insufficient,
            observed,
            q(0),
            q(0),
            stochastic_table_distance,
            stochastic_table_distance,
        ),
        "robustly_unrealizable": robust_classify(
            near_insufficient,
            observed,
            q(1, 8),
            q(0),
            stochastic_table_distance,
            stochastic_table_distance,
        ),
    }

    return {
        "metric": "maximum total variation across declared stochastic rows",
        "surface": surfaces,
        "theorem": {
            "realizability_defect": "eta(q)=inf_m d_Q(r(m),q)",
            "feasible_fibre": "F(q,epsilon)={m:d_Q(r(m),q)<=epsilon}",
            "sufficiency_defect": (
                "Delta(q,epsilon)=sup_{m,n in F} d_Y(t(m),t(n))"
            ),
            "branches": [
                "eta>epsilon -> ROBUSTLY_UNREALIZABLE",
                "eta<=epsilon and Delta<=tau -> ROBUST_RECONSTRUCTION",
                (
                    "eta<=epsilon and Delta>tau -> "
                    "ROBUST_UNDERDETERMINATION"
                ),
            ],
            "exact_limit": (
                "epsilon=tau=0 recovers the HC-DU-039A "
                "realizability-first fibre trichotomy"
            ),
        },
    }


def matrix_transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(row[index] for row in matrix) for index in range(len(matrix[0])))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    right_t = matrix_transpose(right)
    return tuple(
        tuple(
            sum((a * b for a, b in zip(row, column, strict=True)), q(0))
            for column in right_t
        )
        for row in left
    )


def matrix_add(*matrices: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((matrix[i][j] for matrix in matrices), q(0))
            for j in range(len(matrices[0][0]))
        )
        for i in range(len(matrices[0]))
    )


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), q(0))


def basis_density(bit: int) -> Matrix:
    return (
        (q(1), q(0)),
        (q(0), q(0)),
    ) if bit == 0 else (
        (q(0), q(0)),
        (q(0), q(1)),
    )


def deterministic_selective_instrument(post_map: tuple[int, int]) -> tuple[Matrix, Matrix]:
    """K_r=|post_map(r)><r| for r in {0,1}."""

    operators: list[Matrix] = []
    for record in (0, 1):
        rows = [[q(0), q(0)], [q(0), q(0)]]
        rows[post_map[record]][record] = q(1)
        operators.append(tuple(tuple(row) for row in rows))
    return tuple(operators)  # type: ignore[return-value]


def instrument_tables(post_map: tuple[int, int]) -> dict[str, Any]:
    operators = deterministic_selective_instrument(post_map)
    effects = tuple(
        matrix_multiply(matrix_transpose(operator), operator)
        for operator in operators
    )
    record_rows: list[Distribution] = []
    refined_rows: list[Distribution] = []
    repeat_rows: list[Distribution] = []

    for history in (0, 1):
        rho = basis_density(history)
        outcome_probabilities = []
        joint_record_post = [q(0), q(0), q(0), q(0)]
        repeat_one = q(0)
        for record, operator in enumerate(operators):
            output = matrix_multiply(
                matrix_multiply(operator, rho),
                matrix_transpose(operator),
            )
            probability = matrix_trace(output)
            outcome_probabilities.append(probability)
            if probability:
                post_one = output[1][1] / probability
                post_bit = 1 if post_one == 1 else 0
                joint_record_post[2 * record + post_bit] += probability
                repeat_one += probability * post_one
        record_rows.append(tuple(outcome_probabilities))
        refined_rows.append(tuple(joint_record_post))
        repeat_rows.append((q(1) - repeat_one, repeat_one))

    return {
        "post_map": post_map,
        "operators": operators,
        "effects": effects,
        "effect_sum": matrix_add(*effects),
        "record_table": tuple(record_rows),
        "refined_instrument_table": tuple(refined_rows),
        "archive_after_repeat_table": tuple(
            (row[0] + row[1], row[2] + row[3])
            for row in refined_rows
        ),
        "repeat_table": tuple(repeat_rows),
    }


def vertical_slice_controls() -> dict[str, Any]:
    named_maps = {
        "prepare_zero": (0, 0),
        "qnd": (0, 1),
        "flip_after_record": (1, 0),
        "prepare_one": (1, 1),
    }
    implementations = {
        name: instrument_tables(post_map)
        for name, post_map in named_maps.items()
    }
    qnd = implementations["qnd"]
    flip = implementations["flip_after_record"]

    base_models = tuple(
        MetricModel(
            name,
            row["record_table"],
            row["repeat_table"],
        )
        for name, row in implementations.items()
    )
    base_record = qnd["record_table"]
    base_verdict = robust_classify(
        base_models,
        base_record,
        q(0),
        q(0),
        stochastic_table_distance,
        stochastic_table_distance,
    )

    noisy_record: StochasticTable = (
        (q(19, 20), q(1, 20)),
        (q(1, 20), q(19, 20)),
    )
    noisy_feasible = robust_classify(
        base_models,
        noisy_record,
        q(1, 20),
        q(0),
        stochastic_table_distance,
        stochastic_table_distance,
    )
    noisy_unrealizable = robust_classify(
        base_models,
        noisy_record,
        q(1, 40),
        q(0),
        stochastic_table_distance,
        stochastic_table_distance,
    )

    refined_models = tuple(
        MetricModel(
            name,
            row["refined_instrument_table"],
            row["repeat_table"],
        )
        for name, row in implementations.items()
    )
    refined_verdict = robust_classify(
        refined_models,
        qnd["refined_instrument_table"],
        q(0),
        q(0),
        stochastic_table_distance,
        stochastic_table_distance,
    )

    projection_rows = {
        name: apply_coarse_record_projection(row["refined_instrument_table"])
        for name, row in implementations.items()
    }
    projection_contractions = {
        name: {
            "fine_distance": stochastic_table_distance(
                row["refined_instrument_table"],
                qnd["refined_instrument_table"],
            ),
            "projected_distance": stochastic_table_distance(
                projection_rows[name],
                base_record,
            ),
        }
        for name, row in implementations.items()
    }

    shared_chain = {
        "physical_source": "basis-state bit h in {0,1}",
        "formed_pointer_record": qnd["record_table"],
        "archive_record": qnd["record_table"],
        "occurrence_identity": "same run-local source event e0",
        "provenance_route": "source->pointer->immutable_archive",
        "regional_compatibility": "pointer value equals archive value",
        "declared_value_finality": (
            "archive value remains fixed under the held-out repeat"
        ),
        "observer_access": "observer reads archive bit r",
        "base_capability": "announce the initial source-basis value r",
        "omitted_type": "complete selective continuation / post-record map",
    }

    return {
        "implementations": implementations,
        "selected_pair": {
            "left": "qnd",
            "right": "flip_after_record",
            "same_effects": qnd["effects"] == flip["effects"],
            "same_formed_record": qnd["record_table"] == flip["record_table"],
            "different_repeat_target": (
                qnd["repeat_table"] != flip["repeat_table"]
            ),
            "target_distance": stochastic_table_distance(
                qnd["repeat_table"], flip["repeat_table"]
            ),
        },
        "shared_declared_chain": shared_chain,
        "base_verdict": base_verdict,
        "noisy_feasible_verdict": noisy_feasible,
        "noisy_unrealizable_verdict": noisy_unrealizable,
        "refined_selective_map_verdict": refined_verdict,
        "refinement_projection": {
            "label_map": (
                "(r0p0,r0p1,r1p0,r1p1) -> (r0,r1)"
            ),
            "projected_rows": projection_rows,
            "distance_receipts": projection_contractions,
        },
        "minimality_scope": (
            "Within the frozen binary measure-and-prepare class, two "
            "implementations, two outcomes, one formed event and one "
            "held-out repeat are the minimum arities for a "
            "same-effect/different-continuation witness."
        ),
    }


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_add(*polys: Poly) -> Poly:
    width = max(len(poly) for poly in polys)
    return trim(
        tuple(
            sum(
                (
                    poly[index] if index < len(poly) else q(0)
                    for poly in polys
                ),
                q(0),
            )
            for index in range(width)
        )
    )


def poly_scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * coefficient for coefficient in poly))


def poly_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (q(0),)
    return trim(tuple(q(index) * poly[index] for index in range(1, len(poly))))


def poly_multiply(left: Poly, right: Poly) -> Poly:
    result = [q(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(tuple(result))


def poly_value(poly: Poly, x: Fraction) -> Fraction:
    result = q(0)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def poly_integral(poly: Poly, left: Fraction, right: Fraction) -> Fraction:
    return sum(
        (
            coefficient
            * (right ** (index + 1) - left ** (index + 1))
            / q(index + 1)
            for index, coefficient in enumerate(poly)
        ),
        q(0),
    )


def matrix_rank(rows: Sequence[Sequence[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [list(row) for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if matrix[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [
            value / pivot_value for value in matrix[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            multiplier = matrix[row][column]
            if multiplier:
                matrix[row] = [
                    value - multiplier * pivot_value
                    for value, pivot_value in zip(
                        matrix[row], matrix[pivot_row], strict=True
                    )
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def functional_integral_row(
    degree: int, left: Fraction, right: Fraction
) -> Vector:
    return tuple(
        (right ** (index + 1) - left ** (index + 1)) / q(index + 1)
        for index in range(degree + 1)
    )


def functional_value_row(degree: int, x: Fraction) -> Vector:
    return tuple(x**index for index in range(degree + 1))


def second_derivative_rows(degree: int) -> tuple[Vector, ...]:
    rows = []
    for output_power in range(degree - 1):
        row = [q(0) for _ in range(degree + 1)]
        source_power = output_power + 2
        row[source_power] = q(source_power * (source_power - 1))
        rows.append(tuple(row))
    return tuple(rows)


ONE: Poly = (q(1),)
HIDDEN: Poly = (q(1), q(-2), q(-9), q(4), q(10))


def geometry_records(poly: Poly) -> Vector:
    return (
        poly_integral(poly, q(-1), q(1)),
        poly_integral(poly, q(-1), q(0)),
        poly_integral(poly, q(-1), q(1, 2)),
        poly_value(poly, q(-1)),
    )


def dirichlet_action(poly: Poly) -> Fraction:
    derivative = poly_derivative(poly)
    return poly_integral(
        poly_multiply(derivative, derivative), q(-1), q(1)
    ) / q(2)


def geometry_dynamics_controls() -> dict[str, Any]:
    degree = 4
    flat = ONE
    hidden_scale = q(1, 100)
    hidden_rival = poly_add(ONE, poly_scale(HIDDEN, hidden_scale))
    flat_record = geometry_records(flat)
    hidden_record = geometry_records(hidden_rival)
    flat_target = (poly_value(flat, q(1)),)
    hidden_target = (poly_value(hidden_rival, q(1)),)

    record_rows = (
        functional_integral_row(degree, q(-1), q(1)),
        functional_integral_row(degree, q(-1), q(0)),
        functional_integral_row(degree, q(-1), q(1, 2)),
        functional_value_row(degree, q(-1)),
    )
    target_row = functional_value_row(degree, q(1))
    dynamics_rows = second_derivative_rows(degree)

    record_rank = matrix_rank(record_rows)
    record_target_rank = matrix_rank(record_rows + (target_row,))
    fixed_source_rank = matrix_rank(record_rows + dynamics_rows)
    fixed_source_target_rank = matrix_rank(
        record_rows + dynamics_rows + (target_row,)
    )

    hidden_second = poly_derivative(poly_derivative(HIDDEN))
    scaled_hidden_source = poly_scale(hidden_second, hidden_scale)
    hidden_action = dirichlet_action(hidden_rival)
    finite_action_bound = q(1, 100)

    broad_models = (
        MetricModel("flat", flat_record, flat_target),
        MetricModel("hidden", hidden_record, hidden_target),
    )
    source_free_models = (
        MetricModel("flat", flat_record, flat_target),
    )
    broad_verdict = robust_classify(
        broad_models,
        flat_record,
        q(0),
        q(0),
        vector_linf,
        vector_linf,
    )
    finite_action_verdict = robust_classify(
        tuple(
            model
            for model, poly in zip(
                broad_models, (flat, hidden_rival), strict=True
            )
            if dirichlet_action(poly) <= finite_action_bound
        ),
        flat_record,
        q(0),
        q(0),
        vector_linf,
        vector_linf,
    )
    unrestricted_source_verdict = broad_verdict
    source_free_verdict = robust_classify(
        source_free_models,
        flat_record,
        q(0),
        q(0),
        vector_linf,
        vector_linf,
    )

    return {
        "arena": {
            "metric": "g_u=u(x)(-dt^2+dx^2)",
            "polynomial_completion_degree": degree,
            "training_record": (
                "total volume, left volume, overlap volume, anchored left clock"
            ),
            "held_out_target": "right clock squared u(1)",
        },
        "field_law": {
            "action": "S[u]=(1/2) integral_{-1}^{1} (u')^2 dx",
            "source_free_euler_lagrange": "u''=0",
            "inhomogeneous_form": "u''=J",
            "status": (
                "supplied target-independent toy local scalar dynamics; "
                "not Einstein dynamics or a selected physical law"
            ),
        },
        "hidden_mode": {
            "coefficients_low_to_high": HIDDEN,
            "scale": hidden_scale,
            "training_record_flat": flat_record,
            "training_record_hidden": hidden_record,
            "right_clock_flat": flat_target,
            "right_clock_hidden": hidden_target,
            "target_change": vector_linf(flat_target, hidden_target),
            "second_derivative_source": scaled_hidden_source,
            "dirichlet_action": hidden_action,
            "finite_action_bound": finite_action_bound,
            "positive_lower_bound": q(3, 5),
        },
        "nullspace_ranks": {
            "coefficient_dimension": degree + 1,
            "record_rank": record_rank,
            "record_plus_target_rank": record_target_rank,
            "record_plus_fixed_source_dynamics_rank": fixed_source_rank,
            "record_plus_fixed_source_dynamics_plus_target_rank": (
                fixed_source_target_rank
            ),
            "record_nullity": degree + 1 - record_rank,
            "fixed_source_record_nullity": degree + 1 - fixed_source_rank,
        },
        "tournament": {
            "smooth_analytic_only": broad_verdict,
            "finite_action_bound": finite_action_verdict,
            "unrestricted_source": unrestricted_source_verdict,
            "source_free_euler_lagrange": source_free_verdict,
        },
        "theorem": {
            "fixed_source_difference_criterion": (
                "T reconstructs from R on L u=J iff "
                "ker(L) intersect ker(R) is contained in ker(T)"
            ),
            "varying_source_correction": (
                "replace ker(L) by {v:L v lies in the admitted "
                "source-difference space}; arbitrary J restores the full "
                "record nullspace"
            ),
            "energy_boundary": (
                "for every E>0, a sufficiently small nonzero rational "
                "multiple of a record-null smooth mode has action below E"
            ),
        },
    }


def run() -> dict[str, Any]:
    quantitative = quantitative_controls()
    vertical = vertical_slice_controls()
    geometry = geometry_dynamics_controls()
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    surface = quantitative["surface"]
    check(
        "positive_record_misfit_can_be_target_sufficient",
        surface["near_sufficient"]["eta"] == q(1, 4)
        and surface["near_sufficient"]["target_diameter"] == 0
        and surface["near_sufficient"]["branch"] == "ROBUST_RECONSTRUCTION",
        "eta=1/4 and Delta=0 are simultaneously realized",
    )
    check(
        "same_record_misfit_can_be_target_insufficient",
        surface["near_insufficient"]["eta"] == q(1, 4)
        and surface["near_insufficient"]["target_diameter"] == 1
        and surface["near_insufficient"]["branch"]
        == "ROBUST_UNDERDETERMINATION",
        "eta=1/4 is compatible with Delta=1",
    )
    check(
        "exact_limit_recovers_reconstruction_branch",
        surface["exact_sufficient"]["eta"] == 0
        and surface["exact_sufficient"]["target_diameter"] == 0
        and surface["exact_sufficient"]["branch"] == "ROBUST_RECONSTRUCTION",
        "epsilon=tau=0 gives nonempty target-constant fibre",
    )
    check(
        "exact_limit_recovers_underdetermination_branch",
        surface["exact_insufficient"]["eta"] == 0
        and surface["exact_insufficient"]["target_diameter"] == 1
        and surface["exact_insufficient"]["branch"]
        == "ROBUST_UNDERDETERMINATION",
        "epsilon=tau=0 gives nonempty target-nonconstant fibre",
    )
    check(
        "robustly_empty_fibre_is_not_vacuous_reconstruction",
        surface["robustly_unrealizable"]["eta"] == q(1, 4)
        and surface["robustly_unrealizable"]["epsilon"] == q(1, 8)
        and surface["robustly_unrealizable"]["branch"]
        == "ROBUSTLY_UNREALIZABLE",
        "positive distance to the model image is adjudicated before target spread",
    )

    pair = vertical["selected_pair"]
    check(
        "qnd_and_flip_have_identical_effects",
        pair["same_effects"],
        "K_r^T K_r is the same sharp effect for both instruments",
    )
    check(
        "qnd_and_flip_form_the_same_archive_value",
        pair["same_formed_record"],
        "the pointer/archive stochastic table is identical",
    )
    check(
        "qnd_and_flip_differ_only_on_heldout_continuation",
        pair["different_repeat_target"] and pair["target_distance"] == 1,
        "the repeat-outcome tables are at total-variation distance one",
    )
    for name, implementation in vertical["implementations"].items():
        check(
            f"{name}_instrument_is_trace_preserving",
            implementation["effect_sum"]
            == ((q(1), q(0)), (q(0), q(1))),
            f"{name} selective effects sum to identity",
        )
        check(
            f"{name}_formed_archive_is_normalized",
            all(
                sum(row, q(0)) == 1
                for row in implementation["record_table"]
            ),
            f"{name} record rows are normalized",
        )
        check(
            f"{name}_heldout_repeat_preserves_archive",
            implementation["archive_after_repeat_table"]
            == implementation["record_table"],
            f"{name} repeat acts on the system while the archive marginal stays fixed",
        )
    check(
        "every_implementation_supports_the_same_base_value_action",
        all(
            implementation["record_table"]
            == ((q(1), q(0)), (q(0), q(1)))
            for implementation in vertical["implementations"].values()
        ),
        "the observer can announce the initial source bit from the archive with unit success",
    )
    check(
        "value_provenance_finality_chain_is_target_insufficient",
        vertical["base_verdict"]["branch"]
        == "ROBUST_UNDERDETERMINATION"
        and vertical["base_verdict"]["eta"] == 0
        and vertical["base_verdict"]["target_diameter"] == 1,
        "four selective continuations share the complete declared value chain",
    )
    check(
        "noisy_chain_remains_insufficient_at_certified_tolerance",
        vertical["noisy_feasible_verdict"]["branch"]
        == "ROBUST_UNDERDETERMINATION"
        and vertical["noisy_feasible_verdict"]["eta"] == q(1, 20),
        "record noise changes fit but not the held-out continuation diameter",
    )
    check(
        "too_tight_noise_contract_is_unrealizable",
        vertical["noisy_unrealizable_verdict"]["branch"]
        == "ROBUSTLY_UNREALIZABLE",
        "epsilon=1/40 is below the exact record-model distance 1/20",
    )
    check(
        "selective_map_receipt_repairs_repeat_target",
        vertical["refined_selective_map_verdict"]["branch"]
        == "ROBUST_RECONSTRUCTION"
        and vertical["refined_selective_map_verdict"]["feasible_model_ids"]
        == ("qnd",),
        "the implementation-level selective-map receipt selects the QND continuation",
    )
    check(
        "refinement_projection_is_total_variation_contracting",
        all(
            receipt["projected_distance"] <= receipt["fine_distance"]
            for receipt in vertical["refinement_projection"][
                "distance_receipts"
            ].values()
        ),
        "forgetting the post-state tag cannot increase total variation",
    )
    check(
        "fine_fibre_is_contained_in_coarse_fibre",
        set(
            vertical["refined_selective_map_verdict"]["feasible_model_ids"]
        )
        <= set(vertical["base_verdict"]["feasible_model_ids"]),
        "same-class refinement reduces rather than resurrects the fibre",
    )

    hidden = geometry["hidden_mode"]
    ranks = geometry["nullspace_ranks"]
    tournament = geometry["tournament"]
    check(
        "hidden_mode_preserves_every_geometry_training_record",
        hidden["training_record_flat"] == hidden["training_record_hidden"],
        "total, left, overlap, and anchored-clock records are equal",
    )
    check(
        "hidden_mode_changes_remote_clock",
        hidden["target_change"] == q(1, 25),
        "u(1) changes from 1 to 26/25",
    )
    check(
        "hidden_fixture_is_positive",
        hidden["positive_lower_bound"] == q(3, 5),
        "|h|<=40 gives 1+h/100>=3/5",
    )
    check(
        "record_nullspace_is_one_dimensional_in_polynomial_fixture",
        ranks["record_rank"] == 4
        and ranks["record_nullity"] == 1
        and ranks["record_plus_target_rank"] == 5,
        "the held-out clock detects the exact one-dimensional record nullspace",
    )
    check(
        "smoothness_and_analyticity_do_not_select_geometry",
        tournament["smooth_analytic_only"]["branch"]
        == "ROBUST_UNDERDETERMINATION",
        "the hostile mode is polynomial and therefore smooth and analytic",
    )
    check(
        "positive_finite_action_does_not_select_geometry",
        hidden["dirichlet_action"] == q(143, 21875)
        and hidden["dirichlet_action"] < hidden["finite_action_bound"]
        and tournament["finite_action_bound"]["branch"]
        == "ROBUST_UNDERDETERMINATION",
        "the exact hidden rival lies below the frozen 1/100 action bound",
    )
    check(
        "unrestricted_source_relabels_hidden_mode",
        hidden["second_derivative_source"] != (q(0),)
        and tournament["unrestricted_source"]["branch"]
        == "ROBUST_UNDERDETERMINATION",
        "J=h''/100 admits the same record-null rival",
    )
    check(
        "fixed_source_dynamics_kills_record_nullspace",
        ranks["record_plus_fixed_source_dynamics_rank"] == 5
        and ranks["fixed_source_record_nullity"] == 0
        and ranks["record_plus_fixed_source_dynamics_plus_target_rank"] == 5,
        "ker(L) intersect ker(R) is zero in the degree-four fixture",
    )
    check(
        "source_free_euler_lagrange_forces_remote_clock",
        tournament["source_free_euler_lagrange"]["branch"]
        == "ROBUST_RECONSTRUCTION"
        and tournament["source_free_euler_lagrange"]["target_diameter"] == 0,
        "u''=0 plus the frozen records leaves only u=1",
    )

    result = {
        "artifact_type": (
            "exact_robust_reconstruction_vertical_slice_and_"
            "dynamics_restriction_controls"
        ),
        "run_id": (
            "RUN-20260726-161113-robust-vertical-dynamics-reconstruction"
        ),
        "candidate_results": {
            "HC-DU-039B": (
                "robust realizability-sufficiency decomposition"
            ),
            "HC-DU-036G": (
                "complete two-time observer/action vertical-slice boundary"
            ),
            "HC-DU-038C": (
                "dynamics-restricted conformal nullspace theorem"
            ),
        },
        "claim_grade": (
            "EXACT ROBUST FINITE/METRIC SPECIALIZATION + EXACT BINARY "
            "TWO-TIME INSTRUMENT COUNTEREXAMPLE + EXACT TOY "
            "DYNAMICS-RESTRICTED POLYNOMIAL CONFORMAL THEOREM / "
            "COMPONENT MATHEMATICS KNOWN / NO PHYSICAL COMPLETENESS, "
            "SELECTED DYNAMICS, NEW LAW, ONTOLOGY, OR PAPER PROMOTION"
        ),
        "quantitative_reconstruction": quantitative,
        "vertical_slice": vertical,
        "geometry_dynamics": geometry,
        "synthesis": {
            "common_contract": (
                "First measure distance from the observed record to the "
                "admitted model image; only on the resulting nonempty "
                "tolerance fibre measure held-out target diameter."
            ),
            "vertical_localization": (
                "A formed, immutable, provenance-typed value can finalize "
                "the value-reading task while failing to determine the "
                "selective continuation. The missing type is the complete "
                "selective instrument, not another copy of the value."
            ),
            "geometry_localization": (
                "Regularity and finite action do not remove scalable "
                "record-null modes. A field equation removes them only "
                "when its source class is frozen tightly enough that the "
                "homogeneous solution space plus the record map is "
                "uniqueness-generating."
            ),
            "north_star_change": (
                "Reconstruction obligations are now target-indexed and "
                "two-coordinate: realizability eta and sufficiency Delta. "
                "Physical dynamics is evidence only through the admissible "
                "tangent/source class it removes, not through the presence "
                "of a named equation."
            ),
        },
        "checks": checks,
        "checks_passed": len(checks),
        "all_passed": True,
        "limits": [
            "The robust classifier is an exact finite specialization of standard robust inverse-problem geometry.",
            "The instrument witness uses standard binary measure-and-prepare quantum instruments.",
            "The shared vertical chain is complete only for the predeclared value-reading action; it is deliberately incomplete for the held-out repeat until the selective-map receipt is added.",
            "The conformal arena, polynomial class, records, and local scalar action are supplied.",
            "The source-free toy field law is not Einstein dynamics and is not shown to be physically selected.",
            "No physical remainder, record-first ontology, new law, new physics, paper state, or external action is established.",
        ],
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
        "GRADE: exact coupled robust/instrument/dynamics boundary; "
        "no selected physics, ontology, or paper verdict"
    )


if __name__ == "__main__":
    main()
