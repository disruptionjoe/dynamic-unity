"""SWING-DU-PHY-02 Track C: non-scalar selector and persistence comparison.

This comparison consumes the stored Track A and Track B artifacts but
independently recomputes the load-bearing conclusions:

* initial and terminal Bianconi modal shapes together with raw dissipation;
* identical-block replication asymptotics for both Bianconi completions;
* the exact O(3), rather than arbitrary-congruence, scope of modal spectra;
* the common-covariance residual-energy identity and GL(d) invariance;
* iid chi-square score asymptotics, including the participation/Shannon/Gini
  split and vanishing maximum record share; and
* every zero-normalizer boundary.

Euclidean Bianconi, affine Bianconi, and record score energy remain three
separate receipts.  The product record has no score, vote, winner, or claim
promotion.  Contract/check counts establish execution only.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    validate_candidate_contract,
    write_candidate_artifact,
)


SEED = 2026072403
PINNED_NUMPY_VERSION = "2.5.1"
TESTS_DIR = Path(__file__).resolve().parent
TRACK_A_PATH = (
    TESTS_DIR / "artifacts" / "du_bianconi_physical_influence_probe_result.json"
)
TRACK_B_PATH = (
    TESTS_DIR / "artifacts" / "du_record_fisher_influence_probe_result.json"
)
ARTIFACT_PATH = (
    TESTS_DIR
    / "artifacts"
    / "du_physical_influence_selector_comparison_result.json"
)
EULER_GAMMA = 0.5772156649015329


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_stored_candidate(
    artifact: Mapping[str, Any], path: Path
) -> dict[str, Any]:
    candidate = artifact.get("candidate_contract")
    stored_receipt = artifact.get("comparison_receipt")
    if not isinstance(candidate, Mapping):
        raise ValueError(f"{path}: missing candidate_contract")
    if not isinstance(stored_receipt, Mapping):
        raise ValueError(f"{path}: missing comparison_receipt")
    errors = validate_candidate_contract(candidate)
    recomputed = comparison_receipt(candidate)
    return {
        "path": str(path.relative_to(TESTS_DIR.parent)),
        "artifact_sha256": file_sha256(path),
        "candidate_id": candidate.get("candidate_id"),
        "contract_errors": errors,
        "contract_complete": not errors,
        "stored_receipt_matches_recomputed": dict(stored_receipt) == recomputed,
        "stored_receipt": dict(stored_receipt),
        "recomputed_receipt": recomputed,
        "scientific_endorsement": False,
    }


def normalize(
    contributions: Sequence[float], *, zero_threshold: float = 0.0
) -> np.ndarray | None:
    values = np.asarray(contributions, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("contributions must be a nonempty vector")
    if float(np.min(values)) < -1.0e-14:
        raise ValueError("contributions must be nonnegative")
    values = np.maximum(values, 0.0)
    total = float(np.sum(values))
    if total <= zero_threshold:
        return None
    return values / total


def shape_metrics(weights: Sequence[float]) -> dict[str, float]:
    p = np.asarray(weights, dtype=float)
    if p.ndim != 1 or p.size == 0 or float(np.min(p)) < -1.0e-14:
        raise ValueError("weights must be a nonnegative vector")
    total = float(np.sum(p))
    if total <= 0.0:
        raise ValueError("weights must have positive total")
    p = np.maximum(p, 0.0) / total
    n = p.size
    entropy = -float(np.sum(p[p > 0.0] * np.log(p[p > 0.0])))
    ordered = np.sort(p)
    ranks = np.arange(1, n + 1, dtype=float)
    gini = float(
        2.0 * np.dot(ranks, ordered) / n - (n + 1.0) / n
    )
    return {
        "dimension": int(n),
        "lambda_participation": float(np.sqrt(np.sum(p * p))),
        "lambda_shannon": float(math.exp(-0.5 * entropy)),
        "native_gini": max(0.0, gini),
        "max_share": float(np.max(p)),
        "entropy": entropy,
    }


def loglog_slope(xs: Sequence[float], ys: Sequence[float]) -> float:
    x = np.log(np.asarray(xs, dtype=float))
    y = np.log(np.asarray(ys, dtype=float))
    return float(np.polyfit(x, y, 1)[0])


def max_abs_difference(left: Sequence[float], right: Sequence[float]) -> float:
    return float(
        np.max(
            np.abs(
                np.asarray(left, dtype=float)
                - np.asarray(right, dtype=float)
            )
        )
    )


def recompute_snapshot(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    contributions = np.asarray(
        snapshot["squared_modal_contributions"], dtype=float
    )
    total = float(np.sum(contributions))
    weights = normalize(contributions)
    if weights is None:
        raise AssertionError("defined snapshot unexpectedly has zero total")
    # Track A stores the permutation-invariant modal profile in descending
    # order, whereas its squared contributions retain eigensolver order.
    sorted_weights = np.sort(weights)[::-1]
    metrics = shape_metrics(sorted_weights)
    stored_metrics = snapshot["metrics"]
    return {
        "label": snapshot["label"],
        "time": float(snapshot["time"]),
        "step": int(snapshot["step"]),
        "raw_total_dissipation_recomputed": total,
        "raw_total_dissipation_stored": float(snapshot["total_dissipation"]),
        "dissipation_absolute_error": abs(
            total - float(snapshot["total_dissipation"])
        ),
        "raw_weights_recomputed": sorted_weights.tolist(),
        "raw_weights_stored": list(snapshot["raw_normalized_weights"]),
        "weight_max_absolute_error": max_abs_difference(
            sorted_weights, snapshot["raw_normalized_weights"]
        ),
        "shape_recomputed": metrics,
        "shape_stored_native": {
            "lambda_participation": float(
                stored_metrics["lambda_participation"]
            ),
            "lambda_shannon": float(
                stored_metrics["lambda_shannon_kl"]
            ),
            "native_gini": float(stored_metrics["gini"]),
            "max_share": float(max(snapshot["raw_normalized_weights"])),
            "entropy": float(stored_metrics["entropy"]),
        },
        "shape_max_absolute_error": max(
            abs(
                metrics["lambda_participation"]
                - float(stored_metrics["lambda_participation"])
            ),
            abs(
                metrics["lambda_shannon"]
                - float(stored_metrics["lambda_shannon_kl"])
            ),
            abs(metrics["native_gini"] - float(stored_metrics["gini"])),
            abs(metrics["entropy"] - float(stored_metrics["entropy"])),
        ),
    }


def bianconi_receipt(
    artifact: Mapping[str, Any], completion: str
) -> dict[str, Any]:
    results = artifact["results"]
    trajectory = results["stationary_behavior"]["approach_trajectories"][
        completion
    ]
    initial = recompute_snapshot(trajectory["samples"][0])
    terminal = recompute_snapshot(trajectory["samples"][-1])
    exact = results["stationary_behavior"]["exact_stationary_profiles"][
        completion
    ]
    exact_total = float(sum(exact["squared_modal_contributions"]))
    threshold = float(exact["numerical_zero_threshold"])
    exact_recomputed = normalize(
        exact["squared_modal_contributions"], zero_threshold=threshold
    )
    initial_d = initial["raw_total_dissipation_recomputed"]
    terminal_d = terminal["raw_total_dissipation_recomputed"]
    return {
        "comparison_id": (
            "SWING-DU-PHY-02-TC-AE"
            if completion == "euclidean"
            else "SWING-DU-PHY-02-TC-AAI"
        ),
        "source_candidate_id": artifact["candidate_contract"]["candidate_id"],
        "completion": completion,
        "decomposition_identity": (
            "D_E=sum_i eig_i(grad S)^2=-dS/dt"
            if completion == "euclidean"
            else (
                "D_AI=sum_i eig_i(G^(1/2)(grad S)G^(1/2))^2"
                "=-dS/dt"
            )
        ),
        "invariance_group": (
            "simultaneous orthogonal similarity O(3); "
            "arbitrary congruence and nonlinear coordinates not claimed"
        ),
        "initial": initial,
        "terminal": terminal,
        "terminal_over_initial_raw_dissipation": terminal_d / initial_d,
        "terminal_max_share": terminal["shape_recomputed"]["max_share"],
        "exact_zero_domain": {
            "stored_defined": bool(exact["defined"]),
            "stored_weights": exact["raw_normalized_weights"],
            "raw_total_dissipation_recomputed": exact_total,
            "numerical_zero_threshold": threshold,
            "recomputed_weights": (
                None if exact_recomputed is None else exact_recomputed.tolist()
            ),
            "classification": "UNDEFINED",
        },
        "persistence_relation": "NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY",
        "growth_scale_relation": "SCALE_UNASSESSED",
        "selector": "NONE",
    }


def block_replication_diagnostic(
    receipt: Mapping[str, Any]
) -> dict[str, Any]:
    base_p = np.asarray(receipt["initial"]["raw_weights_recomputed"])
    base_d = float(
        receipt["initial"]["raw_total_dissipation_recomputed"]
    )
    block_counts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    rows: list[dict[str, Any]] = []
    for count in block_counts:
        weights = np.tile(base_p, count) / count
        metrics = shape_metrics(weights)
        rows.append(
            {
                "block_count": count,
                "modal_count": int(weights.size),
                "raw_total_dissipation": count * base_d,
                **metrics,
            }
        )
    slopes = {
        "raw_total_dissipation": loglog_slope(
            block_counts,
            [row["raw_total_dissipation"] for row in rows],
        ),
        "lambda_participation": loglog_slope(
            block_counts,
            [row["lambda_participation"] for row in rows],
        ),
        "lambda_shannon": loglog_slope(
            block_counts,
            [row["lambda_shannon"] for row in rows],
        ),
        "native_gini": loglog_slope(
            block_counts, [row["native_gini"] for row in rows]
        ),
        "max_share": loglog_slope(
            block_counts, [row["max_share"] for row in rows]
        ),
    }
    return {
        "construction": (
            "K identical block-diagonal copies; each modal weight is q_j/K "
            "and raw D_K=K D_1. This is a diagnostic, not a native growth law."
        ),
        "rows": rows,
        "slopes": slopes,
        "native_gini_spread": max(row["native_gini"] for row in rows)
        - min(row["native_gini"] for row in rows),
        "expected_signature": {
            "raw_total_dissipation": 1.0,
            "lambda_participation": -0.5,
            "lambda_shannon": -0.5,
            "native_gini": 0.0,
            "max_share": -1.0,
        },
        "scale_reading": {
            "participation": "FINITE_SAMPLE_AMPLITUDE",
            "shannon": "FINITE_SAMPLE_AMPLITUDE",
            "gini": "PERSISTENT_SHAPE_ONLY",
            "native_growth_law": "SCALE_UNASSESSED",
        },
    }


def orthogonal_scope_diagnostic(
    receipt: Mapping[str, Any], rng: np.random.Generator
) -> dict[str, Any]:
    snapshot = receipt["initial"]
    completion = receipt["completion"]
    eigenvalues = np.asarray(
        snapshot["raw_weights_recomputed"], dtype=float
    )
    # Reconstruct one symmetric modal operator whose squared eigenvalues have
    # the stored profile. Signs are taken from the source eigenvalue ordering.
    signs = (
        np.array([-1.0, 1.0, 1.0])
        if completion == "euclidean"
        else np.array([-1.0, 1.0, 1.0])
    )
    operator = np.diag(signs * np.sqrt(eigenvalues))
    baseline = np.sort(
        normalize(np.linalg.eigvalsh(operator) ** 2)
    )
    errors: list[float] = []
    for index in range(6):
        q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        if index == 0:
            q[:, 0] *= -1.0
        transformed = q @ operator @ q.T
        profile = np.sort(
            normalize(np.linalg.eigvalsh(transformed) ** 2)
        )
        errors.append(max_abs_difference(baseline, profile))

    congruence = np.array(
        [[1.7, 0.3, 0.0], [0.0, 0.8, 0.2], [0.1, 0.0, 1.2]]
    )
    congruent = congruence @ operator @ congruence.T
    congruent_profile = np.sort(
        normalize(np.linalg.eigvalsh(congruent) ** 2)
    )
    return {
        "valid_group": "O(3) simultaneous orthogonal similarity",
        "orthogonal_trials": len(errors),
        "maximum_orthogonal_profile_error": max(errors),
        "nonorthogonal_congruence_profile_change": max_abs_difference(
            baseline, congruent_profile
        ),
        "not_claimed": [
            "arbitrary GL(3) congruence",
            "nonlinear reparameterization",
            "canonical labels through eigenvalue degeneracy",
        ],
    }


def score_energy_profile(
    records: np.ndarray, theta: np.ndarray, covariance: np.ndarray
) -> dict[str, Any]:
    n = records.shape[0]
    inverse_covariance = np.linalg.inv(covariance)
    residuals = records - theta
    scores = residuals @ inverse_covariance
    total_fisher = n * inverse_covariance
    inverse_total_fisher = np.linalg.inv(total_fisher)
    leverages = np.einsum(
        "ni,ij,nj->n", scores, inverse_total_fisher, scores
    )
    q = np.einsum(
        "ni,ij,nj->n", residuals, inverse_covariance, residuals
    )
    loss = 0.5 * float(np.mean(q))
    weights = normalize(leverages, zero_threshold=1.0e-15)
    return {
        "leverages": leverages,
        "weights": weights,
        "sum_leverages": float(np.sum(leverages)),
        "twice_mean_loss": 2.0 * loss,
        "residual_energy_identity_error": abs(
            float(np.sum(leverages)) - 2.0 * loss
        ),
        "q_over_n_error": max_abs_difference(leverages, q / n),
    }


def record_invariance_and_zero_diagnostic(
    rng: np.random.Generator,
) -> dict[str, Any]:
    d = 4
    theta = np.array([0.35, -0.2, 0.5, 0.1])
    basis = np.array(
        [
            [1.2, 0.2, -0.1, 0.0],
            [0.1, 0.9, 0.3, -0.2],
            [0.0, -0.1, 1.1, 0.25],
            [0.2, 0.0, 0.15, 0.8],
        ]
    )
    covariance = basis @ basis.T + 0.35 * np.eye(d)
    records = theta + rng.normal(size=(37, d)) @ basis.T
    baseline = score_energy_profile(records, theta, covariance)

    transform = np.array(
        [
            [1.7, 0.2, -0.3, 0.1],
            [0.1, 0.8, 0.4, -0.2],
            [0.0, -0.2, 1.3, 0.3],
            [0.2, 0.1, -0.1, 0.7],
        ]
    )
    transformed = score_energy_profile(
        records @ transform.T,
        transform @ theta,
        transform @ covariance @ transform.T,
    )
    zero = score_energy_profile(
        np.tile(theta, (8, 1)), theta, covariance
    )
    return {
        "valid_group": (
            "GL(4) joint linear reparameterization of records, theta, and "
            "common covariance; record permutations are equivariant"
        ),
        "common_covariance_identity": "sum_i ell_i=2L_N",
        "residual_energy_identity_error": baseline[
            "residual_energy_identity_error"
        ],
        "ell_equals_q_over_n_error": baseline["q_over_n_error"],
        "gl_leverage_max_error": max_abs_difference(
            baseline["leverages"], transformed["leverages"]
        ),
        "gl_weight_max_error": max_abs_difference(
            baseline["weights"], transformed["weights"]
        ),
        "zero_domain": {
            "normalizer": zero["sum_leverages"],
            "weights": (
                None if zero["weights"] is None else zero["weights"].tolist()
            ),
            "classification": "UNDEFINED",
        },
        "not_claimed": [
            "nonlinear finite-coordinate transformations",
            "correlated-record additivity",
            "iid I_N=N Sigma^-1 for heteroskedastic records",
        ],
    }


def iid_record_asymptotics(
    rng: np.random.Generator,
) -> dict[str, Any]:
    dimension = 4
    trials = 192
    record_counts = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
    rows: list[dict[str, Any]] = []
    for n in record_counts:
        q = rng.chisquare(dimension, size=(trials, n))
        totals = np.sum(q, axis=1)
        weights = q / totals[:, None]
        lambda_participation = np.sqrt(
            np.sum(weights * weights, axis=1)
        )
        entropy = -np.sum(
            np.where(weights > 0.0, weights * np.log(weights), 0.0),
            axis=1,
        )
        lambda_shannon = np.exp(-0.5 * entropy)
        ordered = np.sort(weights, axis=1)
        ranks = np.arange(1, n + 1, dtype=float)
        gini = (
            2.0 * np.sum(ordered * ranks, axis=1) / n
            - (n + 1.0) / n
        )
        max_share = np.max(weights, axis=1)
        # ell_i=q_i/N, hence sum ell_i is the sample mean q.
        raw_carrier = totals / n
        rows.append(
            {
                "record_count": n,
                "mean_lambda_participation": float(
                    np.mean(lambda_participation)
                ),
                "mean_lambda_shannon": float(
                    np.mean(lambda_shannon)
                ),
                "mean_native_gini": float(np.mean(gini)),
                "mean_max_share": float(np.mean(max_share)),
                "mean_raw_score_energy": float(np.mean(raw_carrier)),
            }
        )

    slopes = {
        "lambda_participation": loglog_slope(
            record_counts,
            [row["mean_lambda_participation"] for row in rows],
        ),
        "lambda_shannon": loglog_slope(
            record_counts,
            [row["mean_lambda_shannon"] for row in rows],
        ),
        "native_gini": loglog_slope(
            record_counts, [row["mean_native_gini"] for row in rows]
        ),
        "max_share": loglog_slope(
            record_counts, [row["mean_max_share"] for row in rows]
        ),
        "raw_score_energy": loglog_slope(
            record_counts,
            [row["mean_raw_score_energy"] for row in rows],
        ),
    }

    tail = rows[-4:]
    measured_constants = {
        "participation_prefactor": float(
            np.mean(
                [
                    row["mean_lambda_participation"]
                    * math.sqrt(row["record_count"])
                    for row in tail
                ]
            )
        ),
        "shannon_prefactor": float(
            np.mean(
                [
                    row["mean_lambda_shannon"]
                    * math.sqrt(row["record_count"])
                    for row in tail
                ]
            )
        ),
        "gini_limit": float(
            np.mean([row["mean_native_gini"] for row in tail])
        ),
        "raw_score_energy_limit": float(
            np.mean([row["mean_raw_score_energy"] for row in tail])
        ),
    }
    k = dimension / 2.0
    psi_k_plus_one = 1.5 - EULER_GAMMA  # psi(3), because k=d/2=2.
    theory = {
        "participation_prefactor": math.sqrt(
            (dimension + 2.0) / dimension
        ),
        "shannon_prefactor": math.exp(
            0.5 * (psi_k_plus_one - math.log(k))
        ),
        "gini_limit": 3.0 / 8.0,
        "raw_score_energy_limit": float(dimension),
        "max_share_asymptotic": "O(log N / N), hence zero",
    }
    return {
        "seed_stream": "main seed after invariance diagnostics",
        "data_model": (
            "iid Gaussian at true theta; q_i~chi-square_4, "
            "ell_i=q_i/N, p_i=q_i/sum q"
        ),
        "dimension": dimension,
        "trials_per_record_count": trials,
        "rows": rows,
        "slopes": slopes,
        "measured_tail_constants": measured_constants,
        "theory": theory,
        "relative_constant_errors": {
            key: abs(measured_constants[key] - theory[key]) / theory[key]
            for key in (
                "participation_prefactor",
                "shannon_prefactor",
                "gini_limit",
                "raw_score_energy_limit",
            )
        },
        "native_relations": {
            "participation": "FINITE_SAMPLE_AMPLITUDE",
            "shannon": "FINITE_SAMPLE_AMPLITUDE",
            "gini": "PERSISTENT_SHAPE_ONLY",
            "max_individual_share": "VANISHES",
            "raw_score_energy": "SCALE_UNASSESSED",
        },
        "scale_note": (
            "The dimensionless raw score-energy tends to d, but no unit-bearing "
            "or cosmological map is supplied. Native Gini is inequality only; "
            "the endpoint-mapped Gini Lambda is excluded."
        ),
    }


def make_check(name: str, passed: bool) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed)}


def main() -> None:
    track_a = load_json(TRACK_A_PATH)
    track_b = load_json(TRACK_B_PATH)
    validation_a = validate_stored_candidate(track_a, TRACK_A_PATH)
    validation_b = validate_stored_candidate(track_b, TRACK_B_PATH)

    euclidean = bianconi_receipt(track_a, "euclidean")
    affine = bianconi_receipt(track_a, "affine_invariant")
    replication_e = block_replication_diagnostic(euclidean)
    replication_a = block_replication_diagnostic(affine)

    rng = np.random.default_rng(SEED)
    scope_e = orthogonal_scope_diagnostic(euclidean, rng)
    scope_a = orthogonal_scope_diagnostic(affine, rng)
    record_scope = record_invariance_and_zero_diagnostic(rng)
    record_asymptotics = iid_record_asymptotics(rng)

    old_incomparable_pair = {
        "left_counts": [37, 1, 1, 1],
        "right_counts": [36, 4, 0, 0],
        "embedding_into_each_physical_state_space": None,
        "matched_raw_carrier_and_controls": None,
        "independent_response_functional": None,
        "ordering_status": "NOT_EVALUABLE",
        "contract_answer": "NOT_IDENTIFIED",
        "reason": (
            "The physical candidates output profiles. No map embeds both old "
            "profiles into all three candidate state spaces at matched raw "
            "carrier, and no held-out physical response orders those states."
        ),
    }

    comparison_receipts = {
        "bianconi_euclidean": {
            **euclidean,
            "block_replication": replication_e,
            "invariance_scope_recomputed": scope_e,
        },
        "bianconi_affine": {
            **affine,
            "block_replication": replication_a,
            "invariance_scope_recomputed": scope_a,
        },
        "record_score_fisher": {
            "comparison_id": "SWING-DU-PHY-02-TC-BF",
            "source_candidate_id": track_b["candidate_contract"][
                "candidate_id"
            ],
            "decomposition_identity": "sum_i ell_i=2L_N for common Sigma",
            "invariance_scope_recomputed": record_scope,
            "large_N_recomputed": record_asymptotics,
            "persistence_relation": {
                "participation": "FINITE_SAMPLE_AMPLITUDE",
                "shannon": "FINITE_SAMPLE_AMPLITUDE",
                "gini": "PERSISTENT_SHAPE_ONLY",
                "max_individual_share": "VANISHES",
            },
            "absolute_scale_relation": "SCALE_UNASSESSED",
            "selector": "NONE",
        },
    }

    product_record = {
        "record_type": "NON_SCALAR_PRODUCT_RECORD",
        "scalar_score": None,
        "vote": None,
        "winner": None,
        "candidate_order": [
            "bianconi_euclidean",
            "bianconi_affine",
            "record_score_fisher",
        ],
        "candidate_receipts": comparison_receipts,
        "old_incomparable_pair": old_incomparable_pair,
        "selector_relation": "SELECTOR_OPEN",
        "selector_evidence": {
            "participation": None,
            "shannon_kl": None,
            "gini_lorenz": None,
            "independent_conservation_additivity_or_prediction_law": None,
        },
        "scale_relations": {
            "bianconi_euclidean_relaxation": (
                "NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY"
            ),
            "bianconi_affine_relaxation": (
                "NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY"
            ),
            "bianconi_growth": "SCALE_UNASSESSED",
            "record_participation": "FINITE_SAMPLE_AMPLITUDE",
            "record_shannon": "FINITE_SAMPLE_AMPLITUDE",
            "record_gini": "PERSISTENT_SHAPE_ONLY",
            "record_absolute": "SCALE_UNASSESSED",
        },
        "disagreement_attribution": {
            "bianconi_euclidean_vs_affine": "COMPLETION",
            "bianconi_vs_record": [
                "INDEX_SET",
                "DATA_MODEL",
                "METRIC",
                "EVOLUTION_VARIABLE",
                "GROWTH_MAP_ABSENT_FOR_BIANCONI",
            ],
            "participation_shannon_vs_gini": "FUNCTIONAL_ROLE",
            "concept_invariant_failure": False,
        },
        "claim_promotion": False,
        "prediction_seed": False,
        "bank_review": False,
        "scientific_endorsement_from_check_count": False,
        "verdict": "OBJECT-FOUND / SELECTOR-OPEN",
        "verdict_scope": (
            "Three live normalized objects survive their declared algebra and "
            "coordinate groups. No independent functional selector or "
            "unit-bearing nonzero physical scale survives the comparison."
        ),
    }

    block_slope_tolerance = 2.0e-12
    block_checks = []
    for label, diagnostic in (
        ("Euclidean", replication_e),
        ("affine", replication_a),
    ):
        slopes = diagnostic["slopes"]
        block_checks.append(
            make_check(
                f"{label} block replication independently gives "
                "D~K, participation/Shannon~K^-1/2, native Gini~K^0, "
                "and max share~K^-1",
                (
                    abs(slopes["raw_total_dissipation"] - 1.0)
                    < block_slope_tolerance
                    and abs(slopes["lambda_participation"] + 0.5)
                    < block_slope_tolerance
                    and abs(slopes["lambda_shannon"] + 0.5)
                    < block_slope_tolerance
                    and abs(slopes["native_gini"])
                    < block_slope_tolerance
                    and abs(slopes["max_share"] + 1.0)
                    < block_slope_tolerance
                    and diagnostic["native_gini_spread"] < 1.0e-12
                ),
            )
        )

    asymptotic_slopes = record_asymptotics["slopes"]
    asymptotic_errors = record_asymptotics["relative_constant_errors"]
    asymptotic_rows = record_asymptotics["rows"]
    relation_values = set(product_record["scale_relations"].values())

    checks = [
        make_check(
            "runtime uses pinned NumPy 2.5.1",
            np.__version__ == PINNED_NUMPY_VERSION,
        ),
        make_check(
            "stored Track A candidate contract and receipt validate exactly",
            validation_a["contract_complete"]
            and validation_a["stored_receipt_matches_recomputed"],
        ),
        make_check(
            "stored Track B candidate contract and receipt validate exactly",
            validation_b["contract_complete"]
            and validation_b["stored_receipt_matches_recomputed"],
        ),
        make_check(
            "Euclidean initial and terminal modal contributions independently reconstruct raw D and native shape",
            euclidean["initial"]["dissipation_absolute_error"] < 1.0e-12
            and euclidean["initial"]["weight_max_absolute_error"] < 1.0e-12
            and euclidean["initial"]["shape_max_absolute_error"] < 1.0e-12
            and euclidean["terminal"]["dissipation_absolute_error"] < 1.0e-12
            and euclidean["terminal"]["weight_max_absolute_error"] < 1.0e-12
            and euclidean["terminal"]["shape_max_absolute_error"] < 1.0e-12,
        ),
        make_check(
            "affine initial and terminal modal contributions independently reconstruct raw D and native shape",
            affine["initial"]["dissipation_absolute_error"] < 1.0e-12
            and affine["initial"]["weight_max_absolute_error"] < 1.0e-12
            and affine["initial"]["shape_max_absolute_error"] < 1.0e-12
            and affine["terminal"]["dissipation_absolute_error"] < 1.0e-12
            and affine["terminal"]["weight_max_absolute_error"] < 1.0e-12
            and affine["terminal"]["shape_max_absolute_error"] < 1.0e-12,
        ),
        make_check(
            "Euclidean normalized terminal residue approaches a point shape while raw D vanishes and exact D=0 stays undefined",
            euclidean["terminal_over_initial_raw_dissipation"] < 1.0e-12
            and euclidean["terminal_max_share"] > 0.999
            and euclidean["exact_zero_domain"]["recomputed_weights"] is None
            and not euclidean["exact_zero_domain"]["stored_defined"],
        ),
        make_check(
            "affine normalized terminal residue approaches a point shape while raw D vanishes and exact D=0 stays undefined",
            affine["terminal_over_initial_raw_dissipation"] < 1.0e-12
            and affine["terminal_max_share"] > 0.999
            and affine["exact_zero_domain"]["recomputed_weights"] is None
            and not affine["exact_zero_domain"]["stored_defined"],
        ),
        *block_checks,
        make_check(
            "both Bianconi receipts are invariant under O(3) similarity while nonorthogonal congruence is outside scope",
            scope_e["maximum_orthogonal_profile_error"] < 1.0e-12
            and scope_a["maximum_orthogonal_profile_error"] < 1.0e-12
            and scope_e["nonorthogonal_congruence_profile_change"] > 1.0e-3
            and scope_a["nonorthogonal_congruence_profile_change"] > 1.0e-3,
        ),
        make_check(
            "record score energy independently satisfies ell=q/N and sum ell=2L_N",
            record_scope["residual_energy_identity_error"] < 1.0e-12
            and record_scope["ell_equals_q_over_n_error"] < 1.0e-12,
        ),
        make_check(
            "record score energy is invariant under the declared joint GL(4) reparameterization",
            record_scope["gl_leverage_max_error"] < 1.0e-12
            and record_scope["gl_weight_max_error"] < 1.0e-12,
        ),
        make_check(
            "record zero-score normalizer remains undefined",
            record_scope["zero_domain"]["normalizer"] < 1.0e-15
            and record_scope["zero_domain"]["weights"] is None,
        ),
        make_check(
            "iid record participation amplitude recomputes slope -1/2 and the chi-square_4 prefactor",
            abs(asymptotic_slopes["lambda_participation"] + 0.5) < 0.02
            and asymptotic_errors["participation_prefactor"] < 0.02,
        ),
        make_check(
            "iid record Shannon amplitude recomputes slope -1/2 and its chi-square_4 prefactor",
            abs(asymptotic_slopes["lambda_shannon"] + 0.5) < 0.02
            and asymptotic_errors["shannon_prefactor"] < 0.02,
        ),
        make_check(
            "iid record native Gini recomputes a nonzero 3/8 shape limit rather than a physical amplitude",
            abs(asymptotic_slopes["native_gini"]) < 0.03
            and asymptotic_errors["gini_limit"] < 0.03
            and product_record["scale_relations"]["record_gini"]
            == "PERSISTENT_SHAPE_ONLY",
        ),
        make_check(
            "largest iid record share vanishes with growth",
            asymptotic_slopes["max_share"] < -0.70
            and asymptotic_rows[-1]["mean_max_share"] < 0.002
            and asymptotic_rows[-1]["mean_max_share"]
            < asymptotic_rows[0]["mean_max_share"] / 30.0,
        ),
        make_check(
            "dimensionless raw score energy tends to d but remains scale-unassessed without a unit-bearing map",
            asymptotic_errors["raw_score_energy_limit"] < 0.02
            and abs(asymptotic_slopes["raw_score_energy"]) < 0.02
            and product_record["scale_relations"]["record_absolute"]
            == "SCALE_UNASSESSED",
        ),
        make_check(
            "Euclidean, affine, and record-score objects remain three separate comparison receipts",
            list(comparison_receipts) == [
                "bianconi_euclidean",
                "bianconi_affine",
                "record_score_fisher",
            ]
            and len(
                {
                    receipt["comparison_id"]
                    for receipt in comparison_receipts.values()
                }
            )
            == 3,
        ),
        make_check(
            "old incomparable-pair ordering is NOT_EVALUABLE without embedding, matched controls, and an independent response",
            old_incomparable_pair["ordering_status"] == "NOT_EVALUABLE"
            and old_incomparable_pair[
                "embedding_into_each_physical_state_space"
            ]
            is None
            and old_incomparable_pair[
                "matched_raw_carrier_and_controls"
            ]
            is None
            and old_incomparable_pair[
                "independent_response_functional"
            ]
            is None,
        ),
        make_check(
            "no independent law selects participation, Shannon/KL, or Gini/Lorenz",
            product_record["selector_relation"] == "SELECTOR_OPEN"
            and all(
                value is None
                for value in product_record["selector_evidence"].values()
            ),
        ),
        make_check(
            "scale product preserves residue-at-zero, finite-sample, persistent-shape, and unassessed distinctions",
            {
                "NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY",
                "FINITE_SAMPLE_AMPLITUDE",
                "PERSISTENT_SHAPE_ONLY",
                "SCALE_UNASSESSED",
            }.issubset(relation_values),
        ),
        make_check(
            "product comparison has no scalar score, vote, winner, bank, seed, or claim promotion",
            product_record["scalar_score"] is None
            and product_record["vote"] is None
            and product_record["winner"] is None
            and not product_record["bank_review"]
            and not product_record["prediction_seed"]
            and not product_record["claim_promotion"],
        ),
        make_check(
            "no shared failure is attributed to the concept invariant",
            not product_record["disagreement_attribution"][
                "concept_invariant_failure"
            ],
        ),
    ]

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "SWING-DU-PHY-02-TC",
        "track": "Physical influence selector and persistence comparison",
        "question": (
            "Do the Bianconi Euclidean, Bianconi affine, or record-score "
            "influence objects independently select a concentration functional "
            "or sustain a non-fitted nonzero physical scale?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "The two upstream artifacts are immutable inputs whose "
                    "candidate contracts and receipts must validate."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Binds the comparison to the executed Track A/B objects.",
            },
            {
                "id": "A2",
                "statement": (
                    "Euclidean and affine Bianconi mobilities remain separate "
                    "unselected physical-time completions."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Prevents averaging completion disagreement.",
            },
            {
                "id": "A3",
                "statement": (
                    "Identical block replication is a diagnostic only, not a "
                    "native Bianconi cell-growth law."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Exposes shape asymptotics without inventing physical growth.",
            },
            {
                "id": "A4",
                "statement": (
                    "The record asymptotic uses iid Gaussian records at true "
                    "theta with q_i distributed chi-square_4."
                ),
                "status": "IMPORTED",
                "role": "Makes all large-N constants and their data-model scope explicit.",
            },
            {
                "id": "A5",
                "statement": (
                    "A normalized profile is degree zero and cannot supply "
                    "units or common magnitude without a separate raw map."
                ),
                "status": "STANDARD",
                "role": "Separates relative shape from physical scale.",
            },
            {
                "id": "A6",
                "statement": (
                    "No embedding and independent physical response exist for "
                    "the old incomparable profile pair."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Forces the ordering answer to remain NOT_EVALUABLE.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Replicate each initial Bianconi block over "
                    "K=1,2,...,1024 powers of two."
                ),
                "why_not_forced": "The fixed-block action has no native K growth.",
                "sensitivity_test": (
                    "Require the exact analytic slope tuple "
                    "(+1,-1/2,-1/2,0,-1)."
                ),
            },
            {
                "id": "C2",
                "choice": (
                    "Use 192 iid chi-square_4 trials for N=64 through 8192."
                ),
                "why_not_forced": "The grid and Monte Carlo resolution are computational choices.",
                "sensitivity_test": (
                    "Compare slopes and tail constants with exact Gamma-law predictions."
                ),
            },
            {
                "id": "C3",
                "choice": f"Use deterministic random seed {SEED}.",
                "why_not_forced": "Any fixed seed samples the same declared null model.",
                "sensitivity_test": (
                    "Analytic constants, broad tolerances, and monotone max-share decay "
                    "prevent a seed-specific verdict."
                ),
            },
            {
                "id": "C4",
                "choice": (
                    "Report native Gini rather than the prior endpoint-mapped Gini Lambda."
                ),
                "why_not_forced": (
                    "Gini has no canonical amplitude map; endpoint matching inserts one."
                ),
                "sensitivity_test": (
                    "Track native Gini beside max share and both effective-count amplitudes."
                ),
            },
        ],
        "equations": [
            "p_i=a_i/sum_j a_j on sum_j a_j>0",
            "Bianconi: D_X=sum_i a_i^X=-dS/dt",
            "K-block replication: p_kj=q_j/K and D_K=K D_1",
            "lambda_2=sqrt(sum_i p_i^2)",
            "lambda_H=exp[-H(p)/2]",
            "record: ell_i=q_i/N and sum_i ell_i=2L_N",
            "chi-square_d: sqrt(N)lambda_2 -> sqrt((d+2)/d)",
            (
                "chi-square_d: sqrt(N)lambda_H -> "
                "exp((psi(d/2+1)-log(d/2))/2)"
            ),
            (
                "chi-square_4 native Gini -> "
                "Gamma(5/2)/(sqrt(pi)Gamma(3))=3/8"
            ),
        ],
        "observables": [
            "three distinct candidate receipts and their exact invariance groups",
            "initial/terminal Bianconi shape with raw dissipation",
            "Bianconi block-replication exponents and native Gini limit",
            "record residual-energy decomposition and GL(4) errors",
            "record participation/Shannon slopes and analytic prefactors",
            "record native Gini, maximum share, and raw score-energy limits",
            "zero-normalizer behavior for all three candidates",
            "non-scalar selector and scale-relation product",
        ],
        "comparators": [
            "Euclidean versus affine Bianconi completion at shared state",
            "normalized Bianconi terminal shape versus vanishing raw D",
            "participation versus Shannon versus native Gini under growth",
            "record normalized shape versus dimensionless raw score energy",
            "declared coordinate groups versus transformations outside scope",
        ],
        "null_models": [
            "exact Bianconi stationarity: D=0 and normalized profile undefined",
            "zero record scores: sum ell_i=0 and normalized profile undefined",
            "identical block replication: Gini shape persists while every modal share vanishes",
            "iid chi-square_4 records: effective-count amplitudes vanish while Gini tends 3/8",
        ],
        "falsifiers": [
            "an upstream candidate contract or stored receipt fails recomputation",
            "modal contributions fail to reconstruct stored raw D or native shape",
            "block replication misses its exact analytic exponent tuple",
            "joint declared coordinate transformations change the relevant profile",
            "a zero normalizer is filled with a preferred distribution",
            "iid score amplitudes or constants miss chi-square_4 theory",
            "an individual iid record retains nonzero share as N grows",
            "a functional is called selected without an independent response law",
        ],
        "stop_conditions": [
            "Do not average the Euclidean and affine completions.",
            "Do not use a check count, vote, or scalar score as scientific evidence.",
            "Do not replace NOT_EVALUABLE ordering with the old proxy rankings.",
            "Do not call native Gini persistence a nonzero physical amplitude.",
            "Do not bank, seed, promote, or externally publish this comparison.",
            "Any failure localizes to a formalization unless traced to the concept invariant.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A live DU mechanism generates a normalized influence "
                "distribution whose nonuniformity may alter the uniform "
                "baseline without choosing a target."
            ),
            "formalization_id": "PHYSICAL-INFLUENCE-SELECTOR-PRODUCT",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "All three receipts contain live normalized objects on their "
                "nonzero domains, but Bianconi relative shape survives only as "
                "raw dissipation vanishes, and iid record participation/Shannon "
                "amplitudes vanish while Gini retains shape inequality. No "
                "independent functional selector or non-fitted unit-bearing "
                "physical scale is identified."
            ),
            "grade": (
                "OBJECT-FOUND / SELECTOR-OPEN / "
                "NO-NONZERO-PHYSICAL-SCALE-IDENTIFIED"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Bianconi has no native growth law or selected completion; "
                "record-score behavior is data-model and metric conditional; "
                "no held-out response functional, cosmological observable, "
                "units map, rho, or Lambda is supplied."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": "du_physical_influence_selector_comparison",
        "seed": SEED,
        "numpy_version": np.__version__,
        "pinned_numpy_version": PINNED_NUMPY_VERSION,
        "source_validation": {
            "track_a": validation_a,
            "track_b": validation_b,
        },
        "product_record": product_record,
        "scientific_reading": (
            "Object construction succeeds at conditional grade. The selector "
            "and physical-scale questions remain open; normalized persistence "
            "is not absolute persistence."
        ),
    }
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    for check in checks:
        status = "PASS" if check["pass"] else "FAIL"
        print(f"{status}: {check['name']}")
    passed = sum(check["pass"] for check in checks)
    print(f"\nExecution checks: {passed}/{len(checks)}")
    print(
        "Scientific verdict: OBJECT-FOUND / SELECTOR-OPEN / "
        "NO-NONZERO-PHYSICAL-SCALE-IDENTIFIED"
    )
    print(
        "Check counts establish execution only; they are not scientific evidence."
    )
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
