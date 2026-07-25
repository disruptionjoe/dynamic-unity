---
title: "Formed-sharp descent: quantum-selection hostile gate"
status: completed_hostile_gate
date: 2026-07-25
run_id: RUN-20260725-110735-formed-sharp-descent
claim_grade: "EXACT FINITE CONTROLS + KNOWN STRUCTURAL COLLISION / NO QUANTUM SELECTION / REOPENER PRECISE"
implementation:
  - ../tests/du_formed_sharp_quantum_selection_probe.py
artifact:
  - ../tests/artifacts/du_formed_sharp_quantum_selection_result.json
program_refs:
  - HC-DU-033
  - HC-DU-035C
  - HC-DU-039
  - H-CCR-01
  - H-CCR-16
---

# Formed-Sharp Descent: Quantum-Selection Hostile Gate

## Hard answer

The current formed-sharp program contains a real route to excluding a named
post-quantum class, but that exclusion is already occupied mathematics and the
route has not yet been physically derived.

The exact disposition is:

```text
contextwise formed pointer/archive
    is too weak;

system-level repeatable minimally disturbing sharpness
    is known sharp-measurement structure;

pairwise-to-global descent for sharp measurements
    is Specker's principle / known joint-measurability structure;

almost-quantum exclusion under Specker
    is known;

ordinary quantum theory uniquely selected
    is not established.
```

The most important result of this gate is a fork:

1. If physical formation means that **each measurement context separately**
   has some sharp dilation and durable pointer, then it selects nothing
   relevant to descent. Every finite quantum POVM has such a Naimark dilation.
2. If physical formation means that **one common commuting sharp dilation**
   exists across the entire cover, the condition is already equivalent to
   global joint measurability. It assumes the descent result unless the
   common dilation is independently selected by the physical dynamics.

So the missing theorem is not “sharp things glue.” It is:

> A frozen physical process, without looking at the desired global joint
> measurement, selects one context-independent dilation, overlap instrument,
> provenance structure, and stable archive algebra across the full cover.

No result in this branch supplies that theorem.

## Four meanings of “sharp” that must not be merged

| Type | Meaning | What it does not imply |
|---|---|---|
| Archive reread | A classical pointer/archive bit can be read twice with the same value | That the system measurement is repeatable, nondisturbing, projective, or context-independent |
| Contextwise dilation sharpness | A POVM in one context is realized by a PVM on a larger system plus environment | That the same dilation, environment, or pointer algebra works in another context |
| Ideal-measurement sharpness | An instrument is repeatable and minimally disturbs every compatible future measurement | A novel Dynamic Unity definition; this is established GPT sharpness terrain |
| System-level PVM sharpness | In finite-dimensional quantum theory the effects are orthogonal projectors and the ideal instrument is Lüders | That Hilbert space, projectors, the basis, or the coupling was derived from records |

