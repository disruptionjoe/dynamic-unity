---
title: "Conformal null-front transfer, metric-coupling gauge, and scale-anchor boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-110
work_id: CCR-CONFORMAL-NULL-FRONT-TRANSFER-AND-SCALE-ANCHOR-GATE
run_id: RUN-20260729-080716-conformal-null-front-transfer-scale-anchor-gate
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
maximum_grade: "Conditional Grade 3 no-refit null-front/event-control transfer across one conformal metric class plus scoped Grade 4 conformal-factor/nonlinear-coupling nonidentifiability and scale-anchor necessity boundary; no Grade-5 physical remainder or prediction"
---

# Conformal null-front transfer, metric-coupling gauge, and scale-anchor boundary

## Executive result

The swing returned:

```text
FIXED_NULL_FRONTS_TRANSFER_UNCHANGED_ACROSS_THE_CONFORMAL_CLASS
+ FOUR_FRONT_INTERSECTION_COORDINATES_ARE_CONFORMALLY_INVARIANT
+ FINITE_RESOLUTION_CONTROL_CODEBOOK_NEEDS_NO_CONFORMAL_FACTOR_REFIT
+ CONFORMAL_WAVE_QUADRATIC_RESPONSE_HAS_AN_EXACT_METRIC_COUPLING_GAUGE
+ BOUNDARY_IDENTITY_OMEGA_EQUALS_ONE_MAKES_LOCAL_SOURCE_SOLUTION_MAPS_IDENTICAL
+ ALL_MIXED_RESPONSE_ORDERS_DESCEND_THROUGH_THE_SAME_GAUGE
+ NONLINEAR_EVENT_FORMATION_IF_PRESENT_TRANSFERS_BUT_DOES_NOT_SELECT_SCALE
+ FIXING_THE_NONLINEAR_COEFFICIENT_IN_PHYSICAL_UNITS_BREAKS_THIS_GAUGE
+ BREAKING_ONE_GAUGE_IS_NECESSARY_NOT_SUFFICIENT_FOR_SCALE_RECONSTRUCTION
+ CAUSAL_EVENT_NETWORK_CAN_CARRY_CONFORMAL_STRUCTURE_WITHOUT_FULL_METRIC
+ NONCONFORMAL_SCALE_ANCHOR_IS_THE_NEXT_GEOMETRY_DEPENDENCY
+ FORMATION_LATENCY_PROVENANCE_ACQUISITION_AND_FULL_METRIC_TRANSFER_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-109`'s fixed four-front architecture does transfer without directional
or phase-decoder refit across every positive conformal rescaling

\[
g_\Omega=\Omega^2\eta
\]

on the same coordinate manifold. Positive conformal rescaling preserves null
covectors. The same four phase equations therefore meet at the same coordinate
event for every \(\Omega\).

That is the strongest legitimate curved-family positive available to this
architecture. It is also an exact boundary. Null and causal structure determine
only the conformal geometry. They do not determine local metric scale.

The boundary is stronger than a generic warning. For the four-dimensional
conformal wave operator

\[
P_g=\square_g-\frac16R_g
\]

and quadratic equation

\[
P_gu+a u^2=f,
\tag{1}
\]

the transformation

\[
(g,u,a,f)
\longmapsto
(\Omega^2g,\Omega^{-1}u,\Omega^{-1}a,\Omega^{-3}f)
\tag{2}
\]

is an exact covariance. If \(\Omega=1\) on the source/readout region \(V\),
then the same source \(f\) produces the same retained response \(u|_V\) in two
different interiors. The complete local source-to-solution map is identical.
Every mixed derivative and nonlinear interaction coefficient derived from
that map is therefore identical as well.

The fixed architecture can consequently transfer a conditional nonlinear
interaction event through the conformal class while remaining unable to
select the conformal factor. Its success is real, but its success is
scale-blind.

## 1. Frozen typed specimen

Freeze:

- one four-dimensional differentiable manifold;
- one source/readout region \(V\);
- one Minkowski representative \(\eta\);
- a positive compact \(C^k\) family of conformal factors with
  \(\Omega|_V=1\);
- the four phase covectors from `HC-DU-109`;
- the conformal wave operator \(P_g\);
- the quadratic equation (1);
- past-zero or retarded solution selection;
- sources supported in \(V\);
- response restriction to \(V\); and
- the coordinate identification used to compare the conformal interiors.

The four phase rows are

\[
\ell_1=(1,1,0,0),\quad
\ell_2=(1,-1,0,0),\quad
\ell_3=(1,0,1,0),\quad
\ell_4=(1,0,0,1).
\]

Their phase hypersurfaces are

\[
\phi_i(p)=\ell_i p-c_i=0.
\]

