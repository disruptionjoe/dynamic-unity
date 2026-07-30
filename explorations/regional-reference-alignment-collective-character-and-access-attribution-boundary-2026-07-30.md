---
title: "Regional reference alignment: collective character, correlated frame glue, and access-attribution boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-174
run_id: RUN-20260730-171206-regional-reference-alignment-gate
work_id: REGIONAL-REFERENCE-ALIGNMENT-GATE
action_id: REGIONAL-REFERENCE-ALIGNMENT-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Regional reference alignment

## Executive result

`HC-DU-173` left an exact coherent first leak: a global
\(X\otimes X\) response separates a coherent order-marker completion from
its incoherent mixture. The first candidate continuation was to generalize
that result to many regions.

The duplicate gate fired. `HC-DU-035A/C` had already proved that GHZ phase is
hidden from every proper coalition and can be recovered by local \(X\)
measurements plus classical parity pooling. `HC-DU-125` had already shown,
in a formed finite-Abelian record model, that global gluing information can
live only in correlations among regional transcripts. Rebuilding either
result would add no knowledge.

The surviving seam was a premise hidden in the phrase “local measurements
plus pooling”: the local measurement axes must possess a physically usable
relation.

For the \(n\)-region coherence family

\[
\rho_\eta
=
\frac12
\left(
|0^n\rangle\!\langle0^n|
+|1^n\rangle\!\langle1^n|
+\eta|0^n\rangle\!\langle1^n|
+\bar\eta|1^n\rangle\!\langle0^n|
\right),
\qquad |\eta|\leq1,
\tag{1}
\]

and local equatorial measurements

\[
M_i(\theta_i)
=
\cos\theta_i\,X+\sin\theta_i\,Y,
\tag{2}
\]

the joined product-parity response is exactly

\[
C(\boldsymbol\theta)
=
\operatorname{tr}
\left[
\rho_\eta\bigotimes_iM_i(\theta_i)
\right]
=
\operatorname{Re}
\left[
\eta e^{i\sum_i\theta_i}
\right].
\tag{3}
\]

Only one collective phase relation matters. Under local frame changes
\(\alpha_i\),

\[
\eta\mapsto\eta e^{-i\sum_i\alpha_i},
\qquad
\theta_i\mapsto\theta_i+\alpha_i,
\tag{4}
\]

and Equation (3) is invariant. The relevant reference object is therefore
the quotient

\[
U(1)^n/\ker\!\left(\sum\right)\cong U(1),
\tag{5}
\]

not \(n\) absolute phase origins and not a preferred global frame.

This produces the nonintuitive exact control:

> Every region can have a completely uninformative marginal phase reference,
> yet the joined coherence response can remain perfect when the reference
> errors are correlated so that their total phase is fixed.

Conversely, one independently twirled regional frame makes the parity
response vanish. Local reference-quality scores do not determine regional
composability; the missing access resource may live entirely in relations
among the frames.

The complete return is:

```text
MULTIPARTITE_THRESHOLD_DUPLICATE_STOP
+ REFERENCE_COVARIANT_PARITY_LAW
+ COLLECTIVE_U1_CHARACTER_QUOTIENT
+ LOCALLY_UNIFORM_RELATIONALLY_ALIGNED_POSITIVE_CONTROL
+ ONE_INDEPENDENT_TWIRL_CLOSES_THE_FIRST_LEAK
+ TWO_SETTING_RELATIONAL_PHASE_RECONSTRUCTION
+ REFERENCE_ERROR_AND_DEPHASING_PRODUCT_LAW
+ EXACT_ACCESS_ATTRIBUTION_TWIN
+ NO_GLOBAL_REFERENCE_OR_PREFERRED_FRAME_REQUIREMENT
+ KNOWN_QRF_ASYMMETRY_GHZ_AND_DEPHASING_ABSORPTION
+ NO_SELECTED_REFERENCE_RECORD_CONSENSUS_OR_NEW_PHYSICS
+ NO_READY_SUCCESSOR
```

This is a scoped Grade-4 access/reference necessity result. The mathematics
is standard quantum reference-frame, asymmetry, Fourier-character, GHZ, and
dephasing mathematics. The Dynamic Unity increment is the typed composition
boundary.

## 1. Duplicate gate

The proposed all-party access theorem was already present:

- `HC-DU-035A` classifies the GHZ phase pair as exact three-of-three access
  to one classical label, not redundancy, objectivity, QEC, or consensus.
