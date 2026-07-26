#!/usr/bin/env python3
"""Inverse tournament for the conditional three-chiral-generation target.

This probe works backward from a frozen low-energy endpoint. It distinguishes:

* constraints on the content of one Standard Model family;
* constraints on the number of repeated families;
* accessible chirality from global index and hidden completion;
* the lower bound supplied by CKM-like CP violation from an exact count; and
* a fitted endpoint from a source-derived operator with a held-out result.

It does not construct the GU source action, a physical Dirac operator, an
anomaly-inflow completion, or a theory of flavor.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np


RUN_ID = "RUN-20260725-235834-inverse-chirality-generation"
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_inverse_chirality_generation_tournament_result.json"
)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def one_family_anomaly_vector() -> dict[str, Fraction | int]:
    """Return exact anomaly coefficients for left-handed SM Weyl fields.

    Common positive Dynkin-index normalizations are suppressed for the mixed
    nonabelian anomalies; only their exact vanishing is used.
    """

    fields = [
        {
            "field": "Q_L",
            "multiplicity": 6,
            "hypercharge": Fraction(1, 6),
            "su3_cubic": 2,
            "su3_quadratic_copies": 2,
            "su2_quadratic_copies": 3,
            "su2_doublets": 3,
        },
        {
            "field": "u_R_conjugate",
            "multiplicity": 3,
            "hypercharge": Fraction(-2, 3),
            "su3_cubic": -1,
            "su3_quadratic_copies": 1,
            "su2_quadratic_copies": 0,
            "su2_doublets": 0,
        },
        {
            "field": "d_R_conjugate",
            "multiplicity": 3,
            "hypercharge": Fraction(1, 3),
            "su3_cubic": -1,
            "su3_quadratic_copies": 1,
            "su2_quadratic_copies": 0,
            "su2_doublets": 0,
        },
        {
            "field": "L_L",
            "multiplicity": 2,
            "hypercharge": Fraction(-1, 2),
            "su3_cubic": 0,
            "su3_quadratic_copies": 0,
            "su2_quadratic_copies": 1,
            "su2_doublets": 1,
        },
        {
            "field": "e_R_conjugate",
            "multiplicity": 1,
            "hypercharge": Fraction(1, 1),
            "su3_cubic": 0,
            "su3_quadratic_copies": 0,
            "su2_quadratic_copies": 0,
            "su2_doublets": 0,
        },
    ]

    su3_cubic = sum(Fraction(field["su3_cubic"]) for field in fields)
    su3_squared_u1 = sum(
        Fraction(field["su3_quadratic_copies"]) * field["hypercharge"]
        for field in fields
    )
    su2_squared_u1 = sum(
        Fraction(field["su2_quadratic_copies"]) * field["hypercharge"]
        for field in fields
    )
    u1_cubic = sum(
        Fraction(field["multiplicity"]) * field["hypercharge"] ** 3
        for field in fields
    )
    gravitational_u1 = sum(
        Fraction(field["multiplicity"]) * field["hypercharge"]
        for field in fields
    )
    su2_doublets = sum(int(field["su2_doublets"]) for field in fields)

    return {
        "SU3_cubed": su3_cubic,
        "SU3_squared_U1": su3_squared_u1,
        "SU2_squared_U1": su2_squared_u1,
        "U1_cubed": u1_cubic,
        "gravity_squared_U1": gravitational_u1,
        "SU2_doublet_count": su2_doublets,
        "SU2_global_anomaly_parity": su2_doublets % 2,
    }


def anomaly_tournament() -> dict[str, Any]:
    one_family = one_family_anomaly_vector()
    local_keys = [
        "SU3_cubed",
        "SU3_squared_U1",
        "SU2_squared_U1",
        "U1_cubed",
        "gravity_squared_U1",
    ]
    sweep = []
    for family_count in range(1, 7):
        local_vector = {
            key: family_count * Fraction(one_family[key]) for key in local_keys
        }
        doublets = family_count * int(one_family["SU2_doublet_count"])
        sweep.append(
            {
                "family_count": family_count,
                "local_anomaly_vector": {
                    key: fraction_text(value)
                    for key, value in local_vector.items()
                },
                "SU2_doublet_count": doublets,
                "SU2_global_anomaly_parity": doublets % 2,
                "all_tested_anomalies_cancel": bool(
                    all(value == 0 for value in local_vector.values())
                    and doublets % 2 == 0
                ),
            }
        )

    return {
        "normalization_note": (
            "Common Dynkin-index factors are suppressed for mixed anomalies; "
            "only exact zero/nonzero status is used."
        ),
        "one_family_exact_vector": {
            key: fraction_text(Fraction(value))
            for key, value in one_family.items()
        },
        "family_count_sweep": sweep,
        "counts_passing_all_tested_anomaly_constraints": [
            row["family_count"]
            for row in sweep
            if row["all_tested_anomalies_cancel"]
        ],
        "consequence": (
            "Because one complete Standard Model family is anomaly-free and "
            "the anomaly functional is additive, repeating it N times leaves "
            "these constraints zero for every tested N. They constrain family "
            "content but do not select N=3."
        ),
    }


def completion_tournament() -> dict[str, Any]:
    accessible_left = 3
    accessible_right = 0

    arbitrary_index_completions = []
    for global_index in range(-5, 6):
        global_right = max(0, accessible_left - global_index)
        global_left = global_right + global_index
        arbitrary_index_completions.append(
            {
                "global_index": global_index,
                "global_left_zero_modes": global_left,
                "global_right_zero_modes": global_right,
                "accessible_left_zero_modes": accessible_left,
                "accessible_right_zero_modes": accessible_right,
                "hidden_left_zero_modes": global_left - accessible_left,
                "hidden_right_zero_modes": global_right,
                "same_accessible_endpoint": bool(
                    global_left >= accessible_left
                    and accessible_left == 3
                    and accessible_right == 0
                ),
            }
        )

    index_three_hidden_pairs = []
    for hidden_pair_count in range(0, 6):
        global_left = 3 + hidden_pair_count
        global_right = hidden_pair_count
        index_three_hidden_pairs.append(
            {
                "hidden_mirror_pair_count": hidden_pair_count,
                "global_left_zero_modes": global_left,
                "global_right_zero_modes": global_right,
                "global_index": global_left - global_right,
                "accessible_endpoint": [3, 0],
            }
        )

    vectorlike_access = []
    for global_pair_count in range(3, 9):
        vectorlike_access.append(
            {
                "global_left_zero_modes": global_pair_count,
                "global_right_zero_modes": global_pair_count,
                "global_index": 0,
                "accessible_endpoint": [3, 0],
                "hidden_zero_modes": 2 * global_pair_count - 3,
            }
        )

    return {
        "declared_accessible_endpoint_left_right": [
            accessible_left,
            accessible_right,
        ],
        "arbitrary_global_index_completion_sweep": arbitrary_index_completions,
        "index_three_hidden_pair_sweep": index_three_hidden_pairs,
        "vectorlike_access_three_sweep": vectorlike_access,
        "consequence": (
            "Within the broad finite hidden-mode completion class, the same "
            "accessible three-left/zero-right endpoint is compatible with "
            "many total mode counts and every tested global index. Even a "
            "known global index of three does not determine hidden mirror-pair "
            "content."
        ),
        "scope_limit": (
            "This is a completion-class nonidentification result. It does not "
            "assert that every combinatorial completion is a local, unitary, "
            "gauge-consistent physical theory."
        ),
    }


def mixing_parameter_counts(generations: int) -> dict[str, int]:
    return {
        "generations": generations,
        "mixing_angles": generations * (generations - 1) // 2,
        "irreducible_dirac_CP_phases": (
            (generations - 1) * (generations - 2) // 2
        ),
    }


def ckm_matrix(
    theta12: float, theta23: float, theta13: float, delta: float
) -> np.ndarray:
    s12, c12 = np.sin(theta12), np.cos(theta12)
    s23, c23 = np.sin(theta23), np.cos(theta23)
    s13, c13 = np.sin(theta13), np.cos(theta13)
    phase = np.exp(1.0j * delta)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 / phase],
            [
                -s12 * c23 - c12 * s23 * s13 * phase,
                c12 * c23 - s12 * s23 * s13 * phase,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * phase,
                -c12 * s23 - s12 * c23 * s13 * phase,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


def cp_tournament() -> dict[str, Any]:
    parameter_sweep = [mixing_parameter_counts(n) for n in range(1, 7)]
    cp_capable_counts = [
        row["generations"]
        for row in parameter_sweep
        if row["irreducible_dirac_CP_phases"] > 0
    ]

    ckm = ckm_matrix(0.227, 0.041, 0.0036, 1.20)
    unitarity_residual = float(
        np.linalg.norm(ckm.conj().T @ ckm - np.eye(3))
    )
    jarlskog = float(
        np.imag(
            ckm[0, 0]
            * ckm[1, 1]
            * np.conjugate(ckm[0, 1])
            * np.conjugate(ckm[1, 0])
        )
    )

    up_squared = np.diag([1.0, 16.0, 625.0]).astype(complex)
    down_squared = (
        ckm @ np.diag([4.0, 81.0, 2401.0]) @ ckm.conj().T
    )
    commutator = up_squared @ down_squared - down_squared @ up_squared
    commutator_determinant = np.linalg.det(commutator)

    cycle = np.array(
        [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],
        dtype=complex,
    )
    cyclic_up = (
        5.0 * np.eye(3)
        + (1.0 + 2.0j) * cycle
        + (1.0 - 2.0j) * cycle.conj().T
    )
    cyclic_down = (
        3.0 * np.eye(3)
        + (-0.5 + 1.25j) * cycle
        + (-0.5 - 1.25j) * cycle.conj().T
    )
    cyclic_commutator = cyclic_up @ cyclic_down - cyclic_down @ cyclic_up

    return {
        "standard_unitary_mixing_parameter_sweep": parameter_sweep,
        "generation_counts_with_at_least_one_dirac_CP_phase": cp_capable_counts,
        "three_generation_positive_control": {
            "unitarity_residual": unitarity_residual,
            "jarlskog_invariant": jarlskog,
            "mass_squared_commutator_norm": float(
                np.linalg.norm(commutator)
            ),
            "mass_squared_commutator_determinant": {
                "real": float(np.real(commutator_determinant)),
                "imaginary": float(np.imag(commutator_determinant)),
                "absolute": float(abs(commutator_determinant)),
            },
        },
        "common_cyclic_algebra_null": {
            "commutator_norm": float(np.linalg.norm(cyclic_commutator)),
            "commutator_determinant_absolute": float(
                abs(np.linalg.det(cyclic_commutator))
            ),
        },
        "consequence": (
            "Under ordinary unitary CKM-like assumptions, an irreducible "
            "Dirac CP phase requires at least three generations. Counts above "
            "three also admit such phases, so CP supplies a lower bound rather "
            "than an exact count. A nonzero Jarlskog/commutator witness also "
            "rejects any flavor construction confined to one common "
            "commutative cyclic algebra."
        ),
    }


def candidate_preimages() -> list[dict[str, Any]]:
    return [
        {
            "candidate": "DIRECT_GLOBAL_INDEX_THREE",
            "accessible_endpoint": [3, 0],
            "global_index": 3,
            "where_three_enters": "physical index pairing, if independently derived",
            "source_status": "UNDEFINED",
            "completion_discriminator": "topological response and anomaly/inflow receipt",
            "full_conditional_packet_satisfied": False,
        },
        {
            "candidate": "UNIT_INDEX_TIMES_TRIPLET",
            "accessible_endpoint": [3, 0],
            "global_index": 3,
            "where_three_enters": "independently located carrier triplet",
            "source_status": "UNDEFINED",
            "completion_discriminator": "operator factorization and triplet provenance",
            "full_conditional_packet_satisfied": False,
        },
        {
            "candidate": "VECTORLIKE_COMPLETION_ACCESS_THREE",
            "accessible_endpoint": [3, 0],
            "global_index": 0,
            "where_three_enters": "declared energy/region/access map",
            "source_status": "UNDEFINED",
            "completion_discriminator": "boundary expansion, partner search, and threshold running",
            "full_conditional_packet_satisfied": False,
        },
        {
            "candidate": "INDEX_THREE_WITH_HIDDEN_MIRROR_PAIRS",
            "accessible_endpoint": [3, 0],
            "global_index": 3,
            "where_three_enters": "net imbalance; total mode count remains open",
            "source_status": "UNDEFINED",
            "completion_discriminator": "complete mirror census and mass-generation contract",
            "full_conditional_packet_satisfied": False,
        },
        {
            "candidate": "TARGET_CODED_DEFECT_OR_RECTANGULARITY",
            "accessible_endpoint": [3, 0],
            "global_index": 3,
            "where_three_enters": "flux, defect charge, rank, or rectangularity chosen as three",
            "source_status": "TARGET_IMPORTED",
            "completion_discriminator": "independent derivation of the count-setting datum",
            "full_conditional_packet_satisfied": False,
        },
        {
            "candidate": "THREE_COPIES_WITHOUT_COUNT_MECHANISM",
            "accessible_endpoint": [3, 0],
            "global_index": "UNDEFINED",
            "where_three_enters": "matter inventory",
            "source_status": "CARRIER_ONLY",
            "completion_discriminator": "source-owned count-changing counterfactual",
            "full_conditional_packet_satisfied": False,
        },
    ]


def count_sensitive_channel_registry() -> list[dict[str, str]]:
    return [
        {
            "channel": "ordinary_SM_local_anomaly_cancellation",
            "count_status": "BLIND_AFTER_ONE_FAMILY_CANCELS",
            "next_requirement": "none; use it to constrain family content",
        },
        {
            "channel": "ordinary_SM_SU2_global_anomaly",
            "count_status": "BLIND_BECAUSE_EACH_FAMILY_HAS_FOUR_DOUBLETS",
            "next_requirement": "a nonfactorizing family-sensitive global structure",
        },
        {
            "channel": "CKM_like_CP_existence",
            "count_status": "LOWER_BOUND_N_AT_LEAST_3",
            "next_requirement": "an independent exclusion of N greater than 3",
        },
        {
            "channel": "source_derived_index_or_K_theory_pairing",
            "count_status": "POTENTIALLY_EXACT",
            "next_requirement": "actual operator/domain and target-independent index origin",
        },
        {
            "channel": "horizontal_or_discrete_family_anomaly",
            "count_status": "POTENTIALLY_COUNT_SENSITIVE",
            "next_requirement": "independently derived family symmetry and full anomaly audit",
        },
        {
            "channel": "boundary_or_energy_access_expansion",
            "count_status": "COMPLETION_SENSITIVE_NOT_EXACT_COUNT_BY_ITSELF",
            "next_requirement": "matched partner, threshold, and resource observations",
        },
        {
            "channel": "restricted_flavor_algebra_with_held_out_relation",
            "count_status": "POTENTIALLY_SELECTIVE",
            "next_requirement": "source-derived noncommuting operators and unused prediction",
        },
        {
            "channel": "topological_deformation_response",
            "count_status": "PROTECTION_SENSITIVE",
            "next_requirement": "physical gap/locality and permitted deformation class",
        },
    ]


def evaluate() -> dict[str, Any]:
    anomalies = anomaly_tournament()
    completions = completion_tournament()
    cp_data = cp_tournament()
    candidates = candidate_preimages()
    channels = count_sensitive_channel_registry()

    one_family = anomalies["one_family_exact_vector"]
    arbitrary_completions = completions[
        "arbitrary_global_index_completion_sweep"
    ]
    cp_counts = cp_data[
        "generation_counts_with_at_least_one_dirac_CP_phase"
    ]
    positive_cp = cp_data["three_generation_positive_control"]
    cyclic_null = cp_data["common_cyclic_algebra_null"]

    checks = {
        "one_family_SU3_cubed_anomaly_cancels": (
            one_family["SU3_cubed"] == "0"
        ),
        "one_family_SU3_squared_U1_anomaly_cancels": (
            one_family["SU3_squared_U1"] == "0"
        ),
        "one_family_SU2_squared_U1_anomaly_cancels": (
            one_family["SU2_squared_U1"] == "0"
        ),
        "one_family_U1_cubed_anomaly_cancels": (
            one_family["U1_cubed"] == "0"
        ),
        "one_family_gravitational_U1_anomaly_cancels": (
            one_family["gravity_squared_U1"] == "0"
        ),
        "one_family_has_even_SU2_doublet_count": (
            one_family["SU2_global_anomaly_parity"] == "0"
            and one_family["SU2_doublet_count"] == "4"
        ),
        "all_family_counts_one_through_six_pass_tested_anomalies": all(
            row["all_tested_anomalies_cancel"]
            for row in anomalies["family_count_sweep"]
        ),
        "anomalies_do_not_select_three": (
            anomalies["counts_passing_all_tested_anomaly_constraints"]
            == [1, 2, 3, 4, 5, 6]
        ),
        "same_accessible_endpoint_spans_all_tested_global_indices": (
            [row["global_index"] for row in arbitrary_completions]
            == list(range(-5, 6))
            and all(
                row["same_accessible_endpoint"]
                for row in arbitrary_completions
            )
        ),
        "endpoint_does_not_identify_even_global_index_sign": (
            any(row["global_index"] < 0 for row in arbitrary_completions)
            and any(row["global_index"] == 0 for row in arbitrary_completions)
            and any(row["global_index"] > 0 for row in arbitrary_completions)
        ),
        "global_index_three_does_not_identify_hidden_pair_count": (
            len(
                {
                    row["hidden_mirror_pair_count"]
                    for row in completions["index_three_hidden_pair_sweep"]
                }
            )
            == 6
            and all(
                row["global_index"] == 3
                for row in completions["index_three_hidden_pair_sweep"]
            )
        ),
        "vectorlike_global_zero_can_expose_access_three": all(
            row["global_index"] == 0
            and row["accessible_endpoint"] == [3, 0]
            for row in completions["vectorlike_access_three_sweep"]
        ),
        "two_generations_have_no_irreducible_dirac_CP_phase": (
            mixing_parameter_counts(2)["irreducible_dirac_CP_phases"] == 0
        ),
        "three_generations_have_one_irreducible_dirac_CP_phase": (
            mixing_parameter_counts(3)["irreducible_dirac_CP_phases"] == 1
        ),
        "four_generations_also_admit_CP_phases": (
            mixing_parameter_counts(4)["irreducible_dirac_CP_phases"] == 3
        ),
        "CP_phase_existence_sets_minimum_three": (
            cp_counts[0] == 3
        ),
        "CP_phase_existence_does_not_select_exactly_three": (
            cp_counts == [3, 4, 5, 6]
        ),
        "three_generation_CKM_control_is_unitary": (
            positive_cp["unitarity_residual"] < 1e-12
        ),
        "three_generation_Jarlskog_control_is_nonzero": (
            abs(positive_cp["jarlskog_invariant"]) > 1e-7
        ),
        "three_generation_mass_commutator_CP_witness_is_nonzero": (
            positive_cp["mass_squared_commutator_determinant"]["absolute"]
            > 1.0
        ),
        "common_cyclic_flavor_algebra_commutes": (
            cyclic_null["commutator_norm"] < 1e-12
        ),
        "common_cyclic_flavor_algebra_has_zero_CP_commutator_determinant": (
            cyclic_null["commutator_determinant_absolute"] < 1e-24
        ),
        "all_rival_preimages_match_the_accessible_endpoint": all(
            row["accessible_endpoint"] == [3, 0] for row in candidates
        ),
        "rival_preimages_disagree_on_global_index_or_provenance": (
            len({str(row["global_index"]) for row in candidates}) >= 3
            and len({row["source_status"] for row in candidates}) >= 3
        ),
        "no_candidate_has_the_full_source_operator_packet": not any(
            row["full_conditional_packet_satisfied"] for row in candidates
        ),
        "target_coded_candidate_is_flagged": any(
            row["source_status"] == "TARGET_IMPORTED" for row in candidates
        ),
        "registry_contains_count_sensitive_successor_channels": any(
            row["count_status"] == "POTENTIALLY_EXACT" for row in channels
        )
        and any(
            row["count_status"] == "POTENTIALLY_COUNT_SENSITIVE"
            for row in channels
        ),
    }

    passed = sum(bool(value) for value in checks.values())
    total = len(checks)
    verdict = (
        "CONDITIONAL_TARGET_CONSTRAINS__ANOMALIES_COUNT_BLIND__"
        "CP_LOWER_BOUND_NOT_EXACT_COUNT__UV_CAUSE_NONIDENTIFIED__"
        "PHYSICAL_SOURCE_OPERATOR_OPEN"
        if passed == total
        else "PROBE_FAILURE"
    )

    return {
        "run_id": RUN_ID,
        "frozen_conditional_target": (
            "Three observed matter generations are the protected chiral "
            "low-energy kernel of one source-derived physical operator, with "
            "consistent anomaly/mirror completion and restricted "
            "source-derived flavor breaking yielding nondegenerate masses, "
            "nontrivial mixing, and nonzero rephasing-invariant CP."
        ),
        "scope": (
            "Conditional inverse inference with exact anomaly arithmetic, "
            "finite hidden-mode completions, and standard unitary mixing "
            "controls; no GU source operator or generation derivation."
        ),
        "anomaly_tournament": anomalies,
        "completion_tournament": completions,
        "CP_and_flavor_tournament": cp_data,
        "candidate_preimage_tournament": candidates,
        "count_sensitive_channel_registry": channels,
        "return_contract": {
            "ordinary_SM_anomalies": "ANOMALY_REPLICATION_BLIND_TO_COUNT",
            "accessible_chirality": (
                "CHIRAL_ENDPOINT_UNDERIDENTIFIES_GLOBAL_COMPLETION"
            ),
            "ordinary_CKM_CP": (
                "CP_REQUIRES_AT_LEAST_THREE_NOT_EXACTLY_THREE"
            ),
            "common_cyclic_flavor": "NONCOMMUTING_FLAVOR_REQUIRED",
            "physical_GU_source_operator": "PHYSICAL_SOURCE_OPERATOR_OPEN",
            "integrated": (
                "CONDITIONAL_TARGET_CONSTRAINS__"
                "EXACT_THREE_REMAINS_SOURCE_SENSITIVE__"
                "UV_CAUSE_NONIDENTIFIED"
            ),
        },
        "checks": checks,
        "summary": {"passed": passed, "total": total, "verdict": verdict},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ARTIFACT_PATH)
    args = parser.parse_args()

    result = evaluate()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")

    summary = result["summary"]
    print(
        f"{summary['passed']}/{summary['total']} checks passed — "
        f"{summary['verdict']}"
    )
    print(args.output)
    return 0 if summary["passed"] == summary["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