The scalar equation is a controlled mathematical specimen. This receipt does
not claim that it is the fundamental scalar dynamics of nature.

## 2. Fixed-front conformal-transfer theorem

For every positive \(\Omega\),

\[
g_\Omega^{-1}
=
\Omega^{-2}\eta^{-1}.
\]

Because each \(\ell_i\) is null for \(\eta\),

\[
g_\Omega^{-1}(\ell_i,\ell_i)
=
\Omega^{-2}\eta^{-1}(\ell_i,\ell_i)
=0.
\tag{3}
\]

Thus every fixed phase hypersurface remains characteristic for every metric in
the conformal class.

Their common event is determined by

\[
Lp=c,
\qquad
L=
\begin{pmatrix}
1&1&0&0\\
1&-1&0&0\\
1&0&1&0\\
1&0&0&1
\end{pmatrix}.
\]

No conformal factor appears in this equation. Since \(\det L=-2\), the event
is still

\[
t=\frac{c_1+c_2}{2},\quad
x=\frac{c_1-c_2}{2},\quad
y=c_3-t,\quad
z=c_4-t.
\tag{4}
\]

### Scoped theorem

> On one supplied coordinate manifold, the `HC-DU-109` phase code and event
> decoder transfer unchanged across every positive conformal rescaling of the
> Minkowski representative.

This is a no-refit transfer theorem for the **front geometry and coordinate
intersection**, not yet for a finite physical source implementation.

## 3. Finite-resolution codebook transfer

Let \(K=\{c^{(1)},\ldots,c^{(M)}\}\) be any predeclared finite phase codebook.
Equation (4) maps it to the same \(M\) coordinate events for every
\(\Omega\). The conditioning margin inherited from `HC-DU-109`,

\[
\sigma_{\min}(L)
=
\sqrt{\frac{5-\sqrt{17}}2},
\]

is likewise independent of \(\Omega\), because it belongs to the frozen
coordinate control matrix.

Therefore:

- the finite codebook does not need conformal-factor-specific phase refit;
- the same phase-error-to-coordinate-error bound transfers;
- the packet still has only finite event resolution;
- physical source amplitudes and transport are not certified by this
  coordinate statement; and
- the coordinate error is not automatically a proper-distance or proper-time
  error, because those depend on \(\Omega\).

The transfer is useful precisely because it separates causal addressing from
metric-scale measurement.

## 4. Exact conformal metric-coupling gauge

In four dimensions, the conformal wave operator satisfies

\[
P_{\Omega^2g}(\Omega^{-1}u)
=
\Omega^{-3}P_gu.
\tag{5}
\]

Give the quadratic coefficient weight \(-1\):

\[
a_\Omega=\Omega^{-1}a.
\tag{6}
\]

Then

\[
\begin{aligned}
P_{\Omega^2g}(\Omega^{-1}u)
+a_\Omega(\Omega^{-1}u)^2
&=
\Omega^{-3}P_gu
+\Omega^{-1}a\,\Omega^{-2}u^2\\
&=
\Omega^{-3}(P_gu+a u^2).
\end{aligned}
\tag{7}
\]

Thus if \(u\) solves (1) with source \(f\), then
\(\widetilde u=\Omega^{-1}u\) solves the transformed equation with source
\(\widetilde f=\Omega^{-3}f\).

## 5. Same local operational map, different interior

Assume:

\[
\Omega=1\quad\text{on }V,
\qquad
\operatorname{supp}f\subseteq V.
\]

Then

\[
\widetilde f=f
\]

everywhere: it agrees on \(V\), and both sources vanish outside \(V\).
Likewise,

\[
\widetilde u|_V=u|_V.
\]

For every admitted small source \(f\), the local source-to-solution maps obey

\[
\mathcal S_{g,a}(f)
=u|_V
=\widetilde u|_V
=\mathcal S_{\Omega^2g,\Omega^{-1}a}(f).
\tag{8}
\]

Choose a nontrivial \(\Omega\) in the interior. The two metric/coefficient
pairs differ there, while their complete operational maps on \(V\) are
identical.

### Scoped nonidentifiability theorem

> The complete local source-to-solution map for (1) does not separately
> identify the interior conformal factor and a freely covarying quadratic
> coefficient. It identifies at most their declared gauge class.

This is not a finite-data or noise limitation. Within the frozen model class,
no number of repeated local source/response measurements removes the exact
equivalence.

## 6. All nonlinear response orders inherit the gauge

Higher-order linearization differentiates the source-to-solution map with
respect to independently varied source amplitudes. Equation (8) identifies
the complete maps, so for every order \(k\),

\[
D^k\mathcal S_{g,a}(0)
=
D^k\mathcal S_{\Omega^2g,\Omega^{-1}a}(0)
\tag{9}
\]

