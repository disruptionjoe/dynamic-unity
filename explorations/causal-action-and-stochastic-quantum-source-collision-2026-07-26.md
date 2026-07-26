---
title: "Causal action and stochastic-quantum source collision"
status: completed_scoped_collision
doc_type: literature_collision_and_cross_repo_disposition
created: 2026-07-26
run_id: RUN-20260726-165229-finster-barandes-source-collision
claim_grade: "PRIMARY-SOURCE-ANCHORED BOUNDARY FINDINGS + CONDITIONAL DU IMPORTS / NO CLAIM, PRIORITY, PAPER, OR ONTOLOGY MOVEMENT"
---

# Causal action and stochastic-quantum source collision

## Executive verdict

The supplied external-agent memo contains two load-bearing corrections worth
keeping:

1. **Felix Finster's causal action is a genuine physical-law candidate for
   narrowing a completion class.** It variationally selects universal measures
   from a supplied causal-variational problem. It is not merely a change of
   representation.
2. **Jacob A. Barandes's stochastic-quantum theorem is a representation and
   dilation result, not a physical selection law.** In the published proof,
   the constructed dilation preserves the transition family conditioned at
   the distinguished initial time. It does not establish preservation of an
   interventionally complete multi-time process.

Neither framework supplies Dynamic Unity's missing interfaces:

```text
observer
instrument
record map
archive/pointer algebra
access boundary
certification rule
regional finality
held-out capability target
```

The most immediate exact collision is dimensional:

> Fischer--Finster's continuum condition
> \(R_{\mu\nu}^{\mathrm{TF}}=0\) is identically vacuous in two dimensions.
> It therefore cannot restrict DU's current \(1+1\)-dimensional conformal
> hostile family.

This finding does **not** reprioritize the program or promote CFS. It tells a
future CFS-facing Lane-6 attempt which arena would be meaningful.

## Provenance and authority

Joe supplied a detailed external-agent synthesis and asked that it be treated
as information, not directive. This pass checked its load-bearing claims
against primary sources and current owner-repository state.

The resulting classifications are:

| label | meaning |
|---|---|
| `VERIFIED_FOR_USE` | exact source passage or theorem scope was checked and is safe for this collision |
| `SUPPORTED_POINTER` | primary-source abstract or scoped statement supports the pointer; details still require paper-level audit before theorem use |
| `MEMO_QUEUE` | useful source pointer preserved from the external synthesis but not independently audited in enough detail here |
| `BOUNDED_SEARCH_NULL` | targeted search found no bridge; this is not proof of absence |

No external-agent evaluation, grade, roadmap recommendation, theorem name, or
paper ranking is imported as authority.

## Identity correction

The researcher is **Jacob A. Barandes**, not Jacob Brandes. The relevant
program includes:

- [The Stochastic-Quantum Correspondence](https://arxiv.org/abs/2302.10778);
- [The Stochastic-Quantum Theorem](https://arxiv.org/abs/2309.03085);
- [New Prospects for a Causally Local Formulation of Quantum Theory](https://arxiv.org/abs/2402.16935);
- [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192); and
- [A Deflationary Account of Quantum Theory and its Implications for the Complex Numbers](https://arxiv.org/abs/2602.01043).

Status: `VERIFIED_FOR_USE`.

## Typed audit: causal fermion systems

### Native objects

For spin dimension \(n\), a causal fermion system begins with:

\[
\mathcal H,
\qquad
\mathcal F
=
\{x\in L(\mathcal H):
x=x^*,\ \mathrm{rank}(x)<\infty,\ n_\pm(x)\le n\},
\]

and a positive measure \(\rho\) on \(\mathcal F\). Abstract spacetime is

\[
M=\operatorname{supp}\rho.
\]

For \(x,y\in\mathcal F\), the spectrum of \(xy\) defines the causal
Lagrangian \(\mathcal L(x,y)\), and the causal action is

\[
\mathcal S(\rho)
=
\iint_{\mathcal F\times\mathcal F}
\mathcal L(x,y)\,d\rho(x)\,d\rho(y),
\]

subject to declared volume, trace, and boundedness constraints. The current
technical reference is
[Causal Fermion Systems: An Introduction](https://arxiv.org/abs/2411.06450).

### What the action selects

Within a supplied variational problem, the action can select a set

\[
\operatorname*{arg\,min}_{\rho\in\mathcal A}\mathcal S(\rho).
\]

That is a physically serious selector of configurations or measures. It is
stronger than choosing coordinates or dilating a channel.

It does not by itself establish:

- existence in every intended infinite-dimensional/infinite-volume class;
- uniqueness of the minimizer;
- a smooth manifold support;
- the physical Hilbert space, spin dimension, constraints, matter sector, or
  regularization without antecedent input;
- a unique observer, measurement instrument, pointer basis, archive,
  certified record map, or finality rule.

The scoped existence/nonuniqueness boundary is already visible in
[Causal Variational Principles on Measure Spaces](https://arxiv.org/abs/0811.2666).
The presence of many linearized solutions is independently relevant; see
[Solving the Linearized Field Equations of Causal Variational Principles](https://arxiv.org/abs/2304.00965).

Status: `VERIFIED_FOR_USE` for the selector/nonuniqueness distinction.

### The newest geometry results

[Fischer--Finster (2026)](https://arxiv.org/abs/2605.30199) construct CFS on
a supplied globally hyperbolic Lorentzian spin manifold using Dirac and
Hadamard-state data plus regularization. In their scoped continuum analysis,
a declared geometric perturbation satisfies the linearized CFS field
equations iff

\[
R_{\mu\nu}^{\mathrm{TF}}=0.
\]

With supplied on-shell fermionic matter they derive the corresponding
trace-free Einstein--Dirac relation, with coupling determined by
regularization data under the paper's assumptions.

[Finster--Krpoun (2026)](https://arxiv.org/abs/2607.13871) take a different
route: assuming a minimizing measure with smooth-manifold support and suitable
short-range/osculating-vacuum structure, the Lagrangian induces geometry and
the Euler--Lagrange equations imply an Einstein-form equation. Their
Lorentzian construction is worked out in four dimensions.

These are substantive conditional geometry results. They are not proofs that
unrestricted causal-action minimization uniquely selects our spacetime or its
record interfaces.

Status: `VERIFIED_FOR_USE` for the assumptions and trace-free equation;
paper-grade use still requires a complete proof audit.

## Typed audit: Barandes

### Native object

Barandes defines an indivisible stochastic process as a tuple of the form

\[
\mathfrak P
=
(\mathcal C,\mathcal T,\mathcal T_0,\Gamma,p,\mathcal A),
\]

where \(\Gamma(t\leftarrow t_0)\) supplies selected conditional transition
families and \(\mathcal T_0\) is the set of conditioning times.

The paper explicitly notes that this object can fix less information than a
full non-Markovian stochastic process. Different full trajectory processes
can realize the same supplied tuple.

### What the theorem constructs

The proof:

1. starts from \(\Gamma(t\leftarrow0)\);
2. chooses nonunique complex amplitudes whose squared moduli reproduce it;
3. constructs a CPTP channel through Kraus operators;
4. applies Stinespring dilation; and
5. marginalizes an enlarged unistochastic process back to the original
   base-time transition family.

The constructed dilated conditioning-time set is explicitly
\(\widetilde{\mathcal T}_0=\{0\}\). Therefore the proved result is safely read
as:

> a finite initial-time stochastic transition family admits a nonunique
> Hilbert/channel/unitary representation after enlargement.

It should not be read as:

> one unitary dilation preserves every original multi-conditioning-time
> kernel, intervention, or full trajectory law.

Status: `VERIFIED_FOR_USE` against
[The Stochastic-Quantum Theorem, revised 2026](https://arxiv.org/html/2309.03085v2).

### Smallest exact insufficiency controls

#### Same base-time transitions, different temporal fact

Let \(X_0\) be uniform and independent of later variables.

```text
Process A: X2 = X1
Process B: X2 = 1 - X1
```

Both can satisfy

\[
P(X_1=i\mid X_0=j)
=
P(X_2=i\mid X_0=j)
=
\frac12,
\]

while

\[
P_A(X_2=X_1)=1,
\qquad
P_B(X_2=X_1)=0.
\]

Thus \(\Gamma(t\leftarrow0)\) does not determine even the smallest
nontrivial intermediate temporal relation.

#### Same configuration probabilities, different held-out instrument

Let

\[
U_1=H,
\qquad
U_2=ZH.
\]

Their computational-basis transition matrices are identical:

\[
|(U_1)_{ij}|^2
=
|(U_2)_{ij}|^2
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\]

But \(U_1|0\rangle=|+\rangle\) and \(U_2|0\rangle=|-\rangle\), so an
\(X\)-basis held-out instrument separates them perfectly.

These controls specialize the already governing DU rule:

```text
representation of observed statistics
    != selection of a physical process
    != multi-time interventional sufficiency
    != certified record reconstruction
```

The closest standard absorber is the process-tensor/quantum-comb literature:
[Pollock et al. 2015](https://arxiv.org/abs/1512.00589) and
[Pollock et al. 2018](https://arxiv.org/abs/1801.09811).

## Exact collision with Dynamic Unity

### 1. Law-filtered fibres

Let \(M\) be DU's frozen completion class, \(r:M\to Q\) the independently
specified certified-record map, \(t:M\to Y\) the held-out target, and
\(E(m)=0\) an independently warranted physical law.

Define:

\[
M_{\mathrm{law}}
=
\{m\in M:E(m)=0\},
\qquad
F_q^{\mathrm{law}}
=
\{m\in M:r(m)=q,\ E(m)=0\}.
\]

This operation is **completion-class narrowing**, not record refinement.
If \(E\) was not antecedently part of \(M\), adding it is contract retyping.
It cannot be reported as new information carried by \(q\).

The local target-sufficiency condition, modulo the declared gauge, is:

\[
\ker Dr_m
\cap
\ker DE_m
\subseteq
\ker Dt_m.
\]

With admitted source differences, boundary perturbations, regulator changes,
or matter variations, their tangent directions must be included rather than
silently frozen after the result.

This is the correct DU import of causal action.

### 2. Neither framework fills a record fibre

CFS existence is existence for its own scoped variational problem. It does not
imply that a separately declared DU record \(q\) is compatible with any CFS
minimizer.

Barandes begins with a normalized stochastic object. It does not prove that a
separately declared physical record was generated by an admitted source.

Therefore neither entails:

\[
F_q^{\mathrm{law}}\ne\varnothing.
\]

Realizability remains logically prior to target constancy, as required by
`HC-DU-039A/039B`.

### 3. The current \(1+1\) CFS test is vacuous

For every two-dimensional metric,

\[
R_{\mu\nu}
=
\frac12 Rg_{\mu\nu},
\]

so

\[
R_{\mu\nu}^{\mathrm{TF}}\equiv0.
\]

Fischer--Finster's trace-free continuum equation therefore places no
restriction on DU's current family

\[
g_u=u(x)(-dt^2+dx^2).
\]

The existing hostile conformal mode remains a valid DU inverse-problem
counterexample, but it cannot test this particular CFS restriction.

### 4. Why \(3+1\) is necessary but not automatically distinctive

For a four-dimensional linear conformal perturbation

\[
h_{\mu\nu}=2\phi\eta_{\mu\nu},
\]

the trace-free linearized Ricci tensor is

\[
\delta R_{\mu\nu}^{\mathrm{TF}}
=
-2\partial_\mu\partial_\nu\phi
+\frac12\eta_{\mu\nu}\Box\phi.
\]

The vacuum condition removes compactly supported conformal bumps in the
linearized arena. But ordinary vacuum Einstein dynamics already does this.

Accordingly:

- a \(3+1\) vacuum conformal calculation can validate the law-filtered-fibre
  method;
- it does not by itself establish a CFS-specific Dynamic Unity result;
- a distinctive CFS residue would require a frozen finite-regularization term
  or other CFS consequence that removes or predicts something left open by
  Einstein dynamics, robustly across the admitted regulator family.

## Implications for the current program

### Warranted now

1. Preserve **physical-law filtering** as its own operation between completion
   definition and record reconstruction.
2. Preserve **representation without selection** as a permanent adversary.
3. Require an interventionally complete multi-time object when the target is
   multi-time or counterfactual.
4. Do not use the current \(1+1\) conformal specimen as a test of the
   Fischer--Finster trace-free equation.
5. If a future Lane-6 lead chooses CFS, require a frozen \(3+1\) arena with:
   \(\mathcal H\), spin dimension, constraints, sector, regulator family,
   matter/source class, boundary/initial conditions, gauge, record map, and
   held-out target all declared before calculation.
6. Separate:
   - GR-level closure;
   - CFS continuum-limit compatibility;
   - finite-regularization CFS-specific residue.

### Not warranted now

- no new DU theorem or prediction ID;
- no claim or concept promotion;
- no assertion that CFS is DU's missing physical engine;
- no assertion that Barandes reconstructs quantum ontology;
- no paper or Drafting Factory movement;
- no Lane-6 priority displacement;
- no hardware work;
- no claim that the bounded bridge search proves no CFS--process-tensor or
  CFS--Barandes literature exists.

## Candidate results exposed, not promoted

| candidate | honest current shape | strongest absorber | local feasibility |
|---|---|---|---|
| Action-filtered fibre theorem/obstruction | \( \ker Dr\cap\ker DE\subseteq\ker Dt \), modulo gauge and admitted source directions | constrained inverse problems and observability | high |
| Causal-action interface-selection obstruction | action symmetry with no fixed interface blocks unique equivariant record selection | symmetry breaking, decoherence, reference frames | medium-high |
| CFS-to-process sufficient-statistics bridge | construct a full process/instrument object from a frozen minimizer, then test certified-record sufficiency | open-system theory and process tensors | medium |
| Variational observer-target reconstruction | records are target-sufficient on a natural minimizer class without target-fitting | inverse variational problems | lower, high ceiling |
| Collapse-to-certified-record convergence audit | declared pointer reaches an absorbing record sector with scoped probabilities/rates | stochastic collapse and martingale theory | medium-low |

These are a map of the information contained in the collision. They are not
the memo's recommended ordering and are not new work authorization.

## Cross-repository disposition

| owner | warranted capture | disposition |
|---|---|---|
| Dynamic Unity | full typed collision; law-filtered fibre; Barandes scope guard; \(1+1\) vacuity; conditional \(3+1\) arena rule | captured in this note and governing orientation surfaces |
| Time as Finality | CFS local/future algebra and collapse work do not yet select records/finality; Barandes null model is only base-time unless enlarged | owner note and existing Barandes surface updated |
| Temporal Issuance | Barandes remains a representation-without-issuance absorber; causal action is a real selector but still selects within a supplied variational problem | existing absorber surfaces updated |
| GU Formalization | CFS is a useful source-action selector comparator; Barandes/Stinespring remains a chosen-channel null model | exploration comparator and existing crosswalk updated |
| Possibility to Capability | unitary/Hilbert representation is not capability gain; selected configuration is not observer capability without matched access, task, controls, and resources | **pointer only**; repo intentionally not edited because its checkout contains an unpublished local commit |
| AI Epistemology | preserve the distinction among representation, physical selection, interface selection, and reconstruction; record negative bridge searches as bounded | recommended pointer only; no owner write in this run |

## Primary-source pointer register

### CFS: load-bearing sources checked

- Finster,
  [Causal Variational Principles on Measure Spaces](https://arxiv.org/abs/0811.2666)
  — scoped existence, nonuniqueness, and compactness boundary.
- Finster,
  [The Continuum Limit of Causal Fermion Systems](https://arxiv.org/abs/1605.04742)
  — continuum-limit program; conditional construction rather than
  parameter-free unique-world theorem.
- Finster,
  [Solving the Linearized Field Equations](https://arxiv.org/abs/2304.00965)
  — many homogeneous and other linearized solutions.
- Finster--Kleiner--Paganini,
  [Causal Fermion Systems as an Effective Collapse Theory](https://arxiv.org/abs/2405.19254)
  — effective stochastic-collapse route under declared assumptions.
- Finster--Kindermann--Treude,
  [Causal Fermion Systems: An Introduction](https://arxiv.org/abs/2411.06450)
  — current technical reference.
- Fischer--Finster,
  [Continuum Limit Analysis for Curved Spacetimes](https://arxiv.org/abs/2605.30199)
  — trace-free Einstein/Einstein--Dirac continuum result.
- Finster--Krpoun,
  [A Geometric Derivation of the Einstein Equations](https://arxiv.org/abs/2607.13871)
  — geometry from a smooth minimizing support under osculating-vacuum
  assumptions; four-dimensional Lorentzian construction.

### CFS: useful pointers retained for later exact audit

- Finster--Schiefeneder,
  [On the Support of Minimizers](https://arxiv.org/abs/1012.1589).
- Finster,
  [Complex Structures on Jet Spaces and Bosonic Fock Space Dynamics for Causal Variational Principles](https://arxiv.org/abs/1808.03177).
- Finster--Kamran,
  [Fermionic Fock Spaces and Quantum States for Causal Fermion Systems](https://arxiv.org/abs/2101.10793).
- Finster,
  [Entangled Quantum States of Causal Fermion Systems](https://arxiv.org/abs/2207.13157).
- Finster--Oppio,
  [Local Algebras for Causal Fermion Systems in Minkowski Space](https://arxiv.org/abs/2004.00419).
- Finster--Fröhlich--Oppio--Paganini,
  [Causal Fermion Systems and the ETH Approach to Quantum Theory](https://arxiv.org/abs/2004.11785).
- Dappiaggi--Finster--Kamran--Reintjes,
  [Fock Space Dynamics: Non-Abelian Gauge Fields](https://arxiv.org/abs/2607.08488).

These are `SUPPORTED_POINTER` or `MEMO_QUEUE`, not theorem premises in this
run.

### Barandes and process-level absorbers

- Barandes,
  [The Stochastic-Quantum Correspondence](https://arxiv.org/abs/2302.10778).
- Barandes,
  [The Stochastic-Quantum Theorem](https://arxiv.org/html/2309.03085v2).
- Barandes,
  [New Prospects for a Causally Local Formulation of Quantum Theory](https://arxiv.org/abs/2402.16935).
- Barandes,
  [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192).
- Barandes,
  [A Deflationary Account of Quantum Theory and its Implications for the Complex Numbers](https://arxiv.org/abs/2602.01043).
- Pollock et al.,
  [Non-Markovian Quantum Processes: Complete Framework and Efficient Characterization](https://arxiv.org/abs/1512.00589).
- Pollock et al.,
  [Operational Markov Condition for Quantum Processes](https://arxiv.org/abs/1801.09811).
- Bengtsson et al.,
  [Birkhoff's Polytope and Unistochastic Matrices](https://arxiv.org/abs/math/0402325).

## Bounded bridge search

Targeted arXiv searches through 2026-07-26 located no explicit paper joining:

- causal fermion systems and Barandes;
- causal fermion systems and process tensors;
- causal fermion systems and GPT reconstruction; or
- causal fermion systems and quantum causal models.

Classification: `BOUNDED_SEARCH_NULL`. Future work must say “not located in
the bounded search,” never “the literature does not exist.”

## Final research meaning

This collision does not hand DU the missing theory. It improves the program's
type system:

```text
physical law selects a completion class
    != record selects/refines information
    != representation embeds observed statistics
    != observer target is reconstructible
```

Finster makes the first arrow scientifically serious. Barandes makes the
third arrow easy enough that it cannot be mistaken for either the first or
the fourth. Dynamic Unity's live contribution remains the exact relation
among all four.
