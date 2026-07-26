---
title: "Physical sufficiency acquisition gate and finite-shot reconstruction certificate"
date: 2026-07-26
status: completed_prospective_gate
doc_type: public_sidecar_audit_prospective_acquisition_contract_and_scoped_finite_sample_result
claim_grade: "BOUNDED PUBLIC-DATA AUDIT / VERSIONED PROSPECTIVE PHYSICAL PACKET / EXACT COVERAGE LOGIC FOR A BINARY RESPONSE SLICE / NO PHYSICAL FACTORIZATION, REMAINDER, ONTOLOGY, OR NEW-PHYSICS VERDICT"
candidate_ids:
  - HC-DU-036D
paper_id: DU-PAPER-007
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
schema_ref: ../specs/physical-sufficiency-acquisition-packet-v0.1.schema.json
probe_ref: ../tests/du_physical_sufficiency_acquisition_gate_probe.py
artifact_ref: ../tests/artifacts/du_physical_sufficiency_acquisition_gate_result.json
run_id: RUN-20260726-010042-physical-sufficiency-acquisition-gate
---

# Physical sufficiency acquisition gate

## Result

The North-Star bottleneck has moved one full step.

The bounded Xiang sidecar audit is closed at public repository commit
`47d67598a304bb72c315bf05ddfadcda5f4be290`:

> **No joined shot-level sidecar is present in the inspected public tree.**

The repository is scientifically useful. It contains acquisition code,
randomized-benchmarking schedules, processed experiment data, train/test
partitions, learned open-quantum-evolution models, and reconstructed process
tensors. But its reusable experimental rows have already been compressed to
a Clifford sequence plus a calibrated terminal probability. The individual
measurement outcomes and the calibration values that produced that
probability are not retained in the exported row.

Dynamic Unity therefore stops public reuse of that packet for
`HC-DU-036C`. It does not stop using the paper as a process-model and
experimental-design reference.

The replacement is now executable:

1. a versioned, implementation-complete acquisition schema;
2. a strict join validator;
3. a conservative finite-shot binary-response certificate;
4. positive controls for base reconstruction, minimal refinement, and a
   completion-class-relative remainder;
5. an honest finite-shot inconclusive control; and
6. refusal controls for aggregate data, missing attempts, unjoined
   calibration, and incomplete causal breaks.

The probe passes `12/12` checks. Synthetic controls remain explicitly
nonphysical. No North-Star ontological branch has been selected.

## Why this is the highest-value present move

Dynamic Unity already possesses the exact finite mathematical trichotomy:
base reconstruction, refined reconstruction, or a positive margin relative
to a frozen completion class. Its repeated synthetic remainders have been
absorbed by adding omitted environment, route, controller, decoder,
provenance, or resource structure.

The next missing fact was not another theorem-shaped fixture. It was whether
the theorem could consume a real process without silently inventing:

- raw outcomes from a plotted probability;
- rejected attempts from the surviving denominator;
- calibration epochs from a methods paragraph;
- intermediate selective outcomes from a terminal measurement;
- controller and decoder identity from source code;
- or a complete causal break from a nominal reset instruction.

This gate makes those substitutions mechanically impossible.

## Bounded Xiang sidecar audit

### Sources

