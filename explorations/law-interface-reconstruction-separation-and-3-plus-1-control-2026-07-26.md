---
title: "Law–interface–reconstruction separation and a 3+1 conformal control"
status: completed_scoped_result
doc_type: theorem_and_hostile_control
created: 2026-07-26
authority: "Joe direct chat: run the more impactful integrated swing joining physical interface selection to lawful geometry reconstruction"
claim_grade: "EXACT STABILIZER OBSTRUCTION + EXACT LAW/RECORD ATTRIBUTION TRICHOTOMY + EXACT 3+1 LINEARIZED CONFORMAL CONTROL / COMPONENT MATHEMATICS KNOWN / NEW DU DEPENDENCY RESULT / NO NOVEL-PHYSICS OR PAPER PROMOTION"
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260726-122948-law-interface-reconstruction-separation/run-plan.md"
program_ids:
  - HC-DU-033C
  - HC-DU-038D
---

# Law–interface–reconstruction separation

## Result in plain English

The integrated swing did not find one mechanism that simultaneously selects
an observer's record interface and reconstructs geometry. It found a sharper
separation theorem.

A physical law can remove every admissible geometric alternative while still
failing to select any observer, clock direction, pointer, archive, or access
boundary. In that case a held-out geometric quantity is indeed fixed, but the
law fixed it. The records did not do the reconstructive work.

Conversely, adding a physically real timelike current can select a local time
direction, but that alone does not select a record algebra, archive, decoder,
or geometry. Interface selection and target reconstruction are independent
obligations.

The exact \(3+1\)-dimensional control makes the distinction concrete:

1. in the compactly supported conformal tangent sector around Minkowski
   spacetime, the trace-free linearized vacuum equation forces the conformal
   perturbation to vanish;
2. therefore every frozen held-out clock functional is already constant on
   the lawful class, before any record is conditioned on; but
3. Lorentz symmetry has no invariant future-unit timelike vector, so the same
   metric and law cannot naturally select one observer time direction.

This supplies a reusable North-Star audit:

> First ask what the law fixes without the record. Then ask whether the law
> or realized physical state selects the record interface. Only then may the
> further reduction of target uncertainty be credited to records.

The result advances `HC-DU-033` and `HC-DU-038` together. It is an exact
Dynamic Unity dependency result built from standard equivariance,
linearized-gravity, and inverse-problem mathematics. It is not a new law of
physics or a standalone publication claim.

## Frozen typed contract

Let:

- \(M\) be a completion class;
- \(G\) act on \(M\) as the declared physical symmetry or gauge group;
- \(E:M\to Z\) be a \(G\)-equivariant physical equation;
- \(M_E=E^{-1}(0)\) be the lawful completion class;
- \(\mathcal I\) be a space of candidate observer/record interfaces with a
  \(G\)-action;
- \(r_i:M_E\to Q_i\) be the record map associated with interface
  \(i\in\mathcal I\);
- \(t:M_E\to Y\) be a held-out observer-accessible target; and
- \(d_Y\) be the declared target metric.

There are three different maps in this contract:

\[
\text{physical law }E,
\qquad
\text{interface selector }s,
\qquad
\text{record-to-target factorization}.
\]

They must not be collapsed into one another.

An interface claimed to come from the physical law must be natural under the
declared symmetry. At minimum its selector must obey

\[
s(gm)=g\,s(m).
\]

A coordinate-dependent rule that fails this equation has inserted a
reference frame rather than derived one.

## Theorem 1 — stabilizer obstruction to interface selection

For \(m\in M_E\), let

\[
G_m=\{g\in G:gm=m\}
\]

be its stabilizer. If \(s:M_E\to\mathcal I\) is \(G\)-equivariant, then

\[
s(m)\in \mathcal I^{G_m}
=
\{i\in\mathcal I:hi=i\text{ for every }h\in G_m\}.
\]

Therefore:

1. if \(\mathcal I^{G_m}=\varnothing\), no equivariant point selector exists
   at \(m\);
2. if the only fixed interfaces are trivial, no nontrivial interface is
   selected there; and
3. if a complete interface space
   \(\mathcal I_{\mathrm{full}}\) has an equivariant projection to a
   necessary sub-interface \(\mathcal I_0\), and
   \(\mathcal I_0^{G_m}=\varnothing\), then no complete equivariant selector
   exists either.

### Proof

For any \(h\in G_m\),

\[
s(m)=s(hm)=h\,s(m)
\]

