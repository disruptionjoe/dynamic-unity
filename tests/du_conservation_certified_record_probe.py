#!/usr/bin/env python3
"""Conservation-to-certified-record selector/no-go probe.

The probe implements a finite U(1)-conserving measurement architecture rather
than starting from a supplied source POVM.  A source qubit and a bounded phase
reference are measured by a joint PVM that commutes with their additive charge.
The PVM outcome is copied into explicit pointer and archive registers.

The executable checks four distinct statements:

* additive conservation plus an oriented apparatus reference implements an
  approximate equatorial record instrument;
* the instrument is robust over a declared perturbation ball and its complete
  selective maps are informationally tomographable;
* phase-rotated references have identical charge and scalar asymmetry budgets
  but implement different record axes under the same symmetric processor; and
* the resulting discrimination capability is exactly priced to the consumed
  oriented-reference resource and archive quality.

These are standard WAY/resource-theory/interferometric consequences.  Passing
supports a Dynamic Unity interface-necessity classification, not a new law,
ontology, or prediction.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_conservation_certified_record_result.json"
)
RUN_ID = "RUN-20260725-140945-conservation-certified-record"
TOL = 1.0e-10

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
N2 = np.array([[0, 0], [0, 1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)


def dagger(matrix: np.ndarray) -> np.ndarray:
    return matrix.conj().T


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def rounded(value: float) -> float:
    return round(float(value), 12)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def ket_density(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def matrix_unit(row: int, column: int) -> np.ndarray:
    value = np.zeros((2, 2), dtype=complex)
    value[row, column] = 1.0
    return value


def partial_trace_second(state: np.ndarray) -> np.ndarray:
    """Trace the second qubit from a two-qubit operator."""

    return np.trace(state.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def partial_trace_first(state: np.ndarray) -> np.ndarray:
    """Trace the first qubit from a two-qubit operator."""

    return np.trace(state.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def reference_state(alpha: float, visibility: float) -> np.ndarray:
    if not 0.0 <= visibility <= 1.0:
        raise ValueError("visibility must lie in [0, 1]")
    return np.array(
        [
            [0.5, 0.5 * visibility * np.exp(-1j * alpha)],
            [0.5 * visibility * np.exp(1j * alpha), 0.5],
        ],
        dtype=complex,
    )


def equatorial_state(sign: int, phi: float) -> np.ndarray:
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    vector = (KET0 + sign * np.exp(1j * phi) * KET1) / math.sqrt(2.0)
    return ket_density(vector)


def equatorial_observable(alpha: float) -> np.ndarray:
    return (
        math.cos(alpha) * X2
        + math.sin(alpha) * Y2
    )


def conserving_projectors(beta: float) -> dict[str, np.ndarray]:
    """Four-outcome PVM resolving total-charge sectors and their interference."""

    ket00 = np.kron(KET0, KET0)
    ket01 = np.kron(KET0, KET1)
    ket10 = np.kron(KET1, KET0)
    ket11 = np.kron(KET1, KET1)
    chi_plus = math.cos(beta) * ket10 + math.sin(beta) * ket01
    chi_minus = -math.sin(beta) * ket10 + math.cos(beta) * ket01
    return {
        "0": ket_density(ket00),
        "+": ket_density(chi_plus),
        "-": ket_density(chi_minus),
        "2": ket_density(ket11),
    }


def formation_isometry(projectors: dict[str, np.ndarray]) -> np.ndarray:
    """Write the joint PVM to four-level pointer and archive registers."""

    value = np.zeros((64, 4), dtype=complex)
    for label_index, projector in enumerate(projectors.values()):
        label = np.eye(4, dtype=complex)[:, label_index : label_index + 1]
        value += np.kron(np.kron(projector, label), label)
    return value


def selective_map(
    source: np.ndarray,
    reference: np.ndarray,
    projector: np.ndarray,
) -> np.ndarray:
    joint = np.kron(source, reference)
    selected = projector @ joint @ projector
    return partial_trace_second(selected)


def map_effect(
    operation: Callable[[np.ndarray], np.ndarray],
) -> np.ndarray:
    effect = np.zeros((2, 2), dtype=complex)
    for row in range(2):
        for column in range(2):
            probability = np.trace(operation(matrix_unit(row, column)))
            effect[column, row] = probability
    return effect


def choi_matrix(
    operation: Callable[[np.ndarray], np.ndarray],
) -> np.ndarray:
    value = np.zeros((4, 4), dtype=complex)
    for row in range(2):
        for column in range(2):
            value += np.kron(
                matrix_unit(row, column),
                operation(matrix_unit(row, column)),
            )
    return value


def tomography_reconstruction(
    operation: Callable[[np.ndarray], np.ndarray],
) -> np.ndarray:
    """Reconstruct a selective Choi map from four IC source preparations."""

    rho_zero = ket_density(KET0)
    rho_one = ket_density(KET1)
    rho_plus = ket_density((KET0 + KET1) / math.sqrt(2.0))
    rho_plus_i = ket_density((KET0 + 1j * KET1) / math.sqrt(2.0))

    output_zero = operation(rho_zero)
    output_one = operation(rho_one)
    output_x = 2.0 * operation(rho_plus) - output_zero - output_one
    output_y = 2.0 * operation(rho_plus_i) - output_zero - output_one
    output_01 = (output_x + 1j * output_y) / 2.0
    output_10 = (output_x - 1j * output_y) / 2.0

    outputs = {
        (0, 0): output_zero,
        (0, 1): output_01,
        (1, 0): output_10,
        (1, 1): output_one,
    }
    value = np.zeros((4, 4), dtype=complex)
    for (row, column), output in outputs.items():
        value += np.kron(matrix_unit(row, column), output)
    return value


def raw_archive_distribution(
    sign: int,
    phi: float,
    alpha: float,
    visibility: float,
    beta: float,
) -> dict[str, float]:
    source = equatorial_state(sign, phi)
    reference = reference_state(alpha, visibility)
    return {
        label: float(
            np.trace(projector @ np.kron(source, reference)).real
        )
        for label, projector in conserving_projectors(beta).items()
    }


def noisy_archive_distribution(
    raw: dict[str, float],
    archive_flip: float,
) -> dict[str, float]:
    if not 0.0 <= archive_flip <= 0.5:
        raise ValueError("archive_flip must lie in [0, 1/2]")
    return {
        "0": raw["0"],
        "+": (
            (1.0 - archive_flip) * raw["+"]
            + archive_flip * raw["-"]
        ),
        "-": (
            archive_flip * raw["+"]
            + (1.0 - archive_flip) * raw["-"]
        ),
        "2": raw["2"],
    }


def total_variation(
    left: dict[str, float],
    right: dict[str, float],
) -> float:
    return 0.5 * sum(abs(left[key] - right[key]) for key in left)


def predicted_contrast(
    phi: float,
    alpha: float,
    visibility: float,
    beta: float,
    archive_flip: float,
) -> float:
    return (
        (1.0 - 2.0 * archive_flip)
        * visibility
        * math.sin(2.0 * beta)
        * math.cos(phi - alpha)
    )


def scalar_resource_metrics(reference: np.ndarray) -> dict[str, float]:
    mean = float(np.trace(reference @ N2).real)
    variance = float(np.trace(reference @ N2 @ N2).real - mean**2)
    visibility = 2.0 * abs(reference[0, 1])
    return {
        "charge_mean": rounded(mean),
        "charge_variance": rounded(variance),
        "purity": rounded(float(np.trace(reference @ reference).real)),
        "u1_phase_qfi": rounded(visibility**2),
        "trace_asymmetry_to_twirl": rounded(visibility / 2.0),
    }


class Receipt:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(
        self,
        name: str,
        passed: bool,
        detail: str,
    ) -> None:
        self.checks.append(
            {
                "name": name,
                "passed": bool(passed),
                "detail": detail,
            }
        )

    def close(self) -> dict[str, Any]:
        passed = sum(check["passed"] for check in self.checks)
        return {
            "passed": passed,
            "total": len(self.checks),
            "all_passed": passed == len(self.checks),
            "checks": self.checks,
        }


def run() -> dict[str, Any]:
    receipt = Receipt()
    total_charge = np.kron(N2, I2) + np.kron(I2, N2)
    balanced = conserving_projectors(math.pi / 4.0)

    projector_sum = sum(
        balanced.values(),
        start=np.zeros((4, 4), dtype=complex),
    )
    orthogonality_error = max(
        max_abs(left @ right)
        for left_label, left in balanced.items()
        for right_label, right in balanced.items()
        if left_label != right_label
    )
    receipt.check(
        "joint_pvm_is_complete_and_orthogonal",
        max_abs(projector_sum - np.eye(4)) < TOL
        and orthogonality_error < TOL,
        f"sum_error={max_abs(projector_sum - np.eye(4)):.3e}; "
        f"orthogonality_error={orthogonality_error:.3e}",
    )

    conservation_error = max(
        max_abs(projector @ total_charge - total_charge @ projector)
        for projector in balanced.values()
    )
    receipt.check(
        "every_joint_record_projector_conserves_additive_charge",
        conservation_error < TOL,
        f"max_commutator_error={conservation_error:.3e}",
    )

    isometry = formation_isometry(balanced)
    isometry_error = max_abs(dagger(isometry) @ isometry - np.eye(4))
    output_charge = np.kron(np.kron(total_charge, np.eye(4)), np.eye(4))
    intertwining_error = max_abs(
        output_charge @ isometry - isometry @ total_charge
    )
    receipt.check(
        "pointer_archive_formation_is_an_isometry",
        isometry_error < TOL,
        f"isometry_error={isometry_error:.3e}",
    )
    receipt.check(
        "pointer_archive_formation_intertwines_charge",
        intertwining_error < TOL,
        f"intertwining_error={intertwining_error:.3e}",
    )

    alpha = 0.37
    visibility = 0.82
    reference = reference_state(alpha, visibility)
    operations = {
        label: (
            lambda source, projector=projector: selective_map(
                source,
                reference,
                projector,
            )
        )
        for label, projector in balanced.items()
    }
    effects = {
        label: map_effect(operation)
        for label, operation in operations.items()
    }
    expected_effects = {
        "0": 0.5 * ket_density(KET0),
        "+": 0.25 * (
            I2 + visibility * equatorial_observable(alpha)
        ),
        "-": 0.25 * (
            I2 - visibility * equatorial_observable(alpha)
        ),
        "2": 0.5 * ket_density(KET1),
    }
    effect_error = max(
        max_abs(effects[label] - expected_effects[label])
        for label in effects
    )
    effect_sum_error = max_abs(
        sum(effects.values(), start=np.zeros((2, 2), dtype=complex))
        - I2
    )
    receipt.check(
        "balanced_induced_povm_matches_exact_formula",
        effect_error < TOL,
        f"max_effect_error={effect_error:.3e}",
    )
    receipt.check(
        "induced_source_povm_is_complete",
        effect_sum_error < TOL,
        f"effect_sum_error={effect_sum_error:.3e}",
    )

    choi = {
        label: choi_matrix(operation)
        for label, operation in operations.items()
    }
    min_choi_eigenvalue = min(
        float(np.min(np.linalg.eigvalsh(matrix)).real)
        for matrix in choi.values()
    )
    receipt.check(
        "every_selective_source_map_is_completely_positive",
        min_choi_eigenvalue > -TOL,
        f"minimum_choi_eigenvalue={min_choi_eigenvalue:.3e}",
    )

    tomography = {
        label: tomography_reconstruction(operation)
        for label, operation in operations.items()
    }
    tomography_error = max(
        max_abs(tomography[label] - choi[label])
        for label in choi
    )
    receipt.check(
        "informationally_complete_instrument_tomography_recovers_all_choi_maps",
        tomography_error < TOL,
        f"max_choi_reconstruction_error={tomography_error:.3e}",
    )

    grid_phases = (-0.63, 0.0, 0.49, 1.07)
    grid_alphas = (-0.41, 0.13, 0.88)
    grid_visibilities = (0.0, 0.35, 0.8, 1.0)
    grid_betas = (0.47, math.pi / 4.0, 1.03)
    grid_archive_flips = (0.0, 0.07, 0.21, 0.49)
    distribution_error = 0.0
    variation_error = 0.0
    guess_error = 0.0
    for phi in grid_phases:
        for phase in grid_alphas:
            for coherence in grid_visibilities:
                for beta in grid_betas:
                    for archive_flip in grid_archive_flips:
                        observed: dict[int, dict[str, float]] = {}
                        predicted: dict[int, dict[str, float]] = {}
                        for sign in (-1, 1):
                            raw = raw_archive_distribution(
                                sign,
                                phi,
                                phase,
                                coherence,
                                beta,
                            )
                            observed[sign] = noisy_archive_distribution(
                                raw,
                                archive_flip,
                            )
                            contrast = predicted_contrast(
                                phi,
                                phase,
                                coherence,
                                beta,
                                archive_flip,
                            )
                            predicted[sign] = {
                                "0": 0.25,
                                "+": 0.25 * (1.0 + sign * contrast),
                                "-": 0.25 * (1.0 - sign * contrast),
                                "2": 0.25,
                            }
                            distribution_error = max(
                                distribution_error,
                                max(
                                    abs(
                                        observed[sign][label]
                                        - predicted[sign][label]
                                    )
                                    for label in observed[sign]
                                ),
                            )
                        measured_tv = total_variation(
                            observed[1],
                            observed[-1],
                        )
                        expected_tv = 0.5 * abs(
                            predicted_contrast(
                                phi,
                                phase,
                                coherence,
                                beta,
                                archive_flip,
                            )
                        )
                        variation_error = max(
                            variation_error,
                            abs(measured_tv - expected_tv),
                        )
                        measured_guess = 0.5 * (1.0 + measured_tv)
                        expected_guess = 0.5 + expected_tv / 2.0
                        guess_error = max(
                            guess_error,
                            abs(measured_guess - expected_guess),
                        )
    receipt.check(
        "archive_distribution_surface_matches_exact_formula",
        distribution_error < TOL,
        f"max_distribution_error={distribution_error:.3e}",
    )
    receipt.check(
        "accessible_distinguishability_matches_exact_formula",
        variation_error < TOL,
        f"max_total_variation_error={variation_error:.3e}",
    )
    receipt.check(
        "forced_guess_capability_matches_exact_formula",
        guess_error < TOL,
        f"max_guess_success_error={guess_error:.3e}",
    )

    perturbation = {
        "visibility_min": 0.8,
        "phase_radius": 0.2,
        "beam_splitter_radius": 0.1,
        "archive_flip_max": 0.1,
    }
    predicted_floor = (
        0.5
        * (1.0 - 2.0 * perturbation["archive_flip_max"])
        * perturbation["visibility_min"]
        * math.cos(2.0 * perturbation["beam_splitter_radius"])
        * math.cos(perturbation["phase_radius"])
    )
    boundary_observed = 0.5 * abs(
        predicted_contrast(
            perturbation["phase_radius"],
            0.0,
            perturbation["visibility_min"],
            math.pi / 4.0 + perturbation["beam_splitter_radius"],
            perturbation["archive_flip_max"],
        )
    )
    receipt.check(
        "declared_perturbation_ball_has_exact_positive_floor",
        predicted_floor > 0.0
        and abs(boundary_observed - predicted_floor) < TOL,
        f"floor={predicted_floor:.12f}; "
        f"boundary={boundary_observed:.12f}",
    )

    rng = np.random.default_rng(240725)
    off_grid_error = 0.0
    off_grid_floor_margin = float("inf")
    for _ in range(1000):
        phase_error = rng.uniform(
            -perturbation["phase_radius"],
            perturbation["phase_radius"],
        )
        splitter_error = rng.uniform(
            -perturbation["beam_splitter_radius"],
            perturbation["beam_splitter_radius"],
        )
        coherence = rng.uniform(
            perturbation["visibility_min"],
            1.0,
        )
        archive_flip = rng.uniform(
            0.0,
            perturbation["archive_flip_max"],
        )
        left = noisy_archive_distribution(
            raw_archive_distribution(
                1,
                phase_error,
                0.0,
                coherence,
                math.pi / 4.0 + splitter_error,
            ),
            archive_flip,
        )
        right = noisy_archive_distribution(
            raw_archive_distribution(
                -1,
                phase_error,
                0.0,
                coherence,
                math.pi / 4.0 + splitter_error,
            ),
            archive_flip,
        )
        observed_tv = total_variation(left, right)
        expected_tv = 0.5 * abs(
            predicted_contrast(
                phase_error,
                0.0,
                coherence,
                math.pi / 4.0 + splitter_error,
                archive_flip,
            )
        )
        off_grid_error = max(
            off_grid_error,
            abs(observed_tv - expected_tv),
        )
        off_grid_floor_margin = min(
            off_grid_floor_margin,
            observed_tv - predicted_floor,
        )
    receipt.check(
        "off_grid_perturbation_stress_matches_surface",
        off_grid_error < TOL,
        f"1000_case_max_error={off_grid_error:.3e}",
    )
    receipt.check(
        "off_grid_perturbation_stress_respects_floor",
        off_grid_floor_margin > -TOL,
        f"minimum_floor_margin={off_grid_floor_margin:.3e}",
    )

    orientation_zero = reference_state(0.0, 1.0)
    orientation_quarter = reference_state(math.pi / 2.0, 1.0)
    zero_metrics = scalar_resource_metrics(orientation_zero)
    quarter_metrics = scalar_resource_metrics(orientation_quarter)
    receipt.check(
        "phase_rotated_references_have_identical_scalar_resource_budget",
        zero_metrics == quarter_metrics,
        f"metrics={zero_metrics}",
    )

    zero_plus = map_effect(
        lambda source: selective_map(
            source,
            orientation_zero,
            balanced["+"],
        )
    )
    quarter_plus = map_effect(
        lambda source: selective_map(
            source,
            orientation_quarter,
            balanced["+"],
        )
    )
    zero_axis_error = max_abs(4.0 * zero_plus - I2 - X2)
    quarter_axis_error = max_abs(4.0 * quarter_plus - I2 - Y2)
    distinct_axis_distance = 0.5 * float(
        np.sum(
            np.linalg.svd(
                (4.0 * zero_plus - I2)
                - (4.0 * quarter_plus - I2),
                compute_uv=False,
            )
        )
    )
    receipt.check(
        "reference_orientation_rotates_effective_record_axis",
        zero_axis_error < TOL
        and quarter_axis_error < TOL
        and distinct_axis_distance > 1.0,
        f"x_axis_error={zero_axis_error:.3e}; "
        f"y_axis_error={quarter_axis_error:.3e}; "
        f"axis_trace_distance={distinct_axis_distance:.12f}",
    )

    aligned_raw = {
        sign: raw_archive_distribution(
            sign,
            0.0,
            0.0,
            1.0,
            math.pi / 4.0,
        )
        for sign in (-1, 1)
    }
    aligned_tv = total_variation(aligned_raw[1], aligned_raw[-1])
    aligned_success = 0.5 * (1.0 + aligned_tv)
    aligned_coverage = (
        aligned_raw[1]["+"] + aligned_raw[1]["-"]
    )
    aligned_conditional_success = (
        aligned_raw[1]["+"] / aligned_coverage
    )
    receipt.check(
        "aligned_oriented_reference_enables_strict_capability",
        abs(aligned_tv - 0.5) < TOL
        and abs(aligned_success - 0.75) < TOL
        and abs(aligned_coverage - 0.5) < TOL
        and abs(aligned_conditional_success - 1.0) < TOL,
        f"tv={aligned_tv:.12f}; forced_success={aligned_success:.12f}; "
        f"coverage={aligned_coverage:.12f}; "
        f"conditional_success={aligned_conditional_success:.12f}",
    )

    twirled_raw = {
        sign: raw_archive_distribution(
            sign,
            0.0,
            0.0,
            0.0,
            math.pi / 4.0,
        )
        for sign in (-1, 1)
    }
    twirled_tv = total_variation(twirled_raw[1], twirled_raw[-1])
    receipt.check(
        "twirled_reference_removes_equatorial_capability",
        twirled_tv < TOL,
        f"tv={twirled_tv:.3e}; forced_success={0.5 * (1 + twirled_tv):.12f}",
    )

    misaligned_raw = {
        sign: raw_archive_distribution(
            sign,
            0.0,
            math.pi / 2.0,
            1.0,
            math.pi / 4.0,
        )
        for sign in (-1, 1)
    }
    misaligned_tv = total_variation(
        misaligned_raw[1],
        misaligned_raw[-1],
    )
    receipt.check(
        "equal_asymmetry_with_quarter_turn_orientation_removes_target_capability",
        misaligned_tv < TOL,
        f"tv={misaligned_tv:.3e}; scalar_metrics={quarter_metrics}",
    )

    archive_flip = 0.17
    noisy_aligned = {
        sign: noisy_archive_distribution(
            aligned_raw[sign],
            archive_flip,
        )
        for sign in (-1, 1)
    }
    noisy_tv = total_variation(noisy_aligned[1], noisy_aligned[-1])
    receipt.check(
        "archive_noise_prices_observer_access_separately",
        abs(noisy_tv - (1.0 - 2.0 * archive_flip) * aligned_tv) < TOL,
        f"pointer_tv={aligned_tv:.12f}; archive_tv={noisy_tv:.12f}; "
        f"factor={1 - 2 * archive_flip:.12f}",
    )

    average_source = I2 / 2.0
    joint_initial = np.kron(average_source, orientation_zero)
    joint_after = sum(
        (
            projector @ joint_initial @ projector
            for projector in balanced.values()
        ),
        start=np.zeros((4, 4), dtype=complex),
    )
    reference_after = partial_trace_first(joint_after)
    consumed_asymmetry = (
        scalar_resource_metrics(orientation_zero)[
            "trace_asymmetry_to_twirl"
        ]
        - scalar_resource_metrics(reference_after)[
            "trace_asymmetry_to_twirl"
        ]
    )
    receipt.check(
        "oriented_reference_token_is_consumed_by_record_formation",
        max_abs(reference_after - I2 / 2.0) < TOL
        and abs(consumed_asymmetry - 0.5) < TOL,
        f"post_reference_twirl_error={max_abs(reference_after - I2 / 2):.3e}; "
        f"consumed_trace_asymmetry={consumed_asymmetry:.12f}",
    )

    final_receipt = receipt.close()
    result: dict[str, Any] = {
        "run_id": RUN_ID,
        "status": (
            "PASS_INTERFACE_NECESSITY_NO_GO_AND_STANDARD_CAPABILITY_SLICE"
            if final_receipt["all_passed"]
            else "FAIL"
        ),
        "claim_grade": (
            "EXACT FINITE U1-CONSERVING MODEL / STANDARD WAY-ASYMMETRY "
            "SPECIALIZATION / NO NEW PHYSICS, THEOREM ID, OR PREDICTION"
        ),
        "scientific_verdict": {
            "positive": (
                "An oriented bounded reference plus one fixed symmetric "
                "processor forms a robust, completely tomographable "
                "equatorial record instrument."
            ),
            "no_go": (
                "Additive conservation and any symmetry-invariant scalar "
                "asymmetry budget select only a measurement orbit: "
                "phase-rotated apparatus states have identical budgets but "
                "implement different source record axes."
            ),
            "minimal_extra_structure": [
                "an oriented reference token or equivalent symmetry-breaking preparation",
                "a fixed symmetric processor/coupling architecture",
                "a pointer and durable archive boundary",
                "a decoder and action task",
                "complete selective-map access when continuation matters",
            ],
            "absorber": (
                "Wigner-Araki-Yanase constraints, quantum reference frames, "
                "asymmetry resource theory, no-programming, state "
                "discrimination, and standard instrument tomography."
            ),
            "branch_disposition": (
                "Close further finite selector fitting. Conservation "
                "constrains the feasible class; oriented apparatus state "
                "programs the axis; tomography identifies but does not "
                "causally select the instrument."
            ),
        },
        "exact_relations": {
            "accessible_total_variation": (
                "0.5*(1-2*q)*v*abs(sin(2*beta)*cos(phi-alpha))"
            ),
            "forced_guess_success": (
                "0.5+0.25*(1-2*q)*v*abs(sin(2*beta)*cos(phi-alpha))"
            ),
            "perturbation_floor": rounded(predicted_floor),
        },
        "tomography": {
            "preparations": ["|0>", "|1>", "|+>", "|+i>"],
            "selective_outcomes": ["0", "+", "-", "2"],
            "max_choi_reconstruction_error": tomography_error,
            "minimum_choi_eigenvalue": min_choi_eigenvalue,
        },
        "resource_and_capability": {
            "aligned_reference_metrics": zero_metrics,
            "quarter_turn_reference_metrics": quarter_metrics,
            "aligned_forced_guess_success": rounded(aligned_success),
            "aligned_conclusive_coverage": rounded(aligned_coverage),
            "aligned_conditional_success": rounded(
                aligned_conditional_success
            ),
            "twirled_forced_guess_success": rounded(
                0.5 * (1.0 + twirled_tv)
            ),
            "quarter_turn_forced_guess_success": rounded(
                0.5 * (1.0 + misaligned_tv)
            ),
            "consumed_trace_asymmetry": rounded(consumed_asymmetry),
            "interpretation": (
                "The strict capability delta is paid for by an oriented "
                "reference token and archive fidelity. It is not a free "
                "consequence of conservation, record finality, or observer "
                "access."
            ),
        },
        "stress_test": {
            "seed": 240725,
            "cases": 1000,
            "max_surface_error": off_grid_error,
            "minimum_floor_margin": off_grid_floor_margin,
        },
        "receipt": final_receipt,
    }
    return result


def main() -> None:
    result = run()
    payload = canonical_json(result)
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    print(
        f"{result['status']}: "
        f"{result['receipt']['passed']}/{result['receipt']['total']} checks"
    )
    print(f"artifact={ARTIFACT.relative_to(ROOT)}")
    print(f"sha256={digest}")
    if not result["receipt"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
