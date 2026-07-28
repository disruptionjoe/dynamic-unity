#!/usr/bin/env python3
"""Exact finite certificate for HC-DU-073.

The analytic result lives in:
  explorations/causal-priority-intervention-ladder-and-process-transfer-2026-07-28.md

This probe is not a causal-discovery package, quantum simulation proposal,
physical model, ontology test, or hardware assay. It preserves the minimum
finite witnesses showing:

* passive endpoint equality does not orient a formation arrow;
* source and record interventions are jointly necessary to distinguish
  source->record, record->source, and common-cause copy models;
* diagonal interventions and repeated endpoint samples do not help;
* the same intervention pattern holds for two directional Bell-formation
  circuits and a common-source replacement channel; and
* authentication preserves a declared value without identifying its causal
  formation direction.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_causal_priority_intervention_result.json"
)
Q = Fraction


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
    if isinstance(value, complex):
        return [value.real, value.imag]
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


# ---------------------------------------------------------------------------
# Classical three-model formation fixture.
# ---------------------------------------------------------------------------

MODELS = ("source_to_record", "record_to_source", "common_cause")
INTERVENTIONS = ("passive", "do_source_0", "do_record_0", "do_both_0")


def classical_row(model: str, root: int, intervention: str) -> tuple[int, int]:
    if model == "source_to_record":
        source = root
        if intervention in ("do_source_0", "do_both_0"):
            source = 0
        record = source
        if intervention in ("do_record_0", "do_both_0"):
            record = 0
        return source, record

    if model == "record_to_source":
        record = root
        if intervention in ("do_record_0", "do_both_0"):
            record = 0
        source = record
        if intervention in ("do_source_0", "do_both_0"):
            source = 0
        return source, record

    if model == "common_cause":
        source = root
        record = root
        if intervention in ("do_source_0", "do_both_0"):
            source = 0
        if intervention in ("do_record_0", "do_both_0"):
            record = 0
        return source, record

    raise ValueError(model)


def law(
    values: Iterable[tuple[int, int]],
    readout: Callable[[tuple[int, int]], int | tuple[int, int]],
) -> dict[str, Fraction]:
    counts: dict[str, int] = {}
    values_tuple = tuple(values)
    for value in values_tuple:
        key = repr(readout(value))
        counts[key] = counts.get(key, 0) + 1
    return {
        key: Q(count, len(values_tuple))
        for key, count in sorted(counts.items())
    }


def response_signature(model: str, intervention: str) -> dict[str, Fraction]:
    rows = tuple(classical_row(model, root, intervention) for root in (0, 1))
    if intervention == "do_source_0":
        return law(rows, lambda row: row[1])
    if intervention == "do_record_0":
        return law(rows, lambda row: row[0])
    return law(rows, lambda row: row)


def induced_partition(actions: Sequence[str]) -> frozenset[frozenset[str]]:
    blocks: dict[str, set[str]] = {}
    for model in MODELS:
        signature = canonical_json(
            {
                action: jsonable(response_signature(model, action))
                for action in actions
            }
        )
        blocks.setdefault(signature, set()).add(model)
    return frozenset(frozenset(block) for block in blocks.values())


def tv_binary(left: dict[str, Fraction], right: dict[str, Fraction]) -> Fraction:
    keys = set(left) | set(right)
    return Q(1, 2) * sum(abs(left.get(k, Q(0)) - right.get(k, Q(0))) for k in keys)


def signed_certificate(value: int) -> tuple[str, int, int]:
    return ("valid", value, (17 * value + 5) % 19)


# ---------------------------------------------------------------------------
# Minimal two-qubit process control.
# ---------------------------------------------------------------------------

Vector = tuple[complex, ...]
Matrix = tuple[tuple[complex, ...], ...]
SQRT2 = math.sqrt(2.0)
ZERO: Vector = (1.0 + 0j, 0j)
PLUS: Vector = (1.0 / SQRT2 + 0j, 1.0 / SQRT2 + 0j)
Z: Matrix = ((1.0 + 0j, 0j), (0j, -1.0 + 0j))
I2: Matrix = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))
X: Matrix = ((0j, 1.0 + 0j), (1.0 + 0j, 0j))


def kron_vector(left: Vector, right: Vector) -> Vector:
    return tuple(a * b for a in left for b in right)


def kron_matrix(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[i // len(right)][j // len(right[0])]
            * right[i % len(right)][j % len(right[0])]
            for j in range(len(left[0]) * len(right[0]))
        )
        for i in range(len(left) * len(right))
    )


def apply(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    )


def inner(left: Vector, right: Vector) -> complex:
    return sum(a.conjugate() * b for a, b in zip(left, right, strict=True))


def density(vector: Vector) -> tuple[tuple[complex, ...], ...]:
    return tuple(
        tuple(a * b.conjugate() for b in vector)
        for a in vector
    )


def max_matrix_defect(
    left: Sequence[Sequence[complex]], right: Sequence[Sequence[complex]]
) -> float:
    return max(
        abs(a - b)
        for left_row, right_row in zip(left, right, strict=True)
        for a, b in zip(left_row, right_row, strict=True)
    )


def cnot(control: int) -> Matrix:
    # Qubit order is (source, record).
    out = [[0j for _ in range(4)] for _ in range(4)]
    for source, record in itertools.product((0, 1), repeat=2):
        in_index = 2 * source + record
        if control == 0:
            out_source, out_record = source, record ^ source
        else:
            out_source, out_record = source ^ record, record
        out[2 * out_source + out_record][in_index] = 1.0 + 0j
    return tuple(tuple(row) for row in out)


PHI_PLUS: Vector = (
    1.0 / SQRT2 + 0j,
    0j,
    0j,
    1.0 / SQRT2 + 0j,
)
XX = kron_matrix(X, X)
Z_SOURCE = kron_matrix(Z, I2)
Z_RECORD = kron_matrix(I2, Z)


def quantum_output(model: str, intervention: str) -> Vector:
    if model == "source_to_record":
        state = kron_vector(PLUS, ZERO)
        if intervention == "phase_source":
            state = apply(Z_SOURCE, state)
        if intervention == "phase_record":
            state = apply(Z_RECORD, state)
        return apply(cnot(0), state)

    if model == "record_to_source":
        state = kron_vector(ZERO, PLUS)
        if intervention == "phase_source":
            state = apply(Z_SOURCE, state)
        if intervention == "phase_record":
            state = apply(Z_RECORD, state)
        return apply(cnot(1), state)

    if model == "common_source":
        # A replacement channel supplied by an external common source. Local
        # input phases are discarded before the shared Bell pair is emitted.
        return PHI_PLUS

    raise ValueError(model)


def xx_expectation(vector: Vector) -> float:
    return float(inner(vector, apply(XX, vector)).real)


def main() -> int:
    passive_laws = {
        model: response_signature(model, "passive") for model in MODELS
    }
    check(
        "all three classical models have the same passive endpoint law",
        len({canonical_json(jsonable(value)) for value in passive_laws.values()})
        == 1,
        jsonable(passive_laws),
    )

    passive_partition = induced_partition(("passive",))
    diagonal_partition = induced_partition(("passive", "do_both_0"))
    source_partition = induced_partition(("passive", "do_source_0"))
    record_partition = induced_partition(("passive", "do_record_0"))
    full_partition = induced_partition(
        ("passive", "do_source_0", "do_record_0")
    )
    check(
        "passive and diagonal interventions do not orient formation",
        len(passive_partition) == 1 and len(diagonal_partition) == 1,
        {
            "passive": sorted(sorted(block) for block in passive_partition),
            "diagonal": sorted(sorted(block) for block in diagonal_partition),
        },
    )
    check(
        "one source intervention leaves one confounded pair",
        len(source_partition) == 2
        and frozenset(("record_to_source", "common_cause"))
        in source_partition,
        sorted(sorted(block) for block in source_partition),
    )
    check(
        "one record intervention leaves the other confounded pair",
        len(record_partition) == 2
        and frozenset(("source_to_record", "common_cause"))
        in record_partition,
        sorted(sorted(block) for block in record_partition),
    )
    check(
        "two arrow-breaking interventions distinguish all three models",
        full_partition == frozenset(frozenset((model,)) for model in MODELS),
        sorted(sorted(block) for block in full_partition),
    )

    do_source_pr = response_signature("source_to_record", "do_source_0")
    do_source_cc = response_signature("common_cause", "do_source_0")
    do_record_rp = response_signature("record_to_source", "do_record_0")
    do_record_cc = response_signature("common_cause", "do_record_0")
    check(
        "classical arrow-breaking margins are exactly one half",
        tv_binary(do_source_pr, do_source_cc) == Q(1, 2)
        and tv_binary(do_record_rp, do_record_cc) == Q(1, 2),
        {
            "source_intervention_margin": tv_binary(do_source_pr, do_source_cc),
            "record_intervention_margin": tv_binary(do_record_rp, do_record_cc),
        },
    )

    # Exhaust the declared action subsets to verify the minimum cover size.
    candidate_actions = ("do_source_0", "do_record_0", "do_both_0")
    separating_subsets = []
    for size in range(len(candidate_actions) + 1):
        for subset in itertools.combinations(candidate_actions, size):
            if len(induced_partition(("passive",) + subset)) == len(MODELS):
                separating_subsets.append(subset)
    check(
        "minimum classical orientation cover is the two arrow-breaking actions",
        min(map(len, separating_subsets)) == 2
        and ("do_source_0", "do_record_0") in separating_subsets,
        separating_subsets,
    )

    # Authentication is deterministic postprocessing of the record. It keeps
    # all passive endpoint laws equal and does not orient the causal graph.
    authenticated_laws = {}
    for model in MODELS:
        rows = tuple(classical_row(model, root, "passive") for root in (0, 1))
        authenticated_laws[model] = law(
            rows, lambda row: (row[0], signed_certificate(row[1]))
        )
    check(
        "authentication preserves value without revealing formation direction",
        len(
            {
                canonical_json(jsonable(value))
                for value in authenticated_laws.values()
            }
        )
        == 1,
        jsonable(authenticated_laws),
    )

    quantum_models = ("source_to_record", "record_to_source", "common_source")
    terminal_densities = {
        model: density(quantum_output(model, "passive"))
        for model in quantum_models
    }
    check(
        "opposite directional circuits and common source share one Bell endpoint",
        max(
            max_matrix_defect(terminal_densities[quantum_models[0]], value)
            for value in terminal_densities.values()
        )
        < 1e-12,
        "all terminal density matrices equal |Phi+><Phi+|",
    )

    quantum_signatures = {
        model: {
            intervention: round(
                xx_expectation(quantum_output(model, intervention)), 12
            )
            for intervention in ("phase_source", "phase_record")
        }
        for model in quantum_models
    }
    check(
        "source phase identifies source-to-record circuit only",
        quantum_signatures["source_to_record"]["phase_source"] == -1.0
        and quantum_signatures["record_to_source"]["phase_source"] == 1.0
        and quantum_signatures["common_source"]["phase_source"] == 1.0,
        quantum_signatures,
    )
    check(
        "record phase identifies record-to-source circuit only",
        quantum_signatures["record_to_source"]["phase_record"] == -1.0
        and quantum_signatures["source_to_record"]["phase_record"] == 1.0
        and quantum_signatures["common_source"]["phase_record"] == 1.0,
        quantum_signatures,
    )
    check(
        "two quantum arrow-breaking interventions distinguish all three processes",
        len(
            {
                (
                    signature["phase_source"],
                    signature["phase_record"],
                )
                for signature in quantum_signatures.values()
            }
        )
        == 3,
        quantum_signatures,
    )

    result = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-073",
        "result": (
            "TERMINAL_DUALITY_DOES_NOT_ORIENT_CAUSAL_PRIORITY"
            "_TWO_ARROW_BREAKING_INTERVENTIONS_MINIMAL"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(1 for item in checks if item["passed"]),
            "total": len(checks),
            "classical_minimum_interventions": 2,
            "classical_margin": Q(1, 2),
            "quantum_phase_margin": Q(1),
            "hardware_used": False,
            "physical_model_claimed": False,
        },
    }
    ARTIFACT.write_text(canonical_json(jsonable(result)), encoding="utf-8")
    print(canonical_json(jsonable(result)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
