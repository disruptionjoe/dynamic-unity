---
title: "Run: N5-SCF-P2 synergy-preserving gossip/DAG provenance and knowledge"
status: completed
date: 2026-07-27
work_id: N5-SCF-P2
claim_id: HC-DU-048
authority: "Joe direct chat: Go"
result: "../explorations/synergy-preserving-gossip-dag-provenance-and-knowledge-2026-07-27.md"
probe: "../tests/du_synergy_gossip_dag_provenance_probe.py"
artifact: "../tests/artifacts/du_synergy_gossip_dag_provenance_result.json"
next_work: N5-SCF-P3
deferred_work: N5-RS-P2
paper_state_change: none
hardware_state_change: none
provider_state_change: none
---

# Run: N5-SCF-P2 synergy-preserving gossip/DAG provenance and knowledge

## Decision

Follow `HC-DU-047`'s smallest synergistic source through plain gossip, ideal
signed events, hash-DAG ancestry, epistemic pooling, and an event-bound
zero-knowledge statement. Determine what each layer preserves or adds, and
whether any layer can distinguish a physically target-bound source from a
matched null source without a new attestation channel.

Use exact finite factorization, graph, and epistemic certificates. Do not
build a network simulator, cryptographic implementation, or physical model.

## Execution receipt

The swing proved or exhibited:

1. a synergy source and a target-independent null source with identical
   complete payload-pair laws;
2. identical fixed signed-DAG artifact laws despite different physical
   target-binding relations;
3. exact XOR reconstruction after lossless pooling, versus \(1/2\) Bayes
   error under partition, duplicated-origin eclipse, or churn without
   retention;
4. endpoint/order blindness to route and declared-route recovery from
   retained parent links;
5. raw path-length failure and source-to-terminal reachability invariance
   under benign relay subdivision;
6. signed declared-origin rank without physical independence;
7. local fork invisibility and merged signed equivocation evidence;
8. group distributed knowledge before individual target knowledge;
9. the finite asynchronous last-message obstruction to common knowledge;
10. total-order and source-truth separation;
11. unbound versus event-bound proof statements and the residual
    physical-attestation boundary; and
12. direct-message versus shared-trace formation, compression, evaporation,
    and forgery controls.

The central classification is:

```text
propagation can pool source-formed synergy
signed DAGs can preserve declared ancestry
certificates can make declared predicates actionable
none of those alone attests physical source truth
```

## Local-model gate

The executable is a proof/regression certificate outside research-model
admission:

- the decision-changing theorems and counterexamples are analytic;
- the probe checks exact finite information partitions, event projections,
  graph reachability, and epistemic components;
- ideal signature and proof labels do not claim computational security;
- it is not a Hashgraph, gossip, Byzantine, cryptographic, or physical
  implementation; and
- no external hardware or provider path is needed.

The probe returned:

```text
HC-DU-048 gossip/DAG provenance certificate: 34/34 passed
```

## Routing

The sole next executable work object is:

```text
N5-SCF-P3
Provenance-Preserving Metastable-to-Byzantine Hardening
```

It will compare fast probabilistic preference with quorum/threshold locking
while preserving source binding, signed origin, route ancestry, and the first
equivocation witness. The matched null source remains mandatory. `N5-RS-P2`
remains deferred, not canceled. No paper, prediction, provider, hardware,
submission, publication, or external-contact state changed.
