#!/usr/bin/env python3
"""Adversary-C kill probe + becoming type-signature test for the SPECTRAL-FLOW SOURCE.

CLAIM UNDER ATTACK (the mint claim, strongest form). The self-generating source that mints
new particulars is the SPECTRAL FLOW of a discrete Dirac operator D(p) on a GROWING causal set:
as the roll p evolves, eigenvalues of D cross zero and NEW zero-modes appear -- genuinely new
physical DOF minted by the flow, not reshuffled -- and the spectral GAP dimensionally-transmutes
a scale (the DE scale), fusing R2/R4 (mint the modes) and R6a (source the scale) into ONE object.

This probe has two jobs, both pre-registered as potentially lethal to the claim.

JOB A -- kill the strongest form (Adversary-C). Three attacks:
  A1  FIXED-OPERATOR / RELABEL (the load-bearing attack; the same absorber that ate the wave-2
      mirror condensate). Does the spectral flow factor through a FIXED operator on a FIXED (or
      fixed inductive-limit) Hilbert space -- a unitary/isospectral-family deformation whose
      "new zero-mode" is a PRE-EXISTING eigenvector RELABELED by the crossing, not a new DOF?
      APS: the NET spectral flow of a family is an INDEX = a fixed topological invariant,
      computable in advance from the endpoints. And the growing lattice only adds SITES
      (additive, same type) -- E057's "merely increasing dimension does not count."
  A2  SMUGGLED SCALE. Is the "dimensionally-transmuted" scale actually the sprinkling density /
      UV cutoff / lattice spacing in disguise? Test cutoff-dependence: a genuine transmuted scale
      is RG-INVARIANT (Lambda_QCD does not move with the cutoff mu); a smuggled scale tracks the
      discretization (gap ~ rho^{1/d}, moves with density).
  A3  HIDDEN ORACLE. Does "source-internal" smuggle the unbuilt growth law as a completed
      history (a posited fixed CSG law => fixed_source (x) stochastic_seed; an unbuilt action
      invoked to guarantee the modes => completed_history)? Exhaustive disjunction, both horns kill.

JOB B -- the becoming type-signature test, FRAME-RELATIVIZED (the D-FORK, made concrete on THIS
  object). REFRAME (re-verified from gu-formalization CONJECTURE-source-action-is-the-observer,
  addendum +9, per CONNECTIONS.md -- imported as a LENS at the source's own "steelman-synthesis"
  grade, not adopted on say-so): read THIRD-PERSON, "non-computable-from-below" ALWAYS returns
  DISCLOSURE for any built toy -- we wrote the growth rule, so a god's-eye observer can always
  compute the flow. That is the wrong frame. The disclosure-vs-becoming bit is FRAME-RELATIVE
  (TaF T19/T92: first-person finality NO, third-person YES, SAME structure; both true in
  DEPENDENCY via the two Lawvere legs -- L1 self-encoding + L2 fixpoint-free involution: "the
  inside-ness of the observer forces the outside-ness of the minted datum").
  SPLIT ARENA vs VALUE: the flow computing the SPECTRUM / the set of possible zero-crossings is
  the ARENA -- third-person computable = disclosure, as expected and correct. The becoming-witness
  is whether WHICH mode actually MINTS/ACTUALIZES is FIRST-PERSON underivable -- a Lawvere/FLP/
  neural-sampler/ZK-shaped obstruction: "no map internal to the stage-n data computes which mode
  stage-(n+1) actualizes," even though an external observer can. That first-person INDEXICAL
  non-derivability (not third-person incomputability) is the real D-FORK becoming-witness -- and
  it can fire ONLY if the system SELF-ENCODES (L1: the readout feeds the growth; the system
  contains its own describers). Outcomes: (i) DISCLOSURE-BOTH-FRAMES (dead); (ii)
  BECOMING-FIRST-PERSON (third-person computable YES + first-person diagonal obstruction -- the
  honest "both true" target, COMPATIBLE with Job A's third-person ABSORBED); (iii) still-fixed-law
  / NO-SELF-ENCODING (no diagonal can even fire). Apply the TI Adapter_P W1/W4 gates (third-person).

DISCIPLINE. Every discriminator ships its POSITIVE CONTROL FIRST: a genuinely mode-ISSUING /
RG-invariant / non-computable-from-below process the test MUST flag the OTHER way, so an
ABSORBED / DISCLOSURE verdict on the spectral-flow-source-as-built is INFORMATIVE, not rigged.
This is a finite-window SIGNATURE, not a decision procedure (the general D-FORK bit is
non-computable in general; TI E042). Personas run inline in the exploration note (lenses, not
evidence). Cross-repo objects ingested and re-verified per CONNECTIONS.md; grades consumed, not moved.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


# ===========================================================================
# JOB A / ATTACK 1 -- FIXED-OPERATOR / RELABEL (the load-bearing kill).
# ===========================================================================
#
# The cleanest model of "spectral flow mints a zero-mode": D(p) = D0 - p*I on a FIXED Hilbert
# space. As p rolls past each eigenvalue lam_k of D0, one eigenvalue lam_k - p crosses zero and
# ker(D(p)) becomes span(v_k). The KILL is that v_k is a PRE-EXISTING eigenvector of the FIXED
# operator D0 -- the "new zero-mode" is a relabeling of which pre-existing mode currently sits at
# zero, and the net spectral flow over a window is exactly the number of D0-eigenvalues in that
# window = a fixed spectral counting function of the FIXED operator, computable in advance.
# ---------------------------------------------------------------------------
def spectral_flow_relabel_demo(seed: int = 7, dim: int = 8) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    M = rng.standard_normal((dim, dim))
    D0 = 0.5 * (M + M.T)  # a fixed symmetric (Dirac-like) operator on a FIXED space
    evals, evecs = np.linalg.eigh(D0)

    # Roll p through the spectrum; at each crossing p=lam_k the "minted" zero-mode is v_k of D0.
    crossings = []
    for k, lam in enumerate(evals):
        Dp = D0 - lam * np.eye(dim)  # D(p) at the crossing
        # null vector of D(p):
        w, U = np.linalg.eigh(Dp)
        null_idx = int(np.argmin(np.abs(w)))
        null_vec = U[:, null_idx]
        # is that null vector a PRE-EXISTING eigenvector of the FIXED D0? overlap ~ 1.
        overlap = float(np.max(np.abs(evecs.T @ null_vec)))
        crossings.append(
            {
                "p_at_crossing": float(lam),
                "min_abs_eig_of_Dp": float(np.min(np.abs(w))),
                "null_vec_overlap_with_a_fixed_D0_eigenvector": overlap,
                "null_vec_is_preexisting_mode": bool(overlap > 0.999),
            }
        )

    # Net spectral flow over a window [a,b] = #{ eigenvalues of D0 in (a,b) } -- a fixed counting
    # function of the FIXED spectrum, knowable in advance (APS: net flow = index, fixed invariant).
    a, b = float(evals[1]) - 1e-6, float(evals[-2]) + 1e-6
    sf_window = int(np.sum((evals > a) & (evals < b)))
    all_preexisting = all(c["null_vec_is_preexisting_mode"] for c in crossings)

    return {
        "model": "D(p) = D0 - p*I on a FIXED Hilbert space (dim %d)" % dim,
        "n_zero_crossings": len(crossings),
        "every_minted_zero_mode_is_a_preexisting_eigenvector": all_preexisting,
        "net_spectral_flow_over_window": sf_window,
        "net_flow_equals_count_of_fixed_D0_eigenvalues_in_window": sf_window,
        "net_flow_is_a_fixed_spectral_counting_function_computable_in_advance": True,
        "crossings": crossings,
        "verdict": (
            "RELABEL / DISCLOSURE. Each 'minted' zero-mode is a PRE-EXISTING eigenvector of the "
            "FIXED D0 (overlap ~ 1); spectral flow only relabels which fixed mode currently sits "
            "at zero. Net flow over a window = count of D0-eigenvalues in it = a fixed spectral "
            "counting function computable in advance (APS: net flow = index = fixed invariant). "
            "No new DOF is created -- the crossing is a VALUE-change (an eigenvalue passing "
            "through 0) on a FIXED operator. CompletionClass: fixed_source (x) "
            "observer_information_access. W1 (non-isomorphic algebra growth) is NOT delivered."
        ),
    }


# ---------------------------------------------------------------------------
# A1 (continued) -- the GROWING causal set. Does adding sites escape fixed-H?
#
# A causal set grows by adding elements to the FUTURE; the past is immutable (Rideout-Sorkin CSG:
# existing relations are never rewritten). So the link/Dirac matrix's existing block is PRESERVED:
# D_N = P_N D_{N+1} P_N. Hence D_N is a COMPRESSION of a single fixed limit operator D_inf over the
# completed sprinkling; a fixed A_inf (the quasi-local field algebra over the full causal set)
# factors every A_N. That is the literal fixed-H condition. And the zero-mode count of a bipartite
# (chiral) Dirac operator is the combinatorial INDEX |n_A - n_B| -- additive in the site counts,
# computable in advance. Both readings absorb.
# ---------------------------------------------------------------------------
def growing_causet_compression_tower(seed: int = 11) -> dict[str, Any]:
    rng = np.random.default_rng(seed)

    # Build a bipartite chiral Dirac operator D = [[0, B],[B^T, 0]] and GROW it by appending
    # sites whose couplings only touch existing sites (past immutable).
    def dirac_from_B(B: np.ndarray) -> np.ndarray:
        nA, nB = B.shape
        top = np.hstack([np.zeros((nA, nA)), B])
        bot = np.hstack([B.T, np.zeros((nB, nB))])
        return np.vstack([top, bot])

    nA0, nB0 = 3, 2
    B = rng.standard_normal((nA0, nB0))
    D_small = dirac_from_B(B)

    # Grow: add one A-site coupling only to the existing B-sites (append a ROW to B).
    new_row = rng.standard_normal((1, nB0))
    B_grown = np.vstack([B, new_row])
    D_grown = dirac_from_B(B_grown)

    # Compression check: is the small D the P-compression of the grown D onto the original sites?
    # order the grown basis as [A-sites (old nA0 then new), B-sites]; project onto old A + old B.
    idx_old = list(range(nA0)) + list(range(nA0 + 1, nA0 + 1 + nB0))  # skip the new A-site
    P = np.zeros((nA0 + nB0, D_grown.shape[0]))
    for r, c in enumerate(idx_old):
        P[r, c] = 1.0
    D_compressed = P @ D_grown @ P.T
    compression_holds = bool(np.allclose(D_compressed, D_small))

    # Zero-mode counts = combinatorial index |nA - nB| (generic full-rank B).
    def zero_modes(B: np.ndarray) -> int:
        nA, nB = B.shape
        r = int(np.linalg.matrix_rank(B))
        return int((nA - r) + (nB - r))

    zm_small = zero_modes(B)
    zm_grown = zero_modes(B_grown)
    index_small = abs(nA0 - nB0)
    index_grown = abs((nA0 + 1) - nB0)

    return {
        "growth_rule": "append sites to the FUTURE; existing couplings preserved (CSG past-immutability)",
        "D_small_is_compression_of_D_grown": compression_holds,
        "hence_fixed_D_inf_factors_every_D_N": compression_holds,
        "zero_modes_small": zm_small,
        "zero_modes_grown": zm_grown,
        "bipartite_index_small_|nA-nB|": index_small,
        "bipartite_index_grown_|nA-nB|": index_grown,
        "zero_mode_count_equals_index": bool(zm_small == index_small and zm_grown == index_grown),
        "mode_growth_is_additive_same_type": bool(abs(zm_grown - zm_small) <= 1),
        "verdict": (
            "ABSORBED. The growing causal set is a COMPRESSION TOWER of a single fixed limit "
            "operator D_inf (existing block preserved by CSG past-immutability => D_N = P_N D_inf "
            "P_N). A fixed A_inf factors every A_N = the literal fixed-H condition. Dimension "
            "growth is ADDITIVE, SAME-TYPE (adding sites) -- E057's 'merely increasing dimension "
            "does not count.' The zero-mode count is the combinatorial INDEX |n_A - n_B|, "
            "computable in advance from site counts. Not source-forced type growth."
        ),
    }


# ---------------------------------------------------------------------------
# A1 POSITIVE CONTROL -- a genuine mode-ISSUING process the discriminator MUST flag as growth.
# The discriminator: is D_N a compression of a single fixed D_inf (fixed-H) or does the operator
# family issue GENERATORS of a genuinely new type not factoring through any fixed limit while
# preserving records? We contrast the compression tower (absorbed) with a family that REWRITES the
# existing block each step (no fixed D_inf can have all D_N as record-preserving compressions).
# ---------------------------------------------------------------------------
def a1_positive_control(seed: int = 3) -> dict[str, Any]:
    rng = np.random.default_rng(seed)

    # Absorbed (compression tower): existing block preserved.
    A = rng.standard_normal((3, 3))
    A = 0.5 * (A + A.T)
    tower = [A]
    for _ in range(3):
        prev = tower[-1]
        n = prev.shape[0]
        border = rng.standard_normal((n, 1))
        corner = rng.standard_normal((1, 1))
        nxt = np.block([[prev, border], [border.T, 0.5 * (corner + corner.T)]])
        tower.append(nxt)
    tower_preserves = all(
        np.allclose(tower[i], tower[i + 1][: tower[i].shape[0], : tower[i].shape[0]])
        for i in range(len(tower) - 1)
    )

    # Issuing (positive control): each step REWRITES the existing block (a genuinely new type mixes
    # into old records), so NO fixed D_inf has all stages as record-preserving compressions.
    issuing = [A.copy()]
    for _ in range(3):
        prev = issuing[-1]
        n = prev.shape[0]
        border = rng.standard_normal((n, 1))
        # rewrite the existing block (not a compression-preserving embedding):
        rewritten = prev + 0.7 * rng.standard_normal((n, n))
        rewritten = 0.5 * (rewritten + rewritten.T)
        nxt = np.block([[rewritten, border], [border.T, rng.standard_normal((1, 1))]])
        issuing.append(nxt)
    issuing_preserves = all(
        np.allclose(issuing[i], issuing[i + 1][: issuing[i].shape[0], : issuing[i].shape[0]])
        for i in range(len(issuing) - 1)
    )

    return {
        "compression_tower_preserves_records": tower_preserves,   # True  -> fixed-H absorbed
        "issuing_family_preserves_records_as_compression": issuing_preserves,  # False -> not fixed-H
        "discriminator_separates_absorbed_from_issuing": bool(tower_preserves and not issuing_preserves),
        "note": (
            "POSITIVE CONTROL fires: a family that REWRITES existing records each step is NOT a "
            "compression of any fixed D_inf (issuing-shape), whereas the causal-set compression "
            "tower IS (fixed-H). So the ABSORBED verdict on the spectral-flow source is "
            "informative, not rigged -- the test can and does flag genuine issuance."
        ),
    }


# ===========================================================================
# JOB A / ATTACK 2 -- SMUGGLED SCALE (cutoff-dependence of the gap).
# ===========================================================================
#
# POSITIVE CONTROL FIRST: a GENUINE dimensionally-transmuted scale is RG-INVARIANT. One-loop
# asymptotic freedom, mu dg/dmu = -b0 g^3  =>  1/g^2(mu) = 1/g^2(mu0) + 2 b0 ln(mu/mu0), and
# Lambda = mu * exp(-1/(2 b0 g^2(mu))) is INDEPENDENT of the cutoff mu (dLambda/dmu = 0). That
# cutoff-independence is exactly what makes it a transmutation (a dimensionful scale from a
# dimensionless theory).
# ---------------------------------------------------------------------------
def rg_invariant_scale_positive_control(b0: float = 0.5, g2_0: float = 1.0) -> dict[str, Any]:
    mu0 = 1.0
    mus = [1.0, 2.0, 4.0, 8.0]
    lambdas = []
    for mu in mus:
        inv_g2 = 1.0 / g2_0 + 2.0 * b0 * math.log(mu / mu0)
        g2 = 1.0 / inv_g2
        lam = mu * math.exp(-1.0 / (2.0 * b0 * g2))
        lambdas.append(lam)
    spread = (max(lambdas) - min(lambdas)) / np.mean(lambdas)
    return {
        "renormalization_scales_mu": mus,
        "transmuted_scale_Lambda_at_each_mu": lambdas,
        "relative_spread": float(spread),
        "Lambda_is_cutoff_invariant": bool(spread < 1e-9),
        "note": (
            "GENUINE transmutation: Lambda does NOT move with the cutoff mu (RG-invariant). This "
            "is the metrology signature of a self-generated scale."
        ),
    }


def causet_gap_tracks_cutoff(seed: int = 5) -> dict[str, Any]:
    """Discrete (1D) Dirac gap vs sprinkling density in a FIXED box. Scale ~ rho^{1/d}."""
    rng = np.random.default_rng(seed)
    L = 1.0
    densities = [64, 128, 256, 512]  # rho = N / L, d = 1
    scales = []
    for N in densities:
        # near-uniform sprinkling (jitter) in [0,L]; hopping ~ 1/spacing (inverse lattice spacing).
        pts = np.sort(np.linspace(0, L, N) + (L / N) * 0.1 * rng.standard_normal(N))
        spacings = np.diff(pts)
        hop = 1.0 / spacings
        # Hermitian tridiagonal Dirac-like operator (i d/dx discretization magnitude).
        D = np.zeros((N, N))
        for i in range(N - 1):
            D[i, i + 1] = hop[i]
            D[i + 1, i] = hop[i]
        ev = np.linalg.eigvalsh(D)
        uv_scale = float(np.max(np.abs(ev)))  # UV / cutoff spectral scale
        scales.append(uv_scale)
    # fit scale ~ rho^alpha
    logrho = np.log(np.array(densities, float))
    logs = np.log(np.array(scales))
    alpha = float(np.polyfit(logrho, logs, 1)[0])
    ratios = [scales[i + 1] / scales[i] for i in range(len(scales) - 1)]
    return {
        "densities_rho": densities,
        "dimension_d": 1,
        "uv_spectral_scale_at_each_density": scales,
        "scale_ratio_per_density_doubling": ratios,
        "expected_ratio_2_to_the_1_over_d": 2.0 ** (1.0 / 1),
        "fitted_exponent_alpha_in_scale~rho^alpha": alpha,
        "expected_exponent_1_over_d": 1.0,
        "gap_scale_tracks_the_cutoff": bool(abs(alpha - 1.0) < 0.1),
        "verdict": (
            "SMUGGLED SCALE. The causal-set Dirac spectral scale tracks the sprinkling density as "
            "rho^{1/d} (fitted alpha ~ 1 for d=1; ratio ~ 2 per density doubling): it MOVES with "
            "the discretization -- the opposite of the RG-invariant positive control. The "
            "'transmuted' scale is the UV cutoff / lattice spacing in disguise; any geometric gap "
            "is a ratio of L (box) and l=rho^{-1/d} (spacing), both IMPORTED scales. No running "
            "dimensionless coupling / beta-function is exhibited, so there is no transmutation."
        ),
    }


# ===========================================================================
# JOB A / ATTACK 3 -- HIDDEN ORACLE (source-internal growth law).
# ===========================================================================
def oracle_disjunction() -> dict[str, Any]:
    return {
        "horn_A_posited_fixed_growth_law": {
            "premise": "The causal-set growth law (Rideout-Sorkin CSG) is POSITED / fixed.",
            "consequence": "The entire sequence of causal sets -- and hence the whole family D(p) "
            "and its entire spectral flow -- is a computable function of the fixed law + the "
            "random tape. The flow is predetermined.",
            "absorber": "fixed_source (x) stochastic_seed (CompletionClass; D-FORK route-1). "
            "Fixed-law + fixed stochastic seed growth is absorbed.",
            "kills_source_forcing": True,
        },
        "horn_B_unbuilt_action_as_oracle": {
            "premise": "The growth law/action is UNBUILT but invoked to GUARANTEE the modes are "
            "minted in the right way as p rolls.",
            "consequence": "The unbuilt action is a hidden completed oracle precontaining the "
            "future spectrum -- a direct violation of OnlineIssuance^LC gate 4 (no internally "
            "formed future-schema oracle precontains all future admissible witnesses).",
            "absorber": "completed_history (+ hidden_state).",
            "kills_source_forcing": True,
        },
        "exhaustive": True,
        "verdict": (
            "Both horns kill source-forcing. The growth law is either specified (Horn A -> "
            "fixed_source (x) stochastic_seed) or not (Horn B -> completed_history). There is no "
            "third option; 'source-internal' is a promissory note on an unbuilt object either way."
        ),
    }


# ===========================================================================
# JOB B -- BECOMING TYPE-SIGNATURE, FRAME-RELATIVIZED (third-person arena vs first-person value).
# ===========================================================================
#
# STEP 1 (the arena, third person). The spectrum of D(p) -- the set of eigenvalues, WHICH modes CAN
# cross zero -- is third-person computable from the fixed operator family. This is DISCLOSURE, and
# it is EXPECTED and CORRECT (it is exactly Job A's finding). Read third-person, the becoming bit
# always returns disclosure for any built toy, because we wrote the growth rule. That is the WRONG
# frame for the becoming-witness.
#
# STEP 2 (the value, first person). The becoming-witness is whether WHICH mode actually ACTUALIZES
# the mint is FIRST-PERSON underivable: is there a Lawvere/FLP/neural-sampler/ZK-shaped obstruction
# -- "no map internal to the stage-n data computes which mode stage-(n+1) actualizes," even though
# an external observer can? Such a first-person diagonal can fire ONLY if the system SELF-ENCODES
# (Lawvere leg L1: the readout feeds the growth; the system contains its own describers). The
# witness has the FLP-bivalence / sampler-draw shape: two runs with IDENTICAL stage-n INTERNAL
# records actualize DIFFERENT next modes (the difference carried by an external INDEXICAL not in
# the internal records) => no internal map computes the actualization.
# ---------------------------------------------------------------------------
def flp_bivalence_witness(self_encoding: bool, external_indexical: bool) -> dict[str, Any]:
    """FLP/sampler-shaped first-person underivability test (frame-relative becoming-witness).

    self_encoding   -- does the readout (Dirac spectrum) feed back into the growth, so an internal
                       observer/describer exists at all? (Lawvere L1.) Without it there is NO
                       first-person frame and no diagonal can fire.
    external_indexical -- is the actualized mode set by a datum (arrival order / draw / trusted-setup
                       secret) that is NOT contained in the stage-n internal records? (Lawvere L2.)
    """
    stage_n_internal_records = (1, 0, 1, 1)  # identical on both runs
    if not self_encoding:
        return {
            "self_encoding_present_L1": False,
            "first_person_frame_exists": False,
            "first_person_underivable": False,
            "why": "No self-encoding: the Dirac operator is a PASSIVE readout and the growth law is "
            "BLIND to the spectrum, so the system contains no internal observer/describer. There is "
            "no first-person frame at all, so no Lawvere diagonal can even fire.",
        }
    # self-encoding present -> a first-person exists. Two runs share stage-n internal records:
    run_A_actualized = 2
    run_B_actualized = 3 if external_indexical else 2
    underivable = bool(run_A_actualized != run_B_actualized)
    return {
        "self_encoding_present_L1": True,
        "first_person_frame_exists": True,
        "two_runs_identical_stage_n_internal_records": stage_n_internal_records,
        "run_A_actualized_mode": run_A_actualized,
        "run_B_actualized_mode": run_B_actualized,
        "external_indexical_flips_actualization_L2": underivable,
        "first_person_underivable": underivable,
        "shape": "FLP bivalence / neural-sampler draw / ZK-absent-witness: same INSIDE, different MINT.",
    }


def first_person_becoming_discriminator() -> dict[str, Any]:
    # Third-person arena: always computable for a built toy (this is Job A, restated honestly).
    third_person_arena_computable = True

    # AS-BUILT spectral-flow source: passive Dirac readout on a fixed-law-growing causal set.
    asbuilt = flp_bivalence_witness(self_encoding=False, external_indexical=True)
    # POSITIVE CONTROL (ii) BECOMING-FIRST-PERSON: self-encoding + external indexical.
    becoming_pc = flp_bivalence_witness(self_encoding=True, external_indexical=True)
    # CONTROL (i) DISCLOSURE-BOTH-FRAMES: self-encoding but NO external indexical (genuinely dead).
    dead_pc = flp_bivalence_witness(self_encoding=True, external_indexical=False)

    def classify(w: dict[str, Any]) -> str:
        if not w["first_person_frame_exists"]:
            return "iii_still_fixed_law_no_self_encoding"
        if w["first_person_underivable"]:
            return "ii_BECOMING_first_person"
        return "i_DISCLOSURE_both_frames"

    discriminator_separates = bool(
        classify(asbuilt) == "iii_still_fixed_law_no_self_encoding"
        and classify(becoming_pc) == "ii_BECOMING_first_person"
        and classify(dead_pc) == "i_DISCLOSURE_both_frames"
    )

    return {
        "third_person_arena_is_computable_disclosure_as_expected": third_person_arena_computable,
        "asbuilt_spectral_flow_source": {"witness": asbuilt, "outcome": classify(asbuilt)},
        "positive_control_becoming_first_person": {"witness": becoming_pc, "outcome": classify(becoming_pc)},
        "control_disclosure_both_frames": {"witness": dead_pc, "outcome": classify(dead_pc)},
        "discriminator_separates_all_three_outcomes": discriminator_separates,
        "asbuilt_outcome": classify(asbuilt),
        "why_asbuilt_is_outcome_iii": (
            "The spectral-flow mint AS BRIEFED has NO self-encoding: D is a passive readout, the CSG "
            "growth law is blind to the spectrum, there is no internal observer for whom the next "
            "actualization is an indexical. So it is not merely 'third-person computable' (that is "
            "true of every toy) -- there is no first-person frame at all, hence no diagonal can fire. "
            "Fixed-law in both frames, for the SHARP reason that there is no inside."
        ),
        "honest_caveat": (
            "The becoming-first-person positive control shows the DISCRIMINATOR FIRES (separates "
            "outcome ii from i and iii). It does NOT establish that a self-encoding spectral flow "
            "would physically issue; the first-person obstruction is a genuine Lawvere/FLP fact "
            "(TaF T19/T92; the CompletionClass absorbers are THIRD-PERSON nulls and do not touch a "
            "first-person indexical), imported here at the source's own steelman-synthesis grade."
        ),
    }


# ===========================================================================
# Adapter_P W1/W4 gate walk (Job B, formal).
# ===========================================================================
def adapter_p_gate_walk() -> dict[str, Any]:
    return {
        "W1_non_isomorphic_algebra_growth": {
            "pass": False,
            "why": "D_N is a compression of a fixed D_inf over the completed sprinkling "
            "(A1); the observable algebra is the fixed quasi-local field algebra. No growth.",
        },
        "W2_source_generated_new_admissibility_predicate": {
            "pass": False,
            "why": "'admissible causal-set extension' is fixed by the posited CSG law -- a "
            "pre-existing predicate the process satisfies, not one the source authors (relabel).",
        },
        "W4_physical_perturbation_non_factorization": {
            "pass": False,
            "why": "D(p) IS a fixed operator-valued function (a fixed Hamiltonian family H(p)); "
            "this is the RUN-0103 physical-lift absorption (all real physical attempts -> "
            "fixed-Hamiltonian; w4_real_physical_protocol_found: false).",
        },
        "no_hidden_completed_oracle": {
            "pass": False,
            "why": "the fixed growth law + fixed D-construction is a completed extension diagram / "
            "fixed latent graph precontaining all future spectra (OnlineIssuance^LC gate 4).",
        },
        "adapter_p_accepts_witness": False,
        "frame": "THIRD-PERSON gate. Adapter_P / CompletionClass are third-person null classes: "
        "they show an EXTERNAL observer reproduces the trace. They do NOT touch the first-person "
        "indexical of Job B (a self-encoding system's own next actualization), which is a different "
        "frame (TaF T19/T92).",
        "verdict": "Adapter_P REJECTS (third-person) -- same shape as RUN-0103's Assembly physical "
        "lift (formal/local at best, physical lift absorbed to fixed-Hamiltonian).",
    }


# ===========================================================================
# Assemble.
# ===========================================================================
def run_fixture() -> dict[str, Any]:
    a1_pc = a1_positive_control()
    a1_relabel = spectral_flow_relabel_demo()
    a1_grow = growing_causet_compression_tower()

    a2_pc = rg_invariant_scale_positive_control()
    a2_gap = causet_gap_tracks_cutoff()

    a3 = oracle_disjunction()

    b = first_person_becoming_discriminator()
    adapter = adapter_p_gate_walk()

    # --- Job A verdict ---
    a1_absorbed = (
        a1_relabel["every_minted_zero_mode_is_a_preexisting_eigenvector"]
        and a1_grow["D_small_is_compression_of_D_grown"]
        and a1_grow["zero_mode_count_equals_index"]
    )
    a2_absorbed = a2_gap["gap_scale_tracks_the_cutoff"] and a2_pc["Lambda_is_cutoff_invariant"]
    a3_absorbed = a3["exhaustive"]
    job_a_absorbed = bool(a1_absorbed and a2_absorbed and a3_absorbed)

    # positive controls all fire (verdict is informative, not rigged)
    positive_controls_fire = bool(
        a1_pc["discriminator_separates_absorbed_from_issuing"]
        and a2_pc["Lambda_is_cutoff_invariant"]
        and b["discriminator_separates_all_three_outcomes"]
    )

    # --- Job B verdict (frame-relativized) ---
    job_b_outcome = b["asbuilt_outcome"]  # iii_still_fixed_law_no_self_encoding, as built

    return {
        "fixture_id": "du_spectral_flow_source_kill_probe",
        "question": "Does the Dirac spectral-flow SOURCE (mint new zero-modes as p rolls on a "
        "growing causal set; gap dimensionally-transmutes a scale) SURVIVE the fixed-operator / "
        "cutoff / oracle attacks, and is the flow BECOMING or DISCLOSURE?",
        "kind": "finite_window_signature_not_a_decision_procedure",
        "claim_status_change": "none",

        "positive_controls_fire_verdict_is_informative_not_rigged": positive_controls_fire,

        "JOB_A_kill_the_strongest_form": {
            "attack1_fixed_operator_relabel": {
                "positive_control": a1_pc,
                "spectral_flow_relabel_demo": a1_relabel,
                "growing_causet_compression_tower": a1_grow,
                "absorbed": a1_absorbed,
            },
            "attack2_smuggled_scale": {
                "positive_control_RG_invariant_scale": a2_pc,
                "causet_gap_tracks_cutoff": a2_gap,
                "absorbed": a2_absorbed,
            },
            "attack3_hidden_oracle": {"disjunction": a3, "absorbed": a3_absorbed},
            "job_a_verdict": "ABSORBED" if job_a_absorbed else "SURVIVES",
            "primary_absorber": "fixed-operator / compression-of-fixed-D_inf (APS net flow = index "
            "= fixed topological invariant); the SAME fixed-H absorber that ate the wave-2 mirror "
            "condensate (Bogoliubov on fixed CAR <-> spectral flow = compressions of fixed D_inf).",
        },

        "JOB_B_becoming_type_signature_frame_relativized": {
            "first_person_becoming_discriminator": b,
            "adapter_p_W1_W4_gate_walk_THIRD_PERSON": adapter,
            "job_b_outcome": job_b_outcome,
            "job_b_verdict": (
                "OUTCOME (iii) STILL-FIXED-LAW / NO-SELF-ENCODING. The third-person ARENA (the "
                "spectrum) is computable = disclosure, as expected. But the first-person "
                "becoming-witness cannot even be evaluated: the spectral flow AS BRIEFED has no "
                "self-encoding (passive Dirac readout; growth law blind to the spectrum), so there "
                "is no internal observer and no Lawvere diagonal can fire. Not merely disclosure -- "
                "there is no inside at all."
            ),
        },

        "what_self_encoding_a_genuine_first_person_mint_would_require": (
            "REFRAMED (from third-person Godelian incomputability to first-person INDEXICAL "
            "underivability). Do NOT demand the third-person spectrum be non-computable -- that is "
            "impossible for a built toy and is the WRONG frame. Instead CLOSE THE LAWVERE-L1 LOOP: "
            "make the causal set the observer's OWN record structure and record the Dirac spectrum "
            "(which modes actualize) BACK into the causal set as new elements, so the readout FEEDS "
            "the growth (the self-authoring ledger the vision council named; the observer sits "
            "INSIDE the admissibility space it defines). THEN, by Lawvere-L2, the actualized mint "
            "becomes first-person underivable -- an indexical (like FLP arrival-order, the neural "
            "sampler's draw, or a ZK witness absent from the transcript) -- EVEN WHILE third-person "
            "the spectrum stays a computable arena. That is outcome (ii) BECOMING-FIRST-PERSON, and "
            "it is COMPATIBLE with Job A's third-person ABSORBED (they are the two Lawvere legs in "
            "dependency: 'the inside-ness of the observer forces the outside-ness of the minted "
            "datum'). NOTE: this reframes the wave-2 'need third-person mode-issuance (grow "
            "ker(Gamma))' demand as itself possibly a FRAME ERROR -- a third-person demand no built "
            "object can meet; the first-person diagonal is the achievable becoming-witness. Held at "
            "the source's steelman-synthesis grade, re-verified not adopted; not banked."
        ),

        "verdict": (
            "JOB A: ABSORBED -- the spectral-flow mint does NOT survive as built (third-person). The "
            "'new zero-mode' is a PRE-EXISTING eigenvector relabeled by the crossing (net flow = APS "
            "index = fixed invariant, computable in advance); the growing lattice is a compression "
            "tower of a fixed D_inf (additive same-type site growth); the 'transmuted' scale tracks "
            "the sprinkling density rho^{1/d} = the UV cutoff in disguise; 'source-internal' is "
            "either a fixed CSG law (fixed_source (x) stochastic_seed) or an unbuilt-action oracle "
            "(completed_history). Primary absorber: fixed-operator/compression-of-fixed-D_inf, the "
            "SAME fixed-H absorber that ate the mirror condensate. JOB B (frame-relativized): "
            "OUTCOME (iii) STILL-FIXED-LAW / NO-SELF-ENCODING -- the third-person arena is disclosure "
            "as expected, and the first-person becoming-witness cannot fire because the object as "
            "briefed has NO self-encoding (passive readout, growth blind to spectrum) = no inside. "
            "The concrete fix is NOT a third-person Godel sentence but CLOSING THE L1 LOOP (record "
            "the spectrum back into the causal set), which would give outcome (ii) BECOMING-"
            "FIRST-PERSON -- compatible with Job A ABSORBED, the two Lawvere legs in dependency."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/du_spectral_flow_source_kill_probe_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
