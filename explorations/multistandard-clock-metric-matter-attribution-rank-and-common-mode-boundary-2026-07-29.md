---
title: "Multi-standard clock metric--matter attribution rank and universal common-mode boundary"
status: completed_scoped_result
doc_type: north_star_metric_reconstruction_theorem_primary_source_collision_and_exact_controls
created: 2026-07-29
hypothesis_id: HC-DU-114
run_id: RUN-20260729-093419-multistandard-clock-attribution-rank
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 metric--matter attribution-rank and universal-common-mode necessity boundary, with conditional Grade 3 redshift reconstruction in one frozen nuisance class; no selected clock interface, new law, new physics, or prediction"
probe: "../tests/du_multistandard_clock_metric_matter_rank_probe.py"
artifact: "../tests/artifacts/du_multistandard_clock_metric_matter_rank_result.json"
---

# Multi-standard clock metric--matter attribution rank

## Executive result

The swing returned:

```text
ONE_CLOCK_CONDITIONALLY_MEASURES_REDSHIFT_ONLY_WHEN_MATTER_LAW_IS_FROZEN
+ ONE_CLOCK_CONFOUNDS_REDSHIFT_WITH_ADMITTED_LOCAL_MATTER_DRIFT
+ FULL_RECONSTRUCTION_IFF_AUGMENTED_SENSITIVITY_MATRIX_HAS_FULL_COLUMN_RANK
+ TARGET_ONLY_RECONSTRUCTION_IFF_TARGET_ROW_LIES_IN_RECORD_ROW_SPACE
+ TWO_DISTINCT_SENSITIVITIES_ARE_MINIMAL_FOR_ONE_NUISANCE_DIRECTION
+ CLOCK_RATIOS_CANCEL_METRIC_COMMON_MODE_AND_DIAGNOSE_DIFFERENTIAL_MATTER_DRIFT
+ IDENTICAL_OR_NEARLY_PARALLEL_SENSITIVITIES_FAIL_OR_DESTABILIZE_ATTRIBUTION
+ THREE_SPECIES_CAN_SEPARATE_REDSHIFT_ALPHA_AND_MASS_RATIO_IN_A_FROZEN_LINEAR_CLASS
+ UNIVERSAL_FREQUENCY_DRIFT_REMAINS_EXACTLY_CONFOUNDED_WITH_REDSHIFT
+ JOINT_FORMATION_TRANSFER_PROVENANCE_ACCESS_AND_SYSTEMATICS_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-113` showed that a fixed realized matter scale can calibrate intervals
without first deriving the ultimate origin of that scale. This swing asks what
“fixed” must mean when the matter law itself is admitted to vary.

The answer is sharper than “use a better clock”:

1. **One clock measures a combined response.** Its phase or frequency record
   combines proper-time redshift with any local change in the transition law.
   If such a matter-law change is admitted, one clock does not identify which
   contribution occurred.
2. **A clock family is an attribution instrument.** For \(p\) frozen nuisance
   directions, redshift plus all nuisances are reconstructed exactly when the
   augmented sensitivity matrix \([\mathbf 1\;K]\) has rank \(p+1\).
3. **Ratios do a different job.** Comparing two species cancels the common
   metric contribution and exposes differential matter sensitivity. A ratio
   is therefore excellent for testing varying constants, but is not by itself
   a redshift record.
4. **A universal common mode survives every clock family.** A multiplicative
   drift shared identically by all transition frequencies has the same record
   column as metric redshift. No number of clock species separates them using
   clock records alone.
5. **The physical interface remains unselected.** The atoms, interrogations,
   transfer channel, joined archive, sensitivity calibration, systematics,
   and admitted nuisance class must all be physically formed and frozen.

The central correction is:

> Dynamic Unity's scale anchor is not one number carried by one object. It is
> a jointly realizable metrological relation: a clock family, comparison
> process, nuisance contract, provenance-bearing archive, and one explicit
> universal-common-mode quotient or external anchor.

This is a program dependency refinement, not a new clock theorem or a new
prediction.

## 1. Primary-source collision

### Clocks physically resolve gravitational redshift

