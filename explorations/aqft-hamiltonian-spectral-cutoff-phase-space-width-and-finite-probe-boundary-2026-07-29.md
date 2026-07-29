---
title: "AQFT Hamiltonian spectral cutoff, phase-space width, and the finite-probe boundary"
status: completed_scoped_result
doc_type: aqft_natural_cutoff_infinite_rank_width_and_conditional_local_probe_boundary
created: 2026-07-29
hypothesis_id: HC-DU-132
run_id: RUN-20260729-162943-aqft-spectral-cutoff-width-finite-probe-boundary
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
warrants:
  - DERIVED
  - CONSTRUCTIVELY_REALIZED
maximum_grade: "Scoped Grade 4 Hamiltonian-cutoff tail, noncompact-QFT infinite-rank, and phase-space-width/nonselection boundary plus conditional Grade 3 finite-resolution local-probe certification; no selected QFT, state, region, cutoff, target, probe, observer, archive, empirical excess, new AQFT theorem, new law, new physics, or prediction"
probe: "../tests/du_aqft_spectral_cutoff_width_probe.py"
artifact: "../tests/artifacts/du_aqft_spectral_cutoff_width_result.json"
---

# AQFT spectral cutoff, phase-space width, and finite probes

## Executive result

`HC-DU-131` found a real continuum middle: AQFT nuclearity can make the
energy-damped local possibility set finitely approximable at every nonzero
resolution. It did not say whether the physics also chooses the finite
approximation.

This swing tests the strongest obvious selector: the Hamiltonian's own
low-energy spectral projection.

The answer is mixed and exact:

```text
Hamiltonian H + supplied cutoff E
  -> canonical basis-free low-energy projection P_E
  -> exponentially bounded discarded energy-damped tail

noncompact continuum QFT
  + local cyclicity
  + infinitely many low-energy modes
  -> projected local map still has infinite rank

compact resolvent
  -> every bounded spectral projection has finite rank
  -/-> selected detector, coordinates, archive, or observer

nuclear / compact phase-space image
  -> basis-free approximation widths and finite dimension at tolerance eta
  -/-> one selected approximating subspace or physical probe

compact target class
  + target-separating local observables
  + admitted local probe schemes
  + repeatable or jointly compatible campaign
  + complete sub-margin acquisition
  -> conditional finite-resolution local record

NO READY SUCCESSOR
```

The Hamiltonian closes more than an arbitrary truncation. It selects a
physically meaningful **family** of low-energy subspaces and a tail norm. But
in the ordinary noncompact field arena it does not make those subspaces
finite-dimensional. The low-energy sector still contains continuously many
independent wave packets.

This identifies a smallest honest repair:

> A finite physical record needs either additional spectral compactness, such
> as compact resolvent, or a target-relative finite approximation of the
> compact local phase-space image. Neither route by itself selects the
> measurement interaction or forms a record.

The strongest positive composition now available is conditional but physical.
On a compact target class, finitely many local observables suffice whenever
the admitted local observable family separates all target-distinct pairs.
For the quantized real linear scalar field, Fewster, Jubb, and Ruep show that
every local observable has asymptotic local measurement schemes. At fixed
nonzero accuracy, the selected finite observable family can therefore be
paired with finitely many probe schemes. This reaches physical
**realizability**, not physical **selection**.

The mathematical components are mature. The contribution to Dynamic Unity is
the typed boundary among:

1. a law-selected approximation envelope;
2. the size of the smallest adequate approximation;
3. the choice of approximating subspace;
4. realizability of selected observables;
5. formation and certification of a record; and
6. target-relative reconstruction.

## 1. Frozen typed packet

Let:

- \(\mathcal H\) be a supplied Hilbert space;
- \(H\geq0\) be a supplied self-adjoint Hamiltonian;
- \(\Omega\in\mathcal H\) be a normalized supplied reference vector;
- \(O\) be a supplied bounded spacetime region;
- \(\mathcal A(O)\) be its supplied local observable algebra;
- \(\beta>0\) be a supplied damping scale; and
- \(E\geq0\) be a supplied energy cutoff.

Define

\[
\Theta_{\beta,O}(A)
=
e^{-\beta H}A\Omega
\tag{1}
\]

and the spectral projection

\[
P_E
=
\mathbf 1_{[0,E]}(H).
\tag{2}
\]

The projected local map is

