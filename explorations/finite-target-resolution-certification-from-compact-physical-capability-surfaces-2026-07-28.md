---
title: "Finite target-resolution certification from compact physical capability surfaces"
status: completed_scoped_reduction_theorem_counterexample_and_active_wave_boundary
doc_type: finite_certificate_reduction_theorem_and_physical_selection_boundary
created: 2026-07-28
work_id: CCR-FINITE-CERTIFIED-ACTIVE-WAVE-REDUCTION-GATE
claim_id: HC-DU-095
run_id: RUN-20260728-194138-finite-certified-active-wave-reduction
lanes:
  - lane_1
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
claim_grade: "GRADE 4 SCOPED POINTWISE-SEPARATION-TO-FINITE-CERTIFICATE NONIMPLICATION WITHOUT COMPACTNESS AND ONE-EXPERIMENT/FINITE-RECORD NONIDENTIFICATION; CONDITIONAL GRADE 3 FINITE ROBUST TARGET-RESOLUTION CERTIFICATE UNDER COMPACTNESS, CONTINUITY, PHYSICAL TARGET SEPARATION, AND ERROR MARGIN; FINITE-MEASUREMENT INVERSE PROBLEMS, COMPACTNESS, OBSERVABILITY, AND EXPERIMENTAL DESIGN ABSORB THE COMPONENTS; NO PHYSICALLY SELECTED COMPACT CLASS, CANONICAL PROBE FAMILY, CONSTRUCTIVE SOURCE DESIGN, COMPLETE ACQUISITION, EXACT CONTINUUM GEOMETRY, NEW PHYSICS, GRADE-5 REMAINDER, PREDICTION, OR PAPER PROMOTION"
decision: FINITE_REDUCTION_EXISTS_CONDITIONALLY_BUT_PHYSICAL_PREMISES_REMAIN_UNSELECTED
---

# Finite certification from a physical capability surface

## Executive result

`HC-DU-094` left a precise gap. Nonlinear-wave inverse theorems can
reconstruct causal and conformal geometry from an ideal source-to-solution
operator, but that operator ranges over a continuum of possible sources and
responses. It is not one finite certified record.

This swing proves that the continuum-to-finite step is possible under exact
conditions.

> If the admissible physical completion class is compact, the held-out target
> is continuous, and a continuous physically realizable measurement family
> separates every pair of completions that differ by at least the declared
> target resolution, then finitely many measurements already separate all
> such pairs with one positive uniform margin.

If each retained measurement has total error less than half that margin, any
two completions compatible with the same finite record have target distance
strictly below the declared resolution. Compact measurement ranges can then
be quantized, so the certificate can be finite-bit.

This is a real positive. It corrects an overly strong reading of the previous
boundary:

```text
ideal continuum response operator
  does not imply
irreducibly infinite experimental record
```

The correct ladder is:

```text
target-separating capability surface
  + compact physical completion class
  + continuous physically realizable readouts
  + fixed target resolution
  -> finite robust measurement subfamily
  + joint / sequential campaign realizability on the same completion
  + calibrated error below its margin
  -> finite target-sufficient record.
```

The compactness premise is load-bearing. A bounded noncompact family can be
pointwise separated by an infinite measurement family while every finite
subfamily leaves target-distinct completions identical.

The literature also exposes a terminology trap. “One measurement,” “one
source,” or “one observation point” can still carry infinite operational
content:

- one pseudorandom source can contain a countably infinite dense family of
  point sources;
- one returned wave can be observed over a continuum of boundary locations
  and times;
- one white-noise realization can be processed through infinite-time or
  vanishing-scale limits; and
- one timelike curve can receive the full source-to-solution map for a
  continuum of source functions.

Experiment count is therefore not record dimension, precision, duration, or
bit count.

The theorem does not yet activate the active-wave route. Existing Lorentzian
geometry reconstruction results do not also prove:

- compactness of a physically selected spacetime class in the target
  topology;
- uniform continuity or stability of the geometry reconstruction on that
  class;
- target separation by a bounded QFT-realizable source/readout family;
- a constructive finite probe set with manageable margin and resources;
- complete attempted-process acquisition and archive formation; or
- no-refit transfer to a held-out target.

Returned states:

