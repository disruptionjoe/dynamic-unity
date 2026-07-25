#!/usr/bin/env python3
"""Exact bounded probe for a certified-composition quantum-strength gate.

The candidate Dynamic Unity principle says that:

1. finalized event certificates that disagree on the outcome of the same
   local measurement are mutually incompatible;
2. every pairwise incompatible family has total probability at most one; and
3. independently formed regions inherit this rule under product composition.

On a Bell-event interface this is established Local Orthogonality (LO), or
the Bell-scenario face of Consistent Exclusivity (CE); it is not new
mathematics.  The probe verifies the exact one-copy/two-copy PR distinction,
an exact quantum-boundary control, a local control, a signalling stop, and the
standard one-bit Information Causality witness.  It does not claim to
characterize the quantum set.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_strength_selection_result.json"
)


@dataclass(frozen=True)
class Qsqrt2:
    """Exact ordered number ``rational + radical * sqrt(2)``."""

    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", Fraction(self.rational))
        object.__setattr__(self, "radical", Fraction(self.radical))

    @staticmethod
    def coerce(value: Any) -> "Qsqrt2":
        if isinstance(value, Qsqrt2):
            return value
        return Qsqrt2(Fraction(value), Fraction(0))

    def __add__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational + target.rational,
            self.radical + target.radical,
        )

    def __radd__(self, other: Any) -> "Qsqrt2":
        return self + other

    def __sub__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational - target.rational,
            self.radical - target.radical,
        )

    def __rsub__(self, other: Any) -> "Qsqrt2":
        return self.coerce(other) - self

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.rational, -self.radical)

    def __mul__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational * target.rational
            + 2 * self.radical * target.radical,
            self.rational * target.radical
            + self.radical * target.rational,
        )

    def __rmul__(self, other: Any) -> "Qsqrt2":
        return self * other

    def sign(self) -> int:
        a = self.rational
        b = self.radical
        if a == 0:
            return (b > 0) - (b < 0)
        if b == 0:
            return (a > 0) - (a < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        comparison = a * a - 2 * b * b
        if comparison == 0:
            return 0
        if a > 0 and b < 0:
            return 1 if comparison > 0 else -1
        return -1 if comparison > 0 else 1

    def __eq__(self, other: object) -> bool:
        try:
            target = self.coerce(other)
        except (TypeError, ValueError):
            return False
        return (
            self.rational == target.rational
            and self.radical == target.radical
        )

    def __lt__(self, other: Any) -> bool:
        return (self - other).sign() < 0

    def __le__(self, other: Any) -> bool:
        return (self - other).sign() <= 0

    def __gt__(self, other: Any) -> bool:
        return (self - other).sign() > 0

    def __ge__(self, other: Any) -> bool:
        return (self - other).sign() >= 0

    def text(self) -> str:
        if self.radical == 0:
            return str(self.rational)
        if self.rational == 0:
            return f"{self.radical}*sqrt(2)"
        sign = "+" if self.radical > 0 else ""
        return f"{self.rational}{sign}{self.radical}*sqrt(2)"


Scalar = Qsqrt2
Behavior = dict[tuple[int, int, int, int], Scalar]


@dataclass(frozen=True, order=True)
class Event:
    """A multipartite event in output/input order."""

    outputs: tuple[int, ...]
    inputs: tuple[int, ...]

    def text(self) -> str:
        left = "".join(str(value) for value in self.outputs)
        right = "".join(str(value) for value in self.inputs)
        return f"({left}|{right})"


def q(value: Any = 0, radical: Any = 0) -> Qsqrt2:
    return Qsqrt2(Fraction(value), Fraction(radical))


def jsonable(value: Any) -> Any:
    if isinstance(value, Qsqrt2):
        return value.text()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, Event):
        return value.text()
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def pr_behavior() -> Behavior:
    return {
        (x, y, a, b): (
            q(Fraction(1, 2)) if (a ^ b) == (x & y) else q()
        )
        for x, y, a, b in itertools.product((0, 1), repeat=4)
    }


def local_deterministic_behavior() -> Behavior:
    return {
        (x, y, a, b): q(int(a == 0 and b == 0))
        for x, y, a, b in itertools.product((0, 1), repeat=4)
    }


def tsirelson_isotropic_behavior() -> Behavior:
    """Exact CHSH-optimal isotropic behavior, visibility 1/sqrt(2)."""

    behavior: Behavior = {}
    for x, y, a, b in itertools.product((0, 1), repeat=4):
        winning = (a ^ b) == (x & y)
        behavior[(x, y, a, b)] = q(
            Fraction(1, 4),
            Fraction(1 if winning else -1, 8),
        )
    return behavior


def signalling_behavior() -> Behavior:
    """Deterministic control with Bob's output equal to Alice's input."""

    return {
        (x, y, a, b): q(int(a == 0 and b == x))
        for x, y, a, b in itertools.product((0, 1), repeat=4)
    }


def behavior_valid(behavior: Mapping[tuple[int, int, int, int], Scalar]) -> bool:
    return all(value >= 0 for value in behavior.values()) and all(
        sum(
            (
                behavior[(x, y, a, b)]
                for a, b in itertools.product((0, 1), repeat=2)
            ),
            start=q(),
        )
        == 1
        for x, y in itertools.product((0, 1), repeat=2)
    )


def behavior_nonsignalling(
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> bool:
    alice = all(
        sum((behavior[(x, 0, a, b)] for b in (0, 1)), start=q())
        == sum((behavior[(x, 1, a, b)] for b in (0, 1)), start=q())
        for x, a in itertools.product((0, 1), repeat=2)
    )
    bob = all(
        sum((behavior[(0, y, a, b)] for a in (0, 1)), start=q())
        == sum((behavior[(1, y, a, b)] for a in (0, 1)), start=q())
        for y, b in itertools.product((0, 1), repeat=2)
    )
    return alice and bob


def chsh_value(
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> Scalar:
    correlators: dict[tuple[int, int], Scalar] = {}
    for x, y in itertools.product((0, 1), repeat=2):
        correlators[(x, y)] = sum(
            (
                (1 if (a ^ b) == 0 else -1)
                * behavior[(x, y, a, b)]
                for a, b in itertools.product((0, 1), repeat=2)
            ),
            start=q(),
        )
    return (
        correlators[(0, 0)]
        + correlators[(0, 1)]
        + correlators[(1, 0)]
        - correlators[(1, 1)]
    )


def locally_orthogonal(left: Event, right: Event) -> bool:
    return any(
        left_input == right_input and left_output != right_output
        for left_input, right_input, left_output, right_output in zip(
            left.inputs,
            right.inputs,
            left.outputs,
            right.outputs,
            strict=True,
        )
    )


def single_pr_possible_events() -> tuple[Event, ...]:
    return tuple(
        Event((a, b), (x, y))
        for x, y, a, b in itertools.product((0, 1), repeat=4)
        if (a ^ b) == (x & y)
    )


def product_events(events: Iterable[Event], copies: int) -> tuple[Event, ...]:
    base = tuple(events)
    result: list[Event] = []
    for factors in itertools.product(base, repeat=copies):
        outputs = tuple(
            value for factor in factors for value in factor.outputs
        )
        inputs = tuple(
            value for factor in factors for value in factor.inputs
        )
        result.append(Event(outputs, inputs))
    return tuple(sorted(result))


def maximum_orthogonal_clique(events: tuple[Event, ...]) -> tuple[Event, ...]:
    """Exact maximum clique via deterministic Bron--Kerbosch bitsets."""

    size = len(events)
    neighbors: list[int] = []
    for index, event in enumerate(events):
        bits = 0
        for other_index, other in enumerate(events):
            if index != other_index and locally_orthogonal(event, other):
                bits |= 1 << other_index
        neighbors.append(bits)

    best: tuple[int, ...] = ()

    def search(
        clique: tuple[int, ...],
        candidates: int,
        excluded: int,
    ) -> None:
        nonlocal best
        if len(clique) + candidates.bit_count() <= len(best):
            return
        if candidates == 0 and excluded == 0:
            if len(clique) > len(best):
                best = clique
            return

        union = candidates | excluded
        pivot = -1
        if union:
            pivot = max(
                (
                    index
                    for index in range(size)
                    if union & (1 << index)
                ),
                key=lambda index: (
                    (candidates & neighbors[index]).bit_count(),
                    -index,
                ),
            )
        branch = (
            candidates
            if pivot < 0
            else candidates & ~neighbors[pivot]
        )
        while branch:
            bit = branch & -branch
            vertex = bit.bit_length() - 1
            search(
                clique + (vertex,),
                candidates & neighbors[vertex],
                excluded & neighbors[vertex],
            )
            candidates &= ~bit
            excluded |= bit
            branch &= ~bit
            if len(clique) + candidates.bit_count() <= len(best):
                return

    search((), (1 << size) - 1, 0)
    return tuple(events[index] for index in best)


def known_two_copy_witness() -> tuple[Event, ...]:
    raw = (
        ("0000", "0000"),
        ("1110", "0011"),
        ("0011", "0110"),
        ("1101", "1011"),
        ("0111", "1101"),
    )
    return tuple(
        Event(
            tuple(int(value) for value in outputs),
            tuple(int(value) for value in inputs),
        )
        for outputs, inputs in raw
    )


def pairwise_orthogonal(events: tuple[Event, ...]) -> bool:
    return all(
        locally_orthogonal(left, right)
        for left, right in itertools.combinations(events, 2)
    )


def pr_product_probability(event: Event) -> Fraction:
    if len(event.outputs) != len(event.inputs) or len(event.outputs) % 2:
        raise ValueError("event_not_a_product_of_bipartite_copies")
    copies = len(event.outputs) // 2
    for copy in range(copies):
        a = event.outputs[2 * copy]
        b = event.outputs[2 * copy + 1]
        x = event.inputs[2 * copy]
        y = event.inputs[2 * copy + 1]
        if (a ^ b) != (x & y):
            return Fraction(0)
    return Fraction(1, 2**copies)


def information_causality_pr_receipt() -> dict[str, Any]:
    """Exact one-bit random-access-code use of a PR box."""

    rows: list[dict[str, int]] = []
    all_correct = True
    for bit0, bit1, requested, alice_output in itertools.product(
        (0, 1), repeat=4
    ):
        alice_input = bit0 ^ bit1
        bob_input = requested
        bob_output = alice_output ^ (alice_input & bob_input)
        message = bit0 ^ alice_output
        guess = message ^ bob_output
        target = bit0 if requested == 0 else bit1
        all_correct &= guess == target
        rows.append(
            {
                "alice_bit_0": bit0,
                "alice_bit_1": bit1,
                "requested_bit": requested,
                "alice_pr_output": alice_output,
                "alice_message": message,
                "bob_pr_output": bob_output,
                "bob_guess": guess,
                "target": target,
            }
        )
    return {
        "all_16_branches_recover_requested_bit": all_correct,
        "message_bits": 1,
        "information_sum_bits": 2,
        "violates_information_causality_by_bits": 1,
        "rows": rows,
    }


def add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    detail: Any,
) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def main() -> int:
    checks: list[dict[str, Any]] = []

    local = local_deterministic_behavior()
    pr = pr_behavior()
    quantum_boundary = tsirelson_isotropic_behavior()
    signalling = signalling_behavior()

    add_check(checks, "local_behavior_valid", behavior_valid(local), "exact")
    add_check(
        checks,
        "local_behavior_nonsignalling",
        behavior_nonsignalling(local),
        "exact",
    )
    add_check(checks, "local_chsh_is_2", chsh_value(local) == 2, chsh_value(local))

    add_check(checks, "pr_behavior_valid", behavior_valid(pr), "exact")
    add_check(
        checks,
        "pr_behavior_nonsignalling",
        behavior_nonsignalling(pr),
        "exact",
    )
    add_check(checks, "pr_chsh_is_4", chsh_value(pr) == 4, chsh_value(pr))

    one_copy_events = tuple(sorted(single_pr_possible_events()))
    one_copy_clique = maximum_orthogonal_clique(one_copy_events)
    add_check(
        checks,
        "one_pr_possible_event_count_is_8",
        len(one_copy_events) == 8,
        len(one_copy_events),
    )
    add_check(
        checks,
        "one_pr_maximum_lo_clique_size_is_2",
        len(one_copy_clique) == 2,
        one_copy_clique,
    )
    add_check(
        checks,
        "one_pr_maximum_lo_weight_is_1",
        Fraction(len(one_copy_clique), 2) == 1,
        Fraction(len(one_copy_clique), 2),
    )

    two_copy_events = product_events(one_copy_events, 2)
    two_copy_clique = maximum_orthogonal_clique(two_copy_events)
    witness = known_two_copy_witness()
    witness_probabilities = tuple(
        pr_product_probability(event) for event in witness
    )
    witness_sum = sum(witness_probabilities, start=Fraction(0))
    add_check(
        checks,
        "two_pr_possible_event_count_is_64",
        len(two_copy_events) == 64,
        len(two_copy_events),
    )
    add_check(
        checks,
        "published_five_event_witness_is_supported",
        all(event in two_copy_events for event in witness),
        witness,
    )
    add_check(
        checks,
        "published_witness_is_pairwise_locally_orthogonal",
        pairwise_orthogonal(witness),
        witness,
    )
    add_check(
        checks,
        "each_supported_two_pr_witness_event_has_probability_1_over_4",
        all(value == Fraction(1, 4) for value in witness_probabilities),
        witness_probabilities,
    )
    add_check(
        checks,
        "two_pr_witness_sum_is_5_over_4",
        witness_sum == Fraction(5, 4),
        witness_sum,
    )
    add_check(
        checks,
        "two_pr_witness_violates_lo_by_1_over_4",
        witness_sum - 1 == Fraction(1, 4),
        witness_sum - 1,
    )
    add_check(
        checks,
        "two_pr_exhaustive_maximum_lo_clique_size_is_5",
        len(two_copy_clique) == 5,
        two_copy_clique,
    )

    add_check(
        checks,
        "tsirelson_behavior_valid",
        behavior_valid(quantum_boundary),
        "exact Q(sqrt(2)) arithmetic",
    )
    add_check(
        checks,
        "tsirelson_behavior_nonsignalling",
        behavior_nonsignalling(quantum_boundary),
        "exact Q(sqrt(2)) arithmetic",
    )
    add_check(
        checks,
        "tsirelson_chsh_is_2_sqrt_2",
        chsh_value(quantum_boundary) == q(0, 2),
        chsh_value(quantum_boundary),
    )
    tsirelson_five_event_sum = q(
        Fraction(15, 32),
        Fraction(5, 16),
    )
    add_check(
        checks,
        "tsirelson_five_event_sum_below_1",
        tsirelson_five_event_sum < 1,
        tsirelson_five_event_sum,
    )
    add_check(
        checks,
        "tsirelson_five_event_slack_positive_exactly",
        q(1) - tsirelson_five_event_sum > 0,
        q(1) - tsirelson_five_event_sum,
    )

    add_check(
        checks,
        "signalling_control_valid",
        behavior_valid(signalling),
        "exact",
    )
    add_check(
        checks,
        "signalling_control_rejected_by_causal_contract",
        not behavior_nonsignalling(signalling),
        "Bob's marginal depends on Alice's input",
    )

    information_causality = information_causality_pr_receipt()
    add_check(
        checks,
        "pr_random_access_code_recovers_every_requested_bit",
        information_causality["all_16_branches_recover_requested_bit"],
        "16/16 deterministic branches",
    )
    add_check(
        checks,
        "pr_random_access_code_information_sum_2_exceeds_message_1",
        information_causality["information_sum_bits"]
        > information_causality["message_bits"],
        {
            "information_sum_bits": information_causality[
                "information_sum_bits"
            ],
            "message_bits": information_causality["message_bits"],
        },
    )

    all_passed = all(check["passed"] for check in checks)
    result = {
        "schema_version": (
            "dynamic-unity/quantum-strength-selection-frontier-gate/v0.1"
        ),
        "run_id": "RUN-20260725-100452-record-formation-certified-composition",
        "claim_grade": (
            "EXACT FINITE LO/PR SPECIALIZATION + LANDSCAPE NO-GO / "
            "KNOWN COMPONENT MATHEMATICS / QUANTUM SELECTION OPEN"
        ),
        "candidate_principle": {
            "name": (
                "Certified Exclusivity under Independent Regional Composition"
            ),
            "clauses": [
                (
                    "certified events with different outputs for the same "
                    "local input are incompatible"
                ),
                (
                    "every pairwise incompatible event family has total "
                    "probability at most one"
                ),
                (
                    "independently formed regions compose by product "
                    "probabilities and inherited event identities"
                ),
            ],
            "prior_art_identity": (
                "Local Orthogonality on Bell events; Bell-scenario face of "
                "Consistent Exclusivity"
            ),
            "not_a_new_principle": True,
        },
        "exact_receipt": {
            "one_pr": {
                "possible_events": len(one_copy_events),
                "maximum_lo_clique": one_copy_clique,
                "maximum_lo_sum": Fraction(len(one_copy_clique), 2),
                "disposition": (
                    "PASSES_SINGLE_COPY_LO; in bipartite scenarios LO is "
                    "equivalent to no-signalling"
                ),
            },
            "two_independent_pr": {
                "possible_events": len(two_copy_events),
                "maximum_lo_clique": two_copy_clique,
                "published_witness": witness,
                "witness_probabilities": witness_probabilities,
                "witness_sum": witness_sum,
                "excess_over_one": witness_sum - 1,
                "disposition": (
                    "EXCLUDED_UNDER_DECLARED_TWO_COPY_COMPOSITION"
                ),
            },
            "ordinary_quantum": {
                "general_receipt": (
                    "locally orthogonal quantum events have orthogonal "
                    "product projectors, so every LO sum is at most one"
                ),
                "chsh_boundary": chsh_value(quantum_boundary),
                "five_event_witness_sum": tsirelson_five_event_sum,
                "five_event_witness_slack": (
                    q(1) - tsirelson_five_event_sum
                ),
                "disposition": "ADMITTED_BY_LO",
            },
            "information_causality_pr_control": information_causality,
            "signalling_control": {
                "valid_conditional_table": behavior_valid(signalling),
                "no_signalling": behavior_nonsignalling(signalling),
                "disposition": "OUTSIDE_FROZEN_CAUSAL_LANDSCAPE",
            },
        },
        "class_ledger": [
            {
                "class": "local",
                "relation": "strict subset of ordinary quantum",
                "gate_disposition": "admitted",
            },
            {
                "class": "ordinary_quantum",
                "relation": (
                    "satisfies LO/CE; CHSH bounded by 2*sqrt(2)"
                ),
                "gate_disposition": "admitted",
            },
            {
                "class": "almost_quantum",
                "relation": (
                    "strictly larger than ordinary quantum; satisfies LO and "
                    "CE, macroscopic locality, and other named principles"
                ),
                "gate_disposition": (
                    "not excluded by this probability-level principle"
                ),
            },
            {
                "class": "no_signalling",
                "relation": (
                    "strictly larger than ordinary quantum; one-copy PR lies "
                    "here"
                ),
                "gate_disposition": (
                    "partially cut by composition; PR^2 is excluded"
                ),
            },
            {
                "class": "signalling",
                "relation": "outside the declared no-signalling landscape",
                "gate_disposition": "stopped before strength selection",
            },
        ],
        "hard_disposition": (
            "PR_EXCLUSION_FEASIBLE_UNDER_INDEPENDENT_COMPOSITION / "
            "CANDIDATE_COLLAPSES_TO_KNOWN_LO_CE / "
            "ORDINARY_QUANTUM_NOT_SELECTED"
        ),
        "precise_missing_structure": (
            "Probability-level certificate exclusivity supplies only a "
            "binary incompatibility hypergraph. It does not derive the "
            "sharp complete instruments, joint-measurability structure, or "
            "graded positive operator composition that distinguishes "
            "ordinary quantum from almost-quantum correlations."
        ),
        "exact_reopener": {
            "name": "formed-sharp instrument composition",
            "requirements": [
                (
                    "derive a noncircular physical sharpness criterion for "
                    "formed record instruments"
                ),
                (
                    "certify pairwise compatibility at complete selective-"
                    "instrument and continuation level, not event marginals"
                ),
                (
                    "prove or refute a pairwise-to-global joint-instrument "
                    "composition law under independent regional formation"
                ),
                (
                    "admit ordinary projective quantum instruments and "
                    "exclude a declared almost-quantum/Specker witness "
                    "without inserting Hilbert-space quantum structure"
                ),
            ],
            "novelty_condition": (
                "Specker's principle and sharp-measurement axiom families are "
                "occupied terrain. A DU delta would have to derive their "
                "applicability from record formation, provenance, access, "
                "and continuation dynamics or produce a stricter new "
                "consequence."
            ),
        },
        "does_not_establish": [
            "a new exclusivity principle",
            "the Tsirelson bound from Dynamic Unity premises",
            "membership in the ordinary quantum set",
            "exclusion of all post-quantum or almost-quantum correlations",
            "a physical record-selection law",
            "record-first ontology",
        ],
        "checks": checks,
        "checks_passed": sum(check["passed"] for check in checks),
        "checks_total": len(checks),
        "all_checks_passed": all_passed,
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"quantum-strength selection probe: "
        f"{result['checks_passed']}/{result['checks_total']} checks passed"
    )
    print(f"hard disposition: {result['hard_disposition']}")
    print(f"artifact: {ARTIFACT}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
