---
title: "QND tomography reopener audit — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 13:00:09 CDT"
run_id: RUN-20260730-175003-qnd-tomography-reopener-audit
work_id: MPA-REOPENER-QND-TOMOGRAPHY-AUDIT
action_id: MPA-REOPENER-QND-TOMOGRAPHY-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-164
---

# QND tomography reopener audit

## Disposition

```text
PROCESS_TOMOGRAPHY_REOPENER_PARTIALLY_SATISFIED
+ OUTCOME_CONDITIONED_INSTRUMENT_RECONSTRUCTION
+ LABEL_SUFFICIENCY_CRITERION
+ MATERIAL_ARCHIVE_NONSELECTION
+ DILATION_TWIN_NO_GO
+ AGGREGATED_COUNTS_ONLY
+ RANK_ONE_NULL_UNADJUDICATED
+ KNOWN_RESULT_ABSORPTION
+ NO_READY_SUCCESSOR
+ SWING 6 NOT ACTIVATED
```

The bounded reopener audit is complete at scoped Grade 4.

## Operational positive

Pereira--García-Ripoll--Ramos QND measurement tomography uses complete
preparations, intermediate operations, and second measurements to reconstruct
the fitted outcome-conditioned reduced instrument
\(\{\mathcal E_n\}\). The seven-qubit IBM realization therefore closes the
postmeasurement-process rung more strongly than the one-repeat response used
by `HC-DU-163`.

For outcome \(n\), the label alone fixes every later system-only response
across admitted input histories exactly when

\[
\mathcal E_n(\rho)
=
\operatorname{tr}(F_n\rho)\tau_n,
\]

equivalently when the source's Liouville/process matrix has ordinary rank
one. This is the exact operational label-sufficiency test.

## Public-packet audit

The audit pinned:

- Zenodo `10.5281/zenodo.7341393`, version `0.1`;
- archive MD5 `0e317d063561231842a9039306e45f94`; and
- Git commit `5c4b8e51767571602de4d2409836f3a37ca25292`.

The 122 Qiskit result JSON files contain 61,336 experiment-result entries.
Every entry is measurement level 2 and contains aggregate counts. None
contains non-null ordered shot memory or raw/IQ-like data. Count keys preserve
the joined categorical first/second outcomes needed for process tomography,
not shot order, rejected attempts, controller lineage, or a complete
archive/reset census.

The seven stored `data_tomo_v2` packets contain 98 fitted \(4\times4\)
single-qubit outcome process matrices. All are numerically rank four at
tolerance \(10^{-10}\); their relative best-rank-one residual has median
\(0.01395\) and range \(0.00253\) to \(0.03432\). This does not adjudicate an
exact rank-one null: constrained finite-sample maximum likelihood can return
full-rank estimates, and the source does not report a replacer-submodel test
with an uncertainty contract.

## Exact material boundary

Two qubit measurement dilations were constructed:

\[
\begin{aligned}
V_{\rm blank}|n\rangle&=|n_Sn_Cn_E0_R\rangle,\\
V_{\rm copy}|n\rangle&=|n_Sn_Cn_En_R\rangle.
\end{aligned}
\]

After tracing \(E,R\), both induce the same accessible ideal projective
instrument for every input operator. The outcome label is operationally
sufficient in both. Yet the hidden \(R\) register is blank versus copied.
Accessing \(R\) distinguishes the implementations.

Thus:

```text
complete accessible instrument
+ operationally sufficient outcome label
does not select
material archive, provenance, or physical dilation
```

This is standard measurement/Stinespring nonuniqueness applied to the
material-record gate. It is not evidence that the IBM apparatus contains
either toy implementation.

## Repository transition

- `HC-DU-164` is banked in the durable exploration.
- `CONCEPT-DU-019` records the QND-tomography reopener correction.
- `NI-DU-207` preserves the instrument-to-material-archive type trap.
- The quantum-foundations orientation surface carries the scoped correction.
- `CURRENT-RESEARCH.yaml` advances from revision 117 to 118.
- The process-tomography reopener term is satisfied only at fitted
  reduced-instrument level.
- The coherent campaign remains parked with `NO_READY_SUCCESSOR`.
- Swing 6 is not eligible and was not activated.
- No hardware, provider, simulation, prediction, paper, or external action
  was activated.

## Validation

- `python3 tests/du_qnd_tomography_material_archive_probe.py
  --write-artifact` — **PASS**; ideal/coin Liouville ranks, complete
  matrix-unit channel equality, hidden-archive difference, and strict
  access extension.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; all 17 seeds and 10 conditional swing cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; 37/37 governance checks, 320 unique counter-assumptive findings,
  74 resolving current references, 38 resolving stable-entrypoint links, no
  active/executable scientific action, and 5,931/6,000 cold-start words.
- Python compilation of all three probes — **PASS**.
- Direct PyYAML revision, parked-program, `HC-DU-164`,
  null-next-action, and no-ready-successor assertions — **PASS**.
- `python3 -m json.tool` on the source audit — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Exact reopener

Do not reopen with more reduced-process tomography alone. Reopen only with a
source-pinned implementation-complete packet containing joined per-attempt
acquisition records and later responses, declared hidden-environment scope,
retention/provenance/access/reset semantics, and separate material
factorization and behavioral-minimality tests. This receipt does not authorize
Swing 6 or any later campaign card.

## Durable files

- `explorations/qnd-tomography-operational-closure-label-sufficiency-and-material-dilation-boundary-2026-07-30.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_qnd_tomography_material_archive_probe.py`
- `tests/artifacts/du_qnd_tomography_material_archive_result.json`
- `tests/README.md`
- `source-audit.json`
- this plan and receipt