on the retained source/readout interface.

Consequently:

- every Möbius-isolated mixed response from `HC-DU-105` is unchanged;
- every conditional four-wave artificial-point-source response is unchanged;
- every source tuple and boundary return can retain the same provenance
  labels;
- multiplying a distribution by smooth positive \(\Omega^{-1}\) does not move
  its singular support; and
- nonlinear event formation, if the frozen hypotheses make it nonzero and
  detectable, transfers without selecting the conformal factor.

This blocks a tempting overclaim: nonlinear interaction can reveal conformal
geometry without necessarily revealing full metric scale.

## 7. The exact scale-anchor exit

Hold \(a\) fixed instead of transforming it. The field transforms with weight
\(-1\), so

\[
a(\Omega^{-1}u)^2
=
\Omega^{-2}a u^2,
\]

whereas the conformal wave term and transformed source have weight \(-3\).
The nonlinear term therefore differs by one factor of \(\Omega\).

The exact gauge (7) is broken.

This earns only:

> An independently fixed datum that does not covary under (2) is necessary
> to distinguish members of this exact equivalence class.

It does **not** earn:

- injective recovery of \(\Omega\);
- a finite stable inversion theorem;
- physical selection of \(a\);
- proof that \(a\) is constant in operational units;
- uniqueness against other gauges or diffeomorphisms; or
- full-metric reconstruction from one event packet.

A fixed mass, coupling, calibrated proper-time interval, volume, energy scale,
or other nonconformal standard may play the role of an anchor in a future
physical model. Which one is independently selected is a separate question.

## 8. Collision with primary nonlinear inverse theory

The component mathematics is known and must not be presented as a novel
conformal inverse theorem:

