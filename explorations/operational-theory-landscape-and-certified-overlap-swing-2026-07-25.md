---
title: "Operational theory landscape and certified-overlap identity swing"
status: completed_exact_finite_control
date: 2026-07-25
run_id: RUN-20260725-075017-operational-theory-landscape
claim_grade: "EXACT FINITE CALIBRATION + TYPED IDENTITY PILOT / KNOWN COMPONENT MATHEMATICS / PHYSICAL SELECTION OPEN"
program_refs:
  - HC-DU-035C
  - H-CCR-15
  - H-CCR-16
  - CONCEPT-DU-011
---

# Operational theory landscape and certified-overlap identity

## 1. Question

Can the generalized-probabilistic-theory landscape, the two-sided
classical/quantum/super-quantum squeeze, the distinction between proven
nonexistence and mere failure to construct, and the generalized
common-cause exit improve Dynamic Unity's current research rather than create
another Bell-theory orbit?

The answer from this swing is **yes, as a research contract and as a sharper
overlap-identity result**.

The known Bell/GPT results are not Dynamic Unity novelty. The advance inside
DU is that they expose two independent coordinates that the program had been
partly conflating:

1. **theory-class expressiveness** — local, quantum, no-signalling, arbitrary
   conditional; and
2. **identity resolution** — which occurrences in different contexts are
   required to denote one effect, instrument, history, provenance value, or
   upper action.

An obstruction can be removed by moving to a more expressive theory or by
weakening the proposed identity map. Those are different scientific moves.

## 2. Frozen calibration

For the binary CHSH interface, freeze the complete table `p(a,b|x,y)`,
setting identities, measurement independence, tensor/commuting separation,
and output semantics.

The executable classifier then keeps these receipts separate:

```text
valid conditional behavior
    -> no-signalling or signalling
    -> local extension or exact local obstruction
    -> explicit quantum realization, quantum exclusion, or unresolved status
    -> no-signalling permissive class.
```

It never infers quantum membership merely because a behavior does not violate
the tested quantum bound.

## 3. Exact CHSH results

`tests/du_operational_theory_landscape_probe.py` returns `28/28`.

| Fixture | CHSH | Local receipt | Quantum receipt | Correct disposition |
|---|---:|---|---|---|
| deterministic local | `2` | exact global extension | local classical embedding | local |
| isotropic `v=1/2` | `2` | exact global extension | local classical embedding | local boundary |
| rational Bell-state point | `14/5` | exact Farkas obstruction | explicit exact state and measurements | quantum nonlocal |
| same rational behavior, realization withheld | `14/5` | exact Farkas obstruction | none supplied | quantum status unresolved |
| Tsirelson point | `2 sqrt(2)` | direct CHSH witness | explicit exact algebraic state and measurements | quantum boundary |
| isotropic `v=3/4` | `3` | exact Farkas obstruction | exact Tsirelson exclusion | no-signalling post-quantum |
| PR box | `4` | exact Farkas obstruction | exact Tsirelson exclusion | no-signalling post-quantum |
| signalling control | `2` | classification stopped | no-signalling contract fails | outside nested landscape |
| invalid table | n/a | classification stopped | classification stopped | invalid |

The rational quantum point is not a numerical approximation. With the Bell
state, Alice measures `Z` and `X`; Bob measures `(3Z+4X)/5` and
`(3Z-4X)/5`. The complete Born table is rational and gives

\[
S=\frac35+\frac35+\frac45-\left(-\frac45\right)=\frac{14}{5}.
\]

The exact marginal compiler proves that no joint distribution on
`A0,A1,B0,B1` reproduces it, while the explicit state and four observables
constructively realize it in ordinary quantum theory.

The withheld-realization twin is deliberately the same behavior. Its physical
position has not changed; only the evidence supplied to the adjudicator has.
It therefore returns `QUANTUM_STATUS_UNRESOLVED`. This is the cleanest
force-versus-permit control:

> Satisfying a necessary quantum bound permits quantum membership; it does not
> prove it.

## 4. Certified-overlap identity pilot

`tests/du_certified_overlap_identity_probe.py` returns `16/16`.

### 4.1 Quantum instrument result

Three exact one-qubit Z instruments share the same record label:

1. the ordinary QND Z instrument;
2. a Kraus implementation with an outcome-dependent Z phase; and
3. a context-dependent post-record X flip.

The phase implementation induces the same complete selective CP maps as the
QND instrument. It is an implementation gauge and is correctly quotiented.

The X-flip rival has:

- exactly the same two POVM effects;
- exactly the same outcome probabilities on a tomographically complete set
  of physical probe states;
