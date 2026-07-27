---
title: "Locked pre-data prediction for the frozen QND-memory hardware suite"
date: 2026-07-26
locked_at_utc: 2026-07-27T00:25:32Z
status: LOCKED_PRE_DATA__NOT_EXECUTED
prediction_id: PRED-DU-004
protocol_id: du-qnd-memory-causal-break/0.1
lanes:
  - lane_7
  - lane_A
channels:
  - CH-EMPIRICAL
  - CH-PAPER
claim_grade: "registered analytic standard-quantum prediction for one frozen provider-conditional protocol; no hardware evidence or new-physics claim"
---

# Locked pre-data prediction for the frozen QND-memory hardware suite

## Lock statement

Dynamic Unity locks the following prediction **before any hardware execution
or hardware data inspection**:

> In the frozen 19-circuit QND-memory suite, the deliberately incomplete
> pointer record will fail to reconstruct the held-out binary response; the
> formed environment record will repair that failure exactly in the ideal
> ordinary-quantum model; and resetting the three declared qubits will remove
> pre-break-history dependence from the post-break reset-witness,
> environment, and output registers.

This is the expected **ordinary quantum mechanics** branch. It is not a
prediction of a new Dynamic Unity law. Its value is prospective: the exact
content is fixed before data and can later be cited whether the experiment is
run, returns the expected result, returns a surprise, or is never run.

The first public Git commit containing this document is the content-binding
lock. The commit hash binds the text and the public push supplies ordinary
public provenance. Neither is described as a trusted third-party timestamp.

## Pre-data and execution state

| Item | Locked state |
|---|---|
| Hardware job | Not submitted |
| Hardware result | None seen |
| Provider/account access in this run | None |
| Protocol | `du-qnd-memory-causal-break/0.1` |
| Source revision before the lock | `6cff2b354676` |
| Driver SHA-256 | `7aec5321e1aa54603bded82cb4c00de6bcd2e0965cba341af9502816e3c08294` |
| Pointer angle | \(\pi/2\) |
| Circuit-order seed | `271828` |
| Circuits | `19` |
| Planned shots | `256` per circuit; `4864` requested in total |
| Semantic-manifest SHA-256 | `9f118bf1736d6adbd9e1cd39985fc4b9d273307da98c7f1f4d649eb5bff555d5` |
| Evidence ceiling of a normal cloud run | `RETURNED_SHOT_CONDITIONAL_ONLY` |

Changing the driver, circuit semantics, pointer angle, analysis split, or
manifest creates a new protocol and cannot be reported as execution of this
exact lock.

## Exact ideal prediction

Let:

- \(h\in\{0,1\}\) be the prepared history;
- \(a=0\) be `identity_z` and \(a=1\) be `flip_z`;
- \(P\) be the one-bit pointer candidate record;
- \(E\) be the formed environment record; and
- \(Y\) be the held-out response.

The circuit prepares basis-state histories, copies \(h\) into \(E\), applies a
controlled \(R_y(\pi/2)\) to the pointer, measures the pointer, and then
applies the declared response intervention. Ordinary quantum mechanics gives

\[
E=h,\qquad Y=h\oplus a,
\]

and

\[
\Pr(P=0\mid h=0)=1,
\qquad
\Pr(P=0\mid h=1)=\Pr(P=1\mid h=1)=\frac12.
\]

Equivalently, the nonzero conditional probabilities are:

| History \(h\) | Intervention \(a\) | Pointer \(P\) | Environment \(E\) | Output \(Y\) | Probability |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | \(1\) |
| 0 | 1 | 0 | 0 | 1 | \(1\) |
| 1 | 0 | 0 | 1 | 1 | \(1/2\) |
| 1 | 0 | 1 | 1 | 1 | \(1/2\) |
| 1 | 1 | 0 | 1 | 0 | \(1/2\) |
| 1 | 1 | 1 | 1 | 0 | \(1/2\) |

The readout-calibration circuits ideally return the prepared bit. Each
prepare-one/reset calibration ideally returns reset witness zero.

## Locked consequences

### LP-1 — pointer-only reconstruction fails

At fixed intervention and pointer value \(P=0\), both histories occur, while
their output laws are disjoint. Therefore

