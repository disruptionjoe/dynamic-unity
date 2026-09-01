---
title: "Action-selected holonomy, common-view stabilizer obstruction, and regional no-section"
status: banked_scoped_action_selection_and_nonselection_result
doc_type: theorem_obstruction_and_exact_quantum_transfer_control
created: 2026-08-31
claim_id: HC-DU-207
run_id: RUN-20260831-action-selected-common-view-obstruction
program_id: DU-COMPUTATION-FIRST-CLOSED-TRANSITION-SUBSTRATE
action_id: CTS-A2-COMMON-VIEW-CLOSURE-SELECTOR-OR-OBSTRUCTION
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
portfolio_return: COMMON_VIEW_NO_SECTION_OR_AMBIGUITY_OBSTRUCTION
observer_index_return: OBSERVER_INDEX_REMAINS_SUPPLIED
---

# Executive result

The `P35 -> P30 -> P33` positive chain does not close on the smallest frozen
source action.  Something more informative happens instead:

> A physical action can select a relational transport class and its
> gauge-invariant loop holonomy without selecting an observer, material
> record, admitted action bandwidth, consumer, or absolute ruler.

On a four-site signed cycle, freeze

\[
S_\sigma(x)
=
\frac12\sum_{(u,v)}(x_u-\sigma_{uv}x_v)^2,
\qquad \sigma_{uv}\in\{+1,-1\}.
\]

The stationary solution, Hessian, constraints, coupling signs, and gauge rule
are all fixed before any view is named.  The action selects the loop invariant

\[
h=\prod_{e\in C_4}\sigma_e\in\{+1,-1\}
\]

and its response spectrum up to vertex-sign gauge.  For `h=-1`, every
edge-deleted tree region has a one-dimensional nonzero parallel-section
space, but the complete cycle has none.  The obstruction is finite and
response-visible:

\[
\operatorname{spec}L_{-}
=
\{2-\sqrt2,2-\sqrt2,2+\sqrt2,2+\sqrt2\},
\qquad
\det L_-=4.
\]

The same result survives standard quantization.  Four coupled harmonic modes
with

\[
H=\frac12p^Tp+\frac12q^T(I+L_\sigma)q
\]

have different ordinary normal-mode frequencies for `h=+1` and `h=-1`.
This is known quadratic quantum physics, not a new prediction.

The decisive boundary is:

```text
action selects transport orbit and holonomy
  != action selects observer or record interface
  != action selects intervention bandwidth
  != action selects material writer-consumer handoff
  != action selects absolute ruler.
```

`CTS-A2` therefore returns its preregistered negative class:

```text
COMMON_VIEW_NO_SECTION_OR_AMBIGUITY_OBSTRUCTION
+ ACTION_SELECTED_REGIONAL_NO_SECTION
+ OBSERVER_INDEX_REMAINS_SUPPLIED
```

This is scoped Grade 4 because the selection and nonselection statements are
exact in the frozen physical model.  The component mathematics is standard;
no universal no-go, new physical law, empirical excess, ontology, or paper is
claimed.

# 1. Frozen antecedent

Use the cycle

\[
0-1-2-3-0
\]

with one real amplitude per site and one signed coupling per edge.  Write the
signed incidence matrix as `D_sigma`; then

\[
S_\sigma(x)=\frac12\|D_\sigma x\|^2,
\qquad
L_\sigma=D_\sigma^TD_\sigma.
\]

The antecedent contains:

- the four-site cycle;
- the four signed couplings;
- the quadratic action and stationary point;
- the Hessian `L_sigma`;
- vertex-sign gauge transformations; and
- no predeclared observer, instrument, archive, consumer, action cutoff,
  embedding, metric, or ruler.

The local gauge transformation is

\[
x_v\mapsto\eta_vx_v,
\qquad
\sigma_{uv}\mapsto\eta_u\sigma_{uv}\eta_v,
\qquad
\eta_v\in\{+1,-1\}.
\]

It leaves the action invariant and preserves `h`.  All sixteen sign
assignments split into exactly two gauge orbits of eight, indexed by `h`.

