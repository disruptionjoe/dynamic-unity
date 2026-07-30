---
title: Non-Markovian collapse/Bohmian system-control naturality and process-completion boundary
date: 2026-07-30
claim_id: HC-DU-144
evidence_grade: 4
status: banked_scoped_result
programs:
  - CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR
  - CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
---

# Non-Markovian collapse/Bohmian system-control naturality and process-completion boundary

## Result

`HC-DU-143` left one exact reopener: perhaps an active intervention on the
system would separate a non-Markovian stochastic collapse trajectory from its
deterministic Tilloy--Wiseman Bohmian system-plus-bath completion.

The smallest nontrivial active family does **not** separate them.

> One antecedently fixed bath/noise map is natural across every finite
> sequence of instantaneous system-only unitaries. It also remains natural
> when each unitary is selected causally from an already matched record
> prefix, conditional on a supplied common controller. The conditioned
> wavefunction, mapped local beable, record, and record-mediated response stay
> equal without refitting the bath, noise kernel, or hidden initial
> condition.

The result does not extend from a bare uncontrolled trajectory to arbitrary
instruments by logic alone. A trajectory or family of one-time dynamical maps
is not an interventionally complete non-Markovian process. A process tensor,
quantum comb, influence functional with inserted operations, or equivalent
joint system--environment dilation is required.

Once both descriptions inherit the **same** process tensor from the common
bath dilation, all system-side instrument statistics agree by construction.
That closes ordinary system control as an empirical first leak. The first
possible physical differences must alter or reach structure outside the
common process: the bath/hidden variables, collapse kernel or operators,
system--bath boundary, symmetry/covariance realization, stable
bounded-below implementation, or complete resource contract.

## Claim and grade

`HC-DU-144` earns **scoped Grade 4** for:

1. exact naturality of the Tilloy--Wiseman path correspondence under finite
   system-only unitary pulse sequences;
2. conditional extension to matched-record feedback without interface refit;
3. exact necessity of an interventionally complete process object before
   inferring arbitrary active capability from an uncontrolled trajectory;
4. a smallest same-uncontrolled-history/different-intervention-response
   counterexample; and
5. relocation of the first admissible leak outside the common system process.

The mathematical components are established conditional-wavefunction,
open-system, causal-model, and process-tensor results. DU's increment is their
typed composition into the record/issuance/capability question. This is not a
new physical law, universal collapse/Bohmian equivalence, ontology theorem,
empirical discriminator, prediction, or new physics.

## Frozen packet

Hold fixed:

\[
\mathcal P=
(\mathcal H_S,\{A_k\},D,\gamma,\mathcal H_B,H_B,\kappa,
 |\psi_0\rangle\otimes|0_B\rangle,F_0,K,\Pi).
\]

Here:

- \(A_k\) are the collapse/system--bath coupling operators;
- \(D_{jk}(t,s)\) is the colored-noise kernel;
- \(H_B,\kappa,|0_B\rangle\) define the Tilloy--Wiseman oscillator bath;
- \(F_0:x(0)\mapsto w^{[0]}\) is the fixed initial bath-coordinate-to-noise
  map;
- \(K\) is the unchanged downstream record/archive channel; and
- \(\Pi\) is a declared causal feedback policy, if used.

The permitted control alphabet is a finite set of unitary operators acting on
\(\mathcal H_S\) only. Pulse times are fixed in advance or are stopping times
with respect to the matched record prefix. No control acts directly on
\(\mathcal H_B\), changes \(A_k,D,\kappa\), or moves the system--bath
boundary.

## The source structure

Tilloy and Wiseman construct a bath for a generic colored-noise collapse
model:

- Antoine Tilloy and Howard M. Wiseman, “Non-Markovian wave-function collapse
  models are Bohmian-like theories in disguise,” *Quantum* **5**, 594 (2021),
  [arXiv:2105.06115](https://arxiv.org/abs/2105.06115).

Their interaction is

\[
H_{\mathrm{int}}
=
\sqrt\gamma\sum_k A_k\otimes
\int_{\mathbb R}d\omega\,
\kappa^\ell_{k,\omega}\,p_{\ell,\omega}.
\]

The initial bath coordinates determine a Gaussian field with covariance
\(D\), and the live Bohmian bath coordinates satisfy

\[
\frac{d}{dt}w_k(x(t),s)
=2\sqrt\gamma\,D_{kk'}(t,s)\langle A_{k'}\rangle_t.
\]

This is the same update as the collapse model's redefined noise. Their
equation (60) consequently gives the pathwise identity

\[
\psi^B_{x(t)}(t)=\psi^C_{w^{[t]}}(t).
\]

The initial map \(F_0\) depends on the bath coordinates and fixed coupling,
not on a later system-only pulse.

## System-control naturality theorem

### Statement

Suppose the pathwise identity holds immediately before a pulse at time
\(\tau\). Apply the same unitary \(U\) to the system in both descriptions:

\[
\Psi^B(\tau^+)=(U\otimes I_B)\Psi^B(\tau^-),
\qquad
\psi^C(\tau^+)=U\psi^C(\tau^-).
\]

Then:

1. the Bohmian bath coordinate \(x(\tau)\) is unchanged by the instantaneous
   system-only pulse;
2. \(F_0(x(0))\) is unchanged;
3. the conditional wavefunction remains equal across the pulse; and
4. the subsequent bath/noise update equations restart from equal data.

Therefore the pathwise correspondence persists after the pulse. By finite
induction it persists across every finite pulse sequence in the frozen
alphabet.

### Proof

The load-bearing square is

\[
\langle x|(U\otimes I_B)|\Psi\rangle
=
U\langle x|\Psi\rangle.
\]

Normalization commutes with \(U\), so

\[
\psi^B_x(\tau^+)=U\psi^B_x(\tau^-)
=U\psi^C_w(\tau^-)=\psi^C_w(\tau^+).
\]

The pulse acts on no bath canonical variable and therefore does not change
\(x(\tau)\) instantaneously or the fixed initial map \(F_0\). After the
pulse, the Bohmian field update and collapse-noise redefinition both use the
same expectation values \(\langle A_k\rangle_t\) in the now-equal conditional
states. Under the same fixed equations, uniqueness carries equality to the
next pulse. Induction completes the result.

This proof needs no new bath for each \(U\). The relevant naturality square is
the conditional projection identity above: system-unitary action before
conditioning equals system-unitary action after conditioning. Such squares
compose for \(U_n\cdots U_1\), while \(F_0\) itself never changes.

## Record-adapted feedback

Let \(R_{<\tau}=K(Z_{<\tau})\) be the matched record prefix and let

\[
U_\tau=\Pi_\tau(R_{<\tau})
\]

for one antecedently fixed causal policy \(\Pi\). If \(K\) is deterministic,
the two sides have the same record prefix pathwise. If \(K\) is stochastic,
use the same antecedently fixed auxiliary seed to couple its equal conditional
laws; without choosing a coupling, the conclusion is equality in feedback
response law rather than token-by-token identity. In either case the same
record selects the same \(U_\tau\), so the preceding pulse proof applies
branch by branch. Finite induction proves the corresponding equality under
the complete feedback policy.

This is an active capability result, but it is conditional on a supplied
controller that:

- sees only the matched record;
- implements the same system-local pulse;
- has one fixed policy and resource contract; and
- does not itself open a new bath-facing channel.

It does not select a controller, archive, policy, or energy budget in nature.

## Why arbitrary instruments require more structure

A generic intervention can prepare, measure, discard, replace, or couple an
ancilla. In a non-Markovian process, the future can depend on correlations
carried by the environment across that intervention. The instantaneous system
state—even a complete history of its uncontrolled states—does not by itself
specify those counterfactual responses.

Pollock et al. formalize the required object as a process tensor, a multilinear
map from a sequence of system operations to the final conditional state:

- Felix A. Pollock et al., “Non-Markovian quantum processes: complete
  framework and efficient characterisation,”
  [arXiv:1512.00589](https://arxiv.org/abs/1512.00589).
- Felix A. Pollock et al., “Operational Markov condition for quantum
  processes,” [arXiv:1801.09811](https://arxiv.org/abs/1801.09811).

The process tensor is operationally complete for the declared system-side
instrument class. It is equivalent, nonuniquely, to a joint open-system
evolution with an environment. It keeps the environmental influence fixed
while experimenters vary the system operations.

The Tilloy--Wiseman bath supplies exactly such a joint completion. If a
declared instrument family is implemented entirely on the system side of that
**same** completion—possibly using ancillas placed inside \(\mathcal H_S\)
before the packet is frozen—then both descriptions inherit one process
tensor. Every joint instrument-outcome law agrees. This operational equality
is stronger than the pulse theorem, but it comes from the common process
completion, not from the bare stochastic trajectory.

The type distinction is:

```text
one uncontrolled stochastic/conditional path
    != a family of one-time reduced maps
    != an interventionally complete process tensor
    != a physically selected instrument and archive.
```

## Smallest trajectory-only counterexample

Three times and one classical bit suffice to prove that an uncontrolled path
does not select its intervention extension.

Let \(X_0\) be a uniformly random bit. Both processes have the same
uncontrolled history:

\[
(X_0,X_1,X_2)=(X_0,X_0,X_0).
\]

At time \(1\), permit an intervention that flips the visible bit.

- **Current-state process \(P\):** after the intervention,
  \(X_2=X_1^{\mathrm{post}}\).
- **Hidden-memory process \(Q\):** after the intervention,
  \(X_2=X_0\), restored from an inaccessible memory.

With no intervention, every trajectory and every passive record agrees. With
the flip:

\[
X_2^P=1-X_0,
\qquad
X_2^Q=X_0.
\]

The response distributions are disjoint. Thus identity-control path equality
does not determine an active process.

Pollock et al. provide the quantum positive control: a qubit can have
CP-divisible unperturbed reduced dynamics while an intermediate \(X\) pulse
produces an echo by exposing environmental memory. The pulse does not refute
the open-system theory; it shows why unperturbed maps are not the process.

## What the intervention test actually decided

| Proposed first leak | Verdict | Reason |
|---|---|---|
| Fixed system-only unitary pulse | Closed | Conditional projection commutes with \(U\otimes I_B\); \(F_0\) is unchanged. |
| Finite system-only pulse sequence | Closed | Induction and composition. |
| Feedback selected from matched record | Closed conditionally | Equal record prefixes select equal pulses under one supplied policy. |
| Arbitrary system instrument inside one frozen common dilation | Operationally closed | Both descriptions inherit the same process tensor. |
| Instrument response inferred from the uncontrolled trajectory alone | Invalid inference | The three-bit witness gives different active extensions of one path law. |
| Direct bath or hidden-variable intervention | Completion-facing open seam | It exits the common system process. |
| Changing \(A_k,D,\kappa\), or the system--bath boundary | Retyped packet | It is not a no-refit discriminator. |
| Symmetry/covariance implementation | Open physical seam | The common mathematical bath may not meet the same fundamental symmetry contract. |
| Stable bounded-below exact realization | Open physical seam | The source's convenient two-sided-frequency bath is not bounded below. |
| Complete implementation resources | Open physical seam | Operational equality does not imply equal physical realization cost. |

## The more important reopener

The intervention route closes farther than `HC-DU-143` established. The
highest-information next question moves to physical realizability:

> Can the exact path/process correspondence be realized by one stable,
> bounded-below, symmetry-respecting bath under a frozen finite-resource
> contract, or does every such realization introduce a quantitative
> observer-accessible remainder?

This is not merely aesthetic. The exact source construction uses positive and
negative frequency modes and notes that its convenient bath Hamiltonian is
not bounded below. A more physical bounded-below bath makes the noise
band-limited; the resulting history is analytic and its future can be
approximated from derivatives. The source also identifies Lorentz symmetry as
a potential empirical seam.

That is now a better candidate than trying more ordinary system controls.
System controls live inside the shared process. Stability, covariance, and
resource realization ask whether the shared process is physically admissible
as fundamental structure.

## Absorbers, kills, and non-promotions

### Strongest absorbers

- conditional-wavefunction covariance under system-local unitaries;
- oscillator-bath and Stinespring dilation;
- influence functionals;
- process tensors and quantum combs;
- causal-break diagnostics; and
- ordinary counterfactual nonidentifiability.

### Exact kills

1. A system-only pulse is not a discriminator: the path equality commutes
   through it.
2. Record-adapted feedback is not a discriminator when the same matched
   record selects the same system-local action.
3. A bare trajectory cannot support a universal active-capability claim.
4. A process-tensor difference obtained by changing the bath or boundary is a
   changed packet, not excess within the original comparison.

### What is not earned

- no proof that every conceivable intervention is system-local;
- no pathwise theorem for arbitrary selective instruments without their
  dilation;
- no unique process tensor selected by the stochastic trajectory;
- no physical selection of the common bath;
- no stable relativistic realization;
- no ontology priority;
- no empirical excess or prediction; and
- no new physics.

## Plain English

We tried the most obvious way to tell the two stories apart: actively kick the
quantum system instead of merely watching it.

That does not work. If we apply the same kick to the system, the deterministic
bath story and the stochastic-collapse story remain synchronized. If the next
kick is chosen from a record they both produced, they remain synchronized
again.

But this taught us something important about what “the same behavior” must
mean. A movie of what happened when we did nothing does not tell us what would
happen under every possible intervention. For that we need the full
counterfactual process—how the environment carries memory and responds to
each allowed operation. The common bath can supply that process, and once we
use it, ordinary system experiments still cannot separate the two stories.

So the next serious opening is not another control pulse. It is whether the
shared hidden bath can be made physically respectable—stable, bounded below,
relativistically acceptable, and resource-accounted—without losing the exact
equivalence. That is where a real physical difference could begin.

## Disposition

`ACTIVE_SYSTEM_CONTROL_DUALITY_AND_PROCESS_COMPLETION_ABSORPTION`.

No successor is activated. The predictive-issuance program remains complete
and `CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR` remains parked. Reopen on
an exact stable/bounded-below/covariant realization audit or on an action that
physically reaches beyond the common system process without changing the
frozen packet after the fact.
