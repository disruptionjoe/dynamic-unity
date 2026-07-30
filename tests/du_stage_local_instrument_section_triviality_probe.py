#!/usr/bin/env python3
"""Exact finite controls for HC-DU-172.

Passing preserves the rank-one identity, coin-section, marked-cut, and
postprocessing-naturality witnesses used by the scoped theorem. It does not
prove the general theorem by enumeration and does not select a physical
instrument, sampler, outcome, archive, provenance chain, observer, or new
physics.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_stage_local_instrument_section_triviality_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_scale(scale: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scale * value for value in row)
        for row in matrix
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (value * coordinate for value, coordinate in zip(row, vector)),
            Fraction(0),
        )
        for row in matrix
    )


def exact_rank(matrix: Matrix) -> int:
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    if not rows:
        return 0
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(rows))
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            rows[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def trace_from_liouville(vector: Vector) -> Fraction:
    """Trace in the ordered basis E00, E01, E10, E11."""
    return vector[0] + vector[3]


IDENTITY: Matrix = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
DEPHASING: Matrix = (
    (1, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 1),
)
PROJECT_ZERO: Matrix = (
    (1, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)
PROJECT_ONE: Matrix = (
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 1),
)
REPLACER: Matrix = (
    (Fraction(1, 2), 0, 0, Fraction(1, 2)),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (Fraction(1, 2), 0, 0, Fraction(1, 2)),
)
IDENTITY_CHOI: Matrix = (
    (1, 0, 0, 1),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (1, 0, 0, 1),
)
RHO_ZERO: Vector = (1, 0, 0, 0)
RHO_ONE: Vector = (0, 0, 0, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    probabilities = (Fraction(1, 3), Fraction(2, 3))
    coin_identity = tuple(
        matrix_scale(probability, IDENTITY)
        for probability in probabilities
    )
    coin_dephasing = tuple(
        matrix_scale(probability, DEPHASING)
        for probability in probabilities
    )

    # Postprocessing naturality transports a selected identity component to
    # every channel leaving the same input system.
    naturality_controls = {
        name: all(
            matrix_multiply(channel, selected_identity)
            == matrix_scale(probability, channel)
            for probability, selected_identity in zip(
                probabilities,
                coin_identity,
            )
        )
        for name, channel in {
            "identity": IDENTITY,
            "dephasing": DEPHASING,
            "replacer": REPLACER,
        }.items()
    }

    marked_instrument = (PROJECT_ZERO, PROJECT_ONE)
    marked_sum = matrix_add(*marked_instrument)
    marked_probabilities = {
        "rho_zero": tuple(
            trace_from_liouville(matrix_vector(component, RHO_ZERO))
            for component in marked_instrument
        ),
        "rho_one": tuple(
            trace_from_liouville(matrix_vector(component, RHO_ONE))
            for component in marked_instrument
        ),
    }
    transported_marked_sum = matrix_add(
        *(
            matrix_multiply(REPLACER, component)
            for component in marked_instrument
        )
    )

    checks = {
        "identity_choi_has_rank_one": exact_rank(IDENTITY_CHOI) == 1,
        "coin_components_sum_to_identity": (
            matrix_add(*coin_identity) == IDENTITY
        ),
        "postprocessing_naturality_holds_for_exact_controls": all(
            naturality_controls.values()
        ),
        "naturality_forces_coin_decomposition_of_dephasing": all(
            matrix_multiply(DEPHASING, selected_identity) == selected_dephasing
            for selected_identity, selected_dephasing in zip(
                coin_identity,
                coin_dephasing,
            )
        ),
        "marked_projective_instrument_sums_to_dephasing": (
            marked_sum == DEPHASING
        ),
        "marked_projective_instrument_is_informative": (
            marked_probabilities["rho_zero"]
            == (Fraction(1), Fraction(0))
            and marked_probabilities["rho_one"]
            == (Fraction(0), Fraction(1))
        ),
        "informative_decomposition_violates_bare_stage_naturality": (
            marked_instrument != coin_dephasing
        ),
        "marked_components_transport_through_downstream_channel": (
            transported_marked_sum
            == matrix_multiply(REPLACER, DEPHASING)
        ),
    }

    report = {
        "probe": "du_stage_local_instrument_section_triviality_probe",
        "claim_id": "HC-DU-172",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope": (
            "finite-dimensional exact controls for postprocessing-natural "
            "instrument sections and the marked-cut exit"
        ),
        "checks": checks,
        "identity_choi_rank": exact_rank(IDENTITY_CHOI),
        "coin_probabilities": [
            str(probability) for probability in probabilities
        ],
        "marked_outcome_probabilities": {
            state: [str(value) for value in values]
            for state, values in marked_probabilities.items()
        },
        "boundary": (
            "The finite controls preserve the proof boundary; the general "
            "theorem follows analytically from purity of the identity CP map "
            "and downstream naturality, not from enumeration."
        ),
        "disclaimer": (
            "Passing selects no physical cut, instrument, sampler, outcome, "
            "archive, provenance chain, observer, or new physics."
        ),
    }

    if args.write_artifact:
        ARTIFACT.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