- Xinfang Zhang et al.,
  [“Learning and forecasting open quantum dynamics with correlated
  noise”](https://www.nature.com/articles/s42005-025-01944-2),
  *Communications Physics* **8**, 29 (2025).
- Chu Guo,
  [public data and reconstruction repository](https://github.com/guochu/pt_recovery),
  inspected at commit
  `47d67598a304bb72c315bf05ddfadcda5f4be290`.

The paper correctly states that a process tensor maps intervention sequences
to final system states and that the learned OQE may fail outside its
incomplete unitary-training data. That is already a strong reason not to
reinterpret the learned tensor as a complete selective-instrument record.

### Exact audit receipt

The recursively inspected tree contains `1128` files. No filename matched the
bounded sidecar terms `shot`, `count`, `memory`, `calib`, `invalid`, `reject`,
`reset`, `controller`, `decoder`, `provenance`, `raw`, `selective`,
`instrument`, `causal`, `break`, `readout`, or `confusion`.

Absence of a keyword is not the decisive result. The representative
acquisition lineage is:

| public object | exact inspected fact | consequence for DU |
|---|---|---|
| `standard_rb_1q_full_data.json` | `7800` rows; each has only `cl_ops` and `p0` | no individual shot, validity, calibration, or route join |
| `rb_data_0.1.npy` | `200` appended arrays, each shape `(39,)`, `float64` | one calibrated probability per sequence, not repeated binary outcomes |
| `standard_rb_sched.log` | emitted Clifford sequence identities and decompositions | useful intervention provenance, but not outcome provenance |
| `data_process.ipynb` | reshapes the arrays to `200 x 39`, joins them to the schedules, and writes `cl_ops + p0` | confirms where the row-level information boundary is introduced |
| `Q67_flux_sq_rb_script.py` | forms complex acquisition averages; uses the last two values as `cal0` and `cal1`; rotates to a calibrated axis; removes those values; saves only `p0` | the calibration was physically used but is not joined to the exported probability |
| article versus representative script | article text says each reported \(f\) averages `1024` outcomes; the inspected script configures `2048` repetitions | exact run/version provenance is required; neither number may be assigned to every row by assumption |

Pinned blobs:

| object | blob |
|---|---|
| `README.md` | `08acfaae30ca332a60f5b6fdc1b1cb1262482546` |
| `split_rb_data.jl` | `63875ce93997ce23fc7dc334e8754df2d994c5c3` |
| representative `data_process.ipynb` | `a65156052d5f9380eab7c279338da5d0fccd4c4a` |
| representative `rb_data_0.1.npy` | `0d6a8c2742a7d6cf5d13bdca68235d5a0d013126` |
| representative `standard_rb_1q_full_data.json` | `8ef973b3197f062326b75c9cc55b20647c8f3615` |
| representative `Q67_flux_sq_rb_script.py` | `e0f650f0e01d4cdf3fdaa3170efb709dba4a2304` |

The exact bounded verdict is:

```text
NO_JOINED_SHOT_LEVEL_SIDECAR
```

This means “not in the inspected public tree.” It does not mean the source
laboratory never possessed the data.

## The acquisition packet

The canonical embedded-table interchange is
[`physical-sufficiency-acquisition-packet-v0.1.schema.json`](../specs/physical-sufficiency-acquisition-packet-v0.1.schema.json).
Large experiments may stream the same row definitions as JSONL, Arrow, or
Parquet, but the manifest and hashes must reproduce this logical packet.

The executable ingress command is:

```bash
python3 tests/du_physical_sufficiency_acquisition_gate_probe.py \
  --packet path/to/packet.json
```

It prints the assessment without rewriting the deterministic control
artifact. An incomplete packet exits `2` with exact refusal codes.

### 1. Frozen comparison contract

Before acquisition, the packet fixes:

- observer and access boundary;
- candidate record field;
- intervention family;
- response family and outcome alphabet;
- operational metric and equivalence tolerance;
- familywise error budget;
- target-independent completion class;
- componentwise resource vectors;
- every admitted quantum, classical, controller, decoder, environment,
  archive, and route memory;
- minimum held-out shots per response cell; and
- holdout and blinding policy.

The freeze timestamp must precede acquisition. A record or completion selected
after reading held-out responses fails the contract.

### 2. Every attempted trial

The attempt ledger is contiguous and includes valid, invalid, aborted,
heralded, and rejected attempts. A valid trial carries one raw binary outcome.
An invalid trial carries no outcome and a nonempty rejection reason.

Each row retains:

- history, sequence, repeat, and physical order;
- preparation and intervention;
- candidate record and independently formed refinement labels;
- selective instrument outcome;
- terminal setting and result;
- calibration block;
- controller, decoder, and route version;
- immutable raw provenance;
- training, held-out, or causal-break role; and
- causal-break identity where applicable.

An aggregate `p0` is never accepted as a substitute.

### 3. Calibration and process schema

Every trial joins to a time-valid calibration block with:

- raw readout-error counts;
- preparation model and immutable preparation-calibration object;
- joint uncertainty attachment;
- controller and decoder version;
- a frozen worst-case total-variation allowance for remaining joint SPAM and
  drift, with its warrant; and
- an explicit uncertainty method.

The process table separately fixes the selective-map convention,
normalization, physicality constraint, tomography scope, and immutable
raw-row-to-map implementation. A learned terminal predictor is not silently
promoted into a complete selective instrument.

### 4. Multi-time events, routes, and causal breaks

Every valid trial has an ordered event row. The route passport explicitly
names source, reference, processor, pointer, archive, detector, environment,
controller, decoder, ordered ports, and resources.

A candidate remainder additionally requires a causal-break arm. Each admitted
retained memory marked reset-required must appear in a successful,
independently verified reset receipt joined to the trial. Resetting the system
qubit while an environment qubit, controller branch, decoder cache, or
acquisition buffer retains history is not a complete causal break.

The schema can prove that a receipt is present and joined. It cannot prove
that a laboratory assertion is physically true. The verification method and
raw witness remain experimental obligations.

## `HC-DU-036D` — finite-shot epsilon certificate

This swing earns one scoped statistical successor to the exact-rational
trichotomy.

Let the frozen packet contain finitely many binary response cells and binary
readout-calibration cells. Let \(m\) be their total count and let the global
error budget be \(\alpha\). For each empirical proportion with \(n\) shots,
use the simultaneous Hoeffding radius

\[
r(n,m,\alpha)
=
\sqrt{\frac{\log(2m/\alpha)}{2n}}.
\]

By Hoeffding's inequality and a union bound, all response and calibration
probabilities lie in their intervals simultaneously with probability at
least \(1-\alpha\).

For readout errors \(e_0=P(Y=1\mid X=0)\) and
\(e_1=P(Y=0\mid X=1)\), the observed response satisfies

\[
q=e_0+(1-e_0-e_1)p.
\]

If the entire calibration interval obeys \(1-e_0-e_1>0\), interval division
gives a conservative identified interval for \(p\). The packet's frozen joint
SPAM/drift allowance expands that interval.

For histories \(h,h'\) carrying the same record under intervention \(a\),
subtract their identified intervals to obtain
\(D_{h,h',a}\), an interval for the binary total-variation difference.
Given a predeclared operational tolerance \(\varepsilon\):

- if every \(D_{h,h',a}\subseteq[-\varepsilon,\varepsilon]\), the quotient is
  certified \(\varepsilon\)-sufficient for the declared response family at
  simultaneous confidence \(1-\alpha\);
- if any
  \(D_{h,h',a}\cap[-\varepsilon,\varepsilon]=\varnothing\), that quotient is
  certified to fail \(\varepsilon\)-sufficiency; and
- otherwise the result is `INCONCLUSIVE_FINITE_SHOT`.

Apply the rule first to the candidate record and then, without changing the
data-dependent class, to each admitted completion:

1. base certifies: `TOLERANCE_BOUNDED_BASE_RECONSTRUCTION`;
2. base fails and an admitted completion certifies:
   `TOLERANCE_BOUNDED_REFINED_RECONSTRUCTION`, returning every
   componentwise resource-Pareto-minimal repair;
3. base and every frozen completion fail:
   `TOLERANCE_BOUNDED_CLASS_RELATIVE_REMAINDER_CANDIDATE`; or
4. any relevant confidence region overlaps both sides:
   `INCONCLUSIVE_FINITE_SHOT`.

This is exact coverage logic built from standard concentration inequalities,
not a claimed new statistical theorem. Its Dynamic Unity value is that it
prevents finite samples from being forced into an exact yes/no trichotomy.

It is currently implemented for a binary held-out response slice. A full
selective-Choi use must provide the frozen tomography likelihood or confidence
region through the packet's process adapter and charge the corresponding
joint uncertainty. The binary slice must not be described as complete process
tomography.

## Executed controls

The deterministic probe covers all four scientific branches and four major
integrity failures:

| control | expected and observed result |
|---|---|
| same candidate record, same responses | tolerance-bounded base reconstruction |
| same candidate record, different environment-conditioned responses, formed environment label added | tolerance-bounded refined reconstruction |
| every frozen completion retains a separated same-record pair | completion-class-relative remainder candidate |
| response difference smaller than what the current confidence region can resolve | finite-shot inconclusive |
| Xiang-style `cl_ops + p0` object | incomplete contract |
| one required retained controller memory omitted from a reset receipt | incomplete contract |
| one trial linked to a nonexistent calibration block | incomplete contract |
| declared attempt count exceeds retained rows | incomplete contract |

The refined control includes two sufficient completions. The dominated
higher-resource route completion is removed; only the formed environment
record remains Pareto-minimal.

All four classification controls carry
`evidence_kind=synthetic_contract_control`, so the artifact sets
`scientific_verdict=false`.

## Prospective physical assay

The cheapest credible implementation is a co-designed two-qubit
system--environment experiment, close to the Xiang platform but with the
record lineage preserved from acquisition.

### Physical specimen

- **Source:** independently calibrated system preparations.
- **Environment/reference:** a controllable coupled memory qubit plus every
  declared additional retained memory.
- **Instrument:** a two-outcome QND or loss-like intermediate instrument on
  the system with an archived outcome.
- **Continuations:** a preregistered, tomographically spanning set of
  outcome-conditioned controls, including interventions not used to select
  the record.
- **Output:** shot-resolved terminal measurements.
- **Archive:** append-only intermediate outcome plus trial provenance.
- **Completions:** environment syndrome, analog detector record, route,
  controller branch, decoder state, and drift block—only where each is
  independently formed and accessible under a charged resource passport.

### Mandatory arms

1. **Normal history:** allow system--environment memory to persist.
2. **Complete causal break:** reprepare every reset-required quantum and
   classical memory, clear controller/decoder/acquisition state, and record an
   independent reset witness.
3. **Held-out continuation:** reveal the frozen response only after record and
   completion selection.
4. **Boundary expansion:** deliberately admit the strongest independently
   formed omitted record and charge its access and reset resources.
5. **Corrupted integrity controls:** delete one attempt, misjoin one
   calibration block, alter one controller version, and omit one reset
   receipt; the validator must refuse all four.

### Decision

The first scientifically useful outcome need not be a remainder.

- Base reconstruction would show that one physically formed archive is
  operationally sufficient at a declared resolution.
- A minimal refinement would identify exactly which ordinary physical memory
  the candidate record omitted.
- Inconclusiveness would quantify the shot or calibration improvement needed.
- A class-relative remainder would nominate a finite intervention and margin
  for the next completion challenge.

Only the last branch, after repeated physically justified boundary expansion,
could begin to pressure standard quantum-process completeness. One experiment
cannot establish record-first ontology.

## What changed for the North Star

Before this swing, the flagship had:

- exact finite mathematics;
- synthetic process and distributed controls;
- a list of missing physical fields; and
- no ingestible public packet.

After this swing, it has:

- a closed bounded public-reuse decision;
- an immutable acquisition grammar;
- a machine-enforced no-aggregate/no-hidden-memory boundary;
- a finite-shot theorem that includes an inconclusive branch;
- proof-carrying response and refinement certificates; and
- a concrete physical acquisition design.

The remaining bottleneck is now external and specific:

> Acquire one real packet under this schema—or map an existing raw packet into
> it without inventing any join—and then run the frozen assay.

That is a much smaller and more falsifiable problem than “find physical
evidence for certified causal reality.”

## Stops and limitations

- The public audit is commit-bounded non-location, not proof that no private
  sidecar exists.
- The finite-shot result is an \(\varepsilon\)-equivalence statement, not a
  proof of exact equality.
- Hoeffding--Bonferroni is deliberately conservative; a preregistered
  likelihood-ratio, e-process, or joint convex confidence region may improve
  power without changing the contract.
- A schema cannot authenticate a false laboratory attestation. Hashes,
  signatures, independent reset witnesses, and raw calibration objects must
  ground the rows.
- A complete packet does not prove the completion class physically
  exhaustive.
- A response-slice certificate is not complete selective-process
  reconstruction.
- A completion-class-relative remainder is not irreducible new physics.
- No author contact, data request, experiment, paper activation, submission,
  publication, or ontological promotion occurred.

## Reopen rule

Reopen the physical run only when one packet passes the validator with:

1. all raw attempts and binary outcomes;
2. joined preparation, readout, and joint systematic calibration;
3. complete selective multi-time events;
4. immutable controller, decoder, route, and raw provenance;
5. independently verified reset coverage over every admitted retained memory;
6. pre-acquisition record, completion, tolerance, resource, and holdout
   freeze; and
7. enough held-out shots for at least one confidence interval to leave the
   inconclusive region.

Until then, do not spend another swing fitting aggregate public probabilities
or building another synthetic completion fixture.
