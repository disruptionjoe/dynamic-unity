#!/usr/bin/env python3
"""D2 QD/SBS audit-gap witness: exact plateau-with-failed-audit states.

Executes discriminator D2 of the Q-0063 decoherence-null confrontation
campaign (frozen plan:
`explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md`,
section 3, D2; pass/fail table frozen there before this computation).

The question: does the audit layer (physically audited access + fragment
independence + perfect distinguishability -- the conditions Spectrum
Broadcast Structure / strong quantum Darwinism add over the raw quantum
Darwinism mutual-information plateau) have empirical content over raw
redundancy, or is it bookkeeping on the same physical process?

Declared model class (frozen before computation): central-spin pure
dephasing -- one system qubit coupled to N environment qubits by exact
controlled rotations (the finite-time snapshot of H_int = |1><1|_S (x)
sum_k g_k sigma_y^(k)); plus the same class with environment fragments
carrying system-independent pre-existing classical correlations.

Witness form (frozen): exact rational density matrices; every verdict
inequality certified in exact `fractions.Fraction` arithmetic.  For binary
spectra {(1+x)/2, (1-x)/2} entropy comparisons use the exact lemma
h((1+x)/2) < h((1+y)/2) iff |x| > |y| (binary entropy is symmetric and
strictly decreasing in |p - 1/2|), so no floating-point value is ever
load-bearing.  Floats appear in the artifact as descriptive detail only.

Witness W1 (discord/distinguishability rung).  The finite-coupling-time
branching state |Psi> = (|0>|phi_0>^N + |1>|phi_1>^N)/sqrt(2) with exact
rational single-fragment overlap a = <phi_0|phi_1> = 3/5, produced from a
product state by exact controlled rotations.  For N = 2 every proper
fragment satisfies the quantum Darwinism condition I(S:F) = H(S) exactly
(the raw plateau, redundancy 2), while every audited condition fails by a
finite exact margin: conditional fragment states are not perfectly
distinguishable (overlap 3/5), rho_{SF} is entangled (exact NPT
certificate), hence the S:F discord is nonzero and the fragment-accessible
pointer information is Holevo-bounded strictly below the plateau height.
For N = 4 the same holds exactly at the half-environment fragments.

Witness W2 (fragment-independence rung).  Perfect pointer records plus
system-independent correlated environment junk: the plateau is exact,
distinguishability is perfect, all discords vanish, yet the SBS product
form fails exactly at every scale (conditional fragment-fragment mutual
information of one full bit, uniform in fragment number).

Controls (mandatory; a witness a genuine falsifier cannot fail is not a
witness): the ideal SBS state (a = 0) passes every audit; an asymmetric
branching state breaks the exact plateau; independent junk passes the
independence audit.

Passing establishes only the scoped exact finite results named in the
checks.  It does not establish new physics, a mechanism, a consensus
ontology, record fundamentality, a prediction, a grade movement, or any
external action; the audit conditions witnessed here are exactly the
known SBS/strong-quantum-Darwinism conditions of the published
literature (Horodecki-Korbicz-Horodecki PRA 91, 032122 (2015);
Le-Olaya-Castro PRA 98, 032103 (2018) and PRL 122, 010403 (2019);
Korbicz, Quantum 5, 571 (2021)).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from fractions import Fraction
from itertools import product as iproduct
from pathlib import Path
from typing import Any

ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_qd_sbs_audit_gap_witness_result.json"
)

Vec = list[Fraction]
Mat = list[list[Fraction]]


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def frac_record(value: Fraction) -> dict[str, Any]:
    return {"exact": frac_text(value), "decimal": float(value)}


@dataclass
class CheckBook:
    checks: list[dict[str, Any]]

    def add(self, name: str, passed: bool, detail: Any = None) -> None:
        self.checks.append(
            {"name": name, "passed": bool(passed), "detail": detail}
        )

    @property
    def passed(self) -> int:
        return sum(check["passed"] for check in self.checks)


# ---------------------------------------------------------------------------
# Exact linear algebra over Fractions
# ---------------------------------------------------------------------------


def kron_vec(left: Vec, right: Vec) -> Vec:
    return [x * y for x in left for y in right]


def outer(left: Vec, right: Vec) -> Mat:
    return [[x * y for y in right] for x in left]


def mat_add(*mats: Mat) -> Mat:
    dim = len(mats[0])
    return [
        [sum((m[i][j] for m in mats), Fraction(0)) for j in range(dim)]
        for i in range(dim)
    ]


def mat_scale(scale: Fraction, mat: Mat) -> Mat:
    return [[scale * entry for entry in row] for row in mat]


def mat_vec(mat: Mat, vec: Vec) -> Vec:
    return [
        sum((row[j] * vec[j] for j in range(len(vec))), Fraction(0))
        for row in mat
    ]


def vec_dot(left: Vec, right: Vec) -> Fraction:
    return sum((x * y for x, y in zip(left, right, strict=True)), Fraction(0))


def vec_sub(left: Vec, right: Vec) -> Vec:
    return [x - y for x, y in zip(left, right, strict=True)]


def vec_scale(scale: Fraction, vec: Vec) -> Vec:
    return [scale * x for x in vec]


def trace(mat: Mat) -> Fraction:
    return sum((mat[i][i] for i in range(len(mat))), Fraction(0))


def trace_product(left: Mat, right: Mat) -> Fraction:
    dim = len(left)
    return sum(
        (left[i][j] * right[j][i] for i in range(dim) for j in range(dim)),
        Fraction(0),
    )


def is_zero_matrix(mat: Mat) -> bool:
    return all(entry == 0 for row in mat for entry in row)


# ---------------------------------------------------------------------------
# Qubit-register partial trace (qubit 0 = S = most significant bit)
# ---------------------------------------------------------------------------


def partial_trace_pure_pair(
    branches: list[tuple[Fraction, Fraction, Vec, Vec]],
    total_qubits: int,
    keep: tuple[int, ...],
) -> Mat:
    """Exact partial trace of sum_c w_c |alpha_c><beta_c| onto `keep`.

    Each branch contributes weight * Tr_T |alpha><beta|.  Vectors are exact
    Fraction amplitude lists of length 2**total_qubits.
    """
    traced = tuple(q for q in range(total_qubits) if q not in keep)
    kdim = 2 ** len(keep)
    result: Mat = [[Fraction(0)] * kdim for _ in range(kdim)]

    def split(index: int) -> tuple[int, int]:
        keep_part = 0
        traced_part = 0
        for position, qubit in enumerate(keep):
            bit = (index >> (total_qubits - 1 - qubit)) & 1
            keep_part |= bit << (len(keep) - 1 - position)
        for position, qubit in enumerate(traced):
            bit = (index >> (total_qubits - 1 - qubit)) & 1
            traced_part |= bit << (len(traced) - 1 - position)
        return keep_part, traced_part

    dim = 2**total_qubits
    for weight, _unused, alpha, beta in branches:
        by_traced: dict[int, dict[int, Fraction]] = {}
        for index in range(dim):
            amp = alpha[index]
            if amp:
                keep_part, traced_part = split(index)
                by_traced.setdefault(traced_part, {})[keep_part] = amp
        for index in range(dim):
            amp = beta[index]
            if amp:
                keep_part, traced_part = split(index)
                row_map = by_traced.get(traced_part)
                if row_map:
                    for row_keep, row_amp in row_map.items():
                        result[row_keep][keep_part] += (
                            weight * row_amp * amp
                        )
    return result


def partial_transpose_top_qubit(mat: Mat) -> Mat:
    """Partial transpose over the most significant qubit of the register."""
    dim = len(mat)
    half = dim // 2
    result: Mat = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            si, fi = divmod(i, half)
            sj, fj = divmod(j, half)
            result[sj * half + fi][si * half + fj] = mat[i][j]
    return result


# ---------------------------------------------------------------------------
# Exact binary-spectrum entropy bookkeeping
# ---------------------------------------------------------------------------


def entropy_float_binary(x: Fraction) -> float:
    """h((1+x)/2) in bits, descriptive float only."""
    p = (1 + float(abs(x))) / 2
    if p in (0.0, 1.0):
        return 0.0
    q = 1 - p
    return -(p * math.log2(p) + q * math.log2(q))


def binary_entropy_strictly_less(x: Fraction, y: Fraction) -> bool:
    """Exact certificate for h((1+x)/2) < h((1+y)/2)."""
    return abs(x) > abs(y)


def binary_entropy_equal(x: Fraction, y: Fraction) -> bool:
    return abs(x) == abs(y)


# ---------------------------------------------------------------------------
# W1: finite-time central-spin branching states
# ---------------------------------------------------------------------------

# Exact rational rotation R|0> = (cos, sin) with cos^2 + sin^2 = 1.
OVERLAP_MAIN = (Fraction(3, 5), Fraction(4, 5))  # a = 3/5
OVERLAP_IDEAL = (Fraction(0), Fraction(1))  # a = 0 (ideal CNOT / SBS)
OVERLAP_WEAK = (Fraction(24, 25), Fraction(7, 25))  # a = 24/25


def controlled_rotation_images(
    rotation: tuple[Fraction, Fraction],
) -> dict[str, Any]:
    """Exact unitarity and action facts for CR = |0><0| I + |1><1| R."""
    cos, sin = rotation
    unitary = cos * cos + sin * sin == 1
    return {
        "rotation_column": [frac_text(cos), frac_text(sin)],
        "exactly_unitary": unitary,
    }


def branching_state_branches(
    n_env: int, rotation: tuple[Fraction, Fraction]
) -> tuple[Vec, Vec]:
    """u = |0>|0..0>, v = |1>|r..r> for r = R|0>; both exact unit vectors.

    |Psi> = (u + v)/sqrt(2) is exactly the output of the central-spin
    circuit (CR on each environment qubit) applied to |+>_S |0..0>:
    CR fixes |0>|0> -> |0>|0> and maps |1>|0> -> |1>|r>.
    """
    cos, sin = rotation
    zero = [Fraction(1), Fraction(0)]
    one = [Fraction(0), Fraction(1)]
    rvec = [cos, sin]
    u: Vec = zero[:]
    v: Vec = one[:]
    for _ in range(n_env):
        u = kron_vec(u, zero)
        v = kron_vec(v, rvec)
    return u, v


def rank_two_spectrum(
    rho: Mat,
    plus_vec: Vec,
    minus_vec: Vec,
    lam_plus: Fraction,
    lam_minus: Fraction,
) -> bool:
    """Exact certificate that spec(rho) = {lam_plus, lam_minus, 0, ...}.

    rho is PSD by construction (partial trace of a PSD operator).  The
    certificate checks: unit trace, both eigenvector equations exactly,
    lam_plus + lam_minus = 1, and Tr rho^2 = lam_plus^2 + lam_minus^2.
    PSD + unit trace + the two verified eigenpairs summing to one force
    every remaining eigenvalue to be zero.
    """
    if trace(rho) != 1:
        return False
    if lam_plus + lam_minus != 1:
        return False
    if mat_vec(rho, plus_vec) != vec_scale(lam_plus, plus_vec):
        return False
    if mat_vec(rho, minus_vec) != vec_scale(lam_minus, minus_vec):
        return False
    return trace_product(rho, rho) == lam_plus**2 + lam_minus**2


def branching_fragment_analysis(
    n_env: int,
    rotation: tuple[Fraction, Fraction],
    fragment_env_qubits: tuple[int, ...],
) -> dict[str, Any]:
    """Exact plateau and audit facts for one fragment of a branching state.

    Fragment F = the named environment qubits; S is qubit 0.  Returns
    exact spectra parameters (x with spectrum {(1+x)/2, (1-x)/2}), the
    plateau identity, and the three audit-condition margins.
    """
    cos, _sin = rotation
    a = cos
    total = n_env + 1
    m = len(fragment_env_qubits)
    rest = n_env - m
    u, v = branching_state_branches(n_env, rotation)
    half = Fraction(1, 2)
    branches = [
        (half, half, u, u),
        (half, half, v, v),
        (half, half, u, v),
        (half, half, v, u),
    ]

    keep_sf = (0, *fragment_env_qubits)
    keep_f = fragment_env_qubits
    keep_s = (0,)
    rho_sf = partial_trace_pure_pair(branches, total, keep_sf)
    rho_f = partial_trace_pure_pair(branches, total, keep_f)
    rho_s = partial_trace_pure_pair(branches, total, keep_s)

    # Factorized branch vectors on the kept registers.
    zero = [Fraction(1), Fraction(0)]
    one = [Fraction(0), Fraction(1)]
    rvec = [rotation[0], rotation[1]]
    u_f: Vec = [Fraction(1)]
    v_f: Vec = [Fraction(1)]
    for _ in range(m):
        u_f = kron_vec(u_f, zero)
        v_f = kron_vec(v_f, rvec)
    u_sf = kron_vec(zero, u_f)
    v_sf = kron_vec(one, v_f)

    # Exact spectra certificates.
    x_s = a**n_env
    x_f = a**m
    x_sf = a**rest
    spec_s_ok = rank_two_spectrum(
        rho_s,
        [Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(-1)],
        (1 + x_s) / 2,
        (1 - x_s) / 2,
    )
    spec_f_ok = rank_two_spectrum(
        rho_f,
        [x + y for x, y in zip(u_f, v_f, strict=True)],
        [x - y for x, y in zip(u_f, v_f, strict=True)],
        (1 + x_f) / 2,
        (1 - x_f) / 2,
    )
    spec_sf_ok = rank_two_spectrum(
        rho_sf,
        [x + y for x, y in zip(u_sf, v_sf, strict=True)],
        [x - y for x, y in zip(u_sf, v_sf, strict=True)],
        (1 + x_sf) / 2,
        (1 - x_sf) / 2,
    )

    # Raw QD plateau identity: I(S:F) = H(S) iff H(F) = H(SF) iff
    # |x_f| = |x_sf| (exact binary-spectrum lemma).
    plateau_exact = binary_entropy_equal(x_f, x_sf)
    plateau_deviation_sign = (
        0
        if plateau_exact
        else (1 if binary_entropy_strictly_less(x_sf, x_f) else -1)
    )

    # Audit condition 1: one-shot perfect distinguishability of the
    # conditional fragment states <phi_0|phi_1>^m = a^m.
    conditional_overlap = a**m
    distinguishability_fails = conditional_overlap != 0

    # Audit condition 2: nonzero S:F discord, certified by an exact NPT
    # witness on rho_SF (entanglement implies nonzero discord in both
    # directions; zero-discord states are classical-quantum, hence
    # separable).  Compression of the partial transpose onto
    # span{|0> v_perp, |1> u_F} where v_perp = v_F - <u_F|v_F> u_F:
    # G = X^dagger rho^{T_S} X must be PSD if rho^{T_S} is; det G < 0
    # certifies a negative eigenvalue of the partial transpose.
    rho_pt = partial_transpose_top_qubit(rho_sf)
    v_perp = vec_sub(v_f, vec_scale(conditional_overlap, u_f))
    x_vec = kron_vec(zero, v_perp)
    y_vec = kron_vec(one, u_f)
    compression = [
        [
            vec_dot(x_vec, mat_vec(rho_pt, x_vec)),
            vec_dot(x_vec, mat_vec(rho_pt, y_vec)),
        ],
        [
            vec_dot(y_vec, mat_vec(rho_pt, x_vec)),
            vec_dot(y_vec, mat_vec(rho_pt, y_vec)),
        ],
    ]
    compression_det = (
        compression[0][0] * compression[1][1]
        - compression[0][1] * compression[1][0]
    )
    npt_entangled = compression_det < 0

    # Audit condition 2 quantified: pointer information accessible from F
    # is Holevo-bounded by chi = H(rho_F) (pure conditionals), and
    # chi < H(S) exactly iff |x_f| > |x_s|.
    access_gap_positive = binary_entropy_strictly_less(x_f, x_s)
    access_gap_bits = entropy_float_binary(x_s) - entropy_float_binary(x_f)

    return {
        "n_env": n_env,
        "fragment_env_qubits": list(fragment_env_qubits),
        "fragment_size": m,
        "single_fragment_overlap_a": frac_text(a),
        "spectra_certified_exact": bool(
            spec_s_ok and spec_f_ok and spec_sf_ok
        ),
        "spectrum_parameters": {
            "x_S": frac_text(x_s),
            "x_F": frac_text(x_f),
            "x_SF": frac_text(x_sf),
        },
        "entropies_bits_float_detail": {
            "H_S": entropy_float_binary(x_s),
            "H_F": entropy_float_binary(x_f),
            "H_SF": entropy_float_binary(x_sf),
            "I_SF": entropy_float_binary(x_s)
            + entropy_float_binary(x_f)
            - entropy_float_binary(x_sf),
        },
        "plateau_I_equals_H_S_exact": plateau_exact,
        "plateau_deviation_sign": plateau_deviation_sign,
        "audit_distinguishability": {
            "conditional_fragment_overlap": frac_text(conditional_overlap),
            "perfect_distinguishability_fails": distinguishability_fails,
        },
        "audit_discord": {
            "npt_compression_determinant": frac_record(compression_det),
            "rho_SF_entangled_hence_discord_positive": npt_entangled,
        },
        "audit_access_gap": {
            "holevo_pointer_bound_equals_H_F": True,
            "gap_H_S_minus_chi_strictly_positive": access_gap_positive,
            "gap_bits_float_detail": access_gap_bits,
        },
    }


# ---------------------------------------------------------------------------
# W2: perfect records with system-independent correlated junk (classical)
# ---------------------------------------------------------------------------


def dyadic_entropy(dist: dict[Any, Fraction]) -> Fraction:
    """Exact entropy in bits for distributions with power-of-two atoms."""
    total = Fraction(0)
    for probability in dist.values():
        if probability == 0:
            continue
        if probability.numerator != 1:
            raise AssertionError("non-dyadic atom in exact entropy")
        denominator = probability.denominator
        exponent = denominator.bit_length() - 1
        if 2**exponent != denominator:
            raise AssertionError("non-power-of-two atom in exact entropy")
        total += probability * exponent
    return total


def marginal(
    dist: dict[tuple, Fraction], positions: tuple[int, ...]
) -> dict[tuple, Fraction]:
    result: dict[tuple, Fraction] = {}
    for outcome, probability in dist.items():
        key = tuple(outcome[p] for p in positions)
        result[key] = result.get(key, Fraction(0)) + probability
    return result


def correlated_junk_model(
    n_fragments: int, junk_correlated: bool
) -> dict[str, Any]:
    """Joint distribution over (s, r_1..r_n, j_1..j_n).

    s: fair pointer bit, r_k = s exactly (perfect records, realized by
    exact CNOTs from |+>_S), j_k: junk bits never coupled to S -- either
    one shared fair coin copied to every fragment (correlated) or
    independent fair coins.  Fragment F_k = (r_k, j_k).  The quantum state
    is the diagonal embedding of this distribution, so every discord
    vanishes identically and all entropies are classical and exact.
    """
    dist: dict[tuple, Fraction] = {}
    for s in (0, 1):
        if junk_correlated:
            for j in (0, 1):
                outcome = (s, *([s] * n_fragments), *([j] * n_fragments))
                dist[outcome] = Fraction(1, 4)
        else:
            for junk in iproduct((0, 1), repeat=n_fragments):
                outcome = (s, *([s] * n_fragments), *junk)
                dist[outcome] = Fraction(1, 2 ** (n_fragments + 1))

    positions_s = (0,)
    fragment_positions = [
        (1 + k, 1 + n_fragments + k) for k in range(n_fragments)
    ]

    h_s = dyadic_entropy(marginal(dist, positions_s))
    plateau_rows = []
    for k, frag in enumerate(fragment_positions):
        h_f = dyadic_entropy(marginal(dist, frag))
        h_sf = dyadic_entropy(marginal(dist, positions_s + frag))
        plateau_rows.append(
            {
                "fragment": k + 1,
                "I_S_F_bits": frac_text(h_s + h_f - h_sf),
                "plateau_exact": h_s + h_f - h_sf == h_s,
            }
        )
    pair = fragment_positions[0] + fragment_positions[1]
    h_f1 = dyadic_entropy(marginal(dist, fragment_positions[0]))
    h_f2 = dyadic_entropy(marginal(dist, fragment_positions[1]))
    h_sf1 = dyadic_entropy(
        marginal(dist, positions_s + fragment_positions[0])
    )
    h_sf2 = dyadic_entropy(
        marginal(dist, positions_s + fragment_positions[1])
    )
    h_spair = dyadic_entropy(marginal(dist, positions_s + pair))
    h_pair = dyadic_entropy(marginal(dist, pair))
    joint_plateau = h_s + h_pair - h_spair == h_s
    conditional_mi = (h_sf1 - h_s) + (h_sf2 - h_s) - (h_spair - h_s)

    # Perfect distinguishability: conditional fragment supports disjoint.
    supports_disjoint = True
    for frag in fragment_positions:
        support: dict[int, set] = {0: set(), 1: set()}
        for outcome, probability in dist.items():
            if probability:
                support[outcome[0]].add(
                    tuple(outcome[p] for p in frag)
                )
        if support[0] & support[1]:
            supports_disjoint = False

    # SBS product form: conditional joint fragment distribution versus the
    # product of its fragment marginals, given the pointer.
    product_form_fails = False
    for s in (0, 1):
        conditional = {
            tuple(outcome[p] for p in pair): 2 * probability
            for outcome, probability in dist.items()
            if outcome[0] == s
        }
        left = marginal(conditional, (0, 1))
        right = marginal(conditional, (2, 3))
        for key, probability in conditional.items():
            split = left.get((key[0], key[1]), Fraction(0)) * right.get(
                (key[2], key[3]), Fraction(0)
            )
            if split != probability:
                product_form_fails = True

    # Uniqueness of the pointer decomposition: the two conditional
    # fragment-pair operators have disjoint record supports, hence are
    # linearly independent, so no rotated system basis admits an
    # alternative classical decomposition.
    conditional_supports = []
    for s in (0, 1):
        conditional_supports.append(
            {
                tuple(outcome[p] for p in pair)
                for outcome, probability in dist.items()
                if outcome[0] == s and probability
            }
        )
    decomposition_unique = not (
        conditional_supports[0] & conditional_supports[1]
    )

    return {
        "n_fragments": n_fragments,
        "junk_correlated": junk_correlated,
        "H_S_bits": frac_text(h_s),
        "per_fragment_plateau": plateau_rows,
        "joint_fragment_plateau_exact": joint_plateau,
        "raw_redundancy_fragments_at_plateau": sum(
            row["plateau_exact"] for row in plateau_rows
        ),
        "distinguishability_perfect": supports_disjoint,
        "discord_zero_by_diagonal_embedding": True,
        "fragment_pair_conditional_mutual_information_bits": frac_text(
            conditional_mi
        ),
        "sbs_product_form_fails": product_form_fails,
        "pointer_decomposition_unique": decomposition_unique,
        "fragment_entropy_bits": {
            "H_F1": frac_text(h_f1),
            "H_F2": frac_text(h_f2),
        },
    }


# ---------------------------------------------------------------------------
# Asymmetric control: exact plateau breaks when overlaps differ
# ---------------------------------------------------------------------------


def asymmetric_control() -> dict[str, Any]:
    """|Psi> = (|0>|0>|0> + |1>|r_1>|r_2>)/sqrt(2), overlaps 3/5 and 24/25.

    Fragment F1 has H(F1) with x = 3/5 while H(SF1) carries x = 24/25;
    the exact plateau identity fails in both directions.
    """
    a1 = OVERLAP_MAIN[0]
    a2 = OVERLAP_WEAK[0]
    zero = [Fraction(1), Fraction(0)]
    one = [Fraction(0), Fraction(1)]
    r1 = [OVERLAP_MAIN[0], OVERLAP_MAIN[1]]
    r2 = [OVERLAP_WEAK[0], OVERLAP_WEAK[1]]
    u = kron_vec(kron_vec(zero, zero), zero)
    v = kron_vec(kron_vec(one, r1), r2)
    half = Fraction(1, 2)
    branches = [
        (half, half, u, u),
        (half, half, v, v),
        (half, half, u, v),
        (half, half, v, u),
    ]
    rho_f1 = partial_trace_pure_pair(branches, 3, (1,))
    rho_sf1 = partial_trace_pure_pair(branches, 3, (0, 1))
    u_f1 = zero
    v_f1 = r1
    spec_f1_ok = rank_two_spectrum(
        rho_f1,
        [x + y for x, y in zip(u_f1, v_f1, strict=True)],
        [x - y for x, y in zip(u_f1, v_f1, strict=True)],
        (1 + a1) / 2,
        (1 - a1) / 2,
    )
    u_sf1 = kron_vec(zero, u_f1)
    v_sf1 = kron_vec(one, v_f1)
    spec_sf1_ok = rank_two_spectrum(
        rho_sf1,
        [x + y for x, y in zip(u_sf1, v_sf1, strict=True)],
        [x - y for x, y in zip(u_sf1, v_sf1, strict=True)],
        (1 + a2) / 2,
        (1 - a2) / 2,
    )
    plateau_fails = not binary_entropy_equal(a1, a2)
    return {
        "overlaps": [frac_text(a1), frac_text(a2)],
        "spectra_certified_exact": bool(spec_f1_ok and spec_sf1_ok),
        "x_F1": frac_text(a1),
        "x_SF1": frac_text(a2),
        "plateau_identity_fails_exactly": plateau_fails,
        "I_S_F1_minus_H_S_bits_float_detail": entropy_float_binary(a1)
        - entropy_float_binary(a2),
    }


# ---------------------------------------------------------------------------
# Ideal-family scaling: where the null's co-occurrence branch lives
# ---------------------------------------------------------------------------


def ideal_family_scaling(n_env: int) -> dict[str, Any]:
    """Exact fragment sweep of the pure symmetric family at a = 3/5.

    Two-sidedness computation: in the ideal pure branching family at large
    n and large fragments, plateau deviation, conditional-state overlap,
    and branch coherence all decay exponentially together, so the audit
    conditions co-occur with the plateau up to vanishing corrections.  The
    exact-plateau-with-finite-audit-failure witness therefore lives at
    finite overlap and small fragment number (W1) or in non-product
    environments (W2), not in the ideal asymptotic family.
    """
    a = OVERLAP_MAIN[0]
    rows = []
    for m in range(1, n_env):
        x_f = a**m
        x_sf = a ** (n_env - m)
        rows.append(
            {
                "fragment_size": m,
                "plateau_exact": binary_entropy_equal(x_f, x_sf),
                "I_minus_H_S_bits_float_detail": entropy_float_binary(x_f)
                - entropy_float_binary(x_sf),
                "conditional_overlap": frac_text(x_f),
                "branch_coherence_weight": frac_text(x_sf),
            }
        )
    return {
        "n_env": n_env,
        "overlap_a": frac_text(a),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Build artifact
# ---------------------------------------------------------------------------


def build_artifact() -> dict[str, Any]:
    checks = CheckBook([])

    # --- realizing dynamics are exact and in the declared class
    gate_main = controlled_rotation_images(OVERLAP_MAIN)
    gate_ideal = controlled_rotation_images(OVERLAP_IDEAL)
    gate_weak = controlled_rotation_images(OVERLAP_WEAK)
    checks.add(
        "controlled_rotations_exactly_unitary",
        gate_main["exactly_unitary"]
        and gate_ideal["exactly_unitary"]
        and gate_weak["exactly_unitary"],
        {"main": gate_main, "ideal": gate_ideal, "weak": gate_weak},
    )

    # --- W1, N = 2: every proper fragment exactly on the plateau,
    # every audit condition fails by a finite exact margin.
    w1_f1 = branching_fragment_analysis(2, OVERLAP_MAIN, (1,))
    w1_f2 = branching_fragment_analysis(2, OVERLAP_MAIN, (2,))
    checks.add(
        "W1_N2_spectra_certified_exact",
        w1_f1["spectra_certified_exact"] and w1_f2["spectra_certified_exact"],
    )
    checks.add(
        "W1_N2_raw_plateau_exact_on_both_fragments_redundancy_2",
        w1_f1["plateau_I_equals_H_S_exact"]
        and w1_f2["plateau_I_equals_H_S_exact"],
        {
            "I_S_F1_bits": w1_f1["entropies_bits_float_detail"]["I_SF"],
            "H_S_bits": w1_f1["entropies_bits_float_detail"]["H_S"],
        },
    )
    checks.add(
        "W1_N2_audit_distinguishability_fails_overlap_3_5",
        w1_f1["audit_distinguishability"][
            "perfect_distinguishability_fails"
        ]
        and w1_f1["audit_distinguishability"]["conditional_fragment_overlap"]
        == "3/5",
    )
    checks.add(
        "W1_N2_audit_discord_positive_via_exact_NPT",
        w1_f1["audit_discord"]["rho_SF_entangled_hence_discord_positive"]
        and w1_f2["audit_discord"][
            "rho_SF_entangled_hence_discord_positive"
        ],
        {
            "compression_det_F1": w1_f1["audit_discord"][
                "npt_compression_determinant"
            ],
        },
    )
    checks.add(
        "W1_N2_accessible_pointer_information_strictly_below_plateau",
        w1_f1["audit_access_gap"]["gap_H_S_minus_chi_strictly_positive"]
        and w1_f2["audit_access_gap"][
            "gap_H_S_minus_chi_strictly_positive"
        ],
        {
            "gap_bits_float_detail": w1_f1["audit_access_gap"][
                "gap_bits_float_detail"
            ]
        },
    )

    # --- W1, N = 4: half-environment fragments exactly on the plateau
    # with the same finite audit failures (experimental-scale register).
    w1_n4_half_a = branching_fragment_analysis(4, OVERLAP_MAIN, (1, 2))
    w1_n4_half_b = branching_fragment_analysis(4, OVERLAP_MAIN, (3, 4))
    checks.add(
        "W1_N4_spectra_certified_exact",
        w1_n4_half_a["spectra_certified_exact"]
        and w1_n4_half_b["spectra_certified_exact"],
    )
    checks.add(
        "W1_N4_half_fragments_exactly_on_plateau_redundancy_2",
        w1_n4_half_a["plateau_I_equals_H_S_exact"]
        and w1_n4_half_b["plateau_I_equals_H_S_exact"],
    )
    checks.add(
        "W1_N4_half_fragment_audit_fails_all_three_margins",
        w1_n4_half_a["audit_distinguishability"][
            "perfect_distinguishability_fails"
        ]
        and w1_n4_half_a["audit_discord"][
            "rho_SF_entangled_hence_discord_positive"
        ]
        and w1_n4_half_a["audit_access_gap"][
            "gap_H_S_minus_chi_strictly_positive"
        ],
        {
            "conditional_overlap": w1_n4_half_a["audit_distinguishability"][
                "conditional_fragment_overlap"
            ],
            "gap_bits_float_detail": w1_n4_half_a["audit_access_gap"][
                "gap_bits_float_detail"
            ],
        },
    )

    # --- control: ideal decoherence (a = 0) passes every audit.
    control_sbs = branching_fragment_analysis(2, OVERLAP_IDEAL, (1,))
    checks.add(
        "control_ideal_SBS_state_passes_every_audit",
        control_sbs["plateau_I_equals_H_S_exact"]
        and not control_sbs["audit_distinguishability"][
            "perfect_distinguishability_fails"
        ]
        and not control_sbs["audit_discord"][
            "rho_SF_entangled_hence_discord_positive"
        ]
        and not control_sbs["audit_access_gap"][
            "gap_H_S_minus_chi_strictly_positive"
        ],
        control_sbs["audit_discord"],
    )

    # --- control: asymmetric overlaps break the exact plateau.
    control_asym = asymmetric_control()
    checks.add(
        "control_asymmetric_overlaps_break_exact_plateau",
        control_asym["spectra_certified_exact"]
        and control_asym["plateau_identity_fails_exactly"],
        control_asym,
    )

    # --- W2: independence rung, exact at every tested scale.
    w2_rows = [correlated_junk_model(n, True) for n in (2, 3, 4)]
    checks.add(
        "W2_exact_plateau_all_fragments_all_scales",
        all(
            row["joint_fragment_plateau_exact"]
            and all(r["plateau_exact"] for r in row["per_fragment_plateau"])
            for row in w2_rows
        ),
        {
            "raw_redundancy": [
                row["raw_redundancy_fragments_at_plateau"] for row in w2_rows
            ]
        },
    )
    checks.add(
        "W2_distinguishability_perfect_and_discord_zero",
        all(
            row["distinguishability_perfect"]
            and row["discord_zero_by_diagonal_embedding"]
            for row in w2_rows
        ),
    )
    checks.add(
        "W2_sbs_product_form_fails_one_full_bit_uniform_in_scale",
        all(
            row["sbs_product_form_fails"]
            and row["pointer_decomposition_unique"]
            and row["fragment_pair_conditional_mutual_information_bits"]
            == "1/1"
            for row in w2_rows
        ),
        {
            "conditional_mutual_information_bits": [
                row["fragment_pair_conditional_mutual_information_bits"]
                for row in w2_rows
            ]
        },
    )
    control_independent = correlated_junk_model(2, False)
    checks.add(
        "control_independent_junk_passes_independence_audit",
        not control_independent["sbs_product_form_fails"]
        and control_independent[
            "fragment_pair_conditional_mutual_information_bits"
        ]
        == "0/1",
        {
            "conditional_mutual_information_bits": control_independent[
                "fragment_pair_conditional_mutual_information_bits"
            ]
        },
    )

    # --- two-sidedness: ideal-family scaling supports the null's
    # co-occurrence branch asymptotically.
    scaling = ideal_family_scaling(8)
    half_row = next(
        row for row in scaling["rows"] if row["fragment_size"] == 4
    )
    edge_row = next(
        row for row in scaling["rows"] if row["fragment_size"] == 1
    )
    checks.add(
        "two_sided_ideal_family_gap_decays_with_scale",
        half_row["plateau_exact"]
        and Fraction(half_row["conditional_overlap"].split("/")[0])
        / Fraction(half_row["conditional_overlap"].split("/")[1])
        < Fraction(3, 5)
        and not edge_row["plateau_exact"],
        {
            "half_split": half_row,
            "single_fragment": edge_row,
        },
    )

    if checks.passed != len(checks.checks):
        failed = [
            check["name"] for check in checks.checks if not check["passed"]
        ]
        raise AssertionError(f"failed checks: {failed}")

    return {
        "metadata": {
            "run_id": "RUN-20260803-d2-qd-sbs-audit-gap-witness",
            "campaign": (
                "Q-0063 decoherence-null confrontation, discriminator D2"
            ),
            "frozen_plan": (
                "explorations/decoherence-null-audit-layer-confrontation-"
                "campaign-scoping-2026-08-03.md"
            ),
            "claim_grade": (
                "EXACT FINITE WITNESS COMPUTATION / KNOWN MATHEMATICS / "
                "AUDIT CONDITIONS ARE THE PUBLISHED SBS-OVER-QD CONDITIONS"
            ),
            "model_class": (
                "central-spin pure dephasing via exact controlled "
                "rotations; system-independent correlated environment "
                "ancillas"
            ),
        },
        "summary": {
            "checks_passed": checks.passed,
            "checks_total": len(checks.checks),
            "result": "PLATEAU_WITH_FAILED_AUDIT_WITNESSED",
            "frozen_table_branch": (
                "KILLS_THE_NULL_STRONG_FORM_AT_REALIZABLE_SCALES"
            ),
            "two_sided_rider": (
                "IDEAL_FAMILY_CO_OCCURRENCE_AT_LARGE_SCALE_RECORDED"
            ),
        },
        "results": {
            "W1_N2_fragment_1": w1_f1,
            "W1_N2_fragment_2": w1_f2,
            "W1_N4_half_fragment_12": w1_n4_half_a,
            "W1_N4_half_fragment_34": w1_n4_half_b,
            "control_ideal_SBS": control_sbs,
            "control_asymmetric": control_asym,
            "W2_correlated_junk": w2_rows,
            "control_independent_junk": control_independent,
            "ideal_family_scaling": scaling,
        },
        "checks": checks.checks,
        "limits": [
            "All states are exact finite fixtures in the declared "
            "central-spin class; no continuum, thermal, or hardware claim.",
            "The audit conditions witnessed are exactly the published "
            "SBS / strong-quantum-Darwinism conditions; no novelty claim.",
            "Entanglement certifies nonzero discord; the exact optimal "
            "discord value is not computed.",
            "The Holevo gap bounds pointer-observable access; it is not "
            "the full Henderson-Vedral optimization.",
            "W2's independence failure carries no system information; "
            "whether it is an operational objectivity failure or only an "
            "SBS-definition failure is contested in the literature and is "
            "recorded, not resolved, here.",
            "The ideal-family scaling sweep shows plateau and audit "
            "co-occur asymptotically in the pure symmetric family; the "
            "witness lives at finite overlap, small fragments, or "
            "correlated environments.",
            "No grade movement, banking, prediction, paper, routing, or "
            "external action follows from this probe.",
        ],
    }


def main() -> None:
    artifact = build_artifact()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    ARTIFACT_PATH.write_text(rendered, encoding="utf-8")
    summary = artifact["summary"]
    print(
        f"{summary['checks_passed']}/{summary['checks_total']} checks passed"
    )
    print(f"result: {summary['result']}")
    print(f"frozen-table branch: {summary['frozen_table_branch']}")
    print(f"artifact: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
