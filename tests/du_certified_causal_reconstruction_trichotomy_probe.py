#!/usr/bin/env python3
"""Exact finite specialization of the Certified Causal Reconstruction trichotomy.

This probe separates three questions that are often blurred:

1. Does a frozen certified-record kernel reconstruct every declared
   intervention response?
2. If not, does a target-independent, resource-accounted completion do so?
3. If no member of the finite completion class reconstructs, what positive
   class-relative approximation margin remains?

All arithmetic is rational.  The binary-outcome decoder problem is a finite
linear program.  Rather than depending on a numerical optimizer, the probe
enumerates every feasible vertex exactly.  That makes the scoped result
replayable, but does not establish physical completeness of the supplied
record or completion class, theorem novelty, or new physics.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_certified_causal_reconstruction_trichotomy_result.json"
)

Vector = tuple[Fraction, ...]
Kernel = tuple[Vector, ...]
ResponseFamily = tuple[Vector, ...]
ResourceVector = tuple[int, ...]


@dataclass(frozen=True)
class Completion:
    completion_id: str
    record_labels: tuple[str, ...]
    record_kernel: Kernel
    resources: ResourceVector
    independently_formed: bool = True
    future_independent: bool = True
    target_independent: bool = True
    boundary_preserving: bool = True


@dataclass(frozen=True)
class ReconstructionContract:
    contract_id: str
    histories: tuple[str, ...]
    interventions: tuple[str, ...]
    responses_one: ResponseFamily
    completions: tuple[Completion, ...]
    base_completion_id: str
    observer_boundary_id: str
    resource_dimensions: tuple[str, ...]
    contract_frozen: bool = True
    completion_class_frozen: bool = True
    complete_binary_outcomes: bool = True


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"))


def validate_contract(contract: ReconstructionContract) -> list[str]:
    errors: list[str] = []
    history_count = len(contract.histories)
    resource_count = len(contract.resource_dimensions)

    if not contract.contract_frozen:
        errors.append("contract_not_frozen")
    if not contract.completion_class_frozen:
        errors.append("completion_class_not_frozen")
    if not contract.complete_binary_outcomes:
        errors.append("incomplete_outcome_alphabet")
    if not contract.histories:
        errors.append("empty_history_set")
    if len(set(contract.histories)) != history_count:
        errors.append("duplicate_history_id")
    if not contract.interventions:
        errors.append("empty_intervention_set")
    if len(set(contract.interventions)) != len(contract.interventions):
        errors.append("duplicate_intervention_id")
    if len(contract.responses_one) != len(contract.interventions):
        errors.append("response_intervention_arity")
    for row in contract.responses_one:
        if len(row) != history_count:
            errors.append("response_history_arity")
        if any(value < 0 or value > 1 for value in row):
            errors.append("response_probability_out_of_range")
    if not contract.resource_dimensions:
        errors.append("empty_resource_order")
    if len(set(contract.resource_dimensions)) != resource_count:
        errors.append("duplicate_resource_dimension")
    if not contract.observer_boundary_id.strip():
        errors.append("empty_observer_boundary")
    if not contract.completions:
        errors.append("empty_completion_class")

    completion_ids = [item.completion_id for item in contract.completions]
    if len(set(completion_ids)) != len(completion_ids):
        errors.append("duplicate_completion_id")
    if contract.base_completion_id not in completion_ids:
        errors.append("missing_base_completion")

    for item in contract.completions:
        if not item.record_labels:
            errors.append(f"empty_record_alphabet:{item.completion_id}")
        if len(item.record_kernel) != history_count:
            errors.append(f"record_history_arity:{item.completion_id}")
        for row in item.record_kernel:
            if len(row) != len(item.record_labels):
                errors.append(f"record_alphabet_arity:{item.completion_id}")
            if any(value < 0 for value in row):
                errors.append(f"negative_record_probability:{item.completion_id}")
            if sum(row, start=Fraction(0)) != 1:
                errors.append(f"incomplete_record_distribution:{item.completion_id}")
        if len(item.resources) != resource_count:
            errors.append(f"resource_arity:{item.completion_id}")
        if any(value < 0 for value in item.resources):
            errors.append(f"negative_resource:{item.completion_id}")
        if not item.independently_formed:
            errors.append(f"unformed_completion:{item.completion_id}")
        if not item.future_independent:
            errors.append(f"future_correlated_completion:{item.completion_id}")
        if not item.target_independent:
            errors.append(f"target_fitted_completion:{item.completion_id}")
        if not item.boundary_preserving:
            errors.append(f"boundary_changing_completion:{item.completion_id}")
    return sorted(set(errors))


def completion_class_digest(contract: ReconstructionContract) -> str:
    """Hash candidate construction without consulting target responses."""

    payload = {
        "contract_id": contract.contract_id,
        "histories": contract.histories,
        "interventions": contract.interventions,
        "base_completion_id": contract.base_completion_id,
        "observer_boundary_id": contract.observer_boundary_id,
        "resource_dimensions": contract.resource_dimensions,
        "completions": [
            {
                "completion_id": item.completion_id,
                "record_labels": item.record_labels,
                "record_kernel": item.record_kernel,
                "resources": item.resources,
                "independently_formed": item.independently_formed,
                "future_independent": item.future_independent,
                "target_independent": item.target_independent,
                "boundary_preserving": item.boundary_preserving,
            }
            for item in sorted(
                contract.completions, key=lambda candidate: candidate.completion_id
            )
        ],
    }
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()


def solve_square(
    matrix: list[list[Fraction]], rhs: list[Fraction]
) -> tuple[Fraction, ...] | None:
    size = len(matrix)
    augmented = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
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
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            multiplier = augmented[row][column]
            if multiplier:
                augmented[row] = [
                    value - multiplier * pivot_entry
                    for value, pivot_entry in zip(
                        augmented[row], augmented[column], strict=True
                    )
                ]
    return tuple(augmented[row][-1] for row in range(size))


def dot(left: Iterable[Fraction], right: Iterable[Fraction]) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    )


def binary_decoder_lp(record_kernel: Kernel, target: Vector) -> dict[str, Any]:
    """Solve min_k max_h |Q(h)k-target(h)| by exact vertex enumeration."""

    record_count = len(record_kernel[0])
    variable_count = record_count + 1
    constraints: list[tuple[tuple[Fraction, ...], Fraction, str]] = []

    for history_index, (record_row, probability) in enumerate(
        zip(record_kernel, target, strict=True)
    ):
        constraints.append(
            (
                tuple(record_row) + (Fraction(-1),),
                probability,
                f"h{history_index}:prediction_minus_target",
            )
        )
        constraints.append(
            (
                tuple(-value for value in record_row) + (Fraction(-1),),
                -probability,
                f"h{history_index}:target_minus_prediction",
            )
        )
    for record_index in range(record_count):
        lower = [Fraction(0)] * variable_count
        lower[record_index] = Fraction(-1)
        constraints.append(
            (tuple(lower), Fraction(0), f"k{record_index}:lower")
        )
        upper = [Fraction(0)] * variable_count
        upper[record_index] = Fraction(1)
        constraints.append(
            (tuple(upper), Fraction(1), f"k{record_index}:upper")
        )
    epsilon_lower = [Fraction(0)] * variable_count
    epsilon_lower[-1] = Fraction(-1)
    constraints.append((tuple(epsilon_lower), Fraction(0), "epsilon:lower"))
    epsilon_upper = [Fraction(0)] * variable_count
    epsilon_upper[-1] = Fraction(1)
    constraints.append((tuple(epsilon_upper), Fraction(1), "epsilon:upper"))

    vertices: dict[tuple[Fraction, ...], tuple[str, ...]] = {}
    systems_checked = 0
    for active_indexes in itertools.combinations(
        range(len(constraints)), variable_count
    ):
        systems_checked += 1
        matrix = [list(constraints[index][0]) for index in active_indexes]
        rhs = [constraints[index][1] for index in active_indexes]
        solution = solve_square(matrix, rhs)
        if solution is None:
            continue
        if all(
            dot(coefficients, solution) <= bound
            for coefficients, bound, _ in constraints
        ):
            active_names = tuple(
                constraints[index][2] for index in active_indexes
            )
            previous = vertices.get(solution)
            if previous is None or active_names < previous:
                vertices[solution] = active_names

    if not vertices:
        raise AssertionError("bounded decoder LP unexpectedly has no vertex")
    optimum = min(
        vertices,
        key=lambda vertex: (vertex[-1], vertex[:-1], vertices[vertex]),
    )
    decoder = optimum[:-1]
    predictions = tuple(dot(row, decoder) for row in record_kernel)
    residuals = tuple(
        prediction - probability
        for prediction, probability in zip(predictions, target, strict=True)
    )
    return {
        "deficiency": optimum[-1],
        "decoder_probability_one_by_record": decoder,
        "predictions": predictions,
        "signed_residuals": residuals,
        "active_constraints": vertices[optimum],
        "systems_checked": systems_checked,
        "feasible_vertices": len(vertices),
        "certificate_basis": (
            "exact exhaustive feasible-vertex enumeration for a bounded "
            "rational linear program"
        ),
    }


def completion_deficiency(
    contract: ReconstructionContract, completion: Completion
) -> dict[str, Any]:
    intervention_results = []
    for intervention, target in zip(
        contract.interventions, contract.responses_one, strict=True
    ):
        result = binary_decoder_lp(completion.record_kernel, target)
        intervention_results.append(
            {"intervention": intervention, **result}
        )
    deficiency = max(
        item["deficiency"] for item in intervention_results
    )
    binding_interventions = [
        item["intervention"]
        for item in intervention_results
        if item["deficiency"] == deficiency
    ]
    return {
        "completion_id": completion.completion_id,
        "resources": completion.resources,
        "deficiency": deficiency,
        "binding_interventions": binding_interventions,
        "intervention_results": intervention_results,
    }


def dominates(left: ResourceVector, right: ResourceVector) -> bool:
    return all(a <= b for a, b in zip(left, right, strict=True)) and any(
        a < b for a, b in zip(left, right, strict=True)
    )


def pareto_minimal_exact(
    exact_results: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    minimal = []
    for candidate in exact_results:
        if not any(
            dominates(other["resources"], candidate["resources"])
            for other in exact_results
            if other["completion_id"] != candidate["completion_id"]
        ):
            minimal.append(candidate)
    return sorted(
        minimal,
        key=lambda item: (item["resources"], item["completion_id"]),
    )


def adjudicate(contract: ReconstructionContract) -> dict[str, Any]:
    errors = validate_contract(contract)
    digest = completion_class_digest(contract)
    if errors:
        return {
            "contract_id": contract.contract_id,
            "observer_boundary_id": contract.observer_boundary_id,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": errors,
            "completion_class_digest": digest,
        }

    completion_map = {
        item.completion_id: item for item in contract.completions
    }
    results = [
        completion_deficiency(contract, completion_map[completion_id])
        for completion_id in sorted(completion_map)
    ]
    result_map = {item["completion_id"]: item for item in results}
    base_result = result_map[contract.base_completion_id]
    exact_results = [item for item in results if item["deficiency"] == 0]

    if base_result["deficiency"] == 0:
        verdict = "BASE_RECONSTRUCTION"
        selected = [base_result]
        margin = Fraction(0)
    elif exact_results:
        verdict = "REFINED_RECONSTRUCTION"
        selected = pareto_minimal_exact(exact_results)
        margin = Fraction(0)
    else:
        verdict = "CLASS_RELATIVE_REMAINDER"
        margin = min(item["deficiency"] for item in results)
        selected = [
            item for item in results if item["deficiency"] == margin
        ]

    return {
        "contract_id": contract.contract_id,
        "observer_boundary_id": contract.observer_boundary_id,
        "verdict": verdict,
        "errors": [],
        "completion_class_digest": digest,
        "base_completion_id": contract.base_completion_id,
        "class_relative_margin": margin,
        "selected_or_margin_attaining": [
            item["completion_id"] for item in selected
        ],
        "resource_dimensions": contract.resource_dimensions,
        "completion_results": results,
    }


def constant_completion(
    completion_id: str = "base_endpoint",
    resources: ResourceVector = (0, 0, 0),
    history_count: int = 2,
) -> Completion:
    return Completion(
        completion_id=completion_id,
        record_labels=("same",),
        record_kernel=tuple((Fraction(1),) for _ in range(history_count)),
        resources=resources,
    )


def identity_completion(
    completion_id: str,
    resources: ResourceVector,
    history_count: int = 2,
) -> Completion:
    return Completion(
        completion_id=completion_id,
        record_labels=tuple(f"r{index}" for index in range(history_count)),
        record_kernel=tuple(
            tuple(
                Fraction(int(row == column))
                for column in range(history_count)
            )
            for row in range(history_count)
        ),
        resources=resources,
    )


def contract(
    contract_id: str,
    responses: ResponseFamily,
    completions: tuple[Completion, ...],
    *,
    frozen: bool = True,
    observer_boundary_id: str = "local_endpoint_boundary",
) -> ReconstructionContract:
    history_count = len(responses[0])
    return ReconstructionContract(
        contract_id=contract_id,
        histories=tuple(f"h{index}" for index in range(history_count)),
        interventions=tuple(
            f"do_{index}" for index in range(len(responses))
        ),
        responses_one=responses,
        completions=completions,
        base_completion_id="base_endpoint",
        observer_boundary_id=observer_boundary_id,
        resource_dimensions=(
            "additional_record_bits",
            "boundary_expansions",
            "latency_units",
        ),
        contract_frozen=frozen,
    )


def run() -> dict[str, Any]:
    base_exact = contract(
        "base-reconstruction-control",
        ((Fraction(0), Fraction(1)),),
        (identity_completion("base_endpoint", (0, 0, 0)),),
    )

    refined = contract(
        "formed-refinement-control",
        (
            (Fraction(0), Fraction(1)),
            (Fraction(1, 4), Fraction(3, 4)),
        ),
        (
            constant_completion(),
            constant_completion("duplicated_endpoint", (1, 0, 0)),
            identity_completion("formed_syndrome", (1, 0, 1)),
        ),
    )

    remainder = contract(
        "finite-class-remainder-control",
        ((Fraction(0), Fraction(1), Fraction(0)),),
        (
            constant_completion(history_count=3),
            Completion(
                completion_id="formed_coarse_region",
                record_labels=("region_a", "region_b"),
                record_kernel=(
                    (Fraction(1), Fraction(0)),
                    (Fraction(1), Fraction(0)),
                    (Fraction(0), Fraction(1)),
                ),
                resources=(1, 0, 1),
            ),
        ),
    )

    boundary_absorber = contract(
        "boundary-expansion-absorber-control",
        ((Fraction(0), Fraction(1), Fraction(0)),),
        (
            constant_completion(history_count=3),
            Completion(
                completion_id="formed_coarse_region",
                record_labels=("region_a", "region_b"),
                record_kernel=(
                    (Fraction(1), Fraction(0)),
                    (Fraction(1), Fraction(0)),
                    (Fraction(0), Fraction(1)),
                ),
                resources=(1, 0, 1),
            ),
            identity_completion(
                "expanded_access_boundary", (0, 1, 2), history_count=3
            ),
        ),
        observer_boundary_id="expanded_access_boundary_frame",
    )

    pareto = contract(
        "partial-resource-order-control",
        ((Fraction(0), Fraction(1)),),
        (
            constant_completion(),
            identity_completion("one_bit_one_channel", (1, 1, 0)),
            identity_completion("two_bits_no_channel", (2, 0, 0)),
            identity_completion("dominated_exact_copy", (2, 2, 0)),
        ),
    )

    incomplete = replace(
        refined,
        contract_id="unfrozen-contract-control",
        contract_frozen=False,
    )

    adjudications = {
        "base": adjudicate(base_exact),
        "refined": adjudicate(refined),
        "remainder": adjudicate(remainder),
        "boundary_absorber": adjudicate(boundary_absorber),
        "pareto": adjudicate(pareto),
        "incomplete": adjudicate(incomplete),
    }

    target_mutation = replace(
        refined,
        responses_one=(
            (Fraction(1, 10), Fraction(9, 10)),
            (Fraction(1, 3), Fraction(2, 3)),
        ),
    )
    target_digest_stable = (
        completion_class_digest(refined)
        == completion_class_digest(target_mutation)
    )

    checks = {
        "base_reconstruction_detected": (
            adjudications["base"]["verdict"] == "BASE_RECONSTRUCTION"
            and adjudications["base"]["class_relative_margin"] == 0
        ),
        "refinement_detected": (
            adjudications["refined"]["verdict"]
            == "REFINED_RECONSTRUCTION"
            and adjudications["refined"]["selected_or_margin_attaining"]
            == ["formed_syndrome"]
        ),
        "base_failure_precedes_refinement": next(
            item
            for item in adjudications["refined"]["completion_results"]
            if item["completion_id"] == "base_endpoint"
        )["deficiency"]
        > 0,
        "finite_class_remainder_detected": (
            adjudications["remainder"]["verdict"]
            == "CLASS_RELATIVE_REMAINDER"
        ),
        "remainder_margin_positive": (
            adjudications["remainder"]["class_relative_margin"]
            == Fraction(1, 2)
        ),
        "boundary_expansion_absorbs_remainder": (
            adjudications["boundary_absorber"]["verdict"]
            == "REFINED_RECONSTRUCTION"
            and adjudications["boundary_absorber"][
                "selected_or_margin_attaining"
            ]
            == ["expanded_access_boundary"]
        ),
        "incomplete_contract_is_not_scientific_verdict": (
            adjudications["incomplete"]["verdict"] == "INCOMPLETE_CONTRACT"
            and "contract_not_frozen" in adjudications["incomplete"]["errors"]
        ),
        "target_mutation_cannot_change_frozen_class": target_digest_stable,
        "partial_resource_order_retains_incomparable_minima": (
            adjudications["pareto"]["selected_or_margin_attaining"]
            == ["one_bit_one_channel", "two_bits_no_channel"]
        ),
        "dominated_exact_completion_removed": (
            "dominated_exact_copy"
            not in adjudications["pareto"]["selected_or_margin_attaining"]
        ),
        "all_lp_certificates_exact": all(
            intervention_result["certificate_basis"].startswith("exact")
            for name, result in adjudications.items()
            if name != "incomplete"
            for completion_result in result["completion_results"]
            for intervention_result in completion_result[
                "intervention_results"
            ]
        ),
    }
    passed = sum(checks.values())
    if passed != len(checks):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"failed checks: {failed}")

    payload = {
        "probe": "du_certified_causal_reconstruction_trichotomy_probe",
        "claim_grade": (
            "exact finite rational binary-outcome theorem specialization; "
            "physical completeness and novelty open"
        ),
        "theorem_scope": {
            "history_set": "finite",
            "intervention_set": "finite",
            "outcomes": "complete binary",
            "record_and_completion_kernels": "finite exact rational stochastic",
            "completion_class": (
                "finite, frozen, independently formed, future-independent, "
                "target-independent, and boundary-preserving as supplied"
            ),
            "deficiency": (
                "minimum worst-history total variation over stochastic "
                "record decoders, maximized over interventions"
            ),
            "resource_order": "componentwise partial order",
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "target_mutation_digest_stable": target_digest_stable,
        "adjudications": adjudications,
        "limits": [
            "Supplied formation and completion-class premises are not derived.",
            "A positive margin is relative only to the frozen finite class.",
            "Binary-outcome finite rational specialization only.",
            "No shot noise, calibration, drift, or laboratory data are used.",
            "Finite LP geometry is known mathematics; novelty is not claimed.",
            "Boundary expansion can absorb a class-relative remainder.",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(jsonable(payload), indent=2) + "\n")
    return payload


if __name__ == "__main__":
    result = run()
    print(
        json.dumps(
            {
                "verdict": "PASS",
                "checks": f"{result['checks_passed']}/{result['checks_total']}",
                "artifact": str(ARTIFACT.relative_to(ROOT)),
                "remainder_margin": str(
                    result["adjudications"]["remainder"][
                        "class_relative_margin"
                    ]
                ),
            },
            indent=2,
        )
    )