```text
FINITE_TARGET_RESOLUTION_CERTIFICATE
+ POSITIVE_UNIFORM_SEPARATION_MARGIN
+ COMPACTNESS_PERFORMS_FINITE_REDUCTION
+ NONCOMPACT_POINTWISE_SEPARATION_FAILURE
+ BOUNDEDNESS_IS_NOT_COMPACTNESS
+ ONE_EXPERIMENT_NOT_FINITE_RECORD
+ FINITE_DIMENSIONAL_MODEL_CLASS_ABSORBER
+ PHYSICAL_REALIZABILITY_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

## 1. Frozen typed contract

Let:

- \(\Theta\) be an independently fixed admissible physical completion class;
- \(T:\Theta\rightarrow Z\) be the held-out target, where
  \((Z,d_Z)\) is a metric space;
- \(\mathcal M\) be a frozen family of continuous real-valued individually
  realizable measurement functionals \(m:\Theta\rightarrow\mathbb R\);
- \(\delta>0\) be the declared target resolution; and
- \(\eta\geq0\) be the total per-coordinate acquisition, calibration,
  quantization, and retention error.

For a finite family \(F=\{m_1,\ldots,m_N\}\subset\mathcal M\), define its
record map

\[
R_F(\theta)
=
\big(m_1(\theta),\ldots,m_N(\theta)\big).
\]

The full physical measurement family is **target separating** when

\[
T(\theta)\neq T(\theta')
\quad\Longrightarrow\quad
\exists m\in\mathcal M:
m(\theta)\neq m(\theta').
\]

At resolution \(\delta\), only pairs in

\[
K_\delta
=
\left\{
(\theta,\theta')\in\Theta^2:
d_Z\big(T(\theta),T(\theta')\big)\geq\delta
\right\}
\]

must be separated.

This is target-relative sufficiency. It does not say the record reconstructs
the whole completion or every possible target.

It also does not assume that every finite subset of \(\mathcal M\) is jointly
executable. The theorem first selects a finite mathematical subfamily.
Turning it into one physical campaign additionally requires joint
compatibility or repeatable preparations, controlled disturbance and reset,
and a joined complete-attempt archive.

## 2. Theorem — compact capability surfaces admit finite robust certificates

### Theorem

Assume:

1. \(\Theta\) is compact;
2. \(T\) is continuous;
3. every \(m\in\mathcal M\) is continuous; and
4. \(\mathcal M\) separates every pair in \(K_\delta\); and
5. \(K_\delta\) is nonempty.

Then there are finitely many measurements

\[
F_\delta=\{m_1,\ldots,m_N\}\subset\mathcal M
\]

and a margin \(\gamma_\delta>0\) such that

\[
d_Z\big(T(\theta),T(\theta')\big)\geq\delta
\quad\Longrightarrow\quad
\max_{1\leq i\leq N}
\left|m_i(\theta)-m_i(\theta')\right|
\geq\gamma_\delta.
\]

### Proof

Continuity of \(T\) makes \(K_\delta\) closed in
\(\Theta\times\Theta\). Compactness of \(\Theta\) therefore makes
\(K_\delta\) compact.

For each \(m\in\mathcal M\), define

\[
U_m
=
\left\{
(\theta,\theta')\in K_\delta:
m(\theta)\neq m(\theta')
\right\}.
\]

Continuity makes \(U_m\) open in \(K_\delta\). Target separation makes
\(\{U_m:m\in\mathcal M\}\) an open cover of \(K_\delta\). Compactness gives a
finite subcover \(U_{m_1},\ldots,U_{m_N}\).

Define

\[
G(\theta,\theta')
=
\max_{1\leq i\leq N}
\left|m_i(\theta)-m_i(\theta')\right|.
\]

The function \(G\) is continuous and strictly positive on compact
\(K_\delta\). It therefore attains a positive minimum

\[
\gamma_\delta
=
\min_{K_\delta}G
>0.
\]

This is the required margin. \(\square\)

If \(K_\delta\) is empty, the target already has diameter below \(\delta\)
and the empty measurement packet is sufficient; no positive separation
margin is needed.

### What performed the work

The theorem does not manufacture information. Its premises do distinct jobs:

```text
physical measurement family
  -> which distinctions can be probed

target separation
  -> no target-relevant distinction is silent to every probe

compact physical class
  -> one finite probe subfamily covers all target-relevant pairs

continuity
  -> the finite cover has a positive uniform margin

declared delta
  -> exact continuum identity is not demanded.
