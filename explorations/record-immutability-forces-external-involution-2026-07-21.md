---
title: "Record-immutability forces the becoming-involution EXTERNAL? — proof-or-refute of source-is-observer as a THEOREM. VERDICT: CONDITIONAL-THEOREM. The LITERAL bridge ('record-immutability ⇒ monotone accretion ⇒ no internal fixpoint-free involution') is REFUTED — an immutable append-only ledger of flip-events carries a DERIVED orientation whose induced map on {+,−} is a genuine fixpoint-free involution, realized without deleting any record. BUT source-is-observer survives as a theorem under the corrected standard: genuine becoming requires FIRST-PERSON UNDERIVABILITY, every internally-derived orientation is a function of the records hence third-person computable = DISCLOSED (even the parity involution — a Kleene readout/quine), and underivable ⇒ external. The real necessity runs through DERIVABILITY, not fixpoint-freeness. σ = w₁(L_time) is the unique fixpoint-free, Gödel-independent, external involution ⇒ σ's externality is NECESSARY, not accidental. Condition = the fixed-rule-first-person caveat the trunk synthesis already flagged open."
status: active_research
doc_type: exploration
created: 2026-07-21
lane: "1 (North-Star TRUNK / foundations) — turn the trunk's deepest result (self-authoring-dirac-synthesis: a monotone self-authoring loop is a Kleene quine; the becoming-diagonal fires only via a fixpoint-free involution L2, and DU's only one is the external σ) into a theorem — or refute it"
verdict: "CONDITIONAL-THEOREM. Proof-or-refute of: record-immutability ⇒ the L2 becoming-involution is external (source-is-observer). The literal monotonicity bridge is REFUTED (Adversary-C's parity-of-flips: a source-internal fixpoint-free involution DOES exist in a genuine immutable record dynamics — it acts on a derived orientation, not on the records, so immutability is not violated). But the INTENDED thesis (the becoming-L2 is external by necessity) is a THEOREM under the corrected standard that genuine becoming = first-person underivability: every internally-derived orientation is third-person computable (DISCLOSED — the parity involution included), the record-arrow's own orientation is the trivial/orientable class (a torsor, fixpoint-ful), and 'internal-derived AND underivable' is an empty cell. Underivable ⇒ external. σ's externality is NECESSARY, not accidental. The named condition is exactly the trunk's open fixed-rule caveat."
grade: "proof-or-refute at reconstruction/structural grade, argued from the objects' own construction (Bourbaki-Witt/Kleene inflationary fixpoint; Lawvere point-surjection vs a derived-orientation involution; Z/2 line-bundle w₁ over the record cycle) and re-verified per CONNECTIONS.md against the observer +9 addendum L1/L2, three-seam Prong A (σ=w₁(L_time)), oracle-relative Prong III (no_invariant_valuation, Lean-proved), the D-FORK oracle disjunction; no cross-repo grade imported; not banked (no Lane-3 clearance); claim_status_change: none; Krein sign σ untouched (R7)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
probe: tests/du_record_immutability_external_involution_probe.py (foreground; exit 0; positive controls fire — a real internal fixpoint-free involution, a disclosed-vs-underivable separator at acc 1.0 vs ~0.5, an orientable record cycle vs a fixpoint-free Möbius, an empty forbidden cell). Artifact: tests/artifacts/du_record_immutability_external_involution_probe_result.json
ingested_and_reverified:
  - "dynamic-unity self-authoring-dirac-synthesis-2026-07-21.md (the trunk finding: monotone self-authoring loop = Kleene quine; L2 fires the becoming-diagonal; DU's only L2 is the external σ)"
  - "dynamic-unity self-authoring-dirac-adversarial-kill-2026-07-21.md (the Kleene/L2 kill: L1 without L2; §7 the named external-J CONDITIONAL)"
  - "dynamic-unity spectral-flow-source-synthesis-2026-07-21.md (the becoming-witness reframe: first-person underivability, NOT a third-person Gödel sentence)"
  - "dynamic-unity flip-witness-algebra-requirements-2026-07-21.md (R4 source-internal / no external bit; R7 σ stays external)"
  - "dynamic-unity d-fork-regime-resolution-2026-07-21.md (DU's source is a fixed computable-law object on the FTS side; the oracle disjunction — both horns external)"
  - "dynamic-unity bet2-low-entropy-origin-bottom-of-roll-2026-07-21.md (Bet #2: finality = irrevocable accretion = immutability = records don't un-happen; the accretion count is monotone and bottoms out)"
  - "gu-formalization CONJECTURE-source-action-is-the-observer +9 addendum (2026-07-20): L1 self-encoding AND L2 fixpoint-free involution; 'the inside-ness forces the outside-ness of the bit'"
  - "gu-formalization three-seam-prongA-class-relative-frame-2026-07-21.md (A-NUMEROLOGY: σ=w₁(L_time) canonical/forced/external; the record-derived shard-cycle orientation is the TRIVIAL class / a torsor; the flip-band is imported, realization-dependent, a self-inserted external coin)"
  - "gu-formalization oracle-relative-prongIII-exhaustiveness-theorem-2026-07-21.md ('the observer forces externality but cannot supply σ's value' IS A THEOREM at operator/Lean grade — the involution leg / no_invariant_valuation, needs ONLY fixpoint-free α, never depended on L1; the α-parity eigenspace decomposition is complete)"
