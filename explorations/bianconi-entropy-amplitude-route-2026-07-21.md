---
title: "Bianconi entropy -> DE amplitude: give the sigma-Tr-ln-G habitat its dynamics"
status: exploration
doc_type: exploration
lane: "1.1"
created: 2026-07-21
grade: "PARTIAL -- dynamics genuinely built; volume->Lambda link FORCED in the exponent (-1/2), IMPORTED in the value"
directed_by: "Joe direct chat, 2026-07-21 (DU Lane 1.1 pre-registered swing; second independent route to the DE amplitude)"
probe: "tests/bianconi_entropy_amplitude_probe.py (foreground; exit 0; 11/11 checks)"
reads:
  - "possibility-to-capability/explorations/2026-07-20-discrete-gfe-specimen/ (the specimen)"
  - "possibility-to-capability/literature/2026-07-20-discrete-gfe-primary-equation-verification.md (Eqs 6 & 10 verified)"
  - "possibility-to-capability/explorations/2026-07-17-self-excitation-boundary-big-swing/ (9-item obligations)"
posture: "Ingested cross-repo, re-verified here (DU sovereign self-check). Grades are DU's own, not consumed on P2C's say-so. Nothing banked until Lane 3."
---

# Bianconi entropy -> DE amplitude: giving the `sigma*Tr ln G` habitat its dynamics

## The swing in one paragraph

