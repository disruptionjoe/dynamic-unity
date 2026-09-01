---
title: "Autonomous handoff parity, stability-isospectral nonselection, and anchor boundary"
status: banked_scoped_autonomous_handoff_and_selector_boundary
doc_type: exact_theorem_counterexample_quantum_transfer_and_physical_control_audit
created: 2026-09-01
claim_id: HC-DU-219
run_id: RUN-20260901-autonomous-handoff-parity-and-anchor-boundary
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

This wave executed the highest-information reopener left by `HC-DU-205` and
`HC-DU-218`: replace the externally read record and commanded consumer with the
smallest autonomous local writer--record--consumer dynamics, then ask what the
dynamics actually selects.

The answer is positive and negative in different places:

```text
AUTONOMOUS_MATCHED_HANDOFF_FORMS_CONDITIONALLY
+ RECORD_LABEL_GAUGE_REMOVED
+ HANDOFF_PARITY_SURVIVES
+ STABILITY_AND_SPECTRUM_DO_NOT_SELECT_PARITY
+ TARGET_ANCHOR_DECIDES_GAUGE_VERSUS_PHYSICAL
+ SELECTOR_KEY_RELOCATED_UNLESS_PARITY_IS_DERIVED
+ PUBLIC_AUTONOMOUS_CONTROL_IS_POSITIVE_NOT_COMPLETE
+ NO_READY_SUCCESSOR
```

In plain language:

> Local dynamics can make a record and a downstream response settle into one
> stable, self-correcting relationship. That is real autonomous formation. But
> stability does not decide whether the final target should agree with or
> invert the source. Once arbitrary record names are quotiented away, that one
> source-to-target sign remains. It is physical only relative to a fixed target
> ruler; if the target ruler may also be renamed, it becomes gauge.

This is sharper than the earlier consumer-freedom result. `HC-DU-205` held a
writer and record fixed while choosing among four external consumers. Here the
consumer is inside the dynamics and every update path converges. The ambiguity
does not disappear. It contracts from arbitrary consumer policy to one
gauge-invariant binary handoff parity.

The same boundary transfers exactly to a three-qubit Ising Hamiltonian and to
an autonomous mismatch-correction jump graph. It is absorbed by standard
Ising, gauge, Boolean-network, and open-system mathematics. It is not new
quantum physics. Its value to Dynamic Unity is that it identifies the smallest
remaining selector object: a physically derived cross-boundary orientation,
holonomy, or parity, plus a reason the target ruler is fixed.

# 1. Frozen autonomous model

Let the source, record, and target be

\[
 S,R,T\in\{-1,+1\},
\]

with local coupling signs `a,b in {+1,-1}`. The asynchronous autonomous update
rule is

\[
 R\leftarrow aS\quad\text{when }R\ne aS,
 \qquad
 T\leftarrow bR\quad\text{when }T\ne bR.
\tag{1}
\]

`S` is held fixed during one run. There is no external measurement-conditioned
command. The first rule is the writer interaction; the second is the consumer
interaction. Define the end-to-end handoff parity

\[
 h:=ab.
\tag{2}
\]

The corresponding commuting Ising and three-qubit Hamiltonian is

\[
 H_{a,b}=-J\left(a Z_S Z_R+b Z_R Z_T\right).
\tag{3}
\]

This model is deliberately minimal. It does not contain source provenance, a
durable archive, an observer, public certification, resource semantics, or a
noncommuting quantum effect.

# 2. Autonomous convergence theorem

## Theorem 1 — every schedule reaches one matched handoff

For every fixed `a`, `b`, and source value `S`, every initial pair `(R,T)` and
every admissible asynchronous order of the two corrections in (1) terminates
at

\[
 (R_*,T_*)=(aS,abS)=(aS,hS).
\tag{4}
\]

The absorbing state is unique in each source sector.

## Proof

