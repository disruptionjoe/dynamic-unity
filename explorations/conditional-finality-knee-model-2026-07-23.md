---
title: "SWING-DU-SCI-01 Track 3 — conditional finality knee: quantitative fidelity scaling and hysteresis, with a smooth-null identifiability limit"
status: active_research
doc_type: exploration
created: 2026-07-23
lanes: "2.2 / 4.1 / A.1"
swing: SWING-DU-SCI-01
candidate_id: DU.SCI01.TRACK3.FINALITY-KNEE
probe: tests/du_conditional_finality_knee_probe.py
artifact: tests/artifacts/du_conditional_finality_knee_probe_result.json
verdict: "CONDITIONAL_MODEL_ONLY_IDENTIFIABILITY_LIMITED — the labeled information-threshold and persistence posits entail a quantitative fidelity-dependent crossing and post-erasure history surface, but a freely steep smooth irreversible-dephasing law absorbs any finite-grid knee. A knee inserted by hand is not a novel prediction."
grade: "conditional construction; exact finite-unitary positive control; threshold consequences derived relative to explicit posits; no microscopic mechanism, abductive preference, banking, or claim-status change"
---

# Conditional finality-knee model

## Result

The swing gets a real conditional model, but not a finality discovery.

For independent imperfect pure records with single-record branch fidelity

\[
F=\left|\langle e_0|e_1\rangle\right|^2,
\]

ordinary unitary quantum mechanics gives

\[
V_{\rm unitary}(R,F)=F^{R/2}.
\]

An exact inverse of all record interactions restores \(V=1\) at every finite \(R\).
The probe constructs that circuit explicitly and verifies the visibility formula to
\(4.44\times10^{-16}\) and exact erasure to \(9.99\times10^{-16}\).

The **conditional posit** is a sharp, persistent finality event at additive branch
information

\[
M(R,F)=-R\ln F\ge M_c.
\]

The runnable specimen imports \(M_c=2\) nats and complete post-crossing loss
\(q=0\). Given those insertions, it entails

\[
R_c(F)=\left\lceil\frac{M_c}{-\ln F}\right\rceil
\quad\text{and}\quad
V_c=e^{-M_c/2}
\]

at the continuous crossing. Thus the record count at the knee must move with
single-record fidelity, while the pre-finality unitary visibility at the continuous
knee remains common across fidelities. This is more informative than saying merely
"there is a knee," but it remains information **conditional on the chosen trigger
law**.

## Non-ordinal warrant ledger

| Warrant | What this build earns | What it does not earn |
|---|---|---|
| `DERIVED` | \(V=F^{R/2}\), exact inverse recovery, \(R_c(F)\), the common continuous-knee visibility, and the integer overshoot bound follow from the stated finite-record model and threshold rule. | The threshold rule or its physical origin. |
| `CONDITIONALLY_ENTAILED` | A persistent threshold at \(M_c\) implies the displayed fidelity scaling and forward/backward recoverability surface. | An unconditional prediction of Dynamic Unity. |
| `CONSTRUCTIVELY_REALIZED` | A finite-dimensional record circuit, exact eraser, threshold trajectory, reversal protocol, and null comparisons are executable. | An AQFT-local, Lorentz-covariant physical update. |
| `ABDUCTIVELY_PREFERRED` | **Not earned.** The specimen beats a fixed-rate exponential null and a count-only threshold on declared comparisons. | A freely steep smooth irreversible null absorbs the finite-grid knee. |

The warrant types answer different questions; the first three do not add up to the
fourth.

## Model and observable

The standard which-path state is

\[
|\Psi_R\rangle =
\frac{|0\rangle|e_0\rangle^{\otimes R}+
|1\rangle|e_1\rangle^{\otimes R}}{\sqrt 2}.
\]

Tracing out the records multiplies path coherence by
\(\langle e_0|e_1\rangle^R\). The model tracks two observables separately:

1. **Raw visibility:** visibility before undoing record formation.
2. **Recoverable visibility:** visibility after applying the calibrated inverse of
   every record interaction.

Standard unitary dynamics suppresses the first but restores the second to one. The
conditional model inserts a monotone finality flag:

\[
V_{\rm erase}^{\rm conditional} =
\begin{cases}
1,& \max_{\rm history}M<M_c,\\
q,& \max_{\rm history}M\ge M_c.
\end{cases}
\]

The maximum-over-history is not a result. It is precisely where irreversibility is
inserted.

## Threshold location versus record fidelity

For the illustrative \(M_c=2\) nats:

| \(F\) | information per record \(-\ln F\) | continuous \(R_c\) | first integer crossing | standard \(V\) at first crossing |
|---:|---:|---:|---:|---:|
| 0.20 | 1.60944 | 1.243 | 2 | 0.200000 |
| 0.40 | 0.91629 | 2.183 | 3 | 0.252982 |
| 0.60 | 0.51083 | 3.915 | 4 | 0.360000 |
| 0.80 | 0.22314 | 8.963 | 9 | 0.366357 |
| 0.90 | 0.10536 | 18.982 | 19 | 0.367539 |
| 0.95 | 0.05129 | 38.991 | 39 | 0.367799 |
| 0.98 | 0.02020 | 98.997 | 99 | 0.367867 |

The continuous value is \(V_c=e^{-1}=0.367879\). Integer record counts can only
cross after an overshoot. The exact bound

\[
e^{-M_c/2}\sqrt F < V(R_c,F)\le e^{-M_c/2}
\]

holds in all seven cases.

This supplies a useful conditional test:

- a threshold on **raw record count** calibrated at \(F=0.8\) predicts
  \(R_c=9\) for every fidelity;
