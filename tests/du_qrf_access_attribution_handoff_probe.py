#!/usr/bin/env python3
"""Exact reduced-QRF handoff and decoherence-attribution fixture for HC-DU-153.

Passing establishes only:

1. one exact Z2 reduced-QRF example in which block preservation without
   dynamical compatibility fails to preserve an output population;
2. one commuting positive control in which that population is preserved; and
3. the rank-one environment/reference attribution gauge of a local Ramsey
   visibility law, together with an independently calibrated rank-two repair.

It does not select a physical QRF, factorization, PVM, initial assignment,
access boundary, phase reference, record, archive, observer, gravitational
decoherence model, or experimental implementation. It establishes no new
physics, prediction, or paper readiness.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_qrf_access_attribution_handoff_result.json"

Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Iterable[Iterable[int | Fraction]]) -> Matrix:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    width = len(right[0])
    inner = len(right)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(width))
        for i in range(len(left))
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(tuple(value[j][i] for j in range(len(value))) for i in range(len(value[0])))


def trace(value: Matrix) -> Fraction:
    return sum(value[index][index] for index in range(len(value)))


def rank(value: Matrix) -> int:
    work = [list(row) for row in value]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            multiple = work[row][column]
            if multiple:
                work[row] = [
                    work[row][index] - multiple * work[pivot_row][index]
                    for index in range(columns)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def as_json(value: Fraction | Matrix) -> object:
    if isinstance(value, Fraction):
        return int(value) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    return [[as_json(entry) for entry in row] for row in value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    identity = matrix(((1, 0), (0, 1)))
    x_gate = matrix(((0, 1), (1, 0)))
    z_gate = matrix(((1, 0), (0, -1)))
    pointer_zero = matrix(((1, 0), (0, 0)))
    pointer_one = subtract(identity, pointer_zero)
    rho_zero = pointer_zero

    # Luppi et al.'s Z2 reduced-QRF example has
    # Pi_00 = |0><0|_B (and analogous complementary effects).  A controlled
    # inaccessible evolution that flips B violates dynamic compatibility.
    x_commutator = subtract(matmul(pointer_zero, x_gate), matmul(x_gate, pointer_zero))
    z_commutator = subtract(matmul(pointer_zero, z_gate), matmul(z_gate, pointer_zero))

    population_initial = trace(matmul(pointer_zero, rho_zero))
    rho_after_x = matmul(matmul(x_gate, rho_zero), transpose(x_gate))
    rho_after_z = matmul(matmul(z_gate, rho_zero), transpose(z_gate))
    population_after_x = trace(matmul(pointer_zero, rho_after_x))
    population_after_z = trace(matmul(pointer_zero, rho_after_z))

    # A single local Ramsey rate gamma_B = gamma_env + gamma_ref has one row
    # for two source coordinates.  Distinct decompositions therefore have the
    # same complete exponential visibility law at every time.
    single_trace_design = matrix(((1, 1),))
    attribution_null = matrix(((1,), (-1,)))
    twin_one = matrix(((2,), (3,)))
    twin_two = matrix(((4,), (1,)))
    local_rate_one = matmul(single_trace_design, twin_one)
    local_rate_two = matmul(single_trace_design, twin_two)

    # Comparing two uncalibrated references gives two equations for three
    # source coordinates and retains a common-mode gauge.
    two_reference_design = matrix(((1, 1, 0), (1, 0, 1)))
    two_reference_null = matrix(((-1,), (1,), (1,)))

    # Independently measuring/calibrating the reference contribution adds a
    # nonparallel row and identifies both coordinates.
    calibrated_design = matrix(((1, 1), (0, 1)))

    checks = {
        "z2_effect_is_a_projector": matmul(pointer_zero, pointer_zero) == pointer_zero,
        "block_preserving_effects_complete": add(pointer_zero, pointer_one) == identity,
        "noncompatible_commutator_is_nonzero": x_commutator != matrix(((0, 0), (0, 0))),
        "noncompatible_population_changes": (
            population_initial == 1 and population_after_x == 0
        ),
        "compatible_commutator_is_zero": z_commutator == matrix(((0, 0), (0, 0))),
        "compatible_population_is_preserved": (
            population_initial == 1 and population_after_z == 1
        ),
        "single_trace_rank_is_one": rank(single_trace_design) == 1,
        "single_trace_has_env_reference_null": matmul(
            single_trace_design, attribution_null
        )
        == matrix(((0,),)),
        "factorization_twins_have_same_complete_rate": (
            twin_one != twin_two and local_rate_one == local_rate_two == matrix(((5,),))
        ),
        "factorization_twins_have_same_visibility_exponent_all_times": all(
            local_rate_one[0][0] * t == local_rate_two[0][0] * t
            for t in map(Fraction, range(9))
        ),
        "two_uncalibrated_references_remain_rank_deficient": (
            rank(two_reference_design) == 2
            and matmul(two_reference_design, two_reference_null)
            == matrix(((0,), (0,)))
        ),
        "independent_reference_calibration_restores_full_rank": (
            rank(calibrated_design) == 2
        ),
    }

    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    result = {
        "claim_id": "HC-DU-153",
        "return": (
            "HANDOFF_THEOREM_WITH_SUPPLIED_INTERFACE"
            "+REFERENCE_ATTRIBUTION_NONIDENTIFIABILITY"
            "+CALIBRATED_RANK_TWO_REPAIR"
            "+NO_READY_SUCCESSOR"
        ),
        "checks": checks,
        "handoff_fixture": {
            "effect_pi_00": as_json(pointer_zero),
            "noncompatible_unitary": as_json(x_gate),
            "noncompatible_commutator": as_json(x_commutator),
            "population_before": as_json(population_initial),
            "population_after_noncompatible": as_json(population_after_x),
            "compatible_unitary": as_json(z_gate),
            "compatible_commutator": as_json(z_commutator),
            "population_after_compatible": as_json(population_after_z),
        },
        "attribution_fixture": {
            "single_trace_design": as_json(single_trace_design),
            "single_trace_rank": rank(single_trace_design),
            "null_direction": [1, -1],
            "twin_one_env_ref": [2, 3],
            "twin_two_env_ref": [4, 1],
            "common_local_rate": 5,
            "two_uncalibrated_reference_design": as_json(two_reference_design),
            "two_uncalibrated_reference_rank": rank(two_reference_design),
            "two_reference_null_direction": [-1, 1, 1],
            "calibrated_design": as_json(calibrated_design),
            "calibrated_rank": rank(calibrated_design),
        },
        "scope": [
            "Exact finite illustration of Luppi et al. Theorem 4.2.",
            "Exact local-rate source-attribution rank boundary.",
            "No physical interface, record, observer, gravity signal, or new physics is selected.",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
