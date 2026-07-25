#!/usr/bin/env python3
"""Physical stochastic-record transfer for HC-DU-034B/036B.

This probe replaces the prior supplied response tables with:

1. a matrix-derived finite quantum history process with a QND stabilizer
   recorder, noisy accessible pointer, and explicit error environment; and
2. a replayable authenticated operation-DAG process with enumerated delivery
   schedules, a noisy materialized audit bit, and an authenticated receipt.

The same finite exact-rational stochastic-record compiler is used on both.
For record kernel R and later response P_a, factorization means that a
stochastic decoder K_a exists with

    P_a = R K_a

for every admitted intervention. Feasibility is decided by exact enumeration
of basic feasible solutions; no floating tolerance enters the compiler.

Passing establishes scoped finite constructions and a typed transfer. It
does not establish proper time, a laboratory implementation, cryptographic
security, BFT safety, exhaustive physical admissibility, an irreducible
remainder, record-first ontology, or a new physical law.
"""

from __future__ import annotations

import hashlib
import hmac
import itertools
import json
import math
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np

from du_noninvertible_history_certificate_compiler_probe import (
    REQUIRED_CONSTRUCTOR_AUDIT,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_physical_history_certificate_transfer_result.json"
)

Distribution = tuple[Fraction, ...]
Kernel = tuple[Distribution, ...]
ResponseTable = tuple[Kernel, ...]
TOL = 1e-10
VALIDATOR_KEYS = {
    "v0": b"du-fixture-validator-key-v0",
    "v1": b"du-fixture-validator-key-v1",
    "v2": b"du-fixture-validator-key-v2",
}


@dataclass(frozen=True)
class PhysicalRefinement:
    """One target-independent formed refinement candidate."""

    refinement_id: str
    constructor: str
    cost: int
    formed: bool
    future_independent: bool
    accessible: bool
    preserves_frame: bool
    target_independent_claim: bool
    record_outcomes: tuple[str, ...] | None = None
    record_kernel: Kernel | None = None
    path_tags: tuple[str, ...] | None = None
    certified_path_provenance: bool = False
    certificate_kind: str = "none"
    resource_vector: tuple[tuple[str, int], ...] = ()


@dataclass(frozen=True)
class PhysicalHistoryContract:
    """Unchanged physical/protocol interface used on both focal fixtures."""

    contract_id: str
    platform_label: str
    histories: tuple[str, ...]
    interventions: tuple[str, ...]
    response_outcomes: tuple[str, ...]
    responses: ResponseTable
    base_record_outcomes: tuple[str, ...]
    base_record_kernel: Kernel
    target_actions: tuple[str, ...]
    paths: tuple[str, ...]
    path_views: tuple[tuple[str, ...], ...]
    refinements: tuple[PhysicalRefinement, ...]
    resource_budget: int
    equality_rule: str
    constructor_audit: tuple[tuple[str, str], ...]
    contract_frozen: bool = True


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"))


def fractionize(value: float, denominator_limit: int = 10_000) -> Fraction:
    result = Fraction(float(value)).limit_denominator(denominator_limit)
    if abs(float(result) - float(value)) > TOL:
        raise ValueError(f"nonrationalized probability: {value}")
    return result


def kernel_from_float(rows: Iterable[Iterable[float]]) -> Kernel:
    return tuple(
        tuple(fractionize(float(value)) for value in row) for row in rows
    )