Chiribella and Yuan define GPT sharp instruments through repeatability and
minimal disturbance, and state that in quantum theory the resulting sharp
instruments are Lüders instruments and the sharp measurements are projective
([primary source](https://arxiv.org/abs/1404.3348)). Therefore, if the
physical-formation branch returns only those conditions inside an already
supplied quantum model, the mathematical sharpness result is absorbed. The
remaining Dynamic Unity question is whether the physical interaction selects
which instrument satisfies them without supplying its PVM or basis.

The distinction between archive reread and instrument repeatability is
load-bearing. The finite Specker control below has exactly repeatable
context-local archives. That does not make the three measurements one
repeatable, minimally disturbing system-level family.

## Structural Specker versus statistical CE

The previous frontier gate recovered the probability-level principle
Local Orthogonality/Consistent Exclusivity:

```text
pairwise exclusive event probabilities sum to at most one.
```

Almost-quantum correlations satisfy LO/CE
([Navascués et al.](https://arxiv.org/abs/1403.4621)). Hence that statistical
condition cannot select ordinary quantum correlations.

Specker's principle is stronger and lives at measurement level:

```text
pairwise jointly measurable sharp measurements
    imply
one global joint measurement.
```

For sharp quantum observables, pairwise joint measurability implies global
joint measurability
([Heinosaari, Reitzner, and Stano](https://arxiv.org/abs/0811.0783)).
Gonda et al. prove that no theory yielding the almost-quantum correlations can
satisfy Specker's principle
([journal article](https://doi.org/10.22331/q-2018-08-27-87);
[preprint](https://arxiv.org/abs/1712.01225)).

That yields a valid conditional implication:

> If Dynamic Unity independently derives a theory-general formed-record
> principle that entails Specker's principle, it excludes the
> almost-quantum class.

It does **not** yield a new quantum selector:

- the almost-quantum exclusion is Gonda et al.'s result;
- the quantum sharp-observable implication is established;
- excluding almost quantum does not characterize every quantum state,
  transformation, composite, or correlation;
- other GPT and reconstruction foils remain; and
- deriving repeatability inside standard Hilbert-space quantum mechanics
  does not constrain a hypothetical almost-quantum GPT.

The potential Dynamic Unity contribution is therefore a physical derivation
of the applicability of Specker's principle, with provenance, access,
resources, and recursive action semantics. The abstract exclusion itself is
occupied terrain.

## Dilation-fork no-go

The sharp-dilation route has two endpoints and no established noncircular
middle.

### Contextwise endpoint: universal and too weak

For every finite POVM \(\{E_a\}\), Naimark dilation supplies an isometry
\(V\) and projectors \(\{P_a\}\) on a larger space such that

\[
E_a=V^\dagger P_aV.
\]

A context can therefore have:

- orthogonal pointer states;
- an exactly copied classical archive;
- a repeatable archive reread; and
- a sharp PVM on the enlarged boundary,

even when the induced measurements on the original system belong to a
pairwise-compatible but non-global Specker family. Contextwise “a sharp record
formed somewhere” cannot imply full-cover descent.

### Full-cover endpoint: equivalent to the target

Joint measurability of POVMs can be characterized by commuting Naimark
dilations in one common Hilbert space
([Beneduci](https://arxiv.org/abs/1404.1477)). Thus requiring a common
commuting dilation for the full cover already requires the global joint
measurement in dilation language.

The resulting no-go candidate is:

> **Dilation-Fork Lemma.** Contextwise sharp dilatability is universal and
> does not imply global descent. Full-cover common commuting dilatability is
> equivalent to global joint measurability. Consequently, a
> formation-to-descent theorem is noncircular only if physical dynamics
> independently selects a common cross-context dilation identity before the
> global compatibility verdict is evaluated.

The component mathematics is known. The useful Dynamic Unity result is the
dependency: boundary enlargement cannot by itself earn formed-sharp descent.

## Exact finite controls

The deterministic probe returns `16/16`.

### Ordinary projective target

Three binary coordinate PVMs on an eight-point sample space have:

- commuting idempotent projector supports;
- normalized pairwise joints;
- one global eight-atom joint; and
- context-independent outcome identity.

This is a constructive admission control for an ordinary commuting
projective family. It is not a derivation of all quantum structure.

### Perfect Specker anti-correlation

Freeze three pair records:

\[
A\ne B,\qquad B\ne C,\qquad C\ne A,
\]

with each allowed unequal pair carrying probability \(1/2\). Every one-site
marginal is uniform and agrees across contexts. Every context's pair outcome
can be copied to a pointer and reread from an archive exactly.

Yet no binary assignment satisfies all three constraints. The cover has no
global extension.

If the six occurrences

\[
A_{AB},B_{AB},B_{BC},C_{BC},C_{CA},A_{CA}
\]

are treated as different physical variables, an eight-point global
completion exists and reproduces every pair archive. This is the exact
permissive absorber:

```text
local record formation
    + archive repeatability
    + matching one-site probabilities
    !=
formed cross-context identity
    !=
global descent.
```

### A standard-quantum Specker triangle

The probe also freezes the equally noisy binary qubit POVMs

\[
E^{(i)}_a=\frac12(I+a\eta\sigma_i),
\qquad
i\in\{X,Y,Z\},
\qquad
\eta=\frac23.
\]

For every orthogonal pair, the explicit four-outcome joint

\[
G^{(ij)}_{ab}
=\frac14\left(I+a\eta\sigma_i+b\eta\sigma_j\right)
\]

is positive because

\[
2\eta^2=\frac89<1.
\]

The three equally noisy orthogonal observables are triplewise jointly
measurable exactly when

\[
3\eta^2\leq1.
\]

Here

\[
3\eta^2=\frac43>1,
\]

so they are pairwise jointly measurable but not triplewise jointly
measurable. The necessary-and-sufficient orthogonal-triple criterion is due
to the standard qubit joint-measurement literature; see
[Yu and Oh](https://arxiv.org/abs/1312.6470). The executable verifies the
exact specialization and explicit pair marginals; it does not present the
general literature theorem as a newly computed result.

This control is decisive against a loose formation claim. It lives inside
ordinary quantum theory. Every pair can be physically measured and archived;
what fails is one global sharp system-level instrument.

## Landscape disposition

| Role | Frozen class |
|---|---|
| Restrictive foil | One noncontextual preassigned global value for every repeated occurrence |
| Target | Ordinary quantum theory with physically formed projective/Lüders instruments |
| Permissive foil 1 | Pairwise-compatible, non-global unsharp quantum Specker triangle |
| Permissive foil 2 | Almost-quantum correlations, which survive probability-only LO/CE |
| Candidate selector | One predeclared provenance-preserving physical dilation and overlap instrument, natural across the full context cover |
| Strongest absorber | Sharp-measurement theory, Naimark/common-dilation joint measurability, Specker, and Gonda's almost-quantum exclusion |

The gate verdict is:

```text
CONTEXTWISE FORMATION: TOO WEAK
SUPPLIED SYSTEM PVM SHARPNESS: KNOWN
FULL-COVER COMMON DILATION: EQUIVALENT TO JOINT MEASURABILITY
ALMOST-QUANTUM EXCLUSION UNDER SPECKER: KNOWN
QUANTUM SELECTION: NOT DERIVED
```

## Exact reopener

The frontier should reopen only if the physical branch supplies a predicate
\(\mathsf F\) satisfying all of the following without inspecting the desired
global joint:

1. **Theory-independent operational meaning.** The same formation,
   repeatability, disturbance, access, and provenance contract applies to the
   target and permissive theory classes.
2. **Context-independent physical identity.** Repeated overlap outcomes have
   the same selective map and held-out continuations under one fixed
   dilation/interface, not merely equal effects or probabilities.
3. **No dilation refit.** Ancilla, initial state, coupling family, pointer
   algebra, environment boundary, and validity rule are frozen before context
   selection.
4. **Benign-refinement naturality.** Adding an inert relay or representational
   ancilla does not change whether the instrument is formed sharp.
5. **Resource closure.** Blank archives, coherence, memory, environment,
   switching controls, and readout access are charged across the boundary.
6. **Structural consequence.** Pairwise \(\mathsf F\)-compatible instruments
   entail or obstruct one global action-sufficient instrument for a reason
   stronger than writing down a common commuting dilation.

If those conditions entail Specker's principle, almost quantum is
conditionally excluded by the known Gonda theorem. A further outer foil is
still required before calling the result quantum selection.

## Held-out discriminator

The most informative next physical discriminator is a **coherently switched
overlap-instrument assay**:

1. implement the three pairwise contexts with explicit system, pointer,
   archive, switching control, and retained environment;
2. coherently choose between the two implementations of each repeated
   measurement occurrence, such as \(A\) inside \(AB\) versus \(A\) inside
   \(CA\);
3. hold its outcome effect and local archive statistics fixed;
4. recombine the context-control path and retain every which-context port;
5. tomography-check equality of the selective maps and held-out sequential
   continuations under one frozen isometry; and
6. only after that identity receipt, test the three-way continuation.

This can expose context leakage or implementation refit that terminal record
statistics miss. A positive result would establish a formed overlap identity
inside the declared model, not yet a new quantum law. A negative result would
confirm that pairwise archives were never one common formed-sharp family.

The assay is intentionally stronger than rereading a pointer and weaker than
simply asking whether a global joint POVM exists. Whether that intermediate
physical identity condition is sufficient for global descent is the actual
theorem opportunity.

## Program consequence

Do not promote a “finality selects quantum” law from this swing.

Retain:

- the dilation-fork dependency as an exact hostile control;
- the noisy-Pauli Specker triangle as the standard-quantum permissive foil;
- Gonda's theorem as the occupied almost-quantum exclusion;
- the coherent overlap-instrument assay as the held-out discriminator; and
- formed, ideal, system-PVM, and contextwise-dilation sharpness as separate
  types.

No theorem ID, hypothesis ID, prediction, physical law, ontology, paper
priority, or claim grade is promoted by this branch.

## Reproducibility

Run:

```bash
python3 tests/du_formed_sharp_quantum_selection_probe.py
```

Expected result:

```text
formed-sharp quantum-selection hostile gate: 16/16 checks passed
CONTEXTWISE_FORMATION_TOO_WEAK__FULL_COVER_COMMON_DILATION_IS_JOINT_MEASURABILITY__NO_QUANTUM_SELECTION_DERIVED
```
