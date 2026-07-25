---
title: "Multi-time regional grammar and exact marginal transfer"
status: completed_exact_control
doc_type: exploration_and_executed_transfer
created: 2026-07-25
run_id: RUN-20260725-071641-multitime-marginal-transfer
claim_grade: "EXACT FINITE RATIONAL COMPILER + COMPLETE FINITE INSTRUMENT TRANSFERS / COMPONENT MATHEMATICS KNOWN / PHYSICAL THEORY OPEN"
banked: false
seeded: false
---

# Multi-time regional grammar and exact marginal transfer

## Plain result

The prepared swing succeeds technically and corrects the interpretation of
regional descent.

Dynamic Unity now has:

1. a general exact finite marginal compiler that accepts arbitrary finite
   variable alphabets and context hypergraphs and returns either an explicit
   global distribution or a checkable Farkas obstruction;
2. overlapping regions `AB` and `BC` derived from complete independently
   frozen multi-time QND record instruments rather than a favored endpoint
   diagram;
3. one authenticated protocol transfer in which a coarse obstruction is
   exactly repaired by route provenance and then correctly classified as
   equivocation requiring safe rejection; and
4. one complete quantum transfer in which the compiler recovers the
   Mermin--Peres contextuality obstruction, while the context-indexed quantum
   instruments remain ordinary completely positive physics.

The integrated probe passes `33/33`.

The most important conclusion is:

> A marginal obstruction refutes the proposed identification of overlap
> variables. It does not, by itself, refute the existence of the physical
> process that produced the local records.

In the protocol, one authenticated origin was incorrectly forced to have one
value across two routes despite equivocation. In the quantum fixture, one
observable was incorrectly forced to possess one context-independent
pre-existing outcome across incompatible measurement contexts. Splitting the
unjustified identity restores a global process in both.

This produces a new required ordering for the regional-finality program:

```text
derive the local instruments
    -> certify which overlap occurrences are physically the same record
    -> test marginal compatibility under only those certified identifications
    -> test boundary action sufficiency
    -> apply safety, liveness and resource gates.
```

## 1. Exact marginal-extension compiler

### 1.1 Frozen problem

For finite variables \(X_1,\ldots,X_n\), finite outcome alphabets, a context
cover \(\mathcal C\), and complete rational local marginals \(p_C\), enumerate
the global assignments \(\omega\). The marginal problem is

\[
Aq=b,\qquad q\geq0,
\]

where each column of \(A\) is one global assignment and each row asks for one
declared local event probability.

The compiler returns exactly one:

```text
GLOBAL_EXTENSION
DUAL_OBSTRUCTION
INCOMPLETE_CONTRACT
```

`GLOBAL_EXTENSION` includes a sparse exact-rational distribution \(q\) and
substitution checks for every marginal equality.

`DUAL_OBSTRUCTION` includes an integer-normalized vector \(y\) satisfying

\[
A^\mathsf{T}y\geq0,
\qquad
b^\mathsf{T}y<0.
\]

Every hypothetical global distribution would make the weighted expression
nonnegative, while the supplied local records make it negative. This is a
machine-checkable incompatibility receipt.

### 1.2 Solver

`tests/du_exact_marginal_extension_compiler.py` implements an exact Phase-I
simplex using `fractions.Fraction` and Bland entering/leaving rules.

It:

- validates complete normalized rational tables;
- constructs arbitrary finite context hypergraphs;
- begins with an artificial-variable basis;
- returns an original-variable primal when the Phase-I optimum is zero;
- extracts the Farkas dual from the final artificial columns when the optimum
  is negative;
- normalizes the dual to coprime integers; and
- independently substitutes every primal or dual certificate.

No floating tolerance, fitted facet, cycle-specific formula, SciPy solver, or
platform label enters the verdict.

### 1.3 Generic controls

Two triangles glued along an edge supply the first general-hypergraph
controls:

- all-equality local marginals return a two-state global extension;
- changing one edge of the second triangle to inequality returns an exact
  dual obstruction; and
- its three-context frustrated subfamily is inclusion-minimal because every
  one-context deletion returns a global extension.

An unfrozen contract returns `INCOMPLETE_CONTRACT`.

As an independent implementation oracle, the general compiler is also run on
all `343` denominator-six binary-triangle marginal triples from the preceding
cycle-specific probe. It returns `119` primal extensions and `224` dual
obstructions with zero disagreements against the closed signed-sector
weights.

