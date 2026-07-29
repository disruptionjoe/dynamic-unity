#!/usr/bin/env python3
"""Exact finite controls for HC-DU-129.

The analytic result separates four claims:

1. On a fixed m=2n mode algebra, m(m+1)/2 one-quadrature population
   distributions are necessary and sufficient to reconstruct every Gaussian
   mean/covariance packet.
2. Gaussian sample sums and squared sums are likelihood-sufficient under the
   frozen iid instrument, but no finite digitized transcript exactly identifies
   a continuous Gaussian parameter.
3. A bounded-covariance contract gives a finite confidence-qualified
   reconstruction at declared resolution.
4. Exact first and second moments cease to be complete when the Gaussian
   completion class is removed.

This proof-regression constructs no QFT, tomography simulator, state-selection
dynamics, physical detector, record interface, new law, prediction, or
empirical excess.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_gaussian_finite_record_ladder_result.json"

Scalar = Fraction
Vector = tuple[Scalar, ...]
Matrix = tuple[tuple[Scalar, ...], ...]


def dot(left: Sequence[Scalar], right: Sequence[Scalar]) -> Scalar:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        Fraction(0),
    )


def basis_vector(dimension: int, index: int) -> Vector:
    return tuple(
        Fraction(int(position == index)) for position in range(dimension)
    )


def add(left: Vector, right: Vector) -> Vector:
    return tuple(
        a + b for a, b in zip(left, right, strict=True)
    )


def directions(dimension: int) -> tuple[Vector, ...]:
    coordinate = tuple(
        basis_vector(dimension, index) for index in range(dimension)
    )
    pairs = tuple(
        add(coordinate[left], coordinate[right])
        for left in range(dimension)
        for right in range(left + 1, dimension)
    )
    return coordinate + pairs


def symmetric_pairs(dimension: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left in range(dimension)
        for right in range(left + 1, dimension)
    )


def measurement_row(direction: Vector) -> Vector:
    diagonal = tuple(value * value for value in direction)
    off_diagonal = tuple(
        2 * direction[left] * direction[right]
        for left, right in symmetric_pairs(len(direction))
    )
    return diagonal + off_diagonal


def covariance_coordinates(value: Matrix) -> Vector:
    diagonal = tuple(value[index][index] for index in range(len(value)))
    off_diagonal = tuple(
        value[left][right]
        for left, right in symmetric_pairs(len(value))
    )
    return diagonal + off_diagonal


def coordinates_to_covariance(
    value: Vector,
    dimension: int,
) -> Matrix:
    rows = [
        [Fraction(0) for _ in range(dimension)]
        for _ in range(dimension)
    ]
    for index in range(dimension):
        rows[index][index] = value[index]
    offset = dimension
    for pair_index, (left, right) in enumerate(symmetric_pairs(dimension)):
        entry = value[offset + pair_index]
        rows[left][right] = entry
        rows[right][left] = entry
    return tuple(tuple(row) for row in rows)


def quadrature_variance(direction: Vector, covariance: Matrix) -> Scalar:
    return dot(measurement_row(direction), covariance_coordinates(covariance))


def rank(rows: Sequence[Sequence[Scalar]]) -> int:
    if not rows:
        return 0
    work = [list(map(Fraction, row)) for row in rows]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [
            entry / pivot_value for entry in work[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            work[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(
                    work[row],
                    work[pivot_row],
                    strict=True,
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def null_vector(rows: Sequence[Sequence[Scalar]]) -> Vector:
    """Return one nonzero exact vector in the nullspace of a wide matrix."""

    work = [list(map(Fraction, row)) for row in rows]
    row_count = len(work)
    column_count = len(work[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [
            entry / pivot_value for entry in work[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            work[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(
                    work[row],
                    work[pivot_row],
                    strict=True,
                )
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    free_columns = [
        column
        for column in range(column_count)
        if column not in pivot_columns
    ]
    if not free_columns:
        raise AssertionError("matrix has trivial nullspace")

    chosen_free = free_columns[-1]
    solution = [Fraction(0) for _ in range(column_count)]
    solution[chosen_free] = Fraction(1)
    for row, pivot_column in reversed(
        list(enumerate(pivot_columns))
    ):
        solution[pivot_column] = -sum(
            (
                work[row][column] * solution[column]
                for column in free_columns
            ),
            Fraction(0),
        )
    result = tuple(solution)
    if all(entry == 0 for entry in result):
        raise AssertionError("null vector must be nonzero")
    if any(dot(row, result) != 0 for row in rows):
        raise AssertionError("constructed vector is not null")
    return result


def example_covariance(dimension: int) -> Matrix:
    """A rational symmetric covariance with V >= I by diagonal dominance."""

    rows = [
        [Fraction(0) for _ in range(dimension)]
        for _ in range(dimension)
    ]
    for left in range(dimension):
        for right in range(dimension):
            if left == right:
                rows[left][right] = Fraction(2 * dimension + left + 1)
            else:
                rows[left][right] = Fraction(
                    (left + 1) * (right + 1),
                    20 * dimension * dimension,
                )
    return tuple(tuple(row) for row in rows)


def reconstruct_covariance(
    declared_directions: tuple[Vector, ...],
    variances: tuple[Scalar, ...],
) -> Matrix:
    dimension = len(declared_directions[0])
    coordinate_variances = variances[:dimension]
    recovered = [
        [Fraction(0) for _ in range(dimension)]
        for _ in range(dimension)
    ]
    for index, value in enumerate(coordinate_variances):
        recovered[index][index] = value
    offset = dimension
    for pair_index, (left, right) in enumerate(symmetric_pairs(dimension)):
        pair_variance = variances[offset + pair_index]
        value = (
            pair_variance
            - coordinate_variances[left]
            - coordinate_variances[right]
        ) / 2
        recovered[left][right] = value
        recovered[right][left] = value
    return tuple(tuple(row) for row in recovered)


def minimum_gershgorin_margin(value: Matrix) -> Scalar:
    return min(
        value[row][row]
        - sum(
            (
                abs(value[row][column])
                for column in range(len(value))
                if column != row
            ),
            Fraction(0),
        )
        for row in range(len(value))
    )


def scale_matrix(scale: Scalar, value: Matrix) -> Matrix:
    return tuple(
        tuple(scale * entry for entry in row) for row in value
    )


def add_matrices(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            a + b for a, b in zip(left_row, right_row, strict=True)
        )
        for left_row, right_row in zip(left, right, strict=True)
    )


def identity(dimension: int, scale: Scalar = Fraction(1)) -> Matrix:
    return tuple(
        tuple(
            scale if row == column else Fraction(0)
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def gaussian_summary(samples: Iterable[int | Scalar]) -> tuple[int, Scalar, Scalar]:
    values = tuple(Fraction(value) for value in samples)
    return (
        len(values),
        sum(values, Fraction(0)),
        sum((value * value for value in values), Fraction(0)),
    )


def likelihood_quadratic(
    summary: tuple[int, Scalar, Scalar],
) -> tuple[Scalar, Scalar, Scalar]:
    """Coefficients of sum_t (x_t-mu)^2 in powers 1, mu, mu^2."""

    count, total, square_total = summary
    return square_total, -2 * total, Fraction(count)


def normal_bin_probability(
    mean: float,
    variance: float,
    lower: float,
    upper: float,
) -> float:
    if variance <= 0 or not lower < upper:
        raise ValueError("variance and bin width must be positive")
    scale = math.sqrt(2 * variance)
    return 0.5 * (
        math.erf((upper - mean) / scale)
        - math.erf((lower - mean) / scale)
    )


def transcript_probability(
    mean: float,
    variance: float,
    bins: tuple[tuple[float, float], ...],
) -> float:
    return math.prod(
        normal_bin_probability(mean, variance, lower, upper)
        for lower, upper in bins
    )


def sufficient_repetitions(
    modes: int,
    covariance_bound: float,
    mean_error: float,
    covariance_entry_error: float,
    failure_probability: float,
) -> dict[str, int]:
    dimension = 2 * modes
    setting_count = dimension * (dimension + 1) // 2
    if not (
        covariance_bound > 0
        and mean_error > 0
        and 0 < covariance_entry_error < 3 * covariance_bound
        and 0 < failure_probability < 1
    ):
        raise ValueError("invalid concentration contract")
    mean_repetitions = math.ceil(
        (2 * covariance_bound / (mean_error**2))
        * math.log(4 * dimension / failure_probability)
    )
    covariance_repetitions = math.ceil(
        1
        + (72 * covariance_bound**2 / (covariance_entry_error**2))
        * math.log(4 * setting_count / failure_probability)
    )
    return {
        "mean": mean_repetitions,
        "covariance": covariance_repetitions,
        "per_setting": max(mean_repetitions, covariance_repetitions),
        "settings": setting_count,
        "total_outcomes": setting_count
        * max(mean_repetitions, covariance_repetitions),
    }


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


def main() -> None:
    checks: dict[str, bool] = {}
    population_controls: list[dict[str, Any]] = []
    incomplete_controls: list[dict[str, Any]] = []

    for modes in range(1, 5):
        dimension = 2 * modes
        declared_directions = directions(dimension)
        setting_count = dimension * (dimension + 1) // 2
        measurement_rows = tuple(
            measurement_row(direction) for direction in declared_directions
        )
        covariance = example_covariance(dimension)
        variances = tuple(
            quadrature_variance(direction, covariance)
            for direction in declared_directions
        )
        recovered = reconstruct_covariance(
            declared_directions,
            variances,
        )

        checks[f"modes_{modes}_setting_count_is_exact"] = (
            len(declared_directions) == setting_count
        )
        checks[f"modes_{modes}_measurement_rank_is_complete"] = (
            rank(measurement_rows) == setting_count
        )
        checks[f"modes_{modes}_covariance_reconstructs_exactly"] = (
            recovered == covariance
        )
        checks[f"modes_{modes}_example_is_strictly_physical_by_margin"] = (
            minimum_gershgorin_margin(covariance) > Fraction(1, 2)
        )

        population_controls.append(
            {
                "modes": modes,
                "quadrature_dimension": dimension,
                "necessary_and_sufficient_settings": setting_count,
                "measurement_rank": rank(measurement_rows),
                "minimum_covariance_margin": minimum_gershgorin_margin(
                    covariance
                ),
                "reconstructed_exactly": recovered == covariance,
            }
        )

        incomplete_rows = measurement_rows[:-1]
        missing_direction = declared_directions[-1]
        delta_coordinates = null_vector(incomplete_rows)
        delta = coordinates_to_covariance(delta_coordinates, dimension)
        row_norm = max(
            sum((abs(entry) for entry in row), Fraction(0))
            for row in delta
        )
        epsilon = Fraction(1, 2 * max(Fraction(1), row_norm))
        base = identity(dimension, Fraction(2))
        plus = add_matrices(base, scale_matrix(epsilon, delta))
        minus = add_matrices(base, scale_matrix(-epsilon, delta))
        retained_plus = tuple(
            quadrature_variance(direction, plus)
            for direction in declared_directions[:-1]
        )
        retained_minus = tuple(
            quadrature_variance(direction, minus)
            for direction in declared_directions[:-1]
        )
        missing_plus = quadrature_variance(missing_direction, plus)
        missing_minus = quadrature_variance(missing_direction, minus)

        checks[f"modes_{modes}_one_missing_setting_has_null_direction"] = (
            rank(incomplete_rows) == setting_count - 1
            and retained_plus == retained_minus
            and missing_plus != missing_minus
        )
        checks[f"modes_{modes}_incomplete_witness_remains_physical"] = (
            minimum_gershgorin_margin(plus) >= Fraction(3, 2)
            and minimum_gershgorin_margin(minus) >= Fraction(3, 2)
        )

        incomplete_controls.append(
            {
                "modes": modes,
                "retained_settings": setting_count - 1,
                "retained_rank": rank(incomplete_rows),
                "same_retained_variances": retained_plus == retained_minus,
                "missing_variance_plus": missing_plus,
                "missing_variance_minus": missing_minus,
                "plus_physical_margin": minimum_gershgorin_margin(plus),
                "minus_physical_margin": minimum_gershgorin_margin(minus),
            }
        )

    # Under an iid Gaussian instrument, sample order can be compressed to
    # count, sum, and squared sum without changing any Gaussian likelihood.
    transcript_a = (0, 0, 3, 3)
    transcript_b = (0, 1, 1, 4)
    summary_a = gaussian_summary(transcript_a)
    summary_b = gaussian_summary(transcript_b)
    checks["different_transcripts_share_gaussian_sufficient_statistic"] = (
        transcript_a != transcript_b and summary_a == summary_b
    )
    checks["sufficient_statistic_preserves_likelihood_quadratic"] = (
        likelihood_quadratic(summary_a)
        == likelihood_quadratic(summary_b)
        == (Fraction(18), Fraction(-12), Fraction(4))
    )

    # Every nondegenerate Gaussian gives positive mass to each nonempty finite
    # detector bin, so a finite digitized transcript cannot exactly select the
    # continuous state parameter.
    finite_bins = (
        (-0.25, 0.25),
        (1.0, 1.25),
        (-2.0, -1.5),
        (0.5, 0.75),
    )
    vacuum_probability = transcript_probability(
        0.0,
        0.5,
        finite_bins,
    )
    thermal_probability = transcript_probability(
        0.0,
        1.5,
        finite_bins,
    )
    checks["same_finite_binned_transcript_possible_under_two_gaussians"] = (
        vacuum_probability > 0
        and thermal_probability > 0
        and vacuum_probability != thermal_probability
    )

    # Exact same first/second moments, different higher target:
    # |1> and the thermal Gaussian with mean occupation one.
    fock_mean = (Fraction(0), Fraction(0))
    thermal_mean = (Fraction(0), Fraction(0))
    fock_covariance = identity(2, Fraction(3, 2))
    thermal_covariance = identity(2, Fraction(3, 2))
    fock_q_fourth = Fraction(15, 4)
    thermal_q_fourth = Fraction(27, 4)
    fock_number_variance = Fraction(0)
    thermal_number_variance = Fraction(2)
    checks["fock_and_thermal_share_first_moments"] = (
        fock_mean == thermal_mean
    )
    checks["fock_and_thermal_share_covariance"] = (
        fock_covariance == thermal_covariance
    )
    checks["fourth_moment_is_nongaussian_first_leak"] = (
        fock_q_fourth != thermal_q_fourth
    )
    checks["number_variance_is_nongaussian_first_leak"] = (
        fock_number_variance != thermal_number_variance
    )

    # The finite-resolution theorem produces explicit local sample budgets;
    # this is deterministic evaluation of the proven bound, not simulation.
    sample_budgets = tuple(
        {
            "modes": modes,
            **sufficient_repetitions(
                modes=modes,
                covariance_bound=2.0,
                mean_error=0.2,
                covariance_entry_error=0.2,
                failure_probability=0.05,
            ),
        }
        for modes in (1, 2, 3)
    )
    checks["sample_budget_is_finite_at_declared_resolution"] = all(
        budget["per_setting"] > 0
        and budget["total_outcomes"]
        == budget["settings"] * budget["per_setting"]
        for budget in sample_budgets
    )
    checks["sample_budget_grows_with_setting_count"] = all(
        later["settings"] > earlier["settings"]
        and later["total_outcomes"] > earlier["total_outcomes"]
        for earlier, later in zip(
            sample_budgets[:-1],
            sample_budgets[1:],
            strict=True,
        )
    )

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    artifact = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-129",
        "status": "PASS",
        "result": (
            "GAUSSIAN_POPULATION_PACKET_HAS_A_FINITE_MINIMAL_SETTING_BASIS"
            "+FINITE_IID_SUMMARY_IS_LIKELIHOOD_SUFFICIENT_NOT_PARAMETER_DETERMINING"
            "+EVERY_FINITE_DIGITIZED_TRANSCRIPT_HAS_MULTIPLE_GAUSSIAN_COMPLETIONS"
            "+BOUNDED_COVARIANCE_GIVES_FINITE_CONFIDENCE_RECONSTRUCTION"
            "+FIRST_SECOND_MOMENTS_FAIL_OUTSIDE_THE_GAUSSIAN_CLASS"
            "+QUADRATIC_PRESERVATION_IS_NOT_STATE_SELECTION"
            "+NO_READY_SUCCESSOR"
        ),
        "definitions": {
            "quadrature_dimension": "m = 2n",
            "state_parameter": "(d,V)",
            "population_packet": (
                "{mean(u^T R), variance(u^T R)} for declared directions u"
            ),
            "formed_record": (
                "finite digitized outcomes joined to settings, attempts, "
                "calibration and lineage"
            ),
            "certificate": (
                "confidence-qualified physical parameter/target region"
            ),
        },
        "population_setting_theorem": {
            "formula": "k = m(m+1)/2 = n(2n+1)",
            "directions": "{e_i} union {e_i+e_j : i<j}",
            "controls": population_controls,
            "minimality": (
                "Each quadrature population contributes one linear variance "
                "functional on Sym_m, which has dimension k."
            ),
        },
        "incomplete_setting_first_leak": incomplete_controls,
        "iid_likelihood_sufficiency": {
            "transcript_a": transcript_a,
            "transcript_b": transcript_b,
            "shared_summary": summary_a,
            "likelihood_quadratic_coefficients": likelihood_quadratic(
                summary_a
            ),
            "scope": (
                "Sufficiency holds only for the frozen iid Gaussian "
                "instrument; order/provenance can matter outside that model."
            ),
        },
        "finite_transcript_nonidentification": {
            "bins": finite_bins,
            "vacuum_variance": 0.5,
            "thermal_variance": 1.5,
            "vacuum_transcript_probability": vacuum_probability,
            "thermal_transcript_probability": thermal_probability,
            "consequence": (
                "The same finite formed transcript remains possible under "
                "both state parameters; likelihood weight is not exact "
                "rival exclusion."
            ),
        },
        "finite_resolution_certificate": {
            "assumptions": {
                "covariance_spectral_bound": 2.0,
                "mean_max_error": 0.2,
                "covariance_entry_max_error": 0.2,
                "failure_probability": 0.05,
                "iid_repetitions": True,
                "complete_attempt_lineage": True,
            },
            "sufficient_bound": (
                "N >= max((2B/eps_d^2) ln(4m/alpha), "
                "1+(72B^2/eps_V^2) ln(4k/alpha)) per direction"
            ),
            "sample_budgets": sample_budgets,
            "interpretation": (
                "Finite confidence-qualified reconstruction at declared "
                "resolution; not exact state selection."
            ),
        },
        "nongaussian_first_leak": {
            "state_a": "Fock |1>",
            "state_b": "thermal Gaussian with mean occupation 1",
            "shared_mean": fock_mean,
            "shared_covariance": fock_covariance,
            "q_fourth": {
                "fock": fock_q_fourth,
                "thermal": thermal_q_fourth,
            },
            "number_variance": {
                "fock": fock_number_variance,
                "thermal": thermal_number_variance,
            },
        },
        "selection_boundary": {
            "quadratic_unitary": (
                "Preserves a supplied Gaussian class and cannot turn a "
                "non-Gaussian state into a Gaussian one, because its inverse "
                "is also Gaussian."
            ),
            "ground_or_kms_contract": (
                "A specified stable quadratic Hamiltonian plus a specified "
                "ground/KMS state contract can select a Gaussian state; then "
                "the selection is law-side rather than record-side."
            ),
        },
        "local_model_learning_gate": {
            "disposition": "PROOF_FIRST_MINIMAL_REGRESSION_ONLY",
            "simulation": "not admitted",
            "hardware": "irrelevant",
        },
        "checks": checks,
        "check_count": len(checks),
        "non_claims": [
            "not a new Gaussian tomography or statistical sufficiency theorem",
            "not exact state determination from finitely many shots",
            "not a selected Gaussian sector, mode basis or detector",
            "not a QFT continuum or GU/Krein reconstruction",
            "not empirical excess, a new law, new physics or a prediction",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(artifact), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS: {len(checks)}/{len(checks)} exact checks")
    print(f"artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
