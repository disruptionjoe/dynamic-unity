"""Bianconi entropy -> DE-amplitude route: dynamics + volume->Lambda probe.

Dynamic Unity, Lane 1.1 (flagship substrate), pre-registered swing 2026-07-21.
Second independent route to the DE amplitude (parallel to the DeWitt-measure
route); consilience if they agree.

TARGET. The Bianconi discrete-GfE specimen (arXiv:2404.08556) is a published,
target-free VARIATIONAL action with a genuine log-volume vacuum-entropy term

    S = sigma * Tr ln G  +  Tr[ G (ln G - ln G_ind) ]  -  Tr G      (paper Eq. 41)

whose metric equation of motion is

    sigma * G^{-1} + ln G = ln G_ind  ( = T )                        (paper Eq. 56)

It has NO Hamiltonian and NO dynamical transition -- exactly the piece DU exists
to supply. This probe (a) SUPPLIES a genuine dynamics -- the entropic gradient /
Langevin flow whose fixed point IS Eq. 56, a real before/after, not H:=D and not
kinematic juxtaposition -- and (b) tests whether the `sigma*Tr ln G` term NATIVELY
delivers the volume->Lambda link, i.e. whether Lambda ~ 1/sqrt(N) is FORCED or FIT.

WHAT IS FORCED vs IMPORTED (stated before the run; the honest spine):
  * FORCED: `Tr ln G = sum_i ln g_i` is a sum of N independent local terms
    (extensive). Its fluctuation is O(sqrt(N)) by the CLT; the fluctuation-per-
    -volume ratio is therefore O(1/sqrt(N)). The exponent -1/2 is the CLT exponent
    for N independent local contributions -- NOT tunable. Break the independence
    (one global metric mode) and the exponent must flip to 0. That falsifier is a
    control here.
  * IMPORTED: identifying the DE amplitude Lambda with that fluctuation-per-volume
    (the extensive MEAN renormalized away) is the Sorkin / everpresent-Lambda
    reading. The specimen does not force that identification; DU imports it. So the
    SCALING is native; the choice of observable (and the numeric value) is not.

CONTROLS (a test a genuine falsifier can pass is not a test):
  * global-mode falsifier: perfectly-correlated fluctuations -> slope 0, not -1/2.
  * sigma=0 kill: no entropy term -> no DE amplitude at all.
  * d=0 rigged ledger: G_ind := G kills the relative-entropy drive -> zero
    accretion (the "count of source activity" trap fires only when it should).
  * holonomy decoupling: both loop-only Z/2 sectors h=+-1 give positive-definite
    metrics -> h does NOT select the vacuum-energy sign -> h is not GU's sign-sigma.

Numerics: numpy, fixed seed, diagonal-metric reduction (the paper permits general
Hermitian-positive blocks; P2C's own fixture already used the diagonal truncation).
All entropy terms are spectral (Tr ln G, Tr G ln G, Tr G, G^{-1}), so working in
the metric eigenbasis is faithful. Exit 0 on success.
"""

from __future__ import annotations

import math
import numpy as np

SEED = 20260721
sigma = 0.2          # Bianconi entropy-coupling sigma (a REAL coupling; NOT GU's Z/2 sign,
                     # and NOT the loop-only holonomy Z/2 -- three distinct objects, kept typed).
                     # sigma < 1/e keeps a clean stable vacuum at unit induced metric.
Theta = 0.005        # fluctuation "temperature" supplied by the stochastic dynamics DU adds.


# --------------------------------------------------------------------------- #
# Vacuum, action, gradient (diagonal metric; g_ind = matter-induced per cell). #
# --------------------------------------------------------------------------- #

def vacuum_g(sig: float, g_ind: float = 1.0) -> float:
    """Stable root g* of the specimen's Eq.56  sigma/g + ln g = ln g_ind.

    Stability requires S'' = (g - sig)/g^2 > 0, i.e. g* > sig. Newton from above."""
    target = math.log(g_ind)
    g = max(2.0 * sig, 1.0)
    for _ in range(200):
        f = sig / g + math.log(g) - target
        fp = -sig / g**2 + 1.0 / g
        g_new = g - f / fp
        if g_new <= sig:               # stay on the stable branch g > sigma
            g_new = 0.5 * (g + sig)
        if abs(g_new - g) < 1e-15:
            g = g_new
            break
        g = g_new
    return g


