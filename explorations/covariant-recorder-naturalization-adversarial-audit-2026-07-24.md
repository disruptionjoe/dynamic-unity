---
title: "Adversarial audit — covariant recorder naturalization"
status: completed_adversarial_audit
doc_type: adversarial_research_audit
created: 2026-07-24
contract: explorations/covariant-recorder-naturalization-swing-contract-2026-07-24.md
hardening_id: HC-DU-031B
banked: false
seeded: false
novelty_status: SEARCH-INCOMPLETE
---

# Adversarial audit: covariant recorder naturalization

## Bottom line

The finite counter construction survives, but the strongest result is not
“a clock was added.”

Three statements must remain separate:

1. The inert-`q` Clock-QCA encoding admits an exact finite-dimensional
   recorder lift.
2. In fact, that covariance square is closed under an arbitrary unitary on the
   complete non-`q` sector. Exact covariance therefore does not select the
   counter law.
3. A recorder that becomes informative about coherently different histories
   cannot leave the full source channel unchanged. Perfectly readable
   which-history information removes the corresponding source interference.

The audited disposition is:

```text
COVARIANT_COUNTER_WITH_NECESSARY_BACKREACTION
```

This is an exact finite construction plus an exact quantum-information
obstruction. It is not yet an observer, irreversible memory, proper time,
continuum Lorentz symmetry, gravity, cosmology, or Dynamic Unity dynamics.

## 1. Source-exact boundary

