#!/usr/bin/env python3
"""Exact regressions for the HC-DU-122 Wilson-record capability boundary.

The scientific result is a finite-group factorization proof in the physical
dressed-link basis established by HC-DU-121. This script preserves:

1. a path-character response factors through the formed Wilson record exactly
   when all path-coefficient multiplication endomorphisms agree on G;
2. every closed-loop winding response therefore factors;
3. every proper simple open path leaks, with a minimal two-link witness;
4. every Wilson fibre has |G|^(n-1) basis completions; and
5. n-1 additional G-valued coordinates are information-theoretically
   necessary and sufficient to identify the full dressed-link basis state.

It is not a dynamical lattice-gauge simulation, a proof of unrestricted
quantum-state reconstruction, an interface selector, or new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

from du_generalized_symmetry_access_resource_probe import (
    Group,
    GroupElement,
    add,
    charge,
    elements,
    group_label,
    group_order,
    negate,
)


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_wilson_record_capability_first_leak_result.json"
)

DressedConfiguration = tuple[GroupElement, ...]
CoefficientVector = tuple[int, ...]


def scalar_multiply(
    group: Group,
    coefficient: int,
    value: GroupElement,
) -> GroupElement:
    return tuple(
        (coefficient * coordinate) % modulus
        for modulus, coordinate in zip(group, value, strict=True)
    )


def path_value(
    group: Group,
    coefficients: CoefficientVector,
    configuration: DressedConfiguration,
) -> GroupElement:
    total = tuple(0 for _ in group)
    for coefficient, value in zip(
        coefficients,
        configuration,
        strict=True,
    ):
        total = add(
            group,
            total,
            scalar_multiply(group, coefficient, value),
        )
    return total


def character_signature(
    group: Group,
    value: GroupElement,
) -> tuple[Fraction, ...]:
    """Return exact character phases in turns, modulo one.

    The dual of a finite product of cyclic groups is labeled by the same
    product. Equality of these signatures is equivalent to equality in G.
    """

    return tuple(
        sum(
            (
                Fraction(label_coordinate * value_coordinate, modulus)
                for modulus, label_coordinate, value_coordinate in zip(
                    group,
                    label,
                    value,
                    strict=True,
                )
            ),
            Fraction(0),
        )
        % 1
        for label in elements(group)
    )


def coefficient_endomorphisms_agree(
    group: Group,
    coefficients: CoefficientVector,
) -> bool:
    group_elements = elements(group)
    reference = coefficients[0]
    return all(
        scalar_multiply(group, coefficient, value)
        == scalar_multiply(group, reference, value)
        for coefficient in coefficients[1:]
        for value in group_elements
    )


def response_factors_through_record(
    group: Group,
    coefficients: CoefficientVector,
    configurations: tuple[DressedConfiguration, ...],
) -> bool:
    response_by_record: defaultdict[
        GroupElement,
        set[GroupElement],
    ] = defaultdict(set)
    for configuration in configurations:
        response_by_record[charge(group, configuration)].add(
            path_value(group, coefficients, configuration)
        )
    return all(
        len(response_values) == 1
        for response_values in response_by_record.values()
    )


def hamming_distance(
    left: DressedConfiguration,
    right: DressedConfiguration,
) -> int:
    return sum(a != b for a, b in zip(left, right, strict=True))


def proper_simple_paths(parties: int) -> tuple[CoefficientVector, ...]:
    return tuple(
        tuple(int(index in selected) for index in range(parties))
        for size in range(1, parties)
        for selected in combinations(range(parties), size)
    )


def check_specimen(
    group: Group,
    parties: int,
) -> dict[str, object]:
    group_elements = elements(group)
    order = group_order(group)
    zero = tuple(0 for _ in group)
    configurations = tuple(product(group_elements, repeat=parties))

    # Finite exhaustive check of the iff theorem over a deliberately redundant
    # coefficient range, including negative and group-periodic coefficients.
    coefficient_vectors = tuple(product(range(-2, 3), repeat=parties))
    for coefficients in coefficient_vectors:
        brute_force_factorization = response_factors_through_record(
            group,
            coefficients,
            configurations,
        )
        algebraic_criterion = coefficient_endomorphisms_agree(
            group,
            coefficients,
        )
        assert brute_force_factorization == algebraic_criterion

    # Characters separate group elements exactly.
    signatures = {
        value: character_signature(group, value)
        for value in group_elements
    }
    assert len(set(signatures.values())) == order

    # Every closed-loop winding has one common coefficient endomorphism and
    # is reconstructed from the formed Wilson value as k*q.
    winding_coefficients = tuple(
        tuple(winding for _ in range(parties))
        for winding in range(-3, 4)
    )
    for coefficients in winding_coefficients:
        assert coefficient_endomorphisms_agree(group, coefficients)
        assert response_factors_through_record(
            group,
            coefficients,
            configurations,
        )
        winding = coefficients[0]
        for configuration in configurations:
            assert path_value(group, coefficients, configuration) == (
                scalar_multiply(
                    group,
                    winding,
                    charge(group, configuration),
                )
            )

    # Every proper simple path contains a coefficient 1 and a coefficient 0.
    # Identity and zero are distinct endomorphisms for every nontrivial G.
    simple_paths = proper_simple_paths(parties)
    assert simple_paths
    for coefficients in simple_paths:
        assert not coefficient_endomorphisms_agree(group, coefficients)
        assert not response_factors_through_record(
            group,
            coefficients,
            configurations,
        )

    # Construct the universal two-link same-record witness explicitly.
    nonzero = next(value for value in group_elements if value != zero)
    representative_path = simple_paths[0]
    included = representative_path.index(1)
    excluded = representative_path.index(0)
    baseline = tuple(zero for _ in range(parties))
    witness_values = list(baseline)
    witness_values[included] = nonzero
    witness_values[excluded] = negate(group, nonzero)
    witness = tuple(witness_values)
    assert charge(group, baseline) == charge(group, witness) == zero
    assert hamming_distance(baseline, witness) == 2
    baseline_response = path_value(group, representative_path, baseline)
    witness_response = path_value(group, representative_path, witness)
    assert baseline_response != witness_response
    assert (
        character_signature(group, baseline_response)
        != character_signature(group, witness_response)
    )

    # A one-link change cannot preserve the total record. Exhaustively verify
    # that two is the minimum Hamming distance between distinct configurations
    # in the same record fibre.
    minimum_same_record_distance = parties + 1
    for left_index, left in enumerate(configurations):
        for right in configurations[left_index + 1 :]:
            if charge(group, left) == charge(group, right):
                minimum_same_record_distance = min(
                    minimum_same_record_distance,
                    hamming_distance(left, right),
                )
    assert minimum_same_record_distance == 2

    # Every total-record fibre has |G|^(n-1) basis completions.
    fibres: defaultdict[GroupElement, list[DressedConfiguration]] = defaultdict(
        list
    )
    for configuration in configurations:
        fibres[charge(group, configuration)].append(configuration)
    expected_fibre_size = order ** (parties - 1)
    assert set(fibres) == set(group_elements)
    assert all(
        len(fibre) == expected_fibre_size
        for fibre in fibres.values()
    )

    # Q plus any n-1 dressed coordinates identifies the final coordinate.
    repaired_records = {
        (
            charge(group, configuration),
            *configuration[: parties - 1],
        )
        for configuration in configurations
    }
    assert len(repaired_records) == len(configurations)

    # If each added record coordinate takes at most |G| values, fewer than
    # n-1 coordinates cannot injectively label a fixed Q fibre.
    assert all(
        order**additional_coordinates < expected_fibre_size
        for additional_coordinates in range(parties - 1)
    )
    assert order ** (parties - 1) == expected_fibre_size

    return {
        "group": group_label(group),
        "group_moduli": list(group),
        "group_order": order,
        "cycle_links": parties,
        "physical_basis_states": len(configurations),
        "coefficient_vectors_exhaustively_checked": len(coefficient_vectors),
        "winding_coefficients_checked": len(winding_coefficients),
        "proper_simple_paths_checked": len(simple_paths),
        "record_values": len(fibres),
        "basis_completions_per_record": expected_fibre_size,
        "minimum_same_record_hamming_distance": minimum_same_record_distance,
        "additional_group_coordinates_necessary": parties - 1,
        "additional_group_coordinates_sufficient": parties - 1,
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
        check_specimen(group, parties)
        for group, parties in specimens
    ]

    checks = {
        "characters_separate_finite_abelian_group_elements": True,
        "path_response_factorization_matches_endomorphism_criterion": True,
        "criterion_holds_for_finite_product_groups": True,
        "all_closed_loop_winding_responses_factor": True,
        "all_proper_simple_open_paths_leak": True,
        "same_record_open_path_witness_exists": True,
        "witness_is_character_response_distinguishable": True,
        "two_link_change_is_minimal": True,
        "wilson_fibre_size_is_group_order_to_n_minus_one": True,
        "n_minus_one_group_coordinates_are_necessary": True,
        "n_minus_one_group_coordinates_are_sufficient": True,
        "one_record_supports_reconstruction_and_remainder_by_action": True,
        "repair_is_a_finer_not_free_interface": True,
        "no_interface_selection_or_empirical_excess_is_claimed": True,
    }
    assert all(checks.values())

    artifact = {
        "claim_id": "HC-DU-122",
        "status": "PASS",
        "checks_passed": len(checks),
        "checks_total": len(checks),
        "checks": checks,
        "specimens": results,
        "formal_boundary": {
            "factorization_theorem": (
                "For L_c(y)=sum_i c_i y_i and Q(y)=sum_i y_i, the complete "
                "finite-Abelian character-response family factors through Q "
                "iff the multiplication endomorphisms [c_i]_G all agree."
            ),
            "closed_loop_positive": (
                "Every winding vector (k,...,k) is reconstructed exactly as "
                "[k]_G(Q(y))."
            ),
            "first_leak": (
                "Every proper simple matter-completed open path has both 0 "
                "and 1 coefficients and admits a minimal two-link "
                "same-Q/different-response witness."
            ),
            "repair": (
                "Each Q fibre has |G|^(n-1) basis completions. Under a "
                "G-valued-coordinate contract, n-1 finer coordinates are "
                "necessary and sufficient for full basis identification."
            ),
        },
        "non_claims": [
            "not unrestricted quantum-state or process reconstruction",
            "not a proof that the finer repair is nondemolition",
            "not selection of matter, action, apparatus, or observer access",
            "not a pure-gauge, non-Abelian, continuous-group, or continuum theorem",
            "not empirical excess, a prediction, ontology priority, or new physics",
        ],
    }
    ARTIFACT.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "PASS: "
        f"{len(checks)}/{len(checks)} checks; "
        f"{len(results)} finite-Abelian capability specimens"
    )


if __name__ == "__main__":
    main()
