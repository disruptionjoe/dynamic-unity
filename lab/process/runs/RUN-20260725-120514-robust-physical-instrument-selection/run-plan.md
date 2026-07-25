---
run_id: RUN-20260725-120514-robust-physical-instrument-selection
status: completed_scoped_selector_and_no_go
repository: dynamic-unity
workflow: robust physical instrument selection theorem or no-go
authority: "Joe direct chat: Yeah, let's go after it."
starting_revision: 860e149c7914276d1ff8965f4df468b91c33f95b
claim_grade: "OPEN RESEARCH / RESULTS GRADED BY EXECUTED EVIDENCE"
---

# Robust Physical Instrument Selection

## Purpose

Execute the first dependency left by the formed-sharp descent swing:

> Under one independently frozen source process, coupling family,
> perturbation class, action algebra, decoder, resource ledger, and matched
> foils, can physical constraints select one source--pointer--archive
> instrument orbit, or can the remaining freedom be classified exactly?

The run may return a scoped theorem, a quantitative bound, a no-go, an
absorber into established measurement theory, or a precise missing-premise
classification. It may not infer uniqueness from a supplied basis, hide a
selective continuation inside a POVM, or call an implementation difference
new physics.

## Frozen contract

### Source and candidate family

- Source system: one qubit with frozen action generator \(Z\), extended by a
  second internal qubit only for the degenerate-sector continuation control.
- Candidate record axes:
  \(n_\theta=(\sin\theta,0,\cos\theta)\).
- Candidate binary pointer family:
  \[
  M_0=\sqrt{1-\epsilon}P_+^{n_\theta}
      +\sqrt{\epsilon}P_-^{n_\theta},\qquad
  M_1=\sqrt{\epsilon}P_+^{n_\theta}
      +\sqrt{1-\epsilon}P_-^{n_\theta},
  \]
  with \(0\leq\epsilon\leq1/2\).
- Pointer and archive begin in declared blank states. Pointer-to-archive
  copying, archive bit-flip noise, decoder, and all retained route or
  environment ports are explicit.

### Perturbations and resources

- Sweep \(\theta\), pointer crossover \(\epsilon\), and archive flip rate
  \(q\) over predeclared finite grids.
- Compare candidates at matched Hilbert-space dimensions, one
  system--pointer interaction, one pointer--archive copy, one archive bit,
  and the same decoder.
- A three-copy majority decoder is allowed only as a separately charged
  resource control.

### Selection receipts

Keep separately typed:

1. pointer record distinguishability;
2. observer-accessible distinguishability after archive noise;
3. source-action disturbance;
4. repeatability;
5. equality of outcome effects;
6. equality of selective instruments;
7. equality of held-out continuations;
8. full action-algebra preservation;
9. coherent route distinguishability; and
10. microscopic dilation identity.

### Matched foils

- **Conjugate-axis foil:** the same pointer/archive and resource contract,
  with \(\theta=\pi/2\).
- **Continuation-twist foil:** the same sharp sector effects and archive, but
  an outcome-conditioned unitary acts inside a degenerate sector.
- **Degeneracy control:** the continuation twist is invisible to a source
  generator that omits the internal action, and visible when the internal
  splitting is independently nonzero.
- **Archive-noise foil:** the pointer is unchanged but observer access is
  degraded by a declared bit-flip channel.
- **Coherent-routing control:** target and foil are coherently selected while
  route and environment ports are retained; any recovered difference is
  classified as ordinary implementation information unless it exceeds the
  complete standard-quantum model.

## Exact targets

1. Verify the binary information--disturbance identity
   \[
   D=1-2\epsilon,\qquad
   v=2\sqrt{\epsilon(1-\epsilon)}=\sqrt{1-D^2},
   \]
   and
   \[
   \left\|\Phi_{n_\theta}^*(Z)-Z\right\|_\infty
   =(1-\sqrt{1-D^2})|\sin\theta|.
   \]
2. Derive the resulting class-relative alignment bound whenever \(D>0\).
3. Test whether source/action preservation plus matched record quality rejects
   the conjugate foil robustly across the frozen grid.
4. Test whether the full action algebra rejects the continuation twist and
   whether degeneracy reopens it.
5. Propagate pointer distinguishability through the archive and charged
   decoder without confusing latent sharpness with observer access.
6. Classify the maximal selected object: unique instrument, instrument orbit,
   or only an equivalence class relative to the declared actions.

