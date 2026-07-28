---
title: "Indivisible-stochastic modular non-identifiability and quantum-local rigidity boundary"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-079
run_id: RUN-20260728-123801-indivisible-stochastic-modular-rigidity
run_plan: "../lab/process/runs/RUN-20260728-123801-indivisible-stochastic-modular-rigidity/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-123801-indivisible-stochastic-modular-rigidity/run-receipt.md"
owner_repo: dynamic-unity
---

# Indivisible-stochastic modular non-identifiability

## Executive result

Barandes's indivisible-stochastic framework is a useful exact collision for
`HC-DU-078`, but it does not supply a stochastic-native reconstruction of the
self-tested modular spectrum.

Encode the complete tilted-CHSH conditional law unchanged as

\[
\Gamma_{(a,b),(x,y)}
=
p(a,b\mid x,y).
\]

This is a valid four-configuration, one-division-event indivisible stochastic
object. Its setting and outcome semantics remain supplied time-indexed
decoders of the four native configuration labels.

The stochastic-quantum correspondence writes

\[
\Gamma_{ij}=|\Theta_{ij}|^2
\]

with a nonunique potential matrix \(\Theta\), and explicitly treats arbitrary
entrywise phases as Schur-Hadamard gauge. For the exact `HC-DU-078` law, that
freedom is already enough to defeat stochastic-native modular rigidity.

Let

\[
\Theta_\phi
=
D_\phi\sqrt{\Gamma},
\qquad
D_\phi=\operatorname{diag}(1,1,1,e^{i\phi}),
\]

where the square root is entrywise. Then every \(\Theta_\phi\) gives exactly
the same complete labeled transition object:

\[
|\Theta_{\phi,ij}|^2=\Gamma_{ij}.
\]

Use the framework's Hilbert representative with uniform initial
configuration probabilities,

\[
\varrho_\phi
=
\Theta_\phi\frac{I_4}{4}\Theta_\phi^\dagger,
\]

and temporarily hold fixed the supplied output factor
\(\mathbb C^4=\mathbb C^2_A\otimes\mathbb C^2_B\). The reduced eigenvalues are

\[
\lambda_\pm(\phi)
=
\frac12
\pm
\frac18\sqrt{6+2\cos\phi}.
\]

The corresponding fixed-factor modular ratio is

\[
R(\phi)
=
\frac{4+\sqrt{6+2\cos\phi}}
     {4-\sqrt{6+2\cos\phi}}.
\]

Therefore:

\[
R(0)=3+2\sqrt2,
\qquad
R(\pi)=3.
\]

The complete stochastic transition law has not changed. The first lift
happens to reproduce the self-tested ratio from `HC-DU-078`; an equally
admitted lift does not.

This produces the scoped theorem:

> A complete labeled indivisible-stochastic transition family does not by
> itself determine the fixed-factor modular spectrum of its Hilbert
> representation. The target spectrum becomes rigid only after a narrower
> realization class supplies the quantum-local Bell factor and its
> self-testing equivalence.

At \(\phi=\pi\), \(D_\pi\) is controlled-\(Z\) relative to the supplied
\(A\otimes B\) factor. It is a diagonal configuration rephasing and therefore
an allowed Schur-Hadamard gauge transformation, but it is not a product
unitary. This exposes the exact fork:

- if the output factor is held fixed, its reduced spectrum changes;
- if the factor and all emergeables transform with the gauge, the empirical
  description is preserved, but the factor was not fixed by the stochastic
  object.

Either way, the native stochastic process does not select the target factor
or its modular data.

The return is:

```text
INDIVISIBLE_STOCHASTIC_TRANSITIONS_DO_NOT_FIX_MODULAR_DATA
+ SCHUR_HADAMARD_GAUGE_MOVES_THE_SUPPLIED_OUTPUT_FACTOR
+ QUANTUM_LOCAL_SELF_TESTING_RETAINS_A_CONDITIONAL_RIGID_TARGET
+ BASE_TIME_TRANSITIONS_DO_NOT_FIX_MULTI_TIME_FACTS
+ DIVISION_EVENT_IS_NOT_PHYSICAL_RECORD_FINALITY
+ REPRESENTATION_IS_NOT_INTERFACE_OR_PROCESS_SELECTION
+ NO_READY_SCIENTIFIC_SUCCESSOR
```