\[
\Theta_{\beta,O}^{(E)}(A)
=
P_Ee^{-\beta H}A\Omega.
\tag{3}
\]

Keep the following objects distinct:

| Object | What selects or supplies it | What it does not yet supply |
|---|---|---|
| \(H\) | supplied QFT representation and dynamics | one cutoff or observer |
| \(P_E\) | spectral calculus after \(E\) is supplied | finite rank in general |
| \(\Theta_{\beta,O}\) | supplied net, region, state, \(H,\beta\) | detector or record |
| compact/nuclear image | physical phase-space condition | coordinates |
| width \(d_n\) or approximation number | image plus norm | approximating subspace |
| finite observable family | target-relative mathematical selection | measurement campaign |
| probe scheme | supplied probe theory, state, coupling, and readout | provenance-complete archive |
| certified record | physical interaction plus acquisition and retention | universal target sufficiency |

The state and algebra are ontic/theoretical antecedents in this packet. Their
being supplied is not an epistemic denial of their physical reality. It is a
claim about what this theorem does and does not derive.

## 2. The Hamiltonian selects an error envelope

### Theorem 1 — spectral-tail bound

For every \(A\in\mathcal A(O)\),

\[
\left\|
\left(1-P_E\right)e^{-\beta H}A\Omega
\right\|
\leq
e^{-\beta E}\|A\|.
\tag{4}
\]

### Proof

The spectral theorem gives

\[
\left\|
\left(1-P_E\right)e^{-\beta H}
\right\|
\leq
\sup_{\lambda>E}e^{-\beta\lambda}
\leq
e^{-\beta E}.
\tag{5}
\]

Since \(\|\Omega\|=1\),

\[
\|A\Omega\|
\leq
\|A\|.
\tag{6}
\]

Combining (5) and (6) gives (4). \(\square\)

### Corollary — target error after the spectral projection

Let \(F\) be \(L\)-Lipschitz on the energy-damped image. If

\[
\Theta_{\beta,O}^{(E)}(A)
=
\Theta_{\beta,O}^{(E)}(B)
\tag{7}
\]

for \(\|A\|,\|B\|\leq1\), then

\[
\left|
F\big(\Theta_{\beta,O}(A)\big)
-
F\big(\Theta_{\beta,O}(B)\big)
\right|
\leq
2Le^{-\beta E}.
\tag{8}
\]

The proof is the same two-tail triangle inequality as `HC-DU-131`.

This is a stronger physical statement than “some finite-rank approximation
exists.” Once \(E\) is declared, the Hamiltonian itself defines the retained
subspace and the discarded-tail bound without choosing a basis.

It still leaves three questions:

1. Is the retained subspace finite-dimensional?
2. What value of \(E\) is physically warranted for the observer task?
3. How is the retained information physically measured and archived?

The first question already fails in the generic noncompact arena.

## 3. Why a low-energy QFT sector is still infinite

### Theorem 2 — cyclic local excitation makes the projected map dense

Assume:

1. \(\Omega\) is cyclic for \(\mathcal A(O)\), so
   \(\overline{\mathcal A(O)\Omega}=\mathcal H\); and
2. \(P_E\mathcal H\) is infinite-dimensional.

Then the map

\[
A
\longmapsto
P_Ee^{-\beta H}A\Omega
\tag{9}
\]

has infinite rank. More strongly, its range is dense in
\(P_E\mathcal H\).

### Proof

Let

\[
T_E=P_Ee^{-\beta H}.
\tag{10}
\]

Because \(P_E\) and \(e^{-\beta H}\) are functions of \(H\), they commute.
On \(P_E\mathcal H\), the inverse \(e^{\beta H}\) is bounded by
\(e^{\beta E}\). Therefore

\[
T_E\mathcal H=P_E\mathcal H.
\tag{11}
\]

Cyclicity gives

\[
\overline{\mathcal A(O)\Omega}=\mathcal H.
\tag{12}
\]

Continuity of \(T_E\) implies

\[
P_E\mathcal H
=
T_E\mathcal H
\subseteq
\overline{T_E\mathcal A(O)\Omega}.
\tag{13}
\]

The reverse inclusion is immediate, so the closure of the projected local
range is \(P_E\mathcal H\). If (9) had finite rank, its range would lie in a
finite-dimensional closed subspace, and its closure would also be
finite-dimensional. This contradicts assumption 2. \(\square\)

