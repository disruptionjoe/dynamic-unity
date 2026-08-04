---
title: "Wave 3 adjudication: two-sided review of D1 and D2, and the three gated decisions"
status: exploration
doc_type: adjudication_note
created: 2026-08-03
session_note: >-
  The adjudication session opened on the campaign day (2026-08-03) and
  completed 2026-08-04 local. Filed under the campaign day per the directed
  path; this note corrects nothing dated and amends no receipt.
owner_repo: dynamic-unity
directed_by: "Joe direct chat, 2026-08-03 (Wave 3 adjudication of D1+D2; adjudication and rulings only — no commit of the reviewed results, no routing change, no banking)"
campaign: "Q-0063 decoherence-null confrontation (Wave 1b), Wave 3 per the DU wave scaffold"
frozen_plan: explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md
claim_grade: >-
  ADJUDICATION OF EXECUTED DISCRIMINATORS / VERDICTS READ AGAINST THE FROZEN
  §3 TABLES ONLY / INDEPENDENT RECOMPUTATION OF THE D2 WITNESS ARITHMETIC /
  THREE GATED RULINGS AS RECOMMENDATIONS / NO GRADE MOVEMENT, NO BANKING, NO
  REGISTER EDIT, NO PREDICTION, NON-ROUTING
banked: false
routing_note: >-
  This note routes nothing. CURRENT-RESEARCH.yaml remains the sole mutable
  authority for priority, WIP, execution, stops, reopeners, and successor
  selection. The three rulings below are reasoned recommendations against the
  frozen tables; each is Joe-gated through the contract, exactly as the wave
  scaffold specifies. No table is amended here; where a frozen table's
  antecedent is found unavailable, that is reported, not repaired.
lane_channel: "Lane 5 primary (Lanes 3, 4 supporting); CH-COLLIDE, CH-FORMAL, CH-MODEL"
inputs:
  - explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md (frozen plan; §3 tables are the sole verdict authority)
  - explorations/du-wave-scaffold-2026-08-03.md (Wave 3 charter: two-sided review, then three gated decisions)
  - explorations/classicality-transition-functional-form-d1-literature-check-2026-08-03.md (result under review; commit eb0d92f)
  - explorations/qd-sbs-audit-gap-witness-d2-execution-2026-08-03.md (result under review; commit 392cf0a)
  - tests/du_qd_sbs_audit_gap_witness_probe.py and tests/artifacts/du_qd_sbs_audit_gap_witness_result.json (witness and receipt; re-run at adjudication, 16/16, exit 0)
  - CURRENT-RESEARCH.yaml (read-only; state_revision 145)
---

# Wave 3 adjudication: D1 and D2

## 0. What this note is, and the discipline it runs under

The wave scaffold's Wave 3: a two-sided, absorber-first review of the two
executed discriminators, followed by the three gated decisions. Verdicts are
read **against the frozen §3 tables of the campaign plan only**. No table is
amended; per plan §6.1 a changed table is a new discriminator and the old one
banks as abandoned, so where a frozen antecedent turns out to be unavailable
this note *reports the unavailability* rather than rewriting the table.

The review is adversarial in both directions by construction. Section 2
attacks D2's kill on behalf of the null. Section 3 attacks D1's exclusions on
behalf of the mechanism trio. Neither section is permitted to reach a verdict
the frozen tables do not license.

Three coordinates: scope regional/public; status epistemic (this is a review
of executed work, not new physics); formation disclosure only.

**Independent-execution posture.** The D2 witness arithmetic was recomputed
from scratch for this adjudication — separate state construction (numpy state
vectors and eigendecomposition rather than exact `Fraction` partial traces),
plus an independently derived closed form for the entanglement certificate.
No routine from the probe was reused. The probe itself was also re-run
(16/16, exit 0). Results in §1.

---

## 1. Independent recomputation of the D2 witness

Every load-bearing number in the D2 note was recomputed by a method disjoint
from the probe's. All agree.

| Quantity | D2 note claims | Adjudication recomputation | Agree |
|---|---|---|---|
| spec ρ_S, W1 N=2 | {17/25, 8/25} | {0.68, 0.32} | yes |
| spec ρ_F = spec ρ_SF, W1 N=2 | {4/5, 1/5} | {0.8, 0.2} both | yes |
| Plateau identity I(S:F) = H(S), N=2 | exact | I − H(S) = 0 to machine precision | yes |
| H(S), N=2 | ≈ 0.9044 bits | 0.9043814577 | yes |
| χ = H(ρ_F), N=2 | 0.7219 bits | 0.7219280949 | yes |
| Audit gap H(S) − χ, N=2 | ≈ 0.1825 bits ≈ 20% of plateau | 0.1824533628 = 20.174% | yes |
| NPT compression determinant, N=2 | −576/15625 | −576/15625 | yes |
| ρ_SF entangled, N=2 | asserted via compression | min eig(ρ_SF^{T_S}) = −0.22557641 | yes (stronger) |
| Plateau identity, W1 N=4 half-fragments | exact, x = 9/25 | I − H(S) = 0; x = 0.36 | yes |
| Audit gap, N=4 | ≈ 0.0835 bits | 0.0834685273 | yes |
| NPT determinant, N=4 | −5992704/244140625 | −5992704/244140625 | yes |
| W2 conditional MI I(F₁:F₂\|S) | 1 bit, uniform in N ∈ {2,3,4} | 1.000000 at all three | yes |
| W2 independent-junk control | 0 bits | 0.000000 | yes |

