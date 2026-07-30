---
title: "Equivariant stochastic interface selection, normalized-orbit boundary, and formed-record gate"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-156
run_id: RUN-20260730-082843-stochastic-interface-selector-gate
work_id: ANOMALY-STOCHASTIC-INTERFACE-SELECTOR
action_id: SIS-01-EQUIVARIANT-STOCHASTIC-SELECTOR-GATE
owner_repo: dynamic-unity
maximum_grade: 4
---

# Equivariant stochastic interface selection

## Executive return

```text
DETERMINISTIC_SELECTOR_IS_INVARIANT_DIRAC_CASE
+ STOCHASTIC_ONLY_SELECTORS EXIST ON COMPACT ORBITS
+ STOCHASTIC SELECTION IS NOT AUTOMATIC OR GENERALLY UNIQUE
+ THE LORENTZ HYPERBOLOID HAS NO NORMALIZED INVARIANT SELECTOR
+ SELECTED KERNEL != REALIZED INTERFACE != FORMED RECORD
+ SAME UNLABELLED CHANNEL, DIFFERENT LABELLED INSTRUMENTS
+ STANDARD COVARIANT-INSTRUMENT AND SSB ABSORPTION
+ NO NEW PHYSICS, PREDICTION, HARDWARE, PAPER, OR READY SUCCESSOR
```

The correction is simple but consequential:

> Symmetry can select a lottery without selecting a winner.

The deterministic selector obstructions already banked by Dynamic Unity
remain correct. They do not, by themselves, exclude an equivariant
probability law over interfaces. Finite and compact symmetry orbits often
admit such laws by averaging. That opens a real intermediate type between a
set-valued orbit and a selected point.

The escape is sharply limited. The invariant law may be nonunique. A
noncompact orbit may admit no normalized invariant probability at all. Even
a unique probability law does not supply the physical sampler, its realized
outcome, a retained carrier, observer access, or certification.

## 1. Typed setup

Let \(G\) act on a physical antecedent space \(X\) and on a bundle of
candidate-interface fibres \(\mathcal I_x\). Choose an orbit representative
\(x\), with stabilizer

\[
H=G_x=\{g\in G:gx=x\}.
\]

Three selector types must be kept apart:

1. a set-valued admissible orbit;
2. a deterministic equivariant section \(s:X\to\mathcal I\); and
3. an equivariant Markov kernel \(K:X\to\mathcal P(\mathcal I)\).

A physical run adds at least three more types:

\[
\text{kernel}
\longrightarrow
\text{sampling instrument}
\longrightarrow
\text{realized interface}
\longrightarrow
\text{retained accessible record}.
\]

The arrows are not definitions. Each needs physical support.

## 2. Stabilizer theorem

### Theorem 1 — deterministic and stochastic selectors

On the orbit \(Gx\):

- equivariant deterministic sections correspond to \(H\)-fixed points in
  \(\mathcal I_x\);
- equivariant Markov kernels correspond to \(H\)-invariant probability
  measures on \(\mathcal I_x\); and
- deterministic selectors are exactly the invariant Dirac cases.

### Proof

An equivariant object on a transitive orbit is determined by its value at
\(x\). If \(gx=g'x\), then \(g^{-1}g'\in H\). The transported point
\(gs(x)\) is therefore well defined exactly when \(s(x)\) is \(H\)-fixed.
The same argument with pushforwards shows that \(g_*\mu_x\) is well defined
exactly when \(h_*\mu_x=\mu_x\) for every \(h\in H\). A probability measure is
a deterministic selector exactly when it is a Dirac mass.

This is standard homogeneous-space/equivariant-kernel mathematics. The
Dynamic Unity result is the correction to its selector ladder.

## 3. Existence, uniqueness, and failure

### Finite and compact positive

If \(H\) is finite and \(\mathcal I_x\) is nonempty, averaging a Dirac mass
over \(H\) gives an invariant probability. If \(H\) is compact and acts
continuously on a compact fibre, normalized Haar averaging does the same.

For a transitive \(C_3\) action on three interfaces, no point is fixed but the
uniform probability is the unique invariant law. Adding an orientation token
selects one point and converts the stochastic-only case into a deterministic
one.

### Nonuniqueness

Symmetry alone need not determine the probability law. If \(C_3\) acts on
two disjoint three-cycles, invariant probabilities form a one-parameter
family: choose mass \(\alpha\) on the first orbit and \(1-\alpha\) on the
second, then distribute uniformly within each. Symmetry selects uniformity
inside each orbit, not the inter-orbit weight.

### No normalized invariant probability

The integer-translation action on \(\mathbb Z\) admits no normalized
translation-invariant probability. Every singleton would have one mass
\(c\). If \(c>0\), sufficiently many points exceed total mass one; if \(c=0\),
countable additivity gives total mass zero.

The physically important analogue is the proper-orthochronous Lorentz action
on the future-unit timelike hyperboloid

\[
H^3=\{u:u^\mu u_\mu=-1,\ u^0>0\}.
\]