Reeh and Schlieder established the cyclicity property for local field
algebras in the standard relativistic QFT setting
([primary source](https://doi.org/10.1007/BF02787889)). The theorem above
does not claim that every possible QFT representation and region satisfies
those hypotheses. It states exactly what follows when they do.

### Free massive-field witness

For a free massive scalar field on noncompact \(d\)-dimensional space, the
one-particle Hilbert space can be represented as an \(L^2\) space in momentum,
and the one-particle Hamiltonian acts by multiplication with

\[
\omega(p)=\sqrt{|p|^2+m^2}.
\tag{14}
\]

For \(E>m\), the spectral sector

\[
\left\{
\psi:
\operatorname{supp}\psi
\subseteq
\left\{
p:\omega(p)\leq E
\right\}
\right\}
\tag{15}
\]

contains the \(L^2\) space over a positive-measure momentum ball. That space
is infinite-dimensional. It already sits inside the full low-energy Fock
sector.

Therefore:

```text
bounded energy
  != finitely many modes
  != finite rank
```

The exact reason is continuous spectral multiplicity, not merely “QFT has
infinitely many degrees of freedom.”

### Relation to `HC-DU-130`

`HC-DU-130` showed that translating one nonzero compactly supported mode
generates an infinite-dimensional global orbit. The present theorem reaches
the same finite/infinite boundary from a different direction:

```text
local covariance route:
  moving a finite local packet through continuum regions
  -> infinite global orbit

spectral route:
  fixing one region but retaining all low-energy local excitations
  -> infinite projected local range.
```

The two results block different shortcuts. Localizing the packet does not
make its global family finite; bounding energy does not make its local
possibility sector finite.

## 4. An exact finite-rank escape: compact resolvent

### Proposition 3

If \(H\) has compact resolvent, then \(P_E\) has finite rank for every finite
\(E\).

### Reason

A self-adjoint operator with compact resolvent has discrete spectrum with
finite multiplicities and no finite accumulation point. Only finitely many
eigenvalues, counted with multiplicity, lie in a bounded interval.

Thus

\[
\operatorname{rank}P_E<\infty.
\tag{16}
\]

The projected local map (3) is then finite-rank.

This is one exact sufficient mathematical escape, but its typing matters:

```text
compact-resolvent Hamiltonian
  -> finite low-energy spectral sector

finite low-energy spectral sector
  -/-> preferred cutoff value
  -/-> preferred basis within degenerate sectors
  -/-> detector
  -/-> blank-to-written record
  -/-> complete observer access.
```

Finite-volume, confining, or compact-spatial models can produce this spectral
behavior under additional hypotheses. Importing one of those models changes
the physical arena. It is not evidence that the ordinary noncompact theory
already contained a finite low-energy record.

The positive is still valuable. It identifies a concrete antecedent that
converts the Hamiltonian-selected approximation family into a genuinely
finite-dimensional family. A future physical reconstruction theorem may use
that antecedent if the arena independently warrants it.

## 5. Basis-free phase-space size

The failure of finite-rank spectral cutoff does not erase the nuclearity
positive. The correct next object is the approximation complexity of the
compact image, not an arbitrary coordinate list.

Let \(K\subset\mathcal H\) be compact. Its \(n\)-th Kolmogorov width is

\[
d_n(K)
=
\inf_{\dim V\leq n}
\sup_{y\in K}
\operatorname{dist}(y,V).
\tag{17}
\]

At tolerance \(\eta>0\), define the minimum approximation dimension

\[
N_K(\eta)
=
\min\left\{
n:
d_n(K)\leq\eta
\right\},
\tag{18}
\]

when the set is nonempty.

For a compact \(K\), \(d_n(K)\to0\), so \(N_K(\eta)\) is finite at every
positive tolerance.

These quantities are:

- invariant under unitary changes of Hilbert-space coordinates;
- relative to a declared norm and image \(K\);
- target-independent if \(K\) is fixed independently of a held-out target;
- quantitative rather than a finite/infinite slogan; and
- silent about which physical detector realizes an approximating subspace.

For a compact operator between Hilbert spaces with decreasing singular values
\(s_1\geq s_2\geq\cdots\), the image of the unit ball is an ellipsoid and

\[
d_n=s_{n+1}.
\tag{19}
\]

For the AQFT map, the domain is generally a Banach algebra rather than a
Hilbert space, so one must not silently import a canonical singular-value
decomposition. Approximation numbers or widths remain well-defined
basis-free values, while a unique decomposition need not.

### Equal nuclear norm, different finite-resolution cost

Consider two positive diagonal Hilbert-space controls.

The infinite geometric map has singular values

\[
s_j=2^{-j},
\qquad
j=1,2,\ldots,
\tag{20}
\]

so

\[
\sum_js_j=1,
\qquad
d_n=2^{-(n+1)}.
\tag{21}
\]

The rank-\(M\) flat map has

\[
t_1=\cdots=t_M=\frac1M,
\qquad
t_j=0\quad(j>M),
\tag{22}
\]

and also

\[
\sum_jt_j=1.
\tag{23}
\]

But its width profile is

\[
d_n=
\begin{cases}
\frac1M,&n<M,\\
0,&n\geq M.
\end{cases}
\tag{24}
\]

The two maps have equal nuclear/trace norm and very different approximation
profiles. Therefore:

```text
one nuclearity index
  != complete finite-resolution dimension law.
```

Quantitative nuclearity bounds can constrain widths or approximation numbers,
but the whole decay profile matters.

### Size is not selection

Even a fully known width sequence does not encode:

- an optimizing subspace;
- a basis inside that subspace;
- a localized observable family;
- a coupling to a probe;
- a readout;
- an archive; or
- an observer access relation.

Degenerate width profiles can admit whole families of equally optimal
subspaces or coordinate bases. `HC-DU-131` supplied the exact two-dimensional
rotation control: the full irreducible multiplet is invariant, while no
rank-one coordinate is invariant.

Thus the strongest law-side object earned here is:

> a physically typed approximation complexity profile, not a finite record
> interface.

This direction is heavily absorbed. Buchholz and Porrmann explicitly asked
how small QFT phase space is, compared compactness and nuclearity conditions,
and developed quantitative variants
([primary source](https://www.numdam.org/item/AIHPA_1990__52_3_237_0.pdf)).
The component mathematics also belongs to mature approximation theory. DU
should use these tools rather than claim them.

## 6. Conditional finite local-probe packet

The Hamiltonian does not make a finite low-energy sector in the noncompact
arena. Nuclearity nevertheless makes the energy-damped image compact enough
for a target-relative finite reduction.

### Theorem 4 — finite target-separating local observables

Let:

- \(\Theta\) be a compact physical completion class;
- \(T:\Theta\to Z\) be a continuous target;
- \(\delta>0\) be a declared target resolution; and
- \(\mathcal M_{\mathrm{loc}}\) be a family of continuous local observable
  statistics.

Assume \(\mathcal M_{\mathrm{loc}}\) separates every pair
\(\theta,\theta'\) satisfying

\[
d_Z\big(T(\theta),T(\theta')\big)\geq\delta.
\tag{25}
\]

Then there are finitely many statistics

\[
m_1,\ldots,m_N\in\mathcal M_{\mathrm{loc}}
\tag{26}
\]

and a margin \(\gamma_\delta>0\) such that every pair satisfying (25)
obeys

\[
\max_i
\left|
m_i(\theta)-m_i(\theta')
\right|
\geq
\gamma_\delta.
\tag{27}
\]

This is exactly the compact finite-subcover theorem proved and graded in
`HC-DU-095`. It is repeated here only to compose it with a physical QFT
realizability result.

### Realizability in the linear scalar field

Fewster, Jubb, and Ruep show that every local observable of the quantized real
linear scalar field has asymptotic measurement schemes. Their construction
retains:

- a probe theory;
- an initial probe state;
- a coupling region and coupling;
- a processing/readout observable; and
- an accuracy/resource limit.

Compact coupling regions can be used in the asymptotic schemes
([primary source](https://arxiv.org/abs/2203.09529)). The broader
Fewster--Verch framework types how a local system-probe coupling induces a
system observable
([primary framework](https://arxiv.org/abs/1810.06512);
[review](https://arxiv.org/abs/2304.13356)).

For the finite family (26), choose one admitted scheme per observable at
accuracy \(\epsilon_i\). If:

1. the completion can be prepared repeatedly without changing the frozen
   target, or the schemes form one jointly compatible sequential campaign;
2. approximation, calibration, sampling, digitization, missing-attempt, drift,
   and archive errors compose to less than \(\gamma_\delta/2\);
3. all attempted runs and their trial identities are retained;
4. the outputs are joined to the correct source/probe histories; and
5. the observer can access and act on the retained packet,

then the packet certifies \(T\) to resolution \(\delta\).

This is a real conditional bridge:

```text
mathematically finite local separator
  + physically admitted local measurement schemes
  -> finite physically realizable probe family at fixed accuracy.
```

It is not an endogenous selector:

```text
QFT law
  -/-> target T
  -/-> compact completion class Theta
  -/-> observable family M_loc
  -/-> selected finite subfamily
  -/-> probe theory / state / coupling / readout
  -/-> complete archive / observer access.
```

“Every local observable is measurable” answers a capability question. It
does not answer why this observable, probe, region, target, or archive is
physically instantiated.

### Exact role of the Hamiltonian

The Hamiltonian and nuclearity can help with the first two premises:

- they may make the energy-damped physical image compact or quantitatively
  totally bounded; and
- they provide a natural norm and an exponentially controlled high-energy
  tail.

They do not prove that the admitted local observables separate the declared
target, that the schemes are jointly executable, or that complete record
formation occurs.

This is nevertheless the strongest continuum architecture DU has earned:

```text
law-selected approximation envelope
  -> target-relative finite mathematical packet
  -> locally realizable finite probe family
  -> formed certified record, only after explicit acquisition conditions
  -> target reconstruction to fixed nonzero resolution.
```

## 7. What is selected, what is supplied

| Layer | Status in this swing |
|---|---|
| QFT/net/representation | supplied |
| Hamiltonian \(H\) | supplied as part of the representation |
| low-energy family \(P_E\) | selected by \(H\) after \(E\) is supplied |
| energy-tail norm | selected by \(H,\beta,E\) |
| finite rank in noncompact QFT | generally absent |
| finite rank under compact resolvent | derived conditionally |
| compact/nuclear phase-space image | physical property of supplied packet |
| width profile | derived from image and norm |
| target-resolution dimension | derived after tolerance is supplied |
| approximating subspace | not generally selected |
| coordinate basis | not generally selected |
| local observables | supplied/admitted family |
| finite observable subset | target-relative existence, not canonical |
| probe measurement scheme | constructively realizable in scoped theory, still supplied |
| trial lineage and archive | unselected |
| observer access/action class | unselected |
| target reconstruction | conditional Grade 3 |

This table prevents two opposite mistakes:

1. calling every antecedent “merely epistemic” because the theorem does not
   derive it; and
2. calling every mathematically natural construction a physically formed
   record.

## 8. Absorber and novelty audit

### Primary absorbers

- Reeh--Schlieder cyclicity absorbs the density step.
- Haag--Swieca and Buchholz--Wichmann absorb the physical phase-space
  compactness/nuclearity program
  ([Buchholz--Wichmann](https://doi.org/10.1007/BF01454978)).
- Buchholz--Porrmann absorbs the explicit quantitative “how small is phase
  space?” question.
- spectral theory absorbs the compact-resolvent escape.
- Kolmogorov widths, approximation numbers, and compact-operator theory absorb
  basis-free approximation size.
- Fewster--Verch and Fewster--Jubb--Ruep absorb local QFT measurement
  realizability.
- `HC-DU-095` absorbs the compact finite-separator theorem.

### Dynamic Unity increment

No component theorem is claimed as new. The useful increment is the exact
typed synthesis:

\[
\begin{aligned}
&\text{Hamiltonian-selected tail envelope}\\
&+\text{generic noncompact infinite-rank obstruction}\\
&+\text{compact-resolvent exact escape}\\
&+\text{basis-free approximation dimension}\\
&+\text{conditional local-probe realization}\\
&+\text{selection/formation boundary}.
\end{aligned}
\tag{28}
\]

This prevents a future agent from:

- treating energy cutoff as automatically finite;
- treating nuclearity index as a coordinate list;
- treating a finite-dimensional approximant as a detector;
- treating measurability as physical selection;
- claiming a finite experiment without trial-lineage and bit typing; or
- discarding the continuum route merely because exact finite reconstruction
  fails.

## 9. Exact implications for the North Star

### What moved

Before `HC-DU-131--132`, the finite-continuum bridge was largely abstract.
Now a mature QFT route reaches several rungs:

```text
QFT dynamics and spectrum
  -> energy-damped local phase-space envelope
  -> finite approximation dimension at nonzero resolution
  -> finite target-separating local observable family
  -> local probe realizability in one serious QFT class.
```

That is knowledge progress. The continuum does not force every operational
record to be infinite.

### What remains

The missing rungs are now more specific:

1. a physically warranted QFT/state/region/target class;
2. quantitative width or approximation-number bounds in that class;
3. target separation by a fixed admitted local observable family;
4. a no-refit rule selecting the finite family before held-out evaluation;
5. compatible/repeatable probe realization with bounded resources;
6. blank-to-written formation with source provenance;
7. complete attempted-process acquisition and archive;
8. observer access and capability semantics; and
9. transfer to a held-out region, state, or target.

The bottleneck is no longer “can a continuum theory ever have a finite
operational packet?” It is:

> Which physical antecedents select and form one adequate packet, and does it
> transfer without being redesigned around the target?

### Why exact continuum truth is not required

The exact infinite-rank result remains true. It does not defeat the North
Star if all observer-accessible targets are uniformly stable under the
discarded tail and finite acquisition error.

That conditional must be tested, not assumed. In particular, discontinuous
phase labels, sharp sector membership, topological charges, threshold
capabilities, or adversarially fine interventions may fail Lipschitz
stability even when ordinary expectation values are stable.

The first-leak search should therefore range over the declared capability
class, not only smooth observables.

## 10. Grade and disposition

### Earned

Scoped Grade 4:

- the Hamiltonian spectral cutoff gives the exact energy-damped tail bound
  (4);
- if the local vector is cyclic and the low-energy spectral subspace is
  infinite-dimensional, the projected local map has infinite rank;
- a free massive field on noncompact space supplies an explicit continuous
  low-energy multiplicity witness;
- compact resolvent is an exact sufficient condition for finite-rank bounded
  energy projections;
- basis-free phase-space widths define minimal approximation dimension at
  nonzero tolerance; and
- equal nuclear norm does not determine the width profile or a coordinate
  system.

Conditional Grade 3:

- compact target separation reduces to finitely many local observables with a
  positive margin;
- scoped local QFT measurement theory supplies asymptotic probe schemes for
  those observables; and
- repeatability/joint compatibility plus complete sub-margin acquisition
  yields finite-resolution target certification.

### Not earned

- a theorem that every QFT satisfies nuclearity or Reeh--Schlieder in every
  relevant representation;
- a finite low-energy sector in generic noncompact QFT;
- a physically selected cutoff \(E\), tolerance, target, or state class;
- a canonical approximating subspace or basis;
- a QFT-selected probe theory, coupling, readout, archive, or observer;
- a jointly executable campaign or repeatable preparation;
- blank-to-written formation, provenance, complete acquisition, or access;
- no-refit held-out transfer;
- exact continuum reconstruction from finite data;
- empirical excess;
- a new AQFT theorem, law, physical theory, or prediction; or
- a ready scientific successor.

### Successor disposition

Dynamic Unity remains quiescent. This swing closes the obvious
Hamiltonian-cutoff selector candidate and banks the strongest conditional
finite-probe architecture. It does not select an executable scientific
successor.

### Exact reopener

Reopen this branch only with one frozen physical QFT arena that supplies,
before held-out evaluation:

1. a net, representation, state class, regions, Hamiltonian, and physical
   resolution contract;
2. a quantitative nuclearity, width, approximation-number, or compact-resolvent
   bound;
3. an independently admitted target and local observable family with a
   uniform separation theorem;
4. a finite observable/probe packet selected without inspecting the held-out
   completion or target values;
5. repeatable preparation or one compatible finite campaign;
6. complete trial lineage, calibration, digitization, archive, provenance,
   access, and composed error below the separation margin;
7. a bounded resource law; and
8. no-refit transfer to a held-out region, state, target, or capability.

An arbitrary finite box, numerical lattice, post-hoc basis, or detector
chosen to read the target does not satisfy this reopener.

## Resource disposition

The analytic spectral and compactness arguments decide the gate. The exact
43-check artifact only regresses:

- spectral-tail arithmetic;
- refinement-growing low-energy grid multiplicity;
- the compact-resolvent finite-rank control; and
- equal-nuclear-norm/different-width diagonal examples.

The grid is explicitly inadmissible as continuum evidence. It discovers no
new physics and justifies no field simulation. External hardware is
irrelevant until one finite probe packet passes the physical selection,
formation, acquisition, and transfer gates.
