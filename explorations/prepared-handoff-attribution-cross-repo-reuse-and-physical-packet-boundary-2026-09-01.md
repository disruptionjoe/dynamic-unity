---
title: "Prepared-handoff attribution, cross-repo reuse, and physical-packet boundary"
status: banked_scoped_cross_program_attribution_and_reuse_result
doc_type: theorem_boundary_exact_control_and_cross_repo_reuse_audit
created: 2026-09-01
claim_id: HC-DU-218
run_id: RUN-20260901-prepared-handoff-attribution-and-cross-repo-reuse
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The first task in this wave was a read-only audit of Temporal Issuance and Time
as Finality. It found that the proposed instrument-to-feedback build was mostly
already computed across the three repositories. Rebuilding it would have added
little information.

The nonredundant result is the exact attribution theorem joining those pieces:

```text
PREPARED_HANDOFF_CONDITIONAL_RECONSTRUCTION
+ ACCESS_RELATIVE_CAPABILITY_WITH_EXPLICIT_RESOURCE
+ FIXED_SOURCE_DISCLOSURE_NOT_ISSUANCE
+ AUTONOMOUS_INTERFACE_SELECTION_UNEARNED
+ NO_PHYSICAL_REMAINDER_FROM_BRANCH_UNCERTAINTY
+ PUBLIC_PHYSICAL_HANDOFF_STILL_INCOMPLETE
+ NO_REDUNDANT_REBUILD
```

In plain terms:

> A complete, precommitted apparatus can form a record, route it into a fixed
> controller, and let that record determine a later physical response. The
> record can then reconstruct which response occurred. That is a real positive
> conditional result. It does not follow that the isolated source selected the
> apparatus, that a genuinely new source possibility was issued, or that
> uncertainty before reading the record was a physical remainder.

The same event therefore receives different correct verdicts under different
questions. Dynamic Unity asks whether the target factors through the complete
record. Time as Finality asks which actions become available through access to
that record. Temporal Issuance asks whether the source escaped every admitted
pre-action completion. Those are not rival interpretations of one scalar
score.

The exact finite control uses a record alphabet `{0,1}` and a locked consumer
whose separate downstream response alphabet is `{2,5}`. The unconditioned
target image is `{2,5}`, while each full-record fibre has a singleton target
image. A constant coarse summary, an omitted target-relevant nuisance, or a
record treated as source provenance all fail. The target is a downstream
consumer response, not a literal copy of the record field.

The public physical specimens remain incomplete in complementary ways:

- the Peronnin sequential-readout packet forms and exposes a real one-run trace
  but reports no outcome-conditioned physical action; and
- the Rigetti/Riverlane packet joins returned-shot records, decoder status,
  timing, a documented conditional action, and later response, but lacks an
  all-attempt census, complete controller route/state, waveform lineage, and
  archive/reset semantics.

No new detector or feedback toy is needed to establish this attribution. A
future physical promotion requires a genuinely more complete packet, not a
fourth restatement of the same finite circuit.

# 1. What the sibling repositories had already computed

## 1.1 Temporal Issuance

The [whole-family completion barrier
classifier](../../temporal-issuance/tests/artifacts/whole_family_completion_barrier_classifier_result.json)
already distinguishes four completion absorbers. Two are decisive here:

- `PROVENANCE_ACTION_COMPLETION_ABSORPTION` fires when the action, witness,
  provenance, and task delta are preformed; and
- `CAPABILITY_COMPLETION_ABSORPTION` fires when a fixed source plus access,
  schedule, finality, or readout already determines the task change.

The [capability-transport source-action
fixture](../../temporal-issuance/tests/artifacts/capability_transport_source_action_fixture_result.json)
also says that a genuine task-menu handle may be `TAF_EXPRESSIBLE_READOUT` or
`FIXED_SOURCE_DISCLOSURE` without being source action. Escaping that result
would require a concrete pre-action family-noncompletion rule, not merely a
feedback loop or a fresh event label.

Therefore a precommitted measurement and controller packet can be physically
real, conditional, and useful while remaining disclosure relative to TI's
question.

## 1.2 Time as Finality

The [record-conditioned capability discriminator
gate](../../time-as-finality/results/T582-w192-record-conditioned-capability-discriminator-gate-v0.1-results.md)
already gives the relevant access control. A changed task becomes available
when an explicit state/record resource is accessible, but readout, explicit
state, description, fixed-source, and resource-completion absorbers all fire.
The capability delta is real relative to that access contract; it is not
evidence that the source created a new law or state family.

