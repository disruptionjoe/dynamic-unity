#!/usr/bin/env python3
"""Finite interventional-sufficiency and delayed-remainder probe.

This probe is the executable receipt for the heterodox Science Council's
repository-wide advancement wave.  It treats a certified record as the exact,
authenticated output symbol returned after each declared intervention.  The
systems are deterministic finite Mealy processes; no stochastic, quantum, or
adversarial generalization is claimed.

The central construction gives, for every finite horizon h, two processes that
agree on every intervention word of length at most h.  They first differ on
``advance**h ; read`` and both reset to the same endpoint after that read.
Thus complete certified records through a fixed horizon do not establish
unrestricted causal sufficiency.  A finite state bound restores decidability:
breadth-first search on the product machine either returns a shortest
separating intervention or exhausts the reachable product and certifies
input/output equivalence.  The delayed process also has h+1 pairwise distinct
residual behaviors, so its delay cannot be implemented by fewer than h+1
deterministic behavioral states.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from pathlib import Path
from typing import Any


ACTIONS = ("advance", "read")
ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_council_heterodox_delayed_remainder_result.json"
)


def delayed_machine(horizon: int, remainder: bool) -> dict[str, Any]:
    """Return the h-delay control or remainder process.

    States count how many consecutive ``advance`` interventions have occurred,
    capped at ``horizon``.  ``read`` always resets the state.  The remainder
    process returns one only when read after reaching the cap; the control
    always returns zero.
    """

    transitions: list[dict[str, tuple[int, int]]] = []
    for state in range(horizon + 1):
        transitions.append(
            {
                "advance": (min(state + 1, horizon), 0),
                "read": (
                    0,
                    int(remainder and state == horizon),
                ),
            }
        )
    return {
        "initial": 0,
        "transitions": transitions,
        "state_count": horizon + 1,
    }


def relabel_machine(machine: dict[str, Any]) -> dict[str, Any]:
    """Return an isomorphic machine under the reversal state permutation."""

    state_count = machine["state_count"]

    def permute(state: int) -> int:
        return state_count - 1 - state

    transitions: list[dict[str, tuple[int, int]]] = [
        {} for _ in range(state_count)
    ]
    for old_state, row in enumerate(machine["transitions"]):
        for action, (old_next, output) in row.items():
            transitions[permute(old_state)][action] = (
                permute(old_next),
                output,
            )
    return {
        "initial": permute(machine["initial"]),
        "transitions": transitions,
        "state_count": state_count,
    }


def run(
    machine: dict[str, Any],
    word: tuple[str, ...],
) -> tuple[tuple[int, ...], int]:
    return run_from(machine, machine["initial"], word)


def run_from(
    machine: dict[str, Any],
    initial_state: int,
    word: tuple[str, ...],
) -> tuple[tuple[int, ...], int]:
    state = initial_state
    outputs: list[int] = []
    for action in word:
        state, output = machine["transitions"][state][action]
        outputs.append(output)
    return tuple(outputs), state


def words_through(horizon: int) -> list[tuple[str, ...]]:
    return [
        word
        for length in range(horizon + 1)
        for word in itertools.product(ACTIONS, repeat=length)
    ]


def shortest_separator(
    left: dict[str, Any],
    right: dict[str, Any],
) -> tuple[str, ...] | None:
    """Return a shortest output-separating intervention word, if one exists."""

    initial_pair = (left["initial"], right["initial"])
    queue: deque[tuple[int, int, tuple[str, ...]]] = deque(
        [(initial_pair[0], initial_pair[1], ())]
    )
    visited = {initial_pair}

    while queue:
        left_state, right_state, prefix = queue.popleft()
        for action in ACTIONS:
            left_next, left_output = left["transitions"][left_state][action]
            right_next, right_output = right["transitions"][right_state][action]
            candidate = prefix + (action,)
            if left_output != right_output:
                return candidate
            pair = (left_next, right_next)
            if pair not in visited:
                visited.add(pair)
                queue.append((left_next, right_next, candidate))
    return None


def check(
    checks: list[dict[str, Any]],
    name: str,
    condition: bool,
    detail: Any,
) -> None:
    checks.append(
        {
            "name": name,
            "passed": bool(condition),
            "detail": detail,
        }
    )


def main() -> None:
    checks: list[dict[str, Any]] = []
    cases: list[dict[str, Any]] = []

    for horizon in range(1, 9):
        control = delayed_machine(horizon, remainder=False)
        rival = delayed_machine(horizon, remainder=True)
        short_words = words_through(horizon)
        short_agreement = all(
            run(control, word)[0] == run(rival, word)[0]
            for word in short_words
        )
        witness = ("advance",) * horizon + ("read",)
        control_witness = run(control, witness)
        rival_witness = run(rival, witness)
        found = shortest_separator(control, rival)
        product_bound = control["state_count"] * rival["state_count"]
        residual_pairs = list(itertools.combinations(range(horizon + 1), 2))
        pairwise_residual_distinction = all(
            run_from(
                rival,
                left_state,
                ("advance",) * (horizon - right_state) + ("read",),
            )[0]
            != run_from(
                rival,
                right_state,
                ("advance",) * (horizon - right_state) + ("read",),
            )[0]
            for left_state, right_state in residual_pairs
        )

        check(
            checks,
            f"h={horizon}: every certified intervention history through h agrees",
            short_agreement,
            {"word_count": len(short_words), "horizon": horizon},
        )
        check(
            checks,
            f"h={horizon}: delayed witness separates at h+1",
            control_witness[0] != rival_witness[0],
            {
                "witness": witness,
                "control_outputs": control_witness[0],
                "rival_outputs": rival_witness[0],
            },
        )
        check(
            checks,
            f"h={horizon}: separating histories return to one endpoint",
            control_witness[1] == rival_witness[1] == 0,
            {
                "control_endpoint": control_witness[1],
                "rival_endpoint": rival_witness[1],
            },
        )
        check(
            checks,
            f"h={horizon}: product search finds the minimal witness",
            found == witness,
            {"found": found, "expected": witness},
        )
        check(
            checks,
            f"h={horizon}: witness respects the finite product-state bound",
            found is not None and len(found) <= product_bound,
            {
                "witness_length": None if found is None else len(found),
                "product_bound": product_bound,
            },
        )
        check(
            checks,
            f"h={horizon}: all delay states have distinct future behavior",
            pairwise_residual_distinction,
            {
                "state_count": horizon + 1,
                "state_pairs_checked": len(residual_pairs),
                "minimal_behavioral_state_lower_bound": horizon + 1,
            },
        )

        cases.append(
            {
                "horizon": horizon,
                "state_count_each": horizon + 1,
                "certified_words_checked_through_h": len(short_words),
                "shortest_separator": found,
                "shortest_separator_length": None if found is None else len(found),
                "common_endpoint_after_separator": control_witness[1],
                "pairwise_distinct_residual_behaviors": pairwise_residual_distinction,
                "minimal_behavioral_state_lower_bound": horizon + 1,
            }
        )

    null = delayed_machine(6, remainder=False)
    relabelled_null = relabel_machine(null)
    null_separator = shortest_separator(null, relabelled_null)
    check(
        checks,
        "state relabeling null is interventionally equivalent",
        null_separator is None,
        {"shortest_separator": null_separator},
    )

    # Positive and negative congruence controls for a supplied record quotient.
    # The positive quotient q(s)=s mod 2 is stable under toggle/stay and its
    # outputs depend only on q.  The negative fixture merges states whose
    # ``reveal`` outputs differ.
    positive = {
        "initial": 0,
        "state_count": 4,
        "transitions": [
            {"advance": (1, 1), "read": (0, 0)},
            {"advance": (0, 0), "read": (1, 1)},
            {"advance": (3, 1), "read": (2, 0)},
            {"advance": (2, 0), "read": (3, 1)},
        ],
    }
    q = (0, 1, 0, 1)

    def quotient_is_congruence(machine: dict[str, Any]) -> bool:
        for left_state in range(machine["state_count"]):
            for right_state in range(machine["state_count"]):
                if q[left_state] != q[right_state]:
                    continue
                for action in ACTIONS:
                    left_next, left_output = machine["transitions"][left_state][
                        action
                    ]
                    right_next, right_output = machine["transitions"][right_state][
                        action
                    ]
                    if (
                        left_output != right_output
                        or q[left_next] != q[right_next]
                    ):
                        return False
        return True

    negative = json.loads(json.dumps(positive))
    negative["transitions"][2]["read"] = [2, 1]
    check(
        checks,
        "positive supplied record quotient is an intervention congruence",
        quotient_is_congruence(positive),
        {"quotient": q},
    )
    check(
        checks,
        "hostile output perturbation breaks the intervention congruence",
        not quotient_is_congruence(negative),
        {
            "merged_states": [0, 2],
            "action": "read",
            "outputs": [
                negative["transitions"][0]["read"][1],
                negative["transitions"][2]["read"][1],
            ],
        },
    )

    passed = sum(item["passed"] for item in checks)
    payload: dict[str, Any] = {
        "probe": "du_council_heterodox_delayed_remainder_probe",
        "warrant": "exact finite deterministic construction and specialization",
        "claim_scope": (
            "finite deterministic Mealy processes with exact authenticated "
            "outputs and a frozen intervention alphabet"
        ),
        "contract": {
            "process": "deterministic finite controlled transition system",
            "primitive_precedence": "word order of declared interventions",
            "interventions": ACTIONS,
            "record_instrument": "exact output symbol after each intervention",
            "provenance": "source machine and intervention word retained",
            "observer_access": "complete output transcript",
            "rival_class": "pairs of finite deterministic Mealy processes",
            "certificate": "exact transcript equality or a separating word",
            "finalizer": "append-only exact transcript; no adversary",
            "representation_group": "state relabelings preserving transitions and outputs",
            "resources": (
                "finite state count, intervention length, exact reset, "
                "unpriced physical implementation"
            ),
        },
        "theorems_tested": {
            "delayed_remainder": (
                "for every tested h, all words of length <=h agree but "
                "advance^h;read separates and resets both processes"
            ),
            "delay_memory_lower_bound": (
                "the h-delay remainder has h+1 pairwise distinct residual "
                "behaviors and therefore requires at least h+1 deterministic "
                "behavioral states"
            ),
            "finite_factorization_or_witness": (
                "product-state BFS either finds a shortest separating word "
                "of length at most |S0||S1| or exhausts the reachable product"
            ),
            "quotient_congruence": (
                "a supplied record quotient supports a deterministic quotient "
                "process exactly when outputs and successor classes are "
                "constant on each quotient fiber for every intervention"
            ),
        },
        "cases": cases,
        "null_control": {
            "fixture": "state-relabelled isomorphic process",
            "shortest_separator": null_separator,
        },
        "checks": checks,
        "summary": {
            "passed": passed,
            "total": len(checks),
            "all_passed": passed == len(checks),
        },
        "scientific_disposition": (
            "A fixed finite record horizon cannot establish unrestricted "
            "interventional sufficiency.  A declared finite state/resource "
            "bound makes the deterministic comparison decidable.  This is "
            "known automata territory and a CCR baseline, not a novel physical law."
        ),
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256_before_hash_field"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        f"{passed}/{len(checks)} checks passed; "
        f"artifact={ARTIFACT.relative_to(Path.cwd())}"
    )
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
