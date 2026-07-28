---
title: "Stabilizer-syndrome formation transfer and channel--state resource non-unification"
status: completed_scoped_cross_arena_transfer
doc_type: formation_profile_transfer_orthogonal_support_theorem_and_recovery_consequence
created: 2026-07-27
claim_id: HC-DU-066
work_id: N7-CCR-P4-STABILIZER-FORMATION-TRANSFER
program_id: CCR-CAPABILITY-RECORD-GALOIS-CLOSURE
run_id: RUN-20260727-221127-stabilizer-formation-transfer
run_plan: "../lab/process/runs/RUN-20260727-221127-stabilizer-formation-transfer/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260727-221127-stabilizer-formation-transfer/run-receipt.md"
authority: "Joe direct chat: Go"
claim_grade: "SCOPED GRADE-4 EXACT CROSS-ARENA FORMATION-CRITERION TRANSFER, RESOURCE LOWER BOUNDS, AND RECORD-ONLY RECOVERY CONSEQUENCE / STABILIZER-QEC, KNILL--LAFLAMME, PERFECT-DISCRIMINATION, QND-MEASUREMENT, AND DIMENSION MATHEMATICS ABSORBED / NO NEW QEC THEOREM, ENDOGENOUS INTERFACE SELECTION, UNIVERSAL RESOURCE LAW, NEW PHYSICS, PREDICTION, PAPER, MODEL, HARDWARE, OR PROVIDER RESULT"
portfolio_return: ORTHOGONAL_OUTPUT_FORMATION_LAW_TRANSFERS_WHILE_NATIVE_RESOURCE_RECEIPTS_DO_NOT
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Stabilizer-syndrome formation transfer and channel--state resource non-unification

## Executive verdict

The `HC-DU-065` formation framework transfers unchanged to stabilizer
quantum error correction, and the transfer exposes an exact physical
non-unification.

The same four alternatives and three one-bit questions form the same
nondistributive \(M_3\) record lattice in both arenas. The exact physical
formation test is also the same:

> A frozen one-occurrence route can form the complete classical record
> exactly iff the alternatives produce pairwise orthogonal accessible output
> supports, and the retained archive has at least one distinguishable value
> per alternative.

What changes is how a physical architecture satisfies that test.

- A single unassisted use of an unknown Pauli channel leaves four candidate
  outputs in one qubit. They cannot all be orthogonal. The complete record
  needs a second use or a pre-existing entangled reference and joint Bell
  readout.
- In the three-qubit repetition code, one bit-flip occurrence places an
  arbitrary encoded state into one of four pairwise orthogonal syndrome
  subspaces. A supplied QND stabilizer instrument can copy that sector label
  to two syndrome bits without reading the protected logical state.

The QEC route is not free. It consumes a three-qubit encoded carrier,
stabilizer structure, check couplings, pointer capacity or repeated readout,
and a two-bit archive. It needs no separate pre-entangled reference, but that
does not make it the same resource as one bare channel use.

The held-out consequence is exact. Under a controller restricted to the
formed record and one Pauli correction, the complete two-bit syndrome
corrects the frozen class \(\{I,X_1,X_2,X_3\}\). Any one syndrome bit leaves
two required corrections confounded and cannot guarantee recovery of every
encoded state.

This is the requested second physical transfer. It does not select the code,
checks, pointer, decoder, archive, or observer, so it does not reopen
`H-CCR-17`.

## 1. Why this is not a repeat of `HC-DU-040E`

`HC-DU-040E` established a different result:

- the complete stabilizer syndrome is sufficient for a declared correctable
  error class;
- a protected logical quotient \(N(S)/S\) survives for the full Pauli class;
  and
- adding a logical measurement or source log changes the capability or
  boundary contract.

It assumed a formed complete syndrome. It did not ask:

1. which physical resources can form the full syndrome rather than one
   check;
2. which formation lower bounds follow before fault/noise analysis;
3. whether the `HC-DU-065` formation profile transfers without changing its
   formal meaning; or