The [full-record sufficiency
boundary](../../time-as-finality/results/weak-measurement-full-record-sufficiency-boundary-v0.1-results.md)
also closes a common loophole. An auxiliary channel that beats a plotted
average, threshold, or coarse dashboard has not beaten the ordinary record.
The complete preregistered event-level transcript must be held fixed.

The detector work supplies reusable packet discipline:

- [detector export
  map](../../time-as-finality/results/detector-stack-export-map-v0.1-results.md);
- [real-detector packet
  schema](../../time-as-finality/results/real-detector-packet-schema-audit-v0.1-results.md);
- [pre-event
  manifest](../../time-as-finality/results/detector-preregistration-manifest-v0.1-results.md);
  and
- [held-out no-refit prediction
  packet](../../time-as-finality/results/T547-aprd-held-out-prediction-packet-v0.1-results.md).

These schemas are stronger than every conditional laboratory claim needs. In
particular, TaF's separated-authority and public-review gates must not be
silently promoted into universal laws of physical recording. The transferable
core is claim-relative: preserve the fields on which the claimed target,
provenance, access, or future operation depends.

## 1.3 Dynamic Unity

Dynamic Unity had already supplied the remaining pieces:

- `HC-DU-162`: physical one-run trace formation, plus exact compression,
  provenance, archive, and reset boundaries;
- `HC-DU-168`: 8,000 joined returned Rigetti/Riverlane rows with records,
  decoder status, timing, a documented conditional action, and later response,
  but not implementation completeness;
- `HC-DU-204`: matched producer-consumer relabeling descent and the physical
  gauge boundary; and
- `HC-DU-205`: exact consumer freedom—one writer and formed record algebra admit
  four distinct downstream policies.

`HC-DU-217` then admitted a precommitted calibrated instrument as a legitimate
physical antecedent for a conditional experiment while withholding autonomous
interface and complete-handoff credit.

The missing result was not another circuit. It was a theorem stating which
claim each already-computed component can support when they are composed.

# 2. Prepared-handoff attribution theorem

Let `W_a` be the lawful completion fibre under one precommitted antecedent

\[
 a=(L,P,I,A,C),
\]

where `L` is the source law, `P` the preparation, `I` the instrument, `A` the
archive/access contract, and `C` the consumer/controller. Let

\[
 r:W_a\to R
 \qquad\text{and}\qquad
 t:W_a\to T
\]

be the complete declared record and held-out downstream target.

## Theorem 1 — conditional reconstruction

The record reconstructs the target relative to `a` exactly when

\[
 \ker r\vert_{W_a}\subseteq\ker t\vert_{W_a}.
\tag{1}
\]

Equivalently, every target image on a fixed record fibre is a singleton. A
decoder `d:R -> T` then exists with `t=d \circ r` on `W_a`.

This is a conditional reconstruction result. It does not require the isolated
source to select `I`, `A`, or `C`; their physical preparation and precommitment
are part of the antecedent and must be attributed as such.

## Theorem 2 — unconditioned branching is not a remainder

Suppose `t(W_a)` contains more than one value but equation (1) holds. The
law/preparation/handoff packet permits multiple branches before the record is
known, and the record identifies the realized target branch. There is no
same-record/different-target witness. Therefore plural unconditioned target
support is ordinary branch uncertainty, not a Dynamic Unity physical
remainder.

A remainder requires

\[
 \exists w_1,w_2\in W_a:
 r(w_1)=r(w_2)
 \quad\text{and}\quad
 t(w_1)\ne t(w_2).
\tag{2}
\]

## Theorem 3 — capability attribution changes the comparison

If withholding record access changes the consumer's executable action menu,
then a real access-relative capability difference exists. But the two cases
do not lie in one access-complete antecedent fibre: the access resource differs.
The result is attributed to the supplied physical access/consumer contract,
not to source growth or a target-independent new law.

## Theorem 4 — fixed-source handoff is not issuance

If the source, preparation, random seed/completion family, instrument, archive,
access route, and consumer are all part of a fixed pre-action family, then
formed records and later conditioned actions are disclosure relative to that
family. Neither blank-to-written formation nor outcome-conditioned feedback
supplies TI's missing pre-action family-noncompletion witness.

## Theorem 5 — conditional success does not imply autonomous selection

Equation (1) can hold for a handoff prepared by an experimenter. Autonomous
natural-interface selection would additionally require the admitted
source-plus-environment dynamics to select the relevant instrument and matched
writer-consumer orbit, or prove complete physical descent across its residual
freedom. Conditional reconstruction does not imply that stronger claim.

