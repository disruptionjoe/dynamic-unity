---
title: "Predictive-excess trichotomy, interface-channel preservation, and conditional candidate gate"
status: banked_scoped_result_and_gate_correction
doc_type: exploration
created: 2026-07-31
claim_id: HC-DU-186
run_id: RUN-20260731-051900-predictive-excess-trichotomy
work_id: PREDICTIVE-EXCESS-TRICHOTOMY
action_id: PREDICTIVE-EXCESS-TRICHOTOMY
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
evidence_grade: 4
maximum_grade: 4
---

# Predictive-excess trichotomy and modular interface gate

## Executive return

```text
PREDICTIVE_ABSORPTION_IS_ONLY_ONE_OF_THREE_CASES
+ PREDICTIVE_SHARPENING_AND_RIVAL-EXCLUDING_EXCESS_SEPARATED
+ CONSTANT-BUT-DIFFERENT_INCUMBENT_PREDICTION_RESTORED
+ READOUT_CHANNEL_CAN_PRESERVE_OR_ERASE_BUT_NOT_CREATE_RAW_EXCESS
+ LAW_SELECTOR_AND_INTERFACE_SELECTOR_NEED_NOT_BE_THE_SAME_MECHANISM
+ ONE_JOINED_TARGET-BLIND_PHYSICAL_CONTRACT_IS_REQUIRED
+ REVERSIBLE-POINTER_CSL_IS_CLOSEST_CONDITIONAL_TEST_PACKET
+ CHEN-GIACOMINI_PHASE_SURFACE_RETAINS_THE_HIGHEST_CONDITIONAL_CEILING
+ DRIFT_PACKET_SUPPLIES_INTERFACE_INFORMATION_BUT_NO_NEW_LAW
+ NO_OBSERVED_EXCESS_OR_READY_SUCCESSOR
```

`HC-DU-185` correctly separated representational from predictive
absorption, but its live reopener retained two overconstraints:

1. it required the incumbent target to **vary** across its completion fibre;
   and
2. it required one theory to select both the response law and the apparatus
   interface.

The first condition excludes the most ordinary new-physics test:

```text
incumbent predicts one value
+ challenger predicts a different value.
```

The second confuses a modular experiment with a self-designing law. Physics
can select a response conditional on one preparation, while independently
frozen apparatus dynamics form and acquire the record. The apparatus need
not be derived from the challenger. What must be joined is the complete
target-blind physical contract.

The corrected gate recognizes three exhaustive prediction relations and
then asks whether the physical readout preserves the distinction.

## 1. Frozen question

> What are all ways a locked challenger prediction can relate to the matched
> incumbent completion fibre, and what must a separately formed physical
> record preserve for that relation to become empirically testable?

## 2. Exact prediction trichotomy

Let

\[
\mathcal I(a,r)
=
\{T(c):c\in\mathcal C_I(a,r)\}
\]

be the nonempty set of incumbent target values compatible with frozen
antecedents \(a\) and training record \(r\). Let the challenger lock a
singleton held-out prediction \(h=T_H(a,r)\) before reveal.

Exactly one case holds:

### A. Predictive absorption

\[
\mathcal I(a,r)=\{h\}.
\]

Every matched incumbent completion already gives the challenger value.

### B. Predictive sharpening

\[
h\in\mathcal I(a,r),
\qquad
|\mathcal I(a,r)|>1.
\]

The incumbent permits several values and the challenger selects one of
them. This is predictive specificity, not yet exclusion of the incumbent
family.

### C. Rival-excluding excess

\[
h\notin\mathcal I(a,r).
\]

The challenger prediction lies outside every matched incumbent completion.
The special case

\[
\mathcal I(a,r)=\{i\},
\qquad i\ne h,
\]

is the ordinary contest between two definite predictions.

These cases are mutually exclusive and exhaustive because a singleton
\(\{h\}\) either equals the incumbent image, is a proper subset of a
non-singleton incumbent image, or is not contained in it.

