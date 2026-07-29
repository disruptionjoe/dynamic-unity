#!/usr/bin/env python3
"""Regression controls for HC-DU-102.

This probe preserves elementary exact controls for:

1. Weyl-conjugation response factorization on fixed source/readout labels;
2. one-amplitude phase aliasing;
3. same symplectic response with different quasifree covariances;
4. symplectic relabeling with no selected geometric interpretation;
5. the norm-two discontinuity witness for the full automorphism family; and
6. one finite response packet shared by distinct held-out symplectic forms.

Passing establishes no QFT realization, selected localization, field state,
formed record, finite inverse margin, geometry reconstruction, full metric,
novel physics, prediction, or evidence grade.
"""

from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_bounded_weyl_causal_propagator_result.json"
)

Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right, strict=True)), Fraction(0))


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    right_t = transpose(right)
    return tuple(tuple(dot(row, column) for column in right_t) for row in left)


def sigma(left: Vector, right: Vector, form: Matrix) -> Fraction:
    return dot(left, mat_vec(form, right))


def scale_vector(scale: Fraction, vector: Vector) -> Vector:
    return tuple(scale * value for value in vector)


def add_vectors(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def standard_symplectic_form(blocks: int) -> Matrix:
    dimension = 2 * blocks
    rows = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    for block in range(blocks):
        first = 2 * block
        second = first + 1
        rows[first][second] = Fraction(1)
        rows[second][first] = Fraction(-1)
    return tuple(tuple(row) for row in rows)


def diagonal_matrix(values: Iterable[Fraction]) -> Matrix:
    diagonal = tuple(values)
    return tuple(
        tuple(
            diagonal[row] if row == column else Fraction(0)
            for column in range(len(diagonal))
        )
        for row in range(len(diagonal))
    )


def phase_from_cycles(cycles: Fraction) -> complex:
    """Return exp(2*pi*i*cycles); cycles keeps aliases exact before evaluation."""

    return cmath.exp(2j * math.pi * float(cycles))


def main() -> None:
    form_2d = standard_symplectic_form(1)
    vectors: tuple[Vector, ...] = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(2), Fraction(-1)),
        (Fraction(-3, 2), Fraction(4, 3)),
    )

    antisymmetry_cases: list[dict[str, object]] = []
    for left in vectors:
        for right in vectors:
            forward = sigma(left, right, form_2d)
            reverse = sigma(right, left, form_2d)
            assert forward == -reverse
            antisymmetry_cases.append(
                {
                    "left": [str(value) for value in left],
                    "right": [str(value) for value in right],
                    "sigma": str(forward),
                    "antisymmetric": True,
                }
            )

    factorization_cases: list[dict[str, object]] = []
    amplitudes = (Fraction(-2), Fraction(-1, 3), Fraction(1), Fraction(5, 2))
    for source in vectors:
        for readout in vectors:
            for amplitude in amplitudes:
                displacement = scale_vector(amplitude, source)

                # W(-v)W(h) contributes +sigma(v,h)/2. Multiplication by
                # W(v) contributes the same amount because sigma(h-v,v)
                # equals sigma(h,v). Their exact sum is sigma(v,h).
                first_exponent = sigma(displacement, readout, form_2d) / 2
                intermediate = add_vectors(
                    readout,
                    scale_vector(Fraction(-1), displacement),
                )
                second_exponent = -sigma(intermediate, displacement, form_2d) / 2
                composed_exponent = first_exponent + second_exponent
                predicted_exponent = amplitude * sigma(source, readout, form_2d)
                assert composed_exponent == predicted_exponent
                factorization_cases.append(
                    {
                        "amplitude": str(amplitude),
                        "source": [str(value) for value in source],
                        "readout": [str(value) for value in readout],
                        "exact_conjugation_exponent": str(composed_exponent),
                        "factorized": True,
                    }
                )

    # In normalized phase units, exp(2*pi*i*q) is unchanged by q -> q+k.
    base_cycles = Fraction(1, 3)
    alias_cycles = base_cycles + 7
    assert alias_cycles != base_cycles
    assert abs(phase_from_cycles(alias_cycles) - phase_from_cycles(base_cycles)) < 1e-12

    # Two one-mode quasifree covariances satisfy det(mu) >= 1/4, share J,
    # and give different characteristic values on the same nonzero readout.
    covariance_vacuum = diagonal_matrix((Fraction(1, 2), Fraction(1, 2)))
    covariance_thermal = diagonal_matrix((Fraction(1), Fraction(1)))
    vacuum_determinant = covariance_vacuum[0][0] * covariance_vacuum[1][1]
    thermal_determinant = covariance_thermal[0][0] * covariance_thermal[1][1]
    assert vacuum_determinant >= Fraction(1, 4)
    assert thermal_determinant >= Fraction(1, 4)
    state_readout: Vector = (Fraction(1), Fraction(0))
    vacuum_variance = dot(state_readout, mat_vec(covariance_vacuum, state_readout))
    thermal_variance = dot(state_readout, mat_vec(covariance_thermal, state_readout))
    vacuum_characteristic = math.exp(-0.5 * float(vacuum_variance))
    thermal_characteristic = math.exp(-0.5 * float(thermal_variance))
    assert vacuum_characteristic != thermal_characteristic

    # A nontrivial exact symplectic relabeling preserves every abstract response.
    relabeling = diagonal_matrix((Fraction(2), Fraction(1, 2)))
    relabeled_form = mat_mul(mat_mul(transpose(relabeling), form_2d), relabeling)
    assert relabeled_form == form_2d

    relabeling_cases: list[dict[str, object]] = []
    for left in vectors:
        for right in vectors:
            transformed_left = mat_vec(relabeling, left)
            transformed_right = mat_vec(relabeling, right)
            original = sigma(left, right, form_2d)
            transformed = sigma(transformed_left, transformed_right, form_2d)
            assert original == transformed
            relabeling_cases.append(
                {
                    "original_sigma": str(original),
                    "transformed_sigma": str(transformed),
                    "preserved": True,
                }
            )

    # Norm-discontinuity control in phase-cycle units:
    # source=(1,0), lambda=1, readout=(0,1/2) gives half a cycle, so
    # alpha_lambda(W(h))=-W(h) and the norm difference is exactly two.
    norm_source: Vector = (Fraction(1), Fraction(0))
    norm_readout: Vector = (Fraction(0), Fraction(1, 2))
    norm_phase_cycles = sigma(norm_source, norm_readout, form_2d)
    assert norm_phase_cycles == Fraction(1, 2)
    norm_phase = phase_from_cycles(norm_phase_cycles)
    norm_difference = abs(norm_phase - 1)
    assert abs(norm_difference - 2.0) < 1e-12

    # Two nondegenerate four-dimensional symplectic forms agree on a finite
    # training packet but differ on a held-out source/readout pair.
    form_a_rows = [list(row) for row in standard_symplectic_form(2)]
    form_b_rows = [row[:] for row in form_a_rows]
    form_b_rows[0][2] = Fraction(1)
    form_b_rows[2][0] = Fraction(-1)
    form_a: Matrix = tuple(tuple(row) for row in form_a_rows)
    form_b: Matrix = tuple(tuple(row) for row in form_b_rows)
    basis: tuple[Vector, ...] = tuple(
        tuple(
            Fraction(1) if row == column else Fraction(0)
            for row in range(4)
        )
        for column in range(4)
    )
    training_pairs = ((basis[0], basis[1]), (basis[2], basis[3]))
    for left, right in training_pairs:
        assert sigma(left, right, form_a) == sigma(left, right, form_b)
    held_out_a = sigma(basis[0], basis[2], form_a)
    held_out_b = sigma(basis[0], basis[2], form_b)
    assert held_out_a != held_out_b

    result = {
        "probe": "du_bounded_weyl_causal_propagator_probe",
        "status": "PASS",
        "claim_id": "HC-DU-102",
        "checks": {
            "antisymmetry_cases": len(antisymmetry_cases),
            "exact_factorization_cases": len(factorization_cases),
            "one_amplitude_phase_alias": {
                "base_cycles": str(base_cycles),
                "alias_cycles": str(alias_cycles),
                "same_phase": True,
            },
            "same_symplectic_response_different_quasifree_state": {
                "vacuum_covariance_determinant": str(vacuum_determinant),
                "thermal_covariance_determinant": str(thermal_determinant),
                "vacuum_characteristic": vacuum_characteristic,
                "thermal_characteristic": thermal_characteristic,
                "different": True,
            },
            "symplectic_relabeling_cases": len(relabeling_cases),
            "norm_discontinuity_witness": {
                "phase_cycles": str(norm_phase_cycles),
                "exact_norm_difference": 2,
            },
            "finite_packet_same_training_different_held_out": {
                "training_pairs": 2,
                "held_out_form_a": str(held_out_a),
                "held_out_form_b": str(held_out_b),
                "different": True,
            },
        },
        "representative_exact_controls": {
            "antisymmetry": antisymmetry_cases[3],
            "factorization": next(
                case
                for case in factorization_cases
                if case["exact_conjugation_exponent"] == "10/3"
            ),
            "symplectic_relabeling": next(
                case
                for case in relabeling_cases
                if case["original_sigma"] == "4/3"
            ),
        },
        "scope_warning": (
            "Exact finite symplectic controls only. No QFT realization, "
            "selected localization, field state, formed record, finite "
            "inverse margin, causal or conformal geometry, full metric, "
            "novel physics, or prediction is established."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS:",
        len(factorization_cases),
        "factorizations;",
        len(relabeling_cases),
        "symplectic relabelings; norm-two and finite-packet controls",
    )


if __name__ == "__main__":
    main()