“Action-selected” is conditional in the same sense as `P35`: once the complete
action and boundary data are frozen, the holonomy is constant on their
physical representation orbit and needs no view or target fit. The result does
not derive why nature chose this action or why its coupling signs have the
frustrated value. A meta-dynamics selecting those inputs remains outside the
claim.

This is a finite signed-oscillator or real rank-one connection model.  It is
not proposed as a substrate of nature.

# 2. General stabilizer criterion for a covariant selector

Let a group `G` act on antecedents `A` and candidate view families `V`.  A
covariant selector is a map

\[
s:A\to V,
\qquad
s(ga)=g\,s(a).
\]

For one antecedent `a`, let

\[
G_a=\{g\in G:ga=a\}
\]

be its stabilizer.

## Theorem 1 — stabilizer fixed-point necessity

Every covariantly selected value at `a` lies in the stabilizer fixed-point
set:

\[
s(a)\in V^{G_a}.
\]

### Proof

For every `g` in `G_a`,

\[
s(a)=s(ga)=g\,s(a).
\]

Therefore `s(a)` is fixed by every element of the stabilizer. `square`

Two exact consequences follow:

1. if `V^{G_a}` is empty, no covariant selector of that type exists at `a`;
2. if `V^{G_a}` contains several candidates, covariance alone does not select
   one uniquely.

This is elementary equivariant mathematics.  Its role here is to turn
“compute every residual automorphism” in `P35` into a fail-closed test.

# 3. What P35 actually selects

For the frustrated assignment

\[
\sigma=(+1,+1,+1,-1),
\]

the Hessian is

\[
L_-=
\begin{pmatrix}
2&-1&0&1\\
-1&2&-1&0\\
0&-1&2&-1\\
1&0&-1&2
\end{pmatrix}.
\]

Its signed locality-preserving residual symmetry contains sixteen signed
permutation operators and is vertex-transitive.  No vertex is fixed by the
whole stabilizer.  Therefore the action does not select one site as an
observer, archive, or privileged perspective.

The action does select:

- the gauge orbit of the signed couplings;
- the nontrivial holonomy `h=-1`;
- the Hessian response spectrum;
- a two-dimensional low spectral band; and
- a two-dimensional high spectral band.

It does not select an axis inside either doubly degenerate band.  The maximal
positive result is thus a coarse relational response decomposition, not a
complete matched common-view family.

## P35 disposition

```text
PARTIAL_ACTION_SELECTED_TRANSPORT_ORBIT
+ GLOBAL_COMMON_VIEW_SELECTOR_OBSTRUCTION
```

The important correction is positive as well as negative: action selection
need not first select an object or observer.  It may select a relation class,
connection, or obstruction.

# 4. P30 is exact only after an action family is chosen

The same Hessian canonically defines at least three covariant probe
subspaces:

\[
\mathcal A_{\mathrm{low}}=\operatorname{im}P_{\mathrm{low}},
\qquad
\mathcal A_{\mathrm{high}}=\operatorname{im}P_{\mathrm{high}},
\qquad
\mathcal A_{\mathrm{all}}=\mathbb R^4.
\]

The two band projectors are polynomials in `L_-`; all three families therefore
commute with every residual symmetry.  Their ranks are `2`, `2`, and `4`.

For linear response queries, the coarsest sufficient quotient relative to
each family is exact.  But the kernel dimension is `2` for either band and
`0` for the full response family.  The frozen antecedent does not say whether
an agent may excite/read only one spectral band or every mode.

Therefore:

> The interventional causal-state quotient is canonical relative to a frozen
> action family, but the physical action does not automatically select that
> family or its resource cutoff.

## P30 disposition

```text
CAUSAL_STATE_UNIQUE_ONLY_RELATIVE_TO_AN_UNSELECTED_ACTION_FAMILY
```

Choosing maximal access by convention would supply a capability assumption.
Choosing a low-energy band would supply a cutoff.  Neither becomes selected
merely because both are covariant functions of the Hessian.

# 5. P33 selects propagation structure but not a ruler

The signed Hessian supplies:

- adjacency;
- signed parallel transport;
- spectral propagation modes;
- the holonomy class; and
- dimensionless response ratios.

