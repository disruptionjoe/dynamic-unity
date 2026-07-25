---
title: "Science Council commercial scientist — open-frontier advancement wave"
status: completed_persona_work
doc_type: council_persona_memo
created: 2026-07-24
run_id: RUN-20260724-191339-science-council-open-frontier-advancement
persona: commercial_scientist
claim_grade: "EXACT CONVEX-SEPARATION SPECIALIZATION / PHYSICAL PROPER-TIME MARGIN OPEN"
banked: false
seeded: false
---

# Commercial scientist: compile a robust physical history certificate

## Selection

The strongest repository-wide move is the coupled `HC-DU-034B/036B`
physical-history build, narrowed into a **robust history-certificate
compiler**.

The ideal signed-port identity already works. The practical question is
whether a real instrument's complete expected record lies outside every
calibrated classical-history explanation after preparation and measurement
error, drift, leakage, phase error and provenance failures are admitted.
Answering that question supplies a cheap stop/go decision before an expensive
proper-time experiment and provides the formed record/refinement object
needed by later finality-cost work.

## Robust certificate construction

Let each trial produce one finite recorded outcome \(k\), including the
setting, recombination port, clock result and provenance flags. Freeze:

- a convex null set
  \(C=\operatorname{conv}\{p_\theta:\theta\in\Theta\}\) containing every
  admitted classical-history instrument;
- an alternative set \(A\); and
- bounded scores \(w_k\in[-1,1]\).

Define

\[
g^*=
\max_{\|w\|_\infty\le1}
\left[
\inf_{q\in A}w\cdot q-
\sup_{p\in C}w\cdot p
\right].
\]

For finite null and alternative vertices, compute this with the linear
program

\[
\max_{w,g}g
\]

subject to

\[
w\cdot q_\ell-w\cdot p_j\ge g
\quad\text{for every }j,\ell,
\qquad -1\le w_k\le1.
\]

Then:

- \(g^*>0\) means the frozen instrument classes are linearly separable, and
  \(w^*\) is the optimal bounded certificate;
- \(g^*\le0\) means the admitted outcome space cannot certify the proposed
  distinction, so the platform should stop or independently enlarge its
  instrument; and
- for a point alternative \(q\), the optimum is the \(L^1\) distance from
  \(q\) to \(C\).

If the calibrated null ceiling is \(b\), alternative floor is \(a\), and
\(g=a-b>0\), a conservative independent-shot gate is

\[
n\ge
\frac{
2\left(\sqrt{\ln(1/\alpha)}+\sqrt{\ln(1/\beta)}\right)^2
}{g^2}.
\]

Calibration uncertainty must be charged to the null ceiling and therefore
reduces the usable margin.

## Implementation-provenance control

Take Pauli operations

\[
U=ZX=iY,\qquad XZ=-ZX.
\]

Compare two controlled implementations:

\[
M_+:(U_0,U_1)=(ZX,ZX),
\]

\[
M_-:(U_0,U_1)=(ZX,XZ).
\]

Every target-only branch channel is the same,

\[
\rho\mapsto Y\rho Y,
\]

but with a coherent route control prepared in \(|+\rangle\),

\[
\langle X_C\rangle_{M_+}=+1,\qquad
\langle X_C\rangle_{M_-}=-1.
\]

Dephasing the route control returns
\(\langle X_C\rangle=0\).

An endpoint-channel record is therefore exactly insufficient under coherent
control. Implementation/relative-phase provenance absorbs the witness. The
result is **interface incompleteness**, not an irreducible physical
remainder.

## Frozen controls

The certificate requires:

- null and alternative instrument classes frozen before witness data;
- a finite complete outcome alphabet;
- randomized settings that cannot track drift;
- all ports and invalid preparations retained;
- explicit phase-reference and route-control resources;
- full trial, setting, port and clock-result provenance;
- null vertices covering arbitrary history weights plus admitted preparation
  and measurement error, leakage, detector asymmetry, phase noise and drift;
  and
- independence within the preregistered sampling window.

Required arms are coherent, deliberately dephased, endpoint-only,
randomized-provenance, commuting-operation and known-relative-phase
controls. Nonstationary drift requires a sequential or martingale analysis,
not the displayed independent-shot gate.

## Novelty and candidate ledger

Convex separation, dual norms, implementation-dependent coherent channel
control, relative phase under coherent routing and the finite concentration
bound are known terrain.

| Candidate | Honest grade | Failure condition |
|---|---|---|
| Robust Instrument-Class Separation Theorem | Exact known convex-analysis specialization | The convex hulls overlap, or no positive separation exists in the admitted outcome space |
| Endpoint-to-Provenance Refinement Proposition | Exact physical control; known coherent-control terrain | Target-only channels differ, or the controlled circuit does not return the predicted signs |
| Proper-Time Robust Separability Hypothesis | Open physical hypothesis | The physical alternative lies inside the calibrated null cone, or its margin is below systematic uncertainty |
| History-Certificate Efficiency \(g^2/\text{complete cost}\) | Engineering metric, not a law | It fails to predict preregistered decision time or cost across platforms |
| Implementation-Provenance Completeness Hypothesis | Standard-quantum null | A residual survives a complete instrument/dilation/process description and all ordinary phase, memory and control-error models |

The potentially useful conjunction is a compiler combining full physical
instrument uncertainty, retained-port provenance, resource cost and the
`HC-DU-036B` refinement verdict, then carrying the same record schema into
an adversarial distributed-history fixture. Its novelty is
search-incomplete.

## Minimum executable product

Build a history-certificate compiler that accepts calibrated null and
alternative distributions and returns:

1. the optimal score \(w^*\);
2. robust margin \(g^*\);
3. calibration and science-shot requirements;
4. total preparation/coherence cost; and
5. which admissible record refinement changes the verdict.

Run the Pauli-order control first, followed by dephased and
randomized-provenance nulls, a noisy equal-channel/different-implementation
fixture, and only then a specified proper-time-history instrument. Stop the
platform if no accessible complete outcome record has positive margin after
calibration uncertainty.

## Stops and unused paths

Stop:

- adding ideal Bell or two-history examples except as calibration;
- treating frequency shift, dephasing or visibility loss as history
  certification;
- calling ordinary phase, implementation, memory or geometric holonomy
  perspectival curvature;
- pricing formation-to-finality before an instrument passes the assay; and
- deriving geometry, GU or cosmology from an unselected record interface.

Preserve as exploratory options:

- multi-history character pooling across every recombination port;
- sequential e-value certification under slow drift;
- automated convex-null construction from process tomography;
- cost-aware optimization over instrument time and coherence;
- an unchanged distributed-database twin;
- zero-knowledge certification without history disclosure; and
- a finite admissible-refinement enumerator.

## Plain-English meaning

The useful question is no longer whether ideal quantum algebra can
distinguish coherent histories—it can. The question is whether the real
experiment can beat every ordinary explanation its hardware permits.

The compiler is a fraud detector: enumerate the mundane explanations, find
the cheapest statistic that excludes all of them, and calculate the
experiment bill. If there is no robust gap, do not run the expensive
experiment. If there is a gap, the result identifies exactly which record
was missing and which provenance repair absorbs it.
