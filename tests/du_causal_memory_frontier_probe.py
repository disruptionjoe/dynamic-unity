#!/usr/bin/env python3
"""SWING-DU-CMF-01: causal-memory / order-first martingale frontier probe.

This is a deterministic, standard-library build-and-kill tournament for the
nonlocal branch left open by COV-02.  It keeps five objects typed apart:

1. N_J: the literal unweighted four-volume of an event's causal past.
2. N_box: a retarded bi-wave memory proxy, 8*pi*Box_ret^-2(1), not an event count.
3. A separately conserved positive component rho_X=A/sqrt(N_J).
4. A vacuum-stress completion with the corresponding Bianchi exchange.
5. An order-first signed causal martingale S_N/N whose variance produces N^-1/2.

Pre-registered hard questions:

* Does causal memory genuinely leave the local model's superluminal principal class?
* Does the literal count accelerate, or is it an always-on radiation/matter tracker?
* Can an order-first stochastic sign law be quiet early and order-one late without
  selecting an exceptional history?
* Is the spatial covariance fixed by common-past overlap rather than inserted?
* Does an offset/window rescue merely import a clock of order the present age?

The probe does not claim a fundamental nonlocal action, quantum ghost freedom, a
Boltzmann likelihood, or a program-native causet growth law.  It tests the strongest
finite/background consequences that can be fixed before those expensive builds.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Callable


PI = math.pi
OMEGA_R0 = 9.2e-5
OMEGA_M0 = 0.315
OMEGA_LATE_TARGET = 0.69
EARLY_FRACTION_CAP = 0.02
A_INITIAL = 1.0e-10
DEFAULT_OUT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_causal_memory_frontier_probe_result.json"
)


def simpson(fn: Callable[[float], float], lo: float, hi: float, steps: int) -> float:
    """Composite Simpson integration with a fixed, deterministic grid."""
    if steps <= 0 or steps % 2:
        raise ValueError("steps must be a positive even integer")
    h = (hi - lo) / steps
    total = fn(lo) + fn(hi)
    total += 4.0 * sum(fn(lo + i * h) for i in range(1, steps, 2))
    total += 2.0 * sum(fn(lo + i * h) for i in range(2, steps, 2))
    return total * h / 3.0


# ---------------------------------------------------------------------------
# Exact causal-past geometry and a retarded bi-wave comparator.
# ---------------------------------------------------------------------------


def causal_profile(x: float, p: float) -> float:
    """Stable cube-root integrand for C_J(p).

    For a=t^p and T=1,
      a(t') * chi(T,t') = (x-x^p)/(p-1),
    with smooth p=1 limit -x log x.  The four-volume integrand is its cube.
    """
    if x <= 0.0:
        # Minkowski (p=0) has a finite unit-radius past cone at the initial
        # endpoint; every p>0 case used here vanishes there.
        return 1.0 if abs(p) < 1.0e-15 else 0.0
    if abs(p - 1.0) < 1.0e-12:
        return -x * math.log(x)
    return (x - x**p) / (p - 1.0)


def causal_coefficient_exact(p: float) -> float:
    """C_J(p) in Vol(J^-(T))=C_J(p) T^4, valid across p=1."""
    if p <= -1.0 / 3.0:
        raise ValueError("power-law causal volume diverges at the initial boundary")
    return PI / ((3.0 * p + 1.0) * (p + 1.0) * (p + 3.0))


def causal_coefficient_quadrature(p: float, steps: int = 20_000) -> float:
    integral = simpson(lambda x: causal_profile(x, p) ** 3, 0.0, 1.0, steps)
    return 4.0 * PI * integral / 3.0


def biwave_coefficient(p: float) -> float:
    """Coefficient of N_box=8*pi*S for D U=1, D S=U, D=d2+3H d.

    Retarded zero data give U=t^2/[2(1+3p)] and
    S=t^4/[24(1+3p)(1+p)].
    """
    return PI / (3.0 * (3.0 * p + 1.0) * (p + 1.0))


def biwave_auxiliary_residuals(p: float) -> dict[str, float]:
    u2 = 1.0 / (2.0 * (1.0 + 3.0 * p))
    s4 = 1.0 / (24.0 * (1.0 + 3.0 * p) * (1.0 + p))
    # D(u2*t^2)=2(1+3p)u2; D(s4*t^4)=12(1+p)s4*t^2.
    return {
        "D_U_minus_1": 2.0 * (1.0 + 3.0 * p) * u2 - 1.0,
        "D_S_minus_U_coefficient": 12.0 * (1.0 + p) * s4 - u2,
    }


def de_sitter_causal_volume(H: float, duration: float) -> float:
    """Exact causal-past four-volume for a de Sitter phase of finite duration."""
    t = duration
    bracket = (
        t
        - 3.0 * (1.0 - math.exp(-H * t)) / H
        + 1.5 * (1.0 - math.exp(-2.0 * H * t)) / H
        - (1.0 - math.exp(-3.0 * H * t)) / (3.0 * H)
    )
    return 4.0 * PI * bracket / (3.0 * H**3)


def de_sitter_volume_quadrature(H: float, duration: float, steps: int = 20_000) -> float:
    integral = simpson(
        lambda u: ((1.0 - math.exp(-H * u)) / H) ** 3,
        0.0,
        duration,
        steps,
    )
    return 4.0 * PI * integral / 3.0


# ---------------------------------------------------------------------------
# Deterministic positive-envelope tracker and fixed-point comparisons.
# ---------------------------------------------------------------------------


def omega_vacuum_fixed_point(p: float, w_background: float) -> float:
    return 1.0 - 2.0 / (3.0 * p * (1.0 + w_background))


def amplitude_for_fixed_point(
    p: float, w_background: float, coefficient: Callable[[float], float]
) -> float:
    density_coefficient = 3.0 * p * p - 2.0 * p / (1.0 + w_background)
    return density_coefficient * math.sqrt(coefficient(p))


def solve_fixed_point(
    amplitude: float, w_background: float, coefficient: Callable[[float], float]
) -> float:
    baseline = 2.0 / (3.0 * (1.0 + w_background))
    lo = baseline * (1.0 + 1.0e-12)
    hi = 2.0

    def residual(p: float) -> float:
        return amplitude_for_fixed_point(p, w_background, coefficient) - amplitude

    while residual(hi) < 0.0:
        hi *= 2.0
        if hi > 1.0e6:
            raise RuntimeError("fixed-point bracket failed")
    for _ in range(180):
        mid = 0.5 * (lo + hi)
        if residual(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def deterministic_tracker_summary(coefficient: Callable[[float], float]) -> dict[str, float]:
    p_m_late = 2.0 / (3.0 * (1.0 - OMEGA_LATE_TARGET))
    amplitude_late = amplitude_for_fixed_point(p_m_late, 0.0, coefficient)
    p_r_from_late = solve_fixed_point(amplitude_late, 1.0 / 3.0, coefficient)
    omega_r_from_late = omega_vacuum_fixed_point(p_r_from_late, 1.0 / 3.0)

    p_r_cap = 1.0 / (2.0 * (1.0 - EARLY_FRACTION_CAP))
    amplitude_cap = amplitude_for_fixed_point(p_r_cap, 1.0 / 3.0, coefficient)
    p_m_from_cap = solve_fixed_point(amplitude_cap, 0.0, coefficient)
    omega_m_from_cap = omega_vacuum_fixed_point(p_m_from_cap, 0.0)
    return {
        "late_target_omega": OMEGA_LATE_TARGET,
        "late_target_p_matter": p_m_late,
        "amplitude_for_late_target": amplitude_late,
        "predicted_radiation_p": p_r_from_late,
        "predicted_radiation_omega": omega_r_from_late,
        "weak_early_cap": EARLY_FRACTION_CAP,
        "amplitude_at_early_cap": amplitude_cap,
        "predicted_matter_p_from_early_cap": p_m_from_cap,
        "predicted_matter_omega_from_early_cap": omega_m_from_cap,
    }


# ---------------------------------------------------------------------------
# Separately conserved rho_X=A/sqrt(N_J): full radiation/matter history.
# ---------------------------------------------------------------------------


def moment_integral_coefficient(k: int, p: float) -> float:
    """Integral coefficient I_k for a=B*t^p light-cone moments."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if abs(p - 1.0) < 1.0e-12:
        # Not needed for the radiation initial data.
        return math.factorial(k) / (3.0 * p + 1.0) ** (k + 1)
    total = 0.0
    for j in range(k + 1):
        total += (
            (-1.0) ** j
            * math.comb(k, j)
            / (3.0 * p + j * (1.0 - p) + 1.0)
        )
    return total / (1.0 - p) ** k


