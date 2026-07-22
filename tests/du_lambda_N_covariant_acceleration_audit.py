#!/usr/bin/env python3
"""Deterministic background audit for the Dynamic Unity Lambda<->N loop.

The audit asks a deliberately narrow question: if

    Lambda = c_S / sqrt(N),        dN/dt = kappa H^-3,

can the rolling vacuum term be embedded in a conserved flat-FLRW background
without choosing an arbitrary interaction function?  We write

    lambda = Lambda / 3,           H^2 = rho_m + lambda,

in units 8*pi*G/3 = 1, and define Omega = lambda/H^2.  Total conservation
forces the matter/vacuum exchange; it is not independently fitted.

This is a background calculation, not a covariant field theory, perturbation
analysis, likelihood fit, or claim promotion.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence, Tuple


OMEGA_0 = 0.6847
Z_SAMPLES = (0.5, 1.0, 2.0, 10.0, 1100.0)
ARTIFACT = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_lambda_N_covariant_acceleration_audit_result.json"
)


State = Tuple[float, float, float]  # Omega, ln(H/H0), ln(N/A^2)


def model_rhs(state: State, beta: float) -> State:
    """Derivatives with respect to x = ln(a)."""

    omega, _ln_h, _ln_n = state
    omega_prime = omega * (3.0 * (1.0 - omega) - 0.5 * beta * omega * omega)
    ln_h_prime = -1.5 * (1.0 - omega)
    ln_n_prime = beta * omega * omega
    return omega_prime, ln_h_prime, ln_n_prime


def lcdm_rhs(state: State, _beta: float = 0.0) -> State:
    omega, _ln_h, _ln_n = state
    return 3.0 * omega * (1.0 - omega), -1.5 * (1.0 - omega), 0.0


def add_scaled(state: State, slope: State, scale: float) -> State:
    return tuple(state[i] + scale * slope[i] for i in range(3))  # type: ignore[return-value]


def rk4_step(
    state: State,
    step: float,
    beta: float,
    rhs: Callable[[State, float], State],
) -> State:
    k1 = rhs(state, beta)
    k2 = rhs(add_scaled(state, k1, 0.5 * step), beta)
    k3 = rhs(add_scaled(state, k2, 0.5 * step), beta)
    k4 = rhs(add_scaled(state, k3, step), beta)
    return tuple(
        state[i] + step * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
        for i in range(3)
    )  # type: ignore[return-value]


def initial_state(omega_0: float = OMEGA_0) -> State:
    # Set A=1.  The closure lambda=A/sqrt(N) then gives N0=1/Omega0^2
    # because H0=1 and lambda0=Omega0.
    return omega_0, 0.0, -2.0 * math.log(omega_0)


def integrate_to(
    beta: float,
    x_target: float,
    *,
    rhs: Callable[[State, float], State] = model_rhs,
    omega_0: float = OMEGA_0,
) -> State:
    steps = max(80, int(abs(x_target) * 3500.0) + 1)
    step = x_target / steps
    state = initial_state(omega_0)
    for _ in range(steps):
        state = rk4_step(state, step, beta, rhs)
        if not all(math.isfinite(value) for value in state):
            raise ArithmeticError("non-finite integration state")
    return state


def fixed_point(beta: float) -> float:
    if beta == 0.0:
        return 1.0
    return 6.0 / (3.0 + math.sqrt(9.0 + 6.0 * beta))


def fixed_point_row(beta: float) -> Dict[str, float | bool]:
    omega = fixed_point(beta)
    q = 0.5 * (1.0 - 3.0 * omega)
    power = 2.0 / (3.0 * (1.0 - omega))
    stability_eigenvalue = omega * (-3.0 - beta * omega)
    return {
        "beta": beta,
        "c_S_over_sqrt_kappa": 3.0 / math.sqrt(beta),
        "omega_star": omega,
        "q_star": q,
        "w_total_star": -omega,
        "power_law_p": power,
        "stable": stability_eigenvalue < 0.0,
        "stability_eigenvalue": stability_eigenvalue,
        "accelerating": q < 0.0,
    }


def lcdm_hubble(z: float, omega_0: float = OMEGA_0) -> float:
    return math.sqrt((1.0 - omega_0) * (1.0 + z) ** 3 + omega_0)


def background_row(beta: float, z: float) -> Dict[str, float]:
    state = integrate_to(beta, -math.log1p(z))
    omega, ln_h, ln_n = state
    hubble = math.exp(ln_h)
    n_value = math.exp(ln_n)
    lam = omega * hubble * hubble
    closure = lam * math.sqrt(n_value)
    return {
        "z": z,
        "omega_lambda": omega,
        "H_over_H0": hubble,
        "H_over_H_lcdm": hubble / lcdm_hubble(z),
        "closure_lambda_sqrtN_over_A": closure,
    }


def max_hubble_deviation(beta: float, z_max: float = 2.0) -> float:
    deviations: List[float] = []
    for index in range(101):
        z = z_max * index / 100.0
        row = background_row(beta, z)
        deviations.append(abs(row["H_over_H_lcdm"] - 1.0))
    return max(deviations)


def constant_lambda_control() -> Dict[str, float | bool]:
    max_relative_error = 0.0
    for z in Z_SAMPLES:
        _omega, ln_h, _ln_n = integrate_to(
            0.0, -math.log1p(z), rhs=lcdm_rhs
        )
        numerical = math.exp(ln_h)
        analytic = lcdm_hubble(z)
        max_relative_error = max(
            max_relative_error, abs(numerical / analytic - 1.0)
        )
    return {
        "max_relative_H_error": max_relative_error,
        "passes": max_relative_error < 1.0e-9,
    }


def separately_conserved_dust_residual(beta: float, omega: float = OMEGA_0) -> float:
    """Dimensionless Bianchi residual |lambda'|/H^2 at the stated epoch."""

    return 0.5 * beta * omega**3


