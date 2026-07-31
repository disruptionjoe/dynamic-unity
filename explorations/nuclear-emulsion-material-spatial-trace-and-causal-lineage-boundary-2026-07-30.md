---
title: "Nuclear-emulsion material spatial trace and causal-lineage boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-179
run_id: RUN-20260731-014344-nuclear-emulsion-lineage-gate
work_id: NUCLEAR-EMULSION-MATERIAL-PROVENANCE-REOPENER-AUDIT
action_id: NUCLEAR-EMULSION-MATERIAL-PROVENANCE-REOPENER-AUDIT
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
  - CH-MODEL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# Nuclear-emulsion material spatial trace and causal-lineage boundary

## Executive return

```text
MATERIAL_SPATIAL_TRACE_FOUND
+ FINITE_LATENT_ARCHIVE_FOUND
+ LOCAL_FORMATION_PROVENANCE_FOUND
+ CAUSAL_LINEAGE_NOT_INTRINSIC
+ UNIQUE_PATH_COVER_CONDITIONAL
+ EVENT_TIME_AND_DIRECTION_UNSELECTED
+ SOURCE_CLASSIFICATION_CONDITIONAL
+ STANDARD_TRACKING_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

Nuclear emulsion advances the material-record positive beyond the
bubble-chamber event flag. Ionizing passage changes silver-halide grains along
a three-dimensional spatial trace. The latent grain state persists before
development and electronic readout, and developed silver grains retain the
trace for later microscopy. This is a physical material archive of local
deposition occurrences, not merely an abstract observable or transient
current.

The strongest provenance claim nevertheless fails:

> The material selects which local grains changed and their spatial pattern.
> It does not generally store explicit edges saying which grains belong to one
> particle, a timestamp ordering those changes, or a unique upstream source
> identity.

Published emulsion analysis makes that boundary operational. It extracts
grain contours, connects nearby grains using distance and angular tolerances,
extends candidate pairs, and chooses the longest chain as a representative
track. Track membership is therefore a reconstruction relative to a declared
admissibility rule. An exact four-site control confirms that one marked-grain
set can admit two distinct path covers. A physical edge/order tag repairs the
ambiguity; so does an independently warranted physical regime in which the
admissible grain graph has a unique path cover.

The result yields **material spatial provenance**, not full causal lineage.
Standard emulsion physics, tracking, data association, and source
classification absorb the components. No response-order reopener or ready
successor follows.

## 1. Frozen question and target hierarchy

`HC-DU-178` established that a bubble can be an exact material record of
detector-level nucleation while remaining only probabilistic evidence of its
upstream cause. The present run tested the first named reopener:

> Can one source-pinned detector materially retain the upstream causal
> provenance rather than only the terminal detector event?

The word “provenance” was split before inspection:

1. **local formation provenance:** which material sites were altered;
2. **spatial co-membership:** which altered sites belong to one path;
3. **temporal lineage:** in what order and direction the sites were traversed;
4. **source classification:** which particle, interaction, or source class
   produced the path; and
5. **event identity:** which run or time interval the path belongs to.

These targets may coincide in a sparse calibrated experiment. They are not
the same physical object.

## 2. Source-pinned physical chain

For an admitted nuclear-emulsion packet \(\mathcal A\), keep

\[
X
\longrightarrow
E
\longrightarrow
L
\longrightarrow
D
\longrightarrow
I
\longrightarrow
G_\theta
\longrightarrow
P_\theta
\longrightarrow
C
\tag{1}
\]

typed as follows:

- \(X\): upstream particle histories;
- \(E\): local ionization and energy-deposition occurrences;
- \(L\): latent altered-grain field;
- \(D\): developed silver-grain point cloud and morphology;
- \(I\): tomographic or optical images;
- \(G_\theta\): adjacency graph constructed with recognition parameters
  \(\theta\);
- \(P_\theta\): reconstructed path cover or track set; and
- \(C\): particle, energy, direction, or source classification.

The chain contains both physical transformations and inference maps. They
must not be collapsed into one “record.”

## 3. What the material physically selects

### 3.1 Latent formation and finite retention

Silver-halide grains capture radiation-generated electrons and form small
silver nanoparticle latent-image centers. The latent image can fade through
chemical processes, so retention is finite and material-condition dependent:
[“Track formation in nuclear emulsion plates for cosmic-ray imaging with
stabilized Ag nanoparticles”](https://doi.org/10.1016/j.nima.2021.165427).

Fine-grained NIT emulsions record ionizing-particle paths as lines of silver
nanograins, while microscopy is required to read those tracks:
[“Super resolution plasmonic imaging microscopy for submicron tracking
emulsion detector”](https://arxiv.org/abs/1812.09528).

The first solid-state directional dark-matter search exposed an emulsion for
39 days and explicitly describes emulsions as time-insensitive:
[“First direction sensitive search for dark matter with a nuclear emulsion
detector at a surface site”](https://arxiv.org/abs/2310.06265).

Thus the material supplies:

```text
blank grain field
-> history-conditioned latent grain changes
-> retained spatial deposition pattern.
```

It does not need a live electronic trigger to keep the pattern.

### 3.2 Source-dependent response

Track structure depends on energy deposition, particle species, grain
granularity, and recoil physics. Hitachi, Mozumder, and Nakamura model the
electronic energy deposited by carbon, krypton, lead, and proton recoils and
show why several backgrounds occupy related track-structure regimes:
[“Energy deposition on nuclear emulsion by slow recoil ions for directional
dark matter searches”](https://arxiv.org/abs/1905.06664).

The material response is therefore source-dependent and physically useful.
It is not an injective map from complete source histories to grain patterns.

## 4. Where causal lineage enters

Shiraishi et al. use a fine-grained NIT to reconstruct sub-MeV neutron
energies from recoil-proton tracks:
[“Development of New Tracking Detector with Fine-grained Nuclear Emulsion for
sub-MeV Neutron Measurement”](https://arxiv.org/abs/2101.12424).

Their physical and computational stages are unusually explicit:

1. acquire tomographic images;
2. filter images and extract developed-grain contours;
3. remove out-of-focus grains;
4. connect grains below a distance threshold;
5. extend pairs when another grain satisfies distance and angular thresholds;
6. select the longest chain as the representative track; and
7. apply brightness, grain-size, and fiducial cuts.

The automatic recognition efficiency is \(74\pm4\%\), and dust can produce
misrecognized chains. Reconstructed neutron energy also uses the independently
known neutron arrival direction and classical kinematics. The detector is
highly informative, but the source shows that:

- the material point pattern precedes the graph;
- adjacency and path membership depend on a declared algorithm;
- particle-energy reconstruction depends on calibration and a source prior;
  and
- “track” can name either a physical trace or an inferred chain.

## 5. Exact path-cover nonselection theorem

Let \(\Omega\) be an admitted history class. Let

\[
m:\Omega\to\mathcal M
\]

return the retained marked-site field, and let

\[
p:\Omega\to\mathcal P
\]

return the partition of those sites into source paths.

### Proposition 1 — material occupancy does not generally select lineage

If there exist \(\omega,\omega'\in\Omega\) such that

\[
m(\omega)=m(\omega')
\quad\text{and}\quad
p(\omega)\ne p(\omega'),
\tag{2}
\]

then no function of the material occupancy alone reconstructs the path
partition:

\[
\ker m\not\subseteq\ker p.
\tag{3}
\]

Development, scanning, or deterministic image processing that factors
through \(m\) cannot repair (3).

### Smallest finite witness

Take four marked detector sites at the vertices of a cycle \(C_4\). The same
occupied-site record admits two perfect path covers:

```text
cover A: (0--1) + (2--3)
cover B: (1--2) + (3--0).
```

The local material record is identical; the source-lineage target differs.

The exact probe
[`du_material_trace_lineage_probe.py`](../tests/du_material_trace_lineage_probe.py)
enumerates the covers rather than assuming them.

### Proposition 2 — exact repairs

Lineage reconstructs under either of two typed repairs:

1. **record refinement:** retain a physical edge or common-source tag so that
   the record factors \(p\); or
2. **completion-class narrowing:** independently justify a physical
   admissibility class in which the marked-site graph has one path cover.

These repairs must not be conflated. The first changes the record. The second
changes which histories remain possible.

The probe verifies both:

- edge-tagged records factor the path target; and
- deleting one admissible edge turns \(C_4\) into a path graph with a unique
  perfect matching.

### Proposition 3 — time-insensitive direction boundary

Let \(d\) distinguish traversal \(0\to1\) from \(1\to0\). A record containing
only the undirected segment \(\{0,1\}\) satisfies

\[
\ker m\not\subseteq\ker d.
\tag{4}
\]

An ordered endpoint, measured head–tail asymmetry, timestamp, or other
physical orientation field repairs (4). Calling one geometrical axis a
“direction” does not by itself supply its arrow.

## 6. What the source can and cannot certify

| target | disposition | reason |
|---|---|---|
| local altered-grain field | **physically retained** | latent chemistry changes material sites |
| spatial deposition morphology | **physically retained** | positions and grain properties persist through the exposure horizon |
| one reconstructed track | **conditional** | requires development, imaging, adjacency thresholds, and path selection |
| track orientation/head–tail | **not automatic** | a time-insensitive unordered trace need not contain an arrow |
| event time/run identity | **not selected** | long exposure integrates events without native timestamps |
| particle energy | **calibration- and model-conditioned** | range/angle maps and known arrival direction enter the neutron specimen |
| particle/source class | **probabilistic** | recoil, alpha-decay, neutron, fog, and dust responses can overlap |

This yields a provenance ladder:

```text
local material formation
< spatial trace
< unique path membership
< temporal direction
< event identity
< source classification.
```

The ordering is one of logical strength for this typed packet, not a claim
that every detector must implement the stages in that temporal order.

## 7. Absorption, grade, and campaign effect

### Strongest absorbers

- latent-image and silver-halide chemistry;
- nuclear-emulsion detector physics;
- graph path cover and multi-target data association;
- track finding and pattern recognition;
- kinematic reconstruction and detector calibration;
- sufficient statistics and Bayesian source classification; and
- timestamped event-building and provenance systems.

### Earned grade

- **Grade 4:** exact site-record/path-lineage and orientation factorization
  boundaries, plus exact refinements and completion-class repair;
- **Grade 3 conditional:** path reconstruction when a frozen physical
  admissibility class has a unique path cover;
- **Grade 2:** primary-source reconstruction of material trace formation,
  retention, and recognition; and
- **no novelty or new-physics credit:** standard tracking and detector science
  absorb the components.

### What changed

`HC-DU-178` joined detector-event formation and finite retention.
`HC-DU-179` adds a physically retained **spatial provenance carrier** and
locates the next cut:

> Matter can preserve where local history left marks without preserving an
> explicit graph of which marks share one cause.

This is progress toward the North Star because “provenance-bearing record” is
now decomposed into a physical positive and a finite missing relation.

### Why no successor activates

The result does not expose a response-order distinction outside standard
detector, tracking, and inference theory. It also does not select event time,
global lineage, source identity, or the development/microscopy access
quotient. The campaign's dual advance gate remains unmet.

## 8. Exact reopener

Do not run another track-detector inventory. Reopen only with one
source-pinned system that provides:

1. a physical edge/order/event tag surviving independently of offline
   association;
2. a proved unique path cover under a target-blind physical admissibility
   class;
3. mutually singular source-conditioned material-record laws under a frozen
   fault and background class; or
4. an invariant unabsorbed response-order distinction with a finite held-out
   consequence.

## Boundary

This result does not say that published particle tracks are fictitious.
It says exactly what makes them earned: material marks plus a declared,
validated association and calibration contract. It does not identify dark
matter, reconstruct one unique microscopic history, or turn spatial
correlation into intrinsic causal edges.
