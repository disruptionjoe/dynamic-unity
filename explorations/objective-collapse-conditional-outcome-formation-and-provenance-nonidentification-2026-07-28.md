---
title: "Objective-collapse conditional outcome formation and provenance non-identification"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-081
run_id: RUN-20260728-134451-objective-collapse-formation-provenance
run_plan: "../lab/process/runs/RUN-20260728-134451-objective-collapse-formation-provenance/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-134451-objective-collapse-formation-provenance/run-receipt.md"
owner_repo: dynamic-unity
---

# Objective-collapse conditional outcome formation and provenance non-identification

## Executive result

Swing 2 returns a typed conjunction:

```text
macroscopic_outcome:
  ONTOLOGY_CONDITIONAL_FORMATION_ONLY

write_provenance:
  TERMINAL_PATTERN_WITHOUT_OCCURRENCE_IDENTITY

collapse_provenance:
  PHYSICAL_OCCURRENCE_WITHOUT_SELECTED_RETAINED_ARCHIVE

interface_selection:
  SUPPLIED_APPARATUS_CALIBRATION_AND_ACCESS

cross_ontology:
  COMMON_OPERATIONAL_OUTCOME_QUOTIENT_ONLY
```

In plain terms:

> Once a complete GRW theory, apparatus, ready state, interaction, readout
> window, and calibration are fixed, the primitive ontology can physically
> realize a definite macroscopic outcome. In GRWm that outcome is read from a
> coarse matter pattern; in GRWf it is read from a pattern of flashes over a
> finite interval. That is real conditional record formation. But the collapse
> law and primitive ontology do not select the apparatus, interval,
> coarse-graining, calibration, retention contract, or observer access.
> Moreover, a terminal outcome pattern does not certify how it was formed, and
> collapse theory itself forbids universally reliable access to whether a
> specified collapse occurred.

The result therefore avoids two opposite errors:

- it is too strong to say that GRW provides only an event with no possible
  archive; ordinary apparatus dynamics can conditionally form one; and
- it is too strong to say that objective collapse itself selects a
  provenance-bearing record architecture.

No endogenous formed-provenance archive was found. A strictly conditional
record-to-target test remains admissible, but it must freeze the supplied
apparatus qualifier and cannot treat the record as a certificate of collapse
history.

## 1. Frozen object types

Use the two complete theories admitted by `HC-DU-080`:

\[
\Theta_f=(L_{\rm GRW},PO_f),
\qquad
\Theta_m=(L_{\rm GRW},PO_m).
\]

For one bounded apparatus worldtube \(W_A\), define:

- \(B\): a declared ready macroregion at \(t_0\);
- \(W\): the source--apparatus write interaction during \([t_0,t_1]\);
- \(\tau>t_1\): the retained-readout time;
- \(X_A\): one bounded physical readout coupling;
- \(P_W\): whether the claimed blank-to-written source interaction occurred;
- \(P_C\): whether a specified spontaneous collapse/flash occurred in the
  declared source interval; and
- \(T\): the response of a separate pointer under a fixed intervention after
  \(\tau\), escrowed but not used in this swing.

The ontology-native candidates are:

\[
Q_f=F\cap W_A\cap[\tau-\delta,\tau]
\]

and

\[
Q_m=\operatorname{CG}_{\ell}\!\left(m|_{W_A,\tau}\right).
\]

They are not literally the same object. Supplied calibration functions:

\[
\zeta_f:Q_f\to Z,
\qquad
\zeta_m:Q_m\to Z
\]

can nevertheless define one common finite operational outcome alphabet.

## 2. What the GRW outcome formalism actually supplies

Goldstein, Tumulka, and Zanghì derive a GRW outcome formalism by beginning with
a specified experiment. Its ingredients include the apparatus, ready state,
interaction dynamics, time interval, and a calibration function that reads an
outcome from the primitive ontology.

For GRWf, the full flash history has a history POVM \(G\). If:

\[
Z=\zeta_f(F_A),
\]

then the outcome law is the pushforward:

\[
\mathbb P(Z=z)
=
\left\langle\psi\middle|
G\!\left(\zeta_f^{-1}(z)\right)
\middle|\psi\right\rangle,
\]

after the apparatus degrees of freedom are reduced in the standard way.

For GRWm, a calibration function reads the apparatus display from the
matter-density field, commonly at the end of the experiment. For GRWf, a
macroscopic pointer requires many flashes and is naturally read from a short
late interval rather than one instantaneous event.

This establishes a real conditional positive:

### Proposition 1 — apparatus-relative outcome formation

Fix a complete theory \(\Theta_{f/m}\), an apparatus initially in a declared
ready macroregion, its interaction dynamics, a retention horizon, and a
calibration function. If the dynamics sends the ready macroregion into
macroscopically separated outcome regions that remain distinguishable through
the horizon, then \(Z=\zeta_{f/m}(Q_{f/m})\) is a physically formed,
future-readable outcome record relative to that experiment.

