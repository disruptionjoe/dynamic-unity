---
title: "A covariant coherent interaction counter and the cost of making it a record"
status: completed_research_swing
doc_type: technical_research_note_spine
created: 2026-07-24
hardening_id: HC-DU-031B
contract: explorations/covariant-recorder-naturalization-swing-contract-2026-07-24.md
primary_source: "Arrighi, Facchini, and Forets, arXiv:1404.4499"
verdict: COVARIANT_COUNTER_WITH_NECESSARY_BACKREACTION
claim_grade: "EXACT FINITE MATHEMATICAL CONSTRUCTION AND OBSTRUCTION / PHYSICAL IDENTIFICATION OPEN"
novelty: SEARCH-INCOMPLETE
banked: false
seeded: false
---

# A covariant coherent interaction counter and the cost of making it a record

## Abstract

We extend the exactly discrete-Lorentz-covariant `1+1` Clock quantum cellular
automaton of Arrighi, Facchini, and Forets by replacing its particle symbol
`|1>` with finitely many counter-carrying species `|1_k>`. The counter advances
modulo `R` at each source-effective `|1>-|0>` scattering and is transported
unchanged through the quiescent `|q>` symbols inserted by the source encoding.

The local extension is unitary on its complete two-wire Hilbert space. It
inherits the source rectangular-patch covariance square for every finite
counter size, every unitary source coin, and the canonical composable
`q`-insertion encodings. In fact, this is an instance of a stronger closure
lemma: **every** unitary active block on
`H = C|q> direct-sum K` inherits the same local square when `q` crossings are
transparent. Covariance therefore permits the counter, but does not select it.

The extension conserves the source in two weaker, exact senses: an algebraic
quotient `|1_k> -> |1>` intertwines the complete local matrices, and physical
partial trace preserves the source channel on sectors in which every coherent
branch has the same event count. The strongest passive-recorder reading is
false. If a recorder stores different orthogonal values on coherent histories
with different event counts, tracing or reading it removes the corresponding
source interference. More generally, an isometric extension whose reduced
source channel is the same unitary for every input must leave its recorder in
one input-independent state. An informative record cannot be an epiphenomenal
appendage to all coherent histories.

The executable receipt reports `31/31` checks, including nine complete local
unitaries, `12,300` bounded full-basis placement tests, a held-out `6 x 5`
patch, complex counter superpositions, a dense arbitrary-active-block
control, a unitary refinement-breaking rival, cyclic aliasing, recorder-off,
controlled-copy, loss, and no-cloning controls. This constructs a finite
covariant **coherent interaction counter** and a sharp backreaction
obstruction. It does not yet construct a classical irreversible record,
observer-owned archive, proper time, continuum theory, or Dynamic Unity law.

## 1. Source antecedent and exact scope

The host is the Clock QCA in:

- [P. Arrighi, S. Facchini, and M. Forets, *Discrete Lorentz covariance for
  Quantum Walks and Quantum Cellular Automata*](https://arxiv.org/abs/1404.4499).

The downloaded primary TeX used in this swing has SHA-256
`121ccb1e66c5e408c4a659c66a9873e8d0544655e0a28ccd920e3f407ed1fdfb`;
the downloaded PDF has SHA-256
`578c156f25fb9b2698bca5f6f27d43e7e1c09ee884a64f78e9f1e2515b0cebc4`.
The relevant source definition and proof are TeX lines `930–981`.

The source wire space is

```text
H_0 = span{|q>, |0>, |1>}.
```

`|q>` and `|0>` are distinct vacuum symbols and `|1>` is the particle symbol.
The local `9 x 9` scattering `U_C`:

```text
swaps q past 0 or 1,
fixes q/q, 0/0, and 1/1,
and applies C on span{|1,0>, |0,1>}.
```

For `C=[[a,b],[c,d]]`, the source writes

```text
|1,0> -> a|0,1> + b|1,0>
|0,1> -> c|0,1> + d|1,0>.
```

In the standard row-output/column-input matrix convention the displayed block
is `C^T`, which is unitary whenever `C` is unitary.

The canonical encoding is

```text
E_n |x> = |x>|q>^(n-1).
```

The exact source proof replaces one scattering by a rectangular patch of
local scatterings. Its planar boundary convention places the first active
input on an `alpha`-wire incoming boundary and the second on a `beta`-wire
incoming boundary; the first output exits on the `beta` boundary and the
second on the `alpha` boundary. This is the meaning implemented by the
executable braid:

```text
E_alpha(x) tensor E_beta(y)
      -- alpha*beta local crossings -->
E_beta(first output) tensor E_alpha(second output).
```

After the source's boundary naming is restored, this is its abstract
covariance equation

```text
(E_beta tensor E_alpha) U_C
    = Ubar_C (E_beta tensor E_alpha).
```

The source establishes this scoped `1+1` circuit covariance. It does not
establish an accumulated record, proper time, continuum Lorentz invariance,
or higher-dimensional physics.

## 2. Frozen extension and distinctions

For an integer `R >= 2`, define

```text
H_R = span{|q>, |0>, |1_0>, ..., |1_(R-1)>}.
```

The frozen `U_(C,R)` retains the source rules with these changes:

```text
|1_k,q> -> |q,1_k>
|q,1_k> -> |1_k,q>
|1_k,1_l> -> |1_k,1_l>

|1_k,0> -> a|0,1_(k+1)> + b|1_(k+1),0>
|0,1_k> -> c|0,1_(k+1)> + d|1_(k+1),0>,
```

where every counter index is modulo `R`.

The declared readout is the species label `k`. It is fixed across every
admitted encoding. No per-frame decoder is allowed.

Three operations called “forgetting” have different mathematical content:

1. **Algebraic quotient.** The linear map
   `F|q>=|q>`, `F|0>=|0>`, `F|1_k>=|1>` collapses counter species. It is not
   isometric: orthogonal `|1_0>` and `|1_1>` both map to `|1>`.
2. **Fixed-count physical trace.** On the exact-one-particle sector, particle
   path and its internal counter factor as `H_path tensor H_counter`. If every
   coherent branch has the same event count, the counter state factorizes and
   tracing it preserves the source state.
3. **Cross-count physical trace.** If coherent branches have different event
   counts, the counter is which-history information. Tracing it generally
   dephases the source.

The result depends on keeping these three distinct.

## 3. Theorem package

### T1 — complete local unitarity

**Theorem 1.** `U_(C,R)` is unitary on `H_R tensor H_R` for every finite
`R >= 2` and every unitary `C`.

**Proof.** Write

```text
H_R = C|q> direct-sum K_R,
K_R = span{|0>, |1_0>, ..., |1_(R-1)>}.
```

The `q/q` line is fixed. The mutually orthogonal sectors
`|q> tensor K_R` and `K_R tensor |q>` are swapped, so their joint restriction
is unitary.

It remains to inspect `K_R tensor K_R`. The `|0,0>` line is fixed, as is every
`|1_k,1_l>` line. For each `k`, let

```text
V_k = span{|1_k,0>, |0,1_k>}.
```

The spaces `V_k` are mutually orthogonal and exhaust the remaining sector.
`U_(C,R)` maps `V_k` to `V_(k+1)` by the unitary block `C^T`. Thus the
restriction is a cyclic permutation of orthogonal two-dimensional spaces
composed with a unitary on each space. Every summand is unitary and the
summands are orthogonal. Therefore the complete map is unitary. `QED`

This is a full QCA-wire extension, not merely an isometry on the selected
single-particle fixture.

### T2 — exact algebraic conservativity and its physical boundary

**Proposition 2a.** On the complete local extended basis,

```text
(F tensor F) U_(C,R) = U_C (F tensor F).
```

**Proof.** On `q` transport, vacuum, and particle-particle sectors the two
sides apply the same source rule after counter labels are erased. On either
`V_k` input, both extended output branches carry `k+1`; erasing that label
returns exactly the source `C^T` amplitudes and paths. Basis equality extends
linearly. `QED`

The executable checks every extended two-wire basis vector for
`R in {2,3,5}` and three nontrivial coins: `270` cases with zero defect.
It separately compares the recorder-off source `9 x 9` gate with the
blank-counter extension on all nine source basis inputs. Amplitude and path
probability defects are both zero; only the extension exposes a stored `k`.

This proposition is not a physical all-state reduced-channel equality because
`F` is not an isometry or a trace-preserving quantum channel.

**Proposition 2b.** On any exact-one-particle coherent sector whose branches
all undergo the same number `n` of effective interactions, the extended state
factorizes as

```text
U_source|psi> tensor |k+n mod R>.
```

Physical partial trace of the counter therefore preserves the source state on
that sector.

The executable positive control superposes `|1_0,0>` and `i|0,1_0>`. Both
branches increment once. The traced extended output and the ideal source
output have trace distance zero.

The unrestricted physical statement is refuted by T6 below.

### T3 — exact recorder naturality and a stronger closure lemma

The counter's covariance follows from a more general structural fact.

**Theorem 3 (q-transparent lifting lemma).** Let

```text
H = C|q> direct-sum K
```

for any finite-dimensional `K`, and let `W` be any unitary on
`K tensor K`. Define `S_W` by

```text
S_W |q,q> = |q,q>
S_W |q,x> = |x,q>          for x in K
S_W |x,q> = |q,x>          for x in K
S_W restricted to K tensor K = W.
```

Then:

1. `S_W` is unitary;
2. the canonical encodings `E_n(x)=x q^(n-1)` are isometric and satisfy
   `(tensor_n E_m)E_n=E_(mn)`; and
3. the `alpha x beta` rectangular patch of `S_W` obeys the exact source
   covariance square on the complete encoded input space.

**Proof.** The four orthogonal sectors

```text
C|q,q>,
|q> tensor K,
K tensor |q>,
K tensor K
```

are respectively fixed, swapped in pairs, and acted on by `W`, proving
unitarity.

For the encoding composition, expanding one active factor and `n-1`
quiescent factors, then expanding each by `m`, produces exactly one active
factor followed by `mn-1` quiescent factors.

For patch naturality, first take an encoded basis input. If both source symbols
are `q`, every local crossing is `q/q`. If exactly one lies in `K`, transparent
swaps transport it through the patch. If both lie in `K`, transparent swaps
route the two active carriers to one unique active-active crossing, where
`W` acts exactly once; all other crossings only route its outputs through
`q`. The patch output is therefore the encoded direct output. Basis equality
extends to every superposition by linearity. `QED`

The frozen recorder is precisely this construction with

```text
K = span{|0>, |1_0>, ..., |1_(R-1)>}
```

and `W` equal to its active block. Hence its canonical recorder-naturality
square is exact, with one counter rule and one readout in every frame.

This theorem has a crucial negative interpretation:

> q-insertion covariance is a closure property, not a physical selector.

It admits the cyclic counter, but also every other unitary active block. The
physical burden moves to sourcing the interaction, identifying the record
interface, and explaining classicalization, accessibility, and resources.

The source notes that an active symbol could be placed elsewhere among the
`q` ancillas. The same local square holds for every tested placement: the
active strands meet once and exit at the corresponding boundary positions.
However, an arbitrary placement choice at each `n` is not automatically a
composable Lorentz-transform family. For example, “put the active symbol at
index one for every `n>=2`” sends `E_2` followed by `E_2` to index three,
whereas its declared `E_4` uses index one. Thus:

```text
canonical placement: exact covariance family;
all placements: exact local-square robustness;
arbitrary dimension-by-dimension placement selector: family status open
unless its composition law is proved.
```

### T4 — event-count correctness

**Proposition 4.** On the valid single-particle sector:

- every source-effective `1_k/0` scattering increments `k` once on every
  output path;
- every `1_k/q` crossing transports `k` unchanged; and
- before the first alias, readout `k` equals the number of effective
  interactions since initialization.

**Proof.** The two vectors spanning `V_k` are both mapped into `V_(k+1)`,
regardless of the coin amplitudes. Thus a coherent path superposition remains
entirely in one counter sector after each effective event. The `q` rules
preserve the counter index. Induction on the event number proves the claim.
`QED`

The executable repeats the event for a nontrivial complex coin and verifies
the complete counter support through and beyond the first alias. It also
checks patches `(1,1)`, `(2,3)`, `(4,2)`, and held-out `(6,5)`; all expose
counter support `{1}` after one effective interaction.

A deliberately stronger locally unitary rival increments the particle counter
at every `q` crossing. It reads `1` for `beta=1` and `4` for `beta=4`, producing
an exact naturality defect of `1`. Reporting one event then requires
frame-dependent decoder offsets `0`, `10`, and `8` modulo `11` for
`beta=1,2,4`. No one fixed offset works. This kills the raw-micro-crossing
counter without killing the effective-interaction counter.

### T5 — finite-resource obstruction

**Theorem 5.**

1. The frozen counter aliases event numbers `n` and `n+R`.
2. Perfect exact readings `0,...,T` require at least `T+1` mutually
   distinguishable record states.
3. Perfect storage of every independent `T`-bit event history requires at
   least `2^T` mutually distinguishable record states.

**Proof.** Part 1 follows from the modulo-`R` update. For Part 2, two different
readings cannot share the same exact record state; injectivity from `T+1`
readings gives the dimension bound. For Part 3, there are `2^T` binary strings,
and exact discrimination requires mutually orthogonal quantum states (or
distinct classical states). `QED`

An unbounded exact record therefore requires unbounded local dimension,
growing spatial support or exported storage, or weaker approximate/lossy
semantics. An infinite QCA lattice is a possible growing-support resource, not
a free observer-owned archive.

### T6 — an informative recorder cannot be passive on every coherent history

**Theorem 6 (passive-recorder obstruction).** Let

```text
V: H_S -> H_S tensor H_R
```

be an isometry that includes a blank recorder, and let `U` be a source
unitary. If

```text
Tr_R[V rho V*] = U rho U*
```

for every source density operator `rho`, then there is one fixed recorder
state `|r_0>` such that

```text
V|psi> = U|psi> tensor |r_0>
```

for every `|psi>`. The recorder contains no nonconstant information about the
input or history.

**Proof.** Compose `V` with `U*` on the source factor. For every pure
`|psi>`, the resulting joint pure state has pure source marginal
`|psi><psi|`. A bipartite pure state with a pure marginal is a product, so

```text
(U* tensor I)V|psi> = |psi> tensor |r_psi>.
```

Apply linearity to two basis states and their equal superposition. The product
form of the superposition is possible only if the two recorder vectors are
the same up to one irrelevant common phase. Repeating across a basis makes
the recorder state input-independent. `QED`

This is the finite form of the no-information-without-disturbance boundary
needed here. It does not forbid informative records. It says they require at
least one of:

- backreaction or dephasing on cross-history source coherence;
- restriction to a fixed-count or other superselected sector;
- a classicalized source algebra that excludes the interference observable;
- an explicit environment/archive that changes the effective source channel;
  or
- abandonment of readable history information.

#### One-gate Clock-QCA witness

The obstruction is realized inside one frozen extended scattering, not only
by an abstract channel example. Initialize the counter at zero and prepare

```text
(|1_0,q> + |1_0,0>) / sqrt(2).
```

The first branch has no effective interaction and exits with record `0`:

```text
|s_0> tensor |0> = |q,1> tensor |0>.
```

The second branch has one effective interaction and exits with record `1`:

```text
|s_1> tensor |1>
  = (a|0,1> + b|1,0>) tensor |1>.
```

`|s_0>` and `|s_1>` are orthonormal. The ideal source output has their
off-diagonal amplitude `1/2` and normalized interference visibility `1`.
The record states are orthogonal, so physical trace of the counter removes
the off-diagonal exactly:

```text
visibility:       1 -> 0
ideal-state fidelity after trace: 1/2
trace distance from ideal:        1/2.
```

The source-basis populations are unchanged. What changes is the cross-history
coherence. The algebraic quotient `F` would restore the coherent amplitude,
which is precisely why it must not be mistaken for physical partial trace.

## 4. Exact computational receipt

Run:

```bash
.venv/bin/python tests/du_covariant_recorder_naturality_probe.py
```

Result:

```text
31/31 checks pass
VERDICT: COVARIANT COUNTER WITH NECESSARY BACKREACTION
```

The deterministic artifact is:

```text
tests/artifacts/du_covariant_recorder_naturality_result.json
```

Receipt scope:

| Audit | Exact bounded coverage |
|---|---:|
| Complete recorder matrices | `9` (`R=2,3,5`; three nontrivial coins) |
| Complete local formal-forgetting inputs | `270` |
| Training naturality basis/placement cases | `12,300` |
| Held-out `6 x 5`, `R=4`, complex-coin cases | `1,080` |
| Arbitrary dense active-block `5 x 4` cases | `320` |
| Recorder-off source inputs | `9` |

The held-out recorder patch, all training patches, and all placement tests have
maximum sparse-amplitude defect `0` in the executable arithmetic. The dense
`9 x 9` Fourier active block and its q-transparent lift have unitarity defect
below `9.5e-16`.

The executable also constructs an actual `25 x 25` controlled-add unitary:

```text
|x,y> -> |x,y+x mod 5>.
```

It copies every orthogonal basis label `|k>|0> -> |k>|k>` into a charged
second five-state register. If the original carrier is then traced out, the
basis readout remains on the copy. For the coherent input
`(|0>+|1>)/sqrt(2)`, however, the output is
`(|00>+|11>)/sqrt(2)`, not two coherent clones; the target purity and its
fidelity with `|+>` are both `1/2`. Copying also preserves the cyclic alias.
No spatial archive transport or reunion was simulated; both remain open.

Current file hashes:

```text
d65555ee5e8d62f50ee6f8d78d775a5a0e676c5bf13a660a95f7c739e27de243  tests/du_covariant_recorder_naturality_probe.py
42f74179477a8c9f6c1722c5da4e9d9bf54b1f23aa87325b8c766b5bfa41362d  tests/artifacts/du_covariant_recorder_naturality_result.json
```

These hashes should be refreshed if root audit changes either file.

## 5. Countermodels, rivals, and limitations

| Rival or failure mode | Result | Consequence |
|---|---|---|
| Selected-subspace isometry only | Refuted by complete matrix tests | The finite local extension is genuinely unitary |
| One favorable coin | Refuted by real and complex unitary coins | The proof uses only unitarity of `C` |
| Canonical placement accident | Refuted locally by all bounded placements | Placement-family composition remains a separate burden |
| Basis-state accident | Refuted by mixed complex and counter superpositions | The same linear square holds coherently |
| Counter increments on inserted `q` | Exact held-out failure | Raw micro-crossing counts are representation-dependent |
| Per-frame decoder rescue | Requires different offsets | Rejected as refitting |
| Finite counter treated as unbounded | Exact `n`/`n+R` alias | Resource claim must remain finite |
| Algebraic quotient treated as physical trace | Refuted by T6 witness | Cross-count coherence exposes the difference |
| Copying treated as free capacity | Refuted | Copy costs another register and preserves alias |
| Quantum copying treated as cloning | Refuted by controlled-add output | Coherent inputs become entangled |
| Carrier treated as an archive | Open | Loss destroys the uncopied readout |
| Logical copy treated as reunion | Not tested | Spatial transport, access, and reunion remain open |
| Covariance treated as a selector | Refuted by arbitrary-`W` closure | Physical sourcing and record interface remain open |

The construction is finite-dimensional, exactly reversible, and coherent. A
projective measurement of `k`, environmental amplification, or an exported
archive would be additional dynamics. Calling `k` a classical durable record
before one of those constructions survives would overstate the result.

## 6. Related work and novelty status

**Novelty status: `SEARCH-INCOMPLETE`.**

The primary host paper proves the exact Clock-QCA covariance square but does
not introduce this accumulated interaction counter. Adjacent work makes clear
that storing clock information and producing a classical record are separate
resource problems:

- [Y. Yang, G. Chiribella, and M. Hayashi, *Quantum Stopwatch: How to Store
  Time in a Quantum Memory*](https://arxiv.org/abs/1703.05876) studies coherent
  transfer/storage of time information in quantum memory.
- [P. Erker et al., *Autonomous quantum clocks: Does thermodynamics limit our
  ability to measure time?*](https://arxiv.org/abs/1609.06704) studies
  autonomous clock accuracy and thermodynamic resources.
- [K. Wadhia et al., *Entropic costs of the quantum-to-classical transition
  in a microscopic clock*](https://arxiv.org/abs/2502.00096) studies costs
  associated with measurement/amplification toward classical clock records.

These are adjacent antecedents, not evidence that they contain the
q-transparent closure lemma, this Clock-QCA counter, or this exact one-gate
obstruction package.

Before a novelty claim, a broader search must cover:

- QCA extensions with internal clocks, counters, and history tapes;
- quantum transducers and finite-state quantum automata;
- covariant quantum instruments and quantum reference frames;
- reversible measurement and no-information-without-disturbance theorems;
- event-counting full-counting statistics;
- autonomous clocks, quantum memories, and clock classicalization; and
- categorical/naturality treatments of quiescent-symbol circuit encodings.

The closure lemma is elementary enough to be folklore. The potentially useful
publication unit is not “a modulo counter can be attached.” It is the scoped
package:

```text
exact source-host extension
+ arbitrary-active-block covariance closure
+ proof that covariance is nonselective
+ exact separation of algebraic and physical forgetting
+ in-host passive-recorder obstruction
+ executable adversarial receipt.
```

Whether that package is novel enough for a paper remains open.

## 7. Physical interpretation

What has been built is a **coherent interaction counter**:

- it is carried by the particle;
- it advances on the source-declared effective interaction;
- it ignores encoding-added quiescent crossings;
- it transforms with the same q-insertion circuit in admitted frames; and
- it is readable as an orthogonal internal species before cyclic aliasing.

It is not yet:

- an irreversible mark;
- a stable macroscopic pointer;
- an observer-owned memory;
- an archive that survives carrier loss;
- an operational reunion comparison;
- a calibrated duration;
- proper time; or
- a physical reason to choose this counter rather than another covariant
  active block.

T6 is not merely a downside. It identifies where record physics must appear.
If the counter becomes informative across histories, then the source and
record cannot remain dynamically separable on their full coherent algebra.
Record formation must be accompanied by entanglement, decoherence,
superselection, measurement, or another explicit change in the effective
source channel.

## 8. Implications for Dynamic Unity

The swing makes two foundational advances and one narrowing.

First, it gives a constructive positive answer to the finite mathematical
question:

> Exact discrete Clock-QCA covariance is compatible with a coherent,
> source-event-sensitive internal counter.

Second, it identifies a sharper research invariant than “does a covariant
clock exist?”:

> Which physical interaction selects a record algebra, pays for its
> distinguishability and persistence, and explains the corresponding
> backreaction on coherent histories?

Third, it blocks a tempting overinterpretation. The covariance square itself
cannot select the counter because arbitrary active unitaries inherit it.
Therefore the counter does not yet derive time, a dimensional rate, an
observer, or a Dynamic Unity law. Its count is the number of interactions
declared effective by the host construction.

This is nevertheless a real dependency change. The program no longer needs
another abstract debate about whether a clock can be “smuggled in.” It has an
exact finite counter and an exact theorem locating the next missing physics.

## 9. Next decisive experiment

The next concentrated experiment should be the
**classicalization–archive–reunion extension of this same counter**, not a new
premise wave.

Freeze:

1. the same source `U_C`, counter rule, and canonical encoding family;
2. one explicit open-system pointer interaction that turns selected counter
   labels into distinguishable archive states;
3. one finite archive carrier and locality boundary;
4. one controlled-copy law, with every extra `R`-state register charged;
5. one transport path through the actual Clock-QCA circuit;
6. one recorder-carrier loss intervention;
7. one reunion readout fixed before held-out encodings; and
8. one cross-count interferometer measuring the visibility lost as archive
   distinguishability grows.

The decisive outputs are:

```text
record distinguishability,
source interference visibility,
archive support and dimension,
access latency,
loss tolerance,
fixed-decoder reunion accuracy,
and covariance defect.
```

**Advance condition:** one fixed open recorder/archive/reunion law commutes
with the admitted encodings, preserves a distinguishable finite record after
declared loss/transport, and quantitatively accounts for the associated
source dephasing and storage.

**Stop condition:** the archive is only an external label; the decoder changes
by frame; inserted `q` crossings change the record; carrier loss destroys all
access while “observer memory” is still claimed; or unbounded storage is
treated as free.

Only after that survives should the program ask whether the resulting
record-bearing subsystem has an observer-owned boundary or any relation to
proper time.

## 10. Claim grade and publication readiness

### Earned

- exact complete-basis local unitarity of the frozen finite extension;
- exact algebraic source intertwinement;
- exact physical conservativity on fixed-count coherent sectors;
- exact canonical q-insertion naturality;
- a general q-transparent arbitrary-active-block lifting lemma;
- exact event-count correctness before aliasing;
- exact finite record-dimension bounds;
- a general passive-recorder obstruction;
- an in-host one-gate cross-count interference witness; and
- a deterministic adversarial computational receipt.

### Not earned

- physical realization by nature;
- a classical, irreversible, thermodynamic, or observer-owned record;
- spatial archive transport or reunion;
- a reason nature selects this counter;
- proper time, a time unit, or an invariant physical rate;
- continuum, `3+1`, gravitational, or cosmological covariance;
- a bridge to causal-set predictive state, GU, `Lambda`, or another DU
  candidate; or
- a publication novelty claim.

### Readiness

The result is a credible technical spine for a short note, not a
submission-ready paper. Publication readiness requires:

1. independent proof audit of the source boundary convention and lifting
   lemma;
2. broader prior-art search;
3. circuit diagrams and notation cleanup;
4. a precise statement of the finite local result versus an infinite-QCA
   global dynamics;
5. either the open recorder/archive experiment or a disciplined decision to
   publish the construction–obstruction result alone; and
6. external peer criticism.

No physics claim or prediction is banked by this swing.
