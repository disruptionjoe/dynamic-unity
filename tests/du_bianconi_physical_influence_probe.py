"""SWING-DU-PHY-02 Track A: Bianconi dissipation-share influence.

The imported Bianconi SPD action supplies a scalar descent rate only after a
mobility/gradient metric is chosen.  This probe constructs the modal
dissipation-share distribution for the two completions already tested in
``du_bianconi_completion_robustness_probe.py``:

    Euclidean:       A_E = grad_G S
                     D_E = tr(A_E^2)
                     p_i = eig_i(A_E)^2 / D_E

    affine-invariant A_AI = G^(1/2) (grad_G S) G^(1/2)
                     D_AI = tr(A_AI^2)
                     p_i = eig_i(A_AI)^2 / D_AI.

The shares are nonnegative, normalized, and invariant under simultaneous
orthogonal similarity of G and G_ind wherever D > 0.  The tested action is not
silently treated as invariant under arbitrary congruence.  At exact
stationarity D = 0, so the normalized shares are undefined; this probe records
``null`` rather than selecting a limiting distribution by hand.

The normalized shares are also degree zero in the completion operator:
rescaling A by c rescales D by c^2 but leaves p unchanged.  With modal
dimension fixed at three, p therefore carries neither an absolute magnitude
nor a growth law.  A persistent normalized shape cannot by itself establish a
persistent physical scale.

The output is conditional and local to this formalization.  It uses the shared
conditional-candidate harness, whose contract completeness is not scientific
endorsement.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)
from du_bianconi_completion_robustness_probe import (
    SEED as PREDECESSOR_SEED,
    SIGMA,
    action,
    euclidean_gradient,
    exp_symmetric,
    rotation_matrix,
    sqrt_spd,
    stable_matrix_root,
    sym,
)
from du_influence_redistribution_abduction_probe import concentration_metrics


EXPECTED_NUMPY_VERSION = "2.5.1"
INVARIANCE_SEED = 20260724
NUMERICAL_ZERO_D = 1.0e-24
FLOW_RESIDUAL_TOLERANCE = 6.0e-8
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_bianconi_physical_influence_probe_result.json"
)
COMPLETIONS = ("euclidean", "affine_invariant")
METRIC_KEYS = (
    "lambda_participation",
    "lambda_shannon_kl",
    "lambda_gini_lorenz",
)


def orthogonal_matrix(rng: np.random.Generator) -> np.ndarray:
    """Return a deterministic proper orthogonal matrix for the pinned RNG."""

    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0.0:
        q[:, 0] *= -1.0
    return q


def baseline_fixture() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Reproduce the exact noncommuting fixture from the predecessor probe."""

    rng = np.random.default_rng(PREDECESSOR_SEED)
    q_ind = orthogonal_matrix(rng)
    g_ind = sym(q_ind @ np.diag([0.9, 1.4, 2.4]) @ q_ind.T)
    q0 = rotation_matrix()
    g0 = sym(q0 @ np.diag([0.52, 1.65, 2.65]) @ q0.T)
    return g0, g_ind, q_ind


def completion_operator(
    g: np.ndarray, g_ind: np.ndarray, completion: str
) -> np.ndarray:
    """Return the symmetric operator whose squared modes sum to -dS/dt."""

    gradient = euclidean_gradient(g, g_ind)
    if completion == "euclidean":
        return gradient
    if completion == "affine_invariant":
        root = sqrt_spd(g)
        return sym(root @ gradient @ root)
    raise ValueError(f"unknown completion: {completion}")


def modal_profile(
    g: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
    *,
    time: float,
    step: int,
    label: str,
) -> dict[str, Any]:
    """Compute one raw modal decomposition and its three inherited readings."""

    operator = completion_operator(g, g_ind, completion)
    eigenvalues = np.linalg.eigvalsh(operator)
    contributions = np.square(eigenvalues)
    dissipation = float(np.trace(operator @ operator))
    reconstruction_error = abs(float(np.sum(contributions)) - dissipation)
    reconstruction_relative_error = reconstruction_error / max(1.0, dissipation)

    profile: dict[str, Any] = {
        "label": label,
        "completion": completion,
        "time": float(time),
        "step": int(step),
        "total_dissipation": dissipation,
        "modal_eigenvalues": eigenvalues.tolist(),
        "squared_modal_contributions": contributions.tolist(),
        "reconstruction_absolute_error": reconstruction_error,
        "reconstruction_relative_error": reconstruction_relative_error,
        "analytical_domain": "D > 0",
        "numerical_zero_threshold": NUMERICAL_ZERO_D,
    }
    if dissipation <= NUMERICAL_ZERO_D:
        profile.update(
            {
                "defined": False,
                "raw_normalized_weights": None,
                "metrics": None,
                "undefined_reason": (
                    "Total dissipation is numerically zero; normalizing would "
                    "manufacture a preferred 0/0 distribution."
                ),
            }
        )
        return profile

    weights = np.sort(contributions / dissipation)[::-1]
    profile.update(
        {
            "defined": True,
            "raw_normalized_weights": weights.tolist(),
            "metrics": concentration_metrics(weights.tolist()),
            "undefined_reason": None,
        }
    )
    return profile


def flow_step(
    g: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
    step_size: float,
) -> np.ndarray:
    """Take the completion's SPD-compatible first-order descent step."""

    gradient = euclidean_gradient(g, g_ind)
    if completion == "euclidean":
        return sym(g - step_size * gradient)
    if completion == "affine_invariant":
        root = sqrt_spd(g)
        natural_gradient = sym(root @ gradient @ root)
        return sym(root @ exp_symmetric(-step_size * natural_gradient) @ root)
    raise ValueError(f"unknown completion: {completion}")


