---
title: "Reversible-pointer CSL three-width strict-convexity prediction lock and timing-nuisance boundary"
status: banked_scoped_result_and_prediction_hardening
doc_type: exploration
created: 2026-07-31
claim_id: HC-DU-187
prediction_id: PRED-DU-005
prediction_lock_version: 1
run_id: RUN-20260731-061534-csl-three-width-prediction-lock
work_id: CSL-THREE-WIDTH-PREDICTION-LOCK
action_id: CSL-THREE-WIDTH-PREDICTION-LOCK
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_7
supporting_lanes:
  - lane_1
  - lane_3
  - lane_4
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
evidence_grade: 4
maximum_grade: 4
---

# Reversible-pointer CSL three-width prediction lock

## Executive return

```text
TWO-WIDTH_BREATHING_REPAIR_IS_NOT_COMPLETE_AGAINST_THE_SOURCE_MODEL
+ ENDPOINT_TIMING_LOSS_ADDS_A_WIDTH-DEPENDENT_NUISANCE_COLUMN
+ TWO_WIDTHS_PLUS_TWO_UNKNOWN_NUISANCES_HAVE_NO_ATTRIBUTION_RANK
+ CSL_BREATHING_RESPONSE_IS_STRICTLY_CONVEX_IN_PREPARED_ENDPOINT_VARIANCE
+ THREE_DISTINCT_WIDTHS_RESTORE_RANK_IN_THE_FROZEN_MINIMAL_MODEL
+ ONE_EXACT_NUISANCE-ANNIHILATING_CONTRAST_LOCKED
+ PUBLISHED_BASELINE/AGGRESSIVE_PAIR_IS_NOT_THE_MATCHED_CONTROL
+ PRED-DU-005_HARDENED_WITH_RETREAT_COSTS
+ STANDARD_CSL_FILTER-FUNCTION_IDENTIFIABILITY_AND_DESIGN_ABSORPTION
+ NO_CSL_EVIDENCE_COMPLETE_APPARATUS_HARDWARE_ACTION_NEW_DU_LAW_OR_WAVE-3
```

`HC-DU-158` proved that varying only force or path amplitude cannot
distinguish pointlike small-separation CSL from several ordinary loss
channels: all share $I_D = ∫ D^2dt$. It then identified a preparation-width
contrast as the cleanest conditional repair. That repair was exact against
one shared $I_D$ nuisance.

The full v4 proposal contains a second source-internal nuisance that changes
with the proposed control. A timing mismatch produces endpoint-overlap loss
proportional to the pointer variance at recombination. Once its coefficient
is unknown, two widths are saturated by two nuisance columns. The two-width
repair is therefore not a complete prediction lock.

The positive result is stronger and still local. In the source's Gaussian,
small-separation model, the CSL breathing factor is **strictly convex** in
the prepared endpoint variance. Three distinct prepared widths consequently
separate it from both a shared path-loss coefficient and one unknown
width-linear timing-loss coefficient. This yields an exact no-refit contrast
and a sharper version of `PRED-DU-005`.

## 1. Source and scope freeze