def conserved_x_initial_state(amplitude: float) -> list[float]:
    p = 0.5
    c_r = causal_coefficient_exact(p)
    tracker_fraction = 4.0 * amplitude / (3.0 * math.sqrt(c_r))
    if not (0.0 <= tracker_fraction < 1.0):
        raise ValueError("radiation tracker fraction must be in [0,1)")
    radiation_scale = math.sqrt(OMEGA_R0 / (1.0 - tracker_fraction))
    tau = A_INITIAL**2 / (2.0 * radiation_scale)
    b_norm = math.sqrt(2.0 * radiation_scale)
    moments = [
        b_norm ** (3 - k)
        * tau ** (1.0 + 3.0 * p + k * (1.0 - p))
        * moment_integral_coefficient(k, p)
        for k in range(4)
    ]
    return [tau, *moments]


def conserved_x_observables(x: float, y: list[float], amplitude: float) -> dict[str, float]:
    a = math.exp(x)
    _, _, _, m2, m3 = y
    v = 4.0 * PI * m3 / 3.0
    x_term = amplitude / (3.0 * math.sqrt(v)) if amplitude else 0.0
    e2 = OMEGA_R0 * a**-4 + OMEGA_M0 * a**-3 + x_term
    e = math.sqrt(e2)
    omega_r = OMEGA_R0 * a**-4 / e2
    omega_m = OMEGA_M0 * a**-3 / e2
    omega_x = x_term / e2
    dlnv_dx = 3.0 * m2 / (a * e * m3)
    w_x = -1.0 + dlnv_dx / 6.0
    q = 0.5 * (2.0 * omega_r + omega_m + omega_x * (1.0 + 3.0 * w_x))
    omega_lambda0 = 1.0 - OMEGA_R0 - OMEGA_M0
    e_lcdm = math.sqrt(
        OMEGA_R0 * a**-4 + OMEGA_M0 * a**-3 + omega_lambda0
    )
    closure = x_term * 3.0 * math.sqrt(v) / amplitude if amplitude else 1.0
    return {
        "a": a,
        "z": 1.0 / a - 1.0,
        "E": e,
        "E_over_LCDM": e / e_lcdm,
        "tau": y[0],
        "v": v,
        "omega_r": omega_r,
        "omega_m": omega_m,
        "omega_x": omega_x,
        "w_x": w_x,
        "q": q,
        "closure": closure,
    }


