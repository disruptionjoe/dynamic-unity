---
title: "Adversarial audit — covariant archive and boundary relocation"
status: completed_adversarial_audit
doc_type: adversarial_research_audit
created: 2026-07-24
contract: explorations/covariant-archive-boundary-swing-contract-2026-07-24.md
hardening_id: HC-DU-031C
banked: false
seeded: false
novelty_status: SEARCH-INCOMPLETE
verdict: "COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY / INTERFACE_ONLY_ARCHIVE"
---

# Adversarial audit: covariant archive and boundary relocation

## Bottom line

The finite coherent pointer is straightforwardly source-sense covariant because
it is another member of the `q`-transparent active-unitary closure proved in
`HC-DU-031B`. That covariance is exact but remains nonselective.

The archive is more informative than another covariance pass. It separates
four operations that had previously been called “copying a record”:

1. retaining a coherent pointer;
2. transferring it to another carrier;
3. redundantly exporting one pointer-basis predicate; and
4. independently forming additional records from the source history.

Those operations have different information, interference, and resource
consequences. The boundary result is correspondingly graded: state
augmentation is representational, diagonal observational equivalence can
survive informative recording, full coherent source-channel equivalence
cannot, and a capability difference requires an admitted archive intervention
plus later recoupling.

The independent executable disposition is:

```text
COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY
INTERFACE_ONLY_ARCHIVE
```

The finite construction and scoped obstruction survive. The archive boundary,
basis, coupling, blank capacity, and later interventions are explicit added
structure rather than consequences of covariance.

## 1. Primary-source and novelty boundary

