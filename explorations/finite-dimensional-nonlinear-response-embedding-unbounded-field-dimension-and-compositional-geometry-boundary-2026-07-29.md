---
title: "Finite-dimensional nonlinear response embeddings, unbounded field dimension, and compositional geometry"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-106
work_id: CCR-FINITE-DIMENSIONAL-NONLINEAR-PACKET-GATE
run_id: RUN-20260729-062352-finite-dimensional-nonlinear-packet-gate
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
maximum_grade: "Grade 4 scoped model-dimension and exact-finite-packet necessity boundary; conditional Grade 3 no-refit finite response-embedding theorem"
---

# Finite-dimensional nonlinear response embeddings, unbounded field dimension, and compositional geometry

## Executive result

The swing returned:

```text
POINT_AND_TANGENT_COMPLETE_COMPACT_MODEL_ADMITS_A_FINITE_EXACT_PACKET
+ FINITE_PACKET_CAN_BE_FIXED_BEFORE_THE_HELD_OUT_MODEL
+ COMPACT_C1_EMBEDDING_HAS_A_POSITIVE_GLOBAL_INVERSE_MARGIN
+ EXACT_LOCAL_RECONSTRUCTION_NEEDS_AT_LEAST_TARGET_DIMENSION_SCALARS
+ UNBOUNDED_TARGET_DIMENSION_KILLS_EVERY_FIXED_FINITE_CONTINUOUS_PACKET
+ COMPACTNESS_REPAIRS_FIXED_RESOLUTION_NOT_EXACT_CONTINUUM_IDENTITY
+ FINITE_SCALAR_PACKET_IS_NOT_FINITE_BIT_RECORD
+ SOURCE_CONFIGURATION_COUNT_AND_RESPONSE_DIMENSION_ARE_DISTINCT_RESOURCES
+ FINITE_EVENT_LOCALIZATION_CAN_COMPOSE_INTO_A_GROWING_GEOMETRY_RECORD
+ MODEL_CLASS_AND_PHYSICAL_PACKET_SELECTION_REMAIN_UNEARNED
+ NO_READY_SUCCESSOR
```

`HC-DU-105` reduced one \(k\)-way nonlinear coefficient to a finite
counterfactual source packet and showed that source provenance does not
identify the interaction site. This swing decides when a fixed finite
readout family can close that localization gap.

There are three different regimes.

| Target class | What finite measurements can earn |
|---|---|
| Compact target at fixed resolution \(\delta>0\) | `HC-DU-095` already gives some finite robust packet when the full admitted measurement family separates every \(\delta\)-distinct pair |
| Compact finite-dimensional \(C^1\) model manifold | Point separation plus tangent separation by the full physical response family gives one finite exact no-refit response embedding with a positive inverse margin |
| Unrestricted field or metric class with unbounded target dimension | No fixed finite continuous scalar packet can be exactly injective, even when the class is compact in a weaker topology |

The finite-dimensional positive is exact. Let \(\Theta\) be a compact
\(C^1\) model manifold and let \(\mathcal M\) be the full family of admitted
scalar nonlinear-response measurements. If:

1. every two distinct models differ on some \(m\in\mathcal M\); and
2. every nonzero tangent direction changes some \(m\in\mathcal M\),

then a finite subfamily

\[
F=(m_1,\ldots,m_N):\Theta\longrightarrow\mathbb R^N
\]

is a \(C^1\) embedding. The packet is selected once from the whole model
class before the held-out member is known. Compactness and tangent
completeness also give a constant \(c>0\) such that

