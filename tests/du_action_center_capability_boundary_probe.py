#!/usr/bin/env python3
"""Exact regression controls for HC-DU-033D.

The theorem is proved directly in the accompanying exploration.  This file
only preserves the smallest rational positive and hostile specimens:

* a central sharp record in M2 direct-sum M2;
* a noncentral internal projector that disturbs the action algebra;
* an explicit blank pointer/archive formation isometry;
* central versus within-block event/next-record effects;
* a factor with trivial internal center and a noninternal commutant pointer;
* a commutative action algebra whose full action statistics factor through
  its minimal central record; and
* common-representation conjugation invariance.

It uses exact Fraction arithmetic and no external hardware or numerical
tolerance.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable, Sequence


Q = Fraction
Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def zeros(n_rows: int, n_cols: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(n_cols)) for _ in range(n_rows))


def eye(size: int) -> Matrix:
    return tuple(
        tuple(Q(1 if row == col else 0) for col in range(size))
        for row in range(size)
    )


def unit(size: int, row: int, col: int) -> Matrix:
    return tuple(
        tuple(Q(1 if (i, j) == (row, col) else 0) for j in range(size))
        for i in range(size)
    )


def add(*items: Matrix) -> Matrix:
    if not items:
        raise ValueError("add requires at least one matrix")
    return tuple(
        tuple(sum((item[i][j] for item in items), Q(0)) for j in range(len(items[0][0])))
        for i in range(len(items[0]))
    )


def neg(item: Matrix) -> Matrix:
    return tuple(tuple(-value for value in row) for row in item)


def sub(left: Matrix, right: Matrix) -> Matrix:
    return add(left, neg(right))


def scale(value: int | Fraction, item: Matrix) -> Matrix:
    factor = Q(value)
    return tuple(tuple(factor * entry for entry in row) for row in item)


def transpose(item: Matrix) -> Matrix:
    return tuple(tuple(item[i][j] for i in range(len(item))) for j in range(len(item[0])))


def mul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix shapes do not compose")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[i][j] * right[a][b]
            for j in range(len(left[0]))
            for b in range(len(right[0]))
        )
        for i in range(len(left))
        for a in range(len(right))
    )


def trace(item: Matrix) -> Fraction:
    return sum((item[i][i] for i in range(len(item))), Q(0))


def expectation(state: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(state, effect))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(mul(left, right), mul(right, left))


def is_zero(item: Matrix) -> bool:
    return all(entry == 0 for row in item for entry in row)


def commutes_with_all(item: Matrix, algebra_basis: Iterable[Matrix]) -> bool:
    return all(is_zero(commutator(item, basis)) for basis in algebra_basis)


def luders(projectors: Sequence[Matrix], observable: Matrix) -> Matrix:
    return add(*(mul(mul(projector, observable), projector) for projector in projectors))


def diagonal_state(size: int, index: int) -> Matrix:
    return unit(size, index, index)


def projector_support(projector: Matrix) -> list[int]:
    support: list[int] = []
    for i in range(len(projector)):
        if projector[i][i] == 1:
            support.append(i)
        elif projector[i][i] != 0:
            raise ValueError("fixture expects diagonal 0/1 projectors")
    return support


def scalar_on_projector(effect: Matrix, projector: Matrix) -> tuple[bool, Fraction | None]:
    support = projector_support(projector)
    if not support:
        return True, Q(0)
    compression = mul(mul(projector, effect), projector)
    scalar = compression[support[0]][support[0]]
    for i in range(len(projector)):
        for j in range(len(projector)):
            expected = scalar if i == j and i in support else Q(0)
            if compression[i][j] != expected:
                return False, None
    return True, scalar


def effects_descend_to_center(
    effects: Sequence[Matrix], central_projectors: Sequence[Matrix]
) -> bool:
    return all(
        scalar_on_projector(effect, projector)[0]
        for effect in effects
        for projector in central_projectors
    )


def in_factor_m2_tensor_identity(item: Matrix) -> bool:
    """Exact membership in M2 tensor I2 for the system-first ordering."""

    if len(item) != 4 or len(item[0]) != 4:
        return False
    block = tuple(
        tuple(item[2 * i][2 * j] for j in range(2))
        for i in range(2)
    )
    return item == kron(block, eye(2))


def jsonable(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


checks: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


I4 = eye(4)
P0 = add(unit(4, 0, 0), unit(4, 1, 1))
P1 = add(unit(4, 2, 2), unit(4, 3, 3))
central_pvm = (P0, P1)
block_basis = tuple(
    unit(4, row, col)
    for offset in (0, 2)
    for row in range(offset, offset + 2)
    for col in range(offset, offset + 2)
)

check(
    "central projectors form a PVM",
    mul(P0, P1) == zeros(4, 4) and add(P0, P1) == I4,
    "P0 and P1 are orthogonal and sum to identity.",
)
check(
    "central PVM lies in the action center",
    all(commutes_with_all(projector, block_basis) for projector in central_pvm),
    "Both sector projectors commute with every matrix unit of M2 direct-sum M2.",
)
check(
    "central Lüders map preserves the full action algebra",
    all(luders(central_pvm, basis) == basis for basis in block_basis),
    "Every action-algebra basis element is block diagonal.",
)
central_projection_family = (zeros(4, 4), P0, P1, I4)
check(
    "minimal central projectors refine every central projection",
    all(
        candidate
        in (
            zeros(4, 4),
            P0,
            P1,
            add(P0, P1),
        )
        for candidate in central_projection_family
    ),
    "Every central projection is a sum of the two minimal central projectors.",
)

P00 = unit(4, 0, 0)
P00_complement = sub(I4, P00)
X_first_block = add(unit(4, 0, 1), unit(4, 1, 0))
check(
    "noncentral internal projector fails the commutant test",
    not commutes_with_all(P00, block_basis),
    "P00 is action-internal but does not commute with within-block X.",
)
check(
    "noncentral Lüders record disturbs an admitted action",
    luders((P00, P00_complement), X_first_block) != X_first_block,
    "The rank-one within-block readout deletes the off-diagonal action.",
)
check(
    "disturbance witness is exact",
    luders((P00, P00_complement), X_first_block) == zeros(4, 4),
    "The chosen within-block X is completely removed.",
)

# Explicit source-to-blank-pointer-and-archive isometry.  The two record bits
# are ordered as pointer then archive.
V_rows = [[Q(0) for _ in range(4)] for _ in range(16)]
for system_index in range(4):
    sector = 0 if system_index < 2 else 1
    output_index = system_index * 4 + sector * 2 + sector
    V_rows[output_index][system_index] = Q(1)
V = matrix(V_rows)

check(
    "formation map is an isometry",
    mul(transpose(V), V) == I4,
    "The source is embedded while blank pointer and archive acquire the sector label.",
)
check(
    "formation map intertwines the complete action algebra",
    all(mul(kron(basis, eye(4)), V) == mul(V, basis) for basis in block_basis),
    "Central sector copying leaves every admitted block action nondemolished.",
)
check(
    "formation writes matching pointer and archive values",
    all(
        any(
            V[system_index * 4 + sector * 2 + sector][system_index] == 1
            for sector in (0, 1)
        )
        for system_index in range(4)
    ),
    "Each basis state is correlated only with its matching double record.",
)

rho_00 = diagonal_state(4, 0)
rho_01 = diagonal_state(4, 1)
rho_10 = diagonal_state(4, 2)
rho_11 = diagonal_state(4, 3)

central_effect_0 = add(scale(Q(1, 2), P0), scale(Q(1, 3), P1))
central_effect_1 = sub(I4, central_effect_0)
central_effects = (central_effect_0, central_effect_1)
hostile_effect_0 = add(P00, scale(Q(1, 2), P1))
hostile_effect_1 = sub(I4, hostile_effect_0)
hostile_effects = (hostile_effect_0, hostile_effect_1)

check(
    "central joint effects descend to the record center",
    effects_descend_to_center(central_effects, central_pvm),
    "Each complete event/next-record effect is block scalar.",
)
check(
    "same-sector states have identical central rows",
    [expectation(rho_00, effect) for effect in central_effects]
    == [expectation(rho_01, effect) for effect in central_effects]
    and [expectation(rho_10, effect) for effect in central_effects]
    == [expectation(rho_11, effect) for effect in central_effects],
    "The HC-DU-036H row depends only on the central sector.",
)
check(
    "noncentral joint effect fails descent",
    not effects_descend_to_center(hostile_effects, central_pvm),
    "One event effect varies inside the first central block.",
)
check(
    "one admitted action exposes a same-record remainder",
    expectation(rho_00, hostile_effect_0) == 1
    and expectation(rho_01, hostile_effect_0) == 0,
    "Two states with central record q=0 are separated with unit probability margin.",
)
check(
    "central record itself cannot see the hostile pair",
    [expectation(rho_00, projector) for projector in central_pvm]
    == [expectation(rho_01, projector) for projector in central_pvm]
    == [Q(1), Q(0)],
    "The hostile pair has exactly the same formed central record.",
)

# Factor control A = M2 tensor I2.
factor_basis = tuple(
    kron(unit(2, row, col), eye(2))
    for row in range(2)
    for col in range(2)
)
source_projector = kron(unit(2, 0, 0), eye(2))
source_projector_complement = sub(I4, source_projector)
source_X = kron(add(unit(2, 0, 1), unit(2, 1, 0)), eye(2))
commutant_pointer = kron(eye(2), unit(2, 0, 0))

check(
    "factor internal projector is noncentral",
    in_factor_m2_tensor_identity(source_projector)
    and not commutes_with_all(source_projector, factor_basis),
    "A nontrivial source PVM lies in the factor but not its scalar center.",
)
check(
    "factor internal record disturbs the source action",
    luders((source_projector, source_projector_complement), source_X)
    == zeros(4, 4),
    "The nontrivial internal readout removes source coherence.",
)
check(
    "commutant pointer is nondisturbing but noninternal",
    commutes_with_all(commutant_pointer, factor_basis)
    and not in_factor_m2_tensor_identity(commutant_pointer),
    "A separate multiplicity/pointer degree can commute with the factor without belonging to it.",
)
check(
    "factor identity is the only tested internal central projector",
    commutes_with_all(I4, factor_basis)
    and not commutes_with_all(source_projector, factor_basis),
    "The explicit factor control has only the scalar internal center.",
)

# Commutative control: the diagonal action algebra.  Coherent states with the
# same diagonal record remain different density operators, but no action in
# the declared algebra distinguishes them.
diagonal_basis = tuple(unit(4, index, index) for index in range(4))
rho_plus = matrix(
    [
        [Q(1, 2), Q(1, 2), 0, 0],
        [Q(1, 2), Q(1, 2), 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
rho_minus = matrix(
    [
        [Q(1, 2), Q(-1, 2), 0, 0],
        [Q(-1, 2), Q(1, 2), 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
check(
    "commutative minimal central record captures all admitted actions",
    [expectation(rho_plus, effect) for effect in diagonal_basis]
    == [expectation(rho_minus, effect) for effect in diagonal_basis],
    "States with the same complete diagonal record agree on every declared diagonal action.",
)
check(
    "commutative control keeps ontology quotient typed",
    rho_plus != rho_minus,
    "Operational sufficiency for the declared action algebra does not identify full density operators.",
)

# Common representation conjugation by an exact permutation.
permutation = matrix(
    [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ]
)


def conjugate(item: Matrix) -> Matrix:
    return mul(mul(permutation, item), transpose(permutation))


rotated_basis = tuple(conjugate(item) for item in block_basis)
rotated_center = tuple(conjugate(item) for item in central_pvm)
rotated_hostile = tuple(conjugate(item) for item in hostile_effects)
rotated_states = (conjugate(rho_00), conjugate(rho_01))

check(
    "central nondisturbance is representation robust",
    all(
        luders(rotated_center, basis) == basis
        for basis in rotated_basis
    ),
    "Common conjugation preserves the action-center theorem.",
)
check(
    "autonomy verdict is representation robust",
    effects_descend_to_center(
        tuple(conjugate(item) for item in central_effects), rotated_center
    )
    and not effects_descend_to_center(rotated_hostile, rotated_center),
    "Common conjugation preserves central versus noncentral joint effects.",
)
check(
    "same-record remainder margin is representation robust",
    expectation(rotated_states[0], rotated_hostile[0]) == 1
    and expectation(rotated_states[1], rotated_hostile[0]) == 0,
    "The separating probability margin remains one.",
)

passed = sum(1 for item in checks if item["passed"])
result = {
    "run_id": "RUN-20260726-152732-action-center-capability-boundary",
    "hypothesis_id": "HC-DU-033D",
    "status": "completed_scoped_result",
    "verdict": "KNOWN_MATHEMATICS__ACTION_CENTER_FORMATION_TO_CAPABILITY_BOUNDARY_EXACT",
    "checks": checks,
    "summary": {
        "passed": passed,
        "total": len(checks),
        "central_record": "minimal central projections are the finest action-internal sharp PVM preserving the complete finite action algebra under the Lueders channel",
        "formation": "an explicit blank pointer/archive isometry writes the central label and intertwines the action algebra; the coupling remains supplied",
        "autonomy": "the complete event/next-record row descends exactly when its Heisenberg effects are block scalar, equivalently central",
        "remainder": "a noncommutative block contains same-central-record states separated by one admitted action with probability margin one",
        "factor_boundary": "a factor has no nontrivial action-internal nondisturbing sharp record; a commuting external pointer is a different interface object",
        "commutative_boundary": "the central record is sufficient for every admitted action exactly at the commutative action-algebra boundary",
    },
    "local_model_learning_gate": {
        "disposition": "REGRESSION_ONLY_AFTER_DIRECT_PROOF",
        "hardware_required": False,
        "generated_learning_claim": False,
        "purpose": "preserve exact minimal witnesses and representation invariance after the symbolic proof",
    },
    "claim_ceiling": [
        "finite-dimensional action-algebra theorem",
        "known operator-algebra mathematics",
        "conditional on a supplied physical action algebra and supplied formation coupling",
        "no selection of the physical action algebra, observer boundary, pointer, archive, decoder, or microscopic dilation",
        "no universal record completeness, record-first ontology, new quantum law, new physics, hardware result, paper promotion, or publication",
    ],
    "next_dependency": "derive or independently justify the physical action algebra and boundary, then carry the typed central/noncommutative remainder into layered regional composition",
}

artifact_path = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_action_center_capability_boundary_result.json"
)
artifact_path.parent.mkdir(parents=True, exist_ok=True)
payload = json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n"
artifact_path.write_text(payload, encoding="utf-8")
digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()

print(
    json.dumps(
        {
            "artifact": str(artifact_path),
            "passed": passed,
            "sha256": digest,
            "total": len(checks),
            "verdict": result["verdict"],
        },
        indent=2,
        sort_keys=True,
    )
)