The sole physical source is Peter Renkel,
["Testing Continuous Spontaneous Localization by Coherently Simulating a
Measurement with a Nanoparticle"](https://arxiv.org/abs/2606.22707),
arXiv:2606.22707v4, revised July 21, 2026.

The source proposes, but does not report, an experiment. Standard unitary
quantum mechanics predicts endpoint Ramsey-visibility recovery after the
pointer paths recombine. CSL predicts an additional irreversible visibility
loss accumulated along the separated paths.

This run freezes only the source's:

- Gaussian pointer;
- small-separation finite-width CSL equation;
- harmonic matched path;
- thermal initial state;
- endpoint timing-mismatch equation; and
- aggregate Ramsey visibility.

It does not validate feasibility, select a device, reproduce sensitivity
numbers, or claim that the displayed nuisance family is physically complete.

## 2. The prior shared-kernel result remains binding

For the harmonic branch separation

\[
D(t)=\frac{F}{m\omega^2}(1-\cos\omega t),
\qquad
\tau=\frac{2\pi}{\omega},
\]

the source gives

\[
I_D=\int_0^\tau D(t)^2dt
=\frac{3\pi F^2}{m^2\omega^5}.
\]

In the pointlike, small-separation regime, CSL and the admitted unresolved
gas, blackbody, and white electric-field losses are scalar multiples of
$I_D$. Therefore the often attractive lock

\[
\Lambda\propto F^2\omega^{-5}
\]

is a valid CSL response formula but not a CSL provenance signature. More
force points or more precision do not increase the response rank.

## 3. The source itself kills the two-width minimality claim

Let the initial tight-trap frequency be $ω_0$, the weak-trap frequency
be $ω$, and the preparation temperature be $T$. The source gives

\[
\sigma^2(t)
=
\frac{k_BT}{m\omega_0^2}\cos^2\omega t
+
\frac{k_BT}{m\omega^2}\sin^2\omega t.
\]

Define

\[
W:=\sigma^2(\tau)=\frac{k_BT}{m\omega_0^2},
\qquad
C:=\frac{k_BT}{m\omega^2}.
\]

Varying $ω_0$ at fixed $T,m,ω,F$ changes $W$, while the
controlled trajectory $D(t)$, $I_D$, and $C$ remain fixed.

The timing-mismatch term in the same source is

\[
\Lambda_t
\simeq
\frac{\sigma^2(\tau)F^2\delta t^2}{2\hbar^2}
=cW,
\]

where $c=F^2 δt^2/(2ℏ^2)$ is unknown unless timing jitter is
independently fixed.

After dividing the total exponent by the common nonzero path scale, the
minimal admitted response has the form

\[
z_i=aS(W_i;r_c)+b+cW_i.
\]

Here $a$ is the fixed-$r_c$ CSL amplitude, $b$ collects the shared
quadratic-path coefficient, and $cW_i$ is the timing-loss column.

### Proposition 1 — two-width saturation

For two distinct widths $W_1\ne W_2$, the nuisance columns

\[
(1,1)^\mathsf T,
\qquad
(W_1,W_2)^\mathsf T
\]

span $R^2$. Every two-entry CSL response vector is therefore in
their span.

Consequently, two widths identify CSL only if one nuisance coefficient is
fixed independently. The previous determinant against one shared nuisance
was correct; treating it as the complete v4 assay would not be.

## 4. The CSL breathing factor is strictly convex

At fixed nonzero path and fixed $r_c>0$, the source's finite-width factor is

\[
S(W;r_c)
=
\frac1{I_D}
\int_0^\tau
D(t)^2
\left[
1+\frac{W\cos^2\omega t+C\sin^2\omega t}{r_c^2}
\right]^{-5/2}dt.
\]

Differentiating under the finite integral gives

\[
\frac{d^2S}{dW^2}
=
\frac{35}{4r_c^4 I_D}
\int_0^\tau
D(t)^2\cos^4\omega t
\left[
1+\frac{W\cos^2\omega t+C\sin^2\omega t}{r_c^2}
\right]^{-9/2}dt.
\]

Every factor is nonnegative, and the integrand is positive on a set of
nonzero measure for the nonzero harmonic path. Therefore

\[
\frac{d^2S}{dW^2}>0.
\]

### Theorem 1 — three-width strict-convexity repair

For any three distinct ordered widths $W_1<W_2<W_3$, the columns

\[
S=(S(W_1),S(W_2),S(W_3))^\mathsf T,
\qquad
\mathbf 1,
\qquad
W=(W_1,W_2,W_3)^\mathsf T
\]

are linearly independent.

### Proof

If the vector $S$ lay in the span of $\mathbf1$ and $W$, the three sampled
values would lie on one affine line in $W$. Strict convexity forbids equality of
the two adjacent secant slopes. Hence the three-column determinant is
nonzero. ∎

This result is parameter conditional. The sign and convexity hold for every
fixed $r_c>0$, but the magnitude of the contrast depends on $r_c$,
$λ$, and the frozen configuration.

## 5. Version-1 no-refit contrast

For arbitrary distinct widths, choose

\[
w=
(W_3-W_2,\;W_1-W_3,\;W_2-W_1)^\mathsf T.
\]

Then

\[
w^\mathsf T\mathbf1=0,
\qquad
w^\mathsf TW=0,
\]

while strict convexity gives

\[
w^\mathsf TS\ne0.
\]

Thus the frozen contrast obeys

\[
\mathcal C:=w^\mathsf Tz
=a\,w^\mathsf TS(W;r_c).
\]

For equally spaced widths, $w$ is proportional to $(1,-2,1)$, so
$\mathcal C$ is the second finite difference. The matched incumbent family
containing only the declared shared and timing-loss columns predicts zero.
A fixed nonzero CSL parameter point predicts a nonzero value.

This is rival-excluding excess only relative to that frozen nuisance family.
It is not a claim that standard open-system physics has no other
width-dependent channel.

## 6. What is now locked in PRED-DU-005

The version-1 conditional lock fixes:

1. **Source version:** arXiv:2606.22707v4.
2. **Regime:** Gaussian pointer, small separation, fixed nonzero path, fixed
   $m,q,F,ω,T$, fixed $r_c$, and width varied only through
   $ω_0$.
3. **Configurations:** three distinct endpoint variances, numerically fixed
   before any future acquired response is revealed.
4. **Incumbent nuisance basis:** a shared path-loss column and one
   width-linear timing-loss column, plus any further columns declared before
   reveal.
5. **Target:** the nuisance-annihilating contrast $w^\mathsf Tz$.
6. **Challenger:** one fixed nonzero CSL parameter point, not a parameter
   chosen after the target.
7. **Acquisition duty:** joined visibility, width, timing, calibration,
   selection, and attempted-run lineage under one versioned contract.

No numerical apparatus packet yet instantiates items 3, 6, or 7. The lock is
therefore a conditional response-geometry lock, not an execution-ready
experimental registration.

The paper's reported baseline and aggressive points cannot fill the three
width slots. They change $ω$, duration, displacement, breathing factor,
and technical demands together. Using them would be a different contract.

## 7. Pre-registered retreat costs

- If timing variance is not independently monitored or common across width
  configurations, the contrast is **inadmissible**, not evidence for or
  against CSL.
- If a width-dependent nuisance is added after seeing the result, attribution
  is **invalidated**. The new nuisance defines a new version; it cannot rescue
  this lock retrospectively.
- If the realized protocol leaves the Gaussian small-separation regime, the
  lock is **out of scope**. The full response must be frozen as a new version
  before reveal.
- If $λ=0$, $r_c$ is unidentifiable. A null constrains only the
  predeclared nonzero parameter packet and uncertainty region, not all CSL.
- If the response is formed only after undocumented selection or rejected
  attempts, the physical acquisition gate fails even if the contrast has the
  predicted value.
- Changing source version, apparatus transfer, or configuration after reveal
  creates `PRED-DU-005-v2`; it does not mutate version 1.

## 8. Absorption and scientific value

The physical equations belong to CSL and open-system phenomenology. The
strict-convexity calculation, nuisance quotient, and rank test are absorbed
by calculus, filter-function theory, linear identifiability, optimal design,
and preregistration.

Dynamic Unity's gain is integration, not ownership:

```text
temporary path correlation
  -> aggregate visibility loss
  -> exact shared-kernel obstruction
  -> source-internal width nuisance
  -> minimal three-width no-refit quotient
  -> conditional theory-class certificate if acquisition preserves it.
```

This is useful because it prevents two opposite errors: calling a generic
$F^2ω^{-5}$ loss curve collapse evidence, and discarding the route
when a stricter control still exists. It makes the closest conditional packet
more honest and more testable.

No CSL evidence, selected apparatus, complete nuisance model, empirical
record, external-hardware action, new Dynamic Unity law, paper activation,
or Wave-3 reopener is earned.
