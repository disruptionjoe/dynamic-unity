---
title: "Completion-common record quotient and two-tier capability leak"
status: completed_scoped_common_quotient_reconstruction_and_history_counterexample
doc_type: finite_common_quotient_theorem_matched_completion_transfer_and_capability_filtration
created: 2026-07-27
hypothesis_id: HC-DU-045
campaign_id: ECR-N5
swing_id: ECR-N5-S4
run_id: RUN-20260727-dynamic-unity-completion-invariant-transfer
authority: "Joe direct chat: Go"
claim_grade: "SCOPED GRADE-4 FINITE COMMON-QUOTIENT NECESSITY CLASSIFICATION PLUS GRADE-3 COMPLETION-INVARIANT REDUCED-MATTER RECONSTRUCTION AND EXACT HISTORY-TRANSFER COUNTEREXAMPLE / KNOWN PARTITION-LATTICE, FACTORIZATION, MARKOV SUFFICIENCY, BLACKWELL SUFFICIENCY, DILATION, COMPLEMENTARY-CHANNEL, PROCESS-TENSOR, AND OBSERVER-ACCESS COMPONENTS / NO ENDOGENOUS ARCHIVE, MICROSCOPIC COMPLETION SELECTION, UNIVERSAL NO-GO, ONTOLOGY, NEW PHYSICS, PREDICTION, PAPER, HARDWARE, OR PROVIDER RESULT"
run_plan: "../runs/2026-07-27-completion-invariant-transfer.md"
probe: "../tests/du_completion_invariant_transfer_probe.py"
artifact: "../tests/artifacts/du_completion_invariant_transfer_result.json"
---

# Completion-common record quotient and two-tier capability leak

## Executive verdict

The matched-completion test returns a real positive and a decisive adverse
result:

```text
FINEST COMPLETION-COMMON OBSERVER RECORD = TERMINAL MATTER STATE
REDUCED-MATTER FUTURE TRANSFERS WITHOUT REFIT
WRITE-OCCURRENCE HISTORY DOES NOT TRANSFER
CROSS-COMPLETION FIRST LEAK = OCCURRENCE
VISIBLE-BINARY FIRST LEAK = COUNT
```

The positive result is exact. Across the visible-archive and
hidden-reservoir completions inherited from `HC-DU-044`, the terminal matter
state is a strict quotient of the full history and is sufficient for the
complete next-step reduced-matter branch law.

That is ordinary Markov operational closure. It is not reconstruction of
the past and it does not credit the epoch archive.

The minimum historical target already fails. The stale history and the
four-edge return history

\[
\varnothing
\qquad\text{and}\qquad
CWCW
\]

start in \(x_1\), end in \(x_1\), and have the same
completion-common record, but only the second contains a selected write.
Thus no decoder of the completion-common record can answer:

> Did a write occur since the certified epoch reset?

Inside the visible completion, the binary epoch record does answer that
question exactly. It first fails when the capability expands to write count:

\[
CWCW
\qquad\text{and}\qquad
CWCWCWCW
\]

have the same terminal state and occurrence flag but have two and four
writes.

If the observer boundary is enlarged to include both the admitted archive
\(A\) and hidden reservoir \(H\), both completions expose the full history
and all preregistered targets become reconstructible. But that repair:

- changes the observer boundary;
- adds an access route and resources; and
- makes the record injective on the finite history class.

It is completion tomography under a stronger contract, not repair of the
old \(A\)-only record and not endogenous strict compression.

The host therefore exhibits a scoped three-way boundary:

| property pair | what the host supplies |
|---|---|
| completion-invariant + strictly compressive | terminal matter state, sufficient only for reduced future behavior |
| history-sufficient + strictly compressive | visible binary epoch record, but only in the supplied archive completion |
| completion-invariant + history-complete | full \(A+H\) access, but injective and resource-expanded |

No one record in the frozen comparison has all three properties.

The dispositions are:

```text
MARKOV_OPERATIONAL_CLOSURE
COMPLETION_AND_ACCESS_RELATIVE HISTORY SUFFICIENCY
NO_ENDOGENOUS_ARCHIVE FOR THIS HOST
H-CCR-17 REMAINS OPEN
```

## 1. What Swing 4 had to distinguish

`HC-DU-044` established five facts:

1. the bounded “write since epoch” statistic has a unique minimum binary
   transducer;
2. exact repeated set/reset cannot run reversibly on one closed carrier;
3. fresh or exported support can retain the required physical history;
4. the binary occurrence quotient is strict and autonomous for one bounded
   occurrence capability; and
5. the reduced matter host does not select whether the history token enters
   an admitted archive or a hidden reservoir.

That left an ambiguity. Perhaps the archive itself was completion-relative,
but some useful reconstruction theorem still survived every admissible
completion. Or perhaps every apparent success depended on choosing the
history-retaining arm.

This swing therefore froze four different targets:

\[
T_{\mathrm{next}},
\quad
T_{\mathrm{occ}},
\quad
T_{\mathrm{count}},
\quad
T_{\mathrm{word}}.
\]

They mean:

| target | meaning |
|---|---|
| \(T_{\mathrm{next}}\) | complete next-step reduced-matter branch law from the terminal state |
| \(T_{\mathrm{occ}}\) | whether at least one selected write occurred since epoch reset |
| \(T_{\mathrm{count}}\) | the number of selected writes in the horizon |
| \(T_{\mathrm{word}}\) | the complete resolved event word |

The targets were frozen before computing the common record. In particular,
the record was not defined as “whatever answers \(T_{\mathrm{occ}}\).”

## 2. The finite completion-common quotient theorem

Let one frozen lawful realization class be \(\Omega\). Suppose a family of
physically admitted completions or access architectures supplies native
records:

\[
r_i:\Omega\to R_i.
\]

Write:

\[
K_i=\ker r_i.
\]

A statistic

\[
q:\Omega\to Q
\]

is a **common quotient** of the native records when there are maps
\(p_i:R_i\to Q\) such that:

\[
q=p_i\circ r_i
\qquad\text{for every }i.
\]

Equivalently:

\[
K_i\subseteq\ker q
\qquad\text{for every }i.
\]

Let:

\[
K_\ast=\bigvee_i K_i
\]

be the join in the lattice of equivalence relations: the least equivalence
relation containing every \(K_i\).

### Theorem — completion-common quotient

The quotient:

\[
q_\ast:\Omega\to\Omega/K_\ast
\]

is the unique finest common quotient, up to lossless relabeling.

A target:

\[
t:\Omega\to T
\]

factors through every native record exactly when:

\[
K_\ast\subseteq\ker t.
\]

Equivalently, there is one decoder \(d\) on the common quotient such that:

\[
t=d\circ q_\ast,
\]

and every native-record decoder is the same \(d\) after the fixed
preprocessing map \(p_i\).

### Proof

If \(q\) factors through every \(r_i\), then every \(K_i\) is contained in
\(\ker q\). Since \(\ker q\) is itself an equivalence relation, it contains
their join \(K_\ast\). Therefore every common quotient factors through
\(q_\ast\), so \(q_\ast\) is finest and unique up to relabeling.

A target factors through every \(r_i\) iff:

\[
K_i\subseteq\ker t
\qquad\text{for every }i.
\]

Because \(\ker t\) is an equivalence relation, this is equivalent to:

\[
\bigvee_i K_i\subseteq\ker t.
\]

That is exactly the condition that \(t\) factor through \(q_\ast\).
\(\square\)

This is standard finite quotient/factorization mathematics. The Dynamic
Unity contribution is the typed use of the theorem: it prevents a target
that succeeds in one supplied completion from being called
completion-invariant.

## 3. Frozen matched completions

The matter host remains:

\[
x_0\xrightarrow{\alpha}x_1
\xrightarrow{\kappa}x_2
\xrightarrow{\alpha}x_3
\xrightarrow{\kappa}x_0,
\qquad
\alpha>\kappa>0.
\]

The selected fast write orbit is:

\[
W=\{x_0\to x_1,\;x_2\to x_3\}.
\]

The selected slow turnover orbit is:

\[
C=\{x_1\to x_2,\;x_3\to x_0\}.
\]

Use the nine resolved prefixes from \(x_1\):

\[
\varnothing,\;
C,\;
CW,\;
CWC,\;
CWCW,\;
\ldots,\;
CWCWCWCW.
\]

The two complete arms retain the same resolved history token in different
physical places:

\[
V_{\mathrm{visible}}(\omega)
=
\bigl(X_T(\omega),A:\omega,H:\mathrm{blank}\bigr),
\]