\[
\operatorname{TV}
\bigl(
P(Y\mid h=0,a,P=0),
P(Y\mid h=1,a,P=0)
\bigr)=1.
\]

For equal allocation over the two histories and two interventions, the ideal
Bayes error using only \((P,a)\) is

\[
e_{P}=\frac14,
\]

so its ideal maximum accuracy is \(3/4\).

### LP-2 — the environment record repairs the failure

Because \(E=h\), the refined record \((P,E)\) determines

\[
Y=E\oplus a.
\]

Its ideal Bayes error is

\[
e_{P,E}=0,
\]

and the ideal accuracy gain from adding the formed environment is

\[
e_P-e_{P,E}=\frac14.
\]

The corresponding conditional entropies are

\[
H(Y\mid P,A)=0.6887218755408673\ {\rm bits},
\qquad
H(Y\mid P,E,A)=0.
\]

This is record refinement inside the declared circuit model, not evidence
that records are ontologically fundamental.

### LP-3 — the declared three-qubit causal-break response is history-free

The causal-break arm resets all three declared qubits, measures the reset
witness, resets them again, and reads environment and output. The ideal
post-break response is

\[
(\texttt{reset\_witness},E,Y)=(000,0,0)
\]

for both pre-break histories. Its ideal cross-history total-variation
distance is zero.

The pointer was measured **before** the reset and its classical archive is
intentionally retained. LP-3 therefore concerns the post-break response
registers just named; it does not claim that every classical trace of the
past vanished. A normal provider run also does not expose or reset every
provider-controller and environmental memory.

### LP-4 — no anomalous residual is predicted

Under the frozen standard model, a calibrated residual after the declared
three-qubit break is attributed first to readout, reset, drift, route,
selection, controller, or other retained-memory effects. This lock predicts
no finality residual and does not instantiate the extra physical state assumed
by `PRED-DU-003`.

## Future hardware adjudication contract

If Joe later authorizes a provider run, the primary held-out estimands remain:

\[
e_P,\qquad e_{P,E},\qquad e_P-e_{P,E},
\]

estimated by fitting only on the training circuit identities and scoring only
on the held-out identities, without refitting the record or response rule.
The causal-break estimand is the cross-history distance between the joined
`(reset_witness, environment, output)` returned-shot distributions.

The expected direction is locked:

```text
pointer-only error > pointer-plus-environment error
pointer-plus-environment error approximately calibration-limited
post-break response history distance approximately reset/calibration-limited
```

The numeric hardware acceptance tolerances are **not** frozen here. They
depend on a selected backend, shot-power calculation, simultaneous
uncertainty rule, and calibration/systematics model. Those must be locked in a
separate preregistration before submission and before hardware results are
seen. They may not be selected after looking at the outcome.

Any standard cloud result remains conditional on the returned-shot
population. It cannot establish complete-process factorization because the
provider interface does not certify every physical trigger, rejected attempt,
selection reason, or retained controller/environment memory.

## Falsification and interpretation

The analytic prediction is refuted for the frozen ideal circuit if an exact
derivation or faithful noiseless execution disagrees with the table above.

A hardware mismatch does not automatically refute quantum mechanics or
support Dynamic Unity. It first triggers the frozen calibration, drift,
selection, routing, reset, and implementation audit. Only a residual that
survives an independently complete rival and memory boundary could advance a
physical-remainder claim; a normal provider packet cannot reach that grade.

## Publication posture

This artifact may later be cited in a paper as a dated pre-data prediction or
protocol proposal even if no hardware job is ever run. Honest wording is:

> “The analytic prediction and its interpretation were publicly locked before
> hardware execution; no hardware result was used in formulating it.”

If the experiment remains unrun, the paper must say so. The lock is not an
experiment result, not a completed preregistration of backend-specific
statistics, not a novelty claim, and not publication authorization.

## Pointers

- [acquisition bridge](acquisition-visibility-and-hardware-bridge-2026-07-26.md)
- [prediction register](prediction-register.md)
- [acquisition driver](../lab/acquisition/ibm_runtime_du_acquisition.py)
- [driver guide](../lab/acquisition/README.md)
- [provider-capture schema](../specs/physical-sufficiency-provider-capture-v0.1.schema.json)
- [strict scientific packet schema](../specs/physical-sufficiency-acquisition-packet-v0.1.schema.json)
