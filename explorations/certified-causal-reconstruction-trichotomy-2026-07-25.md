---
title: "Certified Causal Reconstruction trichotomy — finite exact specialization"
date: 2026-07-25
status: completed_scoped_theorem
doc_type: exploration
claim_grade: "EXACT FINITE RATIONAL THEOREM SPECIALIZATION / PHYSICAL COMPLETENESS AND NOVELTY OPEN"
candidate_ids:
  - HC-DU-036C
paper_id: DU-PAPER-007
lanes:
  - lane_1
  - lane_7
channels:
  - CH-FORMAL
  - CH-MODEL
probe_ref: tests/du_certified_causal_reconstruction_trichotomy_probe.py
artifact_ref: tests/artifacts/du_certified_causal_reconstruction_trichotomy_result.json
---

# Certified Causal Reconstruction trichotomy — finite exact specialization

## Plain result

Dynamic Unity now has an exact finite answer to a question its earlier
compiler left open:

> Once the certified record, interventions, admissible completion class, and
> resource order have been frozen without reading the desired answer, how
> close can every admitted physical response come to factoring through that
> record?

For finite exact-rational binary-response contracts, exactly one scientific
branch holds:

1. **base reconstruction** — the certified record already recovers every
   declared intervention response;
2. **refined reconstruction** — the base record fails, but at least one
   independently fixed completion recovers every response, with all
   resource-Pareto-minimal repairs reported; or
3. **class-relative remainder** — every member of the frozen finite
   completion class fails by at least one exact positive total-variation
   margin.

If the record, outcome alphabet, intervention family, completion class, or
resource order is not properly frozen, the program returns
`INCOMPLETE_CONTRACT`. That is non-adjudication, not a fourth scientific
outcome.

The executable specialization passes `11/11` controls twice with byte-
identical artifact SHA-256
`514dc79a10a2c4bc6d19991c1716b2fca0dac908efafc852fd38390a42555aae`.

This is useful formal infrastructure, not a new law of physics. Its linear-
program geometry is standard, the supplied completion class is not proved
physically exhaustive, and exact response reconstruction cannot by itself
choose between record-first ontology and an operational duality.

## Frozen finite contract

Let:

- \(H\) be a nonempty finite history set;
- \(A\) be a nonempty finite intervention set;
- \(p_a(h)\in[0,1]\cap\mathbb Q\) be the probability of binary outcome one
  after intervention \(a\) in history \(h\);
- \(\mathcal C\) be a nonempty finite, target-independently frozen completion
  class;
- \(Q_c(z\mid h)\) be the exact rational certified-record kernel supplied by
  completion \(c\), over a finite record alphabet \(Z_c\); and
- \(\rho(c)\in\mathbb N^d\) be its declared resource vector, ordered
  componentwise rather than collapsed to a fitted scalar.

Every admitted completion is supplied as:

- independently formed;
- future-independent;
- target-independent; and
- boundary-preserving relative to the frozen observer/access frame.

Those are contract premises. The theorem validates their types but does not
derive their physical truth.

For each intervention \(a\), a stochastic record decoder is a vector
\(k_a:Z_c\to[0,1]\). It predicts

\[
\widehat p_{a,c}(h)
=
\sum_{z\in Z_c}Q_c(z\mid h)k_a(z).
\]

For binary outcomes, total variation is the absolute probability difference.
Define the completion deficiency

\[
d(c)
=
\max_{a\in A}
\min_{k_a\in[0,1]^{Z_c}}
\max_{h\in H}
\left|
p_a(h)-\widehat p_{a,c}(h)
\right|.
\tag{1}
\]

The candidate-class construction digest includes histories, interventions,
the explicitly frozen observer-boundary identity, record kernels, resource
vectors, access premises, and completion identity. It excludes the response
target. A target-mutation control confirms that changing every desired
response leaves this digest unchanged.

## The finite theorem

### Theorem — certified causal reconstruction trichotomy

For every valid frozen contract above:

1. each \(d(c)\) is attained and is an exact rational number;
2. if the base completion \(c_0\) has \(d(c_0)=0\), the contract returns
   `BASE_RECONSTRUCTION`;
3. otherwise, if some \(c\in\mathcal C\) has \(d(c)=0\), the contract returns
   `REFINED_RECONSTRUCTION` and the resource-Pareto-minimal exact
   completions; and
4. otherwise,
   \[
   \delta_{\mathcal C}
   =
   \min_{c\in\mathcal C}d(c)>0,
   \tag{2}
   \]
   and the contract returns `CLASS_RELATIVE_REMAINDER` with the exact margin
   and every margin-attaining completion.

These branches are mutually exclusive and exhaustive.

### Proof

For fixed \(a,c\), introduce a scalar \(\epsilon\) and solve

