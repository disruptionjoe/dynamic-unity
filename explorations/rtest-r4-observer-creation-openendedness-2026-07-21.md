---
title: "R-test — R4 observer-creation / open-endedness: does a de-teleologized selection dynamics author open-ended new observer TYPES, or only replicate? (a foothold, not a crossing)"
status: active_research
doc_type: rtest
created: 2026-07-21
lane: "2.2 -> 1 (pre-registered swing: promote-or-kill the incentive-selection candidate's R4 leg)"
verdict: "PARTIAL / FOOTHOLD-BUT-REPLICATION-ONLY. The incentive-selection STRUCTURE earns a genuine R4 foothold — source-internal, self-parenting recombination ('observers authoring observers' from existing material, no external bit) that provably out-produces pure replication. But the DECISIVE bar fails as-modeled: every de-teleologized persistence rule tested (neutral, size-fragile, weak-selection, and a diversity-maximizing negative-frequency-dependent niche rule) SATURATES at a bounded set of observer TYPES — unbounded instances/length, finite types = the additive wall. Open-ended new TYPES appear ONLY under an external part-mint (the designer control), which fails R4 by importing an external bit. No designer is smuggled by the goal-free rule (teleology audit clean, with a working positive control). The pinpointed obstruction is NOT teleology — it is the FIXED FINITE PART-SET: no selection rule, goal-free OR teleological, produced open-ended new structural types from a fixed alphabet; only an external mint did."
grade: "R-test / pre-registered promote-or-kill; PARTIAL; no claim banked; claim_status_change: none; both calibration gates pass; foreground python probe + positive controls + teleology audit"
inputs:
  - explorations/incentive-selection-mode-issuance-candidate-2026-07-21.md   # the candidate; Test #2 (R4 observer-creation) + the R4 mapping
  - explorations/flip-witness-algebra-requirements-2026-07-21.md             # R4 spec: source-internal, self-generating, no external bit, no completed oracle
  - tests/du_observer_creation_openendedness_probe.py                        # the foreground probe (this test)
  - tests/artifacts/du_observer_creation_openendedness_probe_result.json     # the result artifact
---

# R-test — R4 observer-creation / open-endedness

**Pre-registered swing (Lane 2.2 -> Lane 1).** Test the R4 self-generation fork for the
incentive-selection candidate. R4 (from the requirements spec) demands growth that is
**source-INTERNAL, self-generating (Gödelian), with no external bit and no completed oracle.**
The candidate's strongest R4 form (from the candidate doc): the genuine novelty event **is
creating new OBSERVERS** — record-bearing subsystems authoring record-bearing subsystems =
autopoiesis / self-replication = the Gödelian shape.

**Decisive question (pre-registered).** Does a **de-teleologized** selection/persistence
dynamics (no intentional agents; formalized via constructor / assembly / open-endedness)
produce **OPEN-ENDED creation of genuinely-new observer TYPES**, or only **REPLICATION** (new
*instances* of a fixed observer type = the additive wall, still finite-type)? And does it avoid
**smuggling a designer** (no external bit / completed oracle)?

**Frontier honesty (stated up front, per the DU charter).** Open-ended evolution is an
**UNSOLVED frontier.** This swing does not try to solve it. It tests exactly one thing: whether
the incentive-selection *structure* gets a **foothold** on R4's source-internal / self-generation
requirements — not whether it crosses open-endedness. Both pre-registered outcomes are lethal to
over-claiming; the honest product is where the structure lands and *why*.

## The build (anti-toy) — a concrete self-reproduction / assembly model

`tests/du_observer_creation_openendedness_probe.py` (foreground; numpy; deterministic seeds;
3 replicates; result artifact `tests/artifacts/du_observer_creation_openendedness_probe_result.json`).

- **Observer** = a record-bearing subsystem == a finite **string over a FIXED finite primitive
  alphabet** (the parts, `|Σ|=4`). Its **TYPE** is its structure; its **assembly index** `a(x)`
  is the minimal number of construction steps to build it from primitives **with full reuse of
  already-built sub-assemblies** (Assembly Theory), computed by an LZ78 phrase-count proxy
  (repetition → low; genuinely novel structure → high; *labeled a proxy*).
