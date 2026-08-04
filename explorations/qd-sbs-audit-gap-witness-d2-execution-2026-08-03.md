---
title: "D2 executed: the QD/SBS audit-gap witness — exact plateau-with-failed-audit states at realizable scales"
status: exploration
doc_type: discriminator_execution_note
created: 2026-08-03
owner_repo: dynamic-unity
directed_by: "Joe direct chat, 2026-08-03 (D2 execution authorization; no commit)"
campaign: "Q-0063 decoherence-null confrontation (Wave 1b), discriminator D2"
frozen_plan: explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md
claim_grade: >-
  EXECUTED DISCRIMINATOR / EXACT FINITE WITNESS + PRIMARY-SOURCE LITERATURE
  RECONSTRUCTION / VERDICT PER FROZEN TABLE / NO GRADE MOVEMENT, BANKING,
  REGISTER EDIT, ROUTING CHANGE, OR PREDICTION ENTERED BY THIS NOTE
banked: false
routing_note: >-
  This note routes nothing. CURRENT-RESEARCH.yaml remains the sole mutable
  authority. Banking the result at the frozen table's named grade, any
  register annotation, and the prediction-register handoff the table names
  are Joe's decisions through the live authority.
witness_script: tests/du_qd_sbs_audit_gap_witness_probe.py
witness_receipt: tests/artifacts/du_qd_sbs_audit_gap_witness_result.json
---

# D2 executed: the QD/SBS audit-gap witness

## 1. What ran, under what contract

Discriminator D2 of the frozen campaign plan (§3, "the central
discriminator"), executed exactly against its preregistered pass/fail
table. The table was frozen in the plan before any computation; nothing
below amends it. The declared model class and witness form (central-spin
pure dephasing via exact controlled rotations; exact rational density
matrices with every verdict inequality certified in `Fraction`
arithmetic) were frozen in the witness script's header before the
computation ran. No interface was refit mid-run.

The sharpened null under test (TaF T1 typing, plan §0–§1): *the audit
layer — physically audited access + fragment independence +
distinguishability, the conditions that turn raw environmental redundancy
into an admissible record — is bookkeeping over one and the same physical
process, with no empirically distinguishable content over the raw
quantum-Darwinism mutual-information plateau.*

Witness: `tests/du_qd_sbs_audit_gap_witness_probe.py` — 16/16 checks,
deterministic byte-identical receipt
`tests/artifacts/du_qd_sbs_audit_gap_witness_result.json`, exit 0; hard
`AssertionError` (nonzero exit) on any failed check. Run:

```bash
python3 tests/du_qd_sbs_audit_gap_witness_probe.py
```

Standard library only; no numerics, no seeds, no floats in any
load-bearing comparison.

## 2. The witness states, exactly

**W1 — discord/distinguishability rung (finite-time central spin).**
The branching state |Ψ⟩ = (|0⟩|φ₀⟩^⊗N + |1⟩|φ₁⟩^⊗N)/√2 with exact
rational overlap a = ⟨φ₀|φ₁⟩ = 3/5, produced exactly by controlled
rotations R = [[3/5, −4/5], [4/5, 3/5]] acting on |+⟩_S|0…0⟩ — the
finite-coupling-time snapshot of the standard central-spin dephasing
Hamiltonian, i.e., the same circuit family the published QD experiments
implement.

- **N = 2:** every proper fragment satisfies the quantum-Darwinism
  condition **I(S:F) = H(S) exactly** (certified by exact spectral
  multiset equality: spec ρ_F = spec ρ_SF = {4/5, 1/5}, spec ρ_S =
  {17/25, 8/25}). Raw redundancy: 2 disjoint fragments, each at the full
  plateau height H(S) ≈ 0.9044 bits. Meanwhile every audited condition
  fails by a finite exact margin:
  - conditional fragment states overlap 3/5 ≠ 0 (one-shot perfect
    distinguishability fails);
  - ρ_SF is entangled — exact NPT certificate: the 2×2 compression of
    the partial transpose has determinant **−576/15625 < 0** — hence the
    S:F quantum discord is strictly positive in both directions (SQD
    fails);
  - the pointer information accessible from a fragment is
    Holevo-bounded by h(4/5) = 0.7219 bits, strictly below the plateau:
    audit gap **H(S) − χ = h(17/25) − h(4/5) ≈ 0.1825 bits ≈ 20% of the
    plateau height**, certified exactly via the binary-entropy ordering
    lemma (no floating point load-bearing).
- **N = 4** (the scale of the photonic experiments): the two disjoint
  half-environment fragments sit **exactly** on the plateau
  (spec ρ_F = spec ρ_SF, x = 9/25) while all three audit margins remain
  finite (conditional overlap 9/25; NPT determinant −5992704/244140625;
  access gap ≈ 0.0835 bits).

**W2 — fragment-independence rung (perfect records + correlated junk).**
ρ = ½ Σᵢ |i⟩⟨i|_S ⊗ |i⟩⟨i|_{R₁} ⊗ … ⊗ |i⟩⟨i|_{R_N} ⊗ γ_{J₁…J_N}, with
γ a shared classical coin copied into every fragment's junk register and
never coupled to S; fragment F_k = (R_k, J_k). Exact results, uniform in
N ∈ {2, 3, 4}: the plateau is exact for every fragment and for the joint
fragment pair (I = H(S) = 1 bit); distinguishability is perfect; all
discords vanish (diagonal embedding); yet the SBS product form fails
exactly — conditional fragment-pair mutual information
**I(F₁:F₂ | pointer) = 1 full bit at every tested scale**, and the
pointer decomposition is unique (disjoint record supports), so no
alternative decomposition rescues the product form. This defeats the
null's "corrections vanishing at observed redundancy scales" branch for
the independence rung specifically: the failure margin is
scale-uniform, not vanishing.

**Controls (falsifiability of the witness itself).** The ideal SBS state
(a = 0) passes every audit; an asymmetric branching state (overlaps 3/5
vs 24/25) breaks the exact plateau identity; independent junk passes the
independence audit with conditional mutual information 0. The witness
checks can fail; they are not vacuous.

## 3. Literature reconstruction (primary sources, per the plan's pin duty)

- **QD condition and the strict gap.** Korbicz's review (Quantum 5, 571
  (2021); arXiv:2007.04276) states the QD condition as
  I(ρ_{S:fE}) = H(ρ_S) independently of f (its Definition 2) and, on the
  gap: *"That SBS states imply quantum Darwinism condition (1) is a
  simple calculation, however the opposite implication turned out to be
  a difficult mathematical problem. As was shown in Section IV,
  condition (1) [is] too weak to impose SBS structure."* Also: *"the
  presence of discord prevents operational checking for (1) using local
  measurements."* (Both quotes verified from the arXiv v2 text.)
