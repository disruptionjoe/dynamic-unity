---
run_id: RUN-20260729-162943-aqft-spectral-cutoff-width-finite-probe-boundary
status: completed
started_at: 2026-07-29T16:29:43-05:00
completed_at: 2026-07-29T16:36:32-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-AQFT-SPECTRAL-CUTOFF-WIDTH-FINITE-PROBE-SELECTION
claim_id: HC-DU-132
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
maximum_grade: "Scoped Grade 4 Hamiltonian-cutoff tail, noncompact-QFT infinite-rank, and phase-space-width/nonselection boundary plus conditional Grade 3 finite-resolution local-probe certification; no selected QFT, state, region, cutoff, target, probe, observer, archive, empirical excess, new AQFT theorem, new law, new physics, or prediction"
external_action_authorization: "Repository-local proof, bounded primary-source collision, minimal exact regression, evidence/authority integration, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
frozen_read_revisions:
  dynamic_unity_parent: 2757c0f57f2dc39526225baee3d3592619f11aec
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
  current_research_revision: 82
  current_research_sha256: 36ed04a76b028d869b289063ebd6b1d38a781cf5a5a15270e129836ef96ac801
  branch: agent/research-compute-cleanup-2026-07-22
  selection_basis: "Joe authorized the next bounded successor. HC-DU-131 established a physically motivated nuclear approximation envelope but left open whether the Hamiltonian itself selects a finite approximation or merely supplies a tail bound. The strongest cheap selector candidate is its spectral cutoff. This run tests that candidate in noncompact QFT, replaces basis-dependent decompositions with phase-space widths, and then asks whether HC-DU-095 plus established local-QFT measurement schemes yields a conditional finite physical probe packet without hiding the remaining interface choices."
write_boundary:
  - lab/process/runs/RUN-20260729-162943-aqft-spectral-cutoff-width-finite-probe-boundary/run-plan.md
  - explorations/aqft-hamiltonian-spectral-cutoff-phase-space-width-and-finite-probe-boundary-2026-07-29.md
  - tests/du_aqft_spectral_cutoff_width_probe.py
  - tests/artifacts/du_aqft_spectral_cutoff_width_result.json
  - CURRENT-RESEARCH.yaml
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - docs/quantum-foundations-orientation-surface.md
  - explorations/concept-register.md
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
---

# AQFT spectral cutoff, phase-space width, and finite probe boundary

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether independently
selected, observer-indexed certified causal records reconstruct all
observer-accessible time, geometry, fields, and capability, or leave a finite
physical remainder.

The current authority is quiescent at revision 82. `HC-DU-131` established:

```text
AQFT nuclearity
  -> finite-rank approximation exists at every nonzero tolerance
  -/-> finite rank
  -/-> selected finite coordinates
  -/-> formed record.
```

The next load-bearing question is whether the Hamiltonian and localization
data that make this approximation physical also select a finite approximation,
or only control its error.

## Typed arena

Let \(H\geq0\) be a supplied self-adjoint Hamiltonian, let
\(P_E=\mathbf 1_{[0,E]}(H)\), and let

\[
\Theta_{\beta,O}(A)=e^{-\beta H}A\Omega
\]

be the energy-damped local map from the unit ball of a supplied local algebra.
Keep distinct:

1. the physically defined low-energy spectral subspace \(P_E\mathcal H\);
2. a tail bound from discarding \((1-P_E)\mathcal H\);
3. finite rank of \(P_E\);
4. a basis-free approximation dimension of the compact phase-space image;
5. a selected approximating subspace or coordinate system;
6. locally realizable probe schemes for selected observables;
7. a joined, retained, certified record; and
8. target-relative reconstruction.

## Assumptions and warrants

### `STANDARD`

- the spectral theorem for nonnegative self-adjoint operators;
- Reeh--Schlieder cyclicity in its admitted AQFT scope;
- elementary compact-operator and Kolmogorov-width theory;
- free-field continuous spectral multiplicity on noncompact space; and
- established local-probe measurement schemes in the quantized real linear
  scalar field.

### `CONDITIONAL_POSIT`

- a supplied QFT net, representation, state, region, Hamiltonian, and scale;
- nuclearity or compactness of the declared phase-space image;
- a compact physical target class separated by admitted local observables;
- repeatable preparations or a jointly compatible finite campaign; and
- complete acquisition, calibration, archive, access, and error control.

These are inputs, not results.

### Warrants

- `DERIVED`: spectral tail, projected-local-range, width/nonselection, and
  conditional finite-packet statements.
- `CONSTRUCTIVELY_REALIZED`: continuous-spectrum multiplicity, compact-resolvent
  escape, and equal-nuclear-size/different-width exact controls.

## Pre-registered theorem spine

### Proposition 1 — the Hamiltonian cutoff selects a tail bound

For \(P_E=\mathbf 1_{[0,E]}(H)\),

\[
\|(1-P_E)e^{-\beta H}A\Omega\|
\leq e^{-\beta E}\|A\|
\]

for normalized \(\Omega\). The Hamiltonian therefore supplies a natural
basis-free approximation envelope.

### Proposition 2 — noncompact QFT keeps infinitely many low-energy modes

If \(\Omega\) is cyclic for \(\mathcal A(O)\) and
\(P_E\mathcal H\) is infinite-dimensional, then

\[
A\longmapsto P_Ee^{-\beta H}A\Omega
\]

has infinite rank. Reeh--Schlieder makes its range dense in
\(P_E\mathcal H\), and the energy damping is boundedly invertible on that
spectral subspace.

For a free massive field on noncompact space, the one-particle low-energy
subspace already contains an \(L^2\) space over a positive-measure momentum
ball when \(E>m\), so it is infinite-dimensional.

