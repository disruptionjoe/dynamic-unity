---
title: "Dynamic Unity prediction register — Lane 4.1 pre-seed holding state, with an explicit seed gate"
status: active_research
doc_type: register
created: 2026-07-21
note: "Operationalizes Lane 4.1 ('extract, freeze, and expose falsifiable predictions, carried with their blockers') as the UPSTREAM holding state before Lane 4.2 seeds anything to the Drafting Factory. Nothing crosses the seed gate until it is SEED-READY. A candidate prediction is registered here so it is not lost — being registered is NOT being seeded."
---

# Dynamic Unity prediction register

The pre-seed home for prediction candidates. A claim lives here from the moment it is
prediction-shaped until it is either seeded to the Drafting Factory (Lane 4.2) or retired.
**Registration is not seeding.** The register exists precisely so a promising-but-unhardened
prediction can be *held and worked* without being pushed to the factory half-formed.

## Lifecycle states

| State | Meaning | Seedable? |
|---|---|---|
| **SEAM** (conditional candidate) | Prediction-shaped, but its **antecedent/mechanism is unbuilt** — it is a prediction only *if* some upstream unlock lands. Cannot yet be frozen as a falsifiable statement. Registered so it is not lost; carried with its antecedent-blocker + a hardening checklist. | **No** |
| **REGISTERED** (frozen-with-blocker) | The antecedent exists enough to freeze a genuinely falsifiable statement. Frozen and carried with its blocker(s). Internal hardening still open. | **No** |
| **SEED-READY** | The hardening checklist is discharged: quantitative statement, a concrete falsifiable gap vs. the standard account, units/no-signaling guards passed, a runnable platform, and a pre-registered cheap kill. A well-formed seed is prepared. | **Yes — this is the 4.1→4.2 gate** |
| **SEEDED** | Routed to the Drafting Factory mailbox (Lane 4.2). Leaves the active set; recorded here. | — |
| **RETIRED** | Falsified, absorbed, or withdrawn. Recorded with the reason. | — |

### The seed gate (non-negotiable)
Nothing is seeded to the Drafting Factory until it is **SEED-READY**. A SEAM or REGISTERED entry
is repo-internal working state only. This is the honesty discipline at the shipping boundary: the
factory receives well-formed seeds, never speculative ones.

---

## Entries

### PRED-DU-001 — "un-recoverable beyond unitary cost" (a sharp finality knee in V(R))
- **State: SEAM for seeding / active conditional-model specimen.**
- **The claim (conditional).** *If* DU's finality is a genuine sharp irreversible-accretion
  threshold (the §3 productive mode-issuance unlock), *then* in a controlled-redundancy which-path
  experiment the interference visibility `V(R)` shows a **knee at a critical redundancy `R_c`** and
  the which-path record becomes **un-recoverable beyond the unitary cost** — a deviation from the
  smooth, always-in-principle-recoverable crossover that standard decoherence predicts.
- **Where it lives.** Reversible-measurement / few-copy-redundancy regime (trapped-ion / QC
  reversible measurement; Wigner's-friend family), *not* the vanilla double-slit (there DU = QM by
  construction; delayed-choice needs no retrocausality — no-signaling keeps the marginal a blob).
  Closest existing formalism to the "record already fixed in the global causal set" intuition:
  two-state-vector / retrocausal-consistent, operationally visible in weak measurement.
