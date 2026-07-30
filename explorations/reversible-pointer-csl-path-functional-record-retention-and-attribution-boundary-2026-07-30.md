---
title: "Reversible-pointer CSL path functional, record retention, and attribution boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-157
run_id: RUN-20260730-085704-reversible-pointer-csl-record-boundary
work_id: ANOMALY-REVERSIBLE-POINTER-CSL-FINALITY
action_id: RPCSL-01-REVERSIBLE-POINTER-RECORD-GATE
owner_repo: dynamic-unity
maximum_grade: 4
---

# Reversible-pointer CSL path functional

## Executive return

```text
ENDPOINT_PATH_NONFACTORIZATION
+ IRREVERSIBILITY_NEED_NOT_BE_A_RETAINED_POINTER_RECORD
+ TEMPORARY_WHICH_BRANCH_CORRELATION_NEED_NOT_SURVIVE
+ ONE_VISIBILITY_IDENTIFIES_ONLY_TOTAL_LOSS
+ MULTI_CONFIGURATION_ATTRIBUTION_HAS_AN_EXACT_RANK_GATE
+ CONDITIONAL_CSL_THEORY_CLASS_DISCRIMINATOR
+ STANDARD_COLLAPSE_DECOHERENCE_AND_IDENTIFIABILITY_ABSORPTION
+ SUPPLIED_APPARATUS_CALIBRATION_ACCESS_AND_PARAMETERS
+ NO OBSERVED RESULT NEW DU LAW HARDWARE ACTION PAPER OR READY SUCCESSOR
```

The new source gives Dynamic Unity a particularly clean hostile specimen.
A nanoparticle can temporarily carry which-branch information and then return
to the same position and momentum under both branches. Standard unitary
quantum mechanics predicts restored Ramsey visibility. Continuous
Spontaneous Localization (CSL) instead predicts an irreversible visibility
loss accumulated while the two mass distributions were separated.

This establishes a useful structural correction:

> A physical law can make a final response depend on a reversible pointer's
> entire trajectory even when the pointer retains no endpoint record of that
> trajectory.

That is not evidence that CSL is true, and it is not a Dynamic Unity
prediction. The cited source is a July 2026 preprint proposing an experiment,
not reporting one. It supplies the apparatus, force, trap, initial state,
collapse parameters, loss budget, calibration, and Ramsey readout. Standard
decoherence can also produce irreversible visibility loss without a retained
pointer value.

The exact Dynamic Unity gain is twofold:

1. **path dependence and record retention are independent coordinates**; and
2. **one endpoint visibility measures total loss, not its provenance**.

A credible theory-class attribution requires a no-refit response surface
across multiple apparatus configurations. That requirement has an exact rank
criterion.

## 1. Source status and declared scope