- `HC-DU-035C` includes noisy GHZ logical access and proper-coalition
  indistinguishability.
- The associated adversarial audit already corrects the false claim that an
  entangled collective measurement is needed: local \(X\) measurements and
  classical pooling suffice.
- `HC-DU-125` gives the more physical regional analogue in which every local
  record marginal is fixed while the global glue lives in joined
  correlations.

Those results remain controls here. No new claim credit is assigned to:

\[
\text{proper-subset equality}
\quad\text{or}\quad
\text{local measurement plus parity pooling}.
\]

The new question begins only after asking what makes the local \(X\) labels
refer to compatible physical axes.

## 2. The relational parity theorem

Write

\[
M(\theta)
=
e^{-i\theta}|0\rangle\!\langle1|
+e^{i\theta}|1\rangle\!\langle0|.
\tag{6}
\]

The diagonal terms of \(\rho_\eta\) contribute zero to the expectation of
\(\bigotimes_iM(\theta_i)\). The two off-diagonal terms give

\[
\frac12\eta e^{i\sum_i\theta_i}
+\frac12\bar\eta e^{-i\sum_i\theta_i},
\]

which proves Equation (3).

### Coordinate covariance

Let

\[
U_i(\alpha_i)
=
|0\rangle\!\langle0|
+e^{i\alpha_i}|1\rangle\!\langle1|.
\tag{7}
\]

Then

\[
U_i(\alpha_i)M(\theta_i)U_i(\alpha_i)^\dagger
=
M(\theta_i+\alpha_i),
\]

while the coherence coordinate transforms as

\[
\eta\mapsto\eta e^{-i\sum_i\alpha_i}.
\]

Substitution proves Equation (3) invariant. A bare \(\eta\), a bare local
angle, or a bare claim that “all parties measured \(X\)” is coordinate
dependent. The observable is the relational combination.

### Collective-character quotient

Define

\[
\chi:U(1)^n\to U(1),
\qquad
\chi(\boldsymbol\alpha)
=e^{i\sum_i\alpha_i}.
\tag{8}
\]

The product-parity response depends on the local reference tuple only
through \(\chi\). Every zero-sum tuple is in \(\ker\chi\) and leaves the
response unchanged. The first isomorphism theorem gives Equation (5).

The operational requirement is therefore:

```text
not n absolute phases
not one observer's absolute phase
not a preferred spacetime foliation

but one physically usable collective phase relation
for the declared multipartite action
```

A shared oscillator or phase standard is one way to supply it. It is not the
only way.

## 3. Reference uncertainty and correlation-only glue

Let the actual local angle be

\[
\theta_i+\delta_i,
\]

where the unobserved reference-error vector has a frozen joint distribution
\(p(\boldsymbol\delta)\). Averaging Equation (3) gives

\[
\bar C
=
\operatorname{Re}
\left[
\eta e^{i\sum_i\theta_i}
\Gamma_p
\right],
\qquad
\Gamma_p
=
\mathbb E_p
\left[
e^{i\sum_i\delta_i}
\right].
\tag{9}
\]

\(\Gamma_p\) is the joint distribution's Fourier coefficient at the
collective character \((1,\ldots,1)\). It is not determined by the marginal
reference distributions.

### Independent errors

If

\[
p(\boldsymbol\delta)=\prod_ip_i(\delta_i),
\]

then

\[
\Gamma_p
=
\prod_i\mu_i,
\qquad
\mu_i
=
\mathbb E_{p_i}[e^{i\delta_i}].
\tag{10}
\]

One independently uniform local phase has \(\mu_i=0\) and closes this first
leak:

\[
\bar C=0.
\]

This is operational twirling. It is not physical destruction of the global
coherence. An expanded physical reference/calibration contract may reopen
it.

### Correlated-error positive control

For two regions, take

\[
\delta_1=T,
\qquad
\delta_2=-T,
\tag{11}
\]

with \(T\) uniform on \(U(1)\). Each local reference marginal is uniform:

\[
\mathbb E[e^{i\delta_1}]
=
\mathbb E[e^{i\delta_2}]
=0.
\]

But

\[
\Gamma_p
=
\mathbb E[e^{i(\delta_1+\delta_2)}]
=1.
\tag{12}
\]

The full joined response is unchanged.

This is the exact regional lesson:

> Absolute local reference quality can be zero while relational
> composability is perfect.

A composition rule based on multiplying local scalar “frame quality” scores
is valid only under an independently justified independence contract. It
fails on the smallest correlated control.