4. why one physical arena forms the four-way top in one occurrence while the
   other cannot.

Those are the present questions.

## 2. Frozen physical and access contract

Use the three-qubit repetition code

\[
\mathcal C
=
\operatorname{span}\{\lvert000\rangle,\lvert111\rangle\},
\qquad
S=\langle g_{12},g_{23}\rangle,
\]

with

\[
g_{12}=Z_1Z_2,
\qquad
g_{23}=Z_2Z_3,
\qquad
g_{13}=g_{12}g_{23}=Z_1Z_3.
\]

Freeze the correctable representative class

\[
X=\{I,X_1,X_2,X_3\}.
\]

Exactly one member of \(X\) describes the admitted error episode. The
logical input is arbitrary and may be entangled with an inaccessible
reference. The syndrome instrument must preserve the logical state.

The observer/controller receives only the declared pointer/archive record.
Afterward it may choose one correction from
\(\{I,X_1,X_2,X_3\}\). It cannot remeasure the code, inspect an environment,
or hide another syndrome extraction inside the recovery map.

The resource ledger keeps separate:

- error occurrences;
- physical data-carrier size and encoded redundancy;
- pre-existing external reference systems and their entanglement;
- pointer count and Hilbert-space dimension;
- check interactions and their locality/arity;
- measurement/readout rounds;
- intermediate export and pointer state management;
- durable value-archive capacity; and
- occurrence, setting, validity, route, and decoder provenance.

The ideal finite theorem does not include device noise or fault tolerance.

## 3. The same semantic \(M_3\) lattice

For \(g\in\{g_{12},g_{23},g_{13}\}\), define

\[
q_g(E)
=
\begin{cases}
0,& Eg=gE,\\
1,& Eg=-gE.
\end{cases}
\]

The four error labels give:

| error | \(q_{12}\) | \(q_{23}\) | \(q_{13}\) |
|---|---:|---:|---:|
| \(I\) | 0 | 0 | 0 |
| \(X_1\) | 1 | 0 | 1 |
| \(X_2\) | 1 | 1 | 0 |
| \(X_3\) | 0 | 1 | 1 |

Therefore

\[
q_{13}=q_{12}\oplus q_{23}.
\]

Each query defines a two-block partition. The three partitions are
incomparable. Any two queries identify the error label and determine the
third. Their closed capability--record lattice is the same \(M_3\) obtained
for the two-bit classical and four-Pauli-channel controls in `HC-DU-064`.

This equality is semantic. It says nothing yet about how the record is
formed.

## 4. Unchanged physical formation criterion

### Theorem 1 — orthogonal-output exact-formation criterion

Fix a finite alternative class \(X\) and one admitted physical route. For
each \(x\in X\), let \(\mathcal K_x\) be the support subspace of every
accessible output state possible under alternative \(x\), including any
retained reference and pointer systems admitted by the route.

There is one exact, nondestructive-to-the-declared-residual classical record
of \(x\) for all admitted source states iff

\[
\mathcal K_x\perp\mathcal K_y
\qquad
(x\ne y),
\]

and the durable value archive has at least \(|X|\) distinguishable states.

For one fixed density operator \(\rho_x\) per alternative, replace
\(\mathcal K_x\) by \(\operatorname{supp}\rho_x\).

### Proof

If an exact measurement has outcome \(x\) with probability one on every
state supported in \(\mathcal K_x\) and probability zero on every other
alternative, positivity of the POVM effects forces the supports assigned to
different certain outcomes to be orthogonal. Conversely, projectors onto
pairwise orthogonal support subspaces distinguish the alternatives exactly.
Copying the result to a classical archive preserves the declared residual
degrees of freedom. A durable classical record of \(|X|\) labels requires at
least \(|X|\) distinguishable archive states. \(\square\)

For an admitted resource budget \(b\), the `HC-DU-065` profile