The exact host remains the `1+1` Clock QCA of
[Arrighi, Facchini, and Forets](https://arxiv.org/abs/1404.4499). Its
construction-specific discrete covariance is not continuum or
higher-dimensional Lorentz invariance.

The following ingredients are established prior structure and cannot be
promoted as novelty:

- Englert's
  [visibility/which-way inequality](https://doi.org/10.1103/PhysRevLett.77.2154);
- channel information-disturbance and enlarged-unitary representations in
  [Kretschmann, Schlingemann, and
  Werner](https://arxiv.org/abs/quant-ph/0605009);
- no-cloning in
  [Wootters and Zurek](https://doi.org/10.1038/299802a0);
- the stronger mixed-state no-broadcasting boundary in
  [Barnum, Caves, Fuchs, Jozsa, and
  Schumacher](https://arxiv.org/abs/quant-ph/9511010);
- environmental proliferation of selected records in
  [Zurek](https://arxiv.org/abs/0903.5082); and
- the operational importance of interventions in quantum causal models, for
  example [Barrett, Lorenz, and
  Oreshkov](https://arxiv.org/abs/1906.10726).

The possible contribution is the exact combination of those constraints with
the source-exact Clock-QCA extension, its inert-`q` nonselection theorem, a
loss/export/reunion receipt, and an explicitly graded boundary contract.
Novelty remains `SEARCH-INCOMPLETE`.

## 2. Exact two-history audit

Let the equal-amplitude history state after record interaction be

```text
|Psi_phi> =
    (|h_0>|a_0> + exp(i phi)|h_1>|a_1>)/sqrt(2),

|a_0> = |0>,
|a_1> = cos(theta)|0> + sin(theta)|1>.
```

Write

```text
gamma = <a_0|a_1> = cos(theta).
```

Tracing the record gives

```text
rho_S(phi) =
1/2 [[1, exp(-i phi) gamma],
     [exp(i phi) gamma*, 1]].
```

The diagonal source populations remain `1/2,1/2`. The normalized fringe
visibility of a fixed balanced recombiner is

```text
V = |gamma|.
```

The trace distance between the two pure record states is

```text
D = 1/2 || |a_0><a_0| - |a_1><a_1| ||_1
  = sqrt(1-|gamma|^2).
```

With equal priors, the optimal success probability is `(1+D)/2`. Hence

```text
V^2 + D^2 = 1.
```

At the frozen intermediate point `theta=pi/3`:

```text
V                  = 1/2
D                  = sqrt(3)/2
optimal success    = (2+sqrt(3))/4
```

This is a calibrated exact relation, not a new duality law.

## 3. Gram-matrix channel theorem

Let `{P_h}` be orthogonal source history projectors and let

```text
W = sum_h U P_h tensor |a_h>
```

be the record isometry. Then

```text
Tr_A[W rho W*]
  = sum_(h,k)
      <a_k|a_h> U P_h rho P_k U*.
```

The archive Gram matrix is therefore exactly the multiplier of the source
history-coherence blocks.

Three consequences survive hostile review.

### 3.1 Diagonal observations survive

If `U* O U` is block diagonal in the history decomposition, every `h!=k`
contribution vanishes in the expectation of `O`. Since
`<a_h|a_h>=1`, the recorded and unrecorded models give the same expectation
for every such observable and every input state.

This is a nontrivial but deliberately restricted observational algebra. It
does not establish equality of the complete source states.

### 3.2 Full coherent channel equality forces an uninformative record

If the reduced channel equals `rho -> U rho U*` for every input, choose source
states and observables that isolate each nonzero `P_h rho P_k` block. Equality
forces

```text
<a_k|a_h> = 1
```

for every relevant pair. Normalized archive states with unit overlap are the
same state. The record is uninformative on that connected history sector.

This is the finite exact endpoint of the information-disturbance relation
already isolated in `HC-DU-031B`.

### 3.3 Population preservation is not passive recording

The diagonal populations can remain exact while the off-diagonal source
coherence changes. A test that checks only paths, counts, or populations is
incapable of detecting record backreaction.

## 4. Four different archive operations

Before distinguishing the four cases, one general conservation statement
applies. Let a history-independent unitary act on a record and one blank
archive:

```text
U_AE |a_h>|0> = |b_h>.
```

Unitarity gives

```text
<b_0|b_1> = <a_0|a_1>.
```

The two conditional joint outputs therefore have exactly the same pure-state
trace distance as the inputs. Partial trace is a quantum channel, so the
distinguishability in either output carrier alone cannot exceed the original
joint distinguishability.

Archive processing can transfer or repartition existing history evidence. It
cannot manufacture more of it without another history-dependent source
interaction. Reproducing the complete input record on both marginals would be
broadcasting and is forbidden for the distinct nonorthogonal pointer states.

### 4.1 Coherent retention

Keeping the pointer preserves the full two-state distinguishability

```text
D_pointer = |sin(theta)|.
```

It is still a coherent quantum degree of freedom, not a classical final
record.

### 4.2 Full transfer by SWAP

Swapping the pointer with a blank archive moves the complete pointer state to
the archive:

```text
|a_h>_A |0>_E -> |0>_A |a_h>_E.
```

After loss of `A`, the archive retains

```text
D_E = |sin(theta)|.
```

There is no general “archive tax” for transfer. The price is that the original
carrier no longer retains a second copy.

### 4.3 Redundant pointer-basis export by CNOT

For a blank archive cell, computational-basis CNOT gives

```text
|a_0>_A|0>_E -> |0,0>
|a_1>_A|0>_E -> cos(theta)|0,0> + sin(theta)|1,1>.
```

The two joint record states still have overlap `gamma`, so their joint
distinguishability remains `|sin(theta)|`.

If the pointer carrier is then lost, however,

```text
rho_E^0 = |0><0|,
rho_E^1 = cos^2(theta)|0><0| + sin^2(theta)|1><1|,
```

and therefore

```text
D_E_after_loss = sin^2(theta) = D_pointer^2.
```

The pointer marginal has the same `sin^2(theta)` distinguishability after
CNOT. The remaining gap between either marginal and the joint value
`|sin(theta)|` is held in pointer-archive correlations.

At `theta=pi/3`, the full pointer/joint record has distinguishability
`sqrt(3)/2`, while the surviving archive alone has `3/4`. Its equal-prior
success probability is `7/8`.

The strict inequality

```text
V^2 + D_E_after_loss^2
  = cos^2(theta) + sin^4(theta)
  < 1
```

for intermediate angles is not a violation of complementarity. Some
distinguishability remains outside the surviving archive marginal.

CNOT has redundantly exported a pointer-basis predicate. It has not cloned the
unknown coherent pointer state.

### 4.4 Independent fresh record formation

If the source history interacts independently with `m` fresh blank cells, the
conditional archive states are

```text
|A_0^(m)> = |a_0>^tensor m,
|A_1^(m)> = |a_1>^tensor m.
```

Thus

```text
V_m = |gamma|^m,
D_m = sqrt(1-|gamma|^(2m)).
```

The increasing distinguishability is paid for twice: one new blank cell per
interaction and additional loss of source coherence.

This is not equivalent to fanning out one pointer with repeated CNOTs. That
fanout produces

```text
cos(theta)|0...0> + sin(theta)|1...1>
```

on the event branch. Its overlap with the blank branch remains `gamma`, and
after original-pointer loss its archive-only distinguishability remains
`sin^2(theta)` regardless of the number of perfectly correlated fanout cells.

Independent evidence and redundant carriage are different resources.

## 5. No-cloning and no-broadcasting guard

Suppose one unitary could retain and duplicate both possible pure pointer
states:

```text
|a_h>|0> -> |a_h>|a_h>.
```

Unitarity preserves the input inner product `gamma`, while the output inner
product is `gamma^2`. Therefore `gamma=gamma^2`; distinct nonorthogonal states
cannot be duplicated this way.

Orthogonal pointer-basis states can be copied, and a complete pointer state can
be transferred by SWAP. Those are the correct positive controls. The
construction must not turn the no-cloning guard into a claim that records
cannot be moved or that classical predicates cannot be redundantly exported.

## 6. Finite reuse is not irreversible accumulation

Repeatedly applying the same rotation to one finite pointer gives

```text
R_theta^m |0>
  = cos(m theta)|0> + sin(m theta)|1>.
```

Its history distinguishability is `|sin(m theta)|`, not a monotone function of
`m`. At `theta=pi/3`, the event and no-event pointer rays coincide again after
three uses and the vector itself returns after six.

Likewise a modulo-`R` counter aliases after `R` increments. An irreversible or
monotonically accumulating classical record therefore needs fresh support, a
bath/coarse-graining limit, dissipation, measurement/finality, or another
explicitly charged ingredient. Finite unitary reuse alone does not supply it.

This gives a restricted local-finiteness/global-openness corollary. Every
finite record horizon has a finite realization, while exact nonaliasing record
semantics at arbitrary horizon cannot be absorbed by one fixed finite record
space. The conclusion is relative to that exact semantic and completion
class. It is not evidence that physical law or the universe is globally open.
Equivalently, relative to a fixed finite-unitary completion class, exact
continued recording must eventually alias/recur, weaken its semantics, or
leave the class by acquiring new support. This is a parameterized resource
trichotomy, not a universal productive-escape law.

## 7. Boundary Relocation Contract Theorem

“Move the source inside the state” has three grades.

### Grade A — representation equivalence

An external source or environment can be included in an enlarged state, with
the original coupling represented as joint dynamics. If the initial state,
dynamics, observation map, and admissible interventions are all transported
unchanged, this is an exact change of representation.

This is standard state augmentation, not a physical discovery.

### Grade B — declared observational equivalence

Comparing the recorded system with the unrecorded source unitary, the exact
preserved algebra is limited by the Gram-matrix theorem. In this fixture all
history-diagonal observations agree. Coherent cross-history observations
generally do not.

The invariant is therefore a declared observation contract, not “the
boundary does not matter.”

### Grade C — interventional or capability equivalence

A local trace-preserving intervention on the archive alone cannot
instantaneously change the source marginal. This no-signalling control must
pass.

The archive can nevertheless change later source outcomes if it is retained,
an admitted intervention acts on it, and later dynamics recouples it to the
source. At the perfect-record endpoint:

```text
|+>_S|0>_A
  --CNOT_(S->A)--> (|00>+|11>)/sqrt(2)
  --Z_A----------> (|00>-|11>)/sqrt(2)
  --CNOT_(S->A)--> |->_S|0>_A.
```

Without `Z_A`, the same record/unrecord sequence returns `|+>_S`. A fixed
source `X` readout therefore flips from certain `+` to certain `-` when the
archive intervention is available. The current source marginal immediately
after `Z_A` remains maximally mixed; the difference appears only after the
declared recoupling.

If the external-source representation offers no corresponding intervention,
the two representations are observationally equivalent only on the narrower
contract and are not capability-equivalent.

This supplies a restricted source-boundary-capability correspondence:

> internalizing a record changes operational capability exactly when the
> admitted access-and-recoupling contract exposes a source-relevant
> intervention.

Mere ontological relabeling or hidden internal state is not capability.

## 8. Covariance and interface audit

The pointer interaction is an active-sector unitary with transparent `q`
transport. The `HC-DU-031B` closure lemma proves its canonical source
covariance for arbitrary positive rectangular patch sizes. Placement sweeps
and a held-out patch remain required executable controls.

This positive result does not select:

- `theta`;
- the pointer basis;
- the archive carrier;
- the export or transfer gate;
- the location of a detector/reunion surface;
- which archive interventions are physically available; or
- an irreversible record law.

A single declared output interface can read or export the transported pointer
without changing its encoded value. That is interface-relative accessibility,
not a derivation of the interface from covariance. Unless the executable
constructs a homogeneous archive-emission rule inside the QCA itself, the
correct scoped outcome includes:

```text
INTERFACE_ONLY_ARCHIVE
```

## 9. Executable decisions

The audit closed only after the probe independently established:

- complete local unitarity outside the selected fixture;
- canonical, all-placement, and held-out patch covariance;
- raw-`q`-crossing rival failure;
- matrix-derived and fringe-derived `V`;
- matrix-derived trace distances and Helstrom success;
- recorder-off, intermediate, and maximal endpoints;
- pointer loss before export;
- CNOT archive survival after pointer loss;
- SWAP transfer versus redundant export;
- CNOT no-cloning failure on a nonorthogonal superposition;
- diagonal-algebra preservation and coherent-channel failure;
- no-signalling before recoupling and capability change after recoupling;
- fresh independent cells versus same-pointer fanout;
- finite rotation recurrence and counter aliasing; and
- deterministic artifact replay.

All `31/31` checks passed in two root reruns with a byte-identical artifact:

```text
c7b052e2b95b72ae5575f6e8b36706af8f4bf0d9d3f15d7263d59219b9c045c8  probe
f280617b9309af21dbceae13283dd317240ff7fe48fbe4647368ddebe79dd018  artifact
f1520f40eb8d315ed2b3ab69aaf4983acfcb883754c417a0cd225407de077b70  technical note
```

The `HC-DU-031B` regression remained `31/31`; the source-semantics,
finite-capacity, resource-gate, and interface-identifiability regressions
remained `15/15`, `16/16`, `16/16`, and `15/15`.

## 10. Claims this swing cannot earn

Even if every finite test passes, it does not establish:

- a dynamically selected record interaction;
- classical irreversibility or finality;
- a physical observer or sovereign agent;
- proper time or a dimensional clock rate;
- continuum or higher-dimensional covariance;
- geometry, gravity, cosmology, or `Lambda`;
- an unrestricted boundary-invariance law; or
- Dynamic Unity identity.

The strongest warranted result would be an exact finite construction and
equivalence hierarchy, with the archive interface and law-selection problem
left explicit.
