---
title: "Relative-entropy record sufficiency and GU index/direct-action descent admission boundary"
status: completed_scoped_result
doc_type: absorption_theorem_counterexample_and_typed_admission_gate
created: 2026-07-29
hypothesis_id: HC-DU-117
run_id: RUN-20260729-104522-relative-entropy-index-descent-admission
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 absorption, sufficiency, and typed non-admission result; no GU theorem, physical interface selection, capacity law, empirical excess, ontology priority, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: 24f4b1b2c3f3b9abab63ddd3bdfa0a493021f47b
  gu_formalization: 2d8ec46cb7997580519c2d2e1747b9199459f82b
probe: "../tests/du_relative_entropy_index_descent_admission_probe.py"
artifact: "../tests/artifacts/du_relative_entropy_index_descent_admission_result.json"
---

# Relative-entropy record sufficiency and GU index/direct-action descent

## Executive result

The swing returned:

```text
ARAKI_RELATIVE_ENTROPY_AND_PETZ_SUFFICIENCY_ABSORB_THE_CORE
+ RELATIVE_ENTROPY_LOSS_IS_A_TYPED_INFORMATION_LOSS_NOT_CAPACITY_BY_ITSELF
+ TARGET_RECONSTRUCTION_IS_STRICTLY_WEAKER_THAN_FULL_STATISTICAL_SUFFICIENCY
+ PHYSICAL_RECORD_USE_REQUIRES_SELECTED_ALGEBRA_CHANNEL_STATE_FAMILY_REFERENCE_ACCESS_ACTION_AND_RESOURCES
+ GU_GENERATION_OBJECT_HAS_AN_UNRESOLVED_INTEGER_INDEX_VERSUS_THREE_PRIMARY_TORSION_FORK
+ GU_SOURCE_ACTION_AND_TORSION_TO_INTEGER_BRIDGE_REMAIN_UNBUILT
+ FULL_GU_FIELD_TO_DIRECT_ACTION_DESCENT_IS_NOT_YET_WELL_POSED
+ POSITIVE_SOURCE_KERNEL_CAN_ERASE_DETERMINANT_ORIENTATION
+ COMPLETE_EFFECTIVE_ACTION_IS_REQUIRED_BEFORE CLAIMING INDEX_OR_ANOMALY_DESCENT
+ REUSABLE_TOOL_ONLY
+ NO_READY_SUCCESSOR
```

The outside council identified a useful junction but overstated both of its
candidate objects.

First, relative entropy is indeed the correct divergence when ordinary
density-matrix entropy is unavailable or ill behaved for local type-III
algebras. But this is mature operator-algebra and quantum-information
mathematics. It does not, by itself, define a record, select an observer
boundary, measure capacity, or establish a physical remainder.

Second, there is a high-ceiling question about whether field-theoretic
topological or chiral information survives exact elimination into a
source-only/direct-action description. But GU does not currently possess the
single settled “generation index” presupposed by that question. Its own
current documents keep an explicit construction fork:

- standard integer/Fredholm indices; and
- a proposed program-native 3-primary torsion carrier.

The generation count remains `OPEN / located-not-forced`; the bridge from the
torsion carrier to integer three and GU's native source action remain
unbuilt. Consequently, no full GU descent theorem can yet be stated without
inventing its domain, invariant, or translation.

The two candidates therefore do not replace Dynamic Unity's current
quiescence:

- relative entropy is admitted as a **reusable diagnostic** inside a
  physically typed record contract; and
- GU/direct-action descent remains a **conditional high-ceiling reopener**
  requiring a source-owned packet.

## 1. Relative entropy: what is established

