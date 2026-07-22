---
title: "R-test (R2/R3): does relocating mode-issuance to the RELATIONAL/coalitional algebra grow genuinely NEW relational TYPES, or only MORE INSTANCES of pairwise correlation? — the additive-count wall, re-instantiated at the relational level"
status: active_research
doc_type: rtest
created: 2026-07-21
lane: "2.2 (candidate-unification generation) -> 1.1 (flip-witness) — the decisive R2/R3 test of the incentive-selection mode-issuance candidate's CORE relocation (LOCAL generators -> RELATIONAL algebra)"
verdict: "INSTANCES-ONLY (as-modeled). The candidate's default relocation collapses onto its own positive controls: 'correlate a growing set of record-subsystems' defaults to a pairwise-closed correlation graph (Θ_eff constant = 1), identical to i.i.d. Bell pairs and to a fully-connected multivariate Gaussian. The additive-count wall wins as-modeled — the core fails. A TYPES-GROW branch (genuine growing-order irreducible coalitions) EXISTS and is non-capping, but is (a) an unprovided extra ingredient, (b) DISCLOSURE at the observable-algebra level — the fixed UHF/CAR algebra ⊗_k M_d factors every finite-N relational algebra (the same fixed-CAR absorber that killed the condensate), so 'new coalition types' are new STATES on a FIXED algebra, exactly R1's disclosure trap — and (c) its only genuine algebra-type route (Araki–Woods III_λ in the N→∞ limit) re-imports source-forcing (R4)."
grade: "model grade; 19/19 calibration checks pass with the mandatory positive control firing; core relocation FAILS the additive wall as-modeled; no claim banked; claim_status_change: none"
inputs:
  - explorations/incentive-selection-mode-issuance-candidate-2026-07-21.md   # the candidate + its Test #1
  - explorations/flip-witness-algebra-requirements-2026-07-21.md             # R1/R2/R3 definitions
  - explorations/wave2-flagship-convergence-synthesis-2026-07-21.md          # the fixed-CAR absorber this re-instantiates
  - tests/du_relational_algebra_growth_probe.py                              # the probe (foreground; positive control)
  - tests/artifacts/du_relational_algebra_growth_result.json                 # machine result
---

# R-test (R2/R3): relational-algebra growth — new TYPES or only more INSTANCES?

## The fork tested
The incentive-selection candidate relocates mode-issuance from **LOCAL generators** (GU's fixed
`Cl(9,5)` forbids new generators) to the **RELATIONAL / coalitional** algebra — correlations among
a growing set of participating record-subsystems. Its own pre-registered Test #1 asks the decisive
question:

> As the participant set grows, does the observable/relational algebra grow in genuinely **NEW
> relational TYPES** (W1 = non-isomorphic; R2 satisfied), or is it just **MORE INSTANCES** of the
> same pairwise-correlation type (the additive-count wall; still finite-type / disclosure)? And is
> the growth **productive/non-absorbing** (R3, Θ_eff non-capping) or does it cap?

## What was built (anti-toy)
A concrete growing model: `N` record-subsystems (qubits) accreting over the roll with a
coalition/correlation hypergraph. The **irreducibility discriminator** is the *exact* connected-
correlation function (joint cumulant / Ursell function): a `k`-body coalition is *irreducibly new*
iff it carries a nonzero order-`k` cumulant not reproducible from any lower-order (≤`k−1`) marginal.
The clean witness of an irreducible `k`-ary type is the **GHZ_k coalition**: in the X basis **every
proper-subset correlator vanishes and only the full `k`-body correlator survives (=1)** — a pure
`k`-body relation invisible to all pairwise/lower marginals, a distinct SLOCC class from any product
of lower coalitions (Dür–Vidal–Cirac). Verified exactly for `k=2,3,4`, plus the independence lemma
(disjoint coalitions carry no cross-cumulant, so the realized irreducible orders of a product of
coalitions = the multiset of block sizes). The effective type-count is
`Θ_eff(N) = |{distinct irreducible-correlation orders realized by stage N}|`.

## Positive controls (mandatory; all fire — the null is informative)
- **PC-PAIRWISE** (product of i.i.d. Bell pairs): realized orders `{2}` forever, `Θ_eff ≡ 1`. **FLAT.**
- **PC-GAUSSIAN** (growing **fully-connected** multivariate Gaussian, off-diagonal correlation up to
  0.64): **all cumulants of order ≥3 vanish identically** (Isserlis) → `Θ_eff ≡ 1`. **FLAT even though
  every variable is correlated with every other** — the sharp control: *growing the correlation GRAPH
  (more edges, denser pairwise) is NOT type growth.*
- **PC-PRODUCTIVE** (positive win control, growing-order coalitions): `Θ_eff = 1,2,…,9` non-capping →
  **TYPES-GROW.** The discriminator *can* register a win, so a non-win verdict is informative, not rigged.

The discriminator cleanly separates the two flat controls from the growing one (19/19 checks pass,
exit 0). If PC-PAIRWISE/PC-GAUSSIAN were not flat, the discriminator would be miscalibrated.

## Result — the candidate as-modeled

The same model family yields three regimes depending on **what "correlate" means at each accretion
step** — so the fork is **discriminator-gated, not decided by the relocation itself**:

| Reading | What accretion does | Θ_eff(N) | Regime |
|---|---|---|---|
| **M1 (default/generic)** | add a subsystem, **correlate it** (a 2-body bond) | `1,1,1,…` | **INSTANCES-ONLY** — additive wall |
| **M2 (bounded coalition)** | genuine but **bounded-order** coalitions (≤3-body) | `2,2,2,…` | **PARTIAL** — R2 yes, R3 no (caps) |
| **M3 (growing coalition)** | authors an **irreducible growing-order** coalition each step | `1,2,3,…` | **TYPES-GROW** — non-capping |

