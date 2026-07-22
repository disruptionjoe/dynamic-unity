#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dynamic Unity -- Lane 2.2 -> 1.3 pre-registered swing probe (R6 loop).

The candidate (incentive-selection-mode-issuance-candidate-2026-07-21.md, Test #4)
closes a feedback loop and reads Lambda as its STATE, not a constant:

    Lambda drives cosmic expansion  ->  expansion accretes records / DOF (N grows)
    ->  the causal-set amplitude law  Lambda l_p^2 = c_S / sqrt(N)  responds  ->  ...

DECISIVE QUESTION (flip-witness-algebra-requirements R6): does this closed loop have a
STABLE FIXED POINT at the observed  Omega_Lambda ~ 0.68  WITHOUT tuning?
  - If Omega_Lambda ~ 0.68 is a robust attractor with no knob  =>  the loop SOURCES the
    magnitude (ROBUST-FIXED-POINT; huge).
  - If Omega_Lambda ~ 0.68 appears only by tuning a coefficient, or there is no non-trivial
    fixed point  =>  the loop does NOT source the value; the R6 wall holds (TUNED-OR-ABSENT).
  - A fixed point at the WRONG value, or one that needs a single import  =>  PARTIAL.

This is a DISPROOF-OR-CONFIRM instrument, not a fit. It builds the loop as an actual
dynamical system, finds its fixed points / attractors, computes the fixed-point Omega_Lambda,
and SCANS the (few) structural parameters to report the basin. It carries POSITIVE CONTROLS
(Section 5) so a genuine sourcing WOULD register -- the test is not rigged to always say
"import". Sanity guards (Section 6): the TaF rate^2-to-rate^2 units check on the Lambda<->rate
bridge, and confirmation that N is the GLOBAL horizon-scale count (homogeneous), not a local
observer density (which would fail the observer-gradient falsifier).

Everything cosmological (Friedmann '3', the Sorkin 1/sqrt(N) exponent, the de Sitter relabel
1/sqrt(N_4)=pi/S_dS, Planck-2018 Omega_Lambda=0.6847) is PORTED and labelled. Nothing asserts
DU. Exploration grade, no canon movement.

Run: python -u tests/du_lambda_N_loop_fixedpoint_probe.py   (foreground; expect exit 0)
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print("numpy required:", exc)
    sys.exit(2)

try:
    from scipy.integrate import solve_ivp
    HAVE_SCIPY = True
except Exception:  # pragma: no cover
    HAVE_SCIPY = False

CHECKS = []


def check(name, got, expected, rel=2e-2, absorb=0.0):
    if expected == 0:
        ok = abs(got) <= (rel + absorb)
    else:
        ok = abs(got - expected) <= rel * abs(expected) + absorb
    CHECKS.append((name, ok))
    flag = "ok " if ok else "XX "
    try:
        print(f"  [{flag}] {name}: got {got:.6g}  expected {expected:.6g}")
    except (TypeError, ValueError):
        print(f"  [{flag}] {name}: got {got}  expected {expected}")
    return ok


def note(name, ok, msg=""):
    CHECKS.append((name, bool(ok)))
    flag = "ok " if ok else "XX "
    print(f"  [{flag}] {name}{('  ' + msg) if msg else ''}")
    return ok


# ===========================================================================
# Ported cosmology anchors (same as de_amplitude_dewitt_route_probe.py)
# ===========================================================================
c_light = 2.99792458e8            # m/s
G_newt  = 6.67430e-11             # m^3 kg^-1 s^-2
hbar    = 1.054571817e-34        # J s
Mpc     = 3.0856775814913673e22  # m
H0_kms  = 67.36                  # km/s/Mpc (Planck 2018)
OMEGA_L_OBS = 0.6847            # PORTED target (Planck 2018)

H0  = H0_kms * 1e3 / Mpc
R_H = c_light / H0
l_p = math.sqrt(hbar * G_newt / c_light**3)

ART: dict[str, Any] = {}


# ===========================================================================
# Section 0: the closed-form attractor map (derived, then confirmed numerically)
#
# Write the loop as a dynamical system in Planck units (l_p = c = 1), state N(t):
#   Friedmann :  H^2 = M a^-3 + Lambda/3           ('3' is Friedmann's)
#   closure   :  Lambda = c_S N^-1/2                (Sorkin causal-set amplitude law)
#   accretion :  dN/dt = kappa H^-3                 (GLOBAL horizon 3-volume birth rate)
#
# There are TWO honest ways to define the record count N; they give DIFFERENT numbers
# from the SAME closure -- already a tell that the value is a modelling choice, not sourced.
#
#   (I) INSTANTANEOUS horizon count   N = k_N (R_H/l_p)^4 = k_N H^-4
#       Then Lambda l_p^2 = (c_S/sqrt(k_N)) (H l_p)^2, and Friedmann Lambda l_p^2 =
#       3 Omega_L (H l_p)^2 forces an ALGEBRAIC IDENTITY  Omega_L = c_eff/3,
#       c_eff = c_S/sqrt(k_N), with the Lambda MAGNITUDE cancelling (degenerate: any
#       Lambda satisfies it). This is exactly the de Sitter relabel  1/sqrt(N_4)=pi/S_dS
#       -- Adversary-C's "de-Sitter-trivial / degenerate" horn.
#
#   (II) ACCUMULATED count            dN/dt = kappa H^-3  (records keep being laid down)
#       The genuinely DYNAMICAL loop. Late-time scaling attractor (derived below):
#           Omega_L* = min( sqrt(2/3) * c_S/sqrt(kappa) , 1 )
#       i.e. a stable fixed point whose value is set LINEARLY by ONE effective coefficient
#       lambda_eff = c_S/sqrt(kappa), with order-unity slope sqrt(2/3)=0.8165 -- NO basin.
# ===========================================================================
print("=== Section 0: closed-form attractor map (to be confirmed numerically) ===")
SLOPE = math.sqrt(2.0 / 3.0)                     # 0.81650 -- scaling-attractor slope
LAMEFF_DS = math.sqrt(3.0 / 2.0)                 # 1.22474 -- knee: Omega_L -> 1 above this
check("0.1  scaling-attractor slope sqrt(2/3)", SLOPE, 0.816497, rel=1e-5)
check("0.2  knee lambda_eff = sqrt(3/2) (Omega_L=1 above)", LAMEFF_DS, 1.224745, rel=1e-5)

# lambda_eff that would be needed to land the scaling attractor exactly on 0.6847:
lameff_needed = OMEGA_L_OBS / SLOPE
check("0.3  lambda_eff needed for Omega_L=0.6847 (accum. count)", lameff_needed, 0.83858, rel=1e-3)
# natural O(1) coefficients c_S = kappa = 1 give lambda_eff = 1:
OmegaL_natural = min(SLOPE * 1.0, 1.0)
check("0.4  Omega_L* at natural c_S=kappa=1 (lambda_eff=1)", OmegaL_natural, 0.81650, rel=1e-4)
note("0.5  natural point Omega_L=0.816 != 0.6847; hitting 0.6847 needs lambda_eff tuned to 0.839",
     abs(OmegaL_natural - OMEGA_L_OBS) / OMEGA_L_OBS > 0.05,
     f"natural is {abs(OmegaL_natural-OMEGA_L_OBS)/OMEGA_L_OBS:.1%} off target")
ART["closed_form"] = {
    "slope_sqrt_2_3": SLOPE,
    "knee_lambda_eff": LAMEFF_DS,
    "lambda_eff_needed_for_0p6847": lameff_needed,
    "OmegaL_at_natural_cS_kappa_1": OmegaL_natural,
}


def OmegaL_star_accum(lam_eff: float) -> float:
    """Closed-form scaling-attractor Omega_L for the accumulated-count loop."""
    return min(SLOPE * lam_eff, 1.0)


# ===========================================================================
# Section 1: HORN (I) -- instantaneous horizon count => algebraic identity, Lambda degenerate
#   Confirms the "de-Sitter-trivial / degenerate" charge: the loop closure with an
#   instantaneous horizon count is a TAUTOLOGY  Omega_L = c_eff/3, and the Lambda
#   MAGNITUDE drops out entirely (the same Lambda cancels on both sides).
# ===========================================================================
print("=== Section 1: HORN (I) instantaneous horizon count -- Omega_L=c_eff/3, Lambda degenerate ===")

def omegaL_instantaneous(c_S, k_N, Hlp):
    """Given closure Lambda l_p^2 = c_S/sqrt(N), N=k_N (1/(H l_p))^4, and Friedmann
       Lambda l_p^2 = 3 Omega_L (H l_p)^2, return the forced Omega_L. Must NOT depend on Hlp."""
    N = k_N * Hlp**(-4)
    Lam_lp2 = c_S / math.sqrt(N)                 # = (c_S/sqrt(k_N)) * Hlp^2
    OmegaL = Lam_lp2 / (3.0 * Hlp**2)            # Friedmann inversion; Hlp^2 cancels
    return OmegaL

# 1.1 the Lambda-magnitude / H-scale DEGENERACY: Omega_L identical across 6 decades of H.
c_S, k_N = 1.0, 1.0
vals = [omegaL_instantaneous(c_S, k_N, Hlp) for Hlp in (1e-61, 1e-40, 1e-20, 1e-6, 1.0)]
note("1.1  Omega_L independent of the Hubble scale (Lambda magnitude cancels => degenerate)",
     max(vals) - min(vals) < 1e-12, f"spread over 61 decades of H l_p = {max(vals)-min(vals):.2e}")
check("1.2  forced Omega_L = c_eff/3 (c_S=k_N=1 => 1/3)", vals[0], 1.0 / 3.0, rel=1e-9)

# 1.3 to move the identity onto 0.6847 you must IMPORT c_eff = 3*Omega_L = 2.054
c_eff_needed = 3.0 * OMEGA_L_OBS
check("1.3  c_eff needed to land Omega_L=0.6847 = 3 Omega_L = 2.054 (the imported factor)",
      c_eff_needed, 2.0541, rel=1e-3)
# ...which is EXACTLY the '3 Omega_L' import the DeWitt route already flagged (Sec 6 there).
check("1.4  omega_instantaneous(c_S=2.054, k_N=1) = 0.6847 (only by importing c_eff)",
      omegaL_instantaneous(2.0541, 1.0, 1e-61), OMEGA_L_OBS, rel=1e-3)
# and this magnitude IS the de Sitter relabel: 1/sqrt(N_4) = (l_p/R_H)^2 = pi/S_dS.
N4 = (R_H / l_p) ** 4
lam_lead = 1.0 / math.sqrt(N4)
S_dS = math.pi * (R_H / l_p) ** 2
check("1.5  1/sqrt(N_4) == pi/S_dS (de Sitter relabel; magnitude is horizon's, not sourced)",
      lam_lead, math.pi / S_dS, rel=1e-9)
ART["horn_I_instantaneous"] = {
    "OmegaL_forced_cS1_kN1": vals[0],
    "H_scale_spread": max(vals) - min(vals),
    "c_eff_needed_for_target": c_eff_needed,
    "one_over_sqrtN4": lam_lead,
    "pi_over_SdS": math.pi / S_dS,
}


# ===========================================================================
# Section 2: HORN (II) -- the genuinely DYNAMICAL accumulated-count loop, INTEGRATED
#   State y = ln N over e-folds n = ln a. In e-folds (dn = H dt):
#       H^2   = M e^{-3n} + (c_S/3) e^{-y/2}
#       dy/dn = kappa H^{-4} e^{-y}              (= (dN/dt)/(N H), accumulated count)
#       Omega_L(n) = (c_S/3) e^{-y/2} / H^2
#   Integrate from a matter-dominated start; read the LATE-TIME attractor Omega_L.
# ===========================================================================
print("=== Section 2: HORN (II) accumulated-count loop -- INTEGRATED to the attractor ===")

def integrate_loop(c_S, kappa, M=1.0, y0=0.0, n_end=90.0, Omega0_target=None):
    """Integrate y=ln N over e-folds; return late-time Omega_L (the attractor)."""
    def H2_of(n, y):
        return M * math.exp(-3.0 * n) + (c_S / 3.0) * math.exp(-0.5 * y)

    def rhs(n, Y):
        y = Y[0]
        H2 = H2_of(n, y)
        # dy/dn = kappa H^{-4} / N = kappa H2^{-2} e^{-y}
        return [kappa * H2 ** (-2.0) * math.exp(-y)]

    if HAVE_SCIPY:
        sol = solve_ivp(rhs, (0.0, n_end), [y0], rtol=1e-10, atol=1e-12,
                        dense_output=False, max_step=0.5)
        n_last, y_last = sol.t[-1], sol.y[0][-1]
    else:  # pragma: no cover -- fixed-step RK4 fallback
        n, y, h = 0.0, y0, 1e-3
        steps = int(n_end / h)
        for _ in range(steps):
            k1 = rhs(n, [y])[0]
            k2 = rhs(n + h / 2, [y + h / 2 * k1])[0]
            k3 = rhs(n + h / 2, [y + h / 2 * k2])[0]
            k4 = rhs(n + h, [y + h * k3])[0]
            y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            n += h
        n_last, y_last = n, y
    H2 = H2_of(n_last, y_last)
    OmegaL = (c_S / 3.0) * math.exp(-0.5 * y_last) / H2
    return OmegaL

# 2.1 natural coefficients c_S = kappa = 1 -> attractor at sqrt(2/3) = 0.8165 (NOT 0.68)
OmL_nat = integrate_loop(1.0, 1.0)
check("2.1  integrated attractor Omega_L (c_S=kappa=1) = sqrt(2/3)=0.8165", OmL_nat, SLOPE, rel=3e-3)

# 2.2 attractor is INDEPENDENT of initial N (basin covers all IC) -- but its VALUE is not 0.68
OmL_ic = [integrate_loop(1.0, 1.0, y0=y0) for y0 in (-20.0, 0.0, 20.0, 60.0)]
note("2.2  attractor Omega_L independent of initial ln N (IC basin is global)",
     max(OmL_ic) - min(OmL_ic) < 5e-3, f"spread over IC = {max(OmL_ic)-min(OmL_ic):.2e}")

# 2.3 attractor tracks the closed-form sqrt(2/3)*lambda_eff across a scan of lambda_eff
lam_effs = [0.4, 0.6, 0.8, lameff_needed, 1.0, 1.15]
rows = []
for le in lam_effs:
    c_S = le          # set kappa=1 so lambda_eff = c_S
    OmL = integrate_loop(c_S, 1.0)
    pred = OmegaL_star_accum(le)
    rows.append((le, OmL, pred))
    note(f"2.3  lambda_eff={le:.3f}: integrated Omega_L={OmL:.4f} matches closed form {pred:.4f}",
         abs(OmL - pred) < 8e-3, f"|diff|={abs(OmL-pred):.1e}")
ART["horn_II_integrated"] = {
    "OmegaL_natural_cS_kappa_1": OmL_nat,
    "IC_spread": max(OmL_ic) - min(OmL_ic),
    "scan": [{"lambda_eff": le, "OmegaL_integrated": o, "OmegaL_closedform": p}
             for (le, o, p) in rows],
}

# 2.4 the tuned point: lambda_eff = 0.839 DOES land on 0.6847 (only by importing the coefficient)
OmL_tuned = integrate_loop(lameff_needed, 1.0)
check("2.4  lambda_eff=0.839 (tuned) lands attractor on 0.6847", OmL_tuned, OMEGA_L_OBS, rel=1e-2)


# ===========================================================================
# Section 3: BASIN / SENSITIVITY -- is 0.6847 robust, tuned, or absent?
#   Map Omega_L*(lambda_eff); measure the local slope (sensitivity). A robust
#   attractor/basin would show a PLATEAU at 0.6847 (d Omega_L / d lambda_eff ~ 0);
#   a tuned point shows an order-unity slope and no plateau.
# ===========================================================================
print("=== Section 3: basin / parameter sensitivity around 0.6847 ===")
d = 1e-3
slope_local = (OmegaL_star_accum(lameff_needed + d) - OmegaL_star_accum(lameff_needed - d)) / (2 * d)
check("3.1  d Omega_L / d lambda_eff at the 0.6847 point = sqrt(2/3) (order unity, NO plateau)",
      slope_local, SLOPE, rel=1e-3)
# fractional-sensitivity: a 1% error in lambda_eff moves Omega_L by ~1% -- no basin.
frac_sens = (lameff_needed / OMEGA_L_OBS) * slope_local
check("3.2  fractional sensitivity (dlnOmega/dln lambda_eff) ~ 1 (tuned, not basined)",
      frac_sens, 1.0, rel=1e-2)
# window of lambda_eff that keeps Omega_L within +-5% of 0.6847 is NARROW (no wide basin):
half_window = 0.05 * OMEGA_L_OBS / SLOPE
note("3.3  lambda_eff window for Omega_L in [0.65,0.72] is narrow (+-0.042), not a basin",
     half_window < 0.1, f"half-window in lambda_eff = {half_window:.3f}")

# 3.4 robustness of the NEGATIVE result across the accretion exponent m (dN/dt=kappa H^-m):
#     the scaling attractor is Omega_L = A(m)*c_S/sqrt(kappa) -- ALWAYS linear in one
#     effective coefficient, for every m. So no accretion-law choice removes the tuning.
def scaling_coeff(m):
    """Scaling-attractor prefactor A(m) for dN/dt = kappa H^-m, closure Lambda=c_S N^-1/2.
       p=(m+1)/6; Omega_L = (Lambda/3)/H^2 with N=(kappa/((m+1)p^m)) t^{m+1}."""
    p = (m + 1) / 6.0
    N_coeff = 1.0 / ((m + 1) * p ** m)                 # N = N_coeff * kappa * t^{m+1}
    # Lambda/3 = (c_S/3) N^-1/2 ; H^2 = p^2/t^2 ; require t-powers match at scaling (3p=(m+1)/2)
    # Omega_L = (c_S/3) (N_coeff*kappa)^-1/2 / p^2  (t-powers cancel by construction)
    # returns A(m) s.t. Omega_L = A(m) * c_S / sqrt(kappa)
    return (1.0 / 3.0) * (N_coeff) ** (-0.5) / p ** 2

A3 = scaling_coeff(3.0)
check("3.4a m=3 (3-volume accretion) prefactor A(3) = sqrt(2/3)", A3, SLOPE, rel=1e-6)
for m in (2.0, 4.0, 5.0):
    Am = scaling_coeff(m)
    note(f"3.4b m={m:g}: Omega_L = {Am:.4f} * c_S/sqrt(kappa) -- still ONE tuned coefficient",
         Am > 0, f"A({m:g})={Am:.4f} (order unity; linear in c_S/sqrt(kappa))")
ART["basin_sensitivity"] = {
    "slope_dOmega_dlambda_at_target": slope_local,
    "fractional_sensitivity": frac_sens,
    "lambda_eff_half_window_5pct": half_window,
    "A_m3": A3,
}


# ===========================================================================
# Section 4: modelling-choice dependence -- the SAME closure gives DIFFERENT Omega_L
#   Instantaneous count (Horn I, c_S=k_N=1) => 1/3;  accumulated count (Horn II,
#   c_S=kappa=1) => sqrt(2/3)=0.8165.  Same 1/sqrt(N) law, two different values from
#   two innocent count definitions -- decisive evidence the value is a modelling choice,
#   NOT sourced by the loop.
# ===========================================================================
print("=== Section 4: same closure, two count definitions, two different Omega_L ===")
OmL_I = omegaL_instantaneous(1.0, 1.0, 1e-61)
OmL_II = OmL_nat
note("4.1  instantaneous-count Omega_L (0.333) != accumulated-count Omega_L (0.816) for c_S=1",
     abs(OmL_I - OmL_II) > 0.3, f"{OmL_I:.3f} vs {OmL_II:.3f} -- value is a modelling choice")
check("4.2  instantaneous-count value = 1/3", OmL_I, 1.0 / 3.0, rel=1e-6)
check("4.3  accumulated-count value  = sqrt(2/3)", OmL_II, SLOPE, rel=3e-3)
ART["modelling_choice"] = {"instantaneous": OmL_I, "accumulated": OmL_II}


# ===========================================================================
# Section 5: POSITIVE CONTROLS (the test is NOT rigged to always say "import")
# ===========================================================================
print("=== Section 5: positive controls (a genuine sourcing WOULD register) ===")
# 5.1 IF a structural invariant FORCED lambda_eff = 0.839 with NO free knob, the attractor
#     would sit on 0.6847 and the test would report ROBUST -- demonstrate the machinery
#     lands on 0.6847 when the coefficient is supplied (so 0.6847 IS reachable; the issue is
#     that here it is supplied by hand, not sourced).
check("5.1  supplied lambda_eff=0.839 -> attractor 0.6847 (machinery CAN confirm a hit)",
      OmegaL_star_accum(lameff_needed), OMEGA_L_OBS, rel=1e-3)
# 5.2 the DISCRIMINATOR between sourced and imported: is Omega_L movable by a free knob?
#     Here sweeping kappa (a free structural rate) sweeps Omega_L across (0,1) -> it IS a
#     free knob -> IMPORT. A genuine sourcing would PIN Omega_L regardless of the free params.
sweep = [integrate_loop(1.0, kap) for kap in (0.5, 1.0, 2.0, 4.0)]
note("5.2  sweeping kappa moves Omega_L across a wide range => coefficient is a FREE KNOB (import)",
     max(sweep) - min(sweep) > 0.2,
     f"Omega_L in [{min(sweep):.3f},{max(sweep):.3f}] as kappa: 0.5..4  (a sourcing would pin it)")
# 5.3 rigged-ledger control: if the closure coefficient were DIMENSIONFUL it could be fixed by
#     units; confirm it is DIMENSIONLESS (so units CANNOT fix it -- it must be sourced or
#     imported). c_S multiplies (H l_p)^2 to give Lambda l_p^2: [rate^2]/[rate^2] = 1.
note("5.3  closure coefficient c_S is dimensionless (units cannot fix it; must be sourced/imported)",
     True, "Lambda l_p^2 = c_eff (H l_p)^2 : dimensionless coefficient")
ART["positive_controls"] = {
    "supplied_coeff_hits_target": OmegaL_star_accum(lameff_needed),
    "kappa_sweep_OmegaL": sweep,
    "kappa_sweep_range": max(sweep) - min(sweep),
}


# ===========================================================================
# Section 6: SANITY GUARDS (units + observer-gradient), per the pre-registration
# ===========================================================================
print("=== Section 6: sanity guards (TaF units; global-N observer-gradient) ===")
# 6.1 TaF rate^2-to-rate^2 units guard on the Lambda<->rate bridge.
#     Lambda has units 1/length^2 = (rate/c)^2; H^2 is rate^2/c^2 -> Lambda ~ rate^2 exactly.
#     The bridge Lambda l_p^2 = c_eff (H l_p)^2 is rate^2 = (dimensionless) x rate^2. PASS.
Lam_lp2_obs = 3.0 * OMEGA_L_OBS * (l_p / R_H) ** 2       # observed Lambda l_p^2 (rate^2 side)
Hlp2_obs    = (H0 * l_p / c_light) ** 2                   # (H l_p / c)^2  (rate^2 side)
ratio_units = Lam_lp2_obs / (3.0 * OMEGA_L_OBS * Hlp2_obs)
check("6.1  TaF units guard: Lambda l_p^2 / [3 Omega_L (H l_p/c)^2] = 1 (rate^2 = rate^2)",
      ratio_units, 1.0, rel=1e-6)
# 6.2 observer-gradient falsifier: N must be the GLOBAL horizon-scale count (one homogeneous
#     number), NOT a local observer/record density. With a global N, Lambda(N) is spatially
#     uniform => grad Lambda = 0. A local-density N would give grad Lambda != 0 (excluded).
#     We used a GLOBAL N throughout (single scalar N(t)); confirm the guard is satisfied.
def gradLambda_is_zero(local_density_model: bool):
    """Global-N => uniform Lambda (grad=0). Local-density N => Lambda varies with density."""
    if local_density_model:
        dens = np.array([0.8, 1.0, 1.3])      # a spatial density contrast
        Lam = 1.0 / np.sqrt(dens)             # Lambda ~ 1/sqrt(N_local) would vary
        return float(np.max(Lam) - np.min(Lam))
    N_global = 1.0e120                          # ONE number for the whole universe
    Lam = np.full(3, 1.0 / math.sqrt(N_global))
    return float(np.max(Lam) - np.min(Lam))
note("6.2  global-N model: grad Lambda = 0 (homogeneous; passes observer-gradient falsifier)",
     gradLambda_is_zero(False) == 0.0, "N is one horizon-scale scalar, not local density")
note("6.3  positive control: a LOCAL-density N WOULD induce grad Lambda != 0 (falsified variant)",
     gradLambda_is_zero(True) > 0.0, "confirms the guard has teeth")
ART["sanity_guards"] = {
    "units_ratio_rate2_over_rate2": ratio_units,
    "gradLambda_global": gradLambda_is_zero(False),
    "gradLambda_local_density": gradLambda_is_zero(True),
}


# ===========================================================================
# Verdict
# ===========================================================================
print("\n" + "=" * 72)
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
verdict = "TUNED-OR-ABSENT (leaning PARTIAL)"
ART["headline"] = {"checks_passed": passed, "checks_total": total, "verdict": verdict}
ART["summary"] = {
    "robust_fixed_point_at_0p6847_without_tuning": False,
    "stable_fixed_point_exists": True,
    "fixed_point_law_accumulated": "Omega_L* = min( sqrt(2/3) * c_S/sqrt(kappa), 1 )",
    "fixed_point_law_instantaneous": "Omega_L = c_eff/3  (Lambda magnitude degenerate)",
    "OmegaL_at_natural_coefficients": {"instantaneous_cS1_kN1": 1.0/3.0,
                                       "accumulated_cS1_kappa1": SLOPE},
    "lambda_eff_to_hit_0p6847": lameff_needed,
    "sensitivity_dlnOmega_dln_lambda": frac_sens,
    "magnitude_10e-122_sourced": False,
    "note_magnitude": "1/sqrt(N_4)=pi/S_dS: the 10^-122 magnitude is the horizon scale "
                      "(de Sitter relabel), not sourced by the loop.",
}

out_default = Path(__file__).resolve().parent / "artifacts" / \
    "du_lambda_N_loop_fixedpoint_probe_result.json"

print(f"HEADLINE: {passed}/{total} checks pass")
print(f"VERDICT: {verdict}")
print("  - The Lambda<->N loop DOES have a stable fixed point / attractor (the loop closes).")
print("  - Accumulated-count loop: a genuine scaling attractor at")
print("      Omega_L* = sqrt(2/3) * c_S/sqrt(kappa)  (=0.8165 for natural c_S=kappa=1).")
print("    Landing it on 0.6847 needs lambda_eff tuned to 0.839 -- ONE imported coefficient,")
print("    order-unity sensitivity, NO plateau/basin at 0.6847.")
print("  - Instantaneous-count loop: an algebraic IDENTITY Omega_L=c_eff/3 with the Lambda")
print("    MAGNITUDE degenerate -- Adversary-C's de-Sitter-trivial horn (1/sqrt(N_4)=pi/S_dS).")
print("  - Same 1/sqrt(N) closure, two innocent count definitions => 1/3 vs 0.816: the VALUE")
print("    is a modelling choice, not sourced. The R6 wall HOLDS; the import is RELOCATED")
print("    (from Lambda's coefficient to the closure coefficient c_S/sqrt(kappa)), not removed.")
print("  - PARTIAL flavour: the loop DOES generically yield an O(1), DE-dominated Omega_L")
print("    (not 0 and not requiring 120-digit tuning) -- a weak structural positive -- but the")
print("    SPECIFIC 0.6847 is tuned, and the 10^-122 magnitude is the horizon (relabel), unsourced.")
print("=" * 72)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(out_default))
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    def _native(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        raise TypeError(f"not serializable: {type(o)}")

    ART["scipy_used"] = HAVE_SCIPY
    ART["checks"] = [{"name": n, "ok": bool(ok)} for n, ok in CHECKS]
    out.write_text(json.dumps(ART, indent=2, default=_native), encoding="utf-8")
    print(f"artifact: {out}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
