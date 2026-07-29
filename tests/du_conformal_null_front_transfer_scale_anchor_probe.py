#!/usr/bin/env python3
"""Exact controls for HC-DU-110.

The scientific result is analytic. This probe preserves:

1. conformal nullness of one fixed four-front architecture;
2. unchanged phase-to-event recovery across several positive Weyl factors;
3. exact four-dimensional conformal-wave and quadratic-coupling weights;
4. a same-boundary-response/different-interior metric-coupling witness;
5. the exact fixed-coefficient covariance break; and
6. the distinction between conformal event transfer and metric-scale recovery.

Passing establishes no fundamental scalar law, physical source formation,
nonzero four-wave symbol, finite-support realization, selected coupling,
source timing, provenance, complete acquisition, full-metric reconstruction,
new physics, prediction, or evidence grade.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_conformal_null_front_transfer_scale_anchor_result.json"
)

Vector = tuple[Fraction, Fraction, Fraction, Fraction]
Matrix = tuple[Vector, Vector, Vector, Vector]

L: Matrix = (
    (Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(-1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(1)),
)

TARGETS: tuple[Vector, ...] = (
    (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    ),
    (
        Fraction(1, 3),
        Fraction(1, 7),
        Fraction(-2, 9),
        Fraction(4, 11),
    ),
    (
        Fraction(-3, 5),
        Fraction(2, 13),
        Fraction(5, 17),
        Fraction(-7, 19),
    ),
    (
        Fraction(2),
        Fraction(-1, 4),
        Fraction(3, 8),
        Fraction(5, 16),
    ),
)

WEYL_FACTORS: tuple[Fraction, ...] = (
    Fraction(1),
    Fraction(3, 2),
    Fraction(2),
    Fraction(5, 2),
)


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def recover_event(control: Vector) -> Vector:
    c1, c2, c3, c4 = control
    time = (c1 + c2) / 2
    space_x = (c1 - c2) / 2
    space_y = c3 - time
    space_z = c4 - time
    return (time, space_x, space_y, space_z)


def minkowski_covector_norm(covector: Vector) -> Fraction:
    return -(covector[0] ** 2) + sum(value**2 for value in covector[1:])


def conformal_covector_norm(
    covector: Vector,
    omega: Fraction,
) -> Fraction:
    # (Omega^2 eta)^(-1) = Omega^(-2) eta^(-1).
    return minkowski_covector_norm(covector) / (omega**2)


def main() -> None:
    # Positive Weyl rescaling does not change the characteristic covectors.
    for omega in WEYL_FACTORS:
        assert omega > 0
        assert tuple(
            conformal_covector_norm(row, omega)
            for row in L
        ) == (0, 0, 0, 0)

    # The intersection equation Lp=c does not contain Omega. The same controls
    # therefore recover the same coordinate events throughout this conformal
    # family.
    controls = tuple(matvec(L, target) for target in TARGETS)
    for omega in WEYL_FACTORS:
        assert omega > 0
        assert tuple(recover_event(control) for control in controls) == TARGETS

    # In four dimensions:
    #   P_{Omega^2 g}(Omega^-1 u) = Omega^-3 P_g u.
    # For a quadratic term, a' = Omega^-1 a makes
    #   a' (Omega^-1 u)^2 = Omega^-3 a u^2.
    conformal_weights = {
        "field_u": -1,
        "conformal_wave_operator_on_u": -3,
        "quadratic_coefficient_a": -1,
        "quadratic_field_power": 2,
        "source_f": -3,
    }
    quadratic_total_weight = (
        conformal_weights["quadratic_coefficient_a"]
        + conformal_weights["quadratic_field_power"]
        * conformal_weights["field_u"]
    )
    assert quadratic_total_weight == -3
    assert (
        quadratic_total_weight
        == conformal_weights["conformal_wave_operator_on_u"]
        == conformal_weights["source_f"]
    )

    # Exact interior witness. Omega=2 changes the metric scale by four and the
    # quadratic coefficient by one half, while leaving a boundary region with
    # Omega=1 unchanged. The source-to-solution maps on that boundary are
    # conjugate and, because the conjugating field factor is one there,
    # identical.
    interior_omega = Fraction(2)
    base_metric_scale = Fraction(1)
    base_coefficient = Fraction(3, 5)
    transformed_metric_scale = interior_omega**2 * base_metric_scale
    transformed_coefficient = base_coefficient / interior_omega
    assert transformed_metric_scale == 4
    assert transformed_coefficient == Fraction(3, 10)
    assert transformed_metric_scale != base_metric_scale
    assert transformed_coefficient != base_coefficient

    boundary_omega = Fraction(1)
    assert boundary_omega**-3 == 1
    assert boundary_omega**-1 == 1

    # If a is held fixed rather than assigned weight -1, its transformed
    # nonlinear term has weight -2 rather than the required -3. The mismatch
    # is a factor Omega. This breaks the exact gauge but does not by itself
    # prove injective recovery of Omega.
    fixed_coefficient_weight = 0
    fixed_quadratic_total_weight = (
        fixed_coefficient_weight
        + conformal_weights["quadratic_field_power"]
        * conformal_weights["field_u"]
    )
    assert fixed_quadratic_total_weight == -2
    assert fixed_quadratic_total_weight != -3
    fixed_term = base_coefficient * (interior_omega**-1) ** 2
    covariant_term = (
        (base_coefficient / interior_omega)
        * (interior_omega**-1) ** 2
    )
    assert fixed_term / covariant_term == interior_omega

    result = {
        "claim_id": "HC-DU-110",
        "status": "PASS",
        "controls": {
            "fixed_null_front_count": len(L),
            "weyl_factors_checked": [
                str(omega) for omega in WEYL_FACTORS
            ],
            "all_covectors_null_for_all_weyl_factors": True,
            "target_event_count_checked": len(TARGETS),
            "all_target_events_unchanged_across_conformal_family": True,
            "conformal_weights": conformal_weights,
            "quadratic_total_weight": quadratic_total_weight,
            "interior_same_map_witness": {
                "omega": str(interior_omega),
                "base_metric_scale": str(base_metric_scale),
                "transformed_metric_scale": str(transformed_metric_scale),
                "base_coefficient": str(base_coefficient),
                "transformed_coefficient": str(transformed_coefficient),
                "boundary_omega": str(boundary_omega),
                "boundary_source_and_response_unchanged": True,
            },
            "fixed_coefficient_weight": fixed_coefficient_weight,
            "fixed_quadratic_total_weight": fixed_quadratic_total_weight,
            "fixed_coefficient_covariance_mismatch_factor": str(
                fixed_term / covariant_term
            ),
            "breaking_gauge_proves_injectivity": False,
        },
        "boundary": (
            "Regression only: no fundamental scalar law, physical source "
            "formation, nonzero four-wave symbol, finite-support realization, "
            "selected coupling, source timing, provenance, complete "
            "acquisition, full-metric reconstruction, new physics, "
            "prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-110 controls: conformal null-front transfer, exact "
        "metric-coupling gauge, and fixed-coefficient scale-anchor boundary"
    )


if __name__ == "__main__":
    main()