\[
V_{\mathrm{hidden}}(\omega)
=
\bigl(X_T(\omega),A:\mathrm{blank},H:\omega\bigr).
\]

Both complete maps are injective. Both reduce to the same matter endpoint
and the same one-step matter branch relation.

The observer boundary is frozen as:

```text
accessible: terminal matter + archive fragment A
excluded: reservoir H
```

This makes the two completions physically different at the declared
observer interface. Swapping the names \(A\) and \(H\) is not an admitted
gauge transformation because it changes the physical access wiring.

The native records are:

\[
r_V(\omega)
=
\bigl(X_T(\omega),A:\omega\bigr),
\]

\[
r_H(\omega)
=
\bigl(X_T(\omega),A:\mathrm{blank}\bigr).
\]

## 4. Exact common record

The visible record distinguishes every history in the finite class:

\[
\ker r_V=\Delta_\Omega.
\]

The hidden record distinguishes only terminal matter states:

\[
\ker r_H=\ker X_T.
\]

Therefore:

\[
\ker r_V\vee\ker r_H
=
\ker X_T.
\]

The finest completion-common observer record is:

\[
q_\ast=X_T.
\]

The exhaustive certificate enumerates all:

\[
B_9=21147
\]

partitions of the nine-history class. Exactly 15 are common quotients of the
two native records. There is exactly one finest candidate, and it is the
four-block terminal-state partition:

\[
\begin{aligned}
x_1 &: \{\varnothing,CWCW,CWCWCWCW\},\\
x_2 &: \{C,CWCWC\},\\
x_3 &: \{CW,CWCWCW\},\\
x_0 &: \{CWC,CWCWCWC\}.
\end{aligned}
\]

Replacing every visible history word by an arbitrary opaque token leaves
the partition and the common quotient unchanged. The result depends on
which distinctions are retained, not how they are named.

## 5. The exact positive: reduced-matter future

The target \(T_{\mathrm{next}}\) is the complete next-step reduced branch
profile:

\[
T_{\mathrm{next}}(\omega)
=
\bigl(
X_T(\omega),
n(X_T(\omega)),
\lambda(X_T(\omega))
\bigr),
\]

where \(n\) is the next state and \(\lambda\) is \(\alpha\) or \(\kappa\).

It depends only on \(X_T\). Therefore:

\[
\ker q_\ast
\subseteq
\ker T_{\mathrm{next}}.
\]

One no-refit decoder works in both completion arms.

The record is strictly compressive on histories. For example:

\[
q_\ast(\varnothing)
=
q_\ast(CWCW)
=x_1.
\]

Yet the same next reduced-matter law follows from both.

### What this earns

It earns:

```text
COMPLETION-INVARIANT STRICT-COMPRESSION RECONSTRUCTION
OF THE NEXT REDUCED-MATTER LAW
```

### What this does not earn

The result is already explained by the Markov state property. The terminal
matter state is a sufficient state for the future reduced process.

It does not show:

- that an epoch archive formed;
- that the past was reconstructed;
- that the environment selected a record;
- that microscopic matter is ontologically a record;
- that the completion was identified; or
- that a new physical law has been found.

Complete public behavior reconstructed from the present reduced state is
operational closure, not source or history derivation.

## 6. The minimum adverse history witness

Consider:

\[
\omega_0=\varnothing
\qquad\text{and}\qquad
\omega_1=CWCW.
\]

Both begin and end in \(x_1\):

\[
q_\ast(\omega_0)
=
q_\ast(\omega_1)
=x_1.
\]

But:

\[
T_{\mathrm{occ}}(\omega_0)=0,
\qquad
T_{\mathrm{occ}}(\omega_1)=1.
\]

Thus:

\[
\ker q_\ast
\not\subseteq
\ker T_{\mathrm{occ}}.
\]

No completion-common decoder exists for write occurrence.

The same pair separates write count and the full event word:

\[
T_{\mathrm{count}}(\omega_0)=0,
\qquad
T_{\mathrm{count}}(\omega_1)=2,
\]

\[
T_{\mathrm{word}}(\omega_0)=\varnothing,
\qquad
T_{\mathrm{word}}(\omega_1)=CWCW.
\]

This is the smallest exact adverse result required by Swing 4:

