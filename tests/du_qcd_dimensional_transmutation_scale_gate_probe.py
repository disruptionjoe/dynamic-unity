#!/usr/bin/env python3
"""Exact controls for HC-DU-113.

The scientific result is analytic and literature-grounded. This probe
preserves:

1. one-loop asymptotically free RG flow and its invariant Lambda coordinate;
2. the unfixed integration constant and reference-value equivalence;
3. common energy-scale covariance;
4. one-loop scheme rescaling with invariant physical masses and ratios;
5. lattice scale matching from one measured dimensionful observable;
6. fixed-matter-mark metric calibration;
7. common metric-matter unit covariance; and
8. failure of one global unit change to absorb unequal local scale changes.

Passing establishes no QCD mass-gap proof, selected Standard-Model parameter,
physical clock, formed record, provenance, access, metric reconstruction in
nature, new physics, prediction, or evidence grade.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_qcd_dimensional_transmutation_scale_gate_result.json"
)

BETA_ZERO = 0.5
LAMBDA_REFERENCE = 0.2


def running_coupling(mu: float, lambda_scale: float) -> float:
    assert mu > lambda_scale > 0.0
    return math.sqrt(
        1.0
        / (
            2.0
            * BETA_ZERO
            * math.log(mu / lambda_scale)
        )
    )


def lambda_from_coupling(mu: float, coupling: float) -> float:
    return mu * math.exp(
        -1.0
        / (2.0 * BETA_ZERO * coupling**2)
    )


def mark(mass_scale: float, proper_time: float) -> float:
    return math.exp(-mass_scale * proper_time)


def main() -> None:
    # Every point on one RG trajectory reconstructs the same integration
    # constant Lambda.
    energy_scales = (1.0, 2.0, 5.0, 10.0, 100.0)
    couplings = tuple(
        running_coupling(mu, LAMBDA_REFERENCE)
        for mu in energy_scales
    )
    reconstructed_lambdas = tuple(
        lambda_from_coupling(mu, coupling)
        for mu, coupling in zip(
            energy_scales,
            couplings,
            strict=True,
        )
    )
    assert all(
        math.isclose(
            reconstructed,
            LAMBDA_REFERENCE,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for reconstructed in reconstructed_lambdas
    )

    # The beta law fixes the slope in log(mu), not the trajectory's origin.
    # Distinct positive Lambdas give distinct couplings at one fixed energy
    # while satisfying the same integrated flow equation.
    lambda_family = (0.1, 0.2, 0.4)
    fixed_energy = 10.0
    family_couplings = tuple(
        running_coupling(fixed_energy, lambda_scale)
        for lambda_scale in lambda_family
    )
    assert len(set(family_couplings)) == len(lambda_family)
    for lambda_scale, coupling in zip(
        lambda_family,
        family_couplings,
        strict=True,
    ):
        assert math.isclose(
            lambda_from_coupling(fixed_energy, coupling),
            lambda_scale,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )

    # Reference-value equivalence: giving g(mu0) and giving Lambda are
    # one-to-one inside this controlled solution family.
    reference_energy = 20.0
    reference_coupling = running_coupling(
        reference_energy,
        LAMBDA_REFERENCE,
    )
    assert math.isclose(
        lambda_from_coupling(
            reference_energy,
            reference_coupling,
        ),
        LAMBDA_REFERENCE,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )

    # Jointly changing every energy unit preserves dimensionless running:
    # g_{Lambda/c}(mu/c)=g_Lambda(mu).
    common_unit_scale = 3.0
    rescaled_couplings = tuple(
        running_coupling(
            mu / common_unit_scale,
            LAMBDA_REFERENCE / common_unit_scale,
        )
        for mu in energy_scales
    )
    assert all(
        math.isclose(
            transformed,
            original,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for transformed, original in zip(
            rescaled_couplings,
            couplings,
            strict=True,
        )
    )

    # At one-loop order a finite inverse-coupling shift u'=u-2a rescales
    # Lambda by exp(a/b0). Coefficients transform inversely so physical
    # masses and their ratios stay fixed.
    scheme_parameter = 0.08
    scheme_factor = math.exp(scheme_parameter / BETA_ZERO)
    lambda_scheme_b = LAMBDA_REFERENCE * scheme_factor
    inverse_coupling_a = (
        1.0
        / running_coupling(
            fixed_energy,
            LAMBDA_REFERENCE,
        )
        ** 2
    )
    inverse_coupling_b = inverse_coupling_a - 2.0 * scheme_parameter
    reconstructed_scheme_b = fixed_energy * math.exp(
        -inverse_coupling_b / (2.0 * BETA_ZERO)
    )
    assert math.isclose(
        reconstructed_scheme_b,
        lambda_scheme_b,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )

    mass_coefficients_a = (3.1, 4.7, 8.25)
    mass_coefficients_b = tuple(
        coefficient / scheme_factor
        for coefficient in mass_coefficients_a
    )
    physical_masses_a = tuple(
        coefficient * LAMBDA_REFERENCE
        for coefficient in mass_coefficients_a
    )
    physical_masses_b = tuple(
        coefficient * lambda_scheme_b
        for coefficient in mass_coefficients_b
    )
    assert all(
        math.isclose(
            first,
            second,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for first, second in zip(
            physical_masses_a,
            physical_masses_b,
            strict=True,
        )
    )
    mass_ratios_a = tuple(
        mass / physical_masses_a[0]
        for mass in physical_masses_a[1:]
    )
    mass_ratios_b = tuple(
        mass / physical_masses_b[0]
        for mass in physical_masses_b[1:]
    )
    assert all(
        math.isclose(
            first,
            second,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for first, second in zip(
            mass_ratios_a,
            mass_ratios_b,
            strict=True,
        )
    )

    # Lattice output supplies dimensionless a*M values. One measured
    # reference mass fixes a in inverse-energy units. Without that input,
    # a->c*a and M->M/c preserve every lattice product and mass ratio.
    lattice_mass_products = (0.47, 0.68, 0.94)
    measured_reference_mass = 1.672
    lattice_spacing = (
        lattice_mass_products[-1] / measured_reference_mass
    )
    predicted_masses = tuple(
        product / lattice_spacing
        for product in lattice_mass_products
    )
    assert math.isclose(
        predicted_masses[-1],
        measured_reference_mass,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    alternative_spacing = 2.0 * lattice_spacing
    alternative_masses = tuple(
        mass / 2.0 for mass in predicted_masses
    )
    assert all(
        math.isclose(
            alternative_spacing * mass,
            product,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for mass, product in zip(
            alternative_masses,
            lattice_mass_products,
            strict=True,
        )
    )
    assert all(
        math.isclose(
            alternative_masses[index]
            / alternative_masses[0],
            predicted_masses[index]
            / predicted_masses[0],
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for index in range(1, len(predicted_masses))
    )

    # A fixed physical mass or transition scale breaks a metric-scale rival
    # and reconstructs selected proper times in units of that scale.
    physical_standard = measured_reference_mass
    proper_times = (0.1, 0.25, 0.5, 1.0)
    fixed_standard_marks = tuple(
        mark(physical_standard, proper_time)
        for proper_time in proper_times
    )
    metric_scale = 1.5
    metric_rescaled_marks = tuple(
        mark(
            physical_standard,
            metric_scale * proper_time,
        )
        for proper_time in proper_times
    )
    assert metric_rescaled_marks != fixed_standard_marks
    reconstructed_times = tuple(
        -math.log(value) / physical_standard
        for value in fixed_standard_marks
    )
    assert all(
        math.isclose(
            reconstructed,
            expected,
            rel_tol=0.0,
            abs_tol=1.0e-12,
        )
        for reconstructed, expected in zip(
            reconstructed_times,
            proper_times,
            strict=True,
        )
    )

    # Co-rescaling metric intervals and every declared matter energy inversely
    # is a common-unit transformation in this controlled observable class:
    # all dimensionless marks stay fixed.
    common_unit_marks = tuple(
        mark(
            physical_standard / metric_scale,
            metric_scale * proper_time,
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
            common_unit_marks,
            fixed_standard_marks,
            strict=True,
        )
    )

    # This is a full unit change only if every other admitted dimensional
    # scale co-transforms. Holding an external sector fixed changes a
    # dimensionless inter-sector ratio and therefore defines a physical rival.
    external_energy_scale = 1000.0 * physical_standard
    original_intersector_ratio = (
        physical_standard / external_energy_scale
    )
    partial_rescaling_ratio = (
        (physical_standard / metric_scale) / external_energy_scale
    )
    assert not math.isclose(
        partial_rescaling_ratio,
        original_intersector_ratio,
        rel_tol=0.0,
        abs_tol=1.0e-15,
    )
    full_rescaling_ratio = (
        (physical_standard / metric_scale)
        / (external_energy_scale / metric_scale)
    )
    assert math.isclose(
        full_rescaling_ratio,
        original_intersector_ratio,
        rel_tol=0.0,
        abs_tol=1.0e-15,
    )

    # One global matter-unit rescaling cannot absorb two unequal local metric
    # factors. Exact absorption would require a locally varying mass standard,
    # which changes the physical matter-law contract.
    local_metric_scales = (1.2, 1.7)
    local_times = (0.4, 0.4)
    local_fixed_marks = tuple(
        mark(
            physical_standard,
            scale * proper_time,
        )
        for scale, proper_time in zip(
            local_metric_scales,
            local_times,
            strict=True,
        )
    )
    assert local_fixed_marks[0] != local_fixed_marks[1]
    required_local_mass_rescalings = tuple(
        physical_standard / scale
        for scale in local_metric_scales
    )
    assert (
        required_local_mass_rescalings[0]
        != required_local_mass_rescalings[1]
    )

    result = {
        "claim_id": "HC-DU-113",
        "status": "PASS",
        "controls": {
            "one_loop_rg_invariant_lambda_reconstructed": True,
            "beta_law_leaves_lambda_integration_constant_free": True,
            "reference_coupling_and_lambda_are_equivalent_parameters": True,
            "common_energy_unit_covariance": True,
            "scheme_change_rescales_lambda": True,
            "physical_masses_and_ratios_scheme_invariant": True,
            "lattice_physical_scale_requires_one_measured_mass": True,
            "unmatched_lattice_global_scale_gauge": True,
            "fixed_matter_mark_breaks_metric_scale_gauge": True,
            "fixed_matter_mark_reconstructs_selected_proper_times": True,
            "joint_rescaling_of_all_admitted_scales_is_common_unit_gauge": True,
            "partial_rescaling_against_fixed_sector_changes_physical_ratio": True,
            "unequal_local_metric_scales_require_local_matter_law_refit": True,
        },
        "boundary": (
            "Regression only: no QCD mass-gap proof, selected Standard-Model "
            "parameter, physical clock, formed record, provenance, access, "
            "metric reconstruction in nature, new physics, prediction, or "
            "evidence grade."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS HC-DU-113 controls: QCD dimensional-transmutation scale "
        "provenance, common-unit gauge, and fixed-matter anchor"
    )


if __name__ == "__main__":
    main()
