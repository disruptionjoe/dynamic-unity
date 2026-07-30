---
title: "Source-pinned coupling response rank — run plan"
status: completed
doc_type: governed_run_plan
created: 2026-07-30
run_id: RUN-20260730-114651-source-pinned-coupling-rank
work_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
action_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Source-pinned coupling response rank

## Cold-start contract

- **Purpose:** make physical reality intelligible as one coherent,
  evidence-accountable whole.
- **North Star:** determine which target-blind physical antecedents select
  material, provenance-bearing, observer-indexed record interfaces, then test
  reconstruction and finite remainder.
- **Earned input:** `HC-DU-160` identifies coupling and readout algebra as
  scoped formal-instrument frontier coordinates while keeping action class as
  the base index.
- **Action:** Joe's `Go` activates only Swing 3,
  `MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK`.

## Source-pinned platform

Use only the sequential superconducting-qubit measurement platform of
Peronnin, Marković, Ficheux, and Huard,
["Sequential dispersive measurement of a superconducting
qubit"](https://arxiv.org/abs/1904.04635), *Physical Review Letters* 124,
180502 (2020).

The physical packet includes:

- Nb-on-Si coplanar-waveguide readout and buffer resonators;
- Al/AlOx/Al Josephson elements and a Josephson ring modulator;
- a pump-controlled beam-splitter coupling
  \(H_{\rm bs}=\hbar(gb^\dagger r+g^*br^\dagger)\);
- independently measured readout and buffer decay rates;
- residual readout-mode photon-number calibration;
- a complex calibrated buffer-output voltage trace; and
- a supplied preparation/readout/action protocol.

No other platform may repair a failed result in this run.

## Exact question

Does varying the physically calibrated pump coupling \(g(t)\) produce a
response direction outside the complete frozen nuisance span? What is the
smallest response packet that identifies it without refitting?

## Frozen local model

At the center of a symmetric pump pulse, choose phase so \(g>0\),
\(\dot g=0\), and take

\[
r(0)=A\ne0,\qquad b(0)=0.
\]

In the source's two-mode calibrated regime:

\[
\dot r=-igb-\frac{\kappa_r}{2}r,
\qquad
\dot b=-igr-\frac{\kappa_b}{2}b.
\]

The response packet is:

1. normalized residual readout population slope;
2. phase-calibrated initial buffer-output slope; and
3. phase-calibrated buffer-output curvature.

The source measures residual readout population and complex output traces in
matched calibration arms. This run does not claim simultaneous one-run access.

## Frozen nuisance contract

Independently calibrate or hold fixed:

- initial readout amplitude and phase;
- \(\kappa_r\) and \(\kappa_b\);
- pump envelope, phase, and digitizer time origin;
- carrier detunings and the selected flux point;
- dispersive and Kerr parameters in the release arm;
- detector gain, phase, DC offset, and efficiency;
- qubit preparation and state;
- pulse duration and action class; and
- admitted parasitic-mode model.

The two-mode positive is restricted to the source's calibrated low-pump
regime. Strong-pump points at which effective \(\kappa_b\), effective \(g\),
or unmonitored modes must be refit are a no-refit failure, not positive
evidence.

## Pre-registered returns

```text
MATERIAL_RESPONSE_RANK
SINGLE_OUTPUT_NONIDENTIFIABILITY
LAW_ONLY_EXPLANATION
KNOWN_RESULT_ABSORPTION
STRONG_COUPLING_NO_REFIT_FAILURE
```

## Exact discriminator

With normalized responses

\[
y_1=\frac{d}{dt}\frac{|r|^2}{|A|^2}\Big|_0,
\qquad
y_2=i\frac{\dot b(0)}{A},
\qquad
y_3=-i\frac{\ddot b(0)}{A},
\]

test the Jacobian with respect to
\((g,\kappa_r,\kappa_b)\). The coupling is locally identifiable against the
declared loss nuisances exactly when its column is outside their span.

## Positive and controls

- **Positive:** the three-response Jacobian has full rank for \(g\ne0\).
- **Negative control:** any one scalar endpoint has response-space dimension
  one, so a coupling and an admitted loss coefficient are locally confounded.
- **Exact witness:** in the weak-coupling terminal model
  \(\Gamma=\kappa_r+4g^2/\kappa_b+\kappa_p\), two distinct
  \((g,\kappa_p)\) pairs with equal \(\Gamma\) give the same residual endpoint.
- **No-refit control:** source-reported strong-pump discrepancies that require
  effective \(\kappa_b\), effective \(g\), or parasitic modes do not inherit
  the low-pump rank result.

## Grade and scope

- Maximum Grade 4 for a source-pinned physical coordinate and exact
  necessity/rank boundary.
- No Grade 5: no anomalous response, new law, physical remainder, or
  prediction is available.
- Expected strongest absorbers: passive linear quantum-system
  identifiability, quantum input-output theory, classical observability,
  Fisher/rank design, and the source paper's own coupling calibration.

## Stops

Stop without Swing 4 if:

- the coupling column lies in the frozen nuisance span;
- the positive requires per-condition gain, timing, decay, or mode refits;
- the source lacks the two required response channels;
- the result is only terminal-fidelity optimization; or
- hardware is required before the exact rank boundary can be learned.

If a scoped rank survives, bank it and leave Swing 4 prepared but inactive.

## Durable output

`explorations/source-pinned-sequential-readout-coupling-response-rank-and-strong-pump-boundary-2026-07-30.md`
