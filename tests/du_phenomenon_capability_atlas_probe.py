#!/usr/bin/env python3
"""Validate the Dynamic Unity Phenomenon-to-Capability Atlas v0.1.

This deterministic probe checks representation, source custody, typed
record/access/capability/finality boundaries, and planted hostile mutations.
It does not evaluate scientific truth, novelty, ontology, paper readiness, or
live research priority.
"""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "lab" / "phenomenon-capability-atlas" / "atlas-v0.1.json"
SCHEMA = ROOT / "specs" / "phenomenon-capability-atlas-v0.1.schema.json"
OUTPUT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_phenomenon_capability_atlas_result.json"
)

REPO_ROOTS = {
    "dynamic-unity": ROOT,
    "gu-formalization": ROOT.parent / "gu-formalization",
    "time-as-finality": ROOT.parent / "time-as-finality",
    "possibility-to-capability": ROOT.parent / "possibility-to-capability",
    "temporal-issuance": ROOT.parent / "temporal-issuance",
    "continuity-ledger": ROOT.parent / "continuity-ledger",
}

RECORD_LEVELS = [
    "EVENT",
    "TRACE",
    "RETAINED_RECORD",
    "ACCESSIBLE_RECORD",
    "CERTIFICATE",
    "PUBLIC_FINAL_RECORD",
    "ACTION_ENABLING_FACT",
]

EXPECTED_PHENOMENA = {
    "DU-PCA-001",
    "DU-PCA-002",
    "DU-PCA-003",
    "DU-PCA-004",
    "DU-PCA-005",
    "DU-PCA-006",
}

EXPECTED_CONTROL_IDS = {f"CTRL-{index:02d}" for index in range(1, 13)}

INVARIANT_IDS = [
    "schema_contract",
    "completed_nonrouting_status",
    "bounded_denominator",
    "source_adapter_custody",
    "gu_requirement_semantic_guard",
    "immutable_source_bindings",
    "source_reference_integrity",
    "six_specimen_identity",
    "eligible_physics_source",
    "source_grounding_ceiling",
    "physics_to_capability_direction",
    "typed_record_ladder",
    "physical_observer_profiles",
    "matched_contrast_frames",
    "p2c_diagnosis_reproduction",
    "normalized_capability_gate",
    "projection_fibre_constancy",
    "finality_triple_gate",
    "issuance_independence_gate",
    "structural_provenance_and_grade",
    "hostile_control_manifest",
    "global_nonclaims",
]


