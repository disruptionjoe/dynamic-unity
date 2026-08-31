#!/usr/bin/env python3
"""Exact controls for record-consumer diagonal descent.

The probe distinguishes a coordinated re-encoding of a record and its
consumer from an unmatched producer/consumer handoff.  It also applies the
same finite contract to the Bell and real-time-QEC specimens already banked
in Dynamic Unity.  It validates algebra and source-artifact consistency only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Hashable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_record_consumer_diagonal_descent_result.json"
)

Label = Hashable


def compose(
    encoder: list[list[Fraction]], consumer: list[list[Fraction]]
) -> list[list[Fraction]]:
    """Compose x->record and record->output stochastic matrices."""

    return [
        [
            sum(encoder[x][r] * consumer[r][y] for r in range(len(consumer)))
            for y in range(len(consumer[0]))
        ]
        for x in range(len(encoder))
    ]


def relabel_encoder(
    encoder: list[list[Fraction]], permutation: tuple[int, ...]
) -> list[list[Fraction]]:
    """Implement new_label=permutation[old_label]."""

    relabeled = [[Fraction(0) for _ in permutation] for _ in encoder]
    for x, row in enumerate(encoder):
        for old, probability in enumerate(row):
            relabeled[x][permutation[old]] = probability
    return relabeled


def relabel_consumer(
    consumer: list[list[Fraction]], permutation: tuple[int, ...]
) -> list[list[Fraction]]:
    """Make the consumer interpret the coordinated new labels."""

    relabeled = [list() for _ in permutation]
    for old, row in enumerate(consumer):
        relabeled[permutation[old]] = list(row)
    return relabeled


def relabel_function(
    function: dict[Label, Label], permutation: dict[Label, Label]
) -> dict[Label, Label]:
    """Return a'=a o permutation^-1 in lookup form."""

    return {permutation[label]: value for label, value in function.items()}


def deterministic_closed_response(
    domain: tuple[Label, ...],
    encoder: dict[Label, Label],
    consumer: dict[Label, Label],
) -> dict[Label, Label]:
    return {point: consumer[encoder[point]] for point in domain}


def load_artifact(name: str) -> dict[str, object]:
    return json.loads((ROOT / "tests" / "artifacts" / name).read_text())