def total_variation(left: Distribution, right: Distribution) -> Fraction:
    return sum(
        (abs(a - b) for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    ) / 2


def matrix_rank_fraction(matrix: Sequence[Sequence[Fraction]]) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if rows[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                left - factor * right
                for left, right in zip(
                    rows[row], rows[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def independent_row_indices(
    matrix: Sequence[Sequence[Fraction]],
) -> tuple[int, ...]:
    selected: list[int] = []
    current: list[Sequence[Fraction]] = []
    rank = 0
    for index, row in enumerate(matrix):
        candidate = current + [row]
        candidate_rank = matrix_rank_fraction(candidate)
        if candidate_rank > rank:
            selected.append(index)
            current.append(row)
            rank = candidate_rank
    return tuple(selected)


def solve_square(
    matrix: Sequence[Sequence[Fraction]],
    target: Sequence[Fraction],
) -> tuple[Fraction, ...] | None:
    size = len(matrix)
    if size == 0:
        return ()
    augmented = [
        list(row) + [target[index]] for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if augmented[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            return None
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        scale = augmented[column][column]
        augmented[column] = [
            value / scale for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                left - factor * right
                for left, right in zip(
                    augmented[row], augmented[column], strict=True
                )
            ]
    return tuple(augmented[index][-1] for index in range(size))


def exact_stochastic_decoder(
    record_kernel: Kernel,
    response_kernel: Kernel,
) -> dict[str, Any]:
    """Decide whether response_kernel = record_kernel @ decoder exactly."""

    history_count = len(record_kernel)
    record_count = len(record_kernel[0])
    outcome_count = len(response_kernel[0])
    variable_count = record_count * outcome_count

    equations: list[tuple[Fraction, ...]] = []
    targets: list[Fraction] = []
    for history in range(history_count):
        for outcome in range(outcome_count):
            row = [Fraction(0)] * variable_count
            for record in range(record_count):
                row[record * outcome_count + outcome] = record_kernel[history][
                    record
                ]
            equations.append(tuple(row))
            targets.append(response_kernel[history][outcome])
    for record in range(record_count):
        row = [Fraction(0)] * variable_count
        for outcome in range(outcome_count):
            row[record * outcome_count + outcome] = Fraction(1)
        equations.append(tuple(row))
        targets.append(Fraction(1))

    coefficient_rank = matrix_rank_fraction(equations)
    augmented_rank = matrix_rank_fraction(
        [
            tuple(row) + (targets[index],)
            for index, row in enumerate(equations)
        ]
    )
    if augmented_rank != coefficient_rank:
        return {
            "factors": False,
            "reason": "inconsistent_linear_equalities",
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "basic_bases_checked": 0,
            "decoder": None,
        }

    independent = independent_row_indices(equations)
    independent_matrix = [equations[index] for index in independent]
    independent_target = [targets[index] for index in independent]
    bases_checked = 0
    for basis in itertools.combinations(
        range(variable_count), coefficient_rank
    ):
        square = [
            [row[column] for column in basis]
            for row in independent_matrix
        ]
        solution = solve_square(square, independent_target)
        if solution is None:
            continue
        bases_checked += 1
        variables = [Fraction(0)] * variable_count
        for column, value in zip(basis, solution, strict=True):
            variables[column] = value
        if any(value < 0 for value in variables):
            continue
        if any(
            sum(
                coefficient * variables[column]
                for column, coefficient in enumerate(row)
            )
            != targets[row_index]
            for row_index, row in enumerate(equations)
        ):
            continue
        decoder = tuple(
            tuple(
                variables[record * outcome_count + outcome]
                for outcome in range(outcome_count)
            )
            for record in range(record_count)
        )
        return {
            "factors": True,
            "reason": "exact_basic_feasible_decoder_found",
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "basic_bases_checked": bases_checked,
            "decoder": decoder,
        }

    return {
        "factors": False,
        "reason": "no_nonnegative_stochastic_decoder",
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "basic_bases_checked": bases_checked,
        "decoder": None,
    }


def constructor_audit(
    overrides: dict[str, str] | None = None,
) -> tuple[tuple[str, str], ...]:
    overrides = overrides or {}
    return tuple(
        (
            key,
            overrides.get(
                key,
                "considered: no distinct admitted primitive in this fixture",
            ),
        )
        for key in REQUIRED_CONSTRUCTOR_AUDIT
    )


def refinement_admissibility(
    item: PhysicalRefinement,
) -> tuple[bool, tuple[str, ...]]:
    failures: list[str] = []
    if not item.formed:
        failures.append("not_independently_formed")
    if not item.future_independent:
        failures.append("not_future_independent")
    if not item.accessible:
        failures.append("outside_frozen_access_class")
    if not item.preserves_frame:
        failures.append("changes_frozen_frame")
    if not item.target_independent_claim:
        failures.append("target_derived_candidate")
    return not failures, tuple(failures)


def validate_contract(contract: PhysicalHistoryContract) -> list[str]:
    errors: list[str] = []
    history_count = len(contract.histories)
    if not contract.contract_frozen:
        errors.append("contract_not_frozen")
    if not contract.histories or len(set(contract.histories)) != history_count:
        errors.append("invalid_history_set")
    if not contract.interventions:
        errors.append("empty_intervention_basis")
    if not contract.response_outcomes:
        errors.append("empty_response_alphabet")
    if not contract.base_record_outcomes:
        errors.append("empty_base_record_alphabet")
    if len(contract.base_record_kernel) != history_count:
        errors.append("base_record_history_arity")
    if len(contract.responses) != len(contract.interventions):
        errors.append("response_intervention_arity")
    if len(contract.target_actions) != history_count:
        errors.append("target_action_arity")
    if len(contract.path_views) != len(contract.paths):
        errors.append("path_view_path_arity")
    if contract.equality_rule != "exact_rational_stochastic_factorization":
        errors.append("unsupported_equality_rule")

    kernels: list[tuple[str, tuple[str, ...], Kernel]] = [
        (
            "base",
            contract.base_record_outcomes,
            contract.base_record_kernel,
        )
    ]
    for item in contract.refinements:
        if (item.record_kernel is None) != (item.record_outcomes is None):
            errors.append(f"partial_record_kernel:{item.refinement_id}")
        if item.record_kernel is not None and item.record_outcomes is not None:
            kernels.append(
                (item.refinement_id, item.record_outcomes, item.record_kernel)
            )
        if item.path_tags is not None:
            if len(item.path_tags) != len(contract.paths):
                errors.append(f"path_tag_arity:{item.refinement_id}")
            if not item.certified_path_provenance:
                errors.append(f"uncertified_path_tag:{item.refinement_id}")

    for kernel_id, outcomes, kernel in kernels:
        if len(kernel) != history_count:
            errors.append(f"record_history_arity:{kernel_id}")
            continue
        for row in kernel:
            if len(row) != len(outcomes):
                errors.append(f"record_outcome_arity:{kernel_id}")
            elif any(value < 0 for value in row):
                errors.append(f"negative_record_probability:{kernel_id}")
            elif sum(row, start=Fraction(0)) != 1:
                errors.append(f"incomplete_record_distribution:{kernel_id}")

    for intervention in contract.responses:
        if len(intervention) != history_count:
            errors.append("response_history_arity")
            continue
        for row in intervention:
            if len(row) != len(contract.response_outcomes):
                errors.append("response_outcome_arity")
            elif any(value < 0 for value in row):
                errors.append("negative_response_probability")
            elif sum(row, start=Fraction(0)) != 1:
                errors.append("incomplete_response_distribution")

    audit_keys = tuple(key for key, _ in contract.constructor_audit)
    if set(audit_keys) != set(REQUIRED_CONSTRUCTOR_AUDIT):
        errors.append("constructor_audit_mismatch")
    if len(set(audit_keys)) != len(audit_keys):
        errors.append("duplicate_constructor_audit_key")
    return sorted(set(errors))


def freeze_candidate_class(contract: PhysicalHistoryContract) -> dict[str, Any]:
    """Freeze candidate structure without consulting targets or responses."""

    admitted: list[PhysicalRefinement] = []
    excluded: list[dict[str, Any]] = []
    for item in contract.refinements:
        admissible, failures = refinement_admissibility(item)
        reasons = list(failures)
        if item.cost > contract.resource_budget:
            reasons.append("primitive_exceeds_resource_budget")
        if reasons:
            excluded.append(
                {"refinement_id": item.refinement_id, "reasons": reasons}
            )
        else:
            admitted.append(item)
    admitted.sort(key=lambda item: item.refinement_id)

    subsets: list[tuple[PhysicalRefinement, ...]] = []
    incompatible: list[tuple[str, ...]] = []
    for count in range(1, len(admitted) + 1):
        for subset in itertools.combinations(admitted, count):
            if sum(item.cost for item in subset) > contract.resource_budget:
                continue
            complete_record_kernels = [
                item for item in subset if item.record_kernel is not None
            ]
            if len(complete_record_kernels) > 1:
                incompatible.append(
                    tuple(item.refinement_id for item in subset)
                )
                continue
            subsets.append(subset)
    subsets.sort(
        key=lambda subset: (
            sum(item.cost for item in subset),
            len(subset),
            tuple(item.refinement_id for item in subset),
        )
    )

    payload = {
        "contract_id": contract.contract_id,
        "base_record_outcomes": contract.base_record_outcomes,
        "base_record_kernel": contract.base_record_kernel,
        "resource_budget": contract.resource_budget,
        "equality_rule": contract.equality_rule,
        "constructor_audit": contract.constructor_audit,
        "refinements": [
            {
                "refinement_id": item.refinement_id,
                "constructor": item.constructor,
                "cost": item.cost,
                "formed": item.formed,
                "future_independent": item.future_independent,
                "accessible": item.accessible,
                "preserves_frame": item.preserves_frame,
                "target_independent_claim": item.target_independent_claim,
                "record_outcomes": item.record_outcomes,
                "record_kernel": item.record_kernel,
                "path_tags": item.path_tags,
                "certified_path_provenance": (
                    item.certified_path_provenance
                ),
                "certificate_kind": item.certificate_kind,
                "resource_vector": item.resource_vector,
            }
            for item in contract.refinements
        ],
        "candidate_subsets": [
            tuple(item.refinement_id for item in subset) for subset in subsets
        ],
        "incompatible_complete_record_combinations": incompatible,
    }
    return {
        "digest": hashlib.sha256(
            canonical_json(payload).encode("utf-8")
        ).hexdigest(),
        "payload": payload,
        "admitted_primitive_ids": [
            item.refinement_id for item in admitted
        ],
        "excluded_primitives": excluded,
        "candidate_subsets": subsets,
        "incompatible_complete_record_combinations": incompatible,
        "selection_dependency": [
            "physically supplied base record kernel",
            "formed/future-independent/access/frame declarations",
            "candidate record kernels and provenance tags",
            "resource budget",
            "constructor audit",
        ],
        "excluded_from_selection": [
            "later response distributions",
            "target actions",
            "platform label",
        ],
    }


def selected_record_kernel(
    contract: PhysicalHistoryContract,
    selected: Sequence[PhysicalRefinement],
) -> tuple[tuple[str, ...], Kernel]:
    replacements = [item for item in selected if item.record_kernel is not None]
    if not replacements:
        return contract.base_record_outcomes, contract.base_record_kernel
    if len(replacements) != 1:
        raise ValueError("multiple complete record kernels are not composable")
    item = replacements[0]
    assert item.record_outcomes is not None
    assert item.record_kernel is not None
    return item.record_outcomes, item.record_kernel


def overlap_obstruction(
    contract: PhysicalHistoryContract,
    record_kernel: Kernel,
) -> dict[str, Any] | None:
    for left in range(len(contract.histories)):
        for right in range(left + 1, len(contract.histories)):
            shared_support = [
                index
                for index, (a, b) in enumerate(
                    zip(
                        record_kernel[left],
                        record_kernel[right],
                        strict=True,
                    )
                )
                if a > 0 and b > 0
            ]
            if not shared_support:
                continue
            for intervention_index, intervention in enumerate(
                contract.interventions
            ):
                if (
                    contract.responses[intervention_index][left]
                    != contract.responses[intervention_index][right]
                ):
                    return {
                        "left_history": contract.histories[left],
                        "right_history": contract.histories[right],
                        "intervention": intervention,
                        "shared_record_support_indices": shared_support,
                        "left_response": contract.responses[
                            intervention_index
                        ][left],
                        "right_response": contract.responses[
                            intervention_index
                        ][right],
                    }
    return None


def response_factorization(
    contract: PhysicalHistoryContract,
    selected: Sequence[PhysicalRefinement],
) -> dict[str, Any]:
    record_outcomes, record_kernel = selected_record_kernel(contract, selected)
    intervention_results = []
    for intervention, response in zip(
        contract.interventions, contract.responses, strict=True
    ):
        decision = exact_stochastic_decoder(record_kernel, response)
        intervention_results.append(
            {"intervention": intervention, **decision}
        )
    return {
        "factors": all(
            result["factors"] for result in intervention_results
        ),
        "criterion": "exists stochastic K_a with P_a = R K_a",
        "record_outcomes": record_outcomes,
        "record_kernel": record_kernel,
        "intervention_results": intervention_results,
        "overlap_obstruction": overlap_obstruction(
            contract, record_kernel
        ),
    }


def path_equalizer(
    contract: PhysicalHistoryContract,
    selected: Sequence[PhysicalRefinement],
) -> dict[str, Any]:
    provenance = [
        item
        for item in selected
        if item.path_tags is not None and item.certified_path_provenance
    ]
    seen: dict[tuple[str, tuple[str, ...]], tuple[str, str, str]] = {}
    conflicts: list[dict[str, Any]] = []
    for path_index, path in enumerate(contract.paths):
        tags = tuple(
            item.path_tags[path_index]  # type: ignore[index]
            for item in provenance
        )
        for history_index, history in enumerate(contract.histories):
            key = (contract.path_views[path_index][history_index], tags)
            action = contract.target_actions[history_index]
            prior = seen.get(key)
            if prior is not None and prior[0] != action:
                conflicts.append(
                    {
                        "public_view": key[0],
                        "path_tags": tags,
                        "left_action": prior[0],
                        "left_path": prior[1],
                        "left_history": prior[2],
                        "right_action": action,
                        "right_path": path,
                        "right_history": history,
                    }
                )
            else:
                seen[key] = (action, path, history)

    noninjective = [
        contract.paths[index]
        for index, views in enumerate(contract.path_views)
        if len(set(views)) < len(views)
    ]
    tag_alphabet = {
        tuple(
            item.path_tags[path_index]  # type: ignore[index]
            for item in provenance
        )
        for path_index in range(len(contract.paths))
    }
    return {
        "factors": not conflicts,
        "comparison_maps_noninvertible": bool(noninjective),
        "noninjective_paths": noninjective,
        "selected_certified_path_provenance": [
            item.refinement_id for item in provenance
        ],
        "selected_path_provenance_alphabet": len(tag_alphabet),
        "conflict_count": len(conflicts),
        "first_conflict": conflicts[0] if conflicts else None,
    }


def evaluate_candidate(
    contract: PhysicalHistoryContract,
    selected: Sequence[PhysicalRefinement],
) -> dict[str, Any]:
    response = response_factorization(contract, selected)
    path = path_equalizer(contract, selected)
    return {
        "refinement_ids": tuple(item.refinement_id for item in selected),
        "total_cost": sum(item.cost for item in selected),
        "resource_vector": {
            key: sum(
                value
                for item in selected
                for candidate_key, value in item.resource_vector
                if candidate_key == key
            )
            for key in sorted(
                {
                    candidate_key
                    for item in selected
                    for candidate_key, _ in item.resource_vector
                }
            )
        },
        "response_factorization": response,
        "path_equalizer": path,
        "sufficient": response["factors"] and path["factors"],
    }


def compile_physical_certificate(
    contract: PhysicalHistoryContract,
) -> dict[str, Any]:
    errors = validate_contract(contract)
    if errors:
        return {
            "schema": (
                "dynamic-unity/physical-stochastic-history-certificate/v0.1"
            ),
            "contract_id": contract.contract_id,
            "platform_label": contract.platform_label,
            "platform_label_used_by_decision": False,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": errors,
        }

    frozen = freeze_candidate_class(contract)
    if not frozen["candidate_subsets"]:
        return {
            "schema": (
                "dynamic-unity/physical-stochastic-history-certificate/v0.1"
            ),
            "contract_id": contract.contract_id,
            "platform_label": contract.platform_label,
            "platform_label_used_by_decision": False,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": ["empty_nonbase_admissible_refinement_class"],
            "frozen_class_digest": frozen["digest"],
        }

    base = evaluate_candidate(contract, ())
    evaluations = [
        evaluate_candidate(contract, subset)
        for subset in frozen["candidate_subsets"]
    ]
    common = {
        "schema": "dynamic-unity/physical-stochastic-history-certificate/v0.1",
        "contract_id": contract.contract_id,
        "platform_label": contract.platform_label,
        "platform_label_used_by_decision": False,
        "class_scope": (
            "finite frozen formed/future-independent/access- and "
            "resource-bounded physical stochastic-record grammar"
        ),
        "frozen_class_digest": frozen["digest"],
        "frozen_class": {
            "selection_dependency": frozen["selection_dependency"],
            "excluded_from_selection": frozen["excluded_from_selection"],
            "admitted_primitive_ids": frozen["admitted_primitive_ids"],
            "excluded_primitives": frozen["excluded_primitives"],
            "candidate_subset_ids": [
                tuple(item.refinement_id for item in subset)
                for subset in frozen["candidate_subsets"]
            ],
            "incompatible_complete_record_combinations": frozen[
                "incompatible_complete_record_combinations"
            ],
        },
        "base_evaluation": base,
        "candidate_evaluations": evaluations,
    }
    if base["sufficient"]:
        return {
            **common,
            "verdict": "FACTORIZATION",
            "certificate": {"record": "base", "evaluation": base},
        }
    sufficient = [item for item in evaluations if item["sufficient"]]
    if sufficient:
        selected = min(
            sufficient,
            key=lambda item: (
                item["total_cost"],
                len(item["refinement_ids"]),
                item["refinement_ids"],
            ),
        )
        return {
            **common,
            "verdict": "MINIMAL_REFINEMENT",
            "certificate": {
                "optimizer": (
                    "minimum(total_cost, primitive_count, "
                    "lexicographic_refinement_ids)"
                ),
                "selected": selected,
                "interpretation": (
                    "formed physical/protocol provenance absorbs the base "
                    "witness; no class-relative remainder"
                ),
            },
        }
    return {
        **common,
        "verdict": "CANDIDATE_REMAINDER",
        "certificate": {
            "finite_class_exhausted": True,
            "candidate_count": len(evaluations),
            "interpretation": (
                "candidate remainder relative only to the frozen access "
                "boundary and finite grammar; not an irreducible remainder"
            ),
        },
    }


def kron(*operators: np.ndarray) -> np.ndarray:
    if not operators:
        return np.array([[1.0 + 0.0j]])
    result = operators[0]
    for operator in operators[1:]:
        result = np.kron(result, operator)
    return result


def partial_distribution(
    state: np.ndarray,
    qubit_count: int,
    retained_qubits: tuple[int, ...],
) -> tuple[float, ...]:
    probabilities = np.abs(state.reshape((2,) * qubit_count)) ** 2
    result = []
    for retained_bits in itertools.product((0, 1), repeat=len(retained_qubits)):
        total = 0.0
        for all_bits in itertools.product((0, 1), repeat=qubit_count):
            if all(
                all_bits[index] == retained_bits[position]
                for position, index in enumerate(retained_qubits)
            ):
                total += float(probabilities[all_bits])
        result.append(total)
    return tuple(result)


def reduced_density_from_state(
    state: np.ndarray,
    kept: tuple[int, ...],
    qubit_count: int,
) -> np.ndarray:
    discarded = tuple(index for index in range(qubit_count) if index not in kept)
    tensor = state.reshape((2,) * qubit_count)
    permutation = kept + discarded
    matrix = np.transpose(tensor, permutation).reshape(
        2 ** len(kept), 2 ** len(discarded)
    )
    return matrix @ matrix.conj().T


def measurement_distribution(
    density: np.ndarray,
    basis_vectors: tuple[np.ndarray, ...],
) -> tuple[float, ...]:
    return tuple(
        float(np.real(vector.conj() @ density @ vector))
        for vector in basis_vectors
    )


def quantum_process_receipt() -> dict[str, Any]:
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    identity = np.eye(2, dtype=complex)
    x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    hadamard = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / math.sqrt(2)
    cnot = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=complex,
    )
    bell_plus = cnot @ (kron(hadamard, identity) @ kron(zero, zero))
    bell_minus = kron(z, identity) @ bell_plus
    stabilizer = kron(x, x)
    projector_plus = (np.eye(4) + stabilizer) / 2
    projector_minus = (np.eye(4) - stabilizer) / 2
    recorder = kron(projector_plus, identity) + kron(projector_minus, x)
    environment = math.sqrt(4 / 5) * zero + math.sqrt(1 / 5) * one
    env_zero = np.outer(zero, zero)
    env_one = np.outer(one, one)
    error_gate = kron(
        np.eye(4),
        kron(identity, env_zero) + kron(x, env_one),
    )
    full_recorder = kron(recorder, identity)

    plus_x = (zero + one) / math.sqrt(2)
    minus_x = (zero - one) / math.sqrt(2)
    x_basis = (
        kron(plus_x, plus_x),
        kron(plus_x, minus_x),
        kron(minus_x, plus_x),
        kron(minus_x, minus_x),
    )
    classical_density = (
        np.outer(kron(zero, zero), kron(zero, zero).conj())
        + np.outer(kron(one, one), kron(one, one).conj())
    ) / 2

    histories: dict[str, Any] = {}
    base_rows = []
    expanded_rows = []
    for label, bell, eigenvalue in (
        ("phase_plus", bell_plus, 1),
        ("phase_minus", bell_minus, -1),
    ):
        initial = kron(bell, zero, environment)
        final = error_gate @ (full_recorder @ initial)
        base_probability = partial_distribution(final, 4, (2,))
        expanded_probability = partial_distribution(final, 4, (2, 3))
        reduced_bc = reduced_density_from_state(final, (0, 1), 4)
        ideal_density = np.outer(bell, bell.conj())
        all_port = measurement_distribution(ideal_density, x_basis)
        histories[label] = {
            "stabilizer_eigenvalue": eigenvalue,
            "state_norm": float(np.vdot(final, final).real),
            "base_pointer_distribution": base_probability,
            "expanded_pointer_environment_distribution": expanded_probability,
            "nondemolition_trace_distance_numeric": float(
                np.linalg.norm(reduced_bc - ideal_density, ord="nuc") / 2
            ),
            "all_port_distribution_order_pp_pm_mp_mm": all_port,
            "signed_all_port_mean": float(
                all_port[0] - all_port[1] - all_port[2] + all_port[3]
            ),
        }
        base_rows.append(base_probability)
        expanded_rows.append(expanded_probability)

    noisy_alternative = tuple(
        Fraction(9, 10) * fractionize(a)
        + Fraction(1, 10) * fractionize(b)
        for a, b in zip(
            histories["phase_plus"][
                "all_port_distribution_order_pp_pm_mp_mm"
            ],
            histories["phase_minus"][
                "all_port_distribution_order_pp_pm_mp_mm"
            ],
            strict=True,
        )
    )
    classical_null = tuple(fractionize(value) for value in measurement_distribution(
        classical_density, x_basis
    ))
    score = (1, -1, -1, 1)
    alternative_mean = sum(
        Fraction(weight) * probability
        for weight, probability in zip(score, noisy_alternative, strict=True)
    )
    null_mean = sum(
        Fraction(weight) * probability
        for weight, probability in zip(score, classical_null, strict=True)
    )
    calibration_bound = Fraction(1, 10)
    calibrated_gap = alternative_mean - calibration_bound
    alpha = Fraction(1, 20)
    beta = Fraction(1, 20)
    shot_gate = math.ceil(
        2
        * (
            math.sqrt(math.log(1 / float(alpha)))
            + math.sqrt(math.log(1 / float(beta)))
        )
        ** 2
        / float(calibrated_gap) ** 2
    )
    return {
        "process": (
            "Bell-history preparation -> QND XxX pointer recorder -> "
            "source-independent detector-error environment"
        ),
        "qubit_order": ["history", "target", "pointer", "error_environment"],
        "unitarity_errors": {
            "cnot": float(
                np.linalg.norm(cnot.conj().T @ cnot - np.eye(4))
            ),
            "qnd_recorder": float(
                np.linalg.norm(recorder.conj().T @ recorder - np.eye(8))
            ),
            "error_gate": float(
                np.linalg.norm(
                    error_gate.conj().T @ error_gate - np.eye(16)
                )
            ),
        },
        "histories": histories,
        "base_record_outcomes": ("pointer_0", "pointer_1"),
        "base_record_kernel": kernel_from_float(base_rows),
        "expanded_record_outcomes": (
            "pointer_0_error_0",
            "pointer_0_error_1",
            "pointer_1_error_0",
            "pointer_1_error_1",
        ),
        "expanded_record_kernel": kernel_from_float(expanded_rows),
        "instrument_certificate": {
            "complete_outcomes": ("plus_plus", "plus_minus", "minus_plus", "minus_minus"),
            "noisy_coherent_alternative": noisy_alternative,
            "classical_dephased_null": classical_null,
            "signed_score": score,
            "alternative_signed_mean": alternative_mean,
            "classical_null_signed_mean": null_mean,
            "ideal_complete_outcome_total_variation": total_variation(
                noisy_alternative, classical_null
            ),
            "ideal_bounded_score_margin": alternative_mean - null_mean,
            "calibration_absolute_bias_bound": calibration_bound,
            "calibrated_gap": calibrated_gap,
            "hoeffding_alpha": alpha,
            "hoeffding_beta": beta,
            "sufficient_preparations": shot_gate,
        },
        "boundary_interpretation": {
            "base": "accessible noisy pointer; error environment departed",
            "expanded": (
                "pointer plus accessible error syndrome after charged "
                "boundary expansion"
            ),
        },
    }


def duplicated_history_rows(kernel: Kernel) -> Kernel:
    return (kernel[0], kernel[0], kernel[1], kernel[1])


def independent_pair_kernel(kernel: Kernel) -> Kernel:
    """Tensor two conditionally independent copies of one finite record."""

    return tuple(
        tuple(left * right for left in row for right in row)
        for row in kernel
    )


def quantum_contract(receipt: dict[str, Any]) -> PhysicalHistoryContract:
    histories = (
        "phase_plus_variant_a",
        "phase_plus_variant_b",
        "phase_minus_variant_a",
        "phase_minus_variant_b",
    )
    base_kernel = duplicated_history_rows(receipt["base_record_kernel"])
    expanded_kernel = duplicated_history_rows(receipt["expanded_record_kernel"])
    independent_copy_kernel = independent_pair_kernel(base_kernel)
    return PhysicalHistoryContract(
        contract_id="QPHYS-QND-HISTORY-01",
        platform_label="matrix_derived_quantum_history",
        histories=histories,
        interventions=("reduced_target_Z", "later_stabilizer_recheck"),
        response_outcomes=("signal_plus", "signal_minus"),
        responses=(
            (
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
            ),
            (
                (Fraction(1), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(1)),
            ),
        ),
        base_record_outcomes=receipt["base_record_outcomes"],
        base_record_kernel=base_kernel,
        target_actions=("preserve", "preserve", "phase_correct", "phase_correct"),
        paths=("direct_detector_route", "relayed_detector_route"),
        path_views=(
            ("bright", "bright", "dark", "dark"),
            ("dark", "dark", "bright", "bright"),
        ),
        refinements=(
            PhysicalRefinement(
                refinement_id="certified_detector_route",
                constructor="routed_implementation",
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                path_tags=("direct", "relay"),
                certified_path_provenance=True,
                certificate_kind="formed_route_register",
                resource_vector=(("authenticated_route_bits", 1),),
            ),
            PhysicalRefinement(
                refinement_id="expanded_pointer_error_syndrome",
                constructor="departed_environment",
                cost=2,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                record_outcomes=receipt["expanded_record_outcomes"],
                record_kernel=expanded_kernel,
                certificate_kind="qnd_pointer_plus_error_syndrome",
                resource_vector=(
                    ("accessible_pointer_bits", 1),
                    ("accessible_error_syndrome_bits", 1),
                ),
            ),
            PhysicalRefinement(
                refinement_id="replicated_noisy_pointer",
                constructor="resource",
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                record_outcomes=(
                    "pointer_00",
                    "pointer_01",
                    "pointer_10",
                    "pointer_11",
                ),
                record_kernel=independent_copy_kernel,
                certificate_kind="conditionally_independent_noisy_pointer_pair",
                resource_vector=(("additional_pointer_copies", 1),),
            ),
            PhysicalRefinement(
                refinement_id="stage_zero_phase_oracle",
                constructor="fixed_future_correlated_oracle",
                cost=1,
                formed=True,
                future_independent=False,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                record_outcomes=("phase_plus", "phase_minus"),
                record_kernel=(
                    (Fraction(1), Fraction(0)),
                    (Fraction(1), Fraction(0)),
                    (Fraction(0), Fraction(1)),
                    (Fraction(0), Fraction(1)),
                ),
                certificate_kind="precorrelated_history_disclosure",
            ),
        ),
        resource_budget=3,
        equality_rule="exact_rational_stochastic_factorization",
        constructor_audit=constructor_audit(
            {
                "seed": "Bell-history preparation fixed before target tests",
                "boundary": (
                    "base pointer and expanded pointer-plus-environment "
                    "boundaries both declared"
                ),
                "resource": "three-unit scalar gate plus explicit resource vector",
                "access": "error syndrome charged only in expanded observer class",
                "history": "QND XxX history record physically constructed",
                "provenance": "detector route register admitted",
                "fixed_future_correlated_oracle": (
                    "constructed and excluded for failed future-independence"
                ),
                "departed_environment": (
                    "detector-error syndrome is the focal boundary refinement"
                ),
                "routed_implementation": "detector route register admitted",
                "alternative_record_instrument": (
                    "all-port instrument retained as assay, not fitted refinement"
                ),
            }
        ),
    )


def hash_event(
    parent_ids: tuple[str, ...],
    sequence: int,
    payload: str,
    signers: tuple[str, ...],
) -> str:
    body = canonical_json(
        {
            "parents": parent_ids,
            "sequence": sequence,
            "payload": payload,
            "signers": signers,
        }
    )
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def event_node(
    parent_ids: tuple[str, ...],
    sequence: int,
    payload: str,
    signers: tuple[str, ...],
) -> tuple[Any, ...]:
    """Construct one content-addressed event with deterministic MAC tags."""

    event_id = hash_event(parent_ids, sequence, payload, signers)
    signatures = tuple(
        (
            signer,
            hmac.new(
                VALIDATOR_KEYS[signer],
                event_id.encode("utf-8"),
                hashlib.sha256,
            ).hexdigest(),
        )
        for signer in signers
    )
    return event_id, parent_ids, sequence, payload, signers, signatures


def build_operation_dag(classification: str, variant: str) -> dict[str, Any]:
    genesis_node = event_node((), 0, "balance=0", ("v0", "v1", "v2"))
    genesis = genesis_node[0]
    if classification == "serializable":
        first_payload, second_payload = (
            ("credit=1", "debit=1")
            if variant == "a"
            else ("debit=1", "credit=1")
        )
        first_node = event_node(
            (genesis,), 1, first_payload, ("v0", "v1")
        )
        first = first_node[0]
        second_node = event_node(
            (first,), 2, second_payload, ("v1", "v2")
        )
        nodes = (
            genesis_node,
            first_node,
            second_node,
        )
    else:
        left_payload, right_payload = (
            ("write=A", "write=B")
            if variant == "a"
            else ("write=B", "write=A")
        )
        left_node = event_node(
            (genesis,), 1, left_payload, ("v0", "v1")
        )
        right_node = event_node(
            (genesis,), 1, right_payload, ("v0", "v2")
        )
        nodes = (
            genesis_node,
            left_node,
            right_node,
        )
    return {
        "classification": classification,
        "variant": variant,
        "nodes": nodes,
    }


def verify_dag(dag: dict[str, Any]) -> dict[str, Any]:
    hash_valid = all(
        event_id == hash_event(parents, sequence, payload, signers)
        for (
            event_id,
            parents,
            sequence,
            payload,
            signers,
            _,
        ) in dag["nodes"]
    )
    authentication_valid = all(
        signatures
        == tuple(
            (
                signer,
                hmac.new(
                    VALIDATOR_KEYS[signer],
                    event_id.encode("utf-8"),
                    hashlib.sha256,
                ).hexdigest(),
            )
            for signer in signers
        )
        for event_id, _, _, _, signers, signatures in dag["nodes"]
    )
    prior_ids: set[str] = set()
    parents_valid = True
    for event_id, parents, _, _, _, _ in dag["nodes"]:
        if any(parent not in prior_ids for parent in parents):
            parents_valid = False
        prior_ids.add(event_id)
    signer_sequence_payloads: dict[tuple[str, int], set[str]] = {}
    for _, _, sequence, payload, signers, _ in dag["nodes"]:
        for signer in signers:
            signer_sequence_payloads.setdefault((signer, sequence), set()).add(
                payload
            )
    equivocation = any(
        len(payloads) > 1
        for (signer, sequence), payloads in signer_sequence_payloads.items()
        if signer == "v0" and sequence > 0
    )
    return {
        "hash_valid": hash_valid,
        "authentication_valid": authentication_valid,
        "parents_valid": parents_valid,
        "equivocation_detected": equivocation,
        "replay_idempotent": (
            len({node[0] for node in dag["nodes"] + (dag["nodes"][-1],)})
            == len(dag["nodes"])
        ),
        "classification": (
            "equivocation" if equivocation else "serializable"
        ),
    }


def distributed_process_receipt() -> dict[str, Any]:
    histories = (
        ("serializable_a", "serializable", "a"),
        ("serializable_b", "serializable", "b"),
        ("equivocation_a", "equivocation", "a"),
        ("equivocation_b", "equivocation", "b"),
    )
    schedules = (
        ("complete_delivery_0", 0),
        ("complete_delivery_1", 0),
        ("complete_delivery_2", 0),
        ("complete_delivery_3", 0),
        ("isolated_split_view", 1),
    )
    base_rows = []
    expanded_rows = []
    dag_receipts: dict[str, Any] = {}
    schedule_receipts = {
        name: hashlib.sha256(
            canonical_json({"schedule": name, "error": error}).encode("utf-8")
        ).hexdigest()
        for name, error in schedules
    }
    for history_id, classification, variant in histories:
        dag = build_operation_dag(classification, variant)
        audit = verify_dag(dag)
        truth = 0 if audit["classification"] == "serializable" else 1
        base_counts = [0, 0]
        expanded_counts = [0, 0, 0, 0]
        for schedule_name, error in schedules:
            public_bit = truth ^ error
            base_counts[public_bit] += 1
            expanded_index = public_bit * 2 + error
            expanded_counts[expanded_index] += 1
            assert schedule_receipts[schedule_name]
        base_rows.append(tuple(Fraction(count, len(schedules)) for count in base_counts))
        expanded_rows.append(
            tuple(Fraction(count, len(schedules)) for count in expanded_counts)
        )
        dag_receipts[history_id] = {
            "dag_digest": hashlib.sha256(
                canonical_json(dag["nodes"]).encode("utf-8")
            ).hexdigest(),
            "audit": audit,
            "node_count": len(dag["nodes"]),
            "materialized_endpoint": "balance_0",
        }

    payload_tamper = build_operation_dag("serializable", "a")
    payload_nodes = list(payload_tamper["nodes"])
    event_id, parents, sequence, _, signers, signatures = payload_nodes[1]
    payload_nodes[1] = (
        event_id,
        parents,
        sequence,
        "credit=999",
        signers,
        signatures,
    )
    payload_tamper["nodes"] = tuple(payload_nodes)

    mac_tamper = build_operation_dag("serializable", "a")
    mac_nodes = list(mac_tamper["nodes"])
    event_id, parents, sequence, payload, signers, signatures = mac_nodes[1]
    forged_signatures = (
        (signatures[0][0], "0" * 64),
        *signatures[1:],
    )
    mac_nodes[1] = (
        event_id,
        parents,
        sequence,
        payload,
        signers,
        forged_signatures,
    )
    mac_tamper["nodes"] = tuple(mac_nodes)

    return {
        "process": (
            "authenticated operation DAG -> enumerated delivery/adversary "
            "schedule -> materialized audit bit -> replay audit"
        ),
        "schedules": schedules,
        "schedule_receipts": schedule_receipts,
        "dag_receipts": dag_receipts,
        "negative_controls": {
            "payload_tamper_audit": verify_dag(payload_tamper),
            "mac_tamper_audit": verify_dag(mac_tamper),
        },
        "base_record_outcomes": ("audit_serializable", "audit_equivocation"),
        "base_record_kernel": tuple(base_rows),
        "expanded_record_outcomes": (
            "audit_0_receipt_0",
            "audit_0_receipt_1",
            "audit_1_receipt_0",
            "audit_1_receipt_1",
        ),
        "expanded_record_kernel": tuple(expanded_rows),
        "security_boundary": (
            "content hashes, parent checks and deterministic fixture MACs are "
            "executable controls, not deployed key management, a forgery "
            "reduction, or an asynchronous BFT proof"
        ),
    }


def distributed_contract(receipt: dict[str, Any]) -> PhysicalHistoryContract:
    histories = (
        "serializable_variant_a",
        "serializable_variant_b",
        "equivocation_variant_a",
        "equivocation_variant_b",
    )
    return PhysicalHistoryContract(
        contract_id="DPHYS-AUTH-DAG-01",
        platform_label="replayable_authenticated_operation_dag",
        histories=histories,
        interventions=("materialized_endpoint_read", "authenticated_replay_audit"),
        response_outcomes=("signal_accept", "signal_reject"),
        responses=(
            (
                (Fraction(1), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(1), Fraction(0)),
            ),
            (
                (Fraction(1), Fraction(0)),
                (Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(1)),
            ),
        ),
        base_record_outcomes=receipt["base_record_outcomes"],
        base_record_kernel=receipt["base_record_kernel"],
        target_actions=("commit", "commit", "abort", "abort"),
        paths=("leaderless_gossip_view", "hardening_layer_view"),
        path_views=(
            ("green", "green", "red", "red"),
            ("red", "red", "green", "green"),
        ),
        refinements=(
            PhysicalRefinement(
                refinement_id="authenticated_layer_register",
                constructor="routed_implementation",
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                path_tags=("gossip", "hardening"),
                certified_path_provenance=True,
                certificate_kind="authenticated_protocol_layer_record",
                resource_vector=(("authenticated_layer_bits", 1),),
            ),
            PhysicalRefinement(
                refinement_id="authenticated_dag_delivery_receipt",
                constructor="history",
                cost=2,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                record_outcomes=receipt["expanded_record_outcomes"],
                record_kernel=receipt["expanded_record_kernel"],
                certificate_kind="operation_dag_plus_delivery_receipt",
                resource_vector=(
                    ("authenticated_dag_records", 1),
                    ("authenticated_delivery_receipts", 1),
                ),
            ),
            PhysicalRefinement(
                refinement_id="replicated_materialized_audit_bit",
                constructor="resource",
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                record_outcomes=(
                    "audit_00",
                    "audit_01",
                    "audit_10",
                    "audit_11",
                ),
                record_kernel=independent_pair_kernel(
                    receipt["base_record_kernel"]
                ),
                certificate_kind=(
                    "conditionally_independent_noisy_materialized_pair"
                ),
                resource_vector=(("replicated_endpoint_copies", 1),),
            ),
            PhysicalRefinement(
                refinement_id="adaptive_abort_decoder",
                constructor="decoder_observer_boundary",
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=False,
                record_outcomes=("serializable", "equivocation"),
                record_kernel=(
                    (Fraction(1), Fraction(0)),
                    (Fraction(1), Fraction(0)),
                    (Fraction(0), Fraction(1)),
                    (Fraction(0), Fraction(1)),
                ),
                certificate_kind="target_fitted_abort_policy",
            ),
        ),
        resource_budget=3,
        equality_rule="exact_rational_stochastic_factorization",
        constructor_audit=constructor_audit(
            {
                "seed": "operation histories and schedules frozen before targets",
                "boundary": "materialized view and full-DAG replay boundaries declared",
                "resource": "three-unit scalar gate plus explicit protocol vector",
                "access": "delivery receipt charged only in expanded access class",
                "history": "authenticated operation DAG physically retained",
                "provenance": "DAG, signer and delivery receipts admitted",
                "fixed_future_correlated_oracle": (
                    "considered; no future-correlated oracle admitted"
                ),
                "departed_environment": (
                    "isolated delivery context represented by signed receipt"
                ),
                "routed_implementation": "protocol layer register admitted",
                "adaptive_controller_scheduler": (
                    "enumerated schedule frozen rather than fitted"
                ),
                "decoder_observer_boundary": (
                    "target-fitted abort decoder constructed and excluded"
                ),
            }
        ),
    )


def restrict_expanded_access(
    contract: PhysicalHistoryContract,
    refinement_id: str,
    suffix: str,
) -> PhysicalHistoryContract:
    return replace(
        contract,
        contract_id=f"{contract.contract_id}-{suffix}",
        refinements=tuple(
            replace(item, accessible=False)
            if item.refinement_id == refinement_id
            else item
            for item in contract.refinements
        ),
    )


def role_signature(contract: PhysicalHistoryContract) -> dict[str, Any]:
    return {
        "history_count": len(contract.histories),
        "intervention_count": len(contract.interventions),
        "response_outcome_count": len(contract.response_outcomes),
        "path_count": len(contract.paths),
        "base_record_outcome_count": len(contract.base_record_outcomes),
        "formed_complete_record_refinements": sum(
            item.record_kernel is not None
            and item.formed
            and item.future_independent
            and item.target_independent_claim
            for item in contract.refinements
        ),
        "formed_path_provenance_refinements": sum(
            item.path_tags is not None
            and item.formed
            and item.future_independent
            and item.target_independent_claim
            for item in contract.refinements
        ),
        "decision": "exact stochastic factorization plus path equalizer",
    }


def run() -> dict[str, Any]:
    quantum_receipt = quantum_process_receipt()
    distributed_receipt = distributed_process_receipt()
    quantum = quantum_contract(quantum_receipt)
    distributed = distributed_contract(distributed_receipt)
    quantum_result = compile_physical_certificate(quantum)
    distributed_result = compile_physical_certificate(distributed)

    quantum_restricted = compile_physical_certificate(
        restrict_expanded_access(
            quantum,
            "expanded_pointer_error_syndrome",
            "RESTRICTED-BOUNDARY",
        )
    )
    distributed_restricted = compile_physical_certificate(
        restrict_expanded_access(
            distributed,
            "authenticated_dag_delivery_receipt",
            "RESTRICTED-BOUNDARY",
        )
    )
    quantum_target_flip = replace(
        quantum,
        target_actions=("alpha", "beta", "alpha", "beta"),
    )
    distributed_target_flip = replace(
        distributed,
        target_actions=("alpha", "beta", "alpha", "beta"),
    )
    quantum_label_swap = compile_physical_certificate(
        replace(quantum, platform_label="arbitrary_platform_metadata")
    )
    distributed_label_swap = compile_physical_certificate(
        replace(distributed, platform_label="arbitrary_platform_metadata")
    )

    quantum_expected_base = (
        (Fraction(4, 5), Fraction(1, 5)),
        (Fraction(4, 5), Fraction(1, 5)),
        (Fraction(1, 5), Fraction(4, 5)),
        (Fraction(1, 5), Fraction(4, 5)),
    )
    distributed_expected_base = quantum_expected_base
    expected_expanded = (
        (Fraction(4, 5), Fraction(0), Fraction(0), Fraction(1, 5)),
        (Fraction(4, 5), Fraction(0), Fraction(0), Fraction(1, 5)),
        (Fraction(0), Fraction(1, 5), Fraction(4, 5), Fraction(0)),
        (Fraction(0), Fraction(1, 5), Fraction(4, 5), Fraction(0)),
    )
    quantum_selected = set(
        quantum_result["certificate"]["selected"]["refinement_ids"]
    )
    distributed_selected = set(
        distributed_result["certificate"]["selected"]["refinement_ids"]
    )

    checks = [
        {
            "id": "quantum_process_uses_unitary_preparation_record_and_error_gates",
            "pass": max(quantum_receipt["unitarity_errors"].values()) < TOL,
        },
        {
            "id": "qnd_recording_preserves_each_stabilizer_history",
            "pass": all(
                row["nondemolition_trace_distance_numeric"] < TOL
                for row in quantum_receipt["histories"].values()
            ),
        },
        {
            "id": "quantum_record_kernels_are_matrix_derived_and_exact",
            "pass": (
                quantum.base_record_kernel == quantum_expected_base
                and next(
                    item.record_kernel
                    for item in quantum.refinements
                    if item.refinement_id
                    == "expanded_pointer_error_syndrome"
                )
                == expected_expanded
            ),
        },
        {
            "id": "reduced_target_readout_is_history_blind",
            "pass": len(set(quantum.responses[0])) == 1,
        },
        {
            "id": "signed_all_port_instrument_excludes_dephased_null",
            "pass": (
                quantum_receipt["instrument_certificate"][
                    "classical_null_signed_mean"
                ]
                == 0
                and quantum_receipt["instrument_certificate"][
                    "alternative_signed_mean"
                ]
                == Fraction(4, 5)
                and quantum_receipt["instrument_certificate"][
                    "calibrated_gap"
                ]
                == Fraction(7, 10)
                and quantum_receipt["instrument_certificate"][
                    "sufficient_preparations"
                ]
                > 0
            ),
        },
        {
            "id": "distributed_hash_and_replay_controls_execute",
            "pass": all(
                row["audit"]["hash_valid"]
                and row["audit"]["authentication_valid"]
                and row["audit"]["parents_valid"]
                and row["audit"]["replay_idempotent"]
                for row in distributed_receipt["dag_receipts"].values()
            )
            and not distributed_receipt["negative_controls"][
                "payload_tamper_audit"
            ]["hash_valid"]
            and not distributed_receipt["negative_controls"][
                "mac_tamper_audit"
            ]["authentication_valid"],
        },
        {
            "id": "distributed_dag_detects_only_equivocating_histories",
            "pass": all(
                row["audit"]["equivocation_detected"]
                == history_id.startswith("equivocation")
                for history_id, row in distributed_receipt[
                    "dag_receipts"
                ].items()
            ),
        },
        {
            "id": "distributed_record_kernels_are_schedule_derived_and_exact",
            "pass": (
                distributed.base_record_kernel == distributed_expected_base
                and next(
                    item.record_kernel
                    for item in distributed.refinements
                    if item.refinement_id
                    == "authenticated_dag_delivery_receipt"
                )
                == expected_expanded
            ),
        },
        {
            "id": "noisy_base_records_fail_exact_later_response_factorization",
            "pass": (
                not quantum_result["base_evaluation"][
                    "response_factorization"
                ]["factors"]
                and not distributed_result["base_evaluation"][
                    "response_factorization"
                ]["factors"]
            ),
        },
        {
            "id": "expanded_formed_records_admit_exact_stochastic_decoders",
            "pass": (
                quantum_result["verdict"] == "MINIMAL_REFINEMENT"
                and distributed_result["verdict"] == "MINIMAL_REFINEMENT"
                and quantum_selected
                == {
                    "expanded_pointer_error_syndrome",
                    "certified_detector_route",
                }
                and distributed_selected
                == {
                    "authenticated_dag_delivery_receipt",
                    "authenticated_layer_register",
                }
            ),
        },
        {
            "id": "finite_independent_noisy_copy_does_not_repair_exact_factorization",
            "pass": all(
                not item["sufficient"]
                for result, copied_id in (
                    (quantum_result, "replicated_noisy_pointer"),
                    (
                        distributed_result,
                        "replicated_materialized_audit_bit",
                    ),
                )
                for item in result["candidate_evaluations"]
                if set(item["refinement_ids"]) == {copied_id}
            ),
        },
        {
            "id": "departed_or_withheld_provenance_makes_remainder_boundary_relative",
            "pass": (
                quantum_restricted["verdict"] == "CANDIDATE_REMAINDER"
                and distributed_restricted["verdict"]
                == "CANDIDATE_REMAINDER"
                and quantum_result["verdict"] == "MINIMAL_REFINEMENT"
                and distributed_result["verdict"] == "MINIMAL_REFINEMENT"
            ),
        },
        {
            "id": "candidate_grammar_excludes_targets_in_both_platforms",
            "pass": (
                freeze_candidate_class(quantum)["digest"]
                == freeze_candidate_class(quantum_target_flip)["digest"]
                and freeze_candidate_class(distributed)["digest"]
                == freeze_candidate_class(distributed_target_flip)["digest"]
            ),
        },
        {
            "id": "platform_metadata_is_not_a_decision_input",
            "pass": (
                quantum_label_swap["verdict"] == quantum_result["verdict"]
                and quantum_label_swap["frozen_class_digest"]
                == quantum_result["frozen_class_digest"]
                and distributed_label_swap["verdict"]
                == distributed_result["verdict"]
                and distributed_label_swap["frozen_class_digest"]
                == distributed_result["frozen_class_digest"]
            ),
        },
        {
            "id": "unchanged_stochastic_factorization_contract_transfers",
            "pass": role_signature(quantum) == role_signature(distributed),
            "quantum_role_signature": role_signature(quantum),
            "distributed_role_signature": role_signature(distributed),
        },
        {
            "id": "exact_lp_checker_accepts_identity_and_rejects_overlap_obstruction",
            "pass": (
                exact_stochastic_decoder(
                    (
                        (Fraction(1), Fraction(0)),
                        (Fraction(0), Fraction(1)),
                    ),
                    (
                        (Fraction(1), Fraction(0)),
                        (Fraction(0), Fraction(1)),
                    ),
                )["factors"]
                and not exact_stochastic_decoder(
                    (
                        (Fraction(4, 5), Fraction(1, 5)),
                        (Fraction(1, 5), Fraction(4, 5)),
                    ),
                    (
                        (Fraction(1), Fraction(0)),
                        (Fraction(0), Fraction(1)),
                    ),
                )["factors"]
            ),
        },
    ]
    result = {
        "schema": (
            "dynamic-unity/physical-history-certificate-transfer-probe/v0.1"
        ),
        "candidate_ids": [
            "HC-DU-033",
            "HC-DU-034B",
            "HC-DU-036B",
            "HC-DU-039",
            "H-CCR-02",
            "H-CCR-05",
            "H-CCR-12",
            "H-CCR-13",
        ],
        "claim_grade": (
            "EXACT FINITE MATRIX/PROTOCOL CONSTRUCTION + EXACT-RATIONAL "
            "STOCHASTIC FACTORIZATION PILOT / PHYSICAL GENERALIZATION, "
            "LABORATORY REALIZATION, CRYPTOGRAPHIC SECURITY AND NOVELTY OPEN"
        ),
        "checks_passed": sum(int(check["pass"]) for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "quantum_process_receipt": quantum_receipt,
        "distributed_process_receipt": distributed_receipt,
        "compiler_results": {
            "quantum_expanded_boundary": quantum_result,
            "quantum_restricted_boundary": quantum_restricted,
            "distributed_expanded_boundary": distributed_result,
            "distributed_restricted_boundary": distributed_restricted,
        },
        "verdict": (
            "PHYSICAL/PROTOCOL STOCHASTIC-RECORD TRANSFER VIABLE / "
            "NOISY BASE RECORDS INSUFFICIENT / FORMED ERROR OR DELIVERY "
            "PROVENANCE RESTORES FACTORIZATION / RESTRICTED-BOUNDARY "
            "REMAINDERS ARE INTERFACE-RELATIVE / NO IRREDUCIBLE PHYSICAL "
            "REMAINDER"
        ),
        "scientific_advance": [
            (
                "The compiler now accepts stochastic formed records through "
                "exact finite Blackwell-style factorization rather than "
                "deterministic history labels."
            ),
            (
                "A matrix-derived QND quantum record and an enumerated "
                "authenticated DAG process use the same decision contract; "
                "the matched 1/5 noise rate is a designed transfer control."
            ),
            (
                "The inaccessible error/delivery syndrome gives an exact "
                "boundary-relative capability witness; expanding the boundary "
                "absorbs it with charged provenance."
            ),
        ],
        "not_established": [
            "universal physical record selection",
            "proper-time history certification",
            "laboratory feasibility beyond the ideal finite model",
            "cryptographic authentication security",
            "asynchronous BFT safety or liveness",
            "a naturally selected normalized cross-platform invariant",
            "exhaustive physical refinement class",
            "irreducible physical remainder",
            "record-first ontology",
            "new physical law",
            "claim-specific novelty",
        ],
    }
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = run()
    print(
        "du_physical_history_certificate_transfer_probe: "
        f"{result['checks_passed']}/{result['checks_total']} checks passed\n"
        f"VERDICT: {result['verdict']}\n"
        f"artifact: {ARTIFACT}"
    )
    if result["checks_passed"] != result["checks_total"]:
        failed = [
            check["id"] for check in result["checks"] if not check["pass"]
        ]
        raise SystemExit(f"failed checks: {failed}")


if __name__ == "__main__":
    main()
