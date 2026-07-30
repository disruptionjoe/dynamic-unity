---
title: "Action-relative behavioral quotient, observed mean, and material-realization boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-163
run_id: RUN-20260730-122318-action-relative-materialization
work_id: MPA-05-ACTION-RELATIVE-RECORD-MATERIALIZATION
action_id: MPA-05-ACTION-RELATIVE-RECORD-MATERIALIZATION
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Action-relative quotient and material-realization boundary

## Executive return

```text
ACTION_RELATIVE_QUOTIENT
+ OBSERVED_MEAN_QUOTIENT_ONLY
+ MATERIAL_REALIZATION_NONIDENTIFICATION
+ ACTION_CLASS_REFINEMENT
+ PARTIAL_PHYSICAL_TYPING
+ KNOWN_RESULT_ABSORPTION
+ NO_READY_SUCCESSOR
```

Swing 5 freezes the smallest source-realized future action on the Peronnin
sequential superconducting-qubit readout platform:

```text
after the first readout:
  apply no outcome-conditioned control
  begin the same second readout 220 ns later
  retain the second calibrated binary outcome
```

At that scope, the coarsest exact behavioral quotient exists as a set
quotient and is unique up to relabeling. It assigns two complete physical
histories to the same class exactly when they induce the same conditional law
for the second outcome.

That mathematical positive does not become a material-record positive:

> The reported \(95\%\) QND agreement is an observed average over histories
> admitted by the first result. It does not show that the complete
> history-conditioned response law is constant on the raw-trace, calibrated
> statistic, or binary-label fibres.

The exact boundary is stronger than ordinary missing-data caution. A single
categorical response from each physical history identifies the **mean** of
the response laws inside a record fibre and cannot identify their dispersion.
Two completion models can therefore have the same candidate-record
distribution, the same joined one-step response law at every reported record
level, and the same \(95\%\) aggregate repeat agreement while possessing
different physical-history quotients.

No source-pinned archive is shown to realize the quotient. Swing 6 does not
activate.

