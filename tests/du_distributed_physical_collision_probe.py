#!/usr/bin/env python3
"""Exact regression certificate for N5-SCF-P5 / HC-DU-051.

The analytic result lives in:
  explorations/distributed-physical-record-collision-and-portfolio-handoff-2026-07-27.md

This script is deliberately not a network, gauge-theory, quantum, consensus,
cryptographic, or hardware simulator.  It exhausts the finite fibres and
probability formulas used by the proof:

* a source-bound gauge record versus a preloaded/null record with the same
  visible alphabet;
* independent archive corruption versus common-shock copies;
* boundary-action closure versus interior/crossing/formation first leaks;
* receiver-contextual physical handoff;
* protocol authentication versus causal physical source binding; and
* the unchanged closed metastable-host obstruction.
"""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Callable, Hashable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_distributed_physical_collision_result.json"
)

CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def factorizes(
    rows: Iterable[Mapping[str, object]],
    view: Callable[[Mapping[str, object]], Hashable],
    target: Callable[[Mapping[str, object]], Hashable],
) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for row in rows:
        key = view(row)
        value = target(row)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def partition(
    rows: Sequence[Mapping[str, object]],
    view: Callable[[Mapping[str, object]], Hashable],
) -> tuple[frozenset[int], ...]:
    blocks: dict[Hashable, set[int]] = defaultdict(set)
    for index, row in enumerate(rows):
        blocks[view(row)].add(index)
    return tuple(
        sorted(
            (frozenset(block) for block in blocks.values()),
            key=lambda block: (min(block), len(block)),
        )
    )


def strictly_refines(
    fine: tuple[frozenset[int], ...],
    coarse: tuple[frozenset[int], ...],
) -> bool:
    return (
        len(fine) > len(coarse)
        and all(any(block <= parent for parent in coarse) for block in fine)
    )


def weighted_distribution(
    rows: Sequence[Mapping[str, object]],
    weights: Sequence[Fraction],
    observable: Callable[[Mapping[str, object]], Hashable],
) -> dict[str, str]:
    out: dict[Hashable, Fraction] = defaultdict(Fraction)
    for row, weight in zip(rows, weights, strict=True):
        out[observable(row)] += weight
    return {
        repr(key): fraction_text(value)
        for key, value in sorted(out.items(), key=lambda item: repr(item[0]))
    }


def majority_error(n: int, p: Fraction) -> Fraction:
    assert n % 2 == 1
    threshold = n // 2 + 1
    return sum(
        Fraction(comb(n, failures))
        * p**failures
        * (1 - p) ** (n - failures)
        for failures in range(threshold, n + 1)
    )


def majority(values: tuple[int, ...]) -> int:
    counts = {value: values.count(value) for value in set(values)}
    return min(
        (value for value, count in counts.items() if count == max(counts.values())),
        default=-1,
    )


# ---------------------------------------------------------------------------
# 1. Physical formation is a relation, not a visible-value distribution.
# ---------------------------------------------------------------------------

formed_rows = tuple(
    {"world": "formed", "target_flux": flux, "record_flux": flux}
    for flux in range(3)
)
null_rows = tuple(
    {
        "world": "preloaded_null",
        "target_flux": flux,
        "record_flux": record_flux,
    }
    for flux in range(3)
    for record_flux in range(3)
)

formed_record_law = weighted_distribution(
    formed_rows,
    (Fraction(1, 3),) * 3,
    lambda row: row["record_flux"],
)
null_record_law = weighted_distribution(
    null_rows,
    (Fraction(1, 9),) * 9,
    lambda row: row["record_flux"],
)

