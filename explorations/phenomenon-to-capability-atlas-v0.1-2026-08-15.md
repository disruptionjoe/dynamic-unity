---
title: "Phenomenon-to-Capability Atlas v0.1 — six-specimen method pilot"
status: completed_nonrouting_method_pilot
doc_type: research_instrument_synthesis
created: 2026-08-15
owner_repo: dynamic-unity
authority: "Joe direct chat: orchestrate the setup and begin progressing the work in a big wave"
banked: false
routing: none
live_routing_authority: ../CURRENT-RESEARCH.yaml
primary_lane: "2"
supporting_lanes: ["3", "4", "5", "6"]
channel: CH-SYN
maximum_atlas_grade: 2
---

# Phenomenon-to-Capability Atlas v0.1

## Executive return

The right home for this work is Dynamic Unity, but only if the project is
built as a source-sovereign forward atlas rather than a replacement physics
ledger.

Version 0.1 now exists as a completed six-specimen method pilot:

- the [program contract](../docs/phenomenon-to-capability-atlas.md) defines the
  unit, record ladder, observer profile, capability frame, finality gate, and
  structural warrants;
- the [JSON Schema](../specs/phenomenon-capability-atlas-v0.1.schema.json)
  fails closed on the machine shape;
- the [frozen atlas bundle](../lab/phenomenon-capability-atlas/atlas-v0.1.json)
  separates source bindings from Dynamic Unity overlays;
- the
  [deterministic probe](../tests/du_phenomenon_capability_atlas_probe.py)
  checks source pins and rejects planted category errors; and
- this note reports what the six specimens teach and what would have to be
  true before scaling.

The pilot does not alter Q0063, select a successor, occupy a WIP slot, or
authorize a next execution. `CURRENT-RESEARCH.yaml` remains the sole routing
authority.

## 1. The key architectural decision

The atlas contains two kinds of object that must never be blended.

### 1.1 Source bindings

A source binding records:

- source owner and adapter;
- immutable repository revision;
- exact artifact and assertion selector;
- SHA-256 content digest;
- native claim status and evidence grade;
- source nonclaims and missing import requirements; and
- a receiver paraphrase explicitly marked non-authoritative.

This layer prevents the atlas from rewriting source truth. A Dynamic Unity
card may say what a source result is useful for, but it cannot bank an unbanked
result, raise its grade, change a GU verdict, or turn a test fixture into an
experimental fact.

### 1.2 Receiver-owned overlays

The overlay begins only after source binding. It records:

```text
phenomenon and regime
  -> dynamics and antecedents
  -> physical interface
  -> typed record ladder
  -> physical observer/access profiles
  -> matched P2C contrasts
  -> task/resource-indexed capability
  -> TaF projection and finality audit
  -> TI issuance/disclosure classification
  -> warranted structural representations
  -> evidence ceiling, absorber, kill, and nonclaims.
```

This direction matters. Known physics induces a typed capability object. The
capability overlay is not allowed to derive or alter the known physics.

## 2. Why the Geometric Unity ledger is an adapter, not the denominator

The pinned Geometric Unity Conditional Physics Ledger v0.258 has 82 canonical
active targets (and 84 row records because two historical superseded rows are
retained). Its denominator counts representation requirements,
Lagrangian/equation slots, and anomaly/consistency requirements. It does not
count physical phenomena.

That makes it extremely useful—but for a different job. A future atlas can
crosswalk a phenomenon card to the GU requirements that constrain its theory,
and one GU row can constrain many phenomena. The relation is many-to-many.

The v0.1 guard therefore makes the GU adapter
`phenomenon_eligible: false`. The validator plants and rejects the mutation in
which a GU requirement row is cast as a phenomenon. This is the cheapest way
to protect both projects from a misleading “82 phenomena” catalog.

## 3. Frozen portfolio

The first six were selected for schema stress, not because they are the six
most important phenomena or representative of all physics.

| Card | Main boundary | Structural families | Atlas grade |
|---|---|---|---:|
| Environment-induced decoherence and redundant quantum records | decohered/redundant trace versus accessible, distinguishable, independently readable record | state/channel space; fragment hypergraph; visible fibres | 2 |
| Superconducting-ring fluxoid memory | retained winding record and normalized storage capability versus readout disclosure and full-family absorption | homotopy/winding; resource preorder | 2 |
| Bubble-chamber nucleation | exact chamber-event record versus probabilistic upstream-source certificate | stochastic detector chain; source-response fibres | 2 |
| Dual-phase-xenon S1/S2 pairing | two real retained records versus an unrecorded common-event relation | bipartite matching complex; packet fibres | 2 |
| Weak-field redshift clock array | individual admissible records versus physically joined full-rank reconstruction | affine record fibres; sensitivity rank; join hypergraph | 1 |
| Schwarzschild-horizon classical access | causal inaccessibility versus deletion, finality, or a cross-profile capability mismatch | Lorentzian causal geometry; exterior quotient | 1 |