def fixed_step_flow(
    g0: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
    *,
    step_size: float,
    final_time: float,
    sample_times: tuple[float, ...],
    label: str,
) -> dict[str, Any]:
    """Integrate at fixed step for the timestep-sensitivity comparison."""

    total_steps = int(round(final_time / step_size))
    if abs(total_steps * step_size - final_time) > 1.0e-12:
        raise ValueError("final_time must be an integer number of steps")
    sample_steps = {
        int(round(sample_time / step_size)): sample_time
        for sample_time in sample_times
    }
    if any(
        abs(index * step_size - sample_time) > 1.0e-12
        for index, sample_time in sample_steps.items()
    ):
        raise ValueError("sample times must lie on the timestep grid")

    g = g0.copy()
    actions = [action(g, g_ind)]
    minimum_eigenvalue = float(np.min(np.linalg.eigvalsh(g)))
    samples: list[dict[str, Any]] = []
    if 0 in sample_steps:
        samples.append(
            modal_profile(
                g,
                g_ind,
                completion,
                time=0.0,
                step=0,
                label=f"{label}:t=0",
            )
        )

    for index in range(1, total_steps + 1):
        candidate = flow_step(g, g_ind, completion, step_size)
        candidate_minimum = float(np.min(np.linalg.eigvalsh(candidate)))
        if candidate_minimum <= 0.0:
            raise RuntimeError(
                f"{completion} fixed step left the SPD cone at step {index}"
            )
        g = candidate
        minimum_eigenvalue = min(minimum_eigenvalue, candidate_minimum)
        actions.append(action(g, g_ind))
        if index in sample_steps:
            sample_time = sample_steps[index]
            samples.append(
                modal_profile(
                    g,
                    g_ind,
                    completion,
                    time=sample_time,
                    step=index,
                    label=f"{label}:t={sample_time:g}",
                )
            )

    action_changes = np.diff(np.asarray(actions))
    return {
        "completion": completion,
        "step_size": step_size,
        "final_time": final_time,
        "total_steps": total_steps,
        "action_initial": actions[0],
        "action_final": actions[-1],
        "maximum_action_increase": float(max(0.0, np.max(action_changes))),
        "minimum_state_eigenvalue": minimum_eigenvalue,
        "samples": samples,
    }


def armijo_profile_flow(
    g0: np.ndarray,
    g_ind: np.ndarray,
    completion: str,
) -> dict[str, Any]:
    """Follow one completion to numerical stationarity and retain raw profiles."""

    g = g0.copy()
    current_action = action(g, g_ind)
    initial_profile = modal_profile(
        g,
        g_ind,
        completion,
        time=0.0,
        step=0,
        label="baseline:initial",
    )
    initial_dissipation = float(initial_profile["total_dissipation"])
    ratio_targets = [1.0e-2, 1.0e-4, 1.0e-6, 1.0e-8, 1.0e-10, 1.0e-12]
    samples = [initial_profile]
    accumulated_time = 0.0
    accepted_steps: list[float] = []
    maximum_action_increase = 0.0

    for index in range(1, 4001):
        gradient = euclidean_gradient(g, g_ind)
        residual = float(np.linalg.norm(gradient, ord="fro"))
        if residual < FLOW_RESIDUAL_TOLERANCE:
            break

        if completion == "euclidean":
            directional_derivative = -(residual**2)
        elif completion == "affine_invariant":
            natural = completion_operator(g, g_ind, completion)
            directional_derivative = -float(np.trace(natural @ natural))
        else:
            raise ValueError(f"unknown completion: {completion}")

        trial = 0.25
        for _ in range(80):
            candidate = flow_step(g, g_ind, completion, trial)
            if float(np.min(np.linalg.eigvalsh(candidate))) <= 1.0e-10:
                trial *= 0.5
                continue
            candidate_action = action(candidate, g_ind)
            if (
                candidate_action
                <= current_action + 1.0e-4 * trial * directional_derivative
            ):
                break
            trial *= 0.5
        else:
            raise RuntimeError(f"{completion} Armijo line search failed")
        if trial < 1.0e-14:
            raise RuntimeError(f"{completion} Armijo line search stalled")

        maximum_action_increase = max(
            maximum_action_increase, candidate_action - current_action
        )
        g = candidate
        current_action = candidate_action
        accumulated_time += trial
        accepted_steps.append(trial)

        profile = modal_profile(
            g,
            g_ind,
            completion,
            time=accumulated_time,
            step=index,
            label=f"baseline:D-ratio-crossing-or-terminal:{index}",
        )
        ratio = float(profile["total_dissipation"]) / initial_dissipation
        while ratio_targets and ratio <= ratio_targets[0]:
            target = ratio_targets.pop(0)
            profile_at_target = dict(profile)
            profile_at_target["label"] = f"baseline:D/D0<={target:.0e}"
            profile_at_target["crossed_ratio_target"] = target
            samples.append(profile_at_target)
    else:
        raise RuntimeError(f"{completion} flow exceeded 4000 steps")

    terminal = modal_profile(
        g,
        g_ind,
        completion,
        time=accumulated_time,
        step=len(accepted_steps),
        label="baseline:terminal-before-exact-stationarity",
    )
    if samples[-1]["step"] != terminal["step"]:
        samples.append(terminal)

    return {
        "completion": completion,
        "action_initial": action(g0, g_ind),
        "action_final": current_action,
        "maximum_action_increase": max(0.0, maximum_action_increase),
        "steps": len(accepted_steps),
        "integrator_time": accumulated_time,
        "minimum_accepted_step": min(accepted_steps),
        "euclidean_gradient_residual": float(
            np.linalg.norm(euclidean_gradient(g, g_ind), ord="fro")
        ),
        "initial_dissipation": initial_dissipation,
        "terminal_dissipation": float(terminal["total_dissipation"]),
        "terminal_dissipation_ratio": (
            float(terminal["total_dissipation"]) / initial_dissipation
        ),
        "samples": samples,
    }


