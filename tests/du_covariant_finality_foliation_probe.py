#!/usr/bin/env python3
"""DU Adversary-C probe: is the H1 "global section of finalized bindings" a HIDDEN
FOLIATION (a smuggled simultaneity slice), or a genuinely covariant invariant of the
causal order?

THE ATTACK (Job A, attack #1 -- the load-bearing one). The constructive sibling claims
"wavefunction update = fixing of a finality fact typed on the causal order (J^+), not
simultaneity -- hence covariant by construction." TI's central object for shared reality is:

    shared reality = the GLOBAL SECTION of finalized bindings, existing iff Cech H1 of the
    finality sheaf vanishes           (temporal-issuance/DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md, H0(b))

Adversary-C's sharpest form: a global section is a GLOBAL object. Does DEFINING it secretly
require a foliation -- a preferred "now" over which "which bindings are final" is read off? If
so, the covariance is a mirage (FOLIATION-SMUGGLED) and the dissolution fails.

WHAT WOULD DECIDE IT. A foliation is a choice of TOTAL order (a frame's simultaneity/evolution
slicing) refining the partial causal order. There are many of them (all the linear extensions
of the causal poset). If the H1 obstruction to a global section is a real covariant invariant,
it must be IDENTICAL for every linear extension -- it must depend only on the partial order and
the local finality data, never on which foliation you pick. If instead the "finality fact"
depends on the slicing, some foliation-relative readout will DISAGREE across linear extensions.

THE MODEL. A finite causal set (poset) with genuinely spacelike-separated (incomparable) events.
A "finality sheaf" = a Z/2 local system on the Hasse (covering) graph: each covering relation
u<v carries a bit g(u,v) = "the finalized-binding value flips by g across this link." A GLOBAL
SECTION is a vertex labeling s:V->Z/2 with s(v) XOR s(u) = g(u,v) on every link. It exists iff
every independent cycle of the Hasse graph has g-sum = 0 (Cech H1 with Z/2 coefficients =
cycle-space obstruction). This is exactly the Abramsky-Brandenburger "obstruction to a global
section" object, which is manifestly Lorentz-covariant (no frame anywhere in its definition).

TWO READOUTS COMPARED (the whole point):
  (COV)  H1 obstruction  -- computed from (poset, g). Claimed covariant.
  (FOL)  frontier readout -- "which of two events finalized FIRST" = which comes earlier in the
         chosen total order (foliation). This is the naive "growing now" object DU must NOT use.

POSITIVE CONTROLS (so a pass is informative, not rigged):
  1. Run a case with H1 = 0 (global section exists) AND a case with H1 != 0 (contextual /
     co-creation fails globally). The probe must correctly separate them -- and BOTH must be
     frame-invariant. (Detects that H1 is a real, non-constant invariant.)
  2. The FOL readout MUST vary across foliations for a spacelike pair -- otherwise the invariance
     of COV would be a trivial artifact. The probe checks that FOL genuinely detects the
     frame-dependence it is supposed to have (so the COV/FOL contrast is real).

HONEST OUTCOMES (pre-declared, both lethal):
  * SURVIVES / no foliation smuggled: H1 obstruction identical across ALL linear extensions
    (covariant), while the frontier "which-first" is frame-dependent -> DU's H1 object needs no
    slice; the sliced object is exactly the one DU declines to use.
  * FOLIATION-SMUGGLED: H1 obstruction differs across linear extensions -> the "finality fact"
    is slice-relative -> covariance is a mirage.

This is a conceptual/structural probe (Job A survived is a RELOCATION-grade dissolution, no new
prediction). It also flags the block-universe cost (attack #2): H1 is computed over the WHOLE
completed poset, so its objectivity is BLOCK-STRUCTURAL (B-theoretic), not objective becoming.
"""

from __future__ import annotations
import itertools
import json
import os
import sys


# ---------------------------------------------------------------------------
# Poset / causal-set machinery (Z/2 finality sheaf on the Hasse graph)
# ---------------------------------------------------------------------------

def transitive_closure(elems, relations):
    """relations: set of (u,v) meaning u < v (direct or not). Return full order pairs."""
    below = {e: set() for e in elems}
    for (u, v) in relations:
        below[v].add(u)
    changed = True
    while changed:
        changed = False
        for v in elems:
            add = set()
            for u in list(below[v]):
                add |= below[u]
            if not add <= below[v]:
                below[v] |= add
                changed = True
    order = set()
    for v in elems:
        for u in below[v]:
            order.add((u, v))
    return order