def run() -> dict[str, object]:
    # Exact stochastic positive and hostile controls.
    encoder = [
        [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)],
        [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)],
    ]
    consumer = [
        [Fraction(1), Fraction(0)],
        [Fraction(1, 3), Fraction(2, 3)],
        [Fraction(0), Fraction(1)],
    ]
    baseline = compose(encoder, consumer)
    stochastic_rows = []
    for permutation in itertools.permutations(range(3)):
        matched = compose(
            relabel_encoder(encoder, permutation),
            relabel_consumer(consumer, permutation),
        )
        unmatched = compose(relabel_encoder(encoder, permutation), consumer)
        assert matched == baseline
        stochastic_rows.append(
            {
                "permutation": list(permutation),
                "matched_equals_baseline": True,
                "unmatched_equals_baseline": unmatched == baseline,
            }
        )
    assert sum(row["unmatched_equals_baseline"] for row in stochastic_rows) == 1

    # Exhaustive deterministic theorem control.  Matched descent holds for
    # every encoder, policy, and permutation.  An unmatched re-encoding is
    # harmless exactly when the policy is constant on the moved labels that
    # the encoder actually reaches.
    domain = (0, 1, 2)
    labels = (0, 1, 2)
    outputs = (0, 1)
    deterministic_cases = 0
    surjective_cases = 0
    for encoded_values in itertools.product(labels, repeat=len(domain)):
        det_encoder = dict(zip(domain, encoded_values, strict=True))
        image = set(encoded_values)
        for policy_values in itertools.product(outputs, repeat=len(labels)):
            policy = dict(zip(labels, policy_values, strict=True))
            baseline_response = deterministic_closed_response(
                domain, det_encoder, policy
            )
            for permutation_values in itertools.permutations(labels):
                permutation = dict(zip(labels, permutation_values, strict=True))
                matched_encoder = {
                    point: permutation[label]
                    for point, label in det_encoder.items()
                }
                matched_policy = relabel_function(policy, permutation)
                assert (
                    deterministic_closed_response(
                        domain, matched_encoder, matched_policy
                    )
                    == baseline_response
                )
                unmatched_equal = (
                    deterministic_closed_response(
                        domain, matched_encoder, policy
                    )
                    == baseline_response
                )
                stabilizes_reached_policy = all(
                    policy[permutation[label]] == policy[label]
                    for label in image
                )
                assert unmatched_equal == stabilizes_reached_policy
                deterministic_cases += 1
                if image == set(labels):
                    surjective_cases += 1
    assert deterministic_cases == 1296
    assert surjective_cases == 288

    # Bell application.  A coordinated relabeling of the four Pauli labels and
    # correction table preserves branchwise correction.  If the producer alone
    # is relabeled, a full unknown-qubit task permits only the identity
    # permutation.  A terminal Z statistic permits the larger sign stabilizer.
    paulis = ("I", "X", "Y", "Z")
    pauli_signatures = {
        "I": (1, 1, 1),
        "X": (1, -1, -1),
        "Y": (-1, 1, -1),
        "Z": (-1, -1, 1),
    }
    bell_matched = 0
    bell_unmatched_full = 0
    bell_unmatched_terminal_z = 0
    for values in itertools.permutations(paulis):
        permutation = dict(zip(paulis, values, strict=True))
        matched_policy = relabel_function({p: p for p in paulis}, permutation)
        matched_ok = all(matched_policy[permutation[p]] == p for p in paulis)
        unmatched_full_ok = all(permutation[p] == p for p in paulis)
        unmatched_z_ok = all(
            pauli_signatures[permutation[p]][2] == pauli_signatures[p][2]
            for p in paulis
        )
        bell_matched += matched_ok
        bell_unmatched_full += unmatched_full_ok
        bell_unmatched_terminal_z += unmatched_z_ok
    assert bell_matched == 24
    assert bell_unmatched_full == 1
    assert bell_unmatched_terminal_z == 4

    # QEC application.  The action consumer identifies statuses 0 and 2 as
    # idle and status 1 as conditional X.  Its unmatched stabilizer contains
    # identity and the 0<->2 swap.  HC-DU-169 shows the same swap is not a
    # symmetry of the retained timing law.
    statuses = (0, 1, 2)
    qec_policy = {0: "idle", 1: "X", 2: "idle"}
    qec_action_stabilizers = []
    for values in itertools.permutations(statuses):
        permutation = dict(zip(statuses, values, strict=True))
        if all(qec_policy[permutation[s]] == qec_policy[s] for s in statuses):
            qec_action_stabilizers.append(list(values))
    assert qec_action_stabilizers == [[0, 1, 2], [2, 1, 0]]

    bell_source = load_artifact("du_bell_prescription_execution_result.json")
    qec_action_source = load_artifact(
        "du_action_resource_finality_quotient_result.json"
    )
    qec_controller_source = load_artifact(
        "du_controller_sidecar_recovery_result.json"
    )
    bell_manual = bell_source["source_scope"]["manual_source_audit"]
    qec_action = qec_action_source["source_defined_action_quotient"]
    qec_ladder = {
        row["level"]: row["status"]
        for row in qec_controller_source["public_sidecar_ladder"]
    }
    assert bell_manual["correction_prescription_derived"] is True
    assert bell_manual["outcome_conditioned_physical_pauli_gate_reported"] is False
    assert qec_action == {
        "no_action_statuses": [0, 2],
        "conditional_x_status": 1,
    }
    assert qec_ladder["intended_command_semantics"] == "SOURCE_SPECIFIED"
    assert (
        qec_ladder["aggregate_physical_actuation_check"]
        == "PARTIALLY_SPECIFIED"
    )
    timing_swap_separated = all(
        row["median_gap_d2_minus_d0"] > 0
        for row in qec_action_source["discovery_timing"]
    )
    assert timing_swap_separated

    return {
        "claim_id": "HC-DU-204",
        "run_id": "RUN-20260831-144802-record-consumer-diagonal-descent",
        "status": "PASS",
        "general_exact_controls": {
            "stochastic_permutations": stochastic_rows,
            "stochastic_matched_invariant_count": 6,
            "stochastic_unmatched_invariant_count": 1,
            "deterministic_cases_checked": deterministic_cases,
            "surjective_deterministic_cases_checked": surjective_cases,
            "matched_descent_universal_in_fixture": True,
            "unmatched_invariance_equals_reached_policy_stabilizer": True,
        },
        "bell_application": {
            "record_labels": list(paulis),
            "matched_relabelings_preserving_full_correction": bell_matched,
            "unmatched_relabelings_preserving_full_unknown_qubit_task": bell_unmatched_full,
            "unmatched_relabelings_preserving_terminal_z_statistic": bell_unmatched_terminal_z,
            "active_physical_pauli_gate_reported": False,
            "interpretation": "absolute label names are dispensable; matched correction semantics are not",
        },
        "qec_application": {
            "status_to_action": qec_policy,
            "unmatched_action_stabilizers": qec_action_stabilizers,
            "status_0_2_swap_separated_by_retained_timing": timing_swap_separated,
            "intended_command_semantics": qec_ladder["intended_command_semantics"],
            "aggregate_actuation_evidence": qec_ladder[
                "aggregate_physical_actuation_check"
            ],
            "interpretation": "a relabeling can be gauge for action and physical for resource timing",
        },
        "theorem_boundary": {
            "matched_diagonal_action": "re-encode producer labels and co-transform consumer semantics",
            "unmatched_action": "change producer encoding or consumer semantics independently",
            "formal_descent": "closed response is invariant under every matched record relabeling",
            "physical_gauge_requirement": "all declared dynamics, costs, provenance, records, and capabilities must descend",
        },
        "earned": [
            "exact diagonal record-consumer relabeling descent",
            "exact unmatched-handoff stabilizer criterion",
            "Bell action-family stabilizer contraction from terminal Z to arbitrary qubit continuation",
            "QEC witness that action equivalence need not preserve retained timing",
            "correction from point-selection-only to selection-or-joint-descent",
        ],
        "not_earned": [
            "physical selection of a Bell or QEC controller from bare dynamics",
            "per-attempt QEC actuation lineage",
            "universal observer selection",
            "regional finality composition",
            "new physics, empirical excess, or ontology priority",
        ],
        "verdict": "MATCHED_RECORD_CONSUMER_ORBIT_CAN_DESCEND_WITHOUT_ABSOLUTE_INTERFACE_SELECTION_BUT_ALIGNMENT_AND_FULL_PHYSICAL_GAUGE_REMAIN_TO_BE_SELECTED_OR_PROVED",
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
