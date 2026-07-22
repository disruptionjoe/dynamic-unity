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
- **State: SEAM** (conditional candidate — antecedent unbuilt).
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
  (wave-2 build/kill). (iii) Therefore doubly-gated: it is not even a *live* prediction until the
  productive mode-issuance unlock exists.
- **Hardening checklist (what must be discharged before it moves).**
  - *SEAM → REGISTERED (antecedent gate):* **H1.** The §3 mode-issuance unlock is built enough that
    the finality threshold is a real consequence, not a hoped-for one; only then can a falsifiable
    statement be frozen.
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

## Boundary
Lane 4.1 working state. Registration ≠ seeding ≠ publishing. The factory owns paper production and
Joe owns posting; this register only holds and hardens candidates up to the SEED-READY gate.