```text
SAME COMPLETION-COMMON RECORD
DIFFERENT HISTORICAL TARGET
```

It is a candidate-record insufficiency result. It does not establish an
ontological remainder because the hidden reservoir contains the omitted
history in the complete physical state.

## 7. Two different first capability leaks

Use the nested capability classes:

\[
H_{\mathrm{matter}}
\subset
H_{\mathrm{occ}}
\subset
H_{\mathrm{count}}
\subset
H_{\mathrm{output}}.
\]

They allow:

| capability | additional action or query |
|---|---|
| \(H_{\mathrm{matter}}\) | predict or control the next reduced matter step |
| \(H_{\mathrm{occ}}\) | also query write occurrence since epoch |
| \(H_{\mathrm{count}}\) | also query the number of writes |
| \(H_{\mathrm{output}}\) | also distinguish the complete resolved output word |

### Across completions

The completion-common record \(X_T\) is sufficient for:

\[
H_{\mathrm{matter}}.
\]

It first fails at:

\[
H_{\mathrm{occ}}.
\]

Therefore:

```text
CROSS-COMPLETION FIRST LEAK = HISTORICAL OCCURRENCE
```

### Inside the visible completion

The visible binary epoch record:

\[
r_{\mathrm{epoch}}
=
\bigl(X_T,b_{\mathrm{occ}}\bigr)
\]

is sufficient for:

\[
H_{\mathrm{occ}}.
\]

It first fails at:

\[
H_{\mathrm{count}}.
\]

The exact witness is:

\[
CWCW
\qquad\text{versus}\qquad
CWCWCWCW.
\]

They have the same endpoint and occurrence bit, but:

\[
2\ne4
\]

writes.

Therefore:

```text
VISIBLE-BINARY FIRST LEAK = WRITE COUNT
```

These are not contradictory verdicts. They refer to two different
boundaries:

1. whether the archive exists at the observer interface across admissible
   completions; and
2. how much of the visible archive a declared capability requires.

## 8. Why full-environment access is a retyped repair

If the observer gains access to both \(A\) and \(H\), the two native records
become:

\[
\bigl(X_T,A:\omega,H:\mathrm{blank}\bigr)
\]

and:

\[
\bigl(X_T,A:\mathrm{blank},H:\omega\bigr).
\]

Both are injective on the finite history class. Their completion-common
partition is the identity, and every preregistered target factors.

This is the correct full-environment absorber. It shows that the history was
not destroyed.

But it does not repair the old claim. The change adds:

- a physical route into \(H\);
- the controls required to read it;
- memory and bandwidth;
- a larger observer boundary; and
- a larger admitted action algebra.

The result is:

```text
ACCESS-EXPANDED FULL-HISTORY TOMOGRAPHY
```

not:

```text
THE A-ONLY RECORD WAS ALREADY SUFFICIENT.
```

It also removes strict compression in this finite class. Therefore it does
not close `H-CCR-17`.

## 9. The scoped three-way boundary

The finite host exposes a useful trilemma-like classification.

### Completion-invariant and compressive

Use:

\[
q_\ast=X_T.
\]

It is strict and common, but reconstructs only endpoint-measurable targets
such as the next reduced-matter law. It loses occurrence.

### History-sufficient and compressive

Use:

\[
r_{\mathrm{epoch}}=(X_T,b_{\mathrm{occ}}).
\]

It is strict and reconstructs the bounded occurrence target, but only in
the history-retaining archive arm. It is not a quotient of the hidden
\(A\)-only record.

### Completion-invariant and history-complete

Enlarge access to \(A+H\). The record distinguishes all finite histories.
It transfers, but is injective and resource-expanded.

### Scoped conclusion

Within this frozen matter host, completion pair, observer boundary, and
target family, no record is simultaneously:

1. completion-invariant;
2. history-sufficient beyond the Markov endpoint; and
3. noninjectively compressive.

This is not a universal impossibility theorem. A richer physical antecedent
could select one completion, guarantee a particular archive route, or impose
additional relations among histories. Such a premise would have to be
derived and charged.

## 10. Collision with strongest absorbers

### Markov sufficient state

For a Markov process, the current state is sufficient for the future
transition law. That completely absorbs the positive
\(T_{\mathrm{next}}\) result.

