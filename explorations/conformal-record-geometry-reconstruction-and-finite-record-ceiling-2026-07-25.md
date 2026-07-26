---
title: "Conformal record geometry: exact reconstruction and the finite-record ceiling"
status: completed_scoped_conditional_reconstruction_and_nonuniqueness
doc_type: exact_theorem_countermodel_and_program_boundary
created: 2026-07-25
run_id: RUN-20260725-222730-conformal-record-geometry-tournament
authority: "Joe direct chat: 'Another strong research swing'"
claim_grade: "EXACT CONDITIONAL TWO-MODE RECONSTRUCTION + SMOOTH COMPLETION NONUNIQUENESS / KNOWN INVERSE-METHOD TERRAIN / NO PHYSICAL SELECTION, NEW LAW, OR ONTOLOGY"
probe: "../tests/du_conformal_record_geometry_tournament_probe.py"
artifact: "../tests/artifacts/du_conformal_record_geometry_tournament_result.json"
---

# Conformal Record Geometry

## Result in plain English

This swing produces both a real reconstruction and the counterexample that
limits it.

Inside one predeclared two-parameter family of smooth curved spacetimes:

- causal order does not identify the geometry;
- total spacetime volume does not identify it;
- one observer's calibrated clock does not identify it;
- one radar return from that observer does not identify it;
- one calibrated regional volume still leaves a one-parameter family;
- two overlapping regional volumes identify both geometric parameters
  exactly; and
- those reconstructed parameters correctly predict a remote clock that was
  held out.

That is a genuine conditional reconstruction result.

But one additional smooth conformal mode can be chosen to preserve **every**
training record above while changing both the remote clock and scalar
curvature. The positive reconstruction therefore depends on the declared
two-mode completion class. It is not a universal result that finite records
determine a smooth spacetime.

The larger lesson is:

> “Order plus volume determines geometry” means causal structure plus a
> sufficiently complete local volume form under strong continuum conditions.
> It does not mean causal order plus one total volume, a finite event count,
> or a few selected regional measurements.

And the program-level correction is:

> Complete causal order plus a finite collection of the calibrated
> regional-volume and stationary-clock records used here can reconstruct an
> exact finite-dimensional geometry class or an operational quotient. It
> cannot identify an arbitrary smooth conformal factor unless independent
> dynamics, regularity, or a complete observation surface removes the hidden
> modes.

The exact probe passes `19/19`.

## Frozen comparison arena

The arena is supplied rather than derived:

\[
M=[0,1]_t\times[-1,1]_x
\]

with anchored left and right observer worldlines and metrics

\[
g_u=u(x)(-dt^2+dx^2),\qquad u(x)>0.
\]

This is a smooth static \(1+1\)-dimensional conformal family. Its volume form
is

\[
d\operatorname{vol}_{g_u}=u(x)\,dt\,dx.
\]

A stationary observer at position \(x_0\) accumulates proper time

\[
\tau_{x_0}=\sqrt{u(x_0)}
\]

over the unit coordinate interval.

Every positive \(u\) has the same null cones and causal order because
multiplying the metric by a positive scalar field does not change the sign of
\(g(v,v)\). The coordinate strip, its dimension, observer anchors, conformal
ansatz, and calibration are antecedents of this tournament. Nothing here
derives them from records.

## The declared two-mode family

Let

\[
\begin{aligned}
f_1(x)&=(x+1)(x-\tfrac13),\\
f_2(x)&=(x+1)(x^2-\tfrac13),\\
u_{a,b}(x)&=1+a f_1(x)+b f_2(x),
\end{aligned}
\]

with

\[
|a|+|b|\leq\tfrac12.
\]

On \([-1,1]\),

\[
|f_1|,|f_2|\leq\tfrac43,
\]

so

\[
u_{a,b}\geq1-\tfrac43(|a|+|b|)\geq\tfrac13.
\]

Every member is therefore a smooth Lorentzian metric.

