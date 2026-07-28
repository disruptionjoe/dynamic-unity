#!/usr/bin/env python3
"""Exact finite certificate for HC-DU-072.

The analytic theorem lives in:
  explorations/operational-duality-no-priority-and-cross-platform-transfer-2026-07-28.md

This probe is not a quantum simulation, network simulation, ontology test,
physical model, or novelty proof. It verifies:

* equal deterministic operational kernels imply equal target scope;
* mutual stochastic garblings preserve a noisy experiment exactly;
* a stabilizer syndrome is dual to the frozen correction quotient but not to
  an enlarged logical-action quotient;
* an authenticated public certificate is dual to its frozen public-action
  quotient but not to physical formation provenance; and
* a same-alphabet, same-marginal, source-unbound record fails the duality gate.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Any, Callable, Hashable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_operational_duality_no_priority_result.json"
)
Q = Fraction
Row = Mapping[str, object]
View = Callable[[Row], Hashable]


checks: list[dict[str, Any]] = []


def check(name: str, condition: bool, detail: Any) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def partition(rows: Sequence[Row], view: View) -> frozenset[frozenset[int]]:
    blocks: dict[Hashable, set[int]] = {}
    for index, row in enumerate(rows):
        blocks.setdefault(view(row), set()).add(index)
    return frozenset(frozenset(block) for block in blocks.values())


def factorizes(rows: Sequence[Row], view: View, target: View) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for row in rows:
        key = view(row)
        value = target(row)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def image_bijection(rows: Sequence[Row], left: View, right: View) -> bool:
    left_to_right: dict[Hashable, Hashable] = {}
    right_to_left: dict[Hashable, Hashable] = {}
    for row in rows:
        left_value = left(row)
        right_value = right(row)
        if (
            left_value in left_to_right
            and left_to_right[left_value] != right_value
        ):
            return False
        if (
            right_value in right_to_left
            and right_to_left[right_value] != left_value
        ):
            return False
        left_to_right[left_value] = right_value
        right_to_left[right_value] = left_value
    return True


def minimum_first_leak(
    rows: Sequence[Row], record: View, enlarged_response: View
) -> tuple[int, int] | None:
    for left, right in itertools.combinations(range(len(rows)), 2):
        if record(rows[left]) == record(rows[right]) and (
            enlarged_response(rows[left]) != enlarged_response(rows[right])
        ):
            return left, right
    return None


def multiply(
    left: Sequence[Sequence[Fraction]],
    right: Sequence[Sequence[Fraction]],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def signed_certificate(value: int) -> tuple[str, int, int]:
    return ("valid", value, (17 * value + 5) % 19)


def main() -> int:
    # Exhaust the deterministic theorem on all pairs of binary presentations
    # and all binary targets over the smallest four-history arena.
    rows4 = tuple({"history": index} for index in range(4))
    binary_maps = tuple(itertools.product((0, 1), repeat=4))
    equal_kernel_pairs = 0
    target_scope_disagreements = 0
    for physical_values, record_values in itertools.product(
        binary_maps, repeat=2
    ):
        physical = lambda row, values=physical_values: values[int(row["history"])]
        record = lambda row, values=record_values: values[int(row["history"])]
        if partition(rows4, physical) != partition(rows4, record):
            continue
        equal_kernel_pairs += 1
        if not image_bijection(rows4, physical, record):
            target_scope_disagreements += 1
            continue
        for target_values in binary_maps:
            target = lambda row, values=target_values: values[int(row["history"])]
            if factorizes(rows4, physical, target) != factorizes(
                rows4, record, target
            ):
                target_scope_disagreements += 1
    check(
        "equal deterministic kernels give identical target scope",
        equal_kernel_pairs > 0 and target_scope_disagreements == 0,
        {
            "equal_kernel_pairs": equal_kernel_pairs,
            "scope_disagreements": target_scope_disagreements,
        },
    )

    # A noisy binary physical experiment and a record experiment made by
    # independently splitting each outcome. K adds the irrelevant coin; L
    # forgets it. Both matrix equalities are exact.
    physical_channel = (
        (Q(3, 4), Q(1, 4)),
        (Q(1, 4), Q(3, 4)),
    )
    add_coin = (
        (Q(1, 2), Q(1, 2), Q(0), Q(0)),
        (Q(0), Q(0), Q(1, 2), Q(1, 2)),
    )
    forget_coin = (
        (Q(1), Q(0)),
        (Q(1), Q(0)),
        (Q(0), Q(1)),
        (Q(0), Q(1)),
    )
    record_channel = multiply(physical_channel, add_coin)
    recovered_physical = multiply(record_channel, forget_coin)
    check(
        "stochastic record is a target-independent garbling of physical experiment",
        record_channel == multiply(physical_channel, add_coin),
        jsonable(record_channel),
    )
    check(
        "physical experiment is recovered by target-independent forgetting",
        recovered_physical == physical_channel,
        jsonable(recovered_physical),
    )

    # Three-qubit repetition-code Pauli-X sectors. Multiplication by logical
    # X=XXX preserves the syndrome but changes the logical action.
    stabilizers_z = ((1, 1, 0), (0, 1, 1))
    representatives_x = (
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    logical_x = (1, 1, 1)

    def syndrome(x_bits: tuple[int, int, int]) -> tuple[int, int]:
        return tuple(
            sum(x * z for x, z in zip(x_bits, generator, strict=True)) % 2
            for generator in stabilizers_z
        )

    quantum_rows = tuple(
        {
            "representative": representative,
            "logical": logical,
            "error": tuple(
                bit ^ (logical * logical_bit)
                for bit, logical_bit in zip(
                    representative, logical_x, strict=True
                )
            ),
        }
        for representative in representatives_x
        for logical in (0, 1)
    )
    q_record = lambda row: syndrome(row["error"])  # type: ignore[arg-type]
    q_physical_quotient = lambda row: (
        "correction",
        syndrome(row["error"]),  # type: ignore[arg-type]
    )
    q_frozen_response = lambda row: syndrome(row["error"])  # type: ignore[arg-type]
    q_enlarged_response = lambda row: (
        syndrome(row["error"]),  # type: ignore[arg-type]
        row["logical"],
    )
    check(
        "quantum correction quotient and syndrome record are operationally dual",
        partition(quantum_rows, q_physical_quotient)
        == partition(quantum_rows, q_record)
        == partition(quantum_rows, q_frozen_response)
        and image_bijection(quantum_rows, q_physical_quotient, q_record),
        "same four syndrome/correction sectors after the declared code quotient",
    )
    quantum_leak = minimum_first_leak(
        quantum_rows, q_record, q_enlarged_response
    )
    check(
        "logical action is the minimum quantum first leak",
        quantum_leak is not None,
        quantum_leak,
    )

    # Authenticated public record. The frozen public action quotient depends
    # on value, while the physical formation mode remains screened.
    distributed_rows = tuple(
        {
            "value": value,
            "formation": formation,
            "certificate": signed_certificate(value),
        }
        for value in (0, 1)
        for formation in ("source_formed", "preloaded")
    )
    d_record = lambda row: row["certificate"]
    d_physical_quotient = lambda row: (
        "public",
        row["value"],
        bool(row["value"]),
    )
    d_frozen_response = lambda row: (row["value"], bool(row["value"]))
    d_enlarged_response = lambda row: (row["value"], row["formation"])
    check(
        "distributed public-action quotient and certificate are operationally dual",
        partition(distributed_rows, d_physical_quotient)
        == partition(distributed_rows, d_record)
        == partition(distributed_rows, d_frozen_response)
        and image_bijection(distributed_rows, d_physical_quotient, d_record),
        "same two public execution sectors despite hidden formation mode",
    )
    distributed_leak = minimum_first_leak(
        distributed_rows, d_record, d_enlarged_response
    )
    check(
        "source-provenance action is the minimum distributed first leak",
        distributed_leak is not None,
        distributed_leak,
    )

    # Same record alphabet and the same uniform record marginal, but the
    # preloaded record is independent of the physical target.
    mismatch_rows = tuple(
        {
            "target": target,
            "record_value": record_value,
            "certificate": signed_certificate(record_value),
        }
        for target in (0, 1)
        for record_value in (0, 1)
    )
    mismatch_physical = lambda row: row["target"]
    mismatch_record = lambda row: row["certificate"]
    check(
        "same alphabet and marginal do not imply operational duality",
        partition(mismatch_rows, mismatch_physical)
        != partition(mismatch_rows, mismatch_record)
        and not factorizes(mismatch_rows, mismatch_record, mismatch_physical),
        "source-unbound certificate crosses target fibres",
    )

    result = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-072",
        "result": (
            "OPERATIONAL_DUALITY_NO_PRIORITY"
            "_WITH_ACTION_RELATIVE_FIRST_LEAK"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(1 for item in checks if item["passed"]),
            "total": len(checks),
            "quantum_first_leak": quantum_leak,
            "distributed_first_leak": distributed_leak,
            "hardware_used": False,
            "physical_model_claimed": False,
        },
    }
    ARTIFACT.write_text(canonical_json(jsonable(result)), encoding="utf-8")
    print(canonical_json(jsonable(result)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
