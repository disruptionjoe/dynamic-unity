#!/usr/bin/env python3
"""Exact spinor-bilinear response-family controls for HC-DU-222."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_spinor_bilinear_response_quotient_result.json"


@dataclass(frozen=True)
class G:
    """Gaussian rational used to keep every rank and response exact."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "G":
        value = as_g(other)
        return G(self.re + value.re, self.im + value.im)

    __radd__ = __add__

    def __neg__(self) -> "G":
        return G(-self.re, -self.im)

    def __sub__(self, other: object) -> "G":
        return self + (-as_g(other))

    def __rsub__(self, other: object) -> "G":
        return as_g(other) - self

    def __mul__(self, other: object) -> "G":
        value = as_g(other)
        return G(
            self.re * value.re - self.im * value.im,
            self.re * value.im + self.im * value.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "G":
        value = as_g(other)
        norm = value.re * value.re + value.im * value.im
        if norm == 0:
            raise ZeroDivisionError
        return G(
            (self.re * value.re + self.im * value.im) / norm,
            (self.im * value.re - self.re * value.im) / norm,
        )

    def conj(self) -> "G":
        return G(self.re, -self.im)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def serial(self) -> str:
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f"{self.im}i"
        sign = "+" if self.im > 0 else ""
        return f"{self.re}{sign}{self.im}i"


def as_g(value: object) -> G:
    if isinstance(value, G):
        return value
    if isinstance(value, Fraction):
        return G(value)
    if isinstance(value, int):
        return G(Fraction(value))
    raise TypeError(value)


ZERO = G()
ONE = G(Fraction(1))
I = G(Fraction(0), Fraction(1))
Matrix = tuple[tuple[G, ...], ...]
Vector = tuple[G, ...]


def matrix(rows: tuple[tuple[object, ...], ...]) -> Matrix:
    return tuple(tuple(as_g(value) for value in row) for row in rows)


I2 = matrix(((1, 0), (0, 1)))
X = matrix(((0, 1), (1, 0)))
Y = ((ZERO, -I), (I, ZERO))
Z = matrix(((1, 0), (0, -1)))


def identity(size: int) -> Matrix:
    return tuple(tuple(ONE if row == column else ZERO for column in range(size)) for row in range(size))


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[r][c] + right[r][c] for c in range(len(left[0]))) for r in range(len(left)))


def mat_scale(value: object, source: Matrix) -> Matrix:
    return tuple(tuple(as_g(value) * entry for entry in row) for row in source)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum((left[r][k] * right[k][c] for k in range(len(right))), ZERO) for c in range(len(right[0])))
        for r in range(len(left))
    )


def dagger(source: Matrix) -> Matrix:
    return tuple(tuple(source[c][r].conj() for c in range(len(source))) for r in range(len(source[0])))


def outer(vector: Vector) -> Matrix:
    return tuple(tuple(vector[r] * vector[c].conj() for c in range(len(vector))) for r in range(len(vector)))


def trace(source: Matrix) -> G:
    return sum((source[index][index] for index in range(len(source))), ZERO)


def expectation(state: Vector, observable: Matrix) -> G:
    return trace(mat_mul(outer(state), observable))


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[r1][c1] * right[r2][c2] for c1 in range(len(left[0])) for c2 in range(len(right[0])))
        for r1 in range(len(left))
        for r2 in range(len(right))
    )


def flatten(source: Matrix) -> list[G]:
    return [entry for row in source for entry in row]


def rank(rows: list[list[G]]) -> int:
    work = [row[:] for row in rows]
    if not work:
        return 0
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if not work[r][column].is_zero()), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for r in range(len(work)):
            if r == pivot_row or work[r][column].is_zero():
                continue
            factor = work[r][column]
            work[r] = [work[r][c] - factor * work[pivot_row][c] for c in range(len(work[0]))]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def span_rank(matrices: list[Matrix]) -> int:
    return rank([flatten(item) for item in matrices])


def reconstruct_qubit(current: tuple[G, G, G, G]) -> Matrix:
    j0, jx, jy, jz = current
    return mat_scale(Fraction(1, 2), mat_add(mat_scale(j0, I2), mat_add(mat_scale(jx, X), mat_add(mat_scale(jy, Y), mat_scale(jz, Z)))))


def current(state: Vector, observables: tuple[Matrix, ...]) -> tuple[G, ...]:
    return tuple(expectation(state, observable) for observable in observables)


