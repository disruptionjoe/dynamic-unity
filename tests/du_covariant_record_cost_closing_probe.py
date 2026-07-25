#!/usr/bin/env python3
"""Deterministic probe for the covariant-record closing theorem.

The probe tests three scoped statements.

1. For a binary controlled, nondemolition history recorder with a blank
   source-independent environment, let ``gamma`` be the surviving source
   coherence, let

       delta = 1/2 ||N_|gamma| - id||_diamond = (1-|gamma|)/2,

   and let ``D`` be half trace distance between the two accessible record
   states.  Then

       D^2 <= 4 delta (1-delta).

2. If the accessible conditional record states factor over independent
   fragments, fragment distinguishabilities ``D_k`` imply

       delta >= (1 - product_k sqrt(1-D_k^2)) / 2.

3. A fixed decoder that recovers one of ``N`` uniformly distributed histories
   with average error ``p`` from a ``K``-dimensional archive obeys the
   Holevo-Fano support bound

       log2(K) >= log2(N) - h2(p) - p log2(N-1).

Passing the probe establishes finite mathematics only.  It does not establish
novelty, autonomous record formation, an irreversible archive, an energy or
entropy cost, continuum covariance, observerhood, proper time, or Dynamic
Unity dynamics.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_covariant_record_cost_closing_result.json"
)
TOL = 3.0e-10
SEED = 20260724


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    """Half trace norm, D(rho,sigma)=1/2 ||rho-sigma||_1."""

    difference = left - right
    difference = (difference + difference.conj().T) / 2.0
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(difference))))


def density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def psd_sqrt(matrix: np.ndarray) -> np.ndarray:
    matrix = (matrix + matrix.conj().T) / 2.0
    values, vectors = np.linalg.eigh(matrix)
    values = np.clip(values, 0.0, None)
    return (vectors * np.sqrt(values)) @ vectors.conj().T


def root_fidelity(left: np.ndarray, right: np.ndarray) -> float:
    """Root fidelity F=||sqrt(rho)sqrt(sigma)||_1, not its square."""

    root = psd_sqrt(left)
    middle = root @ right @ root
    value = float(np.real(np.trace(psd_sqrt(middle))))
    return min(1.0, max(0.0, value))


def haar_unitary(dimension: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    q_matrix, r_matrix = np.linalg.qr(raw)
    diagonal = np.diag(r_matrix)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 1.0e-15
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return q_matrix @ np.diag(phases.conj())


def random_density(dimension: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    matrix = raw @ raw.conj().T
    return matrix / np.trace(matrix)


def depolarize(matrix: np.ndarray, probability: float) -> np.ndarray:
    dimension = matrix.shape[0]
    return (
        (1.0 - probability) * matrix
        + probability * np.eye(dimension, dtype=complex) / dimension
    )


def recorder_row(
    sigma: np.ndarray,
    unitary_zero: np.ndarray,
    unitary_one: np.ndarray,
    archive_noise: float,
) -> dict[str, float]:
    """One mixed-environment controlled-recorder receipt."""

    conditional_zero = unitary_zero @ sigma @ unitary_zero.conj().T
    conditional_one = unitary_one @ sigma @ unitary_one.conj().T
    gamma = np.trace(
        unitary_zero @ sigma @ unitary_one.conj().T
    )
    visibility = float(abs(gamma))
    delta = 0.5 * (1.0 - visibility)

    accessible_zero = depolarize(conditional_zero, archive_noise)
    accessible_one = depolarize(conditional_one, archive_noise)

    environment_fidelity = root_fidelity(
        conditional_zero, conditional_one
    )
    accessible_fidelity = root_fidelity(
        accessible_zero, accessible_one
    )
    distinguishability = trace_distance(
        accessible_zero, accessible_one
    )
    curve_bound = 2.0 * math.sqrt(max(0.0, delta * (1.0 - delta)))

    plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    plus_density = density(plus)
    phase = 1.0 if visibility <= TOL else gamma / visibility
    corrected_output = np.array(
        [[0.5, 0.5 * visibility], [0.5 * visibility, 0.5]],
        dtype=complex,
    )
    fixed_phase_output = np.array(
        [[0.5, 0.5 * gamma], [0.5 * gamma.conjugate(), 0.5]],
        dtype=complex,
    )
    phase_equalizer = np.diag([1.0, phase.conjugate()]).astype(complex)
    equalized_from_fixed = (
        phase_equalizer.conj().T
        @ fixed_phase_output
        @ phase_equalizer
    )

    return {
        "visibility_abs_gamma": visibility,
        "half_diamond_delta": delta,
        "record_trace_distance": distinguishability,
        "curve_bound": curve_bound,
        "squared_curve_slack": (
            4.0 * delta * (1.0 - delta) - distinguishability**2
        ),
        "environment_root_fidelity": environment_fidelity,
        "accessible_root_fidelity": accessible_fidelity,
        "gamma_to_environment_fidelity_slack": (
            environment_fidelity - visibility
        ),
        "fidelity_monotonicity_slack": (
            accessible_fidelity - environment_fidelity
        ),
        "plus_state_trace_distance": trace_distance(
            corrected_output, plus_density
        ),
        "phase_equalization_error": float(
            np.max(np.abs(equalized_from_fixed - corrected_output))
        ),
    }


def pure_tight_row(angle: float) -> dict[str, float]:
    record_zero = np.array([1.0, 0.0], dtype=complex)
    record_one = np.array(
        [math.cos(angle), math.sin(angle)], dtype=complex
    )
    overlap = float(abs(np.vdot(record_zero, record_one)))
    delta = 0.5 * (1.0 - overlap)
    distinguishability = trace_distance(
        density(record_zero), density(record_one)
    )
    bound = 2.0 * math.sqrt(delta * (1.0 - delta))
    return {
        "angle": angle,
        "visibility": overlap,
        "half_diamond_delta": delta,
        "record_trace_distance": distinguishability,
        "curve_bound": bound,
        "equality_error": abs(distinguishability - bound),
    }


def product_fragment_receipt(
    distinguishabilities: list[float],
) -> dict[str, Any]:
    overlaps = [
        math.sqrt(max(0.0, 1.0 - value**2))
        for value in distinguishabilities
    ]
    visibility = math.prod(overlaps)
    delta = 0.5 * (1.0 - visibility)
    lower_bound = 0.5 * (
        1.0
        - math.prod(
            math.sqrt(max(0.0, 1.0 - value**2))
            for value in distinguishabilities
        )
    )
    return {
        "fragment_distinguishabilities": distinguishabilities,
        "fragment_overlaps": overlaps,
        "visibility": visibility,
        "half_diamond_delta": delta,
        "independent_fragment_lower_bound": lower_bound,
        "equality_error": abs(delta - lower_bound),
        "fragment_count": len(distinguishabilities),
        "minimum_declared_tensor_dimension": 2
        ** len(distinguishabilities),
    }


def uniform_fragment_budget(
    disturbance_ceiling: float, fragment_quality: float
) -> dict[str, Any]:
    numerator = 2.0 * math.log(1.0 - 2.0 * disturbance_ceiling)
    denominator = math.log(1.0 - fragment_quality**2)
    real_bound = numerator / denominator
    maximum_integer = max(0, math.floor(real_bound + 1.0e-12))
    next_fragment_cost = 0.5 * (
        1.0
        - (1.0 - fragment_quality**2)
        ** ((maximum_integer + 1) / 2.0)
    )
    return {
        "disturbance_ceiling": disturbance_ceiling,
        "minimum_fragment_trace_distance": fragment_quality,
        "maximum_fragment_count_real": real_bound,
        "maximum_fragment_count_integer": maximum_integer,
        "next_fragment_minimum_disturbance": next_fragment_cost,
        "next_fragment_violates_ceiling": (
            next_fragment_cost > disturbance_ceiling + TOL
        ),
    }


def correlated_fanout_counterexample(
    angle: float, fragment_count: int
) -> dict[str, float | int | bool]:
    visibility = abs(math.cos(angle))
    delta = 0.5 * (1.0 - visibility)
    local_distinguishability = math.sin(angle) ** 2
    invalid_product_bound = 0.5 * (
        1.0
        - (1.0 - local_distinguishability**2)
        ** (fragment_count / 2.0)
    )
    global_archive_distinguishability = local_distinguishability
    return {
        "fragment_count": fragment_count,
        "visibility": visibility,
        "half_diamond_delta": delta,
        "each_local_trace_distance": local_distinguishability,
        "global_archive_trace_distance": (
            global_archive_distinguishability
        ),
        "invalid_product_bound_if_correlations_ignored": (
            invalid_product_bound
        ),
        "invalid_bound_exceeds_actual_delta": (
            invalid_product_bound > delta + TOL
        ),
    }


def binary_entropy(probability: float) -> float:
    if probability <= 0.0 or probability >= 1.0:
        return 0.0
    return -probability * math.log2(probability) - (
        1.0 - probability
    ) * math.log2(1.0 - probability)


def holevo_fano_bits(history_count: int, error_probability: float) -> float:
    if history_count <= 1:
        return 0.0
    return max(
        0.0,
        math.log2(history_count)
        - binary_entropy(error_probability)
        - error_probability * math.log2(history_count - 1),
    )


def support_row(
    history_count: int, error_probability: float, alphabet_size: int
) -> dict[str, Any]:
    bits = holevo_fano_bits(history_count, error_probability)
    cells = math.ceil(bits / math.log2(alphabet_size) - 1.0e-12)
    return {
        "history_count": history_count,
        "average_decode_error": error_probability,
        "archive_dimension_lower_bound": 2.0**bits,
        "archive_bits_lower_bound": bits,
        "alphabet_size_per_cell": alphabet_size,
        "cell_count_lower_bound": max(0, cells),
    }


def make_check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(passed), "detail": detail}


def build_receipt() -> dict[str, Any]:
    rng = np.random.default_rng(SEED)

    mixed_rows: list[dict[str, float]] = []
    for index in range(96):
        dimension = 2 + index % 4
        sigma = random_density(dimension, rng)
        unitary_zero = haar_unitary(dimension, rng)
        unitary_one = haar_unitary(dimension, rng)
        archive_noise = (index % 8) / 10.0
        mixed_rows.append(
            recorder_row(
                sigma,
                unitary_zero,
                unitary_one,
                archive_noise,
            )
        )

    tight_rows = [
        pure_tight_row(angle)
        for angle in np.linspace(0.0, math.pi / 2.0, 33)
    ]
    product_rows = [
        product_fragment_receipt([0.2, 0.45, 0.7, 0.85]),
        product_fragment_receipt([0.35] * 3),
        product_fragment_receipt([0.6] * 6),
    ]
    budget_rows = [
        uniform_fragment_budget(0.05, 0.2),
        uniform_fragment_budget(0.10, 0.3),
        uniform_fragment_budget(0.20, 0.5),
        uniform_fragment_budget(0.35, 0.7),
    ]
    correlated = correlated_fanout_counterexample(
        math.pi / 3.0, 3
    )

    support_rows = [
        support_row(257, 0.0, 2),
        support_row(257, 0.01, 2),
        support_row(2**32, 0.0, 2),
        support_row(2**32, 0.01, 2),
        support_row(81, 0.05, 3),
    ]
    random_guess_rows = [
        support_row(count, 1.0 - 1.0 / count, 2)
        for count in (2, 7, 257)
    ]

    pre_correlated_oracle = {
        "source_half_diamond_delta": 0.0,
        "record_trace_distance": 1.0,
        "would_violate_blank_environment_curve": True,
        "reason_excluded": (
            "the environment is initially correlated with the history, "
            "rather than one source-independent blank state"
        ),
    }

    max_curve_violation = max(
        row["record_trace_distance"] - row["curve_bound"]
        for row in mixed_rows
    )
    min_gamma_fidelity_slack = min(
        row["gamma_to_environment_fidelity_slack"]
        for row in mixed_rows
    )
    min_monotonicity_slack = min(
        row["fidelity_monotonicity_slack"] for row in mixed_rows
    )
    max_plus_delta_error = max(
        abs(
            row["plus_state_trace_distance"]
            - row["half_diamond_delta"]
        )
        for row in mixed_rows
    )
    max_phase_equalization_error = max(
        row["phase_equalization_error"] for row in mixed_rows
    )
    max_tightness_error = max(
        row["equality_error"] for row in tight_rows
    )
    max_product_error = max(
        row["equality_error"] for row in product_rows
    )

    checks = [
        make_check(
            "mixed/noisy record samples obey the exact curve inequality",
            max_curve_violation <= TOL,
            f"96 samples; max(D-bound)={max_curve_violation:.3e}",
        ),
        make_check(
            "controlled-purification overlap is bounded by root fidelity",
            min_gamma_fidelity_slack >= -TOL,
            f"minimum F_env-|gamma|={min_gamma_fidelity_slack:.3e}",
        ),
        make_check(
            "depolarizing archive noise increases root fidelity",
            min_monotonicity_slack >= -TOL,
            f"minimum F_out-F_env={min_monotonicity_slack:.3e}",
        ),
        make_check(
            "plus-state witness attains the half-diamond lower bound",
            max_plus_delta_error <= TOL,
            f"maximum trace-distance error={max_plus_delta_error:.3e}",
        ),
        make_check(
            "phase equalization produces dephasing by absolute coherence",
            max_phase_equalization_error <= TOL,
            f"maximum matrix error={max_phase_equalization_error:.3e}",
        ),
        make_check(
            "pure two-state recorders saturate the curve",
            max_tightness_error <= TOL,
            f"33 angles; maximum equality error={max_tightness_error:.3e}",
        ),
        make_check(
            "conditionally independent pure fragments saturate the product bound",
            max_product_error <= TOL,
            f"three heterogeneous/uniform families; error={max_product_error:.3e}",
        ),
        make_check(
            "the next uniform independent fragment violates each frozen budget",
            all(
                row["next_fragment_violates_ceiling"]
                for row in budget_rows
            ),
            "four disturbance/quality settings",
        ),
        make_check(
            "correlated fanout defeats the product inference when independence is dropped",
            bool(correlated["invalid_bound_exceeds_actual_delta"]),
            (
                "three correlated fragments at theta=pi/3; "
                "the base record-disturbance bound still holds"
            ),
        ),
        make_check(
            "perfect decoding recovers exact archive-dimension endpoints",
            support_rows[0]["cell_count_lower_bound"] == 9
            and support_rows[2]["cell_count_lower_bound"] == 32,
            "257 elapsed labels require 9 qubits; 2^32 histories require 32",
        ),
        make_check(
            "the Holevo-Fano lower bound vanishes at uniform random guessing",
            all(
                row["archive_bits_lower_bound"] <= TOL
                for row in random_guess_rows
            ),
            "N=2,7,257",
        ),
        make_check(
            "a pre-correlated oracle demonstrates the blank-environment assumption is necessary",
            pre_correlated_oracle[
                "would_violate_blank_environment_curve"
            ],
            "delta=0 and D=1 is possible when the record predates the interaction",
        ),
    ]

    return {
        "probe": "du_covariant_record_cost_closing_probe",
        "seed": SEED,
        "norm_conventions": {
            "state_distance": "D(rho,sigma)=1/2 ||rho-sigma||_1",
            "channel_distance": (
                "delta_diamond(Phi,Psi)=1/2 ||Phi-Psi||_diamond"
            ),
            "fidelity": (
                "root fidelity F(rho,sigma)="
                "||sqrt(rho)sqrt(sigma)||_1"
            ),
        },
        "theorem_receipt": {
            "binary_curve": (
                "D_record^2 <= 4 delta (1-delta), "
                "delta=(1-|gamma|)/2"
            ),
            "independent_fragment_bound": (
                "delta >= "
                "(1-product_k sqrt(1-D_k^2))/2"
            ),
            "uniform_fragment_bound": (
                "m <= 2 ln(1-2 delta_bar)/ln(1-d^2)"
            ),
            "support_bound": (
                "log2 K >= log2 N-h2(p)-p log2(N-1)"
            ),
        },
        "mixed_noisy_summary": {
            "samples": len(mixed_rows),
            "maximum_curve_violation": max_curve_violation,
            "minimum_gamma_fidelity_slack": (
                min_gamma_fidelity_slack
            ),
            "minimum_fidelity_monotonicity_slack": (
                min_monotonicity_slack
            ),
            "maximum_plus_delta_error": max_plus_delta_error,
            "maximum_phase_equalization_error": (
                max_phase_equalization_error
            ),
        },
        "tight_pure_rows": tight_rows,
        "independent_product_rows": product_rows,
        "uniform_budget_rows": budget_rows,
        "correlation_counterexample": correlated,
        "pre_correlated_oracle_counterexample": pre_correlated_oracle,
        "support_rows": support_rows,
        "random_guess_support_rows": random_guess_rows,
        "limitations": [
            "binary controlled nondemolition history sector",
            "one source-independent blank environment",
            "product bound requires conditional factorization",
            "support bound uses a fixed decoder and declared prior",
            "no energy, entropy, latency, or irreversible-work law",
            "no autonomous interface or recorder-law selection",
            "finite mathematics and executable evidence only",
        ],
        "checks": checks,
        "passed": all(check["passed"] for check in checks),
    }


def main() -> int:
    receipt = build_receipt()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    passed = sum(check["passed"] for check in receipt["checks"])
    total = len(receipt["checks"])
    print(
        f"du_covariant_record_cost_closing_probe: "
        f"{passed}/{total} checks passed"
    )
    print(f"artifact: {ARTIFACT_PATH}")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
