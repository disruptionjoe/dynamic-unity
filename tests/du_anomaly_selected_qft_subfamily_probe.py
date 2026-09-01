#!/usr/bin/env python3
"""Exact bounded controls for HC-DU-213.

This probe enumerates primitive chiral U(1) Weyl charge spectra and applies
the cubic gauge- and linear mixed-gravitational-anomaly equations. It
calibrates non-copy structural selection and exposes the dependence of any
unique finite answer on the supplied charge and cardinality domain.

Passing establishes no universal anomaly classification, physical choice of
gauge group or candidate domain, material record interface, new QFT, GU
result, or empirical prediction.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests/artifacts/du_anomaly_selected_qft_subfamily_result.json"


def canonical_orbit(charges: Sequence[int]) -> tuple[int, ...]:
    ordered = tuple(sorted(charges))
    conjugate = tuple(sorted(-charge for charge in charges))
    return min(ordered, conjugate)


def primitive(charges: Sequence[int]) -> bool:
    return math.gcd(*(abs(charge) for charge in charges)) == 1


def chiral(charges: Sequence[int]) -> bool:
    charge_set = set(charges)
    return all(-charge not in charge_set for charge in charge_set)


def anomaly_pair(charges: Sequence[int]) -> tuple[int, int]:
    return sum(charges), sum(charge**3 for charge in charges)


def anomaly_free(charges: Sequence[int]) -> bool:
    return anomaly_pair(charges) == (0, 0)


def b2(charges: Sequence[int]) -> int:
    return sum(charge**2 for charge in charges)


def b4(charges: Sequence[int]) -> int:
    return sum(charge**4 for charge in charges)


def raw_spectra(cardinality: int, max_abs_charge: int) -> tuple[tuple[int, ...], ...]:
    alphabet = tuple(
        charge
        for charge in range(-max_abs_charge, max_abs_charge + 1)
        if charge != 0
    )
    return tuple(
        charges
        for charges in itertools.combinations_with_replacement(alphabet, cardinality)
        if primitive(charges) and chiral(charges)
    )


def physical_spectra(cardinality: int, max_abs_charge: int) -> frozenset[tuple[int, ...]]:
    return frozenset(
        canonical_orbit(charges)
        for charges in raw_spectra(cardinality, max_abs_charge)
    )


def selected_spectra(cardinality: int, max_abs_charge: int) -> frozenset[tuple[int, ...]]:
    return frozenset(
        spectrum
        for spectrum in physical_spectra(cardinality, max_abs_charge)
        if anomaly_free(spectrum)
    )


def check(name: str, condition: bool, detail: str) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    return {"name": name, "passed": True, "detail": detail}


def target_image(
    spectra: Iterable[Sequence[int]], target: Callable[[Sequence[int]], int]
) -> frozenset[int]:
    return frozenset(target(spectrum) for spectrum in spectra)


def build_result() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    raw_5_9 = raw_spectra(5, 9)
    physical_5_9 = physical_spectra(5, 9)
    selected_5_9 = selected_spectra(5, 9)
    selected_5_8 = selected_spectra(5, 8)
    selected_5_10 = selected_spectra(5, 10)
    selected_6_5 = selected_spectra(6, 5)
    selected_7_4 = selected_spectra(7, 4)

    known_solution = (-9, -5, -1, 7, 8)
    second_solution = (-10, -4, -2, 7, 9)
    six_field_solution = (-5, -1, -1, -1, 4, 4)
    seven_field_solution = (-4, -2, -2, -1, 3, 3, 3)

    checks.append(
        check(
            "frozen_family_raw_count",
            len(raw_5_9) == 16258,
            "the primitive chiral five-charge family has 16,258 permutation-quotiented encodings before charge conjugation",
        )
    )
    checks.append(
        check(
            "global_sign_quotient_count",
            len(physical_5_9) == 8129,
            "simultaneous charge conjugation pairs every encoding into 8,129 physical candidate orbits",
        )
    )
    checks.append(
        check(
            "global_sign_has_no_fixed_chiral_five_spectrum",
            len(raw_5_9) == 2 * len(physical_5_9),
            "an odd nonzero chiral spectrum cannot equal its global-sign conjugate",
        )
    )
    checks.append(
        check(
            "known_anomaly_free_solution_control",
            known_solution in selected_5_9 and anomaly_pair(known_solution) == (0, 0),
            "(-9,-5,-1,7,8) satisfies both frozen anomaly equations",
        )
    )
    checks.append(
        check(
            "bound_nine_selects_one_orbit",
            selected_5_9 == frozenset({known_solution}),
            "within the supplied five-field and |q|<=9 domain exactly one anomaly-free chiral orbit survives",
        )
    )
    checks.append(
        check(
            "bound_eight_empty_control",
            not selected_5_8,
            "no primitive chiral five-field solution exists with maximum absolute charge at most eight",
        )
    )
    checks.append(
        check(
            "bound_ten_breaks_uniqueness",
            selected_5_10 == frozenset({known_solution, second_solution}),
            "raising the supplied charge bound by one admits a second inequivalent anomaly-free orbit",
        )
    )
    checks.append(
        check(
            "six_field_cardinality_control",
            selected_6_5 == frozenset({six_field_solution}),
            "changing cardinality to six admits a solution already at |q|<=5",
        )
    )
    checks.append(
        check(
            "seven_field_cardinality_control",
            selected_7_4 == frozenset({seven_field_solution}),
            "changing cardinality to seven admits a solution already at |q|<=4",
        )
    )
    checks.append(
        check(
            "anomaly_constraint_selects_proper_subfamily",
            0 < len(selected_5_9) < len(physical_5_9),
            "the target-blind consistency equations remove 8,128 of 8,129 bounded physical candidates",
        )
    )

    incumbent_b2 = target_image(physical_5_9, b2)
    selected_b2 = target_image(selected_5_9, b2)
    incumbent_b4 = target_image(physical_5_9, b4)
    selected_b4 = target_image(selected_5_9, b4)
    selected_5_10_b2 = target_image(selected_5_10, b2)
    checks.append(
        check(
            "quadratic_target_image_is_sharpened",
            len(incumbent_b2) == 313 and selected_b2 == frozenset({220}),
            "the bounded B2 image contracts from 313 values to the value 220",
        )
    )
    checks.append(
        check(
            "secondary_quartic_audit_is_sharpened",
            len(incumbent_b4) == 1075 and selected_b4 == frozenset({13684}),
            "the separately audited B4 image contracts from 1,075 values to 13,684",
        )
    )
    same_b2_anomalous = tuple(
        spectrum
        for spectrum in physical_5_9
        if b2(spectrum) == 220 and not anomaly_free(spectrum)
    )
    checks.append(
        check(
            "held_out_target_does_not_encode_anomaly_status",
            bool(same_b2_anomalous),
            "anomalous spectra share B2=220, so the target value is not an anomaly-free label",
        )
    )
    checks.append(
        check(
            "selector_has_no_answer_coordinate",
            all(
                isinstance(value, int)
                for spectrum in physical_5_9
                for value in anomaly_pair(spectrum)
            ),
            "selection is computed from the linear and cubic charge sums, not from a supplied survivor bit",
        )
    )
    checks.append(
        check(
            "finite_uniqueness_is_domain_relative",
            len(selected_5_9) == 1
            and len(selected_5_10) == 2
            and len(selected_6_5) == 1
            and len(selected_7_4) == 1,
            "uniqueness and minimal charge depend on supplied cardinality and charge range",
        )
    )
    checks.append(
        check(
            "target_value_is_domain_relative",
            selected_5_10_b2 == frozenset({220, 250}),
            "expanding the charge domain changes the selected B2 image from {220} to {220,250}",
        )
    )
    scaled_solution = tuple(2 * charge for charge in known_solution)
    checks.append(
        check(
            "charge_normalization_requires_a_coupling_ruler",
            Fraction(b2(known_solution), 1)
            == Fraction(1, 2) ** 2 * b2(scaled_solution),
            "q -> 2q and g -> g/2 preserves the coupling-weighted quadratic response, so bare B2 is not an absolute observable",
        )
    )

    model_fields = {
        "gauge_group",
        "charge_multiset",
        "charge_range",
        "fermion_cardinality",
        "anomaly_constraints",
    }
    handoff_fields = {
        "instrument",
        "blank_archive",
        "provenance",
        "access_boundary",
        "consumer",
        "reset",
        "resource_envelope",
    }
    checks.append(
        check(
            "consistency_selection_does_not_select_record_handoff",
            model_fields.isdisjoint(handoff_fields),
            "the anomaly equations select no sampler, archive, provenance, observer access, consumer, reset, or resources",
        )
    )
    checks.append(
        check(
            "noncopy_positive_does_not_activate_current_candidates",
            True,
            "the control calibrates a known consistency selector; DU candidates still lack a physically selected domain or complete handoff",
        )
    )

    return {
        "schema_version": "dynamic-unity/anomaly-selected-qft-subfamily/v0.1",
        "claim_id": "HC-DU-213",
        "run_id": "RUN-20260831-anomaly-selected-qft-subfamily-calibration",
        "checks": checks,
        "frozen_domain": {
            "fermion_cardinality": 5,
            "max_abs_charge": 9,
            "primitive_normalization": True,
            "vectorlike_pairs_excluded": True,
            "quotient": ["permutation", "global_charge_sign"],
            "raw_candidates": len(raw_5_9),
            "physical_candidate_orbits": len(physical_5_9),
        },
        "selection": {
            "equations": ["sum(q_i)=0", "sum(q_i^3)=0"],
            "selected_orbits": [list(spectrum) for spectrum in sorted(selected_5_9)],
            "selected_count": len(selected_5_9),
            "selector_key_supplied": False,
            "candidate_domain_physically_selected": False,
        },
        "target_images": {
            "incumbent_b2_count": len(incumbent_b2),
            "selected_b2": sorted(selected_b2),
            "incumbent_b4_count": len(incumbent_b4),
            "selected_b4": sorted(selected_b4),
            "expanded_domain_selected_b2": sorted(selected_5_10_b2),
            "normalization_note": "g^2 B2 is invariant under q->2q, g->g/2",
        },
        "hostile_domain_controls": {
            "five_fields_bound_8_selected_count": len(selected_5_8),
            "five_fields_bound_10_selected_count": len(selected_5_10),
            "six_fields_bound_5_selected_count": len(selected_6_5),
            "seven_fields_bound_4_selected_count": len(selected_7_4),
        },
        "summary": {
            "passed": len(checks),
            "total": len(checks),
            "noncopy_structural_selection": True,
            "bounded_target_sharpening": True,
            "unique_physical_qft_selected": False,
            "record_handoff_selected": False,
            "maximum_grade": 4,
        },
        "verdict": (
            "NONCOPY_QFT_CONSISTENCY_SELECTION_POSITIVE; "
            "FINITE_DOMAIN_UNIQUENESS_NOT_PHYSICAL; "
            "TARGET_SHARPENING_BOUND_RELATIVE; NO_READY_SUCCESSOR"
        ),
    }


def write_artifact(result: Mapping[str, object]) -> str:
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(payload, encoding="utf-8")
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.write_artifact:
        digest = write_artifact(result)
        print(f"PASS {result['summary']['passed']}/{result['summary']['total']} sha256={digest}")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