- the information-threshold specimen predicts \(R_c=2,3,4,9,19,39,99\).

One fidelity cannot distinguish these trigger choices. The seven-fidelity scan
separates them in six of the other six cases.

## Recoverability and hysteresis

At \(F=0.8\), the illustrative crossing is \(R_c=9\). The probe accumulates twelve
records, crosses the threshold, and then exactly uncomputes every record interaction.
Both the initial and returned configurations have current \(M=0\):

- standard unitary comparator after erasure: \(V=1\);
- conditional model before any crossing: \(V=1\);
- conditional model after a past crossing and complete erasure: \(V=q=0\).

The conditional hysteresis gap is therefore one in the strong \(q=0\) specimen.
This rejects ordinary global unitary reversibility **if observed**, but it does not
uniquely diagnose finality. A memoryful irreversible environment can also remember
maximum exposure.

## Smooth-null comparison and the absorption control

The primary smooth irreversible-dephasing null is

\[
V_{\rm smooth}(M_{\max})=e^{-\lambda M_{\max}},
\]

calibrated here to \(V_{\rm smooth}(2M_c)=0.05\). It predicts:

| exposure | conditional recovery | smooth recovery |
|---:|---:|---:|
| \(0.5M_c\) | 1.000 | 0.4729 |
| \(0.99M_c\) | 1.000 | 0.2270 |
| \(1.00M_c\) | 0.000 | 0.2236 |
| \(1.50M_c\) | 0.000 | 0.1057 |
| \(2.00M_c\) | 0.000 | 0.0500 |

Across \(0\le M\le2M_c\), the RMSE is 0.384 and the maximum gap is 0.776.
At model level, the distinction is exact: the conditional specimen is flat below
\(M_c\) and discontinuous at \(M_c\); a fixed-rate null is smooth and loses
recoverability below \(M_c\).

The hostile absorption control then removes the easy win. It fits

\[
V_{\rm absorb}(M_{\max})=
\frac{1}{1+\exp[k(M_{\max}-M_0)]}
\]

on the entire finite seven-fidelity grid. With no independent upper bound on \(k\),
a slope \(k=652.18\,{\rm nat}^{-1}\) fits the inserted step with maximum error
0.00138, comfortably below the declared 1% measurement resolution.

**Identifiability verdict:** a knee, fidelity collapse, and exposure-history effect
can all be reproduced by a sufficiently steep smooth memoryful law formulated on
the same information statistic. Finite data cannot establish a mathematical
discontinuity without an independently motivated slope bound or an additional
mechanism-specific observable.

## Inserted, entailed, and still open

| Epistemic role | Contents |
|---|---|
| **Inserted** | \(M=-R\ln F\) as the physical trigger statistic; \(M_c=2\) nats; sharp crossing; persistence after inverse dynamics; \(q=0\). |
| **Entailed given those insertions** | \(R_c(F)\); common continuous-knee visibility; integer overshoot interval; the forward/backward post-erasure surface; separation from a raw-count threshold and fixed-rate exponential null. |
| **Not entailed** | Microscopic finality; the values of \(M_c\) or \(q\); AQFT locality; covariance of the threshold update; Born selection; single outcome; a novel prediction merely from observing a knee. |

The existing covariant-finality work remains a structural comparator only. It shows
that causal-order finality need not smuggle a foliation on a finite causal-set toy,
but its AQFT-local update is unbuilt. This threshold specimen therefore inherits the
locality-of-update proviso; it does not discharge it.

## Commercial candidate surface

The shared conditional-candidate harness records:

- 5 labeled assumptions;
- 4 visible free choices, each with a sensitivity test;
- 5 observables, 4 comparators, 3 null models, and 5 falsifiers;
- 8/8 executable checks passing;
- admission `CONDITIONAL_CANDIDATE`;
- `scientific_endorsement: false`.

Contract completeness means the candidate is legible and comparable, not true.
The JSON artifact is the machine-readable surface for subsequent cross-track
comparison.

## Heterodox preservation and failure scope

This specimen tests one member of a broader finality family:

> independent pure records + additive \(-\ln F\) information + a sharp persistent
> threshold.

Failure of \(R_c(F)=\lceil M_c/[-\ln F]\rceil\) closes or revises **this
formalization**. It does not by itself disprove every redundancy statistic, correlated
record model, or finality concept. Conversely, replacing the statistic after every
failure without preserving a predeclared finality invariant would be story-shopping,
not heterodox preservation.

## Decision and stop conditions

**Grade: `CONDITIONAL_MODEL_ONLY / IDENTIFIABILITY_LIMITED`.** No claim is banked,
seeded, or promoted.

The best next discriminating protocol, if this track is revisited, is a
multi-fidelity exact-erasure matrix with:

1. \(F\) calibrated independently;
2. dense tuning through \(F_c(R)=e^{-M_c/R}\) at several fixed \(R\);
3. forward and reversal sweeps;
4. an independently justified upper bound on smooth irreversible-dephasing slope;
5. the existing no-signaling and causal-locality controls.

Stop calling the feature finality if the result is only a fitted knee with an
unbounded smooth absorber. Stop the independent-record formalization if modest
correlations destroy its cross-fidelity law. Do not add a new \(M_c\), \(q\), or
trigger statistic after each failed scan. A physical prediction remains gated on a
mechanism that selects the trigger and scale and implements the update locally.

## Reproduction

From the repository root:

```bash
.venv/bin/python tests/du_conditional_finality_knee_probe.py
```

The deterministic artifact is
`tests/artifacts/du_conditional_finality_knee_probe_result.json`.