[Araki](https://doi.org/10.2977/prims/1195191148) defined relative entropy
for normal states of a general von Neumann algebra through the relative
modular operator and proved positivity, lower semicontinuity, convexity, and
monotonicity. No trace-class density matrix for the local algebra is required.

[Petz](https://doi.org/10.1007/BF01212345)
then characterized sufficient subalgebras by equality of relative entropy
under restriction. In modern channel language, data processing gives

\[
D_{\mathcal M}(\rho\Vert\sigma)
\ge
D_{\mathcal N}(R_*\rho\Vert R_*\sigma),
\tag{1}
\]

where \(R_*\) is a fixed normal record channel from states on
\(\mathcal M\) to states on \(\mathcal N\). Equality for an admitted state
family, under the required support and normality conditions, is the
recoverability/sufficiency case.

This operator-algebraic machinery is already used in QFT. For example:

- [Casini](https://arxiv.org/abs/0804.2182) formulates the flat-space
  Bekenstein bound as positivity of relative entropy between a vacuum and an
  excited state restricted to a region; and
- [Jakšić and Pillet](https://arxiv.org/abs/1406.0034) prove a scoped
  Landauer result for a finite system coupled to an infinite thermal
  reservoir using Araki's KMS perturbation theory.

Those are strong absorbers. They show that “use relative entropy because the
local algebra is type III” is correct, but not novel to Dynamic Unity.

GU's own `W105` audit independently reaches the compatible statement that
Araki relative entropy consumes the relative modular operator
\(\log\Delta_{\rm rel}\), not modular conjugation \(J\). That is useful
cross-checking, not a new capacity law.

## 2. The reusable Dynamic Unity object

For a **fixed** algebra, state family, reference state, and record channel,
define the record divergence loss

\[
L_R(\rho,\sigma)
=
D_{\mathcal M}(\rho\Vert\sigma)
-
D_{\mathcal N}(R_*\rho\Vert R_*\sigma)
\ge 0.
\tag{2}
\]

This has one clean interpretation:

> \(L_R\) is the distinguishability lost when the declared state pair is
> passed through the declared record channel.

If \(L_R=0\) for every pair in the admitted family and one common recovery
channel reconstructs that family, the record is statistically sufficient for
the family. If \(L_R>0\), the record loses at least some discrimination in
that family.

That is all (2) says without more structure. It does not tell us:

- whether \(\mathcal M\) is the physically relevant algebra;
- whether \(R_*\) was dynamically selected or chosen by the analyst;
- whether an output was physically formed, retained, accessed, or certified;
- whether the state family is the physically admitted completion class;
- whether \(\sigma\) is a selected physical reference;
- whether the lost distinction affects any observer action;
- what code, error, repetition, deadline, energy, memory, or access contract
  defines a channel capacity; or
- whether the lost distinction changes a held-out target.

Calling (2) “capacity” would therefore collapse a divergence into an
operational optimization problem. Calling it “remainder” would collapse
full-family information loss into a target-relative physical difference.

## 3. Exact sufficient-record control

The executable regression uses two states with record marginals

\[
P_R=(2/3,1/3),
\qquad
Q_R=(1/3,2/3),
\tag{3}
\]

and one common hidden conditional

\[
K(h\mid r=0)=(3/4,1/4),
\qquad
K(h\mid r=1)=(1/5,4/5).
\tag{4}
\]

Define

\[
P(r,h)=P_R(r)K(h\mid r),
\qquad
Q(r,h)=Q_R(r)K(h\mid r).
\tag{5}
\]

The likelihood ratio satisfies

\[
\frac{P(r,h)}{Q(r,h)}
=
\frac{P_R(r)}{Q_R(r)},
\tag{6}
\]

so it depends only on the record. Therefore

\[
D(P\Vert Q)
=
D(P_R\Vert Q_R),
\tag{7}
\]

and the same \(K\) exactly recovers both full states from their record
marginals.

The probe represents each divergence exactly as a rational linear
combination of formal logarithms, rather than comparing floating-point
values. Both sides of (7) have signature

\[
\frac23\log 2+\frac13\log(1/2).
\tag{8}
\]

This is the finite classical shadow of the Petz sufficiency condition.

## 4. Positive information loss does not decide target reconstruction

For

\[
P_H=(3/4,1/4),
\qquad
Q_H=(1/4,3/4),
\tag{9}
\]

and a constant record \(R(h)=\ast\),

\[
D(P_H\Vert Q_H)=\frac12\log 3,
\qquad
D(R_*P_H\Vert R_*Q_H)=0.
\tag{10}
\]

The record therefore loses positive distinguishability.

Now declare two targets on the same histories:

\[
T_{\rm constant}(0)=T_{\rm constant}(1),
\qquad
T_{\rm hidden}(0)\ne T_{\rm hidden}(1).
\tag{11}
\]

The constant record reconstructs \(T_{\rm constant}\) exactly and fails to
reconstruct \(T_{\rm hidden}\). The divergence loss is identical in both
questions.

This proves the strict type boundary:

> Full statistical sufficiency is stronger than reconstruction of one
> independently declared target. Positive relative-entropy loss is not, by
> itself, a target-relative physical remainder.

Dynamic Unity should use (2) when it needs a family-wide
distinguishability/recovery diagnostic. It should retain the simpler
factorization criterion for a declared target:

\[
r(m_1)=r(m_2)
\Longrightarrow
t(m_1)=t(m_2).
\tag{12}
\]

Neither criterion replaces the need to select and physically form \(r\).

## 5. Capacity and Landauer boundary

Relative entropy can enter capacity bounds, hypothesis-testing exponents, and
thermodynamic identities. It does not select those operational contracts.

A capacity statement still requires, at minimum:

```text
physical channel
+ allowed input/code family
+ number/composition of channel uses
+ encoder and decoder access
+ error or distortion criterion
+ resource budget
+ deadline or asymptotic regime
+ adversary/noise model where relevant
```

A Landauer statement still requires:

```text
system and reservoir
+ temperature/KMS state
+ actual transformation or erasure task
+ work/heat convention
+ coupling and switching protocol
+ initial and final state contract
```

Araki relative entropy makes such statements possible in operator-algebraic
settings. It does not turn an unspecified record algebra into an operational
capacity or physical erasure law.

## 6. Correction to the proposed GU descent premise

The claim “GU's generation count is an index of an operator on a bundle, so
direct action may erase it” is too flat.

GU's current construction-fork document says:

| construction | current GU status |
|---|---|
| standard integer index/rank in \(\mathbb Z\) | multiple scoped indices exist, but none currently forces the observed generation count |
| program-native proposed \(3\)-primary carrier in \(\mathbb Z/3\subset\pi_3^s\) | located, with no additive bridge to integer three because \(\mathrm{Hom}(\mathbb Z/3,\mathbb Z)=0\) |
| physical generation count | `OPEN / located-not-forced` |
| native GU source action | unbuilt |

Concrete integer indices in GU are not interchangeable with the physical
count:

- the pinned ghost-subtracted gravitino complex gives \(-42\);
- the geometric gamma-traceless Rarita--Schwinger operator on K3 gives
  \(-38\);
- external flux can realize arbitrary integer chiral index, which does not
  select three; and
- the quaternionic/Krein-native operator class has a scoped even-index wall,
  while the proposed odd-primary count carrier is a differently typed
  object.

The field/direct-action fork may still be profound. But the question must
first choose which object is meant.

## 7. Two distinct descent questions

### 7.1 Integer-index/anomaly descent

For a Dirac-type field operator \(D\), integrating out the field can retain
more than the positive source kernel. The quantum object can include

\[
\det D,
\quad
\arg\det D,
\quad
\eta(D),
\quad
\text{determinant-line holonomy},
\quad
\text{zero-mode and boundary data}.
\tag{13}
\]

[Fujikawa](https://doi.org/10.1103/PhysRevLett.42.1195) showed that the
fermionic path-integral measure acquires an anomaly phase under a chiral
transformation. [Dai and Freed](https://arxiv.org/abs/hep-th/9405012)
relate exponentiated eta invariants, determinant lines, gluing, and global
anomaly holonomy. These are direct warnings against the inference

> “the explicit field was eliminated, therefore its index or chiral
> information disappeared.”

A proper descent theorem must compare the complete quantum effective object,
not just a positive source-response kernel.

### 7.2 Three-primary torsion descent

If the candidate is GU's 3-primary torsion or equivariant rho class, a
determinant-sign test is not enough. One must define:

1. the exact source category and field-side class;
2. the source-only/direct-action target category;
3. the elimination or translation functor;
4. the equivalence relation and background family;
5. the natural image of the torsion/rho class;
6. the integer-valued physical readout, if any; and
7. the proof that the readout is selected rather than target assigned.

No such current packet was found in the read-only GU evidence.

## 8. Minimum typed descent packet

The descent question becomes executable only when all of the following exist:

```yaml
field_theory:
  action:
  fields_and_sources:
  operator_domain_and_boundary:
  state_or_sector:
  regulator_and_measure:
invariant:
  construction_fork: integer_index | determinant_line | eta | torsion | rho
  exact_object:
  codomain:
  physical_readout:
elimination:
  map_or_functor:
  admitted_background_family:
  gauge_and_equivalence:
  retained_determinant_measure_state_boundary_terms:
direct_action:
  source_only_object:
  allowed_interventions:
comparison:
  invariant_preservation_statement:
  held_out_target:
  cheapest_counterexample:
```

For GU specifically, the packet also needs its native source action and the
still-open carrier-selection/physicalization bridge. Without those, the
field/direct-action comparison is not merely hard; it lacks a fixed
proposition.

## 9. Exact orientation-loss control

The regression uses

\[
D_+
=
\begin{pmatrix}
1&0\\0&1
\end{pmatrix},
\qquad
D_-
=
\begin{pmatrix}
-1&0\\0&1
\end{pmatrix}.
\tag{14}
\]

They have the same positive kernel,

\[
D_+^{\mathsf T}D_+
=
D_-^{\mathsf T}D_-
=I,
\tag{15}
\]

but

\[
\det D_+=1,
\qquad
\det D_-=-1.
\tag{16}
\]

Therefore a quotient retaining only \(D^\mathsf TD\) cannot reconstruct the
orientation sign retained by the determinant.

This finite result is deliberately modest. It does not model a Fredholm
index, anomaly, determinant line, GU, or direct-action physics. It proves only
that a magnitude-only source quotient is too coarse for the proposed descent
question and that `HC-DU-116`'s complete-effective-action guard is
load-bearing.

## 10. Admission and roadmap verdict

### Relative entropy

Disposition:

```text
REUSABLE_TOOL_ONLY
```

Use it when a future physically selected algebra and record channel require a
family-wide sufficiency, recoverability, or distinguishability-loss measure,
especially in type-III settings. Do not open a standalone relative-entropy
campaign or rename it capacity.

### GU/direct-action descent

Disposition:

```text
HIGH_CEILING_BUT_NOT_EXECUTABLE
```

Reopen only when GU or another concrete field theory supplies the minimum
typed packet. For GU, the decisive prerequisites are:

1. select the integer-index or 3-primary construction fork;
2. provide the native source action;
3. identify the physical generation/chirality readout;
4. define a complete field-to-direct-action translation; and
5. preserve determinant/measure/state/boundary data or prove why the selected
   invariant lives elsewhere.

### Portfolio

Neither arm admits a scientific successor. Dynamic Unity remains explicitly
quiescent. This is not a loss of the high-ceiling question; it prevents an
ill-typed version from consuming another series of swings.

## 11. Plain-English meaning

Relative entropy tells us how much ability to tell states apart is lost by a
particular compression or record channel. That is a powerful audit tool. But
unless physics tells us which channel is the real record channel and which
task matters, the number is not “the capacity of reality” or “the missing
physical remainder.”

The direct-action question is similarly real but premature. Removing an
explicit field does not necessarily remove its topological information; the
information can move into the phase and global structure of the effective
action. Before testing GU, however, we must know which of GU's several
differently typed generation objects is supposed to be physical and have the
source action that performs the elimination. We do not yet have those.

The useful outcome is a sharper map:

> Relative entropy is ready as an instrument. GU index/direct-action descent
> is not ready as an experiment or theorem. The exact reopener is now known.
