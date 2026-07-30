---
title: "Quantum probability ports, completion odds, and accessible capacity"
status: banked_scoped_result
date: 2026-07-29
claim_id: HC-DU-140
run_id: RUN-20260729-212642-quantum-probability-port-capacity-collision
primary_lane: lane_4
supporting_lanes:
  - lane_3
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
---

# Quantum probability ports, completion odds, and accessible capacity

## Result in one paragraph

The proposed convergence is real at the level of research architecture but
not as a scalar identity. Krhač and Schuller's quantum ports carry the
instantaneous flow of Born probability between a declared additive
decomposition of a unitary quantum system. Norton's completion law relates
thermodynamic entropy increase to the dynamic probability odds of completing
versus reverting a declared molecular-scale process. Dynamic Unity's
reconstruction theorem instead requires accessible mutual information in a
declared source--instrument--transcript--observer protocol. These three
quantities can compose after the whole physical packet is fixed, but none
determines either of the others in general. An exact erasure-family witness
holds the aggregate probability-port history and completion odds fixed while
the accessible information grows as \(s\log d\). Thus probability is a more
natural first boundary coordinate than generic energy in this quantum
decomposition, but “probability” is not one universal physical currency.
`HC-DU-136` is sharpened rather than overturned: the missing object remains a
physically selected map from complete process dynamics to observer-accessible
capacity.

## 1. The proposed convergence

The motivating observation joins three results:

1. quantum port theory replaces classical port-Hamiltonian energy transfer
   with probability transfer;
2. Norton's reliable-completion result is expressed through final-to-failure
   odds; and
3. `HC-DU-136` makes reliability and protocol depth part of the physical
   capacity contract behind a reconstruction floor.

This is an important correction to any attempt to make ordinary energy the
primitive inter-system coordinate. But the strongest sustainable conclusion
is:

> probability supplies several typed boundary coordinates upstream of
> reconstruction; it is not yet one conserved or fungible quantity shared by
> unitary coupling, thermodynamic reliability, measurement, and information.

The scope coordinate is observer-indexed physical access. The process,
apparatus, flow, and formed pointer are ontic physical candidates. Priors,
forecasts, and mutual-information calculations are epistemic tools applied to
that process. No probability object below is cast as source issuance.

## 2. What the probability-port result actually establishes

Krhač's 2023 thesis considers finite-dimensional quantum systems without
translational degrees of freedom. In that arena the Hamiltonian is bounded
and the system's unitary evolution can be decomposed into an additive direct
sum

\[
\mathcal H=\bigoplus_{n=1}^N\mathcal H_n
\]

selected from the representation structure of a materially composite system.
The construction is explicitly different from treating the material tensor
factors as the open subsystems.

For a normalized state

\[
\psi=\bigoplus_n\psi_n
\]

and Hamiltonian blocks \(H_{nm}\), the probability of an affirmative
measurement of membership in \(\mathcal H_n\) is

\[
p_n(t)=\|\psi_n(t)\|^2.
\]

Schrödinger evolution gives

\[
\dot p_n(t)
=
\sum_{m\ne n}J_{n\leftarrow m}(t),
\qquad
J_{n\leftarrow m}
=
2\,\operatorname{Im}
\langle\psi_n,H_{nm}\psi_m\rangle,
\]

with

\[
J_{n\leftarrow m}=-J_{m\leftarrow n}.
\]

The associated real bilinear port pairing
\(2\operatorname{Re}\langle e,f\rangle\) encodes this probability balance.
The interconnection Dirac structure conserves total probability.

