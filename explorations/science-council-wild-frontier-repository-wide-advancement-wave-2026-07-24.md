---
title: "Science Council wild-frontier scientist — repository-wide advancement wave"
status: completed_independent_council_swing
doc_type: council_persona_research_memo
created: 2026-07-24
persona: wild_frontier_scientist
scope: "Dynamic Unity and the Certified Causal Reality program as a whole"
probe: tests/du_council_wild_frontier_interventional_closure_probe.py
artifact: tests/artifacts/du_council_wild_frontier_interventional_closure_result.json
claim_grade: "EXACT FINITE DETERMINISTIC AND LINEAR SPECIALIZATION / CENTRAL PHYSICAL CONJECTURE OPEN"
novelty_status: "KNOWN AUTOMATA AND LINEAR-EQUIVALENCE TERRAIN / CCR CONJUNCTION SEARCH-INCOMPLETE"
banked: false
seeded: false
---

# Wild-frontier repository-wide advancement wave

## Repository-wide reading

I did not treat `HC-DU-035A`, thresholds, or its proposed successor as the
assigned topic. I surveyed the new program as a whole.

The strongest fact about the current repository is not any one positive
mechanism. It is that several waves have independently converged on the same
failure mode:

```text
a static or terminal quotient looks complete
    until a later intervention exposes a distinction it erased.
```

Examples already present in the repository include:

- exact Clock-QCA covariance without entailed observer memory;
- a covariant recorder whose informative action necessarily affects
  cross-history coherence;
- an archive that looks relocatable for a restricted observable algebra but
  ceases to be equivalent when reunion and recoupling are admitted;
- a CSG predictive quotient that is exact for the declared transition
  algebra but not thereby an observer record, geometry, or physical source;
- a hidden global scheduler that can compile every finite causal DAG but is
  gauge only if all admitted interventions factor through the schedule
  quotient;
- recursive architectures whose endpoints tie while controller lesions
  separate their causal roles;
- the finite classical record quotient `HC-DU-033A`, which classifies supplied
  equality and access constraints but is not yet a process congruence; and
- `HC-DU-035A`, which shows that reconstruction, finality, and capability do
  not collapse into one scalar crossing.

This makes the central `HC-DU-036` question unusually ripe. The repository has
many quotients and many intervention-relative counterexamples, but it does not
yet have one exact machine that takes an independently supplied record
quotient and returns either:

1. a proof that all declared future behavior factors through it; or
2. the shortest finite intervention exposing the erased physical remainder.

That is the swing I chose.

## Candidate attempts considered

Scores are from 1 (weak) to 5 (strong). “One swing” means the chance of earning
a defensible theorem, countermodel, or quantitative discriminator now—not the
chance that the eventual foundational claim is true.

| Rank | Materially different attempt | Profundity | Usefulness | Novelty potential | Publishability | Defensible one-swing advance | Judgment |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **Interventional closure and finite remainder witness** (`HC-DU-036`) | 5 | 5 | 3 | 4 | 5 | It directly adjudicates the charter’s ontology fork and admits an exact finite theorem now. |
| 2 | **Multi-time coherent-history certification** (`HC-DU-034`) | 4 | 5 | 3 | 5 | 4 | A proper-time or Clock-QCA process assay could be experimentally sharp, but its complete instrument class and physical readout still need freezing. |
| 3 | **Physical record/interface selection** (parent `HC-DU-033`) | 5 | 5 | 5 | 5 | 2 | This is the deepest dependency, but another merely admissible recorder would not advance it; an autonomous selector or no-go needs more physical input. |
| 4 | **Formation-to-finality resource law** (`HC-DU-035B`) | 4 | 5 | 4 | 4 | 2 | Potentially important, but it must begin from a physically selected instrument that the repository does not yet possess. Starting after the cut would repeat known terrain. |
| 5 | **Meta-record geometry reconstruction** (`HC-DU-038`) | 5 | 4 | 4 | 4 | 2 | High ceiling, but present provenance graphs do not yet carry an independently selected scale, metric, or sufficient held-out geometry. |
| 6 | **Global scheduler gauge-or-witness theorem** (`H-CCR-11`) | 4 | 4 | 3 | 4 | 4 | Buildable and useful, but narrower than the general factorization problem; it should become one test case of the chosen theorem. |
| 7 | **Causal-growth generativity to held-out geometry** | 5 | 3 | 4 | 3 | 1 | The projective predictive state is exact, but recurrence, family selection, active return, scale, and geometry remain jointly open. |
| 8 | **GU/QFT/GR recovery or ablation** (`HC-DU-040`) | 5 | 3 | 5 | 3 | 1 | Potentially enormous, but dependency-violating now. A flexible recovery map would be interpretation rather than evidence. |

