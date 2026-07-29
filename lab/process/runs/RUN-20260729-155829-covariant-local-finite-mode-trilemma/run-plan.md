---
run_id: RUN-20260729-155829-covariant-local-finite-mode-trilemma
status: completed
started_at: 2026-07-29T15:58:29-05:00
completed_at: 2026-07-29T16:09:06-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-COVARIANT-LOCAL-FINITE-MODE-TRILEMMA
claim_id: HC-DU-130
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
maximum_grade: "Scoped Grade 4 local--finite--translation-covariance necessity and continuum-Gaussian first-leak boundary plus conditional Grade 3 target-relative reconstruction; no selected QFT, state, mode family, observer, record interface, empirical excess, new law, new physics, or prediction"
external_action_authorization: "Repository-local proof, bounded primary-source collision, minimal exact regression, evidence/authority integration, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
frozen_read_revisions:
  dynamic_unity_parent: b2b825c547a43f590985a45eac6d5c3d8c79bb65
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
  current_research_revision: 80
  current_research_sha256: 90195011ee0999e0de90a8da730a715c22af4363093fab486409ad578df7c866
  branch: agent/research-compute-cleanup-2026-07-22
  selection_basis: "Joe authorized the next bounded successor. DU is explicitly quiescent. HC-DU-129 proves finite Gaussian population reconstruction only after a finite mode algebra is supplied. HC-DU-061 already audits autonomous state/manifold selection, so repeating Gaussian Lindbladian stabilization would circle a classified boundary. This run instead tests whether one nonzero finite packet of local continuum smearings can itself remain invariant under the physical translation symmetry, and what observer-indexed repair survives."
write_boundary:
  - lab/process/runs/RUN-20260729-155829-covariant-local-finite-mode-trilemma/run-plan.md
  - explorations/covariant-local-finite-mode-trilemma-indexed-family-repair-and-continuum-gaussian-first-leak-2026-07-29.md
  - tests/du_covariant_local_finite_mode_trilemma_probe.py
  - tests/artifacts/du_covariant_local_finite_mode_trilemma_result.json
  - CURRENT-RESEARCH.yaml
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - docs/quantum-foundations-orientation-surface.md
  - explorations/concept-register.md
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
---

# Covariant local finite-mode trilemma

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether independently
selected, observer-indexed certified causal records reconstruct all
observer-accessible time, geometry, fields, and capability, or leave a finite
physical remainder.

The current authority is quiescent at revision 80. `HC-DU-129` established:

```text
fixed finite-mode Gaussian class
  + exact quadrature populations
  -> finite minimal state packet

but

finite shots
  -> confidence-qualified certificate, not exact state truth.
```

Its first exact reopener asks for a dynamically selected finite mode/subalgebra
or a finite-sufficient continuum theorem. This run tests the kinematic
selection boundary before proposing more dynamics.

## Typed arena

Let

\[
\mathcal D=C_c^\infty(\mathbb R^d;\mathbb R)
\]

be a supplied real local test-function space, with translations

\[
(\tau_a f)(x)=f(x-a).
\]

A fixed mode packet is a linear subspace \(S\subset\mathcal D\). Declare:

- **finite:** \(0<\dim S<\infty\);
- **local:** every element has compact spacetime support;
- **globally translation-invariant:** \(\tau_aS=S\) for every
  \(a\in\mathbb R^d\);
- **indexed covariance:** a family \(S_x=\tau_xS_0\), so translating the
  physical location translates the packet rather than leaving one packet
  fixed.

For the Gaussian boundary, let \(\mathcal W(H,\sigma)\) be a supplied CCR Weyl
algebra on a larger symplectic space \(H\), and let \(S\subset H\) be the
finite accessible symplectic sector. The record reconstructs only the
restriction of a quasifree state to \(\mathcal W(S)\) unless a theorem forces
the complement.

Keep these claims distinct:

1. one fixed finite local packet is invariant;
2. a covariant family of finite local packets exists;
3. the union of that family is finite;
4. a finite nonlocal spectral sector is invariant;
5. a finite packet reconstructs its restricted state;
6. that packet reconstructs the continuum state or every held-out target.

## Assumptions and warrants

### `STANDARD`

- ordinary translation action on compactly supported smooth functions;
- finite-dimensional linear algebra;
- CCR/Weyl direct sums and Gaussian characteristic functions; and
- exact population-level Gaussian reconstruction from `HC-DU-129`.

### `CONDITIONAL_POSIT`

- the continuum test-function/localization space;
- translation symmetry as the relevant covariance group;
- the supplied finite accessible sector \(S\);
- the quasifree/Gaussian completion class;
- the source/readout and observer-region index; and
- any target asserted to factor through the restriction to \(S\).

These are frozen inputs, not results.

### Warrants

- `DERIVED`: the local--finite--invariant no-go and indexed-family
  consequence.
- `CONSTRUCTIVELY_REALIZED`: disjoint-translate witnesses, the indexed-family
  positive control, nonlocal character control, and same-restriction/
  different-complement Gaussian witness.

## Pre-registered theorem spine

### Proposition 1 — no fixed finite local translation-invariant packet

There is no nonzero finite-dimensional subspace

\[
S\subset C_c^\infty(\mathbb R^d)
\]

that is invariant under every translation.

For nonzero \(f\in S\), choose a vector \(v\) longer than the diameter of
\(\operatorname{supp}f\). The supports of

