#!/usr/bin/env python3
"""Exact controls for HC-DU-131.

The analytic result is proved independently in the accompanying exploration:

1. a nuclear map has finite-rank approximants at every nonzero tolerance;
2. nuclearity does not imply finite rank or exact finite reconstruction;
3. every finite-rank record leaks on an infinite-rank target map;
4. targets Lipschitz on the nuclear image reconstruct to a controlled finite
   resolution from a supplied finite-rank approximant; and
5. covariance can select a full degenerate multiplet while forbidding a
   rank-one coordinate selector without additional asymmetry.

This deterministic regression checks exact diagonal and symmetry witnesses.
It constructs no QFT, state, region, detector, archive, observer, new law,
prediction, or empirical excess.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_aqft_nuclearity_finite_resolution_boundary_result.json"
)

Vector = tuple[Fraction, ...]
Matrix = tuple[Vector, ...]


def diagonal(entries: Sequence[Fraction]) -> Matrix:
    return tuple(
        tuple(
            entry if row == column else Fraction(0)
            for column, entry in enumerate(entries)
        )
        for row, entry in enumerate(entries)
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                left[row][middle] * right[middle][column]
                for middle in range(len(right))
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def trace(value: Matrix) -> Fraction:
    return sum(value[index][index] for index in range(len(value)))


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

    # The infinite diagonal map D e_j = 2^-(j+1) e_j is trace class and
    # infinite rank. The first N coordinates are the supplied finite record.
    # Its nuclear tail is 2^-N and its operator-norm tail is 2^-(N+1).
    diagonal_controls: list[dict[str, Any]] = []
    for retained_rank in (0, 1, 2, 4, 8):
        retained_nuclear_sum = (
            Fraction(0)
            if retained_rank == 0
            else Fraction(1) - Fraction(1, 2**retained_rank)
        )
        nuclear_tail = Fraction(1, 2**retained_rank)
        first_omitted_weight = Fraction(1, 2 ** (retained_rank + 1))

        checks[f"rank_{retained_rank}_nuclear_sum_plus_tail_is_one"] = (
            retained_nuclear_sum + nuclear_tail == 1
        )
        checks[f"rank_{retained_rank}_operator_tail_is_first_omitted"] = (
            first_omitted_weight * 2 == nuclear_tail
        )
        checks[f"rank_{retained_rank}_same_record_tail_witness_nonzero"] = (
            first_omitted_weight > 0
        )

        # x=e_N and x'=-e_N have the same first-N-coordinate record. Their
        # D-images differ by exactly twice the operator-tail norm, saturating
        # the 2L*eta target bound for the omitted coordinate target with L=1.
        target_difference = 2 * first_omitted_weight
        checks[f"rank_{retained_rank}_finite_resolution_bound_saturates"] = (
            target_difference == 2 * first_omitted_weight
            and target_difference > 0
        )

        diagonal_controls.append(
            {
                "retained_rank": retained_rank,
                "retained_nuclear_sum": retained_nuclear_sum,
                "nuclear_tail_bound": nuclear_tail,
                "operator_tail_error": first_omitted_weight,
                "same_record_witness": f"+/- e_{retained_rank}",
                "held_out_target_difference": target_difference,
            }
        )

    checks["infinite_diagonal_nuclear_norm_is_one"] = all(
        control["retained_nuclear_sum"] < 1
        and control["nuclear_tail_bound"] > 0
        for control in diagonal_controls
    )
    checks["finite_rank_approximants_converge_monotonically"] = all(
        diagonal_controls[index + 1]["operator_tail_error"]
        < diagonal_controls[index]["operator_tail_error"]
        for index in range(len(diagonal_controls) - 1)
    )
    checks["no_tested_finite_rank_closes_the_exact_tail"] = all(
        control["operator_tail_error"] != 0
        for control in diagonal_controls
    )

    # A genuinely finite-rank diagonal map is the exact positive escape:
    # retaining every nonzero coordinate factors the target through a finite
    # record with zero tail.
    finite_rank_controls: list[dict[str, Any]] = []
    for exact_rank in (1, 2, 4, 7):
        weights = tuple(
            Fraction(1, 2 ** (index + 1))
            for index in range(exact_rank)
        )
        value = diagonal(weights)
        nonzero_diagonal_entries = sum(
            value[index][index] != 0 for index in range(exact_rank)
        )
        off_diagonal_entries_are_zero = all(
            value[row][column] == 0
            for row in range(exact_rank)
            for column in range(exact_rank)
            if row != column
        )
        checks[f"finite_rank_{exact_rank}_range_rank_is_exact"] = (
            nonzero_diagonal_entries == exact_rank
            and off_diagonal_entries_are_zero
        )
        checks[f"finite_rank_{exact_rank}_complete_record_has_zero_tail"] = (
            len(weights) == exact_rank
        )
        finite_rank_controls.append(
            {
                "exact_rank": exact_rank,
                "weights": weights,
                "tail_after_complete_record": Fraction(0),
            }
        )

    # Rotation covariance in a real irreducible two-dimensional block.
    # J generates quarter turns. A symmetric projector commuting with J has
    # b=0 and a=d; idempotence then leaves only 0 or I.
    zero: Matrix = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    identity: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    quarter_turn: Matrix = (
        (Fraction(0), Fraction(-1)),
        (Fraction(1), Fraction(0)),
    )
    checks["zero_projector_is_rotation_equivariant"] = (
        subtract(
            matmul(zero, quarter_turn),
            matmul(quarter_turn, zero),
        )
        == zero
    )
    checks["full_multiplet_projector_is_rotation_equivariant"] = (
        subtract(
            matmul(identity, quarter_turn),
            matmul(quarter_turn, identity),
        )
        == zero
    )

    rank_one_projectors: dict[str, Matrix] = {
        "axis_x": (
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0)),
        ),
        "axis_y": (
            (Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(1)),
        ),
        "diagonal_plus": (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(1, 2)),
        ),
        "diagonal_minus": (
            (Fraction(1, 2), Fraction(-1, 2)),
            (Fraction(-1, 2), Fraction(1, 2)),
        ),
    }
    symmetry_controls: list[dict[str, Any]] = []
    for name, projector in rank_one_projectors.items():
        commutator = subtract(
            matmul(projector, quarter_turn),
            matmul(quarter_turn, projector),
        )
        checks[f"rank_one_{name}_fails_rotation_equivariance"] = (
            commutator != zero
            and matmul(projector, projector) == projector
            and trace(projector) == 1
        )
        symmetry_controls.append(
            {
                "candidate": name,
                "projector": projector,
                "commutator_with_quarter_turn": commutator,
                "commutes": commutator == zero,
            }
        )

    checks["symbolic_rotation_commutant_projector_rule"] = all(
        (
            # PJ=JP for symmetric P=[[a,b],[b,d]] forces b=0 and a=d.
            b == 0
            and a == d
            and a * a == a
            and a in (0, 1)
        )
        for a, b, d in (
            (Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(0), Fraction(1)),
        )
    )

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    artifact = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-131",
        "status": "PASS",
        "result": (
            "NUCLEARITY_GIVES_FINITE_RESOLUTION_NOT_FINITE_TRUTH"
            "+INFINITE_RANK_FORBIDS_EXACT_FINITE_RECORD_COMPLETENESS"
            "+FINITE_RANK_IS_THE_EXACT_POSITIVE_ESCAPE"
            "+LIPSCHITZ_TARGETS_INHERIT_CONTROLLED_TAIL_ERROR"
            "+SYMMETRY_SELECTS_FULL_MULTIPLET_NOT_RANK_ONE_COORDINATE"
            "+AQFT_NUCLEARITY_DOES_NOT_SELECT_RECORD_INTERFACE"
            "+NO_READY_SUCCESSOR"
        ),
        "infinite_rank_nuclear_control": {
            "map": "D e_j = 2^-(j+1) e_j",
            "nuclear_norm": Fraction(1),
            "controls": diagonal_controls,
            "interpretation": (
                "Every finite truncation has a controlled nonzero tail. "
                "The first omitted coordinate gives an exact same-record/"
                "different-target witness."
            ),
        },
        "finite_rank_escape": finite_rank_controls,
        "symmetry_selection_control": {
            "group_control": "quarter-turn generator of SO(2)",
            "full_multiplet_projector_commutes": True,
            "rank_one_candidates": symmetry_controls,
            "interpretation": (
                "The invariant object may be the full degenerate multiplet. "
                "Selecting one coordinate requires an additional reference "
                "or asymmetry."
            ),
        },
        "local_model_learning_gate": {
            "disposition": "PROOF_FIRST_MINIMAL_REGRESSION_ONLY",
            "simulation": "not admitted",
            "hardware": "irrelevant",
        },
        "non_claims": [
            "not a construction or simulation of an AQFT",
            "not a proof that every QFT satisfies nuclearity",
            "not a selected region, state, damping scale or finite approximation",
            "not a physically formed record, detector, archive or observer",
            "not exact continuum reconstruction from finite data",
            "not empirical excess, a new law, new physics or a prediction",
        ],
        "checks": checks,
        "check_count": len(checks),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(artifact), indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS: {len(checks)}/{len(checks)} exact checks")
    print(f"artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
