#!/usr/bin/env python3
"""Exact finite certificate for the ECR-N5-S3 epoch-archive boundary.

This probe does not simulate a microscopic environment.  It exhausts the
smallest deterministic transducer class and checks four exact boundaries:

1. the binary "a write occurred since the certified epoch reset" transducer
   is unique once write, idle/turnover, and epoch-reset semantics are frozen;
2. no closed reversible two-state carrier implements its idempotent write
   and reset maps;
3. resetting on the matter host's own turnover edge yields only the already
   selected ready/retained value, not an independent epoch witness; and
4. a fresh append-only output tape retains the history, while its binary
   occurrence quotient is strict only for a bounded declared capability.

The generated artifact is a regression receipt for an analytic result.  A
passing probe does not establish that the metastable host selects a physical
environment factorization, fresh support, an epoch boundary, an archive
access route, or a universal record law.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any, Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_epoch_archive_boundary_result.json"
)

BitMap = tuple[int, int]
Transducer = dict[str, BitMap]

SYMBOLS = ("I", "C", "W", "E")
ALL_BIT_MAPS: tuple[BitMap, ...] = tuple(
    itertools.product((0, 1), repeat=2)
)
BIJECTIONS: tuple[BitMap, ...] = ((0, 1), (1, 0))

DESIRED: Transducer = {
    "I": (0, 1),  # idle retains the epoch bit
    "C": (0, 1),  # internal matter turnover does not start a new epoch
    "W": (1, 1),  # any write makes the bounded occurrence claim true
    "E": (0, 0),  # a certified external epoch reset clears the claim
}

NEXT_STATE = {
    "x0": "x1",
    "x1": "x2",
    "x2": "x3",
    "x3": "x0",
}
EDGE_KIND = {
    "x0": "W",
    "x1": "C",
    "x2": "W",
    "x3": "C",
}
RETAINED_STATES = {"x1", "x3"}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def apply_map(bit_map: BitMap, bit: int) -> int:
    return bit_map[bit]


def apply_word(
    transducer: Transducer,
    word: Iterable[str],
    initial: int = 0,
) -> int:
    bit = initial
    for symbol in word:
        bit = apply_map(transducer[symbol], bit)
    return bit


def all_transducers(
    maps: tuple[BitMap, ...],
) -> Iterable[Transducer]:
    for choices in itertools.product(maps, repeat=len(SYMBOLS)):
        yield dict(zip(SYMBOLS, choices, strict=True))


def satisfies_frozen_semantics(transducer: Transducer) -> bool:
    return transducer == DESIRED


def cycle_prefix(
    length: int,
    initial_state: str = "x1",
) -> tuple[str, str]:
    state = initial_state
    word: list[str] = []
    for _ in range(length):
        word.append(EDGE_KIND[state])
        state = NEXT_STATE[state]
    return "".join(word), state


def evolve_internal_turnover_flag(
    word: str,
    initial: int,
) -> int:
    bit = initial
    for symbol in word:
        if symbol == "C":
            bit = 0
        elif symbol == "W":
            bit = 1
    return bit


def external_epoch_flag(word: str) -> int:
    return int("W" in word)


def count_writes(word: str) -> int:
    return word.count("W")


def fresh_cell_branch_map() -> dict[tuple[str, str], tuple[str, str]]:
    """One exact collision-step branch map with source-labelled output.

    For each matter state, the two classical channel branches are no jump
    and the selected next jump.  The fresh output token retains the source
    and branch, so the map is injective and can be extended to a reversible
    permutation/unitary on a larger state space.
    """

    result: dict[tuple[str, str], tuple[str, str]] = {}
    for state in NEXT_STATE:
        result[(state, "no_jump")] = (state, f"N:{state}")
        result[(state, "jump")] = (
            NEXT_STATE[state],
            f"J:{state}>{NEXT_STATE[state]}",
        )
    return result


def archive_access_completion_twins() -> dict[str, Any]:
    """Two injective completions with one reduced matter branch map.

    In the visible arm the branch token enters the admitted archive fragment.
    In the hidden arm the same token enters a reservoir outside that access
    boundary while the admitted fragment stays blank.  The distinction is
    physical once the access wiring is frozen; it is not selected by the
    reduced matter branch relation.
    """

    branch_map = fresh_cell_branch_map()
    visible: dict[tuple[str, str], tuple[str, str, str]] = {}
    hidden: dict[tuple[str, str], tuple[str, str, str]] = {}
    for source, (destination, token) in branch_map.items():
        visible[source] = (destination, token, "H:blank")
        hidden[source] = (destination, "A:blank", token)

    reduced_visible = {
        source: target[0]
        for source, target in visible.items()
    }
    reduced_hidden = {
        source: target[0]
        for source, target in hidden.items()
    }
    admitted_visible = {
        target[1]
        for target in visible.values()
    }
    admitted_hidden = {
        target[1]
        for target in hidden.values()
    }

    return {
        "visible_completion_injective": is_injective(visible),
        "hidden_completion_injective": is_injective(hidden),
        "same_reduced_matter_branch_map": (
            reduced_visible == reduced_hidden
        ),
        "visible_arm_admitted_archive_cardinality": len(
            admitted_visible
        ),
        "hidden_arm_admitted_archive_cardinality": len(
            admitted_hidden
        ),
        "admitted_archive_differs": admitted_visible != admitted_hidden,
        "interpretation": (
            "fixed reduced matter dynamics does not select whether the "
            "branch token enters the admitted archive or a hidden reservoir"
        ),
    }


def is_injective(mapping: dict[Any, Any]) -> bool:
    return len(set(mapping.values())) == len(mapping)


def find_pair(
    words: Iterable[str],
    same_key: Callable[[str], Any],
    different_key: Callable[[str], Any],
) -> tuple[str, str] | None:
    candidates = list(words)
    for left_index, left in enumerate(candidates):
        for right in candidates[left_index + 1 :]:
            if (
                same_key(left) == same_key(right)
                and different_key(left) != different_key(right)
            ):
                return left, right
    return None


def build_result() -> dict[str, Any]:
    deterministic_candidates = list(all_transducers(ALL_BIT_MAPS))
    semantic_matches = [
        candidate
        for candidate in deterministic_candidates
        if satisfies_frozen_semantics(candidate)
    ]

    reversible_candidates = list(all_transducers(BIJECTIONS))
    reversible_matches = [
        candidate
        for candidate in reversible_candidates
        if satisfies_frozen_semantics(candidate)
    ]

    allowed_prefixes = [
        cycle_prefix(length)
        for length in range(13)
    ]
    internal_turnover_checks = []
    for word, endpoint in allowed_prefixes:
        internal_flag = evolve_internal_turnover_flag(
            word,
            initial=1,
        )
        endpoint_flag = int(endpoint in RETAINED_STATES)
        internal_turnover_checks.append(
            {
                "word": word,
                "endpoint": endpoint,
                "internal_turnover_flag": internal_flag,
                "endpoint_retained_flag": endpoint_flag,
                "equal": internal_flag == endpoint_flag,
            }
        )

    same_endpoint_pair = ("", "CWCW")
    same_endpoint_evidence = {
        "left_word": same_endpoint_pair[0],
        "right_word": same_endpoint_pair[1],
        "initial_state": "x1",
        "terminal_state": "x1",
        "left_epoch_flag": external_epoch_flag(same_endpoint_pair[0]),
        "right_epoch_flag": external_epoch_flag(same_endpoint_pair[1]),
        "separated": (
            external_epoch_flag(same_endpoint_pair[0])
            != external_epoch_flag(same_endpoint_pair[1])
        ),
    }

    parity_transducer = {
        "I": (0, 1),
        "C": (0, 1),
        "W": (1, 0),
        "E": (0, 1),
    }
    parity_counterexample = {
        "word": "CWCW",
        "parity_output": apply_word(parity_transducer, "CWCW"),
        "required_epoch_output": external_epoch_flag("CWCW"),
    }

    longer_allowed_words = [
        cycle_prefix(length)[0]
        for length in range(17)
    ]
    strict_compression_pair = find_pair(
        longer_allowed_words,
        same_key=lambda word: (
            cycle_prefix(len(word))[1],
            external_epoch_flag(word),
        ),
        different_key=count_writes,
    )
    assert strict_compression_pair is not None

    branch_map = fresh_cell_branch_map()
    completion_twins = archive_access_completion_twins()
    history_tapes = {
        word: list(word)
        for word in longer_allowed_words
    }

    result = {
        "schema_version": "1.0",
        "claim": "HC-DU-044",
        "swing": "ECR-N5-S3",
        "method": "exact_finite_exhaustion_and_injectivity_checks",
        "binary_transducer": {
            "symbols": list(SYMBOLS),
            "semantics": {
                "I": "retain",
                "C": "retain_for_external_epoch_question",
                "W": "set_true",
                "E": "clear_at_certified_epoch_reset",
            },
            "deterministic_candidates": len(deterministic_candidates),
            "semantic_matches": len(semantic_matches),
            "unique_match": semantic_matches[0],
            "unique": len(semantic_matches) == 1,
        },
        "closed_reversible_carrier": {
            "two_state_candidates": len(reversible_candidates),
            "semantic_matches": len(reversible_matches),
            "exact_implementation_exists": bool(reversible_matches),
            "write_map_is_bijective": DESIRED["W"] in BIJECTIONS,
            "epoch_reset_map_is_bijective": DESIRED["E"] in BIJECTIONS,
            "parity_counterexample": parity_counterexample,
        },
        "internal_turnover_reset": {
            "checks": internal_turnover_checks,
            "always_equals_endpoint_ready_retained_class": all(
                check["equal"]
                for check in internal_turnover_checks
            ),
            "interpretation": (
                "resetting on the host turnover edge reproduces the "
                "already-selected ready/retained value"
            ),
        },
        "external_epoch": {
            "same_endpoint_occurrence_pair": same_endpoint_evidence,
            "requires_certified_initialization": True,
        },
        "fresh_output_completion": {
            "single_step_branch_map": [
                {
                    "input": list(source),
                    "output": list(target),
                }
                for source, target in branch_map.items()
            ],
            "branch_map_injective": is_injective(branch_map),
            "therefore_extensible_to_reversible_completion": is_injective(
                branch_map
            ),
            "history_tapes": history_tapes,
            "support_cost": "one fresh output cell per resolved step/branch",
        },
        "archive_access_completion_twins": completion_twins,
        "strict_compression": {
            "pair": {
                "left_word": strict_compression_pair[0],
                "right_word": strict_compression_pair[1],
                "shared_endpoint": cycle_prefix(
                    len(strict_compression_pair[0])
                )[1],
                "shared_epoch_flag": external_epoch_flag(
                    strict_compression_pair[0]
                ),
                "left_write_count": count_writes(
                    strict_compression_pair[0]
                ),
                "right_write_count": count_writes(
                    strict_compression_pair[1]
                ),
            },
            "noninjective": True,
            "autonomous_for_H": (
                "future updates and the bounded query "
                "'has any W occurred since E?'"
            ),
            "not_sufficient_for_H_prime": (
                "write count, order, timing, or full output-field access"
            ),
        },
        "verdict": {
            "minimal_epoch_transducer_unique": len(semantic_matches) == 1,
            "bounded_closed_reversible_latch_obstructed": not bool(
                reversible_matches
            ),
            "host_internal_reset_adds_provenance": not all(
                check["equal"]
                for check in internal_turnover_checks
            ),
            "fresh_output_history_can_form": is_injective(branch_map),
            "metastable_host_selects_output_archive": not (
                completion_twins["visible_completion_injective"]
                and completion_twins["hidden_completion_injective"]
                and completion_twins["same_reduced_matter_branch_map"]
                and completion_twins["admitted_archive_differs"]
            ),
            "disposition": "SUPPLIED_EPOCH_ARCHIVE",
        },
        "nonclaims": [
            "no microscopic matter-environment derivation",
            "no unique unravelling or output-field factorization",
            "no universal thermodynamic cost",
            "no public finality or record ontology",
            "no new-physics prediction",
            "no hardware result",
        ],
    }

    assert result["binary_transducer"]["unique"]
    assert not result["closed_reversible_carrier"][
        "exact_implementation_exists"
    ]
    assert parity_counterexample["parity_output"] == 0
    assert parity_counterexample["required_epoch_output"] == 1
    assert result["internal_turnover_reset"][
        "always_equals_endpoint_ready_retained_class"
    ]
    assert same_endpoint_evidence["separated"]
    assert result["fresh_output_completion"]["branch_map_injective"]
    assert completion_twins["visible_completion_injective"]
    assert completion_twins["hidden_completion_injective"]
    assert completion_twins["same_reduced_matter_branch_map"]
    assert completion_twins["admitted_archive_differs"]
    assert not result["verdict"][
        "metastable_host_selects_output_archive"
    ]
    assert result["strict_compression"]["noninjective"]
    assert result["verdict"]["disposition"] == "SUPPLIED_EPOCH_ARCHIVE"
    return result


def main() -> None:
    result = build_result()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print("PASS: exact epoch-archive boundary certified")
    print(
        "verdict:",
        result["verdict"]["disposition"],
    )
    print("artifact:", ARTIFACT)


if __name__ == "__main__":
    main()
