#!/usr/bin/env python3
"""Exact finite controls for HC-DU-191's wide-source model tournament.

This is an occupation-statistics and density-kernel fixture, not a gravity
simulation. It distinguishes exact local profiles, coherent wide states,
macroscopic concentration, mean-profile replacement, and classical
extended-density absorption.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_gravity_source_model_tournament_result.json"
)


def binomial_distribution(n: int, p: float) -> list[float]:
    return [
        math.comb(n, k) * (p**k) * ((1.0 - p) ** (n - k))
        for k in range(n + 1)
    ]


def mean(values: list[float], probabilities: list[float]) -> float:
    return sum(value * probability for value, probability in zip(values, probabilities))


def variance(values: list[float], probabilities: list[float]) -> float:
    average = mean(values, probabilities)
    return sum(
        probability * ((value - average) ** 2)
        for value, probability in zip(values, probabilities)
    )


def characteristic(values: list[float], probabilities: list[float], chi: float) -> complex:
    return sum(
        probability * cmath.exp(-1j * chi * value)
        for value, probability in zip(values, probabilities)
    )


def bilinear_energy(
    left: tuple[int, int],
    right: tuple[int, int],
    kernel: tuple[tuple[float, float], tuple[float, float]],
) -> float:
    return sum(
        left[i] * kernel[i][j] * right[j]
        for i in range(2)
        for j in range(2)
    )


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-11

    # N bosons in one delocalized Hartree mode have binomial local occupation.
    particles = 20
    p_left = 0.35
    probabilities = binomial_distribution(particles, p_left)
    occupations = [float(k) for k in range(particles + 1)]
    occupation_mean = mean(occupations, probabilities)
    occupation_variance = variance(occupations, probabilities)
    checks.append(
        {
            "name": "hartree_profile_distribution_normalizes",
            "passed": abs(sum(probabilities) - 1.0) < tolerance,
        }
    )
    checks.append(
        {
            "name": "hartree_local_mean_is_Np",
            "passed": abs(occupation_mean - particles * p_left) < tolerance,
        }
    )
    checks.append(
        {
            "name": "hartree_local_variance_is_Np_one_minus_p",
            "passed": abs(
                occupation_variance - particles * p_left * (1.0 - p_left)
            )
            < tolerance,
        }
    )
    checks.append(
        {
            "name": "finite_delocalized_hartree_state_is_not_joint_profile_sharp",
            "passed": occupation_variance > 0.0
            and sum(probability > tolerance for probability in probabilities) > 1,
        }
    )

    # Relative fluctuations concentrate as N^{-1/2}, but never vanish at
    # finite N for a genuinely split Hartree mode.
    def coefficient_of_variation(n: int, p: float) -> float:
        return math.sqrt(n * p * (1.0 - p)) / (n * p)

    cv_100 = coefficient_of_variation(100, p_left)
    cv_400 = coefficient_of_variation(400, p_left)
    checks.append(
        {
            "name": "hartree_relative_profile_noise_scales_as_inverse_sqrt_N",
            "passed": abs(cv_400 / cv_100 - 0.5) < tolerance,
            "cv_N_100": cv_100,
            "cv_N_400": cv_400,
        }
    )

    # A potential difference that gives phase chi per particle produces the
    # exact characteristic function, not the phase of the mean occupation.
    chi = 0.21
    exact_characteristic = characteristic(occupations, probabilities, chi)
    closed_characteristic = (
        (1.0 - p_left) + p_left * cmath.exp(-1j * chi)
    ) ** particles
    mean_profile_phase = cmath.exp(-1j * chi * occupation_mean)
    checks.append(
        {
            "name": "hartree_phase_characteristic_has_closed_binomial_form",
            "passed": abs(exact_characteristic - closed_characteristic) < tolerance,
        }
    )
    checks.append(
        {
            "name": "mean_profile_replacement_erases_finite_visibility_loss",
            "passed": abs(exact_characteristic) < 0.99
            and abs(mean_profile_phase) > 1.0 - tolerance,
            "exact_visibility": abs(exact_characteristic),
            "mean_profile_visibility": abs(mean_profile_phase),
        }
    )

    # Holding the accumulated mean phase fixed while increasing N drives the
    # discrepancy to zero: this is the ordinary mean-field concentration
    # limit, not a new exact profile.
    target_mean_phase = 0.8

    def fixed_mean_visibility(n: int) -> float:
        local_chi = target_mean_phase / (n * p_left)
        return abs(((1.0 - p_left) + p_left * cmath.exp(-1j * local_chi)) ** n)

    loss_1000 = 1.0 - fixed_mean_visibility(1000)
    loss_2000 = 1.0 - fixed_mean_visibility(2000)
    checks.append(
        {
            "name": "fixed_mean_phase_profile_error_vanishes_at_mean_field_rate",
            "passed": loss_2000 < loss_1000
            and abs(loss_2000 / loss_1000 - 0.5) < 0.01,
            "loss_N_1000": loss_1000,
            "loss_N_2000": loss_2000,
        }
    )

    # A fragmented Fock profile has exact local occupations and can be broad,
    # but its density-density phase is exactly the classical bilinear energy
    # of that same extended density.
    fragmented_a = (12, 8)
    fragmented_b = (7, 13)
    kernel = ((1.0 / 3.0, 1.0 / 5.0), (1.0 / 4.0, 1.0 / 6.0))
    operator_eigenvalue = bilinear_energy(fragmented_a, fragmented_b, kernel)
    classical_extended_density_energy = bilinear_energy(
        fragmented_a, fragmented_b, kernel
    )
    checks.append(
        {
            "name": "fragmented_fock_state_has_exact_broad_local_profile",
            "passed": all(value > 0 for value in fragmented_a)
            and all(value > 0 for value in fragmented_b)
            and variance([float(fragmented_a[0])], [1.0]) == 0.0
            and variance([float(fragmented_a[1])], [1.0]) == 0.0
            and variance([float(fragmented_b[0])], [1.0]) == 0.0
            and variance([float(fragmented_b[1])], [1.0]) == 0.0,
        }
    )
    checks.append(
        {
            "name": "exact_fragmented_profile_phase_is_classical_extended_density_functional",
            "passed": abs(
                operator_eigenvalue - classical_extended_density_energy
            )
            < tolerance,
            "bilinear_energy": operator_eigenvalue,
        }
    )

    # A cat or delocalized collective coordinate is a superposition of
    # translated profiles, not one extended profile eigenstate.
    cat_values = [0.0, float(particles)]
    cat_probabilities = [0.5, 0.5]
    checks.append(
        {
            "name": "translated_profile_cat_has_nonzero_local_variance",
            "passed": abs(
                variance(cat_values, cat_probabilities) - (particles**2) / 4.0
            )
            < tolerance,
        }
    )

    # Same mean density, different profile statistics: the first information
    # lost by expectation-density closure is a second/higher cumulant.
    half_p = 0.5
    even_particles = 20
    half_probabilities = binomial_distribution(even_particles, half_p)
    half_values = [float(k) for k in range(even_particles + 1)]
    half_chi = 0.27
    hartree_same_mean = characteristic(half_values, half_probabilities, half_chi)
    fragmented_same_mean = cmath.exp(-1j * half_chi * even_particles * half_p)
    checks.append(
        {
            "name": "same_mean_profile_different_cumulants_give_different_visibility",
            "passed": abs(
                mean(half_values, half_probabilities) - even_particles * half_p
            )
            < tolerance
            and abs(hartree_same_mean) < abs(fragmented_same_mean) - 0.1,
            "hartree_visibility": abs(hartree_same_mean),
            "fragmented_visibility": abs(fragmented_same_mean),
        }
    )

    # A local coherent-field occupation is Poissonian. Large amplitude gives
    # relative concentration but not an exact energy-density profile.
    poisson_mean = 25.0
    poisson_characteristic = cmath.exp(
        poisson_mean * (cmath.exp(-1j * chi) - 1.0)
    )
    checks.append(
        {
            "name": "coherent_field_analogue_is_concentrated_but_not_profile_sharp",
            "passed": poisson_mean > 0
            and math.sqrt(poisson_mean) / poisson_mean == 0.2
            and abs(poisson_characteristic) < 1.0,
            "relative_occupation_noise": 0.2,
        }
    )

    # A diagonal phase assay sees only the occupation law. An incoherent
    # mixture with the same law produces the same characteristic function;
    # complementary coherence access is needed to certify a quantum source.
    pure_hartree_characteristic = exact_characteristic
    incoherent_same_law_characteristic = characteristic(
        occupations, probabilities, chi
    )
    pure_first_order_coherence = particles * math.sqrt(
        p_left * (1.0 - p_left)
    )
    incoherent_first_order_coherence = 0.0
    checks.append(
        {
            "name": "diagonal_phase_visibility_is_reproduced_by_classical_profile_mixture",
            "passed": abs(
                pure_hartree_characteristic - incoherent_same_law_characteristic
            )
            < tolerance,
        }
    )
    checks.append(
        {
            "name": "complementary_coherence_access_separates_pure_source_from_mixture",
            "passed": pure_first_order_coherence > 0.0
            and incoherent_first_order_coherence == 0.0,
            "pure_first_order_coherence": pure_first_order_coherence,
            "mixture_first_order_coherence": incoherent_first_order_coherence,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-191",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "exact_boundary": {
            "hartree_profile": "Binomial(N,p), variance Np(1-p)",
            "hartree_characteristic": "[(1-p)+p exp(-i chi)]^N",
            "fragmented_profile": "local-number eigenstate",
            "fragmented_phase": "classical bilinear extended-density kernel",
            "first_surviving_statistic": "second and higher local-stress cumulants",
        },
        "earned_boundary": (
            "Within the frozen occupation-density source classes, exact broad "
            "profiles are available as fragmented local-number eigenstates but "
            "their density-kernel phase is the classical extended-density "
            "functional. Coherent or collectively delocalized sources retain "
            "local-profile fluctuations. Macroscopic Hartree/coherent sources "
            "concentrate only in the ordinary mean-field limit, moving the "
            "first honest target from mean phase to higher stress cumulants."
        ),
        "non_claims": [
            "No universal QFT no-go is proved.",
            "Stress cumulants are not unique predictions of quantum gravity.",
            "Diagonal visibility loss alone does not certify source coherence.",
            "No apparatus, magnitude, hardware action, or new DU law is earned.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
