---
title: "Localized AQFT source, probe, pointer, archive, and access selection ladder"
status: completed_scoped_result
doc_type: antecedent_ladder_theorem_classification_and_primary_source_collision
created: 2026-07-26
hypothesis_id: HC-DU-033H
prepared_id: CCR-N5-S3
run_id: RUN-20260726-dynamic-unity-localized-aqft-antecedent-ladder
authority: "Joe direct chat: Go, executing the third swing of the prepared physical-selection-to-formed-descent campaign"
claim_grade: "EXACT ANTECEDENT-RELATIVE AQFT INDUCTION-FAMILY, REALIZABILITY-FILTER, INSTRUMENT, FORMED-RECORD, ACCESS, AND FINALITY SELECTION LADDER / EXACT INDUCED-OBSERVABLE VERSUS FORMED-RECORD AND MOVABLE-CUT SEMANTIC BOUNDARIES / KNOWN FEWSTER--VERCH, AQFT INSTRUMENT, SPLIT-PROPERTY, AND QUANTUM-REFERENCE MATHEMATICS / NO ENDOGENOUS QFT POINTER, ARCHIVE, OUTCOME, OBSERVER, ACTUALIZATION LAW, NEW QFT, NEW PHYSICS, HARDWARE RESULT, OR PAPER PROMOTION"
run_plan: "../runs/2026-07-26-localized-aqft-antecedent-ladder.md"
---

# Localized AQFT source, probe, pointer, archive, and access selection ladder

## Result in plain English

Relativistic quantum field theory can do considerably more than say
"measurement happens somewhere." In the Fewster--Verch framework it can
represent a target field, a physical probe field, a compact interaction
region, and the scattering map produced by that interaction. Once a probe
state and probe measurement are supplied, the framework determines:

- the observable induced on the target field;
- the corresponding selective and nonselective state updates;
- where the operation is causally localized; and
- how several supplied measurement schemes compose in causal order.

Those are substantial physical constraints. They are not a selector for the
measurement architecture.

At the rung containing only the target, probe, coupling region, coupled
theory, and scattering morphism, the theory determines a **map from possible
probe preparations and measurements to possible target instruments**. It
does not choose one input to that map. Different probe states, effects,
POVMs, and measurement continuations can therefore produce different
induced observables or state updates while all earlier AQFT data remain
fixed.

The distinction is exact:

```text
localized target--probe dynamics
    selects:
        an induction map
        + causal localization
        + causal composition rules

probe preparation and probe POVM
    select:
        one induced target POVM/instrument

pointer, write, archive, provenance, and reset
    select:
        one formed-record interpretation and carrier

observer access, decoder, resources, actions, and horizon
    select:
        one observer-indexed Admissible Record Envelope
        + one exact or approximate finality claim
```

No rung in this ladder selects which outcome actually occurs. A quantum
instrument assigns outcome probabilities and conditional continuations. An
actual-outcome rule would be additional physics or interpretation and is not
derived here.

Two recent results make the boundary sharper.

First, a movable Fewster--Verch Heisenberg cut exists for a class of Gaussian
field measurements. The same target measurement can be implemented through
an arbitrarily extended chain of physical probes. This supports operational
cut relocation for that measurement class, but it does not make all the
chains the same formed record. Their intermediate carriers, provenance,
resources, and access routes differ unless those distinctions are explicitly
quotiented.

Second, relativistic causality and Fewster--Verch realizability are not the
same condition. There are causal QFT channels that cannot be approximated by
Fewster--Verch schemes, while a broad class of diagonal Weyl instruments is
realizable. Thus realizability is a nontrivial physical filter on candidate
operations. It is still not a point selector: the realizable class is plural,
and the paper's promised-gap decision problem—network-implementable versus
far from network-implementable—is uncomputable in its declared countable
class.

The strongest honest result is:

> **Localized AQFT dynamics selects a covariant induction and realizability
> structure relative to supplied target--probe physics. A particular
> measurement first closes with supplied probe preparation and effects; a
> formed record first closes with supplied pointer/archive semantics; and a
> complete observer-indexed record envelope and finality claim first close
> with supplied access, resource, action, and horizon data.**

This is a scoped grade-4 selection/necessity obstruction in the declared
framework. Its component mathematics is established AQFT measurement theory.
Dynamic Unity's gain is the exact typed receipt and the identification of the
remaining scientific opening: a physical principle that selects the
admissible local-operation and record-interface complex rather than merely
permitting or representing its members.

## 1. Frozen explanatory cut