### Proposition 3 — compact resolvent is an exact finite-rank escape

If \(H\) has compact resolvent, every bounded spectral projection \(P_E\) has
finite rank. This closes the mathematical cutoff only by adding a spectral
compactness/confinement property absent from the generic noncompact arena.
It still does not select physical readout coordinates or form a record.

### Proposition 4 — phase-space width is canonical size, not a selector

For compact \(K\subset\mathcal H\), define

\[
d_n(K)=\inf_{\dim V\leq n}\sup_{y\in K}\operatorname{dist}(y,V).
\]

The sequence \(d_n(K)\) and the minimal dimension
\(N_K(\eta)=\min\{n:d_n(K)\leq\eta\}\) are basis-independent approximation
invariants. They do not select an optimizing subspace, basis, detector, or
archive. Equal nuclear norm can coexist with radically different width
profiles.

### Proposition 5 — conditional finite local-probe packet

If a compact physical completion class and continuous target are separated at
resolution \(\delta\) by physically admitted local observables, compactness
selects a finite mathematical subfamily with a positive margin
(`HC-DU-095`). In the real linear scalar field, established asymptotic local
measurement schemes can realize each selected observable to chosen accuracy.
With repeatability or joint compatibility and total error below half the
margin, the retained packet is target sufficient at resolution \(\delta\).

This is a conditional realization theorem. The target, completion class,
observables, probe theories, preparations, couplings, processing regions,
readouts, lineage, archive, access, and tolerance remain supplied.

## Hostile controls

The run must preserve:

- an exact spectral-tail inequality;
- a low-energy rank that grows without bound under noncompact momentum-grid
  refinement;
- a compact-resolvent finite-rank positive escape;
- two compact diagonal images with equal nuclear norm and different
  Kolmogorov-width profiles;
- convergence of both width profiles to zero;
- nonidentification of an approximating subspace from its optimal dimension;
- a conditional local-probe packet rather than an endogenous interface
  selector; and
- no claim that a numerical grid proves the continuum result.

## Literature collision and prior-work boundary

The run must collide with:

- Reeh--Schlieder cyclicity;
- Haag--Swieca and Buchholz--Wichmann phase-space conditions;
- Buchholz--Porrmann quantitative phase-space-size work;
- nuclear maps, approximation numbers, and Kolmogorov widths;
- Fewster--Verch local QFT measurement theory and Fewster--Jubb--Ruep
  asymptotic measurement schemes; and
- DU's `HC-DU-095`, `HC-DU-118`, and `HC-DU-128--131`.

The likely novelty verdict is absorption. The DU increment is the typed
composition of a natural Hamiltonian tail, its generic infinite-rank boundary,
basis-free phase-space size, and conditional finite local-probe realization.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** AQFT phase-space/nuclearity theory, Reeh--Schlieder,
  spectral approximation, and local measurement theory.
- **Cheapest kill:** a theorem making \(P_E\) finite rank in generic noncompact
  QFT, or selecting a finite physically formed local probe/archive interface
  from the AQFT antecedents alone.
- **Positive control:** compact-resolvent Hamiltonians have finite-rank bounded
  spectral projections.
- **Stop:** stop after deciding the natural energy-cutoff candidate,
  defining the basis-free width invariant, and typing the strongest conditional
  finite-probe composition. Do not simulate a field or construct hardware.

## Local-model learning gate

Direct proof and primary literature decide the result. The executable artifact
is a minimal exact regression of discrete spectral tails, refinement-growing
low-energy multiplicity, compact-resolvent escape, and diagonal width profiles.
It is not admitted as evidence for the continuum QFT theorem.

Disposition: `PROOF_FIRST_MINIMAL_REGRESSION_ONLY`.

External hardware is irrelevant.

## Durable return

One dated exploration, exact regression and artifact, appended completion
receipt, and only the live/register surfaces needed to bank the scoped result.
No paper seed, selected successor, ontology promotion, hardware note,
cross-repository claim, or external action.

## Completion receipt

Completed under the frozen contract.

Returned:

```text
HAMILTONIAN_CUTOFF_SELECTS_BASIS_FREE_TAIL_ENVELOPE
+ NONCOMPACT_LOW_ENERGY_LOCAL_MAP_REMAINS_INFINITE_RANK
+ COMPACT_RESOLVENT_IS_AN_EXACT_FINITE_RANK_ESCAPE
+ PHASE_SPACE_WIDTH_QUANTIFIES_SIZE_NOT_COORDINATE_SELECTION
+ EQUAL_NUCLEAR_NORM_ALLOWS_DIFFERENT_WIDTH_PROFILES
+ CONDITIONAL_FINITE_LOCAL_PROBE_CERTIFICATE
+ PHYSICAL_INTERFACE_AND_RECORD_FORMATION_REMAIN_UNSELECTED
+ NO_READY_SUCCESSOR
```

Durable outputs:

- `explorations/aqft-hamiltonian-spectral-cutoff-phase-space-width-and-finite-probe-boundary-2026-07-29.md`
- `tests/du_aqft_spectral_cutoff_width_probe.py`
- `tests/artifacts/du_aqft_spectral_cutoff_width_result.json`
- `CURRENT-RESEARCH.yaml` revision 83
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md` row `NI-DU-176`
- one orientation-surface row, one concept-register entry, and one executable
  test-index entry

Validation:

- focused exact probe: `43/43 PASS`
- agent-orientation/governance probe: `37/37 PASS`
- counter-assumptive register: `289/289` unique
- Python byte compilation: pass
- `git diff --check`: pass

The executable artifact is regression coverage only. No model simulation,
hardware, provider, publication, submission, contact, empirical claim, or
other external action was performed.
