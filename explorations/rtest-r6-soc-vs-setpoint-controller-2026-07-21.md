---
title: "R-TEST #3 (the load-bearing lever): can the R6 record-issuance magnitude be SOURCED by a set-point-free SOC controller, or is it inescapably re-imported by a PID/difficulty set-point?"
status: active_research
doc_type: exploration
lane: "2.2 -> 1.3 (candidate-unification lever feeding the native DE amplitude) — Test #3, the LOAD-BEARING magnitude-sourcing fork of the incentive-selection mode-issuance candidate"
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (pre-registered swing; the load-bearing lever for the incentive-selection candidate)"
posture: "open exploration; honesty bites at the banking gate; adversaries (esp. Adversary-C) are terrain to beat, not gates; anti-toy (a concrete record-issuance dynamics with feedback, not a metaphor). Sovereign self-verification: the SOC/absorbing-state and difficulty-adjustment machinery is standard-field material, ingested and RE-VERIFIED here with DU's own probe, never adopted on say-so."
runnable: tests/du_soc_vs_setpoint_controller_probe.py
probe_exit: "0 (11/11 checks pass; deterministic seed; numpy + stdlib; foreground ~15 s)"
artifact: tests/artifacts/du_soc_vs_setpoint_controller_probe_result.json
verdict: "PARTIAL — set-point-free SOC genuinely SOURCES a critical point + a native power law (the 'inescapably a PID / re-imported' wall FALLS), but the native exponent is tau~3/2 not 1/2, the 1/sqrt(N) reappears only under ADDITIVE counting (no sourced coefficient), and scale-freeness structurally forbids a sourced magnitude. The wall relocates from 'must import a set-point' to 'a scale-free mechanism cannot hand you a scale'."
grade: "exploration / load-bearing-lever result. COMPUTED (deterministic, this swing): a set-point-free flux-balance controller self-organizes to sigma_c=1 (the branching map's absorbing-state transition) from both sides, drive-rate-invariantly (sigma_c=drive^{1/n}, verified vs prediction); the PID positive control regulates to the imported set-point (<0.5% miss); the native SOC avalanche exponent tau=1.48 (~3/2); the additive count self-averages at slope -0.499; the SOC cascade tail index alpha~0.53 (<1, infinite-mean); the exponent invariant under microscopic-unit rescale while the additive 1/sqrt(N) prefactor is window-dependent. No claim banked."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
inputs:
  - explorations/incentive-selection-mode-issuance-candidate-2026-07-21.md   # Test #3 — the load-bearing lever
  - explorations/flip-witness-algebra-requirements-2026-07-21.md             # R6: non-additive count with a SOURCED coefficient
  - explorations/bianconi-entropy-amplitude-route-2026-07-21.md              # wave-1: exponent native, value imported
  - explorations/de-amplitude-dewitt-route-2026-07-21.md                     # wave-1: additive/ultralocal -> import
---

# R-TEST #3 — SOC (set-point-free) vs PID (imported set-point): can R6's magnitude be sourced?

