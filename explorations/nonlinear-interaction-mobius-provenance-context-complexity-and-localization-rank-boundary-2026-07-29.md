---
title: "Nonlinear interaction: Möbius provenance, context complexity, and the localization-rank boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-105
work_id: CCR-NONLINEAR-INTERACTION-PROVENANCE-LOCALIZATION-GATE
run_id: RUN-20260729-054646-nonlinear-interaction-provenance-localization-gate
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
  - CH-MODEL
maximum_grade: "Grade 4 scoped context/resource/identifiability boundary; conditional Grade 3 finite interaction-provenance and localization theorem"
---

# Nonlinear interaction: Möbius provenance, context complexity, and the localization-rank boundary

## Executive result

The swing returned:

```text
BOOLEAN_MOBIUS_PACKET_EXACTLY_ISOLATES_BOUNDED_DEGREE_JOINT_RESPONSE
+ ANALYTIC_FINITE_AMPLITUDE_TAIL_IS_EXPLICITLY_BOUNDED
+ SMALLER_AMPLITUDE_TRADES_NONLINEAR_TAIL_FOR_CONTEXT_ERROR_AMPLIFICATION
+ ALL_2^K_BOOLEAN_CONTEXTS_ARE_WORST_CASE_NECESSARY_IN_THE_FROZEN_MODEL
+ FOUR_WAVE_SOURCE_PROVENANCE_REQUIRES_16_ON_OFF_CONTEXTS_IN_THAT_MODEL
+ JOINT_SOURCE_PROVENANCE_DOES_NOT_IDENTIFY_INTERACTION_LOCATION
+ TARGET_RECONSTRUCTION_IS_EQUIVALENT_TO_KERNEL_CONTAINMENT
+ ROBUST_LOCALIZATION_REQUIRES_A_UNIFORM_POSITIVE_QUOTIENT_MARGIN
+ HIGHER_ORDER_LINEARIZATION_AND_GAUSSIAN_BEAMS_ARE_STRONG_ABSORBERS
+ MULTIPLE_INTERACTIONS_ARE_NOT_AN_IN_PRINCIPLE_NO_GO
+ THE_PUBLISHED_POSITIVE_RETAINS_SUPPLIED_GEOMETRY_BOUNDARY_AND_PROBE_DESIGN
+ A_MIXED_DERIVATIVE_IS_NOT_ONE_FORMED_RECORD
+ NO_READY_SUCCESSOR
```

`HC-DU-104` identified nonlinear wave interaction as the most serious
physical route from robust local response to formed intermediate events.
This swing asks how much of the ideal continuum source-to-solution interface
can be reduced to a finite packet.

The answer is constructive but narrower than the desired result.

For \(k\) independently addressable source channels, the alternating
inclusion-exclusion sum over the \(2^k\) on/off source contexts cancels every
response term that omits at least one channel. If the response is polynomial
of total degree at most \(k\), dividing by the common source amplitude
\(\eta^k\) exactly recovers the coefficient of the pure joint monomial
\(\epsilon_1\cdots\epsilon_k\). For four-wave interaction this is a finite
16-context certificate.

For an analytic response, the same packet estimates the mixed coefficient
with an explicit higher-order tail. But two costs appear:

1. each context is a separate counterfactual source configuration requiring
   repeatability, reset, identity, and joined acquisition; and
2. reducing the amplitude suppresses the nonlinear tail while amplifying
   context-level acquisition error as \(\eta^{-k}\).

More importantly, the packet certifies **joint source dependence**, not the
spacetime identity of the interaction event. Site localization is a second
inverse problem. In a finite site model \(y=Bc\), a held-out target \(Lc\) is
exactly determined if and only if

\[
\ker B\subseteq\ker L.
\]

Full site recovery requires full column rank; robust recovery requires a
uniform positive singular margin on the target quotient.

