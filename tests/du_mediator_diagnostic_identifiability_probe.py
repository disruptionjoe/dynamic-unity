#!/usr/bin/env python3
"""Exact finite regression for HC-DU-147.

The probe pair A,B interacts through one of two inaccessible candidate
mediators G,Q.  Swapping G and Q conjugates the two implementations while
fixing every probe-only preparation, intervention, and measurement.  Therefore
the complete probe input--output process cannot identify which named component
was active.

A calibrated component-selective X_G pulse breaks the symmetry and changes an
accessible probe-parity statistic.  The repair is deliberately not probe-only:
it records the additional physical access that named-component attribution
requires.

This is a finite symmetry regression, not a gravity model, a tomography
experiment, a universal system-identification theorem, or evidence of new
physics.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable, TypeAlias


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_mediator_diagnostic_identifiability_result.json"
)

BitString: TypeAlias = tuple[int, int, int, int]
State: TypeAlias = dict[BitString, complex]
SingleQubitGate: TypeAlias = tuple[
    tuple[complex, complex],
    tuple[complex, complex],
]
Control: TypeAlias = Callable[[State], State]

QUBITS = {"A": 0, "B": 1, "G": 2, "Q": 3}
TOLERANCE = 1e-12
SCALE = 1 / math.sqrt(2)

I_GATE: SingleQubitGate = ((1, 0), (0, 1))
X_GATE: SingleQubitGate = ((0, 1), (1, 0))
Z_GATE: SingleQubitGate = ((1, 0), (0, -1))
H_GATE: SingleQubitGate = ((SCALE, SCALE), (SCALE, -SCALE))
S_GATE: SingleQubitGate = ((1, 0), (0, 1j))


def clean(state: State) -> State:
    return {
        bits: amplitude
        for bits, amplitude in state.items()
        if abs(amplitude) > TOLERANCE
    }


def apply_single(
    state: State,
    qubit: str,
    gate: SingleQubitGate,
) -> State:
    index = QUBITS[qubit]
    updated: State = {}
    for bits, amplitude in state.items():
        input_bit = bits[index]
        for output_bit in (0, 1):
            coefficient = gate[output_bit][input_bit]
            if abs(coefficient) <= TOLERANCE:
                continue
            new_bits = list(bits)
            new_bits[index] = output_bit
            key = tuple(new_bits)  # type: ignore[assignment]
            updated[key] = (
                updated.get(key, 0j) + coefficient * amplitude
            )
    return clean(updated)


def apply_cnot(state: State, control: str, target: str) -> State:
    control_index = QUBITS[control]
    target_index = QUBITS[target]
    updated: State = {}
    for bits, amplitude in state.items():
        new_bits = list(bits)
        if bits[control_index] == 1:
            new_bits[target_index] ^= 1
        key = tuple(new_bits)  # type: ignore[assignment]
        updated[key] = updated.get(key, 0j) + amplitude
    return clean(updated)


def swap_mediators(state: State) -> State:
    return {
        (bits[0], bits[1], bits[3], bits[2]): amplitude
        for bits, amplitude in state.items()
    }


def vector_delta(left: State, right: State) -> float:
    return max(
        (
            abs(left.get(bits, 0j) - right.get(bits, 0j))
            for bits in set(left) | set(right)
        ),
        default=0.0,
    )


def single_qubit_state(label: str) -> tuple[complex, complex]:
    states = {
        "0": (1, 0),
        "1": (0, 1),
        "+": (SCALE, SCALE),
        "+i": (SCALE, 1j * SCALE),
    }
    return states[label]


def product_input(a_label: str, b_label: str) -> State:
    a_state = single_qubit_state(a_label)
    b_state = single_qubit_state(b_label)
    state: State = {}
    for a_bit, a_amplitude in enumerate(a_state):
        for b_bit, b_amplitude in enumerate(b_state):
            amplitude = a_amplitude * b_amplitude
            if abs(amplitude) > TOLERANCE:
                state[(a_bit, b_bit, 0, 0)] = amplitude
    return state


def control_family() -> dict[str, Control]:
    return {
        "I": lambda state: state,
        "X_A": lambda state: apply_single(state, "A", X_GATE),
        "Z_A": lambda state: apply_single(state, "A", Z_GATE),
        "H_A": lambda state: apply_single(state, "A", H_GATE),
        "S_A": lambda state: apply_single(state, "A", S_GATE),
        "X_B": lambda state: apply_single(state, "B", X_GATE),
        "Z_B": lambda state: apply_single(state, "B", Z_GATE),
        "H_B": lambda state: apply_single(state, "B", H_GATE),
        "CNOT_A_B": lambda state: apply_cnot(state, "A", "B"),
        "CNOT_B_A": lambda state: apply_cnot(state, "B", "A"),
    }


def run_route(
    initial: State,
    active: str,
    first_control: Control,
    second_control: Control,
    component_pulse: str | None = None,
) -> State:
    if active not in {"G", "Q"}:
        raise ValueError("active mediator must be G or Q")

    state = apply_cnot(initial, "A", active)
    if component_pulse is not None:
        state = apply_single(state, component_pulse, X_GATE)
    state = first_control(state)
    state = apply_cnot(state, active, "B")
    state = second_control(state)
    return apply_cnot(state, "A", active)


def reduced_probe_state(
    state: State,
) -> dict[tuple[int, int, int, int], complex]:
    reduced: dict[tuple[int, int, int, int], complex] = {}
    for left_bits, left_amplitude in state.items():
        for right_bits, right_amplitude in state.items():
            if left_bits[2:] != right_bits[2:]:
                continue
            key = (
                left_bits[0],
                left_bits[1],
                right_bits[0],
                right_bits[1],
            )
            reduced[key] = (
                reduced.get(key, 0j)
                + left_amplitude * right_amplitude.conjugate()
            )
    return {
        key: value
        for key, value in reduced.items()
        if abs(value) > TOLERANCE
    }


def matrix_delta(
    left: dict[tuple[int, int, int, int], complex],
    right: dict[tuple[int, int, int, int], complex],
) -> float:
    return max(
        (
            abs(left.get(key, 0j) - right.get(key, 0j))
            for key in set(left) | set(right)
        ),
        default=0.0,
    )


def odd_probe_parity_probability(state: State) -> float:
    return sum(
        abs(amplitude) ** 2
        for bits, amplitude in state.items()
        if bits[0] ^ bits[1]
    )


def rounded_state(state: State) -> list[dict[str, object]]:
    return [
        {
            "bits_ABGQ": "".join(str(bit) for bit in bits),
            "amplitude_real": round(amplitude.real, 15),
            "amplitude_imag": round(amplitude.imag, 15),
        }
        for bits, amplitude in sorted(state.items())
    ]


def build_result() -> dict[str, object]:
    controls = control_family()
    input_labels = ("0", "1", "+", "+i")

    initial_mediator_state = product_input("0", "0")
    initial_swap_delta = vector_delta(
        initial_mediator_state,
        swap_mediators(initial_mediator_state),
    )

    conjugation_delta = 0.0
    for index in range(16):
        bits = tuple(
            (index >> shift) & 1
            for shift in (3, 2, 1, 0)
        )
        basis = {bits: 1 + 0j}  # type: ignore[dict-item]
        left = run_route(
            basis,
            "Q",
            controls["I"],
            controls["I"],
        )
        right = swap_mediators(
            run_route(
                swap_mediators(basis),
                "G",
                controls["I"],
                controls["I"],
            )
        )
        conjugation_delta = max(
            conjugation_delta,
            vector_delta(left, right),
        )

    control_commutator_delta = 0.0
    for control in controls.values():
        for index in range(16):
            bits = tuple(
                (index >> shift) & 1
                for shift in (3, 2, 1, 0)
            )
            basis = {bits: 1 + 0j}  # type: ignore[dict-item]
            left = control(swap_mediators(basis))
            right = swap_mediators(control(basis))
            control_commutator_delta = max(
                control_commutator_delta,
                vector_delta(left, right),
            )

    protocol_count = 0
    max_full_swap_delta = 0.0
    max_probe_process_delta = 0.0
    for a_label in input_labels:
        for b_label in input_labels:
            initial = product_input(a_label, b_label)
            for first_control in controls.values():
                for second_control in controls.values():
                    gravity_route = run_route(
                        initial,
                        "G",
                        first_control,
                        second_control,
                    )
                    other_route = run_route(
                        initial,
                        "Q",
                        first_control,
                        second_control,
                    )
                    max_full_swap_delta = max(
                        max_full_swap_delta,
                        vector_delta(
                            other_route,
                            swap_mediators(gravity_route),
                        ),
                    )
                    max_probe_process_delta = max(
                        max_probe_process_delta,
                        matrix_delta(
                            reduced_probe_state(gravity_route),
                            reduced_probe_state(other_route),
                        ),
                    )
                    protocol_count += 1

    positive_initial = product_input("+", "0")
    gravity_positive = run_route(
        positive_initial,
        "G",
        controls["I"],
        controls["I"],
        component_pulse="G",
    )
    other_positive = run_route(
        positive_initial,
        "Q",
        controls["I"],
        controls["I"],
        component_pulse="G",
    )
    gravity_odd = odd_probe_parity_probability(gravity_positive)
    other_odd = odd_probe_parity_probability(other_positive)

    assertions = {
        "initial_mediator_state_is_swap_invariant": (
            initial_swap_delta <= TOLERANCE
        ),
        "routed_processes_are_swap_conjugate": (
            conjugation_delta <= TOLERANCE
        ),
        "all_probe_controls_commute_with_mediator_swap": (
            control_commutator_delta <= TOLERANCE
        ),
        "tomographic_probe_protocols_are_indistinguishable": (
            max_probe_process_delta <= TOLERANCE
        ),
        "full_outputs_differ_only_by_inaccessible_swap": (
            max_full_swap_delta <= TOLERANCE
        ),
        "named_active_component_differs": True,
        "component_selective_pulse_breaks_symmetry": (
            abs(gravity_odd - 1.0) <= TOLERANCE
            and abs(other_odd) <= TOLERANCE
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-147",
        "arena": {
            "qubit_order": ["A", "B", "G", "Q"],
            "probe_inputs": list(input_labels),
            "probe_control_family": list(controls),
            "probe_protocol_count": protocol_count,
            "mediator_initial_state": "|0>_G |0>_Q",
            "routed_gate_pattern": (
                "CNOT(A,M), probe control, CNOT(M,B), "
                "probe control, CNOT(A,M)"
            ),
        },
        "maximum_deltas": {
            "initial_swap": initial_swap_delta,
            "route_conjugation": conjugation_delta,
            "probe_control_commutator": control_commutator_delta,
            "full_output_after_swap": max_full_swap_delta,
            "reduced_probe_process": max_probe_process_delta,
        },
        "positive_control": {
            "operation": "X_G after the first routed coupling",
            "gravity_route_final_state": rounded_state(gravity_positive),
            "other_route_final_state": rounded_state(other_positive),
            "gravity_route_odd_AB_parity_probability": gravity_odd,
            "other_route_odd_AB_parity_probability": other_odd,
        },
        "assertions": assertions,
        "kernel_statement": (
            "The G/Q swap fixes the entire admitted probe process while "
            "flipping the named active-component target. The target therefore "
            "does not factor through complete probe input-output behavior."
        ),
        "minimum_repair": (
            "Break the inaccessible-factor stabilizer with independently "
            "calibrated component-selective control, known topology/coupling "
            "structure, retained component provenance, exclusive mediation, "
            "or a frozen component-specific excess prediction."
        ),
        "scope_guard": (
            "The regression verifies one exact finite symmetry class. The "
            "general all-probe statement follows from swap covariance, not "
            "from enumerating 1,600 protocols. Neither result identifies "
            "gravity, validates a proposed experiment, or predicts new physics."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the canonical JSON regression artifact",
    )
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
