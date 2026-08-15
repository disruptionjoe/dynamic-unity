---
artifact_type: phenomenon_to_capability_atlas_contract
schema_version: "0.2"
status: completed_nonrouting_first_method_run
owner: dynamic-unity
primary_lane: "2"
supporting_lanes: ["3", "4", "5", "6"]
channel: CH-SYN
banked: false
maximum_grade: 2
created: 2026-08-15
updated: 2026-08-15
live_routing_authority: ../CURRENT-RESEARCH.yaml
---

# Phenomenon-to-Capability Atlas contract

## Purpose

The atlas is a Dynamic Unity research instrument for carrying a
source-grounded description of a physical phenomenon through five questions:

1. What accepted dynamics and mathematics describe the phenomenon in a stated
   regime?
2. What physical traces and retained records do those dynamics form?
3. Which physical observers can access which records, under which interfaces,
   horizons, resources, and risks?
4. Which tasks become possible for those observers, and which apparent task
   changes disappear after the frame is normalized?
5. What local finality and structural representation, if any, are earned by
   the preceding answers?

This is the forward direction already native to Dynamic Unity:

\[
\text{accepted dynamics}
\longrightarrow \text{records}
\longrightarrow \text{access}
\longrightarrow \text{capability}
\longrightarrow \text{candidate finality and structure}.
\]

It is not an inverse recipe for deriving physics from capability language. It
does not make people ontologically privileged: a person, detector, archive,
laboratory, autonomous controller, or distributed collaboration is admitted
only through a physical observer profile.

## Status and routing boundary

Version 0.1 is a completed, non-routing, unbanked method pilot. Its schema,
six-card bundle, probe, receipt, and dated synthesis remain immutable evidence.
Version 0.2 is an additive first method run: one existing specimen is remapped,
one vertical composition is attempted, and the reusable contract is hardened.
Neither version is a new WIP program, a successor selection, or an executable
continuation. `CURRENT-RESEARCH.yaml` remains the sole live research authority,
and Q0063 remains untouched.

The atlas may become a large catalog only after a separately authorized source
inventory, primary-source audit, denominator freeze, and expansion review. The
six-card set is intentionally called a bounded stress set, never “all known
phenomena.”

## Source custody and adapters

No source repository gives up ownership when an item is represented here.
Every import is pinned to a repository revision and locator, and its filed
evidence grade is preserved independently of the atlas mapping grade.

| Source | Atlas role | Truth boundary |
|---|---|---|
| Geometric Unity | theory/construction requirements and formal dependencies | A Conditional Physics Ledger row is a requirement target, not automatically a physical phenomenon. Crosswalks are many-to-many and must be separately reviewed. |
| Dynamic Unity | integrated dynamics-record-access-capability representation and receiver-owned controls | The atlas can type and compare imported material; it cannot silently promote source claims. |
| Time as Finality | capability projections, future-action classes, and finality diagnostics | A capability object is indexed by observer, task, horizon, action class, resources, risk, and provenance. Finality is not irreversibility alone. |
| Possibility to Capability | transition-witness vocabulary and classifier | The classifier diagnoses a supplied witness; it does not prove the witness or turn raw task growth into normalized capability growth. |
| Temporal Issuance | guarded issuance-versus-disclosure effect type | Access change, settlement, or finality does not imply issuance. |
| Continuity Ledger | occurrence identity, custody, provenance, and material-record discipline | A trace is not automatically a record, and a record is not automatically a public certificate. |

Eligibility is declared on each **claim binding**, not on a repository-wide
adapter. A binding records its claim role, whether it is independent of the
atlas mapping, its physics-grounding status, revision, locator, selector, and
content digest. An accepted-physics description must resolve at least one
independent `PHYSICS_GROUNDING` binding marked `INDEPENDENT_ACCEPTED` under an
adequate domain review. A method, classifier, theory requirement, or atlas
mapping cannot bootstrap that status, even when it lives in a physics-oriented
repository.

In particular, a Geometric Unity Conditional Physics Ledger row is typed as a
`THEORY_REQUIREMENT` unless a separate accepted-physics source supports the
phenomenon claim. The GU crosswalk may expose a requirement, a missing map, or
a negative result; none of those is silently relabeled as empirical grounding.

## Review axes

Version 0.2 separates four questions that v0.1's single lifecycle label could
not answer:

- mapping review: whether the atlas representation itself has been reviewed;
- source review: whether pins, selectors, and paraphrase entailment have been
  checked;
- domain review: whether accepted-physics grounding is adequate for the claim;
  and
- empirical status: what the source actually establishes in the frozen regime.

Independent agreement on a mapping cannot upgrade source or domain review.
Likewise, a valid source pin does not establish that a paraphrase is entailed by
the pinned source. Review records retain reviewer relation, evidence references,
limitations, prior atlas exposure, and whether the exercise was blinded.

## Unit of analysis

An atlas card is not just a phenomenon name. Its unit is:

\[
A_p=(P,D,I,R,O,X,C,F,G,E),
\]

where:

- \(P\): phenomenon, empirical signature, validity regime, and source pins;
- \(D\): governing dynamics, mathematical objects, antecedents, and
  interventions;
- \(I\): physical interface at which a trace or record can form;
- \(R\): typed record ladder;
- \(O\): physical observer/access profiles;
- \(X\): matched contrasts and transition witnesses;
- \(C\): task- and resource-indexed capability;
- \(F\): local/public/global finality assessment and reopeners;
- \(G\): source-native or atlas-introduced structure with an explicit warrant;
- \(E\): evidence grade, absorbers, cheapest kill, falsifier, and nonclaims.

Version 0.2 also requires explicit initial and boundary conditions, plus a
typed record graph. The graph keeps occurrence, trace, retained endpoint,
relation record, estimate, certificate, and action-support edges distinct. A
single ordered ladder remains a useful status projection, but it is not allowed
to erase the DAG that says which endpoints share an occurrence, which process
formed a token, or which calibration and custody relations support a claim.

Two cards with the same phenomenon label but different regimes, interfaces,
observers, or tasks may be different units. Conversely, several source-ledger
rows may constrain one card.

## The record ladder

Every card instantiates all seven levels in order. `ABSENT`, `PRESENT`,
`CONDITIONAL`, `UNKNOWN`, or `NOT_APPLICABLE` is an answer; omission is not.
The v0.1 migration is explicit: `ESTABLISHED` becomes `PRESENT`, `FAILED`
becomes `ABSENT`, and the other statuses retain their names. This migration is
accepted only at the release boundary; legacy vocabulary is rejected by the
v0.2 card schema.

| Level | Question |
|---|---|
| `EVENT` | Did the physical occurrence happen in the frozen regime? |
| `TRACE` | Did it leave a physically coupled difference somewhere? |
| `RETAINED_RECORD` | Was a trace stabilized for a stated retention horizon? |
| `ACCESSIBLE_RECORD` | Can the named observer obtain it through the declared interface and resources? |
| `CERTIFICATE` | Does it decide the explicitly typed target at the declared error/risk level? |
| `PUBLIC_FINAL_RECORD` | Can the relevant observer class independently use a provenance-preserving common record, and is it settled against the declared reopeners? |
| `ACTION_ENABLING_FACT` | Does the record enable a declared operation that was unavailable in the normalized matched frame? |

The ladder is typed by target. A bubble can be an exact record that chamber
nucleation occurred while remaining only probabilistic evidence for the
upstream particle class. Two S1/S2 signals can both be real retained records
while their common-event relation is not recorded.

## Physical observer and access profiles

Each card has at least two observer profiles. A profile declares:

- the physical boundary or substrate;
- admissible interfaces and operations;
- spatial, causal, temporal, authorization, and query horizons;
- resources, calibration, provenance, and error/risk budget;
- the records visible to that observer; and
- the tasks that can actually be performed.

For a person-facing case, the chain is decomposed rather than compressed into
“human observation”:

\[
\text{occurrence}\to\text{detector coupling}\to\text{registration}
\to\text{archive}\to\text{query}\to\text{interpretation}
\to\text{authorized/safe action}\to\text{public certification}.
\]

This prevents neural perception, institutional permission, safe action, and
public agreement from being smuggled into a single access bit.

## Capability and matched contrasts

Capabilities are indexed objects, not intrinsic labels on phenomena:

\[
\mathcal C(O,T,H,A,\mathcal R,\epsilon,\Pi),
\]

with observer \(O\), task family \(T\), horizon \(H\), admissible actions
\(A\), resources \(\mathcal R\), error/risk budget \(\epsilon\), and
provenance requirements \(\Pi\).

