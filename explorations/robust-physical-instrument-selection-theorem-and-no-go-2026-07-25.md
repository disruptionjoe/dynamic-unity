---
title: "Robust physical instrument selection: source-action theorem and dilation no-go"
status: completed_scoped_result
doc_type: theorem_no_go_and_executable_control
created: 2026-07-25
run_id: RUN-20260725-120514-robust-physical-instrument-selection
authority: "Joe direct chat: Yeah, let's go after it."
claim_grade: "EXACT FINITE FAMILY SELECTOR AND NO-GO / COMPONENT MATHEMATICS KNOWN / EFFECTIVE INSTRUMENT ORBIT SELECTED ONLY RELATIVE TO FROZEN SOURCE, ACTION AND COUPLING CLASSES / NO NEW PHYSICS OR THEOREM-ID PROMOTION"
probe: "../tests/du_robust_physical_instrument_selection_probe.py"
artifact: "../tests/artifacts/du_robust_physical_instrument_selection_result.json"
---

# Robust Physical Instrument Selection

## Result in plain English

This swing gets a real positive result, but it also locates the limit very
cleanly.

The positive result is:

> Once a source action, a matched family of possible couplings, and a
> nonzero-quality record are frozen independently, exact preservation of the
> source action selects the aligned measurement axis, up to relabeling its
> two outcomes. Approximate preservation gives an exact quantitative bound
> on how far the measurement can be misaligned.

This is stronger than the previous result. The earlier control showed that a
frozen source \(Z\) rejects one sharp \(X\) foil. The new control sweeps an
entire continuous family of axes and all binary record strengths. It proves
the exact relation

\[
\delta_Z
=
\left(1-\sqrt{1-D^2}\right)|\sin\theta|,
\]

where:

- \(D\) is the pointer's ability to distinguish the two candidate sectors;
- \(\theta\) is the angle between the candidate record axis and the source
  \(Z\) axis; and
- \(\delta_Z=\|\Phi_\theta^*(Z)-Z\|_\infty\) is the source-action
  disturbance.

Whenever \(D>0\),

\[
|\sin\theta|
\leq
\frac{\delta_Z}{1-\sqrt{1-D^2}}.
\]

At exact nondisturbance, the only surviving axes are \(+Z\) and \(-Z\), which
are the same binary PVM with the outcome names exchanged. At \(D=0\), every
axis passes because no information was recorded. That null is essential: a
selector cannot be earned by an apparatus that learns nothing.

The complete coupling has a parallel symmetry receipt. If the pointer
generator is frozen as degenerate, so the declared total generator is
\(Z\otimes I\), then

\[
\kappa
=
\left\|[U_{\theta,\epsilon},Z\otimes I]\right\|_\infty
=
\sqrt{2\left(1-\sqrt{1-D^2}\right)}
|\sin\theta|.
\]

Thus the aligned informative coupling preserves the frozen generator, while
an equally informative conjugate coupling does not.

The first no-go is:

> The source action can select the measurement axis without selecting the
> selective continuation.

A Lüders instrument and an outcome-conditioned internal twist have exactly
the same sharp effects, archive values, immediate repeatability, and central
source nondisturbance. They nevertheless send one input to orthogonal
post-measurement states. A full within-sector action algebra rejects the
twist. Source energy alone rejects it only when an independently justified
internal splitting breaks the degeneracy.

The second no-go is:

> Even source, symmetry, record, continuation, and access constraints can at
> most select an effective instrument orbit. They cannot select one unique
> microscopic apparatus or dilation.

Two implementations can induce exactly the same system-plus-archive
instrument after an environment is ignored while carrying perfectly
distinguishable retained environment states. This is ordinary dilation
freedom. If that environment is operationally available, it belongs inside
the interface and the implementations are different. If it is not available,
they are one effective instrument for the declared task.

The end-to-end archive remains load-bearing. If the pointer distinction is
\(D\) and the archive flips with probability \(q\), then the observer sees

\[
D_{\mathrm{access}}=|1-2q|D.
\]

Three-copy majority decoding improves that quantity but uses three archive
bits and remains inexact whenever \(q>0\). Pointer selection and
observer-accessible selection are therefore different receipts.

The coherent route control also does useful housekeeping. Coherently routing
the Lüders target and the continuation twist reduces route-\(X\) visibility
from \(1\) to \(1/2\) for the held-out input while preserving the same
outcome effects. The complete standard quantum model predicts that result
exactly. It is a valid instrument-identity assay, not evidence of
perspectival curvature or nonstandard dynamics.

The executable passes `31/31`.

## What is actually selected

The maximal earned object is:

> the source-aligned effective Lüders instrument orbit, inside the declared
> binary-QND and full-action-preserving candidate classes, up to outcome
> relabeling, operationally inert outcome phases, and inaccessible dilation
> freedom.

