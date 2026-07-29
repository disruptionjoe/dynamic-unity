---
title: "Operational event identity, causal saturation, Huygens failure, and the finite conformal-reconstruction boundary"
date: 2026-07-28
status: banked_scoped_result
claim_id: HC-DU-103
work_id: CCR-OPERATIONAL-LOCALIZATION-CAUSAL-SATURATION-GATE
run_id: RUN-20260728-223722-operational-localization-causal-saturation-gate
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
maximum_grade: "Grade 4 scoped causal-saturation necessity and counterexample; conditional Grade 3 robust finite-poset reconstruction"
---

# Operational event identity, causal saturation, Huygens failure, and the finite conformal-reconstruction boundary

## Executive result

The swing returned:

```text
OPERATIONAL_PROVENANCE_CAN_IDENTIFY_EVENTS_WITHOUT_TARGET_COORDINATES
+ PROVENANCE_DOES_NOT_SELECT_LOCAL_FIELD_SUPPORT
+ MICROCAUSALITY_IS_ONE_WAY
+ ANTISYMMETRIC_COMMUTATOR_SUPPORT_REQUIRES_OPERATIONAL_ORIENTATION
+ FINITE_RESPONSE_RECONSTRUCTION_IFF_CAUSALLY_SATURATING
+ UNIFORM_MARGIN_GIVES_ROBUST_FINITE_RECOVERY
+ SHARP_HUYGENS_PROPAGATION_FAILS_DIRECT_TIMELIKE_ORDER_REFLECTION
+ A_SAMPLED_NULL_INTERMEDIARY_CAN_REPAIR_ONLY_THE_ENLARGED_FINITE_NET
+ PROPAGATOR_SPECTRUM_REMOVES_LABELS_BUT_LOSES_INCIDENCE
+ FINITE_EVENT_ORDER_IS_NOT_CONTINUUM_CONFORMAL_GEOMETRY
+ MULTI_CARRIER_OR_NONLINEAR_REPAIR_IS_A_NEW_INTERFACE_WITH_NEW_BURDENS
+ NO_READY_SUCCESSOR
```

The positive result is an exact but conditional finite theorem. Let \(E\) be a
finite set of independently identified operational events, let \(\prec\) be
their held-out causal order, and let \(D\) be the directed relation detected by
a declared family of local intervention/response carriers. If:

1. \(D\subseteq\prec\) (**soundness**); and
2. \(D\) contains every cover relation of the finite poset
   \((E,\prec)\) (**causal saturation**),

then the transitive closure \(D^+\) equals \(\prec\). Conversely, if a cover
edge is absent from \(D\), no transitive closure can recover it. If the true
responses are either zero or at least \(\gamma>0\), and their estimates have
error below \(\gamma/2\), thresholding recovers \(D\) and therefore the finite
order exactly.

The negative result is physical and exact. In the ordinary massless scalar
wave equation on \(3+1\)-dimensional Minkowski spacetime, sharp Huygens
propagation places the causal propagator on the null cone. Two small source
and readout regions may be strictly timelike related while their direct
smeared Pauli--Jordan response is exactly zero. A finite free-field response
packet can therefore satisfy microcausality and still fail causal saturation.

This closes the strongest reading of the candidate inherited from
`HC-DU-102`:

> Target-independent event names plus a finite calibrated Weyl response do
> not by themselves reconstruct causal order or conformal geometry.

They can do so only after a physically warranted carrier family, sampling
architecture, and uniform margin make the response relation
order-reflecting. Those are the substantive inverse premises; locality does
not derive them.

## 1. What target-independent operational identity can do

An event token need not be a coordinate. A retained record may identify an
occurrence by a tuple such as

\[
e=(\text{apparatus identity},\text{port},\text{local sequence token},
   \text{parent record hashes},\text{source/readout role}).
\]

If fixed before the held-out geometric comparison, such tokens can:

- distinguish repeated uses of one apparatus;
- preserve which intervention and readout records belong to one trial;
- bind source and readout roles to a causal provenance chain;
- support relabeling-invariant comparisons across candidate geometries; and
- avoid assigning the target spacetime coordinates to the records in advance.

This is a real improvement over a response matrix whose row and column labels
are metric-defined test-function supports.

It does **not** establish:

- that the apparatus couples to a local algebra \(\mathcal A(O)\);
- which spacetime region \(O\) realizes the event;
- that two devices' local sequence tokens define one global time order;
- that the event family separates spacetime points;
- that every causal relation is realized by an admitted intervention; or
- that the retained response packet has a stable inverse margin.

Operational provenance solves occurrence identity at the evidence layer. A
local QFT model, a physical coupling construction, or a separate localization
theorem must still warrant the map from apparatus events to local field
operations. Calling the event token “local” does not supply that map.

## 2. Finite causal-saturation theorem

### Definitions

Let \((E,\prec)\) be a finite strict poset. Let

\[
r_a(i,j)
\]

be the directed response from a source intervention at event \(e_i\) to a
readout at event \(e_j\), for an admitted carrier \(a\in\mathcal A\). Direction
is supplied by the intervention/readout protocol, not by the sign of the
abstract commutator alone.

For a declared threshold \(\gamma\ge0\), define

\[
i\,D_\gamma\,j
\quad\Longleftrightarrow\quad
\exists a\in\mathcal A:\ |r_a(i,j)|\ge\gamma .
\tag{1}
\]

For the exact zero/nonzero relation, take \(\gamma=0\) with “nonzero” in place
of the weak inequality.

Call \(D\):

- **sound** when \(D\subseteq\prec\);
- **cover-saturating** when every cover edge of \(\prec\) lies in \(D\); and
- **order-reflecting after closure** when \(D^+=\prec\).

### Theorem 1 — finite response reconstruction

If \(D\) is sound, then

\[
D^+=\prec
\quad\Longleftrightarrow\quad
D\text{ contains every cover edge of }\prec.
\tag{2}
\]

#### Proof

If every cover edge lies in \(D\), every comparison \(i\prec j\) in a finite
poset factors through a finite chain of cover edges. Therefore
\(\prec\subseteq D^+\). Soundness and transitivity of \(\prec\) give
\(D^+\subseteq\prec\), so equality follows.

Conversely, let \(i\prec j\) be a cover edge absent from \(D\). If
\((i,j)\in D^+\), there is a directed \(D\)-path from \(i\) to \(j\). A path
of length one would be the missing edge. A longer sound path supplies an
intermediate \(k\) with \(i\prec k\prec j\), contradicting that \((i,j)\) is
a cover. Hence \(D^+\ne\prec\). \(\square\)

This is standard finite-poset/graph mathematics. Dynamic Unity's result is
not a new graph theorem. The contribution is the typed boundary:
microcausality can warrant soundness, but it does not warrant cover
saturation.

### Corollary 1 — robust finite recovery

Assume each admitted response obeys a two-sided gap:

\[
r_a(i,j)=0
\quad\text{or}\quad
|r_a(i,j)|\ge\gamma
\qquad(\gamma>0),
\tag{3}
\]

and every estimate satisfies

\[
|\widehat r_a(i,j)-r_a(i,j)|\le\epsilon<\gamma/2.
\tag{4}
\]

Thresholding at \(\gamma/2\) exactly recovers the zero/nonzero response
relation. If that relation is sound and cover-saturating, its transitive
closure exactly recovers \(\prec\).

The proof is immediate: a true zero remains below \(\gamma/2\), while a true
signal remains above it. The important point is what the corollary does not
do. It does not derive the response gap, carrier family, event coverage,
instrument, or acquisition completeness.

## 3. Why microcausality supplies only the easy direction

For local observables in spacelike separated regions, AQFT microcausality
gives commutation. For a free scalar field, the Pauli--Jordan distribution is
the causal propagator, and its support is causal. Therefore a nonzero
properly localized retarded response can witness a causal relation.

The converse fails:

\[
\text{spacelike}
\Longrightarrow
\text{zero commutator response},
\qquad
\text{zero response}
\centernot\Longrightarrow
\text{spacelike}.
\tag{5}
\]

Zero response may arise from:

- sharp Huygens propagation after a null shell has passed;
- a carrier that does not couple to the relevant mode;
- symmetry or selection rules;
- destructive cancellation under smearing;
- an insensitive readout;
- finite bandwidth or access; or
- an incomplete intervention family.

There is a second typing point. The Pauli--Jordan form is antisymmetric:

\[
\sigma(f,h)=-\sigma(h,f).
\]

Its nonzero support by itself gives adjacency, not an operational arrow. The
arrow comes from the independently recorded fact that one port was
intervened on and another port was subsequently queried, or from a separately
selected retarded response. Without that protocol role, even a complete
commutator matrix does not orient the causal relation.