- Kurylev, Lassas, and Uhlmann construct artificial point sources from
  nonlinear hyperbolic interactions and recover conformal Lorentzian
  structure from supplied source-to-solution data
  ([arXiv:1405.3386](https://arxiv.org/abs/1405.3386)).
- Lassas, Uhlmann, and Wang use semilinear wave interactions to determine the
  conformal class and parts of the nonlinear coefficients under their stated
  assumptions
  ([arXiv:1606.06261](https://arxiv.org/abs/1606.06261)).
- Uhlmann and Zhang analyze quadratic nonlinear wave interactions from the
  boundary, recover a conformal class in the general case, and state stronger
  conditions under which the metric can be recovered up to isometry
  ([arXiv:2104.08386](https://arxiv.org/abs/2104.08386)).
- Alexakis, Isozaki, Lassas, and Tyni recover conformal type from a nonlinear
  scattering operator while retaining a metric/nonlinearity multiplicative
  ambiguity
  ([arXiv:2411.09354](https://arxiv.org/abs/2411.09354)).
- The conformal wave transformation used in (5) is standard; a direct
  derivation in general dimension is given by Gray, Kubizňák, May, Tjoa, and
  Mann
  ([arXiv:2002.05221](https://arxiv.org/abs/2002.05221)).

The Dynamic Unity contribution in this swing is the typed composition:

1. one fixed finite-control architecture transfers across a nontrivial metric
   class without target-specific phase refit;
2. the full nonlinear operational map has an exact interior gauge;
3. event formation and conformal-scale identification are therefore separate
   obligations; and
4. the next packet must add an independently selected, scale-sensitive datum
   rather than more null-front measurements of the same type.

## 9. Composition with the current event chain

The constructive chain is now:

```text
HC-DU-109
fixed four-null-front architecture + four phase controls
  -> unique coordinate intersection in flat 3+1

HC-DU-110
positive conformal family
  -> same characteristic fronts + same coordinate intersection without refit

frozen conformal-wave quadratic PDE
  -> conditional transferred nonlinear interaction

HC-DU-105
complete on/off source contexts
  -> joint-source mixed-response provenance

HC-DU-108
reciprocal detector crosslinks
  -> detector geometry + relative clocks up to gauge

HC-DU-107
four associated arrivals
  -> event localization in the supplied scaffold.
```

The same chain also exposes its own limit:

```text
null fronts + causal event relations
  -> conformal structure
  -/-> conformal factor

(g,a) and (Omega^2 g, Omega^-1 a)
  -> identical complete local nonlinear response
```

The event network can therefore carry genuine causal and conformal geometry
without yet carrying full metric geometry.

## 10. What changed

Before this swing, curved transfer was one undivided open burden. It now
separates into:

1. **Conformal causal transfer — closed conditionally.** The fixed phase
   architecture transfers unchanged across the positive conformal class.
2. **Physical nonlinear formation — still conditional.** The fixed PDE must
   have the required transverse, nonzero, finite-source, detectable response.
3. **Conformal-scale selection — exactly open.** The complete local map has a
   metric/coupling gauge unless an independent nonconformal datum is fixed.
4. **General curved transfer — open.** Metrics outside the conformal class
   change characteristic geometry and may require genuinely different source
   controls.
5. **Record formation and acquisition — open.** Source timing, event
   association, provenance, bounded latency, and attempt-complete acquisition
   remain physical interface obligations.

This is progress. Future work should not spend another swing showing that
causal/null data recover only a conformal class. It should either select a
physical scale anchor and test unchanged transfer, or leave geometry and
advance a different North-Star dependency.

## 11. Strongest absorber and cheapest kills

### Strongest absorber

Conformal Lorentzian geometry and nonlinear inverse-problem theory absorb the
mathematical components. They already establish artificial sources,
higher-order linearization, conformal recovery, and metric/nonlinearity gauge
boundaries from rich supplied operational maps.

### Cheapest kills

- positive Weyl rescaling leaves every fixed null front unchanged;
- the same phase code therefore contains no conformal-factor information;
- \((g,a)\) and \((\Omega^2g,\Omega^{-1}a)\) have the same local map when
  \(\Omega=1\) on the interface;
- every higher-order mixed response inherits that exact equivalence;
- fixing \(a\) breaks one gauge but does not prove scale injectivity;
- event coordinates on one supplied manifold are not selected physical
  labels;
- characteristic intersection does not prove a nonzero physical interaction;
  and
- a conformal event network is not a full metric reconstruction.

## 12. Claim ledger

| Claim | Status | Grade |
|---|---|---:|
| The four `HC-DU-109` covectors remain null under every positive conformal rescaling | proved / standard | 3 |
| Their coordinate intersection and phase decoder are independent of \(\Omega\) | proved in the frozen class | 3 |
| A finite-resolution phase codebook transfers without conformal-factor-specific refit | proved conditionally | 3 |
| The conformal-wave quadratic equation has the transformation (2) | proved / standard | 3 |
| \((g,a)\) and \((\Omega^2g,\Omega^{-1}a)\) can have identical complete local source-to-solution maps | proved under the boundary-identity and well-posedness assumptions | 4 |
| Higher-order mixed responses remove that exact ambiguity | false | 4 |
| A conditional artificial point source transfers across this gauge | proved at the level of conjugate solutions and singular support | 3 |
| That transferred event identifies the conformal factor | false | 4 |
| Holding \(a\) fixed breaks the exact covariance | proved | 3 |
| Breaking the covariance proves stable or injective recovery of \(\Omega\) | false | 4 |
| The complete metric is reconstructed by causal/null event relations alone | false in this class | 4 |
| The coupling or another scale anchor is physically selected | not shown | 0 |
| A finite formed packet reconstructs full regional metric geometry without refit | open | 0 |
| A novel physical law, prediction, or finite remainder survives standard theory | not shown | 0 |

## 13. Highest-information reopener

The next geometry-specific question is:

> Can one independently selected, nonconformally transforming physical datum
> be added to the unchanged source/event packet so that a finite, stable,
> no-refit inversion of the conformal factor holds on a declared compact
> family?

The frozen packet must specify:

- the scale anchor and why it is physical rather than fitted;
- its units, calibration, formation, access, and provenance;
- the metric, coefficient, gauge, source, boundary, and solution class;
- the finite control and readout resolution;
- the source-latency and event-association contract;
- the full remaining equivalence group;
- the target and inverse-stability margin; and
- a held-out transfer that forbids metric- or target-specific interface
  redesign.

A positive would upgrade causal/conformal event reconstruction toward metric
reconstruction. A negative should return one exact same-packet/different-scale
witness.

This reopener is well posed, but it is not automatically the next global
Dynamic Unity priority.

## 14. Repository disposition

- Bank `HC-DU-110` as a conditional Grade-3 conformal no-refit event-control
  transfer and a scoped Grade-4 metric/coupling nonidentifiability boundary.
- Preserve the nullness, event invariance, conformal weights, explicit
  different-interior witness, and fixed-coefficient gauge break in one
  proportional local regression.
- Refine the candidate class to require an independently fixed
  nonconformal scale anchor before full regional geometry can be claimed.
- Keep physical formation, bounded source latency, event provenance,
  attempt-complete acquisition, and transfer outside the conformal class open.
- Keep Dynamic Unity quiescent with no selected successor.
- Do not create a paper, prediction, experiment, hardware path, or external
  action.

## Boundary

This is a scoped conformal-transfer and exact nonidentifiability result. It is
not a new conformal inverse theorem, fundamental scalar dynamics, physical
source-selection theorem, completed artificial-point-source construction,
formed certified record, full metric reconstruction, empirical anomaly,
prediction, or ontological promotion.