record(
    "formed_and_preloaded_worlds_have_the_same_visible_record_marginal",
    formed_record_law == null_record_law,
    formed_record_law,
)
record(
    "formed_gauge_record_exactly_reconstructs_boundary_flux",
    factorizes(
        formed_rows,
        lambda row: row["record_flux"],
        lambda row: row["target_flux"],
    ),
    "the frozen QND formation relation is target-sensitive",
)
record(
    "preloaded_null_record_does_not_reconstruct_boundary_flux",
    not factorizes(
        null_rows,
        lambda row: row["record_flux"],
        lambda row: row["target_flux"],
    ),
    "the same record alphabet and marginal can be physically unbound",
)


def signed_record(record_flux: int) -> tuple[str, int, int]:
    # A deterministic stand-in for any ideal authenticator over the declared
    # value.  The proof uses only that it is a function of that value.
    return ("valid", record_flux, (17 * record_flux + 5) % 19)


record(
    "signed_artifact_laws_match_when_visible_record_laws_match",
    weighted_distribution(
        formed_rows,
        (Fraction(1, 3),) * 3,
        lambda row: signed_record(int(row["record_flux"])),
    )
    == weighted_distribution(
        null_rows,
        (Fraction(1, 9),) * 9,
        lambda row: signed_record(int(row["record_flux"])),
    ),
    "authentication of the declared value does not identify its physical formation",
)

matched_provenance_rows = tuple(
    {
        "formation": formation,
        "target_flux": flux,
        "record_flux": flux,
        "certificate": signed_record(flux),
    }
    for flux in range(3)
    for formation in ("qnd_formed", "preloaded")
)
record(
    "terminal_certificate_does_not_reconstruct_physical_formation_mode",
    not factorizes(
        matched_provenance_rows,
        lambda row: row["certificate"],
        lambda row: row["formation"],
    ),
    "same value and signature, different causal source relation",
)
record(
    "adding_a_formed_coupling_witness_repairs_provenance_only_by_expanding_the_record",
    factorizes(
        matched_provenance_rows,
        lambda row: (row["certificate"], row["formation"]),
        lambda row: row["formation"],
    ),
    "the repair is an additional physical meta-record, not more hashing",
)


# ---------------------------------------------------------------------------
# 2. Material gauge record: action-relative exactness and first leaks.
# ---------------------------------------------------------------------------

gauge_states = tuple(
    {
        "n1": n1,
        "n2": n2,
        "flux": n1 + n2,
        "archive_flux": n1 + n2,
    }
    for n1, n2 in ((0, 0), (0, 1), (1, 0), (1, 1))
)

record(
    "gauss_boundary_record_is_exact_for_boundary_flux_action",
    factorizes(
        gauge_states,
        lambda row: row["archive_flux"],
        lambda row: row["flux"],
    ),
    "ker(record) is contained in ker(boundary action)",
)
record(
    "same_complete_boundary_record_retains_interior_remainder",
    not factorizes(
        gauge_states,
        lambda row: row["archive_flux"],
        lambda row: row["n1"],
    ),
    "(n1,n2)=(0,1) and (1,0) share flux one",
)

boundary_partition = partition(gauge_states, lambda row: row["archive_flux"])
interior_partition = partition(
    gauge_states, lambda row: (row["archive_flux"], row["n1"])
)
record(
    "interior_capability_strictly_refines_boundary_action_equivalence",
    strictly_refines(interior_partition, boundary_partition),
    {
        "boundary_classes": len(boundary_partition),
        "interior_classes": len(interior_partition),
    },
)

formation_history_rows = tuple(
    {
        "flux": flux,
        "archive_flux": flux,
        "microscopic_path": path,
    }
    for flux in range(3)
    for path in ("hamiltonian_log_branch_a", "hamiltonian_log_branch_b")
)
record(
    "terminal_flux_archive_does_not_reconstruct_microscopic_write_history",
    not factorizes(
        formation_history_rows,
        lambda row: row["archive_flux"],
        lambda row: row["microscopic_path"],
    ),
    "equal final instruments admit distinct intermediate dynamics",
)


# ---------------------------------------------------------------------------
# 3. Reliability amplification is not source-information creation.
# ---------------------------------------------------------------------------