Published Lorentzian nonlinear inverse theory supplies a powerful positive.
Higher-order wave interactions, finite-difference linearization, Gaussian
beams, and separation constructions can recover geometric or coefficient
information, including in the presence of multiple intersections. This
absorbs any claim that nonlinear-event localization is impossible in
principle.

It does not select Dynamic Unity's desired record. The construction begins
with a supplied globally hyperbolic spacetime or boundary setting, nonlinear
equation, source and observation regions, source-to-solution or
Dirichlet-to-Neumann operator, repeatable source family, and
geometry-informed probe construction. The interaction singularity is a
physical consequence of the equation; the mixed derivative is an
analytical comparison across source contexts; neither is automatically a
retained, observer-accessible, target-independent event record.

The blockade therefore moves:

> The missing object is no longer a generic nonlinear response. It is a
> physically selected, target-independent finite source/readout packet that
> forms, localizes, retains, and completely acquires interaction events with
> a uniform inverse margin and no-refit transfer.

## 1. Typed setup

Let \(X\) be a normed response space and let

\[
R:U\subset\mathbb R^k\longrightarrow X
\]

be the response of one frozen physical or mathematical system to \(k\)
source amplitudes

\[
\epsilon=(\epsilon_1,\ldots,\epsilon_k).
\]

Fix one amplitude \(\eta>0\). For every source subset
\(S\subseteq[k]\), define

\[
R_S(\eta)=R(\eta\mathbf 1_S),
\]

where \((\mathbf 1_S)_i=1\) exactly when \(i\in S\).

Define the top Boolean Möbius packet

\[
\mathfrak I_k(\eta)
=
\sum_{S\subseteq[k]}
(-1)^{k-|S|}
R_S(\eta).
\tag{1}
\]

The packet is finite, but its type must be stated honestly:

```text
2^k separately configured source contexts
-> 2^k joined response records
-> one alternating analytical combination
-> one joint-source coefficient estimate
```

This is not yet:

```text
one physical interaction occurrence
-> one retained event record
```

Those two arrows coincide only after a physical multiplexing or tagging
construction is independently supplied and validated.

## 2. Exact finite interaction-provenance theorem

### Theorem 1 — Boolean Möbius isolation

Suppose

\[
R(\epsilon)
=
\sum_{\alpha\in\mathbb N^k}
c_\alpha\epsilon^\alpha
\tag{2}
\]

is a formal power series on the admitted amplitude domain. Then

\[
\mathfrak I_k(\eta)
=
\sum_{\substack{\alpha_i\ge 1\\ i=1,\ldots,k}}
c_\alpha\eta^{|\alpha|}.
\tag{3}
\]

Consequently, if \(R\) is polynomial of total degree at most \(k\),

\[
\eta^{-k}\mathfrak I_k(\eta)
=
c_{\mathbf 1},
\qquad
\mathbf 1=(1,\ldots,1).
\tag{4}
\]

#### Proof

The contribution of a monomial \(c_\alpha\epsilon^\alpha\) to (1) is

\[
c_\alpha\eta^{|\alpha|}
\sum_{S\supseteq\operatorname{supp}\alpha}
(-1)^{k-|S|}.
\]

The inner Boolean sum is zero unless
\(\operatorname{supp}\alpha=[k]\), in which case it is one. This gives (3).
If every \(\alpha_i\ge1\) and \(|\alpha|\le k\), then
\(\alpha=\mathbf 1\), proving (4). \(\square\)

The theorem is standard Möbius inversion on the Boolean lattice. Its DU value
is typing what the finite packet actually certifies:

> The top alternating response is a certificate that all \(k\) declared
> source channels participate in the measured response term.

It does not certify where their waves met, whether one or several
interactions contributed, whether the interaction was archived, or whether
the source interface was physically selected.

### Four-wave specialization

The four-wave constructions used in nonlinear Lorentzian inverse problems
correspond to \(k=4\). In the frozen Boolean on/off design, the exact packet
contains

