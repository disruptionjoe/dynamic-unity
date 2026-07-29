---
title: "Massive tails, the dispersive-margin no-go, and formed-relay reconstruction"
date: 2026-07-28
status: banked_scoped_result
claim_id: HC-DU-104
work_id: CCR-MASSIVE-TAIL-FORMED-RELAY-GATE
run_id: RUN-20260728-225200-massive-tail-formed-relay-gate
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
maximum_grade: "Grade 4 scoped passive-carrier margin no-go and formed-relay necessity; conditional Grade 3 finite relay reconstruction"
---

# Massive tails, the dispersive-margin no-go, and formed-relay reconstruction

## Executive result

The swing returned:

```text
MASSIVE_TAIL_REMOVES_SHARP_HUYGENS_ZERO_ONLY_LOCALLY
+ SINGLE_MASSIVE_POINT_CARRIER_HAS_INFINITELY_MANY_TIMELIKE_BLIND_SHELLS
+ FINITE_FIXED_MASSIVE_FAMILY_HAS_NO_UNBOUNDED_UNIFORM_MARGIN
+ GENERIC_MULTIPLE_MASSES_MAY_REMOVE_COMMON_EXACT_ZEROS_BUT_NOT_DECAY
+ COMPACT_ZERO_FREE_SEPARATION_CLASS_HAS_A_POSITIVE_MARGIN
+ FORMED_SHORT_RANGE_RELAYS_CAN_COMPOSE_LOCAL_MARGIN
+ ABSTRACT_SUBDIVISION_IS_NOT_RECORD_FORMATION
+ NONLINEAR_WAVE_INTERACTIONS_ARE_ACTIVE_RELAY_CANDIDATES
+ THE_PUBLISHED_INVERSE_POSITIVE_RETAINS_A_SUPPLIED_CONTINUUM_INTERFACE
+ PASSIVE_DIRECT_CARRIER / UNBOUNDED_DEPTH / UNIFORM_MARGIN FORM_A_TRILEMMA
+ NO_READY_SUCCESSOR
```

`HC-DU-103` left massive fields, multiple carriers, and nonlinear interaction
as possible exits from the sharp-Huygens counterexample. This swing separates
them.

A massive Klein--Gordon field does place a response tail inside the light
cone. It does **not** make one passive carrier globally order-reflecting. For
proper-time separation \(\tau>0\), the timelike-interior point-response kernel
in \(3+1\)-dimensional Minkowski spacetime is, up to sign,

\[
K_m(\tau)
=
\frac{m}{4\pi\tau}J_1(m\tau).
\tag{1}
\]

It has exact blind shells at

\[
\tau=\frac{j_{1,k}}{m},
\qquad k=1,2,\ldots,
\tag{2}
\]

and decays as \(O(\tau^{-3/2})\). Consequently:

1. one massive point carrier still misses infinitely many strictly timelike
   separations; and
2. every fixed finite family of such carriers has combined amplitude tending
   to zero at large timelike separation, even if its masses are chosen so
   that the carriers have no common exact zero.

Thus a finite passive massive family cannot supply one positive response
margin over an unbounded timelike horizon.

There is a clean conditional repair. On a compact separation interval where
the finite family has no common zero, continuity gives a positive uniform
local margin. If the physical dynamics independently forms intermediate
relay events so that every long cover relation is represented by a chain of
these short, robust response edges, transitive closure reconstructs the
original finite causal order.

The adjective **formed** is load-bearing. Adding vertices to a diagram changes
no physical record. A relay must be an admitted occurrence with independently
warranted local coupling, retained identity and provenance, acquired
response, and a resource account.

This identifies a more coherent architecture than one direct global probe:

> Robust large-scale causal reconstruction can be compositional. A physical
> law need only provide a reliable local response scale if it also forms and
> exposes enough intermediate interaction events for those local relations
> to compose.

That is the exact point where distributed-systems structure and quantum-field
propagation can meet without metaphor. Global order is the transitive closure
of physically formed local interaction edges. It is not inferred from a
global clock, and it is not supplied by abstract graph subdivision.