p = Fraction(1, 10)
odd_sizes = (1, 3, 5, 7, 9)
independent_error_curve = {n: majority_error(n, p) for n in odd_sizes}
common_shock_curve = {n: p for n in odd_sizes}

record(
    "independent_archive_errors_amplify_reliability_across_a_size_family",
    all(
        independent_error_curve[right] < independent_error_curve[left]
        for left, right in zip(odd_sizes, odd_sizes[1:])
    ),
    {str(n): fraction_text(error) for n, error in independent_error_curve.items()},
)
record(
    "common_shock_replication_has_no_reliability_scaling_gain",
    len(set(common_shock_curve.values())) == 1,
    {str(n): fraction_text(error) for n, error in common_shock_curve.items()},
)
record(
    "three_independent_cells_beat_one_cell_but_remain_inexact",
    Fraction(0) < independent_error_curve[3] < p,
    {
        "single_cell": fraction_text(p),
        "three_cell_majority": fraction_text(independent_error_curve[3]),
    },
)

independent_noise_rows = tuple(
    {
        "flux": flux,
        "errors": errors,
        "copies": tuple((flux + error) % 3 for error in errors),
    }
    for flux in range(3)
    for errors in itertools.product(range(3), repeat=3)
)
record(
    "finite_full_support_archive_noise_does_not_exactly_identify_flux",
    not factorizes(
        independent_noise_rows,
        lambda row: row["copies"],
        lambda row: row["flux"],
    ),
    "all-zero copies can arise from flux zero/no errors or flux two/all errors",
)
record(
    "majority_hardening_does_not_repair_exact_support_factorization",
    not factorizes(
        independent_noise_rows,
        lambda row: majority(tuple(row["copies"])),
        lambda row: row["flux"],
    ),
    "lower decision risk is not exact reconstructibility",
)

ideal_copy_rows = tuple(
    {
        **row,
        "copies": (row["archive_flux"],) * 5,
    }
    for row in gauge_states
)
record(
    "ideal_redundant_copies_preserve_exact_boundary_flux",
    factorizes(
        ideal_copy_rows,
        lambda row: row["copies"],
        lambda row: row["flux"],
    ),
    "copying preserves the distinction already in the formed source record",
)
record(
    "ideal_redundant_copies_do_not_reconstruct_interior_charge",
    not factorizes(
        ideal_copy_rows,
        lambda row: row["copies"],
        lambda row: row["n1"],
    ),
    "no number of downstream copies splits a source-record fibre",
)

noisy_interior_rows = tuple(
    {
        **row,
        "errors": errors,
        "copies": tuple((int(row["archive_flux"]) + error) % 3 for error in errors),
    }
    for row in gauge_states
    for errors in itertools.product((0, 1), repeat=3)
)
record(
    "independently_corrupted_copies_are_not_independent_physical_sources",
    not factorizes(
        noisy_interior_rows,
        lambda row: row["copies"],
        lambda row: row["n1"],
    ),
    "independent channel failures remain downstream of one common flux record",
)


# ---------------------------------------------------------------------------
# 4. Physical handoff is receiver-contextual and capability-relative.
# ---------------------------------------------------------------------------

handoff_rows: list[dict[str, object]] = []
for archive_flux in range(3):
    for available, epoch_current, orientation_aligned, boundary_preserving in (
        itertools.product((False, True), repeat=4)
    ):
        handoff_rows.append(
            {
                "archive_flux": archive_flux,
                "current_flux": (
                    archive_flux
                    if boundary_preserving
                    else (archive_flux + 1) % 3
                ),
                "available": available,
                "epoch_current": epoch_current,
                "orientation_aligned": orientation_aligned,
                "boundary_preserving": boundary_preserving,
            }
        )