There is no normalized Lorentz-invariant Borel probability on \(H^3\).
Every hyperbolic ball of a fixed radius would have one mass \(c\). Infinitely
many disjoint congruent balls force \(c=0\); a countable cover by such balls
then forces the whole space to have mass zero.

Therefore stochastic selection does not rescue a law-only covariant choice
of one inertial observer direction in Minkowski vacuum. The earlier
`HC-DU-033C` obstruction survives in stronger probability-valued form.

## 4. Same channel, different formed-record candidates

Consider two qubit instruments.

Instrument A uniformly samples \(a\in\{X,Y,Z\}\), applies

\[
\Delta_a(\rho)=\frac{\rho+\sigma_a\rho\sigma_a}{2},
\]

and retains \(a\) as a classical label. Its unlabelled channel is

\[
\Phi_A=\frac13(\Delta_X+\Delta_Y+\Delta_Z),
\]

which maps a Bloch vector \(r\) to \(r/3\).

Instrument B records one of \(I,X,Y,Z\), applying the corresponding Pauli
conjugation with probabilities

\[
\left(\frac12,\frac16,\frac16,\frac16\right).
\]

Its unlabelled channel is also \(r\mapsto r/3\).

For input \(\lvert +x\rangle\), Instrument A's conditional \(X+\)
probabilities are

\[
\left(1,\frac12,\frac12\right),
\]

while Instrument B's are

\[
(1,1,0,0).
\]

Both give the erased-label probability \(2/3\). The accessible label
distinguishes their conditional futures; the endpoint channel does not.
Joint cyclic relabeling of axes, state, and readout preserves the statistics,
so this is not a coordinate artifact.

This proves a narrow but exact boundary:

> Selecting an unlabelled covariant channel does not select its labelled
> instrument, archive alphabet, conditional state, or provenance.

## 5. Collision with existing Dynamic Unity results

### `HC-DU-033F`

The antecedent-relative point-selector theorem remains correct. Its ladder
now needs one intermediate rung:

```text
candidate orbit
  -> invariant probability kernel
  -> physical sampler/instrument
  -> realized interface
  -> formed retained record
  -> accessible/certified record
```

The first arrow can close when the point-selector arrow does not.

### `HC-DU-091`

No equivariant MASA point selector does not exclude a covariant POVM,
instrument family, or probability distribution over candidate algebras.
Standard covariant-measurement theory supplies many such objects. It does not
thereby select the sampler, outcome, future-algebra cofiltration, or archive.

### Minkowski observer direction

The correction does not reopen the covariant vacuum observer-direction case.
The relevant orbit is noncompact \(H^3\), so there is no normalized
Lorentz-invariant lottery to sample.

## 6. Absorber audit

The component mathematics is mature:

- invariant measures and Haar averaging;
- equivariant Markov kernels;
- covariant POVMs and instruments;
- Naimark/Stinespring/Kraus realization;
- ergodic decomposition and spontaneous symmetry breaking; and
- ordinary classical randomization.

Haapasalo and Pellonpää classify covariant quantum measurements and
instruments. Decker, Janzing, and Roetteler study implementations of
group-covariant POVMs by orthogonal measurements. Wreszinski and Zagrebnov
make the relevant spontaneous-symmetry-breaking distinction: an invariant
state/ensemble and selection of a pure phase by a limiting asymmetry are
different operations.

The result is therefore not new physics or a new general theorem. Its value
is diagnostic: it prevents DU from overreading deterministic no-selector
results and makes the residual formation obligation exact.

## 7. Grade and disposition

**Earned grade:** scoped Grade 4 theorem/counterexample boundary.

**Not earned:** a source-selected stochastic instrument, a realized event, a
formed record, a certified observer interface, ontology priority, empirical
excess, a prediction, hardware action, or paper promotion.

**Reopener:** one source-pinned physical packet must select the invariant
kernel *and* its sampler/instrument, retain an accessible outcome carrier,
and give a no-refit held-out consequence that differs from every complete
standard-physics absorber. A source-natural proof that a relevant noncompact
interface orbit admits a normalized selector would also reopen the
probability-existence branch.

**Disposition:** bank the selector-ladder correction, keep
`CCR-PHYSICAL-RECORD-INTERFACE-SELECTION` parked, and retain
`NO_READY_SUCCESSOR`.

## Sources

- Haapasalo and Pellonpää, [Optimal covariant quantum
  measurements](https://arxiv.org/abs/2009.14080).
- Decker, Janzing, and Roetteler, [Implementation of group-covariant POVMs by
  orthogonal measurements](https://arxiv.org/abs/quant-ph/0407054).
- Wreszinski and Zagrebnov, [On ergodic states, spontaneous symmetry breaking
  and the Bogoliubov quasi-averages](https://arxiv.org/abs/1607.03024).

## Reproduction

```bash
python3 tests/du_stochastic_interface_selector_gate_probe.py --write-artifact
```

The executable checks the exact finite selector and qubit-instrument controls.
It does not numerically establish the continuous hyperbolic theorem.
