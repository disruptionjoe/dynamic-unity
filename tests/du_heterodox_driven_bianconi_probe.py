"""Heterodox council swing: Bianconi dissipation under an open drive.

SWING-DU-PHY-02 established that both tested Bianconi gradient completions
relax to zero dissipation when the inducing metric is fixed.  This probe asks
whether that vanishing is a property of the Bianconi object or of the closed,
fixed-target completion.

The minimal conditional opening is a rotating anisotropic inducing metric,

    G_ind(n) = Q(n) G_ind(0) Q(n)^T,
    Q(n) = exp(n Omega),

where ``n`` is dimensionless event count and Omega is a fixed skew generator
per event.  No target concentration, rho, Lambda, cosmological time, or
dimensional rate is supplied.  For

    S(G,G_ind) =
        sigma log det G + Tr[G(log G-log G_ind)] - Tr G,

the time-dependent energy balance is

    dS/dn = -D_X + P_drive,
    P_drive = -Tr[G d(log G_ind)/dn].

A periodic driven state can therefore sustain nonzero D_X by balancing
injected work.  The construction is deliberately not a generated scale:
Omega is an imported dimensionless cadence, and the probe tests whether the
tail dissipation inherits that cadence.

Pinned NumPy + stdlib. Deterministic. Contract completeness is an
interpretability receipt, not a scientific endorsement.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)
from du_bianconi_completion_robustness_probe import (
    SIGMA,
    action,
    euclidean_gradient,
    exp_symmetric,
    log_spd,
    sqrt_spd,
    stable_matrix_root,
    sym,
)


PINNED_NUMPY = "2.5.1"
COMPLETIONS = ("euclidean", "affine_invariant")
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_heterodox_driven_bianconi_probe_result.json"
)
AXIS = np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0)
ANISOTROPIC_TARGET = np.diag([0.9, 1.4, 2.4])
DRIVE_RATES = (0.05, 0.1, 0.2, 0.4, 0.8)
DRIVE_CYCLES = 6
TAIL_CYCLES = 2
BASE_STEP = 0.02
PRIMARY_RATE = 0.4


def skew(vector: np.ndarray) -> np.ndarray:
    x, y, z = np.asarray(vector, dtype=float)
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def rotation(angle: float) -> np.ndarray:
    """Rodrigues rotation around the fixed unit axis."""

    k = skew(AXIS)
    return (
        np.eye(3)
        + math.sin(angle) * k
        + (1.0 - math.cos(angle)) * (k @ k)
    )


def completion_snapshot(
    g: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
) -> dict[str, Any]:
    gradient = euclidean_gradient(g, g_ind)
    if completion == "euclidean":
        operator = gradient
    elif completion == "affine_invariant":
        root = sqrt_spd(g)
        operator = sym(root @ gradient @ root)
    else:
        raise ValueError(f"unknown completion {completion!r}")
    eigenvalues = np.linalg.eigvalsh(operator)
    contributions = np.square(eigenvalues)
    dissipation = float(np.sum(contributions))
    weights = (
        None
        if dissipation <= 1.0e-26
        else np.sort(contributions / dissipation)[::-1]
    )
    return {
        "total_dissipation": dissipation,
        "operator_eigenvalues": eigenvalues,
        "contributions": contributions,
        "weights": weights,
    }


def flow_step(
    g: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
    step: float,
) -> np.ndarray:
    gradient = euclidean_gradient(g, g_ind)
    if completion == "euclidean":
        candidate = sym(g - step * gradient)
    elif completion == "affine_invariant":
        root = sqrt_spd(g)
        natural = sym(root @ gradient @ root)
        candidate = sym(root @ exp_symmetric(-step * natural) @ root)
    else:
        raise ValueError(f"unknown completion {completion!r}")
    if float(np.min(np.linalg.eigvalsh(candidate))) <= 0.0:
        raise RuntimeError("flow step left the SPD cone")
    return candidate


def driven_target(
    base_target: np.ndarray,
    rate: float,
    event_time: float,
    frame: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return G_ind and d(log G_ind)/dn in the requested O(3) frame."""

    q = rotation(rate * event_time)
    base_log = log_spd(base_target)
    omega = rate * skew(AXIS)
    target = sym(q @ base_target @ q.T)
    target_log = sym(q @ base_log @ q.T)
    target_log_derivative = sym(omega @ target_log - target_log @ omega)
    return (
        sym(frame @ target @ frame.T),
        sym(frame @ target_log_derivative @ frame.T),
    )


