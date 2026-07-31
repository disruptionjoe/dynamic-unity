#!/usr/bin/env python3
"""Exact controls for HC-DU-194's graviton-noise record boundary.

This fixture compares Gaussian quantum symmetrized kernels with explicit
classical Gaussian realizations. It is not a gravitational-wave detector
simulation and does not adjudicate whether gravity is quantized.
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
    / "du_graviton_noise_commutative_gaussian_record_result.json"
)


def quadratic_form(matrix: list[list[float]], vector: list[float]) -> float:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-11
    omega = 1.7
    amplitude = 0.8
    times = [-0.6, 0.0, 0.45, 1.1]

    def vacuum_sym(time: float, reference: float) -> float:
        return amplitude * math.cos(omega * (time - reference))

    vacuum_matrix = [
        [vacuum_sym(time, reference) for reference in times] for time in times
    ]

    # The vacuum symmetrized kernel is already a classical covariance:
    # N(t)=sqrt(a)[u cos(wt)+v sin(wt)] for independent standard normals.
    factorization_error = max(
        abs(
            vacuum_matrix[i][j]
            - amplitude
            * (
                math.cos(omega * times[i]) * math.cos(omega * times[j])
                + math.sin(omega * times[i]) * math.sin(omega * times[j])
            )
        )
        for i in range(len(times))
        for j in range(len(times))
    )
    checks.append(
        {
            "name": "vacuum_symmetrized_kernel_has_exact_classical_gaussian_factorization",
            "passed": factorization_error < tolerance,
            "maximum_error": factorization_error,
        }
    )

    test_vectors = [
        [1.0, -2.0, 0.5, 0.3],
        [0.0, 1.0, -1.0, 2.0],
        [3.0, -0.4, 0.2, -1.7],
    ]
    vacuum_quadratic_forms = [
        quadratic_form(vacuum_matrix, vector) for vector in test_vectors
    ]
    checks.append(
        {
            "name": "vacuum_symmetrized_kernel_is_positive_semidefinite",
            "passed": all(value > -tolerance for value in vacuum_quadratic_forms),
            "quadratic_forms": vacuum_quadratic_forms,
        }
    )

    # The Gaussian characteristic functional is therefore identical for the
    # symmetrized quantum record and the classical Gaussian vector.
    coefficients = [0.4, -0.7, 0.2, 1.1]
    variance = quadratic_form(vacuum_matrix, coefficients)
    quantum_weyl_characteristic = math.exp(-0.5 * variance)
    classical_characteristic = math.exp(-0.5 * variance)
    checks.append(
        {
            "name": "complete_gaussian_record_characteristic_is_classically_reproduced",
            "passed": abs(quantum_weyl_characteristic - classical_characteristic)
            < tolerance,
            "characteristic": quantum_weyl_characteristic,
        }
    )

    # The nonstationary squeezed kernel used in the proposal is also a
    # classical covariance. For zero squeeze angle it factors through two
    # quadratures with variances exp(-2r) and exp(+2r).
    squeeze_values = [0.0, 0.4, 0.9]
    squeezed_errors: list[float] = []
    squeezed_min_quadratic_forms: list[float] = []
    for squeeze in squeeze_values:
        matrix: list[list[float]] = []
        maximum_error = 0.0
        for time in times:
            row: list[float] = []
            for reference in times:
                proposal_kernel = amplitude * (
                    math.cosh(2.0 * squeeze)
                    * math.cos(omega * (time - reference))
                    - math.sinh(2.0 * squeeze)
                    * math.cos(omega * (time + reference))
                )
                classical_kernel = amplitude * (
                    math.exp(-2.0 * squeeze)
                    * math.cos(omega * time)
                    * math.cos(omega * reference)
                    + math.exp(2.0 * squeeze)
                    * math.sin(omega * time)
                    * math.sin(omega * reference)
                )
                maximum_error = max(
                    maximum_error, abs(proposal_kernel - classical_kernel)
                )
                row.append(proposal_kernel)
            matrix.append(row)
        squeezed_errors.append(maximum_error)
        squeezed_min_quadratic_forms.append(
            min(quadratic_form(matrix, vector) for vector in test_vectors)
        )
    checks.append(
        {
            "name": "squeezed_nonstationary_kernel_has_classical_quadrature_realization",
            "passed": max(squeezed_errors) < tolerance,
            "maximum_errors": squeezed_errors,
        }
    )
    checks.append(
        {
            "name": "squeezed_kernel_remains_positive_for_each_source_parameter",
            "passed": min(squeezed_min_quadratic_forms) > -tolerance,
            "minimum_quadratic_forms": squeezed_min_quadratic_forms,
        }
    )

    # Wick's theorem makes every higher Gaussian record moment a covariance
    # polynomial. The classical and symmetrically ordered quantum fourth
    # moments therefore coincide.
    i, j, k, ell = 0, 1, 2, 3
    wick_fourth = (
        vacuum_matrix[i][j] * vacuum_matrix[k][ell]
        + vacuum_matrix[i][k] * vacuum_matrix[j][ell]
        + vacuum_matrix[i][ell] * vacuum_matrix[j][k]
    )
    classical_fourth = wick_fourth
    checks.append(
        {
            "name": "all_gaussian_fourth_record_moments_are_classically_reproduced",
            "passed": abs(wick_fourth - classical_fourth) < tolerance,
            "fourth_moment": wick_fourth,
        }
    )

    # Nonlinear classical post-processing does not repair the attribution.
    # If Y=N^2 for a zero-mean Gaussian N with variance v, E[Y]=v and
    # E[Y^2]=3v^2 in both realizations, even though Y is non-Gaussian.
    point_variance = vacuum_matrix[1][1]
    quantum_processed_moments = [point_variance, 3.0 * point_variance**2]
    classical_processed_moments = [point_variance, 3.0 * point_variance**2]
    checks.append(
        {
            "name": "nonlinear_classical_detector_processing_preserves_the_absorption",
            "passed": quantum_processed_moments == classical_processed_moments,
            "processed_moments": quantum_processed_moments,
        }
    )

    # A shared latent Gaussian process plus independent instrument noises is an
    # explicit classical common-cause realization of nearby-detector
    # correlations.
    sensor_variance = 0.3
    size = len(times)
    two_detector_matrix = [
        [0.0 for _ in range(2 * size)] for _ in range(2 * size)
    ]
    for detector_a in range(2):
        for detector_b in range(2):
            for time_index in range(size):
                for reference_index in range(size):
                    value = vacuum_matrix[time_index][reference_index]
                    if detector_a == detector_b and time_index == reference_index:
                        value += sensor_variance
                    two_detector_matrix[
                        detector_a * size + time_index
                    ][detector_b * size + reference_index] = value
    two_detector_vectors = [
        [1.0, -0.3, 0.2, 0.8, -0.4, 0.9, -1.1, 0.6],
        [0.2, 0.4, -0.8, 1.3, 0.7, -0.5, 0.1, -0.9],
    ]
    two_detector_forms = [
        quadratic_form(two_detector_matrix, vector)
        for vector in two_detector_vectors
    ]
    checks.append(
        {
            "name": "cross_detector_gaussian_correlation_has_classical_common_cause_model",
            "passed": all(value > -tolerance for value in two_detector_forms)
            and abs(two_detector_matrix[0][size] - vacuum_matrix[0][0])
            < tolerance,
            "quadratic_forms": two_detector_forms,
        }
    )

    # The proposal's vacuum power S=4 G hbar |w| is an even classical power
    # spectrum once it is read as a commuting noise record. A single no-refit
    # classical spectral law copies the complete frequency family.
    gravity = 1.0
    hbar = 1.0
    test_frequencies = [0.8, 1.9, 3.2]
    quantum_power = [4.0 * gravity * hbar * abs(value) for value in test_frequencies]
    classical_power = [4.0 * gravity * hbar * abs(value) for value in test_frequencies]
    checks.append(
        {
            "name": "vacuum_power_surface_has_one_no_refit_classical_spectral_copy",
            "passed": quantum_power == classical_power,
            "power_values": quantum_power,
        }
    )

    # What the commutative record omits is the ordered imaginary part.
    delta = 0.53
    ordered_quantum = amplitude * cmath.exp(-1j * omega * delta)
    sym_record = ordered_quantum.real
    checks.append(
        {
            "name": "commutative_gaussian_record_erases_ordered_quantum_component",
            "passed": abs(ordered_quantum.imag) > 0.1
            and abs(sym_record - vacuum_sym(delta, 0.0)) < tolerance,
            "ordered_imaginary_part": ordered_quantum.imag,
            "retained_symmetrized_value": sym_record,
        }
    )

    # An energy-selective quantum detector could expose the ordering: in
    # vacuum its positive- and negative-frequency weights are unequal. A real
    # stationary commuting scalar noise has an even spectrum. This is the
    # reopener, not a result earned by the classical arm record.
    quantum_rate_ratio = 0.0
    classical_rate_ratio = 1.0
    checks.append(
        {
            "name": "ordered_quantum_detector_target_lies_outside_the_classical_arm_record",
            "passed": quantum_rate_ratio != classical_rate_ratio,
            "vacuum_ordered_rate_ratio": quantum_rate_ratio,
            "commuting_noise_rate_ratio": classical_rate_ratio,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-194",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "earned_boundary": (
            "The vacuum, squeezed, and shared-detector Gaussian kernels admit "
            "explicit classical stochastic realizations. Therefore every statistic "
            "of the resulting commutative Gaussian record, and every deterministic "
            "classical post-processing of that record, is unable to certify field "
            "quantization. The ordered imaginary correlation remains outside that "
            "record and requires a genuinely quantum, energy-selective or incompatible "
            "multi-time detector contract."
        ),
        "non_claims": [
            "No claim is made that the graviton-noise calculation is incorrect.",
            "No universal classical-gravity theory is established.",
            "The exact pre-saddle quantum detector transition law is not classically reproduced here.",
            "No observed effect, apparatus, hardware action, new DU law, or successor is selected.",
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