`HC-DU-185` proved the absorption case correctly. The error was translating
its negation into only Case B. Predictive non-absorption contains both B and
C.

## 3. A physical record is a channel on predictions

Let

\[
Q:\mathcal Y\rightsquigarrow\mathcal R
\]

be the frozen physical acquisition/readout channel from target outcomes to
formed records. For deterministic finite targets this is a map; generally it
is a stochastic channel. The operational comparison uses the pushforward
families

\[
Q_\ast\mathcal I
\quad\text{and}\quad
Q_\ast h.
\]

A channel may erase raw excess. For example, raw predictions \(2\) and \(4\)
are rival-excluding, but a readout retaining only parity maps both to
“even.” An identity readout preserves them.

A channel cannot manufacture a difference from identical raw target laws.
This is the ordinary data-processing direction. A useful interface must
therefore preserve the candidate distinction at the declared error and
resource level.

The surrounding mathematics is occupied by Blackwell comparison of
experiments, sufficiency, data processing, and their quantum extensions.
Buscemi's
[quantum statistical comparison theorem](https://arxiv.org/abs/1004.3794)
types quantum coarse-grainings as completely positive trace-preserving maps.
Dynamic Unity does not claim novelty for that theory.

## 4. Modular selection theorem

Let:

- \(S_L\) select/freeze a response law or challenger prediction from physical
  antecedents;
- \(S_Q\) select/freeze a material acquisition channel from apparatus,
  preparation, calibration, and access antecedents; and
- \(Q\circ L\) be their typed composition.

### Proposition

A no-refit empirical comparison does not require

\[
S_L=S_Q
\]

or one mechanism that derives both selections. It requires:

1. both modules are fixed before the held-out result;
2. their domains/codomains and physical occurrence identities compose;
3. the apparatus channel preserves the declared prediction relation;
4. nuisance, selection, and rejected-attempt contracts are frozen; and
5. no target-dependent parameter or interface change occurs after reveal.

### Proof

The recorded prediction is \(Q_\ast P\). Once \(P\) and \(Q\) are
independently fixed and composable, their pushforward is fixed. Its value
does not depend on whether one mechanism selected both objects. Conversely,
if either module remains adjustable after reveal, the recorded target can be
refit. If \(Q\) identifies the rival predictions, the raw distinction does
not survive acquisition. \(\square\)

This does **not** weaken the North Star. DU still asks what physical
antecedents select or realize the interface. It removes the unnecessary
claim that the candidate fundamental law must also choose the experimental
apparatus.

## 5. Smallest exact controls

The executable checks:

- incumbent \(\{2\}\), challenger \(2\): absorption;
- incumbent \(\{2,4\}\), challenger \(4\): sharpening;
- incumbent \(\{2\}\), challenger \(4\): rival-excluding excess;
- a resolving readout preserves the last case;
- a parity readout erases it;
- independently frozen response and interface selectors compose; and
- one quadratic response across configurations \(u=0,1,2\) cannot be
  absorbed by refitting a preregistered affine nuisance family because its
  second finite difference is nonzero.

The last fixture is an experimental-design control, not a physical model.
With one configuration, one free scalar nuisance absorbs one scalar
challenger contribution. Configuration diversity and a frozen nuisance
family are load-bearing.

## 6. Strongest existing candidates after correction

### 6.1 Reversible-pointer CSL — closest conditional packet

`HC-DU-157` already provides:

- a fixed unitary-QM baseline with ideal visibility revival;
- a CSL challenger with path-integrated visibility suppression;
- a proposed Ramsey readout;
- a multi-configuration kernel \(K(r_c)\);
- a frozen nuisance design \(B\); and
- the exact identifiability condition
  \(K(r_c)\notin\operatorname{col}(B)\).

For one frozen nonzero \((\lambda,r_c)\), standard unitary QM and CSL give
constant-but-different response surfaces after the nuisance quotient. That
is Case C, not Case B.

This packet is closest to the corrected test shape, but it remains
conditional:

- the source is a July 2026 proposal, not observed data;
- CSL parameters and mass-density coupling are postulated;
- the apparatus and Ramsey interface are designed, not selected by CSL;
- full acquisition/rejected-attempt lineage is absent; and
- the cited proposal does not outperform every existing noninterferometric
  bound.

The modular theorem removes only the invalid requirement that CSL itself
choose the apparatus. It does not promote the proposal.

### 6.2 Chen--Giacomini phase surface — highest conditional ceiling

`HC-DU-148--151` preserve a linearized-quantum-gravity prediction whose
source-shape and commutator-dependent time response differ from the Newton
potential and declared classical/semiclassical rivals. The published
[Physical Review X result](https://doi.org/10.1103/hl1c-t8z9) explicitly
presents effects beyond the Newton potential; its
[full preprint](https://arxiv.org/abs/2402.10288) supplies the derivation.

Under the corrected trichotomy this is also a Case-C-shaped conditional
candidate relative to the frozen rival classes. A direct matter
representation does not absorb it unless an independently selected
incumbent law predicts the same surface.

Its ceiling is higher than CSL for DU's geometry/field ambitions, but its
packet is less complete:

- the relational joint probability has not been transported through the
  authors' later physical quantum-reference-field construction;
- controller stress, back-reaction, gauge/split completion, and same-order
  terms remain open;
- no acquisition packet exists; and
- field ontology does not follow from source--probe records alone.

### 6.3 DRIFT-IId — physical interface without new-law excess

`HC-DU-184` supplies a real acquired detector packet joining absolute-depth
and ensemble polarity information. It materially advances the interface
side. Its response is standard detector physics and supplies no challenger
law or rival-excluding target. It therefore cannot be welded to CSL or
linearized gravity merely because both need a detector.

## 7. Corrected reopener

Replace:

> target varies across the matched incumbent completion fibre, and one
> source-pinned theory selects both law and interface

with:

> one joined source-pinned physical contract locks a held-out target that is
> not predictively absorbed by the matched incumbent fibre—either predictive
> sharpening or rival-excluding excess—and acquires it through a separately
> frozen, physically formed interface that preserves the distinction without
> target-dependent refit.

The **same contract** must type the composition. The **same mechanism** need
not select every module.

## 8. Grade and disposition

Earned:

- scoped Grade-4 exhaustive predictive-relation trichotomy;
- exact interface-preservation/erasure boundary;
- modular law/interface selection proposition;
- corrected campaign reopener; and
- conditional candidate ranking under the corrected rule.

Absorbed:

- Blackwell comparison and statistical experiments;
- classical and quantum sufficiency;
- data processing and identifiability;
- preregistration and no-refit experimental design;
- CSL phenomenology; and
- linearized quantum-gravity source/probe response calculations.

Not earned:

- no observed response surface;
- no CSL or quantum-gravity validation;
- no complete nuisance or acquisition packet;
- no DU-owned new law;
- no selected fundamental apparatus;
- no Grade-5 remainder;
- no paper or hardware action; and
- no ready successor.

The current best order is:

1. preserve the CSL packet as the closest conditional test architecture;
2. preserve the Chen--Giacomini surface as the highest-ceiling conditional
   candidate;
3. do not simulate either locally merely to reproduce supplied equations;
4. reopen only for a new complete source calculation, observed packet, or
   independently versioned prediction lock that closes a named current gap.

## 9. Exact regression

Run:

```bash
python3 tests/du_predictive_excess_trichotomy_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_predictive_excess_trichotomy_result.json`.

Passing establishes only the finite trichotomy, readout-channel, modular
composition, and response-shape boundaries. It establishes no physical
candidate, complete nuisance class, selected interface, observed anomaly,
new physics, or ready successor.
