#!/usr/bin/env python3
"""Fail-closed validation for the Dynamic Unity atlas v0.2 first run.

The probe intentionally uses only the Python standard library.  It executes
the closed JSON-Schema vocabulary used by the four v0.2 schemas, validates
cross-artifact semantics and content pins, and rejects planted category
errors.  It establishes representation integrity, not scientific truth.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "lab/phenomenon-capability-atlas/cards-v0.2/du-xenon-s1-s2.json"
RELEASE = ROOT / "lab/phenomenon-capability-atlas/release-v0.2.json"
REVIEW = ROOT / "lab/phenomenon-capability-atlas/reviews/xenon-s1-s2-independent-remap-v0.2.json"
COMPOSITION = ROOT / "lab/phenomenon-capability-atlas/compositions/gu-record-capability-first-run-v0.2.json"
CARD_SCHEMA = ROOT / "specs/phenomenon-capability-atlas-card-v0.2.schema.json"
RELEASE_SCHEMA = ROOT / "specs/phenomenon-capability-atlas-release-v0.2.schema.json"
REVIEW_SCHEMA = ROOT / "specs/phenomenon-capability-atlas-review-v0.2.schema.json"
COMPOSITION_SCHEMA = ROOT / "specs/phenomenon-capability-atlas-composition-v0.2.schema.json"
OUTPUT = ROOT / "tests/artifacts/du_phenomenon_capability_atlas_v02_result.json"

REPO_ROOTS = {
    "dynamic-unity": ROOT,
    "gu-formalization": ROOT.parent / "gu-formalization",
    "time-as-finality": ROOT.parent / "time-as-finality",
    "possibility-to-capability": ROOT.parent / "possibility-to-capability",
    "temporal-issuance": ROOT.parent / "temporal-issuance",
    "continuity-ledger": ROOT.parent / "continuity-ledger",
}

RECORD_LEVELS = {
    "EVENT", "TRACE", "RETAINED_RECORD", "ACCESSIBLE_RECORD", "CERTIFICATE",
    "PUBLIC_FINAL_RECORD", "ACTION_ENABLING_FACT",
}
REVIEW_COMPARISON_IDS = {
    "M1", "M2", "M3", "M4", "P1", "P2", "P3", "P4", "P5",
    "X1", "X2", "X3", "X4", "X5", "X6", "R1", "R2", "R3", "R4",
    "R5", "R6", "R7", "R8", "O1", "O2", "T1", "T2", "C1", "C2",
    "C3", "F1", "I1", "G1", "G2", "E1", "E2", "E3", "E4", "E5",
}
COMPOSITION_LAYERS = {
    "GU_REQUIREMENT_CROSSWALK", "INITIAL_BOUNDARY_CONDITIONS",
    "DU_CONTINUITY_RECORDS", "P2C_TRANSITION", "TAF_CAPABILITY_FINALITY",
    "TI_ISSUANCE_EFFECT",
}
MUTATION_IDS = [
    "unknown_schema_property", "unsupported_schema_keyword", "legacy_record_status",
    "missing_review_axis", "adapter_level_eligibility", "accepted_without_independent_grounding",
    "gu_requirement_as_physics_grounding", "accepted_with_domain_gap",
    "release_card_count_drift", "release_card_id_drift", "release_digest_drift",
    "schema_digest_drift", "predecessor_digest_drift", "source_digest_drift",
    "predecessor_card_identity_drift", "review_artifact_ref_drift",
    "projection_constant_nonzero", "projection_varies_zero", "projection_not_tested_with_witness",
    "relation_record_missing_subjects", "record_graph_cycle", "missing_representation_kill",
    "supplied_discriminator_without_outcomes", "review_metric_drift", "review_axis_collapse",
    "composition_gu_false_friend", "composition_matched_as_same_occurrence",
    "composition_matched_as_evolution", "composition_dangling_endpoint",
    "composition_atlas_predecessor_role_leak", "p2c_tool_result_drift",
    "composition_cltp_as_physics",
    "composition_finality_promotion", "composition_ti_erases_residue",
    "evidence_grade_promotion", "routing_promotion",
]

INVARIANT_IDS = [
    "stdlib_schema_vocabulary_fail_closed", "all_four_json_schemas_mandatory",
    "v01_evidence_byte_identity", "release_cardinality_and_identity",
    "synthetic_additional_card_release_gate",
    "release_artifact_digest_closure", "completed_nonrouting_status",
    "claim_level_physics_grounding", "accepted_physics_independence_gate",
    "review_axis_separation", "canonical_record_status_vocabulary",
    "explicit_initial_and_boundary_conditions", "relation_record_dag",
    "observer_record_reference_integrity", "matched_contrast_frames",
    "p2c_diagnosis_reproduction", "typed_projection_constancy",
    "finality_triple_gate", "issuance_independence_gate",
    "structural_provenance_and_grade", "split_challenge_semantics",
    "independent_remap_metric_reproduction", "prior_exposure_disclosure",
    "composition_source_closure", "composition_typed_objects_and_maps",
    "same_ring_counterfactual_separation", "gu_false_friend_rejection",
    "cltp_method_only_gate", "taf_record_erasure_factorization",
    "ti_operational_residue_preservation", "composition_grade_ceiling",
]


class SchemaValidationError(ValueError):
    """An instance violates the supported schema vocabulary."""


class UnsupportedSchemaKeyword(ValueError):
    """A schema uses a keyword the stdlib evaluator does not implement."""


SUPPORTED_SCHEMA_KEYWORDS = {
    "$schema", "$id", "$ref", "$defs", "title", "description", "type",
    "const", "enum", "required", "properties", "additionalProperties",
    "items", "minItems", "maxItems", "minLength", "pattern", "minimum",
    "maximum", "format",
}


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_bytes(repo: Path, revision: str, locator: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"{revision}:{locator}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout if result.returncode == 0 else None


def _check_schema_vocabulary(schema: Any, path: str = "$") -> None:
    if not isinstance(schema, dict):
        raise UnsupportedSchemaKeyword(f"{path}: schema node is not an object")
    unsupported = set(schema) - SUPPORTED_SCHEMA_KEYWORDS
    if unsupported:
        raise UnsupportedSchemaKeyword(
            f"{path}: unsupported schema keywords {sorted(unsupported)}"
        )
    if "$ref" in schema and not str(schema["$ref"]).startswith("#/"):
        raise UnsupportedSchemaKeyword(f"{path}: only internal JSON Pointer $ref is supported")
    if "format" in schema and schema["format"] != "date":
        raise UnsupportedSchemaKeyword(f"{path}: unsupported format {schema['format']!r}")
    for container in ("properties", "$defs"):
        values = schema.get(container, {})
        if not isinstance(values, dict):
            raise UnsupportedSchemaKeyword(f"{path}.{container}: expected object")
        for name, subschema in values.items():
            _check_schema_vocabulary(subschema, f"{path}.{container}.{name}")
    if "items" in schema:
        _check_schema_vocabulary(schema["items"], f"{path}.items")
    additional = schema.get("additionalProperties")
    if isinstance(additional, dict):
        _check_schema_vocabulary(additional, f"{path}.additionalProperties")


def _resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise UnsupportedSchemaKeyword(f"external or non-pointer $ref unsupported: {ref}")
    node: Any = root_schema
    for raw in ref[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if not isinstance(node, dict) or token not in node:
            raise UnsupportedSchemaKeyword(f"unresolvable $ref: {ref}")
        node = node[token]
    if not isinstance(node, dict):
        raise UnsupportedSchemaKeyword(f"$ref does not resolve to schema: {ref}")
    return node


def _is_type(instance: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(instance, dict)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "null":
        return instance is None
    raise UnsupportedSchemaKeyword(f"unsupported JSON type: {expected}")


def _validate_schema(
    instance: Any,
    schema: dict[str, Any],
    *,
    root_schema: dict[str, Any] | None = None,
    path: str = "$",
) -> None:
    root_schema = schema if root_schema is None else root_schema
    if "$ref" in schema:
        _validate_schema(
            instance,
            _resolve_ref(root_schema, schema["$ref"]),
            root_schema=root_schema,
            path=path,
        )
    if "const" in schema and instance != schema["const"]:
        raise SchemaValidationError(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaValidationError(f"{path}: {instance!r} is not in enum")
    if "type" in schema and not _is_type(instance, schema["type"]):
        raise SchemaValidationError(f"{path}: expected {schema['type']}")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            raise SchemaValidationError(f"{path}: string shorter than minLength")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            raise SchemaValidationError(f"{path}: string does not match pattern")
        if schema.get("format") == "date":
            try:
                date.fromisoformat(instance)
            except ValueError as exc:
                raise SchemaValidationError(f"{path}: invalid date") from exc

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            raise SchemaValidationError(f"{path}: array shorter than minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            raise SchemaValidationError(f"{path}: array longer than maxItems")
        if "items" in schema:
            for index, item in enumerate(instance):
                _validate_schema(
                    item, schema["items"], root_schema=root_schema,
                    path=f"{path}[{index}]",
                )

    if isinstance(instance, dict):
        for required in schema.get("required", []):
            if required not in instance:
                raise SchemaValidationError(f"{path}: missing required {required!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(properties)
            if extra:
                raise SchemaValidationError(f"{path}: unexpected properties {sorted(extra)}")
        for key, subschema in properties.items():
            if key in instance:
                _validate_schema(
                    instance[key], subschema, root_schema=root_schema,
                    path=f"{path}.{key}",
                )

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise SchemaValidationError(f"{path}: below minimum")
        if "maximum" in schema and instance > schema["maximum"]:
            raise SchemaValidationError(f"{path}: above maximum")


def _schema_code(instance: Any, schema: dict[str, Any]) -> str | None:
    try:
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise UnsupportedSchemaKeyword("Draft 2020-12 marker missing")
        _check_schema_vocabulary(schema)
        _validate_schema(instance, schema)
    except UnsupportedSchemaKeyword:
        return "SCHEMA_ENGINE_UNSUPPORTED"
    except SchemaValidationError:
        return "JSON_SCHEMA"
    return None


def _derived_diagnosis(witness: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    if witness["possibility_family_relation"] == "DIFFERENT":
        result.add("POSSIBILITY_FAMILY_CHANGE")
    if witness["dynamics_change"] == "YES" and witness["possibility_family_relation"] == "SAME":
        result.add("FIXED_FAMILY_DYNAMICS_CHANGE")
    if witness["persistent_record"] == "YES":
        result.add("RECORD_FORMATION")
    if witness["access_change"] == "YES":
        result.add("ACCESS_CHANGE")
    relation = witness["normalized_task_relation"]
    if relation == "SUPERSET":
        result.add("CAPABILITY_ENLARGEMENT")
    elif relation == "SUBSET":
        result.add("CAPABILITY_RESTRICTION")
    elif relation == "EQUAL":
        result.add("NO_CAPABILITY_CHANGE")
    if (
        witness["settlement"] == "YES"
        and witness["preceding_factorization"] == "NO_FACTOR_FOUND"
        and witness["reopenable_by_admissible_continuation"] == "NO"
    ):
        result.add("FINALITY_CANDIDATE")
    return result


def _has_cycle(nodes: set[str], edges: list[tuple[str, str]]) -> bool:
    outgoing: dict[str, list[str]] = {node: [] for node in nodes}
    for left, right in edges:
        outgoing[left].append(right)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(visit(child) for child in outgoing[node]):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in nodes)


def card_semantic_errors(card: dict[str, Any]) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []

    def reject(code: str, detail: str) -> None:
        errors.append((code, detail))

    bindings = card["source_bindings"]
    binding_ids = [binding["binding_id"] for binding in bindings]
    if len(binding_ids) != len(set(binding_ids)):
        reject("UNIQUE_ID", "duplicate source binding")
    by_binding = {binding["binding_id"]: binding for binding in bindings}
    for binding in bindings:
        grounding = binding["physics_grounding"]
        if binding.get("phenomenon_eligible") is not None:
            reject("ADAPTER_ELIGIBILITY", binding["binding_id"])
        if binding["source_owner"] == "gu-formalization" and binding["claim_role"] != "THEORY_REQUIREMENT":
            reject("GU_REQUIREMENT_BINDING", binding["binding_id"])
        if grounding["status"] in {"INDEPENDENT_ACCEPTED", "INDEPENDENT_CONDITIONAL"}:
            if binding["claim_role"] != "PHYSICS_GROUNDING" or grounding["independent_of_atlas_mapping"] is not True:
                reject("PHYSICS_GROUNDING", binding["binding_id"])
        if grounding["status"] == "NON_GROUNDING" and binding["claim_role"] == "PHYSICS_GROUNDING":
            reject("PHYSICS_GROUNDING", binding["binding_id"])

    physics = card["physics"]
    grounding_refs = physics["physics_grounding_refs"]
    if not set(grounding_refs).issubset(by_binding):
        reject("SOURCE_REF", "physics grounding refs")
    if physics["description_status"] == "SCOPED_ACCEPTED_DESCRIPTION":
        accepted = [
            by_binding[ref] for ref in grounding_refs
            if by_binding[ref]["claim_role"] == "PHYSICS_GROUNDING"
            and by_binding[ref]["physics_grounding"]["status"] == "INDEPENDENT_ACCEPTED"
            and by_binding[ref]["physics_grounding"]["independent_of_atlas_mapping"] is True
        ]
        if not accepted:
            reject("ACCEPTED_PHYSICS_GROUNDING", card["card_id"])
        if card["review_status"]["domain"] not in {"LOCAL_PACKET_REVIEWED", "PRIMARY_SOURCE_REVIEWED"}:
            reject("ACCEPTED_PHYSICS_REVIEW", card["card_id"])

    condition_ids: list[str] = []
    for group in ("initial_conditions", "boundary_conditions"):
        for condition in card["process"][group]:
            condition_ids.append(condition["condition_id"])
            if not set(condition["source_binding_refs"]).issubset(by_binding):
                reject("SOURCE_REF", condition["condition_id"])
    if len(condition_ids) != len(set(condition_ids)):
        reject("UNIQUE_ID", "condition")

    graph = card["record_graph"]
    node_ids = [node["record_id"] for node in graph["nodes"]]
    if len(node_ids) != len(set(node_ids)):
        reject("UNIQUE_ID", "record node")
    node_set = set(node_ids)
    if {node["level"] for node in graph["nodes"]} != RECORD_LEVELS:
        reject("RECORD_LEVEL_COVERAGE", card["card_id"])
    for node in graph["nodes"]:
        if not set(node["relates"]).issubset(node_set):
            reject("RECORD_RELATION_REF", node["record_id"])
        if node["node_kind"] == "RELATION_RECORD" and len(node["relates"]) < 2:
            reject("RELATION_RECORD_ARITY", node["record_id"])
        if not set(node["source_binding_refs"]).issubset(by_binding):
            reject("SOURCE_REF", node["record_id"])
    edge_ids = [edge["edge_id"] for edge in graph["edges"]]
    if len(edge_ids) != len(set(edge_ids)):
        reject("UNIQUE_ID", "record edge")
    edge_pairs: list[tuple[str, str]] = []
    for edge in graph["edges"]:
        if edge["from"] not in node_set or edge["to"] not in node_set:
            reject("RECORD_EDGE_REF", edge["edge_id"])
        else:
            edge_pairs.append((edge["from"], edge["to"]))
    if len(edge_pairs) == len(graph["edges"]) and _has_cycle(node_set, edge_pairs):
        reject("RECORD_GRAPH_CYCLE", card["card_id"])

    observer_ids: list[str] = []
    for observer in card["observer_profiles"]:
        observer_ids.append(observer["observer_id"])
        if not set(observer["visible_record_refs"]).issubset(node_set):
            reject("OBSERVER_RECORD_REF", observer["observer_id"])
    if len(observer_ids) != len(set(observer_ids)):
        reject("UNIQUE_ID", "observer")

    contrast_ids: list[str] = []
    for contrast in card["contrasts"]:
        contrast_ids.append(contrast["contrast_id"])
        frame = contrast["comparison_frame"]
        if frame["unmatched_fields"]:
            reject("UNMATCHED_FRAME", contrast["contrast_id"])
        if set(contrast["expected_diagnosis"]) != _derived_diagnosis(contrast["witness"]):
            reject("DIAGNOSIS_MISMATCH", contrast["contrast_id"])
    if len(contrast_ids) != len(set(contrast_ids)):
        reject("UNIQUE_ID", "contrast")
    if not any(item["is_matched_control"] for item in card["contrasts"]):
        reject("MATCHED_CONTROL", card["card_id"])

    projection = card["projection_audit"]
    projected = (
        projection["witness_status"], projection["visible_state_relation"],
        projection["capability_relation"], projection["spread_status"],
    )
    required_projection = {
        "CONSTANT_ON_FIBRES": ("SUPPLIED", "EQUAL", "EQUAL", "ZERO"),
        "VARIES_ON_FIBRES": ("SUPPLIED", "EQUAL", "DIFFERENT", "NONZERO"),
        "NOT_TESTED": ("NOT_SUPPLIED", "UNKNOWN", "UNKNOWN", "UNKNOWN"),
        "NOT_APPLICABLE": ("NOT_APPLICABLE", "NOT_APPLICABLE", "NOT_APPLICABLE", "NOT_APPLICABLE"),
    }[projection["sufficiency_status"]]
    if projected != required_projection:
        reject("PROJECTION_CONSTANCY", str(projected))

    finality = card["finality"]
    if finality["verdict"] != "NONE" and not (
        finality["settlement"] == "YES"
        and finality["preceding_factorization"] == "NO_FACTOR_FOUND"
        and finality["reopenable_by_admissible_continuation"] == "NO"
    ):
        reject("FINALITY_GATE", card["card_id"])
    issuance = card["temporal_issuance"]
    if issuance["classification"] == "ISSUANCE" and not (
        issuance["source_side_primitive"] is True
        and issuance["same_neighbor_data_discriminator"] is True
    ):
        reject("ISSUANCE_GATE", card["card_id"])
    for structure in card["structures"]:
        if structure["origin"] == "ATLAS_INTRODUCED" and (
            structure["warrant"] == "PHYSICS_OWNED" or structure["evidence_ceiling"] > 1
        ):
            reject("STRUCTURE_WARRANT", structure["structure_id"])
    if card["evidence"]["atlas_grade"] > card["evidence_ceiling"]:
        reject("EVIDENCE_CEILING", card["card_id"])
    held_out = card["evidence"]["challenges"]["held_out_discriminator"]
    if held_out["status"] in {"SUPPLIED", "PROPOSED"} and not held_out["opposed_outcomes"]:
        reject("HELD_OUT_DISCRIMINATOR", card["card_id"])
    return errors


def review_semantic_errors(review: dict[str, Any]) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    comparisons = review["field_comparisons"]
    ids = [item["comparison_id"] for item in comparisons]
    if set(ids) != REVIEW_COMPARISON_IDS or len(ids) != len(set(ids)):
        errors.append(("REVIEW_COMPARISON_SET", str(ids)))
    counts = Counter(item["verdict"] for item in comparisons)
    expected = {
        "comparison_units": len(comparisons),
        "agreement": counts["AGREEMENT"],
        "disagreement": counts["DISAGREEMENT"],
        "underdetermined_from_source": counts["UNDERDETERMINED_FROM_SOURCE"],
        "frame_sensitive_units": counts["DISAGREEMENT"] + counts["UNDERDETERMINED_FROM_SOURCE"],
    }
    for field, value in expected.items():
        if review["metrics"][field] != value:
            errors.append(("REVIEW_METRIC", field))
    total = len(comparisons)
    determined = counts["AGREEMENT"] + counts["DISAGREEMENT"]
    fractions = {
        "raw_agreement_fraction": round(counts["AGREEMENT"] / total, 4),
        "raw_disagreement_fraction": round(counts["DISAGREEMENT"] / total, 4),
        "raw_underdetermined_fraction": round(counts["UNDERDETERMINED_FROM_SOURCE"] / total, 4),
        "agreement_on_determined_units": round(counts["AGREEMENT"] / determined, 4),
        "frame_sensitive_fraction": round(expected["frame_sensitive_units"] / total, 4),
    }
    for field, value in fractions.items():
        if review["metrics"][field] != value:
            errors.append(("REVIEW_METRIC", field))
    if set(review["review_axes"]) != {"mapping", "source", "domain"}:
        errors.append(("REVIEW_AXIS", "mapping/source/domain"))
    if review["method"]["prior_atlas_exposure"] is not True or review["method"]["blinded"] is not False:
        errors.append(("REVIEW_EXPOSURE", "prior exposure must remain disclosed"))
    return errors


def composition_semantic_errors(composition: dict[str, Any]) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []

    def reject(code: str, detail: str) -> None:
        errors.append((code, detail))

    bindings = composition["source_bindings"]
    binding_ids = [binding["binding_id"] for binding in bindings]
    if len(binding_ids) != len(set(binding_ids)):
        reject("UNIQUE_ID", "composition source binding")
    binding_by_id = {binding["binding_id"]: binding for binding in bindings}
    owners = {binding["source_owner"] for binding in bindings}
    required_owners = {
        "gu-formalization", "possibility-to-capability", "time-as-finality",
        "temporal-issuance", "continuity-ledger",
    }
    if not required_owners.issubset(owners):
        reject("COMPOSITION_SOURCE_SET", str(sorted(owners)))
    predecessor = binding_by_id.get("SRC-DU-ATLAS-RING-V01", {})
    if predecessor.get("role") != "ATLAS_PREDECESSOR":
        reject("COMPOSITION_ATLAS_ROLE", "receiver-owned atlas cast as physics")
    tool_binding = binding_by_id.get("SRC-P2C-DIAGNOSTIC-TOOL-V01", {})
    if not (
        tool_binding.get("source_owner") == "possibility-to-capability"
        and tool_binding.get("artifact_locator") == "tools/capability_diagnostic.py"
        and tool_binding.get("content_sha256") == "02f07be767923def2254079afe2f7117b20f53f134b2566279d4688370f70e6d"
        and tool_binding.get("role") == "TRANSITION_DIAGNOSTIC"
    ):
        reject("P2C_TOOL_BINDING", "missing or incorrect executable pin")
    gu = composition["source_closure"]["gu_requirement_crosswalk"]
    if set(gu["rejected_false_friends"]) != {"RA-E6", "LT-SM6"} or len(gu["rejected_false_friends"]) != 2:
        reject("COMPOSITION_GU_FALSE_FRIEND", str(gu["rejected_false_friends"]))
    if composition["source_closure"]["physics_packet"]["status"] != "LITERATURE_GRADE_STIPULATION_NO_PRIMARY_PACKET":
        reject("COMPOSITION_PHYSICS_CLOSURE", "physics packet")
    if composition["source_closure"]["continuity"]["status"] != "PROPOSED_METHOD_ONLY_NOT_RING_INSTANCE":
        reject("COMPOSITION_CLTP_ROLE", "continuity source closure")

    object_ids = [item["object_id"] for item in composition["typed_objects"]]
    map_ids = [item["map_id"] for item in composition["typed_maps"]]
    if len(object_ids) != len(set(object_ids)) or len(map_ids) != len(set(map_ids)):
        reject("UNIQUE_ID", "composition object/map")
    object_set = set(object_ids)
    for item in composition["typed_objects"]:
        if not set(item["source_refs"]).issubset(binding_by_id):
            reject("COMPOSITION_SOURCE_REF", item["object_id"])
    for mapping in composition["typed_maps"]:
        if not set(mapping["domain_refs"] + mapping["codomain_refs"]).issubset(object_set):
            reject("COMPOSITION_MAP_REF", mapping["map_id"])
        if mapping["map_type"] == "MATCHING_RELATION" and mapping["causal"] is not False:
            reject("COMPOSITION_MATCHING_CAUSAL_CAST", mapping["map_id"])
        if mapping["map_type"] == "PHYSICAL_EVOLUTION" and mapping["causal"] is not True:
            reject("COMPOSITION_EVOLUTION_TYPE", mapping["map_id"])
        if not set(mapping["source_refs"]).issubset(binding_by_id):
            reject("COMPOSITION_SOURCE_REF", mapping["map_id"])
    relation_ids = [item["relation_id"] for item in composition["relation_records"]]
    if len(relation_ids) != len(set(relation_ids)):
        reject("UNIQUE_ID", "composition relation")
    admissible_refs = object_set | set(map_ids)
    forbidden_matched = {"SAME_OCCURRENCE", "MATERIAL_CONTINUITY", "EVOLVES_TO"}
    for relation in composition["relation_records"]:
        if relation["from_ref"] not in admissible_refs or relation["to_ref"] not in admissible_refs:
            reject("COMPOSITION_RELATION_REF", relation["relation_id"])
        if (
            relation["frame"] == "MATCHED_COUNTERFACTUAL"
            and relation["relation_type"] in forbidden_matched
            and relation["status"] in {"PRESENT", "CONDITIONAL"}
        ):
            reject("COMPOSITION_MATCHED_IDENTITY_CAST", relation["relation_id"])
    present_relation_edges = [
        (relation["from_ref"], relation["to_ref"])
        for relation in composition["relation_records"]
        if relation["from_ref"] in object_set
        and relation["to_ref"] in object_set
        and relation["status"] in {"PRESENT", "CONDITIONAL"}
    ]
    if _has_cycle(object_set, present_relation_edges):
        reject("COMPOSITION_RELATION_CYCLE", "typed relation graph")
    if {step["layer"] for step in composition["steps"]} != COMPOSITION_LAYERS or len(composition["steps"]) != 6:
        reject("COMPOSITION_STEP_SET", "six layers")
    if not any(
        diagram["kind"] == "FAILED_SQUARE" and diagram["verdict"] == "DOES_NOT_COMMUTE"
        for diagram in composition["diagrams"]
    ):
        reject("COMPOSITION_FAILED_SQUARE", "missing")
    relation_set = set(relation_ids)
    map_set = set(map_ids)
    for diagram in composition["diagrams"]:
        diagram_nodes = set(diagram["nodes"])
        if not diagram_nodes.issubset(object_set):
            reject("COMPOSITION_DIAGRAM_REF", diagram["diagram_id"])
        for arrow in diagram["arrows"]:
            if arrow["from_ref"] not in object_set or arrow["to_ref"] not in object_set:
                reject("COMPOSITION_DIAGRAM_REF", arrow["arrow_id"])
            if arrow["arrow_id"] not in relation_set | map_set:
                reject("COMPOSITION_DIAGRAM_ARROW_REF", arrow["arrow_id"])
        diagram_edges = [
            (arrow["from_ref"], arrow["to_ref"])
            for arrow in diagram["arrows"]
            if arrow["from_ref"] in diagram_nodes and arrow["to_ref"] in diagram_nodes
        ]
        if diagram["kind"] == "RELATION_DAG" and _has_cycle(diagram_nodes, diagram_edges):
            reject("COMPOSITION_RELATION_CYCLE", diagram["diagram_id"])
    if composition["cltp_gate"]["physics_role"] != "NON_GROUNDING":
        reject("COMPOSITION_CLTP_ROLE", "physics role")
    if composition["taf_capability_factorization"]["factorization"] != "FACTORS_THROUGH_RECORD_FORMATION_AND_ERASURE_STRUCTURE":
        reject("COMPOSITION_TAF_FACTORIZATION", "holder access cast")
    if composition["ti_effect"]["operational_residue"] != "RETAINED":
        reject("COMPOSITION_TI_RESIDUE", "operational residue erased")
    if composition["finality"]["verdict"] != "NONE":
        reject("COMPOSITION_FINALITY", "finite persistence promoted")
    diagnostic = composition["p2c_diagnostic"]
    if diagnostic["tool_binding_ref"] not in binding_by_id:
        reject("P2C_TOOL_BINDING", diagnostic["tool_binding_ref"])
    tool_result = diagnostic["tool_result"]
    if not tool_result["branch_results"]:
        reject("P2C_TOOL_RESULT", "missing branch result")
    else:
        components = set(tool_result["branch_results"][0].get("components", []))
        if components != {"FIXED_FAMILY_DYNAMICS", "RECORD_FORMATION", "CAPABILITY_ENLARGEMENT"}:
            reject("P2C_TOOL_RESULT", str(sorted(components)))
    if diagnostic["physics_truth_verified"] is not False:
        reject("P2C_TOOL_TRUTH_CAST", "classifier cannot verify physics")
    if set(composition["composition_verdict"]["source_closure_failures"]) != {
        "GU_TYPED_ARROW_MISSING", "PHYSICS_PACKET_LITERATURE_STIPULATION"
    }:
        reject("COMPOSITION_SOURCE_CLOSURE", "failure set")
    if composition["composition_verdict"]["grade"] != 1:
        reject("COMPOSITION_VERDICT_GRADE", str(composition["composition_verdict"]["grade"]))
    controls = [item["control_id"] for item in composition["hostile_controls"]]
    if set(controls) != {"CTRL-GU-FALSE-FRIEND", "CTRL-MATCHED-RELATION-CAST"} or len(controls) != 2:
        reject("COMPOSITION_CONTROL_SET", str(controls))
    if any(item["grade"] > composition["evidence_ceiling"] for item in composition["typed_objects"] + composition["typed_maps"]):
        reject("EVIDENCE_CEILING", "composition object/map")
    if any(step["grade"] > composition["evidence_ceiling"] for step in composition["steps"]):
        reject("EVIDENCE_CEILING", "composition step")
    return errors


def _binding_digest_errors(bindings: list[dict[str, Any]]) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    for binding in bindings:
        repo = REPO_ROOTS.get(binding["source_owner"])
        if repo is None:
            errors.append(("SOURCE_OWNER", binding["binding_id"]))
            continue
        payload = _git_bytes(repo, binding["immutable_revision"], binding["artifact_locator"])
        if payload is None:
            errors.append(("SOURCE_PIN", binding["binding_id"]))
        elif hashlib.sha256(payload).hexdigest() != binding["content_sha256"]:
            errors.append(("SOURCE_DIGEST", binding["binding_id"]))
    return errors


def _p2c_execution_errors(composition: dict[str, Any]) -> list[tuple[str, str]]:
    """Execute the pinned P2C evaluator and reproduce the embedded receipt."""
    by_id = {item["binding_id"]: item for item in composition["source_bindings"]}
    binding = by_id.get(composition["p2c_diagnostic"]["tool_binding_ref"])
    if binding is None:
        return [("P2C_TOOL_BINDING", "binding ref missing")]
    repo = REPO_ROOTS.get(binding["source_owner"])
    if repo is None:
        return [("P2C_TOOL_BINDING", "owner missing")]
    payload = _git_bytes(repo, binding["immutable_revision"], binding["artifact_locator"])
    if payload is None or hashlib.sha256(payload).hexdigest() != binding["content_sha256"]:
        return [("P2C_TOOL_BINDING", "pinned executable unavailable or digest mismatch")]
    namespace: dict[str, Any] = {"__name__": "pinned_p2c_capability_diagnostic"}
    try:
        exec(compile(payload, binding["artifact_locator"], "exec"), namespace)
        actual = namespace["evaluate_assessment"](
            copy.deepcopy(composition["p2c_diagnostic"]["assessment"])
        )
    except Exception as exc:  # noqa: BLE001 - a pinned tool failure must fail closed
        return [("P2C_TOOL_EXECUTION", f"{type(exc).__name__}: {exc}")]
    expected = composition["p2c_diagnostic"]["tool_result"]
    if actual != expected:
        return [("P2C_TOOL_RESULT", "embedded receipt differs from pinned evaluator")]
    if not actual.get("valid") or actual.get("aggregate_outcome") != "MULTI_LEVEL":
        return [("P2C_TOOL_RESULT", "expected valid MULTI_LEVEL")]
    branch_results = actual.get("branch_results", [])
    if len(branch_results) != 1 or set(branch_results[0].get("components", [])) != {
        "FIXED_FAMILY_DYNAMICS", "RECORD_FORMATION", "CAPABILITY_ENLARGEMENT"
    }:
        return [("P2C_TOOL_RESULT", "component set mismatch")]
    if actual.get("label_invariance", {}).get("invariant") is not True:
        return [("P2C_TOOL_RESULT", "label invariance failed")]
    return []


def release_semantic_errors(
    release: dict[str, Any], card: dict[str, Any], review: dict[str, Any],
    composition: dict[str, Any], *, verify_digests: bool,
) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    specimens = release["v02_specimens"]
    if specimens["card_count"] != 1 or specimens["card_ids"] != [card["card_id"]]:
        errors.append(("RELEASE_CARD_SET", "card count/identity"))
    if specimens["review_count"] != 1 or specimens["review_ids"] != [review["review_id"]]:
        errors.append(("RELEASE_REVIEW_SET", "review count/identity"))
    if specimens["composition_count"] != 1 or specimens["composition_ids"] != [composition["composition_id"]]:
        errors.append(("RELEASE_COMPOSITION_SET", "composition count/identity"))
    predecessor = card["lineage"]
    legacy_atlas = release["legacy_v01"]["artifacts"]["atlas"]
    if (
        predecessor["predecessor_card_id"] not in release["legacy_v01"]["card_ids"]
        or predecessor["predecessor_artifact"] != legacy_atlas["path"]
        or predecessor["predecessor_sha256"] != legacy_atlas["sha256"]
    ):
        errors.append(("RELEASE_PREDECESSOR", "card lineage differs from frozen v0.1 atlas"))
    if predecessor["predecessor_card_id"] != card["card_id"]:
        errors.append(("RELEASE_PREDECESSOR_IDENTITY", "additive remap changes specimen identity"))
    if (
        card["review_status"]["review_artifact"] != specimens["artifacts"]["review"]["path"]
        or review["card_ref"] != card["card_id"]
    ):
        errors.append(("RELEASE_REVIEW_LINK", "card, review, and frozen review path disagree"))
    if release["validator"]["hostile_mutation_ids"] != MUTATION_IDS:
        errors.append(("RELEASE_MUTATION_SET", "mutation order/identity"))
    if verify_digests:
        artifact_groups = [
            release["legacy_v01"]["artifacts"], specimens["artifacts"],
            release["schemas"],
        ]
        for group in artifact_groups:
            for name, artifact in group.items():
                path = ROOT / artifact["path"]
                if not path.is_file():
                    errors.append(("RELEASE_ARTIFACT", f"{name}:{artifact['path']}"))
                elif _sha256(path) != artifact["sha256"]:
                    errors.append(("RELEASE_DIGEST", f"{name}:{artifact['path']}"))
        probe_path = ROOT / release["validator"]["probe_path"]
        if not probe_path.is_file() or _sha256(probe_path) != release["validator"]["probe_sha256"]:
            errors.append(("RELEASE_DIGEST", "validator probe"))
    return errors


def _load_state() -> dict[str, Any]:
    return {
        "card": _read_json(CARD), "release": _read_json(RELEASE),
        "review": _read_json(REVIEW), "composition": _read_json(COMPOSITION),
        "card_schema": _read_json(CARD_SCHEMA), "release_schema": _read_json(RELEASE_SCHEMA),
        "review_schema": _read_json(REVIEW_SCHEMA), "composition_schema": _read_json(COMPOSITION_SCHEMA),
    }


def _scalability_control_errors(state: dict[str, Any]) -> list[tuple[str, str]]:
    """Prove core-card extensibility without widening this frozen release."""
    errors: list[tuple[str, str]] = []
    synthetic = copy.deepcopy(state["card"])
    synthetic["card_id"] = "DU-PCA-999"
    if _schema_code(synthetic, state["card_schema"]) is not None:
        errors.append(("SCALABILITY_CONTROL", "synthetic card fails the core schema"))
    if card_semantic_errors(synthetic):
        errors.append(("SCALABILITY_CONTROL", "synthetic card fails core semantics"))

    expanded_release = copy.deepcopy(state["release"])
    expanded_release["v02_specimens"]["card_count"] = 2
    expanded_release["v02_specimens"]["card_ids"] = [
        state["card"]["card_id"], synthetic["card_id"],
    ]
    if _schema_code(expanded_release, state["release_schema"]) != "JSON_SCHEMA":
        errors.append(("SCALABILITY_CONTROL", "frozen release accepts an extra card"))
    return errors


def all_error_codes(state: dict[str, Any], *, verify_digests: bool) -> set[str]:
    codes: set[str] = set()
    pairs = (
        ("card", "card_schema"), ("release", "release_schema"),
        ("review", "review_schema"), ("composition", "composition_schema"),
    )
    valid: dict[str, bool] = {}
    for instance_name, schema_name in pairs:
        code = _schema_code(state[instance_name], state[schema_name])
        valid[instance_name] = code is None
        if code:
            codes.add(code)
    if valid["card"]:
        codes.update(code for code, _ in card_semantic_errors(state["card"]))
    if valid["review"]:
        codes.update(code for code, _ in review_semantic_errors(state["review"]))
    if valid["composition"]:
        codes.update(code for code, _ in composition_semantic_errors(state["composition"]))
    if all(valid.values()):
        codes.update(
            code for code, _ in release_semantic_errors(
                state["release"], state["card"], state["review"],
                state["composition"], verify_digests=verify_digests,
            )
        )
    return codes


Mutation = tuple[str, str, Callable[[dict[str, Any]], None]]


def _mutation_cases() -> list[Mutation]:
    def unknown_property(s: dict[str, Any]) -> None:
        s["card"]["schema_was_optional"] = True

    def unsupported_keyword(s: dict[str, Any]) -> None:
        s["card_schema"]["allOf"] = []

    def legacy_status(s: dict[str, Any]) -> None:
        s["card"]["record_graph"]["nodes"][0]["status"] = "ESTABLISHED"

    def missing_review_axis(s: dict[str, Any]) -> None:
        del s["card"]["review_status"]["source"]

    def adapter_eligibility(s: dict[str, Any]) -> None:
        s["card"]["source_bindings"][0]["phenomenon_eligible"] = True

    def accepted_without_grounding(s: dict[str, Any]) -> None:
        for binding in s["card"]["source_bindings"]:
            binding["claim_role"] = "CAPABILITY_METHOD"
            binding["physics_grounding"] = {
                "status": "NON_GROUNDING", "independent_of_atlas_mapping": False,
                "basis": "hostile mutation",
            }
        s["card"]["physics"]["physics_grounding_refs"] = []

    def gu_grounding(s: dict[str, Any]) -> None:
        binding = s["card"]["source_bindings"][0]
        binding["source_owner"] = "gu-formalization"
        binding["claim_role"] = "PHYSICS_GROUNDING"

    def accepted_domain_gap(s: dict[str, Any]) -> None:
        s["card"]["review_status"]["domain"] = "PRIMARY_AUDIT_REQUIRED"

    def release_count(s: dict[str, Any]) -> None:
        s["release"]["v02_specimens"]["card_count"] = 2

    def release_id(s: dict[str, Any]) -> None:
        s["card"]["card_id"] = "DU-PCA-999"

    def release_digest(s: dict[str, Any]) -> None:
        s["release"]["v02_specimens"]["artifacts"]["card"]["sha256"] = "0" * 64

    def schema_digest(s: dict[str, Any]) -> None:
        s["release"]["schemas"]["card"]["sha256"] = "0" * 64

    def predecessor_digest(s: dict[str, Any]) -> None:
        s["card"]["lineage"]["predecessor_sha256"] = "0" * 64

    def source_digest(s: dict[str, Any]) -> None:
        s["card"]["source_bindings"][0]["content_sha256"] = "0" * 64

    def predecessor_identity(s: dict[str, Any]) -> None:
        s["card"]["lineage"]["predecessor_card_id"] = "DU-PCA-999"

    def review_artifact_ref(s: dict[str, Any]) -> None:
        s["card"]["review_status"]["review_artifact"] = "reviews/not-the-frozen-review.json"

    def projection_constant(s: dict[str, Any]) -> None:
        s["card"]["projection_audit"]["sufficiency_status"] = "CONSTANT_ON_FIBRES"

    def projection_zero(s: dict[str, Any]) -> None:
        s["card"]["projection_audit"]["spread_status"] = "ZERO"

    def projection_not_tested(s: dict[str, Any]) -> None:
        s["card"]["projection_audit"]["sufficiency_status"] = "NOT_TESTED"

    def relation_arity(s: dict[str, Any]) -> None:
        node = next(node for node in s["card"]["record_graph"]["nodes"] if node["node_kind"] == "RELATION_RECORD")
        node["relates"] = []

    def graph_cycle(s: dict[str, Any]) -> None:
        edge = s["card"]["record_graph"]["edges"][0]
        candidate = copy.deepcopy(edge)
        candidate["edge_id"] = "EDGE-HOSTILE-CYCLE"
        candidate["from"], candidate["to"] = edge["to"], edge["from"]
        s["card"]["record_graph"]["edges"].append(candidate)

    def missing_kill(s: dict[str, Any]) -> None:
        del s["card"]["evidence"]["challenges"]["representation_kill"]

    def discriminator_no_outcomes(s: dict[str, Any]) -> None:
        held = s["card"]["evidence"]["challenges"]["held_out_discriminator"]
        held["status"] = "SUPPLIED"
        held["opposed_outcomes"] = []

    def metric_drift(s: dict[str, Any]) -> None:
        s["review"]["metrics"]["agreement"] = 26

    def review_collapse(s: dict[str, Any]) -> None:
        del s["review"]["review_axes"]["domain"]

    def gu_false_friend(s: dict[str, Any]) -> None:
        s["composition"]["source_closure"]["gu_requirement_crosswalk"]["rejected_false_friends"] = ["RA-E6", "RA-E6"]

    def _matched_cast(s: dict[str, Any], relation_type: str) -> None:
        matched = next(item for item in s["composition"]["relation_records"] if item["relation_type"] == "MATCHED_WITH")
        hostile = copy.deepcopy(matched)
        hostile["relation_id"] = f"REL-HOSTILE-{relation_type.replace('_', '-')}"
        hostile["relation_type"] = relation_type
        hostile["status"] = "PRESENT"
        hostile["frame"] = "MATCHED_COUNTERFACTUAL"
        s["composition"]["relation_records"].append(hostile)

    def same_occurrence(s: dict[str, Any]) -> None:
        _matched_cast(s, "SAME_OCCURRENCE")

    def matched_evolution(s: dict[str, Any]) -> None:
        _matched_cast(s, "EVOLVES_TO")

    def dangling_endpoint(s: dict[str, Any]) -> None:
        s["composition"]["relation_records"][0]["to_ref"] = "OBJ-NOT-DECLARED"

    def atlas_role_leak(s: dict[str, Any]) -> None:
        binding = next(
            item for item in s["composition"]["source_bindings"]
            if item["binding_id"] == "SRC-DU-ATLAS-RING-V01"
        )
        binding["role"] = "PHYSICS_STIPULATION"

    def p2c_result_drift(s: dict[str, Any]) -> None:
        result = s["composition"]["p2c_diagnostic"]["tool_result"]["branch_results"][0]
        result["components"] = ["ACCESS_CHANGE"]

    def cltp_physics(s: dict[str, Any]) -> None:
        s["composition"]["cltp_gate"]["physics_role"] = "PHYSICS_GROUNDING"

    def finality_promotion(s: dict[str, Any]) -> None:
        s["composition"]["finality"]["verdict"] = "PUBLIC_CANDIDATE"

    def ti_erasure(s: dict[str, Any]) -> None:
        s["composition"]["ti_effect"]["operational_residue"] = "ERASED"

    def grade_promotion(s: dict[str, Any]) -> None:
        s["card"]["evidence"]["atlas_grade"] = 3

    def routing_promotion(s: dict[str, Any]) -> None:
        s["release"]["routing"]["non_routing"] = False

    return [
        ("unknown_schema_property", "JSON_SCHEMA", unknown_property),
        ("unsupported_schema_keyword", "SCHEMA_ENGINE_UNSUPPORTED", unsupported_keyword),
        ("legacy_record_status", "JSON_SCHEMA", legacy_status),
        ("missing_review_axis", "JSON_SCHEMA", missing_review_axis),
        ("adapter_level_eligibility", "JSON_SCHEMA", adapter_eligibility),
        ("accepted_without_independent_grounding", "ACCEPTED_PHYSICS_GROUNDING", accepted_without_grounding),
        ("gu_requirement_as_physics_grounding", "GU_REQUIREMENT_BINDING", gu_grounding),
        ("accepted_with_domain_gap", "ACCEPTED_PHYSICS_REVIEW", accepted_domain_gap),
        ("release_card_count_drift", "JSON_SCHEMA", release_count),
        ("release_card_id_drift", "RELEASE_CARD_SET", release_id),
        ("release_digest_drift", "RELEASE_DIGEST", release_digest),
        ("schema_digest_drift", "RELEASE_DIGEST", schema_digest),
        ("predecessor_digest_drift", "JSON_SCHEMA", predecessor_digest),
        ("source_digest_drift", "SOURCE_DIGEST", source_digest),
        ("predecessor_card_identity_drift", "RELEASE_PREDECESSOR_IDENTITY", predecessor_identity),
        ("review_artifact_ref_drift", "RELEASE_REVIEW_LINK", review_artifact_ref),
        ("projection_constant_nonzero", "PROJECTION_CONSTANCY", projection_constant),
        ("projection_varies_zero", "PROJECTION_CONSTANCY", projection_zero),
        ("projection_not_tested_with_witness", "PROJECTION_CONSTANCY", projection_not_tested),
        ("relation_record_missing_subjects", "RELATION_RECORD_ARITY", relation_arity),
        ("record_graph_cycle", "RECORD_GRAPH_CYCLE", graph_cycle),
        ("missing_representation_kill", "JSON_SCHEMA", missing_kill),
        ("supplied_discriminator_without_outcomes", "HELD_OUT_DISCRIMINATOR", discriminator_no_outcomes),
        ("review_metric_drift", "JSON_SCHEMA", metric_drift),
        ("review_axis_collapse", "JSON_SCHEMA", review_collapse),
        ("composition_gu_false_friend", "COMPOSITION_GU_FALSE_FRIEND", gu_false_friend),
        ("composition_matched_as_same_occurrence", "COMPOSITION_MATCHED_IDENTITY_CAST", same_occurrence),
        ("composition_matched_as_evolution", "COMPOSITION_MATCHED_IDENTITY_CAST", matched_evolution),
        ("composition_dangling_endpoint", "COMPOSITION_RELATION_REF", dangling_endpoint),
        ("composition_atlas_predecessor_role_leak", "COMPOSITION_ATLAS_ROLE", atlas_role_leak),
        ("p2c_tool_result_drift", "P2C_TOOL_RESULT", p2c_result_drift),
        ("composition_cltp_as_physics", "JSON_SCHEMA", cltp_physics),
        ("composition_finality_promotion", "JSON_SCHEMA", finality_promotion),
        ("composition_ti_erases_residue", "JSON_SCHEMA", ti_erasure),
        ("evidence_grade_promotion", "JSON_SCHEMA", grade_promotion),
        ("routing_promotion", "JSON_SCHEMA", routing_promotion),
    ]


def _result_payload(state: dict[str, Any], rejected: list[str]) -> dict[str, Any]:
    return {
        "artifact_type": "phenomenon_capability_atlas_v02_first_run_check",
        "release": str(RELEASE.relative_to(ROOT)),
        "status": "pass",
        "schema_engine": "stdlib_fail_closed_supported_draft_2020_12_vocabulary",
        "validated_instance_count": 4,
        "validated_instances": [
            str(CARD.relative_to(ROOT)), str(REVIEW.relative_to(ROOT)),
            str(COMPOSITION.relative_to(ROOT)), str(RELEASE.relative_to(ROOT)),
        ],
        "legacy_card_count": state["release"]["legacy_v01"]["card_count"],
        "v02_card_count": state["release"]["v02_specimens"]["card_count"],
        "review_comparison_count": len(state["review"]["field_comparisons"]),
        "composition_step_count": len(state["composition"]["steps"]),
        "validated_invariant_count": len(INVARIANT_IDS),
        "validated_invariants": INVARIANT_IDS,
        "hostile_mutation_count": len(rejected),
        "rejected_mutations": rejected,
        "evidence_ceiling": 2,
        "routing_changed": False,
        "scientific_claims_validated": False,
        "note": (
            "Passing establishes frozen-release, source-custody, type, and "
            "representation integrity only; it does not establish scientific "
            "truth, novelty, ontology, finality, issuance, or research priority."
        ),
    }


def run(*, compare_receipt: bool = True) -> dict[str, Any]:
    state = _load_state()
    base_codes = all_error_codes(state, verify_digests=True)
    base_codes.update(code for code, _ in _binding_digest_errors(state["card"]["source_bindings"]))
    base_codes.update(code for code, _ in _binding_digest_errors(state["composition"]["source_bindings"]))
    base_codes.update(code for code, _ in _p2c_execution_errors(state["composition"]))
    base_codes.update(code for code, _ in _scalability_control_errors(state))
    review_binding = {
        "binding_id": state["review"]["source_freeze"]["binding_id"],
        "source_owner": state["review"]["source_freeze"]["source_owner"],
        "immutable_revision": state["review"]["source_freeze"]["immutable_revision"],
        "artifact_locator": state["review"]["source_freeze"]["artifact_locator"],
        "content_sha256": state["review"]["source_freeze"]["content_sha256"],
    }
    base_codes.update(code for code, _ in _binding_digest_errors([review_binding]))
    if base_codes:
        raise AssertionError(f"base_validation: {sorted(base_codes)}")

    cases = _mutation_cases()
    if [mutation_id for mutation_id, _code, _mutate in cases] != MUTATION_IDS:
        raise AssertionError("mutation_registry: implementation differs from frozen manifest")
    rejected: list[str] = []
    for mutation_id, expected_code, mutate in cases:
        candidate = copy.deepcopy(state)
        mutate(candidate)
        codes = all_error_codes(
            candidate,
            verify_digests=mutation_id in {"release_digest_drift", "schema_digest_drift"},
        )
        if mutation_id == "source_digest_drift":
            codes.update(
                code for code, _ in _binding_digest_errors(candidate["card"]["source_bindings"])
            )
        if expected_code not in codes:
            raise AssertionError(
                f"mutation_control: {mutation_id} did not produce {expected_code}; "
                f"got {sorted(codes)}"
            )
        rejected.append(mutation_id)

    result = _result_payload(state, rejected)
    if compare_receipt:
        checked_in = _read_json(OUTPUT)
        if checked_in != result:
            raise AssertionError("receipt_drift: checked-in artifact differs from deterministic result")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--emit-expected-receipt", action="store_true",
        help="print the deterministic receipt without comparing the checked-in copy",
    )
    args = parser.parse_args()
    result = run(compare_receipt=not args.emit_expected_receipt)
    if args.emit_expected_receipt:
        print(json.dumps(result, indent=2))
    else:
        print(
            "PASS: "
            f"{result['validated_instance_count']} instances; "
            f"{result['validated_invariant_count']} invariants; "
            f"{result['hostile_mutation_count']}/{result['hostile_mutation_count']} "
            "hostile mutations rejected"
        )