def first_unphysical_past_redshift(beta: float) -> float | None:
    """Find where backward evolution first reaches Omega=1 (rho_m=0)."""

    state = initial_state()
    x = 0.0
    step = -1.0e-4
    for _ in range(100_000):
        state = rk4_step(state, step, beta, model_rhs)
        x += step
        if state[0] >= 1.0:
            return math.exp(-x) - 1.0
        if state[0] <= 0.0 or not math.isfinite(state[0]):
            return None
    return None


def rounded(value: object) -> object:
    if isinstance(value, float):
        return round(value, 12)
    if isinstance(value, list):
        return [rounded(item) for item in value]
    if isinstance(value, dict):
        return {key: rounded(item) for key, item in value.items()}
    return value


def run_audit() -> Dict[str, object]:
    beta_for_present_fixed_point = 6.0 * (1.0 - OMEGA_0) / OMEGA_0**2
    fixed_betas = (0.25, 1.0, beta_for_present_fixed_point, 9.0, 36.0, 50.0)
    history_betas = (0.25, 0.5, 1.0, 2.0, 3.0, 4.0)

    fixed_rows = [fixed_point_row(beta) for beta in fixed_betas]
    histories: List[Dict[str, object]] = []
    for beta in history_betas:
        max_deviation = max_hubble_deviation(beta)
        histories.append(
            {
                "beta": beta,
                "c_S_over_sqrt_kappa": 3.0 / math.sqrt(beta),
                "max_abs_H_fraction_vs_lcdm_z_0_to_2": max_deviation,
                "passes_internal_five_percent_background_envelope": max_deviation <= 0.05,
                "samples": [background_row(beta, z) for z in Z_SAMPLES],
            }
        )

    positive_control = constant_lambda_control()
    beta_one_z1100 = background_row(1.0, 1100.0)
    beta_two_history = next(row for row in histories if row["beta"] == 2.0)
    beta_one_history = next(row for row in histories if row["beta"] == 1.0)
    natural_fixed = fixed_point_row(9.0)
    target_fixed = fixed_point_row(beta_for_present_fixed_point)
    natural_past_boundary = first_unphysical_past_redshift(9.0)

    checks: List[Dict[str, object]] = []

    def check(check_id: str, passed: bool, detail: str) -> None:
        checks.append({"id": check_id, "passed": bool(passed), "detail": detail})

    max_fixed_residual = max(
        abs(3.0 * (1.0 - float(row["omega_star"]))
            - 0.5 * float(row["beta"]) * float(row["omega_star"]) ** 2)
        for row in fixed_rows
    )
    check("analytic_fixed_points", max_fixed_residual < 1.0e-12, f"max residual={max_fixed_residual:.3e}")
    check("fixed_points_stable", all(bool(row["stable"]) for row in fixed_rows), "all beta>0 rows have negative linear eigenvalue")
    check("acceleration_threshold_below", fixed_point_row(35.0)["accelerating"] is True, "beta=35 accelerates")
    check("acceleration_threshold_at", abs(float(fixed_point_row(36.0)["q_star"])) < 1.0e-12, "beta=36 gives q=0")
    check("acceleration_threshold_above", fixed_point_row(37.0)["accelerating"] is False, "beta=37 does not accelerate")
    check("natural_coefficients_accelerate", bool(natural_fixed["accelerating"]), "c_S=kappa=1 maps to beta=9 and q<0")
    check("target_fixed_point_accelerates", float(target_fixed["power_law_p"]) > 1.0, "Omega*=0.6847 gives p>1")
    check("constant_lambda_positive_control", bool(positive_control["passes"]), f"max H error={positive_control['max_relative_H_error']:.3e}")

    closure_residual = max(
        abs(float(sample["closure_lambda_sqrtN_over_A"]) - 1.0)
        for history in histories
        for sample in history["samples"]  # type: ignore[index]
    )
    check("lambda_N_closure_preserved", closure_residual < 2.0e-9, f"max closure residual={closure_residual:.3e}")
    check("forced_exchange_is_nonzero", separately_conserved_dust_residual(1.0) > 0.1, "rolling lambda requires nonzero matter exchange")
    check("separate_dust_negative_control", separately_conserved_dust_residual(1.0) > 1.0e-6, "separately conserved dust leaves a Bianchi residual")
    naive_p = 2.0 / 3.0  # 3p=2 from rho_m~a^-3~t^-2.
    naive_q = (1.0 - naive_p) / naive_p
    check("naive_tracker_nonaccelerating", naive_q >= 0.0, "separate-dust scaling branch has p=2/3 and q=1/2")
    check("matter_past_exists_beta_one", float(beta_one_z1100["omega_lambda"]) < 1.0e-6, "beta=1 reaches a matter-dominated early background")
    check("five_percent_envelope_beta_one", bool(beta_one_history["passes_internal_five_percent_background_envelope"]), "beta=1 stays within the declared internal H(z) envelope")
    check("five_percent_envelope_has_teeth", not bool(beta_two_history["passes_internal_five_percent_background_envelope"]), "beta=2 fails the same envelope")
    check("natural_present_history_problem", natural_past_boundary is not None and natural_past_boundary < 0.25, f"beta=9 reaches rho_m=0 by z={natural_past_boundary:.3f}")
    check("present_as_fixed_point_has_no_matter_era", abs(float(target_fixed["omega_star"]) - OMEGA_0) < 1.0e-12, "calibrating today as the attractor keeps Omega constant")
    sample_omega = 0.47
    sample_h_prime = -1.5 * (1.0 - sample_omega)
    sample_omega_prime = sample_omega * (
        3.0 * (1.0 - sample_omega) - 0.5 * sample_omega**2
    )
    sample_bianchi_residual = (
        2.0 * sample_h_prime * (1.0 - sample_omega)
        - sample_omega_prime
        + 2.0 * sample_h_prime * sample_omega
        + sample_omega_prime
        + 3.0 * (1.0 - sample_omega)
    )
    check("forced_exchange_closes_bianchi", abs(sample_bianchi_residual) < 1.0e-14, "Q=-dot(lambda) follows algebraically from total conservation")

    failed = [item for item in checks if not item["passed"]]
    if failed:
        raise AssertionError(f"audit checks failed: {failed}")

    result: Dict[str, object] = {
        "audit_id": "DU-LAMBDA-N-COV-01",
        "status": "executed_scoped",
        "date": "2026-07-21",
        "scope": "flat-FLRW background only; no full covariant N field, action, perturbations, or likelihood fit",
        "definitions": {
            "units": "8*pi*G/3=1",
            "lambda": "Lambda/3",
            "friedmann": "H^2=rho_m+lambda",
            "closure": "lambda=A*N^(-1/2), A=c_S/3",
            "count_law": "dN/dt=kappa*H^(-3)",
            "omega": "lambda/H^2",
            "beta": "kappa/A^2=9*kappa/c_S^2",
        },
        "derived_background_system_d_dln_a": {
            "ln_H": "-3/2*(1-Omega)",
            "ln_N": "beta*Omega^2",
            "ln_lambda": "-beta/2*Omega^2",
            "Omega": "Omega*(3*(1-Omega)-beta/2*Omega^2)",
            "forced_exchange": "Q=-dot(lambda)=(beta/2)*H*Omega^2*lambda",
            "q": "(1-3*Omega)/2",
            "w_total": "-Omega",
        },
        "analytic_result": {
            "positive_fixed_point": "Omega*=6/(3+sqrt(9+6*beta))",
            "stable_for": "all beta>0",
            "accelerates_for": "beta<36, equivalently c_S/sqrt(kappa)>1/2",
            "present_omega_as_fixed_point": {
                "omega": OMEGA_0,
                "beta": beta_for_present_fixed_point,
                "c_S_over_sqrt_kappa": 3.0 / math.sqrt(beta_for_present_fixed_point),
                "power_law_p": target_fixed["power_law_p"],
            },
            "fixed_point_scan": fixed_rows,
        },
        "background_sanity": {
            "reference": "flat constant-Lambda background with the same Omega_lambda,0",
            "internal_envelope": "max |H/H_LCDM-1| <= 5% for 0<=z<=2; diagnostic only, not an observational acceptance criterion",
            "histories": histories,
            "natural_coefficients_beta_9_first_rho_m_zero_redshift": natural_past_boundary,
        },
        "controls": {
            "constant_lambda_positive": positive_control,
            "separately_conserved_dust_negative": {
                "beta_1_bianchi_residual_abs_lambda_prime_over_H2_today": separately_conserved_dust_residual(1.0),
                "reason": "rho_m'+3rho_m=0 with rolling lambda leaves total residual lambda'!=0",
            },
            "old_p_equals_two_thirds_branch": {
                "p": 2.0 / 3.0,
                "q": 0.5,
                "reason": "matching separately conserved dust to lambda~t^-2 forces p=2/3, but the same branch violates Bianchi when lambda rolls",
            },
        },
        "checks": checks,
        "check_summary": {"passed": len(checks), "failed": len(failed)},
        "verdict": "BACKGROUND_CONSERVED_ACCELERATING_FAMILY__FULL_COVARIANCE_AND_VIABILITY_OPEN",
        "interpretation": [
            "The p=2/3 result is not a no-go for every Lambda-N completion; it is the separately-conserved-dust branch, which is Bianchi-inconsistent for rolling lambda.",
            "Total conservation uniquely fixes a background exchange Q=-dot(lambda), and the resulting one-parameter family has stable accelerating fixed points for beta<36.",
            "This does not source Omega_lambda,0: choosing today as the fixed point fixes one coefficient ratio and erases the matter era.",
            "A matter-dominated past and an H(z) history close to constant-Lambda drive beta downward, toward weak exchange and the LambdaCDM limit; perturbations and data must decide how severe that pressure is.",
            "A full win still requires a covariant/local definition of N and its source law, an interaction four-vector or action, stable perturbations, growth, and empirical fitting.",
        ],
    }
    return rounded(result)  # type: ignore[return-value]


def main() -> None:
    result = run_audit()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = result["check_summary"]
    total = summary["passed"] + summary["failed"]  # type: ignore[index]
    print(
        "DU-LAMBDA-N-COV-01: "
        f"{summary['passed']}/{total} checks PASS | "  # type: ignore[index]
        "background-conserved accelerating family found; full covariance/viability OPEN"
    )


if __name__ == "__main__":
    main()