The statement is conditional because the experiment supplies the carrier,
coupling, macroregions, horizon, and calibration. The GRW law determines the
history distribution and thereby the outcome statistics after those choices;
it does not select those choices.

This is the precise sense in which objective collapse improves on a bare
channel, endpoint density matrix, or nonunique stochastic lift: the complete
theory plus apparatus has an actual primitive history that realizes the
pointer pattern.

## 3. Why this is not endogenous interface selection

The same primitive history supports many mathematical coarse-grainings.
Nothing in the cited law alone chooses:

- which subsystem is the apparatus;
- which region and time interval count as its display;
- the ready macroregion;
- the flash-window width \(\delta\);
- the matter coarse-graining scale \(\ell\);
- the calibration maps \(\zeta_f,\zeta_m\);
- which later interactions count as bounded access;
- the required retention horizon; or
- which rival histories the outcome must exclude.

The experiment formalism explicitly takes this structure as part of the
experiment. It then proves how outcome probabilities follow.

### Proposition 2 — scoped interface non-identification

Within the source-defined GRW outcome formalism, the collapse law and
primitive history do not determine a unique finite operational record
quotient.

**Reason.** The outcome is obtained only after a calibration map and apparatus
contract are supplied. Distinct maps can partition the same primitive-history
space differently while leaving the primitive law unchanged. Therefore the
law-to-history map does not by itself factor through one selected \(Z\).
\(\square\)

This is a source/type result, not a universal theorem that no deeper physical
principle could select an apparatus or coarse-graining.

## 4. Terminal pattern does not identify formation provenance

Let:

\[
R_\tau:\mathcal H\to\mathcal Q
\]

be any finite candidate depending only on the future-readable apparatus
pattern at \(\tau\) or on the declared late-flash window. Let:

\[
P_W:\mathcal H\to\{0,1\}
\]

denote the claim that the declared source interaction wrote the carrier from
the trusted blank state.

### Proposition 3 — terminal-pattern provenance obstruction