def physical_handoff_action(row: Mapping[str, object]) -> Hashable:
    if not row["available"]:
        return "WAIT_FOR_EVIDENCE"
    if not row["epoch_current"]:
        return "REJECT_STALE_EPOCH"
    if not row["orientation_aligned"]:
        return "RECALIBRATE_ORIENTATION"
    if not row["boundary_preserving"]:
        return "REFRESH_AFTER_CROSSING"
    return ("ACT_ON_CURRENT_FLUX", row["archive_flux"])


handoff_fields = (
    "archive_flux",
    "available",
    "epoch_current",
    "orientation_aligned",
    "boundary_preserving",
)


def fields_view(fields: tuple[str, ...]) -> Callable[[Mapping[str, object]], tuple]:
    return lambda row: tuple(row[field] for field in fields)


record(
    "physical_handoff_factors_through_export_plus_receiver_context",
    factorizes(handoff_rows, fields_view(handoff_fields), physical_handoff_action),
    handoff_fields,
)
record(
    "archive_value_alone_is_not_a_safe_current_action_handoff",
    not factorizes(
        handoff_rows,
        fields_view(("archive_flux",)),
        physical_handoff_action,
    ),
    "availability, epoch, orientation, and action envelope remain live",
)

omitted_handoff_fields = {
    omitted: factorizes(
        handoff_rows,
        fields_view(tuple(field for field in handoff_fields if field != omitted)),
        physical_handoff_action,
    )
    for omitted in handoff_fields
}
record(
    "every_frozen_handoff_field_has_an_exact_first_failure",
    not any(omitted_handoff_fields.values()),
    omitted_handoff_fields,
)
record(
    "old_archive_remains_exact_for_historical_flux",
    factorizes(
        handoff_rows,
        lambda row: row["archive_flux"],
        lambda row: row["archive_flux"],
    ),
    "durable historical truth is typed separately from current-state sufficiency",
)
record(
    "old_archive_does_not_reconstruct_current_flux_across_crossing",
    not factorizes(
        handoff_rows,
        lambda row: row["archive_flux"],
        lambda row: row["current_flux"],
    ),
    "same historical archive, different current enclosed charge",
)
safe_handoff_rows = tuple(
    row
    for row in handoff_rows
    if row["available"]
    and row["epoch_current"]
    and row["orientation_aligned"]
    and row["boundary_preserving"]
)
record(
    "current_flux_closes_inside_the_frozen_safe_envelope",
    factorizes(
        safe_handoff_rows,
        lambda row: row["archive_flux"],
        lambda row: row["current_flux"],
    ),
    "the scoped finality statement is exact once all premises hold",
)


# ---------------------------------------------------------------------------
# 5. Hardening can enable an action without adjudicating physical truth.
# ---------------------------------------------------------------------------

authority_rows = tuple(
    {
        "formation": formation,
        "record_flux": flux,
        "certificate": signed_record(flux),
        "quorum_valid": True,
    }
    for formation in ("qnd_formed", "preloaded")
    for flux in range(3)
)


def conflict_safe_execution(row: Mapping[str, object]) -> Hashable:
    return ("EXECUTE", row["record_flux"]) if row["quorum_valid"] else "WAIT"


record(
    "hardened_certificate_is_sufficient_for_declared_execution",
    factorizes(
        authority_rows,
        lambda row: (row["certificate"], row["quorum_valid"]),
        conflict_safe_execution,
    ),
    "protocol action closure is real inside the supplied validity/authority rule",
)
record(
    "same_hardened_certificate_does_not_adjudicate_physical_source_binding",
    not factorizes(
        authority_rows,
        lambda row: (row["certificate"], row["quorum_valid"]),
        lambda row: row["formation"],
    ),
    "authority and physical formation are different targets",
)
record(
    "verification_without_disclosure_does_not_change_the_source_fibre",
    not factorizes(
        authority_rows,
        lambda row: ("proved_valid_record", row["quorum_valid"]),
        lambda row: row["formation"],
    ),
    "a proof of the declared relation cannot attest an omitted physical relation",
)