def run() -> dict[str, object]:
    weyl_observables = (I2, X, Y, Z)
    assert span_rank(list(weyl_observables)) == 4

    half = Fraction(1, 2)
    states_2: dict[str, Vector] = {
        "+Z": (ONE, ZERO),
        "-Z": (ZERO, ONE),
        "+X": (G(half), G(half)),
        "-X": (G(half), G(-half)),
        "+Y": (G(half), G(Fraction(0), half)),
        "-Y": (G(half), G(Fraction(0), -half)),
    }
    # The X/Y samples are intentionally unnormalized by a common sqrt(2).
    # Normalize their density/current algebra exactly by dividing by j0.
    weyl_rows: dict[str, dict[str, object]] = {}
    for name, state in states_2.items():
        raw = current(state, weyl_observables)
        normalized = tuple(value / raw[0] for value in raw)
        reconstructed = reconstruct_qubit(normalized)  # type: ignore[arg-type]
        normalized_density = mat_scale(ONE / raw[0], outer(state))
        assert reconstructed == normalized_density
        spatial_norm = sum((value.re * value.re for value in normalized[1:]), Fraction(0))
        assert normalized[0] == ONE and spatial_norm == 1
        phase_state = tuple(I * value for value in state)
        assert current(phase_state, weyl_observables) == raw
        weyl_rows[name] = {
            "current": [value.serial() for value in normalized],
            "null_current": True,
            "density_reconstructed": True,
        }

    # Dirac representation: gamma^0=Z tensor I and gamma^i=iY tensor sigma_i.
    gamma0 = kron(Z, I2)
    gammas = (
        gamma0,
        kron(mat_scale(I, Y), X),
        kron(mat_scale(I, Y), Y),
        kron(mat_scale(I, Y), Z),
    )
    metric = (1, -1, -1, -1)
    for mu in range(4):
        for nu in range(4):
            anticommutator = mat_add(mat_mul(gammas[mu], gammas[nu]), mat_mul(gammas[nu], gammas[mu]))
            expected = mat_scale(2 * metric[mu] if mu == nu else 0, identity(4))
            assert anticommutator == expected

    gamma5 = mat_scale(I, mat_mul(mat_mul(mat_mul(gammas[0], gammas[1]), gammas[2]), gammas[3]))
    bivectors = [
        mat_scale(Fraction(1, 2) * I, mat_add(mat_mul(gammas[mu], gammas[nu]), mat_scale(-1, mat_mul(gammas[nu], gammas[mu]))))
        for mu in range(4)
        for nu in range(mu + 1, 4)
    ]
    dirac_covariants = [identity(4), gamma5, *gammas, *(mat_mul(gamma, gamma5) for gamma in gammas), *bivectors]
    assert len(dirac_covariants) == 16
    assert span_rank(dirac_covariants) == 16

    vector_observables = [mat_mul(gamma0, gamma) for gamma in gammas]
    assert span_rank(vector_observables) == 4
    upper_up: Vector = (ONE, ZERO, ZERO, ZERO)
    upper_down: Vector = (ZERO, ONE, ZERO, ZERO)
    current_up = current(upper_up, tuple(vector_observables))
    current_down = current(upper_down, tuple(vector_observables))
    assert current_up == current_down
    separating = [
        index for index, covariant in enumerate(dirac_covariants)
        if expectation(upper_up, mat_mul(gamma0, covariant))
        != expectation(upper_down, mat_mul(gamma0, covariant))
    ]
    assert separating

    # Exact operational quotient: the response span has an orthogonal
    # complement of dimension d^2-rank. Full span has no operator remainder.
    dirac_vector_remainder = 16 - span_rank(vector_observables)
    dirac_full_remainder = 16 - span_rank(dirac_covariants)
    assert dirac_vector_remainder == 12
    assert dirac_full_remainder == 0

    # Reference extension of HC-DU-221. Spin-only density is identical, while
    # the path-X observable distinguishes relative plus and minus signs.
    psi = states_2["+Z"]
    joint_plus: Vector = (psi[0], psi[1], psi[0], psi[1])
    joint_minus: Vector = (psi[0], psi[1], -psi[0], -psi[1])
    path_x = kron(X, I2)
    assert expectation(joint_plus, path_x) == G(2)
    assert expectation(joint_minus, path_x) == G(-2)
    assert outer(psi) == outer(tuple(-value for value in psi))

    checks = {
        "weyl_current_span_is_operator_complete": True,
        "weyl_current_reconstructs_frozen_projective_states": True,
        "pure_weyl_current_is_null": True,
        "weyl_bilinears_erase_global_phase": True,
        "dirac_gamma_clifford_relations_hold": True,
        "sixteen_dirac_covariants_are_full_rank": True,
        "dirac_vector_current_has_rank_four": True,
        "orthogonal_dirac_states_share_vector_current": True,
        "another_dirac_bilinear_separates_vector_current_twins": True,
        "vector_current_operator_remainder_has_dimension_twelve": True,
        "full_bilinear_operator_remainder_is_zero": True,
        "reference_path_reopens_relative_central_phase": True,
        "hc_du_221_projective_erasure_is_preserved": True,
    }
    assert all(checks.values())
    return {
        "claim_id": "HC-DU-222",
        "verdict": "ACTION_SELECTED_RESPONSE_FAMILY_DEFINES_OPERATIONAL_QUOTIENT_BUT_NOT_RECORD",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "weyl_current_controls": weyl_rows,
        "dirac_bilinear_channel_dimensions": {
            "scalar": 1,
            "pseudoscalar": 1,
            "vector": 4,
            "axial_vector": 4,
            "tensor": 6,
            "total": 16,
        },
        "dirac_vector_current": [value.serial() for value in current_up],
        "dirac_vector_current_twin_states": ["upper_spin_up", "upper_spin_down"],
        "first_separating_bilinear_index": separating[0],
        "operator_remainder_dimensions": {
            "weyl_full_current": 0,
            "dirac_vector_current": dirac_vector_remainder,
            "dirac_full_bilinears": dirac_full_remainder,
        },
        "typed_result": {
            "source_action_can_select": "carrier, symmetries, field content, and admitted interaction-response family",
            "response_family_selects": "operational state quotient relative to admitted couplings",
            "still_required_for_record": "physical vertex realization, preparation, instrument, transducer, archive, provenance, access, and use",
            "twistor_boundary": "Weyl current/null direction and incidence are geometric-response structure, not material record formation",
        },
        "earned": [
            "exact Weyl-current projective reconstruction",
            "exact Dirac vector-current insufficiency and full-bilinear completeness",
            "action-relative response-family operational quotient",
            "reference-extension boundary for central phase",
        ],
        "not_earned": [
            "physical selection of field content, coupling constants, instrument, archive, or observer",
            "twistor substrate, GU transfer, issuance, remainder, prediction, or new physics",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