Dynamic Unity should keep it as a positive control because it proves that
the common-quotient method can return a real noninjective reconstruction.
It should not promote it as a new record law.

### Blackwell and statistical sufficiency

Blackwell comparison and ordinary sufficient-statistic theory already
organize which experiments or statistics retain the information needed for
a declared decision problem.

The common-quotient theorem is the deterministic finite specialization of
that terrain. Its value here is attribution:

- completion invariance is tested before target success is credited;
- capability classes are frozen separately; and
- an access expansion is not called a refinement of the old observer.

No new statistical theorem is claimed.

### Stinespring and complementary channels

A reduced channel does not uniquely determine where complementary
information is physically available. Different dilations, factorizations,
or complementary outputs can realize the same reduced dynamics.

That is exactly why the visible and hidden completion twins are admissible
at the `A_matter` rung. The reduced matter law cannot receive credit for
selecting the archive.

Once one complete coupling and boundary are physically fixed, however, the
archive location is a real part of that model. It is not dismissed as mere
notation.

### Quantum trajectories and unravellings

Different monitoring arrangements can generate different trajectory
records for one reduced open-system law. An unobserved path representation
is not automatically a retained record.

The present result respects both sides:

- the visible output is a record in the specified completion; and
- its existence does not transfer to every completion of the reduced host.

### Process tensors and full-environment completion

A complete multi-time process or full environment can retain distinctions
that a terminal reduced state erases. That absorbs the historical witness as
an omitted-process-variable result.

The Dynamic Unity question is narrower: does an independently selected,
observer-accessible, noninjective record retain the target under a frozen
boundary and action class? Full-process tomography is not that result.

### Redundant records of histories

Stable redundant environment fragments can make histories objectively
accessible. That is the strongest positive physical route.

This swing does not challenge it. It says that the reduced matter generator
does not entail that the required fragment exists at the declared observer
boundary. If a richer source--environment dynamics selects and forms those
fragments, it would exclude the hidden twin through additional physics.

## 11. What was learned about “the delta”

The work sharpens a recurring Dynamic Unity question:

> What can records do that the ordinary physical state or complete process
> does not already do?

For this host:

- the terminal physical state already carries the complete reduced future
  law;
- a formed archive adds historical occurrence capability;
- a fuller archive adds count and output-field capability; and
- complete environment access restores every history distinction but loses
  strict compression.

The potential Dynamic Unity delta is therefore not “records predict the
future.” Markov states already do that.

Nor is it “the environment contains history.” Complete dilations can do
that.

The still-open delta is:

> Can one physical dynamics itself select and form a noninjective
> observer-accessible archive whose history-sensitive held-out transfer
> survives every physically admissible completion left open by that same
> antecedent?

`HC-DU-045` shows exactly what fails when the antecedent fixes only the
reduced matter law.

## 12. `H-CCR-17` passport

| obligation | result |
|---|---|
| target-independent interface selection | fails for the epoch archive; visible and hidden arms remain admitted |
| physical formation | conditional positive in the visible fresh-output arm |
| strict compression | positive for endpoint and visible binary epoch quotients |
| nonzero pre-record target diameter | positive for all four target families across the history class |
| held-out reconstruction | completion-invariant only for reduced future behavior; historical targets fail |
| frozen-envelope sufficiency | positive for \(H_{\mathrm{matter}}\); visible-only positive for \(H_{\mathrm{occ}}\) |
| capability honesty | exact first leaks at \(H_{\mathrm{occ}}\) across completions and \(H_{\mathrm{count}}\) inside the visible epoch record |

The whole conjunction does not close.

The honest verdict remains:

```text
H-CCR-17 OPEN
```

The failure is now localized:

```text
ENDOGENOUS COMPLETION/ACCESS SELECTION
AND COMPLETION-INVARIANT HISTORICAL TRANSFER
```

## 13. What is banked

`HC-DU-045` earns:

1. the exact finite completion-common quotient theorem;
2. one exact physical instantiation in the visible/hidden completion twins;
3. a noninjective completion-invariant positive for next reduced-matter
   behavior;
4. a minimum same-common-record/different-occurrence witness;
5. a two-tier capability filtration;
6. a proof that target-coded occurrence repair is not a quotient of the
   hidden native record; and
7. a typed access-expansion/tomography absorber.

The executable certificate passes:

```text
31 / 31
```

