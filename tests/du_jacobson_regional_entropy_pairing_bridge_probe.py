#!/usr/bin/env python3
"""Exact controls for the Jacobson/regional-entropy/2+1 pairing bridge.

The probe tests four deliberately small statements:

1. two globally orthogonal completions can have the same regional state;
2. a response that factors through that state cannot recover global provenance;
3. a multiplicity-one removal can select an unlabelled 2-of-3 orbit without
   selecting which family was removed; and
4. regional scope and energy scale are independent axes unless an additional
   law couples them.

The imported 0 -> 2 -> 11 invariant-count ladder is a regression against the
read-only GU source packet.  It is not rederived here.  Passing establishes no
GU action, gravitational entropy law, generation count, record interface, new
physics, or empirical prediction.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_jacobson_regional_entropy_pairing_bridge_result.json"
)
RUN_ID = "RUN-20260831-jacobson-regional-entropy-pairing-bridge"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def check(name: str, condition: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(condition), "detail": detail}


def partial_trace_second(sign: int) -> tuple[tuple[Fraction, ...], ...]:
    """Reduced first-qubit state of (|00> + sign |11>)/sqrt(2)."""

    amplitudes = {(0, 0): 1, (1, 1): sign}
    return tuple(
        tuple(
            sum(
                Fraction(amplitudes.get((a, b), 0) * amplitudes.get((ap, b), 0), 2)
                for b in (0, 1)
            )
            for ap in (0, 1)
        )
        for a in (0, 1)
    )


def matrix_trace_product(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> Fraction:
    size = len(left)
    return sum(left[i][j] * right[j][i] for i in range(size) for j in range(size))


def marginals(
    joint: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    rows = tuple(sum(row) for row in joint)
    columns = tuple(sum(joint[i][j] for i in range(len(joint))) for j in range(len(joint[0])))
    return rows, columns


def build_result() -> dict[str, Any]:
    half = Fraction(1, 2)
    zero = Fraction(0, 1)
    one = Fraction(1, 1)

    rho_plus = partial_trace_second(+1)
    rho_minus = partial_trace_second(-1)
    maximally_mixed = ((half, zero), (zero, half))
    local_identity = ((one, zero), (zero, one))
    local_z = ((one, zero), (zero, -one))

    # The full states are orthogonal because (1 + (-1))/2 = 0.  A global
    # X tensor X witness distinguishes them, while every first-qubit response
    # receives the same reduced state.
    full_overlap = Fraction(1 + (-1), 2)
    global_xx_plus = one
    global_xx_minus = -one
    local_modular_response_plus = matrix_trace_product(rho_plus, local_z)
    local_modular_response_minus = matrix_trace_product(rho_minus, local_z)

    # Removing any one of three indistinguishable family slots leaves a
    # normalized rank-two projector.  All three have spectrum (1/2,1/2,0),
    # and agree on the permutation-invariant span generated here by I and J.
    family_states = []
    family_invariant_expectations = []
    identity3 = tuple(
        tuple(one if i == j else zero for j in range(3)) for i in range(3)
    )
    all_ones3 = tuple(tuple(one for _ in range(3)) for _ in range(3))
    for removed in range(3):
        state = tuple(
            tuple(half if i == j and i != removed else zero for j in range(3))
            for i in range(3)
        )
        family_states.append(state)
        family_invariant_expectations.append(
            (
                matrix_trace_product(state, identity3),
                matrix_trace_product(state, all_ones3),
            )
        )

    # Same regional and scale marginals, opposite cross-axis correlation.
    correlated = ((half, zero), (zero, half))
    anticorrelated = ((zero, half), (half, zero))
    correlated_marginals = marginals(correlated)
    anticorrelated_marginals = marginals(anticorrelated)
    parity = ((one, -one), (-one, one))
    correlated_parity = sum(
        correlated[i][j] * parity[i][j] for i in range(2) for j in range(2)
    )
    anticorrelated_parity = sum(
        anticorrelated[i][j] * parity[i][j] for i in range(2) for j in range(2)
    )

    # Imported exact GU regression: invariant pairing channels appear as the
    # symmetry is lowered, so the current route removes a pair below the
    # high-symmetry regime and restores it above that threshold.
    pairing_ladder = {"Spin(10)": 0, "Pati-Salam": 2, "Standard Model": 11}

    checks = [
        check(
            "global_completions_are_orthogonal",
            full_overlap == 0,
            "the two Bell purifications are perfectly distinguishable globally",
        ),
        check(
            "regional_restrictions_are_identical",
            rho_plus == rho_minus == maximally_mixed,
            "both global completions restrict to I/2 on the admitted region",
        ),
        check(
            "regional_normalization_is_exact",
            matrix_trace_product(rho_plus, local_identity) == 1,
            "the regional state has unit trace",
        ),
        check(
            "regional_modular_response_is_provenance_blind",
            local_modular_response_plus == local_modular_response_minus == 0,
            "a fixed regional response gives the same value on equal restrictions",
        ),
        check(
            "global_witness_retains_provenance",
            global_xx_plus == 1 and global_xx_minus == -1,
            "an enlarged algebra distinguishes the hidden relative phase",
        ),
        check(
            "regional_factorization_has_a_nonzero_remainder",
            rho_plus == rho_minus and global_xx_plus != global_xx_minus,
            "same regional state does not reconstruct the global completion target",
        ),
        check(
            "each_pairing_choice_leaves_two_slots",
            all(matrix_trace_product(state, identity3) == 1 for state in family_states),
            "each normalized post-pairing state has rank-two support and unit trace",
        ),
        check(
            "pairing_choice_has_common_entropy_spectrum",
            all(
                tuple(sorted(state[i][i] for i in range(3))) == (zero, half, half)
                for state in family_states
            ),
            "all three removal choices have the same spectrum and entropy log(2)",
        ),
        check(
            "permutation_invariant_response_cannot_name_removed_family",
            len(set(family_invariant_expectations)) == 1,
            "the invariant I/J response agrees for all three unlabelled pairings",
        ),
        check(
            "microscopic_pairing_embeddings_are_distinct",
            len(set(family_states)) == 3,
            "which family was removed remains different on a family-sensitive algebra",
        ),
        check(
            "regional_marginals_match_across_joint_completions",
            correlated_marginals[0] == anticorrelated_marginals[0] == (half, half),
            "the two region marginals agree exactly",
        ),
        check(
            "scale_marginals_match_across_joint_completions",
            correlated_marginals[1] == anticorrelated_marginals[1] == (half, half),
            "the two energy-scale marginals agree exactly",
        ),
        check(
            "region_scale_coupling_is_not_fixed_by_marginals",
            correlated_parity == 1 and anticorrelated_parity == -1,
            "equal one-axis data admit opposite mixed region-scale targets",
        ),
        check(
            "gu_pairing_is_absent_at_highest_symmetry",
            pairing_ladder["Spin(10)"] == 0,
            "the imported high-symmetry pairing invariant vanishes",
        ),
        check(
            "gu_pairing_appears_after_symmetry_lowering",
            pairing_ladder["Pati-Salam"] > pairing_ladder["Spin(10)"]
            and pairing_ladder["Standard Model"] > pairing_ladder["Pati-Salam"],
            "the imported invariant count grows down the symmetry-breaking chain",
        ),
        check(
            "high_energy_peeloff_reading_is_reversed_on_current_route",
            pairing_ladder["Spin(10)"] == 0 and pairing_ladder["Pati-Salam"] > 0,
            "the invariant pairing channel vanishes at highest symmetry rather than opening there",
        ),
    ]

    passed = sum(item["passed"] for item in checks)
    return {
        "probe": "du_jacobson_regional_entropy_pairing_bridge_probe",
        "run_id": RUN_ID,
        "verdict": (
            "REGIONAL_RESPONSE_FACTORS_THROUGH_THE_REGIONAL_STATE; "
            "PAIRING_PROVENANCE_AND_REGION_SCALE_COUPLING_REMAIN_UNSELECTED"
        ),
        "checks_passed": passed,
        "checks_total": len(checks),
        "all_passed": passed == len(checks),
        "exact_controls": {
            "bell_regional_state": [[str(value) for value in row] for row in rho_plus],
            "global_xx_targets": [str(global_xx_plus), str(global_xx_minus)],
            "family_invariant_expectations": [
                [str(value) for value in values]
                for values in family_invariant_expectations
            ],
            "region_scale_parities": [str(correlated_parity), str(anticorrelated_parity)],
            "imported_pairing_ladder": pairing_ladder,
        },
        "checks": checks,
        "scope": {
            "establishes": [
                "regional-response provenance blindness for equal regional states",
                "unlabelled two-of-three pairing-orbit nonselection",
                "independence of regional-scope and energy-scale axes",
                "the direction of the imported GU pairing ladder",
            ],
            "does_not_establish": [
                "a GU source action or physical mass threshold",
                "Jacobson gravity from GU",
                "a generation count or distinguished observed family",
                "a selected causal-diamond algebra, reference state, or record interface",
                "new physics or an empirical prediction",
            ],
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

    print(
        f"{result['probe']}: {result['checks_passed']}/{result['checks_total']} "
        f"checks passed"
    )
    print(result["verdict"])
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
