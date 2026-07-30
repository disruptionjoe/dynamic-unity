#!/usr/bin/env python3
"""Exact finite control for HC-DU-146.

Two four-qubit implementations use only probe--mediator gates and produce the
same final Bell pair plus the same reset mediator endpoint.  They differ only
in whether the component tagged G or Q carried the coherent mediation path.
A component-tagged interaction receipt distinguishes them.

This proves only a scoped attribution nonidentifiability statement.  It does
not model gravity, quantum field theory, constructor theory, an observed BMV
experiment, or new physics.
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
    / "du_mediator_component_attribution_result.json"
)

BitString: TypeAlias = tuple[int, int, int, int]
State: TypeAlias = dict[BitString, complex]

QUBITS = {"A": 0, "B": 1, "G": 2, "Q": 3}
TOLERANCE = 1e-12


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
    return {
        bits: amplitude
        for bits, amplitude in updated.items()
        if abs(amplitude) > TOLERANCE
    }


def inner_product(left: State, right: State) -> complex:
    return sum(
        amplitude.conjugate() * right.get(bits, 0j)
        for bits, amplitude in left.items()
    )


def fidelity(left: State, right: State) -> float:
    return abs(inner_product(left, right)) ** 2


def rounded_state(state: State) -> list[dict[str, object]]:
    return [
        {
            "bits_ABGQ": "".join(str(bit) for bit in bits),
            "amplitude_real": round(amplitude.real, 15),
            "amplitude_imag": round(amplitude.imag, 15),
        }
        for bits, amplitude in sorted(state.items())
    ]


def bell_state(active: str | None = None) -> State:
    scale = 1 / math.sqrt(2)
    if active is None:
        return {
            (0, 0, 0, 0): scale,
            (1, 1, 0, 0): scale,
        }
    active_index = QUBITS[active]
    excited = [1, 0, 0, 0]
    excited[active_index] = 1
    return {
        (0, 0, 0, 0): scale,
        tuple(excited): scale,  # type: ignore[dict-item]
    }


def run_completion(active: str) -> dict[str, object]:
    if active not in {"G", "Q"}:
        raise ValueError("active mediator must be G or Q")

    scale = 1 / math.sqrt(2)
    state: State = {
        (0, 0, 0, 0): scale,
        (1, 0, 0, 0): scale,
    }
    receipt: list[tuple[str, str, str]] = []
    snapshots = [state]

    for control, target in (
        ("A", active),
        (active, "B"),
        ("A", active),
    ):
        receipt.append(("CNOT", control, target))
        state = apply_cnot(state, control, target)
        snapshots.append(state)

    return {
        "active_component": active,
        "receipt": receipt,
        "snapshots": snapshots,
        "final_state": state,
        "no_direct_probe_gate": all(
            {control, target} != {"A", "B"}
            for _, control, target in receipt
        ),
        "active_midpoint_bell_fidelity": fidelity(
            snapshots[1],
            bell_state(active),
        ),
        "active_midpoint_exact": snapshots[1] == bell_state(active),
        "final_probe_bell_fidelity": fidelity(
            state,
            bell_state(),
        ),
        "final_probe_bell_exact": state == bell_state(),
    }


def build_result() -> dict[str, object]:
    gravity_active = run_completion("G")
    matter_active = run_completion("Q")

    gravity_final = gravity_active["final_state"]
    matter_final = matter_active["final_state"]
    if not isinstance(gravity_final, dict) or not isinstance(
        matter_final,
        dict,
    ):
        raise TypeError("final states must be amplitude dictionaries")

    endpoint_fidelity = fidelity(gravity_final, matter_final)
    endpoint_equal = gravity_final == matter_final
    receipts_distinct = (
        gravity_active["receipt"] != matter_active["receipt"]
    )

    assertions = {
        "both_paths_are_locally_mediated": bool(
            gravity_active["no_direct_probe_gate"]
            and matter_active["no_direct_probe_gate"]
        ),
        "active_component_carries_coherent_midpoint": bool(
            gravity_active["active_midpoint_exact"]
            and matter_active["active_midpoint_exact"]
        ),
        "same_complete_endpoint": endpoint_equal,
        "same_probe_bell_output": bool(
            gravity_active["final_probe_bell_exact"]
            and matter_active["final_probe_bell_exact"]
        ),
        "both_mediators_reset": all(
            bits[2:] == (0, 0)
            for bits in gravity_final | matter_final
        ),
        "component_receipt_distinguishes": receipts_distinct,
    }

    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-146",
        "arena": {
            "qubit_order": ["A", "B", "G", "Q"],
            "initial_probe_state": "|+>_A |0>_B",
            "initial_mediator_state": "|0>_G |0>_Q",
            "allowed_gates": "probe--mediator CNOT only",
        },
        "gravity_active_completion": {
            "receipt": gravity_active["receipt"],
            "midpoint": rounded_state(
                gravity_active["snapshots"][1]  # type: ignore[index]
            ),
            "final": rounded_state(gravity_final),
        },
        "matter_active_completion": {
            "receipt": matter_active["receipt"],
            "midpoint": rounded_state(
                matter_active["snapshots"][1]  # type: ignore[index]
            ),
            "final": rounded_state(matter_final),
        },
        "endpoint_fidelity": endpoint_fidelity,
        "assertions": assertions,
        "kernel_statement": (
            "The endpoint map identifies the two completions while the "
            "named active-component target separates them; therefore the "
            "target does not factor through the endpoint record."
        ),
        "minimum_repair": (
            "A physically formed, retained, and accessible component-tagged "
            "interaction receipt, or an intervention that isolates the "
            "component-specific path."
        ),
        "scope_guard": (
            "The finite circuit is an attribution counterexample, not a "
            "gravity model, BMV result, constructor-theory proof, or "
            "empirical prediction."
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