## 1. The native stochastic object

Barandes defines an indivisible stochastic process through a finite
configuration space \(\mathcal C\), target times \(\mathcal T\), admitted
conditioning times \(\mathcal T_0\), first-order transition matrices
\(\Gamma(t\leftarrow t_0)\), standalone probabilities \(p\), and a
commutative algebra of configuration random variables. The laws do not
contain a complete Kolmogorov tower. An admitted conditioning time is called
a **division event**.

See:

- [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192);
- [The Stochastic-Quantum Theorem](https://arxiv.org/abs/2309.03085).

For this collision, freeze:

\[
\mathcal C=\{1,2,3,4\},
\qquad
\mathcal T=\{0,1\},
\qquad
\mathcal T_0=\{0\}.
\]

At \(t=0\), decode the four configurations as

\[
(x,y)\in\{0,1\}^2.
\]

At \(t=1\), decode them as

\[
(a,b)\in\{-1,+1\}^2.
\]

Then set

\[
\Gamma_{(a,b),(x,y)}(1\leftarrow0)
=
p_\theta(a,b\mid x,y)
\]

for the exact \(\theta=\pi/8\) tilted-CHSH law. Every column sums to one.
The law is no-signalling and attains the exact tilted quantum maximum
\(4\sqrt6/3\).

This is a faithful representation of the conditional table. It does not
derive:

- that the initial labels are freely chosen interventions rather than
  ordinary prior configurations;
- that the final labels are two physically separate outcomes;
- a tensor-product or commuting-operator structure;
- the no-communication or measurement-independence contract;
- physical occurrence identity across the two decoding times; or
- formation, provenance, retention, access, or finality.

Those are extra types, not entries of a column-stochastic matrix.

The matrix is not bistochastic, hence it is not directly unistochastic in
four dimensions. Barandes's general theorem supplies a nonunique Kraus and
Stinespring dilation after enlargement. That establishes representability,
not uniqueness of the dilation or preservation of every additional
intervention semantic.

## 2. Exact phase-gauge counterexample

The correspondence first chooses complex amplitudes satisfying

\[
\Gamma_{ij}
=
|\Theta_{ij}|^2.
\]

The source explicitly declares

\[
\Theta_{ij}
\mapsto
\Theta_{ij}e^{i\theta_{ij}}
\]

to be Schur-Hadamard gauge. All stochastic transition probabilities remain
unchanged, while downstream Hilbert ingredients must transform together if
physical predictions are to remain invariant.

It is enough to use the one-parameter subgroup

\[
D_\phi
=
\operatorname{diag}(1,1,1,e^{i\phi}).
\]

Let the outcome order be

\[
(-1,-1),(-1,+1),(+1,-1),(+1,+1).
\]

For uniform input settings, take

\[
\varrho_\phi
=
D_\phi\sqrt{\Gamma}\frac{I_4}{4}
 \sqrt{\Gamma}^{\,T}D_\phi^\dagger.
\]

Relative to the supplied \(A\otimes B\) output factor, the Alice reduction is

\[
\varrho_A(\phi)
=
\begin{pmatrix}
\frac12-\frac{\sqrt2}{8}
&
u+ve^{-i\phi}
\\[4pt]
u+ve^{i\phi}
&
\frac12+\frac{\sqrt2}{8}
\end{pmatrix},
\]

where

\[
u=\frac{\sqrt6-\sqrt2}{16},
\qquad
v=\frac{\sqrt6+\sqrt2}{16}.
\]

Because

\[
|u+ve^{-i\phi}|^2
=
\frac1{16}+\frac{\cos\phi}{32},
\]

the eigenvalues are

\[
\lambda_\pm(\phi)
=
\frac12
\pm
\frac18\sqrt{6+2\cos\phi}.
\]

At \(\phi=0\),

\[
\operatorname{spec}\varrho_A(0)
=
\left\{
\frac{2-\sqrt2}{4},
\frac{2+\sqrt2}{4}
\right\},
\]

so

\[
R(0)=3+2\sqrt2.
\]

At \(\phi=\pi\),

\[
\operatorname{spec}\varrho_A(\pi)
=
\left\{\frac14,\frac34\right\},
\qquad
R(\pi)=3.
\]

The ratio varies continuously across the interval. Every transition
probability, every setting label, every outcome label, and the pooled output
law remain unchanged.

This is stronger than saying that one arbitrary dilation was chosen. It
locates the missing type:

```text
native Gamma
  -> many gauge-related Hilbert representatives
  -/-> selected subsystem factor
  -/-> selected reduced state
  -/-> fixed-factor modular spectrum.
```

The all-positive lift's recovery of \(3+2\sqrt2\) is therefore a useful
honesty trap. It is a valid representation and an attractive coincidence,
not an invariant reconstruction.

## 3. What survives under quantum-local rigidity

There is no contradiction with `HC-DU-078`.

Tilted-CHSH self-testing does not quantify over every Schur-Hadamard lift,
Kraus representation, or Stinespring dilation of one stochastic matrix. It
quantifies over a narrower class of quantum Bell realizations with:

- two identified parties or commuting operator families;
- identified settings and outcomes;
- local measurement operators;
- a quantum state;
- the corresponding no-communication or commutation premise; and
- the exact maximal conditional law.

Within that class, the Bamps--Pironio theorem self-tests the target state and
tested observables up to local isometry and auxiliary degrees:

- [Sum-of-squares decompositions for a family of CHSH-type Bell inequalities and their application to self-testing](https://arxiv.org/abs/1504.06960).

Local isometries preserve the extracted target-state spectrum. Thus the
ratio \(3+2\sqrt2\) remains conditionally rigid there.

Barandes, Hasan, and Kagan later recover Tsirelson's ordinary-CHSH bound for
causally local unistochastic processes:

- [The CHSH Game, Tsirelson's Bound, and Causal Locality](https://arxiv.org/abs/2512.18105).

That result is compatible with this boundary. It uses the
stochastic-quantum correspondence and a causal-locality/factorization
contract to reach the standard quantum operator bound. It does not establish
a tilted-CHSH self-testing theorem native to the bare transition matrix, nor
does it select the party factor or reduce the full Schur-Hadamard gauge to a
local subgroup.

The corrected bridge is:

```text
indivisible stochastic transition law
  + supplied quantum-local realization class
  + maximal tilted-CHSH rigidity
    -> extracted target factor and modular spectrum

indivisible stochastic transition law alone
    -/-> that target factor or modular spectrum.
```

Calling the added structure “causal locality” does not make it information
already contained in \(\Gamma\). It is a realization-class restriction.

## 4. Multi-time insufficiency remains

An indivisible stochastic process intentionally contains only selected
first-order transition families. That makes it smaller than an
interventionally complete multi-time process.

The minimum binary witness fixes \(X_0\) independent of later variables and
compares:

```text
Realizer A: X2 = X1, with X1 uniform.
Realizer B: X2 = 1 - X1, with X1 uniform.
```

Both satisfy

\[
P(X_1=i\mid X_0=j)
=
P(X_2=i\mid X_0=j)
=
\frac12
\]

for every \(i,j\). Yet

\[
P_A(X_2=X_1)=1,
\qquad
P_B(X_2=X_1)=0.
\]

Therefore the same base-time transition families admit opposite
intermediate temporal facts. No choice of phase or larger sample size repairs
missing process data.

The strongest standard absorber is the process-tensor/quantum-comb
framework, which types arbitrary multi-time interventions:

- [Pollock et al., Non-Markovian Quantum Processes](https://arxiv.org/abs/1512.00589);
- [Pollock et al., Operational Markov Condition](https://arxiv.org/abs/1801.09811).

Barandes's theorem remains useful as a representation result. It is not a
replacement for a complete process when DU's target is history,
intervention, provenance, or finality.

## 5. Division events are not finality events

The terminology is tempting and must remain typed.

| object | what it establishes |
|---|---|
| division event | the model admits a first-order conditional transition law from that time |
| process history | joint or intervention-conditioned relations across multiple times |
| formed record | a physical history-conditioned carrier was written |
| retained record | the carrier persists under a declared disturbance class |
| accessible record | an observer can distinguish it under a frozen action/resource contract |
| certificate | the record excludes a declared rival at a stated error |
| regional finality | a declared network can safely compose or act under its incompatibility/fault contract |

A division event may be inserted into \(\mathcal T_0\) as model structure
without selecting an archive. Conversely, a physical carrier may form at an
intermediate time even when the reduced stochastic description omits that
time from \(\mathcal T_0\).

Useful future work may test whether a physical record-formation mechanism
induces divisibility for a declared reduced process. The equality cannot be
assumed.

## 6. Supplied-versus-reconstructed audit

| object | status |
|---|---|
| four native configuration labels | supplied |
| time-indexed setting/outcome decoding | supplied |
| base-time transition matrix \(\Gamma\) | supplied law |
| Schur-Hadamard phase | gauge-underdetermined |
| Kraus representation and unitary dilation | nonunique representation |
| \(A\otimes B\) output factor | not selected by \(\Gamma\) |
| quantum-local Bell realization class | extra contract |
| target factor and state within that class | conditionally self-tested |
| target-factor modular ratio | conditionally reconstructed |
| full multi-time process | absent from the base object |
| division event | mathematical conditioning permission |
| physical record formation and provenance | absent |
| observer access and regional finality | absent |
| ambient modular flow | absent |
| dimensionful time calibration and geometry | absent |

## 7. Grade, novelty, and disposition

### Earned

- **Grade 4, scoped necessity/non-identification:** the complete native
  transition object does not determine fixed-factor modular data across its
  admitted phase gauge. The exact ratio family gives a constructive witness.
- **Grade 3, conditional bridge retained:** after independently supplying the
  standard quantum-local Bell class, `HC-DU-078` still reconstructs the
  extracted target spectrum.
- **Exact multi-time boundary:** selected base-time transition matrices do not
  determine a complete history law.
- **Typed finality correction:** division event is not record formation,
  certification, or finality.

### Absorbed

- Schur-Hadamard gauge freedom and stochastic-quantum representation;
- Kraus and Stinespring dilation;
- tilted-CHSH self-testing;
- finite density-matrix modular arithmetic; and
- process-tensor multi-time sufficiency.

Dynamic Unity's increment is the exact collision on one unchanged law, the
closed-form modular-ratio family, and the resulting representation-class
boundary.

### Not earned

- a new stochastic-quantum theorem independent of the cited framework;
- an empirical difference from quantum mechanics;
- physical selection of configurations, factors, instruments, or records;
- a derivation of time, geometry, finality, or ontology;
- a Grade-5 physical remainder; or
- a standalone paper or new scientific successor.

### Stop

Do not build larger stochastic lifts, simulate more Bell rounds, or use
hardware. The non-identifiability is exact and mathematical.

Do not call an ISP a missing physical selector merely because it admits a
quantum representation. Representation freedom is the result.

### Reopen

Reopen this bridge only if one physical antecedent:

1. selects the configuration and intervention semantics;
2. selects a party/factor or access-preserving algebra class;
3. restricts the stochastic-quantum gauge to a physically justified
   equivalence;
4. forms and retains the labeled record with provenance and bounded access;
5. supplies an interventionally complete process when the target is
   multi-time; and
6. transfers the gauge-invariant result without refitting to a held-out
   temporal, geometric, field, or capability consequence.

No current candidate satisfies that reopener. The repository returns to
`NO_READY_SCIENTIFIC_SUCCESSOR`.

## 8. Reproduction

Run:

```bash
python3 tests/du_indivisible_stochastic_modular_rigidity_probe.py
```

The deterministic artifact is:

```text
tests/artifacts/du_indivisible_stochastic_modular_rigidity_result.json
```

It verifies 25/25 checks. Passing validates the exact finite transition,
phase-gauge, fixed-factor spectrum, and multi-time witnesses. It does not
prove the cited stochastic-quantum correspondence or self-testing theorem,
select a physical realization, or establish new physics.
