---
title: "Run: N5-SCF-P1 joint-input no-minting and dependency-sensitive amplification"
status: completed
date: 2026-07-27
work_id: N5-SCF-P1
claim_id: HC-DU-047
authority: "Joe direct chat: Go"
result: "../explorations/joint-input-no-minting-synergistic-recovery-and-dependency-sensitive-amplification-2026-07-27.md"
probe: "../tests/du_joint_input_amplification_probe.py"
artifact: "../tests/artifacts/du_joint_input_amplification_result.json"
next_work: N5-SCF-P2
deferred_work: N5-RS-P2
paper_state_change: none
hardware_state_change: none
provider_state_change: none
---

# Run: N5-SCF-P1 joint-input no-minting and dependency-sensitive amplification

## Decision

Determine exactly when large populations, stochastic aggregation,
stigmergic traces, sampling, and cryptographic layers can improve a target
decision—and when the complete joint input makes recovery impossible.

Use analytic factorization, exact finite counterexamples, and rational
certificates. Do not build a network simulator or activate hardware.

## Execution receipt

The swing proved or exhibited:

1. deterministic and stochastic joint-input no-minting;
2. the correction that individual insufficiency does not imply joint
   insufficiency;
3. XOR and \(2\)-of-\(3\) Shamir synergistic recovery controls;
4. IID concentration versus copied, common-shock, and clustered evidence;
5. three exchangeable, pairwise-independent laws with identical marginal and
   pairwise statistics but different majority tails;
6. the exact stigmergic target-error law
   \(\delta+(1-2\delta)e_N\);
7. uniform-sampling error \(19/84\) versus eclipse error one at fixed
   population and sample size;
8. zero-knowledge, FHE/MPC, and threshold-authority boundaries; and
9. the absence of a universal effective-support scalar from raw population,
   marginal accuracy, and pairwise correlation alone.

The correct no-minting statement is:

```text
a downstream protocol cannot recover a target absent from the entire joint admitted input
```

not:

```text
a network cannot recover a target absent from every individual marginal
```

## Local-model gate

The executable is a proof/regression certificate outside research model
admission:

- the decision-changing theorems and counterexamples are analytic;
- the probe exhausts finite functions or evaluates exact rational formulas;
- it makes no claim of network, cryptographic, biological, or physical
  fidelity; and
- no external hardware or provider path is needed.

The probe returned:

```text
HC-DU-047 joint-input/amplification certificate: 24/24 passed
```

## Routing

The sole next executable work object is:

```text
N5-SCF-P2
Synergy-Preserving Gossip/DAG Provenance and Knowledge
```

It will compare synergy and null source worlds with matched local marginals,
then type what plain gossip, signed gossip, hash-DAG ancestry, and a
commitment/zero-knowledge provenance proof preserve. `N5-RS-P2` remains
deferred, not canceled. No paper, prediction, provider, hardware, submission,
publication, or external-contact state changed.