\[
\mathsf{Form}_{=}(E)
=
\operatorname{Min}
\{b:\exists i\in\mathcal I_b,\ \ker r_i=E\}
\]

therefore asks which budgets make these support and archive conditions true.
The definition and criterion do not change between the channel and QEC
arenas.

## 5. Why one QEC error occurrence is enough

For \(E\in X\), define the conditional error subspace

\[
\mathcal K_E=E\mathcal C.
\]

### Theorem 2 — syndrome-sector orthogonality

The four subspaces

\[
\mathcal C,\quad
X_1\mathcal C,\quad
X_2\mathcal C,\quad
X_3\mathcal C
\]

are pairwise orthogonal and exhaust the eight-dimensional physical Hilbert
space.

### Proof

Distinct representatives in \(X\) have distinct full syndromes. Hence for
each \(E\ne F\), some stabilizer \(g\) commutes with one and anticommutes
with the other. For arbitrary
\(\lvert\psi\rangle,\lvert\phi\rangle\in\mathcal C\),

\[
\langle E\psi\mid F\phi\rangle
=
\langle\psi\mid E^\dagger F\mid\phi\rangle.
\]

Inserting \(g\), which acts as identity on the code while anticommuting with
\(E^\dagger F\), makes this inner product equal to its negative. It is zero.
Each subspace has dimension two, so the four orthogonal subspaces fill
dimension eight. \(\square\)

Let \(\Pi_s\) project onto the four joint syndrome sectors. The ideal
instrument

\[
\{\Pi_s\}_{s\in\mathbb F_2^2}
\]

therefore identifies the error sector exactly while acting as identity on
the unknown logical state inside that sector. Equivalently, a pointer
isometry can satisfy

\[
W\bigl(\lvert\psi\rangle\otimes\lvert0\rangle_P\bigr)
=
\sum_s
\Pi_s\lvert\psi\rangle\otimes\lvert s\rangle_P.
\]

This forms the complete record after one error occurrence.

The one-occurrence statement charges rather than erases the architecture:
the error acts on an already encoded three-qubit carrier with four
orthogonal syndrome sectors. The measurement interaction can transiently
entangle data and pointer, but it does not require a separately supplied
pre-entangled reference pair.

## 6. Exact pointer and archive boundaries

### Corollary 1 — one terminal binary pointer is insufficient

If the pointer is the only accessible output, is read only once at the end,
and has Hilbert-space dimension two, it cannot encode four exact syndrome
labels. Four certain measurement outcomes require four orthogonal
conditional pointer supports.

More generally, for readout alphabets of sizes \(d_1,\ldots,d_m\), the
retained transcript must satisfy

\[
\prod_{j=1}^m d_j\ge4.
\]

Thus one four-outcome readout or at least two binary readouts are required.
Every exact value archive has the same lower bound:

\[
|R|\ge4,
\qquad
\log_2|R|\ge2.
\]

### Three exact ideal formation routes

| route | error occurrences | encoded carrier | pointer | readable rounds | intermediate retention | interaction burden | value archive |
|---|---:|---|---|---:|---|---|---:|
| parallel checks | 1 | 3 data qubits | 2 binary ancillas | 1 terminal round | none | separate parity-extraction couplings for \(g_{12},g_{23}\) | 4 states / 2 bits |
| sequential reuse | 1 | 3 data qubits | 1 binary ancilla | 2 | first result retained; pointer reset/reprepared or its known state tracked | sequential parity extraction | 4 states / 2 bits |
| joint-sector pointer | 1 | 3 data qubits | 1 four-level pointer | 1 terminal round | none | supplied joint coupling to the four \(\Pi_s\) sectors | 4 states / 2 bits |

These are exact representative receipts under the frozen ideal route menu,
not an exhaustive fault-tolerant circuit frontier. The dimension/transcript
and archive bounds are exhaustive for the declared output interface.

