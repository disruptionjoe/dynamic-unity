#!/usr/bin/env python3
"""Exact finite certificate for N5-CCR-BS-P3-KERNEL / HC-DU-059.

The scientific and formal statement lives in:
  explorations/presentation-invariant-operational-kernel-and-query-separation-2026-07-27.md

This probe is deliberately small.  It does not simulate physics.  It checks
the four-element counterexample showing that coordinate-wise minimality is
presentation-dependent, and it verifies the fibre criteria used in the
scoped theorem:

* a target factors through a signature exactly when it is constant on the
  signature's fibres;
* a named field is derivable from the other named fields exactly when their
  joint fibres refine that field's fibres;
* two individually independent coordinates can be bijectively repackaged as
  one informative coordinate plus one constant coordinate without changing
  the joint operational kernel; and
* adding a held-out target to the input bundle makes it redundant whenever
  the complete process signature already determines it.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Callable, Hashable, Sequence, TypeVar


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_kernel_minimality_result.json"

T = TypeVar("T")
CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def signature(
    item: T, fields: Sequence[Callable[[T], Hashable]]
) -> tuple[Hashable, ...]:
    return tuple(field(item) for field in fields)


def kernel(
    domain: Sequence[T], statistic: Callable[[T], Hashable]
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (left, right)
        for left in range(len(domain))
        for right in range(len(domain))
        if statistic(domain[left]) == statistic(domain[right])
    )


def factorizes(
    domain: Sequence[T],
    source: Callable[[T], Hashable],
    target: Callable[[T], Hashable],
) -> bool:
    decoder: dict[Hashable, Hashable] = {}
    for item in domain:
        source_value = source(item)
        target_value = target(item)
        if source_value in decoder and decoder[source_value] != target_value:
            return False
        decoder[source_value] = target_value
    return True


def partition(
    domain: Sequence[T], statistic: Callable[[T], Hashable]
) -> tuple[tuple[int, ...], ...]:
    blocks: dict[Hashable, list[int]] = {}
    for index, item in enumerate(domain):
        blocks.setdefault(statistic(item), []).append(index)
    return tuple(sorted(tuple(block) for block in blocks.values()))


def main() -> None:
    domain = tuple(product((0, 1), repeat=2))

    first = lambda item: item[0]
    second = lambda item: item[1]
    complete = lambda item: signature(item, (first, second))
    parity = lambda item: item[0] ^ item[1]

    record(
        "target_factorization_equals_kernel_inclusion_positive",
        factorizes(domain, complete, parity)
        and kernel(domain, complete).issubset(kernel(domain, parity)),
        "parity is constant on every complete-signature fibre",
    )
    record(
        "target_factorization_equals_kernel_inclusion_negative",
        not factorizes(domain, first, parity)
        and not kernel(domain, first).issubset(kernel(domain, parity)),
        "the first coordinate alone does not determine parity",
    )

    record(
        "first_field_independent_in_named_presentation",
        not factorizes(domain, second, first),
        "the second field does not derive the first",
    )
    record(
        "second_field_independent_in_named_presentation",
        not factorizes(domain, first, second),
        "the first field does not derive the second",
    )

    packed = lambda item: (item[0], item[1])
    dummy = lambda _item: 0
    packed_bundle = lambda item: signature(item, (packed, dummy))

    record(
        "bijective_repacking_preserves_joint_kernel",
        kernel(domain, complete) == kernel(domain, packed_bundle),
        {
            "original_partition": partition(domain, complete),
            "repacked_partition": partition(domain, packed_bundle),
        },
    )
    record(
        "repacking_makes_one_coordinate_redundant",
        factorizes(domain, packed, dummy),
        "the constant dummy field is derivable after lossless repacking",
    )

    mixed_first = lambda item: item[0]
    mixed_second = lambda item: item[0] ^ item[1]
    mixed_bundle = lambda item: signature(item, (mixed_first, mixed_second))
    record(
        "invertible_coordinate_mixing_preserves_joint_kernel",
        kernel(domain, complete) == kernel(domain, mixed_bundle),
        "the original and XOR-mixed bases preserve exactly the same distinctions",
    )
    record(
        "mixed_basis_retains_coordinate_independence",
        not factorizes(domain, mixed_first, mixed_second)
        and not factorizes(domain, mixed_second, mixed_first),
        "even an irredundant two-field basis is not a unique named basis",
    )

    process_with_target = lambda item: (item[0], item[1], parity(item))
    process_without_target = lambda item: (item[0], item[1])
    augmented_bundle = lambda item: (process_without_target(item), parity(item))
    record(
        "held_out_target_derived_from_complete_process",
        factorizes(domain, process_without_target, parity),
        "the target is a readout of the declared complete process",
    )
    record(
        "target_coordinate_adds_no_kernel_information",
        kernel(domain, process_without_target) == kernel(domain, augmented_bundle),
        "including a derived target in the physical bundle does not refine its fibres",
    )
    record(
        "complete_process_can_absorb_named_target",
        kernel(domain, process_with_target) == kernel(domain, process_without_target),
        "a complete process signature and the same signature with an explicit target agree",
    )

    target_quotient = parity
    record(
        "minimal_target_quotient_is_coarser_than_complete_presentation",
        kernel(domain, complete).issubset(kernel(domain, target_quotient))
        and kernel(domain, complete) != kernel(domain, target_quotient),
        {
            "complete_partition": partition(domain, complete),
            "target_partition": partition(domain, target_quotient),
        },
    )

    passed = sum(1 for check in CHECKS if check["passed"])
    result = {
        "claim_id": "HC-DU-059",
        "work_id": "N5-CCR-BS-P3-KERNEL",
        "domain_size": len(domain),
        "checks_passed": passed,
        "checks_total": len(CHECKS),
        "all_passed": passed == len(CHECKS),
        "returns": [
            "REDUNDANT_OR_DERIVABLE_FIELD",
            "CONTRACT_DEPENDENT_MINIMALITY",
            "ABSORBED_SCHEMA_ONLY",
            "OBSERVER_INDEX_DERIVABLE_FROM_ACCESS_ACTION",
        ],
        "checks": CHECKS,
    }
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
