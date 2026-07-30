---
title: "QND tomography operational closure, label sufficiency, and material-dilation boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-164
run_id: RUN-20260730-175003-qnd-tomography-reopener-audit
work_id: MPA-REOPENER-QND-TOMOGRAPHY-AUDIT
action_id: MPA-REOPENER-QND-TOMOGRAPHY-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# QND tomography operational closure and material-dilation boundary

## Executive return

```text
PROCESS_TOMOGRAPHY_REOPENER_PARTIALLY_SATISFIED
+ OUTCOME_CONDITIONED_INSTRUMENT_RECONSTRUCTION
+ LABEL_SUFFICIENCY_CRITERION
+ MATERIAL_ARCHIVE_NONSELECTION
+ DILATION_TWIN_NO_GO
+ AGGREGATED_COUNTS_ONLY
+ RANK_ONE_NULL_UNADJUDICATED
+ KNOWN_RESULT_ABSORPTION
+ NO_READY_SUCCESSOR
```

The strongest QND-tomography source closes more of the `HC-DU-163`
reopener than an ordinary repeat-agreement experiment.

[Pereira, García-Ripoll, and Ramos](https://arxiv.org/abs/2109.06616)
apply two detector uses, vary a complete set of input preparations and
intermediate operations, and reconstruct the outcome-conditioned quantum
maps \(\{\mathcal E_n\}\). Their later
[seven-qubit IBM experiment](https://www.nature.com/articles/s41534-023-00688-7)
uses 18 QND-tomography circuits plus gate-set tomography, \(2^{13}\) shots
per circuit, and constrained maximum likelihood to reconstruct the process
matrices. The source reports that its fitted model agrees with the
experimental data under its declared 95-percent chi-square criterion.

That is a real positive:

> The source identifies the fitted reduced quantum instrument, not merely a
> one-step repeat rate.

It does not identify the complete material record or the physical
implementation of that instrument. The
[pinned public packet](https://doi.org/10.5281/zenodo.7341393) contains
aggregate measurement-level-2 count histograms. Those histograms preserve
the joint categorical outcomes needed for \(p(m,n\mid i,j)\), but not shot
order, raw/IQ traces, rejected attempts, controller lineage, or complete
archive/reset semantics.

The deeper boundary is exact and survives even perfect instrument
tomography:

> Two physical measurement dilations can induce the same accessible
> outcome-conditioned instrument for every system input and every later
> system-plus-outcome action while retaining different hidden archive
> support.

Thus process tomography satisfies the **operational-process** part of the
reopener. It does not satisfy the **material archive, provenance, and
implementation** part. Swing 6 remains ineligible.

## 1. What the source reconstructs

For outcome \(n\), a quantum instrument supplies a completely positive,
trace-nonincreasing map

\[
\mathcal E_n:\mathcal B(\mathcal H)\longrightarrow
\mathcal B(\mathcal H),
\qquad
\sum_n\mathcal E_n
\text{ trace preserving}.
\tag{1}
\]

The outcome probability and normalized posterior state are

\[
p(n\mid\rho)=\operatorname{tr}\mathcal E_n(\rho),
\qquad
\rho_n(\rho)=
\frac{\mathcal E_n(\rho)}
{\operatorname{tr}\mathcal E_n(\rho)}.
\tag{2}
\]

The source represents \(\mathcal E_n\) by matrices
\(\Upsilon_n\) satisfying

\[
\langle ij|\Upsilon_n|kl\rangle
=
\langle i|\mathcal E_n(|k\rangle\langle l|)|j\rangle.
\tag{3}
\]

Equation (3) is a Liouville/process representation: it gives the map's
values on a matrix-unit basis. With informationally complete prepared states,
intermediate operations, and terminal effects, its entries determine every
later system-only statistic inside the admitted finite-dimensional model.

This earns:

```text
source-pinned interventions
  -> joined first/second categorical outcomes
  -> fitted outcome-conditioned reduced process
```

It does not earn:

```text
fitted reduced process
  -/-> unique detector microhistory
  -/-> unique environment/dilation
  -/-> complete retained archive
  -/-> provenance or reset semantics
```

The word “complete” in the 2022 paper is therefore scoped to characterization
of the detector's declared reduced quantum instrument and its derived
quantifiers. It cannot be imported as material completeness in Dynamic
Unity's stronger sense.

## 2. Outcome-label sufficiency theorem

QND tomography gives a cheap exact test for one narrower question:

> After outcome \(n\), does the outcome label alone determine every later
> system-only response, regardless of the admitted input history?

Let

\[
F_n=\mathcal E_n^\dagger(I)
\tag{4}
\]

be the POVM effect for outcome \(n\).

### Proposition 1 — label sufficiency is measure-and-prepare form

For a nonzero finite-dimensional outcome map \(\mathcal E_n\), the following
are equivalent:

1. for every input state \(\rho\) with \(p(n\mid\rho)>0\), the normalized
   posterior \(\rho_n(\rho)\) is one fixed state \(\tau_n\);
2. every later system-only operation and effect has a probability determined
   by \(n\), with no remaining dependence on the prior input;
3. the outcome map has the form

   \[
   \mathcal E_n(\rho)
   =
   \operatorname{tr}(F_n\rho)\tau_n;
   \tag{5}
   \]

4. the Liouville/process matrix in equation (3) has ordinary matrix rank one.

### Proof

Condition 1 makes every positive input map to the same positive ray generated
by \(\tau_n\). The scale is its trace, which by equation (4) is
\(\operatorname{tr}(F_n\rho)\), giving equation (5). Linearity extends the
identity from states to the full operator space.

Equation (5) has Liouville form

\[
\operatorname{vec}(\mathcal E_n(X))
=
\operatorname{vec}(\tau_n)
\operatorname{vec}(F_n)^\dagger
\operatorname{vec}(X),
\tag{6}
\]

so its nonzero process matrix has rank one. Conversely a completely positive
outcome map with one-dimensional range sends positive inputs to one positive
ray and therefore has form (5). Conditions 1 and 2 are equivalent because
quantum effects separate density operators.

This is standard quantum-instrument and sufficient-statistic mathematics. It
is useful here because it turns an imprecise “the record seems QND” claim into
a typed falsifiable question.

### Controls

- An ideal rank-one projective measurement has
  \(\mathcal E_n(\rho)=\langle n|\rho|n\rangle|n\rangle\langle n|\);
  each outcome process has rank one. The label is operationally sufficient.
- An independent coin label with
  \(\mathcal E_n(\rho)=\rho/2\) has process rank four for a qubit. After the
  same label, a later \(Z\) measurement distinguishes prior inputs
  \(|0\rangle\) and \(|1\rangle\). The label is not sufficient.

The public IBM packet contains seven stored `data_tomo_v2` estimates, each
covering seven qubits and two outcomes. All 98 stored \(4\times4\) process
matrices have numerical rank four at tolerance \(10^{-10}\). Their relative
Frobenius distance to the best rank-one approximation ranges from
\(0.00253\) to \(0.03432\), with median \(0.01395\).

That is a diagnostic, not an exact verdict. Constrained finite-sample
maximum-likelihood estimates can be numerically full rank even when a lower
rank model is statistically adequate. The source reports a goodness-of-fit
test for the general process model, not a likelihood-ratio or bootstrap test
of the rank-one/replacer submodel. Therefore this audit returns:

```text
RANK_ONE_NULL_UNADJUDICATED
```

A future local analysis could fit equation (5) directly to the published
aggregate counts and compare it to the unrestricted instrument model. That
would decide operational label sufficiency for the fitted reduced system; it
would still not select the material archive.

## 3. Instrument–archive nonselection theorem

Let \(S\) be the measured qubit, \(C\) the accessible classical outcome,
\(E\) an environment that decoheres the outcome, and \(R\) a candidate hidden
archive register.

Define two isometries on the computational basis:

\[
\begin{aligned}
V_{\mathrm{blank}}|0\rangle
&=|0_S0_C0_E0_R\rangle,\\
V_{\mathrm{blank}}|1\rangle
&=|1_S1_C1_E0_R\rangle,
\end{aligned}
\tag{7}
\]

and

\[
\begin{aligned}
V_{\mathrm{copy}}|0\rangle
&=|0_S0_C0_E0_R\rangle,\\
V_{\mathrm{copy}}|1\rangle
&=|1_S1_C1_E1_R\rangle.
\end{aligned}
\tag{8}
\]

### Proposition 2 — a complete accessible instrument does not select its
material archive

After tracing \(E\) and \(R\), equations (7) and (8) induce the same channel
on \(S\otimes C\):

\[
\rho
\longmapsto
\rho_{00}|00\rangle\langle00|
+
\rho_{11}|11\rangle\langle11|.
\tag{9}
\]

They therefore agree under every possible input and every later action on
the accessible system and outcome. Yet for input \(|1\rangle\), \(R\) is
blank in equation (7) and contains a copied outcome in equation (8).
Accessing \(R\) distinguishes them.

### Proof

It is enough to evaluate both dilations on the four input matrix units.
Diagonal units give the same accessible diagonal terms. Off-diagonal units
vanish after tracing \(E\), because the two basis branches have orthogonal
environment states in both constructions. The reduced channels are equal on
a basis and hence equal on every operator. The final \(R\) values differ
directly on the \(|1\rangle\) branch.

The same construction can vary hidden provenance, redundant copies, or
retention policy while preserving the accessible instrument. This is the
ordinary nonuniqueness of measurement/Stinespring dilations, applied to
Dynamic Unity's archive question.

The important conjunction is:

```text
perfect operational label sufficiency
+ complete accessible instrument tomography
does not imply
unique material archive or implementation
```

## 4. Pinned public-packet audit

The source makes its code and data public. The exact audit pinned:

- Zenodo DOI `10.5281/zenodo.7341393`, version `0.1`;
- archive MD5 `0e317d063561231842a9039306e45f94`; and
- Git commit `5c4b8e51767571602de4d2409836f3a37ca25292`.

Excluding Git metadata, the repository contains 2,519 files and
449,944,671 bytes. Its 122 Qiskit result JSON files contain 61,336
experiment-result entries:

- 60,926 entries report 8,192 shots;
- 410 entries report 1,000 shots;
- every entry is measurement level 2;
- every entry contains aggregate counts;
- no entry contains non-null ordered shot memory; and
- no entry contains non-null raw/IQ-like data.

The reconstruction code obtains `Result.get_counts` and converts those
histograms into probabilities. The count keys retain the first/second
categorical result within a circuit, which is exactly what process tomography
needs. They do not retain a joined acquisition lineage at Dynamic Unity's
material packet level.

These are claims about the public packet, not claims that IBM never held
lower-level acquisition state.

The machine-readable audit is
[`source-audit.json`](../lab/process/runs/RUN-20260730-175003-qnd-tomography-reopener-audit/source-audit.json).

## 5. Reopener disposition

`HC-DU-163` required:

1. joined per-attempt records and later responses;
2. a predeclared intervention/tomography family determining the
   postmeasurement process;
3. explicit retention, provenance, access, and reset semantics; and
4. factorization plus minimality for the retained archive.

The new audit returns:

| Reopener term | Result |
|---|---|
| Joined categorical responses | **Partial:** joined within aggregate count keys; individual shot order and acquisition lineage absent |
| Process-determining intervention family | **Satisfied at fitted reduced-instrument level** |
| Operational label-factorization test | **Available:** rank-one/replacer criterion; public rank-one null not adjudicated |
| Material record factorization | **Not satisfied:** complete physical history and archive are not observed |
| Behavioral minimality | **Not satisfied:** material quotient remains unidentified |
| Provenance/retention/reset/access | **Not satisfied by the public packet** |
| Unique physical implementation | **Impossible from the accessible instrument alone:** exact dilation twins |

Therefore:

```text
process rung reopened and closed positively
material-archive rung remains open
Swing 6 not activated
```

## 6. What changed

The reopener is now narrower and better:

> Do not ask merely for “more tomography.” Standard QND measurement
> tomography can already reconstruct the fitted reduced instrument. Ask for
> a source-pinned implementation-complete acquisition packet—or a physical
> selection theorem that makes the relevant archive/dilation invariant
> across all admissible implementations.

This avoids circling process reconstruction after the literature has already
solved it. It also prevents a complete operational model from being silently
promoted into a complete material history.

## Grade and scope

**Grade 4, scoped.** The exact rank criterion and dilation twins are rigorous.
The source and public-packet audit are pinned and reproducible. The general
mathematics is absorbed by quantum instruments, measure-and-prepare channels,
process tomography, Stinespring dilation, and sufficient-statistic theory.

No claim is made that:

- the IBM apparatus contains either toy dilation;
- the stored estimates prove exact process rank;
- all physical implementations are observationally indistinguishable under
  every enlarged action class;
- a material archive does not exist;
- Dynamic Unity has reconstructed a physical remainder; or
- any new physical law or prediction has been found.

## Exact local control

Run:

```bash
python3 tests/du_qnd_tomography_material_archive_probe.py --write-artifact
```

The probe verifies exact Liouville ranks for the ideal and coin instruments,
channel equality of the two dilations on a complete matrix-unit basis,
hidden-archive difference, and strict distinction after extending access to
\(R\).
