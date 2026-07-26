---
title: "Robust reconstruction, complete observer-action slice, and dynamics-restricted geometry"
date: 2026-07-26
status: completed_scoped_coupled_result
doc_type: exact_metric_theorem_vertical_counterexample_and_dynamics_tournament
run_id: RUN-20260726-161113-robust-vertical-dynamics-reconstruction
claim_grade: "EXACT ROBUST INVERSE-PROBLEM DECOMPOSITION + EXACT BINARY TWO-TIME INSTRUMENT COUNTEREXAMPLE + EXACT DYNAMICS-RESTRICTED POLYNOMIAL CONFORMAL THEOREM IN A SUPPLIED TOY FIELD LAW / COMPONENT MATHEMATICS KNOWN / NO PHYSICAL COMPLETENESS, SELECTED DYNAMICS, NEW LAW, ONTOLOGY, OR PAPER PROMOTION"
candidate_ids:
  - HC-DU-039B
  - HC-DU-036G
  - HC-DU-038C
related_ids:
  - HC-DU-036C
  - HC-DU-038B
  - HC-DU-039A
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_6
  - lane_7
  - lane_A
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
  - CH-SYN
probe_ref: tests/du_robust_vertical_dynamics_reconstruction_probe.py
artifact_ref: tests/artifacts/du_robust_vertical_dynamics_reconstruction_result.json
---

# Robust Reconstruction, Complete Observer-Action Slice, and
# Dynamics-Restricted Geometry

## Result in plain English

This coupled swing changes three parts of the reconstruction program.

First, reconstruction has two independent quantitative failure coordinates:

1. **record realizability:** how far the observed record lies from anything
   the admitted model class can produce; and
2. **target sufficiency:** how much the held-out result can still vary among
   the models that fit the record within its certified uncertainty.

A model can fit badly while agreeing perfectly about the target, or fit
perfectly while disagreeing maximally about the target. One number cannot
safely stand for both.

Second, the complete two-time slice finds the first unsupported bridge in a
formed record chain. A binary source can produce:

```text
physical event
    -> pointer value
    -> immutable archive
    -> provenance and occurrence identity
    -> compatible regional value certificate
    -> observer access
    -> correct value-reading capability
```

while still leaving its next measurement completely undetermined. A QND
instrument and a record-then-flip instrument have identical sharp outcome
effects and form the same archived value. Their repeat measurements are at
total-variation distance one.

The missing object is not another copy, threshold, quorum, or provenance tag
for the value. It is the **complete selective continuation**: what physical
map occurred conditional on the record. An independently formed
implementation-level selective-map receipt repairs the held-out repeat
exactly.

Third, the conformal hidden mode now has a precise dynamics boundary:

- smoothness does not remove it;
- analyticity does not remove it;
- a positive finite-action bound does not remove it;
- writing a field equation with an unrestricted source only renames the
  hidden mode as source structure; but
- a source-frozen equation whose homogeneous solution space and records are
  jointly uniqueness-generating does remove it.

In the supplied polynomial fixture, the target-independent toy scalar action

