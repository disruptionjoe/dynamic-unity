"""SWING-DU-SCI-01 Track 1: Bianconi completion and CLT robustness.

This probe asks three deliberately separate questions.

1. Does the Bianconi entropy action select a unique dynamics on a genuinely
   non-diagonal SPD metric?  It does not.  We compare the Euclidean gradient
   flow with the affine-invariant SPD gradient flow.  They share the action and
   stationary equation but have non-collinear vector fields.  An isospectral
   conservative flow is included as a no-relaxation control.
2. Does extensivity alone force an N**(-1/2) fluctuation density?  It does not.
   We compute the exact variance of a sum under iid, summable short-range,
   non-summable long-range, and global covariance.
3. Does either completion screen the extensive mean?  No such mechanism is in
   the tested action: at the shared stationary point the raw vacuum term grows
   linearly under block replication.

The result is conditional and local to this formalization.  It cannot falsify
CONCEPT-DU-001.  The JSON result is emitted through the shared conditional
candidate harness, whose contract completeness is not a scientific endorsement.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Callable

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


SEED = 20260723
SIGMA = 0.2
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_bianconi_completion_robustness_probe_result.json"
)


def sym(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (matrix + matrix.T)


def spectral_map(
    matrix: np.ndarray, function: Callable[[np.ndarray], np.ndarray]
) -> np.ndarray:
    values, vectors = np.linalg.eigh(sym(matrix))
    return sym((vectors * function(values)) @ vectors.T)


def log_spd(matrix: np.ndarray) -> np.ndarray:
    values = np.linalg.eigvalsh(sym(matrix))
    if float(np.min(values)) <= 0.0:
        raise ValueError("matrix is not SPD")
    return spectral_map(matrix, np.log)


def sqrt_spd(matrix: np.ndarray) -> np.ndarray:
    return spectral_map(matrix, np.sqrt)


def exp_symmetric(matrix: np.ndarray) -> np.ndarray:
    return spectral_map(matrix, np.exp)


def inv_spd(matrix: np.ndarray) -> np.ndarray:
    return spectral_map(matrix, lambda values: 1.0 / values)


def action(g: np.ndarray, g_ind: np.ndarray) -> float:
    """Bianconi metric action on a real SPD block."""

    sign, logdet = np.linalg.slogdet(g)
    if sign <= 0.0:
        raise ValueError("action received a non-SPD metric")
    relative = np.trace(g @ (log_spd(g) - log_spd(g_ind)))
    return float(SIGMA * logdet + relative - np.trace(g))


def euclidean_gradient(g: np.ndarray, g_ind: np.ndarray) -> np.ndarray:
    """Frobenius gradient of the Bianconi action."""

    return sym(SIGMA * inv_spd(g) + log_spd(g) - log_spd(g_ind))


def stable_scalar_root(g_ind_value: float) -> float:
    """Stable (g > sigma) solution of sigma/g + log(g) = log(g_ind)."""

    target = math.log(g_ind_value)
    g = max(1.25 * g_ind_value, 2.0 * SIGMA)
    for _ in range(200):
        value = SIGMA / g + math.log(g) - target
        derivative = (g - SIGMA) / (g * g)
        candidate = g - value / derivative
        if candidate <= SIGMA:
            candidate = 0.5 * (g + SIGMA)
        if abs(candidate - g) < 1.0e-15:
            return candidate
        g = candidate
    raise RuntimeError("stable scalar root did not converge")


def stable_matrix_root(g_ind: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(g_ind)
    roots = np.array([stable_scalar_root(float(value)) for value in values])
    return sym((vectors * roots) @ vectors.T)


def rotation_matrix() -> np.ndarray:
    q1, _ = np.linalg.qr(
        np.array(
            [
                [1.0, 0.7, -0.2],
                [0.4, -0.3, 1.1],
                [0.8, 0.5, 0.6],
            ]
        )
    )
    if np.linalg.det(q1) < 0.0:
        q1[:, 0] *= -1.0
    return q1


def armijo_flow(
    g0: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
    *,
    max_steps: int = 4000,
    tolerance: float = 6.0e-8,
) -> dict[str, object]:
    """Integrate one dissipative completion with SPD-preserving line search.

    The action change reaches float64 resolution when the Frobenius gradient is
    O(1e-8), so the declared 6e-8 stopping tolerance is a numerical precision
    boundary rather than a claim of exact symbolic stationarity.
    """

    if completion not in {"euclidean", "affine_invariant"}:
        raise ValueError(f"unknown completion: {completion}")

    g = g0.copy()
    actions = [action(g, g_ind)]
    accepted_steps: list[float] = []
    initial_velocity: np.ndarray | None = None

    for _ in range(max_steps):
        gradient = euclidean_gradient(g, g_ind)
        residual = float(np.linalg.norm(gradient, ord="fro"))
        if residual < tolerance:
            break

        if completion == "euclidean":
            velocity = -gradient
            directional_derivative = -residual * residual

            def propose(step: float) -> np.ndarray:
                return sym(g + step * velocity)

        else:
            root = sqrt_spd(g)
            natural_gradient = sym(root @ gradient @ root)
            velocity = -sym(g @ gradient @ g)
            directional_derivative = -float(
                np.linalg.norm(natural_gradient, ord="fro") ** 2
            )

            def propose(step: float) -> np.ndarray:
                move = exp_symmetric(-step * natural_gradient)
                return sym(root @ move @ root)

        if initial_velocity is None:
            initial_velocity = velocity.copy()

        step = 0.25
        current_action = actions[-1]
        for _ in range(80):
            candidate = propose(step)
            if float(np.min(np.linalg.eigvalsh(candidate))) <= 1.0e-10:
                step *= 0.5
                continue
            candidate_action = action(candidate, g_ind)
            if candidate_action <= current_action + 1.0e-4 * step * directional_derivative:
                break
            step *= 0.5
        else:
            raise RuntimeError(f"{completion} line search failed")

        if step < 1.0e-14:
            raise RuntimeError(f"{completion} line search stalled")
        g = candidate
        actions.append(candidate_action)
        accepted_steps.append(step)
    else:
        raise RuntimeError(f"{completion} flow exceeded {max_steps} steps")

    if initial_velocity is None:
        initial_velocity = np.zeros_like(g)
    return {
        "endpoint": g,
        "actions": np.array(actions),
        "steps": len(accepted_steps),
        "accepted_steps": np.array(accepted_steps),
        "residual": float(
            np.linalg.norm(euclidean_gradient(g, g_ind), ord="fro")
        ),
        "initial_velocity": initial_velocity,
    }


def conservative_isospectral_control() -> dict[str, float]:
    """Orthogonal Lax flow when G_ind=I: S is spectral and exactly conserved."""

    q = rotation_matrix()
    g = sym(q @ np.diag([0.55, 1.35, 2.4]) @ q.T)
    g_initial = g.copy()
    g_ind = np.eye(3)
    initial_action = action(g, g_ind)
    initial_residual = float(
        np.linalg.norm(euclidean_gradient(g, g_ind), ord="fro")
    )
    initial_eigenvalues = np.linalg.eigvalsh(g)

    generator = np.array(
        [
            [0.0, -0.9, 0.4],
            [0.9, 0.0, -0.6],
            [-0.4, 0.6, 0.0],
        ]
    )
    step = 0.07
    identity = np.eye(3)
    cayley = np.linalg.solve(
        identity - 0.5 * step * generator,
        identity + 0.5 * step * generator,
    )
    for _ in range(37):
        g = sym(cayley @ g @ cayley.T)

    return {
        "action_drift": abs(action(g, g_ind) - initial_action),
        "eigenvalue_drift": float(
            np.max(np.abs(np.linalg.eigvalsh(g) - initial_eigenvalues))
        ),
        "initial_residual": initial_residual,
        "final_residual": float(
            np.linalg.norm(euclidean_gradient(g, g_ind), ord="fro")
        ),
        "endpoint_displacement": float(
            np.linalg.norm(g - g_initial, ord="fro")
        ),
    }


def sum_variance(n: int, covariance: Callable[[int], float]) -> float:
    """Exact Var(sum_{i=1}^N X_i) for a stationary Toeplitz covariance."""

    value = n * covariance(0)
    value += 2.0 * sum(
        (n - lag) * covariance(lag) for lag in range(1, n)
    )
    return float(value)


def loglog_slope(ns: list[int], values: list[float], tail: int = 4) -> float:
    x = np.log(np.asarray(ns[-tail:], dtype=float))
    y = np.log(np.asarray(values[-tail:], dtype=float))
    return float(np.polyfit(x, y, 1)[0])


def fluctuation_tournament() -> dict[str, object]:
    """Compute fluctuation-density scaling across four correlation classes."""

    ns = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    rho = 0.65
    alpha = 0.5
    covariances: dict[str, Callable[[int], float]] = {
        "iid": lambda lag: 1.0 if lag == 0 else 0.0,
        "short_range_mixing": lambda lag: rho**lag,
        "long_range_power_law": lambda lag: (1.0 + lag) ** (-alpha),
        "global": lambda lag: 1.0,
    }

    classes: dict[str, object] = {}
    for name, covariance in covariances.items():
        variances = [sum_variance(n, covariance) for n in ns]
        densities = [math.sqrt(value) / n for value, n in zip(variances, ns)]
        classes[name] = {
            "variances": variances,
            "fluctuation_density": densities,
            "tail_loglog_slope": loglog_slope(ns, densities),
        }

    return {
        "sizes": ns,
        "rho_short_range": rho,
        "alpha_long_range": alpha,
        "classes": classes,
    }


def finite_difference_gradient_check(
    g: np.ndarray, g_ind: np.ndarray
) -> float:
    direction = sym(
        np.array(
            [
                [0.3, -0.2, 0.1],
                [-0.2, 0.4, 0.25],
                [0.1, 0.25, -0.15],
            ]
        )
    )
    epsilon = 1.0e-6
    finite_difference = (
        action(g + epsilon * direction, g_ind)
        - action(g - epsilon * direction, g_ind)
    ) / (2.0 * epsilon)
    analytic = float(np.trace(euclidean_gradient(g, g_ind) @ direction))
    return abs(finite_difference - analytic) / max(1.0, abs(analytic))


def main() -> None:
    rng = np.random.default_rng(SEED)
    q_ind, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q_ind) < 0.0:
        q_ind[:, 0] *= -1.0
    g_ind = sym(q_ind @ np.diag([0.9, 1.4, 2.4]) @ q_ind.T)

    q0 = rotation_matrix()
    g0 = sym(q0 @ np.diag([0.52, 1.65, 2.65]) @ q0.T)
    target = stable_matrix_root(g_ind)
    commutator_norm = float(np.linalg.norm(g0 @ g_ind - g_ind @ g0))
    gradient_error = finite_difference_gradient_check(g0, g_ind)

    euclidean = armijo_flow(g0, g_ind, "euclidean")
    affine = armijo_flow(g0, g_ind, "affine_invariant")

    v_e = np.asarray(euclidean["initial_velocity"])
    v_a = np.asarray(affine["initial_velocity"])
    direction_cosine = float(
        np.vdot(v_e, v_a).real
        / (
            np.linalg.norm(v_e, ord="fro")
            * np.linalg.norm(v_a, ord="fro")
        )
    )
    best_scalar = float(np.vdot(v_e, v_a).real / np.vdot(v_e, v_e).real)
    direction_noncollinearity = float(
        np.linalg.norm(v_a - best_scalar * v_e, ord="fro")
        / np.linalg.norm(v_a, ord="fro")
    )

    target_errors = {
        "euclidean": float(
            np.linalg.norm(np.asarray(euclidean["endpoint"]) - target, ord="fro")
        ),
        "affine_invariant": float(
            np.linalg.norm(np.asarray(affine["endpoint"]) - target, ord="fro")
        ),
    }
    endpoint_disagreement = float(
        np.linalg.norm(
            np.asarray(euclidean["endpoint"])
            - np.asarray(affine["endpoint"]),
            ord="fro",
        )
    )
    euclidean_monotone = bool(
        np.all(np.diff(np.asarray(euclidean["actions"])) <= 1.0e-11)
    )
    affine_monotone = bool(
        np.all(np.diff(np.asarray(affine["actions"])) <= 1.0e-11)
    )

    conservative = conservative_isospectral_control()
    fluctuations = fluctuation_tournament()
    fluctuation_classes = fluctuations["classes"]
    slopes = {
        name: float(result["tail_loglog_slope"])
        for name, result in fluctuation_classes.items()
    }

    # Replicating the stationary three-dimensional block tests the raw mean,
    # before the imported "subtract mean, retain fluctuation" prescription.
    block_mean = float(SIGMA * np.linalg.slogdet(target)[1])
    replications = [1, 2, 4, 8, 16, 32, 64]
    cell_counts = [3 * copies for copies in replications]
    raw_means = [copies * block_mean for copies in replications]
    mean_slope = loglog_slope(
        cell_counts, [abs(value) for value in raw_means], tail=5
    )
    mean_densities = [
        value / cells for value, cells in zip(raw_means, cell_counts)
    ]
    density_spread = max(mean_densities) - min(mean_densities)

    checks = [
        {
            "name": "matrix gradient matches a noncommuting finite-difference direction",
            "pass": gradient_error < 1.0e-7,
        },
        {
            "name": "specimen is genuinely non-diagonal and noncommuting",
            "pass": commutator_norm > 0.1,
        },
        {
            "name": "Euclidean completion dissipates S and reaches the stable equation",
            "pass": (
                euclidean_monotone
                and float(euclidean["residual"]) < 6.0e-8
                and target_errors["euclidean"] < 2.0e-7
            ),
        },
        {
            "name": "affine-invariant completion dissipates S and reaches the stable equation",
            "pass": (
                affine_monotone
                and float(affine["residual"]) < 6.0e-8
                and target_errors["affine_invariant"] < 2.0e-7
            ),
        },
        {
            "name": "legitimate dissipative completions have non-collinear vector fields",
            "pass": direction_noncollinearity > 0.08,
        },
        {
            "name": "dissipative completions agree on the stationary metric",
            "pass": endpoint_disagreement < 2.0e-7,
        },
        {
            "name": "conservative isospectral control preserves S and does not relax",
            "pass": (
                conservative["action_drift"] < 1.0e-10
                and conservative["eigenvalue_drift"] < 1.0e-10
                and abs(
                    conservative["final_residual"]
                    - conservative["initial_residual"]
                )
                < 1.0e-10
                and conservative["endpoint_displacement"] > 0.1
            ),
        },
        {
            "name": "iid fluctuations give the half-power density",
            "pass": abs(slopes["iid"] + 0.5) < 1.0e-10,
        },
        {
            "name": "summable short-range correlations retain the half-power asymptote",
            "pass": abs(slopes["short_range_mixing"] + 0.5) < 0.01,
        },
        {
            "name": "non-summable long-range correlations change the exponent",
            "pass": abs(slopes["long_range_power_law"] + 0.25) < 0.025,
        },
        {
            "name": "one global mode gives an unsuppressed density",
            "pass": abs(slopes["global"]) < 1.0e-10,
        },
        {
            "name": "extensivity alone does not determine the fluctuation exponent",
            "pass": (
                slopes["iid"] < slopes["long_range_power_law"] - 0.15
                and slopes["long_range_power_law"] < slopes["global"] - 0.15
            ),
        },
        {
            "name": "NO-SCREENING control: raw vacuum mean stays extensive",
            "pass": (
                abs(block_mean) > 1.0e-3
                and abs(mean_slope - 1.0) < 1.0e-10
                and abs(density_spread) < 1.0e-12
            ),
        },
    ]

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "SWING-DU-SCI-01-T1",
        "track": "Entropy-geometry completion robustness",
        "question": (
            "Which stationary, trajectory, fluctuation-scaling, and mean-screening "
            "claims survive legitimate completions of the Bianconi SPD entropy action?"
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
                    "The imported Bianconi metric action is evaluated on a real "
                    "non-diagonal SPD block."
                ),
                "status": "IMPORTED",
                "role": "Defines the static action and stationary equation under test.",
            },
            {
                "id": "A2",
                "statement": (
                    "The stable branch g > sigma is the local basin of interest; "
                    "the action is not claimed globally bounded near the SPD boundary."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Prevents a local-attractor result from being misstated globally.",
            },
            {
                "id": "A3",
                "statement": (
                    "Frobenius and affine-invariant SPD metrics are both legitimate "
                    "but non-unique dissipative completion choices."
                ),
                "status": "STANDARD",
                "role": "Makes completion nonuniqueness executable.",
            },
            {
                "id": "A4",
                "statement": (
                    "The fluctuation observable is a centered finite-variance sum "
                    "with the explicitly named stationary covariance kernel."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Exposes the dependence of the exponent on correlations.",
            },
            {
                "id": "A5",
                "statement": (
                    "Lambda_eff is identified with RMS fluctuation per cell after "
                    "the raw extensive mean is removed."
                ),
                "status": "IMPORTED",
                "role": "Marks the Sorkin-style observable identification, not a specimen result.",
            },
            {
                "id": "A6",
                "statement": "The tested substrate has fixed cell count N.",
                "status": "PROJECT_NATIVE",
                "role": "Limits the result to disclosure dynamics, not cell issuance.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "sigma=0.2 and one generic 3x3 noncommuting SPD fixture",
                "why_not_forced": "The specimen does not select this coupling or fixture.",
                "sensitivity_test": (
                    "The claims are expressed as structural checks: noncommutation, "
                    "stable-branch convergence, and covariance exponents, not fitted values."
                ),
            },
            {
                "id": "C2",
                "choice": "Euclidean and affine-invariant gradient metrics",
                "why_not_forced": "A variational action fixes extrema, not a mobility metric.",
                "sensitivity_test": (
                    "Compare vector-field collinearity, action descent, and endpoint agreement; "
                    "include an isospectral conservative no-relaxation control."
                ),
            },
            {
                "id": "C3",
                "choice": "rho=0.65 and long-range exponent alpha=0.5",
                "why_not_forced": "Neither correlation kernel is supplied by the action.",
                "sensitivity_test": (
                    "Use asymptotic classes: summable covariance should retain -1/2; "
                    "power-law alpha should give -alpha/2; global covariance should give 0."
                ),
            },
            {
                "id": "C4",
                "choice": "Block replication as the mean-screening discriminator",
                "why_not_forced": "No cosmological coupling or renormalization rule is built.",
                "sensitivity_test": (
                    "A real screen must make the raw term subextensive; constant density "
                    "under exact replication is an explicit no-screening result."
                ),
            },
        ],
        "equations": [
            "S(G)=sigma log det G + Tr[G(log G-log G_ind)]-Tr G",
            "grad_E S=sigma G^{-1}+log G-log G_ind",
            "dot G_E=-grad_E S",
            "dot G_AI=-G(grad_E S)G under the affine-invariant SPD metric",
            "Var(sum_i X_i)=N C(0)+2 sum_{r=1}^{N-1}(N-r)C(r)",
            "Lambda_eff(N)=sqrt(Var(sum_i X_i))/N",
        ],
        "observables": [
            "action monotonicity and stationary-gradient residual",
            "initial vector-field noncollinearity and endpoint agreement",
            "tail log-log slope of fluctuation density in four covariance classes",
            "raw vacuum-term growth and density under block replication",
        ],
        "comparators": [
            "Euclidean versus affine-invariant dissipative completion",
            "iid versus short-range, long-range, and global covariance",
            "raw extensive mean versus centered fluctuation density",
        ],
        "null_models": [
            "Isospectral orthogonal Lax flow: SPD dynamics without relaxation",
            "Global common mode: an extensive sum without CLT suppression",
        ],
        "falsifiers": [
            "A dissipative completion misses the shared stationary equation in its stable basin.",
            "The two gradient vector fields are collinear on the generic noncommuting fixture.",
            "Long-range or global covariance retains the iid half-power exponent.",
            "The raw stationary vacuum term becomes subextensive without an added constraint.",
        ],
        "stop_conditions": [
            (
                "Stop claiming completion-robust dynamics if modest legitimate SPD "
                "mobilities change the stationary observable rather than only its path."
            ),
            (
                "Stop saying the half-power is forced by extensivity alone; retain it "
                "only for covariance classes with Var(sum)=Theta(N)."
            ),
            (
                "Stop the Bianconi mean-screening route unless a separately specified "
                "constraint or dynamics makes the raw mean subextensive without hand subtraction."
            ),
            (
                "Any failure here is local to the Bianconi completion formalization; "
                "CONCEPT-DU-001 remains open absent an invariant-level no-go."
            ),
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "Lambda reads a dynamically sourced deviation of effective influence "
                "from uniform, is baseline at uniform, and grows monotonically with concentration."
            ),
            "formalization_id": "ADJACENT-BIANCONI-SPD-ENTROPY-COMPLETIONS",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "The two tested dissipative completions share the stable stationary "
                "metric but not the trajectory; the half-power survives iid and "
                "summable mixing correlations, fails for long-range/global correlation, "
                "and the raw extensive mean is not screened."
            ),
            "grade": (
                "PARTIAL — completion-robust local fixed point and mixing-class "
                "half-power; completion not selected, observable imported, mean unscreened."
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Only one finite non-diagonal block and two dissipative mobilities are "
                "tested; covariance calculations use linearized centered fluctuations; "
                "no cell growth, cosmological response, or native subtraction mechanism exists."
            ),
            "checks": checks,
        },
    }

    payload = {
        "seed": SEED,
        "parameters": {
            "sigma": SIGMA,
            "matrix_dimension": 3,
            "flow_residual_tolerance": 6.0e-8,
            "flow_tolerance_note": (
                "Float64 Armijo action differences reach their precision floor "
                "at residual O(1e-8); endpoint agreement is checked independently."
            ),
            "g_ind_eigenvalues": np.linalg.eigvalsh(g_ind).tolist(),
            "g0_eigenvalues": np.linalg.eigvalsh(g0).tolist(),
        },
        "matrix_validation": {
            "initial_commutator_norm": commutator_norm,
            "directional_gradient_relative_error": gradient_error,
        },
        "dynamics": {
            "initial_direction_cosine": direction_cosine,
            "initial_direction_noncollinearity": direction_noncollinearity,
            "shared_endpoint_disagreement_frobenius": endpoint_disagreement,
            "target_errors": target_errors,
            "euclidean": {
                "steps": int(euclidean["steps"]),
                "residual": float(euclidean["residual"]),
                "action_initial": float(np.asarray(euclidean["actions"])[0]),
                "action_final": float(np.asarray(euclidean["actions"])[-1]),
                "minimum_step": float(
                    np.min(np.asarray(euclidean["accepted_steps"]))
                ),
            },
            "affine_invariant": {
                "steps": int(affine["steps"]),
                "residual": float(affine["residual"]),
                "action_initial": float(np.asarray(affine["actions"])[0]),
                "action_final": float(np.asarray(affine["actions"])[-1]),
                "minimum_step": float(
                    np.min(np.asarray(affine["accepted_steps"]))
                ),
            },
            "conservative_control": conservative,
        },
        "fluctuation_scaling": fluctuations,
        "mean_screening": {
            "stationary_block_raw_vacuum_mean": block_mean,
            "cell_counts": cell_counts,
            "raw_means": raw_means,
            "raw_mean_densities": mean_densities,
            "raw_mean_loglog_slope": mean_slope,
            "screened": False,
        },
        "scope": {
            "fixed_point": (
                "Robust across the two tested dissipative metric choices in one local stable basin."
            ),
            "trajectory": "Not robust: the initial vector fields are non-collinear.",
            "half_power": (
                "Conditional on Var(sum)=Theta(N), satisfied by iid and summable mixing covariance."
            ),
            "mean": "Not screened by the tested action or completions.",
            "concept": (
                "A failure is local to this adjacent formalization and does not close CONCEPT-DU-001."
            ),
        },
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(f"incomplete candidate contract: {receipt['contract_errors']}")

    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("SWING-DU-SCI-01 TRACK 1 — BIANCONI COMPLETION ROBUSTNESS")
    print("=" * 72)
    print(
        "non-diagonal fixture:"
        f" commutator={commutator_norm:.6f}, gradient error={gradient_error:.3e}"
    )
    print(
        "dissipative completions:"
        f" direction cosine={direction_cosine:.6f},"
        f" noncollinearity={direction_noncollinearity:.6f}"
    )
    print(
        "shared endpoint:"
        f" disagreement={endpoint_disagreement:.3e},"
        f" residuals=({float(euclidean['residual']):.3e},"
        f" {float(affine['residual']):.3e})"
    )
    print(
        "conservative control:"
        f" action drift={conservative['action_drift']:.3e},"
        f" endpoint motion={conservative['endpoint_displacement']:.6f}"
    )
    print("fluctuation-density slopes:")
    for name in (
        "iid",
        "short_range_mixing",
        "long_range_power_law",
        "global",
    ):
        print(f"  {name:24s} {slopes[name]:+.6f}")
    print(
        "raw mean:"
        f" block={block_mean:+.6e}, growth slope={mean_slope:+.6f},"
        " screened=False"
    )
    print("-" * 72)
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    passed = sum(bool(check["pass"]) for check in checks)
    print("-" * 72)
    print(f"{passed}/{len(checks)} scientific checks pass")
    print(f"contract: {receipt['contract_status']} (not a scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    print(
        "GRADE: PARTIAL — fixed point robust locally; path non-unique; "
        "half-power requires summable correlations; mean unscreened."
    )

    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