- **The decomposition and realizable non-ideal dynamics.**
  Le & Olaya-Castro, PRA 98, 032103 (2018) (arXiv:1803.00765):
  I(S:F) = χ(S:F) + D(S:F) (their Eq. (11)); in their random-matrix
  two-level-system model, *"Quantum Darwinism can apparently emerge under
  the Perez trace even when spectrum broadcast structure does not
  emerge, and the majority of the quantum mutual information between
  system and environment fractions is in fact quantum in nature"*; and
  *"the amount of quantum discord is comparable to the amount of
  accessible information at the various different fraction sizes f. A
  relatively large fraction of the environment is required to obtain
  (accessible) information approximately equal to the system entropy."*
  So plateau-without-audit is not an artifact of hand-built fixtures: it
  is what generic (random-matrix, non-Markovian-regime) dynamics
  produce.
- **The equivalence theorem (the audit layer's exact formal home).**
  Le & Olaya-Castro, PRL 122, 010403 (2019): SBS ⟺ strong quantum
  Darwinism (I = χ = H(S), zero discord) + strong independence.
  A Comment (Feller, PRL 126, 188901 (2021)) and Reply exist; the
  witness above does not lean on the contested formalization — its
  certificates are bare Holevo and entanglement facts.
- **What the experiments measured (D2 sub-question iii).**
  - Photonic cluster states, Ciampini et al., PRA 98, 020101(R) (2018);
    photonic simulator, Chen et al., Science Bulletin 64, 580 (2019):
    raw mutual-information plateaus.
  - NV centers, Unden et al., PRL 123, 140402 (2019): the **Holevo
    part** χ(fE|S) = H(S) only; the review states this is *"too weak to
    apply the Strong quantum Darwinism Theorem ... precisely because of
    the unknown discord."*
  - Superconducting circuits, Science Advances 11, eadx6857 (2025)
    (arXiv:2504.00781): measured **I, χ, and D separately** at 12 qubits
    (2 system + 10 environment) — the audit split is a demonstrated
    laboratory measurement, and in their engineered good-decoherence
    regime plateau and vanishing discord co-occurred.
  - Le & Olaya-Castro, Quantum Sci. Technol. 5, 045012 (2020): a
    tomography-free witness of strong-QD failure with a proposed
    photonic implementation.

  So: the audit conditions are measurable with already-demonstrated
  capability (block tomography of 2–3 qubit S+fragment marginals, or the
  tomography-free witness). The witness protocol is **not**
  capability-locked; the frozen table's third branch does not apply.

## 4. The three D2 computations, answered

1. **(i) Exact witness in the declared class:** delivered (W1, W2 above;
   exact arithmetic, hard asserts, deterministic receipt).
2. **(ii) Do realizable dynamics generate QD-without-SBS at observable
   scales?** Yes. W1 is the finite-time state of every central-spin
   dephasing process at partial-decoherence couplings — the same N and
   overlap regime as the published photonic experiments; the
   random-matrix result (Le–Olaya-Castro 2018) shows generic
   interacting dynamics hold the discord fraction of the plateau O(1);
   W2-type intra-environment correlation is scale-uniform. The honest
   converse is recorded in §6.
3. **(iii) Did the experiments measure raw or audited redundancy?**
   Split by platform: photonic — raw only; NV — Holevo only (discord
   unknown); superconducting 2025 — full audit split measured. The
   finite protocol separating raw from audited redundancy is: measure
   I(S:F) and χ(S:F) (equivalently D = I − χ) on small S+fragment
   blocks, plus fragment cross-correlation I(F_j:F_k | pointer);
   all components are demonstrated laboratory measurements.

## 5. Verdict, per the frozen table

**Branch 1 — kills the null (strong form), scoped exactly:**

> A physically realizable dynamics in the declared class (central-spin
> at finite coupling time; correlated-ancilla environments) generates
> plateau-with-failed-audit states with finite witness protocols at
> realistic scales (N = 2–4 fragments, overlap 3/5 — the published
> experiments' own regime; audit margins ≈ 0.18 bits / 20% of plateau
> height, and 1 full bit scale-uniform on the independence rung).
> Audited redundancy and raw redundancy therefore **differ empirically**;
> the audit layer is **physical content, not bookkeeping**.

The null's step-4 claim ("auditing access and independence is classical
post-processing ... no new parameter, no deviation in any functional
form") is dead in its frozen form: the audit conditions are *separate
measurable quantities* that provably and by finite margins disagree with
the raw plateau on exactly realizable states, and one 2025 experiment
already measures them as separate quantities.

**Absorber-first discipline (binding, §6.3 of the plan):** the physical
content just witnessed is *exactly* the published SBS/strong-QD-over-QD
gap (Horodecki–Korbicz line; Le–Olaya-Castro). D2 therefore does **not**
hand DU a new mechanism, parameter, or dynamical term — it establishes
that the audit rungs of DU's typed ladder (independently accessible
record ≠ retained record; access + independence audits) coincide with
already-confirmed-to-be-contentful physics rather than with bookkeeping.
Per the table this banks (Joe-gated) as Grade 4 selection/necessity *of
the audit conditions*, with the prediction-register handoff under its
full gates; the DU-distinctive residue is the typed absorption, not
novelty.

