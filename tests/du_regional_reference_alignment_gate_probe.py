#!/usr/bin/env python3
"""Exact/numerical controls for the regional reference-alignment gate.

The probe verifies the finite GHZ-coherence formulas used by HC-DU-174.
Passing establishes an access/reference boundary inside standard quantum
mechanics. It does not select a phase reference, record interface, observer,
consensus rule, collapse law, or physical ontology.
"""

from __future__ import annotations

import argparse
import cmath
import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_regional_reference_alignment_gate_result.json"
)
TOL = 1e-10

X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)


def tensor_all(operators: Sequence[np.ndarray]) -> np.ndarray:
    result = np.array([[1]], dtype=complex)
    for operator in operators:
        result = np.kron(result, operator)
    return result


def equatorial(angle: float) -> np.ndarray:
    return math.cos(angle) * X + math.sin(angle) * Y


def ghz_coherence_state(qubits: int, eta: complex) -> np.ndarray:
    """Return rho_eta on span{|0^n>, |1^n>}."""
    dimension = 2**qubits
    state = np.zeros((dimension, dimension), dtype=complex)
    state[0, 0] = 0.5
    state[-1, -1] = 0.5
    state[0, -1] = 0.5 * eta
    state[-1, 0] = 0.5 * eta.conjugate()
    return state


def product_response_matrix(eta: complex, angles: Sequence[float]) -> float:
    state = ghz_coherence_state(len(angles), eta)
    observable = tensor_all([equatorial(angle) for angle in angles])
    return float(np.trace(state @ observable).real)


def product_response_formula(eta: complex, angles: Sequence[float]) -> float:
    return float((eta * cmath.exp(1j * sum(angles))).real)


def partial_trace(
    state: np.ndarray,
    keep: Sequence[int],
    qubits: int,
) -> np.ndarray:
    kept = tuple(sorted(keep))
    traced = tuple(index for index in range(qubits) if index not in kept)
    out_dimension = 2 ** len(kept)
    result = np.zeros((out_dimension, out_dimension), dtype=complex)

    for row in range(2**qubits):
        row_bits = tuple((row >> (qubits - 1 - q)) & 1 for q in range(qubits))
        for column in range(2**qubits):
            column_bits = tuple(
                (column >> (qubits - 1 - q)) & 1 for q in range(qubits)
            )
            if any(row_bits[q] != column_bits[q] for q in traced):
                continue
            out_row = sum(
                row_bits[q] << (len(kept) - 1 - position)
                for position, q in enumerate(kept)
            )
            out_column = sum(
                column_bits[q] << (len(kept) - 1 - position)
                for position, q in enumerate(kept)
            )
            result[out_row, out_column] += state[row, column]
    return result


def first_fourier_moment(
    distribution: Sequence[tuple[float, float]],
) -> complex:
    return sum(
        probability * cmath.exp(1j * angle)
        for angle, probability in distribution
    )


def independent_error_average(
    eta: complex,
    nominal_angles: Sequence[float],
    distributions: Sequence[Sequence[tuple[float, float]]],
) -> float:
    total = 0.0
    for choices in itertools.product(*distributions):
        errors = [choice[0] for choice in choices]
        probability = math.prod(choice[1] for choice in choices)
        total += probability * product_response_formula(
            eta,
            [
                nominal + error
                for nominal, error in zip(nominal_angles, errors)
            ],
        )
    return total


def correlated_error_average(
    eta: complex,
    nominal_angles: Sequence[float],
    distribution: Iterable[tuple[Sequence[float], float]],
) -> float:
    return sum(
        probability
        * product_response_formula(
            eta,
            [
                nominal + error
                for nominal, error in zip(nominal_angles, errors)
            ],
        )
        for errors, probability in distribution
    )


