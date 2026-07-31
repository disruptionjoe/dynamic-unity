---
title: "Quantum output carrier, classical shadow, and access relocation"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-075
correction_id: CORR-DU-074-1
run_id: RUN-20260728-111609-quantum-output-record-gate
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260728-111609-quantum-output-record-gate/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-111609-quantum-output-record-gate/run-receipt.md"
owner_repo: dynamic-unity
---

# Quantum output carrier, classical shadow, and access relocation

## Executive result

The gate makes one real correction and one equally important non-promotion.

The correction is:

> Different classical unravellings of one open-system process prove
> classical-shadow plurality. They do not, by themselves, prove that the
> underlying quantum output carrier is physically plural or unselected.

A physically formed quantum output can already be a record before an observer
turns it into a classical readout, provided its carrier, formation history,
retention, bounded access, and action consequences are physically fixed.
Homodyne and counting can then be different downstream questions asked of one
carrier.

The non-promotion is:

> Stinespring uniqueness selects at most an abstract
> complementary-information class. It does not select where that information
> is physically located, retained, accessible, or provenance-bound.

The Gough--Rees Diósi--Penrose construction fixes one Hudson--Parthasarathy
Fock-space output process **inside its chosen model**, then chooses homodyne
or number counting downstream. But the Diósi--Penrose generator does not
independently select that dilation as the physical gravitational carrier, and
the paper explicitly leaves the Universe's detector mechanism and readout
feedback unspecified. It also supplies no bounded physical archive or
observer access contract.

The combined return is:

```text
CARRIER_SHADOW_SEPARATION_EARNED
+ ACCESS_PRESERVING_COMPLEMENT_CRITERION_EARNED
+ CLASSICAL_SHADOW_PLURALITY_ONLY
+ DILATION_REPRESENTATION_ONLY
+ OUTPUT_CARRIER_NOT_RETAINED_OR_ACCESSIBLE
+ CORR-DU-074-1
+ NO_READY_SCIENTIFIC_SUCCESSOR
```

`HC-DU-075` is an exact scoped Grade-4 type theorem and source classification.
The finite positive fixture conditionally admits a physical quantum record
only because its carrier and access are explicitly supplied. The
gravitational source remains representation/conditional-construction grade.
No new quantum theorem, collapse mechanism, gravitational prediction,
physical remainder, ontology, paper, model campaign, or hardware action is
earned.

## 1. The type stack

Let \(A\) be an input system and \(B\) its declared reduced output. A
Stinespring isometry

\[
V:A\longrightarrow B\otimes E
\]

defines:

\[
\Phi(\rho)=\operatorname{Tr}_{E}(V\rho V^\dagger)
\]

and a complementary channel

\[
\Psi(\rho)=\operatorname{Tr}_{B}(V\rho V^\dagger).
\]

Those objects are not yet a complete record.

For Dynamic Unity, a candidate quantum-output record has the passport

\[
\mathcal Q=
\left(
E,\Psi,
\mathfrak A_{\rm acc},
\beta,
\mathcal R,
\mathcal P,
\mathcal M
\right),
\]

where:

- \(E\) is the physical carrier or output factor;
- \(\Psi\) is the source-to-carrier channel;
- \(\mathfrak A_{\rm acc}\subseteq\mathcal B(E)\) is the bounded accessible
  algebra;
- \(\beta\) specifies the blank/input condition;
- \(\mathcal R\) specifies retention and future-readable evolution;
- \(\mathcal P\) specifies source, occurrence, route, and epoch provenance;
  and
- \(\mathcal M\) is the target-independent menu of physically admitted
  observer actions.

For a quantum-to-classical measurement channel

\[
M:\mathcal B(E)\longrightarrow \ell^\infty(Y),
\]

the resulting classical shadow is

\[
R_M=M\circ\Psi.
\]

The independently held-out target \(T\), loss \(L\), and resource budget do
not define \(M\), \(\Psi\), or the carrier.

The relevant stack is therefore:

```text
reduced channel Phi
  -> abstract complementary-information class [Psi]
  -> physical output carrier E and formation channel
  -> retained provenance-bearing accessible quantum record Q
  -> observer action M
  -> classical shadow R_M
  -> target-relative response risk.
```

