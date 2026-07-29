---
title: "Pairing-complete dual-valued source response and factorization fibre"
status: completed_scoped_result
doc_type: exact_finite_theorem_counterexamples_and_transfer_boundary
created: 2026-07-29
hypothesis_id: HC-DU-127
run_id: RUN-20260729-144940-pairing-complete-source-response
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
  - CH-SYN
warrants:
  - DERIVED
  - CONSTRUCTIVELY_REALIZED
maximum_grade: "Scoped Grade 4 exact finite dual-valued source-response completeness, pairing-necessity, query-span, scalar-action, and factorization-fibre theorem; no GU theorem, selected physical pairing, infinite-dimensional operator/domain result, continuum or quantum-field transfer, empirical excess, ontology priority, new law, new physics, or prediction"
probe: "../tests/du_pairing_complete_source_response_probe.py"
artifact: "../tests/artifacts/du_pairing_complete_source_response_result.json"
---

# Pairing-complete dual-valued source response

## Executive result

The swing returned:

```text
DUAL_VALUED_RESPONSE_IS_MINIMAL_FOR_COMPLETE_BILINEAR_QUERIES
+ BARE_OPERATOR_IS_COMPLETE ONLY WHEN THE PAIRING IS FIXED OR RESPONSE-DETERMINED ON ITS FIBRES
+ SAME BARE OPERATOR CAN DEFINE DIFFERENT PHYSICAL RESPONSES
+ ONE PHYSICAL RESPONSE HAS AN INFINITE SAME-SIGNATURE (K,M) FIBRE
+ BARE GRADING CAN CHANGE INSIDE ONE SOURCE-RESPONSE FIBRE
+ SCALAR ACTION SEES ONLY THE SYMMETRIC PART
+ SOURCE AND READOUT SPANS JOINTLY BOUND COMPLETENESS
+ HC-DU-126 SURVIVES AS THE FIXED-POSITIVE-PAIRING SPECIAL CASE
+ NO GU, INFINITE-DIMENSIONAL, OR QFT TRANSFER
+ NO READY SUCCESSOR
```

The key correction is simple:

> A physical linear source response is naturally a map from sources to
> covectors. Writing it as an operator on one vector space already uses a
> pairing to identify vectors with covectors.

Let

\[
K:V\longrightarrow V^*
\]

be a nondegenerate pairing and

\[
M:V\longrightarrow V
\]

an operator representative. The source-native response is

\[
C=K M:V\longrightarrow V^*,
\tag{1}
\]

or equivalently the bilinear functional

\[
B_C(y,x)=C(x)(y).
\tag{2}
\]

The complete physical response is \(C\), not \(M\) alone. If \(K\) is fixed
and invertible, this distinction is harmless because

\[
M=K^{-1}C.
\tag{3}
\]

If \(K\) is not fixed or otherwise determined on every \(M\)-fibre, it can be
decisive. The same numerical \(M\) can define different source responses,
while one source response can have infinitely many same-signature \((K,M)\)
factorizations.

This generalizes rather than retracts `HC-DU-126`. Its positive reciprocal
network already froze the voltage/current duality, Euclidean coordinate
pairing, grounding, probes, readout, and source calibration. Its response
matrix was a coordinate representation of \(C\). The new result states what
must be retained before that identification is exported to an indefinite,
nonreciprocal, complex, unbounded, or field-theoretic setting.

## 1. Layer-0 typing

Four objects must remain distinct:

| Object | Type | What it can determine |
|---|---|---|
| operator representative | \(M:V\to V\) | coordinate evolution only after its state-space identification is fixed |
| pairing / Riesz map | \(K:V\to V^*\) | how a vector becomes a physical covector or bilinear value |
| dual-valued response | \(C=KM:V\to V^*\) | every frozen bilinear source query |
| formed transcript | \(Y^\mathsf TCX\) plus trial lineage | only the responses actually probed and retained |

The response law and its formed record are also different. Equation (1) is the
object to be learned. A packet \(Y^\mathsf TCX\) becomes an operational record
only after the source probes \(X\), readout tests \(Y\), association, retention,
and observer access are supplied or selected.

