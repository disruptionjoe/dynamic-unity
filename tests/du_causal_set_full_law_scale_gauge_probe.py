#!/usr/bin/env python3
"""Exact controls for HC-DU-112.

The scientific result is analytic. This probe preserves:

1. full Poisson intensity-measure invariance under metric-density rescaling;
2. representative joint-count-law equality, not merely equality of means;
3. causal-order invariance under positive constant Weyl scaling;
4. extension to local conformal scale when density varies regionally;
5. dimensionless volume, curvature, and proper-time ratios;
6. failure of absolute scale identification from the unmarked law; and
7. the distinction between a fixed and a covarying dimensionful mark.

Passing establishes no physical density, mark, clock, mass, interface,
formation, provenance, access, certified record, new physics, prediction, or
evidence grade.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_causal_set_full_law_scale_gauge_result.json"
)

DIMENSION = 4
REFERENCE_VOLUMES: tuple[Fraction, ...] = (
    Fraction(1),
    Fraction(3, 2),
    Fraction(7, 3),
    Fraction(5),
)
ORIGINAL_DENSITY = Fraction(11, 2)
GLOBAL_SCALE = Fraction(3, 2)


def intensity_measures(
    density: Fraction,
    volumes: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(density * volume for volume in volumes)


def poisson_joint_probability(
    means: tuple[Fraction, ...],
    counts: tuple[int, ...],
) -> float:
    return math.exp(-float(sum(means, start=Fraction(0)))) * math.prod(
        float(mean) ** count / math.factorial(count)
        for mean, count in zip(means, counts, strict=True)
    )


def minkowski_interval_squared(
    first: tuple[Fraction, Fraction, Fraction, Fraction],
    second: tuple[Fraction, Fraction, Fraction, Fraction],
    metric_scale: Fraction,
) -> Fraction:
    delta = tuple(b - a for a, b in zip(first, second, strict=True))
    return metric_scale**2 * (
        -(delta[0] ** 2)
        + delta[1] ** 2
        + delta[2] ** 2
        + delta[3] ** 2
    )


def causal_relation_matrix(
    points: tuple[
        tuple[Fraction, Fraction, Fraction, Fraction],
        ...,
    ],
    metric_scale: Fraction,
) -> tuple[tuple[bool, ...], ...]:
    return tuple(
        tuple(
            i != j
            and points[j][0] > points[i][0]
            and minkowski_interval_squared(
                points[i],
                points[j],
                metric_scale,
            )
            < 0
            for j in range(len(points))
        )
        for i in range(len(points))
    )


def main() -> None:
    # The transformed Lorentzian volume is c^d times the original. The
    # density transforms inversely, leaving the complete intensity measure
    # exactly unchanged on every measurable cell.
    transformed_volumes = tuple(
        GLOBAL_SCALE**DIMENSION * volume
        for volume in REFERENCE_VOLUMES
    )
    transformed_density = (
        ORIGINAL_DENSITY / GLOBAL_SCALE**DIMENSION
    )
    original_intensities = intensity_measures(
        ORIGINAL_DENSITY,
        REFERENCE_VOLUMES,
    )
    transformed_intensities = intensity_measures(
        transformed_density,
        transformed_volumes,
    )
    assert transformed_intensities == original_intensities

    # Equality is at the joint Poisson law, not only at first moments.
    count_vectors = (
        (0, 0, 0, 0),
        (1, 0, 2, 3),
        (4, 7, 1, 9),
        (12, 8, 15, 21),
    )
    joint_probabilities = []
    for counts in count_vectors:
        original_probability = poisson_joint_probability(
            original_intensities,
            counts,
        )
        transformed_probability = poisson_joint_probability(
            transformed_intensities,
            counts,
        )
        assert original_probability == transformed_probability
        joint_probabilities.append(original_probability)

    # Positive constant Weyl scaling preserves the sign of every interval and
    # therefore the induced chronological order.
    points = (
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(3), Fraction(0), Fraction(0)),
        (Fraction(5), Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(7), Fraction(-1), Fraction(1), Fraction(1)),
    )
    original_order = causal_relation_matrix(points, Fraction(1))
    transformed_order = causal_relation_matrix(points, GLOBAL_SCALE)
    assert original_order == transformed_order
    assert any(any(row) for row in original_order)
    assert any(
        i != j
        and not original_order[i][j]
        and not original_order[j][i]
        for i in range(len(points))
        for j in range(len(points))
    )

    # Representative unmarked graph summaries cannot change because the
    # complete ordered-event law is the same.
    relation_count = sum(
        int(value)
        for row in original_order
        for value in row
    )
    interval_cardinalities = tuple(
        sum(
            int(original_order[i][k] and original_order[k][j])
            for k in range(len(points))
        )
        for i in range(len(points))
        for j in range(len(points))
        if original_order[i][j]
    )
    transformed_relation_count = sum(
        int(value)
        for row in transformed_order
        for value in row
    )
    transformed_interval_cardinalities = tuple(
        sum(
            int(transformed_order[i][k] and transformed_order[k][j])
            for k in range(len(points))
        )
        for i in range(len(points))
        for j in range(len(points))
        if transformed_order[i][j]
    )
    assert transformed_relation_count == relation_count
    assert transformed_interval_cardinalities == interval_cardinalities

    # If density is permitted to vary by region, an arbitrary positive local
    # conformal factor is absorbed pointwise. The finite cells preserve the
    # exact full independent-increment law because every cell intensity is
    # unchanged. Analytically the same statement is
    # rho'(x)=rho(x)/Omega(x)^d.
    local_scales = (
        Fraction(2),
        Fraction(3, 2),
        Fraction(5, 4),
        Fraction(7, 3),
    )
    local_rescaled_volumes = tuple(
        scale**DIMENSION * volume
        for scale, volume in zip(
            local_scales,
            REFERENCE_VOLUMES,
            strict=True,
        )
    )
    local_rescaled_densities = tuple(
        ORIGINAL_DENSITY / scale**DIMENSION
        for scale in local_scales
    )
    local_rescaled_intensities = tuple(
        density * volume
        for density, volume in zip(
            local_rescaled_densities,
            local_rescaled_volumes,
            strict=True,
        )
    )
    assert local_rescaled_intensities == original_intensities

    # Global scale cancels from dimensionless volume ratios.
    original_volume_ratios = tuple(
        volume / REFERENCE_VOLUMES[0]
        for volume in REFERENCE_VOLUMES[1:]
    )
    transformed_volume_ratios = tuple(
        volume / transformed_volumes[0]
        for volume in transformed_volumes[1:]
    )
    assert transformed_volume_ratios == original_volume_ratios

    # Curvature has inverse-length-squared units and the discreteness length
    # ell=rho^(-1/d) scales as a length. R*ell^2 therefore survives.
    original_curvature = Fraction(5, 7)
    transformed_curvature = original_curvature / GLOBAL_SCALE**2
    original_discreteness_length = float(ORIGINAL_DENSITY) ** (
        -1.0 / DIMENSION
    )
    transformed_discreteness_length = float(
        transformed_density
    ) ** (-1.0 / DIMENSION)
    assert math.isclose(
        transformed_discreteness_length,
        float(GLOBAL_SCALE) * original_discreteness_length,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert math.isclose(
        float(transformed_curvature)
        * transformed_discreteness_length**2,
        float(original_curvature)
        * original_discreteness_length**2,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )

    # A fixed dimensionful mark breaks the scale gauge conditionally.
    mass_scale = 2.0
    proper_times = (0.5, 1.0, 2.0, 3.0)
    fixed_mass_marks = tuple(
        math.exp(-mass_scale * proper_time)
        for proper_time in proper_times
    )
    transformed_fixed_mass_marks = tuple(
        math.exp(
            -mass_scale
            * float(GLOBAL_SCALE)
            * proper_time
        )
        for proper_time in proper_times
    )
    assert transformed_fixed_mass_marks != fixed_mass_marks

    # If the mass parameter covaries inversely, the mark law is again
    # invariant. Merely adding a mark is insufficient; its scale must be
    # independently fixed.
    transformed_mass_scale = mass_scale / float(GLOBAL_SCALE)
    transformed_covarying_marks = tuple(
        math.exp(
            -transformed_mass_scale
            * float(GLOBAL_SCALE)
            * proper_time
        )
        for proper_time in proper_times
    )
    assert all(
        math.isclose(
            transformed,
            original,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        )
        for transformed, original in zip(
            transformed_covarying_marks,
            fixed_mass_marks,
            strict=True,
        )
    )

    # With fixed known m, the retained mark algebraically reconstructs the
    # proper time of each selected pair.
    reconstructed_proper_times = tuple(
        -math.log(mark) / mass_scale
        for mark in fixed_mass_marks
    )
    assert all(
        math.isclose(
            reconstructed,
            expected,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for reconstructed, expected in zip(
            reconstructed_proper_times,
            proper_times,
            strict=True,
        )
    )

    result = {
        "claim_id": "HC-DU-112",
        "status": "PASS",
        "controls": {
            "dimension": DIMENSION,
            "global_metric_scale": float(GLOBAL_SCALE),
            "poisson_intensity_measure_exactly_invariant": True,
            "representative_joint_count_probabilities_equal": True,
            "joint_count_probability_controls": joint_probabilities,
            "causal_order_exactly_invariant": True,
            "representative_unmarked_graph_statistics_invariant": True,
            "regional_density_absorbs_local_conformal_scale": True,
            "dimensionless_volume_ratios_invariant": True,
            "dimensionless_curvature_in_discreteness_units_invariant": True,
            "absolute_scale_nonidentifiable_from_unmarked_law": True,
            "fixed_dimensionful_mark_breaks_scale_gauge": True,
            "covarying_mark_restores_scale_gauge": True,
            "known_fixed_mark_reconstructs_selected_proper_times": True,
        },
        "boundary": (
            "Regression only: no physical density, dimensionful mark, clock, "
            "mass, interface, formation, provenance, access, certified "
            "record, new physics, prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-112 controls: complete causal-set scale gauge and "
        "fixed-versus-covarying marked anchor"
    )


if __name__ == "__main__":
    main()
