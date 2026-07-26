#!/usr/bin/env python3
"""Exact controls for the HC-DU-038B conformal reconstruction tournament.

The probe separates:

1. causal order, global volume, and one anchored clock/radar record;
2. finite-family reconstruction from calibrated regional volumes;
3. held-out remote-clock prediction; and
4. failure of universal reconstruction under an added smooth conformal mode.

All polynomial integration and linear algebra use exact rational arithmetic.
Passing establishes no physical selection, new geometry, or ontology.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_conformal_record_geometry_tournament_result.json"
)

Poly = tuple[Fraction, ...]


def q(numerator: int, denominator: int = 1) -> Fraction:
    return Fraction(numerator, denominator)


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_add(*polys: Poly) -> Poly:
    width = max(len(poly) for poly in polys)
    return trim(
        tuple(
            sum(
                (
                    poly[index] if index < len(poly) else q(0)
                    for poly in polys
                ),
                q(0),
            )
            for index in range(width)
        )
    )


def poly_scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def poly_multiply(left: Poly, right: Poly) -> Poly:
    result = [q(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(tuple(result))


def poly_derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return (q(0),)
    return trim(tuple(q(index) * poly[index] for index in range(1, len(poly))))


def poly_value(poly: Poly, x: Fraction) -> Fraction:
    value = q(0)
    for coefficient in reversed(poly):
        value = value * x + coefficient
    return value


def poly_integral(poly: Poly, left: Fraction, right: Fraction) -> Fraction:
    return sum(
        (
            coefficient
            * (right ** (index + 1) - left ** (index + 1))
            / q(index + 1)
            for index, coefficient in enumerate(poly)
        ),
        q(0),
    )


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def determinant_2x2(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def scalar_curvature_at(poly: Poly, x: Fraction) -> Fraction:
    """Scalar curvature for g=u(x)(-dt^2+dx^2)."""

    u = poly_value(poly, x)
    first = poly_value(poly_derivative(poly), x)
    second = poly_value(poly_derivative(poly_derivative(poly)), x)
    return -(second / (u * u)) + (first * first) / (u * u * u)


def metric_norm(
    poly: Poly,
    x: Fraction,
    delta_t: Fraction,
    delta_x: Fraction,
) -> Fraction:
    return poly_value(poly, x) * (delta_x * delta_x - delta_t * delta_t)


def as_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def poly_as_text(poly: Poly) -> list[str]:
    return [as_text(value) for value in poly]


ONE: Poly = (q(1),)
F1: Poly = (q(-1, 3), q(2, 3), q(1))
F2: Poly = (q(-1, 3), q(-1, 3), q(1), q(1))
HIDDEN: Poly = (q(1), q(-2), q(-9), q(4), q(10))

X_LEFT = q(-1)
X_RADAR_MIRROR = q(-1, 2)
X_MIDDLE = q(0)
X_RIGHT = q(1)
X_OVERLAP = q(1, 2)


def conformal_factor(
    a: Fraction = q(0),
    b: Fraction = q(0),
    hidden: Fraction = q(0),
) -> Poly:
    return poly_add(
        ONE,
        poly_scale(F1, a),
        poly_scale(F2, b),
        poly_scale(HIDDEN, hidden),
    )


def record_surface(poly: Poly) -> dict[str, Fraction]:
    left_clock_squared = poly_value(poly, X_LEFT)
    radar_coordinate_duration = q(2) * (X_RADAR_MIRROR - X_LEFT)
    return {
        "total_volume": poly_integral(poly, X_LEFT, X_RIGHT),
        "left_volume": poly_integral(poly, X_LEFT, X_MIDDLE),
        "overlap_volume": poly_integral(poly, X_LEFT, X_OVERLAP),
        "left_clock_squared": left_clock_squared,
        "left_radar_time_squared": (
            left_clock_squared * radar_coordinate_duration**2
        ),
        "right_clock_squared": poly_value(poly, X_RIGHT),
        "center_clock_squared": poly_value(poly, X_MIDDLE),
        "center_scalar_curvature": scalar_curvature_at(poly, X_MIDDLE),
    }


def recover_two_mode(
    left_volume: Fraction,
    overlap_volume: Fraction,
) -> tuple[Fraction, Fraction]:
    left_delta = left_volume - q(1)
    overlap_delta = overlap_volume - q(3, 2)
    a = (q(16) * overlap_delta - q(45) * left_delta) / q(9)
    b = (q(72) * left_delta - q(64) * overlap_delta) / q(9)
    return a, b


def predict_right_clock_squared(
    left_volume: Fraction,
    overlap_volume: Fraction,
) -> Fraction:
    left_delta = left_volume - q(1)
    overlap_delta = overlap_volume - q(3, 2)
    return q(1) + q(4) * left_delta - q(64, 9) * overlap_delta


def run() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    mode_integrals = {
        "f1": {
            "full": poly_integral(F1, X_LEFT, X_RIGHT),
            "left": poly_integral(F1, X_LEFT, X_MIDDLE),
            "overlap": poly_integral(F1, X_LEFT, X_OVERLAP),
            "left_endpoint": poly_value(F1, X_LEFT),
            "right_endpoint": poly_value(F1, X_RIGHT),
        },
        "f2": {
            "full": poly_integral(F2, X_LEFT, X_RIGHT),
            "left": poly_integral(F2, X_LEFT, X_MIDDLE),
            "overlap": poly_integral(F2, X_LEFT, X_OVERLAP),
            "left_endpoint": poly_value(F2, X_LEFT),
            "right_endpoint": poly_value(F2, X_RIGHT),
        },
        "hidden": {
            "full": poly_integral(HIDDEN, X_LEFT, X_RIGHT),
            "left": poly_integral(HIDDEN, X_LEFT, X_MIDDLE),
            "overlap": poly_integral(HIDDEN, X_LEFT, X_OVERLAP),
            "left_endpoint": poly_value(HIDDEN, X_LEFT),
            "right_endpoint": poly_value(HIDDEN, X_RIGHT),
        },
    }

    check(
        "two_modes_preserve_base_records",
        mode_integrals["f1"]["full"] == 0
        and mode_integrals["f2"]["full"] == 0
        and mode_integrals["f1"]["left_endpoint"] == 0
        and mode_integrals["f2"]["left_endpoint"] == 0,
        "both declared modes preserve total volume and the anchored left clock",
    )
    check(
        "hidden_mode_annihilates_training_records",
        mode_integrals["hidden"]["full"] == 0
        and mode_integrals["hidden"]["left"] == 0
        and mode_integrals["hidden"]["overlap"] == 0
        and mode_integrals["hidden"]["left_endpoint"] == 0
        and mode_integrals["hidden"]["right_endpoint"] == 4,
        "the hostile smooth mode preserves every training functional but changes the right clock",
    )

    declared_lower_bound = q(1) - q(4, 3) * q(1, 2)
    hidden_lower_bound = q(1) - q(40) * q(1, 100)
    check(
        "declared_family_positive",
        F1 == poly_multiply((q(1), q(1)), (q(-1, 3), q(1)))
        and F2
        == poly_multiply((q(1), q(1)), (q(-1, 3), q(0), q(1)))
        and poly_value(F1, q(-1, 3)) == q(-4, 9)
        and poly_value(F1, q(1)) == q(4, 3)
        and declared_lower_bound == q(1, 3),
        "|f1|,|f2| <= 4/3 and |a|+|b| <= 1/2 imply u >= 1/3",
    )
    check(
        "hidden_fixture_positive",
        HIDDEN
        == poly_multiply(
            (q(1), q(1)),
            (q(1), q(-3), q(-6), q(10)),
        )
        and q(2) * sum((abs(value) for value in (q(1), q(-3), q(-6), q(10))), q(0))
        == q(40)
        and hidden_lower_bound == q(3, 5),
        "the conservative |h| <= 40 bound gives 1+h/100 >= 3/5",
    )

    flat = conformal_factor()
    curved = conformal_factor(q(1, 4), q(1, 4))
    one_volume_rival = conformal_factor(q(1, 10), q(-2, 5))
    hidden_rival = conformal_factor(hidden=q(1, 100))

    flat_records = record_surface(flat)
    curved_records = record_surface(curved)
    one_volume_records = record_surface(one_volume_rival)
    hidden_records = record_surface(hidden_rival)

    sample_points = (q(-1), q(-1, 2), q(0), q(1, 2), q(1))
    check(
        "positive_conformal_rescaling_preserves_cones",
        all(
            metric_norm(poly, x, q(1), q(1)) == 0
            and metric_norm(poly, x, q(1), q(-1)) == 0
            and metric_norm(poly, x, q(1), q(0)) < 0
            and metric_norm(poly, x, q(0), q(1)) > 0
            for poly in (flat, curved, one_volume_rival, hidden_rival)
            for x in sample_points
        ),
        "null, timelike, and spacelike tangent classes agree for every positive conformal fixture",
    )
    check(
        "base_record_surface_is_blind",
        all(
            records["total_volume"] == q(2)
            and records["left_clock_squared"] == q(1)
            and records["left_radar_time_squared"] == q(1)
            for records in (
                flat_records,
                curved_records,
                one_volume_records,
                hidden_records,
            )
        ),
        "causal order, total volume, left clock, and left radar timing do not identify the conformal factor",
    )

    training_matrix = [
        [mode_integrals["f1"]["left"], mode_integrals["f2"]["left"]],
        [
            mode_integrals["f1"]["overlap"],
            mode_integrals["f2"]["overlap"],
        ],
    ]
    training_determinant = determinant_2x2(training_matrix)
    check(
        "one_regional_volume_leaves_a_fibre",
        matrix_rank([training_matrix[0]]) == 1
        and flat_records["left_volume"] == one_volume_records["left_volume"]
        == q(1)
        and flat_records["overlap_volume"]
        != one_volume_records["overlap_volume"],
        "one calibrated regional volume leaves a one-parameter exact rival family",
    )
    check(
        "two_regional_volumes_identify_two_modes",
        training_determinant == q(3, 64)
        and matrix_rank(training_matrix) == 2,
        "the two overlapping regional-volume rows have exact full column rank",
    )

    recovered_curved = recover_two_mode(
        curved_records["left_volume"],
        curved_records["overlap_volume"],
    )
    check(
        "exact_parameter_reconstruction",
        recovered_curved == (q(1, 4), q(1, 4)),
        "the rational inverse recovers the curved fixture parameters exactly",
    )
    check(
        "declared_family_right_clock_prediction",
        curved_records["left_volume"] == q(43, 48)
        and curved_records["overlap_volume"] == q(345, 256)
        and predict_right_clock_squared(
            curved_records["left_volume"],
            curved_records["overlap_volume"],
        )
        == curved_records["right_clock_squared"]
        == q(5, 3),
        "training regional volumes predict held-out right proper time sqrt(5/3)",
    )
    check(
        "curvature_separates_flat_and_curved",
        flat_records["center_scalar_curvature"] == 0
        and curved_records["center_scalar_curvature"] == q(-357, 250),
        "an anchored scalar-curvature invariant proves the curved fixture is not flat",
    )

    check(
        "one_volume_rival_is_exact",
        one_volume_records["left_volume"] == q(1)
        and one_volume_records["overlap_volume"] == q(249, 160)
        and one_volume_records["right_clock_squared"] == q(3, 5),
        "the explicit (1/10,-2/5) rival matches the first regional volume but changes later records",
    )

    expanded_training_matrix = [
        training_matrix[0] + [mode_integrals["hidden"]["left"]],
        training_matrix[1] + [mode_integrals["hidden"]["overlap"]],
    ]
    two_mode_heldout_row = [
        mode_integrals["f1"]["right_endpoint"],
        mode_integrals["f2"]["right_endpoint"],
    ]
    expanded_heldout_row = two_mode_heldout_row + [
        mode_integrals["hidden"]["right_endpoint"]
    ]
    check(
        "two_mode_heldout_is_in_training_row_span",
        matrix_rank(training_matrix + [two_mode_heldout_row])
        == matrix_rank(training_matrix)
        == 2,
        "inside the declared two-mode class the held-out clock row is fixed by training",
    )
    check(
        "expanded_completion_reopens_nonidentification",
        matrix_rank(expanded_training_matrix) == 2
        and matrix_rank(expanded_training_matrix + [expanded_heldout_row]) == 3,
        "adding the smooth hidden mode creates a training null direction seen by the held-out clock",
    )
    check(
        "hidden_completion_defeats_universal_prediction",
        hidden_records["total_volume"] == flat_records["total_volume"]
        and hidden_records["left_volume"] == flat_records["left_volume"]
        and hidden_records["overlap_volume"] == flat_records["overlap_volume"]
        and hidden_records["left_clock_squared"]
        == flat_records["left_clock_squared"]
        and hidden_records["right_clock_squared"] == q(26, 25)
        != flat_records["right_clock_squared"],
        "all training records match flat space while the remote proper time changes",
    )
    check(
        "hidden_completion_is_nonflat",
        hidden_records["center_scalar_curvature"]
        == q(182200, 1030301)
        != 0,
        "the hidden-mode rival has exact nonzero scalar curvature at the anchored center",
    )

    left_child_rows = [
        [
            poly_integral(F1, q(-1), q(-1, 2)),
            poly_integral(F2, q(-1), q(-1, 2)),
        ],
        [
            poly_integral(F1, q(-1, 2), q(0)),
            poly_integral(F2, q(-1, 2), q(0)),
        ],
    ]
    reaggregated_left_row = [
        left_child_rows[0][column] + left_child_rows[1][column]
        for column in range(2)
    ]
    check(
        "regional_subdivision_reaggregates_naturally",
        reaggregated_left_row == training_matrix[0],
        "additive child-region volumes compose to the original measurement row",
    )
    check(
        "separate_child_access_is_physical_information",
        matrix_rank([reaggregated_left_row]) == 1
        and matrix_rank(left_child_rows) == 2
        and determinant_2x2(left_child_rows) == q(1, 64),
        "retaining both child volumes increases rank and is not benign bookkeeping",
    )

    check(
        "right_clock_prediction_formula_is_exact_on_basis",
        all(
            predict_right_clock_squared(
                record_surface(conformal_factor(a, b))["left_volume"],
                record_surface(conformal_factor(a, b))["overlap_volume"],
            )
            == record_surface(conformal_factor(a, b))["right_clock_squared"]
            for a, b in (
                (q(0), q(0)),
                (q(1, 4), q(1, 4)),
                (q(1, 10), q(-2, 5)),
                (q(-1, 5), q(1, 4)),
            )
        ),
        "the held-out prediction identity holds across exact off-origin controls",
    )

    result: dict[str, object] = {
        "artifact_type": "exact_conformal_reconstruction_and_nonuniqueness_controls",
        "theorem_family": "HC-DU-038B",
        "claim_grade": (
            "EXACT CONDITIONAL TWO-MODE RECONSTRUCTION + SMOOTH "
            "COMPLETION COUNTERMODEL / NO PHYSICAL SELECTION OR NEW GEOMETRY"
        ),
        "arena": {
            "manifold": "[0,1]_t x [-1,1]_x",
            "metric_family": "g_u = u(x)(-dt^2+dx^2), u>0",
            "supplied_scaffolding": [
                "dimension",
                "coordinate strip",
                "left/right observer anchors",
                "conformal ansatz",
                "volume and clock calibration",
            ],
        },
        "modes": {
            "f1_coefficients_low_to_high": poly_as_text(F1),
            "f2_coefficients_low_to_high": poly_as_text(F2),
            "hidden_coefficients_low_to_high": poly_as_text(HIDDEN),
            "integrals_and_endpoints": {
                mode: {
                    key: as_text(value) for key, value in values.items()
                }
                for mode, values in mode_integrals.items()
            },
        },
        "identification": {
            "training_matrix": [
                [as_text(value) for value in row] for row in training_matrix
            ],
            "determinant": as_text(training_determinant),
            "one_volume_fibre_dimension": 1,
            "two_volume_fibre_dimension_in_declared_family": 0,
            "expanded_hidden_mode_fibre_dimension": 1,
            "right_clock_squared_prediction": (
                "1 + 4*(V_left-1) - (64/9)*(V_overlap-3/2)"
            ),
        },
        "fixtures": {
            "flat": {
                "parameters": ["0", "0", "0"],
                "records": {
                    key: as_text(value) for key, value in flat_records.items()
                },
            },
            "identified_curved": {
                "parameters": ["1/4", "1/4", "0"],
                "records": {
                    key: as_text(value)
                    for key, value in curved_records.items()
                },
                "right_proper_time": "sqrt(5/3)",
            },
            "one_volume_rival": {
                "parameters": ["1/10", "-2/5", "0"],
                "records": {
                    key: as_text(value)
                    for key, value in one_volume_records.items()
                },
                "right_proper_time": "sqrt(3/5)",
            },
            "hidden_completion": {
                "parameters": ["0", "0", "1/100"],
                "records": {
                    key: as_text(value)
                    for key, value in hidden_records.items()
                },
                "right_proper_time": "sqrt(26/25)",
            },
        },
        "returns": {
            "base_records": "NONIDENTIFYING",
            "one_regional_volume": "ONE_DIMENSIONAL_FIBRE",
            "two_regional_volumes_declared_family": "EXACT_RECONSTRUCTION",
            "heldout_remote_clock_declared_family": "EXACT_PREDICTION",
            "smooth_completion_class": "NONIDENTIFIED_BY_FINITE_TRAINING_SET",
            "regional_subdivision": (
                "GAUGE_ONLY WHEN CHILD VOLUMES ARE REAGGREGATED; "
                "NEW ACCESS WHEN RETAINED SEPARATELY"
            ),
        },
        "checks": checks,
        "checks_passed": len(checks),
        "all_passed": True,
        "limits": [
            "The dimension, coordinate strip, anchors, conformal ansatz, and calibrations are supplied rather than reconstructed.",
            "The exact positive reconstruction holds only inside the declared two-mode family.",
            "A finite set of volume and stationary-clock records cannot identify an unrestricted smooth conformal factor when a held-out functional lies outside their span.",
            "The hidden mode is a completion-class countermodel, not an irreducible physical remainder.",
            "No quantum dynamics, Einstein equation, stress-energy source, physical record-formation law, or experimental realization is supplied.",
        ],
    }
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = run()
    print(
        "PASS "
        f"{result['checks_passed']}/{result['checks_passed']} "
        f"theorem_family={result['theorem_family']}"
    )
    print(f"artifact={OUTPUT.relative_to(ROOT)}")
    print(
        "GRADE: exact conditional reconstruction and smooth completion "
        "countermodel; no physical selection, new geometry, ontology, or "
        "paper verdict"
    )


if __name__ == "__main__":
    main()