- **Production (the candidate)** = a child is assembled from **substrings of two parents**
  (self-parent + other-parent, "gossip about gossip"). **No symbol ever enters that was not
  already present in the population** — the honest source-internal / no-external-bit condition.
- **Selection (the de-teleologized "incentive")** = reproduce ∝ `exp(β · S(x))`, where `S(x)` is
  a **local structural stability** (mean adjacent-part bond compatibility under a fixed drive)
  minus a size-fragility term. **No target string, no goal, no lookahead** — dissipative-
  adaptation-style differential *persistence*, not goal-pursuit. Population held at a carrying
  capacity `K` (a resource ledger, not a goal).

**Measure (assembly-index / novelty), cap-robust.** Observer size is capped (resource ledger),
so *present* complexity plateaus for any finite process; open-endedness must be read from
**continual discovery**. Primary signal = whether cumulative distinct **structural motifs** ever
produced **break PAST the finite internal-part ceiling** (`Σ_{j≤k} |Σ|^j`: 84 at k=3, 5460 at
k=6) and keep climbing. Crossing that ceiling is only possible with an **unbounded (external)
part source** — the honest necessary condition for open-ended new TYPES. Raw distinct-**string**
churn is reported but is **not** decisive: recombination always churns *instances* (new lengths)
even when structural type diversity is frozen — that is precisely the additive wall.

### The mandatory positive controls (both directions) — and one for the audit
- **(A) Pure replication** (copy the same observer): MUST register **saturating** type-diversity.
  If not, the novelty measure is miscalibrated and every downstream verdict is void.
- **(B) Designer-injected novelty** (an external oracle mints a never-seen primitive each step,
  kept via a sliding window): MUST register **open-ended** — cumulative structural discovery
  breaks past the internal ceiling and keeps growing. If not, the measure cannot detect
  open-endedness when present.
- **(E) Teleology-positive control** (selection rewards assembly index — a complexity *target*):
  the **teleology audit's own positive control** — the audit MUST detect that a goal changes the
  trajectory.

### Teleology audit (R4 fails by smuggling if it is dirty)
The candidate's `S(x)` takes only `(own structure, fixed drive)` — no goal argument, no future
state. Verified operationally: **goal-invariance** (identical configs are bit-identical; a goal
could only enter through an argument the function does not have) and **no lookahead**. The
gamma>0 teleology control is the detector's positive control.

## Results (from the artifact; both calibration gates PASS)

| regime | classification | cum-motif k3 | broke ceiling? | present-motif k3 | max a(x) | string-churn/gen |
|---|---|---|---|---|---|---|
| **A** pure replication *(control)* | REPLICATION_ONLY_saturated | 10.7 | **no** | 2 | 3.3 | 0 |
| **B** designer-injected *(control)* | **OPEN_ENDED_new_types** | **75 011** | **YES** | 2489 | 120 | 300 |
| **C** de-teleologized, neutral | REPLICATION_ONLY_saturated | 72.7 | no | 1.3 | 15 | 0.16 |
| **D** de-teleologized, size-fragile | REPLICATION_ONLY_saturated | 71.0 | no | 2 | 12.3 | 0.07 |
| **C2** de-teleologized, weak selection | REPLICATION_ONLY (instances≠types) | 79.3 | no | 41 | 31.7 | 285 |
| **C3** de-teleologized, freq-dependent diversity | REPLICATION_ONLY (instances≠types) | 80.0 | no | 76.7 | 7 | 27.6 |
| **E** teleology-positive *(audit control)* | REPLICATION_ONLY (instances≠types) | 76.7 | no | 64 | 48 | 297 |

- **Calibration PASSES both gates.** A saturates; B (external mint) breaks the ceiling to 75 011
  distinct motifs growing at 300/gen — genuinely unbounded. The measure discriminates.
- **All four de-teleologized variants SATURATE.** None breaks the finite internal-part ceiling
  (all `cum-motif k3 < 84`). The neutral and fragile rules **collapse** diversity to 1–2 present
  types (a fixation sweep to the most locally-stable motif). Weak-selection and the
  diversity-maximizing negative-frequency-dependent niche rule **maintain** diversity (present
  motifs 41 and 77) and **churn instances enormously** (285 and 28 new strings/gen) — but produce
  **no new TYPES**: the churn is new lengths of a bounded type-set = the **additive wall exactly**.
