"""Comparative-abduction probe for CONCEPT-DU-001.

Track 2 of SWING-DU-SCI-01 tests three materially distinct concentration
functionals on the same influence simplex:

  * participation-ratio effective count (Hill q=2),
  * Shannon/KL effective count (Hill q=1), and
  * Gini/Lorenz concentration.

The invariant-level tests are deliberately weaker than an identity claim.
Every faithful proxy must recover the Sorkin baseline at uniform influence and
increase under majorization (unambiguous concentration).  Majorization is only
a partial order, so the probe also exhausts a finite grid to expose ranking
disagreement on incomparable distributions.  Such disagreement is evidence
against manufacturing an abductive winner without an independent physical
criterion; it is not a failure of the concept invariant.

Invariant (iv), mechanistic sourcing, is tested with a target-free
replicator--mixing flow

    dp_i/dt = s p_i (p_i - sum_j p_j^2) + mu (1/n - p_i).

The nonlinear term is positive frequency-dependent influence reinforcement;
the second term is uniform mixing.  The uniform state has transverse linear
growth rate s/n - mu, so rho := n mu / s = 1 is a predeclared *local*
bifurcation.  Below it, a finite fluctuation selects an identity but not a
target amplitude; above it, small perturbations decay.  The nonlinear flow can
still have a distant concentrated basin, so the probe reports that basin
dependence rather than globalizing the linear result.  The construction tests
existence and persistence only.  The physical value of rho and the
identification of p_i remain imported/open.

Pure Python standard library.  Deterministic.  Writes the shared conditional-
candidate contract artifact and exits nonzero if a predeclared check fails.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, Sequence

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    validate_candidate_contract,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_influence_redistribution_abduction_probe_result.json"
)
METRIC_KEYS = (
    "lambda_participation",
    "lambda_shannon_kl",
    "lambda_gini_lorenz",
)
TOL = 1.0e-11


def normalize(weights: Sequence[float]) -> list[float]:
    values = [float(value) for value in weights]
    if not values or any(value < -1.0e-13 for value in values):
        raise ValueError("influence weights must be nonempty and nonnegative")
    values = [max(0.0, value) for value in values]
    total = sum(values)
    if total <= 0.0:
        raise ValueError("influence weights must have positive total")
    return [value / total for value in values]


def concentration_metrics(weights: Sequence[float]) -> dict[str, float]:
    """Return three endpoint-matched Lambda proxies and their native objects.

    Participation and Shannon retain the concept register's native
    Lambda=1/sqrt(N_eff) map.  Gini has no canonical amplitude map, so it is
    affinely endpoint-matched to the same [1/sqrt(n), 1] interval.  Only its
    ordering, which is unchanged under any strictly increasing remap, is used
    in the comparative-abduction verdict.
    """

    p = normalize(weights)
    n = len(p)
    baseline = 1.0 / math.sqrt(n)

    sum_squares = sum(value * value for value in p)
    n_eff_participation = 1.0 / sum_squares
    lambda_participation = 1.0 / math.sqrt(n_eff_participation)

    entropy = -sum(value * math.log(value) for value in p if value > 0.0)
    kl_from_uniform = math.log(n) - entropy
    n_eff_shannon = math.exp(entropy)
    lambda_shannon = 1.0 / math.sqrt(n_eff_shannon)

    ascending = sorted(p)
    gini = (
        2.0
        * sum((index + 1) * value for index, value in enumerate(ascending))
        / n
        - (n + 1.0) / n
    )
    gini_max = (n - 1.0) / n if n > 1 else 1.0
    gini_normalized = gini / gini_max if n > 1 else 0.0
    lambda_gini = baseline + (1.0 - baseline) * gini_normalized

    return {
        "n": n,
        "baseline": baseline,
        "n_eff_participation": n_eff_participation,
        "lambda_participation": lambda_participation,
        "entropy": entropy,
        "kl_from_uniform": kl_from_uniform,
        "n_eff_shannon": n_eff_shannon,
        "lambda_shannon_kl": lambda_shannon,
        "gini": gini,
        "gini_normalized": gini_normalized,
        "lambda_gini_lorenz": lambda_gini,
        "concentration_participation": (
            (lambda_participation - baseline) / (1.0 - baseline)
            if n > 1
            else 0.0
        ),
        "concentration_shannon_kl": (
            (lambda_shannon - baseline) / (1.0 - baseline)
            if n > 1
            else 0.0
        ),
        "concentration_gini_lorenz": gini_normalized,
    }


def majorizes(left: Sequence[float], right: Sequence[float]) -> bool:
    """Whether left is at least as concentrated as right in majorization order."""

    a = sorted(normalize(left), reverse=True)
    b = sorted(normalize(right), reverse=True)
    if len(a) != len(b):
        raise ValueError("majorization requires equal dimensions")
    return all(
        sum(a[:cut]) >= sum(b[:cut]) - TOL for cut in range(1, len(a))
    )


def one_peak_distribution(n: int, peak: float) -> list[float]:
    if n < 2 or not 1.0 / n <= peak <= 1.0:
        raise ValueError("peak must run from the uniform share to one")
    remainder = (1.0 - peak) / (n - 1)
    return [peak] + [remainder] * (n - 1)


def integer_partitions(
    total: int, parts: int, maximum: int | None = None
) -> Iterable[tuple[int, ...]]:
    """Non-increasing integer partitions of total into exactly `parts` slots."""

    if parts == 1:
        if maximum is None or total <= maximum:
            yield (total,)
        return
    cap = total if maximum is None else min(total, maximum)
    for head in range(cap, -1, -1):
        for tail in integer_partitions(total - head, parts - 1, head):
            yield (head,) + tail


def sign(value: float, tolerance: float = 1.0e-12) -> int:
    if value > tolerance:
        return 1
    if value < -tolerance:
        return -1
    return 0


def metric_order(left: dict[str, float], right: dict[str, float]) -> dict[str, int]:
    return {
        key: sign(left[key] - right[key])
        for key in METRIC_KEYS
    }


def majorization_tests() -> dict:
    n = 8
    chain_peaks = (1.0 / n, 0.20, 0.35, 0.55, 0.80, 1.0)
    chain = [one_peak_distribution(n, peak) for peak in chain_peaks]
    chain_metrics = [concentration_metrics(profile) for profile in chain]

    chain_majorization = all(
        majorizes(chain[index + 1], chain[index])
        for index in range(len(chain) - 1)
    )
    chain_monotonic = {
        key: all(
            chain_metrics[index + 1][key] > chain_metrics[index][key] + TOL
            for index in range(len(chain_metrics) - 1)
        )
        for key in METRIC_KEYS
    }

    uniform = concentration_metrics([1.0] * n)
    point = concentration_metrics([1.0] + [0.0] * (n - 1))
    endpoint_checks = {
        key: {
            "uniform": uniform[key],
            "uniform_target": uniform["baseline"],
            "uniform_pass": abs(uniform[key] - uniform["baseline"]) < TOL,
            "point_mass": point[key],
            "point_mass_target": 1.0,
            "point_mass_pass": abs(point[key] - 1.0) < TOL,
        }
        for key in METRIC_KEYS
    }

    # Exhaust a permutation-quotiented rational grid.  This is stronger than
    # showing one selected chain and keeps the incomparable-case finding from
    # depending on a hand-picked pair.
    grid_total = 40
    grid_dimension = 4
    partitions = list(integer_partitions(grid_total, grid_dimension))
    profiles = [
        [part / grid_total for part in partition]
        for partition in partitions
    ]
    bundles = [concentration_metrics(profile) for profile in profiles]

    comparable_pairs = 0
    incomparable_pairs = 0
    majorization_violations = {key: 0 for key in METRIC_KEYS}
    ranking_disagreement_pairs = 0
    pairwise_disagreements = {
        "participation_vs_shannon_kl": 0,
        "participation_vs_gini_lorenz": 0,
        "shannon_kl_vs_gini_lorenz": 0,
    }

    for left_index, left in enumerate(profiles):
        for right_index in range(left_index + 1, len(profiles)):
            right = profiles[right_index]
            left_majorizes = majorizes(left, right)
            right_majorizes = majorizes(right, left)
            if left_majorizes or right_majorizes:
                comparable_pairs += 1
                concentrated_index = left_index if left_majorizes else right_index
                diffuse_index = right_index if left_majorizes else left_index
                for key in METRIC_KEYS:
                    if (
                        bundles[concentrated_index][key]
                        < bundles[diffuse_index][key] - TOL
                    ):
                        majorization_violations[key] += 1
                continue

            incomparable_pairs += 1
            orders = metric_order(bundles[left_index], bundles[right_index])
            nonzero_orders = {order for order in orders.values() if order != 0}
            if 1 in nonzero_orders and -1 in nonzero_orders:
                ranking_disagreement_pairs += 1
            if (
                orders["lambda_participation"]
                * orders["lambda_shannon_kl"]
                < 0
            ):
                pairwise_disagreements["participation_vs_shannon_kl"] += 1
            if (
                orders["lambda_participation"]
                * orders["lambda_gini_lorenz"]
                < 0
            ):
                pairwise_disagreements["participation_vs_gini_lorenz"] += 1
            if (
                orders["lambda_shannon_kl"]
                * orders["lambda_gini_lorenz"]
                < 0
            ):
                pairwise_disagreements["shannon_kl_vs_gini_lorenz"] += 1

    exemplar_left_counts = (37, 1, 1, 1)
    exemplar_right_counts = (36, 4, 0, 0)
    exemplar_left = [value / grid_total for value in exemplar_left_counts]
    exemplar_right = [value / grid_total for value in exemplar_right_counts]
    exemplar_left_metrics = concentration_metrics(exemplar_left)
    exemplar_right_metrics = concentration_metrics(exemplar_right)
    exemplar_orders = metric_order(
        exemplar_left_metrics, exemplar_right_metrics
    )
    exemplar_cumulative = {
        "left": [
            sum(sorted(exemplar_left, reverse=True)[:cut])
            for cut in range(1, grid_dimension)
        ],
        "right": [
            sum(sorted(exemplar_right, reverse=True)[:cut])
            for cut in range(1, grid_dimension)
        ],
    }

    return {
        "endpoints": endpoint_checks,
        "majorization_chain": {
            "dimension": n,
            "peaks": list(chain_peaks),
            "profiles": chain,
            "metrics": chain_metrics,
            "chain_is_majorization_ordered": chain_majorization,
            "strictly_monotone": chain_monotonic,
        },
        "exhaustive_grid": {
            "dimension": grid_dimension,
            "integer_total": grid_total,
            "permutation_quotiented_profiles": len(profiles),
            "comparable_pairs": comparable_pairs,
            "incomparable_pairs": incomparable_pairs,
            "majorization_violations": majorization_violations,
            "ranking_disagreement_pairs": ranking_disagreement_pairs,
            "ranking_disagreement_fraction_of_incomparable": (
                ranking_disagreement_pairs / incomparable_pairs
            ),
            "pairwise_disagreements": pairwise_disagreements,
        },
        "incomparable_exemplar": {
            "left_counts": list(exemplar_left_counts),
            "right_counts": list(exemplar_right_counts),
            "left": exemplar_left,
            "right": exemplar_right,
            "left_cumulative": exemplar_cumulative["left"],
            "right_cumulative": exemplar_cumulative["right"],
            "left_majorizes_right": majorizes(
                exemplar_left, exemplar_right
            ),
            "right_majorizes_left": majorizes(
                exemplar_right, exemplar_left
            ),
            "left_metrics": {
                key: exemplar_left_metrics[key] for key in METRIC_KEYS
            },
            "right_metrics": {
                key: exemplar_right_metrics[key] for key in METRIC_KEYS
            },
            "orders_left_minus_right": exemplar_orders,
            "reading": (
                "The first cumulative sum favors the left profile and the "
                "second favors the right, so majorization is silent. "
                "Participation ranks left more concentrated; Shannon/KL and "
                "Gini/Lorenz rank right more concentrated. No invariant-level "
                "contradiction follows."
            ),
        },
    }


def influence_field(
    weights: Sequence[float], reinforcement: float, mixing: float
) -> list[float]:
    p = normalize(weights)
    n = len(p)
    second_moment = sum(value * value for value in p)
    uniform = 1.0 / n
    return [
        reinforcement * value * (value - second_moment)
        + mixing * (uniform - value)
        for value in p
    ]


def rk4_step(
    weights: Sequence[float],
    reinforcement: float,
    mixing: float,
    dt: float,
) -> list[float]:
    p = list(weights)

    def shifted(
        base: Sequence[float], direction: Sequence[float], scale: float
    ) -> list[float]:
        return [
            value + scale * delta
            for value, delta in zip(base, direction)
        ]

    k1 = influence_field(p, reinforcement, mixing)
    k2 = influence_field(
        shifted(p, k1, 0.5 * dt), reinforcement, mixing
    )
    k3 = influence_field(
        shifted(p, k2, 0.5 * dt), reinforcement, mixing
    )
    k4 = influence_field(shifted(p, k3, dt), reinforcement, mixing)
    updated = [
        value
        + dt * (d1 + 2.0 * d2 + 2.0 * d3 + d4) / 6.0
        for value, d1, d2, d3, d4 in zip(p, k1, k2, k3, k4)
    ]
    if min(updated) < -1.0e-10:
        raise ArithmeticError("RK4 step left the probability simplex")
    return normalize([max(0.0, value) for value in updated])


def integrate(
    initial: Sequence[float],
    reinforcement: float,
    mixing: float,
    total_time: float,
    dt: float,
    sample_interval: float = 10.0,
) -> tuple[list[float], list[dict]]:
    p = normalize(initial)
    steps = round(total_time / dt)
    sample_every = max(1, round(sample_interval / dt))
    trajectory = [
        {
            "time": 0.0,
            "weights": p,
            "metrics": concentration_metrics(p),
        }
    ]
    for step_index in range(1, steps + 1):
        p = rk4_step(p, reinforcement, mixing, dt)
        if step_index % sample_every == 0 or step_index == steps:
            trajectory.append(
                {
                    "time": step_index * dt,
                    "weights": p,
                    "metrics": concentration_metrics(p),
                }
            )
    return p, trajectory


def perturbed_uniform(n: int, winner: int, epsilon: float) -> list[float]:
    if not 0 <= winner < n:
        raise ValueError("winner index out of range")
    if not 0.0 < epsilon < 1.0 / n:
        raise ValueError("epsilon must be a small positive simplex perturbation")
    p = [1.0 / n - epsilon / (n - 1)] * n
    p[winner] = 1.0 / n + epsilon
    return p


def perturbation_norm(weights: Sequence[float]) -> float:
    p = normalize(weights)
    uniform = 1.0 / len(p)
    return math.sqrt(sum((value - uniform) ** 2 for value in p))


def growth_rate_specimen(n: int, rho: float) -> dict:
    reinforcement = 1.0
    mixing = rho * reinforcement / n
    initial = perturbed_uniform(n, winner=0, epsilon=1.0e-8)
    duration = 30.0
    final, _ = integrate(
        initial,
        reinforcement,
        mixing,
        total_time=duration,
        dt=0.02,
        sample_interval=duration,
    )
    measured = math.log(
        perturbation_norm(final) / perturbation_norm(initial)
    ) / duration
    predicted = reinforcement / n - mixing
    return {
        "n": n,
        "rho": rho,
        "mixing": mixing,
        "predicted_transverse_rate": predicted,
        "measured_transverse_rate": measured,
        "relative_error": abs(measured - predicted) / abs(predicted),
    }


def dynamics_tests() -> dict:
    n = 8
    reinforcement = 1.0
    rho = 0.64
    mixing = rho * reinforcement / n
    primary_initial = perturbed_uniform(n, winner=0, epsilon=1.0e-4)
    primary_final, primary_trajectory = integrate(
        primary_initial,
        reinforcement,
        mixing,
        total_time=800.0,
        dt=0.05,
    )
    primary_metrics = concentration_metrics(primary_final)
    baseline = primary_metrics["baseline"]
    field_residual = max(
        abs(value)
        for value in influence_field(
            primary_final, reinforcement, mixing
        )
    )

    trajectory_monotonic = {
        key: all(
            later["metrics"][key] >= earlier["metrics"][key] - TOL
            for earlier, later in zip(
                primary_trajectory, primary_trajectory[1:]
            )
        )
        for key in METRIC_KEYS
    }

    held_final, _ = integrate(
        primary_final,
        reinforcement,
        mixing,
        total_time=200.0,
        dt=0.05,
        sample_interval=200.0,
    )
    held_metrics = concentration_metrics(held_final)
    hold_drift = max(
        abs(held_metrics[key] - primary_metrics[key])
        for key in METRIC_KEYS
    )

    perturbation_sweep = {}
    for epsilon in (1.0e-6, 1.0e-4, 1.0e-2):
        final, _ = integrate(
            perturbed_uniform(n, winner=0, epsilon=epsilon),
            reinforcement,
            mixing,
            total_time=800.0,
            dt=0.05,
            sample_interval=800.0,
        )
        perturbation_sweep[f"{epsilon:.0e}"] = {
            "final_weights": final,
            "final_metrics": concentration_metrics(final),
        }
    perturbation_spread = {
        key: max(
            specimen["final_metrics"][key]
            for specimen in perturbation_sweep.values()
        )
        - min(
            specimen["final_metrics"][key]
            for specimen in perturbation_sweep.values()
        )
        for key in METRIC_KEYS
    }

    winner_sweep = {}
    for winner in (0, 3, 7):
        final, _ = integrate(
            perturbed_uniform(n, winner=winner, epsilon=1.0e-4),
            reinforcement,
            mixing,
            total_time=800.0,
            dt=0.05,
            sample_interval=800.0,
        )
        winner_sweep[str(winner)] = {
            "winning_index": max(range(n), key=final.__getitem__),
            "sorted_final_weights": sorted(final, reverse=True),
            "final_metrics": concentration_metrics(final),
        }
    winner_metric_spread = {
        key: max(
            specimen["final_metrics"][key]
            for specimen in winner_sweep.values()
        )
        - min(
            specimen["final_metrics"][key]
            for specimen in winner_sweep.values()
        )
        for key in METRIC_KEYS
    }

    no_reinforcement_final, _ = integrate(
        primary_final,
        reinforcement=0.0,
        mixing=mixing,
        total_time=400.0,
        dt=0.05,
        sample_interval=400.0,
    )
    no_reinforcement_metrics = concentration_metrics(
        no_reinforcement_final
    )

    below_growth = growth_rate_specimen(n=n, rho=rho)
    above_growth = growth_rate_specimen(n=n, rho=1.28)

    phase_sweep = {}
    for dimension in (4, 8, 16):
        dimension_results = {}
        for phase_ratio in (0.32, 0.64, 0.80, 1.28, 1.60):
            phase_mixing = phase_ratio / dimension
            final, _ = integrate(
                perturbed_uniform(
                    dimension, winner=0, epsilon=1.0e-4
                ),
                reinforcement=1.0,
                mixing=phase_mixing,
                total_time=1200.0,
                dt=0.05,
                sample_interval=1200.0,
            )
            metrics = concentration_metrics(final)
            phase_key = f"{phase_ratio:.2f}"
            dimension_results[phase_key] = {
                "rho": phase_ratio,
                "mixing": phase_mixing,
                "final_max_weight": max(final),
                "final_metrics": metrics,
                "field_residual": max(
                    abs(value)
                    for value in influence_field(
                        final, 1.0, phase_mixing
                    )
                ),
            }
        phase_sweep[str(dimension)] = dimension_results

    phase_classification_pass = all(
        (
            specimen["final_metrics"]["lambda_participation"]
            > specimen["final_metrics"]["baseline"] + 0.10
            if specimen["rho"] < 1.0
            else abs(
                specimen["final_metrics"]["lambda_participation"]
                - specimen["final_metrics"]["baseline"]
            )
            < 1.0e-8
        )
        for dimension_results in phase_sweep.values()
        for specimen in dimension_results.values()
    )

    # rho=1 is a local threshold. Expose the nonlinear basin structure by
    # starting above it from the already-concentrated fixed point, then use a
    # much stronger mixing value as a global control for this specimen.
    bistable_rho = 1.28
    bistable_final, _ = integrate(
        primary_final,
        reinforcement=1.0,
        mixing=bistable_rho / n,
        total_time=1200.0,
        dt=0.05,
        sample_interval=1200.0,
    )
    bistable_metrics = concentration_metrics(bistable_final)
    strong_mixing_rho = 3.0
    strong_mixing_final, _ = integrate(
        primary_final,
        reinforcement=1.0,
        mixing=strong_mixing_rho / n,
        total_time=1200.0,
        dt=0.05,
        sample_interval=1200.0,
    )
    strong_mixing_metrics = concentration_metrics(strong_mixing_final)

    refined_final, _ = integrate(
        primary_initial,
        reinforcement,
        mixing,
        total_time=800.0,
        dt=0.025,
        sample_interval=800.0,
    )
    refined_metrics = concentration_metrics(refined_final)
    resolution_difference = max(
        abs(refined_metrics[key] - primary_metrics[key])
        for key in METRIC_KEYS
    )

    return {
        "equation": (
            "dp_i/dt = s p_i(p_i - sum_j p_j^2) "
            "+ mu(1/n - p_i)"
        ),
        "target_concentration_term_present": False,
        "phase_ratio": "rho = n mu / s",
        "analytic_uniform_stability": {
            "transverse_rate": "s/n - mu = (s/n)(1-rho)",
            "bifurcation": "rho = 1",
        },
        "primary_run": {
            "n": n,
            "reinforcement_s": reinforcement,
            "mixing_mu": mixing,
            "rho": rho,
            "initial_weights": primary_initial,
            "final_weights": primary_final,
            "initial_metrics": concentration_metrics(primary_initial),
            "final_metrics": primary_metrics,
            "field_residual": field_residual,
            "trajectory_monotonic": trajectory_monotonic,
            "sampled_trajectory": primary_trajectory,
            "hold_time": 200.0,
            "hold_metric_drift": hold_drift,
        },
        "linear_stability_specimens": {
            "below_threshold": below_growth,
            "above_threshold": above_growth,
        },
        "initial_perturbation_sensitivity": {
            "runs": perturbation_sweep,
            "metric_spread": perturbation_spread,
            "reading": (
                "The perturbation selects a branch but its amplitude does not "
                "set the final concentration across four decades."
            ),
        },
        "winner_identity_sensitivity": {
            "runs": winner_sweep,
            "metric_spread": winner_metric_spread,
            "reading": (
                "Changing which coordinate receives the fluctuation changes "
                "identity, not the permutation-invariant concentration."
            ),
        },
        "no_reinforcement_null": {
            "initial_weights": primary_final,
            "final_weights": no_reinforcement_final,
            "final_metrics": no_reinforcement_metrics,
            "returns_to_uniform": all(
                abs(no_reinforcement_metrics[key] - baseline) < 1.0e-8
                for key in METRIC_KEYS
            ),
        },
        "phase_and_dimension_sensitivity": {
            "runs": phase_sweep,
            "classification_matches_rho_threshold": phase_classification_pass,
            "reading": (
                "From the same near-uniform perturbation, concentration "
                "emerges for rho<1 across n=4,8,16 while rho>1 returns locally "
                "to uniform. Its numerical amplitude varies with rho and n, "
                "so no physical value is selected by this construction."
            ),
            "local_threshold_only": True,
            "nonlinear_basin_diagnostic": {
                "rho": bistable_rho,
                "start": "primary concentrated fixed point",
                "final_metrics": bistable_metrics,
                "concentrated_basin_persists": (
                    bistable_metrics["lambda_participation"]
                    > bistable_metrics["baseline"] + 0.10
                ),
                "reading": (
                    "At rho=1.28 the uniform state is locally stable, but a "
                    "distant concentrated initial state remains in a "
                    "concentrated basin. Therefore rho=1 is not claimed as a "
                    "global uniqueness boundary."
                ),
            },
            "strong_mixing_control": {
                "rho": strong_mixing_rho,
                "start": "primary concentrated fixed point",
                "final_metrics": strong_mixing_metrics,
                "returns_to_uniform": all(
                    abs(strong_mixing_metrics[key] - baseline) < 1.0e-8
                    for key in METRIC_KEYS
                ),
            },
        },
        "integration_resolution": {
            "dt_primary": 0.05,
            "dt_refined": 0.025,
            "max_metric_difference": resolution_difference,
        },
    }


def build_checks(majorization: dict, dynamics: dict) -> list[dict]:
    endpoints = majorization["endpoints"]
    chain = majorization["majorization_chain"]
    grid = majorization["exhaustive_grid"]
    exemplar = majorization["incomparable_exemplar"]
    primary = dynamics["primary_run"]
    stability = dynamics["linear_stability_specimens"]
    perturbation = dynamics["initial_perturbation_sensitivity"]
    identity = dynamics["winner_identity_sensitivity"]

    return [
        {
            "name": "All three proxies recover the 1/sqrt(n) uniform baseline",
            "pass": all(
                endpoint["uniform_pass"] for endpoint in endpoints.values()
            ),
        },
        {
            "name": "All three proxies reach one at a point mass",
            "pass": all(
                endpoint["point_mass_pass"] for endpoint in endpoints.values()
            ),
        },
        {
            "name": "The declared one-peak chain is majorization ordered",
            "pass": chain["chain_is_majorization_ordered"],
        },
        {
            "name": "Every proxy increases strictly on the majorization chain",
            "pass": all(chain["strictly_monotone"].values()),
        },
        {
            "name": "The exhaustive rational grid has zero majorization violations",
            "pass": all(
                count == 0
                for count in grid["majorization_violations"].values()
            ),
        },
        {
            "name": "Incomparable profiles exhibit material proxy-ranking disagreement",
            "pass": (
                grid["incomparable_pairs"] > 0
                and grid["ranking_disagreement_pairs"] > 0
                and grid[
                    "ranking_disagreement_fraction_of_incomparable"
                ]
                > 0.10
            ),
        },
        {
            "name": "The named exemplar is majorization-incomparable",
            "pass": not exemplar["left_majorizes_right"]
            and not exemplar["right_majorizes_left"],
        },
        {
            "name": "The exemplar reverses participation versus Shannon/KL and Gini/Lorenz",
            "pass": (
                exemplar["orders_left_minus_right"][
                    "lambda_participation"
                ]
                == 1
                and exemplar["orders_left_minus_right"][
                    "lambda_shannon_kl"
                ]
                == -1
                and exemplar["orders_left_minus_right"][
                    "lambda_gini_lorenz"
                ]
                == -1
            ),
        },
        {
            "name": "Below-threshold perturbations grow at the analytic transverse rate",
            "pass": stability["below_threshold"]["relative_error"] < 0.01
            and stability["below_threshold"][
                "measured_transverse_rate"
            ]
            > 0.0,
        },
        {
            "name": "Above-threshold perturbations decay at the analytic transverse rate",
            "pass": stability["above_threshold"]["relative_error"] < 0.01
            and stability["above_threshold"][
                "measured_transverse_rate"
            ]
            < 0.0,
        },
        {
            "name": "All proxies grow monotonically on the primary mechanistic path",
            "pass": all(primary["trajectory_monotonic"].values()),
        },
        {
            "name": "The nonzero concentrated fixed point persists without a target term",
            "pass": (
                not dynamics["target_concentration_term_present"]
                and primary["final_metrics"]["lambda_participation"]
                > primary["final_metrics"]["baseline"] + 0.10
                and primary["field_residual"] < 1.0e-10
                and primary["hold_metric_drift"] < 1.0e-10
            ),
        },
        {
            "name": "Final concentration is insensitive to perturbation amplitude",
            "pass": all(
                spread < 1.0e-9
                for spread in perturbation["metric_spread"].values()
            ),
        },
        {
            "name": "Winner identity changes without changing concentration amplitude",
            "pass": (
                {
                    run["winning_index"]
                    for run in identity["runs"].values()
                }
                == {0, 3, 7}
                and all(
                    spread < 1.0e-9
                    for spread in identity["metric_spread"].values()
                )
            ),
        },
        {
            "name": "Removing reinforcement returns the concentrated state to uniform",
            "pass": dynamics["no_reinforcement_null"][
                "returns_to_uniform"
            ],
        },
        {
            "name": "Near-uniform phase and dimension sensitivity follow the local rho=1 threshold",
            "pass": dynamics["phase_and_dimension_sensitivity"][
                "classification_matches_rho_threshold"
            ],
        },
        {
            "name": "Strong mixing erases even a concentrated initial state",
            "pass": dynamics["phase_and_dimension_sensitivity"][
                "strong_mixing_control"
            ]["returns_to_uniform"],
        },
        {
            "name": "The mechanistic result is stable under halving the RK4 step",
            "pass": dynamics["integration_resolution"][
                "max_metric_difference"
            ]
            < 1.0e-9,
        },
        {
            "name": "No abductive winner is assigned without an independent physical criterion",
            "pass": grid["ranking_disagreement_pairs"] > 0,
        },
    ]


def candidate_contract(checks: list[dict]) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-SCI-01-T2-INFLUENCE-ABDUCTION",
        "track": "SWING-DU-SCI-01 Track 2 / Lane 2.2",
        "question": (
            "Do participation-ratio, Shannon/KL, and Gini/Lorenz "
            "formalizations preserve CONCEPT-DU-001's invariant, do any win "
            "comparative abduction, and can a target-free higher-order "
            "mechanism sustain nonzero influence concentration?"
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
                    "Effective influences are nonnegative normalized weights "
                    "on a finite simplex."
                ),
                "status": "STANDARD",
                "role": "Defines the shared mathematical comparison object.",
            },
            {
                "id": "A2",
                "statement": (
                    "Uniform influence is the one-record-one-vote baseline, "
                    "with Lambda baseline 1/sqrt(n)."
                ),
                "status": "PROJECT_NATIVE",
                "role": "Carries CONCEPT-DU-001 invariant clauses (i)-(ii).",
            },
            {
                "id": "A3",
                "statement": (
                    "Majorization is the criterion for an unambiguous increase "
                    "in influence concentration."
                ),
                "status": "STANDARD",
                "role": "Tests invariant clause (iii) without picking a proxy.",
            },
            {
                "id": "A4",
                "statement": (
                    "Each proxy's concentration value can be read as a Lambda "
                    "amplitude after the stated endpoint map."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Admits structural comparison; it is not a physical "
                    "identity or coefficient derivation."
                ),
            },
            {
                "id": "A5",
                "statement": (
                    "Positive frequency-dependent reinforcement is a candidate "
                    "higher-order influence-redistribution mechanism."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Supplies the nonlinear mechanistic term.",
            },
            {
                "id": "A6",
                "statement": (
                    "Uniform mixing competes with reinforcement and is "
                    "represented by mu(1/n-p_i)."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Provides a declared null-restoring process.",
            },
            {
                "id": "A7",
                "statement": (
                    "The physical identity of p_i and the dimensionless ratio "
                    "rho=n*mu/s are not supplied by current DU dynamics."
                ),
                "status": "IMPORTED",
                "role": (
                    "Prevents the toy persistence mechanism from being "
                    "reported as a sourced Lambda value."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "F1",
                "choice": (
                    "Use Hill-order q=2 participation, q=1 Shannon/KL, and "
                    "Gini/Lorenz as the three representative proxies."
                ),
                "why_not_forced": (
                    "The concept invariant does not select a unique "
                    "concentration functional."
                ),
                "sensitivity_test": (
                    "Test all three on the same endpoint, ordered, and "
                    "incomparable specimens."
                ),
            },
            {
                "id": "F2",
                "choice": (
                    "Affinely map normalized Gini from the 1/sqrt(n) baseline "
                    "to one at a point mass."
                ),
                "why_not_forced": (
                    "Gini fixes an order, not a canonical Lambda amplitude."
                ),
                "sensitivity_test": (
                    "Use only Gini rankings in the abductive verdict; every "
                    "strictly increasing remap preserves them."
                ),
            },
            {
                "id": "F3",
                "choice": (
                    "Use n=8 for the main path and n=4,8,16 for sensitivity."
                ),
                "why_not_forced": "No physical degree count is identified here.",
                "sensitivity_test": (
                    "Repeat both sides of the rho=1 phase boundary at all "
                    "three dimensions."
                ),
            },
            {
                "id": "F4",
                "choice": (
                    "Use self-reinforcing fitness f_i=p_i opposed by uniform "
                    "mixing."
                ),
                "why_not_forced": (
                    "This is one minimal higher-order mechanism, not a "
                    "derivation from the DU source."
                ),
                "sensitivity_test": (
                    "Remove reinforcement and cross the analytic stability "
                    "threshold as two controls."
                ),
            },
            {
                "id": "F5",
                "choice": "Use rho=0.64 for the primary concentrated path.",
                "why_not_forced": (
                    "The mechanism does not determine a physical rho."
                ),
                "sensitivity_test": (
                    "Sweep rho=0.32,0.64,0.80,1.28,1.60; report amplitude "
                    "variation rather than fitting a target."
                ),
            },
            {
                "id": "F6",
                "choice": (
                    "Seed symmetry breaking with one-coordinate finite "
                    "perturbations and integrate by RK4."
                ),
                "why_not_forced": (
                    "Exact uniformity remains exactly uniform; branch identity "
                    "requires a fluctuation and numerical resolution is chosen."
                ),
                "sensitivity_test": (
                    "Sweep perturbation size over four decades, winner "
                    "identity, and halve the RK4 step."
                ),
            },
        ],
        "equations": [
            "N_eff,2 = 1/sum_i p_i^2; Lambda_2 = 1/sqrt(N_eff,2).",
            (
                "H(p)=-sum_i p_i log p_i; D_KL(p||u)=log n-H; "
                "N_eff,1=exp(H); Lambda_1=1/sqrt(N_eff,1)."
            ),
            (
                "G_norm=Gini/((n-1)/n); "
                "Lambda_G=1/sqrt(n)+(1-1/sqrt(n))*G_norm."
            ),
            (
                "dp_i/dt=s p_i(p_i-sum_j p_j^2)+mu(1/n-p_i); "
                "rho=n mu/s."
            ),
            (
                "At uniform p_i=1/n, zero-sum perturbations obey "
                "d epsilon_i/dt=(s/n-mu)epsilon_i."
            ),
        ],
        "observables": [
            "Uniform and point-mass endpoint values for all three proxies.",
            "Majorization monotonicity on a declared chain.",
            "Majorization violations on an exhaustive rational grid.",
            "Proxy-ranking reversals on incomparable distributions.",
            "Early transverse perturbation growth or decay rate.",
            "Long-time nonzero concentration and fixed-point residual.",
            "Sensitivity to rho, n, perturbation amplitude, winner, and timestep.",
        ],
        "comparators": [
            "Participation-ratio versus Shannon/KL versus Gini/Lorenz.",
            "Majorization as the proxy-independent partial order.",
            "Below-threshold reinforcement versus above-threshold mixing.",
            "The same concentrated state with reinforcement removed.",
        ],
        "null_models": [
            (
                "Uniform mixing with s=0: every nonuniform state must return "
                "to the uniform baseline."
            ),
            (
                "High-mixing rho>1: infinitesimal and sufficiently small "
                "near-uniform perturbations must decay under the same model "
                "family; a stronger-mixing control must also erase the tested "
                "concentrated state."
            ),
            (
                "Proxy consensus restricted to majorization-comparable "
                "profiles: agreement there cannot select a proxy globally."
            ),
        ],
        "falsifiers": [
            (
                "A proxy that misses the uniform baseline or reverses a "
                "majorization-ordered pair is locally unfaithful."
            ),
            (
                "Failure of target-free dynamics to maintain nonzero "
                "concentration below its analytic instability falsifies this "
                "mechanism, not the concept family."
            ),
            (
                "Dependence of the final amplitude on the seed perturbation "
                "would reveal target insertion through initial data."
            ),
            (
                "If the no-reinforcement or rho>1 null also retains "
                "concentration, the claimed discriminator fails."
            ),
            (
                "A direct no-go on monotone mechanistically generated "
                "deviation from uniform would reach the concept invariant."
            ),
        ],
        "stop_conditions": [
            (
                "Do not add more concentration proxies merely to break the "
                "observed incomparable-case tie; require a physical observable "
                "or native dynamics that selects a functional."
            ),
            (
                "Stop this mechanism if persistence requires a C_target term "
                "or retuning rho separately for every specimen."
            ),
            (
                "Do not promote a Lambda magnitude until DU identifies p_i "
                "and sources the dimensionless rho or an equivalent scale."
            ),
            (
                "A future failed proxy remains local unless the invariant "
                "itself is contradicted or a diverse family shares a traced "
                "invariant-level failure."
            ),
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-001",
            "invariant": (
                "Lambda reads deviation of effective influence from uniform, "
                "returns the 1/sqrt(n) baseline at uniform, grows under "
                "concentration, and the concentration is produced by "
                "higher-order dynamics rather than a tuned target."
            ),
            "formalization_id": (
                "PARTICIPATION-Q2__SHANNON-KL-Q1__GINI-LORENZ__"
                "REPLICATOR-MIXING-PERSISTENCE"
            ),
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "All three proxies carry the endpoint and majorization "
                "invariant, but materially disagree on incomparable profiles, "
                "so none is abductively preferred. A target-free nonlinear "
                "flow conditionally realizes persistent nonzero concentration "
                "below a declared bifurcation; it does not source the physical "
                "phase ratio or Lambda value."
            ),
            "grade": (
                "CONCEPT-SUPPORTED-BY-DIVERSE-FORMALIZATIONS / "
                "MECHANISM-CONDITIONAL / NO-ABDUCTIVE-WINNER / VALUE-OPEN"
            ),
            "admission": "CONCEPT_SUPPORTED",
            "remaining_uncertainty": (
                "No DU-native object yet fixes the influence weights, chooses "
                "q=2 versus q=1 versus Lorenz order, or derives rho. The "
                "simplex mechanism is a constructive existence specimen, not "
                "a physical dark-energy model; its nonlinear basin/hysteresis "
                "structure is only diagnosed, not exhaustively mapped."
            ),
            "checks": checks,
        },
    }


def main() -> None:
    print("DU INFLUENCE-REDISTRIBUTION COMPARATIVE-ABDUCTION PROBE")
    print("SWING-DU-SCI-01 Track 2 / CONCEPT-DU-001")

    majorization = majorization_tests()
    dynamics = dynamics_tests()
    checks = build_checks(majorization, dynamics)
    candidate = candidate_contract(checks)
    contract_errors = validate_candidate_contract(candidate)
    if contract_errors:
        raise SystemExit(
            "candidate contract incomplete:\n" + "\n".join(contract_errors)
        )

    passed = sum(check["pass"] for check in checks)
    for check in checks:
        print(f"  {'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")

    grid = majorization["exhaustive_grid"]
    primary = dynamics["primary_run"]
    print(
        "  incomparable ranking disagreements: "
        f"{grid['ranking_disagreement_pairs']}/"
        f"{grid['incomparable_pairs']} "
        f"({grid['ranking_disagreement_fraction_of_incomparable']:.3%})"
    )
    print(
        "  target-free primary concentration: "
        f"Lambda_PR={primary['final_metrics']['lambda_participation']:.6f}, "
        f"baseline={primary['final_metrics']['baseline']:.6f}, "
        f"hold drift={primary['hold_metric_drift']:.2e}"
    )
    print(
        "  grade: CONCEPT-SUPPORTED-BY-DIVERSE-FORMALIZATIONS / "
        "MECHANISM-CONDITIONAL / NO-ABDUCTIVE-WINNER / VALUE-OPEN"
    )

    payload = {
        "formalization_definitions": {
            "participation_ratio": {
                "hill_order": 2,
                "effective_count": "1/sum_i p_i^2",
                "lambda_map": "1/sqrt(N_eff,2)",
            },
            "shannon_kl": {
                "hill_order": 1,
                "effective_count": "exp(H(p))",
                "distance": "D_KL(p||uniform)=log(n)-H(p)",
                "lambda_map": "1/sqrt(N_eff,1)",
            },
            "gini_lorenz": {
                "native_object": "Lorenz-area / Gini concentration",
                "lambda_map": (
                    "endpoint-matched affine map; only ordinal results used"
                ),
            },
        },
        "majorization_and_ranking_results": majorization,
        "mechanistic_persistence_results": dynamics,
        "comparative_abduction": {
            "aggregation": "No scalar score and no vote.",
            "winner": None,
            "winner_reason": (
                "The invariant fixes majorization-monotone behavior but not "
                "rankings outside the majorization order. No independent DU "
                "observable currently selects sensitivity to peaks (q=2), "
                "information/code length (q=1), or Lorenz transfers."
            ),
            "candidate_reads": {
                "participation_ratio": {
                    "compression": (
                        "Directly preserves the register's N_eff and "
                        "1/sqrt(N_eff) language with one algebraic moment."
                    ),
                    "independence": (
                        "Its apparent 1/sqrt(N) fit reuses the same quadratic/"
                        "second-moment structure as variance and CLT routes."
                    ),
                    "novelty": (
                        "Distinctly peak-sensitive on incomparable profiles."
                    ),
                    "robustness": (
                        "Schur-convex and endpoint-correct; not uniquely "
                        "selected beyond the majorization order."
                    ),
                },
                "shannon_kl": {
                    "compression": (
                        "Unifies effective count and distance from uniform "
                        "through D_KL=log(n)-H."
                    ),
                    "independence": (
                        "Needs a physical information or likelihood object to "
                        "be more than a standard entropy re-expression."
                    ),
                    "novelty": (
                        "Weights tails differently from participation and "
                        "reverses some incomparable rankings."
                    ),
                    "robustness": (
                        "Schur-convex and endpoint-correct; no native DU "
                        "selection criterion yet."
                    ),
                },
                "gini_lorenz": {
                    "compression": (
                        "Makes one-record-one-vote deviation geometrically "
                        "visible as Lorenz area."
                    ),
                    "independence": (
                        "Its Lambda amplitude map is imported; only order is "
                        "independently meaningful here."
                    ),
                    "novelty": (
                        "Supplies a pairwise-transfer-sensitive ordering "
                        "distinct from both Hill counts."
                    ),
                    "robustness": (
                        "Schur-convex and endpoint-correct under every "
                        "strictly monotone amplitude remap."
                    ),
                },
            },
            "progressivity": (
                "The swing reduces ambiguity by identifying the exact domain "
                "of proxy agreement (majorization) and the exact domain where "
                "new physics is required (incomparable profiles). It adds a "
                "falsifiable target-free persistence mechanism while charging "
                "rho as an unsourced choice."
            ),
        },
        "epistemic_accounting": {
            "assumption_count": len(candidate["assumptions"]),
            "free_choice_count": len(candidate["free_choices"]),
            "warrant_types": candidate["warrants"],
            "abductively_preferred_warrant_claimed": False,
            "target_concentration_parameter_present": False,
            "physical_lambda_value_sourced": False,
            "concept_failure_scope_if_a_proxy_later_fails": "FORMALIZATION",
        },
        "stop_rule_evaluation": {
            "proxy_proliferation_stop_triggered": True,
            "reason": (
                "Three faithful proxies already disagree outside the "
                "invariant's partial order. Adding proxies without an "
                "independent physical selector would be story-shopping."
            ),
            "mechanism_stop_triggered": False,
            "mechanism_reason": (
                "The candidate beats the mixing controls and sustains "
                "concentration without a target term, but remains at "
                "conditional toy-mechanism grade."
            ),
            "reopen_condition": (
                "A DU-native influence object or observable selects a "
                "functional, or a source dynamics derives rho/equivalent "
                "scale without fitting Lambda."
            ),
        },
    }
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)
    print(f"artifact: {ARTIFACT_PATH}")

    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise SystemExit(f"unexpected failed checks: {failed}")
    print("All predeclared checks match. Exit 0.")


if __name__ == "__main__":
    main()