The NPT determinant was not merely reproduced but derived in closed form.
Writing α = a^m (conditional fragment overlap) and β = a^{N−m} (residual
branch coherence on the fragment-plus-system block), the compression of the
partial transpose onto span{|0⟩(v−αu), |1⟩u} is

    G = [[0, ½β(1−α²)], [½β(1−α²), ½α²]],   det G = −¼ β² (1−α²)².

At N=2, m=1 (α=β=3/5) this is −576/15625; at N=4, m=2 (α=β=9/25) it is
−5992704/244140625. Both frozen values are exact and correct, and the
determinant is manifestly negative for every proper fragment with α < 1 —
so the entanglement rung of the audit does not depend on the particular
rational chosen.

**Verdict on arithmetic: clean.** No error found in the probe, the receipt,
or the note's quoted values. The `Fraction`-only discipline is real (no float
is load-bearing; the binary-entropy ordering lemma used in place of numeric
comparison is correct: h((1+x)/2) is strictly decreasing in |x|).

---

## 2. Charge A — attacking D2's kill

### 2.1 Is the witness in the frozen null's declared class? Split verdict.

**W1: yes, squarely.** The frozen plan §3 D2 names the admissible model class
as "(central-spin, collisional, QBM)". W1 is central-spin pure dephasing at
finite coupling time, realized by exact controlled rotations — the null's own
workhorse from plan §1 step 1, not a variant built for the occasion. The
class declared in the witness script header is therefore a *subset* of the
frozen list, which is the one refit test an adjudicator can run
independently of the author's attestation about ordering. It passes.

**W2: no — outside the frozen list.** W2's class is "environment fragments
carrying system-independent pre-existing classical correlations." That is
declared in the script header, but it is not central-spin, collisional, or
QBM; it is a hand-built classical fixture. Declaring a model class in the
witness does not extend the class the frozen plan named.

**Ruling.** W2 is **struck from the frozen-table verdict basis** and retained
as an illustrative fixture only. This costs the verdict nothing: the D2 note
had already demoted W2 on independent grounds (§6.4 — its independence
failure carries no system information, and whether that is an operational
objectivity failure or only an SBS-definition failure is exactly what the
Feller Comment/Reply dispute is about) and stated that "W1 is the
load-bearing witness and W2 is recorded as the independence-rung probe only."
The adjudication converts that self-demotion into a formal exclusion. The
branch-1 verdict stands on W1 alone.

### 2.2 Strawman test: does W1 instantiate what the null called vacuous?

The frozen null's step 4, verbatim: *"Auditing access and independence is
classical post-processing over the same physical state. It changes what an
observer may claim, never what the system does: no new parameter, no
dynamical term, no deviation in any functional form."*

W1 exhibits a state on which I(S:F) = H(S) holds *exactly* while three
separately measurable audit quantities fail by finite margins. The audit
verdict is therefore not recoverable by post-processing the
mutual-information data: two states can agree on the entire I(S:F) curve and
disagree on χ, on D = I − χ, and on conditional-state distinguishability.
Determining them requires *different measurements*, not further arithmetic on
the same ones. That is a direct hit on step 4 as frozen, not on a weakened
paraphrase.

**Not a strawman.** But the hit is narrower than "the audit layer is DU's":
see §2.5.

### 2.3 "Realizable scales" — honest, with two tightenings

The claim under attack: the witness protocol is not capability-locked, on the
strength of the 2025 superconducting experiment (Sci. Adv. 11, eadx6857;
arXiv:2504.00781; 12 qubits, 2 system + 10 environment, I, χ and D measured
separately).

Decomposing the requirement:

1. **Measurement of I, χ, D on system-plus-fragment blocks** — *directly
   demonstrated* by the cited experiment. This is the load-bearing component
   for W1 and it is honestly claimed.
2. **Preparation at partial coupling** (finite conditional overlap, i.e.
   incomplete decoherence). The cited experiment ran in an engineered
   good-decoherence regime, so it did *not* publish this regime. But a
   partial controlled rotation is a strictly weaker gate than the full one
   the experiment already executes. The capability claim is sound; it is,
   however, an inference from a strictly-weaker-gate argument, not a
   published measurement in the witness's own regime. That should be stated
   as such rather than folded into "demonstrated."
3. **Fragment-fragment conditional mutual information** I(F_j:F_k | pointer).
   The D2 note's blanket "all components are demonstrated laboratory
   measurements" overreaches here: the cited experiment reports
   system-fragment quantities, and the note's own supporting sentence names
   only "block tomography of 2–3 qubit S+fragment marginals." Fragment-pair
   conditional MI is plainly within a 12-qubit device's capability, but it is
   capability-inferred, not demonstrated. Immaterial to the verdict once W2
   is struck (§2.1), since this component belongs to the independence rung.

**Scale.** The D2 note justifies realizability as "N = 2–4 fragments … the
published experiments' own regime." Against a 10-environment-qubit
experiment that is a stretch on its face. The adjudication's own computation
(§2.4) *rescues and strengthens* the claim: the binding constraint is not
fragment number at all, and the witness extends cleanly to N = 12 and beyond.

**Verdict: honest.** With the two tightenings above recorded, and with the
stated justification replaced by the stronger one in §2.4.

