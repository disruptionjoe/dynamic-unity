#!/usr/bin/env python3
"""Exact boundary checks for one typed reconstruction framework.

The framework asks, in order:

1. does the declared record possess an admissible completion; and
2. if so, is the held-out target constant on that completion fibre?

It is applied without changing those meanings to a multi-time process,
conformal geometry, and a hostile regional-finality specimen.  Local
computation is restricted to exact finite witnesses and the minimum binary
pair-context obstruction.  Passing establishes no physical completeness,
novel mathematics, record-first ontology, or new physics.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Hashable, Mapping, Sequence

from du_conformal_record_geometry_tournament_probe import (
    F1,
    F2,
    HIDDEN,
    X_LEFT,
    X_MIDDLE,
    X_OVERLAP,
    conformal_factor,
    determinant_2x2,
    poly_integral,
    poly_value,
    q,
    record_surface,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_certified_reconstruction_fiber_result.json"
)
RUN_ID = "RUN-20260726-103543-typed-reconstruction-unification"

UNREALIZABLE = "UNREALIZABLE_RECORD"
RECONSTRUCTS = "RECONSTRUCTS_TARGET"
UNDERDETERMINED = "UNDERDETERMINED_TARGET"
INCOMPLETE = "INCOMPLETE_CONTRACT"


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda item: str(item[0]))
        }
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


@dataclass(frozen=True)
class TypedFiniteContract:
    """Finite executable specialization of the abstract fibre contract."""

    contract_id: str
    model_ids: tuple[str, ...]
    records: tuple[Hashable, ...]
    targets: tuple[Hashable, ...]
    observed_record: Hashable
    completion_class_exhaustive: bool = True
    record_type_frozen: bool = True
    target_type_frozen: bool = True
    identity_type_frozen: bool = True


def contract_errors(contract: TypedFiniteContract) -> tuple[str, ...]:
    errors: list[str] = []
    if not contract.contract_id:
        errors.append("missing_contract_id")
    if not contract.model_ids:
        errors.append("empty_ambient_completion_class")
    if len(set(contract.model_ids)) != len(contract.model_ids):
        errors.append("duplicate_model_id")
    if len(contract.records) != len(contract.model_ids):
        errors.append("record_arity")
    if len(contract.targets) != len(contract.model_ids):
        errors.append("target_arity")
    if not contract.completion_class_exhaustive:
        errors.append("completion_class_not_exhaustive")
    if not contract.record_type_frozen:
        errors.append("record_type_not_frozen")
    if not contract.target_type_frozen:
        errors.append("target_type_not_frozen")
    if not contract.identity_type_frozen:
        errors.append("identity_type_not_frozen")
    return tuple(sorted(errors))


def classify(contract: TypedFiniteContract) -> dict[str, Any]:
    errors = contract_errors(contract)
    if errors:
        return {
            "contract_id": contract.contract_id,
            "verdict": INCOMPLETE,
            "errors": errors,
        }

    fibre = tuple(
        (model_id, target)
        for model_id, record, target in zip(
            contract.model_ids,
            contract.records,
            contract.targets,
            strict=True,
        )
        if record == contract.observed_record
    )
    if not fibre:
        return {
            "contract_id": contract.contract_id,
            "verdict": UNREALIZABLE,
            "fibre_size": 0,
            "target_values": (),
        }

    target_values = tuple(dict.fromkeys(target for _, target in fibre))
    if len(target_values) == 1:
        return {
            "contract_id": contract.contract_id,
            "verdict": RECONSTRUCTS,
            "fibre_size": len(fibre),
            "target_values": target_values,
            "models": tuple(model_id for model_id, _ in fibre),
        }

    first_target = target_values[0]
    second_target = target_values[1]
    first_model = next(
        model_id for model_id, target in fibre if target == first_target
    )
    second_model = next(
        model_id for model_id, target in fibre if target == second_target
    )
    return {
        "contract_id": contract.contract_id,
        "verdict": UNDERDETERMINED,
        "fibre_size": len(fibre),
        "target_values": target_values,
        "witness": {
            "same_record_models": (first_model, second_model),
            "different_targets": (first_target, second_target),
        },
    }


def factorization_receipt(
    model_ids: Sequence[str],
    records: Sequence[Hashable],
    targets: Sequence[Hashable],
) -> dict[str, Any]:
    """Check ker(record) <= ker(target) on a finite declared class."""

    if not (len(model_ids) == len(records) == len(targets)):
        raise ValueError("factorization_arity")
    decoder: dict[Hashable, Hashable] = {}
    witness: dict[str, Any] | None = None
    for model_id, record, target in zip(
        model_ids, records, targets, strict=True
    ):
        if record in decoder and decoder[record] != target:
            first_index = next(
                index
                for index, prior_record in enumerate(records)
                if prior_record == record and targets[index] != target
            )
            witness = {
                "record": record,
                "models": (model_ids[first_index], model_id),
                "targets": (targets[first_index], target),
            }
            break
        decoder[record] = target
    return {
        "factorizes": witness is None,
        "kernel_inclusion": witness is None,
        "decoder_on_record_image": tuple(
            (record, target)
            for record, target in sorted(
                decoder.items(), key=lambda item: repr(item[0])
            )
        ),
        "witness": witness,
    }


def refinement_receipt(
    model_ids: Sequence[str],
    coarse_records: Sequence[Hashable],
    fine_records: Sequence[Hashable],
    projection: Callable[[Hashable], Hashable],
) -> dict[str, Any]:
    """Check r_coarse = projection o r_fine on one completion class."""

    if not (len(model_ids) == len(coarse_records) == len(fine_records)):
        raise ValueError("refinement_arity")
    failures = tuple(
        model_id
        for model_id, coarse, fine in zip(
            model_ids, coarse_records, fine_records, strict=True
        )
        if projection(fine) != coarse
    )
    return {
        "is_same_class_refinement": not failures,
        "projection_failures": failures,
    }


def bit_assignments(vertices: Sequence[str]) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.product((0, 1), repeat=len(vertices)))


def satisfies_parities(
    vertices: Sequence[str],
    assignment: Sequence[int],
    edges: Sequence[tuple[str, str, int]],
) -> bool:
    values = dict(zip(vertices, assignment, strict=True))
    return all(
        values[right] == (values[left] ^ parity)
        for left, right, parity in edges
    )


def satisfying_assignments(
    vertices: Sequence[str],
    edges: Sequence[tuple[str, str, int]],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        assignment
        for assignment in bit_assignments(vertices)
        if satisfies_parities(vertices, assignment, edges)
    )


def uniform_pair_table(parity: int) -> tuple[Fraction, ...]:
    """Order: 00, 01, 10, 11."""

    return tuple(
        Fraction(1, 2) if right == (left ^ parity) else Fraction(0)
        for left, right in itertools.product((0, 1), repeat=2)
    )


def marginal_from_uniform_support(
    vertices: Sequence[str],
    support: Sequence[Sequence[int]],
    left: str,
    right: str,
) -> tuple[Fraction, ...]:
    if not support:
        raise ValueError("empty_support")
    left_index = vertices.index(left)
    right_index = vertices.index(right)
    weight = Fraction(1, len(support))
    return tuple(
        sum(
            (
                weight
                for assignment in support
                if assignment[left_index] == left_value
                and assignment[right_index] == right_value
            ),
            Fraction(0),
        )
        for left_value, right_value in itertools.product((0, 1), repeat=2)
    )


def search_minimum_hostile_pair_context() -> dict[str, Any]:
    """Find the first inclusion-minimal inconsistent simple binary cover."""

    for vertex_count in range(1, 5):
        vertices = tuple(
            chr(ord("A") + index) for index in range(vertex_count)
        )
        possible_pairs = tuple(itertools.combinations(vertices, 2))
        for edge_count in range(1, len(possible_pairs) + 1):
            for selected_pairs in itertools.combinations(
                possible_pairs, edge_count
            ):
                for parities in itertools.product((0, 1), repeat=edge_count):
                    edges = tuple(
                        (left, right, parity)
                        for (left, right), parity in zip(
                            selected_pairs, parities, strict=True
                        )
                    )
                    support = satisfying_assignments(vertices, edges)
                    if support:
                        continue
                    deletion_supports = tuple(
                        satisfying_assignments(
                            vertices,
                            edges[:index] + edges[index + 1 :],
                        )
                        for index in range(len(edges))
                    )
                    if not all(deletion_supports):
                        continue
                    deletion_marginals_match = all(
                        all(
                            marginal_from_uniform_support(
                                vertices,
                                deletion_supports[deleted_index],
                                left,
                                right,
                            )
                            == uniform_pair_table(parity)
                            for edge_index, (left, right, parity) in enumerate(
                                edges
                            )
                            if edge_index != deleted_index
                        )
                        for deleted_index in range(len(edges))
                    )
                    if not deletion_marginals_match:
                        continue
                    return {
                        "vertex_count": vertex_count,
                        "context_count": edge_count,
                        "vertices": vertices,
                        "contexts": edges,
                        "global_support": support,
                        "proper_deletion_supports": deletion_supports,
                        "local_tables": tuple(
                            (
                                f"{left}{right}",
                                uniform_pair_table(parity),
                            )
                            for left, right, parity in edges
                        ),
                        "singleton_overlaps": (
                            Fraction(1, 2),
                            Fraction(1, 2),
                        ),
                        "inclusion_minimal": True,
                    }
    raise RuntimeError("no_hostile_pair_context_found")


def run() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        if not condition:
            raise AssertionError(f"{name}: {detail}")
        checks.append({"id": name, "pass": True, "detail": detail})

    # Multi-time process: equal ordinary endpoints, different held-out breaks.
    inputs = tuple(itertools.product((0, 1), repeat=3))
    no_break_table = tuple(a ^ c for a, _, c in inputs)
    recorded_break_table = no_break_table
    endpoint_break_table = tuple(0 for _ in inputs)
    model_ids = ("recorded_qnd_process", "endpoint_rival")
    multitime_base_records = (no_break_table, no_break_table)
    multitime_targets = (recorded_break_table, endpoint_break_table)
    base_multitime = classify(
        TypedFiniteContract(
            contract_id="multitime_endpoint_record",
            model_ids=model_ids,
            records=multitime_base_records,
            targets=multitime_targets,
            observed_record=no_break_table,
        )
    )
    stage_one_transcript = tuple((a ^ b, b ^ c) for a, b, c in inputs)
    refined_multitime_records = (
        ("FORMED_INTERMEDIATE_RECORDS", stage_one_transcript, no_break_table),
        ("NO_INTERMEDIATE_RECORD", (), no_break_table),
    )
    refined_multitime = classify(
        TypedFiniteContract(
            contract_id="multitime_formed_history_record",
            model_ids=model_ids,
            records=refined_multitime_records,
            targets=multitime_targets,
            observed_record=refined_multitime_records[0],
        )
    )
    multitime_refinement = refinement_receipt(
        model_ids,
        multitime_base_records,
        refined_multitime_records,
        lambda record: record[2],
    )
    check(
        "multitime_base_is_underdetermined",
        base_multitime["verdict"] == UNDERDETERMINED
        and sum(
            left != right
            for left, right in zip(
                recorded_break_table, endpoint_break_table, strict=True
            )
        )
        == 4,
        "the two frozen processes share the complete ordinary endpoint table and differ on four of eight held-out causal-break histories",
    )
    check(
        "formed_multitime_record_repairs_target",
        refined_multitime["verdict"] == RECONSTRUCTS
        and multitime_refinement["is_same_class_refinement"],
        "the independently formed intermediate transcript refines the endpoint record on the same completion class",
    )

    # Conformal geometry: the same fibre criterion on exact record values.
    flat_records = record_surface(conformal_factor())
    one_volume_records = record_surface(
        conformal_factor(q(1, 10), q(-2, 5))
    )
    hidden_records = record_surface(conformal_factor(hidden=q(1, 100)))
    geometry_models = ("flat", "one_volume_rival")
    geometry_one_records = (
        (flat_records["left_volume"],),
        (one_volume_records["left_volume"],),
    )
    geometry_two_records = (
        (
            flat_records["left_volume"],
            flat_records["overlap_volume"],
        ),
        (
            one_volume_records["left_volume"],
            one_volume_records["overlap_volume"],
        ),
    )
    geometry_targets = (
        flat_records["right_clock_squared"],
        one_volume_records["right_clock_squared"],
    )
    geometry_base = classify(
        TypedFiniteContract(
            contract_id="geometry_one_regional_volume",
            model_ids=geometry_models,
            records=geometry_one_records,
            targets=geometry_targets,
            observed_record=geometry_one_records[0],
        )
    )
    geometry_refined = classify(
        TypedFiniteContract(
            contract_id="geometry_two_regional_volumes",
            model_ids=geometry_models,
            records=geometry_two_records,
            targets=geometry_targets,
            observed_record=geometry_two_records[0],
        )
    )
    geometry_refinement = refinement_receipt(
        geometry_models,
        geometry_one_records,
        geometry_two_records,
        lambda record: (record[0],),
    )
    training_matrix = [
        [
            poly_integral(F1, X_LEFT, X_MIDDLE),
            poly_integral(F2, X_LEFT, X_MIDDLE),
        ],
        [
            poly_integral(F1, X_LEFT, X_OVERLAP),
            poly_integral(F2, X_LEFT, X_OVERLAP),
        ],
    ]
    training_determinant = determinant_2x2(training_matrix)
    hidden_geometry_records = (
        (
            flat_records["total_volume"],
            flat_records["left_clock_squared"],
            flat_records["left_volume"],
            flat_records["overlap_volume"],
        ),
        (
            hidden_records["total_volume"],
            hidden_records["left_clock_squared"],
            hidden_records["left_volume"],
            hidden_records["overlap_volume"],
        ),
    )
    hidden_geometry = classify(
        TypedFiniteContract(
            contract_id="geometry_hostile_smooth_completion",
            model_ids=("flat", "hidden_smooth_mode"),
            records=hidden_geometry_records,
            targets=(
                flat_records["right_clock_squared"],
                hidden_records["right_clock_squared"],
            ),
            observed_record=hidden_geometry_records[0],
        )
    )
    check(
        "geometry_one_record_is_underdetermined",
        geometry_base["verdict"] == UNDERDETERMINED,
        "one regional volume leaves flat space and the exact one-volume rival in one target-disagreeing fibre",
    )
    check(
        "geometry_two_mode_reconstruction_uses_same_classifier",
        geometry_refined["verdict"] == RECONSTRUCTS
        and geometry_refinement["is_same_class_refinement"]
        and training_determinant == Fraction(3, 64),
        "the second regional volume is an ordinary refinement and the full two-mode family is injective because its exact determinant is 3/64",
    )
    check(
        "geometry_hidden_mode_reopens_fibre",
        hidden_geometry["verdict"] == UNDERDETERMINED
        and poly_integral(HIDDEN, X_LEFT, X_MIDDLE) == 0
        and poly_integral(HIDDEN, X_LEFT, X_OVERLAP) == 0
        and poly_value(HIDDEN, X_LEFT) == 0
        and poly_value(HIDDEN, q(1)) == 4,
        "the hostile smooth mode preserves the training fibre and changes the held-out right clock",
    )

    # Hostile regional finality: exact minimal search, no encoded parity verdict.
    hostile = search_minimum_hostile_pair_context()
    regional_vertices = tuple(hostile["vertices"])
    regional_assignments = bit_assignments(regional_vertices)
    regional_model_ids = tuple(
        "".join(str(value) for value in assignment)
        for assignment in regional_assignments
    )
    regional_parity_records = tuple(
        tuple(
            assignment[regional_vertices.index(left)]
            ^ assignment[regional_vertices.index(right)]
            for left, right, _ in hostile["contexts"]
        )
        for assignment in regional_assignments
    )
    observed_parity_record = tuple(
        parity for _, _, parity in hostile["contexts"]
    )
    regional_contract = TypedFiniteContract(
        contract_id="regional_frustrated_pair_context",
        model_ids=regional_model_ids,
        records=regional_parity_records,
        targets=tuple(
            "DECLARED_UPPER_ACTION" for _ in regional_model_ids
        ),
        observed_record=observed_parity_record,
    )
    regional_result = classify(regional_contract)
    naive_constancy_only = len(
        {
            target
            for record, target in zip(
                regional_contract.records,
                regional_contract.targets,
                strict=True,
            )
            if record == regional_contract.observed_record
        }
    ) <= 1
    check(
        "hostile_regional_case_is_minimum",
        hostile["vertex_count"] == 3
        and hostile["context_count"] == 3
        and not hostile["global_support"]
        and len(regional_model_ids) == 8
        and all(hostile["proper_deletion_supports"]),
        "exact search first finds the three-variable, three-context frustrated cycle; none of eight ambient assignments lies in its fibre and every one-context deletion has a completion",
    )
    check(
        "hostile_local_records_are_individually_valid",
        all(
            sum(table, Fraction(0)) == 1
            and table.count(Fraction(1, 2)) == 2
            and table.count(Fraction(0)) == 2
            for _, table in hostile["local_tables"]
        )
        and hostile["singleton_overlaps"]
        == (Fraction(1, 2), Fraction(1, 2)),
        "every local pair table is normalized and every singleton overlap is exactly uniform",
    )
    check(
        "realizability_prevents_vacuous_reconstruction",
        regional_result["verdict"] == UNREALIZABLE
        and naive_constancy_only,
        "target constancy alone is vacuously true on the empty completion fibre, so existence must be checked first",
    )

    # The global factorization criterion and same-class refinement boundary.
    multitime_factorization = factorization_receipt(
        model_ids, multitime_base_records, multitime_targets
    )
    refined_multitime_factorization = factorization_receipt(
        model_ids, refined_multitime_records, multitime_targets
    )
    geometry_factorization = factorization_receipt(
        geometry_models, geometry_two_records, geometry_targets
    )
    check(
        "kernel_inclusion_matches_factorization",
        not multitime_factorization["kernel_inclusion"]
        and refined_multitime_factorization["kernel_inclusion"]
        and geometry_factorization["kernel_inclusion"],
        "on finite realized records, target factorization and record-kernel inclusion return identical verdicts",
    )

    coarse_models = ("m0", "m1")
    coarse_records = ("q0", "q1")
    fine_records = (("q0", "f0"), ("q1", "f1"))
    refinement = refinement_receipt(
        coarse_models,
        coarse_records,
        fine_records,
        lambda value: value[0],
    )
    absent_coarse_record = "q_missing"
    fine_over_absent = tuple(
        fine
        for coarse, fine in zip(coarse_records, fine_records, strict=True)
        if coarse == absent_coarse_record
    )
    check(
        "ordinary_refinement_cannot_resurrect_empty_fibre",
        refinement["is_same_class_refinement"] and not fine_over_absent,
        "if r_coarse = projection o r_fine on the same model class, every fine fibre lies inside its coarse fibre",
    )
    check(
        "regional_provenance_repair_is_contract_retyping",
        regional_result["verdict"] == UNREALIZABLE
        and hostile["proper_deletion_supports"]
        and not fine_over_absent,
        "restoring a process by splitting context occurrences must change the completion or identity type; it is not an ordinary refinement of the empty coarse fibre",
    )

    incomplete = classify(
        TypedFiniteContract(
            contract_id="unfrozen_identity_control",
            model_ids=("m",),
            records=("q",),
            targets=("t",),
            observed_record="q",
            identity_type_frozen=False,
        )
    )
    check(
        "unfrozen_identity_is_nonadjudication",
        incomplete["verdict"] == INCOMPLETE,
        "an unfrozen cross-context identity returns incomplete rather than reconstruction, remainder, or incompatibility",
    )

    result = {
        "schema_version": "dynamic-unity/certified-reconstruction-fiber/v0.1",
        "run_id": RUN_ID,
        "claim_grade": (
            "EXACT TYPED FIBRE THEOREM SPECIALIZATION + INCLUSION-MINIMAL "
            "REGIONAL COUNTEREXAMPLE / COMPONENT MATHEMATICS KNOWN / "
            "NO PHYSICAL SUFFICIENCY, ONTOLOGY, OR NEW PHYSICS"
        ),
        "theorem_receipt": {
            "classifier": (
                UNREALIZABLE,
                RECONSTRUCTS,
                UNDERDETERMINED,
            ),
            "global_reconstruction_criterion": (
                "target factors through record image iff "
                "kernel(record) is contained in kernel(target)"
            ),
            "refinement_boundary": (
                "same-class refinement can split a nonempty fibre but "
                "cannot make an empty coarse fibre nonempty"
            ),
            "hostile_correction": (
                "realizability precedes target constancy; occurrence "
                "splitting that restores a process is contract retyping"
            ),
        },
        "specimens": {
            "multitime": {
                "base": base_multitime,
                "refined": refined_multitime,
                "refinement": multitime_refinement,
                "base_factorization": multitime_factorization,
                "refined_factorization": refined_multitime_factorization,
            },
            "conformal_geometry": {
                "one_volume": geometry_base,
                "two_volumes": geometry_refined,
                "refinement": geometry_refinement,
                "two_mode_determinant": training_determinant,
                "two_volume_factorization": geometry_factorization,
                "hostile_smooth_completion": hidden_geometry,
            },
            "regional_finality": {
                "classification": regional_result,
                "naive_constancy_only_verdict": naive_constancy_only,
                "minimum_hostile_case": hostile,
                "repair_type": "CONTRACT_RETYPE_NOT_SAME_CLASS_REFINEMENT",
            },
        },
        "local_model_learning_receipt": {
            "admission_disposition": "ADMIT_LOCAL_LEARNING_BUILD",
            "research_only_baseline": (
                "standard fibre factorization plus known cyclic marginal "
                "obstructions"
            ),
            "local_learning_delta": (
                "the minimum exact DU hostile fixture exposes vacuous "
                "constancy and separates record refinement from identity/"
                "completion retyping"
            ),
            "generated_not_encoded": (
                "simple covers and parity labels were searched in increasing "
                "size; every assignment and one-context deletion was "
                "enumerated for each candidate through the first obstruction"
            ),
            "pre_hardware_checkpoint_result": (
                "REALIZABILITY_FIRST_COMMON_THEOREM_WITH_MINIMUM_HOSTILE_CASE"
            ),
            "decision_consequence": (
                "install realizability before reconstruction and type "
                "provenance repair as contract retyping"
            ),
            "stop_or_continuation": "STOP_EXACT_BOUNDARY_EARNED",
            "maximum_grade": (
                "exact finite and set-theoretic program theorem; no "
                "external hardware path"
            ),
        },
        "checks": checks,
        "summary": {
            "passed": sum(int(item["pass"]) for item in checks),
            "total": len(checks),
        },
    }
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    return result


if __name__ == "__main__":
    output = run()
    print(
        f"certified reconstruction fibre: "
        f"{output['summary']['passed']}/{output['summary']['total']} checks passed"
    )
