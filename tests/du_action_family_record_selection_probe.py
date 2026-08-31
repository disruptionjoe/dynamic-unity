#!/usr/bin/env python3
"""Exact action-family record-selection controls for HC-DU-202.

The eight-element carrier and correction map come from the source-pinned
heralded Bell apparatus banked in HC-DU-201. This probe exhausts all 4,140 set
partitions of that carrier, verifies the coarsest common-sufficient quotient
for every subset of a frozen task family, and supplies exact Blackwell-style
decision witnesses. It does not validate the source experiment or select a
physical continuation family.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_action_family_record_selection_result.json"
Raw = tuple[int, int, int]
Task = Callable[[Raw], Hashable]
Partition = tuple[tuple[Raw, ...], ...]

RAW: tuple[Raw, ...] = tuple(itertools.product((0, 1), repeat=3))


def passage(raw: Raw) -> int:
    return raw[0]


def herald(raw: Raw) -> int:
    return raw[1]


def atom(raw: Raw) -> int:
    return raw[2]


def parity(raw: Raw) -> int:
    return raw[1] ^ raw[2]


def correction(raw: Raw) -> tuple[int, int]:
    return passage(raw), parity(raw)


def identity(raw: Raw) -> Raw:
    return raw


TASKS: dict[str, Task] = {
    "bell_family": passage,
    "bell_sign": parity,
    "correction": correction,
    "herald_audit": herald,
    "atom_audit": atom,
    "raw_identity": identity,
}


def canonical_partition(blocks: Iterable[Iterable[Raw]]) -> Partition:
    normalized = [tuple(sorted(block)) for block in blocks]
    return tuple(sorted(normalized, key=lambda block: RAW.index(block[0])))


def all_partitions(items: tuple[Raw, ...]) -> Iterable[Partition]:
    """Generate every set partition exactly once."""
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in all_partitions(rest):
        yield canonical_partition(((first,), *partition))
        for index in range(len(partition)):
            blocks = [list(block) for block in partition]
            blocks[index].append(first)
            yield canonical_partition(blocks)


def task_signature(raw: Raw, names: tuple[str, ...]) -> tuple[Hashable, ...]:
    return tuple(TASKS[name](raw) for name in names)


def kernel_partition(names: tuple[str, ...]) -> Partition:
    blocks: dict[tuple[Hashable, ...], list[Raw]] = {}
    for raw in RAW:
        blocks.setdefault(task_signature(raw, names), []).append(raw)
    return canonical_partition(blocks.values())


def is_sufficient(partition: Partition, names: tuple[str, ...]) -> bool:
    return all(
        len({task_signature(raw, names) for raw in block}) == 1
        for block in partition
    )


def refines(fine: Partition, coarse: Partition) -> bool:
    coarse_lookup = {
        raw: block_index
        for block_index, block in enumerate(coarse)
        for raw in block
    }
    return all(
        len({coarse_lookup[raw] for raw in block}) == 1
        for block in fine
    )


def relabel_partition(partition: Partition, permutation: dict[Raw, Raw]) -> Partition:
    return canonical_partition(
        tuple(permutation[raw] for raw in block) for block in partition
    )


def gf2_rank(rows: list[tuple[int, int, int]]) -> int:
    matrix = [list(row) for row in rows if any(row)]
    rank = 0
    for column in range(3):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for index in range(len(matrix)):
            if index != rank and matrix[index][column]:
                matrix[index] = [
                    left ^ right for left, right in zip(matrix[index], matrix[rank])
                ]
        rank += 1
    return rank


LINEAR_ROWS: dict[str, list[tuple[int, int, int]]] = {
    "bell_family": [(1, 0, 0)],
    "bell_sign": [(0, 1, 1)],
    "correction": [(1, 0, 0), (0, 1, 1)],
    "herald_audit": [(0, 1, 0)],
    "atom_audit": [(0, 0, 1)],
    "raw_identity": [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
}


def best_uniform_guess_success(observation: Task, target: Task) -> float:
    blocks: dict[Hashable, list[Raw]] = {}
    for raw in RAW:
        blocks.setdefault(observation(raw), []).append(raw)
    correct = 0
    for block in blocks.values():
        counts: dict[Hashable, int] = {}
        for raw in block:
            value = target(raw)
            counts[value] = counts.get(value, 0) + 1
        correct += max(counts.values())
    return correct / len(RAW)


def run() -> dict[str, object]:
    partitions = tuple(all_partitions(RAW))
    assert len(partitions) == 4140
    assert len(set(partitions)) == 4140

    # A bare eight-element carrier has the full symmetric group as its
    # relabeling group. Adjacent transpositions generate S_8. The only
    # partitions invariant under every bare relabeling are equality and the
    # indiscrete partition; any nontrivial quotient needs additional typed
    # structure.
    adjacent_transpositions: list[dict[Raw, Raw]] = []
    for index in range(len(RAW) - 1):
        permutation = {raw: raw for raw in RAW}
        permutation[RAW[index]] = RAW[index + 1]
        permutation[RAW[index + 1]] = RAW[index]
        adjacent_transpositions.append(permutation)
    bare_invariant_partitions = [
        partition
        for partition in partitions
        if all(
            relabel_partition(partition, permutation) == partition
            for permutation in adjacent_transpositions
        )
    ]
    assert len(bare_invariant_partitions) == 2
    assert {len(partition) for partition in bare_invariant_partitions} == {1, 8}

    # The actual apparatus already types the three coordinates differently.
    # Even the residual herald/atom swap preserves many partitions, so
    # symmetry admission remains weaker than selection.
    herald_atom_swap = {
        raw: (raw[0], raw[2], raw[1])
        for raw in RAW
    }
    typed_invariant_partitions = [
        partition
        for partition in partitions
        if relabel_partition(partition, herald_atom_swap) == partition
    ]
    assert correction(raw=(0, 0, 1)) == correction(raw=(0, 1, 0))
    assert kernel_partition(("correction",)) in typed_invariant_partitions
    assert len(typed_invariant_partitions) > 2

    subset_results: list[dict[str, object]] = []
    task_names = tuple(TASKS)
    for size in range(len(task_names) + 1):
        for names in itertools.combinations(task_names, size):
            kernel = kernel_partition(names)
            sufficient = [p for p in partitions if is_sufficient(p, names)]
            minimum_count = min(len(p) for p in sufficient)
            minimum = [p for p in sufficient if len(p) == minimum_count]

            # The kernel of the joint task signature is the unique coarsest
            # sufficient partition, and every sufficient partition refines it.
            assert len(minimum) == 1
            assert minimum[0] == kernel
            assert all(refines(p, kernel) for p in sufficient)

            rows = [row for name in names for row in LINEAR_ROWS[name]]
            rank = gf2_rank(rows)
            assert len(kernel) == 2**rank
            subset_results.append(
                {
                    "tasks": list(names),
                    "minimum_classes": len(kernel),
                    "minimum_bits": rank,
                    "sufficient_partition_count": len(sufficient),
                }
            )

    correction_kernel = kernel_partition(("correction",))
    correction_herald_kernel = kernel_partition(("correction", "herald_audit"))
    correction_atom_kernel = kernel_partition(("correction", "atom_audit"))
    identity_kernel = kernel_partition(("raw_identity",))

    assert len(correction_kernel) == 4
    assert correction_herald_kernel == identity_kernel
    assert correction_atom_kernel == identity_kernel
    assert len(identity_kernel) == 8

    # Exactly sixteen partitions preserve the correction task: each of its
    # four two-element blocks may either remain joined or split. Only one of
    # those sixteen is coarsest.
    correction_sufficient = [
        p for p in partitions if is_sufficient(p, ("correction",))
    ]
    assert len(correction_sufficient) == 16
    assert sum(len(p) == 4 for p in correction_sufficient) == 1

    decision_witnesses = {
        "guess_correction_from_correction_quotient": best_uniform_guess_success(
            correction, correction
        ),
        "guess_herald_from_correction_quotient": best_uniform_guess_success(
            correction, herald
        ),
        "guess_atom_from_correction_quotient": best_uniform_guess_success(
            correction, atom
        ),
        "guess_herald_from_raw": best_uniform_guess_success(identity, herald),
        "guess_atom_from_raw": best_uniform_guess_success(identity, atom),
    }
    assert decision_witnesses == {
        "guess_correction_from_correction_quotient": 1.0,
        "guess_herald_from_correction_quotient": 0.5,
        "guess_atom_from_correction_quotient": 0.5,
        "guess_herald_from_raw": 1.0,
        "guess_atom_from_raw": 1.0,
    }

    representative_families = {
        "none": (),
        "bell_family_only": ("bell_family",),
        "correction_only": ("correction",),
        "correction_plus_redundant_family": ("correction", "bell_family"),
        "correction_plus_herald_audit": ("correction", "herald_audit"),
        "correction_plus_atom_audit": ("correction", "atom_audit"),
        "raw_identity": ("raw_identity",),
    }
    representatives = {
        label: {
            "tasks": list(names),
            "classes": len(kernel_partition(names)),
            "blocks": [[list(raw) for raw in block] for block in kernel_partition(names)],
        }
        for label, names in representative_families.items()
    }

    return {
        "claim_id": "HC-DU-202",
        "carrier_size": len(RAW),
        "all_partition_count": len(partitions),
        "task_family_subset_count": len(subset_results),
        "naturality_controls": {
            "bare_carrier_s8_invariant_partition_count": len(bare_invariant_partitions),
            "bare_carrier_invariant_class_counts": sorted(
                len(partition) for partition in bare_invariant_partitions
            ),
            "typed_herald_atom_swap_invariant_partition_count": len(
                typed_invariant_partitions
            ),
            "correction_quotient_is_swap_invariant": True,
        },
        "representative_minimal_quotients": representatives,
        "correction_sufficient_partition_count": len(correction_sufficient),
        "decision_witnesses": decision_witnesses,
        "all_task_subsets": subset_results,
        "prior_result_reproduced": {
            "finite_common_sufficiency": (
                "the kernel of the joint task signature is the unique coarsest "
                "deterministic quotient sufficient for that frozen task family; "
                "already banked as HC-DU-163"
            ),
            "monotonicity": (
                "enlarging a task/continuation family can only refine its minimal quotient; "
                "already banked as HC-DU-163"
            ),
        },
        "earned_here": {
            "bell_boundary": (
                "the correction family selects four classes; adding either independent "
                "audit bit restores all eight raw classes"
            ),
            "universal_decision_boundary": (
                "the correction quotient is sufficient for correction but strictly loses "
                "decision value for herald and atom audit tasks"
            ),
            "bare_carrier_naturality": (
                "full relabeling covariance admits only equality and the indiscrete "
                "partition; every nontrivial quotient needs additional typed structure"
            ),
        },
        "not_earned": [
            "physical selection of the task or continuation family",
            "a unique record quotient from the carrier alone",
            "experimental validation",
            "quantum ontology priority",
            "new physics or an empirical prediction",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
