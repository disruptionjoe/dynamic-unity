---
title: "Low-amplitude cutoff affine-or-provenance mixture, composition, and steering boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-09-03
claim_id: HC-DU-229
prediction_id: PRED-DU-006
run_id: RUN-20260903-low-amplitude-mixture-composition-and-steering-gate
work_id: LOW-AMPLITUDE-MIXTURE-COMPOSITION-STEERING-GATE
owner_repo: dynamic-unity
primary_lane: lane_7
supporting_lanes:
  - lane_1
  - lane_3
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-EMPIRICAL
evidence_grade: 4
maximum_grade: 4
---

# Low-amplitude cutoff affine-or-provenance boundary

## Executive return

```text
STATE_COMPLETE_FIXED_RESPONSE_REQUIRES_CONVEX_AFFINITY
+ OFFSET_CUTOFF_FAILS_THE_FOUR_PREPARATION_IDENTITY
+ DENSITY_LEVEL_READING_CONFLICTS_WITH_ORDINARY_RANDOMIZATION
+ BRANCHWISE_READING_FAILS_THE_REMOTE_STEERING_GATE
+ PREPARATION_ROUTE_CAN_REPAIR_FACTORING_ONLY_AS_EXTRA_PHYSICAL_STRUCTURE
+ INACCESSIBLE_ROUTE_RECORD_CANNOT_CHANGE_LOCAL_STATISTICS
+ NO_CLICK_AND_POSTSELECTION_CHANGE_THE_OPERATIONAL_CONTRACT
+ CAUSAL_NONLINEAR_THEORIES_ARE_NOT_UNIVERSALLY_EXCLUDED
+ STATE_ONLY_FORM_OF_PRED_DU_006_RETIRED
+ COMPLETE_PROCESS_AND_PROVENANCE_REOPENER_PRESERVED
+ NO_NEW_LAW_ANOMALY_PAPER_HARDWARE_OR_SUCCESSOR
```

`HC-DU-228` established that the literal offset response

\[
f_c(q)=\max(q-c,0),\qquad q=\operatorname{Tr}(P\rho),\quad c>0,
\tag{1}
\]

is not affine in `rho`. This wave asks the question that decides whether that
mathematical excess can be a physical theory: what does (1) mean for mixed
preparations and entangled composite systems?

There is no state-only answer preserving all the ordinary contracts. If a
density operator is the complete local operational state and classical
randomization obeys the law of total probability, every fixed response is
affine. If (1) is instead applied to hidden pure members of an ensemble, two
decompositions of the same density operator become locally distinguishable;
the explicit Bell-state witness then permits a remote measurement choice to
change the local unconditional click rate. If a preparation or detector route
is added to repair the contradiction, that route must be a physically formed,
locally accessible process record. The prediction is no longer a function of
the quantum state alone.

This does **not** prove that every nonlinear quantum theory is impossible.
There are causal proposals and consistent generalized update-rule foils that
alter the state, composition, locality, or measurement contract. It proves a
more useful scoped result: the simple cutoff cannot be promoted from a
one-apparatus pure-profile model to a universal Born-rule modification without
choosing and paying for one of those larger structures.

## 1. The affine-or-extra-state theorem

Let `S` be an operational state space closed under ordinary classical mixing.
Preparing `s_i` with probability `p_i` and discarding the classical label
prepares

\[
s=\sum_i p_i s_i.
\tag{2}
\]

Let `R(s)` be the unconditional probability of a fixed outcome under one
fixed apparatus. If `s` is complete for that response, the law of total
probability requires

\[
R\!\left(\sum_i p_i s_i\right)=\sum_i p_iR(s_i).
\tag{3}
\]

Thus `R` is affine. In quantum mechanics, `R(rho)=Tr(E rho)` for one effect
`0<=E<=I` supplies the familiar realization, but the necessity in (3) is more
general than the Hilbert representation.

A non-affine response has three logically distinct readings:

1. the alleged state is not complete, because the response also depends on a
   preparation, detector, environment, or history variable;
2. ordinary classical randomization or probability composition is changed;
   or
3. the proposed response is not one unconditional fixed-apparatus outcome
   law.

That is the first exact boundary. It does not say which escape Nature uses.
It says that an escape must be typed.

## 2. Smallest fixed-apparatus witness

Use a qubit and `P=|1><1|`. Consider the four pure states

\[
|0\rangle,\quad |1\rangle,\quad
|+\rangle={|0\rangle+|1\rangle\over\sqrt2},\quad
|-\rangle={|0\rangle-|1\rangle\over\sqrt2}.
\tag{4}
\]

The equal `Z` and `X` ensembles have the same state:

\[
{ |0\rangle\!\langle0|+|1\rangle\!\langle1|\over2}
=
{ |+\rangle\!\langle+|+|-\rangle\!\langle-|\over2}
={I\over2}.
\tag{5}
\]