- a trace-preserving nonselective instrument; but
- different selective CP maps and the opposite next-Z continuation after
  each nonzero record.

Thus:

```text
same measurement label
    + same complete single-time outcome statistics
    != same multi-time record instrument
    != same future capability.
```

The result does not refute outcome-effect identity. It proves that outcome
identity and history/action identity are different typed claims.

### 4.2 Authenticated protocol result

Two route messages can both:

- authenticate correctly;
- name the same origin; and
- carry the same epoch;

while carrying different values. Authentication certifies each occurrence,
not one canonical cross-route value.

A formed origin/epoch/value commitment gives a positive identity receipt in
the bounded fixture when the commitments agree. A mismatch proves
equivocation and requires safe rejection. A cross-epoch pair is not silently
identified.

The quantum and protocol controls now share the same ladder:

```text
same label
    != same local occurrence
    != same effect/value
    != same complete process/history
    != same upper action.
```

## 5. Transfer to the existing DU fixtures

### Authenticated regional protocol

- **Restrictive foil:** one canonical origin value across routes.
- **Exclusion receipt:** exact dual obstruction.
- **Formed realization:** route/epoch-provenance global process.
- **Adversarial disposition:** safe rejection because the formed provenance
  exposes equivocation.
- **Permissive foil:** unrelated value per occurrence.
- **Selection principle:** formed origin/route/epoch/value commitments plus a
  declared equivocation and failure-domain contract.

### Mermin--Peres instruments

- **Restrictive foil:** one context-independent preassigned value for every
  repeated observable.
- **Exclusion receipt:** inclusion-minimal exact dual obstruction.
- **Formed realization:** complete ordinary context-indexed quantum
  instruments.
- **Permissive foil:** unrelated variable for every context occurrence.
- **Selection principle:** independently certified effect or instrument
  equivalence, compatibility/nondisturbance, repeatability, and disturbance
  accounting at the level the claim requires.

The contextuality result still does not show that the quantum process fails.
The new result says more precisely why a future DU physical experiment must
match complete instruments rather than only record marginals.

## 6. Repo-wide application map

This is a preliminary approach map, not a verdict on the hypotheses.

| Hypothesis | Restrictive foil | Target middle | Permissive absorber/foil | Next decisive receipt |
|---|---|---|---|---|
| `H-CCR-01` record selection | inserted preferred basis | dynamically/equivariantly selected record algebra | post-hoc interface per result | unchanged selector under symmetry, perturbation and held-out access |
| `H-CCR-02` history difference | terminal-state sufficiency | complete multi-time process | arbitrary hidden history tag | formed held-out continuation after matched endpoints |
| `H-CCR-03` public threshold | trusted coordinator/count threshold | explicit adversarial certificate process | unconstrained rejection or oracle | matched split-view and safety/liveness receipts |
| `H-CCR-04` public stable algebra | raw dephasing/redundancy | selected broadcastable stable algebra | inserted code/pointer algebra | same-data absorber plus independent formation selector |
| `H-CCR-05` record sufficiency | supplied coarse record | admissible target-independent refinement class | target-defined behavioral quotient | bounded separating intervention after completion battery |
| `H-CCR-06` finality capability | confidence or finality label alone | matched-risk, matched-resource action gain | free controller/access expansion | exact task transition under frozen budget |
| `H-CCR-07` finality resource | free hardening | resource/optionality tradeoff | uncharged environment/export | complete cross-boundary ledger and countermodel |
| `H-CCR-08` provenance | terminal outcome equality | formed meta-record sufficient for held-out action | after-the-fact complete log | provenance twin with future intervention |
| `H-CCR-09` observer role | named observer/node | minimal intervention-stable role cover | arbitrary fitted cover | label/refinement-invariant held-out separator |
| `H-CCR-10` fresh records | preloaded path tape | physically formed bounded source/transducer | unrestricted oracle or output tape | future-independence and resource receipt |
| `H-CCR-11` global clock | physical hidden scheduler | quotient/gauge under complete interventions | frame-refitted scheduler | Lorentz-sensitive witness or exact factorization |
| `H-CCR-12` cross-platform invariant | verbal analogy | one normalized quantity with unchanged meaning | platform-specific redefinition | unchanged compiler and unit/resource semantics |
| `H-CCR-13` public holonomy | forced path equality | equalizer/provenance lift | retain every route label | nontrivial implementation-complete loop witness |
| `H-CCR-14` connectivity frustration | tree/no-loop model | formed syndrome repair/reject/lift | reject every difficult case | matched noisy/adversarial capability comparison |
| `H-CCR-15` physical remainder | incomplete retained-memory model | implementation-complete ordinary quantum process | signalling/nonlinear escape | residual after complete causal break |
| `H-CCR-16` regional descent | one completed global biography | typed certified overlaps and action-safe composition | split every occurrence | physical overlap-identity selector plus sparse recursive composition |