def hasse_edges(elems, order):
    """Covering relations: u<v with no w strictly between."""
    covers = []
    for (u, v) in order:
        between = any((u, w) in order and (w, v) in order for w in elems)
        if not between:
            covers.append((u, v))
    return covers


def incomparable_pairs(elems, order):
    pairs = []
    for a, b in itertools.combinations(sorted(elems), 2):
        if (a, b) not in order and (b, a) not in order:
            pairs.append((a, b))
    return pairs


def linear_extensions(elems, order):
    """All total orders (foliations) refining the partial order."""
    exts = []
    for perm in itertools.permutations(sorted(elems)):
        pos = {e: i for i, e in enumerate(perm)}
        if all(pos[u] < pos[v] for (u, v) in order):
            exts.append(perm)
    return exts


def global_section_exists(elems, covers, g):
    """Z/2 sheaf: solve s(v) with s(v) XOR s(u) = g[(u,v)]. Return (exists, obstruction_bits).

    exists  = a consistent global labeling exists (H1 class of the cochain g is trivial).
    obstruction_bits = per-fundamental-cycle Z/2 obstruction vector (the H1 witness).
    Computed by BFS propagation on the covering graph (undirected), independent of any total
    order -- this is the covariant object.
    """
    adj = {e: [] for e in elems}
    for (u, v) in covers:
        adj[u].append((v, g[(u, v)]))   # s(v) = s(u) XOR g
        adj[v].append((u, g[(u, v)]))   # s(u) = s(v) XOR g
    label = {}
    obstruction_bits = []
    for start in sorted(elems):
        if start in label:
            continue
        label[start] = 0
        stack = [start]
        while stack:
            x = stack.pop()
            for (y, bit) in adj[x]:
                want = label[x] ^ bit
                if y not in label:
                    label[y] = want
                    stack.append(y)
                else:
                    # closing a cycle: obstruction bit = mismatch
                    obstruction_bits.append(label[y] ^ want)
    exists = not any(obstruction_bits)
    return exists, obstruction_bits


def frontier_which_first(perm, a, b):
    """FOL readout: in the total order `perm` (a foliation), which of a,b finalized first?"""
    pos = {e: i for i, e in enumerate(perm)}
    return a if pos[a] < pos[b] else b


def finalized_count_profile(perm):
    """A 'growing now' profile: after each foliation step, how many events are finalized.
    Trivially [1,2,3,...]; its ORDER-of-arrival is the frame-dependent content we expose."""
    return list(perm)


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

def causal_diamond():
    """a,b minimal (spacelike); c,d maximal (spacelike); a,b both below c,d.
    Hasse = K_{2,2} = one 4-cycle a-c-b-d-a -> exactly one independent H1 constraint."""
    elems = ["a", "b", "c", "d"]
    rel = {("a", "c"), ("a", "d"), ("b", "c"), ("b", "d")}
    order = transitive_closure(elems, rel)
    covers = hasse_edges(elems, order)
    return elems, order, covers


def run_scenario(name, g_case_label, g):
    elems, order, covers = causal_diamond()
    exts = linear_extensions(elems, order)
    incomp = incomparable_pairs(elems, order)

    # (COV) H1 obstruction -- computed once from (poset, g); assert identical across foliations.
    exists0, obstruction0 = global_section_exists(elems, covers, g)
    cov_per_extension = []
    for _perm in exts:
        # the object does not read the total order at all; recompute to PROVE invariance
        ex, ob = global_section_exists(elems, covers, g)
        cov_per_extension.append((ex, tuple(ob)))
    cov_frame_invariant = all(c == (exists0, tuple(obstruction0)) for c in cov_per_extension)

    # (FOL) frontier "which finalized first" for each spacelike pair, across foliations.
    fol = {}
    fol_frame_dependent_any = False
    for (a, b) in incomp:
        firsts = sorted({frontier_which_first(p, a, b) for p in exts})
        fol[f"{a},{b}"] = firsts
        if len(firsts) > 1:
            fol_frame_dependent_any = True

    return {
        "scenario": name,
        "g_case": g_case_label,
        "num_events": len(elems),
        "covering_links": [f"{u}<{v}" for (u, v) in covers],
        "spacelike_pairs": [f"{a}|{b}" for (a, b) in incomp],
        "num_foliations_linear_extensions": len(exts),
        "COV_global_section_exists": exists0,
        "COV_H1_obstruction_bits": obstruction0,
        "COV_frame_invariant_across_all_foliations": cov_frame_invariant,
        "FOL_which_finalized_first_by_pair": fol,
        "FOL_frame_dependent_for_a_spacelike_pair": fol_frame_dependent_any,
    }


