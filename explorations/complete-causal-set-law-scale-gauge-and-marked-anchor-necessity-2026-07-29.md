---
title: "Complete causal-set law: scale gauge and marked-anchor necessity"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-112
work_id: CCR-CAUSAL-SET-FULL-LAW-SCALE-GAUGE-AND-MARKED-ANCHOR-GATE
run_id: RUN-20260729-083413-causal-set-full-law-scale-gauge
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
maximum_grade: "Scoped Grade 4 complete-law absolute-scale nonidentifiability and scale-anchor necessity theorem, with conditional Grade 3 marked proper-time reconstruction; no Grade-5 physical remainder, new law, or prediction"
---

# Complete causal-set law: scale gauge and marked-anchor necessity

## Executive result

The swing returned:

```text
COMPLETE_POISSON_CAUSAL_SET_LAW_IS_INVARIANT_UNDER_METRIC_DENSITY_RESCALE
+ CAUSAL_ORDER_AND_INTENSITY_MEASURE_FACTOR_THROUGH_THE_SAME_SCALE_GAUGE
+ EVERY_UNMARKED_CAUSAL_SET_STATISTIC_IS_ABSOLUTE_SCALE_BLIND
+ FREE_REGIONAL_DENSITY_EXTENDS_THE_FULL_LAW_GAUGE_TO_LOCAL_CONFORMAL_SCALE
+ HOMOGENEOUS_DENSITY_RETAINS_RELATIVE_AND_DIMENSIONLESS_GEOMETRY
+ MORE_GRAPH_STATISTICS_CANNOT_SELF_CALIBRATE_ABSOLUTE_SCALE
+ FIXED_FUNDAMENTAL_DENSITY_BREAKS_THE_GAUGE_BY_ASSUMPTION
+ FIXED_DIMENSIONFUL_MARK_BREAKS_THE_GAUGE_CONDITIONALLY
+ COVARYING_MARK_RESTORES_THE_GAUGE
+ MARK_FORMATION_PROVENANCE_ACCESS_AND_PHYSICAL_SELECTION_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-111` showed that selected cell-count means contain only the products
\(\rho V\). `HC-DU-112` strengthens that result from a finite statistic to the
**complete random ordered-event law**.

Let \(M\) be a \(d\)-dimensional Lorentzian manifold with metric \(g\), and
sprinkle events by a Poisson point process of homogeneous density \(\rho\).
For every \(c>0\), define

\[
g'=c^2g,
\qquad
\rho'=\frac{\rho}{c^d}.
\tag{1}
\]

Then:

1. \(g\) and \(g'\) have exactly the same causal order;
2. their Poisson intensity measures are exactly equal; and therefore
3. the complete induced unmarked causal-set laws are exactly equal.

Consequently:

> No statistic, graph invariant, consensus summary, estimator, or learning
> algorithm that sees only the complete unmarked causal set can identify
> absolute length, time, volume, or curvature scale.

This is stronger than finite-count underidentification. It is equality of the
complete statistical experiment.

With homogeneous but unknown density, relative and dimensionless geometry can
survive. If density may instead vary regionally, the same argument absorbs an
arbitrary positive local conformal factor:

\[
g'=\Omega^2g,
\qquad
\rho'(x)=\frac{\rho(x)}{\Omega(x)^d}.
\tag{2}
\]

The escape is also exact. A fixed density, mass, clock period, correlation
length, or other independently fixed dimensionful physical relation can break
the gauge. Merely adding a mark does not suffice: if its dimensionful
parameter covaries with the metric, the gauge returns.

The result does not establish that causal sets lack physical scale. It says
where the scale comes from:

> Absolute scale is supplied or dynamically selected by a scale-bearing
> physical structure; it is not self-calibrated by the unmarked order-and-count
> law.

## 1. Controlled object

Freeze:

- a measurable \(d\)-dimensional Lorentzian manifold \(M\);
- a Lorentzian metric \(g\);
- its chronological relation \(\prec_g\);
- measurable regions whose definition does not import the held-out metric
  normalization;
- a Poisson point process \(\Pi_{g,\rho}\) with intensity measure
  \[
  \Lambda_{g,\rho}(A)
  =
  \int_A\rho\,d\mathrm{vol}_g;
  \tag{3}
  \]
- the unlabelled locally finite partial order obtained by restricting
  \(\prec_g\) to the sprinkled points;
- every statistic whose input is only that unmarked ordered event set; and
- absolute geometry, relative geometry, and dimensionless geometry as
  different targets.

The founding causal-set architecture gives causal order and number distinct
roles in approximating spacetime geometry
([Bombelli--Lee--Meyer--Sorkin](https://doi.org/10.1103/PhysRevLett.59.521)).
Poisson sprinkling supplies the standard covariant number-volume
correspondence, and its special status under strong small-region
number-volume requirements has been characterized precisely
([Saravani--Aslanbeigi](https://arxiv.org/abs/1403.6429)).

This result does not challenge that architecture. It asks which part carries
the unit of scale.

## 2. Complete-law global scale-gauge theorem

### Theorem

Let

\[
\mathcal E(g,\rho)
\]

denote the probability law of the complete unmarked Poisson causal set on
\((M,g)\) at homogeneous density \(\rho>0\). In dimension \(d\), for every
\(c>0\),

\[
\mathcal E(g,\rho)
=
\mathcal E(c^2g,\rho/c^d).
\tag{4}
\]

### Proof

A positive conformal rescaling preserves timelike, null, and spacelike
directions. In particular,

\[
\prec_{c^2g}
=
\prec_g.
\tag{5}
\]

The volume measure scales as

\[
d\mathrm{vol}_{c^2g}
=
c^d d\mathrm{vol}_g.
\tag{6}
\]

Therefore the transformed intensity measure is

\[
\begin{aligned}
\Lambda_{c^2g,\rho/c^d}
&=
\frac{\rho}{c^d}d\mathrm{vol}_{c^2g}\\
&=
\frac{\rho}{c^d}c^d d\mathrm{vol}_g\\
&=
\rho d\mathrm{vol}_g\\
&=
\Lambda_{g,\rho}.
\end{aligned}
\tag{7}
\]

A Poisson point-process law is determined by its intensity measure. For
example, its Laplace functional is

\[
\mathbb E\!\left[
\exp\!\left(-\int f\,d\Pi\right)
\right]
=
\exp\!\left(
-\int_M(1-e^{-f})\,d\Lambda
\right).
\tag{8}
\]

Equation (7) makes every such functional identical. Thus the complete random
point-set laws coincide. Equation (5) makes the deterministic order relation
applied to each realized point set coincide. Pushing the same point-process
law through the same order map yields equation (4). \(\square\)

### What “complete law” adds

The theorem is not restricted to:

- one region;
- cell cardinalities;
- means or variances;
- one finite sample size;
- one graph statistic; or
- one estimator family.

It covers the joint distribution of the entire unmarked ordered event set in
the frozen arena.

## 3. Data-processing corollary

Let \(S\) be any measurable statistic of the unmarked causal set. It may
return:

- cardinality;
- interval populations;
- ordering fractions;
- chain or antichain summaries;
- suborder frequencies;
- degree or neighborhood profiles;
- a dimension estimate;
- a graph embedding;
- a regional consensus output;
- a neural representation; or
- a randomized estimate using independent algorithmic randomness.

From equation (4),

\[
S_*\mathcal E(g,\rho)
=
S_*\mathcal E(c^2g,\rho/c^d).
\tag{9}
\]

Thus \(S\) has the same distribution in both models.

### Corollary

> More computation over the same unmarked causal set cannot self-calibrate
> absolute scale.

This is not a computational-complexity limit. It is statistical
nonidentifiability: there is no different signal for a more powerful
algorithm to extract.

The result also covers distributed algorithms. Hashes, gossip histories,
threshold certificates, Byzantine finality, or hypergraph summaries can
certify and compose functions of the event network. They cannot create an
absolute-scale distinction absent from the complete input law.

## 4. Local conformal extension

The constant transformation in equation (1) is the surviving gauge when
density is required to be homogeneous.

If a positive density field \(\rho(x)\) is instead admitted, let

\[
g'=\Omega^2g,
\qquad
\rho'(x)=\Omega(x)^{-d}\rho(x),
\tag{10}
\]

for any positive smooth \(\Omega\).

Conformal rescaling still preserves causal order, while

\[
d\mathrm{vol}_{g'}
=
\Omega^d d\mathrm{vol}_g.
\tag{11}
\]

Therefore

\[
\rho'(x)d\mathrm{vol}_{g'}
=
\rho(x)d\mathrm{vol}_g.
\tag{12}
\]

The complete point-process and causal-set laws are again identical.

### Scoped extension

> If the event-density field is unrestricted, the complete unmarked
> order-and-number law is blind to local conformal scale as well as global
> scale.

This sharpens the dependency:

| Density class | Geometry retained by the complete unmarked law |
|---|---|
| Fixed known \(\rho\) | Volume scale is statistically calibrated |
| Homogeneous unknown \(\rho\) | Relative conformal shape can survive; one global scale is hidden |
| Unrestricted unknown \(\rho(x)\) | Local conformal factor can be absorbed pointwise |

Homogeneity is therefore not a minor statistical convenience. It is a
physical restriction on the completion class.

## 5. What remains identifiable

The theorem does not erase every geometric target.

Under the global transformation:

- causal order is identical;
- spacetime dimension can remain identifiable under the appropriate
  manifoldlike and sampling premises;
- volume ratios are unchanged;
- proper-time ratios are unchanged;
- scale-free shape data can remain;
- topology and conformal structure can remain; and
- dimensionless curvature in discreteness units can remain.

For example, the discreteness length

\[
\ell_\rho=\rho^{-1/d}
\tag{13}
\]

transforms as

\[
\ell_{\rho/c^d}
=
c\ell_\rho.
\tag{14}
\]

Scalar curvature transforms under constant scaling as

\[
R_{c^2g}=c^{-2}R_g.
\tag{15}
\]

Hence

\[
R_g\ell_\rho^2
\tag{16}
\]

is invariant.

The correct conclusion is not “causal sets contain no geometry.” It is:

> The unmarked law naturally carries geometry in its own density units.
> Converting those units into an independently calibrated absolute scale
> requires additional physics.

## 6. Fixed-density class exit

Suppose the theory declares one density \(\rho_*\) to be physically fixed and
does not transform it with \(g\). Then

\[
\Lambda_{c^2g,\rho_*}
=
c^d\Lambda_{g,\rho_*},
\tag{17}
\]

so counts distinguish the two metric scales statistically.

This is a legitimate exit. But it must be typed correctly:

- fixing \(\rho_*\) supplies a dimensionful anchor;
- deriving \(\rho_*\) from independent dynamics would select an anchor;
- estimating \(\rho_*\) from an external calibrated volume would calibrate an
  anchor; and
- merely writing “fundamental density” does not reconstruct the anchor from
  the unmarked causal set.

Local finiteness supplies finite cardinalities for bounded regions. It does
not, by itself, state what one element means in metres or seconds.

## 7. Marked-anchor control

The minimal exit can be illustrated without proposing a new ontology.

For selected timelike-related events \(x\prec y\), add the pair mark

\[
q_m(x,y)
=
\exp[-m\tau_g(x,y)],
\qquad
m>0.
\tag{18}
\]

Treat \(m\) as a fixed known inverse-time scale.

Under

\[
g'=c^2g,
\]

proper time transforms as

\[
\tau_{g'}(x,y)
=
c\tau_g(x,y).
\tag{19}
\]

If \(m\) remains fixed,

\[
q_m'(x,y)
=
\exp[-mc\tau_g(x,y)]
\ne
q_m(x,y)
\tag{20}
\]

for nonzero proper time and \(c\ne1\). The mark distinguishes the scales.
Moreover,

\[
\tau_g(x,y)
=
-\frac{\log q_m(x,y)}m.
\tag{21}
\]

This is conditional Grade-3 reconstruction of selected proper-time intervals
from the supplied calibrated mark.

### Covarying-mark control

If the parameter is allowed to transform as

\[
m'=\frac{m}{c},
\tag{22}
\]

then

\[
q_{m'}^{g'}(x,y)
=
\exp\!\left[
-\frac{m}{c}c\tau_g(x,y)
\right]
=
q_m^g(x,y).
\tag{23}
\]

The gauge returns.

### Marked-anchor necessity rule

> Adding more structure breaks the scale gauge only when at least one
> dimensionful relation is independently fixed rather than transformed along
> the equivalence.

A massive field correlation, clock transition, decay time, action scale, or
other physical candidate may instantiate that role. This swing does not show
that any particular candidate is selected, formed, retained, or accessible.

## 8. Record and access boundary

A substrate mark is not automatically a Dynamic Unity certified record.

To become one, a candidate still needs:

1. **Physical selection.** Why this density, mass, clock, correlation, or
   coupling rather than another?
2. **Formation.** Which interaction creates a retained value?
3. **Occurrence identity.** Which two events or histories does it concern?
4. **Provenance.** How is the value linked to that physical formation path?
5. **Retention.** For what horizon does the mark persist?
6. **Access.** Which observer-indexed operations can retrieve it?
7. **Calibration.** What fixes its units independently of the held-out
   geometry?
8. **Acquisition.** Are every admitted attempt and selection path accounted
   for?
9. **Certification.** Which rival scales or completion models does it exclude,
   at what error?
10. **Capability.** Which matched-resource action becomes possible because of
    the mark?

The complete-law theorem prevents one tempting shortcut: none of those
obligations can be replaced by computing a more elaborate invariant of the
same unmarked causal set.

## 9. Relation to the North Star

The positive North-Star chain is now:

```text
causal order
  + independently calibrated volume measure
  -> full metric up to declared equivalence

unmarked Poisson causal set
  + fixed known density
  -> statistical volume and metric scale

unmarked Poisson causal set
  + unknown homogeneous density
  -> relative/dimensionless geometry only

unmarked Poisson causal set
  + unrestricted density field
  -> causal/conformal geometry only

unmarked Poisson causal set
  + independently fixed accessible dimensionful mark
  -> conditional calibrated intervals
```

This is useful because it separates three questions that were easy to merge:

- Does an event network encode causal and relative geometry?
- Does the physical theory select a dimensionful scale?
- Does an observer obtain a certified record of that scale?

The answer to the first can be positive while the latter two remain open.

## 10. Distributed-systems interpretation

Distributed-systems machinery can improve:

- event identity;
- duplicate suppression;
- provenance;
- authenticated joins;
- eventual or Byzantine finality;
- regional reconciliation;
- access control; and
- safe composition.

Those are real contributions to the record layer.

But if two physical models induce the same complete unmarked event-network
law, every distributed protocol fed only that network also has the same law.
Consensus can stabilize a value relative to an input contract; it cannot
supply a missing dimensionful referent.

This is the exact boundary between:

- **certifying the network one has**, and
- **calibrating what that network means physically**.

The latter requires a scale-bearing physical relation.

## 11. Absorber and novelty audit

### Absorbed components

- causal order is conformally invariant;
- Lorentzian volume has conformal weight \(d\);
- Poisson laws are determined by intensity measures;
- equal statistical experiments remain equal under data processing;
- dimensionless combinations survive unit rescaling; and
- fixed mass, time, or density scales set physical units.

These are standard.

### Dynamic Unity-owned synthesis

The scoped contribution is their composition at the certified-record
boundary:

1. equality is proved for the complete unmarked causal-set law;
2. every possible unmarked graph statistic is eliminated at once;
3. homogeneous and regional density classes are separated;
4. dimensionless reconstruction is preserved rather than wrongly discarded;
5. a fixed versus covarying marked-anchor discriminator is explicit; and
6. physical selection, formation, provenance, access, and calibration remain
   typed obligations.

This is a program-level necessity theorem and research stop, not a new
physical law.

## 12. Claim grading

| Claim | Verdict | Grade |
|---|---|---:|
| Equation (4): complete unmarked Poisson causal-set law is invariant under global metric-density rescaling | proved in the controlled class | 4 |
| Every unmarked statistic is absolute-scale blind | proved by pushforward/data processing | 4 |
| Equation (10): free density field absorbs arbitrary local conformal scale | proved in the controlled class | 4 |
| Relative and dimensionless geometry can survive homogeneous unknown density | proved conditionally | 3 |
| Fixed known density breaks the gauge | proved conditionally; scale supplied | 3 |
| Fixed known pair mark reconstructs selected proper time | proved for the toy mark law | 3 |
| Covarying mark restores the gauge | proved | 4 boundary |
| Causal sets select their fundamental density physically | not established | 0 |
| A physical dimensionful mark is formed, accessible, and certified | not established | 0 |
| New empirical excess over standard physics | not established | 0 |

Maximum earned grade:

> Scoped Grade 4 for complete-law absolute-scale nonidentifiability, its local
> conformal extension, and scale-anchor necessity; conditional Grade 3 for
> reconstruction from an independently fixed mark.

No Grade-5 remainder or prediction is earned.

## 13. Falsifiers and reopeners

The theorem is falsified in its declared class by any of:

- positive constant conformal scaling changing causal order;
- the compensated transformation changing the intensity measure;
- equal point-process and order laws yielding different statistic laws; or
- a fixed dimensionful mark remaining unchanged when its measured interval
  changes.

The research branch reopens constructively with:

> A physical theory that independently selects one dimensionful event density,
> clock, mass, correlation, coupling, or action scale; forms a
> provenance-bearing accessible mark of it; and transfers that unchanged
> through a finite no-refit metric reconstruction packet.

If the supposed anchor can covary with the metric, be refit from the held-out
target, or remain inaccessible to the admitted observer, it does not satisfy
the reopener.

## 14. Practical disposition

Do not:

- search additional unmarked causal-set statistics for absolute scale;
- treat more neural, graph, consensus, or hypergraph sophistication as
  calibration;
- import a Planck or discreteness scale and call it reconstructed;
- confuse physical substrate marks with observer records; or
- simulate a larger causal set to decide an exact law equality.

Do:

- preserve causal-set reconstruction of relative/dimensionless geometry;
- state explicitly whether density is fixed, homogeneous unknown, or locally
  variable;
- identify the physical source of any dimensionful anchor;
- test fixed versus covarying behavior before claiming scale selection; and
- require formation, provenance, access, and calibration before calling the
  anchor a certified record.

No scientific successor is selected. The repository returns to explicit
quiescence.

## 15. Executable preservation

`tests/du_causal_set_full_law_scale_gauge_probe.py` preserves:

- exact compensated intensity-measure equality in \(d=4\);
- representative joint Poisson law equality;
- exact causal-order invariance on a finite Minkowski specimen;
- representative unmarked graph-statistic invariance;
- regional density absorption of local conformal factors;
- invariant volume ratios and curvature in discreteness units;
- fixed-mark gauge breaking;
- covarying-mark gauge restoration; and
- conditional proper-time recovery from a fixed known mark.

The deterministic receipt is
`tests/artifacts/du_causal_set_full_law_scale_gauge_result.json`.

Passing earns no physical density, mark, clock, mass, interface, formation,
provenance, access, certified record, new physics, prediction, or evidence
grade.
