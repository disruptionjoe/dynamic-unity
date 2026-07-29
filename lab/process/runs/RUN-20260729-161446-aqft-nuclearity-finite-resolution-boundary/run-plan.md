---
run_id: RUN-20260729-161446-aqft-nuclearity-finite-resolution-boundary
status: completed
started_at: 2026-07-29T16:14:46-05:00
completed_at: 2026-07-29T16:22:20-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-AQFT-NUCLEARITY-FINITE-RESOLUTION-RECORD-BOUNDARY
claim_id: HC-DU-131
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 exact-finite versus nuclear finite-resolution necessity, infinite-rank first-leak, and symmetry-selection boundary plus conditional Grade 3 target-relative finite-resolution reconstruction; no selected QFT, state, region, nuclearity scale, finite coordinates, instrument, observer, record interface, empirical excess, new law, new physics, or prediction"
external_action_authorization: "Repository-local proof, bounded primary-source collision, minimal exact regression, evidence/authority integration, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
frozen_read_revisions:
  dynamic_unity_parent: a3401d2eea7f188479f3b277b03a80096c794393
lane_selection:
  owner: dynamic-unity
  primary_lane_id: "1"
  supporting_lane_ids:
    - "3"
    - "4"
    - "6"
    - "7"
  manifest_revision: 97
  manifest_sha256: 7d8bf6650a229fdac42dd63397fbc15352e42457d9f70ea0e036f8003573d80a
  current_research_revision: 81
  current_research_sha256: e8074a18dc657f0b3edf29fe130ede71392265bcffcf9ba1db066e7e798e89aa
  branch: agent/research-compute-cleanup-2026-07-22
  selection_basis: "Joe authorized the next bounded successor. DU is explicitly quiescent. HC-DU-128--130 progress from complete functionals to finite Gaussian packets to covariant indexed local families, but leave exact continuum support outside every finite packet. HC-DU-095--098 already prove generic compactness and observability conditions, so another abstract finite-cover argument would duplicate them. This run instead tests the established AQFT phase-space/nuclearity route as the strongest physical finite-resolution bridge and asks exactly what it selects versus only approximates."
write_boundary:
  - lab/process/runs/RUN-20260729-161446-aqft-nuclearity-finite-resolution-boundary/run-plan.md
  - explorations/aqft-nuclearity-effective-finite-resolution-reconstruction-and-interface-selection-boundary-2026-07-29.md
  - tests/du_aqft_nuclearity_finite_resolution_boundary_probe.py
  - tests/artifacts/du_aqft_nuclearity_finite_resolution_boundary_result.json
  - CURRENT-RESEARCH.yaml
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - docs/quantum-foundations-orientation-surface.md
  - explorations/concept-register.md
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
---

# AQFT nuclearity and the finite-resolution record boundary

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether independently
selected, observer-indexed certified causal records reconstruct all
observer-accessible time, geometry, fields, and capability, or leave a finite
physical remainder.

The current authority is quiescent at revision 81. `HC-DU-130` established:

```text
finite local continuum packet
  + translation covariance
  -> region-indexed family with infinite global orbit

finite Gaussian packet
  -> exact restricted-state reconstruction
  -/-> continuum completion.
```

The remaining question is whether a real QFT phase-space condition converts
that exact infinite boundary into a controlled finite-resolution bridge
without pretending to select a record interface.

## Typed arena

Let \(X,Y\) be Banach spaces and let \(T:X\to Y\) be a nuclear map:

\[
Tx=\sum_{j\geq1}\phi_j(x)y_j,
\qquad
\sum_{j\geq1}\|\phi_j\|\,\|y_j\|<\infty.
\]

For AQFT, the standard energy-nuclearity specimen is the map

\[
\Theta_{\beta,O}:A\longmapsto e^{-\beta H}A\Omega
\]

from the unit ball of the supplied local algebra \(\mathcal A(O)\) into the
vacuum Hilbert space. The region \(O\), Hamiltonian \(H\), vacuum/state
\(\Omega\), damping scale \(\beta\), algebra, and representation are supplied
antecedents.

