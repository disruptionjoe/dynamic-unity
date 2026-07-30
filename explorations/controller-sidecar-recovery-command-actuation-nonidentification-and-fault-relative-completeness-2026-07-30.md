---
title: "Controller-sidecar recovery, command/actuation nonidentification, and fault-relative implementation completeness"
status: banked_scoped_result
doc_type: exploration_result
created: 2026-07-30
claim_id: HC-DU-170
run_id: RUN-20260730-153100-controller-sidecar-recovery-audit
evidence_grade: 4
---

# Implementation completeness is target- and fault-class relative

## Executive result

The arXiv source bundle for the Riverlane/Rigetti experiment materially
improves `HC-DU-168`'s controller description.

The supplementary information specifies:

- the high-level controller program and instruction ordering;
- decoder initialization categories;
- measurement buffering and reordering;
- packet formation and WISHBONE communication;
- decoder-status polling;
- the conditional-\(X\)/matched-idle branch;
- the star-network controller route and clock crossings; and
- an aggregate physical end-to-end timing check using the qubit's \(T_1\).

Therefore the public record does **not** merely contain an unexplained decoder
label and response. The descriptive controller workflow and route
architecture are source-specified.

But the bundle contains no exact pyQuil, assembly listing, compiled binary,
waveform program, FPGA firmware, complete configuration values, per-attempt
controller log, actuation acknowledgement, trigger/disposition census,
archive policy, or environment scope. The workflow is reproducibly described;
the realized implementation lineage is not reproduced.

The correction is:

```text
descriptive workflow and route architecture       recovered
exact executable/configuration identity           absent
intended per-result command semantics              recovered
per-attempt command/route/actuation lineage        absent
aggregate end-to-end actuation evidence            partial
all-attempt/archive/environment completeness       absent
```

The deeper result is a repair to Dynamic Unity's reopener:

> Implementation completeness is not maximal telemetry. It is target- and
> fault-class-relative constancy on the implementation fibre.

Full waveform lineage is necessary only when the admitted target or fault
class can vary while all coarser fields agree. Irrelevant telemetry should
not be demanded merely because it exists.

Disposition:

```text
DESCRIPTIVE_CONTROLLER_SIDECAR_RECOVERED
+ PRIOR_MISSING_PROGRAM_CLAIM_NARROWED
+ EXECUTABLE_AND_CONFIGURATION_SIDECAR_ABSENT
+ AGGREGATE_ACTUATION_EVIDENCE_ONLY
+ PER_ATTEMPT_ACTUATION_NONIDENTIFICATION
+ FAULT_RELATIVE_COMPLETENESS_RULE
+ REOPENER_NARROWED_NOT_SATISFIED
+ NO_READY_SUCCESSOR
```

This is a scoped Grade-4 source and necessity boundary. It is not evidence
of a lost pulse, laboratory defect, physical remainder, new law, ontology,
or new physics.

## 1. Frozen sources

The empirical source remains the 5.6 MB
`fast_feedback_raw_data.h5` packet:

```text
MD5     3b2503a80f2b92916660489e2f07e880
SHA256  dd2a3d48e86ea81094b44439fb58a3d9788757e26799bd4ee7497eb94798ed08
```

