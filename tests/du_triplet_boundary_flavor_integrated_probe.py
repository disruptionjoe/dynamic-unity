#!/usr/bin/env python3
"""Exact finite proxy for the triplet--boundary--flavor integrated swing.

This probe does not construct the GU source action or a physical Dirac
operator. It asks what follows after a triplet carrier and a unit-index
boundary map are supplied, and what still does not follow.

The finite proxy has four jobs:

1. verify index multiplication for a boundary map tensored with an n-channel
   carrier;
2. distinguish global chiral index from boundary/access-relative mode count;
3. prove that full triplet equivariance cannot differentiate flavor; and
4. show that noncommuting flavor operators can create mixing but are fit-only
   until their form is independently derived.

All matrices controlling the index calculation use exact rational rank.
Floating-point linear algebra is restricted to deterministic Hermitian flavor
controls with explicit residual tolerances.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import numpy as np


RUN_ID = "RUN-20260725-234255-triplet-boundary-flavor-integrated-swing"
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_triplet_boundary_flavor_integrated_probe_result.json"
)


def exact_rank(matrix: list[list[int | Fraction]]) -> int:
    """Return matrix rank by exact Gaussian elimination."""

    if not matrix:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    rank = 0
    pivot_col = 0
    while rank < rows and pivot_col < cols:
        pivot = next(
            (row for row in range(rank, rows) if work[row][pivot_col] != 0),
            None,
        )
        if pivot is None:
            pivot_col += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][pivot_col]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][pivot_col]
            if factor:
                work[row] = [
                    work[row][col] - factor * work[rank][col]
                    for col in range(cols)
                ]
        rank += 1
        pivot_col += 1
    return rank


def identity(size: int) -> list[list[int]]:
    return [[int(row == col) for col in range(size)] for row in range(size)]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def block_diagonal(*blocks: list[list[int]]) -> list[list[int]]:
    total_rows = sum(len(block) for block in blocks)
    total_cols = sum(len(block[0]) for block in blocks)
    result = [[0 for _ in range(total_cols)] for _ in range(total_rows)]
    row_offset = 0
    col_offset = 0
    for block in blocks:
        for row, values in enumerate(block):
            for col, value in enumerate(values):
                result[row_offset + row][col_offset + col] = value
        row_offset += len(block)
        col_offset += len(block[0])
    return result


def kronecker(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    for left_row in left:
        for right_row in right:
            row: list[int] = []
            for left_value in left_row:
                row.extend(left_value * right_value for right_value in right_row)
            result.append(row)
    return result


def index_receipt(matrix: list[list[int]]) -> dict[str, int]:
    """Index of a finite map C^columns -> C^rows."""

    rows = len(matrix)
    cols = len(matrix[0])
    rank = exact_rank(matrix)
    kernel = cols - rank
    cokernel = rows - rank
    return {
        "domain_dimension": cols,
        "codomain_dimension": rows,
        "rank": rank,
        "kernel_dimension": kernel,
        "cokernel_dimension": cokernel,
        "index_kernel_minus_cokernel": kernel - cokernel,
    }


def commutant_dimension(generators: Iterable[list[list[int]]]) -> dict[str, int]:
    """Dimension of real 3x3 matrices commuting with all supplied generators."""

    equations: list[list[int]] = []
    size = 3
    for generator in generators:
        for row in range(size):
            for col in range(size):
                equation = [0] * (size * size)
                # (XG)_{row,col}
                for middle in range(size):
                    equation[row * size + middle] += generator[middle][col]
                # -(GX)_{row,col}
                for middle in range(size):
                    equation[middle * size + col] -= generator[row][middle]
                equations.append(equation)
    constraint_rank = exact_rank(equations)
    return {
        "endomorphism_dimension": size * size,
        "constraint_rank": constraint_rank,
        "commutant_dimension": size * size - constraint_rank,
    }


def off_diagonal_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix - np.diag(np.diag(matrix))))


def finite_index_tournament() -> dict[str, Any]:
    # One boundary imbalance, independent of the triplet count.
    q_unit = [[1, 0, 0], [0, 1, 0]]
    q_closed = identity(3)
    q_target_three = [[1, 0, 0, 0]]
    q_mirror = transpose(q_unit)

    unit = index_receipt(q_unit)
    triplet = index_receipt(kronecker(q_unit, identity(3)))
    closed_triplet = index_receipt(kronecker(q_closed, identity(3)))
    target_coded = index_receipt(q_target_three)
    mirror = index_receipt(q_mirror)

    dimension_sweep = []
    for carrier_dimension in range(1, 6):
        receipt = index_receipt(kronecker(q_unit, identity(carrier_dimension)))
        dimension_sweep.append(
            {
                "carrier_dimension": carrier_dimension,
                "boundary_index": unit["index_kernel_minus_cokernel"],
                "tensor_index": receipt["index_kernel_minus_cokernel"],
                "equals_carrier_times_boundary_index": bool(
                    receipt["index_kernel_minus_cokernel"]
                    == carrier_dimension * unit["index_kernel_minus_cokernel"]
                ),
            }
        )

    # A vectorlike completion carries the opposite boundary sector. Its global
    # index is zero although a restricted boundary sees three right-null modes.
    vectorlike = index_receipt(
        kronecker(block_diagonal(q_unit, q_mirror), identity(3))
    )
    restricted_access_rank = triplet["kernel_dimension"]
    expanded_access_rank = (
        vectorlike["kernel_dimension"] + vectorlike["cokernel_dimension"]
    )

    # Add a contractible square block. This changes presentation/dimension but
    # not index; it is the finite stable-equivalence/refinement control.
    stabilized = index_receipt(
        kronecker(block_diagonal(q_unit, identity(2)), identity(3))
    )

    # Identical terminal operators with different claimed construction
    # provenance have identical spectral receipts. Operator output alone
    # cannot certify source ownership.
    provenance_source_derived = index_receipt(q_unit)
    provenance_target_coded = index_receipt(q_unit)

    return {
        "unit_boundary": unit,
        "triplet_tensor": triplet,
        "dimension_sweep": dimension_sweep,
        "closed_vectorlike_control": closed_triplet,
        "target_coded_scalar_index_three_control": target_coded,
        "opposite_boundary_sector": mirror,
        "vectorlike_completion": {
            **vectorlike,
            "restricted_boundary_capability_rank": restricted_access_rank,
            "expanded_boundary_zero_mode_access_rank": expanded_access_rank,
            "effective_three_does_not_identify_global_index": bool(
                restricted_access_rank == 3
                and expanded_access_rank == 6
                and vectorlike["index_kernel_minus_cokernel"] == 0
            ),
        },
        "benign_stabilization": stabilized,
        "provenance_nonidentification": {
            "source_derived_label_receipt": provenance_source_derived,
            "target_coded_label_receipt": provenance_target_coded,
            "all_operator_observables_identical": bool(
                provenance_source_derived == provenance_target_coded
            ),
            "consequence": (
                "Source ownership requires an independently audited construction "
                "map; it cannot be inferred from the final operator or index."
            ),
        },
    }


def flavor_tournament() -> dict[str, Any]:
    # The real spin-1 / SO(3) triplet representation. Its full commutant is
    # scalar, the finite real form of the Schur-lemma obstruction.
    lx = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
    ly = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
    lz = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]
    commutant = commutant_dimension([lx, ly, lz])

    # Exact common cyclic symmetry: every Hermitian polynomial in the same
    # three-cycle commutes and is diagonal in the same Fourier basis.
    cycle = np.array(
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],
        dtype=complex,
    )

    def hermitian_circulant(center: float, coupling: complex) -> np.ndarray:
        return (
            center * np.eye(3, dtype=complex)
            + coupling * cycle
            + np.conjugate(coupling) * cycle.conj().T
        )

    up_cyclic = hermitian_circulant(5.0, 1.0 + 2.0j)
    down_cyclic = hermitian_circulant(3.0, -0.5 + 1.25j)
    omega = np.exp(2.0j * np.pi / 3.0)
    fourier = np.array(
        [[omega ** (row * col) for col in range(3)] for row in range(3)],
        dtype=complex,
    ) / np.sqrt(3.0)
    up_fourier = fourier.conj().T @ up_cyclic @ fourier
    down_fourier = fourier.conj().T @ down_cyclic @ fourier
    cyclic_commutator = up_cyclic @ down_cyclic - down_cyclic @ up_cyclic
    up_gaps = np.diff(np.sort(np.linalg.eigvalsh(up_cyclic)))
    down_gaps = np.diff(np.sort(np.linalg.eigvalsh(down_cyclic)))

    # A source can produce nontrivial relative mixing only after supplying
    # noncommuting triplet-breaking structure. This explicit construction is a
    # positive control, not an explanation: the spectra and rotation are inputs.
    rotation_12 = np.array(
        [[3.0 / 5.0, -4.0 / 5.0, 0.0], [4.0 / 5.0, 3.0 / 5.0, 0.0], [0.0, 0.0, 1.0]]
    )
    rotation_23 = np.array(
        [[1.0, 0.0, 0.0], [0.0, 5.0 / 13.0, -12.0 / 13.0], [0.0, 12.0 / 13.0, 5.0 / 13.0]]
    )
    mixing_input = rotation_12 @ rotation_23
    up_broken = np.diag([1.0, 2.0, 5.0])
    down_spectrum_input = np.array([1.5, 3.5, 7.0])
    down_broken = (
        mixing_input @ np.diag(down_spectrum_input) @ mixing_input.T
    )
    broken_commutator = up_broken @ down_broken - down_broken @ up_broken
    down_spectrum_recovered = np.linalg.eigvalsh(down_broken)

    return {
        "full_triplet_equivariance": {
            **commutant,
            "only_scalar_endomorphisms_survive": bool(
                commutant["commutant_dimension"] == 1
            ),
            "consequence": (
                "A fully triplet-equivariant effective flavor operator is scalar "
                "and cannot split three masses or select a mixing basis."
            ),
        },
        "common_cyclic_symmetry_control": {
            "commutator_frobenius_norm": float(np.linalg.norm(cyclic_commutator)),
            "up_fourier_off_diagonal_norm": off_diagonal_norm(up_fourier),
            "down_fourier_off_diagonal_norm": off_diagonal_norm(down_fourier),
            "up_min_spectral_gap": float(np.min(np.abs(up_gaps))),
            "down_min_spectral_gap": float(np.min(np.abs(down_gaps))),
            "shared_eigenbasis_implies_trivial_relative_mixing": True,
            "consequence": (
                "One exact common cyclic action can split eigenvalues, but two "
                "normal flavor operators built only from that action commute and "
                "cannot generate nontrivial relative mixing."
            ),
        },
        "broken_noncommuting_positive_control": {
            "commutator_frobenius_norm": float(np.linalg.norm(broken_commutator)),
            "mixing_input": mixing_input.tolist(),
            "down_spectrum_input": down_spectrum_input.tolist(),
            "down_spectrum_recovered": down_spectrum_recovered.tolist(),
            "mixing_is_nontrivial": bool(
                np.linalg.norm(mixing_input - np.eye(3)) > 0.5
            ),
            "consequence": (
                "Noncommuting triplet-breaking operators can realize hierarchy "
                "and mixing, but this construction inserts both. It is FLAVOR_FIT_ONLY "
                "until a source law restricts them and yields held-out relations."
            ),
        },
    }


def evaluate() -> dict[str, Any]:
    index_data = finite_index_tournament()
    flavor_data = flavor_tournament()
    scope_contract = {
        "gu_physical_packet": "SOURCE_OPERATOR_UNDEFINED",
        "predictive_unified_operator": "NOT_EARNED",
    }

    checks = {
        "unit_boundary_index_is_one": (
            index_data["unit_boundary"]["index_kernel_minus_cokernel"] == 1
        ),
        "triplet_tensor_index_is_three": (
            index_data["triplet_tensor"]["index_kernel_minus_cokernel"] == 3
        ),
        "index_multiplies_across_carrier_dimensions": all(
            row["equals_carrier_times_boundary_index"]
            for row in index_data["dimension_sweep"]
        ),
        "closed_triplet_control_index_is_zero": (
            index_data["closed_vectorlike_control"][
                "index_kernel_minus_cokernel"
            ]
            == 0
        ),
        "scalar_target_coded_control_can_insert_three": (
            index_data["target_coded_scalar_index_three_control"][
                "index_kernel_minus_cokernel"
            ]
            == 3
        ),
        "opposite_boundary_has_index_minus_one": (
            index_data["opposite_boundary_sector"][
                "index_kernel_minus_cokernel"
            ]
            == -1
        ),
        "vectorlike_completion_global_index_is_zero": (
            index_data["vectorlike_completion"][
                "index_kernel_minus_cokernel"
            ]
            == 0
        ),
        "vectorlike_completion_has_three_modes_each_chirality": (
            index_data["vectorlike_completion"]["kernel_dimension"] == 3
            and index_data["vectorlike_completion"]["cokernel_dimension"] == 3
        ),
        "restricted_access_three_expands_to_six": (
            index_data["vectorlike_completion"][
                "effective_three_does_not_identify_global_index"
            ]
        ),
        "benign_stabilization_preserves_triplet_index": (
            index_data["benign_stabilization"][
                "index_kernel_minus_cokernel"
            ]
            == 3
        ),
        "terminal_operator_does_not_identify_source_provenance": (
            index_data["provenance_nonidentification"][
                "all_operator_observables_identical"
            ]
        ),
        "full_triplet_commutant_is_scalar": (
            flavor_data["full_triplet_equivariance"][
                "only_scalar_endomorphisms_survive"
            ]
        ),
        "common_cyclic_flavor_operators_commute": (
            flavor_data["common_cyclic_symmetry_control"][
                "commutator_frobenius_norm"
            ]
            < 1e-12
        ),
        "common_cyclic_up_operator_is_fourier_diagonal": (
            flavor_data["common_cyclic_symmetry_control"][
                "up_fourier_off_diagonal_norm"
            ]
            < 1e-12
        ),
        "common_cyclic_down_operator_is_fourier_diagonal": (
            flavor_data["common_cyclic_symmetry_control"][
                "down_fourier_off_diagonal_norm"
            ]
            < 1e-12
        ),
        "common_cyclic_control_spectra_are_nondegenerate": (
            flavor_data["common_cyclic_symmetry_control"][
                "up_min_spectral_gap"
            ]
            > 1e-6
            and flavor_data["common_cyclic_symmetry_control"][
                "down_min_spectral_gap"
            ]
            > 1e-6
        ),
        "broken_flavor_operators_do_not_commute": (
            flavor_data["broken_noncommuting_positive_control"][
                "commutator_frobenius_norm"
            ]
            > 1.0
        ),
        "broken_control_has_nontrivial_mixing": (
            flavor_data["broken_noncommuting_positive_control"][
                "mixing_is_nontrivial"
            ]
        ),
        "broken_control_recovers_inserted_spectrum": bool(
            np.allclose(
                flavor_data["broken_noncommuting_positive_control"][
                    "down_spectrum_input"
                ],
                flavor_data["broken_noncommuting_positive_control"][
                    "down_spectrum_recovered"
                ],
                atol=1e-12,
            )
        ),
        "scope_contract_keeps_physical_source_operator_undefined": (
            scope_contract["gu_physical_packet"]
            == "SOURCE_OPERATOR_UNDEFINED"
        ),
        "scope_contract_blocks_predictive_unified_operator": (
            scope_contract["predictive_unified_operator"] == "NOT_EARNED"
        ),
    }

    passed = sum(bool(value) for value in checks.values())
    total = len(checks)
    verdict = (
        "CONDITIONAL_INDEX_BRIDGE_FOUND__EFFECTIVE_THREE_NONIDENTIFIED__"
        "FLAVOR_BREAKING_REQUIRED__PHYSICAL_SOURCE_OPERATOR_OPEN"
        if passed == total
        else "PROBE_FAILURE"
    )

    return {
        "run_id": RUN_ID,
        "question": (
            "What can a unit-index boundary operator actually add to GU's "
            "triplet carrier, and what remains missing before three chiral "
            "generations and flavor are explained?"
        ),
        "scope": (
            "Exact finite boundary-complex and flavor-symmetry proxy; no "
            "physical GU source action, Fredholm/APS domain, anomaly "
            "certificate, Standard Model recovery, or new physics."
        ),
        "index_tournament": index_data,
        "flavor_tournament": flavor_data,
        "return_contract": {
            "gu_physical_packet": scope_contract["gu_physical_packet"],
            "unit_index_times_triplet_proxy": "CONDITIONAL_INDEX_THREE",
            "restricted_vectorlike_boundary": "EFFECTIVE_ACCESS_THREE",
            "scalar_index_three_control": "TARGET_CODED_THREE",
            "fully_equivariant_flavor": "FLAVOR_DEGENERATE",
            "noncommuting_broken_flavor_control": "FLAVOR_FIT_ONLY",
            "predictive_unified_operator": scope_contract[
                "predictive_unified_operator"
            ],
        },
        "checks": checks,
        "summary": {"passed": passed, "total": total, "verdict": verdict},
        "next_operator_contract": {
            "carrier": "actual GU triplet inside the physical vectorlike carrier",
            "boundary_operator": "source-derived physical operator and domain",
            "index_origin": "unit boundary/topological class fixed without target import",
            "mirror_and_anomaly_completion": "explicit local/global anomaly and inflow receipt",
            "access_map": "energy/region/task boundary separated from global chiral index",
            "flavor_structure": (
                "at least two source-derived noncommuting triplet-breaking "
                "effective operators or an equivalent predictive structure"
            ),
            "held_out_requirement": (
                "one mass, mixing, CP, running, or partner relation not used "
                "to choose the operator"
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ARTIFACT_PATH)
    args = parser.parse_args()

    result = evaluate()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")

    summary = result["summary"]
    print(
        f"{summary['passed']}/{summary['total']} checks passed — "
        f"{summary['verdict']}"
    )
    print(args.output)
    return 0 if summary["passed"] == summary["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