This run is finite-dimensional and real. Over a complex vector space,
transpose becomes conjugate transpose and symmetric becomes Hermitian.

## 2. The dual-valued response theorem

Let \(V\) be finite-dimensional. Let \(C_1,C_2\in\operatorname{Hom}(V,V^*)\).
For source family \(X\subseteq V\) and readout-test family \(Y\subseteq V\),
define

\[
R_{X,Y}(C)
=
\bigl(C(x)(y)\bigr)_{y\in Y,\;x\in X}.
\tag{4}
\]

In chosen bases this is

\[
R_{X,Y}(C)=Y^\mathsf T C X.
\tag{5}
\]

### Theorem 1 — complete queries determine exactly \(C\)

If \(X\) and \(Y\) each span \(V\), then

\[
R_{X,Y}(C_1)=R_{X,Y}(C_2)
\quad\Longleftrightarrow\quad
C_1=C_2.
\tag{6}
\]

#### Proof

The reverse implication is immediate. For the forward implication, equality
on \(X\times Y\) extends by bilinearity to all \(V\times V\). For every
\(x\in V\), the covector \((C_1-C_2)x\) therefore vanishes on every
\(y\in V\), so it is zero. This holds for every \(x\), hence
\(C_1=C_2\). \(\square\)

### Corollary 1 — minimal complete record

Any record equivalence sufficient for every bilinear source query must refine
equality of \(C\). Since \(C\) itself predicts every query, it is the minimal
complete source-response record up to information-equivalent encoding.

“Minimal” names an equivalence relation, not a minimum physical memory, bit
count, detector, archive, or energy cost.

### Corollary 2 — query-relative completeness

For incomplete \(X\) or \(Y\), the minimal record is only the compressed
response \(Y^\mathsf TCX\). A nonzero response perturbation can vanish on the
retained source/readout spans and survive on a held-out query.

The exact control uses

\[
C_0=
\begin{pmatrix}
1&0\\0&1
\end{pmatrix},
\qquad
C_1=
\begin{pmatrix}
1&0\\0&2
\end{pmatrix}.
\tag{7}
\]

They agree on the source \(e_1\) with complete vector output and agree for
the readout \(e_1\) with complete source input. The held-out source or readout
\(e_2\) separates them. This is the source/readout version of DU's general
first-leak rule.

## 3. The pairing-necessity theorem

Let \(K\) be invertible and \(C=KM\).

### Theorem 2 — exact operator-sufficiency criterion

On a declared completion class of packets \((K,M)\), the record \(M\) is
sufficient for all source queries exactly when

\[
M_1=M_2
\quad\Longrightarrow\quad
K_1M_1=K_2M_2.
\tag{8}
\]

That is: \(C=KM\) must be constant on every \(M\)-fibre. Fixing \(K\) is the
standard sufficient case. It is not logically necessary if a separate law
determines \(K\), or if allowed variations of \(K\) vanish on
\(\operatorname{im}M\).

### Corollary 3 — fixed pairing

For fixed \(K\),

\[
M_1=M_2
\quad\Longleftrightarrow\quad
K M_1=K M_2.
\tag{9}
\]

Thus an operator is a complete coordinate representation of the response
when the pairing and source calibration are frozen.

### Theorem 3 — unrestricted variable-pairing obstruction

If \(K\) varies, neither implication below holds in general:

\[
M_1=M_2\;\Longrightarrow\;K_1M_1=K_2M_2,
\tag{10}
\]

\[
K_1M_1=K_2M_2\;\Longrightarrow\;(K_1,M_1)=(K_2,M_2).
\tag{11}
\]

Both failures occur in the smallest grading-capable dimension while the two
pairings retain the same normalized Krein signature.

### Witness A — same bare operator, different response

Take

\[
M=I,\qquad
K_X=
\begin{pmatrix}
0&1\\1&0
\end{pmatrix},
\qquad
K_Z=
\begin{pmatrix}
1&0\\0&-1
\end{pmatrix}.
\tag{12}
\]

Both pairings are symmetric involutions with signature \((1,1)\). But

\[
C_X=K_XM=K_X\ne K_Z=K_ZM=C_Z.
\tag{13}
\]

