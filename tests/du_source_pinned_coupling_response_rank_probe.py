#!/usr/bin/env python3
"""Exact controls for HC-DU-161.

Passing proves only the declared local Jacobian rank and the one-output
coupling/loss counterexample in the frozen two-mode model. It establishes no
complete record packet, physical selector, anomalous response, empirical
result, new law, or new physics.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_source_pinned_coupling_response_rank_result.json"
)

Matrix3 = tuple[
    tuple[Fraction, Fraction, Fraction],
    tuple[Fraction, Fraction, Fraction],
    tuple[Fraction, Fraction, Fraction],
]


def determinant_3x3(matrix: Matrix3) -> Fraction:
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )


def response_jacobian(
    coupling: Fraction,
    kappa_readout: Fraction,
    kappa_buffer: Fraction,
) -> Matrix3:
    """Jacobian of (-kappa_r, g, g(kappa_r+kappa_b)/2).

    Columns are ordered (g, kappa_r, kappa_b).
    """
    half = Fraction(1, 2)
    return (
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (
            half * (kappa_readout + kappa_buffer),
            half * coupling,
            half * coupling,
        ),
    )


def weak_coupling_population_rate(
    coupling: Fraction,
    kappa_readout: Fraction,
    kappa_buffer: Fraction,
    kappa_parasitic: Fraction,
) -> Fraction:
    return (
        kappa_readout
        + 4 * coupling * coupling / kappa_buffer
        + kappa_parasitic
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    specimens = (
        (Fraction(1, 3), Fraction(1, 5), Fraction(7, 3)),
        (Fraction(2, 5), Fraction(3, 7), Fraction(11, 4)),
        (Fraction(5, 8), Fraction(2, 9), Fraction(13, 6)),
    )
    determinants = []
    for coupling, kappa_readout, kappa_buffer in specimens:
        determinant = determinant_3x3(
            response_jacobian(coupling, kappa_readout, kappa_buffer)
        )
        determinants.append(
            {
                "coupling": str(coupling),
                "kappa_readout": str(kappa_readout),
                "kappa_buffer": str(kappa_buffer),
                "determinant": str(determinant),
                "expected": str(coupling / 2),
                "pass": determinant == coupling / 2 and determinant != 0,
            }
        )

    # A one-scalar residual endpoint cannot distinguish these two parameter
    # pairs in the weak-coupling reduced model. Both stay in 4g/kappa_b < 0.7.
    kappa_readout = Fraction(1, 10)
    kappa_buffer = Fraction(40)
    twin_left = (Fraction(1), Fraction(9, 10))
    twin_right = (Fraction(2), Fraction(3, 5))
    left_rate = weak_coupling_population_rate(
        twin_left[0],
        kappa_readout,
        kappa_buffer,
        twin_left[1],
    )
    right_rate = weak_coupling_population_rate(
        twin_right[0],
        kappa_readout,
        kappa_buffer,
        twin_right[1],
    )
    endpoint_twin = {
        "kappa_readout": str(kappa_readout),
        "kappa_buffer": str(kappa_buffer),
        "left": {
            "coupling": str(twin_left[0]),
            "kappa_parasitic": str(twin_left[1]),
            "population_rate": str(left_rate),
            "four_g_over_kappa_buffer": str(4 * twin_left[0] / kappa_buffer),
        },
        "right": {
            "coupling": str(twin_right[0]),
            "kappa_parasitic": str(twin_right[1]),
            "population_rate": str(right_rate),
            "four_g_over_kappa_buffer": str(4 * twin_right[0] / kappa_buffer),
        },
        "same_endpoint_for_every_time": left_rate == right_rate,
        "distinct_parameters": twin_left != twin_right,
        "both_inside_source_low_pump_ratio": (
            4 * twin_left[0] / kappa_buffer < Fraction(7, 10)
            and 4 * twin_right[0] / kappa_buffer < Fraction(7, 10)
        ),
    }

    # The source's main operating ratio, using reported g/2pi=7.2 MHz and
    # kappa_b/2pi=21 MHz, is retained only as a scope flag.
    source_main_ratio = 4 * Fraction(72, 10) / Fraction(21)

    checks = {
        "three_response_jacobian_full_rank": all(
            item["pass"] for item in determinants
        ),
        "determinant_equals_g_over_two": all(
            item["determinant"] == item["expected"] for item in determinants
        ),
        "one_endpoint_has_exact_coupling_loss_twins": (
            endpoint_twin["same_endpoint_for_every_time"]
            and endpoint_twin["distinct_parameters"]
        ),
        "endpoint_twins_respect_low_pump_scope": (
            endpoint_twin["both_inside_source_low_pump_ratio"]
        ),
        "source_main_point_outside_strict_reflection_calibration_regime": (
            source_main_ratio > Fraction(7, 10)
        ),
        "source_main_point_inside_reported_release_model_regime": (
            source_main_ratio < Fraction(8, 5)
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"source-pinned coupling-rank checks failed: {failed}")

    result = {
        "probe": "du_source_pinned_coupling_response_rank_probe",
        "status": "PASS",
        "claim_id": "HC-DU-161",
        "scope": "peronnin_two_mode_release_local_rank_and_endpoint_control",
        "source": {
            "title": "Sequential dispersive measurement of a superconducting qubit",
            "arxiv": "1904.04635",
            "journal": "Physical Review Letters 124, 180502 (2020)",
        },
        "response": [
            "normalized_residual_population_slope",
            "phase_calibrated_buffer_output_slope",
            "phase_calibrated_buffer_output_curvature",
        ],
        "jacobian_specimens": determinants,
        "endpoint_twin": endpoint_twin,
        "source_main_four_g_over_kappa_buffer": str(source_main_ratio),
        "checks": checks,
        "disclaimer": (
            "Passing establishes only exact controls in the frozen two-mode "
            "model; it establishes no complete record packet, physical "
            "selector, anomalous response, empirical result, new law, or new "
            "physics."
        ),
    }
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
