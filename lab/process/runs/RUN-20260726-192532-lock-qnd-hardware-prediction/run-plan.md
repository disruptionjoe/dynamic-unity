---
run_id: RUN-20260726-192532-lock-qnd-hardware-prediction
status: completed
repository: dynamic-unity
authority: "Joe direct chat: lock the prediction now so a later publication can cite the dated pre-data commitment even if the hardware run is never executed"
starting_revision: 6cff2b354676
prediction_id: PRED-DU-004
lanes:
  - lane_7
  - lane_A
channels:
  - CH-EMPIRICAL
  - CH-PAPER
maximum_grade: "REGISTERED PRE-DATA STANDARD-QUANTUM PREDICTION FOR ONE FROZEN PROVIDER-CONDITIONAL CIRCUIT SUITE / NO HARDWARE EVIDENCE, NEW PHYSICS, PRED-DU-003 ADJUDICATION, PAPER ACTIVATION, SUBMISSION, OR PUBLICATION"
write_boundary:
  - START-HERE.md
  - LANES.yaml
  - explorations/prediction-register.md
  - explorations/locked-qnd-memory-hardware-prediction-2026-07-26.md
  - lab/acquisition/README.md
  - lab/process/runs/RUN-20260726-192532-lock-qnd-hardware-prediction/run-plan.md
external_action_authorization: "Local analytic derivation, repository commit, and non-force GitHub push only; no provider/account access, hardware submission, data acquisition, contact, paper activation, submission, publication, or other external action."
---

# Lock the frozen QND-memory hardware prediction

## Objective

Create a public, dated, pre-data prediction for the already frozen
`du-qnd-memory-causal-break/0.1` suite. The lock must:

1. bind the prediction to the exact driver, semantic manifest, circuit
   identities, pointer angle, and shot plan;
2. state the ideal ordinary-quantum joint distribution and its exact
   record-sufficiency consequences;
3. keep the retained classical pointer archive separate from the reset
   response boundary;
4. state what a future provider run can and cannot adjudicate;
5. preserve any future hardware tolerances as a separate preregistration
   dependency rather than choosing them after data; and
6. be citable later even if no hardware job is ever submitted.

## Frozen object

- protocol: `du-qnd-memory-causal-break/0.1`;
- driver SHA-256:
  `7aec5321e1aa54603bded82cb4c00de6bcd2e0965cba341af9502816e3c08294`;
- pointer angle: \(\pi/2\);
- circuit-order seed: `271828`;
- circuits: `19`;
- planned shots: `256` per circuit, `4864` total requested shots;
- semantic-manifest SHA-256:
  `9f118bf1736d6adbd9e1cd39985fc4b9d273307da98c7f1f4d649eb5bff555d5`;
- data state: no hardware job submitted and no hardware result seen.

## Prediction to derive and lock

For equally allocated histories \(h\in\{0,1\}\) and interventions
\(a\in\{0,1\}\):

\[
E=h,\qquad Y=h\oplus a,
\]

while the incomplete pointer satisfies

\[
P(P=0\mid h=0)=1,\qquad
P(P=0\mid h=1)=P(P=1\mid h=1)=\frac12.
\]

Therefore:

- the overlap stratum \(P=0\) contains same-pointer histories with disjoint
  response laws, with total-variation separation one;
- the ideal Bayes error using only pointer plus intervention is \(1/4\);
- adding environment makes the ideal Bayes error zero;
- the ideal accuracy gain is \(1/4\);
- \(H(Y\mid P,A)=0.6887218755408673\) bits and
  \(H(Y\mid P,E,A)=0\);
- after the declared three-qubit causal break,
  `(reset_witness, environment, output)=(000,0,0)` independently of
  pre-break history in the ideal model; and
- the already measured classical pointer archive remains retained, so the
  causal-break null is not a claim that every classical trace vanished.

## Hardware interpretation boundary

A future ordinary provider result may test the prediction only on returned
shots, after its own pre-data statistical/calibration contract is frozen.
The present lock fixes the estimands and expected direction but does not
invent a hardware tolerance without a selected backend, calibration model,
and power calculation.

The result cannot by itself:

- observe rejected/lower-level attempts or every controller/environment
  memory;
- reach `IMPLEMENTATION_COMPLETE_MAPPING_ELIGIBLE`;
- adjudicate `PRED-DU-003`;
- establish a finality residual or new physical law; or
- turn a standard-QM calibration result into a Dynamic Unity novelty claim.

## Stop conditions

- Do not submit a provider job.
- Do not call the lock an experiment result.
- Do not call the ordinary-QM prediction unique to Dynamic Unity.
- Do not select hardware thresholds after seeing data.
- Do not imply that a Git commit is a trusted third-party timestamp; it
  cryptographically binds content, while the public push supplies ordinary
  public provenance.
- Do not seed or activate a paper merely because the prediction is locked.

## Intended durable outputs

1. one dated prediction-lock receipt;
2. one stable `PRED-DU-004` register entry;
3. one acquisition-guide pointer;
4. one machine-readable Lane pointer without priority movement; and
5. one public Git commit that later work can cite as the pre-data record.

## Completion receipt

Completed on 2026-07-26 before any hardware submission or hardware-result
inspection.

- Registered `PRED-DU-004` as
  `LOCKED PRE-DATA / NOT EXECUTED / STANDARD-QM CONTROL`.
- Bound the prediction to the exact driver SHA-256, protocol, pointer angle,
  circuit-order seed, 19-circuit plan, 256-shot plan, and semantic-manifest
  SHA-256.
- Derived and locked the complete nonzero ideal joint distribution.
- Proved the exact pointer-only Bayes error \(1/4\), refined error zero,
  ideal accuracy gain \(1/4\), and conditional-entropy reduction
  `0.6887218755408673 -> 0` bits.
- Scoped the causal-break null to the reset-witness, environment, and output
  response while preserving the retained classical pointer archive.
- Kept backend-specific statistical tolerances as a separate mandatory
  pre-submission preregistration rather than choosing them without a backend
  or after data.
- Changed no circuit, acquisition driver, hardware state, paper state, or
  scientific priority.
- Performed no provider/account access, hardware submission, acquisition,
  contact, paper activation, submission, or publication.

Validation:

- exact rational Bayes-error derivation: `1/4 -> 0`;
- exact conditional entropy:
  `0.6887218755408673 -> 0` bits;
- hardware-bridge structural controls: `15/15`;
- cold-start/agent orientation contract: `54/54`;
- `LANES.yaml` parse and manifest revision `65`: passed;
- prediction identifiers: four unique `PRED-DU-*` entries;
- changed-surface local links: `75/75`;
- source driver SHA-256:
  `7aec5321e1aa54603bded82cb4c00de6bcd2e0965cba341af9502816e3c08294`;
- `git diff --check`: passed.

Final disposition:

```text
PRE_DATA_PREDICTION_LOCKED
ORDINARY_QM_BRANCH
PUBLIC_COMMIT_CITABLE_IF_UNRUN

NO HARDWARE RESULT
NO BACKEND_SPECIFIC_STATISTICAL_PREREGISTRATION
NO PRED_DU_003_ADJUDICATION
NO NEW_PHYSICS_OR_PAPER_PROMOTION
```