note: "Cross-repo material ingested freely and re-verified with DU's own apparatus; grades consumed, not moved. DO NOT commit/push (per task). Personas run inline (DU board), lenses not evidence. Adversary-C carried inline, attacking the strongest internal-involution counterexample; per charter a clean refute of a sub-claim is an honest finding, adversaries are terrain, sovereign self-verification. Positive controls required and present (probe exit 0)."
---

# Record-immutability forces the becoming-involution external? — a proof-or-refute

## 0. Verdict up front

> **`CONDITIONAL-THEOREM`.** Two findings, and the split *is* the result:
>
> 1. **The literal claim is REFUTED at its load-bearing bridge.** "Record-immutability ⇒ monotone
>    accretion ⇒ (Kleene) a fixpoint ⇒ **no internal fixpoint-free involution**" is **false at the
>    third arrow**. Adversary-C exhibits a genuine **immutable** (append-only) record dynamics with a
>    **source-internal fixpoint-free involution**: a ledger that accretes *flip-events*, whose derived
>    orientation `o(R) = (#flip-records) mod 2` induces the **swap** on `{+,−}` — a fixpoint-free
>    involution (`ι²=id`, no fixed point) realized **without deleting any record**. The involution acts
>    on a **derived orientation**, not on the records, so immutability is intact. **Monotonicity does
>    NOT forbid an internal fixpoint-free involution.**
>
> 2. **But source-is-observer SURVIVES as a theorem under the corrected standard.** The becoming-witness
>    the trunk actually needs (spectral-flow synthesis) is **first-person underivability**, not mere
>    fixpoint-freeness. Every **internally-derived** orientation is a function of the records, hence
>    **third-person computable = DISCLOSED** — the parity involution included: a third-person predictor
>    reads `o(R)` off the ledger **exactly** (a Kleene readout / **quine**). Genuine becoming needs an
>    orientation the inside **cannot** derive; underivable ⇒ **not a function of the records** ⇒
>    **external**. So the real necessity runs through **DERIVABILITY, not fixpoint-freeness**, and it
>    still lands on **external**.
>
> **σ's externality is NECESSARY, not accidental.** `σ = w₁(L_time)` is the unique DU object that is
> *both* a fixpoint-free involution (`U K_S U⁻¹ = −K_S`, pointwise-exact) *and* underivable
> (Gödel-independent; `no_invariant_valuation` is Lean-proved, needing **only** fixpoint-free α — Prong
> III). The record accretion is intrinsically **orientable** (immutability = a globally-consistent
> "later" direction = trivial `w₁`, a torsor, fixpoint-ful); the fixpoint-free twist lives on a
> **different bundle** (the metric fiber's arrow-of-time line), external to the records. **The
> condition** is exactly the caveat the trunk synthesis already carried open: this holds *iff* one
> requires **first-person underivability** for "genuine becoming." If disclosed formal-involution
> (parity) is accepted as becoming, the theorem downgrades to finding (1) — the refutation.

Kill/verify conditions were declared before computation (probe docstring + the positive controls that
must fire the OTHER way). Probe `tests/du_record_immutability_external_involution_probe.py`, foreground,
deterministic, **exit 0**, all controls fire.

---

## 1. The claim, decomposed (so the proof and the refutation land on the right arrow)

The pre-registered chain:

> **immutable** ⟹ **monotone/inflationary** ⟹ (Kleene) **has a fixpoint** ⟹ **no internal
> fixpoint-free involution** ⟹ **L2 external** ⟹ **σ external by necessity** (source-is-observer).

Four distinct links. Grading them separately is the whole discipline, because three are theorems and
one is false — and the conclusion is nonetheless rescued by a *different* route.

- **(i) L1** = self-encoding: a point-surjection `A → B^A` (the record set encodes its own describers).
  The trunk established L1 is *installed* by the self-authoring loop (0.68 vs 0.00 blind).
- **(ii) L2** = a **fixpoint-free involution** on the value/orientation object `B` (`ι²=id`, no fixed
  point). By Lawvere, L1 with a fixpoint-free `g:B→B` forces the diagonal element to escape every
  internal describer = the becoming-witness.
- **(iii) immutability** = records don't un-happen (Bet #2: *finality = irrevocable accretion*). We
  read this as: the state grows in the record partial order; the growth law is a function of the
  existing state.

The target: **immutable ⇒ L2 must be external.**

---

## 2. The proof attempt — three of the four links ARE theorems

### 2.1 immutable ⇒ inflationary ⇒ **has a fixpoint** (the quine). THEOREM.

Model the accretion as `Φ(R) = R ∪ g(R)` where `g(R)` is the records generated from the current state.
Immutability = **union** = never delete, so `R ⊆ Φ(R)`: `Φ` is **inflationary**. By **Bourbaki-Witt**
(an inflationary map on a chain-complete poset has a fixpoint) — *no monotonicity of the law `g`
required* — iteration from `⊥ = ∅` reaches `R*` with `Φ(R*) = R*`, i.e. `g(R*) ⊆ R*`: a record set
**closed under its own generation law** = the self-consistent record set = the **disclosure limit / a
quine**. If `g` is additionally Scott-continuous, the sharper **Kleene fixed-point theorem** gives `R*`
as the sup of the ω-chain (the accretion *is* the ascending Kleene chain). *Probe Part 1:* the modeled
`Φ` (with a deliberately **non-monotone** `g`) is inflationary at every step, reaches `Φ(R*)=R*` closed
under `g`; a deleting (non-immutable) control is non-inflationary and **cycles** — no closure. **The
"has a fixpoint" link is a theorem**, and cleaner than the claim states (Bourbaki-Witt needs only
*inflationary*, which immutability gives for free).

### 2.2 The Lawvere link, *if L1 is a total point-surjection*. THEOREM — but the hypothesis is only fixture-grade.

Lawvere: a point-surjection `e:A→B^A` forces **every** `g:B→B` to have a fixpoint. *Contrapositive:* a
fixpoint-free `g` (L2) ⇒ **no** point-surjection ⇒ the self-encoding is **not internally total** ⇒ the
diagonal escapes = the becoming-witness is external. This is the +9 addendum's "inside-ness forces
outside-ness," and it is genuine. **But** it needs L1 to be a *total* point-surjection, and Prong III is
explicit that L1-as-total-diagonal "lands at fixture grade," blocked at the product-uniform
norm-resolvent obstruction. So the pure-Lawvere route to "L2 external" is **conditional on an unproven
totality**. This matters, because it is exactly the crack the refutation walks through.

### 2.3 The order-theoretic reading of immutability — orientability. (Sets up both the refute and the rescue.)

Immutability has a sharper reading than "monotone." *Records don't un-happen* means the accretion
carries a **globally-consistent direction** (a well-defined, non-vanishing, self-returning "later-than"
field). A globally-consistent direction is an **orientation in the trivial class** (`w₁ = 0`): the
accretion is **orientable**, and immutability *is* the choice of orientation. Hold this — it is the
hinge.

---

## 3. The REFUTATION (Adversary-C, at full strength): the third link is FALSE

**Claim under attack (the third arrow):** "has a fixpoint ⇒ no internal fixpoint-free involution."

**The crux the task names:** must the involution act on the **records** (⇒ deletion ⇒ violates
immutability), or can it act on a **derived orientation** that flips **without deleting**? Adversary-C
builds the second, and it is genuine.

**The counterexample — the parity-of-flips ledger.** An **append-only** (immutable) ledger accretes
*flip-events*. Define the derived orientation `o(R) = (#flip-records in R) mod 2`.
- **On the records**, "append a flip" is `R ↦ R ∪ {new}` — strictly increasing, and applying it twice
  gives `R ∪ {f₁, f₂} ≠ R`: it **never returns** (immutable — nothing is deleted). So on the records it
  is *not* an involution; it is monotone accretion.
- **On the value object** `{+,−}`, the *induced* map is the **swap**: `ι(+) = −`, `ι(−) = +`. This is a
  **fixpoint-free involution** — `ι² = id`, no fixed point — realized by pure accretion, deleting
  nothing. The orientation sequence is `+,−,+,−,…`: it flips every step.

*Probe Part 2:* append-only records only grow; append-twice does **not** return; the induced map is a
fixpoint-free involution. **So an immutable record dynamics DOES host a source-internal fixpoint-free
involution.** The literal bridge is **refuted**: monotone accretion does **not** forbid one — the
involution lives on a *derived orientation*, off the record poset, where flipping costs no deletion.

**Why Lawvere doesn't save the bridge here:** the parity ledger is fixpoint-free on `{+,−}` *precisely
because* it has **no total point-surjection** — a countable accreting ledger cannot encode all `2^A`
functions `A→{+,−}` (Cantor). L1 is *partial*, not total, so Lawvere permits the internal fixpoint-free
involution. This is the fixture-grade gap of §2.2 made concrete. **The claim as literally stated is
dead.**

---

## 4. The RESCUE: the real invariant is DERIVABILITY, and it still forces external

The refutation produces a fixpoint-free involution that is **disclosed**, and disclosure is exactly what
disqualifies it as the *becoming*-L2. This is not a dodge — it is the trunk's own corrected standard
(spectral-flow synthesis §2): the becoming-witness is **first-person underivability**, not a
third-person Gödel sentence, and *not* mere formal fixpoint-freeness.

**The parity involution is DISCLOSED.** `o(R) = parity(#flips)` is a **function of the records**, hence
**third-person computable**: a god's-eye predictor reads it off the ledger **exactly**. *Probe Part 3:*
derived-orientation recovery accuracy **1.0**. It is a **Kleene readout / quine** — the ledger computes
its own consistent orientation. Formally fixpoint-free, but **derivable**, so it fires **no** diagonal
that escapes the inside: it is disclosure wearing an involution costume, the same absorber that ate the
self-authoring loop (L1 without a *genuine* L2).

**The external coin is UNDERIVABLE.** An orientation `σ` **not written into the records** is recoverable
by **no** function of the records: *Probe Part 3:* accuracy **0.492 ≈ chance**. This is
Gödel-independence made operational — `no_invariant_valuation`, **Lean-proved** (Prong III), needing
**only** that σ is a fixpoint-free involution. "The observer forces externality but cannot supply σ's
value" is a **theorem** on this leg, and it **never depended on L1**.

**The corrected necessity (the theorem):**
> Any orientation **internal to** the record dynamics is a **function of the records** ⇒ **third-person
> computable** ⇒ **DISCLOSED** (derivable by the inside too). Genuine becoming requires an orientation
> the inside **cannot** derive. Underivable ⇒ **not a function of the records** ⇒ **EXTERNAL**.
> Therefore the **becoming-L2 is external by necessity.** ∎ (under the underivability standard)

The refutation is **absorbed**, not defeated: it is a *real* internal fixpoint-free involution, but a
*disclosed* one, so it is not the becoming-L2. The bridge that survives is **monotone-derived ⇒
computable-from-inside ⇒ disclosed ⇒ not-underivable**, and **underivable ⇒ external** — which is
airtight and needs **neither** the false "monotonicity forbids involutions" step **nor** the
fixture-grade L1-totality.

---

## 5. The topological instance — σ = w₁(L_time) is external by construction (three-seam Prong A)

The abstract theorem has a concrete DU face, and it is decisive. The record helix's type-quotient is the
**shard-cycle** `S→I→O→S`. Ask: does the cycle carry a canonically-forced fixpoint-free
orientation-involution?

- **The record-arrow's own orientation is the TRIVIAL class.** A consistent cyclic successor direction
  returns to itself: `w₁(TS¹) = 0`. Its two orientations (the record-arrow direction) are a **free Z/2
  torsor** — a *stable global choice*, **fixpoint-ful**, NOT the fixpoint-free involution the diagonal
  needs. This is §2.3's orientability, realized on the cycle. *Probe Part 4:* `record_arrow_w₁ = 0`,
  has a global section.
- **The fixpoint-free flip is a Möbius twist (`w₁ = 1`)** — no global section, genuinely fixpoint-free
  — **but it is not forced by the record structure.** Obtaining it requires **decorating** the cycle
  with a `sign(K_S)`-band, and (Prong A, four independent links): the type-quotient **forgets**
  `sign(K_S)` (no functor transports it); the accumulation is **realization-dependent** (`K_S, −K_S`
  isospectral ⇒ *both* a flip-closure `w₁=1` and a no-flip-closure `w₁=0` exist on the same cycle); and
  the fresh-token seam sign **IS the inserted external coin σ**. *Probe Part 4:* both closures exist
  (`w₁=1` and `w₁=0`); GU forces neither. "Cycle-orientation = σ" is a **tautology of insertion**, not a
  derivation — `A-NUMEROLOGY`.
- **What is forced is `σ = w₁(L_time)`** — the Möbius class of the arrow-of-time line bundle over the
  **metric fiber** `F ≅ RP³`, the monodromy of the fixed deck involution `U` (`U K_S U⁻¹ = −K_S`). It
  **is** an orientation class — of a canonical line bundle **external to the record accretion**, not of
  the record cycle.

So the concrete instance matches the abstract theorem exactly: the **record-derived** orientation is
trivial/orientable (fixpoint-ful, disclosed), and the **fixpoint-free** one is `w₁(L_time)` — a
different bundle, external, Gödel-independent.

---

## 6. Exhaustiveness — there is no source-internal *underivable* fixpoint-free involution

The last thing an honest proof owes: could Adversary-C's *next* candidate be internal **and**
underivable? No — the disjunction is exhaustive.

- If the growth law is a **fixed computable rule** (DU's case — D-FORK: DU's source is "a fixed physical
  action generating a monotone 4-volume … on the FTS side by construction"), then every function of the
  records is computable = **disclosed** (parity, fixed-law order-complex torsion — the APS-index
  absorber).
- If the growth law is a **productive / non-c.e.** object (underivable-from-below), then by the D-FORK's
  own oracle disjunction it **factors through an oracle** — the posited fixed source or the unbuilt
  action as a completed history — i.e. an **external datum by another name**.

*Probe Part 5:* the cell "internal-derived **AND** underivable" is **empty**; every source is exactly
one of {internal-derived-disclosed, external-underivable}. This mirrors Prong III's **α-parity
eigenspace completeness** (every operator is even + odd, uniquely, no third class): the **odd**
(fixpoint-free) part **with an underivable value** is *precisely* the external posit. There is no fourth
door.

---

## 7. Personas inline (DU board — lenses, not evidence)

- **Model-theorist (Lawvere/Kleene/Gödel; internal-generativity).** "The claim conflates *fixpoint-free*
  with *Gödel-independent*. Kleene: self-reference with a computable fixpoint is a quine (parity).
  Lawvere: a fixpoint-free `g` forces no total point-surjection — but a *partial* self-encoding (a
  countable ledger) permits an internal fixpoint-free `g` that is still **computable**. The diagonal
  that *escapes the inside* needs the involution's **value** to be underivable, which a
  function-of-the-records never is. **Reads: literal bridge false; underivability rescue sound.**"
- **Order/Domain theorist (finality = closure/monotonicity).** "Immutability = inflationary, and
  Bourbaki-Witt hands you the fixpoint with **no** monotonicity of the law — the accretion *is* the
  Kleene chain and its sup is the quine. But a fixpoint of `Φ` on the record poset says nothing about a
  fixpoint of a **derived** involution on `{+,−}` — different objects. The real content is:
  immutability makes the accretion **orientable** (a consistent direction = trivial `w₁`), so its *own*
  orientation is a torsor, fixpoint-ful. **Reads: the twist must be off-poset = external.**"
- **Type-theorist (external-as-effect).** "A derived orientation is a **pure** value (a function of the
  state); an underivable orientation is an **effect** — an oracle read / an indexical the context
  supplies. Parity is pure ⇒ disclosed. Becoming needs an effect ⇒ external. The Krein σ is the effect;
  the ledger is the pure part. **Reads: external by necessity.**"
- **Symbolic Dynamics (irreversibility/immutability).** "Append-only = a one-sided shift; the derived
  parity is a **factor map** onto `{+,−}^ℤ` under the shift — fully determined by the record tape
  (deterministic factor = disclosed). An *underivable* orientation would be a symbol **not** in the
  tape's sigma-algebra = external input. **Reads: parity is a factor (disclosed); σ is exogenous.**"
- **Adversary-C (strongest internal-involution counterexample).** "I built the best one — parity-of-flips,
  a *genuine* fixpoint-free involution in a *genuine* immutable dynamics, deleting nothing. It **refutes
  the literal claim**. But I concede it is **recoverable-from-records** (acc 1.0), so it is disclosure,
  not becoming. My next candidate (a non-computable law) factors through an oracle = external. I cannot
  build a source-internal **underivable** fixpoint-free involution. **Reads: literal REFUTE stands;
  source-is-observer survives at the underivability standard.**"

**Board convergence:** unanimous that the literal monotonicity bridge is **refuted** (parity); unanimous
that the becoming-L2 is **external by necessity** under the **underivability** standard; unanimous that
σ's externality is **necessary, not accidental** (a different bundle / an effect / an exogenous symbol /
`no_invariant_valuation` Lean-proved). No dissent survives to an unconditional THEOREM, and none survives
to a full REFUTE of source-is-observer.

