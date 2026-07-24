---
artifact_type: exploration
exploration_id: DU-XREPO-HARDEN-01
status: active_prioritized_register
created: 2026-07-21
lane: "1.4 + 1.5 + 2.3 + 2.4 + 4.4 + A"
directed_by: "Joe direct chat, 2026-07-21"
claim_status_change: none
canon_change: none
public_posture_change: none
verification:
  - tests/du_lambda_N_covariant_acceleration_audit.py
  - tests/artifacts/du_lambda_N_covariant_acceleration_audit_result.json
---

# Cross-repo gap hardening and non-intuitive reuse map

## Result first

Dynamic Unity does **not** need another Lane. Its present job/mode topology has
the right owners. It needs one prioritized hardening program routed through the
existing channels, with stable IDs that automation can advance without erasing
the original fifty-persona / one-hundred-suggestion register.

The highest-priority swing, `SWING-DU-COV-01`, was executed in this pass. The
result is:

> **A Bianchi-conserved, accelerating FLRW background family exists without an
> arbitrary exchange function. Full covariance, perturbative stability and
> observational viability remain open.**

The old `p=2/3` tracker is not a universal no-go. It is the branch obtained by
keeping dust separately conserved while `Lambda(N)` rolls. That branch leaves
a nonzero Bianchi residual. If total conservation is imposed, the required
matter/vacuum exchange is forced by the closure itself. The repaired system has
stable accelerating attractors across a broad parameter range.

The rescue is important but limited. Calibrating today's `Omega_Lambda` as the
attractor erases the matter era. Retaining a matter-dominated past and an
`H(z)` history close to constant-Lambda pushes the interaction toward weak
coupling and toward the LambdaCDM limit. The background calculation therefore
opens a real route and identifies the next hard kill: the covariant definition
of `N`, the interaction four-vector/action, perturbations, growth and data.

This work is deliberately disjoint from the spectral-flow/source-mint work
completed by the other agent at Dynamic Unity commit `946dbc3`. That run found
the naive spectral-flow mint absorbed and moved the live construction to a
self-authoring feedback loop. This note does not reopen or duplicate it.

## Scope and source pins

Every sibling repository was read-only. Repository-owned claims were consumed
as typed inputs, not imported as Dynamic Unity truth. GU Formalization already
had unrelated uncommitted changes in `LANE-STATE.yaml`, `NEXT-STEPS.md` and
`lab/process/research-portfolio.json`; those state surfaces were not used as
authority and were not touched.

| Repository | Inspected commit | State at inspection | Use here |
|---|---|---|---|
| Dynamic Unity | `946dbc3bfde3` | clean/even after the other agent closed | writable owner |
| Time as Finality | `b8a5c189c29d` | clean/even | finality, capability and descent models |
| Temporal Issuance | `1eef69e0d619` | clean/even | completion absorbers and source-issuance tournament |
| GU Formalization | `e620ff090215` | dirty in three unrelated state files | committed canon and class-relative maps only |
| Possibility to Capability | `8e52fbe451b7` | clean/even | typed capability, construction forks and completion firewall |
| Continuity Ledger | `d06f2a10020` | clean/even | no-go/escape/import/loss and same-frame control discipline |

## Lane placement

| Work | Primary owner | Supporting owner | Placement decision |
|---|---|---|---|
| Conserved cosmological background, perturbations and observations | `1.4` | `4.1`, `4.3`, `4.4` | keep in Lane 1; this is a direct flagship validity test |
| Typed `N`, action, EFT, CSG/AQFT and low-energy recovery | `1.5` | `A.1`, `4.4` | keep in Lane 1; it is theory construction, not stewardship alone |
| GU contribution and live rival comparison | `2.3` | `4.4` | keep in Lane 2; do not prejudge GU identity |
| Source mint, open-endedness and emergence alternatives | `2.4` | `1.1`, `1.2` | keep in Lane 2 until a source-owned object passes the mint rubric |
| Claim grades, evidence independence and clean-room replication | `4.4` | `A.1`, `A.2` | cross-cutting hardening, not a new gate Lane |
| Lossless persona suggestion custody | `A.3` | `3.x` | original `P01-A` through `P50-B` records remain authoritative |

No new lane is added because a “credibility lane” would wrongly turn honesty
into a downstream stage. Each scientific channel must carry its own hardening
burden; Lane 4 and Lane A maintain the shared instruments and provenance.

## The executed swing: conserved Lambda-N background

### Typed definitions

Use flat FLRW units `8*pi*G/3=1` and distinguish the cosmological constant from
its Friedmann energy term:

```text
lambda = Lambda/3
H^2 = rho_m + lambda
lambda = A / sqrt(N),     A = c_S/3
dN/dt = kappa H^-3
Omega = lambda/H^2
beta = kappa/A^2 = 9 kappa/c_S^2
```

If the rolling vacuum term has pressure `p_lambda=-lambda`, total conservation
requires

```text
rho_m' + 3 rho_m = Q/H
lambda' = -Q/H
```

where prime means `d/d ln(a)`. The closure and count law fix the exchange; no
free function is chosen:

```text
d ln(N)/d ln(a)      = beta Omega^2
d ln(lambda)/d ln(a) = -(beta/2) Omega^2
Q = -dot(lambda)     = (beta/2) H Omega^2 lambda
```

Friedmann plus total conservation then give the closed autonomous background:

```text
d ln(H)/d ln(a) = -(3/2)(1-Omega)
dOmega/d ln(a)  = Omega [3(1-Omega) - (beta/2)Omega^2]
q               = (1-3Omega)/2
w_total         = -Omega
```

### Analytic result

For every `beta>0` there is one positive stable fixed point,

```text
Omega_* = 6 / (3 + sqrt(9+6 beta)).
```

It accelerates exactly when

```text
beta < 36    <=>    c_S/sqrt(kappa) > 1/2.
```

| `beta` | `c_S/sqrt(kappa)` | `Omega_*` | `q_*` | `a(t)` power `p` | Reading |
|---:|---:|---:|---:|---:|---|
| 0.25 | 6.000 | 0.9615 | -0.9422 | 17.31 | accelerating, near de Sitter |
| 1.00 | 3.000 | 0.8730 | -0.8095 | 5.25 | accelerating |
| 4.0353 | 1.493 | 0.6847 | -0.5271 | 2.114 | today's fraction used as attractor |
| 9.00 | 1.000 | 0.5486 | -0.3229 | 1.477 | natural unit coefficients accelerate |
| 36.00 | 0.500 | 0.3333 | 0 | 1 | acceleration boundary |
| 50.00 | 0.424 | 0.2916 | +0.0626 | 0.941 | nonaccelerating |

This overturns only the broad reading of the old `p=2/3` result. It does not
overturn the old coefficient/sourcing result. `Omega_*` is still controlled by
one dimensionless ratio. Setting `Omega_*=0.6847` selects
`c_S/sqrt(kappa)=1.493`; it is not predicted.

### Background sanity pressure

The executable probe normalizes `Omega_0=0.6847`, integrates backward, and
compares `H(z)` with flat constant-Lambda cosmology at the same present
fraction. Its five-percent envelope is an internal teeth check, not a data fit.

