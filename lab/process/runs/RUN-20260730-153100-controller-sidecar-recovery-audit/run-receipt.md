---
title: "Rigetti controller-sidecar recovery and command/actuation boundary — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 15:37:21 CDT"
run_id: RUN-20260730-153100-controller-sidecar-recovery-audit
work_id: RIGETTI-CONTROLLER-SIDECAR-RECOVERY-AUDIT
action_id: RIGETTI-CONTROLLER-SIDECAR-RECOVERY-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-170
---

# Rigetti controller-sidecar recovery and command/actuation boundary

## Disposition

```text
DESCRIPTIVE_CONTROLLER_SIDECAR_RECOVERED
+ PRIOR_MISSING_PROGRAM_CLAIM_NARROWED
+ EXECUTABLE_AND_CONFIGURATION_SIDECAR_ABSENT
+ AGGREGATE_ACTUATION_EVIDENCE_ONLY
+ PER_ATTEMPT_ACTUATION_NONIDENTIFICATION
+ FAULT_RELATIVE_COMPLETENESS_RULE
+ REOPENER_NARROWED_NOT_SATISFIED
+ NO_READY_SUCCESSOR
```

The bounded source and implementation-fibre audit is complete at scoped
Grade 4.

## Positive recovery

The primary paper's supplementary source specifies:

- a proprietary-assembly workflow interleaved with the QEC circuit;
- decoder-feature/configuration initialization categories;
- sequencer-memory buffering and instruction reordering;
- 32-bit packet formation and WISHBONE writes;
- start, status polling, Boolean result, conditional \(X\), and matched idle;
- the hub-and-single-hop star route;
- sequencer/decoder clocks and clock-crossing logic; and
- an aggregate qubit-\(T_1\) end-to-end actuation-timing check.

`HC-DU-168`'s broad wording that the physical program and controller route
were absent is therefore narrowed: descriptive workflow and route
architecture are public.

## Remaining public boundary

The frozen arXiv bundle contains TeX, bibliographies, and figures only. It
contains no:

- exact pyQuil, assembly listing, waveform program, program binary, firmware
  image, or complete configuration values/digests;
- per-attempt issued-command, message-route, controller-state, or physical
  actuation acknowledgement;
- trigger identifier and complete reject/retry/abort disposition census;
- pre-integration waveform/buffer lineage;
- archive write/retention/overwrite/access/reset contract; or
- declared controller/environment/persistence scope.

The joined response and \(T_1\) check provide aggregate physical evidence,
not per-attempt actuation identity.

## Exact nonidentification control

The finite control keeps the returned tuple

```text
reported M1 = 0
logical result = 1
issued command = X
reported Y = 1
```

fixed while comparing:

```text
post-M1 state 0 + X delivered
post-M1 state 1 + X lost.
```

The source's nontrivial \(P(S\mid M)\) calibration admits the hidden
postmeasurement-state distinction. The twin proves only that
command-plus-response does not identify per-attempt physical actuation under
that fault class. It does not allege that a pulse was lost.

## Corrected completeness rule

For implementation class \(\mathcal I\), retained passport \(p\), and target
law \(T\), the packet is complete exactly when

\[
p(i)=p(i')\Longrightarrow T(i)=T(i')
\qquad(i,i'\in\mathcal I).
\]

Implementation completeness is therefore target-, fault-, and
environment-relative. It is not maximal telemetry. A waveform is required
only when an admitted target or fault varies inside the coarser packet
fibre.

## Repository transition

- `HC-DU-170` is banked in the dated exploration.
- `CONCEPT-DU-019` carries the fault-relative implementation criterion.
- `NI-DU-213` preserves the maximal-telemetry and command/actuation traps.
- `CURRENT-RESEARCH.yaml` advances from revision 123 to 124.
- The reopener now asks for a target/fault/environment-complete passport:
  all-attempt dispositions, exact executable/configuration identity,
  target-sufficient actuation/route evidence, archive
  lineage/access/reset, factorization, and minimality.
- Waveform lineage is conditional rather than categorically required.
- The flagship remains parked with `NO_READY_SUCCESSOR`.
- No hardware, provider, laboratory contact, large raw-file download, paper,
  prediction, ontology verdict, or later campaign was activated.

## Validation

- `du_controller_sidecar_recovery_audit.py` against the frozen arXiv source —
  **PASS**; 17/17 hash, inventory, workflow-marker, missing-executable, and
  command/actuation checks.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; all 17 seeds and 10 conditional cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; 37/37 governance checks, 326 unique counter-assumptive findings,
  86 resolving current references, no active/executable scientific action,
  and a cold-start surface below 6,000 words.
- Python compilation of all three probes — **PASS**.
- Direct PyYAML revision-124, parked-program, `HC-DU-170`,
  null-next-action, and no-ready-successor assertions — **PASS**.
- JSON validation of the compact result artifact — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Exact reopener

Freeze the held-out target, admitted implementation-fault class, and
environment/persistence scope. Reopen only when a source-pinned packet makes
that target constant on the remaining implementation fibre and supports
material factorization plus behavioral minimality without refitting.

For this QEC specimen, the next minimum passport is:

1. all trigger IDs and dispositions;
2. exact executable/configuration identity;
3. target-sufficient per-attempt command/route/actuation evidence;
4. archive lineage, access, retention, overwrite, and reset semantics; and
5. the declared environment scope.

## Durable files

- `explorations/controller-sidecar-recovery-command-actuation-nonidentification-and-fault-relative-completeness-2026-07-30.md`
- `explorations/concept-register.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_controller_sidecar_recovery_audit.py`
- `tests/artifacts/du_controller_sidecar_recovery_result.json`
- `tests/README.md`
- this plan and receipt