Both modes obey

\[
\int_{-1}^{1}f_i(x)\,dx=0
\quad\text{and}\quad
f_i(-1)=0.
\]

Consequently every member has:

- the same causal order and null curves;
- total unit-window spacetime volume \(2\);
- left-observer proper time \(1\); and
- the same left-clock calibration of a fixed null radar return.

These records leave the full two-parameter family open.

## Theorem 1 — finite-family identification

Let a declared finite-dimensional conformal family be

\[
u_\theta=u_0+\sum_{k=1}^{n}\theta_k f_k,
\]

and let the training records be linear functionals \(L_j(u)\), such as
regional volumes or stationary-clock squared values. Define

\[
A_{jk}=L_j(f_k).
\]

Then:

1. \(\theta\) is uniquely identified by the training records exactly when
   \(A\) has full column rank.
2. A linear held-out observable \(H(u)\) is constant on every training fibre
   exactly when its mode row

   \[
   h_k=H(f_k)
   \]

   lies in the row space of \(A\).

### Proof

Two parameters \(\theta,\theta'\) produce the same training records exactly
when

\[
A(\theta-\theta')=0.
\]

Thus all training fibres are singletons exactly when
\(\ker A=\{0\}\), equivalently when \(A\) has full column rank.

The held-out difference is

\[
H(u_\theta)-H(u_{\theta'})
=h(\theta-\theta').
\]

It vanishes on every training fibre exactly when \(h\) annihilates
\(\ker A\). In finite-dimensional linear algebra,

\[
(\ker A)^\perp=\operatorname{row}(A),
\]

which proves the second statement.

This is ordinary finite inverse-problem linear algebra. Its role here is to
make the record/completion contract exact.

## Exact regional reconstruction

Use two overlapping calibrated regional volumes:

\[
\begin{aligned}
V_L&=\int_{-1}^{0}u_{a,b}(x)\,dx,\\
V_Q&=\int_{-1}^{1/2}u_{a,b}(x)\,dx.
\end{aligned}
\]

Exact integration gives

\[
\begin{aligned}
V_L&=1-\tfrac13a-\tfrac1{12}b,\\
V_Q&=\tfrac32-\tfrac38a-\tfrac{15}{64}b.
\end{aligned}
\]

The measurement matrix is

\[
A=
\begin{pmatrix}
-1/3 & -1/12\\
-3/8 & -15/64
\end{pmatrix},
\qquad
\det A=\tfrac3{64}\neq0.
\]

Let

\[
L=V_L-1,
\qquad
Q=V_Q-\tfrac32.
\]

Then

\[
\boxed{
a=\frac{16Q-45L}{9},
\qquad
b=\frac{72L-64Q}{9}
}.
\]

Inside this declared family, two overlapping volume records therefore
reconstruct the conformal factor exactly.

One volume is not enough. The explicit rival

\[
(a,b)=(\tfrac1{10},-\tfrac25)
\]

has the same \(V_L=1\) as flat space but

\[
V_Q=\tfrac{249}{160}
\quad\text{and}\quad
\tau_R^2=\tfrac35.
\]

The first regional record leaves a genuine one-dimensional fibre.

## Held-out remote-clock prediction

The right observer's proper time was not used in the reconstruction:

\[
\tau_R^2=u_{a,b}(1)=1+\tfrac43(a+b).
\]

Substitution of the reconstructed parameters yields

\[
\boxed{
\tau_R^2
=1+4L-\frac{64}{9}Q
}.
\]

For the nonflat fixture

\[
(a,b)=(\tfrac14,\tfrac14),
\]

the training records are

\[
V_L=\tfrac{43}{48},
\qquad
V_Q=\tfrac{345}{256}.
\]

They reconstruct \(a=b=1/4\) exactly and predict

\[
\tau_R^2=\tfrac53,
\qquad
\tau_R=\sqrt{\tfrac53}.
\]

The prediction is independently evaluated by the probe.

This fixture is not merely a differently labeled flat metric. For

\[
g=u(x)(-dt^2+dx^2),
\]

the scalar curvature is

\[
R=-\frac{u''}{u^2}+\frac{(u')^2}{u^3}.
\]

At the anchored center \(x=0\), the flat metric has \(R=0\), while the curved
fixture has

\[
R=-\frac{357}{250}.
\]

The two metrics are nonisometric.

## Theorem 2 — finite linear-record ceiling

Let \(X\) be a vector space of smooth conformal factors and let

\[
L_1,\ldots,L_m:X\rightarrow\mathbb R
\]

be finitely many linear training records. If a held-out linear functional
\(H\) is not in

\[
\operatorname{span}\{L_1,\ldots,L_m\},
\]

then there is a smooth perturbation \(f\) such that

\[
L_j(f)=0
\quad\text{for every }j,
\qquad
H(f)\neq0.
\]

For any strictly positive base factor \(u_0\), sufficiently small
\(\epsilon\) makes

\[
u_\epsilon=u_0+\epsilon f>0.
\]

The metrics \(g_{u_0}\) and \(g_{u_\epsilon}\) then share causal structure and
all finite training records but differ on the held-out observable.

### Proof

Let

\[
L:X\rightarrow\mathbb R^m,
\qquad
L(f)=(L_1(f),\ldots,L_m(f)).
\]

If \(H\) vanished on \(\ker L\), it would factor through the finite-dimensional
quotient \(X/\ker L\), hence through \(\operatorname{im}L\), making it a linear
combination of the \(L_j\). The contrapositive supplies
\(f\in\ker L\) with \(H(f)\neq0\). Compactness of the strip and strict
positivity of \(u_0\) allow a sufficiently small coefficient to preserve
positivity.

This theorem applies directly to regional volumes and stationary-clock
squared values in this \(1+1\) static conformal arena. It is not claimed for
arbitrary nonlinear, complete, or infinite observation surfaces.

## Explicit hostile smooth completion

The tournament does not leave Theorem 2 abstract. Define

\[
h(x)=(x+1)(1-3x-6x^2+10x^3).
\]

It obeys

\[
\begin{aligned}
h(-1)&=0,\\
\int_{-1}^{1}h\,dx&=0,\\
\int_{-1}^{0}h\,dx&=0,\\
\int_{-1}^{1/2}h\,dx&=0,
\end{aligned}
\]

but

\[
h(1)=4.
\]

The metric

\[
g_h=(1+\tfrac1{100}h(x))(-dt^2+dx^2)
\]

is positive because the conservative bound \(|h|\leq40\) gives
\(1+h/100\geq3/5\).

It matches flat space on:

- causal order and null reachability;
- total volume;
- the left clock and fixed left radar return;
- \(V_L\); and
- \(V_Q\).

Yet it predicts

\[
\tau_R^2=\tfrac{26}{25}
\]

instead of \(1\), and its exact center curvature is

\[
R=\frac{182200}{1030301}\neq0.
\]

Thus the same finite training record supports two nonisometric smooth
geometries with a finite remote-clock discriminator.

This is a completion-class countermodel, not an irreducible physical
remainder. The hidden mode has not been shown to satisfy an Einstein equation,
energy condition, physical source law, or independently formed record
instrument.

## Regional refinement versus new access

Split the left measured region at \(x=-1/2\).

If the two child volumes are only reaggregated, their measurement rows add
exactly to the original \(V_L\) row. The subdivision is benign bookkeeping.

If both child volumes remain independently accessible, their two mode rows
have determinant

\[
\frac1{64}\neq0.
\]

They identify both parameters even without the overlapping \(V_Q\) record.

Therefore:

> Region subdivision is gauge only when the additional subregion evidence is
> not independently retained. Separate certified access can increase
> reconstruction rank and capability.

This supplies a precise bridge between Lane 5 regional finality and Lane 6
geometry. The topology did not create geometry; the additional accessible
measurement did work.

## Collision with established results

There is no conflict with continuum causal reconstruction.

- Hawking--King--McCarthy and Malament establish recovery of conformal
  structure from sufficiently complete causal structure under their
  hypotheses
  ([HKM](https://doi.org/10.1063/1.522874);
  [Malament](https://doi.org/10.1063/1.523436)).
- The causal-set program combines order with local finiteness/number and a
  continuum approximation contract, rather than one global volume scalar
  ([Bombelli et al.](https://doi.org/10.1103/PhysRevLett.59.521)).
- Lorentzian inverse-problem work reconstructs conformal structure from rich
  families of light observation sets or active source-to-solution data, not
  one radar return
  ([Kurylev--Lassas--Uhlmann](https://arxiv.org/abs/1405.3386);
  [Hintz--Uhlmann](https://arxiv.org/abs/1705.01215)).

The rank theorem, row-span prediction criterion, and finite-functional
nullspace are known inverse-method mathematics. The candidate Dynamic Unity
contribution is not a new theorem of Lorentzian geometry. It is the typed
reconstruction contract:

```text
causal order
    != total volume
    != local volume form
    != one observer's clock/radar record
    != multiple independently accessible regional records
    != exact geometry inside a declared completion class
    != universal smooth geometry
    != physically selected spacetime.
```

## What changes in the research program

`H-CCR-08` should no longer ask whether a finite meta-record simply
“reconstructs geometry.” It must specify:

1. the target resolution or finite model class;
2. the causal and coordinate scaffolding supplied;
3. which local volume and clock functionals are formed and accessible;
4. the training measurement operator and its nullspace;
5. the held-out observable;
6. the physical law or regularizer restricting completion modes; and
7. the gauge and benign-refinement class.

The North Star remains viable, but its exact-continuum reading changes:

> Finite, physically regular certified measurements can reconstruct the
> complete observer-accessible quotient at a declared resolution. Exact
> continuum geometry additionally requires a complete limiting record surface
> or independent dynamics that selects the admissible completion class.

## Next physical reopener

Do not add more arbitrary conformal modes or regional volumes. The next
high-value question is what **physical structure** removes them.

The next specimen should add one independently justified restriction:

- a nontrivial field equation and sourced stress-energy class, in a model
  where the dynamics genuinely constrains the metric rather than vacuum
  \(1+1\) Einstein gravity;
- an energy/regularity/locality condition;
- a complete active source-to-solution or calibrated clock-and-light
  observation instrument;
- a finite task-resolution quotient; or
- a dynamics selecting a low-dimensional geometric mode family.

Freeze that restriction before revealing the remote clock. Then ask whether:

1. the hidden mode becomes physically inadmissible;
2. the held-out clock is forced with calibrated uncertainty;
3. another admissible mode survives; or
4. the physical contract remains incomplete.

The reusable mathematical object is a **record nullspace**:

\[
\mathcal N_R=\{f:L_j(f)=0\ \forall j\}.
\]

Physical reconstruction succeeds only when the admissible physical tangent
space intersects \(\mathcal N_R\) entirely inside declared gauge, or when
every surviving direction is irrelevant to the observer's target
capabilities.

## Reproducibility and limits

Run:

```bash
python3 tests/du_conformal_record_geometry_tournament_probe.py
```

The exact-rational probe checks all integrals, ranks, inversions, positivity
bounds, causal-cone controls, regional refinement, held-out predictions, and
curvature values. It writes
`tests/artifacts/du_conformal_record_geometry_tournament_result.json`.

Passing establishes:

- exact conditional reconstruction in the declared two-mode family;
- exact held-out prediction in that family;
- one explicit smooth completion countermodel; and
- the finite-record nullspace boundary.

It does not establish a physical geometry, selected conformal family,
Einstein solution, quantum-gravity result, new law, ontology, experiment, or
paper verdict.
