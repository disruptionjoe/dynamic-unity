---
title: "AQFT modular energy, work, and postselection: the physical selector boundary for uniformly finite state families"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-135
work_id: CCR-AQFT-MODULAR-RESOURCE-PHYSICAL-SELECTOR
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
novelty_status: absorbed_mathematics_and_physics_typed_du_composition
---

# AQFT modular energy, work, and postselection: the physical selector boundary for uniformly finite state families

## Result in one paragraph

`HC-DU-134`'s relative-entropy radius can be physically grounded, but only
under a typed resource contract. On the canonical standard-split factor, let
\(\sigma\) be the faithful reference density and
\(K_\sigma=-\log\sigma\). Any independently selected upper bound

\[
\operatorname{Tr}(\rho K_\sigma)\le E
\]

implies

\[
D(\rho\Vert\sigma)\le E
\]

and therefore activates `HC-DU-134`'s uniform finite compression with an
explicit error. More generally, an ordinary Hamiltonian \(H\) supplies an
affine relative-entropy bound for all states exactly when the split modular
energy is form-dominated,

\[
K_\sigma\le aH+bI.
\]

A genuine Gibbs identification
\(\sigma=Z^{-1}e^{-\beta H}\) is the exact positive control. A verified
thermal work budget also bounds the radius when a frozen formation protocol
obeys the appropriate free-energy work law. But bounded operator norm,
deterministic success, and a postselection-probability floor do not suffice:
norm-one, success-one unitaries can drive
\(D(U\sigma U^*\Vert\sigma)\) to infinity. A fixed ordinary-energy cap also
fails without the form comparison, even when \(H\) has compact resolvent.
Recent modular Reeh--Schlieder cost bounds constrain large **negative**
expectation of the ambient type-III modular generator; they explicitly do
not bound Araki relative entropy and do not control the positive one-sided
split modular tail used here. A 2025 result exactly reconstructs a global
Hamiltonian from nested local modular algebras in finite-volume CFT and
proposes approximations in general QFT. That is a real physical-selector
rung, but it neither proves the split form inequality nor forms a record.
The next exact reopener is therefore model-specific:

\[
\boxed{
K_{\sigma,\Lambda}\le aH_{\mathrm{physical}}+bI
}
\]

or an equally strong resource inequality, followed by a realized
source--probe--archive interface. No ready successor is selected.

## 1. The question left by `HC-DU-134`

For a supplied standard split triple

\[
\Lambda=(A,B,\Omega),
\]

`HC-DU-133` selects a canonical type-\(I_\infty\) factor

\[
N_\Lambda\cong B(\mathcal K)
\]

and a faithful reference density

\[
\sigma>0,\qquad \operatorname{Tr}\sigma=1.
\]

`HC-DU-134` proves that every forward-relative-entropy ball

\[
\mathcal K_D(\sigma)
=\{\rho:D(\rho\Vert\sigma)\le D\}
\]

is trace-norm compact and uniformly approximated by the same spectral
compressions of \(\sigma\).

The theorem's open physical premise was the radius \(D\). The question here
is not whether another mathematical family is compact. It is:

> Does a known physical operation, energy, work, or success-probability
> contract force the states actually available to an observer into one such
> forward-relative-entropy ball?

## 2. The three modular objects that must not be conflated

The word *modular* names different typed objects in this problem.

### 2.1 One-sided split modular energy

On the canonical type-I factor,

\[
K_\sigma=-\log\sigma
\]

is a positive, generally unbounded operator on \(\mathcal K\). It is the
one-sided operator entering

\[
D(\rho\Vert\sigma)
=\operatorname{Tr}(\rho K_\sigma)-S(\rho).
\]

This is the object controlling `HC-DU-134`'s spectral projections.

### 2.2 Ambient modular Liouvillean

For a standard pair \((M,\Omega)\), Tomita--Takesaki theory supplies

\[
\Delta_{M,\Omega}
\quad\text{and}\quad
L_{M,\Omega}=-\log\Delta_{M,\Omega}.
\]

The spectrum of this signed generator is generally two-sided. In a
type-I standard representation its form is schematically