The threshold work therefore changes the controls, but it does not determine
the frontier choice. The best repository-wide swing is the factorization fork.

# Chosen swing: the Interventional Closure Dichotomy

## 1. Frozen finite deterministic contract

Let:

- \(S\) be a finite state or complete-history realization, \(|S|=n\);
- \(A\) be a finite alphabet of admitted interventions;
- \(T_a:S\to S\) be the frozen transition for intervention \(a\);
- \(R:S\to Q\) be an **independently supplied** record or certificate map; and
- \(Y:S\to O\) be an independently declared observer-accessible physical
  readout.

`R` is not defined from `Y` or from every target experiment. It must have been
selected before this test. The diagnostic observation at a state is

\[
Z(s)=(R(s),Y(s)).
\]

Including future `R` values in `Z` is necessary: a quotient is not a process
quotient if two members of one current record class evolve to different future
record classes under the same admitted intervention.

For a word \(w=a_1\cdots a_k\), write \(T_w\) for the corresponding composed
intervention. Define behavior

\[
B_s(w)=Z(T_w s).
\]

The supplied record is interventionally sufficient within this contract when

\[
R(s)=R(t)
\quad\Longrightarrow\quad
B_s(w)=B_t(w)
\quad
\text{for every }w\in A^*.
\]

This is a strong local result, not universal ontology. It is relative to the
declared state class, interventions, readout, and resources.

## 2. Interventional closure construction

Let \(E_R=\ker R\) and

\[
E_0=\ker R\cap\ker Y.
\]

Recursively define

\[
E_{k+1}
=
E_k
\cap
\bigcap_{a\in A}T_a^{-1}(E_k),
\]

where

\[
(s,t)\in T_a^{-1}(E_k)
\iff
(T_a s,T_a t)\in E_k.
\]

Each step can only split classes. Since \(S\) is finite, the sequence reaches
a stable relation \(E_*\).

### Theorem 1 — finite interventional closure

\(E_*\) is the greatest transition congruence contained in
\(\ker R\cap\ker Y\). Consequently:

1. the quotient \(q_*:S\to S/E_*\) carries \(R\) and \(Y\);
2. every \(T_a\) descends uniquely to \(S/E_*\);
3. every other deterministic process quotient refining \(R\) and carrying
   \(Y\) refines \(q_*\); and
4. the supplied record is interventionally sufficient exactly when
   \[
   E_*=\ker R.
   \]

#### Proof

Every \(E_k\) is an equivalence relation. The recursion preserves only pairs
that were already equivalent and whose images under every intervention remain
equivalent. Stability therefore makes \(E_*\) a congruence, and
\(E_*\subseteq E_0\).

Let \(C\subseteq E_0\) be any other transition congruence. Inductively,
\(C\subseteq E_k\): this is true at \(k=0\), and if it is true at \(k\), then
transition stability gives
\((s,t)\in C\Rightarrow(T_as,T_at)\in C\subseteq E_k\) for every \(a\).
Thus \(C\subseteq E_{k+1}\), and hence \(C\subseteq E_*\). So \(E_*\) is the
greatest such congruence.

