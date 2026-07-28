---
title: "Causal-priority intervention ladder and unchanged process transfer"
status: completed_scoped_necessity_and_minimality_result
doc_type: exact_intervention_ladder_quantum_distributed_transfer_and_ontology_boundary
created: 2026-07-28
claim_id: HC-DU-073
work_id: CAUSAL-PRIORITY-INTERVENTION-LADDER
program_id: CCR-CAUSAL-PRIORITY-INTERVENTION-LADDER
run_id: RUN-20260728-092501-causal-priority-intervention-ladder
claim_grade: "SCOPED GRADE-4 TERMINAL-NONORIENTATION, TWO-INTERVENTION CAUSAL-PRIORITY MINIMALITY, QUANTUM/DISTRIBUTED PROCESS TRANSFER, AND ONTOLOGY BOUNDARY / STRUCTURAL CAUSAL MODELS, INTERVENTION CALCULUS, QUANTUM CAUSAL MODELS, CAUSAL TOMOGRAPHY, PROCESS TENSORS, AND EXISTING DU COMPONENTS ABSORBED / NO ONTOLOGICAL PRIORITY, PHYSICAL INTERFACE SELECTION, NEW CAUSAL OR QUANTUM LAW, GRADE-5 REMAINDER, PREDICTION, PAPER, MODEL, OR HARDWARE RESULT"
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Causal-priority intervention ladder

## Executive result

`HC-DU-072` established that terminal physical-operational and record
presentations can contain exactly the same decision information without
settling which is ontologically prior. The next question was whether one
intervention can orient the formation relation.

In the smallest frozen three-model arena, it cannot.

Let \(P\) be a physical-source variable, \(R\) a record variable, and
\(U\) a hidden uniform root. Compare:

```text
M_PR: U -> P -> R
M_RP: U -> R -> P
M_CC: U -> P and U -> R.
```

All three have the same passive endpoint law:

\[
P=R=U.
\]

One surgical intervention on \(P\) distinguishes \(P\to R\), but leaves
\(R\to P\) observationally identical to the common-cause model. One
surgical intervention on \(R\) gives the converse. Both independently
addressed interventions are necessary and sufficient to distinguish the
three models in this declared class.

The result transfers unchanged to:

- two opposite CNOT formation circuits and a Bell-pair replacement channel
  with the same terminal Bell state; and
- source-write, certificate-driven actuation, and common-source distributed
  histories with the same authenticated endpoint.

The important research consequence is not a new causal-discovery theorem.
Structural causal models and quantum causal-process theory absorb the
mathematics. Dynamic Unity gains a sharper physical reopener:

```text
terminal equality or operational duality
    does not orient formation

one one-sided intervention
    does not exclude a common source

two independently realizable, pre-formation arrow-breaking interventions
    can identify the local process direction in the frozen model class

identified process direction
    still does not establish ontological substrate priority.
```

No current physical arena supplies this complete intervention and acquisition
contract without importing the source/record boundary under test. No
scientific successor is activated.

## 1. Frozen classical contract

Let:

\[
U\sim\operatorname{Bernoulli}(1/2),
\qquad
P,R\in\{0,1\}.
\]

The three deterministic structural models are:

\[
\begin{aligned}
M_{PR}:&\quad P:=U,\quad R:=P,\\
M_{RP}:&\quad R:=U,\quad P:=R,\\
M_{CC}:&\quad P:=U,\quad R:=U.
\end{aligned}
\]

The admitted operations are:

1. passive endpoint observation;
2. `do(P=0)` followed by readout of \(R\);
3. `do(R=0)` followed by readout of \(P\); and
4. `do(P=0,R=0)` as a negative control.

The words `do(P=0)` and `do(R=0)` denote surgical replacement of one
structural assignment while leaving the others unchanged. A semantic rename,
post-formation overwrite, selective deletion, or correlated joint setting is
not this intervention.

## 2. Terminal nonorientation

### Proposition 1

Every passive endpoint statistic and every deterministic or stochastic
postprocessing of that endpoint has the same law in all three models.

### Proof

For every \(u\in\{0,1\}\), all three models return

\[
(P,R)=(u,u).
\]

Since \(U\) is uniform, their common endpoint law is

\[
\Pr(P=0,R=0)=\Pr(P=1,R=1)=1/2.
\]

Equal input laws remain equal under every common Markov kernel. Therefore
more terminal samples, terminal tomography, signatures, hashes, or other
endpoint-only postprocessing cannot orient the formation relation.
\(\square\)

The same conclusion holds under the diagonal intervention
`do(P=0,R=0)`: all three models return the forced pair \((0,0)\). Breaking
both candidate arrows at once removes the very response needed to orient
either arrow.

## 3. One-sided interventions and their ambiguity