### 2.4 The sharpened refuge — a new adjudication computation

The D2 note's two-sided §6.1 attributes the null's surviving corner to *large
fragments and large complements*: "Wherever both the fragment and its
complement are large, plateau and audit co-occur up to exponentially
vanishing corrections." Recomputation shows this diagnosis is **wrong in a
way that favours the null more than the facts require**.

Two exact structural facts about W1's family:

**(a) The exact plateau is a single fragment size.** I(S:F) = H(S) holds
exactly iff a^m = a^{N−m}, i.e. iff m = N/2. At N = 4 the fragments of size 1
and 3 are off the plateau by ∓0.244 bits; at N = 8 the size-1 fragment is off
by −0.278 bits. So the witness's "plateau" is a point, not a flat region —
the null proponent's §6.5 objection ("short plateaus") is correct as stated
and this adjudication upholds it.

**(b) The audit gap at that point is governed by residual system coherence,
not by fragment number.** Writing C = |⟨0|ρ_S|1⟩| = a^N/2 for the residual
coherence the environment has not yet destroyed:

- the Holevo access gap is H(S) − χ = h((1+a^N)/2) − h((1+a^{N/2})/2) → **C / ln 2** as C → 0;
- the conditional-state overlap (the distinguishability rung) is a^{N/2} = **√(2C)** — decaying only as the *square root* of the coherence, so it is the most robust of the three rungs;
- the entanglement negativity of ρ_SF stays O(0.2) across the whole range examined.

Numerically, at the exact-plateau fragment m = N/2:

| a | N | H(S) | audit gap | gap / H(S) | C | C / ln 2 | overlap |
|---|---|---|---|---|---|---|---|
| 0.6 | 4 | 0.98785 | 0.08347 | 8.45% | 0.0648 | 0.0935 | 0.360 |
| 0.6 | 8 | 0.99980 | 0.01195 | 1.19% | 0.0084 | 0.0121 | 0.130 |
| 0.6 | 12 | 1.00000 | 0.00157 | 0.16% | 0.0011 | 0.0016 | 0.047 |
| 0.9 | 8 | 0.86186 | 0.19972 | 23.17% | 0.2152 | 0.3105 | 0.656 |
| 0.9 | 12 | 0.94167 | 0.15627 | 16.60% | 0.1412 | 0.2037 | 0.531 |
| 0.95 | 12 | 0.77770 | 0.21357 | 27.46% | 0.2702 | 0.3898 | 0.735 |

Read the a = 0.9 and a = 0.95 rows against the a = 0.6 rows. At N = 12 — both
fragment and complement of size 6, neither small — the audit gap is still
17–27% of the plateau height. The co-occurrence the null needs is **not**
produced by large fragments. It is produced by **completed decoherence**.

This has three consequences, and they cut in both directions:

- **For D2 (favourable).** The witness is not confined to N = 2–4. Fix any
  fragment count the experiments can reach and choose the per-fragment
  coupling so that decoherence is incomplete; the exact plateau identity
  still holds at the half split and all three audit margins remain O(1). The
  realizability claim is stronger than D2 argued it.
- **For the null (favourable, and this is the honest price).** In W1's family
  the audit layer's empirical content is *proportional to the incompleteness
  of decoherence*. Once the environment has finished its work, C → 0 and the
  audit gap vanishes as C/ln 2. A null proponent's sharpest remaining line is
  therefore not "large environments" but: *the audit layer only has content
  before the record has actually formed* — which, they will say, is precisely
  where DU's own ladder does not yet license the word "record."
- **For D3 (decisive).** This converts a vague asymptotic worry into a
  quantitative target. See §4.

**Scope guard on (b).** This is a theorem about the pure symmetric branching
family, not about decoherence generally. The escape route is already pinned
in the D2 note: Le & Olaya-Castro's random-matrix result (PRA 98, 032103
(2018)) reports the discord fraction staying O(1) at large fragment fractions
in generic interacting dynamics. That pin is doing heavy lifting for the
generalization and it is *literature, not DU computation* — as the D2 note
itself concedes at §6.5. The adjudication upholds that concession and marks
it as the single largest unearned step in D2's reasoning.

### 2.5 Absorber-first pricing: exactly what survives as DU's

The D2 note's absorber-first block is correct as far as it goes ("the
DU-distinctive residue is the typed absorption, not novelty"). It is not
precise enough. Priced exactly:

**What is not DU's — everything physical.** The witnessed conditions are the
published SBS-over-QD conditions (Horodecki–Korbicz–Horodecki 2015;
Le–Olaya-Castro 2018/2019; Korbicz 2021). No mechanism, parameter, dynamical
term, functional form, prediction, or priority accrues to DU. Note further
that the Grade-4 banking the frozen table names — "selection/necessity **of
the audit conditions**" — is a grade on *those* conditions, i.e. on the SBS
literature's objects. DU does not own the banked object.

**What is DU's — one thing, stated exactly.** A **non-vacuity result for one
rung of the CCR ladder**: the rung `retained record ≠ independently
accessible record`. D2 shows the set of states that this rung separates is
non-empty *inside the null's own declared model class*, at realizable
parameters, with a finite measurement protocol. DU's claim on the result is a
*coincidence claim* — that its typed rung picks out exactly the SBS
conditions — not an ownership claim.

