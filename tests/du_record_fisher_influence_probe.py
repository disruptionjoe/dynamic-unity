"""Track B of SWING-DU-PHY-02: record-score/Fisher-metric influence.

The live object is the vector finality-consistency empirical loss

    L_N(theta) = (1/2N) sum_i (theta-r_i)^T Sigma^-1 (theta-r_i).

For a common known covariance Sigma, the per-record score, total Fisher metric,
and observed score leverage are

    s_i   = Sigma^-1 (r_i-theta),
    I_N   = N Sigma^-1,
    ell_i = s_i^T I_N^-1 s_i
          = (1/N) (r_i-theta)^T Sigma^-1 (r_i-theta).

Where sum_i ell_i > 0, p_i = ell_i/sum_j ell_j is a nonnegative normalized
record-native influence distribution.  It exactly decomposes twice the named
loss: sum_i ell_i = 2 L_N.

Expected Fisher contribution and observed score leverage are deliberately kept
separate.  For iid identical records, I_i=Sigma^-1 and
tr(I_N^-1 I_i)=d/N for every record; exchangeability also gives E[p_i]=1/N.
An observed batch nevertheless has unequal ell_i because realized score norms
are unequal.

The probe tests the declared GL(d) coordinate group by transforming theta,
records, and Sigma together.  It also covers equal-radius and zero-score nulls,
iid data, a correctly specified heteroskedastic extension, an outlier control,
per-record-Fisher-natural loss flow, record accretion, and large-N scaling.  No
rho, Lambda, target concentration, or fitted amplitude appears in the weights.

Pinned NumPy + stdlib.  Deterministic.  Uses the shared conditional-candidate
harness and writes a JSON artifact.  Contract completeness is not a scientific
endorsement.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    validate_candidate_contract,
    write_candidate_artifact,
)


SEED = 20260724
PINNED_NUMPY = "2.5.1"
TOL = 2.0e-11
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_fisher_influence_probe_result.json"
)


def native(value: Any) -> Any:
    """Recursively convert NumPy scalars/arrays for the shared JSON writer."""

    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, dict):
        return {str(key): native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [native(item) for item in value]
    return value


def normalize_positive(values: np.ndarray) -> np.ndarray | None:
    """Normalize nonnegative values, leaving the all-zero domain undefined."""

    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("leverage values must be a nonempty vector")
    if np.min(values) < -1.0e-12:
        raise ValueError("leverage values must be nonnegative")
    values = np.maximum(values, 0.0)
    total = float(np.sum(values))
    if total <= 1.0e-15:
        return None
    return values / total


def concentration_metrics(weights: np.ndarray) -> dict[str, float]:
    """Participation, Shannon/KL, and Gini/Lorenz readings used in SCI-01."""

    p = np.asarray(weights, dtype=float)
    if p.ndim != 1 or p.size == 0 or np.min(p) < -1.0e-12:
        raise ValueError("weights must be a nonempty nonnegative vector")
    p = p / np.sum(p)
    n = p.size
    baseline = 1.0 / math.sqrt(n)

    sum_squares = float(np.dot(p, p))
    n_eff_participation = 1.0 / sum_squares
    lambda_participation = math.sqrt(sum_squares)

    positive = p[p > 0.0]
    entropy = -float(np.sum(positive * np.log(positive)))
    n_eff_shannon = math.exp(entropy)
    lambda_shannon = math.exp(-0.5 * entropy)
    kl_from_uniform = math.log(n) - entropy

    ascending = np.sort(p)
    ranks = np.arange(1, n + 1, dtype=float)
    gini = (
        2.0 * float(np.dot(ranks, ascending)) / n
        - (n + 1.0) / n
    )
    gini = max(0.0, gini)
    gini_max = (n - 1.0) / n if n > 1 else 1.0
    gini_normalized = gini / gini_max if n > 1 else 0.0
    lambda_gini = baseline + (1.0 - baseline) * gini_normalized

    return {
        "n": int(n),
        "baseline": baseline,
        "sum_squares": sum_squares,
        "n_eff_participation": n_eff_participation,
        "n_eff_participation_fraction": n_eff_participation / n,
        "lambda_participation": lambda_participation,
        "entropy": entropy,
        "kl_from_uniform": kl_from_uniform,
        "n_eff_shannon": n_eff_shannon,
        "n_eff_shannon_fraction": n_eff_shannon / n,
        "lambda_shannon_kl": lambda_shannon,
        "gini": gini,
        "gini_normalized": gini_normalized,
        "lambda_gini_lorenz": lambda_gini,
        "max_share": float(np.max(p)),
    }


def fisher_leverages(
    records: np.ndarray,
    theta: np.ndarray,
    covariances: np.ndarray,
) -> dict[str, Any]:
    """Compute observed score leverage in the total Fisher metric.

    `covariances` may be one common SPD matrix or an N-stack of known SPD
    matrices.  The latter is the minimal heteroskedastic sensitivity:

        I_total = sum_i Sigma_i^-1,
        ell_i   = s_i^T I_total^-1 s_i.

    Only the common-covariance case carries the exact identity
    sum ell_i = 2 L_N for the predeclared named loss.
    """

    records = np.asarray(records, dtype=float)
    theta = np.asarray(theta, dtype=float)
    covariances = np.asarray(covariances, dtype=float)
    if records.ndim != 2 or theta.shape != (records.shape[1],):
        raise ValueError("records must be Nxd and theta must be length d")
    n, d = records.shape
    common = covariances.shape == (d, d)
    if common:
        covariance_stack = np.broadcast_to(covariances, (n, d, d))
        precision = np.linalg.inv(covariances)
        precision_stack = np.broadcast_to(precision, (n, d, d))
    elif covariances.shape == (n, d, d):
        covariance_stack = covariances
        precision_stack = np.linalg.inv(covariance_stack)
    else:
        raise ValueError("covariances must be dxd or Nxdxd")

    residuals = records - theta
    scores = np.einsum("nij,nj->ni", precision_stack, residuals)
    fisher_total = np.sum(precision_stack, axis=0)
    fisher_inverse = np.linalg.inv(fisher_total)
    leverages = np.einsum(
        "ni,ij,nj->n", scores, fisher_inverse, scores
    )
    leverages = np.maximum(leverages, 0.0)
    weights = normalize_positive(leverages)

    score_outer_sum = scores.T @ scores
    metric_trace = float(np.trace(fisher_inverse @ score_outer_sum))
    quadratic_terms = np.einsum(
        "ni,nij,nj->n", residuals, precision_stack, residuals
    )
    average_loss = 0.5 * float(np.mean(quadratic_terms))
    expected_metric_contributions = np.asarray(
        [
            np.trace(fisher_inverse @ precision_stack[index])
            for index in range(n)
        ],
        dtype=float,
    )
    expected_weights = expected_metric_contributions / np.sum(
        expected_metric_contributions
    )

    return {
        "common_covariance": common,
        "dimension": d,
        "record_count": n,
        "scores": scores,
        "fisher_total": fisher_total,
        "fisher_inverse": fisher_inverse,
        "leverages": leverages,
        "weights": weights,
        "metric_trace": metric_trace,
        "average_loss": average_loss,
        "quadratic_terms": quadratic_terms,
        "expected_metric_contributions": expected_metric_contributions,
        "expected_weights": expected_weights,
        "covariances": covariance_stack,
    }


def records_from_common_covariance(
    rng: np.random.Generator,
    n: int,
    theta: np.ndarray,
    covariance: np.ndarray,
) -> np.ndarray:
    chol = np.linalg.cholesky(covariance)
    return theta + rng.standard_normal((n, theta.size)) @ chol.T


def transformed_covariances(
    transform: np.ndarray, covariances: np.ndarray
) -> np.ndarray:
    covariances = np.asarray(covariances)
    if covariances.ndim == 2:
        return transform @ covariances @ transform.T
    return np.einsum(
        "ab,nbc,dc->nad", transform, covariances, transform
    )


def loglog_slope(xs: list[int] | np.ndarray, ys: list[float] | np.ndarray) -> float:
    return float(
        np.polyfit(
            np.log(np.asarray(xs, dtype=float)),
            np.log(np.asarray(ys, dtype=float)),
            1,
        )[0]
    )


def scenario_suite(rng: np.random.Generator) -> dict[str, Any]:
    """Null, iid, heteroskedastic, outlier, and GL(d) test cases."""

    d = 4
    theta = np.array([0.35, -0.2, 0.5, 0.1])
    covariance = np.array(
        [
            [1.7, 0.45, -0.20, 0.10],
            [0.45, 1.2, 0.30, -0.15],
            [-0.20, 0.30, 1.5, 0.25],
            [0.10, -0.15, 0.25, 0.9],
        ]
    )
    chol = np.linalg.cholesky(covariance)

    # Equal Mahalanobis radius in +/- coordinate directions.
    radius = 1.75
    whitened_equal = radius * np.vstack((np.eye(d), -np.eye(d)))
    equal_records = theta + whitened_equal @ chol.T
    equal = fisher_leverages(equal_records, theta, covariance)
    equal_metrics = concentration_metrics(equal["weights"])

    # The zero-score limit is outside the normalized distribution's domain.
    zero_records = np.repeat(theta[None, :], 2 * d, axis=0)
    zero = fisher_leverages(zero_records, theta, covariance)

    # Representative iid observed batch.
    iid_records = records_from_common_covariance(
        rng, 64, theta, covariance
    )
    iid = fisher_leverages(iid_records, theta, covariance)
    iid_metrics = concentration_metrics(iid["weights"])

    # Normalization nulls: p cannot retain a common raw scale, and exact
    # replication cannot distinguish new independent information from copies.
    common_rescale_factor = 37.0
    common_rescaled_weights = normalize_positive(
        common_rescale_factor * iid["leverages"]
    )
    duplication_factor = 4
    duplicated_records = np.repeat(
        iid_records, duplication_factor, axis=0
    )
    duplicated = fisher_leverages(
        duplicated_records, theta, covariance
    )
    duplicated_metrics = concentration_metrics(duplicated["weights"])

    # GL(d) coordinate change with a non-orthogonal, moderately conditioned A.
    q_left, _ = np.linalg.qr(rng.standard_normal((d, d)))
    q_right, _ = np.linalg.qr(rng.standard_normal((d, d)))
    transform = q_left @ np.diag([3.2, 1.4, 0.65, 0.28]) @ q_right
    transformed = fisher_leverages(
        iid_records @ transform.T,
        transform @ theta,
        transformed_covariances(transform, covariance),
    )

    # Correctly specified heteroskedastic extension.  Covariance multipliers
    # are test data, not fitted weights.
    covariance_multipliers = np.tile(
        np.array([0.25, 1.0, 4.0]), 100
    )
    hetero_covariances = (
        covariance_multipliers[:, None, None] * covariance[None, :, :]
    )
    hetero_records = np.empty((covariance_multipliers.size, d))
    for index, multiplier in enumerate(covariance_multipliers):
        z = rng.standard_normal(d)
        hetero_records[index] = theta + math.sqrt(multiplier) * (chol @ z)
    hetero = fisher_leverages(
        hetero_records, theta, hetero_covariances
    )
    hetero_metrics = concentration_metrics(hetero["weights"])
    hetero_groups: dict[str, Any] = {}
    for multiplier in (0.25, 1.0, 4.0):
        mask = covariance_multipliers == multiplier
        hetero_groups[str(multiplier)] = {
            "count": int(np.sum(mask)),
            "mean_expected_metric_contribution": float(
                np.mean(hetero["expected_metric_contributions"][mask])
            ),
            "mean_expected_normalized_weight": float(
                np.mean(hetero["expected_weights"][mask])
            ),
            "mean_observed_normalized_weight": float(
                np.mean(hetero["weights"][mask])
            ),
            "observed_group_share": float(
                np.sum(hetero["weights"][mask])
            ),
        }

    # Matched batch with and without one declared high-score record.
    outlier_n = 64
    whitened_base = rng.standard_normal((outlier_n, d))
    base_records = theta + whitened_base @ chol.T
    base = fisher_leverages(base_records, theta, covariance)
    outlier_whitened = whitened_base.copy()
    outlier_whitened[0] = np.array([12.0, 0.0, 0.0, 0.0])
    outlier_records = theta + outlier_whitened @ chol.T
    outlier = fisher_leverages(outlier_records, theta, covariance)
    base_metrics = concentration_metrics(base["weights"])
    outlier_metrics = concentration_metrics(outlier["weights"])

    # Expected/common Fisher contribution versus observed score leverage.
    expected_n = 16
    batches = 800
    observed_weights = np.empty((batches, expected_n))
    observed_leverages = np.empty((batches, expected_n))
    for batch in range(batches):
        sample = records_from_common_covariance(
            rng, expected_n, theta, covariance
        )
        result = fisher_leverages(sample, theta, covariance)
        observed_weights[batch] = result["weights"]
        observed_leverages[batch] = result["leverages"]
    expected_scalar = d / expected_n

    common_results = (
        equal,
        iid,
        duplicated,
        transformed,
        base,
        outlier,
    )
    max_metric_decomposition_error = max(
        abs(float(np.sum(result["leverages"])) - result["metric_trace"])
        for result in common_results + (hetero,)
    )
    max_common_loss_identity_error = max(
        abs(float(np.sum(result["leverages"])) - 2.0 * result["average_loss"])
        for result in common_results
    )

    return {
        "dimension": d,
        "theta": theta,
        "covariance": covariance,
        "equal_radius_null": {
            "radius": radius,
            "leverages": equal["leverages"],
            "weights": equal["weights"],
            "metrics": equal_metrics,
        },
        "zero_score_null": {
            "leverages": zero["leverages"],
            "normalizer": float(np.sum(zero["leverages"])),
            "weights_defined": zero["weights"] is not None,
            "weights": zero["weights"],
            "reading": (
                "All scores vanish, so the normalizing scalar is zero and "
                "p_i^F is undefined; no preferred uniform fill is inserted."
            ),
        },
        "iid_observed": {
            "record_count": iid["record_count"],
            "leverages": iid["leverages"],
            "weights": iid["weights"],
            "expected_weights": iid["expected_weights"],
            "metrics": iid_metrics,
        },
        "normalization_nulls": {
            "common_rescaling": {
                "factor": common_rescale_factor,
                "original_normalizer": float(np.sum(iid["leverages"])),
                "rescaled_normalizer": float(
                    np.sum(common_rescale_factor * iid["leverages"])
                ),
                "rescaled_weights": common_rescaled_weights,
                "max_weight_error": float(
                    np.max(
                        np.abs(common_rescaled_weights - iid["weights"])
                    )
                ),
                "reading": (
                    "A common positive rescaling changes the raw score-energy "
                    "carrier but cancels exactly from p_i."
                ),
            },
            "exact_duplication": {
                "factor": duplication_factor,
                "weights": duplicated["weights"],
                "metrics": duplicated_metrics,
                "aggregated_copy_weight_error": float(
                    np.max(
                        np.abs(
                            duplicated["weights"].reshape(
                                iid["record_count"], duplication_factor
                            ).sum(axis=1)
                            - iid["weights"]
                        )
                    )
                ),
                "participation_ratio_to_original": (
                    duplicated_metrics["lambda_participation"]
                    / iid_metrics["lambda_participation"]
                ),
                "shannon_ratio_to_original": (
                    duplicated_metrics["lambda_shannon_kl"]
                    / iid_metrics["lambda_shannon_kl"]
                ),
                "native_gini_error": abs(
                    duplicated_metrics["gini"] - iid_metrics["gini"]
                ),
                "reading": (
                    "Duplicating every record K times assigns p_i/K to each "
                    "copy, scales participation and Shannon amplitudes by "
                    "K^-1/2, and leaves native Gini unchanged. The normalized "
                    "profile alone cannot certify independent information."
                ),
            },
        },
        "expected_fisher_vs_observed_score": {
            "record_count": expected_n,
            "dimension": d,
            "analytic_expected_fisher_metric_contribution_per_record": expected_scalar,
            "analytic_expected_normalized_weight": 1.0 / expected_n,
            "monte_carlo_mean_observed_leverage_by_record": np.mean(
                observed_leverages, axis=0
            ),
            "monte_carlo_mean_observed_weight_by_record": np.mean(
                observed_weights, axis=0
            ),
            "monte_carlo_observed_weight_std": float(
                np.std(observed_weights)
            ),
            "single_batch_observed_weight_range": [
                float(np.min(observed_weights[0])),
                float(np.max(observed_weights[0])),
            ],
            "reading": (
                "Expected Fisher contribution is exactly uniform under iid "
                "identical records; observed score leverage is a random, "
                "sample-dependent realization and is not uniform in general."
            ),
        },
        "invertible_linear_reparameterization": {
            "transform": transform,
            "condition_number": float(np.linalg.cond(transform)),
            "max_leverage_error": float(
                np.max(np.abs(iid["leverages"] - transformed["leverages"]))
            ),
            "max_weight_error": float(
                np.max(np.abs(iid["weights"] - transformed["weights"]))
            ),
            "loss_error": abs(iid["average_loss"] - transformed["average_loss"]),
            "declared_group": (
                "GL(d): theta'=A theta, r_i'=A r_i, "
                "Sigma'=A Sigma A^T for invertible A"
            ),
        },
        "heteroskedastic": {
            "covariance_multipliers": covariance_multipliers,
            "leverages": hetero["leverages"],
            "weights": hetero["weights"],
            "expected_weights": hetero["expected_weights"],
            "metrics": hetero_metrics,
            "groups": hetero_groups,
            "metric_decomposition_error": abs(
                float(np.sum(hetero["leverages"]))
                - hetero["metric_trace"]
            ),
            "reading": (
                "With known unequal Sigma_i, I_total=sum_i Sigma_i^-1. "
                "Expected leverage is no longer uniform: more precise records "
                "carry more expected Fisher metric contribution. Observed "
                "leverage remains sample-dependent around that structure."
            ),
        },
        "outlier_control": {
            "outlier_index": 0,
            "declared_whitened_radius": 12.0,
            "matched_base_weights": base["weights"],
            "weights": outlier["weights"],
            "base_metrics": base_metrics,
            "outlier_metrics": outlier_metrics,
            "reading": (
                "The radius changes the declared test record, not the weight "
                "formula. A high realized score receives high leverage."
            ),
        },
        "identities": {
            "max_metric_decomposition_error": max_metric_decomposition_error,
            "max_common_loss_identity_error": max_common_loss_identity_error,
            "common_identity": "sum_i ell_i = 2 L_N",
            "general_metric_identity": (
                "sum_i ell_i = tr(I_total^-1 sum_i s_i s_i^T)"
            ),
        },
    }


def gradient_flow_suite(
    rng: np.random.Generator,
    covariance: np.ndarray,
    theta_center: np.ndarray,
) -> dict[str, Any]:
    """Follow the per-record-Fisher-natural gradient flow of the named loss."""

    records = records_from_common_covariance(
        rng, 80, theta_center, covariance
    )
    rbar = np.mean(records, axis=0)
    chol = np.linalg.cholesky(covariance)
    theta_initial = rbar + chol @ np.array([2.4, -1.5, 0.8, 0.35])
    times = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
    path = []
    for time in times:
        theta = rbar + math.exp(-time) * (theta_initial - rbar)
        result = fisher_leverages(records, theta, covariance)
        path.append(
            {
                "time": time,
                "theta": theta,
                "loss": result["average_loss"],
                "normalizer": float(np.sum(result["leverages"])),
                "weights": result["weights"],
                "metrics": concentration_metrics(result["weights"]),
            }
        )

    # Couple coordinate invariance to the dynamics itself, not merely to one
    # static profile.  The per-record Fisher-natural equation transforms as
    # theta_dot'=A theta_dot, so the exact path must obey theta'(t)=A theta(t).
    d = theta_center.size
    q_left, _ = np.linalg.qr(rng.standard_normal((d, d)))
    q_right, _ = np.linalg.qr(rng.standard_normal((d, d)))
    transform = q_left @ np.diag([2.7, 1.3, 0.72, 0.31]) @ q_right
    transformed_records = records @ transform.T
    transformed_covariance = transformed_covariances(transform, covariance)
    transformed_rbar = transform @ rbar
    transformed_theta_initial = transform @ theta_initial
    max_theta_equivariance_error = 0.0
    max_path_weight_invariance_error = 0.0
    max_path_loss_invariance_error = 0.0
    for index, time in enumerate(times):
        transformed_theta = transformed_rbar + math.exp(-time) * (
            transformed_theta_initial - transformed_rbar
        )
        original_theta = np.asarray(path[index]["theta"])
        max_theta_equivariance_error = max(
            max_theta_equivariance_error,
            float(
                np.linalg.norm(transformed_theta - transform @ original_theta)
            ),
        )
        transformed_result = fisher_leverages(
            transformed_records,
            transformed_theta,
            transformed_covariance,
        )
        max_path_weight_invariance_error = max(
            max_path_weight_invariance_error,
            float(
                np.max(
                    np.abs(
                        transformed_result["weights"]
                        - np.asarray(path[index]["weights"])
                    )
                )
            ),
        )
        max_path_loss_invariance_error = max(
            max_path_loss_invariance_error,
            abs(
                transformed_result["average_loss"]
                - float(path[index]["loss"])
            ),
        )

    losses = [entry["loss"] for entry in path]
    weight_sums = [float(np.sum(entry["weights"])) for entry in path]
    return {
        "completion": (
            "Per-record-Fisher-natural gradient: theta_dot = "
            "-Sigma grad_theta L_N = -(theta-rbar)"
        ),
        "times": times,
        "path": path,
        "loss_is_nonincreasing": all(
            losses[index + 1] <= losses[index] + 1.0e-13
            for index in range(len(losses) - 1)
        ),
        "max_weight_normalization_error": max(
            abs(value - 1.0) for value in weight_sums
        ),
        "initial_to_terminal_weight_l1": float(
            np.sum(np.abs(path[0]["weights"] - path[-1]["weights"]))
        ),
        "terminal_weight_l1_8_to_16": float(
            np.sum(np.abs(path[-2]["weights"] - path[-1]["weights"]))
        ),
        "GL_path_check": {
            "transform_condition_number": float(np.linalg.cond(transform)),
            "max_theta_equivariance_error": max_theta_equivariance_error,
            "max_weight_invariance_error": max_path_weight_invariance_error,
            "max_loss_invariance_error": max_path_loss_invariance_error,
            "exact_relation": (
                "rbar'=A rbar and theta_0'=A theta_0 imply "
                "theta'(t)=rbar'+exp(-t)(theta_0'-rbar')=A theta(t)"
            ),
        },
        "reading": (
            "The loss descends covariantly under the declared per-record-Fisher-natural "
            "completion. The leverage profile changes with theta and settles "
            "to the residual-score profile at the sample mean; concentration "
            "need not be a monotone Lyapunov observable."
        ),
    }


def accretion_suite(
    rng: np.random.Generator,
    covariance: np.ndarray,
    theta_center: np.ndarray,
) -> dict[str, Any]:
    """Accrete records, fully relax to rbar_N, and follow an early outlier."""

    d = theta_center.size
    n_max = 4096
    chol = np.linalg.cholesky(covariance)
    whitened = rng.standard_normal((n_max, d))
    whitened[0] = np.array([12.0, 0.0, 0.0, 0.0])
    stream = theta_center + whitened @ chol.T
    checkpoints = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    running_mean = np.zeros(d)
    recurrence_max_error = 0.0
    entries = []
    checkpoint_set = set(checkpoints)
    for index, record in enumerate(stream, start=1):
        running_mean = running_mean + (record - running_mean) / index
        direct_mean = np.mean(stream[:index], axis=0)
        recurrence_max_error = max(
            recurrence_max_error,
            float(np.linalg.norm(running_mean - direct_mean)),
        )
        if index in checkpoint_set:
            result = fisher_leverages(
                stream[:index], running_mean, covariance
            )
            entries.append(
                {
                    "record_count": index,
                    "theta_hat": running_mean.copy(),
                    "weights": result["weights"],
                    "outlier_share": float(result["weights"][0]),
                    "metrics": concentration_metrics(result["weights"]),
                }
            )

    tail_counts = [entry["record_count"] for entry in entries[3:]]
    tail_outlier_shares = [entry["outlier_share"] for entry in entries[3:]]
    return {
        "update": "theta_hat_N = theta_hat_(N-1) + (r_N-theta_hat_(N-1))/N",
        "checkpoints": entries,
        "max_online_vs_direct_mean_error": recurrence_max_error,
        "outlier_share_tail_slope": loglog_slope(
            tail_counts, tail_outlier_shares
        ),
        "outlier_share_dilution_factor": (
            entries[0]["outlier_share"] / entries[-1]["outlier_share"]
        ),
        "reading": (
            "At each checkpoint the loss is relaxed to the accreted sample "
            "mean. A fixed early high-score record is diluted by later iid "
            "accretion rather than creating a persistent target scale."
        ),
    }


def large_n_suite(rng: np.random.Generator, dimension: int = 4) -> dict[str, Any]:
    """Measure all three concentration readings for iid score leverage."""

    ns = [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    trials = 128
    summary = []
    for n in ns:
        metric_rows = []
        for _ in range(trials):
            quadratic_scores = rng.chisquare(dimension, size=n)
            weights = quadratic_scores / np.sum(quadratic_scores)
            metric_rows.append(concentration_metrics(weights))
        summary.append(
            {
                "record_count": n,
                "mean_lambda_participation": float(
                    np.mean(
                        [row["lambda_participation"] for row in metric_rows]
                    )
                ),
                "mean_lambda_shannon_kl": float(
                    np.mean(
                        [row["lambda_shannon_kl"] for row in metric_rows]
                    )
                ),
                "mean_lambda_gini_lorenz": float(
                    np.mean(
                        [row["lambda_gini_lorenz"] for row in metric_rows]
                    )
                ),
                "mean_gini": float(
                    np.mean([row["gini"] for row in metric_rows])
                ),
                "mean_n_eff_participation_fraction": float(
                    np.mean(
                        [
                            row["n_eff_participation_fraction"]
                            for row in metric_rows
                        ]
                    )
                ),
                "mean_n_eff_shannon_fraction": float(
                    np.mean(
                        [
                            row["n_eff_shannon_fraction"]
                            for row in metric_rows
                        ]
                    )
                ),
                "mean_max_share": float(
                    np.mean([row["max_share"] for row in metric_rows])
                ),
            }
        )

    # A single nested iid stream supplies raw profiles for Track C to recompute.
    quadratic_stream = rng.chisquare(dimension, size=ns[-1])
    representative_weights_by_n = {
        str(n): (
            quadratic_stream[:n] / np.sum(quadratic_stream[:n])
        )
        for n in ns
    }

    participation = [
        row["mean_lambda_participation"] for row in summary
    ]
    shannon = [row["mean_lambda_shannon_kl"] for row in summary]
    gini = [row["mean_gini"] for row in summary]
    max_share = [row["mean_max_share"] for row in summary]
    baseline = np.asarray([1.0 / math.sqrt(n) for n in ns])
    participation_enhancement = np.asarray(participation) - baseline
    shannon_enhancement = np.asarray(shannon) - baseline

    # For q~chi-square_4 = Gamma(2,2), these limits are exact.
    euler_gamma = 0.5772156649015329
    psi_three = 1.5 - euler_gamma
    theory_participation_fraction = dimension / (dimension + 2.0)
    theory_shannon_fraction = math.exp(math.log(2.0) - psi_three)
    theory_gini = 3.0 / 8.0

    return {
        "data_model": (
            "iid Gaussian records evaluated at the true theta; whitened "
            "quadratic score q_i~chi-square_d and p_i=q_i/sum q"
        ),
        "dimension": dimension,
        "trials_per_record_count": trials,
        "record_counts": ns,
        "summary": summary,
        "representative_weights_by_record_count": representative_weights_by_n,
        "slopes": {
            "lambda_participation": loglog_slope(ns, participation),
            "lambda_shannon_kl": loglog_slope(ns, shannon),
            "gini": loglog_slope(ns, gini),
            "mean_max_share": loglog_slope(ns, max_share),
            "participation_enhancement_over_uniform": loglog_slope(
                ns, participation_enhancement
            ),
            "shannon_enhancement_over_uniform": loglog_slope(
                ns, shannon_enhancement
            ),
        },
        "asymptotic_theory_chi_square_4": {
            "n_eff_participation_fraction": theory_participation_fraction,
            "n_eff_shannon_fraction": theory_shannon_fraction,
            "gini": theory_gini,
        },
        "reading": (
            "Participation and Shannon amplitude readings vanish as "
            "N^-1/2, including their enhancement over the uniform baseline. "
            "The largest individual share also vanishes. Gini instead tends "
            "to the nonzero relative inequality of chi-square_4 scores. This "
            "measure-dependent persistence is not a physical selector."
        ),
    }


def build_candidate(
    checks: list[dict[str, Any]], grade: str
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-PHY-02-TB-RECORD-FISHER",
        "track": "SWING-DU-PHY-02 / Track B / Lanes 1.3, 2.2, 4.4, A.1",
        "question": (
            "Does the named vector finality-consistency loss construct a "
            "nonnegative, normalized, GL(d)-invariant record influence "
            "distribution without fitted rho, Lambda, amplitude, or target "
            "concentration, and does any concentration persist under flow "
            "or accretion?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "STRUCTURAL_ANALOGY",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "The vector record loss is quadratic with known SPD "
                    "covariance geometry."
                ),
                "status": "STANDARD",
                "role": "Defines scores, loss curvature, and Fisher metric.",
            },
            {
                "id": "A2",
                "statement": (
                    "The finality-consistency empirical loss is the named "
                    "record-accretion object under investigation."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Binds the construction to the existing DU track.",
            },
            {
                "id": "A3",
                "statement": (
                    "Observed score energy in the total Fisher metric may be "
                    "read as per-record influence."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "This is the candidate physical interpretation, not a theorem.",
            },
            {
                "id": "A4",
                "statement": (
                    "The iid, heteroskedastic, and outlier data models are "
                    "declared controls rather than derived DU record laws."
                ),
                "status": "IMPORTED",
                "role": "Provides discriminating nulls and sensitivities.",
            },
            {
                "id": "A5",
                "statement": (
                    "Coordinate changes act through GL(d): theta'=A theta, "
                    "r'=A r, Sigma'=A Sigma A^T."
                ),
                "status": "STANDARD",
                "role": "Declares the exact invariance group tested.",
            },
            {
                "id": "A6",
                "statement": (
                    "The vector loss follows the natural gradient of its "
                    "per-record Fisher metric between accretion events."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Supplies a coordinate-covariant path; its time "
                    "normalization is conventional."
                ),
            },
            {
                "id": "A7",
                "statement": (
                    "Heteroskedastic covariance matrices are known and "
                    "I_total=sum_i Sigma_i^-1."
                ),
                "status": "IMPORTED",
                "role": "Tests sensitivity when records are not identically distributed.",
            },
        ],
        "free_choices": [
            {
                "id": "F1",
                "choice": "A four-component record and one non-diagonal SPD covariance.",
                "why_not_forced": "DU has not fixed the record dimension or covariance.",
                "sensitivity_test": (
                    "Apply a non-orthogonal GL(4) transformation and unequal "
                    "per-record covariance scales."
                ),
            },
            {
                "id": "F2",
                "choice": "Observed score leverage s_i^T I_total^-1 s_i.",
                "why_not_forced": (
                    "Fisher geometry does not by itself prove this is the "
                    "cosmological influence observable."
                ),
                "sensitivity_test": (
                    "Separate it from uniform expected Fisher contribution "
                    "and compare three concentration readings."
                ),
            },
            {
                "id": "F3",
                "choice": (
                    "Per-record-Fisher-natural rather than Euclidean vector "
                    "gradient flow, with unit time normalization."
                ),
                "why_not_forced": "A physical kinetic geometry is not yet selected.",
                "sensitivity_test": (
                    "Check loss descent, coordinate covariance, theta "
                    "dependence, and terminal settling without claiming selector status."
                ),
            },
            {
                "id": "F4",
                "choice": (
                    "Equal-radius, Gaussian, three-scale heteroskedastic, "
                    "one radius-12 outlier, common-rescaling, and exact-"
                    "duplication controls."
                ),
                "why_not_forced": "These are deterministic stress cases, not a DU data law.",
                "sensitivity_test": (
                    "Retain all raw weights and compare matched data before "
                    "and after each declared perturbation."
                ),
            },
            {
                "id": "F5",
                "choice": "Finite-N grid 32 through 8192 with 128 iid trials.",
                "why_not_forced": "The computational grid is a resolution choice.",
                "sensitivity_test": (
                    "Fit scaling over nine sizes and compare with exact "
                    "chi-square_4 asymptotic constants."
                ),
            },
        ],
        "equations": [
            "L_N(theta)=(1/2N) sum_i (theta-r_i)^T Sigma^-1(theta-r_i)",
            "s_i=Sigma^-1(r_i-theta); I_N=N Sigma^-1",
            "ell_i=s_i^T I_N^-1 s_i=(1/N)(r_i-theta)^T Sigma^-1(r_i-theta)",
            "p_i^F=ell_i/sum_j ell_j on the domain sum_j ell_j>0",
            "sum_i ell_i=2 L_N for common Sigma",
            "E[ell_i]=tr(I_N^-1 I_i)=d/N for iid identical records",
            "heteroskedastic: I_total=sum_i Sigma_i^-1",
            (
                "per-record-Fisher-natural flow: "
                "theta_dot=-Sigma grad L_N=-(theta-rbar)"
            ),
        ],
        "observables": [
            "raw normalized leverage vector p_i^F",
            "sum ell_i and the reconstructed Fisher-metric score trace",
            "named loss L_N along the natural-gradient path",
            "participation N_eff and Lambda_2=sqrt(sum p_i^2)",
            "Shannon/KL N_eff and Lambda_1=exp(-H/2)",
            "Gini/Lorenz relative inequality and endpoint-matched reading",
            "maximum record share and fixed-outlier share under accretion",
        ],
        "comparators": [
            "uniform expected Fisher contribution for iid identical records",
            "sample-dependent observed score leverage",
            "equal-Mahalanobis-radius records",
            "known heteroskedastic total-Fisher geometry",
            "matched batch before and after a declared outlier",
            "participation, Shannon/KL, and Gini/Lorenz concentration readings",
        ],
        "null_models": [
            "equal-radius records give exactly uniform leverage",
            "all-zero scores make the normalized distribution undefined",
            "iid identical records have uniform expected, not observed, contribution",
            "common positive rescaling changes raw score energy but not normalized weights",
            "exact K-fold record duplication rescales count-based readings without independent evidence",
        ],
        "falsifiers": [
            "negative leverage, failed normalization, or failed metric decomposition",
            "a joint invertible linear reparameterization changes ell_i or p_i",
            "expected iid Fisher contribution is not uniform",
            "the declared natural-gradient path increases the named loss",
            "a fixed early outlier retains a nonzero individual share under iid accretion",
            "large-N readings are reported as measure-independent when they disagree",
            "normalized weights are claimed to retain a common raw score-energy scale",
        ],
        "stop_conditions": [
            "do not insert rho, Lambda, a fitted amplitude, outlier rate, or target concentration",
            "do not repair zero total score by filling in a preferred distribution",
            "stop this formalization if GL(d) covariance or metric decomposition fails",
            "do not call observed Fisher leverage the cosmological observable without a new discriminator",
            "do not call relative Gini persistence a nonzero physical scale while individual shares vanish",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A live DU mechanism generates a normalized influence "
                "distribution whose nonuniformity may alter the uniform "
                "1/sqrt(N) baseline without choosing a target."
            ),
            "formalization_id": "RECORD-SCORE-FISHER-LEVERAGE",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "Observed score leverage constructs a live GL(d)-invariant "
                "record influence distribution wherever total score energy "
                "is nonzero. Expected iid contribution is uniform but "
                "realized leverage is sample-dependent. Under iid growth, "
                "participation and Shannon amplitudes vanish as N^-1/2 and "
                "individual shares vanish, while Gini retains relative "
                "inequality; no physical concentration functional or "
                "cosmological observable is selected."
            ),
            "grade": grade,
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "DU has not selected the score-leverage interpretation, "
                "record covariance/data law, physical gradient completion, "
                "concentration functional, or any identity with Lambda."
            ),
            "checks": checks,
        },
    }


def main() -> None:
    rng = np.random.default_rng(SEED)
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool) -> None:
        checks.append({"name": name, "pass": bool(condition)})

    scenarios = scenario_suite(rng)
    covariance = np.asarray(scenarios["covariance"])
    theta = np.asarray(scenarios["theta"])
    flow = gradient_flow_suite(rng, covariance, theta)
    accretion = accretion_suite(rng, covariance, theta)
    large_n = large_n_suite(rng)

    equal = scenarios["equal_radius_null"]
    zero = scenarios["zero_score_null"]
    iid = scenarios["iid_observed"]
    normalization_nulls = scenarios["normalization_nulls"]
    expected = scenarios["expected_fisher_vs_observed_score"]
    gl = scenarios["invertible_linear_reparameterization"]
    hetero = scenarios["heteroskedastic"]
    outlier = scenarios["outlier_control"]
    identities = scenarios["identities"]

    representative_defined = (
        equal["weights"],
        iid["weights"],
        hetero["weights"],
        outlier["weights"],
    )
    check("runtime uses pinned NumPy 2.5.1", np.__version__ == PINNED_NUMPY)
    check(
        "representative leverages are nonnegative and normalized",
        all(
            np.min(weights) >= -TOL
            and abs(float(np.sum(weights)) - 1.0) < TOL
            for weights in representative_defined
        ),
    )
    check(
        "score leverages exactly reconstruct the total Fisher-metric score trace",
        identities["max_metric_decomposition_error"] < 5.0e-12,
    )
    check(
        "common-covariance leverage sum exactly equals twice the named loss",
        identities["max_common_loss_identity_error"] < 5.0e-12,
    )
    check(
        "GL(4) joint reparameterization preserves every leverage",
        gl["max_leverage_error"] < 2.0e-11,
    )
    check(
        "GL(4) joint reparameterization preserves normalized weights and loss",
        gl["max_weight_error"] < 2.0e-12 and gl["loss_error"] < 2.0e-11,
    )
    check(
        "iid expected Fisher contribution is analytically uniform",
        np.max(
            np.abs(
                np.asarray(iid["expected_weights"])
                - 1.0 / iid["record_count"]
            )
        )
        < 2.0e-14,
    )
    check(
        "Monte Carlo mean observed iid weights recover uniform exchangeability",
        np.max(
            np.abs(
                np.asarray(expected["monte_carlo_mean_observed_weight_by_record"])
                - expected["analytic_expected_normalized_weight"]
            )
        )
        < 0.0045,
    )
    check(
        "observed score leverage is sample-dependent rather than identically uniform",
        expected["monte_carlo_observed_weight_std"] > 0.025
        and (
            expected["single_batch_observed_weight_range"][1]
            - expected["single_batch_observed_weight_range"][0]
        )
        > 0.02,
    )
    check(
        "equal-Mahalanobis-radius null gives uniform leverage",
        np.max(
            np.abs(
                np.asarray(equal["weights"])
                - 1.0 / len(equal["weights"])
            )
        )
        < 2.0e-14,
    )
    check(
        "zero-score null remains explicitly undefined",
        not zero["weights_defined"]
        and zero["normalizer"] <= 1.0e-15
        and zero["weights"] is None,
    )
    check(
        "representative iid batch is defined and nonuniform",
        iid["weights"] is not None
        and np.std(np.asarray(iid["weights"])) > 1.0e-3,
    )
    check(
        "common score-energy rescaling changes the raw carrier but not p_i",
        normalization_nulls["common_rescaling"]["max_weight_error"]
        < 2.0e-15
        and abs(
            normalization_nulls["common_rescaling"]["rescaled_normalizer"]
            / normalization_nulls["common_rescaling"]["original_normalizer"]
            - normalization_nulls["common_rescaling"]["factor"]
        )
        < 2.0e-14,
    )
    duplication = normalization_nulls["exact_duplication"]
    expected_duplication_ratio = 1.0 / math.sqrt(
        duplication["factor"]
    )
    check(
        "exact duplication exposes count scaling without independent information",
        duplication["aggregated_copy_weight_error"] < 2.0e-14
        and abs(
            duplication["participation_ratio_to_original"]
            - expected_duplication_ratio
        )
        < 2.0e-14
        and abs(
            duplication["shannon_ratio_to_original"]
            - expected_duplication_ratio
        )
        < 2.0e-14
        and duplication["native_gini_error"] < 2.0e-14,
    )

    hetero_groups = hetero["groups"]
    expected_group_means = [
        hetero_groups[key]["mean_expected_normalized_weight"]
        for key in ("0.25", "1.0", "4.0")
    ]
    observed_group_means = [
        hetero_groups[key]["mean_observed_normalized_weight"]
        for key in ("0.25", "1.0", "4.0")
    ]
    check(
        "known heteroskedastic Fisher geometry changes expected leverage by precision",
        expected_group_means[0] > expected_group_means[1] > expected_group_means[2],
    )
    check(
        "heteroskedastic observed group means resolve the expected precision ordering",
        observed_group_means[0] > observed_group_means[1] > observed_group_means[2],
    )

    base_metrics = outlier["base_metrics"]
    outlier_metrics = outlier["outlier_metrics"]
    check(
        "declared outlier is the largest observed leverage with substantial share",
        int(np.argmax(outlier["weights"])) == outlier["outlier_index"]
        and outlier["weights"][0] > 0.25,
    )
    check(
        "outlier increases all three concentration readings over the matched batch",
        all(
            outlier_metrics[key] > base_metrics[key]
            for key in (
                "lambda_participation",
                "lambda_shannon_kl",
                "lambda_gini_lorenz",
            )
        ),
    )
    check(
        "Fisher-natural gradient completion monotonically descends the named loss",
        flow["loss_is_nonincreasing"],
    )
    check(
        "the entire natural-gradient path is GL(4)-equivariant with invariant leverage",
        flow["GL_path_check"]["max_theta_equivariance_error"] < 2.0e-13
        and flow["GL_path_check"]["max_weight_invariance_error"] < 2.0e-12
        and flow["GL_path_check"]["max_loss_invariance_error"] < 2.0e-11,
    )
    check(
        "flow leverage remains normalized and settles at the sample-mean profile",
        flow["max_weight_normalization_error"] < 2.0e-14
        and flow["terminal_weight_l1_8_to_16"] < 1.0e-3,
    )
    check(
        "observed leverage responds nontrivially to theta along the flow",
        flow["initial_to_terminal_weight_l1"] > 0.10,
    )
    check(
        "online accretion recurrence equals the direct sample mean",
        accretion["max_online_vs_direct_mean_error"] < 2.0e-13,
    )
    check(
        "a fixed early outlier is diluted rather than sustained by iid accretion",
        -1.15 < accretion["outlier_share_tail_slope"] < -0.75
        and accretion["outlier_share_dilution_factor"] > 15.0,
    )

    slopes = large_n["slopes"]
    summary = large_n["summary"]
    theory = large_n["asymptotic_theory_chi_square_4"]
    check(
        "iid participation amplitude scales as N^-1/2",
        abs(slopes["lambda_participation"] + 0.5) < 0.025,
    )
    check(
        "iid Shannon/KL amplitude scales as N^-1/2",
        abs(slopes["lambda_shannon_kl"] + 0.5) < 0.025,
    )
    check(
        "participation and Shannon enhancements over uniform also scale as N^-1/2",
        abs(slopes["participation_enhancement_over_uniform"] + 0.5) < 0.04
        and abs(slopes["shannon_enhancement_over_uniform"] + 0.5) < 0.04,
    )
    check(
        "iid Gini retains relative score inequality at its chi-square_4 limit",
        abs(slopes["gini"]) < 0.04
        and abs(summary[-1]["mean_gini"] - theory["gini"]) < 0.02,
    )
    check(
        "large-N effective-count fractions match chi-square_4 theory",
        abs(
            summary[-1]["mean_n_eff_participation_fraction"]
            - theory["n_eff_participation_fraction"]
        )
        < 0.02
        and abs(
            summary[-1]["mean_n_eff_shannon_fraction"]
            - theory["n_eff_shannon_fraction"]
        )
        < 0.02,
    )
    check(
        "largest individual observed leverage share vanishes with record growth",
        slopes["mean_max_share"] < -0.70
        and summary[-1]["mean_max_share"] < 0.002,
    )

    grade = (
        "OBJECT-FOUND / SELECTOR-OPEN / DATA-MODEL-CONDITIONAL / "
        "MEASURE-DEPENDENT-PERSISTENCE"
    )
    candidate = build_candidate(checks, grade)
    contract_errors = validate_candidate_contract(candidate)
    if contract_errors:
        raise AssertionError(
            "candidate contract incomplete:\n" + "\n".join(contract_errors)
        )

    payload = {
        "probe": "du_record_fisher_influence_probe",
        "seed": SEED,
        "numpy_version": np.__version__,
        "pinned_numpy_version": PINNED_NUMPY,
        "grade": grade,
        "scenarios": scenarios,
        "gradient_flow": flow,
        "record_accretion": accretion,
        "large_N_scaling": large_n,
        "representative_raw_normalized_weights": {
            "equal_radius_null": equal["weights"],
            "zero_score_null": zero["weights"],
            "iid": iid["weights"],
            "heteroskedastic": hetero["weights"],
            "outlier": outlier["weights"],
            "exact_duplication": normalization_nulls[
                "exact_duplication"
            ]["weights"],
        },
        "scientific_reading": (
            "A record-native GL(d)-invariant influence object is constructed "
            "on the nonzero-score domain. It does not select a concentration "
            "functional: participation and Shannon amplitudes vanish as "
            "N^-1/2, while Gini preserves relative score inequality even as "
            "every individual share vanishes. The score-leverage identity "
            "with a cosmological observable remains open."
        ),
    }
    write_candidate_artifact(
        ARTIFACT_PATH, native(candidate), native(payload)
    )

    passed = sum(check_item["pass"] for check_item in checks)
    print("DU RECORD-SCORE / FISHER-METRIC INFLUENCE PROBE")
    for check_item in checks:
        state = "PASS" if check_item["pass"] else "FAIL"
        print(f"  {state}  {check_item['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(f"grade: {grade}")
    print(f"artifact: {ARTIFACT_PATH}")
    if passed != len(checks):
        failures = [
            item["name"] for item in checks if not item["pass"]
        ]
        raise SystemExit(f"unexpected failures: {failures}")


if __name__ == "__main__":
    main()