It does not supply an embedding length.  Embed the same cycle as a square of
side `1` or side `3`.  The unweighted signed action and every response above
remain identical, while the perimeter changes from `4` to `12`.

This is the finite version of `HC-DU-112`:

> A propagation or causal structure may select conformal, combinatorial, or
> dimensionless geometry while an absolute ruler remains supplied until a
> dimensionful physical relation breaks the scale freedom.

## P33 disposition

```text
PROPAGATION_AND_HOLONOMY_SELECTED
+ ABSOLUTE_RULER_UNSELECTED
```

No spacetime interpretation is attached to the four sites.

# 6. The P40/P31 branch returns an exact regional obstruction

A parallel section satisfies

\[
x_u=\sigma_{uv}x_v
\]

on every retained edge.

Delete any one cycle edge.  The remaining graph is a tree, the relations can
be propagated from one freely chosen nonzero root value, and the section
space has dimension one.

On the full cycle, transport around the loop gives

\[
x_0=hx_0.
\]

For `h=-1`, this requires `x_0=0`, and then every site value is zero.  Thus:

```text
every proper tree region has a nonzero local section
the full frustrated cycle has no nonzero global section
the obstruction is the action-selected Z2 holonomy.
```

This is not failed numerical reconstruction.  It is the exact regional
no-section outcome named by `P40/P31`.

The holonomy is also response-visible: the balanced cycle has one zero mode
and spectrum `{0,2,2,4}`; the frustrated cycle has no zero mode and the
gapped spectrum stated above.  The action therefore selects a finite
structural remainder before any record instrument is supplied.

What is **not** yet earned is equally important.  A latent response invariant
is not a formed record, public fact, or observer-accessible certificate.

# 7. Standard quantum transfer

Add the same positive mass to both holonomy classes and quantize the four
coupled modes:

\[
H_\sigma
=
\frac12p^Tp
+
\frac12q^T(I+L_\sigma)q.
\]

The normal-mode frequencies are:

\[
\omega_+=\{1,\sqrt3,\sqrt3,\sqrt5\},
\]

for trivial holonomy, and

\[
\omega_-=\{
\sqrt{3-\sqrt2},
\sqrt{3-\sqrt2},
\sqrt{3+\sqrt2},
\sqrt{3+\sqrt2}
\},
\]

for negative holonomy.

This establishes that the finite invariant is not an artifact of treating the
network classically.  It is an ordinary quantum spectral distinction.  It
does not select how the frequencies are measured, recorded, accessed, or
used.

# 8. Relation to HC-DU-123

`HC-DU-123` begins with a formed complete cycle record `Q_T(y)` and proves:

\[
\ker Q_T=\operatorname{im}d,
\]

with exact open-path remainders and min-cut distances in a matter-completed
finite-Abelian arena.

The present result begins one layer earlier:

```text
HC-DU-207:
  source action -> signed transport orbit -> holonomy/no-section

HC-DU-123:
  supplied formed cycle record -> exact record fibre -> capability remainder
```

They are complementary, not duplicates.  The missing bridge is now exact:

```text
action-selected holonomy
  ?-> physically selected sampler and material cycle record
  ?-> provenance, archive and access
  ?-> selected continuation/action family
  -> only then HC-DU-123 reconstruction and remainder machinery.
```

# 9. Absorber and novelty audit

The components are mature:

- signed graph Laplacians and structural balance already classify balanced
  and frustrated signed networks; see Kunegis's signed-network treatment
  ([primary preprint](https://arxiv.org/abs/1402.6865));
- cellular sheaf Laplacians relate kernels, global sections, and cohomology;
  see Hansen and Ghrist
  ([primary preprint](https://arxiv.org/abs/1808.01513));
- gauge holonomy and magnetic/connection Laplacians already make loop
  transport spectrally visible;
- sufficient statistics and observability already make the quotient depend
  on the admitted query family; and
- the stabilizer criterion is elementary equivariant reasoning.

The Dynamic Unity increment is not a new component theorem.  It is the exact
same-antecedent composition and type result:

> The variational action selects a relational obstruction and a coarse
> response decomposition, while the interventional quotient, observer,
> material record, consumer, and ruler remain separately unselected.

This prevents both overclaims:

1. “the action selected nothing”; and
2. “the action selected the observer-accessible world.”

# 10. Science-council disposition

- **Orthodox:** bank the stabilizer criterion and signed-cycle proof at scoped
  Grade 4; all mathematical components are absorbed.
- **Heterodox:** preserve the positive reversal—the selected object may be
  holonomy/no-section rather than a global view.
- **Commercial:** test the new source-selected invariant against the complete
  material-handoff passport before building a larger model.
- **Wild frontier:** a measurable perspectival holonomy would require the
  record/access bridge; this oscillator spectrum is the standard-physics
  control, not that signal.
- **Philosopher:** local physical sections without one global section do not
  imply subjectivity or mind-created reality.  They describe a physical
  local-to-global obstruction.

# 11. Grade, stops, and successor

## Earned

- the general stabilizer fixed-point necessity criterion for covariant
  selection;
- an exact source-pinned signed-cycle action;
- exact gauge-orbit classification by `Z2` holonomy;
- exact spectral visibility of that holonomy;
- exact residual-symmetry nonselection of an observer vertex;
- exact selection of coarse spectral bands but not their internal axes;
- exact nonuniqueness of covariant action families and their quotients;
- exact absolute-ruler nonselection;
- exact regional local-section/global-no-section obstruction; and
- unchanged transfer to ordinary quantized harmonic modes.

## Not earned

- a universal common-view no-go;
- a material record, instrument, sampler, writer, consumer, archive, observer,
  capability horizon, public finality rule, spacetime metric, or scale;
- a non-Abelian, continuum, QFT, gravitational, or cosmological result;
- selection of this action or its coupling signs from a broader theory class;
- new mathematics, new physics, empirical excess, prediction, or ontology;
- a paper, hardware path, provider action, or sibling-repository claim.

## Stops

- Do not rename latent holonomy as a record.
- Do not choose full or low-band access by convention and call it selected.
- Do not turn vertex transitivity into observer inexistence.
- Do not identify the cycle with spacetime or its sign with DU perspectival
  curvature.
- Do not repeat another graph obstruction without testing the missing
  material handoff.

## Selected successor question

The result supplies one new source-pinned invariant worth testing and nothing
more:

> Does an action-selected holonomy naturally select a material sampler,
> provenance-bearing archive, observer access, and matched continuation—or
> do the instrument and consumer freedoms survive unchanged?

This becomes `CTS-A3-ACTION-SELECTED-HOLONOMY-MATERIAL-RECORD-GATE`.  It must
use the complete interface passport and one unchanged standard-quantum or
finite-gauge realization.  A supplied Wilson/QND instrument is a kill, not a
repair.

# Reproducibility

Run:

```bash
python3 tests/du_action_selected_common_view_obstruction_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_action_selected_common_view_obstruction_result.json` and
reports `18/18` checks.

# Final status

**BANKED SCOPED GRADE-4 ACTION-SELECTION AND NONSELECTION RESULT / ONE FROZEN
SIGNED-CYCLE ACTION SELECTS A GAUGE ORBIT, Z2 HOLONOMY, RESPONSE SPECTRUM, AND
COARSE SPECTRAL BANDS / ITS RESIDUAL SYMMETRY SELECTS NO OBSERVER VERTEX OR
AXIS INSIDE A DEGENERATE BAND / MULTIPLE COVARIANT ACTION FAMILIES PRODUCE
DIFFERENT CAUSAL-STATE QUOTIENTS / PROPAGATION DOES NOT SELECT ABSOLUTE RULER
SCALE / EVERY PROPER TREE REGION HAS A NONZERO SECTION WHILE THE FRUSTRATED
CYCLE HAS NO NONZERO GLOBAL SECTION / THE HOLONOMY SURVIVES ORDINARY QUANTUM
OSCILLATOR TRANSFER / ACTION-SELECTED RELATIONAL OBSTRUCTION IS NOT A FORMED
RECORD OR PUBLIC FINALITY / COMPONENT MATHEMATICS ABSORBED / NO UNIVERSAL
NO-GO, NEW PHYSICS, PREDICTION, ONTOLOGY, PAPER, HARDWARE, OR SIBLING CLAIM.**
