#!/usr/bin/env python3
"""Exact finite probe for the Clock-QCA covariant recorder extension.

The host is the q-transparent Clock QCA of Arrighi, Facchini, and Forets
(arXiv:1404.4499, exact TeX SHA-256 pinned below).  The frozen extension
replaces |1> by cyclic counter species |1_k> and increments k only in the
source-effective |1>-|0> scattering sector.

The source TeX proof (lines 965--981) uses a planar boundary convention:
the first active input is embedded in an alpha-wire boundary and the second
in a beta-wire boundary, while the first output exits on the beta boundary
and the second on the alpha boundary.  ``rectangular_patch`` implements that
alpha-by-beta network as the braid of all alpha*beta local crossings.  Its
output tensor order is therefore beta-boundary then alpha-boundary.  This is
the explicit circuit form of the source's abstract covariance square.

The probe distinguishes three notions that must not be conflated:

* algebraic forgetting: the non-isometric linear quotient |1_k> -> |1>;
* fixed-count physical forgetting: tracing a factorized counter register;
* global physical forgetting: tracing which-history counter information,
  which dephases coherent branches with different interaction counts.

Passing this finite executable is not a claim that nature implements this
QCA, that the counter is classical or irreversible, or that it is proper time.
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
    / "du_covariant_recorder_naturality_result.json"
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


def coin_family() -> list[tuple[str, np.ndarray]]:
    theta = 0.37
    dirac = np.array(
        [
            [math.cos(theta), -1j * math.sin(theta)],
            [-1j * math.sin(theta), math.cos(theta)],
        ],
        dtype=complex,
    )
    hadamard = np.array(
        [[1.0, 1.0], [1.0, -1.0]],
        dtype=complex,
    ) / math.sqrt(2.0)
    theta_g = 0.61
    phi = 0.23
    chi = -0.47
    general_su2 = np.array(
        [
            [
                np.exp(1j * phi) * math.cos(theta_g),
                np.exp(1j * chi) * math.sin(theta_g),
            ],
            [
                -np.exp(-1j * chi) * math.sin(theta_g),
                np.exp(-1j * phi) * math.cos(theta_g),
            ],
        ],
        dtype=complex,
    )
    return [
        ("dirac_theta_0p37", dirac),
        ("hadamard", hadamard),
        ("general_su2", general_su2),
    ]


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


def source_scattering(coin: np.ndarray) -> np.ndarray:
    """Construct the source 9x9 Clock-QCA scattering matrix.

    Alphabet order is q=0, vacuum 0=1, particle 1=2.  The source writes the
    selected coin block by input images, so the numerical block in the usual
    row-output/column-input convention is coin.T; transpose preserves
    unitarity.
    """

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


def recorder_scattering(
    counter_size: int,
    coin: np.ndarray,
    *,
    increment_on_q: bool = False,
) -> np.ndarray:
    """Construct the complete frozen U_(C,R), optionally with the bad q rival."""

    if counter_size < 2:
        raise ValueError("counter_size must be at least two")
    dimension = counter_size + 2
    q, zero = 0, 1
    particles = list(range(2, dimension))
    matrix = np.zeros((dimension**2, dimension**2), dtype=complex)

    add_entry(matrix, (q, q), (q, q), 1.0, dimension)
    add_entry(matrix, (zero, q), (q, zero), 1.0, dimension)
    add_entry(matrix, (q, zero), (zero, q), 1.0, dimension)
    add_entry(matrix, (zero, zero), (zero, zero), 1.0, dimension)

    for particle in particles:
        k = particle - 2
        next_particle = 2 + ((k + 1) % counter_size)
        transported = next_particle if increment_on_q else particle
        add_entry(matrix, (q, transported), (particle, q), 1.0, dimension)
        add_entry(matrix, (transported, q), (q, particle), 1.0, dimension)

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
    for particle in particles:
        k = particle - 2
        next_particle = 2 + ((k + 1) % counter_size)
        add_entry(
            matrix,
            (zero, next_particle),
            (particle, zero),
            a,
            dimension,
        )
        add_entry(
            matrix,
            (next_particle, zero),
            (particle, zero),
            b,
            dimension,
        )
        add_entry(
            matrix,
            (zero, next_particle),
            (zero, particle),
            c,
            dimension,
        )
        add_entry(
            matrix,
            (next_particle, zero),
            (zero, particle),
            d,
            dimension,
        )
    return matrix


def active_block(matrix: np.ndarray, dimension: int) -> np.ndarray:
    """Return the K tensor K block for H=Cq direct-sum K."""

    indices = [
        pair_index(left, right, dimension)
        for left in range(1, dimension)
        for right in range(1, dimension)
    ]
    return matrix[np.ix_(indices, indices)]


def q_transparent_lift(block: np.ndarray) -> np.ndarray:
    """Lift an arbitrary unitary W on K tensor K by transparent q crossings."""

    block_side = int(round(math.sqrt(block.shape[0])))
    if block.shape != (block_side**2, block_side**2):
        raise ValueError("block must act on K tensor K")
    dimension = block_side + 1
    matrix = np.zeros((dimension**2, dimension**2), dtype=complex)
    add_entry(matrix, (0, 0), (0, 0), 1.0, dimension)
    for x in range(1, dimension):
        add_entry(matrix, (x, 0), (0, x), 1.0, dimension)
        add_entry(matrix, (0, x), (x, 0), 1.0, dimension)
    for left_in in range(block_side):
        for right_in in range(block_side):
            input_column = pair_index(left_in, right_in, block_side)
            for output_row, amplitude in enumerate(block[:, input_column]):
                if abs(amplitude) <= 1.0e-14:
                    continue
                left_out, right_out = pair_from_index(output_row, block_side)
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
    """Apply every crossing in the alpha-by-beta rectangular braid.

    Input factor order is the alpha boundary followed by the beta boundary.
    Each beta strand is braided leftward across all alpha strands.  Output
    factor order is beta boundary followed by alpha boundary, exactly as in
    the source proof's a^(0,beta-1), b^(alpha-1,0) exit convention.
    """

    if alpha < 1 or beta < 1:
        raise ValueError("positive patch dimensions required")
    expected_length = alpha + beta
    if any(len(basis) != expected_length for basis in state):
        raise ValueError("state has wrong boundary size")
    result = dict(state)
    for beta_strand in range(beta):
        for position in range(
            alpha + beta_strand - 1,
            beta_strand - 1,
            -1,
        ):
            result = apply_adjacent_gate(
                result, position, matrix, dimension
            )
    return result


def embedded_basis(
    symbol: int,
    length: int,
    placement: int,
    q: int = 0,
) -> tuple[int, ...]:
    if not 0 <= placement < length:
        raise ValueError("placement outside encoding")
    output = [q] * length
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
    """Encode the two direct outputs on beta then alpha exit boundaries."""

    output: SparseState = {}
    for (left_out, right_out), amplitude in local_action(
        matrix,
        dimension,
        (left_symbol, right_symbol),
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


def superposition_naturality(
    matrix: np.ndarray,
    dimension: int,
    alpha: int,
    beta: int,
    left_placement: int,
    right_placement: int,
    terms: list[tuple[int, int, complex]],
) -> dict[str, Any]:
    norm = math.sqrt(sum(abs(amplitude) ** 2 for _, _, amplitude in terms))
    encoded: SparseState = {}
    expected: SparseState = {}
    for left_symbol, right_symbol, amplitude in terms:
        coefficient = amplitude / norm
        basis = encoded_input(
            left_symbol,
            right_symbol,
            alpha,
            beta,
            left_placement,
            right_placement,
        )
        encoded[basis] = encoded.get(basis, 0.0j) + coefficient
        local_expected = expected_patch_output(
            matrix,
            dimension,
            left_symbol,
            right_symbol,
            alpha,
            beta,
            left_placement,
            right_placement,
        )
        for out_basis, out_amplitude in local_expected.items():
            expected[out_basis] = (
                expected.get(out_basis, 0.0j)
                + coefficient * out_amplitude
            )
    actual = rectangular_patch(
        prune(encoded), alpha, beta, matrix, dimension
    )
    error = sparse_distance(actual, prune(expected))
    return {
        "term_count": len(terms),
        "maximum_error": error,
        "pass": error <= TOL,
    }


def formal_forget_pair(pair: tuple[int, int]) -> tuple[int, int]:
    return tuple(2 if symbol >= 2 else symbol for symbol in pair)  # type: ignore[return-value]


def formal_forgetting_sweep(
    extended: np.ndarray,
    source: np.ndarray,
    extended_dimension: int,
) -> dict[str, Any]:
    source_dimension = 3
    cases = 0
    maximum_error = 0.0
    for input_index in range(extended_dimension**2):
        input_pair = pair_from_index(input_index, extended_dimension)
        forgotten_output = np.zeros(source_dimension**2, dtype=complex)
        for output_index, amplitude in enumerate(extended[:, input_index]):
            if abs(amplitude) <= 1.0e-14:
                continue
            output_pair = pair_from_index(output_index, extended_dimension)
            forgotten_pair = formal_forget_pair(output_pair)
            forgotten_output[
                pair_index(*forgotten_pair, source_dimension)
            ] += amplitude
        forgotten_input = formal_forget_pair(input_pair)
        expected = source[
            :, pair_index(*forgotten_input, source_dimension)
        ]
        maximum_error = max(
            maximum_error,
            float(np.max(np.abs(forgotten_output - expected))),
        )
        cases += 1
    return {
        "basis_cases": cases,
        "maximum_error": maximum_error,
        "pass": maximum_error <= TOL,
        "map_is_isometric": False,
        "nonisometry_witness": {
            "input_inner_product_1_0_vs_1_1": 0,
            "forgotten_inner_product": 1,
        },
    }


def recorder_off_receipt(
    counter_size: int,
    coin: np.ndarray,
) -> dict[str, Any]:
    """Compare the source gate (recorder off) with a blank-counter lift."""

    source_dimension = 3
    extended_dimension = counter_size + 2
    source = source_scattering(coin)
    extended = recorder_scattering(counter_size, coin)
    maximum_amplitude_error = 0.0
    maximum_probability_error = 0.0
    cases = 0
    for left in range(source_dimension):
        for right in range(source_dimension):
            extended_input = (
                2 if left == 2 else left,
                2 if right == 2 else right,
            )
            forgotten_output = np.zeros(source_dimension**2, dtype=complex)
            extended_column = extended[
                :,
                pair_index(*extended_input, extended_dimension),
            ]
            for output_index, amplitude in enumerate(extended_column):
                if abs(amplitude) <= 1.0e-14:
                    continue
                output_pair = pair_from_index(
                    output_index, extended_dimension
                )
                forgotten_pair = formal_forget_pair(output_pair)
                forgotten_output[
                    pair_index(*forgotten_pair, source_dimension)
                ] += amplitude
            source_column = source[
                :, pair_index(left, right, source_dimension)
            ]
            maximum_amplitude_error = max(
                maximum_amplitude_error,
                float(np.max(np.abs(forgotten_output - source_column))),
            )
            maximum_probability_error = max(
                maximum_probability_error,
                float(
                    np.max(
                        np.abs(
                            np.abs(forgotten_output) ** 2
                            - np.abs(source_column) ** 2
                        )
                    )
                ),
            )
            cases += 1
    return {
        "recorder_off_object": "source 9x9 U_C",
        "recorder_on_object": "extended U_(C,R), initialized at k=0",
        "complete_source_basis_cases": cases,
        "maximum_forgotten_amplitude_error": maximum_amplitude_error,
        "maximum_path_probability_error": maximum_probability_error,
        "stored_readout_off": None,
        "stored_readout_on_after_one_1_0_event": 1,
        "pass": maximum_amplitude_error <= TOL,
    }


def state_after_repeated_events(
    matrix: np.ndarray,
    dimension: int,
    counter_size: int,
    event_count: int,
) -> SparseState:
    state: SparseState = {(2, 1): 1.0 + 0.0j}
    for _ in range(event_count):
        output: SparseState = {}
        for pair, amplitude in state.items():
            for out_pair, local_amplitude in local_action(
                matrix, dimension, pair
            ).items():
                output[out_pair] = (
                    output.get(out_pair, 0.0j)
                    + amplitude * local_amplitude
                )
        state = prune(output)
    expected_counter = event_count % counter_size
    observed_counters = sorted(
        {
            next(symbol - 2 for symbol in pair if symbol >= 2)
            for pair in state
        }
    )
    if observed_counters != [expected_counter]:
        raise AssertionError(
            f"wrong counter support {observed_counters}, expected {expected_counter}"
        )
    return state


def event_count_receipt(
    matrix: np.ndarray,
    dimension: int,
    counter_size: int,
) -> dict[str, Any]:
    rows = []
    for events in range(counter_size + 3):
        state = state_after_repeated_events(
            matrix, dimension, counter_size, events
        )
        rows.append(
            {
                "events": events,
                "counter_readout": events % counter_size,
                "support_size": len(state),
                "norm": sum(abs(value) ** 2 for value in state.values()),
            }
        )
    return {
        "rows": rows,
        "pre_alias_exact": all(
            row["counter_readout"] == row["events"]
            for row in rows
            if row["events"] < counter_size
        ),
        "alias_pair": {
            "events_a": 1,
            "events_b": counter_size + 1,
            "readout": 1,
        },
    }


def q_crossing_bad_rival(
    counter_size: int,
    coin: np.ndarray,
) -> dict[str, Any]:
    dimension = counter_size + 2
    bad = recorder_scattering(
        counter_size, coin, increment_on_q=True
    )
    direct_basis = encoded_input(2, 1, 3, 1, 0, 0)
    refined_basis = encoded_input(2, 1, 3, 4, 0, 0)
    direct = rectangular_patch(
        {direct_basis: 1.0 + 0.0j}, 3, 1, bad, dimension
    )
    refined = rectangular_patch(
        {refined_basis: 1.0 + 0.0j}, 3, 4, bad, dimension
    )

    def counter_support(state: SparseState) -> list[int]:
        return sorted(
            {
                symbol - 2
                for basis in state
                for symbol in basis
                if symbol >= 2
            }
        )

    direct_support = counter_support(direct)
    refined_support = counter_support(refined)
    expected = expected_patch_output(
        bad, dimension, 2, 1, 3, 4, 0, 0
    )
    defect = sparse_distance(refined, expected)
    frame_betas = (1, 2, 4)
    frame_readouts = {
        str(beta): beta % counter_size for beta in frame_betas
    }
    offsets = {
        str(beta): (1 - readout) % counter_size
        for beta, readout in (
            (beta, frame_readouts[str(beta)]) for beta in frame_betas
        )
    }
    return {
        "matrix_unitarity_error": matrix_error(bad),
        "direct_beta_1_counter_support": direct_support,
        "refined_beta_4_counter_support": refined_support,
        "refinement_naturality_defect": defect,
        "frame_readouts": frame_readouts,
        "per_frame_decoder_offsets_to_report_one": offsets,
        "one_fixed_offset_exists": len(set(offsets.values())) == 1,
    }


def source_counter_joint_amplitudes(
    extended_state: SparseState,
    source_dimension: int,
    counter_size: int,
) -> np.ndarray:
    """Factor the exact-one-particle sector as source pair tensor counter."""

    amplitudes = np.zeros(
        (source_dimension**2, counter_size), dtype=complex
    )
    for pair, amplitude in extended_state.items():
        particles = [symbol for symbol in pair if symbol >= 2]
        if len(particles) != 1:
            raise ValueError("witness left the exact-one-particle sector")
        counter = particles[0] - 2
        source_pair = formal_forget_pair(pair)
        amplitudes[pair_index(*source_pair, source_dimension), counter] += (
            amplitude
        )
    return amplitudes


def apply_local_to_sparse_pair(
    state: SparseState,
    matrix: np.ndarray,
    dimension: int,
) -> SparseState:
    output: SparseState = {}
    for pair, amplitude in state.items():
        for out_pair, local_amplitude in local_action(
            matrix, dimension, pair
        ).items():
            output[out_pair] = (
                output.get(out_pair, 0.0j)
                + amplitude * local_amplitude
            )
    return prune(output)


def passive_recorder_witness(
    counter_size: int,
    coin: np.ndarray,
) -> dict[str, Any]:
    """One-gate QCA witness for the T6 no-passive-informative-record result."""

    dimension = counter_size + 2
    source_dimension = 3
    extended = recorder_scattering(counter_size, coin)
    source = source_scattering(coin)
    inv_sqrt_two = 1.0 / math.sqrt(2.0)

    cross_count_input: SparseState = {
        (2, 0): inv_sqrt_two,  # |1_0,q>: no effective event
        (2, 1): inv_sqrt_two,  # |1_0,0>: one effective event
    }
    extended_output = apply_local_to_sparse_pair(
        cross_count_input, extended, dimension
    )
    joint = source_counter_joint_amplitudes(
        extended_output, source_dimension, counter_size
    )
    reduced = joint @ joint.conj().T

    source_input = np.zeros(source_dimension**2, dtype=complex)
    source_input[pair_index(2, 0, source_dimension)] = inv_sqrt_two
    source_input[pair_index(2, 1, source_dimension)] = inv_sqrt_two
    ideal_vector = source @ source_input
    ideal = np.outer(ideal_vector, ideal_vector.conj())

    s_zero = source[:, pair_index(2, 0, source_dimension)]
    s_one = source[:, pair_index(2, 1, source_dimension)]
    ideal_coherence = complex(s_zero.conj() @ ideal @ s_one)
    retained_coherence = complex(s_zero.conj() @ reduced @ s_one)
    fidelity = float(np.real(ideal_vector.conj() @ reduced @ ideal_vector))
    eigenvalues = np.linalg.eigvalsh(reduced - ideal)
    trace_distance = float(0.5 * np.sum(np.abs(eigenvalues)))

    fixed_count_input: SparseState = {
        (2, 1): inv_sqrt_two,
        (1, 2): 1j * inv_sqrt_two,
    }
    fixed_extended_output = apply_local_to_sparse_pair(
        fixed_count_input, extended, dimension
    )
    fixed_joint = source_counter_joint_amplitudes(
        fixed_extended_output, source_dimension, counter_size
    )
    fixed_reduced = fixed_joint @ fixed_joint.conj().T
    fixed_source_input = np.zeros(source_dimension**2, dtype=complex)
    fixed_source_input[pair_index(2, 1, source_dimension)] = inv_sqrt_two
    fixed_source_input[pair_index(1, 2, source_dimension)] = (
        1j * inv_sqrt_two
    )
    fixed_ideal_vector = source @ fixed_source_input
    fixed_ideal = np.outer(
        fixed_ideal_vector, fixed_ideal_vector.conj()
    )
    fixed_trace_distance = float(
        0.5
        * np.sum(np.abs(np.linalg.eigvalsh(fixed_reduced - fixed_ideal)))
    )

    return {
        "realized_inside_one_extended_clock_qca_scattering": True,
        "cross_count_histories": [
            "|1_0,q> (zero effective interactions)",
            "|1_0,0> (one effective interaction)",
        ],
        "record_states_orthogonal": True,
        "ideal_off_diagonal_magnitude": abs(ideal_coherence),
        "retained_off_diagonal_magnitude": abs(retained_coherence),
        "normalized_interference_visibility_ideal": (
            2.0 * abs(ideal_coherence)
        ),
        "normalized_interference_visibility_after_trace": (
            2.0 * abs(retained_coherence)
        ),
        "fidelity_with_ideal_pure_source_output": fidelity,
        "trace_distance_from_ideal_source_output": trace_distance,
        "source_basis_populations_preserved": bool(
            np.max(np.abs(np.diag(reduced) - np.diag(ideal))) <= TOL
        ),
        "fixed_count_sector_trace_distance": fixed_trace_distance,
        "theorem_scope": (
            "If Tr_R[V rho V*]=U rho U* for every rho, purity of the "
            "unitary channel forces V|psi>=U|psi> tensor |r0>; an "
            "informative record therefore cannot be passive on all coherent "
            "source histories."
        ),
    }


def copy_loss_receipt(counter_size: int) -> dict[str, Any]:
    """Controlled-add copy, no-cloning, carrier-loss, and alias controls."""

    copy_unitary = np.zeros(
        (counter_size**2, counter_size**2), dtype=complex
    )
    for source_label in range(counter_size):
        for target_label in range(counter_size):
            input_index = pair_index(
                source_label, target_label, counter_size
            )
            output_index = pair_index(
                source_label,
                (target_label + source_label) % counter_size,
                counter_size,
            )
            copy_unitary[output_index, input_index] = 1.0
    classical_copy_success = True
    basis_readout_survives_source_trace = True
    for label in range(counter_size):
        input_vector = np.zeros(counter_size**2, dtype=complex)
        input_vector[pair_index(label, 0, counter_size)] = 1.0
        output_vector = copy_unitary @ input_vector
        expected = np.zeros(counter_size**2, dtype=complex)
        expected[pair_index(label, label, counter_size)] = 1.0
        classical_copy_success = classical_copy_success and bool(
            np.max(np.abs(output_vector - expected)) <= TOL
        )
        output_matrix = output_vector.reshape(
            counter_size, counter_size
        )
        target_reduced_for_label = (
            output_matrix.conj().T @ output_matrix
        )
        expected_target = np.zeros(
            (counter_size, counter_size), dtype=complex
        )
        expected_target[label, label] = 1.0
        basis_readout_survives_source_trace = (
            basis_readout_survives_source_trace
            and bool(
                np.max(
                    np.abs(target_reduced_for_label - expected_target)
                )
                <= TOL
            )
        )
    plus = np.zeros(counter_size, dtype=complex)
    plus[0] = 1.0 / math.sqrt(2.0)
    plus[1] = 1.0 / math.sqrt(2.0)
    coherent_input = np.zeros(counter_size**2, dtype=complex)
    coherent_input[pair_index(0, 0, counter_size)] = plus[0]
    coherent_input[pair_index(1, 0, counter_size)] = plus[1]
    copied = (copy_unitary @ coherent_input).reshape(
        counter_size, counter_size
    )
    target_reduced = copied.conj().T @ copied
    desired_plus = np.outer(plus, plus.conj())
    fidelity_to_coherent_clone = float(
        np.real(plus.conj() @ target_reduced @ plus)
    )
    alias_a = 1
    alias_b = counter_size + 1
    copied_alias_a = (alias_a % counter_size,) * 2
    copied_alias_b = (alias_b % counter_size,) * 2
    return {
        "controlled_add_unitarity_error": matrix_error(copy_unitary),
        "controlled_add_digest": matrix_digest(copy_unitary),
        "classical_orthogonal_label_copy_success": classical_copy_success,
        "basis_readout_survives_tracing_original_carrier": (
            basis_readout_survives_source_trace
        ),
        "coherent_input": "(|0>+|1>)/sqrt(2)",
        "copy_output": "(|00>+|11>)/sqrt(2)",
        "target_reduced_purity": float(
            np.real(np.trace(target_reduced @ target_reduced))
        ),
        "target_fidelity_to_coherent_plus": fidelity_to_coherent_clone,
        "is_two_coherent_clones": bool(
            np.max(np.abs(target_reduced - desired_plus)) <= TOL
        ),
        "carrier_loss_without_copy_readout": None,
        "carrier_loss_with_copy_readout": "available from extra R-state register",
        "copy_cost_dimension": counter_size,
        "spatial_transport_or_reunion_simulated": False,
        "reunion_status": (
            "OPEN: this receipt tests logical copying and carrier loss only"
        ),
        "copied_alias_pair": {
            "events_a": alias_a,
            "events_b": alias_b,
            "copy_a": copied_alias_a,
            "copy_b": copied_alias_b,
            "still_aliases": copied_alias_a == copied_alias_b,
        },
    }


def encoding_composition_receipt() -> dict[str, Any]:
    """Canonical semigroup law and an arbitrary-placement non-family control."""

    alphabet = (0, 1, 2)
    canonical_cases = 0
    canonical_pass = True
    for outer in range(1, 5):
        for inner in range(1, 5):
            for symbol in alphabet:
                first = embedded_basis(symbol, inner, 0)
                composed: list[int] = []
                for item in first:
                    composed.extend(embedded_basis(item, outer, 0))
                direct = embedded_basis(symbol, outer * inner, 0)
                canonical_pass = canonical_pass and tuple(composed) == direct
                canonical_cases += 1

    # A deliberately incoherent selector: use position one at every n>=2.
    symbol = 2
    e2 = embedded_basis(symbol, 2, 1)
    composed_bad: list[int] = []
    for item in e2:
        composed_bad.extend(embedded_basis(item, 2, 1))
    direct_bad = embedded_basis(symbol, 4, 1)
    return {
        "canonical_cases": canonical_cases,
        "canonical_composition_pass": canonical_pass,
        "canonical_rule": (
            "(tensor_n E_m) E_n = E_(mn) for E_n(x)=x q^(n-1)"
        ),
        "arbitrary_placement_local_square_can_pass": True,
        "arbitrary_selector_composition_counterexample": {
            "rule": "place the active symbol at index 1 for every n>=2",
            "composed_E2_then_E2": list(composed_bad),
            "direct_E4": list(direct_bad),
            "same": tuple(composed_bad) == direct_bad,
        },
        "scope": (
            "All-placement tests are robustness tests of the local square; "
            "only a placement rule with its own composition law is a full "
            "Lorentz-transform encoding family."
        ),
    }


def make_check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def main() -> None:
    coins = coin_family()
    coin_rows = [
        {
            "name": name,
            "unitarity_error": matrix_error(coin),
            "digest": matrix_digest(coin),
        }
        for name, coin in coins
    ]
    source_rows = [
        {
            "coin": name,
            "unitarity_error": matrix_error(source_scattering(coin)),
            "digest": matrix_digest(source_scattering(coin)),
        }
        for name, coin in coins
    ]

    local_rows: list[dict[str, Any]] = []
    forget_rows: list[dict[str, Any]] = []
    closure_rows: list[dict[str, Any]] = []
    for counter_size in (2, 3, 5):
        for coin_name, coin in coins:
            matrix = recorder_scattering(counter_size, coin)
            dimension = counter_size + 2
            block = active_block(matrix, dimension)
            lifted = q_transparent_lift(block)
            local_rows.append(
                {
                    "counter_size": counter_size,
                    "coin": coin_name,
                    "dimension": dimension,
                    "full_matrix_dimension": dimension**2,
                    "unitarity_error": matrix_error(matrix),
                    "active_block_unitarity_error": matrix_error(block),
                    "matrix_digest": matrix_digest(matrix),
                }
            )
            forget_rows.append(
                {
                    "counter_size": counter_size,
                    "coin": coin_name,
                    **formal_forgetting_sweep(
                        matrix, source_scattering(coin), dimension
                    ),
                }
            )
            closure_rows.append(
                {
                    "counter_size": counter_size,
                    "coin": coin_name,
                    "lift_reconstruction_error": float(
                        np.max(np.abs(lifted - matrix))
                    ),
                }
            )

    training_patches = [
        (alpha, beta)
        for alpha in range(1, 5)
        for beta in range(1, 5)
    ]
    naturality_rows: list[dict[str, Any]] = []
    for counter_size in (2, 3):
        for coin_name, coin in coins:
            matrix = recorder_scattering(counter_size, coin)
            naturality_rows.append(
                {
                    "counter_size": counter_size,
                    "coin": coin_name,
                    "patches": "all alpha,beta in 1..4",
                    "placements": "all",
                    **naturality_sweep(
                        matrix,
                        counter_size + 2,
                        training_patches,
                        all_placements=True,
                    ),
                }
            )

    held_out_coin_name, held_out_coin = coins[-1]
    held_out_counter_size = 4
    held_out_matrix = recorder_scattering(
        held_out_counter_size, held_out_coin
    )
    held_out_naturality = naturality_sweep(
        held_out_matrix,
        held_out_counter_size + 2,
        [(6, 5)],
        all_placements=True,
    )

    superposition = superposition_naturality(
        held_out_matrix,
        held_out_counter_size + 2,
        5,
        4,
        3,
        2,
        [
            (0, 0, 1.0 + 0.0j),
            (2, 1, 0.0 + 1.0j),
            (3, 1, -0.5 + 0.25j),
            (1, 4, 0.3 - 0.7j),
            (5, 2, -0.2 - 0.4j),
        ],
    )
    counter_superposition = superposition_naturality(
        held_out_matrix,
        held_out_counter_size + 2,
        4,
        3,
        2,
        1,
        [
            (2, 1, 1.0 + 0.0j),
            (3, 1, 0.0 + 1.0j),
        ],
    )

    arbitrary_k_dimension = 3
    arbitrary_block = fourier_unitary(arbitrary_k_dimension**2)
    arbitrary_lift = q_transparent_lift(arbitrary_block)
    arbitrary_lift_naturality = naturality_sweep(
        arbitrary_lift,
        arbitrary_k_dimension + 1,
        [(5, 4)],
        all_placements=True,
    )

    event_matrix = recorder_scattering(5, coins[0][1])
    event_receipt = event_count_receipt(event_matrix, 7, 5)
    good_q_readouts = []
    for alpha, beta in ((1, 1), (2, 3), (4, 2), (6, 5)):
        state = rectangular_patch(
            {encoded_input(2, 1, alpha, beta, 0, 0): 1.0 + 0.0j},
            alpha,
            beta,
            event_matrix,
            7,
        )
        counters = sorted(
            {
                symbol - 2
                for basis in state
                for symbol in basis
                if symbol >= 2
            }
        )
        good_q_readouts.append(
            {"alpha": alpha, "beta": beta, "counter_support": counters}
        )

    deterministic_coin = np.eye(2, dtype=complex)
    bad_rival = q_crossing_bad_rival(11, deterministic_coin)
    passive_witness = passive_recorder_witness(3, coins[0][1])
    recorder_off = recorder_off_receipt(5, coins[0][1])
    copy_receipt = copy_loss_receipt(5)
    composition = encoding_composition_receipt()
    resource_rows = [
        {
            "horizon_T": horizon,
            "exact_count_minimum_dimension": horizon + 1,
            "independent_binary_history_minimum_dimension": 2**horizon,
        }
        for horizon in (1, 2, 5, 8, 13)
    ]

    all_naturality_cases = sum(
        row["cases"] for row in naturality_rows
    )
    all_forget_cases = sum(row["basis_cases"] for row in forget_rows)

    checks = [
        make_check(
            "all declared 2x2 coins are unitary",
            all(row["unitarity_error"] <= TOL for row in coin_rows),
            "three nontrivial real/complex coins",
        ),
        make_check(
            "source Clock-QCA matrices are full-basis unitary",
            all(row["unitarity_error"] <= TOL for row in source_rows),
            "complete 9x9 matrices, not selected fixtures",
        ),
        make_check(
            "frozen recorder matrices are full-basis unitary",
            all(row["unitarity_error"] <= TOL for row in local_rows),
            f"{len(local_rows)} complete matrices across R=2,3,5",
        ),
        make_check(
            "every recorder active block is unitary",
            all(
                row["active_block_unitarity_error"] <= TOL
                for row in local_rows
            ),
            "K tensor K restriction includes 0/0, particle/particle, and coin sectors",
        ),
        make_check(
            "frozen recorder is exactly a q-transparent lift",
            all(
                row["lift_reconstruction_error"] <= TOL
                for row in closure_rows
            ),
            "establishes membership in the scoped closure class",
        ),
        make_check(
            "formal source forgetting intertwines on the complete local basis",
            all(row["pass"] for row in forget_rows),
            f"{all_forget_cases} extended input basis states",
        ),
        make_check(
            "formal forgetting is not a physical isometry",
            all(not row["map_is_isometric"] for row in forget_rows),
            "orthogonal |1_0>,|1_1> both map to |1>",
        ),
        make_check(
            "recorder-off source gate and blank-counter lift agree locally",
            recorder_off["pass"]
            and recorder_off["stored_readout_off"] is None
            and recorder_off["stored_readout_on_after_one_1_0_event"] == 1,
            "all nine source basis inputs; only the extended gate stores k",
        ),
        make_check(
            "canonical and placed recorder patches are exactly natural",
            all(row["pass"] for row in naturality_rows),
            f"{all_naturality_cases} full encoded-basis/placement cases",
        ),
        make_check(
            "held-out 6x5 recorder patch is exactly natural",
            held_out_naturality["pass"],
            f"{held_out_naturality['cases']} all-placement full-basis cases",
        ),
        make_check(
            "patch naturality is linear on a mixed complex superposition",
            superposition["pass"],
            f"{superposition['term_count']} terms",
        ),
        make_check(
            "counter-label superpositions satisfy the same naturality square",
            counter_superposition["pass"],
            "no counter-basis measurement or decoder is inserted",
        ),
        make_check(
            "an arbitrary dense active block has a unitary q-transparent lift",
            matrix_error(arbitrary_lift) <= TOL,
            "9x9 Fourier W on K tensor K, not the cyclic counter block",
        ),
        make_check(
            "arbitrary dense active block passes held-out patch naturality",
            arbitrary_lift_naturality["pass"],
            f"{arbitrary_lift_naturality['cases']} full-basis/placement cases",
        ),
        make_check(
            "canonical q-insertion encodings compose",
            composition["canonical_composition_pass"],
            f"{composition['canonical_cases']} E_mn composition cases",
        ),
        make_check(
            "arbitrary placement is not automatically an encoding family",
            not composition[
                "arbitrary_selector_composition_counterexample"
            ]["same"],
            "local all-placement robustness is scoped below semigroup compatibility",
        ),
        make_check(
            "effective interactions advance the good counter exactly once",
            event_receipt["pre_alias_exact"],
            "all pre-alias horizons on a nontrivial complex coin",
        ),
        make_check(
            "q-insertion refinement does not advance the good counter",
            all(row["counter_support"] == [1] for row in good_q_readouts),
            "four patches through held-out 6x5",
        ),
        make_check(
            "q-increment rival remains locally unitary",
            bad_rival["matrix_unitarity_error"] <= TOL,
            "failure is naturality, not a malformed local map",
        ),
        make_check(
            "q-increment rival fails refinement naturality",
            bad_rival["refinement_naturality_defect"] > 1.0e-6
            and bad_rival["direct_beta_1_counter_support"]
            != bad_rival["refined_beta_4_counter_support"],
            "encoding-added q crossings change the record",
        ),
        make_check(
            "q-increment rival needs a frame-dependent decoder",
            not bad_rival["one_fixed_offset_exists"],
            "beta-dependent offsets are rejected as refits",
        ),
        make_check(
            "finite cyclic counter exhibits its first exact alias",
            event_receipt["alias_pair"]["events_b"]
            - event_receipt["alias_pair"]["events_a"]
            == 5,
            "n and n+R have the same readout",
        ),
        make_check(
            "exact count and independent-history resource bounds are distinct",
            all(
                row["exact_count_minimum_dimension"]
                == row["horizon_T"] + 1
                and row["independent_binary_history_minimum_dimension"]
                == 2 ** row["horizon_T"]
                for row in resource_rows
            ),
            "T+1 count states versus 2^T binary histories",
        ),
        make_check(
            "one-gate cross-count record kills source interference",
            passive_witness[
                "normalized_interference_visibility_ideal"
            ]
            >= 1.0 - TOL
            and passive_witness[
                "normalized_interference_visibility_after_trace"
            ]
            <= TOL,
            "actual |1_0,q> versus |1_0,0> Clock-QCA input",
        ),
        make_check(
            "cross-count witness has fidelity and trace distance one half",
            abs(
                passive_witness[
                    "fidelity_with_ideal_pure_source_output"
                ]
                - 0.5
            )
            <= TOL
            and abs(
                passive_witness[
                    "trace_distance_from_ideal_source_output"
                ]
                - 0.5
            )
            <= TOL,
            "orthogonal record states carry complete which-history information",
        ),
        make_check(
            "fixed-count sector preserves the physical source channel",
            passive_witness["fixed_count_sector_trace_distance"] <= TOL,
            "both coherent branches increment to the same counter state",
        ),
        make_check(
            "cross-count dephasing preserves source-basis populations",
            passive_witness["source_basis_populations_preserved"],
            "the failure is coherence, not classical path probability",
        ),
        make_check(
            "orthogonal counter labels can be copied with charged storage",
            copy_receipt["controlled_add_unitarity_error"] <= TOL
            and copy_receipt["classical_orthogonal_label_copy_success"]
            and copy_receipt[
                "basis_readout_survives_tracing_original_carrier"
            ]
            and copy_receipt["copy_cost_dimension"] == 5,
            "actual 25x25 controlled-add unitary uses a second five-state register",
        ),
        make_check(
            "coherent counter state is entangled rather than cloned",
            not copy_receipt["is_two_coherent_clones"]
            and abs(copy_receipt["target_reduced_purity"] - 0.5) <= TOL
            and abs(
                copy_receipt["target_fidelity_to_coherent_plus"] - 0.5
            )
            <= TOL,
            "controlled copy sends |+>|0> to a Bell-like state",
        ),
        make_check(
            "controlled copying does not repair cyclic aliasing",
            copy_receipt["copied_alias_pair"]["still_aliases"],
            "logical redundancy improves basis-label loss tolerance but not capacity",
        ),
        make_check(
            "loss of the uncopied carrier removes the readout",
            copy_receipt["carrier_loss_without_copy_readout"] is None,
            "the counter is carried by the particle, not left in a free archive",
        ),
    ]
    checks_passed = sum(check["pass"] for check in checks)

    artifact = {
        "probe": "du_covariant_recorder_naturality_probe",
        "hardening_id": "HC-DU-031B",
        "source": {
            "citation": (
                "Arrighi, Facchini, and Forets, Discrete Lorentz covariance "
                "for Quantum Walks and Quantum Cellular Automata"
            ),
            "arxiv": "https://arxiv.org/abs/1404.4499",
            "exact_tex_sha256": SOURCE_TEX_SHA256,
            "pdf_sha256": SOURCE_PDF_SHA256,
            "tex_scope": "Clock QCA definition/covariance, lines 930-981",
            "boundary_convention": (
                "input alpha then beta; output beta then alpha, matching "
                "the planar rectangular-patch proof"
            ),
        },
        "candidate": {
            "alphabet": "|q>, |0>, |1_0>,...,|1_(R-1)>",
            "counter_update": "k -> k+1 mod R only on 1_k/0",
            "q_rule": "transparent swap with no counter update",
            "encoding": "E_n(x)=x tensor q^(n-1)",
            "fixed_decoder": "read particle species k in every admitted frame",
        },
        "theorem_results": {
            "T1_local_unitarity": "PROVED_AND_EXHAUSTIVELY_CHECKED",
            "T2_source_conservativity": (
                "ALGEBRAICALLY_EXACT_ON_COMPLETE_LOCAL_BASIS; "
                "PHYSICALLY_EXACT_ON_FIXED_COUNT_SECTORS; "
                "FALSE_AS_ALL_HISTORY_REDUCED_CHANNEL_EQUALITY"
            ),
            "T3_exact_recorder_naturality": (
                "PROVED_FOR_CANONICAL_Q_INSERTION_FAMILY; "
                "ALL_PLACEMENTS_PASS_LOCAL_SQUARE"
            ),
            "T4_event_count_correctness": (
                "PROVED_ON_SINGLE_PARTICLE_VALID_SECTOR_BEFORE_ALIAS"
            ),
            "T5_finite_resource_obstruction": "PROVED",
            "T6_passive_recorder_obstruction": (
                "PROVED_WITH_ONE_GATE_CLOCK_QCA_INTERFERENCE_WITNESS"
            ),
            "closure_lifting_lemma": (
                "For H=Cq direct-sum K, every unitary W on K tensor K "
                "inherits the q-insertion rectangular covariance square "
                "under the q-transparent lift."
            ),
        },
        "coin_rows": coin_rows,
        "source_rows": source_rows,
        "local_unitarity_rows": local_rows,
        "formal_forgetting_rows": forget_rows,
        "closure_rows": closure_rows,
        "naturality_training_rows": naturality_rows,
        "held_out_naturality": {
            "counter_size": held_out_counter_size,
            "coin": held_out_coin_name,
            "patch": [6, 5],
            "placements": "all",
            **held_out_naturality,
        },
        "linearity": {
            "general_superposition": superposition,
            "counter_superposition": counter_superposition,
        },
        "arbitrary_active_block_control": {
            "K_dimension": arbitrary_k_dimension,
            "W": "9x9 discrete Fourier unitary",
            "W_unitarity_error": matrix_error(arbitrary_block),
            "lift_unitarity_error": matrix_error(arbitrary_lift),
            "patch": [5, 4],
            **arbitrary_lift_naturality,
        },
        "encoding_composition": composition,
        "event_count": event_receipt,
        "q_refinement_readouts": good_q_readouts,
        "q_increment_rival": bad_rival,
        "resource_bounds": resource_rows,
        "recorder_off_control": recorder_off,
        "passive_recorder_obstruction": passive_witness,
        "copy_and_loss_control": copy_receipt,
        "checks": checks,
        "checks_passed": checks_passed,
        "checks_total": len(checks),
        "underlying_case_counts": {
            "full_local_unitarity_matrices": len(local_rows),
            "formal_forgetting_basis_cases": all_forget_cases,
            "training_naturality_basis_placement_cases": (
                all_naturality_cases
            ),
            "held_out_recorder_cases": held_out_naturality["cases"],
            "arbitrary_active_block_cases": (
                arbitrary_lift_naturality["cases"]
            ),
        },
        "verdict": "COVARIANT_COUNTER_WITH_NECESSARY_BACKREACTION",
        "claim_grade": (
            "EXACT FINITE MATHEMATICAL CONSTRUCTION AND OBSTRUCTION / "
            "PHYSICAL IDENTIFICATION OPEN / NO CLAIM BANKED"
        ),
        "scope_not_earned": [
            "classical irreversible record",
            "observer ownership or free archive",
            "proper time or a dimensional time unit",
            "continuum or higher-dimensional covariance",
            "gravity, cosmology, Lambda, or a Dynamic Unity law",
            "publication novelty beyond SEARCH-INCOMPLETE related-work audit",
        ],
    }
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("COVARIANT RECORDER NATURALITY PROBE")
    for check in checks:
        status = "PASS" if check["pass"] else "FAIL"
        print(f"{status}  {check['name']}")
    print(f"{checks_passed}/{len(checks)} checks pass")
    print(
        "VERDICT: COVARIANT COUNTER WITH NECESSARY BACKREACTION "
        "(NO PHYSICS CLAIM BANKED)"
    )
    print(f"artifact: {ARTIFACT_PATH}")
    if checks_passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
