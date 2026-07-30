---
title: "QRF outcome broadcast, reference coherence, and layered-finality boundary"
status: completed_scoped_result
doc_type: primary_source_collision_exact_broadcast_theorem_and_finality_nonimplication
created: 2026-07-30
hypothesis_id: HC-DU-154
run_id: RUN-20260730-075045-qrf-outcome-broadcast-layering
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 exact outcome-broadcast/reference-coherence nonimplication and retained-branch-information boundary; Grade 5 only after a physically selected formed-record interface yields no-refit excess over standard quantum theory"
probe: "../tests/du_qrf_outcome_broadcast_layering_probe.py"
artifact: "../tests/artifacts/du_qrf_outcome_broadcast_layering_result.json"
---

# QRF outcome broadcast, reference coherence, and layered finality

## Executive result

The swing returned:

```text
POSITION_SUPERPOSED_LAB_AND_INTERNAL_OUTCOME_REGISTER_ARE_SEPARATE_DEGREES
+ PERFECT_OUTCOME_BROADCAST_NEED_NOT_REVEAL_POSITION_BRANCH
+ PERFECT_OUTCOME_READABILITY_AND_REFERENCE_POSITION_COHERENCE_CAN_COEXIST
+ RETAINED_BRANCH_INFORMATION_NOT_OUTCOME_INFORMATION_CONTROLS_DECOHERENCE
+ TEMPORARY_BRANCH_MARKING_CAN_BE_COHERENTLY_ERASED
+ AN_INACCESSIBLE_COPY_OF_THE_TEMPORARY_TAG_PREVENTS_RESTORATION
+ PARTIAL_BRANCH_LEAKAGE_OBEYS_STANDARD_VISIBILITY_DISTINGUISHABILITY
+ ONE_WHOLE_SYSTEM_FINALITY_SCALAR_IS_REFUTED_AS_A_GENERAL_DESCRIPTION
+ ALGEBRA_RELATIVE_RECORD_STATUS_IS_SUPPORTED_CONDITIONALLY
+ THE_HEISENBERG_CUT_OUTCOME_BASIS_APPARATUS_ACCESS_AND_CERTIFICATION_REMAIN_SUPPLIED
+ STANDARD_UNITARY_QM_COMPLEMENTARITY_ERASURE_AND_DECOHERENCE_ABSORB_THE_RESULT
+ NO_NEW_PHYSICS_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

Vanrietvelde's
[*Specifying the operational meaning of quantum reference
frames*](https://arxiv.org/abs/2607.03417) makes a useful distinction that is
easy to miss. A laboratory may be in a superposition of **absolute
positions** while its internal measurement register holds a definite
**outcome**. The paper then gives a two-location communication protocol that
copies the outcome to a well-localized receiver without leaving the receiver
correlated with the lab's position.

The Dynamic Unity result is:

> Broadcasting an outcome does not by itself classicalize every degree of
> freedom of the system that holds it. Reference-position coherence is lost
> exactly to the extent that some retained external degree of freedom can
> distinguish the position branches.

This is a concrete orthodox-quantum example of independently typed finality
coordinates. The outcome can be definite and externally copyable while the
position remains coherent. It rules out a naive single scalar such as “the
lab is finalized” as a complete description.

It does **not** prove Dynamic Unity's proposed layered regional finality as a
new law. The paper explicitly places the internal outcome outside its
Heisenberg cut. It assumes the lab decomposition, measurement register,
definite outcome, communication interactions, external receiver, and access
arrangement. Standard unitary quantum mechanics, which-path
complementarity, decoherence, and quantum erasure explain the complete
protocol.

## 1. Source passport

| Object | Source status | Dynamic Unity reading |
|---|---|---|
| Lab/rocket absolute position | physically modeled in superposition | reference degree, not an outcome |
| Lab internal degrees | supplied composite system | includes apparatus and outcome register |
| Internal outcome \(s\) | taken as definite after placing it outside the Heisenberg cut | ordinary measurement assumption, not derived actualization |
| Alice's outcome register | physical carrier at a definite relative location in the lab | formed record conditional on the cut |
| Eve's receiver register | supplied external communication carrier | access interface |
| Known candidate positions \(x_0,x_1\) | supplied protocol geometry | permits the sequential local contacts |
| First local copy interaction | supplied controlled operation at \(x_0\) | temporarily marks the position branch |
| Coherent transport of Eve's register | supplied control | preserves the temporary superposition |
| Second local copy interaction | supplied controlled operation at \(x_1\) | removes the position dependence of the message |
| Final receiver outcome | derived from the protocol | readable copy of \(s\) |
| Final position coherence | derived under the isolated coherent packet | restored/preserved |
| Lost intermediate tag | hostile variation added here | creates ordinary which-path decoherence |
| Observer/public certification | not selected | one receiver is not public/BFT finality |
| New dynamics or excess prediction | absent | standard-QM construction |

The source is explicit that the QRF proposal requires no special solution to
the measurement problem. That is a strength as an operational clarification
and a hard limit on what Dynamic Unity may import.

## 2. Exact controlled-message theorem

Let \(L\) be the reference-position system with orthonormal branches
\(\{|x\rangle\}\), \(R\) an internal register holding a definite outcome
\(r\), and \(E\) an external message carrier initially blank. Consider a
nondemolition communication isometry of the form

\[
V\bigl(|x\rangle_L|r\rangle_R|0\rangle_E\bigr)
=
|x\rangle_L|r\rangle_R|m_{r,x}\rangle_E.
\tag{1}
\]

For an initial reference state

\[
\rho_L=\sum_{x,y}\rho_{xy}|x\rangle\!\langle y|,
\tag{2}
\]

tracing the message carrier after the communication gives

\[
\rho'_{xy}
=
\rho_{xy}
\langle m_{r,y}|m_{r,x}\rangle.
\tag{3}
\]

### Proof

Apply (1) to each ket and bra in (2). The \(x,y\) term becomes

\[
\rho_{xy}
|x\rangle\!\langle y|
\otimes
|m_{r,x}\rangle\!\langle m_{r,y}|.
\]

The partial trace over \(E\) contributes
\(\langle m_{r,y}|m_{r,x}\rangle\), yielding (3). \(\square\)

### Corollary 1 — exact reference-state preservation

The communication preserves every reference density operator exactly iff

\[
\langle m_{r,y}|m_{r,x}\rangle=1
\quad\text{for every }x,y
\tag{4}
\]

on the admitted branch support. In particular, it suffices that

\[
|m_{r,x}\rangle=|m_r\rangle
\quad\text{for every }x.
\tag{5}
\]

### Corollary 2 — outcome readability is compatible

Perfect outcome readability requires orthogonal messages for distinct
outcomes,

\[
\langle m_{r'}|m_r\rangle=0
\quad(r'\ne r).
\tag{6}
\]

Equations (5) and (6) are compatible. The message may depend perfectly on
the outcome \(r\) while being independent of the position branch \(x\).
Perfect outcome broadcast therefore does not imply any position decoherence.

### Corollary 3 — the first leak

If the messages for two position branches are orthogonal at fixed outcome,

\[
\langle m_{r,1}|m_{r,0}\rangle=0,
\tag{7}
\]

the corresponding position coherence vanishes after the message carrier is
lost. The first leak is retained **branch information**, not retained outcome
information.

## 3. The paper's sequential protocol and the hostile control

For outcome \(s=1\), begin with

\[
|\Psi_0\rangle
=
\frac{|x_0\rangle+|x_1\rangle}{\sqrt2}
\otimes|0\rangle_E.
\tag{8}
\]

The first local contact at \(x_0\) gives

\[
|\Psi_1\rangle
=
\frac{
  |x_0\rangle|1\rangle_E
  +
  |x_1\rangle|0\rangle_E
}{\sqrt2}.
\tag{9}
\]

The receiver temporarily carries a perfect position tag. If it is traced or
measured now, the reference position decoheres.

Eve instead retains the receiver coherently, moves it to \(x_1\), and applies
the second local contact:

\[
|\Psi_2\rangle
=
\frac{|x_0\rangle+|x_1\rangle}{\sqrt2}
\otimes|1\rangle_E.
\tag{10}
\]

The outcome is now outside the lab and the position tag is gone. The
position coherence is fully restored because the final message state is the
same on both branches.

The hostile control inserts an inaccessible register \(F\) that copies
Eve's temporary value after Equation (9). After the second contact,

\[
|\Psi_{2,\mathrm{leak}}\rangle
=
\frac{
  |x_0\rangle|1\rangle_E|1\rangle_F
  +
  |x_1\rangle|1\rangle_E|0\rangle_F
}{\sqrt2}.
\tag{11}
\]

Eve still reads the outcome perfectly, but tracing \(F\) destroys the
position off-diagonal. Coherent uncomputation cannot erase information that
has already been retained elsewhere.

This is the precise boundary between:

- temporary correlation;
- a reversible provisional mark;
- a broadcast outcome;
- a retained which-branch record; and
- irreversible-for-the-declared-access-class decoherence.

## 4. Partial leakage

For two pure branch-conditioned message states, define

\[
V=|\langle m_1|m_0\rangle|,
\qquad
D=\sqrt{1-|\langle m_1|m_0\rangle|^2}.
\tag{12}
\]

Then

\[
V^2+D^2=1.
\tag{13}
\]

The exact regression uses

\[
|m_0\rangle=|0\rangle,
\qquad
|m_1\rangle=\frac35|0\rangle+\frac45|1\rangle,
\tag{14}
\]

so \(V=3/5\) and \(D=4/5\).

This is the familiar pure-state two-path complementarity relation. It shows
that the layered reading is quantitative, but not novel physics: the
remaining reference coherence is exactly the information that did **not**
escape about the reference branch.

## 5. What this changes for Dynamic Unity

### 5.1 One whole-system finality scalar is too coarse

The statement “the laboratory is classical/final” loses essential type
information. In the source's packet:

| coordinate | status |
|---|---|
| internal outcome value | definite by the supplied cut |
| internal outcome carrier | physically formed |
| outcome availability to Eve | copied and accessible |
| absolute position | coherent superposition |
| temporary branch tag | reversible while coherently retained |
| leaked branch tag | irreversible relative to the reduced access class |
| public/BFT certification | absent |

Different algebras and access cuts therefore support different stability and
copyability judgments at the same time.

### 5.2 The strongest sustainable layered-finality statement

The earned statement is conditional:

> In standard quantum mechanics, finality-like properties are indexed to a
> chosen observable algebra, carrier, environment, and access class. A fact
> may be definite and broadcastable in one factor while another factor
> remains coherent.

This supports Dynamic Unity's insistence that local, regional, and public
record status not be collapsed. It does not show that these layers are new
fundamental dynamics, consensus mechanisms, or a substrate ontology.

### 5.3 Formation and retention remain distinct

Equation (9) looks like a record if one inspects only the instantaneous
correlation. Equation (10) shows that the branch tag was provisional and
erasable. Equation (11) shows what makes it durable for the reduced observer:
the distinguishing information survives in an inaccessible carrier.

Thus:

```text
correlation != retained record
temporary distinguishability != finality
outcome broadcast != global classicalization
one external copy != public certification
```

### 5.4 Relation to `HC-DU-153`

`HC-DU-153` established that a chosen block population survives a reduced
QRF handoff only under dynamical compatibility, and that environment versus
reference decoherence is not identifiable from one local visibility curve.

`HC-DU-154` adds the complementary formation/broadcast control:

- an outcome block can be copied across a physical reference boundary;
- the copy need not carry reference-branch information;
- reference coherence survives exactly when the complete outgoing packet
  erases that branch information; and
- an unobserved retained branch tag is enough to destroy it.

Together they supply a stronger orthodox-quantum architecture for
access-relative handoff. They still do not select the outcome algebra,
measurement cut, factorization, or certification rule.

## 6. Absorber and novelty

The component result is absorbed by:

- controlled unitary measurement models;
- which-path information and visibility complementarity;
- decoherence by entanglement with inaccessible degrees;
- quantum erasure/uncomputation;
- no-information-without-disturbance; and
- the source's own operational QRF construction.

The Dynamic Unity increment is the typed synthesis:

```text
outcome information
  is independent of