Campaign consequence: D1 (executed earlier the same day,
`explorations/classicality-transition-functional-form-d1-literature-check-2026-08-03.md`)
left the null unwounded and routed the campaign to exactly this
audit-content route; the decision tree now proceeds D2 → D3 with the
"witness" branch taken. D3 (BPH genericity transfer) remains live and is
now precisely pointed: the null survives only if genericity makes the
audit conditions automatic *wherever plateaus are physically observed* —
§6 below records exactly where that pressure sits.

## 6. Two-sidedness: the strongest case for the opposite reading

Stated per the binding rule, as a proponent of the null would put it:

1. **Asymptotic co-occurrence in ideal dynamics (computed, in-probe).**
   In the pure symmetric branching family at fixed overlap, the exact
   sweep (N = 8) shows single fragments fall *off* the plateau
   (I − H(S) ≈ −0.28 bits) while half-environment blocks sit exactly on
   it with exponentially small coherence (a^{N/2}) and exponentially
   good distinguishability. Wherever both the fragment and its
   complement are large, plateau and audit co-occur up to exponentially
   vanishing corrections. In the macroscopic-environment idealization,
   the audit is asymptotically automatic — the null's second branch
   holds *in that corner*, and D3's genericity theorems will try to make
   that corner the whole physical story.
