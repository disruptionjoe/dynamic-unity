---
title: "Bubble-chamber material event record and upstream source-certificate boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-178
run_id: RUN-20260731-013132-bubble-chamber-material-record-gate
work_id: BUBBLE-CHAMBER-MATERIAL-RECORD-REOPENER-AUDIT
action_id: BUBBLE-CHAMBER-MATERIAL-RECORD-REOPENER-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_3
supporting_lanes:
  - lane_1
  - lane_4
  - lane_7
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# Bubble-chamber material event record and upstream source-certificate boundary

## Executive return

```text
MATERIAL_FORMATION_AND_FINITE_RETENTION_FOUND
+ PHYSICALLY_SELECTED_SOURCE_RESPONSE_CONTRACT
+ DETECTOR_EVENT_RECORD_NOT_UPSTREAM_SOURCE_CERTIFICATE
+ ACCESS_AND_DIGITAL_ARCHIVE_SUPPLIED
+ STANDARD_DETECTOR_PHYSICS_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

A bubble chamber closes a real part of Dynamic Unity's record-interface gap.
Conditional on a physically built and prepared chamber, localized deposited
energy can drive a superheated liquid from a metastable blank state into a
growing bubble. The bubble persists as a material distinction until the
chamber is recompressed. This is a source-pinned, target-blind physical
formation-and-retention mechanism; it is not merely a quantum observable, an
ensemble average, or a label added after inspection.

The boundary is equally important:

> The bubble is an exact material record of a nucleation event in the chamber.
> It is only probabilistic evidence about the upstream particle history that
> produced that event.

Different upstream histories can nucleate visually identical bubbles, and the
same declared source class can fail to nucleate because efficiency is below
one. Optical and acoustic channels improve classification and localization,
but they remain separate readout records with calibration, trigger, storage,
and access contracts. The result therefore clears formation and finite
retention relative to a supplied apparatus. It does not select complete
upstream provenance, a unique source class, a digital archive, observer
access, or an unabsorbed higher-response law.

This is a useful physical reopener but not a successor selection. Ordinary
nucleation, detector-response, signal-detection, and experimental-acquisition
theory absorb the components.

## 1. Frozen question and scope

The run asked:

> Does an actual detector's material dynamics select a formed record even when
> that record fails to certify the upstream quantum event?

The bounded comparison used:

1. autonomous thermodynamic quantum detectors as a transient-current control;
2. superconducting nanowire single-photon detectors as a transient-pulse
   control; and
3. PICO-style superheated-liquid bubble chambers as the strongest
   metastable-to-material-archive candidate.

The run did **not** ask bubble-chamber physics to solve the measurement problem
or establish a new ontology. It tested which record duties are physically
realized by a source-pinned apparatus.

## 2. The typed physical chain

For an admitted chamber packet \(\mathcal A\), keep the stages distinct:

\[
X
\longrightarrow
E(x,t)
\longrightarrow
N
\longrightarrow
B_H
\longrightarrow
(V,A)
\longrightarrow
C.
\tag{1}
\]

Here:

- \(X\) is an upstream particle or background history;
- \(E(x,t)\) is its localized energy-deposition field in the active fluid;
- \(N\) is the detector-level occurrence “a supercritical bubble nucleated”;
- \(B_H\) is the bubble morphology retained through a declared horizon \(H\)
  before recompression;
- \(V\) is the optical record and \(A\) the acoustic record; and
- \(C\) is a calibrated event classification or physics inference.

These arrows have different status.

### 2.1 Material formation

Denzel, Diemand, and Angélil directly simulate heat-spike-induced nucleation
in a superheated metastable liquid:
[“Molecular dynamics simulations of bubble nucleation in dark matter
detectors”](https://arxiv.org/abs/1601.07390).

The source gives a physical blank and write:

```text
superheated liquid without a supercritical bubble
  -> localized deposited energy
  -> supercritical vapor region
  -> expanding bubble.