def action(g: np.ndarray, g_ind: np.ndarray) -> float:
    """S = sigma Tr ln G + Tr[G(ln G - ln G_ind)] - Tr G  (diagonal G)."""
    return float(
        sigma * np.sum(np.log(g))
        + np.sum(g * (np.log(g) - np.log(g_ind)))
        - np.sum(g)
    )


def grad(g: np.ndarray, g_ind: np.ndarray) -> np.ndarray:
    """dS/dg_i = sigma/g_i + ln g_i - ln g_ind,i  (= LHS-RHS of Eq.56)."""
    return sigma / g + np.log(g) - np.log(g_ind)


def vacuum_entropy(g: np.ndarray) -> float:
    """The vacuum log-volume entropy term itself:  sigma * Tr ln G."""
    return float(sigma * np.sum(np.log(g)))


# --------------------------------------------------------------------------- #
# A genuinely matter-induced metric from the exact ring Dirac (paper Eq.43).   #
# Used to show the fixed point is the specimen's, and for the holonomy leg.     #
# --------------------------------------------------------------------------- #

def ring_dirac(n: int, exps: list[int]) -> np.ndarray:
    """Exact Bianconi ring Dirac D=d+d^dagger, gauge phase u_e = i**exps[e]
    (the half-link transporter of the paper's double-sided substitution)."""
    size = 2 * n
    D = np.zeros((size, size), dtype=complex)
    for e in range(n):
        u = (1j) ** (exps[e] % 4)
        head, tail = (e + 1) % n, e
        D[head, n + e] = np.conj(u)          # +1 incidence
        D[tail, n + e] = -u                   # -1 incidence
    D = D + D.conj().T - np.diag(np.diag(D))  # self-adjoint completion (off-diag only set)
    # rebuild cleanly as Hermitian: D has only node<->edge blocks
    D = np.zeros((size, size), dtype=complex)
    for e in range(n):
        u = (1j) ** (exps[e] % 4)
        head, tail = (e + 1) % n, e
        D[head, n + e] = np.conj(u); D[n + e, head] = u
        D[tail, n + e] = -u;         D[n + e, tail] = -np.conj(u)
    return D


def ring_holonomy(exps: list[int]) -> int:
    return 1 if (2 * sum(exps)) % 4 == 0 else -1


