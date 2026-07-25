#!/usr/bin/env python3
"""Finite proof-carrying pilot for noninvertible history certificates.

The compiler in this probe keeps two operations separate:

1. freeze a finite, target-independent grammar of admissible record and
   provenance refinements; and
2. test those already-frozen candidates against a declared response/action
   target.

All stochastic response signatures are exact rational distributions.  The
pilot deliberately rejects nonzero approximate tolerances: pairwise
``epsilon``-closeness is not generally transitive and therefore does not by
itself define a record quotient.

The same typed compiler is applied to a noisy coherent-route fixture and an
authenticated distributed-history fixture.  The platform label is metadata
only.  Passing establishes a finite software/formal specialization, not a
quantum/consensus identity, a physical record-selection law, or an
irreducible physical remainder.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_noninvertible_history_certificate_compiler_result.json"
)

Distribution = tuple[Fraction, ...]
ResponseTable = tuple[tuple[Distribution, ...], ...]

REQUIRED_CONSTRUCTOR_AUDIT = (
    "seed",
    "boundary",
    "resource",
    "access",
    "hidden_state",
    "history",
    "provenance",
    "gauge",
    "family_containment",
    "fixed_future_correlated_oracle",
    "departed_environment",
    "routed_implementation",
    "adaptive_controller_scheduler",
    "alternative_record_instrument",
    "decoder_observer_boundary",
)


@dataclass(frozen=True)
class Refinement:
    """One primitive candidate fixed without consulting target responses."""

    refinement_id: str
    constructor: str
    record_labels: tuple[str, ...]
    cost: int
    formed: bool
    future_independent: bool
    accessible: bool
    preserves_frame: bool
    target_independent_claim: bool
    path_tags: tuple[str, ...] | None = None
    certified_path_provenance: bool = False
    certificate_kind: str = "none"


@dataclass(frozen=True)
class HistoryContract:
    """The unchanged finite interface consumed by the compiler."""

    contract_id: str
    platform_label: str
    histories: tuple[str, ...]
    interventions: tuple[str, ...]
    outcomes: tuple[str, ...]
    base_record: tuple[str, ...]
    responses: ResponseTable
    target_actions: tuple[str, ...]
    paths: tuple[str, ...]
    path_views: tuple[tuple[str, ...], ...]
    refinements: tuple[Refinement, ...]
    resource_budget: int
    equality_rule: str
    tolerance: Fraction
    constructor_audit: tuple[tuple[str, str], ...]
    contract_frozen: bool = True


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


def validate_contract(contract: HistoryContract) -> list[str]:
    errors: list[str] = []
    history_count = len(contract.histories)
    outcome_count = len(contract.outcomes)

    if not contract.contract_frozen:
        errors.append("contract_not_frozen")
    if not contract.histories:
        errors.append("empty_history_set")
    if len(set(contract.histories)) != history_count:
        errors.append("duplicate_history_id")
    if not contract.interventions:
        errors.append("empty_intervention_basis")
    if len(set(contract.interventions)) != len(contract.interventions):
        errors.append("duplicate_intervention_id")
    if not contract.outcomes:
        errors.append("empty_complete_outcome_alphabet")
    if len(set(contract.outcomes)) != outcome_count:
        errors.append("duplicate_outcome_id")
    if len(contract.base_record) != history_count:
        errors.append("base_record_arity")
    if len(contract.target_actions) != history_count:
        errors.append("target_action_arity")
    if not contract.paths:
        errors.append("empty_reconciliation_path_set")
    if len(set(contract.paths)) != len(contract.paths):
        errors.append("duplicate_path_id")
    if len(contract.path_views) != len(contract.paths):
        errors.append("path_view_path_arity")
    elif any(len(row) != history_count for row in contract.path_views):
        errors.append("path_view_history_arity")
    if contract.resource_budget < 0:
        errors.append("negative_resource_budget")

    if contract.equality_rule != "exact_rational_stochastic_signature":
        errors.append("unsupported_equality_rule")
    if contract.tolerance != 0:
        errors.append("nonzero_tolerance_requires_declared_closure_rule")

    if len(contract.responses) != len(contract.interventions):
        errors.append("response_intervention_arity")
    else:
        for intervention_row in contract.responses:
            if len(intervention_row) != history_count:
                errors.append("response_history_arity")
                continue
            for distribution in intervention_row:
                if len(distribution) != outcome_count:
                    errors.append("response_outcome_arity")
                elif any(value < 0 for value in distribution):
                    errors.append("negative_probability")
                elif sum(distribution, start=Fraction(0)) != 1:
                    errors.append("incomplete_outcome_distribution")

    refinement_ids = [item.refinement_id for item in contract.refinements]
    if len(set(refinement_ids)) != len(refinement_ids):
        errors.append("duplicate_refinement_id")
    for item in contract.refinements:
        if len(item.record_labels) != history_count:
            errors.append(f"record_label_arity:{item.refinement_id}")
        if item.cost < 0:
            errors.append(f"negative_cost:{item.refinement_id}")
        if item.path_tags is not None:
            if len(item.path_tags) != len(contract.paths):
                errors.append(f"path_tag_arity:{item.refinement_id}")
            if not item.certified_path_provenance:
                errors.append(
                    f"uncertified_path_tag_declared:{item.refinement_id}"
                )

    audit_keys = tuple(key for key, _ in contract.constructor_audit)
    if len(set(audit_keys)) != len(audit_keys):
        errors.append("duplicate_constructor_audit_key")
    if set(audit_keys) != set(REQUIRED_CONSTRUCTOR_AUDIT):
        missing = sorted(set(REQUIRED_CONSTRUCTOR_AUDIT) - set(audit_keys))
        extra = sorted(set(audit_keys) - set(REQUIRED_CONSTRUCTOR_AUDIT))
        errors.append(f"constructor_audit_mismatch:{missing}:{extra}")
    if any(not disposition.strip() for _, disposition in contract.constructor_audit):
        errors.append("empty_constructor_audit_disposition")
    return sorted(set(errors))


def refinement_admissibility(item: Refinement) -> tuple[bool, tuple[str, ...]]:
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


def freeze_candidate_class(contract: HistoryContract) -> dict[str, Any]:
    """Freeze the finite grammar without reading responses or target actions."""

    admitted: list[Refinement] = []
    excluded: list[dict[str, Any]] = []
    for item in contract.refinements:
        admissible, failures = refinement_admissibility(item)
        if admissible and item.cost <= contract.resource_budget:
            admitted.append(item)
        else:
            reasons = list(failures)
            if item.cost > contract.resource_budget:
                reasons.append("primitive_exceeds_resource_budget")
            excluded.append(
                {
                    "refinement_id": item.refinement_id,
                    "reasons": reasons,
                }
            )

    admitted.sort(key=lambda item: item.refinement_id)
    subsets: list[tuple[Refinement, ...]] = []
    for count in range(1, len(admitted) + 1):
        for subset in itertools.combinations(admitted, count):
            if sum(item.cost for item in subset) <= contract.resource_budget:
                subsets.append(subset)
    subsets.sort(
        key=lambda subset: (
            sum(item.cost for item in subset),
            len(subset),
            tuple(item.refinement_id for item in subset),
        )
    )

    frozen_payload = {
        "contract_id": contract.contract_id,
        "base_record": contract.base_record,
        "resource_budget": contract.resource_budget,
        "equality_rule": contract.equality_rule,
        "constructor_audit": contract.constructor_audit,
        "refinements": [
            {
                "refinement_id": item.refinement_id,
                "constructor": item.constructor,
                "record_labels": item.record_labels,
                "cost": item.cost,
                "formed": item.formed,
                "future_independent": item.future_independent,
                "accessible": item.accessible,
                "preserves_frame": item.preserves_frame,
                "target_independent_claim": item.target_independent_claim,
                "path_tags": item.path_tags,
                "certified_path_provenance": (
                    item.certified_path_provenance
                ),
                "certificate_kind": item.certificate_kind,
            }
            for item in contract.refinements
        ],
        "candidate_subsets": [
            tuple(item.refinement_id for item in subset) for subset in subsets
        ],
    }
    digest = hashlib.sha256(
        canonical_json(frozen_payload).encode("utf-8")
    ).hexdigest()
    return {
        "digest": digest,
        "selection_dependency": [
            "refinement metadata",
            "formed/future-independent/access/frame declarations",
            "resource budget",
            "base record",
            "constructor audit",
        ],
        "excluded_from_selection": [
            "response distributions",
            "target actions",
            "platform label",
        ],
        "admitted_primitive_ids": [
            item.refinement_id for item in admitted
        ],
        "excluded_primitives": excluded,
        "candidate_subsets": subsets,
        "frozen_payload": frozen_payload,
    }


def total_variation(left: Distribution, right: Distribution) -> Fraction:
    return sum(
        (abs(a - b) for a, b in zip(left, right, strict=True)),
        start=Fraction(0),
    ) / 2


def record_signatures(
    contract: HistoryContract, selected: Sequence[Refinement]
) -> tuple[tuple[str, ...], ...]:
    return tuple(
        (contract.base_record[index],)
        + tuple(item.record_labels[index] for item in selected)
        for index in range(len(contract.histories))
    )


def response_factorization(
    contract: HistoryContract, selected: Sequence[Refinement]
) -> dict[str, Any]:
    signatures = record_signatures(contract, selected)
    checked_pairs = 0
    maximum_gap = Fraction(0)
    maximum_witness: dict[str, Any] | None = None
    failures: list[dict[str, Any]] = []

    for left in range(len(contract.histories)):
        for right in range(left + 1, len(contract.histories)):
            if signatures[left] != signatures[right]:
                continue
            checked_pairs += 1
            for intervention_index, intervention in enumerate(
                contract.interventions
            ):
                left_distribution = contract.responses[intervention_index][left]
                right_distribution = contract.responses[intervention_index][right]
                gap = total_variation(left_distribution, right_distribution)
                if gap > maximum_gap:
                    score = tuple(
                        1 if a > b else -1 if a < b else 0
                        for a, b in zip(
                            left_distribution,
                            right_distribution,
                            strict=True,
                        )
                    )
                    maximum_gap = gap
                    maximum_witness = {
                        "left_history": contract.histories[left],
                        "right_history": contract.histories[right],
                        "intervention": intervention,
                        "complete_outcomes": contract.outcomes,
                        "left_distribution": left_distribution,
                        "right_distribution": right_distribution,
                        "total_variation_gap": gap,
                        "optimal_signed_score": score,
                        "signed_score_gap": 2 * gap,
                    }
                if gap != 0:
                    failures.append(
                        {
                            "left_history": contract.histories[left],
                            "right_history": contract.histories[right],
                            "intervention": intervention,
                            "total_variation_gap": gap,
                        }
                    )

    return {
        "factors": not failures,
        "equality_rule": contract.equality_rule,
        "record_class_count": len(set(signatures)),
        "same_record_pairs_checked": checked_pairs,
        "maximum_total_variation_gap": maximum_gap,
        "optimal_complete_outcome_witness": maximum_witness,
        "failure_count": len(failures),
    }


def path_conflict_graph(contract: HistoryContract) -> dict[str, Any]:
    """Find path identities that a zero-error task decoder must distinguish."""

    conflict_edges: set[tuple[int, int]] = set()
    within_path_conflicts: list[dict[str, Any]] = []
    for left_path in range(len(contract.paths)):
        for right_path in range(left_path, len(contract.paths)):
            for left_history in range(len(contract.histories)):
                for right_history in range(len(contract.histories)):
                    if (
                        contract.path_views[left_path][left_history]
                        != contract.path_views[right_path][right_history]
                    ):
                        continue
                    if (
                        contract.target_actions[left_history]
                        == contract.target_actions[right_history]
                    ):
                        continue
                    if left_path == right_path:
                        within_path_conflicts.append(
                            {
                                "path": contract.paths[left_path],
                                "view": contract.path_views[left_path][
                                    left_history
                                ],
                                "left_history": contract.histories[left_history],
                                "right_history": contract.histories[
                                    right_history
                                ],
                            }
                        )
                    else:
                        conflict_edges.add((left_path, right_path))

    coloring: tuple[int, ...] | None = None
    if not within_path_conflicts:
        path_count = len(contract.paths)
        for color_count in range(1, path_count + 1):
            for candidate in itertools.product(
                range(color_count), repeat=path_count
            ):
                if candidate[0] != 0:
                    continue
                if all(
                    candidate[left] != candidate[right]
                    for left, right in conflict_edges
                ):
                    coloring = candidate
                    break
            if coloring is not None:
                break

    return {
        "within_path_conflicts": within_path_conflicts,
        "conflict_edges": [
            (contract.paths[left], contract.paths[right])
            for left, right in sorted(conflict_edges)
        ],
        "path_only_provenance_can_suffice": not within_path_conflicts,
        "minimum_task_relative_provenance_alphabet": (
            None if coloring is None else max(coloring, default=0) + 1
        ),
        "one_minimal_path_coloring": (
            None
            if coloring is None
            else {
                contract.paths[index]: coloring[index]
                for index in range(len(contract.paths))
            }
        ),
    }


def path_equalizer(
    contract: HistoryContract, selected: Sequence[Refinement]
) -> dict[str, Any]:
    provenance_items = [
        item
        for item in selected
        if item.path_tags is not None and item.certified_path_provenance
    ]
    seen: dict[tuple[str, tuple[str, ...]], tuple[str, str, str]] = {}
    conflicts: list[dict[str, Any]] = []
    for path_index, path in enumerate(contract.paths):
        tags = tuple(
            item.path_tags[path_index]  # type: ignore[index]
            for item in provenance_items
        )
        for history_index, history in enumerate(contract.histories):
            view = contract.path_views[path_index][history_index]
            key = (view, tags)
            action = contract.target_actions[history_index]
            prior = seen.get(key)
            if prior is not None and prior[0] != action:
                conflicts.append(
                    {
                        "public_view": view,
                        "certified_path_tags": tags,
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

    noninjective_paths = []
    for path_index, path in enumerate(contract.paths):
        views = contract.path_views[path_index]
        if len(set(views)) < len(views):
            noninjective_paths.append(path)

    distinct_tag_tuples = {
        tuple(
            item.path_tags[path_index]  # type: ignore[index]
            for item in provenance_items
        )
        for path_index in range(len(contract.paths))
    }
    return {
        "factors": not conflicts,
        "comparison_maps_noninvertible": bool(noninjective_paths),
        "noninjective_paths": noninjective_paths,
        "selected_certified_path_provenance": [
            item.refinement_id for item in provenance_items
        ],
        "selected_path_provenance_alphabet": len(distinct_tag_tuples),
        "public_key_count": len(seen),
        "conflict_count": len(conflicts),
        "first_conflict": conflicts[0] if conflicts else None,
        "unrefined_task_relative_bound": path_conflict_graph(contract),
    }


def evaluate_candidate(
    contract: HistoryContract, selected: Sequence[Refinement]
) -> dict[str, Any]:
    response = response_factorization(contract, selected)
    path = path_equalizer(contract, selected)
    return {
        "refinement_ids": tuple(item.refinement_id for item in selected),
        "total_cost": sum(item.cost for item in selected),
        "response_factorization": response,
        "path_equalizer": path,
        "sufficient": response["factors"] and path["factors"],
    }


def failure_fingerprint(evaluation: dict[str, Any]) -> tuple[Any, ...]:
    response_witness = evaluation["response_factorization"][
        "optimal_complete_outcome_witness"
    ]
    path_witness = evaluation["path_equalizer"]["first_conflict"]
    if response_witness is not None:
        return (
            "response",
            response_witness["left_history"],
            response_witness["right_history"],
            response_witness["intervention"],
        )
    if path_witness is not None:
        return (
            "path",
            path_witness["public_view"],
            path_witness["left_path"],
            path_witness["right_path"],
        )
    return ("unknown",)


def compile_history_certificate(contract: HistoryContract) -> dict[str, Any]:
    errors = validate_contract(contract)
    if errors:
        return {
            "schema": "dynamic-unity/noninvertible-history-certificate/v0.1",
            "contract_id": contract.contract_id,
            "platform_label": contract.platform_label,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": errors,
            "platform_label_used_by_decision": False,
        }

    frozen_class = freeze_candidate_class(contract)
    if not frozen_class["candidate_subsets"]:
        return {
            "schema": "dynamic-unity/noninvertible-history-certificate/v0.1",
            "contract_id": contract.contract_id,
            "platform_label": contract.platform_label,
            "verdict": "INCOMPLETE_CONTRACT",
            "errors": ["empty_nonbase_admissible_refinement_class"],
            "frozen_class": {
                key: value
                for key, value in frozen_class.items()
                if key not in {"candidate_subsets", "frozen_payload"}
            },
            "platform_label_used_by_decision": False,
        }

    base = evaluate_candidate(contract, ())
    evaluations = [
        evaluate_candidate(contract, subset)
        for subset in frozen_class["candidate_subsets"]
    ]
    common = {
        "schema": "dynamic-unity/noninvertible-history-certificate/v0.1",
        "contract_id": contract.contract_id,
        "platform_label": contract.platform_label,
        "platform_label_used_by_decision": False,
        "class_scope": (
            "finite frozen formed/future-independent/access- and "
            "resource-bounded candidate grammar"
        ),
        "frozen_class_digest": frozen_class["digest"],
        "frozen_class": {
            "selection_dependency": frozen_class["selection_dependency"],
            "excluded_from_selection": frozen_class["excluded_from_selection"],
            "admitted_primitive_ids": frozen_class["admitted_primitive_ids"],
            "excluded_primitives": frozen_class["excluded_primitives"],
            "candidate_subset_ids": [
                tuple(item.refinement_id for item in subset)
                for subset in frozen_class["candidate_subsets"]
            ],
            "candidate_count": len(frozen_class["candidate_subsets"]),
        },
        "base_evaluation": base,
        "candidate_evaluations": evaluations,
    }

    if base["sufficient"]:
        return {
            **common,
            "verdict": "FACTORIZATION",
            "certificate": {
                "record": "base",
                "response_factorization": base["response_factorization"],
                "path_equalizer": base["path_equalizer"],
            },
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
        selection_key = (
            selected["total_cost"],
            len(selected["refinement_ids"]),
            selected["refinement_ids"],
        )
        checked_before = [
            item
            for item in evaluations
            if (
                item["total_cost"],
                len(item["refinement_ids"]),
                item["refinement_ids"],
            )
            < selection_key
        ]
        return {
            **common,
            "verdict": "MINIMAL_REFINEMENT",
            "certificate": {
                "optimizer": (
                    "minimum(total_cost, primitive_count, "
                    "lexicographic_refinement_ids)"
                ),
                "selected": selected,
                "strictly_prior_candidates_checked": len(checked_before),
                "strictly_prior_candidates_all_fail": all(
                    not item["sufficient"] for item in checked_before
                ),
                "interpretation": (
                    "formed candidate provenance absorbs the base witness; "
                    "no class-relative remainder"
                ),
            },
        }

    fingerprints = [failure_fingerprint(item) for item in evaluations]
    uniform = len(set(fingerprints)) == 1
    return {
        **common,
        "verdict": "CANDIDATE_REMAINDER",
        "certificate": {
            "finite_class_exhausted": True,
            "candidate_count": len(evaluations),
            "uniform_witness_across_class": uniform,
            "uniform_witness_fingerprint": (
                fingerprints[0] if uniform else None
            ),
            "per_candidate_failure_fingerprints": fingerprints,
            "interpretation": (
                "candidate remainder relative only to this frozen finite "
                "class; not an irreducible physical remainder"
            ),
        },
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


def quantum_like_contract() -> HistoryContract:
    histories = (
        "plus_history_a",
        "plus_history_b",
        "minus_history_a",
        "minus_history_b",
    )
    return HistoryContract(
        contract_id="QF-ROUTE-EXACT-RATIONAL-01",
        platform_label="noisy_quantum_like_coherent_route",
        histories=histories,
        interventions=("ordinary_channel", "coherent_recombination_X"),
        outcomes=("port_0", "port_1"),
        base_record=("same_reduced_endpoint",) * len(histories),
        responses=(
            (
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
            ),
            (
                (Fraction(9, 10), Fraction(1, 10)),
                (Fraction(9, 10), Fraction(1, 10)),
                (Fraction(1, 10), Fraction(9, 10)),
                (Fraction(1, 10), Fraction(9, 10)),
            ),
        ),
        target_actions=("preserve", "preserve", "phase_correct", "phase_correct"),
        paths=("direct_route", "relay_route"),
        path_views=(
            ("bright", "bright", "dark", "dark"),
            ("dark", "dark", "bright", "bright"),
        ),
        refinements=(
            Refinement(
                refinement_id="certified_route_id",
                constructor="routed_implementation",
                record_labels=("route_agnostic",) * len(histories),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                path_tags=("direct", "relay"),
                certified_path_provenance=True,
                certificate_kind="formed_route_register",
            ),
            Refinement(
                refinement_id="duplicate_endpoint_copy",
                constructor="resource",
                record_labels=("copy",) * len(histories),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="redundant_endpoint_copy",
            ),
            Refinement(
                refinement_id="formed_recombination_port",
                constructor="alternative_record_instrument",
                record_labels=("plus", "plus", "minus", "minus"),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="signed_all_port_history_record",
            ),
            Refinement(
                refinement_id="stage_zero_future_oracle",
                constructor="fixed_future_correlated_oracle",
                record_labels=("plus", "plus", "minus", "minus"),
                cost=1,
                formed=True,
                future_independent=False,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="precorrelated_disclosure_tree",
            ),
        ),
        resource_budget=2,
        equality_rule="exact_rational_stochastic_signature",
        tolerance=Fraction(0),
        constructor_audit=constructor_audit(
            {
                "seed": "fixed before responses; no target-derived seed admitted",
                "resource": "two-unit refinement budget frozen",
                "history": "formed_recombination_port admitted",
                "provenance": "certified_route_id admitted",
                "fixed_future_correlated_oracle": (
                    "constructed then excluded for failed future-independence"
                ),
                "routed_implementation": "certified_route_id admitted",
                "alternative_record_instrument": (
                    "formed_recombination_port admitted"
                ),
            }
        ),
    )


def distributed_contract() -> HistoryContract:
    histories = (
        "serializable_history_a",
        "serializable_history_b",
        "equivocating_history_a",
        "equivocating_history_b",
    )
    return HistoryContract(
        contract_id="DF-AUTHENTICATED-HISTORY-01",
        platform_label="authenticated_distributed_history",
        histories=histories,
        interventions=("ordinary_materialized_read", "audit_challenge"),
        outcomes=("accept_signal", "reject_signal"),
        base_record=("same_materialized_endpoint",) * len(histories),
        responses=(
            (
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
            ),
            (
                (Fraction(19, 20), Fraction(1, 20)),
                (Fraction(19, 20), Fraction(1, 20)),
                (Fraction(1, 5), Fraction(4, 5)),
                (Fraction(1, 5), Fraction(4, 5)),
            ),
        ),
        target_actions=("commit", "commit", "abort", "abort"),
        paths=("leaderless_gossip_layer", "bft_hardening_layer"),
        path_views=(
            ("green", "green", "red", "red"),
            ("red", "red", "green", "green"),
        ),
        refinements=(
            Refinement(
                refinement_id="authenticated_layer_id",
                constructor="routed_implementation",
                record_labels=("layer_agnostic",) * len(histories),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                path_tags=("gossip", "bft"),
                certified_path_provenance=True,
                certificate_kind="threshold_authenticated_layer_record",
            ),
            Refinement(
                refinement_id="authenticated_operation_dag",
                constructor="history",
                record_labels=(
                    "serializable",
                    "serializable",
                    "equivocation",
                    "equivocation",
                ),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="threshold_signed_operation_provenance",
            ),
            Refinement(
                refinement_id="replicated_endpoint_copy",
                constructor="resource",
                record_labels=("copy",) * len(histories),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="replicated_terminal_value",
            ),
            Refinement(
                refinement_id="adaptive_target_decoder",
                constructor="decoder_observer_boundary",
                record_labels=(
                    "serializable",
                    "serializable",
                    "equivocation",
                    "equivocation",
                ),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=False,
                certificate_kind="target_fitted_decoder",
            ),
        ),
        resource_budget=2,
        equality_rule="exact_rational_stochastic_signature",
        tolerance=Fraction(0),
        constructor_audit=constructor_audit(
            {
                "boundary": "validator/read boundary frozen",
                "resource": "two-unit refinement budget frozen",
                "history": "authenticated_operation_dag admitted",
                "provenance": (
                    "threshold-signed operation and layer records admitted"
                ),
                "routed_implementation": "authenticated_layer_id admitted",
                "adaptive_controller_scheduler": (
                    "considered; no adaptive candidate admitted"
                ),
                "decoder_observer_boundary": (
                    "target-fitted decoder constructed then excluded"
                ),
            }
        ),
    )


def branch_contract(
    contract_id: str,
    response_gap: bool,
    repair_available: bool,
) -> HistoryContract:
    response = (
        (Fraction(1), Fraction(0)),
        (
            (Fraction(0), Fraction(1))
            if response_gap
            else (Fraction(1), Fraction(0))
        ),
    )
    refinements: tuple[Refinement, ...]
    if repair_available:
        labels = ("left", "right") if response_gap else ("same", "same")
        refinements = (
            Refinement(
                refinement_id="formed_branch_record",
                constructor="history",
                record_labels=labels,
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="branch_test",
            ),
        )
    else:
        refinements = (
            Refinement(
                refinement_id="uninformative_formed_copy",
                constructor="resource",
                record_labels=("same", "same"),
                cost=1,
                formed=True,
                future_independent=True,
                accessible=True,
                preserves_frame=True,
                target_independent_claim=True,
                certificate_kind="branch_test",
            ),
        )
    return HistoryContract(
        contract_id=contract_id,
        platform_label="synthetic_branch_control",
        histories=("left", "right"),
        interventions=("test",),
        outcomes=("zero", "one"),
        base_record=("same", "same"),
        responses=((response[0], response[1]),),
        target_actions=("act", "act"),
        paths=("only_path",),
        path_views=(("public", "public"),),
        refinements=refinements,
        resource_budget=1,
        equality_rule="exact_rational_stochastic_signature",
        tolerance=Fraction(0),
        constructor_audit=constructor_audit(),
    )


def run() -> dict[str, Any]:
    quantum = quantum_like_contract()
    distributed = distributed_contract()
    quantum_result = compile_history_certificate(quantum)
    distributed_result = compile_history_certificate(distributed)

    factorization_result = compile_history_certificate(
        branch_contract(
            "BRANCH-FACTORIZATION", response_gap=False, repair_available=True
        )
    )
    refinement_result = compile_history_certificate(
        branch_contract(
            "BRANCH-MINIMAL-REFINEMENT",
            response_gap=True,
            repair_available=True,
        )
    )
    remainder_result = compile_history_certificate(
        branch_contract(
            "BRANCH-CANDIDATE-REMAINDER",
            response_gap=True,
            repair_available=False,
        )
    )
    incomplete_contract = replace(
        branch_contract(
            "BRANCH-INCOMPLETE", response_gap=True, repair_available=True
        ),
        refinements=(),
    )
    incomplete_result = compile_history_certificate(incomplete_contract)

    quantum_target_flip = replace(
        quantum,
        target_actions=("alpha", "beta", "alpha", "beta"),
    )
    quantum_class_original = freeze_candidate_class(quantum)
    quantum_class_flipped = freeze_candidate_class(quantum_target_flip)

    swapped_quantum = compile_history_certificate(
        replace(quantum, platform_label="arbitrary_metadata_label")
    )
    swapped_distributed = compile_history_certificate(
        replace(distributed, platform_label="arbitrary_metadata_label")
    )

    checks = [
        {
            "id": "compiler_exercises_all_four_verdicts",
            "pass": (
                factorization_result["verdict"],
                refinement_result["verdict"],
                remainder_result["verdict"],
                incomplete_result["verdict"],
            )
            == (
                "FACTORIZATION",
                "MINIMAL_REFINEMENT",
                "CANDIDATE_REMAINDER",
                "INCOMPLETE_CONTRACT",
            ),
        },
        {
            "id": "candidate_grammar_is_target_independent_in_implementation",
            "pass": (
                quantum_class_original["digest"]
                == quantum_class_flipped["digest"]
                and quantum_class_original["frozen_payload"]
                == quantum_class_flipped["frozen_payload"]
            ),
            "digest": quantum_class_original["digest"],
        },
        {
            "id": "platform_label_is_not_a_decision_input",
            "pass": (
                quantum_result["verdict"] == swapped_quantum["verdict"]
                and quantum_result["frozen_class_digest"]
                == swapped_quantum["frozen_class_digest"]
                and distributed_result["verdict"]
                == swapped_distributed["verdict"]
                and distributed_result["frozen_class_digest"]
                == swapped_distributed["frozen_class_digest"]
            ),
        },
        {
            "id": "quantum_like_fixture_uses_noninvertible_paths",
            "pass": quantum_result["base_evaluation"]["path_equalizer"][
                "comparison_maps_noninvertible"
            ],
        },
        {
            "id": "distributed_fixture_uses_noninvertible_paths",
            "pass": distributed_result["base_evaluation"]["path_equalizer"][
                "comparison_maps_noninvertible"
            ],
        },
        {
            "id": "quantum_like_witness_absorbed_by_formed_provenance",
            "pass": (
                quantum_result["verdict"] == "MINIMAL_REFINEMENT"
                and set(
                    quantum_result["certificate"]["selected"][
                        "refinement_ids"
                    ]
                )
                == {"formed_recombination_port", "certified_route_id"}
                and quantum_result["certificate"]["selected"]["total_cost"] == 2
            ),
        },
        {
            "id": "authenticated_distributed_witness_absorbed_by_provenance",
            "pass": (
                distributed_result["verdict"] == "MINIMAL_REFINEMENT"
                and set(
                    distributed_result["certificate"]["selected"][
                        "refinement_ids"
                    ]
                )
                == {
                    "authenticated_operation_dag",
                    "authenticated_layer_id",
                }
                and distributed_result["certificate"]["selected"][
                    "total_cost"
                ]
                == 2
            ),
        },
        {
            "id": "fixed_oracle_and_target_decoder_are_excluded",
            "pass": (
                {
                    item["refinement_id"]
                    for item in quantum_result["frozen_class"][
                        "excluded_primitives"
                    ]
                }
                == {"stage_zero_future_oracle"}
                and {
                    item["refinement_id"]
                    for item in distributed_result["frozen_class"][
                        "excluded_primitives"
                    ]
                }
                == {"adaptive_target_decoder"}
            ),
        },
        {
            "id": "complete_outcome_scores_expose_positive_base_gaps",
            "pass": (
                quantum_result["base_evaluation"]["response_factorization"][
                    "maximum_total_variation_gap"
                ]
                == Fraction(4, 5)
                and distributed_result["base_evaluation"][
                    "response_factorization"
                ]["maximum_total_variation_gap"]
                == Fraction(3, 4)
            ),
        },
        {
            "id": "both_fixtures_need_two_path_provenance_values",
            "pass": (
                quantum_result["base_evaluation"]["path_equalizer"][
                    "unrefined_task_relative_bound"
                ]["minimum_task_relative_provenance_alphabet"]
                == 2
                and distributed_result["base_evaluation"]["path_equalizer"][
                    "unrefined_task_relative_bound"
                ]["minimum_task_relative_provenance_alphabet"]
                == 2
            ),
        },
        {
            "id": "nonzero_tolerance_is_rejected_without_closure_rule",
            "pass": compile_history_certificate(
                replace(
                    quantum,
                    contract_id="QF-UNSAFE-TOLERANCE-CONTROL",
                    tolerance=Fraction(1, 100),
                )
            )["verdict"]
            == "INCOMPLETE_CONTRACT",
        },
    ]

    result = {
        "schema": (
            "dynamic-unity/noninvertible-history-certificate-compiler-probe/v0.1"
        ),
        "candidate_ids": ["HC-DU-034B", "HC-DU-036B", "H-CCR-13", "H-CCR-14"],
        "claim_grade": (
            "EXACT FINITE RATIONAL SOFTWARE/FORMAL PILOT / "
            "TARGET-INDEPENDENT GRAMMAR AND TARGET-DEPENDENT SELECTION "
            "SEPARATED / PHYSICAL TRANSFER AND NOVELTY OPEN"
        ),
        "checks_passed": sum(int(check["pass"]) for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "fixture_results": {
            "noisy_quantum_like": quantum_result,
            "authenticated_distributed": distributed_result,
        },
        "branch_controls": {
            "factorization": factorization_result,
            "minimal_refinement": refinement_result,
            "candidate_remainder": remainder_result,
            "incomplete_contract": incomplete_result,
        },
        "verdict": (
            "FINITE COMPILER KERNEL VIABLE / BOTH CROSS-PLATFORM "
            "WITNESSES ABSORBED BY FORMED PROVENANCE / "
            "NO CLASS-RELATIVE REMAINDER IN EITHER FOCAL FIXTURE"
        ),
        "not_established": [
            "physical record selection",
            "complete physically legitimate refinement class",
            "irreducible physical remainder",
            "quantum/distributed physical identity",
            "approximate/noisy quotient theorem",
            "robust calibration or finite-shot guarantee",
            "public objectivity or finality law",
            "novel publishable theorem",
            "record-first ontology",
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
        f"{result['checks_passed']}/{result['checks_total']} checks pass\n"
        f"VERDICT: {result['verdict']}\n"
        f"artifact={ARTIFACT}"
    )
    if result["checks_passed"] != result["checks_total"]:
        failed = [
            check["id"] for check in result["checks"] if not check["pass"]
        ]
        raise SystemExit(f"failed checks: {failed}")


if __name__ == "__main__":
    main()
