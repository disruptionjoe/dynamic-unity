#!/usr/bin/env python3
"""Exact controls for HC-DU-115.

The probe preserves a finite quadratic mediator-elimination theorem, a
nonunique mediator/absorber factorization, and the action-class enlargement
that distinguishes source-equivalent completions. It does not model QED,
AQFT, Haag's theorem, absorber theory, RTI, collapse, a physical record, or
new physics.
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
    / "du_mediator_elimination_interface_fork_result.json"
)


Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(column) for column in zip(*matrix, strict=True))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    right_t = transpose(right)
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(row, column, strict=True)),
                Fraction(0),
            )
            for column in right_t
        )
        for row in left
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (coefficient * value for coefficient, value in zip(
                row,
                vector,
                strict=True,
            )),
            Fraction(0),
        )
        for row in matrix
    )


def vector_add(left: Vector, right: Vector) -> Vector:
    return tuple(
        a + b for a, b in zip(left, right, strict=True)
    )


def vector_scale(scale: Fraction, vector: Vector) -> Vector:
    return tuple(scale * value for value in vector)


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            a - b for a, b in zip(left_row, right_row, strict=True)
        )
        for left_row, right_row in zip(left, right, strict=True)
    )


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be nonempty and square")

    augmented = [
        list(row) + list(unit_row)
        for row, unit_row in zip(matrix, identity(size), strict=True)
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
    return tuple(
        tuple(row[size:]) for row in augmented
    )


def quadratic(matrix: Matrix, vector: Vector) -> Fraction:
    return sum(
        (
            value * response
            for value, response in zip(
                vector,
                matvec(matrix, vector),
                strict=True,
            )
        ),
        Fraction(0),
    )


def stationary_mediator(
    coupling: Matrix,
    mediator_kernel: Matrix,
    source: Vector,
) -> Vector:
    return vector_scale(
        Fraction(-1),
        matvec(
            inverse(mediator_kernel),
            matvec(transpose(coupling), source),
        ),
    )


def effective_kernel(
    source_kernel: Matrix,
    coupling: Matrix,
    mediator_kernel: Matrix,
) -> Matrix:
    return matrix_subtract(
        source_kernel,
        matmul(
            matmul(coupling, inverse(mediator_kernel)),
            transpose(coupling),
        ),
    )


def full_action(
    source_kernel: Matrix,
    coupling: Matrix,
    mediator_kernel: Matrix,
    source: Vector,
    mediator: Vector,
) -> Fraction:
    source_term = Fraction(1, 2) * quadratic(
        source_kernel,
        source,
    )
    coupled = sum(
        (
            source_value * response
            for source_value, response in zip(
                source,
                matvec(coupling, mediator),
                strict=True,
            )
        ),
        Fraction(0),
    )
    mediator_term = Fraction(1, 2) * quadratic(
        mediator_kernel,
        mediator,
    )
    return source_term + coupled + mediator_term


def effective_action(kernel: Matrix, source: Vector) -> Fraction:
    return Fraction(1, 2) * quadratic(kernel, source)


def normalized_squared_weights(couplings: Iterable[Fraction]) -> Vector:
    squares = tuple(value * value for value in couplings)
    total = sum(squares, Fraction(0))
    if total == 0:
        raise ValueError("at least one coupling must be nonzero")
    return tuple(value / total for value in squares)


def main() -> None:
    # A two-source, one-mediator exact elimination control.
    source_kernel = (
        (Fraction(3), Fraction(1)),
        (Fraction(1), Fraction(2)),
    )
    coupling = (
        (Fraction(1),),
        (Fraction(-1),),
    )
    mediator_kernel = ((Fraction(2),),)
    source = (Fraction(2, 3), Fraction(-1, 4))

    mediator = stationary_mediator(
        coupling,
        mediator_kernel,
        source,
    )
    kernel = effective_kernel(
        source_kernel,
        coupling,
        mediator_kernel,
    )
    assert full_action(
        source_kernel,
        coupling,
        mediator_kernel,
        source,
        mediator,
    ) == effective_action(kernel, source)

    # The source force/response agrees after stationary elimination.
    full_source_response = vector_add(
        matvec(source_kernel, source),
        matvec(coupling, mediator),
    )
    assert full_source_response == matvec(kernel, source)

    # The same scalar effective interaction has inequivalent mediator/channel
    # completions. One has one mediator; one has two candidate channels.
    scalar_source_kernel = ((Fraction(0),),)
    one_channel_coupling = ((Fraction(1),),)
    one_channel_kernel = ((Fraction(1),),)
    two_channel_coupling = (
        (Fraction(3, 5), Fraction(4, 5)),
    )
    two_channel_kernel = identity(2)

    one_effective = effective_kernel(
        scalar_source_kernel,
        one_channel_coupling,
        one_channel_kernel,
    )
    two_effective = effective_kernel(
        scalar_source_kernel,
        two_channel_coupling,
        two_channel_kernel,
    )
    assert one_effective == two_effective == ((Fraction(-1),),)

    scalar_source = (Fraction(7, 11),)
    assert effective_action(
        one_effective,
        scalar_source,
    ) == effective_action(
        two_effective,
        scalar_source,
    )

    # The source kernel does not select a candidate channel/event partition.
    assert normalized_squared_weights((Fraction(1),)) == (Fraction(1),)
    assert normalized_squared_weights(
        (Fraction(3, 5), Fraction(4, 5))
    ) == (Fraction(9, 25), Fraction(16, 25))

    # The larger completion has an action direction invisible to the original
    # source: the vector orthogonal to its coupling changes a mediator-facing
    # probe but leaves the source coupling unchanged.
    hidden_mediator_direction = (
        Fraction(-4, 5),
        Fraction(3, 5),
    )
    assert matvec(
        two_channel_coupling,
        hidden_mediator_direction,
    ) == (Fraction(0),)
    mediator_probe = ((Fraction(0), Fraction(1)),)
    assert matvec(
        mediator_probe,
        hidden_mediator_direction,
    ) == (Fraction(3, 5),)

    # Reconstructing the stationary mediator is possible only after its
    # factorization has been supplied. The two source-equivalent completions
    # return differently typed mediator coordinates.
    one_mediator = stationary_mediator(
        one_channel_coupling,
        one_channel_kernel,
        scalar_source,
    )
    two_mediator = stationary_mediator(
        two_channel_coupling,
        two_channel_kernel,
        scalar_source,
    )
    assert one_mediator == (Fraction(-7, 11),)
    assert two_mediator == (
        Fraction(-21, 55),
        Fraction(-28, 55),
    )

    result = {
        "claim_id": "HC-DU-115",
        "status": "PASS",
        "controls": {
            "stationary_mediator_elimination_exact": True,
            "source_response_preserved": True,
            "same_source_kernel_one_vs_two_channels": True,
            "absorber_partition_not_selected_by_source_kernel": True,
            "mediator_facing_action_distinguishes_enlarged_completion": True,
            "mediator_reconstruction_requires_supplied_factorization": True,
        },
        "boundary": (
            "Regression only: no QED/AQFT/direct-action equivalence theorem, "
            "Haag resolution, absorber selection, RTI validation, collapse, "
            "formed event, record, access, ontology, empirical excess, new "
            "physics, prediction, paper, hardware, or external action."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
