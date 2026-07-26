---
title: "Stabilizer syndrome records: operational duality and the protected logical remainder"
status: completed_scoped_result
doc_type: exploration_synthesis
created: 2026-07-26
authority: "Joe direct chat: execute the next North-Star swing after the material gauge-boundary result"
hypothesis_id: HC-DU-040E
claim_grade: "EXACT FINITE STABILIZER-SYNDROME OPERATIONAL-DUALITY AND LOGICAL-REMAINDER CLASSIFICATION / KNOWN STABILIZER-QEC, KNILL-LAFLAMME, OPERATOR-QEC, AND HOMOLOGICAL-CODE MATHEMATICS / NO NEW QEC THEOREM, UNIVERSAL RECORD SELECTOR, IRREDUCIBLE ONTOLOGICAL REMAINDER, NEW PHYSICS, HARDWARE RESULT, OR PAPER PROMOTION"
---

# Stabilizer syndrome records and the logical remainder

## Result in plain English

A complete quantum-error-correction syndrome can be a genuine, physically
formed, target-independent record and still omit something physically real.

That is not necessarily a defect. It is the point of the code.

The syndrome is exactly complete for one job: identify the error sector needed
by a declared correctable error class and decoder. It is exactly incomplete
for a richer job: determine which protected logical operation occurred. Two
physical error histories can produce the same result on every stabilizer
check, every repeated check, and every check archive while differing by a
logical operation that a later encoded experiment detects with certainty.

The exact residual is not vague “hidden information.” For an
\([[n,k]]\) stabilizer code it is

\[
N(S)/S,
\]

the logical Pauli group, with binary symplectic dimension \(2k\).

This gives Dynamic Unity its strongest current example of the three-way
North-Star structure inside one standard physical architecture:

```text
complete syndrome record
    -> exact operational duality for the correctable action class
    -> protected logical remainder for the full encoded action class
    -> contract retyping if a logical measurement is added to close it.
```

The result does not show that records are secondary to physics in every
description. It shows something narrower and more useful: **record
completeness is capability-relative, and preserving a quantum capability can
require a principled remainder outside the complete classical record.**

## What is new to this run

The prior Dynamic Unity QEC fixture showed that a noisy pointer became
sufficient after an omitted error syndrome was added. That was a
boundary-expansion absorber.

This run starts after that repair:

- every independent stabilizer check is measured;
- the generator-invariant joint syndrome is present;
- check identity, round, route, ancilla outcome, reset, decoder, correction,
  and archive provenance are retained;
- the error class and future action class are frozen; and
- the held-out target is not used to define the record.

The surviving distinction is therefore not an omitted syndrome. It is the
logical quotient that the syndrome is physically designed not to reveal.

## Frozen physical process

Let \(S\) be an abelian stabilizer subgroup of the \(n\)-qubit Pauli group,
excluding \(-I\), with \(n-k\) independent generators. Its simultaneous
\(+1\) eigenspace is a \(2^k\)-dimensional code space \(\mathcal C\), with
projector \(P_{\mathcal C}\).

The complete process is:

1. prepare an arbitrary state on \(\mathcal C\), possibly entangled with an
   inaccessible reference;
2. apply one Pauli error \(E\) from a frozen finite error class
   \(\mathcal E\);
3. QND-measure a generating family for \(S\) with ancillary pointers;
4. archive the complete stabilizer character and all implementation
   provenance already declared by the process;
5. apply a frozen correction \(C_{\sigma(E)}\) depending only on that
   record; and
6. perform a held-out logical action or observable.

The code, check Hamiltonians/couplings, system--pointer--archive boundary,
error class, decoder, and future action class are supplied physical
structures. The complete joint eigenspace algebra is target-independent and
invariant under changing the independent generator basis. A particular
ancilla circuit or microscopic Hamiltonian is not thereby uniquely selected.
The standard quantum instrument and its classical outcome semantics are also
premises; this theorem does not derive collapse, actualization, or one
fundamental outcome event.

## The strongest admitted record class

Write \(\mathfrak R_{\rm check}\) for every classical record formed by this
complete stabilizer-check process and every target-independent,
code-internal refinement that:

1. preserves arbitrary encoded states and their reference entanglement;
2. preserves the full logical action algebra;
3. retains every selective check route, invalid attempt, reset, controller,
   decoder, and archive field already present; and
4. does not add an external source/controller log or a target-coded logical
   measurement absent from the frozen process.

This is deliberately stronger than one syndrome bit string. It includes
repeated complete checks, alternative independent generator sets, redundant
parity checks, and all already formed check-apparatus provenance.

It is deliberately narrower than “every record one could add to the
universe.” A physical controller that logs which logical operator it applied
is a boundary/resource enlargement. A logical measurement that removes a
conjugate encoded capability changes the future action contract. Those are
legitimate repairs, but they are not evidence that the original check record
was complete.

