---
title: "Quantum-strength selection frontier gate"
status: completed_bounded_frontier_gate
date: 2026-07-25
run_id: RUN-20260725-100452-record-formation-certified-composition
claim_grade: "EXACT FINITE LO/PR SPECIALIZATION + LANDSCAPE NO-GO / KNOWN COMPONENT MATHEMATICS / QUANTUM SELECTION OPEN"
implementation:
  - ../tests/du_quantum_strength_selection_probe.py
artifact:
  - ../tests/artifacts/du_quantum_strength_selection_result.json
program_refs:
  - HC-DU-035C
  - HC-DU-039
  - H-CCR-12
  - H-CCR-16
---

# Quantum-strength selection frontier gate

## Question and hard answer

Can an independently motivated certified-causal composition or finality
principle admit ordinary quantum correlations while excluding the PR box or
another no-signalling foil?

**Bounded answer: yes for PR exclusion, no for quantum selection.**

A natural Dynamic Unity principle has three clauses:

1. finalized event certificates that disagree on the output of the same local
   input are mutually incompatible;
2. every pairwise incompatible certificate family has total probability at
   most one; and
3. independently formed regions inherit that rule under product composition.

On a Bell-event interface, these clauses are exactly the established
**Local Orthogonality** principle, or the Bell-scenario instance of
**Consistent Exclusivity**. They admit all ordinary quantum behaviors and
exclude two independent PR boxes by an exact five-event witness. But they do
not select ordinary quantum theory: the strictly larger almost-quantum set
satisfies Local Orthogonality and Consistent Exclusivity.

The frontier gate therefore returns:

```text
PR EXCLUSION FEASIBLE UNDER INDEPENDENT COMPOSITION
CANDIDATE COLLAPSES TO KNOWN LO/CE
ORDINARY QUANTUM NOT SELECTED
```

The result is useful because it locates the next missing structure precisely.
Probability-level incompatibility is too weak. A viable successor has to work
at the level of **physically formed sharp record instruments and their global
composition**, without inserting the quantum formalism it aims to recover.

## Frozen operational landscape

The scenario is binary CHSH:

```text
x,y in {0,1}
a,b in {0,1}
p(a,b|x,y).
```

The common interface freezes:

- setting and outcome identities;
- complete conditional tables;
- measurement independence;
- no-signalling as the causal-admissibility boundary;
- product composition for two independently formed copies;
- the local exclusivity relation;
- no provenance, decoder, setting, or event-identity refit per behavior.

Keep the classes separate:

```text
local
    proper subset ordinary quantum
    proper subset almost quantum
    proper subset no-signalling
    proper subset valid conditional tables.
```

The displayed nesting uses almost quantum only as a named strict outer class
containing the ordinary quantum set; it does not assert that every
no-signalling behavior is almost quantum. Signalling tables are outside the
frozen causal landscape rather than a stronger admissible theory.

## Candidate principle and its prior-art identity

Call the candidate **Certified Exclusivity under Independent Regional
Composition**:

> If two certified events assign different outputs to the same local
> measurement, they cannot both occur. Every pairwise incompatible family has
> probability sum at most one, and independent regional composition preserves
> this constraint.

The architectural motivation is native to Dynamic Unity:

- public finality needs an incompatibility condition;
- overlap identities must be frozen before composition;
- a higher region should not certify mutually contradictory local records;
- independent regions must compose without changing event semantics.

