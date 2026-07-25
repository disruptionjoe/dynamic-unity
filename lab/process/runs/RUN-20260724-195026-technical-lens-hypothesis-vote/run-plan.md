---
title: "Run plan — technical-lens hypothesis panel and quadratic vote"
status: completed
doc_type: research_run_plan
created: 2026-07-24
run_id: RUN-20260724-195026-technical-lens-hypothesis-vote
target: dynamic-unity-repository-wide
---

# Run Plan: RUN-20260724-195026-technical-lens-hypothesis-vote

Plan created at: 2026-07-24T19:50:26-05:00

Status: completed

Run type: `exploration_and_priority_signal`

Target: `dynamic-unity / repository-wide Certified Causal Reality program`

Workflow: `eighteen inline technical lenses, two independently framed
hypotheses per lens, complete quadratic ballots with no self-votes, root
synthesis, deterministic audit, commit, and push`

Workflow source: `Joe direct chat, 2026-07-24: assemble at least ten and up
to twenty useful lenses including metastable consensus, hypergraphs,
cellular automata, distributed consensus, adversarial distributed systems,
zero-knowledge cryptography, and data/database networking; let each claim
two strongest hypotheses; then give every lens 100 quadratic credits to
weight every other hypothesis with no self-voting`

## Objective

Generate a diverse, falsifiable hypothesis portfolio from the complete
current repository, then identify cross-lens curiosity and priority without
mistaking a ballot for scientific evidence.

Each lens originates:

1. one strongest near-to-medium-term hypothesis; and
2. one higher-upside hypothesis selected for some combination of novelty,
   profundity, usefulness, and publishability.

Each hypothesis must state:

- the proposed relation;
- the declared scope;
- what makes it worth testing;
- a concrete falsifier or cheap failure mode; and
- its current warrant.

## Panel

The eighteen nonredundant lenses are:

1. metastable/Avalanche-style consensus;
2. hypergraphs, higher categories, and cycle filling;
3. cellular automata and quantum cellular automata;
4. distributed consensus and BFT;
5. adversarial distributed systems;
6. zero-knowledge cryptography;
7. distributed databases, gossip, and data networking;
8. quantum information and process tensors;
9. quantum error correction and fault tolerance;
10. information theory and coding;
11. control theory and system identification;
12. stochastic processes and phase transitions;
13. formal methods and model checking;
14. experimental metrology and optical clocks;
15. thermodynamics and resource theory;
16. causal inference and philosophy of science;
17. causal sets and emergent geometry; and
18. temporal networks and network science.

This includes every lens Joe named. Causal geometry and temporal networks
were retained because they introduce distinct reconstruction and
time-respecting-cut hypotheses. Additional personas were stopped when they
would merely duplicate one of these contracts.

## Ballot contract

- There are exactly `36` hypotheses, two owned by every lens.
- A lens may cast no vote on either hypothesis it owns.
- Every other hypothesis receives an explicit nonnegative integer weight;
  omitted positive allocations are recorded as zero.
- A ballot costs
  \(\sum_h v_h^2\) credits and must spend exactly `100`.
- Lenses may choose different concentration profiles; intensity is part of
  the quadratic vote.
- Aggregate rank is descending total vote units, then descending number of
  distinct supporting lenses, then stable hypothesis ID.
- The audit must verify `1,800` total credits, zero self-votes, complete
  non-owner weight surfaces, and deterministic output.

Votes are curiosity and comparative-priority signals only. They do not
promote a concept, create a core hypothesis, seed a prediction, bank a claim,
authorize the next swing, or establish truth.

## Repository state

- Repository session sync started successfully.
- Branch:
  `agent/research-compute-cleanup-2026-07-22`.
- Starting commit:
  `3842f90048b5606c9cded405d091214d124977fa`.
- The branch was clean and even with its upstream.
- Current canonical state is `LANES.yaml` revision 22.

## Planned outputs

- one complete panel, ballot, ranking, and synthesis exploration;
- one deterministic audit probe;
- one machine-readable ballot/ranking artifact;
- a compact tests README entry; and
- memory/log custody.

No current `H-CCR`, concept, prediction, claim-bank, or Lane priority is
changed by the panel itself.

## Validation

1. validate two hypotheses and ownership per lens;
2. validate unique IDs and falsifier fields;
3. validate every ballot has explicit weights for every hypothesis;
4. validate no self-votes and exactly 100 quadratic credits per lens;
5. recompute aggregate vote units, supporters, ties, and rank;
6. run twice and require byte-identical artifact output;
7. compile the probe and parse its JSON;
8. run `git diff --check`;
9. stage explicit paths only;
10. commit, push, and finish the repository session.

## Result

The inline panel completed with 18 lenses and 36 hypotheses. Every requested
specialty was represented; causal-set/geometry and temporal-network lenses
were added because they supplied nonredundant reconstruction and
time-respecting-cut hypotheses.

The complete report is:

`explorations/technical-lens-hypothesis-panel-quadratic-vote-2026-07-24.md`

The deterministic audit is:

`tests/du_technical_lens_hypothesis_quadratic_vote_probe.py`

Its artifact is:

`tests/artifacts/du_technical_lens_hypothesis_quadratic_vote_result.json`

The vote reconciles exactly:

```text
18 ballots
36 hypotheses
1,800 / 1,800 quadratic credits
436 vote units
0 self-votes
8 / 8 audit checks
```

The top results are:

1. `HG-B`, Cycle-Filling Public-Finality — 39 vote units, 13
   supporters;
2. `DC-A`, Loop-Resolution Finality — 39 vote units, 8 supporters;
3. `FM-A`, Decidable Refinement-Trichotomy Compiler — 34 vote units,
   13 supporters;
4. `QI-B`, Noisy Public Fixed-Algebra Convergence — 31 vote units,
   10 supporters; and
5. `QE-A`, Public Fact as Correctable Logical Algebra — 27 vote units,
   9 supporters.

`HG-B` wins the stable tie-break through broader support. `DC-A` receives
more quadratic credits because its fewer supporters vote more intensely.
Those two hypotheses are treated as one convergent theorem family in the
synthesis rather than two independent discoveries.

The ballot's integrated candidate is a Higher-Order Finality and Refinement
Compiler: compute loop syndromes, noninvertible equalizers/fixed algebras,
task-relative provenance, finite intervention bases, higher-certificate
effects, and a proof-carrying factorization/interface/remainder trichotomy on
unchanged distributed and quantum fixtures. This is a panel recommendation,
not authorization.

Primary hypotheses receive 278 vote units and frontier hypotheses 158.
Zero-vote hypotheses remain preserved and are not treated as falsified or
worthless.

Validation:

- probe run twice: `8/8` both times;
- artifact SHA-256, byte-identical:
  `9b68d5f34e7bb01c01f97317607cc2502c2acd253c2e0055c37267e31d853e38`;
- probe SHA-256:
  `7838eba7c3901bf19ba7ff54bc391b75740ef37c08c6a09b34c01539635eab2e`;
- Python compilation: passed;
- artifact JSON parse: passed; and
- `git diff --check`: passed.

No `H-CCR`, concept, prediction, claim, seed, ontology, or Lane priority was
changed. The vote remains a curiosity/priority signal and supplies no
scientific evidence or execution authority.
