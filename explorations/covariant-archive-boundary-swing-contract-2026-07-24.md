---
title: "Covariant finite archive and boundary-relocation swing contract"
status: completed_research_swing
doc_type: research_swing_contract
created: 2026-07-24
directed_by: "Joe direct chat, 2026-07-24"
hardening_id: HC-DU-031C
predecessor: explorations/covariant-recorder-naturalization-swing-2026-07-24.md
run_plan: lab/process/runs/RUN-20260724-133640-covariant-archive-boundary/run-plan.md
lane: "1.5 / 2.2 / 2.4 / 4.4"
banking_authority: none
prediction_authority: none
---

# Covariant finite archive and boundary-relocation swing contract

## Why this is the next meaningful swing

`HC-DU-031B` established four exact facts:

1. a finite coherent interaction counter can be attached to the exact
   Arrighi-Facchini-Forets Clock QCA as a complete local unitary;
2. the counter is transported naturally through the source's canonical
   `q`-insertion encodings;
3. the same covariance square admits every active-sector unitary and therefore
   does not select the counter law; and
4. a recorder that distinguishes coherent histories cannot leave the complete
   source unitary channel unchanged.

The next knowledge-bearing object is consequently not another clock premise or
council. It is the smallest explicit archive interaction that turns the
qualitative backreaction statement into a measured information/interference
tradeoff and separates carrier, archive, interface, loss, and reunion.

## Source-exact host and scope

Retain the exact `1+1` Clock QCA and source-sense rectangular-patch covariance
used in `HC-DU-031B`. The source wire is

```text
H_0 = span{|q>, |0>, |1>},
```

and the finite extension replaces `|1>` by a particle carrying a finite
internal record. Encoding-added `q` symbols remain inert and transparent.

The source antecedent is:

- P. Arrighi, S. Facchini, and M. Forets, *Discrete Lorentz covariance for
  Quantum Walks and Quantum Cellular Automata*, arXiv:1404.4499.

No result may upgrade this construction-specific circuit covariance to
continuum, higher-dimensional, or empirical Lorentz invariance.

## Frozen finite record interaction

Use a two-history subspace `span{|h_0>,|h_1>}` and one finite pointer qubit
initialized to `|0_A>`. The no-event history leaves the pointer blank. The
source-effective event applies the fixed rotation

```text
R_theta =
[[ cos(theta), -sin(theta)],
 [ sin(theta),  cos(theta)]],
```

so

```text
|h_0>|0_A> -> |h_0>|a_0>,   |a_0>=|0>
|h_1>|0_A> -> |h_1>|a_1>,   |a_1>=cos(theta)|0>+sin(theta)|1>.
```

The interaction is a complete finite unitary, not only the displayed
isometry. The pointer is transported unchanged at `q` crossings. One fixed
`theta`, pointer basis, encoding family, and readout are used in every tested
patch.

The primary intermediate fixture uses `theta=pi/3`. Recorder-off
`theta=0`, maximal-record `theta=pi/2`, and additional bounded angles are
controls.

## Frozen archive export

At one explicitly declared interface, add one fresh archive qubit `E` in
`|0_E>` and apply a controlled-NOT from the pointer basis to the archive:

```text
|0_A>|0_E> -> |0_A>|0_E>
|1_A>|0_E> -> |1_A>|1_E>.
```

For a coherent pointer superposition this creates entanglement. It does not
copy an arbitrary unknown quantum state. The interface is a declared physical
boundary/readout structure; covariance of the source counter does not select
its location, basis, or coupling.

Compare:

- carrier loss before export;
- carrier loss after export;
- archive access with the carrier present;
- archive access after carrier loss; and
- a fixed source recombiner at the declared reunion surface.

If the executable fixture recombines a fixed history subspace rather than
simulating a complete spatial return, call it an interface-relative reunion.

## Frozen observables

For equal history amplitudes and pure archive states define

```text
gamma = <a_0|a_1>
V = |gamma|
D = 1/2 || |a_0><a_0| - |a_1><a_1| ||_1
  = sqrt(1-|gamma|^2).
```

`V` is the normalized source interference visibility under the fixed
recombiner. `D` is optimal binary archive-state distinguishability, with equal
priors and Helstrom success probability `(1+D)/2`.

The candidate equality is

```text
V^2 + D^2 = 1.
```

This is known wave/particle and information/disturbance structure. The run may
use it as a calibrated bridge and executable invariant, not as a novelty
claim.

## Target theorem package

### T1 — covariant finite pointer

The complete finite record interaction is unitary and inherits the same
canonical and placement-refined Clock-QCA covariance square because all added
`q` crossings transport the active state transparently. A raw
micro-crossing-count rival must fail.

### T2 — Gram-matrix reduction

For an isometry

```text
W = sum_h U P_h tensor |a_h>,
```

tracing the archive maps a source history block as

```text
P_h rho P_k -> U P_h rho P_k U* <a_k|a_h>.
```

