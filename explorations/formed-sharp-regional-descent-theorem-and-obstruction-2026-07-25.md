---
title: "Formed-sharp regional descent — exact absorber, conditional theorem, and obstructions"
status: completed_exact_branch
doc_type: exploration_and_executed_formal_result
created: 2026-07-25
run_id: RUN-20260725-110735-formed-sharp-descent
claim_grade: "EXACT FINITE CONSTRUCTIONS AND OBSTRUCTIONS / COMPONENT MATHEMATICS KNOWN / PHYSICAL FORMATION OPEN"
banked: false
seeded: false
---

# Formed-Sharp Regional Descent

## Plain-English result

This branch found a useful hard boundary rather than a new
pairwise-to-global quantum theorem.

If several measurements really are **sharp projective measurements on one
common quantum system**, then pairwise joint measurability already guarantees
one global joint measurement. That is a known consequence of commutation and
the spectral calculus. A cyclic family whose local records all look sharp but
cannot be glued globally is therefore not a counterexample. It shows that the
records were never established as occurrences of one common sharp archive.

If sharpness is relaxed, pairwise-to-global descent fails. Three orthogonal
qubit measurements with unsharpness \(\eta=2/3\) possess explicit joint
measurements for every pair but no triple joint measurement. If only the
outcome effects are matched, descent can fail even earlier: two instruments
can have the same sharp effects while producing different post-record states,
continuations, and total channels.

The strongest honest Dynamic Unity statement is consequently conditional:

> Once physical formation, common occurrence identity, and selective-map
> identity have been independently earned, regional descent still requires a
> full-cover compatibility receipt and a separate proof that the exported
> certificate preserves the upper-layer action.

On a join-tree cover the probability extension is automatic from matching
separator marginals. On a cyclic cover it is not. None of this derives the
physical instrument or archive.

The deterministic probe passes `36/36`:

- [probe](../tests/du_formed_sharp_descent_probe.py)
- [artifact](../tests/artifacts/du_formed_sharp_descent_result.json)

## 1. Keep the types separate

The word “compatible” is insufficient without an object type. This branch
freezes the following ladder:

```text
same outcome effect
    != same selective state-change map
    != same nonselective channel
    != same held-out continuation
    != same formed archive occurrence
    != one full-cover joint instrument
    != a certificate sufficient for the declared upper action.
```