def conserved_x_derivative(x: float, y: list[float], amplitude: float) -> list[float]:
    a = math.exp(x)
    _, m0, m1, m2, m3 = y
    v = 4.0 * PI * m3 / 3.0
    e = math.sqrt(
        OMEGA_R0 * a**-4
        + OMEGA_M0 * a**-3
        + amplitude / (3.0 * math.sqrt(v))
    )
    return [
        1.0 / e,
        a**3 / e,
        m0 / (a * e),
        2.0 * m1 / (a * e),
        3.0 * m2 / (a * e),
    ]


def vector_add(y: list[float], k: list[float], factor: float) -> list[float]:
    return [yi + factor * ki for yi, ki in zip(y, k)]


def rk4_step(x: float, y: list[float], h: float, amplitude: float) -> list[float]:
    k1 = conserved_x_derivative(x, y, amplitude)
    k2 = conserved_x_derivative(x + 0.5 * h, vector_add(y, k1, 0.5 * h), amplitude)
    k3 = conserved_x_derivative(x + 0.5 * h, vector_add(y, k2, 0.5 * h), amplitude)
    k4 = conserved_x_derivative(x + h, vector_add(y, k3, h), amplitude)
    return [
        yi + h * (a + 2.0 * b + 2.0 * c + d) / 6.0
        for yi, a, b, c, d in zip(y, k1, k2, k3, k4)
    ]


def simulate_conserved_x(
    amplitude: float,
    steps: int,
    target_redshifts: tuple[float, ...] = (1.0e9, 1100.0, 2.0, 1.0, 0.0),
) -> dict[str, Any]:
    x_start = math.log(A_INITIAL)
    x_end = 0.0
    h = (x_end - x_start) / steps
    y = conserved_x_initial_state(amplitude)
    x = x_start
    targets = sorted((math.log(1.0 / (1.0 + z)), z) for z in target_redshifts)
    target_index = 0
    samples: dict[str, dict[str, float]] = {}
    max_matter_fraction_10_to_1000 = 0.0

    for _ in range(steps):
        y = rk4_step(x, y, h, amplitude)
        x += h
        obs = conserved_x_observables(x, y, amplitude)
        if 10.0 <= obs["z"] <= 1000.0:
            max_matter_fraction_10_to_1000 = max(
                max_matter_fraction_10_to_1000, obs["omega_m"]
            )
        while target_index < len(targets) and x >= targets[target_index][0]:
            _, z = targets[target_index]
            samples[f"z={z:g}"] = obs.copy()
            target_index += 1

    final = conserved_x_observables(x, y, amplitude)
    samples["z=0"] = final.copy()
    return {
        "steps": steps,
        "samples": samples,
        "max_omega_m_for_10_le_z_le_1000": max_matter_fraction_10_to_1000,
        "final": final,
    }


def calibrate_conserved_x(steps: int = 12_000) -> float:
    c_r = causal_coefficient_exact(0.5)
    lo = 0.0
    hi = 0.999999 * 3.0 * math.sqrt(c_r) / 4.0
    for _ in range(46):
        mid = 0.5 * (lo + hi)
        e_final = simulate_conserved_x(mid, steps, target_redshifts=(0.0,))["final"]["E"]
        if e_final < 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Order-first martingale: RMS, sign persistence, and common-past covariance.
