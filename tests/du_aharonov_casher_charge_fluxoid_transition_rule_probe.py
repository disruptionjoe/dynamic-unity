#!/usr/bin/env python3
"""Exact finite controls for HC-DU-225.

The probe verifies only the charge-parity/interference quotient, fluxoid
transition-graph topology, endpoint-certification boundary, and the smallest
time-reversal no-section. It is not a superconducting-device simulation or a
new prediction.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_aharonov_casher_charge_fluxoid_transition_rule_result.json"
)

CHARGES = tuple(range(-4, 5))
FLUXOIDS = tuple(range(-4, 5))
SIGNED_BRANCHES = (-1, 1)


def charge_parity(charge: int) -> int:
    return charge % 2


def path_sign(charge: int) -> int:
    return 1 if charge_parity(charge) == 0 else -1


def single_slip_amplitude(charge: int, left: int = 1, right: int = 1) -> int:
    return left + path_sign(charge) * right


def single_slip_rate(charge: int, left: int = 1, right: int = 1) -> int:
    return single_slip_amplitude(charge, left, right) ** 2


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


def allowed_steps(charge: int, left: int = 1, right: int = 1) -> tuple[int, ...]:
    steps = [-2, 2]
    if single_slip_amplitude(charge, left, right) != 0:
        steps.extend((-1, 1))
    return tuple(sorted(steps))


def neighbors(
    fluxoid: int,
    charge: int,
    left: int = 1,
    right: int = 1,
) -> tuple[int, ...]:
    return tuple(
        fluxoid + step
        for step in allowed_steps(charge, left, right)
        if fluxoid + step in FLUXOIDS
    )


def components(charge: int, left: int = 1, right: int = 1) -> tuple[tuple[int, ...], ...]:
    unseen = set(FLUXOIDS)
    blocks: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        queue = deque([seed])
        unseen.remove(seed)
        block = {seed}
        while queue:
            current = queue.popleft()
            for neighbor in neighbors(current, charge, left, right):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    block.add(neighbor)
                    queue.append(neighbor)
        blocks.append(tuple(sorted(block)))
    return tuple(sorted(blocks))


def graph_signature(charge: int, left: int = 1, right: int = 1) -> tuple[tuple[int, ...], ...]:
    return components(charge, left, right)


def endpoint_law(charge: int) -> dict[int, Fraction]:
    # Frozen illustrative one-step kernel: uniform over the reachable support
    # from winding zero, including no jump. It tests identifiability only.
    support = (0,) + neighbors(0, charge)
    probability = Fraction(1, len(support))
    return {outcome: probability for outcome in support}


def total_variation(left: dict[int, Fraction], right: dict[int, Fraction]) -> Fraction:
    outcomes = set(left) | set(right)
    return Fraction(1, 2) * sum(
        abs(left.get(outcome, Fraction(0)) - right.get(outcome, Fraction(0)))
        for outcome in outcomes
    )


def time_reversal_equivariant_map_exists() -> tuple[bool, int]:
    # Charge parity is T-even; signed winding is T-odd. Enumerate every map.
    maps = tuple(product(SIGNED_BRANCHES, repeat=2))
    equivariant = 0
    for values in maps:
        mapping = {0: values[0], 1: values[1]}
        if all(mapping[parity] == -mapping[parity] for parity in (0, 1)):
            equivariant += 1
    return equivariant > 0, equivariant


def oriented_writer(parity: int, orientation: int) -> int:
    return orientation * (1 if parity == 0 else -1)


def oriented_writer_is_equivariant() -> bool:
    return all(
        oriented_writer(parity, -orientation)
        == -oriented_writer(parity, orientation)
        for parity in (0, 1)
        for orientation in SIGNED_BRANCHES
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    symmetric_rates = {charge: single_slip_rate(charge) for charge in CHARGES}
    no_second_path_rates = {
        charge: single_slip_rate(charge, 1, 0) for charge in CHARGES
    }
    asymmetric_rates = {
        charge: single_slip_rate(charge, 2, 1) for charge in CHARGES
    }
    even_graph = graph_signature(0)
    odd_graph = graph_signature(1)
    odd_asymmetric_graph = graph_signature(1, 2, 1)
    even_law = endpoint_law(0)
    odd_law = endpoint_law(1)
    tv = total_variation(even_law, odd_law)
    optimal_error = Fraction(1, 2) * (1 - tv)
    no_section, equivariant_map_count = time_reversal_equivariant_map_exists()

    endpoint_histories = tuple(
        (charge, endpoint)
        for charge in CHARGES
        for endpoint in endpoint_law(charge)
    )

    checks = [
        (
            "symmetric interference suppresses single slips exactly for odd charge",
            all(
                (rate == 0) == (charge_parity(charge) == 1)
                for charge, rate in symmetric_rates.items()
            ),
        ),
        (
            "charge parity and single-slip rate induce the same source quotient",
            factors_through(CHARGES, charge_parity, single_slip_rate)
            and factors_through(CHARGES, single_slip_rate, charge_parity),
        ),
        (
            "full signed charge does not factor through the parity response",
            not factors_through(CHARGES, single_slip_rate, lambda charge: charge),
        ),
        (
            "even charge admits one connected fluxoid transition component",
            len(even_graph) == 1,
        ),
        (
            "odd charge selects exactly two fluxoid-parity components",
            len(odd_graph) == 2
            and all(len({value % 2 for value in block}) == 1 for block in odd_graph),
        ),
        (
            "charge parity selects the transition-graph topology",
            factors_through(CHARGES, charge_parity, graph_signature)
            and factors_through(CHARGES, graph_signature, charge_parity),
        ),
        (
            "removing the second coherent path erases charge sensitivity",
            len(set(no_second_path_rates.values())) == 1,
        ),
        (
            "path asymmetry removes exact parity protection",
            all(rate > 0 for rate in asymmetric_rates.values())
            and len(odd_asymmetric_graph) == 1,
        ),
        (
            "one realized endpoint does not reconstruct charge parity",
            not factors_through(
                endpoint_histories,
                lambda history: history[1],
                lambda history: charge_parity(history[0]),
            ),
        ),
        (
            "a parity-changing endpoint is a one-sided even-charge certificate",
            all(
                charge_parity(charge) == 0
                for charge, endpoint in endpoint_histories
                if endpoint % 2 == 1
            )
            and any(endpoint % 2 == 1 for _, endpoint in endpoint_histories),
        ),
        (
            "overlapping endpoint laws have nonzero optimal one-shot error",
            tv == Fraction(2, 5) and optimal_error == Fraction(3, 10),
        ),
        (
            "time reversal forbids a charge-only signed-winding selector",
            not no_section and equivariant_map_count == 0,
        ),
        (
            "a time-odd orientation makes an equivariant signed response possible",
            oriented_writer_is_equivariant(),
        ),
    ]

    result = {
        "claim_id": "HC-DU-225",
        "run_id": "RUN-20260902-aharonov-casher-charge-selected-fluxoid-transition-rule",
        "symmetric_single_slip_rates": symmetric_rates,
        "no_second_path_rates": no_second_path_rates,
        "asymmetric_path_rates": asymmetric_rates,
        "fluxoid_graphs": {
            "even_charge_components": even_graph,
            "odd_charge_components": odd_graph,
            "odd_charge_asymmetric_components": odd_asymmetric_graph,
        },
        "endpoint_laws": {
            "even": {str(key): str(value) for key, value in even_law.items()},
            "odd": {str(key): str(value) for key, value in odd_law.items()},
            "total_variation": str(tv),
            "optimal_equal_prior_error": str(optimal_error),
        },
        "time_reversal": {
            "charge_only_equivariant_signed_writer_exists": no_section,
            "equivariant_map_count": equivariant_map_count,
            "oriented_writer_equivariant": oriented_writer_is_equivariant(),
        },
        "checks": [{"name": name, "passed": passed} for name, passed in checks],
        "passed": sum(passed for _, passed in checks),
        "total": len(checks),
        "verdict": (
            "AHARONOV_CASHER_PHYSICAL_COUPLING_FOUND "
            "+ CHARGE_PARITY_SELECTS_TRANSITION_RULE "
            "+ FLUXOID_PARITY_PROTECTION_IS_CONDITIONAL "
            "+ FULL_CHARGE_IS_QUOTIENTED_AWAY "
            "+ TRANSITION_RULE_IS_NOT_RECORD_VALUE "
            "+ ONE_ENDPOINT_IS_NOT_ZERO_ERROR_CHARGE_CERTIFICATE "
            "+ TIME_REVERSAL_FORBIDS_UNBIASED_SIGNED_WRITE "
            "+ SYMMETRY_AND_ORIENTATION_REMAIN_ANTECEDENTS "
            "+ NO_COMPLETE_HC-DU-223-TO-224_HANDOFF "
            "+ NO_READY_SUCCESSOR"
        ),
        "maximum_grade": (
            "Scoped Grade 4 charge-selected transition-rule and equivariant "
            "writer obstruction; no new superconducting physics, prediction, "
            "complete handoff, issuance, or physical remainder"
        ),
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"checks: {result['passed']}/{result['total']}")
    print(f"verdict: {result['verdict']}")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