The mathematics is not native novelty. Fritz et al. define Local
Orthogonality by exactly the same event relation, prove that it is equivalent
to no-signalling in bipartite scenarios, prove that quantum correlations
satisfy it, and show that two copies of a PR box violate it
([primary source](https://arxiv.org/abs/1210.3018)). Acín et al. place the
same structure in contextuality hypergraphs and show that LO is a special
case of a broader consistent-exclusivity construction
([primary source](https://arxiv.org/abs/1212.4084)).

Therefore:

```text
DU finality language
    + probability-level incompatibility
    + product closure
    =
known LO/CE specialization,
not a new quantum-strength law.
```

## Exact finite result

The executable probe returns `25/25`.

### One PR box passes

The PR behavior is

\[
p_{\mathrm{PR}}(a,b\mid x,y)
=
\begin{cases}
\frac12,&a\oplus b=xy,\\
0,&\text{otherwise}.
\end{cases}
\]

It is a valid no-signalling behavior with `CHSH=4`. Among its eight supported
events, the exact maximum locally orthogonal clique has size two. Each
supported event has probability `1/2`, so the maximum one-copy LO sum is
exactly one.

This is the essential first no-go:

> Local certificate incompatibility at one bipartite layer cannot distinguish
> PR from admissible no-signalling behavior.

That is not a failure to find the right inequality. In the bipartite scenario,
LO and no-signalling are equivalent.

### Two independent PR boxes fail

For two independently composed copies, the following events are pairwise
locally orthogonal:

\[
\begin{aligned}
&(0000\mid0000),\\
&(1110\mid0011),\\
&(0011\mid0110),\\
&(1101\mid1011),\\
&(0111\mid1101).
\end{aligned}
\]

Every event is supported with probability `1/4`, hence

\[
\sum_{i=1}^{5}p(e_i)=\frac54>1.
\]

The probe independently verifies every pairwise orthogonality relation,
every probability, the exact excess `1/4`, and by exhaustive clique search
over all `64` supported product events verifies that the maximum supported
clique has size five.

This supplies a real composition result:

> A probability-level incompatibility rule that is stable under independent
> regional composition admits a single PR box but excludes two independently
> available PR boxes.

It is an exclusion under declared assumptions, not a proof that product
composition is physically selected by Dynamic Unity.

### Ordinary quantum behavior is admitted

If two quantum Bell events are locally orthogonal, their product projectors
are orthogonal because one party uses the same projective measurement with
different outcomes. Any pairwise locally orthogonal family therefore obeys

\[
\sum_i P_i\leq I
\quad\Longrightarrow\quad
\sum_i\operatorname{Tr}(\rho P_i)\leq1.
\]

The argument persists under arbitrary independent copies. The exact
CHSH-optimal isotropic control in the probe has

\[
S=2\sqrt2
\]

and the displayed five-event sum

\[
\frac{15+10\sqrt2}{32}<1.
\]

This is an admission receipt for ordinary quantum theory, not a selection
receipt.

## Why this does not recover the Tsirelson boundary

Tsirelson's `2 sqrt(2)` bound follows from ordinary quantum operator geometry
([primary source](https://doi.org/10.1007/BF00417500)). Local Orthogonality
knows only a binary event relation:

```text
exclusive / not exclusive.
```

It does not determine:

- nonzero overlaps between compatible events;
- a positive-semidefinite moment or Gram structure;
- which event effects belong to one complete instrument;
- how compatible instruments compose sequentially;
- which tensor or commuting-operator representation is physical; or
- why a particular state/effect geometry is selected.

That loss is decisive. Navascués et al. construct the strictly supraquantum
almost-quantum set and prove that it satisfies Local Orthogonality,
Macroscopic Locality, nontrivial communication complexity, and no advantage
for nonlocal computation; they report numerical rather than theorem-level
support for Information Causality
([primary source](https://arxiv.org/abs/1403.4621)). Consequently, the
probability-level candidate leaves at least

```text
ordinary quantum
    proper subset almost quantum
    subset candidate-admissible correlations.
```

No theorem in this gate identifies the final inclusion with equality.

## Collision with the named principles

| Principle or framework | What it adds | PR disposition | Why it does not finish DU |
|---|---|---|---|
| Tsirelson bound | Hilbert/operator geometry bounds CHSH by `2 sqrt(2)` | Excluded directly | It is the target quantum theorem, not an independently derived DU premise |
| Information Causality | Bounds remote information gain by communicated information | A single PR box violates it through a one-bit perfect random-access code | It imports a communication task and information measure; it does not characterize the full quantum set |
| Macroscopic Locality | Requires a classical local macroscopic fluctuation limit | PR is excluded | The admitted set is larger than quantum; the principle is macroscopic-statistical rather than formed-record composition |
| Local Orthogonality | Pairwise locally exclusive event sums, stable under copies | One PR passes; `PR^2` fails at `5/4` | This is exactly the current candidate at probability level |
| Consistent Exclusivity | Extends pairwise event exclusivity to general contextuality scenarios and products | Excludes some postquantum models | Almost-quantum models satisfy it; event statistics omit measurement structure |
| Quantum causal models | Replace classical common-cause factorization with quantum channels and quantum conditional independence | PR is not an ordinary quantum realization | The quantum state/channel structure supplies the restriction; causal certification alone has not derived it |
| Causally local indivisible stochastic processes | A specific 2026 framework reports a CHSH derivation of the Tsirelson bound | PR excluded in that framework | Any DU causal-locality derivation now collides directly and must differ in assumptions, reach, or consequence |

Information Causality is kept distinct in the executable. In the standard
protocol, Alice holds two independent bits and sends one classical bit. With a
PR box Bob recovers either requested bit perfectly, so the information sum is
`2` bits while the message contains `1`
([primary source](https://arxiv.org/abs/0905.2292)).

Macroscopic Locality recovers a classical macroscopic limit but admits a set
beyond ordinary quantum
([primary source](https://arxiv.org/abs/0907.0372)). It is not a synonym for
LO, finality, or coarse-grained record formation.

Allen et al.'s quantum causal models provide a genuine generalized
common-cause factorization using quantum channels
([primary source](https://arxiv.org/abs/1609.09487)). That is a constructive
exit from Bell-classical causation, but the word “causal” does not by itself
explain the quantum-strength boundary.

Finally, Barandes, Hasan, and Kagan derive the CHSH quantum bound inside a
particular causally local, indivisible stochastic-process framework
([primary source](https://arxiv.org/abs/2512.18105)). A DU result based only
on renamed causal locality or process indivisibility would be absorbed unless
it changes the premise set, yields a broader theorem, or derives its
stochastic-quantum structure from formed records.

## The sharper reopener: from events to formed sharp instruments

The most important correction is that probability-level Consistent
Exclusivity is only a consequence of a stronger measurement-level idea.
Gonda et al. distinguish:

```text
pairwise exclusive event probabilities
    !=
pairwise compatible measurements
    !=
one global joint measurement.
```

For sharp quantum measurements, Specker's principle says that pairwise joint
measurability implies global joint measurability. Gonda et al. prove that no
general probabilistic theory can both yield almost-quantum models and satisfy
Specker's principle, even though almost-quantum correlations satisfy
Consistent Exclusivity
([primary source](https://arxiv.org/abs/1712.01225)).

This makes the move from events to instruments a **viable Dynamic Unity
tension**, but not yet a novel DU axiom:

- **Established reach:** Specker-style sharp-measurement principles already
  expose structure that event-level CE misses.
- **Exact tension:** “sharp,” “pairwise compatible,” and “globally jointly
  measurable” are usually supplied properties. Dynamic Unity's central
  problem is how a physical process forms and selects the record instruments
  to which those predicates apply.
- **Potential DU delta:** derive a record-relative sharpness and composition
  law from physical formation, nondisturbance, repeatability, provenance,
  continuation, and access—then show when pairwise formed records do or do not
  descend to one global joint instrument and public action algebra.
- **Restatement boundary:** postulating Specker's principle, citing its
  almost-quantum exclusion, or calling projectors “final records” is occupied
  terrain.

Specker's principle also does not by itself prove that the complete ordinary
quantum set is uniquely selected. It removes an important named outer foil.
Further postquantum classes and the full state/transformation structure remain
to be classified.

## Exact reopener

Reopen this frontier only with a **Formed-Sharp Instrument Composition**
candidate satisfying all four requirements:

1. **Physical sharpness formation.** Starting from an independently fixed
   process, derive a noncircular criterion under which a record instrument is
   repeatable, nondisturbing on its stable algebra, and robustly accessible.
   Do not supply the projective basis or declare durability to be sharpness.
2. **Complete pairwise receipts.** Certify compatibility at the level of
   selective CP maps and held-out multi-time continuations, not only equal
   effects or pairwise marginals.
3. **Global composition theorem or obstruction.** Prove conditions under
   which pairwise compatible formed-sharp regional instruments possess one
   global joint instrument whose boundary certificate is action-sufficient;
   otherwise return a finite typed obstruction.
4. **Two-sided landscape result.** Constructively admit ordinary projective
   quantum instruments and exclude a declared almost-quantum/Specker witness
   for the same independently frozen reason. Then test whether a stronger
   postquantum foil remains.

The potential paper-shaped theorem is:

> **Formed-Sharp Descent Theorem.** Under independently stated physical
> formation, sharpness, provenance, access, and regional-independence
> conditions, pairwise compatible record instruments descend to a global
> action-sufficient instrument if and only if a declared composition
> obstruction vanishes.

That theorem would connect `HC-DU-033` record formation to `HC-DU-035C`
regional descent and could supply a real `HC-DU-039` invariant. Its novelty
would lie in deriving the applicable instrument class and carrying
action/provenance semantics—not in the abstract pairwise-to-global axiom.

## Landscape card

```yaml
card_id: DU-QS-01
operational_object: binary Bell event certificates under independent regional composition
frozen_assumptions:
  - complete conditional tables
  - fixed event and setting identities
  - measurement independence
  - no-signalling causal boundary
  - product composition for independent copies
  - local exclusivity inherited under composition
restrictive_foil: local common-cause behaviors
target_class: ordinary quantum behaviors
permissive_foil: no-signalling behaviors including PR
membership_receipt: explicit local and exact CHSH-boundary quantum realizations inherited from the landscape calibration
exclusion_receipt: exact five-event PR-squared LO witness with sum 5/4
selection_principle: Certified Exclusivity under Independent Regional Composition
held_out_discriminator: almost-quantum class satisfies probability-level LO/CE
disposition: PR_EXCLUDED_UNDER_COMPOSITION__QUANTUM_NOT_SELECTED
does_not_establish:
  - new LO/CE mathematics
  - a Dynamic Unity derivation of the Tsirelson bound
  - exclusion of almost-quantum correlations
  - a physical record-selection law
  - record-first ontology
```

## Program consequence

This gate should **not** become another broad quantum-principles branch. Its
use is surgical:

- retain the exact `PR^2` result as a regression control for any regional
  composition law;
- stop probability-only exclusivity or “finality Tsirelson” work;
- route the formed-sharp instrument reopener into the primary record-formation
  branch and the certified-overlap composition branch;
- demand a direct Gonda/Specker, almost-quantum, LO/CE, quantum-causal, and
  Barandes collision audit before novelty language.

No theorem ID, hypothesis ID, prediction, ontology, paper priority, or lane
state changes in this bounded artifact.