The swing does **not** select:

- the source Hamiltonian or action algebra;
- the class of admissible couplings;
- the pointer or archive boundary;
- the decoder;
- a unique apparatus Hamiltonian;
- a unique Stinespring dilation;
- quantum theory among generalized probabilistic theories; or
- a physical ontology in which records are fundamental.

This is the exact answer to the flagship question. Physical structure can
select an instrument orbit, but only relative to a source, action, candidate,
access, and resource contract that was fixed before the verdict. A unique
microscopic implementation is neither required operationally nor obtainable
from the present conditions.

## Frozen model

Let

\[
n_\theta=(\sin\theta,0,\cos\theta)
\]

and let

\[
P_\pm^{(\theta)}
=
\frac{I\pm n_\theta\cdot\sigma}{2}.
\]

For \(0\leq\epsilon\leq1/2\), the two pointer Kraus operators are

\[
\begin{aligned}
M_0
&=\sqrt{1-\epsilon}\,P_+^{(\theta)}
  +\sqrt{\epsilon}\,P_-^{(\theta)},\\
M_1
&=\sqrt{\epsilon}\,P_+^{(\theta)}
  +\sqrt{1-\epsilon}\,P_-^{(\theta)}.
\end{aligned}
\]

The probe constructs a full system--pointer unitary, begins the pointer and
archive in declared blank states, copies the pointer to the archive, and
recovers these Kraus operators by reading the copied archive. It does not
start from a bare POVM.

The target and conjugate foil have the same:

- system, pointer, and archive dimensions;
- number of system--pointer interactions;
- pointer-to-archive copy;
- decoder;
- archive-noise channel; and
- declared resource ledger.

The only changed coordinate is \(\theta\).

## Scoped theorem 1 — source-action alignment

Define

\[
D=1-2\epsilon
\]

and

\[
v=2\sqrt{\epsilon(1-\epsilon)}
  =\sqrt{1-D^2}.
\]

The nonselective channel is dephasing about \(n_\theta\): it preserves the
Bloch component parallel to \(n_\theta\) and multiplies every transverse
component by \(v\). Therefore

\[
\Phi_\theta^*(Z)
=
vZ+(1-v)(n_\theta\cdot\hat z)(n_\theta\cdot\sigma).
\]

Subtracting \(Z\) gives a Bloch vector of length

\[
(1-v)|\sin\theta|.
\]

Hence

\[
\boxed{
\|\Phi_\theta^*(Z)-Z\|_\infty
=
\left(1-\sqrt{1-D^2}\right)|\sin\theta|
}.
\]

For \(D>0\), the coefficient is strictly positive. Exact source-action
nondisturbance then implies \(\sin\theta=0\), so the axis is \(+Z\) or
\(-Z\). Conversely, those axes preserve \(Z\). The approximate bound follows
by division.

This is a scoped algebraic theorem for the frozen binary family. It is not a
universal measurement theorem and receives no new theorem ID.

## Scoped theorem 2 — full-action continuation selection

Let \(\{P_j\}\) be a sharp sector PVM and restrict the candidate instruments
to unitary within-sector twists

\[
K_j=U_jP_j.
\]

Every such instrument has effects \(P_j\), is repeatable, and preserves the
center generated by the \(P_j\). Those conditions therefore do not select a
continuation.

Now require the nonselective adjoint channel to preserve every member of the
full block action algebra

\[
\mathcal A_{\mathrm{block}}
=
\bigoplus_j \mathcal B(P_j\mathcal H).
\]

For any \(A\) supported in sector \(j\), this condition says

\[
U_j^\dagger A U_j=A.
\]

Thus \(U_j\) lies in the commutant of the full matrix algebra on that sector
and is scalar there. The outcome phase cancels in
\(K_j\rho K_j^\dagger\), leaving the Lüders instrument

\[
\mathcal I_j(\rho)=P_j\rho P_j.
\]

So the full action algebra selects the effective Lüders continuation within
this candidate class. It does not explain why that full action algebra is the
physically correct one.

The two-qubit foil makes the dependency concrete. With

\[
P_0=|0\rangle\langle0|\otimes I,\qquad
P_1=|1\rangle\langle1|\otimes I,
\]

compare

\[
K_0=P_0,\quad K_1=P_1
\]

with

\[
\widetilde K_0=|0\rangle\langle0|\otimes X,\qquad
\widetilde K_1=P_1.
\]

The effects and archive are identical. For

\[
H=Z\otimes I+\mu I\otimes Z,
\]

the Lüders channel preserves \(H\), while the twist has exact source-energy
disturbance \(2|\mu|\). At \(\mu=0\), energy cannot see the twist. Full block
actions can.