Under `do(P=0)`:

| Model | Readout law for \(R\) |
|---|---|
| \(M_{PR}\) | \(R=0\) with probability 1 |
| \(M_{RP}\) | \(R=U\), uniform |
| \(M_{CC}\) | \(R=U\), uniform |

Thus `do(P=0)` distinguishes \(P\to R\), with total-variation distance
\(1/2\) from either rival, but it cannot distinguish \(R\to P\) from a
common source.

Under `do(R=0)`:

| Model | Readout law for \(P\) |
|---|---|
| \(M_{PR}\) | \(P=U\), uniform |
| \(M_{RP}\) | \(P=0\) with probability 1 |
| \(M_{CC}\) | \(P=U\), uniform |

This intervention distinguishes \(R\to P\), again at total-variation
distance \(1/2\), while leaving \(P\to R\) confounded with a common source.

The common-cause rival is load-bearing. A two-model comparison of
\(P\to R\) and \(R\to P\) can make one intervention look conclusive only
because it silently excludes the most important third explanation.

## 4. Minimum intervention-cover theorem

### Theorem 2

Within the frozen three-model class and admitted operation set,

\[
\{\operatorname{do}(P=0),\operatorname{do}(R=0)\}
\]

is the unique inclusion-minimal arrow-breaking intervention cover, up to
the chosen forced values.

### Proof

Sufficiency follows from the two response tables: the ordered signatures are

\[
\begin{array}{c|cc}
 & \operatorname{do}(P=0) & \operatorname{do}(R=0)\\
\hline
M_{PR} & \delta_0 & \operatorname{Bernoulli}(1/2)\\
M_{RP} & \operatorname{Bernoulli}(1/2) & \delta_0\\
M_{CC} & \operatorname{Bernoulli}(1/2) &
          \operatorname{Bernoulli}(1/2).
\end{array}
\]

All three rows are distinct.

For necessity, omit `do(P=0)`. Then \(M_{PR}\) and \(M_{CC}\) have the same
remaining passive, record-intervention, and diagonal-intervention laws.
Omit `do(R=0)`. Then \(M_{RP}\) and \(M_{CC}\) have the same remaining laws.
The diagonal operation distinguishes nothing. Hence every separating family
must contain both arrow-breaking interventions.
\(\square\)

This is a model-class-relative minimum, not a universal lower bound on causal
discovery. Larger state spaces, additional time-resolved observations,
nonclassical correlations, different instruments, or stronger structural
assumptions can change the minimum.

## 5. Quantum transfer

Label the two qubits \(S\) and \(A\). Compare:

```text
Q_SA:
  prepare |+>_S |0>_A
  apply CNOT S -> A

Q_AS:
  prepare |0>_S |+>_A
  apply CNOT A -> S

Q_CC:
  discard local inputs
  emit |Phi+> from a common-source replacement channel.
```

All three return:

\[
|\Phi^+\rangle
  = \frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Their complete terminal density matrices are identical. Terminal state
tomography therefore cannot distinguish these three prepared processes.

Now apply \(Z_S\) before formation and measure \(X\otimes X\):

\[
\langle X\otimes X\rangle
=
\begin{cases}
-1 & Q_{SA},\\
+1 & Q_{AS},\\
+1 & Q_{CC}.
\end{cases}
\]

Apply \(Z_A\) before formation:

\[
\langle X\otimes X\rangle
=
\begin{cases}
+1 & Q_{SA},\\
-1 & Q_{AS},\\
+1 & Q_{CC}.
\end{cases}
\]

The two intervention signatures distinguish the processes exactly.

This is deliberately a process-level result. The three models use different
preparation-and-channel histories even though they share one output state.
The result does not say that arbitrary quantum causal structures always
require two interventions. Quantum coherence can sometimes enable causal
inference from observational correlations unavailable classically, and full
quantum causal models type interventions at process inputs and outputs.

## 6. Distributed and cryptographic transfer

Use the same three structural roles:

```text
D_PR: physical source transition -> archive/certificate
D_RP: accepted archive/certificate -> controller actuation
D_CC: common upstream event -> physical state and archive/certificate
```

A deterministic authentication function can preserve the endpoint value and
declared signer relation in all three cases. It cannot determine which causal
formation model generated that value.

To orient the local process, one needs both:

1. a physical source-side perturbation whose propagation to the
   archive/certificate is observable; and
2. a record/controller-side perturbation whose propagation to the physical
   source response is observable.

The source intervention cannot be replaced by signing a different message,
and the record intervention cannot be replaced by changing certificate
semantics. The perturbations must enter the physical process at the declared
ports before the candidate formation relation.

This preserves Dynamic Unity's existing distinctions:

```text
authentication
  != physical source binding
  != controller actuation
  != causal formation direction
  != ontological creation.
```

The transfer is structural, not a claim that consensus protocols create
matter or that quantum records implement a blockchain.

## 7. Literature collision

The components are occupied:

- Pearl's structural intervention calculus defines `do(x)` by replacing a
  structural mechanism and uses the resulting truncated factorization to
  distinguish observation from intervention:
  [Pearl, *An Introduction to Causal Inference*](https://ftp.cs.ucla.edu/pub/stat_ser/r354-corrected-reprint.pdf).
- Quantum causal models make localized interventions and the complete quantum
  process—not one endpoint state—the relevant causal object:
  [Costa and Shrapnel, *Quantum Causal Modelling*](https://arxiv.org/abs/1512.07106)
  and
  [Barrett, Lorenz, and Oreshkov, *Quantum Causal Models*](https://arxiv.org/abs/1906.10726).
- Quantum common-cause compatibility has its own channel factorization
  conditions:
  [Allen et al., *Quantum Common Causes and Quantum Causal Models*](https://arxiv.org/abs/1609.09487).
- Multi-time process tensors reconstruct operational quantum processes from
  interventions rather than endpoint maps:
  [Pollock et al., *Non-Markovian Quantum Processes: Complete Framework and
  Efficient Characterisation*](https://arxiv.org/abs/1512.00589).
- Quantum causal tomography can sometimes distinguish direct cause from
  common cause with observational quantum correlations, so the present
  two-intervention minimum must remain fixture-relative:
  [Ried et al., *Inferring Causal Structure: A Quantum
  Advantage*](https://arxiv.org/abs/1406.5036).

Therefore:

- endpoint nonorientation in the equal-law fixture is elementary;
- surgical intervention and common-cause discrimination are known causal
  modeling;
- the quantum circuit is a controlled process-tomography specimen, not a new
  quantum result; and
- the DU advance is a typed minimum reopener connecting operational duality,
  formation, cryptographic provenance, physical intervention, and ontology
  without conflating them.

The maximum grade is scoped Grade 4 under Dynamic Unity's selection/necessity
scale. There is no new causal theorem, quantum law, distributed-systems law,
or physical prediction.

## 8. What the causal arrow earns

If the two interventions are physically realizable and their complete
response laws match one model, the experiment earns:

> Within the frozen model class, port definitions, intervention semantics,
> and acquisition boundary, this variable is causally upstream of the other.

It does not earn:

- that the upstream variable is metaphysically fundamental;
- that the downstream variable is unreal or merely cognitive;
- that one presentation is the substrate of every observer;
- that the source/record partition was selected by the dynamics;
- that the common-cause class is complete outside the frozen alternatives;
  or
- that the same direction holds under an enlarged action envelope.

Ontological priority could remain underidentified even after a local causal
arrow is identified. Causal order is a relation inside a typed process;
substrate priority is a stronger explanatory claim about why that process,
its variables, and its intervention ports are physically privileged.

## 9. North-Star consequence and disposition

The previous physical reopener—“find an enlarged action that breaks
operational duality”—was necessary but underspecified. A one-sided first leak
can still leave a direct-cause model confounded with a common-source model.

The corrected reopener is:

> Supply a frozen physical process with independently selected source and
> record ports, two realizable pre-formation arrow-breaking intervention
> families, complete attempted-process acquisition, and a common-cause rival.
> Identify the response family without interface, source, target, resource,
> or acquisition refit.

This does not activate the IBM returned-shot packet: accepted or returned
shots do not establish complete acquisition, and its pointer/environment
roles are engineered. It does not activate infrared memory: the detector,
access algebra, and record boundary remain supplied. It does not activate a
distributed analogy: changing a certificate is not necessarily a physical
intervention on a field or source.

The work therefore returns:

```text
CAUSAL_PRIORITY_LADDER_EARNED
PHYSICAL_REOPENER_SHARPENED
NO_READY_SCIENTIFIC_SUCCESSOR
```

## 10. Executable certificate

[`tests/du_causal_priority_intervention_probe.py`](../tests/du_causal_priority_intervention_probe.py)
checks:

1. common passive endpoint laws;
2. failure of passive and diagonal operations;
3. the two one-intervention confounded pairs;
4. exact total-variation margins;
5. exhaustive minimum-cover size over the declared intervention set;
6. authentication nonorientation;
7. equality of the three terminal Bell density matrices; and
8. exact two-intervention \(X\otimes X\) quantum signatures.

Result:

```text
12 / 12 checks passed
classical minimum intervention count: 2
classical separation margin: 1/2
external hardware: none
physical model: none claimed
```

Artifact:
[`tests/artifacts/du_causal_priority_intervention_result.json`](../tests/artifacts/du_causal_priority_intervention_result.json).
