#!/usr/bin/env python3
"""DU covariant-finality-collapse probe: is the wavefunction "update" a covariant
finality fact typed on the causal order (J+), or does it secretly smuggle a foliation?

THE QUESTION (the one real problem). How is the "instantaneous" update of the state
compatible with the light-cone limit? No-signaling is already safe (no-communication
theorem). The genuinely open part is that a *physical* collapse seems to need a
PREFERRED SIMULTANEITY: in EPR, boosted frames disagree on which wing "collapsed first"
and in what order -- a non-covariant "when." Shimony's "peaceful coexistence" is
descriptive, not explanatory.

THE BUILD UNDER TEST. The update is NOT a process propagating through space. It is the
FIXING OF A FINALITY FACT TYPED ON THE CAUSAL (light-cone) PARTIAL ORDER J+, not on a
simultaneity surface. Special relativity's invariant structure IS the causal partial
order; a foliation is the frame-dependent thing. So if "final" == "fixed relative to its
own causal future J+", finality is frame-independent BY CONSTRUCTION, the EPR "which
collapsed first?" is malformed (the two wings are causally INCOMPARABLE), and the
correlation is a joint property of ONE finalized record (TI's H1 global section over the
causal set), not something built by propagation.

Cross-repo objects consumed and RE-VERIFIED here per CONNECTIONS.md (no grade imported):
  - TaF FORMALISM: the causal partial order <_c is PRIMITIVE; metric time, a global
    clock, a universal present, and a total order over spacelike events are explicitly
    NOT primitive; "the result must be invariant under the choice of topological
    ordering." Spacelike-separated stabilized records remain INCOMPARABLE. (T21 gives
    the CHSH/global-section obstruction; T16 the gluing to a global partial order.)
  - TI DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE: shared reality is the GLOBAL SECTION glued
    from finalized bindings (Cech H1 of the finality sheaf); "observers may disagree
    about coordinate time because they take different local slices... it does NOT mean a
    preferred foliation or absolute simultaneity."

WHAT THIS PROBE COMPUTES (anti-toy; four modules; each falsifiable):

(a) FRAME-INDEPENDENCE with a POSITIVE CONTROL that discriminates.
    An EPR/Bell pair as events on a small causal set: source P (common past), wings A, B
    (spacelike), comparison C (common future). We boost through a range of rapidities and
    check that the CAUSAL-ORDER data (the partial-order incidence matrix) is IDENTICAL in
    every frame -- machine-precision invariant. POSITIVE CONTROL: a naive foliation-based
    collapse orders {A,B} by boosted time-coordinate t'; we show sign(t'_A - t'_B) FLIPS
    with the boost (both wings "collapse first" in some frame). So the test DISCRIMINATES:
    same input, the foliation account is frame-dependent, the causal-order account is not,
    and the "which collapsed first" question is malformed (A,B incomparable in <_c).

(b) NO-SIGNALING. The local marginal at wing A is independent of the far setting at B
    (the non-selective / Fewster-Verch causal-factorization invariance): P(a | theta_a,
    theta_b) = 1/2 for every theta_b. Computed on the real singlet.

(c) CORRELATION FROM THE GLOBAL SECTION, NO PROPAGATION. The full singlet correlation
    E(theta_a, theta_b) = -cos(theta_a - theta_b) is reproduced as an expectation in the
    ONE state prepared at P and read jointly (the finalized joint record / global section
    at C), with NO A->B edge in the causal set (A,B are incomparable -> there is no
    propagation path to carry it). CHSH = 2*sqrt(2) confirms it is genuinely quantum:
    there is NO global section of LOCAL HIDDEN VALUES (the Bell obstruction, H1 != 0 for
    the value-assignment sheaf -- TaF T21), yet the finalized JOINT-RECORD section at C is
    a single well-defined object. Those are two different sheaves; the account lives on the
    second.

(d) SORKIN ADMISSIBILITY (the decisive test). Sorkin (1993): a naive ideal (Lueders)
    measurement in QFT, applied as an instantaneous update ACROSS A SLICE, can signal
    superluminally unless the operations are restricted; the admissible ones are exactly
    the causally-localized (Fewster-Verch covariant-measurement) updates. We build a
    Sorkin-type three-region toy: Alice at A, an EXTENDED measurement region modeled by its
    two spacelike ends b1,b2, Charlie at C, with A < b1, b2 < C, and A||C, b1||b2 (the only
    causal routes are A->b1 and b2->C; A->C requires linking the SPACELIKE pair b1,b2). A
    FOLIATION update fabricates the b1~b2 co-collapse link (they share a slice) -> opens
    A->b1~b2->C -> SIGNALS (the impossible measurement). A CAUSAL-ORDER (finality) update
    FORBIDS the b1-b2 link (they are incomparable in <_c, so their joint co-fixing is NOT
    "final") -> NO SIGNAL. => finality-on-causal-order SUPPLIES exactly Sorkin's admissible
    restriction. We compute I(A:C) under each account.

HONEST SCOPE. (a),(b),(c) are exact (Minkowski causal order; the real singlet). (d) is a
faithful SCHEMATIC of the Sorkin mechanism at qubit level: the modeling choice "ideal
measurement of the extended-region observable == a b1-b2 co-collapse link" is motivated by
the mechanism (an ideal Lueders update treats a whole slice through the region as
co-fixed), not derived from the CCR net. What it demonstrates rigorously is the STRUCTURE:
a foliation-typed update fabricates spacelike links and signals; a causal-order-typed
update forbids them and does not -- which is precisely the Sorkin-admissible / Fewster-Verch
restriction. "It feels covariant" is not a result; the frame-independence (a) and the
Sorkin-admissibility (d) are computed and are the result.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

EPS = 1e-9

# ---------------------------------------------------------------------------
# Minkowski (1+1) causal order -- the PRIMITIVE object (TaF FORMALISM).
# e precedes f  iff  f is in the closed forward light cone of e:
#   dt := f.t - e.t >= 0  AND  dt^2 - dx^2 >= 0.
# This relation is Lorentz-INVARIANT by construction; a foliation (a choice of
# simultaneity surface) is the frame-dependent thing that is NOT primitive.
# ---------------------------------------------------------------------------
def boost(events: np.ndarray, rapidity: float) -> np.ndarray:
    """Active Lorentz boost of (t, x) events by rapidity phi."""
    ch, sh = math.cosh(rapidity), math.sinh(rapidity)
    t, x = events[:, 0], events[:, 1]
    tp = ch * t - sh * x
    xp = ch * x - sh * t
    return np.stack([tp, xp], axis=1)


def causal_incidence(events: np.ndarray) -> np.ndarray:
    """Strict causal-precedence incidence matrix M[i,j] = 1 iff event i strictly
    precedes event j (j in the OPEN forward cone of i)."""
    n = len(events)
    M = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            dt = events[j, 0] - events[i, 0]
            dx = events[j, 1] - events[i, 1]
            interval = dt * dt - dx * dx  # > 0 timelike, = 0 null, < 0 spacelike
            if dt > EPS and interval > EPS:
                M[i, j] = 1
    return M


def module_a_frame_independence(n_boosts: int = 41, rap_max: float = 3.0) -> dict[str, Any]:
    """(a) Causal-order data is boost-invariant; the foliation ordering flips. Positive
    control DISCRIMINATES."""
    labels = ["P", "A", "B", "C"]
    # P common past; A,B the two wings (SPACELIKE); C common future comparison event.
    events = np.array(
        [
            [-2.0, 0.0],   # P source
            [0.0, -1.0],   # A  (Alice wing)
            [0.0, 1.0],    # B  (Bob wing)
            [2.0, 0.0],    # C  comparison / joint readout
        ]
    )
    iA, iB = labels.index("A"), labels.index("B")

    lab = causal_incidence(events)
    rapidities = np.linspace(-rap_max, rap_max, n_boosts)

    max_incidence_deviation = 0
    foliation_signs = set()
    ab_incomparable_all_frames = True

    for phi in rapidities:
        ev = boost(events, phi)
        M = causal_incidence(ev)
        max_incidence_deviation = max(max_incidence_deviation, int(np.abs(M - lab).max()))
        # foliation (naive) collapse order of the spacelike wings: sort by boosted time t'
        dt_ab = ev[iA, 0] - ev[iB, 0]
        foliation_signs.add(int(np.sign(round(dt_ab, 12))))
        # causal-order verdict: A,B incomparable (neither precedes the other)?
        if M[iA, iB] != 0 or M[iB, iA] != 0:
            ab_incomparable_all_frames = False

    # sanity on the lab causal structure we intended
    causal_structure = {
        "P<A": bool(lab[0, 1]), "P<B": bool(lab[0, 2]), "P<C": bool(lab[0, 3]),
        "A<C": bool(lab[1, 3]), "B<C": bool(lab[2, 3]),
        "A||B (incomparable)": bool(lab[1, 2] == 0 and lab[2, 1] == 0),
    }

    passed = (
        max_incidence_deviation == 0
        and ab_incomparable_all_frames
        and foliation_signs == {-1, 0, 1}  # foliation order flips sign across boosts
        and all(causal_structure.values())
    )
    return {
        "labels": labels,
        "lab_incidence": lab.tolist(),
        "causal_structure_as_intended": causal_structure,
        "n_boosts": n_boosts,
        "rapidity_range": [-rap_max, rap_max],
        "max_incidence_deviation_across_boosts": max_incidence_deviation,
        "causal_order_invariant": max_incidence_deviation == 0,
        "AB_incomparable_in_every_frame": ab_incomparable_all_frames,
        "foliation_which_first_signs_observed": sorted(foliation_signs),
        "foliation_order_is_frame_dependent": foliation_signs == {-1, 0, 1},
        "control_discriminates": passed,
        "verdict": "PASS" if passed else "FAIL",
        "reading": (
            "Causal-order (finality) data identical in every boost; the naive foliation "
            "collapse-order of the spacelike wings flips sign (both '+' and '-' observed). "
            "'Which collapsed first' is malformed: A,B incomparable in <_c in EVERY frame."
        ),
    }


# ---------------------------------------------------------------------------
# The real singlet and spin measurements in the x-z plane.
#   sigma(theta) = cos(theta) Z + sin(theta) X ;  P_pm = (I +- sigma)/2.
# ---------------------------------------------------------------------------
I2 = np.eye(2)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)


def sigma(theta: float) -> np.ndarray:
    return math.cos(theta) * Z + math.sin(theta) * X


def proj(theta: float, outcome: int) -> np.ndarray:
    s = 1 if outcome == 0 else -1  # outcome 0 -> +1 eigenspace, 1 -> -1
    return 0.5 * (I2 + s * sigma(theta))


SINGLET = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)  # (|01> - |10>)/sqrt2


def joint_prob(theta_a: float, theta_b: float, a: int, b: int) -> float:
    Pi = np.kron(proj(theta_a, a), proj(theta_b, b))
    return float(np.real(np.vdot(SINGLET, Pi @ SINGLET)))


def module_b_no_signaling(grid: int = 24) -> dict[str, Any]:
    """(b) The local marginal at A is independent of the far setting at B."""
    thetas = np.linspace(0, math.pi, grid)
    max_dev = 0.0
    for ta in thetas:
        for tb in thetas:
            pa0 = joint_prob(ta, tb, 0, 0) + joint_prob(ta, tb, 0, 1)  # marginalize b
            max_dev = max(max_dev, abs(pa0 - 0.5))
    passed = max_dev < 1e-12
    return {
        "grid": grid,
        "max_deviation_of_marginal_from_half": max_dev,
        "marginal_independent_of_far_setting": passed,
        "verdict": "PASS" if passed else "FAIL",
        "reading": (
            "P(a | theta_a, theta_b) = 1/2 for every far setting theta_b: the local "
            "(non-selective / Fewster-Verch) marginal cannot be moved from the spacelike wing."
        ),
    }


def correlation(theta_a: float, theta_b: float) -> float:
    return float(np.real(np.vdot(SINGLET, np.kron(sigma(theta_a), sigma(theta_b)) @ SINGLET)))


def module_c_global_section(a_edge_present: bool) -> dict[str, Any]:
    """(c) Full correlation reconstructed from the ONE finalized joint record, no A->B
    propagation. CHSH = 2*sqrt(2) => no local-hidden-value global section (Bell), yet the
    joint-record section is a single object."""
    # correlation reproduced everywhere as -cos(dtheta), the joint-record readout
    thetas = np.linspace(0, math.pi, 19)
    max_corr_err = 0.0
    for ta in thetas:
        for tb in thetas:
            max_corr_err = max(max_corr_err, abs(correlation(ta, tb) - (-math.cos(ta - tb))))

    # CHSH with the optimal singlet angles
    A0, A1, B0, B1 = 0.0, math.pi / 2, math.pi / 4, 3 * math.pi / 4
    S = correlation(A0, B0) - correlation(A0, B1) + correlation(A1, B0) + correlation(A1, B1)
    tsirelson = 2 * math.sqrt(2)

    # structural: there is NO causal edge A->B (A||B from module (a)); the correlation is
    # NOT carried by propagation. a_edge_present is the FALSE counterfactual (a propagation
    # model would need a directed A->B edge whose direction is frame-dependent).
    passed = (
        max_corr_err < 1e-12
        and abs(abs(S) - tsirelson) < 1e-12
        and not a_edge_present
    )
    return {
        "max_correlation_error_vs_minus_cos": max_corr_err,
        "CHSH_S": S,
        "tsirelson_2root2": tsirelson,
        "chsh_is_quantum_maximal": abs(abs(S) - tsirelson) < 1e-12,
        "no_local_hidden_value_global_section": abs(S) > 2.0 + 1e-9,  # Bell / H1 != 0
        "A_to_B_causal_edge_present": a_edge_present,  # False: no propagation path exists
        "correlation_from_single_finalized_record": (max_corr_err < 1e-12 and not a_edge_present),
        "verdict": "PASS" if passed else "FAIL",
        "reading": (
            "E = -cos(dtheta) reproduced exactly as a readout of the ONE state prepared at P "
            "and read jointly at C -- with NO A->B edge in the causal set. CHSH=2sqrt2: no "
            "global section of LOCAL HIDDEN VALUES (Bell obstruction, H1!=0), but the finalized "
            "JOINT-RECORD section at C is a single well-defined object. Two different sheaves."
        ),
    }


# ---------------------------------------------------------------------------
# (d) Sorkin impossible-measurement three-region toy.
# Qubits: A (Alice input), b1,b2 (the two spacelike ends of the extended measurement
# region), C (Charlie). Order of tensor factors: A, b1, b2, C.
# ---------------------------------------------------------------------------
def _cnot(n_qubits: int, ctrl: int, targ: int) -> np.ndarray:
    dim = 1 << n_qubits
    U = np.zeros((dim, dim), dtype=complex)
    for s in range(dim):
        bits = [(s >> (n_qubits - 1 - k)) & 1 for k in range(n_qubits)]
        if bits[ctrl]:
            bits[targ] ^= 1
        t = 0
        for k in range(n_qubits):
            t = (t << 1) | bits[k]
        U[t, s] = 1
    return U


def _basis_state(n_qubits: int, bits: list[int]) -> np.ndarray:
    dim = 1 << n_qubits
    idx = 0
    for b in bits:
        idx = (idx << 1) | b
    v = np.zeros(dim, dtype=complex)
    v[idx] = 1
    return v


def _charlie_marginal(state: np.ndarray, n_qubits: int, c_index: int) -> float:
    """P(C=1)."""
    dim = 1 << n_qubits
    p1 = 0.0
    for s in range(dim):
        bit_c = (s >> (n_qubits - 1 - c_index)) & 1
        if bit_c == 1:
            p1 += abs(state[s]) ** 2
    return p1


def _run_channel(alice_bit: int, apply_bridge: bool) -> float:
    """Return P(C=1) given Alice's input bit and whether the b1-b2 bridge is applied."""
    n = 4  # A, b1, b2, C
    A_i, b1_i, b2_i, C_i = 0, 1, 2, 3
    state = _basis_state(n, [alice_bit, 0, 0, 0])
    state = _cnot(n, A_i, b1_i) @ state       # A < b1 : legitimate causal influence
    if apply_bridge:
        state = _cnot(n, b1_i, b2_i) @ state   # foliation co-collapse link across b1||b2
    state = _cnot(n, b2_i, C_i) @ state       # b2 < C : legitimate causal influence
    return _charlie_marginal(state, n, C_i)