Nonlinear Lorentzian inverse problems make this route scientifically serious.
Their interacting waves create new singularities that can act as
geometry-bearing intermediate events. But the published positive uses a rich
continuum source-to-solution map in a supplied observer region. It does not
yet select a finite formed relay packet or its certified record interface.

## 1. Exact massive-field control

### 1.1 Retarded kernel

For the massive Klein--Gordon equation

\[
(\Box+m^2)G_{\mathrm{ret}}
=
\delta(t)\delta^{(3)}(\mathbf x),
\]

the retarded Green function in \(3+1\)-dimensional Minkowski spacetime can be
written

\[
G_{\mathrm{ret}}(t,r)
=
\frac{\delta(t-r)}{4\pi r}
-
\frac{m\,\Theta(t-r)}
     {4\pi\sqrt{t^2-r^2}}
J_1\!\left(m\sqrt{t^2-r^2}\right).
\tag{3}
\]

Forgács and Lukács derive this form explicitly in Appendix B of
[their 2021 paper](https://link.springer.com/article/10.1140/epjc/s10052-021-09022-x).

Inside the future light cone, set

\[
\tau=\sqrt{t^2-r^2}>0.
\]

The null-cone delta term is absent and the interior tail is
\(-K_m(\tau)\), with \(K_m\) given by (1). Mass therefore removes the broad
sharp-Huygens interior zero of the massless field. That is a genuine repair
of the particular `HC-DU-103` counterexample.

It is only a local repair.

### 1.2 Near-coincidence response

The Bessel expansion

\[
J_1(z)=\frac z2+O(z^3)
\]

gives

\[
\lim_{\tau\downarrow0}K_m(\tau)
=
\frac{m^2}{8\pi}.
\tag{4}
\]

Because \(J_1(z)>0\) before its first positive zero, one point carrier has no
interior blind shell on

\[
0<\tau<\frac{j_{1,1}}m,
\qquad
j_{1,1}\simeq3.8317059702.
\tag{5}
\]

On every compact subinterval of (5), its absolute response has a positive
minimum. This is the simplest exact local-margin positive.

### 1.3 Blind shells

The NIST Digital Library of Mathematical Functions records that \(J_1\) has
infinitely many simple positive real
[zeros](https://dlmf.nist.gov/10.21). Hence

\[
K_m(j_{1,k}/m)=0
\tag{6}
\]

for every positive zero \(j_{1,k}\).

These are point-kernel controls. A finite extended source and detector
integrate the kernel over their supports, so a central point separation at
(6) need not make every smearing exactly zero. Conversely, finite smearing
can introduce additional cancellations. The honest result is:

> One standard massive point-response carrier is not an exact detector of
> every timelike separation.

It is not:

> Every massive smeared response vanishes on the same shells.

That stronger statement is neither needed nor earned.

## 2. Finite massive-family global-margin no-go

### Theorem 1 — finite passive massive families have no unbounded margin

Fix finitely many masses \(m_1,\ldots,m_N>0\) and fixed finite
normalizations. Define

\[
A_{\mathcal M}(\tau)
=
\max_{1\le a\le N}|K_{m_a}(\tau)|.
\tag{7}
\]

Then, for every \(\tau_0>0\),

\[
\inf_{\tau\ge\tau_0}A_{\mathcal M}(\tau)=0.
\tag{8}
\]

#### Proof

The standard large-argument Bessel asymptotic gives

\[
J_1(z)
=
\sqrt{\frac{2}{\pi z}}
\left(
\cos(z-3\pi/4)+O(z^{-1})
\right).
\tag{9}
\]

Therefore, for every fixed \(m_a\),

\[
K_{m_a}(\tau)=O(\tau^{-3/2})
\qquad
(\tau\to\infty).
\tag{10}
\]

The maximum of finitely many functions converging to zero also converges to
zero:

\[
A_{\mathcal M}(\tau)\longrightarrow0.
\]

This implies (8). \(\square\)

The component asymptotic is standard; see
[DLMF §10.17](https://dlmf.nist.gov/10.17). The theorem's content for Dynamic
Unity is the typed consequence for `HC-DU-103`'s response-margin premise.

### Corollary 1 — generic exact coverage does not imply robust coverage

Several distinct masses may avoid a common exact Bessel zero on a declared
interval. That can repair exact zero/nonzero coverage on that interval. It
does not repair (8).

For every proposed threshold \(\gamma>0\), there is a sufficiently large
timelike separation for which

\[
|K_{m_a}(\tau)|<\gamma
\quad
\text{for every }a.
\tag{11}
\]

Thus:

\[
\text{pointwise nonzero}
\;\centernot\Longrightarrow\;
\text{uniformly detectable}.
\tag{12}
\]

This matters because `HC-DU-103`'s robust reconstruction requires one
zero/signal gap fixed before the held-out geometry is known.

### Scope

Theorem 1 covers the standard freely propagating, fixed-normalization,
timelike-interior point-response tails of a finite massive Klein--Gordon
family. The same conclusion extends to fixed smooth compact smearings when
the translated responses obey the corresponding dispersive decay.

It is not a universal theorem over:

- every linear hyperbolic field on every background;
- long-range or topological charges;
- massless null-shell relay networks;
- adaptive amplifiers or target-dependent source normalization;
- infinite carrier families;
- bound modes, cavities, or nondecaying media; or
- nonlinear interaction-generated events.

Each is a class exit with a new selection, resource, or interface burden.

## 3. Compact local-margin positive

### Theorem 2 — compact zero-free families have a margin

Let \(I\subset(0,\infty)\) be compact. For a fixed finite massive family,
suppose

\[
\forall \tau\in I,\qquad
\max_a |K_{m_a}(\tau)|>0.
\tag{13}
\]

Then

\[
\gamma_I
:=
\min_{\tau\in I}
\max_a |K_{m_a}(\tau)|
>0.
\tag{14}
\]

#### Proof

The finite maximum of the continuous functions \(|K_{m_a}|\) is continuous.
It is strictly positive on compact \(I\), so it attains a strictly positive
minimum. \(\square\)

For one mass, every compact

\[
I\subset(0,j_{1,1}/m)
\]

satisfies the premise.

This is the first usable positive from the massive repair:

> A massive tail can support robust short-range causal edges on a frozen,
> zero-free separation class.

The result still supplies the mass, point-response idealization, separation
class, normalization, and detector calibration. It does not select them.

There is also a reconstruction circularity to avoid. The interval \(I\) is
written in the held-out proper-time variable. A record-first construction
cannot inspect the unknown geometry, place a relay whenever
\(\tau<j_{1,1}/m\), and then claim to have reconstructed that geometry. The
short-range class must instead be selected by an antecedent physical law or
operational rule—for example, a fixed local coupling and threshold whose
coverage is proved afterward. The mass supplies a physical scale inside the
assumed Klein--Gordon geometry; it does not by itself derive the geometry from
records.

## 4. Formed-relay composition

The global-margin failure does not imply that robust causal reconstruction is
impossible. It rules out one architecture: a finite fixed passive carrier
family directly detecting every causal depth at one threshold.

### Definition — formed relay extension

Let \((E,\prec)\) be the original finite event poset. A **formed relay
extension** consists of:

1. a finite event set \(E'\supseteq E\);
2. a sound causal order \(\prec'\) whose restriction to \(E\) is \(\prec\);
3. independently localized physical occurrences for every event in
   \(E'\setminus E\);
4. a directed response graph \(D\subseteq\prec'\);
5. retained identities and provenance for the relay events and edges; and
6. an acquisition contract that includes failed attempts and preserves
   source/readout pairing.

Items 3--6 distinguish a physical relay extension from drawing extra points
on a causal curve. The relay-placement or relay-formation rule must also be
fixed without querying the held-out cover lengths or target geometry.

### Theorem 3 — formed-relay finite-order reconstruction

Suppose \(D\subseteq\prec'\) is sound and, for every cover edge
\((x,y)\) of the original poset \((E,\prec)\), there is a finite directed
\(D\)-path in \(E'\) from \(x\) to \(y\). Then

\[
D^+\cap(E\times E)=\prec.
\tag{15}
\]

If every path edge has true response zero or at least
\(\gamma_{\mathrm{local}}>0\), and every acquired estimate has error below
\(\gamma_{\mathrm{local}}/2\), thresholding recovers the same result exactly.

#### Proof

Each original cover edge is in \(D^+\) by the path premise. Every comparison
in a finite poset factors through cover edges, so
\(\prec\subseteq D^+\cap(E\times E)\). Soundness of every relay edge and
transitivity of \(\prec'\) give the reverse inclusion. The robust statement is
the threshold corollary already proved in `HC-DU-103`. \(\square\)

The graph mathematics is standard. The physical hinge is whether the relay
events and their local response edges are formed and acquired without using
the held-out geometry as their definition.

### Why subdivision alone fails

Let the retained event packet contain only \(x\) and \(y\). Inserting
unobserved mathematical points \(z_1,\ldots,z_k\) into a candidate causal
curve does not alter:

- the event set in the record;
- the admitted source/readout operations;
- the measured response graph; or
- the completion fibre induced by that record.

It therefore cannot repair a missing detected edge.

This is consistent with the repository's existing relay/refinement guard.
An inert deterministic relay can be a representation refinement and should
often be quotiented. A formed physical relay is different precisely when it
carries an independently detectable occurrence, coupling, resource, latency,
or response that changes the operational record.

## 5. The passive-carrier trilemma

For the scoped finite massive-family class, the following three demands
cannot be held together:

1. **direct passive carrier:** infer each original relation from a direct
   fixed source-to-readout response;
2. **unbounded causal depth:** admit arbitrarily large timelike separation;
3. **uniform positive margin:** use one predeclared threshold
   \(\gamma>0\).

Theorem 1 shows that a finite fixed massive family can retain at most two.

The principal repairs and their prices are:

| Repair | What it gains | What it adds |
|---|---|---|
| Bound the separation class | Compact zero-free margin | A horizon/compactness premise |
| Choose a new carrier or normalization by target | Detectability | Target-dependent refit and resource change |
| Use infinitely many carriers | Possible coverage | Infinite interface and acquisition burden |
| Use a cavity/bound/topological mode | Nondecaying signal | New background, boundary, or sector |
| Form physical short-range relays | Compositional global order | Event formation, localization, provenance, acquisition |
| Use nonlinear interactions | Dynamical intermediate signatures | Nonlinear law and rich active source interface |

This is not a no-go against causal reconstruction. It locates which
architecture could work.

## 6. Nonlinear interaction is the serious active-relay route

Lassas, Uhlmann, and Wang study

\[
\Box_g u+H(x,u)=f
\]

on a four-dimensional Lorentzian spacetime. Their
[source-to-solution theorem](https://arxiv.org/abs/1606.06261) shows that a
map from local sources \(f\) to observed solutions \(u|_V\), for \(V\) near a
timelike geodesic, determines the topology, differentiable structure, and
conformal class in the maximal region where waves can leave and return.

The nonlinearity is not decorative. Interacting waves create new
singularities at their intersection. Those new singularities propagate and
can reveal causal geometry unavailable from one passive linear response.

In Dynamic Unity's typed vocabulary, that construction is closer to a
**dynamically formed relay** than to a stronger version of one massive tail:

```text
localized source events
-> propagating waves
-> nonlinear interaction occurrence
-> newly propagating singularity
-> observer-region response
-> geometric inference
```

This is the strongest constructive direction after the trilemma because the
intermediary is generated by the physical equation rather than inserted as a
graph label.

It still does not supply:

- target-independent operational names for every interaction occurrence;
- a physically selected source and observation interface;
- one finite source packet rather than a continuum map;
- a uniform finite-response and inverse margin on a compact completion class;
- complete attempt-level acquisition;
- certified provenance from the source events through the interaction;
- a formed archive or observer-access rule; or
- no-refit transfer across arenas.

The theorem is a real conformal-reconstruction positive. The missing work is a
finite, formed, physically selected interface theorem.

## 7. What this teaches the North Star

Before this swing, the leading response-based architecture implicitly asked
one finite carrier packet to see every causally relevant relation directly.
The massive-field test shows why that is the wrong default at scale.

The better architecture is:

```text
physical dynamics
-> formed local interaction events
-> robust short-range response edges
-> authenticated/local provenance
-> transitive regional composition
-> finite causal order
-> conditional conformal reconstruction
```

This does not assert that nature is a distributed database. It states an
exact structural correspondence:

- a directed response edge is a physically realized `happens-before`
  witness;
- relay closure is valid only for events physically present in the process;
- regional/global order can be compositional without a global clock; and
- the reconstruction grade depends on formation, faithfulness, margin, and
  acquisition, not on the graph vocabulary.

The finding also clarifies the role of records. The propagator tail does not
become a record merely by existing. A record-bearing relay requires a physical
interaction that leaves a retained, accessible, provenance-preserving trace.
The field law may select which interactions are possible; the record
interface must still be earned.

## 8. Literature and novelty collision

The components are occupied:

- the massive Klein--Gordon Green function and its interior Bessel tail are
  standard;
- Bessel zeros and large-argument decay are standard analysis;
- finite-poset recovery through paths replacing cover edges is standard graph
  mathematics;
- dispersive loss of long-range pointwise amplitude is standard wave
  behavior; and
- nonlinear Lorentzian inverse problems already use interacting waves to
  reconstruct conformal geometry.

Dynamic Unity may claim:

1. the explicit collision between massive-tail decay and the uniform
   causal-saturation margin required by `HC-DU-103`;
2. the scoped passive-carrier/unbounded-depth/uniform-margin trilemma;
3. the exact distinction between abstract relay subdivision and physically
   formed relay composition; and
4. the corrected handoff from passive linear response to nonlinear
   interaction-generated event nets.

This is a scoped Grade-4 architecture/necessity result with a conditional
Grade-3 finite relay theorem. It is not new QFT, a new Bessel theorem, a new
inverse-problem theorem, a physical record selector, a conformal
reconstruction result for finite records, a physical remainder, a prediction,
or a standalone paper claim at present.

## 9. Disposition

The candidate class is narrowed from:

```text
target-independent operational event net
+ finite causally saturating carrier family
+ uniform response margin
```

to:

```text
target-independent physically formed event net
+ independently warranted local couplings
+ finite jointly realizable short-range response family
+ uniform local response margin
+ physically formed relay paths covering every original finite-order cover
+ complete attempt-level acquisition and provenance
+ compact finite-resolution completion class
+ no-refit held-out causal/conformal transfer
```

No inspected arena supplies the conjunction:

- the massive point kernel supplies only a scoped local margin;
- a finite massive family loses every global positive margin by dispersion;
- abstract relays supply no occurrences or records; and
- nonlinear inverse theorems retain a rich supplied continuum interface.

Dynamic Unity therefore remains quiescent. The exact reopener is:

> Reopen response-based causal/conformal reconstruction when a physical
> construction independently forms and localizes a finite relay event net,
> proves a uniform local response margin and cover-path saturation on a frozen
> compact completion class, completely acquires the relay provenance, and
> transfers unchanged to a held-out causal or conformal target.

The highest-information next candidate within this path is not another mass
or another passive response matrix. It is a finite-interface reduction of a
nonlinear interaction-generated source-to-solution construction, with the
interaction occurrences treated as formed events and with an explicit
no-refit margin.

That candidate is not yet ready enough to activate because no inspected
result selects its finite sources, interaction-event identities, observation
packet, or acquisition contract.

## 10. Regression artifact

The proportional control
[`du_massive_tail_formed_relay_probe.py`](../tests/du_massive_tail_formed_relay_probe.py)
preserves:

- the first positive \(J_1\) root;
- the corresponding massive point-response blind shell;
- a sampled positive short-range interval before that root;
- failure of a short-range response rule on a long two-event packet; and
- recovery after three relay events are admitted as formed nodes.

The generated artifact is
[`du_massive_tail_formed_relay_result.json`](../tests/artifacts/du_massive_tail_formed_relay_result.json).
It is a regression control, not scientific or empirical evidence.