Primary source:
[Krhač, *Canonical Dirac structure of unitary quantum dynamics*](https://essay.utwente.nl/96635/).

This is a substantial system-theoretic representation of unitary coupling.
It does **not** by itself supply:

- a thermodynamic entropy current;
- a record, actual outcome, archive, or observer access map;
- a success/failure task;
- a source encoding or decoder;
- accessible mutual information; or
- a physical cost of reliability.

The complete port variables are Hilbert-space valued. Their scalar pairing
records probability flow; it does not count the distinguishable information
carried by internal degrees of freedom.

### Energy correction

The broad slogan “almost all quantum states do not have an energy” should not
be imported as a theorem without qualification.

- A generic state is not an eigenstate of the Hamiltonian and therefore has
  no single sharp energy value.
- The spectral theorem still assigns an energy probability distribution.
- An energy expectation exists when the relevant integrability/domain
  condition holds.
- In the finite-dimensional arena of the probability-port thesis, every
  operator is bounded and every state has a finite energy expectation.

Probability is the natural port variable here because unitary evolution
conserves norm and redistributes direct-sum occupancy. This does not make
energy meaningless or eliminate energy currents, energy-constrained channel
capacities, work, or thermodynamic accounting in correctly typed models.

## 3. The finite-time measurement extension

Krhač, Schuller, and Stramigioli subsequently place the ex ante part of
projective measurement and Schrödinger--Liouville evolution in one
quantum--classical hybrid differential equation:
[“Hybrid Schrödinger-Liouville and projective dynamics”](https://arxiv.org/abs/2504.05532).

Their exactly solvable implementation has

\[
\dot\rho(z,t)
=
\gamma\big(P_z\hat\rho(t)P_z-\rho(z,t)\big),
\]

so that

\[
p(z,t)
=
e^{-\gamma t}p(z,0)
+
(1-e^{-\gamma t})
\operatorname{tr}\!\big(P_z\hat\rho(0)\big).
\]

This is useful for Dynamic Unity because it provides a finite-time classical
pointer-probability process rather than only a terminal projection slogan.
But the paper explicitly:

- starts with a measurement operator \(M=\sum_zm_zP_z\);
- supplies the classical state space \(Z\);
- admits multiple viable implementations;
- chooses an arbitrary positive rate \(\gamma\) for the simplest one;
- requires a read-off time;
- treats the ex ante distribution, not the actual ex post outcome; and
- does not select retention, provenance, access, certification, or finality.

It therefore supplies a candidate middle arrow in a typed process. It does
not select the complete record interface.

The paper's rotating-apparatus example yields finite-time predictions once
the implementation and rate are chosen. Those predictions are not yet a
mechanism-specific Dynamic Unity excess over standard finite-duration
open-system measurement modeling.

## 4. Norton's quantity is narrower than arbitrary probability

Norton's fluctuation argument gives, for the declared thermodynamic process,

\[
\Delta S
=
k_{\rm B}\log
\frac{P_{\rm completion}}{P_{\rm reversion}}.
\]

The relation prices the entropy gradient needed to suppress molecular-scale
thermal fluctuations and make a physical step complete with the declared
odds. It is not a general equation that assigns thermodynamic entropy to
every probability ratio.

Norton's current formulation makes the guard especially explicit. It
distinguishes:

- **dynamic probabilities** realized by a thermal system migrating among
  accessible states; and
- **static probabilities** representing uncertainty about which stable
  memory value is present.

Only after a physical thermodynamic process warrants the dynamic
probabilities may the Boltzmann relation be used in this way. See
[Norton, “Too Good to Be True”](https://doi.org/10.1017/psa.2026.10221).

This guard applies equally to the proposed convergence. A Born probability
flow between Hilbert subspaces, a thermodynamic occupation probability, a
static prior over messages, and a decoder's success probability may all be
written \(p\). They have different physical referents.

## 5. Exact nonfactorization theorem

### Proposition — flow and odds do not determine accessible capacity

Fix any terminal success probability \(s\in(0,1)\). For every integer
\(d\ge2\), construct a protocol with:

- a fixed progress system carrying `ready`, `success`, and `failure` ports;
- a \(d\)-dimensional label system;
- dynamics on the progress system tensored with the identity on the label;
- a uniform input \(X\in\{1,\ldots,d\}\);
- a successful output that reveals \(X\); and
- a failed output equal to one common erasure symbol \(\bot\).

Choose the same progress dynamics for every \(d\). Then:

1. every aggregate progress-port probability \(p_n(t)\) is the same;
2. every aggregate scalar port current \(J_{n\leftarrow m}(t)\) is the same;
3. the terminal completion odds are the same:

   \[
   O=\frac{s}{1-s};
   \]

4. but the accessible mutual information of the complete transcript is

   \[
   I(X;Y)=s\log d.
   \]

The last equality is the capacity of the \(d\)-ary erasure channel with
success probability \(s\) under the uniform input.

Consequently, no finite function of aggregate probability-port flow and
completion odds alone can determine or uniformly upper-bound observer-
accessible capacity across untyped systems:

\[
\mathcal C_\Pi
\ne
F\!\left(J(\cdot),O\right)
\quad\text{universally}.
\]

The witness does not say that complete port signals are uninformative. It
says that the scalar flow and endpoint odds omit the internal alphabet and
the source--measurement--access contract. Supplying the full Hilbert-space
port type, encoding, instrument, and readout can expose the \(d\)-dependence;
that is exactly the typed repair.

### Corollary — Norton odds are not a capacity

The same family keeps \(O\) fixed while \(I(X;Y)=s\log d\) is unbounded in
\(d\). Completion reliability and communicated distinction count therefore
cannot be exchanged. Reliability is one coordinate of the capacity contract,
not the capacity itself.

### Converse separation

The same amount of accessible information may also be implemented through
different progress paths, retry structures, thermal barriers, and completion
odds. Hence capacity does not determine Norton's process cost either.

## 6. The surviving typed composition

The three lines do form one conditional ladder:

```text
selected subsystem decomposition + complete quantum/hybrid dynamics
  -> probability-port signals and outcome transition law
selected source encoding + instrument + read time + retained transcript
  -> conditional outcome distribution p(y|x)
selected success/failure task
  -> completion odds O
selected observer access + decoder + resource contract
  -> accessible information C_Pi(B)
target packing + failure tolerance
  -> HC-DU-136 reconstruction floor
```

Norton supplies an additional thermodynamic inequality only when the
success/failure process is physically realized by the thermal fluctuation
contract his theorem assumes.

This is the positive result. Probability ports may provide the first
dynamical layer that a record-capacity construction needs. The hybrid
measurement work may provide a second. But physics must still select:

- the decomposition and its retained port variables;
- the measurement operator and implementation;
- the actual outcome and archive;
- the source encoding;
- observer access and allowed actions;
- success, failure, reversion, and stopping semantics; and
- the thermodynamic or other resource model.

## 7. What changed for Dynamic Unity

### Strengthened

1. The search for a universal information-to-energy scalar should remain
   stopped.
2. Probability-flow formalisms are a legitimate upstream candidate for
   physically typing a quantum boundary exchange.
3. The next viable positive would be a **port-to-accessible-capacity theorem**,
   not “probability replaces energy.”
4. Norton reinforces the need to preserve complete process history and
   distinguishes dynamically realized probabilities from analyst uncertainty.

### Not earned

- probability as a universal conserved substance;
- a selected record interface;
- a finality-cost law;
- \(\Delta S=k_{\rm B}\log O\) for arbitrary quantum measurement odds;
- an energy-free quantum resource theory;
- a model-selected capacity;
- a physical remainder, empirical excess, new law, or new physics.

### Reopener

Reopen this branch only when one physical theory or apparatus packet
independently selects:

1. the port decomposition or equivalent boundary variables;
2. the source and measurement dynamics;
3. the formed and retained transcript;
4. observer access and task semantics; and
5. a theorem connecting the resulting conditional law to
   \(\mathcal C_\Pi(B)\) without refitting.

A probability-port decomposition, a Born outcome distribution, or a Norton
odds ratio alone does not satisfy the reopener.

## 8. Inline science-council disposition

- **Orthodox professor:** preserve the conditional ladder; quantum continuity,
  channel theory, and stochastic thermodynamics absorb the pieces.
- **Heterodox professor:** probability flow may be the right inter-layer
  coordinate, but only a selected instrument can turn flow into a record and
  capability.
- **Commercial scientist:** the exact erasure witness decides the universal
  claim locally; no simulation or hardware should be funded.
- **Wild-frontier scientist:** finite-time hybrid measurement is the most
  interesting reopener, but its free \(M,\gamma,Z\), and read time currently
  prevent it from selecting a new physical law.
- **Philosopher of science:** Norton's dynamic/static probability distinction
  blocks an ontic--epistemic cast. Shared notation is not shared ontology.

The portfolio remains `NO_READY_SUCCESSOR`.