by equivariance. Thus \(s(m)\) is fixed by every element of \(G_m\). The first
two claims follow immediately. For the third, composing a hypothetical
complete selector with the equivariant projection would produce the forbidden
selector into \(\mathcal I_0\). \(\square\)

### What the theorem does and does not say

The theorem does not say that physical interfaces cannot form. It says that
they cannot be uniquely and naturally selected at a solution whose surviving
symmetry has no fixed candidate interface.

There are three honest exits:

1. the realized physical state contains symmetry-breaking structure;
2. boundary or initial conditions select a branch from a symmetry-related
   orbit; or
3. the law selects the entire orbit or covariant family, while a separate
   physical event selects one member.

The third outcome is common but weaker than point selection. A law may
canonically supply a net \(U\mapsto\mathcal A(U)\) of local algebras without
choosing the observer region \(U\), just as it may supply every allowed frame
without choosing one frame.

## Theorem 2 — law/record attribution trichotomy

Assume \(M_E\neq\varnothing\). Define the law-only target diameter

\[
\Delta_E
=
\sup_{m,n\in M_E}d_Y(t(m),t(n)).
\]

For a supplied interface \(i\), record value \(q\), and nonempty lawful
record fibre

\[
F^{E,i}_q
=
\{m\in M_E:r_i(m)=q\},
\]

define

\[
\Delta_{E,i}(q)
=
\sup_{m,n\in F^{E,i}_q}d_Y(t(m),t(n)).
\]

Then

\[
\Delta_{E,i}(q)\leq\Delta_E.
\]

Relative to target tolerance \(\tau\), exactly one of the following applies
after nonemptiness has been established:

1. **law-only closure**
   \[
   \Delta_E\leq\tau;
   \]
2. **record-assisted reconstruction**
   \[
   \Delta_E>\tau
   \quad\text{and}\quad
   \Delta_{E,i}(q)\leq\tau;
   \]
3. **lawful record underdetermination**
   \[
   \Delta_{E,i}(q)>\tau.
   \]

If the fibre is empty, the return is instead
`UNREALIZABLE_LAWFUL_RECORD`; target constancy is not evaluated.

### Proof

The fibre \(F^{E,i}_q\) is a subset of \(M_E\), so its target diameter cannot
exceed the diameter of \(M_E\). If the fibre is nonempty, either
\(\Delta_E\leq\tau\) or \(\Delta_E>\tau\). In the second branch, either
\(\Delta_{E,i}(q)\leq\tau\) or it is greater than \(\tau\). These alternatives
are mutually exclusive and exhaustive. \(\square\)

### Robust successor

For noisy records, first calculate the distance

\[
\eta_E(q)
=
\inf_{m\in M_E}d_Q(r_i(m),q)
\]

and use the certified tolerance fibre. The order is:

```text
lawful record realizability
    -> law-only target diameter
    -> record-conditioned target diameter
    -> interface-selection status
```

The first three quantities are properties of a frozen supplied interface.
The last asks whether that interface was physically selected. Passing the
first three does not answer the fourth.

## Exact \(3+1\) hostile control

### Arena

Freeze:

- Minkowski spacetime \((\mathbb R^{1,3},\eta)\) with signature
  \((-+++)\);
- conformal tangent perturbations
  \[
  h_{\mu\nu}=2\phi\,\eta_{\mu\nu},
  \qquad
  \phi\in C_c^3(\mathbb R^{1,3});
  \]
- the trace-free linearized vacuum equation
  \[
  E_{\mu\nu}(\phi)=\delta R_{\mu\nu}^{\mathrm{TF}}=0;
  \]
- any finite target-independent linear record map \(R\phi\); and
- a held-out first-order clock target along a frozen timelike curve
  \(\gamma\),
  \[
  T_\gamma(\phi)=\int_\gamma\phi\,d\tau_\eta.
  \]

The curve is explicitly supplied for the target assay. The next theorem will
show that the vacuum law did not select it.

The linearized trace-free Ricci tensor in this sector is

\[
E_{\mu\nu}(\phi)
=
-2\partial_\mu\partial_\nu\phi
+\frac12\eta_{\mu\nu}\Box\phi.
\]

This is the first dimension in which the trace-free condition is
nonvacuous. In \(1+1\), it vanishes identically and cannot run this test.

### Lemma 3 — compact conformal vacuum closure

If \(\phi\in C_c^3(\mathbb R^{1,3})\) and
\(E_{\mu\nu}(\phi)=0\), then \(\phi=0\).

### Proof

Taking the divergence gives

