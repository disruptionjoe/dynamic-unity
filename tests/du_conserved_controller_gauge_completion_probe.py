#!/usr/bin/env python3
"""Exact conserved-controller gauge-completion fixture for HC-DU-150.

The probe implements discrete summation by parts on a periodic 1+1 lattice.
It establishes two scoped facts:

1. the linearized coupling -1/2 sum(h_{mu nu} T^{mu nu}) is invariant under
   h -> h + D_mu xi_nu + D_nu xi_mu exactly when the tested total source has
   zero discrete divergence; and
2. adding an apparatus/controller with the opposite divergence repairs gauge
   invariance but does not select a unique completion, because an arbitrary
   divergence-free symmetric tensor can still be added.

This is an exact theorem fixture, not a simulation of gravity or a verdict on
any published interferometric phase.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable


NT = 4
NX = 5
ARTIFACT_PATH = (
    Path(__file__).parent
    / "artifacts"
    / "du_conserved_controller_gauge_completion_result.json"
)

Scalar = list[list[int]]
Vector = list[Scalar]
Tensor = list[list[Scalar]]


def scalar_field(function: Callable[[int, int], int]) -> Scalar:
    return [[function(t, x) for x in range(NX)] for t in range(NT)]


def zero_scalar() -> Scalar:
    return scalar_field(lambda _t, _x: 0)


def copy_scalar(field: Scalar) -> Scalar:
    return [row[:] for row in field]


def zero_tensor() -> Tensor:
    return [[zero_scalar() for _nu in range(2)] for _mu in range(2)]


def tensor_add(left: Tensor, right: Tensor) -> Tensor:
    result = zero_tensor()
    for mu in range(2):
        for nu in range(2):
            for t in range(NT):
                for x in range(NX):
                    result[mu][nu][t][x] = (
                        left[mu][nu][t][x] + right[mu][nu][t][x]
                    )
    return result


def tensor_scale(scale: int, tensor: Tensor) -> Tensor:
    result = zero_tensor()
    for mu in range(2):
        for nu in range(2):
            for t in range(NT):
                for x in range(NX):
                    result[mu][nu][t][x] = scale * tensor[mu][nu][t][x]
    return result


def forward_difference(field: Scalar, axis: int) -> Scalar:
    if axis == 0:
        return scalar_field(
            lambda t, x: field[(t + 1) % NT][x] - field[t][x]
        )
    return scalar_field(
        lambda t, x: field[t][(x + 1) % NX] - field[t][x]
    )


def backward_difference(field: Scalar, axis: int) -> Scalar:
    if axis == 0:
        return scalar_field(
            lambda t, x: field[t][x] - field[(t - 1) % NT][x]
        )
    return scalar_field(
        lambda t, x: field[t][x] - field[t][(x - 1) % NX]
    )


def tensor_divergence(tensor: Tensor) -> Vector:
    divergence: Vector = [zero_scalar(), zero_scalar()]
    for nu in range(2):
        for mu in range(2):
            derivative = backward_difference(tensor[mu][nu], mu)
            for t in range(NT):
                for x in range(NX):
                    divergence[nu][t][x] += derivative[t][x]
    return divergence


def gauge_metric_shift(xi: Vector) -> Tensor:
    shift = zero_tensor()
    for mu in range(2):
        for nu in range(2):
            first = forward_difference(xi[nu], mu)
            second = forward_difference(xi[mu], nu)
            for t in range(NT):
                for x in range(NX):
                    shift[mu][nu][t][x] = (
                        first[t][x] + second[t][x]
                    )
    return shift


def coupling(metric: Tensor, source: Tensor) -> Fraction:
    contraction = 0
    for mu in range(2):
        for nu in range(2):
            for t in range(NT):
                for x in range(NX):
                    contraction += (
                        metric[mu][nu][t][x]
                        * source[mu][nu][t][x]
                    )
    return Fraction(-contraction, 2)


def vector_pair(left: Vector, right: Vector) -> int:
    return sum(
        left[nu][t][x] * right[nu][t][x]
        for nu in range(2)
        for t in range(NT)
        for x in range(NX)
    )


def tensor_norm_squared(tensor: Tensor) -> int:
    return sum(
        tensor[mu][nu][t][x] ** 2
        for mu in range(2)
        for nu in range(2)
        for t in range(NT)
        for x in range(NX)
    )


def vector_is_zero(vector: Vector) -> bool:
    return all(
        vector[nu][t][x] == 0
        for nu in range(2)
        for t in range(NT)
        for x in range(NX)
    )


def vectors_are_opposite(left: Vector, right: Vector) -> bool:
    return all(
        left[nu][t][x] == -right[nu][t][x]
        for nu in range(2)
        for t in range(NT)
        for x in range(NX)
    )


def make_probe_source() -> Tensor:
    probe = zero_tensor()
    probe[0][0] = scalar_field(lambda t, x: 2 * t + x * x - 3)
    mixed = scalar_field(lambda t, x: ((3 * t + 2 * x + t * x) % 9) - 4)
    probe[0][1] = copy_scalar(mixed)
    probe[1][0] = copy_scalar(mixed)
    probe[1][1] = scalar_field(lambda t, x: t * t - 2 * x + 1)
    return probe


def make_divergence_free_addition() -> Tensor:
    """Return a nonconstant symmetric tensor K with backward-div(K)=0.

    For a periodic scalar phi, define the discrete Airy tensor

        K_00 = B_1 B_1 phi
        K_11 = B_0 B_0 phi
        K_01 = K_10 = -B_0 B_1 phi.

    The two backward differences commute, so each divergence component
    cancels identically.
    """

    phi = scalar_field(lambda t, x: ((t * x + 3 * t + 2 * x) % 11) - 5)
    b0 = backward_difference(phi, 0)
    b1 = backward_difference(phi, 1)
    addition = zero_tensor()
    addition[0][0] = backward_difference(b1, 1)
    mixed = tensor_scale_scalar(-1, backward_difference(b1, 0))
    addition[0][1] = copy_scalar(mixed)
    addition[1][0] = copy_scalar(mixed)
    addition[1][1] = backward_difference(b0, 0)
    return addition


def tensor_scale_scalar(scale: int, field: Scalar) -> Scalar:
    return scalar_field(lambda t, x: scale * field[t][x])


def fraction_json(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


def build_result() -> dict[str, object]:
    probe = make_probe_source()
    probe_divergence = tensor_divergence(probe)
    # Choosing xi=div(T_probe) makes the open-source gauge shift a positive
    # sum of squares under the exact summation-by-parts identity.
    xi = [copy_scalar(component) for component in probe_divergence]
    delta_h = gauge_metric_shift(xi)
    probe_gauge_variation = coupling(delta_h, probe)
    integration_by_parts_target = vector_pair(xi, probe_divergence)

    addition = make_divergence_free_addition()
    controller_one = tensor_scale(-1, probe)
    controller_two = tensor_add(controller_one, addition)
    total_one = tensor_add(probe, controller_one)
    total_two = tensor_add(probe, controller_two)

    controller_one_variation = coupling(delta_h, controller_one)
    controller_two_variation = coupling(delta_h, controller_two)
    total_one_variation = coupling(delta_h, total_one)
    total_two_variation = coupling(delta_h, total_two)

    probe_divergence_norm_squared = vector_pair(
        probe_divergence,
        probe_divergence,
    )
    addition_norm_squared = tensor_norm_squared(addition)
    # The divergence-free addition itself is a legal algebraic test field.
    # Its pairing separates the two conserved completions.
    held_out_one = coupling(addition, total_one)
    held_out_two = coupling(addition, total_two)

    assertions = {
        "probe_source_is_open_and_nonconserved": (
            probe_divergence_norm_squared > 0
        ),
        "exact_discrete_summation_by_parts_holds": (
            probe_gauge_variation == integration_by_parts_target
        ),
        "probe_only_coupling_has_nonzero_gauge_shift": (
            probe_gauge_variation > 0
        ),
        "controller_one_carries_opposite_exchange_current": vectors_are_opposite(
            tensor_divergence(controller_one),
            probe_divergence,
        ),
        "controller_two_carries_same_opposite_exchange_current": vectors_are_opposite(
            tensor_divergence(controller_two),
            probe_divergence,
        ),
        "first_total_source_is_conserved": vector_is_zero(
            tensor_divergence(total_one)
        ),
        "second_total_source_is_conserved": vector_is_zero(
            tensor_divergence(total_two)
        ),
        "controller_cancels_probe_gauge_shift": (
            controller_one_variation == -probe_gauge_variation
            and controller_two_variation == -probe_gauge_variation
        ),
        "both_completed_couplings_are_gauge_invariant": (
            total_one_variation == 0 and total_two_variation == 0
        ),
        "nonzero_divergence_free_completion_freedom_exists": (
            addition_norm_squared > 0
            and vector_is_zero(tensor_divergence(addition))
        ),
        "conserved_completions_differ_on_held_out_pairing": (
            held_out_one != held_out_two
            and held_out_two == Fraction(-addition_norm_squared, 2)
        ),
        "dropping_controller_restores_positive_control": (
            probe_gauge_variation != total_one_variation
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-150",
        "arena": {
            "spacetime": f"periodic {NT}x{NX} integer lattice",
            "tensor_rank": "symmetric 2x2",
            "gauge_shift": "delta_h(mu,nu)=D_mu xi_nu+D_nu xi_mu",
            "coupling": "-1/2 sum h(mu,nu) T(mu,nu)",
            "divergence": "sum_mu B_mu T(mu,nu)",
            "gauge_parameter": "xi=div(T_probe)",
        },
        "exact_values": {
            "probe_divergence_norm_squared": (
                probe_divergence_norm_squared
            ),
            "probe_gauge_variation": fraction_json(
                probe_gauge_variation
            ),
            "controller_one_gauge_variation": fraction_json(
                controller_one_variation
            ),
            "controller_two_gauge_variation": fraction_json(
                controller_two_variation
            ),
            "total_one_gauge_variation": fraction_json(
                total_one_variation
            ),
            "total_two_gauge_variation": fraction_json(
                total_two_variation
            ),
            "divergence_free_addition_norm_squared": (
                addition_norm_squared
            ),
            "held_out_pairing_total_one": fraction_json(held_out_one),
            "held_out_pairing_total_two": fraction_json(held_out_two),
        },
        "assertions": assertions,
        "theorem_statement": (
            "For the linearized symmetric-tensor coupling, a probe-only "
            "source with nonzero divergence has a gauge-dependent coupling. "
            "A controller carrying the opposite divergence restores total "
            "conservation and gauge invariance. Conservation alone selects "
            "only an affine completion class: divergence-free controller "
            "additions preserve gauge invariance while changing a held-out "
            "interaction pairing."
        ),
        "scope": (
            "Exact periodic-lattice Ward-identity and completion-freedom "
            "fixture only; not a simulation of linearized gravity, not a "
            "model of a laboratory controller, and not a verdict on the "
            "Chen--Giacomini phase."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT_PATH.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    passed = sum(result["assertions"].values())  # type: ignore[union-attr]
    total = len(result["assertions"])  # type: ignore[arg-type]
    print(f"du_conserved_controller_gauge_completion_probe: {passed}/{total} PASS")
    print(json.dumps(result["exact_values"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
