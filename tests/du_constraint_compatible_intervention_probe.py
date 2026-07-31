#!/usr/bin/env python3
"""Exact controls for HC-DU-198's lawful-intervention boundary.

The probe separates three objects that must not be identified:

1. the full mathematical source--port intervention cube;
2. the constraint-compatible surface actually admitted by a physical law; and
3. an independently preparable radiative input sector.

It also audits whether any reviewed gravitational platform supplies the full
source--port--receiver packet required by HC-DU-197.  Passing establishes only
the scoped finite boundary and the recorded primary-source classification.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_constraint_compatible_intervention_result.json"


def constrained_mediator(source: int) -> int:
    """Near-field toy constraint: the port value is fixed by the source."""

    return source


def mediated_near_field(source: int, mediator: int) -> int:
    del source
    return mediator


def direct_near_field(source: int, mediator: int) -> int:
    del mediator
    return source


def radiative_field(source: int, incoming_mode: int) -> int:
    """A lawful free radiative mode modifies receiver response."""

    return source ^ incoming_mode


def near_field_only_rival(source: int, incoming_mode: int) -> int:
    del incoming_mode
    return source


def direct_with_radiative_input(source: int, incoming_mode: int) -> int:
    """A response-equivalent direct presentation using the same free input."""

    return source ^ incoming_mode


def platform_audit() -> dict[str, dict[str, object]]:
    """Frozen qualitative audit, with 0/1/2 indicating absent/partial/full.

    The scores summarize the exact typed packet, not scientific importance.
    `gravity_transfer` is kept separate so an analogue positive control cannot
    accidentally be ranked as a gravitational implementation.
    """

    return {
        "bmv_near_field": {
            "source_family": 2,
            "independent_port_operations": 0,
            "receiver": 2,
            "row_lineage": 1,
            "surgical_isolation": 0,
            "no_refit_target": 2,
            "physical_port_selection": 1,
            "explicit_rivals": 2,
            "gravity_transfer": True,
            "sector": "constraint_bound_near_field",
        },
        "harmonic_trap_graviton_detector": {
            "source_family": 1,
            "independent_port_operations": 0,
            "receiver": 2,
            "row_lineage": 0,
            "surgical_isolation": 0,
            "no_refit_target": 1,
            "physical_port_selection": 1,
            "explicit_rivals": 2,
            "gravity_transfer": True,
            "sector": "radiative_receiver_proposal",
        },
        "acoustic_resonator_ligo_correlated": {
            "source_family": 2,
            "independent_port_operations": 0,
            "receiver": 2,
            "row_lineage": 1,
            "surgical_isolation": 0,
            "no_refit_target": 2,
            "physical_port_selection": 1,
            "explicit_rivals": 2,
            "gravity_transfer": True,
            "sector": "radiative_receiver_proposal",
        },
        "wide_source_phase": {
            "source_family": 2,
            "independent_port_operations": 0,
            "receiver": 1,
            "row_lineage": 0,
            "surgical_isolation": 0,
            "no_refit_target": 2,
            "physical_port_selection": 1,
            "explicit_rivals": 2,
            "gravity_transfer": True,
            "sector": "source_probe_phase",
        },
        "massive_material_mediator": {
            "source_family": 1,
            "independent_port_operations": 2,
            "receiver": 2,
            "row_lineage": 1,
            "surgical_isolation": 1,
            "no_refit_target": 2,
            "physical_port_selection": 2,
            "explicit_rivals": 2,
            "gravity_transfer": False,
            "sector": "controlled_material_mediator",
        },
        "cavity_or_phonon_analogue": {
            "source_family": 2,
            "independent_port_operations": 2,
            "receiver": 2,
            "row_lineage": 2,
            "surgical_isolation": 2,
            "no_refit_target": 2,
            "physical_port_selection": 2,
            "explicit_rivals": 2,
            "gravity_transfer": False,
            "sector": "native_nongravitational_positive_control",
        },
    }


def packet_complete(row: dict[str, object]) -> bool:
    fields = (
        "source_family",
        "independent_port_operations",
        "receiver",
        "row_lineage",
        "surgical_isolation",
        "no_refit_target",
        "physical_port_selection",
        "explicit_rivals",
    )
    return all(row[field] == 2 for field in fields)


def build_result() -> dict[str, object]:
    full_cube = [(source, mediator) for source in (0, 1) for mediator in (0, 1)]
    lawful_near_field = [(source, constrained_mediator(source)) for source in (0, 1)]
    unlawful_cuts = [point for point in full_cube if point not in lawful_near_field]

    mediated_lawful = [mediated_near_field(source, mediator) for source, mediator in lawful_near_field]
    direct_lawful = [direct_near_field(source, mediator) for source, mediator in lawful_near_field]
    mediated_full = [mediated_near_field(source, mediator) for source, mediator in full_cube]
    direct_full = [direct_near_field(source, mediator) for source, mediator in full_cube]

    radiative_surface = [
        {
            "source": source,
            "incoming_mode": mode,
            "field_response": radiative_field(source, mode),
            "near_field_only_response": near_field_only_rival(source, mode),
            "direct_with_same_input_response": direct_with_radiative_input(source, mode),
        }
        for source in (0, 1)
        for mode in (0, 1)
    ]

    audit = platform_audit()
    complete_native = [name for name, row in audit.items() if packet_complete(row)]
    complete_gravity = [
        name
        for name, row in audit.items()
        if packet_complete(row) and row["gravity_transfer"]
    ]

    assertions = {
        "full_intervention_cube_has_four_points": len(full_cube) == 4,
        "constraint_surface_has_two_points": len(lawful_near_field) == 2,
        "off_surface_cuts_violate_mediator_equals_source": (
            len(unlawful_cuts) == 2
            and all(mediator != source for source, mediator in unlawful_cuts)
        ),
        "mediated_and_direct_models_equal_on_every_lawful_near_field_action": (
            mediated_lawful == direct_lawful == [0, 1]
        ),
        "unlawful_full_cube_would_separate_the_presentations": mediated_full != direct_full,
        "radiative_mode_is_independently_variable": (
            {(row["source"], row["incoming_mode"]) for row in radiative_surface}
            == set(full_cube)
        ),
        "radiative_variation_separates_near_field_only_rival": any(
            row["field_response"] != row["near_field_only_response"]
            for row in radiative_surface
        ),
        "response_equivalent_direct_twin_survives_radiative_test": all(
            row["field_response"] == row["direct_with_same_input_response"]
            for row in radiative_surface
        ),
        "no_reviewed_gravitational_platform_has_complete_packet": not complete_gravity,
        "analogue_platform_is_complete_native_positive_control": (
            complete_native == ["cavity_or_phonon_analogue"]
        ),
        "analogue_positive_control_does_not_transfer_gravity_attribution": (
            not audit["cavity_or_phonon_analogue"]["gravity_transfer"]
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-198",
        "disposition": (
            "CONSTRAINT_COMPATIBLE_INTERVENTIONS_REPLACE_ARBITRARY_PORT_CUT_"
            "RADIATIVE_SECTOR_REOPENS_RELATIVE_RESPONSE_NOT_ONTOLOGY"
        ),
        "near_field": {
            "constraint": "M=S",
            "full_mathematical_cube": full_cube,
            "lawful_intervention_surface": lawful_near_field,
            "unlawful_port_cuts": unlawful_cuts,
            "mediated_response_on_lawful_surface": mediated_lawful,
            "direct_response_on_lawful_surface": direct_lawful,
            "mediated_response_on_full_cube": mediated_full,
            "direct_response_on_full_cube": direct_full,
        },
        "radiative_sector": {
            "lawful_surface": radiative_surface,
            "positive_discriminator": "incoming R=1 separates D=S XOR R from D=S",
            "ontology_boundary": (
                "D=S XOR R has both a field-mediated and a response-equivalent "
                "direct presentation, so the response test does not select ontology"
            ),
        },
        "platform_audit_scale": {"absent": 0, "partial": 1, "full": 2},
        "platform_audit": audit,
        "complete_native_packets": complete_native,
        "complete_gravitational_packets": complete_gravity,
        "assertions": assertions,
        "theorem_statement": (
            "An intervention identifies a target only relative to the lawful "
            "action algebra of a frozen physical completion class. Enlarging "
            "that algebra with operations that violate a field constraint "
            "changes the physical problem rather than refining its record. "
            "When M is fixed by S, mediated and direct presentations may agree "
            "on every lawful near-field action even though arbitrary off-law "
            "cuts would separate them. An independently preparable radiative "
            "mode can reopen a lawful response-class discriminator, but equal "
            "radiative response still does not select field ontology."
        ),
        "scope_guard": (
            "This exact finite result does not prove that gravity is direct, "
            "that gravitational radiation is quantized, that a reviewed "
            "proposal is impossible, or that a radiative response identifies "
            "a field ontology. The platform audit is source-bounded and earns "
            "no observation, hardware action, Grade-5 remainder, or active successor."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the canonical JSON regression artifact",
    )
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