---

## 8. Honest outcome (the two questions the task asks)

**Is source-is-observer a THEOREM (immutability ⇒ external involution) or REFUTED (an internal
fixpoint-free involution exists)?** — **Both, cleanly separated, hence CONDITIONAL:**
- The **literal** theorem ("immutability/monotonicity ⇒ *no* internal fixpoint-free involution") is
  **REFUTED**. Name of the counterexample: the **parity-of-flips ledger** — an append-only immutable
  record dynamics whose derived orientation `o(R)=parity(#flips)` is a fixpoint-free involution on
  `{+,−}`, realized without deletion. So the trunk quest for an internal involution is *not* closed by
  immutability alone — but the internal one it yields is **disclosed**.
- The **intended** theorem ("the **becoming**-L2 is external by necessity = source-is-observer") is a
  **THEOREM under the corrected standard** that genuine becoming = first-person **underivability**: every
  internally-derived orientation is third-person computable (disclosed), the record accretion's own
  orientation is trivial/orientable (a torsor), the internal-and-underivable cell is empty, and
  **underivable ⇒ external**. The right necessity is **DERIVABILITY, not fixpoint-freeness**.

**Is σ's externality necessary or accidental?** — **NECESSARY.** Not a construction gap and not bad luck:
`σ = w₁(L_time)` is the unique DU object that is simultaneously a fixpoint-free involution
(`U K_S U⁻¹ = −K_S`, pointwise-exact) **and** underivable (Gödel-independent; `no_invariant_valuation`
Lean-proved, needing only fixpoint-free α). An immutable record accretion is intrinsically orientable, so
it structurally **cannot be its own** fixpoint-free-and-underivable involution; that twist is a
different-bundle, external datum. σ's externality is forced.

