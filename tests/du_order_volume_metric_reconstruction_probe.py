#!/usr/bin/env python3
"""Exact controls for HC-DU-111.

The scientific result is analytic. This probe preserves:

1. four-dimensional metric-scale recovery from conformal class plus volume;
2. exact finite-cell recovery in a piecewise-constant conformal family;
3. bounded volume-error to conformal-scale stability;
4. additive partition refinement with unique occurrence identity;
5. known-density Poisson precision and concentration;
6. exact global- and local-density scale gauges; and
7. a same-cell-volume/different-smooth-factor witness.

Passing establishes no physical volume selector, fundamental event density,
formed count record, complete acquisition, metric-independent partition,
unrestricted smooth-metric reconstruction, new physics, prediction, or
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
    / "du_order_volume_metric_reconstruction_result.json"
)

REFERENCE_VOLUMES: tuple[Fraction, ...] = (
    Fraction(1),
    Fraction(2),
    Fraction(5, 2),
    Fraction(7, 3),
)
CONFORMAL_FACTORS: tuple[Fraction, ...] = (
    Fraction(1),
    Fraction(3, 2),
    Fraction(2),
    Fraction(5, 4),
)


def cell_volumes(
    reference_volumes: tuple[Fraction, ...],
    conformal_factors: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        reference * omega**4
        for reference, omega in zip(
            reference_volumes,
            conformal_factors,
            strict=True,
        )
    )


def fourth_root(value: Fraction) -> float:
    return float(value) ** 0.25


def poisson_means(
    density: Fraction | tuple[Fraction, ...],
    reference_volumes: tuple[Fraction, ...],
    conformal_factors: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    densities = (
        (density,) * len(reference_volumes)
        if isinstance(density, Fraction)
        else density
    )
    return tuple(
        rho * reference * omega**4
        for rho, reference, omega in zip(
            densities,
            reference_volumes,
            conformal_factors,
            strict=True,
        )
    )


def main() -> None:
    volumes = cell_volumes(REFERENCE_VOLUMES, CONFORMAL_FACTORS)

    # In d=4, dvol_{Omega^2 gbar} = Omega^4 dvol_gbar. The exact
    # piecewise-constant inverse is the positive fourth root.
    recovered = tuple(
        fourth_root(volume / reference)
        for volume, reference in zip(
            volumes,
            REFERENCE_VOLUMES,
            strict=True,
        )
    )
    assert all(
        math.isclose(
            estimate,
            float(expected),
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for estimate, expected in zip(
            recovered,
            CONFORMAL_FACTORS,
            strict=True,
        )
    )

    # The determinant control makes the same fact explicit for one
    # representative: det(Omega^2 eta)=Omega^8 det(eta), hence
    # sqrt(|det|)=Omega^4.
    omega_control = Fraction(3, 2)
    metric_diagonal = (
        -(omega_control**2),
        omega_control**2,
        omega_control**2,
        omega_control**2,
    )
    determinant = math.prod(metric_diagonal)
    assert determinant == -(omega_control**8)
    assert math.sqrt(abs(float(determinant))) == float(omega_control**4)

    # Mean-value stability: for |delta| <= epsilon < 1,
    # |(1+delta)^(1/4)-1|
    # <= epsilon / (4(1-epsilon)^(3/4)).
    epsilon = 0.1
    stability_bound = epsilon / (4.0 * (1.0 - epsilon) ** 0.75)
    for step in range(-100, 101):
        delta = epsilon * step / 100.0
        relative_scale_error = abs((1.0 + delta) ** 0.25 - 1.0)
        assert relative_scale_error <= stability_bound + 1.0e-15

    # A volume measure is additive under benign refinement.
    parent_volume = volumes[2]
    children = (
        parent_volume * Fraction(1, 5),
        parent_volume * Fraction(3, 10),
        parent_volume * Fraction(1, 2),
    )
    assert sum(children, start=Fraction(0)) == parent_volume

    # Counts are additive only after occurrence identity prevents a duplicate
    # from being counted in two children.
    child_event_ids = (
        frozenset({"e1", "e2"}),
        frozenset({"e2", "e3"}),
    )
    naive_child_sum = sum(len(ids) for ids in child_event_ids)
    unique_parent_count = len(set().union(*child_event_ids))
    assert naive_child_sum == 4
    assert unique_parent_count == 3
    assert naive_child_sum != unique_parent_count

    # Known homogeneous Poisson density: Vhat=N/rho is unbiased with relative
    # standard deviation 1/sqrt(lambda). A standard two-sided multiplicative
    # Chernoff bound gives failure <= 2 exp(-lambda epsilon^2/3).
    poisson_lambda = 3000.0
    poisson_relative_sd = 1.0 / math.sqrt(poisson_lambda)
    poisson_epsilon = 0.1
    poisson_failure_bound = 2.0 * math.exp(
        -poisson_lambda * poisson_epsilon**2 / 3.0
    )
    lower_scale_ratio = (1.0 - poisson_epsilon) ** 0.25
    upper_scale_ratio = (1.0 + poisson_epsilon) ** 0.25
    assert poisson_relative_sd < 0.019
    assert poisson_failure_bound < 1.0e-4
    assert lower_scale_ratio < 1.0 < upper_scale_ratio

    # Unknown global density is exactly confounded with absolute scale.
    density = Fraction(5)
    original_means = poisson_means(
        density,
        REFERENCE_VOLUMES,
        CONFORMAL_FACTORS,
    )
    global_scale = Fraction(3)
    rescaled_factors = tuple(
        global_scale * omega for omega in CONFORMAL_FACTORS
    )
    rescaled_density = density / global_scale**4
    global_gauge_means = poisson_means(
        rescaled_density,
        REFERENCE_VOLUMES,
        rescaled_factors,
    )
    assert global_gauge_means == original_means
    # The common unknown density cancels from ratios, so relative scale remains
    # identifiable even though absolute scale does not.
    relative_scale_fourth_power = (
        (original_means[1] / REFERENCE_VOLUMES[1])
        / (original_means[0] / REFERENCE_VOLUMES[0])
    )
    assert relative_scale_fourth_power == (
        CONFORMAL_FACTORS[1] / CONFORMAL_FACTORS[0]
    ) ** 4

    # Unknown cell-dependent density absorbs arbitrary local scale changes.
    alternative_factors: tuple[Fraction, ...] = (
        Fraction(2),
        Fraction(1),
        Fraction(5, 2),
        Fraction(7, 4),
    )
    local_densities = tuple(
        density * (old / new) ** 4
        for old, new in zip(
            CONFORMAL_FACTORS,
            alternative_factors,
            strict=True,
        )
    )
    local_gauge_means = poisson_means(
        local_densities,
        REFERENCE_VOLUMES,
        alternative_factors,
    )
    assert local_gauge_means == original_means
    assert alternative_factors != CONFORMAL_FACTORS

    # One exact cell-volume integral cannot identify an unrestricted smooth
    # factor. On x in [0,1], q0=Omega0^4=1 and
    # q1=Omega1^4=x+1/2 are positive and integrate to one, but differ
    # pointwise. This is an exact polynomial-density witness.
    q0_integral = Fraction(1)
    q1_integral = Fraction(1, 2) + Fraction(1, 2)
    assert q0_integral == q1_integral == 1
    q0_samples = (
        Fraction(1),
        Fraction(1),
        Fraction(1),
    )
    q1_samples = (
        Fraction(1, 2),
        Fraction(1),
        Fraction(3, 2),
    )
    assert q0_samples != q1_samples
    assert all(value > 0 for value in q1_samples)

    result = {
        "claim_id": "HC-DU-111",
        "status": "PASS",
        "controls": {
            "dimension": 4,
            "piecewise_constant_cell_count": len(REFERENCE_VOLUMES),
            "cell_volume_map": "V_j = Omega_j^4 Vbar_j",
            "all_conformal_factors_exactly_recovered": True,
            "metric_determinant_volume_control": True,
            "relative_volume_error_epsilon": epsilon,
            "relative_scale_error_bound": stability_bound,
            "partition_refinement_volume_additive": True,
            "duplicate_event_id_breaks_naive_count_additivity": True,
            "poisson_known_density_control": {
                "lambda": poisson_lambda,
                "relative_standard_deviation": poisson_relative_sd,
                "relative_count_error": poisson_epsilon,
                "two_sided_failure_bound": poisson_failure_bound,
                "conformal_scale_ratio_interval": [
                    lower_scale_ratio,
                    upper_scale_ratio,
                ],
            },
            "unknown_global_density_absolute_scale_gauge": True,
            "unknown_global_density_preserves_relative_scale": True,
            "unknown_local_density_local_scale_gauge": True,
            "same_cell_volume_different_smooth_factor_witness": True,
        },
        "boundary": (
            "Regression only: no physical volume selector, fundamental event "
            "density, formed count record, complete acquisition, "
            "metric-independent partition, unrestricted smooth-metric "
            "reconstruction, new physics, prediction, or evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-111 controls: order-plus-volume metric reconstruction "
        "and event-density/provenance boundaries"
    )


if __name__ == "__main__":
    main()