## 4. Fixed two-setting reconstruction

When the collective frame relation is stable, two target-independent
settings recover the complex relational coherence:

\[
\begin{aligned}
C_X
&=
\langle X^{\otimes n}\rangle
=\operatorname{Re}\eta,\\
C_Y
&=
\langle Y\otimes X^{\otimes(n-1)}\rangle
=-\operatorname{Im}\eta.
\end{aligned}
\tag{13}
\]

Hence

\[
\eta=C_X-iC_Y.
\tag{14}
\]

This avoids choosing a phase-matched measurement after learning \(\eta\).
It still presupposes:

1. stable local axis labels across repetitions;
2. a certified relation among those axes;
3. joined shot identity and outcome provenance; and
4. permission to aggregate all regional outcomes.

If an offset is fixed but unknown, additional calibration or
reference-frame-independent encodings may estimate or bypass it. Haar
twirling in Equation (9) represents a different contract: the relevant
relation is unobserved and randomized, or inaccessible under the admitted
reference symmetry. Do not turn an ordinary calibration problem into
physical decoherence.

## 5. Dephasing and reference quality are different types

Let independent local phase-damping channels multiply the off-diagonal
operator on region \(i\) by \(\lambda_i\). Then

\[
\eta
\mapsto
\eta\prod_i\lambda_i
\]

and the observed parity is

\[
\bar C
=
\operatorname{Re}
\left[
\eta e^{i\sum_i\theta_i}
\left(\prod_i\lambda_i\right)
\Gamma_p
\right].
\tag{15}
\]

The factors have different meanings:

| factor | type |
|---|---|
| \(\eta\) | coherence of the supplied global carrier |
| \(\prod_i\lambda_i\) | physical survival under the admitted local channels |
| \(\Gamma_p\) | access/reference relation under the admitted frame contract |
| \(e^{i\sum_i\theta_i}\) | chosen relational assay setting |

They multiply in this specimen but must not be identified.

### Exact attribution twin

Even the two quadratures in Equation (13) identify only the complex product

\[
z
=
\eta
\left(\prod_i\lambda_i\right)
\Gamma_p.
\tag{16}
\]

For example:

```text
completion A: eta = 0.8 + 0.2 i, dephasing/reference factor = 1
completion B: eta = 1 + 0.25 i, dephasing/reference factor = 0.8
```

Both give

\[
z=0.8+0.2i
\]

and therefore identical \(X^{\otimes n}\) and
\(Y\otimes X^{\otimes(n-1)}\) responses.

No number of repetitions of those same parity settings attributes the loss
to source coherence, physical dephasing, or reference misalignment.
Independent reference calibration, environment access, or a source-selective
intervention is required. This is the regional version of the attribution
null already exposed by `HC-DU-153`.

## 6. Why this is not consensus or a preferred frame

### Not consensus

The theorem concerns whether one quantum correlator is operationally
defined and accessible. It supplies no:

- fault model;
- validity rule;
- authenticated identity;
- adversarial safety;
- liveness;
- Byzantine threshold;
- metastable convergence;
- record formation; or
- public settlement rule.

Classical parity aggregation after local measurements is not a consensus
protocol. It assumes the measurement outcomes and their joined identities.

### Not law-of-large-numbers strengthening

Under independent identical reference quality

\[
|\mu_i|=r<1,
\]

the accessible correlation scales as

\[
r^n.
\tag{17}
\]

It decays smoothly and exponentially with the number of regions. More
participants do not make this coherence record more final or more public.
Correlated reference architecture can instead preserve it exactly.

### Not a global absolute frame

Equation (5) removes \(n-1\) local phase coordinates. The observable needs
one relational character, not an absolute origin. The result therefore gives
no support to a preferred foliation or globally accessible clock. A physical
global reference is sufficient but not forced.

## 7. Selected-versus-supplied ledger

| object | status |
|---|---|
| \(n\)-partite carrier and tensor factorization | supplied |
| coherence parameter \(\eta\) | supplied physical state coordinate |
| local equatorial controls | supplied |
| local frame carriers | supplied or absent |
| joint reference-error distribution \(p\) | supplied model |
| local dephasing factors \(\lambda_i\) | supplied channel parameters |
| parity-response law | derived |
| covariance and collective quotient | derived |
| correlation-only reference positive control | derived |
| two-setting relational-coherence reconstruction | derived conditionally |
| separation of dephasing from reference loss | not identified by parity alone |
| joined shot identity and provenance | supplied |
| physical reference selector | absent |
| record formation and retention | absent |
| fault/adversary and public-finality rule | absent |
| global actuality or new dynamics | not derived |

