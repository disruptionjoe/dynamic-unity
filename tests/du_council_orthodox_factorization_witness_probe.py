#!/usr/bin/env python3
"""Exact finite controls for the HC-DU-036 deterministic specialization.

This probe does not test a physical ontology.  It checks the finite
factorization-or-witness theorem, its tight intervention-length bound, the
minimal stable behavioral refinement, and the absence of a size-free
certification horizon.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations, product
import json
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_council_orthodox_factorization_witness_result.json"
)


def canonical_partition(values: Sequence[object]) -> tuple[int, ...]:
    """Return restricted-growth labels for equality among ``values``."""

    labels: dict[object, int] = {}
    out: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        out.append(labels[value])
    return tuple(out)


def set_partitions(n: int) -> Iterable[tuple[int, ...]]:
    """Generate every partition of ``range(n)`` as restricted-growth labels."""

    if n == 0:
        yield ()
        return

    def extend(prefix: tuple[int, ...]) -> Iterable[tuple[int, ...]]:
        if len(prefix) == n:
            yield prefix
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix + (label,))

    yield from extend((0,))


def step(
    transitions: tuple[tuple[int, ...], ...], state: int, word: tuple[int, ...]
) -> int:
    for action in word:
        state = transitions[action][state]
    return state


def words(action_count: int, max_length: int) -> Iterable[tuple[int, ...]]:
    for length in range(max_length + 1):
        yield from product(range(action_count), repeat=length)


def shortest_witness(
    transitions: tuple[tuple[int, ...], ...],
    visible: tuple[object, ...],
    left: int,
    right: int,
) -> tuple[int, ...] | None:
    """Breadth-first shortest word whose terminal visible symbols differ."""

    queue: deque[tuple[int, int, tuple[int, ...]]] = deque([(left, right, ())])
    seen = {(left, right)}
    while queue:
        x, y, word = queue.popleft()
        if visible[x] != visible[y]:
            return word
        for action, transition in enumerate(transitions):
            pair = (transition[x], transition[y])
            if pair not in seen:
                seen.add(pair)
                queue.append((pair[0], pair[1], word + (action,)))
    return None


def behavioral_partition(
    transitions: tuple[tuple[int, ...], ...], visible: tuple[object, ...]
) -> tuple[int, ...]:
    """Greatest transition congruence contained in equality of visible output."""

    labels = canonical_partition(visible)
    while True:
        signatures = tuple(
            (visible[state],)
            + tuple(labels[transition[state]] for transition in transitions)
            for state in range(len(visible))
        )
        refined = canonical_partition(signatures)
        if refined == labels:
            return labels
        labels = refined


def is_refinement(fine: tuple[int, ...], coarse: tuple[int, ...]) -> bool:
    """Whether equality under ``fine`` implies equality under ``coarse``."""

    n = len(fine)
    return all(
        fine[x] != fine[y] or coarse[x] == coarse[y]
        for x in range(n)
        for y in range(n)
    )


def is_stable_visible_congruence(
    partition: tuple[int, ...],
    transitions: tuple[tuple[int, ...], ...],
    visible: tuple[object, ...],
) -> bool:
    n = len(partition)
    for x in range(n):
        for y in range(n):
            if partition[x] != partition[y]:
                continue
            if visible[x] != visible[y]:
                return False
            if any(
                partition[transition[x]] != partition[transition[y]]
                for transition in transitions
            ):
                return False
    return True


def quotient_is_markov_sufficient(
    record: tuple[int, ...],
    transitions: tuple[tuple[int, ...], ...],
    target: tuple[int, ...],
) -> bool:
    """Local target factorization plus transition congruence for record labels."""

    n = len(record)
    for x in range(n):
        for y in range(n):
            if record[x] != record[y]:
                continue
            if target[x] != target[y]:
                return False
            if any(
                record[transition[x]] != record[transition[y]]
                for transition in transitions
            ):
                return False
    return True


def enumerate_machine_family(
    n_values: Sequence[int], action_count: int
) -> tuple[int, int, int]:
    """Check pair witnesses and the tight ``n-2`` upper bound exhaustively."""

    machine_count = 0
    pair_count = 0
    violations = 0
    for n in n_values:
        transition_space = product(range(n), repeat=n * action_count)
        for flat in transition_space:
            transitions = tuple(
                tuple(flat[action * n : (action + 1) * n])
                for action in range(action_count)
            )
            for target in product(range(2), repeat=n):
                machine_count += 1
                visible = tuple(target)
                behavior = behavioral_partition(transitions, visible)
                for left, right in combinations(range(n), 2):
                    pair_count += 1
                    witness = shortest_witness(
                        transitions, visible, left, right
                    )
                    equivalent = behavior[left] == behavior[right]
                    if (witness is None) != equivalent:
                        violations += 1
                    if witness is not None and len(witness) > n - 2:
                        violations += 1
                    if witness is not None:
                        before = words(action_count, len(witness) - 1)
                        if any(
                            visible[step(transitions, left, word)]
                            != visible[step(transitions, right, word)]
                            for word in before
                        ):
                            violations += 1
    return machine_count, pair_count, violations


def check_minimal_refinement() -> tuple[int, int]:
    """Exhaustively verify the universal property through four states."""

    candidate_count = 0
    violations = 0
    for n in range(2, 5):
        partitions = tuple(set_partitions(n))
        for transition in product(range(n), repeat=n):
            transitions = (tuple(transition),)
            for target in product(range(2), repeat=n):
                visible = tuple(target)
                behavior = behavioral_partition(transitions, visible)
                if not is_stable_visible_congruence(
                    behavior, transitions, visible
                ):
                    violations += 1
                for candidate in partitions:
                    candidate_count += 1
                    if is_stable_visible_congruence(
                        candidate, transitions, visible
                    ) and not is_refinement(candidate, behavior):
                        violations += 1
    return candidate_count, violations


def check_record_markov_upgrade() -> tuple[int, int]:
    """Verify the local congruence iff global record-trace sufficiency test."""

    contract_count = 0
    violations = 0
    for n in range(2, 5):
        partitions = tuple(set_partitions(n))
        for transition in product(range(n), repeat=n):
            transitions = (tuple(transition),)
            for target in product(range(2), repeat=n):
                for record in partitions:
                    contract_count += 1
                    local = quotient_is_markov_sufficient(
                        record, transitions, tuple(target)
                    )
                    visible = tuple(
                        (record[state], target[state]) for state in range(n)
                    )
                    behavior = behavioral_partition(transitions, visible)
                    global_trace = all(
                        record[x] != record[y]
                        or behavior[x] == behavior[y]
                        for x in range(n)
                        for y in range(n)
                    )
                    if local != global_trace:
                        violations += 1
    return contract_count, violations


def tight_chain(n: int) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    transition = tuple(min(state + 1, n - 1) for state in range(n))
    target = tuple(1 if state == n - 1 else 0 for state in range(n))
    return (transition,), target


def main() -> None:
    single_machines, single_pairs, single_violations = enumerate_machine_family(
        range(2, 5), 1
    )
    binary_machines, binary_pairs, binary_violations = enumerate_machine_family(
        range(2, 4), 2
    )
    refinement_contracts, refinement_violations = check_minimal_refinement()
    markov_contracts, markov_violations = check_record_markov_upgrade()

    tight_lengths: dict[str, int] = {}
    tight_violations = 0
    for n in range(2, 10):
        transitions, target = tight_chain(n)
        witness = shortest_witness(transitions, target, 0, 1)
        length = -1 if witness is None else len(witness)
        tight_lengths[str(n)] = length
        if length != n - 2:
            tight_violations += 1

    no_horizon: dict[str, int] = {}
    horizon_violations = 0
    for horizon in range(0, 9):
        n = horizon + 3
        transitions, target = tight_chain(n)
        witness = shortest_witness(transitions, target, 0, 1)
        length = -1 if witness is None else len(witness)
        no_horizon[str(horizon)] = length
        if length != horizon + 1:
            horizon_violations += 1

    checks = [
        {
            "id": "single_action_exhaustive_pair_equivalence",
            "pass": single_violations == 0,
            "machines": single_machines,
            "state_pairs": single_pairs,
        },
        {
            "id": "two_action_exhaustive_pair_equivalence",
            "pass": binary_violations == 0,
            "machines": binary_machines,
            "state_pairs": binary_pairs,
        },
        {
            "id": "shortest_witness_bound_n_minus_2",
            "pass": single_violations == 0 and binary_violations == 0,
            "state_pairs": single_pairs + binary_pairs,
        },
        {
            "id": "behavioral_partition_is_greatest_stable_refinement",
            "pass": refinement_violations == 0,
            "candidate_congruences": refinement_contracts,
        },
        {
            "id": "record_markov_upgrade_iff_local_congruence",
            "pass": markov_violations == 0,
            "record_contracts": markov_contracts,
        },
        {
            "id": "tight_chain_attains_n_minus_2",
            "pass": tight_violations == 0,
            "shortest_lengths_by_state_count": tight_lengths,
        },
        {
            "id": "no_size_free_finite_horizon",
            "pass": horizon_violations == 0,
            "declared_horizon_to_first_difference": no_horizon,
        },
    ]

    result = {
        "schema": "dynamic-unity/council-orthodox-factorization-witness/v1",
        "candidate_id": "HC-DU-036A",
        "claim_grade": (
            "exact finite deterministic specialization / "
            "known automata mathematics / physical and stochastic lift open"
        ),
        "checks_passed": sum(check["pass"] for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "verdict": (
            "FINITE DETERMINISTIC TRACE FACTORIZATION OR TIGHT BOUNDED "
            "INTERVENTION WITNESS; NO SIZE-FREE CERTIFICATION HORIZON"
        ),
    }
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"{result['checks_passed']}/{result['checks_total']} checks pass\n"
        f"VERDICT: {result['verdict']}"
    )
    if result["checks_passed"] != result["checks_total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
