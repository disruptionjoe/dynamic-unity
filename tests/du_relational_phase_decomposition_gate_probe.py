#!/usr/bin/env python3
"""Exact phase-decomposition and relational-probability control for HC-DU-149.

The same total qubit Hamiltonian is written as a continuous family of
"free + interaction" splits.  The exact propagator and every fixed endpoint
probability are unchanged, while the commutator assigned to the two pieces
varies continuously and can be made zero.  A second control verifies that a
unitary perspective change preserves probabilities only when state, dynamics,
and measurement are transformed together.

This does not model linearized gravity, implement a diffeomorphism, or prove
that any Chen--Giacomini phase is gauge dependent.  It proves the narrower
identifiability boundary: a commutator-labelled term from one Hamiltonian
split is not by itself a separately observable quantity.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import TypeAlias


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_relational_phase_decomposition_gate_result.json"
)

Vector: TypeAlias = tuple[complex, complex]
Matrix: TypeAlias = tuple[
    tuple[complex, complex],
    tuple[complex, complex],
]

I2: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))
X: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
Z: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))
ZERO: Matrix = ((0j, 0j), (0j, 0j))
TOLERANCE = 1e-12


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(scalar: complex, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_adjoint(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_delta(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[row][column] - right[row][column])
        for row in range(2)
        for column in range(2)
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(
        matrix_multiply(left, right),
        matrix_scale(-1, matrix_multiply(right, left)),
    )


def frobenius_norm(matrix: Matrix) -> float:
    return math.sqrt(
        sum(
            abs(matrix[row][column]) ** 2
            for row in range(2)
            for column in range(2)
        )
    )


def inner(left: Vector, right: Vector) -> complex:
    return sum(
        left[index].conjugate() * right[index]
        for index in range(2)
    )


def probability(state: Vector, effect_vector: Vector) -> float:
    return abs(inner(effect_vector, state)) ** 2


def total_propagator(time: float) -> Matrix:
    """Return exp(-i time (X + Z)) using (X + Z)^2 = 2 I."""

    frequency = math.sqrt(2)
    return matrix_add(
        matrix_scale(math.cos(frequency * time), I2),
        matrix_scale(
            -1j * math.sin(frequency * time) / frequency,
            matrix_add(X, Z),
        ),
    )


def z_rotation(angle: float) -> Matrix:
    return (
        (cmath.exp(-0.5j * angle), 0j),
        (0j, cmath.exp(0.5j * angle)),
    )


def rounded_matrix(matrix: Matrix) -> list[list[dict[str, float]]]:
    return [
        [
            {
                "real": round(matrix[row][column].real, 15),
                "imag": round(matrix[row][column].imag, 15),
            }
            for column in range(2)
        ]
        for row in range(2)
    ]


def build_result() -> dict[str, object]:
    # H = H0(alpha) + HI(alpha) for every alpha.  The labelled commutator
    # changes even though the physical Hamiltonian does not.
    total = matrix_add(X, Z)
    split_rows: list[dict[str, float]] = []
    maximum_total_delta = 0.0
    for alpha in (0.0, 0.25, 0.5, 0.75, 1.0):
        free = matrix_scale(1 - alpha, X)
        interaction = matrix_add(Z, matrix_scale(alpha, X))
        reconstructed = matrix_add(free, interaction)
        total_delta = matrix_delta(reconstructed, total)
        maximum_total_delta = max(maximum_total_delta, total_delta)
        split_rows.append(
            {
                "alpha": alpha,
                "total_hamiltonian_delta": total_delta,
                "labelled_commutator_frobenius_norm": frobenius_norm(
                    commutator(free, interaction)
                ),
            }
        )

    time = 0.37
    angle = 0.61
    propagator = total_propagator(time)
    frame = z_rotation(angle)
    frame_adjoint = matrix_adjoint(frame)
    transformed_propagator = matrix_multiply(
        matrix_multiply(frame, propagator),
        frame_adjoint,
    )

    scale = 1 / math.sqrt(2)
    initial: Vector = (scale, scale)
    readout: Vector = (scale, 1j * scale)
    evolved = matrix_vector(propagator, initial)
    base_probability = probability(evolved, readout)

    transformed_initial = matrix_vector(frame, initial)
    transformed_readout = matrix_vector(frame, readout)
    transformed_evolved = matrix_vector(
        transformed_propagator,
        transformed_initial,
    )
    relational_probability = probability(
        transformed_evolved,
        transformed_readout,
    )
    fixed_coordinate_probability = probability(
        transformed_evolved,
        readout,
    )

    commutator_norms = [
        row["labelled_commutator_frobenius_norm"]
        for row in split_rows
    ]
    assertions = {
        "all_splits_have_same_total_hamiltonian": (
            maximum_total_delta <= TOLERANCE
        ),
        "original_split_has_nonzero_labelled_commutator": (
            commutator_norms[0] > 1
        ),
        "equivalent_split_has_zero_labelled_commutator": (
            commutator_norms[-1] <= TOLERANCE
        ),
        "labelled_commutator_varies_across_equivalent_splits": (
            len({round(value, 12) for value in commutator_norms}) == 5
        ),
        "relational_probability_is_frame_invariant": (
            abs(base_probability - relational_probability) <= TOLERANCE
        ),
        "untransformed_readout_is_positive_control": (
            abs(base_probability - fixed_coordinate_probability) > 1e-3
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-149",
        "arena": {
            "hilbert_dimension": 2,
            "total_hamiltonian": "X + Z",
            "split_family": (
                "H0(alpha)=(1-alpha)X; "
                "HI(alpha)=Z+alpha X"
            ),
            "time": time,
            "perspective_rotation": f"exp(-i {angle} Z / 2)",
            "tolerance": TOLERANCE,
        },
        "split_rows": split_rows,
        "maximum_total_hamiltonian_delta": maximum_total_delta,
        "exact_total_propagator": rounded_matrix(propagator),
        "probabilities": {
            "base_joint_contract": base_probability,
            "fully_transformed_relational_contract": (
                relational_probability
            ),
            "transformed_state_and_dynamics_but_fixed_readout": (
                fixed_coordinate_probability
            ),
        },
        "assertions": assertions,
        "theorem_statement": (
            "The total evolution and relational endpoint probabilities can "
            "remain fixed while the commutator assigned to a chosen "
            "free/interaction split varies continuously and vanishes in an "
            "equivalent split. A commutator-labelled phase component is "
            "therefore not separately identifiable without a physically "
            "selected, invariant decomposition and measurement contract."
        ),
        "scope": (
            "Exact finite decomposition and relational-covariance control "
            "only; not a gravitational gauge calculation."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    result = build_result()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