## 8. Literature collision and novelty

The component structure is mature:

- Mermin's GHZ analysis supplies the multipartite coherence architecture:
  [Phys. Rev. Lett. 65, 1838
  (1990)](https://doi.org/10.1103/PhysRevLett.65.1838).
- Hillery, Bužek, and Berthiaume use GHZ states for quantum secret sharing:
  [arXiv:quant-ph/9806063](https://arxiv.org/abs/quant-ph/9806063).
- Bartlett, Rudolph, and Spekkens review the operational consequences of
  missing or uncorrelated quantum reference frames, group twirling,
  superselection, and relational encodings:
  [arXiv:quant-ph/0610030](https://arxiv.org/abs/quant-ph/0610030).
- Skotiniotis and Gour treat \(U(1)\) phase-reference alignment and its
  relation to asymmetry:
  [arXiv:1202.3163](https://arxiv.org/abs/1202.3163).
- `HC-DU-035A/C`, `HC-DU-125`, and `HC-DU-153` already own the relevant DU
  threshold, correlation-glue, and reference-attribution controls.

No new GHZ theorem, quantum-reference-frame theorem, resource monotone,
measurement protocol, or empirical prediction is claimed.

The useful DU synthesis is:

```text
local quantum access
  + classical outcome aggregation
  is not yet
joined operational access;

joined access additionally requires
  a physically usable relational reference
  + joined provenance
  + a declared action class.
```

The synthesis corrects both extremes:

1. local pooling does not work merely because every participant can measure;
2. successful pooling does not require one absolute global frame.

## 9. North-Star consequence

The physical-selection problem has become one field more explicit. A complete
regional record/access packet must type:

```text
regional carrier
+ local instrument
+ relational reference certificate
+ joined occurrence/provenance identity
+ communication/aggregation route
+ action and resource class
+ finality/fault rule
```

The relational reference may itself be stored in correlations and need not
appear in any local record. That is a real architectural lesson for layered
regional finality.

It does not reopen the flagship. The present carrier, factorization,
references, controls, and aggregation are all supplied. The QEC
implementation-complete reopener remains unchanged.

## 10. Reproducibility

Run:

```bash
python3 tests/du_regional_reference_alignment_gate_probe.py \
  --write-artifact
```

The regression checks:

- the direct matrix/parity formula;
- the already-banked proper-coalition control;
- covariance under joint state/measurement frame transformation;
- the zero-sum reference kernel;
- independent-error factorization;
- complete loss under one independent uniform twirl;
- complete survival under locally uniform anticorrelated frames;
- fixed two-setting reconstruction;
- dephasing/reference multiplication;
- an exact attribution twin;
- smooth \(r^n\) scaling; and
- the wrong-basis/undephased-coherence control.

It does not simulate a laboratory or prove a physical source of reference
alignment.

## Final status

**BANKED SCOPED RESULT / THE OBVIOUS MULTIPARTITE ACCESS GENERALIZATION WAS
ALREADY BANKED AND WAS NOT REBUILT / A REGIONAL GHZ-PARITY RESPONSE DEPENDS
ONLY ON ONE COLLECTIVE \(U(1)\) CHARACTER / LOCAL FRAME TUPLES WITH ZERO
TOTAL PHASE ARE GAUGE FOR THAT RESPONSE / ONE INDEPENDENTLY TWIRLED REGION
CLOSES THE FIRST LEAK, WHILE LOCALLY UNIFORM BUT ANTICORRELATED FRAMES
PRESERVE IT EXACTLY / REFERENCE UNCERTAINTY AND PHYSICAL DEPHASING MULTIPLY
BUT REMAIN DIFFERENT TYPES AND ARE NOT ATTRIBUTED BY THE SAME TWO PARITY
QUADRATURES / A RELATIONAL REFERENCE CERTIFICATE, NOT AN ABSOLUTE GLOBAL
FRAME, IS THE MISSING COMPOSITION FIELD / STANDARD GHZ, QUANTUM REFERENCE
FRAME, ASYMMETRY, FOURIER, AND DEPHASING MATHEMATICS ABSORB THE COMPONENTS /
NO SELECTED REFERENCE, RECORD, CONSENSUS, PREFERRED FRAME, NEW PHYSICS,
PAPER, HARDWARE, OR READY SUCCESSOR.**