For every fixed effect `E`, linearity gives the exact identity

\[
{p_E(0)+p_E(1)\over2}
=
{p_E(+)+p_E(-)\over2}
=\operatorname{Tr}\!\left(E{I\over2}\right).
\tag{6}
\]

Set `c=1/4` in (1). The proposed responses are

\[
f(0)=0,\quad f(1)=\frac34,\quad
f(+)=f(-)=\frac14.
\tag{7}
\]

Therefore

\[
\bar f_Z=\frac38,
\qquad
\bar f_X=\frac14,
\qquad
\Delta=\frac18.
\tag{8}
\]

This four-pure-preparation equality is the smallest clean empirical contract.
It does not require pretending that a laboratory can prepare an abstract
"density operator directly." It requires one frozen apparatus, four specified
pure inputs, unconditional attempt counts, and no adjustment after observing
the result.

## 3. Why the two natural extensions fail differently

### 3.1 Density-level reading

Suppose (1) acts directly on `rho`. Then

\[
f_c(I/2)=\frac14.
\tag{9}
\]

This is independent of which ensemble decomposition an observer writes down,
so remote steering alone does not signal. But a local randomizer that sends
`|0>` or `|1>` with equal probability has unconditional frequency `3/8` if
the pure-state calibrations in (7) remain valid. The same density operator is
therefore assigned both `1/4` and `3/8`.

One cannot repair this merely by instructing the nonlinear device to act on
the density matrix "after mixing." A physical random sequence of calibrated
pure inputs still has observed frequencies governed by conditional
probability. As Cavalcanti and Menicucci emphasize for verifiable nonlinear
devices, refusing that implication removes the density matrix as a complete
representation of proper mixtures.

The live repair is to add the preparation device, retained randomizer label,
environment, or larger joint state. That can be coherent, but the response is
then not `f_c(Tr(P rho))` alone.

### 3.2 Branchwise or ensemble-member reading

Suppose instead that (1) acts on whichever pure member is physically realized
and local frequencies average those member responses. The `Z` and `X`
decompositions then give the distinct values in (8).

For the Bell state

\[
|\Phi^+\rangle={|00\rangle+|11\rangle\over\sqrt2}
={|++\rangle+|--\rangle\over\sqrt2},
\tag{10}
\]

Alice can choose a `Z` or `X` measurement. With her outcome unread, Bob's
reduced density operator remains `I/2` in both cases. But if Bob's response is
the ensemble-member average, his unconditional frequency is `3/8` after the
`Z` choice and `1/4` after the `X` choice. The nonzero `1/8` contrast is a
superluminal signal under the standard spacelike composite-system contract.

This is the concrete two-basis instance of the Gisin--Polchinski/HJW boundary.
It kills the naive branchwise extension, not every conceivable nonlinear
theory.

## 4. Provenance is a physical repair only when accessible

Let the three preparation routes be

```text
direct density-level assignment
local Z randomizer
local X randomizer
```

They share the same reduced state `I/2` but (under the conflicting extensions)
carry responses `1/4`, `3/8`, and `1/4`. The response therefore does not factor
through the reduced state. Adding a route variable makes formal factorization
possible:

\[
(\rho,\text{route})\longmapsto p.
\tag{11}
\]

DU's record discipline adds the missing physical condition: the route cannot
alter a local detector merely because it exists somewhere in a completion. It
must be retained, transported, and coupled into the detector through an
admissible causal channel. An inaccessible remote steering choice supplies no
such local route record. Letting it change Bob's response is precisely the
signal.

The repair therefore has a useful positive reading. A physically accessible
preparation-history or detector-memory record can make an apparently
state-nonlinear response lawful. But then the phenomenon is a
**process-conditioned record response**, not a state-only Born-rule
modification. `HC-DU-226` supplies the corresponding provenance and support
test.

## 5. Rate, no-click, and postselection typing

Schonfeld's first-droplet expression is initially a nucleation rate density,
not a normalized general measurement law. A cutoff applied to rates can be
completed by an explicit no-click outcome. For two equal candidate outcomes
and `c=1/4`, the two click weights are each `1/4` and the no-click probability
is `1/2`.

Conditioning on a click renormalizes the reported distribution. That can
produce sharp, nonlinear-looking curves while remaining a statement about
selection, finite duration, or detector physics. It does not establish an
unconditional violation. Conversely, declaring the no-click outcome does not
make the branchwise rule affine; the all-attempt frequency contrast in (8)
remains.

Any serious test must consequently keep separate:

- the microscopic event rate;
- the probability of at least one event in a fixed exposure;
- the unconditional outcome alphabet including no-click/rejection;
- the conditional distribution among accepted tracks; and
- the classifier and complete attempt census.