Primary physical source:
[Peronnin, Marković, Ficheux, and Huard, “Sequential dispersive
measurement of a superconducting qubit”](https://arxiv.org/abs/1904.04635),
*Physical Review Letters* 124, 180502 (2020).

## 1. Frozen physical and action contract

Let \(\Omega\) be the lawful complete physical histories through the end of
the first readout. “Complete” is relative to the declared physical completion
class; it is not a hidden-variable or ontological claim.

The candidate source records are:

\[
\begin{aligned}
r_V(h)&=V_1(t),\\
r_\beta(h)&=\beta_1=\int V_1(t)w(t)\,dt,\\
r_z(h)&=z_1\in\{g,e\}.
\end{aligned}
\]

The hypothetical full-lineage archive \(r_L\) remains a comparison object.
`HC-DU-162` showed that the source does not select its retention,
provenance, or reset semantics.

The frozen action class contains one action \(a_0\):

1. do not use \(z_1\) to change a later physical control;
2. wait until the source's fixed second readout begins;
3. perform the same readout with the same \(w\) and \(Z_g\); and
4. retain only \(z_2\in\{g,e\}\).

No alternate basis, pulse, feedback command, raw second trace, detector
tomography, or additional intervention belongs to this action class.

For \(h\in\Omega\), define the physical response signature

\[
\sigma_{a_0}(h)
=
\left(
\mathbb P(z_2=g\mid\operatorname{do}(a_0),h),
\mathbb P(z_2=e\mid\operatorname{do}(a_0),h)
\right).
\tag{1}
\]

This is a physical-history conditional law. It is not the observed
conditional frequency given \(z_1\), \(\beta_1\), or \(V_1\).

## 2. Coarsest action-relative quotient theorem

The result is stated for an arbitrary frozen finite family of actions because
the proof costs nothing beyond the one-action case.

Let \(A\) be a set of admitted actions, with response kernels

\[
K_a:\Omega\longrightarrow\mathcal P(Y_a)
\qquad (a\in A).
\]

Define the complete response signature

\[
\sigma_A(h)=\left(K_a(h)\right)_{a\in A}
\tag{2}
\]

and

\[
h\sim_A h'
\quad\Longleftrightarrow\quad
\sigma_A(h)=\sigma_A(h').
\tag{3}
\]

Let \(q_A:\Omega\to Q_A=\Omega/{\sim_A}\) be the quotient map.

### Proposition 1 — existence, uniqueness, and universal property

\(Q_A\) is the unique coarsest exact behavioral quotient, up to bijective
relabeling.

For any record map \(r:\Omega\to R\), the following are equivalent:

1. equal records imply equal response laws;
2. \(\ker r\subseteq\ker\sigma_A\);
3. there is a unique map
   \(\phi:r(\Omega)\to Q_A\) satisfying

   \[
   q_A=\phi\circ r.
   \tag{4}
   \]

Thus every response-sufficient record refines \(q_A\).

### Proof

Equation (3) is an equivalence relation because equality of response
signatures is reflexive, symmetric, and transitive. The quotient therefore
exists.

If equal \(r\)-values imply equal signatures, assign

\[
\phi(r(h))=q_A(h).
\]

The implication makes this well-defined, and surjectivity of \(r\) onto its
image makes it unique. Conversely, (4) makes equal records imply equal
quotient classes and hence equal signatures.

Any other quotient with this universal property factors through and is
factored through by \(q_A\), so the induced maps on quotient classes are
inverse bijections.

This is a set-level result. It does not guarantee that \(Q_A\) is a standard
Borel quotient, finite dimensional, continuous, learnable, computable, or
materially realizable. Each stronger property requires additional
regularity.

### Corollary 1 — material realization trichotomy

A candidate archive \(r\):

- realizes the coarsest quotient exactly iff
  \(\ker r=\ker\sigma_A\);
- is response-sufficient but overfine iff
  \(\ker r\subsetneq\ker\sigma_A\);
- is lossy/coarse if it merges a response-distinct pair; and
- can be incomparable with the quotient if it both preserves irrelevant
  distinctions and loses a response-relevant one.

Completeness of provenance and behavioral minimality are therefore different
questions. An injective attempt archive is trivially response-sufficient but
usually overfine.

### Corollary 2 — action refinement

If \(A\subseteq A'\), then

\[
\ker\sigma_{A'}\subseteq\ker\sigma_A.
\tag{5}
\]

Adding actions can only refine the exact quotient. A record exact for one
observer/action class may be coarse for another without either observer being
subjective or mistaken.

## 3. Physical-history law versus observed mean law

Let \(H\) be the random complete history and let \(R=r(H)\) be a candidate
record. For a finite response event \(y\), the observed conditional response
is

\[
\bar K_a(r;y)
=
\mathbb P(Y_a=y\mid\operatorname{do}(a),R=r).
\tag{6}
\]

The law of total conditional probability gives

\[
\bar K_a(R;y)
=
\mathbb E\!\left[
  K_a(H;y)
  \mid R
\right].
\tag{7}
\]

Equation (7) is the pivotal type wall:

```text
physical-history response signature
  --conditional averaging over a record fibre-->
observed predictive law
```

The arrow need not be invertible.

### Proposition 2 — zero-heterogeneity sufficiency criterion

For finite outcomes, define

\[
\mathcal D_A(r)
=
\sum_{a\in A}
\mathbb E
\left[
  \left\|
    K_a(H)-\mathbb E[K_a(H)\mid R]
  \right\|_2^2
\right].
\tag{8}
\]

Then, on the support of the declared probability law,

\[
\mathcal D_A(r)=0
\quad\Longleftrightarrow\quad
\sigma_A\text{ factors through }r
\quad\text{almost surely}.
\tag{9}
\]

### Proof

Each term in (8) is nonnegative. The sum is zero exactly when every response
probability is almost surely measurable with respect to \(R\), which is
equivalent to factorization of every \(K_a\) through \(r\).

Equation (8) is conditional-variance mathematics, not a new physical
quantity. It is useful here because it separates:

- estimating \(\bar K_a(r)\), the mean predictive response after seeing the
  record; from
- establishing \(\mathcal D_A(r)=0\), the physical claim that no
  response-relevant heterogeneity remains inside the record fibre.

### Proposition 3 — one-response latent-dispersion nonidentification

For a binary response and any
\(\bar p(r)\in(0,1)\), choose

\[
0<\epsilon(r)
\le
\min\{\bar p(r),1-\bar p(r)\}.
\]

Two equally weighted history subtypes with response propensities

\[
p_\pm(r)=\bar p(r)\pm\epsilon(r)
\tag{10}
\]

produce the same observed Bernoulli law as a homogeneous history with
propensity \(\bar p(r)\).

Therefore one future Bernoulli response per history identifies
\(\bar p(r)\), not the conditional dispersion of \(p(H)\) within \(r\).

This does not posit a hidden subtype in the apparatus. It proves that the
observed one-step law alone cannot exclude one.

## 4. Exact \(95\%\) source-report twins

The finite control uses histories

\[
h=(z,u,n_\beta,n_V),
\]

where:

- \(z\in\{g,e\}\) is the first label;
- \(u\in\{\mathrm{stable},\mathrm{fragile}\}\) is an admitted but unrecorded
  physical-history coordinate in the hostile completion;
- \(n_\beta,n_V\in\{0,1\}\) are response-irrelevant record distinctions.

All sixteen histories are equally weighted.

Candidate record maps are:

\[
\begin{aligned}
r_z(h)&=z,\\
r_\beta(h)&=(z,n_\beta),\\
r_V(h)&=(z,n_\beta,n_V),\\
r_L(h)&=h.
\end{aligned}
\]

The finite symbols represent only the refinement relations among label,
statistic, trace, and an idealized identity archive. They are not a model of
the microwave waveform.

### Completion A — homogeneous response

Every history repeats its first label with probability

\[
p_{\rm same}=\frac{19}{20}.
\]

The physical quotient has two classes, one for each first label.

### Completion B — within-record heterogeneity

\[
p_{\rm same}(u)
=
\begin{cases}
1,&u=\mathrm{stable},\\
9/10,&u=\mathrm{fragile}.
\end{cases}
\tag{11}
\]

The mean within every \(z\), \((z,n_\beta)\), and
\((z,n_\beta,n_V)\) fibre remains

\[
\frac12\left(1+\frac9{10}\right)=\frac{19}{20}.
\]

The two completions consequently have:

- identical candidate-record distributions;
- identical joined one-step response laws at the label, statistic, and trace
  levels;
- identical \(95\%\) aggregate repeat agreement; but
- two versus four physical-history quotient classes.

Their archive relations are:

| candidate | homogeneous completion | heterogeneous completion |
|---|---|---|
| binary label \(r_z\) | exact realization | coarse response loss |
| calibrated statistic \(r_\beta\) | overfine and sufficient | incomparable |
| raw trace \(r_V\) | overfine and sufficient | incomparable |
| idealized identity archive \(r_L\) | overfine and sufficient | overfine and sufficient |

For \(r_z\), the within-record response-propensity variance is:

\[
0
\quad\text{versus}\quad
\frac1{400}.
\]

The exact probe verifies every relation. The hostile completion is not
evidence that the source contains \(u\); it proves that the source's reported
one-step statistics do not decide whether it does.

## 5. What the source earns

Peronnin et al. report:

- one single-realization digitized \(V(t)\);
- a calibrated \(\beta\) distribution and \(g/e\) classifier;
- two readouts performed one after the other;
- heralding on first-readout realizations that give the expected prepared
  outcome;
- a \(95\%\) probability that the second result equals the first; and
- average two-readout signals in supplemental Fig. S12.

The second readout starts \(220\) ns after the first. The source does not
report:

- the complete conditional kernel
  \(\mathbb P(z_2\mid z_1)\) separately for every first label;
- joined per-attempt
  \(V_1,\beta_1,z_1,V_2,\beta_2,z_2\) data;
- \(\mathbb P(z_2\mid V_1)\) or
  \(\mathbb P(z_2\mid\beta_1)\);
- a self-consistent postmeasurement instrument tomography;
- a proof that the future response law is constant on any candidate-record
  fibre; or
- a minimality proof that a sufficient record contains no
  response-irrelevant detail.

The \(95\%\) scalar is even coarser than the observed label-conditioned
quotient. It averages over heralded first outcomes and therefore does not by
itself specify both binary transition rows.

### Source-pinned disposition

| object | earned status |
|---|---|
| abstract \(Q_{H_{\rm QND}}\) | exists uniquely up to relabeling |
| observed mean response | one aggregate same-outcome probability reported |
| binary label realizes \(Q_H\) | not identified |
| calibrated statistic realizes \(Q_H\) | not identified |
| raw trace realizes \(Q_H\) | not identified |
| complete lineage realizes \(Q_H\) | not source-selected; exactness not tested |
| response-conditioned physical feedback | absent |
| action-relative reconstruction | not earned |

Physical trace formation remains a real positive from `HC-DU-162`. This
result does not demote it. It prevents physical formation from being cast as
predictive sufficiency or behavioral minimality without the missing test.

## 6. Action-class extension control

The finite control adds one explicitly excluded audit response depending on
\(u\). In the homogeneous baseline:

```text
repeat-readout-only quotient: 2 classes
repeat-readout + audit quotient: 4 classes
```

The binary label changes from exact to coarse.

This is not a proposed physical intervention on the Peronnin apparatus. It
verifies (5) and records the operational consequence:

> “The record is complete” has no action-independent meaning. Every new
> admitted action requires the quotient relation to be rechecked.

The control does not violate the frozen contract because the audit action is
not used in the source disposition.

## 7. Absorber collision

The general mathematics is mature.

| absorber | what it already supplies | surviving DU use |
|---|---|---|
| minimal sufficient statistics and Blackwell comparison | factorization, minimality, and decision-relative information order | distinguish exact quotient from a physically formed archive |
| [Shalizi–Crutchfield causal states](https://arxiv.org/abs/cond-mat/9907176) | histories are equivalent when they induce the same future distribution; minimal predictive representation | keep observed-history causal states separate from complete physical-history sufficiency |
| [predictive-state representations](https://arxiv.org/abs/1207.4167) | controlled state represented by predictions of future tests | make action-class dependence explicit |
| probabilistic bisimulation and lumpability | behavioral equivalence and quotienting of stochastic systems | supply the transition-system analogue |
| [process-tensor tomography](https://arxiv.org/abs/2106.11722) | operationally complete multi-time response to admitted interventions | identifies what the one-action source does not supply |
| [QND measurement tomography](https://arxiv.org/abs/2109.06616) | reconstructs measurement processes, fidelity, ideality, and backaction | supplies a plausible process-level reopener, not archive selection |

The quotient theorem, conditional-mean identity, and finite mixture
nonidentification are not novel mathematics.

The scoped Dynamic Unity contribution is the typed conjunction:

```text
minimal predictive quotient of observed histories
  !=
minimal behavioral quotient of complete physical histories
  !=
physically formed material archive realizing either quotient
```

That distinction is useful to the North Star but should not be advertised as
a new causal-state, PSR, bisimulation, or sufficiency theorem.

## 8. Campaign disposition

Swing 5 is complete at scoped Grade 4:

```text
ACTION_RELATIVE_QUOTIENT
+ OBSERVED_MEAN_QUOTIENT_ONLY
+ MATERIAL_REALIZATION_NONIDENTIFICATION
+ ACTION_CLASS_REFINEMENT
+ PARTIAL_PHYSICAL_TYPING
+ KNOWN_RESULT_ABSORPTION
+ NO_READY_SUCCESSOR
```

Not earned:

- no source-selected coarsest material archive;
- no proof that \(V_1,\beta_1,\) or \(z_1\) is physically sufficient;
- no action-relative reconstruction;
- no law–record target-diameter comparison;
- no first leak;
- no transfer result;
- no regional finality;
- no ontology priority;
- no new quantum law or new physics.

Swing 6 does not activate because the source does not freeze a material record
whose relation to the physical-history quotient is known. Advancing anyway
would replace the failed prerequisite with an observed mean quotient.

### Exact reopener

Reopen the campaign only with one source-pinned packet that supplies:

1. joined per-attempt first records and later responses;
2. a predeclared intervention or tomography family rich enough to determine
   the postmeasurement response process;
3. an explicit retention, provenance, access, and reset contract;
4. a proof or falsifiable test that the response kernel factors through the
   retained archive; and
5. a minimality test showing which archived distinctions are behaviorally
   irrelevant.

QND instrument tomography or process-tensor tomography may help with items
2 and 4. Neither automatically selects or materializes items 1, 3, or 5.

## Reproducibility

The exact quotient partitions, observed-law twins, conditional-variance
control, archive relations, and action extension are in:

```text
tests/du_action_relative_materialization_probe.py
tests/artifacts/du_action_relative_materialization_result.json
```

Passing establishes only those finite logical controls. It establishes no
latent variable in the source apparatus, complete physical archive,
reconstruction, remainder, new law, or new physics.