The Bianconi discrete-GfE specimen (arXiv:2404.08556, "Quantum entropy couples matter with
geometry") is a published, target-free **variational** action carrying a genuine log-volume
vacuum-entropy term `sigma * Tr ln G`, a loop-only Z/2 holonomy, and a discrete Dirac `D = d + d†`.
P2C froze it as a two-sector specimen candidate but named its blocking gap precisely: it is
**purely variational** — no Hamiltonian, no dynamical transition, before/after is kinematic
juxtaposition. That missing dynamics is exactly what Dynamic Unity exists to supply. This swing
supplies it and asks the flagship question: does `sigma*Tr ln G`, once given dynamics, **natively
deliver the volume->Lambda link** (the dark-energy amplitude `Lambda ~ 1/sqrt(N)`)? The honest
answer is **PARTIAL**: the dynamics is real and non-trivial, and the entropy term **forces the
`N^{-1/2}` scaling exponent for free**, but the identification of `Lambda` with the entropy
fluctuation (and the value) is an imported reading, not forced by the specimen.

## 1. What the specimen gives, and the one thing it withholds

Re-verified from the P2C extraction + the primary-PDF equation check (DU re-checks, does not
adopt on say-so):

- **Carrier.** Cell complex `K` with `N0` nodes, `N1` edges, `N2` two-cells; topological spinor
  `Phi = (chi, psi, xi)`; total `N = N0 + N1 + N2`.
- **Metric.** `G = diag(G0, G1, G2)`, one Hermitian-positive block per cell dimension. The
  vacuum-entropy term is built from `G` alone.
- **Action (Eq. 41).** `S = sigma * Tr ln G  +  Tr[G(ln G - ln G_ind)]  -  Tr G`. The first term
  is the **log-volume vacuum entropy** `sigma * Tr ln G = sigma * ln det G`; the second is the
  quantum relative entropy between the network metric `G` and the matter-induced metric `G_ind`.
- **Metric EOM (Eq. 56).** Setting `delta S / delta G = 0` gives `sigma * G^{-1} + ln G = ln G_ind`.
- **Loop-only Z/2.** Minimal substitution `B^(A) = B^+ e^{-iA} + B^- e^{+iA}` makes the phase a
  half-link transporter; the naive link-sign field is datum-free, and the only surviving order-two
  datum is the **full-link holonomy `h = prod e^{2iA} in {+1, -1}`**.
- **The withheld piece.** The word "Hamiltonian" never appears. No time axis, no evolution, no
  dynamical transition. `H := D` is a standard-field completion the paper *licenses* but never
  *performs*. **This is the gap.**

## 2. The dynamics DU supplies (anti-toy: not `H := D`, not kinematic)

The instruction was explicit: do **not** assert `H := D`; construct a **genuine dynamical
transition**. The natural, non-toy dynamics for a variational entropy functional is its own
**entropic gradient flow** (a geometric flow — the Differential Geometer's lens: make a static
geometry dynamic):

```
dG/dtau = - delta S / delta G = - ( sigma G^{-1} + ln G - ln G_ind )
```

This is a genuine dynamical system, and it earns the "not a toy" label on three counts the probe
verifies exactly (`tests/bianconi_entropy_amplitude_probe.py`, Part 1):

1. **It strictly dissipates.** `dS/dtau = -|delta S/delta G|^2 <= 0`, strict off the fixed point —
   real work is done along the trajectory, so the before/after is a **process**, not a relabeling.
2. **Its fixed point IS the specimen's Eq. 56.** The flow does not invent physics; it flows the
   metric to the exact variational vacuum the paper already writes down. DU supplies the *arrow*;
   the specimen supplies the *target*. (Converged to `|delta S/delta G|_max ~ 1e-15`.)
3. **The "after" is a genuine attractor.** Two distinct initial metrics reach the **same** fixed
   point — the endpoint is not the start relabeled; it is an initial-condition-independent
   attractor of an actual dynamics.

The generator here is the **entropic action's gradient**, not the Dirac operator asserted as a
Hamiltonian. `D` enters legitimately and only through `G_ind` (the matter-induced metric
`G_ind = I + diag(D|Phi><Phi|D)`, paper Eq. 43), so matter genuinely couples into the flow through
the specimen's own construction. This is the concrete substrate move the swing was for: the
`sigma-Tr-ln-G` habitat now has dynamics, and the dynamics is disciplined by the specimen itself.

*Faithfulness note (honest truncation).* Every entropy term is spectral (`Tr ln G`, `Tr G ln G`,
`Tr G`, `G^{-1}`), so working in the metric eigenbasis with per-cell eigenvalues `g_i > 0` is
faithful; the probe uses the diagonal-metric reduction the paper permits and P2C's own fixture
already adopted. General non-diagonal blocks are a follow-up, not a claim.

## 3. The volume -> Lambda link: FORCED in the exponent, IMPORTED in the value

This is the crux, and the place honesty bites hardest.

**The target.** `Lambda ~ 1/sqrt(N)` (N = accreted record count / cell count) is precisely the
**Sorkin / everpresent-Lambda** scaling — the one known mechanism that gives dark energy the right
order of magnitude, and the scaling LANES 1.3 wants to *beat the Sorkin-import by deriving
natively* rather than assert.

**What the entropy term forces (native, for free).** `Tr ln G = sum_i ln g_i` is a sum of `N`
**independent local** log-volume terms — it is *extensive*. Any stationary fluctuation ensemble of
`G` therefore makes the vacuum entropy fluctuate by `O(sqrt(N))` (the CLT, N independent local
contributions), while the extensive volume grows as `N`. The **fluctuation-per-volume** ratio is
thus `O(sqrt(N))/N = O(1/sqrt(N))`. The exponent `-1/2` is the CLT exponent; it is **not tunable**.

The probe measures this two ways (Part 3):
- **Analytic:** Gaussian fluctuations around the Eq. 56 vacuum give
  `Lambda_eff(N) = (sigma/g*) sqrt(Theta/S'') / sqrt(N)`, a clean `-0.5000` log-log slope over
  `N in {16 .. 1024}`.
- **A real dynamics realizes it:** a stochastic (Langevin) completion of the entropic flow —
  `dG = -delta S/delta G dtau + sqrt(2 Theta) dW`, stationary law `~ exp(-S/Theta)` — reproduces
  the predicted `Var(sigma Tr ln G)` to ~20% at `N = 64` (Monte-Carlo). So the `-1/2` is not an
  algebraic coincidence; a genuine dynamical process on the specimen produces it.

**The test has teeth (the falsifier control).** If the metric fluctuations are made
**non-extensive** — one global mode common to all cells instead of `N` independent local ones —
the same machinery gives slope `0`, not `-1/2`. A genuine falsifier can and does come out
differently; the `-1/2` is therefore a real property of the *extensivity of `sigma Tr ln G`*, not
a fitted constant. The `sigma = 0` control removes the entropy term and the amplitude vanishes
entirely: the DE amplitude, in this route, **comes from that term and no other**.

**What is imported (the honest debit).** Identifying `Lambda` with the fluctuation-per-volume —
i.e. **renormalizing the extensive mean away and keeping only the residual** — is the Sorkin /
everpresent reading. The specimen does not force it: its variational vacuum energy is the
*extensive mean* `~N`, which is the cosmological-constant problem itself, unsolved here. DU imports
the "mean cancels, fluctuation survives" identification wholesale. So:

> The `sigma*Tr ln G` term delivers the **`N^{-1/2}` SCALING natively and forcedly**; it does
> **not** deliver the **value** (that needs the imported cancellation-of-the-mean plus a
> units/coefficient fixing the observed magnitude). Scaling forced, amplitude fit.

This is genuine consilience *material* for the parallel DeWitt-measure route: if that independent
route also lands on `-1/2`, the exponent is doubly-sourced. But this route alone does not close the
amplitude.

## 4. Terrain (addressed as terrain, not gates)

**Record-change != finality (continuity-ledger).** *Is the log-volume accretion a genuine crossing
or bookkeeping?* Under the flow, `Tr ln G` changes by a genuine, dissipation-driven amount
(`Delta(Tr ln G) ~ -26.5` in the probe run, with `S` strictly dropping) — this is a real
transduction with `d > 0`, **not** the `d = 0` "count of source activity re-labeled" trap. The
probe's `d = 0` control (start the flow *at* its fixed point) yields **zero** accretion, so the
accretion is not a definitional artifact that appears for free — it requires genuine
off-equilibrium dynamics. **But** — and this is the type-distinction the terrain insists on —
record-change is *not itself finality*. The deterministic flow is (in principle) reversible, so it
is **record-change without finality**. Only the *stochastic* completion has genuine **entropy
production** (irreversibility), which is the finality candidate and is exactly TI's reversal-cost
measure `mu` pricing the arrow. Finality here therefore rests on an *added* ingredient (the
dissipative noise), honestly flagged — the accretion survives the `d = 0` trap but does not, on its
own, deliver finality.

**The D-FORK / Gödelian-regime question (TI).** *Is this source self-generating (Gödelian) or
finite-type?* The Bianconi complex is a **fixed** finite cell complex: `N` is constant, the metric
flows but the substrate does not accrete cells. As literally given, the specimen sits in the
**finite-type-space (disclosure) regime** — the "roll" is metric flow on a fixed `N`-cell
substrate, i.e. fixed-source disclosure, not self-generating issuance. To reach the Gödelian regime
where record-accretion is genuine *becoming*, `N` itself (the cell count) would have to grow
self-referentially — a **cell-accretion dynamics** the specimen does not supply and which would be
a further construction. Per the charter this is class-relative terrain, not a wall: a
growing-complex version could sit in the Gödelian regime; but for THIS substrate the honest reading
is disclosure, and the "becoming" interpretation of the DE is not earned here.

**Observer-gradient falsifier (TaF).** The mechanism is a global fluctuation-per-volume ratio; it
carries no observer-centred spatial gradient, so it does not trip the excluded-gradient falsifier.
(Cheap sanity check; passes.)

**Krein sign no-go (P2C).** DU already accepts the DE *sign* is external (`sigma`); this route
does not try to derive it from dynamics and so does not run into the Krein no-go — consistent with
the charter. The amplitude/scaling is the target; the sign is a supplied bit (see next).

## 5. Does the loop-only Z/2 map to GU's `sigma`? (Three sigmas, kept typed)

There is a genuine three-way `sigma` collision that must be kept typed apart, or the mapping
question dissolves into a pun:

1. **Bianconi's `sigma`** — the *entropy-coupling real constant* in `sigma*Tr ln G`. This is what
   sets the DE amplitude *coefficient* (`Lambda_eff proportional to sigma`).
2. **The loop-only Z/2 `h`** — the *gauge holonomy sector* `h = prod e^{2iA} in {+1,-1}`, an
   H¹-valued, configuration-chosen datum.
3. **GU's `sigma`** — the *fixed structural energy-positivity / Krein sign bit* (the external Z/2
   the Bounded Fiber Theorem's "Door 4" and the Krein probe say no conserving dynamics derives).

Are (2) and (3) the same Z/2? **Same abstract group, NOT the same physical bit** — and the probe
gives this a computational leg (Part 4): both holonomy sectors `h = +1` and `h = -1` yield
**positive-definite** induced metrics, so `h` does **not** select the sign of the vacuum energy.
GU's `sigma` is precisely the energy-sign/Krein bit; the Bianconi `h` is holonomy and leaves the
energy positivity untouched (`G` is positive in both sectors by construction). They *could* have
coincided only if the holonomy sector selected the Krein sign; the specimen provides no such
coupling. This matches the harvest's own warning that the tri-repo signed-graph agreement is
"partly by construction" and the H¹ coincidence "earns no identity." **Verdict: coincidence of
type, not identity of bit.** The DE sign remains the external `sigma`-posit DU already accepts; the
loop-only Z/2 is a decoupled holonomy sector, at most a subleading matter-level effect on the
amplitude coefficient, never its sign.

## 6. Inline DU board (personas as lenses; computation disposes)

- **Spin Geometry (the discrete Dirac `D`).** `D` is used honestly — as the source of `G_ind`
  (Eq. 43), the matter coupling into the flow — never smuggled in as the Hamiltonian. The
  `gamma_0`-symmetry (spectrum symmetric about zero) is intact; the holonomy leg is built on the
  exact ring `D`. No objection; flags that the general (non-diagonal, higher-d) `D` is untested here.
- **Dynamical Systems (supply the missing transition — the lead lens).** Delivered: a genuine
  dissipative flow with a strict Lyapunov function (`S`), a real attractor, and a stochastic
  completion with entropy production. This is a bona-fide before/after, not kinematic juxtaposition.
  Its own caution: the flow is a *DU-chosen* completion; the specimen licenses but does not uniquely
  pick it (other dynamics with the same fixed point exist). Honest — the fixed point is forced, the
  flow is a natural but non-unique choice.
- **Information Geometry (the entropy->Lambda link).** The `-1/2` is Fisher-flavoured exactly as
  expected: `sqrt(N)` is the standard-error width of `N` independent local log-volume terms. The
  lens's sharpest point: the *exponent* is native, but the *observable choice* (fluctuation, not
  mean) is the imported Sorkin identification — do not let the elegance of the CLT launder that in.
