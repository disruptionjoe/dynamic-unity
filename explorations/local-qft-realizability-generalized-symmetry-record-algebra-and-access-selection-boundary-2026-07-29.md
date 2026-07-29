---
title: "Local-QFT realizability, generalized-symmetry record algebra, and access-selection boundary"
status: completed_scoped_result
doc_type: physical_filter_nonselection_theorem_and_finite_counterexample
created: 2026-07-29
hypothesis_id: HC-DU-118
run_id: RUN-20260729-110224-local-qft-record-algebra-selection
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 realizability-versus-selection and algebra-access boundary with conditional Grade 3 finite target-reconstruction result; no universal QFT theorem, selected physical instrument, record-formation law, empirical excess, ontology priority, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: 2c20f5b06213
probe: "../tests/du_local_qft_record_algebra_selection_probe.py"
artifact: "../tests/artifacts/du_local_qft_record_algebra_selection_result.json"
---

# Local-QFT realizability and record-algebra selection

## Executive result

The swing returned:

```text
LOCAL_QFT_REALIZABILITY_CONSTRAINS_BUT_DOES_NOT_SELECT_AN_INSTRUMENT
+ PROBE_COUPLING_STATE_READOUT_REGION_AND_ACCESS_REMAIN_SUPPLIED
+ CAUSALITY_AND_REALIZABILITY_ARE_DISTINCT_FILTERS
+ PROPER_LOCAL_RECORDS_CAN_AGREE_WHILE_AN_EXTENDED_TARGET_DIFFERS
+ GENERALIZED_SYMMETRY_NET_COMPLETION_CAN_CARRY_NONLOCAL_TARGETS
+ EXTENDED_TARGET_IS_OBSERVER_ACCESSIBLE_ONLY_UNDER_A_FROZEN_REALIZABLE_ACTION
+ ADDING_THE_EXTENDED_OPERATOR_CAN_BE_ACCESS_RETYPE_NOT_RECORD_REFINEMENT
+ CONDITIONAL_EXPECTATION_IS_CANONICAL_ONLY_RELATIVE_TO_A_SUPPLIED_GROUP_ACTION
+ RELATIVE_ENTROPY_QUANTIFIES_FIXED_NET_LOSS_BUT_DOES_NOT_SELECT_THE_NET
+ REALIZABILITY_FILTER_NOT_RECORD_INTERFACE_SELECTOR
+ NO_READY_SUCCESSOR
```

The result is not that local QFT lacks a measurement theory. The opposite is
now important. Fewster--Verch measurement schemes give a serious local,
covariant, composable framework for inducing system observables from physical
probe couplings. Recent work identifies substantial classes of realizable
measurements and proves that causality and realizability are distinct.

The result is the narrower selection boundary:

> A physical theory of which local instruments are realizable does not, by
> that fact alone, select which instrument actually forms the observer's
> record.

The system theory, probe theory, probe preparation, coupling region,
scattering morphism, probe observable or POVM, readout boundary, and observer
action remain inputs to the measurement scheme. The scheme then calculates an
induced observable and instrument.

Generalized-symmetry AQFT supplies a second genuine structure. A theory may
admit an additive algebra generated locally and a larger algebra containing
nonlocally generated operators. Relative entropy can quantify the information
lost by the conditional expectation from the larger algebra to the additive
one. But that inclusion still does not decide which algebra is physically
available to a given observer.

The combined lesson is constructive:

> Dynamic Unity should search for a **physically selected measurement
> scheme**, not merely a physically realizable operation or a mathematically
> natural algebra inclusion.

The distinction matters because the most interesting "remainder" can sit
exactly in the gap between an additive local algebra and an extended algebra.
That is a real algebraic remainder. It becomes an observer-accessible physical
remainder only after the extended operation is independently shown to be
available under the frozen action and acquisition contract.

## 1. What local-QFT measurement theory actually selects