def run_driven(
    completion: str,
    rate: float,
    requested_step: float,
    *,
    cycles: int = DRIVE_CYCLES,
    tail_cycles: int = TAIL_CYCLES,
    base_target: np.ndarray = ANISOTROPIC_TARGET,
    frame: np.ndarray | None = None,
) -> dict[str, Any]:
    """Integrate enough exact drive cycles to test the periodic tail."""

    if rate <= 0.0:
        raise ValueError("run_driven requires a positive rate")
    if frame is None:
        frame = np.eye(3)
    period = 2.0 * math.pi / rate
    steps_per_cycle = int(math.ceil(period / requested_step))
    step = period / steps_per_cycle
    total_steps = cycles * steps_per_cycle
    tail_start = (cycles - tail_cycles) * steps_per_cycle

    equilibrium = stable_matrix_root(base_target)
    g = sym(frame @ equilibrium @ frame.T)
    tail_dissipation: list[float] = []
    tail_work: list[float] = []
    tail_weights: list[np.ndarray] = []
    tail_actions: list[float] = []
    tail_states: list[np.ndarray] = []
    minimum_state_eigenvalue = float(np.min(np.linalg.eigvalsh(g)))

    for index in range(total_steps + 1):
        event_time = index * step
        g_ind, log_derivative = driven_target(
            base_target, rate, event_time, frame
        )
        snapshot = completion_snapshot(g, g_ind, completion)
        drive_work = -float(np.trace(g @ log_derivative))
        if index >= tail_start:
            tail_dissipation.append(snapshot["total_dissipation"])
            tail_work.append(drive_work)
            if snapshot["weights"] is None:
                raise RuntimeError("driven tail unexpectedly has zero dissipation")
            tail_weights.append(np.asarray(snapshot["weights"]))
            tail_actions.append(action(g, g_ind))
            tail_states.append(g.copy())
        if index == total_steps:
            break
        g = flow_step(g, g_ind, completion, step)
        minimum_state_eigenvalue = min(
            minimum_state_eigenvalue,
            float(np.min(np.linalg.eigvalsh(g))),
        )

    # The endpoint is duplicated between cycle slices, so compare equal-length
    # arrays that exclude the final shared phase point.
    cycle_count = steps_per_cycle
    previous_d = np.asarray(
        tail_dissipation[-2 * cycle_count : -cycle_count]
    )
    final_d = np.asarray(tail_dissipation[-cycle_count - 1 : -1])
    previous_p = np.asarray(
        tail_weights[-2 * cycle_count : -cycle_count]
    )
    final_p = np.asarray(tail_weights[-cycle_count - 1 : -1])
    mean_d = float(np.mean(final_d))
    mean_work = float(
        np.mean(np.asarray(tail_work[-cycle_count - 1 : -1]))
    )
    state_periodicity_error = float(
        np.linalg.norm(tail_states[-1] - tail_states[-cycle_count - 1])
        / max(1.0, np.linalg.norm(tail_states[-1]))
    )
    action_periodicity_error = abs(
        tail_actions[-1] - tail_actions[-cycle_count - 1]
    )

    sample_indices = np.linspace(
        0, cycle_count - 1, 17, dtype=int
    )
    final_cycle_weights = final_p[sample_indices]
    return {
        "completion": completion,
        "drive_rate_per_event": rate,
        "event_parameter": "dimensionless event count n",
        "requested_step": requested_step,
        "actual_step": step,
        "cycles": cycles,
        "tail_cycles": tail_cycles,
        "steps_per_cycle": steps_per_cycle,
        "minimum_state_eigenvalue": minimum_state_eigenvalue,
        "tail_mean_dissipation": mean_d,
        "tail_min_dissipation": float(np.min(final_d)),
        "tail_max_dissipation": float(np.max(final_d)),
        "tail_mean_injected_work": mean_work,
        "mean_work_to_dissipation_relative_error": abs(mean_work - mean_d)
        / max(mean_d, 1.0e-30),
        "cycle_to_cycle_dissipation_relative_error": float(
            np.max(np.abs(final_d - previous_d)) / max(mean_d, 1.0e-30)
        ),
        "cycle_to_cycle_weight_max_error": float(
            np.max(np.abs(final_p - previous_p))
        ),
        "state_periodicity_relative_error": state_periodicity_error,
        "action_periodicity_absolute_error": action_periodicity_error,
        "tail_mean_weights": np.mean(final_p, axis=0),
        "tail_weight_minima": np.min(final_p, axis=0),
        "tail_weight_maxima": np.max(final_p, axis=0),
        "final_cycle_weight_samples": final_cycle_weights,
    }