# ---------------------------------------------------------------------------
# 5b. MMO dual-mesh control: representation is not action authority.
# ---------------------------------------------------------------------------

dual_mesh_rows = (
    {
        "render_mesh": "wall-visible-v7",
        "collision_mesh": "solid-wall-v7",
        "render_signature": ("signed", "wall-visible-v7"),
        "collision_response": "BLOCK",
    },
    {
        "render_mesh": "wall-visible-v7",
        "collision_mesh": "ghost-wall-v7",
        "render_signature": ("signed", "wall-visible-v7"),
        "collision_response": "PASS",
    },
)
record(
    "signed_render_mesh_exactly_identifies_the_delivered_representation",
    factorizes(
        dual_mesh_rows,
        lambda row: row["render_signature"],
        lambda row: row["render_mesh"],
    ),
    "representation provenance can be exact on its own target",
)
record(
    "signed_render_mesh_does_not_identify_collision_capability",
    not factorizes(
        dual_mesh_rows,
        lambda row: row["render_signature"],
        lambda row: row["collision_response"],
    ),
    "identical visible asset, BLOCK versus PASS",
)
record(
    "authoritative_dual_mesh_binding_repairs_action_by_expanding_the_handoff",
    factorizes(
        dual_mesh_rows,
        lambda row: (row["render_signature"], row["collision_mesh"]),
        lambda row: row["collision_response"],
    ),
    "the repair binds the action surface; it is not a stronger signature over render alone",
)


# ---------------------------------------------------------------------------
# 6. Mandatory hostile control: the metastable host stays closed.
# ---------------------------------------------------------------------------

host_rows = (
    {
        "history": "",
        "endpoint": "x1",
        "occurrence": 0,
        "next_branch": ("C", "x2"),
        "visible_token": "",
        "hidden_token": "",
    },
    {
        "history": "CWCW",
        "endpoint": "x1",
        "occurrence": 1,
        "next_branch": ("C", "x2"),
        "visible_token": "CWCW",
        "hidden_token": "CWCW",
    },
)
record(
    "metastable_endpoint_preserves_markov_operational_closure",
    factorizes(
        host_rows,
        lambda row: row["endpoint"],
        lambda row: row["next_branch"],
    ),
    "the positive endpoint-action control survives",
)
record(
    "metastable_endpoint_does_not_reconstruct_historical_occurrence",
    not factorizes(
        host_rows,
        lambda row: row["endpoint"],
        lambda row: row["occurrence"],
    ),
    "empty history and CWCW share endpoint x1",
)
record(
    "replication_signing_and_hardening_of_endpoint_do_not_repair_occurrence",
    not factorizes(
        host_rows,
        lambda row: (
            (row["endpoint"],) * 7,
            signed_record(1),
            "valid-quorum",
        ),
        lambda row: row["occurrence"],
    ),
    "every downstream artifact is constant on the adverse endpoint fibre",
)
record(
    "full_history_token_repairs_occurrence_only_by_injective_access",
    factorizes(
        host_rows,
        lambda row: row["history"],
        lambda row: row["occurrence"],
    )
    and len({row["history"] for row in host_rows}) == len(host_rows),
    "the mandatory hostile repair is full-history tomography on this witness",
)

archive_location_rows = (
    {
        "host_antecedent": ("four_state_cycle", "same_reduced_law"),
        "archive_location": "accessible_A",
    },
    {
        "host_antecedent": ("four_state_cycle", "same_reduced_law"),
        "archive_location": "hidden_H",
    },
)
record(
    "unchanged_host_antecedent_does_not_select_archive_location",
    not factorizes(
        archive_location_rows,
        lambda row: row["host_antecedent"],
        lambda row: row["archive_location"],
    ),
    "HC-DU-046 archive-relocation obstruction remains intact",
)


