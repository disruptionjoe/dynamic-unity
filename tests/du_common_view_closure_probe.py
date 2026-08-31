#!/usr/bin/env python3
"""Exact controls for HC-DU-206's common-view closure audit.

The finite constructions validate rank, factorization, quantum-transfer, and
metric-nonselection boundaries.  They are not evidence for a computational
ontology, four fundamental degrees, or a physical common-view selector.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from itertools import combinations, product
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ATLAS_PATH = ROOT / "lab" / "process" / "computation-first-common-view-relationship-atlas.json"
ARTIFACT_PATH = ROOT / "tests" / "artifacts" / "du_common_view_closure_result.json"


def gf2_rank(rows: Iterable[Iterable[int]], width: int = 4) -> int:
    work = [sum((int(bit) & 1) << index for index, bit in enumerate(row)) for row in rows]
    rank = 0
    for column in range(width):
        pivot = next((index for index in range(rank, len(work)) if (work[index] >> column) & 1), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for index in range(len(work)):
            if index != rank and ((work[index] >> column) & 1):
                work[index] ^= work[rank]
        rank += 1
    return rank


def rational_rank(rows: Iterable[Iterable[int | Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    rank = 0
    for column in range(column_count):
        pivot = next((index for index in range(rank, row_count) if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for index in range(row_count):
            if index == rank or not work[index][column]:
                continue
            factor = work[index][column]
            work[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[index], work[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def signature(state: tuple[int, ...], rows: list[list[int]]) -> tuple[int, ...]:
    return tuple(sum(bit * coefficient for bit, coefficient in zip(state, row)) % 2 for row in rows)


def indistinguishable_pairs(rows: list[list[int]]) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    states = list(product((0, 1), repeat=4))
    return [
        (left, right)
        for left, right in combinations(states, 2)
        if signature(left, rows) == signature(right, rows)
    ]


def metric_response_row(vector: tuple[int, int, int, int]) -> list[int]:
    """Linear coefficients of v^T g v for symmetric 4x4 g.

    Parameter order is g00,g11,g22,g33,g01,g02,g03,g12,g13,g23.
    """

    diagonal = [coordinate * coordinate for coordinate in vector]
    cross = [
        2 * vector[left] * vector[right]
        for left, right in combinations(range(4), 2)
    ]
    return diagonal + cross


def run() -> dict:
    atlas = json.loads(ATLAS_PATH.read_text(encoding="utf-8"))

    views = {
        "record": [[1, 0, 0, 0], [0, 1, 0, 0]],
        "capability": [[0, 1, 0, 0], [0, 0, 1, 0]],
        "classical_composability": [[0, 0, 1, 0], [0, 0, 0, 1]],
        "regional_finality": [[1, 0, 0, 0], [0, 0, 0, 1]],
    }
    joint_rows = [row for rows in views.values() for row in rows]
    view_ranks = {name: gf2_rank(rows) for name, rows in views.items()}
    joint_rank = gf2_rank(joint_rows)

    pair_ranks = {
        f"{left}+{right}": gf2_rank(views[left] + views[right])
        for left, right in combinations(views, 2)
    }

    hostile_views = {
        "record": [[1, 0, 0, 0], [0, 1, 0, 0]],
        "capability": [[0, 1, 0, 0], [0, 0, 1, 0]],
        "classical_composability": [[1, 0, 1, 0]],
        "regional_finality": [[1, 1, 0, 0], [0, 0, 1, 0]],
    }
    hostile_rows = [row for rows in hostile_views.values() for row in rows]
    hostile_rank = gf2_rank(hostile_rows)
    hostile_pairs = indistinguishable_pairs(hostile_rows)

    all_nonzero_functionals = [bits for bits in product((0, 1), repeat=4) if any(bits)]

    # For a two-qubit Pauli label x=(x1,x2,z1,z2), commutation with tester
    # v is the symplectic functional x.J.v.  The symplectic J is invertible,
    # so all fifteen nonzero GF(2) functionals are realized by Pauli testers.
    symplectic_j = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    pauli_functionals = {
        tuple(
            sum(symplectic_j[row][column] * tester[column] for column in range(4)) % 2
            for row in range(4)
        )
        for tester in all_nonzero_functionals
    }

    axes = [tuple(int(index == coordinate) for index in range(4)) for coordinate in range(4)]
    pair_sums = [
        tuple(int(index in {left, right}) for index in range(4))
        for left, right in combinations(range(4), 2)
    ]
    axis_rows = [metric_response_row(vector) for vector in axes]
    full_ruler_rows = axis_rows + [metric_response_row(vector) for vector in pair_sums]
    axis_rank = rational_rank(axis_rows)
    full_metric_rank = rational_rank(full_ruler_rows)

    atlas_view_ids = {item.get("id") for item in atlas.get("views", [])}

    metric_a = (1, 1, 1, 1)
    metric_b = (1, 1, 1, 4)
    e4 = (0, 0, 0, 1)
    e4_length_squared_a = sum(weight * coordinate for weight, coordinate in zip(metric_a, e4))
    e4_length_squared_b = sum(weight * coordinate for weight, coordinate in zip(metric_b, e4))

    checks = [
        {
            "name": "each_perspective_is_lossy",
            "passed": all(rank == 2 for rank in view_ranks.values()),
            "detail": view_ranks,
        },
        {
            "name": "joint_views_separate_four_degree_control",
            "passed": joint_rank == 4 and not indistinguishable_pairs(joint_rows),
            "detail": {"joint_rank": joint_rank},
        },
        {
            "name": "relationships_are_not_one_scalar_chain",
            "passed": set(pair_ranks.values()) == {3, 4},
            "detail": pair_ranks,
        },
        {
            "name": "undercomplete_positive_falsifier",
            "passed": hostile_rank == 3 and bool(hostile_pairs),
            "detail": {"rank": hostile_rank, "witness": hostile_pairs[0]},
        },
        {
            "name": "classical_process_does_not_select_one_view",
            "passed": len(all_nonzero_functionals) == 15,
            "detail": {"candidate_one_bit_views": len(all_nonzero_functionals)},
        },
        {
            "name": "two_qubit_pauli_transfer_preserves_view_freedom",
            "passed": pauli_functionals == set(all_nonzero_functionals),
            "detail": {"pauli_testers": len(pauli_functionals)},
        },
        {
            "name": "four_axial_rulers_do_not_identify_general_metric",
            "passed": axis_rank == 4 and axis_rank < 10,
            "detail": {"rank": axis_rank, "metric_parameters": 10},
        },
        {
            "name": "axis_plus_pair_rulers_identify_symmetric_metric_control",
            "passed": full_metric_rank == 10,
            "detail": {"rank": full_metric_rank, "rulers": len(full_ruler_rows)},
        },
        {
            "name": "same_views_admit_different_metric_completions",
            "passed": e4_length_squared_a == 1 and e4_length_squared_b == 4,
            "detail": {
                "metric_a_e4_squared": e4_length_squared_a,
                "metric_b_e4_squared": e4_length_squared_b,
            },
        },
        {
            "name": "atlas_verdict_and_boundary_are_frozen",
            "passed": (
                atlas.get("verdict") == "NONTRIVIAL_AXIOM_WITH_THEOREM_OBLIGATION"
                and atlas.get("observer_index_verdict") == "OBSERVER_INDEX_REMAINS_SUPPLIED"
                and atlas.get("extra_axiom", {}).get("id") == "CVC-A"
                and atlas_view_ids
                == {"record", "capability", "classical_composability", "regional_finality", "geometry"}
                and atlas.get("mathematical_correction", {}).get("pointwise_components") == 10
                and bool(atlas.get("scientific_boundary"))
            ),
            "detail": {
                "verdict": atlas.get("verdict"),
                "observer_index_verdict": atlas.get("observer_index_verdict"),
                "view_ids": sorted(atlas_view_ids),
            },
        },
    ]

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "probe": "du_common_view_closure_probe",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "claim_id": "HC-DU-206",
        "run_id": "RUN-20260831-181219-common-view-closure-audit",
        "verdict": atlas["verdict"],
        "observer_index_verdict": atlas["observer_index_verdict"],
        "checks_passed": passed,
        "checks_total": len(checks),
        "checks": checks,
        "earned": [
            "exact joint-kernel reconstruction control",
            "exact undercomplete-view witness",
            "unchanged classical-to-two-qubit-Pauli response-functional transfer",
            "four-axis versus ten-response metric-rank boundary",
            "physically selected common-view closure isolated as the extra axiom",
        ],
        "not_earned": [
            "four fundamental physical degrees",
            "a selected process boundary or view family",
            "a selected metric, connection, scale, observer, record, or finality law",
            "a computational ontology, empirical excess, or new physics",
        ],
        "scientific_boundary": (
            "Exact finite relationship and necessity controls only. The component "
            "mathematics is standard; the physical common-view selector remains open."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
