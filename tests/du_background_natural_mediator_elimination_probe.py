#!/usr/bin/env python3
"""Exact controls for HC-DU-116.

The probe separates pointwise source equivalence, background-natural source
equivalence, local mediator-response partitions, and determinant-inclusive
quantum background response. It is finite Schur-complement and Gaussian
determinant algebra. It does not model gravity, QFT, a physical record, an
observer, or new physics.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_background_natural_mediator_elimination_result.json"
)


def effective_coefficient(
    source_kernel: Fraction,
    couplings: Iterable[Fraction],
    mediator_kernels: Iterable[Fraction],
) -> Fraction:
    """Return A - sum_i B_i^2 / K_i for diagonal mediator kernel K."""
    coupling_values = tuple(couplings)
    kernel_values = tuple(mediator_kernels)
    if len(coupling_values) != len(kernel_values):
        raise ValueError("coupling and kernel dimensions must agree")
    if any(value == 0 for value in kernel_values):
        raise ValueError("mediator kernels must be invertible")
    return source_kernel - sum(
        (
            coupling * coupling / kernel
            for coupling, kernel in zip(
                coupling_values,
                kernel_values,
                strict=True,
            )
        ),
        Fraction(0),
    )


def effective_coefficient_derivative(
    source_kernel_derivative: Fraction,
    couplings: Iterable[Fraction],
    coupling_derivatives: Iterable[Fraction],
    mediator_kernels: Iterable[Fraction],
    mediator_kernel_derivatives: Iterable[Fraction],
) -> Fraction:
    """Differentiate A - sum_i B_i^2 / K_i exactly at one background."""
    values = tuple(
        zip(
            couplings,
            coupling_derivatives,
            mediator_kernels,
            mediator_kernel_derivatives,
            strict=True,
        )
    )
    if any(kernel == 0 for _, _, kernel, _ in values):
        raise ValueError("mediator kernels must be invertible")
    return source_kernel_derivative + sum(
        (
            -(Fraction(2) * coupling * coupling_derivative / kernel)
            + (
                coupling
                * coupling
                * kernel_derivative
                / (kernel * kernel)
            )
            for (
                coupling,
                coupling_derivative,
                kernel,
                kernel_derivative,
            ) in values
        ),
        Fraction(0),
    )


def stationary_mediator(
    coupling: Fraction,
    mediator_kernel: Fraction,
    source: Fraction,
) -> Fraction:
    if mediator_kernel == 0:
        raise ValueError("mediator kernel must be invertible")
    return -coupling * source / mediator_kernel


def full_partial_background_derivative(
    source_kernel_derivative: Fraction,
    coupling_derivative: Fraction,
    mediator_kernel_derivative: Fraction,
    source: Fraction,
    mediator: Fraction,
) -> Fraction:
    """Partial lambda derivative of S(j, phi; lambda) at fixed j and phi."""
    return (
        Fraction(1, 2)
        * source_kernel_derivative
        * source
        * source
        + coupling_derivative * source * mediator
        + Fraction(1, 2)
        * mediator_kernel_derivative
        * mediator
        * mediator
    )


def effective_action(
    effective_kernel: Fraction,
    source: Fraction,
) -> Fraction:
    return Fraction(1, 2) * effective_kernel * source * source


def effective_action_derivative(
    effective_kernel_derivative: Fraction,
    source: Fraction,
) -> Fraction:
    return (
        Fraction(1, 2)
        * effective_kernel_derivative
        * source
        * source
    )


def log_determinant_derivative(
    mediator_kernels: Iterable[Fraction],
    mediator_kernel_derivatives: Iterable[Fraction],
) -> Fraction:
    """Return d log det K / d lambda = tr(K^-1 K') for diagonal K."""
    pairs = tuple(
        zip(
            mediator_kernels,
            mediator_kernel_derivatives,
            strict=True,
        )
    )
    if any(kernel == 0 for kernel, _ in pairs):
        raise ValueError("mediator kernels must be invertible")
    return sum(
        (
            kernel_derivative / kernel
            for kernel, kernel_derivative in pairs
        ),
        Fraction(0),
    )


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    # Positive envelope control with nontrivial A, B, K and their derivatives.
    source = Fraction(7, 11)
    source_kernel = Fraction(3)
    source_kernel_derivative = Fraction(2)
    coupling = Fraction(2)
    coupling_derivative = Fraction(1)
    mediator_kernel = Fraction(5)
    mediator_kernel_derivative = Fraction(3)

    mediator = stationary_mediator(
        coupling,
        mediator_kernel,
        source,
    )
    coefficient_derivative = effective_coefficient_derivative(
        source_kernel_derivative,
        (coupling,),
        (coupling_derivative,),
        (mediator_kernel,),
        (mediator_kernel_derivative,),
    )
    envelope_derivative = full_partial_background_derivative(
        source_kernel_derivative,
        coupling_derivative,
        mediator_kernel_derivative,
        source,
        mediator,
    )
    reduced_derivative = effective_action_derivative(
        coefficient_derivative,
        source,
    )
    assert envelope_derivative == reduced_derivative

    # Pointwise twins: same source action at lambda_0, different first
    # background derivative. Both have A=0, B=1, K=1 at lambda_0; only K'
    # differs.
    twin_coefficient_1 = effective_coefficient(
        Fraction(0),
        (Fraction(1),),
        (Fraction(1),),
    )
    twin_coefficient_2 = effective_coefficient(
        Fraction(0),
        (Fraction(1),),
        (Fraction(1),),
    )
    assert twin_coefficient_1 == twin_coefficient_2 == Fraction(-1)
    assert effective_action(
        twin_coefficient_1,
        source,
    ) == effective_action(
        twin_coefficient_2,
        source,
    )

    twin_derivative_1 = effective_coefficient_derivative(
        Fraction(0),
        (Fraction(1),),
        (Fraction(0),),
        (Fraction(1),),
        (Fraction(1),),
    )
    twin_derivative_2 = effective_coefficient_derivative(
        Fraction(0),
        (Fraction(1),),
        (Fraction(0),),
        (Fraction(1),),
        (Fraction(2),),
    )
    assert twin_derivative_1 == Fraction(1)
    assert twin_derivative_2 == Fraction(2)
    assert effective_action_derivative(
        twin_derivative_1,
        source,
    ) != effective_action_derivative(
        twin_derivative_2,
        source,
    )

    # Full-family absorption control. One- and two-channel completions share
    # the same effective source coefficient and derivative when every channel
    # carries the same background-dependent K(lambda).
    family_kernel = Fraction(5, 3)
    family_kernel_derivative = Fraction(7, 4)
    one_family_coefficient = effective_coefficient(
        Fraction(0),
        (Fraction(1),),
        (family_kernel,),
    )
    two_family_coefficient = effective_coefficient(
        Fraction(0),
        (Fraction(3, 5), Fraction(4, 5)),
        (family_kernel, family_kernel),
    )
    one_family_derivative = effective_coefficient_derivative(
        Fraction(0),
        (Fraction(1),),
        (Fraction(0),),
        (family_kernel,),
        (family_kernel_derivative,),
    )
    two_family_derivative = effective_coefficient_derivative(
        Fraction(0),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(0), Fraction(0)),
        (family_kernel, family_kernel),
        (family_kernel_derivative, family_kernel_derivative),
    )
    assert one_family_coefficient == two_family_coefficient
    assert one_family_derivative == two_family_derivative

    # The same total two-channel derivative has a branch-relative internal
    # allocation. The source kernel fixes only the sum, not one local channel
    # or mediator-stress partition.
    channel_derivative_contributions = (
        Fraction(9, 25) * one_family_derivative,
        Fraction(16, 25) * one_family_derivative,
    )
    assert sum(
        channel_derivative_contributions,
        Fraction(0),
    ) == one_family_derivative
    assert channel_derivative_contributions != (
        one_family_derivative,
    )

    # A Gaussian determinant is source-independent at a frozen background but
    # its background derivative need not vanish. Source-equivalent one- and
    # two-channel families have different determinant derivatives because the
    # latter contains an additional mediator direction.
    one_logdet_derivative = log_determinant_derivative(
        (family_kernel,),
        (family_kernel_derivative,),
    )
    two_logdet_derivative = log_determinant_derivative(
        (family_kernel, family_kernel),
        (family_kernel_derivative, family_kernel_derivative),
    )
    assert one_logdet_derivative != 0
    assert two_logdet_derivative == 2 * one_logdet_derivative

    result = {
        "claim_id": "HC-DU-116",
        "status": "PASS",
        "controls": {
            "on_shell_background_envelope_identity_exact": True,
            "pointwise_source_equivalence_not_derivative_equivalence": True,
            "held_out_background_response_separates_pointwise_twins": True,
            "full_parameter_kernel_equivalence_preserves_total_source_response": True,
            "local_mediator_response_partition_not_identified": True,
            "source_independent_determinant_has_background_response": True,
            "determinant_response_not_fixed_by_source_kernel": True,
        },
        "witnesses": {
            "envelope_derivative": fraction_text(envelope_derivative),
            "pointwise_twin_effective_kernel": fraction_text(
                twin_coefficient_1
            ),
            "pointwise_twin_kernel_derivatives": [
                fraction_text(twin_derivative_1),
                fraction_text(twin_derivative_2),
            ],
            "full_family_effective_kernel": fraction_text(
                one_family_coefficient
            ),
            "full_family_kernel_derivative": fraction_text(
                one_family_derivative
            ),
            "two_channel_derivative_partition": [
                fraction_text(value)
                for value in channel_derivative_contributions
            ],
            "one_vs_two_channel_logdet_derivatives": [
                fraction_text(one_logdet_derivative),
                fraction_text(two_logdet_derivative),
            ],
        },
        "boundary": (
            "Regression only: no gravity or QFT model, metric selection, "
            "stress-energy prediction, counterterm prescription, physical "
            "record, access boundary, ontology priority, empirical excess, "
            "new physics, prediction, paper, hardware, or external action."
        ),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
