---
title: "Covariant collapse via finality-on-causal-order — does the wavefunction 'update' become a frame-independent finality fact typed on J⁺ inside the algebraic-QFT covariant-measurement framework, or does it secretly smuggle a foliation? (constructive build)"
status: active_research
doc_type: exploration
created: 2026-07-21
lane: "1 (targeted hypothesis pursuit) / measurement × relativity — the CONSTRUCTIVE build; a sibling runs the adversarial kill + the deviation question in parallel"
verdict: "PARTIAL, split by horn. The COVARIANCE horn — the genuinely open 'preferred simultaneity' part of the problem — DISSOLVES AT RELOCATION GRADE ON A FINITE CAUSAL-ORDER TOY (not a net-level theorem): finality typed on the causal future J⁺ is boost-invariant to machine precision (computed, not asserted), the EPR 'which collapsed first?' question is MALFORMED (the wings are incomparable in the causal order in every frame), and NO foliation is smuggled (J⁺ is the invariant light-cone, not a simultaneity surface) — an explanatory upgrade over Shimony's peaceful coexistence. The SORKIN-ADMISSIBILITY horn is SUPPLIED at the correct TYPE and is CONSILIENT with Fewster–Verch: a foliation-typed (Lüders-on-a-slice) update fabricates spacelike co-collapse links and signals superluminally (~1 bit in the toy) — Sorkin's impossible measurement — while a causal-order-typed (finality) update forbids them and leaks exactly 0 bits. But this is CHARACTERIZATION/CONSILIENCE grade, not a DERIVATION of the covariant-measurement scheme inside the net of local algebras (that AQFT-net embedding is UNBUILT). Single-outcome and Born are inherited OPEN from Bet #1. Does it smuggle a foliation? NO. Is it a rigorous theorem inside AQFT? NOT YET."
grade: "reconstruction/structural + one foreground probe (4 modules, all PASS, exit 0). Covariance horn: DISSOLVES (relocation grade; finite boost-invariance computation, AQFT-net derivation unbuilt) for frame-independence-of-the-update (the specific open sub-problem), relocation grade as an interpretation overall. Sorkin horn: strong PARTIAL (correct type, consilient with Fewster–Verch, not a net-level derivation). All cross-repo material re-verified per CONNECTIONS.md; no grade imported. Not banked (no Lane-3 clearance). claim_status_change: none."
probe: "tests/du_covariant_finality_collapse_probe.py (+ tests/artifacts/du_covariant_finality_collapse_probe_result.json) — 4 modules, foreground, exit 0, ALL PASS. Positive control included (foliation ordering flips; causal order invariant)."
directed_by: "Joe direct chat via coordinator, 2026-07-21 (pre-registered Lane-1 constructive swing, measurement × relativity: build+test the finality-on-causal-order account of covariant collapse against the AQFT covariant-measurement terrain — Fewster–Verch, Sorkin's impossible measurements — with a Bell-pair-on-a-causal-set probe carrying a discriminating positive control; grade honestly; DO NOT commit/push)."
inputs:
  - dynamic-unity/explorations/bet1-measurement-via-records-finality-2026-07-21.md
  - dynamic-unity/explorations/measurement-and-double-slit-records-account-2026-07-21.md
  - dynamic-unity/explorations/flip-witness-algebra-requirements-2026-07-21.md
  - temporal-issuance/DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md   # H¹ global section; μ; no-preferred-foliation bridge
  - time-as-finality/FORMALISM.md                              # causal order primitive; T21 CHSH; T16 gluing; T2 measurement
self_check: >-
  Per DU's sovereign self-verification duty (CONNECTIONS.md): TaF's causal-order-primitive
  formalism (metric time / global clock / universal present / total order over spacelike events
  explicitly NOT primitive; result invariant under choice of topological ordering; spacelike
  records incomparable), TI's H¹-global-section-of-finalized-bindings and the "observers take
  different local slices, NOT a preferred foliation" bridge, and the Fewster–Verch / Sorkin
  terrain are all CONSUMED as hypotheses re-verified here, not adopted on any sibling's (or the
  literature's) say-so. The frame-independence, the no-signaling marginal, the global-section
  correlation, and the Sorkin discriminator are DU's own computed reads (foreground probe, exit
  0). Nothing is banked; the build carries the adversaries (Relativity Hardliner, block-universe,
  Sorkin-signaling) as kills to beat, and reports where it stops (net-level AQFT embedding unbuilt;
  single-outcome/Born open).