Keep distinct:

1. compact or nuclear image of a unit ball;
2. finite-rank approximation at tolerance \(\epsilon>0\);
3. exact finite-dimensional range;
4. selected finite coordinates;
5. physically formed finite observations of those coordinates;
6. target-relative reconstruction; and
7. exact continuum-state reconstruction.

## Assumptions and warrants

### `STANDARD`

- elementary Banach/Hilbert nuclear and compact-operator theory;
- finite-rank factorization and Hahn--Banach separation;
- the standard AQFT energy-nuclearity and split-property definitions; and
- exact finite linear algebra for symmetry controls.

### `CONDITIONAL_POSIT`

- a QFT net, representation, local region, Hamiltonian, state, and scale for
  which the declared nuclearity condition holds;
- a target Lipschitz on the nuclear image in the declared norm;
- any finite-rank approximation and acquisition map used as a record; and
- a frozen capability/error tolerance.

These are inputs, not results.

### Warrants

- `DERIVED`: nuclear tail approximation, infinite-rank exact-finite no-go,
  target-relative error theorem, and symmetry obstruction.
- `CONSTRUCTIVELY_REALIZED`: diagonal nuclear control, finite-rank tail
  witnesses, same-finite-record/different-tail witnesses, and irreducible
  symmetry control.

## Pre-registered theorem spine

### Proposition 1 — nuclearity gives finite resolution, not finite truth

For partial sums

\[
T_Nx=\sum_{j=1}^N\phi_j(x)y_j,
\]

\[
\|T-T_N\|
\leq
\sum_{j>N}\|\phi_j\|\,\|y_j\|
\longrightarrow0.
\]

Thus the image of the unit ball is totally bounded and has finite-rank
approximations at every nonzero tolerance. Nuclearity does not imply that
the tail terminates or that \(T\) has finite rank.

### Proposition 2 — every exact finite record leaks on an infinite-rank map

Let \(R:X\to\mathbb R^m\) be any finite-rank linear record. If

\[
Rx=Rx'\Longrightarrow Tx=Tx'
\]