The redshift and horizon cards are deliberately capped at Grade 1. Their local
finite controls are exact enough to test the atlas, but a publication-facing
“accepted physics” card still needs a dedicated primary-source experimental or
GR reference packet. The schema records that gap instead of hiding it.

## 4. Specimen returns

### 4.1 Decoherence and redundant records

The useful unit is not “decoherence happened.” The unit includes the selected
system/environment partition, fragment rule, detector interface, observer
window, and pointer-inference task.

Two contrasts do different work:

1. Holding the physical state fixed and opening the fragment/archive channel
   produces an access change. Raw task support grows, but after the readout
   resource is normalized the task sets are equal. This is not an intrinsic
   capability enlargement.
2. Holding the observer interface fixed while changing distinguishability,
   discord, or independence can change the normalized one-shot inference and
   public-objectivity tasks. This is physical audit content already absorbed
   by strong-QD/SBS—not a new Dynamic Unity mechanism.

Raw mutual-information redundancy is therefore an insufficient visible
projection for the audited capability. The atlas earns a projection-fibre
witness and a typed absorption, not a new theory of measurement.

### 4.2 Superconducting-ring fluxoid memory

The fluxoid is a material record before a SQUID reads it. Adding the SQUID
changes access; it does not create the winding record. The normal versus
superconducting phase contrast is different: under the frozen P2C frame, the
superconducting branch supports finite-horizon, zero-maintenance winding
storage that the matched normal branch does not.

The strongest absorber is equally important. One BCS/GL possibility family
and phase diagram already contains both branches. Heating or a phase slip can
erase the record. The card therefore supports a frame-indexed capability
delta, while absolute finality, whole-family enlargement, and issuance remain
unearned.

### 4.3 Bubble-chamber nucleation

The physical chain is typed:

\[
X\to E(x,t)\to N\to B_H\to(V,A)\to C,
\]

from upstream source through energy deposition, nucleation, finite-horizon
bubble, visual/acoustic channels, and classifier.

The bubble is an exact material record of chamber nucleation in the scoped
apparatus. It is generally not an exact certificate of the upstream source
class because source-conditioned response supports overlap. Recompression
erases the material bubble but need not erase the archived visual/acoustic
record. Finality must therefore be indexed by target, carrier, observer, and
horizon.

### 4.4 Dual-phase xenon S1/S2 pairing

Prompt S1 and delayed S2 can each be physical, retained, queryable records.
That does not mean their common-event relation is recorded. An immutable
triggerless packet can admit more than one physically allowed bipartite
matching.

A correct pair gives the prompt origin needed for absolute drift depth. A
software partition without a physical tag or a unique-matchability theorem
does not. This card is the cleanest pilot demonstration that relational
records need their own provenance duty: preserving two endpoints is not the
same as preserving the edge between them.

### 4.5 Weak-field redshift clock array

Inside the frozen two-source weak-field model, one clock record leaves a
nontrivial source fibre. Two distinct, jointly realized and calibrated clock
records can make the sensitivity matrix full rank and support exact held-out
transfer.

But two counterfactual clock records cannot be concatenated, and two real
records in isolated archives do not give one observer the joint capability.
The physical archive join, authorization, calibration, and common-occurrence
provenance are resources. Enlarging the source or matter-nuisance class
reopens the fibre, so finite rank is not global geometric finality.

### 4.6 Schwarzschild-horizon access

The frozen classical screen gives the strongest negative control. A radial
outgoing signal can reach the exterior cutoff from outside the horizon but
not from the horizon or interior. Two states can have the same exterior shadow
and different interior records while still giving an aligned exterior
observer the same task set.

The apparent capability split appears only if the comparison silently changes
to an infalling or full-slice observer. That is an access-profile mismatch, not
a failure of the exterior projection. The card explicitly excludes Hawking
radiation, evaporation, holography, algebraic QFT, and the black-hole
information problem.

## 5. Cross-specimen findings

### 5.1 Record formation and access are orthogonal

The ring and bubble form material records before a person-facing query path
exists. Decoherence can form conditional environmental traces that are not
independently readable. The horizon can block exterior access without deleting
an interior occurrence. An atlas that uses one `observed` Boolean cannot
represent these cases.

### 5.2 Capability is a comparison, not a property label

Every capability claim needed the same tuple:

```text
observer + task + horizon + action menu + resources
+ error/risk + provenance + normalization frame.
```

The planted raw-growth mutation proves this is load-bearing: if the normalized
task relation is `EQUAL`, the validator rejects `CAPABILITY_ENLARGEMENT`.

### 5.3 Relations can be the missing record

The xenon case makes the point exactly, and the clock-array case repeats it at
a larger scale. Record A and record B can both exist while “A and B came from
the same physical state/event and may be jointly used” remains absent. The
atlas should treat occurrence identity, archive join, calibration join, and
event pairing as first-class relation records.