[Fewster and Verch](https://arxiv.org/abs/1810.06512) model a measurement by
coupling a system QFT to a probe QFT in a bounded spacetime region. A supplied
initial probe state and the scattering map determine a completely positive
map from probe observables to induced system observables. The induced
observables localize in the causal hull of the coupling region. Causally
ordered schemes compose consistently when the scattering map obeys causal
factorization.

This earns several important pieces:

- the operation has a relativistically meaningful localization;
- system and probe are treated dynamically rather than by an instantaneous
  collapse rule;
- the induced system observable is calculated from a declared physical
  scheme;
- post-selected and nonselective state updates form a Davies--Lewis
  instrument; and
- causally disjoint schemes compose without an arbitrary ordering choice.

It does not select the scheme's inputs. The induced observable has the typed
form

\[
\varepsilon_{\sigma,\Theta}(B),
\tag{1}
\]

where \(B\) is the measured probe observable, \(\sigma\) the probe
preparation, and \(\Theta\) the scattering morphism determined by the chosen
system--probe coupling. The localization region is also declared through the
coupling support and the probe readout.

[Mandrysch and Navascués](https://arxiv.org/abs/2411.13605) strengthen the
positive side. Gaussian-modulated measurements of locally smeared fields are
Fewster--Verch-realizable and admit a movable Fewster--Verch Heisenberg cut.
This is useful to Dynamic Unity because it prevents an easy dismissal:
physical probe chains need not stop at one magically measured probe.

But the theorem remains a **realizability result**. To represent an instrument
one still supplies a probe theory, probe state, scattering morphism, and probe
POVM. Moving the cut proves consistency of a class of schemes, not a unique
law selecting one member of the class.

The 2026 result of
[Mandrysch, Simmons, and Navascués](https://arxiv.org/abs/2607.12976)
sharpens the boundary further in the free scalar field:

- some causal channels cannot be approximated arbitrarily well by
  Fewster--Verch schemes;
- a wide class of random-displacement instruments is
  Fewster--Verch-realizable;
- those instruments can implement arbitrary POVMs over declared field
  quadratures nondestructively with respect to commuting quadratures; and
- deciding whether a general instrument is implementable, or far from
  implementable, by compositions of Fewster--Verch operations is
  uncomputable.

This proves that the following ladder must not be collapsed:

```text
formal channel
  -> causal channel
  -> physically realizable channel
  -> actually instantiated scheme
  -> formed and retained output
  -> observer-accessible certified record
```

The first three rungs are already nontrivial and distinct. The last three do
not follow from them.

The uncomputability result also changes Dynamic Unity's method:

> A general-purpose algorithm that decides physical QFT realizability cannot
> be a prerequisite for the record program. A positive path needs an explicit
> constructive realization or a proved sufficient class; a negative path
> needs a scoped obstruction.

## 2. What generalized-symmetry nets actually add

[Casini, Huerta, Magán, and Pontello](https://arxiv.org/abs/2008.11748)
analyze additivity and Haag duality for operator nets. In regions with
nontrivial topology, nonlocally generated operators may extend the additive
algebra. Their existence is associated with generalized symmetries, and the
same underlying theory can admit more than one algebra choice for the region.

Schematically, let

\[
\mathcal A_{\rm add}(R)
\subsetneq
\mathcal A_{\rm max}(R).
\tag{2}
\]

The smaller algebra is generated additively by appropriate local subregions.
The larger algebra also contains extended operators such as suitable Wilson,
't Hooft, twist, or intertwining operators.

Given a declared conditional expectation

\[
E:
\mathcal A_{\rm max}(R)
\longrightarrow
\mathcal A_{\rm add}(R),
\tag{3}
\]

the relative entropy

\[
S_{\mathcal A_{\rm max}}
\bigl(\omega\Vert \omega\circ E\bigr)
\tag{4}
\]

is an entropic order parameter for the information carried by the nonlocal
operators and erased by the restriction.

This is much stronger than saying "there might be hidden global
information." It provides:

- a mathematically typed algebra inclusion;
- physical operator families associated with the gap;
- a conditional expectation erasing the nonlocal sector;
- a type-III-compatible relative-entropy diagnostic; and
- dual certainty relations for complementary order/disorder structures.

It still leaves one observer question open:

> Which algebra can this observer physically act on and acquire?

The theory may physically structure both
\(\mathcal A_{\rm add}\) and \(\mathcal A_{\rm max}\). That does not make them
interchangeable record interfaces. A local observer limited to operations in
\(\mathcal A_{\rm add}\) cannot be credited with a target in
\(\mathcal A_{\rm max}\) merely because that target exists in the theory.
Conversely, an observer with a realized extended measurement should not be
artificially restricted to the additive algebra.

This is the exact role of Dynamic Unity's observer/action index.

## 3. Typed supplied-versus-derived audit

| Object | Status in the local-QFT scheme | Dynamic Unity consequence |
|---|---|---|
| System QFT/net | Supplied as the theory being probed | Does not emerge from the measurement scheme |
| Probe QFT | Supplied | Candidate physical carrier, not selected carrier |
| Probe preparation \(\sigma\) | Supplied | Changes the induced observable/channel |
| Coupling region | Supplied | Fixes localization and causal hull |
| Interaction/scattering morphism \(\Theta\) | Supplied or derived from a supplied interaction | Changes the induced observable/channel |
| Probe observable/POVM \(B\) | Supplied | Fixes what is read |
| Induced system observable \(\varepsilon_{\sigma,\Theta}(B)\) | Derived | A real calculable output of the scheme |
| Davies--Lewis instrument | Derived from the scheme | Physical update model conditional on the inputs |
| Causality | Property that may be proved | Necessary filter, not sufficient realizability |
| Fewster--Verch realizability | Property or constructive witness | Physical filter, not unique selection |
| Output formation/retention | Not selected by the abstract scheme alone | Needs a physical apparatus/archive theorem |
| Observer acquisition/access | Not selected | Must be frozen independently |
| Additive algebra | Derived relative to the net and region class | One candidate operational algebra |
| Maximal/extended algebra | Derived relative to the net and topology | Carries possible nonlocal target distinctions |
| Conditional expectation \(E\) | Canonical relative to a fixed inclusion/group action in scoped cases | Does not select the inclusion or observer action |
| Relative-entropy loss | Derived after the inclusion, state, and expectation are fixed | Quantifier, not selector |

## 4. Exact finite instrument-nonselection control

Take one system bit \(s\), one probe bit \(p\), and initialize \(p=0\). All
three maps below are reversible maps on the same four-state arena:

\[
\begin{aligned}
U_0(s,p)&=(s,p),\\
U_1(s,p)&=(s,p\oplus s),\\
U_2(s,p)&=(s,p\oplus s\oplus1).
\end{aligned}
\tag{5}
\]

Read the probe after the interaction. The induced record channels are:

\[
\begin{array}{c|cc}
&s=0&s=1\\\hline
R_0&0&0\\
R_1&0&1\\
R_2&1&0
\end{array}
\tag{6}
\]

All three interactions are admissible under the frozen finite condition
"reversible system--probe coupling." They yield three distinct record
quotients.

This proves the finite selection boundary:

> A physical admissibility or realizability class containing more than one
> scheme does not select one induced record channel.

The control is not a QFT theorem. Its transfer burden is discharged by the
primary literature's explicit dependence on probe, state, coupling, and
readout and by the existence of broad realizable instrument classes. It is a
minimal logical witness, not a model of a quantum field.

## 5. Exact additive-local versus extended-target control

Let \(x=(x_1,x_2,x_3)\in\{0,1\}^3\), and define

\[
\chi(x)=(-1)^{x_1+x_2+x_3}.
\tag{7}
\]

Consider the full-support pair

\[
P_\pm(x)
=
\frac{1\pm\frac12\chi(x)}{8}.
\tag{8}
\]

For \(P_+\), every even-parity outcome has probability \(3/16\) and every
odd-parity outcome \(1/16\). \(P_-\) reverses those probabilities.

Marginalizing any nonempty proper subset \(S\subsetneq\{1,2,3\}\) sums over at
least one unconstrained bit. The character cancels:

\[
\sum_{x_j\in\{0,1\}}(-1)^{x_1+x_2+x_3}=0.
\tag{9}
\]

Therefore

\[
(P_+)_S=(P_-)_S
\tag{10}
\]

for every one-site and two-site restriction. Every such marginal is uniform.
No statistic in any one proper-subset algebra distinguishes the states.

The extended parity observable does:

\[
\mathbb E_{P_+}[\chi]=+\frac12,
\qquad
\mathbb E_{P_-}[\chi]=-\frac12.
\tag{11}
\]

As a deterministic target on individual histories, parity also fails to
factor through every proper-subset record. It factors through the full
three-site record.

The full Kullback--Leibler signature is exact:

\[
\begin{aligned}
D(P_+\Vert P_-)
&=
\frac34\log 3+\frac14\log(1/3)\\
&=
\frac12\log3.
\end{aligned}
\tag{12}
\]

Every proper-local restriction has divergence zero.

This earns a finite target-reconstruction theorem:

> An extended target may fail to factor through every proper-local record
> even when the admitted distributions have full support and every proper
> marginal agrees.

It does not earn the physical claim that the extended target is accessible.
There are two different contracts:

1. **proper-local observer:** the action algebra contains only a declared
   proper-local algebra; the parity difference is not an accessible target;
2. **extended observer:** a realizable operation measures the global parity;
   the parity difference is accessible.

Moving from the first to the second is an **action/access retype** unless the
extended operation was already part of the frozen observer contract. It is
not ordinary record refinement within an unchanged acquisition process.

## 6. Conditional expectation is relative, not absolute

On \(\{0,1\}^2\), let one \(\mathbb Z_2\) action flip the first bit:

\[
g_1(x_1,x_2)=(x_1\oplus1,x_2),
\tag{13}
\]

and another flip both:

\[
g_2(x_1,x_2)=(x_1\oplus1,x_2\oplus1).
\tag{14}
\]

For a function \(f\), each group average

\[
E_i f(x)=\frac{f(x)+f(g_i x)}2
\tag{15}
\]

is positive, unital, invariant under its declared action, and idempotent.
Each is the canonical expectation onto its own fixed algebra.

For \(f=\mathbf1_{\{(0,0)\}}\),

\[
E_1f
=
\frac12\mathbf1_{\{(0,0),(1,0)\}},
\tag{16}
\]

while

\[
E_2f
=
\frac12\mathbf1_{\{(0,0),(1,1)\}}.
\tag{17}
\]

The expectations and fixed algebras differ. Thus:

> "Take the invariant subalgebra" is not an absolute selection rule. It
> becomes canonical only after the physical group action is fixed.

The same guard applies to relative-entropy order parameters. Equation (4)
quantifies loss under a chosen expectation; it does not choose the group,
action, algebra inclusion, reference state, or observer access.

## 7. Formal result at the earned grade

### Proposition 1 — realizability does not imply selection

Let \(\mathfrak I\) be a physically admitted class of instruments and let
\(R:\mathfrak I\to\mathfrak C\) assign each instrument its induced record
channel. If there exist \(I_1,I_2\in\mathfrak I\) with
\(R(I_1)\ne R(I_2)\), admission of \(\mathfrak I\) does not define a unique
record channel.

The proof is immediate from nonconstancy of \(R\). The scientific work is
therefore not this abstract proposition; it is showing that the physical
theory admits the multiple schemes and does not supply an independent
selector. Fewster--Verch provides the typed map, and the finite control
provides the smallest witness.

### Proposition 2 — local-algebra target obstruction

For the family (8), every proper-subset record channel \(r_S\) satisfies

\[
(r_S)_*P_+=(r_S)_*P_-,
\tag{18}
\]

while the extended parity target has different distributions and fails
deterministic factorization through \(r_S\). Hence no inference or operation
whose complete input is \(r_S\) can reconstruct the parity target.

### Proposition 3 — observer-access qualification

Proposition 2 establishes an algebra-relative target remainder. It
establishes an observer-accessible physical remainder only if:

1. the two completions belong to the independently admitted physical class;
2. the local record is physically formed and completely acquired;
3. the extended target is a physically realizable action or consequence for
   the same observer;
4. access to that target was frozen before seeing the rival completions; and
5. adding the target does not change the occurrence, apparatus, boundary, or
   resource contract being held fixed.

Absent item 3 or 4, the result is a difference in a larger theory algebra, not
a capability available to the observer under study.

## 8. What changed for Dynamic Unity

### A. The interface problem is narrower

Dynamic Unity should no longer say only that QFT "does not supply a record
interface." Local QFT supplies serious physical **measurement-scheme
machinery** and nontrivial realizability filters. The remaining question is:

> What selects and instantiates one scheme, forms its output, and makes it
> accessible to the declared observer?

That is sharper than the old generic gap.

### B. Physical realizability is a valuable filter

A proposed Dynamic Unity record channel should not be credited merely because
it is causal as an abstract channel. When the arena is QFT, it should carry:

- an explicit Fewster--Verch realization;
- membership in a proved realizable sufficient class; or
- a scoped alternative local-QFT measurement construction.

The 2026 uncomputability result means the program should not wait for or claim
a universal implementability decider.

### C. Generalized symmetries provide genuine remainder specimens

Nonmaximal nets are not metaphors. They supply physical theories in which an
extended operator algebra contains distinctions erased by an additive local
algebra. These are excellent hostile specimens for Dynamic Unity's
completion-fibre and access-indexed reconstruction machinery.

But they do not automatically solve interface selection:

- topology and theory may select an inclusion of algebras;
- a symmetry may select a conditional expectation relative to that
  inclusion;
- relative entropy may quantify the lost sector;
- none of those facts alone says a local observer can measure the extended
  operator.

### D. Relative entropy now has a precise place

`HC-DU-117` admitted relative entropy as a diagnostic after a channel is
fixed. `HC-DU-118` supplies the most promising physical setting so far:

\[
\mathcal A_{\rm max}
\xrightarrow{E}
\mathcal A_{\rm add}.
\tag{19}
\]

Here relative-entropy loss is not generic "capacity." It is a physically
motivated measure of what the declared additive algebra forgets about the
extended sector.

This still does not select \(E\), \(\mathcal A_{\rm max}\), or the observer's
action algebra.

## 9. Successor disposition

The swing does not select a new flagship.

It strengthens one existing candidate class:

```text
physically-selected-observable-carrier-algebra
  + constructively realizable measurement scheme
  + physically formed retained output
  + frozen observer action/access algebra
  + access-preserving target factorization
```

A ready successor would need one concrete packet satisfying at least one of
the following reopeners.

### Reopener A — selected local-QFT instrument

Provide a physical law, symmetry, boundary, or source mechanism that selects
one probe theory, state, coupling, and readout from the realizable class,
forms a retained output, and transfers unchanged to a held-out target.

### Reopener B — generalized-symmetry access theorem

Fix one QFT, region topology, additive/maximal inclusion, physical
conditional expectation, and observer operation class. Construct an explicit
realizable measurement of the extended sector and prove a target consequence
that does not factor through the additive record.

### Reopener C — nonselection theorem

In one fixed physical QFT, prove that a surviving physical automorphism or
scheme degeneracy acts transitively on candidate record interfaces and admits
no invariant selector, while at least two candidates have incompatible
held-out target consequences.

Until one of these packets exists, further finite variants would restate the
same boundary.

## 10. Grade and limits

Earned:

- scoped Grade-4 distinction among causality, realizability, scheme
  instantiation, record formation, and access;
- scoped Grade-4 algebra-relative versus observer-accessible remainder
  boundary;
- exact finite proper-local/nonlocal target counterexample;
- exact finite relative-entropy-loss calculation;
- exact finite conditional-expectation dependence control; and
- conditional Grade-3 finite target reconstruction when the extended action
  is admitted.

Not earned:

- a universal QFT nonselection theorem;
- a physically selected QFT instrument;
- formation, retention, provenance, or complete acquisition;
- a theorem that every generalized-symmetry operator is an observer record;
- a capacity law;
- a new generalized-symmetry or relative-entropy result;
- empirical excess over QFT;
- ontology priority;
- a law of nature, new physics, or prediction; or
- a ready flagship successor.

## Bottom line

Local QFT has moved the program closer to the North Star, but not by handing
it a record selector. It supplies the first credible **physical
realizability filter** for candidate record channels.

Generalized symmetries supply a credible place where the choice of operational
algebra changes what can be reconstructed. Relative entropy quantifies that
change exactly.

The missing piece is now explicit:

> Which physically realizable operation is actually instantiated, and which
> algebra is genuinely available to this observer?

That is the next positive theorem a concrete physical packet must answer.