**Is the gain nonzero? Yes, and it is defensive.** Before D2 the live charge
against DU's ladder in this arena was vacuity: the null's step 4 said the
rung marks no physical difference. That charge is now refuted on the null's
home turf. Under the house rule that exact kills and absorptions credit as
results, a refuted defeater is a real return. But it *removes a defeater; it
adds no content*. DU leaves this arena smaller and cleaner, not larger.

**What D2 did not touch, and must not be read as covering.** The campaign's
own definition of the audit layer (plan §0) has three components: *physically
audited access + fragment independence + provenance*. D2 witnessed access
solidly; independence is struck (§2.1); **provenance was not witnessed at
all**. Provenance is where HC-DU-043's idle-versus-write fibre lives and is
arguably the rung DU cares about most. Any statement of the campaign result
must say "one of three declared audit components," never "the audit layer."

### 2.6 Ruling on D2

**Frozen table, branch 1 (kills the null, strong form): upheld, on W1
alone, with the scope stated as follows.**

> Within the frozen declared model class (central-spin dephasing at finite
> coupling time), there exist states on which the quantum-Darwinism plateau
> identity I(S:F) = H(S) holds exactly at the half-environment fragment while
> the audit conditions fail by finite, separately measurable margins, at
> fragment counts and with measurement capabilities the published experiments
> already possess. The frozen null's step 4 — that auditing is classical
> post-processing with no empirically distinguishable content — is **dead in
> its frozen form**.

Attached scope, binding on any downstream citation:

1. The verdict rests on W1; W2 carries no frozen-table weight.
2. The result covers the *access* component of the audit layer only.
3. The empirical content witnessed is published SBS physics; DU's share is a
   non-vacuity/coincidence result on one ladder rung.
4. In the declared family the audit margin is governed by residual system
   coherence C, vanishing as C/ln 2 — so the result is a statement about
   *decoherence in progress*, not about completed records.
5. The generalization beyond the branching family rests on a cited
   random-matrix result, not on DU computation.

Branch 2 was not available: it requires "proof (or exact computation over the
declared class) that the audit conditions co-occur with the plateau up to
corrections vanishing at observed redundancy scales," and the corrections
demonstrably do not vanish at observed scales — they vanish with decoherence
completeness, which is a different parameter. Branch 3 (capability-locked
formal excess) was correctly declined: the load-bearing measurements are
demonstrated.

---

## 3. Charge B — attacking D1's exclusions

### 3.1 Critical scaling — EXCLUDED does not overreach

The strongest available attack is that excluding a critical point requires
sweeping the control parameter through the region where the critical point
would sit, and the swept ranges are narrow (cat sizes n̄ = 3.3 to 5.1; a
factor ~2 in molecule internal temperature; a family of |Δα|). A metastable
threshold at 10⁶ amu or 10⁴ photons is untouched by this corpus. D1's
resolution-honesty paragraph answers this counterfactually ("a tipping point
with critical exponents inside the measured regimes would have produced curve
shapes these datasets could not have fit") — asserted qualitatively, not
quantified. That is the exclusion's soft spot and it is real.

**But the attack fails, on the signature's logical form.** The frozen
signature is a *conjunction*: "tipping point with critical exponents;
finite-size scaling; universality classes across microscopically unrelated
systems." Refuting any one conjunct excludes the signature. D1's third leg
refutes the universality conjunct directly and strongly: each platform's rate
is fixed by its own independently measured microphysics (cavity damping rate,
measured ion heating rate, calculated van der Waals cross-section), and
Turchette's engineered phase reservoir explicitly exhibits "no simple
universal scaling law for the functional form" while still matching
one-parameter theory. Shared exponents across microscopically unrelated
systems are not merely unobserved — the platform-specific rate structure is
positively incompatible with them at measured scales.

**Verdict: no overreach.** The exclusion rests on a solid conjunct
(universality) plus a softer one (non-analyticity within the swept range).
Recorded: the softer leg is judgment-grade and should not be cited alone.

### 3.2 Quorum — EXCLUDED does not overreach

The attack: only D1's third leg (quantum-Darwinism experiments, I versus
fragment size) measures the *participation* observable the signature names,
and that leg partly argues from what experimenters *reported* ("No discrete
participation threshold is reported on any of them") rather than from a
resolution analysis. With ~4–10 environment qubits the fragment-size axis is
coarse, and a steeply-rising-then-flat QD curve is not obviously
distinguishable from a step.

**The attack fails because legs 1 and 2 are themselves participation
counts.** In the collisional regime the participation variable is the number
of collisions, and visibility falls exponentially *from the first collision*
over a full decade of pressure — which excludes any quorum of N ≥ 2 (a quorum
would produce flat-then-drop). In the thermal regime the participation
variable is the number of emitted photons in the weak-fragment regime — the
regime where a participation jump would be *most* visible — and the measured
onset is gradual with the expected functional dependence across 1500–3000 K.
These are two microscopically unrelated platforms measuring participation
count at high resolution. The frozen table's "two or more independent
platforms with sufficient resolution" condition is met without leg 3.

D1's handling of the degenerate quorum-of-one case (recorded as a degeneracy
carrying no distinguishable mechanism content, not as a detection) is
correct: a mechanism that is empirically identical to the null in the regime
where it is tested has lost its empirical target, which is precisely the
frozen table's own language.

