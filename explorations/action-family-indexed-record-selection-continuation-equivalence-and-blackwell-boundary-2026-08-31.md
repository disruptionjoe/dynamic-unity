---
title: "Bell specialization of action-family records: audit restoration and the naturality boundary"
status: banked_source_grounded_specialization_and_naturality_boundary
doc_type: exploration
created: 2026-08-31
claim_id: HC-DU-202
run_id: RUN-20260831-134333-action-family-record-selection
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
---

# Executive result

`HC-DU-201` found a real physical record-to-capability positive: one heralded
Bell apparatus forms three raw bits whose two-bit quotient selects the four
teleportation corrections. This swing asks whether those two bits are *the*
record selected by the apparatus.

They are not. They are the unique coarsest record for the frozen correction
task. If the same physical controller must also answer either one-bit audit
question—“which herald result occurred?” or “which atomic projection
occurred?”—the unique minimal common-sufficient record expands back to all
three raw bits. If no future use is admitted, every raw outcome can collapse
to one class. If every possible decision problem is admitted, no nontrivial
compression survives.

The governing general result is:

> A physical carrier does not by itself select a unique nontrivial operational
> record quotient. A frozen family of physically admissible continuations does:
> identify exactly those carrier values that give the same response
> distribution under every admitted continuation.

That continuation-equivalence quotient is unique up to relabeling and is the
coarsest quotient sufficient for the frozen family. Enlarging the continuation
family can only refine it. But this is not a newly earned DU theorem.
`HC-DU-163` already proved the coarsest action-relative behavioral quotient and
action-refinement law on a sequential superconducting-readout specimen;
`HC-DU-054` and the capability-record Galois closure bank adjacent quotient
mathematics. The independent derivation below is a control, not a duplicate
claim.

What this swing newly adds is a source-grounded Bell-apparatus realization of
that prior theorem, an exact witness that either audit task restores the raw
three-bit carrier, a Blackwell decision-value loss certificate, and a
bare-carrier naturality obstruction. Together they show why the continuation
family—observer boundary, actions, readouts, resources, and horizon—must itself
be independently physical rather than chosen to fit a later target.

The mathematics is not novel. Minimal sufficient statistics,
Blackwell--Sherman--Stein comparison, Myhill--Nerode equivalence,
probabilistic bisimulation, computational-mechanics causal states, and quantum
statistical comparison absorb its components. The DU gain is a corrected type
boundary:

```text
formed physical carrier
  != continuation-complete operational record
  != task-minimal certificate.
```

This is a Grade-3 source-grounded realization plus a scoped Grade-4
naturality/necessity control, not new physics and not a scientific successor.

# Source and absorber positioning