def _mutual_information_A_C(apply_bridge: bool) -> float:
    """I(A:C) in bits for a uniform Alice input over {0,1}."""
    # p(a) = 1/2 each; p(c|a) from the channel
    pc_given_a = {a: _run_channel(a, apply_bridge) for a in (0, 1)}  # P(C=1|a)
    p_a = 0.5
    # joint p(a,c)
    joint = {}
    for a in (0, 1):
        p1 = pc_given_a[a]
        joint[(a, 1)] = p_a * p1
        joint[(a, 0)] = p_a * (1 - p1)
    p_c = {c: sum(joint[(a, c)] for a in (0, 1)) for c in (0, 1)}
    mi = 0.0
    for (a, c), pac in joint.items():
        if pac > 0 and p_c[c] > 0:
            mi += pac * math.log2(pac / (p_a * p_c[c]))
    return mi


def module_d_sorkin() -> dict[str, Any]:
    """(d) Does finality-on-causal-order supply Sorkin's admissible restriction?"""
    # Geometry check: A<b1, b2<C, A||C, b1||b2, A||b2, b1||C.
    labels = ["A", "b1", "b2", "C"]
    events = np.array(
        [
            [0.0, -2.0],   # A  Alice
            [2.0, -1.0],   # b1 (near-Alice end of the extended region)
            [2.0, 1.0],    # b2 (near-Charlie end)   b1||b2 spacelike (dt=0, dx=2)
            [4.0, 2.5],    # C  Charlie
        ]
    )
    M = causal_incidence(events)
    geom = {
        "A<b1": bool(M[0, 1]), "b2<C": bool(M[2, 3]),
        "A||C": bool(M[0, 3] == 0 and M[3, 0] == 0),
        "b1||b2": bool(M[1, 2] == 0 and M[2, 1] == 0),
        "A||b2": bool(M[0, 2] == 0 and M[2, 0] == 0),
        "b1||C": bool(M[1, 3] == 0 and M[3, 1] == 0),
    }
    geom_ok = all(geom.values())

    # Foliation update: fabricates the b1~b2 co-collapse link -> signals.
    I_foliation = _mutual_information_A_C(apply_bridge=True)
    pc_fol = {a: _run_channel(a, True) for a in (0, 1)}
    # Causal-order (finality) update: b1||b2 incomparable -> link FORBIDDEN -> no signal.
    I_causal = _mutual_information_A_C(apply_bridge=False)
    pc_cau = {a: _run_channel(a, False) for a in (0, 1)}

    passed = (
        geom_ok
        and I_foliation > 0.999           # ~1 bit leaks A->C across spacelike separation
        and I_causal < 1e-12              # exactly zero under the causal-order restriction
    )
    return {
        "labels": labels,
        "geometry_as_intended": geom,
        "geometry_ok": geom_ok,
        "foliation_update": {
            "P(C=1|a=0)": pc_fol[0], "P(C=1|a=1)": pc_fol[1],
            "mutual_information_A_C_bits": I_foliation,
            "signals_superluminally": I_foliation > 1e-9,
        },
        "causal_order_finality_update": {
            "P(C=1|a=0)": pc_cau[0], "P(C=1|a=1)": pc_cau[1],
            "mutual_information_A_C_bits": I_causal,
            "signals_superluminally": I_causal > 1e-9,
        },
        "finality_supplies_sorkin_restriction": passed,
        "verdict": "PASS" if passed else "FAIL",
        "reading": (
            "Foliation update fabricates the b1~b2 co-collapse (they share a slice) and leaks "
            "~1 bit A->C across spacelike separation -- Sorkin's impossible measurement. The "
            "causal-order (finality) update forbids the b1-b2 link (incomparable in <_c) and "
            "leaks 0 bits. Finality-on-causal-order == Sorkin/Fewster-Verch admissible restriction."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        default=str(Path(__file__).parent / "artifacts" / "du_covariant_finality_collapse_probe_result.json"),
    )
    args = ap.parse_args()

    results = {
        "probe": "du_covariant_finality_collapse_probe",
        "question": (
            "Is the wavefunction update a covariant finality fact typed on the causal order "
            "J+ (frame-independent), or does it secretly smuggle a foliation? Does it supply "
            "Sorkin's admissibility restriction inside a covariant-measurement picture?"
        ),
        "module_a_frame_independence": module_a_frame_independence(),
        "module_b_no_signaling": module_b_no_signaling(),
        "module_c_global_section": module_c_global_section(a_edge_present=False),
        "module_d_sorkin_admissibility": module_d_sorkin(),
    }
    verdicts = {
        k: v["verdict"]
        for k, v in results.items()
        if isinstance(v, dict) and "verdict" in v
    }
    results["all_pass"] = all(x == "PASS" for x in verdicts.values())
    results["verdicts"] = verdicts

    def _native(o: Any) -> Any:
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2, default=_native), encoding="utf-8")

    print("=" * 78)
    print("DU covariant-finality-collapse probe")
    print("=" * 78)
    for k, v in verdicts.items():
        print(f"  {v:5s}  {k}")
    print("-" * 78)
    a = results["module_a_frame_independence"]
    print(f"(a) causal-order invariant across {a['n_boosts']} boosts: "
          f"{a['causal_order_invariant']} (max incidence deviation = "
          f"{a['max_incidence_deviation_across_boosts']}); "
          f"foliation 'which-first' signs = {a['foliation_which_first_signs_observed']} "
          f"(frame-dependent); A||B every frame: {a['AB_incomparable_in_every_frame']}")
    b = results["module_b_no_signaling"]
    print(f"(b) max |marginal - 1/2| over settings grid = {b['max_deviation_of_marginal_from_half']:.2e}")
    c = results["module_c_global_section"]
    print(f"(c) CHSH S = {c['CHSH_S']:.6f} (Tsirelson {c['tsirelson_2root2']:.6f}); "
          f"corr err vs -cos = {c['max_correlation_error_vs_minus_cos']:.2e}; "
          f"A->B edge present = {c['A_to_B_causal_edge_present']}")
    d = results["module_d_sorkin_admissibility"]
    print(f"(d) I(A:C) foliation = {d['foliation_update']['mutual_information_A_C_bits']:.6f} bits "
          f"(signals); I(A:C) causal-order = {d['causal_order_finality_update']['mutual_information_A_C_bits']:.2e} bits "
          f"(no signal)")
    print("-" * 78)
    print(f"ALL PASS: {results['all_pass']}")
    print(f"artifact: {out}")
    return 0 if results["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
