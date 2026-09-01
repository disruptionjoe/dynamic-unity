---
title: "Anomaly-selected QFT subfamily, domain-relative uniqueness, and ruler boundary"
status: banked_scoped_noncopy_selection_calibration_and_domain_boundary
doc_type: exact_bounded_classification_selection_theorem_boundary_and_portfolio_disposition
created: 2026-08-31
claim_id: HC-DU-213
run_id: RUN-20260831-anomaly-selected-qft-subfamily-calibration
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The first non-copy QFT-selector calibration succeeds, but not as a new
physical successor.

```text
NONCOPY_QFT_CONSISTENCY_SELECTION_POSITIVE
ANOMALY_FREE_SUBFAMILY_PROPER
QFT_EXPRESSIBILITY_PRESERVED
BOUNDED_QUADRATIC_TARGET_SHARPENED
FINITE_DOMAIN_UNIQUENESS_NOT_PHYSICAL
CHARGE_NORMALIZATION_REQUIRES_COUPLING_RULER
RECORD_HANDOFF_UNSELECTED
NORTH_STAR_GATE_CALIBRATED
NO_READY_SUCCESSOR
```

For five left-handed Weyl fermions with primitive nonzero integer `U(1)`
charges, no vectorlike pair, and `|q_i|<=9`, quotienting permutations and
global charge conjugation leaves `8,129` physical candidate spectra. The
standard anomaly equations

\[
A_1=\sum_i q_i=0,
\qquad
A_3=\sum_i q_i^3=0
\]

select exactly one orbit:

\[
(-9,-5,-1,7,8).
\]

This is a genuine non-copy selection. No supplied bit names the survivor; two
target-blind quantum-consistency equations eliminate `8,128` alternatives.
The quadratic representation weight

\[
B_2=\sum_i q_i^2
\]

contracts from an incumbent image of `313` values to `{220}`. A secondary
quartic audit contracts from `1,075` values to `{13,684}`. Anomalous spectra
with `B_2=220` exist, so the held-out target does not encode the anomaly
answer.

The hostile controls are decisive:

- with `|q_i|<=8`, no five-field chiral solution exists;
- with `|q_i|<=10`, a second orbit `(-10,-4,-2,7,9)` appears and the selected
  `B_2` image becomes `{220,250}`;
- six fields admit a solution already at maximum charge five; and
- seven fields admit one already at maximum charge four.

Therefore the anomaly equations select a proper QFT subfamily, but they do
not select the fermion count, charge domain, gauge group, or normalization.
The apparent unique spectrum and target value are relative to a supplied
candidate domain.

There is a second ruler boundary. Under

\[
q_i\mapsto 2q_i,
\qquad
g\mapsto g/2,
\]

the bare `B_2` changes by four while the coupling-weighted response
`g^2 B_2` is unchanged. Primitive integer normalization chooses a convenient
representative; it is not by itself an absolute observable or a physically
selected coupling ruler.

The result adds a positive rung to the DU selection spine:

```text
supplied selector key                         [HC-DU-212 negative]
  != non-copy consistency constraint         [HC-DU-213 positive]
  != physically selected candidate domain    [still open]
  != unique physical QFT                      [still open]
  != locked empirical response with ruler    [still open]
  != selected material record handoff        [still open].
```

# 1. Why this is the right calibration

`HC-DU-211` established that a deeper construction need not escape QFT. It
may contribute by deriving a proper QFT subfamily. `HC-DU-212` then showed
that ordinary dynamics selecting a sector is insufficient when the deciding
coefficient is an isomorphic copy of the selected answer.

Those results left a possible defect in the gate: perhaps every finite
selector would be rejected as premise relocation. A useful admission rule
must distinguish a copied key from a real constraint.