checks and exhausts all 21,147 partitions of the nine-history arena.

## 14. What is not banked

This swing does not establish:

- a microscopic matter--environment model;
- selection of one physical completion;
- an endogenous archive or observer boundary;
- a universal completion-invariance no-go;
- an irreducible ontological remainder;
- record-first fundamentality;
- a new Markov, sufficiency, or dilation theorem;
- a new physical law;
- a physical prediction;
- a paper result;
- hardware evidence; or
- provider evidence.

## 15. Retyped `ECR-N5-S5` and completion receipt

Swing 5 is now executable as:

### Robustness and Host-Level North-Star Adjudication

**Decision question**

Does the exact boundary survive benign representation, longer horizons,
stochastic branch weights, approximate archive leakage, and every physical
premise actually selected by the host—or can one non-target-coded host
condition exclude the hidden completion and preserve historical transfer?

**Frozen inputs**

- the finite common-quotient theorem;
- the visible/hidden completion pair;
- the two-tier first-leak classification;
- the reversible support debt from `HC-DU-044`; and
- the `H-CCR-17` passport.

**Required attacks**

1. prove the endpoint common quotient and occurrence witness for arbitrary
   completed cycle count or give the first horizon where it changes;
2. retain the result under lossless archive relabeling and benign temporal
   subdivision;
3. add a declared approximate history leak to the hidden \(A\) fragment and
   derive the exact decision/error boundary rather than switching silently
   from exact to approximate sufficiency;
4. test whether any condition selected by the metastable host, rather than
   by the desired target, excludes the hidden completion;
5. keep full-environment access as a resource-changing tomography control;
   and
6. return one final host-level verdict:

```text
ENDOGENOUS_COMPRESSIVE_RECONSTRUCTION
ENDOGENOUS_OPERATIONAL_DUALITY_ONLY
FINITE_CAPABILITY_RELATIVE_REMAINDER
SELECTION_OR_FORMATION_OBSTRUCTION
INJECTIVE_TOMOGRAPHY_ONLY
INCOMPLETE_CONTRACT
```

**Likely but not precommitted outcome**

If no host-selected premise excludes the hidden twin, the correct final
verdict is:

```text
SELECTION_OR_FORMATION_OBSTRUCTION
```

for the metastable host, while the broader Dynamic Unity North Star remains
open.

**Stop**

Do not fit another detector, environment, or archive Hamiltonian merely to
remove the hostile completion. A positive exclusion must follow from the
same independently motivated physical antecedent or be labeled as a new
supplied premise.

The ten-lens
[`N5-RS` preparation](next-five-swing-host-closeout-to-record-selection-scaffold-2026-07-27.md)
preserved this exact Swing 5 as the sole next executable object. It placed a
minimum-premise and whole-DU portfolio pivot immediately afterward so an
adverse host verdict causes a disciplined redirect rather than another fitted
archive construction.

`ECR-N5-S5` is now complete as
[`HC-DU-046`](metastable-host-robustness-and-archive-relocation-obstruction-2026-07-27.md).
It proves that this boundary survives arbitrary horizon, positive weights,
lossless relabeling and benign subdivision; supplies the exact
partial-history-leak Bayes-risk law; and shows that archive relocation leaves
the host antecedent invariant while changing the interface. The scoped host
verdict is `SELECTION_OR_FORMATION_OBSTRUCTION`. Only `N5-RS-P2`, the
minimum-premise compiler and whole-DU portfolio pivot, was initially queued.
Joe subsequently interposed the
[`N5-SCF` sequence](next-five-swing-stochastic-consensus-finality-scaffold-2026-07-27.md).
Only `N5-SCF-P1` is now executable; `N5-RS-P2` is deferred.

## Bottom line

Some useful physics really is completion-invariant:

> The present matter state is enough to predict the next reduced matter
> behavior.

The history archive is not:

> Whether a write occurred is available only when the complete physical
> process places that history into the observer's admitted archive.

That is the main knowledge gain. The record hierarchy is doing real work,
but each rung changes a different capability:

```text
terminal matter
    -> future reduced behavior
visible epoch bit
    -> historical occurrence
full visible output
    -> count and resolved history
full environment
    -> completion tomography
```

The missing breakthrough is no longer vague. It is a physical reason,
independent of the desired history target, that selects which of those
interfaces actually forms and is available.