\[
\|F(\theta)-F(\theta')\|
\ge
c\,d_\Theta(\theta,\theta').
\tag{1}
\]

This is a genuine no-refit mathematical reconstruction theorem.

The exact negative is equally sharp. A continuous exact packet for a
\(d\)-parameter open target region needs at least \(d\) scalar coordinates.
More generally, if a target class contains target-distinct spheres of
arbitrarily high dimension, Borsuk--Ulam defeats every fixed finite packet.
A regularity-bounded field or gauge-fixed Lorentzian metric class contains
arbitrarily many independent small perturbation directions. Therefore no
fixed finite continuous scalar packet exactly reconstructs its full
continuum target.

This does not reverse the program's recent progress. It corrects the object
being requested:

> A finite packet should localize one formed event or one physically selected
> finite-dimensional model sector. A growing network of those finite records
> can then carry progressively richer causal and geometric structure. One
> fixed packet should not be expected to encode an unrestricted continuum
> field exactly.

For a four-source nonlinear interaction, the 16 Boolean source settings from
`HC-DU-105` and the response dimension \(N\) are separate resources. If the
same four-source contexts return \(N\) simultaneous readout channels, there
are still 16 source configurations but \(16N\) retained scalar values. If
each response coordinate requires a different quartet, the configuration
burden can instead grow toward \(16N\). The architecture and acquisition
contract determine which count applies.

No external hardware or PDE simulation is needed for this decision. The live
uncertainty is now whether a physical arena selects a finite-dimensional
formed-event target and a point-and-tangent-complete response family.

## 1. What “finite packet” means

Three notions that are often collapsed must remain distinct.

### Finite coordinate packet

A map

\[
F:\Theta\longrightarrow\mathbb R^N
\]

has finitely many scalar coordinates.

### Finite-precision packet

Each coordinate is retained only to a declared error or quantization scale.
This gives a finite alphabet when the response range is bounded.

### Finite-bit record

The complete retained packet has a finite number of possible codewords.

An exact real-valued coordinate generally contains unbounded precision. Thus
the finite exact embedding theorem below is not by itself a finite-bit
physical record theorem. Its inverse margin converts finite coordinate error
into finite target error; `HC-DU-095` and target packing then govern
quantization and bit cost.

This is the correct relationship:

```text
finite exact response embedding
  + positive inverse margin
  + bounded response range
  + calibrated finite precision
  -> finite-resolution finite-bit target certificate
```

## 2. Frozen response-manifold contract

Let:

- \((\Theta,d_\Theta)\) be a compact \(C^1\) manifold with a fixed
  Riemannian metric;
- \(\mathcal M\subset C^1(\Theta,\mathbb R)\) be the frozen family of
  scalar physically admitted measurements;
- \(U\Theta\) be the unit tangent bundle;
- \(R_\mathcal M(\theta)\) denote the full response surface
  \(m\mapsto m(\theta)\); and
- \(F_A(\theta)=(m(\theta))_{m\in A}\) for a finite
  \(A\subset\mathcal M\).

The family is **point complete** when

\[
\theta\ne\theta'
\quad\Longrightarrow\quad
\exists m\in\mathcal M:
m(\theta)\ne m(\theta').
\tag{2}
\]

It is **tangent complete** when

\[
v\in T_\theta\Theta,\ v\ne0
\quad\Longrightarrow\quad
\exists m\in\mathcal M:
d m_\theta(v)\ne0.
\tag{3}
\]

Point completeness is the differential-geometric version of the full
operator being injective. Tangent completeness rules out an infinitesimal
target direction that is silent to every admitted response.

These are properties of the declared response family. Neither property
selects that family physically.

## 3. Finite exact no-refit response-embedding theorem

### Theorem 1

If \(\Theta\) is compact and \(\mathcal M\) is point complete and tangent
complete, then there is a finite subfamily

\[
A=\{m_1,\ldots,m_N\}\subset\mathcal M
\]

such that

\[
F_A:\Theta\longrightarrow\mathbb R^N
\]

is a \(C^1\) embedding.

The set \(A\) is fixed for the whole model class; it does not depend on the
held-out \(\theta\).

### Proof

For each \(m\in\mathcal M\), define

\[
V_m
=
\left\{
(\theta,v)\in U\Theta:
d m_\theta(v)\ne0
\right\}.
\]

The sets \(V_m\) are open. Tangent completeness makes them an open cover of
the compact unit tangent bundle. Choose a finite subcover

\[
V_{m_1},\ldots,V_{m_r}.
\]

The combined map

\[
F_0=(m_1,\ldots,m_r)
\]

has injective derivative at every point, so it is an immersion. By the local
embedding theorem, every \(\theta\in\Theta\) has a neighborhood on which
\(F_0\) is injective. Compactness gives a uniform neighborhood of the
diagonal

\[
\mathcal N\subset\Theta\times\Theta
\]

such that distinct \((\theta,\theta')\in\mathcal N\) are separated by
\(F_0\).

The complement

\[
K=(\Theta\times\Theta)\setminus\mathcal N
\]

is compact and contains no diagonal point. For every
\((\theta,\theta')\in K\), point completeness supplies some
\(m\in\mathcal M\) with
\(m(\theta)\ne m(\theta')\). The corresponding separation sets are an open
cover of \(K\). Select a finite subcover

\[
m_{r+1},\ldots,m_N.
\]

Then \(F_A=(m_1,\ldots,m_N)\) is injective and has injective derivative.
An injective immersion from a compact manifold into a Hausdorff space is an
embedding. \(\square\)

### What the theorem adds to `HC-DU-095`

`HC-DU-095` works at a declared target resolution \(\delta>0\). The
target-distinct pair set is then compact because it stays away from the
diagonal.

Exact reconstruction sets \(\delta=0\). The off-diagonal pair space need not
be compact; arbitrarily close pairs approach the diagonal. Tangent
completeness is the additional condition that controls this missing region.

Thus:

```text
point separation + compactness
  -> finite packet at every fixed target resolution

point separation + tangent separation + compact finite-dimensional manifold
  -> one finite exact packet.
```

## 4. Uniform inverse-margin corollary

### Corollary 1

Under the assumptions of Theorem 1, the finite packet may be chosen so that
there is a constant \(c>0\) satisfying (1).

### Proof boundary

The finite tangent subcover gives a positive minimum derivative gain on the
compact unit tangent bundle:

\[
\lambda
=
\min_{(\theta,v)\in U\Theta}
\|dF_A{}_\theta(v)\|
>0.
\]

In finitely many coordinate charts, uniform continuity of \(dF_A\) gives,
for sufficiently close pairs,

\[
\|F_A(\theta)-F_A(\theta')\|
\ge
\frac{\lambda}{2}d_\Theta(\theta,\theta').
\]

For pairs outside that common neighborhood, injectivity and compactness give
a positive minimum of

\[
\frac{\|F_A(\theta)-F_A(\theta')\|}
     {d_\Theta(\theta,\theta')}.
\]

The smaller of the local and nonlocal constants is \(c\). \(\square\)

If every retained coordinate has error at most \(\varepsilon\), then two
models compatible with the same measured packet satisfy

\[
d_\Theta(\theta,\theta')
\le
\frac{2\sqrt N\,\varepsilon}{c}
\tag{4}
\]

for Euclidean packet norm. This is the explicit handoff from an exact
real-coordinate embedding to a finite-precision physical certificate.

The theorem gives no numerical \(N\) or \(c\). A physical response family can
be point/tangent complete but extremely inefficient.

## 5. Exact target-dimension lower bound

### Theorem 2

Suppose the target class contains an open subset of
\(\mathbb R^d\), and let

\[
F:\Theta\longrightarrow\mathbb R^N
\]

be continuous and injective on that subset. Then

\[
N\ge d.
\tag{5}
\]

### Proof

Assume \(N<d\). Compose \(F\) with the coordinate inclusion

\[
\mathbb R^N\hookrightarrow\mathbb R^d.
\]

This would give a continuous injective map from an open subset of
\(\mathbb R^d\) into \(\mathbb R^d\) whose image lies in a proper linear
subspace. Invariance of domain says the image must be open, while a proper
linear subspace has empty interior. Contradiction. \(\square\)

This is a coordinate-count lower bound, not an experiment-count lower bound.
One physical context may return many scalar response coordinates
simultaneously.

### Event-location specialization

A generic event location in a four-dimensional spacetime is locally a
four-parameter target. Any continuous exact localization packet therefore
needs at least four independent real response coordinates.

The abstract Whitney theorem says a smooth \(d\)-manifold admits an embedding
in \(\mathbb R^{2d+1}\), so nine generic mathematical coordinates are a
universal upper bound for an abstract four-dimensional event manifold.
Those coordinates need not belong to the physically realizable nonlinear
response family. Theorem 1 is more physically relevant because it selects a
finite subfamily from the admitted responses, but it gives no universal
count.

## 6. Unbounded-dimensional exact-packet obstruction

### Theorem 3 — spherical-dimension obstruction

Suppose that for every \(N\ge1\), the admissible completion class contains a
continuous subfamily

\[
\iota_N:S^N\longrightarrow\Theta
\]

such that

\[
T(\iota_N(x))
\ne
T(\iota_N(-x))
\quad
\text{for every }x\in S^N.
\tag{6}
\]

Then no fixed finite continuous scalar packet exactly reconstructs \(T\).

### Proof

Let \(F:\Theta\to\mathbb R^N\) be any \(N\)-scalar continuous packet.
Borsuk--Ulam gives a point \(x\in S^N\) such that

\[
F(\iota_N(x))
=
F(\iota_N(-x)).
\]

Equation (6) says their targets differ. Therefore \(F\) is not
target-sufficient. This holds for every finite \(N\). \(\square\)

### Lorentzian and field-class specialization

The Lorentzian-signature condition is open under sufficiently small
\(C^0\) metric perturbations. Fix:

- a background Lorentzian metric \(g_0\);
- a declared gauge slice;
- \(N+1\) linearly independent smooth compactly supported perturbations
  \(h_0,\ldots,h_N\) inside that slice; and
- a sufficiently small amplitude \(\delta>0\).

Then

\[
g_a
=
g_0+\delta\sum_{j=0}^{N}a_jh_j,
\qquad
a\in S^N,
\tag{7}
\]

remains Lorentzian. If the perturbations are target-distinct modulo the
declared gauge and equivalence, antipodal points have different targets.

For conformal geometry, use target-distinct trace-free/gauge-fixed
perturbations rather than pure conformal rescalings. For a scalar coefficient
target, use

\[
q_a=q_0+\delta\sum_j a_j\phi_j.
\]

A regularity-bounded infinite-dimensional class contains such
finite-dimensional spheres for arbitrary \(N\). It may simultaneously be
compact in a weaker target topology by the `HC-DU-096` regularity gap. The
spherical obstruction still applies to exact full-target reconstruction.

Therefore:

> Compactness does not make an infinite-dimensional continuum target exactly
> finite-coordinate. It makes it finitely coverable at every nonzero
> resolution.

This is the exact version of the entropy and box-dimension warning in
`HC-DU-097`.

## 7. Nonlinear source contexts and response dimensions

For one scalar mixed-response coordinate \(m_j(\theta)\), the four-source
Boolean packet is

\[
m_j(\theta)
=
\eta^{-4}
\sum_{S\subseteq[4]}
(-1)^{4-|S|}
R_{j,\theta}(\eta\mathbf1_S)
\tag{8}
\]

under the bounded-degree idealization, with the `HC-DU-105` tail/error
correction otherwise.

For \(N\) scalar response coordinates, there are several architectures.

### Shared contexts, parallel readouts

One source quartet is run in 16 on/off contexts and every context returns an
\(N\)-vector:

```text
16 source configurations
16N retained scalar response values
N mixed-response coordinates.
```

### Distinct source quartets

Each response coordinate uses a separately positioned or shaped quartet:

```text
up to 16N source configurations
at least 16N retained scalar response values
N mixed-response coordinates.
```

Intermediate architectures can share some sources, contexts, or readouts.
The acquisition contract must state the actual factorization.

The dimension lower bound applies to \(N\), not automatically to the number
of source configurations. A four-dimensional event needs at least four
independent scalar response coordinates, but those may be read out in
parallel from the same 16 source settings.

The exact-arithmetic control in
`tests/du_finite_dimensional_nonlinear_packet_probe.py` recovers a
three-parameter target from 16 four-source contexts carrying three response
channels: 16 configurations and 48 scalar values. Replacing the full-rank
three-channel packet by two channels produces a same-packet/different-target
witness.

## 8. Collision with the strongest known results

The mathematical components are standard:

- point/tangent separation and compact-manifold embeddings;
- Whitney embedding and generic projection;
- invariance of domain;
- Borsuk--Ulam;
- finite-dimensional inverse-function stability;
- finite box dimension and stable embeddings;
- metric entropy and compressed sensing; and
- finite-rank observability.

`HC-DU-097` already collided the finite-dimensional escape with manifold
embedding, low-rank tomography, and Sobolev entropy. This result does not
repackage that escape as a new theorem. It adds the exact diagonal/tangent
condition and the unbounded-spherical-dimension no-go required by the
specific `HC-DU-105` finite nonlinear packet.

The physical inverse results remain strong:

- Kurylev, Lassas, and Uhlmann
  [reconstruct conformal Lorentzian structure](https://arxiv.org/abs/1405.3386)
  from a full local source-to-solution operator using nonlinear wave
  interactions.
- Lassas, Uhlmann, and Wang
  [prove the semilinear source-to-solution result](https://arxiv.org/abs/1606.06261).
- Lassas, Liimatainen, Potenciano-Machado, and Tyni
  [prove Hölder-stable coefficient recovery](https://arxiv.org/abs/2106.12257)
  from a full Dirichlet-to-Neumann map using higher-order linearization and
  Gaussian beams.

These establish point separation or stability for rich response operators in
their declared arenas. They do not jointly prove:

- physical selection of a compact finite-dimensional Lorentzian class;
- point and tangent completeness of one bounded scalar measurement family on
  that class;
- construction of the finite subfamily from physically executable sources
  and readouts;
- simultaneous or repeatable four-source contexts;
- complete attempt-level acquisition;
- source-to-interaction-to-readout record provenance; or
- no-refit transfer from localized events to a held-out geometry.

The surviving DU delta is therefore architectural and typed, not a new
embedding or inverse-wave theorem.

## 9. Compositional geometry is the viable class exit

The unbounded-dimension theorem rules out this default:

```text
one fixed finite packet
-> exact unrestricted continuum geometry.
```

It does not rule out:

```text
finite packet
-> one formed event location

many formed event packets
-> growing authenticated causal event network

network refinement
-> increasingly resolved regional causal/conformal geometry.
```

This is the mathematically disciplined version of the layered distributed
architecture that motivated the recent campaign.

Each local event target has bounded dimension and can, conditionally, admit a
finite exact response embedding. As more independent events or field modes
are admitted, the target dimension grows and so must retained response
capacity. For \(M\) unconstrained four-dimensional event locations, the
local parameter dimension is generically \(4M\) before quotienting known
relations, gauge, symmetries, or dynamics. A fixed response dimension cannot
remain exactly sufficient as \(M\to\infty\).

Physical laws can reduce this cost by:

- constraining which event configurations are admissible;
- supplying causal relations that remove independent degrees of freedom;
- selecting finite-dimensional attractors or effective sectors;
- permitting finite-resolution rather than exact reconstruction;
- making local records reusable across overlapping regional targets; or
- providing compositional consistency checks.

Those reductions must be derived and resource-accounted. They are not
granted by calling the record network distributed.

This changes the North-Star question from:

> Can one finite nonlinear packet reconstruct the full geometry?

to:

> Does physical dynamics form a growing family of finite,
> point-and-tangent-complete event records whose regional composition
> reconstructs geometry at the resolution and capability actually available
> to an observer?

The latter can remain exact at every finite event stage while allowing record
capacity to grow with physical complexity.

## 10. What the result does and does not say

### Earned

- **Conditional Grade 3:** a compact finite-dimensional model class with a
  point- and tangent-complete admitted response family has one finite exact
  no-refit response embedding and a positive inverse margin.
- **Scoped Grade 4:** exact continuous reconstruction needs response
  dimension at least the local target dimension.
- **Scoped Grade 4:** a target class containing target-distinct spheres of
  unbounded dimension admits no fixed finite continuous exact packet.
- **Scoped Grade 4:** compactness gives finite resolution but does not
  finite-coordinate an exact unrestricted continuum target.
- **Scoped Grade 4:** the viable fixed-finite target is a formed event or
  selected finite-complexity sector; full geometry must be compositional,
  growing, finite-resolution, or otherwise physically compressed.

### Not earned

- a physically selected finite-dimensional Lorentzian model class;
- a physically selected point/tangent-complete response family;
- a constructive finite nonlinear probe packet in QFT;
- a formed event identity, archive, observer, or access rule;
- finite-bit exact continuum reconstruction;
- a regional composition theorem from event packets to conformal geometry;
- no-refit transfer in a physical arena;
- new topology, embedding, inverse-problem, or QFT mathematics;
- a Grade-5 physical remainder or prediction;
- a paper promotion; or
- a ready successor.

## 11. Disposition

The `HC-DU-105` candidate:

```text
target-independent physically multiplexed nonlinear interaction packet
+ uniform localization margin
+ no-refit conformal transfer
```

is narrowed to:

```text
physically selected finite-dimensional formed-event target
+ physically realizable point-and-tangent-complete nonlinear response family
+ finite no-refit source/readout subfamily
+ repeatable or multiplexed four-source contexts
+ complete source-to-event-to-readout acquisition and provenance
+ positive inverse margin and finite-precision certificate
+ growing regional event-network composition
+ held-out causal/conformal transfer without interface refit.
```

The highest-information next candidate is now an event-localization theorem,
not another full-field finite-packet attempt:

> Freeze a compact four-dimensional interaction-event region and one
> physically realizable nonlinear response family. Test whether its scalar
> mixed responses separate every event pair and every event-location tangent
> direction without using the held-out event or geometry to choose the
> sources.

A positive finite subfamily would provide the first exact no-refit local
event packet. A negative tangent direction would identify the smallest
physical blind mode. Only after that result should DU attempt regional
composition into held-out geometry.

No inspected arena yet supplies the physically selected response family and
formation/acquisition contract, so Dynamic Unity remains quiescent with no
ready successor.

## 12. Regression boundary

`tests/du_finite_dimensional_nonlinear_packet_probe.py` preserves:

- exact three-parameter recovery from a full-rank three-channel mixed
  response packet;
- 16 source configurations versus 48 retained scalar values;
- the rank-three point/tangent-complete positive control; and
- a rank-two same-packet/different-three-parameter-target witness.

The regression is proportional. It establishes no Lorentzian metric,
nonlinear field, selected model class, physical source or readout, formed
event, record, geometry, new physics, prediction, or evidence grade.
