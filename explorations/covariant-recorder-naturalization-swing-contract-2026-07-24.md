---
title: "Covariant recorder naturalization swing contract"
status: completed_research_swing
doc_type: research_swing_contract
created: 2026-07-24
directed_by: "Joe direct chat, 2026-07-24"
hardening_id: HC-DU-031B
predecessor: explorations/science-council-five-persona-premise-free-foundational-wave-synthesis-2026-07-24.md
lane: "1.5 / 2.2 / 2.4 / 4.4"
banking_authority: none
prediction_authority: none
---

# Covariant recorder naturalization swing contract

## Why this is the one concentrated swing

The fifth Science Council wave changed the record-clock dependency:

- exact Clock-QCA circuit covariance is a positive source antecedent;
- its published countdown and keep-going signals do not entail accumulated
  observer memory;
- finite record capacity and record identity now have exact resource and
  interface constraints; and
- another general premise/council wave is stopped until direct construction
  changes the evidence.

The highest combined purpose, profundity, usefulness, novelty, and
publishability opportunity is therefore to construct—or sharply obstruct—the
first explicit recorder extension of the exact Clock QCA.

This swing follows one research spine. It does not fan out into several
unrelated branches.

## Primary question

Can the exact `1+1` Clock-QCA covariance square be extended by one finite,
readable interaction counter whose state:

1. advances once per source-effective `|1>-|0>` scattering;
2. does not advance on encoding-added `|q>` crossings;
3. is transported by the same physical encoding in every admitted frame;
4. preserves the original Clock-QCA dynamics after forgetting the counter;
5. remains readable after propagation and reunion; and
6. exposes, rather than hides, the resource price of a finite or unbounded
   record?

If yes, the result is a covariant coherent interaction counter. It is not
automatically a classical irreversible record, an observer, proper time, or a
Dynamic Unity law.

## Source-exact host

Use the Clock QCA of Arrighi, Facchini, and Forets, not a generic substitute.
Its wire Hilbert space has basis:

```text
|q>, |0>, |1>.
```

The `9 x 9` scattering unitary `U_C`:

- stabilizes or transports the `q/0` vacuum pairs;
- transports `1` through `q`;
- leaves `1/1` unchanged; and
- applies a fixed `2 x 2` unitary
  `C=[[a,b],[c,d]]` on the ordered subspace
  `span{|1,0>, |0,1>}`.

The source encoding is:

```text
E_alpha |x> = |x> |q>^(alpha-1),
```

with the source explicitly noting that the active symbol may be placed
elsewhere among the `q` ancillas. The source covariance relation is:

```text
(E_beta tensor E_alpha) U_C
    = Ubar_C (E_beta tensor E_alpha),
```

where `Ubar_C` is the rectangular patch of local scatterings.

