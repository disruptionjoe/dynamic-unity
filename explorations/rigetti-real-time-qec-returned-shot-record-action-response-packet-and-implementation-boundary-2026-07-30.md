---
title: "Rigetti real-time QEC returned-shot record/action/response packet and implementation boundary"
status: banked_scoped_result
doc_type: exploration_result
created: 2026-07-30
claim_id: HC-DU-168
run_id: RUN-20260730-142222-rigetti-fast-feedback-packet-audit
evidence_grade: 4
---

# Real-time QEC returned-shot packet

## Executive result

Riverlane and Rigetti's open fast-feedback dataset is the strongest public
physical record packet Dynamic Unity has inspected so far.

It is not aggregate-only. Within each returned hardware repetition, the HDF5
row joins:

- the ordered hard measurement history;
- the corresponding complex soft readout values;
- the FPGA decoder registers;
- a decoder/control timing value;
- the decoder branch used by the documented conditional \(X\) action; and
- a later measurement of the conditional qubit.

It also retains the QPU identity, qubit map, Stim circuit, run metadata,
explicit no-reset status, and immediately following measurement-fidelity,
double-measurement, and \(T_1\)-delay reference packets.

But it still does not cross the implementation-complete boundary. It has no
census of every controller trigger, rejected or retried attempt, main
physical Quil/pulse program, decoder firmware/configuration, controller route
or hidden memory, within-measurement raw waveform, physical archive policy,
or declared hidden-environment scope.

Disposition:

```text
SOURCE_PINNED_JOINED_PHYSICAL_PACKET_FOUND
+ RETURNED_SHOT_MULTI_TIME_REOPENER_EARNED
+ CONDITIONAL_ACTION_AND_LATER_RESPONSE_JOINED
+ REPEATED_HARD_HISTORY_DECODER_COMPATIBILITY
+ ALL_ATTEMPT_VISIBILITY_STILL_OPEN
+ IMPLEMENTATION_COMPLETE_REOPENER_NOT_MET
+ NO_GRADE_5_REMAINDER
+ NO_READY_SUCCESSOR
```

## 1. Frozen sources