It uses **common-output instrument compatibility** in the finite control: one
joint instrument must have the candidate instruments as exact selective-map
marginals on the same retained output system. Other notions of instrument
compatibility exist, so the operational type must be declared rather than
inferred from the word. See
[Mitra and Farkas](https://arxiv.org/abs/2110.00932) and
[Leppäjärvi and Sedlák](https://arxiv.org/abs/2212.11225).

“Formed” is also not a synonym for “written in the model.” It requires an
independent physical receipt for pointer/archive formation, access,
provenance, and resources. This branch begins after that receipt; it does not
manufacture one.

## 2. The common-sharp absorber

Let

\[
\mathsf P_i=\{P_i^{a_i}\}_{a_i\in A_i}
\]

be a finite family of PVMs on one Hilbert space. Joint measurability of two
PVMs is equivalent to commutation of all their effects. If every pair is
jointly measurable, all cross-effects commute, and

\[
G_{\mathbf a}=\prod_iP_i^{a_i}
\]

is a global joint PVM with the required marginals.

This is established measurement theory, not a Dynamic Unity theorem.
Heinosaari, Reitzner, and Stano state the pairwise-to-global result explicitly
for sharp observables
([primary source](https://arxiv.org/abs/0811.0783)). The exact finite fixture
in the probe realizes it on an eight-outcome diagonal archive:

- all regional effects are idempotent projections;
- every pair commutes;
- the product projections are exactly the eight archive singletons;
- the global PVM is orthogonal and normalized; and
- the selective diagonal filters are repeatable and mutually
  nondisturbing.

Therefore:

> A cyclic “sharp record” counterexample must fail common-system identity,
> genuine quantum sharpness, or the claimed pairwise compatibility.

It cannot refute the sharp-PVM theorem while retaining all three.

## 3. Finite commutative archive equivalence

There is a precise, but known, conditional theorem at the probability layer.

### Theorem — global extension versus commutative sharp archive

Fix finite variables, a context cover, outcome identities across overlaps,
and normalized context tables \(p_C\). The following are equivalent:

1. there is a global distribution \(p\) whose context marginals are the
   \(p_C\); and
2. the tables have a realization as deterministic coarse-grainings of one
   finite commutative sharp archive, with a diagonal state and a singleton
   master PVM.

**Construction.** From a global extension \(p\), take a Hilbert basis indexed
by global assignments \(\omega\), the diagonal state

\[
\rho=\sum_\omega p(\omega)|\omega\rangle\langle\omega|,
\]

and master projections
\(M_\omega=|\omega\rangle\langle\omega|\). Each context outcome is the sum of
the \(M_\omega\) in its cylinder set. Conversely, measuring any such master
archive supplies a global outcome distribution whose coarse-grainings are the
context tables.

This is a representation equivalence. It does **not** prove that the physical
system formed that master archive. Constructing the archive after seeing a
global distribution would be an interface completion, not a formation law.

For acyclic covers, matching separator marginals guarantee the global
extension by the known Vorob'ev/junction-tree result
([primary source](https://www.mathnet.ru/eng/tvp4710)). The probe constructs
the `AB—BC` extension exactly by conditional multiplication and reproduces
both context tables.

## 4. The cyclic obstruction says exactly what failed

The negative classical fixture has

\[
A=B,\qquad B=C,\qquad C\ne A
\]

with uniform marginals. Every context table is normalized and deterministic
on its declared pair relation. Every singleton overlap marginal is exactly
uniform. Yet the \(\mathbb Z_2\) cycle syndrome is one and exhaustive
enumeration finds zero global assignments.

This is standard marginal, contextuality, sheaf, and database-join terrain;
see the unified sheaf formulation of
[Abramsky and Brandenburger](https://arxiv.org/abs/1102.0264).
It has a narrow Dynamic Unity use:

```text
contextwise sharp relation
    + exact overlap probabilities
    != common formed occurrence identity
    != common sharp archive.
```

The fixture is natural under three declared harmless changes:

- flipping an outcome label merely moves the odd parity to another edge;
- inserting a deterministic identity relay preserves the odd syndrome; and
- adding redundant singleton marginals cannot repair the missing global
  extension.

Thus the obstruction is not a label, relay-count, or cover-presentation
artifact.

## 5. Exact unsharp Specker control

For three orthogonal Pauli directions \(i=x,y,z\), define binary effects

\[
E^{(i)}_a=\frac12(I+a\eta\sigma_i),
\qquad a\in\{-1,+1\}.
\]

Set \(\eta=2/3\). For each pair \(i\ne j\),

\[
G^{ij}_{ab}
=\frac14\left[I+\eta(a\sigma_i+b\sigma_j)\right]
\]

is positive because \(2\eta^2=8/9<1\), and its marginals are exactly
\(E^{(i)}_a\) and \(E^{(j)}_b\). Hence all three pairs are jointly measurable.

Suppose a triple joint POVM \(G_s\), \(s\in\{-1,+1\}^3\), existed. Its
marginals would imply

\[
\sum_s s_iG_s=\eta\sigma_i.
\]

Using the largest eigenvalue
\(\lambda_{\max}(s_x\sigma_x+s_y\sigma_y+s_z\sigma_z)=\sqrt3\),

\[
3\eta
=\frac12\sum_s
\operatorname{Tr}\!\left[
(s_x\sigma_x+s_y\sigma_y+s_z\sigma_z)G_s
\right]
\leq\sqrt3.
\]

But \(3\eta=2>\sqrt3\), so no triple joint POVM exists. The probe checks the
pairwise constructions and the squared dual inequality exactly. As a positive
control, \(\eta=1/2\) admits the explicit eight-effect triple joint POVM

\[
G_s=\frac18\left[I+\eta(s_x\sigma_x+s_y\sigma_y+s_z\sigma_z)\right].
\]

This is known joint-measurability/Specker terrain, not a new obstruction; a
necessary-and-sufficient treatment for three unbiased qubit observables is
given by [Yu and Oh](https://arxiv.org/abs/1312.6470). Its value is diagnostic:

> If the physical-formation branch earns only noisy effects or generic POVMs,
> pairwise compatibility cannot support global descent.

The result does not weaken the common-system sharp-PVM theorem. At
\(\eta=1\), even the displayed orthogonal pair construction is nonpositive.

## 6. Effect equality is below instrument identity

The probe also gives two exact binary instruments with the same sharp
outcome effects:

- a QND instrument retains the measured bit; and
- a flip instrument changes the post-record bit.

The outcome-zero QND map is idempotent. The effect-identical flip map is not.
A held-out repeat measurement distinguishes them with certainty. Their
nonselective channels are respectively identity and bit flip.

Under the frozen common-output compatibility type, they cannot be marginals
of one joint instrument: summing any joint instrument over all outcomes gives
one total channel, whereas the proposed marginals require two different total
channels.

This supplies the exact typed stop:

> Matching sharp effects does not license cross-context instrument identity
> or descent.

Repeatability, the selective map, total channel, and held-out continuation
must be checked before gluing.

## 7. Upper-action sufficiency is independent

The common archive fixture has a perfectly valid global sharp instrument.
Nevertheless, an exported `AB` certificate loses the action

\[
u(A,B,C)=A\oplus B\oplus C.
\]

Under the uniform fixture, its optimal action error is \(1/2\). The full
`ABC` archive has zero error.

For any deterministic certificate \(f:H\to C\), exact upper-action
sufficiency is the separate condition

\[
u=\bar u\circ f,
\]

equivalently that \(u\) is constant on every certificate fiber. A global
joint measurement does not imply this for an arbitrary exported
coarse-graining or task.

## 8. Strongest honest descent statement

The branch supports the following scoped contract:

> **Conditional formed-sharp descent.** Freeze a finite physical formation
> receipt, a common occurrence and selective-map identity type, context
> instruments, a cover, an exported certificate, and an upper task. If the
> formed context instruments are deterministic quotients of one common
> commutative sharp archive, then they possess a global joint instrument.
> At the probability layer a join-tree cover with matching separators
> constructs such an extension. On a general cover, a full-cover extension
> receipt is necessary. The descended certificate is action-sufficient
> exactly when the upper response factors through it.

This statement combines several required receipts without turning them into
one scalar:

\[
\left(
\text{formed typed identity},
\ \text{full-cover extension},
\ \text{upper-action factorization},
\ \text{provenance/access/resources}
\right).
\]

Its mathematical components are occupied. The potentially distinctive
Dynamic Unity contribution remains **upstream**: physically derive the
instrument class and common identity without supplying a PVM, basis, master
archive, or decoder.

## 9. Disposition and next discriminator

| Candidate | Exact branch result | Disposition |
|---|---|---|
| Pairwise-to-global for common sharp PVMs | True automatically by standard spectral theory | `ABSORBED / REGRESSION CONTROL` |
| Join-tree context gluing | True for matching finite marginals | `KNOWN POSITIVE CONTROL` |
| Cyclic pair records with exact overlaps | No global extension | `KNOWN FULL-COVER OBSTRUCTION` |
| General unsharp pairwise compatibility | Does not imply global compatibility | `EXACT SPECKER CONTROL` |
| Equal sharp effects | Does not imply equal instruments or continuations | `EXACT TYPED NO-GO` |
| Global instrument | Does not imply arbitrary coarse certificate is action-sufficient | `EXACT TASK-RELATIVE CONTROL` |
| New Dynamic Unity theorem from Branch B alone | Not obtained | `NO PROMOTION` |

The next branch should not search for another abstract gluing theorem. It
should ask whether physical formation supplies a condition stronger than a
declared PVM:

1. derive the selective instrument from an implementation-complete
   system–pointer–archive process;
2. freeze repeatability, nondisturbance, access, provenance, and resources;
3. test held-out continuations and total channels;
4. determine whether a common archive is selected rather than added as a
   completion; and
5. only then carry the full-cover and upper-action receipts through descent.

If physical formation yields only ordinary supplied PVM structure, the
pairwise-to-global branch is finished by the known absorber. If it yields a
strictly motivated instrument class that excludes the unsharp Specker or
almost-quantum foil without importing Hilbert structure, that is the genuine
reopener.

No physical law, theorem ID, prediction, ontology, or paper priority is
promoted by this branch alone.
