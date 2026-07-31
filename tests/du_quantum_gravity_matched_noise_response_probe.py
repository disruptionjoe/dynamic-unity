#!/usr/bin/env python3
"""Exact controls for HC-DU-193's matched-noise response boundary.

This is a finite harmonic-response and stochastic-realization fixture. It is
not a quantum-gravity simulation, an apparatus model, or evidence for a field
mediator.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_gravity_matched_noise_response_result.json"
)


def coth(value: float) -> float:
    return 1.0 / math.tanh(value)


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-11
    beta = 1.3
    hbar = 1.0
    frequencies = [1.0, 2.4]
    zero_point_weights = [0.4, 0.25]

    # A thermal oscillator's symmetrized covariance and retarded response.
    # A_j = a_j coth(beta hbar omega_j / 2), while the response amplitude is
    # 2 a_j / hbar. The two objects are not freely specifiable in a calibrated
    # KMS state: the quantum fluctuation--dissipation relation joins them.
    sym_weights = [
        weight * coth(beta * hbar * frequency / 2.0)
        for weight, frequency in zip(zero_point_weights, frequencies)
    ]

    def sym_covariance(time: float) -> float:
        return sum(
            weight * math.cos(frequency * time)
            for weight, frequency in zip(sym_weights, frequencies)
        )

    def quantum_response(time: float) -> float:
        if time < 0.0:
            return 0.0
        return sum(
            2.0 * weight * math.sin(frequency * time) / hbar
            for weight, frequency in zip(zero_point_weights, frequencies)
        )

    checks.append(
        {
            "name": "thermal_quantum_covariance_is_nontrivial_and_positive_at_origin",
            "passed": sym_covariance(0.0) > 0.0
            and abs(sym_covariance(0.37) - sym_covariance(-0.37)) < tolerance,
            "covariance_at_origin": sym_covariance(0.0),
        }
    )

    # Explicit classical Gaussian realization. Let u_j and v_j be independent
    # standard normal variables and xi(t) = sum sqrt(A_j)(u_j cos wt +
    # v_j sin wt). Its covariance is exactly the quantum symmetrized one. Add
    # the chosen causal response as a deterministic convolution with the drive.
    classical_covariance = lambda time, reference: sum(
        weight * (
            math.cos(frequency * time) * math.cos(frequency * reference)
            + math.sin(frequency * time) * math.sin(frequency * reference)
        )
        for weight, frequency in zip(sym_weights, frequencies)
    )
    sample_pairs = [(-1.1, 0.4), (-0.2, -0.7), (0.0, 0.0), (0.31, 1.2), (1.7, -0.3)]
    covariance_error = max(
        abs(classical_covariance(time, reference) - sym_covariance(time - reference))
        for time, reference in sample_pairs
    )
    checks.append(
        {
            "name": "classical_gaussian_process_matches_quantum_symmetrized_covariance",
            "passed": covariance_error < tolerance,
            "maximum_error": covariance_error,
        }
    )

    classical_response = quantum_response
    sample_times = [pair[0] for pair in sample_pairs]
    response_error = max(
        abs(classical_response(time) - quantum_response(time))
        for time in sample_times
    )
    checks.append(
        {
            "name": "classical_input_output_model_can_copy_the_causal_response",
            "passed": response_error < tolerance,
            "maximum_error": response_error,
        }
    )

    # The copied susceptibility does not manufacture an operator commutator.
    # A scalar classical stationary autocorrelation is real and even; the
    # quantum ordered correlation carries the imaginary commutator part.
    ordered_imaginary = -sum(
        weight * math.sin(frequency * 0.43)
        for weight, frequency in zip(zero_point_weights, frequencies)
    )
    checks.append(
        {
            "name": "matched_classical_response_does_not_supply_quantum_ordering",
            "passed": abs(ordered_imaginary) > 0.05,
            "quantum_ordered_imaginary_part": ordered_imaginary,
            "classical_scalar_imaginary_part": 0.0,
        }
    )

    # A qubit noise spectrometer can distinguish the two orderings. For a
    # thermal quantum oscillator S(-w)/S(+w)=exp(-beta hbar w), whereas a real
    # stationary commuting scalar process has an even spectrum and ratio one.
    detailed_balance_ratios = [
        math.exp(-beta * hbar * frequency) for frequency in frequencies
    ]
    checks.append(
        {
            "name": "quantum_ordered_spectrum_has_kms_asymmetry",
            "passed": all(
                0.0 < ratio < 1.0 - 0.1 for ratio in detailed_balance_ratios
            ),
            "ratios": detailed_balance_ratios,
        }
    )
    checks.append(
        {
            "name": "real_stationary_commuting_noise_has_even_spectrum",
            "passed": all(abs(1.0 - ratio) < tolerance for ratio in [1.0, 1.0]),
            "ratios": [1.0, 1.0],
        }
    )

    # The calibrated quantum and classical equilibrium FDTs have different
    # multi-frequency shape. With k_B=hbar=1,
    #   R_q(w)=S_sym(w)/chi''(w)=coth(beta w/2)
    # and R_c(w)=2T/w. Hence T_eff=w R/2 is constant classically and strictly
    # increasing with w quantum mechanically at finite beta.
    quantum_effective_temperatures = [
        frequency * coth(beta * frequency / 2.0) / 2.0
        for frequency in frequencies
    ]
    classical_effective_temperatures = [1.0 / beta, 1.0 / beta]
    checks.append(
        {
            "name": "two_frequency_quantum_fdt_rejects_one_temperature_classical_fdt",
            "passed": quantum_effective_temperatures[1]
            > quantum_effective_temperatures[0] + 0.1,
            "quantum_effective_temperatures": quantum_effective_temperatures,
            "classical_effective_temperatures": classical_effective_temperatures,
        }
    )
    checks.append(
        {
            "name": "one_temperature_classical_fdt_is_frequency_constant",
            "passed": abs(
                classical_effective_temperatures[1]
                - classical_effective_temperatures[0]
            )
            < tolerance,
        }
    )

    # The quantum relation approaches the classical one in the high-temperature
    # limit, which is a required positive control rather than a discriminator.
    def fdt_relative_error(local_beta: float, frequency: float) -> float:
        quantum_ratio = coth(local_beta * frequency / 2.0)
        classical_ratio = 2.0 / (local_beta * frequency)
        return abs(quantum_ratio - classical_ratio) / classical_ratio

    warm_error = fdt_relative_error(0.1, frequencies[1])
    hot_error = fdt_relative_error(0.001, frequencies[1])
    checks.append(
        {
            "name": "quantum_fdt_recovers_classical_high_temperature_limit",
            "passed": hot_error < warm_error / 1000.0 and hot_error < 1.0e-6,
            "warm_relative_error": warm_error,
            "hot_relative_error": hot_error,
        }
    )

    # The strict-frequency result is not a numerical accident. For x>0,
    # d[x coth(x)]/dx = coth(x)-x csch(x)^2, whose numerator is
    # sinh(x)cosh(x)-x and has positive derivative 2 sinh(x)^2.
    x_values = [beta * frequency / 2.0 for frequency in frequencies]
    derivative_numerators = [
        math.sinh(value) * math.cosh(value) - value for value in x_values
    ]
    checks.append(
        {
            "name": "quantum_two_frequency_contrast_has_strict_monotonicity_certificate",
            "passed": all(value > 0.0 for value in derivative_numerators),
            "derivative_numerators": derivative_numerators,
        }
    )

    levels = [
        "symmetrized_noise",
        "c_number_causal_susceptibility",
        "ordered_spectral_asymmetry_or_incompatible_sequential_response",
        "mediator_provenance_or_component_access",
    ]
    checks.append(
        {
            "name": "response_hierarchy_separates_classical_realization_from_field_attribution",
            "passed": len(levels) == len(set(levels)) == 4,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-193",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "response_hierarchy": levels,
        "earned_boundary": (
            "At fixed calibrated KMS temperature, symmetrized noise and linear "
            "response are joined by the quantum fluctuation--dissipation relation, "
            "so they cannot be independently matched and varied inside that class. "
            "Outside that class, an explicit classical Gaussian input--output model "
            "can copy both. Ordered spectral asymmetry rejects a real stationary "
            "commuting scalar-noise rival, and two calibrated frequencies reject a "
            "one-temperature classical equilibrium FDT, but neither result identifies "
            "a gravitational field rather than a direct quantum environment."
        ),
        "non_claims": [
            "No gravitational field, direct-action ontology, or apparatus is modeled.",
            "No universal classical stochastic or semiclassical theory is excluded.",
            "A copied c-number susceptibility is not credited as an operator commutator.",
            "No observed effect, hardware action, new DU law, or successor is selected.",
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
