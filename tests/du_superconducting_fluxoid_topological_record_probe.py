#!/usr/bin/env python3
"""Exact finite controls for HC-DU-224.

The discrete cycle represents nonvanishing U(1) phase configurations with
principal increments. Local moves redistribute phase gradient without crossing
zero; the connected components are winding sectors. Passing proves only the
finite topology, target-factorization, orientation, and provenance controls.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_superconducting_fluxoid_topological_record_result.json"
)

MODULUS = 5
EDGE_COUNT = 6
PRINCIPAL_INCREMENTS = tuple(range(-2, 3))
State = tuple[int, ...]
History = tuple[State, str]
BlankOrState = State | None


def states() -> tuple[State, ...]:
    return tuple(
        increments
        for increments in product(PRINCIPAL_INCREMENTS, repeat=EDGE_COUNT)
        if sum(increments) % MODULUS == 0
    )


def winding(state: State) -> int:
    return sum(state) // MODULUS


def winding_or_none(state: BlankOrState) -> int | None:
    return None if state is None else winding(state)


def parity(state: State) -> int:
    return winding(state) % 2


def orientation_reverse(state: State) -> State:
    return tuple(-value for value in reversed(state))


def local_neighbors(state: State, domain: frozenset[State]) -> tuple[State, ...]:
    result: list[State] = []
    for left in range(EDGE_COUNT):
        right = (left + 1) % EDGE_COUNT
        for step in (-1, 1):
            candidate = list(state)
            candidate[left] += step
            candidate[right] -= step
            candidate_tuple = tuple(candidate)
            if candidate_tuple in domain:
                result.append(candidate_tuple)
    return tuple(result)


def connected_components(domain: frozenset[State]) -> tuple[frozenset[State], ...]:
    unseen = set(domain)
    components: list[frozenset[State]] = []
    while unseen:
        seed = min(unseen)
        queue = deque([seed])
        unseen.remove(seed)
        component = {seed}
        while queue:
            current = queue.popleft()
            for neighbor in local_neighbors(current, domain):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        components.append(frozenset(component))
    return tuple(components)


def factors_through(
    domain: Iterable[Hashable],
    view: Callable[[Hashable], Hashable],
    target: Callable[[Hashable], Hashable],
) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for item in domain:
        key = view(item)
        value = target(item)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def witness(
    domain: Iterable[Hashable],
    view: Callable[[Hashable], Hashable],
    target: Callable[[Hashable], Hashable],
) -> tuple[Hashable, Hashable] | None:
    items = tuple(domain)
    for index, left in enumerate(items):
        for right in items[index + 1 :]:
            if view(left) == view(right) and target(left) != target(right):
                return left, right
    return None


def persistent_current(state: State) -> Fraction:
    # Frozen dimensionless London/circuit response at external flux 1/4 Phi_0.
    return Fraction(winding(state), 1) - Fraction(1, 4)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    domain = frozenset(states())
    components = connected_components(domain)
    winding_blocks: dict[int, set[State]] = defaultdict(set)
    for state in domain:
        winding_blocks[winding(state)].add(state)

    component_blocks = frozenset(components)
    expected_blocks = frozenset(
        frozenset(block) for block in winding_blocks.values()
    )
    winding_values = tuple(sorted(winding_blocks))
    binary_domain = tuple(
        state for state in domain if winding(state) in (0, 1)
    )
    histories: tuple[History, ...] = tuple(
        (state, route)
        for state in domain
        for route in ("passive_quench", "field_biased_quench")
    )

    microstate_witness = witness(domain, winding, lambda state: state)
    provenance_witness = witness(
        histories,
        lambda history: winding(history[0]),
        lambda history: history[1],
    )
    parity_current_witness = witness(domain, parity, persistent_current)

    zero = (0,) * EDGE_COUNT
    one = (1, 1, 1, 1, 1, 0)

    checks = [
        (
            "nonvanishing local-deformation components equal winding sectors",
            component_blocks == expected_blocks,
        ),
        (
            "five winding sectors occur in the frozen finite carrier",
            winding_values == (-2, -1, 0, 1, 2),
        ),
        (
            "central winding sectors strictly compress phase microstates",
            all(len(winding_blocks[value]) > 1 for value in (-1, 0, 1)),
        ),
        (
            "orientation reversal negates winding",
            all(
                winding(orientation_reverse(state)) == -winding(state)
                for state in domain
            ),
        ),
        (
            "winding parity survives orientation reversal",
            all(
                parity(orientation_reverse(state)) == parity(state)
                for state in domain
            ),
        ),
        (
            "winding determines frozen persistent-current response",
            factors_through(domain, winding, persistent_current),
        ),
        (
            "binary winding parity determines response in the two-sector window",
            factors_through(binary_domain, parity, persistent_current),
        ),
        (
            "binary parity fails outside the two-sector operating window",
            not factors_through(domain, parity, persistent_current)
            and parity_current_witness is not None,
        ),
        (
            "winding record does not reconstruct phase microstate",
            microstate_witness is not None,
        ),
        (
            "winding record does not reconstruct formation provenance",
            provenance_witness is not None,
        ),
        (
            "phase-slip jump crosses disconnected winding components",
            winding(zero) == 0
            and winding(one) == 1
            and not any(zero in block and one in block for block in components),
        ),
        (
            "normal blank has no winding while every admitted condensate does",
            winding_or_none(None) is None
            and all(winding_or_none(state) is not None for state in domain),
        ),
    ]

    result = {
        "claim_id": "HC-DU-224",
        "run_id": "RUN-20260902-superconducting-fluxoid-topological-material-record",
        "carrier": {
            "modulus": MODULUS,
            "edge_count": EDGE_COUNT,
            "nonvanishing_state_count": len(domain),
            "winding_values": winding_values,
            "component_sizes": {
                str(value): len(winding_blocks[value]) for value in winding_values
            },
            "normal_blank_winding": None,
        },
        "factorization": {
            "full_winding_to_persistent_current": factors_through(
                domain, winding, persistent_current
            ),
            "binary_parity_to_current_in_window": factors_through(
                binary_domain, parity, persistent_current
            ),
            "binary_parity_to_current_full_family": factors_through(
                domain, parity, persistent_current
            ),
        },
        "witnesses": {
            "same_winding_different_microstate": microstate_witness,
            "same_winding_different_provenance": provenance_witness,
            "same_parity_different_full_family_current": parity_current_witness,
            "phase_slip_component_jump": (zero, one),
        },
        "checks": [
            {"name": name, "passed": passed} for name, passed in checks
        ],
        "passed": sum(passed for _, passed in checks),
        "total": len(checks),
        "verdict": (
            "TOPOLOGY_SELECTS_MATERIAL_RECORD_COORDINATE "
            "+ BLANK_TO_WRITTEN_FLUXOID_FORMATION "
            "+ NONZERO_ORDER_PARAMETER_PROTECTS_WINDING "
            "+ PHASE_SLIP_IS_THE_ERASURE_GATE "
            "+ BINARY_WINDOW_TARGET_SUFFICIENCY "
            "+ FULL_SECTOR_AND_PROVENANCE_FIRST_LEAK "
            "+ READOUT_REVEALS_BUT_DOES_NOT_CREATE_RECORD "
            "+ CONDITIONAL_MATERIAL_POSITIVE_NOT_UNIVERSAL_SELECTOR "
            "+ DOES_NOT_COMPLETE_HC-DU-223_CHARGE_HANDOFF "
            "+ NO_READY_SUCCESSOR"
        ),
        "maximum_grade": (
            "Scoped Grade 4 exact finite topology and target-relative material-"
            "record boundary; no universal selector, issuance, permanent finality, "
            "prediction, or new physics"
        ),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"checks: {result['passed']}/{result['total']}")
    print(f"verdict: {result['verdict']}")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
