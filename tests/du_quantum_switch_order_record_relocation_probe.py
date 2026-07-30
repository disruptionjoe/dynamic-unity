#!/usr/bin/env python3
"""Exact finite controls for HC-DU-173.

The probe checks a two-branch order-marker model with rational amplitudes.
Passing establishes the complementarity and access-extension witnesses used
by the scoped DU result. It does not prove causal nonseparability, select a
physical marker or observer, establish objective collapse, or predict physics
beyond standard quantum theory.
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
    / "du_quantum_switch_order_record_relocation_result.json"
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def outer(vector: Vector) -> Matrix:
    return tuple(
        tuple(left * right for right in vector)
        for left in vector
    )


def matrix_scale(scale: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scale * value for value in row)
        for row in matrix
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def trace_product(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        (
            left[row][column] * right[column][row]
            for row in range(len(left))
            for column in range(len(left))
        ),
        Fraction(0),
    )


def partial_trace_marker(state: Matrix) -> Matrix:
    """Trace the second qubit from a control⊗marker density matrix."""
    return tuple(
        tuple(
            sum(
                (
                    state[2 * control_left + marker][
                        2 * control_right + marker
                    ]
                    for marker in range(2)
                ),
                Fraction(0),
            )
            for control_right in range(2)
        )
        for control_left in range(2)
    )


def conditioned_control(state: Matrix, effect: Matrix) -> tuple[Fraction, Matrix]:
    """Apply a marker effect and return probability plus normalized control."""
    unnormalized = tuple(
        tuple(
            sum(
                (
                    effect[marker_right][marker_left]
                    * state[2 * control_left + marker_left][
                        2 * control_right + marker_right
                    ]
                    for marker_left in range(2)
                    for marker_right in range(2)
                ),
                Fraction(0),
            )
            for control_right in range(2)
        )
        for control_left in range(2)
    )
    probability = unnormalized[0][0] + unnormalized[1][1]
    normalized = matrix_scale(Fraction(1, 1) / probability, unnormalized)
    return probability, normalized


def coherent_marker_state(
    overlap: Fraction,
    orthogonal_component: Fraction,
    branch_sign: int = 1,
) -> Matrix:
    """Build 1/2 |v><v| with v=(|0>|r0> + sign|1>|r1>)."""
    vector: Vector = (
        Fraction(1),
        Fraction(0),
        Fraction(branch_sign) * overlap,
        Fraction(branch_sign) * orthogonal_component,
    )
    return matrix_scale(Fraction(1, 2), outer(vector))


X2: Matrix = (
    (0, 1),
    (1, 0),
)
XX: Matrix = (
    (0, 0, 0, 1),
    (0, 0, 1, 0),
    (0, 1, 0, 0),
    (1, 0, 0, 0),
)
P_PLUS: Matrix = (
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 2)),
)
P_MINUS: Matrix = (
    (Fraction(1, 2), Fraction(-1, 2)),
    (Fraction(-1, 2), Fraction(1, 2)),
)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def matrix_text(matrix: Matrix) -> list[list[str]]:
    return [
        [fraction_text(value) for value in row]
        for row in matrix
    ]


def run_probe() -> dict[str, object]:
    cases = (
        ("unmarked", Fraction(1), Fraction(0), Fraction(0)),
        ("partial_3_4_5", Fraction(3, 5), Fraction(4, 5), Fraction(4, 5)),
        ("orthogonal", Fraction(0), Fraction(1), Fraction(1)),
    )

    complementarity: list[dict[str, str]] = []
    checks: list[dict[str, object]] = []
    for name, overlap, orthogonal_component, distinguishability in cases:
        state = coherent_marker_state(overlap, orthogonal_component)
        reduced = partial_trace_marker(state)
        visibility = abs(trace_product(reduced, X2))
        identity = visibility * visibility + distinguishability * distinguishability
        checks.append(
            {
                "name": f"{name}_visibility_matches_marker_overlap",
                "passed": visibility == abs(overlap),
            }
        )
        checks.append(
            {
                "name": f"{name}_pure_marker_duality",
                "passed": identity == 1,
            }
        )
        complementarity.append(
            {
                "case": name,
                "marker_overlap": fraction_text(overlap),
                "visibility": fraction_text(visibility),
                "distinguishability": fraction_text(distinguishability),
                "D2_plus_V2": fraction_text(identity),
            }
        )

    coherent = coherent_marker_state(Fraction(0), Fraction(1))
    branch_zero = matrix_scale(
        Fraction(1, 2),
        outer((Fraction(1), Fraction(0), Fraction(0), Fraction(0))),
    )
    branch_one = matrix_scale(
        Fraction(1, 2),
        outer((Fraction(0), Fraction(0), Fraction(0), Fraction(1))),
    )
    incoherent = matrix_add(branch_zero, branch_one)

    diagonal_coherent = tuple(coherent[index][index] for index in range(4))
    diagonal_incoherent = tuple(incoherent[index][index] for index in range(4))
    reduced_coherent = partial_trace_marker(coherent)
    reduced_incoherent = partial_trace_marker(incoherent)
    coherent_xx = trace_product(coherent, XX)
    incoherent_xx = trace_product(incoherent, XX)

    checks.extend(
        (
            {
                "name": "diagonal_order_record_is_identical",
                "passed": diagonal_coherent == diagonal_incoherent,
            },
            {
                "name": "restricted_control_state_is_identical",
                "passed": reduced_coherent == reduced_incoherent,
            },
            {
                "name": "coherent_joint_action_is_first_leak",
                "passed": coherent_xx == 1 and incoherent_xx == 0,
            },
        )
    )

    plus_probability, plus_control = conditioned_control(coherent, P_PLUS)
    minus_probability, minus_control = conditioned_control(coherent, P_MINUS)
    plus_x = trace_product(plus_control, X2)
    minus_x = trace_product(minus_control, X2)
    unconditional_x = trace_product(reduced_coherent, X2)
    averaged_x = plus_probability * plus_x + minus_probability * minus_x

    checks.extend(
        (
            {
                "name": "eraser_outcomes_are_balanced",
                "passed": plus_probability == minus_probability == Fraction(1, 2),
            },
            {
                "name": "conditional_eraser_restores_unit_interference",
                "passed": plus_x == 1 and minus_x == -1,
            },
            {
                "name": "unconditional_interference_remains_zero",
                "passed": unconditional_x == averaged_x == 0,
            },
        )
    )

    passed = all(bool(check["passed"]) for check in checks)
    return {
        "probe": "du_quantum_switch_order_record_relocation_probe",
        "claim_id": "HC-DU-173",
        "status": "PASS" if passed else "FAIL",
        "checks_passed": sum(bool(check["passed"]) for check in checks),
        "checks_total": len(checks),
        "complementarity_cases": complementarity,
        "restricted_record_twin": {
            "coherent_diagonal": [fraction_text(value) for value in diagonal_coherent],
            "incoherent_diagonal": [
                fraction_text(value) for value in diagonal_incoherent
            ],
            "coherent_reduced_control": matrix_text(reduced_coherent),
            "incoherent_reduced_control": matrix_text(reduced_incoherent),
            "coherent_XX_response": fraction_text(coherent_xx),
            "incoherent_XX_response": fraction_text(incoherent_xx),
        },
        "eraser": {
            "plus_probability": fraction_text(plus_probability),
            "minus_probability": fraction_text(minus_probability),
            "plus_conditioned_X": fraction_text(plus_x),
            "minus_conditioned_X": fraction_text(minus_x),
            "unconditional_X": fraction_text(unconditional_x),
        },
        "checks": checks,
        "interpretation": (
            "A diagonal order record can close a restricted action class while "
            "a coherent joint operation distinguishes the purified completion. "
            "The marker relocates coherence; it does not by itself prove global "
            "actualization or select a physical archive."
        ),
        "scope_limit": (
            "Finite standard-quantum control only. Causal separability of "
            "dephased quantum-controlled processes is source-derived, not "
            "proved by this regression."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