---

# Covariant collapse via finality-on-causal-order — the constructive build

## The one real problem, stated precisely

How is the "instantaneous" update of the wavefunction compatible with the light-cone limit?
**No-signaling is already safe** (no-communication theorem) — that is *not* the open part. The
genuinely open part is that a *physical* collapse seems to need a **preferred simultaneity**: in
EPR, boosted frames disagree on which wing's measurement "caused" the update and in what order — a
non-covariant **"when."** Shimony's **"peaceful coexistence"** asserts that no-signaling and the
update can cohabit, but it is **descriptive, not explanatory**: it says *that* they do not conflict,
not *why* there is no non-covariant fact to reconcile.

**The build under test.** The update is **not a process propagating through space.** It is the
**fixing of a finality fact typed on the causal (light-cone) partial order J⁺, not on a simultaneity
surface.** Special relativity's invariant structure *is* the causal partial order `<_c`; a foliation
is the frame-dependent add-on. So the thesis is: if **"final" ≡ "fixed relative to its own causal
future J⁺,"** then

1. finality is **frame-independent by construction** (J⁺ is Lorentz-invariant);
2. the EPR **"which collapsed first?"** is **malformed** (the two wings are *incomparable* in `<_c`);
3. the correlation is a **joint property of ONE finalized record** — TI's **H¹ global section**
   over the causal set — **not** something built by propagation.

The question this document must answer honestly: **does this hold rigorously inside the algebraic-QFT
covariant-measurement framework, or does it secretly smuggle a foliation?**

---

## Ingest + re-verify (cross-repo, per CONNECTIONS.md — consumed as hypotheses, not granted)

**TaF `FORMALISM.md` — the causal order is the primitive, the foliation is not.** Re-verified: the
primitive inventory is a finite set of causal events with a **strict causal partial order `<_c`**;
explicitly **NOT primitive** are "metric time, a global clock, a universal present, **a total order
over spacelike events**, experienced temporal order." The binding discipline: *"the executable model
may use a topological ordering to evaluate the graph, but its result must be **invariant under the
choice of topological ordering**."* The Reconstruction Rule states spacelike-separated stabilized
records **remain incomparable** until a causal reconciliation. **This is exactly the object the build
needs** — finality defined on `<_c`, provably foliation-free — and it is TaF's own construction, not
an import I am inventing. (T21 supplies the CHSH/global-section obstruction; T16 the gluing of local
finality domains to a global partial order or an obstruction witness; T2 the qubit measurement-
finality model.) **Self-check verdict: the ingredient is real and re-verified; I do not import its
grade — I re-derive its covariance below in DU's own probe.**

**TI `DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md` — H¹ global section + the explicit no-foliation
bridge.** Re-verified: shared reality is *"the global section glued from observers' local finalized
bindings, existing iff a gluing obstruction (Čech H¹ of the finality sheaf) vanishes."* And the
relativity bridge is stated in the source verbatim: *"it does **not** mean synchronized by a shared
coordinate clock, preferred foliation, or absolute simultaneity … observers may disagree about
coordinate time because they take different local slices through the shared issuance-consistency
structure."* **Self-check verdict: TI already commits to no-preferred-foliation and to the H¹-section
reading of correlation. That is the thesis's home. But TI states it as *framing discipline*, not a
theorem — so the burden here is to make the covariance *computed*, and that is Module (a).**