Let \(\Omega\) be a class of complete realizations of a locally covariant
target QFT together with possible probes, measurement couplings, records, and
observers. Quotient only harmless algebraic presentations, covariant
relabelings, and lossless outcome relabelings. Do not quotient changes of
probe preparation, measured effect, instrument continuation, material
pointer, archive, provenance, observer access, resource budget, or admitted
future action.

Freeze the antecedent ladder

\[
\begin{aligned}
A_0={}&
(\text{locally covariant target theory, spacetime/source class, laws}),\\
A_1={}&
A_0+(\text{realized target state, material source, quantum reference}),\\
A_2={}&
A_1+(\text{probe theory, compact coupling region, coupled theory,
scattering morphism}),\\
A_3={}&
A_2+(\text{probe preparation and effects, pointer/archive,
provenance, reset}),\\
A_4={}&
A_3+(\text{observer access, decoder, resources,
future action envelope, horizon}).
\end{aligned}
\]

For every typed field \(x:\Omega/G_{\mathrm{rep}}\to X\), define

\[
\Sigma_{A_j}^{x}(\alpha)
=
\{x(\omega):A_j(\omega)=\alpha\}.
\]

As in `HC-DU-033F`, \(A_j\) point-selects \(x\) exactly when

\[
\ker A_j\subseteq\ker x.
\]

If the fibre image is a covariant family, one symmetry orbit, several
inequivalent possibilities, a trivial object only, or an empty nontrivial
class, return that exact set-valued result.

This ladder separates four questions that are often compressed into one:

1. Which operations are covariantly definable?
2. Which operations are physically realizable by a local target--probe
   interaction?
3. Which realizable operation and record carrier is physically selected?
4. Which outcome is actual in one run?

The first two can constrain the third. They are not answers to it.

## 2. The Fewster--Verch induction map

Use a target theory \(\mathcal A\), probe theory \(\mathcal B\), compact
coupling region \(K\), and scattering morphism

\[
\Theta:\mathcal A\otimes\mathcal B
\longrightarrow
\mathcal A\otimes\mathcal B .
\]

For a supplied probe state \(\sigma\), let

\[
\eta_\sigma(A\otimes B)=\sigma(B)A
\]

be partial evaluation over the probe. A supplied probe observable \(B\)
induces the target observable

\[
\varepsilon_{\sigma,\Theta}(B)
=
\eta_\sigma\!\left(\Theta(\mathbf 1\otimes B)\right).
\]

For a supplied probe POVM, the same data determine the induced target POVM
and its selective pre-instrument. The corresponding nonselective map
describes target evolution when the outcome is ignored.