def first_variation_error(
    g: np.ndarray, g_ind: np.ndarray, completion: str
) -> dict[str, float]:
    """Verify that the named modal total is the action's initial descent rate."""

    epsilon = 1.0e-7
    initial_action = action(g, g_ind)
    candidate = flow_step(g, g_ind, completion, epsilon)
    observed_rate = -(action(candidate, g_ind) - initial_action) / epsilon
    predicted_rate = float(
        modal_profile(
            g,
            g_ind,
            completion,
            time=0.0,
            step=0,
            label="first-variation",
        )["total_dissipation"]
    )
    return {
        "step": epsilon,
        "observed_negative_action_derivative": observed_rate,
        "modal_total_dissipation": predicted_rate,
        "relative_error": abs(observed_rate - predicted_rate)
        / max(1.0, predicted_rate),
    }


def fixture_summary(g: np.ndarray, g_ind: np.ndarray) -> dict[str, Any]:
    return {
        "g_eigenvalues": np.linalg.eigvalsh(g).tolist(),
        "g_ind_eigenvalues": np.linalg.eigvalsh(g_ind).tolist(),
        "commutator_frobenius_norm": float(
            np.linalg.norm(g @ g_ind - g_ind @ g, ord="fro")
        ),
        "action": action(g, g_ind),
    }


def profile_weight_delta(
    left: dict[str, Any], right: dict[str, Any]
) -> float:
    if not left["defined"] or not right["defined"]:
        raise ValueError("cannot compare undefined profiles")
    return float(
        np.max(
            np.abs(
                np.asarray(left["raw_normalized_weights"])
                - np.asarray(right["raw_normalized_weights"])
            )
        )
    )


def profile_metric_differences(
    left: dict[str, Any], right: dict[str, Any]
) -> dict[str, float]:
    if not left["defined"] or not right["defined"]:
        raise ValueError("cannot compare undefined profiles")
    return {
        key: float(left["metrics"][key] - right["metrics"][key])
        for key in METRIC_KEYS
    }


def coordinate_tests(
    g0: np.ndarray, g_ind: np.ndarray
) -> dict[str, Any]:
    """Test O(3) invariance and explicitly probe the non-O(3) boundary."""

    originals = {
        completion: modal_profile(
            g0,
            g_ind,
            completion,
            time=0.0,
            step=0,
            label="coordinate:original",
        )
        for completion in COMPLETIONS
    }
    rng = np.random.default_rng(INVARIANCE_SEED)
    rotations: list[dict[str, Any]] = []
    maximum_weight_error = {completion: 0.0 for completion in COMPLETIONS}
    maximum_dissipation_relative_error = {
        completion: 0.0 for completion in COMPLETIONS
    }
    maximum_action_error = 0.0

    for index in range(6):
        q = orthogonal_matrix(rng)
        if index == 0:
            # Include the disconnected det=-1 component, not only SO(3).
            q[:, 0] *= -1.0
        transformed_g = sym(q @ g0 @ q.T)
        transformed_g_ind = sym(q @ g_ind @ q.T)
        profiles = {
            completion: modal_profile(
                transformed_g,
                transformed_g_ind,
                completion,
                time=0.0,
                step=0,
                label=f"coordinate:orthogonal-{index + 1}",
            )
            for completion in COMPLETIONS
        }
        for completion in COMPLETIONS:
            maximum_weight_error[completion] = max(
                maximum_weight_error[completion],
                profile_weight_delta(originals[completion], profiles[completion]),
            )
            original_d = float(originals[completion]["total_dissipation"])
            transformed_d = float(profiles[completion]["total_dissipation"])
            maximum_dissipation_relative_error[completion] = max(
                maximum_dissipation_relative_error[completion],
                abs(transformed_d - original_d) / max(1.0, original_d),
            )
        maximum_action_error = max(
            maximum_action_error,
            abs(action(transformed_g, transformed_g_ind) - action(g0, g_ind)),
        )
        rotations.append(
            {
                "rotation_index": index + 1,
                "determinant": float(np.linalg.det(q)),
                "orthogonality_error": float(
                    np.linalg.norm(q.T @ q - np.eye(3), ord="fro")
                ),
                "action": action(transformed_g, transformed_g_ind),
                "profiles": profiles,
            }
        )

    congruence = np.array(
        [
            [1.70, 0.30, 0.00],
            [0.00, 0.80, 0.20],
            [0.10, 0.00, 1.20],
        ]
    )
    congruent_g = sym(congruence @ g0 @ congruence.T)
    congruent_g_ind = sym(congruence @ g_ind @ congruence.T)
    congruent_profiles = {
        completion: modal_profile(
            congruent_g,
            congruent_g_ind,
            completion,
            time=0.0,
            step=0,
            label="coordinate:nonorthogonal-congruence",
        )
        for completion in COMPLETIONS
    }
    congruence_weight_changes = {
        completion: profile_weight_delta(
            originals[completion], congruent_profiles[completion]
        )
        for completion in COMPLETIONS
    }
    return {
        "declared_invariance_group": (
            "Simultaneous orthogonal similarity: "
            "(G,G_ind) -> (QGQ^T,QG_indQ^T), Q in O(3)."
        ),
        "not_claimed": (
            "Arbitrary nonorthogonal congruence or nonlinear "
            "reparameterization invariance."
        ),
        "original_profiles": originals,
        "orthogonal_similarity": {
            "seed": INVARIANCE_SEED,
            "determinant_coverage": (
                "One independently generated reflection (det=-1) and five "
                "independently generated proper rotations (det=+1)."
            ),
            "independent_rotations": rotations,
            "maximum_action_absolute_error": maximum_action_error,
            "maximum_weight_absolute_error": maximum_weight_error,
            "maximum_dissipation_relative_error": (
                maximum_dissipation_relative_error
            ),
        },
        "nonorthogonal_congruence_scope_control": {
            "matrix": congruence.tolist(),
            "determinant": float(np.linalg.det(congruence)),
            "condition_number": float(np.linalg.cond(congruence)),
            "action_before": action(g0, g_ind),
            "action_after": action(congruent_g, congruent_g_ind),
            "profiles_before": originals,
            "profiles_after": congruent_profiles,
            "maximum_weight_changes": congruence_weight_changes,
            "interpretation": (
                "The displayed formula is not invariant under this naive "
                "nonorthogonal congruence.  Track A therefore claims O(3) "
                "similarity invariance only; it does not relabel this scope "
                "failure as general coordinate invariance."
            ),
        },
    }