- **Constructor/Assembly (is the accretion a genuine transduction?).** `d > 0` confirmed (the
  `d = 0` control gives zero accretion). But assembly/issuance needs the substrate to *grow*; the
  fixed-`N` complex is disclosure-regime. Genuine transduction of the metric, yes; genuine issuance
  of new record, not without cell-accretion.
- **Metrology / Invariance (is `Lambda ~ 1/sqrt(N)` a real invariant or an artifact?).** The
  exponent is coordinate-free (it is the extensivity of a trace, invariant under basis change) and
  it flips under a genuine structural change (global vs local fluctuations) — so it is a real
  invariant of the *extensive* term, not a coordinate artifact. The *coefficient* is
  scheme-dependent (depends on `Theta`, the imported fluctuation scale), which is where the value's
  softness lives.
- **Anti-crank council (fires because an amplitude result is on the table).** Scientific Skeptic:
  "you imported the cancellation of the mean" — conceded, and stated in the grade. Adversary-C
  (strongest-form kill): "the whole `Lambda`-is-a-fluctuation move is Sorkin's; DU added dynamics
  but not the amplitude" — **this is correct and is the exact ceiling of the result.** The swing
  does not claim to have beaten the Sorkin import on the *value*; it claims the *scaling exponent*
  is now sourced from a specific published entropy term via a genuine dynamics, which is a real (if
  bounded) native contribution and consilience material.

