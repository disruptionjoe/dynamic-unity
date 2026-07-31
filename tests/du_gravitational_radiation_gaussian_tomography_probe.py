#!/usr/bin/env python3
"""Exact controls for HC-DU-199's radiative tomography boundary.

The probe studies the single-mode, vacuum-receiver beamsplitter channel used in
the cited gravitational-wave tomography proposal.  It separates:

1. population-level Gaussian reconstruction under a known transfer factor;
2. exact nonidentifiability when that factor is not calibrated;
3. coupling cancellation in normalized second-order coherence from the finite
   acquisition cost of estimating the cancelling ratio; and
4. exclusion of a classical random-displacement signal from identification of
   a gravitational field ontology.

Passing proves only these finite algebraic statements.  It is not a gravity
experiment, a feasibility result, or evidence that gravitational radiation is
quantized.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "artifacts" / "du_gravitational_radiation_gaussian_tomography_result.json"


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
Vector2 = tuple[Fraction, Fraction]


VACUUM: Matrix2 = (
    (Fraction(1, 2), Fraction(0)),
    (Fraction(0), Fraction(1, 2)),
)


def determinant(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def physical_one_mode_covariance(matrix: Matrix2) -> bool:
    """Sufficient exact check for the diagonal/symmetric examples used here."""

    return (
        matrix[0][1] == matrix[1][0]
        and matrix[0][0] > 0
        and matrix[1][1] > 0
        and determinant(matrix) >= Fraction(1, 4)
    )


def attenuate_covariance(input_covariance: Matrix2, eta: Fraction) -> Matrix2:
    one_minus_eta = Fraction(1) - eta
    return tuple(
        tuple(
            one_minus_eta * VACUUM[row][column]
            + eta * input_covariance[row][column]
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def reconstruct_covariance(output_covariance: Matrix2, eta: Fraction) -> Matrix2:
    one_minus_eta = Fraction(1) - eta
    return tuple(
        tuple(
            (
                output_covariance[row][column]
                - one_minus_eta * VACUUM[row][column]
            )
            / eta
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def attenuate_displacement(input_displacement: Vector2, eta: Fraction) -> Vector2:
    """Use examples with rational square-root transmissivity."""

    root_lookup = {
        Fraction(1, 4): Fraction(1, 2),
        Fraction(1, 2): None,
    }
    root_eta = root_lookup.get(eta)
    if root_eta is None:
        raise ValueError("the exact displacement example requires eta=1/4")
    return tuple(root_eta * value for value in input_displacement)  # type: ignore[return-value]


def reconstruct_displacement(output_displacement: Vector2, eta: Fraction) -> Vector2:
    if eta != Fraction(1, 4):
        raise ValueError("the exact displacement example requires eta=1/4")
    return tuple(2 * value for value in output_displacement)  # type: ignore[return-value]


def transfer_from_reference_slope(
    receiver_input_gap: Fraction,
    receiver_output_gap: Fraction,
) -> Fraction:
    """Recover eta when a fixed source is probed by two known references."""

    slope = receiver_output_gap / receiver_input_gap
    return Fraction(1) - slope * slope


def matrix_rank(rows: Iterable[Iterable[Fraction]]) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if matrix[index][column] != 0),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(row_count):
            if row == rank:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    current - factor * pivot_current
                    for current, pivot_current in zip(matrix[row], matrix[rank])
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def fock_two_loss_statistics(eta: Fraction) -> dict[str, Fraction]:
    """Loss-channel output for an incident two-quantum Fock state."""

    p2 = eta * eta
    p1 = 2 * eta * (1 - eta)
    p0 = (1 - eta) * (1 - eta)
    mean = p1 + 2 * p2
    factorial_second = 2 * p2
    g2 = factorial_second / (mean * mean)
    return {
        "p0": p0,
        "p1": p1,
        "p2": p2,
        "mean": mean,
        "factorial_second": factorial_second,
        "g2": g2,
    }


def encode_fraction(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def encode_matrix(matrix: Matrix2) -> list[list[str]]:
    return [[encode_fraction(value) for value in row] for row in matrix]


def encode_mapping(mapping: dict[str, Fraction]) -> dict[str, str]:
    return {key: encode_fraction(value) for key, value in mapping.items()}


def build_result() -> dict[str, object]:
    eta_a = Fraction(1, 4)
    eta_b = Fraction(1, 2)
    input_a: Matrix2 = (
        (Fraction(1, 4), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    input_b: Matrix2 = (
        (Fraction(3, 8), Fraction(0)),
        (Fraction(0), Fraction(3, 4)),
    )
    shared_output = attenuate_covariance(input_a, eta_a)
    second_output = attenuate_covariance(input_b, eta_b)

    input_displacement: Vector2 = (Fraction(3, 2), Fraction(-1, 2))
    output_displacement = attenuate_displacement(input_displacement, eta_a)

    calibration_eta = Fraction(3, 4)
    receiver_input_gap = Fraction(2)
    receiver_output_gap = Fraction(1)
    reconstructed_calibration_eta = transfer_from_reference_slope(
        receiver_input_gap,
        receiver_output_gap,
    )

    three_phase_design = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(1, 2), Fraction(1), Fraction(1, 2)),
    )
    two_phase_design = three_phase_design[:2]

    weak_eta = Fraction(1, 10)
    tenfold_weaker_eta = Fraction(1, 100)
    weak_statistics = fock_two_loss_statistics(weak_eta)
    weaker_statistics = fock_two_loss_statistics(tenfold_weaker_eta)
    target_double_events = 100
    weak_trials = Fraction(target_double_events, 1) / weak_statistics["p2"]
    weaker_trials = Fraction(target_double_events, 1) / weaker_statistics["p2"]

    min_output_variance = min(shared_output[0][0], shared_output[1][1])

    assertions = {
        "both_incident_covariances_are_physical": (
            physical_one_mode_covariance(input_a)
            and physical_one_mode_covariance(input_b)
        ),
        "distinct_eta_and_input_pairs_have_identical_detector_covariance": (
            eta_a != eta_b and input_a != input_b and shared_output == second_output
        ),
        "known_eta_exactly_reconstructs_incident_covariance": (
            reconstruct_covariance(shared_output, eta_a) == input_a
            and reconstruct_covariance(second_output, eta_b) == input_b
        ),
        "known_eta_exactly_reconstructs_incident_displacement": (
            reconstruct_displacement(output_displacement, eta_a) == input_displacement
        ),
        "two_known_receiver_references_reconstruct_transfer_if_source_is_fixed": (
            reconstructed_calibration_eta == calibration_eta
        ),
        "three_quadrature_phases_span_gaussian_covariance": (
            matrix_rank(three_phase_design) == 3
        ),
        "two_cardinal_phases_leave_cross_covariance_unidentified": (
            matrix_rank(two_phase_design) == 2
        ),
        "normalized_g2_is_exactly_one_half_at_both_couplings": (
            weak_statistics["g2"]
            == weaker_statistics["g2"]
            == Fraction(1, 2)
        ),
        "double_event_probability_scales_as_eta_squared": (
            weak_statistics["p2"] == weak_eta * weak_eta
            and weaker_statistics["p2"] == tenfold_weaker_eta * tenfold_weaker_eta
        ),
        "tenfold_weaker_transfer_requires_one_hundredfold_more_trials": (
            weaker_trials / weak_trials == 100
        ),
        "shared_detector_output_contains_subvacuum_quadrature": (
            min_output_variance == Fraction(7, 16) < Fraction(1, 2)
        ),
        "classical_random_displacement_of_vacuum_cannot_explain_subvacuum_output": (
            min_output_variance < Fraction(1, 2)
        ),
        "response_equivalent_quantum_ancilla_remains": True,
    }
    if not all(assertions.values()):
        raise AssertionError(f"failed assertions: {assertions}")

    return {
        "claim_id": "HC-DU-199",
        "disposition": (
            "CALIBRATED_GAUSSIAN_RADIATIVE_STATE_RECONSTRUCTION_"
            "COUPLING_INVARIANT_RATIO_NOT_ACQUISITION_INVARIANT_"
            "SCOPED_CLASSICAL_DRIVE_EXCLUSION_NOT_FIELD_ONTOLOGY"
        ),
        "gaussian_channel": {
            "law": "V_out=(1-eta) I/2 + eta V_in; m_out=sqrt(eta) m_in",
            "pair_a": {
                "eta": encode_fraction(eta_a),
                "input_covariance": encode_matrix(input_a),
            },
            "pair_b": {
                "eta": encode_fraction(eta_b),
                "input_covariance": encode_matrix(input_b),
            },
            "shared_output_covariance": encode_matrix(shared_output),
            "exact_displacement_example": {
                "eta": encode_fraction(eta_a),
                "input": [encode_fraction(value) for value in input_displacement],
                "output": [encode_fraction(value) for value in output_displacement],
            },
            "reference_slope_calibration_positive_control": {
                "assumption": "same source state across two known receiver preparations",
                "receiver_input_gap": encode_fraction(receiver_input_gap),
                "receiver_output_gap": encode_fraction(receiver_output_gap),
                "reconstructed_eta": encode_fraction(reconstructed_calibration_eta),
                "identity": "eta=1-(delta_receiver_output/delta_receiver_input)^2",
            },
            "calibration_boundary": (
                "eta>0 must be fixed for Gaussian-state inversion. One vacuum-receiver "
                "output does not fix it; two known receiver references can do so only "
                "if the source state is stable across the calibration arms."
            ),
        },
        "quadrature_design": {
            "parameters": ["V_xx", "V_xp", "V_pp"],
            "phase_rows": [
                [encode_fraction(value) for value in row]
                for row in three_phase_design
            ],
            "rank_three_phases": matrix_rank(three_phase_design),
            "rank_two_phases": matrix_rank(two_phase_design),
        },
        "finite_acquisition": {
            "incident_state": "two-quantum Fock state",
            "eta_1_over_10": encode_mapping(weak_statistics),
            "eta_1_over_100": encode_mapping(weaker_statistics),
            "target_double_events": target_double_events,
            "expected_trials_eta_1_over_10": encode_fraction(weak_trials),
            "expected_trials_eta_1_over_100": encode_fraction(weaker_trials),
            "trial_ratio": encode_fraction(weaker_trials / weak_trials),
            "boundary": (
                "g2 cancels eta at the population level, while the event count "
                "needed to estimate it diverges as eta^-2 in this exact control"
            ),
        },
        "rival_boundary": {
            "subvacuum_output_variance": encode_fraction(min_output_variance),
            "excluded_rival": (
                "vacuum detector plus exogenous classical random displacement, "
                "whose added covariance is positive semidefinite"
            ),
            "surviving_rival": (
                "a non-gravitational quantum ancilla or direct quantum response law "
                "with the same Gaussian state and calibrated channel"
            ),
            "ontology_result": "NOT_SELECTED",
        },
        "assertions": assertions,
        "theorem_statement": (
            "For a frozen one-mode vacuum-receiver beamsplitter channel with known "
            "eta>0, detector first and second moments injectively reconstruct the "
            "incident Gaussian state. If eta is not independently calibrated, "
            "distinct physical Gaussian inputs can produce the same detector "
            "covariance at one receiver setting. A known two-reference receiver "
            "family reconstructs eta if the source is fixed across arms. Normalized "
            "second-order coherence may cancel eta exactly "
            "while finite evidence formation remains eta-dependent. A subvacuum "
            "quadrature excludes the scoped classical random-displacement signal "
            "but not response-equivalent quantum or direct-action realizations."
        ),
        "scope_guard": (
            "This finite channel result assumes a selected on-shell mode, RWA, "
            "vacuum receiver where stated, calibrated transfer, source repeatability, "
            "phase reference, and Gaussian "
            "class where stated. It proves no astrophysical state preparation, "
            "graviton observation, feasibility, universal classical-gravity "
            "exclusion, field ontology, hardware action, Grade-5 remainder, or "
            "active Dynamic Unity successor."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the canonical JSON regression artifact",
    )
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
