---
title: "ECR-N5-S4 completion-invariant transfer and first capability leak"
status: completed
doc_type: run_plan
created: 2026-07-27
completed: 2026-07-27
run_id: RUN-20260727-dynamic-unity-completion-invariant-transfer
campaign_id: ECR-N5
swing_id: ECR-N5-S4
mode: execute
lanes:
  - 1
  - 3
  - 4
  - 6
  - A
channels:
  - CH-FORMAL
  - CH-SYN
  - CH-COLLIDE
  - CH-MODEL
starting_revision: aa50c9ae74f2757b5745f8467dc324efe541bc55
---

# ECR-N5-S4 completion-invariant transfer and first capability leak

## Objective

Hold the reduced four-state matter law fixed and compare the
history-retaining completion from `HC-DU-044` with a physically distinct
archive-hidden completion. Determine the finest record that is a quotient of
both native observer records, then test without refitting which preregistered
targets and capability classes factor through that common record.

The swing must distinguish:

1. future reduced-matter prediction;
2. historical write occurrence;
3. write count; and
4. native output-field access.

A positive result for the first target may not be credited as reconstruction
of the latter three.

## Frozen arena

- the four-state alternating-rate matter host and its complete reduced
  branch relation from `HC-DU-043/044`;
- the visible fresh-output completion and the exact hidden-reservoir twin
  from `HC-DU-044`;
- the same matter interventions and the same resolved history set in both
  arms;
- a physical observer boundary that admits the archive fragment `A` and
  excludes reservoir `H`;
- native visible record `r_V=(X_T,\text{visible history token})`;
- native hidden record `r_H=(X_T,\text{blank})`;
- common records defined only as target-independent quotients of both
  native records;
- capability filtration
  `H_matter ⊂ H_occ ⊂ H_count ⊂ H_output`; and
- no decoder, interface, access route, completion, target, or resource
  contract may be refit after the comparison.

## Preregistered targets

| target | frozen meaning | expected discriminator |
|---|---|---|
| `T_next` | complete next-step reduced-matter branch law from terminal matter state | positive Markov/operational-closure control |
| `T_occ` | whether at least one selected write occurred since the certified epoch reset | minimum history target |
| `T_count` | number of selected writes in the retained horizon | first refinement beyond the binary occurrence quotient |
| `T_word` | resolved output-history word | native output-field capability |

The expectations are preregistered nulls, not verdicts:

- `T_next` should factor through the terminal matter state in both arms;
- `T_occ`, `T_count`, and `T_word` should not factor through the
  completion-common record if that record is only the matter endpoint;
- the visible binary occurrence quotient should reconstruct `T_occ` but not
  `T_count`; and
- granting hidden-reservoir access should repair history only by changing
  the observer boundary and capability/resource contract.

## Exact questions

1. What is the finest common quotient of `r_V` and `r_H`?
2. Is its equivalence relation invariant under lossless relabeling of either
   native archive?
3. Which preregistered targets are constant on its fibres?
4. Does one common no-refit decoder exist for any nontrivial historical
   target?
5. What is the smallest exact same-common-record/different-target witness?
6. Which capability enlargement first exposes information hidden by the
   common quotient?
7. Does full-environment completion repair the result within the old
   contract, or only after observer/access/resource retyping?

## Formal result sought

For finite completion records `r_i : Ω -> R_i`, let `K_i=ker(r_i)`.
The finest target-independent common quotient has kernel

```text
K_common = join_i K_i
```

where the join is the equivalence closure of the union. A target
`t : Ω -> T` transfers through every native record without refit exactly
when

```text
K_common subset ker(t).
```

The finite probe may exhaust partitions and emit witnesses, but the theorem
must be established independently by factorization reasoning.

## Local-model and hardware disposition

`DIRECT_EXACT_ANALYSIS_WITH_MINIMAL_PARTITION_CERTIFICATE`.

The executable is a bounded proof/regression artifact, not a microscopic
environment simulation. Its local learning delta is the exact common
quotient, the target-by-target transfer classification, and the minimum
first-leak witness. It must stop after those receipts. No external hardware,
provider adapter, trajectory simulation, or parameter sweep is admitted.

## Strongest absorbers

- finite partition lattices and quotient factorization;
- Blackwell and quantum statistical sufficiency;
- Markov sufficient statistics and controlled lumpability;
- Stinespring/complementary-channel nonuniqueness;
- process tensors and full-environment completion;
- quantum trajectories/unravellings; and
- observer-relative access and resource-accounted capability.

## Evidence ceiling

A scoped finite common-quotient theorem, exact positive reduced-matter
transfer, exact adverse history-transfer witness, and capability-indexed
completion/access boundary. The result cannot establish a universal archive
no-go, endogenous record selection, ontology, new physics, a physical
prediction, or a paper merely by succeeding.

## Stop conditions

Stop or downgrade if:

- the common record is defined from a held-out target;
- the visible and hidden arms differ in the reduced matter process;
- a coordinate relabeling is counted as a hostile physical completion;
- hidden-reservoir access is added without retyping the observer boundary
  and resources;
- future matter prediction is presented as historical reconstruction;
- a different decoder is fit separately for each target or completion;
- full-environment distinguishability is confused with accessible record
  sufficiency; or
- the finite certificate is treated as selecting a microscopic
  environment.

## Planned outputs

- one scoped common-quotient and completion-transfer result;
- one minimal exact partition/factorization certificate;
- explicit positive and hostile target witnesses;
- a capability filtration and first-leak receipt;
- a collision against the strongest standard absorbers;
- a retyped `ECR-N5-S5` robustness/adjudication contract;
- concise orientation, Lane, concept, counter-assumptive, campaign, and test
  updates; and
- this Run Plan with a closing receipt.

## Closing receipt

`ECR-N5-S4` completed as `HC-DU-045`.

The unique finest target-independent quotient common to the visible-archive
and hidden-reservoir native records is terminal matter state. It is a strict
compression of the nine-history arena and reconstructs the complete
next-step reduced-matter branch law without refit. It does not reconstruct
write occurrence, count, or event word.

The exact cross-completion first capability leak is historical occurrence.
Inside the visible binary epoch record, the first leak is write count. Full
`A+H` access reconstructs all frozen targets only by enlarging the observer,
action, and resource contract and becoming injective history tomography.

The exact certificate exhausts all 21,147 partitions of the nine-history
arena and passes all checks. The host verdict is:

```text
MARKOV_OPERATIONAL_CLOSURE
COMPLETION_AND_ACCESS_RELATIVE HISTORY SUFFICIENCY
NO_ENDOGENOUS_ARCHIVE FOR THIS HOST
H-CCR-17 REMAINS OPEN
```

No claim, paper, prediction, ontology, hardware result, or provider action is
promoted. `ECR-N5-S5`, robustness and host-level North-Star adjudication, is
the sole next executable campaign object.