The audited file is
`fast_feedback_raw_data.h5` from the [version-2 Zenodo
record](https://zenodo.org/records/15364358):

```text
MD5     3b2503a80f2b92916660489e2f07e880
SHA256  dd2a3d48e86ea81094b44439fb58a3d9788757e26799bd4ee7497eb94798ed08
```

The [primary paper](https://arxiv.org/abs/2410.05202) and its
[published version](https://www.nature.com/articles/s41467-026-73331-6)
describe the physical experiment: after the stability experiment, the FPGA
decoder receives the measurement outcomes; `DASR=1` triggers a conditional
\(X\) on qubit 50; qubit 50 is measured again after a fixed delay. The paper
reports a 9.6 microsecond full response time at nine rounds and states that
resets were unavailable.

The external HDF5 remains uncommitted. The hashes, audit code, and compact
derived receipt are durable.

## 2. Exact retained packet

Eight circuit groups cover two through nine QEC rounds. Each contains 1,000
rows. Across all groups, the packet retains:

| field | exact retained content |
|---|---:|
| returned hardware repetitions | 8,000 |
| classified measurement events | 216,000 |
| complex soft measurement events | 216,000 |
| decoder-register rows | 8,000 |
| decoder/control timing rows | 8,000 |
| post-feedback qubit-50 responses | 8,000 |
| \(T_1\)-delay reference groups | 13 × 10,000 rows |
| measurement-fidelity references | 2 × 10,000 rows |
| double-measurement references | 2 × 10,000 rows |

For every qubit in every circuit, hard and soft arrays have identical shapes
and share the repetition index. Qubit 50 has exactly one extra measurement
beyond the QEC-round sequence. That column is the later response described
by the paper.

This is a genuinely joined multi-time physical packet, not a fitted
instrument or histogram.

## 3. Conditional branch and later response

Let:

- \(X_{\rm pre}\) be qubit 50's last QEC measurement;
- \(A=\mathbf1[DASR=1]\) be the documented conditional-\(X\) branch; and
- \(Y\) be the extra, later qubit-50 measurement.

The source-defined no-refit response relation is

\[
\widehat Y=X_{\rm pre}\oplus A.
\]

The observed matches are:

| rounds | matches / 1,000 |
|---:|---:|
| 2 | 746 |
| 3 | 718 |
| 4 | 703 |
| 5 | 626 |
| 6 | 617 |
| 7 | 631 |
| 8 | 583 |
| 9 | 599 |

These rates do not estimate an ideal gate fidelity. They combine the
pre-measurement, decoder branch, conditional operation, fixed delay,
relaxation, and final measurement. Their value for DU is more basic: the
retained record is visibly upstream of a physically implemented branch and a
later physical response.

## 4. Repeated-history compatibility

Define a returned hard-history key by concatenating every classified QEC
measurement in one row while excluding only the extra post-feedback qubit-50
response.

Across all circuits:

- 176 hard-history keys repeat;
- those keys cover 389 rows; and
- no repeated key carries conflicting `DASR` values.

This is a positive compatibility control for factorization of the observed
FPGA decision through the retained hard history.

It is not a proof of global decoder factorization. Most high-round histories
occur only once, the physical decoder firmware/configuration is not stored,
and an unobserved controller state could agree on all repeated keys while
differing elsewhere.

## 5. Where implementation completeness fails

### 5.1 Returned rows are not an attempted-process census

The Zenodo description says each row is a separate repetition of the
experiment. The HDF5 schema contains no:

- pre-return trigger count;
- accepted/rejected selector;
- rejected response stratum;
- retry lineage; or
- controller-level attempt identifier.

Therefore the packet identifies a returned-shot kernel:

\[
P(M,D,T,Y\mid S=1),
\]

where \(M\) is the measurement history, \(D\) the decoder state, \(T\) the
timing, \(Y\) the later response, and \(S=1\) means the row was retained.

It does not identify the unconditional attempted process
\(P(M,D,T,Y,S)\). Knowing that 8,000 rows were returned does not determine
what, if anything, happened in an unrecorded \(S=0\) stratum.

This is the acquisition-visibility factorization boundary instantiated on a
real laboratory packet.

### 5.2 The action is documented but not implementation-complete

The paper specifies the conditional \(X\), and the HDF5 stores:

- the conditional qubit;
- `DASR`;
- the later qubit measurement; and
- Stim representations of the stability circuit.

But the main circuit groups do not retain the physical Quil/pulse program.
They also omit the decoder bitstream or firmware/configuration, message-route
state, sequencer memory, and a per-row applied-action register.

The branch is source-grounded and empirically visible. Its complete physical
implementation is not archived.

### 5.3 “Soft measurement” is not full waveform lineage

Each soft event is one complex in-phase/quadrature value. The arrays preserve
event-level integrated readouts and align them with the hard classifications.
They do not contain a within-measurement time-series waveform, receiver
buffers, threshold configuration, or classifier firmware.

Calling them “raw readout signals,” as the paper does in its operational
context, must not be cast as complete analog acquisition lineage.

### 5.4 Reset and archive semantics remain typed

`use_resets=False` is retained for every circuit, and the paper states that
resets were unavailable. That clearly answers whether the QEC sequence used
active qubit resets.

It does not answer:

- whether controller memory was blank between rows;
- what buffers were overwritten or retained;
- whether every attempted row reached the HDF5 writer;
- what route state persisted; or
- what environmental support carried residual correlations.

Qubit reset, controller reset, archive reset, and complete causal break remain
different objects.

## 6. What this changes in Dynamic Unity

Before this audit, DU's strongest open packets were either:

- aggregate provider returns;
- joined categorical counts;
- formed voltage traces without complete provenance; or
- fitted reduced instruments.

This packet advances the empirical frontier. It supplies a real,
source-pinned, multi-time chain:

```text
formed readout events
 -> hard and soft retained records
 -> FPGA decoder certificate
 -> conditional physical branch
 -> later physical response
```

The packet therefore satisfies the **returned-shot joined multi-time** part
of the reopener.

It does not satisfy:

```text
all physical attempts
 -> complete controller implementation
 -> complete archive/provenance/reset semantics
 -> declared hidden-environment scope.
```

Material reconstruction remains parked. A future bounded analysis may use
this packet to test returned-shot prediction and first-leak questions, but no
such result can be promoted to an all-attempt physical remainder without the
missing selector and implementation fields.

## 7. Absorption and novelty

The experiment is standard real-time QEC and classical feedback. Joined
measurement/decoder/response analysis is standard process identification.
Selection-bias and missing-attempt boundaries are standard missing-data and
provenance concerns.

Dynamic Unity's earned contribution is the typed packet audit:

- it recognizes a stronger physical record rather than dismissing it because
  it is incomplete;
- it identifies precisely which North-Star rung it clears; and
- it prevents returned-shot completeness from being promoted to
  implementation completeness.

That is a scoped Grade-4 interface boundary, not new physics.

## 8. Exact next reopener

The minimum completing sidecar would add:

1. a monotonically assigned identifier for every controller trigger before
   selection;
2. disposition for every trigger: executed, rejected, retried, aborted, or
   returned;
3. the exact physical control program and decoder firmware/configuration;
4. per-row applied-action and route/controller-state lineage;
5. waveform or receiver-buffer lineage sufficient to audit the classifier;
6. archive retention, overwrite, access, and reset semantics; and
7. the declared environment and persistence boundary.

No external hardware is needed to state that contract. Hardware or an author
collaboration would be required only to produce a sidecar if none already
exists.

## Reproducibility

After downloading the frozen 5.6 MB source file, run:

```bash
uv run --with h5py python tests/du_rigetti_fast_feedback_packet_audit.py \
  --source /path/to/fast_feedback_raw_data.h5 \
  --write-artifact
```
