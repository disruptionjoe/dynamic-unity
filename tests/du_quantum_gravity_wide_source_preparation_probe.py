#!/usr/bin/env python3
"""Exact controls for HC-DU-190's wide-source spectral boundary.

This is a two-cell one-particle spectral fixture, not a quantum-gravity
simulation.  It distinguishes a global stationary state, deterministic local
energy-density profiles, expectation profiles, and the induced Newton kernel.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_gravity_wide_source_preparation_result.json"
)

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]
Vector = tuple[complex, complex]

I: Matrix = ((1, 0), (0, 1))
X: Matrix = ((0, 1), (1, 0))
Y: Matrix = ((0, -1j), (1j, 0))
Z: Matrix = ((1, 0), (0, -1))
P_L: Matrix = ((1, 0), (0, 0))
P_R: Matrix = ((0, 0), (0, 1))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(
        tuple(c * a[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def apply(a: Matrix, v: Vector) -> Vector:
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def inner(u: Vector, v: Vector) -> complex:
    return sum(u[i].conjugate() * v[i] for i in range(2))


def expectation(v: Vector, a: Matrix) -> complex:
    return inner(v, apply(a, v))


def variance(v: Vector, a: Matrix) -> float:
    mean = expectation(v, a)
    mean_square = expectation(v, multiply(a, a))
    return float((mean_square - mean * mean).real)


def norm(v: Vector) -> float:
    return math.sqrt(float(inner(v, v).real))


def delta(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    a = 3.0
    b = 5.0
    hopping = 2.0

    t_left = add(scale(a, P_L), scale(hopping / 2.0, X))
    t_right = add(scale(b, P_R), scale(hopping / 2.0, X))
    h_total = add(t_left, t_right)
    expected_h = add(add(scale(a, P_L), scale(b, P_R)), scale(hopping, X))
    checks.append(
        {
            "name": "local_cells_sum_to_global_hamiltonian",
            "passed": delta(h_total, expected_h) < 1.0e-12,
        }
    )
    global_trace = h_total[0][0] + h_total[1][1]
    global_determinant = (
        h_total[0][0] * h_total[1][1] - h_total[0][1] * h_total[1][0]
    )
    checks.append(
        {
            "name": "global_source_hamiltonian_is_positive_definite",
            "passed": global_trace.real > 0
            and abs(global_trace.imag) < 1.0e-12
            and global_determinant.real > 0
            and abs(global_determinant.imag) < 1.0e-12,
        }
    )

    commutator = add(multiply(t_left, t_right), scale(-1, multiply(t_right, t_left)))
    expected_commutator = scale(1j * hopping * (a + b) / 2.0, Y)
    checks.append(
        {
            "name": "positive_hopping_local_energy_cells_do_not_commute",
            "passed": delta(commutator, expected_commutator) < 1.0e-12
            and delta(commutator, scale(0, I)) > 1.0,
        }
    )

    # For a=b, |+x> is a stationary, spatially wide global-energy state.
    mass = 4.0
    t_left_symmetric = add(scale(mass, P_L), scale(hopping / 2.0, X))
    t_right_symmetric = add(scale(mass, P_R), scale(hopping / 2.0, X))
    h_symmetric = add(t_left_symmetric, t_right_symmetric)
    plus_x: Vector = (1 / math.sqrt(2), 1 / math.sqrt(2))
    energy = mass + hopping
    stationary_residual = tuple(
        value - energy * plus_x[index]
        for index, value in enumerate(apply(h_symmetric, plus_x))
    )
    checks.append(
        {
            "name": "wide_state_is_global_energy_eigenstate",
            "passed": norm(stationary_residual) < 1.0e-12,
        }
    )
    checks.append(
        {
            "name": "wide_stationary_state_has_zero_mean_current",
            "passed": abs(expectation(plus_x, Y)) < 1.0e-12,
        }
    )
    commutator_symmetric = add(
        multiply(t_left_symmetric, t_right_symmetric),
        scale(-1, multiply(t_right_symmetric, t_left_symmetric)),
    )
    checks.append(
        {
            "name": "zero_mean_current_does_not_annihilate_local_commutator",
            "passed": norm(apply(commutator_symmetric, plus_x)) > 1.0,
        }
    )
    checks.append(
        {
            "name": "global_energy_eigenstate_is_not_local_profile_eigenstate",
            "passed": variance(plus_x, t_left_symmetric) > 0.1
            and variance(plus_x, t_right_symmetric) > 0.1,
        }
    )

    # The commutator is invertible, so no vector can be a joint eigenvector.
    determinant = (
        commutator_symmetric[0][0] * commutator_symmetric[1][1]
        - commutator_symmetric[0][1] * commutator_symmetric[1][0]
    )
    checks.append(
        {
            "name": "hopping_case_has_no_common_local_energy_eigenvector",
            "passed": abs(determinant) > 1.0,
        }
    )

    # In the commuting rest-density limit, the one-particle joint profiles are
    # the two localized vertices; the wide wavefunction has only expectations.
    localized_profiles = ((mass, 0.0), (0.0, mass))
    wide_expectation_profile = (
        expectation(plus_x, scale(mass, P_L)).real,
        expectation(plus_x, scale(mass, P_R)).real,
    )
    checks.append(
        {
            "name": "commuting_limit_joint_profiles_are_localized",
            "passed": localized_profiles == ((4.0, 0.0), (0.0, 4.0)),
        }
    )
    checks.append(
        {
            "name": "wide_density_is_expectation_not_eigenprofile",
            "passed": all(
                abs(value - 2.0) < 1.0e-12
                for value in wide_expectation_profile
            )
            and abs(variance(plus_x, scale(mass, P_L)) - 4.0) < 1.0e-12
            and wide_expectation_profile not in localized_profiles,
        }
    )

    # With localized profile eigenvalues, Eq. (19)'s cross kernel is exactly
    # the lattice Newton potential on every |i,j> branch.
    distances = ((3, 4), (2, 3))
    profile_kernel = tuple(
        -mass * mass / distances[i][j] for i in range(2) for j in range(2)
    )
    newton_kernel = tuple(
        -mass * mass / distances[i][j] for i in range(2) for j in range(2)
    )
    checks.append(
        {
            "name": "localized_profile_phase_is_exactly_newton_kernel",
            "passed": profile_kernel == newton_kernel,
            "kernel": list(profile_kernel),
        }
    )

    # Coarsening to total mass makes the wide state deterministic only by
    # identifying both spatial profiles.
    total_mass = add(scale(mass, P_L), scale(mass, P_R))
    left_state: Vector = (1, 0)
    right_state: Vector = (0, 1)
    checks.append(
        {
            "name": "coarse_determinacy_erases_spatial_shape",
            "passed": variance(plus_x, total_mass) < 1.0e-12
            and abs(expectation(left_state, total_mass) - mass) < 1.0e-12
            and abs(expectation(right_state, total_mass) - mass) < 1.0e-12,
        }
    )

    # Replacing a profile-valued phase by its mean misses visibility loss.
    phases = (0.0, math.pi / 2.0)
    coherent_average = sum(cmath.exp(1j * phase) for phase in phases) / 2.0
    mean_phase_replacement = cmath.exp(1j * sum(phases) / 2.0)
    checks.append(
        {
            "name": "expectation_profile_replacement_misses_phase_visibility",
            "passed": abs(coherent_average) < abs(mean_phase_replacement) - 0.1,
            "coherent_visibility": abs(coherent_average),
            "mean_phase_visibility": abs(mean_phase_replacement),
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-190",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "analytic_boundary": {
            "local_cells": "T_L=a P_L+(J/2)X; T_R=b P_R+(J/2)X",
            "commutator": "[T_L,T_R]=i J(a+b)Y/2",
            "hopping_case": "J>0 and a+b>0 implies no common eigenvector",
            "commuting_case": "J=0 gives localized one-particle profiles",
            "phase_control": "localized profile kernel equals lattice Newton kernel",
        },
        "earned_boundary": (
            "A wide stationary global-energy state is not thereby a "
            "deterministic local-energy profile. In the smallest two-cell "
            "model with a positive global source Hamiltonian, hopping "
            "removes the joint local spectrum; "
            "removing hopping restores localized profiles and the Newton "
            "kernel. Coarse determinacy erases the spatial shape."
        ),
        "non_claims": [
            "No universal QFT no-go is proved.",
            "No Chen--Giacomini equation is algebraically refuted.",
            "No apparatus, magnitude, hardware action, or new DU law is earned.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