Because \(R\) and \(Y\) are constant on \(E_*\), they factor through \(q_*\).
Because \(E_*\) is transition-stable, each \(T_a\) also factors through
\(q_*\). The same induction proves that states in one \(E_*\) class have equal
behavior for every word. Conversely, behavioral equivalence is itself a
transition congruence contained in \(E_0\), so it equals \(E_*\).

Since \(E_*\subseteq\ker R\), all same-record states have equal behavior
exactly when equality holds. \(\square\)

### Interpretation

The diagnostic \(q_*\) is the **minimal remainder-augmented predictive
state**. It must not be renamed a physically formed record. It was computed
using the target readout and is therefore evidence about what `R` omitted,
not an independently selected replacement for `R`.

The result gives the charter’s three local outcomes cleanly:

```text
E_* = ker R
    -> factorization through the supplied record, within the frozen class

E_* strictly refines ker R
    -> a finite physics-first remainder witness exists

model/intervention/readout class not frozen
    -> comparison contract incomplete; no verdict
```

Underidentification is therefore not silently reported as duality.

## 3. Bounded witness theorem

Let \(b_0\) be the number of classes in \(E_0\).

### Theorem 2 — finite witness bound

If \(R\) is not interventionally sufficient, then there are
\(s,t\in S\) with \(R(s)=R(t)\) and an intervention word \(w\) such that

\[
Z(T_w s)\ne Z(T_w t),
\]

with

\[
\boxed{|w|\le n-b_0.}
\]

The bound is tight for every \(n\ge3\).

#### Proof

A strict refinement of a finite partition increases its number of classes by
at least one. Starting with \(b_0\) classes, the sequence can therefore have
at most \(n-b_0\) strict refinements.

If a pair first splits in \(E_k\), unfolding the definition produces a word
of length at most \(k\) whose terminal observations differ. If \(E_*\) is
strictly finer than \(\ker R\), either a same-record pair is already split in
\(E_0\), giving a length-zero witness, or it splits during those at most
\(n-b_0\) refinements.

For tightness, take states \(0,\ldots,n-1\), one intervention

\[
T(i)=\min(i+1,n-1),
\]

a constant record, and readout

\[
Y(i)=\mathbf 1[i=n-1].
\]

The initial partition has two classes. States \(0\) and \(1\) first differ
after \(n-2=n-b_0\) interventions. \(\square\)

The smallest delayed deterministic witness has three states:

```text
states:       0, 1, 2
record:       0, 0, 0
current Y:    0, 0, 1
T:            0->1, 1->2, 2->2
tested pair:  0 versus 1
```

The pair has the same record and current readout. One intervention produces
readouts `0` and `1`. Exhaustive enumeration confirms that no two-state unary
deterministic machine can provide a positive-length witness when the pair’s
current record and readout agree.

## 4. Linear witness-rank extension

The deterministic partition theorem is not the most general result available
in one swing.

Let a finite multi-event process have a \(d\)-dimensional linear
representation:

- each admitted intervention or outcome branch is a linear map \(M_a\);
- \(v\) is the difference between two candidate initial realizations with the
  same supplied record; and
- \(\ell\) is a declared terminal readout effect.

The difference produced by word \(w\) is

\[
f(w)=\ell(M_wv).
\]

Define the reachable distinction space

\[
V_\infty(v)
=
\operatorname{span}\{M_wv:w\in A^*\}
\]

and its supplied-realization rank

\[
r(v)=\dim V_\infty(v).
\]

### Theorem 3 — reachable-rank witness bound

If any word distinguishes the two candidates, a word of length at most

\[
\boxed{r(v)-1}
\]

does.

#### Proof

Let

\[
V_k=\operatorname{span}\{M_wv:|w|\le k\}.
\]

If \(V_{k+1}=V_k\), then \(V_k\) is invariant under every \(M_a\), so no later
word can enlarge it. Before stabilization, each depth increases dimension by
at least one.