## 7. Grade and what would move it

**GRADE: PARTIAL.** Dynamics genuinely built (the specimen's missing piece supplied, non-trivially,
anti-toy); the `sigma*Tr ln G -> Lambda ~ N^{-1/2}` link is **FORCED in the exponent** (native to
the extensivity of the entropy term; falsifier control has teeth) and **FIT/IMPORTED in the value**
(the Sorkin fluctuation-identification and the cancelled mean are not forced by the specimen). Not
DELIVERS (the amplitude value is not natively produced); not DOESN'T (the term genuinely and
forcedly supplies the hard-to-get `-1/2` scaling — the entropy term is *not* impotent).

**Does the accretion survive record-change != finality?** It survives the `d = 0` relabel trap (it
is a genuine `d > 0` transduction), but it is **record-change without finality** under the
deterministic flow; finality would need the stochastic entropy production as an added, honestly
flagged ingredient — and the fixed-`N` substrate is disclosure-regime (D-FORK lands finite-type)
unless cell-accretion is added.

**Loop-only Z/2 -> GU's `sigma`?** Same abstract Z/2, **not** the same physical bit: the holonomy
does not select the energy sign (both sectors positive-definite), whereas GU's `sigma` *is* the
energy-sign bit. Coincidence of type, not identity.

**What would move PARTIAL -> DELIVERS (the forcing conditions to pursue next):**
1. **Force the fluctuation identification instead of importing it.** Derive `Lambda := ` the
   entropy fluctuation *from the dynamics* (e.g. show the deterministic extensive mean is
   dynamically screened / cancelled by a constraint the specimen carries, leaving the fluctuation as
   the only physical residue) rather than asserting the Sorkin cancellation. This is the single
   highest-value follow-up and is exactly the cosmological-constant problem — so expect it hard.
2. **Add a cell-accretion dynamics (`N` grows)** to move the substrate into the Gödelian regime and
   convert record-change into finality — the D-FORK win.
3. **Fix `Theta` (the fluctuation scale) natively** rather than as a free parameter, so the
   *coefficient* (not just the exponent) is sourced — candidate: tie `Theta` to the discrete
   Dirac's spectral gap so the fluctuation temperature is set by `D`, not inserted.
4. **Cross-check against the DeWitt-measure route.** If that independent route also yields `-1/2`,
   bank the exponent as consilient; the two routes disagreeing would be an equally informative
   negative.

## 8. Provenance / boundary

Cross-repo material (the P2C specimen, the equation verification, the 9-item obligations) was
ingested and **re-verified here** with DU's own apparatus — the grades in this document are DU's,
not consumed on P2C's say-so (sovereign self-check). The P2C files were read, not edited. The probe
is stdlib+numpy, fixed seed, foreground, exit 0, 11/11 checks with real falsifier controls (the
`-1/2` test provably *can* fail — the global-mode control makes it). Nothing here is banked; this is
exploration tier and faces Lane 3 before any count. No commit/push, no external action taken.
```
Probe: python tests/bianconi_entropy_amplitude_probe.py   ->  exit 0, 11/11
```