The primary specimen is Peter Renkel,
["Testing Continuous Spontaneous Localization by Coherently Simulating a
Measurement with a Nanoparticle"](https://arxiv.org/abs/2606.22707),
arXiv:2606.22707v4, revised July 21, 2026.

Its protocol has:

- a microscopic two-branch Ramsey source;
- opposite branch-conditioned forces on a charged trapped nanoparticle;
- a full harmonic cycle during which the pointer branches separate and
  recombine in position and momentum;
- a final Ramsey visibility measurement on the microscopic source; and
- a CSL prediction of coherence suppression accumulated during the
  separation.

The proposal is measurement-like because information is temporarily
transferred to a mesoscopic pointer. It deliberately reverses that transfer.
The final measured object is not a retained pointer label. It is the
microscopic Ramsey visibility after recombination.

The source reports projected sensitivity, not data. It states that the
proposal could substantially improve the **direct interferometric**
visibility-loss comparison while remaining weaker than the strongest
non-interferometric CSL bounds in important parameter regions. This run did
not independently validate its engineering feasibility or numerical
sensitivity curve. It audited the exact source equations and the record,
history, and attribution types.

## 2. The physical objects do not collapse into one record

| Object | Physical type | What the proposal supplies |
|---|---|---|
| \(D(t)\) | branch-conditioned pointer separation | controlled temporary correlation |
| pointer endpoint | position/momentum state after one trap cycle | branch paths recombined |
| \(\Lambda_{\rm CSL}\) | theory-dependent path-integrated coherence-loss exponent | conditional on CSL parameters and mass-density model |
| \(\Lambda_{\rm loss}\) | aggregate ordinary loss exponent | gas, blackbody, force, timing, field, and mismatch family |
| \(V\) | ensemble Ramsey visibility | final accessible statistic |
| one CSL noise history | primitive stochastic-theory history | not measured or retained by the proposed readout |
| apparatus choice | source, trap, force, geometry, preparation, control | supplied experimental design |
| provenance certificate | evidence identifying CSL rather than every admitted ordinary loss | not supplied by one visibility datum |

This yields the typed chain:

```text
temporary branch correlation
  -> coherent recombination of the pointer
  -> theory-dependent path-integrated loss
  -> final ensemble visibility
```

It is not:

```text
formed pointer outcome
  -> retained pointer archive
  -> certified record of a collapse occurrence.
```

Calling \(\Lambda_{\rm CSL}\) “memory” can also mislead. The standard CSL
master equation used by the source is Markovian. The final exponential
depends on an integral of instantaneous rates along the controlled path; no
separate accessible memory register is required.

## 3. Endpoint-return/path-functional nonfactorization

The branch separation in the ideal forced harmonic protocol is

\[
D(t)=\frac{F}{m\omega^2}(1-\cos\omega t),
\qquad
\tau=\frac{2\pi}{\omega}.
\]

At the endpoint:

\[
D(0)=D(\tau)=0,
\qquad
\dot D(0)=\dot D(\tau)=0.
\]

Thus the no-force protocol \(F=0\) and every nonzero-force protocol have the
same branch-separation endpoint record

\[
r_{\rm end}=(0,0).
\]

In the pointlike, small-separation CSL limit, the source gives

\[
\Gamma_{\rm CSL}(t)
\simeq
\lambda\frac{m^2}{4m_0^2r_c^2}D(t)^2.
\]

The path integral is

\[
\begin{aligned}
\int_0^\tau D(t)^2\,dt
&=
\frac{F^2}{m^2\omega^4}
\int_0^{2\pi/\omega}(1-\cos\omega t)^2\,dt\\
&=
\frac{F^2}{m^2\omega^5}
\int_0^{2\pi}(1-\cos u)^2\,du\\
&=
\frac{3\pi F^2}{m^2\omega^5}.
\end{aligned}
\]

Therefore

\[
\Lambda_{\rm CSL}
=
\lambda\frac{3\pi F^2}
{4m_0^2r_c^2\omega^5}.
\]

For \(\lambda>0\), it is zero at \(F=0\) and positive at \(F\ne0\), even
though \(r_{\rm end}\) is identical.

### Proposition 1 — endpoint nonfactorization

On the admitted protocol family, no function \(f\) satisfies

\[
\Lambda_{\rm CSL}=f(r_{\rm end})
\]

for all \(F\).

This is an exact same-endpoint/different-target witness. It is not a
same-**complete-record** witness: a control transcript containing \(F\),
\(\omega\), the elapsed cycle, and the mass-density model predicts the
conditional CSL exponent. The result says the returned pointer state is not
that transcript.

The source's finite-width treatment strengthens rather than removes this
structure. For an isotropic Gaussian mass distribution it gives

\[
\Gamma_{\rm CSL}^{3D}(t)
=
\lambda\frac{m^2}{m_0^2}
\left(1+\frac{\sigma^2(t)}{r_c^2}\right)^{-3/2}
\left[
1-\exp\!\left(
-\frac{D^2(t)}
{4(r_c^2+\sigma^2(t))}
\right)
\right].
\]

This remains a trajectory functional of \(D(t)\) and the breathing width
\(\sigma(t)\), not a function of the recombined endpoint alone.

## 4. Irreversibility does not imply a retained pointer archive

Under ideal unitary dynamics, temporary entanglement reduces the microscopic
subsystem's intermediate coherence. At the full trap period the pointer
disentangles, its two phase-space paths close, and the Ramsey contrast
returns. The source explicitly distinguishes this “false decoherence” from
the CSL signal.

Under CSL, the endpoint coherence is modeled as

\[
\rho_{+-}(\tau)
=
\rho_{+-}(0)
e^{-\Lambda_{\rm CSL}}
e^{-\Lambda_{\rm loss}},
\]

so the final visibility is

\[
V=V_0e^{-\Lambda_{\rm CSL}}e^{-\Lambda_{\rm loss}}.
\]

The pointer can therefore have:

- no surviving branch-conditioned displacement;
- no retained pointer label;
- no endpoint token saying which temporary path occurred; and
- a theory-dependent irreversible effect on later visibility.

### Proposition 2 — retained-record implication failure

In the declared CSL protocol:

\[
\text{irreversible visibility loss}
\not\Rightarrow
\text{retained accessible pointer record}.
\]

The converse also fails in ordinary measurement models: unitary dynamics
plus environmental amplification can create a stable accessible record
without CSL. Dynamic Unity must therefore keep at least four coordinates:

\[
\text{temporary correlation},
\quad
\text{single-run actuality},
\quad
\text{irreversible response},
\quad
\text{retained accessible provenance}.
\]

This corrects any one-axis model in which “more final” automatically means
“more recorded.” It does not show that objective collapse lacks an ontic
history. A complete CSL ontology may contain a stochastic history not
available through this apparatus. The result is specifically about retained
pointer and observer-accessible records.

## 5. One visibility identifies total loss, not CSL provenance

Define

\[
y=-\log(V/V_0).
\]

The source model gives

\[
y=\Lambda_{\rm CSL}+\Lambda_{\rm loss}.
\]

With one apparatus configuration and an admitted unknown ordinary-loss
scalar, every candidate CSL contribution can be traded against ordinary
loss. More shots narrow the estimate of \(y\); they do not separate its two
summands.

This is an attribution obstruction, not a claim that CSL is untestable.
Controls and multiple configurations can make the CSL response shape
independent of a frozen nuisance family.

### Theorem 3 — no-refit attribution rank

For \(n\) frozen configurations, let

\[
y=\lambda K(r_c)+B\theta,
\]

where:

- \(K(r_c)\in\mathbb R^n\) is the CSL response predicted from the controlled
  paths and widths;
- \(B\in\mathbb R^{n\times p}\) is a preregistered ordinary-loss design; and
- \(\theta\) is an unknown nuisance vector.

At fixed \(r_c\), \(\lambda\) is locally identifiable exactly when

\[
K(r_c)\notin\operatorname{col}(B).
\]

**Proof.** If \(K\in\operatorname{col}(B)\), write \(K=Bc\). Then
\((\lambda,\theta)\) and \((0,\theta+\lambda c)\) produce the same \(y\).
If \(K\notin\operatorname{col}(B)\), its class in the quotient
\(\mathbb R^n/\operatorname{col}(B)\) is nonzero, and projecting \(y\) to
that quotient determines \(\lambda\). \(\square\)

For nonzero \(\lambda\), joint local identification of \((\lambda,r_c)\)
requires

\[
\operatorname{rank}
\left[
B\ \ K(r_c)\ \ \lambda\partial_{r_c}K(r_c)
\right]
=
\operatorname{rank}(B)+2.
\]

At \(\lambda=0\), \(r_c\) is unidentifiable because its derivative direction
vanishes. A null experiment therefore constrains a curve or region in
\((\lambda,r_c)\) rather than selecting one correlation length.

### Experimental-design consequence

A serious no-refit packet should deliberately vary controls that change the
CSL kernel differently from the admitted nuisance family—for example:

- source force \(F\);
- trap frequency \(\omega\);
- pointer width/breathing profile \(\sigma(t)\);
- mass distribution or geometry; and
- source-off and zero-separation controls.

The nuisance basis must be frozen before looking at the result. Adding a new
loss direction after seeing the data can always erase attribution. Conversely,
declaring every ordinary loss perfectly known would manufacture it.

## 6. Collision with prior Dynamic Unity results

### `HC-DU-081`

The earlier GRW audit credited apparatus-relative outcome formation while
showing that collapse does not select the apparatus, coarse graining,
archive, access, or provenance. The present specimen adds the complementary
case: collapse-sensitive irreversible response without a retained pointer
outcome.

### `HC-DU-142`

The prior thermodynamic packet separated:

```text
formation
!= single-run actualization
!= retained accessible provenance.
```

The reversible pointer adds a fourth independent coordinate:

```text
irreversible path-dependent response.
```

No one of the four can replace the others.

### `HC-DU-154`

The QRF/quantum-erasure fixture showed that temporary branch information can
be coherently removed unless an inaccessible copy survives. The CSL proposal
uses the same reversible-pointer shape but changes the dynamics: a
fundamental nonunitary law can suppress the later visibility even when no
ordinary branch copy remains. This is a theory-class delta conditional on
CSL, not a new Dynamic Unity mechanism.

### `HC-DU-156`

The CSL master equation selects a stochastic law only after its parameters
and mass-density coupling are postulated. The proposed experiment supplies
the sampler-facing apparatus and reports an ensemble visibility. It does not
make the stochastic history an accessible archive. The

```text
law -> realization -> formed record -> access
```

ladder therefore remains necessary.

## 7. Absorber and novelty audit

The component physics is mature:

- GRW and CSL are established objective-collapse model classes;
- collapse-induced visibility loss and mass/separation scaling are standard
  CSL phenomenology;
- trapped-particle and matter-wave collapse tests already exist;
- reversible entanglement and coherence revival are standard unitary
  controls;
- ordinary decoherence also accumulates along a path without leaving a
  pointer label; and
- rank-based parameter identifiability is standard inverse-problem and
  experimental-design mathematics.

The 2026 source appears to contribute a concrete reversible mesoscopic
pointer architecture and projected direct-interferometric reach. Dynamic
Unity does not claim priority for that protocol or its CSL prediction.

The scoped DU contribution is the typed integration:

```text
returned endpoint state
!= controlled path transcript
!= irreversible response
!= retained pointer archive
!= stochastic-history provenance
!= theory attribution.
```

That is useful because it blocks two opposite mistakes:

- treating every irreversible physical effect as a record; and
- treating the absence of a retained pointer value as the absence of a
  measurable history-dependent theory delta.

## 8. Conditional prediction packet

The source supplies a real conditional discriminator:

> For fixed nonzero CSL parameters \((\lambda,r_c)\), a frozen reversible
> pointer protocol has a final Ramsey visibility reduced by
> \(e^{-\lambda K(r_c)}\) relative to the matched ordinary-quantum prediction,
> after ordinary loss is independently controlled.

This is:

- quantitative;
- dimensioned;
- locally calculable before hardware;
- testable by a direct visibility measurement; and
- not a Dynamic Unity-original physical law.

Its proper kill is conditional. A frozen parameter point is excluded if the
measured no-refit response surface is incompatible with its predicted
kernel after the preregistered nuisance family and uncertainty budget pass.
A null does not eliminate CSL with free \((\lambda,r_c)\); it excludes a
region.

The proposal itself remains unexecuted. Its projected sensitivity does not
surpass the strongest existing non-interferometric bounds near several
benchmarks, although it may strengthen the direct interferometric class.
No hardware action follows from this audit.

## 9. Grade and disposition

**Earned:** scoped Grade 4 endpoint/path nonfactorization, retained-record
implication failure, and no-refit attribution-rank theorem.

**Conditionally preserved:** one imported Grade-5-shaped CSL theory-class
discriminator.

**Not earned:** evidence for CSL, a detected anomaly, a Dynamic Unity law,
record-first ontology, objective-finality mechanism, selected apparatus,
run-level collapse certificate, accessible stochastic history, external
hardware need, paper promotion, or ready scientific successor.

The physical-record interface-selection reopener is not met. The source
chooses a useful apparatus; the collapse law does not select it. The program
remains quiescent.

## 10. Reopen rule

Reopen this packet only for one of:

1. a preregistered multi-configuration experiment whose CSL kernel adds rank
   beyond a complete frozen ordinary-loss family;
2. observed no-refit data with retained calibration and attempt lineage;
3. a physical derivation selecting the apparatus, collapse parameters,
   archive, and observer access rather than supplying them; or
4. a distinct modified-dynamics model whose response surface survives the
   same controls and makes a competing quantitative prediction.

Do not reopen for another single visibility estimate, a larger local
simulation of the supplied equations, or a claim that any irreversible loss
is itself a record.

## Primary sources

- Peter Renkel,
  ["Testing Continuous Spontaneous Localization by Coherently Simulating a
  Measurement with a Nanoparticle"](https://arxiv.org/abs/2606.22707)
  (2026 preprint).
- Angelo Bassi, Kristian Lochan, Seema Satin, Tejinder P. Singh, and Hendrik
  Ulbricht,
  ["Models of wave-function collapse, underlying theories, and experimental
  tests"](https://arxiv.org/abs/1204.4325).
- Angelo Bassi, Mauro Dorato, and Hendrik Ulbricht,
  ["Collapse Models: A Theoretical, Experimental and Philosophical
  Review"](https://arxiv.org/abs/2310.14969).
- C. Wan et al.,
  ["Free Nano-Object Ramsey Interferometry for Large Quantum
  Superpositions"](https://arxiv.org/abs/1511.02738).
- Sandro Donadi et al.,
  ["Novel CSL bounds from the noise-induced radiation emission from
  atoms"](https://arxiv.org/abs/1710.01973).