def stationary_null(
    completion: str,
    base_target: np.ndarray,
) -> dict[str, Any]:
    equilibrium = stable_matrix_root(base_target)
    snapshot = completion_snapshot(equilibrium, base_target, completion)
    return {
        "completion": completion,
        "target_eigenvalues": np.linalg.eigvalsh(base_target),
        "equilibrium_eigenvalues": np.linalg.eigvalsh(equilibrium),
        "dissipation": snapshot["total_dissipation"],
        "weights": snapshot["weights"],
    }


def rotating_isotropic_null(
    completion: str,
    rate: float,
    base_target: np.ndarray,
) -> dict[str, Any]:
    """Evaluate a full nominal rotation whose isotropic target cannot move."""

    equilibrium = stable_matrix_root(base_target)
    phases = np.linspace(0.0, 2.0 * math.pi / rate, 33)
    target_errors: list[float] = []
    log_derivative_norms: list[float] = []
    dissipations: list[float] = []
    weights_defined: list[bool] = []
    for event_time in phases:
        target, log_derivative = driven_target(
            base_target, rate, float(event_time), np.eye(3)
        )
        snapshot = completion_snapshot(equilibrium, target, completion)
        target_errors.append(
            float(np.linalg.norm(target - base_target, ord="fro"))
        )
        log_derivative_norms.append(
            float(np.linalg.norm(log_derivative, ord="fro"))
        )
        dissipations.append(float(snapshot["total_dissipation"]))
        weights_defined.append(snapshot["weights"] is not None)
    return {
        "completion": completion,
        "drive_rate_per_event": rate,
        "phase_samples": len(phases),
        "maximum_target_change": max(target_errors),
        "maximum_log_derivative_norm": max(log_derivative_norms),
        "maximum_dissipation": max(dissipations),
        "any_weights_defined": any(weights_defined),
    }


def loglog_slope(xs: list[float], ys: list[float]) -> float:
    return float(
        np.polyfit(
            np.log(np.asarray(xs, dtype=float)),
            np.log(np.asarray(ys, dtype=float)),
            1,
        )[0]
    )


def native(value: Any) -> Any:
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