Suppose the shortest detecting word has length \(k\). The functional
\(\ell\) annihilates \(V_{k-1}\), while it does not annihilate the vector
produced at length \(k\). Therefore \(V_k\) strictly enlarges
\(V_{k-1}\). Every preceding level must also have enlarged, or stabilization
would already have occurred. Starting from the one-dimensional span of
nonzero \(v\), \(r(v)\ge k+1\), hence \(k\le r(v)-1\). \(\square\)

For an \(n\)-state trace-preserving classical process comparing two point
states, \(v=e_s-e_t\) lies in the invariant zero-sum subspace, so
\(r(v)\le n-1\) and the bound becomes \(n-2\). The tight chain above has
\(r(v)=n-1\) and first witness length \(n-2\).

For trace-nonincreasing classical or quantum instrument branches, use the
full finite operator-space dimension unless a smaller invariant subspace is
proved. A \(D\)-dimensional quantum system has a \(D^2\)-dimensional Hermitian
operator space, giving only a coarse \(D^2-1\) word bound in the most direct
finite representation. This does **not** cover arbitrary unbounded-memory
process tensors; finite linear realization is an imported assumption.

The raw reachable rank is invariant under invertible coordinate changes, but
can be inflated by gratuitous unobservable state. A fully behavioral rank
should be defined through a minimal realization or the Hankel rank of
\(f(w)\). That stronger representation-free statement is a successor
hypothesis, not an earned theorem here.

## 5. Executable finite result

The probe
`tests/du_council_wild_frontier_interventional_closure_probe.py` uses only the
Python standard library and exact rational arithmetic. Its deterministic JSON
artifact is
`tests/artifacts/du_council_wild_frontier_interventional_closure_result.json`.

It passes `9/9` named checks:

- exhaustive closure-versus-shortest-word agreement for `67,332`
  one-intervention machines through four states, covering `199,232`
  same-record pairs;
- the bound above across all those pairs;
- exhaustive closure-versus-shortest-word agreement for `5,898`
  two-intervention machines through three states and `17,560` state pairs;
- exact minimality of the three-state delayed witness;
- a tight chain family from three through eight states;
- exact equality of witness length and reachable rank minus one on that
  family;
- a positive factorizing quotient;
- invariance of the minimal behavior quotient under one exact
  state-duplication construction; and
- a declared binary decision fixture in which one intervention reduces
  hypothesis error from \(1/2\) to \(0\).

The tight family gives:

| Raw states \(n\) | Initial behavior classes \(b_0\) | Stable classes | Shortest witness | Reachable rank |
|---:|---:|---:|---:|---:|
| 3 | 2 | 3 | 1 | 2 |
| 4 | 2 | 4 | 2 | 3 |
| 5 | 2 | 5 | 3 | 4 |
| 6 | 2 | 6 | 4 | 5 |
| 7 | 2 | 7 | 5 | 6 |
| 8 | 2 | 8 | 6 | 7 |

This is a computed finite countermodel to the idea that same present record
and readout imply process sufficiency.

## 6. Why this matters to Certified Causal Reality

The program’s “physical remainder” no longer needs to remain a verbal
residual. In a frozen finite process it becomes:

1. a pair inside one supplied record class;
2. the shortest intervention word that separates it;
3. the readout gap produced by that word; and
4. the minimal stable predictive refinement \(S/E_*\).

That is more useful than asking whether information or physics is
metaphysically fundamental in the abstract.

It also unifies several repository lessons without identifying unlike
physical objects:

- **Clock/archive:** a restricted archive readout may merge histories that
  carrier reunion or coherent recoupling later separates.
- **Scheduler:** a scheduler quotient is gauge exactly when its classes are
  closed under the full admitted intervention behavior.
- **Distributed system:** equal finalized endpoints can conceal different
  lock or provenance states that a view change exposes.
- **Recursive control:** equal endpoint viability can conceal different
  intervention-role structure that a lesion exposes.