```

## 3. Corollary — finite noisy records suffice

Assume the selected finite family can be executed as one valid campaign on
the same completion—or on repeatable preparations governed by the same
completion—and its results can be joined without selection loss.

Suppose a retained record \(q=(q_1,\ldots,q_N)\) obeys

\[
\left|q_i-m_i(\theta)\right|\leq\eta
\]

for every coordinate and the actual completion \(\theta\).

If two completions \(\theta,\theta'\) are both compatible with the same
record, then

\[
\left|m_i(\theta)-m_i(\theta')\right|
\leq2\eta
\]

for all \(i\). Therefore, if

\[
2\eta<\gamma_\delta,
\]

they cannot belong to \(K_\delta\). Every nonempty record fibre has

\[
\operatorname{diam}_T
\left\{
\theta:
\left|q_i-m_i(\theta)\right|\leq\eta
\ \forall i
\right\}
<\delta.
\]

Because every continuous \(m_i\) has compact range on \(\Theta\), each range
can be covered by finitely many bins at any fixed error scale. Thus the
record can be represented with finitely many bits.

This is a finite target-resolution certificate. It is not exact continuum
reconstruction and provides no efficient bound on:

- \(N\);
- \(\gamma_\delta^{-1}\);
- required energy or source amplitude;
- observation duration;
- detector bandwidth;
- numerical conditioning; or
- total archive bits.

Compactness proves existence, not practicality.

### Metric-entropy lower bound

Let \(P_\delta(T(\Theta))\) be the packing number: the supremum of
cardinalities of target subsets whose pairwise distances are at least
\(\delta\). If a discrete record alphabet \(\mathcal Q\) has every record
fibre of target diameter below \(\delta\), then

\[
|\mathcal Q|
\geq
P_\delta(T(\Theta)).
\]

Indeed, two members of a \(\delta\)-separated target set cannot share one
record code. Therefore a \(B\)-bit archive must satisfy

\[
B
\geq
\left\lceil
\log_2 P_\delta(T(\Theta))
\right\rceil.
\]

This is an exact information lower bound. It is absorbed by packing,
rate-distortion, and metric-entropy reasoning, but it supplies the correct DU
resource coordinate:

> Finite-resolution reconstruction cost is controlled by the number of
> physically admitted target possibilities at that resolution, not by the
> mere fact that the underlying theory uses continuum variables.

Compactness of \(T(\Theta)\) makes the packing number finite for every fixed
positive resolution. As \(\delta\rightarrow0\), the packing number and
required bits may diverge.

## 4. Exact counterexample — pointwise separation need not finite-reduce

Let

\[
\Theta=\{e_n:n\in\mathbb N\}\subset\ell^2,
\]

where \(e_n\) is the \(n\)-th standard basis vector. This class is bounded:

\[
\|e_n\|_2=1.
\]

It is not norm compact because

\[
\|e_n-e_k\|_2=\sqrt2
\]

for all \(n\neq k\).

Let \(T:\Theta\rightarrow\Theta\) be the identity with the norm metric, and
let

\[
m_j(e_n)=\langle e_j,e_n\rangle=\delta_{jn}.
\]

Every \(m_j\) is a bounded linear measurement and the full family
\(\{m_j:j\in\mathbb N\}\) separates every pair.

For any finite subset \(m_1,\ldots,m_N\), choose distinct \(n,k>N\). Then

\[
m_i(e_n)=m_i(e_k)=0
\]

for every retained coordinate, while

\[
\|T(e_n)-T(e_k)\|_2=\sqrt2.
\]

No finite subfamily certifies any target resolution
\(\delta\leq\sqrt2\).

### Boundary

This proves:

```text
bounded class
  + continuous pointwise-separating measurement family
  != finite robust certificate.