# ---------------------------------------------------------------------------
# 7. Typed translation verdict and portfolio handoff.
# ---------------------------------------------------------------------------

translation = {
    "source_sensitive_joint_input": {
        "distributed": "source-bound complementary participant evidence",
        "physical": "QND boundary-flux formation relation",
        "verdict": "SCOPED_CORRESPONDENCE",
    },
    "reliability_amplification": {
        "distributed": "independent evidence concentration under frozen dependence",
        "physical": "independent archive-cell corruption plus majority decoding",
        "verdict": "SCOPED_CORRESPONDENCE_WITH_COMMON_SHOCK_CONTROL",
    },
    "selective_view_and_capability": {
        "distributed": "local action closure without global history",
        "physical": "boundary-flux closure without interior or formation history",
        "verdict": "EXACT_CAPABILITY_RELATIVE_CORRESPONDENCE",
    },
    "receiver_context": {
        "distributed": "availability, epoch, membership, semantics",
        "physical": "archive availability, epoch, orientation, preserved boundary",
        "verdict": "EXACT_HANDOFF_CORRESPONDENCE",
    },
    "dual_mesh_handoff": {
        "distributed": "signed render/replication view plus authoritative collision state",
        "physical": "certified record representation plus causal action/formation surface",
        "verdict": "EXACT_FACTORIZATION_ANALOGY_ONLY",
        "reason": (
            "a signature can authenticate the delivered representation while "
            "the action target still fails on its fibres"
        ),
    },
    "authenticated_provenance": {
        "distributed": "declared signer/origin and hash ancestry",
        "physical": "causal source--pointer formation relation",
        "verdict": "EXACT_NON_UNIFICATION",
        "reason": "the same signed record can be QND-formed or preloaded",
    },
    "hard_finality": {
        "distributed": "conflict-safe authorization under membership/fault rules",
        "physical": "target factorization under an action/horizon envelope",
        "verdict": "EXACT_NON_UNIFICATION_WITH_SCOPED_ACTION_ANALOGY",
    },
    "zero_knowledge_or_encrypted_computation": {
        "distributed": "verification/computation with bounded disclosure",
        "physical": "operational access to a formed physical record",
        "verdict": "NO_SAME_SEMANTICS_WITHOUT_ADDITIONAL_PHYSICAL_INTERFACE",
    },
    "emergence_and_scaling": {
        "distributed": "macro protocol variable and finite-size reliability",
        "physical": "law-constrained flux quotient and standard concentration",
        "verdict": "COARSE_GRAINING_OR_WEAK_EMERGENCE_ONLY",
    },
}

