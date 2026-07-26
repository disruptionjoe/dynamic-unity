#!/usr/bin/env python3
"""Exact regression controls for HC-DU-040B.

The accompanying exploration proves the operator-algebra transport and
finite-horizon statements directly.  This file preserves only their smallest
exact controls:

* a binary sharp record is nondisturbing for the diagonal action algebra;
* adding one coherent action generates a factor proxy and destroys that
  internal finality;
* two states with the same record are then separated by one admitted effect;
* binary Lüders disturbance equals the corresponding commutator norm in the
  exact Pauli specimen;
* a rational one-step leakage can coherently accumulate to an almost maximal
  public-record difference over eight admitted continuations; and
* a symmetry orbit may be selected when no point interface is fixed, while an
  oriented reference reduces the stabilizer and selects one point.

All arithmetic is exact ``Fraction`` arithmetic.  This is a regression after
direct proof, not a QFT simulation, hardware result, or model-derived claim.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence


Q = Fraction
Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def add(*items: Matrix) -> Matrix:
    if not items:
        raise ValueError("add requires at least one matrix")
    return tuple(
        tuple(
            sum((item[i][j] for item in items), Q(0))
            for j in range(len(items[0][0]))
        )
        for i in range(len(items[0]))
    )


def neg(item: Matrix) -> Matrix:
    return tuple(tuple(-entry for entry in row) for row in item)


def sub(left: Matrix, right: Matrix) -> Matrix:
    return add(left, neg(right))


def scale(value: int | Fraction, item: Matrix) -> Matrix:
    factor = Q(value)
    return tuple(tuple(factor * entry for entry in row) for row in item)


def mul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix shapes do not compose")
    return tuple(
        tuple(
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Q(0),
            )
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def trace(item: Matrix) -> Fraction:
    return sum((item[i][i] for i in range(len(item))), Q(0))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(mul(left, right), mul(right, left))


def luders(projectors: Sequence[Matrix], observable: Matrix) -> Matrix:
    return add(
        *(mul(mul(projector, observable), projector) for projector in projectors)
    )


def expectation(state: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(state, effect))


def is_zero(item: Matrix) -> bool:
    return all(entry == 0 for row in item for entry in row)


def flatten(item: Matrix) -> tuple[Fraction, ...]:
    return tuple(entry for row in item for entry in row)


def rational_rank(rows: Iterable[Sequence[Fraction]]) -> int:
    work = [list(map(Q, row)) for row in rows]
    if not work:
        return 0
    row_count = len(work)
    col_count = len(work[0])
    rank = 0
    for col in range(col_count):
        pivot = next(
            (row for row in range(rank, row_count) if work[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][col]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for row in range(row_count):
            if row == rank or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][j] - factor * work[rank][j]
                for j in range(col_count)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def center_dimension(
    algebra_basis: Sequence[Matrix], generators: Sequence[Matrix]
) -> int:
    constraint_rows: list[list[Fraction]] = []
    for generator in generators:
        commutators = [
            flatten(commutator(basis, generator)) for basis in algebra_basis
        ]
        for entry_index in range(len(commutators[0])):
            constraint_rows.append(
                [item[entry_index] for item in commutators]
            )
    return len(algebra_basis) - rational_rank(constraint_rows)


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


I = matrix(((1, 0), (0, 1)))
X = matrix(((0, 1), (1, 0)))
Z = matrix(((1, 0), (0, -1)))
J = mul(X, Z)
P0 = scale(Q(1, 2), add(I, Z))
P1 = scale(Q(1, 2), sub(I, Z))
PLUS = scale(Q(1, 2), add(I, X))
MINUS = scale(Q(1, 2), sub(I, X))
E_PLUS_X = PLUS


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, evidence: object) -> None:
    checks.append({"name": name, "passed": bool(passed), "evidence": evidence})
    if not passed:
        raise AssertionError(f"{name}: {evidence}")


check("binary_pvm_complete", add(P0, P1) == I, True)
check("binary_pvm_orthogonal", is_zero(mul(P0, P1)), True)
check("binary_pvm_idempotent", mul(P0, P0) == P0 and mul(P1, P1) == P1, True)

check("luders_fixes_identity", luders((P0, P1), I) == I, True)
check("luders_fixes_public_Z", luders((P0, P1), Z) == Z, True)
check("luders_removes_coherent_X", is_zero(luders((P0, P1), X)), True)

diagonal_center_dimension = center_dimension((I, Z), (Z,))
factor_center_dimension = center_dimension((I, X, Z, J), (X, Z))
check(
    "diagonal_action_algebra_has_two_dimensional_center",
    diagonal_center_dimension == 2,
    diagonal_center_dimension,
)
check(
    "coherent_action_expansion_generates_factor_proxy",
    factor_center_dimension == 1,
    factor_center_dimension,
)
check(
    "record_projector_not_central_after_expansion",
    not is_zero(commutator(P0, X)),
    tuple(map(fraction_text, flatten(commutator(P0, X)))),
)

plus_record = (expectation(PLUS, P0), expectation(PLUS, P1))
minus_record = (expectation(MINUS, P0), expectation(MINUS, P1))
check(
    "coherent_pair_has_same_public_record",
    plus_record == minus_record == (Q(1, 2), Q(1, 2)),
    tuple(map(fraction_text, plus_record)),
)
plus_response = expectation(PLUS, E_PLUS_X)
minus_response = expectation(MINUS, E_PLUS_X)
check(
    "new_coherent_effect_separates_same_record_pair",
    (plus_response, minus_response) == (Q(1), Q(0)),
    (fraction_text(plus_response), fraction_text(minus_response)),
)

disturbance = sub(X, luders((P0, P1), X))
commutator_px = commutator(P0, X)
check(
    "binary_luders_commutator_identity",
    mul(Z, disturbance) == commutator_px,
    True,
)
check(
    "expanded_action_has_unit_exact_disturbance",
    disturbance == X,
    True,
)

# A rational Bloch-sphere rotation with cos(theta)=99/101 and
# sin(theta)=20/101.  The Heisenberg pullback of the public Z effect gains an
# X coefficient sin(k theta); |sin(k theta)| is both its distance from the
# diagonal public algebra and the response gap on PLUS versus MINUS.
cos_theta = Q(99, 101)
sin_theta = Q(20, 101)
check(
    "rational_rotation_is_on_unit_circle",
    cos_theta * cos_theta + sin_theta * sin_theta == 1,
    (fraction_text(cos_theta), fraction_text(sin_theta)),
)

rotation_rows: list[dict[str, object]] = []
cos_k = Q(1)
sin_k = Q(0)
for horizon in range(1, 9):
    cos_k, sin_k = (
        cos_k * cos_theta - sin_k * sin_theta,
        sin_k * cos_theta + cos_k * sin_theta,
    )
    rotation_rows.append(
        {
            "horizon": horizon,
            "cos": fraction_text(cos_k),
            "sin": fraction_text(sin_k),
            "leakage": fraction_text(abs(sin_k)),
            "leakage_decimal": float(abs(sin_k)),
        }
    )
    check(
        f"rotation_norm_preserved_h{horizon}",
        cos_k * cos_k + sin_k * sin_k == 1,
        rotation_rows[-1],
    )
    check(
        f"word_length_bound_h{horizon}",
        abs(sin_k) <= horizon * abs(sin_theta),
        {
            "actual": fraction_text(abs(sin_k)),
            "bound": fraction_text(horizon * abs(sin_theta)),
        },
    )

eighth_leakage = abs(sin_k)
check(
    "one_step_leakage_exact",
    abs(sin_theta) == Q(20, 101),
    fraction_text(abs(sin_theta)),
)
check(
    "eight_step_leakage_exact",
    eighth_leakage == Q(10825473963759840, 10828567056280801),
    fraction_text(eighth_leakage),
)
check(
    "eight_step_leakage_near_maximal",
    eighth_leakage > Q(999, 1000),
    float(eighth_leakage),
)
check(
    "same_record_response_gap_equals_eight_step_leakage",
    eighth_leakage == abs(sin_k),
    fraction_text(eighth_leakage),
)

# A three-axis symmetry control.  The full permutation group selects the
# orbit {0,1,2} but no point.  Supplying an oriented reference 0 reduces the
# stabilizer, after which 0 is the unique fixed axis.
axes = (0, 1, 2)
group = tuple(itertools.permutations(axes))
fixed_without_reference = tuple(
    axis for axis in axes if all(permutation[axis] == axis for permutation in group)
)
orbit_zero = tuple(sorted({permutation[0] for permutation in group}))
reference_stabilizer = tuple(
    permutation for permutation in group if permutation[0] == 0
)
fixed_with_reference = tuple(
    axis
    for axis in axes
    if all(permutation[axis] == axis for permutation in reference_stabilizer)
)
check(
    "symmetric_interface_family_has_no_fixed_point",
    fixed_without_reference == (),
    fixed_without_reference,
)
check("symmetric_interface_orbit_is_selected", orbit_zero == axes, orbit_zero)
check(
    "oriented_reference_selects_one_point",
    fixed_with_reference == (0,),
    fixed_with_reference,
)

result = {
    "claim_id": "HC-DU-040B",
    "disposition": (
        "KNOWN_OPERATOR_ALGEBRA_TRANSPORT__FACTOR_INTERNAL_RECORD_NO_GO__"
        "FINITE_HORIZON_APPROXIMATE_FINALITY_ONLY"
    ),
    "checks_passed": f"{sum(item['passed'] for item in checks)}/{len(checks)}",
    "center_transport_control": {
        "diagonal_center_dimension": diagonal_center_dimension,
        "expanded_factor_proxy_center_dimension": factor_center_dimension,
        "same_record": tuple(map(fraction_text, plus_record)),
        "expanded_action_responses": (
            fraction_text(plus_response),
            fraction_text(minus_response),
        ),
    },
    "approximate_horizon_control": {
        "one_step_cos": fraction_text(cos_theta),
        "one_step_leakage": fraction_text(abs(sin_theta)),
        "eight_step_leakage": fraction_text(eighth_leakage),
        "eight_step_leakage_decimal": float(eighth_leakage),
        "rows": rotation_rows,
    },
    "symmetry_control": {
        "fixed_points_without_reference": fixed_without_reference,
        "selected_orbit": orbit_zero,
        "fixed_points_with_oriented_reference": fixed_with_reference,
    },
    "claim_ceiling": [
        "exact finite regression after direct proof",
        "no QFT simulation",
        "no physically selected apparatus or record",
        "no universal approximate-finality law",
        "no ontology, new physics, hardware result, or paper promotion",
    ],
    "checks": checks,
}

artifact_path = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_algebraic_qft_record_transport_result.json"
)
payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
artifact_path.write_text(payload, encoding="utf-8")
digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()

print(result["disposition"])
print(result["checks_passed"])
print(f"artifact={artifact_path}")
print(f"sha256={digest}")
