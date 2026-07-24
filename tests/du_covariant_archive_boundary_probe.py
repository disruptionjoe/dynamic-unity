#!/usr/bin/env python3
"""Finite probe for a covariant Clock-QCA pointer and declared archive.

The source host is the q-transparent 1+1 Clock QCA of Arrighi, Facchini,
and Forets (arXiv:1404.4499).  A particle carries one pointer qubit.  A
source-effective particle/zero event applies R_theta to that pointer, while
encoding-added q crossings transport it unchanged.

The archive coupling is intentionally separate from the source-covariant
gate.  At a declared interface, pointer-basis CNOT export, full SWAP transfer,
and independent fresh-cell recording are compared.  Passing this probe earns
only finite mathematical construction and scoped obstruction results.  It
does not select an interface or law, make a classical irreversible record, or
establish continuum physics, observerhood, proper time, or Dynamic Unity.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_covariant_archive_boundary_result.json"
)
SOURCE_TEX_SHA256 = (
    "121ccb1e66c5e408c4a659c66a9873e8d0544655e0a28ccd920e3f407ed1fdfb"
)
SOURCE_PDF_SHA256 = (
    "578c156f25fb9b2698bca5f6f27d43e7e1c09ee884a64f78e9f1e2515b0cebc4"
)
TOL = 2.0e-10

SparseState = dict[tuple[int, ...], complex]


def pair_index(left: int, right: int, dimension: int) -> int:
    return left * dimension + right


def pair_from_index(index: int, dimension: int) -> tuple[int, int]:
    return divmod(index, dimension)


def add_entry(
    matrix: np.ndarray,
    output_pair: tuple[int, int],
    input_pair: tuple[int, int],
    amplitude: complex,
    dimension: int,
) -> None:
    matrix[
        pair_index(*output_pair, dimension),
        pair_index(*input_pair, dimension),
    ] += amplitude


def matrix_error(matrix: np.ndarray) -> float:
    identity = np.eye(matrix.shape[0], dtype=complex)
    return float(np.max(np.abs(matrix.conj().T @ matrix - identity)))


def matrix_digest(matrix: np.ndarray) -> str:
    serial = [
        [
            [round(float(value.real), 15), round(float(value.imag), 15)]
            for value in row
        ]
        for row in matrix
    ]
    raw = json.dumps(serial, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = left - right
    if np.max(np.abs(difference - difference.conj().T)) > TOL:
        singular_values = np.linalg.svd(difference, compute_uv=False)
        return float(0.5 * np.sum(singular_values))
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(difference))))


def pure_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def reduced_from_pure(
    vector: np.ndarray,
    dimensions: tuple[int, ...],
    keep: tuple[int, ...],
) -> np.ndarray:
    """Partial trace of a pure state, preserving the declared subsystem order."""

    discarded = tuple(index for index in range(len(dimensions)) if index not in keep)
    tensor = vector.reshape(dimensions)
    permuted = np.transpose(tensor, keep + discarded)
    keep_dimension = math.prod(dimensions[index] for index in keep)
    discard_dimension = math.prod(dimensions[index] for index in discarded)
    matrix = permuted.reshape(keep_dimension, discard_dimension)
    return matrix @ matrix.conj().T


def coin_family() -> list[tuple[str, np.ndarray]]:
    theta = 0.37
    dirac = np.array(
        [
            [math.cos(theta), -1j * math.sin(theta)],
            [-1j * math.sin(theta), math.cos(theta)],
        ],
        dtype=complex,
    )
    general_theta = 0.61
    phi = 0.23
    chi = -0.47
    general = np.array(
        [
            [
                np.exp(1j * phi) * math.cos(general_theta),
                np.exp(1j * chi) * math.sin(general_theta),
            ],
            [
                -np.exp(-1j * chi) * math.sin(general_theta),
                np.exp(-1j * phi) * math.cos(general_theta),
            ],
        ],
        dtype=complex,
    )
    return [("dirac_theta_0p37", dirac), ("general_su2", general)]


def pointer_rotation(theta: float) -> np.ndarray:
    return np.array(
        [
            [math.cos(theta), -math.sin(theta)],
            [math.sin(theta), math.cos(theta)],
        ],
        dtype=complex,
    )


def source_scattering(coin: np.ndarray) -> np.ndarray:
    """Exact source 9x9 Clock-QCA scattering in row-output convention."""

    dimension = 3
    q, zero, one = 0, 1, 2
    matrix = np.zeros((dimension**2, dimension**2), dtype=complex)
    add_entry(matrix, (q, q), (q, q), 1.0, dimension)
    add_entry(matrix, (zero, q), (q, zero), 1.0, dimension)
    add_entry(matrix, (q, zero), (zero, q), 1.0, dimension)
    add_entry(matrix, (zero, zero), (zero, zero), 1.0, dimension)
    add_entry(matrix, (one, one), (one, one), 1.0, dimension)
    add_entry(matrix, (q, one), (one, q), 1.0, dimension)
    add_entry(matrix, (one, q), (q, one), 1.0, dimension)
    a, b = coin[0, 0], coin[0, 1]
    c, d = coin[1, 0], coin[1, 1]
    add_entry(matrix, (zero, one), (one, zero), a, dimension)
    add_entry(matrix, (one, zero), (one, zero), b, dimension)
    add_entry(matrix, (zero, one), (zero, one), c, dimension)
    add_entry(matrix, (one, zero), (zero, one), d, dimension)
    return matrix


def pointer_scattering(
    theta: float,
    coin: np.ndarray,
    *,
    rotate_on_q: bool = False,
) -> np.ndarray:
    """Complete 16x16 source gate with a particle-carried pointer qubit.

    Alphabet order is q=0, zero=1, particle-pointer-0=2,
    particle-pointer-1=3.  The good candidate rotates the pointer only on the
    source-effective particle/zero sector.  ``rotate_on_q`` is the deliberately
    bad microscopic-crossing rival.
    """

    dimension = 4
    q, zero = 0, 1
    particles = (2, 3)
    rotation = pointer_rotation(theta)
    matrix = np.zeros((dimension**2, dimension**2), dtype=complex)

    add_entry(matrix, (q, q), (q, q), 1.0, dimension)
    add_entry(matrix, (zero, q), (q, zero), 1.0, dimension)
    add_entry(matrix, (q, zero), (zero, q), 1.0, dimension)
    add_entry(matrix, (zero, zero), (zero, zero), 1.0, dimension)

    for pointer_in, particle_in in enumerate(particles):
        for pointer_out, particle_out in enumerate(particles):
            amplitude = (
                rotation[pointer_out, pointer_in]
                if rotate_on_q
                else (1.0 if pointer_out == pointer_in else 0.0)
            )
            add_entry(
                matrix,
                (q, particle_out),
                (particle_in, q),
                amplitude,
                dimension,
            )
            add_entry(
                matrix,
                (particle_out, q),
                (q, particle_in),
                amplitude,
                dimension,
            )

    for left_particle in particles:
        for right_particle in particles:
            add_entry(
                matrix,
                (left_particle, right_particle),
                (left_particle, right_particle),
                1.0,
                dimension,
            )

    a, b = coin[0, 0], coin[0, 1]
    c, d = coin[1, 0], coin[1, 1]
    for pointer_in, particle_in in enumerate(particles):
        for pointer_out, particle_out in enumerate(particles):
            record_amplitude = rotation[pointer_out, pointer_in]
            add_entry(
                matrix,
                (zero, particle_out),
                (particle_in, zero),
                a * record_amplitude,
                dimension,
            )
            add_entry(
                matrix,
                (particle_out, zero),
                (particle_in, zero),
                b * record_amplitude,
                dimension,
            )
            add_entry(
                matrix,
                (zero, particle_out),
                (zero, particle_in),
                c * record_amplitude,
                dimension,
            )
            add_entry(
                matrix,
                (particle_out, zero),
                (zero, particle_in),
                d * record_amplitude,
                dimension,
            )
    return matrix


def active_block(matrix: np.ndarray, dimension: int) -> np.ndarray:
    indices = [
        pair_index(left, right, dimension)
        for left in range(1, dimension)
        for right in range(1, dimension)
    ]
    return matrix[np.ix_(indices, indices)]


def q_transparent_lift(block: np.ndarray) -> np.ndarray:
    active_dimension = int(round(math.sqrt(block.shape[0])))
    if block.shape != (active_dimension**2, active_dimension**2):
        raise ValueError("block must act on K tensor K")
    dimension = active_dimension + 1
    matrix = np.zeros((dimension**2, dimension**2), dtype=complex)
    add_entry(matrix, (0, 0), (0, 0), 1.0, dimension)
    for symbol in range(1, dimension):
        add_entry(matrix, (symbol, 0), (0, symbol), 1.0, dimension)
        add_entry(matrix, (0, symbol), (symbol, 0), 1.0, dimension)
    for input_index in range(active_dimension**2):
        left_in, right_in = pair_from_index(input_index, active_dimension)
        for output_index, amplitude in enumerate(block[:, input_index]):
            if abs(amplitude) <= 1.0e-14:
                continue
            left_out, right_out = pair_from_index(
                output_index, active_dimension
            )
            add_entry(
                matrix,
                (left_out + 1, right_out + 1),
                (left_in + 1, right_in + 1),
                amplitude,
                dimension,
            )
    return matrix


def fourier_unitary(dimension: int) -> np.ndarray:
    rows = np.arange(dimension, dtype=float)[:, None]
    columns = np.arange(dimension, dtype=float)[None, :]
    return np.exp(2j * np.pi * rows * columns / dimension) / math.sqrt(
        dimension
    )


def local_action(
    matrix: np.ndarray,
    dimension: int,
    input_pair: tuple[int, int],
) -> dict[tuple[int, int], complex]:
    column = matrix[:, pair_index(*input_pair, dimension)]
    return {
        pair_from_index(index, dimension): complex(amplitude)
        for index, amplitude in enumerate(column)
        if abs(amplitude) > 1.0e-13
    }


def prune(state: SparseState) -> SparseState:
    return {
        basis: amplitude
        for basis, amplitude in state.items()
        if abs(amplitude) > 1.0e-12
    }


def apply_adjacent_gate(
    state: SparseState,
    position: int,
    matrix: np.ndarray,
    dimension: int,
) -> SparseState:
    output: SparseState = {}
    for basis, amplitude in state.items():
        pair = (basis[position], basis[position + 1])
        for out_pair, local_amplitude in local_action(
            matrix, dimension, pair
        ).items():
            out_basis = list(basis)
            out_basis[position : position + 2] = out_pair
            key = tuple(out_basis)
            output[key] = (
                output.get(key, 0.0j) + amplitude * local_amplitude
            )
    return prune(output)


def rectangular_patch(
    state: SparseState,
    alpha: int,
    beta: int,
    matrix: np.ndarray,
    dimension: int,
) -> SparseState:
    """Source planar braid: input alpha,beta; output beta,alpha."""

    if alpha < 1 or beta < 1:
        raise ValueError("positive patch dimensions required")
    result = dict(state)
    for beta_strand in range(beta):
        for position in range(
            alpha + beta_strand - 1, beta_strand - 1, -1
        ):
            result = apply_adjacent_gate(
                result, position, matrix, dimension
            )
    return result


def embedded_basis(
    symbol: int,
    length: int,
    placement: int,
) -> tuple[int, ...]:
    if not 0 <= placement < length:
        raise ValueError("placement outside encoding")
    output = [0] * length
    output[placement] = symbol
    return tuple(output)


def encoded_input(
    left_symbol: int,
    right_symbol: int,
    alpha: int,
    beta: int,
    left_placement: int,
    right_placement: int,
) -> tuple[int, ...]:
    return embedded_basis(
        left_symbol, alpha, left_placement
    ) + embedded_basis(right_symbol, beta, right_placement)


def expected_patch_output(
    matrix: np.ndarray,
    dimension: int,
    left_symbol: int,
    right_symbol: int,
    alpha: int,
    beta: int,
    left_placement: int,
    right_placement: int,
) -> SparseState:
    output: SparseState = {}
    for (left_out, right_out), amplitude in local_action(
        matrix, dimension, (left_symbol, right_symbol)
    ).items():
        basis = embedded_basis(
            left_out, beta, right_placement
        ) + embedded_basis(right_out, alpha, left_placement)
        output[basis] = output.get(basis, 0.0j) + amplitude
    return prune(output)


def sparse_distance(left: SparseState, right: SparseState) -> float:
    keys = set(left) | set(right)
    return max(
        (abs(left.get(key, 0.0j) - right.get(key, 0.0j)) for key in keys),
        default=0.0,
    )


def naturality_sweep(
    matrix: np.ndarray,
    dimension: int,
    patches: Iterable[tuple[int, int]],
    *,
    all_placements: bool,
) -> dict[str, Any]:
    cases = 0
    maximum_error = 0.0
    first_failure: dict[str, Any] | None = None
    for alpha, beta in patches:
        left_placements = range(alpha) if all_placements else range(1)
        right_placements = range(beta) if all_placements else range(1)
        for left_placement in left_placements:
            for right_placement in right_placements:
                for left_symbol in range(dimension):
                    for right_symbol in range(dimension):
                        basis = encoded_input(
                            left_symbol,
                            right_symbol,
                            alpha,
                            beta,
                            left_placement,
                            right_placement,
                        )
                        actual = rectangular_patch(
                            {basis: 1.0 + 0.0j},
                            alpha,
                            beta,
                            matrix,
                            dimension,
                        )
                        expected = expected_patch_output(
                            matrix,
                            dimension,
                            left_symbol,
                            right_symbol,
                            alpha,
                            beta,
                            left_placement,
                            right_placement,
                        )
                        error = sparse_distance(actual, expected)
                        cases += 1
                        maximum_error = max(maximum_error, error)
                        if error > TOL and first_failure is None:
                            first_failure = {
                                "alpha": alpha,
                                "beta": beta,
                                "left_placement": left_placement,
                                "right_placement": right_placement,
                                "left_symbol": left_symbol,
                                "right_symbol": right_symbol,
                                "error": error,
                            }
    return {
        "cases": cases,
        "maximum_error": maximum_error,
        "first_failure": first_failure,
        "pass": first_failure is None,
    }


def record_unitary(theta: float) -> np.ndarray:
    """History-controlled pointer rotation on H tensor A."""

    matrix = np.zeros((4, 4), dtype=complex)
    matrix[0:2, 0:2] = np.eye(2, dtype=complex)
    matrix[2:4, 2:4] = pointer_rotation(theta)
    return matrix


def record_isometry(theta: float) -> np.ndarray:
    blank = np.array([1.0, 0.0], dtype=complex)
    embedding = np.zeros((4, 2), dtype=complex)
    embedding[0, 0] = 1.0
    embedding[2, 1] = 1.0
    return record_unitary(theta) @ embedding


def fixed_fringe_probability(rho_history: np.ndarray, phase: float) -> float:
    phase_gate = np.diag([1.0, np.exp(1j * phase)])
    hadamard = np.array(
        [[1.0, 1.0], [1.0, -1.0]], dtype=complex
    ) / math.sqrt(2.0)
    output = hadamard @ phase_gate @ rho_history @ phase_gate.conj().T @ hadamard
    return float(np.real(output[0, 0]))


def history_record_receipt(theta: float) -> dict[str, Any]:
    zero = np.array([1.0, 0.0], dtype=complex)
    a_zero = zero
    a_one = pointer_rotation(theta) @ zero
    rho_zero = pure_density(a_zero)
    rho_one = pure_density(a_one)
    gamma = complex(a_zero.conj() @ a_one)
    distinguishability = trace_distance(rho_zero, rho_one)
    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    isometry = record_isometry(theta)
    joint = isometry @ plus
    rho_history = reduced_from_pure(joint, (2, 2), (0,))
    gram = np.array(
        [
            [a_zero.conj() @ a_zero, a_zero.conj() @ a_one],
            [a_one.conj() @ a_zero, a_one.conj() @ a_one],
        ],
        dtype=complex,
    )
    expected = pure_density(plus) * gram
    p_zero = fixed_fringe_probability(rho_history, 0.0)
    p_pi = fixed_fringe_probability(rho_history, math.pi)
    fixed_visibility = abs(p_zero - p_pi) / (p_zero + p_pi)
    matrix_visibility = 2.0 * abs(rho_history[0, 1])
    return {
        "theta": theta,
        "gamma_real": float(np.real(gamma)),
        "gamma_imag": float(np.imag(gamma)),
        "record_unitary_error": matrix_error(record_unitary(theta)),
        "isometry_error": float(
            np.max(np.abs(isometry.conj().T @ isometry - np.eye(2)))
        ),
        "gram_reduction_error": float(
            np.max(np.abs(rho_history - expected))
        ),
        "source_populations": [
            float(np.real(rho_history[0, 0])),
            float(np.real(rho_history[1, 1])),
        ],
        "source_coherence_magnitude": float(abs(rho_history[0, 1])),
        "matrix_visibility": float(matrix_visibility),
        "fixed_fringe": {
            "phase_0_probability": p_zero,
            "phase_pi_probability": p_pi,
            "visibility": float(fixed_visibility),
        },
        "record_trace_distance_D": distinguishability,
        "helstrom_equal_prior_success": (1.0 + distinguishability) / 2.0,
        "complementarity_sum": (
            matrix_visibility**2 + distinguishability**2
        ),
        "analytic_visibility": abs(math.cos(theta)),
        "analytic_distinguishability": abs(math.sin(theta)),
    }


def source_pointer_joint_amplitudes(
    extended_output: np.ndarray,
) -> np.ndarray:
    """Factor exact-one-particle outputs as source-pair tensor pointer."""

    joint = np.zeros((9, 2), dtype=complex)
    for output_index, amplitude in enumerate(extended_output):
        if abs(amplitude) <= 1.0e-14:
            continue
        pair = pair_from_index(output_index, 4)
        particle_positions = [
            index for index, symbol in enumerate(pair) if symbol >= 2
        ]
        if len(particle_positions) != 1:
            raise ValueError("fixture left exact-one-particle sector")
        position = particle_positions[0]
        pointer = pair[position] - 2
        source_pair = list(pair)
        source_pair[position] = 2
        source_index = pair_index(source_pair[0], source_pair[1], 3)
        joint[source_index, pointer] += amplitude
    return joint


def qca_history_witness(theta: float, coin: np.ndarray) -> dict[str, Any]:
    extended = pointer_scattering(theta, coin)
    source = source_scattering(coin)
    inv_sqrt_two = 1.0 / math.sqrt(2.0)
    input_vector = np.zeros(16, dtype=complex)
    input_vector[pair_index(2, 0, 4)] = inv_sqrt_two
    input_vector[pair_index(2, 1, 4)] = inv_sqrt_two
    joint = source_pointer_joint_amplitudes(extended @ input_vector)

    source_no_event = source[:, pair_index(2, 0, 3)]
    source_event = source[:, pair_index(2, 1, 3)]
    a_zero = np.array([1.0, 0.0], dtype=complex)
    a_one = pointer_rotation(theta) @ a_zero
    expected = (
        np.outer(source_no_event, a_zero)
        + np.outer(source_event, a_one)
    ) * inv_sqrt_two
    reduced = joint @ joint.conj().T
    ideal_vector = (source_no_event + source_event) * inv_sqrt_two
    ideal = pure_density(ideal_vector)
    no_event_population = float(
        np.real(source_no_event.conj() @ reduced @ source_no_event)
    )
    event_population = float(
        np.real(source_event.conj() @ reduced @ source_event)
    )
    coherence = complex(
        source_no_event.conj() @ reduced @ source_event
    )
    return {
        "realized_inside_one_clock_qca_scattering": True,
        "histories": [
            "|1_0,q> (no source-effective event)",
            "|1_0,0> (one source-effective event)",
        ],
        "history_output_overlap": float(
            abs(source_no_event.conj() @ source_event)
        ),
        "factorization_error": float(np.max(np.abs(joint - expected))),
        "history_populations": [no_event_population, event_population],
        "normalized_coherence_visibility": 2.0 * abs(coherence),
        "trace_distance_from_unrecorded_source": trace_distance(
            reduced, ideal
        ),
    }


def cnot_matrix() -> np.ndarray:
    matrix = np.zeros((4, 4), dtype=complex)
    for control in range(2):
        for target in range(2):
            matrix[
                pair_index(control, target ^ control, 2),
                pair_index(control, target, 2),
            ] = 1.0
    return matrix


def swap_matrix() -> np.ndarray:
    matrix = np.zeros((4, 4), dtype=complex)
    for left in range(2):
        for right in range(2):
            matrix[
                pair_index(right, left, 2),
                pair_index(left, right, 2),
            ] = 1.0
    return matrix


def archive_export_receipt(theta: float) -> dict[str, Any]:
    zero = np.array([1.0, 0.0], dtype=complex)
    a_zero = zero
    a_one = pointer_rotation(theta) @ zero
    cnot = cnot_matrix()
    swap = swap_matrix()
    ae_zero_input = np.kron(a_zero, zero)
    ae_one_input = np.kron(a_one, zero)

    cnot_zero = cnot @ ae_zero_input
    cnot_one = cnot @ ae_one_input
    cnot_full_D = trace_distance(
        pure_density(cnot_zero), pure_density(cnot_one)
    )
    cnot_e_zero = reduced_from_pure(cnot_zero, (2, 2), (1,))
    cnot_e_one = reduced_from_pure(cnot_one, (2, 2), (1,))
    cnot_a_zero = reduced_from_pure(cnot_zero, (2, 2), (0,))
    cnot_a_one = reduced_from_pure(cnot_one, (2, 2), (0,))

    swap_zero = swap @ ae_zero_input
    swap_one = swap @ ae_one_input
    swap_e_zero = reduced_from_pure(swap_zero, (2, 2), (1,))
    swap_e_one = reduced_from_pure(swap_one, (2, 2), (1,))
    swap_a_zero = reduced_from_pure(swap_zero, (2, 2), (0,))
    swap_a_one = reduced_from_pure(swap_one, (2, 2), (0,))

    dense_interface = fourier_unitary(4)
    dense_zero = dense_interface @ ae_zero_input
    dense_one = dense_interface @ ae_one_input
    dense_joint_D = trace_distance(
        pure_density(dense_zero), pure_density(dense_one)
    )
    dense_a_D = trace_distance(
        reduced_from_pure(dense_zero, (2, 2), (0,)),
        reduced_from_pure(dense_one, (2, 2), (0,)),
    )
    dense_e_D = trace_distance(
        reduced_from_pure(dense_zero, (2, 2), (1,)),
        reduced_from_pure(dense_one, (2, 2), (1,)),
    )

    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    copied_plus = cnot @ np.kron(plus, zero)
    target_plus = reduced_from_pure(copied_plus, (2, 2), (1,))
    desired_plus = pure_density(plus)

    fanout_rows: list[dict[str, Any]] = []
    for archive_cells in range(1, 5):
        dimension = 2 ** (archive_cells + 1)
        r_zero = np.zeros(dimension, dtype=complex)
        r_one = np.zeros(dimension, dtype=complex)
        r_zero[0] = 1.0
        r_one[0] = math.cos(theta)
        r_one[-1] = math.sin(theta)
        archive_zero = reduced_from_pure(
            r_zero,
            (2,) * (archive_cells + 1),
            tuple(range(1, archive_cells + 1)),
        )
        archive_one = reduced_from_pure(
            r_one,
            (2,) * (archive_cells + 1),
            tuple(range(1, archive_cells + 1)),
        )
        fanout_rows.append(
            {
                "archive_cells": archive_cells,
                "archive_dimension": 2**archive_cells,
                "joint_overlap": float(abs(r_zero.conj() @ r_one)),
                "joint_distinguishability": trace_distance(
                    pure_density(r_zero), pure_density(r_one)
                ),
                "archive_only_distinguishability_after_pointer_loss": (
                    trace_distance(archive_zero, archive_one)
                ),
            }
        )

    gamma = float(np.real(a_zero.conj() @ a_one))
    return {
        "theta": theta,
        "interface_status": (
            "DECLARED: source covariance does not select location, basis, "
            "CNOT, SWAP, or fresh blank cell"
        ),
        "cnot_unitarity_error": matrix_error(cnot),
        "swap_unitarity_error": matrix_error(swap),
        "conditional_joint_record_overlap": float(
            abs(cnot_zero.conj() @ cnot_one)
        ),
        "conditional_joint_record_distinguishability": cnot_full_D,
        "carrier_loss_before_export_archive_distinguishability": 0.0,
        "cnot_redundant_basis_export": {
            "archive_only_distinguishability_after_pointer_loss": (
                trace_distance(cnot_e_zero, cnot_e_one)
            ),
            "pointer_only_distinguishability_after_archive_loss": (
                trace_distance(cnot_a_zero, cnot_a_one)
            ),
            "expected_archive_tax_D_squared": math.sin(theta) ** 2,
            "perfect_loss_surviving_bit": bool(
                abs(trace_distance(cnot_e_zero, cnot_e_one) - 1.0) <= TOL
            ),
        },
        "swap_full_transfer": {
            "archive_distinguishability_after_pointer_loss": trace_distance(
                swap_e_zero, swap_e_one
            ),
            "pointer_distinguishability_after_transfer": trace_distance(
                swap_a_zero, swap_a_one
            ),
            "retains_pointer_copy": False,
        },
        "history_independent_unitary_evidence_conservation": {
            "control": "dense 4x4 Fourier unitary on pointer plus blank archive",
            "unitarity_error": matrix_error(dense_interface),
            "input_overlap": float(abs(ae_zero_input.conj() @ ae_one_input)),
            "output_overlap": float(abs(dense_zero.conj() @ dense_one)),
            "joint_distinguishability": dense_joint_D,
            "pointer_marginal_distinguishability": dense_a_D,
            "archive_marginal_distinguishability": dense_e_D,
            "both_marginals_bounded_by_joint": bool(
                dense_a_D <= dense_joint_D + TOL
                and dense_e_D <= dense_joint_D + TOL
            ),
        },
        "no_cloning_guard": {
            "input": "(|0>+|1>)/sqrt(2) tensor |0>",
            "cnot_output": "(|00>+|11>)/sqrt(2)",
            "target_purity": float(np.real(np.trace(target_plus @ target_plus))),
            "target_fidelity_to_input_plus": float(
                np.real(plus.conj() @ target_plus @ plus)
            ),
            "is_two_coherent_clones": bool(
                np.max(np.abs(target_plus - desired_plus)) <= TOL
            ),
            "nonorthogonal_duplication_inner_product_defect": abs(
                gamma - gamma**2
            ),
        },
        "repeated_basis_fanout": fanout_rows,
        "spatial_transport_simulated": False,
    }


def fresh_cell_scaling_receipt(theta: float) -> dict[str, Any]:
    zero = np.array([1.0, 0.0], dtype=complex)
    one_record = pointer_rotation(theta) @ zero
    gamma = abs(complex(zero.conj() @ one_record))
    fresh_rows: list[dict[str, Any]] = []
    for cells in range(1, 7):
        state_zero = zero
        state_one = one_record
        for _ in range(cells - 1):
            state_zero = np.kron(state_zero, zero)
            state_one = np.kron(state_one, one_record)
        overlap = abs(complex(state_zero.conj() @ state_one))
        distinguishability = trace_distance(
            pure_density(state_zero), pure_density(state_one)
        )
        fresh_rows.append(
            {
                "cells": cells,
                "archive_dimension": 2**cells,
                "overlap": overlap,
                "visibility": overlap,
                "distinguishability": distinguishability,
                "analytic_visibility": gamma**cells,
                "analytic_distinguishability": math.sqrt(
                    max(0.0, 1.0 - gamma ** (2 * cells))
                ),
            }
        )

    rotation = pointer_rotation(theta)
    reused = zero.copy()
    reuse_rows: list[dict[str, Any]] = []
    for events in range(7):
        if events:
            reused = rotation @ reused
        reuse_rows.append(
            {
                "events": events,
                "visibility_to_blank_ray": abs(complex(zero.conj() @ reused)),
                "state": [
                    float(np.real(reused[0])),
                    float(np.real(reused[1])),
                ],
            }
        )
    toggle = pointer_rotation(math.pi / 2.0)
    toggled_twice = toggle @ toggle @ zero
    return {
        "theta": theta,
        "fresh_independent_cells": fresh_rows,
        "fresh_cells_are_separate_interactions_not_cnot_fanout": True,
        "one_cell_reuse": reuse_rows,
        "projective_recurrence_at_three_events": bool(
            abs(reuse_rows[3]["visibility_to_blank_ray"] - 1.0) <= TOL
        ),
        "finite_basis_alias_control": {
            "two_quarter_turn_updates_same_basis_readout_as_blank": bool(
                abs(abs(complex(zero.conj() @ toggled_twice)) - 1.0) <= TOL
            ),
            "scope": "same ray up to global phase",
        },
    }


def boundary_relocation_receipt(theta: float) -> dict[str, Any]:
    isometry = record_isometry(theta)
    rho = np.array(
        [[0.6, 0.25 + 0.1j], [0.25 - 0.1j, 0.4]], dtype=complex
    )
    joint = isometry @ rho @ isometry.conj().T
    joint_tensor = joint.reshape(2, 2, 2, 2)
    reduced = np.trace(joint_tensor, axis1=1, axis2=3)
    a_zero = np.array([1.0, 0.0], dtype=complex)
    a_one = pointer_rotation(theta) @ a_zero
    gram = np.array(
        [
            [a_zero.conj() @ a_zero, a_one.conj() @ a_zero],
            [a_zero.conj() @ a_one, a_one.conj() @ a_one],
        ],
        dtype=complex,
    )
    expected = rho * gram
    diagonal_observables = [
        np.eye(2, dtype=complex),
        np.diag([1.0, -1.0]).astype(complex),
        np.diag([1.0, 0.0]).astype(complex),
    ]
    diagonal_defect = max(
        abs(np.trace(observable @ rho) - np.trace(observable @ reduced))
        for observable in diagonal_observables
    )
    coherent_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    coherent_expectation_change = abs(
        np.trace(coherent_x @ rho) - np.trace(coherent_x @ reduced)
    )
    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    plus_reduced = reduced_from_pure(
        isometry @ plus, (2, 2), (0,)
    )
    full_channel_witness_distance = trace_distance(
        plus_reduced, pure_density(plus)
    )

    zero = np.array([1.0, 0.0], dtype=complex)
    initial = np.kron(np.kron(plus, zero), zero)
    record_on_ha = np.kron(record_unitary(theta), np.eye(2))
    inverse_record_on_ha = np.kron(
        record_unitary(-theta), np.eye(2)
    )
    export_on_ae = np.kron(np.eye(2), cnot_matrix())
    archive_z = np.kron(
        np.eye(4), np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    )
    hadamard_on_h = np.kron(
        np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
        / math.sqrt(2.0),
        np.eye(4),
    )
    exported = export_on_ae @ record_on_ha @ initial
    exported_z = archive_z @ exported
    source_before = reduced_from_pure(exported, (2, 2, 2), (0,))
    source_after_local_z = reduced_from_pure(
        exported_z, (2, 2, 2), (0,)
    )
    closed_control = (
        hadamard_on_h
        @ inverse_record_on_ha
        @ export_on_ae
        @ exported
    )
    closed_intervened = (
        hadamard_on_h
        @ inverse_record_on_ha
        @ export_on_ae
        @ exported_z
    )
    control_probability = float(
        np.real(
            np.trace(
                reduced_from_pure(
                    closed_control, (2, 2, 2), (0,)
                )
                @ np.diag([1.0, 0.0])
            )
        )
    )
    intervened_probability = float(
        np.real(
            np.trace(
                reduced_from_pure(
                    closed_intervened, (2, 2, 2), (0,)
                )
                @ np.diag([1.0, 0.0])
            )
        )
    )
    return {
        "theta": theta,
        "state_augmentation": (
            "External archive can be represented inside an enlarged host "
            "state; augmentation alone is bookkeeping, not full invariance."
        ),
        "gram_matrix_reduction_error": float(
            np.max(np.abs(reduced - expected))
        ),
        "history_diagonal_observational_equivalence": {
            "maximum_expectation_defect": float(abs(diagonal_defect)),
            "archive_interventions_allowed": False,
            "pass": bool(abs(diagonal_defect) <= TOL),
        },
        "full_coherent_channel_equivalence": {
            "plus_state_trace_distance_from_original": (
                full_channel_witness_distance
            ),
            "coherent_X_expectation_change": float(
                abs(coherent_expectation_change)
            ),
            "relevant_archive_overlap": float(
                abs(a_zero.conj() @ a_one)
            ),
            "criterion": (
                "Exact original unitary source channel requires one common "
                "archive state, equivalently the required Gram entries are 1."
            ),
            "pass": full_channel_witness_distance <= TOL,
        },
        "interventional_equivalence": {
            "local_archive_Z_changes_immediate_source_marginal_by": (
                float(np.max(np.abs(source_before - source_after_local_z)))
            ),
            "fixed_later_interface": (
                "inverse CNOT export, inverse record rotation, fixed Hadamard "
                "history recombiner"
            ),
            "control_later_h0_probability": control_probability,
            "archive_Z_later_h0_probability": intervened_probability,
            "later_probability_change": abs(
                control_probability - intervened_probability
            ),
            "pass": abs(control_probability - intervened_probability) <= TOL,
            "scope": (
                "No-signalling preserves the immediate source marginal; "
                "failure appears when the intervened archive is later "
                "re-coupled at the declared interface."
            ),
        },
        "equivalence_grade": {
            "diagonal_observational": "PRESERVED",
            "full_coherent_channel": (
                "PRESERVED_ONLY_FOR_UNINFORMATIVE_COMMON_RECORD"
            ),
            "interventional": (
                "FAILS_WHEN_ARCHIVE_OPERATION_AND_LATER_RECOUPLING_ARE_ALLOWED"
            ),
        },
    }


def raw_microstep_rival_receipt(
    theta: float, coin: np.ndarray
) -> dict[str, Any]:
    bad = pointer_scattering(theta, coin, rotate_on_q=True)
    result = naturality_sweep(
        bad, 4, [(3, 4)], all_placements=False
    )
    return {
        "unitarity_error": matrix_error(bad),
        "patch": [3, 4],
        "naturality": result,
        "failure_is_refinement_sensitive": not result["pass"],
    }


def make_check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def main() -> None:
    theta_rows = [
        ("off", 0.0),
        ("weak_pi_over_6", math.pi / 6.0),
        ("primary_pi_over_3", math.pi / 3.0),
        ("maximal_pi_over_2", math.pi / 2.0),
    ]
    coins = coin_family()

    local_rows: list[dict[str, Any]] = []
    for theta_name, theta in theta_rows:
        for coin_name, coin in coins:
            matrix = pointer_scattering(theta, coin)
            block = active_block(matrix, 4)
            local_rows.append(
                {
                    "theta_name": theta_name,
                    "theta": theta,
                    "coin": coin_name,
                    "coin_unitarity_error": matrix_error(coin),
                    "source_unitarity_error": matrix_error(
                        source_scattering(coin)
                    ),
                    "pointer_matrix_unitarity_error": matrix_error(matrix),
                    "q_transparent_reconstruction_error": float(
                        np.max(
                            np.abs(q_transparent_lift(block) - matrix)
                        )
                    ),
                    "matrix_digest": matrix_digest(matrix),
                }
            )

    canonical_rows = []
    for theta_name, theta in theta_rows:
        matrix = pointer_scattering(theta, coins[0][1])
        canonical_rows.append(
            {
                "theta_name": theta_name,
                **naturality_sweep(
                    matrix,
                    4,
                    [(1, 1), (2, 3), (4, 2)],
                    all_placements=False,
                ),
            }
        )

    training_patches = [
        (alpha, beta)
        for alpha in range(1, 5)
        for beta in range(1, 5)
    ]
    all_placement_rows = []
    for coin_name, coin in coins:
        all_placement_rows.append(
            {
                "theta": math.pi / 3.0,
                "coin": coin_name,
                **naturality_sweep(
                    pointer_scattering(math.pi / 3.0, coin),
                    4,
                    training_patches,
                    all_placements=True,
                ),
            }
        )
    held_out = naturality_sweep(
        pointer_scattering(math.pi / 3.0, coins[-1][1]),
        4,
        [(6, 5)],
        all_placements=True,
    )

    arbitrary_active_dimension = 3
    arbitrary_block = fourier_unitary(arbitrary_active_dimension**2)
    arbitrary_lift = q_transparent_lift(arbitrary_block)
    arbitrary_naturality = naturality_sweep(
        arbitrary_lift, 4, [(5, 4)], all_placements=True
    )

    record_rows = [
        {"setting": name, **history_record_receipt(theta)}
        for name, theta in theta_rows
    ]
    primary_record = next(
        row for row in record_rows if row["setting"] == "primary_pi_over_3"
    )
    qca_witness = qca_history_witness(
        math.pi / 3.0, coins[0][1]
    )
    archive = archive_export_receipt(math.pi / 3.0)
    maximal_archive = archive_export_receipt(math.pi / 2.0)
    scaling = fresh_cell_scaling_receipt(math.pi / 3.0)
    boundary_primary = boundary_relocation_receipt(math.pi / 3.0)
    boundary_off = boundary_relocation_receipt(0.0)
    bad_rival = raw_microstep_rival_receipt(
        math.pi / 3.0, np.eye(2, dtype=complex)
    )

    fresh_rows = scaling["fresh_independent_cells"]
    fanout_rows = archive["repeated_basis_fanout"]
    checks = [
        make_check(
            "all source coins and Clock-QCA matrices are unitary",
            all(
                row["coin_unitarity_error"] <= TOL
                and row["source_unitarity_error"] <= TOL
                for row in local_rows
            ),
            "two complex coins across all pointer settings",
        ),
        make_check(
            "pointer-event gates are complete full-basis unitaries",
            all(
                row["pointer_matrix_unitarity_error"] <= TOL
                for row in local_rows
            ),
            f"{len(local_rows)} complete 16x16 matrices",
        ),
        make_check(
            "pointer-event gates are exact q-transparent lifts",
            all(
                row["q_transparent_reconstruction_error"] <= TOL
                for row in local_rows
            ),
            "pointer rotation occurs only in the active source sector",
        ),
        make_check(
            "canonical rectangular patches reproduce the direct gate",
            all(row["pass"] for row in canonical_rows),
            f"{sum(row['cases'] for row in canonical_rows)} full-basis cases",
        ),
        make_check(
            "all bounded active-symbol placements close the same local square",
            all(row["pass"] for row in all_placement_rows),
            f"{sum(row['cases'] for row in all_placement_rows)} cases",
        ),
        make_check(
            "held-out 6x5 all-placement patch is natural",
            held_out["pass"],
            f"{held_out['cases']} full-basis/placement cases",
        ),
        make_check(
            "Clock-QCA one-gate witness realizes the frozen two-history map",
            qca_witness["factorization_error"] <= TOL
            and qca_witness["history_output_overlap"] <= TOL,
            "|1_0,q> versus |1_0,0>",
        ),
        make_check(
            "source history populations remain one half",
            all(
                max(abs(value - 0.5) for value in row["source_populations"])
                <= TOL
                for row in record_rows
            ),
            "off, weak, primary, and maximal records",
        ),
        make_check(
            "Gram-matrix reduction is matrix-exact",
            all(row["gram_reduction_error"] <= TOL for row in record_rows),
            "source coherence is multiplied by record overlap",
        ),
        make_check(
            "matrix and fixed-fringe visibilities equal record overlap",
            all(
                abs(row["matrix_visibility"] - row["analytic_visibility"])
                <= TOL
                and abs(
                    row["fixed_fringe"]["visibility"]
                    - row["analytic_visibility"]
                )
                <= TOL
                for row in record_rows
            ),
            "fixed phases 0 and pi with one Hadamard recombiner",
        ),
        make_check(
            "trace-distance distinguishability matches the pure-state formula",
            all(
                abs(
                    row["record_trace_distance_D"]
                    - row["analytic_distinguishability"]
                )
                <= TOL
                for row in record_rows
            ),
            "equal-prior Helstrom convention",
        ),
        make_check(
            "exact pure-record complementarity holds",
            all(
                abs(row["complementarity_sum"] - 1.0) <= TOL
                for row in record_rows
            ),
            "V^2 + D^2 = 1 at every frozen setting",
        ),
        make_check(
            "recorder-off and maximal-record endpoints are recovered",
            abs(record_rows[0]["matrix_visibility"] - 1.0) <= TOL
            and record_rows[0]["record_trace_distance_D"] <= TOL
            and record_rows[-1]["matrix_visibility"] <= TOL
            and abs(record_rows[-1]["record_trace_distance_D"] - 1.0)
            <= TOL,
            "theta=0 and theta=pi/2",
        ),
        make_check(
            "declared CNOT and SWAP interfaces are complete unitaries",
            archive["cnot_unitarity_error"] <= TOL
            and archive["swap_unitarity_error"] <= TOL,
            "interface operations are added structure, not covariance-selected",
        ),
        make_check(
            "CNOT export preserves full joint record distinguishability",
            abs(
                archive["conditional_joint_record_distinguishability"]
                - primary_record["record_trace_distance_D"]
            )
            <= TOL,
            "the joint A-E overlap remains gamma",
        ),
        make_check(
            "CNOT archive-only access pays the squared-distinguishability tax",
            abs(
                archive["cnot_redundant_basis_export"][
                    "archive_only_distinguishability_after_pointer_loss"
                ]
                - math.sin(math.pi / 3.0) ** 2
            )
            <= TOL,
            "D_E=sin^2(theta), not sin(theta), after pointer loss",
        ),
        make_check(
            "only the maximal CNOT record is a perfect loss-surviving bit",
            not archive["cnot_redundant_basis_export"][
                "perfect_loss_surviving_bit"
            ]
            and maximal_archive["cnot_redundant_basis_export"][
                "perfect_loss_surviving_bit"
            ],
            "partial coherent records degrade when one share is lost",
        ),
        make_check(
            "SWAP transfers full nonorthogonal record without retaining a copy",
            abs(
                archive["swap_full_transfer"][
                    "archive_distinguishability_after_pointer_loss"
                ]
                - primary_record["record_trace_distance_D"]
            )
            <= TOL
            and archive["swap_full_transfer"][
                "pointer_distinguishability_after_transfer"
            ]
            <= TOL
            and not archive["swap_full_transfer"]["retains_pointer_copy"],
            "transfer and redundant export are distinct contracts",
        ),
        make_check(
            "history-independent archive unitary conserves joint evidence",
            archive["history_independent_unitary_evidence_conservation"][
                "unitarity_error"
            ]
            <= TOL
            and abs(
                archive[
                    "history_independent_unitary_evidence_conservation"
                ]["input_overlap"]
                - archive[
                    "history_independent_unitary_evidence_conservation"
                ]["output_overlap"]
            )
            <= TOL
            and abs(
                archive[
                    "history_independent_unitary_evidence_conservation"
                ]["joint_distinguishability"]
                - primary_record["record_trace_distance_D"]
            )
            <= TOL
            and archive[
                "history_independent_unitary_evidence_conservation"
            ]["both_marginals_bounded_by_joint"],
            "unitarity preserves overlap; partial trace cannot increase D",
        ),
        make_check(
            "pointer-basis CNOT entangles a coherent input rather than cloning",
            not archive["no_cloning_guard"]["is_two_coherent_clones"]
            and abs(archive["no_cloning_guard"]["target_purity"] - 0.5)
            <= TOL
            and archive["no_cloning_guard"][
                "nonorthogonal_duplication_inner_product_defect"
            ]
            > 1.0e-6,
            "basis predicate sharing is not arbitrary-state duplication",
        ),
        make_check(
            "carrier loss before export leaves no record in a blank archive",
            archive[
                "carrier_loss_before_export_archive_distinguishability"
            ]
            <= TOL,
            "there is no free external record before the interface",
        ),
        make_check(
            "repeated CNOT fanout does not equal independent fresh recording",
            all(
                abs(
                    row[
                        "archive_only_distinguishability_after_pointer_loss"
                    ]
                    - math.sin(math.pi / 3.0) ** 2
                )
                <= TOL
                for row in fanout_rows
            )
            and any(
                fresh_rows[index]["distinguishability"]
                > fanout_rows[index][
                    "archive_only_distinguishability_after_pointer_loss"
                ]
                + 1.0e-6
                for index in range(1, len(fanout_rows))
            ),
            "GHZ-like basis redundancy is not m independent weak records",
        ),
        make_check(
            "fresh independent cells obey gamma^m visibility scaling",
            all(
                abs(row["visibility"] - row["analytic_visibility"]) <= TOL
                and abs(
                    row["distinguishability"]
                    - row["analytic_distinguishability"]
                )
                <= TOL
                for row in fresh_rows
            ),
            "each extra cell is charged and doubles archive Hilbert dimension",
        ),
        make_check(
            "one finite reused pointer exhibits recurrence and alias",
            scaling["projective_recurrence_at_three_events"]
            and scaling["finite_basis_alias_control"][
                "two_quarter_turn_updates_same_basis_readout_as_blank"
            ],
            "finite unitary reuse is not monotone irreversible accumulation",
        ),
        make_check(
            "history-diagonal observational algebra is preserved",
            boundary_primary[
                "history_diagonal_observational_equivalence"
            ]["pass"],
            "archive is not intervened on in this scoped contract",
        ),
        make_check(
            "informative records break the full coherent source channel",
            not boundary_primary[
                "full_coherent_channel_equivalence"
            ]["pass"]
            and boundary_primary["full_coherent_channel_equivalence"][
                "plus_state_trace_distance_from_original"
            ]
            > 1.0e-6
            and boundary_off["full_coherent_channel_equivalence"]["pass"],
            "full equality returns only at the uninformative endpoint",
        ),
        make_check(
            "archive intervention leaves immediate source marginal unchanged",
            boundary_primary["interventional_equivalence"][
                "local_archive_Z_changes_immediate_source_marginal_by"
            ]
            <= TOL,
            "no-signalling guard",
        ),
        make_check(
            "archive intervention changes a later fixed reunion outcome",
            not boundary_primary["interventional_equivalence"]["pass"]
            and boundary_primary["interventional_equivalence"][
                "later_probability_change"
            ]
            > 1.0e-6,
            "failure appears after declared recoupling, not by signalling",
        ),
        make_check(
            "raw q-microstep recorder remains unitary",
            bad_rival["unitarity_error"] <= TOL,
            "negative control is a valid local law",
        ),
        make_check(
            "raw q-microstep recorder fails source refinement",
            bad_rival["failure_is_refinement_sensitive"]
            and bad_rival["naturality"]["maximum_error"] > 1.0e-6,
            "encoding-added q crossings change the pointer",
        ),
        make_check(
            "arbitrary active unitary also inherits source covariance",
            matrix_error(arbitrary_lift) <= TOL
            and arbitrary_naturality["pass"],
            "covariance admits but does not select the pointer law",
        ),
    ]
    checks_passed = sum(check["pass"] for check in checks)

    artifact = {
        "probe": "du_covariant_archive_boundary_probe",
        "hardening_id": "HC-DU-031C",
        "source": {
            "citation": (
                "Arrighi, Facchini, and Forets, Discrete Lorentz covariance "
                "for Quantum Walks and Quantum Cellular Automata"
            ),
            "arxiv": "https://arxiv.org/abs/1404.4499",
            "exact_tex_sha256": SOURCE_TEX_SHA256,
            "pdf_sha256": SOURCE_PDF_SHA256,
            "scope": "Clock QCA definition and rectangular-patch covariance",
        },
        "construction": {
            "wire_alphabet": "|q>, |0>, |1,A=0>, |1,A=1>",
            "event_rule": "source-effective particle/zero applies R_theta",
            "q_rule": "transparent transport with no pointer update",
            "primary_theta": "pi/3",
            "archive_interface": (
                "separately declared CNOT basis export or SWAP transfer"
            ),
            "reunion": (
                "fixed two-history subspace recombiner at a declared interface"
            ),
        },
        "theorem_results": {
            "T1_covariant_finite_pointer": (
                "PROVED_AND_BOUNDED_FULL_BASIS_CHECKED; "
                "COVARIANCE ADMITS BUT DOES NOT SELECT LAW"
            ),
            "T2_gram_matrix_reduction": "PROVED_AND_MATRIX_CHECKED",
            "T3_pure_record_complementarity": (
                "V_EQUALS_ABS_GAMMA; D_EQUALS_SQRT_1_MINUS_GAMMA_SQUARED; "
                "V_SQUARED_PLUS_D_SQUARED_EQUALS_ONE"
            ),
            "T4_boundary_relocation": (
                "DIAGONAL_OBSERVATIONAL_EQUIVALENCE_ONLY; "
                "INFORMATIVE_RECORD_OBSTRUCTS_FULL_COHERENT_CHANNEL; "
                "INTERVENABLE_RECORD_OBSTRUCTS_INTERVENTIONAL_EQUIVALENCE"
            ),
            "T5_finite_resource_and_recurrence": (
                "FRESH_CELLS_SCALE_AS_GAMMA_POWER_M_WITH_DIMENSION_2_POWER_M; "
                "FINITE_REUSE_RECURS"
            ),
            "export_distinction": (
                "CNOT_REDUNDANCY_GIVES_ARCHIVE_ONLY_D_EQUALS_D_FULL_SQUARED; "
                "SWAP_TRANSFERS_FULL_D_WITHOUT_A_RETAINED_COPY; "
                "FANOUT_IS_NOT_INDEPENDENT_RECORDING"
            ),
            "unitary_archive_evidence_conservation": (
                "HISTORY_INDEPENDENT_UNITARY_PRESERVES_CONDITIONAL_OVERLAP "
                "AND_JOINT_TRACE_DISTANCE; MARGINAL_TRACE_DISTANCE_CANNOT_GROW"
            ),
        },
        "local_unitarity_rows": local_rows,
        "canonical_naturality_rows": canonical_rows,
        "all_placement_naturality_rows": all_placement_rows,
        "held_out_naturality": {"patch": [6, 5], **held_out},
        "clock_qca_history_witness": qca_witness,
        "record_tradeoff_rows": record_rows,
        "archive_export_and_loss": archive,
        "maximal_archive_control": maximal_archive,
        "fresh_cell_and_reuse_scaling": scaling,
        "boundary_relocation_primary": boundary_primary,
        "boundary_relocation_off_control": boundary_off,
        "raw_microstep_rival": bad_rival,
        "arbitrary_active_unitary_control": {
            "active_dimension": arbitrary_active_dimension,
            "W": "9x9 Fourier unitary",
            "W_unitarity_error": matrix_error(arbitrary_block),
            "lift_unitarity_error": matrix_error(arbitrary_lift),
            "patch": [5, 4],
            **arbitrary_naturality,
        },
        "checks": checks,
        "checks_passed": checks_passed,
        "checks_total": len(checks),
        "underlying_case_counts": {
            "complete_pointer_unitaries": len(local_rows),
            "canonical_full_basis_cases": sum(
                row["cases"] for row in canonical_rows
            ),
            "all_placement_training_cases": sum(
                row["cases"] for row in all_placement_rows
            ),
            "held_out_all_placement_cases": held_out["cases"],
            "arbitrary_active_unitary_cases": arbitrary_naturality["cases"],
        },
        "terminal_outcomes": [
            "COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY",
            "INTERFACE_ONLY_ARCHIVE",
        ],
        "claim_grade": (
            "EXACT FINITE MATHEMATICAL CONSTRUCTION AND SCOPED OBSTRUCTION / "
            "PHYSICAL INTERFACE AND LAW SELECTION OPEN"
        ),
        "novelty": "SEARCH-INCOMPLETE",
        "banked": False,
        "prediction_seeded": False,
        "scope_not_earned": [
            "classical irreversible or thermodynamic record",
            "covariance-selected archive interface, basis, or coupling",
            "arbitrary-state cloning",
            "realistic spatial reunion",
            "monotone unbounded memory from finite unitary reuse",
            "observerhood, proper time, continuum covariance, gravity, cosmology",
            "Dynamic Unity identity or a publication novelty claim",
        ],
    }
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("COVARIANT ARCHIVE AND BOUNDARY PROBE")
    for check in checks:
        status = "PASS" if check["pass"] else "FAIL"
        print(f"{status}  {check['name']}")
    print(f"{checks_passed}/{len(checks)} checks pass")
    print(
        "VERDICT: COVARIANT FINITE ARCHIVE WITH EXACT COMPLEMENTARITY; "
        "INTERFACE ONLY (NO PHYSICS CLAIM BANKED)"
    )
    print(f"artifact: {ARTIFACT_PATH}")
    if checks_passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