## Exact theorem

### Stabilizer Record Duality and Logical Remainder Theorem

Let \(\overline{\mathcal P}_n\cong\mathbb F_2^{2n}\) be the \(n\)-qubit
Pauli group modulo phases, and let \(S\subset\overline{\mathcal P}_n\) be an
\((n-k)\)-dimensional stabilizer subspace with \(k>0\).

For \(E\in\overline{\mathcal P}_n\), define its generator-invariant syndrome
as the character

\[
\sigma(E):S\longrightarrow\mathbb F_2,
\qquad
\sigma(E)(s)=\langle E,s\rangle_{\rm sp},
\]

where the value records whether \(E\) commutes or anticommutes with \(s\).
Then:

1. **Exact syndrome quotient**

   \[
   \ker\sigma=S^\perp=N(S),
   \qquad
   \overline{\mathcal P}_n/N(S)\cong S^*
   \cong\mathbb F_2^{n-k}.
   \]

   Thus the complete syndrome exactly reconstructs the Pauli error sector
   modulo the normalizer.

2. **Exact correctability boundary**
   A Pauli error class \(\mathcal E\) is exactly correctable by a
   syndrome-conditioned recovery iff

   \[
   \sigma(E_a)=\sigma(E_b)
   \quad\Longrightarrow\quad
   E_a^\dagger E_b\in S
   \]

   for every \(E_a,E_b\in\mathcal E\), modulo phases.

3. **Protected logical remainder**
   For the unrestricted Pauli completion class, the nontrivial
   same-syndrome ambiguity after stabilizers are quotiented is

   \[
   \ker\sigma/S=N(S)/S,
   \]

   the logical Pauli group. Its binary symplectic dimension is

   \[
   \dim N(S)-\dim S
   =(n+k)-(n-k)=2k.
   \]

4. **No syndrome-only universal correction**
   For any \(E\) and any nontrivial logical Pauli
   \(L\in N(S)\setminus S\), \(E\) and \(EL\) have the same complete syndrome.
   One fixed syndrome decoder applies the same correction to both, so their
   residual logical operations differ by \(L\). It cannot correct both on
   every encoded state.

5. **No preserving classical refinement closes the quotient**
   No refinement in \(\mathfrak R_{\rm check}\) can perfectly distinguish
   \(E\) from \(EL\) while preserving every encoded state, reference
   entanglement, and the full logical action algebra. Otherwise the record
   could condition an inverse and correct the pair \(\{E,EL\}\), contradicting
   the exact correctability condition.

Therefore the same formed record supports:

```text
OPERATIONAL_DUALITY
    relative to a correctable error class and its recovery action;

LOGICAL_PHYSICS_REMAINDER
    relative to the unrestricted Pauli class and full encoded action algebra;

CONTRACT_RETYPING_OR_BOUNDARY_EXPANSION
    when a logical measurement, restricted task, or external source log
    is added to close that remainder.
```

### Proof

The Pauli commutation relation is the nondegenerate symplectic form on
\(\mathbb F_2^{2n}\). The syndrome map is its restriction against \(S\).
An error has zero syndrome exactly when it commutes with every stabilizer, so

\[
\ker\sigma=S^\perp=N(S).
\]

Because the symplectic form is nondegenerate and
\(\dim S=n-k\), \(\sigma\) is onto \(S^*\). The first isomorphism theorem gives
the exact syndrome quotient.

For the correctability statement, the Knill--Laflamme condition for the
Pauli class is

\[
P_{\mathcal C}E_a^\dagger E_bP_{\mathcal C}
=\alpha_{ab}P_{\mathcal C}.
\]

If the two syndromes differ, \(E_a^\dagger E_b\) anticommutes with a
stabilizer and maps the code into an orthogonal syndrome sector, so the
left-hand side is zero. If the syndromes agree,
\(E_a^\dagger E_b\in N(S)\). Its restriction to the code is scalar exactly
when its class lies in \(S\); otherwise it is a nontrivial logical Pauli.
This proves the iff boundary.

Since \(\dim S^\perp=2n-\dim S=n+k\), quotienting \(N(S)\) by \(S\) leaves
dimension \(2k\). If a code-internal classical record distinguished
\(\{E,EL\}\) without disturbing the full logical algebra, its label followed
by the appropriate conditional inverse would be a recovery for that pair.
But \(E^\dagger EL=L\notin S\), so Knill--Laflamme forbids such a recovery.
\(\square\)

## Minimum exact witness

Use the three-qubit repetition code

\[
\mathcal C=\operatorname{span}\{|000\rangle,|111\rangle\},
\qquad
S=\langle Z_1Z_2,\ Z_2Z_3\rangle.
\]

