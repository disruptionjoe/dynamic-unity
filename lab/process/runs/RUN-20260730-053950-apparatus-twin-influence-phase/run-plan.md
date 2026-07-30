---
run_id: RUN-20260730-053950-apparatus-twin-influence-phase
status: complete
started_at: 2026-07-30T05:39:50-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-PHYSICAL-RECORD-INTERFACE-SELECTION
action_id: PRIS-15-APPARATUS-TWIN-INFLUENCE-PHASE
claim_id: HC-DU-151
completed_at: 2026-07-30T05:46:12-05:00
evidence_grade: 4
maximum_grade: "Scoped Grade 4 quadratic influence-phase criterion, exact conserved apparatus-twin counterexample and positive control, and primary-source apparatus boundary; Grade 5 only after a physical controller class and complete relational probability retain frozen no-refit excess."
frozen_read_revisions:
  dynamic_unity_parent: 2596d3db8fad
lane_selection:
  owner: dynamic-unity
  primary_lane_id: "3"
  supporting_lane_ids:
    - "1"
    - "2"
    - "4"
    - "6"
    - "7"
  channel_ids:
    - CH-COLLIDE
    - CH-FORMAL
    - CH-MODEL
write_boundary:
  - explorations/quantum-gravity-apparatus-twin-influence-phase-and-orthogonality-boundary-2026-07-30.md
  - lab/process/runs/RUN-20260730-053950-apparatus-twin-influence-phase/run-plan.md
  - explorations/concept-register.md
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - tests/du_apparatus_twin_influence_phase_probe.py
  - tests/artifacts/du_apparatus_twin_influence_phase_result.json
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
  - tests/artifacts/du_agent_orientation_contract_result.json
  - CURRENT-RESEARCH.yaml
external_action_authorization: "Repository-local primary-source audit, exact finite theorem/counterexample derivation, authority integration, explicit-path commit, and non-force push only. No hardware, provider, contact, mailbox mutation, publication, submission, or other external action."
---

# PRIS-15 — apparatus-twin influence-phase gate

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether
independently selected, observer-indexed certified causal records reconstruct
all observer-accessible time, geometry, fields, and capability, or leave a
finite physical remainder.

The repository is quiescent at revision 102. `HC-DU-150` proves that a driven
probe is an open stress subsystem and that gauge completion forces a
controller/support into the conserved source, but conservation selects only
an affine class of completions. It leaves open whether integrating out the
linear field makes the observable relative phase independent of that class.

## Exact question

1. For a symmetric Gaussian response kernel \(G\), how does the on-shell or
   influence phase \(I(T)=\frac12\langle T,GT\rangle\) change when a
   divergence-free controller completion \(K\) is added?
2. If the same \(K\) is added to both branches, does its self-phase cancel?
3. Can its controller--branch cross phase remain and change the relative
   phase while both total sources stay conserved and the reduced probe
   histories stay fixed?
4. What exact necessary-and-sufficient condition makes the relative phase
   constant on the admitted apparatus-completion fibre?
5. Do existing linearized-gravity interferometer models prove that condition,
   assume a sufficient heavy/homogeneous limit, or leave it open?

## Preregistered returns

### Completion-independent phase theorem

Every admitted divergence-free apparatus variation is response-orthogonal to
the branch-difference source. The relative phase factors through the reduced
source/probe history. Bank the theorem and narrow the physical packet needed
to verify its hypotheses.

### Exact conditional independence plus counterexample

The phase is completion-independent exactly on the response-orthogonal
subspace. A conserved nonorthogonal completion shifts it, while the common
controller self-phase cancels. Bank the criterion and stop treating
conservation as sufficient.

### Published-apparatus absorption

A primary source already proves the exact completion-independence theorem for
the relevant physical controller class. Record the absorber and close the
apparatus-twin reopener.

### Full phase cancellation

Every closed completion cancels the proposed branch phase. Close the phase
reopener without inferring an observed effect.

## Controls

1. Gaussian integration and quadratic source phases are standard influence-
   functional mathematics; they are not DU novelty.
2. Common apparatus self-action cancels from a relative phase, but
   source--apparatus cross action need not.
3. Stress conservation and gauge invariance constrain admissibility; they do
   not by themselves impose response orthogonality.
4. A heavy apparatus with a homogeneous field is a physical sufficient
   approximation if independently established, not a consequence of
   conservation.
5. The finite lattice may prove the algebraic boundary but is not a
   laboratory controller, graviton propagator, or prediction.