\[
2^4=16
\]

contexts, including the all-off baseline, four singleton sources, six pairs,
four triples, and the all-on context.

The alternating combination removes all effects attributable to fewer than
four declared sources. That is a real finite reduction of one derivative
coefficient. It is not a finite reduction of the full source-to-solution
operator.

## 3. The scoped context lower bound

It would be tempting to call 16 contexts globally minimal. That would be
false without fixing the experimental design and function class.

### Theorem 2 — every Boolean vertex is necessary in the unrestricted
multiaffine query model

Let the admissible response class be all multiaffine scalar functions on
\([0,1]^k\), and allow queries only at Boolean vertices
\(\{0,1\}^k\). To identify the coefficient of
\(x_1\cdots x_k\) for every admissible response, all \(2^k\) vertices are
necessary.

#### Proof

Suppose vertex \(v\in\{0,1\}^k\) is omitted. Define the Boolean delta
polynomial

\[
\delta_v(x)
=
\prod_{i:v_i=1}x_i
\prod_{i:v_i=0}(1-x_i).
\tag{5}
\]

It is multiaffine, vanishes at every Boolean vertex other than \(v\), and has
top coefficient

\[
(-1)^{k-|v|}\ne0.
\]

Therefore the zero response and \(\delta_v\) agree on every queried context
but have different top coefficients. \(\square\)

The scope is load-bearing. Different assumptions can change the count:

- homogeneous polynomial structure;
- exchange symmetry;
- complex phases;
- signed amplitudes;
- polarization identities;
- simultaneous multiplexing;
- prior sparsity; or
- a target coarser than the full mixed coefficient.

The earned statement is:

> Four-wave provenance costs 16 contexts in the unrestricted on/off
> multiaffine model—not in every possible physical design.

This converts “finite” into a concrete acquisition burden without
overclaiming a universal lower bound.

## 4. Finite-amplitude tail and acquisition-noise tradeoff

### Proposition 3 — analytic tail

Assume the coefficients of (2) satisfy the aggregate majorant

\[
\sum_{|\alpha|=n}\|c_\alpha\|
\le
M\rho^{-n},
\qquad n\ge0,
\tag{6}
\]

for some \(M>0\), \(\rho>0\). If \(0<\eta<\rho\), then

\[
\left\|
\eta^{-k}\mathfrak I_k(\eta)-c_{\mathbf1}
\right\|
\le
M\rho^{-k}
\frac{\eta/\rho}{1-\eta/\rho}.
\tag{7}
\]

#### Proof

Equation (3) leaves only multi-indices with all entries positive. After the
degree-\(k\) term, bound each total-degree shell by (6):

\[
\sum_{n=k+1}^{\infty}
M\rho^{-n}\eta^{n-k}
=
M\rho^{-k}
\sum_{j=1}^{\infty}(\eta/\rho)^j.
\]

The geometric series gives (7). \(\square\)

This is the finite-amplitude counterpart of the finite-jet control in
`HC-DU-100`. The shared coefficient majorant is a physical or model-class
premise; it is not created by inclusion-exclusion.

### Proposition 4 — context error amplification

If every acquired context has error

\[
\|\widehat R_S-R_S\|\le\varepsilon,
\]

then

\[
\left\|
\eta^{-k}
\sum_S(-1)^{k-|S|}
(\widehat R_S-R_S)
\right\|
\le
\frac{2^k\varepsilon}{\eta^k}.
\tag{8}
\]

The bound is sharp under independent adversarial error signs.

Combining (7) and (8) gives

\[
E(\eta)
\le
\frac{2^k\varepsilon}{\eta^k}
+
M\rho^{-k}
\frac{\eta/\rho}{1-\eta/\rho}.
\tag{9}
\]

For \(\eta\le\rho/2\),

\[
E(\eta)
\le
\frac{2^k\varepsilon}{\eta^k}
+
\frac{2M\eta}{\rho^{k+1}}.
\tag{10}
\]