\[
\begin{aligned}
\text{minimize}\quad &\epsilon\\
\text{subject to}\quad
&-\epsilon
\leq
\sum_zQ_c(z\mid h)k_a(z)-p_a(h)
\leq\epsilon
\quad\text{for every }h,\\
&0\leq k_a(z)\leq1,\qquad 0\leq\epsilon\leq1.
\end{aligned}
\tag{3}
\]

This is a nonempty bounded rational polytope: a constant stochastic decoder
is feasible with \(\epsilon\leq1\). A linear objective attains its minimum at
a vertex, and every vertex solves a square subsystem of active rational
constraints. Therefore the minimum exists and is rational. Taking the
maximum over the finite intervention set preserves exact attainment and
rationality, proving part 1.

Exact reconstruction is equivalent to \(d(c)=0\). Testing the distinguished
base completion first and then the remaining finite class yields parts 2 and
3. If neither exact branch holds, every one of finitely many \(d(c)\) is
strictly positive; their minimum is therefore strictly positive, proving
part 4. The stated tests partition all valid contracts. \(\square\)

The probe enumerates every feasible vertex of (3) using exact fractions. Its
artifact preserves the optimal decoder, predictions, signed residuals,
active constraints, systems checked, and feasible-vertex count for every
intervention and completion. This is a machine-replayable finite
specialization of the proof, not a claim that vertex enumeration is the
efficient general algorithm.

## Controls and what they teach

| control | exact result | research lesson |
|---|---|---|
| base identity record | `BASE_RECONSTRUCTION` | A complete supplied record can factor every target response. |
| constant endpoint plus formed syndrome | `REFINED_RECONSTRUCTION` | An endpoint failure can be only omitted formed information. |
| finite coarse-region class | `CLASS_RELATIVE_REMAINDER`, \(\delta_{\mathcal C}=1/2\) | A finite positive margin is possible and exactly certifiable. |
| same target in a newly frozen expanded access frame | `REFINED_RECONSTRUCTION` | The prior remainder was class-relative and disappears when the charged boundary contract changes. |
| two incomparable exact repairs | both retained as Pareto-minimal | Bits, boundary access, and latency must not be hidden in one fitted cost. |
| unfrozen contract | `INCOMPLETE_CONTRACT` | Missing premises do not count as evidence for or against reconstruction. |

The boundary-expansion pair is the most important hostile control. The
expanded candidate is **not** smuggled into the original class: the probe
constructs a second contract whose expanded observer boundary is explicitly
frozen and whose resource vector charges that expansion. It proves why
equation (2) must never be reported as an irreducible physical remainder: the
conclusion quantifies over the original boundary and \(\mathcal C\), not over
every physically possible completion.

## What changed relative to the prior compiler

`HC-DU-036B` decided exact factorization and selected minimum supplied
refinements. It deliberately rejected nonzero tolerances because pairwise
epsilon-closeness does not define a transitive history quotient.

`HC-DU-036C` does **not** turn epsilon-closeness into a quotient. It instead
defines an optimization distance from the full response table to the convex
set of tables obtainable through a fixed stochastic record kernel. This
produces:

- an exact quantitative failure margin;
- a finite completion-class lower bound;
- a resource-partial-order repair surface; and
- a stable place to attach finite-shot confidence regions later.

The new result is therefore a better mathematical spine for the North Star,
but its next meaningful gain must come from an implementation-complete
physical contract rather than another synthetic fixture.

## Scientific interpretation

An exact base or refined reconstruction says that, for the declared
interventions and outcomes, no observer-accessible response distinction lies
outside the supplied record object. It does **not** say that records create
physical reality. The same operational result remains compatible with:

- a record-first account;
- a lossless physical/record dual description; or
- a physics-first ontology whose admitted operational projection happens to
  factor through the record.

A positive \(\delta_{\mathcal C}\) is stronger than a plotted discrepancy:
it says no stochastic decoder for any member of the frozen class can absorb
the gap. It still earns only a **class-relative candidate remainder** until
the physical warrant for \(\mathcal C\), the observer boundary, the
instrument, the calibration model, and the resource passport are defended.

## Stops and next gate

Do not claim:

- theorem novelty from finite linear programming;
- a physically exhaustive completion class;
- an ontology from operational factorization;
- a laboratory remainder from synthetic rational tables;
- an approximate record equivalence relation; or
- one scalar capability price from the componentwise resource order.

The next physical use should ingest one public evidence packet that passes
the four-table gate, freeze its record and completion class before
adjudication, replace exact probabilities with calibration-linked confidence
regions, and compute either:

1. a robust reconstruction bound;
2. a resource-Pareto-minimal physical refinement; or
3. a finite lower confidence bound on \(\delta_{\mathcal C}\).