2. **The best-instrumented experiment found co-occurrence.** The 2025
   superconducting experiment measured the audit split and found discord
   ≈ 0 exactly where the plateau formed, in its engineered regime. A
   null proponent reads this as: where redundancy is actually observed
   to form well, the audit adds no *surprise*.
3. **The content is not DU's.** Everything witnessed is standard
   quantum-information physics from 2015–2021. A null proponent can
   retreat to: "the audit layer is real physics, but it is
   Horodecki/Korbicz/Le–Olaya-Castro physics; DU's audit vocabulary adds
   nothing beyond it." This retreat is *conceded in advance* — but note
   it is a different claim from the frozen null, which asserted
   bookkeeping (no empirical content at all). The frozen claim is the
   one D2 was preregistered to adjudicate, and it lost.
4. **The W2 rung is contestable.** The independence failure in W2
   carries no system information, and the PRL 122 line itself argues
   strong QD alone (without strong independence) signals objectivity of
   outcomes. If one adopts that reading, W2 witnesses a failure of the
   SBS *definition*, not of operational objectivity. W1 does not have
   this weakness (its failing rungs — discord and distinguishability —
   are operationally meaningful access facts), which is why W1 is the
   load-bearing witness and W2 is recorded as the independence-rung
   probe only.
5. **Short plateaus.** At N = 2 the "plateau" is a point and at N = 4 a
   half-split pair; a null proponent may call this a degenerate plateau.
   Response: these are the scales at which the published experiments
   report QD plateaus, and the random-matrix pin shows the same
   separation in larger, generic models — but the response is an
   appeal to literature, not to this probe's own exact computation.

## 7. Not established

No new physics, mechanism, consensus ontology, or record fundamentality;
no universal claim about macroscopic environments (point 1 of §6 is the
live boundary, owned by D3); no exact optimal-discord values (only
strict positivity); no claim that DU's audit ladder adds content *over
the SBS literature* (the opposite is recorded); no experimental
reanalysis performed (D2's sub-question iii is answered from published
descriptions verified against primary text, not from data); no grade
movement, banking, register edit, prediction entry, routing change,
paper posture, hardware, or external action. The Feller Comment / Reply
dispute over the SQD formalization is noted, not adjudicated. Banking at
the frozen table's named grade is Joe's decision through
CURRENT-RESEARCH.yaml.

## 8. Provenance

- Frozen plan: `explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md` (§3 D2 pass/fail table; §6 preregistration discipline).
- Wave-1a absorption note: `explorations/external-mergeable-sector-theorem-spine-and-taf-record-typing-absorption-2026-08-03.md` (sharpened null; audit ladder).
- D1 execution note: `explorations/classicality-transition-functional-form-d1-literature-check-2026-08-03.md` (null survives D1; campaign routed to D2).
- Witness: `tests/du_qd_sbs_audit_gap_witness_probe.py`; receipt `tests/artifacts/du_qd_sbs_audit_gap_witness_result.json` (16/16, byte-identical reruns).
- Primary sources verified during execution: arXiv:2007.04276v2 (Korbicz review; Quantum 5, 571 (2021)); arXiv:1803.00765v2 (Le–Olaya-Castro, PRA 98, 032103 (2018)); PRL 122, 010403 (2019) (Le–Olaya-Castro; arXiv:1803.08936); PRL 126, 188901 (2021) (Comment) and arXiv:2101.10756 (Reply); arXiv:1312.6588v2 (Horodecki–Korbicz–Horodecki, PRA 91, 032122 (2015)); Quantum Sci. Technol. 5, 045012 (2020) (arXiv:1908.08818); arXiv:2504.00781 (Science Advances 11, eadx6857 (2025), superconducting circuits); PRA 98, 020101(R) (2018) (Ciampini et al.); PRL 123, 140402 (2019) (Unden et al.); Science Bulletin 64, 580 (2019) (Chen et al.).
- DU internal consumed: HC-DU-057, HC-DU-063, HC-DU-043 boundaries as typed in the plan; TaF T1 typing by pointer.