## 4. Exact Huygens counterexample

In four-dimensional Minkowski spacetime, the massless wave equation obeys the
sharp Huygens principle: the retarded/advanced fundamental solutions have
support on the null cone rather than throughout its timelike interior.
Yagdjian reviews the link between Huygens propagation and commutator support
and records the standard odd-spatial-dimension Minkowski result in
[arXiv:1206.0239](https://arxiv.org/abs/1206.0239).

Take

\[
p=(0,0,0,0),
\qquad
q=(2,0,0,0).
\]

Then \(q\) is strictly timelike to the future of \(p\):

\[
(q^0-p^0)^2-\|\mathbf q-\mathbf p\|^2=4>0.
\]

Choose sufficiently small relatively compact neighborhoods \(U\ni p\) and
\(V\ni q\) such that every difference \(y-x\), with \(x\in U\) and \(y\in V\),
remains timelike and bounded away from the null cone. The massless causal
propagator vanishes on \(V\times U\). Hence for all
\(f\in C_c^\infty(U)\) and \(h\in C_c^\infty(V)\),

\[
\sigma(f,h)=0,
\tag{6}
\]

even though \(U\) causally precedes \(V\).

This is not an exotic failure or a new-physics signal. It occurs in the
ordinary standard free theory.

Add a sampled intermediate event

\[
n=(1,1,0,0).
\]

Both \(p\to n\) and \(n\to q\) are null. A finite response graph containing
all three event tokens may detect \(p\,D\,n\) and \(n\,D\,q\), after which
transitive closure recovers \(p\prec q\). But the two-event packet
\(\{p,q\}\) cannot invent \(n\). The “repair” is an enlarged sampling and
record contract, not a theorem that every finite response packet is faithful.

This establishes the exact cheapest kill requested by `HC-DU-102`: one
physically standard field family, one strictly timelike comparison, and zero
direct response.

## 5. What survives from the Weyl route

`HC-DU-102` remains valid. For fixed labeled source/readout functions,

\[
W(\lambda f)^*W(h)W(\lambda f)
=e^{i\lambda\sigma(f,h)}W(h),
\tag{7}
\]

so a calibrated amplitude interval exposes \(\sigma(f,h)\) exactly.

`HC-DU-103` changes what that exactness means:

| Layer | What is earned | What remains open |
|---|---|---|
| Fixed-pair Weyl channel | Exact causal symplectic phase | Physical event and local-coupling selection |
| Finite response graph | Exact detected influence edges | Cover saturation and a uniform margin |
| Transitive closure | Exact finite order if all covers are detected | Whether the physical family detects them |
| Dense/full propagator | Null-geodesic singularity relation under standard hypotheses | Finite acquisition and target-independent labels |
| Causal order | Conditional conformal structure in a distinguishing continuum | Topology/density, scale, and full metric |

The full causal propagator remains geometrically rich. In the smooth case its
wavefront relation follows null geodesics; Sánchez Sánchez and Schrohe give
the corresponding finite-regularity results in
[arXiv:2203.04362](https://arxiv.org/abs/2203.04362). That fact supports the
continuum conditional bridge. It does not show that one finite, formed,
operational packet captures the wavefront relation.

## 6. The spectral alternative does not solve localization

Jones and Yazdi propose an asymptotic spectral-density law for the causal
propagator and discuss possible Lorentzian spectral geometry in
[arXiv:2606.00311](https://arxiv.org/abs/2606.00311). This is worth tracking
because a spectrum is basis- and relabeling-invariant. It may carry aggregate
dimension or volume information if the conjecture survives.

But relabeling invariance is not event reconstruction. Consider the two real
skew matrices \(K(v)\) associated with

\[
v_1=(5,0,0),
\qquad
v_2=(3,4,0).
\]

For a \(3\times3\) cross-product matrix,

\[
\det(\lambda I-K(v))
=\lambda(\lambda^2+\|v\|^2).
\]

Both matrices therefore have characteristic polynomial
\(\lambda(\lambda^2+25)\), while one has one nonzero labeled upper-triangular
incidence and the other has two. Spectrum alone cannot recover which
operational event pairs respond.

This exact finite control is not a physical isospectral-spacetime theorem and
does not refute the 2026 conjecture. It establishes the narrower logical
boundary: spectral density can be a useful invariant without selecting or
reconstructing event localization.

## 7. Repairs and their prices

### Massive fields or curvature tails

A massive scalar field in Minkowski spacetime and generic propagation on
curved spacetime can have support inside the light cone. That removes this
particular sharp-Huygens zero. It does not prove:

- nonzero response on every cover relation;
- freedom from cancellation under finite smearing;
- a common uniform lower margin;
- selection of the field mass, state, source, or readout; or
- transfer across a frozen completion class.

The repair is a new carrier-class hypothesis, not a consequence of locality.

### Multiple carrier fields

The union of several response relations may be causally saturating even when
each one is not. The theorem permits this. The program must still show that
the carrier family is physically selected, jointly executable, completely
acquired, and uniformly separated without choosing a new field after seeing
the target.

### Nonlinear source-to-solution maps

Nonlinear wave interactions can generate much richer inverse data. Lassas,
Uhlmann, and Wang prove that a semilinear source-to-solution operator near a
timelike geodesic determines the topology, differentiable structure, and
conformal class in a causally accessible region
([arXiv:1606.06261](https://arxiv.org/abs/1606.06261)). This remains the
strongest constructive absorber and guide.

It is not the free Weyl packet. Moving to that route adds:

- a nonlinear physical law and source family;
- a continuum source-to-solution surface;
- an observer region and localization contract;
- finite approximation and stability;
- complete acquisition; and
- no-refit transfer.

Those additions may be scientifically warranted, but they must be declared as
a new interface rather than credited to the bounded Weyl result.

## 8. Literature and novelty collision

The component mathematics is occupied:

- finite-poset recovery from cover relations is standard;
- microcausality and the Pauli--Jordan response are standard AQFT/QFT;
- the Huygens counterexample is standard wave-equation structure;
- propagation of singularities links the full causal propagator to null
  geometry;
- causal order conditionally determines conformal structure under standard
  spacetime hypotheses;
- nonlinear Lorentzian inverse problems already reconstruct conformal
  geometry from rich source-to-solution maps; and
- spectral density of the causal propagator is an active 2026 conjectural
  direction, not a completed finite localization theorem.

Dynamic Unity may claim:

1. the exact typed decomposition of operational event identity, local support,
   directed response, causal saturation, inverse margin, finite order, and
   continuum geometry;
2. the explicit Huygens collision against the finite Weyl
   order-reconstruction handoff;
3. the necessary-and-sufficient finite causal-saturation gate and its robust
   margin corollary; and
4. the corrected reopener for any future response-based North-Star candidate.

This is a scoped Grade-4 selection/necessity boundary with a conditional
Grade-3 finite reconstruction theorem. It is not new QFT, a new inverse
theorem, a physical remainder, a prediction, or a standalone paper claim at
present.

## 9. Disposition

The candidate class is narrowed from:

```text
target-independently-localized finite Weyl-response packet
with a uniform causal/conformal inverse margin
```

to:

```text
target-independent operational event net
+ independently warranted local couplings
+ finite jointly realizable carrier family
+ causal cover saturation
+ uniform response margin
+ complete acquisition
+ compact finite-resolution completion class
+ no-refit held-out transfer
```

That is not a ready successor. No inspected physical arena currently supplies
the whole conjunction. Dynamic Unity should remain quiescent rather than run
another free-field packet that changes only the number of sources or
readouts.

The exact reopener is:

> Reopen response-based causal/conformal reconstruction only when a physical
> construction independently forms event identities and local couplings and
> proves that one finite, jointly realizable carrier family is cover-saturating
> with a uniform positive margin on a frozen compact completion class.

A nonlinear or multi-field proposal may satisfy that trigger, but it must
earn its own instrument, finite-record, acquisition, and no-refit contracts.

## 10. Regression artifact

The proportional local control
[`du_operational_localization_causal_saturation_probe.py`](../tests/du_operational_localization_causal_saturation_probe.py)
preserves:

- a four-event finite poset reconstructed from all cover edges;
- exact failure after removing one cover edge;
- rational robust-margin recovery;
- the two-event sharp-Huygens miss and three-event null-intermediary repair;
  and
- equal skew spectra with different labeled incidence.

The generated artifact is
[`du_operational_localization_causal_saturation_result.json`](../tests/artifacts/du_operational_localization_causal_saturation_result.json).
It is a regression control, not empirical evidence.
