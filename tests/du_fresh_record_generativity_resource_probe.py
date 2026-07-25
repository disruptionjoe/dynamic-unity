#!/usr/bin/env python3
"""Finite resource hedge for fresh-record and generativity claims.

The probe asks two different questions that are often conflated:

1. What resources are required for exact, indefinitely nonaliasing records?
2. Does observing fresh record growth exclude a source fixed at stage zero?

The first question has a finite counting answer: exact distinct prefixes need
growing accessible support, export, weakened semantics, or modeled
coarse-graining/nonunitarity. The second answer is negative in this fixture.
A compact fixed-law transducer with an append-only output tape reproduces the
entire finite counterfactual response tree without preloading the realized
path. Thus an exponentially large extensional tree is not an appropriate
resource lower bound when compressed fixed laws are admitted.

Passing narrows H-CCR-10 and XH-01. It does not prove physical openness,
source issuance, computational irreducibility, or a universal lower bound.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_fresh_record_generativity_resource_result.json"
)


def words(alphabet: tuple[int, ...], maximum_depth: int) -> Iterable[tuple[int, ...]]:
    """Enumerate every nonempty word through ``maximum_depth``."""

    for depth in range(1, maximum_depth + 1):
        yield from itertools.product(alphabet, repeat=depth)


def parity_trace(interventions: tuple[int, ...]) -> tuple[int, ...]:
    """Online two-state transducer: emit running parity."""

    state = 0
    trace = []
    for intervention in interventions:
        state ^= intervention
        trace.append(state)
    return tuple(trace)


def append_only_record(interventions: tuple[int, ...]) -> tuple[int, ...]:
    """One fresh exact cell per admitted intervention."""

    return tuple(interventions)


def stage_zero_path_tape(
    realized_interventions: tuple[int, ...],
) -> dict[str, Any]:
    """A fixed tape carrying one realized path and its response transcript."""

    return {
        "interventions": realized_interventions,
        "responses": parity_trace(realized_interventions),
    }


def extensional_response_tree(
    alphabet: tuple[int, ...],
    depth: int,
) -> dict[str, tuple[int, ...]]:
    """Materialize every finite intervention history and response trace."""

    return {
        "".join(str(symbol) for symbol in intervention_word): parity_trace(
            intervention_word
        )
        for intervention_word in words(alphabet, depth)
    }


def fixed_law_replay(
    intervention_word: tuple[int, ...],
) -> dict[str, tuple[int, ...]]:
    """Run the compact fixed law while emitting the exact external record."""

    return {
        "response_trace": parity_trace(intervention_word),
        "record": append_only_record(intervention_word),
    }


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def build_result() -> dict[str, Any]:
    alphabet = (0, 1)
    horizon = 8
    finite_support_size = 8
    realized_path = (1, 0, 1, 1, 0, 1, 0, 0)

    # Fixed finite support: a modular recorder aliases at t=0 and t=M, and
    # pigeonhole guarantees some alias for every M-state recorder over M+1
    # exact time labels.
    modular_records = tuple(
        time_index % finite_support_size
        for time_index in range(finite_support_size + 1)
    )
    first_alias = next(
        (
            (left, right)
            for left in range(len(modular_records))
            for right in range(left + 1, len(modular_records))
            if modular_records[left] == modular_records[right]
        ),
        None,
    )

    # Fresh exact binary prefixes occupy 2^t distinct record values at depth t.
    prefix_counts = {
        depth: len(
            {
                append_only_record(intervention_word)
                for intervention_word in itertools.product(
                    alphabet, repeat=depth
                )
            }
        )
        for depth in range(horizon + 1)
    }
    minimum_record_bits = {
        depth: math.ceil(math.log2(count))
        for depth, count in prefix_counts.items()
    }

    # The original fixed-oracle control: one preloaded tape can replay one
    # realized path, but not arbitrary held-out interventions.
    preloaded_tape = stage_zero_path_tape(realized_path)
    tape_hash_before = hashlib.sha256(canonical_bytes(preloaded_tape)).hexdigest()
    tape_replay = preloaded_tape["responses"]
    tape_hash_after = hashlib.sha256(canonical_bytes(preloaded_tape)).hexdigest()
    held_out_path = (1, 1, 1, 0, 1, 0, 1, 1)
    tape_covers_held_out = held_out_path == preloaded_tape["interventions"]

    # Stronger rival: an extensional response tree contains every finite
    # counterfactual, yet the same mapping is generated by a two-state fixed
    # transition law. The law was frozen before the selected path.
    response_tree = extensional_response_tree(alphabet, horizon)
    all_counterfactual_words = tuple(words(alphabet, horizon))
    compressed_matches = all(
        response_tree[
            "".join(str(symbol) for symbol in intervention_word)
        ]
        == fixed_law_replay(intervention_word)["response_trace"]
        for intervention_word in all_counterfactual_words
    )
    extensional_node_count = len(response_tree)
    expected_node_count = sum(
        len(alphabet) ** depth for depth in range(1, horizon + 1)
    )
    fixed_law_table_entries = 2 * len(alphabet)

    # Exact prefix semantics force the record support to grow even though the
    # controller law remains fixed. The controller and the record substrate
    # are therefore distinct resource accounts.
    deepest_words = tuple(itertools.product(alphabet, repeat=horizon))
    distinct_emitted_records = {
        fixed_law_replay(intervention_word)["record"]
        for intervention_word in deepest_words
    }
    controller_state_count = 2
    required_record_state_count = len(distinct_emitted_records)

    checks = [
        {
            "id": "fixed_finite_recorder_aliases_within_support_plus_one_steps",
            "pass": (
                len(modular_records) == finite_support_size + 1
                and first_alias is not None
                and first_alias == (0, finite_support_size)
            ),
        },
        {
            "id": "fresh_binary_prefixes_require_exponential_record_support",
            "pass": all(
                prefix_counts[depth] == 2**depth
                for depth in range(horizon + 1)
            ),
        },
        {
            "id": "minimum_exact_record_bits_grow_one_per_binary_event",
            "pass": all(
                minimum_record_bits[depth] == depth
                for depth in range(horizon + 1)
            ),
        },
        {
            "id": "stage_zero_realized_path_tape_is_immutable_and_replays",
            "pass": (
                tape_hash_before == tape_hash_after
                and tape_replay == parity_trace(realized_path)
            ),
        },
        {
            "id": "one_path_tape_fails_a_distinct_held_out_intervention_path",
            "pass": not tape_covers_held_out,
        },
        {
            "id": "extensional_tree_contains_every_declared_counterfactual",
            "pass": (
                extensional_node_count == expected_node_count
                and set(response_tree)
                == {
                    "".join(str(symbol) for symbol in intervention_word)
                    for intervention_word in all_counterfactual_words
                }
            ),
        },
        {
            "id": "compact_fixed_law_matches_the_full_extensional_tree",
            "pass": compressed_matches,
        },
        {
            "id": "extensional_tree_size_is_not_a_compressed_law_lower_bound",
            "pass": extensional_node_count > 100 * fixed_law_table_entries,
        },
        {
            "id": "fixed_controller_and_growing_record_support_are_separable",
            "pass": (
                controller_state_count == 2
                and required_record_state_count == 2**horizon
                and required_record_state_count > controller_state_count
            ),
        },
        {
            "id": "fixed_law_handles_a_path_not_preloaded_on_the_realized_tape",
            "pass": (
                fixed_law_replay(held_out_path)["response_trace"]
                == parity_trace(held_out_path)
                and fixed_law_replay(held_out_path)["record"] == held_out_path
            ),
        },
    ]

    passed = sum(bool(check["pass"]) for check in checks)
    status = "PASS" if passed == len(checks) else "FAIL"
    return {
        "probe": "du_fresh_record_generativity_resource_probe",
        "date": "2026-07-24",
        "status": status,
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "parameters": {
            "alphabet": alphabet,
            "horizon": horizon,
            "finite_support_size": finite_support_size,
            "realized_path": realized_path,
            "held_out_path": held_out_path,
        },
        "finite_support_receipt": {
            "modular_records": modular_records,
            "first_alias": first_alias,
            "prefix_counts": prefix_counts,
            "minimum_record_bits": minimum_record_bits,
        },
        "fixed_completion_receipt": {
            "preloaded_tape": preloaded_tape,
            "preloaded_tape_sha256": tape_hash_before,
            "preloaded_tape_covers_held_out": tape_covers_held_out,
            "extensional_response_tree_nodes": extensional_node_count,
            "expected_tree_nodes": expected_node_count,
            "fixed_law_controller_states": controller_state_count,
            "fixed_law_transition_entries": fixed_law_table_entries,
            "compressed_law_matches_every_declared_counterfactual": (
                compressed_matches
            ),
            "depth_h_exact_record_states": required_record_state_count,
        },
        "result": {
            "resource_statement": (
                "Exact nonaliasing binary-prefix records through depth T "
                "require at least 2^T distinguishable global record states, "
                "equivalently T record bits, unless semantics are weakened or "
                "information is exported/coarse-grained."
            ),
            "disclosure_statement": (
                "Fresh exact record growth does not by itself exclude a "
                "stage-fixed compressed law: a two-state controller plus an "
                "append-only tape matches the full finite counterfactual "
                "response tree in this fixture."
            ),
            "separation": (
                "Record-support growth and source-law fixedness are orthogonal "
                "accounts. The former is witnessed here; the latter cannot be "
                "inferred from the same transcript."
            ),
            "verdict": (
                "FINITE SUPPORT-GROWTH REQUIREMENT RETAINED / PRELOADED-PATH "
                "RIVAL TOO WEAK / EXTENSIONAL RESPONSE-TREE COST ABSORBED BY "
                "COMPRESSED FIXED LAW / NO GENERATIVITY OR ISSUANCE WITNESS"
            ),
        },
        "program_effect": {
            "H-CCR-10": (
                "supported only at the exact finite counting/control grade"
            ),
            "XH-01": (
                "strengthened: compare against compressed fixed-law "
                "transducers, not only explicit future-correlated tables"
            ),
            "new_hypothesis": False,
            "next_decisive_question": (
                "Which independently justified causal-access or resource "
                "constraint excludes a compressed fixed-law completion without "
                "defining novelty as computational non-reducibility?"
            ),
        },
        "nonclaims": [
            "physical openness",
            "source issuance",
            "absolute computational irreducibility",
            "universal minimal-description lower bound",
            "fixed-law physical realizability for every candidate process",
            "record-first ontology",
            "new physical law",
        ],
    }


def main() -> None:
    result = build_result()
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "du_fresh_record_generativity_resource_probe: "
        f"{result['checks_passed']}/{result['checks_total']} checks passed\n"
        f"VERDICT: {result['result']['verdict']}\n"
        f"artifact: {ARTIFACT}"
    )
    if result["status"] != "PASS":
        failed = [
            check["id"] for check in result["checks"] if not check["pass"]
        ]
        raise SystemExit(f"failed checks: {failed}")


if __name__ == "__main__":
    main()