- **The teleology audit is clean.** `candidate_is_de_teleologized: true` (goal-invariant, no
  lookahead); the audit's positive control **fires** — injecting a complexity target moves
  mean `a(x)` from 9.2 → 38.3, so the audit provably *can* catch a smuggled goal.
- **Foothold is real.** Source-internal (no external symbol ever); recombination out-produces
  replication in structural exploration (`cum-motif k3` 72.7 vs 10.7). `r4_structural_foothold: true`.

### The decisive anti-artifact catch (Scientific Skeptic, load-bearing)
An earlier cut of the discriminator flagged C2/C3 "open-ended" off a positive late-window slope
in cumulative k=6 motifs. **That was a measurement artifact.** With a fixed 4-symbol alphabet the
cumulative distinct-motif count at any fixed scale is **bounded** (5460 at k=6); a positive slope
at gen 250 merely means the candidate is still *filling* that finite set — a finite-fill
transient, not open-endedness. The corrected discriminator keys on **breaking past the finite
ceiling** (only an unbounded/external source can), which no candidate does and the designer does
by four orders of magnitude. Being fooled by the finite-fill transient is exactly the "is
open-ended real or a measurement artifact?" failure the skeptic seat exists to catch; catching it
is what makes the REPLICATION-ONLY verdict trustworthy rather than an artifact of a lenient
threshold.

## The pinpointed obstruction — it is the FIXED FINITE PART-SET, not teleology

The sharpest, most transferable result is *which* thing blocks R4. It is **not** teleology-
smuggling per se: the teleology-positive control (E) — which openly rewards a complexity target —
**also fails to break the ceiling** (cum-motif k3 = 76.7). It merely fills the finite type-space
*deeper* (present motifs 64/64, max `a(x)` = 48). **A goal does not manufacture open-ended new
TYPES from a fixed alphabet either.** The one and only mechanism that broke the ceiling was the
**external part-mint** (B) — a source of genuinely new *parts*.

So the honest structural theorem the probe illustrates: **with a fixed finite part-set, structural
type-diversity at any bounded assembly scale is finite; open-ended new TYPES therefore require
either an external part-mint (an external bit / designer — fails R4) or unbounded assembly DEPTH,
and a goal-free local persistence rule sustains neither** (local stability sweeps to a
low-complexity attractor; even the diversity-maximizing niche rule only *populates* the finite
set). This is precisely the additive wall re-appearing at the observer level, and it locates R4's
real cost exactly: an R4-satisfying engine needs a **source-internal way to mint new PARTS**
(open the alphabet from within) — which is the unsolved autopoiesis/open-endedness core, not
something the incentive/persistence dynamics supplies on its own.

## Inline DU-board council (personas are lenses; computation disposes)

- **Constructor Theory.** A constructor must effect a transformation and remain able to repeat it;
  self-reproduction requires the *recipe* (the knowledge) instantiated in the substrate. Here the
  recombination operator is a legitimate constructor and it *does* repeat (foothold granted). But
  constructor theory also says **new tasks require new knowledge**; a fixed part-set + fixed
  bond-drive encodes a *fixed* knowledge, so no genuinely new constructible-task TYPE is authored.
  Reads: foothold yes, open-ended no. **Concurs with the verdict.**
- **Assembly Theory.** The Assembly `A = Σ e^{a_i}(n_i−1)/N` spikes in the fixation runs (many
  copies of a moderately-deep string) — but that is the AT *selection signature for high copy
  number of a fixed object*, i.e. **replication**, not novelty. AT's own discriminator (does the
  *assembly index of the discovered set* keep rising?) says no for every candidate; only the
  external mint raises it without bound. **Concurs**, and warns not to read a large `A` as
  open-endedness (it is the additive wall dressed up).
- **Open-endedness.** Textbook OEE result: fixed genotype-space + fixed fitness → convergence, not
  ongoing novelty. The probe reproduces this even under the strongest goal-free diversity engine
  (negative frequency dependence). Genuine OEE systems that *do* keep going (Tierra/Avida-like)
  smuggle in an effectively **open instruction/part-set** — which is exactly the external-mint
  lever here. **Concurs**; flags that "open the part-set from within" is the unsolved crux.
