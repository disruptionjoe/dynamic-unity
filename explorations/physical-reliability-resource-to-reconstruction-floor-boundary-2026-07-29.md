---
title: "Physical reliability, resource capacity, and the finite reconstruction floor"
status: banked_scoped_result
date: 2026-07-29
claim_id: HC-DU-136
run_id: RUN-20260729-192647-physical-reliability-reconstruction-floor
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
---

# Physical reliability, resource capacity, and the finite reconstruction floor

## Result in one paragraph

The proposed resource-floor inversion is mathematically valid but does not
possess a universal information-to-energy bridge. For a physically admitted
completion class, target pseudometric, protocol class, and resource contract,
let \(M_T(2\delta)\) be a finite \(2\delta\)-packing of held-out target values
and let \(\mathcal C_\Pi(B)\) upper-bound the information accessible to every
admissible protocol with resource at most \(B\). Any protocol that reconstructs
the target to error \(\delta\) with failure probability at most \(\epsilon\)
must satisfy

\[
\mathcal C_\Pi(B)
\;\ge\;
\log M_T(2\delta)-h_2(\epsilon)
-\epsilon\log\!\big(M_T(2\delta)-1\big).
\]

This is the exact capacity-to-resolution bridge. Fano/minimax and
rate-distortion theory absorb its mathematical core. Its physical content
comes entirely from independently selecting the completion class, target
metric, admissible protocols, resource vector, budget, and capacity bound.
Neither \(k_{\rm B}T\log2\), ordinary energy, expected heat, single-run
entropy production, duration, detector count, nor success probability alone
supplies that selection. Norton and mainstream Landauer results can be
simultaneously correct because they constrain differently typed parts of a
physical implementation. A further load-bearing asymmetry is now explicit:
published thermodynamic reliability work can use
\(D(\gamma\Vert\rho)\), while `HC-DU-134` requires
\(D(\rho\Vert\gamma)\); `HC-DU-134` already proves that the reverse
orientation does not activate its uniform carrier. The campaign therefore
continues through one exact metastable-record specimen that must derive the
operative divergence and capacity from its dynamics rather than choose them.

## 1. Question and evidence consumed

`HC-DU-095` proves that a compact physically admitted class with a separating
measurement family admits some finite certificate at every fixed nonzero
target resolution. `HC-DU-097` shows that compactness alone supplies no packet
count, margin, algorithm, or cost; in its Sobolev specimen the relevant metric
entropy grows as a power of inverse resolution. The Runtime mailbox proposed
inverting that ladder:

> combine a lower bound on the number of distinctions required at resolution
> \(\delta\) with a physical resource budget, then infer a nonzero resolution
> floor.

`HC-DU-135` supplies the immediate hostile control. Norm, success probability,
and arbitrary ordinary energy do not generally select its forward-relative-
entropy state family. Only the same split modular-energy budget, a genuine
Gibbs specialization, or a proved comparison
\(K_\sigma\le aH+bI\) does.

The present question is therefore not whether a counting argument can be
written. It is:

> Which physically selected resource constrains the number of target
> distinctions an actual observer protocol can reliably establish?

The scope coordinate is observer-indexed physical access. The record and
apparatus are ontic physical systems; the use of a prior in a minimax proof is
an epistemic proof device, not an ontology. Nothing in the result bears on
source issuance.

## 2. Primary-source and absorber collision

### 2.1 Norton and Myrvold do not force a binary choice

Norton's fluctuation argument prices reliable completion of the physical steps
used by a molecular-scale implementation. For a completion-to-reversion odds
ratio \(O\), his Boltzmann argument gives an entropy difference
\(k_{\rm B}\log O\), and a compound implementation must price the steps whose
successful completion it requires.

