---
title: "Sequential-readout formed trace, complete-packet, and provenance boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-162
run_id: RUN-20260730-115843-sequential-readout-complete-packet
work_id: MPA-04-COMPLETE-PHYSICAL-RECORD-PACKET
action_id: MPA-04-COMPLETE-PHYSICAL-RECORD-PACKET
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Sequential-readout formed trace and complete-packet boundary

## Executive return

```text
RAW_TRACE_FORMATION
+ CALIBRATION_CONDITIONAL_ONE_RUN_OUTCOME
+ PARTIAL_PHYSICAL_TYPING
+ PROVENANCE_NONIDENTIFICATION
+ ARCHIVE_POLICY_NONSELECTION
+ RESET_LAYER_SPLIT
+ NO_OUTCOME_CONDITIONED_PHYSICAL_ACTION
+ KNOWN_RESULT_ABSORPTION
```

Swing 4 returns a mixed result on the same platform used by `HC-DU-161`.

The important positive is physical:

> Peronnin et al.'s apparatus forms a real one-run detector trace. A prepared
> microwave probe interacts with the qubit, is released into a transmission
> line, amplified, down-converted, and digitized as \(V(t)\). A calibrated
> functional gives one complex amplitude \(\beta\), and a calibrated decision
> region gives one operational binary result.

This is substantially more than a formal instrument or ensemble-only pointer.
The physical chain implements a blank-to-written transition at the digitizer
and supplies one accessible result for each admitted run.

The complete-packet claim nevertheless fails:

> The source does not select one retained, provenance-complete, reset-defined
> archive with a held-out outcome-conditioned physical action. The raw trace,
> compressed amplitude, binary label, residual-population assay, QND test,
> and summary histograms live at different information and calibration
> layers.

The failure is not a claim that the platform could never implement such a
packet. It is a source-contract result: the published apparatus and reported
statistics do not determine it.