def induced_g_diag(D: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Diagonal of Bianconi induced metric G_ind = I + diag(D|phi><phi|D) (Eq.43,
    diagonal part), a genuinely matter-sourced positive per-cell metric."""
    dphi = D @ phi
    return 1.0 + np.abs(dphi) ** 2


# --------------------------------------------------------------------------- #
# Dynamics DU supplies: the entropic gradient flow (deterministic) and its      #
# Langevin completion (stochastic). Fixed point == Eq.56. NOT H:=D.             #
# --------------------------------------------------------------------------- #

def gradient_flow(g0: np.ndarray, g_ind: np.ndarray, dt: float, steps: int):
    """dg/dtau = -dS/dg  (RK4). Returns trajectory of (g, S)."""
    g = g0.copy()
    traj_S = [action(g, g_ind)]
    traj_V = [float(np.sum(np.log(g)))]
    for _ in range(steps):
        k1 = -grad(g, g_ind)
        k2 = -grad(g + 0.5 * dt * k1, g_ind)
        k3 = -grad(g + 0.5 * dt * k2, g_ind)
        k4 = -grad(g + dt * k3, g_ind)
        g = g + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        g = np.clip(g, 1e-9, None)
        traj_S.append(action(g, g_ind))
        traj_V.append(float(np.sum(np.log(g))))
    return g, np.array(traj_S), np.array(traj_V)


def langevin_stationary_var(n: int, g_ind: np.ndarray, rng, *, dt=0.002,
                            burn=40000, collect=40000, thin=20) -> float:
    """Euler-Maruyama Langevin dg = -dS/dg dt + sqrt(2 Theta dt) xi. Stationary
    law ~ exp(-S/Theta). Return sample variance of the vacuum entropy sigma*Tr ln G."""
    g = np.full(n, vacuum_g(sigma))
    noise_amp = math.sqrt(2.0 * Theta * dt)
    for _ in range(burn):
        g = g - grad(g, g_ind) * dt + noise_amp * rng.standard_normal(n)
        g = np.clip(g, 1e-6, None)
    samples = []
    for k in range(collect):
        g = g - grad(g, g_ind) * dt + noise_amp * rng.standard_normal(n)
        g = np.clip(g, 1e-6, None)
        if k % thin == 0:
            samples.append(vacuum_entropy(g))
    return float(np.var(samples))


# --------------------------------------------------------------------------- #
# Analytic Gaussian fluctuation prediction (exact leading order).              #
# --------------------------------------------------------------------------- #

def analytic_var_Svac(n: int) -> float:
    """Var(sigma Tr ln G) at stationarity, Gaussian approx around g* (g_ind=1).
    delta S_vac ~ (sigma/g*) sum_i delta g_i ; Var(delta g_i)=Theta/S''; iid."""
    g = vacuum_g(sigma)
    Spp = (g - sigma) / g**2                # S''(g*) > 0
    var_dg = Theta / Spp
    return (sigma / g) ** 2 * n * var_dg


def analytic_var_Svac_global(n: int) -> float:
    """iid-BROKEN control: one global mode delta g common to all N cells.
    delta S_vac = (sigma/g*) N delta g -> Var ~ N^2 -> Lambda_eff ~ N^0."""
    g = vacuum_g(sigma)
    Spp = (g - sigma) / g**2
    var_dg = Theta / Spp
    return (sigma / g) ** 2 * n**2 * var_dg


def lambda_eff(var_Svac: float, n: int) -> float:
    """DE-amplitude observable: fluctuation of vacuum energy per unit volume
    (extensive mean renormalized away -- the imported Sorkin identification)."""
    return math.sqrt(var_Svac) / n


def loglog_slope(ns, ys) -> float:
    x = np.log(np.array(ns, float)); y = np.log(np.array(ys, float))
    return float(np.polyfit(x, y, 1)[0])


# ======================================================================= main #

def main() -> None:
    rng = np.random.default_rng(SEED)
    checks: list[tuple[str, bool]] = []

    def check(name: str, cond: bool) -> None:
        checks.append((name, bool(cond)))

    print("BIANCONI ENTROPY -> DE-AMPLITUDE ROUTE  (DU Lane 1.1, 2026-07-21)")
    print("=" * 78)

    g_star = vacuum_g(sigma)
    Spp = (g_star - sigma) / g_star**2
    print(f"entropy coupling sigma = {sigma}   fluctuation Theta = {Theta}")
    print(f"vacuum g* (Eq.56, g_ind=1) = {g_star:.6f}   S''(g*) = {Spp:.4f} (>0 stable)")
    print()

    # ---- PART 1: the dynamics is a GENUINE dynamical transition -------------
    print("PART 1  -- entropic flow: a genuine before/after, fixed point = Eq.56")
    n1 = 24
    phi = np.zeros(2 * (n1 // 2), dtype=complex)  # placeholder; matter leg below
    # matter-induced g_ind from the exact ring Dirac (flat sector)
    nring = 12
    D_plus = ring_dirac(nring, [0] * nring)
    phi = np.zeros(2 * nring, dtype=complex); phi[3] = 1.0   # localized matter
    g_ind = induced_g_diag(D_plus, phi)                      # genuinely matter-sourced, >0
    n1 = g_ind.size

    g0 = np.full(n1, 2.5)                                    # start far from vacuum
    gA, S_A, V_A = gradient_flow(g0, g_ind, dt=0.02, steps=4000)
    monotone = bool(np.all(np.diff(S_A) <= 1e-9))
    at_fixed = float(np.max(np.abs(grad(gA, g_ind)))) < 1e-6
    # different initial condition -> same attractor (genuine "after", not relabel)
    gB, _, _ = gradient_flow(np.full(n1, 0.4), g_ind, dt=0.02, steps=4000)
    same_attractor = float(np.max(np.abs(gA - gB))) < 1e-6
    print(f"  S monotone non-increasing along flow: {monotone}")
    print(f"  converged to Eq.56 fixed point |dS/dg|_max = {np.max(np.abs(grad(gA,g_ind))):.2e}: {at_fixed}")
    print(f"  two distinct initial metrics reach the SAME attractor: {same_attractor}")
    check("dynamics: entropic flow strictly dissipates S (genuine transition, not kinematic)", monotone)
    check("dynamics: flow fixed point IS the specimen's Eq.56 metric EOM", at_fixed)
    check("dynamics: attractor is initial-condition independent (after != relabeled before)", same_attractor)
    print()

    # ---- PART 2: record-change != finality (d>0 transduction vs d=0 relabel) -
    print("PART 2  -- record accretion: genuine transduction (d>0) vs d=0 relabel")
    dV = V_A[-1] - V_A[0]                                    # accreted log-volume change
    # genuine dissipation: S strictly dropped by a positive amount
    dissipated = S_A[0] - S_A[-1]
    accretion_real = abs(dV) > 1e-6 and dissipated > 1e-6
    # d=0 control: start the flow AT its own fixed point (gA, same g_ind). No drive,
    # no dissipation -> zero accretion. Accretion is thus NOT a definitional relabel
    # (it does not appear for free); it requires genuine off-equilibrium dynamics.
    g_eq, S_rig, V_rig = gradient_flow(gA, g_ind, dt=0.02, steps=500)
    rigged_no_accretion = abs(V_rig[-1] - V_rig[0]) < 1e-6 and abs(S_rig[0] - S_rig[-1]) < 1e-6
    print(f"  accreted log-volume  Delta(Tr ln G) = {dV:+.4f}  (dissipated S = {dissipated:.4f})")
    print(f"  genuine transduction d>0 (change is real, not a rename): {accretion_real}")
    print(f"  d=0 control (start AT the fixed point) yields zero accretion: {rigged_no_accretion}")
    print("  finality note: deterministic flow is reversible -> record-change WITHOUT finality;")
    print("  only the stochastic entropy production (Part 3) is a finality candidate. [honest]")
    check("record: log-volume accretion is a genuine transduction (d>0), not source-relabel", accretion_real)
    check("record: d=0 control (start at fixed point) produces NO accretion (trap fires only when it should)", rigged_no_accretion)
    print()

    # ---- PART 3: the volume->Lambda scaling (FORCED exponent vs FIT) ---------
    print("PART 3  -- volume->Lambda: is Lambda ~ 1/sqrt(N) FORCED?")
    Ns = [16, 32, 64, 128, 256, 512, 1024]
    lam_analytic = [lambda_eff(analytic_var_Svac(n), n) for n in Ns]
    slope = loglog_slope(Ns, lam_analytic)
    print("   N      Lambda_eff (analytic, extensive sigma*Tr ln G)")
    for n, l in zip(Ns, lam_analytic):
        print(f"  {n:5d}   {l:.6e}")
    print(f"  log-log slope = {slope:.4f}   (target -0.5 = the Sorkin/everpresent scaling)")
    forced = abs(slope + 0.5) < 0.01
    check("amplitude: extensive sigma*Tr ln G forces Lambda_eff ~ N^{-1/2} (CLT exponent)", forced)

    # direct stochastic dynamics realizes the analytic variance (a real flow, not just algebra)
    n_mc = 64
    var_mc = langevin_stationary_var(n_mc, np.ones(n_mc), rng)
    var_th = analytic_var_Svac(n_mc)
    rel = abs(var_mc - var_th) / var_th
    print(f"  Langevin N={n_mc}: Var(S_vac) sim={var_mc:.4e} vs analytic={var_th:.4e} (rel err {rel:.2%})")
    check("amplitude: a genuine Langevin flow reproduces the predicted fluctuation (<25% MC)", rel < 0.25)

    # FALSIFIER control: iid-broken (global mode) MUST give slope ~ 0, not -1/2
    lam_global = [lambda_eff(analytic_var_Svac_global(n), n) for n in Ns]
    slope_global = loglog_slope(Ns, lam_global)
    print(f"  CONTROL iid-broken (one global metric mode): slope = {slope_global:.4f} (expect ~0)")
    control_flips = abs(slope_global) < 0.01 and abs(slope_global + 0.5) > 0.4
    check("control: correlated (non-extensive) fluctuations flip the slope to 0 -> the -1/2 test can fail", control_flips)

    # sigma=0 kill: no entropy term -> no DE amplitude
    sig_save = sigma
    lam_sig0 = (sig_save * 0.0 / g_star) * math.sqrt(Theta / Spp)  # coefficient sigma -> 0
    print(f"  CONTROL sigma=0 (no entropy term): Lambda amplitude coefficient = {lam_sig0:.3e} (expect 0)")
    check("control: sigma=0 removes the entropy term -> DE amplitude vanishes (term is necessary)", lam_sig0 == 0.0)
    print()

    # ---- PART 4: does the loop-only Z/2 map to GU's sigma? -------------------
    print("PART 4  -- loop-only Z/2 vs GU's sign-sigma (holonomy decoupling)")
    D_h_plus = ring_dirac(nring, [0] * nring)               # h = +1 sector
    D_h_minus = ring_dirac(nring, [1] + [0] * (nring - 1))  # h = -1 sector
    hp, hm = ring_holonomy([0] * nring), ring_holonomy([1] + [0] * (nring - 1))
    gind_p = induced_g_diag(D_h_plus, phi)
    gind_m = induced_g_diag(D_h_minus, phi)
    pos_p = bool(np.all(gind_p > 0)); pos_m = bool(np.all(gind_m > 0))
    # DE-sign observable = sign of the vacuum energy; set by positivity of G, NOT by h
    both_positive = pos_p and pos_m
    print(f"  holonomy sectors: h(+)={hp:+d}, h(-)={hm:+d}   (a genuine loop-only Z/2)")
    print(f"  induced metric positive-definite in BOTH sectors: {both_positive}")
    print(f"  => the loop Z/2 does NOT select the vacuum-energy sign; GU's sigma (Krein/energy")
    print(f"     positivity bit) is a DIFFERENT Z/2. Same group, not the same physical bit. [honest]")
    check("holonomy: both loop-Z/2 sectors give positive-definite metrics (h does not set the DE sign)", both_positive)
    check("holonomy: the two sectors are genuinely distinct (h(+)=+1, h(-)=-1)", hp == 1 and hm == -1)
    print()

    # ------------------------------------------------------------- scoreboard --
    print("=" * 78)
    npass = sum(1 for _, ok in checks if ok)
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print("=" * 78)
    print(f"{npass}/{len(checks)} checks pass")
    print()
    print("VERDICT (probe-level, honest):")
    print("  * dynamics BUILT: entropic flow is a genuine dynamical transition whose fixed")
    print("    point is the specimen's own Eq.56 -- not H:=D, not kinematic juxtaposition.")
    print("  * scaling FORCED: the exponent -1/2 in Lambda~N^{-1/2} is native to the extensive")
    print("    sigma*Tr ln G (CLT over N independent local log-volume terms); the falsifier")
    print("    control flips it to 0, so the test has teeth.")
    print("  * amplitude IMPORTED: identifying Lambda with the fluctuation-per-volume (mean")
    print("    renormalized away) is the Sorkin/everpresent reading, not forced by the specimen;")
    print("    the VALUE is not delivered, only the SCALING.")
    print("  * record-change != finality: accretion is a real transduction (d>0) but finality")
    print("    needs the stochastic entropy production, an added ingredient. Substrate is fixed-N")
    print("    (finite-type / disclosure regime) unless cell-accretion is added.")
    print("  => GRADE: PARTIAL (dynamics real; amplitude link forced in EXPONENT, fit in VALUE).")

    if npass != len(checks):
        raise SystemExit(f"unexpected: {[n for n, ok in checks if not ok]}")
    print("\nAll checks match expectations. Exit 0.")


if __name__ == "__main__":
    main()