Together these statements form an attribution theorem, not a new dynamical
law. Their value is to prevent one positive result from being overclaimed and
one negative result from erasing a legitimate conditional success.

# 3. Exact finite control

The locked control has two source histories. The prepared instrument writes
record `0` or `1`. A consumer fixed before either history maps them to distinct
physical continuations:

| record | action | held-out target |
|---:|---|---:|
| 0 | idle | 2 |
| 1 | phase kick | 5 |

The target alphabet `{2,5}` is disjoint from the record alphabet `{0,1}`. The
target is therefore not the identical database field copied twice. This does
**not** by itself discharge the stronger anti-copy burden: every deterministic
finite response can be re-encoded as a function of its input. Independent
physical precommitment and no-refit transfer must establish that the consumer
was not chosen to encode the held-out answer. The exact results are:

1. law/preparation/instrument/consumer target image: `{2,5}`;
2. target image conditional on record `0`: `{2}`;
3. target image conditional on record `1`: `{5}`;
4. target image on one constant summary fibre: `{2,5}`;
5. adding an omitted binary nuisance reopens both record fibres;
6. allowing measurement flips gives each record value two possible source
   histories, so outcome is not provenance;
7. one writer and record support four target signatures under four consumers;
8. matched record/consumer relabeling preserves the response; and
9. unmatched relabeling changes it.

The exact control earns conditional reconstruction only for the complete
locked packet. It does not earn physical anti-copy independence. It
simultaneously validates the coarse-record, hidden-nuisance, provenance,
consumer-selection, and physical-gauge stop conditions.

# 4. Collision with the physical packets

## Peronnin sequential readout

The source forms an actual digitized trace, derives a calibrated statistic and
binary result, and uses the first outcome to herald analysis of a second
readout. That is a real record-conditioned response statistic. The first
outcome does not choose a later physical pulse or command. The specimen is
therefore formation/access positive and feedback negative.

## Rigetti/Riverlane fast feedback

The public packet is stronger in the complementary direction. It joins 8,000
returned repetitions to classified measurements, decoder status, timing, a
documented conditional `X` branch, and a later response. This is genuine
returned-shot record/action/response evidence.

It still lacks the census and joins required to identify every admitted
attempt and implementation path: pre-return triggers, rejected attempts,
retries, main physical program and firmware/configuration, controller route
and hidden state, raw waveform lineage, and archive/access/reset policy. Those
unknown strata can carry target-relevant differences. More returned shots do
not identify them.

The two specimens together show that all component arrows are physically
ordinary and realizable. They do not compose into one public
implementation-complete packet merely because different experiments realize
different arrows.

# 5. What changed

The North-Star gate becomes more permissive and more precise:

```text
For a conditional reconstruction claim:
  complete precommitted prepared handoff is sufficient antecedent.

For an autonomous-classicality claim:
  source-plus-environment selection of the handoff remains required.

For a physical-remainder claim:
  same complete record + same complete antecedent + different target is required.

For a source-issuance claim:
  pre-action completion resistance is independently required.
```

This is progress because it identifies a positive result DU can legitimately
earn without first solving autonomous measurement or new physics. It also
prevents the easier result from being mistaken for the blockbuster.

No current public packet earns the complete physical positive. The local
theoretical boundary is now closed enough that another toy feedback circuit
would be redundant. The exact physical reopener is a precommitted packet with:

1. full event/attempt identity, including rejects and retries admitted by the
   claim;
2. raw and calibrated record lineage;
3. per-attempt controller input, route/state equivalence, command, and applied
   action;
4. downstream held-out response;
5. archive/access/reset/resource semantics; and
6. a locked target comparison with no post-result refit.

That path may require a public implementation-complete dataset or laboratory
collaboration. Under DU's local-hardware rule, it is an awareness reopener, not
a reason to keep circling local emulations.

# Grade and disposition

**Earned at scoped Grade 4:**

- exact prepared-handoff attribution theorem;
- exact conditional-reconstruction positive control;
- exact coarse-record, hidden-nuisance, provenance, consumer-freedom, and
  matched-orbit controls;
- cross-repository reuse map without sibling mutation; and
- physical-packet disposition showing why no rebuild is informative.

**Not earned:**

- one implementation-complete public physical handoff;
- autonomous natural-interface selection;
- Temporal Issuance source action;
- a physical remainder;
- a new quantum prediction, new law, or new physics; or
- a ready scientific successor.

# Reproducibility

Run:

```bash
python3 tests/du_prepared_handoff_cross_repo_attribution_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_prepared_handoff_cross_repo_attribution_result.json` and
reports `13/13` checks.