Its logical operators may be chosen as

\[
X_L=X_1X_2X_3,
\qquad
Z_L=Z_1.
\]

Both \(I\) and \(X_L\) commute with both stabilizer generators. Every complete
stabilizer check therefore returns \((+1,+1)\), and every syndrome-only
decoder takes the same action.

On the encoded input \(|0_L\rangle=|000\rangle\):

\[
I|0_L\rangle=|0_L\rangle,
\qquad
X_L|0_L\rangle=|1_L\rangle.
\]

A held-out \(Z_L\) measurement separates the results with total-variation
margin one. Replacing the independent generators with
\(Z_1Z_2,Z_1Z_3\), repeating the checks, or archiving all ideal check ancillas
does not change the verdict.

Adding \(Z_L\) to the record is not harmless completion of the same task. On
an arbitrary state

\[
\alpha|0_L\rangle+\beta|1_L\rangle
\]

it destroys or conditions the conjugate \(X_L\) coherence. It narrows the
logical action class from the full encoded qubit to a commuting classical
subalgebra. A controller log saying “\(X_L\) was applied” would repair the
case without disturbing the state, but it is an external source record absent
from the original process.

The repetition code is only the smallest witness. It is not a full
single-qubit-Pauli code and carries no universal QEC claim.

## Homological lift

The surface/toric-code case makes the remainder geometric without making it
new.

For one Pauli sector, represent an error by a one-chain \(e\). The complete
local syndrome is its boundary:

\[
r(e)=\partial e.
\]

Two errors have the same syndrome exactly when their difference is a cycle.
Stabilizer-equivalent cycles are boundaries of higher cells. The residual is
therefore

\[
\frac{\ker\partial_1}{\operatorname{im}\partial_2}
=H_1,
\]

the homology class carrying the logical operation. A noncontractible closed
loop has zero local syndrome and a nontrivial encoded action.

This is the exact form of “local finality with a higher-layer remainder”:

- every local check can be final and mutually compatible;
- the complete local defect record can be empty;
- the logical sector can still differ; and
- a nonlocal encoded action exposes the difference.

The result is the standard homological structure of topological codes, not a
new physical law.

## The admissible-refinement boundary

The logical remainder survives the declared record class for a principled
reason:

> A classical record that reveals the protected quantum distinction strongly
> enough to correct it would itself be an error-correction resource.

For \(\{E,EL\}\), exact recovery without source side information is forbidden.
The possible repairs are therefore typed:

| Repair | What changed |
|---|---|
| Measure one logical observable | narrows the full logical action algebra and disturbs/conditions its conjugate capability |
| Record the external controller or noise-source label | enlarges the observer boundary, process, and resource ledger |
| Restrict the admitted error class to a correctable set | narrows the completion class |
| Restrict the future task to syndrome-dependent recovery | narrows the capability/target class |
| Add coherent environment access and reverse the joint process | removes the independent classical-final-record premise and expands control |
| Change the code or decoder | retypes the physical interface |

None is illegitimate. None is an ordinary same-process check-record
refinement.

## Exact-sequence synthesis with the gauge-boundary anchor

The material gauge-boundary result and the QEC result share one exact
mathematical form.

Let \(M\) be a finite group of physical history differences, let
\(r:M\to Q\) be a target-independent formed record homomorphism, and let
\(G\subseteq\ker r\) be the subgroup declared physically trivial for the
frozen target/action class. Then

\[
0\longrightarrow \ker r/G
\longrightarrow M/G
\longrightarrow \operatorname{im}r
\longrightarrow0
\]

is exact. The record reconstructs \(\operatorname{im}r\). The surviving
action-relative remainder is \(\ker r/G\). A target \(t\) factors through the
record exactly when

\[
\ker r\subseteq\ker t.
\]

This is established quotient/kernel mathematics and is the group-specialized
form of Dynamic Unity's existing reconstruction criterion.

Its two physical readings are:

| Anchor | Formed record | Scoped duality | Retained remainder |
|---|---|---|---|
| `HC-DU-040D` material gauge boundary | oriented total boundary flux | every boundary-flux action | interior redistribution, crossing history, or microscopic formation when the corresponding action is admitted |
| `HC-DU-040E` stabilizer QEC | complete stabilizer character/syndrome | every correction action in the frozen correctable class | logical Pauli class \(N(S)/S\) for the full encoded action algebra |

The common statement is not that a gauge detector and a quantum code are the
same physical system. It is:

> A physically formed boundary/check record can be exactly complete for an
> upper action quotient while a lower or protected capability-bearing kernel
> remains physically live.

In the gauge case, the first leak is an interior or crossing-sensitive
action. In QEC, it is a logical action. The action class decides whether the
kernel is irrelevant gauge, protected capability, or an exposed remainder.

