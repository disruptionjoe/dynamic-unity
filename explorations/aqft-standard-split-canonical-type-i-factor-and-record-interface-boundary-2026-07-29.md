---
title: "AQFT standard split inclusions: canonical type-I factor, finite state compression, and record-interface boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-133
work_id: CCR-AQFT-STANDARD-SPLIT-CANONICAL-FACTOR-BOUNDARY
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
novelty_status: absorbed_mathematics_typed_du_correction
---

# AQFT standard split inclusions: canonical type-I factor, finite state compression, and record-interface boundary

## Result in one paragraph

Dynamic Unity's prior statement was too broad. The split property by itself
only asserts that at least one intermediate type-I factor exists, and there
can be infinitely many. But a **standard split inclusion**
\(\Lambda=(A,B,\Omega)\)—a split inclusion equipped with a vector cyclic and
separating for \(A\), \(B\), and \(A'\cap B\)—does canonically select one:

\[
N_\Lambda
 =A\vee J_\Lambda A J_\Lambda
 =B\cap J_\Lambda B J_\Lambda ,
\]

for factorial endpoints, where \(J_\Lambda\) is the modular conjugation of
\((A'\cap B,\Omega)\). The construction is natural under unitary equivalences
of the full triple. This is a genuine conditional subsystem selector, not
merely an existence result. In nontrivial AQFT examples the selected factor is
type \(I_\infty\), not finite-dimensional. The distinguished state restricted
to it has a faithful trace-class density operator of infinite rank. A declared
spectral tolerance then canonically selects finite-rank, basis-free
compressions with vanishing reference-state error, but those compressions do
not uniformly approximate all normal states, do not remain intermediate
factors containing the inner local algebra, and do not select a detector,
instrument, pointer, archive, access rule, or actual record formation.

## 1. Why this audit was necessary

`HC-DU-131` said:

> The split property inserts a type-I factor between nested local algebras but
> does not canonically choose one intermediate type-I factor.

That sentence is correct only if “the split property” means the bare inclusion
\(A\subset B\) together with existence of some type-I interpolation. It is
false as a statement about **standard split inclusions**. Doplicher and Longo
proved that the additional standard vector supplies a canonical intermediate
factor.

This matters to Dynamic Unity because “selection” must be graded relative to
the antecedent. A construction can fail to select a net or state and still
genuinely select a subsystem boundary once that net, state, and region pair
are physically fixed. Calling all such structure “supplied” flattened a real
selector rung.

The correction does **not** turn the split property into a record theory. It
locates the gain precisely:

```text
bare split inclusion
  -> at least one type-I interpolation
  -> generally plural

standard split triple (A, B, Ω)
  -> one canonical type-I interpolation N_Λ
  -> exact subsystem/tensor-product arena
  -/-> finite subsystem
  -/-> measurement interface
  -/-> formed record
```

## 2. Primary-source boundary

The core result is due to Doplicher and Longo,
[“Standard and split inclusions of von Neumann algebras”](https://doi.org/10.1007/BF01388641),
*Inventiones Mathematicae* 75 (1984), 493–536.

Three later primary sources make the scope especially clear:

- [Fewster, “The split property for locally covariant quantum field theories
  in curved spacetime”](https://arxiv.org/abs/1501.02682) constructs states
  whose local inclusions are both split and standard, states the canonical
  tensor-product implementation, and notes that the resulting intermediate
  factor is type \(I_\infty\) in the nontrivial case.
- [Weiner, “An algebraic Haag's theorem”](https://arxiv.org/abs/1006.4726)
  gives the modular-conjugation formula and records invariance of the canonical
  factor under unitaries preserving the inclusion and standard vector.
- [Longo and Xu, “Von Neumann Entropy in
  QFT”](https://doi.org/10.1007/s00220-020-03702-7) emphasizes both sides:
  a split inclusion has infinitely many intermediate type-I factors, while
  the nested regions together with the vacuum vector select the canonical
  factor and a vacuum density matrix on it.

The operator-algebra theorem is mature. No new AQFT theorem is claimed here.
The Dynamic Unity increment is the corrected selector taxonomy and the exact
finite-state-compression boundary below.

## 3. Typed definitions

Let \(A\subset B\subset B(\mathcal H)\) be von Neumann algebras.

### 3.1 Split inclusion

The inclusion is **split** if there exists a type-I factor \(N\) such that

\[
A\subset N\subset B.
\]

This is an existence statement. It need not identify one \(N\).

### 3.2 Standard vector

A unit vector \(\Omega\in\mathcal H\) is standard for the inclusion when it is
cyclic and separating for

\[
A,\qquad B,\qquad A'\cap B.
\]

The triple

\[
\Lambda=(A,B,\Omega)
\]

is a **standard split inclusion** when the inclusion is split and \(\Omega\)
is standard.

### 3.3 Canonical factor

Let

\[
J_\Lambda=J_{A'\cap B,\Omega}
\]

be the Tomita--Takesaki modular conjugation of the relative commutant with
respect to \(\Omega\). If \(A\) and \(B\) are factors, Doplicher--Longo give

\[
\boxed{
N_\Lambda
 =A\vee J_\Lambda A J_\Lambda
 =B\cap J_\Lambda B J_\Lambda
}
\]

and prove

\[
A\subset N_\Lambda\subset B,
\qquad
N_\Lambda\text{ is type I}.
\]

If only one endpoint is known to be a factor, the corresponding formula is
still available under the theorem's stated hypotheses.

There is a unitary split implementation

\[
W_\Lambda:\mathcal H\longrightarrow\mathcal H\otimes\mathcal H
\]

that sends the inside/outside product algebra to its tensor-product
representation and satisfies, in the standard AQFT presentation,

\[
N_\Lambda
 =
W_\Lambda^{-1}
\big(B(\mathcal H)\otimes \mathbf 1\big)
W_\Lambda.
\]

The exact Hilbert-factor labels are representation bookkeeping. The invariant
content is the selected intermediate type-I factor and induced subsystem
factorization.

## 4. Proposition A — this is genuine relative selection

Let \(U:\mathcal H\to\widetilde{\mathcal H}\) be unitary and set

\[
\widetilde A=UAU^*,\qquad
\widetilde B=UBU^*,\qquad
\widetilde\Omega=U\Omega.
\]

Tomita--Takesaki covariance gives

\[
J_{\widetilde\Lambda}=UJ_\Lambda U^*.
\]

Therefore

\[
\begin{aligned}
N_{\widetilde\Lambda}
 &=\widetilde A\vee
   J_{\widetilde\Lambda}\widetilde A J_{\widetilde\Lambda}\\
 &=UAU^*\vee UJ_\Lambda A J_\Lambda U^*\\
 &=UN_\Lambda U^* .
\end{aligned}
\]

Thus the construction is equivariant under equivalence of the full standard
split triple. In particular, every unitary symmetry that preserves \(A\),
\(B\), and \(\Omega\) preserves \(N_\Lambda\).

This earns point-selection credit at the declared antecedent:

\[
(A,B,\Omega)\longmapsto N_\Lambda.
\]

It does **not** earn

\[
\text{physical laws alone}
\longmapsto
(A,B,\Omega).
\]

Those are different selection questions.

## 5. Exactly what remains antecedent

The canonical factor depends on a typed packet:

| Input | Physical meaning | Selected by the modular construction? |
|---|---|---:|
| QFT net and representation | Which local observables exist | No |
| Nested regions / inclusion \(A\subset B\) | Inner region plus collar/outer region | No |
| State or standard vector \(\Omega\) | Vacuum or other admitted reference state | No |
| Split property | Existence of a type-I interpolation | No; hypothesis/theory result |
| Standardness | Modular construction is well-typed | No; hypothesis/theory result |
| \(N_\Lambda\) | Canonical intermediate subsystem factor | **Yes, relative to the packet** |

In Minkowski vacuum AQFT, covariance and the spectrum condition may make the
vacuum physically distinguished, so it would be wrong to dismiss
\(\Omega\) as merely arbitrary. Likewise, a concrete observer, detector
region, or causal experiment can physically fix the nested region pair. In
that case the canonical factor is a physically meaningful conditional
selector.

There is no generally covariant preferred-state selection for arbitrary
curved spacetimes. Fewster's
[natural-state no-go](https://arxiv.org/abs/1105.6202) shows that, under
dynamical locality and the stated Reeh--Schlieder/faithfulness hypotheses, a
covariantly preferred natural state would trivialize the theory. The
state-relative qualifier is therefore not removable in general by simply
asking local covariance to choose \(\Omega\).

## 6. Proposition B — the selected factor is generally infinite

Fewster's nontrivial standard split construction has properly infinite local
endpoint algebras on an infinite-dimensional separable Hilbert space. Its
canonical intermediate factor is

\[
N_\Lambda\cong B(\mathcal K)
\]

for a countably infinite-dimensional \(\mathcal K\). Hence

\[
N_\Lambda\text{ is type }I_\infty,
\]

not \(M_n(\mathbb C)\).

This distinction is load-bearing:

```text
type I
  -> ordinary subsystem/tensor-product and density-matrix language

type I∞
  -/-> finitely many degrees of freedom
  -/-> finite-dimensional state
  -/-> finite output alphabet
  -/-> finite record
```

The standard vector is cyclic for \(A\subset N_\Lambda\), so it is cyclic for
\(N_\Lambda\). It is separating for \(B\supset N_\Lambda\), so it is
separating for \(N_\Lambda\). Thus its restricted normal state is faithful.

Under \(N_\Lambda\cong B(\mathcal K)\), there is a density operator

\[
\rho_\Lambda\geq0,\qquad
\operatorname{Tr}\rho_\Lambda=1,
\qquad
\omega_\Omega(X)=\operatorname{Tr}(\rho_\Lambda X).
\]

Faithfulness gives

\[
\ker\rho_\Lambda=\{0\}.
\]

Because \(\mathcal K\) is infinite-dimensional,

\[
\operatorname{rank}\rho_\Lambda=\infty.
\]

Therefore the canonical standard-split state has no exact finite support.

Longo--Xu show that its von Neumann entropy can nevertheless be finite in
particular conformal free-fermion models. Finite entropy and finite rank are
not the same claim.

## 7. Proposition C — a canonical finite reference-state compression exists

Although \(\rho_\Lambda\) has infinite rank, it is trace class. For every
declared spectral threshold \(\tau>0\), define

\[
P_\tau=\mathbf1_{[\tau,\infty)}(\rho_\Lambda).
\]

### 7.1 Finite rank

If \(r_\tau=\operatorname{rank}P_\tau\), every retained eigenvalue is at least
\(\tau\), so

\[
1=\operatorname{Tr}\rho_\Lambda
\geq r_\tau\tau.
\]

Hence

\[
\boxed{r_\tau\leq \lfloor1/\tau\rfloor.}
\]

The projection is basis-free and includes complete degenerate eigenspaces.
Under an equivalence of standard split triples, the induced normal
isomorphism of the canonical type-I factors carries their restricted states
and density operators into one another. In coherent spatial
representations, for the induced unitary \(\widehat U\),

\[
\rho_{\widetilde\Lambda}=\widehat U\rho_\Lambda\widehat U^*
\quad\Longrightarrow\quad
P_{\tau,\widetilde\Lambda}
=\widehat U P_{\tau,\Lambda}\widehat U^*.
\]

### 7.2 Vanishing reference-state tail

Let

\[
\delta_\tau
=\operatorname{Tr}\big(\rho_\Lambda(1-P_\tau)\big).
\]

Trace-class spectral summability gives

\[
\delta_\tau\longrightarrow0
\qquad(\tau\downarrow0).
\]

For \(0<\tau\leq\|\rho_\Lambda\|\), the projection is nonzero. Normalize the
compressed state:

\[
\rho_{\Lambda,\tau}
=\frac{P_\tau\rho_\Lambda P_\tau}{1-\delta_\tau}.
\]

Because \(P_\tau\) commutes with \(\rho_\Lambda\),

\[
\boxed{
\|\rho_\Lambda-\rho_{\Lambda,\tau}\|_1=2\delta_\tau.
}
\]

Therefore every effect \(0\leq E\leq1\) obeys

\[
\left|
\operatorname{Tr}(\rho_\Lambda E)
-\operatorname{Tr}(\rho_{\Lambda,\tau}E)
\right|
\leq\delta_\tau,
\]

and every bounded observable \(X\) obeys

\[
\left|
\operatorname{Tr}((\rho_\Lambda-\rho_{\Lambda,\tau})X)
\right|
\leq2\delta_\tau\|X\|.
\]

This is an exact positive result:

> A standard split triple plus a declared spectral tolerance canonically
> selects a finite-dimensional, basis-free approximation of its distinguished
> reference state.

It improves on a pure width count: a subspace is actually selected.

## 8. Why the finite compression is not yet a finite physical record

The positive result has four exact limits.

### 8.1 It is state-relative, not uniform

For every finite \(P_\tau\) in infinite-dimensional \(\mathcal K\), choose a
unit vector \(e\in(1-P_\tau)\mathcal K\). The normal pure state

\[
\varphi_e(X)=\langle e,Xe\rangle
\]

has

\[
\varphi_e(P_\tau)=0.
\]

The same projection that approximates \(\omega_\Omega\) arbitrarily well
therefore loses all probability mass for another normal state.

So:

\[
\text{reference-state approximation}
\neq
\text{uniform local-state/process reconstruction}.
\]

A larger admitted state class would require an independently justified
uniform domination, compactness, energy, entropy, or phase-space condition.

### 8.2 Compression is not interpolation

The corner

\[
P_\tau N_\Lambda P_\tau\cong M_{r_\tau}(\mathbb C)
\]

is finite-dimensional, but it is a compression. In general it is not an
intermediate factor satisfying

\[
A\subset P_\tau N_\Lambda P_\tau\subset B.
\]

It therefore does not replace the exact local subsystem by a finite
subsystem while preserving all inner-algebra actions.

### 8.3 A probability tolerance remains supplied

The triple selects the spectrum. It does not select \(\tau\), a tolerated
tail \(\delta\), a held-out target error, or a resource budget. These are
operational contracts unless another physical mechanism fixes them.

### 8.4 Algebra is not acquisition

Neither \(N_\Lambda\) nor \(P_\tau\) specifies:

- a probe theory;
- a coupling and instrument;
- a pointer basis or output alphabet;
- blank-to-written material change;
- acquisition attempts and rejected strata;
- provenance and authentication;
- durable archive;
- observer access and decoder;
- future action envelope and finality; or
- an actual outcome in one run.

The modular construction selects an algebraic subsystem boundary. A physical
record remains a process involving formation and retained access.

## 9. Corrected selector ladder

| Rung | Exact return | Grade/type | What remains open |
|---:|---|---|---|
| 0 | Supplied net/representation | antecedent | theory and physical realization |
| 1 | Supplied nested regions \(A\subset B\) | observer/geometry indexed | why this collar is the relevant one |
| 2 | Split property | known structural condition | only existence of some type-I factor |
| 3 | Standard vector \(\Omega\) | state antecedent | state selection outside special vacuum settings |
| 4 | Canonical \(N_\Lambda\) | exact conditional point selector | infinite subsystem; no measurement |
| 5 | Canonical \(\rho_\Lambda\) | exact reference-state density | infinite rank |
| 6 | \(P_\tau N_\Lambda P_\tau\) | finite reference-state approximation | tolerance, nonuniformity, lost action closure |
| 7 | Realized finite instrument | measurement architecture | not selected here |
| 8 | Formed retained certified record | North-Star input | formation, lineage, access, finality |
| 9 | Held-out target factorization | reconstruction/duality/remainder verdict | requires no-refit transfer |

The correction is at rungs 4–6. The North Star is not closed because rungs
7–9 remain.

## 10. Relationship to recent Dynamic Unity results

### `HC-DU-128`

GNS reconstructs a representation from a complete positive functional on a
fixed algebra. The standard split result supplies a canonical type-I algebra
relative to a richer triple, so the state restriction admits an ordinary
density matrix. It does not turn that complete theoretical state into a
formed finite record.

### `HC-DU-129--130`

A supplied finite Gaussian sector has finite population-level sufficient
statistics, while a single fixed finite local sector cannot be translation
invariant on noncompact continuum spacetime. The standard split factor is
covariantly defined relative to nested regions and state, but it is
infinite-dimensional. Its finite spectral corner is an indexed,
state-relative approximation, not one globally invariant local mode packet.

### `HC-DU-131`

Nuclearity can imply the split property and control finite-resolution local
phase space. The corrected statement is:

```text
nuclearity/split alone
  -/-> one canonical intermediate factor

standard split triple
  -> one canonical intermediate factor
  -/-> finite formed record.
```

The prior broad sentence is superseded by this typed version.

### `HC-DU-132`

The Hamiltonian selects a low-energy spectral subspace, but it can remain
infinite-dimensional on noncompact space. The canonical split density matrix
offers a different selector:

```text
Hamiltonian cutoff:
  state-family/energy motivated, generally infinite low-energy rank

canonical split-state cutoff:
  finite rank at every positive eigenvalue threshold,
  but only approximates the distinguished split state
```

Neither selects a detector or archive. Their possible composition would
require a common, frozen physical target and a proof that the state-relative
compression controls the admitted excitation/process family.

### `HC-DU-040B` and `HC-DU-057`

The type-I interpolation does not refute the full-factor internal-record
boundary. A nontrivial sharp record cannot be both internal to a factor and
nondisturbing for every factor action. The split construction gives a
subsystem arena in which ordinary instruments can be defined; it does not
make a pointer central or final.

## 11. Strongest possible positive interpretation

The result deserves more credit than “AQFT supplies no interface.”

If a physical theory and experiment independently fix:

1. a local net and representation;
2. a nested region pair;
3. a distinguished standard state, such as a unique vacuum; and
4. a finite probability tolerance;

then standard split theory canonically returns:

1. an exact subsystem boundary \(N_\Lambda\);
2. an ordinary density-matrix state on that subsystem; and
3. a finite basis-free reference-state compression with explicit trace error.

That is a serious partial solution to the interface-selection problem. It
turns an arbitrary-factor objection into a state-and-collar dependency
statement.

## 12. Cheapest kills of stronger readings

### Strong reading 1

> The split property itself chooses the subsystem.

**Kill:** one split inclusion can have infinitely many intermediate type-I
factors. The standard vector is load-bearing.

### Strong reading 2

> The canonical type-I factor is a finite subsystem.

**Kill:** nontrivial standard AQFT inclusions give type \(I_\infty\).

### Strong reading 3

> The canonical spectral corner approximates every local state.

**Kill:** a normal pure state supported in \(1-P_\tau\) is missed completely.

### Strong reading 4

> The finite corner is an exact finite replacement of the local inclusion.

**Kill:** compression generally does not contain \(A\) and does not preserve
the full action algebra.

### Strong reading 5

> The selected algebra is already a record.

**Kill:** no probe, write, output, lineage, archive, observer access, or
outcome rule follows from the modular construction.

## 13. Novelty and evidence grade

### Established literature

- standard split inclusions;
- the canonical modular type-I factor;
- its tensor-product implementation and covariance;
- type \(I_\infty\) in the nontrivial AQFT setting;
- vacuum density matrices and canonical split entanglement entropy.

### Direct elementary consequence used here

- finite-rank spectral threshold \(P_\tau\);
- \(r_\tau\leq1/\tau\);
- exact trace-norm truncation error \(2\delta_\tau\);
- failure of uniform state approximation by a complement-supported normal
  state.

### Dynamic Unity increment

- correction of the prior split-property nonselection statement;
- separation of bare-split existence from standard-triple point selection;
- recognition of a canonical finite reference-state approximation rung;
- proof that this rung still does not supply a uniform finite process or
  formed certified record.

**Grade:** scoped Grade 4 for the exact selector dependency,
type-\(I_\infty\), finite-compression, and nonuniformity boundaries; conditional
Grade 3 for reference-state finite-resolution reconstruction after the full
triple and tolerance are independently fixed.

No empirical excess, new AQFT theorem, new law, new physics, prediction, paper
promotion, hardware path, or selected scientific successor is earned.

## 14. Disposition

Bank the correction and leave Dynamic Unity quiescent.

The next reopener should not ask again whether “the split property” selects
anything. It should ask one of two sharper questions:

1. Does a concrete physical QFT process independently select the standard
   triple and turn its canonical factor into a realized probe--pointer--archive
   interface?
2. Can a physically warranted state/process class be shown uniformly
   controlled by the canonical split spectral compressions, with a held-out
   target and no refitting?

Until one of those has a concrete antecedent, the honest return is:

```text
CANONICAL_SUBSYSTEM_RELATIVE_TO_STANDARD_TRIPLE
PLUS_FINITE_REFERENCE_STATE_APPROXIMATION
BUT_NO_FORMED_RECORD_OR_UNIFORM_PROCESS_RECONSTRUCTION
```
