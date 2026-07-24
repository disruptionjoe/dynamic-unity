---
title: "Conditional and abductive research contract"
status: active
doc_type: research_process
created: 2026-07-23
implementation: "tests/conditional_candidate_harness.py"
first_use: "explorations/science-council-three-track-swing-contract-2026-07-23.md"
---

# Conditional and abductive research contract

## Purpose

Make conditional construction and comparative abduction operational without
turning them into either second-class science or unconstrained story generation.
The contract makes candidates comparable by exposing their posits, free choices,
discriminators, and failure scope.

This is a research instrument, not a standing verification gate. Contract
completeness means **legible and comparable**, not correct, important, or ready
to bank.

## Required candidate surface

Every governed conditional or abductive probe records:

- its exact question and one or more typed warrants;
- assumptions labeled `STANDARD`, `PROJECT_NATIVE`, `CONDITIONAL_POSIT`, or
  `IMPORTED`;
- every material free choice, why it is not forced, and how sensitivity to it is
  tested;
- equations, observables, comparators, null models, falsifiers, and stop
  conditions;
- an explicit result, remaining uncertainty, and executable checks;
- for a concept-family test, the concept invariant, tested formalization, and
  whether a failure reaches the formalization or the concept.

The executable shape validator and deterministic artifact writer live in
`tests/conditional_candidate_harness.py`.

## Warrant types are non-ordinal

Do not reduce these relations to one "strength of derivation" ladder:

| Warrant | Relation established |
|---|---|
| `DERIVED` | The conclusion follows from stated premises by formal or mathematical argument. |
| `CONDITIONALLY_ENTAILED` | A labeled posit plus a specified completion implies a discriminating consequence. |
| `CONSTRUCTIVELY_REALIZED` | An explicit object or dynamics has been built and shown to possess the stated behavior. |
| `ABDUCTIVELY_PREFERRED` | Among declared rivals, one explanation wins a comparative test on compression, independence, robustness, or novel consequences. |
| `STRUCTURAL_ANALOGY` | A typed structural correspondence is present without an identity claim. |

A candidate may carry multiple warrants. No warrant licenses silently dropping
its premises.

## Comparative abduction

Abduction is comparative. Name the rivals and report:

1. **Explanatory compression:** independent observations accounted for per free
   choice.
2. **Evidence independence:** whether apparent consilience reuses the same
   assumption, dataset, or mathematical mechanism.
3. **Discriminating novelty:** a result a named null does not already produce.
4. **Robustness:** behavior that survives legitimate completion or
   formalization changes.
5. **Progressivity:** whether the work reduces arbitrary choices or adds risky
   consequences.

These dimensions are evidence. Do not collapse them into a false-precision score
unless a decision explicitly requires and justifies an aggregation rule.

## Concept-family failure scope

A formalization joins a concept family only if it carries the predeclared
invariant. Failure then closes that **formalization**, not the concept.
Concept-level closure requires either:

1. a direct no-go on the invariant; or
2. exhaustion of a materially diverse family whose failures share a mode traced
   to the invariant.

Swapping proxies after every failure without preserving the invariant is
story-shopping, not heterodox preservation.

## Admission and stop boundary

An explicit model with labeled assumptions, equations, and a real discriminator
is admitted to exploration. It reaches `BANK_REVIEW_ONLY` only after its
track-specific robustness tests, standard-rival comparison, and independent
claim audit; this instrument cannot bank it.

Stop rather than circle when a track:

- produces only behavior shared by its null;
- needs a new unconstrained parameter after each failed test;
- loses its signature under modest, physically legitimate perturbations; or
- cannot name an observation that distinguishes the construction from its
  antecedent inserted by hand.

Negative results should localize failure to a completion, formalization, or
conditional posit. Do not inflate them into global concept kills.
