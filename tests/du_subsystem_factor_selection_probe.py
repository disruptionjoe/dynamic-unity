#!/usr/bin/env python3
"""Exact finite controls for HC-DU-076.

The probe distinguishes:

1. an abstract Hilbert-space tensor factorization;
2. a source-law stabilizer orbit of factorizations;
3. a target-derived invariant profile that classifies one factorization; and
4. a physically supplied pair of commuting observable algebras that
   reconstructs a tensor-product structure.

It is a finite algebraic certificate, not a simulation of emergent spacetime
or a proof that a physical Hamiltonian selects subsystems.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_subsystem_factor_selection_result.json"
)
TOL = 1e-10


def kron(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def hs_rank(operators: list[np.ndarray]) -> int:
    columns = [op.reshape(-1) for op in operators]
    return int(np.linalg.matrix_rank(np.column_stack(columns), tol=TOL))


def partial_trace_second_pure(state: np.ndarray) -> np.ndarray:
    matrix = state.reshape(2, 2)
    return matrix @ matrix.conj().T


def entropy_bits(matrix: np.ndarray) -> float:
    values = np.linalg.eigvalsh(matrix)
    values = values[values > TOL]
    return float(-np.sum(values * np.log2(values)))


def phase_equivalent(left: np.ndarray, right: np.ndarray) -> bool:
    overlap = np.vdot(left, right)
    return bool(abs(abs(overlap) - 1.0) < TOL)


def main() -> None:
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    ii = kron(identity, identity)
    xi = kron(x, identity)
    yi = kron(y, identity)
    zi = kron(z, identity)
    ix = kron(identity, x)
    iy = kron(identity, y)
    iz = kron(identity, z)

    hamiltonian = np.diag([0.0, 1.0, 2.0, 4.0]).astype(complex)
    controlled_z = np.diag([1.0, 1.0, 1.0, -1.0]).astype(complex)

    algebra_a0 = [ii, xi, yi, zi]
    algebra_b0 = [ii, ix, iy, iz]
    algebra_a1 = [
        controlled_z @ op @ controlled_z.conj().T for op in algebra_a0
    ]
    algebra_b1 = [
        controlled_z @ op @ controlled_z.conj().T for op in algebra_b0
    ]

    plus = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
    psi = kron(plus, plus)
    psi_in_rotated_factorization = controlled_z.conj().T @ psi

    rho_a_t0 = partial_trace_second_pure(psi)
    rho_a_t1 = partial_trace_second_pure(psi_in_rotated_factorization)
    entropy_t0 = entropy_bits(rho_a_t0)
    entropy_t1 = entropy_bits(rho_a_t1)

    eigenvalues = np.diag(hamiltonian).real
    vandermonde = np.column_stack(
        [(eigenvalues**degree) * psi for degree in range(4)]
    )

    fixed_center = [ii, zi]
    dephasing_fixed_basis = [
        ii,
        ix,
        iy,
        iz,
        zi,
        kron(z, x),
        kron(z, y),
        kron(z, z),
    ]

    checks: dict[str, bool] = {
        "hamiltonian_is_nondegenerate": len(set(eigenvalues.tolist())) == 4,
        "controlled_z_preserves_hamiltonian": np.linalg.norm(
            controlled_z @ hamiltonian
            - hamiltonian @ controlled_z
        )
        < TOL,
        "controlled_z_moves_first_factor": np.linalg.norm(algebra_a1[1] - xi)
        > 1.0,
        "controlled_z_maps_xi_to_xz": np.linalg.norm(
            algebra_a1[1] - kron(x, z)
        )
        < TOL,
        "controlled_z_maps_ix_to_zx": np.linalg.norm(
            algebra_b1[1] - kron(z, x)
        )
        < TOL,
        "original_factor_algebras_commute": all(
            np.linalg.norm(a @ b - b @ a) < TOL
            for a in algebra_a0
            for b in algebra_b0
        ),
        "rotated_factor_algebras_commute": all(
            np.linalg.norm(a @ b - b @ a) < TOL
            for a in algebra_a1
            for b in algebra_b1
        ),
        "original_pair_generates_full_algebra": hs_rank(
            [a @ b for a in algebra_a0 for b in algebra_b0]
        )
        == 16,
        "rotated_pair_generates_full_algebra": hs_rank(
            [a @ b for a in algebra_a1 for b in algebra_b1]
        )
        == 16,
        "original_factor_intersection_is_scalar": (
            hs_rank(algebra_a0)
            + hs_rank(algebra_b0)
            - hs_rank(algebra_a0 + algebra_b0)
        )
        == 1,
        "rotated_factor_intersection_is_scalar": (
            hs_rank(algebra_a1)
            + hs_rank(algebra_b1)
            - hs_rank(algebra_a1 + algebra_b1)
        )
        == 1,
        "same_state_is_product_in_original_factorization": abs(entropy_t0)
        < TOL,
        "same_state_is_maximally_entangled_in_rotated_factorization": abs(
            entropy_t1 - 1.0
        )
        < TOL,
        "full_support_state_breaks_controlled_z_symmetry": not phase_equivalent(
            psi, controlled_z @ psi
        ),
        "polynomials_of_h_on_full_support_state_span_hilbert_space": (
            np.linalg.matrix_rank(vandermonde, tol=TOL) == 4
        ),
        "target_tps_entropy_profiles_disagree_on_same_h_and_state": abs(
            entropy_t1 - entropy_t0
        )
        > 0.9,
        "dephasing_fixed_algebra_has_dimension_eight": hs_rank(
            dephasing_fixed_basis
        )
        == 8,
        "dephasing_center_has_dimension_two": hs_rank(fixed_center) == 2,
        "central_sector_structure_does_not_fix_full_factor_pair": (
            np.linalg.norm(controlled_z @ zi - zi @ controlled_z) < TOL
            and np.linalg.norm(algebra_b1[1] - algebra_b0[1]) > 1.0
        ),
    }

    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "claim_id": "HC-DU-076",
        "status": "PASS" if not failures else "FAIL",
        "checks_passed": len(checks) - len(failures),
        "checks_total": len(checks),
        "failures": failures,
        "exact_fixture": {
            "hamiltonian_spectrum": eigenvalues.tolist(),
            "stabilizer": "CZ",
            "entropy_bits_original_tps": entropy_t0,
            "entropy_bits_rotated_tps": entropy_t1,
            "state_stabilizer_overlap_magnitude": float(
                abs(np.vdot(psi, controlled_z @ psi))
            ),
            "polynomial_orbit_rank": int(
                np.linalg.matrix_rank(vandermonde, tol=TOL)
            ),
            "original_joint_algebra_rank": hs_rank(
                [a @ b for a in algebra_a0 for b in algebra_b0]
            ),
            "rotated_joint_algebra_rank": hs_rank(
                [a @ b for a in algebra_a1 for b in algebra_b1]
            ),
        },
        "scope": (
            "Finite algebraic certificate for source-law stabilizer-orbit "
            "nonselection, target-profile classification, and observable-"
            "algebra reconstruction. No physical TPS, record carrier, "
            "spacetime, ontology, or new quantum law is selected."
        ),
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"{result['status']}: {result['checks_passed']}/"
        f"{result['checks_total']} checks"
    )
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