- **Causal growth:** two finite-prefix-equivalent laws can differ after a
  longer experiment; without a finite model-class bound, no uniform short
  witness follows.
- **Quantum process:** equal terminal density operators need not imply equal
  multi-time instrument statistics.

The common object is not “consensus is quantum mechanics.” It is the closure
of an equivalence relation under a declared intervention algebra.

## 7. Imported assumptions and exact boundary

The advance imports all of the following:

1. a finite state space or finite-dimensional linear realization;
2. a stationary, frozen intervention alphabet and maps;
3. an independently supplied record map;
4. a declared observer readout family;
5. exact equality, not experimental tolerance;
6. repeatable state preparation sufficient to compare candidate responses;
7. no adversarial mid-experiment change to the maps;
8. no free extension of the model class after seeing the witness; and
9. enough control to execute the separating word.

It does not supply:

- physical record formation or interface selection;
- completeness of the intervention family;
- a provenance or adversary model;
- public finality;
- approximate/noisy statistical power;
- thermodynamic or coherence costs;
- continuum, relativistic, or field-theoretic realization;
- observer individuation;
- geometry reconstruction; or
- ontological priority.

`q_*` cannot be promoted to the record quotient, because it was computed with
the target readout. Its legitimate role is to identify the minimal omitted
predictive distinction.

## 8. Rivals and hostile readings

### Rival A — unrestricted completion

An unrestricted hidden-state or time-dependent model can reproduce any finite
test and postpone divergence. The finite bound is meaningful only after a
finite realization class or a separately justified rank bound is frozen.

### Rival B — weak intervention manufacture

A record can appear sufficient because the test alphabet never perturbs the
hidden distinction. This proves only relative sufficiency. Instrument
completeness must be argued physically, not inferred from a passed test.

### Rival C — target-defined records

One could simply replace \(R\) by \(q_*\) and declare victory. That would be
the forbidden sufficiency tautology. The refinement is a remainder
diagnostic until an independent formation law produces it.

### Rival D — exact but operationally invisible gap

An arbitrarily small probability difference is mathematically nonzero but may
require prohibitive repetitions, coherence time, energy, or control
precision. A physical theorem needs a gap and resource bound, not only a word
length.

### Rival E — nonminimal representation

Raw state count and reachable rank can be inflated with unobservable modes.
The canonical deterministic behavior quotient survives exact clone
duplication in the tested construction, but the general linear invariant
should use minimal/Hankel rank.

### Rival F — finality substitution

Behavioral factorization proves neither honest intersection nor irreversible
public action. `HC-DU-035A` remains a necessary type correction: prediction,
finality, and capability are separate.

## 9. Resource ledger

Even the finite test spends:

- intervention depth \(|w|\);
- state re-preparation count;
- readout resolution and statistical repetitions;
- controller memory for the word or adaptive tree;
- latency and coherence time across the sequence;
- implementation work for each instrument;
- authenticated provenance if histories can be spoofed;
- model-description complexity; and
- computational cost for closure or linear-basis construction.

For deterministic finite machines, partition refinement is finite and
mechanical. For rational linear models, basis growth is polynomial in the
supplied dimension and action count, while naive word enumeration is
exponential. In a physical noisy fixture, sample complexity depends on the
actual readout gap; no sample bound was earned in this swing.

## 10. Novelty collision and publication prospect

The component mathematics is known terrain.

- Moore/Nerode-style state distinguishability and partition refinement are
  classical automata theory.