\[
L_\sigma
=K_\sigma\otimes I-I\otimes K_\sigma.
\]

It is not the one-sided \(K_\sigma\).

### 2.3 Geometric modular generator

Bisognano--Wichmann identifies the modular group of a vacuum wedge algebra
with boosts. In vacuum CFT, a ball or causal diamond has a local weighted
stress-tensor modular Hamiltonian. These are scoped identifications of the
ambient modular generator for a particular algebra and state.

None of these statements alone identifies that generator with the
one-sided density logarithm of an intermediate canonical split factor.

## 3. Primary-source and novelty collision

The main ingredients are mature:

- Casini writes local relative entropy as modular-energy change minus entropy
  change and, for a Gibbs reference, as the nonequilibrium free-energy
  difference in
  [“Relative entropy and the Bekenstein bound”](https://arxiv.org/abs/0804.2182).
- Brandão, Horodecki, Oppenheim, Renes, and Spekkens identify free energy as
  the asymptotic work resource for energy-preserving thermal operations in
  [“The Resource Theory of Quantum States Out of Thermal Equilibrium”](https://arxiv.org/abs/1111.3882).
- Wilming, Gallego, and Eisert characterize relative entropy/free energy as
  the continuous extensive athermality monotone under declared catalytic
  operation classes in
  [“Axiomatic characterization of the quantum relative entropy and free energy”](https://arxiv.org/abs/1702.08473).
- Faist and Renner show that one-shot process work requires a more detailed
  coherent-relative-entropy contract in
  [“Fundamental work cost of quantum processes”](https://arxiv.org/abs/1709.00506).
- Blanco-Romero and Almenares Mendoza derive norm and postselection lower
  bounds from negative ambient modular energy in
  [“Modular Lower Bounds on Reeh--Schlieder State Preparation”](https://arxiv.org/abs/2605.18640).
  They explicitly distinguish their signed modular expectation from Araki
  relative entropy.
- Chen, Lashkari, and Leung exactly reconstruct the global Hamiltonian of a
  finite-volume CFT from nested local modular algebras and propose
  inclusion-based local approximations in general QFT in
  [“Local approximations of global Hamiltonian from inclusion of algebras”](https://arxiv.org/abs/2512.25062).

No new relative-entropy, thermodynamic, modular, CFT, or AQFT theorem is
claimed. The Dynamic Unity increment is:

1. the exact resource-to-`HC-DU-134` composition;
2. a necessary-and-sufficient affine comparison contract;
3. two exact hostile families;
4. the three-modular-object anti-conflation;
5. the identification of the exact finite-volume CFT positive; and
6. the resulting selector triangle and model-specific reopener.

## 4. Proposition A — a split modular-energy cap activates uniform compression

Let

\[
K_\sigma=-\log\sigma.
\]

For every density operator \(\rho\) with finite
\(\operatorname{Tr}(\rho K_\sigma)\), the Gibbs variational inequality gives

\[
0\le D(\rho\Vert\sigma)
=\operatorname{Tr}(\rho K_\sigma)-S(\rho)
\le\operatorname{Tr}(\rho K_\sigma).
\]

Therefore:

\[
\boxed{
\operatorname{Tr}(\rho K_\sigma)\le E
\quad\Longrightarrow\quad
D(\rho\Vert\sigma)\le E.
}
\]

The infinite-dimensional statement follows by finite spectral truncation
and lower semicontinuity; finite \(K_\sigma\)-expectation also forces the
relevant entropy term to be finite under the same Gibbs variational bound.

Let \(P\) be a finite spectral projection of \(\sigma\), set

\[
Q=1-P,
\qquad
q=\operatorname{Tr}(\sigma Q),
\qquad
p_\rho=\operatorname{Tr}(\rho Q).
\]

Composing with `HC-DU-134` gives

\[
p_\rho
\le
b(E,q)
:=
\min\!\left\{
1,\frac{E+\log2}{\log(1/q)}
\right\},
\]

and for the canonical reference-replacement channel
\(\mathcal C_P\),

\[
\boxed{
\|\rho-\mathcal C_P(\rho)\|_1
\le
\min\{2,\,2\sqrt{b(E,q)}+b(E,q)\}.
}
\]

Every fixed downstream CPTP process and bounded effect inherits the same
uniform control.

This is an exact positive:

> A physically warranted upper split-modular-energy budget is enough to
> select a uniformly finite state family.

It does not show that any physical QFT or apparatus supplies that budget.

## 5. Proposition B — exact ordinary-energy comparison criterion

Let \(H\ge0\) be a candidate physical Hamiltonian. Suppose \(H\) and
\(K_\sigma\) have a common quadratic-form domain.

For constants \(a\ge0\) and \(b\in\mathbb R\), consider:

\[
K_\sigma\le aH+bI
\tag{1}
\]

as a quadratic-form inequality.

Then every density operator with finite \(H\)-energy satisfies

\[
D(\rho\Vert\sigma)
\le
\operatorname{Tr}(\rho K_\sigma)
\le
a\operatorname{Tr}(\rho H)+b.
\]

Conversely, suppose

\[
D(|\psi\rangle\langle\psi|\Vert\sigma)
\le
a\langle\psi,H\psi\rangle+b
\tag{2}
\]

for every unit vector in the common form domain. A pure state has zero
von Neumann entropy, so

\[
D(|\psi\rangle\langle\psi|\Vert\sigma)
=\langle\psi,K_\sigma\psi\rangle.
\]

Thus (2) is exactly (1).

Hence:

\[
\boxed{
\begin{aligned}
&D(\rho\Vert\sigma)
\le a\operatorname{Tr}(\rho H)+b
\quad\text{for all states}\\
&\text{is forced, and on pure states is possible, exactly through}\\
&K_\sigma\le aH+bI.
\end{aligned}
}
\]

This is the smallest honest bridge contract. “Energy bounds the relative
entropy” is not a generic principle; it is a comparison theorem between the
physical and split modular Hamiltonians.

## 6. Positive control — genuine Gibbs energy

Suppose the reference density is physically selected as

\[
\sigma_{\beta,H}
=\frac{e^{-\beta H}}{Z},
\qquad
Z=\operatorname{Tr}(e^{-\beta H})<\infty.
\]

Then

\[
K_\sigma
=\beta H+\log Z
\]

exactly, so Proposition B holds with

\[
a=\beta,\qquad b=\log Z.
\]

Therefore:

\[
\boxed{
\operatorname{Tr}(\rho H)\le E_H
\quad\Longrightarrow\quad
D(\rho\Vert\sigma_{\beta,H})
\le\beta E_H+\log Z.
}
\]

Equivalently,

\[
D(\rho\Vert\sigma_{\beta,H})
=\beta\big(F_\beta(\rho)-F_\beta(\sigma_{\beta,H})\big).
\]

This gives two physically interpretable routes.

### 6.1 Energy-cap route

A physically selected Hamiltonian, temperature, equilibrium state, and
upper energy budget activate the finite-compression theorem directly.

### 6.2 Work-cap route

If a frozen formation protocol obeys

\[
W_{\mathrm{actual}}
\ge
F_\beta(\rho)-F_\beta(\sigma_{\beta,H})
\]

and a verified apparatus budget gives

\[
W_{\mathrm{actual}}\le W_{\max},
\]

then

\[
\boxed{
D(\rho\Vert\sigma_{\beta,H})
\le\beta W_{\max}.
}
\]

The operation class is load-bearing. The asymptotic many-copy resource
theory, correlated-catalytic monotones, and one-shot work theories use
different contracts. A generic word such as “work” does not transfer the
inequality.

### 6.3 Why the formal Gibbs rewrite is not selection

Every faithful density can be written

\[
\sigma=e^{-K_\sigma}
\]

with partition function one. Calling \(K_\sigma/\beta\) a Hamiltonian does
not make it a laboratory energy, select \(\beta\), or supply a work meter.
The positive is physical only when \(H\), the dynamics, equilibrium
preparation, temperature, and resource accounting are independently
warranted.

## 7. Proposition C — operator norm and success probability do not select the family

Let

\[
\sigma=\sum_{j\ge1}s_j|e_j\rangle\langle e_j|,
\qquad
s_j>0,
\qquad
s_j\longrightarrow0.
\]

Fix \(s_1>0\). Let \(U_n\) swap \(e_1\) and \(e_n\), leaving the orthogonal
complement fixed. Define

\[
\rho_n=U_n\sigma U_n^*.
\]

The preparation is deterministic:

\[
\|U_n\|=1,
\qquad
p_{\mathrm{succ}}=1.
\]

Since \(\rho_n\) and \(\sigma\) commute,

\[
\begin{aligned}
D(\rho_n\Vert\sigma)
&=
s_n\log\frac{s_n}{s_1}
+s_1\log\frac{s_1}{s_n}\\
&=
(s_1-s_n)\log\frac{s_1}{s_n}
\longrightarrow\infty.
\end{aligned}
\]

Therefore:

\[
\boxed{
\text{bounded operator norm}
+\text{ deterministic success}
\;\not\Longrightarrow\;
\text{bounded forward relative entropy}.
}
\]

The same construction defeats any fixed postselection-probability floor.
It already lives inside the candidate type-I split factor. A restriction to
a smaller physically realizable local operation algebra is an additional
contract and must be proved to change the result.

The missing resource is visible: these unitaries inject unbounded
\(K_\sigma\)-energy. Norm and success do not price that injection.

## 8. Proposition D — ordinary energy fails without the comparison theorem

The failure is not limited to a completely degenerate Hamiltonian.

On \(\ell^2(\mathbb N)\), let

\[
H|e_j\rangle=j|e_j\rangle
\]

and choose

\[
\sigma
=Z^{-1}\sum_{j\ge1}e^{-j^2}|e_j\rangle\langle e_j|.
\]

Thus

\[
K_\sigma|e_j\rangle
=(j^2+\log Z)|e_j\rangle.
\]

For \(n\ge2\), define

\[
\rho_n
=\left(1-\frac1n\right)|e_1\rangle\langle e_1|
+\frac1n|e_n\rangle\langle e_n|.
\]

Its physical \(H\)-energy is uniformly bounded:

\[
\operatorname{Tr}(\rho_nH)
=\left(1-\frac1n\right)+\frac1n n
=2-\frac1n
<2.
\]

But

\[
\begin{aligned}
D(\rho_n\Vert\sigma)
&=
\left(1-\frac1n\right)
\log\frac{1-1/n}{s_1}
+\frac1n\log\frac{1/n}{s_n}\\
&=
n+O(1)
\longrightarrow\infty.
\end{aligned}
\]

Here \(H\) has compact resolvent and no infinite low-energy degeneracy. The
failure occurs because

\[
K_\sigma\sim H^2
\]

rather than \(K_\sigma\le aH+b\).

Thus:

\[
\boxed{
\text{finite ordinary energy}
\;\not\Longrightarrow\;
\text{bounded }D(\rho\Vert\sigma)
}
\]

for an arbitrary faithful reference.

## 9. Important correction — failure of this route is not failure of finite approximation

The family in Proposition D is nevertheless uniformly finitely
approximable in the **physical \(H\)-basis**.

For the spectral projection

\[
P_N^H=\mathbf1_{[0,N]}(H),
\]

Markov's inequality gives every state with
\(\operatorname{Tr}(\rho H)\le E_H\):

\[
\operatorname{Tr}\rho(1-P_N^H)
\le\frac{E_H}{N}.
\]

Because \(H\) has compact resolvent, \(P_N^H\) has finite rank.

So Proposition D proves:

```text
PHYSICAL_H_ENERGY_CAP
  -/-> CANONICAL_SIGMA_RELATIVE_ENTROPY_BALL

BUT

PHYSICAL_H_ENERGY_CAP + COMPACT_RESOLVENT
  -> UNIFORM_FINITE_H_SPECTRAL_CARRIER.
```

This is the `HC-DU-132` route, not a failure of finite effective physics.
It also reveals a selector competition:

- \(\sigma\)-spectral corners are canonical relative to the standard split
  state;
- \(H\)-spectral corners are canonical relative to physical dynamics; and
- the two agree operationally only after a comparison or target-transfer
  theorem.

## 10. Why the 2026 modular preparation bound does not close the selector

Blanco-Romero and Almenares Mendoza prove, for a local operator
\(A\) with

\[
\xi=A\Omega,
\]

that

\[
\|A\|
\ge
\|\xi\|
\exp\!\left[
-\frac12
\langle L_{\mathcal O}\rangle_{\hat\xi}
\right],
\]

where

\[
L_{\mathcal O}=-\log\Delta_{\mathcal O}
\]

is the signed ambient modular generator. Rescaling \(A\) to a contraction
turns large negative modular expectation into a small postselection
probability.

This is a real physical cost result. It does not supply the present selector
for three independent reasons.

### 10.1 Wrong direction

It gives a lower preparation cost for states with large **negative**
ambient modular expectation. `HC-DU-134` requires an upper bound preventing
escape to large positive one-sided \(K_\sigma\)-energy.

### 10.2 Wrong object

The paper states explicitly that the signed expectation is not Araki
relative entropy. The ambient
\(-\log\Delta_{\mathcal O}\) is not the one-sided
\(-\log\sigma\) of the canonical split density.

### 10.3 Exact hostile control

Proposition C has

\[
\|U_n\|=1,
\qquad
p_{\mathrm{succ}}=1,
\qquad
D(U_n\sigma U_n^*\Vert\sigma)\to\infty.
\]

The cost theorem and the hostile family are consistent: the theorem forbids
deterministic access to negative modular sectors, while the hostile family
escapes through an unbounded positive sector.

The correct classification is:

\[
\boxed{\texttt{ONE\_SIDED\_COST\_ONLY}.}
\]

## 11. Strongest literature positive — modular inclusion can select a physical Hamiltonian

Chen, Lashkari, and Leung supply a more relevant positive.

### 11.1 Exact finite-volume CFT result

For nested ball algebras in vacuum CFT on the Lorentzian cylinder, their
characteristic-function construction expresses the global cylinder
Hamiltonian exactly in terms of local modular inclusion data. The conformal
representation gives that Hamiltonian a discrete spectrum.

This earns a real selection/reconstruction rung:

```text
NESTED_LOCAL_ALGEBRAS
+ VACUUM
+ CONFORMAL_GEOMETRY
  -> GLOBAL_PHYSICAL_HAMILTONIAN.
```

Combined with an independently bounded energy family and finite
low-energy multiplicity, this can activate the \(H\)-spectral finite-carrier
route.

### 11.2 General QFT remains approximate and nonunique

Away from the CFT fixed point, the paper proposes local approximations

\[
H_z(R)
\]

or mixtures parameterized by a filter \(p(z)\). The filter is to be chosen
according to which infrared data the approximation should preserve.

That is honest approximation, not one uniquely selected QFT Hamiltonian.
It leaves:

- the state and inclusion family;
- the filter or optimization target;
- approximation error;
- physical access to modular operators;
- finite acquisition;
- the energy cap;
- and the record interface

separately supplied.

### 11.3 It does not prove the split comparison

The exact CFT construction acts on ambient modular data of nested local
algebras. It does not establish

\[
K_{\sigma,\Lambda}
\le
aH_{\mathrm{CFT}}+bI
\]

for the one-sided density logarithm of the canonical standard-split factor.
Nor does it prove that the finite \(H\)-carrier and the finite
\(\sigma\)-carrier preserve the same observer targets.

The classification is:

\[
\boxed{\texttt{CONDITIONAL\_COMPARISON\_BRIDGE}.}
\]

## 12. Selector scorecard

| Candidate antecedent | Exact return | Classification |
|---|---|---|
| Upper bound on the same split \(K_\sigma=-\log\sigma\) | \(D(\rho\Vert\sigma)\le E\), hence explicit uniform finite compression | `PHYSICALLY_SELECTS_FORWARD_BALL` only after the bound and meter are physical |
| Genuine trace-class Gibbs state of physical \(H\) plus energy cap | \(D\le\beta E_H+\log Z\) | `PHYSICALLY_SELECTS_FORWARD_BALL` |
| Frozen thermal formation law plus verified work cap | \(D\le\beta W_{\max}\) under the declared work theorem | `PHYSICALLY_SELECTS_FORWARD_BALL` conditionally |
| Form inequality \(K_\sigma\le aH+bI\) | \(D\le aE_H+b\) | `CONDITIONAL_COMPARISON_BRIDGE` |
| Bounded operator norm | Exact success-one unitary escape | `FAILS_BY_EXACT_COUNTEREXAMPLE` |
| Postselection success floor | Same success-one escape | `FAILS_BY_EXACT_COUNTEREXAMPLE` |
| Arbitrary ordinary-energy cap | Exact compact-resolvent counterexample | `FAILS_BY_EXACT_COUNTEREXAMPLE` for the \(\sigma\)-route |
| Compact-resolvent \(H\)-energy cap | Uniform finite \(H\)-spectral carrier | `ALTERNATE_FINITE_CARRIER`, already `HC-DU-132` |
| Negative ambient modular preparation-cost bound | Prices the wrong sign and modular object | `ONE_SIDED_COST_ONLY` |
| Nested modular inclusion in finite-volume vacuum CFT | Exact global \(H\) reconstruction | `PHYSICAL_H_SELECTOR_FOUND`, but no split comparison or record |
| Nested modular inclusion in generic QFT | Family of proposed approximants with filter choice | `PARTIAL_PHYSICAL_TYPING` |

## 13. The selector triangle

The QFT-facing problem now has a clean three-corner structure.

### Corner A — canonical split state

\[
\text{standard split triple}
\to \sigma
\to \text{finite }\sigma\text{-spectral corners}.
\]

Strength: finite corners exist at every tolerance.

Missing: physical energy/resource meaning and selected state family.

### Corner B — physical Hamiltonian

\[
\text{QFT dynamics}
\to H
\to \text{energy-bounded family}.
\]

Strength: genuine physical resource meaning.

Missing in noncompact QFT: finite low-energy rank; `HC-DU-132`.

### Corner C — genuine Gibbs alignment

\[
\sigma=Z^{-1}e^{-\beta H}.
\]

Strength: both routes align exactly.

Cost: this is the trace-class Gibbs/finite-volume or otherwise confined
regime where standard thermal and spectral mathematics already supplies the
answer.

The high-value opening is not a fourth generic information measure. It is a
model-specific theorem that joins A and B in a physically serious continuum
arena.

## 14. Minimum next theorem

The exact reopener is:

> For a physically selected QFT net, state, collar, and canonical standard
> split factor, prove or refute a model-uniform quadratic-form bound
>
> \[
> K_{\sigma,\Lambda}
> \le
> aH_{\mathrm{physical}}+bI
> \]
>
> with \(a,b\) independently fixed by physical geometry, temperature,
> nuclearity, or apparatus resources.

A weaker but still useful target is a nonlinear coercive relation

\[
\operatorname{Tr}(\rho K_{\sigma,\Lambda})
\le
f(\operatorname{Tr}(\rho H))
\]

with finite \(f(E)\) on the physical family.

### Positive result

A positive theorem composes immediately with `HC-DU-134` to give a uniform
finite state carrier with a physically determined error curve.

### Negative result

A sequence of physically admissible states with bounded ordinary energy and
unbounded split modular energy proves that the canonical split compression
is not resource-natural for that model. The \(H\)-carrier may still survive.

### What must follow either result

Neither branch forms a record. A source--probe--pointer--archive instrument,
complete acquisition, observer access, fixed target, and no-refit transfer
remain required.

## 15. Corrected selector ladder

| Rung | Exact return | Status |
|---:|---|---|
| 0 | supplied QFT/net/representation | antecedent |
| 1 | standard split triple | antecedent/model condition |
| 2 | canonical type-\(I_\infty\) factor and \(\sigma\) | selected relative to triple |
| 3 | split \(K_\sigma=-\log\sigma\) | selected mathematically |
| 4a | upper \(K_\sigma\)-budget | exact sufficient selector, physical origin open |
| 4b | genuine Gibbs \(H,\beta\) and energy/work budget | exact physical positive in scoped type-I arena |
| 4c | ambient/geometric modular cost | different object and one-sided constraint |
| 5 | form comparison \(K_\sigma\le aH+bI\) | exact missing bridge in generic physical arena |
| 6 | uniform finite state carrier and error | conditional theorem |
| 7 | locally realized compression/probe | open |
| 8 | formed retained archive and access | open |
| 9 | fixed held-out target transfer | open |
| 10 | North-Star reconstruction or remainder | open |

## 16. Relationship to recent Dynamic Unity results

### `HC-DU-117`

Relative entropy remains a tool rather than a physical capacity law. This
run identifies one exact circumstance in which a physical resource gives it
meaning: a genuine Gibbs or form-comparison contract.

### `HC-DU-131--132`

Nuclearity and physical energy cutoffs already supply alternate finite
approximation routes. The Proposition-D family shows why those routes need
not factor through the canonical split reference.

### `HC-DU-133--134`

The reference-state and forward-family mathematics remains correct. The
radius is no longer merely arbitrary in principle: thermodynamic or modular
energy can select it. Generic standard-split AQFT does not yet do so.

### `HC-DU-095--101`

Those results require a physically selected compact source/process class.
This run supplies the exact state-family resource contract such a class
would need on the split branch, but not its instrument or response
completeness.

## 17. Evidence grade

### Scoped Grade 4

- the split modular-energy implication;
- the affine energy-comparison necessity/sufficiency criterion;
- the norm-one/success-one relative-entropy escape;
- the compact-resolvent ordinary-energy mismatch;
- the alternate \(H\)-carrier correction; and
- the modular-object/sign non-transfer.

### Conditional Grade 3

A genuine Gibbs energy/work contract or proved QFT form comparison yields a
uniform finite state-family reconstruction with explicit error.

### Not earned

- a selected QFT model or apparatus;
- a physical split modular-energy meter;
- the required generic-QFT form comparison;
- a selected energy/work cap;
- a finite classical record;
- source/probe/archive formation;
- empirical excess;
- a new thermodynamic, AQFT, or CFT theorem;
- new law, new physics, prediction, paper promotion, or hardware path.

## 18. Disposition

Bank the selector criterion and keep Dynamic Unity quiescent.

Do not continue by trying more generic resource words. Reopen only when a
concrete model or apparatus supplies one of:

1. a proved comparison between the canonical split modular Hamiltonian and a
   physically metered Hamiltonian/resource;
2. a genuine trace-class Gibbs realization of the canonical split state in
   a target-relevant arena;
3. a physically realized local operation family with a proven uniform split
   modular-energy ceiling; or
4. a formed finite \(H\)- or \(\sigma\)-carrier with complete acquisition,
   archive lineage, access, and held-out transfer.

The durable return is:

```text
PHYSICAL_SPLIT_MODULAR_ENERGY_CAP
  -> FORWARD_RELATIVE_ENTROPY_BALL
  -> UNIFORM_FINITE_SPLIT_CARRIER

GENUINE_GIBBS_ENERGY_OR_WORK_CAP
  -> PHYSICAL_SPECIALIZATION

OPERATOR_NORM_OR_SUCCESS_PROBABILITY
  -/-> RELATIVE_ENTROPY_RADIUS

ORDINARY_ENERGY
  -> RELATIVE_ENTROPY_RADIUS
  IFF THE REQUIRED FORM COMPARISON HOLDS

ORDINARY_ENERGY + COMPACT_RESOLVENT
  -> ALTERNATE_H_CARRIER
  EVEN WHEN THE SIGMA_ROUTE FAILS

AMBIENT_NEGATIVE_MODULAR_COST
  -/-> POSITIVE_ONE_SIDED_SPLIT_CONTROL

FINITE_VOLUME_CFT_MODULAR_INCLUSION
  -> GLOBAL_H_SELECTOR
  -/-> SPLIT_COMPARISON
  -/-> FORMED_RECORD.
```