\[
\partial^\mu E_{\mu\nu}
=
-\frac32\partial_\nu\Box\phi
=0.
\]

Hence \(\Box\phi=C\) is constant. Outside the compact support of \(\phi\), all
derivatives vanish, so \(C=0\). The field equation then gives

\[
\partial_\mu\partial_\nu\phi=0.
\]

Thus \(\phi\) is affine. A compactly supported affine function is zero.
\(\square\)

Without the compact-support or corresponding boundary condition, the
trace-free equation permits the finite family

\[
\phi(x)
=
\frac{C}{8}\eta_{\mu\nu}x^\mu x^\nu
+a_\mu x^\mu+b.
\]

The boundary/source contract is therefore load-bearing and must not be hidden
inside the word “vacuum.”

### Attribution verdict

For the matched lawful record \(q=R(0)\),

\[
M_E=\{0\},
\qquad
F_q^{E,R}=\{0\},
\qquad
\Delta_E=0,
\qquad
\Delta_{E,R}(q)=0.
\]

Every held-out clock target is reconstructed in this supplied tangent class,
but the result is **law-only closure**. Deleting the entire record map leaves
the target fixed.

For \(q\neq R(0)\), the lawful fibre is empty. Such a record cannot be called
a successful reconstruction merely because every pair of completions in the
empty set agrees.

This validates physical completion narrowing in \(3+1\), but it does not
show that records create or reconstruct geometry. Ordinary linearized
Einstein dynamics already absorbs the vacuum conformal closure; no
causal-fermion-system-specific residue is earned.

## Exact Minkowski interface obstruction

Let the necessary local frame component of an observer interface be the
future-unit hyperboloid

\[
\mathcal I_0
=
H^3
=
\{u\in\mathbb R^{1,3}:
\eta(u,u)=-1,\ u^0>0\}.
\]

The proper orthochronous Lorentz group acts transitively on \(H^3\).
Minkowski spacetime is fixed by the full Lorentz group, but \(H^3\) has no
Lorentz-fixed point:

- spatial rotations force the spatial part of a fixed vector to vanish; and
- a boost then moves every vector of the form \((u^0,0,0,0)\).

By Theorem 1, the Minkowski metric or any Lorentz-natural vacuum action at
that solution cannot select a unique observer time direction. Any complete
record interface with an equivariant projection to its observer direction is
therefore also unselected.

The conclusion is stronger than “coordinates are arbitrary” and weaker than
“observers are impossible”:

> the symmetric law may supply the full covariant family of possible
> observer interfaces, but it does not choose one member.

## Symmetry-breaking positive control

Enrich the realized completion with a nonzero future-timelike physical
current \(J^\mu\). Then

\[
u^\mu(J)
=
\frac{J^\mu}{\sqrt{-\eta_{\alpha\beta}J^\alpha J^\beta}}
\]

is a Lorentz-equivariant selector of a local time direction.

This positive control proves that the obstruction is not rigged against
selection. It identifies the minimum repair for this one interface
component: a target-independent physical timelike direction, whether supplied
by matter, a clock field, an apparatus worldtube, or boundary/initial data.

It also exposes two remaining distinctions:

1. if an action selects only a degenerate Lorentz orbit of currents, a
   realized branch or boundary condition is still needed to select one
   orientation; and
2. a selected time direction does not by itself select a pointer algebra,
   record-writing coupling, archive, decoder, access boundary, or cadence.

The full physical interface remains a structured object, not one vector.

## Combined theorem — selection and reconstruction are independent

The \(3+1\) control realizes:

```text
lawful geometric target closure: yes
record contribution to that closure: no
observer-direction selection by the symmetric law: no
observer-direction selection after adding a timelike current: yes, conditionally
complete record-interface selection: still open
```

Therefore configuration selection, interface selection, record formation,
and target reconstruction are logically independent receipts.

A variational or field law can be powerful enough to determine the target
while remaining silent about the observer interface. An interface can also
be selected by extra physical structure while leaving a nontrivial lawful
target fibre. Neither result implies the other.

This is the smallest counterexample to the hoped-for automatic unification:

> “the dynamics selects the physical configuration” does not entail “the
> dynamics selects the records,” and “the lawful record fibre has zero target
> diameter” does not entail “the records supplied the identifying
> information.”

## North-Star attribution receipt

Future claims that certified records reconstruct observer-accessible physics
must report four receipts:

1. **lawful realizability** — the observed record has a nonempty tolerance
   fibre in the frozen physical/source/boundary class;
2. **law-only baseline** — the held-out target diameter before conditioning
   on records;
