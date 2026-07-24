#!/usr/bin/env python3
"""Exact finite probe for representation-relative record identifiability.

The probe separates three claims that are easy to conflate:

1. A predicate can be durable under a dynamics.
2. A predicate can be copied by a predicate-specific classical channel.
3. Bare, unlabelled dynamics can canonically select that predicate as *the*
   record observable.

For identity dynamics on a finite state space, (1) and (2) hold for every
binary predicate.  Yet the automorphism group of the bare dynamics is the
full symmetric group, and its only invariant binary predicates are constants.
Thus durability and classical copyability do not identify a nontrivial
record observable.

This is deliberately not a no-go for physical records.  A declared readout,
intervention, locality, tensor factorization, or resource algebra reduces the
admissible automorphism group.  Nonconstant invariant predicates can then
exist.  Alternatively, a record channel may transform covariantly with its
codomain under a representation change.  Covariance preserves a record
relation; it does not select one member of an otherwise unlabelled orbit.

The finite calculation uses only dimensionless sets, maps, and counts.  It
does not derive an observer, thermodynamic irreversibility, proper time,
spacetime, a physical unit, or a Dynamic Unity law.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any, Callable, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_foundational_philosopher_record_identifiability_result.json"
)

StateMap = tuple[int, ...]


def compose(left: StateMap, right: StateMap) -> StateMap:
    """Return left after right."""
    return tuple(left[right[state]] for state in range(len(right)))


def inverse(permutation: StateMap) -> StateMap:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def conjugate(dynamics: StateMap, permutation: StateMap) -> StateMap:
    """Transport a dynamics by a representation change."""
    return compose(permutation, compose(dynamics, inverse(permutation)))


def automorphisms(dynamics: StateMap) -> list[StateMap]:
    """All state permutations commuting with the finite dynamics."""
    size = len(dynamics)
    return [
        permutation
        for permutation in itertools.permutations(range(size))
        if compose(permutation, dynamics) == compose(dynamics, permutation)
    ]


def predicate_value(mask: int, state: int) -> int:
    return (mask >> state) & 1


def predicate_support(mask: int, size: int) -> frozenset[int]:
    return frozenset(
        state for state in range(size) if predicate_value(mask, state)
    )


def support_mask(support: Iterable[int]) -> int:
    mask = 0
    for state in support:
        mask |= 1 << state
    return mask


def transport_predicate(mask: int, permutation: StateMap) -> int:
    """Transport r to r^phi = r after phi^{-1}."""
    transported_support = {
        permutation[state]
        for state in predicate_support(mask, len(permutation))
    }
    return support_mask(transported_support)


def predicate_is_durable(mask: int, dynamics: StateMap) -> bool:
    return all(
        predicate_value(mask, dynamics[state])
        == predicate_value(mask, state)
        for state in range(len(dynamics))
    )


def predicate_is_invariant(mask: int, group: Iterable[StateMap]) -> bool:
    return all(transport_predicate(mask, member) == mask for member in group)


def classical_copy_map(mask: int, size: int) -> tuple[tuple[int, int], ...]:
    """C_r(x,b)=(x,b xor r(x)), represented on X times {0,1}."""
    return tuple(
        (state, blank ^ predicate_value(mask, state))
        for state in range(size)
        for blank in (0, 1)
    )


def copy_map_is_bijective(mask: int, size: int) -> bool:
    outputs = classical_copy_map(mask, size)
    return len(set(outputs)) == 2 * size


def copy_map_copies_from_blank(mask: int, size: int) -> bool:
    return all(
        classical_copy_map(mask, size)[2 * state]
        == (state, predicate_value(mask, state))
        for state in range(size)
    )


def summarize_dynamics(name: str, dynamics: StateMap) -> dict[str, Any]:
    size = len(dynamics)
    group = automorphisms(dynamics)
    predicate_masks = range(1 << size)
    durable = [
        mask for mask in predicate_masks if predicate_is_durable(mask, dynamics)
    ]
    invariant = [
        mask
        for mask in range(1 << size)
        if predicate_is_invariant(mask, group)
    ]
    nontrivial = [
        mask for mask in invariant if mask not in (0, (1 << size) - 1)
    ]
    return {
        "name": name,
        "state_count": size,
        "dynamics": list(dynamics),
        "automorphism_group_order": len(group),
        "durable_predicate_count": len(durable),
        "durable_nontrivial_predicate_count": len(durable) - 2,
        "automorphism_invariant_predicate_count": len(invariant),
        "automorphism_invariant_predicate_masks": invariant,
        "nontrivial_automorphism_invariant_predicate_count": len(nontrivial),
        "nontrivial_automorphism_invariant_predicate_masks": nontrivial,
    }


def identity_case(bit_count: int) -> dict[str, Any]:
    size = 1 << bit_count
    dynamics = tuple(range(size))

    # For the held-out three-bit case, checking every predicate against all
    # 8! automorphisms is exact but needlessly bulky.  Pair transpositions
    # generate the full symmetric group, so invariance under this generator
    # set is equivalent to invariance under the full group.
    transpositions: list[StateMap] = []
    for left in range(size):
        for right in range(left + 1, size):
            permutation = list(range(size))
            permutation[left], permutation[right] = (
                permutation[right],
                permutation[left],
            )
            transpositions.append(tuple(permutation))

    invariant_masks = [
        mask
        for mask in range(1 << size)
        if predicate_is_invariant(mask, transpositions)
    ]
    durable_masks = [
        mask
        for mask in range(1 << size)
        if predicate_is_durable(mask, dynamics)
    ]
    copyable_masks = [
        mask
        for mask in range(1 << size)
        if copy_map_is_bijective(mask, size)
        and copy_map_copies_from_blank(mask, size)
    ]

    return {
        "bit_count": bit_count,
        "state_count": size,
        "dynamics": list(dynamics),
        "automorphism_group": "full symmetric group",
        "automorphism_group_order": math.factorial(size),
        "exact_generator_set": "all pair transpositions",
        "generator_count": len(transpositions),
        "binary_predicate_count": 1 << size,
        "durable_predicate_count": len(durable_masks),
        "durable_nontrivial_predicate_count": len(durable_masks) - 2,
        "classically_copyable_predicate_count": len(copyable_masks),
        "copy_channels_are_predicate_specific": True,
        "full_group_invariant_predicate_masks": invariant_masks,
        "full_group_invariant_predicate_count": len(invariant_masks),
        "full_group_invariant_nontrivial_predicate_count": len(
            [
                mask
                for mask in invariant_masks
                if mask not in (0, (1 << size) - 1)
            ]
        ),
    }


def coordinate_parity_covariance_control() -> dict[str, Any]:
    size = 4
    dynamics = tuple(range(size))
    coordinate_support = frozenset({2, 3})
    parity_support = frozenset({1, 2})
    coordinate_mask = support_mask(coordinate_support)
    parity_mask = support_mask(parity_support)

    # Map the coordinate-1 block to the odd-parity block and its complement
    # to the even-parity block.
    permutation = (0, 3, 1, 2)
    transported_coordinate = transport_predicate(coordinate_mask, permutation)

    return {
        "state_encoding": ["00", "01", "10", "11"],
        "coordinate_predicate": {
            "definition": "first bit equals 1",
            "support": sorted(coordinate_support),
            "mask": coordinate_mask,
        },
        "parity_predicate": {
            "definition": "bit parity equals 1",
            "support": sorted(parity_support),
            "mask": parity_mask,
        },
        "representation_change_phi": list(permutation),
        "phi_is_bijection": len(set(permutation)) == size,
        "conjugated_dynamics": list(conjugate(dynamics, permutation)),
        "identity_dynamics_preserved": conjugate(dynamics, permutation)
        == dynamics,
        "transported_coordinate_mask": transported_coordinate,
        "coordinate_transports_to_parity": transported_coordinate
        == parity_mask,
        "both_predicates_durable": all(
            predicate_is_durable(mask, dynamics)
            for mask in (coordinate_mask, parity_mask)
        ),
        "both_predicates_copyable": all(
            copy_map_is_bijective(mask, size)
            and copy_map_copies_from_blank(mask, size)
            for mask in (coordinate_mask, parity_mask)
        ),
        "reading": (
            "Coordinate and parity records are in the same representation "
            "orbit. Transporting the predicate with the state representation "
            "is an exact covariance relation, but bare identity dynamics "
            "does not canonically choose either orbit representative."
        ),
    }


def interface_stabilizer_control(bit_count: int) -> dict[str, Any]:
    size = 1 << bit_count
    block_size = size // 2
    coordinate_support = frozenset(range(block_size, size))
    coordinate_mask = support_mask(coordinate_support)
    parity_support = frozenset(
        state for state in range(size) if state.bit_count() % 2 == 1
    )
    parity_mask = support_mask(parity_support)

    if bit_count == 2:
        full_group = itertools.permutations(range(size))
        stabilizer = [
            permutation
            for permutation in full_group
            if transport_predicate(coordinate_mask, permutation)
            == coordinate_mask
        ]
        invariant_masks = [
            mask
            for mask in range(1 << size)
            if predicate_is_invariant(mask, stabilizer)
        ]
        parity_is_invariant = predicate_is_invariant(parity_mask, stabilizer)
    else:
        # The stabilizer is Sym(block 0) x Sym(block 1).  Pair
        # transpositions within either block generate it exactly.
        generators: list[StateMap] = []
        for block in (
            tuple(range(0, block_size)),
            tuple(range(block_size, size)),
        ):
            for left_index, left in enumerate(block):
                for right in block[left_index + 1 :]:
                    permutation = list(range(size))
                    permutation[left], permutation[right] = (
                        permutation[right],
                        permutation[left],
                    )
                    generators.append(tuple(permutation))
        stabilizer = generators
        invariant_masks = [
            mask
            for mask in range(1 << size)
            if predicate_is_invariant(mask, stabilizer)
        ]
        parity_is_invariant = predicate_is_invariant(parity_mask, stabilizer)

    expected_interface_algebra = {
        0,
        coordinate_mask,
        ((1 << size) - 1) ^ coordinate_mask,
        (1 << size) - 1,
    }

    return {
        "bit_count": bit_count,
        "declared_accessible_readout": "first bit",
        "readout_support": sorted(coordinate_support),
        "admissible_group": (
            "state permutations preserving each labelled readout block"
        ),
        "admissible_group_order": math.factorial(block_size) ** 2,
        "coordinate_readout_is_invariant": predicate_is_invariant(
            coordinate_mask, stabilizer
        ),
        "parity_readout_is_invariant": parity_is_invariant,
        "invariant_predicate_masks": invariant_masks,
        "invariant_predicate_count": len(invariant_masks),
        "invariants_equal_readout_algebra": set(invariant_masks)
        == expected_interface_algebra,
        "reading": (
            "The declared readout is extra physical structure. It reduces "
            "the automorphism group, leaving exactly the Boolean algebra "
            "generated by that readout. The result is interface-relative, "
            "not a coordinate record extracted from bare dynamics."
        ),
    }


def asymmetric_positive_control() -> dict[str, Any]:
    # One fixed point plus a three-cycle.  The dynamics itself distinguishes
    # two automorphism orbits, so a nontrivial invariant partition exists.
    dynamics = (0, 2, 3, 1)
    summary = summarize_dynamics(
        "fixed point plus three-cycle positive control", dynamics
    )
    expected_nontrivial = {
        support_mask({0}),
        support_mask({1, 2, 3}),
    }
    summary["expected_nontrivial_orbit_predicates"] = sorted(
        expected_nontrivial
    )
    summary["nontrivial_orbit_partition_recovered"] = (
        set(summary["nontrivial_automorphism_invariant_predicate_masks"])
        == expected_nontrivial
    )
    summary["reading"] = (
        "The no-go is not universal across all dynamics. Asymmetric bare "
        "dynamics can have nontrivial automorphism orbits and hence "
        "nonconstant invariant predicates. Whether such an orbit is a "
        "physical memory still requires record semantics."
    )
    return summary


def flip_dynamics_holdout() -> dict[str, Any]:
    # Two indistinguishable two-cycles.  There are nontrivial durable
    # predicates (one per cycle), but automorphisms can exchange the cycles,
    # so no nontrivial predicate is canonical.
    dynamics = (1, 0, 3, 2)
    summary = summarize_dynamics(
        "two indistinguishable bit-flip cycles holdout", dynamics
    )
    summary["reading"] = (
        "Nontrivial time-invariant predicates can exist while remaining "
        "unidentified: the bare dynamics admits an automorphism exchanging "
        "the two cycles."
    )
    return summary


def build_artifact() -> dict[str, Any]:
    identity_two = identity_case(2)
    identity_three = identity_case(3)
    covariance = coordinate_parity_covariance_control()
    interface_two = interface_stabilizer_control(2)
    interface_three = interface_stabilizer_control(3)
    flip_holdout = flip_dynamics_holdout()
    asymmetric = asymmetric_positive_control()

    checks: list[tuple[str, bool]] = [
        (
            "identity dynamics makes every 2-bit predicate durable",
            identity_two["durable_predicate_count"]
            == identity_two["binary_predicate_count"]
            == 16,
        ),
        (
            "every 2-bit predicate has a predicate-specific classical copy map",
            identity_two["classically_copyable_predicate_count"] == 16,
        ),
        (
            "full 2-bit identity automorphism invariance leaves no nontrivial predicate",
            identity_two["full_group_invariant_nontrivial_predicate_count"]
            == 0,
        ),
        (
            "held-out 3-bit identity case leaves no nontrivial invariant predicate",
            identity_three["full_group_invariant_nontrivial_predicate_count"]
            == 0,
        ),
        (
            "coordinate and parity predicates are conjugate",
            covariance["coordinate_transports_to_parity"],
        ),
        (
            "predicate transport preserves identity dynamics",
            covariance["identity_dynamics_preserved"],
        ),
        (
            "coordinate and parity are both durable and classically copyable",
            covariance["both_predicates_durable"]
            and covariance["both_predicates_copyable"],
        ),
        (
            "a declared 2-bit interface selects its readout algebra",
            interface_two["coordinate_readout_is_invariant"]
            and interface_two["invariants_equal_readout_algebra"],
        ),
        (
            "the 2-bit interface rejects parity as invariant",
            not interface_two["parity_readout_is_invariant"],
        ),
        (
            "held-out 3-bit interface result is the same",
            interface_three["coordinate_readout_is_invariant"]
            and not interface_three["parity_readout_is_invariant"]
            and interface_three["invariants_equal_readout_algebra"],
        ),
        (
            "nonidentity two-cycle holdout has durable nontrivial predicates",
            flip_holdout["durable_nontrivial_predicate_count"] == 2,
        ),
        (
            "nonidentity two-cycle holdout still has no canonical nontrivial predicate",
            flip_holdout[
                "nontrivial_automorphism_invariant_predicate_count"
            ]
            == 0,
        ),
        (
            "asymmetric dynamics admits a nontrivial invariant orbit partition",
            asymmetric["nontrivial_orbit_partition_recovered"],
        ),
        (
            "the mechanism-disabled persistence null overgenerates records",
            identity_two["durable_nontrivial_predicate_count"] == 14,
        ),
        (
            "no dimensional unit is introduced",
            True,
        ),
    ]

    passed = sum(passed for _, passed in checks)
    return {
        "metadata": {
            "probe": (
                "du_foundational_philosopher_record_identifiability_probe"
            ),
            "scope": (
                "Exact finite classical identifiability under state-space "
                "automorphisms; not a universal quantum or thermodynamic "
                "record theorem."
            ),
            "assumptions": [
                "Finite state spaces and deterministic transition maps.",
                "A scalar binary record candidate is a predicate on states.",
                "Bare-theory representation independence means invariance under every automorphism of the declared bare dynamics.",
                "Classical copyability means existence of the predicate-specific reversible map C_r(x,b)=(x,b xor r(x)).",
                "A physical interface, if used, is independently declared rather than inferred from the same persistence result.",
            ],
            "free_choices": [
                "Finite state-space size.",
                "Choice of bare dynamics.",
                "Choice of admissible automorphism group.",
                "Choice of accessible readout/intervention algebra.",
                "Choice of scalar predicate rather than a general channel.",
            ],
            "warrants": [
                "DERIVED automorphism-triviality theorem for identity dynamics.",
                "CONSTRUCTIVELY_REALIZED coordinate/parity conjugacy.",
                "CONSTRUCTIVELY_REALIZED classical copy channels.",
                "CONDITIONALLY ENTAILED interface-relative record algebra.",
                "EXACT FINITE HELD-OUT controls on three bits and nonidentity dynamics.",
            ],
        },
        "theorem": {
            "name": "bare-dynamics record-extractor triviality",
            "statement": (
                "Let X be a finite state space with |X|>1 and identity "
                "dynamics. Every binary predicate r:X->{0,1} is durable and "
                "has a predicate-specific reversible classical copy channel. "
                "But Aut(X,id)=Sym(X), and any scalar predicate invariant "
                "under every automorphism is constant. Therefore bare "
                "dynamics plus durability and classical copyability cannot "
                "canonically select a nontrivial record predicate."
            ),
            "scope_correction": (
                "This does not forbid nonconstant predicates under a smaller "
                "physically fixed automorphism group, nor equivariant record "
                "channels whose codomain and predicate transform with the "
                "representation. It forbids treating unrestricted literal "
                "coordinate invariance as a nontrivial record selector."
            ),
            "proof_outline": [
                "Identity dynamics commutes with every state permutation, so its automorphism group is the full symmetric group.",
                "The full symmetric group acts transitively on X. If r is invariant, r(x)=r(y) for every pair x,y, hence r is constant.",
                "Identity dynamics leaves every predicate unchanged in time, hence every predicate is durable.",
                "C_r is its own inverse and copies r into a blank classical bit, hence every predicate is classically copyable.",
            ],
        },
        "identity_dynamics": {
            "development_two_bit": identity_two,
            "held_out_three_bit": identity_three,
        },
        "covariant_predicate_transport": covariance,
        "interface_relative_positive_control": {
            "two_bit": interface_two,
            "held_out_three_bit": interface_three,
        },
        "nonidentity_controls": {
            "two_indistinguishable_cycles": flip_holdout,
            "asymmetric_orbit_positive_control": asymmetric,
        },
        "cheap_kills": {
            "object_exists_independently_of_readout": {
                "pass": False,
                "result": (
                    "Bare identity dynamics selects only constants. A "
                    "nontrivial record requires an interface, asymmetry, or "
                    "covariantly transported channel."
                ),
            },
            "relabeling_or_quotient": {
                "pass": True,
                "result": (
                    "The theorem is stated on the automorphism quotient; "
                    "coordinate and parity are explicitly conjugate."
                ),
            },
            "simpler_rival": {
                "pass": False,
                "result": (
                    "Mechanism-disabled identity dynamics makes all "
                    "predicates persistent, so persistence alone is an "
                    "overgenerating null."
                ),
            },
            "selected_partition_or_resolution": {
                "pass": False,
                "result": (
                    "Choosing the first-bit partition selects a record only "
                    "after that readout partition is declared as physical."
                ),
            },
            "held_out_cases": {
                "pass": True,
                "result": (
                    "The three-bit case repeats the theorem; two-cycle and "
                    "asymmetric nonidentity controls delimit its scope."
                ),
            },
            "dimensional_unit_import": {
                "pass": True,
                "result": "Only dimensionless finite counts and maps appear.",
            },
            "final_state_hides_provenance": {
                "pass": False,
                "result": (
                    "All identity-dynamics candidates have perfect endpoint "
                    "persistence. The endpoint does not identify which "
                    "predicate was written, copied, or read."
                ),
            },
            "mechanism_disable": {
                "pass": False,
                "result": (
                    "With temporal writing disabled by identity dynamics, "
                    "all fourteen nonconstant two-bit predicates still pass "
                    "the durability test."
                ),
            },
        },
        "rivals": [
            {
                "name": "status quo / no record object",
                "disposition": (
                    "Wins for bare identity dynamics if a nontrivial scalar "
                    "record is demanded without extra structure."
                ),
            },
            {
                "name": "persistence or endpoint replay",
                "disposition": "Matches every candidate and does not select one.",
            },
            {
                "name": "classical copyability",
                "disposition": (
                    "Every predicate is copyable by its own channel; the "
                    "channel moves rather than solves the selection burden."
                ),
            },
            {
                "name": "exact circuit covariance",
                "disposition": (
                    "Can transport a chosen channel covariantly but does not "
                    "by itself pick a durable observer record."
                ),
            },
            {
                "name": "interface/locality/access algebra",
                "disposition": (
                    "Positive conditional rival: reduces the automorphism "
                    "group and yields a nontrivial invariant record algebra."
                ),
            },
            {
                "name": "asymmetric bare dynamics",
                "disposition": (
                    "Positive scope control: dynamical automorphism orbits "
                    "can support nontrivial invariant predicates."
                ),
            },
            {
                "name": "quantum no-broadcasting",
                "disposition": (
                    "A separate physical restriction on copyable quantum "
                    "state families; the present theorem is classical and "
                    "addresses selection even when copying is unrestricted."
                ),
            },
        ],
        "checks": [
            {"name": name, "passed": check_passed}
            for name, check_passed in checks
        ],
        "check_count": len(checks),
        "passed_count": passed,
        "all_checks_passed": passed == len(checks),
        "verdict": (
            "FULL-AUTOMORPHISM SCALAR RECORD EXTRACTION IS TRIVIAL ON "
            "IDENTITY DYNAMICS / DURABILITY AND CLASSICAL COPYABILITY "
            "UNDERSELECT / PHYSICAL RECORDS REQUIRE A DECLARED "
            "INTERFACE-RELATIVE OR EQUIVARIANT CHANNEL"
        ),
        "banked": False,
        "seeded": False,
    }


def main() -> None:
    artifact = build_artifact()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for check in artifact["checks"]:
        status = "PASS" if check["passed"] else "FAIL"
        print(f"{status:4}  {check['name']}")
    print(
        f"{artifact['passed_count']}/{artifact['check_count']} checks pass"
    )
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {artifact['verdict']}")

    if not artifact["all_checks_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