**Verdict: no overreach.** Recorded: leg 3 is corroborating and partly
report-based; the exclusion should be cited on legs 1–2.

### 3.3 Scope guard audit — carried everywhere it must be

The measured-regimes-only guard was checked at every point where a verdict is
asserted:

| Location | Guard present |
|---|---|
| §2 signature-1 verdict line | "excluded **at measured scales** on two or more independent platforms" |
| §3 signature-2 verdict line | "excluded **at measured scales**…" |
| §6 composite table, both EXCLUDED rows | "EXCLUDED **at measured scales**, ≥ 2 independent platforms" |
| §6 composite bullet 2 | "in the **measured regimes**" |
| §6 dedicated scope-guard bullet | enumerates the ranges and states "Nothing here extrapolates the exclusions to unmeasured macroscopic regimes" |
| §6 bullet 1 ("null survives D1 unwounded") | corpus-scoped ("anywhere in the corpus"), which is the correct scoping for a non-detection |
| §5 deviation sweep | corpus-scoped throughout |
| Not-established section | states the sweep may have missed platforms; absence from the sweep is not absence from the literature |

**No unguarded exclusion statement found.** The guard is carried
consistently, including in the one place it is easiest to drop — the summary
table.

### 3.4 The SILENT verdict is correctly not counted as an exclusion

Confirmed on both sides, which is the test that matters:

- **Not counted as an exclusion.** D1 §6 states it explicitly: "The full
  first-branch closure of the trio is *not* claimed: the merge leg is
  silence, not exclusion, and silence is not a verdict on the mechanism — it
  gates D6." The composite table types it as the third branch.
- **Not counted as support either.** Nowhere does D1 read the absence of an
  order-permutation experiment as evidence *for* the merge mechanism. The
  §4 analysis is entirely about the observable being wrong and the
  monotonicity leg being non-discriminating (and correctly notes that
  engineered-memory regimes show non-monotone revivals that standard
  open-system theory itself predicts — so "strict monotone convergence"
  cannot even be posed as a signature without a scoping the battery does not
  supply).

The exact missing measurement is recorded as the frozen third branch
requires, and it is specified tightly enough to be executable: one system
coupled sequentially to individually addressable fragments with mutually
non-commuting couplings, fragment order permuted between otherwise identical
runs at matched total interaction strength, pointer record compared across
orders.

### 3.5 Per-signature decomposition versus the trio-level table