If the writer constraint is violated, its update makes `R=aS`. It can never be
violated again because `S` is fixed and no other rule changes `R`. The writer
update may make the consumer constraint false, but the consumer update then
makes `T=bR`. Once the writer constraint is satisfied, that consumer update is
permanent. If the consumer fires first, at most one later writer update and one
later consumer update remain. Thus every path has finite length at most three
and ends at (4). Direct enumeration verifies all 32 combinations of coupling,
source, and initial state and every update ordering.

The result earns autonomous *formation relative to the fixed action*. No
outside controller chooses the branch after seeing the record. It does not
derive the signs already written into the action.

# 3. What record-label gauge removes—and what it cannot

An internal record relabeling sends

\[
 R\mapsto-R,
 \qquad
 (a,b)\mapsto(-a,-b).
\tag{5}
\]

It changes neither (1) nor the end-to-end response. The four sign pairs
therefore form exactly two matched record-gauge orbits:

\[
 \{(-1,-1),(+1,+1)\},
 \qquad
 \{(-1,+1),(+1,-1)\}.
\tag{6}
\]

They are classified by `h=+1` and `h=-1`. Thus `a` and `b` separately depend
on the internal record convention, while their product does not.

## The target-anchor fork

A target relabeling sends

\[
 T\mapsto-T,
 \qquad
 b\mapsto-b,
 \qquad
 h\mapsto-h.
\tag{7}
\]

If the target ruler and every target observable co-transform, (7) is another
gauge operation and all four actions lie in one label orbit. If the target
ruler is fixed independently—for example, the target sign is tied to a
calibrated physical actuation—then (7) is not an admissible gauge move and
`h` distinguishes two physical response classes.

This conditional must remain explicit. A sign cannot be both a physical
prediction and a freely relabeled convention in the same contract.

# 4. Stability and spectrum do not select the anchored parity

## Theorem 2 — stability-isospectral nonselection

All four actions have:

- the same unique-attractor count;
- the same exhaustive asynchronous path-length histogram;
- the same classical energy multiplicities; and
- the same three-qubit diagonal quantum spectrum.

Yet, relative to a fixed target ruler, the two values of `h` produce opposite
source-to-target response.

The common all-path histogram is

```text
length 0: 2 paths
length 1: 4 paths
length 2: 2 paths
length 3: 2 paths
```

for each sign pair after both source sectors are combined. The dimensionless
energy `H/J` has common multiplicities

```text
-2: 2 states
 0: 4 states
+2: 2 states
```

Therefore convergence, stability, gap, and spectrum cannot choose the
anchored end-to-end parity. A physical action with fixed coefficients does
select one parity conditionally, but saying “the action contains `h`” has only
moved the selector into a one-bit action datum unless a prior law derives it.

This is not a universal theorem that every autonomous interface leaves one
bit. It is the smallest exact counterexample to the stronger claim that stable
autonomous handoff formation alone selects the complete anchored response.

# 5. Exact Gibbs and quantum transfer

At `beta J = ln 2`, direct rational enumeration gives

\[
 \langle SR\rangle=a\frac35,
 \qquad
 \langle RT\rangle=b\frac35,
 \qquad
 \langle ST\rangle=ab\frac{9}{25}=h\frac{9}{25}.
\tag{8}
\]

The local correlations carry the convention-dependent signs, while the
source-to-target correlation exposes the record-gauge-invariant parity.

For the quantum Hamiltonian (3), conjugation by `X_R` implements (5), while
conjugation by `X_T` implements (7). Every sign choice is isospectral, but the
fixed-ruler thermal response `\langle Z_S Z_T\rangle` changes sign with `h`.
The asynchronous correction graph can likewise be embedded as population
dynamics with mismatch-conditioned local jumps.

This is a transfer control inside ordinary quantum/open-system theory. Because
the Hamiltonian is diagonal in the declared basis, it earns no noncommuting
quantum advantage and no excess prediction over standard physics.

# 6. Physical positive controls and the public-packet boundary

The bounded primary-source search found one especially relevant new control:

- Irfan et al., [*Autonomous Stabilization of Remote Entanglement in a Cascaded
  Quantum Network*](https://doi.org/10.1103/z6zz-vw5q), physically stabilize a
  remote entangled steady state using a nonreciprocal waveguide, local drives,
  and a coherent quantum-absorber architecture. Their
  [open dataset](https://doi.org/10.5281/zenodo.19688682) includes experimental
  data, analysis code, and documentation.

This is a stronger physical positive control for *autonomous distributed
relation formation* than a local software toy. It also displays the boundary
honestly: the apparatus, chiral coupling, drive parameters, symmetry choice,
and tomography are engineered. The paper reports that device imbalance breaks
the first target symmetry and that a modified, parameter-matched symmetry is
more robust. The experiment therefore shows that a prepared dissipative law
can stabilize a selected relation; it does not show that physics selected the
law, the target symmetry, an observer record, or a target ruler without those
antecedents.

The existing Rigetti/Riverlane [real-time-QEC
dataset](https://zenodo.org/records/15364358) remains the stronger public packet
for an explicit returned-shot record--decoder--action--response chain. It still
lacks the all-attempt controller, route, archive, and reset lineage required by
`HC-DU-218` for implementation completeness. The Irfan packet avoids an
external classical feedback loop but does not replace that missing lineage: it
is an engineered reservoir-steady-state experiment, not the complete typed
writer--record--consumer packet.

Other bounded search hits were simulations, aggregate trajectories, ordinary
state tomography, or unrelated device data. No stronger public
implementation-complete handoff was established. That is a bounded search
result, not proof that no such dataset exists.

# 7. Relation to the existing theorem spine

This result advances rather than repeats four prior boundaries:

1. `HC-DU-204` removed matched producer--consumer label conventions. The new
   result identifies the invariant `h` left after that quotient.
2. `HC-DU-205` proved broad consumer freedom for a fixed writer. The new result
   internalizes the consumer and contracts that freedom to two anchored
   handoff classes.
3. `HC-DU-207` showed that an action can select a `Z2` holonomy while leaving
   record and ruler interfaces open. The new `h` is the smallest chain analogue
   of such a cross-boundary sign, without claiming the two objects are
   identical.
4. `HC-DU-218` proved the attribution of a complete prepared handoff. The new
   result shows exactly how far autonomous stable interaction moves beyond
   that prepared case and where it stops.

# 8. What is earned

At scoped Grade 4, Dynamic Unity may bank:

1. the exact autonomous convergence theorem for the frozen binary chain;
2. the two-orbit record-gauge quotient and invariant handoff parity;
3. the stability-isospectral nonselection counterexample;
4. the target-anchor gauge/physical fork;
5. the exact Gibbs response and diagonal quantum/open-system transfer; and
6. the physical calibration that autonomous dissipative stabilization is real
   but conditional on an engineered action and target symmetry.

Dynamic Unity has not earned:

- a universal one-bit no-go;
- derivation of the parity, coupling signs, target ruler, or candidate class;
- a complete material record, provenance, observer, or public-finality packet;
- a noncommuting quantum result;
- source issuance or a physical remainder;
- a novel empirical prediction; or
- a selected scientific successor.

# 9. Exact reopener

Do not build another autonomous feedback toy. Reopen this seam only with a
source-pinned physical theory that does at least one of the following:

1. derives an anchored cross-boundary parity/holonomy from premises that do not
   already name it, and survives premise ablation and benign enlargement;
2. proves that the target ruler co-transforms, so the apparent twofold choice is
   genuinely gauge rather than physical;
3. produces a complete material writer--record--consumer--access--provenance
   packet with a locked no-refit target; or
4. yields a same-record/different-target remainder after the lawful action and
   all selected interfaces are frozen.

The best GU-independent route is now more precise: search for a physical
cross-boundary anchor, not merely a stable interface. Until such an antecedent
or packet appears, the Lane-1 portfolio remains honestly `no_ready`.

# 10. Reproduction

Run:

```bash
python3 tests/du_autonomous_handoff_parity_selector_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_autonomous_handoff_parity_selector_result.json` and reports
`14/14` checks.