The prior odd-cycle inequalities remain valuable optimized special cases.
The new compiler establishes a general finite adjudicator, not a scalable
large-system algorithm.

## 2. Instrument-derived multi-time regions

### 2.1 Complete instruments

Three binary primitives \(A,B,C\) are prepared in computational-basis states.
Two QND parity instruments measure

\[
Z_AZ_B,\qquad Z_BZ_C.
\]

For each instrument the probe constructs the exact projectors

\[
P_\pm=\frac{I\pm O}{2}
\]

over Gaussian-rational matrices and verifies:

- the observable is Hermitian and squares to identity;
- every selective map has one Kraus projector and is completely positive;
- the projectors are Hermitian and idempotent;
- \(\sum P^\dagger P=I\), so the nonselective instrument is trace preserving;
- the instruments commute;
- every computational-basis input is nondemolished; and
- Born probabilities reproduce the complete deterministic stochastic record
  kernels.

### 2.2 Region extraction

For a complete controlled instrument kernel, a primitive belongs to its
minimal parent region exactly when changing that primitive while fixing every
other input changes the complete accessible outcome distribution for some
declared control.

Applied before any downstream task:

```text
record_AB -> {A,B}
record_BC -> {B,C}
```

The regions overlap at `B`. They are preserved under relabeling. Replacing
`B` with a deterministic implementation relay changes the raw parent labels
but collapses to the same regions under the predeclared relay provenance
quotient.

Changing the downstream target cannot change the frozen instrument digest.

This is a finite instrument-derived regional grammar. It does not show that
this parent-support definition is the uniquely physical regionalization of a
general process tensor.

### 2.3 Multi-time separator

The instrument process retains the two formed parity records and later emits

\[
r_{AB}\oplus r_{BC}=A\oplus C.
\]

An endpoint rival computes \(A\oplus C\) directly. Without an intermediate
intervention, the two models agree on all eight inputs.

A held-out causal break resets the primitive qubits after record formation
while leaving the record registers intact. The recorded process preserves the
old parity; the endpoint rival outputs the reset value. Four of eight
histories separate.

The result is deliberately modest:

> Endpoint equivalence does not identify multi-time regional history when a
> predeclared causal break can preserve formed records while resetting their
> primitive sources.