result = {
    "claim_id": "HC-DU-051",
    "work_id": "N5-SCF-P5",
    "title": (
        "Physical-record amplification and capability-relative finality "
        "with exact distributed/physical provenance non-unification"
    ),
    "arena_selection": {
        "primary": "HC-DU-040D material Z3 gauge boundary",
        "absorber": "HC-DU-040E stabilizer syndrome",
        "hostile": "HC-DU-046 closed metastable host",
        "reason": (
            "the primary already has a formed source-pointer-archive channel, "
            "declared access, stochastic redundancy controls, frozen targets, "
            "and exact local proofs"
        ),
    },
    "returns": [
        "SCOPED_AMPLIFICATION_WITHOUT_INFORMATION_CREATION_THEOREM",
        "CAPABILITY_RELATIVE_REGIONAL_FINALITY_THEOREM",
        "EXACT_DISTRIBUTED_PHYSICAL_NON_UNIFICATION",
    ],
    "first_non_unifying_arrow": (
        "authenticated_declared_origin_to_causal_physical_source_binding"
    ),
    "theorem_package": {
        "no_minting": (
            "Every randomized replica, decoder, certificate, or hardening "
            "layer downstream of one formed record is constant in law on "
            "that record's physical fibres."
        ),
        "risk": {
            "single_cell_error": fraction_text(p),
            "three_independent_cell_majority_error": fraction_text(
                independent_error_curve[3]
            ),
            "three_common_shock_cell_error": fraction_text(p),
            "exact_finite_noisy_reconstruction": False,
        },
        "capability_relative_finality": (
            "The gauge archive is exact for boundary-flux actions in the "
            "frozen envelope and incomplete for interior, crossing, and "
            "microscopic-formation targets."
        ),
        "handoff": (
            "Safe physical handoff factors through the archived value plus "
            "availability, epoch, orientation, and boundary-preservation context."
        ),
        "non_unification": (
            "Protocol signatures, quorums, threshold authority, and proof "
            "systems certify declared relations.  They do not identify the "
            "causal physical formation relation without an additional formed "
            "physical meta-record."
        ),
        "dual_mesh_interpretation": (
            "The certified public view is representation-like; the physical "
            "source/action relation is collision-like.  Safe handoff requires "
            "the action target to factor through the view or an independently "
            "formed binding between them."
        ),
        "hostile_control": (
            "Endpoint replication and hardening do not repair the metastable "
            "history fibre; full-history access remains injective tomography."
        ),
    },
    "translation": translation,
    "emergence_grade": {
        "material_flux": "LAW_CONSTRAINED_ACTION_SUFFICIENT_COARSE_GRAINING",
        "archive_majority": "STANDARD_STATISTICAL_AMPLIFICATION",
        "strong_emergence": "NOT_EARNED",
        "criticality_or_universality": "NOT_EARNED",
    },
    "portfolio_handoff": {
        "work_id": "N5-RS-P2",
        "recommendation": "RESUME_WITH_SHARPENED_INPUTS",
        "reason": (
            "the distributed stack adds reliability, propagation, audit, and "
            "action safety only after a target-sensitive physical formation "
            "channel exists; it cannot supply the missing physical selector "
            "or source-binding premise"
        ),
        "sharpened_minimum_premise": (
            "an independently motivated physical antecedent must select and "
            "form a target-sensitive causal source-to-record relation, bind "
            "its orientation/epoch/access semantics, and support a frozen "
            "noninjective action quotient before downstream finality layers "
            "can add value"
        ),
    },
    "grade": (
        "EXACT_FINITE_TYPED_SYNTHESIS_USING_KNOWN_FACTORIZATION_QND_GAUGE_"
        "CONCENTRATION_AND_DISTRIBUTED_SYSTEMS_MATHEMATICS"
    ),
    "not_earned": [
        "new distributed-systems theorem",
        "new gauge or quantum theorem",
        "physical equivalence between consensus and quantum mechanics",
        "strong emergence or universality class",
        "record-first ontology",
        "new physics or prediction",
        "paper promotion",
        "hardware or provider escalation",
    ],
    "local_model_gate": {
        "disposition": "THEOREM_REGRESSION_OUTSIDE_RESEARCH_MODEL_ADMISSION",
        "reason": (
            "the analytic fibre and probability arguments decide the result; "
            "the script only exhausts their finite witnesses"
        ),
    },
    "checks": {
        "passed": sum(bool(item["passed"]) for item in CHECKS),
        "total": len(CHECKS),
        "all_pass": all(bool(item["passed"]) for item in CHECKS),
        "details": CHECKS,
    },
}


def main() -> None:
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    checks = result["checks"]
    if not checks["all_pass"]:
        failed = [
            item["name"]
            for item in checks["details"]
            if not bool(item["passed"])
        ]
        raise SystemExit(f"failed checks: {failed}")
    print(
        "HC-DU-051 distributed/physical collision certificate: "
        f"{checks['passed']}/{checks['total']} passed"
    )
    print("first non-unifying arrow:", result["first_non_unifying_arrow"])
    print(
        "portfolio handoff:",
        result["portfolio_handoff"]["recommendation"],
        result["portfolio_handoff"]["work_id"],
    )


if __name__ == "__main__":
    main()