**Bottom line up front.** The R6 record-issuance controller is **NOT inescapably a PID**. A
genuinely **set-point-free** controller exists and works: a flux-balance feedback that contains
**no target value** self-organizes to the branching map's critical point `sigma_c = 1` and
generically produces a power law — the critical point and the exponent are **SOURCED**, not
imported. That is a real result and it **falls the wall** as the candidate stated it ("regulates
to an *imported* target ... so the coefficient is RE-IMPORTED"). **But** the magnitude R6
actually wants — `Lambda ~ 1/sqrt(N)` with a *sourced coefficient* — is **not** delivered by this
route, for two independent reasons the probe makes precise:

1. **The native SOC exponent is `tau ~ 3/2`, not `1/2`.** It is an avalanche-*size* exponent,
   and `tau > 1` is forced for any normalizable size distribution — so **`1/2` can never be an
   SOC avalanche-size exponent.** The `1/2` reappears only under **additive** (independent)
   counting, i.e. the ordinary CLT / standard-error exponent — which is exactly the **wave-1
   route** (Bianconi/DeWitt), native but additive, and carrying **no sourced coefficient**. The
   genuinely **non-additive** count R6 demands is heavy-tailed (`alpha = tau-1 ~ 1/2`,
   infinite-mean) — a `1/2` of the **opposite character** (extreme-dominated, not a small
   self-averaging fluctuation).
2. **A scale-free mechanism cannot source a coefficient.** SOC's power comes precisely from
   having *no characteristic scale*: the exponent is invariant under rescaling the microscopic
   issuance unit. For that same reason it **cannot output a magnitude**. The wall therefore does
   not disappear — it **relocates**, from "you must import a set-point" (which SOC refutes) to
   "a scale-free mechanism has no scale to hand you."

**Grade: PARTIAL** (per the pre-registration: *SOC works but the exponent/value isn't
`1/sqrt(N)`*), but a **sharp and informative** PARTIAL: it converts the candidate's open Test #3
into a precise structural statement, and it moves one real thing forward — a **set-point-free
sourcing mechanism** for the critical point and the exponent, which wave-1 lacked (wave-1 had the
CLT exponent but no dynamical mechanism, and no answer to "is the controller forced to import a
target?"). Receipt: `tests/du_soc_vs_setpoint_controller_probe.py`, deterministic, numpy+stdlib,
**run 2026-07-21, exit 0, 11/11 checks**, with a POSITIVE CONTROL and real falsifier controls.

---

## 1. The fork, stated so the traps are visible

R6 (flip-witness-algebra-requirements) demands a **non-additive count with a SOURCED
coefficient**: `Lambda ~ 1/sqrt(N)` must carry a *derived* coefficient, not an imported one. The
incentive-selection candidate (Test #3) framed the decisive question sharply: the DE magnitude
machinery is a **record-issuance-rate controller**; is it

- **SOC-like / set-point-FREE** — finds its critical point from the dynamics, generically
  yielding a power law, so the coefficient is **SOURCED**; or
- **inescapably a PID / difficulty-adjustment** controller — regulates to an *imported* target
  (Bitcoin's 10-minute block time is a design constant), so the coefficient is **RE-IMPORTED**
  (the wall)?

Bonus: does an SOC route yield `~1/sqrt(N)` natively?

The two pre-registered lethal outcomes were **SOURCED** (set-point-free SOC self-tunes with no
imported target and the scaling is native — *flag loudly if the exponent is ~1/2*) and
**RE-IMPORTED** (every controller that hits the right magnitude smuggles a set-point/scale), with
**PARTIAL** = "SOC works but the exponent/value isn't `1/sqrt(N)`."

## 2. The build (anti-toy): a concrete record-issuance dynamics with feedback

Records issue in **avalanches** (bursts of ledger writes) on a **branching frontier**. Each
active record triggers `Binomial(2, sigma/2)` downstream records — mean **branching ratio
`sigma`** (downstream records per record). The frontier runs to a depth `n` with **boundary
dissipation**: records still active at the boundary *settle/finalize* and leave. `sigma_c = 1`
is the **absorbing-state (extinction) transition** of the branching map — the point where
avalanches marginally span the system. This is not a toy identity `H:=D`; it is a genuine
stochastic issuance dynamics with a genuine control parameter and a genuine phase transition.

Two controllers act on `sigma` (SOC) or on an issuance rate (PID):

- **SOC — set-point-FREE (the candidate for SOURCED).** Pure **flux balance**, dissipation
  averaged over a window:
  ```
  sigma  <-  sigma + eta * ( drive  -  <dissipated_out>_window )
  ```
  **There is no target value of `sigma` anywhere in this rule.** Its fixed point is where in-flux
  equals out-flux. Because `E[dissipated] = E[active at boundary] = sigma^n`, balance forces
  `sigma^n = drive`, i.e. `sigma_c = drive^{1/n}`.
- **PID / difficulty-adjustment — the POSITIVE CONTROL (the wall).** The **Bitcoin rule**
  `D <- D * (rate_observed / rate_TARGET)^gain`. The **target rate is a design constant that
  literally appears in the update.** Regulated rate → target for *any* target.

## 3. Results (probe, 11/11, exit 0)

### 3.1 The set-point-free controller self-organizes to the critical point — SOURCED
The flux-balance feedback converges to `sigma_c = 1.000` (from below, start 0.5) and `1.002`
(from above, start 1.5): a genuine **two-sided attractor at the critical point, with no target in
the rule.** The critical value is the branching map's **absorbing-state transition**, *derived*,
never inserted.

**Drive-rate invariance (the decisive check that `sigma_c` is not a smuggled scale).**
`sigma_c = drive^{1/n}`, verified against prediction:

| `n` | `sigma_c(drive=0.5)` measured | predicted `0.5^{1/n}` |
|----|----|----|
| 6  | 0.894 | 0.891 |
| 10 | 0.936 | 0.933 |
| 16 | 0.956 | 0.958 |

`sigma_c` is **not** the drive value (0.5); halving the drive leaves `sigma_c` near 1, and
`sigma_c -> 1` as `n` grows regardless of drive. The drive sets only a **vanishing finite-size
correction**, never the critical value. **This is the crux: the number `1` is not in the
controller — it is a property of the dynamics.** Contrast the PID, whose target sits *inside* the
update rule.

### 3.2 POSITIVE CONTROL — the PID regulates to the imported set-point
| target `r*` | regulated rate | miss |
|----|----|----|
| 5.0  | 5.03  | 0.5% |
| 12.0 | 12.05 | 0.4% |
| 30.0 | 30.05 | 0.2% |
| 80.0 | 80.03 | 0.0% |

The regulated value **equals the imported set-point** for every target (max miss 0.5%); the
magnitude is imported by construction. This is the contrast that makes "SOC sources it"
meaningful — and it is exactly the RE-IMPORTED outcome, realized **only** for the PID, **not** for
the SOC controller.

### 3.3 Native power law at the self-organized point — SOURCED exponent (but it is 3/2)
At `sigma_c = 1` the avalanche-size PDF is the universal **mean-field power law `tau = 1.480`
(~3/2)** (Otter–Dwass critical-branching total-progeny law). The off-critical control (fixed
`sigma = 0.8`, no self-organization) has a **finite characteristic size ~`1/(1-sigma) = 5`** and
**no scaling window** — so the power law is genuinely a fruit of the self-organization, not put in
by hand. **The `tau` test can fail (and does, off-critical): it has teeth.**

Crucial ceiling: **`tau > 1` is forced** for any normalizable size PDF (`s^{-1/2}` is not
normalizable on `[1, infinity)`), so **`1/2` is never an admissible SOC avalanche-size exponent.**

### 3.4 The `1/sqrt(N)` fork — additive gives it, non-additive doesn't
- **(a) ADDITIVE count** (independent branching lines): relative-fluctuation slope vs `N0` =
  **−0.499** — the CLT / standard-error exponent. This is `1/sqrt(N)` **natively**, but it is the
  **additive** route: precisely the wave-1 (Bianconi extensive `Tr ln G`, DeWitt ultralocal)
  structure, which the wave-1 swings already found delivers the **exponent** but **imports the
  value**.
- **(b) NON-ADDITIVE SOC cascade** (the correlated avalanche R6 actually wants): tail index
  `alpha = tau - 1 ~ 0.53` (Hill, top decile), CCDF slope **−0.491**. So a **`1/2` does appear**
  in the SOC route — the heavy-tail index — but with **`alpha < 1` (infinite mean,
  extreme-dominated)**: a `1/2` of the **opposite character** to the DE's small, self-averaging
  standard-error fluctuation.

**Reading:** the DE's `1/sqrt(N)` needs **additivity**; the genuinely **non-additive** count R6
demands carries a heavy-tail `1/2` that is not a self-averaging amplitude. **Non-additivity and
`1/sqrt(N)`-as-a-small-fluctuation are in tension** in this route.

### 3.5 The coefficient is not sourced — scale-freeness (the wall relocates)
Rescaling the microscopic issuance unit (`x7.3`) leaves the exponent **invariant** (`tau: 1.480 ->
1.480`): SOC is **scale-free**, with *no characteristic magnitude*. For that same reason it
**cannot output a coefficient.** And even the additive `1/sqrt(N)` prefactor `sqrt(t*v)` is
**scheme-dependent** — it rides on the observation window `t` (`1.41, 1.99, 2.77` for `t = 4, 8,
16`), a modeling choice, not criticality. So **no route here sources the magnitude.**

## 4. Inline DU board (personas as lenses; computation disposes)

- **Dynamical Systems (SOC, absorbing-state transitions) — lead.** `sigma_c = 1` is the
  extinction/absorbing-state transition of the branching map; the drive–dissipation flux balance
  *pins* the system to it — textbook SOC-as-self-tuned-absorbing-state (Dickman–Muñoz–
  Vespignani–Zapperi). The self-organization is **real and set-point-free**; the sharp caution it
  raises itself: the self-organized point is critical only because the *deterministic* fixed point
  is `sigma^n = drive` — fluctuation kicks pull it subcritical unless the feedback is gentle
  (windowed), an honest finite-system feature, not a defeater. Verdict: SOURCED for the critical
  point.
- **Information Geometry (Fisher / `1/sqrt(N)` flavor).** The `1/sqrt(N)` is the Cramér–Rao /
  standard-error exponent — Fisher information from `N` independent contributions adds as `N I_1`.
  That is **additive** by construction, which is *why* it is generic and *why* it carries no
  sourced coefficient. Exactly as in the DeWitt route, the info-geometry lens **explains the
  obstruction** rather than rescuing it: the geometry that gives `1/sqrt(N)` is additive; making
  the count non-additive (SOC) *destroys* the clean `1/sqrt(N)`.
- **Metrology / Invariance (is the exponent a real invariant or a coordinate artifact?).** The
  exponents (`tau = 3/2`, `alpha = 1/2`) are **scale-free invariants** — they survive rescaling of
  the microscopic unit (probe Part 5). But a *coefficient* is, by definition, **not** invariant
  (it is the scale you rescaled away). So SOC **invariantly sources the exponent** and
  **invariantly cannot source the coefficient.** This is the decisive lens: it is not that we
  failed to find the coefficient — a scale-free mechanism *provably has none to give*.
- **Metabolic Scaling (non-additive vs counting).** SOC finally delivers the **genuinely
  non-additive count** the DeWitt route could not (ultralocal → additive → `sqrt(N)` with a
  constant prefactor, the exact failure mode). SOC avalanches are correlated cascades, heavy-
  tailed — non-additive in the strong sense. **But** the non-additive exponent is `3/2` (and the
  tail `1/2` is infinite-mean), so non-additivity buys a power law, **not** the small
  `1/sqrt(N)` amplitude. The "is the count non-additive or absorbed by counting?" absorber is
  *passed* (genuinely non-additive) — and that very success is what moves the exponent off `1/2`.
- **Adversary-C (strongest-form kill: "every set-point-free story secretly imports a scale").**
  Two moves. (a) *"`sigma_c = 1` is a target in disguise."* **Rebutted:** the number `1` is not in
  the update rule; it is the branching map's critical eigenvalue, and the drive-rate-invariance
  table (`sigma_c = drive^{1/n}`, not `= drive`) shows the controller finds it without holding it.
  (b) *"the microscopic unit / the drive / the system size is the imported scale."* **Conceded —
  and this is Adversary-C's genuine win, on the coefficient:** SOC sources the *dimensionless*
  structure (critical point, exponents) but any *dimensionful magnitude* rides on the microscopic
  scale (lattice/Planck), which SOC does not source. So Adversary-C **loses on the
  exponent/critical-point** (a real set-point-free sourcing exists) and **wins on the
  coefficient/value** (a scale-free mechanism cannot produce a scale). That split *is* the result.

**Council synthesis:** unanimous **PARTIAL**, with a precise decomposition — SOURCED for the
set-point-free critical point and the power-law exponent (the "inescapably a PID" wall falls),
NOT sourced for the `1/2` exponent (it is `3/2`; `1/2` needs additivity) and NOT sourced for the
coefficient (scale-freeness). The two lenses with the best chance of a native win
(Information-Geometry and Metrology) both **actively explain the obstruction**.

## 5. Honest outcome, and what survives

**PARTIAL.** Answering the three questions the swing was to settle:

1. **Can the magnitude be SOURCED by a set-point-free SOC controller, or is it always
   re-imported?** The **controller is not inescapably a PID** — a genuinely set-point-free
   flux-balance controller self-organizes to the critical point with no imported target
   (drive-rate-invariant `sigma_c = drive^{1/n} -> 1`). So *"every controller that hits the
   magnitude smuggles a set-point"* is **false**, and the **critical point + power-law exponent
   are sourced.** But the **coefficient/value is not sourced by any route here**: SOC is
   scale-free and structurally cannot output a magnitude; the additive route that does give
   `1/sqrt(N)` carries only a scheme-dependent prefactor. The wall **relocates** rather than
   falls: from *"import a set-point"* to *"a scale-free mechanism has no scale to hand you."*
2. **Is the native exponent `~1/2`?** **No, not as the DE wants it.** The native SOC exponent is
   `tau ~ 3/2` (an avalanche-size exponent; `tau > 1` is forced, so `1/2` is impossible as a size
   exponent). A `1/2` appears in two places, both the *wrong* character for the DE: the
   **additive CLT** relative-fluctuation exponent (self-averaging, but additive = the wave-1
   route, no sourced coefficient), and the **SOC heavy-tail index** `alpha = tau-1 ~ 1/2`
   (infinite-mean, extreme-dominated — the opposite of a small amplitude).
3. **The grade.** **PARTIAL**, matching the pre-registration ("SOC works but the exponent/value
   isn't `1/sqrt(N)`"), sharpened into a structural finding.

**What this moves (and what it does not).** It does **not** move canon, claim status, or posture,
and it does **not** touch the Krein **sign** (`sigma`, external — untouched throughout; the target
was the magnitude). It **does** advance the incentive-selection candidate's open **Test #3** from
a question to a precise answer, and it isolates the real obstruction for R6's *coefficient*: the
route that sources the *mechanism* (SOC, non-additive, set-point-free) is exactly the route that
*cannot* source the *scale*, and the route that gives `1/sqrt(N)` (additive CLT) is the already-
known wave-1 route with an imported value. **The one reopening condition that survives:** an SOC-
like route delivers the DE **value** only if a **second, scale-fixing ingredient** (a
dimensionful input the dynamics genuinely sources — e.g. the `D`-spectral-gap tie R6 gestures at,
tying the microscopic issuance unit to a sourced spectral scale) is added *on top of* the set-
point-free criticality. That ingredient is downstream of the same B5/source-action bottleneck the
wave-1 routes hit; it is not available at current grade. Until then the DE **coefficient** stays a
pure import, while the **exponent** now has a genuine set-point-free **mechanism** (a real gain
over wave-1's bare CLT).

## 6. Boundary / provenance

New files only: this exploration and `tests/du_soc_vs_setpoint_controller_probe.py` (+ its JSON
artifact under `tests/artifacts/`). No existing file edited; **nothing committed or pushed** (per
instruction); nothing external. The SOC / absorbing-state and Bitcoin-difficulty machinery is
standard-field material, **ingested and re-verified here** with DU's own probe under the sovereign
self-verification rule — consumed as source and re-checked, never adopted on say-so. The probe is
a disprove-or-confirm instrument, not a fit: it carries a **POSITIVE CONTROL** (the PID hits the
imported set-point) and real falsifier controls (the off-critical `sigma` has a characteristic
scale; the `tau` test can and does fail off-critical). Deterministic seed, numpy+stdlib,
foreground, exit 0, 11/11. No `claim_status_change`, `canon_verdict_change`, or
`public_posture_change`. This is an exploration-tier, load-bearing-lever result offered as a
PROPOSAL for the candidate's Test #3; it invites hostile re-verification.

```
Probe: python tests/du_soc_vs_setpoint_controller_probe.py   ->  exit 0, 11/11
```