The primary construction is due to
[Fewster and Verch](https://arxiv.org/abs/1810.06512). Their framework proves
causal localization of induced observables and causal factorization for
several supplied coupling regions. These are positive \(A_2\)-level results.

### Theorem 1 — induction-family selection, not point selection

For fixed \(A_2\), the target--probe dynamics determines the family-valued
map

\[
\mathsf{Ind}_{A_2}:
(\sigma,\mathsf B)
\longmapsto
\left(
\varepsilon_{\sigma,\Theta}(\mathsf B),
\mathcal I_{\sigma,\Theta,\mathsf B}
\right),
\]

where \(\mathsf B\) is a probe POVM and
\(\mathcal I_{\sigma,\Theta,\mathsf B}\) is the induced target instrument.

It does not point-select one member of the image unless an additional
physical premise already makes the allowed probe preparation and POVM a
singleton modulo the declared equivalence.

### Proof

The formula for \(\mathsf{Ind}_{A_2}\) is fixed by the target--probe
scattering morphism. Its arguments \(\sigma\) and \(\mathsf B\) are not
fields of \(A_2\). Two complete realizations can therefore agree on every
\(A_2\) field and differ only in those arguments.

If the induction map has nontrivial image, there are allowed choices whose
induced target effects or continuations differ. In particular, the unit
effect always induces \(\mathbf 1\); any induced nontrivial effect therefore
makes the image plural. Hence

\[
\ker A_2\nsubseteq
\ker(\text{induced target instrument}).
\]

If its image is trivial, \(A_2\) still does not select a nontrivial local
record. Therefore \(A_2\) selects either a plural induction family or no
nontrivial target instrument, not one nontrivial record interface.

At \(A_3\), a supplied \(\sigma\), probe POVM, and scattering scheme
determine one target instrument. This is an apparatus-relative selection
receipt. It is not selection by the bare target theory or locality.

### Exact symmetry- and resource-matched control

The smallest algebraic control uses SU(2)-symmetric isomorphic target and
probe qubits with a fixed SWAP scattering unitary. For every probe effect
\(E\),

\[
\varepsilon_\sigma(E)
=
\eta_\sigma\!\left(
\operatorname{SWAP}^{*}(\mathbf 1\otimes E)\operatorname{SWAP}
\right)
=E.
\]

Hold fixed the maximally mixed probe preparation, coupling, binary pointer,
one-bit archive, and resource charge. The two probe PVMs

\[
E^{z}_{\pm}=\frac{\mathbf 1\pm Z}{2},
\qquad
E^{x}_{\pm}=\frac{\mathbf 1\pm X}{2}
\]

induce the distinct target PVMs \(E^{z}\) and \(E^{x}\). They have the same
outcome count, ranks, sharpness, pointer size, and write cost. A joint
Hadamard rotation preserves the SWAP architecture and moves one PVM to the
other, so the earlier symmetric antecedent contains the full measurement-axis
orbit. No lossless outcome relabeling identifies the two noncommuting target
algebras.

This is an exact finite control of the selector logic, not evidence that a
particular AQFT realizes a qubit SWAP locally. The field-theoretic conclusion
rests on the Fewster--Verch definitions and the primary-source realizability
families; the control only proves that "the interaction determines an
induction map" cannot be silently upgraded to "the interaction chooses its
measurement input."

## 3. Observable, instrument, and record are distinct

A POVM fixes outcome probabilities. It does not fix the post-measurement
state. Distinct instruments can implement the same POVM, and distinct
measurement channels can retain or erase different future capabilities.

[Mandrysch and Navascués](https://arxiv.org/abs/2411.13605) make this
distinction explicit in the Fewster--Verch setting. Their construction
contains families of instruments with the same measured POVM but different
dephasing or continuation behavior.

Thus:

\[
\text{same POVM}
\not\Longrightarrow
\text{same selective continuation}.
\]

An induced target instrument is still not a formed record. To obtain one,
the physical contract must specify:

- the event-to-pointer correlation;
- the pointer's material carrier and value semantics;
- a write and durable archive;
- provenance joining the archived value to the occurrence;
- reset and rejected/invalid-attempt treatment; and
- the accessible classical register or operational readout.

Those are \(A_3\) fields in this ladder. Calling the abstract effect itself a
record would skip the formation problem.

Finally, an instrument does not select an actual outcome. It returns a family
of outcome-indexed completely positive maps and their probabilities. The
architecture of possible records and the realization of one record value are
different explanatory targets.

## 4. What locality and causal factorization actually select

Fewster--Verch supplies two important positive results relative to a frozen
coupling.

### 4.1 Causal localization

The scattering morphism is trivial in regions causally disjoint from the
coupling, and induced observables can be localized in the causal hull of the
coupling region under the framework's hypotheses.

This selects a causal localization relation **conditional on \(K\),
\(\Theta\), the probe, and the measured probe effect**. It does not select
those fields.

### 4.2 Causal factorization

Several compactly supported couplings compose in their causal order.
Causally disjoint schemes give order-independent induced operations under
the appropriate hypotheses.

This selects a composition rule for supplied schemes. It does not:

- create a pointer or archive;
- authenticate an outcome;
- choose an access route or observer;
- decide which coupling occurs;
- choose a future action envelope; or
- make the result final against every future recoupling.

Relativistic causal order therefore constrains formed records without
forming them.

## 5. Causality is not realizability, and realizability is not selection

A 2026 primary-source preprint,
[Mandrysch, Simmons, and Navascués](https://arxiv.org/abs/2607.12976),
separates two candidate classes of local QFT operations:

1. instruments satisfying a relativistic causal condition; and
2. instruments realizable, exactly or asymptotically, through
   Fewster--Verch probe schemes.

They prove, in their declared free-scalar/Weyl setting, that:

- some causal channels cannot be approximated by Fewster--Verch schemes;
- a broad class of diagonal Weyl instruments is asymptotically
  Fewster--Verch realizable;
- such instruments suffice for nondemolition implementation of broad field
  POVM classes; and
- distinguishing network-implementable channels from channels far from that
  class is uncomputable for a countable class, assuming the paper's split and
  network conditions.

The Dynamic Unity receipt is:

```text
Einstein causality:
    supplies a necessary admissibility screen
    but permits operations outside the FV-realizable class

FV realization:
    supplies a stronger physical implementation witness
    but leaves many possible probes, instruments, and records

network-FV undecidability:
    blocks one universal effective classifier in the scoped class
    but does not select an implementation or actual outcome
```

This recent result strengthens the scientific opening. A principle that
selects the physically feasible operation class beyond causality is an open
QFT problem in the source itself. Dynamic Unity must not claim to have solved
it. Its contribution here is to identify that open class-selection problem
as the QFT instance of physical Admissible Record Envelope selection.

Uncomputability also must not be inflated. It does not imply physical
openness, becoming, or actualization. It says that the declared membership
problem has no general algorithmic decision procedure.

## 6. Movable cut: operational equivalence versus formed-record identity

[Mandrysch and Navascués](https://arxiv.org/abs/2411.13605) show that their
Gaussian-modulated field measurements admit an arbitrarily movable
Fewster--Verch Heisenberg cut. A probe can itself be measured by another
probe, and so on, while retaining the target measurement in the relevant
limit.

This is a strong absorber for any claim that the location of the abstract
system/apparatus cut is itself new physics.

It does not establish formed-record invariance for free. Extending the chain
can change:

- the number and type of material probes;
- coupling and processing regions;
- intermediate pointer values;
- provenance depth;
- reset memories and failure strata;
- resource use and latency; and
- which observer can access which carrier.

Let \(c_n\) denote an \(n\)-probe implementation and let \(q_{\mathrm{tar}}\)
be the induced target measurement statistics. Movable-cut equivalence can
give

\[
q_{\mathrm{tar}}(c_n)
\simeq
q_{\mathrm{tar}}(c_m).
\]

It does not imply

\[
q_{\mathrm{formed}}(c_n)
=
q_{\mathrm{formed}}(c_m)
\]

when \(q_{\mathrm{formed}}\) retains complete pointer, provenance, attempt,
and access data.

Therefore cut movement is:

- an operational target-level equivalence in the proved measurement class;
- a possible refinement or completion enlargement at the formed-record
  level; and
- an invariance only after the omitted intermediate distinctions are proved
  irrelevant to every frozen held-out action.

## 7. Split inclusions and quantum reference frames

The split property can insert a type-I factor between nested local algebras
under additional assumptions. That creates a useful subsystem arena. It does
not canonically select:

- one split inclusion;
- one probe;
- one tensor-product presentation;
- one pointer basis;
- one material archive; or
- one decoder and observer boundary.

This preserves `HC-DU-040B`: a full local factor has no nontrivial exact
internal nondisturbing finite sharp record. A nontrivial record must use an
independently justified restricted action algebra, an enlarged
source--probe--pointer--archive interface, boundary/sector structure, or an
approximate horizon-indexed contract.

Quantum reference frames can remove some symmetry ambiguity by adding a
physical reference resource. In
[Fewster et al.](https://arxiv.org/abs/2403.11973), field observables are
measured relative to a supplied QRF and the invariant joint algebra can take
crossed-product/type-II form under stated thermal conditions.

That is a positive \(A_1/A_2\) construction. The reference resource, its
covariant observable, and its state are physical inputs. The construction
does not show that the target QFT selects which QRF is present.

## 8. Pointer, archive, access, ARE, and finality receipt

| Field | First rung that can close it | Exact receipt |
|---|---:|---|
| Locally covariant target theory and spacetime/source class | \(A_0\) | Supplied theory class, not one realized state |
| Realized target state/material source/QRF | \(A_1\) | Supplied or independently source-selected; QRF is a resource |
| Probe theory, coupling region, coupled theory, scattering morphism | \(A_2\) | One physical measurement architecture supplied |
| Induction map and causal localization/composition | \(A_2\) | Selected relative to the supplied architecture |
| Particular induced target observable or instrument | \(A_3\) | Fixed by probe preparation and probe POVM/effect |
| Pointer, write, archive, provenance, reset | \(A_3\) | Formed record only after these material semantics are supplied |
| Actual outcome in one run | no rung | Instrument probabilities are not an actualization rule |
| Observer access, authentication, decoder, resource budget | \(A_4\) | Observer-indexed access contract |
| Complete physical ARE | \(A_4\) | Requires joint realizability, resources, and action class |
| Exact finality | \(A_4\), if at all | Only relative to the frozen future action envelope |
| Approximate finality | \(A_4\), finite horizon | Requires norm, horizon, and leakage composition |

The full local action algebra remains noncommutative and commonly factorial.
Consequently, the exact record cannot be a nontrivial sharp internal record
that nondisturbingly preserves every local action. It must be
apparatus-relative, action-restricted, boundary/sector-supported, or
approximate.

For a formed public record algebra \(\mathcal Z\) and frozen future selective
maps \(\{\Phi_{a,y}\}\), reuse `HC-DU-035D`:

\[
\Phi_{a,y}^{*}(\mathcal Z_{\mathrm{future}})
\subseteq
\mathcal Z_{\mathrm{current}}
\]

for every admitted action \(a\) and outcome \(y\). This is a finality
criterion after the record and action class are supplied. AQFT locality does
not select the action class or horizon.

## 9. Exact verdict

The selector-fibre verdict is:

\[
\begin{array}{c|c}
\text{Antecedent} & \text{Minimal honest return}\\
\hline
A_0 &
\text{covariant target-theory and causal-operation classes}\\
A_1 &
\text{state/reference-relative classes}\\
A_2 &
\text{one induction map and FV architecture, but plural instruments}\\
A_3 &
\text{one apparatus-relative induced instrument and formed record}\\
A_4 &
\text{one observer/resource/action-relative ARE and finality contract}
\end{array}
\]

Accordingly:

1. **A2 induction-family theorem — exact.** The target--probe dynamics
   selects the map from supplied probe choices to induced target operations,
   not one operation.
2. **Induced-observable/formed-record separation — exact.** A target effect
   or instrument does not supply a material pointer, archive, provenance, or
   actual outcome.
3. **Causality/realizability separation — imported exact result.** Causal
   admissibility is broader than Fewster--Verch realizability in the scoped
   source class.
4. **Movable-cut semantic boundary — exact.** Target measurement equivalence
   does not imply complete formed-record identity without an additional
   action-sufficiency proof.
5. **Factor control — preserved.** The full local factor has no nontrivial
   exact internal nondisturbing finite sharp record.
6. **ARE/finality closure — antecedent-relative.** A complete record envelope
   and finality claim first close at \(A_4\).

No generic AQFT pointer, archive, outcome, observer, actualization law,
record-substrate ontology, new relativistic measurement dynamics, or new
physics is selected.

## 10. Prior-art and novelty grade

### Established mathematics

- Fewster--Verch target--probe measurement schemes;
- induced observables and instruments;
- causal localization and factorization;
- POVM/instrument nonuniqueness;
- movable Fewster--Verch cuts for the proved Gaussian measurement class;
- split-property subsystem constructions;
- quantum-reference relative observable algebras;
- causal-versus-FV-realizable operation separation; and
- scoped undecidability of network-FV implementability.

### Dynamic Unity gain

Dynamic Unity contributes the unchanged `HC-DU-033F` selector passport across
all of those layers:

\[
\text{law}
\to
\text{realized source/reference}
\to
\text{localized probe dynamics}
\to
\text{induced instrument}
\to
\text{formed archive}
\to
\text{observer ARE/finality}.
\]

The exact gain is the attribution of what each arrow selects, what it merely
maps, and what remains supplied. That is scientifically useful because it
prevents causal localization, realizability, a POVM, or cut invariance from
being mistaken for record formation or finality.

### Grade

- **Scoped selection/necessity obstruction:** grade `4`.
- **Novel QFT theorem:** not earned.
- **New physical law or prediction:** not earned.
- **Paper promotion:** not earned.

The most important unabsorbed scientific question is shared with the recent
QFT source:

> What physical principle selects the feasible local-operation and
> record-interface complex beyond relativistic causality, and does that
> principle also select formed archives and observer capabilities?

This swing formulates that question precisely but does not answer it.

## 11. Handoff to `CCR-N5-S4`

The campaign now has two independent adverse/partial selector receipts:

1. Einstein--matter can select flow and conditional synchronization before
   it selects clocks, writes, archives, or access; and
2. localized AQFT can select an induction/realizability structure before it
   selects a probe measurement, formed archive, observer ARE, or actual
   outcome.

`CCR-N5-S4` should not require either arena to supply an endogenous pointer.
It should take the smallest explicitly formed \(A_3/A_4\) interfaces from:

- the material `Z3` gauge recorder;
- the stabilizer/QEC control;
- the Einstein--matter clock/archive control; and
- the localized AQFT apparatus-relative record class;

then ask whether their certified overlap and action-sufficiency conditions
descend through one typed law, or whether the quantum-field and
distributed/finite systems require provably different composition objects.

The QFT branch must preserve:

- the distinction between causal and FV-realizable operations;
- the physical probe and coupling receipt;
- every pointer/archive/provenance/access field;
- the movable-cut quotient actually being used; and
- the frozen future action class and horizon.

Do not reopen detector fitting, add a simulation, or claim that operational
cut equivalence supplies formed-record equivalence.