Each arrow can close while a later arrow remains open.

## 2. Access-preserving equivalence

Minimal Stinespring representations of one channel are equivalent up to an
environment isometry. Conjugate/complementary channels are accordingly unique
only up to partial isometry. This is the standard channel result, not a new DU
theorem; see [Stinespring's original representation
theorem](https://doi.org/10.1090/S0002-9939-1955-0069403-4),
[King et al. on conjugate channels](https://arxiv.org/abs/quant-ph/0509126),
and [Kretschmann, Schlingemann, and Werner on Stinespring
continuity](https://arxiv.org/abs/quant-ph/0605009).

That equivalence is sufficient for claims depending only on the total
complementary information. It is too coarse for a physical record.

Two quantum-record passports \(\mathcal Q_1,\mathcal Q_2\) are
**access-preserving equivalent** only if there is an isometry \(W:E_1\to E_2\)
such that:

1. \(\Psi_2=\operatorname{Ad}_{W}\circ\Psi_1\);
2. \(W\mathfrak A_{{\rm acc},1}W^\dagger=
   \mathfrak A_{{\rm acc},2}\) on the realized support;
3. \(W\) transports the blank/input condition;
4. \(W\) intertwines retained future-readable evolution over the declared
   horizon;
5. \(W\) preserves the typed source/route/epoch provenance; and
6. the admitted action/resource menu transports without adding access.

Plain Stinespring equivalence guarantees only the first item.

### Theorem 1 — quantum carrier / classical shadow separation

Let an antecedent select one passport class \([\mathcal Q]_{\rm acc}\). If
\(M_1,M_2\in\mathcal M\) and

\[
M_1\circ\Psi\not\simeq M_2\circ\Psi,
\]

then the two classical shadows are inequivalent. This does not imply that the
carrier passport is unselected.

**Proof.** Both shadows factor through the same selected \(\Psi\), carrier,
access algebra, retention, and provenance. Their difference lies in the
downstream maps \(M_1,M_2\). Nonconstancy of the composite over an action
index does not imply nonconstancy of the common factor over antecedent
fibres. \(\square\)

This is elementary channel typing. Its value is preventing a false
nonselection inference.

### Theorem 2 — access-relocation obstruction

A reduced channel, even together with the isometry class of its full
complement, does not in general select a record at a fixed observer access
port.

**Witness.** Let \(A\) be one qubit, \(B\) an erased output, \(E\) a fixed
accessible port, and \(H\) a hidden port:

\[
\begin{aligned}
V_{\rm vis}|b\rangle
  &=|0\rangle_B|b\rangle_E|0\rangle_H,\\
V_{\rm hid}|b\rangle
  &=|0\rangle_B|0\rangle_E|b\rangle_H.
\end{aligned}
\]

Both induce the same reduced erasure channel on \(B\). Their full
complements on \(E\otimes H\) are related by `SWAP`. But `SWAP` sends the
fixed accessible algebra

\[
\mathcal B(E)\otimes I_H
\]

to

\[
I_E\otimes\mathcal B(H),
\]

so it is not access-preserving. A uniformly random input bit has decoding
error \(0\) from \(E\) in the visible completion and \(1/2\) in the hidden
completion.

Thus:

```text
same reduced channel
+ isometric full complement
does not imply
same physically accessible record.
```

This is the quantum form of the earlier archive-relocation boundary.

### Corollary — minimum quantum-record admission rule

An abstract complement becomes a physically admitted quantum record only
relative to an antecedent that selects:

1. a physical output carrier/factor and source coupling;
2. a blank-to-written or input-to-output provenance relation;
3. retention over the declared action horizon;
4. a bounded accessible algebra and resource budget; and
5. at least one target-independent action consequence.

A classical pointer value is not required at the formation instant. But
mathematical existence of an environment factor is insufficient.

## 3. Exact finite control: one carrier, two useful shadows

Use the amplitude-damping isometry

\[
\begin{aligned}
V|0\rangle
  &=|0\rangle_B|0\rangle_E,\\
V|1\rangle
  &=\sqrt{1-\gamma}|1\rangle_B|0\rangle_E
    +\sqrt{\gamma}|0\rangle_B|1\rangle_E
\end{aligned}
\]

with \(\gamma=1/4\). The environment output is explicitly declared retained
and accessible. That declaration makes this a conditional positive control,
not an endogenous physical selector.

For phase-opposite inputs \(|+\rangle,|-\rangle\), the environment states are

\[
\rho_E^\pm=
\begin{pmatrix}
7/8 & \pm 1/4\\
\pm 1/4 & 1/8
\end{pmatrix}.
\]

Predeclare:

- the action menu \(\{Z\text{-measurement},X\text{-measurement}\}\); and
- two targets: phase sign \(|+\rangle\) versus \(|-\rangle\), and population
  \(|0\rangle\) versus \(|1\rangle\).

For the phase target:

| Access | Equal-prior error |
|---|---:|
| \(Z\) counting-like shadow | \(1/2\) |
| \(X\) homodyne-like shadow | \(1/4\) |
| full quantum carrier | \(1/4\) |

For the population target:

| Access | Equal-prior error |
|---|---:|
| \(Z\) counting-like shadow | \(3/8\) |
| \(X\) homodyne-like shadow | \(1/2\) |
| full quantum carrier | \(3/8\) |

So neither classical shadow is “the record” for every action. The quantum
carrier supports a capability menu; the observer's later action determines
which classical distinction becomes available. Nothing about this plurality
requires a plural carrier.

The exact certificate is
[`du_quantum_output_record_gate_probe.py`](../tests/du_quantum_output_record_gate_probe.py),
with deterministic
[`artifact`](../tests/artifacts/du_quantum_output_record_gate_result.json).
It passes 12/12 checks.

## 4. Source-pinned gravitational application

Gough and Rees start from the Diósi--Penrose Lindbladian, construct a
Hudson--Parthasarathy Fock-space dilation, define input and output fields, and
then choose continuously monitored output quadratures to derive a quantum
filter. They separately give number counting as another monitoring strategy.
The paper is now published in *Physical Review A* and remains available as
the [primary preprint](https://arxiv.org/abs/2601.17384).

The relevant source facts are:

1. the reduced Diósi--Penrose generator is fixed;
2. a particular Fock-space color space, coupling operators, unitary QSDE, and
   output-field process are constructed;
3. output homodyning defines one commutative filtration and filter;
4. number counting defines another;
5. the authors characterize the filter construction as a first step and do
   not provide a physical mechanism by which the Universe acts as the
   detector or uses the readout to curve spacetime.

The standard trajectory literature already says that one master equation
admits multiple diffusive unravellings interpreted as different
environment-monitoring arrangements; see [Wiseman and
Diósi](https://arxiv.org/abs/quant-ph/0012016). Therefore homodyne/counting
plurality is expected measurement theory.

### Source passport

| Field | Source status | DU classification |
|---|---|---|
| reduced system law | Diósi--Penrose Lindbladian is the starting point | supplied physical candidate |
| dilation | HP Fock-space dilation is constructed | selected as a mathematical/model representation, not derived uniquely from the reduced law |
| quantum output process | input/output field relation is explicit inside that dilation | model-level output process |
| full output algebra | noncommutative Fock output exists in the construction | mathematical carrier class |
| homodyne shadow | output quadrature and commutative filtration are chosen | downstream measurement action |
| counting shadow | output number measurement is separately chosen | downstream measurement action |
| physical detector mechanism | not supplied | first physical admission failure |
| bounded retained archive | not supplied | open |
| observer access/resource boundary | not supplied | open |
| readout-to-spacetime feedback | not supplied | open |
| independent held-out reconstruction target | absent | no North-Star reconstruction claim |

### Exact disposition

Relative to the **reduced generator alone**:

```text
DILATION_REPRESENTATION_ONLY
+ PHYSICAL_QUANTUM_OUTPUT_NONSELECTION.
```

Relative to the **paper's chosen HP model**:

```text
ONE_MODEL_LEVEL_QUANTUM_OUTPUT_PROCESS
+ CLASSICAL_SHADOW_PLURALITY_ONLY
+ OBSERVER_MEASUREMENT_AS_ACTION.
```

Relative to a **physically admitted record**:

```text
OUTPUT_CARRIER_NOT_PHYSICALLY_SELECTED
+ OUTPUT_CARRIER_NOT_RETAINED_OR_ACCESSIBLE
+ OBSERVER_ACCESS_UNSELECTED.
```

The first missing field is not the classical readout. It is an independently
warranted physical identification of the output field as the actual
gravitational carrier. Even granting that field as a premise, bounded
retention, access, and provenance remain missing.

## 5. Scope correction to HC-DU-074

`CORR-DU-074-1` preserves the earned core of `HC-DU-074`:

- the unconditional generator does not select one classical trajectory;
- homodyne and counting produce different classical record processes;
- neither monitoring supplies bounded retention, access, provenance, or
  target reconstruction; and
- the source does not presently activate a scientific successor.

It rejects only this broader inference:

```text
two inequivalent classical unravellings
  therefore
no common quantum output carrier is selected.
```

The corrected statement is:

```text
two inequivalent classical unravellings
  establish
classical-shadow plurality;

carrier selection is a separate
access-preserving antecedent-fibre question.
```

The source has one common output field **within its chosen dilation**. The
remaining no-ready verdict rests on the earlier and independently sufficient
formation, physical-selection, retention, access, provenance, and target
gaps—not on classical-shadow plurality.

## 6. What this changes for the North Star

The North Star does not require every record to be classical at its first
formation. It permits the more coherent sequence:

```text
physical dynamics forms a quantum output carrier
  -> the carrier is retained and accessible
  -> an observer chooses an admitted action
  -> one classical shadow becomes actual for that interaction
  -> the resulting record changes a declared capability.
```

This is the exact place where observer relativity can enter without making
the observer create the entire carrier or requiring the law to choose every
later question.

But the result also tightens the burden. A theory cannot call its arbitrary
Stinespring environment “the record.” It must derive or independently warrant
the physical factor, output route, retention, access, and provenance. An
isometry that moves information across the observer boundary is not a
harmless representation change.

## 7. Absorption, grade, and stop

### Absorbed

- Stinespring representation and uniqueness;
- complementary/conjugate channels;
- Helstrom binary discrimination;
- amplitude damping;
- quantum-to-classical measurement channels;
- input--output theory;
- quantum filtering; and
- unravelling plurality.

### Dynamic Unity increment

- the access-preserving equivalence passport;
- the carrier/classical-shadow type separation;
- the exact access-relocation obstruction tied to record admission;
- the scoped correction to `HC-DU-074`; and
- the branch-specific source classification.

### Grade

- exact scoped theorem/counterexample: **Grade 4**;
- finite physical-record fixture: **conditional positive control only**;
- Gough--Rees source as DU record selector: **Grade 2 representation /
  conditional construction**;
- empirical/new-physics content: **none**.

### Stop

The action stops here:

- do not run trajectories;
- do not seek hardware;
- do not fit a detector or measurement to a desired target;
- do not infer objective collapse or record ontology;
- do not call the Fock complement a bounded archive; and
- do not activate a later reconstruction swing.

### Reopener

Reopen only with a physical theory or implementation that independently
fixes:

1. the actual source-to-output carrier rather than an arbitrary dilation;
2. its localized formation and blank/input condition;
3. retained provenance over a declared finite horizon;
4. a bounded observer-access algebra and resource budget; and
5. a target-independent action menu with one held-out capability or
   reconstruction consequence.

That future result may keep multiple classical measurements. Their plurality
is no longer treated as a defect.

## 8. Plain-English conclusion

The paper does contain one quantum “thing” that both homodyne and counting
can inspect: its output field. We were right that the two classical histories
are different, but wrong to treat that fact alone as evidence that there is
no common output.

The important question moved one layer earlier:

> Is that output field a real, retained part of the gravitational world, or
> just one mathematically convenient environment used to represent the same
> reduced dynamics?

The paper does not answer that. So the candidate is still not ready—but now
for the right reason.
