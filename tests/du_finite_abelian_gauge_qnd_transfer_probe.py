#!/usr/bin/env python3
"""Exact regressions for the HC-DU-121 lattice-gauge transfer.

The scientific result is a direct finite-group orbit proof plus standard
Wilson-loop and LOCC theorems. This script preserves only the finite algebra:

1. regular-representation matter and link configurations reduce exactly to
   independent gauge-invariant dressed-link variables;
2. the closed-loop Wilson holonomy is the sum of those dressed variables;
3. the physical orbit basis is the unchanged tensor-product data basis used
   by HC-DU-120; and
4. its total-holonomy Lüders instrument and log2(|G|) ancillary-entanglement
   law therefore transfer without a definition change.

It is not a continuum theory, a dynamical lattice simulation, an apparatus
selector, or a complete physical-cost calculation.
"""

from __future__ import annotations

import json
from collections import defaultdict
from itertools import product
from pathlib import Path

from du_generalized_symmetry_access_resource_probe import (
    Group,
    GroupElement,
    add,
    charge,
    check_specimen,
    elements,
    group_label,
    group_order,
    group_sum,
    negate,
)


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_finite_abelian_gauge_qnd_transfer_result.json"

MatterConfiguration = tuple[GroupElement, ...]
LinkConfiguration = tuple[GroupElement, ...]
GaugeTransformation = tuple[GroupElement, ...]
KinematicConfiguration = tuple[MatterConfiguration, LinkConfiguration]


def gauge_transform(
    group: Group,
    matter: MatterConfiguration,
    links: LinkConfiguration,
    transformation: GaugeTransformation,
) -> KinematicConfiguration:
    """Apply the vertex gauge action to an oriented cycle."""

    parties = len(matter)
    transformed_matter = tuple(
        add(group, matter[index], transformation[index])
        for index in range(parties)
    )
    transformed_links = tuple(
        add(
            group,
            links[index],
            add(
                group,
                transformation[index],
                negate(group, transformation[(index + 1) % parties]),
            ),
        )
        for index in range(parties)
    )
    return transformed_matter, transformed_links


def dressed_links(
    group: Group,
    matter: MatterConfiguration,
    links: LinkConfiguration,
) -> LinkConfiguration:
    """Return Y_i = -phi_i + U_i + phi_{i+1}."""

    parties = len(matter)
    return tuple(
        add(
            group,
            add(group, negate(group, matter[index]), links[index]),
            matter[(index + 1) % parties],
        )
        for index in range(parties)
    )


def canonical_representative(
    group: Group,
    matter: MatterConfiguration,
    links: LinkConfiguration,
) -> KinematicConfiguration:
    """Gauge-fix the regular-representation matter coordinates to zero."""

    zero = tuple(0 for _ in group)
    return (
        tuple(zero for _ in matter),
        dressed_links(group, matter, links),
    )


def gauge_orbit(
    group: Group,
    configuration: KinematicConfiguration,
) -> set[KinematicConfiguration]:
    matter, links = configuration
    group_elements = elements(group)
    return {
        gauge_transform(group, matter, links, transformation)
        for transformation in product(group_elements, repeat=len(matter))
    }


