---
title: "Order plus volume: full-metric reconstruction, event-density gauge, and provenance boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-111
work_id: CCR-ORDER-VOLUME-METRIC-RECONSTRUCTION-AND-DENSITY-CALIBRATION-GATE
run_id: RUN-20260729-082343-order-volume-metric-reconstruction-gate
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
maximum_grade: "Conditional Grade 3 full-metric reconstruction from a supplied conformal class plus independently calibrated volume measure in a fixed finite-complexity arena, with scoped Grade 4 density, occurrence-identity, acquisition, and unrestricted-field boundaries; no Grade-5 physical remainder or prediction"
---

# Order plus volume: full-metric reconstruction, event-density gauge, and provenance boundary

## Executive result

The swing returned:

```text
CAUSAL_CONFORMAL_CLASS_PLUS_VOLUME_MEASURE_DETERMINES_FULL_METRIC
+ FOUR_DIMENSIONAL_CONFORMAL_FACTOR_IS_THE_FOURTH_ROOT_OF_VOLUME_DENSITY
+ FINITE_CELL_VOLUMES_EXACTLY_RECOVER_PIECEWISE_CONSTANT_SCALE
+ VOLUME_ERROR_HAS_AN_EXPLICIT_CONFORMAL_SCALE_STABILITY_BOUND
+ VOLUME_IS_ADDITIVE_UNDER_BENIGN_PARTITION_REFINEMENT
+ KNOWN_POISSON_DENSITY_GIVES_A_QUANTIFIED_FINITE_RESOLUTION_RECORD
+ UNKNOWN_GLOBAL_EVENT_DENSITY_IS_EXACTLY_CONFOUNDED_WITH_ABSOLUTE_SCALE
+ COMMON_UNKNOWN_DENSITY_STILL_PERMITS_RELATIVE_SCALE
+ UNKNOWN_LOCAL_EVENT_DENSITY_ABSORBS_LOCAL_CONFORMAL_SCALE
+ UNIQUE_OCCURRENCE_IDENTITY_AND_COMPLETE_ACQUISITION_ARE_COUNTING_ANTECEDENTS
+ ORDER_PLUS_NUMBER_IS_A_CONDITIONAL_ARCHITECTURE_NOT_INTERFACE_SELECTION
+ FINITE_PARTITION_DOES_NOT_EXACTLY_RECOVER_AN_UNRESTRICTED_SMOOTH_FACTOR
+ PHYSICAL_VOLUME_FORMATION_AND_DENSITY_CALIBRATION_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-110` showed that the fixed nonlinear-event architecture can transfer
through a conformal metric class while remaining unable to recover metric
scale. `HC-DU-111` identifies the exact missing mathematical datum:

> A conformal Lorentzian geometry plus a positive spacetime volume measure
> determines the full Lorentzian metric.

In four dimensions, if

\[
g=\Omega^2\bar g,
\]

then

\[
d\mathrm{vol}_{g}
=
\Omega^4d\mathrm{vol}_{\bar g}.
\]

Therefore

\[
\Omega
=
\left(
\frac{d\mathrm{vol}_{g}}
     {d\mathrm{vol}_{\bar g}}
\right)^{1/4}.
\tag{1}
\]

This is the clean completion of the causal/conformal branch. It is standard
Lorentzian geometry, not new physics.

The physical-record question does not disappear. A count \(N\) measures
volume only relative to a formation density \(\rho\). If

\[
N_j\sim\operatorname{Poisson}(\rho V_j),
\]

then unknown homogeneous \(\rho\) is exactly confounded with one global metric
scale. Unknown region-dependent \(\rho_j\) absorbs every local conformal
factor. Counts also require unique occurrence identity, de-duplication, and
complete acquisition before they form an additive measure.

Thus the causal-set slogan “order plus number equals geometry” is a strong
conditional architecture. It does not by itself select the number-to-volume
scale or make the fundamental elements into observer-accessible certified
records.

## 1. Typed starting point