The new audit source is the arXiv v1 TeX bundle for the
[primary paper](https://arxiv.org/abs/2410.05202):

```text
MD5     c540a68e31307224b1ed2370cbfe0e00
SHA256  25f66da6b24385f5456da6c8fd078e597e4d3993b00bf1eb0d7759c55588d8f6
```

Its complete member classes are:

```text
main.tex
supplement.tex
two bibliography files
eleven PDF figures
```

It contains no executable, configuration, data, or log member. The raw
source bundle and HDF5 remain external; hashes, the compact audit, and the
derived boundary are durable.

The [Zenodo record](https://zenodo.org/records/15364358) remains the
authoritative data description.

## 2. What the supplementary source recovers

### 2.1 Program workflow

The source says proprietary assembly instructions are interleaved with the
stability experiment. Its ordered workflow is:

1. initialize decoder features and configuration categories, including round
   count and logical-observable definition;
2. execute the QEC gates and measurements;
3. buffer the latest measurement outcomes in decoder-sequencer memory;
4. collect and format them as 32-bit strings and write them to the decoder;
5. start Collision Clustering and poll the status register until completion;
6. read the Boolean logical result; and
7. apply \(X\) if the result is one, otherwise idle for the same gate
   duration, then measure.

This closes the **descriptive workflow** rung.

It does not supply the exact instruction stream, configuration values, binary
loaded on each sequencer, or firmware state used for each returned row.

### 2.2 Route architecture

The source specifies:

- a 32-bit WISHBONE interface;
- gate-drive sequencer access to decoder addresses and status ports;
- a hub-and-single-hop star network across chassis;
- the decoder on the hub gate-drive sequencer;
- a 250 MHz sequencer clock;
- a 156.25 MHz decoder clock; and
- explicit clock-crossing logic.

The earlier phrase “controller route absent” was too broad. The route
**architecture** is public. Per-attempt route state, message identity,
buffer/stack contents, stale-state controls, and command acknowledgements are
not.

### 2.3 Physical actuation evidence

The source does more than assert an intended \(X\):

- returned rows join decoder result to a later qubit response;
- the supplement checks the expected \(M_1/M_2\) relationship by logical
  result; and
- a separate \(T_1\)-based analysis uses the qubit as an end-to-end physical
  clock and agrees with controller-clock timing in aggregate.

That is real aggregate evidence that the feedback path physically operated.
It is not a per-attempt certificate that one declared pulse was delivered on
one returned row.

## 3. Exact source audit

| Interface level | Public status | What is and is not earned |
|---|---|---|
| Logical circuit, qubits, measurement order | `SOURCE_SPECIFIED` | HDF5 Stim circuit, mapping, arrays, and attributes |
| Controller workflow | `SOURCE_SPECIFIED` | Ordered operations and intended branch |
| Route architecture | `SOURCE_SPECIFIED` | Hub, WISHBONE, sequencer, ports, clocks |
| Decoder algorithm class | `PARTIALLY_SPECIFIED` | Collision Clustering and unweighted graph; not exact firmware/configuration |
| Exact executable identity | `ABSENT` | No pyQuil, assembly, binary, waveform program, firmware image, or digest |
| Intended command semantics | `SOURCE_SPECIFIED` | \(L=1\to X\), otherwise matched idle |
| Per-attempt command/route lineage | `ABSENT` | No issued-command identifier, message route, or controller-state log |
| Aggregate physical actuation check | `PARTIALLY_SPECIFIED` | Joined response and \(T_1\) end-to-end check |
| Per-attempt actuation acknowledgement | `ABSENT` | No pulse-delivery or physical-effect certificate per row |
| Returned-row join | `SOURCE_SPECIFIED` | Measurements, decoder registers, timing, response |
| All-attempt disposition census | `ABSENT` | No trigger IDs, rejects, retries, aborts, or dispositions |
| Acquisition lineage | `PARTIALLY_SPECIFIED` | Integrated I/Q per event; no pre-integration waveform/buffer lineage |
| Archive semantics | `ABSENT` | No write, retention, overwrite, access, or controller-reset contract |
| Environment/persistence scope | `ABSENT` | No declared exhaustive memory/environment boundary |

`ABSENT` means absent from the public packet. It says nothing about what the
laboratory retained privately.

## 4. Command is not actuation

Let:

- \(M_1\) be the retained pre-feedback measurement;
- \(L=1\) be the logical result;
- \(C=X\) be the program's intended command;
- \(S\) be the unobserved physical post-\(M_1\) state;
- \(U\) indicate whether the physical \(X\) was delivered; and
- \(Y\) be the retained later response.

The source itself measures a nontrivial conditional distribution
\(P(S\mid M_1)\). Therefore \(M_1\) does not identify \(S\) per attempt.

Consider:

| implementation | \(M_1\) | \(L\) | command | hidden \(S\) | \(U\) | \(Y\) |
|---|---:|---:|---|---:|---:|---:|
| delivered | 0 | 1 | \(X\) | 0 | 1 | 1 |
| lost/compensated | 0 | 1 | \(X\) | 1 | 0 | 1 |

The second row is an admitted latent-fault countermodel, not a laboratory
claim. Both implementations have the same returned command/response tuple,
but physical actuation differs.

Thus:

\[
(\text{reported pre-state},\text{logical result},
\text{intended command},\text{returned response})
\not\Rightarrow
\text{per-attempt physical actuation identity}.
\]

Calibration constrains the probability of such latent alternatives. It does
not assign one hidden postmeasurement state or pulse-delivery history to each
row.

## 5. Fault-relative implementation completeness

Let:

- \(\mathcal I\) be a declared class of physical implementations, including
  admitted faults and environments;
- \(p:\mathcal I\to P\) be the retained implementation packet; and
- \(T:\mathcal I\to\mathcal P(Y)\) be the target law.

### Criterion

The packet is implementation-complete for \(T\) relative to
\(\mathcal I\) exactly when

\[
p(i)=p(i')
\Longrightarrow
T(i)=T(i')
\qquad
(i,i'\in\mathcal I).
\]

Equivalently, \(T\) factors through \(p\).

This is the same fibre criterion used throughout Dynamic Unity, now applied
to implementations rather than physical histories.

### Consequences

1. **Completeness is target-relative.** A packet complete for the binary
   response can be incomplete for actuation provenance, latency, or archive
   identity.
2. **Completeness is fault-class-relative.** If lost pulses, stale buffers,
   unobserved retries, or hidden postmeasurement states are excluded by
   premise, the required packet changes. They cannot be excluded silently.
3. **Maximal telemetry is unnecessary.** A waveform is required only if two
   admitted waveform histories share every coarser packet field yet change
   the target.
4. **No finite packet is absolutely complete against an undeclared,
   arbitrarily extensible environment.** The environment and persistence
   scope must be frozen.
5. **Threat-model expansion is completion enlargement.** Adding a new fault
   mode after seeing the result changes \(\mathcal I\); it is not record
   refinement.

The mathematics is ordinary identifiability and sufficient-statistic
factorization. The Dynamic Unity gain is an attainable physical contract
rather than an unbounded demand for every hidden variable.

## 6. Corrected reopener

The current packet has earned:

```text
returned-shot multi-time join
+ descriptive controller workflow
+ route architecture
+ intended branch semantics
+ aggregate physical feedback evidence.
```

The next packet does **not** need every imaginable field. It must instead
freeze the target and fault/environment class, then make that target constant
on the remaining implementation fibre.

For the current flagship questions, the minimum likely includes:

1. an all-trigger attempt identifier and every disposition;
2. exact executable/configuration identity or an equivalent no-refit digest;
3. target-sufficient per-attempt command/route/actuation evidence under the
   declared fault class;
4. archive write, lineage, retention, overwrite, access, and reset semantics;
5. a declared controller/environment/persistence scope; and
6. material factorization and behavioral-minimality tests.

Waveform lineage is conditional: require it only if the target or admitted
faults can vary inside the integrated-I/Q fibre.

The public source does not satisfy this corrected reopener. The flagship
remains parked and no successor is ready.

## 7. Absorption and scientific status

The components are absorbed by:

- system identification and latent-variable nonidentification;
- event sourcing and database provenance;
- control-system command/acknowledgement semantics;
- experimental reproducibility passports;
- fault-tree and adversarial threat modeling; and
- sufficient-statistic factorization.

The result corrects and narrows Dynamic Unity's empirical gate. It does not
claim a new general theorem, a faulty experiment, a physical remainder, or
physics beyond standard quantum mechanics.

## Reproducibility

Run:

```bash
python3 tests/du_controller_sidecar_recovery_audit.py \
  --source /path/to/arxiv-2410.05202-v1-source.tar \
  --write-artifact
```

The 17 checks pin the source hashes, member inventory, positive workflow
markers, absence of executable/data members, and command/actuation twin.