def close(left: complex | float, right: complex | float) -> bool:
    return abs(left - right) <= TOL


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    # Direct matrix/formula controls across sizes and complex coherences.
    formula_errors: list[float] = []
    for qubits, eta, angles in (
        (2, 0.6 + 0.2j, (0.1, -0.4)),
        (3, -0.3 + 0.5j, (0.2, 0.7, -0.6)),
        (4, 0.8 - 0.1j, (0.3, -0.2, 0.4, 0.9)),
    ):
        matrix_value = product_response_matrix(eta, angles)
        formula_value = product_response_formula(eta, angles)
        formula_errors.append(abs(matrix_value - formula_value))
    checks.append(
        {
            "name": "reference_covariant_product_response_formula",
            "passed": max(formula_errors) <= TOL,
            "max_error": max(formula_errors),
        }
    )

    # The already-banked proper-coalition threshold remains a regression
    # control, not the new result.
    proper_subset_errors: list[float] = []
    for qubits in range(2, 6):
        coherent = ghz_coherence_state(qubits, 0.6 + 0.2j)
        mixture = ghz_coherence_state(qubits, 0j)
        for size in range(1, qubits):
            for keep in itertools.combinations(range(qubits), size):
                difference = partial_trace(coherent, keep, qubits) - partial_trace(
                    mixture, keep, qubits
                )
                proper_subset_errors.append(float(np.max(np.abs(difference))))
    checks.append(
        {
            "name": "proper_coalition_threshold_regression_only",
            "passed": max(proper_subset_errors) <= TOL,
            "max_error": max(proper_subset_errors),
        }
    )

    # Coordinate covariance: eta -> eta exp(-i sum alpha) and
    # theta_i -> theta_i + alpha_i leaves the relational response invariant.
    eta = 0.7 - 0.25j
    angles = (0.2, -0.5, 0.9)
    frame_changes = (0.4, -0.3, 0.8)
    baseline = product_response_formula(eta, angles)
    transformed_eta = eta * cmath.exp(-1j * sum(frame_changes))
    transformed_angles = tuple(
        angle + change for angle, change in zip(angles, frame_changes)
    )
    transformed = product_response_formula(transformed_eta, transformed_angles)
    checks.append(
        {
            "name": "state_and_measurement_frame_change_is_covariant",
            "passed": close(baseline, transformed),
            "baseline": baseline,
            "transformed": transformed,
        }
    )

    # Kernel of the collective character: absolute local changes with zero
    # total phase are operational gauge for this response.
    kernel_shift = (0.73, -0.21, -0.52)
    kernel_response = product_response_formula(
        eta,
        tuple(angle + shift for angle, shift in zip(angles, kernel_shift)),
    )
    checks.append(
        {
            "name": "zero_sum_local_frame_shift_is_in_collective_kernel",
            "passed": close(sum(kernel_shift), 0.0)
            and close(kernel_response, baseline),
            "kernel_sum": sum(kernel_shift),
        }
    )

    # Independent reference error multiplies the response by the product of
    # first Fourier moments.
    delta = 0.4
    distributions = (
        ((delta, 0.5), (-delta, 0.5)),
        ((0.2, 0.25), (-0.2, 0.75)),
        ((0.0, 0.6), (math.pi, 0.4)),
    )
    nominal = (0.0, 0.0, 0.0)
    enumerated_average = independent_error_average(eta, nominal, distributions)
    product_moment = math.prod(
        first_fourier_moment(distribution)
        for distribution in distributions
    )
    predicted_average = (
        eta * cmath.exp(1j * sum(nominal)) * product_moment
    ).real
    checks.append(
        {
            "name": "independent_reference_quality_factorizes",
            "passed": close(enumerated_average, predicted_average),
            "enumerated": enumerated_average,
            "predicted": predicted_average,
        }
    )

    # One independently uniform local reference is enough to erase the
    # coherent/mixed distinction from this regional parity statistic.
    uniform_quarter_turns = tuple(
        (turn * math.pi / 2, 0.25) for turn in range(4)
    )
    twirled_average = independent_error_average(
        eta,
        nominal,
        (
            uniform_quarter_turns,
            ((0.0, 1.0),),
            ((0.0, 1.0),),
        ),
    )
    checks.append(
        {
            "name": "one_independent_uniform_reference_twirl_closes_first_leak",
            "passed": close(twirled_average, 0.0),
            "twirled_response": twirled_average,
        }
    )

    # Absolute local orientation is not necessary. Two locally uniform but
    # perfectly anticorrelated errors keep the collective phase exact.
    correlated_distribution = tuple(
        (((turn * math.pi / 2), (-turn * math.pi / 2), 0.0), 0.25)
        for turn in range(4)
    )
    correlated_average = correlated_error_average(
        eta,
        nominal,
        correlated_distribution,
    )
    local_moment_1 = sum(
        probability * cmath.exp(1j * errors[0])
        for errors, probability in correlated_distribution
    )
    local_moment_2 = sum(
        probability * cmath.exp(1j * errors[1])
        for errors, probability in correlated_distribution
    )
    checks.append(
        {
            "name": "relational_alignment_survives_locally_uniform_frames",
            "passed": close(local_moment_1, 0j)
            and close(local_moment_2, 0j)
            and close(correlated_average, eta.real),
            "local_moment_1_abs": abs(local_moment_1),
            "local_moment_2_abs": abs(local_moment_2),
            "collective_response": correlated_average,
        }
    )

    # A fixed two-setting contract reconstructs the complex relational
    # coherence without choosing a phase-matched setting after the fact.
    x_response = product_response_formula(eta, (0.0, 0.0, 0.0))
    yxx_response = product_response_formula(
        eta,
        (math.pi / 2, 0.0, 0.0),
    )
    reconstructed_eta = complex(x_response, -yxx_response)
    checks.append(
        {
            "name": "fixed_two_setting_relational_phase_reconstruction",
            "passed": close(reconstructed_eta, eta),
            "reconstructed_real": reconstructed_eta.real,
            "reconstructed_imag": reconstructed_eta.imag,
        }
    )

    # Independent local dephasing and independent reference error multiply;
    # they remain different typed mechanisms.
    lambdas = (0.8, 0.75, 0.5)
    reference_moments = tuple(
        first_fourier_moment(distribution)
        for distribution in distributions
    )
    combined_eta = eta * math.prod(lambdas)
    dephased_enumerated = independent_error_average(
        combined_eta,
        nominal,
        distributions,
    )
    dephased_predicted = (
        eta * math.prod(lambdas) * math.prod(reference_moments)
    ).real
    checks.append(
        {
            "name": "dephasing_and_reference_quality_multiply_but_remain_typed",
            "passed": close(dephased_enumerated, dephased_predicted),
            "enumerated": dephased_enumerated,
            "predicted": dephased_predicted,
        }
    )

    # The same parity quadratures cannot attribute loss to physical
    # dephasing versus unresolved reference jitter when only their product is
    # observed.
    dephasing_twin = product_response_formula(
        0.8 + 0.2j,
        nominal,
    )
    reference_twin = product_response_formula(
        1.0 + 0.25j,
        nominal,
    ) * 0.8
    dephasing_twin_y = product_response_formula(
        0.8 + 0.2j,
        (math.pi / 2, 0.0, 0.0),
    )
    reference_twin_y = product_response_formula(
        1.0 + 0.25j,
        (math.pi / 2, 0.0, 0.0),
    ) * 0.8
    checks.append(
        {
            "name": "parity_quadratures_do_not_attribute_dephasing_vs_reference_loss",
            "passed": close(dephasing_twin, reference_twin)
            and close(dephasing_twin_y, reference_twin_y),
            "x_quadrature": dephasing_twin,
            "y_quadrature": dephasing_twin_y,
        }
    )

    # More independently misaligned regions suppress rather than sharpen the
    # parity signal. This is a smooth product law, not metastable consensus.
    quality = 0.9
    scaling = [quality**qubits for qubits in range(2, 9)]
    checks.append(
        {
            "name": "independent_reference_scaling_is_smooth_not_threshold",
            "passed": all(
                0 < scaling[index + 1] < scaling[index] < 1
                for index in range(len(scaling) - 1)
            ),
            "qualities_n_2_through_8": scaling,
        }
    )

    # A ninety-degree total mismatch can hide real coherence without
    # destroying it, distinguishing access failure from physical dephasing.
    real_eta = 0.8 + 0j
    aligned_response = product_response_formula(real_eta, nominal)
    misaligned_response = product_response_formula(
        real_eta,
        (math.pi / 2, 0.0, 0.0),
    )
    checks.append(
        {
            "name": "wrong_collective_basis_can_hide_undephased_coherence",
            "passed": close(aligned_response, 0.8)
            and close(misaligned_response, 0.0),
            "aligned_response": aligned_response,
            "misaligned_response": misaligned_response,
        }
    )

    passed = all(bool(check["passed"]) for check in checks)
    return {
        "probe": "du_regional_reference_alignment_gate_probe",
        "claim_id": "HC-DU-174",
        "status": "PASS" if passed else "FAIL",
        "checks_passed": sum(bool(check["passed"]) for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "theorem_surface": {
            "parity_response": "Re[eta exp(i sum_i theta_i)]",
            "frame_covariance": (
                "eta -> eta exp(-i sum_i alpha_i), "
                "theta_i -> theta_i + alpha_i"
            ),
            "reference_error_factor": (
                "E[exp(i sum_i delta_i)]; product of first Fourier moments "
                "only under independent errors"
            ),
            "independent_dephasing_factor": "product_i lambda_i",
            "relevant_reference_group": (
                "U(1)^n / ker(sum) ~= U(1), not n absolute phase origins"
            ),
        },
        "duplicate_guard": (
            "Proper-coalition GHZ indistinguishability and local-X parity "
            "pooling were already banked in HC-DU-035A/C and HC-DU-125. "
            "They are regression controls only."
        ),
        "interpretation": (
            "Regional quantum access composes only relative to a relational "
            "reference certificate. Independent local reference quality is "
            "insufficient: locally uniform but correlated frames can retain "
            "full joined access, while one independently twirled frame can "
            "erase it operationally."
        ),
        "scope_limit": (
            "Known GHZ, quantum-reference-frame, asymmetry, twirling, and "
            "dephasing mathematics. No reference, record, regionalization, "
            "consensus rule, actualization, or new physics is selected."
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