The map changes immediate priority only for `H-CCR-16`, because that is where
the necessary exact compiler and transfer fixtures already exist.

## 7. What was actually learned

### 7.1 Evidence status is not a theory class

`UNDERIDENTIFIED` and `QUANTUM_STATUS_UNRESOLVED` describe the adjudicator's
evidence, not another physical theory between quantum and post-quantum.

### 7.2 Overlap identity is a vector

The prior phrase “certified overlap identity” was still too scalar. A record
claim must name whether it needs equality of:

- effects;
- selective maps;
- full multi-time continuation;
- provenance/value; or
- upper action.

This is the main substantive advance of the swing.

### 7.3 Moving a boundary and splitting an identity are not the same

Adding a formed context/provenance register enlarges the process boundary with
physical evidence. Splitting every occurrence without a formed register only
weakens the comparison contract. Both can restore a global extension, but
only the first is a candidate physical explanation.

### 7.4 The constructive causal exit remains open

Quantum causal models show that Bell-classical factorization can be replaced
without merely adding a superluminal signal. DU has not yet shown that its
regional records select a distinctive generalized causal factorization or
exclude PR-like behavior for a new reason.

### 7.5 A “finality Tsirelson bound” is not ready

It is a potentially profound direction, but the repo still lacks one
operational finality quantity with unchanged meaning across classical,
quantum, distributed, and permissive GPT fixtures. A 2026 causally local
stochastic-process derivation of the CHSH bound also creates an immediate
collision class for any causal-locality route. The analogy remains useful;
the law does not yet exist.

## 8. Candidate theorem and conjecture surfaces

These are retained at exploration grade only.

### Finite instrument identity separation lemma

For finite-dimensional instruments, equality of every selective linear map on
an operator basis is sufficient for equality under every admitted linear
continuation. If two instruments have the same effects but unequal selective
maps, a finite preparation-and-continuation witness exists.

This is standard finite linear algebra/process tomography. DU's possible
contribution is its placement as the mandatory identity receipt before
recursive regional descent, not the lemma alone.

### Typed overlap descent conjecture

Relative to a declared upper task, regional composition requires identity
only at the weakest level sufficient for every admitted upper continuation.
Stronger identity is unnecessary; weaker identity either produces a finite
continuation witness or leaves the task underidentified.

This may become a useful theorem if “weakest level” is constructed
non-circularly from independently frozen instruments and a bounded
continuation class.

### Regional finality bound conjecture

There may exist a resource-normalized upper bound on mutually certifiable
public distinctions for ordinary quantum regional processes that is stricter
than a no-signalling/GPT bound and looser than a classical common-cause bound.

No quantity, theorem, or prediction is yet supplied.

## 9. Prepared next actions

### `OI-NEXT-02` — robust typed instrument identity

- Replace exact maps with calibrated confidence regions.
- Add drift, leakage, memory, context dependence and adversarial adaptivity.
- Require a predeclared equivalence margin and held-out continuation family.
- Negative result: physical overlap identity remains underidentified at the
  required history/action level.

### `OI-NEXT-03` — physical sequential-context transfer

- Apply the exact typed receipt to one implementation-complete sequential
  contextuality or proper-time-history instrument.
- Match outcome effects, complete selective maps, controller, environment and
  context record.
- Test whether any proposed layered-finality difference survives.

### `TL-NEXT-01` — scalable quantum landscape

- Add an optional NPA outer-exclusion adapter only when a scenario outgrows
  explicit realizations and known exact bounds.
- Preserve `NOT_EXCLUDED` versus `REALIZED`.
- Do not make generic quantum-set compilation the bottleneck for
  `H-CCR-16`.

### `RC-NEXT-01` — recursive vector defect

- Compose effect/instrument/history identity uncertainty separately from
  marginal incompatibility and upper-action defect.
- Test correlated errors and benign subdivision before seeking a scalar law.

## 10. Disposition

- Install the operational theory-landscape contract as a reusable research
  instrument.
- Extend `HC-DU-035C`, `H-CCR-16`, and `CONCEPT-DU-011`.
- Mark the exact typed overlap-identity pilot complete at finite control
  grade.
- Keep physical overlap selection, robust calibration, sparse compilation,
  recursive defect composition, generalized causal reconstruction and any
  regional-finality bound open.
- Add no new core hypothesis ID, physical prediction, ontology, paper
  priority, Factory state, submission, publication, or external action.