- **Model-theorist (internal generativity vs external satisfaction).** The candidate's type-set is
  the closure of a fixed alphabet under a fixed operator — an **internally-bounded** structure that
  a finite model *satisfies*, never one that internally *generates* beyond itself. Open-endedness
  needs internal generativity (a theory that proves its own extensions); the fixed part-set forbids
  it. Only the external oracle supplies "new elements from outside." **Concurs**, and names this the
  hosts-not-derives shape at the observer level.
- **Scientific Skeptic.** Owns the anti-artifact catch above (finite-fill transient ≠
  open-endedness). Also checks: is the fixation an artifact of β too high? No — the weak-selection
  and freq-dependent variants avoid fixation and *still* saturate. Is saturation a length-cap
  artifact? No — candidates saturate structurally well *below* the cap while the designer rides the
  cap yet stays open-ended (novelty is in the *parts*, not the length). Verdict is not an artifact.
- **Adversary-C (attack the strongest form).** Strongest pro-candidate case: "recombination of a
  fixed alphabet is Turing-universal in reachable strings, so new types *are* available." Rebuttal
  the probe forces: *available* ≠ *authored-and-persisting under a goal-free rule*. The reachable
  set being infinite in principle is defeated by the finite-scale ceiling being un-exceeded in
  practice under every de-teleologized rule; unbounded reachability is not unbounded *production*.
  The only escape Adversary-C finds is to open the alphabet — which is the external bit. **The kill
  survives Adversary-C**; the concession banked is the foothold, not open-endedness.

**Council synthesis (no divergence to preserve — the six lenses converge):** foothold granted,
open-ended new TYPES denied as-modeled, no designer smuggled by the goal-free rule, obstruction =
the fixed finite part-set.

## Grade, boundary, and what would flip it

**Grade: PARTIAL / FOOTHOLD-BUT-REPLICATION-ONLY.** Against the pre-registered outcomes:
REPLICATION-ONLY is the dominant reading (the de-teleologized persistence dynamics gives the
**additive wall at the observer level** — new instances, finite types); it is *not* TELEOLOGY-
SMUGGLED (the audit is clean, and teleology doesn't even help); and it earns a genuine, honestly-
bounded **FOOTHOLD** on the source-internal / self-generation *scaffold* (the reason it is PARTIAL
and not a flat kill). Open-endedness remains the hard, unsolved frontier — this swing shows the
incentive-selection structure does not cross it, while cleanly getting a foothold underneath it.

**The buildable witness that would flip R4 to a real crossing (the named next object):** a
**source-internal part-mint** — a mechanism by which the existing configuration *authors new
primitive parts* (opens its own alphabet) without an external oracle, so cumulative structural
discovery breaks the finite ceiling from the inside. That is exactly autopoiesis in the strong
sense (observers whose activity enlarges the very type-space of observers), and it is the unsolved
core. Absent it, "observers authoring observers" is **replication**, and R4's Gödelian
self-generation is not met by the incentive/persistence dynamics alone. This sharpens the
candidate's own R4 open-fork ("open-ended vs replication — the same additive wall at the observer
level") to a precise obstruction and a precise buildable target.

**Feedback to the candidate (Lane 2.2 → 1).** The R4 leg does **not** promote to Lane 1 as an
open-ended engine on this test; it promotes a **narrower, honest** object: *recombination-on-
selected-growth is a validated source-internal replicator* (consistent with the candidate's R3/R5
fit and the CSG "each birth ingests the past" host), whose R4 **open-endedness** is now reduced to
one crisp missing piece — the source-internal part-mint. Pair this with Test #1 (R2/W1 relational
new-types-vs-instances): the two share one obstruction (finite type-set closed under a fixed
operator), so a single "self-authored new-parts" mechanism would answer both, and its absence
kills both as open-ended. That is the highest-value place to point the next swing.

## Boundary

R-test / pre-registered promote-or-kill; PARTIAL; **no claim banked, `claim_status_change: none`**.
Finite-window assembly SIGNATURE, not a decision procedure for open-endedness (undecidable in
general); the assembly index is a labeled LZ78 proxy. Foreground python probe with both mandatory
positive controls and a teleology audit (with its own positive control); both calibration gates
pass. Cross-repo lenses (constructor / assembly / open-endedness; model-theoretic hosts-not-derives)
used as terrain and re-verified here per CONNECTIONS.md — none imported as a grade.
