#!/usr/bin/env python3
"""Validate the HC-DU-036F novelty and reachability disposition.

This probe does not contact a provider, run a quantum simulator, establish
literature novelty, or make a physical claim.  It freezes and checks:

1. which scientific components are already occupied by nearby primary work;
2. which capabilities current public provider documentation actually
   promises, without converting silence into absence;
3. the claim ceiling of each experimental rung; and
4. the decision rule for formalize, pilot, partner, stop, and reopen actions.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_interventional_sufficiency_reachability_gate_result.json"
)
RUN_ID = "RUN-20260726-093934-interventional-sufficiency-go-no-go"

DOCUMENTED = "DOCUMENTED"
DOCUMENTED_BOUNDED = "DOCUMENTED_BOUNDED"
NOT_DOCUMENTED = "NOT_DOCUMENTED"
INTERFACE_REVIEW_REQUIRED = "INTERFACE_REVIEW_REQUIRED"
DEVICE_DEPENDENT = "DEVICE_DEPENDENT"

PILOT_FIELDS = {
    "mid_circuit_measurement_and_control",
    "shot_joined_named_results",
    "job_and_circuit_provenance",
}
PHYSICAL_ADJUDICATION_FIELDS = {
    "all_physical_triggers_and_retries",
    "invalid_rejected_rows_and_reasons",
    "retained_memory_inventory",
    "independently_witnessed_complete_reset",
}


SOURCE_COLLISION: list[dict[str, Any]] = [
    {
        "source_id": "Pollock-et-al-2018-process-tensor",
        "primary_url": "https://doi.org/10.1103/PhysRevA.97.012127",
        "occupies": [
            "multi_time_process_representation",
            "arbitrary_intervention_response",
        ],
    },
    {
        "source_id": "White-et-al-2020-experimental-process-tensor",
        "primary_url": "https://doi.org/10.1038/s41467-020-20113-3",
        "occupies": [
            "held_out_multi_time_prediction",
            "causal_break_memory_blocking",
            "restricted_instrument_warning",
        ],
    },
    {
        "source_id": "White-et-al-2022-process-tensor-tomography",
        "primary_url": "https://doi.org/10.1103/PRXQuantum.3.020344",
        "occupies": [
            "non_markovian_process_tomography",
            "physicality_constrained_reconstruction",
        ],
    },
    {
        "source_id": "Taranto-et-al-2019-quantum-Markov-order",
        "primary_url": "https://doi.org/10.1103/PhysRevA.99.042108",
        "occupies": [
            "instrument_specific_memory",
            "finite_memory_causal_break_structure",
        ],
    },
    {
        "source_id": "Rudinger-et-al-2021-QILGST",
        "primary_url": "https://arxiv.org/abs/2103.03008",
        "occupies": [
            "mid_circuit_quantum_instrument_characterization",
            "classical_and_quantum_measurement_outputs",
        ],
    },
    {
        "source_id": "Branciard-2011-detection-loophole",
        "primary_url": "https://doi.org/10.1103/PhysRevA.83.032123",
        "occupies": [
            "selection_conditioning_can_change_inference",
            "postselection_requires_explicit_null_model",
        ],
    },
]


INTEGRATED_CONTRACT = {
    "obligations": [
        "independently_frozen_observer_indexed_record_quotient",
        "all_acquisition_strata_including_invalid_and_rejected_rows",
        "target_independent_physically_admissible_resource_accounted_completion_class",
        "verified_reset_over_every_admitted_retained_memory",
        "one_factorization_refinement_remainder_incomplete_contract_adjudicator",
    ],
    "single_primary_source_status": "NOT_LOCATED_SEARCH_INCOMPLETE",
    "novelty_status": "UNRESOLVED_NOT_PROMOTED",
}


PROVIDERS: list[dict[str, Any]] = [
    {
        "provider": "IBM Quantum",
        "official_sources": [
            "https://quantum.cloud.ibm.com/docs/en/guides/execute-dynamic-circuits",
            "https://quantum.cloud.ibm.com/docs/en/guides/sampler-input-output",
            "https://quantum.cloud.ibm.com/docs/en/guides/save-jobs",
        ],
        "capabilities": {
            "mid_circuit_measurement_and_control": DOCUMENTED,
            "shot_joined_named_results": DOCUMENTED,
            "job_and_circuit_provenance": DOCUMENTED,
            "execution_timing": DOCUMENTED_BOUNDED,
            "all_physical_triggers_and_retries": NOT_DOCUMENTED,
            "invalid_rejected_rows_and_reasons": NOT_DOCUMENTED,
            "retained_memory_inventory": NOT_DOCUMENTED,
            "independently_witnessed_complete_reset": NOT_DOCUMENTED,
        },
    },
    {
        "provider": "Quantinuum",
        "official_sources": [
            "https://docs.quantinuum.com/systems/user_guide/hardware_user_guide/h2.html",
            "https://docs.quantinuum.com/systems/trainings/h2/getting_started/mcmr.html",
        ],
        "capabilities": {
            "mid_circuit_measurement_and_control": DOCUMENTED,
            "shot_joined_named_results": INTERFACE_REVIEW_REQUIRED,
            "job_and_circuit_provenance": INTERFACE_REVIEW_REQUIRED,
            "execution_timing": NOT_DOCUMENTED,
            "all_physical_triggers_and_retries": NOT_DOCUMENTED,
            "invalid_rejected_rows_and_reasons": NOT_DOCUMENTED,
            "retained_memory_inventory": NOT_DOCUMENTED,
            "independently_witnessed_complete_reset": NOT_DOCUMENTED,
        },
    },
    {
        "provider": "Rigetti QCS",
        "official_sources": [
            "https://docs.rigetti.com/qcs/guides/quil/dynamic-control-flow",
            "https://docs.rigetti.com/qcs/troubleshooting",
        ],
        "capabilities": {
            "mid_circuit_measurement_and_control": DOCUMENTED,
            "shot_joined_named_results": DOCUMENTED_BOUNDED,
            "job_and_circuit_provenance": INTERFACE_REVIEW_REQUIRED,
            "execution_timing": NOT_DOCUMENTED,
            "all_physical_triggers_and_retries": NOT_DOCUMENTED,
            "invalid_rejected_rows_and_reasons": NOT_DOCUMENTED,
            "retained_memory_inventory": NOT_DOCUMENTED,
            "independently_witnessed_complete_reset": NOT_DOCUMENTED,
        },
    },
    {
        "provider": "IonQ",
        "official_sources": [
            "https://docs.ionq.com/api-reference/v0.4/jobs/get-job",
            "https://docs.ionq.com/sdks/cirq/index",
        ],
        "capabilities": {
            "mid_circuit_measurement_and_control": INTERFACE_REVIEW_REQUIRED,
            "shot_joined_named_results": DOCUMENTED_BOUNDED,
            "job_and_circuit_provenance": DOCUMENTED,
            "execution_timing": NOT_DOCUMENTED,
            "all_physical_triggers_and_retries": NOT_DOCUMENTED,
            "invalid_rejected_rows_and_reasons": NOT_DOCUMENTED,
            "retained_memory_inventory": NOT_DOCUMENTED,
            "independently_witnessed_complete_reset": NOT_DOCUMENTED,
        },
    },
    {
        "provider": "Amazon Braket",
        "official_sources": [
            "https://docs.aws.amazon.com/braket/latest/developerguide/braket-result-types.html",
            "https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-tasks-to-braket.html",
        ],
        "capabilities": {
            "mid_circuit_measurement_and_control": DEVICE_DEPENDENT,
            "shot_joined_named_results": DEVICE_DEPENDENT,
            "job_and_circuit_provenance": DOCUMENTED,
            "execution_timing": DOCUMENTED_BOUNDED,
            "all_physical_triggers_and_retries": NOT_DOCUMENTED,
            "invalid_rejected_rows_and_reasons": NOT_DOCUMENTED,
            "retained_memory_inventory": NOT_DOCUMENTED,
            "independently_witnessed_complete_reset": NOT_DOCUMENTED,
        },
    },
]


CLAIM_LADDER = [
    {
        "rung": "L0_SYNTHETIC_STRUCTURE",
        "maximum_claim": "contract_and_corruption_controls_only",
        "current_status": "COMPLETE",
    },
    {
        "rung": "L1_PROVIDER_RETURNED_SHOTS",
        "maximum_claim": "provider_visible_instrument_kill_or_calibration",
        "current_status": "READY_ONLY_AFTER_DIRECT_AUTHORIZATION",
    },
    {
        "rung": "L2_CLOUD_API_BOUNDARY",
        "maximum_claim": "record_sufficiency_relative_to_the_declared_API_boundary",
        "current_status": "REACHABLE_BUT_NOT_PHYSICAL_SUBSTRATE",
    },
    {
        "rung": "L3_IMPLEMENTATION_COMPLETE_PROCESS",
        "maximum_claim": "one_platform_physical_factorization_or_remainder_candidate",
        "current_status": "PARTNER_GATED",
    },
    {
        "rung": "L4_FROZEN_COMPLETION_CLASS",
        "maximum_claim": "completion_class_relative_reconstruction_or_remainder",
        "current_status": "DEPENDS_ON_L3_AND_FORMAL_CLASS_DEFENSE",
    },
    {
        "rung": "L5_NEW_PHYSICS",
        "maximum_claim": "standard_quantum_null_failure_across_independent_platforms",
        "current_status": "NOT_REACHED",
    },
]


LOCAL_LEARNING_FRONTIER = [
    {
        "work": "integrated_contract_theorem_or_absorption",
        "execution": "LOCAL",
        "significant_outcome": (
            "exact_theorem_no_go_or_source_pinned_absorption_and_stop"
        ),
    },
    {
        "work": "finite_identifiability_and_counterexample_search",
        "execution": "LOCAL",
        "significant_outcome": (
            "tight_observability_bound_or_minimal_indistinguishable_process_pair"
        ),
    },
    {
        "work": "minimum_discriminating_experiment_and_sample_complexity",
        "execution": "LOCAL",
        "significant_outcome": (
            "smallest_measurement_reset_and_shot_contract_that_changes_the_claim"
        ),
    },
    {
        "work": "simulation_of_the_frozen_instrument",
        "execution": "LOCAL",
        "significant_outcome": "implementation_kill_or_calibration_only",
    },
    {
        "work": "physical_remainder_adjudication",
        "execution": "EXTERNAL_EVIDENCE_REQUIRED",
        "significant_outcome": "one_platform_physical_result",
    },
    {
        "work": "new_physics_adjudication",
        "execution": "EXTERNAL_EVIDENCE_REQUIRED",
        "significant_outcome": "independent_cross_platform_standard_null_failure",
    },
]


EXTERNAL_HARDWARE_POSTURE = {
    "default_availability": "ASSUME_UNAVAILABLE",
    "local_exhaustion_requirements": [
        "integrated_theorem_or_absorption_gate_completed",
        "minimum_physical_discriminator_and_standard_null_frozen",
        "local_counterexample_and_existing_data_routes_exhausted",
        "external_hardware_shown_to_be_the_irreducible_next_dependency",
    ],
    "boundary_action": (
        "record_and_send_one_awareness_note_describing_the_available_external_"
        "path_what_it_would_decide_and_the_local_fallback"
    ),
    "authorization_rule": "JOE_SEPARATELY_AUTHORIZES_ANY_EXTERNAL_PURSUIT",
    "without_authorization": "TAKE_LOCAL_ALTERNATIVE_OR_PARK_BRANCH",
    "anti_circling_rule": (
        "NO_REPEAT_PROVIDER_SEARCH_ADAPTER_BUILD_OR_HARDWARE_PROPOSAL_WITHOUT_"
        "A_NEW_REOPENER"
    ),
}


def documented_for(provider: dict[str, Any], fields: set[str]) -> bool:
    return all(
        provider["capabilities"].get(field) == DOCUMENTED for field in fields
    )


def decide_route(
    *,
    single_source_match_found: bool,
    collision_sufficient_for_routing: bool,
    pilot_ready: list[str],
    physically_decisive: list[str],
    formal_fallback_ready: bool,
) -> str:
    if single_source_match_found:
        return "ABSORBED_STOP"
    if physically_decisive:
        return "CLOUD_DECISIVE"
    if (
        collision_sufficient_for_routing
        and pilot_ready
        and formal_fallback_ready
    ):
        return "FORMAL_FIRST_PARTNER_GATED"
    return "INCOMPLETE_COLLISION"


def build_result() -> dict[str, Any]:
    provider_names = [provider["provider"] for provider in PROVIDERS]
    pilot_ready = [
        provider["provider"]
        for provider in PROVIDERS
        if documented_for(provider, PILOT_FIELDS)
    ]
    physically_decisive = [
        provider["provider"]
        for provider in PROVIDERS
        if documented_for(provider, PHYSICAL_ADJUDICATION_FIELDS)
    ]
    component_occupancy = {
        occupied
        for source in SOURCE_COLLISION
        for occupied in source["occupies"]
    }
    formal_fallback_ready = all(
        rung["current_status"] != "UNDEFINED"
        for rung in CLAIM_LADDER[:5]
    )
    route = decide_route(
        single_source_match_found=False,
        collision_sufficient_for_routing=True,
        pilot_ready=pilot_ready,
        physically_decisive=physically_decisive,
        formal_fallback_ready=formal_fallback_ready,
    )

    corrupt_not_documented = [
        {
            **provider,
            "capabilities": {
                **provider["capabilities"],
                "all_physical_triggers_and_retries": "DOCUMENTED_ABSENT",
            },
        }
        for provider in PROVIDERS
    ]
    cloud_boundary_promotable = CLAIM_LADDER[2]["maximum_claim"].endswith(
        "physical_substrate"
    )
    locally_significant = [
        item["work"]
        for item in LOCAL_LEARNING_FRONTIER
        if item["execution"] == "LOCAL"
        and item["significant_outcome"] != "implementation_kill_or_calibration_only"
    ]

    checks = {
        "source_collision_has_primary_pointers": all(
            source["primary_url"].startswith(("https://doi.org/", "https://arxiv.org/"))
            for source in SOURCE_COLLISION
        ),
        "multitime_process_component_is_occupied": (
            "multi_time_process_representation" in component_occupancy
        ),
        "instrument_specific_memory_component_is_occupied": (
            "instrument_specific_memory" in component_occupancy
        ),
        "mid_circuit_instrument_characterization_is_occupied": (
            "mid_circuit_quantum_instrument_characterization"
            in component_occupancy
        ),
        "selection_conditioning_component_is_occupied": (
            "selection_conditioning_can_change_inference" in component_occupancy
        ),
        "integrated_conjunction_is_not_promoted_to_novelty": (
            INTEGRATED_CONTRACT["single_primary_source_status"]
            == "NOT_LOCATED_SEARCH_INCOMPLETE"
            and INTEGRATED_CONTRACT["novelty_status"]
            == "UNRESOLVED_NOT_PROMOTED"
        ),
        "provider_names_are_unique": len(provider_names) == len(set(provider_names)),
        "provider_sources_are_official_https_pages": all(
            provider["official_sources"]
            and all(url.startswith("https://") for url in provider["official_sources"])
            for provider in PROVIDERS
        ),
        "only_existing_IBM_bridge_is_pilot_ready_in_scoped_matrix": (
            pilot_ready == ["IBM Quantum"]
        ),
        "no_scoped_standard_provider_is_physically_decisive": (
            physically_decisive == []
        ),
        "not_documented_is_not_documented_absence": all(
            status != "DOCUMENTED_ABSENT"
            for provider in PROVIDERS
            for status in provider["capabilities"].values()
        ),
        "corrupt_absence_promotion_is_detectable": any(
            provider["capabilities"]["all_physical_triggers_and_retries"]
            == "DOCUMENTED_ABSENT"
            for provider in corrupt_not_documented
        ),
        "claim_ladder_has_six_ordered_rungs": (
            [rung["rung"].split("_", 1)[0] for rung in CLAIM_LADDER]
            == [f"L{index}" for index in range(6)]
        ),
        "cloud_API_boundary_is_not_promoted_to_physical_substrate": (
            not cloud_boundary_promotable
            and CLAIM_LADDER[2]["current_status"]
            == "REACHABLE_BUT_NOT_PHYSICAL_SUBSTRATE"
        ),
        "implementation_complete_rung_is_partner_gated": (
            CLAIM_LADDER[3]["current_status"] == "PARTNER_GATED"
        ),
        "new_physics_rung_is_not_reached": (
            CLAIM_LADDER[5]["current_status"] == "NOT_REACHED"
        ),
        "local_computer_retains_three_significant_learning_routes": (
            locally_significant
            == [
                "integrated_contract_theorem_or_absorption",
                "finite_identifiability_and_counterexample_search",
                "minimum_discriminating_experiment_and_sample_complexity",
            ]
        ),
        "local_simulation_is_capped_at_kill_or_calibration": (
            next(
                item
                for item in LOCAL_LEARNING_FRONTIER
                if item["work"] == "simulation_of_the_frozen_instrument"
            )["significant_outcome"]
            == "implementation_kill_or_calibration_only"
        ),
        "physical_remainder_requires_external_evidence": (
            next(
                item
                for item in LOCAL_LEARNING_FRONTIER
                if item["work"] == "physical_remainder_adjudication"
            )["execution"]
            == "EXTERNAL_EVIDENCE_REQUIRED"
        ),
        "new_physics_requires_external_evidence": (
            next(
                item
                for item in LOCAL_LEARNING_FRONTIER
                if item["work"] == "new_physics_adjudication"
            )["execution"]
            == "EXTERNAL_EVIDENCE_REQUIRED"
        ),
        "external_hardware_is_assumed_unavailable_by_default": (
            EXTERNAL_HARDWARE_POSTURE["default_availability"]
            == "ASSUME_UNAVAILABLE"
        ),
        "hardware_boundary_requires_local_exhaustion_and_exact_discriminator": (
            EXTERNAL_HARDWARE_POSTURE["local_exhaustion_requirements"]
            == [
                "integrated_theorem_or_absorption_gate_completed",
                "minimum_physical_discriminator_and_standard_null_frozen",
                "local_counterexample_and_existing_data_routes_exhausted",
                "external_hardware_shown_to_be_the_irreducible_next_dependency",
            ]
        ),
        "hardware_boundary_emits_one_awareness_note_then_routes_or_parks": (
            EXTERNAL_HARDWARE_POSTURE["boundary_action"].startswith(
                "record_and_send_one_awareness_note"
            )
            and EXTERNAL_HARDWARE_POSTURE["without_authorization"]
            == "TAKE_LOCAL_ALTERNATIVE_OR_PARK_BRANCH"
        ),
        "external_path_cannot_recur_without_a_new_reopener": (
            EXTERNAL_HARDWARE_POSTURE["authorization_rule"]
            == "JOE_SEPARATELY_AUTHORIZES_ANY_EXTERNAL_PURSUIT"
            and EXTERNAL_HARDWARE_POSTURE["anti_circling_rule"].startswith(
                "NO_REPEAT_PROVIDER_SEARCH"
            )
        ),
        "formal_fallback_is_well_typed": formal_fallback_ready,
        "route_is_formal_first_and_partner_gated": (
            route == "FORMAL_FIRST_PARTNER_GATED"
        ),
        "provider_switch_without_documented_advantage_does_not_trigger_adapter": (
            pilot_ready == ["IBM Quantum"] and not physically_decisive
        ),
        "single_source_match_would_stop_distinctive_claim": (
            decide_route(
                single_source_match_found=True,
                collision_sufficient_for_routing=True,
                pilot_ready=pilot_ready,
                physically_decisive=physically_decisive,
                formal_fallback_ready=formal_fallback_ready,
            )
            == "ABSORBED_STOP"
        ),
        "documented_decisive_provider_would_reopen_cloud_route": (
            decide_route(
                single_source_match_found=False,
                collision_sufficient_for_routing=True,
                pilot_ready=pilot_ready,
                physically_decisive=["counterfactual-provider"],
                formal_fallback_ready=formal_fallback_ready,
            )
            == "CLOUD_DECISIVE"
        ),
    }

    return {
        "run_id": RUN_ID,
        "claim_grade": (
            "SOURCE-PINNED NOVELTY/REACHABILITY ROUTING CONTROL; "
            "NO NOVELTY, PROVIDER ABSENCE, HARDWARE, OR PHYSICAL VERDICT"
        ),
        "source_collision": SOURCE_COLLISION,
        "integrated_contract": INTEGRATED_CONTRACT,
        "provider_matrix": PROVIDERS,
        "claim_ladder": CLAIM_LADDER,
        "local_learning_frontier": LOCAL_LEARNING_FRONTIER,
        "external_hardware_posture": EXTERNAL_HARDWARE_POSTURE,
        "decision": {
            "route": route,
            "pilot_ready_providers_under_scoped_docs": pilot_ready,
            "physically_decisive_standard_providers_under_scoped_docs": (
                physically_decisive
            ),
            "next_actions": [
                "exhaust_the_local_theorem_or_absorption_gate_before_external_escalation",
                "derive_the_minimum_discriminating_experiment_and_sample_complexity_locally",
                "use_the_existing_IBM_pilot_only_if_authorized_and_decision_changing",
                "seek_an_implementation_complete_partner_packet_only_if_novelty_survives",
            ],
            "external_dependency_trigger": (
                "only_after_a_distinct_formal_result_survives_and_the_minimum_"
                "physical_discriminator_is_defined"
            ),
            "stop_actions": [
                "new_provider_adapter_without_documented_observability_advantage",
                "synthetic_completion_fixture_without_a_new_formal_question",
                "physical_remainder_claim_from_provider_returned_rows",
            ],
        },
        "checks": checks,
        "summary": {
            "passed": sum(checks.values()),
            "total": len(checks),
            "all_passed": all(checks.values()),
        },
    }


def main() -> int:
    result = build_result()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = result["summary"]
    print(
        f"{summary['passed']}/{summary['total']} checks passed; "
        f"route={result['decision']['route']}"
    )
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
