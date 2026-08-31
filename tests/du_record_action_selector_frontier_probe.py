#!/usr/bin/env python3
"""Exact controls for the record-algebra / consumer-action selector frontier.

The probe uses a reversible three-bit write/consume/unwrite circuit as a
classical-basis subtheory of finite quantum mechanics.  It proves that a
formed, nondemolition record and its inverse write do not select a downstream
conditional action.  It also checks the matched-relabeling descent already
banked by HC-DU-204 and source-artifact consistency for the three selector
mechanism families compared by HC-DU-205.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_record_action_selector_frontier_result.json"

State = tuple[int, int, int]  # source, record, target
Policy = tuple[int, int]


def writer(state: State) -> State:
    """CNOT from source to record; self-inverse and reversible."""

    source, record, target = state
    return source, record ^ source, target


def consumer(state: State, policy: Policy) -> State:
    """Apply a record-controlled target flip selected by the policy."""

    source, record, target = state
    return source, record, target ^ policy[record]


def permutation_matrix(transform) -> list[list[int]]:
    """Exact 8x8 permutation matrix for a reversible three-bit map."""

    matrix = [[0 for _ in range(8)] for _ in range(8)]
    for source, record, target in itertools.product((0, 1), repeat=3):
        old = 4 * source + 2 * record + target
        new_state = transform((source, record, target))
        new = 4 * new_state[0] + 2 * new_state[1] + new_state[2]
        matrix[new][old] = 1
    return matrix


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def record_projector(value: int) -> list[list[int]]:
    return [
        [int(i == j and ((i // 2) % 2) == value) for j in range(8)]
        for i in range(8)
    ]


def load_artifact(name: str) -> dict[str, object]:
    return json.loads((ROOT / "tests" / "artifacts" / name).read_text())


def run() -> dict[str, object]:
    policies = tuple(itertools.product((0, 1), repeat=2))
    writer_matrix = permutation_matrix(writer)
    assert transpose(writer_matrix) == writer_matrix
    assert multiply(transpose(writer_matrix), writer_matrix) == identity(8)

    policy_rows = []
    response_signatures = set()
    record_snapshots = set()
    for policy in policies:
        consumer_matrix = permutation_matrix(lambda state, p=policy: consumer(state, p))

        # Every conditional consumer preserves the complete classical record
        # algebra: it commutes with both record-sector projectors.
        for record_value in (0, 1):
            projector = record_projector(record_value)
            assert multiply(consumer_matrix, projector) == multiply(
                projector, consumer_matrix
            )

        rows = []
        for source in (0, 1):
            initial = (source, 0, 0)
            formed = writer(initial)
            used = consumer(formed, policy)
            erased = writer(used)
            assert formed == (source, source, 0)
            assert used[:2] == formed[:2]
            assert erased == (source, 0, policy[source])
            rows.append(
                {
                    "source": source,
                    "formed": list(formed),
                    "after_consumer": list(used),
                    "after_inverse_write": list(erased),
                }
            )

        signature = tuple(row["after_inverse_write"][2] for row in rows)
        snapshot = tuple(tuple(row["formed"][:2]) for row in rows)
        response_signatures.add(signature)
        record_snapshots.add(snapshot)
        policy_rows.append(
            {
                "policy": list(policy),
                "target_response_signature": list(signature),
                "rows": rows,
            }
        )

    # Same writer and formed-record algebra support four distinct downstream
    # policies.  Formation-only or record-preservation-only antecedents cannot
    # point-select the consumer.
    assert len(record_snapshots) == 1
    assert len(response_signatures) == 4

    # The inverse write alone erases the record and changes no target.
    inverse_only = []
    for source in (0, 1):
        initial = (source, 0, 0)
        inverse_only.append(writer(writer(initial)))
    assert inverse_only == [(0, 0, 0), (1, 0, 0)]

    # Exact HC-DU-204 matched-label descent.  A producer re-encoding and the
    # co-transformed policy preserve the target response.  An unmatched swap
    # is harmless only for the two constant policies.
    matched_cases = 0
    unmatched_cases = 0
    relabel_rows = []
    for permutation in ((0, 1), (1, 0)):
        inverse_permutation = tuple(permutation.index(value) for value in (0, 1))
        for policy in policies:
            co_policy = tuple(policy[inverse_permutation[label]] for label in (0, 1))
            matched = tuple(co_policy[permutation[source]] for source in (0, 1))
            unmatched = tuple(policy[permutation[source]] for source in (0, 1))
            matched_ok = matched == policy
            unmatched_ok = unmatched == policy
            assert matched_ok
            matched_cases += int(matched_ok)
            unmatched_cases += int(unmatched_ok)
            relabel_rows.append(
                {
                    "permutation": list(permutation),
                    "policy": list(policy),
                    "matched_response": list(matched),
                    "unmatched_response": list(unmatched),
                    "unmatched_invariant": unmatched_ok,
                }
            )
    assert matched_cases == 8
    assert unmatched_cases == 6

    # Source-grounded consistency with the three compared mechanism families
    # and the embodied-relation control.
    qnd = load_artifact("du_robust_physical_instrument_selection_result.json")
    direct_action = load_artifact("du_mediator_elimination_interface_fork_result.json")
    embodied = load_artifact("du_relational_reference_symmetry_reduction_result.json")
    ir_text = (
        ROOT
        / "explorations"
        / "finite-time-infrared-memory-typed-record-reopener-audit-2026-07-28.md"
    ).read_text()

    assert qnd["summary"]["all_passed"] is True
    assert qnd["continuation_selector"]["same_effect_error"] == 0.0
    assert qnd["continuation_selector"]["selective_output_trace_distance"] == 1.0
    assert direct_action["status"] == "PASS"
    assert embodied["status"] == "PASS"
    assert "PARTIAL_PHYSICAL_TYPING" in ir_text
    assert "FINITE_OPERATIONAL_RECORD_INTERFACE: not selected" in ir_text

    tournament = {
        "source_action_qnd": {
            "selected": [
                "record axis/effective instrument orbit inside a frozen informative QND candidate class"
            ],
            "not_selected": [
                "source action and candidate class",
                "downstream consumer action",
                "archive/access boundary",
                "microscopic dilation",
            ],
            "decisive_witness": "same effects and record, orthogonal selective continuation",
            "full_handoff_selected": False,
        },
        "finite_time_infrared_memory": {
            "selected": [
                "soft carrier structure",
                "conditional dressing component after a time frame and rotation subgroup are supplied",
            ],
            "not_selected": [
                "bounded detector and resolution",
                "blank-to-written provenance archive",
                "consumer/action family",
                "held-out reconstruction target",
            ],
            "decisive_witness": "physical detector resolution indexes a family of record quotients",
            "full_handoff_selected": False,
        },
        "direct_action": {
            "selected": [
                "source relation/response after a direct-action theory and boundary prescription are supplied"
            ],
            "not_selected": [
                "mediator or absorber factorization",
                "event partition",
                "formed archive and provenance",
                "consumer/access/action family",
            ],
            "decisive_witness": "one source kernel has inequivalent channel factorizations",
            "full_handoff_selected": False,
        },
        "embodied_relation_control": {
            "selected": [
                "bounded prepare/invert capability through reuse of one stable interaction"
            ],
            "not_selected": [
                "formed retained occurrence record",
                "portable archive",
                "public certification",
            ],
            "decisive_witness": "action-relative capability exists without a record token",
            "full_handoff_selected": False,
        },
    }
    assert not any(row["full_handoff_selected"] for row in tournament.values())

    return {
        "claim_id": "HC-DU-205",
        "run_id": "RUN-20260831-151458-record-module-selector-tournament",
        "status": "PASS",
        "exact_consumer_freedom": {
            "record_labels": [0, 1],
            "consumer_policies_checked": len(policies),
            "distinct_formed_record_snapshots": len(record_snapshots),
            "distinct_target_response_signatures": len(response_signatures),
            "all_consumers_commute_with_record_projectors": True,
            "policy_rows": policy_rows,
        },
        "inverse_write_boundary": {
            "writer_is_self_inverse": True,
            "inverse_only_outputs": [list(state) for state in inverse_only],
            "result": "inverse write returns the record to blank; it does not select a target action",
        },
        "matched_orbit_control": {
            "cases_checked": len(relabel_rows),
            "matched_invariant_cases": matched_cases,
            "unmatched_invariant_cases": unmatched_cases,
            "rows": relabel_rows,
        },
        "selector_tournament": tournament,
        "earned": [
            "exact record-preserving consumer-action freedom",
            "exact inverse-write erasure/nonselection boundary",
            "matched label-orbit descent regression",
            "unchanged-passport comparison of three physical selector families",
            "minimum reopener localized to a cross-boundary write/read action law",
        ],
        "not_earned": [
            "a full physical handoff selector",
            "a universal no-go against physical handoff selection",
            "regional composition or public finality",
            "empirical excess, new physics, or ontology priority",
        ],
        "verdict": "NO_CURRENT_MECHANISM_SELECTS_A_COMPLETE_HANDOFF; RECORD_FORMATION_AND_RECORD_PRESERVATION_LEAVE_CONSUMER_ACTION_FREE; THE_INVERSE_WRITE_ERASES_BUT_DOES_NOT_SUPPLY_USE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
