#!/usr/bin/env python3
"""Exact controls for HC-DU-197's causal-cut boundary.

The finite arena deliberately separates three questions:

1. Does an endpoint response identify a causal bottleneck?
2. Is one replacement arm enough to identify that bottleneck?
3. Does an interventionally complete bottleneck certificate identify the
   physical ontology of the port?

The first two questions are decided by exhaustive Boolean functions. The
third is decided by an exact same-record/different-label pair.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_source_mediator_causal_cut_result.json"


BitFunction = Callable[[int, int], int]


@dataclass(frozen=True)
class Arm:
    name: str
    replacement: int | None


NATURAL = Arm("natural", None)
REPLACE_ZERO = Arm("replace_zero", 0)
REPLACE_ONE = Arm("replace_one", 1)
ALL_ARMS = (NATURAL, REPLACE_ZERO, REPLACE_ONE)


def mediator_value(source: int, arm: Arm) -> int:
    return source if arm.replacement is None else arm.replacement


def candidate(source: int, mediator: int) -> int:
    """Pure serial mediation: the detector depends only on the port."""

    del source
    return mediator


def direct_edge_rival(source: int, mediator: int) -> int:
    """A direct S->D dependence hidden on the natural and reset-zero arms."""

    return source & mediator


def table(function: BitFunction, arms: Iterable[Arm]) -> dict[str, list[int]]:
    return {
        arm.name: [
            function(source, mediator_value(source, arm))
            for source in (0, 1)
        ]
        for arm in arms
    }


def truth_table(function: BitFunction) -> tuple[int, int, int, int]:
    return tuple(
        function(source, mediator)
        for source in (0, 1)
        for mediator in (0, 1)
    )


def function_from_mask(mask: int) -> BitFunction:
    def function(source: int, mediator: int) -> int:
        index = 2 * source + mediator
        return (mask >> index) & 1

    return function


def matches_arms(
    function: BitFunction,
    reference: BitFunction,
    arms: Iterable[Arm],
) -> bool:
    return table(function, arms) == table(reference, arms)


def has_direct_source_dependence(function: BitFunction) -> bool:
    return any(function(0, mediator) != function(1, mediator) for mediator in (0, 1))


def matching_masks(arms: Iterable[Arm]) -> list[int]:
    return [
        mask
        for mask in range(16)
        if matches_arms(function_from_mask(mask), candidate, arms)
    ]


def record_for_label(label: str) -> dict[str, object]:
    """The label is intentionally omitted from the operational record."""

    return {
        "source_settings": [0, 1],
        "arms": [arm.name for arm in ALL_ARMS],
        "detector_table": table(candidate, ALL_ARMS),
        "port_dimension": 2,
        "implementation_label_hidden": True,
    }


def build_result() -> dict[str, object]:
    candidate_table = table(candidate, ALL_ARMS)
    rival_table = table(direct_edge_rival, ALL_ARMS)

    natural_matches = matching_masks((NATURAL,))
    zero_cut_matches = matching_masks((NATURAL, REPLACE_ZERO))
    one_cut_matches = matching_masks((NATURAL, REPLACE_ONE))
    complete_matches = matching_masks(ALL_ARMS)

    gravitational_record = record_for_label("gravitational_port")
    ancilla_record = record_for_label("non_gravitational_quantum_ancilla")

    candidate_truth = truth_table(candidate)
    rival_truth = truth_table(direct_edge_rival)

    assertions = {
        "natural_endpoint_collision": (
            candidate_table[NATURAL.name] == rival_table[NATURAL.name]
        ),
        "one_zero_replacement_still_collides": (
            candidate_table[REPLACE_ZERO.name]
            == rival_table[REPLACE_ZERO.name]
        ),
        "second_replacement_separates_hidden_direct_edge": (
            candidate_table[REPLACE_ONE.name]
            != rival_table[REPLACE_ONE.name]
        ),
        "natural_arm_leaves_four_boolean_completions": (
            len(natural_matches) == 4
        ),
        "natural_plus_zero_cut_leaves_two_completions": (
            len(zero_cut_matches) == 2
        ),
        "natural_plus_one_cut_leaves_two_completions": (
            len(one_cut_matches) == 2
        ),
        "complete_replacements_select_one_boolean_response": (
            len(complete_matches) == 1
        ),
        "selected_boolean_response_has_no_direct_source_dependence": (
            not has_direct_source_dependence(function_from_mask(complete_matches[0]))
        ),
        "rival_really_has_direct_source_dependence": (
            has_direct_source_dependence(direct_edge_rival)
        ),
        "candidate_and_rival_truth_tables_differ": (
            candidate_truth != rival_truth
        ),
        "complete_operational_record_does_not_select_physical_label": (
            gravitational_record == ancilla_record
        ),
        "physical_labels_differ": (
            "gravitational_port" != "non_gravitational_quantum_ancilla"
        ),
        "trial_lineage_is_explicit": (
            gravitational_record["source_settings"] == [0, 1]
            and gravitational_record["arms"]
            == ["natural", "replace_zero", "replace_one"]
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-197",
        "disposition": (
            "INTERVENTIONALLY_COMPLETE_PORT_CERTIFIES_RELATIVE_CAUSAL_"
            "BOTTLENECK_NOT_PHYSICAL_ONTOLOGY"
        ),
        "arena": {
            "source": "binary split-node input S",
            "candidate_port": "binary mediator M",
            "detector": "binary response D",
            "candidate_rule": "D=M",
            "direct_edge_rival_rule": "D=S AND M",
            "surgical_arms": [arm.name for arm in ALL_ARMS],
        },
        "candidate_table": candidate_table,
        "direct_edge_rival_table": rival_table,
        "candidate_truth_table_order_s0m0_s0m1_s1m0_s1m1": candidate_truth,
        "direct_edge_rival_truth_table_order_s0m0_s0m1_s1m0_s1m1": rival_truth,
        "completion_counts": {
            "natural_only": len(natural_matches),
            "natural_and_replace_zero": len(zero_cut_matches),
            "natural_and_replace_one": len(one_cut_matches),
            "natural_and_both_replacements": len(complete_matches),
        },
        "matching_masks": {
            "natural_only": natural_matches,
            "natural_and_replace_zero": zero_cut_matches,
            "natural_and_replace_one": one_cut_matches,
            "natural_and_both_replacements": complete_matches,
        },
        "same_record_different_physical_label": {
            "record": gravitational_record,
            "completion_labels": [
                "gravitational_port",
                "non_gravitational_quantum_ancilla",
            ],
        },
        "assertions": assertions,
        "theorem_statement": (
            "In the frozen binary split-node class, natural behavior plus one "
            "replacement arm does not establish that M is a complete causal "
            "bottleneck. Source-conditioned responses under a spanning "
            "replacement family reconstruct the complete response f(S,M) and "
            "thereby decide direct S-to-D functional dependence. Even that "
            "complete operational certificate is invariant under replacing a "
            "named gravitational port with an operationally identical quantum "
            "ancilla, so physical ontology still requires independently formed "
            "port lineage or a theory-level selection result."
        ),
        "quantum_transfer": (
            "For quantum systems, replace the two Boolean replacements by an "
            "informationally complete spanning family of CP interventions and "
            "test the quantum process/Markov factorization. One causal break "
            "remains only a necessary control; complete process access "
            "certifies an operational causal structure, not a unique dilation "
            "or named field ontology."
        ),
        "scope_guard": (
            "This is an exact finite causal-identification and typing result. "
            "It proves no gravitational mediator, complete quantum-field port, "
            "observed causal break, new causal theorem, physical interface "
            "selection, or Grade-5 remainder."
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