## Landscape and novelty gate

Compare every central statement with Wigner--Araki--Yanase constraints,
quantum nondemolition measurement, Lüders/repeatable instruments,
information--disturbance tradeoffs, Stinespring/Naimark freedom, and ordinary
coherent control. The component mathematics is presumed established unless a
source-pinned audit shows otherwise.

Potential Dynamic Unity value lies in the unchanged conjunction of physical
source selection, complete selective instrument identity, end-to-end archive
access, continuation foils, route retention, and an explicit quotient over
unobservable implementation freedom. That conjunction must not be promoted
as a new physical law merely because it is useful program architecture.

## Stopping rule

Return the strongest exact no-go if any of the following remains:

- a phase, dilation, or within-sector transformation invisible to every
  frozen action and record;
- a degeneracy not broken by independently justified source structure;
- an archive or decoder choice supplied after seeing the desired result; or
- a coherent-route signal completely reproduced by the declared standard
  quantum implementation.

No ontology, prediction, theorem ID, law, hypothesis ID, paper priority, or
Factory state changes unless the result beats the strongest adjacent account
with an independently derived premise and a held-out discriminator.

## Validation

1. deterministic self-checking probe and canonical JSON artifact;
2. exact analytic identities checked against complete matrix instruments;
3. tolerance and finite grids declared before reading verdicts;
4. matched-resource and degeneracy controls pass;
5. prior formed-sharp probes regress unchanged;
6. JSON/YAML parse, local links, `git diff --check`, explicit-path staging,
   commit, push, and repository session finish succeed.

## Completion receipt

The frozen swing completed without refitting its target and foil contracts:

- `tests/du_robust_physical_instrument_selection_probe.py` passes `31/31`;
- the explicit system--pointer--archive isometries recover the analytic
  instruments on the full predeclared grid;
- pointer distinction, residual visibility, source-action disturbance, and
  coupling symmetry obey the two exact identities stated in the target;
- for every \(D>0\), exact source-action nondisturbance selects \(+Z\) or
  \(-Z\), one PVM orbit up to outcome relabeling;
- the exact formula supplies the approximate-alignment bound and the \(D=0\)
  null correctly selects nothing;
- a matched conjugate foil has the same record quality and finite resource
  contract but pays the predicted disturbance;
- a within-sector twist preserves effects, archive, repeatability, and the
  central source action while changing a held-out selective continuation by
  trace distance one;
- a full block action algebra rejects that twist, while source energy alone
  is blind at exact degeneracy and acquires disturbance \(2|\mu|\) after an
  independent internal splitting \(\mu\) is supplied;
- archive noise gives
  \(D_{\mathrm{access}}=|1-2q|D\), and charged three-copy majority decoding
  improves but does not make nonzero noise exact;
- coherent target-versus-twist routing reduces route-\(X\) visibility from
  \(1\) to \(1/2\), exactly as predicted by the complete standard-quantum
  implementation; and
- distinct retained-environment dilations induce exactly the same reduced
  effective instrument.

The maximal selected object is therefore a source-aligned effective Lüders
instrument orbit relative to the declared source, QND candidate family, full
action algebra, archive, decoder, and resources. A unique microscopic
apparatus is not selected and is not identifiable through the reduced
instrument. The component mathematics is occupied WAY-adjacent, QND,
Lüders, commutant, instrument, and dilation terrain; no theorem ID,
hypothesis ID, physical law, prediction, ontology, paper priority, or Factory
state is promoted.

The integrated result is
`explorations/robust-physical-instrument-selection-theorem-and-no-go-2026-07-25.md`.
The next reopener is a laboratory-motivated additive total-conservation model
with a calibrated apparatus-asymmetry budget, declared perturbation ball,
complete self-consistent instrument tomography, and a frozen archive/decoder.

Validation completed:

- the new artifact is deterministic at SHA-256
  `ce0a8b7f4c07c295433140d421b0a41ac22570020655cca905d96b4e561da407`;
- a fixed-seed `500`-case off-grid stress test has maximum analytic-versus-
  matrix error `6.307e-15`;
- related probes regress at `34/34`, `36/36`, `16/16`, and `24/24`;
- the new Python source compiles and all JSON/YAML files parse;
- local Markdown links resolve; and
- repository whitespace checks pass; explicit-path staging, commit, push, and
  session finish follow this receipt under repository custody.