Thus archive distinguishability and source decoherence are the same coupling
viewed through complementary outputs.

### T3 — exact pure-record complementarity

In the frozen two-history pure-state fixture,

```text
V=|gamma|,
D=sqrt(1-|gamma|^2),
V^2+D^2=1.
```

The probe must verify the formula from matrices and from the fixed reunion
fringe, not merely print the analytic values.

### T4 — boundary relocation and informative-record obstruction

An external-source representation can always be rewritten as an enlarged
internal-state representation by including the source/archive state in the
host state. This state augmentation alone is not the substantive theorem.

The useful scoped result distinguishes:

1. **history-diagonal observational equivalence:** if the declared source
   algebra contains no cross-history coherences and the archive is not
   intervened on, relocating the archive can preserve all declared
   expectations;
2. **full coherent channel equivalence:** this holds only when every relevant
   archive state has the same Gram entries required by the original source
   channel—in the unitary-source case, one fixed archive state up to an
   irrelevant common factor;
3. **interventional equivalence:** this fails whenever an allowed operation on
   the relocated archive changes a later source probability while no
   corresponding intervention exists in the external/fixed representation.

Therefore boundary relocation preserves only a declared observational
contract. An informative or intervenable relocated record obstructs full
channel or interventional invariance.

### T5 — finite resource and recurrence

For independent fresh record cells with the same overlap `gamma`,

```text
V_m = |gamma|^m,
D_m = sqrt(1-|gamma|^(2m)).
```

The archive dimension is `2^m` for `m` qubit cells, even when only a smaller
history code is occupied. Reusing one finite pointer does not produce
monotone irreversible accumulation in general: finite unitary rotation
recurs, and cyclic counters alias. Fresh blank cells, growing support, a bath
limit, coarse graining, or another irreversible ingredient must be charged.

## Executable contract

Create:

```text
tests/du_covariant_archive_boundary_probe.py
tests/artifacts/du_covariant_archive_boundary_result.json
```

The deterministic probe must include:

1. complete-unitary checks for several angles;
2. direct-gate, canonical rectangular-patch, all-placement, and held-out
   covariance checks;
3. source population and coherence calculations before and after archive
   discard;
4. matrix-derived `V`, `D`, Helstrom success, and fixed-fringe visibility;
5. exact complementarity at off, intermediate, and maximal settings;
6. carrier-loss before/after export;
7. coherent-basis export and an explicit no-cloning guard;
8. diagonal-algebra preservation and coherent-channel failure;
9. an archive intervention that changes a later source outcome;
10. fresh-cell scaling and one-cell recurrence/alias controls;
11. a raw-microstep rival that fails source refinement;
12. an arbitrary-active-unitary control showing covariance nonselection; and
13. deterministic source-pinned output.

Passing checks establish only the declared finite mathematical results.

## Adversarial audit

The root audit must try to break:

- unitarity outside the selected input fixture;
- covariance under active-symbol placement changes;
- visibility normalization;
- distinguishability convention and equal-prior assumption;
- archive survival claims after the wrong subsystem is lost;
- the distinction between coherent basis export and cloning;
- the distinction between algebraic quotient and physical trace;
- the distinction between diagonal observational, full channel, and
  interventional equivalence;
- monotone-record claims under finite unitary reuse;
- claims that a declared detector/interface was selected by the dynamics;
- novelty claims already covered by complementarity,
  information-disturbance, Stinespring dilation, open-system, or
  environmental-record literature; and
- extrapolation to physical observerhood, proper time, continuum theory,
  gravity, cosmology, or Dynamic Unity identity.

## Primary prior-art boundary

- Englert's 1996 inequality is the primary comparator for
  visibility/which-way distinguishability.
- Kretschmann, Schlingemann, and Werner
  (arXiv:quant-ph/0605009) are the primary comparator for channel
  information-disturbance and Stinespring continuity.
- Zurek (arXiv:0903.5082) is context for environmental proliferation of
  records, not evidence that this finite construction yields classical
  objectivity.

Possible novelty is limited to the exact combination of:

- a source-exact Clock-QCA finite pointer lift;
- its inert-`q` covariance closure and nonselection result;
- an explicit archive/loss/reunion receipt; and
- the carefully graded boundary-relocation obstruction.

Novelty remains `SEARCH-INCOMPLETE`.

## Terminal disposition grammar

Report all applicable scoped outcomes:

```text
COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY
INTERFACE_ONLY_ARCHIVE
ARCHIVE_BREAKS_NATURALITY
NO_LOSS_SURVIVING_RECORD
NO_NEW_DEPENDENCY_STATE
```

Then state separately:

- construction grade;
- theorem grade;
- physical interpretation grade;
- novelty grade;
- whether any claim was banked or prediction seeded.

## Publication and claim boundary

The output should be shaped as a technically serious note, but it remains a
repository research result. No claim is banked, no prediction is seeded, and
no publication priority is asserted by this contract.