Every card includes at least two contrasts and one matched control. Each
contrast uses the Possibility-to-Capability witness fields for possibility
family, representation, description, dynamics, record, access, control,
irreversibility, settlement, raw and normalized task-set relations,
factorization, ordering, and reopening.

The raw task relation is recorded before normalization. A claim of capability
enlargement requires `normalized_task_relation: SUPERSET`. A raw superset that
becomes `EQUAL` after adding the hidden readout, energy, calibration, authority,
time, or provenance resource is not a capability enlargement.

Access and capability also remain distinct. Opening an archive can change
access while leaving the normalized task set equal; a new task can arise from
a physical record transition without any new access channel.

## Projection sufficiency

For a visible projection \(\pi:X\to V\), the atlas asks whether the capability
map is constant on visible-equivalence fibres:

\[
\pi(x_1)=\pi(x_2)\quad\Rightarrow\quad
\mathcal C(x_1)=\mathcal C(x_2).
\]

If this fails, the projection is insufficient for that capability claim. The
verdict is one of `CONSTANT_ON_FIBRES`, `VARIES_ON_FIBRES`, `NOT_TESTED`, or
`NOT_APPLICABLE`, and must agree with the supplied same-visible/different-state
witness. This is a target- and frame-relative test, not a universal notion of
information sufficiency.

The witness is typed rather than inferred from prose. It declares whether a
witness was supplied, whether the visible states are equal, whether the
capabilities are equal or different, and whether the measured spread is zero,
nonzero, unknown, or not applicable. Contradictory combinations fail
validation.

## Finality and Temporal Issuance

Finality is assessed separately at local, public, and global scopes. A
`FINALITY_CANDIDATE` requires all three conditions:

1. settlement for the declared future-action class;
2. no factorization through a preceding record/access/capability layer; and
3. no admissible reopening within the frozen horizon and resource frame.

Irreversibility, long retention, causal inaccessibility, digitization, or
institutional closure alone is insufficient. Every non-`NONE` finality entry
names a reopener or explains why the declared frame excludes one.

Temporal Issuance is an independent field with values `ISSUANCE`,
`DISCLOSURE`, `UNDECIDED`, or `NOT_APPLICABLE`. `ISSUANCE` requires a
source-side primitive and a same-neighbor-data discriminator that survives an
ordinary disclosure/access completion. The atlas never derives it from
finality.

## Structural families and warrants

“Geometry” is intentionally plural. A card may use several structural
families:

- source-native metric, symplectic, gauge, state-space, causal, topological,
  or configuration geometry;
- process or provenance graphs;
- observer projections and fibres;
- quotient or equivalence structures;
- record/capability preorders;
- hypergraphs, matching complexes, presheaves, or sheaves when their gluing
  duties are explicit; and
- smooth geometry only when the source physics supplies smooth structure.

Every structural entry declares its carrier, arrows or relation, invariant,
provenance, and warrant:

- `PHYSICS_OWNED`: explicitly supplied by the accepted source theory;
- `FAITHFUL_REPRESENTATION`: isomorphic/equivalent bookkeeping justified in
  the card;
- `STRUCTURAL_ANALOGY`: useful atlas-introduced representation with no ontic
  claim;
- `OPEN`: proposed but not yet justified;
- `NOT_APPLICABLE`.

Atlas-introduced structure cannot exceed Grade 1 unless a separate formal
equivalence proof is filed. A visually suggestive graph, fibre, or sheaf is
not evidence of a new physical geometry.

## Evidence and claim ceilings

The source claim grade and the atlas mapping grade are separate. Version 0.1
uses the Dynamic Unity scale with a hard atlas ceiling of Grade 2:

- Grade 0: vocabulary, scaffold, or unresolved mapping;
- Grade 1: internally coherent structural or diagnostic representation;
- Grade 2: source-grounded representation with explicit contrasts and
  boundaries.

An imported Grade 4 theorem remains Grade 4 in its source, but placing it on a
card does not make the atlas card Grade 4. Conversely, the atlas cannot promote
an unverified source attribution by giving it polished structure.

Every card names separately:

- the strongest ordinary-physics or established-method absorber;
- the cheapest `representation_kill` that would defeat the atlas mapping;
- a `claim_falsifier` that would defeat the scoped source claim;
- a `regime_reopener` that narrows or reopens the claim without falsifying it;
- a held-out discriminator, including the opposed outcomes it could separate;
- missing source, empirical, or review work;
- explicit nonclaims; and
- its maximum earned atlas grade.

A repair is not a falsifier. For example, adding a physical common-event tag
to an ambiguous detector packet reopens or narrows the regime; it does not
falsify the theorem that the original untagged packet was insufficient.

Passing the schema or validator establishes only representation integrity. It
does not establish scientific truth, novelty, a theorem, an experiment, new
physics, ontology, paper readiness, or publication priority.

## Frozen v0.1 stress set

The first six cards were selected for orthogonal schema stress:

| Card | Primary boundary | Structural diversity |
|---|---|---|
| Environment-induced decoherence and redundant records | formed/redundant record versus accessible and independently readable record | fragment hypergraph, projection fibres, convex state/channel structure |
| Superconducting-ring fluxoid memory | physical memory and normalized capability versus fixed-family disclosure | winding/homotopy and resource preorder |
| Bubble-chamber nucleation | detector-event record versus upstream-cause certificate | typed stochastic chain and source-response fibres |
| Dual-phase-xenon S1/S2 pairing | two formed records versus an unrecorded relation between them | bipartite matching graph/polytope |
| Weak-field redshift clock array | individual records versus jointly realizable reconstruction | affine fibres, sensitivity rank, join complex |
| Schwarzschild-horizon access | causal inaccessibility versus erasure or finality | Lorentzian causal order and exterior projection |

The last two cards deliberately retain `PRIMARY_AUDIT_REQUIRED` source status.
They exercise the fail-closed boundary; they are not presented as
publication-ready physics reviews.

## Expansion gate

A later atlas-wide catalog requires, in order:

1. a source-owned physics-phenomena inventory with explicit inclusion and
   exclusion rules;
2. a versioned denominator and identity policy for regimes, phases, and
   composite phenomena;
3. audited many-to-many crosswalks to the Geometric Unity requirement ledger
   and other theory catalogs;
4. primary-source packets for each card;
5. inter-rater source-grounding and observer-profile review;
6. duplicate/alias detection and coverage reporting; and
7. a separately authorized routing decision.

Until those gates are met, v0.1 is useful as a method, schema, six worked
specimens, and a queue-definition surface—not as an exhaustive ledger.

## Frozen v0.2 first run

The v0.2 release contains one remapped **existing** specimen, dual-phase-xenon
S1/S2 event formation and pairing. It is not a seventh phenomenon and does not
change the v0.1 denominator. The source-first review found that the strongest
detector/fibre result is stable while analyst framing enters materially in five
places: occurrence identity, relation-record topology, primary-task choice,
geometric naming, and falsifier-versus-reopener semantics. Because the reviewer
had prior exposure to the atlas, the exercise is source-first but explicitly
not blinded; the agreement rate is not treated as an independence result.

The vertical specimen follows the superconducting-ring fluxoid-memory packet
through accepted local physics, record formation, observer access, normalized
capability, whole-family completion, issuance, and finality. It returns
`CONDITIONAL_DOWNSTREAM_COMPOSITION_WITH_SOURCE_CLOSURE_FAILURE`:

- the matched normal/superconducting counterfactual supports a finite,
  frame-indexed task-envelope delta carried by record-formation and erasure
  structure;
- the pinned P2C classifier reproduces the supplied matched-frame witness as a
  provisional multi-level dynamics/record/capability diagnosis while explicitly
  declining to verify the physics;
- the same-ring cool-through process and the matched final-temperature
  counterfactual are different relation types and cannot be one commuting
  physical square while preserving identity, final temperature, budget, and
  transduction;
- the current GU requirement ledger contains no superconductivity/fluxoid row,
  so the source edge is absent rather than invented;
- whole-family completion absorbs an absolute novelty reading but not the
  operational capability delta;
- heating, phase slip, a changed horizon, or a changed context remains a
  reopener, so finality is `NONE`; and
- no source grade, physics grade, routing state, or issuance claim moves.

The core card schema is denominator-agnostic. A separate release manifest
freezes exact card identities and content digests, source bindings, hostile
mutations, predecessor digests, and the non-routing posture. This permits a
synthetic seventh-card scalability control without publishing or authorizing a
seventh card.