Quantum anomalies provide the cleanest known positive control. Adler and
Bardeen established that quantum corrections can produce anomalous Ward
identities even when the classical formulation suggests the corresponding
symmetry ([Adler 1969](https://doi.org/10.1103/PhysRev.177.2426),
[Bardeen 1969](https://doi.org/10.1103/PhysRev.184.1848)); the
Adler--Bardeen result controls the higher-order status of the anomalous
divergence in its scope
([primary paper](https://doi.org/10.1103/PhysRev.182.1517)).

For a four-dimensional `U(1)` theory with left-handed Weyl charges `q_i`, the
cubic gauge and mixed gauge-gravitational cancellation conditions are the
cubic and linear equations above. Modern work treats their integer solutions
as a Diophantine classification problem and proves general parametrizations
([Costa, Dobrescu, and Fox 2019](https://arxiv.org/abs/1905.13729)). Earlier
constructive work shows both how restrictive and how nonunique anomaly-free
extensions can be
([Batra, Dobrescu, and Spivak 2005](https://arxiv.org/abs/hep-ph/0510181)).

Nothing in that literature is a DU novelty. Its role here is adversarial:
does the selection-accounting contract credit an established quantum
consistency condition without confusing it with a complete physical theory?

# 2. Frozen bounded family

Define `C_{5,9}` as the unordered five-element multisets of charges drawn from

\[
\{-9,\ldots,-1,1,\ldots,9\}
\]

subject to:

1. `gcd(|q_i|)=1`, fixing a primitive integer representative;
2. no pair `q,-q`, excluding vectorlike mass pairs; and
3. quotient by simultaneous sign reversal, corresponding to global charge
   conjugation.

Permutation was already removed by using multisets. Because five is odd and
all charges are nonzero, no admitted chiral spectrum is fixed by global sign
reversal.

Exact enumeration gives:

| stage | count |
|---|---:|
| primitive chiral multisets before global sign quotient | 16,258 |
| physical candidate orbits after global sign quotient | 8,129 |
| orbits satisfying `A_1=A_3=0` | 1 |

The candidate class is generated without looking at `B_2` or `B_4`.

# 3. What the anomaly equations genuinely select

Let

\[
S_{5,9}=\{q\in C_{5,9}:A_1(q)=A_3(q)=0\}.
\]

Then

\[
S_{5,9}=\{(-9,-5,-1,7,8)\}.
\]

This is not `HC-DU-212`'s selector-key relocation. The antecedent contains the
gauge group, representation domain, and quantum-consistency requirement, but
not a survivor label. The survivor is obtained by solving two independent
polynomial constraints.

Accordingly, within the frozen family the selector earns:

- a proper target-blind subfamily;
- non-copy structural selection;
- exact necessity relative to the stated consistency contract; and
- QFT compatibility, because the selected object remains a QFT spectrum.

It does not earn:

- a derivation of `U(1)`;
- a physical reason for five fermions or the charge bound nine;
- a unique spectrum in the unrestricted anomaly-free class;
- dynamics selecting the realized spectrum among consistent theories; or
- a material record interface.

# 4. Held-out target audit

Freeze the quadratic representation target

\[
B_2(q)=\sum_i q_i^2
\]

before enumeration. It is a natural group-theoretic weight entering ordinary
gauge response and running once the coupling and normalization contract are
fixed.

On `C_{5,9}`:

\[
|B_2(C_{5,9})|=313,
\qquad
B_2(S_{5,9})=\{220\}.
\]

The independently audited quartic weight has:

\[
|B_4(C_{5,9})|=1075,
\qquad
B_4(S_{5,9})=\{13684\}.
\]

Several anomalous spectra also have `B_2=220`. Thus neither the target
definition nor its selected value is equivalent to the anomaly predicate.
This is a real bounded target-image contraction.

It is not a physical prediction. At `|q|<=10`, the second anomaly-free orbit

\[
(-10,-4,-2,7,9)
\]

has `B_2=250`, so the selected target image expands to `{220,250}`. The
bounded singleton was conditional on the supplied domain.

# 5. Domain-selection theorem boundary

Let `C_d` be a family of QFT candidates supplied by domain data `d`, and let a
target-blind consistency predicate `P` define

\[
S_d=\{q\in C_d:P(q)\}.
\]

If `S_d` is nonempty and proper, `P` earns structural selection **relative to
`C_d`**. It does not follow that `P` selects `d`, nor that the union

\[
\bigcup_d S_d
\]

is a singleton or target-sufficient.

This is elementary set theory, not a new theorem. Its physical importance is
that the incumbent completion class is itself part of the antecedent passport.
One cannot obtain a unique theory by silently choosing the one finite domain
on which a consistency equation has one solution.

The exact controls show the dependence directly:

| cardinality | charge bound | selected orbit count | example |
|---:|---:|---:|---|
| 5 | 8 | 0 | none |
| 5 | 9 | 1 | `(-9,-5,-1,7,8)` |
| 5 | 10 | 2 | adds `(-10,-4,-2,7,9)` |
| 6 | 5 | 1 | `(-5,-1,-1,-1,4,4)` |
| 7 | 4 | 1 | `(-4,-2,-2,-1,3,3,3)` |

Anomaly cancellation does real work in every row. The row selection is
additional work not performed by the anomaly equations.

# 6. Ruler and normalization boundary

The overall normalization of an abelian charge assignment can be exchanged
against the gauge coupling. For the selected spectrum,

\[
B_2(2q)=4B_2(q),
\]

but

\[
(g/2)^2B_2(2q)=g^2B_2(q).
\]

Therefore a bare integer `B_2` is a representation coordinate until a
physical charge/coupling normalization is fixed. Primitive `gcd=1`
normalization prevents duplicate enumeration; it does not construct the
physical ruler.

This does not erase the anomaly selection. The equations `A_1=A_3=0` are
homogeneous and their zero set is normalization invariant. It changes the
target claim:

```text
anomaly-free representation class          [structurally selected]
bare integer quadratic weight              [normalization-relative]
coupling-weighted observable response       [needs fixed physical coupling]
acquired empirical response                 [also needs selected interface].
```

# 7. Consequence for the current portfolio

## What advances

The `HC-DU-211--212` gate is now calibrated on both sides:

- a Wilson coefficient copying a sector does not earn upstream surplus;
- anomaly equations selecting a proper spectrum family do earn non-copy
  structural selection; and
- neither result selects a complete handoff.

This is decision-changing. DU should no longer ask only whether an action
chooses a state. It should search for source-owned **indices, anomalies,
quantization conditions, and stable consistency constraints** that restrict a
physically justified QFT domain.

## What does not advance

No live candidate is thereby activated:

- **Conditional GU/K77:** highest ceiling remains an action/index/anomaly
  derivation of field content, pairing, or parameter relations. GU still has
  not supplied the source action and explicit QFT map required by DU.
- **Causal action/CFS:** selects within a supplied variational problem but has
  not selected the QFT ansatz, regulator, sector, observer, or instrument.
- **Direct action:** changes the mediator ontology but has not supplied a
  non-copy QFT subfamily with a locked target.
- **Infrared memory:** supplies a partial carrier/formation route but not the
  theory domain, complete handoff, or hard target.
- **Computation/consensus framings:** may illuminate relational architecture
  but do not derive a gauge-theory candidate class through an anomaly theorem.

# 8. Corrected reopener

The next admissible physical packet must now contain all of:

1. an independently justified physical domain of candidate fields,
   representations, parameters, or sectors;
2. a non-copy action, index, anomaly, quantization condition, or stable
   constraint selecting a proper subfamily;
3. the representation/gauge quotient and any charge, scale, or coupling
   ruler;
4. one locked target whose physical image sharpens or exits the incumbent
   image without refit; and
5. a separately selected complete material handoff before any empirical
   claim.

A packet may earn structural selection at step 2 without yet satisfying
steps 3--5. Grades should preserve that partial success.

# 9. Grade, absorption, and stop

## Earned at scoped Grade 4

- exact enumeration of `16,258` primitive chiral encodings and `8,129`
  charge-conjugacy orbits in the frozen family;
- exact anomaly selection of one bounded orbit;
- exact non-copy versus selector-key distinction;
- exact `B_2` and `B_4` target-image contractions;
- exact range and cardinality hostile controls;
- exact charge-normalization/coupling compensation; and
- a corrected domain-and-ruler reopener.

## Absorbed

- anomaly cancellation and its equations are standard QFT;
- their integer solution space is mature Diophantine model-building;
- quadratic and higher representation weights are standard;
- the domain-relative factorization statement is elementary; and
- the passport discipline extends prior DU completion-class, no-refit, and
  ruler controls.

## Not earned

- new anomaly mathematics or QFT;
- universal uniqueness of the five-charge solution;
- physical selection of gauge group, fermion count, charge domain, coupling,
  normalization, state, observer, or instrument;
- a distinctive empirical target or Grade-5 remainder;
- GU transfer, new physics, paper, provider, or hardware result; or
- a ready scientific successor.

# Reproducibility

Run:

```bash
python3 tests/du_anomaly_selected_qft_subfamily_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_anomaly_selected_qft_subfamily_result.json`. It reports
`19/19` exact checks.

# Final status

**BANKED SCOPED GRADE-4 NON-COPY QFT-CONSISTENCY SELECTION CALIBRATION /
ANOMALY CANCELLATION SELECTS A PROPER BOUNDED QFT SUBFAMILY AND SHARPENS TWO
FROZEN REPRESENTATION TARGETS / THE APPARENT UNIQUE SPECTRUM AND TARGET ARE
RELATIVE TO A SUPPLIED CHARGE AND CARDINALITY DOMAIN / BARE QUADRATIC WEIGHT
ALSO REQUIRES A COUPLING RULER / THE COMPLETE RECORD HANDOFF REMAINS
UNSELECTED / THE GATE IS NOW POSITIVELY CALIBRATED BUT NO CURRENT CANDIDATE IS
READY.**
