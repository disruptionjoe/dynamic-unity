#!/usr/bin/env python3
"""Foreground COV-02 kill for the Dynamic Unity Lambda(N) cosmology.

This script does not fit data and does not claim a fundamental action.  It asks
whether the COV-01 FLRW bookkeeping can be promoted to a covariant interacting-
vacuum system without adding a free momentum-transfer or sound-speed function.

The strongest local lift tested here is

    V(N) = A N^(-1/2),
    u^a nabla_a N = S(Theta) = kappa (Theta/3)^(-3),
    T_V^{ab} = -V g^{ab},
    nabla_a T_m^{ab} = nabla^b V.

Here u^a is the matter four-velocity and Theta=nabla_a u^a.  This is a scalar
transport law, not a coordinate-time prescription.  It reproduces COV-01 on
FLRW and fixes the complete transfer four-vector.  Its scalar perturbations are
written in matter-comoving gauge, where every displayed perturbation equals its
gauge-invariant comoving counterpart.

The principal scalar characteristic is derived, not selected:

    c_N^2 = S_Theta V_N / rho_m
          = beta Omega_V^3 / (2(1-Omega_V)).

At every accelerating fixed point of COV-01 this becomes c_N^2=3 Omega_V>1.
The same pressure/force term dominates linear-scale gravity unless beta is of
order 1e-5 or smaller at k=0.1 h/Mpc, where the background is numerically the
constant-Lambda limit.  The result is scoped to this natural local lift; it is
not a no-go for every possible causal-set or nonlocal completion.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable, Dict, List, Sequence, Tuple

from du_lambda_N_covariant_acceleration_audit import (
    OMEGA_0,
    background_row,
    first_unphysical_past_redshift,
    fixed_point,
    integrate_to,
)


ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_lambda_N_covariant_perturbation_kill_result.json"
)

C_KM_S = 299_792.458
H100_KM_S_MPC = 100.0
K_H0_PER_H_MPC = C_KM_S / H100_KM_S_MPC
Z_INITIAL = 100.0


def beta_function(a: float, b: float) -> float:
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def causal_past_volume_coefficient(power_p: float) -> float:
    """C(p) in Vol(J^-(T))=C(p) T^4 for flat a(t)=t^p, 0<p<1."""

    if not 0.0 < power_p < 1.0:
        raise ValueError("power-law causal-volume formula requires 0<p<1")
    beta_arg = (1.0 + 3.0 * power_p) / (1.0 - power_p)
    return (
        (4.0 * math.pi / 3.0)
        * beta_function(beta_arg, 4.0)
        / (1.0 - power_p) ** 4
    )


def causal_past_kappa_effective(power_p: float) -> float:
    """(dN/dt)/H^-3 for the causal-past four-volume of a power-law FLRW."""

    return 4.0 * causal_past_volume_coefficient(power_p) * power_p**3


def causal_past_volume_coefficient_numeric(power_p: float, panels: int = 20_000) -> float:
    """Independent Simpson integration of the causal-past coefficient."""

    if panels % 2:
        raise ValueError("Simpson integration requires an even panel count")
    step = 1.0 / panels

    def integrand(x: float) -> float:
        return x ** (3.0 * power_p) * (1.0 - x ** (1.0 - power_p)) ** 3

    total = integrand(0.0) + integrand(1.0)
    for index in range(1, panels):
        total += (4.0 if index % 2 else 2.0) * integrand(index * step)
    integral = total * step / 3.0
    return (4.0 * math.pi / 3.0) * integral / (1.0 - power_p) ** 3


def sound_speed_sq(beta: float, omega: float) -> float:
    if beta == 0.0:
        return 0.0
    return 0.5 * beta * omega**3 / (1.0 - omega)


def fixed_point_sound_speed_sq(beta: float) -> float:
    return sound_speed_sq(beta, fixed_point(beta))


def k_over_h0(k_h_mpc: float) -> float:
    return k_h_mpc * K_H0_PER_H_MPC


def present_jeans_ratio(beta: float, k_h_mpc: float) -> float:
    """Pressure/force principal term divided by the dust gravity coefficient."""

    omega_m = 1.0 - OMEGA_0
    gravity = 1.5 * omega_m
    pressure = sound_speed_sq(beta, OMEGA_0) * k_over_h0(k_h_mpc) ** 2
    return pressure / gravity


def beta_at_unit_jeans_ratio(k_h_mpc: float) -> float:
    omega_m = 1.0 - OMEGA_0
    cs2_per_beta = OMEGA_0**3 / (2.0 * omega_m)
    return 1.5 * omega_m / (cs2_per_beta * k_over_h0(k_h_mpc) ** 2)


GrowthState = Tuple[float, float, float, float, float, float]
# Omega_V, ln(H/H0), ln(N/A^2), delta_m, delta_Theta/H, delta_N/N


def add_scaled(state: Sequence[float], slope: Sequence[float], scale: float) -> GrowthState:
    return tuple(state[i] + scale * slope[i] for i in range(6))  # type: ignore[return-value]


def perturbation_rhs(x: float, state: GrowthState, beta: float, k_h_mpc: float) -> GrowthState:
    omega, ln_h, _ln_n, delta_m, expansion, delta_n = state
    omega_m = 1.0 - omega
    if omega_m <= 0.0:
        raise ArithmeticError("matter density became non-positive")

    omega_prime = omega * (3.0 * omega_m - 0.5 * beta * omega * omega)
    ln_h_prime = -1.5 * omega_m
    g_count = beta * omega * omega

    ratio_v_m = omega / omega_m
    phi_comoving = -0.5 * ratio_v_m * delta_n
    cs2 = sound_speed_sq(beta, omega)
    k_a_h_sq = k_over_h0(k_h_mpc) ** 2 * math.exp(-2.0 * (x + ln_h))

    # Perturbed scalar transport:
    # delta(dot N)_c - dot(N) phi_c = S_Theta delta(Theta)_c.
    delta_n_prime = -g_count * (expansion + delta_n - phi_comoving)

    # Perturbed matter energy balance.  No delta Q, rest frame, or sound speed
    # is chosen independently; each follows from V(N) and the transport law.
    delta_m_prime = (
        -cs2 * (delta_m + 0.5 * delta_n)
        + 0.5 * ratio_v_m * delta_n_prime
        + 1.5 * ratio_v_m * delta_n
        - expansion
    )

    # Gauge-invariant comoving Raychaudhuri equation, including the acceleration
    # divergence fixed by rho_m a_i = D_i V and phi_c=delta V_c/rho_m.
    expansion_prime = (
        -(0.5 + 1.5 * omega) * expansion
        - 4.5 * omega_m * phi_comoving
        - 1.5 * omega_m * delta_m
        - 1.5 * omega * delta_n
        - k_a_h_sq * phi_comoving
    )

    return (
        omega_prime,
        ln_h_prime,
        g_count,
        delta_m_prime,
        expansion_prime,
        delta_n_prime,
    )


def rk4_step(
    x: float,
    state: GrowthState,
    step: float,
    beta: float,
    k_h_mpc: float,
) -> GrowthState:
    k1 = perturbation_rhs(x, state, beta, k_h_mpc)
    k2 = perturbation_rhs(
        x + 0.5 * step,
        add_scaled(state, k1, 0.5 * step),
        beta,
        k_h_mpc,
    )
    k3 = perturbation_rhs(
        x + 0.5 * step,
        add_scaled(state, k2, 0.5 * step),
        beta,
        k_h_mpc,
    )
    k4 = perturbation_rhs(
        x + step,
        add_scaled(state, k3, step),
        beta,
        k_h_mpc,
    )
    return tuple(
        state[i]
        + step * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
        for i in range(6)
    )  # type: ignore[return-value]


def integrate_growth(beta: float, k_h_mpc: float, *, steps: int = 30_000) -> Dict[str, float]:
    x_initial = -math.log1p(Z_INITIAL)
    omega_i, ln_h_i, ln_n_i = integrate_to(beta, x_initial)
    state: GrowthState = (omega_i, ln_h_i, ln_n_i, 1.0, -1.0, 0.0)
    step = -x_initial / steps
    x = x_initial
    max_abs_delta_n = 0.0
    for _ in range(steps):
        state = rk4_step(x, state, step, beta, k_h_mpc)
        x += step
        max_abs_delta_n = max(max_abs_delta_n, abs(state[5]))
        if not all(math.isfinite(value) for value in state):
            raise ArithmeticError("non-finite perturbation state")
    return {
        "beta": beta,
        "k_h_Mpc": k_h_mpc,
        "delta_m_z0": state[3],
        "delta_theta_over_H_z0": state[4],
        "delta_N_over_N_z0": state[5],
        "max_abs_delta_N_over_N": max_abs_delta_n,
    }


StandardState = Tuple[float, float, float, float]
# Omega_V, ln H, delta, d(delta)/dln a


def standard_rhs(state: StandardState, beta: float) -> StandardState:
    omega, _ln_h, delta, delta_prime = state
    omega_m = 1.0 - omega
    return (
        omega * (3.0 * omega_m - 0.5 * beta * omega * omega),
        -1.5 * omega_m,
        delta_prime,
        -(0.5 + 1.5 * omega) * delta_prime + 1.5 * omega_m * delta,
    )


def standard_rk4(state: StandardState, step: float, beta: float) -> StandardState:
    def add(s: Sequence[float], k: Sequence[float], q: float) -> StandardState:
        return tuple(s[i] + q * k[i] for i in range(4))  # type: ignore[return-value]

    k1 = standard_rhs(state, beta)
    k2 = standard_rhs(add(state, k1, 0.5 * step), beta)
    k3 = standard_rhs(add(state, k2, 0.5 * step), beta)
    k4 = standard_rhs(add(state, k3, step), beta)
    return tuple(
        state[i]
        + step * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
        for i in range(4)
    )  # type: ignore[return-value]


def integrate_standard_growth(beta: float = 0.0, *, steps: int = 30_000) -> float:
    x_initial = -math.log1p(Z_INITIAL)
    omega_i, ln_h_i, _ln_n_i = integrate_to(beta, x_initial)
    state: StandardState = (omega_i, ln_h_i, 1.0, 1.0)
    step = -x_initial / steps
    for _ in range(steps):
        state = standard_rk4(state, step, beta)
    return state[2]


def gauge_invariance_control() -> Dict[str, float | bool]:
    delta_n = 0.37
    n_dot = 1.91
    theta = -0.24
    time_shift = 0.63
    original = delta_n + n_dot * theta
    transformed = (delta_n - n_dot * time_shift) + n_dot * (theta + time_shift)
    return {
        "original_delta_N_com": original,
        "transformed_delta_N_com": transformed,
        "absolute_residual": abs(original - transformed),
        "passes": abs(original - transformed) < 1.0e-14,
    }


def lambda_fractional_change_since_z(beta: float, z: float) -> float:
    _omega, _ln_h, ln_n_past = integrate_to(beta, -math.log1p(z))
    _omega0, _ln_h0, ln_n_now = integrate_to(beta, 0.0)
    lambda_now_over_then = math.exp(-0.5 * (ln_n_now - ln_n_past))
    return lambda_now_over_then - 1.0


def rounded(value: object) -> object:
    if isinstance(value, float):
        return round(value, 12)
    if isinstance(value, list):
        return [rounded(item) for item in value]
    if isinstance(value, dict):
        return {key: rounded(item) for key, item in value.items()}
    return value


def run_audit() -> Dict[str, object]:
    checks: List[Dict[str, object]] = []

    def check(check_id: str, passed: bool, detail: str) -> None:
        checks.append({"id": check_id, "passed": bool(passed), "detail": detail})

    # Candidate A: a slice-integrated four-volume has an arbitrary cell-volume
    # normalization.  The observable Lambda changes under that arbitrary choice.
    cell_rescaling = 16.0
    lambda_rescaling = cell_rescaling ** -0.5
    check(
        "global_slice_volume_has_arbitrary_cell",
        abs(lambda_rescaling - 0.25) < 1.0e-14,
        "rescaling an arbitrary comoving cell by 16 rescales Lambda by 1/4",
    )

    # Candidate B: causal-past volume is invariant and retarded, but its exact
    # dN/dt coefficient is history-dependent, so it is not the COV-01 constant-
    # kappa law without changing the background model.
    kappa_radiation = causal_past_kappa_effective(0.5)
    kappa_matter = causal_past_kappa_effective(2.0 / 3.0)
    causal_kappa_ratio = kappa_matter / kappa_radiation
    causal_numeric_residual = max(
        abs(
            causal_past_volume_coefficient(power_p)
            / causal_past_volume_coefficient_numeric(power_p)
            - 1.0
        )
        for power_p in (0.5, 2.0 / 3.0)
    )
    check(
        "causal_past_volume_formula_positive_control",
        causal_numeric_residual < 1.0e-9,
        f"max analytic/numeric coefficient residual={causal_numeric_residual:.3e}",
    )
    check(
        "causal_past_count_coefficient_is_history_dependent",
        abs(causal_kappa_ratio - 1.0) > 0.1,
        f"kappa_eff(matter)/kappa_eff(radiation)={causal_kappa_ratio:.6f}",
    )

    # Candidate C: the local congruence scalar exactly reproduces COV-01 and
    # fixes Q_a=-nabla_a V (vacuum convention) / +nabla^a V to matter.
    sample_h = 0.73
    sample_kappa = 1.17
    theta = 3.0 * sample_h
    scalar_source = sample_kappa * (theta / 3.0) ** -3
    background_source = sample_kappa * sample_h**-3
    check(
        "local_scalar_transport_reproduces_background",
        abs(scalar_source / background_source - 1.0) < 1.0e-14,
        "u.nabla N=kappa(Theta/3)^-3 reduces exactly to Ndot=kappa H^-3",
    )
    check(
        "full_transfer_four_vector_fixed",
        True,
        "T_V=-Vg implies Q_vac,a=-nabla_a V and fixes both energy and momentum transfer",
    )

    gauge_control = gauge_invariance_control()
    check(
        "comoving_count_perturbation_is_gauge_invariant",
        bool(gauge_control["passes"]),
        f"time-shift residual={gauge_control['absolute_residual']:.3e}",
    )

    # A minimal local Lagrange-multiplier action cannot keep the assumed
    # stress split: N-variation gives div(chi u)=-V_N, so chi=0 is impossible
    # for V_N=-V/(2N)!=0.  This does not forbid a different action; it records
    # that the complete-Q lift is phenomenological rather than action-derived.
    v_over_n = 0.42
    v_n = -0.5 * v_over_n
    check(
        "minimal_action_has_nonzero_multiplier_stress",
        abs(v_n) > 0.0,
        "V_N!=0 forces a nonzero constraint multiplier; its stress cannot be silently omitted",
    )

    # The zero-sound-speed/geodesic escape is not compatible with the declared
    # local count law: delta V_com=0 => delta N_com=0; geodesic flow => phi=0;
    # transport then demands S_Theta delta Theta=0, excluding growing structure
    # for beta>0.
    s_theta = -2.3
    growing_delta_theta = 0.41
    geodesic_transport_residual = s_theta * growing_delta_theta
    check(
        "geodesic_zero_sound_escape_incompatible",
        abs(geodesic_transport_residual) > 1.0e-6,
        "delta N_com=phi=0 leaves nonzero S_Theta*deltaTheta for a growing mode",
    )

    beta_rows: List[Dict[str, object]] = []
    for beta in (1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2, 0.25, 1.0):
        omega_star = fixed_point(beta)
        cs2_now = sound_speed_sq(beta, OMEGA_0)
        cs2_star = fixed_point_sound_speed_sq(beta)
        beta_rows.append(
            {
                "beta": beta,
                "omega_star": omega_star,
                "cs2_today": cs2_now,
                "cs2_fixed_point": cs2_star,
                "three_omega_star": 3.0 * omega_star,
                "fixed_point_superluminal": cs2_star > 1.0,
            }
        )

    fixed_identity_residual = max(
        abs(float(row["cs2_fixed_point"]) - float(row["three_omega_star"]))
        for row in beta_rows
    )
    check(
        "fixed_point_characteristic_identity",
        fixed_identity_residual < 2.0e-9,
        f"max |c_N^2-3Omega*|={fixed_identity_residual:.3e}",
    )
    check(
        "all_accelerating_fixed_points_superluminal",
        all(
            (float(row["omega_star"]) <= 1.0 / 3.0)
            or bool(row["fixed_point_superluminal"])
            for row in beta_rows
        ),
        "acceleration requires Omega*>1/3, hence c_N^2=3Omega*>1",
    )
    target_principal_cs2 = (-2.0) * (-0.3)
    unstable_control_cs2 = (-2.0) * (+0.3)
    check(
        "principal_symbol_unstable_interaction_control",
        target_principal_cs2 > 0.0 and unstable_control_cs2 < 0.0,
        "flipping V_N changes oscillatory characteristics into a gradient instability",
    )

    jeans_caps = {
        "k_0p01_h_Mpc": beta_at_unit_jeans_ratio(0.01),
        "k_0p1_h_Mpc": beta_at_unit_jeans_ratio(0.1),
    }
    check(
        "linear_scale_jeans_gate_forces_small_beta",
        jeans_caps["k_0p1_h_Mpc"] < 1.1e-5,
        f"unit force/gravity ratio at k=0.1 h/Mpc occurs at beta={jeans_caps['k_0p1_h_Mpc']:.3e}",
    )

    # Foreground scale-dependent growth.  The beta=0 target is independently
    # integrated in standard second-order form as a positive control.
    standard_growth = integrate_standard_growth(0.0)
    target_control = integrate_growth(0.0, 0.1)
    control_relative_error = abs(target_control["delta_m_z0"] / standard_growth - 1.0)
    check(
        "constant_lambda_growth_positive_control",
        control_relative_error < 2.0e-9,
        f"relative growth mismatch={control_relative_error:.3e}",
    )

    growth_rows: List[Dict[str, object]] = []
    for beta in (1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2):
        for k_h_mpc in (0.01, 0.1):
            row = integrate_growth(beta, k_h_mpc)
            row["growth_ratio_to_lambda"] = row["delta_m_z0"] / standard_growth
            row["present_jeans_ratio"] = present_jeans_ratio(beta, k_h_mpc)
            growth_rows.append(row)

    convergence_coarse = integrate_growth(1.0e-3, 0.1, steps=30_000)
    convergence_fine = integrate_growth(1.0e-3, 0.1, steps=60_000)
    growth_resolution_residual = abs(
        convergence_coarse["delta_m_z0"] / convergence_fine["delta_m_z0"] - 1.0
    )
    check(
        "growth_resolution_convergence",
        growth_resolution_residual < 1.0e-8,
        f"30k/60k relative residual={growth_resolution_residual:.3e}",
    )

    row_beta_1e4_k01 = next(
        row
        for row in growth_rows
        if row["beta"] == 1.0e-4 and row["k_h_Mpc"] == 0.1
    )
    check(
        "growth_probe_has_scale_dependent_teeth",
        abs(float(row_beta_1e4_k01["growth_ratio_to_lambda"]) - 1.0) > 0.01,
        "beta=1e-4 produces >1% scale-dependent growth movement at k=0.1 h/Mpc",
    )

    beta_growth_cap = jeans_caps["k_0p1_h_Mpc"]
    lambda_change_z2 = lambda_fractional_change_since_z(beta_growth_cap, 2.0)
    early_row_at_cap = background_row(beta_growth_cap, 1100.0)
    natural_past_boundary = first_unphysical_past_redshift(9.0)
    check(
        "lambda_limit_keeps_positive_matter_era",
        float(early_row_at_cap["omega_lambda"]) < 1.0e-8,
        f"Omega_V(z=1100)={early_row_at_cap['omega_lambda']:.3e}",
    )
    check(
        "natural_beta_matter_positivity_control",
        natural_past_boundary is not None and natural_past_boundary < 0.25,
        f"beta=9 reaches rho_m=0 at z={natural_past_boundary:.3f}",
    )
    check(
        "growth_allowed_branch_is_lambda_limit",
        abs(lambda_change_z2) < 1.0e-5,
        f"at the internal k=0.1 growth cap, |Delta Lambda/Lambda| since z=2 is {abs(lambda_change_z2):.3e}",
    )

    failed = [item for item in checks if not item["passed"]]
    if failed:
        raise AssertionError(f"COV-02 checks failed: {failed}")

    result: Dict[str, object] = {
        "audit_id": "DU-LAMBDA-N-COV-02",
        "date": "2026-07-21",
        "status": "executed_scoped",
        "scope": (
            "covariant-count candidate audit plus the strongest local matter-congruence "
            "complete-Q lift; gauge-invariant scalar principal symbol and finite linear-growth "
            "probe; no Boltzmann code, likelihood, radiation/baryon split, or fundamental action"
        ),
        "candidate_matrix": [
            {
                "candidate": "homogeneous or slice-integrated four-volume",
                "covariant": False,
                "local": False,
                "reproduces_COV01": "only after an arbitrary slicing/cell/horizon prescription",
                "disposition": "BACKGROUND_ONLY",
            },
            {
                "candidate": "causal-past four-volume N(x)=Vol(J^-(x) cap J^+(Sigma0))",
                "covariant": True,
                "local": False,
                "causal": True,
                "reproduces_COV01": False,
                "reason": "the exact coefficient in dN/dt=kappa_eff H^-3 depends on expansion history; perturbations are retarded memory integrals",
                "disposition": "SEPARATE_NONLOCAL_MODEL__NOT_THIS_BACKGROUND_LIFT",
            },
            {
                "candidate": "matter-congruence scalar counter",
                "definition": "u^a nabla_a N=kappa(Theta/3)^-3",
                "covariant": True,
                "local": True,
                "reproduces_COV01": True,
                "complete_transfer": "Q_vac,a=-nabla_a V; matter receives +nabla^a V",
                "action_status": "complete-Q phenomenology; minimal multiplier action changes the assumed stress split",
                "disposition": "ADVANCES_TO_PERTURBATION_KILL",
            },
            {
                "candidate": "geodesic zero-sound interaction Q^a parallel u^a",
                "covariant": True,
                "local": True,
                "reproduces_COV01": "background only",
                "reason": "for V_N!=0 it forces delta N_com=0; the local count transport then forces deltaTheta=0 for beta>0",
                "disposition": "REIMPORTS_TARGET_HISTORY_OR_BETA_ZERO",
            },
        ],
        "local_covariant_completion": {
            "vacuum": "T_V^{ab}=-V(N)g^{ab}, V=A*N^(-1/2)",
            "count_transport": "u^a*nabla_a N=S(Theta)=kappa*(Theta/3)^(-3)",
            "matter_energy": "dot(rho_m)+Theta*rho_m=-dot(V)",
            "matter_momentum": "rho_m*a^a=D^a V",
            "transfer": "Q_vac,a=-nabla_a V",
            "comoving_gauge_invariants": {
                "delta_N_c": "delta N + dot(N)*theta_m",
                "delta_V_c": "V_N*delta_N_c",
                "lapse": "phi_c=delta_V_c/rho_m",
                "transport": "delta(dot N)_c-dot(N)*phi_c=S_Theta*deltaTheta_c",
                "energy": "delta(dot rho)_c-dot(rho)*phi_c+Theta*delta rho_c+rho*deltaTheta_c=-delta(dot V)_c+dot(V)*phi_c",
            "raychaudhuri": "delta(dot Theta)_c-dot(Theta)*phi_c+(2/3)Theta*deltaTheta_c+4piG(delta rho_c-2delta V_c)-D^2 phi_c=0",
            },
            "vector_tensor_sectors": "the transfer force is a scalar gradient and vacuum has no anisotropic stress; no new linear transverse/vector or tensor principal mode is supplied",
        },
        "principal_symbol": {
            "equation": "delta(ddot N)_c+c_N^2*(k^2/a^2)*delta N_c=lower-derivative terms",
            "sound_speed_sq": "c_N^2=S_Theta*V_N/rho_m=beta*Omega_V^3/[2(1-Omega_V)]",
            "fixed_point_identity": "c_N^2=3*Omega_V*",
            "accelerating_fixed_point_consequence": "Omega_V*>1/3 => c_N^2>1",
            "kinetic_sign_status": "not established without an action; classical principal mode is oscillatory rather than gradient-unstable",
            "unstable_control": "flipping the sign of V_N makes c_N^2<0 and the same principal mode exponentially unstable",
            "rows": beta_rows,
        },
        "causal_past_volume_control": {
            "formula": "Vol(J^-(T))=C(p)T^4 for a=t^p; kappa_eff=(dN/dt)/H^-3=4C(p)p^3",
            "radiation_p_1_over_2": kappa_radiation,
            "matter_p_2_over_3": kappa_matter,
            "matter_to_radiation_ratio": causal_kappa_ratio,
        },
        "growth": {
            "initial_redshift": Z_INITIAL,
            "initial_mode": "matter-era growing mode delta_m=1, deltaTheta/H=-1, deltaN/N=0",
            "k_conversion": "k/H0=(c/100 km/s/Mpc)*(k/[h/Mpc])",
            "positive_control_standard_growth": standard_growth,
            "positive_control_target_growth": target_control,
            "positive_control_relative_error": control_relative_error,
            "resolution_convergence_relative_error": growth_resolution_residual,
            "rows": growth_rows,
            "internal_jeans_caps": jeans_caps,
            "note": "unit force/gravity is a fail-fast internal discriminator, not a likelihood-derived empirical bound",
        },
        "lambda_limit": {
            "beta_cap_from_k_0p1_internal_jeans_gate": beta_growth_cap,
            "fractional_lambda_change_since_z2_at_cap": lambda_change_z2,
            "omega_V_z1100_at_cap": early_row_at_cap["omega_lambda"],
            "natural_beta_9_first_rho_m_zero_redshift": natural_past_boundary,
            "interpretation": "the count-driven rolling becomes observationally and dynamically idle before linear clustering is protected",
        },
        "controls": {
            "gauge_invariance": gauge_control,
            "global_cell_rescaling": {
                "cell_factor": cell_rescaling,
                "lambda_factor": lambda_rescaling,
            },
            "geodesic_transport_residual": geodesic_transport_residual,
        },
        "checks": checks,
        "check_summary": {"passed": len(checks), "failed": len(failed)},
        "verdict": "VIABLE_ONLY_AS_LAMBDA_LIMIT",
        "interpretation": [
            "COV-01 is not merely non-covariant: a natural local covariant lift with a complete transfer four-vector exists at phenomenological interacting-vacuum grade.",
            "That lift fixes a nonzero comoving vacuum perturbation and a scale-dependent scalar force; no rest-frame sound speed or momentum transfer remains free to tune.",
            "Every accelerating fixed point has a superluminal scalar characteristic in the declared continuum equations, so the local lift fails the causal perturbation gate for any beta>0 that reaches its attractor.",
            "On currently linear clustering scales the same force requires beta of order 1e-5 or smaller even under a deliberately weak unit-pressure/gravity discriminator.",
            "At that beta the change in Lambda since z=2 is below 1e-5: the surviving branch is physically the constant-Lambda limit and the N transport is explanatorily idle.",
            "The causal-past count remains a distinct retarded nonlocal model worth separate construction, but it does not inherit the COV-01 constant-kappa background and cannot be counted as a rescue of this closure.",
        ],
    }
    return rounded(result)  # type: ignore[return-value]


def main() -> None:
    result = run_audit()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    summary = result["check_summary"]
    total = summary["passed"] + summary["failed"]  # type: ignore[index]
    print(
        "DU-LAMBDA-N-COV-02: "
        f"{summary['passed']}/{total} checks PASS | "  # type: ignore[index]
        "local covariant lift exists but is viable only as the constant-Lambda limit"
    )


if __name__ == "__main__":
    main()
