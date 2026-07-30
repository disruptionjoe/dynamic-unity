---
title: "QRF access-attribution and handoff gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
started_at: 2026-07-30T06:48:34-05:00
completed_at: 2026-07-30T06:54:26-05:00
run_id: RUN-20260730-064834-qrf-access-attribution-handoff
work_id: ANOMALY-QRF-REDUCED-CHANNEL-ATTRIBUTION
action_id: QRF-01-ACCESS-ATTRIBUTION-HANDOFF-GATE
claim_id: HC-DU-153
state_revision: 106
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# QRF access-attribution and handoff gate

## Scientific return

```text
PHYSICAL_QUANTUM_REFERENCE_AND_ACCESS_REDUCTION_ARE_EXPLICIT
+ DYNAMIC_COMPATIBILITY_IFF_UNIFORM_FACTORIZED_POPULATION_PRESERVATION
+ BLOCK_PRESERVATION_ALONE_IS_INSUFFICIENT
+ EXACT_NONCOMMUTING_AND_COMMUTING_Z2_CONTROLS_PASS
+ LOCAL_COHERENCE_FACTORS_INTO_ENVIRONMENT_AND_REFERENCE_TERMS
+ ONE_LOCAL_RAMSEY_CURVE_HAS_ATTRIBUTION_NULL_DIRECTION_1_MINUS_1
+ TWO_UNCALIBRATED_REFERENCES_RETAIN_A_COMMON_MODE_GAUGE
+ INDEPENDENT_REFERENCE_CALIBRATION_RESTORES_FULL_RANK
+ SAME_COMPLETE_EXPERIMENT_IS_FRAME_INVARIANT
+ DIFFERENT_LOCAL_PHASE_STANDARDS_ARE_DIFFERENT_PROCEDURES
+ ACCESS_PVMS_ASSIGNMENT_REFERENCE_RECORD_AND_ARCHIVE_REMAIN_SUPPLIED
+ KNOWN_QRF_OPEN_SYSTEM_RAMSEY_AND_IDENTIFIABILITY_THEORY_ABSORB_COMPONENTS
+ NO_NEW_PHYSICS_PREDICTION_HARDWARE_PATH_PAPER_OR_READY_SUCCESSOR
```

Luppi, Kabel, Giacomini, and Smirne's July 2026 source gives Dynamic Unity a
source-native physical handoff map:

\[
\mathcal Q[\rho]
=\operatorname{Tr}_{AE}
\left[\hat S_{A\to B}\rho\hat S_{A\to B}^\dagger\right].
\]

For a block-preserving reduced QRF channel and controlled old-frame
dephasing, the source proves that all output populations remain constant for
every factorized inaccessible preparation iff the pulled-back output effects
commute with their conditional inaccessible evolutions. The exact local
\(\mathbb Z_2\) fixture changes one population from one to zero under a
noncommuting reference flip and preserves it under a commuting phase.

In the Hamiltonian-symmetric regime,

\[
\gamma_{\rm local}(t)
=\gamma_{\rm env}(t)+\gamma_{\rm ref}(t).
\]

The exact design row \([1,1]\) has null direction \((1,-1)\). The twins
\((2,3)\) and \((4,1)\) give the same complete exponential visibility law.
Two uncalibrated references produce a rank-two-by-three design with common-
mode null \((-1,1,1)\). Independently calibrating one reference adds a
nonparallel row and restores full rank.

This is a strong known-physics adapter for observer- and access-relative
handoff. It is not a formed-record, finality, interface-selection, gravity,
or excess-physics result.

## Grade

- **Evidence:** scoped Grade 4 necessity/nonidentifiability.
- **Novelty:** low. The handoff theorem is the source's result; additive
  nuisance attribution and rank repair are standard.
- **DU-owned value:** typed source passport, exact smallest controls, the
  two-reference common-mode guard, and integration with the physical-record
  North Star.
- **Maximum:** no Grade 5 without a physically selected formed-record
  interface and one no-refit discriminator beyond standard quantum theory.

## Portfolio disposition

- `HC-DU-153` is attached to the parked physical-reliability branch as a
  supporting result.
- No active scientific program, executable action, or selected successor is
  created.
- No existing reopen rule is satisfied.
- The prepared publication slot is unchanged.
- No hardware, provider, collaboration, prediction, or paper action is
  authorized.

## Durable files

- `explorations/reduced-qrf-access-handoff-and-decoherence-attribution-boundary-2026-07-30.md`
- `tests/du_qrf_access_attribution_handoff_probe.py`
- `tests/artifacts/du_qrf_access_attribution_handoff_result.json`
- this plan and receipt
- the minimum concept, counter-assumptive, orientation, test-index, and
  current-authority updates

## Validation

- `python3 tests/du_qrf_access_attribution_handoff_probe.py
  --write-artifact` — **PASS**, 12/12 exact checks.
- `python3 tests/du_agent_orientation_contract_probe.py
  --write-artifact` — **PASS**, 37/37 governance checks, 309 unique
  counter-assumptive rows, and 5,892/6,000 cold-start words.
- direct PyYAML revision, quiescence, `HC-DU-153` dependency, and artifact
  assertions — **PASS** at revision 106.
- changed-test Python compilation — **PASS**.
- changed-document local-link check — **PASS**.
- `git diff --check` — **PASS**.