The physical carrier remains the source-pinned eight-outcome apparatus of
Arenskötter et al.,
[Physical Review Research 6, 023061 (2024)](https://doi.org/10.1103/PhysRevResearch.6.023061).
The paper itself says that the Bell projection produces the classical two-bit
information needed to complete teleportation. `HC-DU-201` reconstructed that
map and its finite resource boundary.

The central mathematical absorber is Blackwell's comparison of statistical
experiments. An experiment is at least as informative as another for all
decision problems exactly when the second can be obtained from the first by a
stochastic post-processing in the finite classical setting. See Blackwell,
[“Comparison of Experiments” (1951)](https://digicoll.lib.berkeley.edu/record/112749).
Buscemi extends the comparison/sufficiency structure to finite-dimensional
quantum statistical models using statistical morphisms and completely positive
trace-preserving coarse-grainings; see
[arXiv:1004.3794](https://arxiv.org/abs/1004.3794).

The continuation reading is also adjacent to:

- Myhill--Nerode equivalence, which identifies histories that no admitted
  continuation distinguishes;
- Larsen and Skou's
  [probabilistic testing/bisimulation](https://doi.org/10.1016/0890-5401(91)90030-6);
  and
- Crutchfield and Young's predictive causal-state construction, which groups
  histories with the same conditional future distribution.

Therefore the theorem below is a typed import, independent check, and physical
application, not a claim that DU invented sufficiency or behavioral
equivalence.

# Reused theorem — finite action-family record selection (`HC-DU-163`)

Let `R` be a finite formed carrier and let

```text
K = { K_a(y | r) : a in A }
```

be a frozen family of response kernels for the physically admitted future
actions `A`. Define

```text
r ~_K r'
    iff
K_a(. | r) = K_a(. | r')  for every a in A.
```

Then:

1. `~_K` is an equivalence relation;
2. every admitted response kernel factors through the quotient
   `q_K:R->R/~_K`;
3. if another deterministic quotient `q:R->Q` supports every admitted
   response kernel, then `q(r)=q(r')` implies `r~_K r'`;
4. hence `q` refines `q_K`, and `q_K` is the unique coarsest sufficient
   quotient up to relabeling; and
5. if `K subset L`, then `~_L subset ~_K`, so adding continuations can only
   refine the selected operational record.

## Independent finite proof control

Equality of probability distributions is reflexive, symmetric, and
transitive, proving (1). A response distribution is constant on every
equivalence class by definition, so it descends to the quotient, proving (2).
If every kernel factors through `q`, equal `q` values give equal values of every
kernel, proving (3). Thus every `q`-block lies inside one `~_K` class, which
proves (4). Finally, equality for all kernels in a larger family implies
equality for all kernels in its subfamily, proving (5).

For deterministic tasks `T_i:R->Y_i`, this becomes particularly simple:

```text
r ~ r'  iff  T_i(r)=T_i(r') for every i.
```

The joint signature `(T_1(r),...,T_n(r))` is the minimal common-sufficient
record.

# Scoped naturality control — the bare-carrier obstruction

Suppose a selector sees only a finite set `R`, with no typed coordinates,
dynamics, actions, costs, or distinguished values, and must be equivariant
under every permutation of `R`. The only invariant equivalence relations are:

1. equality, which retains every value; and
2. the indiscrete relation, which retains none.

## Proof

If an invariant equivalence relation identifies one distinct pair `r != r'`,
a permutation maps that pair to any other distinct pair. Invariance therefore
identifies every pair, giving the indiscrete relation. Otherwise no distinct
pair is identified, giving equality.

This does not say physical carriers are bare sets. The Bell apparatus already
distinguishes passage timing, herald polarization, and atomic projection. It
does say that every nontrivial quotient must use some additional typed
structure. Covariance can admit a quotient, but it does not generally select
one: the exhaustive Bell control finds `352` partitions invariant even under
the apparatus-relevant swap of herald and atomic bits, including the
correction quotient.

# Exact Bell record lattice

Write the raw carrier as

```text
R = Z_2^3,
r = (p,h,a),
```

where `p` is passage, `h` the herald result, and `a` the atomic projection.
The correction task uses

```text
C(r) = (p, h XOR a).
```

The exact minimal quotients are:

| Frozen continuation/task family | Minimal classes | Bits |
|---|---:|---:|
| No future distinction | 1 | 0 |
| Bell family only | 2 | 1 |
| Bell sign only | 2 | 1 |
| Teleportation correction | 4 | 2 |
| Correction plus Bell family or sign | 4 | 2 |
| Correction plus herald audit | 8 | 3 |
| Correction plus atomic audit | 8 | 3 |
| Raw identity / every deterministic task | 8 | 3 |

Why does one audit bit restore the full record? From `p`, `h XOR a`, and `h`,
one reconstructs `a`; from `p`, `h XOR a`, and `a`, one reconstructs `h`.

The exhaustive probe checks all `4,140` partitions of the eight-element
carrier against all `64` subsets of the frozen six-task family. For every
family, the joint task kernel is the unique coarsest sufficient partition and
every other sufficient partition refines it. In the linear Boolean arena, the
number of quotient classes is `2^rank`, where `rank` is the `GF(2)` rank of the
admitted task functionals.

For the correction task alone, exactly `16` partitions are sufficient: each
of the four two-element correction classes may remain paired or be split.
Only one of those partitions is coarsest. This makes two distinctions exact:

- **sufficient is not minimal**; and
- **minimal for one task is not universal**.

# Blackwell decision witness

The correction quotient is a deterministic garbling of the raw record. It
preserves correction perfectly, so its optimal correction success is `1`.
But under the uniform ideal carrier:

| Decision problem | Raw carrier | Correction quotient |
|---|---:|---:|
| Guess correction | `1` | `1` |
| Guess herald result | `1` | `1/2` |
| Guess atomic projection | `1` | `1/2` |

Thus the raw carrier strictly Blackwell-dominates the correction quotient
when all decision problems are admitted. The quotient is equivalent only
relative to the frozen correction problem. “Preserve every possible use” is a
valid target-blind rule, but in this arena it selects the full carrier rather
than a nontrivial two-bit record.

# Three objects DU must keep separate

## 1. Formed physical carrier

The material degrees of freedom and detector outputs actually produced and
retained by the apparatus. Its individuation depends on physical resolution,
timing, thresholds, memory, provenance, and acquisition.

## 2. Continuation-complete operational record

The quotient preserving every response available to one independently fixed
observer/controller continuation algebra. This is target-blind relative to a
later held-out target only when the continuation algebra was frozen or
physically selected first.

## 3. Task-minimal certificate

The coarsest quotient sufficient for one declared action or decision family.
In HC-DU-201 this is the two-bit correction value. It can be ideal for the task
while discarding other physically accessible distinctions.

The full carrier need not be the complete quantum ontology. Conversely, a
task-minimal certificate should not be promoted to the apparatus's complete
record merely because it is sufficient for one impressive capability.

# What could physically select the continuation family?

The theorem relocates rather than solves the selector problem. Candidate
physical antecedents include:

- the actual control ports and readout channels causally coupled to the
  controller;
- finite energy, time, memory, bandwidth, and coherence constraints;
- stable closed-loop dynamics and reachable intervention semigroups;
- a physically installed archive/query interface;
- superselection, locality, gauge, or causal constraints on lawful actions;
  and
- a declared horizon over which continuations must agree.

Those objects can make continuation equivalence physical. Merely quantifying
over a mathematically imagined action set cannot. In particular, “all
possible actions” is not a selected observer capability class unless the
physical theory says which actions are possible for that observer and at what
resource cost.

# North-Star consequence

The North-Star chain should be read as:

```text
target-blind physical antecedents
  -> formed material carrier and acquisition
  -> independently selected observer/access/continuation algebra
  -> unique continuation-equivalence record
  -> task-relative certificates and capabilities
  -> reconstruction, duality, or finite remainder.
```

This is stricter than asking whether a state contains “the record.” It also
prevents a common circularity: defining record equivalence by whichever target
one later wishes to reconstruct.

The most informative future reopener is therefore not another quotient of the
same Bell outcomes. It is one physical system in which the admissible
continuation algebra is itself selected by independently frozen dynamics and
resources, after which the continuation quotient predicts a held-out response
without refit.

# Grade, disposition, and nonclaims

- **Reused, not re-earned:** `HC-DU-163` for the coarsest action-relative
  quotient and action refinement, with `HC-DU-054` and the Galois-closure work
  as adjacent prior DU mathematics.
- **Earned at Grade 3:** the source-grounded Bell realization, exact
  audit-restoration witness, and Blackwell task-value loss certificate.
- **Earned as a scoped Grade-4 control:** bare-carrier naturality and the
  necessity of typed structure for any nontrivial equivariant quotient.
- **Novelty:** low as mathematics; useful as a physical specialization and
  North-Star type boundary.
- **Not earned:** physical selection of a continuation algebra, a new quantum
  record ontology, new dynamics, empirical excess, issuance, or Grade 5.
- **Disposition:** bank `HC-DU-202`; keep `NO_READY_SUCCESSOR`.
- **Stop:** do not run more Bell quotient variants. Reopen only when a physical
  candidate independently fixes its continuation algebra and exposes a
  no-refit held-out response, or when two candidate dynamics give different
  continuation-equivalence records for one frozen apparatus.

# Reproduction

```bash
python3 tests/du_action_family_record_selection_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_action_family_record_selection_result.json`. Passing proves
the finite combinatorics and decision witnesses only; it does not validate the
source experiment or physically select the task family.