def sensitivity_tests(
    g0: np.ndarray, g_ind: np.ndarray, q_ind: np.ndarray
) -> dict[str, Any]:
    """Probe initial geometry, eigenspectrum, and numerical timestep choices."""

    g0_eigenvalues = np.linalg.eigvalsh(g0)
    commuting_g0 = sym(q_ind @ np.diag(g0_eigenvalues) @ q_ind.T)
    perturbed_g0 = sym(
        rotation_matrix() @ np.diag([0.68, 1.25, 3.10]) @ rotation_matrix().T
    )
    fixtures = {
        "baseline_noncommuting": g0,
        "commuting_same_eigenspectrum": commuting_g0,
        "perturbed_eigenspectrum_noncommuting": perturbed_g0,
    }
    geometry: dict[str, Any] = {}
    for name, fixture in fixtures.items():
        flows = {
            completion: fixed_step_flow(
                fixture,
                g_ind,
                completion,
                step_size=0.01,
                final_time=0.5,
                sample_times=(0.0, 0.5),
                label=f"sensitivity:{name}:{completion}",
            )
            for completion in COMPLETIONS
        }
        geometry[name] = {
            "fixture": fixture_summary(fixture, g_ind),
            "flows": flows,
        }

    timestep_runs: dict[str, Any] = {}
    for completion in COMPLETIONS:
        timestep_runs[completion] = {
            f"dt={step_size:g}": fixed_step_flow(
                g0,
                g_ind,
                completion,
                step_size=step_size,
                final_time=1.0,
                sample_times=(0.0, 0.5, 1.0),
                label=f"timestep:{completion}:dt={step_size:g}",
            )
            for step_size in (0.02, 0.01, 0.005)
        }

    return {
        "geometry_and_spectrum": geometry,
        "timestep_refinement": timestep_runs,
    }


