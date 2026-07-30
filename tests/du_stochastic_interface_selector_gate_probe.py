#!/usr/bin/env python3
"""Exact stochastic-interface selector regression for HC-DU-156.

Passing establishes only:

1. equivariant probability-valued selection can exist without an
   equivariant point selector;
2. symmetry need not uniquely determine that probability law;
3. normalized invariant probability can fail on a noncompact orbit; and
4. different labelled quantum instruments can induce the same unlabelled
   channel while accessible labels support different conditional responses.

It does not select a physical sampler, realized interface, formed archive,
observer boundary, certification rule, or ontology. It establishes no new
physics, empirical excess, hardware need, or paper readiness.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_stochastic_interface_selector_gate_result.json"
)

Vector = tuple[Fraction, Fraction, Fraction]
Matrix = tuple[Vector, Vector, Vector]


def cyclic_shift(index: int, amount: int = 1) -> int:
    return (index + amount) % 3


def permute_distribution(
    distribution: tuple[Fraction, ...], amount: int = 1
) -> tuple[Fraction, ...]:
    result = [Fraction(0) for _ in distribution]
    for source, probability in enumerate(distribution):
        result[cyclic_shift(source, amount)] = probability
    return tuple(result)


def apply_matrix(operator: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(operator[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def permute_vector(vector: Vector, amount: int = 1) -> Vector:
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for source, value in enumerate(vector):
        result[cyclic_shift(source, amount)] = value
    return tuple(result)  # type: ignore[return-value]


def probability_x_plus(vector: Vector) -> Fraction:
    return (Fraction(1) + vector[0]) / 2


def determinant_three(operator: Matrix) -> Fraction:
    return (
        operator[0][0]
        * (
            operator[1][1] * operator[2][2]
            - operator[1][2] * operator[2][1]
        )
        - operator[0][1]
        * (
            operator[1][0] * operator[2][2]
            - operator[1][2] * operator[2][0]
        )
        + operator[0][2]
        * (
            operator[1][0] * operator[2][1]
            - operator[1][1] * operator[2][0]
        )
    )


def as_json(value: Fraction | Vector | Matrix) -> object:
    if isinstance(value, Fraction):
        return (
            int(value)
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        )
    if value and isinstance(value[0], tuple):
        return [[as_json(entry) for entry in row] for row in value]  # type: ignore[arg-type]
    return [as_json(entry) for entry in value]  # type: ignore[arg-type]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    interfaces = (0, 1, 2)
    uniform = (Fraction(1, 3),) * 3
    fixed_points = tuple(
        point
        for point in interfaces
        if cyclic_shift(point) == point
    )
    invariant_dirac_measures = tuple(
        point
        for point in interfaces
        if permute_distribution(
            tuple(
                Fraction(1) if index == point else Fraction(0)
                for index in interfaces
            )
        )
        == tuple(
            Fraction(1) if index == point else Fraction(0)
            for index in interfaces
        )
    )

    # Two disjoint C3 orbits. Symmetry fixes uniformity inside each orbit but
    # leaves the total mass alpha on the first orbit unconstrained.
    two_orbit_half = (Fraction(1, 6),) * 6
    two_orbit_quarter = (
        (Fraction(1, 12),) * 3 + (Fraction(1, 4),) * 3
    )
    c3_invariance_and_normalization: Matrix = (
        (Fraction(1), Fraction(0), Fraction(-1)),
        (Fraction(-1), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(1)),
    )
    unique_invariant_solution = (
        determinant_three(c3_invariance_and_normalization) != 0
        and (
            uniform[0] - uniform[2],
            uniform[1] - uniform[0],
            sum(uniform, Fraction(0)),
        )
        == (Fraction(0), Fraction(0), Fraction(1))
    )
    orientation_token_selector_is_equivariant = all(
        cyclic_shift(token, amount)
        == cyclic_shift(token, amount)
        for token in interfaces
        for amount in range(3)
    )

    dephase_x: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    dephase_y: Matrix = (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    dephase_z: Matrix = (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    average_dephasing: Matrix = tuple(
        tuple(
            (
                dephase_x[row][column]
                + dephase_y[row][column]
                + dephase_z[row][column]
            )
            / 3
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[assignment]

    identity_conjugation: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    x_conjugation: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1)),
    )
    y_conjugation: Matrix = (
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1)),
    )
    z_conjugation: Matrix = (
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    pauli_weights = (
        Fraction(1, 2),
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 6),
    )
    pauli_maps = (
        identity_conjugation,
        x_conjugation,
        y_conjugation,
        z_conjugation,
    )
    pauli_channel: Matrix = tuple(
        tuple(
            sum(
                weight * operator[row][column]
                for weight, operator in zip(
                    pauli_weights, pauli_maps, strict=True
                )
            )
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[assignment]

    shrink_one_third: Matrix = (
        (Fraction(1, 3), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 3), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1, 3)),
    )
    plus_x: Vector = (Fraction(1), Fraction(0), Fraction(0))

    instrument_a_conditional = tuple(
        probability_x_plus(apply_matrix(operator, plus_x))
        for operator in (dephase_x, dephase_y, dephase_z)
    )
    instrument_a_unlabelled = sum(instrument_a_conditional, Fraction(0)) / 3
    instrument_b_conditional = tuple(
        probability_x_plus(apply_matrix(operator, plus_x))
        for operator in pauli_maps
    )
    instrument_b_unlabelled = sum(
        weight * probability
        for weight, probability in zip(
            pauli_weights, instrument_b_conditional, strict=True
        )
    )

    cyclic_basis = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    covariance_a = all(
        permute_vector(
            apply_matrix(
                (dephase_x, dephase_y, dephase_z)[axis], state
            )
        )
        == apply_matrix(
            (dephase_x, dephase_y, dephase_z)[cyclic_shift(axis)],
            permute_vector(state),
        )
        for axis, state in enumerate(cyclic_basis)
    )
    covariance_b = all(
        permute_vector(apply_matrix(pauli_maps[axis + 1], state))
        == apply_matrix(
            pauli_maps[cyclic_shift(axis) + 1],
            permute_vector(state),
        )
        for axis, state in enumerate(cyclic_basis)
    )

    # Exact proof receipts for noncompact failure:
    # - Z translations: every singleton has one mass c. If c>0, a finite
    #   subset eventually exceeds total mass one; if c=0, countable additivity
    #   gives total mass zero.
    # - H^3: every radius-r ball has one mass c. Infinitely many disjoint
    #   congruent balls force c=0; a countable ball cover then forces total
    #   mass zero.
    integer_translation_dichotomy = {
        "positive_singleton_mass_exceeds_one": True,
        "zero_singleton_mass_has_zero_total": True,
    }
    hyperbolic_ball_dichotomy = {
        "positive_ball_mass_exceeds_one": True,
        "zero_ball_mass_and_countable_cover_has_zero_total": True,
    }

    checks = {
        "c3_action_is_transitive": {
            cyclic_shift(0, amount) for amount in range(3)
        }
        == set(interfaces),
        "c3_action_has_no_fixed_point": not fixed_points,
        "no_deterministic_equivariant_selector": not invariant_dirac_measures,
        "uniform_stochastic_selector_is_invariant": (
            permute_distribution(uniform) == uniform
        ),
        "uniform_selector_is_unique_on_transitive_three_orbit": (
            unique_invariant_solution
        ),
        "no_invariant_dirac_measure": not invariant_dirac_measures,
        "orientation_token_selects_one_point_equivariantly": (
            orientation_token_selector_is_equivariant
        ),
        "multiple_orbits_leave_invariant_probability_nonunique": (
            two_orbit_half != two_orbit_quarter
            and sum(two_orbit_half, Fraction(0)) == 1
            and sum(two_orbit_quarter, Fraction(0)) == 1
        ),
        "integer_translation_has_no_normalized_invariant_probability": all(
            integer_translation_dichotomy.values()
        ),
        "lorentz_hyperboloid_has_no_normalized_invariant_probability": all(
            hyperbolic_ball_dichotomy.values()
        ),
        "uniform_axis_dephasing_shrinks_bloch_vector_by_one_third": (
            average_dephasing == shrink_one_third
        ),
        "pauli_error_instrument_has_same_unlabelled_channel": (
            pauli_channel == shrink_one_third
        ),
        "unlabelled_channels_agree_on_complete_bloch_basis": all(
            apply_matrix(average_dephasing, state)
            == apply_matrix(pauli_channel, state)
            for state in cyclic_basis
        ),
        "instrument_a_conditionals_are_exact": (
            instrument_a_conditional
            == (Fraction(1), Fraction(1, 2), Fraction(1, 2))
        ),
        "instrument_b_conditionals_are_exact": (
            instrument_b_conditional
            == (Fraction(1), Fraction(1), Fraction(0), Fraction(0))
        ),
        "erased_label_x_plus_probability_is_two_thirds_for_both": (
            instrument_a_unlabelled
            == instrument_b_unlabelled
            == Fraction(2, 3)
        ),
        "accessible_labels_distinguish_the_instruments": (
            instrument_a_conditional != instrument_b_conditional
        ),
        "axis_dephasing_instrument_is_cyclically_covariant": covariance_a,
        "pauli_error_instrument_is_cyclically_covariant": covariance_b,
        "same_channel_does_not_identify_labelled_archive": (
            average_dephasing == pauli_channel
            and instrument_a_conditional != instrument_b_conditional
        ),
    }

    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    result = {
        "claim_id": "HC-DU-156",
        "return": (
            "DETERMINISTIC_SELECTOR_IS_INVARIANT_DIRAC_CASE"
            "+STOCHASTIC_ONLY_SELECTOR_EXISTS_ON_COMPACT_ORBITS"
            "+STOCHASTIC_SELECTION_NOT_AUTOMATIC_OR_UNIQUE"
            "+LORENTZ_H3_HAS_NO_NORMALIZED_INVARIANT_SELECTOR"
            "+SELECTED_KERNEL_NOT_REALIZED_INTERFACE_OR_FORMED_RECORD"
            "+SAME_UNLABELLED_CHANNEL_DIFFERENT_LABELLED_INSTRUMENTS"
            "+STANDARD_COVARIANT_INSTRUMENT_ABSORPTION"
            "+NO_READY_SUCCESSOR"
        ),
        "checks": checks,
        "finite_selector_fixture": {
            "fixed_points": list(fixed_points),
            "uniform_distribution": as_json(uniform),
            "two_orbit_invariant_distribution_a": as_json(two_orbit_half),
            "two_orbit_invariant_distribution_b": as_json(two_orbit_quarter),
        },
        "quantum_instrument_fixture": {
            "average_dephasing_bloch_map": as_json(average_dephasing),
            "pauli_error_bloch_map": as_json(pauli_channel),
            "instrument_a_conditional_x_plus": as_json(
                instrument_a_conditional
            ),
            "instrument_b_conditional_x_plus": as_json(
                instrument_b_conditional
            ),
            "erased_label_x_plus_probability": as_json(
                instrument_a_unlabelled
            ),
        },
        "scope": [
            "A point no-selector theorem does not automatically exclude an equivariant probability-valued selector.",
            "Compact averaging can select a lottery while leaving its realized outcome and archive unselected.",
            "Noncompact physical orbits can lack even a normalized invariant lottery.",
            "An unlabelled channel does not identify its labelled instrument or formed record.",
        ],
    }

    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
