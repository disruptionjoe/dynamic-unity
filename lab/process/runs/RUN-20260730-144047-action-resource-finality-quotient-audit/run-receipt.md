---
title: "Action/resource finality quotient audit — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 15:14:22 CDT"
run_id: RUN-20260730-144047-action-resource-finality-quotient-audit
work_id: ACTION-RESOURCE-FINALITY-QUOTIENT-AUDIT
action_id: ACTION-RESOURCE-FINALITY-QUOTIENT-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-169
---

# Action/resource finality quotient audit

## Disposition

```text
ACTION_QUOTIENT_RESOURCE_DISTINCTION
+ NO_DETECTED_ACTION_QUOTIENT_RESPONSE_DISTINCTION
+ HELDOUT_SCHEMA_CANNOT_TEST_ACTION_QUOTIENT
+ KNOWN_CONTROL_THEORY_ABSORPTION
+ IMPLEMENTATION_COMPLETE_REOPENER_UNCHANGED
+ NO_READY_SUCCESSOR
```

The bounded empirical quotient audit is complete at scoped Grade 4.

## Exact positive

The Riverlane/Rigetti source maps decoder states `DASR=0` and `DASR=2` to
the same no-\(X\) control action. In the joined returned-shot packet, those
two action-equivalent certificates have different retained completion-time
distributions in every circuit from rounds 3 through 9.

- The status-2 median exceeds the status-0 median in all seven rounds.
- The median gaps range from 240 to 356 retained counter units.
- The empirical probability that a status-2 time exceeds a status-0 time,
  with half weight for ties, ranges from 0.728 to 0.911.
- The empirical Kolmogorov--Smirnov distance ranges from 0.362 to 0.689.

The retained timing kernel therefore does not factor through the
source-defined action quotient in this packet.

This is a sample-level architectural distinction. It does not identify a
causal decoder-status effect or population law.

## Downstream-response control

With the no-refit failure indicator

\[
E=\mathbf1[Y\ne X_{\rm pre}\oplus\mathbf1[DASR=1]],
\]

status 0 has 487 failures in 1,310 rows and status 2 has 1,700 failures in
4,810 rows. A Cochran--Mantel--Haenszel score stratified by round and
pre-feedback qubit state gives

```text
z = 1.508872
two-sided normal p = 0.131331
```

The frozen five-percent test detects no corresponding split in this binary
response coordinate. This is not evidence that the response laws are equal.

## Held-out boundary

The independently published timing CSV passes both frozen file hashes and
contains 300,000 rows: 100,000 each at rounds 9, 17, and 25. Its complete
schema is

```text
rounds,cycles,time_per_round
```

It contains neither decoder status nor a stable row identifier joining its
timings to a decoder-result archive. It therefore cannot replicate or refute
the status-conditioned timing distinction.

This is an exact schema kill, not a failed replication or null result. The
minimum completing sidecar is decoder status beside each timing row, or a
stable join key.

## Theorem and absorption

For certificate \(D\), action map \(a(D)\), and coordinate kernel
\(K_Z(\cdot\mid D)\), the action quotient is sufficient for \(Z\) exactly
when

\[
a(d)=a(d')
\Longrightarrow
K_Z(\cdot\mid d)=K_Z(\cdot\mid d').
\]

The mathematics is absorbed by sufficient statistics, Markov lumpability,
controller minimization, and ordinary feedback-control/QEC latency
analysis. Dynamic Unity earns the typed physical specimen:

```text
certificate finality
!= action finality
!= resource/timing finality
!= response finality
!= provenance finality
```

No novel general theorem or new physical effect is claimed.

## Repository transition

- `HC-DU-169` is banked in the dated exploration.
- `CONCEPT-DU-019` carries the coordinate-specific factorization rule.
- `NI-DU-212` preserves the one-finality-quotient trap.
- `CURRENT-RESEARCH.yaml` advances from revision 122 to 123.
- The flagship remains parked with `NO_READY_SUCCESSOR`.
- The implementation-complete all-attempt/controller/archive reopener from
  `HC-DU-168` remains unchanged.
- No large raw-file download, hardware, provider action, paper, prediction,
  ontology verdict, or later campaign was activated.

## Validation

- `du_action_resource_finality_quotient_audit.py` against both frozen
  sources — **PASS**; 47/47 source, quotient, timing, response, and held-out
  schema checks.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; all campaign seeds and conditional cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; governance, authority, current-reference, stable-entrypoint,
  quiescence, and cold-start checks.
- Python compilation of all three probes — **PASS**.
- Direct PyYAML revision-123, parked-program, `HC-DU-169`,
  null-next-action, and no-ready-successor assertions — **PASS**.
- JSON validation of the compact result artifact — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Exact reopener

For held-out action/resource testing, require decoder status beside each
timing row or a stable timing-to-decoder join. For flagship reconstruction,
retain the stronger `HC-DU-168` reopener: an all-attempt census,
dispositions, physical program/firmware and route state, waveform lineage,
archive/access/reset semantics, and declared environment scope, followed by
material factorization and behavioral-minimality tests without refitting.

## Durable files

- `explorations/action-equivalent-decoder-certificates-resource-timing-split-and-heldout-status-join-boundary-2026-07-30.md`
- `explorations/concept-register.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_action_resource_finality_quotient_audit.py`
- `tests/artifacts/du_action_resource_finality_quotient_result.json`
- `tests/README.md`
- this plan and receipt