reference-branch information;

record formation
  is independent of
whole-system classicalization;

external broadcast
  is independent of
public certification.
```

This is useful for the North Star because it names the exact physical datum
that a layered-finality model must track: not “how classical the system is,”
but which distinctions have become durably available to which action/access
class.

It is not a novel law or empirical prediction.

## 7. Exact reopener

A scientific successor exists only if one physical model supplies, without
target-dependent refitting:

1. the measurement dynamics and actualization rule rather than a supplied
   Heisenberg cut;
2. the subsystem/reference decomposition and outcome algebra;
3. a blank-to-written carrier with retained provenance;
4. the complete outgoing/environment packet;
5. the observer action/access and certification class;
6. a composable multi-region handoff;
7. one held-out target; and
8. a result not reproduced by the corresponding standard quantum channel.

Until then, additional QRF communication toys would reproduce known quantum
information theory. No hardware, prediction, paper, or successor is
activated.

## 8. Exact evidence

Run:

```bash
python3 tests/du_qrf_outcome_broadcast_layering_probe.py --write-artifact
```

The regression checks:

- the initial reference-position coherence;
- temporary loss under the first branch-marking interaction;
- full restoration after coherent protocol completion;
- perfect outcome readability at the receiver;
- coexistence of orthogonal outcome messages and branch-independent messages;
- failure of coherence restoration after an inaccessible intermediate copy;
  and
- the exact \(3/5\), \(4/5\) complementarity control.

It is an exact finite illustration, not a laboratory simulation.

## Final disposition

```text
claim_id: HC-DU-154
return: ALGEBRA_RELATIVE_BROADCAST
first_leak: RETAINED_REFERENCE_BRANCH_INFORMATION
absorber: STANDARD_UNITARY_QUANTUM_MECHANICS
interface: SUPPLIED
grade: scoped Grade 4
next: NO_READY_SUCCESSOR
hardware: not warranted
prediction: none
paper_state: unchanged
```
