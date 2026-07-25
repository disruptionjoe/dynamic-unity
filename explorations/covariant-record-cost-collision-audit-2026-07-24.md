---
title: "Hostile collision audit — Covariant Records Are Not Free"
status: completed_hostile_novelty_audit
doc_type: exploration
created: 2026-07-24
paper_id: DU-PAPER-003
claim_grade: "LITERATURE COLLISION / INDEPENDENT ADVERSARIAL REVIEW"
novelty_status: "CURRENT GENERAL PACKAGE ABSORBED; MODEL-SPECIFIC NARROWING CONDITIONALLY OPEN"
recommendation: "NARROW / PRE-PROOF KILL GATE"
banked: false
---

# Hostile collision audit: `DU-PAPER-003`

## Executive verdict

**Decision: NARROW / CONDITIONAL GO. Do not draft the currently advertised
general theorem package as a standalone paper.**

The current Clock-QCA work is exact, careful, and useful as a benchmark. Its
general information-theoretic claims, however, are already contained in mature
literatures:

1. exact and approximate information--disturbance through complementary
   channels;
2. two-path complementarity;
3. quantum instruments and covariant instrument dilations;
4. no-cloning, no-broadcasting, and no-hiding;
5. finite-dimensional state packing, Holevo information, and Fano decoding
   bounds; and
6. symmetry, locality, memory, and measurement-resource bounds.

In particular:

- The exact two-history relation

  \[
  \delta=\frac{1-|\gamma|}{2},
  \qquad
  D^2=4\delta(1-\delta)
  \]

  is **fully absorbed** by the pure-marker equality in two-path
  complementarity plus the elementary diamond norm of a qubit dephasing
  channel.
- A Welch support bound for many pure record states is **fully absorbed** by
  classical frame theory.
- A decoding-support bound obtained from Holevo plus Fano is **fully
  absorbed** by standard quantum information theory.
- Combining those results side by side does not create a new theorem.

What remains potentially distinctive is much narrower:

> In the Arrighi--Facchini--Forets Clock QCA, canonical `q`-insertion
> covariance admits an arbitrary unitary on the active-active sector. It
> therefore does not select a recorder law, while explicit recorder and
> archive lifts expose how familiar information--disturbance and support
> constraints appear in that exact covariant fixture.

That is a model-specific negative result and a useful worked example. **As
currently proved, it is not enough for a normal standalone research paper.**
The arbitrary-`W` lifting lemma follows almost immediately from the orthogonal
sector decomposition and unique active crossing. The paper becomes defensible
only if it adds at least one of:

- a non-tautological **complete classification** of a physically motivated
  class of Clock-QCA recorder/archive extensions; or
- a genuinely joint **covariance--locality--record-support theorem** that is
  stronger than placing a standard channel tradeoff beside a standard
  Holevo/Welch bound.

Without one of those, this material belongs as a technical note, benchmark
appendix, or case study inside a broader paper.

## 1. Scope and terminology

This audit covers the claims and constructions in:

- `covariant-recorder-naturalization-swing-2026-07-24.md`;
- `covariant-recorder-naturalization-adversarial-audit-2026-07-24.md`;
- `covariant-archive-boundary-swing-2026-07-24.md`;
- `covariant-archive-boundary-adversarial-audit-2026-07-24.md`; and
- the `DU-PAPER-003` entry in the paper portfolio.

It adjudicates novelty, not correctness. The finite constructions and probes
may all be correct while the proposed paper contribution is already known.

Two naming boundaries are essential.

### 1.1 The covariance in the fixture is narrow

The established covariance is the exact source-sense naturality square for
canonical `q`-insertion encodings and finite rectangular patches of the
discrete Clock QCA. It is not, without additional proof:

- continuum Lorentz covariance;
- covariance under an arbitrary spacetime symmetry group;
- covariance of a measurement instrument in the usual group-representation
  sense; or
- a classification of all refinement maps or all physical observers.

The paper must say `Clock-QCA q-insertion covariance` or `source-sense
refinement covariance` until a stronger bridge is proved.

### 1.2 “Cost” needs a declared currency

The current exact fixture establishes costs in at least two distinct senses:

- informative complementary output degrades some coherent source distinctions;
- exact nonaliasing classical histories require enough orthogonal support.

It does **not** yet establish a universal energetic or thermodynamic cost.
A controlled unitary can correlate a source with a pre-supplied pure,
degenerate-energy ancilla without a model-independent positive work bill.
The consumed resources may instead be blank-state purity, dimension, control,
asymmetry, locality, reset capacity, or readout amplification. A paper titled
“Records Are Not Free” must freeze which of these currencies it prices.

## 2. Claim-by-claim collision matrix

| Current or proposed claim | Closest established result | What remains after collision | Verdict |
|---|---|---|---|
| The `1+1` Clock QCA has exact discrete source covariance | Arrighi, Facchini, and Forets, [arXiv:1404.4499](https://arxiv.org/abs/1404.4499), [DOI 10.1088/1367-2630/16/9/093007](https://doi.org/10.1088/1367-2630/16/9/093007) | Reproduction and use as a host fixture | Prior art / host |
| Every `q`-transparent active unitary `W` inherits the canonical rectangular covariance square | Orthogonal-sector unitarity plus the host's unique-active-crossing proof; compare general QCA structure in Schumacher--Werner, [quant-ph/0405174](https://arxiv.org/abs/quant-ph/0405174) | A clean model-specific nonselection lemma | Exact but likely too immediate for standalone novelty |
| A finite modulo counter can be lifted coherently into the Clock QCA | General unitary ancilla/instrument dilation; QCA “with history” is already explicit in Vlasov, [quant-ph/0406119](https://arxiv.org/abs/quant-ph/0406119) | This particular finite Clock-QCA implementation and executable tests | Useful construction; weak novelty alone |
| Exact preservation of a unitary source channel forces a constant complementary recorder | KSW information--disturbance, [quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009); Bény--Oreshkov recovery/complement duality, [arXiv:1103.0649](https://arxiv.org/abs/1103.0649); Busch, [arXiv:0706.3526](https://arxiv.org/abs/0706.3526) | A short self-contained proof specialized to the fixture | Fully absorbed |
| Pure two-history markers obey `V^2+D^2=1` | Englert, [DOI 10.1103/PhysRevLett.77.2154](https://doi.org/10.1103/PhysRevLett.77.2154) | Notation and a Clock-QCA realization | Fully absorbed |
| `δ=(1-|γ|)/2` and `D^2=4δ(1-δ)` | Englert equality plus the elementary diamond norm of a qubit dephasing/Pauli channel; broader tight tradeoffs in Hashagen--Wolf, [arXiv:1802.09893](https://arxiv.org/abs/1802.09893) | An exact saturating family inside this fixture | Fully absorbed as a theorem |
| History-independent archive unitaries preserve joint record evidence | Unitary invariance of Gram matrices and trace distance; Stinespring uniqueness; no-hiding, Braunstein--Pati, [gr-qc/0603046](https://arxiv.org/abs/gr-qc/0603046) | A helpful boundary-accounting demonstration | Fully absorbed |
| SWAP transfers the record; CNOT exports a basis predicate; repeated fanout does not create independent evidence | No-cloning and no-broadcasting, including Barnum et al., [quant-ph/9511010](https://arxiv.org/abs/quant-ph/9511010) | Exact finite controls showing transfer versus redundant carriage | Standard illustration |
| Fresh independent marker cells yield overlap `γ^m` and distinguishability `sqrt(1-|γ|^(2m))` | Tensor-product overlap and pure-state trace distance | Clock-QCA placement and accounting | Fully absorbed mathematically |
| A finite reused unitary pointer recurs or aliases | Finite-dimensional unitary recurrence and elementary modular counting | Exact recurrence horizons for the chosen counter/rotation | Standard; useful kill control |
| Perfect records of `M` histories require archive dimension at least `M` | Orthogonality/rank | Clock-QCA interpretation | Fully absorbed |
| Approximate pure records require dimension according to a Welch-type bound | Welch, [DOI 10.1109/TIT.1974.1055219](https://doi.org/10.1109/TIT.1974.1055219), plus the larger spherical-code/frame literature | At most a specialization to a constrained reachable ensemble | Fully absorbed unless covariance changes the reachable-code problem |
| Decoding `M` records with error `p_e` requires a Holevo/Fano-sized archive | Holevo 1973, [MathNet record](https://www.mathnet.ru/eng/ppi903), plus Fano's inequality | At most a specialization with a new locality/covariance restriction | Fully absorbed |
| Moving the archive into an enlarged state preserves some observations but changes available interventions | Stinespring dilation, state augmentation, complementary-channel recovery, and no-hiding | A clear operational contract for this model | Conceptually useful; not a new general theorem |
| Covariance admits but does not select a record law | The arbitrary-`W` Clock-QCA lift is a model-specific negative example; general covariant-instrument classifications already show large admissible families | Possible paper nucleus if upgraded to a complete, non-tautological classification | Conditionally open |
| Physically covariant records require apparatus asymmetry or symmetry resource | WAY/asymmetry results: Marvian--Spekkens, [arXiv:1212.3378](https://arxiv.org/abs/1212.3378), and Hokkyo--Tajima, [arXiv:2607.09075](https://arxiv.org/abs/2607.09075) | A result specific to source-refinement covariance rather than ordinary group symmetry | Prior art dominates any broad symmetry-cost claim |
| Ideal records have unavoidable energy/dimension cost | Guryanova--Friis--Huber, [arXiv:1805.11899](https://arxiv.org/abs/1805.11899), under their explicit measurement model | A matched Clock-QCA Hamiltonian, blank-state, control, reset, and readout ledger | Not established by the present fixture |
| A local/open QCA record export has constrained information flow | Reversible QCA locality in Schumacher--Werner and open-QCA information current in Wagner et al., [arXiv:2204.09922](https://arxiv.org/abs/2204.09922) | A stronger theorem coupling refinement covariance to reachable archive information | Open only if it exceeds standard locality plus channel-capacity composition |

## 3. Exact adjudication of the two-history relation

Let the record isometry be

\[
|0\rangle\mapsto |0\rangle|a_0\rangle,\qquad
|1\rangle\mapsto |1\rangle|a_1\rangle,
\qquad
\gamma=\langle a_0|a_1\rangle .
\]

After the record is discarded, the source undergoes

\[
\Lambda_\gamma
\begin{pmatrix}
\rho_{00}&\rho_{01}\\
\rho_{10}&\rho_{11}
\end{pmatrix}
=
\begin{pmatrix}
\rho_{00}&\gamma^*\rho_{01}\\
\gamma\rho_{10}&\rho_{11}
\end{pmatrix}.
\]

For the repository's real nonnegative `γ=cos(theta)` family,

\[
\Lambda_\gamma=(1-p)\operatorname{id}+p\,\operatorname{Ad}_Z,
\qquad
p=\frac{1-\gamma}{2}.
\]

The identity and `Z` unitary channels are perfectly distinguishable, hence

\[
\frac12\|\Lambda_\gamma-\operatorname{id}\|_\diamond=p
=\frac{1-\gamma}{2}.
\]

For complex `γ`, one first factors the known diagonal phase. Optimizing over
that harmless phase correction replaces `γ` by `|γ|`, giving

\[
\delta_{\rm phase\text{-}optimized}
=\frac12\inf_{\phi}
\|\Lambda_\gamma-\operatorname{Ad}_{U_\phi}\|_\diamond
=\frac{1-|\gamma|}{2}.
\]

The trace distance of the two pure marker states is

\[
D=\frac12
\bigl\||a_0\rangle\!\langle a_0|
-|a_1\rangle\!\langle a_1|\bigr\|_1
=\sqrt{1-|\gamma|^2}.
\]

Since `|γ|=1-2δ`,

\[
D^2=1-(1-2\delta)^2=4\delta(1-\delta).
\]

### Novelty ruling

**Fully absorbed.** The `V=|γ|`, `D=sqrt(1-|γ|^2)` equality is the pure-marker
endpoint of two-path complementarity. The diamond-distance expression is the
one-line norm computation for the corresponding qubit dephasing channel.
KSW supplies the broader dimension-independent continuity relation between a
channel and its complement, while Hashagen--Wolf establishes tight optimal
measurement-error/diamond-disturbance tradeoffs for a substantially broader
instrument class.

The Clock-QCA construction can be cited as one exact saturating realization,
but the equality cannot be presented as a new theorem.

## 4. Exact adjudication of archive-support bounds

### 4.1 Welch

For `M` unit pure record vectors in a `d`-dimensional archive, the Welch bound
implies, for `M>d`,

\[
\max_{i\ne j}|\langle a_i|a_j\rangle|^2
\ge \frac{M-d}{d(M-1)}.
\]

If every pairwise overlap is required to be at most `mu`, this rearranges to

\[
d\ge \frac{M}{1+\mu^2(M-1)}.
\]

That is a standard frame-packing bound. Replacing “codeword” with “record
state” does not change its novelty. More specialized quantum spherical-code
and state-discrimination bounds may dominate Welch for particular error
criteria.

### 4.2 Holevo plus Fano

Let a uniformly distributed history label `X` have `M` values and let a
measurement on archive `A` decode it with error probability `p_e`. Fano gives

\[
I(X:\widehat X)
\ge
\log_2 M-h_2(p_e)-p_e\log_2(M-1).
\]

Holevo gives

\[
I(X:\widehat X)\le \chi(X:A)\le \log_2 d_A.
\]

Therefore

\[
\log_2 d_A
\ge
\log_2 M-h_2(p_e)-p_e\log_2(M-1).
\]

This is a standard corollary. For `M=2^T` histories it yields the expected
linear-in-`T` reliable classical support requirement, up to the allowed error.

### Novelty ruling

**Both candidate support theorems are fully absorbed.** Substituting a
disturbance-dependent overlap into Welch, or placing the Holevo/Fano bound
beside KSW, remains a composition of known inequalities unless the Clock-QCA
covariance and locality assumptions impose a new joint feasible region.

A publishable result must do more than write

\[
\text{known disturbance bound}
\quad+\quad
\text{known dimension bound}
\quad+\quad
\text{finite-speed light cone}.
\]

It must show that source-refinement covariance rules out instruments or codes
that the unconstrained inequalities permit, derive a strictly stronger bound,
or completely classify and saturate the constrained optimum.

## 5. The sharpest absorbers

No single prior theorem absorbs every line of the proposed paper. The proposed
general contribution is instead covered by a mature stack.

### 5.1 Channel/complement layer

Kretschmann, Schlingemann, and Werner's continuity of Stinespring
representation is the sharpest general absorber for:

- exact unitary source preservation implies a constant complementary record;
- approximate source recovery limits environment information; and
- approximate no-broadcasting.

Bény and Oreshkov sharpen the recovery/complement viewpoint by making
approximate simulation and environment leakage dual optimization problems.
The present boundary-relocation and later-recoupling analysis should be
written as a specialization of this framework, not as a new universal law.

### 5.2 Instrument tradeoff layer

Hashagen and Wolf is the strongest direct collision with the planned “tight
approximate/noisy record--disturbance theorem.” It gives universal optimal
instrument families and dimension-independent diamond-norm tradeoffs for
von Neumann measurements, with semidefinite-program treatment for general
POVMs. Buscemi and Sacchi,
[quant-ph/0610196](https://arxiv.org/abs/quant-ph/0610196), separately optimize
the information--disturbance tradeoff for discriminating two pure states.

### 5.3 Covariance layer

Covariant instrument structure is itself established:

- Carmeli, Heinosaari, and Toigo,
  [arXiv:0805.3917](https://arxiv.org/abs/0805.3917);
- Chiribella, D'Ariano, and Perinotti,
  [arXiv:0810.3211](https://arxiv.org/abs/0810.3211); and
- Verdon's covariant Stinespring theorem,
  [arXiv:2108.09872](https://arxiv.org/abs/2108.09872).

These works concern representation-theoretic covariance, not automatically
the repository's `q`-insertion refinement square. That difference is a
possible opening, but only after it is formalized. It is not permission to
ignore the existing covariant-instrument classifications.

### 5.4 Archive and public-record layer

No-cloning, no-broadcasting, strong Quantum Darwinism, and Spectrum Broadcast
Structure already separate:

- transfer from copying;
- one correlated fanout from independently accessible evidence;
- decoherence from public objectivity; and
- redundancy from broadcastable classical information.

Relevant primary sources include:

- Barnum et al., [quant-ph/9511010](https://arxiv.org/abs/quant-ph/9511010);
- Piani, Horodecki, and Horodecki,
  [arXiv:0707.0848](https://arxiv.org/abs/0707.0848);
- Le and Olaya-Castro,
  [arXiv:1803.08936](https://arxiv.org/abs/1803.08936); and
- Korbicz, [arXiv:2007.04276](https://arxiv.org/abs/2007.04276).

Any “public record” result must compare against the full information in an
SBS/strong-QD description, not only against ordinary decoherence.

### 5.5 Physical-resource layer

Broad claims that covariance or measurement makes records physically costly
collide with:

- WAY/asymmetry resource theory;
- finite apparatus dimension and energy bounds for ideal measurement;
- quantum-clock accuracy/resource tradeoffs; and
- explicit experiments separating microscopic ticks from macroscopic
  amplification and readout.

The last point is especially concrete in Wadhia et al.,
[arXiv:2502.00096](https://arxiv.org/abs/2502.00096): their device finds that
the macroscopic record/readout contribution dominates the microscopic
clockwork dissipation. That supports the repository's insistence on charging
the interface, but it also means an energetic paper needs a physical
apparatus model rather than a finite unitary ancilla alone.

## 6. What survives the collision

The surviving package is a **model conjunction**, not a new general law:

1. an exact source Clock-QCA with canonical refinement maps;
2. an exact family of finite recorder and archive lifts;
3. a proof that every active-sector unitary `W` passes the same canonical
   `q`-insertion covariance square;
4. explicit demonstrations of known information--disturbance,
   record-transfer, carrier-loss, recurrence, and boundary-access effects;
5. executable positive and negative controls.

This conjunction has pedagogical and programmatic value. It establishes that
covariance can coexist with records while failing to select their dynamics,
and it prevents Dynamic Unity from treating “covariant recorder exists” as a
derivation of observer memory or finality.

It does not yet establish:

- that the arbitrary-`W` family exhausts all physically relevant extensions;
- that the record interface is selected rather than inserted;
- an autonomous local archive-emission law;
- a new optimal approximate tradeoff;
- a new support bound;
- thermodynamic irreversibility;
- a continuum or higher-dimensional result; or
- a novel experiment.

### Is the model-specific conjunction enough for a short paper?

**Not in its current form.**

It could support a defensible short negative note if all of the following are
true:

1. the admissible extension class is motivated independently of the desired
   result;
2. the result is a complete classification or no-go, not merely the
   observation that a block-diagonal definition permits an arbitrary block;
3. the paper states that the channel, complementarity, and storage formulas
   are known controls;
4. the exact Clock-QCA conclusion answers a live misconception or open
   question in the source literature; and
5. a primary-literature search finds no prior equivalent refinement-natural
   recorder classification.

If those conditions are not met, the correct venue is an appendix, software
artifact, or technical benchmark rather than a standalone theorem paper.

## 7. Minimal theorem targets that could still survive

### Target A — complete Clock-QCA recorder-extension classification

Freeze a class `C` of local finite-cell extensions without building the
answer into its definition. At minimum, specify:

- one common quiescent state;
- a compositional family of refinement encodings;
- finite propagation radius and translation invariance;
- one frame-independent source quotient;
- one frame-independent readout interface;
- exact naturality for every admitted rectangular refinement; and
- equivalence under declared local gauge changes.

Then classify all extensions in `C` that produce a nonconstant accessible
record channel.

A potentially publishable negative conclusion would be:

> Exact source-refinement covariance leaves a full active-instrument family
> unconstrained; every additional recorder selection requires structure not
> present in the source covariance data.

The proof must establish necessity or a universal embedding statement. The
current arbitrary-`W` lemma establishes a large sufficient family, which is
not the same result.

**Immediate danger:** if `C` assumes transparent `q` sectors and then defines
the active-active block as arbitrary, the classification is tautological and
the paper is killed.

### Target B — local covariant archive-export bound

Freeze:

- local cell dimension `d_0`;
- interaction radius and update depth;
- a compositional refinement family;
- an autonomous blank-cell/archive interface;
- `M` admissible histories;
- target decoding error `epsilon`;
- a source recovery/disturbance metric; and
- the exact accessible archive region after `t` updates.

Seek the constrained optimum over all admissible local instruments, not a
particular pointer:

\[
\text{best record distinguishability}
\quad\text{subject to}\quad
\text{source disturbance, locality, covariance, and support}.
\]

To survive collision, the theorem must show one of:

- the Clock-QCA/refinement constraints make the attainable region strictly
  smaller than the unconstrained KSW/Hashagen--Wolf plus Holevo region;
- a new equality or extremal instrument classification;
- a stronger spacetime-support lower bound than ordinary capacity plus
  finite propagation; or
- a tight separation between correlated fanout and independently
  accessible record fragments forced by the local covariant dynamics.

Merely deriving

\[
n\log d_0
\ge
\log M-h_2(\epsilon)-\epsilon\log(M-1)
\]

and observing that `n` lies in a QCA light cone is not enough.

### Target C — model-specific negative paper

If A and B are too large, the honest short-paper target is:

> **Covariance Does Not Select Records in the Clock QCA.**

The record-cost relations would appear only as known diagnostics. The core
would be a complete statement of what source-sense covariance does and does
not constrain, with a family of inequivalent recorder, no-recorder, erasing,
and archive laws all satisfying the same covariance contract.

This is lower upside but much more defensible than presenting known
information-theoretic bounds as new.

## 8. Hard-kill conditions

Kill or merge `DU-PAPER-003` as a standalone paper if any of the following
holds after the next proof attempt.

1. **Two-history kill.** The main quantitative result is
   `D^2=4δ(1-δ)` or an equivalent reparameterization.
2. **KSW kill.** The approximate theorem is a direct specialization of
   Stinespring continuity, complementary-channel recovery, or
   Hashagen--Wolf without a stricter Clock-QCA feasible region.
3. **Welch/Holevo kill.** The archive theorem is Welch, rank,
   Holevo--Fano, random-access coding, or state packing with record
   vocabulary.
4. **Direct-sum kill.** The covariance theorem says only that an arbitrary
   block remains arbitrary after an orthogonal direct-sum lift.
5. **Factorized-conjunction kill.** The proposed novelty is only “known
   channel theorem + known storage theorem + finite light cone.”
6. **Unpriced-cost kill.** The title or abstract claims physical,
   thermodynamic, or energetic cost without a Hamiltonian, preparation,
   control, reset, and readout ledger.
7. **Covariance-overclaim kill.** The paper calls canonical `q`-insertion
   naturality simply “Lorentz covariance” or “covariant measurement” without
   proving the bridge.
8. **Interface-insertion kill.** The recorder/archive boundary and readout
   law remain hand-declared, while the paper claims they are dynamically
   selected.
9. **Autonomy kill.** Every growing record is supplied by externally
   allocated fresh blank cells with no local emission/transport law, while
   the paper claims an autonomous archive.
10. **Objectivity kill.** Publicity or independent evidence is inferred from
    fanout without comparison to no-broadcasting and SBS/strong-QD controls.
11. **Tightness kill.** The claimed optimum is saturated only by the
    two-history qubit pointer, with no proof over the declared admissible
    class.
12. **Literature-boundary kill.** The final comparison omits covariant
    instruments, approximate recovery, QCA information flow, WAY/asymmetry,
    and measurement-resource results.

## 9. Go/no-go gates

### Gate 1 — classification pre-proof

Attempt a necessity theorem for a non-tautological extension class. The
deliverable must distinguish:

- what follows from source covariance;
- what follows from transparency/locality assumptions;
- what follows from the inserted record interface; and
- what remains arbitrary.

If the proof collapses to the current four-sector decomposition, stop the
standalone paper.

### Gate 2 — nonseparable quantitative theorem

Formulate the optimization over all admissible local covariant instruments.
First reproduce the unconstrained KSW/Hashagen--Wolf and Holevo/Welch
benchmarks. Then test whether Clock-QCA refinement covariance removes any
otherwise optimal instrument.

If it does not, the quantitative theorem is an application, not a new result.

### Gate 3 — title and venue

- If Gate 1 passes: pursue the narrow negative/classification paper.
- If Gate 2 also passes: retain a stronger record-cost title.
- If neither passes: merge the exact fixture into the broader CCR or
  boundary-relocation paper and preserve the probes as reusable benchmarks.

## 10. Primary-source collision index

### Clock QCA, locality, and information flow

- Arrighi, Facchini, and Forets, “Discrete Lorentz covariance for Quantum
  Walks and Quantum Cellular Automata,”
  [arXiv:1404.4499](https://arxiv.org/abs/1404.4499),
  [DOI 10.1088/1367-2630/16/9/093007](https://doi.org/10.1088/1367-2630/16/9/093007).
- Schumacher and Werner, “Reversible quantum cellular automata,”
  [quant-ph/0405174](https://arxiv.org/abs/quant-ph/0405174).
- Arrighi, Nesme, and Werner, “Unitarity plus causality implies
  localizability,”
  [DOI 10.1016/j.jcss.2010.05.004](https://doi.org/10.1016/j.jcss.2010.05.004).
- Vlasov, “On Quantum Cellular Automata,”
  [quant-ph/0406119](https://arxiv.org/abs/quant-ph/0406119).
- Wagner et al., “Information Flow in Non-Unitary Quantum Cellular
  Automata,” [arXiv:2204.09922](https://arxiv.org/abs/2204.09922).

### Information, disturbance, and recovery

- Kretschmann, Schlingemann, and Werner, “The Information-Disturbance
  Tradeoff and the Continuity of Stinespring's Representation,”
  [quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009),
  [DOI 10.1109/TIT.2008.917696](https://doi.org/10.1109/TIT.2008.917696).
- Bény and Oreshkov, “General Conditions for Approximate Quantum Error
  Correction and Near-Optimal Recovery Channels,”
  [arXiv:0907.5391](https://arxiv.org/abs/0907.5391),
  [DOI 10.1103/PhysRevLett.104.120501](https://doi.org/10.1103/PhysRevLett.104.120501).
- Bény and Oreshkov, “Approximate simulation of quantum channels,”
  [arXiv:1103.0649](https://arxiv.org/abs/1103.0649).
- Busch, “No Information Without Disturbance,”
  [arXiv:0706.3526](https://arxiv.org/abs/0706.3526).
- D'Ariano, Perinotti, and Tosini, “Information and disturbance in
  operational probabilistic theories,”
  [arXiv:1907.07043](https://arxiv.org/abs/1907.07043).

### Tight measurement tradeoffs and complementarity

- Englert, “Fringe Visibility and Which-Way Information: An Inequality,”
  [DOI 10.1103/PhysRevLett.77.2154](https://doi.org/10.1103/PhysRevLett.77.2154).
- Hashagen and Wolf, “Universality and Optimality in the
  Information-Disturbance Tradeoff,”
  [arXiv:1802.09893](https://arxiv.org/abs/1802.09893).
- Banaszek, “Fidelity balance in quantum operations,”
  [quant-ph/0003123](https://arxiv.org/abs/quant-ph/0003123).
- Buscemi and Sacchi, “Information-Disturbance Tradeoff in Quantum State
  Discrimination,”
  [quant-ph/0610196](https://arxiv.org/abs/quant-ph/0610196).

### Instruments and covariance

- Carmeli, Heinosaari, and Toigo, “Covariant quantum instruments,”
  [arXiv:0805.3917](https://arxiv.org/abs/0805.3917),
  [DOI 10.1016/j.jfa.2009.08.013](https://doi.org/10.1016/j.jfa.2009.08.013).
- Chiribella, D'Ariano, and Perinotti, “Realization schemes for quantum
  instruments in finite dimensions,”
  [arXiv:0810.3211](https://arxiv.org/abs/0810.3211),
  [DOI 10.1063/1.3105923](https://doi.org/10.1063/1.3105923).
- Verdon, “A covariant Stinespring theorem,”
  [arXiv:2108.09872](https://arxiv.org/abs/2108.09872).

### Broadcasting, hiding, and objectivity

- Barnum et al., “Noncommuting Mixed States Cannot Be Broadcast,”
  [quant-ph/9511010](https://arxiv.org/abs/quant-ph/9511010).
- Piani, Horodecki, and Horodecki, “No-local-broadcasting theorem for
  multipartite quantum correlations,”
  [arXiv:0707.0848](https://arxiv.org/abs/0707.0848).
- Braunstein and Pati, “Quantum information cannot be completely hidden in
  correlations,” [gr-qc/0603046](https://arxiv.org/abs/gr-qc/0603046).
- Le and Olaya-Castro, “Strong Quantum Darwinism and Strong Independence are
  Equivalent to Spectrum Broadcast Structure,”
  [arXiv:1803.08936](https://arxiv.org/abs/1803.08936).
- Korbicz, “Roads to objectivity: Quantum Darwinism, Spectrum Broadcast
  Structures, and Strong quantum Darwinism,”
  [arXiv:2007.04276](https://arxiv.org/abs/2007.04276).

### Support and decoding

- Welch, “Lower bounds on the maximum cross correlation of signals,”
  [DOI 10.1109/TIT.1974.1055219](https://doi.org/10.1109/TIT.1974.1055219).
- Holevo, “Bounds for the Quantity of Information Transmitted by a Quantum
  Communication Channel,”
  [MathNet record](https://www.mathnet.ru/eng/ppi903).
- Nayak, “Optimal lower bounds for quantum automata and random access
  codes,” [quant-ph/9904093](https://arxiv.org/abs/quant-ph/9904093).
- Montanaro, “On the distinguishability of random quantum states,”
  [quant-ph/0607011](https://arxiv.org/abs/quant-ph/0607011).
- Flammia et al., “Limits on the storage of quantum information in a volume
  of space,” [arXiv:1610.06169](https://arxiv.org/abs/1610.06169).

### Symmetry and physical resources

- Marvian and Spekkens, “An information-theoretic account of the
  Wigner-Araki-Yanase theorem,”
  [arXiv:1212.3378](https://arxiv.org/abs/1212.3378).
- Hokkyo and Tajima, “Quantitative Wigner-Araki-Yanase Theorems for Unitary
  and Antiunitary Symmetries,”
  [arXiv:2607.09075](https://arxiv.org/abs/2607.09075).
- Guryanova, Friis, and Huber, “Ideal Projective Measurements Have Infinite
  Resource Costs,” [arXiv:1805.11899](https://arxiv.org/abs/1805.11899).
- Erker et al., “Autonomous Quantum Clocks: Does Thermodynamics Limit Our
  Ability to Measure Time?”,
  [arXiv:1609.06704](https://arxiv.org/abs/1609.06704).
- Wadhia et al., “Entropic costs of the quantum-to-classical transition in a
  microscopic clock,”
  [arXiv:2502.00096](https://arxiv.org/abs/2502.00096).

## 11. Final recommendation

Preserve the exact Clock-QCA recorder/archive suite. It is a strong benchmark
and has already corrected an important conceptual mistake: covariance does
not itself supply memory, select a record law, or make a finite unitary
archive irreversible.

For publication:

1. rename the live target provisionally to **Covariance Does Not Select
   Records in the Clock QCA**;
2. attempt the non-tautological classification in Gate 1;
3. in parallel on paper, formulate—but do not brute-force—the constrained
   instrument optimization in Gate 2;
4. treat the two-history, Welch, and Holevo formulas as cited controls; and
5. stop the standalone paper if neither gate produces a result unavailable
   from the prior-art stack.

The most honest present disposition is:

```text
scientific fixture:        strong
general theorem novelty:   absorbed
model-specific novelty:    possible but thin
standalone paper now:      no
short paper after Gate 1:  conditional yes
strong record-cost paper:  only after Gate 2
```

## Search boundary

This was a bounded hostile collision review of primary papers and direct
preprints through 2026-07-24, not a certified exhaustive bibliography. It is
wide enough to reject the current general novelty claim. Any surviving
Clock-QCA classification would still require a focused citation and theorem
search around refinement-natural QCA extensions before submission.