No route dominates the others without exchange rates among pointer count,
pointer dimension, readout latency, intermediate export, interaction
locality, and state-management burden. The formation profile remains Pareto,
not naturally scalar.

## 7. Held-out recovery consequence

Let a record-only decoder choose

\[
D:R\longrightarrow\{I,X_1,X_2,X_3\}
\]

and apply \(D(r)\) as its only recovery action.

### Theorem 3 — the complete syndrome is necessary and sufficient

The full two-bit syndrome guarantees exact recovery of every error in \(X\)
on every encoded input. No one atomic record
\(q_{12},q_{23}\), or \(q_{13}\) does.

### Proof

The full syndrome is injective on \(X\), so choose \(D(\sigma(E))=E\).
Each Pauli is its own inverse up to phase.

For any one atomic query, two distinct errors \(E,F\in X\) share the same
record while having different full syndromes. If one correction \(C\)
recovered both on every encoded state, then both \(CE\) and \(CF\) would act
as stabilizers on the code. This would imply

\[
E^\dagger F\in S.
\]

But stabilizer-equivalent errors have the same full syndrome, contrary to
the choice of \(E,F\). Hence at least one member of the pair fails exact
recovery. \(\square\)

A more powerful recovery channel could internally measure the omitted
syndrome. Under this contract that is not a counterexample: it has added the
missing physical record interface or coherent control access and must carry
its own receipt.

## 8. Exact comparison with the Pauli-channel arena

| feature | one-use Pauli-channel specimen | repetition-code syndrome specimen |
|---|---|---|
| semantic alternatives | four Pauli labels | \(I,X_1,X_2,X_3\) |
| closed record lattice | \(M_3\) | \(M_3\) |
| one-occurrence accessible supports without extra route | four nonzero states in dimension 2; not all orthogonal | four dimension-2 syndrome subspaces in dimension 8; pairwise orthogonal |
| exact top route | two channel uses, or one use plus maximally entangled reference and Bell readout | one error occurrence plus encoded carrier and complete QND syndrome extraction |
| external reference entanglement | necessary on the one-use route | not necessary |
| charged native resource | repeated process access or entangled reference plus joint analyzer | code redundancy plus stabilizer/check/pointer architecture |
| held-out consequence | exact channel-label reconstruction | exact record-only recovery on the frozen class |

The unchanged law is support orthogonality plus archive capacity. The physical
resources that make the law true are different.

This is the first exact non-unification:

```text
same semantic M3
    + same exact-formation criterion
    != same physical carrier
    != same resource receipt
    != same native mechanism.
```

Calling both systems “two-bit finality” would discard the main physical
information. Calling the encoded carrier free would make the QEC route look
artificially cheaper. Calling one error occurrence one channel use would
collapse a persistent state architecture into a process-query architecture.

## 9. Relation to distributed records and layered finality

The syndrome is a clean physical example of layered finality:

1. commuting checks produce two classical bits;
2. those bits can be exported, copied, reconciled, and used by a classical
   controller;
3. they are complete for the frozen correction action; and
4. they deliberately leave the encoded logical state unmeasured.

The upper syndrome layer therefore behaves like a classical fault
certificate while the lower protected layer remains quantum. The classical
record lattice and a distributed two-bit record can share partition
mathematics. They do not thereby share a physical consensus protocol,
measurement mechanism, validator set, or resource law.

The useful bridge is typed:

\[
\text{physical alternatives}
\to
\text{orthogonal accessible sectors}
\to
\text{formed classical syndrome}
\to
\text{record-only recovery capability}.
\]

Every arrow remains an explicit physical or operational map.

## 10. Literature collision

All component mathematics and architectures are established:

- Gottesman's stabilizer formalism supplies commuting checks, syndrome
  sectors, normalizers, and encoded operations
  ([*Stabilizer Codes and Quantum Error Correction*](https://arxiv.org/abs/quant-ph/9705052)).
- Knill and Laflamme give the necessary and sufficient perfect-recovery
  conditions and the syndrome representation
  ([*A Theory of Quantum Error-Correcting Codes*](https://arxiv.org/abs/quant-ph/9604034)).
- Standard ancilla-based stabilizer extraction makes the pointer and circuit
  overhead physical rather than semantic; single-ancilla and two-ancilla
  repetition-code routes are explicit in
  [Antipov, Kiktenko, and Fedorov](https://arxiv.org/abs/2207.13356).
- `HC-DU-033E/038E` supplies the Admissible Record Envelope;
  `HC-DU-040E` supplies the syndrome/logical-remainder boundary; and
  `HC-DU-064/065` supplies the closure lattice and formation profile.

Perfect distinguishability by orthogonal supports and the output-dimension
bound are standard finite-dimensional quantum mechanics and are proved
directly above. No new code, decoder, syndrome circuit, threshold, state-
discrimination theorem, or QEC prediction is claimed.

The scoped Dynamic Unity addition is the unchanged cross-arena composition:

\[
\text{capability--record closure}
\quad+\quad
\text{orthogonal-output formation law}
\quad+\quad
\text{native resource receipt}
\quad+\quad
\text{held-out capability consequence}.
\]

## 11. What Dynamic Unity earns

### Earned

- The `HC-DU-065` formation definition and orthogonal-output criterion
  transfer unchanged to a second serious physical arena.
- The repetition-code checks realize the same \(M_3\) semantic lattice.
- One error occurrence produces four pairwise orthogonal syndrome sectors.
- One terminal binary pointer cannot form the top; two binary readouts or
  one four-outcome readout and a four-state archive are exact minima.
- Parallel, sequential, and joint-sector routes expose a resource antichain
  rather than one natural cost.
- Full syndrome is necessary and sufficient for the frozen record-only
  recovery action; every atom fails.
- Pauli-channel and QEC formation satisfy the same law using different native
  resources.

### Not earned

- no new QEC, state-discrimination, or channel-discrimination theorem;
- no fault-tolerance, noisy-device, threshold, or hardware result;
- no natural law selecting the repetition code, stabilizers, check
  Hamiltonians, pointer architecture, decoder, archive, or observer;
- no universal exchange rate among uses, redundancy, entanglement, pointer
  capacity, locality, latency, or memory;
- no shared physical mechanism with distributed consensus;
- no new physics, prediction, paper, ontology, or reopener of `H-CCR-17`.

### Stop

Do not:

- infer physical formation from the common \(M_3\) lattice;
- equate one error occurrence with one bare channel use;
- omit the encoded carrier and check apparatus from the resource receipt;
- treat transient measurement entanglement as a free pre-existing reference;
- call syndrome finality completeness for the protected logical algebra; or
- repeat the result on more stabilizer codes without a new selection or
  quantitative invariant.

### Reopener

Reopen only for:

1. dynamics that select the code/check/pointer/archive interface from a
   stronger physical antecedent; or
2. a quantitative cross-arena relation beyond ordinary orthogonal-support
   discrimination that predicts a held-out response without fitting a
   resource exchange law.

## 12. Portfolio return

```text
HC-DU-066: complete
SECOND_PHYSICAL_ARENA: three-qubit repetition-code syndrome
SEMANTIC_LATTICE: M3 transfers unchanged
FORMATION_CRITERION: pairwise orthogonal accessible supports + archive floor
QEC_TOP: one error occurrence + encoded carrier + complete syndrome interface
ONE_BINARY_TERMINAL_POINTER: impossible
MINIMUM_TRANSCRIPT: two binary outcomes or one four-outcome readout
HELD_OUT_ACTION: exact record-only recovery
NATIVE_RESOURCE_UNIFICATION: false
ENDOGENOUS_INTERFACE_SELECTION: open
H-CCR-17: not reopened
LOCAL_MODEL: not warranted
EXTERNAL_HARDWARE: irrelevant
NEXT_SCIENTIFIC_ACTION: unselected
```