For any admitted rival pair \(h,h'\) satisfying:

\[
R_\tau(h)=R_\tau(h')
\quad\text{and}\quad
P_W(h)\ne P_W(h'),
\]

there is no provenance decoder:

\[
d:\mathcal Q\to\{0,1\}
\quad\text{with}\quad
P_W=d\circ R_\tau
\]

on that rival class.

This is the history-factorization criterion applied to formation rather than
to a later physical target. The hostile twins show exactly how it is met:

| rival | same terminal outcome possible? | differing fact | consequence |
|---|---:|---|---|
| preloaded display | yes, absent a trusted ready-state receipt | claimed write origin | endpoint alone is not provenance |
| alternative writer / rewrite | yes | writer and route | value is not source identity |
| erase then recreate | yes | intervening history | endpoint is not append-only history |
| relocation outside \(A\)'s boundary | yes locally | where provenance remains | global information is not bounded access |
| reset after occurrence | blank endpoint | occurrence happened | event existence does not imply retention |

The preloaded rival is excluded only if the trusted ready-state certification
is part of the contract. The relocation rival is excluded only if the
observer boundary includes the displaced support. An append-only lineage can
exclude erase/rewrite only by adding a persistent trace and its disturbance
model. Every repair is legitimate physical architecture, but none is free.

Thus the obstruction does **not** say that provenance records are impossible.
It says the terminal GRW pointer pattern is not one, and that a provenance
archive must retain additional history-conditioned physical state.

## 5. Collapse occurrence is especially inaccessible

The collapse predicate:

\[
P_C(h)=
\mathbf 1\{\text{a specified collapse occurred in }[t_1,t_2]\}
\]

is a well-defined fact in the GRW process. It nevertheless fails to be a
universally accessible record.

Cowan and Tumulka prove that no experiment can in general determine with
certainty whether a collapse occurred. In a two-branch known-state example,
the optimal reliability is strictly below one whenever collapse probability
is nonzero in the stated regime. For a uniformly random unknown initial pure
state, no experiment improves on blind guessing.

### Proposition 4 — no universal collapse-occurrence certificate

There is no bounded experiment-independent record functional of the
post-interval accessible system that certifies \(P_C\) with zero error for
every admitted initial state.

This follows directly from the cited optimal-detection bounds. A complete
flash history contains the occurrence by definition, but the history is not
therefore a later bounded observer archive. The distinction:

```text
fact exists in primitive history
  != fact is retained in a present carrier
  != fact is reliably retrievable.
```

is physical inside GRW, not merely a Dynamic Unity bookkeeping preference.

## 6. Cross-ontology quotient and its limit

The two ontologies can agree through:

\[
\Pi_f(H_f)=\zeta_f(Q_f)=Z,
\qquad
\Pi_m(H_m)=\zeta_m(Q_m)=Z,
\]

with matched outcome laws for the same experiment.

This earns an operational quotient:

```text
late flash pattern ----\
                        > calibrated outcome Z
coarse matter pattern -/
```

It does not earn:

- a pointwise identification of flash and matter histories;
- one ontology-independent raw archive;
- a law-selected calibration;
- shared microscopic provenance; or
- ontological priority for either arm.

The flash arm is irreducibly interval-typed at the pointer level, while the
matter arm can use a time-slice field. Their operational agreement therefore
demonstrates precisely why value agreement must not erase formation type.

## 7. Five-part formation result

| condition | GRWf with fixed apparatus | GRWm with fixed apparatus | verdict |
|---|---|---|---|
| source-conditioned outcome | macroscopic late-flash pattern | macroscopic matter pattern | conditional pass |
| finite persistence | continued pattern over supplied window/horizon | stable density pattern under supplied apparatus dynamics | conditional pass |
| bounded readout | supplied physical readout and calibration | supplied physical readout and calibration | conditional pass |
| nontrivial outcome information | yes for a functioning measurement | yes for a functioning measurement | conditional pass |
| target-independent definition | frozen before \(T\) | frozen before \(T\) | pass |
| write-route provenance | not fixed by terminal pattern | not fixed by terminal pattern | fail without added lineage |
| exact collapse provenance | not universally accessible | not universally accessible | fail |
| endogenous interface selection | absent | absent | fail |

The correct chairman return is therefore not “no record.” It is:

```text
ONTOLOGY_CONDITIONAL_FORMATION_ONLY
+ TERMINAL_PATTERN_WITHOUT_OCCURRENCE_IDENTITY
+ PHYSICAL_OCCURRENCE_WITHOUT_SELECTED_RETAINED_ARCHIVE
```

## 8. What this changes for the North Star

Before this swing, Dynamic Unity had only a conditional occurrence/matter
antecedent. It now has a sharper complete arrow:

```text
(GRW law, primitive ontology, supplied apparatus)
  -> actual ontology-native macroscopic outcome pattern
  -> supplied finite operational quotient Z
```

The unresolved arrows are:

```text
physical antecedent
  ?-> independently selected apparatus / archive / calibration

terminal outcome
  ?-> provenance-bearing certificate

bounded outcome record
  ?-> nontrivial held-out target contraction beyond law-only prediction.
```

A next swing may test the last arrow only conditionally. It must:

1. keep the apparatus, horizon, calibration, access, and ontology qualifier
   fixed;
2. distinguish ordinary outcome conditioning from provenance certification;
3. compare law-only and record-conditioned target fibres;
4. use a target that is not merely a direct copy of \(Z\); and
5. stop if the GRW outcome formalism already supplies the entire result.

## 9. Warrant, grade, absorbers, and disposition

### Warrant

- `STANDARD`: the cited GRW outcome and accessibility theorems.
- `CONDITIONAL_POSIT`: each complete theory \(\Theta_f\) or \(\Theta_m\) plus
  the fixed apparatus contract.
- `DERIVED`: endpoint-provenance nonfactorization and the no-universal-
  certificate consequence of the source detection bounds.
- `PROJECT_NATIVE`: the formation, access, target escrow, and hostile-history
  typing.

### Grade

```text
Grade 4:
  scoped terminal-pattern provenance non-identification
  and no-universal-collapse-certificate boundary

Grade 2:
  conditional physical outcome-record formation and
  cross-ontology operational quotient

Grade 0:
  endogenous interface selection, provenance archive,
  North-Star target reconstruction, ontology preference,
  and new empirical prediction.
```

### Strongest absorbers

- the standard GRW experiment/outcome formalism;
- ordinary apparatus amplification, persistence, and memory;
- statistical decision theory for event detection;
- history-factorization and data-processing mathematics; and
- ordinary archive relocation across an observer boundary.

The Dynamic Unity increment is the exact typed conjunction: objective collapse
can conditionally form an actual outcome without selecting its operational
interface or certifying its formation history.

### Resource disposition

- source and exact formal analysis decide the gate;
- no trajectory simulation is warranted;
- no external hardware is needed;
- no prediction or paper state changes; and
- Swing 3 remains prepared only as a strictly conditional lawful-fibre test.

## Primary sources

- Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì,
  [The Quantum Formalism and the GRW
  Formalism](https://arxiv.org/abs/0710.0885).
- Valia Allori, Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì,
  [Predictions and Primitive Ontology in Quantum Foundations: A Study of
  Examples](https://arxiv.org/abs/1206.0019).
- Charles Wesley Cowan and Roderich Tumulka,
  [Epistemology of Wave Function Collapse in Quantum
  Physics](https://arxiv.org/abs/1307.0827).
- Charles Wesley Cowan and Roderich Tumulka,
  [Can One Detect Whether a Wave Function Has
  Collapsed?](https://arxiv.org/abs/1307.0810).
- The six-source primary packet cited in `HC-DU-080`.
