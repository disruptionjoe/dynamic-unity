---
title: "QCD dimensional transmutation: operational metric anchor and scale-origin boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-113
work_id: CCR-QCD-DIMENSIONAL-TRANSMUTATION-METRIC-ANCHOR-AND-SCALE-ORIGIN-GATE
run_id: RUN-20260729-091617-qcd-dimensional-transmutation-scale-gate
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
maximum_grade: "Scoped Grade 4 RG scale-provenance and common-unit-gauge boundary, with conditional Grade 3 metric reconstruction in fixed physical-matter units; no Grade-5 remainder, new law, or prediction"
---

# QCD dimensional transmutation: operational metric anchor and scale-origin boundary

## Executive result

The swing returned:

```text
ASYMPTOTIC_FREEDOM_YIELDS_AN_RG_INVARIANT_SCALE_COORDINATE
+ BETA_FUNCTION_LEAVES_ONE_DIMENSIONFUL_INTEGRATION_CONSTANT_FREE
+ DIMENSIONAL_TRANSMUTATION_REPARAMETERIZES_RATHER_THAN_ELIMINATES_SCALE_INPUT
+ SCHEME_CHANGE_RESCALES_LAMBDA_WHILE_PHYSICAL_MASS_RATIOS_SURVIVE
+ LATTICE_QCD_REQUIRES_ONE_MEASURED_DIMENSIONFUL_INPUT_FOR_PHYSICAL_UNITS
+ FIXED_PHYSICAL_MATTER_MARK_BREAKS_THE_METRIC_SCALE_GAUGE
+ JOINT_RESCALING_OF_METRIC_AND_ALL_ADMITTED_SCALES_PRESERVES_DIMENSIONLESS_MARKS
+ PARTIAL_RESCALING_AGAINST_A_FIXED_SECTOR_CHANGES_A_PHYSICAL_RATIO
+ LOCAL_CONFORMAL_SCALE_REMAINS_TESTABLE_AGAINST_A_TRANSPORTED_FIXED_MARK
+ QCD_CAN_CLOSE_OPERATIONAL_SCALE_RECONSTRUCTION_WITHOUT_EXPLAINING_SCALE_ORIGIN
+ MARK_FORMATION_PROVENANCE_ACCESS_AND_NO_REFIT_TRANSFER_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-112` proved that the complete unmarked Poisson causal-set law cannot
self-calibrate absolute metric scale. This swing tests QCD dimensional
transmutation as the strongest familiar candidate for the missing
scale-bearing physical mark.

The answer is not simply positive or negative:

1. **QCD supplies real scale-bearing physics.** Quantum running replaces a
   dimensionless coupling coordinate with an RG-invariant scale
   \(\Lambda\). Hadron masses and correlation scales instantiate physical
   standards.
2. **The beta function does not select the absolute value of \(\Lambda\).**
   Its value is an integration constant, equivalently fixed by the coupling
   at one reference energy or by one measured dimensionful observable.
3. **That does not block Dynamic Unity's operational reconstruction.** A
   fixed realized mass or transition scale breaks the `HC-DU-112` metric
   gauge and measures intervals in matter units.
4. **Co-rescaling metric intervals and every admitted dimensionful scale
   according to physical dimension is a common-unit change.** No
   dimensionless observation changes, so it is representation gauge inside
   the closed contract rather than a physical remainder. If any other
   admitted scale is held fixed, the changing inter-sector ratio is physical.
5. **Local scale variation remains physical.** One global unit change cannot
   absorb unequal regional conformal factors against the same transported
   matter standard.

The key correction is:

> Dynamic Unity need not explain the ultimate origin of every dimensionful
> constant before reconstructing observer-accessible geometry. It must recover
> geometry relative to a physically stable matter standard and quotient one
> common global unit conversion.

The remaining burden is concrete: form, transport, retain, access, and
certify such a standard without local refit.

## 1. Primary-source collision

