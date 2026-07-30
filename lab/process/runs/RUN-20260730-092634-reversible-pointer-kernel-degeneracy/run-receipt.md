---
title: "Reversible-pointer CSL quadratic-kernel attribution gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 09:35:00 CDT"
run_id: RUN-20260730-092634-reversible-pointer-kernel-degeneracy
work_id: ANOMALY-CSL-PATH-KERNEL-ATTRIBUTION
action_id: RPCSL-02-QUADRATIC-KERNEL-DEGENERACY-GATE
claim_id: HC-DU-158
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Reversible-pointer CSL quadratic-kernel attribution gate

## Disposition

```text
EXACT_QUADRATIC_PATH_DEGENERACY
+ FORCE AMPLITUDE CANNOT SUPPLY PROVENANCE
+ SOURCE-OFF VISIBILITY DOES NOT ESTIMATE PATH-LOSS COEFFICIENTS
+ FINITE-WIDTH BREATHING CONTRAST RESTORES ONE RESPONSE RANK
+ MASS/CHARGE CONTRAST SUPPLIES A SECOND CONDITIONAL REPAIR
+ SEPARATION NONLINEARITY TOO SMALL IN THE SOURCE REGIME
+ STANDARD FILTER-FUNCTION AND EXPERIMENTAL-DESIGN ABSORPTION
+ NO READY SUCCESSOR
```

The run completed at scoped Grade 4. It instantiates the abstract
`HC-DU-157` nuisance-span criterion, kills the naive force-amplitude assay,
and locates the smallest source-native response coordinate that can repair
the rank.

## Earned result

In the source's pointlike small-separation model,

\[
\Lambda_{\rm CSL}^{(0)}
=
\lambda\frac{m^2}{4m_0^2r_c^2}I_D,
\quad
\Lambda_{\rm gas}=\eta_{\rm gas}I_D,
\quad
\Lambda_{\rm bb}=\eta_{\rm bb}I_D,
\quad
\Lambda_E^{\rm intra}=\frac{q^2S_E}{4\hbar^2}I_D,
\]

with

\[
I_D=\int_0^\tau D^2dt
=\frac{3\pi F^2}{m^2\omega^5}.
\]

Those four design columns are proportional. Exact force or pointlike
frequency scans identify their sum only. With the force off, \(I_D=0\), so
source-off Ramsey visibility does not estimate a coefficient multiplying
\(I_D\).

The finite-width signal is instead

\[
I_{DG,i}=I_{D,i}S_i.
\]

Against one shared \(I_D\) nuisance, the two-configuration determinant is

\[
I_{D,1}I_{D,2}(S_1-S_2).
\]

Distinct breathing factors therefore restore rank at fixed \(r_c\). A
matched-trajectory preparation-width contrast is the least-retyping
candidate because it can vary \(I_{DG}\) without intentionally varying
\(I_D\), mass, charge, source, or duration. Width-dependent endpoint losses
remain explicit nuisance burdens.

A matched-path mass/charge contrast separates pointlike CSL from white
electric-field loss iff

\[
m_1^2q_2^2\ne m_2^2q_1^2.
\]

It changes more apparatus properties and is therefore the secondary repair.

Finally, the exact CSL response's departure from quadratic separation is
bounded by \(D_{\max}^2/(8r_c^2)\): at the cited baseline and aggressive
points this is at most \(3.125\times10^{-6}\) and \(5.0\times10^{-5}\).
That nonlinearity is not the cheap attribution lever.

## Scientific meaning

Path dependence is not provenance. A candidate law becomes attributable only
through a response coordinate outside the complete admitted nuisance span.
More precision on a rank-one response surface cannot create that coordinate.

The positive finding is that thermal breathing is not only a sensitivity
penalty. Deliberately varied and independently measured, it can become a CSL
response contrast. This keeps the reversible-pointer route alive while
sharply changing the assay it would need.

The result remains conditional on a supplied experimental packet. It does not
select a pointer, apparatus, archive, observer boundary, or nuisance class,
and it supplies no observed anomaly or evidence for CSL.

## Portfolio transition

- `CURRENT-RESEARCH.yaml` advanced from revision 110 to 111.
- `HC-DU-158` was attached to the parked physical-reliability branch.
- `PRED-DU-005` now records the exact shared-kernel obstruction and
  breathing-contrast repair.
- `NI-DU-201` prevents agents from treating
  \(F^2\omega^{-5}\) as a theory-specific provenance signature.
- the candidate class is narrowed to a reversible-pointer
  breathing-contrast discriminator; and
- no parked reopener was satisfied, so the portfolio remains quiescent with
  `NO_READY_SUCCESSOR`.

## Resource disposition

The primary-source equations and direct determinant proofs decide the local
question. A simulation would only reproduce them. No external hardware,
provider, apparatus search, or run is authorized.

## Durable files

- `explorations/reversible-pointer-csl-quadratic-kernel-degeneracy-and-breathing-contrast-repair-2026-07-30.md`
- `explorations/prediction-register.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `CURRENT-RESEARCH.yaml`
- this run plan and receipt

## Validation

- current arXiv v4 TeX source cross-check — **PASS**; the source gives the
  four proportional \(I_D\) terms, exact finite-width CSL response,
  \(S_{\rm br}=4.82\times10^{-2}\) and \(2.41\times10^{-2}\), and the cited
  maximum separations.
- direct determinant proofs and exact rational controls — **PASS**; the
  breathing and mass/charge determinants factor as stated, and the nonlinear
  bounds are exactly \(1/320000\) and \(1/20000\).
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, 37/37 governance checks, 314 unique counter-assumptive findings,
  and 5,923/6,000 cold-start words. The first pass correctly caught the stale
  expected row count before it was advanced from 313 to 314.
- Python compilation of the changed governance probe — **PASS**.
- direct PyYAML revision, quiescence, successor, and durable-path assertions
  — **PASS**.
- `git diff --check` — **PASS**.