**The condition (what would flip it).** The theorem is CONDITIONAL on the **underivability standard**.
If one accepts a **disclosed** formal-involution (parity — third-person computable) as "genuine
becoming," then finding (1) governs: an internal fixpoint-free involution exists and source-is-observer
is **not** forced (becoming would be a dressed recursion). This is *exactly* the caveat the trunk
synthesis pre-registered as open — "whether first-person underivability under a **fixed** rule is genuine
becoming or a sophisticated disclosure" — now localized precisely: it **is** the whole hinge, and it is a
foundational / ai-epistemology question, not settled here.

---

## 9. What this earns and does not earn

**Earned (re-verified with DU's own apparatus; grades consumed, not moved):**
- A **precise decomposition** of the trunk's headline into four links, with the false one named (the
  third arrow) and a **concrete refutation** (parity-of-flips) — sharper than "monotone ⇒ quine."
- The **corrected theorem**: the becoming-L2 is external by necessity via **derivability**, needing
  neither the false monotonicity step nor the fixture-grade L1-totality — it rides the Lean-proved
  `no_invariant_valuation` (involution leg), which never depended on L1.
- The **σ-externality = necessary** result, matched abstractly (orientable accretion vs off-bundle
  twist) and concretely (three-seam Prong A: record-derived orientation trivial; σ = w₁(L_time)
  external).