6. Identical reduced probe histories do not mean identical complete sources.
7. No toy completion may be copied into the Chen--Giacomini or gravitational-
   entanglement phase as a numerical correction.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** Gaussian field integration, Feynman--Vernon
  influence functionals, Ward identities, the apparatus appendix of
  Christodoulou et al., and `HC-DU-149--150`.
- **Cheapest kill:** one exact periodic finite kernel with two branchwise
  conserved total sources and a common divergence-free controller addition
  for which the relative phase shift equals a nonzero response pairing.
- **Positive control:** make the two branch totals equal and require the same
  controller addition to generate no relative phase.
- **Stop:** after proving the criterion, running the exact control, and
  locating the literature boundary. Do not model a physical trap, estimate
  an experimental correction, design hardware, or claim a published phase
  wrong.

## Local-model learning gate

One exact rational periodic-lattice response is admissible because it proves
or refutes the universal implication from conservation to phase
independence. It must use a symmetric nonlocal kernel commuting with the
discrete divergence and preserve source/controller/probe types. No external
hardware is required or warranted.

## Planned validation

```bash
python3 tests/du_apparatus_twin_influence_phase_probe.py --write-artifact
python3 tests/du_agent_orientation_contract_probe.py --write-artifact
python3 -m py_compile tests/du_apparatus_twin_influence_phase_probe.py
git diff --check
```

## Durable output

One dated primary-source apparatus audit, one exact quadratic influence-phase
criterion and counterexample, this governed receipt, and only the authority,
concept, counter-assumptive, and test-index changes needed to preserve it. No
paper, prediction, hardware path, phase verdict, or successor promotion unless
independently earned.

## Return

```text
A_CLOSED_LINEAR_GAUSSIAN_FIELD_PHASE_IS_QUADRATIC_IN_THE_TOTAL_BRANCH_SOURCE
+ A_COMMON_CONTROLLER_SELF_PHASE_CANCELS_FROM_THE_RELATIVE_PHASE
+ THE_SOURCE_CONTROLLER_CROSS_PHASE_NEED_NOT_CANCEL
+ CONSERVATION_AND_GAUGE_ADMISSIBILITY_DO_NOT_IMPLY_APPARATUS_INDEPENDENCE
+ A_COMMON_DIVERGENCE_FREE_COMPLETION_SHIFTS_THE_RELATIVE_PHASE_BY_ONE_RESPONSE_PAIRING
+ APPARATUS_INDEPENDENCE_IS_EQUIVALENT_TO_RESPONSE_ORTHOGONALITY_ON_THE_ADMITTED_COMPLETION_SPACE
+ AN_EXACT_NONZERO_ORTHOGONAL_COMPLETION_PRESERVES_THE_PHASE
+ CHRISTODOULOU_ET_AL_IDENTIFY_THE_MISSING_APPARATUS_AND_USE_HEAVY_HOMOGENEOUS_SUFFICIENT_APPROXIMATIONS
+ OPERATIONAL_GIE_MODELS_RETAIN_EXTERNAL_FORCE_OR_TRAP_INTERFACES
+ THE_MATHEMATICS_IS_ABSORBED_BY_GAUSSIAN_INFLUENCE_FUNCTIONALS
+ THE_PHYSICAL_REOPENER_IS_SELECTION_PLUS_ORTHOGONALITY_OR_A_NO_REFIT_VIOLATION
+ NO_PUBLISHED_PHASE_VERDICT_DU_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

`HC-DU-151` proves the exact quadratic factorization criterion. For a
symmetric response \(G\), adding one common controller completion \(K\) to
both branch totals changes the relative phase by
\(\langle T_1-T_0,GK\rangle\). The controller self-phase cancels, but its
cross phase need not. Conservation therefore does not imply apparatus
independence.

The exact rational fixture keeps the reduced probes fixed and every total
source conserved. A common completion shifts the phase by
\(4361746/23925\), exactly the response cross pairing. A constructed nonzero
orthogonal completion leaves the phase unchanged. All 14 assertions pass.

Christodoulou et al. explicitly identify the missing apparatus stress for
arbitrary driven trajectories and invoke sufficient heaviness and field
homogeneity to suppress branch-relative apparatus terms. This is the nearest
physical absorber, not a universal consequence of conservation. The
remaining reopener is a physically selected controller class with uniform
orthogonality or one complete no-refit violation. The repository remains
quiescent.

## Validation result

The exact probe passed all 14 assertions. The agent-orientation contract
passed all 37 checks with 308 unique counter rows and a 5,950-word cold-start
surface. Both Python modules compiled, and `git diff --check` passed.
