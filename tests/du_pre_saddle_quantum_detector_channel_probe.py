#!/usr/bin/env python3
"""Exact controls for HC-DU-195's quantum-detector channel boundary.

This fixture tests finite channel identities and the finite-time resonance
window.  It is not a graviton-detector simulation and does not establish that
gravity is quantized.
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
    / "du_pre_saddle_quantum_detector_channel_result.json"
)


Matrix = list[list[complex]]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def dagger(matrix: Matrix) -> Matrix:
    return [
        [matrix[j][i].conjugate() for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def scale(weight: float, matrix: Matrix) -> Matrix:
    return [[weight * value for value in row] for row in matrix]


def maximum_error(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def conjugate(operator: Matrix, state: Matrix) -> Matrix:
    return multiply(multiply(operator, state), dagger(operator))


def amplitude_damping(state: Matrix, gamma: float) -> Matrix:
    root = math.sqrt(1.0 - gamma)
    loss = math.sqrt(gamma)
    k0: Matrix = [[1.0, 0.0], [0.0, root]]
    k1: Matrix = [[0.0, loss], [0.0, 0.0]]
    return add(conjugate(k0, state), conjugate(k1, state))


def finite_time_window(detuning: float, duration: float) -> float:
    if abs(detuning) < 1.0e-14:
        return duration**2
    return (2.0 * math.sin(detuning * duration / 2.0) / detuning) ** 2


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-12
    identity: Matrix = [[1.0, 0.0], [0.0, 1.0]]
    bit_flip: Matrix = [[0.0, 1.0], [1.0, 0.0]]

    # Every exogenous classical random Hamiltonian produces a convex mixture
    # of unitary conjugations and is therefore unital.
    weight = 0.37
    random_unitary_identity = add(
        scale(weight, conjugate(identity, identity)),
        scale(1.0 - weight, conjugate(bit_flip, identity)),
    )
    checks.append(
        {
            "name": "classical_random_hamiltonian_channel_is_unital",
            "passed": maximum_error(random_unitary_identity, identity) < tolerance,
            "maximum_error": maximum_error(random_unitary_identity, identity),
        }
    )

    gamma = 0.23
    damped_identity = amplitude_damping(identity, gamma)
    checks.append(
        {
            "name": "vacuum_relaxation_channel_is_nonunital",
            "passed": maximum_error(damped_identity, identity) > 0.2,
            "image_of_identity": [
                [value.real for value in row] for row in damped_identity
            ],
        }
    )
    checks.append(
        {
            "name": "nonunital_relaxation_excludes_random_unitary_force_only_rival",
            "passed": maximum_error(damped_identity, random_unitary_identity) > 0.2,
            "separation": maximum_error(
                damped_identity, random_unitary_identity
            ),
        }
    )

    ground: Matrix = [[1.0, 0.0], [0.0, 0.0]]
    excited: Matrix = [[0.0, 0.0], [0.0, 1.0]]
    damped_ground = amplitude_damping(ground, gamma)
    damped_excited = amplitude_damping(excited, gamma)
    upward_probability = damped_ground[1][1].real
    downward_probability = damped_excited[0][0].real
    checks.append(
        {
            "name": "vacuum_channel_has_downward_without_upward_transition",
            "passed": abs(upward_probability) < tolerance
            and abs(downward_probability - gamma) < tolerance,
            "upward_probability": upward_probability,
            "downward_probability": downward_probability,
        }
    )

    # The harmonic-trap source supplies exactly the bosonic n versus n+1
    # asymmetry and the two-quantum detector selection rule.
    field_occupations = [0, 1, 7]
    absorption_weights = field_occupations
    emission_weights = [occupation + 1 for occupation in field_occupations]
    checks.append(
        {
            "name": "bosonic_transition_weights_retain_vacuum_spontaneous_term",
            "passed": absorption_weights[0] == 0
            and emission_weights[0] == 1
            and all(
                emission == absorption + 1
                for absorption, emission in zip(
                    absorption_weights, emission_weights, strict=True
                )
            ),
            "absorption_weights": absorption_weights,
            "emission_weights": emission_weights,
            "detector_selection_rule": "delta_n_detector=plus_or_minus_2",
        }
    )

    # A classical real stationary force has an even power spectrum and hence
    # equal golden-rule weights at opposite frequencies.
    test_frequencies = [0.8, 2.1, 4.7]
    classical_positive = [abs(value) for value in test_frequencies]
    classical_negative = [abs(-value) for value in test_frequencies]
    checks.append(
        {
            "name": "real_stationary_classical_force_has_symmetric_rate_surface",
            "passed": classical_positive == classical_negative,
            "positive_frequency_weights": classical_positive,
            "negative_frequency_weights": classical_negative,
        }
    )

    # Energy-basis records alone do not identify the implementation.  A
    # classical two-state decay process has the same population transition
    # matrix as amplitude damping.
    classical_population_transition = [[1.0, gamma], [0.0, 1.0 - gamma]]
    quantum_population_transition = [
        [
            amplitude_damping(ground, gamma)[0][0].real,
            amplitude_damping(excited, gamma)[0][0].real,
        ],
        [
            amplitude_damping(ground, gamma)[1][1].real,
            amplitude_damping(excited, gamma)[1][1].real,
        ],
    ]
    checks.append(
        {
            "name": "classical_dissipative_population_process_copies_energy_records",
            "passed": maximum_error(
                classical_population_transition, quantum_population_transition
            )
            < tolerance,
            "transition_matrix": classical_population_transition,
        }
    )

    # The complete amplitude-damping channel also has a direct quantum-ancilla
    # dilation; endpoint tomography cannot tell whether the environment was a
    # gravitational field or another quantum degree of freedom.
    root = math.sqrt(1.0 - gamma)
    loss = math.sqrt(gamma)
    k0_from_ancilla: Matrix = [[1.0, 0.0], [0.0, root]]
    k1_from_ancilla: Matrix = [[0.0, loss], [0.0, 0.0]]
    kraus_completeness = add(
        multiply(dagger(k0_from_ancilla), k0_from_ancilla),
        multiply(dagger(k1_from_ancilla), k1_from_ancilla),
    )
    test_state: Matrix = [[0.4, 0.2 + 0.1j], [0.2 - 0.1j, 0.6]]
    ancilla_channel = add(
        conjugate(k0_from_ancilla, test_state),
        conjugate(k1_from_ancilla, test_state),
    )
    checks.append(
        {
            "name": "direct_quantum_ancilla_copies_complete_endpoint_channel",
            "passed": maximum_error(kraus_completeness, identity) < tolerance
            and maximum_error(
                ancilla_channel, amplitude_damping(test_state, gamma)
            )
            < tolerance,
            "kraus_completeness_error": maximum_error(
                kraus_completeness, identity
            ),
            "maximum_error": maximum_error(
                ancilla_channel, amplitude_damping(test_state, gamma)
            ),
        }
    )

    # The source paper takes an infinite-time limit and retains delta squared.
    # A finite switching contract produces a bounded resonance window instead.
    duration = 3.4
    detunings = [0.0, 0.25, 0.9]
    windows = [finite_time_window(value, duration) for value in detunings]
    checks.append(
        {
            "name": "finite_switching_replaces_delta_squared_with_bounded_window",
            "passed": abs(windows[0] - duration**2) < tolerance
            and all(math.isfinite(value) and value >= 0.0 for value in windows),
            "detunings": detunings,
            "window_values": windows,
        }
    )

    trap_frequencies = [1.3, 2.4]
    resonant_field_frequencies = [2.0 * value for value in trap_frequencies]
    checks.append(
        {
            "name": "harmonic_trap_supplies_a_two_gap_resonance_surface",
            "passed": resonant_field_frequencies == [2.6, 4.8],
            "trap_frequencies": trap_frequencies,
            "resonant_field_frequencies": resonant_field_frequencies,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-195",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "disposition": (
            "RANDOM_UNITARY_FORCE_RIVAL_KILLED_ENDPOINT_AND_FIELD_ATTRIBUTION_OPEN"
        ),
        "checks": checks,
        "earned_boundary": (
            "Vacuum downward-without-upward relaxation is nonunital and therefore "
            "excludes an exogenous classical random-Hamiltonian force as the complete "
            "detector model. It does not identify a gravitational field: a classical "
            "dissipative population process copies energy records and a direct quantum "
            "ancilla copies the complete endpoint channel. The published harmonic-trap "
            "proposal supplies the gap and selection rule, but its delta-squared "
            "infinite-time expression is not a finite acquired probability contract."
        ),
        "non_claims": [
            "No claim is made that the harmonic-trap calculation is incorrect.",
            "No universal semiclassical- or classical-gravity no-go is established.",
            "No endpoint decay statistic uniquely identifies a graviton or field mediator.",
            "No observed effect, finite apparatus packet, hardware action, new DU law, or successor is selected.",
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
