#!/usr/bin/env python3
"""Exact finite regression for HC-DU-091.

The analytic result lives in:
  explorations/eth-actuality-algebra-naturality-restriction-counterexample-and-instrument-boundary-2026-07-28.md

This is a proportional proof-boundary artifact added after the algebraic
argument. It is not a simulation, event detector, collapse experiment,
ontology test, or physical co-filtration selector. It verifies:

* covariance of the center-of-centralizer construction under one exact
  state-preserving star-automorphism;
* failure of restriction/co-filtration naturality in M_2(C);
* a nontracial control showing the failure is not only tracial degeneracy;
* incompatibility of two symmetry-related atomic event algebras; and
* equality of the fixed finite ETH conditioning step with the matched
  Lüders projective instrument.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_eth_actuality_algebra_naturality_result.json"
)
Q = Fraction
Gaussian = tuple[Fraction, Fraction]
Matrix = tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]


def g(real: int | Fraction = 0, imag: int | Fraction = 0) -> Gaussian:
    return Q(real), Q(imag)


ZERO = g()
ONE = g(1)


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_sub(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] - right[0], left[1] - right[1]


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def g_div(left: Gaussian, right: Gaussian) -> Gaussian:
    denominator = right[0] * right[0] + right[1] * right[1]
    if denominator == 0:
        raise ZeroDivisionError
    return (
        (left[0] * right[0] + left[1] * right[1]) / denominator,
        (left[1] * right[0] - left[0] * right[1]) / denominator,
    )


def g_neg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def m_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def m_sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_sub(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def m_scale(scalar: Gaussian, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(g_mul(scalar, matrix[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def m_mul(*matrices: Matrix) -> Matrix:
    result = matrices[0]
    for right in matrices[1:]:
        result = tuple(
            tuple(
                g_add(
                    g_mul(result[row][0], right[0][column]),
                    g_mul(result[row][1], right[1][column]),
                )
                for column in range(2)
            )
            for row in range(2)
        )  # type: ignore[assignment]
    return result


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return m_sub(m_mul(left, right), m_mul(right, left))


def trace(matrix: Matrix) -> Gaussian:
    return g_add(matrix[0][0], matrix[1][1])


def is_zero_matrix(matrix: Matrix) -> bool:
    return all(entry == ZERO for row in matrix for entry in row)


I: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, g(0, -1)), (g(0, 1), ZERO))
Z: Matrix = ((ONE, ZERO), (ZERO, g(-1)))
H0: Matrix = ((ONE, ONE), (ONE, g(-1)))

A_BASIS = (I, X, Y, Z)
BZ_BASIS = (I, Z)
BX_BASIS = (I, X)


def gaussian_rank(rows: list[list[Gaussian]]) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                candidate
                for candidate in range(pivot_row, row_count)
                if matrix[candidate][column] != ZERO
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [
            g_div(value, pivot_value) for value in matrix[pivot_row]
        ]
        for candidate in range(row_count):
            if candidate == pivot_row:
                continue
            factor = matrix[candidate][column]
            if factor == ZERO:
                continue
            matrix[candidate] = [
                g_sub(value, g_mul(factor, pivot_value))
                for value, pivot_value in zip(
                    matrix[candidate], matrix[pivot_row], strict=True
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def center_dimension(basis: tuple[Matrix, ...]) -> int:
    equations: list[list[Gaussian]] = []
    for right in basis:
        commutators = [commutator(left, right) for left in basis]
        for row in range(2):
            for column in range(2):
                equations.append(
                    [matrix[row][column] for matrix in commutators]
                )
    return len(basis) - gaussian_rank(equations)


State = Callable[[Matrix], Gaussian]


def density_state(density: Matrix) -> State:
    return lambda matrix: trace(m_mul(density, matrix))


TRACE_STATE = density_state(m_scale(g(Q(1, 2)), I))
BIASED_STATE = density_state(
    ((g(Q(3, 4)), ZERO), (ZERO, g(Q(1, 4))))
)


def centralizer_dimension(
    basis: tuple[Matrix, ...],
    state: State,
) -> int:
    equations = [
        [state(commutator(left, right)) for left in basis]
        for right in basis
    ]
    return len(basis) - gaussian_rank(equations)


def alpha_hadamard(matrix: Matrix) -> Matrix:
    # H = H0/sqrt(2), so H M H^\dagger = H0 M H0 / 2 exactly.
    return m_scale(g(Q(1, 2)), m_mul(H0, matrix, H0))


def projector(pauli: Matrix, sign: int) -> Matrix:
    return m_scale(
        g(Q(1, 2)),
        m_add(I, m_scale(g(sign), pauli)),
    )


def probability(state: State, event: Matrix) -> Gaussian:
    return state(event)


def joint_luders_probability(
    density: Matrix,
    first: Matrix,
    second: Matrix,
) -> Gaussian:
    return trace(m_mul(second, first, density, first, second))


checks: list[dict[str, Any]] = []


def check(name: str, condition: bool, detail: Any) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(part, Fraction) for part in value)
    ):
        real, imag = value
        if imag == 0:
            return f"{real.numerator}/{real.denominator}"
        return {
            "real": f"{real.numerator}/{real.denominator}",
            "imag": f"{imag.numerator}/{imag.denominator}",
        }
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


# ---------------------------------------------------------------------------
# Center-of-centralizer and restriction controls.
# ---------------------------------------------------------------------------

check(
    "tracial_centralizer_is_full_m2",
    centralizer_dimension(A_BASIS, TRACE_STATE) == 4,
    {"centralizer_complex_dimension": centralizer_dimension(A_BASIS, TRACE_STATE)},
)

check(
    "full_m2_actuality_algebra_is_scalar",
    center_dimension(A_BASIS) == 1,
    {"actuality_algebra_complex_dimension": center_dimension(A_BASIS)},
)

check(
    "restricted_z_algebra_is_abelian_and_actual",
    all(is_zero_matrix(commutator(left, right)) for left in BZ_BASIS for right in BZ_BASIS)
    and center_dimension(BZ_BASIS) == 2,
    {"actuality_algebra_complex_dimension": center_dimension(BZ_BASIS)},
)

check(
    "restricted_x_algebra_is_abelian_and_actual",
    all(is_zero_matrix(commutator(left, right)) for left in BX_BASIS for right in BX_BASIS)
    and center_dimension(BX_BASIS) == 2,
    {"actuality_algebra_complex_dimension": center_dimension(BX_BASIS)},
)

check(
    "restriction_naturality_fails",
    center_dimension(BZ_BASIS) == 2 > 1 == center_dimension(A_BASIS),
    {
        "Z_tau_restricted_Bz_dimension": center_dimension(BZ_BASIS),
        "Bz_intersection_Z_tau_A_dimension": 1,
    },
)

check(
    "nontracial_control_has_diagonal_full_actuality_algebra",
    centralizer_dimension(A_BASIS, BIASED_STATE) == 2
    and all(
        BIASED_STATE(commutator(left, right)) == ZERO
        for left in BZ_BASIS
        for right in A_BASIS
    ),
    {
        "full_centralizer_complex_dimension": centralizer_dimension(
            A_BASIS, BIASED_STATE
        ),
        "identified_centralizer_basis": ["I", "Z"],
    },
)

check(
    "nontracial_restriction_rotates_actuality_algebra",
    centralizer_dimension(BX_BASIS, BIASED_STATE) == 2
    and center_dimension(BX_BASIS) == 2,
    {
        "full_actuality_algebra": "span(I,Z)",
        "restricted_actuality_algebra": "span(I,X)",
        "intersection": "span(I)",
    },
)


# ---------------------------------------------------------------------------
# Representation covariance, symmetry orbit, and atomic event controls.
# ---------------------------------------------------------------------------

check(
    "hadamard_is_exact_star_automorphism_control",
    alpha_hadamard(I) == I
    and alpha_hadamard(X) == Z
    and alpha_hadamard(Z) == X
    and alpha_hadamard(Y) == m_scale(g(-1), Y),
    {
        "alpha_I": alpha_hadamard(I),
        "alpha_X": alpha_hadamard(X),
        "alpha_Y": alpha_hadamard(Y),
        "alpha_Z": alpha_hadamard(Z),
    },
)

check(
    "hadamard_preserves_tracial_state",
    all(TRACE_STATE(alpha_hadamard(matrix)) == TRACE_STATE(matrix) for matrix in A_BASIS),
    {
        "before": [TRACE_STATE(matrix) for matrix in A_BASIS],
        "after": [TRACE_STATE(alpha_hadamard(matrix)) for matrix in A_BASIS],
    },
)

check(
    "representation_covariance_maps_actuality_algebras",
    alpha_hadamard(BZ_BASIS[0]) == BX_BASIS[0]
    and alpha_hadamard(BZ_BASIS[1]) == BX_BASIS[1],
    {
        "source": "span(I,Z)",
        "image": "span(I,X)",
    },
)

check(
    "symmetry_related_event_algebras_are_incompatible",
    not is_zero_matrix(commutator(X, Z)),
    {"commutator_X_Z": commutator(X, Z)},
)

PZ_PLUS = projector(Z, 1)
PZ_MINUS = projector(Z, -1)
PX_PLUS = projector(X, 1)
PX_MINUS = projector(X, -1)

for label, event in (
    ("Pz_plus", PZ_PLUS),
    ("Pz_minus", PZ_MINUS),
    ("Px_plus", PX_PLUS),
    ("Px_minus", PX_MINUS),
):
    check(
        f"{label}_is_rank_one_projection",
        m_mul(event, event) == event and trace(event) == ONE,
        {"projection": event, "trace": trace(event)},
    )

check(
    "atomic_event_pairs_partition_identity",
    m_add(PZ_PLUS, PZ_MINUS) == I
    and is_zero_matrix(m_mul(PZ_PLUS, PZ_MINUS))
    and m_add(PX_PLUS, PX_MINUS) == I
    and is_zero_matrix(m_mul(PX_PLUS, PX_MINUS)),
    {
        "z_partition": ["Pz_plus", "Pz_minus"],
        "x_partition": ["Px_plus", "Px_minus"],
    },
)


# ---------------------------------------------------------------------------
# Matched Lüders-instrument boundary.
# ---------------------------------------------------------------------------

TRACE_DENSITY = m_scale(g(Q(1, 2)), I)

check(
    "born_weights_are_half",
    all(
        probability(TRACE_STATE, event) == g(Q(1, 2))
        for event in (PZ_PLUS, PZ_MINUS, PX_PLUS, PX_MINUS)
    ),
    {
        "weights": [
            probability(TRACE_STATE, event)
            for event in (PZ_PLUS, PZ_MINUS, PX_PLUS, PX_MINUS)
        ]
    },
)

check(
    "eth_conditioned_state_equals_luders_posterior",
    all(
        m_scale(
            g(2),
            m_mul(event, TRACE_DENSITY, event),
        )
        == event
        for event in (PZ_PLUS, PZ_MINUS, PX_PLUS, PX_MINUS)
    ),
    {"posterior_rule": "P rho P / Tr(rho P)"},
)

sequential_weights = [
    joint_luders_probability(TRACE_DENSITY, first, second)
    for first in (PZ_PLUS, PZ_MINUS)
    for second in (PX_PLUS, PX_MINUS)
]

check(
    "matched_sequential_instrument_weights_are_quarters",
    sequential_weights == [g(Q(1, 4))] * 4,
    {"sequential_weights": sequential_weights},
)


result = {
    "claim_id": "HC-DU-091",
    "fixture": {
        "ambient_algebra": "M2(C)",
        "dynamics": "identity",
        "states": {
            "symmetric": "tau=Tr/2",
            "nontracial_control": "rho=diag(3/4,1/4)",
        },
        "cofiltration_refinements": [
            ["M2(C)", "span(I,Z)", "C I"],
            ["M2(C)", "span(I,X)", "C I"],
        ],
        "shared_coarse_endpoints": ["M2(C)", "C I"],
    },
    "disposition": {
        "representation": "REPRESENTATION_NATURALITY",
        "restriction": "ALGEBRA_RELATIVE_EVENT_AMBIGUITY",
        "cofiltration": "NO_PHYSICAL_COFILTRATION_SELECTOR",
        "fixed_collapse_step": "STANDARD_INSTRUMENT_ABSORPTION",
        "event_to_record_continuation": "STOP_LOWER_SELECTOR_FAILED",
    },
    "checks": checks,
    "summary": {
        "passed": sum(1 for item in checks if item["passed"]),
        "total": len(checks),
    },
}

ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
ARTIFACT.write_text(
    json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

print(
    "du_eth_actuality_algebra_naturality_probe: "
    f"PASS ({result['summary']['passed']}/{result['summary']['total']})"
)