The fixed held-out query gives

\[
B_{C_X}(e_1,e_2)=1,
\qquad
B_{C_Z}(e_1,e_2)=0.
\tag{14}
\]

The bare operator does not determine the physical response.

### Witness B — same response, different bare grading

Let the grading be

\[
\Gamma=K_Z
\tag{15}
\]

and the common physical response be

\[
C=K_X.
\tag{16}
\]

Two packets factorize it:

\[
(K_1,M_1)=(K_X,I),
\tag{17}
\]

\[
(K_2,M_2)=
\left(
K_Z,\,
K_ZK_X
\right).
\tag{18}
\]

Both pairings have signature \((1,1)\). Both operators are self-adjoint
relative to their own pairing:

\[
M_i^\mathsf T K_i=K_iM_i.
\tag{19}
\]

Yet

\[
[M_1,\Gamma]=0,
\qquad
\{M_2,\Gamma\}=0.
\tag{20}
\]

The bare operators occupy opposite grading classes while

\[
K_1M_1=K_2M_2=C
\tag{21}
\]

and \(C\) anticommutes with \(\Gamma\) in both packets.

Therefore a grading or chirality classification made on \(M\) alone need not
descend to the complete source-response quotient. It becomes physical only
when the factorization, or an independently admitted factorization-facing
action, is part of the contract.

### Infinite same-signature factorization fibre

For every integer \(n\), define

\[
K_n=
\begin{pmatrix}
n&1\\1&0
\end{pmatrix},
\qquad
M_n=
\begin{pmatrix}
1&0\\-n&1
\end{pmatrix}.
\tag{22}
\]

Then

\[
\det K_n=-1,
\qquad
K_nM_n=K_X=C,
\tag{23}
\]

and every \(M_n\) is \(K_n\)-self-adjoint. Thus one complete source response
has an infinite family of distinct same-signature operator/pairing
factorizations.

This is an operational-duality fibre, not proof that the factorizations are
the same ontology. A factorization-facing intervention can reopen it.

## 4. Scalar action is a stricter object

Suppose an analyst is given only

\[
S_C(x)=\frac12 C(x)(x).
\tag{24}
\]

Then

\[
dS_C|_x(h)
=
\frac12\bigl(C(x)(h)+C(h)(x)\bigr).
\tag{25}
\]

The action determines only

\[
\operatorname{sym}C
=
\frac12(C+C^\mathsf T).
\tag{26}
\]

The exact control uses

\[
C_\pm=I\pm
\begin{pmatrix}
0&1\\-1&0
\end{pmatrix}.
\tag{27}
\]

Every quadratic value agrees:

\[
x^\mathsf TC_+x=x^\mathsf TC_-x=x^\mathsf Tx,
\tag{28}
\]

but

\[
e_1^\mathsf TC_+e_2=1,
\qquad
e_1^\mathsf TC_-e_2=-1.
\tag{29}
\]

Therefore:

- a quadratic source action does not contain a general nonsymmetric response;
- its actual derivative response is the symmetric part; and
- if \(C\) is symmetric—as when \(M\) is \(K\)-self-adjoint for symmetric
  \(K\)—polarization reconstructs \(C\).

For a two-dimensional symmetric response, the three fixed probes
\(e_1,e_2,e_1+e_2\) recover its three independent entries. This is the
coordinate-free reason behind `HC-DU-126`'s scalar-action query count.

## 5. Representation covariance

