---
title: "Rigetti fast-feedback returned-shot packet audit — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 14:28:44 CDT"
run_id: RUN-20260730-142222-rigetti-fast-feedback-packet-audit
work_id: RIGETTI-FAST-FEEDBACK-RETURNED-SHOT-PACKET-AUDIT
action_id: RIGETTI-FAST-FEEDBACK-RETURNED-SHOT-PACKET-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-168
---

# Rigetti fast-feedback returned-shot packet audit

## Disposition

```text
SOURCE_PINNED_JOINED_PHYSICAL_PACKET_FOUND
+ RETURNED_SHOT_MULTI_TIME_REOPENER_EARNED
+ CONDITIONAL_ACTION_AND_LATER_RESPONSE_JOINED
+ REPEATED_HARD_HISTORY_DECODER_COMPATIBILITY
+ ALL_ATTEMPT_VISIBILITY_STILL_OPEN
+ IMPLEMENTATION_COMPLETE_REOPENER_NOT_MET
+ NO_GRADE_5_REMAINDER
+ NO_READY_SUCCESSOR
```

The bounded empirical packet audit is complete at scoped Grade 4.

## Physical positive

Riverlane and Rigetti's public Ankaa-2 fast-feedback packet retains 8,000
row-joined hardware repetitions. Each row joins ordered classified and
complex integrated readouts to FPGA decoder registers, timing, a documented
conditional-\(X\) branch, and a later measurement of the conditional qubit.

The packet contains 216,000 hard and 216,000 complex soft measurement
events. It also retains immediate measurement-fidelity,
double-measurement, and \(T_1\)-delay reference packets, explicit
`use_resets=False` metadata, QPU/session identity, and the Stim circuit.

This satisfies the returned-shot joined multi-time term that earlier public
packets had left open.

## Exact controls

With \(X_{\rm pre}\) the final QEC measurement of qubit 50,
\(A=\mathbf1[DASR=1]\) the source-documented conditional branch, and \(Y\)
the extra later measurement, the frozen relation

\[
\widehat Y=X_{\rm pre}\oplus A
\]

matches 746, 718, 703, 626, 617, 631, 583, and 599 of the 1,000 returned
rows at rounds two through nine. These are joined-chain observations, not an
ideal-gate estimate.

Across all circuits, 176 complete hard-history keys repeat, covering 389
rows. No repeated key has conflicting retained `DASR` values. That is a
positive compatibility control for observed decoder factorization, not a
global proof; most higher-round histories are unique and the decoder
implementation is absent.

## Implementation-complete kill

The public schema has no:

- census or identifier for every pre-return controller trigger;
- rejected, retried, or aborted attempt disposition;
- main physical Quil/pulse program or decoder firmware/configuration;
- per-row applied-action or controller-route/memory lineage;
- within-measurement waveform or receiver-buffer lineage;
- physical archive retention, overwrite, access, or reset policy; or
- declared hidden-environment and persistence scope.

The complex soft values are event-level integrated I/Q values, not full
analog waveforms. `use_resets=False` answers whether active qubit resets
were used; it does not establish a blank controller, archive, or
environment between rows.

The packet therefore identifies

\[
P(M,D,T,Y\mid S=1),
\]

the returned-shot kernel, not the unconditional attempted process
\(P(M,D,T,Y,S)\).

## Repository transition

- `HC-DU-168` is banked in the dated exploration.
- `CONCEPT-DU-019` records the returned-shot physical packet and boundary.
- `NI-DU-211` preserves the raw-file/implementation-completeness trap.
- `CURRENT-RESEARCH.yaml` advances from revision 121 to 122.
- The joined returned-shot term is now satisfied.
- The exact reopener is narrowed to an all-attempt/controller/archive
  sidecar plus factorization and minimality.
- The flagship remains parked with `NO_READY_SUCCESSOR`.
- No hardware, provider submission, prediction, paper, new law, ontology
  verdict, or later campaign card was activated.

## Validation

- `du_rigetti_fast_feedback_packet_audit.py` against the frozen source —
  **PASS**; 103/103 source, schema, join, response, repeated-history,
  calibration, and boundary checks.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; 17 seeds and 10 conditional swing cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; 37/37 governance checks, 324 unique counter-assumptive findings,
  82 resolving current references, 38 resolving stable-entrypoint links, no
  active/executable scientific action, and 5,950/6,000 cold-start words.
- Python compilation of the three probes — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Exact reopener

Reopen material reconstruction only when one source-pinned sidecar adds the
missing attempt census, dispositions, program/firmware, applied-action and
route state, waveform lineage, archive/access/reset semantics, and
environment scope. It must then support material-archive factorization and
behavioral-minimality tests without refitting.

Returned-shot prediction or first-leak work may be useful as explicitly
conditional analysis. It cannot adjudicate the all-attempt physical
remainder.

## Durable files

- `explorations/rigetti-real-time-qec-returned-shot-record-action-response-packet-and-implementation-boundary-2026-07-30.md`
- `explorations/concept-register.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_rigetti_fast_feedback_packet_audit.py`
- `tests/artifacts/du_rigetti_fast_feedback_packet_result.json`
- `tests/README.md`
- this plan and receipt