def _git_bytes(repo: Path, revision: str, locator: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{revision}:{locator}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout if result.returncode == 0 else None


def _derived_diagnosis(witness: dict[str, str]) -> set[str]:
    result: set[str] = set()
    if witness["possibility_family_relation"] == "DIFFERENT":
        result.add("POSSIBILITY_FAMILY_CHANGE")
    if (
        witness["dynamics_change"] == "YES"
        and witness["possibility_family_relation"] == "SAME"
    ):
        result.add("FIXED_FAMILY_DYNAMICS_CHANGE")
    if witness["persistent_record"] == "YES":
        result.add("RECORD_FORMATION")
    if witness["access_change"] == "YES":
        result.add("ACCESS_CHANGE")
    if witness["normalized_task_relation"] == "SUPERSET":
        result.add("CAPABILITY_ENLARGEMENT")
    elif witness["normalized_task_relation"] == "SUBSET":
        result.add("CAPABILITY_RESTRICTION")
    elif witness["normalized_task_relation"] == "EQUAL":
        result.add("NO_CAPABILITY_CHANGE")
    if (
        witness["settlement"] == "YES"
        and witness["preceding_factorization"] == "NO_FACTOR_FOUND"
        and witness["reopenable_by_admissible_continuation"] == "NO"
    ):
        result.add("FINALITY_CANDIDATE")
    return result


def semantic_errors(
    atlas: dict[str, Any], *, verify_source_content: bool
) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []

    def reject(code: str, detail: str) -> None:
        errors.append((code, detail))

    if atlas.get("status") != "COMPLETED_NONROUTING_METHOD_PILOT":
        reject("ROUTING_STATUS", "pilot status changed")
    routing = atlas.get("routing", {})
    if (
        routing.get("non_routing") is not True
        or routing.get("banked") is not False
        or routing.get("wip") is not False
        or routing.get("live_authority") != "CURRENT-RESEARCH.yaml"
        or routing.get("scheduled_priority_unchanged") is not True
        or routing.get("executable_continuation") is not None
    ):
        reject("ROUTING_STATUS", "non-routing/WIP/live-authority contract failed")

    denominator = atlas.get("denominator", {})
    if (
        denominator.get("kind") != "BOUNDED_STRESS_SET"
        or denominator.get("count") != 6
        or denominator.get("exhaustive") is not False
    ):
        reject("DENOMINATOR", "v0.1 must remain a non-exhaustive six-card stress set")
    if atlas.get("evidence_ceiling") != 2:
        reject("EVIDENCE_CEILING", "root evidence ceiling must be Grade 2")

    adapters = atlas.get("source_adapters", [])
    adapter_ids = [item.get("adapter_id") for item in adapters]
    if len(adapter_ids) != len(set(adapter_ids)):
        reject("UNIQUE_ID", "source adapter IDs are not unique")
    adapter_by_id = {item.get("adapter_id"): item for item in adapters}
    for adapter in adapters:
        if adapter.get("authority_transfer") is not False:
            reject("AUTHORITY_TRANSFER", str(adapter.get("adapter_id")))
        repo = REPO_ROOTS.get(adapter.get("source_repo"))
        revision = adapter.get("revision", "")
        if repo is None or len(revision) != 40:
            reject("SOURCE_ADAPTER", str(adapter.get("adapter_id")))
    gu = adapter_by_id.get("ADAPTER-GU-CPL", {})
    if (
        gu.get("source_kind") != "THEORY_REQUIREMENT_LEDGER"
        or gu.get("phenomenon_eligible") is not False
    ):
        reject(
            "GU_REQUIREMENT_ADAPTER",
            "GU requirement rows cannot be treated as phenomenon rows",
        )

    bindings = atlas.get("source_bindings", [])
    binding_ids = [item.get("binding_id") for item in bindings]
    if len(binding_ids) != len(set(binding_ids)):
        reject("UNIQUE_ID", "source binding IDs are not unique")
    binding_by_id = {item.get("binding_id"): item for item in bindings}
    for binding in bindings:
        adapter = adapter_by_id.get(binding.get("adapter_ref"))
        if adapter is None:
            reject("SOURCE_REF", f"missing adapter for {binding.get('binding_id')}")
            continue
        if binding.get("immutable_revision") != adapter.get("revision"):
            reject("SOURCE_REVISION", str(binding.get("binding_id")))
        if not binding.get("source_nonclaims"):
            reject("SOURCE_CUSTODY", str(binding.get("binding_id")))
        if verify_source_content:
            repo = REPO_ROOTS[adapter["source_repo"]]
            payload = _git_bytes(
                repo,
                binding["immutable_revision"],
                binding["artifact_locator"],
            )
            if payload is None:
                reject("SOURCE_PIN", str(binding.get("binding_id")))
            else:
                actual = hashlib.sha256(payload).hexdigest()
                if actual != binding.get("content_sha256"):
                    reject("SOURCE_DIGEST", str(binding.get("binding_id")))

    phenomena = atlas.get("phenomena", [])
    phenomenon_ids = [item.get("phenomenon_id") for item in phenomena]
    if set(phenomenon_ids) != EXPECTED_PHENOMENA or len(phenomenon_ids) != 6:
        reject("PHENOMENON_SET", str(phenomenon_ids))
    if len(phenomenon_ids) != len(set(phenomenon_ids)):
        reject("UNIQUE_ID", "phenomenon IDs are not unique")

    all_observer_ids: list[str] = []
    all_contrast_ids: list[str] = []
    all_structure_ids: list[str] = []
    for card in phenomena:
        card_id = str(card.get("phenomenon_id"))
        refs = card.get("source_binding_refs", [])
        if not refs or any(ref not in binding_by_id for ref in refs):
            reject("SOURCE_REF", card_id)
        physics_refs = card.get("physics", {}).get("source_assertion_refs", [])
        if not physics_refs or not set(physics_refs).issubset(set(refs)):
            reject("SOURCE_REF", f"physics assertion refs for {card_id}")
        eligible = False
        for ref in refs:
            binding = binding_by_id.get(ref)
            if binding:
                adapter = adapter_by_id.get(binding.get("adapter_ref"), {})
                eligible = eligible or adapter.get("phenomenon_eligible") is True
        if not eligible:
            reject("PHENOMENON_SOURCE", card_id)

        grade = card.get("evidence", {}).get("atlas_grade")
        if not isinstance(grade, int) or grade < 0 or grade > 2:
            reject("EVIDENCE_CEILING", card_id)
        if card.get("source_grounding_status") == "PRIMARY_AUDIT_REQUIRED":
            if grade is not None and grade > 1:
                reject("SOURCE_GROUNDING_CEILING", card_id)
            if not any(
                binding_by_id.get(ref, {}).get("missing_import_requirements")
                for ref in refs
            ):
                reject("SOURCE_GROUNDING_GAP", card_id)
        if card.get("process", {}).get("direction") != (
            "SOURCE_PHYSICS_TO_INDUCED_CAPABILITY"
        ):
            reject("DIRECTION", card_id)

        ladder = card.get("record_ladder", [])
        if [stage.get("level") for stage in ladder] != RECORD_LEVELS:
            reject("RECORD_LADDER", card_id)
        for stage in ladder:
            if not all(
                stage.get(field)
                for field in ("target", "carrier", "condition", "warrant")
            ):
                reject("RECORD_LADDER", f"incomplete stage in {card_id}")

        observers = card.get("observer_profiles", [])
        if len(observers) < 2:
            reject("OBSERVER_PROFILE", card_id)
        for observer in observers:
            observer_id = observer.get("observer_id")
            all_observer_ids.append(observer_id)
            if observer.get("observer_kind") in (None, "HUMAN", "PERSON"):
                reject("OBSERVER_KIND", f"{card_id}:{observer_id}")
            for field in (
                "physical_subsystem",
                "boundary",
                "channels",
                "horizon",
                "operations",
                "resources",
                "risk_or_error",
                "provenance",
            ):
                if not observer.get(field):
                    reject("OBSERVER_PROFILE", f"{card_id}:{observer_id}:{field}")

        contrasts = card.get("contrasts", [])
        if len(contrasts) < 2 or not any(
            contrast.get("is_matched_control") is True for contrast in contrasts
        ):
            reject("CONTRAST_PORTFOLIO", card_id)
        for contrast in contrasts:
            contrast_id = contrast.get("contrast_id")
            all_contrast_ids.append(contrast_id)
            frame = contrast.get("comparison_frame", {})
            if not frame.get("matched_fields") or not frame.get("changed_fields"):
                reject("MATCHED_FRAME", f"{card_id}:{contrast_id}")
            if frame.get("unmatched_fields"):
                reject("UNMATCHED_FRAME", f"{card_id}:{contrast_id}")
            witness = contrast.get("witness", {})
            expected = set(contrast.get("expected_diagnosis", []))
            derived = _derived_diagnosis(witness)
            if expected != derived:
                reject(
                    "DIAGNOSIS_MISMATCH",
                    f"{card_id}:{contrast_id}:{sorted(expected)}!={sorted(derived)}",
                )
            if (
                witness.get("normalized_task_relation") == "EQUAL"
                and "CAPABILITY_ENLARGEMENT" in expected
            ):
                reject("CAPABILITY_NORMALIZATION", f"{card_id}:{contrast_id}")
            if (
                witness.get("preceding_factorization") == "NO_FACTOR_FOUND"
                and not witness.get("factorization_search_scope")
            ):
                reject("FACTORIZATION_SCOPE", f"{card_id}:{contrast_id}")

        projection = card.get("projection_audit", {})
        spread = str(projection.get("capability_spread", "")).lower()
        if (
            projection.get("sufficiency_status") == "CONSTANT_ON_FIBRES"
            and not spread.startswith("zero")
        ):
            reject("PROJECTION_CONSTANCY", card_id)
        if (
            projection.get("sufficiency_status") == "VARIES_ON_FIBRES"
            and spread.startswith("zero")
        ):
            reject("PROJECTION_CONSTANCY", card_id)

        finality = card.get("finality", {})
        if finality.get("verdict") != "NONE" and not (
            finality.get("settlement") == "YES"
            and finality.get("preceding_factorization") == "NO_FACTOR_FOUND"
            and finality.get("factorization_search_scope")
            and finality.get("reopenable_by_admissible_continuation") == "NO"
        ):
            reject("FINALITY_GATE", card_id)

        issuance = card.get("temporal_issuance", {})
        if issuance.get("classification") == "ISSUANCE" and not (
            issuance.get("source_side_primitive") is True
            and issuance.get("same_neighbor_data_discriminator") is True
        ):
            reject("ISSUANCE_GATE", card_id)

        structures = card.get("structures", [])
        if len(structures) < 2:
            reject("STRUCTURE_PORTFOLIO", card_id)
        for structure in structures:
            all_structure_ids.append(structure.get("structure_id"))
            origin = structure.get("origin")
            warrant = structure.get("warrant")
            ceiling = structure.get("evidence_ceiling")
            if origin == "ATLAS_INTRODUCED" and (
                warrant == "PHYSICS_OWNED" or ceiling is None or ceiling > 1
            ):
                reject("ATLAS_GEOMETRY_WARRANT", str(structure.get("structure_id")))
            if origin == "SOURCE_THEORY" and warrant in (
                "STRUCTURAL_ANALOGY",
                "OPEN",
            ):
                reject("SOURCE_GEOMETRY_WARRANT", str(structure.get("structure_id")))
            if warrant == "PHYSICS_OWNED" and origin != "SOURCE_THEORY":
                reject("ATLAS_GEOMETRY_WARRANT", str(structure.get("structure_id")))
            if not structure.get("axioms_checked"):
                reject("STRUCTURE_AXIOMS", str(structure.get("structure_id")))

    for values, label in (
        (all_observer_ids, "observer"),
        (all_contrast_ids, "contrast"),
        (all_structure_ids, "structure"),
    ):
        if len(values) != len(set(values)):
            reject("UNIQUE_ID", f"duplicate {label} ID")

    controls = atlas.get("cross_specimen_controls", [])
    if {item.get("control_id") for item in controls} != EXPECTED_CONTROL_IDS:
        reject("CONTROL_MANIFEST", "expected CTRL-01 through CTRL-12")
    if len(atlas.get("nonclaims", [])) < 5:
        reject("NONCLAIMS", "global nonclaim surface is incomplete")
    return errors


def _mutation_cases() -> list[
    tuple[str, str, Callable[[dict[str, Any]], None]]
]:
    def gu_as_phenomenon(data: dict[str, Any]) -> None:
        data["source_adapters"][0]["phenomenon_eligible"] = True

    def missing_ladder_stage(data: dict[str, Any]) -> None:
        data["phenomena"][0]["record_ladder"].pop(2)

    def unphysical_person(data: dict[str, Any]) -> None:
        data["phenomena"][0]["observer_profiles"][0]["observer_kind"] = "HUMAN"

    def capability_from_raw_growth(data: dict[str, Any]) -> None:
        data["phenomena"][0]["contrasts"][0]["expected_diagnosis"].append(
            "CAPABILITY_ENLARGEMENT"
        )

    def irreversibility_as_finality(data: dict[str, Any]) -> None:
        data["phenomena"][2]["finality"]["verdict"] = "PUBLIC_CANDIDATE"

    def finality_as_issuance(data: dict[str, Any]) -> None:
        data["phenomena"][2]["temporal_issuance"]["classification"] = "ISSUANCE"

    def geometry_provenance_loss(data: dict[str, Any]) -> None:
        data["phenomena"][0]["structures"][1]["origin"] = "SOURCE_THEORY"

    def stale_source_digest(data: dict[str, Any]) -> None:
        data["source_bindings"][0]["content_sha256"] = "0" * 64

    def false_projection_sufficiency(data: dict[str, Any]) -> None:
        data["phenomena"][0]["projection_audit"]["sufficiency_status"] = (
            "CONSTANT_ON_FIBRES"
        )

    def hidden_unmatched_resource(data: dict[str, Any]) -> None:
        data["phenomena"][1]["contrasts"][1]["comparison_frame"][
            "unmatched_fields"
        ] = ["unpriced cryogenic maintenance"]

    def grade_promotion(data: dict[str, Any]) -> None:
        data["phenomena"][0]["evidence"]["atlas_grade"] = 3

    def exhaustive_cast(data: dict[str, Any]) -> None:
        data["denominator"]["exhaustive"] = True

    def broken_source_ref(data: dict[str, Any]) -> None:
        data["phenomena"][0]["source_binding_refs"][0] = "SRC-NOT-THERE"

    def authority_transfer(data: dict[str, Any]) -> None:
        data["source_adapters"][1]["authority_transfer"] = True

    def only_ineligible_source(data: dict[str, Any]) -> None:
        data["phenomena"][1]["source_binding_refs"] = ["SRC-TI-RING"]
        data["phenomena"][1]["physics"]["source_assertion_refs"] = [
            "SRC-TI-RING"
        ]

    def duplicate_id(data: dict[str, Any]) -> None:
        data["phenomena"][1]["phenomenon_id"] = data["phenomena"][0][
            "phenomenon_id"
        ]

    return [
        ("gu_requirement_cast", "GU_REQUIREMENT_ADAPTER", gu_as_phenomenon),
        ("missing_record_stage", "RECORD_LADDER", missing_ladder_stage),
        ("human_observer_primitive", "OBSERVER_KIND", unphysical_person),
        (
            "raw_growth_as_capability",
            "DIAGNOSIS_MISMATCH",
            capability_from_raw_growth,
        ),
        ("irreversibility_as_finality", "FINALITY_GATE", irreversibility_as_finality),
        ("finality_as_issuance", "ISSUANCE_GATE", finality_as_issuance),
        (
            "geometry_provenance_loss",
            "SOURCE_GEOMETRY_WARRANT",
            geometry_provenance_loss,
        ),
        ("stale_source_digest", "SOURCE_DIGEST", stale_source_digest),
        (
            "false_projection_sufficiency",
            "PROJECTION_CONSTANCY",
            false_projection_sufficiency,
        ),
        ("hidden_unmatched_resource", "UNMATCHED_FRAME", hidden_unmatched_resource),
        ("atlas_grade_promotion", "EVIDENCE_CEILING", grade_promotion),
        ("exhaustive_cast", "DENOMINATOR", exhaustive_cast),
        ("broken_source_reference", "SOURCE_REF", broken_source_ref),
        ("authority_transfer", "AUTHORITY_TRANSFER", authority_transfer),
        ("ineligible_only_source", "PHENOMENON_SOURCE", only_ineligible_source),
        ("duplicate_identity", "PHENOMENON_SET", duplicate_id),
    ]


def result_payload(atlas: dict[str, Any], rejected: list[str]) -> dict[str, Any]:
    return {
        "artifact_type": "phenomenon_capability_atlas_representation_check",
        "atlas": str(ATLAS.relative_to(ROOT)),
        "schema": str(SCHEMA.relative_to(ROOT)),
        "status": "pass",
        "specimen_count": len(atlas["phenomena"]),
        "source_binding_count": len(atlas["source_bindings"]),
        "validated_invariant_count": len(INVARIANT_IDS),
        "validated_invariants": INVARIANT_IDS,
        "hostile_mutation_count": len(rejected),
        "rejected_mutations": rejected,
        "evidence_ceiling": 2,
        "routing_changed": False,
        "scientific_claims_validated": False,
        "note": (
            "Passing establishes source/provenance and representation integrity "
            "only; it does not establish physics, novelty, ontology, finality, "
            "issuance, paper readiness, or research priority."
        ),
    }


def run() -> dict[str, Any]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise AssertionError("schema_contract: Draft 2020-12 marker missing")
    if schema.get("additionalProperties") is not False:
        raise AssertionError("schema_contract: root must fail closed")
    if schema.get("properties", {}).get("phenomena", {}).get("maxItems") != 6:
        raise AssertionError("schema_contract: six-card maximum missing")

    try:
        import jsonschema  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        pass
    else:
        validator = jsonschema.Draft202012Validator(schema)
        schema_errors = sorted(validator.iter_errors(atlas), key=lambda err: list(err.path))
        if schema_errors:
            first = schema_errors[0]
            raise AssertionError(
                f"json_schema: {list(first.path)}: {first.message}"
            )

    errors = semantic_errors(atlas, verify_source_content=True)
    if errors:
        raise AssertionError(f"{errors[0][0]}: {errors[0][1]}")

    rejected: list[str] = []
    for mutation_id, expected_code, mutate in _mutation_cases():
        candidate = copy.deepcopy(atlas)
        mutate(candidate)
        codes = {
            code
            for code, _detail in semantic_errors(
                candidate,
                verify_source_content=mutation_id == "stale_source_digest",
            )
        }
        if expected_code not in codes:
            raise AssertionError(
                f"mutation_control: {mutation_id} did not produce {expected_code}; "
                f"got {sorted(codes)}"
            )
        rejected.append(mutation_id)

    result = result_payload(atlas, rejected)
    checked_in = json.loads(OUTPUT.read_text(encoding="utf-8"))
    if checked_in != result:
        raise AssertionError(
            "receipt_drift: checked-in artifact differs from deterministic result"
        )
    return result


if __name__ == "__main__":
    output = run()
    print(
        "PASS: "
        f"{output['specimen_count']} cards; "
        f"{output['validated_invariant_count']} invariants; "
        f"{output['hostile_mutation_count']}/{output['hostile_mutation_count']} "
        "hostile mutations rejected"
    )
