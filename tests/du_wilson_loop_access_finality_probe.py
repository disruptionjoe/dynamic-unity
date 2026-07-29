#!/usr/bin/env python3
"""Exact finite controls for HC-DU-119.

The probe checks a binary finite shadow of four distinctions:

1. a pre-distributed cat ancilla and strictly local couplings form an
   all-shares-required parity record without leaking finer local data;
2. that protocol implements the parity Lüders channel and preserves
   within-sector coherence;
3. local data readout also reveals parity but implements a strictly finer,
   destructive channel; and
4. singleton conjugacy classes in Z2 have unambiguous multiplication, while
   the transposition class in S3 has products in more than one conjugacy
   class.

The probe is not a lattice gauge theory, a proof of Wilson-loop
measurability, a relativistic causality theorem, or evidence for new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_wilson_loop_access_finality_result.json"

BitString = tuple[int, ...]
Permutation = tuple[int, ...]


def parity(bits: Iterable[int]) -> int:
    return sum(bits) % 2


def cat_share_distribution(data: BitString) -> dict[BitString, Fraction]:
    """X-basis outcomes after local controlled phases on a cat ancilla.

    For n data bits, each of the 2^(n-1) share strings with parity equal to
    the data parity occurs with equal probability. This is the exact Kraus
    distribution of the ideal cat-ancilla parity measurement.
    """

    n = len(data)
    weight = Fraction(1, 2 ** (n - 1))
    return {
        shares: weight
        for shares in product((0, 1), repeat=n)
        if parity(shares) == parity(data)
    }


def marginal(
    distribution: dict[BitString, Fraction],
    coordinates: tuple[int, ...],
) -> dict[BitString, Fraction]:
    result: defaultdict[BitString, Fraction] = defaultdict(Fraction)
    for outcome, probability in distribution.items():
        projected = tuple(outcome[index] for index in coordinates)
        result[projected] += probability
    return dict(result)


def qnd_matrix_unit_factor(left: BitString, right: BitString) -> int:
    """Coefficient on |left><right| under the parity Lüders channel."""

    return int(parity(left) == parity(right))


def destructive_matrix_unit_factor(
    left: BitString,
    right: BitString,
) -> int:
    """Coefficient under complete computational-basis dephasing."""

    return int(left == right)


def cat_channel_matrix_unit_factor(
    left: BitString,
    right: BitString,
) -> Fraction:
    """Derive the cat-ancilla channel by summing exact Kraus weights."""

    left_distribution = cat_share_distribution(left)
    right_distribution = cat_share_distribution(right)
    common_outcomes = set(left_distribution) & set(right_distribution)
    if not common_outcomes:
        return Fraction(0)

    # Each nonzero Kraus amplitude has magnitude 2^(-(n-1)/2). The product
    # of the left/right amplitudes is therefore 2^(-(n-1)).
    amplitude_product = Fraction(1, 2 ** (len(left) - 1))
    return len(common_outcomes) * amplitude_product


def sequential_ancilla_outcome(data: BitString) -> int:
    """One |+> ancilla acquires one phase per local encounter."""

    phase = 1
    for bit in data:
        if bit:
            phase *= -1
    return 0 if phase == 1 else 1


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def conjugate(
    group_element: Permutation,
    element: Permutation,
) -> Permutation:
    return compose(
        compose(group_element, element),
        inverse(group_element),
    )


def conjugacy_class(
    group: tuple[Permutation, ...],
    element: Permutation,
) -> frozenset[Permutation]:
    return frozenset(conjugate(g, element) for g in group)


def cycle_type(permutation: Permutation) -> tuple[int, ...]:
    seen: set[int] = set()
    cycles: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = permutation[current]
            length += 1
        cycles.append(length)
    return tuple(sorted(cycles, reverse=True))


def main() -> None:
    n = 3
    data_states = tuple(product((0, 1), repeat=n))

    # Every basis state yields four equiprobable share strings whose joined
    # parity equals the loop target.
    for data in data_states:
        distribution = cat_share_distribution(data)
        assert sum(distribution.values(), Fraction(0)) == 1
        assert len(distribution) == 2 ** (n - 1)
        assert all(parity(shares) == parity(data) for shares in distribution)

    # No proper subset of shares contains any target information. In fact,
    # every proper-subset marginal is uniform and is identical for every data
    # state, including states in opposite parity sectors.
    proper_subsets = tuple(
        coordinates
        for size in range(1, n)
        for coordinates in combinations(range(n), size)
    )
    for coordinates in proper_subsets:
        expected = {
            outcome: Fraction(1, 2 ** len(coordinates))
            for outcome in product((0, 1), repeat=len(coordinates))
        }
        for data in data_states:
            assert marginal(
                cat_share_distribution(data),
                coordinates,
            ) == expected

    # The full share distribution depends only on parity, not on finer field
    # detail. It is therefore a parity record rather than a hidden local-data
    # transcript.
    for left in data_states:
        for right in data_states:
            distributions_equal = (
                cat_share_distribution(left)
                == cat_share_distribution(right)
            )
            assert distributions_equal == (parity(left) == parity(right))

    # The cat protocol implements exactly the parity Lüders channel on all
    # computational matrix units.
    for left in data_states:
        for right in data_states:
            assert cat_channel_matrix_unit_factor(
                left,
                right,
            ) == qnd_matrix_unit_factor(left, right)

    within_sector_pair = ((0, 0, 0), (0, 1, 1))
    cross_sector_pair = ((0, 0, 0), (0, 0, 1))
    assert qnd_matrix_unit_factor(*within_sector_pair) == 1
    assert destructive_matrix_unit_factor(*within_sector_pair) == 0
    assert qnd_matrix_unit_factor(*cross_sector_pair) == 0

    # A single timelike-routed coherent ancilla implements the same parity
    # outcome, but it changes the route/time/resource contract.
    assert all(
        sequential_ancilla_outcome(data) == parity(data)
        for data in data_states
    )

    # Local computational-basis readout contains the parity but is strictly
    # finer: several records map to each parity and within-sector coherence
    # is destroyed.
    parity_fibres: dict[int, list[BitString]] = {
        value: [
            data
            for data in data_states
            if parity(data) == value
        ]
        for value in (0, 1)
    }
    assert all(len(fibre) == 4 for fibre in parity_fibres.values())
    assert destructive_matrix_unit_factor(*within_sector_pair) == 0

    # Small-group algebraic hinge. Z2 is Abelian, so every conjugacy class is
    # a singleton and class multiplication is single-valued. In S3, products
    # of two transpositions land in both the identity and 3-cycle classes.
    z2 = (0, 1)
    z2_classes = ({element} for element in z2)
    assert all(len(conjugacy) == 1 for conjugacy in z2_classes)
    assert {
        (left + right) % 2
        for left in (1,)
        for right in (1,)
    } == {0}

    s3 = tuple(permutations(range(3)))
    transpositions = frozenset(
        element
        for element in s3
        if cycle_type(element) == (2, 1)
    )
    assert len(transpositions) == 3
    assert conjugacy_class(s3, next(iter(transpositions))) == transpositions
    product_types = {
        cycle_type(compose(left, right))
        for left in transpositions
        for right in transpositions
    }
    assert product_types == {(1, 1, 1), (3,)}

    controls = {
        "cat_shares_jointly_reconstruct_parity": True,
        "every_proper_share_subset_is_target_blind": True,
        "share_distribution_depends_only_on_parity": True,
        "cat_protocol_equals_parity_luders_channel": True,
        "qnd_protocol_preserves_within_sector_coherence": True,
        "qnd_protocol_removes_cross_sector_coherence": True,
        "local_readout_reconstructs_parity_but_is_strictly_finer": True,
        "local_readout_destroys_within_sector_coherence": True,
        "sequential_coherent_ancilla_reconstructs_same_parity": True,
        "z2_conjugacy_products_are_single_class": True,
        "s3_transposition_products_span_multiple_classes": True,
    }
    assert all(controls.values())

    result = {
        "claim_id": "HC-DU-119",
        "status": "PASS",
        "controls": controls,
        "witnesses": {
            "data_bits": n,
            "target_bits": 1,
            "local_share_bits": n,
            "share_threshold": n,
            "conditional_share_entropy_bits": n - 1,
            "full_share_target_information_bits_equal_prior": 1,
            "proper_subset_target_information_bits_equal_prior": 0,
            "within_sector_coherence": {
                "matrix_unit": [
                    "".join(map(str, within_sector_pair[0])),
                    "".join(map(str, within_sector_pair[1])),
                ],
                "qnd_factor": qnd_matrix_unit_factor(*within_sector_pair),
                "destructive_factor": destructive_matrix_unit_factor(
                    *within_sector_pair
                ),
            },
            "cross_sector_coherence": {
                "matrix_unit": [
                    "".join(map(str, cross_sector_pair[0])),
                    "".join(map(str, cross_sector_pair[1])),
                ],
                "qnd_factor": qnd_matrix_unit_factor(*cross_sector_pair),
            },
            "s3_transposition_product_cycle_types": [
                list(value)
                for value in sorted(product_types)
            ],
        },
        "interpretation": {
            "regional_record": (
                "Each local share is target-blind; only the complete joined "
                "share set determines the extended parity."
            ),
            "formation_access_split": (
                "The local couplings and share measurements form a "
                "distributed record before any one observer aggregates it."
            ),
            "destructive_boundary": (
                "Full local readout derives the same parity while forming a "
                "strictly finer record and destroying extra coherence."
            ),
            "resource_boundary": (
                "Pre-distributed entanglement and a timelike sequential route "
                "implement the same ideal parity instrument under different "
                "resource and acquisition contracts."
            ),
            "group_boundary": (
                "The S3 enumeration checks the non-Abelian conjugacy-product "
                "ambiguity used by the primary-source causality argument."
            ),
        },
        "limits": [
            "finite binary circuit control, not a gauge-field simulation",
            "parity is only a finite shadow of an Abelian Wilson loop",
            "S3 class enumeration is not the relativistic causality proof",
            "the protocol is supplied rather than selected by a universal law",
            "no hardware, empirical excess, ontology priority, or new physics",
        ],
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("HC-DU-119 Wilson-loop access/finality controls: 11/11 passed")


if __name__ == "__main__":
    main()