**Bet #1 (`bet1-measurement-via-records-finality`) — the scope fence I must respect.** Re-verified:
the records/finality account **reframes** pointer-basis and tensor-split at relocation grade,
**FAILs** the non-circular Born kill, and leaves **single-outcome** as right-type-PARTIAL (absorbed by
block-universe + D-FORK/FTS-disclosure). **Self-check verdict: this build must NOT re-open Born or
single-outcome — those are Bet #1's OPEN results and are inherited, not re-litigated. This build's
question is disjoint: the *covariance of the update*, which Bet #1 did not address.** Keeping them
disjoint is the honest move; conflating them would inflate.

---

## The rigorous terrain (engaged, not reinvented)

**Fewster–Verch covariant measurement in AQFT.** A measurement scheme couples the system QFT to a
**probe** QFT via a **compactly-supported** interaction in a bounded spacetime region `O`. The induced
system observable is localized in the **causal hull** of `O`, and the state-update (instrument) obeys
**causal factorization**: the *non-selective* update (averaged over outcomes) leaves the state's
restriction to algebras in the **causal complement and the causal past** of `O` **invariant** — hence
**no superluminal signaling** is a theorem, with *no preferred foliation* anywhere in the construction.
Crucially, the FV update is typed on the **causal relationships of `O`** (its causal hull / future),
not on a Cauchy slice. **This is precisely a "finality fact typed on J⁺" in operator-algebra clothing.**
The map is: DU's *non-selective* finalization ↔ FV's non-selective instrument (Module b); DU's
*selective* finalization conditioned on the outcome ↔ FV's selective instrument, which alters the
spacelike-separated *conditional* state (= the correlation, Module c) but is invisible locally
(no-signaling).

**Sorkin, "Impossible measurements on quantum fields" (1993).** A naïve **ideal (Lüders) projective
measurement** of a local observable in QFT, applied as an **instantaneous update across a Cauchy
slice**, is a **nonlocal channel** and **can signal superluminally**; the pathology is removed only by
**restricting** the admissible operations to the causally-localized (probe-coupled) ones — exactly the
FV class. **The Sorkin pathology *is* the foliation creeping in through the slice-instantaneous
Lüders update.** So the decisive test of the thesis is sharp: *does finality-on-causal-order naturally
supply exactly Sorkin's admissible restriction?* If yes, the account is not decoration — it is the
principle whose content is the FV/Sorkin admissibility class. Module (d) tests exactly this.

**Comparison points (placed, honestly).**
- **Consistent / decoherent histories (Gell-Mann–Hartle):** Lorentz-friendly *by construction*
  because histories are defined on spacetime regions and the decoherence functional is covariant.
  The finality account is a **near-cousin**: a finalized record *is* a decoherent history that has
  become irreversible (redundancy/reversal-cost typed). It **inherits CH's covariance virtue** and
  shares a cousin of CH's **many-incompatible-frameworks** problem — which is precisely the **H¹
  gluing obstruction** (no canonical global section of frameworks). Honest parity, plus DU's
  irreversibility typing as the delta.
