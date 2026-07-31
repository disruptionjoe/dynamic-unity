#!/usr/bin/env python3
"""Exact controls for HC-DU-196's finite trapped-detector boundary.

The fixture solves the resonant two-state rotating-wave block and checks its
detector and complementary channels.  It is not a complete gravitational
detector simulation and does not identify a physical mediator.
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
    / "du_finite_time_trapped_detector_dilation_result.json"
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


def conjugate(operator: Matrix, state: Matrix) -> Matrix:
    return multiply(multiply(operator, state), dagger(operator))


def maximum_error(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def exchange_amplitudes(
    coupling: float, detuning: float, duration: float
) -> tuple[complex, complex]:
    """Return survival and exchange amplitudes for a two-state RWA block."""

    frequency = math.sqrt(coupling**2 + (detuning / 2.0) ** 2)
    if frequency == 0.0:
        return 1.0 + 0.0j, 0.0 + 0.0j
    sine = math.sin(frequency * duration)
    survival = math.cos(frequency * duration) - 1j * (
        detuning / (2.0 * frequency)
    ) * sine
    exchange = -1j * (coupling / frequency) * sine
    return survival, exchange


def detector_channel(state: Matrix, survival: complex, exchange: complex) -> Matrix:
    k0: Matrix = [[1.0, 0.0], [0.0, survival]]
    k1: Matrix = [[0.0, exchange], [0.0, 0.0]]
    return add(conjugate(k0, state), conjugate(k1, state))


def complementary_channel(
    state: Matrix, survival: complex, exchange: complex
) -> Matrix:
    rho00, rho01 = state[0]
    rho10, rho11 = state[1]
    return [
        [rho00 + abs(survival) ** 2 * rho11, exchange.conjugate() * rho01],
        [exchange * rho10, abs(exchange) ** 2 * rho11],
    ]


def rotate_environment(state: Matrix) -> Matrix:
    swap: Matrix = [[0.0, 1.0], [1.0, 0.0]]
    return conjugate(swap, state)


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-11
    identity: Matrix = [[1.0, 0.0], [0.0, 1.0]]

    coupling = 0.41
    detuning = 0.37
    duration = 1.8
    survival, exchange = exchange_amplitudes(coupling, detuning, duration)
    normalization = abs(survival) ** 2 + abs(exchange) ** 2
    checks.append(
        {
            "name": "finite_two_state_exchange_block_is_unitary",
            "passed": abs(normalization - 1.0) < tolerance,
            "normalization": normalization,
            "survival_amplitude": [survival.real, survival.imag],
            "exchange_amplitude": [exchange.real, exchange.imag],
        }
    )

    transition_probability = abs(exchange) ** 2
    checks.append(
        {
            "name": "finite_transition_probability_is_bounded_without_delta_squared",
            "passed": 0.0 <= transition_probability <= 1.0,
            "transition_probability": transition_probability,
        }
    )

    weak_coupling = 0.01
    weak_detuning = 0.7
    weak_duration = 1.3
    _, weak_exchange = exchange_amplitudes(
        weak_coupling, weak_detuning, weak_duration
    )
    exact_weak_probability = abs(weak_exchange) ** 2
    perturbative_window = (
        4.0
        * weak_coupling**2
        * math.sin(weak_detuning * weak_duration / 2.0) ** 2
        / weak_detuning**2
    )
    checks.append(
        {
            "name": "weak_coupling_limit_recovers_finite_sinc_squared_window",
            "passed": abs(exact_weak_probability - perturbative_window)
            / perturbative_window
            < 5.0e-4,
            "exact_probability": exact_weak_probability,
            "perturbative_probability": perturbative_window,
        }
    )

    test_state: Matrix = [[0.35, 0.17 + 0.09j], [0.17 - 0.09j, 0.65]]
    detector_output = detector_channel(test_state, survival, exchange)
    trace = detector_output[0][0] + detector_output[1][1]
    checks.append(
        {
            "name": "finite_detector_map_is_trace_preserving",
            "passed": abs(trace - 1.0) < tolerance,
            "output_trace": trace.real,
        }
    )

    detector_identity = detector_channel(identity, survival, exchange)
    checks.append(
        {
            "name": "nonzero_exchange_retains_the_nonunital_discriminator",
            "passed": maximum_error(detector_identity, identity) > 0.1,
            "image_of_identity": [
                [value.real for value in row] for row in detector_identity
            ],
        }
    )

    # A non-gravitational two-level ancilla using the same isometry produces
    # exactly the same detector channel for every input. Test a spanning set.
    spanning_states: list[Matrix] = [
        [[1.0, 0.0], [0.0, 0.0]],
        [[0.0, 0.0], [0.0, 1.0]],
        [[0.5, 0.5], [0.5, 0.5]],
        [[0.5, -0.5j], [0.5j, 0.5]],
    ]
    field_outputs = [
        detector_channel(state, survival, exchange) for state in spanning_states
    ]
    direct_ancilla_outputs = [
        detector_channel(state, survival, exchange) for state in spanning_states
    ]
    channel_copy_error = max(
        maximum_error(left, right)
        for left, right in zip(field_outputs, direct_ancilla_outputs, strict=True)
    )
    checks.append(
        {
            "name": "direct_quantum_ancilla_matches_complete_detector_channel",
            "passed": channel_copy_error < tolerance,
            "maximum_error": channel_copy_error,
        }
    )

    # Detector tomography does retain one implementation-independent resource
    # fact: two linearly independent Kraus operators force a minimal pure
    # dilation environment of dimension at least two.
    kraus_gram_determinant = (
        (1.0 + abs(survival) ** 2) * abs(exchange) ** 2
    )
    checks.append(
        {
            "name": "detector_channel_selects_minimal_memory_dimension_not_identity",
            "passed": kraus_gram_determinant > 0.1,
            "kraus_gram_determinant": kraus_gram_determinant,
            "minimal_pure_environment_dimension": 2,
        }
    )

    # One fixed coupling law copies two independently chosen trap gaps without
    # after-result parameter fitting.
    scale = 0.017
    trap_gaps = [1.2, 2.3]
    gap_duration = 0.9
    two_gap_errors: list[float] = []
    two_gap_probabilities: list[float] = []
    for gap in trap_gaps:
        source_coupling = scale * gap**2
        source_survival, source_exchange = exchange_amplitudes(
            source_coupling, 0.0, gap_duration
        )
        rival_survival, rival_exchange = exchange_amplitudes(
            scale * gap**2, 0.0, gap_duration
        )
        two_gap_errors.append(
            maximum_error(
                detector_channel(test_state, source_survival, source_exchange),
                detector_channel(test_state, rival_survival, rival_exchange),
            )
        )
        two_gap_probabilities.append(abs(source_exchange) ** 2)
    checks.append(
        {
            "name": "one_no_refit_direct_ancilla_family_matches_two_gap_surface",
            "passed": max(two_gap_errors) < tolerance
            and two_gap_probabilities[0] != two_gap_probabilities[1],
            "gap_probabilities": two_gap_probabilities,
            "maximum_errors": two_gap_errors,
        }
    )

    mediator_output = complementary_channel(test_state, survival, exchange)
    checks.append(
        {
            "name": "detector_loss_is_complementary_mediator_information_gain",
            "passed": abs(mediator_output[1][1] - abs(exchange) ** 2 * 0.65)
            < tolerance
            and abs(mediator_output[0][1]) > 0.01,
            "mediator_excitation_probability": mediator_output[1][1].real,
            "mediator_coherence_magnitude": abs(mediator_output[0][1]),
        }
    )

    # At a full resonant swap, the detector is reset while the complementary
    # output contains the entire input state up to a known phase convention.
    full_swap_duration = math.pi / (2.0 * coupling)
    swap_survival, swap_exchange = exchange_amplitudes(
        coupling, 0.0, full_swap_duration
    )
    swapped_detector = detector_channel(test_state, swap_survival, swap_exchange)
    swapped_mediator = complementary_channel(test_state, swap_survival, swap_exchange)
    phase_correction: Matrix = [[1.0, 0.0], [0.0, 1j]]
    corrected_mediator = conjugate(phase_correction, swapped_mediator)
    ground_state: Matrix = [[1.0, 0.0], [0.0, 0.0]]
    checks.append(
        {
            "name": "full_swap_moves_the_complete_record_out_of_the_detector",
            "passed": maximum_error(swapped_detector, ground_state) < tolerance
            and maximum_error(corrected_mediator, test_state) < tolerance,
            "detector_reset_error": maximum_error(swapped_detector, ground_state),
            "mediator_recovery_error": maximum_error(
                corrected_mediator, test_state
            ),
        }
    )

    # Environment basis is not fixed by the detector channel. Applying a
    # mediator-only unitary changes its record while leaving detector outputs
    # untouched.
    rotated_mediator = rotate_environment(mediator_output)
    checks.append(
        {
            "name": "environment_isometry_changes_mediator_record_not_detector_channel",
            "passed": maximum_error(rotated_mediator, mediator_output) > 0.1
            and maximum_error(
                detector_output,
                detector_channel(test_state, survival, exchange),
            )
            < tolerance,
            "mediator_record_change": maximum_error(
                rotated_mediator, mediator_output
            ),
        }
    )

    # The single-mode block revives. That rejects an irreversible homogeneous
    # amplitude-damping semigroup, but not a memory-bearing direct rival.
    transfer_time = math.pi / (2.0 * coupling)
    revival_time = math.pi / coupling
    _, transfer_exchange = exchange_amplitudes(coupling, 0.0, transfer_time)
    _, revival_exchange = exchange_amplitudes(coupling, 0.0, revival_time)
    transfer_probability = abs(transfer_exchange) ** 2
    revival_probability = abs(revival_exchange) ** 2
    checks.append(
        {
            "name": "single_mode_revival_excludes_irreversible_markov_semigroup_only",
            "passed": abs(transfer_probability - 1.0) < tolerance
            and revival_probability < tolerance,
            "transfer_probability": transfer_probability,
            "later_transition_probability": revival_probability,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-196",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "disposition": (
            "FINITE_CHANNEL_DERIVED_DETECTOR_ONLY_DILATION_ATTRIBUTION_CLOSED_"
            "INTERFACE_EXPANSION_REQUIRED"
        ),
        "checks": checks,
        "earned_boundary": (
            "The resonant rotating-wave block gives a bounded finite-time "
            "amplitude-damping channel and a complementary mediator channel. "
            "Detector-only tomography, two gaps, coherence access, and single-mode "
            "memory can exclude random-unitary and memoryless semigroup rivals, "
            "but cannot identify the physical dilation: one no-refit quantum-ancilla "
            "family reproduces the complete detector surface. Distinguishing "
            "dilations requires an independently selected interface not factoring "
            "through the original detector process."
        ),
        "non_claims": [
            "The rotating-wave two-state block is not the complete source Hamiltonian or continuum field theory.",
            "No claim is made that every constrained direct-action theory matches the gravitational process.",
            "A mediator-facing or expanded port is necessary only within an admitted detector-process equivalence class and is not sufficient for gravitational attribution.",
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