```

Kozynets, Fallows, and Krauss model the subsequent irreversible expansion and
its acoustic emission:
[“Modeling emission of acoustic energy during bubble expansion in PICO bubble
chambers”](https://arxiv.org/abs/1906.04712).

This is stronger than identifying a slow manifold or a possible pointer
sector. The chamber matter undergoes the occurrence-conditioned transition.

### 2.2 Finite material retention

PICO operation supplies a finite physical horizon. In the PICO-60 cycle,
successive live images trigger on a bubble; optical and acoustic data around
the trigger are logged; hydraulic recompression then raises the pressure and
recondenses the fluid:
[PICO-60 detector and cycle description](https://doi.org/10.1103/PhysRevD.93.052014).

Thus \(B_H\) is retained without requiring the camera image to be the thing
that keeps it real. Its persistence is neither eternal nor microscopic
injectivity. It lasts through the declared acquisition horizon and is then
deliberately erased by recompression.

### 2.3 Source-response law

The physical chamber parameters determine a nontrivial response family:

\[
\Pr(N=1\mid X,\mathcal A).
\tag{2}
\]

Li and Piro show why this response cannot be replaced by one ideal step
threshold. Their model combines molecular dynamics, Monte Carlo transport,
and Lindhard energy partition to predict nucleation efficiency for several
target fluids and to improve on the Seitz heat-spike approximation:
[“Model for bubble nucleation efficiency of low-energy nuclear recoils in
bubble chambers for dark matter detection”](https://arxiv.org/abs/2401.15531).

The response contract is therefore physically meaningful and
source-dependent, but stochastic and apparatus-conditioned.

## 3. Exact target-typing result

Let \(\Omega\) be a completion class containing the admitted upstream and
detector histories. Define:

\[
r_N:\Omega\to\mathcal R
\]

as the retained bubble record,

\[
n:\Omega\to\{0,1\}
\]

as the detector-level nucleation occurrence, and

\[
s:\Omega\to\mathcal S
\]

as an upstream source-history target.

### Proposition 1 — detector-event record without source certificate

If

\[
\ker r_N\subseteq\ker n
\tag{3}
\]

but

\[
\ker r_N\not\subseteq\ker s,
\tag{4}
\]

then the same material carrier is a complete record of the detector event
\(n\) and an incomplete record of the upstream source target \(s\).

This is immediate factorization:

- (3) implies \(n=f\circ r_N\) for some \(f\);
- (4) implies no function of \(r_N\) alone reconstructs \(s\).

There is no contradiction and no reason to demote the bubble to “not a
record.” The target changed.

### Proposition 2 — stochastic exact-certification boundary

For source classes \(s_0,s_1\), let

\[
\mu_i(\cdot)=
\Pr(r_N\in\cdot\mid s_i,\mathcal A).
\]

Zero-error source certification from \(r_N\) requires the admitted source
classes to have disjoint record support, equivalently mutual singularity:

\[
\mu_0\perp\mu_1.
\tag{5}
\]

If the laws overlap, no record-only classifier can identify the source class
with zero error. Calibration can still supply a useful likelihood ratio,
posterior, or bounded-error certificate.

The PICO sources supply direct overlap mechanisms:

- nucleation efficiency is generally not one;
- alpha-induced and nuclear-recoil-induced bubbles can be visually
  indistinguishable;
- wall and interface events can have nuclear-recoil-like acoustic signatures;
  and
- acoustic and spatial information improve discrimination without making
  terminal bubble morphology a unique source history.

The strongest empirical controls are:

- [PICO-2L C3F8 results](https://arxiv.org/abs/1503.00008), which report
  threshold-dependent detection and acoustic alpha discrimination;
- [PICO-60 CF3I results](https://arxiv.org/abs/1510.07754), which report
  unknown background populations with distinct acoustic, spatial, and timing
  behavior; and
- [the buffer-free chamber study](https://arxiv.org/abs/1905.07367), which
  reports surface/interface backgrounds, stereoscopic position
  reconstruction, and acoustic discrimination.

## 4. Seven-duty packet audit

| duty | disposition | reason |
|---|---|---|
| physical carrier | **selected relative to the prepared apparatus** | the active superheated fluid and its vapor bubble carry the distinction |
| blank-to-written formation | **physically realized** | localized energy deposition can nucleate a supercritical bubble |
| one-run material event | **physically realized** | an individual chamber cycle contains or does not contain a bubble |
| finite retention | **physically realized** | the bubble grows and remains available until recompression |
| occurrence provenance | **detector-level only** | the bubble certifies nucleation but does not uniquely identify the upstream source history |
| observer access/archive | **physically implemented but externally specified** | cameras, acoustic transducers, triggers, calibration, data logging, and storage define the accessible record |
| reset | **physically realized at apparatus level** | hydraulic recompression recondenses the fluid and starts a new cycle; archive reset is a separate policy |

The strongest earned conjunction is therefore:

```text
prepared apparatus
+ source-response family
+ detector-level formation
+ finite material retention
+ physical reset
```

not:

```text
target-blind complete source certificate
+ uniquely selected access/archive
+ invariant higher-response first leak.
```

## 5. Comparator tournament

| candidate | formed one-run signal | retained without added archive | reset | upstream source certificate | disposition |
|---|---:|---:|---:|---:|---|
| autonomous detector current | partial: emitted excitation/average current model | no | yes | no | transient response host |
| SNSPD electrical pulse | yes, conditional on physical readout chain | no: pulse decays unless captured | yes/recovery | no: efficiency, dark counts, location, and device response remain | transient formed signal |
| bubble chamber | **yes: nucleation and bubble growth** | **yes through the cycle horizon** | **yes: recompression** | no: response distributions overlap | strongest material event record |

The SNSPD controls are documented by the electrothermal and distributed
readout literature, including
[Kerman et al.](https://arxiv.org/abs/0812.0290) and
[Zhao et al.](https://arxiv.org/abs/1811.01067).
They form real detector pulses, but the pulse itself is transient and becomes
a retained record only through downstream acquisition.

## 6. What changed in Dynamic Unity

The prior abstract result `HC-DU-042` said metastability can select a carrier
and retention while leaving write, provenance, access, and action unselected.
`HC-DU-142` separated formation, single-run actualization, and retained
accessible provenance. `HC-DU-162` then showed that a superconducting readout
forms a one-run digitized trace while leaving archive policy and provenance
supplied.

The bubble-chamber specimen adds one narrower physical positive:

> A real apparatus can join formation, one-run material occurrence, finite
> retention, and physical reset before digital readout, while the exact
> upstream source certificate remains unselected.

This corrects two tempting defaults:

1. a physical record need not be a classical data file or an exact source
   certificate; and
2. showing a durable material event does not identify the quantum history
   that caused it.

The detector event and the inferred physics event must therefore remain
different targets in every future record passport.

## 7. Absorbers, grade, and routing

### Strongest absorbers

- classical and molecular nucleation theory;
- metastability and first-passage physics;
- quantum detector and measurement theory;
- signal detection, likelihood, and sufficient-statistic theory;
- PICO calibration, background rejection, and data acquisition; and
- ordinary finite-horizon memory and reset.

### Earned grade

- **Grade 4:** exact target-factorization and stochastic support boundary,
  applied to a source-pinned apparatus packet;
- **Grade 2:** primary-source reconstruction of the detector mechanisms;
- **no novelty credit:** the physical components are standard detector
  science; and
- **no new-physics or paper claim:** this is a dependency clarification and
  reopener audit.

### Campaign decision

The result partially satisfies the physical reopener:

```text
source-pinned theory/apparatus
+ selected formation duty
+ finite retention
+ physical source-response contract.
```

It does not satisfy the campaign's second conjunct:

```text
invariant unabsorbed response-order question
+ finite held-out consequence.
```

Wave 3 therefore remains ineligible. The portfolio returns to explicit
no-ready quiescence.

## 8. Exact reopener

Do not run another detector survey. Reopen this line only if one source-pinned
apparatus or theory supplies at least one of:

1. an upstream provenance carrier whose source-class record laws are
   mutually singular under a frozen fault class;
2. a physically selected access/archive quotient rather than merely installed
   cameras, transducers, triggers, and storage;
3. a no-refit transfer of the same formed-record passport across materially
   different detector platforms; or
4. an invariant response-order distinction with a finite held-out consequence
   not absorbed by ordinary detector-response theory.

## Boundary

This result says what an actual bubble records. It does not identify dark
matter, derive collapse, select consciousness, establish record-first
ontology, or turn a material detector event into a unique biography of its
upstream quantum source.