\[
S[u]=\frac12\int_{-1}^{1}(u')^2\,dx
\]

has source-free Euler--Lagrange equation \(u''=0\). That equation plus the
frozen records forces \(u=1\) and therefore the remote clock. The same
equation with unrestricted \(J\) in \(u''=J\) does not.

This is not a derivation of gravity and does not select a physical field law.
It tells Dynamic Unity exactly what a future dynamics must accomplish:

> It must remove the target-visible record nullspace through a frozen
> solution/source class. Merely naming a local equation, regularity
> condition, or energy penalty is insufficient.

The exact probe passes `36/36`; repeated artifacts are byte-identical at
SHA-256
`569aa36546ef97bdaa79babd0f14faf983745742af25a3c92423dec0b24dfd1a`.

## 1. The robust reconstruction type

Let:

- \(M\) be a nonempty compact admitted model class;
- \((Q,d_Q)\) be the certified-record metric space;
- \((Y,d_Y)\) be the held-out target metric space;
- \(r:M\to Q\) be the record map;
- \(t:M\to Y\) be the target map;
- \(q\in Q\) be the observed record;
- \(\epsilon\ge0\) be its certified record tolerance; and
- \(\tau\ge0\) be the declared target tolerance.

The model class, mixture closure, record and target types, metrics,
uncertainty, occurrence identity, gauge, resources, and observer boundary
must be frozen before adjudication. If not, the contract is incomplete.

Define the **realizability defect**

\[
\eta(q)
=
\inf_{m\in M}d_Q(r(m),q),
\tag{1}
\]

the tolerance fibre

\[
F_{q,\epsilon}
=
\{m\in M:d_Q(r(m),q)\le\epsilon\},
\tag{2}
\]

and, when that fibre is nonempty, the **target diameter**

\[
\Delta(q,\epsilon)
=
\sup_{m,n\in F_{q,\epsilon}}d_Y(t(m),t(n)).
\tag{3}
\]

For stochastic records, this run uses maximum total variation over all
declared record rows. For an intervention family, the target metric is
maximum total variation over the held-out response rows. Geometry uses the
declared \(L_\infty\) distance on calibrated scalar targets. These metrics
are supplied operational choices, not derived ontology.

### Theorem 1 — robust realizability/sufficiency trichotomy

Assume \(r\) and \(t\) are continuous. Exactly one branch holds:

1. \(\eta(q)>\epsilon\), returning `ROBUSTLY_UNREALIZABLE`;
2. \(\eta(q)\le\epsilon\) and
   \(\Delta(q,\epsilon)\le\tau\), returning
   `ROBUST_RECONSTRUCTION`; or
3. \(\eta(q)\le\epsilon\) and
   \(\Delta(q,\epsilon)>\tau\), returning
   `ROBUST_UNDERDETERMINATION` with an attaining witness pair.

#### Proof

Compactness and continuity make the infimum in equation (1) attainable.
Consequently \(F_{q,\epsilon}\) is empty exactly when
\(\eta(q)>\epsilon\). If it is nonempty, it is compact. Its image under
continuous \(t\) is compact, so the diameter in equation (3) is attained and
is either at most \(\tau\) or greater than \(\tau\). The three cases are
disjoint and exhaustive. \(\square\)

At \(\epsilon=\tau=0\), compactness gives:

- \(\eta(q)>0\) exactly when \(q\notin\operatorname{im}r\);
- \(\eta(q)=0\) exactly when the exact fibre is nonempty; and
- \(\Delta(q,0)=0\) exactly when \(t\) is constant on that fibre.

The theorem therefore reduces to `HC-DU-039A` in the exact limit.

### Why the two defects cannot be collapsed

The finite stochastic control constructs all four combinations:

| record defect \(\eta\) | target diameter \(\Delta\) | result |
|---:|---:|---|
| \(0\) | \(0\) | exact reconstruction |
| \(0\) | \(1\) | exact underdetermination |
| \(1/4\) | \(0\) | near-fit but target-sufficient at \(\epsilon=1/4\) |
| \(1/4\) | \(1\) | same near-fit, target-insufficient |

At \(\epsilon=1/8\), the last two models lie outside the feasible fibre and
return robust unrealizability. Their target behavior is not consulted.

This does not replace `HC-DU-036C`. That result asks how well an admitted
stochastic record kernel can *decode* a complete response family.
Equations (1)--(3) ask a prior inverse question: whether the observed record
is near the admitted model image and how wide the target remains over its
preimage. The quantities should be composed, not merged.

### Theorem 2 — robust same-class refinement

Let \(r_2:M\to Q_2\) refine \(r_1:M\to Q_1\) on the same model class, with

\[
r_1=\pi\circ r_2,\qquad q_1=\pi(q_2),
\]

where \(\pi\) is \(L\)-Lipschitz. Then

\[
F^{(2)}_{q_2,\epsilon}
\subseteq
F^{(1)}_{q_1,L\epsilon}.
\tag{4}
\]

#### Proof

If \(m\in F^{(2)}_{q_2,\epsilon}\), then

\[
\begin{aligned}
d_{Q_1}(r_1(m),q_1)
&=d_{Q_1}(\pi(r_2(m)),\pi(q_2))\\
&\le Ld_{Q_2}(r_2(m),q_2)\\
&\le L\epsilon.
\end{aligned}
\]

This proves equation (4). \(\square\)

Thus a fine fibre can reduce target diameter, but if the corresponding
coarse fibre is robustly empty, no same-class fine record projecting to it
can be populated. For stochastic coarse-graining, total variation obeys the
data-processing inequality and \(L=1\).

As in `HC-DU-039A`, a repair that changes occurrence identity, source class,
mixture closure, observer boundary, or \(M\) is contract retyping rather
than ordinary refinement.

## 2. The complete two-time observer/action slice

### Frozen physical instruments

On a binary source basis, use:

\[
K_r^{Q}=|r\rangle\langle r|
\]

for the QND instrument and

\[
K_r^{F}=X|r\rangle\langle r|
\]

for record-then-flip. For both:

\[
(K_r^{Q})^\dagger K_r^{Q}
=
(K_r^{F})^\dagger K_r^{F}
=
|r\rangle\langle r|.
\]

The outcome effects are identical and sum to the identity. Each instrument
records \(r=h\) with certainty for source history \(h\), and the archive
retains that value.

The run also enumerates the full deterministic binary
measure-and-prepare family

\[
K_r^{f}=|f(r)\rangle\langle r|,
\qquad
f:\{0,1\}\to\{0,1\}.
\]

There are four post-record maps:

```text
prepare zero: (0,0)
QND:          (0,1)
flip:         (1,0)
prepare one:  (1,1)
```

All four have the same effects and record table. Their repeat-measurement
tables realize all four deterministic binary continuations.

### What agrees before the held-out intervention

The frozen chain records:

1. the physical basis-state source event;
2. its selective pointer outcome;
3. an immutable archive copy;
4. the run-local occurrence identity;
5. the route `source -> pointer -> archive`;
6. exact pointer/archive value compatibility;
7. declared value finality under the later repeat;
8. observer read access; and
9. the capability to announce the original basis value.

Every implementation agrees on that chain. In particular, the later repeat
does not rewrite the archive.

This is a complete chain for the declared **value-reading** action. It is not
called a complete physical record of every continuation.

### The held-out result

For QND, the repeat result equals \(h\). For record-then-flip, it equals
\(1-h\). Their complete repeat-response tables are at total-variation
distance one.

Applied to all four implementations, the robust contract returns:

\[
\eta=0,\qquad\Delta=1,
\]

and `ROBUST_UNDERDETERMINATION`.

With a noisy observed archive at error \(1/20\):

- at certified tolerance \(\epsilon=1/20\), every implementation remains
  feasible and \(\Delta=1\);
- at \(\epsilon=1/40\), none is feasible and the result becomes
  `ROBUSTLY_UNREALIZABLE`.

This cleanly separates archive-model fit from continuation sufficiency.

### The exact repair

Add an independently formed implementation-level receipt for the complete
selective map, represented by the joint record/post-state transition table.
Forgetting the post-state tag is a stochastic projection back to the
ordinary archive record.

The refined QND fibre is the singleton `qnd`; its repeat target diameter is
zero. Total-variation contraction and fine-fibre inclusion are checked
exactly.

The repair says:

```text
more copies or stronger finality of the same value
    != complete selective continuation

complete selective-map receipt
    -> repeat-response reconstruction in the frozen class
```

### What this changes

This is standard quantum-instrument mathematics, and earlier DU controls
already distinguished equal effects from equal instruments. The new result
is the end-to-end localization:

> Physical formation, provenance, regional value compatibility, immutable
> finality, observer access, and one genuine capability can all succeed
> before the selective continuation is known.

Therefore finality and capability must remain proposition- and
intervention-indexed. “The record is final” cannot silently become “the
complete future physical response is final.”

The witness is arity-minimal inside the frozen binary
measure-and-prepare class: underdetermination needs at least two
implementations and two target outcomes, and continuation difference needs
one formed event followed by one held-out intervention. This is not a global
minimality theorem over arbitrary quantum models.

## 3. Dynamics-restricted conformal reconstruction

### Frozen arena and previous hidden mode

Reuse

\[
g_u=u(x)(-dt^2+dx^2)
\]

on the anchored strip and the degree-four hidden polynomial

\[
h(x)=1-2x-9x^2+4x^3+10x^4.
\]

The training record is:

\[
R(u)
=
\left(
\int_{-1}^{1}u,\;
\int_{-1}^{0}u,\;
\int_{-1}^{1/2}u,\;
u(-1)
\right),
\]

and the held-out remote-clock target is

\[
T(u)=u(1).
\]

Exactly:

\[
R(1+h/100)=R(1)=(2,1,3/2,1),
\]

while

\[
T(1+h/100)=26/25\ne1=T(1).
\]

The previous conservative positivity bound remains
\(1+h/100\ge3/5\).

On the five-dimensional degree-at-most-four polynomial space:

- \(R\) has rank four;
- its nullspace is one-dimensional;
- adding \(T\) raises the rank to five; and
- \(h\) is the exact target-visible null direction.

### Theorem 3 — dynamics-restricted record reconstruction

Let \(V\) be a linear completion space, \(L:V\to W\) a frozen linear field
operator, \(R:V\to Q\) the record operator, and \(T:V\to Y\) the held-out
target.

On a nonempty fixed-source solution class

\[
M_J=\{u\in V:Lu=J\},
\]

\(T\) is constant on every record fibre exactly when

\[
\ker L\cap\ker R\subseteq\ker T.
\tag{5}
\]

#### Proof

Two fixed-source solutions \(u_0,u_1\) with the same record differ by
\(v=u_1-u_0\) satisfying \(Lv=0\) and \(Rv=0\). They have the same target
exactly when \(Tv=0\). Therefore target constancy for all such pairs is
equivalent to equation (5). \(\square\)

If source differences are admitted from a space \(D_J\subseteq W\), replace
\(\ker L\) by

\[
\{v\in V:Lv\in D_J\}.
\tag{6}
\]

An arbitrary source class can therefore make the field equation impose no
restriction at all: every completion simply carries \(J=Lu\).

This is standard linear inverse-problem mathematics. Its DU value is the
typed rule for deciding whether a proposed dynamics actually closes the
record fibre.

### Four-way hostile tournament

#### A. Smoothness and analyticity

The hidden mode is a polynomial. It survives both. The target diameter
remains \(1/25\).

#### B. A positive finite-action bound

For

\[
S[u]=\frac12\int_{-1}^{1}(u')^2dx,
\]

the hidden rival has exact action

\[
S[1+h/100]
=
\frac{143}{21875}
<
\frac1{100}.
\]

More generally,

\[
S[1+\lambda h]=\lambda^2S[h].
\]

For every positive action bound, a sufficiently small nonzero rational
\(\lambda\) preserves positivity, every training record, and a nonzero
remote-clock change. A bound regularizes the hidden mode but cannot remove
it.

Selecting the unique action minimizer would be stronger. It is a supplied
variational law, not the same premise as finite action.

#### C. Inhomogeneous dynamics with unrestricted source

The hidden rival satisfies

\[
u''=J_h,\qquad
J_h=-\frac9{50}+\frac6{25}x+\frac65x^2.
\]

If that source is allowed, the field equation preserves the same
underdetermined fibre. The source field has absorbed the missing mode.

#### D. Source-free Euler--Lagrange dynamics

The source-free stationary equation is

\[
u''=0.
\]

Every solution is \(u=ax+b\). The anchored clock and total volume give

\[
-a+b=1,\qquad 2b=2,
\]

so \(a=0,b=1\). The remote clock is forced:

\[
u(1)=1.
\]

Equivalently, stacking the dynamics rows with the record rows raises the
rank to five; the fixed-source record nullspace is zero. The robust result
is `ROBUST_RECONSTRUCTION`.

Again, this is only a supplied toy scalar law. It establishes a proof
boundary, not the correct physics of the conformal factor.

## 4. What the three stages say together

The coupled result is:

```text
freeze physical/model/identity/resource contract
    -> compute distance eta from observed record to admitted record image
    -> if eta exceeds uncertainty, stop: record/model contract mismatch
    -> otherwise compute target diameter Delta on the feasible fibre
    -> if Delta is too large, identify the target-visible null direction
    -> add only an independently formed record or independently warranted
       dynamics that removes that direction
    -> rerun both eta and Delta
```

This produces two exact diagnostics for different failures:

| failure | witness | valid repair |
|---|---|---|
| record outside admitted image | positive \(\eta-\epsilon\) | recalibration, physical model change, identity/completion retyping |
| target varies on feasible fibre | positive \(\Delta-\tau\) and model pair | formed same-class refinement or warranted uniqueness-generating dynamics |

The vertical and geometry cases then identify two distinct null directions:

| case | record-null distinction | what removes it |
|---|---|---|
| two-time instrument | post-record selective continuation | complete selective-map receipt |
| conformal geometry | target-visible geometric mode | fixed source/dynamics satisfying equation (5) |

Neither is repaired by merely making the already-recorded value more final.

## 5. Consequence for the North Star

The North Star does not change. Its implementation becomes sharper:

> Independently selected observer-indexed certified causal records must first
> be realizable in the admitted physical class. On the resulting uncertainty
> fibre, they must reconstruct each declared observer-accessible target to
> its tolerance, or return an exact target-visible remainder witness.

Two additions are now mandatory:

1. every reconstruction receipt carries both \(\eta\) and \(\Delta\); and
2. every proposed dynamics declares its source-difference space and proves
   that its admissible tangent space removes the target-visible record
   nullspace.

This prevents three common false positives:

- calling an inconsistent or badly fitted record reconstructive;
- promoting finalized value access into complete continuation knowledge; and
- calling a field equation reconstructive while its free source absorbs
  every hidden mode.

## 6. Collision and earned grade

The mathematical and physical components are occupied:

- robust feasible-set inversion, set-membership estimation, and
  identification diameter;
- total-variation data processing;
- quantum effects, selective instruments, QND measurement, and
  measure-and-prepare continuations;
- linear field-equation inverse problems, nullspaces, and regularization;
  and
- elementary Euler--Lagrange and polynomial rank calculations.

The result is therefore not promoted as new mathematics or new physics.
The earned Dynamic Unity contribution is a coupled program theorem and
localization:

1. record-model misfit and held-out insufficiency are independent;
2. a complete value-finality chain can stop short of selective
   continuation; and
3. geometry closes only under a source-typed, uniqueness-generating
   dynamics, not regularity or finite action alone.

`HC-DU-039B`, `HC-DU-036G`, and `HC-DU-038C` are scoped exact program
results. None completes their broader physical candidates.

## 7. Stops and next reopener

Do not claim:

- one scalar reconstruction deficiency;
- physical nonexistence from positive record-model misfit under a weak class;
- complete physical finality from one finalized proposition;
- total capability equality for the QND and flip implementations;
- a unique microscopic instrument from an implementation-level receipt;
- selected geometry from the source-free toy law;
- Einstein dynamics, quantum gravity, new physics, or record-first ontology;
- theorem novelty for the occupied component mathematics; or
- paper, Drafting Factory, submission, publication, provider, or hardware
  progress.

The highest-value next reopener is no longer another synthetic mode or more
archive copies. It is one of:

1. apply the \((\eta,\Delta)\) receipt to a genuinely
   implementation-complete physical packet;
2. replace the toy \(u''=0\) law with one independently warranted physical
   dynamics and a frozen source class; or
3. test whether one proposed layered regional-finality dynamics removes a
   target-visible continuation/null direction without silently adding the
   answer to the certificate.

External hardware is not required to learn the exact boundaries established
here. The local build stops at this result.