For a simultaneous source-coordinate change \(x=T x'\),

\[
K'=T^\mathsf TKT,
\qquad
M'=T^{-1}MT,
\qquad
C'=T^\mathsf TCT.
\tag{30}
\]

The identity

\[
K'M'=T^\mathsf T(KM)T
\tag{31}
\]

is verified exactly.

Consequently:

- if source relabelings are gauge, the physical response record is the
  allowed congruence orbit \([C]\);
- if source ports and their calibration are physical, the labeled \(C\) is
  the response record; and
- changing only \(K\) while holding \(M\) and the calibrated source labels
  fixed is not a coordinate change.

This prevents the counterexamples from being misread as ordinary basis
dependence.

## 6. Literature collision and novelty

The mathematical ingredients are mature.

- Mostafazadeh explicitly discusses the nonuniqueness of a metric operator and
  its consequences for physical observables in
  [*Pseudo-Hermiticity, PT-symmetry, and the Metric Operator*](https://arxiv.org/abs/quant-ph/0508214)
  and gives the wider representation framework in
  [*Pseudo-Hermitian Representation of Quantum Mechanics*](https://arxiv.org/abs/0810.5643).
- Albeverio, Günther, and Kuzhel show in
  [*J-self-adjoint operators with C-symmetries*](https://arxiv.org/abs/0811.0365)
  that the infinite-dimensional problem also depends on self-adjoint
  extension domains; domains of \(J\)-self-adjoint extensions correspond to
  additional extension data.
- Bilinear-form duality, polarization, rank-complete experimental design, and
  congruence are standard linear algebra.

The result is therefore not new mathematics saying that an inner product
matters. The DU increment is the typed composition:

1. the source-native response is \(C:V\to V^*\);
2. a formed record is the separately typed packet \(Y^\mathsf TCX\);
3. full source/readout spans are necessary and sufficient for complete
   no-refit source transfer;
4. \(M\) is sufficient exactly when \(C\) is constant on its fibres, with a
   fixed pairing/calibration contract as the standard sufficient case;
5. one response can leave an infinite factorization fibre; and
6. operator-level grading or topology is a physical remainder only after a
   factorization-facing action is independently admitted.

That is a reusable Grade-4 boundary, not a physical law or Grade-5
discriminator.

## 7. What changes in Dynamic Unity

### `HC-DU-126` is strengthened, not corrected away

The finite resistor-network response \(A\) was already \(C\) in a supplied
positive reciprocal calibration. Its exact reconstruction, intervention
minimum, and unbounded mediator-topology fibre remain unchanged.

Outside that arena, “response operator” should be read as:

> the complete dual-valued response or bilinear functional, represented by an
> operator only relative to a frozen pairing, domain, and readout contract.

### Field/direct-action comparisons become stricter

Matching a bare kernel at one supplied pairing is weaker than matching the
complete source functional. A valid elimination or duality must preserve, at
minimum:

- the dual-valued response \(C\);
- the allowed source and readout spaces;
- background dependence and the complete effective action from `HC-DU-116`;
- the state, measure, determinant, regulator, boundary, and counterterm
  packet when quantum/background targets are admitted; and
- every physically admitted factorization-facing capability.

Source-query equivalence still need not preserve local fields, stress
partitions, grading assignments, domains, or topology.

### GU remains a hostile specimen, not a premise

The read-only GU correction motivated this test because GU's physical
bilinear included a Krein pairing omitted by its first bare-operator probe.
DU independently verified the general finite mechanism.

Nothing here establishes:

- GU's pairing as physically selected;
- GU's operator/domain or Green-form packet;
- a Yukawa, chirality, generation, source-action, or `sigma=w1` result;
- an infinite-dimensional transfer; or
- a Dynamic Unity source-is-observer corollary.

GU's missing native pairing/domain packet is exactly the kind of structure
this theorem says cannot be omitted.

## 8. Exact reopener and stop

The finite theorem is closed. More \(2\times2\), resistor-network, or freely
chosen pairing examples add no value.

The physical reopener is:

> Supply one independently selected pairing, closed domain, adjoint/Green
> boundary form, source algebra, state/boundary packet, and physically formed
> source/readout interface in a serious field or direct-action theory; then
> test whether the unchanged dual-valued response reconstructs one held-out
> physical target without refit.

A positive would upgrade the finite control toward physical reconstruction.
Two equally admissible packets with the same retained response and different
held-out physical target would instead bank a pairing/domain nonselection or
remainder theorem.

No current arena satisfies that reopener, so no successor is selected.

## Honest status

`HC-DU-127` is a scoped Grade-4 finite necessity and completeness result
assembled from standard mathematics and exact rational controls. It clarifies
what the source-native record is and where operator-only reasoning fails.

It does not select the pairing, form a physical archive, determine an
observer, establish ontology priority, transfer to GU or QFT, produce
empirical excess, or supply new physics.
