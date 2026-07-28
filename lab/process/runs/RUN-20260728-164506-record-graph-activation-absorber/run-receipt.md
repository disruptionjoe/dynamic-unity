---
title: "Record-graph activation absorber — receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-28
run_id: RUN-20260728-164506-record-graph-activation-absorber
work_id: RGAA-RECORD-GRAPH-ACTIVATION-ABSORBER
program_id: CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Run receipt

## Result

```text
WEIGHTED_RECORD_GRAPH_SELECTS_SETTLEMENT
DELAYED_ACTIVATION_REPRODUCES_NUCLEATED_GRAPH
EDGE_PROVENANCE_SURVIVES
TYPE_PREEXISTENCE_NOT_IDENTIFIED
SOURCE_ISSUANCE_NOT_ESTABLISHED
NO_DU_REOPENER
```

`HC-DU-087` proves that every settlement observable defined from a
time-indexed weighted record graph is invariant under a label-, edge-, and
weight-preserving graph isomorphism. A fixed initial type reservoir with the
rule “consume the current head when activated” constructs exactly the same
graph process as the TaF nucleated arm.

The new TaF result therefore locates a genuine provenance-sensitive settlement
effect but does not distinguish type creation from delayed activation. Its
defect channel was already absorbed by stochastic variant adoption; its
settlement channel is absorbed by the missing predeclared-chain arm.

## Disposition

```text
cross-repo input: verified and narrowed
scoped factorization/nonidentifiability result: banked
new physical law: none
source issuance: none
scientific successor: none
new simulation: skipped
external hardware: irrelevant
```

## Durable output

- `explorations/record-graph-settlement-and-delayed-activation-nonidentifiability-2026-07-28.md`
- this run plan
- this receipt

## Validation

- `python3 tests/du_agent_orientation_contract_probe.py` — **PASS**, 35/35
  checks, 240 unique counter-assumptive rows, and 5,992/6,000 cold-start
  words.
- `git diff --check` — **PASS**.
