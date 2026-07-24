---
title: "A covariant finite pointer, archive evidence conservation, and the boundary-relocation obstruction"
status: completed_research_swing
doc_type: technical_research_note_spine
created: 2026-07-24
hardening_id: HC-DU-031C
contract: explorations/covariant-archive-boundary-swing-contract-2026-07-24.md
predecessor: explorations/covariant-recorder-naturalization-swing-2026-07-24.md
primary_source: "Arrighi, Facchini, and Forets, arXiv:1404.4499"
terminal_outcomes:
  - COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY
  - INTERFACE_ONLY_ARCHIVE
claim_grade: "EXACT FINITE MATHEMATICAL CONSTRUCTION AND SCOPED OBSTRUCTION / PHYSICAL INTERFACE AND LAW SELECTION OPEN"
novelty: SEARCH-INCOMPLETE
banked: false
seeded: false
---

# A covariant finite pointer, archive evidence conservation, and the boundary-relocation obstruction

## Abstract

We replace the orthogonal one-step write in the covariant Clock-QCA counter
with a tunable finite pointer interaction. A source-effective event rotates a
particle-carried qubit by `R_theta`; encoding-added `q` crossings transport it
unchanged. The resulting complete local unitary inherits the exact
Arrighi-Facchini-Forets rectangular-patch covariance square. A one-gate
Clock-QCA witness realizes two coherent histories whose pointer-state overlap
is

```text
gamma = cos(theta).
```

Tracing the pointer multiplies the source history coherence by `gamma`.
Under one fixed reunion recombiner, the source visibility `V` and optimal
pure-record distinguishability `D` obey

```text
V = |gamma|,
D = sqrt(1-|gamma|^2),
V^2 + D^2 = 1.
```

This calibrated relation is known complementarity structure, not a novelty
claim. The new work is to use it to distinguish operations often collapsed
into the word “archive.”

Any history-independent unitary acting on a record and a blank archive
preserves the conditional states' joint overlap and therefore their joint
trace distance. Partial trace cannot increase either carrier's marginal
distinguishability. Such an interface can transfer or repartition existing
evidence, but cannot manufacture it.

For the frozen pointer-basis CNOT:

```text
D_joint = sin(theta)
D_archive after pointer loss = sin^2(theta) = D_joint^2.
```

Only the orthogonal `theta=pi/2` endpoint exports a perfect loss-surviving
bit. A SWAP instead transfers the full nonorthogonal record,
`D_archive=sin(theta)`, but leaves no retained pointer copy. Repeated CNOT
fanout creates a GHZ-like redundant basis predicate and does not improve the
archive-only distinguishability after pointer loss. Independent fresh record
interactions do improve it:

```text
V_m = |gamma|^m,
D_m = sqrt(1-|gamma|^(2m)),
archive dimension = 2^m.
```

Finally, boundary relocation is graded rather than invariant without
qualification. Internalizing an archive can preserve a declared
history-diagonal observable algebra. It does not preserve the full coherent
source channel when the archive is informative, and it does not preserve the
interventional theory when operations on the relocated archive can affect a
later recoupling. The executable receipt passes `31/31` checks.

The result constructs a finite covariant coherent record and a declared
archive interface. It does not construct classical irreversibility, select
the interface or record law, simulate a spatial reunion, derive proper time,
or establish a Dynamic Unity law.

## 1. Source antecedent and exact boundary

The host is the `1+1` Clock QCA in:

