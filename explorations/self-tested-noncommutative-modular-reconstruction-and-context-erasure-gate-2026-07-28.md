---
title: "Self-tested noncommutative modular reconstruction and context-erasure gate"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-078
run_id: RUN-20260728-121120-self-tested-modular-reconstruction
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260728-121120-self-tested-modular-reconstruction/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-121120-self-tested-modular-reconstruction/run-receipt.md"
owner_repo: dynamic-unity
---

# Self-tested noncommutative modular reconstruction

## Executive result

`HC-DU-077` closed a static route:

```text
complete state on one commutative record algebra
  -/-> nontrivial ambient modular flow.
```

It did **not** prove that classical records can never reconstruct
noncommutative structure. This swing finds the exact conditional positive.

In a Bell experiment, the record object is not merely an unlabeled list of
outcomes. It is a family of conditional probabilities

\[
p(a,b\mid x,y)
\]

whose input labels \(x,y\), output labels \(a,b\), party separation, and
cross-party compatibility have declared operational meanings.

For the tilted-CHSH family, maximal quantum correlations self-test a
partially entangled two-qubit state and the relevant measurements up to a
local isometry and auxiliary degrees of freedom. The extracted local factor
is noncommutative, and for a nonmaximally entangled target its reduced state
is faithful and nontracial. Its target-factor modular spectrum is therefore
nontrivial.

At the exact point \(\theta=\pi/8\), the labeled classical correlation table
conditionally reconstructs:

\[
\rho_A
=
\begin{pmatrix}
(2+\sqrt2)/4&0\\
0&(2-\sqrt2)/4
\end{pmatrix},
\qquad
\frac{\lambda_0}{\lambda_1}=3+2\sqrt2.
\]

Hence the extracted factor's modular action has the exact off-diagonal phase

\[
\sigma_t^{\rho_A}(|0\rangle\langle1|)
=
(3+2\sqrt2)^{it}|0\rangle\langle1|.
\]

This is a real reconstruction result, but its type is conditional:

```text
supplied Bell ports and labels
  + supplied quantum/commutation contract
  + exact labeled conditional law
    -> self-tested target factor and state up to operational gauge
    -> target-factor modular data
    -/-> selected physical interface
    -/-> full ambient modular flow
    -/-> calibrated time or geometry.
```

The hostile control shows why the type matters. Erase \(x,y\), pool the
outcomes, and define a setting-independent classical source that emits
\((a,b)\) with exactly that pooled distribution. It has the identical
complete unlabeled outcome law. With the labels retained, it fails the
tilted Bell test. Thus:

> The recoverable quantum structure lives in the intervention-conditioned
> relations among classical records, not in the outcome values alone.

The return is:

```text
LABELED_CLASSICAL_CORRELATIONS_CAN_SELF_TEST_A_TARGET_QUANTUM_FACTOR
+ TARGET_STATE_SPECTRUM_FIXES_TARGET_FACTOR_MODULAR_DATA
+ SETTING_ERASURE_HAS_AN_EXACT_CLASSICAL_SAME_RECORD_COMPLETION
+ NONCOMMUTATIVITY_ALONE_DOES_NOT_GUARANTEE_NONTRIVIAL_MODULAR_FLOW
+ SELF_TESTING_RECONSTRUCTS_BUT_DOES_NOT_SELECT_THE_PHYSICAL_INTERFACE
+ NO_READY_SCIENTIFIC_SUCCESSOR
```

The tilted-CHSH self-testing theorem is established quantum-information
mathematics. Dynamic Unity's increment is the composition with the modular
target, the exact context-erasure fibre, and the resulting typed correction
to `HC-DU-077`. This is not a new Bell theorem, quantum law, derivation of
proper time, spacetime reconstruction, or record ontology.

## 1. The exact Bell object

Let Alice and Bob have binary observables

\[
A_0,A_1,B_0,B_1
\]

with

\[
A_x^2=B_y^2=I,
\qquad
[A_x,B_y]=0.
\]

The tilted-CHSH operator is

\[
\mathcal I_\alpha
=
\alpha A_0
+A_0B_0+A_0B_1+A_1B_0-A_1B_1,
\qquad
0\leq\alpha<2.
\]

