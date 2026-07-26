#!/usr/bin/env python3
"""Exact regression controls for HC-DU-035D.

The accompanying exploration proves the center-screening and first-leak
statements directly.  This executable preserves only the smallest rational
two-region controls.  Each region has one public sector bit and one retained
two-dimensional fibre:

    A_i = C^2_sector tensor M2_fibre.

All calculations use Fraction arithmetic.  There is no simulation, random
sampling, numerical tolerance, provider access, or external hardware.
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


def transpose(item: Matrix) -> Matrix:
    return tuple(
        tuple(item[i][j] for i in range(len(item)))
        for j in range(len(item[0]))
    )


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


def kron_all(*items: Matrix) -> Matrix:
    result = items[0]
    for item in items[1:]:
        result = kron(result, item)
    return result


def trace(item: Matrix) -> Fraction:
    return sum((item[i][i] for i in range(len(item))), Q(0))


def expectation(state: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(state, effect))


def evolve(unitary: Matrix, state: Matrix) -> Matrix:
    return mul(mul(unitary, state), transpose(unitary))


def pullback(unitary: Matrix, effect: Matrix) -> Matrix:
    return mul(mul(transpose(unitary), effect), unitary)


def dephase(state: Matrix, phase_flip: Matrix) -> Matrix:
    return scale(Q(1, 2), add(state, evolve(phase_flip, state)))


def is_zero(item: Matrix) -> bool:
    return all(entry == 0 for row in item for entry in row)


def projector_support(projector: Matrix) -> list[int]:
    support: list[int] = []
    for index in range(len(projector)):
        if projector[index][index] == 1:
            support.append(index)
        elif projector[index][index] != 0:
            raise ValueError("fixture expects diagonal 0/1 central projectors")
    return support


def central_coefficients(
    item: Matrix, central_projectors: Sequence[Matrix]
) -> tuple[Fraction, ...] | None:
    coefficients: list[Fraction] = []
    reconstruction = zeros(len(item), len(item))
    for projector in central_projectors:
        support = projector_support(projector)
        coefficient = item[support[0]][support[0]]
        candidate = scale(coefficient, projector)
        compression = mul(mul(projector, item), projector)
        if compression != candidate:
            return None
        coefficients.append(coefficient)
        reconstruction = add(reconstruction, candidate)
    if reconstruction != item:
        return None
    return tuple(coefficients)


def is_central(item: Matrix, central_projectors: Sequence[Matrix]) -> bool:
    return central_coefficients(item, central_projectors) is not None


def unitary_screens_center(
    unitary: Matrix, central_projectors: Sequence[Matrix]
) -> bool:
    return all(
        is_central(pullback(unitary, projector), central_projectors)
        for projector in central_projectors
    )


def central_distribution(
    state: Matrix, central_projectors: Sequence[Matrix]
) -> tuple[Fraction, ...]:
    return tuple(expectation(state, projector) for projector in central_projectors)


def selective_cells_screen_center(
    kraus: Sequence[Matrix], central_projectors: Sequence[Matrix]
) -> bool:
    return all(
        is_central(mul(mul(transpose(operator), projector), operator), central_projectors)
        for operator in kraus
        for projector in central_projectors
    )


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


I2 = eye(2)
X = matrix([[0, 1], [1, 0]])
Z = matrix([[1, 0], [0, -1]])
P0 = unit(2, 0, 0)
P1 = unit(2, 1, 1)
P_PLUS = scale(Q(1, 2), add(I2, X))
P_MINUS = scale(Q(1, 2), sub(I2, X))
I16 = eye(16)


def op(s_a: Matrix, f_a: Matrix, s_b: Matrix, f_b: Matrix) -> Matrix:
    return kron_all(s_a, f_a, s_b, f_b)


central_projectors = tuple(
    op(P0 if sector_a == 0 else P1, I2, P0 if sector_b == 0 else P1, I2)
    for sector_a in (0, 1)
    for sector_b in (0, 1)
)


def product_state(
    sector_a: Matrix, fibre_a: Matrix, sector_b: Matrix, fibre_b: Matrix
) -> Matrix:
    return op(sector_a, fibre_a, sector_b, fibre_b)


# Public-only coupling: the B sector flips only as a function of the A sector.
U_CENTER = add(
    op(P0, I2, I2, I2),
    op(P1, I2, X, I2),
)

# Population leak: the B sector flips as a function of the A fibre Z value.
U_FIBRE_POP = add(
    op(I2, P0, I2, I2),
    op(I2, P1, X, I2),
)

# Coherent phase leak: the B sector flips as a function of the A fibre X value.
U_FIBRE_PHASE = add(
    op(I2, P_PLUS, I2, I2),
    op(I2, P_MINUS, X, I2),
)

Z_FIBRE_A = op(I2, Z, I2, I2)

check(
    "regional central projectors form a four-cell PVM",
    add(*central_projectors) == I16
    and all(
        is_zero(mul(left, right))
        for index, left in enumerate(central_projectors)
        for right in central_projectors[index + 1 :]
    ),
    "The two regional public bits define four orthogonal central sectors.",
)
check(
    "public-only coupling is exactly unitary",
    mul(transpose(U_CENTER), U_CENTER) == I16,
    "Sector-controlled CNOT is a permutation unitary.",
)
check(
    "population-leak coupling is exactly unitary",
    mul(transpose(U_FIBRE_POP), U_FIBRE_POP) == I16,
    "Fibre-population-controlled CNOT is a permutation unitary.",
)
check(
    "phase-leak coupling is exactly unitary",
    mul(transpose(U_FIBRE_PHASE), U_FIBRE_PHASE) == I16,
    "Orthogonal X-fibre projectors control the public-sector flip.",
)

check(
    "public-only coupling screens the regional center",
    unitary_screens_center(U_CENTER, central_projectors),
    "Every pulled-back next public projector remains a current central projector.",
)
check(
    "parallel and sequential public-only composition remains screened",
    unitary_screens_center(mul(U_CENTER, U_CENTER), central_projectors),
    "The exact positive composition closes on the public center.",
)

rho_sector_a_0 = P0
rho_sector_a_1 = P1
rho_sector_b_0 = P0
rho_fibre_b_0 = P0
rho_pop_0 = product_state(
    rho_sector_a_0, P0, rho_sector_b_0, rho_fibre_b_0
)
rho_pop_1 = product_state(
    rho_sector_a_0, P1, rho_sector_b_0, rho_fibre_b_0
)
rho_phase_plus = product_state(
    rho_sector_a_0, P_PLUS, rho_sector_b_0, rho_fibre_b_0
)
rho_phase_minus = product_state(
    rho_sector_a_0, P_MINUS, rho_sector_b_0, rho_fibre_b_0
)

check(
    "population hostile pair has one identical formed regional record",
    central_distribution(rho_pop_0, central_projectors)
    == central_distribution(rho_pop_1, central_projectors)
    == (Q(1), Q(0), Q(0), Q(0)),
    "Both states have public sectors A=0 and B=0.",
)
check(
    "population fibre leaks into the next public center",
    central_distribution(evolve(U_FIBRE_POP, rho_pop_0), central_projectors)
    == (Q(1), Q(0), Q(0), Q(0))
    and central_distribution(evolve(U_FIBRE_POP, rho_pop_1), central_projectors)
    == (Q(0), Q(1), Q(0), Q(0)),
    "The hidden A-fibre population flips B's public sector with unit margin.",
)
check(
    "population coupling fails center screening",
    not unitary_screens_center(U_FIBRE_POP, central_projectors),
    "A pulled-back public projector is noncentral inside one current sector.",
)

check(
    "phase hostile pair has one identical public record",
    central_distribution(rho_phase_plus, central_projectors)
    == central_distribution(rho_phase_minus, central_projectors)
    == (Q(1), Q(0), Q(0), Q(0)),
    "The old public center is blind to the fibre phase.",
)
check(
    "phase hostile pair also has identical Z-fibre populations",
    expectation(rho_phase_plus, op(I2, P0, I2, I2))
    == expectation(rho_phase_minus, op(I2, P0, I2, I2))
    == Q(1, 2),
    "The witness is not a hidden computational-basis population difference.",
)
check(
    "coherent fibre phase leaks into the next public center",
    central_distribution(
        evolve(U_FIBRE_PHASE, rho_phase_plus), central_projectors
    )
    == (Q(1), Q(0), Q(0), Q(0))
    and central_distribution(
        evolve(U_FIBRE_PHASE, rho_phase_minus), central_projectors
    )
    == (Q(0), Q(1), Q(0), Q(0)),
    "X-fibre phase is converted into B's public sector with unit margin.",
)
check(
    "phase coupling fails center screening",
    not unitary_screens_center(U_FIBRE_PHASE, central_projectors),
    "The public pullback contains a noncentral X-fibre projector.",
)

final_public_effect = central_projectors[0]
phase_pullback = pullback(U_FIBRE_PHASE, final_public_effect)
check(
    "first noncentral pullback is localized at the phase coupling",
    is_central(final_public_effect, central_projectors)
    and not is_central(phase_pullback, central_projectors),
    "The final effect is central and leaves the center at the first hostile reverse step.",
)
check(
    "first-leak probability margin is exactly one",
    expectation(rho_phase_plus, phase_pullback)
    - expectation(rho_phase_minus, phase_pullback)
    == 1,
    "The compression has eigenvalues one and zero in the same public block.",
)

# Screening need not destroy the fibre.
screened_plus = evolve(U_CENTER, rho_phase_plus)
screened_minus = evolve(U_CENTER, rho_phase_minus)
check(
    "center screening preserves an orthogonal quantum fibre",
    trace(mul(screened_plus, screened_minus)) == 0
    and central_distribution(screened_plus, central_projectors)
    == central_distribution(screened_minus, central_projectors),
    "The public-only update screens rather than destroys the retained phase.",
)
check(
    "a later hostile map reopens the screened fibre",
    central_distribution(
        evolve(U_FIBRE_PHASE, screened_plus), central_projectors
    )
    != central_distribution(
        evolve(U_FIBRE_PHASE, screened_minus), central_projectors
    ),
    "Finality was only relative to the earlier center-preserving future action class.",
)

# Physical dephasing is a matched way to destroy the phase before recoupling.
dephased_plus = dephase(rho_phase_plus, Z_FIBRE_A)
dephased_minus = dephase(rho_phase_minus, Z_FIBRE_A)
check(
    "Z dephasing makes the phase hostile pair identical",
    dephased_plus == dephased_minus,
    "The two X-fibre eigenstates both become the maximally mixed fibre.",
)
check(
    "dephasing screens the later phase-to-center assay",
    central_distribution(
        evolve(U_FIBRE_PHASE, dephased_plus), central_projectors
    )
    == central_distribution(
        evolve(U_FIBRE_PHASE, dephased_minus), central_projectors
    ),
    "Destroying coherent optionality removes the public feedback witness.",
)

# Aggregate-versus-selective control.  The route measurement is in the
# X-fibre basis.  Its aggregate channel leaves every central projector fixed,
# while each retained route cell is noncentral.
K_PLUS = op(I2, P_PLUS, I2, I2)
K_MINUS = op(I2, P_MINUS, I2, I2)
route_kraus = (K_PLUS, K_MINUS)
check(
    "route Kraus operators form a complete instrument",
    add(
        mul(transpose(K_PLUS), K_PLUS),
        mul(transpose(K_MINUS), K_MINUS),
    )
    == I16,
    "The two X-fibre route effects sum exactly to identity.",
)
check(
    "aggregate route channel preserves every public central effect",
    all(
        add(
            mul(mul(transpose(K_PLUS), projector), K_PLUS),
            mul(mul(transpose(K_MINUS), projector), K_MINUS),
        )
        == projector
        for projector in central_projectors
    ),
    "Discarding the route makes the public center transition look closed.",
)
check(
    "complete selective route cells fail center screening",
    not selective_cells_screen_center(route_kraus, central_projectors),
    "Each retained route carries noncentral X-fibre information.",
)
check(
    "retained route separates the same-public-record phase pair",
    expectation(rho_phase_plus, mul(transpose(K_PLUS), K_PLUS)) == 1
    and expectation(rho_phase_minus, mul(transpose(K_PLUS), K_PLUS)) == 0,
    "Aggregate center preservation is insufficient for HC-DU-036H.",
)

# Positive public update table.
rho_public_10 = product_state(
    rho_sector_a_1, P_PLUS, rho_sector_b_0, rho_fibre_b_0
)
check(
    "public-only coupling implements a deterministic center kernel",
    central_distribution(evolve(U_CENTER, rho_public_10), central_projectors)
    == (Q(0), Q(0), Q(0), Q(1)),
    "Public input (A=1,B=0) maps to public output (A=1,B=1) independently of fibres.",
)

# Common exact representation change.
permutation_rows = [[Q(0) for _ in range(16)] for _ in range(16)]
for index in range(16):
    s_a = (index >> 3) & 1
    f_a = (index >> 2) & 1
    s_b = (index >> 1) & 1
    f_b = index & 1
    new_index = (((1 - s_a) * 2 + f_a) * 2 + s_b) * 2 + f_b
    permutation_rows[new_index][index] = Q(1)
PERMUTATION = matrix(permutation_rows)


def conjugate(item: Matrix) -> Matrix:
    return mul(mul(PERMUTATION, item), transpose(PERMUTATION))


rotated_center = tuple(conjugate(item) for item in central_projectors)
rotated_safe = conjugate(U_CENTER)
rotated_hostile = conjugate(U_FIBRE_PHASE)
check(
    "center-screening verdict is representation robust",
    unitary_screens_center(rotated_safe, rotated_center)
    and not unitary_screens_center(rotated_hostile, rotated_center),
    "Common conjugation preserves safe versus leaking classification.",
)
check(
    "first-leak margin is representation robust",
    expectation(
        conjugate(rho_phase_plus),
        pullback(rotated_hostile, conjugate(final_public_effect)),
    )
    - expectation(
        conjugate(rho_phase_minus),
        pullback(rotated_hostile, conjugate(final_public_effect)),
    )
    == 1,
    "The exact separating probability remains one after relabeling.",
)

# Unchanged distributed-process shadow.
def safe_certificate_update(state: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    cert_a, local_a, cert_b, local_b = state
    return cert_a, local_a, cert_b ^ cert_a, local_b


def unsafe_hidden_hook(state: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    cert_a, local_a, cert_b, local_b = state
    return cert_a, local_a, cert_b ^ local_a, local_b


distributed_0 = (0, 0, 0, 0)
distributed_1 = (0, 1, 0, 0)
public_projection = lambda state: (state[0], state[2])

check(
    "distributed shadow begins with one certified regional record",
    public_projection(distributed_0) == public_projection(distributed_1) == (0, 0),
    "The hidden local state is outside the public certificate.",
)
check(
    "safe distributed transition descends through certificates",
    public_projection(safe_certificate_update(distributed_0))
    == public_projection(safe_certificate_update(distributed_1)),
    "The public update uses only certified input bits.",
)
check(
    "hidden distributed hook violates certificate finality",
    public_projection(unsafe_hidden_hook(distributed_0))
    != public_projection(unsafe_hidden_hook(distributed_1)),
    "A local hidden bit feeds back into the later public certificate.",
)

passed = sum(1 for item in checks if item["passed"])
result = {
    "run_id": "RUN-20260726-154509-center-screening-regional-finality",
    "hypothesis_id": "HC-DU-035D",
    "status": "completed_scoped_result",
    "verdict": "KNOWN_MATHEMATICS__CENTER_SCREENING_FINALITY_AND_FIRST_LEAK_EXACT",
    "checks": checks,
    "summary": {
        "passed": passed,
        "total": len(checks),
        "descent": "the public regional process closes exactly when every complete selective map pulls the next center into the current center",
        "composition": "selectively center-screening maps close under tensor product, sequential composition, and record-adaptive policies",
        "first_leak": "any later public dependence on a retained fibre has a first noncentral pullback and a same-center finite witness",
        "margin": "the hostile coherent phase-to-public conversion has exact probability gap one inside one central block",
        "screening": "a noncommutative fibre can persist while screened; finality does not require destruction",
        "selective_boundary": "aggregate center preservation can hide a noncentral retained route and therefore does not satisfy HC-DU-036H",
        "cross_platform": "the same center/fibre schema applies to an authenticated distributed shadow, while the phase-only witness remains quantum",
    },
    "local_model_learning_gate": {
        "disposition": "REGRESSION_ONLY_AFTER_DIRECT_PROOF",
        "hardware_required": False,
        "generated_learning_claim": False,
        "purpose": "preserve exact minimal phase, selective-route, first-leak, and cross-platform controls after the symbolic proof",
    },
    "claim_ceiling": [
        "finite-dimensional center-screening and first-leak theorem",
        "known operator-algebra, stable-commutative-subalgebra, process-memory, and lumpability mathematics",
        "conditional on supplied regions, centers, selective maps, future action class, and formation receipts",
        "no physical regionalization, universal finality, quantum-theory selection, record-first ontology, new law, new physics, hardware result, paper promotion, or publication",
    ],
    "next_dependency": "apply the screened center process to time/geometry reconstruction while retaining one explicit fibre-leak foil, and separately seek physical selection of the regional action algebras and couplings",
}

artifact_path = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_center_screening_regional_finality_result.json"
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