```

It does not prove compactness is the only possible sufficient premise.
Metric-entropy bounds, finite-dimensionality, sparsity, analyticity,
bandlimiting, coercive regularization, or a directly constructed uniform
finite separator can perform equivalent work.

### Topology warning

If \(0\) is added and the class is given the weak topology, the sequence
\(e_n\) converges weakly to \(0\), and the enlarged set is weakly compact.
The coordinate measurements remain weakly continuous. But the norm-metric
target is not continuous in that topology.

Thus “compact” is incomplete unless the topology is declared and makes the
target continuous. A weakly compact energy-bounded class does not certify a
strong geometric target merely by changing topology.

## 5. Why “one measurement” can still be infinite data

### One pseudorandom source

Helin, Lassas, and Oksanen's
[one-measurement pseudorandom-noise inverse
problem](https://arxiv.org/abs/1011.2527) uses one named source

\[
f(t,x)
=
\sum_{j=1}^{\infty}
a_j\delta_{x_j}(x)\delta(t),
\]

where the \(x_j\) form a dense boundary set and the amplitudes encode source
identity. The returned solution is observed on
\(\mathbb R\times\partial M\).

This is one source invocation, but it contains:

- countably infinitely many source locations;
- infinitely structured amplitudes;
- a continuum boundary response; and
- a continuum time trace.

It is not one finite source vector or finite-bit record.

### One white-noise realization

Helin, Lassas, and Oksanen's
[white-noise-source inverse problem](https://arxiv.org/abs/1308.4879)
uses one random-source realization and the complete response on
\(\mathbb R_+\times\partial M\). Its recovery proof uses time translations,
ergodic limits, a countable dense parameter set, and a vanishing beam-width
limit.

Again:

```text
one source realization
  != bounded duration
  != finite response samples
  != finite precision
  != finite retained archive.
```

### One timelike curve

Nursultanov, Oksanen, and Tzou's
[single-point Lorentzian result](https://arxiv.org/abs/2310.06925)
restricts the observation locus to one timelike curve. The input remains the
source-to-solution **map**, meaning a family of source functions and their
returned curve responses.

“Single point” narrows where responses are observed. It does not reduce the
source family, curve-time data, precision, or archive to one finite record.

### Terminology rule

Every future use of “single measurement” or “finite measurements” must type:

| Coordinate | Required question |
|---|---|
| experiment identity | How many invocations? |
| source family | How many independent controls or source degrees of freedom? |
| output carrier | Scalar, finite vector, field, boundary function, or time series? |
| duration | Finite interval or asymptotic/infinite limit? |
| precision | Exact real/field value or calibrated finite resolution? |
| acquisition | Are rejected, failed, and retried attempts retained? |
| archive | How many durable bits are certified? |

## 6. Finite-measurement inverse-problem collision

Alberti and Santacesaria prove
[finite-measurement Calderón
reconstruction](https://arxiv.org/abs/1803.04224) for an unknown potential
belonging to a known finite-dimensional subspace. They obtain global
uniqueness, Lipschitz stability, and a convergent reconstruction scheme; the
number of measurements depends on the subspace dimension and the stability
constant deteriorates rapidly with that dimension.

Their later
[general framework](https://arxiv.org/abs/1906.10028) shows that broad
inverse problems with full-data Lipschitz stability can retain stability
under finite-dimensional measurement approximation when the unknown lies in
a finite-dimensional subspace.

These are strong absorbers for the positive shape:

```text
full response map
  + restricted model class
  + stability
  -> finite measurement reconstruction.
