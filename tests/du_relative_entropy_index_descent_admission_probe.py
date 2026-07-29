#!/usr/bin/env python3
"""Exact finite controls for HC-DU-117.

The probe preserves four typed facts:

1. a parameter-independent hidden conditional makes a record statistically
   sufficient and preserves KL divergence exactly;
2. a constant record can lose a positive divergence;
3. positive information loss does not decide every target-relative
   reconstruction question; and
4. a positive source kernel D^T D can erase determinant orientation.

This is a finite classical sufficiency and determinant-sign regression. It
does not implement Araki relative entropy, a type-III algebra, GU, a physical
record, channel capacity, an anomaly, or new physics.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Hashable, Mapping


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_relative_entropy_index_descent_admission_result.json"
)

Outcome = Hashable
Distribution = Mapping[Outcome, Fraction]


def normalized(distribution: Distribution) -> bool:
    return (
        all(probability >= 0 for probability in distribution.values())
        and sum(distribution.values(), Fraction(0)) == 1
    )


def kl_log_signature(
    numerator: Distribution,
    denominator: Distribution,
) -> dict[Fraction, Fraction]:
    """Represent KL exactly as sum_r coefficient[r] * log(r).

    A signature is enough for the exact equalities used here and avoids
    floating-point logarithms. Ratio-one terms are omitted.
    """
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


def joint_from_record_and_conditional(
    record_distribution: Mapping[int, Fraction],
    hidden_given_record: Mapping[int, tuple[Fraction, Fraction]],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for record, record_probability in record_distribution.items():
        conditional = hidden_given_record[record]
        if sum(conditional, Fraction(0)) != 1:
            raise ValueError("conditional probabilities must sum to one")
        for hidden, hidden_probability in enumerate(conditional):
            result[(record, hidden)] = (
                record_probability * hidden_probability
            )
    return result


def pushforward(
    distribution: Distribution,
    quotient: Mapping[Outcome, Outcome],
) -> dict[Outcome, Fraction]:
    result: defaultdict[Outcome, Fraction] = defaultdict(Fraction)
    for outcome, probability in distribution.items():
        result[quotient[outcome]] += probability
    return dict(result)


def factors_through(
    histories: tuple[Outcome, ...],
    record: Mapping[Outcome, Outcome],
    target: Mapping[Outcome, Outcome],
) -> bool:
    values_by_record: dict[Outcome, Outcome] = {}
    for history in histories:
        record_value = record[history]
        target_value = target[history]
        if (
            record_value in values_by_record
            and values_by_record[record_value] != target_value
        ):
            return False
        values_by_record[record_value] = target_value
    return True


def determinant_2x2(
    matrix: tuple[tuple[int, int], tuple[int, int]],
) -> int:
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )


def gram_2x2(
    matrix: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    return (
        (
            matrix[0][0] ** 2 + matrix[1][0] ** 2,
            matrix[0][0] * matrix[0][1]
            + matrix[1][0] * matrix[1][1],
        ),
        (
            matrix[0][1] * matrix[0][0]
            + matrix[1][1] * matrix[1][0],
            matrix[0][1] ** 2 + matrix[1][1] ** 2,
        ),
    )


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


def main() -> None:
    # Sufficient-record positive control. Both states share the same hidden
    # conditional K(h|r), so the likelihood ratio depends only on r.
    record_state_p = {0: Fraction(2, 3), 1: Fraction(1, 3)}
    record_state_q = {0: Fraction(1, 3), 1: Fraction(2, 3)}
    common_hidden_conditional = {
        0: (Fraction(3, 4), Fraction(1, 4)),
        1: (Fraction(1, 5), Fraction(4, 5)),
    }
    full_state_p = joint_from_record_and_conditional(
        record_state_p,
        common_hidden_conditional,
    )
    full_state_q = joint_from_record_and_conditional(
        record_state_q,
        common_hidden_conditional,
    )
    full_signature = kl_log_signature(full_state_p, full_state_q)
    record_signature = kl_log_signature(record_state_p, record_state_q)
    assert full_signature == record_signature

    record_projection = {
        outcome: outcome[0]
        for outcome in full_state_p
    }
    assert pushforward(full_state_p, record_projection) == record_state_p
    assert pushforward(full_state_q, record_projection) == record_state_q

    # Exact recovery is the shared conditional itself.
    recovered_p = joint_from_record_and_conditional(
        pushforward(full_state_p, record_projection),
        common_hidden_conditional,
    )
    recovered_q = joint_from_record_and_conditional(
        pushforward(full_state_q, record_projection),
        common_hidden_conditional,
    )
    assert recovered_p == full_state_p
    assert recovered_q == full_state_q

    # Insufficient-record control. The constant quotient loses the full
    # divergence (1/2) log 3 exactly.
    hidden_state_p = {0: Fraction(3, 4), 1: Fraction(1, 4)}
    hidden_state_q = {0: Fraction(1, 4), 1: Fraction(3, 4)}
    constant_record = {0: "same", 1: "same"}
    hidden_signature = kl_log_signature(hidden_state_p, hidden_state_q)
    constant_signature = kl_log_signature(
        pushforward(hidden_state_p, constant_record),
        pushforward(hidden_state_q, constant_record),
    )
    assert hidden_signature == {
        Fraction(3): Fraction(3, 4),
        Fraction(1, 3): Fraction(1, 4),
    }
    assert constant_signature == {}

    # The same lossy record is sufficient for one target and insufficient for
    # another. Information loss is therefore not itself a target-relative
    # physical remainder.
    histories = (0, 1)
    constant_target = {0: "available", 1: "available"}
    hidden_target = {0: "left", 1: "right"}
    assert factors_through(
        histories,
        constant_record,
        constant_target,
    )
    assert not factors_through(
        histories,
        constant_record,
        hidden_target,
    )

    # Naturality positive control: a bijective relabeling preserves the exact
    # KL signature.
    relabel = {0: "beta", 1: "alpha"}
    assert kl_log_signature(
        pushforward(hidden_state_p, relabel),
        pushforward(hidden_state_q, relabel),
    ) == hidden_signature

    # Minimal orientation-loss control. D_+ and D_- have the same positive
    # source kernel D^T D but opposite determinant signs.
    positive_orientation = ((1, 0), (0, 1))
    negative_orientation = ((-1, 0), (0, 1))
    positive_kernel = gram_2x2(positive_orientation)
    negative_kernel = gram_2x2(negative_orientation)
    assert positive_kernel == negative_kernel == ((1, 0), (0, 1))
    assert determinant_2x2(positive_orientation) == 1
    assert determinant_2x2(negative_orientation) == -1

    result = {
        "claim_id": "HC-DU-117",
        "status": "PASS",
        "controls": {
            "shared_conditional_record_is_statistically_sufficient": True,
            "relative_entropy_preserved_exactly_under_sufficient_record": True,
            "exact_recovery_from_sufficient_record": True,
            "constant_record_loses_positive_relative_entropy": True,
            "positive_information_loss_does_not_decide_target_reconstruction": True,
            "bijective_relabeling_preserves_relative_entropy": True,
            "positive_source_kernel_erases_determinant_orientation": True,
            "complete_determinant_retains_orientation": True,
        },
        "witnesses": {
            "sufficient_full_and_record_signature": signature_text(
                full_signature
            ),
            "insufficient_full_signature": signature_text(
                hidden_signature
            ),
            "insufficient_record_signature": signature_text(
                constant_signature
            ),
            "insufficient_loss_closed_form": "(1/2) log 3",
            "constant_target_factors": True,
            "hidden_target_factors": False,
            "shared_positive_kernel": [
                list(row)
                for row in positive_kernel
            ],
            "opposite_determinants": [1, -1],
        },
        "interpretation": {
            "relative_entropy": (
                "A divergence-loss and sufficiency diagnostic only after the "
                "algebra, state family, channel, and reference are fixed."
            ),
            "target_boundary": (
                "Full statistical sufficiency is stronger than reconstruction "
                "of one independently declared target."
            ),
            "descent_boundary": (
                "A positive source kernel may erase orientation retained by "
                "the complete determinant/effective action."
            ),
        },
        "limits": [
            "finite classical KL control, not a type-III computation",
            "no physical algebra, record channel, observer, or resource selected",
            "no channel capacity or Landauer law derived",
            "determinant-sign witness is not a GU generation model",
            "no GU source action or torsion-to-integer bridge supplied",
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
