---
title: "Run: N5-SCF-P3 metastable-to-Byzantine hardening and provenance lift"
status: completed
date: 2026-07-27
work_id: N5-SCF-P3
claim_id: HC-DU-049
authority: "Joe direct chat: Go"
result: "../explorations/metastable-to-byzantine-hardening-and-provenance-lift-2026-07-27.md"
probe: "../tests/du_metastable_byzantine_provenance_hardening_probe.py"
artifact: "../tests/artifacts/du_metastable_byzantine_provenance_hardening_result.json"
next_work: N5-SCF-P4
deferred_work: N5-RS-P2
paper_state_change: none
hardware_state_change: none
provider_state_change: none
---

# Run: N5-SCF-P3 metastable-to-Byzantine hardening and provenance lift

## Decision

Carry the unchanged source-bound and matched-null specimens through an exact
Avalanche-like confidence layer, a \(5\)-of-\(7\) Byzantine lock, explicit
and compressed certificates, threshold signing, private relation
verification, membership churn, and mobile corruption.

Determine what hardening genuinely adds, what certificate compression
forgets, and the exact premises under which the layers compose. Use analytic
finite proofs and counterexamples rather than a network or cryptographic
implementation.

## Execution receipt

The swing proved or exhibited:

1. exact wrong-preference probabilities of \(1/7\), \(1/343\), \(1/7\), and
   \(1\) under one sample, three independent samples, a reused correlated
   neighborhood, and eclipse respectively;
2. a minimum intersection of three for any two \(5\)-of-\(7\) quorums, so a
   correct non-conflicting lock excludes conflicting certificates under two
   Byzantine faults;
3. the separate liveness boundary: a \(4\mid3\) partition preserves safety
   but prevents a quorum;
4. identical proposal and hardened-certificate laws in the source-bound and
   target-independent null worlds, despite physical-target error zero versus
   \(1/2\);
5. the separation of validator quorum, declared source-key count, and
   physical controller independence;
6. signer-set preservation by explicit or bitmap-bearing certificates and
   signer-set loss under ordinary group-key threshold verification;
7. clean and rejected-equivocation histories with the same final quorum
   certificate;
8. a semantic provenance root invariant under benign relay subdivision,
   with route forensics retained separately when an action needs them;
9. the need to bind membership epoch and membership root into a certificate;
10. the need for proactive refresh, erasure, and epoch typing under mobile
    corruption;
11. the boundary that ZK, VSS, MPC, and threshold signatures certify or
    compute admitted relations without attesting an unmodeled physical
    target; and
12. an eight-premise scoped composition contract with an exact first-failure
    return for every omitted premise.

The central classification is:

```text
metastable confidence changes decision risk
quorum locking changes conflict safety
certificate design changes retained audit capability
none of these changes the physical truth of the source claim
```

The exact return is:

```text
SCOPED_LAYERED_FINALITY_COMPOSITION_WITH_CAPABILITY_INDEXED_PROVENANCE_LIFT
```

## Local-model gate

The executable is a proof/regression certificate outside research-model
admission:

- the decision-changing results are analytic finite theorems and
  counterexamples;
- the probe checks exact combinatorics, factorization fibres, certificate
  projections, and first-failure controls;
- ideal signature, threshold, proof, and MPC labels do not claim
  cryptographic implementation or security; and
- no simulator, external hardware, or provider path is needed.

The probe returned:

```text
HC-DU-049 metastable/Byzantine provenance hardening certificate: 43/43 passed
```

## Routing

The sole next executable work object is:

```text
N5-SCF-P4
Capability-Relative Selective Views and Regional Handoff
```

It will reuse the tentative, execution, accountability,
equivocation-audit, and physical-source action classes; derive the minimal
selective view sufficient for each; and test compact-certificate handoff with
on-demand provenance under partition, churn, rollback, and capability
expansion. The matched null source remains mandatory. `N5-RS-P2` remains
deferred, not canceled. No paper, prediction, provider, hardware,
submission, publication, or external-contact state changed.