## Exact residual no-go — microscopic selection

An effective quantum instrument is a set of completely positive selective
maps. Its microscopic unitary realization is not unique. Appending a
different fixed environment state, applying an environment isometry, or
changing an inaccessible dilation can leave every reduced selective map
unchanged.

Therefore:

> No criterion expressed only in the source-to-accessible-archive instrument
> can select one unique microscopic dilation.

This is not a defect in the theorem. It identifies the correct quotient. A
claim about unique apparatus microphysics must add retained environment ports
or another independently accessible discriminator. Otherwise the
operational object is the effective instrument orbit.

## Established-terrain audit

The positive selector is compatible with, and substantially occupied by,
known quantum measurement theory:

- The Wigner--Araki--Yanase line proves that exact projective measurement of
  an observable incompatible with a conserved system quantity is impossible
  under the stated conservation and probe conditions. Kuramochi and Tajima
  give a modern extension to continuous and unbounded conserved observables
  ([paper](https://arxiv.org/abs/2208.13494)).
- Lüders' nondisturbance theorem and its unsharp extensions relate
  nondisturbance to commutativity
  ([Busch and Singh](https://arxiv.org/abs/1304.0054)).
- Quantum-instrument theory explicitly treats the classical outcome and the
  conditional post-measurement state together; experimental instrument
  tomography can detect wrong observables, scrambled records, and wrong
  post-measurement states that a POVM alone misses
  ([Rudinger et al.](https://arxiv.org/abs/2103.03008)).
- Instrument post-processing already studies equivalence classes and
  sequential transformations beyond outcome POVMs
  ([Leppäjärvi and Sedlák](https://arxiv.org/abs/2010.15816)).
- Stinespring dilation freedom and ordinary coherent control absorb any claim
  that the retained-route signal by itself establishes new dynamics.

The present calculation is not a universal WAY bound: it freezes a
degenerate pointer generator and directly evaluates source-action
nondisturbance and coupling symmetry in one complete finite family. The
specific closed form is an elementary specialization of standard dephasing
geometry.

The Dynamic Unity value is architectural and falsification-oriented:

```text
source/action selection
    -> complete selective instrument
    -> archive transduction and decoder
    -> held-out continuation identity
    -> effective-instrument quotient
    -> only then regional descent or finality pricing.
```

Keeping that whole chain unchanged prevents five common false positives:

1. selecting a basis relative to itself;
2. mistaking equal effects for equal instruments;
3. mistaking a pointer record for an accessible record;
4. mistaking an ordinary routed implementation difference for new physics;
   and
5. demanding unique inaccessible microphysics when only an effective
   instrument is operationally identifiable.

## Consequence for the flagship program

This result partially closes the first dependency of `HC-DU-033`.

What has now been earned:

- an exact continuous-family source-action selector;
- a matched conjugate foil;
- a quantitative approximate-alignment bound;
- an exact degeneracy and continuation control;
- an end-to-end archive formula;
- a coherent route assay; and
- the maximal effective-instrument quotient.

What remains open:

1. replace the abstract source action with one independently motivated
   laboratory Hamiltonian or process;
2. impose a genuine additive total-conservation contract with a calibrated
   apparatus asymmetry budget, rather than a degenerate pointer generator;
3. enlarge the candidate coupling class and prove a perturbation-ball bound
   instead of a one-parameter family identity;
4. tomograph the complete selective instrument, not only its outcome
   statistics;
5. freeze an experimentally realistic archive and decoder error model; and
6. only after that, test whether selected local instruments possess a
   nontrivial regional descent or finality law.

The highest-value next physical experiment is therefore not another abstract
record model. It is a conservation- and instrument-tomography assay:

> hold record quality and apparatus asymmetry resources fixed; vary the
> source-axis alignment and a within-sector continuation; reconstruct the
> full instrument and archive channel; test the quantitative disturbance
> surface and the predicted degeneracy reopening.

If ordinary quantum instrument theory explains the entire surface, Dynamic
Unity gains a clean physical interface contract but no new physics. A
reproducible residual outside the complete instrument, environment, and
resource model would be the first legitimate reopener.

## Disposition

- Extend `HC-DU-033`, `HC-DU-035C`, `H-CCR-16`, and `CONCEPT-DU-011` at exact
  finite-control/general-open grade.
- Record a scoped **source-action instrument-orbit selector** and a
  **microscopic-dilation no-go** without creating theorem or hypothesis IDs.
- Do not promote a law, prediction, ontology, paper priority, or Drafting
  Factory state.
- Reopen formed regional descent only after one laboratory-motivated
  instrument survives a total-conservation, perturbation, complete
  instrument-tomography, and end-to-end archive contract.
