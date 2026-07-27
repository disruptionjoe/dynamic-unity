---
title: "Run: N5-SCF-P4 capability-relative selective views and regional handoff"
status: completed
date: 2026-07-27
work_id: N5-SCF-P4
claim_id: HC-DU-050
authority: "Joe direct chat: Go go"
result: "../explorations/capability-relative-selective-views-and-regional-handoff-2026-07-27.md"
probe: "../tests/du_capability_relative_selective_view_handoff_probe.py"
artifact: "../tests/artifacts/du_capability_relative_selective_view_handoff_result.json"
next_work: N5-SCF-P5
deferred_work: N5-RS-P2
paper_state_change: none
hardware_state_change: none
provider_state_change: none
---

# Run: N5-SCF-P4 capability-relative selective views and regional handoff

## Decision

Reuse the source-bound and matched-null worlds plus the Position-3
certificate boundary. Freeze tentative response, conflict-safe execution,
signer accountability, equivocation proof, and physical-source adjudication
before defining selective views.

Compute the minimum sufficient view for each action and attack regional
handoff with:

- unavailable committed sidecars;
- stale membership epochs;
- capability expansion;
- incompatible partial views;
- adaptive self-confirming interest filters; and
- the unchanged physical-source null.

Use exact finite factorization and counterexamples, not a network simulator.

## Execution receipt

The swing proved or exhibited:

1. the exact action-relative factorization criterion
   \(\ker V\subseteq\ker A\);
2. exhaustive minimum field bundles for all five frozen actions over 512
   histories;
3. two incomparable certificate implementations sufficient for execution,
   only one of which preserves signer accountability;
4. strict refinement of history equivalence under capability enlargement;
5. simultaneous local action sufficiency for incompatible incomplete regional
   views without global-history reconstruction;
6. stronger capability from joined complementary views;
7. identical certificate and provenance commitments with different proof
   availability;
8. identical group-key verification records with current versus stale receiver
   epochs;
9. a self-confirming adaptive interest filter that hides a corrective event;
10. monotone positive fork evidence and nonmonotone absence of a fork;
11. a dead-reckoning failure under hidden acceleration, plus authoritative
    correction and explicit rollback controls;
12. failure of isolated shards to close a nonlocal quota invariant;
13. failure of every complete protocol-only selective view to adjudicate the
    matched null physical target; and
14. an eight-premise receiver-contextual handoff contract with exact
    first-failure controls.

The exact return is:

```text
CAPABILITY_RELATIVE_SELECTIVE_VIEW_AND_REGIONAL_HANDOFF_THEOREM
WITH_AVAILABILITY_EPOCH_AND_MONOTONICITY_BOUNDARIES
```

## Local-model gate

The executable is a proof/regression certificate outside research-model
admission:

- the result is stated analytically as finite factorization and explicit
  counterexamples;
- the script exhausts histories, projections, capability partitions, and
  first-failure controls;
- it does not implement or simulate an MMO, database, cryptographic protocol,
  consensus system, network, or physical observer; and
- no external hardware or provider path is needed.

The probe returned:

```text
HC-DU-050 capability-relative selective-view/handoff certificate: 28/28 passed
```

## Routing

The sole next executable work object in this interposed sequence is:

```text
N5-SCF-P5
DU Physical Collision and Portfolio Handoff
```

It must apply the completed distributed stack unchanged to one physical
record arena and the closed metastable host as a hostile control, then return
either a scoped physical correspondence or the first exact arrow where the
translation fails. `N5-RS-P2` remains deferred, not canceled. No paper,
prediction, provider, hardware, submission, publication, or external-contact
state changed.