This is consistent with the process-tensor emphasis on complete multi-time
controls rather than endpoint channels. Pollock et al. describe the process
tensor as a mapping from sequences of control operations to output states
and show its general open-system realization
([source](https://arxiv.org/abs/1512.00589)).

## 3. Authenticated protocol transfer

### 3.1 Executed fixture

The protocol fixture contains three origins, three pair routes, a fixed
epoch, HMAC-SHA256 fixture authentication, route-bound messages, and
enumerated hidden states.

Every one of its `12` routed messages verifies under its declared origin,
route, and epoch. Replaying a valid message into a different epoch is
rejected.

The local transcripts are:

```text
AB: A = B
BC: B = C
CA: C != A
```

All messages are authentic. Origin `A`, however, signs different values on
`AB` and `CA` in the same epoch.

### 3.2 Coarse obstruction

If route-local occurrences are forcibly glued into one canonical value for
each of `A,B,C`, the general compiler returns `DUAL_OBSTRUCTION`.

Every proper context subfamily is compatible. The full loop is not, because
one binary triangle cannot contain exactly one mismatch.

Authentication alone therefore does not establish cross-route value
consistency.

### 3.3 Provenance lift and disposition

When the independently formed route labels are retained,

```text
A@AB, B@AB, B@BC, C@BC, C@CA, A@CA,
```

the unchanged compiler returns a two-state `GLOBAL_EXTENSION` over its
64-state declared space.

The coarse terminal summary also aliases histories requiring accept and
reject, giving binary action defect `1/2`. Adding the formed equivocation
provenance reduces the defect to zero.

That is not successful consensus descent. The correct protocol result is:

```text
SAFE_REJECTION_EQUIVOCATION_PROVENANCE_FORMED
```

The apparent stochastic remainder was an unjustified cross-route identity.
The provenance lift explains the process and supplies the evidence needed to
reject it safely.

The fixture establishes no cryptographic reduction, BFT theorem, liveness
bound, or production protocol security.

## 4. Quantum-instrument transfer

### 4.1 Complete Mermin--Peres instruments

The quantum arm constructs the nine two-qubit Pauli observables

```text
XI  IX  XX
IY  YI  YY
XY  YX  ZZ
```

and the six row/column contexts. Every context contains three commuting
observables. The product is \(+I\) in all three rows and the first two
columns, and \(-I\) in the last column.

For every context and all eight outcome triples, the probe constructs the
joint spectral projector, then verifies:

- exact Hermiticity and idempotence;
- Kraus-form complete positivity;
- projector completeness;
- trace preservation of the nonselective instrument;
- four nonzero outcomes;
- exact normalization; and
- support on precisely the required parity sector.

The state is \(I/4\), so every allowed triple has probability \(1/4\).
Nothing is fitted to the marginal compiler.

### 4.2 Noncontextual gluing obstruction

Forcing each of the nine observable names to have one pre-existing value
shared across its row and column produces:

- `9` binary variables;
- `512` proposed global assignments;
- `6` contexts;
- `48` exact marginal constraints; and
- an exact `DUAL_OBSTRUCTION` after `54` Phase-I pivots.

All six one-context deletions return `GLOBAL_EXTENSION`. Thus every proper
context subfamily is compatible.

The parity reason is familiar: multiplying all six required context parities
gives \(-1\), while multiplying one global assignment counts every observable
twice and must give \(+1\).

This is the standard Mermin--Peres contextuality structure, not a Dynamic
Unity novelty. Mermin's original simplified no-hidden-variable construction
is [here](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.65.3373);
Abramsky and Brandenburger formalize contextuality as a global-section
obstruction over arbitrary measurement covers
([source](https://arxiv.org/abs/1102.0264)).

### 4.3 Context-indexed physical process

The no-global-value result does not mean no quantum process exists. All six
context instruments are explicit completely positive instruments.

When each outcome is indexed by the actually implemented context, the exact
product construction gives a normalized `4^6 = 4096`-support global
distribution whose six marginals reproduce the instrument tables exactly.

Erasing the context register also aliases two declared action classes and
has binary half-range defect `1/2`; retaining it makes the defect zero.

The honest result is:

```text
standard context-indexed quantum process exists
    +
one context-independent noncontextual value assignment does not.
```

No beyond-standard dynamics, observer-relative collapse law, reality
curvature, public-finality threshold, or physical backreaction follows.

## 5. The cross-platform lesson: identity before descent

The protocol and quantum arms fail coarse gluing for different physical
reasons but expose the same formal hazard.

| Arm | Forced overlap identity | Why it fails | Formed repair | Final disposition |
|---|---|---|---|---|
| authenticated protocol | one origin has one value across routes | authenticated equivocation | route/epoch provenance | global routed process + safe rejection |
| quantum instrument | one observable has one pre-existing value across incompatible contexts | standard contextuality | implemented-context register | ordinary context-indexed quantum process |

The compiler never decides which overlap occurrences deserve identification.
It only decides the consequences of the supplied identification.

This sharpens `HC-DU-035C`:

```text
local overlap agreement
    != certified overlap identity
    != global marginal compatibility
    != action-sufficient node promotion
    != safe public finality.
```

### 5.1 Occurrence-splitting absorber lemma

For any finite family of normalized local marginals, replace each occurrence
of variable \(X\) in context \(C\) by a separate variable \(X@C\). The product
of the local marginal distributions is then a global extension.

Therefore:

> Every finite marginal obstruction can be absorbed by maximal context
> splitting.

This is elementary and not novel. Its importance is diagnostic: a physically
meaningful obstruction requires independently justified gluing maps. Without
them, the obstruction identifies only that one proposed cross-context
identity is too strong.

### 5.2 Certified-overlap precondition

A regional descent claim should now carry two independent receipts:

1. **overlap-identity receipt:** why two local record occurrences are the same
   operational event or value across the declared contexts; and
2. **extension receipt:** whether the identified local marginals possess one
   global extension.

For protocols, identity evidence can involve origin, epoch, route, parent
hash, failure domain, and equivocation rules.

For quantum instruments, it can involve one declared observable effect,
operational equivalence, compatibility/nondisturbance conditions, sequential
repeatability, complete context controls, and disturbance accounting.

Neither receipt may be defined by the target result it is meant to support.

## 6. What is complete and what remains open

### Complete at exact finite-control grade

- general finite rational marginal compilation;
- primal and Farkas certificate verification;
- glued-cycle and nonacyclic-context controls;
- exact QND multi-time regional parent extraction;
- relay and label covariance controls;
- held-out causal-break separation;
- authenticated coarse obstruction and route lift;
- safe equivocation rejection;
- complete two-qubit contextual instruments;
- exact noncontextual obstruction and all leave-one-context-out controls; and
- exact context-indexed product absorption.

### Still open

- a physically unique or abductively preferred regional grammar for general
  process tensors;
- a non-tautological overlap-identity certificate that transfers across
  platforms;
- robust finite-shot versions with calibration, drift, leakage, and
  adversarial adaptivity;
- sparse/chordal decomposition rather than full global-state enumeration;
- recursive composition of compatibility and action defects;
- authenticated protocol security and liveness;
- a contextuality experiment closing compatibility/disturbance and
  identification loopholes under this record contract;
- a residual not absorbed by standard quantum instruments, route provenance,
  controller/environment completion, or context splitting; and
- any new physics, ontology, law, prediction, geometry, or paper claim.

## 7. Prepared next approaches

### `OI-NEXT-01` — certified overlap identity assay

- **Question:** when are two local record occurrences licensed as one physical
  overlap variable?
- **Approach:** freeze occurrence maps before outcomes; require provenance,
  repeatability or operational-equivalence evidence; hold out a context
  permutation, causal break, and disturbance audit.
- **First object:** the two QND parity instruments plus a context-dependent
  disturbance rival with matched endpoint marginals.
- **Negative output:** overlap remains underidentified or context-relative.
- **Cheap kill:** “same variable name” or “same operator label” supplies the
  identity.
- **Scale gate:** unchanged identity receipt transfers to one authenticated
  route protocol.

### `MC-NEXT-01` — sparse exact marginal compiler

- **Question:** can exact certificates scale without enumerating every global
  assignment?
- **Approach:** use acyclic/junction-tree decomposition where valid and
  column generation or decomposition elsewhere, with the current solver as
  the oracle regression.
- **First object:** two recursively glued context complexes with a chordal
  positive control and one irreducible cycle obstruction.
- **Negative output:** an exact exponential lower-bound specimen or a typed
  resource stop.
- **Cheap kill:** a heuristic message-passing fixed point is reported as an
  exact extension.
- **Scale gate:** reproduce every current primal/dual certificate and solve a
  materially larger sparse cover.

### `RC-NEXT-01` — recursive defect composition after identity

- **Question:** how do overlap-identity uncertainty, compatibility
  obstruction, and boundary-action defect compose across two promotions?
- **Approach:** retain them as a vector before seeking bounds; include shared
  provenance and correlated error explicitly.
- **First object:** two promoted contextual/protocol triangles sharing one
  independently certified boundary.
- **Negative output:** a counterexample proving no scalar composition law.
- **Cheap kill:** independent errors or independent validators are assumed.
- **Scale gate:** invariance under benign subdivision and one correlated-noise
  family.

### `PHY-NEXT-01` — implementation-complete overlap stress test

- **Question:** does any gluing obstruction survive complete quantum
  instrument, context, environment, controller and record provenance?
- **Approach:** start from a standard contextuality or coherent-history
  positive control; progressively close compatibility, disturbance, leakage,
  memory and context-tag completions without changing the assay.
- **First object:** proposal-level sequential QND/contextual instrument with
  a complete causal-break and formed record registers.
- **Negative output:** standard contextuality/process-tensor absorption.
- **Cheap kill:** nonexistence of a noncontextual value assignment is called a
  failure of the quantum process itself.
- **Scale gate:** a calibrated residual under a held-out instrument and
  implementation-complete null.

## 8. Disposition

- Extend `HC-DU-035C`, `H-CCR-16`, and `CONCEPT-DU-011`.
- Install certified overlap identity as a required precondition inside the
  existing recursive-regional-finality concept, not a new ontology.
- Mark the general finite marginal compiler, QND regional control,
  authenticated transfer, and quantum transfer completed at exact scoped
  grade.
- Keep sparse scaling, physical overlap selection, robust experiment, and
  recursive defect composition open.
- Add no prediction, claim, law, ontology, paper priority, Factory state,
  draft, submission, publication, or external action.