Primary source:
[Arrighi, Facchini, and Forets, *Discrete Lorentz covariance for Quantum
Walks and Quantum Cellular Automata*](https://arxiv.org/abs/1404.4499).

## Candidate extension frozen before execution

For finite counter size `R >= 2`, replace the particle symbol with `R`
counter-carrying particle species:

```text
H_R = span{|q>, |0>, |1_0>, ..., |1_(R-1)>}.
```

Define `U_(C,R)` on basis sectors:

```text
q/0 vacuum sector:       same rules as U_C
1_k/q sector:            particle and counter propagate through q
1_k/1_l sector:          identity

|1_k,0> -> a|0,1_(k+1)> + b|1_(k+1),0>
|0,1_k> -> c|0,1_(k+1)> + d|1_(k+1),0>,
```

where `k+1` is modulo `R`.

Use the extended encoding:

```text
E_alpha^R |x> = |x>|q>^(alpha-1)
```

for every extended alphabet symbol `x`, plus held-out placement variants
`E_(alpha,s)^R` that put the one active symbol at position `s`.

The forgetful map sends `|1_k>` to `|1>` and fixes `|q>,|0>`.

## Target theorem package

The swing should prove or refute each part:

### T1 — local unitarity

`U_(C,R)` is unitary whenever `C` is unitary. The proof must cover the complete
extended two-wire basis, not only the selected one-particle fixture.

### T2 — source conservativity

Forgetting the counter intertwines the extended scattering with `U_C` on the
declared source sector. The recorder may enrich the state but may not change
the source amplitudes or particle paths.

### T3 — exact recorder naturality

For every tested and analytically admitted `alpha,beta` and placement:

```text
(E_beta^R tensor E_alpha^R) U_(C,R)
    = Ubar_(C,R) (E_beta^R tensor E_alpha^R)
```

on the complete declared encoded input space. One fixed `C`, counter rule,
encoding family, and readout must be used. A decoder refitted per frame is a
failure.

### T4 — event-count correctness

On the single-particle valid sector, the counter advances once for each
source-effective `1/0` interaction and not for `q` crossings introduced by
refinement. Its readout is therefore invariant under the admitted source
encoding at horizons before aliasing.

### T5 — finite-resource obstruction

The counter aliases after `R` effective interactions. Perfect elapsed-count
readings `0..T` require `R >= T+1`; exact independent binary event history
requires at least `2^T` distinguishable histories. Unbounded exact memory
therefore needs unbounded local dimension, growing spatial support/export, or
weaker/approximate semantics.

### T6 — passive-recorder obstruction

Test the stronger global meaning of “source conservativity.”

Let an isometry `V:H_S -> H_S tensor H_R` append a blank recorder to a source
unitary `U`. If

```text
Tr_R[V rho V*] = U rho U*
```

for every source state `rho`, then the reduced source channel is a pure unitary
channel. Stinespring uniqueness/extremality should force

```text
V|psi> = U|psi> tensor |r_0>
```

up to a fixed recorder state, so the recorder cannot contain nonconstant
information about the input or history.

The finite counter candidate can still conserve source amplitudes locally and
on fixed-event-count sectors. But if coherent branches accumulate different
counter values, the counter becomes which-history information; tracing or
reading it dephases the source interference. The probe must construct the
smallest two-history interference witness.

This is not a defect to conceal. If established, it is a central result:

> a nontrivial readable record cannot be an epiphenomenal appendage to every
> coherent source history; it must backreact, induce an effective
> superselection/decoherence, use a restricted sector, or cease to be
> informative.

## Exact executable probe

Build:

```text
tests/du_covariant_recorder_naturality_probe.py
tests/artifacts/du_covariant_recorder_naturality_result.json
```

The probe must:

1. construct the complete finite scattering matrices for several nontrivial
   unitary coins and `R`;
2. verify exact or tolerance-controlled unitarity;
3. enumerate the complete extended basis for local source conservativity;
4. simulate rectangular crossing patches on sparse state dictionaries;
5. test all placements for bounded `alpha,beta`, with a held-out larger patch;
6. test linearity on superpositions, not only classical basis paths;
7. compare the counter readout before and after encoding;
8. include a raw-micro-crossing counter that fails refinement;
9. include a cyclic-alias counterexample;
10. include recorder-off and source-forgetting controls;
11. include the T6 two-history interference witness and distinguish local or
    fixed-count conservativity from global channel equality;
12. include copied-carrier and reunion readouts if they add real
    discrimination; and
13. write a deterministic, source-pinned JSON artifact.

Passing execution is not a physical claim.

## Adversarial audit

The same object must face:

- a full-basis unitary check rather than a selected-subspace isometry;
- alternative active-symbol placements allowed by the source;
- arbitrary nontrivial unitary coins rather than one favorable coin;
- a raw gate-count rival;
- a counter that increments on `q` ancillas;
- finite cyclic aliasing;
- a per-frame decoder/gate refit;
- counter superpositions and entanglement with particle path;
- no-cloning and classical-readout overclaims;
- loss of the counter carrier;
- source dynamics with the recorder forgotten;
- higher-dimensional, continuum, gravity, and proper-time overreach; and
- prior-art/novelty search.

Any failed theorem must be scoped to the exact failed construction. Do not
turn a construction failure into a universal no-go.

## Publication-shaped output

Create:

```text
explorations/covariant-recorder-naturalization-swing-2026-07-24.md
```

It should read as the technical spine of a possible short research note:

1. abstract;
2. source antecedent;
3. problem and definitions;
4. theorem statements and proofs;
5. exact computational receipt;
6. countermodels and limitations;
7. novelty/related-work audit;
8. physical interpretation;
9. implications for Dynamic Unity;
10. next decisive experiment; and
11. honest claim-grade and publication readiness.

Novelty must be labeled `SEARCH-INCOMPLETE` unless a broader literature review
supports more.

## Decision outcomes

- `FINITE_COVARIANT_COUNTER_CONSTRUCTED`: T1–T5 survive. Advance to a
  classicalization/archive/reunion experiment.
- `COVARIANT_COUNTER_WITH_NECESSARY_BACKREACTION`: the finite counter is
  exactly natural and readable, while T6 proves that informative cross-history
  records cannot preserve the full coherent source channel. Advance the
  backreaction/decoherence law as the physical target.
- `SOURCE_CONSERVATIVE_BUT_NONNATURAL`: local counter works but covariance
  fails. Preserve the first counterexample and stop this recorder.
- `NATURAL_ONLY_WITH_FRAME_REFIT`: reject; the encoding/decoder does the work.
- `SELECTED_SECTOR_ONLY`: useful conditional isometry, not a QCA extension.
- `SOURCE_DYNAMICS_CHANGED`: reject as an extension of the cited host.
- `NO_NEW_DEPENDENCY_STATE`: stop the mode and do not produce another roadmap.

No outcome by itself banks a physics claim or seeds a prediction.

## Ownership and coordination

One formal lead may create only the swing memo, uniquely named probe, and
artifact. Root owns the contract, source/novelty audit, adversarial
reproduction, shared-state integration, memory, Git history, and publication
decision.

## Execution closure

The frozen candidate passed T1–T5 in their stated finite mathematical scope.
T6 also passed as an obstruction: global physical source-channel
conservativity is incompatible with a nonconstant readable record. The
algebraic quotient remains exact, and fixed-count coherent sectors retain the
source channel, but distinguishable cross-count records suppress the matching
source interference.

The bounded probe passed `31/31` checks twice with byte-identical artifact
SHA-256:

```text
42f74179477a8c9f6c1722c5da4e9d9bf54b1f23aa87325b8c766b5bfa41362d
```

An actual controlled-add unitary establishes copyability of orthogonal finite
counter labels with a charged second register and confirms the no-cloning
boundary for coherent inputs. Spatial archive transport and reunion were not
simulated and remain explicitly open.

Final disposition:

```text
COVARIANT_COUNTER_WITH_NECESSARY_BACKREACTION
```

The resulting next build is `HC-DU-031C`, not another premise wave.
