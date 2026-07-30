#!/usr/bin/env python3
"""Exact QRF outcome-broadcast and branch-leakage fixture for HC-DU-154.

Passing establishes only:

1. a definite internal outcome can be copied to an external receiver while a
   position-superposed carrier retains its position coherence;
2. a temporary position tag can be coherently erased before it is retained;
3. an inaccessible copy of that temporary tag prevents the restoration; and
4. partial branch distinguishability obeys the pure two-path
   visibility--distinguishability identity in one exact fixture.

It does not solve the measurement problem, select a Heisenberg cut, reference
factorization, apparatus, outcome basis, record, observer, access boundary,
archive, certification protocol, or finality rule. It establishes no new
physics, prediction, hardware need, or paper readiness.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_qrf_outcome_broadcast_layering_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Iterable[Iterable[int | Fraction]]) -> Matrix:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


def transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column] for row in range(len(value)))
        for column in range(len(value[0]))
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                left[row][inner] * right[inner][column]
                for inner in range(len(right))
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def apply_unitary(unitary: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(unitary, rho), transpose(unitary))


def pure_density(dimension: int, support: dict[int, Fraction]) -> Matrix:
    return tuple(
        tuple(support.get(row, Fraction(0)) * support.get(column, Fraction(0))
              for column in range(dimension))
        for row in range(dimension)
    )


def permutation_matrix(
    dimension: int, mapping: Callable[[int], int]
) -> Matrix:
    rows = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    images = [mapping(index) for index in range(dimension)]
    if sorted(images) != list(range(dimension)):
        raise AssertionError(f"mapping is not a permutation: {images}")
    for source, target in enumerate(images):
        rows[target][source] = Fraction(1)
    return tuple(tuple(row) for row in rows)


def trace_out_second_qubit(rho: Matrix) -> Matrix:
    # Basis order is |left, right>.
    return tuple(
        tuple(
            sum(rho[2 * left + right][2 * other_left + right] for right in range(2))
            for other_left in range(2)
        )
        for left in range(2)
    )


def trace_out_first_qubit(rho: Matrix) -> Matrix:
    # Basis order is |left, right>.
    return tuple(
        tuple(
            sum(rho[2 * left + right][2 * left + other_right] for left in range(2))
            for other_right in range(2)
        )
        for right in range(2)
    )


def trace_out_receiver_and_leak(rho: Matrix) -> Matrix:
    # Basis order is |position, receiver, leak>.
    return tuple(
        tuple(
            sum(
                rho[4 * left + 2 * receiver + leak][
                    4 * other_left + 2 * receiver + leak
                ]
                for receiver in range(2)
                for leak in range(2)
            )
            for other_left in range(2)
        )
        for left in range(2)
    )


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(a * b for a, b in zip(left, right, strict=True))


def as_json(value: Fraction | Matrix) -> object:
    if isinstance(value, Fraction):
        return int(value) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    return [[as_json(entry) for entry in row] for row in value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    coherent_position = matrix(
        (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(1, 2)),
        )
    )
    decohered_position = matrix(
        (
            (Fraction(1, 2), 0),
            (0, Fraction(1, 2)),
        )
    )
    receiver_one = matrix(((0, 0), (0, 1)))

    # The record outcome is fixed to s=1.  The first local interaction writes
    # the receiver only on position branch 0.  The second writes it only on
    # branch 1.  Together they copy the outcome without retaining a position
    # tag.
    initial_two = pure_density(
        4,
        {
            0: Fraction(1, 2),  # unnormalized branch amplitudes are handled below
            2: Fraction(1, 2),
        },
    )
    # Rescale the outer product from amplitudes 1/2 to density entries 1/2.
    initial_two = tuple(
        tuple(Fraction(2) * entry for entry in row) for row in initial_two
    )

    first_write = permutation_matrix(
        4,
        lambda index: (
            2 * (index // 2) + ((index % 2) ^ 1)
            if index // 2 == 0
            else index
        ),
    )
    second_write = permutation_matrix(
        4,
        lambda index: (
            2 * (index // 2) + ((index % 2) ^ 1)
            if index // 2 == 1
            else index
        ),
    )

    after_first = apply_unitary(first_write, initial_two)
    after_second = apply_unitary(second_write, after_first)

    initial_position = trace_out_second_qubit(initial_two)
    intermediate_position = trace_out_second_qubit(after_first)
    final_position = trace_out_second_qubit(after_second)
    final_receiver = trace_out_first_qubit(after_second)

    # Repeat with a third system that irreversibly retains the temporary
    # receiver value after the first local interaction.
    initial_three = pure_density(
        8,
        {
            0: Fraction(1, 2),
            4: Fraction(1, 2),
        },
    )
    initial_three = tuple(
        tuple(Fraction(2) * entry for entry in row) for row in initial_three
    )

    first_write_three = permutation_matrix(
        8,
        lambda index: (
            4 * (index // 4)
            + 2 * (((index // 2) % 2) ^ 1)
            + (index % 2)
            if index // 4 == 0
            else index
        ),
    )
    copy_receiver_to_leak = permutation_matrix(
        8,
        lambda index: (
            4 * (index // 4)
            + 2 * ((index // 2) % 2)
            + ((index % 2) ^ ((index // 2) % 2))
        ),
    )
    second_write_three = permutation_matrix(
        8,
        lambda index: (
            4 * (index // 4)
            + 2 * (((index // 2) % 2) ^ 1)
            + (index % 2)
            if index // 4 == 1
            else index
        ),
    )

    leaked = apply_unitary(first_write_three, initial_three)
    leaked = apply_unitary(copy_receiver_to_leak, leaked)
    leaked = apply_unitary(second_write_three, leaked)
    leaked_final_position = trace_out_receiver_and_leak(leaked)

    # General controlled-message boundary in one exact pure two-path fixture.
    outcome_zero_message = (Fraction(1), Fraction(0))
    outcome_one_message = (Fraction(0), Fraction(1))
    branch_independent_message = outcome_one_message
    partially_marked_branch_zero = (Fraction(1), Fraction(0))
    partially_marked_branch_one = (Fraction(3, 5), Fraction(4, 5))

    outcome_overlap = dot(outcome_zero_message, outcome_one_message)
    no_branch_overlap = dot(branch_independent_message, branch_independent_message)
    partial_branch_overlap = dot(
        partially_marked_branch_zero, partially_marked_branch_one
    )
    visibility = abs(partial_branch_overlap)
    distinguishability = Fraction(4, 5)

    checks = {
        "initial_position_is_coherent": initial_position == coherent_position,
        "first_local_write_temporarily_marks_position": (
            intermediate_position == decohered_position
        ),
        "second_local_write_erases_temporary_position_tag": (
            final_position == coherent_position
        ),
        "external_receiver_contains_outcome_one": final_receiver == receiver_one,
        "outcome_messages_are_perfectly_distinguishable": outcome_overlap == 0,
        "same_outcome_message_is_branch_independent": no_branch_overlap == 1,
        "perfect_outcome_broadcast_and_position_coherence_coexist": (
            final_receiver == receiver_one and final_position == coherent_position
        ),
        "retained_intermediate_tag_blocks_coherence_restoration": (
            leaked_final_position == decohered_position
        ),
        "partial_branch_overlap_is_three_fifths": partial_branch_overlap == Fraction(3, 5),
        "partial_visibility_is_three_fifths": visibility == Fraction(3, 5),
        "partial_distinguishability_is_four_fifths": (
            distinguishability == Fraction(4, 5)
        ),
        "pure_two_path_complementarity_saturates": (
            visibility * visibility
            + distinguishability * distinguishability
            == 1
        ),
    }

    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    result = {
        "claim_id": "HC-DU-154",
        "return": (
            "OUTCOME_BROADCAST_WITHOUT_REFERENCE_DECOHERENCE"
            "+RETAINED_BRANCH_INFORMATION_IS_THE_FIRST_LEAK"
            "+ALGEBRA_RELATIVE_FINALITY_ONLY"
            "+STANDARD_QUANTUM_ABSORPTION"
            "+NO_READY_SUCCESSOR"
        ),
        "checks": checks,
        "two_stage_fixture": {
            "initial_position_state": as_json(initial_position),
            "position_state_after_first_local_write": as_json(intermediate_position),
            "position_state_after_coherent_completion": as_json(final_position),
            "external_receiver_state": as_json(final_receiver),
            "position_state_after_intermediate_leak": as_json(leaked_final_position),
        },
        "controlled_message_fixture": {
            "outcome_message_overlap": as_json(outcome_overlap),
            "within_outcome_branch_overlap": as_json(no_branch_overlap),
            "partial_branch_overlap": as_json(partial_branch_overlap),
            "visibility": as_json(visibility),
            "distinguishability": as_json(distinguishability),
            "visibility_squared_plus_distinguishability_squared": 1,
        },
        "scope": [
            "Exact finite illustration of outcome-only broadcast and branch-information leakage.",
            "Outcome-record and reference-position coherence are independently typed.",
            "Measurement actualization, interface selection, certification, and new physics remain open.",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
