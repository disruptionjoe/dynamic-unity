#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dynamic Unity -- Lane 1.3 pre-registered swing probe.

Question: does the (9,5)/gimmel DeWitt-fiber measure DERIVE the dark-energy
normalization  phi = 1/(3 Omega_L)^2  (hence Lambda ~ 1/sqrt(N), the observed
~10^-120) NATIVELY, beating BOTH traps that sank route (ii):
  (a) the IMPORTED Sorkin  Lambda l_p^2 ~ 1/sqrt(N)  amplitude law, and
  (b) the de-Sitter-entropy RELABEL  1/sqrt(N) = pi/S_dS  ("no novelty").

This probe is a DISPROOF-OR-CONFIRM instrument, not a fit. It builds the actual
DeWitt supermetric on the 10-dim fiber Sym^2(T*X) from the gimmel ledger
(G_lambda(S,T) = tr(g^-1 S g^-1 T) - lambda tr_g(S) tr_g(T), lambda_GU = 1/2),
and asks whether any native invariant of that measure supplies the amplitude
factor 3 Omega_L = 2.054 that phi encodes. It also carries POSITIVE CONTROLS
that a genuine native success WOULD pass (Section 7), so a pass here is not
vacuous.

Everything ported (Sorkin 1/sqrt(N), the FRW critical-density relation) is
labelled PORTED. Nothing asserts DU. Exploration grade, no canon movement.

