#!/usr/bin/env python3
"""Exact controls for HC-DU-114.

The probe preserves a finite linear attribution theorem and its smallest
counterexamples. It does not form a physical clock, compare remote standards,
select a nuisance class, reconstruct nature's metric, or establish new
physics.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_multistandard_clock_metric_matter_rank_result.json"
)


def matrix_rank(rows: Iterable[Iterable[Fraction]]) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")

    pivot_row = 0
    for column in range(width):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = (
            matrix[pivot],
            matrix[pivot_row],
        )
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [
            value / pivot_value for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor == 0:
                continue
            matrix[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    matrix[row],
                    matrix[pivot_row],
                    strict=True,
                )
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def matvec(
    matrix: Iterable[Iterable[Fraction]],
    vector: Iterable[Fraction],
) -> tuple[Fraction, ...]:
    vector_tuple = tuple(vector)
    return tuple(
        sum(
            (coefficient * value for coefficient, value in zip(
                row,
                vector_tuple,
                strict=True,
            )),
            Fraction(0),
        )
        for row in matrix
    )


def solve_square(
    matrix: Iterable[Iterable[Fraction]],
    output: Iterable[Fraction],
) -> tuple[Fraction, ...]:
    rows = [list(row) for row in matrix]
    target = list(output)
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        raise ValueError("matrix must be nonempty and square")
    if len(target) != size:
        raise ValueError("target length mismatch")

    augmented = [
        row + [value] for row, value in zip(rows, target, strict=True)
    ]
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            raise ValueError("singular matrix")
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        pivot_value = augmented[column][column]
        augmented[column] = [
            value / pivot_value for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    augmented[row],
                    augmented[column],
                    strict=True,
                )
            ]
    return tuple(row[-1] for row in augmented)


def main() -> None:
    # One clock and one admitted matter-law nuisance have an exact
    # same-record/different-redshift witness.
    one_clock = ((Fraction(1), Fraction(2)),)
    completion_a = (Fraction(3, 10), Fraction(1, 10))
    completion_b = (Fraction(1, 10), Fraction(1, 5))
    assert matvec(one_clock, completion_a) == matvec(
        one_clock,
        completion_b,
    )
    assert completion_a[0] != completion_b[0]
    assert matrix_rank(one_clock) == 1

    # Freezing the matter law removes the nuisance column and makes the same
    # one-clock reading a conditional redshift reconstruction.
    fixed_matter_clock = ((Fraction(1),),)
    assert matrix_rank(fixed_matter_clock) == 1
    assert solve_square(
        fixed_matter_clock,
        (Fraction(7, 20),),
    ) == (Fraction(7, 20),)

    # Two distinct sensitivities are the minimum full-rank repair for one
    # nuisance coordinate.
    two_clock = (
        (Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(3)),
    )
    assert matrix_rank(two_clock) == 2
    latent = (Fraction(2, 5), Fraction(1, 10))
    observed = matvec(two_clock, latent)
    assert solve_square(two_clock, observed) == latent

    # Repeating an identical species adds samples but no attribution rank.
    repeated_clock = (
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(2)),
    )
    assert matrix_rank(repeated_clock) == 1

    # A frequency ratio/difference cancels the metric common mode and keeps
    # only differential matter sensitivity.
    z = Fraction(7, 20)
    theta = Fraction(1, 8)
    sensitivity_1 = Fraction(1, 2)
    sensitivity_2 = Fraction(5, 2)
    reading_1 = z + sensitivity_1 * theta
    reading_2 = z + sensitivity_2 * theta
    assert reading_2 - reading_1 == (
        sensitivity_2 - sensitivity_1
    ) * theta

    # Literature-informed three-species control. Coefficients reproduce the
    # rounded Sr, Yb+, and Cs alpha/mu sensitivity pattern reported by
    # Sherrill et al.; the probe treats them only as an exact finite fixture.
    three_species = (
        (Fraction(1), Fraction(206, 100), Fraction(0)),
        (Fraction(1), Fraction(-395, 100), Fraction(0)),
        (Fraction(1), Fraction(483, 100), Fraction(1)),
    )
    assert matrix_rank(three_species) == 3
    physical_coordinates = (
        Fraction(1, 100),
        Fraction(1, 1000),
        Fraction(-1, 2000),
    )
    three_species_record = matvec(
        three_species,
        physical_coordinates,
    )
    assert solve_square(
        three_species,
        three_species_record,
    ) == physical_coordinates

    # Two clocks cannot reconstruct redshift plus two independent nuisance
    # directions, regardless of their coefficient values.
    two_clock_two_nuisance = (
        (Fraction(1), Fraction(2), Fraction(0)),
        (Fraction(1), Fraction(-4), Fraction(1)),
    )
    assert matrix_rank(two_clock_two_nuisance) == 2

    # A universal multiplicative frequency drift and metric redshift have
    # identical design columns. No number of clock species separates them.
    universal_common_mode = (
        (Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(1), Fraction(-3)),
        (Fraction(1), Fraction(1), Fraction(5)),
    )
    assert matrix_rank(universal_common_mode) == 2
    universal_a = (
        Fraction(3, 10),
        Fraction(1, 10),
        Fraction(1, 20),
    )
    universal_b = (
        Fraction(1, 5),
        Fraction(1, 5),
        Fraction(1, 20),
    )
    assert matvec(universal_common_mode, universal_a) == matvec(
        universal_common_mode,
        universal_b,
    )
    assert universal_a[0] != universal_b[0]

    # Nearly parallel sensitivities are formally invertible but amplify
    # bounded record error by the inverse sensitivity gap.
    k_1 = Fraction(1)
    k_2 = Fraction(1001, 1000)
    epsilon = Fraction(1, 1_000_000)
    sensitivity_gap = abs(k_2 - k_1)
    theta_error_bound = 2 * epsilon / sensitivity_gap
    z_error_bound = (
        (abs(k_1) + abs(k_2)) * epsilon / sensitivity_gap
    )
    assert theta_error_bound == Fraction(1, 500)
    assert z_error_bound == Fraction(2001, 1_000_000)

    result = {
        "claim_id": "HC-DU-114",
        "status": "PASS",
        "controls": {
            "one_clock_same_record_different_redshift_witness": True,
            "one_clock_reconstructs_only_with_frozen_matter_law": True,
            "two_distinct_sensitivities_repair_one_nuisance": True,
            "identical_species_add_no_attribution_rank": True,
            "clock_ratio_cancels_metric_common_mode": True,
            "three_species_reconstruct_frozen_redshift_alpha_mu_class": True,
            "two_clocks_fail_for_two_nuisance_directions": True,
            "universal_frequency_drift_exactly_confounds_redshift": True,
            "near_parallel_sensitivities_amplify_record_error": True,
        },
        "boundary": (
            "Regression only: no physical clock selection, formation, "
            "transport, joined archive, provenance, access, unrestricted "
            "matter-law control, natural metric reconstruction, new physics, "
            "prediction, evidence grade, or external-hardware result."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-114 controls: multi-standard clock metric/matter "
        "attribution rank and universal common-mode boundary"
    )


if __name__ == "__main__":
    main()
