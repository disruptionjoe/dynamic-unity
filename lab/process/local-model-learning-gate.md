---
title: "Local Model Learning Gate"
date: 2026-07-26
status: ratified_repository_contract
contract_id: LMLG-01
claim_grade: "RESEARCH-ROUTING CONTRACT / NO SCIENTIFIC RESULT"
authority: "Joe direct chat"
probe_ref: ../../tests/du_local_model_learning_gate_probe.py
artifact_ref: ../../tests/artifacts/du_local_model_learning_gate_result.json
---

# Local Model Learning Gate

## Rule

> Build a local research model only when the model can produce a meaningful
> learning result before any external-hardware dependency, and that result is
> not already available at equal grade from a bounded literature and formal
> analysis pass.

Hardware may extend a locally productive model. It may not be the model's
first epistemic payoff.

## Scope

This gate applies to future simulations, toy models, finite fixtures,
numerical solvers, model-training runs, emulators, provider adapters, and
other executable constructions proposed as a way to learn about a live
Dynamic Unity question.

A minimal regression or proof-checking artifact created **after** an
independent result may preserve reproducibility without claiming model-derived
learning. It must remain proportional to that result and cannot bootstrap
itself into a new modeling program without passing this gate.

## Admission contract

Before building, record all eight fields:

| field | required answer |
|---|---|
| `question` | The exact uncertainty or decision the model addresses. |
| `research_only_baseline` | What bounded source review and formal analysis can already answer, including the strongest known absorber. |
| `local_learning_delta` | The specific result the executable model can generate that the baseline cannot provide at equal grade. |
| `generated_not_encoded` | Why that result is produced by the model rather than inserted through its rules, labels, target, fixture, or scoring function. |
| `pre_hardware_checkpoint` | The observable theorem candidate, counterexample, bound, classifier, architecture decision, or kill result available entirely on the current computer. |
| `decision_changed` | What research action changes if the local result is positive, negative, or null. |
| `minimal_build` | The smallest construction capable of reaching the checkpoint. |
| `stop_and_hardware_boundary` | When the local build stops, and what later hardware could add without being required for the first learning. |

Missing any field returns `INCOMPLETE_LEARNING_CONTRACT`.

## Counterfactual admission test

Ask in this order:

1. **No-hardware counterfactual.** If external hardware never becomes
   available, can the proposed build still answer a nontrivial question or
   change a research decision?
   - No: `EXTERNAL_PAYOFF_ONLY_STOP`.
2. **Research-only counterfactual.** Would a bounded source review or direct
   formal analysis deliver the same insight at the same grade without the
   build?
   - Yes: `DESK_RESEARCH_FIRST`.
3. **Generator test.** Does the model generate the proposed result rather than
   merely replay a known equation, encode the target in the fixture, or
   restate assumptions as output?
   - No: `DESK_RESEARCH_FIRST` or `INCOMPLETE_LEARNING_CONTRACT`.
4. **Decision-value test.** Would positive, negative, and null local outcomes
   change what DU does next?
   - No: `NO_DECISION_VALUE_STOP`.
5. **Minimality test.** Is this the smallest build that can reach the local
   checkpoint?
   - No: `REDUCE_BEFORE_ADMISSION`.

Only a full pass returns `ADMIT_LOCAL_LEARNING_BUILD`.

## What counts as pre-hardware learning

Eligible examples include:

- discovering a minimal counterexample or hostile completion not apparent
  from the formal statement;
- computing a tight finite bound, phase boundary, identifiability limit, or
  sample-complexity requirement;
- discriminating among competing architectures under frozen assumptions;
- finding that a proposed mechanism cannot produce its required behavior;
- locating a structural invariant that becomes a theorem target; or
- determining the smallest experiment capable of separating a model from its
  strongest admitted null.

The result need only be new to the active research decision at its declared
grade. It is not thereby novel in the literature, physically true, or
publishable.

## What does not count

- reproducing a result already established in a cited paper;
- simulating standard quantum mechanics merely to confirm that the simulator
  implements standard quantum mechanics;
- drawing or animating a mechanism whose consequences are already known;
- building a larger fixture to obtain more examples of an already classified
  behavior;
- preparing provider-specific plumbing whose first meaningful output requires
  a hardware job;
- fitting a target-coded toy whose desired conclusion is embedded in its
  state space, loss, labels, boundary, or source; or
- calling implementation familiarity, code volume, or readiness itself a
  scientific insight.

Use bounded research or formal analysis instead.

## Checkpoint and continuation

An admitted build begins with only its `minimal_build`. At the predeclared
checkpoint:

- local learning obtained: bank the result at its earned grade and decide
  whether another local question is justified;
- null but decision-changing: bank the kill or boundary and stop;
- no predeclared learning: return `STOP_NO_LOCAL_LEARNING`; and
- an external-hardware dependency appears before the checkpoint: return
  `EXTERNAL_PAYOFF_ONLY_STOP`.

A later hardware path is eligible only when the repository's separate
unavailable-by-default hardware gate also passes. At that boundary, issue one
awareness note. Without separate Joe authorization, take a local alternative
or park; do not use the local build as momentum for circling hardware.

## Scenario controls

| proposal | disposition | reason |
|---|---|---|
| Exhaustively search a finite completion class for the smallest same-record/different-response pair, then use the specimen to state a theorem | `ADMIT_LOCAL_LEARNING_BUILD` | The exact counterexample is generated locally and changes the theorem target before hardware. |
| Implement a published dephasing model only to recover its published curve | `DESK_RESEARCH_FIRST` | The claimed learning is already available from research. |
| Build a provider adapter whose first informative output is a real-device result | `EXTERNAL_PAYOFF_ONLY_STOP` | No meaningful pre-hardware checkpoint exists. |
| Compute the minimum intervention basis and finite-shot margin locally, with hardware later estimating the physical parameters | `ADMIT_LOCAL_LEARNING_BUILD` | Local experimental theory produces the first insight; hardware may add more. |
| Add a small deterministic regression after an exact theorem is proved independently | outside research-model admission | Reproducibility only; it earns no new-learning claim and must stay minimal. |

## Required receipt

Every admitted model receipt reports:

```text
admission disposition
research-only baseline
local learning delta
generated-not-encoded control
pre-hardware checkpoint result
decision consequence
stop or continuation
maximum grade
```

No build is justified by “it may be useful later.”