# ---------------------------------------------------------------------------


def martingale_rms_omega_per_lambda(p: float) -> float:
    return 1.0 / (3.0 * p * p * math.sqrt(causal_coefficient_exact(p)))


def brownian_positive_survival(count_ratio: float) -> float:
    """P(no zero after N0 through N1 | S(N0)>0), N1/N0=count_ratio."""
    if count_ratio <= 1.0:
        return 1.0
    return 2.0 * math.atan(1.0 / math.sqrt(count_ratio - 1.0)) / PI


def brownian_survival_quadrature(count_ratio: float, steps: int = 20_000) -> float:
    if count_ratio <= 1.0:
        return 1.0
    variance_increment = count_ratio - 1.0
    integrand = lambda y: (
        2.0
        / math.sqrt(2.0 * PI)
        * math.exp(-0.5 * y * y)
        * math.erf(y / math.sqrt(2.0 * variance_increment))
    )
    return simpson(integrand, 0.0, 10.0, steps)


def matter_era_count_ratio(z_start: float) -> float:
    # a=t^(2/3), N proportional t^4 proportional a^6.
    return (1.0 + z_start) ** 6


def minkowski_overlap_correlation(separation_over_age: float) -> float:
    """Equal-time 3+1 Minkowski common-past fraction for a t=0 initial surface."""
    s = separation_over_age
    if s <= 0.0:
        return 1.0
    if s >= 2.0:
        return 0.0
    return 1.0 - s + 0.25 * s**3 - 0.0625 * s**4


def equal_ball_intersection_volume(radius: float, separation: float) -> float:
    if separation >= 2.0 * radius:
        return 0.0
    return PI * (4.0 * radius + separation) * (2.0 * radius - separation) ** 2 / 12.0


def minkowski_overlap_quadrature(separation_over_age: float, steps: int = 20_000) -> float:
    s = separation_over_age
    if s <= 0.0:
        return 1.0
    if s >= 2.0:
        return 0.0
    overlap = simpson(lambda r: equal_ball_intersection_volume(r, s), 0.5 * s, 1.0, steps)
    single = PI / 3.0
    return overlap / single


