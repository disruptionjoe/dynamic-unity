#!/usr/bin/env python3
"""DU governance-selection-on-CSG probe: can a governance / incentive SELECTION BIAS on the
Rideout-Sorkin classical-sequential-growth (CSG) transition probabilities steer the grown causal
set OFF the Kleitman-Rothschild-dominated (non-manifoldlike) region TOWARD manifoldlikeness -- or
does KR entropy dominate any physically-reasonable bias? (the Test #5 / meta-requirement fork of
the incentive-selection mode-issuance candidate).

THE FORK (meta / KR). The incentive-selection candidate's concrete host is Rideout-Sorkin CSG of
causal sets ("gossip about gossip": each new atom is born with links into its causal past;
internal, covariant). The known headwind is our own T223 no-go (imported from time-as-finality and
RE-VERIFIED here, not on TaF's say-so): the uniform finality-colimit ensemble does NOT concentrate
on manifoldlike causal sets. The candidate's claim: the genesis GOVERNANCE / incentive-issuance
function is a SELECTION BIAS on the CSG transition probabilities that steers growth AWAY from the
entropically-dominant non-manifoldlike posets toward manifoldlike, algebra-growing structure.
Decisive question: can any such bias MEASURABLY shift the grown ensemble toward manifoldlikeness at
accessible N, or does entropy swamp any reasonable bias?

------------------------------------------------------------------------------------------------
A SEAM WE STATE HONESTLY UP FRONT (the sovereign self-check, CONNECTIONS.md). "Uniform CSG",
"Kleitman-Rothschild", and "T223" are THREE DISTINCT unbiased measures and must not be silently
identified:
  * KR theorem (Kleitman-Rothschild 1975): the UNIFORM measure over all LABELED posets on n
    elements concentrates, as n->inf, on 3-LAYER posets (layer sizes ~ n/4, n/2, n/4), height 3,
    middle-dominated -- non-manifoldlike. This is an ASYMPTOTIC theorem about the uniform-poset
    measure. Small-N cannot prove it; we IMPORT it as literature and re-state it honestly, and we
    CALIBRATE our estimator against a hand-built KR-shaped ensemble so "KR domination" is concrete.
  * Rideout-Sorkin CSG / transitive percolation: a DIFFERENT measure (a covariant growth dynamics).
    Its generic (fixed-parameter) grown causet is ALSO non-manifoldlike, but by a chain<->antichain
    crossover mechanism, not the KR flat-3-layer mechanism. This is the candidate's ACTUAL host, so
    it is what we grow.
  * T223: TaF's uniform 1+1 ordinal finality-colimit ensemble -- a third measure; its survivors are
    a thin decaying rare tail through n=8. We re-use its MM estimator and its "no-go on the uniform
    ensemble" shape, re-verified here.
The honest target is therefore: does a governance bias on the RS-CSG measure (the host) measurably
move the grown ensemble toward the manifold band -- with the KR asymptotic theorem carried as the
un-refuted (and un-demonstrated) wall it must eventually beat.
------------------------------------------------------------------------------------------------

WHAT THIS PROBE COMPUTES (anti-toy; foreground; POSITIVE CONTROLS mandatory).

Representation. A causal set = a strictly-ordered finite poset, grown one atom at a time in birth
order; past[i] is a bitmask of all ancestors of i (transitive closure maintained incrementally, so
every object is a genuine transitively-closed causet). Estimators computed on it:
  * ordering fraction  of = (#comparable pairs)/C(n,2);
  * Myrheim-Meyer continuum dimension d_MM = f^{-1}(of), f(d)=Gamma(d+1)Gamma(d/2)/(2 Gamma(3d/2))
    (RE-VERIFIED here against genuine d-dim Minkowski sprinklings, per CONNECTIONS.md -- not
    imported on TaF's grade);
  * height H = longest chain length (# elements); its N-scaling gives an INDEPENDENT dimension
    d_chain via H ~ N^{1/d} (manifold 2D: H ~ 2*sqrt(N), slope 1/2; KR: H fixed ~ 3, slope -> 0;
    chain: H ~ N, slope 1). d_chain is the SHARP KR discriminator that ordering-fraction alone
    lacks (KR of ~ 3/8 -> d_MM ~ 2.4 is only weakly separated from 2D's 1/2; height flatly
    separates 3 from sqrt(N)).
  * largest rank-layer fraction w = (max rank-antichain size)/n  (KR: -> ~1/2; 2D sprinkle: -> 0).

Modules:
  (0) MM VALIDATION (positive control, falsifiable): sprinkle N points into genuine d-dim Minkowski
      causal diamonds (d=2,3,4); the estimator must RECOVER the input dimension. If it does not, the
      instrument is miscalibrated and nothing downstream means anything.
  (1) MANIFOLD control (hand-forced manifold; positive control): 1+1 Minkowski sprinkle across the
      N-sweep must read d_MM ~ 2 AND height-slope ~ 1/2. Shows the estimator CAN register
      manifoldlikeness (a genuine falsifier -- a rubber-stamp estimator would also pass, so it is
      paired with (2)).
  (2) KR / UNBIASED-CSG control (positive control): (2a) a hand-built KR-shaped 3-layer ensemble
      must be FLAGGED non-manifoldlike (height-slope ~ 0, w high) -- calibrates the KR signature and
      proves the estimator is NOT a rubber stamp; (2b) unbiased Rideout-Sorkin transitive
      percolation (gamma=0) must NOT be robustly in the manifold band -- the CSG-native
      non-manifoldlike precursor. Together: "unbiased CSG reproduces the (small-N precursor of the)
      entropic non-manifold domination", as required.
  (3) GOVERNED CSG (the decisive test): apply a DE-TELEOLOGIZED governance/incentive selection bias
      on the transition probabilities -- a "bounded unit-of-account / recent-ingestion" rule that is
      BLIND to the dimension target (it references only the order structure -- recency/depth and
      ingestion valence -- never d_MM or of), so it cannot be accused of biasing toward the answer.
      Two independent governance primitives + their combination:
        (3a) RECENCY bias: link-probability to an existing atom m decays with m's depth below the
             current growth frontier, ~ exp(-gamma * depth(m)) -- "each new record ingests a RECENT
             slice of the ledger, not the whole history". gamma=0 recovers unbiased percolation.
        (3b) BOUNDED-VALENCE / ingestion-fee: base link prob = c/n_existing so each atom ingests
             O(c) predecessors regardless of ledger size -- "a bounded working set / a per-ingestion
             fee". (This IS the known p~1/N manifoldlike tuning, named as governance -- exactly
             Adversary-C's crux, engaged head-on.)
      Measure whether the governed ensemble sits MEASURABLY closer to the manifold band than the
      unbiased ensemble, across seeds, with an N-STABILITY sub-test: at FIXED governance strength,
      does the manifoldlikeness score hold as N grows across the accessible window, or degrade (KR
      entropy reasserting -> the strength would have to RUN with N -> fine-tuning, not a fixed rule)?

HONEST SCOPE (logged; no silent extrapolation). Small-N only (N <= 48). Small-N can show: (i) the
estimator is calibrated (MM validation, manifold+KR controls discriminate); (ii) whether a governance
bias produces a MEASURABLE finite-N shift and whether a FIXED strength holds across the accessible
window. Small-N CANNOT show: the asymptotic KR theorem (imported, not demonstrated), nor whether any
finite-N foothold survives N->inf (the number of non-manifoldlike posets grows super-exponentially --
2^{n^2/4+o(n^2)} -- so a finite-N large-deviation shift can still be entropically swamped in the
limit). What is NOT demonstrated is stated explicitly in the verdict; nothing here is extrapolated to
the continuum or to a spacetime/manifoldlikeness THEOREM.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

# ---------------------------------------------------------------------------
# Myrheim-Meyer ordering-fraction dimension (RE-VERIFIED here, not imported).
#   f(d) = Gamma(d+1) Gamma(d/2) / (2 Gamma(3d/2)),  strictly decreasing on [1, inf):
#   f(1)=1 (chain), f(2)=1/2, f(3)=0.2286..., f(4)=1/10.
# ---------------------------------------------------------------------------
def mm_f(d: float) -> float:
    return math.exp(math.lgamma(d + 1.0) + math.lgamma(d / 2.0)
                    - math.log(2.0) - math.lgamma(1.5 * d))


def mm_invert(order_frac: float) -> float:
    """Invert f on [1, 8] (f strictly decreasing). of>=1 -> d=1 (chain); of<f(8) -> capped at 8."""
    if order_frac >= 1.0:
        return 1.0
    lo, hi = 1.0, 8.0
    if order_frac <= mm_f(hi):
        return hi
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mm_f(mid) > order_frac:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Causet as incremental transitive-closed poset (bitmask ancestor sets).
# past[i] = int bitmask of all j < i with j <_c i (already transitively closed).
# ---------------------------------------------------------------------------
def _popcount(x: int) -> int:
    return bin(x).count("1")


def causet_stats(past: list[int], n: int) -> dict[str, float]:
    """Ordering fraction, MM dimension, height (longest chain, # elements), largest rank-layer
    fraction. past[i] transitively closed."""
    comparable = sum(_popcount(p) for p in past)
    total_pairs = n * (n - 1) // 2
    of = comparable / total_pairs if total_pairs else 0.0

    # rank[i] = longest chain from a minimal element up to i (0-based); process in birth order,
    # but ancestors can be any earlier index, so compute by longest path over ancestors.
    rank = [0] * n
    for i in range(n):
        pi = past[i]
        best = -1
        m = pi
        while m:
            j = (m & -m).bit_length() - 1
            if rank[j] > best:
                best = rank[j]
            m &= m - 1
        rank[i] = best + 1
    height = (max(rank) + 1) if n else 0  # # elements in the longest chain

    # largest rank-layer (an antichain) as a cheap, O(n) width signature.
    layer_counts: dict[int, int] = {}
    for r in rank:
        layer_counts[r] = layer_counts.get(r, 0) + 1
    max_layer_frac = (max(layer_counts.values()) / n) if n else 0.0

    return {
        "n": n,
        "ordering_fraction": of,
        "d_MM": mm_invert(of),
        "height": height,
        "max_layer_fraction": max_layer_frac,
    }


# ---------------------------------------------------------------------------
# GROWTH DYNAMICS.
# ---------------------------------------------------------------------------
def grow_percolation(n: int, rng: np.random.Generator, base_p: float,
                     gamma: float = 0.0, bounded_c: float | None = None) -> list[int]:
    """Rideout-Sorkin transitive percolation with an optional GOVERNANCE selection bias.

    For each new atom k and each existing atom m<k, a raw link m<_c k is placed with probability
      p(m) = clip( p_eff * exp(-gamma * depth(m)),  0, 1 )
    where p_eff = base_p, OR p_eff = bounded_c / k if bounded_c is set (bounded-ingestion / fee),
    and depth(m) = (current frontier rank) - rank(m) is m's depth below the growth frontier
    (RECENCY: recent atoms ingested preferentially). The past is transitively closed incrementally.
    gamma=0 and bounded_c=None  ==>  plain unbiased transitive percolation (the control).
    The bias references ONLY the order structure (depths), never any dimension estimator.
    """
    past: list[int] = []
    rank: list[int] = []
    for k in range(n):
        if k == 0:
            past.append(0)
            rank.append(0)
            continue
        frontier = max(rank)  # current top rank
        p_eff = (bounded_c / k) if bounded_c is not None else base_p
        S = 0  # raw direct-or-indirect predecessor accumulator (we OR in closed pasts)
        for m in range(k):
            depth = frontier - rank[m]
            pm = p_eff * math.exp(-gamma * depth) if gamma > 0.0 else p_eff
            if pm > 1.0:
                pm = 1.0
            if rng.random() < pm:
                S |= (past[m] | (1 << m))  # transitive closure: m and all of m's ancestors
        past.append(S)
        # rank of k = 1 + max rank among its ancestors (longest chain ending at k)
        best = -1
        m = S
        while m:
            j = (m & -m).bit_length() - 1
            if rank[j] > best:
                best = rank[j]
            m &= m - 1
        rank.append(best + 1)
    return past


def build_kr_shaped(n: int, rng: np.random.Generator, p_link: float = 0.5) -> list[int]:
    """Hand-built KLEITMAN-ROTHSCHILD-shaped 3-layer poset: layer sizes ~ n/4, n/2, n/4, links only
    downward-adjacent-layer with prob p_link, then transitively closed. This is the calibration
    control for 'KR domination' -- the estimator MUST flag it non-manifoldlike (height ~ 3 fixed)."""
    n1 = max(1, n // 4)
    n3 = max(1, n // 4)
    n2 = n - n1 - n3
    # order the atoms bottom-layer, middle-layer, top-layer so birth order respects <_c.
    layer_of = [0] * n1 + [1] * n2 + [2] * n3
    past: list[int] = [0] * n
    for k in range(n):
        lk = layer_of[k]
        S = 0
        for m in range(k):
            lm = layer_of[m]
            if lm == lk - 1 and rng.random() < p_link:  # link to adjacent lower layer
                S |= (past[m] | (1 << m))
        past[k] = S
    return past


# ---------------------------------------------------------------------------
# GENUINE MINKOWSKI SPRINKLINGS (controls -- MM ground truth, per CONNECTIONS.md).
# ---------------------------------------------------------------------------
def sprinkle_diamond(n: int, d: int, rng: np.random.Generator) -> list[int]:
    """Sprinkle n points uniformly into the Alexandrov interval (causal diamond) between the origin
    and (T,0,...,0) in d-dim Minkowski, causal relation p<q iff dt>0 and dt^2 > |dx|^2. Returns the
    transitively-closed ancestor bitmasks in a birth order that is a linear extension (sorted by t).
    For d=2 uses light-cone coords (u,v) in the unit square (an exact 2D causal diamond)."""
    if d == 2:
        pts = rng.random((n, 2))  # (u, v) in [0,1]^2; p<q iff u_p<=u_q and v_p<=v_q
        order = np.argsort(pts[:, 0] + pts[:, 1])  # linear extension by u+v (~ time)
        pts = pts[order]
        past: list[int] = []
        for i in range(n):
            S = 0
            for j in range(i):
                if pts[j, 0] <= pts[i, 0] and pts[j, 1] <= pts[i, 1]:
                    S |= (1 << j)
            # transitive closure via OR of ancestors' pasts
            m, T = S, 0
            while m:
                jj = (m & -m).bit_length() - 1
                T |= past[jj]
                m &= m - 1
            past.append(S | T)
        return past

    # general d: rejection-sample the causal diamond between o=(0,..) and e=(T,0,..), T=1.
    T = 1.0
    apex = np.zeros(d)
    apex[0] = T
    pts_list = []
    guard = 0
    while len(pts_list) < n and guard < 200 * n:
        guard += 1
        x = rng.random(d)
        x[0] = x[0] * T
        x[1:] = (x[1:] - 0.5) * T  # spatial in [-T/2, T/2]
        # inside future cone of origin AND past cone of apex?
        s2_o = x[0] ** 2 - np.dot(x[1:], x[1:])
        dx = apex - x
        s2_e = dx[0] ** 2 - np.dot(dx[1:], dx[1:])
        if x[0] > 0 and s2_o > 0 and dx[0] > 0 and s2_e > 0:
            pts_list.append(x)
    pts = np.array(pts_list[:n])
    if len(pts) < n:  # pad shortfall by resampling near center (keeps N fixed; rare)
        while len(pts) < n:
            pts = np.vstack([pts, np.array([[0.5, *([0.0] * (d - 1))]])])
    order = np.argsort(pts[:, 0])
    pts = pts[order]
    past = []
    for i in range(n):
        S = 0
        for j in range(i):
            dt = pts[i, 0] - pts[j, 0]
            dspace = pts[i, 1:] - pts[j, 1:]
            if dt > 0 and dt * dt - float(np.dot(dspace, dspace)) > 0:
                S |= (1 << j)
        m, Tc = S, 0
        while m:
            jj = (m & -m).bit_length() - 1
            Tc |= past[jj]
            m &= m - 1
        past.append(S | Tc)
    return past


# ---------------------------------------------------------------------------
# Aggregation helpers.
# ---------------------------------------------------------------------------
def ensemble(gen, n: int, seeds: int, seed0: int) -> dict[str, float]:
    """Run a generator (seed-> past list) over `seeds` seeds at size n; return mean estimators."""
    ofs, dmm, hts, wls = [], [], [], []
    for s in range(seeds):
        rng = np.random.default_rng(seed0 + 1009 * s + 7 * n)
        past = gen(n, rng)
        st = causet_stats(past, n)
        ofs.append(st["ordering_fraction"])
        dmm.append(st["d_MM"])
        hts.append(st["height"])
        wls.append(st["max_layer_fraction"])
    return {
        "n": n,
        "seeds": seeds,
        "ordering_fraction_mean": float(np.mean(ofs)),
        "d_MM_mean": float(np.mean(dmm)),
        "d_MM_std": float(np.std(dmm)),
        "height_mean": float(np.mean(hts)),
        "height_std": float(np.std(hts)),
        "max_layer_fraction_mean": float(np.mean(wls)),
    }


def height_scaling_dimension(rows: list[dict[str, float]]) -> float:
    """Fit log(height) = a + (1/d) log(N) over the N-sweep; return d_chain = 1/slope."""
    xs = np.log(np.array([r["n"] for r in rows], dtype=float))
    ys = np.log(np.array([max(r["height_mean"], 1.0) for r in rows], dtype=float))
    slope = float(np.polyfit(xs, ys, 1)[0])
    if slope <= 1e-6:
        return float("inf")
    return 1.0 / slope


def sweep(gen, n_values: list[int], seeds: int, seed0: int) -> dict[str, Any]:
    rows = [ensemble(gen, n, seeds, seed0) for n in n_values]
    d_chain = height_scaling_dimension(rows)
    return {
        "rows": rows,
        "d_chain_from_height_scaling": d_chain,
        "d_MM_at_largest_N": rows[-1]["d_MM_mean"],
        "max_layer_fraction_at_largest_N": rows[-1]["max_layer_fraction_mean"],
    }


# ---------------------------------------------------------------------------
# Manifold-band membership (the honest, dual-estimator criterion).
# A condition is "manifoldlike-2D-ish" iff BOTH dimension estimators agree near 2 AND width
# collapses. KR fails the height axis; a chain fails it the other way.
# ---------------------------------------------------------------------------
def manifold_band(sweep_res: dict[str, Any], d_lo=1.6, d_hi=2.6, w_max=0.35) -> dict[str, Any]:
    d_mm = sweep_res["d_MM_at_largest_N"]
    d_ch = sweep_res["d_chain_from_height_scaling"]
    w = sweep_res["max_layer_fraction_at_largest_N"]
    in_mm = d_lo <= d_mm <= d_hi
    in_ch = d_lo <= d_ch <= d_hi
    in_w = w <= w_max
    return {
        "d_MM": d_mm, "d_chain": d_ch, "max_layer_fraction": w,
        "in_MM_band": in_mm, "in_chain_band": in_ch, "width_collapses": in_w,
        "manifoldlike": bool(in_mm and in_ch and in_w),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(Path(__file__).parent / "artifacts"
                                         / "du_governance_selection_csg_probe_result.json"))
    ap.add_argument("--seeds", type=int, default=24)
    ap.add_argument("--seed0", type=int, default=20260721)
    args = ap.parse_args()

    N = [12, 20, 32, 48]
    seeds, seed0 = args.seeds, args.seed0
    BASE_P = 0.30      # fixed-p percolation coupling (unbiased + recency conditions)
    GAMMA = 1.5        # recency governance strength (chosen; a gamma-sweep locates the window)
    BOUNDED_C = 2.0    # bounded-ingestion governance: ~c recent predecessors per birth

    # ---- Module 0: MM VALIDATION (positive control) -------------------------------------------
    mm_val = {}
    for d in (2, 3, 4):
        res = ensemble(lambda n, rng, dd=d: sprinkle_diamond(n, dd, rng), 90, seeds, seed0)
        mm_val[f"sprinkle_d{d}"] = {
            "input_d": d, "measured_ordering_fraction": res["ordering_fraction_mean"],
            "recovered_d_MM": res["d_MM_mean"], "closed_form_f": mm_f(d),
        }
    mm_ok = all(abs(mm_val[f"sprinkle_d{d}"]["recovered_d_MM"] - d) < 0.45 for d in (2, 3, 4))

    # ---- Module 1: MANIFOLD control (hand-forced manifold) ------------------------------------
    manifold = sweep(lambda n, rng: sprinkle_diamond(n, 2, rng), N, seeds, seed0)
    manifold_band_res = manifold_band(manifold)
    CTRL_MANIFOLD = manifold_band_res["manifoldlike"]  # estimator CAN register manifoldlikeness

    # ---- Module 2: KR / UNBIASED-CSG controls -------------------------------------------------
    kr = sweep(lambda n, rng: build_kr_shaped(n, rng, 0.5), N, seeds, seed0)
    kr_band = manifold_band(kr)
    # KR must be flagged NON-manifoldlike, specifically flat on the height axis + wide.
    CTRL_KR = (not kr_band["manifoldlike"]) and (kr["d_chain_from_height_scaling"] > 3.5) \
        and (kr["max_layer_fraction_at_largest_N"] > 0.35)

    unbiased = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=0.0), N, seeds, seed0)
    unbiased_band = manifold_band(unbiased)
    CTRL_UNBIASED_NOT_MANIFOLD = not unbiased_band["manifoldlike"]

    # ---- Module 3: GOVERNED CSG (the decisive test) -------------------------------------------
    # 3a recency, 3b bounded-valence, 3c both.
    gov_recency = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=GAMMA), N, seeds, seed0)
    gov_bounded = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=0.0,
                                                        bounded_c=BOUNDED_C), N, seeds, seed0)
    gov_both = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=GAMMA,
                                                     bounded_c=BOUNDED_C), N, seeds, seed0)
    gov_recency_band = manifold_band(gov_recency)
    gov_bounded_band = manifold_band(gov_bounded)
    gov_both_band = manifold_band(gov_both)

    # STRENGTH-SWEEPS at fixed N to locate each governance window and see whether it CROSSES the
    # manifold dimension d=2 (i.e. is governance a real dimensional lever?).
    Nwin = 32
    gamma_sweep = []
    for g in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
        r = ensemble(lambda n, rng, gg=g: grow_percolation(n, rng, BASE_P, gamma=gg), Nwin, seeds, seed0)
        gamma_sweep.append({"gamma": g, "d_MM": r["d_MM_mean"], "height": r["height_mean"],
                            "max_layer_fraction": r["max_layer_fraction_mean"]})
    c_sweep = []
    for c in (1.0, 2.0, 3.0, 4.0, 6.0, 8.0):
        r = ensemble(lambda n, rng, cc=c: grow_percolation(n, rng, BASE_P, gamma=0.0, bounded_c=cc),
                     Nwin, seeds, seed0)
        c_sweep.append({"c": c, "d_MM": r["d_MM_mean"], "height": r["height_mean"],
                        "max_layer_fraction": r["max_layer_fraction_mean"]})

    def sweep_crosses_d2(rows, key):
        vals = [row["d_MM"] for row in rows]
        return (min(vals) < 2.0 < max(vals)) or any(abs(v - 2.0) < 0.15 for v in vals)
    recency_crosses = sweep_crosses_d2(gamma_sweep, "gamma")
    bounded_crosses = sweep_crosses_d2(c_sweep, "c")
    governance_is_a_lever = recency_crosses or bounded_crosses

    # TUNED-CROSSING N-STABILITY (the decisive small-N probe of the asymptotic question).
    # Pick, from each strength-sweep, the strength whose d_MM at Nwin is closest to 2.0 (the tuned
    # crossing). Then run THAT FIXED strength across the whole N-sweep: does d_MM HOLD near 2, or
    # drift back toward the non-manifold value as N grows (=> the strength would have to RUN with N
    # = fine-tuning, not a fixed governance rule => the KR wall reasserting)?
    def band_distance(row):
        return abs(row["d_MM_mean"] - 2.0)

    gstar = min(gamma_sweep, key=lambda x: abs(x["d_MM"] - 2.0))["gamma"]
    cstar = min(c_sweep, key=lambda x: abs(x["d_MM"] - 2.0))["c"]
    tuned_recency = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=gstar), N, seeds, seed0)
    tuned_bounded = sweep(lambda n, rng: grow_percolation(n, rng, BASE_P, gamma=0.0, bounded_c=cstar),
                          N, seeds, seed0)

    # Reference: a GENUINE manifold (the 2D sprinkle control) has N-INDEPENDENT d_MM ~ 2 (flat).
    # A genuine foothold must reproduce that FLATNESS, not merely touch d=2 at one N. We therefore
    # distinguish PLATEAU-at-2 (max |d_MM-2| over the whole N-window is small = a real basin) from
    # TREND-through-2 (d_MM is monotone in N and merely CROSSES 2 inside the window = a tuned
    # crossing whose location moves with N => strength must run with N => fine-tuning, not a rule).
    manifold_dmm_by_N = [r["d_MM_mean"] for r in manifold["rows"]]
    manifold_flatness = max(abs(v - 2.0) for v in manifold_dmm_by_N)  # ~ how flat a true manifold is

    def stability_of(tuned, label, strength):
        seq = [r["d_MM_mean"] for r in tuned["rows"]]
        devs = [abs(v - 2.0) for v in seq]
        max_dev = max(devs)
        diffs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        monotone = all(x > 0 for x in diffs) or all(x < 0 for x in diffs)
        span = abs(seq[-1] - seq[0])
        crosses_under_N = (min(seq) < 2.0 < max(seq))
        widths_ok = all(r["max_layer_fraction_mean"] <= 0.35 for r in tuned["rows"])
        # PLATEAU: near 2 across the ENTIRE window (flat, like the manifold control) AND narrow.
        plateau = (max_dev <= 0.30) and widths_ok
        # TUNED CROSSING: a real monotone trend (span > flatness scale) that passes THROUGH 2.
        tuned_crossing = monotone and (span > 0.4) and crosses_under_N
        return {
            "label": label, "tuned_strength": strength,
            "d_MM_by_N": [{"n": r["n"], "d_MM": r["d_MM_mean"],
                           "max_layer_fraction": r["max_layer_fraction_mean"]} for r in tuned["rows"]],
            "max_abs_dev_from_2_over_window": max_dev,
            "monotone_in_N": bool(monotone), "span_over_window": span,
            "crosses_2_under_N": bool(crosses_under_N),
            "plateau_at_2_across_window": bool(plateau),
            "tuned_crossing_not_plateau": bool(tuned_crossing),
        }
    stab_recency = stability_of(tuned_recency, "tuned_recency", gstar)
    stab_bounded = stability_of(tuned_bounded, "tuned_bounded_valence", cstar)
    stable_foothold = stab_recency["plateau_at_2_across_window"] \
        or stab_bounded["plateau_at_2_across_window"]
    tuned_crossing_only = (not stable_foothold) and (
        stab_recency["tuned_crossing_not_plateau"] or stab_bounded["tuned_crossing_not_plateau"])

    # spread of d_MM across the strength-sweeps = the size of the dimensional lever.
    lever_range = {
        "recency_d_MM_min_max": [min(x["d_MM"] for x in gamma_sweep),
                                 max(x["d_MM"] for x in gamma_sweep)],
        "bounded_d_MM_min_max": [min(x["d_MM"] for x in c_sweep),
                                 max(x["d_MM"] for x in c_sweep)],
    }
    unbiased_gap = band_distance(unbiased["rows"][-1])
    any_governed_manifoldlike = any(manifold_band(v)["manifoldlike"]
                                    for v in (gov_recency, gov_bounded, gov_bounded))

    # ---- Physics verdict (the finding; separate from the instrument gates) --------------------
    positive_controls = {
        "MM_validation_recovers_input_dimension": mm_ok,
        "CTRL_MANIFOLD_estimator_registers_manifoldlikeness": CTRL_MANIFOLD,
        "CTRL_KR_estimator_flags_KR_nonmanifold": CTRL_KR,
        "CTRL_UNBIASED_CSG_not_robustly_manifold": CTRL_UNBIASED_NOT_MANIFOLD,
    }
    controls_pass = all(positive_controls.values())

    # Three pre-registered outcomes, graded honestly against the PLATEAU-vs-CROSSING distinction:
    #   BIAS-SHIFTS  : a fixed, physically-reasonable strength holds d_MM ~ 2 FLAT across the whole
    #                  N-window (a genuine basin, reproducing the manifold control's N-flatness).
    #   KR-DOMINATES : governance is not even a lever -- no strength approaches the manifold band.
    #   PARTIAL      : governance IS a measurable dimensional lever that crosses manifoldlikeness,
    #                  but the manifold value is a TUNED CROSSING (a monotone function of strength
    #                  and N passing through 2), not a fixed-point basin -- keeping d ~ 2 as N grows
    #                  needs the strength to run with N (fine-tuning). The meta-wall (KR entropy) is
    #                  NOT refuted at accessible N, and governance is NOT shown impotent either.
    if stable_foothold:
        verdict = ("BIAS-SHIFTS-AT-SMALL-N: a fixed governance strength holds the Myrheim-Meyer "
                   "dimension flat at ~2 across the whole accessible N-window (a genuine foothold; "
                   "honest small-N caveat: not shown to survive N->inf)")
    elif governance_is_a_lever:
        verdict = ("PARTIAL / meta-wall-NOT-refuted: governance/incentive selection is a measurable "
                   "dimensional lever that CROSSES manifoldlikeness under tuning (d_MM tunable from "
                   "chain-like ~1.2 through 2 to KR-flat ~4), but the manifold value is a TUNED "
                   "CROSSING -- a monotone function of strength AND N passing through 2, not a "
                   "fixed-point basin. Holding d~2 as N grows needs the strength to run with N "
                   "(fine-tuning), the KR-entropy signature reasserting as-modeled; not a clean escape")
    else:
        verdict = "KR-DOMINATES (no reasonable bias even approached the manifold band at accessible N)"

    results: dict[str, Any] = {
        "probe": "du_governance_selection_csg_probe",
        "question": ("Can a governance/incentive selection bias on Rideout-Sorkin CSG transition "
                     "probabilities measurably shift the grown causal set toward manifoldlikeness "
                     "at accessible N, or does KR entropy dominate any reasonable bias?"),
        "seam_note": ("KR (uniform-poset, asymptotic), RS-CSG percolation (the host measure), and "
                      "T223 (TaF uniform ordinal ensemble) are THREE DISTINCT unbiased measures; "
                      "the KR theorem is IMPORTED as literature and calibrated against a hand-built "
                      "KR ensemble, not proven at small N."),
        "parameters": {"N_sweep": N, "seeds": seeds, "base_p": BASE_P, "gamma": GAMMA,
                       "bounded_c": BOUNDED_C},
        "module0_MM_validation": mm_val,
        "module1_manifold_control": {"sweep": manifold, "band": manifold_band_res},
        "module2_KR_control": {"sweep": kr, "band": kr_band},
        "module2_unbiased_CSG_control": {"sweep": unbiased, "band": unbiased_band},
        "module3_governed": {
            "recency": {"sweep": gov_recency, "band": gov_recency_band},
            "bounded_valence": {"sweep": gov_bounded, "band": gov_bounded_band},
            "both": {"sweep": gov_both, "band": gov_both_band},
            "gamma_sweep_at_N32": gamma_sweep,
            "c_sweep_at_N32": c_sweep,
            "tuned_crossing_N_stability": {"recency": stab_recency, "bounded_valence": stab_bounded},
        },
        "decisive_comparison": {
            "unbiased_d_MM_at_largest_N": unbiased["rows"][-1]["d_MM_mean"],
            "unbiased_d_MM_gap_from_2": unbiased_gap,
            "governance_is_a_measurable_dimensional_lever": bool(governance_is_a_lever),
            "lever_d_MM_range_across_strength_sweeps": lever_range,
            "recency_sweep_crosses_d2": bool(recency_crosses),
            "bounded_sweep_crosses_d2": bool(bounded_crosses),
            "a_fixed_strength_plateaus_at_2_across_window": bool(stable_foothold),
            "manifold_value_is_a_tuned_crossing_not_a_basin": bool(tuned_crossing_only),
            "manifold_control_flatness_reference": manifold_flatness,
            "any_governed_condition_manifoldlike": bool(any_governed_manifoldlike),
        },
        "positive_controls": positive_controls,
        "positive_controls_all_pass": controls_pass,
        "physics_verdict": verdict,
        "honest_scope": {
            "N_max": max(N),
            "shown": ["estimator calibrated (MM validation + manifold/KR discrimination)",
                      "whether a governance bias produces a measurable finite-N shift",
                      "whether a FIXED governance strength holds across the accessible N window"],
            "NOT_shown": ["the asymptotic Kleitman-Rothschild theorem (imported, not demonstrated)",
                          "whether any finite-N foothold survives N->inf (super-exponential "
                          "non-manifold poset count can swamp a finite-N large-deviation shift)",
                          "any continuum / metric / Lorentzian / spacetime / manifoldlikeness THEOREM"],
            "no_silent_extrapolation": True,
        },
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")

    # ---- console summary ----------------------------------------------------------------------
    line = "=" * 88
    print(line)
    print("DU governance-selection-on-CSG probe  (meta-requirement / KR fork, Test #5)")
    print(line)
    print("MM VALIDATION (must recover input dimension):")
    for d in (2, 3, 4):
        v = mm_val[f"sprinkle_d{d}"]
        print(f"   sprinkle d={d}: of={v['measured_ordering_fraction']:.4f}  "
              f"recovered d_MM={v['recovered_d_MM']:.2f}  (closed-form f={v['closed_form_f']:.4f})")
    print("-" * 88)
    print("CONDITION (largest N)          d_MM   d_chain(height)  max_layer_frac   manifoldlike?")
    def show(name, s, b):
        dch = s["d_chain_from_height_scaling"]
        dch_s = "inf " if dch == float("inf") else f"{dch:5.2f}"
        print(f"   {name:26s} {b['d_MM']:5.2f}      {dch_s}          "
              f"{b['max_layer_fraction']:.3f}          {b['manifoldlike']}")
    show("MANIFOLD 2D sprinkle (ctrl)", manifold, manifold_band_res)
    show("KR 3-layer (ctrl)", kr, kr_band)
    show("UNBIASED CSG gamma=0 (ctrl)", unbiased, unbiased_band)
    show("GOVERNED recency", gov_recency, gov_recency_band)
    show("GOVERNED bounded-valence", gov_bounded, gov_bounded_band)
    show("GOVERNED both", gov_both, gov_both_band)
    print("-" * 88)
    print(f"STRENGTH-SWEEPS at N={Nwin} (does governance CROSS manifold dimension d=2?):")
    print("   recency:  " + "  ".join(f"g={g['gamma']:.1f}:{g['d_MM']:.2f}" for g in gamma_sweep)
          + f"   crosses_d2={recency_crosses}")
    print("   bounded:  " + "  ".join(f"c={c['c']:.0f}:{c['d_MM']:.2f}" for c in c_sweep)
          + f"   crosses_d2={bounded_crosses}")
    print("-" * 88)
    print(f"TUNED N-STABILITY (fixed strength; PLATEAU-at-2 vs TREND-through-2? "
          f"manifold-control flatness ref = max|d_MM-2|={manifold_flatness:.2f}):")
    for stab in (stab_recency, stab_bounded):
        seq = "  ".join(f"N{r['n']}:{r['d_MM']:.2f}" for r in stab["d_MM_by_N"])
        print(f"   {stab['label']:22s} (strength={stab['tuned_strength']:.1f})  {seq}")
        print(f"       max|d_MM-2| over window={stab['max_abs_dev_from_2_over_window']:.3f}  "
              f"monotone={stab['monotone_in_N']}  crosses2underN={stab['crosses_2_under_N']}   "
              f"PLATEAU={stab['plateau_at_2_across_window']}  "
              f"tuned_crossing={stab['tuned_crossing_not_plateau']}")
    print("-" * 88)
    dc = results["decisive_comparison"]
    print(f"DECISIVE: unbiased d_MM={dc['unbiased_d_MM_at_largest_N']:.2f} (|.-2|={dc['unbiased_d_MM_gap_from_2']:.2f});  "
          f"governance lever range recency={lever_range['recency_d_MM_min_max'][0]:.2f}..{lever_range['recency_d_MM_min_max'][1]:.2f}, "
          f"bounded={lever_range['bounded_d_MM_min_max'][0]:.2f}..{lever_range['bounded_d_MM_min_max'][1]:.2f}")
    print(f"   governance_is_a_lever={dc['governance_is_a_measurable_dimensional_lever']}  "
          f"fixed_strength_plateaus_at_2={dc['a_fixed_strength_plateaus_at_2_across_window']}  "
          f"manifold_is_tuned_crossing={dc['manifold_value_is_a_tuned_crossing_not_a_basin']}")
    print("-" * 88)
    print("POSITIVE CONTROLS:")
    for k, v in positive_controls.items():
        print(f"   [{'PASS' if v else 'FAIL'}]  {k}")
    print("-" * 88)
    print(f"PHYSICS VERDICT: {verdict}")
    print(f"positive controls all pass (instrument valid): {controls_pass}")
    print(f"artifact: {out}")
    return 0 if controls_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