Primary source:
[Peronnin, Marković, Ficheux, and Huard, “Sequential dispersive
measurement of a superconducting qubit”](https://arxiv.org/abs/1904.04635),
*Physical Review Letters* 124, 180502 (2020).

## 1. The source-pinned physical chain

The source separates the basic measurement process into:

1. deterministic preparation of a coherent readout-resonator probe;
2. dispersive interaction with the transmon for a chosen time;
3. pump-controlled conversion from the readout mode into a lossy buffer and
   transmission line;
4. traveling-wave and conventional amplification;
5. down-conversion and digitization of a voltage trace \(V(t)\);
6. linear demodulation to one complex amplitude; and
7. binary classification as ground or excited.

For one run, the recorded statistic is

\[
\beta_w(V)=\int V(t)w(t)\,dt.
\tag{1}
\]

The binary output is

\[
z_{w,Z_g}(V)
=
\begin{cases}
g,&\beta_w(V)\in Z_g,\\
e,&\beta_w(V)\notin Z_g,
\end{cases}
\tag{2}
\]

where

\[
Z_g=\{\beta:P_g(\beta)>P_e(\beta)\}.
\tag{3}
\]

These maps have different physical status.

- \(V(t)\) is a physically formed detector trace.
- \(\beta\) is a calibrated projection of that trace.
- \(z\) is a decision relative to a calibrated classification task.

The paper constructs \(w\) from state-labelled average voltage traces and
sets its normalization using a declared preparation. It constructs \(Z_g\)
from the measured state-conditioned densities \(P_g\) and \(P_e\).
Consequently, the physical detector chain realizes the trace, while the
particular statistic and label remain calibration- and task-conditioned.

That does not make the label unreal. It means the label is not a
target-blind interface selected by the source Hamiltonian alone.

## 2. Seven-field packet audit

`SEED-DU-MPA-15` requires the seven fields to travel together.

| packet field | source disposition | reason |
|---|---|---|
| blank-to-written formation | **physically realized** | one run produces an amplified, down-converted, digitized voltage trace |
| one-run outcome | **realized conditional on calibration** | \(\beta\) and the \(g/e\) label are computed for each realization using \(w\) and \(Z_g\) |
| retained archive | **used but not selected** | recorded traces and \(10^5\)-run distributions require operational retention, but no retention horizon, storage state, overwrite rule, or minimum archive is specified |
| causal provenance | **partial sequence, not identified** | the pulse schedule orders preparation, interaction, release, and readout, but the retained trial/control join is not specified and the binary label cannot identify its preparation history |
| observer access | **physically realized, boundary supplied** | the amplifier, mixer, digitizer, demodulator, and analysis path provide access; the chosen port, weight, decision region, and analyst/controller boundary are supplied |
| reset | **approximate probe reset only** | reported release efficiency is \(91\%\), consecutive-readout agreement is \(95\%\), and no archive-memory reset semantics are given |
| held-out action | **absent as physical feedback** | the source uses the first result for heralded analysis of a second readout, not to control a later physical operation |

The conjunction therefore returns:

```text
PARTIAL_PHYSICAL_TYPING
not COMPLETE_RECORD_PACKET
```

## 3. Exact calibrated-projection boundary

Let the digitized trace live in a real vector space \(\mathcal V\), and let
\(\ell_w:\mathcal V\rightarrow\mathbb C\) denote (1).

### Proposition 1 — statistic compression

If

\[
\delta V\in\ker\ell_w,
\qquad
\delta V\ne0,
\]

then

\[
\beta_w(V+\delta V)=\beta_w(V)
\]

and therefore

\[
z_{w,Z_g}(V+\delta V)=z_{w,Z_g}(V).
\]

Thus neither \(\beta\) nor the binary label retains the complete detector
waveform. The exact finite control uses

\[
w=(1,2,-1,0),
\quad
V=(1,0,0,0),
\quad
\delta V=(2,-1,0,3),
\]

for which

\[
w\mathbin{\cdot}\delta V=0.
\]

The two distinct traces have the same \(\beta=1\) and the same label.

This is ordinary linear compression, not a quantum novelty. Its relevance is
typed: a statistic sufficient for qubit classification need not preserve
waveform, channel, or occurrence provenance.

### Proposition 2 — the binary label is not source provenance

The source reports

\[
P(z=g\mid\text{prepared }e)=0.034
\]

and

\[
P(z=e\mid\text{prepared }g)=0.016.
\]

Hence both declared preparations have positive probability of producing the
same binary label. This incorporates preparation errors, thermal population,
qubit decay, and histogram overlap. It follows exactly that

\[
z\not\mapsto\text{unique preparation history}.
\]

The result is not “measurement failed.” The reported average fidelity remains
\(97.5\%\). The result is that a high-fidelity operational outcome is not a
provenance certificate.

## 4. Archive-policy nonselection

The front-end detector and the published summary statistics are compatible
with at least two downstream acquisition completions.

### Full-lineage completion

Retain

```text
trial identifier
+ preparation/control schedule
+ raw V(t)
+ beta
+ binary label
+ repeat-readout result
```

through a declared horizon.

### Streaming-summary completion

For each run:

1. compute \(\beta\), label, histogram count, and repeat-agreement counter;
2. update the aggregate;
3. discard the raw trace, trial identifier, and per-run join.

The two completions can return the same:

- state-conditioned \(\beta\) histograms;
- binary error rates;
- average fidelity;
- repeat-readout agreement; and
- plotted aggregate traces.

They differ in what later interventions can recover. The full completion can
audit one trial's controls and waveform. The streaming completion cannot.

### Proposition 3 — reported-summary archive nonselection

Let \(s\) be the map from a trial stream to the source's declared aggregate
statistics, and let \(\xi\) be the retained archive/lineage architecture.
The two completions above satisfy

\[
s(m_{\rm full})=s(m_{\rm stream}),
\qquad
\xi(m_{\rm full})\ne\xi(m_{\rm stream}).
\]

Therefore

\[
\ker s\not\subseteq\ker\xi.
\]

The reported front-end and summaries do not select the complete retained
archive. This is an exact completion twin, not a claim about which
implementation the laboratory actually used.

It also resolves the erase/rewrite control. A pipeline may retain the
original \(V(t)\), overwrite it after computing \(\beta\), or later reproduce
the same \(\beta\) from a distinct trace in the kernel twin. The compressed
record contains no tag that distinguishes those histories.

## 5. Reset is layered

The source reports:

- \(91\%\) release efficiency for the chosen operating point;
- rapid on-demand emptying of the high-\(Q\) readout mode;
- \(95\%\) probability that two consecutive readouts give the same outcome
  after heralding on the first; and
- possible dissipation into unmonitored modes for faster flushes.

These statements concern different systems:

```text
readout resonator reset
!= buffer/output evacuation
!= qubit state persistence
!= detector readiness
!= fresh archive capacity
!= deletion of the previous record
```

A \(91\%\) release efficiency is not an exact blank state. A \(95\%\)
repeat-agreement probability is not exact QND persistence. Neither defines
how digitizer memory becomes fresh or how an old trial remains addressable
after the next one.

### Proposition 4 — reset nonimplication

No map from “readout mode sufficiently emptied for another pulse” to
“previous material record retained with lineage and new memory blank” is
specified. Probe reset and archive reset are therefore independent packet
fields on the source contract.

This does not deny that ordinary laboratory control electronics perform
memory allocation and storage. It prevents those operations from being
credited to the qubit–resonator–JRM dynamics without being typed.

## 6. Access and held-out action

The source has a real access channel: the released field is amplified,
down-converted, digitized, and analyzed. Access is therefore physically
realized relative to the supplied output port and electronics.

The QND check goes further. The first binary result is used to herald a subset
of trials, and a second readout begins \(220\) ns later. The source reports
\(95\%\) same-outcome probability on that conditioned subset. This is a
record-conditioned held-out **response statistic**.

It is not an outcome-conditioned physical action:

- the first result does not choose a later pulse or controller command;
- heralding is an analysis/postselection operation; and
- the second readout protocol is already fixed.

The distinction is experimentally real. Superconducting-qubit feedback
experiments explicitly feed a measurement record into a controller and alter
later dynamics; for a primary comparison see
[Vijay et al., “Quantum feedback control of a superconducting qubit:
Persistent Rabi oscillations”](https://arxiv.org/abs/1205.5591).

Peronnin's platform may support such a future controller. The audited source
does not implement it.

## 7. Strongest absorbers

The component results are mature:

- matched filtering and sufficient-statistic theory absorb the
  \(V\mapsto\beta\) compression;
- statistical decision theory absorbs the calibrated \(g/e\) boundary;
- ordinary single-shot circuit-QED readout absorbs physical trace formation
  and state classification;
- QND measurement theory absorbs consecutive-readout agreement;
- classical data acquisition and database provenance absorb the
  full-versus-streaming archive distinction; and
- measurement-based feedback theory supplies the missing physical action
  architecture.

Dynamic Unity's scoped contribution is the conjunction boundary:

> Formation, single-run classification, archive retention, causal provenance,
> observer access, reset, and action consequence are different interface
> arrows. Demonstrating several does not silently select the rest.

## 8. Campaign disposition

Swing 4 is complete at scoped Grade 4:

```text
RAW_TRACE_FORMATION
+ CALIBRATION_CONDITIONAL_ONE_RUN_OUTCOME
+ PARTIAL_PHYSICAL_TYPING
+ PROVENANCE_NONIDENTIFICATION
+ ARCHIVE_POLICY_NONSELECTION
+ RESET_LAYER_SPLIT
+ NO_OUTCOME_CONDITIONED_PHYSICAL_ACTION
+ KNOWN_RESULT_ABSORPTION
```

Not earned:

- no complete source-selected record packet;
- no claim that the actual laboratory discarded provenance;
- no target-blind binary classifier;
- no exact apparatus or archive reset;
- no feedback capability result;
- no action-relative reconstruction;
- no physical remainder;
- no new quantum law or new physics.

Swing 5 is scientifically eligible only because the campaign explicitly
allows an **explicitly partial** packet. If separately authorized, it must
freeze:

```text
raw trace V(t)
calibrated statistic beta
binary label z
supplied acquisition/retention/access contract
declared action class
```

and derive the coarsest future-response quotient without crediting the partial
archive as complete or target-blind. Swing 5 remains inactive here.

## Reproducibility

The exact compression, archive, lineage, and reset controls are in:

```text
tests/du_sequential_readout_complete_record_packet_probe.py
tests/artifacts/du_sequential_readout_complete_record_packet_result.json
```

Passing proves only those finite logical controls around the source audit. It
establishes no experimental fact, complete physical record, reconstruction,
remainder, new law, or new physics.