The host is the `1+1` Clock QCA of
[Arrighi, Facchini, and Forets](https://arxiv.org/abs/1404.4499). Its wire
space has basis `|q>,|0>,|1>`. The source scattering:

- swaps `q` past either non-`q` symbol;
- fixes `q/q`, `0/0`, and `1/1`; and
- applies one declared `2 x 2` unitary coin on
  `span{|1,0>,|0,1>}`.

The canonical encoding is

```text
E_n|x> = |x>|q>^(n-1).
```

It is isometric and composition-compatible:

```text
(tensor_n E_m) E_n = E_(mn).
```

The source proves its local covariance square because the two non-`q` input
symbols meet exactly once in the rectangular patch and every other crossing
only transports a symbol through `q`.

This audit uses the source's algebraic discrete-Lorentz notion. It does not
upgrade that notion to ordinary continuum Lorentz invariance.

## 2. Closure theorem hidden inside the construction

### Theorem 1 — inert-ancilla covariance closure

Let

```text
H = C|q> direct_sum K
```

for any finite-dimensional active space `K`, and let `W` be any unitary on
`K tensor K`. Define a two-wire scattering `S_W` by

```text
S_W |q,q> = |q,q>
S_W |q,x> = |x,q>        for x in K
S_W |x,q> = |q,x>        for x in K
S_W |_(K tensor K) = W.
```

With

```text
E_n|q> = |q>^tensor n
E_n|x> = |x>|q>^(n-1),
```

`S_W` is unitary, the encoding family composes, and for every positive
`alpha,beta`:

```text
(E_beta tensor E_alpha) S_W
    = patch_(alpha,beta)(S_W) (E_beta tensor E_alpha).
```

### Proof

The two-wire basis decomposes into four mutually orthogonal sectors:

```text
C|q,q>
(C|q> tensor K)
(K tensor C|q>)
(K tensor K).
```

`S_W` is respectively the identity, a swap between the two one-`q` sectors,
and `W`; hence it is unitary.

In the encoded rectangular circuit, each incoming wire from one side crosses
each incoming wire from the other side once. There is exactly one `K-K`
crossing. It applies `W`. Every other gate swaps a `K` carrier through `q` or
fixes `q/q`. The outputs are therefore exactly the encoded outputs of `W`.
Linearity extends the basis argument to all superpositions. The displayed
definition of `E_n` also proves the composition law directly. QED.

### Consequence

The Clock QCA is the special case `K=span{|0>,|1>}` with a particular `W`.
The recorder is another special case with a larger `K`.

This is both positive and deflationary:

- a large class of finite internal interaction dynamics can be made exactly
  covariant in the source sense; and
- passing this covariance square alone cannot identify a physical clock,
  recorder, observer, or preferred update law.

Arbitrary active-symbol placements are useful local-square robustness tests.
They are not automatically a new Lorentz-transform family: a placement rule
must separately satisfy the encoding composition law. The canonical
left-placement family does.

## 3. The finite counter as a unitary lift

For `R>=2`, take

```text
K_R = span{|0>,|1_0>,...,|1_(R-1)>}.
```

The active block fixes `|0,0>` and every `|1_k,1_l>`, and maps

```text
|1_k,0> -> a|0,1_(k+1)> + b|1_(k+1),0>
|0,1_k> -> c|0,1_(k+1)> + d|1_(k+1),0>,
```

with indices modulo `R`.

### T1 — full local unitarity: survives

The active basis splits into:

- the one-dimensional `|0,0>` sector;
- the `R^2` fixed particle-particle states; and
- `R` orthogonal two-dimensional input blocks
  `span{|1_k,0>,|0,1_k>}` mapped cyclically onto the corresponding
  `k+1` output blocks by the same unitary coin.

The cyclic block permutation composed with the unitary coin is unitary.
Together with the `q` sectors in Theorem 1, this covers the complete local
basis, not only a one-particle fixture.

### T2 — algebraic source conservativity: survives with a required rename

The linear map

```text
F|q>=|q>,  F|0>=|0>,  F|1_k>=|1>
```

satisfies

```text
(F tensor F) S_(C,R) = S_C (F tensor F).
```

This is an algebraic quotient or semantics map. It preserves the source path
and coin amplitudes after counter labels are formally identified.

It is not a physical “forgetting channel”: `F` is not an isometry or
trace-preserving quantum operation. Physically discarding an orthogonal
counter label means a partial trace or dephasing channel, which behaves
differently on coherences between labels. T6 below supplies the exact
boundary.

### T3 — exact recorder naturality: survives

Theorem 1 proves the canonical covariance square for every finite `R`, every
unitary coin, and every positive patch size. No decoder or coin is refitted
per patch. Alternative placements test the same unique-active-crossing
mechanism, but only a composition-compatible placement family earns the full
transform-family language.

### T4 — effective-event count: survives at finite horizon

`q` crossings transport `1_k` without changing `k`. The only increment occurs
in the non-`q` `1_k/0` block, exactly where the source applies its effective
particle-vacuum coin. Both reflected and transmitted amplitudes carry the
same `k+1`, so a fixed-count superposition in the declared single-particle
sector retains its source interference under the sector's global
position-versus-counter factorization.

The readout is a coherent internal label. Measuring it is an intervention; it
is not already a classical, redundantly copied, irreversible record.

### T5 — finite-resource obstruction: survives

Modulo-`R` counting aliases `n` and `n+R`. Perfectly distinguishing elapsed
counts `0,...,T` needs at least `T+1` orthogonal states. Storing arbitrary
independent binary histories of length `T` needs at least `2^T`
distinguishable records.

The construction therefore buys a finite coherent counter, not free
unbounded memory. Extension by growing support must price transport, carrier
loss, archive access, and reunion readout.

## 4. No passive informative recorder

### Theorem 2 — exact passive-recorder obstruction

Let `U` be a unitary on source Hilbert space `H_S` and let

```text
V:H_S -> H_S tensor H_R
```

be an isometry representing evolution with a blank recorder. If

```text
Tr_R[V rho V*] = U rho U*
```

for every source density operator `rho`, then there is one fixed normalized
recorder state `|r_0>` such that

```text
V|psi> = U|psi> tensor |r_0>
```

for every `|psi>`. The complementary recorder channel is constant and
contains no information about the source input or history.

### Proof

For every pure `|psi>`, the reduced source output is the pure state
`U|psi>`. A bipartite pure state with a pure marginal is a product, so

```text
V|psi> = U|psi> tensor |r_psi>.
```

Apply this to two basis vectors and their nontrivial superposition. Linearity
can produce a product with the required source superposition only if the two
recorder factors are identical, including their relative phase. Repeating
over a basis makes the factor independent of `|psi>`. QED.

This is the exact zero-disturbance endpoint of the channel
information-disturbance relation; see
[Kretschmann, Schlingemann, and Werner](https://arxiv.org/abs/quant-ph/0605009).
The proof above is self-contained and narrower than their quantitative
continuity theorem.

### Two-history witness

Let two orthogonal source histories leave recorder states `|r_0>` and
`|r_1>`. For the coherent input

```text
(|h_0> + |h_1>)/sqrt(2),
```

discarding the recorder multiplies the source off-diagonal term by

```text
gamma = <r_1|r_0>.
```

Thus:

```text
source interference visibility = |gamma|
perfectly distinguishable record => gamma=0 => no cross-history interference
exact source-unitary channel     => gamma=1 => no record distinguishability.
```

The counter realizes the perfect-record endpoint whenever the two branches
have different count labels. A one-gate Clock-QCA witness already exists:
superpose a `1_0/q` no-increment branch with a `1_0/0` increment branch.
The source scattering preserves their coherent superposition, whereas the
extended scattering correlates the branches with orthogonal counter labels
`0` and `1`. Tracing or reading the counter removes the cross term.

The counter therefore preserves:

- the formal source quotient;
- source amplitudes and paths within each count branch; and
- the complete source channel on the declared single-particle sector when
  every coherent branch has the same count.

It does not preserve the source channel on arbitrary cross-count
superpositions. A local per-wire erasure channel can decohere still more by
retaining which-wire information; it is not the sector factorization used for
the fixed-count statement.

## 5. Controls and failure boundaries

| Attack | Result |
|---|---|
| complete-basis unitarity | survives by orthogonal-sector decomposition |
| nontrivial coins | survives for every unitary active block |
| held-out patch sizes | survives analytically by the unique active crossing |
| raw microscopic gate counter | fails: patch refinement changes the count |
| `q`-crossing counter | fails: encoding ancillas manufacture elapsed time |
| per-frame decoder | unnecessary and disallowed |
| cyclic alias | occurs exactly after `R` effective interactions |
| recorder off | returns the source Clock QCA and removes accessible count |
| physical counter discard | dephases cross-count coherence |
| counter measurement/copy | can read/copy an orthogonal label only with the corresponding entanglement/backreaction |
| carrier loss | loses the unexported record |
| arbitrary placement | local square survives; transform-family composition is a separate obligation |
| archive/reunion | not supplied by the local counter alone |
| classical irreversibility | not supplied by finite unitary dynamics alone |
| observer/proper time | not identified |
| higher dimension/continuum/gravity | not established |

## 6. Related-work and novelty audit

The bounded search checked:

- the exact Clock-QW/QCA source above;
- the structural QCA framework of
  [Schumacher and Werner](https://arxiv.org/abs/quant-ph/0405174);
- Vlasov's adjacent QCA scheme “with history”
  [arXiv:quant-ph/0406119](https://arxiv.org/abs/quant-ph/0406119); and
- the channel information-disturbance result cited above;
- the coherent clock-to-memory protocol in
  [*Quantum Stopwatch*](https://arxiv.org/abs/1703.05876);
- the accuracy/entropy tradeoff for
  [autonomous quantum clocks](https://arxiv.org/abs/1609.06704); and
- the measured distinction between microscopic ticks and the amplification
  cost of a macroscopic record in
  [Wadhia et al.](https://arxiv.org/abs/2502.00096).

Searches combining `Clock QCA`, Lorentz covariance, finite counters, memory,
history, recorders, and passive recording did not expose a direct match for
the combined theorem package. That is only a bounded arXiv-oriented search.

```text
novelty status: SEARCH-INCOMPLETE
```

The no-passive-recorder theorem is established quantum-information structure,
not a novelty claim. The potentially distinct contribution is the combination
of:

1. the inert-ancilla covariance-closure theorem;
2. an explicit finite interaction-counter lift of the exact Clock QCA;
3. the algebraic-quotient versus physical-forgetting distinction; and
4. the resulting record/backreaction dependency for this covariant
   construction class.

Before submission, this needs a broader literature review, independent proof
review, and careful comparison with reversible-history QCA and quantum-clock
work. The clock-memory and thermodynamic-clock literature especially prevents
the finite coherent counter from being mislabeled as a classical tick archive
or an autonomous clock.

## 7. What changes in Dynamic Unity

`HC-DU-031B` is no longer an open “can a recorder be appended?” question. It
has a constructive answer.

The live question moves one level deeper:

```text
Can a physically selected, source-sense-covariant record-forming channel
produce stable accessible records with an explicit and testable
backreaction/decoherence law, archive cost, and reunion readout?
```

The next decisive build should couple the counter to an explicit finite
archive/environment and test, under the same covariance square:

1. record distinguishability;
2. source interference visibility;
3. the exact tradeoff between them;
4. archive export and carrier-loss recovery;
5. fixed-count versus cross-count sectors;
6. resource scaling before aliasing; and
7. whether any interaction law is selected by additional DU structure rather
   than merely admitted by the covariance closure.

Do not run another broad council wave before that build or the independent
causal-post program changes the evidence.

## 8. Claim and publication grade

```text
warrant:
  constructively realized:
    - finite full-basis unitary counter
    - exact source-sense covariance
    - finite-horizon effective-interaction readout
  derived:
    - inert-ancilla covariance closure
    - finite resource bounds
    - passive informative recorder obstruction
  not established:
    - classical irreversible record
    - observer identity or proper time
    - physical law selection
    - continuum or higher-dimensional covariance
    - gravity, cosmology, Lambda, or DU identity

claim bank: none
prediction seed: none
publication readiness: TECHNICAL-NOTE-SPINE / NOT SUBMISSION-READY
```

## 9. Independent execution receipt

Root replayed the final probe twice in the repository's pinned compute
environment. Both runs passed `31/31` checks and rewrote the artifact
byte-identically:

```text
d65555ee5e8d62f50ee6f8d78d775a5a0e676c5bf13a660a95f7c739e27de243  tests/du_covariant_recorder_naturality_probe.py
42f74179477a8c9f6c1722c5da4e9d9bf54b1f23aa87325b8c766b5bfa41362d  tests/artifacts/du_covariant_recorder_naturality_result.json
```

The replay used `.venv/bin/python`; the system Python lacked NumPy and was not
treated as a scientific failure. JSON parsing, Python compilation, YAML
manifest revision checks, and `git diff --check` also passed.
