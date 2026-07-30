---
title: Non-Markovian collapse/Bohmian record duality and issuance first leak
date: 2026-07-29
claim_id: HC-DU-143
evidence_grade: 4
status: banked_scoped_result
programs:
  - CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR
  - CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
---

# Non-Markovian collapse/Bohmian record duality and issuance first leak

## Result

Tilloy and Wiseman give an exact construction in which a non-Markovian
stochastic collapse trajectory is the conditioned wavefunction of a
deterministic Bohmian system coupled to a hidden oscillator bath. The
collapse noise is a function of the bath's initial hidden configuration, its
law agrees with the collapse noise law, and the conditioned system
wavefunction agrees path by path. Their natural local beable is preserved as
well.

Dynamic Unity can therefore bank a precise downstream corollary:

> If two source descriptions are related by that pathwise
> measure-preserving correspondence, every unchanged passive record, archive,
> decoder, and target formed only from the matched path has the same law.
> Such a record cannot determine whether its apparent randomness was
> progressively introduced or disclosed from an enlarged initial
> completion.

This is a scoped operational-duality and formation-label nonfactorization
result. It is not proof that collapse and Bohmian ontologies are identical,
that objective collapse is false, that determinism is true, or that issuance
never occurs. The source theorem fixes one uncontrolled process. Equality
under active source interventions would require a correspondence natural
across the entire intervention family; that stronger object is not supplied.

## Claim and grade

`HC-DU-143` earns **scoped Grade 4** for:

1. exact preservation of passive downstream record laws under the published
   non-Markovian collapse/Bohmian correspondence;
2. exact nonfactorization of the labels “progressive stochastic formation”
   and “initial-condition disclosure” through those records;
3. separation of fixed-process path equivalence from intervention-natural
   process equivalence; and
4. a finite first-leak classification.

It earns no universal ontology theorem, no generic objective-collapse
equivalence, no Markovian-collapse no-go, no new dynamics, no empirical
excess, and no new physics. The source mathematics is known. DU's increment
is the typed record/capability consequence and the exact boundary on what
would have to differ next.

## Source-owned correspondence

The primary source is:

- Antoine Tilloy and Howard M. Wiseman, “Non-Markovian wave-function collapse
  models are Bohmian-like theories in disguise,” *Quantum* **5**, 594 (2021),
  [arXiv:2105.06115](https://arxiv.org/abs/2105.06115).

For a broad class of non-Markovian stochastic Schrödinger equations, the
source constructs:

- a system coupled linearly to a bath of harmonic oscillators;
- an initial quantum state for the bath;
- Bohmian hidden bath coordinates \(x(0)\);
- a deterministic joint Schrödinger evolution and Bohmian bath trajectory
  \(x(t)\); and
- a noise history \(w^{[t]}\) obtained as a linear functional of the bath
  coordinates.

The pushforward of the equilibrium distribution of \(x(0)\) is the Gaussian
noise law required by the collapse model. Most importantly, their equation
(60) identifies the normalized Bohmian conditional wavefunction with the
nonlinear collapse-model trajectory:

\[
\psi_{x(t)}(t)
\;=\;
\frac{\langle x(t)\mid\Psi(t)\rangle}
     {\|\langle x(t)\mid\Psi(t)\rangle\|}
\;=\;
\psi_{w^{[t]}}(t).
\]

The construction also maps a natural local beable. Thus it is stronger than
equality of an unconditional density operator: the conditioned path that
could drive a downstream record agrees realization by realization under the
map.

The source's own dictionary makes the interpretive collision explicit:
continuous stochastic information introduced during collapse evolution is
represented on the Bohmian side by deterministic evolution with uncertainty
in the bath's initial hidden variables. The source describes these as
empirically indistinguishable within the matched non-Markovian domain.

As a positive control that this relationship is not unique to one formal
construction, Toroš, Donadi, and Bassi derive GRW-like conditional collapse
from Bohmian collisional dynamics in an appropriate environment and
approximation:

- Marko Toroš, Sandro Donadi, and Angelo Bassi, “Bohmian Mechanics, Collapse
  Models and the emergence of Classicality,”
  [arXiv:1603.02541](https://arxiv.org/abs/1603.02541).

That second result is approximate and assumption-dependent. It supports the
general relevance of source-completion duality but does not enlarge the exact
claim.

## DU record-preservation theorem

Let \((\Omega_B,\mu_B)\) be the space of Bohmian bath initial conditions and
\((\Omega_C,\mu_C)\) the collapse-noise path space. Let

\[
F:\Omega_B\longrightarrow\Omega_C,
\qquad
F_*\mu_B=\mu_C.
\]

Let \(Z_B\) and \(Z_C\) denote the declared matched path object: the
conditioned system wavefunction together with the source-preserved local
beable. Suppose

\[
Z_B = Z_C\circ F
\quad \mu_B\text{-almost surely}.
\]

For any unchanged passive Markov kernel \(K(dr\mid z)\) from the matched path
to an operational record or archive, and any measurable record event \(A\),

\[
\begin{aligned}
\Pr_B(R\in A)
&=\int_{\Omega_B}K(A\mid Z_B(x))\,d\mu_B(x)\\
&=\int_{\Omega_B}K(A\mid Z_C(F(x)))\,d\mu_B(x)\\
&=\int_{\Omega_C}K(A\mid Z_C(w))\,d\mu_C(w)\\
&=\Pr_C(R\in A).
\end{aligned}
\]

The same composition proves equality for any passive archive, decoder, loss,
or target kernel downstream of \(R\). If an operational capability is fully
defined by such a record-mediated decision problem, its attainable response
law and risk are equal as well.

This is ordinary measurable pushforward mathematics. It is exact, but the
component theorem is absorbed by probability theory, open-system dilation,
and the Tilloy--Wiseman construction.

## Why active capabilities are a different claim

An active intervention can change the source dynamics that generated the
matched path. To claim that the two theories have the same active capability
profile over an intervention class \(\mathcal U\), one needs more than one map
for the uncontrolled process. One needs a family

\[
\{F_u:\Omega_{B,u}\to\Omega_{C,u}\}_{u\in\mathcal U}
\]

that:

1. preserves the relevant path law for every admitted intervention \(u\);
2. uses one antecedently fixed intervention translation rather than refitting
   after the outcome is known;
3. composes coherently under sequential and adaptive interventions; and
4. preserves the same resource, access, archive, and readout contract.

That is an intervention-natural or process-level correspondence. The
published fixed-process theorem does not by itself establish it.

This correction matters. “Every downstream passive record agrees” is proved.
“Every operation any observer could ever perform agrees” is not.

## Issuance/disclosure consequence

Define a formation label \(L\) with two values:

- \(L=\mathrm{progressive}\): the stochastic increment is introduced as the
  collapse process runs; and
- \(L=\mathrm{initial}\): the matched history is determined by an enlarged
  initial bath completion and disclosed through deterministic evolution.

The source correspondence gives pairs with the same \(Z\), and therefore the
same passive record \(R=K(Z)\), but different \(L\). Hence no function
\(\ell\) can satisfy

\[
L=\ell(R)
\]

throughout the paired theory class. The formed record does not identify its
formation label.

This is not an argument that the labels are meaningless. They refer to
different global completions. It is an exact statement that the distinction
is absent from the specified record quotient.

For DU's completed forecasting/issuance branch, this clears the
source-completion reopener and returns a negative but useful theorem:
apparently progressive stochastic forecasting is compatible with
initial-condition disclosure after physically enlarging the completion.
Issuance evidence must therefore resist this completion, not merely exhibit a
single stochastic outcome, non-Markovian memory, or an unpredictable local
trajectory.

## What “the same apparatus” means here

The comparison holds fixed:

- the operational system;
- its conditioned wavefunction path;
- the declared local beable;
- every passive downstream record/archive map;
- observer access to that record; and
- every downstream task that factors through it.

It does **not** make the global descriptions literally identical. The
Bohmian construction includes a bath, a global joint wavefunction, and hidden
bath coordinates. The collapse presentation treats the corresponding
colored noise as stochastic. Moving between them is an enlarged-completion
representation, not proof that their unobserved global ontology is one
object.

This is exactly the boundary DU needs: operational equality can be genuine
while completion identity fails.

## First-leak audit

| Candidate discriminator | Current verdict | Why |
|---|---|---|
| Conditioned wavefunction or matched local beable | Closed | Preserved pathwise by the source map. |
| Passive pointer, archive, transcript, decoder, or record-mediated task | Closed | Equal by unchanged-kernel pushforward. |
| A different passive detector placed on the same preserved path | Closed | Changing \(K\) in the same way on both sides preserves equality. |
| Adaptive source intervention | Open | Requires one coherent correspondence across the intervention family. |
| Direct bath-coordinate or global-wavefunction access | Completion-facing | It can separate descriptions only by admitting variables outside the matched local record contract. |
| Symmetry, covariance, or relativistic implementation | Open physical seam | A representation may require structure or break a symmetry not shared by its rival. |
| Finite resource, thermodynamic, or controller cost | Open physical seam | The source correspondence does not prove a matched implementation cost. |
| Markovian white-noise limit | Singular/resource seam | The source says the mapping persists formally, while the Bohmian realization requires a continuously infinite bath; this is not a record-only discriminator. |
| Ontology-specific counterfactual | Open only if operationalized | A verbal difference is not excess; a frozen physical intervention and response must be supplied. |

The highest-information next question is therefore:

> Does the Tilloy--Wiseman correspondence extend naturally across one
> nontrivial, physically frozen intervention family with matched resources
> and archives?

A positive result would strengthen the operational duality from passive paths
to an active process class. A smallest counterexample would locate genuine
excess and identify the first observer-accessible physical remainder. Either
return teaches more than another survey of pointer models.

## Absorbers and controls

### Strongest absorbers

- non-Markovian stochastic Schrödinger equations;
- Bohmian conditional wavefunctions;
- oscillator-bath dilation and open-system theory;
- measurable pushforward and Blackwell-style downstream equivalence; and
- collisional derivations of effective collapse.

### Cheapest kills

1. A proposed passive record discriminator that depends only on the matched
   path is killed by the pushforward proof.
2. A proposed ontology discriminator that directly reads an added bath
   variable changes the access/completion contract.
3. A claim of full active equivalence without an intervention-natural family
   overclaims the source theorem.
4. A claim that the Markovian limit is unmappable contradicts the source; the
   honest issue is its singular continuously infinite realization.

### What would reopen the result

- an exact intervention for which no no-refit correspondence preserves the
  local response;
- a regulator-robust symmetry or covariance difference that reaches an
  observer record;
- an implementation-cost separation under one frozen resource contract; or
- a source-selected archive/access interface whose statistics do not factor
  through the matched path.

## Plain English

One theory says randomness is being created as collapse happens. Another says
the same apparent randomness was already encoded in hidden starting
conditions of a larger system. For an important non-Markovian class, the two
stories can produce exactly the same evolving local quantum state and the
same local physical trace, run by run.

So if we attach the same passive detector and archive to that local history,
the records cannot tell us which story generated them. This directly warns
DU that “one actual random-looking record appeared” is not evidence for
issuance rather than disclosure.

The wall is not total. We have not shown that the two descriptions stay
equivalent when an observer actively changes the source, accesses the hidden
bath, demands relativistic symmetry, or accounts for the complete physical
cost. Those are now the exact places to look.

## Disposition

`SCOPED_RECORD_DUALITY_AND_FORMATION_LABEL_NONFACTORIZATION`.

No successor is activated. `CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR`
remains parked, and the predictive-issuance program remains complete. Reopen
only on an intervention-natural comparison or one completion-facing
difference converted into an unchanged observer-accessible response.