**The candidate's default reading is M1.** "Correlations among a growing set of record-subsystems"
means, by default, a growing graph of **pairwise** bonds — which is pairwise-closed and lands exactly
on PC-PAIRWISE / PC-GAUSSIAN: `Θ_eff` constant, the additive wall. **As-modeled, the core relocation
does not escape the wall — it fails.**

TYPES-GROW (M3) requires the accretion to **author genuinely irreducible higher-order coalitions of
growing order** — an added, non-generic ingredient the candidate *names* ("coalition") but supplies
**no mechanism for**; it is precisely the unsolved genuine-multipartite-structure content.

## The deeper obstruction — even TYPES-GROW is DISCLOSURE at the algebra level

Grant M3 anyway. At every finite `N` the composite observable algebra of fixed-local-algebra
subsystems is `M_{d^N}(ℂ)` — a **type-I factor whose only *-isomorphism invariant is dimension**. All
of them embed in the **single fixed UHF/CAR algebra** `A_∞ = ⊗_{k≥1} M_d` via the unital
*-homomorphism `x ↦ x⊗I` (verified: product/adjoint/unit preserved). **A fixed `A_∞` factoring every
finite-`N` relational algebra is exactly the fixed-H / fixed-CAR absorber that killed the mirror
condensate — now re-instantiated at the RELATIONAL level.**

Consequently the "growing coalition TYPES" are **SLOCC classes = equivalence classes of STATES** under
local operations, **not *-isomorphism types of the observable algebra**. New state-classes on a fixed
algebra is precisely **R1's disclosure trap** ("a fixed algebra hosts all phases as states"), not R1's
growth (`A_late ≇ A_early` *as algebras*). So even M3's apparent type-growth is disclosure here.

**The one genuine algebra-type route** (leaving type I) is the `N→∞` von Neumann completion in a
non-type-I representation — **Araki–Woods `III_λ`** (illustrated: per-site state `λ=0→I_∞`, `0<λ<1→III_λ`
Powers, `λ=1→II_1`). Its type is a function of the **per-site STATE**, so *which type the relational
algebra grows into is state-selected* → **re-imports source-forcing (R4)**, the very crux the whole
flagship is stuck on. And it is a new **state/representation on the fixed algebra**, not an enlarged
algebra of observables — the same disclosure/growth line R1 draws.

## R5 (light) — transduction, not relabel
A local-unitary relabel of GHZ_3 leaves its irreducible-order signature fixed (`d=0`). Genuine growth
(M3) moves the invariant, `k_max: 2→10` (`d>0`). So `d>0` holds **only in the M3 branch** (the
unprovided ingredient); the default M1/M2 accretion is closer to a `d=0` relabel — more instances of a
fixed pairwise motif.

## DU-board reading (inline; personas are lenses, not evidence)
- **Constructor/Assembly:** the object grows only in the M3 SLOCC sense; as an *algebra* it does not
  grow (type-I at all finite `N`) — the assembly index of a pairwise-generated record does not increase
  in TYPE.
- **Model-theorist:** M1/M2 default is more INSTANCES of a fixed type (relabel-like, `d≈0`); the
  genuinely-new type (M3) is not supplied by "correlation" alone.
- **Applied Category Theory:** the coalition sheaf's *sections* (states) proliferate; the *structure
  sheaf* (observable algebra) is the fixed UHF colimit — growth is in sections = disclosure.
- **Metabolic-Scaling absorber (the "non-additive or absorbed by counting?" seat):** record
  **redundancy** — what makes something an *objective record* (R5) — is pairwise-classical (many
  identical system–fragment correlations = INSTANCES); irreducible higher-order (GHZ) coalitions are
  fragile and non-redundant. Hence a **record/irreducibility dilemma**: *record-like ⇒ additive wall;
  irreducible ⇒ not record-durable.*
- **Adversary-C (strongest form):** the candidate's best *physical* instantiation, quantum-Darwinism
  redundancy, is many identical **pairwise** system–fragment records — more instances of one pairwise
  type, not new types. The strongest form of the candidate IS the additive wall.

## Verdict and grade
**INSTANCES-ONLY (as-modeled).** The candidate's core relocation does not escape the additive-count
wall for its default/generic model — it collapses onto its own positive controls. A conditional
**TYPES-GROW** branch is located and shown non-capping, but it is an unprovided ingredient, is
DISCLOSURE at the observable-algebra level (states on the fixed UHF/CAR algebra = the same fixed-CAR
absorber that killed the condensate), and its only genuine algebra-type route (Araki–Woods III)
re-imports source-forcing (R4). **Model grade; no claim banked; `claim_status_change: none`.**

## Constructive relocation (what this earns)
The open question sharpens from the vague *"grow the relational algebra"* to a **sharp, non-vacuous
R4/R6 target**: *does the source dynamics select a type-III (modular/KMS) limit representation?* This
consiliently identifies the relational route's crux with the flagship's existing source-forcing crux —
it does not rescue the candidate as-modeled, but it points the next swing at a precise object (the
modular/KMS structure of the `N→∞` limit and whether B5 can source its `λ`).

## Boundary
R-test / model grade; anti-toy build with a firing positive control; sovereign self-verification per
CONNECTIONS.md (the fixed-CAR absorber, SLOCC/GHZ facts, and Araki–Woods classification were used as
tools and re-checked here, none adopted on a sibling's or source's say-so). No claim banked, no grade
moved. Probe: `tests/du_relational_algebra_growth_probe.py`; artifact:
`tests/artifacts/du_relational_algebra_growth_result.json`.
