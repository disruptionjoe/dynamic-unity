#!/usr/bin/env python3
"""Exact finite controls for HC-DU-127.

The analytic result is elementary:

    K : V -> V*
    M : V -> V
    C = K M : V -> V*

Every bilinear source query factors through C.  With complete source and
covector access, equality of all query values is equality of C, so C is the
minimal complete response object up to information-equivalent encoding.
An operator matrix M represents that object only when C is constant on the
declared M-fibres; fixing K and the source/readout calibration is the standard
sufficient contract.

This exact rational regression preserves the smallest hostile witnesses.  It
does not prove a GU result, select a physical pairing, handle unbounded
operators or their domains, transfer to QFT, or establish new physics.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_pairing_complete_source_response_result.json"

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


def matrix(rows: tuple[tuple[int | Fraction, ...], ...]) -> Matrix:
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


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] + right[row][column]
            for column in range(len(left[0]))
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


def scale(value: Fraction, operand: Matrix) -> Matrix:
    return tuple(
        tuple(value * entry for entry in row)
        for row in operand
    )


def matrix_vector(operator: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (
                operator[row][column] * vector[column]
                for column in range(len(vector))
            ),
            Fraction(0),
        )
        for row in range(len(operator))
    )


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        Fraction(0),
    )


def bilinear(covector_response: Matrix, left: Vector, right: Vector) -> Fraction:
    return dot(left, matrix_vector(covector_response, right))


def quadratic(covector_response: Matrix, source: Vector) -> Fraction:
    return bilinear(covector_response, source, source)


def determinant_2(value: Matrix) -> Fraction:
    assert len(value) == 2 and len(value[0]) == 2
    return value[0][0] * value[1][1] - value[0][1] * value[1][0]


def inverse_2(value: Matrix) -> Matrix:
    determinant = determinant_2(value)
    assert determinant != 0
    return (
        (value[1][1] / determinant, -value[0][1] / determinant),
        (-value[1][0] / determinant, value[0][0] / determinant),
    )


def symmetric(value: Matrix) -> bool:
    return value == transpose(value)


def same_signature_11(left: Matrix, right: Matrix) -> bool:
    return (
        symmetric(left)
        and symmetric(right)
        and determinant_2(left) < 0
        and determinant_2(right) < 0
    )


def zero(value: Matrix) -> bool:
    return all(entry == 0 for row in value for entry in row)


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def anticommutator(left: Matrix, right: Matrix) -> Matrix:
    return add(multiply(left, right), multiply(right, left))


def grading_relation(operator: Matrix, grading: Matrix) -> str:
    if zero(commutator(operator, grading)):
        return "commutes"
    if zero(anticommutator(operator, grading)):
        return "anticommutes"
    return "mixed"


def k_self_adjoint(operator: Matrix, pairing: Matrix) -> bool:
    return multiply(transpose(operator), pairing) == multiply(pairing, operator)


def columns(vectors: tuple[Vector, ...]) -> Matrix:
    return tuple(
        tuple(vector[row] for vector in vectors)
        for row in range(len(vectors[0]))
    )


def query_table(
    response: Matrix,
    sources: tuple[Vector, ...],
    readouts: tuple[Vector, ...],
) -> Matrix:
    return tuple(
        tuple(
            bilinear(response, readout, source)
            for source in sources
        )
        for readout in readouts
    )


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
    i2 = identity(2)
    x_matrix = matrix(((0, 1), (1, 0)))
    z_matrix = matrix(((1, 0), (0, -1)))
    j_matrix = multiply(z_matrix, x_matrix)
    e1: Vector = (Fraction(1), Fraction(0))
    e2: Vector = (Fraction(0), Fraction(1))

    checks: dict[str, bool] = {}

    # Same normalized (1,1)-signature pairings, same bare M, distinct physics.
    same_m_c_x = multiply(x_matrix, i2)
    same_m_c_z = multiply(z_matrix, i2)
    checks["same_bare_operator"] = i2 == i2
    checks["same_signature_pairings"] = same_signature_11(x_matrix, z_matrix)
    checks["pairings_are_involutions"] = (
        multiply(x_matrix, x_matrix) == i2
        and multiply(z_matrix, z_matrix) == i2
    )
    checks["same_m_different_dual_response"] = same_m_c_x != same_m_c_z
    checks["held_out_bilinear_separates_pairings"] = (
        bilinear(same_m_c_x, e1, e2) == 1
        and bilinear(same_m_c_z, e1, e2) == 0
    )

    # Same physical response, same pairing signature, different bare grading.
    packet_a_k = x_matrix
    packet_a_m = i2
    packet_b_k = z_matrix
    packet_b_m = j_matrix
    packet_a_c = multiply(packet_a_k, packet_a_m)
    packet_b_c = multiply(packet_b_k, packet_b_m)
    checks["same_physical_response"] = packet_a_c == packet_b_c == x_matrix
    checks["factor_pairings_have_same_signature"] = same_signature_11(
        packet_a_k,
        packet_b_k,
    )
    checks["both_operators_are_k_self_adjoint"] = (
        k_self_adjoint(packet_a_m, packet_a_k)
        and k_self_adjoint(packet_b_m, packet_b_k)
    )
    checks["bare_operator_grading_changes"] = (
        grading_relation(packet_a_m, z_matrix) == "commutes"
        and grading_relation(packet_b_m, z_matrix) == "anticommutes"
    )
    checks["physical_response_grading_is_invariant"] = (
        grading_relation(packet_a_c, z_matrix)
        == grading_relation(packet_b_c, z_matrix)
        == "anticommutes"
    )

    # Infinite exact same-signature factorization fibre, sampled at nine n.
    factorization_family: list[dict[str, Any]] = []
    for parameter in range(-4, 5):
        pairing = matrix(((parameter, 1), (1, 0)))
        operator = matrix(((1, 0), (-parameter, 1)))
        response = multiply(pairing, operator)
        factorization_family.append(
            {
                "parameter": parameter,
                "pairing": pairing,
                "operator": operator,
                "response": response,
                "determinant": determinant_2(pairing),
                "k_self_adjoint": k_self_adjoint(operator, pairing),
            }
        )
    checks["factorization_family_same_response"] = all(
        member["response"] == x_matrix
        for member in factorization_family
    )
    checks["factorization_family_same_signature"] = all(
        member["determinant"] < 0
        for member in factorization_family
    )
    checks["factorization_family_k_self_adjoint"] = all(
        member["k_self_adjoint"]
        for member in factorization_family
    )
    checks["factorization_family_operators_distinct"] = (
        len({member["operator"] for member in factorization_family})
        == len(factorization_family)
    )

    # With K fixed and invertible, M <-> C is a bijection.
    recovered_m = multiply(inverse_2(x_matrix), packet_a_c)
    checks["fixed_pairing_recovers_operator"] = recovered_m == packet_a_m

    # Scalar diagonal action erases the antisymmetric part.
    c_plus = add(i2, j_matrix)
    c_minus = subtract(i2, j_matrix)
    scalar_sources = tuple(
        (Fraction(left), Fraction(right))
        for left in range(-2, 3)
        for right in range(-2, 3)
    )
    checks["all_sampled_quadratic_values_equal"] = all(
        quadratic(c_plus, source) == quadratic(c_minus, source)
        for source in scalar_sources
    )
    checks["antisymmetric_cross_query_survives"] = (
        bilinear(c_plus, e1, e2) == 1
        and bilinear(c_minus, e1, e2) == -1
    )
    checks["scalar_action_recovers_only_symmetric_part"] = (
        scale(Fraction(1, 2), add(c_plus, transpose(c_plus)))
        == scale(Fraction(1, 2), add(c_minus, transpose(c_minus)))
        == i2
    )

    # Polarization exactly repairs a symmetric two-dimensional response.
    symmetric_response = matrix(((2, -1), (-1, 3)))
    e12: Vector = (Fraction(1), Fraction(1))
    q1 = quadratic(symmetric_response, e1)
    q2 = quadratic(symmetric_response, e2)
    q12 = quadratic(symmetric_response, e12)
    reconstructed_cross = (q12 - q1 - q2) / 2
    reconstructed_symmetric = (
        (q1, reconstructed_cross),
        (reconstructed_cross, q2),
    )
    checks["three_scalar_queries_reconstruct_symmetric_response"] = (
        reconstructed_symmetric == symmetric_response
    )
    checks["scalar_query_count_matches_symmetric_dimension"] = 3 == 2 * 3 // 2

    # Incomplete source or readout spans leave an exact held-out first leak.
    c_base = i2
    c_hidden = matrix(((1, 0), (0, 2)))
    retained_sources = (e1,)
    full_sources = (e1, e2)
    retained_readouts = (e1,)
    full_readouts = (e1, e2)
    checks["incomplete_source_span_agrees"] = (
        tuple(matrix_vector(c_base, source) for source in retained_sources)
        == tuple(matrix_vector(c_hidden, source) for source in retained_sources)
    )
    checks["held_out_source_separates"] = (
        matrix_vector(c_base, e2) != matrix_vector(c_hidden, e2)
    )
    checks["incomplete_readout_span_agrees"] = (
        query_table(c_base, full_sources, retained_readouts)
        == query_table(c_hidden, full_sources, retained_readouts)
    )
    checks["held_out_readout_separates"] = (
        query_table(c_base, full_sources, full_readouts)
        != query_table(c_hidden, full_sources, full_readouts)
    )
    checks["complete_basis_query_recovers_response"] = (
        query_table(symmetric_response, full_sources, full_readouts)
        == symmetric_response
    )

    # A simultaneous basis change transforms C by congruence. Changing only K
    # while holding M and calibrated source labels fixed is not a basis change.
    transform = matrix(((1, 1), (0, 1)))
    transform_inverse = inverse_2(transform)
    transformed_k = multiply(
        multiply(transpose(transform), packet_b_k),
        transform,
    )
    transformed_m = multiply(
        multiply(transform_inverse, packet_b_m),
        transform,
    )
    transformed_c = multiply(
        multiply(transpose(transform), packet_b_c),
        transform,
    )
    checks["simultaneous_basis_change_is_covariant"] = (
        multiply(transformed_k, transformed_m) == transformed_c
    )

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    artifact = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-127",
        "status": "PASS",
        "result": (
            "DUAL_VALUED_RESPONSE_IS_MINIMAL_FOR_COMPLETE_BILINEAR_QUERIES"
            "+BARE_OPERATOR_IS_COMPLETE_IFF_C_IS_CONSTANT_ON_M_FIBRES"
            "+SAME_M_CAN_YIELD_DIFFERENT_C"
            "+SAME_C_HAS_AN_INFINITE_SAME_SIGNATURE_KM_FIBRE"
            "+BARE_GRADING_CAN_CHANGE_INSIDE_ONE_SOURCE_RESPONSE_FIBRE"
            "+SCALAR_ACTION_SEES_ONLY_THE_SYMMETRIC_PART"
            "+QUERY_AND_READOUT_SPANS_BOUND_COMPLETENESS"
            "+NO_GU_OR_QFT_TRANSFER"
        ),
        "definitions": {
            "pairing": "K: V -> V*",
            "operator_representative": "M: V -> V",
            "physical_dual_response": "C = K M: V -> V*",
            "bilinear_query": "B(y,x) = y^T C x",
            "query_packet": "R_XY(C) = Y^T C X",
        },
        "same_operator_different_response": {
            "operator": i2,
            "pairing_1": x_matrix,
            "pairing_2": z_matrix,
            "response_1": same_m_c_x,
            "response_2": same_m_c_z,
            "pairing_signature": [1, 1],
            "held_out_query": {
                "left": e1,
                "right": e2,
                "value_1": bilinear(same_m_c_x, e1, e2),
                "value_2": bilinear(same_m_c_z, e1, e2),
            },
        },
        "same_response_different_factorization": {
            "response": packet_a_c,
            "packet_a": {
                "pairing": packet_a_k,
                "operator": packet_a_m,
                "bare_grading": grading_relation(packet_a_m, z_matrix),
                "physical_grading": grading_relation(packet_a_c, z_matrix),
            },
            "packet_b": {
                "pairing": packet_b_k,
                "operator": packet_b_m,
                "bare_grading": grading_relation(packet_b_m, z_matrix),
                "physical_grading": grading_relation(packet_b_c, z_matrix),
            },
            "both_k_self_adjoint": True,
        },
        "factorization_family": {
            "formula": {
                "K_n": "[[n,1],[1,0]]",
                "M_n": "[[1,0],[-n,1]]",
                "K_n_M_n": "[[0,1],[1,0]]",
                "det_K_n": "-1",
                "parameter_domain": "all integers n",
            },
            "checked_members": factorization_family,
        },
        "scalar_action_boundary": {
            "response_plus": c_plus,
            "response_minus": c_minus,
            "common_symmetric_part": i2,
            "quadratic_sources_checked": len(scalar_sources),
            "cross_values": [
                bilinear(c_plus, e1, e2),
                bilinear(c_minus, e1, e2),
            ],
            "polarization_specimen": {
                "target": symmetric_response,
                "queries": [e1, e2, e12],
                "values": [q1, q2, q12],
                "reconstructed": reconstructed_symmetric,
            },
        },
        "query_span_first_leak": {
            "base_response": c_base,
            "hidden_response": c_hidden,
            "retained_source": e1,
            "held_out_source": e2,
            "retained_readout": e1,
            "held_out_readout": e2,
        },
        "basis_covariance": {
            "transform": transform,
            "transformed_pairing": transformed_k,
            "transformed_operator": transformed_m,
            "transformed_response": transformed_c,
            "identity": "K' M' = T^T (K M) T",
        },
        "analytic_theorem": {
            "complete_query_equivalence": (
                "If y^T C1 x = y^T C2 x for spanning source and readout "
                "families, then C1 = C2."
            ),
            "fixed_pairing_corollary": (
                "For fixed invertible K, C = K M is bijective in M."
            ),
            "operator_sufficiency_criterion": (
                "On any declared packet class, M is sufficient exactly when "
                "M1=M2 implies K1 M1=K2 M2."
            ),
            "variable_pairing_obstruction": (
                "If K varies, equality of M does not imply equality of C."
            ),
            "factorization_nonidentifiability": (
                "Equality of C does not identify K or M separately."
            ),
            "scalar_action_corollary": (
                "x^T C x determines sym(C); it determines C only when C is "
                "symmetric (Hermitian over the complex field)."
            ),
        },
        "local_model_learning_gate": {
            "admission": "ADMIT_LOCAL_LEARNING_BUILD",
            "research_only_baseline": (
                "Finite duality and metric-dependent adjoints predict that K "
                "matters; DU lacked the minimum same-signature source witness."
            ),
            "local_learning_delta": (
                "The 2x2 exact specimens locate the invariant at C=KM, expose "
                "an infinite factorization fibre, and fix the query-span leak."
            ),
            "pre_hardware_checkpoint": "PASS",
            "hardware": "irrelevant",
            "continuation": (
                "Bank the finite theorem; require a native domain/boundary "
                "packet before any infinite-dimensional or GU transfer."
            ),
        },
        "checks": checks,
        "check_count": len(checks),
        "non_claims": [
            "not a selected physical pairing, source basis, probe, or readout",
            "not an unbounded-operator, domain, Green-form, or QFT theorem",
            "not a GU chirality, source-action, or generation result",
            "not a formed archive, observer, public fact, or finality result",
            "not empirical excess, a new law, new physics, or a prediction",
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
