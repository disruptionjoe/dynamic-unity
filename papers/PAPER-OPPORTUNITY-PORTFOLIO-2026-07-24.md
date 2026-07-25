---
title: "Dynamic Unity paper-opportunity portfolio and preliminary readiness audit"
status: completed_portfolio_audit_and_factory_intake
doc_type: upstream_paper_opportunity_inventory
created: 2026-07-24
run_id: RUN-20260724-204614-paper-opportunity-portfolio-audit
source_revision: 63a50a212d789797b6e21c0f3cf109ae7d34ecbe
reconciled_source_revision: 0504f948891a97b87fdfca561575d3490d92d97d
factory_intake_revision: ca7b748e58e9210fbace1ad897df88f849ae9ff5
claim_grade: "PORTFOLIO, FACTORY-SEED READINESS, AND CONFIRMED INTAKE / NO SCIENTIFIC, PRODUCTION, OR PUBLICATION PROMOTION"
---

# Dynamic Unity paper-opportunity portfolio

## Result

The repository currently exposes **27 deduplicated paper families**:

| Upstream disposition | Count | Meaning |
|---|---:|---|
| Factory post-ready | 1 | Existing Factory package; do not duplicate |
| Factory-seeded, unselected | 8 | One pre-existing seed plus seven newly admitted standalone seeds |
| Factory merge review | 2 | Newly admitted for deduplication against named existing or new seeds |
| one bounded clarification before seed | 4 | One source-owned choice is needed to make the opportunity credible and sortable |
| merge rather than standalone | 6 | Real result or concept module, but no distinct paper at current novelty grade |
| research result required | 4 | Still an agenda or dependency rather than a credible paper opportunity |
| transfer to another source owner | 2 | Paper-shaped, but Dynamic Unity does not own the research truth |

This is the upstream source-owner inventory plus a receipt for confirmed
Factory custody. It is **not** a parallel Factory queue, production plan,
drafting authorization, scientific ranking, submission decision, or
publication ledger.

The machine-readable portfolio is
`papers/paper-opportunity-portfolio.json`. Its deterministic audit is
`tests/du_paper_opportunity_portfolio_probe.py`.

## The seed-readiness correction

Dynamic Unity had been conflating two different gates:

```text
Factory seed readiness
    = cheap opportunity pointer

scientific hardening readiness
    = claim can support the intended manuscript or experimental protocol
```

The Drafting Factory requires only an owning source, evidence pointers,
possible contribution, audience, current grade and open conditions, overlaps,
and an unselected/no-request posture. It explicitly does **not** require a
novelty verdict, completed proof, draft, or production commitment.

The older prediction register's stringent quantitative/platform/cheap-kill
gate remains useful, but it now names **scientific prediction hardening**, not
the minimum threshold for preserving a paper opportunity in the Factory.

## Work estimate convention

A **source swing** means one concentrated research job with a decisive return,
such as:

- a theorem plus proof and counterexample;
- a claim-specific primary-literature collision review;
- a cross-platform transfer with unchanged semantics;
- a calibrated experimental/null packet; or
- a matched-resource lower-bound and construction pair.

The estimates are workload classes, not calendar promises:

| Manuscript distance | Count |
|---|---:|
| Factory post-ready | 1 |
| one source-hardening swing | 6 |
| two or three source swings | 7 |
| dependency program | 5 |
| not standalone at current grade | 8 |

## A. Existing Factory custody

| ID | Candidate | Current state | Remaining source work |
|---|---|---|---|
| `DU-PAPER-001` | **Collapse Without a Preferred Now** | Factory post-ready at relocation grade | None for the bounded paper. AQFT embedding or predictive collapse would be a new paper. |
| `DU-PAPER-002` | **Scale-Free Laws Source Structure, Not Particulars** | Existing high-conviction Factory seed | `2–3` swings: choose theorem versus synthesis, complete collision review, and separate imported/superseded physics. |