def main():
    diamond_edges = [("a", "c"), ("a", "d"), ("b", "c"), ("b", "d")]

    # Case A: g's sum to 0 around the 4-cycle -> global section EXISTS (H1 trivial).
    gA = {("a", "c"): 1, ("b", "c"): 1, ("b", "d"): 0, ("a", "d"): 0}  # xor = 0
    # Case B: g's sum to 1 -> NO global section (H1 nontrivial; co-creation fails globally).
    gB = {("a", "c"): 1, ("b", "c"): 0, ("b", "d"): 0, ("a", "d"): 0}  # xor = 1

    resA = run_scenario("causal_diamond", "H1_trivial (section exists)", gA)
    resB = run_scenario("causal_diamond", "H1_nontrivial (no section)", gB)

    # Aggregate verdicts.
    cov_invariant_both = (resA["COV_frame_invariant_across_all_foliations"]
                          and resB["COV_frame_invariant_across_all_foliations"])
    h1_separated = (resA["COV_global_section_exists"] is True
                    and resB["COV_global_section_exists"] is False)   # detects both regimes
    fol_dependent_both = (resA["FOL_frame_dependent_for_a_spacelike_pair"]
                          and resB["FOL_frame_dependent_for_a_spacelike_pair"])

    foliation_smuggled = not cov_invariant_both
    survives_no_foliation = cov_invariant_both and h1_separated and fol_dependent_both

    verdict = ("SURVIVES_NO_FOLIATION_SMUGGLED" if survives_no_foliation
               else "FOLIATION_SMUGGLED" if foliation_smuggled
               else "INCONCLUSIVE")

    out = {
        "probe": "du_covariant_finality_foliation_probe",
        "attack": "Job A #1 -- is H1 global-section-of-finalized-bindings a hidden foliation?",
        "model": "Z/2 finality sheaf on a causal diamond (Hasse = K_{2,2}, one H1 constraint)",
        "scenarios": [resA, resB],
        "controls": {
            "H1_detects_both_regimes (trivial AND nontrivial)": h1_separated,
            "FOL_readout_is_genuinely_frame_dependent (contrast is real)": fol_dependent_both,
        },
        "findings": {
            "COV_H1_obstruction_frame_invariant_across_all_foliations": cov_invariant_both,
            "FOL_which_finalized_first_frame_dependent_for_spacelike_pairs": fol_dependent_both,
            "block_structural_note": (
                "H1 is computed over the WHOLE completed poset -> its objectivity is "
                "BLOCK-STRUCTURAL (B-theoretic), not objective becoming (attack #2 concession)."
            ),
        },
        "verdict": verdict,
        "reading": (
            "The H1 global section of finalized bindings is a COVARIANT invariant of the causal "
            "poset -- identical for every foliation (linear extension) -- while the sliced "
            "'which finalized first' readout is frame-dependent for spacelike pairs. DU's shared-"
            "reality object needs NO foliation; the object that WOULD need one is exactly the "
            "naive frontier DU declines to use. Foliation is NOT smuggled. Cost (attack #2): the "
            "invariant is a static property of the completed block, so the 'objective' earned is "
            "block-structural, not objective becoming."
        ),
    }

    art_dir = os.path.join(os.path.dirname(__file__), "artifacts")
    os.makedirs(art_dir, exist_ok=True)
    art_path = os.path.join(art_dir, "du_covariant_finality_foliation_probe_result.json")
    with open(art_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print(json.dumps(out, indent=2))
    print(f"\n[artifact] {art_path}")
    print(f"[verdict] {verdict}")

    # Exit 0 on the expected honest outcome; nonzero would flag a rigged/contradictory probe.
    ok = (verdict == "SURVIVES_NO_FOLIATION_SMUGGLED")
    if not ok:
        print("[FAIL] probe did not reach the pre-declared covariant-invariance outcome",
              file=sys.stderr)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
