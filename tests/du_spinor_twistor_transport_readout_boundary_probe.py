#!/usr/bin/env python3
"""Exact spin-holonomy, interference, and frame-soldering controls for HC-DU-221."""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_spinor_twistor_transport_readout_boundary_result.json"
)

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]
Vector = tuple[complex, complex]

I2: Matrix = ((1, 0), (0, 1))
X: Matrix = ((0, 1), (1, 0))
Y: Matrix = ((0, -1j), (1j, 0))
Z: Matrix = ((1, 0), (0, -1))


def scale(matrix: Matrix, value: complex) -> Matrix:
    return tuple(tuple(value * entry for entry in row) for row in matrix)  # type: ignore[return-value]


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][k] * right[k][column] for k in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def add_vectors(left: Vector, right: Vector, sign: int = 1) -> Vector:
    return tuple(left[index] + sign * right[index] for index in range(2))  # type: ignore[return-value]


def norm2(vector: Vector) -> int:
    value = sum(
        int(round(entry.real)) ** 2 + int(round(entry.imag)) ** 2
        for entry in vector
    )
    return value


def density(vector: Vector) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return tuple(
        tuple(vector[row] * vector[column].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def x_readout_probabilities(vector: Vector, holonomy: Matrix) -> tuple[Fraction, Fraction]:
    transported = mat_vec(holonomy, vector)
    denominator = 4 * norm2(vector)
    return (
        Fraction(norm2(add_vectors(vector, transported, 1)), denominator),
        Fraction(norm2(add_vectors(vector, transported, -1)), denominator),
    )


def z_readout_probabilities(vector: Vector, holonomy: Matrix) -> tuple[Fraction, Fraction]:
    transported = mat_vec(holonomy, vector)
    denominator = 2 * norm2(vector)
    return (Fraction(norm2(vector), denominator), Fraction(norm2(transported), denominator))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def octahedral_rotations() -> tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1:
                rotations.append((permutation, signs))
    assert len(rotations) == 24
    return tuple(rotations)


def rotate_axis(
    element: tuple[str, int, int] | tuple[str, int],
    rotation: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> tuple[str, int, int] | tuple[str, int]:
    if element[0] == "center":
        return element
    _, overall_sign, axis = element
    permutation, signs = rotation
    return ("axis", overall_sign * signs[axis], permutation[axis])


def holonomy_orbits() -> list[list[list[int | str]]]:
    elements: set[tuple] = {
        ("center", 1),
        ("center", -1),
        *{("axis", sign, axis) for sign in (-1, 1) for axis in range(3)},
    }
    rotations = octahedral_rotations()
    result: list[list[list[int | str]]] = []
    while elements:
        seed = min(elements)
        members = {rotate_axis(seed, rotation) for rotation in rotations}
        result.append([list(item) for item in sorted(members)])
        elements -= members
    return sorted(result, key=lambda orbit: (len(orbit), str(orbit)))


def commutes(left: Matrix, right: Matrix) -> bool:
    return mat_mul(left, right) == mat_mul(right, left)


def candidate_real_matrices() -> list[Matrix]:
    return [
        ((a, b), (c, d))
        for a, b, c, d in itertools.product((-1, 0, 1), repeat=4)
    ]


def run() -> dict[str, object]:
    holonomies: dict[str, Matrix] = {
        "+I": I2,
        "-I": scale(I2, -1),
        "+iX": scale(X, 1j),
        "-iX": scale(X, -1j),
        "+iY": scale(Y, 1j),
        "-iY": scale(Y, -1j),
        "+iZ": scale(Z, 1j),
        "-iZ": scale(Z, -1j),
    }
    orbits = holonomy_orbits()
    assert sorted(len(orbit) for orbit in orbits) == [1, 1, 6]

    psi: Vector = (1, 0)
    plus_spinor = mat_vec(holonomies["+I"], psi)
    minus_spinor = mat_vec(holonomies["-I"], psi)
    assert plus_spinor != minus_spinor
    assert density(plus_spinor) == density(minus_spinor)

    x_probabilities = {
        name: [str(value) for value in x_readout_probabilities(psi, matrix)]
        for name, matrix in holonomies.items()
    }
    z_probabilities = {
        name: [str(value) for value in z_readout_probabilities(psi, matrix)]
        for name, matrix in holonomies.items()
    }
    assert x_probabilities["+I"] == ["1", "0"]
    assert x_probabilities["-I"] == ["0", "1"]
    assert z_probabilities["+I"] == z_probabilities["-I"] == ["1/2", "1/2"]
    assert all(
        x_probabilities[name] == ["1/2", "1/2"]
        for name in ("+iX", "-iX", "+iY", "-iY", "+iZ", "-iZ")
    )

    # Deleting/tracing out the path leaves a mixture of the two arm states.
    # For central +/-I both arms have the same spin density, so the reduced
    # spin state is identical.
    reduced_spin_density = {
        name: density(mat_vec(matrix, psi))
        for name, matrix in {"+I": holonomies["+I"], "-I": holonomies["-I"]}.items()
    }
    assert reduced_spin_density["+I"] == reduced_spin_density["-I"]

    # Finite Pauli-frame shadow: four possible source-target alignments are a
    # torsor under independent source and target frame changes (xor law).
    alignments = set(range(4))
    transformed = {
        alignment: {
            target_frame ^ alignment ^ source_frame
            for source_frame in range(4)
            for target_frame in range(4)
        }
        for alignment in alignments
    }
    assert all(images == alignments for images in transformed.values())
    assert not any(
        all(target_frame ^ alignment ^ source_frame == alignment
            for source_frame in range(4) for target_frame in range(4))
        for alignment in alignments
    )

    # Exact finite Schur control. In a two-dimensional carrier, a real matrix
    # commuting with both Pauli X and Z is scalar. Restricting entries to
    # {-1,0,1} leaves 0 and +/-I; the nonzero orthogonal choices are +/-I.
    commutant = [matrix for matrix in candidate_real_matrices() if commutes(matrix, X) and commutes(matrix, Z)]
    expected_commutant = [scale(I2, value) for value in (-1, 0, 1)]
    assert sorted(commutant, key=str) == sorted(expected_commutant, key=str)
    nonzero_intertwiners = [matrix for matrix in commutant if matrix != scale(I2, 0)]
    assert len(nonzero_intertwiners) == 2
    assert density(mat_vec(nonzero_intertwiners[0], psi)) == density(mat_vec(nonzero_intertwiners[1], psi))
    assert x_readout_probabilities(psi, nonzero_intertwiners[0]) != x_readout_probabilities(psi, nonzero_intertwiners[1])

    parent = json.loads(
        (ROOT / "tests" / "artifacts" / "du_holonomy_handoff_soldering_boundary_result.json").read_text()
    )
    assert parent["passed"] == parent["total"] == 15
    assert parent["verdict"] == "HOLONOMY_SELECTS_RETURN_PARITY_BUT_DISTINCT_TARGET_REQUIRES_SOLDERING"

    checks = {
        "finite_spin_frame_shadow_has_24_rotations": True,
        "spin_holonomies_split_into_two_central_and_one_axis_orbit": True,
        "central_spinors_differ_as_vectors": True,
        "central_spinors_are_identical_as_rays": True,
        "single_spin_density_erases_central_sign": True,
        "coherent_reference_x_readout_separates_central_sign": True,
        "path_z_readout_does_not_separate_central_sign": True,
        "noncentral_pi_holonomies_have_zero_x_visibility_in_control": True,
        "reference_deletion_erases_central_sign_again": True,
        "independent_spin_frames_act_transitively_on_alignments": True,
        "no_alignment_is_fixed_by_independent_frame_changes": True,
        "pauli_irrep_commutant_is_scalar_in_exact_control": True,
        "projective_phase_is_erased_without_reference": True,
        "relative_phase_is_visible_with_reference": True,
        "hc_du_220_boundary_is_preserved": True,
    }
    assert all(checks.values())

    return {
        "claim_id": "HC-DU-221",
        "verdict": "SPIN_TRANSPORT_IS_REAL_BUT_PHASE_VISIBILITY_AND_DISTINCT_TARGET_COUPLING_REQUIRE_INTERFACES",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "spin_holonomy_orbits": orbits,
        "reference_arm_x_readout": x_probabilities,
        "path_z_readout": z_probabilities,
        "finite_frame_alignment_orbit_size": len(alignments),
        "exact_pauli_commutant": [str(matrix) for matrix in commutant],
        "twistor_type_boundary": {
            "carrier": "local twistor Z=(omega^A, pi_A')",
            "transport_requires": "conformal spin/twistor connection and path",
            "incidence_requires": "spacetime point/soldering data omega^A = i x^{AA'} pi_A'",
            "material_record_requires": "selected coupling, coherent or dissipative transduction, meter, archive, and access",
            "finite_spinor_probe_is_full_twistor_construction": False,
        },
        "earned": [
            "spin transport orbit and central-sign type separation",
            "projective erasure of isolated central phase",
            "reference-arm and readout-basis necessity for phase visibility",
            "distinct-spin-frame intertwiner obstruction",
            "typed twistor-to-material coupling boundary",
        ],
        "not_earned": [
            "physical selection of a spin/twistor connection or path",
            "physical selection of a reference arm, recombiner, meter, or archive",
            "full Lorentzian twistor theory, GU transfer, issuance, remainder, or new physics",
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