Neither should be reseeded.

## B. Confirmed Drafting Factory intake

### Standalone seeds

| ID | Working paper | Current source grade | Estimated manuscript work | Load-bearing next work |
|---|---|---|---:|---|
| `DU-PAPER-003` | **Covariant Records Are Not Free** | Exact Clock-QCA recorder, obstruction, complementarity, archive, and boundary controls | `1` swing | Primary-literature collision plus a tight approximate record-disturbance-support/archive-cost theorem |
| `DU-PAPER-007` | **Interventional Record Sufficiency** | Exact finite and finite-linear factorization/witness baseline | `2–3` | Freeze completion class, build proof-carrying compiler, and transfer unchanged across quantum and distributed fixtures |
| `DU-PAPER-009` | **Higher-Order Public Finality** | Exact reversible holonomy/fixed-algebra/project-or-lift baseline | `2–3` | Noninvertible/noisy theorem, higher-certificate relation, and BFT/QEC transfer |
| `DU-PAPER-013` | **Tail Universality Classes in Causal-Set Post Renormalization** | Known exact post map plus locally derived multi-tail exponent family | `1` | Full causal-set collision review and a uniform asymptotic theorem with tight counterfamilies |
| `DU-PAPER-015` | **Is a Global Update Clock Physical or Gauge?** | Five exact finite scheduler/clock controls and reunion no-go | `1–2` | One unified gauge-or-witness theorem and logical-clock/relativity/discrete-model collision review |
| `DU-PAPER-016` | **Systems Without a Privileged Depth** | Exact finite active-control constructions and depth-refinement countertheorem | `1–2` | General role-cover theorem, prior-art review, and one non-toy specimen |
| `DU-PAPER-017` | **Finite Records Cannot Certify Open-Endedness** | Exact aliasing, finite-prefix, fixed-completion, and fixed-oracle controls | `1–2` | Freeze completion/novelty class and prove a parameterized escape-or-incomplete-contract theorem |

These seven are now canonical unselected Factory seeds at
`drafting-factory@ca7b748e58e9210fbace1ad897df88f849ae9ff5`. Factory
prioritization may reorder them against every other research seed. Custody
does not activate any of them.

### Merge-review seeds

| ID | Working paper | Why the seed is complete | Merge question |
|---|---|---|---|
| `DU-PAPER-004` | **Boundary Relocation, Record Access, and Capability** | Exact finite relocation and reunion controls; contribution and theorem target are clear | Standalone restricted invariance theorem, or a theorem section inside `DU-PAPER-003`? |
| `DU-PAPER-024` | **A Covariant Finality Deviation Beyond Smooth Decoherence** | Conditional opportunity, current absorber, platform need, and claim ceiling are explicit | Separate long-horizon experimental seed, or remain linked to existing `DU-PAPER-001`? |

Both entered the Factory as merge reviews rather than presumptively distinct
production candidates. Neither has a production home.

## C. One bounded clarification before cheap seed

| ID | Candidate | Clarification needed | Manuscript distance afterward |
|---|---|---|---|
| `DU-PAPER-010` | **Finality, Capability, and Coherent Optionality** | Choose the first physically formed distinction and state the exact matched-frame theorem | `2–3` source swings |
| `DU-PAPER-019` | **Record-Relative Actuality** | Select one formal state object and state one theorem plus one killing counterexample | `2–3` |
| `DU-PAPER-020` | **Informational Distance and Reality Bandwidth** | Choose an operational distance class or a scalar-impossibility theorem and its smallest network | `2–3` |
| `DU-PAPER-021` | **The Cost of Making a Fact Public** | Freeze one matched protocol pair and candidate residual beyond ordinary accounting | `2–3` |

These are not missing metadata. They are missing the decision that determines
what paper is actually being proposed.

## D. Real modules that should merge, not seed separately