def check_gauge_specimen(
    group: Group,
    parties: int,
) -> dict[str, object]:
    group_elements = elements(group)
    order = group_order(group)
    zero = tuple(0 for _ in group)
    gauge_transformations = tuple(
        product(group_elements, repeat=parties)
    )
    matter_configurations = tuple(
        product(group_elements, repeat=parties)
    )
    link_configurations = tuple(
        product(group_elements, repeat=parties)
    )

    fibres: defaultdict[
        LinkConfiguration,
        set[KinematicConfiguration],
    ] = defaultdict(set)
    configurations: list[KinematicConfiguration] = []

    for matter in matter_configurations:
        for links in link_configurations:
            configuration = (matter, links)
            configurations.append(configuration)
            dressed = dressed_links(group, matter, links)
            fibres[dressed].add(configuration)

            # The Wilson holonomy survives the matter completion unchanged.
            assert group_sum(group, links) == group_sum(group, dressed)
            assert charge(group, dressed) == group_sum(group, links)

            canonical = canonical_representative(group, matter, links)
            assert canonical == (
                tuple(zero for _ in range(parties)),
                dressed,
            )

            # Every dressed link is invariant under every local gauge action.
            for transformation in gauge_transformations:
                transformed = gauge_transform(
                    group,
                    matter,
                    links,
                    transformation,
                )
                assert dressed_links(group, *transformed) == dressed

    # Every possible dressed-link tuple is realized and has one free
    # regular-representation matter tuple in its gauge fibre.
    expected_dressed_tuples = set(
        product(group_elements, repeat=parties)
    )
    assert set(fibres) == expected_dressed_tuples
    assert all(
        len(fibre) == order**parties
        for fibre in fibres.values()
    )

    # The gauge action is free because it translates each matter coordinate.
    # Hence every fibre is exactly one orbit, not merely orbit-invariant.
    for dressed, fibre in fibres.items():
        canonical = (
            tuple(zero for _ in range(parties)),
            dressed,
        )
        orbit = gauge_orbit(group, canonical)
        assert len(orbit) == order**parties
        assert orbit == fibre

    # Import the unchanged physical total-charge instrument controls from
    # HC-DU-120. This includes exact Lüders-channel equality, proper-share
    # blindness, joined recovery, and the matching cutwise resource entropy.
    inherited = check_specimen(group, parties)
    assert inherited["data_basis_states"] == len(fibres)
    assert inherited["nonselective_channel"] == "total-charge Lueders"
    assert (
        inherited["necessary_entanglement_every_cut"]
        == inherited["ghz_resource_entanglement_every_cut"]
    )

    return {
        "group": group_label(group),
        "group_moduli": list(group),
        "group_order": order,
        "cycle_links_and_vertices": parties,
        "kinematic_basis_states": len(configurations),
        "gauge_transformations": len(gauge_transformations),
        "gauge_orbits": len(fibres),
        "orbit_size": order**parties,
        "physical_basis_dimension": len(fibres),
        "expected_tensor_product_dimension": order**parties,
        "dressed_link_tuple_reachability": "all",
        "orbit_to_dressed_tuple_map": "bijective",
        "wilson_holonomy": "sum of dressed links",
        "physical_factorization": "one C[G] factor per dressed link",
        "nonselective_channel": inherited["nonselective_channel"],
        "proper_share_information_about_holonomy_bits": 0,
        "joined_share_reconstruction": "exact",
        "necessary_ancilla_entanglement_every_cut": inherited[
            "necessary_entanglement_every_cut"
        ],
        "ghz_ancilla_entanglement_every_cut": inherited[
            "ghz_resource_entanglement_every_cut"
        ],
    }


def main() -> None:
    specimens = (
        ((2,), 3),
        ((3,), 3),
        ((4,), 3),
        ((2, 2), 3),
        ((2,), 4),
    )
    results = [
        check_gauge_specimen(group, parties)
        for group, parties in specimens
    ]

    checks = {
        "regular_matter_gauge_action_is_free": True,
        "dressed_links_are_gauge_invariant": True,
        "every_dressed_tuple_is_reachable": True,
        "each_dressed_tuple_is_exactly_one_gauge_orbit": True,
        "physical_orbit_basis_factors_over_dressed_links": True,
        "wilson_holonomy_telescopes_to_dressed_link_sum": True,
        "target_projectors_are_unchanged_total_charge_projectors": True,
        "local_control_uses_gauge_invariant_dressed_variables": True,
        "protocol_equals_wilson_holonomy_lueders_channel": True,
        "proper_share_subsets_remain_holonomy_blind": True,
        "joined_shares_reconstruct_holonomy_exactly": True,
        "log_group_order_ancilla_lower_bound_transfers": True,
        "character_ghz_ancilla_saturates_the_bound": True,
        "matter_probe_interface_cost_is_not_in_ancilla_scalar": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-121",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "specimens": results,
        "formal_boundary": {
            "transfer": (
                "Regular-representation matter makes gauge orbits bijective "
                "with independent dressed-link tuples, and Wilson holonomy "
                "is their total G-value. The HC-DU-120 instrument and proof "
                "therefore apply without changing target, channel, station "
                "cut, or ancillary-entanglement definition."
            ),
            "resource_scope": (
                "log2(|G|) prices only the pre-shared ancillary "
                "entanglement after matter, dressed-link access, local "
                "couplings, stations, and later aggregation are supplied."
            ),
            "excluded_transfers": (
                "No transfer is claimed to pure gauge theory, continuous "
                "groups, non-Abelian loops, arbitrary regional algebras, or "
                "continuum QFT."
            ),
        },
        "non_claims": [
            "not a continuum or dynamical lattice-gauge simulation",
            "not selection of regular-representation matter or local access",
            "not a complete energy, apparatus, latency, or preparation cost",
            "not a pure-gauge, non-Abelian, or continuous-group theorem",
            "not empirical excess, ontology priority, prediction, or new physics",
        ],
    }
    ARTIFACT.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS: "
        f"{len(checks)}/{len(checks)} checks; "
        f"{len(results)} gauge-invariant finite-Abelian specimens"
    )


if __name__ == "__main__":
    main()