## 6. Literature collision and exact scope

The component mathematics is mature:

- Hughston, Jozsa, and Wootters classify pure-state ensembles with one density
  operator, supplying the general remote-preparation background.
- Polchinski showed the EPR/branch-communication problem for Weinberg-type
  nonlinear quantum mechanics.
- Simon, Bužek, and Gisin derive linear completely positive density-matrix
  dynamics from standard static quantum assumptions plus no signalling.
- Cavalcanti and Menicucci show why empirically verifiable nonlinear evolution
  breaks the usual density-matrix representation of proper mixtures.

The no-go is assumption-relative. Kaplan and Rajendran construct a causal
nonlinear framework by changing the global state/history prescription.
Fiorentino and Weigert exhibit unconventional state-update rules that remain
well defined and no-signalling. Those results prevent the overclaim that any
nonlinearity or any alternative update rule is impossible.

What survives for DU is the exact fork:

| Candidate reading | What it buys | What it costs |
|---|---|---|
| fixed quantum instrument | causal, convex operational law | no literal offset on the declared state family |
| density-level cutoff | decomposition-independent value | ordinary mixture composition fails unless the state is enlarged |
| branchwise cutoff | preserves pure-member rule | remote steering changes local unconditional statistics |
| process/provenance response | can represent route-dependent detector physics | route must be physically formed and accessible; claim is no longer state-only |
| causal nonlinear completion | may retain genuine excess | must specify a new complete state, composition, update, and locality law |

## 7. Disposition of `PRED-DU-006`

The former state-only reading is retired. The expression
`max(Tr(P rho)-c,0)` is not an admissible complete prediction merely by naming
`rho`.

The prediction-shaped seam remains only in this stronger form:

> One source-pinned complete process law specifies preparation, mixed states,
> entangled composites, detector coupling, no-click/rejection, and accessible
> provenance. Under one frozen all-attempt apparatus it predicts a nonzero
> four-preparation contrast (8), while also predicting zero spacelike remote-
> choice contrast and differing from every admitted ordinary quantum process
> without refit.

That is much harder than the original offset, but it is the minimum coherent
claim. A positive would be genuine excess. A null four-preparation contrast
at the preregistered scale kills the simple cutoff. A nonzero remote-choice
contrast kills relativistic no-signalling under the declared composition law.
If the effect factors through an accessible preparation/detector record, it is
a process-dependent interface result and must be assessed at that type.

## 8. Grade, novelty, and next boundary

### Earned

- A scoped Grade-4 affine-or-extra-state necessity theorem.
- An exact four-pure-preparation witness with contrast `1/8` at `c=1/4`.
- An explicit Bell-state steering kill for the branchwise completion.
- A proof that route dependence repairs factorization only by adding physical
  preparation provenance.
- A corrected, complete-process reopener for `PRED-DU-006`.

### Not earned

- No universal no-go against nonlinear quantum mechanics.
- No proof that Schonfeld's detector mechanism is false.
- No physically selected nonlinear law or value.
- No observed Born-rule violation or superluminal signal.
- No DU-original component theorem, paper seed, hardware action, or ready
  successor.

The highest-information next evidence would be a source-owned complete
mixed/composite rule. Without it, more curve fitting or detector simulation
cannot change the classification. The portfolio remains `no_ready`.

## Sources

- Schonfeld, [The first droplet in a cloud chamber
  track](https://arxiv.org/abs/2106.05178).
- Hughston, Jozsa, and Wootters, [A complete classification of quantum
  ensembles having a given density matrix](https://doi.org/10.1016/0375-9601(93)90880-9).
- Polchinski, [Weinberg's nonlinear quantum mechanics and the
  Einstein--Podolsky--Rosen paradox](https://doi.org/10.1103/PhysRevLett.66.397).
- Simon, Bužek, and Gisin, [No-signaling condition and quantum
  dynamics](https://doi.org/10.1103/PhysRevLett.87.170405).
- Cavalcanti and Menicucci, [Verifiable nonlinear quantum evolution implies
  failure of density matrices to represent proper
  mixtures](https://arxiv.org/abs/1004.1219).
- Kaplan and Rajendran, [Causal framework for nonlinear quantum
  mechanics](https://doi.org/10.1103/PhysRevD.105.055002).
- Fiorentino and Weigert, [Beyond the projection postulate and back: Quantum
  theories with generalized state-update
  rules](https://doi.org/10.1103/2zpm-jsh7).

## Reproduction

```bash
python3 tests/du_low_amplitude_mixture_steering_gate_probe.py --write-artifact
```

The probe checks only the exact finite ensemble identity, cutoff contrast,
Bell-state steering witness, route-factorization repair, and no-click typing.
It does not simulate a detector or establish a physical anomaly.
