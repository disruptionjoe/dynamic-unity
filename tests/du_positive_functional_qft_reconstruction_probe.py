#!/usr/bin/env python3
"""Exact finite controls for HC-DU-128.

The analytic result is the GNS/Wightman reconstruction boundary:

    fixed star algebra A + normalized positive functional omega
        -> Hilbert pairing, null quotient, cyclic representation and domain

The functional does not select A's multiplication, involution, source/test
space, spacetime, or physical record interface.  A finite correlation
truncation also does not determine an unrestricted functional hierarchy.

This exact rational regression preserves the smallest finite witnesses.  It
does not prove a new GNS, Wightman, or Osterwalder--Schrader theorem, construct
a QFT, select a physical state or algebra, transfer to a Krein theory, or
establish new physics.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_positive_functional_qft_reconstruction_result.json"
)

Scalar = Fraction
Vector = tuple[Scalar, ...]
Matrix = tuple[tuple[Scalar, ...], ...]


def vector(values: tuple[int | Scalar, ...]) -> Vector:
    return tuple(Fraction(value) for value in values)


def matrix(rows: tuple[tuple[int | Scalar, ...], ...]) -> Matrix:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column] for row in range(len(value)))
        for column in range(len(value[0]))
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def matrix_vector(operator: Matrix, operand: Vector) -> Vector:
    return tuple(
        sum(
            (
                operator[row][column] * operand[column]
                for column in range(len(operand))
            ),
            Fraction(0),
        )
        for row in range(len(operator))
    )


def dot(left: Vector, right: Vector) -> Scalar:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        Fraction(0),
    )


def determinant_2(value: Matrix) -> Scalar:
    return value[0][0] * value[1][1] - value[0][1] * value[1][0]


def pointwise(left: Vector, right: Vector) -> Vector:
    return tuple(
        a * b for a, b in zip(left, right, strict=True)
    )


def average(value: Vector) -> Scalar:
    return sum(value, Fraction(0)) / len(value)


def coordinates_in_basis(value: Vector, basis: tuple[Vector, ...]) -> Vector:
    # Both finite controls use orthonormal bases for their supplied state
    # pairing, so coefficient extraction is the state inner product.
    return tuple(average(pointwise(item, value)) for item in basis)


def matrix_2_coordinates(value: Matrix) -> Vector:
    upper_left, upper_right = value[0]
    lower_left, lower_right = value[1]
    return (
        (upper_left + lower_right) / 2,
        (upper_right + lower_left) / 2,
        (upper_right - lower_left) / 2,
        (upper_left - lower_right) / 2,
    )


def matrix_2_star_coordinates(value: Vector) -> Vector:
    coefficient_i, coefficient_x, coefficient_j, coefficient_z = value
    return (
        coefficient_i,
        coefficient_x,
        -coefficient_j,
        coefficient_z,
    )


def linear_combination(
    coefficients: Vector,
    basis: tuple[Matrix, ...],
) -> Matrix:
    return tuple(
        tuple(
            sum(
                (
                    coefficients[index] * basis[index][row][column]
                    for index in range(len(basis))
                ),
                Fraction(0),
            )
            for column in range(len(basis[0][0]))
        )
        for row in range(len(basis[0]))
    )


def left_regular_matrix(
    left: Vector,
    basis_coordinates: tuple[Vector, ...],
    product: Callable[[Vector, Vector], Vector],
) -> Matrix:
    columns = tuple(product(left, item) for item in basis_coordinates)
    return tuple(
        tuple(columns[column][row] for column in range(len(columns)))
        for row in range(len(columns[0]))
    )


def gram_matrix(
    basis_coordinates: tuple[Vector, ...],
    product: Callable[[Vector, Vector], Vector],
    star: Callable[[Vector], Vector],
    state: Callable[[Vector], Scalar],
) -> Matrix:
    return tuple(
        tuple(
            state(product(star(left), right))
            for right in basis_coordinates
        )
        for left in basis_coordinates
    )


def moment(
    nodes: tuple[int, ...],
    weights: tuple[Scalar, ...],
    order: int,
) -> Scalar:
    return sum(
        (
            weight * Fraction(node**order)
            for node, weight in zip(nodes, weights, strict=True)
        ),
        Fraction(0),
    )


def finite_difference_states(order: int) -> dict[str, Any]:
    nodes = tuple(range(order + 2))
    signed = tuple(
        Fraction(((-1) ** (order + 1 - index)) * comb(order + 1, index))
        for index in nodes
    )
    maximum = max(abs(value) for value in signed)
    baseline = Fraction(1, order + 2)
    epsilon = Fraction(1, 2 * (order + 2)) / maximum
    plus = tuple(baseline + epsilon * value for value in signed)
    minus = tuple(baseline - epsilon * value for value in signed)
    retained_plus = tuple(moment(nodes, plus, degree) for degree in range(order + 1))
    retained_minus = tuple(
        moment(nodes, minus, degree) for degree in range(order + 1)
    )
    next_plus = moment(nodes, plus, order + 1)
    next_minus = moment(nodes, minus, order + 1)
    return {
        "order": order,
        "nodes": nodes,
        "signed_difference": signed,
        "epsilon": epsilon,
        "state_plus": plus,
        "state_minus": minus,
        "retained_plus": retained_plus,
        "retained_minus": retained_minus,
        "next_plus": next_plus,
        "next_minus": next_minus,
        "finite_difference_next_gap": (
            next_plus - next_minus
        ),
        "expected_gap_magnitude": 2 * epsilon * factorial(order + 1),
    }


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


def main() -> None:
    checks: dict[str, bool] = {}

    # One real four-dimensional vector space admits two positive star-algebra
    # packets with identical one-point coordinates and identical GNS Gram
    # pairing, while their products are physically different.
    walsh_basis: tuple[Vector, ...] = (
        vector((1, 1, 1, 1)),
        vector((1, 1, -1, -1)),
        vector((1, -1, 1, -1)),
        vector((1, -1, -1, 1)),
    )
    coordinate_basis: tuple[Vector, ...] = (
        vector((1, 0, 0, 0)),
        vector((0, 1, 0, 0)),
        vector((0, 0, 1, 0)),
        vector((0, 0, 0, 1)),
    )

    def commutative_product(left: Vector, right: Vector) -> Vector:
        left_values = tuple(
            sum(
                (
                    left[index] * walsh_basis[index][point]
                    for index in range(4)
                ),
                Fraction(0),
            )
            for point in range(4)
        )
        right_values = tuple(
            sum(
                (
                    right[index] * walsh_basis[index][point]
                    for index in range(4)
                ),
                Fraction(0),
            )
            for point in range(4)
        )
        return coordinates_in_basis(
            pointwise(left_values, right_values),
            walsh_basis,
        )

    def commutative_star(value: Vector) -> Vector:
        return value

    def common_state(value: Vector) -> Scalar:
        return value[0]

    i2 = matrix(((1, 0), (0, 1)))
    x2 = matrix(((0, 1), (1, 0)))
    j2 = matrix(((0, 1), (-1, 0)))
    z2 = matrix(((1, 0), (0, -1)))
    matrix_basis = (i2, x2, j2, z2)

    def matrix_product(left: Vector, right: Vector) -> Vector:
        return matrix_2_coordinates(
            multiply(
                linear_combination(left, matrix_basis),
                linear_combination(right, matrix_basis),
            )
        )

    matrix_star = matrix_2_star_coordinates

    commutative_gram = gram_matrix(
        coordinate_basis,
        commutative_product,
        commutative_star,
        common_state,
    )
    matrix_gram = gram_matrix(
        coordinate_basis,
        matrix_product,
        matrix_star,
        common_state,
    )

    checks["same_state_coordinates"] = (
        tuple(common_state(item) for item in coordinate_basis)
        == (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    )
    checks["commutative_gram_is_identity"] = commutative_gram == identity(4)
    checks["matrix_gram_is_identity"] = matrix_gram == identity(4)
    checks["same_two_point_gram"] = commutative_gram == matrix_gram

    commutative_left = tuple(
        left_regular_matrix(item, coordinate_basis, commutative_product)
        for item in coordinate_basis
    )
    matrix_left = tuple(
        left_regular_matrix(item, coordinate_basis, matrix_product)
        for item in coordinate_basis
    )
    omega = coordinate_basis[0]

    checks["commutative_cyclic_vector_spans_basis"] = all(
        matrix_vector(operator, omega) == basis_item
        for operator, basis_item in zip(
            commutative_left,
            coordinate_basis,
            strict=True,
        )
    )
    checks["matrix_cyclic_vector_spans_basis"] = all(
        matrix_vector(operator, omega) == basis_item
        for operator, basis_item in zip(
            matrix_left,
            coordinate_basis,
            strict=True,
        )
    )
    checks["commutative_left_representation_is_multiplicative"] = all(
        left_regular_matrix(
            commutative_product(left, right),
            coordinate_basis,
            commutative_product,
        )
        == multiply(
            left_regular_matrix(left, coordinate_basis, commutative_product),
            left_regular_matrix(right, coordinate_basis, commutative_product),
        )
        for left in coordinate_basis
        for right in coordinate_basis
    )
    checks["matrix_left_representation_is_multiplicative"] = all(
        left_regular_matrix(
            matrix_product(left, right),
            coordinate_basis,
            matrix_product,
        )
        == multiply(
            left_regular_matrix(left, coordinate_basis, matrix_product),
            left_regular_matrix(right, coordinate_basis, matrix_product),
        )
        for left in coordinate_basis
        for right in coordinate_basis
    )
    checks["commutative_star_matches_gns_adjoint"] = all(
        left_regular_matrix(
            commutative_star(item),
            coordinate_basis,
            commutative_product,
        )
        == transpose(left_regular_matrix(item, coordinate_basis, commutative_product))
        for item in coordinate_basis
    )
    checks["matrix_star_matches_gns_adjoint"] = all(
        left_regular_matrix(matrix_star(item), coordinate_basis, matrix_product)
        == transpose(left_regular_matrix(item, coordinate_basis, matrix_product))
        for item in coordinate_basis
    )

    a = coordinate_basis[1]
    b = coordinate_basis[2]
    c = coordinate_basis[3]
    commutative_triple = common_state(
        commutative_product(commutative_product(a, b), c)
    )
    matrix_triple = common_state(matrix_product(matrix_product(a, b), c))
    commutative_commutator = tuple(
        left - right
        for left, right in zip(
            commutative_product(a, b),
            commutative_product(b, a),
            strict=True,
        )
    )
    matrix_commutator = tuple(
        left - right
        for left, right in zip(
            matrix_product(a, b),
            matrix_product(b, a),
            strict=True,
        )
    )
    checks["commutative_triple_is_positive_one"] = commutative_triple == 1
    checks["matrix_triple_is_negative_one"] = matrix_triple == -1
    checks["held_out_triple_separates_products"] = (
        commutative_triple != matrix_triple
    )
    checks["commutative_packet_commutes"] = all(
        value == 0 for value in commutative_commutator
    )
    checks["matrix_packet_is_noncommutative"] = any(
        value != 0 for value in matrix_commutator
    )

    # Positivity is load-bearing.  On R[x]/(x^2=1), omega(x)=2 gives a
    # normalized but nonpositive functional.
    indefinite_gram = matrix(((1, 2), (2, 1)))
    negative_vector = vector((1, -1))
    negative_norm = dot(
        negative_vector,
        matrix_vector(indefinite_gram, negative_vector),
    )
    checks["normalized_nonpositive_functional_has_negative_norm"] = (
        negative_norm == -2
    )
    checks["nonpositive_gram_has_negative_determinant"] = (
        determinant_2(indefinite_gram) == -3
    )

    # A positive nonfaithful state omega(x)=1 has a null ideal.  GNS quotients
    # it rather than treating the bare source vector space as physical.
    nonfaithful_gram = matrix(((1, 1), (1, 1)))
    null_vector = vector((1, -1))
    null_norm = dot(
        null_vector,
        matrix_vector(nonfaithful_gram, null_vector),
    )
    x_left = matrix(((0, 1), (1, 0)))
    checks["nonfaithful_state_has_exact_null_vector"] = null_norm == 0
    checks["nonfaithful_gram_has_rank_one"] = (
        determinant_2(nonfaithful_gram) == 0
        and nonfaithful_gram != matrix(((0, 0), (0, 0)))
    )
    checks["null_space_is_left_invariant"] = (
        matrix_vector(x_left, null_vector)
        == tuple(-value for value in null_vector)
    )

    # Small explicit moment control: same m0,m1,m2 and different m3.
    moments_a_nodes = (-1, 1)
    moments_a_weights = (Fraction(1, 2), Fraction(1, 2))
    moments_b_nodes = (-1, 0, 2)
    moments_b_weights = (Fraction(1, 3), Fraction(1, 2), Fraction(1, 6))
    moments_a = tuple(
        moment(moments_a_nodes, moments_a_weights, degree)
        for degree in range(4)
    )
    moments_b = tuple(
        moment(moments_b_nodes, moments_b_weights, degree)
        for degree in range(4)
    )
    checks["explicit_states_match_through_second_moment"] = (
        moments_a[:3] == moments_b[:3] == (Fraction(1), Fraction(0), Fraction(1))
    )
    checks["explicit_third_moment_is_first_leak"] = (
        moments_a[3] == 0 and moments_b[3] == 1
    )

    # General exact finite-difference construction through orders 0..6.
    finite_hierarchy_family = tuple(
        finite_difference_states(order) for order in range(7)
    )
    checks["finite_hierarchy_states_are_strictly_positive"] = all(
        all(weight > 0 for weight in member["state_plus"])
        and all(weight > 0 for weight in member["state_minus"])
        for member in finite_hierarchy_family
    )
    checks["finite_hierarchy_states_are_normalized"] = all(
        sum(member["state_plus"], Fraction(0)) == 1
        and sum(member["state_minus"], Fraction(0)) == 1
        for member in finite_hierarchy_family
    )
    checks["all_retained_moments_match"] = all(
        member["retained_plus"] == member["retained_minus"]
        for member in finite_hierarchy_family
    )
    checks["next_moment_always_leaks"] = all(
        member["next_plus"] != member["next_minus"]
        for member in finite_hierarchy_family
    )
    checks["finite_difference_gap_formula_is_exact"] = all(
        abs(member["finite_difference_next_gap"])
        == member["expected_gap_magnitude"]
        for member in finite_hierarchy_family
    )

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    artifact = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-128",
        "status": "PASS",
        "result": (
            "FIXED_STAR_ALGEBRA_PLUS_FULL_POSITIVE_FUNCTIONAL"
            "_RECONSTRUCTS_ITS_CYCLIC_GNS_PACKET"
            "+FUNCTIONAL_VALUES_AND_TWO_POINT_PAIRING_DO_NOT_SELECT_PRODUCT"
            "+POSITIVITY_IS_LOAD_BEARING"
            "+NULL_QUOTIENT_IS_FUNCTIONAL_RELATIVE"
            "+EVERY_FIXED_FINITE_CORRELATION_ORDER_HAS_A_NEXT_ORDER_LEAK"
            "+WIGHTMAN_OS_RECONSTRUCTION_IS_A_CONDITIONAL_POSITIVE"
            "+THEORETICAL_FUNCTIONAL_IS_NOT_A_FORMED_FINITE_RECORD"
            "+NO_GU_OR_INDEFINITE_METRIC_TRANSFER"
        ),
        "definitions": {
            "state_packet": "(A, *, omega)",
            "gns_pairing": "<[a],[b]> = omega(a* b)",
            "null_ideal": "N_omega = {a : omega(a* a)=0}",
            "cyclic_domain": "D_omega = pi_omega(A) Omega_omega",
            "full_correlation_functional": (
                "omega evaluated on every admitted algebra word/test tuple"
            ),
        },
        "same_state_and_pairing_different_product": {
            "basis": ["1", "a", "b", "c"],
            "state_coordinates": ["1", "0", "0", "0"],
            "commutative_gram": commutative_gram,
            "matrix_gram": matrix_gram,
            "commutative_triple_omega_abc": commutative_triple,
            "matrix_triple_omega_abc": matrix_triple,
            "commutative_commutator_ab": commutative_commutator,
            "matrix_commutator_ab": matrix_commutator,
            "interpretation": (
                "The linear functional and induced two-point Hilbert pairing "
                "are identical, while the supplied algebra product differs."
            ),
        },
        "fixed_packet_gns": {
            "commutative_left_representation": commutative_left,
            "matrix_left_representation": matrix_left,
            "cyclic_vector": omega,
            "pairing": identity(4),
            "domain_dimension": 4,
        },
        "positivity_boundary": {
            "algebra": "R[x]/(x^2=1)",
            "normalized_functional": "omega(1)=1, omega(x)=2",
            "gram": indefinite_gram,
            "negative_vector": negative_vector,
            "negative_norm": negative_norm,
            "consequence": "No positive Hilbert GNS packet follows.",
        },
        "null_quotient": {
            "algebra": "R[x]/(x^2=1)",
            "positive_state": "omega(1)=1, omega(x)=1",
            "gram": nonfaithful_gram,
            "null_vector": null_vector,
            "null_norm": null_norm,
            "quotient_dimension": 1,
        },
        "finite_hierarchy_first_leak": {
            "explicit_order_two": {
                "state_a": {
                    "nodes": moments_a_nodes,
                    "weights": moments_a_weights,
                    "moments_0_to_3": moments_a,
                },
                "state_b": {
                    "nodes": moments_b_nodes,
                    "weights": moments_b_weights,
                    "moments_0_to_3": moments_b,
                },
            },
            "general_family": finite_hierarchy_family,
            "status": "REGRESSION_OF_HC_DU_100_NOT_NEW_THEOREM",
        },
        "analytic_theorem": {
            "gns_reconstruction": (
                "For fixed A and positive omega, quotienting N_omega and "
                "completing gives a cyclic star representation unique up to "
                "the standard unitary equivalence."
            ),
            "wightman_reconstruction": (
                "A complete positive Wightman functional satisfying the "
                "declared axioms reconstructs the corresponding relativistic "
                "QFT representation up to unitary equivalence."
            ),
            "os_reconstruction": (
                "Euclidean Schwinger functions satisfying the precise OS "
                "axioms reconstruct Wightman/Hamiltonian data; reflection "
                "positivity is load-bearing."
            ),
            "algebra_antecedent": (
                "The functional cannot be evaluated on products until the "
                "algebra product, involution and test/source labels are fixed."
            ),
            "finite_record_boundary": (
                "No fixed finite correlation order determines an unrestricted "
                "positive functional hierarchy."
            ),
        },
        "local_model_learning_gate": {
            "disposition": "PROOF_FIRST_MINIMAL_REGRESSION_ONLY",
            "simulation": "not admitted",
            "hardware": "irrelevant",
            "learning": (
                "Formal reconstruction and exact counterexamples determine "
                "the boundary; the executable artifact preserves them only."
            ),
        },
        "checks": checks,
        "check_count": len(checks),
        "non_claims": [
            "not a new GNS, Wightman, Osterwalder-Schrader or moment theorem",
            "not a selected physical algebra, state, source, geometry or interface",
            "not a finite formed record or acquisition theorem",
            "not a GU, Krein, gauge-field or indefinite-metric reconstruction",
            "not field-ontology or direct-action-ontology selection",
            "not empirical excess, a new law, new physics or a prediction",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(artifact), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"PASS: {len(checks)}/{len(checks)} exact checks")
    print(f"artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