Myrvold proves a Landauer-type result without suppressing fluctuations, but
his manipulated-system accounting deliberately sets aside entropy generated
by external systems that drive the Hamiltonian changes. Myrvold and Norton
later state jointly that the analyses are compatible:
[“On Norton's ‘...Shook...’ and Myrvold's ‘Shakin'...’”](https://doi.org/10.31389/pop.81).

Consequently:

- a Landauer expectation bound inside the manipulated system;
- fluctuation-suppression costs in the controller or driver;
- single-run completion odds;
- retries, stopping time, and correlated stages; and
- total apparatus work and entropy production

are not interchangeable estimates of one universal scalar. The step
decomposition is itself part of the physical protocol and cannot be inferred
from the logical function.

### 2.2 Landauer identities are process-typed, not record-capacity laws

Reeb and Wolf start with a system, an initially thermal reservoir, an initial
product state, and a joint unitary. Their equality form resolves the reservoir
heat into the system entropy decrease plus final mutual information and
reservoir relative entropy; finite reservoirs give explicit positive
corrections:
[“An improved Landauer Principle with finite-size corrections”](https://arxiv.org/abs/1306.4352).

This is a strong theorem about that physical process. It is not an upper bound
on how many target distinctions an arbitrary observer can acquire for a given
heat budget.

Sagawa and Ueda make the typing sharper. Measurement work and erasure work
trade against memory free-energy changes; neither measurement alone nor
erasure alone has one universal lower work bound, while their declared cycle
obeys a mutual-information-dependent bound:
[“Minimal Energy Cost for Thermodynamic Information Processing”](https://arxiv.org/abs/0809.4098).

Thus \(k_{\rm B}T\log2\) cannot be attached directly to “one formed bit.” It
prices a special symmetric erasure contract, not physical occurrence,
measurement, retention, certification, or observer access in general.

### 2.3 Reliability already has multiple inequivalent information measures

Janzing, Wocjan, Zeier, Geiss, and Beth formulate the thermodynamic worth of a
resource for reliable erasure through distinguishability from equilibrium.
Their reliability bound uses the orientation
\(D(\gamma\Vert\rho)\), rather than the free-energy orientation
\(D(\rho\Vert\gamma)\):
[“The thermodynamic cost of reliability and low temperatures”](https://arxiv.org/abs/quant-ph/0002048).

That orientation difference is decisive in Dynamic Unity. `HC-DU-134` proves
uniform finite compression only for a forward ball
\(D(\rho\Vert\sigma)\le D_0\), and supplies an exact tail-escaping family with
bounded \(D(\sigma\Vert\rho)\). “Reliability is relative-entropic” therefore
does not by itself connect reliability to DU's existing modular carrier.

Finite-time stochastic thermodynamics adds duration, activity, control, and
subsystem trade-offs rather than collapsing them into one number; see
[Kamijima, Funo, and Sagawa](https://arxiv.org/abs/2409.08606). Quantum
estimation likewise separates multi-shot expected work and Fisher information
from single-shot deterministic work and confidence intervals; see
[Lipka-Bartosik and Demkowicz-Dobrzanski](https://arxiv.org/abs/1805.01477).

### 2.4 Physical energy constrains capacity only after a channel contract

Energy-constrained quantum-channel capacity is well defined after the channel,
energy observable, input constraint, coding task, error mode, and asymptotic
contract are fixed. Even general capacity theorems require spectral conditions
such as a Gibbs condition and finite output entropy; see
[Wilde and Qi](https://arxiv.org/abs/1609.01997).

This is the closest positive absorber for the intended campaign. It confirms
the right architecture:

\[
\text{physical protocol and resource constraint}
\longrightarrow
\text{capacity bound}
\longrightarrow
\text{resolution floor}.
\]

It does not select the first arrow.

## 3. Proposition A — no energy-only information capacity

There is an exact finite counterexample to any cross-system claim that an
ordinary energy budget alone bounds accessible information.

For each \(d\), take a \(d\)-dimensional system with

\[
H_d=0.
\]

Prepare one of \(d\) orthogonal states and measure in that basis. Every state
has energy zero, while the one-use accessible information is \(\log d\).
Hence no finite function of ordinary energy alone upper-bounds accessible
information uniformly over system dimension, algebra, apparatus, and
measurement class.

This does not construct a zero-resource physical memory. It exposes exactly
which resources were omitted: dimension or phase-space volume, preparation,
control, measurement, localization, duration, support, and reset. Adding
those resources repairs the statement by retyping it, not by defending
energy as the universal scalar.

The same logic blocks duration alone through parallelization, detector count
alone through multivalued outcomes, and success probability alone through
arbitrarily informative deterministic channels. A useful resource contract
is generally a typed vector, not a natural scalar:

\[
B=(E,W,Q,\Sigma,\tau,n_{\rm use},\text{support},
\text{control},\text{memory},\epsilon,\ldots).
\]

One scalar may emerge in a frozen model. It is not universal before that
model is selected.

## 4. Proposition B — exact conditional capacity-to-resolution theorem

Let:

- \(\mathcal M_{\rm phys}\) be a physically admitted completion class;
- \(T:\mathcal M_{\rm phys}\to\mathcal Y\) be a held-out target;
- \(d_T\) be a declared target pseudometric;
- \(\Pi_B\) be all physically admissible protocols under resource budget \(B\);
- \(Y_\pi\) be the complete accessible transcript of protocol \(\pi\); and
- \(\mathcal C_\Pi(B)\) satisfy

\[
\sup_{\pi\in\Pi_B} I(X;Y_\pi)\le\mathcal C_\Pi(B)
\]

for every finite hypothesis variable \(X\) in the declared protocol model.

Choose \(m_1,\ldots,m_M\) whose target values form a strict
\(2\delta\)-packing:

\[
d_T(T(m_i),T(m_j))>2\delta
\qquad(i\ne j).
\]

Give their labels a uniform proof prior \(X\). Any estimator whose target
error is at most \(\delta\) determines the correct packing label, because two
packing points cannot both lie within \(\delta\) of its output. If its worst-
case failure probability is at most \(\epsilon\), its average label error
under this prior is at most \(\epsilon\). Fano's inequality gives

\[
H(X\mid Y_\pi)
\le
h_2(\epsilon)+\epsilon\log(M-1),
\]

and therefore

\[
I(X;Y_\pi)
\ge
\log M-h_2(\epsilon)-\epsilon\log(M-1).
\]

Consequently:

### Capacity-to-resolution necessity

\[
\boxed{
\mathcal C_\Pi(B)
\ge
\log M_T(2\delta)
-h_2(\epsilon)
-\epsilon\log\!\big(M_T(2\delta)-1\big)
}
\]

is necessary for uniform \(\delta\)-reconstruction with failure at most
\(\epsilon\).

A weaker convenient form is

\[
\mathcal C_\Pi(B)
\ge
(1-\epsilon)\log M_T(2\delta)-\log2.
\]

Because the uniform prior is used only to lower-bound worst-case error, this
does not posit an ensemble ontology or turn ignorance into thermodynamic
entropy.

Define the conditional floor

\[
\delta_{\rm floor}(B,\epsilon)
=
\inf\left\{
\delta>0:
\log M_T(2\delta)
\le
\frac{\mathcal C_\Pi(B)+\log2}{1-\epsilon}
\right\}.
\]

Every smaller resolution is impossible under the frozen contract.

## 5. What the theorem does and does not earn

### It earns

1. the exact mathematical form of the resource-floor inversion;
2. a proof that the bridge variable is accessible protocol information, not
   logical bit count;
3. a no-go on ordinary energy as a universal cross-system capacity scalar;
4. a reconciliation of Norton and Landauer accounting through type
   separation;
5. an exact relative-entropy-orientation warning connecting reliability work
   to `HC-DU-134`; and
6. the minimum physical input the next swing must derive:
   \(\mathcal C_\Pi(B)\).

### It does not earn

- a physical completion class, apparatus, protocol, resource meter, budget,
  record, archive, target, or observer;
- a universal thermodynamic price for information;
- a claim that inability to estimate is ontological incompleteness;
- a same-certified-record/different-target Grade-5 remainder;
- a type-III Landauer theorem;
- a modular-to-physical-energy comparison;
- empirical excess, a new law, or new physics.

An operational floor becomes a North-Star physical remainder only after the
resource and protocol boundary is independently physical, the record is
formed and accessible, and a target difference survives every admitted
protocol rather than merely a chosen measurement.

## 6. Five-swing campaign after the audit

The audit completes the originally proposed first swing and the abstract
theorem portion of the second. The remaining sequence is gated:

| phase | question | positive return | stop |
|---|---|---|---|
| 1 — complete | Is there a universal resource scalar, and what theorem connects a physical capacity to target resolution? | Conditional Fano floor; no universal scalar | Complete at `HC-DU-136` |
| 2 — executable | In one exact metastable record apparatus, which resource and divergence orientation actually control finite-time reliability and acquired information? | Model-selected \(\mathcal C_\Pi(B)\) | Stop if the cost or protocol is fitted rather than dynamical |
| 3 — conditional | Does the unchanged resource/capacity contract transfer to one quantum measurement or estimation specimen? | Quantum transfer without refit | Stop on task-specific redefinition |
| 4 — conditional | Does the selected physical resource control the same split modular object used by `HC-DU-134`? | Proved \(K_\sigma\)-to-physical-resource bridge | Stop on wrong object or orientation |
| 5 — conditional | Does the formed record determine one held-out physical target to the floor, and where is the first leak? | Quantified physical remainder or reconstruction | Stop on law-only explanation, supplied interface, or target refit |

Only phase 2 is selected now.

## 7. Exact next action

Use the smallest continuous-time two-state metastable memory satisfying local
detailed balance, with:

- an explicit blank/equilibrium state;
- a source-conditioned drive;
- a finite write interval and stopping rule;
- success, failure, and retry events retained;
- an explicit controller-work and entropy-production ledger;
- a readout channel and complete transcript;
- one binary held-out target; and
- no reset charge unless reset is part of the declared task.

Derive rather than assume:

1. the exact success/error curve;
2. which forward, reverse, symmetric, or path-space divergence controls it;
3. the mutual information available to the observer;
4. the dependence on work, entropy production, duration, activity, and
   retries; and
5. the resulting \(\mathcal C_\Pi(B)\), if one exists.

### Positive control

A fixed local-detailed-balance protocol yields an exact, independently
calculated resource-to-error or resource-to-information curve.

### Cheapest kill

Two admissible protocols share the proposed scalar budget and reliability but
have different accessible capacities, or the claimed resource bound depends
on an externally chosen step decomposition.

### Local-learning disposition

Begin analytically. A minimal local computation is admitted only if it finds
an exact phase boundary or hostile protocol not already supplied by the
literature and direct proof. External hardware is unavailable and unnecessary.

## 8. Grade and disposition

### Scoped Grade 4

- no ordinary-energy-only universal capacity;
- exact conditional capacity-to-resolution necessity;
- resource, reliability, and relative-entropy orientation boundaries.

### Conditional Grade 3

The theorem reconstructs a finite-resolution impossibility boundary only after
a physical protocol and its capacity are supplied. No such physical
selection is earned here.

### Disposition

```text
NO_UNIVERSAL_RESOURCE_SCALAR
+ NORTON_AND_LANDAUER_CONSTRAIN_TYPED_DIFFERENT_OBJECTS
+ ABSTRACT_RESOURCE_FLOOR_ABSORBED_BY_FANO_AND_CAPACITY_THEORY
+ EXACT_CAPACITY_TO_RESOLUTION_THEOREM
+ RELIABILITY_RELATIVE_ENTROPY_MAY_HAVE_WRONG_ORIENTATION
+ MODEL_SPECIFIC_CAPACITY_SPECIMEN_SELECTED
+ NO_PHYSICAL_REMAINDER_YET
```