Freeze:

- an oriented and time-oriented four-dimensional manifold \(M\);
- a distinguishing causal structure sufficient to recover a conformal class;
- a conformal representative \(\bar g\);
- a positive Borel volume measure \(\mu\) absolutely continuous with respect
  to \(d\mathrm{vol}_{\bar g}\);
- a declared representation quotient by causal- and volume-preserving
  diffeomorphism;
- a fixed finite partition only for the finite positive control; and
- count formation, density, provenance, and acquisition as separate physical
  interfaces.

The causal reconstruction premise has a precise classical scope.
Hawking--King--McCarthy and Malament show, under their causality and regularity
conditions, that causal/timelike structure determines the topological,
differential, and conformal structure—not the conformal factor
([Hawking--King--McCarthy](https://doi.org/10.1063/1.522874),
[Malament](https://doi.org/10.1063/1.523436)).

This swing begins after that conformal class has been recovered. It does not
claim that the finite DU packet has already met all premises of those global
theorems.

## 2. Conformal-class-plus-volume theorem

In dimension \(d\), Weyl rescaling gives

\[
\det(\Omega^2\bar g)
=
\Omega^{2d}\det\bar g,
\]

and hence

\[
d\mathrm{vol}_{\Omega^2\bar g}
=
\Omega^d d\mathrm{vol}_{\bar g}.
\tag{2}
\]

Let

\[
r
=
\frac{d\mu}{d\mathrm{vol}_{\bar g}}
\]

be the positive Radon--Nikodym density. There is exactly one positive
conformal factor satisfying

\[
d\mu=d\mathrm{vol}_{\Omega^2\bar g},
\]

namely

\[
\Omega=r^{1/d}.
\tag{3}
\]

For \(d=4\), this is equation (1).

### Scoped theorem

> On a fixed differentiable manifold and within a fixed conformal class, a
> positive volume measure uniquely selects the metric representative. The
> remaining equivalence is the declared diffeomorphism action preserving both
> causal and volume structure.

The volume measure is doing real work. It is not derivable from null relations
alone.

## 3. Finite piecewise-constant reconstruction

Let \(C_1,\ldots,C_k\) be a fixed partition with known positive reference
volumes

\[
\bar V_j
=
\int_{C_j}d\mathrm{vol}_{\bar g}.
\]

Restrict the conformal family to

\[
g_\omega|_{C_j}
=
\omega_j^2\bar g,
\qquad
\omega_j>0.
\]

Then

\[
V_j
=
\mu(C_j)
=
\omega_j^4\bar V_j,
\]

so

\[
\omega_j
=
\left(\frac{V_j}{\bar V_j}\right)^{1/4}.
\tag{4}
\]

The map from \(k\) positive scale parameters to \(k\) cell volumes is exactly
injective and uses one unchanged partition for the entire declared class.

This is a finite no-refit full-metric reconstruction theorem **inside the
piecewise-constant family**. It does not select:

- the partition;
- the conformal class;
- the volume interface;
- the cell occurrence identities;
- the scale units; or
- the physical density that turns counts into \(V_j\).

## 4. Explicit stability

Suppose

\[
\widehat V_j
=
V_j(1+\delta_j),
\qquad
|\delta_j|\le\epsilon<1.
\]

Then

\[
\frac{\widehat\omega_j}{\omega_j}
=
(1+\delta_j)^{1/4}.
\]

The mean-value theorem gives

\[
\left|
\frac{\widehat\omega_j}{\omega_j}-1
\right|
\le
\frac{\epsilon}
     {4(1-\epsilon)^{3/4}}.
\tag{5}
\]

Thus a calibrated relative-volume error has a direct and unusually mild
fourth-root scale effect. This is a real stability advantage, conditional on
the volume error contract being honest.

## 5. Refinement invariance

A genuine measure is additive. If a cell \(C\) is partitioned into disjoint
subcells \(C_\alpha\),

\[
\mu(C)=\sum_\alpha\mu(C_\alpha).
\tag{6}
\]

Benign subdivision changes the representation but not the parent volume.
This passes the refinement warning learned from Time as Finality and avoids
using relay count or graph path length as if either were physical scale.

The corresponding count law needs stronger typing. If \(E_\alpha\) is the set
of uniquely identified occurrences in child cell \(C_\alpha\), then

\[
\left|\bigsqcup_\alpha E_\alpha\right|
=
\sum_\alpha|E_\alpha|
\]

only when the occurrence sets are disjoint. If one event can appear under two
regional IDs, the naive sum double-counts it. If an event is missed, selected
away, or inaccessible, the retained union undercounts it.

Distributed mergeability therefore requires:

- globally or reconciliation-stably unique occurrence identity;
- de-duplication semantics;
- cell membership or boundary-crossing semantics;
- complete or explicitly modeled selection;
- preserved provenance; and
- a declared horizon over which the count is final.

This is where a physical volume measure differs from an arbitrary regional
counter.

## 6. Known-density Poisson reconstruction

The causal-set proposal uses a locally finite partial order and a
number-volume correspondence. In a faithful Poisson sprinkling with density
\(\rho\),

\[
N(C)\sim\operatorname{Poisson}(\rho\,\mu(C)).
\tag{7}
\]

The founding causal-set paper makes both the causal-order and approximate
number-volume roles explicit
([Bombelli--Lee--Meyer--Sorkin](https://doi.org/10.1103/PhysRevLett.59.521)).
Later work proves precise optimality properties for Poisson sprinkling under a
strong small-region number-volume requirement
([Saravani--Aslanbeigi](https://arxiv.org/abs/1403.6429)).

When \(\rho\) is independently known,

\[
\widehat V=\frac{N}{\rho}
\]

is unbiased, with

\[
\operatorname{Var}(\widehat V)
=
\frac{V}{\rho},
\qquad
\frac{\operatorname{sd}(\widehat V)}{V}
=
\frac1{\sqrt{\rho V}}.
\tag{8}
\]

For \(0<\epsilon\le1\), a standard multiplicative Poisson bound gives

\[
\Pr\!\left(
|N-\rho V|\ge\epsilon\rho V
\right)
\le
2\exp\!\left(
-\frac{\rho V\epsilon^2}{3}
\right).
\tag{9}
\]

On the complementary event, equation (5) transfers the count interval into a
conformal-scale interval.

This is finite-resolution statistical reconstruction, not exact metric
recovery from one finite random count.

## 7. Exact global density-scale gauge

In cell \(j\), the Poisson mean is

\[
\lambda_j
=
\rho\,\omega_j^4\bar V_j.
\tag{10}
\]

For every constant \(c>0\), define

\[
\omega'_j=c\omega_j,
\qquad
\rho'=\frac{\rho}{c^4}.
\tag{11}
\]

Then

\[
\rho'(\omega'_j)^4\bar V_j
=
\rho\omega_j^4\bar V_j
=
\lambda_j.
\]

Every joint count distribution is identical. No amount of counting
distinguishes the two absolute scales.

### Scoped no-go

> A homogeneous but uncalibrated event density leaves one exact global Weyl
> scale undetermined.

The count ratios still identify relative scale:

\[
\frac{\lambda_i/\bar V_i}{\lambda_j/\bar V_j}
=
\left(\frac{\omega_i}{\omega_j}\right)^4.
\tag{12}
\]

Thus common unknown density does not erase the conformal-factor **shape**. It
erases its absolute normalization.

## 8. Exact local density-scale gauge

If density is allowed to vary independently by cell,

\[
\lambda_j
=
\rho_j\omega_j^4\bar V_j.
\]

For any alternative positive factors \(\omega'_j\), choose

\[
\rho'_j
=
\rho_j
\left(\frac{\omega_j}{\omega'_j}\right)^4.
\tag{13}
\]

Every \(\lambda_j\) is unchanged.

### Scoped no-go

> Without a homogeneity law or independent local calibration, event counts
> identify neither absolute nor relative local metric scale.

A claim that count density is uniform is therefore a physical-law premise,
not a harmless statistical convenience.

## 9. Local finiteness does not select an accessible volume record

The 1987 causal-set proposal is a serious foundational architecture, but three
levels must remain separate:

1. **Local finiteness:** every bounded causal interval contains finitely many
   fundamental elements.
2. **Number-volume correspondence:** element cardinality represents continuum
   four-volume in units fixed by a fundamental density.
3. **Observer-accessible record:** a physical subsystem forms, retains, and
   can certify the relevant element identities and counts.

The first does not alone give the second's conversion scale. Neither gives the
third's access interface.

In causal-set kinematics, fundamental density may be postulated as part of the
substrate. That is legitimate. In Dynamic Unity's North-Star direction,
however, importing that density and complete element count as record data
would supply the very scale and access structure being tested.

The honest positive is conditional:

> If causal order, fundamental event identity, homogeneous density, and
> complete counts are physically available, then order plus number supplies
> full metric geometry statistically and at the declared discreteness scale.

## 10. Finite cells do not identify an unrestricted smooth factor

One exact cell volume gives only

\[
\int_C\Omega^4d\mathrm{vol}_{\bar g}.
\]

Distinct smooth positive factors can have the same integral. On
\([0,1]\) with unit reference measure, for example,

\[
\Omega_0^4(x)=1,
\qquad
\Omega_1^4(x)=x+\frac12
\]

are both positive and integrate to one, but differ pointwise.

Likewise, finitely many cell integrals leave within-cell variations
unidentified. Exact recovery of a general smooth \(\Omega(x)\) requires:

- a growing/refining family of volume records;
- an independently selected finite-dimensional model;
- a regularity-and-resolution target rather than exact field identity; or
- a continuum volume measure.

This is the scale-side counterpart of `HC-DU-106`'s finite-packet versus
unrestricted-field boundary.

## 11. Composition with the current geometry chain

The positive architecture is now explicit:

```text
HC-DU-109
fixed null fronts + phase controls
  -> controlled event intersections

HC-DU-110
positive conformal class
  -> unchanged event control + conformal-scale gauge

Malament/HKM premise
causal order on a distinguishing smooth spacetime
  -> conformal geometry

HC-DU-111
independently calibrated volume measure
  -> unique full metric representative

finite piecewise-constant specialization
  -> finite exact scale packet with explicit stability.
```

The corresponding physical-interface chain remains:

```text
physical event formation
  -> unique event identity
  -> region membership
  -> complete de-duplicated count
  -> independently calibrated homogeneous density
  -> volume measure
  -> metric scale.
```

No arrow in the second chain is implied merely by the existence of null-front
intersections.

## 12. What changed

Before this swing, “find a nonconformal scale anchor” was an open category.
It is now a precise best-case theorem and a precise failure map:

1. **Mathematical anchor — solved.** A volume measure is sufficient to
   complete conformal geometry into full metric geometry.
2. **Finite-complexity inversion — solved conditionally.** Fixed cell volumes
   recover fixed piecewise-constant scale factors with an explicit margin.
3. **Global calibration — exactly open.** Common unknown count density leaves
   one absolute scale gauge.
4. **Local formation law — exactly open.** Unknown regional density absorbs
   local scale.
5. **Record interface — open.** Occurrence identity, de-duplication,
   selection, access, and acquisition must be physically formed.
6. **Unrestricted geometry — open.** A fixed finite partition cannot recover
   an arbitrary smooth conformal factor.

The next work should not merely add “counts” to the event graph. It must either
physically select and calibrate their density or prove that another formed
scale carrier closes the same interface with fewer assumptions.

## 13. Strongest absorber and cheapest kills

### Strongest absorber

Classical Lorentzian causal reconstruction and causal-set kinematics absorb
the component architecture. “Order plus number equals geometry” already
captures the conceptual positive.

Dynamic Unity's residual is the typed inverse interface:

- which physical occurrences are counted;
- what selects their density;
- which observer can access them;
- how regional counts merge without duplication;
- what makes the count complete; and
- whether the same interface transfers without target refit.

### Cheapest kills

- unknown common density exactly absorbs absolute scale;
- unknown local density absorbs every local scale factor;
- duplicate IDs violate naive additive counting;
- incomplete acquisition confounds smaller volume with missing events;
- a supplied fundamental density is not reconstructed from records;
- one finite cell partition misses within-cell smooth variation; and
- a partition chosen from the held-out metric is interface refit.

## 14. Claim ledger

| Claim | Status | Grade |
|---|---|---:|
| Distinguishing causal structure determines conformal geometry under the standard smooth conditions | imported theorem | 3 |
| A conformal class plus a positive volume measure determines the full metric representative | proved / standard | 3 |
| In four dimensions the conformal factor is the fourth root of the volume-density ratio | proved / standard | 3 |
| Fixed cell volumes exactly recover a fixed piecewise-constant conformal family | proved | 3 |
| Relative volume error has the bound (5) on relative scale error | proved | 3 |
| A genuine volume measure is invariant under benign partition refinement | proved / standard | 3 |
| Known homogeneous Poisson density supplies a finite-resolution volume record with (8)--(9) | proved conditionally | 3 |
| Unknown homogeneous density still permits absolute scale recovery | false | 4 |
| Unknown homogeneous density permits relative cell-scale recovery | proved conditionally | 3 |
| Unknown regional density permits local scale recovery | false | 4 |
| Raw counts are additive without unique occurrence identity | false | 4 |
| Local finiteness selects the physical number-to-volume scale | not shown | 0 |
| Fundamental causal-set elements are automatically observer-accessible certified records | false as an implication | 4 |
| A fixed finite cell packet identifies an unrestricted smooth conformal factor | false | 4 |
| The event architecture physically forms and calibrates a complete volume measure | not shown | 0 |
| A novel physical law, prediction, or finite remainder survives standard theory | not shown | 0 |

## 15. Highest-information reopener

The next geometry-specific question is:

> Can the formed event network produce an independently calibrated,
> refinement-additive volume measure—complete enough to exclude density,
> duplication, and selection rivals—without importing a metric-defined
> partition or external absolute scale?

The smallest useful arena should freeze:

- one finite causal-event network;
- one source formation and event-identity mechanism;
- one density law and calibration route;
- one regional de-duplication/merge protocol;
- one acquisition visibility contract;
- one finite piecewise-constant conformal class;
- one held-out cell-scale target; and
- the global-scale rival (11) plus the local-density rival (13).

A positive would complete a finite, operational order-plus-volume metric
reconstruction. A negative should identify whether the first irreducible input
is density, event identity, acquisition, partition selection, or absolute
scale.

This is a sharp geometry reopener, not automatically the next global
Dynamic Unity priority.

## 16. Repository disposition

- Bank `HC-DU-111` as a conditional Grade-3 order-plus-volume full-metric
  reconstruction and scoped Grade-4 density/provenance/acquisition boundary.
- Preserve exact cell recovery, stability, refinement, Poisson precision,
  global/local density gauges, duplicate-ID failure, and smooth within-cell
  ambiguity in one proportional local regression.
- Refine the geometry candidate from “nonconformal scale anchor” to an
  independently calibrated, refinement-additive physical volume measure with
  unique occurrence identity and complete acquisition.
- Keep Dynamic Unity quiescent with no selected successor.
- Do not create a paper, prediction, experiment, hardware path, or external
  action.

## Boundary

This is a scoped reconstruction and nonidentifiability result. It is not a new
Lorentzian causal theorem, causal-set theory, physical event-density law,
formed volume record, selected absolute scale, unrestricted smooth-metric
reconstruction, empirical anomaly, prediction, or ontological promotion.