- A **probe** with mandatory positive controls (a real internal involution; disclosed-vs-underivable at
  1.0 vs ~0.5; orientable cycle vs fixpoint-free Möbius; empty forbidden cell) so every verdict is
  falsifiable and separated (exit 0).

**NOT earned (no promotion; `claim_status_change: none`):**
- No claim banked; nothing cleared Lane 3. The result is CONDITIONAL on the underivability standard, and
  that standard's own status (fixed-rule becoming vs disclosure) stays **open** — the trunk's honest
  residue, not resolved here.
- The Lawvere-diagonal *totality* (L1 as a total point-surjection) remains **fixture grade** (Prong
  III's product-uniform obstruction); the theorem here **routes around** it via derivability rather than
  discharging it.
- σ is untouched (R7). "External by necessity" is a statement about the **becoming-involution's**
  sourcing, not a re-derivation of σ's value (which stays the external Z/2 packet).

## 10. Boundary

Exploration tier, proof-or-refute at reconstruction/structural grade, argued from the objects' own
construction and re-verified per CONNECTIONS.md; no cross-repo grade imported (the Lean `no_invariant_
valuation`, the Prong A A-NUMEROLOGY, the D-FORK FTS verdict, the +9 L1/L2 addendum are each consumed as
re-verified hypotheses, not adopted on a sibling's say-so). Only this artifact and its probe
(`tests/du_record_immutability_external_involution_probe.py`, foreground, deterministic, **exit 0**,
positive controls fire) were written. No edit to any claim/canon/verdict/ledger file, LANES.yaml, the
prediction register, or another agent's artifact. `claim_status_change: none`; `canon_verdict_change:
none`; `public_posture_change: none`. Kill/verify conditions declared before computation. Krein sign σ
untouched (R7). **Not committed/pushed (per task).**