Raised on the adjudication's own motion, because it is the one place D1 could
have quietly amended a frozen table. The frozen first branch is written for
the trio jointly ("sufficient resolution to exclude **the three** mechanism
signatures"). D1 applied the table per signature and took branch 1 for two
and branch 3 for one.

**Permissible, because it is strictly conservative.** D1 declines the first
branch's full consequent (trio-level closure) and therefore claims less than
the table would have licensed had all three excluded. A decomposition that
can only weaken the conclusion is not an amendment. One consequence must be
tracked: the first branch's clause "DU may continue only through D2/D3
(audit-content route), not through mechanism signatures" is in force for the
two excluded signatures but **not** for the merge signature, whose route
stays open via the third branch's "burden moves to D6." D1 §4 and §6 track
this correctly, and it is what makes gated decision 2 live at all.

### 3.6 Ruling on D1

**Both EXCLUDED verdicts upheld** at their stated scope; **SILENT upheld and
correctly typed**; **composite "null survives D1 unwounded" upheld** (branch
two did not fire anywhere in the corpus, which is all that "unwounded"
requires). Recorded weaknesses, neither of which changes a verdict: the
critical-scaling non-analyticity leg is judgment-grade, and the quorum leg 3
is partly report-based.

---

## 4. Gated decision 1 — D3 framing

### 4.1 First, a frozen-table finding that must be stated before framing

D3's frozen first branch reads: transfer succeeds → the audit layer is a
theorem, hence bookkeeping → "**combined with D2's second branch** this kills
DU's distinctive claim in the arena."

D2 did not take its second branch. **The conjunction the frozen table names
is therefore unavailable, and D3's first branch cannot fire its stated
consequent.** This is reported, not repaired: no table is amended here.

The substantive reason the table now under-describes the situation is simple
and should be stated plainly: *generic is not universal*. A genericity
theorem showing the audit conditions hold for most fragments under a channel
measure does not remove the empirical distinguishability of a preparable
state on which they fail. D2 answered the campaign's frozen question — does
the audit layer add empirically distinguishable content over raw redundancy —
in the affirmative, and no genericity result can retract that answer. What
D3 can still decide is the **scope and physical weight** of the content D2
established.

### 4.2 D3's question, framed precisely for the surviving refuge

Aimed at the corner §2.4 isolated:

> Do the Brandão–Piani–Horodecki generic-objectivity theorems and the
> Qi–Ranard strengthening, **under their exact assumptions**, entail that
> failure of the audit conditions — perfect fragment distinguishability,
> vanishing S:F discord, fragment independence — is bounded by a quantity
> that vanishes **at the same rate and with the same parameter** that makes
> the mutual-information plateau flat, **uniformly over the fragments an
> observer can actually access**, at physical rates and scales?

Equivalently, in the form the adjudication computation makes checkable: is
the relation *audit margin ≈ residual system coherence / ln 2 at the
plateau fragment* a theorem of channel structure, or an artifact of the pure
symmetric branching family?

The named assumption seams D3 must test are the four the plan already froze —
channel measure unphysical; "most fragments" ≠ the accessible ones;
outcome-versus-observable objectivity; rate/scale gap — plus the one §2.4
sharpens into a fifth and most decisive:

- **(e) the co-occurrence-rate seam:** do the theorems bound audit failure by
  a quantity co-vanishing with plateau flatness, or do the two quantities
  have independent scaling (as they do outside the branching family, if the
  random-matrix pin holds)?

House rule reasserted: **no cross-domain theorem by metaphor.** The transfer
succeeds only through the theorems' exact assumptions, and the plan's guard
stands unchanged — *a failed transfer is a result about the absorber's scope,
never positive evidence for DU.*

### 4.3 What each outcome does to the campaign

| D3 outcome | Frozen branch | Effect on the campaign |
|---|---|---|
| **Transfer succeeds** — audit failure bounded by plateau flatness, uniformly over accessible fragments, at physical rates | branch 1, consequent partly unavailable (§4.1) | D2's witness survives as a **preparable but atypical** corner of standard decoherence. DU's arena claim reduces to: the access rung is non-vacuous but generic-measure-small. Terminal verdict is a near-total absorption — but *not* the plan §7 amputation, whose antecedent ("the null survives D1, D2 and D3") is already false. |
| **Transfer fails at a named assumption** (including "the theorems are silent on specified accessible fragments," which is a failure at the most-fragments assumption, not a third branch) | branch 2 | The named gap becomes the precise surviving home of DU's claim, and plan §2(b) — "a proof that the genericity absorber does not cover the audit conditions at physical scales, leaving a named, non-vacuous empirical gap" — is satisfied. Combined with D2's witness this is the strongest outcome available to the campaign. Guard: still not positive DU evidence; the positive content remains published SBS physics. |

There is no third branch and none is invented: an indeterminate transfer maps
onto branch 2 by naming the assumption at which it stalls.

---

## 5. Gated decision 2 — D6 run-license

### 5.1 The license exists

D1's merge leg fired the frozen third branch, whose own text reads "burden
moves to D6." The license is therefore granted by the frozen table itself,
not by scaffold interpolation. The scaffold's gate ("granted only on D1
silence") is satisfied in the partial form D1 actually returned.

### 5.2 But D6-as-designed cannot discharge the burden that licensed it

Three independent reasons, each sufficient:

1. **Target mismatch.** The burden D1 transferred is *confluence* — order
   independence of the classical outcome under permutation of fragment
   decoherence order. D6's frozen table is a finite-size-scaling reanalysis:
   declare an order parameter and scaling family target-blind, then test for
   shared exponents. Scaling and confluence are different questions. D1 said
   this in §4 and the adjudication confirms it.
2. **Its mechanism target is already excluded.** D6's frozen table adjudicates
   the metastable/critical mechanism — the signature D1 §2 **excluded** at
   measured scales, on the same published corpus D6 would reanalyze. D6's
   first branch ("smooth system-specific curves → the metastable/critical
   mechanism fails") is now a restatement of a returned verdict, and its
   second branch ("shared exponents") was already swept in D1 §2 leg 3.
   Running it would spend an M-cost slot re-litigating a closed signature,
   with the residual risk that an unconstrained fit manufactures an anomaly
   the corpus does not contain.
3. **The empirical confluence leg is at the frozen hardware boundary.** D1's
   §4 established that no publication-grade order-permutation experiment
   exists. D6's own frozen hardware clause covers exactly this: "if published
   data cannot support the reanalysis, write exactly one awareness note (what
   a measurement would decide, minimum access, local fallback) and stop."

### 5.3 Redesign is not available

Plan §6.1: "Any change after a computation starts is a *new* discriminator
with a new table; the old one banks as abandoned, not amended." Rewriting D6
to target confluence would create a new discriminator and require a new
frozen table routed through the contract before any execution. It would also
duplicate D7, which already holds the theory-side confluence question with a
table frozen for it (§6).

### 5.4 Ruling

**D6 does not run as designed; it is not redesigned; the confluence burden
defers to a D7-shaped protocol.** Concretely, recommended to the contract:

- D6 closes **unexecuted and superseded** — not "abandoned," which the plan
  reserves for a discriminator stopped mid-run — with its frozen table intact
  and unamended, and with the reason recorded as §5.2 (2)+(3).
- The **theory-side** confluence burden routes to the D7 slot (§6).
- The **empirical** confluence burden is parked at the frozen hardware
  boundary, and **D1 §4 already is the one awareness note** the boundary
  permits: it names what the measurement would decide, the minimum access
  (individually addressable fragments with mutually non-commuting couplings
  and order permutation at matched total coupling), and the nearest existing
  capabilities (circuit-QED Darwinism setups; photonic cluster-state
  environments). No second note is authorized, and per the house rule the
  campaign does not circle the wall.
- If Joe instead wants a preregistered scaling reanalysis on its own merits,
  it enters as a **new** discriminator with a new two-sided table routed
  through CURRENT-RESEARCH.yaml — not as D6.

---

## 6. Gated decision 3 — D7 side-probe slot

### 6.1 The slot is filled, by D7 as frozen

The scaffold fills the slot only "if a mechanism-split survives adjudication
that D7's confluence counter-model would actually decide"; the plan adds that
D7 "may run only as the single bounded side probe and only when its outcome
would change a decision."

After D1, the merge mechanism is the **only** surviving member of layer D,
and it survives solely by silence on the wrong observable. D7's frozen table
closes it either way:

- *decoherence class is order-dependent exactly where a merge mechanism
  requires confluence* → the CRDT-merge mechanism is killed within the
  version space → layer D closes on "none" for all three signatures (two by
  exclusion, one by version-space kill);
- *decoherence class is provably confluent on the admitted class* → the
  confluence signature discriminates nothing and is struck from the battery →
  the last surviving mechanism loses its empirical target too.

Either branch empties layer D and terminates the mechanism route that D1's
SILENT verdict is currently holding open. That is a decision change, so the
discipline gate is passed.

### 6.2 The frozen D7 already matches D1's missing measurement

D7's frozen scope is "one exact small model (sequential noncommuting fragment
couplings)"; D1's missing-measurement specification is a system coupled
sequentially to individually addressable fragments with mutually
non-commuting couplings, order permuted at matched total interaction
strength. These coincide. **The theory-side confluence burden lands in D7
with no table amendment required** — which is what makes the §5.4 disposal of
D6 discipline-preserving rather than a workaround.

### 6.3 Guards attached to the fill

1. **D7 does not touch the null** (frozen text). Both branches are
   DU-negative or DU-neutral: neither can produce positive DU content. Running
   it is cleanup, not a bid. This is not a two-sidedness violation, because
   the plan types D7 as a within-version-space side probe rather than a
   discriminator; its two live sides are internal to the version space.
2. **Bounded at S.** One exact small model, inside the local computation
   boundary. No expansion, per plan §8.
3. **A battery correction banks as a battery correction**, not as a DU result.

### 6.4 Candidates rejected for the slot

- **A quorum-degeneracy probe** (does the quorum mechanism have any
  non-degenerate content, given D1 §3's quorum-of-one degeneracy?) — rejected:
  D1 already settled it. Quorum-of-one is empirically identical to the null
  where tested; quorum ≥ 2 is excluded. Nothing remains to decide, so it fails
  the "would change a decision" gate.
- **A witness-robustness probe** (does plateau-with-failed-audit survive
  outside the branching family — in the collisional or QBM classes the plan
  also named?) — this is the single most valuable unexecuted computation in
  the campaign, because §2.4 shows D2's generalization currently rests on a
  literature pin rather than on DU computation. But it is **not a
  mechanism-split question** and must not consume the mechanism-split slot;
  it is a D2 hardening that overlaps D3's remit. Recorded here as the
  strongest candidate for a *different* decision, and explicitly **not**
  proposed as a slot filler.

### 6.5 Ruling

**The single bounded side-probe slot is filled by D7 as frozen**, aimed at
the confluence question D1's third branch transferred, run as a within-
version-space splitter with the §6.3 guards. Activation is Joe's through the
contract.

---

## 7. Composite campaign position after D1+D2 — a Wave 5 preview

### 7.1 Where the campaign actually stands

- **Mechanism route (layer D).** Two of three signatures excluded at measured
  scales on ≥ 2 independent platforms each. The third is silent on the wrong
  observable, with its theory-side burden routed to D7 and its empirical leg
  parked at the hardware boundary. **The consensus-mechanism reading of DU's
  classicality claim has no live empirical target in existing data**, and D7
  will close the residue either way.
- **Audit-content route.** The frozen null's step 4 is dead in its frozen
  form. The access component of the audit layer has empirically
  distinguishable content at realizable scales, verified here by independent
  recomputation.
- **Absorber-first.** That content is published SBS physics. DU's share is a
  non-vacuity result on one ladder rung — a removed defeater, not added
  content. Independence is struck from the verdict basis; provenance was
  never witnessed.
- **The null's refuge, now quantified.** Not "large environments" but
  *completed decoherence*: in the declared family the audit margin tracks
  residual system coherence and vanishes as C / ln 2. Whether that is a
  theorem or a family artifact is exactly D3.

### 7.2 What D3 must show for the terminal verdict to go each way

**For the terminal verdict "the audit layer holds, at exactly its earned
grade":** D3 must fail transfer at a named assumption, and the named gap must
be one the accessible-fragment / physical-rate seam actually occupies. The
sufficient showing is: the BPH/Qi–Ranard theorems, under their exact
assumptions, do **not** bound audit failure of *specified accessible*
fragments by any quantity co-vanishing with plateau flatness — i.e. seam (e)
is open. Then the earned terminal statement is that the audit conditions are
selected/necessary content on the accessible-fragment class rather than
generic corollaries of channel structure, banked at the frozen table's Grade 4
*on the audit conditions*, with DU's share stated as the coincidence claim on
one rung and nothing more. Even this best case yields **no DU novelty, no
mechanism, and no prediction**.

**For the terminal verdict "near-total absorption":** D3 must succeed at
transfer in the strong form — audit failure bounded by plateau flatness,
uniformly over the accessible fragment set, at physical rates and scales.
Then D2's witness stands as a preparable, atypical, incomplete-decoherence
corner, and DU's distinctive reading of the audit layer as a separate
physical layer with independent content retires. The consensus-mechanism
reading is already dead by then via D1 and D7.

### 7.3 A frozen-text gap Wave 5 must handle honestly

Plan §7's terminal statement is conditioned on "If the null survives D1, D2,
and D3." **The null did not survive D2.** §7's antecedent is therefore false
and its licensed outcome is off the table by its own terms — including its
headline sentence that "the audit layer adds empirically distinguishable
content over raw redundancy" is dead. That sentence is now the *opposite* of
the executed result.

This is not a table breach: §7 is stakes prose ("The honest stakes — the
licensed outcome"), not a §3 pass/fail table, and no pass/fail table is
touched. But it means **no frozen text covers the branch the campaign is
actually on** — D2 branch 1 combined with either D3 outcome. Wave 5 must
write that terminal statement fresh and say plainly that it is doing so,
rather than reaching for §7's wording.

Two further §7 corrections Wave 5 should carry, both additive:

- The plan's §7 "what survives the amputation" paragraph and the yaml's
  `cheapest_kill` field both assert that the audit conditions "co-occur with
  raw redundancy at observed scales." That is now refuted at observed scales
  and holds only at completed decoherence. The correction is additive through
  this dated note and the live authority; nothing dated is edited.
- A null win can no longer be described as "the null survives D1–D3." The
  strongest remaining null outcome is *near-total absorption with the
  step-4 bookkeeping claim already lost*.

### 7.4 One state-hygiene observation, non-routing

`CURRENT-RESEARCH.yaml` at state_revision 145 still carries
`active_work_id: Q0063-D1-...`, `current_grade: "SCOPED CAMPAIGN, NOTHING
EXECUTED"`, and `successor_selection.blocked_by: Q0063-D1-...`, while D1 and
D2 are both executed and committed (eb0d92f, 392cf0a). Recorded as an
observation for Joe's next contract transition. This note makes no edit to
the live authority and asserts no obligation beyond the observation.

---

## 8. Frozen-table discipline audit of this adjudication

- **No table amended.** Where a frozen antecedent proved unavailable (D3
  branch 1's conjunction with D2 branch 2; plan §7's antecedent), the
  unavailability is reported and the table left intact.
- **No branch invented.** D3 keeps two branches; an indeterminate transfer is
  mapped onto branch 2 by naming the stalling assumption.
- **Absorber-first.** Every positive statement in §2 is standard
  quantum-information physics; no DU-distinctive wording is used in any
  verdict; §2.5 prices the concession explicitly.
- **Two-sided.** §2 attacks D2 on the null's behalf and found two real
  defects (W2's class membership; the independence-measurement capability
  claim) plus one favourable correction (§2.4). §3 attacks D1 on the
  mechanisms' behalf and found two soft legs. Neither section was permitted
  to reach a verdict the tables do not license.
- **Independent verification.** D2's arithmetic recomputed by a disjoint
  method and the entanglement certificate derived in closed form; the probe
  re-run (16/16, exit 0).
- **Rulings are recommendations.** All three gated decisions are Joe-gated
  through CURRENT-RESEARCH.yaml, per the wave scaffold's governance clause.

## Not established

This note establishes no new physics and moves no grade. It banks nothing:
D1's and D2's verdicts remain unbanked and their banking is Joe's decision
through the live authority. The recomputation in §1 verifies D2's arithmetic;
it does not independently verify D2's literature reconstruction, which was
accepted at the executing note's stated grade. The §2.4 scaling relation is a
statement about the pure symmetric branching family only, computed here, and
is not a claim about decoherence generally; its extension rests on the cited
random-matrix result, which this adjudication did not re-derive. The claim
that D2's model class and witness form were frozen *before* computation
rests on the executing note's attestation; what is independently checkable —
that the declared class is a subset of the frozen plan's named list — was
checked and passes for W1 and fails for W2. The three rulings are reasoned
recommendations, not activations. No commit of the reviewed results, no
register edit, no prediction entry, no paper posture, no cross-repository
authorization, and no hardware or provider work follows from this note.

## Provenance

Internal:

- `explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md` (frozen plan; §3 tables, §6 discipline, §7 stakes prose)
- `explorations/du-wave-scaffold-2026-08-03.md` (Wave 3 charter and gating structure)
- `explorations/classicality-transition-functional-form-d1-literature-check-2026-08-03.md` (D1, commit eb0d92f)
- `explorations/qd-sbs-audit-gap-witness-d2-execution-2026-08-03.md` (D2, commit 392cf0a)
- `tests/du_qd_sbs_audit_gap_witness_probe.py`; `tests/artifacts/du_qd_sbs_audit_gap_witness_result.json` (re-run at adjudication: 16/16, exit 0)
- `explorations/external-mergeable-sector-theorem-spine-and-taf-record-typing-absorption-2026-08-03.md` (Wave 1a; sharpened null and audit ladder)
- `CURRENT-RESEARCH.yaml` (read-only, state_revision 145)

External, consumed by pointer at the executing notes' stated grades and not
re-verified here: Horodecki–Korbicz–Horodecki PRA 91, 032122 (2015);
Le & Olaya-Castro PRA 98, 032103 (2018) and PRL 122, 010403 (2019);
Feller Comment PRL 126, 188901 (2021) and Reply; Korbicz, Quantum 5, 571
(2021); Sci. Adv. 11, eadx6857 (2025) / arXiv:2504.00781; Brandão–Piani–
Horodecki Nat. Commun. 6, 7908 (2015) and Qi–Ranard (2021); and the D1
decoherence corpus as listed in that note's Provenance.