Bamps and Pironio prove sum-of-squares bounds and robust self-testing for
this family
([primary source](https://arxiv.org/abs/1504.06960)). Its maximal quantum
value is

\[
I_\alpha^{\max}=\sqrt{8+2\alpha^2},
\]

compared with the local classical bound \(2+\alpha\).

For

\[
|\psi_\theta\rangle
=
\cos\theta|00\rangle+\sin\theta|11\rangle,
\qquad
0<\theta\leq\frac\pi4,
\]

one optimal strategy is

\[
A_0=Z,\qquad A_1=X,
\]

\[
B_0=\cos\mu\,Z+\sin\mu\,X,
\qquad
B_1=\cos\mu\,Z-\sin\mu\,X,
\]

where

\[
\tan\mu=\sin2\theta,
\qquad
\alpha=\frac{2}{\sqrt{1+2\tan^2 2\theta}}.
\]

At maximal violation, the correlation self-tests the target state and the
action of the target observables under the theorem's quantum Bell contract.
More generally, every pure bipartite entangled state has explicit
self-testing correlations
([Coladangelo, Goh, and Scarani](https://arxiv.org/abs/1611.08062)).

The word “device-independent” must not erase the assumptions. Internal
device dimension and implementation are not trusted, but the result still
uses:

- identified parties or commuting operator families;
- identified input and output alphabets;
- a quantum realization class;
- a conditional law whose settings have retained identity;
- no communication during the declared measurement round, or the
  corresponding commutation structure;
- an acquisition process faithful enough to estimate that conditional law;
  and
- for a physical Bell interpretation, setting provenance and an appropriate
  measurement-independence contract.

Those are part of the antecedent. The theorem does not select them.

## 2. Exact \(\theta=\pi/8\) certificate

Freeze

\[
\theta=\frac\pi8.
\]

Then

\[
\alpha=\frac2{\sqrt3},
\qquad
\cos\mu=\sqrt{\frac23},
\qquad
\sin\mu=\frac1{\sqrt3}.
\]

The ideal correlators are

\[
\langle A_0\rangle=\frac1{\sqrt2},
\]

\[
\langle A_0B_0\rangle
=
\langle A_0B_1\rangle
=
\sqrt{\frac23},
\]

\[
\langle A_1B_0\rangle=\frac1{\sqrt6},
\qquad
\langle A_1B_1\rangle=-\frac1{\sqrt6}.
\]

Therefore

\[
\langle\mathcal I_\alpha\rangle
=
\frac{4\sqrt6}{3}
=
\sqrt{8+2\alpha^2},
\]

which is strictly larger than

\[
2+\frac2{\sqrt3}.
\]

The local reduced state is

\[
\rho_A
=
\operatorname{diag}(\cos^2\theta,\sin^2\theta)
=
\operatorname{diag}
\left(
\frac{2+\sqrt2}{4},
\frac{2-\sqrt2}{4}
\right).
\]

Both eigenvalues are positive, so the state is faithful on the extracted
\(M_2\) factor. It is not tracial. Its eigenvalue ratio is

\[
\cot^2\frac\pi8
=
3+2\sqrt2.
\]

Consequently,

\[
\sigma_t^{\rho_A}(E_{01})
=
\rho_A^{it}E_{01}\rho_A^{-it}
=
(3+2\sqrt2)^{it}E_{01}.
\]

The executable verifies this entire arithmetic chain and the complete
conditional probability law. It reports:

- tilted quantum score \(3.2659863237\);
- tilted classical bound \(3.1547005384\);
- modular eigenvalue ratio \(5.8284271247\); and
- all 23 checks passed.

## 3. What self-testing reconstructs

At exact maximal violation, the self-testing conclusion has the form

\[
\Phi_A\otimes\Phi_B(|\widetilde\psi\rangle)
=
|\mathrm{junk}\rangle\otimes|\psi_\theta\rangle,
\]

with the tested observables acting as the ideal target observables on the
extracted factor, on the tested state. Robust versions replace equality by
controlled error.

This earns:

1. an extracted two-dimensional target factor;
2. noncommuting target generators \(X,Z\);
3. the target bipartite state;
4. the target local reduced-state spectrum; and
5. the conjugacy class of the target-factor modular flow.

The modular data is well-defined under the certified local-unitary gauge. If

\[
\rho'=U\rho U^\dagger,\qquad A'=UAU^\dagger,
\]

then

\[
\sigma_t^{\rho'}(A')
=
U\sigma_t^\rho(A)U^\dagger.
\]

The eigenvalue ratio is invariant. The chosen tilted strategy is real, so
the standard complex-conjugation ambiguity does not change this spectrum or
the displayed target modular phase.

Self-testing does **not** determine:

- the auxiliary “junk” state or all ambient degrees of freedom;
- the modular flow of the complete physical ambient algebra;
- a unique microscopic tensor decomposition outside the tested support;
- which physical devices, regions, or interactions instantiate the ports;
- record formation, archive retention, provenance, or observer access;
- a dimensionful conversion from modular parameter to proper time; or
- modular inclusions, net geometry, spacetime, or ontology.

The positive result therefore closes `M1` only for an **extracted target
factor under a supplied operational interface**. It does not satisfy the
full `HC-DU-077` physical reopener.

## 4. The context-erasure theorem

Let \(p(a,b\mid x,y)\) be any binary conditional law and suppose the four
setting pairs are sampled uniformly. Define the setting-erasure map

\[
E(p)(a,b)
=
\frac14\sum_{x,y}p(a,b\mid x,y).
\]

Now define

\[
q(a,b\mid x,y)=E(p)(a,b)
\]

for every \(x,y\).

### Theorem

\(q\) has a local setting-independent realization and

\[
E(q)=E(p).
\]

### Proof

Draw a shared classical variable \(\lambda=(a,b)\) with probability
\(E(p)(a,b)\). Alice returns \(a\) and Bob returns \(b\), independently of
the supplied settings. This realizes \(q\) as a local hidden-variable
process. Averaging \(q\) over the four settings returns the same
\(E(p)(a,b)\). \(\square\)

Take \(p=p_\theta\), the exact maximal tilted-CHSH law above. Then:

```text
E(p_theta) = E(q)
```

while:

```text
p_theta self-tests the tilted target under the quantum Bell contract;
q is setting-independent and local.
```

The executable finds a maximum labeled conditional-probability difference
of approximately \(0.2925\), while the unlabeled pooled-law distance is
exactly zero at machine precision.

Therefore no decoder of the complete unlabeled output law can infer the
self-tested factor or state. The input labels are not optional annotations;
their relation to the outputs is the discriminator.

## 5. The ordinary-CHSH modular null

Set \(\alpha=0\). Maximal ordinary CHSH self-tests a maximally entangled
two-qubit target and noncommuting Pauli measurements. Yet either local
reduced state is

\[
\rho_A=\frac I2.
\]

Therefore

\[
\sigma_t^{\rho_A}(A)=A
\]

for every \(A\in M_2\).

This separates two prerequisites:

```text
certified noncommutative factor
  != certified nontracial faithful state.
```

Noncommutativity is necessary for a nontrivial finite modular flow, but it is
not sufficient. The state matters.

This also prevents an attractive overclaim: Bell violation does not by
itself reconstruct modular time. The selected correlation must certify an
appropriate state spectrum, and physical time still needs calibration.

## 6. Supplied-versus-reconstructed audit

| object | status in this swing |
|---|---|
| two input ports per party | supplied |
| two output labels per party | supplied |
| input/output occurrence identity | supplied by transcript schema |
| Alice/Bob separation or cross-commutation | supplied operational premise |
| quantum realization class | supplied model class |
| exact \(p(a,b\mid x,y)\) | formed only inside the ideal mathematical specimen |
| target \(M_2\) factor and tested generators | conditionally reconstructed up to local isometry/junk |
| target state and local spectrum | conditionally reconstructed |
| target-factor modular flow | mathematically derived from reconstructed pair |
| complete ambient algebra and state | not reconstructed |
| setting source and measurement independence | not selected |
| physical subsystem or spacetime region | not selected |
| blank archive, write, retention, provenance, access | not selected |
| dimensionful clock calibration | absent |
| modular inclusion or net geometry | absent |
| held-out temporal/geometric physical consequence | absent |

Moving from unlabeled outcomes to a labeled transcript is ordinary record
refinement only when the setting occurrences and provenance already belong
to the same frozen physical process. Adding new setting devices, a separation
boundary, or a quantum realization premise changes the experiment or
completion contract. The operation must be typed case by case.

## 7. Relation to `HC-DU-077`

There is no contradiction.

`HC-DU-077` studies:

\[
(\mathcal D,\omega|_{\mathcal D}),
\]

one complete commutative algebra--state pair.

This result studies:

\[
\{p(a,b\mid x,y)\}_{x,y},
\]

a family indexed by distinct interventions with a declared cross-party
compatibility structure.

The latter contains relational information that is absent from the former.
It is still encoded in classical data, but not as one static state on one
outcome ledger.

The corrected statement is:

> Static classical record values do not carry nontrivial modular flow.
> Sufficiently rich, independently typed classical intervention records can
> conditionally reconstruct an extracted noncommutative factor and state
> whose modular data is nontrivial.

This is one of the clearest examples in Dynamic Unity of why the complete
multi-intervention process is a different object from a terminal record
state.

## 8. North-Star consequence

The result advances the North Star in one precise way.

It shows that a record-first reconstruction program need not postulate that
the durable record carrier itself is noncommutative. Classical records can
be enough to certify noncommutative structure when their intervention,
party, and conditional relationships are preserved.

But this does not remove the physical-selection problem. The Bell protocol
already supplies:

- which questions were asked;
- which answer belongs to which question;
- which ports count as separate;
- which commutation/no-communication relation is admitted; and
- which model class makes the self-testing implication valid.

Dynamic Unity still needs a physical account of how those distinctions are
selected, formed, retained, provenance-bound, and made accessible without
target fitting.

The minimum live ladder is now:

```text
formed, provenance-bearing labeled intervention transcript
  + independently warranted separation/model contract
    -> self-tested target algebra and state
    -> target-factor modular data
  + physical calibration and modular inclusion/net conditions
    -> candidate time or geometry reconstruction
  + no-refit held-out consequence
    -> North-Star candidate.
```

The first two arrows are now mathematically connected. The physical
antecedents and latter arrows are not.

## 9. Grade, novelty, and disposition

### Earned

- **Grade 3, conditional reconstruction:** exact maximal tilted-CHSH records
  reconstruct an extracted target factor, target state, and target modular
  spectrum under the standard self-testing contract.
- **Grade 4, scoped necessity/non-identification:** setting-erased outcome
  records cannot carry that conclusion; the exact same pooled law has a
  setting-independent classical completion.
- **Typed correction:** `HC-DU-077` is a theorem against static commutative
  modular reconstruction, not against all classical-record reconstruction of
  quantum structure.

### Absorbed

- tilted-CHSH quantum maximum;
- sum-of-squares certificate;
- exact and robust self-testing;
- local-isometry/junk equivalence; and
- modular flow of a finite faithful density matrix.

### Not earned

- a novel Bell or modular theorem;
- physical selection of ports, settings, parties, algebra, or state;
- implementation-complete record formation;
- proper time, geometry, spacetime, or field reconstruction;
- observer-independent ontology;
- external-hardware evidence; or
- a standalone high-novelty paper.

### Portfolio disposition

The result is banked as `HC-DU-078`, and the gate is complete. It does not
activate a scientific successor. Reopen only with one physical antecedent
that independently selects or forms the setting/separation interface and
retains its provenance, while the same no-refit transcript certifies the
target factor/state and transfers to a held-out calibrated temporal or
geometric consequence.

No external hardware is needed. Larger Bell simulations or finite-shot
provider runs would not decide the missing physical-selection question.

## 10. Reproduction

Run:

```bash
python3 tests/du_self_tested_modular_reconstruction_probe.py
```

The deterministic artifact is:

```text
tests/artifacts/du_self_tested_modular_reconstruction_result.json
```

It verifies 23/23 finite checks. Passing validates the exact two-qubit
arithmetic and context-erasure counterexample only. The self-testing
implication is supplied by the cited theorem, and none of the physical
selection, formation, time, geometry, or ontology claims is inferred from
the executable.