Bothwell et al. resolved the gravitational redshift across a millimetre-scale
strontium optical lattice sample
([Nature 602, 420--424](https://doi.org/10.1038/s41586-021-04349-7)).
The result demonstrates that atomic transitions can instantiate an extremely
sensitive local proper-time comparator.

It does not establish that every observed frequency change is uniquely
geometric under an unrestricted matter-law class. That inference uses local
position invariance and a calibrated transition model.

### Different clocks have different matter sensitivities

Rosenband et al. compared the \(^{27}\mathrm{Al}^{+}\) and
\(^{199}\mathrm{Hg}^{+}\) optical-clock frequencies and used their ratio to
constrain temporal variation of the fine-structure constant
([Science 319, 1808--1812](https://doi.org/10.1126/science.1154622);
[NIST record](https://www.nist.gov/publications/frequency-ratio-al-and-hg-single-ion-optical-clocks-metrology-17th-decimal-place)).

The scientific power comes from unequal dependence of the two transitions on
the same dimensionless parameter. A common frequency contribution cancels in
the ratio.

### Multi-species sensitivity is already an experimental method

Sherrill et al. analyze \(^{87}\mathrm{Sr}\), \(^{171}\mathrm{Yb}^{+}\), and
\(^{133}\mathrm{Cs}\) clock data with distinct sensitivities to the
fine-structure constant and electron-to-proton mass ratio
([*Analysis of atomic-clock data to constrain variations of fundamental
constants*](https://arxiv.org/abs/2302.04565)). Their table gives, to the
reported precision:

| clock | alpha sensitivity | mass-ratio sensitivity |
|---|---:|---:|
| \(^{87}\mathrm{Sr}\) | \(2+0.06\) | \(0\) |
| \(^{171}\mathrm{Yb}^{+}\) | \(2-5.95\) | \(0\) |
| \(^{133}\mathrm{Cs}\) | \(2+2.83\) | \(1\) |

This is the physical absorber for the finite three-species control below.
Dynamic Unity does not own the coefficients, varying-constants method, or
experimental constraints.

## 2. Frozen typed clock record

Let two declared regions be compared during one frozen epoch. For each clock
species \(s=1,\ldots,S\), let

\[
y_s
\]

be the formed, corrected small fractional frequency or phase shift between
the regions.

Freeze:

- the paths and regions;
- the proper-time/redshift target \(z\);
- \(p\) dimensionless matter-law nuisance coordinates
  \(\theta=(\theta_1,\ldots,\theta_p)\);
- calibrated sensitivities \(K_{sa}\);
- the clock preparations and interrogations;
- the local oscillators and readout maps;
- the frequency-transfer or transport process;
- the epoch and synchronization convention;
- systematic-error bounds;
- complete joined acquisition;
- provenance identifying species, location, route, setting, and trial; and
- the observer/access/resource contract.

The local linear model is

\[
y_s
=
z+\sum_{a=1}^{p}K_{sa}\theta_a.
\tag{1}
\]

In vector form,

\[
y=Ax,
\qquad
x=
\begin{pmatrix}
z\\
\theta
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
\mathbf 1&K
\end{pmatrix}.
\tag{2}
\]

The column of ones expresses the equivalence-principle prediction that metric
redshift is common to every ideal clock species. The \(K\) columns express
species-dependent matter response.

Equation (1) is exact inside the declared finite linear specimen. It is a
linearized physical model, not an assertion that every possible clock or
matter deformation belongs to a finite vector space.

## 3. Full attribution theorem

### Theorem 1

The joined clock record reconstructs \(z\) and every declared nuisance
coordinate exactly if and only if

\[
\operatorname{rank}A=p+1.
\tag{3}
\]

### Proof

Full reconstruction means the map \(x\mapsto Ax\) is injective. A linear map
from \(\mathbb R^{p+1}\) is injective exactly when its kernel is trivial,
equivalently when it has full column rank \(p+1\). \(\square\)

### Consequences

- At least \(p+1\) scalar clock records are necessary.
- Having \(S\ge p+1\) records is not sufficient; their sensitivity rows must
  be independent after adding the common metric column.
- Repeating one species improves statistical precision but does not add
  attribution rank.
- A formally full-rank clock list is not yet a jointly realizable record. The
  comparisons and archive must coexist inside one resource contract.

This is standard observability mathematics. Its DU role is to expose the
minimum physical record architecture hidden inside “use a matter standard.”

## 4. Target-only reconstruction

Dynamic Unity need not always reconstruct every nuisance parameter. Let a
held-out linear target be

\[
T(x)=tx.
\]

### Theorem 2

The target factors through the clock record if and only if

\[
\ker A\subseteq\ker t,
\tag{4}
\]

equivalently

\[
t\in\operatorname{rowspan}A.
\tag{5}
\]

This is the existing `HC-DU-039C` factorization theorem applied to the
physical clock family.

For redshift alone,

\[
t_z=(1,0,\ldots,0).
\]

Thus a clock family can fail to identify every nuisance while still
reconstructing redshift, but only if every unresolved direction has zero
redshift component. This condition must be checked rather than assumed.

## 5. Smallest one-clock obstruction

For one nuisance coordinate,

\[
y=z+k\theta.
\tag{6}
\]

If \(k\ne0\), then for every \(\delta\),

\[
(z,\theta)
\mapsto
(z-k\delta,\theta+\delta)
\tag{7}
\]

preserves \(y\).

The kernel contains

\[
(-k,1),
\]

whose redshift component is nonzero. Therefore:

> One clock cannot distinguish metric redshift from one admitted local
> matter-law change to which that clock is sensitive.

This does not invalidate ordinary clock redshift measurements. It states
their exact conditional:

> One clock measures redshift relative to a frozen transition law and
> controlled systematics.

If \(\theta\) is excluded by the physical contract, equation (6) reduces to
\(y=z\) and the clock conditionally reconstructs redshift.

## 6. Minimal two-clock repair

For two species and one nuisance,

\[
\begin{pmatrix}
y_1\\
y_2
\end{pmatrix}
=
\begin{pmatrix}
1&k_1\\
1&k_2
\end{pmatrix}
\begin{pmatrix}
z\\
\theta
\end{pmatrix}.
\tag{8}
\]

The determinant is

\[
k_2-k_1.
\tag{9}
\]

Therefore reconstruction is exact if and only if

\[
k_1\ne k_2.
\tag{10}
\]

The decoder is

\[
\theta
=
\frac{y_2-y_1}{k_2-k_1},
\qquad
z
=
\frac{k_2y_1-k_1y_2}{k_2-k_1}.
\tag{11}
\]

### Stability

If each clock record has absolute error at most \(\varepsilon\), then

\[
|\Delta\theta|
\le
\frac{2\varepsilon}{|k_2-k_1|},
\tag{12}
\]

and

\[
|\Delta z|
\le
\frac{|k_1|+|k_2|}{|k_2-k_1|}\varepsilon.
\tag{13}
\]

Distinct sensitivity is therefore a qualitative requirement; well-separated
sensitivity is the quantitative requirement. Near-parallel clock standards
are mathematically invertible but experimentally fragile.

## 7. What clock ratios do

Subtracting the two rows gives

\[
y_2-y_1
=
(k_2-k_1)\theta.
\tag{14}
\]

The metric redshift cancels exactly.

This is why clock ratios are powerful varying-constants probes. It also
prevents a category error:

\[
\text{differential clock ratio}
\ne
\text{metric-redshift record}.
\]

A ratio diagnoses the matter-law direction. The common-mode combination is
then required to recover redshift.

## 8. Three-species finite control

Freeze two nuisance coordinates:

- a fractional fine-structure variation; and
- an electron-to-proton mass-ratio variation.

Using the rounded literature sensitivity pattern, the augmented matrix is

\[
A_{\mathrm{clock}}
=
\begin{pmatrix}
1&2.06&0\\
1&-3.95&0\\
1&4.83&1
\end{pmatrix}.
\tag{15}
\]

Its determinant is nonzero:

\[
\det A_{\mathrm{clock}}=-6.01.
\tag{16}
\]

Thus the three joined records conditionally reconstruct:

\[
(z,\Delta\alpha/\alpha,\Delta\mu/\mu)
\]

inside this frozen linear class.

This is not a claim that these three clocks reconstruct geometry under every
possible Standard-Model, environmental, scalar-field, or apparatus
deformation. Adding another independent nuisance column can immediately make
the same three-record system underdetermined. The nuisance class is part of
the theorem statement.

## 9. Universal common-mode no-go

Now admit a universal fractional drift \(u\) that changes every clock
frequency equally:

\[
y_s
=
z+u+\sum_aK_{sa}\theta_a.
\tag{17}
\]

The augmented matrix is

\[
\widetilde A
=
\begin{pmatrix}
\mathbf 1&\mathbf 1&K
\end{pmatrix}.
\tag{18}
\]

The first two columns are identical. Therefore

\[
(1,-1,0,\ldots,0)
\in
\ker\widetilde A.
\tag{19}
\]

The redshift changes along this kernel direction.

### Theorem 3

> No number of clock species or repeated clock measurements can distinguish
> metric redshift from a universal multiplicative drift shared identically by
> every admitted clock frequency using clock-only records.

This is the clock realization of `HC-DU-113`'s common-unit boundary.

- If the universal change is a rescaling of every admitted dimensional
  quantity, it is unit gauge.
- If another sector remains fixed, the change is a physical inter-sector
  ratio, but clock-only records still do not identify whether it belongs to
  geometry or universal matter drift.

The repair requires one of:

- exclude \(u\) through a warranted local-position-invariance contract;
- quotient it as common-unit gauge;
- add a non-clock physical anchor with a different sensitivity;
- add a source model that ties \(u\) to other observables; or
- weaken the target to the identifiable combination \(z+u\).

No vocabulary choice removes the rank defect.

## 10. Physical formation ladder

A clock transition is not yet a record. The required physical chain is:

```text
stable physical transition family
  -> prepared clock state
  -> proper-time phase accumulation
  -> interrogation against a local oscillator
  -> outcome readout
  -> remote transport or frequency-transfer comparison
  -> joined species/location/route/epoch archive
  -> calibrated sensitivity and systematic-error certificate
  -> observer-accessible regional metric--matter record
```

Every arrow carries a separate failure mode.

### Preparation

The species, state, trap, field environment, temperature, interrogation
sequence, and reference oscillator must be declared. A reproducible
transition is a physical scale carrier, not a self-certifying archive.

### Transport or transfer

A transportable clock carries apparatus and its environmental history. A
remote comparison carries frequency through an optical, microwave, satellite,
or other link. Link asymmetry, latency, phase slips, path changes, and
selection can mimic or erase the target unless bounded.

### Joined acquisition

Multiple individually valid clocks do not form one record unless their
results share occurrence identity, epoch, route, settings, and compatible
acquisition. This is the physical content of the admissible-record envelope.

### Sensitivity calibration

The \(K\) matrix is imported from atomic/nuclear theory and calibration. If it
is refitted after observing the target, the reconstruction is circular. Its
uncertainty belongs in the inverse margin.

### Nuisance completeness

Full rank relative to a hand-picked \(K\) does not prove nature contains no
other nuisance direction. The declared class must be independently warranted
and adversarially enlarged before a physical remainder or unrestricted metric
claim is earned.

## 11. Relation to prior Dynamic Unity results

### `HC-DU-113`

`HC-DU-113` required one fixed realized matter mark. The present result
replaces “fixed” with an operational contract:

\[
\text{fixed relative to}
\quad
\{\text{nuisance class, sensitivity matrix, comparison process, archive}\}.
\]

### `HC-DU-039C`

The generic source-attribution rank theorem now has a concrete physical
target. A measured clock phase is not automatically an attributed proper-time
phase.

### Admissible-record envelope

Adding clock species changes the resource and interface class. The
reconstruction belongs to the joined multi-clock contract, not to any
individual clock and not to a counterfactual tuple of separately run records.

### `HC-DU-110--112`

The event network supplies causal/conformal structure but lacks scale. Clock
families can conditionally supply scale and diagnose selected matter drift,
but a universal scale direction survives. This is consistent rather than
contradictory:

```text
causal/conformal event record
  + formed full-rank clock-family record
  + universal-common-mode quotient or anchor
  -> conditional metric reconstruction
```

## 12. Absorption and novelty

### Standard/absorbed content

- gravitational redshift with atomic clocks;
- optical-clock sensitivity to dimensionless constants;
- frequency-ratio common-mode cancellation;
- multi-species varying-constants analysis;
- linear rank, kernel, and conditioning theorems;
- equivalence-principle and local-position-invariance tests; and
- standard metrological systematics.

### Dynamic Unity-owned synthesis

The project-native contribution is the typed boundary:

1. physical scale carrier is not formed record;
2. one clock is target-sufficient only relative to a frozen matter-law class;
3. every added nuisance direction creates an exact record-rank obligation;
4. added clocks count only when jointly realizable and archived;
5. ratios and common modes carry different target content;
6. universal matter drift and metric redshift define an exact clock-only
   equivalence class; and
7. a record-first geometry theorem must declare whether it quotients,
   externally anchors, or predicts that class.

This is useful and program-sharpening. Its mathematics is not a blockbuster
on its own.

## 13. Claim grading

| Claim | Verdict | Grade |
|---|---|---:|
| Full linear reconstruction iff \([\mathbf1\;K]\) has full column rank | proved / standard | 4 boundary |
| Redshift factors iff its target row lies in the record row space | proved / standard | 4 boundary |
| One clock fails with one admitted nonzero sensitivity | proved exact counterexample | 4 |
| Two distinct sensitivities repair one nuisance | proved conditionally | 3 |
| Clock ratios cancel common metric redshift | proved / standard | absorber |
| Three named sensitivities reconstruct one frozen three-coordinate class | exact finite control | 3 |
| Universal clock drift is confounded with redshift for any clock family | proved in the declared class | 4 |
| Physics selects the clock family, nuisance class, archive, or access route | not established | 0 |
| Unrestricted metric reconstruction | not established | 0 |
| New empirical excess or prediction | not established | 0 |

Maximum earned grade:

> Scoped Grade 4 for the metric--matter rank and universal-common-mode
> necessity boundary; conditional Grade 3 for redshift reconstruction inside
> a frozen finite nuisance and jointly archived clock class.

## 14. Falsifiers and reopeners

The scoped result is falsified by:

- one clock uniquely separating redshift from a free nuisance to which it has
  nonzero sensitivity;
- a rank-deficient augmented matrix possessing an exact full decoder;
- a clock ratio retaining the common metric term in equation (1);
- any clock-only family separating two identical common-mode columns; or
- exact reconstruction surviving a new nuisance direction without added
  record rank or an independently derived constraint.

The physical constructive branch reopens with:

> One predeclared jointly realizable clock family whose preparation,
> interrogation, transport/transfer, complete joined acquisition, provenance,
> sensitivity matrix, nuisance class, systematics, and common-mode quotient or
> external anchor are frozen before a held-out local/regional metric target,
> and whose inverse margin transfers without refit.

No scientific successor is selected by this run.

## 15. Practical disposition

Do not:

- call one clock an unconditional metric sensor;
- call a clock ratio a redshift record;
- add species without checking rank and conditioning;
- concatenate separately unrealizable archives;
- hide matter-law stability inside the word “clock”;
- treat local-position invariance as already derived by DU;
- claim full geometry from a finite nuisance model; or
- request hardware to rediscover the exact rank boundary.

Do:

- state the nuisance class and sensitivity matrix;
- keep differential matter tests separate from metric common mode;
- use at least \(p+1\) jointly formed independent records for \(p\) nuisance
  directions when full attribution is required;
- propagate calibration and record error through the inverse margin;
- declare the universal-common-mode quotient or external anchor;
- preserve species/location/epoch/route provenance; and
- transfer the frozen instrument to a held-out regional geometry.

The repository returns to explicit quiescence.

## 16. Executable preservation

`tests/du_multistandard_clock_metric_matter_rank_probe.py` preserves:

- the one-clock same-record/different-redshift witness;
- conditional one-clock reconstruction under a frozen matter law;
- the two-clock one-nuisance repair;
- repeated-species rank failure;
- clock-ratio metric cancellation;
- the three-species frozen linear control;
- the two-clock/two-nuisance rank deficit;
- the universal-common-mode counterexample; and
- inverse-error amplification for nearly parallel sensitivities.

The deterministic receipt is
`tests/artifacts/du_multistandard_clock_metric_matter_rank_result.json`.

Passing earns no physical clock selection, formation, transport, joined
archive, provenance, access, unrestricted matter-law control, natural metric
reconstruction, new physics, prediction, evidence grade, or
external-hardware result.