def main() -> None:
    if np.__version__ != EXPECTED_NUMPY_VERSION:
        raise RuntimeError(
            f"expected NumPy {EXPECTED_NUMPY_VERSION}, got {np.__version__}"
        )

    g0, g_ind, q_ind = baseline_fixture()
    target = stable_matrix_root(g_ind)
    baseline_profiles = {
        completion: modal_profile(
            g0,
            g_ind,
            completion,
            time=0.0,
            step=0,
            label="baseline:shared-initial-state",
        )
        for completion in COMPLETIONS
    }
    first_variations = {
        completion: first_variation_error(g0, g_ind, completion)
        for completion in COMPLETIONS
    }
    long_flows = {
        completion: armijo_profile_flow(g0, g_ind, completion)
        for completion in COMPLETIONS
    }
    coordinates = coordinate_tests(g0, g_ind)
    sensitivity = sensitivity_tests(g0, g_ind, q_ind)

    isotropic_g = 1.6 * np.eye(3)
    isotropic_g_ind = np.eye(3)
    isotropic_profiles = {
        completion: modal_profile(
            isotropic_g,
            isotropic_g_ind,
            completion,
            time=0.0,
            step=0,
            label="isotropic-equal-modal-null",
        )
        for completion in COMPLETIONS
    }
    exact_stationary_profiles = {
        completion: modal_profile(
            target,
            g_ind,
            completion,
            time=float(long_flows[completion]["integrator_time"]),
            step=int(long_flows[completion]["steps"]) + 1,
            label="exact-stationary-metric",
        )
        for completion in COMPLETIONS
    }

    completion_weight_delta = profile_weight_delta(
        baseline_profiles["euclidean"],
        baseline_profiles["affine_invariant"],
    )
    completion_metric_differences = profile_metric_differences(
        baseline_profiles["affine_invariant"],
        baseline_profiles["euclidean"],
    )
    degree_zero_scale_control: dict[str, Any] = {}
    maximum_degree_zero_weight_error = 0.0
    maximum_degree_two_dissipation_error = 0.0
    for completion in COMPLETIONS:
        original = baseline_profiles[completion]
        original_weights = np.asarray(original["raw_normalized_weights"])
        contributions = np.asarray(original["squared_modal_contributions"])
        original_dissipation = float(original["total_dissipation"])
        scaled_cases = []
        for operator_scale in (0.1, 3.0, 10.0):
            scaled_contributions = operator_scale**2 * contributions
            scaled_dissipation = float(np.sum(scaled_contributions))
            scaled_weights = np.sort(
                scaled_contributions / scaled_dissipation
            )[::-1]
            maximum_degree_zero_weight_error = max(
                maximum_degree_zero_weight_error,
                float(np.max(np.abs(scaled_weights - original_weights))),
            )
            maximum_degree_two_dissipation_error = max(
                maximum_degree_two_dissipation_error,
                abs(
                    scaled_dissipation
                    - operator_scale**2 * original_dissipation
                )
                / max(1.0, operator_scale**2 * original_dissipation),
            )
            scaled_cases.append(
                {
                    "operator_scale": operator_scale,
                    "total_dissipation": scaled_dissipation,
                    "raw_normalized_weights": scaled_weights.tolist(),
                }
            )
        degree_zero_scale_control[completion] = {
            "modal_dimension": 3,
            "original_total_dissipation": original_dissipation,
            "original_raw_normalized_weights": original_weights.tolist(),
            "scaled_cases": scaled_cases,
        }

    geometry = sensitivity["geometry_and_spectrum"]
    geometry_weight_changes: dict[str, dict[str, float]] = {}
    for completion in COMPLETIONS:
        baseline_initial = geometry["baseline_noncommuting"]["flows"][completion][
            "samples"
        ][0]
        commuting_initial = geometry["commuting_same_eigenspectrum"]["flows"][
            completion
        ]["samples"][0]
        perturbed_initial = geometry[
            "perturbed_eigenspectrum_noncommuting"
        ]["flows"][completion]["samples"][0]
        geometry_weight_changes[completion] = {
            "noncommuting_vs_commuting_same_spectrum": profile_weight_delta(
                baseline_initial, commuting_initial
            ),
            "baseline_vs_perturbed_eigenspectrum": profile_weight_delta(
                baseline_initial, perturbed_initial
            ),
        }

    timestep_endpoint_deltas: dict[str, Any] = {}
    for completion in COMPLETIONS:
        runs = sensitivity["timestep_refinement"][completion]
        coarse = runs["dt=0.02"]["samples"][-1]
        medium = runs["dt=0.01"]["samples"][-1]
        fine = runs["dt=0.005"]["samples"][-1]
        timestep_endpoint_deltas[completion] = {
            "coarse_vs_fine_weight_max_abs": profile_weight_delta(coarse, fine),
            "medium_vs_fine_weight_max_abs": profile_weight_delta(medium, fine),
            "coarse_vs_fine_action_abs": abs(
                float(runs["dt=0.02"]["action_final"])
                - float(runs["dt=0.005"]["action_final"])
            ),
            "medium_vs_fine_action_abs": abs(
                float(runs["dt=0.01"]["action_final"])
                - float(runs["dt=0.005"]["action_final"])
            ),
        }

    defined_profiles: list[dict[str, Any]] = []

    def collect_profiles(value: Any) -> None:
        if isinstance(value, dict):
            if {
                "defined",
                "total_dissipation",
                "raw_normalized_weights",
            }.issubset(value):
                if value["defined"]:
                    defined_profiles.append(value)
                return
            for nested in value.values():
                collect_profiles(nested)
        elif isinstance(value, list):
            for nested in value:
                collect_profiles(nested)

    preliminary_payload = {
        "baseline_profiles": baseline_profiles,
        "long_flows": long_flows,
        "coordinate_tests": coordinates,
        "sensitivity": sensitivity,
        "isotropic_profiles": isotropic_profiles,
    }
    collect_profiles(preliminary_payload)
    all_nonnegative = all(
        min(profile["raw_normalized_weights"]) >= -1.0e-14
        for profile in defined_profiles
    )
    all_normalized = all(
        abs(sum(profile["raw_normalized_weights"]) - 1.0) < 2.0e-12
        for profile in defined_profiles
    )
    maximum_reconstruction_error = max(
        profile["reconstruction_relative_error"]
        for profile in defined_profiles
    )

    orthogonal = coordinates["orthogonal_similarity"]
    congruence = coordinates["nonorthogonal_congruence_scope_control"]
    all_fixed_flows = [
        flow
        for completion_runs in sensitivity["timestep_refinement"].values()
        for flow in completion_runs.values()
    ] + [
        fixture["flows"][completion]
        for fixture in sensitivity["geometry_and_spectrum"].values()
        for completion in COMPLETIONS
    ]
    fixed_descent = all(
        flow["maximum_action_increase"] < 2.0e-12
        and flow["minimum_state_eigenvalue"] > 0.0
        for flow in all_fixed_flows
    )

    uniform_target = [1.0 / 3.0] * 3
    isotropic_uniform = all(
        profile["defined"]
        and np.max(
            np.abs(
                np.asarray(profile["raw_normalized_weights"]) - uniform_target
            )
        )
        < 2.0e-12
        for profile in isotropic_profiles.values()
    )
    stationary_undefined = all(
        not profile["defined"]
        and float(profile["total_dissipation"]) <= NUMERICAL_ZERO_D
        for profile in exact_stationary_profiles.values()
    )
    long_flow_decay = all(
        float(flow["terminal_dissipation_ratio"]) < 1.0e-12
        and float(flow["maximum_action_increase"]) < 2.0e-12
        for flow in long_flows.values()
    )
    no_fitted_parameters = True

    checks = [
        {
            "name": (
                "all defined modal shares are nonnegative and normalized across "
                "baseline, perturbation, coordinate, null, and trajectory cases"
            ),
            "pass": all_nonnegative and all_normalized,
        },
        {
            "name": (
                "squared modal contributions reconstruct each completion's total "
                "dissipation"
            ),
            "pass": maximum_reconstruction_error < 2.0e-12,
        },
        {
            "name": "Euclidean modal total equals the action's initial descent rate",
            "pass": first_variations["euclidean"]["relative_error"] < 2.0e-6,
        },
        {
            "name": (
                "affine-invariant modal total equals the action's initial descent rate"
            ),
            "pass": (
                first_variations["affine_invariant"]["relative_error"] < 2.0e-6
            ),
        },
        {
            "name": (
                "six independent simultaneous O(3) changes, including a reflection, "
                "preserve action, dissipation, and raw modal shares"
            ),
            "pass": (
                orthogonal["maximum_action_absolute_error"] < 2.0e-12
                and all(
                    value < 2.0e-12
                    for value in orthogonal[
                        "maximum_weight_absolute_error"
                    ].values()
                )
                and all(
                    value < 2.0e-12
                    for value in orthogonal[
                        "maximum_dissipation_relative_error"
                    ].values()
                )
            ),
        },
        {
            "name": (
                "scope control exposes rather than assumes arbitrary-congruence "
                "invariance"
            ),
            "pass": (
                abs(congruence["action_after"] - congruence["action_before"])
                > 1.0e-3
                and max(congruence["maximum_weight_changes"].values()) > 1.0e-2
            ),
        },
        {
            "name": "associated fixed-step and Armijo trajectories descend the action",
            "pass": (
                fixed_descent
                and all(
                    flow["maximum_action_increase"] < 2.0e-12
                    for flow in long_flows.values()
                )
            ),
        },
        {
            "name": (
                "modal shares respond to commuting versus noncommuting initial geometry"
            ),
            "pass": all(
                changes["noncommuting_vs_commuting_same_spectrum"] > 1.0e-2
                for changes in geometry_weight_changes.values()
            ),
        },
        {
            "name": "modal shares respond to a legitimate initial eigenspectrum change",
            "pass": all(
                changes["baseline_vs_perturbed_eigenspectrum"] > 1.0e-2
                for changes in geometry_weight_changes.values()
            ),
        },
        {
            "name": (
                "timestep refinement stabilizes the one-time-unit raw modal profiles"
            ),
            "pass": all(
                deltas["medium_vs_fine_weight_max_abs"]
                < deltas["coarse_vs_fine_weight_max_abs"]
                and deltas["medium_vs_fine_weight_max_abs"] < 5.0e-3
                for deltas in timestep_endpoint_deltas.values()
            ),
        },
        {
            "name": (
                "Euclidean and affine completions disagree on the raw distribution "
                "and on all three concentration readings at the shared initial state"
            ),
            "pass": (
                completion_weight_delta > 0.1
                and all(
                    abs(value) > 0.05
                    for value in completion_metric_differences.values()
                )
            ),
        },
        {
            "name": (
                "normalized shares are degree zero while total dissipation carries "
                "the quadratic operator scale"
            ),
            "pass": (
                maximum_degree_zero_weight_error < 2.0e-12
                and maximum_degree_two_dissipation_error < 2.0e-12
            ),
        },
        {
            "name": "isotropic equal-modal null is uniform for both completions",
            "pass": isotropic_uniform,
        },
        {
            "name": (
                "total dissipation vanishes approaching the shared stationary metric"
            ),
            "pass": long_flow_decay,
        },
        {
            "name": (
                "exact stationary shares are left undefined rather than filled by hand"
            ),
            "pass": stationary_undefined,
        },
        {
            "name": (
                "no rho, Lambda, target distribution, or concentration amplitude is fitted"
            ),
            "pass": no_fitted_parameters,
        },
    ]

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "SWING-DU-PHY-02-TA",
        "track": "Bianconi dissipation spectrum",
        "question": (
            "Do the already-tested Bianconi dissipative completions supply a "
            "nonnegative normalized O(3)-invariant influence distribution, and "
            "is its concentration completion-robust and persistent at stationarity?"
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
                    "The imported Bianconi action on a real SPD block is the live "
                    "static object under test."
                ),
                "status": "IMPORTED",
                "role": "Supplies S(G,G_ind) and its Euclidean matrix gradient.",
            },
            {
                "id": "A2",
                "statement": (
                    "Euclidean and affine-invariant SPD gradient metrics are two "
                    "legitimate but unselected dissipative completions."
                ),
                "status": "STANDARD",
                "role": (
                    "Turns the action into two candidate flows and makes completion "
                    "dependence part of the result."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "The declared coordinate group is simultaneous orthogonal "
                    "similarity of G and G_ind."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Limits the invariant claim to the group under which the "
                    "matrix-log action is covariant."
                ),
            },
            {
                "id": "A4",
                "statement": (
                    "A dissipation-share distribution exists only where its total "
                    "dissipation D is strictly positive."
                ),
                "status": "STANDARD",
                "role": "Prevents a hand-selected distribution at the stationary 0/0 limit.",
            },
            {
                "id": "A5",
                "statement": (
                    "Participation, Shannon/KL, and Gini/Lorenz are inherited "
                    "comparison readings, not functionals selected by the action."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Keeps proxy comparison separate from physical selection.",
            },
            {
                "id": "A6",
                "statement": (
                    "Integrator time is the physical time only conditionally on "
                    "choosing that completion."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Prevents comparing two unselected mobilities as one unique clock.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Reuse sigma=0.2 and the exact 3x3 predecessor fixture seeded "
                    "by 20260723."
                ),
                "why_not_forced": "The Bianconi action does not select this finite fixture.",
                "sensitivity_test": (
                    "Compare commuting geometry at fixed spectrum and a changed "
                    "eigenspectrum without fitting either to a concentration target."
                ),
            },
            {
                "id": "C2",
                "choice": "Use Euclidean and affine-invariant gradient completions.",
                "why_not_forced": "The action fixes stationary points, not a mobility metric.",
                "sensitivity_test": (
                    "Compute separate raw shares, action descent, trajectories, and "
                    "all three concentration readings."
                ),
            },
            {
                "id": "C3",
                "choice": "Use fixed steps 0.02, 0.01, and 0.005 for numerical refinement.",
                "why_not_forced": "A numerical timestep is not physical input.",
                "sensitivity_test": (
                    "Require medium-to-fine endpoint convergence and preserve every "
                    "raw endpoint distribution."
                ),
            },
            {
                "id": "C4",
                "choice": (
                    "Treat D<=1e-24 as numerical zero while retaining the analytical "
                    "domain D>0."
                ),
                "why_not_forced": "Float64 cannot resolve an exact symbolic zero.",
                "sensitivity_test": (
                    "Report D and squared contributions; never normalize the exact "
                    "stationary specimen."
                ),
            },
            {
                "id": "C5",
                "choice": (
                    "Use six seeded orthogonal scope controls: one reflection "
                    "and five proper rotations."
                ),
                "why_not_forced": "Any orthogonal matrices would test the same covariance.",
                "sensitivity_test": (
                    "Generate them independently and compare action, D, and raw "
                    "weights to tight float64 tolerances."
                ),
            },
        ],
        "equations": [
            "S(G)=sigma log det G + Tr[G(log G-log G_ind)]-Tr G",
            "A_E=grad_G S=sigma G^{-1}+log G-log G_ind",
            "D_E=Tr(A_E^2)=-dS/dt for dot G=-A_E",
            "A_AI=G^(1/2) A_E G^(1/2)",
            "D_AI=Tr(A_AI^2)=-dS/dt for the affine-invariant gradient flow",
            "p_i^X=eig_i(A_X)^2/D_X on D_X>0",
            "p_i(c A_X)=p_i(A_X) while D_X(c A_X)=c^2 D_X(A_X)",
        ],
        "observables": [
            "raw sorted modal-share vector and total dissipation at labeled time/step",
            "action descent and first-variation reconstruction of -dS/dt",
            "participation, Shannon/KL, and Gini/Lorenz readings of each raw profile",
            "terminal dissipation ratio and exact-stationary defined/undefined state",
            "degree-zero share and degree-two total-dissipation scale control",
            "orthogonal-similarity errors and nonorthogonal-congruence scope control",
        ],
        "comparators": [
            "Euclidean versus affine-invariant gradient completion",
            "noncommuting versus commuting initial geometry at fixed spectrum",
            "baseline versus perturbed initial eigenspectrum",
            "coarse, medium, and fine numerical timesteps",
        ],
        "null_models": [
            "Isotropic G and G_ind with equal modal dissipation gives uniform shares.",
            "Simultaneous orthogonal rotation changes coordinates but not modal shares.",
            (
                "Nonorthogonal congruence is a scope control: this displayed action "
                "does not supply that broader invariance."
            ),
        ],
        "falsifiers": [
            "A squared modal contribution is negative or the shares fail to normalize.",
            "The modal squares fail to reconstruct the associated action descent rate.",
            "Simultaneous orthogonal similarity changes D or the sorted raw shares.",
            "Both legitimate completions produce the same raw trajectory and readings.",
            "A nonzero absolute dissipation survives at the stationary metric.",
        ],
        "stop_conditions": [
            "Stop if weights are chosen to reproduce a favored proxy ordering.",
            (
                "Do not call the distribution persistent when D vanishes and the "
                "stationary normalization is undefined."
            ),
            (
                "Do not average Euclidean and affine results or call either completion "
                "physically selected without an independent criterion."
            ),
            (
                "Do not promote O(3) similarity invariance to arbitrary congruence "
                "or nonlinear reparameterization invariance."
            ),
            (
                "Any failure is local to this Bianconi formalization; it does not "
                "close CONCEPT-DU-001."
            ),
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "Lambda reads a dynamically sourced deviation of effective influence "
                "from uniform, is baseline at uniform, and grows monotonically with concentration."
            ),
            "formalization_id": "BIANCONI-DISSIPATION-SHARE-SPECTRA",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "Both completions construct live nonnegative normalized O(3)-invariant "
                "dissipation-share objects on D>0, but they disagree strongly on the "
                "raw profile and all three concentration readings.  Their total "
                "dissipation vanishes and the exact stationary shares are undefined; "
                "the degree-zero shares at fixed modal dimension contain no absolute scale."
            ),
            "grade": (
                "OBJECT-FOUND / SELECTOR-OPEN / TRANSIENT-ONLY — relative modal "
                "concentration exists during relaxation, but no completion, functional, "
                "persistent absolute scale, growth law, rho, or Lambda is selected."
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "The coordinate claim is only O(3); only one action, two mobilities, "
                "and finite 3x3 specimens are tested.  A direction-dependent normalized "
                "limit can remain along a trajectory even as D vanishes, but it is not "
                "an influence distribution at the exact stationary point and, because "
                "p is degree zero at fixed modal dimension, it has no physical magnitude."
            ),
            "checks": checks,
        },
    }

    payload = {
        "provenance": {
            "numpy_version": np.__version__,
            "expected_numpy_version": EXPECTED_NUMPY_VERSION,
            "predecessor_fixture_seed": PREDECESSOR_SEED,
            "orthogonal_invariance_seed": INVARIANCE_SEED,
            "predecessor_probe": (
                "tests/du_bianconi_completion_robustness_probe.py"
            ),
            "contract": (
                "explorations/physical-influence-selector-wave-contract-2026-07-24.md"
            ),
        },
        "parameters": {
            "sigma": SIGMA,
            "matrix_dimension": 3,
            "analytical_distribution_domain": "D > 0",
            "numerical_zero_dissipation": NUMERICAL_ZERO_D,
            "flow_residual_tolerance": FLOW_RESIDUAL_TOLERANCE,
            "fitted_parameters": [],
            "forbidden_insertions": [
                "rho",
                "Lambda",
                "target distribution",
                "target concentration",
            ],
        },
        "baseline_fixture": fixture_summary(g0, g_ind),
        "baseline_profiles": baseline_profiles,
        "first_variation": first_variations,
        "completion_comparison": {
            "shared_state_weight_max_abs_difference": completion_weight_delta,
            "affine_minus_euclidean_metric_differences": (
                completion_metric_differences
            ),
            "raw_ordering_result": (
                "The affine profile is more concentrated than the Euclidean "
                "profile under all three inherited readings at the shared initial state."
            ),
            "selection_result": (
                "Quantitative agreement fails; no independent criterion in the "
                "action selects either completion or any one concentration functional."
            ),
        },
        "degree_zero_scale_control": {
            "statement": (
                "At fixed modal dimension n=3, p is degree zero in A and has no "
                "absolute units; only D retains the squared operator scale."
            ),
            "profiles": degree_zero_scale_control,
            "maximum_raw_weight_error": maximum_degree_zero_weight_error,
            "maximum_quadratic_dissipation_error": (
                maximum_degree_two_dissipation_error
            ),
            "physical_implication": (
                "A persistent normalized shape cannot establish a nonzero physical "
                "scale or an N-growth law without an independently meaningful D and units."
            ),
        },
        "coordinate_tests": coordinates,
        "sensitivity": {
            **sensitivity,
            "geometry_weight_changes": geometry_weight_changes,
            "timestep_endpoint_deltas": timestep_endpoint_deltas,
        },
        "stationary_behavior": {
            "stationary_metric_eigenvalues": np.linalg.eigvalsh(target).tolist(),
            "approach_trajectories": long_flows,
            "exact_stationary_profiles": exact_stationary_profiles,
            "classification": {
                "normalized_relative_concentration": (
                    "Defined along each finite-D relaxation and can retain a "
                    "completion/path-dependent nonuniform directional residue; the "
                    "terminal samples approach a point-mass shape."
                ),
                "absolute_influence": (
                    "Transient: D tends to zero for both completions."
                ),
                "exact_stationarity": (
                    "Undefined: p_i is 0/0 and is not filled by hand."
                ),
                "persistent_nonzero_scale": False,
                "degree_and_dimension": (
                    "p is degree zero and n=3 is fixed, so normalized persistence "
                    "has neither absolute magnitude nor growth scaling."
                ),
                "wave_disposition": "TRANSIENT-ONLY",
            },
        },
        "isotropic_equal_modal_null": {
            "fixture": fixture_summary(isotropic_g, isotropic_g_ind),
            "profiles": isotropic_profiles,
            "expected_raw_weights": uniform_target,
        },
        "validation_summary": {
            "defined_profile_count": len(defined_profiles),
            "all_nonnegative": all_nonnegative,
            "all_normalized": all_normalized,
            "maximum_reconstruction_relative_error": (
                maximum_reconstruction_error
            ),
            "no_fitted_parameters": no_fitted_parameters,
        },
        "disposition": {
            "track_a": "OBJECT-FOUND / SELECTOR-OPEN / TRANSIENT-ONLY",
            "physical_object": (
                "Completion-conditional modal shares of instantaneous action dissipation."
            ),
            "selector": (
                "Open: Euclidean and affine-invariant completions disagree, and "
                "the action privileges none of participation, Shannon/KL, or Gini/Lorenz."
            ),
            "persistence": (
                "The normalized shape becomes nearly point-like along both finite-D "
                "trajectories, but this degree-zero fixed-n residue supplies no "
                "absolute scale; D vanishes and p is undefined at exact stationarity."
            ),
            "concept_scope": (
                "Supports a live formalization during relaxation but neither banks "
                "nor falsifies CONCEPT-DU-001."
            ),
        },
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(f"incomplete candidate contract: {receipt['contract_errors']}")
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("SWING-DU-PHY-02 TRACK A — BIANCONI PHYSICAL INFLUENCE")
    print("=" * 76)
    for completion in COMPLETIONS:
        profile = baseline_profiles[completion]
        terminal = long_flows[completion]
        weights = profile["raw_normalized_weights"]
        print(
            f"{completion:18s} D0={profile['total_dissipation']:.6e} "
            f"p0={[round(value, 6) for value in weights]} "
            f"Dend/D0={terminal['terminal_dissipation_ratio']:.3e}"
        )
    print(
        "completion weight delta:"
        f" {completion_weight_delta:.6f}; "
        "stationary profiles undefined="
        f"{stationary_undefined}"
    )
    print(
        "orthogonal max errors:"
        f" action={orthogonal['maximum_action_absolute_error']:.3e}, "
        f" weights={max(orthogonal['maximum_weight_absolute_error'].values()):.3e}"
    )
    print("-" * 76)
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    passed = sum(bool(check["pass"]) for check in checks)
    print("-" * 76)
    print(f"{passed}/{len(checks)} scientific checks pass")
    print(f"contract: {receipt['contract_status']} (not a scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    print(
        "GRADE: OBJECT-FOUND / SELECTOR-OPEN / TRANSIENT-ONLY — "
        "completion-dependent during relaxation; D->0; stationary p undefined."
    )
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failures: {failed}")


if __name__ == "__main__":
    main()