\[
f,\tau_vf,\tau_{2v}f,\ldots
\]

are pairwise disjoint. These translates lie in \(S\) by invariance and are
linearly independent, contradicting finite dimensionality.

### Corollary 1 — local/finite/covariant trilemma

A nontrivial continuum packet must surrender at least one of:

1. one fixed finite packet;
2. proper localization; or
3. invariance of that same packet under the full translation group.

This does not forbid covariance. It changes its type:

\[
S_x=\tau_xS_0
\]

is a covariant family of finite local packets, but the span of its full orbit
is infinite. The location/observer-region index is physical interface data,
not a subjective belief and not a selected global foliation.

### Proposition 2 — nonlocal and compact-arena controls

Finite spans of translation characters are invariant because translations
act by phases. On noncompact spacetime those characters are global,
non-compactly-supported generalized modes. On a finite periodic arena the
same construction is finite and exact because compactification/discretization
has been supplied.

These controls prevent the theorem from being overstated as “no finite
covariant mode sector.”

### Proposition 3 — continuum Gaussian first leak

Suppose the larger CCR system contains one symplectically independent mode
outside the finite accessible sector \(S\). Choose two product quasifree
states that agree on \(S\), put the vacuum on the extra mode in one state,
and a centered thermal covariance on it in the other. They agree on every
Weyl observable in \(\mathcal W(S)\) and differ on a held-out Weyl observable
of the extra mode.

Thus:

```text
finite Gaussian packet
  -> exact restricted-state reconstruction

finite Gaussian packet
  -/-> exact continuum-state reconstruction.
```

The first leak is complement access, not a higher moment.

### Proposition 4 — target-relative finite sufficiency

A held-out target is exactly reconstructible from the finite packet only
when it factors through the state restriction to the supplied sector. A
target acting on an independently admitted complementary mode fails that
criterion by Proposition 3.

This is conditional reconstruction, not selection of \(S\), the state, or
the instrument.

## Hostile controls

The run must explicitly preserve:

- a covariant *family* of finite local packets as a positive repair;
- a finite translation-invariant nonlocal character sector;
- a finite periodic/lattice arena where a supplied cutoff changes the result;
- arbitrary packet dimension with one hidden Gaussian mode;
- a held-out target inside \(S\), which reconstructs exactly; and
- a held-out target outside \(S\), which leaks.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** standard translation-invariant-subspace/harmonic
  analysis, locally covariant QFT, and Gaussian restriction mathematics.
- **Cheapest kill:** one nonzero finite-dimensional translation-invariant
  subspace of compactly supported smooth functions on \(\mathbb R^d\).
- **Scope kill:** a covariant indexed family exists, so the theorem cannot be
  promoted into a no-go on finite local measurements or observer-indexed
  records.
- **Stop:** stop after proving the fixed-packet theorem, preserving both
  escape controls, and typing the complement-state witness. Do not construct
  a field simulator, detector, lattice theory, or hardware bridge.

## Local-model learning gate

Direct proof supplies the result. The executable artifact is a minimal
deterministic regression of disjoint-support independence, indexed-family
covariance, character covariance, and finite-sector Gaussian first leaks.
It is not an admitted simulation or learning model.

Disposition: `PROOF_FIRST_MINIMAL_REGRESSION_ONLY`.

External hardware is irrelevant.

## Durable return

One dated exploration, exact regression and artifact, appended completion
receipt, and only the live/register surfaces needed to bank the scoped
result. No paper seed, selected successor, ontology promotion, hardware note,
cross-repository claim, or external action.

## Completion receipt

Disposition:

```text
NO_NONZERO_FIXED_FINITE_TRANSLATION_INVARIANT_LOCAL_PACKET
+ INDEXED_FINITE_LOCAL_PACKET_FAMILY_IS_COVARIANT
+ FULL_LOCAL_TRANSLATION_ORBIT_HAS_UNBOUNDED_DIMENSION
+ NONLOCAL_CHARACTER_AND_FINITE_PERIODIC_ESCAPES_PRESERVED
+ FINITE_GAUSSIAN_PACKET_RECONSTRUCTS_ONLY_ITS_RESTRICTION
+ COMPLEMENT_MODE_IS_THE_CONTINUUM_FIRST_LEAK
+ NO_READY_SUCCESSOR
```

Banked outputs:

- `HC-DU-130` proves the scoped fixed-packet no-go by disjoint translates;
- the region-indexed family is the exact positive covariance repair;
- nonlocal character sectors and supplied finite periodic arenas preserve the
  mandatory escapes;
- the Gaussian complement witness separates restricted-state reconstruction
  from continuum-state reconstruction; and
- current authority advances to revision 81 while remaining quiescent.

Validation:

- `du_covariant_local_finite_mode_trilemma_probe.py`: `36/36`;
- `du_gaussian_finite_record_ladder_probe.py`: `33/33`;
- `du_positive_functional_qft_reconstruction_probe.py`: `27/27`;
- `du_operational_localization_causal_saturation_probe.py`: pass;
- `du_bounded_weyl_causal_propagator_probe.py`: `64` factorizations and `16`
  symplectic relabelings;
- agent-orientation contract: `37/37`, `5983/6000` cold-start words;
- Python compilation, YAML/frontmatter/JSON parsing, and
  `git diff --check`: pass.

No physical mode family, state, QFT, observer, record interface, empirical
excess, law, prediction, paper, hardware action, provider action, or
publication was selected or authorized.
