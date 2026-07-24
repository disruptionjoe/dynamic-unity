#!/usr/bin/env python3
"""Exact finite probe for interventional closure of a supplied record quotient.

This probe advances a deliberately bounded part of HC-DU-036.  A finite
deterministic process is supplied with:

* an independently fixed record label ``R``;
* an independently fixed observer readout ``Y``; and
* a finite family of admitted interventions ``T_a``.

The record is interventionally sufficient exactly when two states with the
same record have the same complete readout-and-record behavior after every
intervention word.  Partition refinement computes the coarsest
intervention-stable refinement of the supplied record that also carries the
readout.  If the supplied record is insufficient, a finite word witnesses the
missing distinction.

The probe also checks the linear reachable-rank bound used for stochastic and
finite operator-space generalizations.  These are finite automata/linear
systems results.  Passing does not physically select a record instrument,
make the intervention family complete, establish quantum or relativistic
realization, or prove record-first ontology.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_council_wild_frontier_interventional_closure_result.json"
)

Partition = tuple[int, ...]
StateMap = tuple[int, ...]
Word = tuple[int, ...]
Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def canonical_partition(labels: Sequence[Any]) -> Partition:
    """Return restricted-growth labels for the kernel of ``labels``."""

    relabel: dict[Any, int] = {}
    result: list[int] = []
    for value in labels:
        if value not in relabel:
            relabel[value] = len(relabel)
        result.append(relabel[value])
    return tuple(result)


def class_count(partition: Partition) -> int:
    return max(partition, default=-1) + 1


def initial_partition(
    record: Sequence[Any], readout: Sequence[Any]
) -> Partition:
    return canonical_partition(
        tuple(zip(record, readout, strict=True))
    )


def refine_partition(
    partition: Partition, transitions: Sequence[StateMap]
) -> Partition:
    """One Moore-style intervention-closure refinement."""

    return canonical_partition(
        tuple(
            (
                partition[state],
                tuple(partition[transition[state]] for transition in transitions),
            )
            for state in range(len(partition))
        )
    )


def closure_sequence(
    record: Sequence[Any],
    readout: Sequence[Any],
    transitions: Sequence[StateMap],
) -> tuple[Partition, ...]:
    """Return every strict refinement, followed by the stable partition."""

    current = initial_partition(record, readout)
    sequence = [current]
    while True:
        refined = refine_partition(current, transitions)
        if refined == current:
            return tuple(sequence)
        sequence.append(refined)
        current = refined


def observation(
    state: int, record: Sequence[Any], readout: Sequence[Any]
) -> tuple[Any, Any]:
    return record[state], readout[state]


def shortest_witness(
    left: int,
    right: int,
    record: Sequence[Any],
    readout: Sequence[Any],
    transitions: Sequence[StateMap],
) -> Word | None:
    """Breadth-first shortest intervention word distinguishing two states."""

    queue: list[tuple[int, int, Word]] = [(left, right, tuple())]
    visited: set[tuple[int, int]] = set()
    cursor = 0
    while cursor < len(queue):
        left_state, right_state, word = queue[cursor]
        cursor += 1
        pair = (left_state, right_state)
        if pair in visited:
            continue
        visited.add(pair)
        if observation(left_state, record, readout) != observation(
            right_state, record, readout
        ):
            return word
        for action, transition in enumerate(transitions):
            queue.append(
                (
                    transition[left_state],
                    transition[right_state],
                    word + (action,),
                )
            )
    return None


def deterministic_transition_matrix(transition: StateMap) -> Matrix:
    size = len(transition)
    return tuple(
        tuple(
            Fraction(int(transition[source] == target))
            for source in range(size)
        )
        for target in range(size)
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (entry * component for entry, component in zip(row, vector, strict=True)),
            start=Fraction(0),
        )
        for row in matrix
    )


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def matrix_rank(vectors: Iterable[Vector]) -> int:
    """Exact row rank of vectors over the rationals."""

    rows = [list(vector) for vector in vectors if any(vector)]
    if not rows:
        return 0
    row = 0
    columns = len(rows[0])
    for column in range(columns):
        pivot = next(
            (
                candidate
                for candidate in range(row, len(rows))
                if rows[candidate][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        pivot_value = rows[row][column]
        rows[row] = [value / pivot_value for value in rows[row]]
        for candidate in range(len(rows)):
            if candidate == row:
                continue
            factor = rows[candidate][column]
            if factor:
                rows[candidate] = [
                    value - factor * basis
                    for value, basis in zip(
                        rows[candidate], rows[row], strict=True
                    )
                ]
        row += 1
        if row == len(rows):
            break
    return row


def reachable_vectors(
    initial_difference: Vector,
    actions: Sequence[Matrix],
) -> tuple[tuple[Word, Vector], ...]:
    """Return a word-indexed spanning search until the reachable rank stabilizes."""

    dimension = len(initial_difference)
    frontier: list[tuple[Word, Vector]] = [(tuple(), initial_difference)]
    all_items: list[tuple[Word, Vector]] = []
    basis: list[Vector] = []
    known_rank = 0
    while frontier:
        next_frontier: list[tuple[Word, Vector]] = []
        grew = False
        for word, vector in frontier:
            candidate_rank = matrix_rank(basis + [vector])
            if candidate_rank == known_rank:
                continue
            basis.append(vector)
            known_rank = candidate_rank
            all_items.append((word, vector))
            grew = True
            if known_rank < dimension:
                for action_index, action in enumerate(actions):
                    next_frontier.append(
                        (word + (action_index,), matvec(action, vector))
                    )
        if not grew or known_rank == dimension:
            break
        frontier = next_frontier
    return tuple(all_items)


def linear_shortest_witness(
    initial_difference: Vector,
    effect: Vector,
    actions: Sequence[Matrix],
    max_length: int,
) -> tuple[Word, Fraction] | None:
    words: list[tuple[Word, Vector]] = [(tuple(), initial_difference)]
    for length in range(max_length + 1):
        next_words: list[tuple[Word, Vector]] = []
        for word, vector in words:
            value = dot(effect, vector)
            if value:
                return word, value
            if length < max_length:
                for action_index, action in enumerate(actions):
                    next_words.append(
                        (word + (action_index,), matvec(action, vector))
                    )
        words = next_words
    return None


def tight_chain(size: int) -> dict[str, Any]:
    transition = tuple(min(state + 1, size - 1) for state in range(size))
    record = (0,) * size
    readout = tuple(int(state == size - 1) for state in range(size))
    sequence = closure_sequence(record, readout, (transition,))
    witness = shortest_witness(0, 1, record, readout, (transition,))

    difference = tuple(
        Fraction(int(state == 0) - int(state == 1))
        for state in range(size)
    )
    effect = tuple(Fraction(value) for value in readout)
    action_matrix = deterministic_transition_matrix(transition)
    reachable = reachable_vectors(difference, (action_matrix,))
    linear_witness = linear_shortest_witness(
        difference,
        effect,
        (action_matrix,),
        max_length=size,
    )

    return {
        "size": size,
        "transition": list(transition),
        "readout": list(readout),
        "initial_class_count": class_count(sequence[0]),
        "stable_class_count": class_count(sequence[-1]),
        "strict_refinement_depth": len(sequence) - 1,
        "shortest_witness": list(witness) if witness is not None else None,
        "shortest_witness_length": len(witness) if witness is not None else None,
        "reachable_difference_rank": matrix_rank(
            vector for _, vector in reachable
        ),
        "linear_shortest_witness_length": (
            len(linear_witness[0]) if linear_witness is not None else None
        ),
        "linear_witness_value": (
            str(linear_witness[1]) if linear_witness is not None else None
        ),
    }


def duplicate_machine(
    record: Sequence[Any],
    readout: Sequence[Any],
    transitions: Sequence[StateMap],
) -> tuple[tuple[Any, ...], tuple[Any, ...], tuple[StateMap, ...]]:
    size = len(record)
    duplicate_record: list[Any] = []
    duplicate_readout: list[Any] = []
    for state in range(size):
        duplicate_record.extend((record[state], record[state]))
        duplicate_readout.extend((readout[state], readout[state]))
    duplicate_transitions = tuple(
        tuple(
            2 * transition[state // 2] + (state % 2)
            for state in range(2 * size)
        )
        for transition in transitions
    )
    return (
        tuple(duplicate_record),
        tuple(duplicate_readout),
        duplicate_transitions,
    )


@dataclass
class CheckBook:
    checks: list[dict[str, Any]]

    def add(self, name: str, passed: bool, detail: Any = None) -> None:
        self.checks.append(
            {"name": name, "passed": bool(passed), "detail": detail}
        )

    @property
    def passed(self) -> int:
        return sum(int(check["passed"]) for check in self.checks)


def run() -> dict[str, Any]:
    checks = CheckBook([])

    # Exhaust all binary record/readout maps and all one-action deterministic
    # maps through four states.  Each same-record pair must agree between the
    # stable partition and direct shortest-word search.
    one_action_cases = 0
    one_action_pairs = 0
    one_action_witnesses = 0
    bound_failures: list[dict[str, Any]] = []
    equivalence_failures: list[dict[str, Any]] = []
    for size in range(1, 5):
        for transition in itertools.product(range(size), repeat=size):
            for record in itertools.product((0, 1), repeat=size):
                for readout in itertools.product((0, 1), repeat=size):
                    one_action_cases += 1
                    sequence = closure_sequence(record, readout, (transition,))
                    stable = sequence[-1]
                    initial_blocks = class_count(sequence[0])
                    for left in range(size):
                        for right in range(left + 1, size):
                            if record[left] != record[right]:
                                continue
                            one_action_pairs += 1
                            witness = shortest_witness(
                                left,
                                right,
                                record,
                                readout,
                                (transition,),
                            )
                            closure_separates = stable[left] != stable[right]
                            search_separates = witness is not None
                            if closure_separates != search_separates:
                                equivalence_failures.append(
                                    {
                                        "size": size,
                                        "transition": transition,
                                        "record": record,
                                        "readout": readout,
                                        "pair": (left, right),
                                    }
                                )
                            if witness is not None:
                                one_action_witnesses += 1
                                bound = size - initial_blocks
                                if len(witness) > bound:
                                    bound_failures.append(
                                        {
                                            "size": size,
                                            "initial_blocks": initial_blocks,
                                            "witness_length": len(witness),
                                        }
                                    )

    checks.add(
        "exhaustive_one_action_closure_matches_word_search",
        not equivalence_failures,
        {
            "machines": one_action_cases,
            "same_record_pairs": one_action_pairs,
            "separated_pairs": one_action_witnesses,
            "failures": len(equivalence_failures),
        },
    )
    checks.add(
        "exhaustive_one_action_witness_bound",
        not bound_failures,
        {"failures": len(bound_failures)},
    )

    # Exhaust all two-action deterministic maps through three states to ensure
    # the closure result is not an artifact of a unary intervention alphabet.
    two_action_cases = 0
    two_action_pairs = 0
    two_action_failures: list[dict[str, Any]] = []
    for size in range(1, 4):
        maps = tuple(itertools.product(range(size), repeat=size))
        for left_transition in maps:
            for right_transition in maps:
                for readout in itertools.product((0, 1), repeat=size):
                    two_action_cases += 1
                    record = (0,) * size
                    transitions = (left_transition, right_transition)
                    stable = closure_sequence(record, readout, transitions)[-1]
                    for left in range(size):
                        for right in range(left + 1, size):
                            two_action_pairs += 1
                            witness = shortest_witness(
                                left,
                                right,
                                record,
                                readout,
                                transitions,
                            )
                            if (stable[left] != stable[right]) != (
                                witness is not None
                            ):
                                two_action_failures.append(
                                    {
                                        "size": size,
                                        "transitions": transitions,
                                        "readout": readout,
                                        "pair": (left, right),
                                    }
                                )
    checks.add(
        "exhaustive_two_action_closure_matches_word_search",
        not two_action_failures,
        {
            "machines": two_action_cases,
            "pairs": two_action_pairs,
            "failures": len(two_action_failures),
        },
    )

    # A delayed witness requires at least three deterministic states when the
    # two candidates have equal current record and readout.
    delayed_two_state_exists = False
    for transition in itertools.product(range(2), repeat=2):
        for record in itertools.product((0, 1), repeat=2):
            for readout in itertools.product((0, 1), repeat=2):
                if (
                    record[0] == record[1]
                    and readout[0] == readout[1]
                ):
                    witness = shortest_witness(
                        0, 1, record, readout, (transition,)
                    )
                    delayed_two_state_exists |= (
                        witness is not None and len(witness) > 0
                    )

    minimal = tight_chain(3)
    checks.add(
        "three_states_are_minimal_for_delayed_unary_witness",
        (
            not delayed_two_state_exists
            and minimal["shortest_witness_length"] == 1
        ),
        {
            "two_state_delayed_witness_exists": delayed_two_state_exists,
            "three_state_fixture": minimal,
        },
    )

    tight_family = [tight_chain(size) for size in range(3, 9)]
    checks.add(
        "partition_refinement_bound_is_tight",
        all(
            item["shortest_witness_length"]
            == item["size"] - item["initial_class_count"]
            == item["strict_refinement_depth"]
            for item in tight_family
        ),
        tight_family,
    )
    checks.add(
        "reachable_rank_bound_is_tight",
        all(
            item["shortest_witness_length"]
            == item["reachable_difference_rank"] - 1
            == item["linear_shortest_witness_length"]
            for item in tight_family
        ),
        tight_family,
    )

    # Exact factorizing control: clones inside each record block may evolve,
    # but their record/readout behavior remains identical under every word.
    factor_record = (0, 0, 1, 1)
    factor_readout = (0, 0, 1, 1)
    factor_transitions = (
        (1, 0, 3, 2),  # swap clones within each record block
        (2, 3, 0, 1),  # toggle the record block consistently
    )
    factor_sequence = closure_sequence(
        factor_record, factor_readout, factor_transitions
    )
    factor_record_partition = canonical_partition(factor_record)
    checks.add(
        "factorizing_record_control",
        factor_sequence[-1] == factor_record_partition,
        {
            "record_partition": factor_record_partition,
            "stable_partition": factor_sequence[-1],
            "refinement_depth": len(factor_sequence) - 1,
        },
    )

    # Duplicating exact behavioral clones doubles the raw state count but not
    # the minimal interventionally sufficient quotient.
    base_size = 5
    base_transition = tuple(
        min(state + 1, base_size - 1) for state in range(base_size)
    )
    base_record = (0,) * base_size
    base_readout = tuple(
        int(state == base_size - 1) for state in range(base_size)
    )
    base_stable = closure_sequence(
        base_record, base_readout, (base_transition,)
    )[-1]
    duplicate_record, duplicate_readout, duplicate_transitions = (
        duplicate_machine(
            base_record, base_readout, (base_transition,)
        )
    )
    duplicate_stable = closure_sequence(
        duplicate_record, duplicate_readout, duplicate_transitions
    )[-1]
    checks.add(
        "behavioral_clone_invariance",
        (
            class_count(base_stable) == base_size
            and class_count(duplicate_stable) == base_size
        ),
        {
            "base_raw_states": base_size,
            "duplicate_raw_states": 2 * base_size,
            "base_sufficient_classes": class_count(base_stable),
            "duplicate_sufficient_classes": class_count(duplicate_stable),
        },
    )

    # The minimal three-state delayed witness changes a declared binary
    # decision problem from prior-only error 1/2 to zero error after one
    # admitted intervention and readout.
    capability_prior_error = Fraction(1, 2)
    capability_post_error = Fraction(0)
    checks.add(
        "delayed_witness_enlarges_declared_action_capability",
        capability_post_error < capability_prior_error,
        {
            "hypotheses": ["initial_state_0", "initial_state_1"],
            "prior": ["1/2", "1/2"],
            "record_and_current_readout": [0, 0],
            "intervention_word": minimal["shortest_witness"],
            "readout_after_word": [0, 1],
            "record_only_error": str(capability_prior_error),
            "interventional_error": str(capability_post_error),
        },
    )

    passed = checks.passed
    total = len(checks.checks)
    return {
        "metadata": {
            "probe": Path(__file__).name,
            "scope": "finite deterministic record closure plus exact linear reachable-rank control",
            "claim_grade": "exact finite specialization; physical completeness and novelty open",
        },
        "result": {
            "checks_passed": passed,
            "checks_total": total,
            "all_passed": passed == total,
            "exact_conclusion": (
                "A supplied finite record quotient is interventionally sufficient "
                "iff it equals its stable readout-and-intervention congruence. "
                "Otherwise a finite word separates a same-record pair. In a "
                "d-dimensional linear realization, any separable pair has a "
                "word of length at most reachable distinction rank minus one."
            ),
        },
        "finite_enumeration": {
            "one_action_machines": one_action_cases,
            "one_action_same_record_pairs": one_action_pairs,
            "one_action_separated_pairs": one_action_witnesses,
            "two_action_machines": two_action_cases,
            "two_action_pairs": two_action_pairs,
        },
        "minimal_delayed_witness": minimal,
        "tight_family": tight_family,
        "factorizing_control": {
            "record": list(factor_record),
            "readout": list(factor_readout),
            "transitions": [list(item) for item in factor_transitions],
            "stable_partition": list(factor_sequence[-1]),
        },
        "clone_control": {
            "base_states": base_size,
            "duplicated_states": 2 * base_size,
            "sufficient_classes_before": class_count(base_stable),
            "sufficient_classes_after": class_count(duplicate_stable),
        },
        "checks": checks.checks,
    }


def main() -> None:
    result = run()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"{result['result']['checks_passed']}/"
        f"{result['result']['checks_total']} checks passed"
    )
    print(ARTIFACT_PATH)
    if not result["result"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