```

They also reinforce Dynamic Unity's typing:

- the model class is supplied or independently justified;
- a finite number of boundary excitations may still return boundary
  functions rather than finitely many noisy bits;
- exact real-valued data are not physical archives;
- uniqueness does not select the instrument;
- stability constants and measurement counts are part of capability; and
- a theorem for potentials or conductivities does not automatically transfer
  to unknown Lorentzian geometry.

The abstract compactness theorem above is therefore not claimed as new
inverse-problem mathematics. Its project value is to identify the exact
finite-certificate contract and the premises a physical arena must earn.

## 7. Application to active-wave spacetime reconstruction

Let \(\Theta\) be a class of Lorentzian spacetimes modulo the declared gauge
or conformal equivalence. Let \(T\) be a finite-resolution causal or
conformal target. Let \(\mathcal M_{\rm phys}\) be the family of bounded
source/readout procedures physically realizable in the observer worldtube.

The finite-certificate theorem applies if:

1. \(\Theta\) is compact in a topology in which \(T\) is continuous;
2. each admitted source/readout statistic is continuous in that topology;
3. \(\mathcal M_{\rm phys}\) separates every pair whose target distance is at
   least \(\delta\); and
4. the retained total error satisfies \(2\eta<\gamma_\delta\).

Published nonlinear-wave uniqueness theorems establish an important part of
item 3 for an ideal source-to-solution operator under their own spacetime,
field-equation, regularity, source, and observation contracts.

They do not by themselves establish items 1, 2, or 4 for a physically formed
finite packet. Nor do they prove that the separating scalar functionals
chosen by the compactness proof correspond to bounded QFT-realizable
operations or form a compatible repeated-source campaign.

### Target dependence

The finite subcover may depend on the declared target map \(T\) and
resolution \(\delta\). That is legitimate pre-registered experimental design
when \(T\) is a task fixed before data acquisition. It is not an endogenous
universal record selector.

The full admissible family \(\mathcal M_{\rm phys}\) must be physically fixed
without defining a readout to return \(T\) itself. Otherwise
\(m(\theta)=T(\theta)\) makes the theorem circular. Target knowledge may
select among independently available probes; it may not create a
target-coded probe or completion class.

Dynamic Unity's stronger no-refit result would require either:

- a packet physically selected independently of the held-out target and
  shown sufficient afterward; or
- one packet designed on a training target family and transferred unchanged
  to a genuinely held-out target.

The theorem may not be used to choose new probes after observing the true
completion or failed reconstruction.

## 8. Exact North-Star update

The minimum active-reconstruction ladder is now:

```text
one actual history
  < one complete process
  < a physically realizable capability family
  < target separation by that family
  < compact / finite-complexity physical completion class
  < finite robust separating subfamily at resolution delta
  < jointly executable or repeatably preparable campaign
  < complete retained acquisition below margin gamma_delta / 2
  < finite target-sufficient certified record
  < no-refit transfer
  < exact continuum reconstruction, if a controlled delta -> 0 limit exists.
```

This changes one priority judgment:

> The active-wave route is not blocked in principle by the continuum size of
> the published response operator. It is blocked by the absence of a
> physically selected compact class, a physically realizable uniformly
> separating family, a constructive margin/resource bound, and formed
> acquisition.

The next useful search should therefore not ask merely for “fewer
measurements.” It should ask which physical law supplies compactness or
finite metric entropy in the target topology and whether the admitted
observer operations retain uniform target separation on that class.

## 9. Grade, disposition, and reopener

### Earned

Scoped Grade 4:

- pointwise target separation does not imply any finite certificate without
  compactness, total boundedness, finite complexity, or a direct uniform
  separator;
- boundedness alone is insufficient;
- one named experiment does not identify finite record dimension; and
- weak compactness does not control a strong target unless the target is
  continuous in that topology.

Conditional Grade 3:

- compactness plus continuous physical target separation yields a finite
  robust target-resolution certificate;
- calibrated total error below half the uniform margin makes every record
  fibre target-small; and
- compact ranges allow finite-bit quantization.

### Not earned

- a physically selected compact Lorentzian completion class;
- a natural or canonical finite probe set;
- a constructive bound on probe count, margin, resource, or bits;
- QFT realization of the separating measurements;
- joint or repeatable campaign realizability without changing the completion;
- complete attempted-process visibility;
- exact continuum geometry;
- no-refit transfer;
- a physical remainder or prediction;
- new inverse-problem mathematics; or
- paper promotion.

### Successor disposition

The active-wave candidate is sharper but still not ready. Dynamic Unity
remains quiescent.

### Exact reopener

Reopen with one physical arena that supplies, before held-out evaluation:

1. a field equation and observer/source boundary;
2. a physically selected compact or quantitatively totally bounded
   completion class modulo gauge in the target topology;
3. a bounded physically realizable measurement family;
4. a proof that this family uniformly separates the declared target quotient;
5. a constructive finite probe subset and positive margin;
6. a joint-execution or repeatable-preparation and reset contract preserving
   the same completion across the packet;
7. complete attempted-process acquisition, calibration, and retention with
   total error below half the margin;
8. an explicit resource and bit budget; and
9. a no-refit held-out target or a finite surviving remainder.

An exact-continuum claim additionally requires a controlled sequence
\(\delta\rightarrow0\) with resource scaling and a justified limiting
completion class.

## Resource disposition

Exact proof and primary-source collision decide the gate. A local numerical
inverse solver would only instantiate a selected finite-dimensional class and
could not select the physical class or measurements, so it fails the
local-model learning gate. External hardware is irrelevant until a
constructive finite physical packet exists. No paper, prediction,
publication, submission, provider, or contact action was authorized or
performed.