- Tzeng’s primary probabilistic-automata result gives a polynomial-time
  linear-algebraic equivalence algorithm:
  [A Polynomial-Time Algorithm for the Equivalence of Probabilistic Automata](https://doi.org/10.1137/0221017).
- Multi-time quantum processes and their dependence on the admitted
  instruments are already formalized by the process-tensor program:
  [Non-Markovian quantum processes: complete framework and efficient characterisation](https://arxiv.org/abs/1512.00589)
  and
  [Quantum Markov Order](https://arxiv.org/abs/1805.11341).

Therefore:

```text
finite closure theorem                         KNOWN / SPECIALIZATION
reachable-rank witness bound                  KNOWN LINEAR-ALGEBRA TERRAIN
three-state and tight-chain fixtures          EXACT CONTROLS
CCR factorization-or-remainder interpretation USEFUL PROGRAM SYNTHESIS
novel physical/cross-platform law             NOT YET EARNED
```

The publishable opening is narrower and harder:

> Begin with a physically formed, independently selected certified record;
> use one unchanged intervention-closure object on a quantum multi-time
> process and an adversarial distributed history; derive a minimal witness
> rank and an operational gap or resource bound; and show that the omitted
> distinction changes a frozen bounded-risk capability.

That conjunction is not established by the prior art located here. Its
novelty remains search-incomplete.

## 11. Kill conditions

Stop this route as a flagship if any of these occurs:

1. every interesting physical candidate requires unbounded or
   experiment-dependent realization rank, so the finite witness bound has no
   predictive force;
2. the intervention alphabet needed to reveal the remainder is fitted after
   looking at each model;
3. the readout gap vanishes faster than available experimental resources can
   resolve it;
4. the quantum and distributed examples require different definitions of
   record equivalence, intervention, or factorization;
5. physical record selection remains absent and the work becomes repeated
   minimization of supplied automata;
6. the only output is Tzeng/Moore/process-tensor prior art in CCR vocabulary;
7. a strong conventional physical completion factors every proposed witness
   with fewer assumptions and equal resources; or
8. the purported capability change disappears after readout, verification,
   rollback, and action costs.

# Required ending ledgers

## Exact result and grade

**Exact result.** For a frozen finite deterministic process, the iterative
relation

\[
E_{k+1}=E_k\cap\bigcap_aT_a^{-1}(E_k),
\qquad
E_0=\ker R\cap\ker Y,
\]

stabilizes at the greatest transition congruence \(E_*\) contained in the
supplied record/readout equivalence. The record quotient is sufficient
exactly when \(E_*=\ker R\). Otherwise a same-record pair has a separating
word of length at most \(n-b_0\), and this bound is tight. In a supplied
\(d\)-dimensional linear realization, any detectable distinction has a word
of length at most reachable distinction rank minus one.

The executable result is `9/9`; it exhausts `67,332` unary machines and
`5,898` two-action machines in the declared size ranges, proves the smallest
delayed fixture has three states, and realizes the tight family through eight
states.

**Grade.**

```text
EXACT FINITE DETERMINISTIC THEOREM
EXACT FINITE LINEAR-REALIZATION BOUND
KNOWN AUTOMATA / LINEAR-EQUIVALENCE MATHEMATICS
USEFUL HC-DU-036 SCOPED ADVANCE
PHYSICAL RECORD SELECTION AND INTERVENTION COMPLETENESS OPEN
CROSS-PLATFORM NOVELTY AND ONTOLOGY OPEN
NO CLAIM BANKED OR SEEDED
```

## What failed or is no longer worth time

- Treating same endpoint, current record, or static quotient as process
  sufficiency.
- Enumerating more bare record partitions without closing them under
  interventions.
- Adopting the target-derived stable quotient as though it were a physically
  selected record.
- Looking for another universal scalar threshold across reconstruction,
  finality, and capability.
- Calling a hidden scheduler gauge because it fits every finite trace.
- Repeating supplied finite-automaton minimization without a physical
  formation law, operational gap, or cross-platform transfer.
- Beginning geometry, GU, or cosmology recovery before the factorization
  question has a physical fixture.

## Newly visible hypotheses, theorems, and conjectures, ranked

1. **Certified Interventional Closure Theorem.** For a physically selected
   certified-record instrument and a frozen finite process class, either its
   record kernel is an intervention congruence or the closure algorithm
   returns a shortest operational remainder witness. The deterministic core
   is exact here; physical formation and noisy instruments remain.
2. **Minimal-Hankel Remainder Conjecture.** The representation-independent
   complexity of a finite physical remainder is the Hankel rank of its
   intervention/readout difference series, and the shortest witness is
   bounded by that minimal behavioral rank rather than raw hidden dimension.
3. **Cross-Platform Remainder-Rank Invariance.** One typed remainder series
   and minimal-rank notion survives without refitting between a quantum
   process tensor and an adversarial DAG/database history.
4. **Capability-Separating Witness Theorem.** A record refinement strictly
   enlarges a frozen bounded-risk action set exactly when its shortest
   witness produces a decision-relevant gap exceeding verification and
   action cost.
5. **Formation-to-Closure Resource Law.** Creating a physical record quotient
   whose kernel is stable under a larger intervention algebra requires added
   support, disturbance, authentication, memory, or loss of coherent
   optionality unless the remainder is explicitly exported.
6. **Scheduler Congruence Criterion.** A global update scheduler is gauge
   exactly when scheduler relabeling lies inside the stable intervention
   congruence of all accessible records and capabilities.
7. **Meta-Record Geometry Reopener.** Only provenance distinctions that
   survive interventional closure should enter geometry reconstruction;
   closure-unstable acquisition graphs are coordinate artifacts or incomplete
   state descriptions.

## Next decisive test

Build one `HC-DU-036A` assay with the **same** typed mathematics on two unlike
fixtures.

1. **Quantum fixture:** use the existing finite Clock-QCA pointer/archive
   system. Freeze its supplied archive record, then admit carrier reunion,
   coherent recoupling, archive readout, and one phase-sensitive effect. Form
   the exact density-operator difference series and compute the shortest
   word, readout gap, and minimal linear rank.
2. **Distributed fixture:** construct two DAG/database states with the same
   declared endpoint record but different authenticated lock/provenance
   histories. Freeze view-change, replay, query, and irreversible-action
   operations. Compute the same closure, shortest word, gap, and capability
   change.

Advance only if record, intervention word, effect, factorization, and rank
retain one definition across both. Kill the cross-platform claim if either
fixture needs a semantic refit. Even a negative result is valuable: it will
locate whether the irreducible remainder is coherence, provenance,
authentication, or an incomplete record interface.

## Short divergent wish list

- A symbolic shortest-witness compiler for rational classical and quantum
  instruments.
- An approximate closure theory with a physically calibrated probability or
  diamond-norm gap.
- A minimal-Hankel-rank proof or counterexample for noncommuting intervention
  alphabets.
- A process-tensor bond-dimension version of the witness bound.
- A cryptographic provenance channel whose forged and honest histories share
  endpoints but differ under one frozen challenge.
- A scheduler-gauge benchmark compiled directly into the same closure engine.
- A resource-weighted witness objective: maximize decision gap per coherence
  time, intervention depth, energy, and verification cost.
- A non-fitted intervention basis selected by locality or an autonomous
  source/archive coupling.
- An experiment in which the shortest witness is not merely detectable but
  changes an irreversible public action.
- A theorem classifying when closure adds a physical state distinction versus
  merely exposing an omitted observer boundary.

## Plain-English interpretation

A snapshot can lie by omission.

Two worlds can show an observer the same record right now and still respond
differently when the observer performs a sequence of allowed operations. In a
finite model, we can now determine this exactly. Either the record remains
complete under every allowed operation, or there is a bounded experiment that
reveals what it left out.

The smallest genuinely delayed example needs only three states. More
generally, the number of intervention steps needed is controlled by how many
distinct hidden responses the operations can generate—not by how persuasive
the current record looks.

This does not prove that records are fundamental. It gives us a way to stop
arguing about that abstractly. Give the theory a physically formed record and
a real set of interventions; the machinery will either show that the future
really factors through the record or hand us a concrete piece of physics that
does not.