The balancing amplitude therefore scales as

\[
\eta_\ast
\asymp
\varepsilon^{1/(k+1)}
\tag{11}
\]

up to the declared constants.

This is an important correction to “just take the derivative at zero.”
Smaller amplitudes suppress higher-order contamination but make finite
measurement error more destructive. A physical certificate needs a
calibrated amplitude window, response sensitivity, repeatability, and
complete acquisition—not merely differentiability of an ideal map.

## 5. Source provenance is not event provenance

Equation (1) identifies a response component that vanishes whenever any one
of the \(k\) source channels is absent. Several different physical histories
can nevertheless produce the same coefficient:

- one four-wave interaction at site \(p\);
- one four-wave interaction at site \(q\);
- several interaction sites whose propagated responses add;
- a distributed nonlinear region; or
- different site distributions that lie in the readout nullspace.

Thus:

```text
joint dependence on source labels
!=
identity of a spacetime interaction event
!=
retained provenance of that event
```

This is the principal new typing result of the swing. The mixed coefficient
is closer to provenance than a terminal output alone, but it is provenance
for the **source tuple**, not automatically for the **interaction
occurrence**.

## 6. Finite localization theorem

Freeze a finite candidate site class with weights

\[
c=(c_1,\ldots,c_n)^\top\in\mathbb R^n.
\]

Let the finite readout packet be

\[
y=Bc,
\qquad
B\in\mathbb R^{m\times n},
\tag{12}
\]

and let the held-out target be

\[
T(c)=Lc.
\]

### Theorem 5 — target-relative localization

There exists a map \(\Phi\) such that

\[
\Phi(Bc)=Lc
\quad\text{for every admitted }c
\tag{13}
\]

if and only if

\[
\ker B\subseteq\ker L.
\tag{14}
\]

#### Proof

If (13) holds and \(z\in\ker B\), then
\(\Phi(B(c+z))=\Phi(Bc)\), so \(Lz=0\). Conversely, if (14) holds, define
\(\Phi\) on \(\operatorname{im}B\) by \(\Phi(Bc)=Lc\). Kernel containment
makes this definition independent of the representative. \(\square\)

Full site recovery corresponds to \(L=I\), so it requires
\(\ker B=\{0\}\), equivalently full column rank. If \(m<n\), this is
impossible for arbitrary site weights.

The rank obstruction remains physical for nonnegative weights. Choose an
interior positive baseline \(c_0\) and any nonzero \(z\in\ker B\). For
sufficiently small \(\delta>0\), both

\[
c_\pm=c_0\pm\delta z
\]

are nonnegative, have the same record \(Bc_\pm\), and differ on every target
with \(Lz\ne0\).

### Robust version

Exact kernel containment is not enough for finite evidence. On the
target-relevant quotient, define the smallest admitted response gain

\[
\gamma
=
\inf_{\substack{z\ \text{target-relevant}\\\|z\|=1}}
\|Bz\|.
\tag{15}
\]

A positive \(\gamma\) gives stable inversion with error proportional to
\(\gamma^{-1}\). For full finite-dimensional site recovery, \(\gamma\) is
the smallest singular value of \(B\). Across a completion class, DU needs

\[
\inf_{m\in\mathcal M}\gamma(m)>0.
\tag{16}
\]

This is the nonlinear-interaction version of the uniform response margin
already required by `HC-DU-095` through `HC-DU-104`.

The theorem does not select:

- the finite site class;
- the source and readout modes;
- the matrix \(B\);
- the target \(L\);
- the norm or noise model;
- the positive margin; or
- the physical process that forms and archives the packet.

It states exactly what any proposed selection mechanism must deliver.

## 7. Collision with nonlinear Lorentzian inverse theory

### 7.1 The strong positive