for all \(x,x'\), then \(\ker R\subseteq\ker T\), so \(T\) factors through
the finite-dimensional quotient \(X/\ker R\). Hence \(T\) has finite rank.

Contrapositively, if \(T\) has infinite rank, every finite-rank exact record
has a same-record/different-\(T\) witness. A continuous linear target on
\(Y\) separates the two outputs.

### Proposition 3 — conditional finite-resolution reconstruction

If \(\|T-T_N\|\leq\eta\) on the unit ball and a target \(F\) is
\(L\)-Lipschitz on \(T(B_X)\), then

\[
T_Nx=T_Nx'
\Longrightarrow
|F(Tx)-F(Tx')|\leq2L\eta.
\]

This is a target-resolution certificate relative to a supplied approximation
and exact finite coordinates. Physical acquisition, digitization, lineage,
and confidence add further error and remain separate.

### Proposition 4 — covariance may select a multiplet, not its coordinates

In a two-dimensional irreducible real rotation representation, every
linear projector commuting with the full rotation group is \(0\) or \(I\).
Therefore no symmetry-equivariant rule selects one rank-one coordinate
inside the degenerate block. Keeping the entire multiplet is covariant;
choosing a basis vector needs additional asymmetry/reference structure.

This is a scoped control, not a universal no-selector theorem.

## Hostile controls

The run must preserve:

- a nuclear infinite-rank diagonal map;
- exact finite-rank maps as a positive escape;
- finite-resolution tail convergence;
- a same-finite-record/different-tail witness at every tested rank;
- a target inside the retained range that reconstructs;
- a target on the first omitted direction that leaks;
- an invariant full degenerate multiplet; and
- failure of every nontrivial rank-one orthogonal projector to commute with
  the full rotation control family.

## Literature collision and prior-work boundary

The run must collide with:

- Buchholz--Wichmann energy nuclearity and its phase-space interpretation;
- Haag--Swieca compactness;
- the nuclearity-to-split-property literature;
- locally covariant and modular nuclearity results; and
- DU's existing `HC-DU-040B`, `HC-DU-057`, `HC-DU-095--098`, and
  `HC-DU-128--130`.

The likely novelty verdict is absorption. The intended DU increment is the
typed composition of physical phase-space compactness with exact finite
record, finite-resolution reconstruction, and interface-selection boundaries.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** AQFT nuclearity/split-property theory plus compact
  and nuclear operator approximation.
- **Cheapest kill:** an admitted nuclearity theorem that canonically selects
  a physically formed finite coordinate/archive interface, or a proof that
  nuclearity itself makes the relevant map finite rank.
- **Positive control:** a nuclear infinite-rank map with arbitrarily accurate
  finite-rank approximants.
- **Stop:** stop after typing the exact/approximate boundary, preserving the
  finite-rank and symmetry controls, and testing one real AQFT nuclearity
  family. Do not simulate a field, construct a detector, or reopen generic
  compactness.

## Local-model learning gate

Direct proof and primary literature supply the result. The executable artifact
is a minimal deterministic regression of diagonal nuclear tails, finite-rank
factorization, exact tail witnesses, and symmetry commutators. It is not an
admitted simulation or learning model.

Disposition: `PROOF_FIRST_MINIMAL_REGRESSION_ONLY`.

External hardware is irrelevant.

## Durable return

One dated exploration, exact regression and artifact, appended completion
receipt, and only the live/register surfaces needed to bank the scoped result.
No paper seed, selected successor, ontology promotion, hardware note,
cross-repository claim, or external action.

## Completion receipt

Disposition:

```text
AQFT_NUCLEARITY_SUPPLIES_A_PHYSICAL_FINITE_RESOLUTION_BRIDGE
+INFINITE_RANK_STILL_FORBIDS_EXACT_FINITE_LINEAR_RECORD_COMPLETENESS
+FINITE_RANK_IS_THE_EXACT_ESCAPE
+LIPSCHITZ_TARGETS_INHERIT_A_2Leta_TAIL_BOUND
+SYMMETRY_CAN_SELECT_A_MULTIPLET_WITHOUT_SELECTING_COORDINATES
+NUCLEARITY_DOES_NOT_SELECT_A_PHYSICAL_RECORD_INTERFACE
+NO_READY_SUCCESSOR
```

The exact diagonal control is nuclear with norm one and infinite rank. Every
tested finite truncation has its predicted nonzero nuclear/operator tail and
a same-record/different-target witness saturating the target-error bound.
Every tested genuinely finite-rank map closes exactly. The full rotation
multiplet is invariant while every tested rank-one coordinate projector
fails equivariance.

The primary-source collision found mature absorption in Haag--Swieca
compactness, Buchholz--Wichmann energy nuclearity, nuclearity/split-property
theory, and locally covariant/modular nuclearity. Their useful physical
increment over `HC-DU-095--098` is a genuine QFT phase-space condition, not a
selected coordinate, instrument, archive, observer, or record.

Validation:

- `python3 tests/du_positive_functional_qft_reconstruction_probe.py` —
  **PASS**, `27/27`;
- `python3 tests/du_gaussian_finite_record_ladder_probe.py` — **PASS**,
  `33/33`;
- `python3 tests/du_covariant_local_finite_mode_trilemma_probe.py` —
  **PASS**, `36/36`;
- `python3 tests/du_aqft_nuclearity_finite_resolution_boundary_probe.py` —
  **PASS**, `38/38`; and
- `python3 tests/du_agent_orientation_contract_probe.py` — **PASS**,
  `37/37`, cold-start `5984/6000`.

The repo returns quiescent at `CURRENT-RESEARCH.yaml` revision 82. No
scientific successor, paper seed, hardware path, provider action, external
contact, or cross-repository claim is selected.
