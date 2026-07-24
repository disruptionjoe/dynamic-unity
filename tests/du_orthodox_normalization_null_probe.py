"""Orthodox-council null for the SWING-DU-PHY-02 interpretation.

The physical-influence wave found two features that might look mechanism
specific:

1. a normalized modal profile becoming point-like while raw dissipation
   vanishes; and
2. the replication signature
   ``(D, lambda_2, lambda_H, Gini, max p) ~
   (K, K^-1/2, K^-1/2, K^0, K^-1)``.

This probe asks whether those features discriminate the Dynamic Unity concept
from an ordinary linear quadratic relaxation.  They do not.  For

    S(X; A) = 1/2 Tr(X A X A),
    grad S  = A X A,
    dot X   = -A X A,

with commuting diagonal ``A`` and ``X``, each mode obeys
``x_i(t)=x_i(0) exp(-r_i t)`` for ``r_i=A_i^2`` and the instantaneous
dissipation is ``D=sum_i (r_i x_i)^2``.  A unique slow rate generically leaves
a point residue after normalization even though ``D -> 0``.  A degenerate
slow subspace leaves an initial-condition-dependent residue.  Identical block
replication gives the same exponent tuple by normalization alone.

The null has no higher-order influence-redistribution law, record-growth law,
functional selector, unit-bearing observable map, or cosmological
identification.  Reproducing the signatures therefore preserves them as
diagnostics while preventing them from carrying concept-level evidence by
themselves.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Sequence

import numpy as np


SEED = 20260724
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_orthodox_normalization_null_probe_result.json"
)


def normalize(contributions: Sequence[float]) -> np.ndarray | None:
    values = np.asarray(contributions, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("contributions must be a nonempty vector")
    if float(np.min(values)) < 0.0:
        raise ValueError("contributions must be nonnegative")
    total = float(np.sum(values))
    if total == 0.0:
        return None
    return values / total


def shape_metrics(weights: Sequence[float]) -> dict[str, float]:
    p = normalize(weights)
    if p is None:
        raise ValueError("shape metrics are undefined at zero total")
    positive = p[p > 0.0]
    entropy = -float(np.sum(positive * np.log(positive)))
    ordered = np.sort(p)
    n = p.size
    ranks = np.arange(1, n + 1, dtype=float)
    gini = float(
        2.0 * np.dot(ranks, ordered) / n - (n + 1.0) / n
    )
    return {
        "lambda_participation": float(np.sqrt(np.dot(p, p))),
        "lambda_shannon": float(math.exp(-0.5 * entropy)),
        "native_gini": max(0.0, gini),
        "max_share": float(np.max(p)),
        "entropy": entropy,
    }


def quadratic_snapshot(
    rates: Sequence[float],
    initial_diagonal: Sequence[float],
    time: float,
) -> dict[str, Any]:
    r = np.asarray(rates, dtype=float)
    x0 = np.asarray(initial_diagonal, dtype=float)
    if r.shape != x0.shape or float(np.min(r)) <= 0.0:
        raise ValueError("rates and initial diagonal must match; rates are positive")
    x = x0 * np.exp(-r * time)
    gradient_eigenvalues = r * x
    contributions = np.square(gradient_eigenvalues)
    dissipation = float(np.sum(contributions))
    action = 0.5 * float(np.sum(r * np.square(x)))
    exact_negative_action_derivative = float(
        np.sum(np.square(r * x))
    )
    p = normalize(contributions)
    return {
        "time": float(time),
        "rates": r.tolist(),
        "state_eigenvalues": x.tolist(),
        "action": action,
        "gradient_eigenvalues": gradient_eigenvalues.tolist(),
        "squared_modal_contributions": contributions.tolist(),
        "total_dissipation": dissipation,
        "exact_negative_action_derivative": exact_negative_action_derivative,
        "dissipation_identity_error": abs(
            dissipation - exact_negative_action_derivative
        ),
        "normalized_profile": None if p is None else np.sort(p)[::-1].tolist(),
        "metrics": None if p is None else shape_metrics(p),
    }


def orthogonal_invariance_check(
    rates: Sequence[float],
    initial_diagonal: Sequence[float],
    time: float,
) -> dict[str, float]:
    r = np.asarray(rates, dtype=float)
    x0 = np.asarray(initial_diagonal, dtype=float)
    a = np.diag(np.sqrt(r))
    x = np.diag(x0 * np.exp(-r * time))
    e = a @ x @ a
    original = np.sort(np.square(np.linalg.eigvalsh(e)))[::-1]
    original_d = float(np.trace(e @ e))

    rng = np.random.default_rng(SEED)
    q, _ = np.linalg.qr(rng.normal(size=(r.size, r.size)))
    if np.linalg.det(q) > 0.0:
        q[:, 0] *= -1.0
    transformed_a = q @ a @ q.T
    transformed_x = q @ x @ q.T
    transformed_e = transformed_a @ transformed_x @ transformed_a
    transformed = np.sort(
        np.square(np.linalg.eigvalsh(transformed_e))
    )[::-1]
    transformed_d = float(np.trace(transformed_e @ transformed_e))
    return {
        "orthogonality_error": float(
            np.linalg.norm(q.T @ q - np.eye(r.size), ord="fro")
        ),
        "determinant": float(np.linalg.det(q)),
        "modal_contribution_max_error": float(
            np.max(np.abs(original - transformed))
        ),
        "dissipation_error": abs(original_d - transformed_d),
    }


def loglog_slope(xs: Sequence[float], ys: Sequence[float]) -> float:
    return float(
        np.polyfit(
            np.log(np.asarray(xs, dtype=float)),
            np.log(np.asarray(ys, dtype=float)),
            1,
        )[0]
    )


def replication_null() -> dict[str, Any]:
    base_profile = np.asarray([0.50, 0.30, 0.20])
    base_dissipation = 7.0
    block_counts = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    rows: list[dict[str, Any]] = []
    for count in block_counts:
        weights = np.tile(base_profile / count, count)
        rows.append(
            {
                "block_count": count,
                "raw_total_dissipation": count * base_dissipation,
                **shape_metrics(weights),
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
            block_counts,
            [row["native_gini"] for row in rows],
        ),
        "max_share": loglog_slope(
            block_counts,
            [row["max_share"] for row in rows],
        ),
    }
    return {
        "base_profile": base_profile.tolist(),
        "base_dissipation": base_dissipation,
        "rows": rows,
        "slopes": slopes,
        "native_gini_spread": float(
            max(row["native_gini"] for row in rows)
            - min(row["native_gini"] for row in rows)
        ),
    }


def main() -> None:
    unique_initial = quadratic_snapshot([1.0, 2.0, 4.0], [1.0, 1.0, 1.0], 0.0)
    unique_terminal = quadratic_snapshot(
        [1.0, 2.0, 4.0], [1.0, 1.0, 1.0], 16.0
    )
    exact_stationary = quadratic_snapshot(
        [1.0, 2.0, 4.0], [0.0, 0.0, 0.0], 0.0
    )
    degenerate_a = quadratic_snapshot(
        [1.0, 1.0, 4.0], [1.0, 2.0, 1.0], 16.0
    )
    degenerate_b = quadratic_snapshot(
        [1.0, 1.0, 4.0], [1.0, 3.0, 1.0], 16.0
    )
    orthogonal = orthogonal_invariance_check(
        [1.0, 2.0, 4.0], [1.0, 1.0, 1.0], 1.25
    )
    replication = replication_null()

    unique_ratio = (
        unique_terminal["total_dissipation"]
        / unique_initial["total_dissipation"]
    )
    degenerate_delta = float(
        np.max(
            np.abs(
                np.asarray(degenerate_a["normalized_profile"])
                - np.asarray(degenerate_b["normalized_profile"])
            )
        )
    )
    slopes = replication["slopes"]
    checks = [
        {
            "name": "quadratic modal squares exactly reconstruct action dissipation",
            "pass": max(
                unique_initial["dissipation_identity_error"],
                unique_terminal["dissipation_identity_error"],
                degenerate_a["dissipation_identity_error"],
                degenerate_b["dissipation_identity_error"],
            )
            < 1.0e-14,
        },
        {
            "name": "simultaneous O(3) similarity preserves the quadratic modal receipt",
            "pass": (
                orthogonal["orthogonality_error"] < 1.0e-12
                and orthogonal["modal_contribution_max_error"] < 1.0e-12
                and orthogonal["dissipation_error"] < 1.0e-12
            ),
        },
        {
            "name": "a unique slow quadratic mode gives a point residue while raw dissipation vanishes",
            "pass": (
                unique_terminal["normalized_profile"][0] > 1.0 - 1.0e-12
                and unique_ratio < 1.0e-12
            ),
        },
        {
            "name": "the exact zero-dissipation quadratic endpoint remains undefined",
            "pass": exact_stationary["normalized_profile"] is None,
        },
        {
            "name": "a degenerate slow subspace leaves an initial-condition-dependent residue",
            "pass": (
                degenerate_a["normalized_profile"][0] > 0.79
                and degenerate_b["normalized_profile"][0] > 0.89
                and degenerate_delta > 0.09
            ),
        },
        {
            "name": "identical replication gives the generic normalization signature",
            "pass": (
                abs(slopes["raw_total_dissipation"] - 1.0) < 1.0e-12
                and abs(slopes["lambda_participation"] + 0.5) < 1.0e-12
                and abs(slopes["lambda_shannon"] + 0.5) < 1.0e-12
                and abs(slopes["native_gini"]) < 1.0e-12
                and abs(slopes["max_share"] + 1.0) < 1.0e-12
                and replication["native_gini_spread"] < 1.0e-12
            ),
        },
    ]
    payload = {
        "probe": "du_orthodox_normalization_null_probe",
        "seed": SEED,
        "numpy_version": np.__version__,
        "contested_finding": (
            "The live-object receipts materially support CONCEPT-DU-001, rather "
            "than only constructing concept-compatible formalization components."
        ),
        "null_model": {
            "action": "S(X;A)=1/2 Tr(X A X A)",
            "gradient": "E=A X A",
            "flow": "dot X=-A X A",
            "declared_absences": [
                "higher-order influence-redistribution mechanism",
                "record-growth law",
                "functional selector",
                "unit-bearing map to a physical observable",
                "cosmological Lambda identification",
            ],
        },
        "unique_slow_mode": {
            "initial": unique_initial,
            "terminal": unique_terminal,
            "terminal_over_initial_dissipation": unique_ratio,
            "interpretation": (
                "The point residue is a generic spectral-relaxation effect. It "
                "can diagnose a slow mode, but does not by itself evidence the "
                "Dynamic Unity influence concept."
            ),
        },
        "degenerate_slow_subspace": {
            "initial_condition_a": degenerate_a,
            "initial_condition_b": degenerate_b,
            "profile_max_difference": degenerate_delta,
            "interpretation": (
                "Without a simple slow rate, the residue is not universal; it "
                "retains initial-condition information inside the slow subspace."
            ),
        },
        "orthogonal_invariance": orthogonal,
        "exact_stationary": exact_stationary,
        "replication": replication,
        "checks": checks,
        "result": {
            "passed": sum(bool(check["pass"]) for check in checks),
            "total": len(checks),
            "verdict": (
                "NULL_REPRODUCES_SIGNATURE / CONCEPT_GRADE_NARROWED / "
                "DIAGNOSTIC_USE_PRESERVED"
            ),
            "scientific_reading": (
                "The replication exponents are a normalization theorem, and a "
                "point-like terminal residue occurs in an ordinary quadratic "
                "relaxation. These facts uphold the no-scale conclusion and "
                "preserve diagnostic uses, but are not discriminating evidence "
                "for the full CONCEPT-DU-001 invariant."
            ),
        },
    }
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("ORTHODOX COUNCIL — NORMALIZATION / QUADRATIC NULL")
    print("=" * 72)
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print("-" * 72)
    print(f"{payload['result']['passed']}/{payload['result']['total']} checks pass")
    print(f"artifact: {ARTIFACT_PATH}")
    print(f"VERDICT: {payload['result']['verdict']}")
    if payload["result"]["passed"] != payload["result"]["total"]:
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
