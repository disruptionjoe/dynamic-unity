---
title: "Response--record--rule three-separation, zero-error composition, and first-leak boundary"
status: banked_scoped_composition_and_known_mathematics_absorption_result
doc_type: exact_finite_theorem_counterexamples_and_novelty_collision
created: 2026-09-02
claim_id: HC-DU-226
run_id: RUN-20260902-response-record-rule-composition-boundary
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The `HC-DU-223--225` chain now has one exact composition boundary.

Three physically meaningful achievements are independent:

```text
a law selects a source response
  != a material carrier forms one realized record value
  != the source selects the carrier's transition/admissibility rule.
```

They compose into an exact target-preserving handoff only under an additional
condition. Let `x` be a physical completion or history, `t(x)` the held-out
target, and `P(z|x)` the law of the accessible material record. An exact
decoder from the record exists if and only if no one possible record outcome
`z` can be produced by two completions with different target values:

\[
 P(z\mid x)>0\ \text{and}\ P(z\mid x')>0
 \quad\Longrightarrow\quad
 t(x)=t(x').
\tag{1}
\]

For a response-conditioned writer

\[
 P(z\mid x)=W(z\mid r(x)),
\tag{2}
\]

equation (1) says that target-distinct response classes must have disjoint
output support. Randomness is compatible with exact reconstruction; overlap
across target classes is not.

The same theorem applies to a complete finite process record by replacing
`z` with the full observed path. Selecting two different transition kernels
is not enough. If the two path laws share even one possible path, that path
cannot identify which rule governed it with zero error.

Applied to the physical sequence:

1. `HC-DU-223` gives a response exactly sufficient for total electric charge.
2. The Aharonov--Casher bridge in `HC-DU-225` first quotients charge to charge
   parity. Full signed charge is irretrievably lost to every downstream
   record that factors through that bridge.
3. Charge parity selects different fluxoid transition graphs, but their
   finite path supports share the no-slip path. A parity-changing event is a
   one-sided certificate for the single-slip/even-charge rule; absence of
   that event is not a finite zero-error certificate for the odd-charge rule.
4. The `HC-DU-224` fluxoid sector is still a formed material record. It is not
   automatically a record of charge parity or of the history that formed it.

The mathematics is absorbed by statistical sufficiency, zero-error channel
theory, data processing, quantum instruments, and multi-time process theory.
The bounded literature collision does not establish a new mathematical
theorem or physical law. Dynamic Unity's retained contribution is the typed
composition and first-leak localization across one standard-physics chain.
That is useful framework hardening, but it is not yet a standalone
blockbuster or paper-ready theorem.

The disposition is:

```text
THREE_LAYER_SEPARATION_PROVED
+ EXACT_HANDOFF_SUPPORT_CRITERION
+ RESPONSE_SELECTION_DOES_NOT_IMPLY_FORMATION
+ FORMATION_DOES_NOT_IMPLY_TARGET_SUFFICIENCY
+ RULE_SELECTION_DOES_NOT_IMPLY_VALUE_SELECTION
+ FINITE_PATH_OVERLAP_BLOCKS_ZERO_ERROR
+ FULL_CHARGE_LEAK_PRECEDES_PARITY_RECORD_LEAK
+ PROVENANCE_REQUIRES_A_HISTORY_RECORD
+ KNOWN_MATHEMATICS_ABSORPTION
+ DU_TYPED_COMPOSITION_SURVIVES
+ NOVEL_THEOREM_NOT_ESTABLISHED
+ PAPER_STATUS_UNCHANGED
+ NO_READY_SUCCESSOR
```

# 1. Frozen objects and scope

Let:

- `X` be a finite admitted completion or physical-history space;
- `T` be the held-out target alphabet;
- `t:X->T` be fixed before the record is inspected;
- `Q` be a selected physical response alphabet;
- `r:X->Q` be the response map;
- `Z` be the accessible material-record alphabet; and
- `P(z|x)` be the stochastic record experiment.

For a response-conditioned physical writer, equation (2) holds for one
stochastic kernel `W:Q->Delta(Z)`. The factorization is a substantive physical
claim: once `r(x)` is fixed, no omitted completion variable is allowed to
change the record law.

A transition-rule selector has additional structure. For every response
class `q`, it selects a Markov kernel

\[
 K_q(z'\mid z)
\tag{3}
\]

on a material carrier. Given a frozen initial preparation `mu_0`, the endpoint
law after `n` steps is `mu_0 K_q^n`. The complete path law is

\[
 P_q(z_0,\ldots,z_n)
 =\mu_0(z_0)\prod_{j=0}^{n-1}K_q(z_{j+1}\mid z_j).
\tag{4}
\]

Equation (3) is a law, not a realized record value. Equation (4) is a law over
possible histories, not one occurred history. A material record exists only
when the physical carrier occupies a realized, retained state or path. An
accessible record additionally requires the declared readout/archive route.

This claim is finite and exact. It does not say controlled-risk inference is
useless. `HC-DU-070--071` already gives the Blackwell/Le Cam risk-indexed
version. Here “reconstruction” means zero error on every admitted supported
case.

# 2. Exact support-overlap theorem

For every `x`, write

\[
 S_x=\{z\in Z:P(z\mid x)>0\}.
\]

## Theorem 1 — exact record decoder

There exists a deterministic decoder `d:Z->T` satisfying

\[
 d(z)=t(x)
 \quad\text{for every }x\in X\text{ and }z\in S_x
\tag{5}
\]

if and only if equation (1) holds.

### Proof

**Necessity.** Suppose `z` lies in both `S_x` and `S_x'`. Equation (5) gives
`d(z)=t(x)` and `d(z)=t(x')`; therefore `t(x)=t(x')`.

**Sufficiency.** For every record symbol occurring with positive probability,
choose any `x` for which `z in S_x` and set `d(z)=t(x)`. Equation (1) makes
this independent of the chosen completion. Define `d` arbitrarily on record
symbols outside the realized support. Then equation (5) holds. QED.

Equivalently, build the confusability graph on completions by joining `x` and
`x'` when their record supports overlap. Exact target reconstruction holds
if and only if `t` is constant on every connected component. This graph
language adds no new theorem; it makes the first leak visible.

## Corollary 1 — response-to-record composition

Assume equation (2), and assume the target already factors through the
response:

\[
 t=\tau\circ r.
\tag{6}
\]

Then an exact target decoder from `Z` exists if and only if

\[
 \operatorname{supp}W(\cdot\mid q)
 \cap
 \operatorname{supp}W(\cdot\mid q')=\varnothing
\tag{7}
\]

for every pair of reachable response values satisfying
`tau(q) != tau(q')`.

This is the complete finite zero-error composition condition. A stochastic
writer can preserve the target exactly while using many outcomes per target;
those target blocks must merely be disjoint. Conversely, a deterministic
writer can fail if it maps two target-distinct responses to the same value.

## Corollary 2 — irreparable upstream quotient

If `r(x)=r(x')` while `t(x)!=t(x')`, every downstream record law satisfying
equation (2) is identical on `x` and `x'`. No record processing, repetition,
decoder, archive, or consumer downstream of `r` can reconstruct `t`.

This is data processing in its sharpest finite form. Recovering the target
requires changing the physical response family or adding another response
that distinguishes the two completions—not a cleverer decoder.

## Corollary 3 — process-record criterion

For any fixed finite horizon, substitute the path alphabet `Z^(n+1)` and the
path law in equation (4) for `Z` and `P`. Exact reconstruction from the full
finite path exists if and only if target-distinct path-law supports are
disjoint.

Distinct kernels, rates, spectra, or graph topologies need not satisfy that
condition. If both laws permit one common path, observing that path is
ambiguous. Repetition may reduce statistical error while never producing a
finite two-sided zero-error certificate.

# 3. The three strict nonimplications

The exact probe supplies four minimal controls.

## 3.1 Response selection does not imply material formation

Let the selected response equal the binary target, `r(x)=t(x)=x`. The response
is exactly target-sufficient. Let the physical record carrier remain in one
constant blank state for both source values. No material value distinguishes
the target.

This prevents a Noether current, field response, phase, or transition
amplitude from being called a record merely because it is informative in a
formal model.

## 3.2 Material formation does not imply target sufficiency

Let a carrier settle robustly into either of two latched states with the same
law for both source targets. Real values are formed and retained. Their
supports completely overlap across target classes, so no target decoder
exists.

Formation is an ontic physical achievement. Sufficiency is a relation among
that achievement, an observer's accessible record, and a declared target.
Neither erases the other.

## 3.3 Transition-rule selection does not imply value selection

Let one source class admit no-jump, single-step, and double-step transitions,
and let the other admit no-jump and double-step transitions only. The
transition graphs differ. Nevertheless, both rules can produce the same
endpoint and the same all-zero finite path. The source has selected the
carrier's admissibility structure without selecting one realized value or
making every realized path source-identifying.

## 3.4 Endpoint or path sufficiency does not imply provenance

Duplicate each source class with two different formation routes and let the
record law depend only on the source response. The complete record laws agree
between routes. No endpoint or process decoder can recover which route
occurred.

Provenance becomes reconstructible only when the physical process forms and
retains a route-sensitive distinction. Appending a route label afterward is
record refinement only if that label was independently formed; otherwise it
is contract retyping.

# 4. The two first leaks in the charge--fluxoid chain

The preceding three physical controls now compose without being flattened.

## 4.1 Total charge to Aharonov--Casher response

`HC-DU-223` established that the Dirac--Maxwell current and Gauss boundary
flux are exactly sufficient for total enclosed electric charge in the frozen
theory. That response is compressive with respect to the complete matter
state but sufficient for its declared target.

The Aharonov--Casher coupling in `HC-DU-225` has a narrower natural response:

\[
 Q\longmapsto Q\bmod 2e.
\tag{8}
\]

Charges differing by `2e` induce the same interference response. By
Corollary 2, every fluxoid record formed solely through that response loses
the full signed-charge target before any material endpoint is considered.
This is the first leak.

It is not a failure of the coupling. The physical interaction selected its
own quotient. The target must either narrow to charge parity or the response
family must widen.

## 4.2 Charge parity to fluxoid process record

At the symmetric odd-charge point, destructive interference removes single
phase slips while double slips remain. For even charge, single and double
slips are admitted. Thus charge parity selects whether the fluxoid transition
graph is connected or split into parity components.

At every finite horizon the no-slip path is allowed under both rules. Their
finite path supports therefore overlap. By Corollary 3, even a complete
finite fluxoid trajectory is not a two-sided zero-error charge-parity record
under this uncontrolled protocol.

A parity-changing single-slip event is impossible under the ideal odd-charge
rule and therefore certifies the even-charge/single-slip rule in one
direction. Failure to observe such an event does not certify the other rule:
the even rule may simply have realized no single slip. This is the second
leak.

The exact illustrative uniform one-step control has total variation `2/5`
and equal-prior optimal error `3/10`. Those numbers are not a device
prediction. They merely witness the general distinction between different
laws and disjoint support.

Repeated monitoring, a controlled drive, spectroscopy, or a deliberately
prepared write pulse may make the error small or produce disjoint finite
supports. Each changes the process/instrument contract. It can be a valid
physical advance; it must not be attributed to the uncontrolled endpoint.

# 5. Quantum scope

The theorem above is stated for an accessible classical archive. Quantum
mechanics strengthens rather than removes the typing burden.

A quantum instrument contains both an outcome law and an outcome-conditioned
state transformation. Two instruments can have the same effects and outcome
probabilities while producing different conditional continuations. This is
the boundary already banked in `HC-DU-208` and formalized by the
Davies--Lewis instrument framework. A terminal POVM or endpoint distribution
therefore cannot replace a complete instrument or multi-time process.

For quantum carriers, perfect one-shot discrimination requires the relevant
conditional quantum states to have orthogonal support under the admitted
measurement resources. Once a classical record is formed, equation (1)
applies to its accessible outcome channel. A process-tensor treatment is
needed when later interventions can expose memory or continuation differences.

This result does not claim that every quantum record must be classical at
formation. It says that whichever physical object is admitted as the record
must carry the target through its complete accessible discrimination
contract. Calling it a quantum state, history, or instrument does not remove
that obligation.

# 6. Prior-art and absorber collision

The component mathematics is occupied.

1. Blackwell's comparison of statistical experiments supplies the standard
   garbling/sufficiency order and decision-theoretic meaning of an informative
   channel: [Blackwell 1953](https://doi.org/10.1214/aoms/1177729032).
2. Shannon's zero-error theory supplies confusability as the obstruction to
   exact decoding through a noisy channel: [Shannon
   1956](https://doi.org/10.1109/TIT.1956.1056798).
3. Davies and Lewis introduced quantum instruments precisely to retain both
   measurement outcome and state transformation: [Davies--Lewis
   1970](https://doi.org/10.1007/BF01647093).
4. Quantum combs and process tensors already type multi-time interventions
   and outcome-conditioned continuations: [Chiribella, D'Ariano, and
   Perinotti 2009](https://doi.org/10.1103/PhysRevA.80.022339), [Pollock et
   al. 2018](https://arxiv.org/abs/1512.00589).
5. Conditional instrument composition and post-processing are treated
   directly by [Leppajarvi and Sedlak
   2020](https://arxiv.org/abs/2010.15816).
6. Hartle's records-first decoherent-histories formulation connects recorded
   alternatives to decoherent history sets, while still requiring a declared
   coarse graining and record relation: [Hartle
   2016](https://arxiv.org/abs/1608.04145).
7. Spectrum broadcast structure gives a strong standard account of
   redundantly accessible objective state information under its objectivity
   assumptions: [Korbicz, Horodecki, and Horodecki
   2013](https://arxiv.org/abs/1305.3247).

The support theorem is elementary zero-error statistics. The three
nonimplications also follow from ordinary distinctions among a response map,
a stochastic process, its realized sample, and a history label. The
superconducting phenomena are established standard physics.

The bounded collision did not locate one source presenting exactly DU's
response-selection/material-formation/transition-rule-selection/provenance
composition ladder. That search result is not evidence of novelty. The honest
classification is:

```text
KNOWN COMPONENT MATHEMATICS
+ KNOWN PHYSICAL SPECIMENS
+ DISTINCT DU TYPED SYNTHESIS AND FIRST-LEAK AUDIT
+ NOVEL THEOREM NOT ESTABLISHED.
```

# 7. What is publishable and what is not

This result is not a new law of nature, a new quantum theorem, or a standalone
paper-ready theorem. A paper whose central claim were only equation (1) would
be absorbed immediately by zero-error and sufficient-statistic theory.

It can become a valuable theorem section or methods spine in a broader paper
if that paper contributes at least one nonabsorbed object, for example:

1. a physically selected response-to-process-record writer whose complete
   target and provenance contract satisfies the composition condition without
   target fitting;
2. a natural physical class for which a materially complete no-section
   theorem proves that no such handoff can exist;
3. a finite record-conditioned physical remainder surviving every admitted
   response, instrument, archive, and consumer completion; or
4. a cross-platform no-refit theorem showing that the same physically selected
   interface preserves the target quotient in more than one arena.

Until one of those appears, paper status must remain unchanged. No Drafting
Factory seed or publication promotion is warranted by this wave.

# 8. North-Star consequence

The most useful change is a more precise search target. “Find a record” is too
coarse. A candidate physical chain must now say where it sits:

```text
source/history
  -> selected response quotient
  -> selected material transition/process law
  -> realized retained value or path
  -> provenance-bearing archive
  -> observer access
  -> fixed consumer/target consequence.
```

At every arrow, test both:

1. **descent:** does the downstream law depend only on the upstream object it
   claims to consume? and
2. **separation:** do target-distinct upstream classes remain distinguishable
   under the required exact or controlled-risk standard?

This prevents work at a later layer from being used to repair information
already lost earlier. It also credits partial positives correctly: selecting
a response, forming a memory, and protecting a transition sector are each
real achievements even when the complete handoff remains open.

The exact scientific reopener remains physical, not combinatorial:

> one natural source-pinned process must select a material value or finite
> process record whose complete accessible law preserves its declared source
> target and occurrence provenance under a precommitted consumer—or a theorem
> must show that this is impossible for one physically natural complete class.

No further synthetic support variants are warranted. The repository remains
`NO_READY_SUCCESSOR` after banking this boundary.

# 9. Reproducibility

Run:

```bash
python3 tests/du_response_record_rule_composition_probe.py --write-artifact
```

The exact probe returns `16/16`. It exhausts all `49` nonempty binary-target,
three-output support pairs; checks the disjoint-support positive; supplies the
three nonimplication controls; verifies finite path overlap through horizon
five; localizes the full-charge and parity leaks; and proves the formation
route is absent from the frozen process law.

The deterministic artifact is
`tests/artifacts/du_response_record_rule_composition_result.json`.