- **Blocker(s).** (i) It is a **deviation from unitary QM** — a large claim. (ii) **DU-as-built
  does not predict it**: μ is Born-blind (Bet #1) and the mirror-condensate count is one-shot
  (wave-2 build/kill). (iii) Therefore it is not seed-ready or an unconditional DU prediction.
  This does **not** bar a labeled conditional construction; source derivation is not an
  exploration gate.
- **Hardening checklist (what must be discharged before it moves).**
  - *SEAM → REGISTERED (antecedent gate):* **H1.** The §3 mode-issuance unlock is built enough that
    the finality threshold is a real consequence, not a hoped-for one; only then can a falsifiable
    unconditional DU statement be frozen. Conditional-model work may proceed before H1.
  - *REGISTERED → SEED-READY (internal hardening):* **H2.** Quantitative form — define `R_c` and the
    functional shape of `V(R)`/recoverability; predict the knee's *location and sharpness*, not just
    its existence. **H3.** A concrete falsifiable gap vs. standard decoherence's smooth crossover
    (what is measured, at what precision, what refutes). **H4.** Units/no-signaling guards — TaF
    rate²-to-rate² sanity; confirm the marginal stays a blob (effect lives only in
    recoverability/coincidence). **H5.** Beat the block-universe absorber operationally (why the
    threshold is genuine finality, not a relabel). **H6.** Map to an actually-runnable platform,
    with the weak-value regime as operational home. **H7.** Pre-register a cheap kill — an outcome
    (e.g. smoothness at the platform's resolution) that falsifies DU's version specifically.
- **Source pointers.** `wave2-flagship-convergence-synthesis-2026-07-21.md` §6; the double-slit
  discussion (records/finality account of correlation-determinism);
  `bet1-measurement-via-records-finality-2026-07-21.md` (μ Born-blind — why the mechanism is not
  yet there).
- **Disposition.** Held as a SEAM. It is the flagship's first *empirical* target; it becomes a
  live REGISTERED prediction the moment H1 lands, and is not seeded to the factory before H2–H7.

#### 2026-07-23 conditional-model result

`SWING-DU-SCI-01` supplied an executable independent-record specimen with branch fidelity `F`,
information exposure `M=-R ln F`, an imported threshold `M_c`, and an imported persistent
post-crossing flag. Conditional on those posits it derives
`R_c(F)=ceil(M_c/[-ln F])`, a common continuous-knee visibility `exp(-M_c/2)`, integer overshoot
bounds, and a forward/reversal recovery surface. Exact finite-unitary construction confirms
`V=F^(R/2)` and full recovery under the standard global inverse.

This partially discharges H2 and supplies a multi-fidelity/count-only discriminator for H3.
It also finds an identifiability ceiling: an unconstrained steep smooth memory law fits the finite
grid within `0.001375`, so a knee alone is not novel and does not identify finality. State remains
**SEAM / CONDITIONAL_MODEL_ONLY / IDENTIFIABILITY_LIMITED**. Reopen physical promotion only with
a mechanism selecting the trigger/scale, an AQFT-local update, and either an independently
justified smooth-slope bound or another mechanism-specific observable. See
`conditional-finality-knee-model-2026-07-23.md`.

### PRED-DU-002 — the finality-threshold deviation is Lorentz-covariant-by-construction
- **State: SEAM** (conditional — shares PRED-DU-001's antecedent, plus its own proviso). This is the
  *covariance property* of PRED-DU-001's observable, not an independent observable.
- **The claim (conditional).** *If* the finality threshold is real (the mode-issuance unlock), the
  redundancy-gated recoverability knee of PRED-DU-001 is **Lorentz-covariant-by-construction** — its
  trigger is the causal-order **redundancy count**, a frame-independent invariant — genuinely
  **evading the frame-dependent-noise tension** that afflicts relativistic GRW/CSL (Pearle/Bedingham).
  I.e. a *covariant objective-collapse* candidate: objective (observer-independent H¹ fact) yet not a
  spacetime process. Established at causal-set/order + qubit-schematic level by the covariant-finality
  build+kill pair (foliation NOT smuggled; the third position is real).
- **Blocker(s).** (i) Shares PRED-DU-001's mode-issuance antecedent (doubly-gated). (ii) Its **own**
  blocker — the **locality-of-update proviso**: finalization must be a *local* Fewster–Verch
  operation; a *global* Lüders update reintroduces Sorkin's impossible measurement → superluminal
  signal → DEVIATION-BUT-NON-COVARIANT. (iii) Likely survives existing collapse-model bounds (Donadi
  X-ray, matter-wave) — no always-on coupling — but is experimentally subtle (coincidence, not marginal).
- **Hardening checklist.** *SEAM → REGISTERED:* shares PRED-DU-001 **H1**, PLUS **H1'.** the
  **AQFT-net (Haag–Kastler) embedding** — construct the finality closure on the net of local algebras
  and *prove* Fewster–Verch causal factorization *from* "final ≡ fixed on J⁺" (currently matched, not
  derived), AND establish the update is *local*, not global Lüders. *REGISTERED → SEED-READY:* inherits
  PRED-DU-001 H2–H7.
- **Source pointers.** `covariant-finality-collapse-synthesis-2026-07-21.md` (§3, §5); the build +
  adversarial-kill pair it synthesizes.
- **Disposition.** Held as a SEAM beside PRED-DU-001 — a *covariance upgrade* of the same observable,
  its prize being that a covariant objective-collapse candidate evades the standard Lorentz tension.
  Not seeded before its own H1' (the AQFT-net embedding) plus the shared gate.

---

## Conditional predictions — labeled-assumption, NOT source-gated (added 2026-07-22)
**Correction of an over-conservative posture.** PRED-DU-001/002 above were filed as SEAMs "doubly-gated
on the unbuilt source" — correct for the SEED gate, but WRONG as a bar on the *prediction itself*. A
**conditional prediction** ("IF the source has [labeled minimal assumption], THEN [falsifiable
consequence]") is standard physics (all of EFT/BSM) and needs no source built. It is a first-class
product, graded *conditional on the labeled posit*, and it **does work either way: if it fails, it
falsifies the assumption and constrains the source.** These are NOT source-gated; only *seeding* them to
the factory follows the normal SEED gate. Strength ≈ (minimality/motivation of the assumption) ×
(falsifiable content the framework adds beyond it). Lead with the assumption; keep every posit labeled.

### CPRED-01 — TeV mirror sector → collider + dark-matter signature (least-gated; strongest to make now)
- **Assumption (labeled):** the source produces the recovered Z/2 mirror sector at ~TeV with minimal structure.
- **Content/target:** the LHC signature (masses, couplings, σ) AND whether mirror baryons are a viable
  dark-matter candidate (relic abundance). **The real target is a PINNED RELATION** (a mass ratio / the
  scale tied to σ,τ) — the difference between a prediction and "there might be a particle."
- **Falsifier:** LHC non-observation at the pinned scale; DM direct-detection / relic mismatch.
- **Execution:** parallel-flow P08 — frame as conditional-with-a-pinned-relation, not a free-parameter catalog.

### CPRED-02 — exactly 3 generations, forced by the Z/3 trit (structural)
- **Assumption:** the generation structure is τ = Z/3 (established in-session).
- **Content:** the count is forced to **3** — forbids 2 and 4 (a menu-restriction, not just "explains 3").
- **Falsifier:** a 4th generation; or the Z/3 forcing failing on audit.

### CPRED-03 — RETIRED AS WRITTEN: exactly one external Z/2 bit
- **State: RETIRED / STALE-PREMISE (2026-07-23).**
- **Why:** GU's corrected operator bridge establishes only failure of one
  `K`-definite polarization. It does not establish nonexistence or cardinality of
  `J`-self-adjoint domains, physical externality, `σ=w1`, or a nonzero anomaly
  class. `no_invariant_valuation` remains a generic codomain theorem but does not
  by itself prove that no physical internal observable supplies `σ`.
- **Disposition:** do not use "exactly one external bit" as a current DU
  prediction or source theorem. A future explicitly constructed physical-domain
  bridge could reopen a differently warranted candidate; until then this entry
  remains as supersession history, not an active conditional prediction.

### CPRED-04 — no phantom crossing, w > −1 (cosmology; gated on COV-03)
- **Assumption:** dark energy IS a healthy single canonical scalar (the tachyon roll).
- **Content:** w stays > −1, no crossing of the phantom divide (single-field theorem); sharp, DESI-testable,
  theorem-backed (σ = fixed external sign → no dynamical sign flip).
- **Gate:** COV-02 showed the *local* roll is superluminal-or-trivial → rides COV-03 (the causal-past-N roll
  being a *healthy* single field). Gated on that health, not on the full source.

## Boundary
Lane 4.1 working state. Registration ≠ seeding ≠ publishing. The factory owns paper production and
Joe owns posting; this register only holds and hardens candidates up to the SEED-READY gate.