Kurylev, Lassas, and Uhlmann's
[nonlinear Lorentzian inverse theorem](https://arxiv.org/abs/1405.3386)
uses the source-to-solution operator in a neighborhood of a timelike
geodesic. In four dimensions, nonlinear interactions determine topological,
differentiable, and conformal structure in the region where waves can leave
and return.

Lassas, Uhlmann, and Wang
[prove the corresponding semilinear result](https://arxiv.org/abs/1606.06261)
for

\[
\Box_g u+H(x,u)=f.
\]

The nonlinearity is constructive: interacting waves create singularities
whose propagation exposes geometry not available from one passive linear
response.

Lassas, Liimatainen, Potenciano-Machado, and Tyni later
[prove Hölder-stable recovery](https://arxiv.org/abs/2106.12257) of a
time-dependent zeroth-order coefficient in

\[
\Box_g u+qu^m=0,
\qquad m\ge4,
\]

from a Dirichlet-to-Neumann map. Their method uses higher-order
linearization and Gaussian beams. It does not assume convex boundary or that
two lightlike geodesics intersect only once. Its separation construction
shows that multiple candidate intersections are a technical inverse problem,
not an in-principle impossibility.

These are strong absorbers. DU must not claim:

- that nonlinear interactions have not been used for reconstruction;
- that finite differences cannot expose higher-order response;
- that multiple intersections necessarily destroy localization;
- that conformal information cannot be recovered from observer-local active
  measurements; or
- that a finite-rank localization criterion is itself new inverse-problem
  mathematics.

### 7.2 What those theorems supply

Across the cited positive constructions, some combination of the following
is antecedent:

- a globally hyperbolic Lorentzian manifold or boundary setting;
- a dimension and causal orientation;
- the wave operator and nonlinear law;
- a source region and observation region;
- a source-to-solution or Dirichlet-to-Neumann map;
- repeatable independent source parameters;
- the ability to take higher derivatives or finite differences;
- Gaussian-beam or geometric-optics solutions;
- null geodesic and intersection constructions;
- continuum boundary or observer-region response data; and
- a target already typed as conformal geometry or a coefficient.

This is legitimate inverse-problem mathematics. It is not yet a
record-selection theorem.

### 7.3 The no-refit concern

An existence proof may choose Gaussian beams whose geodesics meet at a
specified interior point and then show that the resulting response determines
the target. A Dynamic Unity record-first claim has a different burden:

1. fix the physical source and readout family without consulting the held-out
   geometry;
2. execute and acquire that family without dropping failed contexts;
3. show that the same packet has a uniform inverse margin across the frozen
   completion class; and
4. transfer the unchanged packet to a held-out causal or conformal target.

If the beam directions, interaction site, source supports, readout windows,
or separation matrix are redesigned after the target geometry is known, the
result is an adaptive inverse proof, not no-refit reconstruction from a
selected record.

This is not a criticism of the cited theorems. It identifies the additional
claim DU is asking them to support.

## 8. Formation and acquisition boundary

A nonlinear interaction can be a physical event: the equation makes a new
singularity or response component conditional on the incoming waves. But
event formation, record formation, and analytic attribution are distinct.

| Object | What forms it | What it establishes |
|---|---|---|
| Nonlinear interaction occurrence | Field dynamics | A physical interaction happened in the admitted model |
| Propagating singularity | Hyperbolic evolution | The interaction can influence later regions |
| Mixed derivative | Comparison across source contexts | Joint source dependence |
| Gaussian-beam localization | Source/readout geometry plus inverse analysis | Conditional interaction-site sensitivity |
| Acquired transcript | Instrument and controller | Which contexts and readouts were retained |
| Certified event record | Formation, identity, provenance, access, and validation | An occurrence is action-available to the observer |

The physical interaction is the most promising relay candidate seen in this
campaign because it is generated by the dynamics rather than drawn into a
graph. The row does not collapse: the physical event can be real even when
its localization and record interface remain supplied.

To turn the 16-context four-wave packet into a formed certificate requires at
least:

1. independently formed source-channel identities;
2. a repeatability or multiplexing theorem;
3. a shared baseline and stable reset contract;
4. joined attempt-level acquisition for all contexts;
5. a finite target-independent readout family;
6. a localization rank and uniform-margin certificate;
7. retained source-to-interaction-to-readout provenance;
8. a finite resource and accuracy account; and
9. no-refit transfer to a held-out target.

No external quantum hardware is needed to state or test these proof
obligations. A large numerical PDE build would only illustrate them until a
specific physical source and detector class is fixed.

## 9. Novelty and grade

The mathematical components are occupied:

- Boolean Möbius inversion and multiaffine interpolation;
- finite-difference approximation of mixed derivatives;
- analytic coefficient-tail estimates;
- rank/nullspace and singular-value inverse criteria;
- higher-order linearization;
- Gaussian-beam localization; and
- nonlinear Lorentzian geometric and coefficient reconstruction.

Dynamic Unity may claim:

1. the exact distinction between finite joint-source provenance and
   interaction-event provenance;
2. the scoped context/acquisition cost of reducing an ideal mixed derivative
   to a Boolean packet;
3. the finite-amplitude-tail versus acquisition-error tradeoff inside the
   North-Star record contract;
4. the target-relative localization kernel condition as the next physical
   gate after source attribution; and
5. the supplied-versus-selected and no-refit collision between strong
   nonlinear inverse positives and a finite formed record.

This earns:

- **Grade 4, scoped:** a context/resource/identifiability boundary showing
  what finite nonlinear provenance cannot establish without a localization
  interface;
- **Grade 3, conditional:** exact finite source-provenance and
  target-localization theorems under a frozen response class and full-rank
  packet; and
- **not Grade 5:** no physical remainder, novel law, empirical prediction, or
  source-selected record has been established.

This is not yet a standalone blockbuster. It is a decisive narrowing of the
most promising constructive route.

## 10. Disposition

The previous candidate:

```text
target-independent physically formed short-range response relay net
+ uniform local margin
+ complete provenance
+ no-refit conformal transfer
```

is narrowed to:

```text
target-independent physically multiplexed nonlinear source packet
+ formed source-channel and interaction-event identities
+ finite context and readout family
+ common reset and complete attempt-level acquisition
+ source-to-event-to-readout provenance
+ target-relative localization rank
+ uniform positive quotient margin on a frozen compact class
+ no-refit held-out causal/conformal transfer
```

The nearest exact positive is the 16-context four-source Möbius certificate.
It proves that finite nonlinear source attribution is possible under a
bounded-order or analytic-tail contract.

The nearest exact negative is equally important. Source attribution does not
identify the interaction event. An aggregate readout can give identical
records for different interaction-site distributions.

The highest-information reopener is therefore:

> Fix one physically admissible compact or finite-complexity Lorentzian class
> and ask whether a target-independent finite source/readout packet—chosen
> before the held-out geometry—has a uniform positive localization margin for
> the nonlinear interaction target used by an existing stability theorem.

A positive would close the finite-interface bridge far more sharply than
another response hierarchy. A negative would identify the smallest
geometry-dependent interface that cannot be removed.

No inspected result yet selects that packet, so Dynamic Unity remains
quiescent with no ready successor.

## 11. Exact regression

`tests/du_nonlinear_interaction_provenance_localization_probe.py` preserves:

- exact four-source Möbius recovery from 16 Boolean contexts;
- the omitted-vertex witness for every Boolean context;
- the sharp factor-16 context-error amplification before amplitude division;
- linear finite-amplitude contamination from one fifth-order term;
- same aggregate record for two different site distributions; and
- repair by a full-rank two-readout packet.

The regression is proportional. It establishes no physical nonlinear field,
selected source interface, repeatability, formed interaction record, event
localization, finite QFT acquisition, geometry reconstruction, new physics,
or prediction.