| ID | Material | Current disposition | Best destination |
|---|---|---|---|
| `DU-PAPER-005` | finite record-selection and coalition-access quotient | Exact but standard component mathematics | `DU-PAPER-007` or the CCR umbrella |
| `DU-PAPER-006` | rejection of one universal objectivity threshold | Exact controls; known quorum/Blackwell/SBS/QEC terrain | `DU-PAPER-009` or `DU-PAPER-010` |
| `DU-PAPER-008` | signed all-port coherent-history assay | Exact analytic control; current proper-time certification collision | physical arm of `DU-PAPER-007` |
| `DU-PAPER-018` | influence-distribution objects and no-selector/no-scale result | Standalone proxy route stopped | existing `DU-PAPER-002` seed |
| `DU-PAPER-022` | protected public facts as logical codes/phases | Concept plus known thresholds; no distinct theorem | `DU-PAPER-009` or `DU-PAPER-010` |
| `DU-PAPER-023` | observer identity as record colimit | Formal and philosophical layers not yet separated | formal portion into `DU-PAPER-016` |

This merge discipline is how the inventory remains broad without turning
every exact lemma or evocative concept into a nominal paper.

## E. Research result required before seed

| ID | Candidate | Why it is not yet a credible paper opportunity | Minimum result needed |
|---|---|---|---|
| `DU-PAPER-011` | **Meta-Record Geometry** | Reconstruction object, refinement category, and uniqueness theorem are absent | First assumption-minimal reconstruction or nonuniqueness theorem |
| `DU-PAPER-012` | **Certified Causal Reality** | This is still the umbrella charter | At least two theorem families plus unchanged quantum/distributed transfer |
| `DU-PAPER-014` | **Post-Generating Causal Growth and Emergent Geometry** | No fixed family jointly earns posts, running, and held-out geometry | One fixed-law survivor or a class-level no-go |
| `DU-PAPER-027` | **Physical Recovery from Certified Causal Reality** | No certified-causal substrate or nontrivial QFT/GR/GU recovery exists | Upstream theorem spine plus one honest recovery/obstruction result |

Raw agenda seeds for these would duplicate the research program rather than
preserve a concrete publication opportunity.

## F. Transfer rather than DU seed

| ID | Candidate | Correct owner or merge |
|---|---|---|
| `DU-PAPER-025` | conditional mirror-sector, generation, and cosmology predictions | `gu-formalization`; DU retains only recovery-test pointers |
| `DU-PAPER-026` | sovereign-agent error decorrelation and council methodology | `ai-epistemology` and the Factory's existing AI research methodology candidate |

No transfer has been sent by this audit.

## The most useful portfolio interpretation

### Closest source packets

One item is already Factory post-ready. Six more paper families are plausibly
one concentrated source-hardening swing from a defensible packet:

1. `DU-PAPER-003` — covariant records;
2. `DU-PAPER-013` — causal-set post tail classes;
3. `DU-PAPER-015` — global clock gauge-or-witness;
4. `DU-PAPER-016` — systems without privileged depth;
5. `DU-PAPER-017` — finite records and open-endedness; and
6. `DU-PAPER-004` — boundary relocation, likely merged with `003`.

This does not reorder scientific importance. It measures distance from current
source material to a paper-shaped package.

### Highest-upside source sequence

If Dynamic Unity funds only one paper-hardening swing:

1. **`DU-PAPER-003`** remains the shortest credible paper path.
2. **`DU-PAPER-007`** remains the flagship route most central to the program.
3. **`DU-PAPER-009`** remains the most distinctive cross-domain theorem route.

The portfolio adds `013`, `015`, `016`, and `017` as serious lower-cost
alternatives that the previous top-three exercise did not fully expose.

### Why the new alternatives matter

- The CSG tail-class result already has a compact theorem shape, but it is
  collision-sensitive because causal-set post renormalization is established
  terrain.
- The global-clock result has multiple exact countermodels and a clean
  gauge-or-witness question, but needs one unified theorem rather than five
  probe narratives.