- [P. Arrighi, S. Facchini, and M. Forets, *Discrete Lorentz covariance for
  Quantum Walks and Quantum Cellular Automata*](https://arxiv.org/abs/1404.4499).

The source wire space is

```text
H_0 = span{|q>, |0>, |1>}.
```

Its complete local scattering:

- swaps `q` transparently past `0` or `1`;
- fixes `q/q`, `0/0`, and `1/1`; and
- applies a declared `2 x 2` unitary coin `C` on
  `span{|1,0>, |0,1>}`.

The canonical encoding is

```text
E_n |x> = |x>|q>^(n-1).
```

In the source rectangular patch, the two active strands meet exactly once.
Every other gate only transports an active symbol through `q`. This proves
the source-sense circuit covariance square.

The primary source TeX and PDF pins carried forward from `HC-DU-031B` are:

```text
121ccb1e66c5e408c4a659c66a9873e8d0544655e0a28ccd920e3f407ed1fdfb  source TeX
578c156f25fb9b2698bca5f6f27d43e7e1c09ee884a64f78e9f1e2515b0cebc4  source PDF
```

Nothing below upgrades this discrete `1+1` circuit statement to continuum,
higher-dimensional, empirical, or gravitational Lorentz invariance.

## 2. Why the tunable pointer replaces the orthogonal counter in this assay

`HC-DU-031B` carried an orthogonal modulo-`R` label `k`. If that label were
retained beside the new pointer, the zero-event and one-event histories would
already have orthogonal `k=0` and `k=1` records. Their distinguishability
would be one for every `theta`, making the partial information/interference
assay trivial.

This swing therefore uses a softened one-event recorder family:

```text
theta=0       recorder off
0<theta<pi/2 partial coherent record
theta=pi/2    orthogonal one-event write
```

It is not claimed to be a faithful elapsed counter under unlimited reuse.
Repeated `R_theta` updates are tested as a finite-recurrence control. The
orthogonal modulo counter remains the separate `HC-DU-031B` construction.

## 3. Complete local pointer extension

Replace the particle by two internal species:

```text
H_A = span{|q>, |0>, |1,A=0>, |1,A=1>}.
```

Let

```text
R_theta =
[[ cos(theta), -sin(theta)],
 [ sin(theta),  cos(theta)]].
```

At a particle/zero scattering, the source coin acts on the two path
possibilities and `R_theta` acts on the pointer. At a particle/`q` crossing,
the pointer is transported unchanged. Particle/particle lines remain fixed.

### Theorem 1 — complete unitarity

**Statement.** The frozen pointer scattering is unitary on
`H_A tensor H_A` for every real `theta` and every unitary source coin `C`.

**Proof.** Decompose the complete two-wire space into the mutually orthogonal
`q/q`, one-`q`, and no-`q` sectors. The `q/q` line is fixed. The two one-`q`
sectors are swapped, preserving the pointer.

In the no-`q` sector, `|0,0>` and all particle/particle lines are fixed. The
remaining four-dimensional particle/zero sector factors into path and pointer
degrees. Its restriction is the tensor product, up to basis ordering, of the
unitary source path block `C^T` and the unitary pointer rotation `R_theta`.
The orthogonal direct sum of these unitary restrictions is unitary. `QED`

The executable checks eight complete `16 x 16` matrices: four pointer angles
and two nontrivial complex source coins.

### Theorem 2 — exact source-sense covariance

**Statement.** The pointer extension inherits the canonical
Arrighi-Facchini-Forets rectangular-patch covariance square for every real
`theta`.

**Proof.** The extension is a `q`-transparent lift. In an encoded rectangular
patch, the two non-`q` strands meet exactly once, so the complete active block
acts exactly once. All other crossings transport the active state through
`q` without changing the pointer. The patch output therefore equals the
encoded direct-gate output on every basis input and hence every
superposition. `QED`

The receipt checks:

| Coverage | Cases | Maximum defect |
|---|---:|---:|
| canonical patches across four angles | 192 | `0` |
| all placements, patches `1..4 x 1..4` | 3,200 | `0` |
| held-out all-placement `6 x 5` patch | 480 | `0` |

The all-placement rows are local-square robustness tests. Only the canonical
placement rule, whose encodings obey the required composition law, is claimed
as the full transform family.

A locally unitary rival that also rotates the pointer at `q` crossings fails
the `3 x 4` refinement test with maximum amplitude defect
`1.7320508075688772`. The failure is refinement sensitivity, not malformed
local dynamics.

### Covariance remains admission, not selection

The same proof works for every unitary active block `W` on
`K tensor K` when

```text
H = C|q> direct-sum K
```

and `q` crossings are transparent. The executable's unrelated dense `9 x 9`
Fourier active block passes all `320` cases of a held-out `5 x 4` patch.

Thus covariance admits the pointer family but does not select:

- `theta`;
- the pointer basis;
- the archive boundary;
- CNOT rather than SWAP or another coupling;
- fresh archive cells; or
- a classicalization law.

## 4. The two-history Clock-QCA witness

Inside one actual extended Clock-QCA scattering, initialize the pointer at
zero and superpose:

```text
|h_0> = |1,A=0; q>   (no source-effective event)
|h_1> = |1,A=0; 0>   (one source-effective event).
```

Their source outputs are orthogonal. The extension gives

```text
|h_0>|0_A> -> |s_0>|a_0>
|h_1>|0_A> -> |s_1>|a_1>

|a_0> = |0>
|a_1> = cos(theta)|0> + sin(theta)|1>.
```

The executable factorization defect is exactly zero. At the primary
`theta=pi/3` setting, source-history populations remain
`0.5, 0.5`, normalized coherence visibility is `0.5`, and trace distance
from the unrecorded pure source output is `0.25`.

## 5. Gram reduction and exact complementarity

Let `{P_h}` be mutually orthogonal history projectors and let

```text
W = sum_h U P_h tensor |a_h>
```

be the record isometry. For any source state `rho`,

```text
Tr_A[W rho W*]
  = sum_(h,k) U P_h rho P_k U* <a_k|a_h>.
```

### Theorem 3 — Gram-matrix reduction

**Statement.** Physical archive discard multiplies every history block
`P_h rho P_k` by the corresponding archive Gram entry
`G_hk=<a_k|a_h>`.

**Proof.** Expand `W rho W*` in the history indices and use
`Tr(|a_h><a_k|)=<a_k|a_h>`. `QED`

This makes source decoherence and archive evidence two views of the same
coupling.

For equal history amplitudes and the two pure record states above:

```text
gamma = <a_0|a_1> = cos(theta)
V = |gamma|
D = (1/2)|| |a_0><a_0| - |a_1><a_1| ||_1
  = sqrt(1-|gamma|^2).
```

Therefore:

```text
V^2 + D^2 = 1.
```

The equal-prior optimal discrimination success is

```text
P_success = (1+D)/2.
```

The receipt obtains `V` both from the reduced matrix and from one fixed
recombiner with phases `0` and `pi`; it obtains `D` from the trace norm,
not by substituting the analytic formula.

| Setting | `V` | `D` | `P_success` |
|---|---:|---:|---:|
| `theta=0` | `1` | `0` | `0.5` |
| `theta=pi/6` | `0.8660254` | `0.5` | `0.75` |
| `theta=pi/3` | `0.5` | `0.8660254` | `0.9330127` |
| `theta=pi/2` | `0` | `1` | `1` |

The complementarity relation is established prior structure; the primary
comparator is [B.-G. Englert, *Fringe Visibility and Which-Way Information:
An Inequality*](https://doi.org/10.1103/PhysRevLett.77.2154).

## 6. Archive interfaces conserve joint evidence

The archive starts in one fixed blank state `|0_E>`. Let `J` be any
history-independent unitary on pointer plus archive and define

```text
|r_h> = J(|a_h>|0_E>).
```

### Theorem 4 — unitary archive evidence conservation

**Statement.**

1. `J` preserves every conditional-state overlap:

   ```text
   <r_k|r_h> = <a_k|a_h>.
   ```

2. It therefore preserves the joint pure-state trace distance.
3. Partial trace cannot increase the distinguishability available from either
   subsystem alone.

**Proof.** Part 1 is invariance of inner products under a unitary. Pure-state
trace distance is a function only of overlap, proving Part 2. Partial trace is
a quantum channel, and trace distance is contractive under quantum channels,
proving Part 3. `QED`

An archive interface can transfer or repartition existing evidence. It cannot
manufacture more joint history evidence from a blank cell.

This exact statement is compatible with the broader channel
information-disturbance structure of
[Kretschmann, Schlingemann, and Werner](https://arxiv.org/abs/quant-ph/0605009).
The theorem here is the elementary finite pure-state specialization needed by
this construction.

The executable applies a dense `4 x 4` Fourier unitary to the pointer and
blank archive. At `theta=pi/3`, the input and output overlaps agree at `0.5`;
joint `D` remains `0.8660254`; and both marginals satisfy the contraction
bound.

## 7. CNOT redundancy, SWAP transfer, and no broadcasting

### 7.1 Pointer-basis CNOT

At the declared interface, apply CNOT from pointer `A` to blank archive `E`:

```text
|0_A,0_E> -> |0_A,0_E>
|1_A,0_E> -> |1_A,1_E>.
```

The conditional joint records become

```text
|r_0> = |00>
|r_1> = cos(theta)|00> + sin(theta)|11>.
```

Their overlap remains `gamma`, so

```text
D_joint = sin(theta).
```

After the pointer-bearing carrier is lost:

```text
rho_E^0 = |0><0|
rho_E^1 = cos^2(theta)|0><0| + sin^2(theta)|1><1|.
```

Hence:

```text
D_E = sin^2(theta) = D_joint^2.
```

At the primary setting:

```text
D_joint = 0.8660254
D_E     = 0.75.
```

This squared-distinguishability tax is specific to redundant
computational-basis CNOT export in this fixture. It is not a universal limit
on transfer.

Only `theta=pi/2` exports a perfectly distinguishable bit that survives
pointer loss. Before any export, the separate blank archive has `D_E=0`.

### 7.2 Full SWAP transfer

A SWAP gives:

```text
|a_h>_A |0>_E -> |0>_A |a_h>_E.
```

After pointer loss, the archive retains the full

```text
D_E = sin(theta).
```

But the pointer is blank for both histories and retains no copy. At
`theta=pi/3`, the executable obtains

```text
D_E = 0.8660254
D_A = 0.
```

Thus “the record survives carrier loss” is incomplete unless one states
whether the interface duplicated a classical basis predicate, transferred a
quantum state, or created a new independent record.

### 7.3 CNOT does not clone the pointer state

For the coherent input `|+>|0>`, CNOT produces

```text
(|00>+|11>)/sqrt(2),
```

not `|+>|+>`. The target marginal has purity `1/2` and fidelity `1/2` with
`|+>`.

More generally, suppose a unitary duplicated both nonorthogonal conditional
states while retaining perfect copies on both sides. Inner-product
preservation would require

```text
gamma = gamma^2,
```

which is impossible for `0<|gamma|<1`. This is the pure-state endpoint of the
no-broadcasting result of
[Barnum, Caves, Fuchs, Jozsa, and Schumacher](https://arxiv.org/abs/quant-ph/9511010).

The interface can:

- preserve the full evidence jointly;
- move it to another carrier;
- divide its accessibility across correlated shares; or
- copy an orthogonal basis predicate.

It cannot give both subsystems the full nonorthogonal record while leaving
the original intact.

## 8. Repeated fanout is not independent recording

Fan out the same pointer basis to `m` blank archive cells by repeated CNOT.
The one-event record is

```text
cos(theta)|0_A 0...0_E> + sin(theta)|1_A 1...1_E>.
```

For every `m`:

```text
joint overlap = cos(theta)
joint D = sin(theta)
archive-only D after pointer loss = sin^2(theta).
```

The executable checks `m=1,2,3,4`. At `theta=pi/3`, archive dimensions
`2,4,8,16` all leave archive-only `D=0.75`. More blank cells add basis
redundancy but do not turn one weak coherent record into `m` independent weak
records.

This matters for any environmental-record claim. Redundancy, independent
evidence accumulation, and mere growth of Hilbert dimension are different
resources. Zurek's environmental-record program is relevant context:
[W. H. Zurek, *Quantum Darwinism*](https://arxiv.org/abs/0903.5082). It does
not establish that this finite CNOT fanout yields classical objectivity.

## 9. Fresh independent cells and finite recurrence

If the history independently controls `m` fresh cells, their conditional
states are

```text
|0>^tensor m
and
|a_1>^tensor m.
```

Therefore:

```text
gamma_m = gamma^m
V_m = |gamma|^m
D_m = sqrt(1-|gamma|^(2m)).
```

For `theta=pi/3`:

| Fresh cells | Dimension | `V_m` | `D_m` |
|---:|---:|---:|---:|
| 1 | 2 | `0.5` | `0.8660254` |
| 2 | 4 | `0.25` | `0.9682458` |
| 3 | 8 | `0.125` | `0.9921567` |
| 4 | 16 | `0.0625` | `0.9980450` |
| 5 | 32 | `0.03125` | `0.9995116` |
| 6 | 64 | `0.015625` | `0.9998779` |

The gain is real, but each cell is a new interaction and the full archive
dimension is explicitly `2^m`.

By contrast, repeatedly applying `R_(pi/3)` to one reused pointer produces
blank-ray visibility

```text
1, 1/2, 1/2, 1, 1/2, 1/2, 1, ...
```

The record ray recurs after three events. A two-state orthogonal toggle
similarly aliases after two writes, up to global phase.

Finite reversible reuse is not monotone classical accumulation. A monotone
record requires fresh support, a bath or limit, coarse graining,
measurement, dissipation, or another explicitly charged irreversible
ingredient.

## 10. Boundary relocation and informative-record obstruction

An external source/archive model can always be rewritten as an enlarged
internal-state model by including the source or archive state in the host.
That state augmentation is bookkeeping. The substantive question is what
contract remains invariant.

### Theorem 5 — graded boundary relocation

For the record isometry

```text
W = sum_h U P_h tensor |a_h>,
```

three equivalence grades differ.

#### 1. History-diagonal observational equivalence

If the declared source observable algebra contains no cross-history
coherences and the archive is not intervened on, relocation preserves its
expectations. The record channel changes only off-diagonal history blocks.

The executable checks three independent history-diagonal observables on a
nontrivial density matrix. Maximum expectation defect is zero.

#### 2. Full coherent channel equivalence

Exact equality with the original source unitary channel requires

```text
<a_k|a_h> = 1
```

for every relevant pair of histories. Equivalently, on each connected
relevant history class the archive state is one common state. An informative
record violates this condition.

At `theta=pi/3`, the plus-state source channel differs from the original by
trace distance `0.25`, and the coherent `X` expectation changes by `0.25`.
At `theta=0`, full channel equality returns.

#### 3. Interventional equivalence

If the relocated archive can be acted on and later recoupled, the enlarged
model has interventions absent from a representation that treats the source
as fixed and inaccessible.

The fixed executable witness is:

1. form the pointer record;
2. CNOT-export it;
3. optionally apply `Z` to the archive;
4. apply the same inverse CNOT interface;
5. apply the same inverse pointer record;
6. apply the same Hadamard history recombiner; and
7. measure the same `h=0` outcome.

The archive `Z` alone changes the immediate source marginal by exactly zero,
as no-signalling requires. After the declared recoupling:

```text
no archive intervention:  P(h=0) = 1
archive Z intervention:    P(h=0) = 0.25
```

Thus the difference is interventional access plus later interaction, not
instantaneous signalling.

### Corollary

Boundary relocation preserves only a declared observational contract.

- An informative relocated record obstructs full coherent-channel
  invariance.
- An intervenable relocated record obstructs interventional invariance when
  its later coupling can change source outcomes.
- A diagonal quotient can remain valid without making the full physical
  theories equivalent.

This is the scoped **Boundary Relocation and Informative-Record
Obstruction**. It is stronger and less misleading than an unqualified
“boundary relocation invariance theorem.”

## 11. Interface-relative reunion

The probe's reunion is one frozen two-history subspace recombiner. Its basis,
phases, and later inverse coupling are fixed before evaluation and are not
refitted by encoding.

It is useful because it exposes coherence operationally. It is not a
simulation of:

- a complete particle trajectory away from and back to an observer;
- spatial archive transport;
- an autonomous detector;
- an observer-owned causal boundary; or
- a realistic relativistic laboratory reunion.

The correct grade is **interface-relative reunion**.

## 12. Executable receipt

Run:

```bash
.venv/bin/python tests/du_covariant_archive_boundary_probe.py
```

Result:

```text
31/31 checks pass
VERDICT: COVARIANT FINITE ARCHIVE WITH EXACT COMPLEMENTARITY;
         INTERFACE ONLY (NO PHYSICS CLAIM BANKED)
```

Artifacts:

```text
c7b052e2b95b72ae5575f6e8b36706af8f4bf0d9d3f15d7263d59219b9c045c8  tests/du_covariant_archive_boundary_probe.py
f280617b9309af21dbceae13283dd317240ff7fe48fbe4647368ddebe79dd018  tests/artifacts/du_covariant_archive_boundary_result.json
```

Receipt coverage:

| Audit | Bounded coverage |
|---|---:|
| complete pointer unitaries | 8 |
| canonical full-basis covariance cases | 192 |
| training all-placement covariance cases | 3,200 |
| held-out `6 x 5` all-placement cases | 480 |
| arbitrary-active-unitary cases | 320 |
| pointer settings for exact `V/D` | 4 |
| CNOT fanout archive sizes | 4 |
| fresh-cell horizons | 6 |

The probe also checks:

- matrix and fixed-fringe visibility;
- trace-norm distinguishability and equal-prior Helstrom success;
- carrier loss before and after export;
- CNOT versus SWAP;
- a dense history-independent interface unitary;
- coherent-input no-cloning;
- fresh cells versus fanout;
- finite recurrence and aliasing;
- diagonal, coherent-channel, and interventional boundary grades;
- a no-signalling guard before later recoupling;
- a raw-microstep negative control; and
- covariance nonselection by arbitrary active dynamics.

## 13. Countermodels and claim boundaries

| Tempting claim | Executable or analytic result | Correct conclusion |
|---|---|---|
| pointer law follows from covariance | arbitrary active block also passes | covariance admits, does not select |
| archive is already present | before export the blank cell has `D=0` | interface is added structure |
| CNOT copies the quantum record | coherent input becomes entangled | only a basis predicate is shared |
| CNOT preserves full evidence on each carrier | each marginal has `D=sin^2(theta)` | full evidence remains joint |
| loss tax forbids full transfer | SWAP retains `D=sin(theta)` on archive | transfer is possible without a retained copy |
| more CNOT targets mean independent evidence | fanout `D_E` stays fixed | GHZ-like redundancy is not fresh recording |
| finite unitary reuse accumulates irreversibly | exact revivals occur | fresh support or irreversibility must be charged |
| moving the boundary changes nothing | only diagonal algebra survives generally | equivalence is contract-relative |
| archive intervention signals instantly | immediate source marginal is unchanged | later recoupling exposes the intervention |
| reunion is a spatial return | only a fixed history recombiner was built | reunion remains interface-relative |

## 14. Relation to prior work and novelty

**Novelty status: `SEARCH-INCOMPLETE`.**

The source Clock-QCA covariance is due to Arrighi, Facchini, and Forets. The
visibility/distinguishability relation is established complementarity
structure, with Englert as the primary comparator. The channel-level
information/disturbance boundary is established quantum information, with
Kretschmann, Schlingemann, and Werner as the primary comparator.
No-broadcasting is established by Barnum and collaborators. Environmental
record proliferation is a developed program, with Zurek included here only
as primary context.

None of those antecedents by itself establishes that the exact package here
is novel:

```text
source-exact Clock-QCA tunable pointer
+ q-transparent covariance and nonselection
+ one-gate visibility/distinguishability witness
+ transfer-versus-redundancy-versus-fresh-record separation
+ archive-loss squared-D control
+ graded boundary-relocation obstruction
+ executable interventional reunion witness.
```

A broader search must still cover:

- quantum instruments covariant under discrete circuit encodings;
- reversible QCA measurement and history tapes;
- which-way markers with lossy environmental fragments;
- approximate broadcasting and information splitting;
- collision models and repeated-interaction decoherence;
- quantum Darwinism redundancy metrics;
- Stinespring representation uniqueness and subsystem relocation;
- process-theoretic observational and interventional equivalence; and
- finite-environment recurrences and resource-priced classicalization.

No publication priority is asserted.

## 15. What this changes for Dynamic Unity

The swing replaces one vague question—“can the record be moved into an
archive?”—with four distinct operations and exact consequences:

1. **Unitary repartition:** joint evidence is conserved.
2. **Redundant basis export:** loss-surviving distinguishability can be less
   than the original coherent distinguishability.
3. **Full transfer:** the original distinguishability can survive, but no
   second full copy remains.
4. **Independent recording:** distinguishability can grow, but only through
   new interactions and explicitly growing support.

It also sharpens the boundary question. A source can be mathematically
internalized without making all descriptions physically interchangeable.
What survives depends on whether one asks about:

- a restricted observable algebra;
- the full coherent channel; or
- the set of interventions and later couplings.

This is foundationally useful because it locates where additional physics
must enter. Covariance supplies compatibility. It does not supply the
interface, the preferred record basis, the flow of fresh blank capacity, or
irreversibility.

## 16. Next decisive move

The next build on this branch should not add another abstract clock premise.
It should ask whether any independently motivated local structure selects an
archive interface and record algebra rather than merely permitting one.

A decisive candidate would freeze:

1. an explicit locality geometry for archive cells;
2. an autonomous source-to-archive coupling rather than a hand-declared
   detector surface;
3. a finite resource account for blank cells and transport;
4. a fixed family of loss and reunion interventions;
5. a redundancy metric that distinguishes fanout from independent evidence;
6. a finite-environment recurrence horizon; and
7. a held-out comparison against other q-transparent active laws.

Advance would require a source-independent reason that one interface or
record algebra is preferred and an observable consequence of that choice.
If every archive law remains equally admissible and only the declared
interface makes the result, the correct disposition remains
`INTERFACE_ONLY_ARCHIVE`.

## 17. Final grade

### Earned

- complete finite unitary pointer extension;
- exact source-sense q-insertion covariance;
- in-host two-history realization;
- exact Gram-matrix source reduction;
- exact pure-state `V/D` complementarity;
- unitary archive evidence-conservation theorem;
- CNOT loss tax and SWAP transfer distinction;
- explicit no-cloning/no-broadcasting guard;
- fanout versus independent-record scaling;
- finite recurrence and alias controls;
- graded boundary-relocation obstruction;
- no-signalling-safe interventional witness; and
- deterministic `31/31` executable receipt.

### Not earned

- classical, irreversible, thermodynamic, or macroscopic record formation;
- a covariance-selected pointer, basis, archive, or interface;
- full redundant broadcasting of nonorthogonal records;
- autonomous transport or realistic spatial reunion;
- monotone unbounded memory from a finite reversible system;
- observer ownership or proper time;
- continuum or higher-dimensional covariance;
- gravity, cosmology, or Dynamic Unity identity;
- a banked claim, prediction seed, or publication novelty claim.

### Disposition

```text
COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY
INTERFACE_ONLY_ARCHIVE

construction grade:
  EXACT FINITE MATHEMATICAL CONSTRUCTION

theorem grade:
  EXACT SCOPED THEOREMS AND OBSTRUCTIONS

physical interpretation:
  COHERENT POINTER AND DECLARED INTERFACE;
  CLASSICALIZATION AND LAW SELECTION OPEN

novelty:
  SEARCH-INCOMPLETE

claim bank:
  none

prediction seed:
  none
```