### 5.4 Finality usually reduces before it generalizes

None of the six cards earns an atlas-level finality candidate. Each apparent
case factors through an earlier layer or has a declared reopener:

- coherent environmental control or a changed fragment audit;
- phase slip or heating;
- recalibration or a new detector channel;
- new pairing side information;
- an enlarged source/nuisance class; or
- a changed causal-access profile or physical theory.

This is a useful success. Time as Finality contributes a disciplined question
and a triple gate; it does not require the atlas to manufacture finality where
ordinary physics, access, or resources suffice.

### 5.5 “Geometry” should be a warranted family

The six cases need several kinds of structure: Hilbert/state geometry,
homotopy, stochastic chains, matchings, affine inverse-problem fibres,
Lorentzian causal order, hypergraphs, quotients, and resource preorders.

Forcing all of them into a smooth manifold would lose information. The useful
common rule is instead:

```text
carrier + maps/relations + invariant + axioms checked
+ source/atlas provenance + warrant + grade ceiling.
```

The validator rejects an atlas-introduced structural analogy relabeled as
source theory. This lets geometric language be ambitious without becoming an
unearned ontological claim.

### 5.6 People enter through a physical chain

No card uses `HUMAN` as an observer primitive. Person-facing capability is
decomposed into detector coupling, registration, archive, query,
interpretation, authorization/safety, action, and public certification. The
planted human-default mutation is rejected.

## 6. Adversarial validation

The deterministic probe currently validates 22 invariant families and rejects
16 planted mutations, including:

- GU requirement-to-phenomenon casting;
- a missing record-ladder stage;
- an unexplained human observer;
- raw task growth promoted to capability;
- irreversibility promoted to finality;
- finality promoted to issuance;
- structural-provenance loss;
- a stale source digest;
- false projection sufficiency;
- a hidden unmatched resource;
- evidence-grade promotion;
- an exhaustive-coverage cast;
- a broken source reference;
- source-authority transfer;
- an ineligible-only physics source; and
- duplicate phenomenon identity.

Passing these checks validates the artifact contract, not the truth of the
physics summaries. Primary-source review remains a scientific operation.

## 7. What a scaled atlas should look like

A credible larger project has five distinct layers:

1. **Source-owned phenomenon inventory.** Freeze inclusion, exclusion,
   identity, regime-splitting, alias, and denominator rules. Do not begin by
   claiming “every known phenomenon.”
2. **Primary-source packets.** Each physical card needs accepted theory,
   governing mathematics, empirical signature, observables, validity regime,
   and explicit anomalies or open boundaries.
3. **Dynamic Unity overlays.** Apply this typed record/access/capability/
   finality/structure contract without modifying the source packet.
4. **Crosswalks.** Link phenomena many-to-many to GU requirements, detector
   families, record interfaces, observer classes, and capability tasks.
5. **Coverage and collision review.** Measure gaps, aliases, disagreement,
   inter-rater consistency, strongest absorbers, and which overlays produce a
   genuinely new held-out question.

A useful next denominator would be domain-stratified rather than a flat list:
mechanics and waves; thermodynamics and statistical physics; electromagnetism
and optics; condensed matter; atomic/molecular physics; nuclear/particle
physics; quantum information/foundations; gravitation/cosmology; plasma and
fluid phenomena; and detector/metrology phenomena. That proposal is a design
surface only. It is not routed or authorized here.

## 8. Highest-value expansion gates

Before scale-up, the most valuable gates are:

- construct a source-owned phenomenon identity policy;
- add primary-source audits for the clock and horizon cards;
- test inter-rater agreement on record-ladder and observer-profile typing;
- define a reviewed many-to-many GU crosswalk format;
- add relation-record primitives for event pairing, joint realizability, and
  custody joins;
- compare graph, quotient, sheaf/presheaf, causal, and resource structures by
  explicit proof obligations rather than visual appeal; and
- require at least one held-out capability or projection prediction before a
  card can exceed representation grade.

Only a later Joe-directed routing decision can turn one of these gates into
live work.

## 9. Evidence ceiling and nonclaims

The v0.1 maximum atlas grade is Grade 2; the clock and horizon cards remain at
Grade 1. Source-native results retain their own grades, but those grades do not
transfer to the atlas.

Not established:

- an exhaustive physics-phenomena ledger;
- a new law of access, capability, finality, issuance, or observation;
- a universal geometric carrier for physical records;
- a derivation of physics from observer capability;
- a privileged role for people;
- a new mechanism, empirical anomaly, prediction, experiment, or hardware
  need;
- a paper or publication posture; or
- any change to live Dynamic Unity routing.

The result is narrower and useful: a durable method, a strict machine
contract, six worked stress specimens, explicit source gaps, and a validator
that already rejects the most tempting category mistakes.
