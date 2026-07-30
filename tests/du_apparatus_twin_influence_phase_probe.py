#!/usr/bin/env python3
"""Exact apparatus-twin Gaussian influence-phase fixture for HC-DU-151.

The probe uses a periodic 1+1 lattice only as a finite theorem fixture.  A
translation-invariant positive scalar response is applied componentwise to
symmetric conserved sources.  Two controller completions keep the reduced
probe histories fixed and preserve total conservation.

For the quadratic influence phase I(T)=1/2 <T,G T>, adding one common
divergence-free completion K to both branches changes the relative phase by

    <T_1-T_0, G K>.

The K self-phase cancels.  Completion independence therefore holds exactly
when the branch-difference source is response-orthogonal to every admitted
completion direction.  This standard Gaussian identity is not a gravity
simulation or a numerical correction to any published phase.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable


NT = 4
NX = 5
SITE_COUNT = NT * NX
MASS_SQUARED = Fraction(1)
ARTIFACT_PATH = (
    Path(__file__).parent
    / "artifacts"
    / "du_apparatus_twin_influence_phase_result.json"
)

Scalar = list[list[Fraction]]
Vector = list[Scalar]
Tensor = list[list[Scalar]]


def q(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def scalar_field(
    function: Callable[[int, int], int | Fraction],
) -> Scalar:
    return [[q(function(t, x)) for x in range(NX)] for t in range(NT)]


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


def tensor_subtract(left: Tensor, right: Tensor) -> Tensor:
    return tensor_add(left, tensor_scale(Fraction(-1), right))


def tensor_scale(scale: Fraction | int, tensor: Tensor) -> Tensor:
    factor = q(scale)
    result = zero_tensor()
    for mu in range(2):
        for nu in range(2):
            for t in range(NT):
                for x in range(NX):
                    result[mu][nu][t][x] = (
                        factor * tensor[mu][nu][t][x]
                    )
    return result


def scalar_scale(scale: Fraction | int, field: Scalar) -> Scalar:
    factor = q(scale)
    return scalar_field(lambda t, x: factor * field[t][x])


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


def tensor_is_zero(tensor: Tensor) -> bool:
    return all(
        tensor[mu][nu][t][x] == 0
        for mu in range(2)
        for nu in range(2)
        for t in range(NT)
        for x in range(NX)
    )


def tensor_equal(left: Tensor, right: Tensor) -> bool:
    return tensor_is_zero(tensor_subtract(left, right))


def make_airy_tensor(phi: Scalar) -> Tensor:
    """Return a symmetric tensor with exact backward divergence zero."""

    b0 = backward_difference(phi, 0)
    b1 = backward_difference(phi, 1)
    result = zero_tensor()
    result[0][0] = backward_difference(b1, 1)
    mixed = scalar_scale(-1, backward_difference(b1, 0))
    result[0][1] = copy_scalar(mixed)
    result[1][0] = copy_scalar(mixed)
    result[1][1] = backward_difference(b0, 0)
    return result


def make_probe(branch: int) -> Tensor:
    probe = zero_tensor()
    probe[0][0] = scalar_field(
        lambda t, x: (branch + 2) * t + x * x - 3 * branch
    )
    mixed = scalar_field(
        lambda t, x: (
            ((3 + branch) * t + 2 * x + (branch + 1) * t * x) % 11
        )
        - 5
    )
    probe[0][1] = copy_scalar(mixed)
    probe[1][0] = copy_scalar(mixed)
    probe[1][1] = scalar_field(
        lambda t, x: (branch + 1) * t * t - (branch + 2) * x + 1
    )
    return probe


def flatten(field: Scalar) -> list[Fraction]:
    return [field[t][x] for t in range(NT) for x in range(NX)]


def unflatten(values: list[Fraction]) -> Scalar:
    return [
        values[t * NX : (t + 1) * NX]
        for t in range(NT)
    ]


def site_index(t: int, x: int) -> int:
    return (t % NT) * NX + (x % NX)


def response_matrix() -> list[list[Fraction]]:
    """Return I plus the positive periodic graph Laplacian."""

    matrix = [
        [Fraction(0) for _column in range(SITE_COUNT)]
        for _row in range(SITE_COUNT)
    ]
    for t in range(NT):
        for x in range(NX):
            row = site_index(t, x)
            matrix[row][row] += MASS_SQUARED + 4
            matrix[row][site_index(t + 1, x)] -= 1
            matrix[row][site_index(t - 1, x)] -= 1
            matrix[row][site_index(t, x + 1)] -= 1
            matrix[row][site_index(t, x - 1)] -= 1
    return matrix


def solve_linear(
    matrix: list[list[Fraction]],
    target: list[Fraction],
) -> list[Fraction]:
    size = len(target)
    augmented = [
        matrix[row][:] + [target[row]]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            row
            for row in range(column, size)
            if augmented[row][column] != 0
        )
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        divisor = augmented[column][column]
        augmented[column] = [
            value / divisor for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                augmented[row][entry] - factor * augmented[column][entry]
                for entry in range(size + 1)
            ]
    return [augmented[row][-1] for row in range(size)]


RESPONSE_MATRIX = response_matrix()


def response_scalar(field: Scalar) -> Scalar:
    return unflatten(solve_linear(RESPONSE_MATRIX, flatten(field)))


def response_tensor(tensor: Tensor) -> Tensor:
    result = zero_tensor()
    for mu in range(2):
        for nu in range(2):
            result[mu][nu] = response_scalar(tensor[mu][nu])
    return result


def tensor_pair(left: Tensor, right: Tensor) -> Fraction:
    return sum(
        (
            left[mu][nu][t][x] * right[mu][nu][t][x]
            for mu in range(2)
            for nu in range(2)
            for t in range(NT)
            for x in range(NX)
        ),
        Fraction(0),
    )


def response_pair(left: Tensor, right: Tensor) -> Fraction:
    return tensor_pair(left, response_tensor(right))


def influence_phase(source: Tensor) -> Fraction:
    return response_pair(source, source) / 2


def fraction_json(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


def tensor_norm_squared(tensor: Tensor) -> Fraction:
    return tensor_pair(tensor, tensor)


def build_result() -> dict[str, object]:
    probe_zero = make_probe(0)
    probe_one = make_probe(1)

    total_zero = make_airy_tensor(
        scalar_field(lambda t, x: ((2 * t * x + 3 * t + x) % 13) - 6)
    )
    total_one = make_airy_tensor(
        scalar_field(lambda t, x: ((t * x + t * t + 4 * x) % 17) - 8)
    )
    completion = make_airy_tensor(
        scalar_field(lambda t, x: ((3 * t * x + 2 * t + x * x) % 19) - 9)
    )
    second_completion = make_airy_tensor(
        scalar_field(lambda t, x: ((t * x * x + 5 * t + 3 * x) % 23) - 11)
    )

    controller_a_zero = tensor_subtract(total_zero, probe_zero)
    controller_a_one = tensor_subtract(total_one, probe_one)
    controller_b_zero = tensor_add(controller_a_zero, completion)
    controller_b_one = tensor_add(controller_a_one, completion)
    total_b_zero = tensor_add(probe_zero, controller_b_zero)
    total_b_one = tensor_add(probe_one, controller_b_one)

    branch_difference = tensor_subtract(total_one, total_zero)
    cross = response_pair(branch_difference, completion)
    second_cross = response_pair(branch_difference, second_completion)
    orthogonal_completion = tensor_subtract(
        tensor_scale(second_cross, completion),
        tensor_scale(cross, second_completion),
    )
    orthogonal_cross = response_pair(
        branch_difference,
        orthogonal_completion,
    )

    phase_a_zero = influence_phase(total_zero)
    phase_a_one = influence_phase(total_one)
    relative_a = phase_a_one - phase_a_zero
    phase_b_zero = influence_phase(total_b_zero)
    phase_b_one = influence_phase(total_b_one)
    relative_b = phase_b_one - phase_b_zero
    phase_shift = relative_b - relative_a
    completion_self_phase = influence_phase(completion)
    increment_zero = phase_b_zero - phase_a_zero
    increment_one = phase_b_one - phase_a_one

    total_c_zero = tensor_add(total_zero, orthogonal_completion)
    total_c_one = tensor_add(total_one, orthogonal_completion)
    relative_c = (
        influence_phase(total_c_one) - influence_phase(total_c_zero)
    )

    equal_branch_relative_a = influence_phase(total_zero) - influence_phase(
        total_zero
    )
    equal_branch_relative_b = influence_phase(
        tensor_add(total_zero, completion)
    ) - influence_phase(tensor_add(total_zero, completion))

    response_symmetry = response_pair(total_one, completion) == response_pair(
        completion,
        total_one,
    )

    assertions = {
        "both_reduced_probe_branches_are_open": (
            not vector_is_zero(tensor_divergence(probe_zero))
            and not vector_is_zero(tensor_divergence(probe_one))
        ),
        "all_base_and_completion_sources_are_conserved": all(
            vector_is_zero(tensor_divergence(source))
            for source in (
                total_zero,
                total_one,
                completion,
                second_completion,
                orthogonal_completion,
            )
        ),
        "controller_a_repairs_both_probe_divergences": (
            vectors_are_opposite(
                tensor_divergence(controller_a_zero),
                tensor_divergence(probe_zero),
            )
            and vectors_are_opposite(
                tensor_divergence(controller_a_one),
                tensor_divergence(probe_one),
            )
        ),
        "controller_b_repairs_both_probe_divergences": (
            vectors_are_opposite(
                tensor_divergence(controller_b_zero),
                tensor_divergence(probe_zero),
            )
            and vectors_are_opposite(
                tensor_divergence(controller_b_one),
                tensor_divergence(probe_one),
            )
        ),
        "apparatus_twins_keep_reduced_probe_histories_fixed": (
            all(
                tensor_equal(
                    tensor_subtract(total, controller),
                    probe,
                )
                for total, controller, probe in (
                    (total_zero, controller_a_zero, probe_zero),
                    (total_one, controller_a_one, probe_one),
                    (total_b_zero, controller_b_zero, probe_zero),
                    (total_b_one, controller_b_one, probe_one),
                )
            )
        ),
        "response_preserves_conservation": all(
            vector_is_zero(tensor_divergence(response_tensor(source)))
            for source in (
                total_zero,
                total_one,
                completion,
                orthogonal_completion,
            )
        ),
        "response_pair_is_symmetric_on_tested_sources": response_symmetry,
        "nonzero_common_completion_exists": (
            tensor_norm_squared(completion) > 0
        ),
        "common_completion_self_phase_cancels_from_relative_phase": (
            increment_one - increment_zero == cross
            and completion_self_phase
            == (
                increment_zero
                - response_pair(total_zero, completion)
            )
            == (
                increment_one
                - response_pair(total_one, completion)
            )
        ),
        "relative_phase_shift_equals_response_cross_pairing": (
            phase_shift == cross
        ),
        "conservation_does_not_force_phase_independence": (
            cross != 0 and relative_a != relative_b
        ),
        "nonzero_response_orthogonal_completion_exists": (
            tensor_norm_squared(orthogonal_completion) > 0
            and orthogonal_cross == 0
        ),
        "orthogonal_completion_preserves_relative_phase": (
            relative_c == relative_a
        ),
        "identical_branch_positive_control_has_zero_relative_phase": (
            equal_branch_relative_a == 0
            and equal_branch_relative_b == 0
        ),
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-151",
        "arena": {
            "spacetime": f"periodic {NT}x{NX} rational lattice",
            "source": "symmetric 2x2 tensor with backward divergence",
            "response": (
                "componentwise inverse of I plus periodic graph Laplacian"
            ),
            "phase": "I(T)=1/2 <T,G T>",
            "completion": (
                "common divergence-free discrete Airy tensor added to both "
                "branch controllers"
            ),
        },
        "exact_values": {
            "relative_phase_completion_a": fraction_json(relative_a),
            "relative_phase_completion_b": fraction_json(relative_b),
            "completion_induced_phase_shift": fraction_json(phase_shift),
            "response_cross_pairing": fraction_json(cross),
            "common_completion_self_phase": fraction_json(
                completion_self_phase
            ),
            "orthogonal_completion_cross_pairing": fraction_json(
                orthogonal_cross
            ),
            "relative_phase_orthogonal_completion": fraction_json(relative_c),
            "completion_norm_squared": fraction_json(
                tensor_norm_squared(completion)
            ),
            "orthogonal_completion_norm_squared": fraction_json(
                tensor_norm_squared(orthogonal_completion)
            ),
        },
        "assertions": assertions,
        "theorem_statement": (
            "For a symmetric Gaussian response, the change in relative "
            "branch phase under a common controller completion K is exactly "
            "<T_1-T_0,GK>. The K self-phase cancels. Hence the relative phase "
            "is constant on an admitted linear completion space exactly when "
            "the branch-difference source is response-orthogonal to that "
            "space. Conservation alone does not imply this condition."
        ),
        "scope": (
            "Exact finite Gaussian-response theorem fixture only; not a "
            "Lorentzian graviton propagator, realistic apparatus, prediction, "
            "or correction to a published gravitational phase."
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
    print(f"du_apparatus_twin_influence_phase_probe: {passed}/{total} PASS")
    print(json.dumps(result["exact_values"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
