#!/usr/bin/env python3
"""Exact finite control for the GU-K77 luminous-polarization bridge.

The control keeps six types separate:

* the trace-reversed indefinite carrier;
* its W/mirror half grading and cross-pairing;
* the independent 2+1 origin split (two true-family slots and one imposter);
* the complete theory's fundamental chirality;
* an odd order parameter with a swap-symmetric curvature-dependent potential;
* a later material record instrument.

It proves a conditional positive result: a symmetric non-chiral parent can
select one relational light/luminous half per broken vacuum, and can restore
the paired phase when the quadratic coefficient changes sign.  It also proves
the two boundaries needed for honest GU/DU transfer: the 2+1 origin label does
not choose its coupling to that polarization, and the selected light sector
still does not select a record instrument.

Passing establishes no GU source action, luminous matter mechanism, observed
generation, chirality, record formation, new physics, or empirical prediction.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_gu_k77_luminous_polarization_bridge_result.json"
)
RUN_ID = "RUN-20260831-gu-k77-luminous-polarization-bridge"
TOL = 1.0e-12


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def check(name: str, condition: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(condition), "detail": detail}


def potential(z: float, coefficient: float) -> float:
    return 0.25 * z**4 + 0.5 * coefficient * z**2


def potential_gradient(z: float, coefficient: float) -> float:
    return z**3 + coefficient * z


def potential_hessian(z: float, coefficient: float) -> float:
    return 3.0 * z**2 + coefficient


def projector_probability(projector: np.ndarray, state: np.ndarray) -> float:
    return float(np.real(np.vdot(state, projector @ state)))


def build_result() -> dict[str, Any]:
    identity3 = np.eye(3)
    identity6 = np.eye(6)
    swap2 = np.array([[0.0, 1.0], [1.0, 0.0]])
    sign2 = np.diag([1.0, -1.0])

    # Basis: (true-1, W), (true-1, mirror), (true-2, W),
    # (true-2, mirror), (imposter, W), (imposter, mirror).
    exchange = np.kron(identity3, swap2)
    krein_pairing = exchange.copy()
    half_grading = np.kron(identity3, sign2)
    projector_w = 0.5 * (identity6 + half_grading)
    projector_m = 0.5 * (identity6 - half_grading)

    imposter_origin3 = np.diag([0.0, 0.0, 1.0])
    true_origin3 = np.eye(3) - imposter_origin3
    imposter_origin = np.kron(imposter_origin3, np.eye(2))
    true_origin = np.kron(true_origin3, np.eye(2))

    pairing_eigenvalues = np.linalg.eigvalsh(krein_pairing)
    positive_inertia = int(np.sum(pairing_eigenvalues > TOL))
    negative_inertia = int(np.sum(pairing_eigenvalues < -TOL))
    null_inertia = int(np.sum(np.abs(pairing_eigenvalues) <= TOL))

    low_coefficient = -1.0
    high_coefficient = 1.0
    low_stationary = (-1.0, 0.0, 1.0)
    low_minima = tuple(
        z
        for z in low_stationary
        if abs(potential_gradient(z, low_coefficient)) < TOL
        and potential_hessian(z, low_coefficient) > TOL
    )
    high_stationary = (0.0,)

    base_mass_squared = 2.0
    coupling = 1.0

    def response_mass(z: float) -> np.ndarray:
        return base_mass_squared * identity6 - coupling * z * half_grading

    mass_plus = response_mass(1.0)
    mass_minus = response_mass(-1.0)
    mass_high = response_mass(0.0)

    # The relational luminous projector follows the broken vacuum.  Absolute
    # W/mirror spelling is exchanged together with the order parameter.
    luminous_plus = projector_w
    luminous_minus = projector_m

    # The 2+1 origin label admits multiple swap-symmetric response couplings.
    # Nothing in the typed split alone selects either coefficient vector.
    equal_origin_coupling = np.diag([1.0, 1.0, 1.0])
    split_origin_coupling = np.diag([1.0, 1.0, 2.0])
    equal_response = np.kron(equal_origin_coupling, sign2)
    split_response = np.kron(split_origin_coupling, sign2)

    # Even after a vacuum selects W relationally, the two true-family slots
    # support an energy-preserving unitary ambiguity inside that sector.
    true_swap3 = np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    within_sector_twist = np.kron(true_swap3, np.eye(2))
    luders_kraus = (projector_w, projector_m)
    twisted_kraus = (
        within_sector_twist @ projector_w,
        projector_m,
    )
    effect_differences = tuple(
        float(np.linalg.norm(left.T @ left - right.T @ right))
        for left, right in zip(luders_kraus, twisted_kraus, strict=True)
    )
    true1_w = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    true2_w = twisted_kraus[0] @ true1_w
    conditional_overlap = abs(np.vdot(true1_w, true2_w))

    checks = [
        check(
            "paired_carrier_is_indefinite",
            (positive_inertia, negative_inertia, null_inertia) == (3, 3, 0),
            "the reduced W/mirror control has balanced nondegenerate Witt inertia",
        ),
        check(
            "individual_halves_are_null",
            np.allclose(projector_w.T @ krein_pairing @ projector_w, 0.0, atol=TOL)
            and np.allclose(projector_m.T @ krein_pairing @ projector_m, 0.0, atol=TOL),
            "the pairing vanishes on each half separately",
        ),
        check(
            "cross_pair_is_full_rank",
            np.linalg.matrix_rank(
                projector_w.T @ krein_pairing @ projector_m,
                tol=TOL,
            )
            == 3,
            "the nondegenerate information lies in the cross-half pairing",
        ),
        check(
            "exchange_flips_half_grading",
            np.allclose(exchange @ half_grading @ exchange, -half_grading, atol=TOL),
            "the parent involution exchanges W and mirror labels",
        ),
        check(
            "exchange_preserves_2plus1_origin",
            np.allclose(exchange @ imposter_origin @ exchange, imposter_origin, atol=TOL),
            "the 2+1 origin axis is independent of the W/mirror exchange",
        ),
        check(
            "origin_and_half_gradings_commute",
            np.allclose(imposter_origin @ half_grading, half_grading @ imposter_origin, atol=TOL),
            "imposter/true origin and luminous/mirror are simultaneous but distinct labels",
        ),
        check(
            "each_half_contains_two_plus_one",
            int(round(np.trace(true_origin @ projector_w))) == 2
            and int(round(np.trace(imposter_origin @ projector_w))) == 1
            and int(round(np.trace(true_origin @ projector_m))) == 2
            and int(round(np.trace(imposter_origin @ projector_m))) == 1,
            "both halves contain two true slots and one imposter slot",
        ),
        check(
            "trace_pairing_does_not_choose_half",
            np.allclose(
                np.sort(np.linalg.eigvalsh(projector_w)),
                np.sort(np.linalg.eigvalsh(projector_m)),
                atol=TOL,
            ),
            "the paired geometry treats the two half projectors symmetrically",
        ),
        check(
            "low_curvature_has_two_stable_vacua",
            low_minima == (-1.0, 1.0)
            and potential(1.0, low_coefficient) < potential(0.0, low_coefficient),
            "the even double well selects a conjugate pair of nonzero stable vacua",
        ),
        check(
            "unbroken_low_curvature_point_is_unstable",
            potential_hessian(0.0, low_coefficient) < 0.0,
            "the symmetric point is not a low-curvature minimum",
        ),
        check(
            "high_curvature_restores_paired_phase",
            abs(potential_gradient(0.0, high_coefficient)) < TOL
            and potential_hessian(0.0, high_coefficient) > 0.0
            and all(
                potential(z, high_coefficient) > potential(0.0, high_coefficient)
                for z in (-1.0, 1.0)
            ),
            "the positive quadratic coefficient has one stable symmetric vacuum",
        ),
        check(
            "action_is_exchange_symmetric",
            all(
                abs(potential(z, low_coefficient) - potential(-z, low_coefficient)) < TOL
                for z in (-2.0, -1.0, 0.0, 1.0, 2.0)
            ),
            "the parent action remains non-chiral under z -> -z",
        ),
        check(
            "mass_response_is_covariant",
            np.allclose(exchange @ mass_plus @ exchange, mass_minus, atol=TOL),
            "exchanging halves and the vacuum preserves the full response law",
        ),
        check(
            "each_broken_vacuum_has_one_light_half",
            np.allclose(mass_plus @ luminous_plus, 1.0 * luminous_plus, atol=TOL)
            and np.allclose(mass_minus @ luminous_minus, 1.0 * luminous_minus, atol=TOL)
            and np.allclose(mass_plus @ projector_m, 3.0 * projector_m, atol=TOL)
            and np.allclose(mass_minus @ projector_w, 3.0 * projector_w, atol=TOL),
            "the selected vacuum makes one relational half light and its partner heavy",
        ),
        check(
            "luminous_projector_descends_as_matched_orbit",
            np.allclose(exchange @ luminous_plus @ exchange, luminous_minus, atol=TOL),
            "absolute half labels differ but the light-relative-to-vacuum relation is invariant",
        ),
        check(
            "high_curvature_response_is_half_degenerate",
            np.allclose(mass_high, base_mass_squared * identity6, atol=TOL),
            "at the restored point the two halves recouple and no luminous projector is selected",
        ),
        check(
            "2plus1_coupling_is_not_selected_by_labels",
            np.allclose(exchange @ equal_response @ exchange, -equal_response, atol=TOL)
            and np.allclose(exchange @ split_response @ exchange, -split_response, atol=TOL)
            and not np.allclose(equal_response, split_response, atol=TOL),
            "equal and imposter-distinct responses obey the same typed symmetries",
        ),
        check(
            "true_family_symmetry_survives_selected_half",
            np.allclose(within_sector_twist @ imposter_origin, imposter_origin @ within_sector_twist, atol=TOL)
            and np.allclose(within_sector_twist @ mass_plus, mass_plus @ within_sector_twist, atol=TOL),
            "the selected light sector retains a two-true-family continuation freedom",
        ),
        check(
            "selected_half_does_not_select_instrument",
            max(effect_differences) < TOL
            and projector_probability(projector_w, true1_w) > 1.0 - TOL
            and projector_probability(projector_w, true2_w) > 1.0 - TOL
            and conditional_overlap < TOL,
            "two QND instruments have the same luminous effect but orthogonal true-family continuations",
        ),
        check(
            "finite_conditional_control_only",
            krein_pairing.shape == (6, 6)
            and set(low_minima) == {-1.0, 1.0}
            and high_stationary == (0.0,),
            "the run is one exact finite conditional control, not a GU dynamics simulation",
        ),
    ]

    passed = sum(item["passed"] for item in checks)
    return {
        "run_id": RUN_ID,
        "claim_id": "HC-DU-209",
        "action_id": "GU-K77-LUMINOUS-POLARIZATION-BRIDGE-AUDIT",
        "return_class": "CONDITIONAL_RELATIONAL_LUMINOUS_ORBIT_WITH_UNSELECTED_2PLUS1_COUPLING_AND_RECORD",
        "evidence_grade": 4,
        "gu_transfer_grade": 1,
        "maximum_evidence_grade": 4,
        "typed_axes": {
            "trace_reversed_frobenius_carrier": "indefinite_K77_shadow",
            "W_mirror_half_grading": "null_halves_with_nondegenerate_cross_pair",
            "two_plus_one_origin": "true_1_true_2_imposter",
            "fundamental_chirality": "not_identified_with_either_axis",
            "luminous_status": "lighter_half_relative_to_broken_vacuum",
            "material_record": "later_instrument_and_archive_not_selected",
        },
        "finite_control": {
            "carrier_dimension": 6,
            "krein_inertia": [positive_inertia, negative_inertia, null_inertia],
            "low_curvature_minima": list(low_minima),
            "high_curvature_minimum": 0.0,
            "broken_vacuum_mass_squared": {
                "luminous": 1.0,
                "partner": 3.0,
            },
            "instrument_effect_differences": list(effect_differences),
            "hostile_conditional_overlap": float(conditional_overlap),
        },
        "gu_admission": {
            "current_k77_supplies": [
                "trace_reversed_indefinite_carrier",
                "W_mirror_exchange_and_cross_pairing",
                "source_native_2plus1_label_structure",
            ],
            "current_k77_does_not_supply": [
                "full_source_action_and_stationary_background",
                "action_owned_exchange_odd_order_parameter",
                "curvature_dependent_double_well_coefficient",
                "derived_imposter_sensitive_response_coupling",
                "selected_material_record_instrument",
                "observer_access_archive_consumer_or_public_finality",
            ],
        },
        "absorbers": [
            "Landau spontaneous symmetry breaking",
            "Krein and Witt decomposition",
            "equivariant bifurcation theory",
            "spectral projectors",
            "quantum instrument nonuniqueness",
        ],
        "checks": checks,
        "summary": {
            "passed": passed,
            "total": len(checks),
            "all_passed": passed == len(checks),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(canonical_json(result), end="")
    return 0 if result["summary"]["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