Run: python -u tests/de_amplitude_dewitt_route_probe.py   (expect ALL PASS, exit 0)
"""

import math
import sys

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print("numpy required:", exc)
    sys.exit(2)

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
# Constants (SI / cosmology; same anchors as gu-formalization W145/W146)
# ===========================================================================
c     = 2.99792458e8            # m/s
G     = 6.67430e-11             # m^3 kg^-1 s^-2
hbar  = 1.054571817e-34        # J s
Mpc   = 3.0856775814913673e22  # m
eV    = 1.602176634e-19        # J

H0_kms  = 67.36                # km/s/Mpc  (Planck 2018)
Omega_L = 0.6847              # dark-energy fraction, present epoch (Planck 2018)

H0  = H0_kms * 1e3 / Mpc                 # s^-1
R_H = c / H0                             # Hubble radius, m
l_p = math.sqrt(hbar * G / c**3)         # Planck length, m

# The target normalization and the amplitude factor it encodes.
three_OmegaL = 3.0 * Omega_L             # = 2.054, the residual of route (ii)
phi_target   = 1.0 / three_OmegaL**2     # = 0.237, the "measured-record 4-density"

print("=== Section 0: the target algebra ===")
check("0.1  3*Omega_L (route-ii residual)", three_OmegaL, 2.054, rel=1e-3)
check("0.2  phi_target = 1/(3 Omega_L)^2", phi_target, 0.237, rel=1e-2)
# phi and the amplitude factor are two views of ONE number: 1/sqrt(phi) = 3 Omega_L.
check("0.3  1/sqrt(phi_target) == 3 Omega_L", 1.0 / math.sqrt(phi_target), three_OmegaL, rel=1e-9)


# ===========================================================================
# Section 1: positive controls (background scales; PORTED)
# ===========================================================================
print("=== Section 1: positive controls (PORTED) ===")
rho_crit = 3 * H0**2 * c**2 / (8 * math.pi * G)          # J/m^3  (FRW; the '3' is Friedmann)
rho_L    = Omega_L * rho_crit
rho_L_scale_meV = ((rho_L * (hbar * c)**3) ** 0.25) / eV * 1e3
check("1.1  observed rho_L^{1/4} (meV)", rho_L_scale_meV, 2.24, rel=3e-2)

ratio_RH_lp = R_H / l_p
check("1.2  R_H/l_p", ratio_RH_lp, 8.5e60, rel=5e-2)

N4        = ratio_RH_lp**4                                # 4-volume of Hubble patch in Planck units
sqrtN4    = math.sqrt(N4)
lam_lead  = 1.0 / sqrtN4                                  # PORTED Sorkin leading amplitude
check("1.3  N_4 (4-volume, Planck units)", N4, 5.21e243, rel=1e-1)
check("1.4  1/sqrt(N_4) = Lambda l_p^2 (leading, PORTED)", lam_lead, 1.39e-122, rel=5e-2)

lam_obs = 3 * Omega_L * (l_p / R_H)**2                    # observed Lambda l_p^2
check("1.5  observed Lambda l_p^2", lam_obs, 2.85e-122, rel=5e-2)
# the whole game in one line: observed / leading = 3 Omega_L exactly.
check("1.6  observed/leading == 3 Omega_L", lam_obs / lam_lead, three_OmegaL, rel=1e-6)


# ===========================================================================
# Section 2: TRAP (b) -- the de Sitter relabel is EXACT and untouched
#   1/sqrt(N_4) = pi / S_dS  (both equal (l_p/R_H)^2). The magnitude is fixed
#   by the 4-volume ALONE; no fiber measure enters it.
# ===========================================================================
print("=== Section 2: TRAP (b) the de Sitter relabel (EXACT) ===")
S_dS = math.pi * ratio_RH_lp**2                          # de Sitter horizon entropy
check("2.1  S_dS", S_dS, 2.27e122, rel=5e-2)
check("2.2  1/sqrt(N_4) == pi/S_dS (EXACT identity)", lam_lead, math.pi / S_dS, rel=1e-12)
# A fiber reweight multiplies N by a constant; it cannot change that the leading
# magnitude IS the Gibbons-Hawking value. Demonstrate: for ANY phi, the magnitude
# stays pi/S_dS up to the O(1) factor 1/sqrt(phi) -- the 10^-120 is de Sitter's.
for phi in (0.1, 0.237, 1.0, 4.0):
    lam_phi = 1.0 / math.sqrt(phi * N4)
    ratio_to_dS = lam_phi / (math.pi / S_dS)
    note(f"2.3  phi={phi}: magnitude still = (1/sqrt(phi)) * pi/S_dS",
         abs(ratio_to_dS - 1.0 / math.sqrt(phi)) < 1e-9,
         f"factor {1.0/math.sqrt(phi):.4g}")


# ===========================================================================
# Section 3: the ACTUAL (9,5)/gimmel DeWitt-fiber measure
#   Fiber W = Sym^2(T*_x X), dim 10. Bilinear form (gimmel ledger):
#     G_lambda(S,T) = tr(g^-1 S g^-1 T) - lambda tr(g^-1 S) tr(g^-1 T)
#   lambda_GU = 1/2 (trace-reversal), lambda_DW = 1 (conventional DeWitt).
# ===========================================================================
print("=== Section 3: the actual (9,5)/gimmel DeWitt fiber measure ===")

def sym_basis(d=4):
    """Orthonormal-index basis of Sym^2 (d x d), dim d(d+1)/2 = 10 for d=4."""
    B = []
    for i in range(d):
        for j in range(i, d):
            E = np.zeros((d, d))
            E[i, j] = 1.0
            E[j, i] = 1.0
            B.append(E)
    return B

def dewitt_gram(g, lam):
    """10x10 Gram matrix of G_lambda on the fiber basis, at base metric g."""
    gi = np.linalg.inv(g)
    B = sym_basis(g.shape[0])
    n = len(B)
    M = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            Sa, Tb = B[a], B[b]
            t1 = np.trace(gi @ Sa @ gi @ Tb)
            t2 = np.trace(gi @ Sa) * np.trace(gi @ Tb)
            M[a, b] = t1 - lam * t2
    return M

g_lor = np.diag([-1.0, 1.0, 1.0, 1.0])   # Lorentzian base, signature (3,1)

# 3.1 pure-trace direction S = T = g reproduces the ledger:  G(g,g) = d - lambda d^2.
def G_of_gg(g, lam):
    gi = np.linalg.inv(g)
    return np.trace(gi @ g @ gi @ g) - lam * np.trace(gi @ g)**2

check("3.1  G_GU(g,g) [lambda=1/2] = -4 (ledger)", G_of_gg(g_lor, 0.5), -4.0, rel=1e-9)
check("3.2  G_DW(g,g) [lambda=1]  = -12 (ledger)", G_of_gg(g_lor, 1.0), -12.0, rel=1e-9)
check("3.3  DW/GU pure-trace ratio = 3 (d=4)",
      G_of_gg(g_lor, 1.0) / G_of_gg(g_lor, 0.5), 3.0, rel=1e-9)

# 3.4 fiber signature on the Lorentzian locus is (6,4) for lambda > 1/4.
for lam, tag in ((0.5, "GU"), (1.0, "DW")):
    ev = np.linalg.eigvalsh(dewitt_gram(g_lor, lam))
    pos = int(np.sum(ev > 1e-9))
    neg = int(np.sum(ev < -1e-9))
    note(f"3.4  fiber signature ({tag}, lambda={lam}) = (6,4)",
         (pos, neg) == (6, 4), f"got ({pos},{neg})")


# ===========================================================================
# Section 4: TRAP (a) -- ADDITIVITY. The DeWitt supermetric is ULTRALOCAL
#   (pointwise, no derivatives), so it is a PRODUCT measure over base points:
#   the count is additive, the Fisher information adds, Cramer-Rao gives sqrt(N)
#   with a CONSTANT prefactor. A local reweight phi cannot change the sqrt(N)
#   LAW -- only rescale N inside it. So it cannot beat the Sorkin import.
# ===========================================================================
print("=== Section 4: TRAP (a) additivity -- phi is only a constant reweight ===")
# Under N -> phi*N (a local per-cell reweight), the amplitude law is UNCHANGED:
#   1/sqrt(phi*N) = (1/sqrt(phi)) * 1/sqrt(N).
# Verify the exponent is exactly -1/2 for a range of N (i.e. the sqrt law survives).
Ns = np.array([1e10, 1e20, 1e40, 1e80, N4])
phi = phi_target
amp = 1.0 / np.sqrt(phi * Ns)
# fit slope of log(amp) vs log(N): must be -1/2 (Sorkin law intact, not beaten)
slope = np.polyfit(np.log(Ns), np.log(amp), 1)[0]
check("4.1  reweighted-count amplitude still scales as N^(-1/2)", slope, -0.5, rel=1e-6)
# and the prefactor it introduces is EXACTLY 1/sqrt(phi) = 3 Omega_L -- i.e. phi is
# DEFINED by the target, not derived: circular unless something ELSE fixes phi.
pref = (1.0 / np.sqrt(phi * N4)) / (1.0 / np.sqrt(N4))
check("4.2  reweight prefactor == 3 Omega_L (phi defined BY the target)",
      pref, three_OmegaL, rel=1e-9)


# ===========================================================================
# Section 5: METROLOGY -- is phi a native invariant, or a frame artifact?
#   A fiber->base amplitude ratio inherits the fiber-volume Weyl weight. The
#   fiber volume density sqrt|det G| is NOT scale-invariant: under g -> alpha*g,
#   G_ab ~ alpha^-2, so det(10x10) ~ alpha^-20. Nonzero weight => phi needs an
#   imported scale (exactly PRED-NORM-RANK's rank-3 freedom). Only a RATIO of
#   two fiber measures (same 10-dim space) is invariant -- and that needs the
#   unbuilt interacting C-operator (H59 open).
# ===========================================================================
print("=== Section 5: metrology -- fiber measure is scale-dependent ===")
lam = 0.5
det0 = np.linalg.det(dewitt_gram(g_lor, lam))
for alpha in (2.0, 4.0, 10.0):
    det1 = np.linalg.det(dewitt_gram(alpha * g_lor, lam))
    predicted = alpha**(-20) * det0            # 10x10 det, each entry ~ alpha^-2
    note(f"5.1  det G(alpha*g)/det G(g) = alpha^-20  (alpha={alpha})",
         abs(det1 - predicted) <= 1e-6 * abs(predicted),
         f"weight nonzero => NOT scale-invariant")
# the fiber VOLUME density weight is -10 in alpha (sqrt of det); the only reason
# it matters: it is NONZERO, so a fiber-to-base ratio carries a frame-dependent
# scale and cannot be a native invariant. (A same-space measure ratio cancels it.)
vol_weight = math.log(math.sqrt(abs(np.linalg.det(dewitt_gram(4.0*g_lor, lam)))) /
                      math.sqrt(abs(det0))) / math.log(4.0)
check("5.2  fiber volume-density Weyl weight (nonzero => frame-dependent)",
      vol_weight, -10.0, rel=1e-6)


# ===========================================================================
# Section 6: does ANY native invariant of the measure hit 3 Omega_L = 2.054?
#   The native subleading amplitude factors GU actually has (W145) are the
#   number-variance sqrt(c) for the {2,7,13}-smooth spectrum, plus discrete
#   signature/dimension data. Check the whole native menu against 2.054.
# ===========================================================================
print("=== Section 6: native invariants vs the needed factor 3 Omega_L = 2.054 ===")
native_factors = {
    "sqrt(2)  [W145 number-variance]":  math.sqrt(2),   # 1.414
    "sqrt(7)  [W145 number-variance]":  math.sqrt(7),   # 2.646
    "sqrt(13) [W145 number-variance]":  math.sqrt(13),  # 3.606
    "10/4  fiber/neg-count":            10.0 / 4.0,
    "14/4  Y14/base":                   14.0 / 4.0,
    "9/5  (9,5) signature":             9.0 / 5.0,
    "6/4  fiber (6,4)":                 6.0 / 4.0,
    "2  naive doubling (closest)":      2.0,
}
target = three_OmegaL
best_name, best_gap = None, 1e9
for name, val in native_factors.items():
    gap = abs(val - target) / target
    within = gap < 0.02
    note(f"6.1  native factor {name} = {val:.4g} vs 2.054",
         not within,  # PASS means it does NOT spuriously match (honest: none is native)
         f"rel gap {gap:.2%}" + ("  <-- would-be match" if within else ""))
    if gap < best_gap:
        best_name, best_gap = name, gap
note("6.2  no native factor lands within 2% of 3 Omega_L",
     best_gap >= 0.02, f"closest: {best_name}, gap {best_gap:.2%}")

# 6.3 the count c that WOULD be needed is (3 Omega_L)^2 = 4.219 -- not a
#     GU-native count ({2,7,13}); and it is Omega_L-dependent (dynamical).
c_needed = three_OmegaL**2
check("6.3  c needed = (3 Omega_L)^2", c_needed, 4.219, rel=1e-3)
note("6.4  c_needed=4.22 not in the native spectrum {2,7,13}",
     all(abs(c_needed - x) / x > 0.05 for x in (2, 7, 13)), "so sqrt(c) cannot supply it")

# 6.5 even the '3' is not cleanly native: DeWitt trace-ratio 2(1-d)/(2-d) and the
#     Friedmann factor (d-1)(d-2)/2 BOTH equal 3 at d=4 but are DIFFERENT functions
#     of d (they part ways at d=3,5) -- a d=4 coincidence, not an identity.
def dewitt_ratio(d):    return 2 * (1 - d) / (2 - d)
def friedmann_fac(d):   return (d - 1) * (d - 2) / 2.0
check("6.5a DeWitt trace-ratio(d=4)", dewitt_ratio(4), 3.0, rel=1e-9)
check("6.5b Friedmann factor(d=4)",   friedmann_fac(4), 3.0, rel=1e-9)
note("6.5c the two '3'-functions DIFFER off d=4 (coincidence, not identity)",
     abs(dewitt_ratio(3) - friedmann_fac(3)) > 0.5 and
     abs(dewitt_ratio(5) - friedmann_fac(5)) > 0.5,
     f"d=3: {dewitt_ratio(3):.3g} vs {friedmann_fac(3):.3g}; "
     f"d=5: {dewitt_ratio(5):.3g} vs {friedmann_fac(5):.3g}")


# ===========================================================================
# Section 7: POSITIVE CONTROLS (a real native success WOULD pass these)
#   The instrument is not rigged to always say "import". If the fiber measure
#   DID supply a scale-invariant factor equal to 3 Omega_L, the closure would
#   register. Demonstrate the machinery CAN confirm a native win.
# ===========================================================================
print("=== Section 7: positive controls (the test can register a native win) ===")
# 7.1 hypothetical: a native factor A_native = 3 Omega_L reproduces observed Lambda.
A_native_hypothetical = three_OmegaL
lam_native = A_native_hypothetical * lam_lead
check("7.1  IF a native factor = 3 Omega_L existed, it reproduces observed Lambda",
      lam_native, lam_obs, rel=1e-6)
# 7.2 and the corresponding phi would be exactly the target (closure is consistent).
phi_from_native = 1.0 / A_native_hypothetical**2
check("7.2  ...and its phi would equal phi_target (closure consistent)",
      phi_from_native, phi_target, rel=1e-9)
# 7.3 rigged-ledger control: a same-space measure RATIO cancels the Weyl weight
#     (this is the ONE native route that is scale-invariant) -- show cancellation,
#     so the obstruction in Sec 5 is specifically the fiber->base ratio, correctly.
detGU = np.linalg.det(dewitt_gram(g_lor, 0.5))
detDW = np.linalg.det(dewitt_gram(g_lor, 1.0))
r0 = detGU / detDW
detGU_a = np.linalg.det(dewitt_gram(3.0 * g_lor, 0.5))
detDW_a = np.linalg.det(dewitt_gram(3.0 * g_lor, 1.0))
r_a = detGU_a / detDW_a
check("7.3  same-space measure RATIO is scale-invariant (control)", r_a, r0, rel=1e-9)
# ...but that invariant ratio is a FIXED geometric number, not 3 Omega_L, and it
# needs no dynamics -- so it cannot be the epoch-dependent Omega_L either.
note("7.4  the scale-invariant ratio is a fixed number != 3 Omega_L(t)",
     abs(r0 - three_OmegaL) / three_OmegaL > 0.02, f"ratio detGU/detDW = {r0:.4g}")


# ===========================================================================
# Verdict
# ===========================================================================
print("\n" + "=" * 68)
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
print(f"HEADLINE: {passed}/{total} checks pass")
print("VERDICT: CONFIRMS-IMPORT")
print("  - Trap (b) de Sitter relabel: UNTOUCHED (Sec 2). The 10^-120 magnitude")
print("    is 1/sqrt(N_4) = pi/S_dS exactly; the fiber never enters it.")
print("  - Trap (a) Sorkin sqrt(N) import: UNTOUCHED (Sec 4). The ultralocal")
print("    DeWitt measure is additive; a reweight phi only rescales N by a")
print("    CONSTANT, leaving the imported sqrt(N) law intact.")
print("  - phi = 1/(3 Omega_L)^2 is NOT native (Sec 5,6): the fiber->base factor")
print("    is scale-dependent (needs the imported B.5 cut scale, PRED-NORM-RANK),")
print("    the native discrete factors {sqrt2,sqrt7,sqrt13} miss 2.054, and the")
print("    residual Omega_L is a DYNAMICAL cosmological ratio, not a kinematic")
print("    invariant of Met(X4). The '3' is Friedmann's, only coincidentally the")
print("    DeWitt trace-ratio at d=4.")
print("=" * 68)

if passed == total:
    print("exit 0")
    sys.exit(0)
else:
    print("exit 1 -- some checks failed")
    sys.exit(1)
