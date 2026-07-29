---
title: "Quantitative finite-probe construction, small-ball observability, and the Sobolev entropy boundary"
status: completed_scoped_quantitative_probe_theorem_resource_lower_bounds_and_infinite_dimension_boundary
doc_type: quantitative_finite_certificate_theorem_counterexamples_and_physical_observability_gate
created: 2026-07-28
work_id: CCR-QUANTITATIVE-FINITE-PROBE-PACKET-GATE
claim_id: HC-DU-097
run_id: RUN-20260728-204954-quantitative-finite-probe-packet-gate
lanes:
  - lane_1
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
claim_grade: "GRADE 4 SCOPED NO-UNIFORM-PACKET-SIZE, MARGIN, OR FIXED-FINITE-STABLE-EMBEDDING BOUNDARY FROM COMPACTNESS ALONE, WITH EXACT PROBE-FAMILY AND SOBOLEV-ENTROPY CONTROLS; CONDITIONAL GRADE 3 QUANTITATIVE FINITE-PACKET CONSTRUCTION UNDER A PHYSICALLY SELECTED UNIFORM SMALL-BALL OBSERVABILITY MODULUS, EFFECTIVE PAIR COVER, JOINT REALIZABILITY, AND CALIBRATED ACQUISITION; METRIC ENTROPY, RANDOM EMBEDDINGS, OBSERVABILITY, COMPRESSED SENSING, AND FINITE-DIMENSIONAL TOMOGRAPHY ABSORB THE COMPONENTS; NO PHYSICAL PROBE DISTRIBUTION, NEW PHYSICS, GRADE-5 REMAINDER, PREDICTION, PAPER, OR SUCCESSOR"
decision: COMPACTNESS_FINITE_REDUCES_BUT_PHYSICAL_OBSERVABILITY_AND_COMPLEXITY_CONTROL_DETERMINE_RESOURCE_VIABILITY
---

# Quantitative finite-probe packet gate

## Executive result

`HC-DU-095` proves that compactness turns pointwise target separation into
some finite robust measurement packet. `HC-DU-096` identifies a physical
regularity-gap route to that compactness. Neither result says whether the
packet is constructible or affordable.

This swing identifies the missing quantitative object:

> A physical probe family becomes finitely designable when target-distinct
> completion pairs have a uniform probability of producing a declared
> response gap under a physically fixed probe distribution.

Call this a **uniform small-ball observability modulus**:

\[
\nu
\left\{
m:
\left|m(\theta)-m(\theta')\right|
\geq a_\delta
\right\}
\geq p_\delta
\quad
\text{for every }(\theta,\theta')\in K_\delta.
\]

If the probes are uniformly Lipschitz and the target-distinct pair space has
a finite net of size \(Q_\delta\), then for \(0<p_\delta<1\),

\[
N
\geq
\frac{\log Q_\delta+\log(1/\alpha)}
     {-\log(1-p_\delta)}
\]

independent probes give, with probability at least \(1-\alpha\), one finite
packet with uniform response margin at least \(a_\delta/2\). Retained error
\(\eta<a_\delta/4\) then gives the `HC-DU-095` target-resolution certificate.
When \(p_\delta=1\), one sampled probe covers the finite net almost surely.

This is the clean constructive positive. It also reveals why compactness
alone was insufficient:

- it gives no sampling distribution \(\nu\);
- it gives no lower bound on \(p_\delta\);
- it gives no response scale \(a_\delta\);
- it gives no effective pair-space cover \(Q_\delta\);
- it gives no compatibility or repetition contract; and
- it gives no acquisition precision or source cost.

Two exact controls separate these resources:

1. a compact \(n\)-point class with only singleton-indicator probes requires
   \(n-1\) scalar coordinates although a rich binary code needs only
   \(\lceil\log_2n\rceil\) bits; and
2. multiplying a separating probe by arbitrary
   \(\varepsilon>0\) preserves topology and packet count while making its
   robust margin arbitrarily small.

The regularity route also has an important ceiling. The unit \(H^s\) ball on
a \(d\)-dimensional compact domain is compact in \(H^{s'}\), \(s'<s\), but
its metric entropy obeys, for \(r=s-s'\),

\[
\log P_\epsilon
\gtrsim
\epsilon^{-d/r}.
\]

It therefore has infinite box-counting dimension. A fixed finite-dimensional
bi-Hölder stable embedding is unavailable for the whole ball. At every fixed
resolution a finite packet exists; as resolution sharpens, the worst-case
record cost grows at least like \(\epsilon^{-d/r}\) bits.

Finite-dimensional manifolds, sparse/low-rank models, and finite-dimensional
attractors escape this ceiling. That is established mathematics, but the
restriction must be physically selected. It cannot be smuggled into the
completion class after the target is known.

No audited active-wave arena currently supplies the uniform physical
observability modulus, effective cover, joint probe campaign, and complete
acquisition. Dynamic Unity therefore remains quiescent.

Returned states:

```text
UNIFORM_SMALL_BALL_PROBE_BOUND
+ EFFECTIVE_NET_DETERMINISTIC_BOUND
+ TARGET_ENTROPY_RECORD_LOWER_BOUND
+ COMPACTNESS_WITH_ARBITRARILY_SMALL_MARGIN
+ RESTRICTED_PROBE_FAMILY_PACKET_INFLATION
+ SOBOLEV_COMPACT_CLASS_INFINITE_BOX_DIMENSION
+ FINITE_DIMENSIONAL_STRUCTURE_ABSORBER
+ PHYSICAL_OBSERVABILITY_MODULUS_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

## 1. Frozen quantitative contract

Let \((\Theta,d)\) be the compact physical completion class from
`HC-DU-095/096`. Let

\[
T:\Theta\rightarrow(Z,d_Z)
\]

be the held-out target and define

\[
K_\delta
=
\left\{
(\theta,\theta')\in\Theta^2:
d_Z(T\theta,T\theta')\geq\delta
\right\}.
\]

Give \(\Theta^2\) the pair metric

\[
d_2\big((\theta,\theta'),(x,x')\big)
=
d(\theta,x)+d(\theta',x').
\]

Let:

- \(\mathcal M\) be a target-independent physically admitted scalar probe
  family;
- \(\nu\) be a physical design probability measure on probes, or on
  compatible repeatable probe slots;
- \(L<\infty\) be a common Lipschitz bound:

  \[
  |m(\theta)-m(x)|\leq Ld(\theta,x);
  \]

- \(a_\delta>0\) be a declared physical response gap;
- \(p_\delta\in(0,1]\) be a uniform small-ball probability;
- \(\eta\) be total per-coordinate record error; and
- \(\alpha\in(0,1)\) be the allowed probe-design failure probability.

The design probability \(\alpha\) is not the experiment's theory-testing
error. It is the probability that a random packet fails to cover the frozen
target pair class before the experiment begins.

## 2. The quantitative random-packet theorem

### Theorem

Assume:

1. \(K_\delta\) is nonempty and compact;
2. every \(m\in\mathcal M\) is \(L\)-Lipschitz;
3. for all \((\theta,\theta')\in K_\delta\),

   \[
   \nu
   \left\{
   m:
   |m(\theta)-m(\theta')|\geq a_\delta
   \right\}
   \geq p_\delta;
   \]

4. \(Q_\delta\) is the covering number of \(K_\delta\) at pair radius

   \[
   \rho_\delta=\frac{a_\delta}{2L};
   \]

5. sampled probes can be executed jointly or on repeatable preparations
   governed by the same completion.

Draw \(N\) probes independently from \(\nu\). If
\(0<p_\delta<1\) and

\[
N
\geq
\frac{\log Q_\delta+\log(1/\alpha)}
     {-\log(1-p_\delta)},
\]

then with probability at least \(1-\alpha\), every pair in \(K_\delta\) is
separated by at least one sampled probe with margin \(a_\delta/2\).
If \(p_\delta=1\), one sampled probe covers every center in the finite net
almost surely, so the logarithmic formula is unnecessary.

### Proof

Choose a \(\rho_\delta\)-net

\[
\{c_1,\ldots,c_{Q_\delta}\}
\subset K_\delta.
\]

For a fixed center \(c_j=(\theta_j,\theta'_j)\), the probability that none of
the \(N\) sampled probes has response gap at least \(a_\delta\) is at most

\[
(1-p_\delta)^N.
\]

A union bound makes the probability that any net center is missed at most

\[
Q_\delta(1-p_\delta)^N
\leq\alpha.
\]

For a successful packet and any \(c\in K_\delta\), choose a net center
\(c_j\) with \(d_2(c,c_j)\leq\rho_\delta\). The score

\[
s_m(\theta,\theta')
=
|m(\theta)-m(\theta')|
\]

is \(L\)-Lipschitz in the pair metric. The probe separating \(c_j\) therefore
satisfies

\[
s_m(c)
\geq
a_\delta-L\rho_\delta
=
\frac{a_\delta}{2}.
\]

This holds for every pair in \(K_\delta\). \(\square\)

### Acquisition corollary

If each retained coordinate has total error

\[
\eta<\frac{a_\delta}{4},
\]

two completions compatible with the same record differ by less than
\(a_\delta/2\) in every selected response. They therefore cannot belong to
\(K_\delta\). Every compatible-record fibre has target diameter below
\(\delta\).

This is exactly the `HC-DU-095` certificate with a constructive random packet
bound.

The construction is target-relative: \(K_\delta\), its cover, and the packet
are built for the held-out target \(T\). The admitted probe family and its
physical design law must nevertheless be frozen independently of the target.
This is an assay-design theorem, not selection of one universal record
interface by physics.

The theorem does not derive the number of repetitions needed to achieve
\(\eta\). That requires the actual response statistics and their
between-trial memory. An IID bounded-output Hoeffding calculation would be an
additional conditional layer, not part of this result.

## 3. Deterministic effective-net variant

Suppose an effective \(\rho_\delta\)-net

\[
\{c_1,\ldots,c_{Q_\delta}\}
\]

is available and a target-independent separator algorithm returns, for every
net center \(c_j\), a physically admitted probe \(m_j\) with

\[
s_{m_j}(c_j)\geq a_\delta.
\]

Then the packet

\[
\{m_1,\ldots,m_{Q_\delta}\}
\]

has uniform margin at least \(a_\delta/2\) on \(K_\delta\).

This is constructive but can be extremely inefficient. Topological
compactness alone gives neither a computable net nor a separator oracle.
Calling the finite-subcover proof an experimental design algorithm would
silently add both.

## 4. Record-capacity lower bound

Let

\[
P_\delta(T(\Theta))
\]

be the maximum number of targets separated pairwise by at least \(\delta\).
Suppose a packet has \(N\) coordinates and each retained coordinate has an
alphabet of at most \(A\) values after calibration and quantization.

The full record alphabet has at most \(A^N\) values. A target-sufficient
record cannot assign the same record to two members of a
\(\delta\)-separated target packing. Therefore

\[
A^N
\geq
P_\delta(T(\Theta)),
\]

and

\[
N
\geq
\left\lceil
\frac{\log P_\delta(T(\Theta))}
     {\log A}
\right\rceil.
\]

This separates three costs:

```text
target entropy
  -> minimum total retained symbols / bits

physical probe family
  -> how many coordinates realize those symbols

response statistics and margin
  -> repetitions, precision, duration and source cost.
```

None determines the other two.

## 5. Exact packet-inflation counterexample

Let

\[
\Theta_n=\{1,\ldots,n\}
\]

with the discrete target metric, and let the only admitted probes be

\[
m_i(j)=\mathbf1_{\{i=j\}},
\qquad
i=1,\ldots,n.
\]

Any packet omitting two indices \(j\neq k\) assigns both completions the
all-zero record. Therefore every target-sufficient packet contains at least
\(n-1\) probes. Conversely, any \(n-1\) singleton probes suffice because the
omitted label is identified by all-zero response.

Thus:

\[
N_{\min}=n-1.
\]

Yet an unrestricted binary coding interface needs only

\[
\lceil\log_2n\rceil
\]

bits. The gap can grow without bound.

Compactness and target entropy therefore do not determine probe count. The
geometry of the physically admitted measurement family is load-bearing.

## 6. Exact margin-collapse counterexample

Let

\[
\Theta=[0,1],
\qquad
T(x)=x,
\qquad
m_\varepsilon(x)=\varepsilon x
\]

for arbitrary \(\varepsilon>0\).

One probe separates every target pair. For target resolution \(\delta\), its
uniform margin is

\[
\gamma_\delta=\varepsilon\delta.
\]

The retained error must satisfy

\[
2\eta<\varepsilon\delta.
\]

As \(\varepsilon\rightarrow0\), the topology, target, and packet count remain
unchanged while the required precision diverges. A fixed response
normalization, detector noise floor, source amplitude, and resource contract
are therefore necessary. Point separation alone has no quantitative content.

The same construction can make the mass of an indispensable probe under a
design distribution arbitrarily small, collapsing \(p_\delta\) and making
random packet discovery arbitrarily expensive.

## 7. Sobolev regularity balls are compact but quantitatively large

Consider the unit ball

\[
\Theta=B_{H^s}(\mathbb T^d)
\]

with target metric \(H^{s'}\), where

\[
r=s-s'>0.
\]

`HC-DU-096` establishes compactness in this weaker topology. The class
nevertheless has large metric entropy.

### Lower packing bound

Let

\[
\Lambda_R
=
\{k\in\mathbb Z^d:R\leq|k|\leq2R\},
\qquad
n_R=|\Lambda_R|\asymp R^d.
\]

For sign vectors \(\sigma\in\{-1,1\}^{n_R}\), define

\[
u_\sigma
=
cR^{-s}n_R^{-1/2}
\sum_{k\in\Lambda_R}
\sigma_ke^{ik\cdot x},
\]

with fixed sufficiently small \(c\). Every \(u_\sigma\) lies in the unit
\(H^s\) ball.

There is a subset of at least \(\exp(c_1n_R)\) sign vectors whose pairwise
Hamming distances are at least \(n_R/4\). For any two such vectors,

\[
\|u_\sigma-u_\tau\|_{H^{s'}}
\geq
c_2R^{-r}.
\]

Setting

\[
\epsilon=c_2R^{-r}
\]

gives

\[
\log P_\epsilon(\Theta;H^{s'})
\geq
c_3\epsilon^{-d/r}.
\]

### Elementary upper control

Truncate Fourier modes at \(|k|\leq R\). The \(H^{s'}\) norm of the discarded
tail is at most \(R^{-r}\). Choosing

\[
R\asymp\epsilon^{-1/r}
\]

leaves \(O(R^d)\) coordinates. A Euclidean cover of that finite-dimensional
ball gives

\[
\log N_\epsilon(\Theta;H^{s'})
\leq
C\epsilon^{-d/r}\log(C/\epsilon).
\]

The lower bound is enough for the present decision.

### Consequences

First,

\[
\overline{\dim}_{\mathrm B}\Theta
=
\limsup_{\epsilon\to0}
\frac{\log N_\epsilon(\Theta)}
     {\log(1/\epsilon)}
=
\infty.
\]

Second, suppose a map into \(\mathbb R^m\) had a Hölder-stable inverse on
\(\Theta\). A bounded subset of \(\mathbb R^m\) has only polynomial covering
growth; pulling that cover back through a Hölder inverse would force

\[
N_\epsilon(\Theta)
\leq
C\epsilon^{-q}
\]

for some finite \(q\), contradicting the entropy lower bound.

Therefore the full regularity ball admits no fixed finite-dimensional
bi-Hölder stable encoding. Fixed-resolution finite certification remains
possible, but no fixed finite stable packet works uniformly down to arbitrary
resolution for the identity target.

With \(A\) retained symbols per probe, the capacity lower bound yields

\[
N
\gtrsim
\frac{\epsilon^{-d/r}}{\log A}
\]

in the worst case.

This is not an absolute experimental cost for causal or conformal geometry.
Those targets may quotient away most field modes. It is the correct
worst-case warning against treating a regularity-compact completion ball as a
finite-dimensional model.

## 8. Primary-source collision and absorbers

Margaris and Robinson study Euclidean embeddings of compact subsets of Banach
spaces with finite box-counting dimension, extending the
Hunt--Kaloshin/Robinson program
([primary source](https://arxiv.org/abs/1811.03872)). This is a real positive
for finite-dimensional compact invariant sets. The full Sobolev ball above
fails its finite-box-dimension premise.

Haraux and Anguiano estimate Kolmogorov \(\epsilon\)-entropy for compact
Sobolev-like Hilbert ellipsoids and use it to bound dimensions of parabolic
attractors
([primary source](https://arxiv.org/abs/1704.02891)). The distinction is
exactly DU's: the regularity ball can have high/infinite effective dimension
while a physically selected dissipative attractor may have finite dimension.

Yap, Wakin, and Rozell prove stable random embeddings for
manifold-modeled signals under structured restricted-isometry conditions
([primary source](https://arxiv.org/abs/1209.3312)). The result quantifies
measurements only after manifold geometry and an admissible measurement
ensemble are supplied.

Flammia, Gross, Liu, and Eisert obtain compressed quantum tomography,
noise bounds, and near-matching sample-complexity bounds for low-rank states
under Pauli measurements
([primary source](https://arxiv.org/abs/1205.2300)). This is an excellent
physical positive control. Low rank and finite Hilbert dimension perform the
model-class reduction; the theorem does not transfer to a full
infinite-dimensional field completion class.

These literatures absorb the mathematical components. Dynamic Unity's
remaining task is not to rediscover compressed sensing. It is to determine
whether physical dynamics selects the required low-complexity class and
physical probe distribution before the held-out target is revealed.

## 9. Impact on the active-wave route

The active-wave candidate now has a quantitative admission ladder:

```text
physically selected regularity / noncollapse completion class
  -> compact target topology

physically selected probe ensemble
  + uniform small-ball observability (a_delta, p_delta)
  + pair-space entropy Q_delta
  -> bounded probe count

finite per-probe alphabet / precision
  + target packing
  -> record and coordinate lower bounds

joint realizability / repeatable preparation
  + complete acquisition
  + no-refit held-out transfer
  -> empirical finite certificate.
```

The nonlinear-wave uniqueness theorems previously audited do not yet supply:

- a probability measure on bounded physical sources/readouts;
- a uniform lower small-ball probability over every target pair;
- a response margin after finite detector resolution;
- a target-pair covering number for the admitted Lorentzian class;
- a jointly executable finite packet with bounded energy and duration; or
- implementation-complete acquisition.

Compactness makes the problem finite at each scale. The observability modulus
decides whether it is learnable at that scale.

## 10. Grade and disposition

### Earned

- **Scoped Grade 4:** compactness and pointwise separation alone imply no
  uniform packet-size, precision, or resource bound.
- **Scoped Grade 4:** target entropy lower-bounds total retained capacity,
  while restricted physical probe families can require far more coordinates.
- **Scoped Grade 4:** a regularity-compact Sobolev ball has infinite box
  dimension and no fixed finite-dimensional Hölder-stable encoding for the
  full weaker-norm identity target.
- **Conditional Grade 3:** a physically selected uniform small-ball
  observability modulus and effective pair cover give an explicit random or
  deterministic finite-packet construction.

### Not earned

- a physical probe distribution or observability modulus;
- a physically selected finite-dimensional manifold, attractor, sparse or
  low-rank class;
- joint QFT-realizable probe execution;
- repetitions, source energy, duration, bandwidth or detector precision;
- complete acquisition or no-refit transfer;
- a Grade-5 physical remainder or new prediction;
- a paper promotion; or
- a ready successor.

### Exact reopener

Reopen the active-wave candidate only with one physical arena that supplies:

1. the `HC-DU-096` compact target class;
2. a target-independent bounded physical probe ensemble \(\nu\);
3. explicit \(L,a_\delta,p_\delta,Q_\delta\);
4. a jointly realizable packet and repetition/noise calculation;
5. complete joined acquisition; and
6. no-refit transfer to a held-out causal or conformal target.

If the route instead assumes a finite-dimensional manifold, attractor,
sparsity, low rank, or parametric family, the physical law must independently
select that restriction and the result must be compared against the
corresponding standard embedding or compressed-sensing theorem.