- The role-cover result may be more publishable as control/system
  individuation than as fundamental physics.
- The open-endedness result could consolidate a repeated lesson across DU,
  Temporal Issuance, and finite process theory, provided its completion class
  is not defined to force the answer.

## Preliminary primary-literature collision scan

This is a routing scan, not a claim-specific novelty verdict.

- QCA has a mature structure and simulation literature, so
  `DU-PAPER-003` must live on the new record tradeoff rather than the use of a
  QCA host:
  [Arrighi's QCA overview](https://arxiv.org/abs/1904.12956) and
  [the exact Clock-QCA source](https://arxiv.org/abs/1404.4499).
- Process tensors and complete operational histories are established, so
  `DU-PAPER-007` must contribute the physical-refinement trichotomy and
  cross-platform proof object:
  [operational quantum process framework](https://arxiv.org/abs/1512.00589).
- Cohomological obstruction, database contextuality, and correctable operator
  algebras are mature neighboring fields for `DU-PAPER-009`:
  [contextuality, cohomology, and databases](https://arxiv.org/abs/1502.03097)
  and
  [general-noise QEC](https://arxiv.org/abs/quant-ph/9908066).
- The CSG post transformation and its fixed-point terrain are already
  published, making the tail-class delta the only plausible core of
  `DU-PAPER-013`:
  [causal-set post renormalization](https://arxiv.org/abs/gr-qc/0009063).
- Quantum Darwinism/SBS already supplies a strong objectivity absorber, so
  `DU-PAPER-006` and `022` need more than redundancy or a chosen decoder:
  [SBS and strong-QD review](https://arxiv.org/abs/2007.04276).
- A June 2026 paper already formulates proper-time history certification as a
  channel-separation problem. That is why `DU-PAPER-008` currently merges
  rather than seeds standalone:
  [Certifying Nonclassical Proper-Time Histories with a Quantum Clock](https://arxiv.org/abs/2606.12755).
- Information acquisition already has thermodynamic lower bounds, so
  `DU-PAPER-021` requires a matched residual not absorbed by ordinary
  accounting:
  [Thermodynamic Cost of Acquiring Information](https://arxiv.org/abs/1211.0506).

Every proposal selected for actual Factory production still needs a
claim-specific bibliography and novelty review.

## Confirmed Factory intake

The accepted source-to-seed mapping is:

```text
standalone:
    DU-PAPER-003 -> DU-SEED-COVARIANT-RECORD-COST
    DU-PAPER-007 -> DU-SEED-INTERVENTIONAL-RECORD-SUFFICIENCY
    DU-PAPER-009 -> DU-SEED-HIGHER-ORDER-PUBLIC-FINALITY
    DU-PAPER-013 -> DU-SEED-CSG-POST-TAIL-CLASSES
    DU-PAPER-015 -> DU-SEED-GLOBAL-CLOCK-GAUGE-WITNESS
    DU-PAPER-016 -> DU-SEED-NO-PRIVILEGED-DEPTH
    DU-PAPER-017 -> DU-SEED-FINITE-RECORD-OPENNESS

merge review:
    DU-PAPER-004 -> DU-SEED-BOUNDARY-RELOCATION
    DU-PAPER-024 -> DU-SEED-CONDITIONAL-FINALITY-DEVIATION
```

The Factory remains free to reprioritize, deduplicate, defer, merge, or decline
every seed. Dynamic Unity continues to own claim grades and source hardening.
All nine remain unselected or in merge review, with no hardening request or
production activation.

## Maintenance rule

Update the portfolio when:

- a new exact result acquires an identifiable contribution and audience;
- a candidate is seeded, merged, transferred, activated, or returned for
  hardening;
- a novelty collision changes standalone viability;
- a source swing changes manuscript distance materially; or
- a concept becomes a theorem target or loses its paper-shaped core.

Do not update it merely because another persona restates an existing idea.