3. **record increment** — the target diameter after conditioning, with credit
   to records only when this crosses the declared reconstruction threshold;
4. **interface provenance** — whether the observer, instrument, record
   algebra, archive, decoder, and access boundary are selected, selected only
   up to an orbit, supplied, or fitted.

This does not make record-assisted reconstruction harder by definition. It
prevents a sufficiently restrictive physical law from being mistakenly
reported as evidence for record fundamentality.

## Counterfactual kill tests

The result yields three cheap tests for future swings.

### Ablate the record

If the held-out target remains fixed on \(M_E\) after deleting \(r\), return
`LAW_ONLY_CLOSURE`. Do not credit the record.

### Apply the stabilizer

At every candidate lawful solution \(m\), calculate \(G_m\). If the candidate
interface has no \(G_m\)-fixed point, return
`INTERFACE_ORBIT_ONLY` or `INTERFACE_UNSELECTED`.

### Charge the symmetry breaker

If matter, a reference, an environment, an apparatus, a boundary, or an
initial condition selects the interface, retain it as an explicit physical
premise and ask which interface components it actually selects. Do not let a
timelike vector stand in for a pointer/archive/decoder theorem.

## Consequences for the conditional \(4+6+4\) work surface

The exterior-graded \(4+6+4\) candidate should receive this result as an
acceptance gate, not drive the next swing.

Its components must do more than parameterize a covariant field family:

1. identify a target-independent symmetry breaker or equivariant interface
   orbit;
2. state which observer/interface component is selected;
3. leave a nontrivial lawful target diameter before records; and
4. show that the proposed graded record actually shrinks that diameter on a
   nonempty fibre.

If the law already fixes the target, or if an exterior component merely names
an observer frame inserted by hand, the candidate remains a representation.

## Collision and grade

The component mathematics is strongly occupied:

- the stabilizer lemma is standard equivariant reasoning;
- the conformal linearization is standard linearized gravity;
- the target-diameter comparison is standard constrained inverse-problem
  logic; and
- symmetry breaking, reference frames, matter clocks, and observer fields are
  established physical tools.

The defensible Dynamic Unity contribution is the typed conjunction and
attribution rule. It prevents three common category errors in one test:

1. configuration selection being called interface selection;
2. law-only target closure being called record reconstruction; and
3. selection of a frame component being called selection of a complete
   record interface.

No claim is made that this conjunction is a novel mathematical theorem,
measurable deviation, ontology, or paper.

## Highest-information successor

Do not run another vacuum conformal model. The next useful arena must satisfy
all of the following before calculation:

1. a frozen \(3+1\) physical law and source/boundary class with
   \(\Delta_E>0\) for a held-out observer-accessible target;
2. an independently motivated realized symmetry breaker, such as a timelike
   matter current or clock field;
3. a formed record coupling and access boundary derived from or calibrated
   against that physical structure; and
4. a record-conditioned fibre that may reduce the target diameter without
   refitting the law, source, interface, or target.

The most economical candidate is a linearized Einstein--matter inverse
problem with a timelike matter current and one frozen local clock/record
instrument. Its first task is not simulation. It is an exact kernel and
stabilizer calculation:

\[
\Delta_E>\tau
\quad\text{and}\quad
\ker DE\cap\ker Dr\subseteq\ker Dt
\quad ?
\]

A surviving lawful record-null target mode kills reconstruction. A closed
target fibre with a physically selected interface earns genuine
record-assisted reconstruction in the supplied class. Either result teaches
more than extending the already closed vacuum control.

## Disposition

```text
HC-DU-033C STABILIZER INTERFACE-SELECTION OBSTRUCTION EXACT
HC-DU-038D LAW/RECORD ATTRIBUTION TRICHOTOMY EXACT
3+1 COMPACT CONFORMAL TRACE-FREE VACUUM CLASS CLOSES
VACUUM CLOSURE IS LAW-ONLY, NOT RECORD-ASSISTED
MINKOWSKI LAW DOES NOT SELECT AN OBSERVER TIME DIRECTION
TIMELIKE PHYSICAL CURRENT SELECTS THAT COMPONENT CONDITIONALLY
COMPLETE RECORD INTERFACE REMAINS OPEN
COMPONENT MATHEMATICS KNOWN
NO NEW PHYSICS, ONTOLOGY, PAPER, HARDWARE, OR EXTERNAL ACTION
```

No executable model was built. Direct proof supplied the decision-changing
result at a higher grade than a local simulation could have earned.