- **Relational QM / QBism (the subjective-update alternative):** dissolves the preferred-simultaneity
  problem by making the update **observer-relative / subjective** — no objective "when" because no
  objective update. The finality account is the **objective-but-covariant** third option: the update
  is a **real external fact** (finality is redundancy-conferred and *"external, not self-certified"* —
  TI's Gödel discipline), yet **typed on the invariant causal order**, so it is covariant *without*
  going subjective. This is a genuine and statable placement: objective like collapse, covariant like
  RQM, without RQM's subjectivity.

**Consilience to watch (flagged, NOT banked — coincidence grade, like W157).** Sorkin appears three
times in the program: **causal sets** (the Λ~1/√N DE amplitude), **impossible measurements** (this
problem), and **discrete spacetime**. The causal-order-finality account lives **natively in the
causal-set framework** — a finite causal partial order with no foliation, which is *the same object*
TaF's FORMALISM uses and *the same object* underlying the DE amplitude. That the foliation-removing
object here is the causal set, and the DE-amplitude object is also a Sorkin causal set, is a **real
structural consilience** — recorded as coincidence-grade to watch, not evidence.

---

## The board, inline (DU Dynamic-Physics seats — lenses, not evidence)

Seats run **inline in one worker**: **Quantum Foundations**, a **Relativity Hardliner** (the sharpest
internal check — hunt any hidden universal tick / foliation), a **Philosopher of Time** (keep
"finality" from equivocating with "simultaneity"), an **algebraic-QFT / operator-algebra** lens
(Haag–Kastler net), an **Order/Domain theorist** (finality as a closure/fixed-point on a partial
order), and a **Model-theorist** (internal vs external, definability).

**Order/Domain theorist.** Finality is a **closure operator** `cl` on the poset of record-states
(idempotent, monotone, extensive — Bet #1 Leg 1). Type it on the causal order: a record at event `e`
is *final* when `cl` has fixed it **relative to `J⁺(e)`** — its own causal future. `J⁺(e)` is a
**down/up-set in `<_c`**, an order-theoretic object, **not** an antichain-slice picked by a frame.
"Final relative to J⁺" is therefore a statement in the language of the partial order alone. That is
the whole move, and it is well-typed.

**Philosopher of Time (the equivocation guard — load-bearing).** The entire thesis rides on **`J⁺(e)`
≠ a simultaneity surface.** `J⁺(e)` is the **forward light cone**, a Lorentz-**invariant** set; a
foliation is a choice of **spacelike Cauchy surfaces**, a Lorentz-**variant** add-on. "Finality" must
mean *fixed-relative-to-causal-future* and must **never** slide to *fixed-as-of-now*. If it slides,
the account smuggles a foliation and dies. **The guard is discharged only if a computation shows the
finality assignment is invariant under boosts while a genuine foliation assignment is not.** That is
Module (a)'s positive control — and it is the reason a positive control is mandatory, not optional.

**Relativity Hardliner (pressing for the hidden tick).** I grant `J⁺` is invariant. My bite is
elsewhere: does the *correlation* story need a "when the joint record forms"? If the account says the
singlet becomes-one-record "at" some event, and that event is on a slice, the tick re-enters. **Answer
(Module c):** the joint record is finalized at a **causal-set event `C` in `J⁺(A) ∩ J⁺(B)`** — the
common causal future — which is again an invariant intersection of light cones, **not** a slice. And
there is **no `A→B` edge** (they are incomparable), so nothing forms "across" them. My second bite is
the real one and I press it in Module (d): an *ideal* measurement in an extended region *does* act
across a slice — is your account just renaming the FV restriction, or does it supply it? (Held to the
Module-d result below.)

**algebraic-QFT / operator-algebra lens (Haag–Kastler).** In the net `O ↦ A(O)`, "finality typed on
J⁺" should read: the finalization channel associated to a region `O` acts as the identity on
`A(O')` for the **causal complement** `O'` (Einstein locality / microcausality: `[A(O), A(O')]=0`),
and its selective form alters only conditional expectations reachable in `J⁺(O)`. **That matches, at
the level of type, the FV causal-factorization property (a type-match, not a verbatim derivation).** So *at the level of type*, the finality principle and the FV
admissibility condition are the **same statement**. What I do **not** yet have is the finality closure
`cl` **constructed on the net** with FV causal factorization **proven** from it — that is a genuine
theorem, and it is **unbuilt**. So I can certify **type-match and consilience**, not a net-level
derivation. That ceiling must be in the grade.

**Model-theorist (internal vs external, definability).** "Final relative to J⁺(e)" is **definable in
the causal-order structure** `(E, <_c)` **without** a global "now" parameter — good, it is an internal
predicate. The residue: selecting a **single outcome** (not merely the correlation structure) needs
the finalization to fix a *value*, and Bet #1 already graded that right-type-PARTIAL / absorbed. So
this build is honestly scoped to the **covariance of the update**, and must **not** claim single-
outcome. Definability of the covariance predicate: **yes**. Definability of single-outcome selection:
**out of scope, inherited open.**

**Quantum Foundations (synthesis).** The board converges: the covariance horn is **clean and the
right type** provided a computation discharges the Philosopher's guard; the Sorkin horn is **the
decisive test** and turns on whether the causal-order typing forbids exactly the slice-fabricated
links; single-outcome/Born stay out of scope. Run the probe.

---

## The probe (anti-toy; foreground; exit 0; positive control included)

`tests/du_covariant_finality_collapse_probe.py` → `tests/artifacts/du_covariant_finality_collapse_probe_result.json`.
Four modules; **all PASS; exit 0.** An EPR/Bell pair as events on a small (1+1) Minkowski causal set;
the real singlet for the quantum content.

### (a) Frame-independence — with a discriminating positive control → PASS

Events: source `P` (common past), wings `A`, `B` (**spacelike**), comparison `C` (common future),
with the intended structure verified: `P<A, P<B, P<C, A<C, B<C, A∥B`. Boosting through **41
rapidities in [−3, 3]**:

| Quantity | Result |
|---|---|
| Causal-order incidence matrix, max deviation across all boosts | **0** (machine-exact invariant) |
| `A∥B` (incomparable) in **every** frame | **True** |
| Foliation "which-collapsed-first" sign `sign(t'_A − t'_B)` | **{−1, 0, +1}** — flips with the boost |

**Reading.** The **causal-order (finality) data is identical in every boost**; the **naïve foliation
collapse-order of the spacelike wings flips sign** (each wing "collapses first" in some frame). The
positive control therefore **discriminates**: same input, the foliation account is frame-dependent,
the causal-order account is not. The EPR **"which collapsed first?" is malformed** — `A, B` are
incomparable in `<_c` in *every* frame. **The Philosopher of Time's guard is discharged by
computation, not assertion.**

### (b) No-signaling — the local marginal is immune to the far setting → PASS

Real singlet, spin settings `σ(θ)=cosθ·Z+sinθ·X`, scanning both wings over a 24×24 grid:
`max |P(a | θ_a, θ_b) − ½| = 2.2×10⁻¹⁶`. The **local marginal cannot be moved** from the spacelike
wing — the **FV non-selective / causal-factorization invariance**, computed.

### (c) Correlation from the global section, no propagation → PASS

| Quantity | Result |
|---|---|
| `max |E(θ_a,θ_b) − (−cos(θ_a−θ_b))|` over a 19×19 grid | **3.3×10⁻¹⁶** (exact readout of the one state) |
| CHSH `S` at optimal angles | **−2.828427 = −2√2** (Tsirelson) |
| Global section of **local hidden values** | **does not exist** (`|S|>2` — Bell obstruction, H¹≠0) |
| `A→B` causal edge | **absent** (no propagation path exists) |

**Reading.** The full correlation is reproduced as an expectation in the **one state prepared at `P`
and read jointly at `C`** — with **no `A→B` edge** to carry it. The CHSH violation makes the structural
point sharp: there is **no global section of *local hidden values*** (the Bell/CHSH obstruction — TaF
T21, an H¹≠0 for the value-assignment sheaf), **yet the finalized *joint-record* section at `C` is a
single well-defined object.** These are **two different sheaves**: the account denies a global section
of the first and asserts one for the second. That distinction is the honest content of "one finalized
record" — it is **not** a hidden-variable global value assignment.

### (d) Sorkin admissibility — the decisive test → PASS

Sorkin three-region toy. Alice `A`; the **extended** measurement region modeled by its **two spacelike
ends** `b1, b2`; Charlie `C`. Geometry verified: `A<b1, b2<C, A∥C, b1∥b2, A∥b2, b1∥C` — so the **only**
causal routes are `A→b1` and `b2→C`; an `A→C` signal **requires linking the spacelike pair `b1,b2`.**
Qubit channel (`A`→`b1` CNOT legitimate; optional `b1`→`b2` "bridge"; `b2`→`C` CNOT legitimate):

| Update rule | `P(C=1|a=0)` | `P(C=1|a=1)` | `I(A:C)` | Signals? |
|---|---|---|---|---|
| **Foliation** (Lüders-on-a-slice: fabricates the `b1~b2` co-collapse) | 0 | 1 | **1.000 bit** | **YES — Sorkin's impossible measurement** |
| **Causal-order (finality)** (`b1∥b2` incomparable ⇒ link forbidden) | 0 | 0 | **0.0 bits** | **NO** |

**Reading.** The **foliation update fabricates the `b1~b2` co-collapse** (it treats a whole slice
through the region as jointly fixed) and **leaks ~1 bit `A→C` across spacelike separation** — exactly
Sorkin's impossible measurement. The **causal-order (finality) update forbids the `b1–b2` link**
(they are incomparable in `<_c`, so their *joint* co-fixing is **not "final"**) and **leaks 0 bits.**
**Finality-on-causal-order supplies exactly the Sorkin/Fewster–Verch admissible restriction** — the
admissible (non-signaling) update *is* the causal-order-typed one; the impossible (signaling) update
*is* the foliation-typed one.

**Honest scope of (d).** This is a **faithful schematic** of the Sorkin mechanism at qubit level. The
modeling choice — *"ideal measurement of the extended-region observable ≡ a `b1~b2` co-collapse
link"* — is **motivated by the mechanism** (a slice-instantaneous Lüders update treats the region's
spacelike ends as co-fixed), **not derived from the CCR net**. What it demonstrates, at qubit-schematic grade (not a net-level derivation), is the
**structure**: a foliation-typed update fabricates spacelike links and signals; a causal-order-typed
update forbids them and does not — which is precisely the content of the FV/Sorkin admissibility
theorem. It is **not** a re-proof of FV inside the net.

---

## Verdict — honest, per horn

**Does finality-on-causal-order give a covariant collapse? Split by horn.**

### Horn 1 — Covariance / no preferred simultaneity: **DISSOLVES (at relocation grade, finite toy)** (for the open sub-problem; AQFT-net derivation unbuilt)

The genuinely open part of "the one real problem" was the **preferred-simultaneity / non-covariant
'when.'** On that part the account **dissolves the problem, and now with a computation, not a slogan**:

- finality typed on `J⁺` is **boost-invariant to machine precision** (Module a: incidence deviation 0
  across 41 boosts) while a genuine foliation ordering **provably flips** (positive control: signs
  {−1,0,+1});
- the EPR **"which collapsed first?" is malformed** — the wings are **incomparable in `<_c` in every
  frame**;
- **no foliation is smuggled**: `J⁺(e)` and `J⁺(A)∩J⁺(B)` are invariant light-cone objects, not slices
  — the Philosopher of Time's equivocation guard is **discharged by Module (a)**.

This is a **genuine explanatory upgrade over Shimony's peaceful coexistence**: peaceful coexistence
says *there is no conflict, don't ask how*; this says **there is no non-covariant fact to reconcile
because the update was never typed on a "when" — it is typed on the invariant causal order, and the
"when" question is ill-posed.** As an interpretation it remains **relocation grade** (block-universe-
compatible, predicts identically to QM — consistent with Bet #1 and the double-slit account), but the
covariance is no longer *conceptual*; it is *shown*.

### Horn 2 — Sorkin admissibility inside AQFT: **strong PARTIAL** (correct type, consilient, not a net derivation)

Finality-on-causal-order **supplies the correct-TYPE restriction** and **forbids exactly the impossible
(slice-typed) measurements** (Module d: 1 bit → 0 bits), and this **matches the Fewster–Verch
admissibility class** at the level of type/causal factorization (a type-match, not a verbatim derivation; the AQFT lens confirmed the
type-identity). **But**: (i) the demonstration is a **qubit schematic**, not the CCR net; (ii) the
finality **closure has not been constructed on the Haag–Kastler net with FV causal factorization
*proven* from it** — that theorem is **UNBUILT**; (iii) the account **characterizes** the admissible
class, it does not **derive** the FV compact-support probe scheme (FV get their restriction from a
dynamical mechanism; finality states it as a principle). So: **supplies Sorkin's restriction at
characterization / consilience grade — consilient with FV, not yet a rigorous theorem inside the net.**

### Does it secretly smuggle a foliation? **NO.** Is it rigorous inside AQFT? **NOT YET.**

The exact mechanism (positive): **the causal future `J⁺` is Lorentz-invariant, so a fact "final
relative to `J⁺`" carries no frame-dependent 'when'; the correlation is the content of a single
finalized section over the common causal future `J⁺(A)∩J⁺(B)`, with no spacelike edge to propagate
along; and typing updates on `<_c` rather than on a slice is exactly what removes Sorkin's pathology.**
The exact obstruction (honest): **the account currently lives at the level of the causal *set / order*
and a qubit schematic; the lift to the *net of local algebras* — construct `cl` on `A(O)` and prove FV
causal factorization from "final ≡ fixed on `J⁺`" — is the missing rigorous step**, and single-outcome
+ Born remain **open (inherited from Bet #1)**.

### Grade

**PARTIAL.** Covariance horn **DISSOLVES (relocation grade; finite boost-invariance computation, AQFT-net derivation unbuilt)** for the frame-independence-of-the-update
sub-problem (computed, positive-control-discriminated, no foliation smuggled — an explanatory upgrade
over peaceful coexistence, relocation grade as an interpretation). Sorkin horn **strong PARTIAL**
(supplies the admissible restriction at the correct type, consilient with Fewster–Verch, not a
net-level derivation; the AQFT-net embedding is unbuilt). Single-outcome / Born **OPEN** (Bet #1).
Not a clean global DISSOLVES — that would require the net-level FV theorem — but decisively more than
"peaceful coexistence," and **it does not smuggle a foliation.**

**Highest-value buildable next step** (the one that would move Horn 2 to DISSOLVES): construct the
finality closure `cl` **on a Haag–Kastler net** for a free-field toy and **prove** that "final ≡ fixed
on `J⁺`" **implies** Fewster–Verch causal factorization (identity on the causal complement) — i.e.
derive the admissibility class from the finality typing rather than matching it. If that theorem
lands, the Sorkin horn upgrades from consilience to derivation and the whole account becomes rigorous
*inside* AQFT, not merely consilient with it.

---

## Adversaries (carried as terrain, per LANES.yaml)

- **Relativity Hardliner** — pressed for a hidden tick/foliation; **beaten on covariance** (Module a:
  invariant; `J⁺` is the light cone, not a slice), and his sharper Sorkin bite is **answered at type
  grade** (Module d) but **not at net grade** (he keeps the win that the net-level theorem is unbuilt).
- **Block-universe absorber** — the account is **absorbed** as an interpretation (relocation grade,
  block-compatible), exactly as in Bet #1; the covariance result survives *because* it is a structural
  claim about `<_c`, which the absorber does not touch. No becoming is claimed here.
- **Sorkin-signaling** — **beaten in the toy** (the causal-order update leaks 0 bits where the
  foliation update leaks 1), which is the positive content; the residue is the net-level lift.

## Boundary

Exploration/constructive-build tier (Lane 1, measurement × relativity). **Two NEW files**: this
document + `tests/du_covariant_finality_collapse_probe.py` (with artifact
`tests/artifacts/du_covariant_finality_collapse_probe_result.json`); the probe ran **foreground,
exit 0, all 4 modules PASS**, positive control included. All cross-repo material (TaF causal-order
formalism + T21/T16/T2, TI H¹-section + no-foliation bridge + μ, the Fewster–Verch / Sorkin terrain)
is **consumed as hypotheses re-verified here, not adopted on any sibling's or the literature's
say-so** (CONNECTIONS.md sovereign self-check). **Nothing is banked**; the per-horn grades are the
product (Horn 1 DISSOLVES at relocation grade (finite toy) for the covariance sub-problem, Horn 2 strong PARTIAL, single-
outcome/Born inherited OPEN). Personas ran **inline** (DU board), lenses not evidence. No edit to
LANES.yaml, README, AGENTS.md, CONNECTIONS.md, or any GU/TaF/TI/P2C file. `claim_status_change: none`;
`canon_verdict_change: none`; `public_posture_change: none`. **No commit, no push** (per the directing
instruction). Joe alone publishes; nothing routes externally.