Gross and Wilczek and, independently, Politzer established asymptotic freedom
for non-Abelian gauge theories
([Gross--Wilczek](https://doi.org/10.1103/PhysRevLett.30.1343),
[Politzer](https://doi.org/10.1103/PhysRevLett.30.1346)).
Their result determines the ultraviolet running law; it does not choose one
RG trajectory's dimensional integration constant.

Lattice QCD demonstrates that QCD dynamics reproduces the observed light
hadron spectrum after its physical inputs are fixed
([Dürr et al.](https://arxiv.org/abs/0906.3599)). That paper explicitly lists
the light and strange quark masses and the coupling as inputs to its full
calculation.

The scale-setting literature states the remaining dependency directly.
Borsanyi et al. describe QCD as having quark masses and an overall scale and
explain that a dimensionful observable at known energy must be matched to
express lattice results in physical units. Their implementation uses the
\(\Omega\)-baryon mass to set that scale
([Borsanyi et al.](https://arxiv.org/abs/1203.4469)).

Renormalization-scheme work likewise distinguishes the convention-dependent
coupling and \(\Lambda\) parameter from physical observables
([Boito--Jamin--Miravitllas](https://arxiv.org/abs/1612.01792)).

These sources already contain the component facts. Dynamic Unity's work is to
type their consequence for record-based geometry.

## 2. One-loop scale-provenance theorem

Consider the asymptotically free one-coupling equation

\[
\mu\frac{dg}{d\mu}
=
-b_0g^3,
\qquad
b_0>0.
\tag{1}
\]

Separating variables gives

\[
\frac{dg}{g^3}
=
-b_0\frac{d\mu}{\mu}.
\]

Integration yields

\[
\frac1{g^2(\mu)}
=
2b_0\log\frac{\mu}{\Lambda},
\tag{2}
\]

where \(\Lambda>0\) is an integration constant. Equivalently,

\[
\Lambda
=
\mu\exp\!\left[
-\frac1{2b_0g^2(\mu)}
\right].
\tag{3}
\]

Equation (3) is independent of the chosen point \(\mu\) along one RG
trajectory.

### What the beta function selects

The beta function selects:

- the direction of running;
- the shape of \(g(\mu/\Lambda)\);
- the ultraviolet fixed-point behavior;
- relations between coupling values at different energy ratios; and
- conditional dimensionless predictions once the trajectory is fixed.

### What it does not select

For every \(\Lambda>0\), equation (2) gives a distinct trajectory satisfying
the same beta law. Therefore the beta function does not select:

- the origin of the logarithmic energy coordinate;
- the numerical value of \(\Lambda\);
- the coupling at one fixed external energy; or
- a dimensionless ratio between \(\Lambda\) and an independently fixed
  electroweak, gravitational, or other-sector scale.

### Scoped theorem

> The asymptotically free beta function generates an RG-invariant
> dimensionful coordinate but leaves its one integration constant free.

This is a necessity statement, not a criticism of QCD.

## 3. Dimensional transmutation is a parameter exchange

Fix a reference energy \(\mu_0\). Equation (3) gives a one-to-one map

\[
g(\mu_0)
\longleftrightarrow
\Lambda.
\tag{4}
\]

Specifying the dimensionless coupling at a dimensionful reference point and
specifying the dimensionful transmutation scale carry the same trajectory
information.

Thus dimensional transmutation:

- removes the classical appearance that no scale can occur;
- converts the anomaly and running into physical scale dependence;
- explains why masses and correlation lengths can arise without a classical
  mass term in the pure gauge action; but
- does not reduce the number of physical inputs needed to locate the
  trajectory.

### Correct formulation

> Dimensional transmutation generates physical scale structure while
> reparameterizing, rather than uniquely selecting, the remaining overall
> scale input.

This avoids two opposite mistakes:

- calling QCD mass generation a mere relabel; and
- claiming the beta function predicts the universe's absolute scale from no
  boundary data.

## 4. Scale covariance of the RG family

Equation (2) depends only on the ratio \(\mu/\Lambda\). Hence

\[
g_{\Lambda/c}(\mu/c)
=
g_\Lambda(\mu)
\tag{5}
\]

for every \(c>0\).

All dimensionless running-coupling observations are invariant when every
energy is expressed in a unit scaled by the same factor.

This is the RG analogue of the `HC-DU-112` common scale orbit. The beta law
provides rich relative structure along the orbit without choosing its global
normalization.

## 5. Scheme-dependent \(\Lambda\), physical observables

At one-loop order, write

\[
u=\frac1{g^2}.
\]

A finite coupling redefinition induces an asymptotic shift

\[
u'=u-2a.
\tag{6}
\]

Using equation (2),

\[
2b_0\log\frac{\mu}{\Lambda'}
=
2b_0\log\frac{\mu}{\Lambda}-2a,
\]

and therefore

\[
\Lambda'
=
e^{a/b_0}\Lambda.
\tag{7}
\]

The numerical \(\Lambda\) parameter depends on renormalization convention.
It is not itself the record target.

For a physical mass in a one-scale pure theory, write

\[
M_i
=
C_i^{(S)}\Lambda_S.
\tag{8}
\]

Under a scheme change,

\[
\Lambda_{S'}
=
k\Lambda_S,
\qquad
C_i^{(S')}
=
\frac1kC_i^{(S)}.
\tag{9}
\]

Then

\[
M_i^{(S')}
=
M_i^{(S)}
\tag{10}
\]

and

\[
\frac{M_i}{M_j}
=
\frac{C_i^{(S)}}{C_j^{(S)}}
\tag{11}
\]

is scheme independent.

### Dynamic Unity typing

- \(\Lambda_S\) is a useful representation coordinate.
- A physical pole mass, transition frequency, decay scale, or correlation
  length is the candidate physical mark.
- A dimensionless ratio of such observables is the invariant target.

Treating \(\Lambda_{\overline{\mathrm{MS}}}\) itself as a directly formed
record would conflate representation and observable.

## 6. Lattice scale-setting control

A lattice calculation naturally returns dimensionless quantities such as

\[
aM_i,
\tag{12}
\]

where \(a\) is the lattice spacing.

Mass ratios are available without fixing \(a\):

\[
\frac{M_i}{M_j}
=
\frac{aM_i}{aM_j}.
\tag{13}
\]

To express \(a\) in physical units, choose one measured reference mass
\(M_*\):

\[
a
=
\frac{aM_*}{M_*^{\mathrm{measured}}}.
\tag{14}
\]

Then every other mass follows:

\[
M_i
=
\frac{aM_i}{a}.
\tag{15}
\]

Without the measured reference,

\[
a\mapsto ca,
\qquad
M_i\mapsto M_i/c
\tag{16}
\]

preserves every dimensionless lattice output.

This is not a weakness of lattice QCD. It is the operational structure of all
dimensional measurement:

> Theory predicts relations; one physical standard fixes their unit
> realization.

The lattice literature is therefore a direct positive control for the
Dynamic Unity scale boundary.

## 7. Matter-mark metric reconstruction

Let \(M_*>0\) be one fixed physical mass or transition energy. On a selected
timelike relation, use the controlled mark

\[
q_*(x,y)
=
\exp[-M_*\tau_g(x,y)].
\tag{17}
\]

This is a schematic correlation/phase-decay mark, not a claim that every
hadron is a clock.

When \(M_*\) is fixed and known,

\[
\tau_g(x,y)
=
-\frac{\log q_*(x,y)}{M_*}.
\tag{18}
\]

Under

\[
g\mapsto c^2g,
\]

proper time scales as

\[
\tau_g\mapsto c\tau_g.
\tag{19}
\]

Holding \(M_*\) fixed changes \(q_*\). Thus a fixed matter standard breaks the
metric-only scale gauge.

### Conditional positive

> A stable physical matter scale conditionally calibrates observer-accessible
> metric intervals in units of that scale.

This is precisely what `HC-DU-112` required mathematically.

## 8. Common-unit gauge

Now transform both geometry and matter:

\[
g\mapsto c^2g,
\qquad
M_i\mapsto M_i/c.
\tag{20}
\]

Then

\[
M_i\tau_g
\mapsto
\frac{M_i}{c}\,c\tau_g
=
M_i\tau_g.
\tag{21}
\]

Every mark of the form in equation (17) remains unchanged. So do all mass
ratios and other dimensionless matter--geometry observables.

### Interpretation

Inside the declared matter--metric observable class, the transformation in
equation (20) is a common change of unit. In a larger contract, every admitted
dimensionful parameter must transform according to its physical dimension.
No observer can distinguish the full common transformation because no
dimensionless quantity changes.

This is not permission to rescale QCD and the metric while silently holding
another admitted sector fixed. If Newton's constant, a cosmological scale, an
electroweak scale, a regulator scale, or any other dimensionful parameter
remains fixed, a dimensionless inter-sector ratio changes. That is a physical
rival, not a common-unit gauge.

Therefore:

> The surviving global scale orbit should be quotiented as representation
> gauge, not reported as a physical remainder.

This changes the burden inherited from `HC-DU-112`. Dynamic Unity does not
need a metaphysically absolute metre. It needs the complete
observer-accessible dimensionless relation between records, matter, and
geometry.

### What “why this scale?” means physically

The statement

> Why is \(\Lambda_{\mathrm{QCD}}\) approximately some number of MeV?

is incomplete because the MeV is itself a chosen unit. A physical origin
question instead asks for a dimensionless ratio such as

\[
\frac{\Lambda_{\mathrm{QCD}}}{M_{\mathrm{Planck}}},
\qquad
\frac{\Lambda_{\mathrm{QCD}}}{v_{\mathrm{EW}}},
\tag{22}
\]

or a relation among other independently specified sectors.

Predicting one of those ratios would be a deeper unification result. It is
not required merely to use QCD matter as a local geometric standard.

## 9. Local scale remains observable

Let two regions acquire unequal conformal factors

\[
c_1\ne c_2.
\]

Against one transported fixed matter standard \(M_*\), the marks become

\[
q_i'
=
\exp[-M_*c_i\tau_i].
\tag{23}
\]

One global unit change \(M_*\mapsto M_*/c\) can cancel both only when

\[
c_1=c_2=c.
\]

Otherwise exact cancellation requires region-dependent matter scales

\[
M_*^{(i)}
=
\frac{M_*}{c_i},
\tag{24}
\]

which changes the matter-law contract.

### Discriminator

> A common transported matter standard turns nonuniform conformal scale into a
> dimensionless, observer-accessible difference.

This is the substantive geometry target. It is not erased by the global
common-unit quotient.

## 10. Real QCD versus the one-scale control

The pure one-scale equation is a clean control, not the full Standard Model.

Real QCD also contains:

- quark masses;
- flavor thresholds;
- electroweakly generated mass inputs;
- scheme and matching contracts;
- finite-volume and regulator control in lattice realizations; and
- prepared detectors and matter states in actual measurements.

Accordingly:

- QCD's physical spectrum is real and strongly confirmed;
- its dimensionless ratios are legitimate calibration structure;
- a continuum four-dimensional Yang--Mills mass gap is not proved here;
- the beta function does not predict every QCD parameter;
- no unique particle species is forced as the preferred clock; and
- choosing one stable standard can be conventional without making its
  physical behavior subjective.

Multiple standards are acceptable when their conversion ratios are stable and
path independent within the declared accuracy and resource contract.

## 11. Record-formation boundary

A physical mass scale is not yet a certified record. The full ladder is:

```text
QCD or matter scale exists
  != one system is prepared in a scale-sensitive process
  != a phase, decay, transition, or correlation is physically formed
  != that result is retained with occurrence provenance
  != an observer has bounded access to it
  != the mark excludes a declared metric rival
  != regional standards reconcile without local refit
  != the reconstructed interval enables a matched-resource action
```

A successful physical packet must freeze:

- the particle, transition, or correlation used;
- preparation and readout;
- its relation to proper time;
- environmental shifts and systematic errors;
- transport or comparison channels;
- event identity and provenance;
- retention and acquisition;
- the observer's access operations;
- the common-unit quotient;
- the local metric rival class; and
- a held-out interval or geometry target.

QCD supplies a candidate physical scale carrier. It does not automatically
supply this record instrument.

## 12. Relation to the North Star

Before this swing, the geometry chain appeared to require:

```text
explain or select absolute scale
  -> then calibrate metric geometry
```

The corrected chain is:

```text
fix one physical matter standard before the held-out target
  -> form and access a scale-sensitive mark
  -> reconstruct metric intervals in matter units
  -> quotient one common global unit conversion
  -> test nonuniform/local geometry without refit
```

The ultimate origin of inter-sector dimensionless ratios remains a profound
unification question. It is no longer a prerequisite for the Dynamic Unity
record-reconstruction theorem.

This is real progress because it converts an apparently metaphysical missing
absolute scale into a finite operational interface problem.

## 13. Strongest absorber and distinctive synthesis

### Absorbed components

- asymptotic freedom;
- dimensional transmutation;
- RG integration constants;
- renormalization-scheme dependence;
- physical hadron masses and mass ratios;
- lattice scale setting;
- rods, clocks, and spectroscopy; and
- common-unit covariance.

### Dynamic Unity-owned synthesis

The distinctive result is the typed composition:

1. `HC-DU-112`'s unmarked causal network is scale blind.
2. QCD supplies physically instantiated scale-bearing matter.
3. The beta law selects relative running but not the scale integration
   constant.
4. One fixed realized matter mark nevertheless closes operational metric
   scale.
5. Joint global rescaling of the metric and every admitted dimensional scale
   is declared gauge.
6. Nonuniform local scale remains a physical target.
7. Formation, provenance, access, and no-refit transfer—not ultimate unit
   origin—are now the live dependencies.

This is a program-level boundary and dependency correction, not new QCD.

## 14. Claim grading

| Claim | Verdict | Grade |
|---|---|---:|
| One-loop asymptotic freedom yields equations (2)--(3) | standard and reproduced | absorber |
| Beta law leaves one scale integration constant free | proved in the controlled class | 4 |
| Dimensional transmutation exchanges rather than eliminates the parameter | proved in the controlled class | 4 |
| Scheme changes rescale \(\Lambda\) while physical masses/ratios remain invariant | standard and controlled | 4 boundary |
| Lattice results require one dimensional input for physical units | source-grounded and algebraically controlled | 4 boundary |
| Fixed matter mark reconstructs selected proper-time intervals | proved conditionally | 3 |
| Joint rescaling of the metric and every admitted dimensional scale is common-unit gauge | proved for the declared observable class | 4 |
| Unequal local conformal factors survive one global unit quotient | proved conditionally | 4 |
| QCD selects a unique absolute scale from no boundary data | false in the controlled class | 0 |
| A QCD-derived certified record interface is physically selected | not established | 0 |
| New empirical excess over standard physics | not established | 0 |

Maximum earned grade:

> Scoped Grade 4 for RG scale provenance, parameter retention, and the
> common-unit/local-physical-scale distinction; conditional Grade 3 for metric
> reconstruction from a fixed matter mark.

No Grade-5 remainder or new prediction is earned.

## 15. Falsifiers and reopeners

The scoped result is falsified by:

- a unique \(\Lambda\) derived from equation (1) without a boundary value or
  equivalent scale input;
- a consistent scheme change altering a physical observable;
- absolute lattice spacing emerging without one dimensionful match;
- a fixed matter mark failing to change under same-units local metric
  rescaling; or
- one global unit conversion absorbing unequal local rescalings.

The constructive branch reopens with:

> One predeclared physically formed matter-scale mark—preferably a
> spectroscopic, correlation, or clock process—with retained provenance,
> bounded systematics, complete acquisition, observer access, cross-region
> transport/comparison, common-unit quotient, and unchanged transfer to a
> held-out metric interval.

No scientific successor is selected by this run. Candidate selection still
requires comparison against the full portfolio.

## 16. Practical disposition

Do not:

- search for an absolute metre inside unmarked causal-set statistics;
- require a theory of the ultimate origin of all scale before continuing;
- call \(\Lambda_{\overline{\mathrm{MS}}}\) a scheme-independent record;
- call a common unit conversion a physical metric ambiguity;
- locally refit the matter standard to absorb regional geometry;
- run lattice QCD merely to reproduce the primary-source result; or
- promote standard matter metrology to new physics.

Do:

- reconstruct dimensionless matter--geometry relations;
- declare one global common-unit quotient acting on every admitted
  dimensionful parameter;
- preserve inter-sector scale ratios as genuine deeper theory targets;
- identify a physically formable and transportable scale-sensitive process;
- freeze it before the held-out geometry; and
- test local/regional metric variation against that unchanged standard.

The repository returns to explicit quiescence.

## 17. Executable preservation

`tests/du_qcd_dimensional_transmutation_scale_gate_probe.py` preserves:

- one-loop RG flow and invariant-\(\Lambda\) reconstruction;
- the free integration-constant family;
- reference-coupling/\(\Lambda\) equivalence;
- common energy-unit covariance;
- one-loop scheme rescaling;
- invariant physical masses and mass ratios;
- lattice scale matching from one measured mass;
- fixed-matter-mark interval reconstruction;
- full common-unit covariance plus the held-fixed-sector control; and
- the unequal-local-scale discriminator.

The deterministic receipt is
`tests/artifacts/du_qcd_dimensional_transmutation_scale_gate_result.json`.

Passing earns no QCD mass-gap proof, selected Standard-Model parameter,
physical clock, formed record, provenance, access, metric reconstruction in
nature, new physics, prediction, or evidence grade.
