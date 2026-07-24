#!/usr/bin/env python3
"""Conditional finality-knee probe for SWING-DU-SCI-01 Track 3.

This is a conditional construction, not a derivation of finality.

STANDARD COMPARATOR
-------------------
For a path qubit S and R imperfect pure record qubits,

    |Psi_R> = (|0>|e_0>^R + |1>|e_1>^R) / sqrt(2),
    F = |<e_0|e_1>|^2,

the ordinary unitary visibility is V_unitary(R,F) = F^(R/2).  Applying the
inverse of every record interaction restores V=1 exactly, for every finite R.

CONDITIONAL POSIT
-----------------
Define additive branch information

    M(R,F) = -ln |<E_0|E_1>|^2 = -R ln F.

Insert a sharp finality threshold M >= M_c and a persistent finality flag.  Once
the flag is raised, the model applies an irreversible dephasing factor q and an
otherwise exact global eraser can recover at most q.  The default q=0 represents
the strong "unrecoverable" posit.

WHAT IS ACTUALLY TESTED
-----------------------
Given those posits, the probe derives and checks:

* R_c(F) = ceil(M_c / -ln F);
* the continuous-threshold unitary visibility V_c = exp(-M_c/2), independent of
  single-record fidelity;
* the integer-lattice overshoot bound at the first crossing;
* a history-dependent post-erasure surface (hysteresis) after crossing.

It compares these consequences with standard exact unitary erasure, a smooth
irreversible-dephasing null, a count-only threshold absorber, and an arbitrarily
steep smooth sigmoid absorber.  The last control is deliberately hostile: on
any finite grid with no independent slope bound, a continuous sigmoid can mimic
the inserted step to arbitrary precision.  Therefore a knee alone is not an
identifiable or novel prediction.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Any

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    write_candidate_artifact,
)


DEFAULT_INFORMATION_THRESHOLD = 2.0
DEFAULT_FINAL_COHERENCE = 0.0
FIDELITIES = (0.20, 0.40, 0.60, 0.80, 0.90, 0.95, 0.98)
NUMERIC_TOL = 1e-11


def record_information(fidelity: float) -> float:
    """Pure-state Chernoff/branch information per independent record, in nats."""
    if not 0.0 <= fidelity <= 1.0:
        raise ValueError("fidelity must lie in [0,1]")
    if fidelity == 0.0:
        return math.inf
    if fidelity == 1.0:
        return 0.0
    return -math.log(fidelity)


def unitary_visibility(record_count: int, fidelity: float) -> float:
    """Reduced path visibility before erasing the record interactions."""
    if record_count < 0:
        raise ValueError("record_count must be nonnegative")
    return fidelity ** (0.5 * record_count)


def first_crossing(
    fidelity: float, information_threshold: float
) -> tuple[float, int | None]:
    """Return continuous and first-integer threshold locations."""
    if information_threshold <= 0.0:
        raise ValueError("information_threshold must be positive")
    per_record = record_information(fidelity)
    if per_record == 0.0:
        return math.inf, None
    if math.isinf(per_record):
        return 0.0, 1
    continuous = information_threshold / per_record
    # The subtraction only removes floating-point overshoot at an exact integer.
    integer = max(1, math.ceil(continuous - 1e-12))
    return continuous, integer


def finality_recovery(
    maximum_information_exposure: float,
    information_threshold: float,
    final_coherence: float,
) -> float:
    """Visibility after an otherwise exact eraser under the persistent threshold posit."""
    return (
        1.0
        if maximum_information_exposure < information_threshold
        else final_coherence
    )


def smooth_irreversible_recovery(
    maximum_information_exposure: float, dephasing_rate: float
) -> float:
    """Memoryful but smooth irreversible-dephasing null."""
    return math.exp(-dephasing_rate * maximum_information_exposure)


def _apply_controlled_record_rotation(
    state: np.ndarray,
    record_count: int,
    target_record: int,
    rotation: np.ndarray,
) -> np.ndarray:
    """Apply rotation to one record conditional on path S=1.

    Basis convention: S is the most-significant bit, followed by record qubits.
    """
    dimension = 1 << (record_count + 1)
    system_mask = 1 << record_count
    target_mask = 1 << (record_count - 1 - target_record)
    out = state.copy()
    for index_zero in range(dimension):
        if not (index_zero & system_mask) or (index_zero & target_mask):
            continue
        index_one = index_zero | target_mask
        pair = rotation @ np.array(
            [state[index_zero], state[index_one]], dtype=complex
        )
        out[index_zero], out[index_one] = pair[0], pair[1]
    return out


def _path_visibility(state: np.ndarray, record_count: int) -> float:
    branches = state.reshape(2, 1 << record_count)
    reduced = branches @ branches.conj().T
    return float(2.0 * abs(reduced[0, 1]))


def explicit_unitary_record_model(
    record_count: int, fidelity: float
) -> dict[str, float]:
    """Build the finite-dimensional record circuit and exactly reverse it."""
    dimension = 1 << (record_count + 1)
    state = np.zeros(dimension, dtype=complex)
    state[0] = 1.0 / math.sqrt(2.0)
    state[1 << record_count] = 1.0 / math.sqrt(2.0)

    overlap = math.sqrt(fidelity)
    distinguishability = math.sqrt(1.0 - fidelity)
    rotation = np.array(
        [
            [overlap, -distinguishability],
            [distinguishability, overlap],
        ],
        dtype=complex,
    )

    for target in range(record_count):
        state = _apply_controlled_record_rotation(
            state, record_count, target, rotation
        )
    entangled_visibility = _path_visibility(state, record_count)

    for target in reversed(range(record_count)):
        state = _apply_controlled_record_rotation(
            state, record_count, target, rotation.conj().T
        )
    erased_visibility = _path_visibility(state, record_count)
    return {
        "entangled_visibility": entangled_visibility,
        "analytic_visibility": unitary_visibility(record_count, fidelity),
        "erased_visibility": erased_visibility,
    }


def standard_unitary_control() -> dict[str, Any]:
    cases: list[dict[str, float | int]] = []
    max_formula_error = 0.0
    max_erasure_error = 0.0
    for fidelity in (0.2, 0.5, 0.8, 0.95):
        for record_count in range(1, 7):
            result = explicit_unitary_record_model(record_count, fidelity)
            formula_error = abs(
                result["entangled_visibility"] - result["analytic_visibility"]
            )
            erasure_error = abs(result["erased_visibility"] - 1.0)
            max_formula_error = max(max_formula_error, formula_error)
            max_erasure_error = max(max_erasure_error, erasure_error)
            cases.append(
                {
                    "fidelity": fidelity,
                    "record_count": record_count,
                    **result,
                    "formula_error": formula_error,
                    "erasure_error": erasure_error,
                }
            )
    return {
        "cases": cases,
        "max_formula_error": max_formula_error,
        "max_erasure_error": max_erasure_error,
        "analytic_visibility_verified": max_formula_error < NUMERIC_TOL,
        "exact_global_erasure_verified": max_erasure_error < NUMERIC_TOL,
    }


def threshold_table(
    information_threshold: float, final_coherence: float
) -> list[dict[str, Any]]:
    table: list[dict[str, Any]] = []
    continuous_knee_visibility = math.exp(-0.5 * information_threshold)
    for fidelity in FIDELITIES:
        per_record = record_information(fidelity)
        continuous, integer = first_crossing(fidelity, information_threshold)
        if integer is None:
            raise AssertionError("the fixed fidelity grid excludes F=1")
        crossing_information = integer * per_record
        visibility_at_first_crossing = unitary_visibility(integer, fidelity)
        lower_bound = continuous_knee_visibility * math.sqrt(fidelity)
        table.append(
            {
                "single_record_fidelity_F": fidelity,
                "information_per_record_minus_ln_F_nats": per_record,
                "continuous_Rc": continuous,
                "first_integer_Rc": integer,
                "information_at_first_crossing_nats": crossing_information,
                "integer_overshoot_nats": (
                    crossing_information - information_threshold
                ),
                "standard_visibility_at_first_crossing": (
                    visibility_at_first_crossing
                ),
                "continuous_threshold_visibility_exp_minus_Mc_over_2": (
                    continuous_knee_visibility
                ),
                "integer_visibility_bound": {
                    "strict_lower": lower_bound,
                    "upper_inclusive": continuous_knee_visibility,
                },
                "post_ideal_eraser_before_crossing": 1.0,
                "post_ideal_eraser_after_crossing": final_coherence,
            }
        )
    return table


def threshold_positive_control(
    table: list[dict[str, Any]],
    information_threshold: float,
    final_coherence: float,
) -> dict[str, Any]:
    detections: list[dict[str, Any]] = []
    all_match = True
    all_bounds_hold = True
    for row in table:
        fidelity = float(row["single_record_fidelity_F"])
        expected = int(row["first_integer_Rc"])
        per_record = record_information(fidelity)
        observed: int | None = None
        for record_count in range(0, expected + 3):
            recovery = finality_recovery(
                record_count * per_record,
                information_threshold,
                final_coherence,
            )
            if recovery < 0.5 * (1.0 + final_coherence):
                observed = record_count
                break
        lower = float(row["integer_visibility_bound"]["strict_lower"])
        upper = float(row["integer_visibility_bound"]["upper_inclusive"])
        visibility = float(row["standard_visibility_at_first_crossing"])
        bound_holds = lower < visibility <= upper + NUMERIC_TOL
        all_match = all_match and observed == expected
        all_bounds_hold = all_bounds_hold and bound_holds
        detections.append(
            {
                "fidelity": fidelity,
                "expected_Rc": expected,
                "detected_Rc": observed,
                "matches": observed == expected,
                "integer_visibility_bound_holds": bound_holds,
            }
        )
    return {
        "detections": detections,
        "all_threshold_locations_recovered": all_match,
        "all_integer_overshoot_bounds_hold": all_bounds_hold,
    }


def smooth_null_comparison(
    information_threshold: float, final_coherence: float
) -> dict[str, Any]:
    # Calibrate the primary null to retain 5% coherence after twice the threshold
    # exposure.  That calibration is explicit and does not favor the sharp model.
    calibration_exposure = 2.0 * information_threshold
    calibration_recovery = 0.05
    rate = -math.log(calibration_recovery) / calibration_exposure
    exposures = np.linspace(0.0, calibration_exposure, 801)
    conditional = np.array(
        [
            finality_recovery(x, information_threshold, final_coherence)
            for x in exposures
        ]
    )
    smooth = np.exp(-rate * exposures)
    differences = np.abs(conditional - smooth)
    samples = {}
    for multiple in (0.0, 0.5, 0.99, 1.0, 1.01, 1.5, 2.0):
        exposure = multiple * information_threshold
        samples[f"{multiple:.2f}_Mc"] = {
            "exposure_nats": exposure,
            "conditional_recovery": finality_recovery(
                exposure, information_threshold, final_coherence
            ),
            "smooth_irreversible_recovery": smooth_irreversible_recovery(
                exposure, rate
            ),
        }
    return {
        "null": "V_smooth(M_max)=exp(-lambda M_max)",
        "calibration": {
            "V_smooth_at_2Mc": calibration_recovery,
            "lambda_per_nat": rate,
        },
        "samples": samples,
        "rmse_over_zero_to_2Mc": float(
            np.sqrt(np.mean((conditional - smooth) ** 2))
        ),
        "max_absolute_gap_over_zero_to_2Mc": float(differences.max()),
        "model_level_discriminator": (
            "The sharp model is exactly flat below Mc and discontinuous at Mc; "
            "the fixed-rate irreversible-dephasing null is smooth and loses "
            "recoverability below Mc."
        ),
    }


def hysteresis_control(
    information_threshold: float, final_coherence: float
) -> dict[str, Any]:
    fidelity = 0.8
    per_record = record_information(fidelity)
    _, crossing = first_crossing(fidelity, information_threshold)
    if crossing is None:
        raise AssertionError("F=0.8 must cross")
    maximum_records = crossing + 3
    maximum_exposure = maximum_records * per_record

    upward = []
    for current_records in range(maximum_records + 1):
        current_information = current_records * per_record
        upward.append(
            {
                "current_records": current_records,
                "current_information_nats": current_information,
                "post_eraser_visibility": finality_recovery(
                    current_information,
                    information_threshold,
                    final_coherence,
                ),
            }
        )

    downward = []
    for current_records in reversed(range(maximum_records + 1)):
        current_information = current_records * per_record
        downward.append(
            {
                "current_records": current_records,
                "current_information_nats": current_information,
                "maximum_information_exposure_nats": maximum_exposure,
                "post_eraser_visibility": finality_recovery(
                    maximum_exposure,
                    information_threshold,
                    final_coherence,
                ),
            }
        )

    initial_at_zero = upward[0]["post_eraser_visibility"]
    returned_at_zero = downward[-1]["post_eraser_visibility"]
    return {
        "protocol": (
            "Accumulate imperfect records past Rc, then exactly uncompute every "
            "record interaction and return current M to zero."
        ),
        "fidelity": fidelity,
        "first_integer_Rc": crossing,
        "maximum_records": maximum_records,
        "upward_sweep": upward,
        "downward_sweep_after_crossing": downward,
        "standard_unitary_visibility_after_complete_erasure": 1.0,
        "conditional_initial_visibility_at_M_zero": initial_at_zero,
        "conditional_returned_visibility_at_M_zero": returned_at_zero,
        "hysteresis_gap_at_same_current_M_zero": (
            initial_at_zero - returned_at_zero
        ),
        "warning": (
            "Hysteresis rejects standard unitary reversibility but is not unique "
            "to finality: any memoryful irreversible-dephasing law can also retain "
            "exposure history."
        ),
    }


def count_threshold_identifiability_control(
    table: list[dict[str, Any]],
) -> dict[str, Any]:
    reference_fidelity = 0.8
    reference = next(
        row
        for row in table
        if row["single_record_fidelity_F"] == reference_fidelity
    )
    fitted_count_threshold = int(reference["first_integer_Rc"])
    comparisons = []
    distinguishable_count = 0
    for row in table:
        information_prediction = int(row["first_integer_Rc"])
        differs = information_prediction != fitted_count_threshold
        distinguishable_count += int(differs)
        comparisons.append(
            {
                "fidelity": row["single_record_fidelity_F"],
                "information_threshold_Rc": information_prediction,
                "count_only_threshold_Rc": fitted_count_threshold,
                "distinguishable": differs,
            }
        )
    return {
        "absorber": (
            "A threshold on raw record count R alone, calibrated to the F=0.8 run."
        ),
        "single_fidelity_identifiability": (
            "ABSORBED: at the calibration fidelity the count and information "
            "thresholds make the same Rc claim."
        ),
        "multi_fidelity_identifiability": (
            "The information threshold predicts Rc(F)=ceil(Mc/-ln F), while "
            "the count-only threshold remains fixed."
        ),
        "fitted_count_threshold": fitted_count_threshold,
        "comparisons": comparisons,
        "number_of_other_fidelities_that_separate": distinguishable_count,
    }


def steep_smooth_absorption_control(
    table: list[dict[str, Any]],
    information_threshold: float,
    measurement_resolution: float = 0.01,
) -> dict[str, Any]:
    """Show that a finite-grid step can be absorbed by a sufficiently steep sigmoid."""
    sampled_exposures: list[float] = []
    for row in table:
        per_record = float(row["information_per_record_minus_ln_F_nats"])
        crossing = int(row["first_integer_Rc"])
        for record_count in range(0, crossing + 4):
            sampled_exposures.append(record_count * per_record)

    below = max(x for x in sampled_exposures if x < information_threshold)
    above = min(x for x in sampled_exposures if x >= information_threshold)
    midpoint = 0.5 * (below + above)
    finite_grid_gap = above - below
    target_error = 0.25 * measurement_resolution
    # At either nearest point this slope makes the logistic error <= target_error.
    slope = (
        2.2
        * math.log((1.0 - target_error) / target_error)
        / finite_grid_gap
    )

    def sigmoid(exposure: float) -> float:
        z = slope * (exposure - midpoint)
        if z > 50.0:
            return 0.0
        if z < -50.0:
            return 1.0
        return 1.0 / (1.0 + math.exp(z))

    max_error = 0.0
    for exposure in sampled_exposures:
        target = 1.0 if exposure < information_threshold else 0.0
        max_error = max(max_error, abs(sigmoid(exposure) - target))

    return {
        "absorber": (
            "V_absorb(M_max)=1/[1+exp(k(M_max-M0))], a smooth, memoryful "
            "irreversible-dephasing curve with unconstrained slope."
        ),
        "measurement_resolution": measurement_resolution,
        "nearest_sample_below_Mc": below,
        "nearest_sample_at_or_above_Mc": above,
        "finite_grid_information_gap": finite_grid_gap,
        "fitted_midpoint_M0": midpoint,
        "required_slope_k_per_nat": slope,
        "max_fit_error_on_all_sampled_points": max_error,
        "absorbs_within_resolution": max_error < measurement_resolution,
        "identifiability_verdict": (
            "KNEE_ALONE_NOT_IDENTIFIABLE: without an independently bounded "
            "maximum smooth-dephasing slope, a finite data grid cannot establish "
            "a mathematical discontinuity."
        ),
    }


def threshold_scale_sensitivity() -> list[dict[str, Any]]:
    rows = []
    for threshold in (1.0, 2.0, 4.0):
        fidelity = 0.8
        per_record = record_information(fidelity)
        continuous, integer = first_crossing(fidelity, threshold)
        if integer is None:
            raise AssertionError("F=0.8 must cross")
        rows.append(
            {
                "information_threshold_Mc_nats": threshold,
                "continuous_Rc_at_F_0.8": continuous,
                "first_integer_Rc_at_F_0.8": integer,
                "continuous_knee_visibility": math.exp(-0.5 * threshold),
                "integer_crossing_information_over_Mc": (
                    integer * per_record / threshold
                ),
            }
        )
    return rows


def build_candidate(
    information_threshold: float,
    final_coherence: float,
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU.SCI01.TRACK3.FINALITY-KNEE",
        "track": "SWING-DU-SCI-01 Track 3: conditional finality phenomenology",
        "question": (
            "If a sharp, persistent finality event occurs when additive branch "
            "information M=-R ln F reaches an imported threshold Mc, what "
            "recoverability curve, fidelity scaling, and hysteresis follow, and "
            "do they distinguish the construction from unitary erasure and "
            "smooth irreversible dephasing?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
        ],
        "assumptions": [
            {
                "id": "A_STANDARD_RECORDS",
                "statement": (
                    "R conditionally independent pure record qubits have "
                    "single-record branch fidelity F=|<e0|e1>|^2."
                ),
                "status": "STANDARD",
                "role": (
                    "Supplies the finite unitary which-path comparator and the "
                    "additive information formula."
                ),
            },
            {
                "id": "A_INFORMATION_TRIGGER",
                "statement": (
                    "Finality is triggered sharply when M(R,F)=-R ln F reaches Mc."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "This is the threshold law being tested; neither its form "
                    "nor its physical origin is derived."
                ),
            },
            {
                "id": "A_PERSISTENT_FLAG",
                "statement": (
                    "After the first crossing, a monotone finality flag survives "
                    "later unitary erasure and limits recovered coherence to q."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Creates the recoverability hysteresis; irreversibility is "
                    "inserted here rather than obtained from unitary dynamics."
                ),
            },
            {
                "id": "A_CAUSAL_REDUNDANCY_READING",
                "statement": (
                    "The effective record statistic is intended to be evaluated "
                    "on causal-order-local records rather than a simultaneity slice."
                ),
                "status": "PROJECT_NATIVE",
                "role": (
                    "Connects to the covariant-finality program, but this probe "
                    "does not construct the missing AQFT-local update."
                ),
            },
            {
                "id": "A_NUMERICAL_SCALE",
                "statement": (
                    f"The illustrative threshold is Mc={information_threshold:g} "
                    f"nats and the strong final coherence is q={final_coherence:g}."
                ),
                "status": "IMPORTED",
                "role": (
                    "Fixes a runnable specimen; no DU source currently selects "
                    "either value."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C_THRESHOLD_SCALE",
                "choice": f"Mc={information_threshold:g} nats",
                "why_not_forced": (
                    "No microscopic finality mechanism or measured scale fixes Mc."
                ),
                "sensitivity_test": (
                    "Repeat at Mc=1,2,4; Rc and the common knee visibility move "
                    "according to the displayed analytic laws."
                ),
            },
            {
                "id": "C_TRIGGER_STATISTIC",
                "choice": "M=-R ln F for independent pure records",
                "why_not_forced": (
                    "Correlated/mixed records admit other information and "
                    "effective-redundancy statistics."
                ),
                "sensitivity_test": (
                    "Vary F at fixed preparation and compare with a raw-count "
                    "threshold; later work must test correlated and mixed records."
                ),
            },
            {
                "id": "C_FINAL_COHERENCE",
                "choice": f"q={final_coherence:g}",
                "why_not_forced": (
                    "The strong unrecoverability posit chooses q=0; a mechanism "
                    "could instead leave residual coherence."
                ),
                "sensitivity_test": (
                    "Vary q in [0,0.2]; it changes the plateau and hysteresis "
                    "amplitude but not Rc(F)."
                ),
            },
            {
                "id": "C_NULL_FAMILY",
                "choice": (
                    "A fixed-rate exponential null plus an unconstrained-slope "
                    "sigmoid absorption control."
                ),
                "why_not_forced": (
                    "Irreversible environmental dynamics are not uniquely exponential."
                ),
                "sensitivity_test": (
                    "Allow the smooth slope to float; the finite-grid step becomes "
                    "unidentifiable unless an external slope bound is supplied."
                ),
            },
        ],
        "equations": [
            "|Psi_R>=(|0>|e0>^R+|1>|e1>^R)/sqrt(2), F=|<e0|e1>|^2.",
            "V_unitary(R,F)=F^(R/2); an exact inverse record unitary gives V_erase=1.",
            "M(R,F)=-R ln F and Rc(F)=ceil(Mc/[-ln F]) for 0<F<1.",
            "V_c at the continuous threshold equals exp(-Mc/2), independent of F.",
            (
                "V_conditional_after_eraser=1 if max_history(M)<Mc, else q; "
                "the max-history dependence is the inserted persistent flag."
            ),
            "V_smooth_after_eraser=exp(-lambda max_history(M)) for the primary null.",
        ],
        "observables": [
            "Reduced path visibility before erasure as a function of R and F.",
            "Visibility after applying the calibrated global inverse record interaction.",
            "First crossing Rc(F) while tuning single-record fidelity.",
            "Forward/backward recoverability at the same current M after a past crossing.",
            "Subthreshold slope and near-threshold jump at fixed R while continuously tuning F.",
        ],
        "comparators": [
            "Standard finite-dimensional unitary which-path dynamics with exact global erasure.",
            "A raw-record-count threshold calibrated at one fidelity.",
            "A smooth memoryful irreversible-dephasing law calibrated at twice Mc.",
            "A freely steep smooth sigmoid absorber on the finite measurement grid.",
        ],
        "null_models": [
            "Unitary QM: records suppress local visibility but an exact global inverse restores V=1 for every R.",
            "Smooth irreversible dephasing: recovered visibility is analytic in cumulative exposure and has no exact flat-then-jump law.",
            "Count-only threshold: Rc is independent of record fidelity after calibration.",
        ],
        "falsifiers": [
            "At fixed Mc, measured Rc(F) fails the 1/[-ln F] scaling beyond integer-crossing uncertainty.",
            "The inferred continuous-knee visibility is not common across record fidelities.",
            "A full inverse interaction restores V=1 after an alleged crossing.",
            "A bounded-slope smooth irreversible-dephasing model fits the preregistered multi-fidelity and reversal surface.",
            "The threshold update cannot be made causal-order local and violates the no-signaling proviso.",
        ],
        "stop_conditions": [
            "Stop calling the feature finality if it is only a fitted knee with no independently constrained smooth-null slope.",
            "Stop this independent-record formalization if modest record correlations destroy its Rc(F) relation; that closes the formalization, not every finality concept.",
            "Stop promotion if each failed fidelity scan requires a new Mc, q, or trigger statistic.",
            "Do not bank or seed a physical prediction until a mechanism selects the threshold law/scale and the locality-of-update proviso is discharged.",
        ],
        "result": {
            "claim": (
                "The labeled information-threshold and persistence posits entail "
                "a quantitative Rc(F), a common continuous-knee visibility, and "
                "a post-erasure history surface. These distinguish the specimen "
                "from unitary erasure, fixed-rate smooth dephasing, and a "
                "count-only threshold, but a freely steep smooth irreversible "
                "null absorbs any finite-grid knee. No finality mechanism or "
                "novel physical prediction is derived."
            ),
            "grade": (
                "CONDITIONAL_MODEL_ONLY / IDENTIFIABILITY_LIMITED; mathematical "
                "consequences verified, threshold law/scale and irreversibility "
                "inserted, no abductive preference or claim banking."
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Microscopic trigger, choice of information statistic for "
                "correlated/mixed records, threshold scale, residual coherence, "
                "AQFT-local implementation, experimental inverse fidelity, and "
                "an independent upper bound on smooth-null steepness remain open."
            ),
            "checks": checks,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=str(
            Path(__file__).parent
            / "artifacts"
            / "du_conditional_finality_knee_probe_result.json"
        ),
    )
    parser.add_argument(
        "--information-threshold",
        type=float,
        default=DEFAULT_INFORMATION_THRESHOLD,
    )
    parser.add_argument(
        "--final-coherence",
        type=float,
        default=DEFAULT_FINAL_COHERENCE,
    )
    args = parser.parse_args()

    if args.information_threshold <= 0.0:
        parser.error("--information-threshold must be positive")
    if not 0.0 <= args.final_coherence < 1.0:
        parser.error("--final-coherence must lie in [0,1)")

    standard = standard_unitary_control()
    table = threshold_table(
        args.information_threshold, args.final_coherence
    )
    positive = threshold_positive_control(
        table, args.information_threshold, args.final_coherence
    )
    smooth = smooth_null_comparison(
        args.information_threshold, args.final_coherence
    )
    hysteresis = hysteresis_control(
        args.information_threshold, args.final_coherence
    )
    count_control = count_threshold_identifiability_control(table)
    steep_absorber = steep_smooth_absorption_control(
        table, args.information_threshold
    )
    sensitivity = threshold_scale_sensitivity()

    continuous_visibilities = {
        round(
            float(
                row[
                    "continuous_threshold_visibility_exp_minus_Mc_over_2"
                ]
            ),
            14,
        )
        for row in table
    }
    checks = [
        {
            "name": "explicit circuit matches V=F^(R/2)",
            "pass": bool(standard["analytic_visibility_verified"]),
        },
        {
            "name": "explicit inverse record unitary restores V=1",
            "pass": bool(standard["exact_global_erasure_verified"]),
        },
        {
            "name": "injected threshold locations recover ceil(Mc/-ln F)",
            "pass": bool(positive["all_threshold_locations_recovered"]),
        },
        {
            "name": "integer first crossings obey the analytic visibility bound",
            "pass": bool(positive["all_integer_overshoot_bounds_hold"]),
        },
        {
            "name": "continuous threshold visibility collapses across fidelities",
            "pass": len(continuous_visibilities) == 1,
        },
        {
            "name": "persistent posit produces a nonzero reversal hysteresis gap",
            "pass": (
                float(hysteresis["hysteresis_gap_at_same_current_M_zero"])
                > 0.0
            ),
        },
        {
            "name": "multi-fidelity scan separates information and count thresholds",
            "pass": (
                int(count_control["number_of_other_fidelities_that_separate"])
                >= len(FIDELITIES) - 2
            ),
        },
        {
            "name": "finite-grid knee is absorbed by unconstrained steep smooth null",
            "pass": bool(steep_absorber["absorbs_within_resolution"]),
        },
    ]

    candidate = build_candidate(
        args.information_threshold,
        args.final_coherence,
        checks,
    )
    payload = {
        "parameters": {
            "information_threshold_Mc_nats": args.information_threshold,
            "final_coherence_q": args.final_coherence,
            "fidelities": list(FIDELITIES),
        },
        "standard_unitary_control": standard,
        "threshold_location_vs_fidelity": table,
        "threshold_positive_control": positive,
        "smooth_irreversible_null_comparison": smooth,
        "recoverability_hysteresis": hysteresis,
        "count_threshold_identifiability_control": count_control,
        "steep_smooth_absorption_control": steep_absorber,
        "threshold_scale_sensitivity": sensitivity,
        "inserted_vs_entailed": {
            "inserted": [
                "The trigger statistic M=-R ln F.",
                f"The threshold scale Mc={args.information_threshold:g} nats.",
                "A sharp rather than smooth crossing.",
                "Persistence of the finality flag after inverse record interactions.",
                f"The post-crossing coherence q={args.final_coherence:g}.",
            ],
            "entailed_given_the_insertions": [
                "Rc(F)=ceil(Mc/-ln F).",
                "Continuous-knee unitary visibility exp(-Mc/2), common across F.",
                "The integer-crossing visibility overshoot interval.",
                "The forward/backward post-erasure history surface.",
                "Separation from a raw-count threshold and a fixed-rate exponential null.",
            ],
            "not_entailed": [
                "A microscopic source of finality.",
                "The numerical value of Mc or q.",
                "A novel physical prediction from merely observing a knee.",
                "AQFT locality, covariance of the update, Born selection, or single outcome.",
                "Identification of a discontinuity from finite data without a smooth-slope bound.",
            ],
        },
        "verdict": {
            "status": "CONDITIONAL_MODEL_ONLY_IDENTIFIABILITY_LIMITED",
            "summary": (
                "The conditional model earns quantitative, falsifiable relations "
                "beyond saying 'a knee exists,' but it does not earn a finality "
                "mechanism or an abductive win over arbitrarily steep smooth "
                "irreversible dephasing."
            ),
            "claim_status_change": "none",
            "bankable": False,
        },
    }

    out = Path(args.out)
    write_candidate_artifact(out, candidate, payload)

    print("DU conditional finality-knee probe")
    print(
        "  unitary formula max error: "
        f"{standard['max_formula_error']:.3e}"
    )
    print(
        "  exact erasure max error: "
        f"{standard['max_erasure_error']:.3e}"
    )
    print(
        "  threshold locations recovered: "
        f"{positive['all_threshold_locations_recovered']}"
    )
    print(
        "  information-vs-count separations: "
        f"{count_control['number_of_other_fidelities_that_separate']}"
    )
    print(
        "  steep smooth absorber max error: "
        f"{steep_absorber['max_fit_error_on_all_sampled_points']:.3e}"
    )
    print(
        "  contract checks: "
        f"{sum(bool(check['pass']) for check in checks)}/{len(checks)}"
    )
    print("  grade: CONDITIONAL_MODEL_ONLY / IDENTIFIABILITY_LIMITED")
    print(f"  artifact: {out}")
    return 0 if all(bool(check["pass"]) for check in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