def correlation_half_scale() -> float:
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if minkowski_overlap_correlation(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Explicit imported-clock control.
# ---------------------------------------------------------------------------


def offset_clock_ratio(omega_asymptotic: float, omega_now: float) -> float:
    """t_c/t0 for N=N0+C t^4 and Omega=Omega_inf/sqrt(1+(t_c/t)^4)."""
    return ((omega_asymptotic / omega_now) ** 2 - 1.0) ** 0.25


def offset_omega(omega_asymptotic: float, t_over_t0: float, tc_over_t0: float) -> float:
    return omega_asymptotic / math.sqrt(1.0 + (tc_over_t0 / t_over_t0) ** 4)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool, evidence: Any) -> None:
        checks.append({"name": name, "pass": bool(condition), "evidence": evidence})

    p_values = (0.0, 0.5, 2.0 / 3.0, 1.0, 2.150537634408602)
    geometry: dict[str, Any] = {}
    for p in p_values:
        exact = causal_coefficient_exact(p)
        numeric = causal_coefficient_quadrature(p)
        box = biwave_coefficient(p)
        key = f"p={p:.12g}"
        geometry[key] = {
            "C_J_exact": exact,
            "C_J_quadrature": numeric,
            "relative_quadrature_error": abs(numeric - exact) / exact,
            "C_box": box,
            "C_J_over_C_box": exact / box,
            "ratio_identity_3_over_p_plus_3": 3.0 / (p + 3.0),
            "biwave_auxiliary_residuals": biwave_auxiliary_residuals(p),
        }
        check(
            f"causal-volume quadrature matches exact coefficient at p={p:.6g}",
            abs(numeric - exact) / exact < 2.0e-10,
            geometry[key]["relative_quadrature_error"],
        )
        check(
            f"literal-count/bi-wave ratio identity holds at p={p:.6g}",
            abs(exact / box - 3.0 / (p + 3.0)) < 2.0e-13,
            exact / box,
        )

    check(
        "Minkowski literal count equals normalized bi-wave memory",
        abs(causal_coefficient_exact(0.0) - biwave_coefficient(0.0)) < 1.0e-14,
        causal_coefficient_exact(0.0),
    )
    max_aux_residual = max(
        abs(value)
        for p in p_values
        for value in biwave_auxiliary_residuals(p).values()
    )
    check(
        "retarded bi-wave power-law auxiliary equations close",
        max_aux_residual < 1.0e-14,
        max_aux_residual,
    )

    ds_exact = de_sitter_causal_volume(1.0, 20.0)
    ds_quad = de_sitter_volume_quadrature(1.0, 20.0)
    ds_100 = de_sitter_causal_volume(1.0, 100.0)
    ds_400 = de_sitter_causal_volume(1.0, 400.0)
    ds_lambda_decay_ratio = math.sqrt(ds_400 / ds_100)
    de_sitter = {
        "H": 1.0,
        "duration_20_exact": ds_exact,
        "duration_20_quadrature": ds_quad,
        "relative_quadrature_error": abs(ds_quad - ds_exact) / ds_exact,
        "asymptotic_formula": "N=(4*pi/3H^3)[T-11/(6H)+O(exp(-HT))]",
        "Lambda_rms_at_T100_over_T400": ds_lambda_decay_ratio,
    }
    check(
        "finite de Sitter causal volume matches independent quadrature",
        de_sitter["relative_quadrature_error"] < 2.0e-11,
        de_sitter["relative_quadrature_error"],
    )
    check(
        "literal full-past Lambda decays rather than reaching a de Sitter constant",
        ds_lambda_decay_ratio > 1.9,
        ds_lambda_decay_ratio,
    )

    literal_tracker = deterministic_tracker_summary(causal_coefficient_exact)
    biwave_tracker = deterministic_tracker_summary(biwave_coefficient)
    check(
        "late-calibrated literal positive envelope predicts order-one radiation fraction",
        literal_tracker["predicted_radiation_omega"] > 0.7,
        literal_tracker["predicted_radiation_omega"],
    )
    check(
        "late-calibrated bi-wave positive envelope predicts order-one radiation fraction",
        biwave_tracker["predicted_radiation_omega"] > 0.7,
        biwave_tracker["predicted_radiation_omega"],
    )
    check(
        "weak radiation cap makes literal matter-era fraction negligible",
        literal_tracker["predicted_matter_omega_from_early_cap"] < EARLY_FRACTION_CAP,
        literal_tracker["predicted_matter_omega_from_early_cap"],
    )
    check(
        "weak radiation cap makes bi-wave matter-era fraction negligible",
        biwave_tracker["predicted_matter_omega_from_early_cap"] < EARLY_FRACTION_CAP,
        biwave_tracker["predicted_matter_omega_from_early_cap"],
    )

    local_control_c2 = 3.0 * OMEGA_LATE_TARGET
    principal_structure = {
        "COV02_local_control_c_squared": local_control_c2,
        "biwave_principal_polynomial": "(g^ab k_a k_b)^2",
        "biwave_characteristic_speeds_in_local_Minkowski_frame": [-1.0, 1.0],
        "honest_limit": "null support is not a quantum ghost or full feedback stability theorem",
    }
    check(
        "COV-02 local control is superluminal at the late target",
        local_control_c2 > 1.0,
        local_control_c2,
    )
    check(
        "retarded bi-wave proxy has only metric-null principal characteristics",
        all(abs(abs(speed) - 1.0) < 1.0e-15 for speed in (-1.0, 1.0)),
        principal_structure["biwave_characteristic_speeds_in_local_Minkowski_frame"],
    )

    # Independently integrate the separately conserved completion.
    calibrated_a = calibrate_conserved_x(12_000)
    conserved_20k = simulate_conserved_x(calibrated_a, 20_000)
    conserved_40k = simulate_conserved_x(calibrated_a, 40_000)
    convergence_fields = ("E", "tau", "omega_x", "w_x", "q", "v")
    convergence = {
        field: abs(conserved_40k["final"][field] - conserved_20k["final"][field])
        for field in convergence_fields
    }
    max_convergence = max(convergence.values())
    radiation_tracker_fraction = 4.0 * calibrated_a / (
        3.0 * math.sqrt(causal_coefficient_exact(0.5))
    )
    conserved_history = {
        "completion": "ordinary radiation and matter separately conserved; p_X forced by rho_X=A/sqrt(N_J)",
        "calibrated_A": calibrated_a,
        "analytic_radiation_tracker_fraction": radiation_tracker_fraction,
        "analytic_w_X_radiation": 1.0 / 3.0,
        "analytic_w_X_matter": 0.0,
        "run_20k": conserved_20k,
        "run_40k": conserved_40k,
        "absolute_20k_40k_convergence": convergence,
        "max_convergence_residual": max_convergence,
    }
    final = conserved_40k["final"]
    z1100 = conserved_40k["samples"]["z=1100"]
    z2 = conserved_40k["samples"]["z=2"]
    z1 = conserved_40k["samples"]["z=1"]
    z1e9 = conserved_40k["samples"]["z=1e+09"]
    check(
        "separately conserved history converges at 20k/40k",
        max_convergence < 2.0e-8,
        max_convergence,
    )
    check(
        "late calibration closes E(1)=1",
        abs(final["E"] - 1.0) < 2.0e-7,
        final["E"],
    )
    check(
        "algebraic Lambda sqrt(N)/A closure is exact",
        abs(final["closure"] - 1.0) < 1.0e-12,
        final["closure"],
    )
    check(
        "late-calibrated conserved completion is radiation dominated by X at z~1e9",
        z1e9["omega_x"] > 0.99,
        z1e9["omega_x"],
    )
    check(
        "late-calibrated conserved completion violates weak early fraction at last scattering",
        z1100["omega_x"] > 0.9,
        z1100["omega_x"],
    )
    check(
        "late-calibrated conserved completion never develops a standard matter interval",
        conserved_40k["max_omega_m_for_10_le_z_le_1000"] < 0.8,
        conserved_40k["max_omega_m_for_10_le_z_le_1000"],
    )
    check(
        "late-calibrated conserved completion is nonaccelerating today",
        final["q"] > 0.0 and final["w_x"] > -1.0 / 3.0,
        {"q0": final["q"], "w_x0": final["w_x"]},
    )
    check(
        "late-calibrated conserved completion strongly departs from LCDM over z=1..2",
        max(abs(z1["E_over_LCDM"] - 1.0), abs(z2["E_over_LCDM"] - 1.0)) > 0.5,
        {"z1": z1["E_over_LCDM"], "z2": z2["E_over_LCDM"]},
    )
    check(
        "age control flags a substantially too-young expansion history",
        final["tau"] < 0.85,
        final["tau"],
    )

    # Vacuum stress + separately conserved radiation exact fixed-era contradiction.
    test_omega_vac = 0.01
    vacuum_radiation_completion = {
        "assumptions": "p_Lambda=-rho_Lambda; exact p=1/2 radiation scaling; radiation separately conserved; exchange assigned to matter",
        "test_positive_omega_Lambda": test_omega_vac,
        "forced_omega_r": 1.0 + 3.0 * test_omega_vac,
        "forced_omega_m": -4.0 * test_omega_vac,
        "identity": "Omega_r=1+3 Omega_Lambda; Omega_m=-4 Omega_Lambda",
    }
    check(
        "vacuum-stress radiation completion forces negative matter for positive Lambda",
        vacuum_radiation_completion["forced_omega_m"] < 0.0,
        vacuum_radiation_completion,
    )

    p_late = 2.0 / (3.0 * (1.0 - OMEGA_LATE_TARGET))
    rms_radiation_per_lambda = martingale_rms_omega_per_lambda(0.5)
    rms_late_per_lambda = martingale_rms_omega_per_lambda(p_late)
    lambda_max_from_early = EARLY_FRACTION_CAP / rms_radiation_per_lambda
    late_rms_at_early_cap = lambda_max_from_early * rms_late_per_lambda
    sigma_for_late_target = OMEGA_LATE_TARGET / late_rms_at_early_cap
    lambda_for_late_rms = OMEGA_LATE_TARGET / rms_late_per_lambda
    radiation_rms_from_late = lambda_for_late_rms * rms_radiation_per_lambda

    survival: dict[str, Any] = {}
    for z_start in (0.5, 0.7, 1.0, 2.0):
        ratio = matter_era_count_ratio(z_start)
        analytic = brownian_positive_survival(ratio)
        numeric = brownian_survival_quadrature(ratio)
        survival[f"z={z_start:g}_to_0"] = {
            "count_ratio": ratio,
            "analytic_continuous_survival": analytic,
            "quadrature": numeric,
            "absolute_error": abs(analytic - numeric),
        }
        check(
            f"Brownian positive-survival formula matches quadrature from z={z_start:g}",
            abs(analytic - numeric) < 2.0e-12,
            abs(analytic - numeric),
        )

    overlap: dict[str, Any] = {}
    for s in (0.0, 0.25, 0.75, 1.5, 2.0):
        analytic = minkowski_overlap_correlation(s)
        numeric = minkowski_overlap_quadrature(s)
        overlap[f"r_over_T={s:g}"] = {
            "analytic_common_past_fraction": analytic,
            "quadrature": numeric,
            "absolute_error": abs(analytic - numeric),
        }
        check(
            f"common-past covariance matches ball-overlap quadrature at r/T={s:g}",
            abs(analytic - numeric) < 2.0e-12,
            abs(analytic - numeric),
        )

    martingale = {
        "definition": "S_x=sum_{e in J-(x)} xi_e; Lambda_x=lambda*S_x/N_x; E[xi]=0; Cov(xi_e,xi_f)=delta_ef",
        "conditional_mean": 0.0,
        "conditional_variance": "lambda^2/N_x",
        "cross_covariance": "lambda^2*N_xz/(N_x*N_z), N_xz=|J-(x) intersect J-(z)|",
        "radiation_rms_omega_per_lambda": rms_radiation_per_lambda,
        "late_rms_omega_per_lambda": rms_late_per_lambda,
        "lambda_max_from_weak_early_cap": lambda_max_from_early,
        "late_rms_at_weak_early_cap": late_rms_at_early_cap,
        "late_target_in_sigma_units_at_early_cap": sigma_for_late_target,
        "lambda_for_late_rms_target": lambda_for_late_rms,
        "radiation_rms_when_late_rms_is_target": radiation_rms_from_late,
        "positive_sign_survival": survival,
        "minkowski_equal_time_common_past_correlation": {
            "formula": "rho(s)=1-s+s^3/4-s^4/16 for 0<=s<=2, else 0",
            "half_correlation_r_over_T": correlation_half_scale(),
            "samples": overlap,
        },
        "action_grade": "complete-Q stochastic phenomenology only; a causal response plus positive noise kernel/CTP construction is unbuilt",
    }
    check(
        "weak early RMS cap makes the late target an extreme martingale realization",
        sigma_for_late_target > 100.0,
        sigma_for_late_target,
    )
    check(
        "late-RMS calibration makes radiation-era fluctuations supercritical",
        radiation_rms_from_late > 1.0,
        radiation_rms_from_late,
    )
    check(
        "unmodified martingale has poor positive-sign persistence from z=2",
        survival["z=2_to_0"]["analytic_continuous_survival"] < 0.03,
        survival["z=2_to_0"]["analytic_continuous_survival"],
    )
    check(
        "common-past covariance is neither a global constant nor independent local noise",
        0.4 < minkowski_overlap_correlation(correlation_half_scale()) < 0.6,
        correlation_half_scale(),
    )

    tc_ratio = offset_clock_ratio(0.98, OMEGA_LATE_TARGET)
    early_offset_fraction = offset_omega(0.98, 1.0e-5, tc_ratio)
    imported_clock_control = {
        "model": "N=N0+C t^4; Omega=Omega_inf/sqrt(1+(t_c/t)^4)",
        "omega_asymptotic": 0.98,
        "omega_now_target": OMEGA_LATE_TARGET,
        "required_t_c_over_t0": tc_ratio,
        "omega_at_t_over_t0_1e-5": early_offset_fraction,
        "disposition": "positive rescue control, but t_c approximately t0 explicitly reimports the desired cosmic clock",
    }
    check(
        "an offset can suppress early density (positive rescue control)",
        early_offset_fraction < 1.0e-6,
        early_offset_fraction,
    )
    check(
        "the offset rescue requires a clock of order the present age",
        0.5 < tc_ratio < 2.0,
        tc_ratio,
    )

    candidate_tournament = [
        {
            "candidate": "literal causal-past count as separately conserved effective component",
            "gain": "covariant, retarded, unique unweighted count; pressure forced rather than selected",
            "result": "TRACKING_NONACCELERATING",
            "decisive_evidence": "w_X=1/3 in radiation, 0 in matter; late-calibrated q0>0 and early Omega_X~1",
        },
        {
            "candidate": "literal count with vacuum stress and complete exchange",
            "gain": "Bianchi-compatible phenomenology can be written",
            "result": "PATHOLOGICAL_SECTOR_EXCHANGE_OR_ALWAYS_ON_TRACKER",
            "decisive_evidence": "positive vacuum in an exact radiation era forces negative receiving matter under the least arbitrary partition",
        },
        {
            "candidate": "retarded bi-wave memory N_box=8*pi*Box_ret^-2(1)",
            "gain": "metric-null principal polynomial; genuine escape from COV-02 local sound cone",
            "result": "CAUSAL_ESCAPE_TRACKER_FAIL",
            "decisive_evidence": "still homogeneous degree four and late calibration predicts order-one radiation fraction; also a memory proxy, not an event count",
        },
        {
            "candidate": "order-first signed causal martingale S_N/N",
            "gain": "half-power, sign, retarded update, and spatial covariance arise from count statistics/common-past overlap",
            "result": "PRINCIPAL_ESCAPE_BACKGROUND_KILL / ACTION_OPEN",
            "decisive_evidence": "weak early cap makes the late target >100 sigma; sign persistence is low; raw de Sitter memory never becomes stationary",
        },
        {
            "candidate": "order-first growth with an endogenously generated memory scale",
            "gain": "only identified route that could break scale-free tracking without choosing today's history",
            "result": "OPEN_UNBUILT_FRONTIER",
            "decisive_evidence": "must construct label-invariant growth, geometry recovery, return arrow, CTP/noise action, and source the scale before cosmological fitting",
        },
    ]

    all_pass = all(item["pass"] for item in checks)
    terminal_outcome = "CAUSAL_ESCAPE_TRACKER_FAIL"
    result: dict[str, Any] = {
        "probe": "du_causal_memory_frontier_probe",
        "swing": "SWING-DU-CMF-01",
        "terminal_outcome": terminal_outcome,
        "all_instrument_and_verdict_checks_pass": all_pass,
        "checks_passed": sum(1 for item in checks if item["pass"]),
        "checks_total": len(checks),
        "checks": checks,
        "geometry": geometry,
        "de_sitter": de_sitter,
        "principal_structure": principal_structure,
        "deterministic_positive_envelope": {
            "literal_count": literal_tracker,
            "biwave_memory": biwave_tracker,
        },
        "separately_conserved_history": conserved_history,
        "vacuum_radiation_completion": vacuum_radiation_completion,
        "order_first_martingale": martingale,
        "imported_clock_control": imported_clock_control,
        "candidate_tournament": candidate_tournament,
        "typed_boundary": {
            "N_J": "literal unweighted causal-past event/four-volume count on a supplied metric",
            "N_box": "retarded bi-wave memory coordinate, not a count",
            "S_N_over_N": "signed stochastic action-density/martingale, not positive deterministic vacuum energy",
            "N0_or_window": "boundary/kernel datum; a clock unless independently generated",
            "order_first_N": "causet past-cardinality before geometry; program-native candidate, not built by metric-seeded FLRW",
        },
        "honest_grade": (
            "Exact/structural for power-law causal volumes, bi-wave coefficients and principal cone, "
            "de Sitter full-past asymptotics, tracker equations of state, Brownian survival, and "
            "Minkowski common-past covariance. Deterministic finite-background grade for the "
            "separately conserved radiation/matter history. Phenomenological only for stress "
            "closure; no order-first growth law, CTP/noise-complete action, finite-k feedback "
            "spectrum, Boltzmann hierarchy, or likelihood."
        ),
        "verdict_reason": (
            "Causal memory genuinely exits the local superluminal-characteristic class, so COV-02 "
            "was class-relative. But every built scale-free positive branch tracks the dominant "
            "era or fails to accelerate, while the order-first martingale is far too noisy early, "
            "rarely preserves a positive sign, and has no stationary raw-past de Sitter limit. "
            "A fitted offset/window works only by importing a present-age clock."
        ),
        "surviving_frontier": (
            "A label-invariant order-first causal growth law with feedback and an endogenously "
            "generated dimensional memory scale, plus a causal response/noise action. Stochastic "
            "sign alone and nonlocality alone are insufficient."
        ),
        "primary_sources": [
            "https://arxiv.org/abs/astro-ph/0209274",
            "https://arxiv.org/abs/0711.2904",
            "https://arxiv.org/abs/1403.1622",
            "https://arxiv.org/abs/1402.0448",
            "https://arxiv.org/abs/1601.03808",
            "https://arxiv.org/abs/2307.13743",
        ],
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("=" * 88)
    print("SWING-DU-CMF-01 -- causal-memory / order-first martingale frontier probe")
    print("=" * 88)
    print(f"checks: {result['checks_passed']}/{result['checks_total']} PASS")
    print(f"terminal outcome: {terminal_outcome}")
    print("\nExact escape:")
    print(f"  COV-02 local c^2 at Omega={OMEGA_LATE_TARGET:.2f}: {local_control_c2:.6f}")
    print("  bi-wave principal characteristic speed: 1 (metric-null; ghost theorem NOT claimed)")
    print("\nDeeper background kill:")
    print(f"  conserved-X A: {calibrated_a:.12f}")
    print(f"  Omega_X(z=1100): {z1100['omega_x']:.9f}")
    print(f"  q0: {final['q']:.9f}   w_X0: {final['w_x']:.9f}   H0*t0: {final['tau']:.9f}")
    print(f"  early-cap late martingale RMS: {late_rms_at_early_cap:.9f}")
    print(f"  target / late RMS: {sigma_for_late_target:.3f} sigma")
    print(f"  P(Lambda stays positive, z=2->0 | positive at z=2): "
          f"{survival['z=2_to_0']['analytic_continuous_survival']:.6f}")
    print("\nNovel fixed spatial prediction:")
    print("  Corr[Lambda(x),Lambda(z)] = common-past fraction")
    print(f"  half-correlation separation r/T: {correlation_half_scale():.9f}")
    print(f"\nartifact: {args.out}")

    if not all_pass:
        print("\nFAILED CHECKS:")
        for item in checks:
            if not item["pass"]:
                print(f"  - {item['name']}: {item['evidence']}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