## Primary-source collision

Every load-bearing mathematical component is established:

| Component | Primary source | Collision |
|---|---|---|
| stabilizer group, syndromes, normalizer, encoded Pauli operations | Daniel Gottesman, [*Stabilizer Codes and Quantum Error Correction*](https://arxiv.org/abs/quant-ph/9705052) | known stabilizer formalism |
| exact recovery condition and syndrome representation | Emanuel Knill and Raymond Laflamme, [*A Theory of Quantum Error-Correcting Codes*](https://arxiv.org/abs/quant-ph/9604034) | known necessary-and-sufficient correctability |
| active correction plus protected/noiseless subsystem structure | David Kribs, Raymond Laflamme, and David Poulin, [*A Unified and Generalized Approach to Quantum Error Correction*](https://arxiv.org/abs/quant-ph/0412076) | known operator-QEC terrain |
| correctable hybrid classical/quantum observable algebras | Cédric Bény, Achim Kempf, and David Kribs, [*Quantum Error Correction of Observables*](https://arxiv.org/abs/0705.1574) | known operator-algebra QEC |
| topological code and anyonic logical structure | Alexei Kitaev, [*Fault-tolerant quantum computation by anyons*](https://arxiv.org/abs/quant-ph/9707021) | known topological-code construction |
| surface-code recovery, homological logical operations, and threshold | Dennis, Kitaev, Landahl, and Preskill, [*Topological quantum memory*](https://arxiv.org/abs/quant-ph/0110143) | known homological and threshold structure |

No new QEC theorem, code, decoder, threshold, or experimental prediction is
claimed. The Dynamic Unity gain is a typed North-Star synthesis:

1. the record is formed and complete rather than deliberately weakened;
2. the exact positive duality and negative remainder branches coexist in one
   process;
3. the reason the remainder survives is preservation of a richer capability,
   not merely missing syndrome bits;
4. every apparent repair is classified as error-class restriction,
   capability restriction, boundary enlargement, source record, coherent
   recoupling, or interface retyping; and
5. the same quotient/kernel statement now links two independently physical
   anchors without semantic refitting.

## What this changes for Dynamic Unity

### 1. A complete record need not be a complete physical state

The syndrome is complete for its declared correction job and incomplete for
the encoded logical job. “Complete” must always name the action class.

### 2. A remainder can be capability-bearing

The logical fibre is not merely inaccessible clutter. It is where the encoded
quantum capability lives. Eliminating it into a classical record can destroy
the very capability the code protects.

### 3. Stronger public finality can coexist with protected private structure

Repeated, archived syndrome checks can harden the public error sector while
leaving the logical state coherent. This gives an exact physical instance of
layered finality without importing a blockchain metaphor.

### 4. Record-first and physics-first descriptions can be dual only at a
declared quotient

At the correction quotient, the syndrome description and physical-error
description are operationally dual. At the full logical action level, they
are not. The ontology question cannot be settled without naming which
capabilities count.

### 5. The strongest current North-Star statement narrows

A universal claim that certified classical records reconstruct every
observer-accessible capability is false in this frozen code class. The
defensible target is:

> Independently formed records reconstruct every capability that factors
> through their physically selected quotient; protected noncommutative
> capability appears as a typed kernel remainder until an additional
> physical interface changes the action or access contract.

This remains class-relative. An external source log can absorb the finite
witness, so it is not an irreducible ontology verdict.

## Disposition and next move

The result is banked as:

```text
CODE_RELATIVE_RECORD_ALGEBRA_SELECTED
    given the supplied stabilizer/check architecture

SCOPED_OPERATIONAL_DUALITY
    for the frozen correctable error and recovery class

FINITE_PROTECTED_LOGICAL_REMAINDER
    for the unrestricted Pauli completion and full logical action class

NO UNIVERSAL INTERFACE SELECTOR
NO IRREDUCIBLE ONTOLOGICAL REMAINDER
NO NEW QEC THEOREM OR PHYSICAL LAW
```

Do not spend another swing proving stabilizer or surface-code variants of the
same quotient. The next high-information physical question is whether a
non-engineered, perturbation-stable many-body phase can independently select
both:

1. a formed classical check/boundary record algebra; and
2. a nontrivial protected quotient that retains a held-out capability,

without the code, region, decoder, and future action class being inserted as
the answer.

A topological phase may supply that arena, but it should advance only if the
selection statement goes beyond the standard fact that a supplied
commuting-projector code has topological logical sectors. Otherwise the QEC
branch stops here and Dynamic Unity returns to a different physical
North-Star arena.

No executable model was admitted. Direct group, recovery, and homology
arguments decide the bounded question at a higher grade than a local
simulation, and no external hardware path is implicated.
