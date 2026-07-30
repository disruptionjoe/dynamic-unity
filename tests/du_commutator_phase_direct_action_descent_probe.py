#!/usr/bin/env python3
"""Exact central-commutator descent control for HC-DU-148.

A source qubit S and probe qubit P act on one mediator qubit M through
controlled X and Z operations.  Their four-step group commutator returns M
exactly and induces a controlled phase on S,P.  A direct S--P phase operation
therefore reproduces the complete endpoint process for every input, although
mid-process access to M distinguishes the implementations.

This is a finite representation/attribution control.  It does not model
linearized gravity, derive the Chen--Giacomini phase, refute their proposed
functional-form tests, or establish a physical direct-action completion.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import TypeAlias


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_commutator_phase_direct_action_descent_result.json"
)

BitString: TypeAlias = tuple[int, int, int]
State: TypeAlias = dict[BitString, complex]

QUBITS = {"S": 0, "P": 1, "M": 2}
TOLERANCE = 1e-12
SCALE = 1 / math.sqrt(2)


def clean(state: State) -> State:
    return {
        bits: amplitude
        for bits, amplitude in state.items()
        if abs(amplitude) > TOLERANCE
    }


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


def apply_controlled_z(
    state: State,
    left: str,
    right: str,
) -> State:
    left_index = QUBITS[left]
    right_index = QUBITS[right]
    return clean(
        {
            bits: (
                -amplitude
                if bits[left_index] == bits[right_index] == 1
                else amplitude
            )
            for bits, amplitude in state.items()
        }
    )


def mediated_commutator(state: State) -> State:
    """Apply C_X(S,M), C_Z(P,M), C_X(S,M), C_Z(P,M)."""

    state = apply_cnot(state, "S", "M")
    state = apply_controlled_z(state, "P", "M")
    state = apply_cnot(state, "S", "M")
    return apply_controlled_z(state, "P", "M")


def direct_phase(state: State) -> State:
    return apply_controlled_z(state, "S", "P")


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


def product_input(
    source_label: str,
    probe_label: str,
    mediator_label: str,
) -> State:
    source = single_qubit_state(source_label)
    probe = single_qubit_state(probe_label)
    mediator = single_qubit_state(mediator_label)
    state: State = {}
    for source_bit, source_amplitude in enumerate(source):
        for probe_bit, probe_amplitude in enumerate(probe):
            for mediator_bit, mediator_amplitude in enumerate(mediator):
                amplitude = (
                    source_amplitude
                    * probe_amplitude
                    * mediator_amplitude
                )
                if abs(amplitude) > TOLERANCE:
                    state[
                        (source_bit, probe_bit, mediator_bit)
                    ] = amplitude
    return state


def mediator_one_probability(state: State) -> float:
    return sum(
        abs(amplitude) ** 2
        for bits, amplitude in state.items()
        if bits[QUBITS["M"]] == 1
    )


def rounded_state(state: State) -> list[dict[str, object]]:
    return [
        {
            "bits_SPM": "".join(str(bit) for bit in bits),
            "amplitude_real": round(amplitude.real, 15),
            "amplitude_imag": round(amplitude.imag, 15),
        }
        for bits, amplitude in sorted(state.items())
    ]


def build_result() -> dict[str, object]:
    basis_max_delta = 0.0
    phase_table: dict[str, int] = {}
    for source_bit in (0, 1):
        for probe_bit in (0, 1):
            for mediator_bit in (0, 1):
                bits = (source_bit, probe_bit, mediator_bit)
                initial = {bits: 1 + 0j}
                mediated = mediated_commutator(initial)
                direct = direct_phase(initial)
                basis_max_delta = max(
                    basis_max_delta,
                    vector_delta(mediated, direct),
                )
                phase = mediated.get(bits, 0j)
                if abs(phase.imag) > TOLERANCE:
                    raise AssertionError("basis phase must be real")
                phase_table["".join(str(bit) for bit in bits)] = int(
                    round(phase.real)
                )

    labels = ("0", "1", "+", "+i")
    spanning_max_delta = 0.0
    spanning_cases = 0
    for source_label in labels:
        for probe_label in labels:
            for mediator_label in labels:
                initial = product_input(
                    source_label,
                    probe_label,
                    mediator_label,
                )
                spanning_max_delta = max(
                    spanning_max_delta,
                    vector_delta(
                        mediated_commutator(initial),
                        direct_phase(initial),
                    ),
                )
                spanning_cases += 1

    positive_initial = product_input("+", "0", "0")
    mediated_midpoint = apply_cnot(
        positive_initial,
        "S",
        "M",
    )
    direct_midpoint = positive_initial
    mediated_mediator_one = mediator_one_probability(
        mediated_midpoint
    )
    direct_mediator_one = mediator_one_probability(direct_midpoint)

    assertions = {
        "basis_operator_equality": basis_max_delta <= TOLERANCE,
        "spanning_input_equality": spanning_max_delta <= TOLERANCE,
        "mediator_endpoint_restored_for_every_input": (
            spanning_max_delta <= TOLERANCE
        ),
        "only_joint_source_probe_one_gets_minus_phase": all(
            phase == (-1 if key[0:2] == "11" else 1)
            for key, phase in phase_table.items()
        ),
        "mediator_facing_midpoint_separates": (
            abs(mediated_mediator_one - 0.5) <= TOLERANCE
            and abs(direct_mediator_one) <= TOLERANCE
        ),
        "mediated_path_has_no_direct_source_probe_gate": True,
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-148",
        "arena": {
            "qubit_order": ["S", "P", "M"],
            "mediated_sequence": [
                "C_X(S,M)",
                "C_Z(P,M)",
                "C_X(S,M)",
                "C_Z(P,M)",
            ],
            "direct_sequence": ["C_Z(S,P)"],
            "tolerance": TOLERANCE,
        },
        "basis_cases": 8,
        "spanning_product_cases": spanning_cases,
        "basis_max_state_delta": basis_max_delta,
        "spanning_max_state_delta": spanning_max_delta,
        "basis_phase_table": phase_table,
        "positive_control": {
            "input": "|+>_S |0>_P |0>_M",
            "mediated_midpoint": rounded_state(mediated_midpoint),
            "direct_midpoint": rounded_state(direct_midpoint),
            "mediated_probability_M_equals_1": (
                mediated_mediator_one
            ),
            "direct_probability_M_equals_1": direct_mediator_one,
        },
        "assertions": assertions,
        "theorem_statement": (
            "A central mediator group commutator can induce an exact "
            "source--probe phase while returning the mediator identity. "
            "Complete endpoint behavior then factors through a direct "
            "source--probe action, whereas mediator-facing mid-process "
            "access separates the realizations."
        ),
        "scope_guard": (
            "This finite Weyl/Pauli control proves a representation and "
            "attribution boundary only. It does not reproduce linearized "
            "gravity, derive the Chen--Giacomini functional form, select a "
            "physical direct-action theory, or erase the proposed excess "
            "over Newtonian and declared classical models."
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