| `beta` | max `|H/H_LCDM-1|`, `0<=z<=2` | `Omega_Lambda(z=1100)` | Internal envelope |
|---:|---:|---:|---|
| 0.25 | 1.01% | `1.70e-9` | pass |
| 0.50 | 2.09% | `1.78e-9` | pass |
| 1.00 | 4.47% | `1.98e-9` | pass |
| 2.00 | 10.53% | `2.62e-9` | fail |
| 3.00 | 19.88% | `4.24e-9` | fail |
| 4.00 | 42.58% | `5.25e-8` | fail |

For natural `c_S=kappa=1`, hence `beta=9`, normalizing the present universe to
`Omega_0=0.6847` places it above the fixed point; backward evolution reaches
`rho_m=0` near `z=0.18` and becomes unphysical. Conversely, making today's
fraction exactly the fixed point keeps that fraction constant and removes the
matter era. A viable history therefore requires a smaller `beta` and direct
growth/early-universe checks. The numerics do **not** establish an empirical
bound; they establish that the observational gate has teeth.

### Exact grade

`SWING-DU-COV-01` earns:

```text
BACKGROUND_CONSERVED_ACCELERATING_FAMILY
```

It does **not** yet earn the preregistered full outcome
`COVARIANT-ACCELERATING`, because these remain unbuilt:

1. a local or relational covariant definition of the cumulative count `N`;
2. a covariant source law that does not silently choose a preferred foliation;
3. an action or interaction four-vector, including momentum transfer;
4. scalar/vector/tensor perturbations, sound speeds and ghost/gradient checks;
5. matter creation microphysics and a resource/entropy ledger;
6. growth, lensing, CMB, BBN, supernova and BAO likelihoods;
7. a naturalness argument for the surviving coefficient range.

### External primary-source sanity anchors (not DU evidence)

The background bookkeeping matches the standard interacting-vacuum warning
structure, but these papers do not validate this particular closure:

- Wands, De-Santiago and Wang, [*Inhomogeneous vacuum energy*
  (arXiv:1203.6776)](https://arxiv.org/abs/1203.6776), shows why a varying
  vacuum needs a covariant vacuum prescription or energy-transfer four-vector
  before inhomogeneous perturbations are defined. It also makes the foliation
  issue explicit.
- Valiviita, Majerotto and Maartens, [*Large-scale instability in interacting
  dark energy and dark matter fluids*
  (arXiv:0804.0232)](https://arxiv.org/abs/0804.0232), is a direct warning that
  a well-behaved background can hide an early superhorizon perturbation
  instability.
- Li and Zhang, [*Large-scale stable interacting dark energy model*
  (arXiv:1312.6328)](https://arxiv.org/abs/1312.6328), supplies a positive
  control: stability is possible for a designed interaction, but the form of
  the interaction and the observational constraints do substantive work. DU
  may use it as a comparator, not import its chosen `Q`.

These checks strengthen the priority of `HC-DU-002` through `HC-DU-005`; they
do not raise `HC-DU-001` above background model grade.

## Credibility ladder used by the hardening register

This ladder records what a claim has actually survived; it is not a pipeline
and does not replace repo-native grades.

| Grade | Minimum content |
|---|---|
| `DU-H0` | named lead with explicit nonclaim |
| `DU-H1` | typed objects, class boundary, equations or decision contract |
| `DU-H2` | analytic or executable model with positive and failing-direction controls |
| `DU-H3` | preregistered hostile attack plus independent reimplementation |
| `DU-H4` | source-grounded physical model: action/dynamics, observables, errors and recovery limits |
| `DU-H5` | cross-family replication or held-out prediction against strongest live rivals |
| `DU-H6` | external empirical or expert verification with independent provenance |

An item may be mathematically `DU-H3` and physically only `DU-H1`. The lower
of the relevant grades controls any physical headline.

## Prioritized hardening register

Statuses are deliberately non-destructive: `DONE_SCOPED` means only the named
burden is closed; `REUSE` points to an existing model that DU must re-verify;
`ACTIVE_OTHER` prevents duplicate work; `OPEN` remains live.

| ID | Priority | Object / credibility gap | Current grade and status | Exact next discriminator | DU home | Reuse |
|---|---|---|---|---|---|---|
| `HC-DU-001` | P0 | conserved accelerating Lambda-N background | `DU-H2`, `DONE_SCOPED` | independently rederive and attack assumptions | `1.4/4.4` | new audit |
| `HC-DU-002` | P0 | covariant/local definition of cumulative `N` | `DU-H2`, `DONE_SCOPED_METRIC_SEEDED__ORDER_FIRST_OPEN` | literal causal-past count and bi-wave proxy now exact; build label-invariant order-first cardinality and reconstruct geometry without importing FLRW | `1.4/1.5/2.2` | COV-02; CMF-01; TaF T526 |
| `HC-DU-003` | P0 | covariant interaction/action | `DU-H2`, `PARTIAL_COMPLETE_Q__CTP_ACTION_OPEN` | construct a retarded response plus positive common-past noise kernel in a stress-consistent CTP/action completion | `1.4/1.5` | COV-02; CMF-01; P2C source-action obligations |
| `HC-DU-004` | P0 | perturbative stability and growth | `DU-H2`, `SCOPED_FAIL_LOCAL_AND_SCALE_FREE_MEMORY` | CMF-01 escapes the local principal cone but fails background; finite-k growth waits on a generated-scale/action branch | `1.4` | COV-02 + CMF-01 probes |
| `HC-DU-005` | P0 | observational background and early universe | `DU-H2`, `SCOPED_FAIL_SCALE_FREE_MEMORY__LIKELIHOOD_DEFERRED` | do not run a likelihood on the raw count; derive overlap `P_Lambda(k,z)` only after a background/action escape | `1.4/4.1` | CMF-01 exact tracker/history; Zuntz comparator |
| `HC-DU-006` | P0 | coefficient sourcing / naturalness | `DU-H2`, `OPEN_GENERATED_SCALE_ONLY` | raw late calibration makes early density order one; source a dimensional memory scale before `H(z)`, not another scale-free coefficient | `1.3/1.4/2.4` | CMF-01; GU ratio-only warning; RR comparator |
| `HC-DU-007` | P0 | typed map among all objects called `N` | `DU-H2`, `PARTIAL_EXECUTABLE_TYPE_BOUNDARY` | CMF-01 separates literal count, bi-wave memory, martingale, offset and order-first cardinality; finish the repository-wide commuting/noncommuting diagram | `1.5/A.1` | CMF-01; P2C indexed profiles; CLTP |
| `HC-DU-008` | P0 | evidence-dependency and common-source audit | `DU-H0`, `OPEN` | DAG every support edge; collapse common ancestors before counting consilience | `4.4/A.1` | TaF/P2C provenance rules |
| `HC-DU-009` | P0 | clean-checkout reproducibility | `DU-H2`, `OPEN` | second implementation from equations only; compare frozen JSON | `4.4/A.2` | CL blinding discipline |
| `HC-DU-010` | P0 | minimum theory passport and low-energy recovery | `DU-H0`, `OPEN` | state space, action, symmetries, constraints, observables, quantization, GR/SM limits | `1.5` | P2C eight-gate/source-action rubrics |
| `HC-DU-011` | P0 | causal-set classical growth law | `DU-H1`, `NEXT_FRONTIER_PROGRAM__FIRST_BUILD_HC-DU-011A` | freeze the full covariance passport and exact small-unlabeled-causet harness: statewise isomorphism plus equal path weight across natural labelings, normalization, spectator/Bell behavior, past immutability and physical-record versus gauge bookkeeping | `1.5/2.2/2.4` | CMF-01; five-persona council; TaF T526; TI RUN-0177 |
| `HC-DU-012` | P1 | quantum-measure/decoherence completion | `DU-H0`, `OPEN` | explicit decoherence functional and grade-2 additivity tests | `1.5` | TI record/Born no-go |
| `HC-DU-013` | P1 | AQFT/locality embedding | `DU-H0`, `OPEN` | net isotony, locality, covariance and state-positive checks on one nontrivial region family | `1.5` | TaF finite restriction systems |
| `HC-DU-014` | P1 | source-internal mint / self-authoring loop | `DU-H1`, `ACTIVE_OTHER` | do not duplicate; next build must feed issued records back into the law | `1.1/1.2/2.4` | DU `946dbc3`; TI D-FORK |
| `HC-DU-015` | P1 | BV/BRST, anomaly and constraint closure | `DU-H0`, `OPEN` | master-equation/anomaly audit for the actual field content | `1.5` | GU carrier-bit/RS work |
| `HC-DU-016` | P1 | EFT and radiative stability | `DU-H0`, `OPEN` | operator basis, symmetries, loops and technical-naturalness calculation | `1.5` | none complete |
| `HC-DU-017` | P1 | GU ablation | `DU-H0`, `OPEN` | rerun each flagship argument with GU removed; record what changes | `2.3` | GU construction-fork map |
| `HC-DU-018` | P1 | live rival tournament | `DU-H2`, `PARTIAL_CAUSAL_MEMORY_TOURNAMENT` | CMF-01 compares literal, bi-wave, martingale, offset and generated-scale branches; extend the same scorecard to sequestering/RR and fixed-history nulls | `2.3/4.4` | CMF-01; TI/P2C completion firewalls |
| `HC-DU-019` | P1 | operational finality observable | `DU-H1`, `OPEN` | source-owned Hamiltonian, locality-of-update, effect size and detector contract | `4.1/4.3` | TaF T583-T587 |
| `HC-DU-020` | P1 | Born weights and single outcome | `DU-H1`, `OPEN` | explicit rival-separated probability rule; record stability alone is barred | `1.5/4.1` | TI RUN-0072/0073 |
| `HC-DU-021` | P1 | covariant finality/AQFT bridge | `DU-H1`, `OPEN` | build the net embedding; do not infer becoming from causal-order covariance | `1.5/4.3` | DU covariant-finality synthesis |
| `HC-DU-022` | P0 | genuine dimensional transmutation | `DU-H0`, `NEXT_FRONTIER_PROGRAM__STAGE_2_AFTER_011A` | after full path covariance, test only covariant-landmark renormalization and physical coupling-record routes for a regulator-stable hierarchy relative to one declared microscopic unit; no direct `p(N)`, `m~H0`, target epoch or inserted window | `1.3/2.4` | CMF-01; five-persona council; wild-frontier count-running kill; spectral-flow kill at `946dbc3`; RR comparator |
| `HC-DU-023` | P1 | sign bit `sigma` | `DU-H2`, `PARTIAL_MARTINGALE_SIGN_FAILS_PERSISTENCE` | the centered causal martingale makes a sign but stays positive from z=2 only 2.36%; source persistence without `abs(S)` or seed selection | `1.3/1.5/2.2` | CMF-01; GU signed-readout theorem |
| `HC-DU-024` | P1 | non-circular open-endedness | `DU-H0`, `OPEN` | novelty measure invariant to renaming/completion and tied to a resource ledger | `2.4` | TI D-FORK; P2C boundary discriminator |
| `HC-DU-025` | P2 | persona/agent method calibration | `DU-H0`, `OPEN` | blinded comparison against non-persona baselines and leakage controls | `3.x/A.3` | P2C decisive-test incidents |
| `HC-DU-026` | P2 | prediction/kill register | `DU-H0`, `OPEN` | stable prediction IDs, priors, stop rules, supersession and null results | `4.1/A.1` | TI kill criteria; CL no-third-branch |
| `HC-DU-027` | P2 | provenance, release and licensing | `DU-H0`, `OPEN` | source/version/license metadata and one-command receipts | `A.2` | CL extraction/authorship rule |
| `HC-DU-028` | P2 | hostile external review | `DU-H0`, `OPEN` | frozen packet to an independent cosmologist/mathematical physicist | `4.4` | TaF external-grade ceiling |
| `HC-DU-029` | P2 | rotating counterfamily search | `DU-H0`, `OPEN` | held-out failure families, not more same-family examples | `4.4` | TI 12-class completion tournament |
| `HC-DU-030` | P2 | durable failure/retirement map | `DU-H0`, `OPEN` | one ledger of dead, scoped-dead, class-exited and reopened branches | `A.1/A.3` | GU no-go map; CLTP `N/X/L/I` |

## Existing models to reuse instead of rebuilding

### Time as Finality

| DU burden | Existing model / result | Honest import boundary |
|---|---|---|
| typed capability object | `results/T583-capability-contract-v1-v0.1-results.md` and T584 invariance gate | finite review contract, not universal physics |
| physical capability example | `results/T585-landauer-physical-capability-gate-v0.1-results.md` | Landauer input, not a time derivation |
| record-order attack | T586 plus `results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md` | record order collapses to task prerequisites; typed filter survives |
| local-to-global records | `FORMALISM.md`, T53/T54 observer descent results | finite descent data; full sheaf not forced |
| class-relative walls | `explorations/class-no-go-council-update-2026-07-10.md` | distinguishes real walls from diagnostic artifacts |

### Temporal Issuance

| DU burden | Existing model / result | Honest import boundary |
|---|---|---|
| strongest absorber family | `COMPLETION-CLASS.md` | bounded class, not a universal metaphysical no-go |
| physical candidate exhaustion | `agent-runs/RUN-0177-physical-witness-completion-tournament.md` | twelve scoped classes absorbed; a thirteenth needs new structure |
| source signatures | `agent-runs/RUN-0150-h8-d-fork-regime-signature-bundle.md` | signature bundle does not decide D-FORK |
| horizon modes | RUN-0124 | standard de Sitter crossing is fixed-source disclosure |
| Everett / Born | RUN-0108, RUN-0072, RUN-0073 | branching and stable records do not issue sources or Born weights |
| adapter limits | RUN-0131 | no cross-repo adapter can manufacture a physical source witness |

### GU Formalization

| DU burden | Existing model / result | Honest import boundary |
|---|---|---|
| construction identity | `GEOMETER-VS-PHYSICS-OBJECTS.md` | prevents applying a theorem to the wrong GU object |
| no-go scope | `canon/no-go-class-relative-map.md` | class exits are not theorem refutations |
| ghosts and chirality | `canon/ghost-parity-krein-synthesis.md`; `canon/swing-ghost-parity-no-chiral-selection.md` | positive-norm sector yes; chiral generation selection no |
| generation count | `canon/three-generations-locate-not-force-CRT-RESULTS.md`; `canon/external-by-structure-synthesis-RESULTS.md` | odd count is external in the scoped class; nothing privileges three |
| source-action burden | `canon/source-action-seiberg-witten-RESULTS.md` | algebraic action exists; generation-count channel remains orthogonal |
| signed readout | `canon/signed-readout-boundary-theorem-RESULTS.md` | internal theorem, not external physics |
| weak-field honesty | `canon/schwarzschild-weak-field-rfail.md` | imported-metric compatibility, not GU recovery of GR |

### Possibility to Capability

| DU burden | Existing model / result | Honest import boundary |
|---|---|---|
| legitimate completion firewall | `explorations/2026-07-16-completion-class-firewall/` | finite formal model; survival hangs on local-operation invariance |
| construction-indexed verdicts | `2026-07-19-cross-frame-descent-or-fork/` and profile-descent theorem | profiles descend; one universal top label does not |
| raw reachability | `2026-07-19-indexed-restriction-diagram/` | exact toy, not source-grounded physics |
| source-action acceptance | `2026-07-17-self-excitation-boundary-big-swing/` | closure/maintenance/autonomy are separated from origin/resources |
| GU adapter restraint | co-flip holonomy preflight and trit-access closure | abstention or falsification is better than filling unknowns |

### Continuity Ledger

| DU burden | Existing model / result | Honest import boundary |
|---|---|---|
| typed no-go/escape accounting | `interfaces/continuity-ledger-transaction-v0.1.md` | proposed packet grammar, not a DU verdict |
| frame-relative comparison | `explorations/2026-07-16-r0-individuation-RESULT.md` | absolute `R0` fails; same-frame paired differences survive |
| near-miss controls | `evidence/cl-001-interval-sweep-dossiers/near-miss-control-admission.md` | controls are constrained but not yet admitted |
| blind evidence architecture | `blind-t-isolated-return-*` dossiers | currently blocked by lack of an isolated blind author |
| authority/provenance | `governance/CHARTER.md` | prevents summary-over-canon and analyst-prior-as-extraction failures |

## Non-intuitive learning annex: false walls, reversals and scoped no-gos

### Inclusion rule

This annex preserves every DU-relevant non-intuitive result located in the
active/canon/status surfaces inspected at the commits above: cases where the
first plausible reading was wrong, a no-go applied only to another class, a
positive result collapsed under a stronger comparator, or a negative result
was rescued only with an explicit price. It is not a copy of every historical
artifact in the five repositories.

### GU source keys

- `G1`: `GEOMETER-VS-PHYSICS-OBJECTS.md`
- `G2`: `canon/no-go-class-relative-map.md`
- `G3`: `canon/ghost-parity-krein-synthesis.md`
- `G4`: `canon/swing-ghost-parity-no-chiral-selection.md`
- `G5`: `canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md`
- `G6`: `canon/external-by-structure-synthesis-RESULTS.md`
- `G7`: `canon/gamma-traceless-38-adjudication-RESULTS.md`
- `G8`: `canon/hessian-z3-carrier-occupancy-RESULTS.md`
- `G9`: `canon/schwarzschild-weak-field-rfail.md`
- `G10`: `canon/good-stable-compactification-no-go-RESULTS.md`
- `G11`: `canon/source-action-seiberg-witten-RESULTS.md`
- `G12`: `canon/three-generations-locate-not-force-CRT-RESULTS.md`

| ID | First-reading wall or tempting conclusion | What the work actually found | DU consequence | Source |
|---|---|---|---|---|
| `NI-GU-01` | noncompact gauge group means nonunitary/invalid | native object is `Sp(32,32;H)` with a Krein structure; Hilbert positivity was the wrong class | type the state space before applying positivity no-gos | G1 |
| `NI-GU-02` | ghosts must be deleted before physics | Turok-Bateman/ghost parity can grade a positive-norm physical sector while retaining the doubled structure | “ghost present” is not itself a kill; demand the grading map | G3 |
| `NI-GU-03` | ghost parity also chooses the chiral generations | the cross-chirality Krein form makes every maximal positive sector 50/50; net chiral index stays zero | use ghost parity for consistency, never as the missing generation selector | G4 |
| `NI-GU-04` | the ghost-parity construction evades a compact-class no-go from inside that class | the indefinite sector exists because GU exits the compact class; the theorem is inapplicable, not refuted | label scope exits explicitly | G3/G4 |
| `NI-GU-05` | signature `(9,5)` is killed by multi-time Hilbert positivity | the Krein construction absorbs that objection, conditionally | do not count a Hilbert-class wall twice against a Krein model | G1 |
| `NI-GU-06` | the guardian must be a super-Poincare translation generator | GU's guardian is a graded internal spin connection | compare the actual algebraic role, not the shared word “supersymmetry” | G1 |
| `NI-GU-07` | three generations should be an integer index | the located object is an order-3 torsion class; `Hom(Z/3,Z)=0` blocks an automatic integer three | require the explicit torsion-to-multiplicity bridge | G12 |
| `NI-GU-08` | locating a `Z/3` class forces three copies | GU locates a 3-primary arena but does not privilege integer 3; its verified chain can yield one | preserve LOCATE versus FORCE as distinct grades | G12 |
| `NI-GU-09` | pure conformal-gravity failures kill GU gravity | GU's gravitational candidate is induced from `|II|^2`/section geometry, not merely pure conformal Yang-Mills | scope the rival correctly, while keeping GR recovery open | G1/G2 |
| `NI-GU-10` | the DeWitt/gimmel normalization fixes an absolute physical scale | it supplies ratios and signatures; the absolute scale remains structurally free | do not use GU geometry to hide Lambda's coefficient | G1 |
| `NI-GU-11` | “the metric” is one object | base spacetime metric and fiber DeWitt/gimmel metric have different jobs | make every DU metric/count map typed | G1 |
| `NI-GU-12` | Velo-Zwanziger immediately kills the RS sector | the standalone minimally-coupled assumptions may fail for a nondecoupled `ker Gamma` subbundle; escape is conditional on unbuilt symbol/extrinsic-curvature checks | treat it as a live test, not cleared physics | G2 |
| `NI-GU-13` | Witten compactification no-go is a universal wall | noncompact field-space fibers, boundaries, flux or singularities exit its compact smooth class | scope exit buys a new burden; it does not generate families | G2 |
| `NI-GU-14` | Distler-Garibaldi refutes GU | GU is outside the single-`E8` target category; the theorem is not engaged | never advertise inapplicability as refutation of a theorem | G2 |
| `NI-GU-15` | spin-c is enough for the quaternionic index construction | the relevant route needs a real spin precondition; the CP2 example was retired and K3 remains conditional | make topology preconditions explicit in DU imports | G2 |
| `NI-GU-16` | chirality and frame charge have orthogonal supports, so no operator couples them | carrier `V-S` entanglement gives a linear frame-active net-chiral operator with `+16/+32` | the clean no-go was false | G5 |
| `NI-GU-17` | that frame-active operator solves odd generation counting | it is linear, 2-primary and index-conserving; it cannot force an odd count | a counterexample to one proof is not a solution to the target | G5 |
| `NI-GU-18` | weakening Krein compatibility opens an antilinear odd-count loophole | the larger isotropic-eigenspace class remains index-null; definite regradings classify ghost/physical, not chirality | carry the enlarged admissible class into DU no-go audits | G5/G6 |
| `NI-GU-19` | the generation count is merely “not yet found” internally | in the delimited Clifford-RS class, odd count is external by structure; an external topological index can still be any integer | search for the external bridge, not more internal selectors | G6 |
| `NI-GU-20` | gamma-traceless `-38` is a repackaging of ghost-subtracted `-42` | they are distinct K-classes; the former has nonzero order-3 rho classes and differs by two reversed-chirality spin-1/2 units | the live decider is the unbuilt action's carrier choice | G7 |
| `NI-GU-21` | a zero net signature in the carrier is a Hessian zero mode | it is an index, while the Hessian is a nondegenerate `+/-1` saddle; a mass term moves the supposed flat direction | distinguish index, nullity and dynamical eigenvalue | G8 |
| `NI-GU-22` | the Schwarzschild check derived GU's solar-system success | both earlier linear orders were artifacts; harmonicity kills the linear residual and leaves a small quadratic term, but only on an imported Schwarzschild metric | compatibility is not recovery or derivation | G9 |
| `NI-GU-23` | the good-stable no-go is universal | it closes GU-native neutral/adjoint/charged-extremal classes but leaves exotic non-extremal vectors and its positive-majorant premise open | record the surviving class exit and its price | G10 |
| `NI-GU-24` | building the Seiberg-Witten source action should also fix generations | the algebraic action exists and can conditionally address dark energy while remaining orthogonal to the generation-count bridge | one source action need not unify every unresolved channel | G11 |

### Time as Finality source keys

- `T1`: `FORMALISM.md`
- `T2`: `explorations/class-no-go-council-update-2026-07-10.md`
- `T3`: `results/T583` through `T587` result files
- `T4`: `explorations/temporal-issuance-bridge-v0.1.md`
- `T5`: `results/observer-colimit-descent-boundary-v0.1-results.md`
- `T6`: `results/minimal-d1-generalization-v0.1-results.md`

| ID | First reading | Corrected finding | DU consequence | Source |
|---|---|---|---|---|
| `NI-TAF-01` | finality should be one scalar arrow | scalar/vector summaries lose graph, access and gluing information; the supported object is a partial/multiaxis relation | do not scalarize DU finality or credibility | T1 |
| `NI-TAF-02` | a strict monotone should exist in any finite model | closed reversible and stationary zero-resource classes block it; open/nonstationary/resource-accounted systems exit the class | class exit requires an explicit resource/export ledger | T2 |
| `NI-TAF-03` | projection nonfactorization itself proves novelty | a richer neighbor state can absorb it; forgotten structure and strongest completion must be named | every DU novelty claim gets a completion attack | T1 |
| `NI-TAF-04` | adding a capability field makes a projection explanatory | trivial enrichment is always possible; naturality, minimality and physical sourcing are the burden | reject label-only rescues | T3 |
| `NI-TAF-05` | observer records uniquely reconstruct the global order | compatible colimits can be noncanonical; identity, overlap and axis-descent conditions are needed | separate consistency from uniqueness | T5 |
| `NI-TAF-06` | full sheaf machinery is required immediately | finite graph-indexed restrictions and quotient-union descent suffice for current witnesses | use the smallest earned formalism | T1/T6 |
| `NI-TAF-07` | a manifoldlikeness rejection is evidence against the target | the order-dimension diagnostic rejected genuine larger sprinklings more strongly as they improved | calibrate diagnostics on positive target ensembles | T2 |
| `NI-TAF-08` | compression and finality track one another | Rule 30 and Rule 0 supply opposite counterexamples | keep compressibility out of the finality definition unless separately linked | T1 |
| `NI-TAF-09` | Landauer capability supplies an arrow of time | it gives a real source-law capability quotient under a budget, not a temporal order | reuse the capability model without importing time | T3 |
| `NI-TAF-10` | record dependence creates a new temporal partial order | the T586 relation exactly collapses to ordinary task prerequisites; only a typed record filter remains | issued records screen inputs but do not derive time | T3 |
| `NI-TAF-11` | access, intervention, readout, flux or randomness automatically makes a record | none counts without a source-owned stable record consumed by a later task | require a record-issuance rule | T3 |
| `NI-TAF-12` | the same observer finality implies the same hidden source order | identical readout can hide different source order; cadence/access can alter apparent finality without changing the source | finality cannot stand in for issuance | T4 |
| `NI-TAF-13` | local covariant order implies objective becoming | it earns a block-structural causal relation unless an additional becoming discriminator survives | keep covariance and becoming separate | T4 |
| `NI-TAF-14` | record stability can supply Born weights/single outcome | it supplies pointer/access structure only; the probability module remains missing | block the measurement overclaim | T3 |
| `NI-TAF-15` | similar TaF/TI/P2C diagrams identify one object | same shape is not identity; explicit adapter contracts and loss maps are required | cross-repo consilience needs typed transport | T4 |

### Temporal Issuance source keys

- `I1`: `COMPLETION-CLASS.md`
- `I2`: `agent-runs/RUN-0177-physical-witness-completion-tournament.md`
- `I3`: `agent-runs/RUN-0150-h8-d-fork-regime-signature-bundle.md`
- `I4`: RUN-0124 de Sitter, RUN-0108 Everett, RUN-0072/0073 records/Born
- `I5`: `agent-runs/RUN-0131-d-fork-adapter-no-go-synthesis.md`
- `I6`: `LANE-STATE.yaml`, `ANTI-HYPOTHESIS.md`, `KILL-CRITERIA.md`

| ID | First reading | Corrected finding | DU consequence | Source |
|---|---|---|---|---|
| `NI-TI-01` | completed-history absorption is a physical causal explanation | it can block absolute novelty while remaining only a global representation | distinguish ontological containment from dynamics | I1 |
| `NI-TI-02` | more candidate examples will find issuance | twelve physically motivated classes are already absorbed in the bounded tournament | a new candidate needs new structure, not a thirteenth synonym | I2 |
| `NI-TI-03` | the tournament proves a universal no-go | its scope is the declared completion class and candidate inventory | retain a named reopen condition | I2 |
| `NI-TI-04` | de Sitter horizon crossing issues new modes | on fixed background it is an accessible subalgebra of the fixed Bunch-Davies algebra | classify it as disclosure unless the carrier/algebra grows natively | I4 |
| `NI-TI-05` | Everett branching issues realities | fixed-unitary branching decomposes into projection, finalization and loss, not source issuance | do not use branch count as mint evidence | I4 |
| `NI-TI-06` | stable redundant records derive Born weights | pointer stability survives; weights need a separate module | same block as `NI-TAF-14` from another owner | I4 |
| `NI-TI-07` | accessible RSPS traces escape fixed-H quantum mechanics | all inspected traces are absorbed by the fixed Hamiltonian/algebra | a detector distinction must change source structure or observables | I4 |
| `NI-TI-08` | one “issuance rate” is a coherent object | cadence, spectral rate, gap and filtered obstruction have different types and can disagree | type every rate before cross-repo transport | I3/I6 |
| `NI-TI-09` | finite-time novelty, sustained novelty and bounded formal incompleteness are one regime | D-FORK signatures separate them but do not decide which world is realized | treat signatures as tests, not a verdict | I3 |
| `NI-TI-10` | finality/access/records can substitute for source issuance | they are downstream readout/completion objects unless a native source law emits them | preserve source/readout firewall | I5 |
| `NI-TI-11` | a generic fixed-codomain theorem proves GU cannot read its own output | that overreach was corrected; the domain-to-alpha-even bridge is unproved | generic theorems need the construction-specific domain map | I6 |
| `NI-TI-12` | a cross-repo adapter can turn a suggestive GU/P2C model into a physical witness | adapters type evidence; they cannot manufacture missing Hamiltonians, interventions or source laws | abstain on incomplete packets | I5 |
| `NI-TI-13` | randomness is issuance | a fixed stochastic seed/source completion absorbs it unless native carrier growth and anti-after-naming structure survive | stochasticity is not enough | I1/I2 |
| `NI-TI-14` | source and cosmology are separate flagship problems | both reduce to the same D-FORK: fixed disclosure versus native extension | share the discriminator, not the verdict | I3/I6 |

### Possibility to Capability source keys

- `P1`: `explorations/2026-07-16-completion-class-firewall/SYNTHESIS.md`
- `P2`: `explorations/2026-07-19-cross-frame-descent-or-fork/SYNTHESIS.md`
- `P3`: `explorations/2026-07-19-indexed-restriction-diagram/SYNTHESIS.md`
- `P4`: `explorations/2026-07-19-profile-descent-theorem/THEOREM.md`
- `P5`: `explorations/2026-07-20-trit-access-closure/SYNTHESIS.md`
- `P6`: `explorations/2026-07-20-coflip-holonomy-boundary-preflight/SYNTHESIS.md`
- `P7`: `explorations/2026-07-17-self-excitation-boundary-big-swing/SYNTHESIS.md`
- `P8`: `explorations/2026-07-16-decisive-tests/SYNTHESIS.md`

| ID | First reading | Corrected finding | DU consequence | Source |
|---|---|---|---|---|
| `NI-P2C-01` | possibility/access/capability/finality is a universal chronology | it is a family of diagnostic types whose ordering can depend on the construction | do not narrate the hierarchy as cosmic stages | P2/P4 |
| `NI-P2C-02` | global containment removes local capability change | a family may contain a realization while a fixed starting context cannot realize it | keep containment and operational reachability separate | P2 |
| `NI-P2C-03` | one top English label should descend across frames | primitive profiles descend, but any faithful common top label collapses P2C's Access/Capability distinction | preserve construction-indexed outputs | P4 |
| `NI-P2C-04` | unequal capability profiles are intrinsic/context-free | every equalization changes a declared action stage, budget, interface, verifier or horizon | record the price of each collapse | P3 |
| `NI-P2C-05` | forgetting origin yields a harmless quotient | the coarse quotient becomes nondeterministic and erases start embeddings; it is not a bisimulation | require faithful transport, not visual similarity | P3 |
| `NI-P2C-06` | the completion firewall is an ad hoc ban on rivals | frame preservation, outcome independence and a nonconstant diagnostic derive it; unrestricted hull absorption makes the instrument constant | reuse the axioms, not the fixture verdict | P1 |
| `NI-P2C-07` | composite absorbers broadly fail | the survivor hangs on one signature: local-operation invariance | attack that single margin before celebrating | P1 |
| `NI-P2C-08` | three access layers naturally realize GU's trit because `3=3` | the access object is a directed strict chain with trivial automorphism; closing it gives oriented `Z/3`, not unoriented `S3` | arity coincidence is zero structural evidence | P5 |
| `NI-P2C-09` | unknown packet fields can be encoded as false | false means demonstrated absence and true invents a match; the honest result was abstention | add a three-valued/incomplete intake or stop | P6 |
| `NI-P2C-10` | a GU matrix witness is already a P2C physical capability witness | no Hamiltonian, before/after transition, budget, task delta or native response was supplied | point to the gap instead of importing the result | P6 |
| `NI-P2C-11` | self-maintaining boundary feedback solves origin | maintenance does not solve initialization; below viability the boundary dies | separate initiation, maintenance and closure | P7 |
| `NI-P2C-12` | autonomous means resource-free | feedback still needs an energy/resource ledger and a return arrow | autonomy is not ex nihilo sourcing | P7 |
| `NI-P2C-13` | a closed loop explains why the loop exists | closure is not origin and cannot import its desired target physics | block circular source-action stories | P7 |
| `NI-P2C-14` | representation relabel controls are mechanically safe | a partial overlay silently changed an omitted field and produced a false equivalence failure | fixtures must declare inheritance bases or full materialization | P2 |
| `NI-P2C-15` | label-free equals flip-even beyond binary cases | the lemma breaks at alphabet size three; pattern classes split into multiple flip orbits | re-test every binary invariant before trit use | P8 |
| `NI-P2C-16` | synthetic directional tests can pressure realistic rivals | a vacuous detector and scope mismatch earned no pressure; source prerequisites matter | controls must be capable of failing in the rival's domain | P8 |
| `NI-P2C-17` | “located” is close to “forced” | a typed location can remain entirely compatible with completion, resource or access explanations | keep the two words at different grades | P1/P3 |

### Continuity Ledger source keys

- `C1`: `governance/CHARTER.md`
- `C2`: `interfaces/continuity-ledger-transaction-v0.1.md`
- `C3`: `explorations/2026-07-16-r0-individuation-RESULT.md`
- `C4`: `experiments/CL-001-interval-sweep.md`
- `C5`: shared-frame and near-miss control dossiers
- `C6`: `hypotheses/HORIZON.md`
- `C7`: blind-T isolated-return architecture/protocol and stop dossiers

| ID | First reading | Corrected finding | DU consequence | Source |
|---|---|---|---|---|
| `NI-CL-01` | constraints only reduce freedom | binding constraints can create reliable capabilities by stabilizing action surfaces | count enablement as well as restriction | C1/C2 |
| `NI-CL-02` | evaluator intentions determine what is binding | the enforcement substrate determines which constraints can actually bind | separate belief from mechanism | C4 |
| `NI-CL-03` | continuity is conservation of one quantity | continuity can be provenance, entitlement, constraint or causal dependence; losses/imports differ by type | never collapse the ledger to one scalar | C2 |
| `NI-CL-04` | escaping a no-go makes the theorem false | the theorem remains true in its class; the escape ledger records which assumption/class changed | use `N` plus `X`, not “wall defeated” | C1/C2 |
| `NI-CL-05` | a no-go is only an obstacle | transduction can produce the new constraint/no-go that makes a capability reliable | inspect newly created constraints as outputs | C2 |
| `NI-CL-06` | Bitcoin and photosynthesis are an illuminating paired test | they lacked one shared frame, so the comparison was invalid | broad analogy is not an experiment | C4/C6 |
| `NI-CL-07` | an absolute rule must individuate `R0` before comparison | no admissible autonomous rule survived; `R0` behaves like a gauge choice | declare a frame and test paired differences | C3 |
| `NI-CL-08` | failure of absolute `R0` kills discrimination | the preregistered interpretation was wrong: same-frame differences can be invariant even when the frame is conventional | pairing neutralizes arbitrariness | C3 |
| `NI-CL-09` | “matched null” means similar subject matter | it must share `R0`, `M1` and the declared comparison frame | enforce same-frame nulls in DU rivals | C3/C5 |
| `NI-CL-10` | a floor null stipulated to lack the target is strong evidence | it is tautological and often cannot even be populated in the target frame | use positively specified near misses | C5 |
| `NI-CL-11` | testnet and regtest are interchangeable Bitcoin controls | testnet3 changes difficulty rules; regtest is cleaner, yet may still fail the retail frame | validate the control's frame, not its name | C3/C5 |
| `NI-CL-12` | an unexpected third result can be called inconclusive | CL-001 declares instrument failure a kill; no unlisted escape branch exists | preregister outcome exhaustiveness | C4 |
| `NI-CL-13` | a planning summary can safely render repo canon | one summary substituted portfolio paraphrase for charter truth; canon precedence was made explicit | cite owner canon, never a fleet paraphrase as authority | C1 |
| `NI-CL-14` | a tidy evidence table is source extraction | the old layer encoded the analyst's prior, formatted as extraction | mark repo-authored fields and assumptions | C1/C6 |
| `NI-CL-15` | any citation supplies provenance | a citation predating the object it describes is an automatic provenance failure | add temporal/source plausibility checks | C1 |
| `NI-CL-16` | ordinary open-label agent cycles can implement a blind field | the current agent architecture cannot populate the isolated blind `T` without contamination | independence has operational cost and can block work | C7 |
| `NI-CL-17` | more diligence can fix a schema that omits attribution | non-comparability assertions lacked a provenance column; the fix belongs in the format | harden schemas, not reviewer heroics | C1/C3 |
| `NI-CL-18` | a declared shared frame is already evidence that the arms fit it | the frame is construction authority; later source population can still falsify it | distinguish preregistration from source support | C5 |

## Persona-register disposition addendum

The original 100 suggestions remain intact. The executed swing changes only
these item dispositions; it does not rewrite their text or close their broader
work packages.

| Persona item | Disposition after this pass | Evidence / surviving burden |
|---|---|---|
| `P01-A` | `PARTIAL_SCOPED` | local and literal causal-past `N` plus complete-Q phenomenologies built; order-first growth and a response/noise-complete action remain open |
| `P01-B` | `SCOPED_FAIL_BUILT_COMPLETIONS` | local acceleration is superluminal; conserved causal memory tracks and does not accelerate; interacting-vacuum envelope is always on early |
| `P02-A` | `ACTIVE_EXPANDED` | local growth and full retarded-background generators now exist; common-past covariance is exact; no viable background warrants likelihood yet |
| `P02-B` | `PARTIAL_STRONG_KILL` | raw causal memory has `Omega_X(z=1100)=0.989`, no matter era, `q0=0.526`, and large `H(z)` errors; full likelihood is deliberately not run |
| `P04-A` | `OPEN_NEXT_FRONTIER` | CMF-01 shows metric-seeded causality is calibration; label-invariant order-first growth with Bell-causality/normalization remains the live build |
| `P14-A` | `SCOPED_FAIL_BUILT_COMPLETIONS` | the bi-wave exits the local principal class, but every built scale-free causal-memory background tracks or fails to accelerate |
| `P14-B` | `PARTIAL_SCOPED` | bi-wave characteristics are metric-null, but full finite-k feedback and action positivity remain open; background already fails |
| `P15-A` | `PARTIAL_EXECUTABLE` | literal causal volume, local counter, bi-wave memory, martingale, offset and order-first cardinality are explicitly separated; full repo diagram open |
| `P17-B` | `PARTIAL` | one common tournament now compares literal causal set, nonlocal bi-wave, stochastic and generated-scale branches; broader rival set remains open |
| `P19-A` | `SCOPED_FAIL_SCALE_FREE` | local coupling collapses to Lambda; causal-memory late calibration makes early density order one; only a generated dimensional scale remains live |
| `P30-A` | `PARTIAL` | CMF-01 now compares against everpresent-Lambda and nonlocal-gravity primary constructions without claiming their grades; full compression scorecard open |
| `P44-A` | `PARTIAL_SCOPED` | local and retarded state/complete-transfer equations explicit; stress-consistent CTP action and source/resource ledger open |
| `P44-B` | `PARTIAL_SCOPED` | local failure injection, nonlocal tracker kill, sign survival and offset controls executed; generated-scale nonlinear feedback remains open |
| `P45-A` | `PARTIAL` | a precise causal martingale law was tested, but its mark variance, growth law and return arrow remain imported rather than action-derived |

## Orchestrated next sequence

1. **`SWING-DU-COV-02`: COMPLETED — `VIABLE_ONLY_AS_LAMBDA_LIMIT`.** Preserve
   the local result; its no-go is explicitly class-relative.
2. **`SWING-DU-CMF-01`: COMPLETED — `CAUSAL_ESCAPE_TRACKER_FAIL`.** Literal
   causal volume, a metric-null bi-wave proxy and an order-first martingale were
   built. Nonlocality escapes the local cone, but scale-free memory is an
   always-on/nonaccelerating tracker and the raw martingale fails early RMS,
   sign-persistence and de Sitter-stationarity controls.
3. **`HC-DU-011A` full covariance passport and small-causet harness.** This is
   the first build in the next major program. Distinguish statewise relabeling
   equivariance from equal path weight across every natural labeling; test
   normalization, spectator/Bell behavior, past immutability and whether
   coupling updates are physical records or gauge bookkeeping. Direct
   cardinality-running transitive percolation is now a killed control.
4. **Two-route feedback/transmutation assay (`HC-DU-011 + HC-DU-022`).** Only
   after `HC-DU-011A` passes, test (a) effective coupling renormalization at
   covariant order landmarks and (b) coupling updates written as physical
   causal records. Seek a regulator-stable hierarchy relative to one declared
   microscopic unit; dimensionless order does not create physical units ex
   nihilo. No third family before these receive distinct dispositions.
5. **Complete the typed-`N` diagram (`HC-DU-007`).** CMF-01 supplies the
   executable counterexamples; extend them across algebraic, observer, durable-
   record and novelty counts with units and lossy/nonexistent maps.
6. **Response/noise action and overlap spectrum (`HC-DU-003/004/005`).** Only
   after a generated-scale background survives, construct the CTP/noise kernel,
   finite-k determinant and common-past `P_Lambda(k,z)`; do not select a good seed.
7. **Independent reimplementation (`HC-DU-009`).** Give the exact CMF-01
   equations and preregistered outcomes to a clean-room implementer and compare
   frozen JSON before credibility promotion.
8. **Cross-repo hardening (`HC-DU-019/020/024`).** Keep TaF/TI/P2C/CL negative
   models as fixtures and run initial-surface/kernel sweeps in the same declared
   frame rather than rerunning their searches under new names.

## Pre-registration for `SWING-DU-COV-02`

**Question.** Can the forced background exchange be lifted to a covariant,
local-enough physical model with stable perturbations and a credible cosmic
history without choosing `Q(a)`, a preferred slicing or a target `H(z)`?

**Required build.** A declared local/global status for `N`; a covariant source
law; action or complete `Q^mu`; gauge-invariant linear scalar equations; sound
speeds and kinetic signs; matter-density positivity; early-DE and growth
curves; constant-Lambda and unstable-interaction controls.

**Outcomes.**

1. `COVARIANT_PERTURBATIVELY_VIABLE`: all structural and stability gates pass;
   empirical fitting becomes warranted.
2. `BACKGROUND_ONLY`: the FLRW construction cannot be lifted without an
   arbitrary/nonlocal/preferred-frame prescription.
3. `COVARIANT_BUT_UNSTABLE`: a lift exists but perturbations kill it.
4. `VIABLE_ONLY_AS_LAMBDA_LIMIT`: the allowed interaction collapses toward
   `beta=0`, leaving the count law explanatorily idle.
5. `REIMPORTS_TARGET_HISTORY`: a free `Q(a)`, sound speed or boundary history
   does the work.

**Hard kill.** Any construction that calls a global cumulative count a local
scalar without a transport law, or that suppresses perturbations by selecting
an arbitrary rest-frame prescription after seeing the result, is
`BACKGROUND_ONLY` or `REIMPORTS_TARGET_HISTORY`, not a physical completion.

## Execution disposition for `SWING-DU-COV-02`

Executed in
`explorations/lambda-N-covariant-perturbation-kill-2026-07-21.md` with foreground
probe `tests/du_lambda_N_covariant_perturbation_kill.py` and frozen JSON artifact.

- A local covariant lift exists:
  `u.nabla N=kappa(Theta/3)^-3`, `V=A/sqrt(N)`,
  `Q_vac,mu=-nabla_mu V`. It reproduces COV-01 and fixes momentum transfer.
- Its gauge-invariant scalar principal speed is
  `c_N^2=beta Omega_V^3/[2(1-Omega_V)]`.
- At every accelerating COV-01 fixed point, `c_N^2=3 Omega_V*>1` exactly.
- The geodesic zero-sound prescription would force both `delta N_com=0` and,
  through the declared transport, `deltaTheta_com=0` for `beta>0`; it cannot
  preserve ordinary growing structure.
- A finite growth probe plus constant-Lambda and unstable-sign controls passes
  `18/18`; its weak unit-force/gravity discriminator at `k=0.1 h/Mpc` gives
  `beta~1.03e-5`, where `|Delta Lambda/Lambda|<1e-6` since `z=2`.
- A causal-past volume is covariant and retarded but has a history-dependent
  `kappa_eff`; it is a separate nonlocal model, not this background's lift.

Pre-registered outcome: **`VIABLE_ONLY_AS_LAMBDA_LIMIT`**. Scope: the declared
constant-`kappa` local lift. No universal no-go for every causal-set, nonlocal
or UV completion is claimed.

## Execution disposition for `SWING-DU-CMF-01`

Joe directed an orchestrated wild frontier heterodox swing after COV-02. It is
executed in
`explorations/causal-memory-order-first-martingale-frontier-2026-07-21.md`
with foreground probe `tests/du_causal_memory_frontier_probe.py` and a frozen
JSON artifact.

Three independently attacked branches were kept distinct:

- the literal unweighted causal-past count `N_J`;
- the metric-null bi-wave memory `N_box=8 pi Box_ret^-2 1`;
- the order-first signed causal martingale `Lambda=lambda S_N/N`.

Root re-derivation establishes:

- `C_J(p)=pi/[(1+3p)(1+p)(3+p)]` exactly for `a=t^p`;
- `C_box(p)=pi/[3(1+3p)(1+p)]` and
  `C_J/C_box=3/(p+3)`, so the proxy is not silently an event count;
- the bi-wave principal polynomial is `(g^ab k_a k_b)^2`, a genuine
  metric-null escape from COV-02's local `c_N^2=3 Omega` class;
- a separately conserved `A/sqrt(N_J)` has
  `w_X=-1+2/(3p)`, hence it tracks radiation and matter rather than accelerating;
- the full late-calibrated background gives `Omega_X(z=1100)=0.989`,
  `q0=0.526`, no standard matter era, and `H/H_LCDM(z=2)=1.792`;
- imposing only `Omega_rms,radiation<0.02` makes a martingale late target of
  `0.69` a `210 sigma` realization;
- its probability of remaining positive from `z=2` to `0`, conditional on
  starting positive, is `0.0236` in the matter-era Brownian benchmark;
- common-past overlap fixes the 3+1 Minkowski equal-time correlation
  `rho(s)=1-s+s^3/4-s^4/16`, with half-correlation at `r/T=0.53277`;
- raw full-past memory grows linearly in de Sitter, so its RMS decays as
  `T^-1/2` rather than approaching constant `Lambda`;
- an offset can suppress the early component only by taking `t_c~t_0`, the
  explicit `REIMPORTS_COSMIC_CLOCK` control.

Pre-registered outcome: **`CAUSAL_ESCAPE_TRACKER_FAIL`**. The local no-go was
class-relative, but nonlocality and stochastic sign are not sufficient. The
surviving frontier couples `HC-DU-011` and `HC-DU-022`: an order-first,
label-invariant growth/action law with feedback and an endogenously generated
dimensional memory scale. No sibling claim, canon or public posture moves.

## Run receipt

- Cross-repo work was read-only and pinned; GU's pre-existing dirty state was
  preserved.
- All 100 persona suggestions remain in their original stable-ID register.
- Thirty hardening items now have stable IDs, priorities, owners, grades and
  exact next discriminators.
- Eighty-eight non-intuitive/class-relative findings are preserved above.
- The COV-01 P0 background swing generated a frozen JSON receipt.
- `SWING-DU-COV-02` subsequently executed with `18/18` checks and returned
  `VIABLE_ONLY_AS_LAMBDA_LIMIT`; the original preregistration above remains intact.
- `SWING-DU-CMF-01` subsequently executed with `45/45` checks and returned
  `CAUSAL_ESCAPE_TRACKER_FAIL`; all individual persona suggestions remain intact.
- No physics claim, sibling-repo verdict, canon status or public posture moved.
