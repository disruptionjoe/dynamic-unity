#!/usr/bin/env python3
"""Exact finite controls for HC-DU-118.

The probe preserves four typed facts:

1. several reversible system-probe couplings in one finite arena induce
   different record channels;
2. every proper-local marginal of a full-support parity family can agree
   while one extended parity target differs;
3. the corresponding KL loss is exact but does not select the local or
   extended algebra; and
4. group averaging is canonical only relative to a supplied group action.

This is a finite classical selection-boundary regression. It does not model
QFT, the Fewster-Verch scheme, a generalized symmetry, a type-III algebra, a
physical observer, record formation, or new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Callable, Hashable, Mapping


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_local_qft_record_algebra_selection_result.json"
)

Outcome = Hashable
Distribution = Mapping[Outcome, Fraction]
BitPair = tuple[int, int]
BitTriple = tuple[int, int, int]


def normalized(distribution: Distribution) -> bool:
    return (
        all(probability >= 0 for probability in distribution.values())
        and sum(distribution.values(), Fraction(0)) == 1
    )


def kl_log_signature(
    numerator: Distribution,
    denominator: Distribution,
) -> dict[Fraction, Fraction]:
    """Represent KL exactly as sum_r coefficient[r] * log(r)."""
    if not normalized(numerator) or not normalized(denominator):
        raise ValueError("distributions must be normalized")
    coefficients: defaultdict[Fraction, Fraction] = defaultdict(Fraction)
    for outcome, probability in numerator.items():
        if probability == 0:
            continue
        reference = denominator.get(outcome, Fraction(0))
        if reference == 0:
            raise ValueError("infinite KL divergence is outside this control")
        ratio = probability / reference
        if ratio != 1:
            coefficients[ratio] += probability
    return {
        ratio: coefficient
        for ratio, coefficient in coefficients.items()
        if coefficient != 0
    }


def signature_text(
    signature: Mapping[Fraction, Fraction],
) -> dict[str, str]:
    def fraction_text(value: Fraction) -> str:
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"

    return {
        fraction_text(ratio): fraction_text(coefficient)
        for ratio, coefficient in sorted(signature.items())
    }


def reversible_record_channel(
    coupling: Callable[[BitPair], BitPair],
) -> dict[int, int]:
    """Read the probe after a reversible coupling with probe initialized at 0."""
    domain = tuple(product((0, 1), repeat=2))
    image = tuple(coupling(state) for state in domain)
    if len(set(image)) != len(domain):
        raise ValueError("coupling must be reversible")
    return {
        system: coupling((system, 0))[1]
        for system in (0, 1)
    }


def parity(outcome: BitTriple) -> int:
    return sum(outcome) % 2


def parity_character(outcome: BitTriple) -> int:
    return 1 if parity(outcome) == 0 else -1


def parity_distribution(sign: int) -> dict[BitTriple, Fraction]:
    if sign not in (-1, 1):
        raise ValueError("sign must be plus or minus one")
    result = {
        outcome: (
            Fraction(1, 8)
            * (
                1
                + sign
                * Fraction(1, 2)
                * parity_character(outcome)
            )
        )
        for outcome in product((0, 1), repeat=3)
    }
    assert normalized(result)
    return result


def marginal(
    distribution: Mapping[BitTriple, Fraction],
    coordinates: tuple[int, ...],
) -> dict[tuple[int, ...], Fraction]:
    result: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for outcome, probability in distribution.items():
        result[tuple(outcome[index] for index in coordinates)] += probability
    return dict(result)


def expectation(
    distribution: Mapping[BitTriple, Fraction],
    observable: Callable[[BitTriple], int],
) -> Fraction:
    return sum(
        (
            probability * observable(outcome)
            for outcome, probability in distribution.items()
        ),
        Fraction(0),
    )


def factors_through_subset(coordinates: tuple[int, ...]) -> bool:
    values_by_record: dict[tuple[int, ...], int] = {}
    for outcome in product((0, 1), repeat=3):
        record = tuple(outcome[index] for index in coordinates)
        target = parity(outcome)
        if record in values_by_record and values_by_record[record] != target:
            return False
        values_by_record[record] = target
    return True


FiniteFunction = Mapping[BitPair, Fraction]
Action = Callable[[BitPair], BitPair]


def average_over_z2(
    function: FiniteFunction,
    action: Action,
) -> dict[BitPair, Fraction]:
    return {
        outcome: (
            function[outcome] + function[action(outcome)]
        )
        / 2
        for outcome in product((0, 1), repeat=2)
    }


def invariant_under(
    function: FiniteFunction,
    action: Action,
) -> bool:
    return all(
        function[outcome] == function[action(outcome)]
        for outcome in product((0, 1), repeat=2)
    )


def main() -> None:
    # Three reversible couplings in the same finite system-probe arena induce
    # three different record channels. Admissibility of a coupling class does
    # not select one member.
    identity = lambda state: state
    controlled_not = lambda state: (
        state[0],
        state[1] ^ state[0],
    )
    controlled_not_then_probe_flip = lambda state: (
        state[0],
        state[1] ^ state[0] ^ 1,
    )

    constant_channel = reversible_record_channel(identity)
    copy_channel = reversible_record_channel(controlled_not)
    complement_channel = reversible_record_channel(
        controlled_not_then_probe_flip
    )
    induced_channels = {
        tuple(sorted(channel.items()))
        for channel in (
            constant_channel,
            copy_channel,
            complement_channel,
        )
    }
    assert len(induced_channels) == 3
    assert constant_channel == {0: 0, 1: 0}
    assert copy_channel == {0: 0, 1: 1}
    assert complement_channel == {0: 1, 1: 0}

    # Full-support parity pair. Every one-site and two-site marginal agrees
    # exactly, while the extended parity observable separates the states.
    plus = parity_distribution(1)
    minus = parity_distribution(-1)
    proper_subsets = tuple(
        coordinates
        for size in (1, 2)
        for coordinates in combinations(range(3), size)
    )
    marginal_equalities = {
        coordinates: marginal(plus, coordinates)
        == marginal(minus, coordinates)
        for coordinates in proper_subsets
    }
    assert all(marginal_equalities.values())
    assert all(
        set(marginal(plus, coordinates).values())
        == {Fraction(1, 2 ** len(coordinates))}
        for coordinates in proper_subsets
    )

    plus_parity_expectation = expectation(plus, parity_character)
    minus_parity_expectation = expectation(minus, parity_character)
    assert plus_parity_expectation == Fraction(1, 2)
    assert minus_parity_expectation == Fraction(-1, 2)
    assert not any(
        factors_through_subset(coordinates)
        for coordinates in proper_subsets
    )
    assert factors_through_subset((0, 1, 2))

    full_signature = kl_log_signature(plus, minus)
    assert full_signature == {
        Fraction(3): Fraction(3, 4),
        Fraction(1, 3): Fraction(1, 4),
    }
    local_signatures = {
        coordinates: kl_log_signature(
            marginal(plus, coordinates),
            marginal(minus, coordinates),
        )
        for coordinates in proper_subsets
    }
    assert all(signature == {} for signature in local_signatures.values())

    # Conditional expectations produced by two supplied Z2 actions are each
    # idempotent and invariant, yet their fixed-point quotients differ.
    outcomes_2 = tuple(product((0, 1), repeat=2))
    indicator_00 = {
        outcome: Fraction(int(outcome == (0, 0)))
        for outcome in outcomes_2
    }
    flip_first = lambda outcome: (outcome[0] ^ 1, outcome[1])
    flip_both = lambda outcome: (outcome[0] ^ 1, outcome[1] ^ 1)

    average_first = average_over_z2(indicator_00, flip_first)
    average_both = average_over_z2(indicator_00, flip_both)
    assert invariant_under(average_first, flip_first)
    assert invariant_under(average_both, flip_both)
    assert average_over_z2(average_first, flip_first) == average_first
    assert average_over_z2(average_both, flip_both) == average_both
    assert average_first != average_both

    result = {
        "claim_id": "HC-DU-118",
        "status": "PASS",
        "controls": {
            "same_finite_arena_admits_distinct_induced_record_channels": True,
            "all_proper_local_marginals_agree": True,
            "extended_parity_target_differs": True,
            "parity_target_fails_every_proper_subset_factorization": True,
            "full_record_reconstructs_parity_target": True,
            "proper_local_relative_entropy_is_zero": True,
            "full_relative_entropy_is_positive": True,
            "each_supplied_z2_action_has_an_idempotent_expectation": True,
            "different_supplied_actions_induce_different_expectations": True,
        },
        "witnesses": {
            "induced_record_channels": {
                "identity_coupling": constant_channel,
                "controlled_not": copy_channel,
                "controlled_not_then_probe_flip": complement_channel,
            },
            "proper_subsets": [
                list(coordinates)
                for coordinates in proper_subsets
            ],
            "plus_parity_expectation": "1/2",
            "minus_parity_expectation": "-1/2",
            "full_kl_signature": signature_text(full_signature),
            "full_kl_closed_form": "(1/2) log 3",
            "proper_local_kl_signatures": {
                "".join(str(index) for index in coordinates): signature_text(
                    signature
                )
                for coordinates, signature in local_signatures.items()
            },
            "flip_first_expectation_of_indicator_00": {
                str(outcome): str(value)
                for outcome, value in average_first.items()
            },
            "flip_both_expectation_of_indicator_00": {
                str(outcome): str(value)
                for outcome, value in average_both.items()
            },
        },
        "interpretation": {
            "instrument_boundary": (
                "Admitting a class of local system-probe couplings does not "
                "select one induced record channel."
            ),
            "algebra_boundary": (
                "A fixed proper-local algebra can erase an extended target; "
                "granting the extended observable changes the access algebra."
            ),
            "entropy_boundary": (
                "Relative-entropy loss quantifies a fixed restriction but "
                "does not select that restriction."
            ),
            "expectation_boundary": (
                "Group averaging is canonical only after the group action is "
                "supplied."
            ),
        },
        "limits": [
            "finite classical control, not a QFT or type-III computation",
            "reversible bit couplings are not Fewster-Verch instruments",
            "parity is only a finite shadow of an extended operator",
            "no generalized symmetry or physical algebra selected",
            "no record formation, retention, provenance, or access proved",
            "no empirical excess, ontology priority, or new physics",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