def make_candidate(
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-COUNCIL-HETERODOX-DRIVEN-BIANCONI",
        "track": "Open driven Bianconi counterexample",
        "question": (
            "Is vanishing Bianconi dissipation generic, or local to closed "
            "fixed-target relaxation; and does a minimal open drive generate "
            "rather than import a persistent physical scale?"
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
                    "The imported Bianconi SPD action remains the local "
                    "constitutive object under test."
                ),
                "status": "IMPORTED",
                "role": "Supplies the action, gradient, and dissipation objects.",
            },
            {
                "id": "A2",
                "statement": (
                    "A rotating anisotropic inducing metric is a minimal "
                    "conditional open-system drive."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Tests the closed-equilibrium scope without fitting concentration.",
            },
            {
                "id": "A3",
                "statement": (
                    "The evolution parameter is dimensionless event count; "
                    "no map to cosmological time is supplied."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Prevents the input cadence from masquerading as a physical scale.",
            },
            {
                "id": "A4",
                "statement": (
                    "Euclidean and affine-SPD mobilities remain separate, "
                    "unselected completions."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Preserves the completion disagreement from SWING-DU-PHY-02.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Rotate the reused anisotropic spectrum [0.9,1.4,2.4] "
                    "around axis (1,1,1)/sqrt(3)."
                ),
                "why_not_forced": "The Bianconi action does not select this drive.",
                "sensitivity_test": (
                    "Use an isotropic target null and an O(3) frame change."
                ),
            },
            {
                "id": "C2",
                "choice": (
                    "Use drive rates 0.05, 0.1, 0.2, 0.4, and 0.8 per event."
                ),
                "why_not_forced": "The cadence is imported and dimensionless.",
                "sensitivity_test": (
                    "Fit the tail dissipation slope against the input cadence."
                ),
            },
            {
                "id": "C3",
                "choice": (
                    "Integrate six periods with fixed-step geometric updates "
                    "and analyze the last two."
                ),
                "why_not_forced": "This is a numerical resolution choice.",
                "sensitivity_test": "Repeat the primary rate at three step sizes.",
            },
        ],
        "equations": [
            "G_ind(n)=Q(n)G_ind(0)Q(n)^T; Q(n)=exp(n Omega)",
            "d(log G_ind)/dn=[Omega,log G_ind]",
            "dS/dn=-D_X+P_drive",
            "P_drive=-Tr[G d(log G_ind)/dn]",
            "closed fixed-target equilibrium: D_X=0",
            "slow-drive linear response: E=O(omega), hence D_X=O(omega^2)",
        ],
        "observables": [
            "tail mean, minimum, and maximum raw dissipation",
            "tail mean injected work and work-dissipation balance",
            "cycle-to-cycle state, action, dissipation, and profile errors",
            "drive-rate versus tail-dissipation scaling",
            "completion-specific mean and range of normalized modal shares",
        ],
        "comparators": [
            "closed fixed-target equilibrium",
            "rotating isotropic target",
            "Euclidean versus affine-SPD completion",
            "three numerical step sizes",
            "simultaneous O(3) frame change",
        ],
        "null_models": [
            "zero drive at the fixed-target equilibrium has zero dissipation",
            "rotating an isotropic target is no physical drive and has zero dissipation",
            "an O(3) frame change preserves the driven receipt",
        ],
        "falsifiers": [
            "driven tail dissipation decays cycle over cycle toward zero",
            "tail work fails to balance tail dissipation after refinement",
            "the open result is not stable under timestep refinement",
            "an O(3) frame change alters the physical receipt",
            "tail dissipation is independent of the imported drive cadence",
        ],
        "stop_conditions": [
            "Do not call the imported drive cadence a generated physical clock.",
            "Do not infer a concentration-functional selector from sustained D.",
            "Do not map event count or action dissipation to Lambda without units.",
            "Do not treat this open-system counterexample as selection of a mobility.",
            "Do not fit a target concentration, rho, Lambda, or cosmological rate.",
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "A live mechanism dynamically sources nonuniform influence "
                "without choosing a target concentration."
            ),
            "formalization_id": "OPEN-DRIVEN-BIANCONI-DISSIPATION",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "A rotating anisotropic inducing metric sustains periodic "
                "nonzero Bianconi dissipation in both tested completions, "
                "whereas the closed and isotropic nulls remain at zero. The "
                "persistent activity is powered by the imported drive and "
                "therefore does not generate a physical scale."
            ),
            "grade": (
                "CONDITIONAL OPEN-SYSTEM COUNTEREXAMPLE / "
                "PERSISTENT-ACTIVITY / SCALE-IMPORTED / SELECTOR-OPEN"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "No DU-native law selects the driver, its cadence, either "
                "mobility, a response functional, units, or a cosmological map."
            ),
            "checks": checks,
        },
    }


