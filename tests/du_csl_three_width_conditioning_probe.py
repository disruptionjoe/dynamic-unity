#!/usr/bin/env python3
"""Numerical conditioning controls for HC-DU-188 and PRED-DU-005.

The probe evaluates only equations already supplied by arXiv:2606.22707v4.
It tests whether the HC-DU-187 three-width contrast is numerically useful in
the proposal's benchmark regime before any hardware question is entertained.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_csl_three_width_conditioning_result.json"
)

KB = 1.380649e-23
TEMPERATURE = 0.4
MASS = 1.0e-18
RC = 1.0e-7
LOSS_BUDGET = 0.3
SOURCE_EXPOSURE = 5.0e5


def simpson(values: list[float], step: float) -> float:
    total = values[0] + values[-1]
    total += 4.0 * sum(values[1:-1:2])
    total += 2.0 * sum(values[2:-1:2])
    return total * step / 3.0


def breathing_factor(omega: float, q: float, panels: int = 20_000) -> float:
    """Return S_br for q=omega_0/omega using the v4 3D formula."""
    if panels % 2:
        raise ValueError("Simpson panels must be even")
    alpha = KB * TEMPERATURE / (MASS * omega**2 * RC**2)
    step = 2.0 * math.pi / panels
    numerator: list[float] = []
    denominator: list[float] = []
    for index in range(panels + 1):
        u = index * step
        path_weight = (1.0 - math.cos(u)) ** 2
        width_ratio = alpha * (
            math.sin(u) ** 2 + math.cos(u) ** 2 / q**2
        )
        denominator.append(path_weight)
        numerator.append(path_weight * (1.0 + width_ratio) ** (-2.5))
    return simpson(numerator, step) / simpson(denominator, step)


def normalized_contrast(
    omega: float,
    q_values: tuple[float, float, float],
) -> dict[str, object]:
    alpha = KB * TEMPERATURE / (MASS * omega**2 * RC**2)
    widths = tuple(alpha / q**2 for q in q_values)
    signals = tuple(breathing_factor(omega, q) for q in q_values)
    raw_weights = (
        widths[2] - widths[1],
        widths[0] - widths[2],
        widths[1] - widths[0],
    )
    scale = sum(abs(value) for value in raw_weights)
    weights = tuple(value / scale for value in raw_weights)
    contrast = sum(weight * signal for weight, signal in zip(weights, signals))
    return {
        "q_values": list(q_values),
        "width_variance_over_rc_squared": list(widths),
        "breathing_factors": list(signals),
        "l1_normalized_weights": list(weights),
        "breathing_contrast": contrast,
    }


def shot_requirement(
    contrast: dict[str, object],
    source_kernel: float,
    source_q: float,
    omega: float,
    lambda_point: float,
) -> dict[str, float]:
    source_breathing = breathing_factor(omega, source_q)
    pointlike_kernel = source_kernel / source_breathing
    exponent_amplitude = lambda_point * pointlike_kernel
    exponent_contrast = abs(
        exponent_amplitude * float(contrast["breathing_contrast"])
    )
    # For an L1-normalized contrast and equal per-shot visibility noise,
    # optimal allocation N_i proportional to |w_i| gives variance
    # exp(2 Lambda_loss)/N_total in the small-signal log-visibility limit.
    total_shots_5sigma = (
        25.0 * math.exp(2.0 * LOSS_BUDGET) / exponent_contrast**2
    )
    return {
        "source_breathing_factor": source_breathing,
        "pointlike_kernel_seconds": pointlike_kernel,
        "lambda_point_per_second": lambda_point,
        "exponent_amplitude": exponent_amplitude,
        "absolute_exponent_contrast": exponent_contrast,
        "optimistic_total_shots_5sigma": total_shots_5sigma,
        "exposure_penalty_vs_source_N0": total_shots_5sigma / SOURCE_EXPOSURE,
    }


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    baseline = {
        "omega": 2.0e3,
        "source_q": 5.0e3,
        "source_S": 4.82e-2,
        "source_kernel": 1.26e8,
        "lambda_min": 7.6e-11,
    }
    aggressive = {
        "omega": 1.0e3,
        "source_q": 1.0e4,
        "source_S": 2.41e-2,
        "source_kernel": 2.02e9,
        "lambda_min": 4.7e-12,
    }

    calculated_baseline = breathing_factor(
        baseline["omega"], baseline["source_q"]
    )
    calculated_aggressive = breathing_factor(
        aggressive["omega"], aggressive["source_q"]
    )
    checks.append(
        {
            "name": "baseline_breathing_factor_reproduces_rounded_source",
            "passed": abs(calculated_baseline - baseline["source_S"]) < 5.0e-5,
            "value": calculated_baseline,
        }
    )
    checks.append(
        {
            "name": "aggressive_breathing_factor_reproduces_rounded_source",
            "passed": abs(calculated_aggressive - aggressive["source_S"]) < 5.0e-5,
            "value": calculated_aggressive,
        }
    )

    convergence_pairs = (
        (baseline["omega"], baseline["source_q"]),
        (aggressive["omega"], aggressive["source_q"]),
    )
    convergence_error = max(
        abs(
            breathing_factor(omega, q, panels=10_000)
            - breathing_factor(omega, q, panels=20_000)
        )
        for omega, q in convergence_pairs
    )
    checks.append(
        {
            "name": "simpson_grid_converges_at_source_points",
            "passed": convergence_error < 1.0e-12,
            "max_absolute_delta": convergence_error,
        }
    )

    wide_q = (10.0, 20.0, 50.0)
    baseline_wide = normalized_contrast(baseline["omega"], wide_q)
    aggressive_wide = normalized_contrast(aggressive["omega"], wide_q)
    baseline_wide_shots = shot_requirement(
        baseline_wide,
        baseline["source_kernel"],
        baseline["source_q"],
        baseline["omega"],
        baseline["lambda_min"],
    )
    aggressive_wide_shots = shot_requirement(
        aggressive_wide,
        aggressive["source_kernel"],
        aggressive["source_q"],
        aggressive["omega"],
        aggressive["lambda_min"],
    )
    checks.append(
        {
            "name": "wide_baseline_contrast_still_costs_over_fifty_million_shots",
            "passed": baseline_wide_shots["optimistic_total_shots_5sigma"]
            > 5.0e7,
            "value": baseline_wide_shots["optimistic_total_shots_5sigma"],
        }
    )
    checks.append(
        {
            "name": "wide_aggressive_contrast_still_costs_over_ten_million_shots",
            "passed": aggressive_wide_shots["optimistic_total_shots_5sigma"]
            > 1.0e7,
            "value": aggressive_wide_shots["optimistic_total_shots_5sigma"],
        }
    )

    baseline_near_q = (500.0, 1_000.0, baseline["source_q"])
    aggressive_near_q = (500.0, 1_000.0, aggressive["source_q"])
    baseline_near = normalized_contrast(baseline["omega"], baseline_near_q)
    aggressive_near = normalized_contrast(
        aggressive["omega"], aggressive_near_q
    )
    baseline_near_shots = shot_requirement(
        baseline_near,
        baseline["source_kernel"],
        baseline["source_q"],
        baseline["omega"],
        baseline["lambda_min"],
    )
    aggressive_near_shots = shot_requirement(
        aggressive_near,
        aggressive["source_kernel"],
        aggressive["source_q"],
        aggressive["omega"],
        aggressive["lambda_min"],
    )
    checks.append(
        {
            "name": "source_near_baseline_contrast_is_catastrophically_conditioned",
            "passed": baseline_near_shots["optimistic_total_shots_5sigma"]
            > 1.0e19,
            "value": baseline_near_shots["optimistic_total_shots_5sigma"],
        }
    )
    checks.append(
        {
            "name": "source_near_aggressive_contrast_is_catastrophically_conditioned",
            "passed": aggressive_near_shots["optimistic_total_shots_5sigma"]
            > 1.0e17,
            "value": aggressive_near_shots["optimistic_total_shots_5sigma"],
        }
    )

    checks.append(
        {
            "name": "usable_curvature_probe_requires_orders_lower_prep_frequency",
            "passed": (
                baseline["source_q"] / max(wide_q) >= 100.0
                and aggressive["source_q"] / max(wide_q) >= 200.0
            ),
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-188",
        "prediction_id": "PRED-DU-005",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "source_model": {
            "arxiv_version": "2606.22707v4",
            "temperature_kelvin": TEMPERATURE,
            "mass_kg": MASS,
            "rc_m": RC,
            "loss_budget": LOSS_BUDGET,
            "benchmark_exposure": SOURCE_EXPOSURE,
        },
        "baseline": {
            "wide_redesign": baseline_wide,
            "wide_redesign_shots": baseline_wide_shots,
            "source_near": baseline_near,
            "source_near_shots": baseline_near_shots,
        },
        "aggressive": {
            "wide_redesign": aggressive_wide,
            "wide_redesign_shots": aggressive_wide_shots,
            "source_near": aggressive_near,
            "source_near_shots": aggressive_near_shots,
        },
        "earned_boundary": (
            "The HC-DU-187 three-width contrast is formally identifiable but "
            "catastrophically ill-conditioned near the proposal's actual "
            "tight-trap ratios. A measurable curvature contrast requires a "
            "large preparation redesign whose systematics and feasibility are "
            "not established by the source."
        ),
        "non_claims": [
            "The shot counts are optimistic source-model diagnostics, not an apparatus forecast.",
            "No complete nuisance family or timing monitor is supplied.",
            "No CSL parameter point is excluded or supported.",
            "No hardware search, provider, experiment, or paper is authorized.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the deterministic JSON result",
    )
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
