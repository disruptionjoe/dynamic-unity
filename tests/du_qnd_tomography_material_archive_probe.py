#!/usr/bin/env python3
"""Exact finite controls for HC-DU-164.

Passing proves only the label-sufficiency and dilation-twin boundaries declared
by the governed QND-tomography reopener audit. It does not characterize the
IBM apparatus, establish a complete archive, identify a physical dilation,
reconstruct a remainder, or imply new physics.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_qnd_tomography_material_archive_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]
OutputBasis = tuple[int, int, int, int]
SparseOperator = dict[tuple[int, ...], Fraction]


def exact_rank(matrix: Matrix) -> int:
    """Return matrix rank by exact rational row reduction."""
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    pivot_row = 0
    for column in range(n_cols):
        pivot = next(
            (
                row
                for row in range(pivot_row, n_rows)
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def projective_outcome_process(outcome: int) -> Matrix:
    """Liouville matrix for E_n(X)=|n><n| X |n><n|."""
    if outcome not in (0, 1):
        raise ValueError(outcome)
    selected = 0 if outcome == 0 else 3
    return tuple(
        tuple(
            Fraction(int(row == selected and column == selected))
            for column in range(4)
        )
        for row in range(4)
    )


def coin_outcome_process() -> Matrix:
    """Liouville matrix for the uninformative outcome map E(X)=X/2."""
    return tuple(
        tuple(Fraction(int(row == column), 2) for column in range(4))
        for row in range(4)
    )


def reduced_accessible_operator(
    dilation: dict[int, OutputBasis],
    input_ket: int,
    input_bra: int,
) -> SparseOperator:
    """Trace hidden environment/archive factors from one matrix unit."""
    ket = dilation[input_ket]
    bra = dilation[input_bra]
    visible_ket = ket[:2]
    visible_bra = bra[:2]
    hidden_ket = ket[2:]
    hidden_bra = bra[2:]
    if hidden_ket != hidden_bra:
        return {}
    return {visible_ket + visible_bra: Fraction(1)}


def accessible_channel_signature(
    dilation: dict[int, OutputBasis],
) -> tuple[tuple[tuple[tuple[int, ...], str], ...], ...]:
    """Channel values on a matrix-unit basis, enough to prove equality."""
    signature = []
    for input_ket in (0, 1):
        for input_bra in (0, 1):
            operator = reduced_accessible_operator(
                dilation,
                input_ket,
                input_bra,
            )
            signature.append(
                tuple(
                    sorted(
                        (basis, str(value))
                        for basis, value in operator.items()
                    )
                )
            )
    return tuple(signature)


def hidden_archive_value(
    dilation: dict[int, OutputBasis],
    input_basis_state: int,
) -> int:
    return dilation[input_basis_state][3]


def serialize_signature(
    signature: Iterable[Iterable[tuple[tuple[int, ...], str]]],
) -> list[list[dict[str, object]]]:
    return [
        [
            {"basis": list(basis), "coefficient": coefficient}
            for basis, coefficient in matrix_unit
        ]
        for matrix_unit in signature
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    ideal_ranks = {
        str(outcome): exact_rank(projective_outcome_process(outcome))
        for outcome in (0, 1)
    }
    coin_rank = exact_rank(coin_outcome_process())

    # S, C, E, R. E decoheres the accessible outcome in both models.
    # R stays blank in one implementation and copies the outcome in the other.
    blank_archive_dilation = {
        0: (0, 0, 0, 0),
        1: (1, 1, 1, 0),
    }
    copied_archive_dilation = {
        0: (0, 0, 0, 0),
        1: (1, 1, 1, 1),
    }

    blank_signature = accessible_channel_signature(blank_archive_dilation)
    copied_signature = accessible_channel_signature(copied_archive_dilation)

    hidden_archive_for_input_one = {
        "blank_archive": hidden_archive_value(blank_archive_dilation, 1),
        "copied_archive": hidden_archive_value(copied_archive_dilation, 1),
    }

    checks = {
        "ideal_outcome_maps_have_one_dimensional_range": (
            ideal_ranks == {"0": 1, "1": 1}
        ),
        "uninformative_coin_label_does_not_fix_postmeasurement_state": (
            coin_rank == 4
        ),
        "same_accessible_instrument_for_every_input_operator": (
            blank_signature == copied_signature
        ),
        "hidden_archive_support_differs": (
            hidden_archive_for_input_one["blank_archive"]
            != hidden_archive_for_input_one["copied_archive"]
        ),
        "hidden_archive_access_is_a_strict_action_extension": (
            blank_signature == copied_signature
            and hidden_archive_for_input_one
            == {"blank_archive": 0, "copied_archive": 1}
        ),
        "operational_label_sufficiency_does_not_select_material_archive": (
            ideal_ranks == {"0": 1, "1": 1}
            and blank_signature == copied_signature
            and hidden_archive_for_input_one["blank_archive"]
            != hidden_archive_for_input_one["copied_archive"]
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"QND material-archive controls failed: {failed}")

    result = {
        "probe": "du_qnd_tomography_material_archive_probe",
        "status": "PASS",
        "claim_id": "HC-DU-164",
        "scope": (
            "finite-dimensional label sufficiency and exact measurement-"
            "dilation twins"
        ),
        "label_sufficiency_controls": {
            "ideal_projective_outcome_liouville_ranks": ideal_ranks,
            "uninformative_coin_outcome_liouville_rank": coin_rank,
            "future_action_witness": (
                "After the same coin outcome, a later Z effect distinguishes "
                "input |0> from input |1>; the label alone is insufficient."
            ),
        },
        "dilation_twins": {
            "factor_order": ["system", "classical_outcome", "environment", "R"],
            "blank_archive_dilation": {
                str(key): list(value)
                for key, value in blank_archive_dilation.items()
            },
            "copied_archive_dilation": {
                str(key): list(value)
                for key, value in copied_archive_dilation.items()
            },
            "accessible_channel_on_matrix_units": serialize_signature(
                blank_signature
            ),
            "hidden_archive_for_input_one": hidden_archive_for_input_one,
        },
        "checks": checks,
        "disclaimer": (
            "Passing establishes only exact finite representation and "
            "nonselection controls. It establishes no fact about the IBM "
            "apparatus, complete archive, physical dilation, remainder, new "
            "law, or new physics."
        ),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