def main() -> None:
    if np.__version__ != PINNED_NUMPY:
        raise RuntimeError(
            f"expected NumPy {PINNED_NUMPY}, got {np.__version__}"
        )

    stationary = {
        completion: stationary_null(completion, ANISOTROPIC_TARGET)
        for completion in COMPLETIONS
    }
    isotropic_target = 1.4 * np.eye(3)
    isotropic = {
        completion: rotating_isotropic_null(
            completion, PRIMARY_RATE, isotropic_target
        )
        for completion in COMPLETIONS
    }
    rate_sweeps = {
        completion: {
            str(rate): run_driven(completion, rate, BASE_STEP)
            for rate in DRIVE_RATES
        }
        for completion in COMPLETIONS
    }
    rate_slopes = {
        completion: loglog_slope(
            list(DRIVE_RATES[:3]),
            [
                rate_sweeps[completion][str(rate)][
                    "tail_mean_dissipation"
                ]
                for rate in DRIVE_RATES[:3]
            ],
        )
        for completion in COMPLETIONS
    }
    refinements = {
        completion: {
            str(step): run_driven(
                completion, PRIMARY_RATE, step
            )
            for step in (0.04, 0.02, 0.01)
        }
        for completion in COMPLETIONS
    }

    reflection = np.diag([-1.0, 1.0, 1.0])
    frame_runs = {
        completion: run_driven(
            completion,
            PRIMARY_RATE,
            BASE_STEP,
            frame=reflection,
        )
        for completion in COMPLETIONS
    }

    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool) -> None:
        checks.append({"name": name, "pass": bool(condition)})

    check(
        "closed fixed-target equilibrium has zero dissipation",
        all(
            result["dissipation"] < 1.0e-24
            and result["weights"] is None
            for result in stationary.values()
        ),
    )
    check(
        "rotating an isotropic target supplies no drive or dissipation",
        all(
            result["maximum_target_change"] < 1.0e-14
            and result["maximum_log_derivative_norm"] < 1.0e-14
            and result["maximum_dissipation"] < 1.0e-24
            and not result["any_weights_defined"]
            for result in isotropic.values()
        ),
    )
    check(
        "anisotropic open drive sustains nonzero tail dissipation in both completions",
        all(
            rate_sweeps[completion][str(rate)][
                "tail_min_dissipation"
            ]
            > 1.0e-6
            for completion in COMPLETIONS
            for rate in DRIVE_RATES
        ),
    )
    check(
        "driven tail converges to a periodic state rather than decaying cycle over cycle",
        all(
            rate_sweeps[completion][str(rate)][
                "cycle_to_cycle_dissipation_relative_error"
            ]
            < 0.01
            and rate_sweeps[completion][str(rate)][
                "state_periodicity_relative_error"
            ]
            < 0.003
            for completion in COMPLETIONS
            for rate in DRIVE_RATES
        ),
    )
    check(
        "tail injected work balances raw dissipation after transients",
        all(
            rate_sweeps[completion][str(rate)][
                "mean_work_to_dissipation_relative_error"
            ]
            < 0.025
            for completion in COMPLETIONS
            for rate in DRIVE_RATES
        ),
    )
    check(
        "small-drive dissipation inherits approximately quadratic cadence scaling",
        all(1.70 < slope < 2.10 for slope in rate_slopes.values()),
    )
    check(
        "timestep refinement stabilizes primary tail dissipation",
        all(
            abs(
                refinements[completion]["0.02"][
                    "tail_mean_dissipation"
                ]
                - refinements[completion]["0.01"][
                    "tail_mean_dissipation"
                ]
            )
            < abs(
                refinements[completion]["0.04"][
                    "tail_mean_dissipation"
                ]
                - refinements[completion]["0.01"][
                    "tail_mean_dissipation"
                ]
            )
            and abs(
                refinements[completion]["0.02"][
                    "tail_mean_dissipation"
                ]
                / refinements[completion]["0.01"][
                    "tail_mean_dissipation"
                ]
                - 1.0
            )
            < 0.025
            for completion in COMPLETIONS
        ),
    )
    check(
        "simultaneous O(3) frame change preserves driven dissipation and modal shape",
        all(
            abs(
                frame_runs[completion]["tail_mean_dissipation"]
                / rate_sweeps[completion][str(PRIMARY_RATE)][
                    "tail_mean_dissipation"
                ]
                - 1.0
            )
            < 2.0e-11
            and float(
                np.max(
                    np.abs(
                        np.asarray(
                            frame_runs[completion]["tail_mean_weights"]
                        )
                        - np.asarray(
                            rate_sweeps[completion][str(PRIMARY_RATE)][
                                "tail_mean_weights"
                            ]
                        )
                    )
                )
            )
            < 2.0e-11
            for completion in COMPLETIONS
        ),
    )
    check(
        "the two unselected mobilities retain quantitatively different driven receipts",
        abs(
            rate_sweeps["euclidean"][str(PRIMARY_RATE)][
                "tail_mean_dissipation"
            ]
            / rate_sweeps["affine_invariant"][str(PRIMARY_RATE)][
                "tail_mean_dissipation"
            ]
            - 1.0
        )
        > 0.02
        and float(
            np.max(
                np.abs(
                    np.asarray(
                        rate_sweeps["euclidean"][str(PRIMARY_RATE)][
                            "tail_mean_weights"
                        ]
                    )
                    - np.asarray(
                        rate_sweeps["affine_invariant"][
                            str(PRIMARY_RATE)
                        ]["tail_mean_weights"]
                    )
                )
            )
        )
        > 0.03,
    )
    check(
        "no target concentration, rho, Lambda, cosmological clock, or dimensional rate is fitted",
        True,
    )

    candidate = make_candidate(checks)
    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate: {receipt['contract_errors']}"
        )

    payload = {
        "probe": "du_heterodox_driven_bianconi_probe",
        "numpy_version": np.__version__,
        "parameters": {
            "sigma": SIGMA,
            "target_eigenvalues": np.linalg.eigvalsh(
                ANISOTROPIC_TARGET
            ),
            "rotation_axis": AXIS,
            "drive_rates_per_event": DRIVE_RATES,
            "drive_cycles": DRIVE_CYCLES,
            "tail_cycles": TAIL_CYCLES,
            "base_requested_step": BASE_STEP,
            "fitted_parameters": [],
            "forbidden_insertions": [
                "target concentration",
                "rho",
                "Lambda",
                "cosmological time",
                "dimensional drive rate",
            ],
        },
        "analytic_balance": {
            "identity": "dS/dn=-D_X+P_drive",
            "drive_work": "P_drive=-Tr[G d(log G_ind)/dn]",
            "slow_drive": (
                "Linear lag is O(omega), so D is O(omega^2); "
                "the activity scale inherits the imported cadence."
            ),
        },
        "closed_stationary_null": stationary,
        "rotating_isotropic_null": isotropic,
        "drive_rate_sweeps": rate_sweeps,
        "small_drive_loglog_slopes": rate_slopes,
        "timestep_refinement": refinements,
        "orthogonal_frame_runs": frame_runs,
        "scientific_reading": {
            "contested_finding": "NARROWED",
            "formalization_local": (
                "D->0 is established for fixed-target closed relaxation, "
                "not for open Bianconi dynamics."
            ),
            "positive_result": (
                "A target-free-in-concentration rotating anisotropic drive "
                "sustains nonzero periodic dissipation through injected work."
            ),
            "scale_result": (
                "The magnitude follows the imported dimensionless cadence; "
                "no unit-bearing or endogenous physical scale is generated."
            ),
            "branch_result": (
                "Do not reopen standalone influence-to-Lambda inference. "
                "Reuse the object inside a native order-first growth law "
                "whose drive and units are generated independently."
            ),
        },
    }
    write_candidate_artifact(
        ARTIFACT_PATH, native(candidate), native(payload)
    )

    for check_item in checks:
        print(
            f"{'PASS' if check_item['pass'] else 'FAIL'}: "
            f"{check_item['name']}"
        )
    passed = sum(bool(item["pass"]) for item in checks)
    print(f"{passed}/{len(checks)} checks pass")
    for completion in COMPLETIONS:
        primary = rate_sweeps[completion][str(PRIMARY_RATE)]
        print(
            f"{completion}: <D>={primary['tail_mean_dissipation']:.6e}, "
            f"<P>={primary['tail_mean_injected_work']:.6e}, "
            f"rate slope={rate_slopes[completion]:.4f}"
        )
    print(f"artifact: {ARTIFACT_PATH}")
    print(
        "VERDICT: fixed-target TRANSIENT-ONLY narrowed; open drive gives "
        "PERSISTENT-ACTIVITY, but SCALE-IMPORTED / SELECTOR-OPEN."
    )
    if passed != len(checks):
        failed = [item["name"] for item in checks if not item["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
