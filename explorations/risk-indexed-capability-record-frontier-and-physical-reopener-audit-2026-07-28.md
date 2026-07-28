---
title: "Risk-indexed capability--record frontier and physical reopener audit"
status: completed_scoped_theorem_and_portfolio_adjudication
doc_type: exact_decision_frontier_no_scope_theorem_and_unchanged_physical_audit
created: 2026-07-28
claim_id: HC-DU-071
work_id: RISK-INDEXED-CAPABILITY-RECORD-CLOSURE
program_id: CCR-RISK-INDEXED-CAPABILITY-FRONTIER
run_id: RUN-20260728-082431-risk-indexed-capability-frontier
claim_grade: "SCOPED GRADE-4 RISK-INDEXED CAPABILITY POLARITY, NO-SCOPE-FROM-CONFIDENCE THEOREM, THREE-MARGIN NON-UNIFICATION, AND PHYSICAL REOPENER ADJUDICATION / BLACKWELL, LE CAM, MINIMAX, DATA-PROCESSING, AND FORMAL-CONCEPT COMPONENTS ABSORBED / NO NEW PROBABILITY THEOREM, PHYSICAL LAW, RECORD ONTOLOGY, GRADE-5 REMAINDER, PREDICTION, PAPER, MODEL, OR HARDWARE RESULT"
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Risk-indexed capability--record frontier

## Executive result

`HC-DU-070` showed that a full-support null can forbid zero-error exclusion
while still permitting finite-confidence discrimination. That correction
does **not** mean confidence can make a record answer a question it did not
already statistically address.

The exact boundary is:

```text
record laws differ across target classes
  -> controlled risk may fall with better readout or more samples

complete joint record laws are identical across target classes
  -> every record-only binary decision has worst-case error at least 1/2
  -> repetition, consensus, signatures, and confidence cannot create scope
```

For a fixed target, loss, resource envelope, and acceptable error, records and
actions form an antitone polarity. Its closed pairs give a complete lattice of
risk-feasible action families and record families. This is the controlled-risk
version of `HC-DU-064`, but it is not one universal ladder of finality:
different targets, losses, budgets, and error thresholds define different
contracts.

The physical audit returns:

- material gauge-boundary and metastable records can cross nonzero-risk
  thresholds when their accessible laws already retain target information;
- stabilizer syndrome and gravitational-wave intensity records exactly close
  their frozen recovery or intensity jobs while leaving logical or oriented
  jobs open;
- identical-law interior, logical, occurrence, and orientation fibres retain
  a binary \(1/2\) minimax floor;
- proper-time and CHSH specimens can separate frozen **theory families**
  without selecting a formed record interface or reconstructing a physical
  source;
- infrared memory still lacks a complete operational record contract; and
- the provider QND packet still lacks implementation-complete acquisition and
  physical data.

The three relevant margins are therefore independent:

```text
theory-law separation
    != record-to-target reconstruction
    != antecedent-to-interface selection.
```

No audited arena satisfies all three with complete acquisition and a held-out
target. The corrected risk route is real, but it activates no Dynamic Unity
scientific successor.

```text
NO_READY_SCIENTIFIC_SUCCESSOR
```

## 1. Frozen decision object

Let:

- \(H\) be a nonempty finite history/completion class;
- \(R\) be a target-independent record with finite outcome set \(Z_R\);
- \(Q_R(z\mid h)\) be its **complete joint** record law;
- \(A\) be a frozen family of future actions or queries;
- \(P_a(y\mid h)\) be the held-out response law for \(a\in A\); and
- \(\varepsilon_a\in[0,1]\) be a threshold fixed before decoding.

For total-variation loss, define the minimax reconstruction deficiency

\[
d_R(a)
=
\min_{K_a:Z_R\rightsquigarrow Y_a}
\max_{h\in H}
\operatorname{TV}
\left(
P_a(\cdot\mid h),
\sum_z Q_R(z\mid h)K_a(\cdot\mid z)
\right).
\]

The minimum exists because the finite Markov-kernel polytope is compact and
the objective is continuous. The risk-feasible action frontier is

\[
\mathcal C_\varepsilon(R)
=
\{a\in A:d_R(a)\leq\varepsilon_a\}.
\]

This object is deliberately target- and contract-relative. It does not call
an observer capable merely because a statistic is estimable under an
undeclared prior, loss, budget, or error tolerance.

General bounded losses may replace total variation. Total variation is used
here because it is the exact finite response-law deficiency already banked in
`HC-DU-036C`.

## 2. Risk-indexed capability polarity

Fix a universe \(\mathfrak R\) of admitted records and the complete threshold
contract \(\varepsilon=(\varepsilon_a)_{a\in A}\). Define

\[
\Phi_\varepsilon(S)
=
\left\{
R\in\mathfrak R:
\sup_{a\in S}d_R(a)\leq\varepsilon_a
\right\},
\]

for \(S\subseteq A\), and

\[
\Psi_\varepsilon(\mathcal T)
=
\left\{
a\in A:
\sup_{R\in\mathcal T}d_R(a)\leq\varepsilon_a
\right\},
\]

for \(\mathcal T\subseteq\mathfrak R\).

### Theorem 1 — risk-indexed antitone Galois connection

\[
S\subseteq\Psi_\varepsilon(\mathcal T)
\quad\Longleftrightarrow\quad
\mathcal T\subseteq\Phi_\varepsilon(S).
\]

#### Proof

Either side says exactly that

\[
d_R(a)\leq\varepsilon_a
\qquad
\text{for every }a\in S,\ R\in\mathcal T.
\]

Therefore \(\Phi_\varepsilon\) and \(\Psi_\varepsilon\) are antitone. Their
composites are extensive, monotone, and idempotent closure operators. The
closed record/action pairs form the complete formal-concept lattice of the
binary incidence relation

\[
R\,I_\varepsilon\,a
\quad\Longleftrightarrow\quad
d_R(a)\leq\varepsilon_a.
\qquad\square
\]

### What this earns

It gives one exact answer to “which record is final enough for which future
job at which declared risk?” It also preserves regional incomparability:
records useful for different actions need not form a chain.

### What it does not earn

- The lattice does not form any record physically.
- It does not select \(\varepsilon\), the loss, the target, or the resource
  budget.
- It does not turn a semantic join into a jointly realizable interface.
- Lattices from different risk contracts do not become one canonical scalar
  finality scale.

The theorem is formal-concept analysis applied to a Blackwell/Le Cam
decision relation. Its component mathematics is known and absorbed.

## 3. No-scope-from-confidence

### Theorem 2 — exact factorization boundary

In the frozen finite arena,

\[
d_R(a)=0
\]

if and only if there is a Markov decoder \(K_a\) satisfying

\[
P_a(\cdot\mid h)
=
\sum_z Q_R(z\mid h)K_a(\cdot\mid z)
\qquad
\text{for every }h\in H.
\]

This is exact stochastic factorization. The compactness clause matters:
without an attained minimum, an infimum of zero alone would not supply the
decoder.

### Theorem 3 — postprocessing cannot improve reconstruction

Suppose \(S\) is obtained from \(R\) by a common target-independent
postprocessing kernel \(L\):

\[
Q_S=Q_RL.
\]

Then

\[
d_R(a)\leq d_S(a)
\qquad
\text{for every }a.
\]

#### Proof

Every decoder \(K\) from \(S\) induces the decoder \(LK\) from \(R\).
Optimization over all decoders from \(R\) cannot perform worse than
optimization over this restricted composite family. \(\square\)

This is the decision-theoretic data-processing law. Authentication, hashing,
majority voting, consensus, compression, and public certification can make a
record easier to trust, retrieve, or act on. As target-independent downstream
maps, they cannot split a target fibre already collapsed by the upstream
record law.

### Theorem 4 — identical complete-law minimax floor

Let \(h_0,h_1\in H\) have opposite deterministic binary targets:

\[
P_a(\cdot\mid h_0)=\delta_0,
\qquad
P_a(\cdot\mid h_1)=\delta_1.
\]

If their complete joint record laws agree,

\[
Q_R(\cdot\mid h_0)=Q_R(\cdot\mid h_1),
\]

then

\[
d_R(a)\geq\frac12.
\]

#### Proof

Every record-only decoder has one common binary output law \(\mu\) under both
histories. Its two errors are \(1-\mu(0)\) and \(1-\mu(1)\). Their sum is one,
so their maximum is at least \(1/2\). A fair randomized guess attains
\(1/2\). \(\square\)

For every repetition count \(n\), the same result holds whenever the
**complete \(n\)-record laws** agree. In particular, conditionally independent
repetition of identical one-shot laws cannot help.

Equality of one-shot marginals alone is not enough for this conclusion.
History-dependent correlations or a joint measurement can expose synergy
absent from each marginal. That possibility is why the theorem is stated
against the complete admitted joint law rather than against a list of
individual readouts.

### Corollary — confidence lowers risk; it does not create target information

Repeated measurement can lower risk only when the admitted joint record law
already differs across the target classes. Lower p-values quantify evidence
inside a sensitive channel. They do not widen that channel's physical target
scope.

## 4. Three margins that must not be collapsed

### 4.1 Theory-law separation

For frozen null and alternative law families \(\mathcal N,\mathcal A\) on a
complete transcript space, one possible robust margin is

\[
\delta_{\rm law}
=
\inf_{p\in\mathcal N,\ q\in\mathcal A}
\operatorname{TV}(p,q).
\]

A positive value supports a finite-confidence theory test under the declared
acquisition and error contract.

### 4.2 Record-to-target reconstruction

\(d_R(a)\) asks whether the held-out response law factors, exactly or within
risk, through the formed record. It can vanish even when there is no rival
physical law to separate.

### 4.3 Antecedent-to-interface selection

Selection asks whether every admissible implementation under the claimed
physical antecedent induces the same accessible record interface, up to the
frozen operational equivalence. A supplied detector may have \(d_R(a)=0\)
while the antecedent still permits visible, hidden, differently oriented, or
differently calibrated interfaces.

These are differently typed objects, not three terms in one scalar score.

### Minimum independence controls

| Control | Theory-law margin | Reconstruction | Interface selection |
|---|---|---|---|
| Frozen CHSH law families | positive bounded-score margin | no DU formed-record target is supplied | not established |
| Closed gravitational-wave intensity archive | no rival-law margin is needed | \(d_R(T_I)=0\) | probe, orientation, and archive are supplied |
| Antecedent-selected constant register with a varying binary target | no rival-law margin | \(d_R=1/2\) | closed by construction |

No column implies either of the other two.

Blackwell's comparison of statistical experiments and Le Cam deficiency
absorb the decision-theoretic core. In the quantum setting, channel
randomization criteria make the same distinction; see Anna Jenčová,
[*Comparison of quantum channels and statistical
experiments*](https://arxiv.org/abs/1601.06370). Dynamic Unity's earned
increment is the typed composition with physical formation, access, and
interface-selection fibres.

## 5. Unchanged physical audit

No interface, source, target, loss, or resource contract was refitted for this
audit.

| Arena | Frozen job | Risk/frontier result | Formation and selection | Acquisition | Disposition |
|---|---|---|---|---|---|
| Material `Z3` gauge boundary | reconstruct boundary flux | ideal QND archive has \(d=0\); independent archive errors lower majority risk for flux, while common shock does not | carrier and write are physically formed; boundary, orientation, calibration, archive route, and access remain supplied | exact in the finite specimen | useful scoped positive; no reopener |
| Material `Z3` gauge boundary | distinguish interior site within fixed flux | histories \((0,1)\) and \((1,0)\) induce the same complete flux-record law and opposite binary interior labels, so \(d=1/2\) | unchanged | exact in the finite specimen | confidence cannot recover interior scope |
| Stabilizer syndrome | frozen correctable-class record-only recovery | complete syndrome gives \(d=0\) for the declared recovery quotient | code, checks, QND interface, archive, and recovery class are supplied | exact finite theorem | useful scoped positive; no endogenous selector |
| Stabilizer syndrome | distinguish or undo a nontrivial logical coset in \(N(S)/S\) | same syndrome can carry opposite held-out logical consequences; binary restriction has \(d\geq1/2\) | unchanged | exact finite theorem | protected logical remainder |
| Metastable host endpoint | next reduced-matter branch | endpoint has \(d=0\) | host selects transition law but not visible archive routing or access | exact finite theorem | ordinary Markov operational closure |
| Metastable host history leak | occurrence across \(h_0,h_4\) | with reveal probability \(\lambda\), minimax error is \((1-\lambda)/2\); at \(\lambda=0\) it stays \(1/2\), and exact closure arrives only at \(\lambda=1\) | the leak route is supplied, not selected by the host | exact finite theorem | clearest positive control: risk changes only when record law changes |
| Causally closed gravitational wave | downstream normalized intensity | supplied intensity archive has \(d=0\) under orthogonal transport | lawful transport does not select probe, material reference, or archive | exact finite sector | strict noninjective transfer |
| Causally closed gravitational wave | oriented polarization response | \(x\) and \(-x\) have the same intensity law and opposite signed response; binary subproblem has \(d=1/2\) | unchanged | exact finite sector | capability-relative remainder |
| Finite-time infrared memory | bounded operational memory to held-out hard target | \(d_R(a)\) is not yet well typed because the bounded record and target contract are incomplete | soft carrier forms; detector worldtube, resolution, archive, access, and target remain supplied | incomplete | `PARTIAL_PHYSICAL_TYPING`; no reopener |
| Proper-time coherent histories | reject a frozen classical-history channel family | coherent recombination can yield a positive process-family margin; terminal reduced dephasing alone has zero such margin | complete instrument and rival family are supplied; source labels remain underidentified | exact conditional theorem; no new data | theory certification, not source or interface selection |
| Provider QND packet | incomplete pointer \(\rightarrow\) environment repair \(\rightarrow\) causal break | ordinary-QM conditional prediction is frozen, but no physical estimate is returned | circuit interface is supplied | synthetic only; provider ceiling is returned-shot conditional | prediction remains locked; no scientific promotion |
| CHSH control | distinguish frozen quantum and PR-box law classes | full support blocks zero-error exclusion, while the bounded win-score margin gives controlled finite error | no DU record-formation or source-reconstruction interface | mathematical control only | calibration for `HC-DU-070`, not a successor |

### The important positive case

The metastable leak family shows that controlled risk can enlarge the usable
action set without exact sufficiency. For the equal-prior occurrence pair,

\[
d_{R_\lambda}(O)=\frac{1-\lambda}{2}.
\]

For a declared tolerance \(\varepsilon<1/2\), occurrence enters the
risk-feasible frontier exactly when

\[
\lambda\geq1-2\varepsilon.
\]

That is genuine operational progress. It comes from a changed accessible
record law—the history token is sometimes revealed—not from confidence
applied to an unchanged endpoint.

## 6. Portfolio adjudication

A controlled-risk physical successor required all of:

1. a physically warranted law family or record process;
2. complete acquisition and a frozen error model;
3. a target-independent formed interface;
4. an independently held-out target;
5. a positive robust reconstruction or theory-separation margin after the
   strongest legitimate class enlargement; and
6. no interface, source, decoder, or resource refit.

No audited arena satisfies the conjunction.

- Gauge, QEC, metastable, and wave specimens have useful exact or risk-indexed
  transfer results, but their decisive interfaces or archive routes are
  supplied.
- Proper time and CHSH have theory-family separation without the missing
  physical interface-selection result.
- Infrared memory lacks the complete bounded operational contract.
- The provider packet lacks implementation-complete acquisition and returned
  physical data.

The result is therefore:

```text
NO_READY_SCIENTIFIC_SUCCESSOR
```

This is not whole-repository exhaustion and not a no-go against physical
record selection. It says the `HC-DU-070` controlled-risk correction does not
by itself reopen any current candidate.

## 7. Durable consequences

### Keep

1. Exact finality is the zero-risk boundary of a broader action-indexed
   decision frontier.
2. Approximate finality must declare target, loss, error threshold, resource
   envelope, and complete joint record law.
3. Confidence may improve reliability or admit an action before exact
   sufficiency, but only through target-sensitive record laws.
4. Theory testing, record reconstruction, and interface selection require
   separate receipts.
5. Regional finality remains a lattice or profile, not one scalar confidence
   level.

### Stop

1. Do not call more copies independent physical sources.
2. Do not infer a broader target scope from a lower p-value.
3. Do not infer physical interface selection from \(d_R(a)=0\).
4. Do not infer record reconstruction from a positive theory-law margin.
5. Do not rerun gauge, QEC, metastable, wave, proper-time, or CHSH controls
   unless a new physical selector or complete acquisition contract is
   supplied.

### Reopen

Reopen this frontier only when a candidate supplies:

- a physically selected formed record interface;
- complete acquisition and frozen noise;
- a held-out target and action family;
- a declared loss/resource/error contract;
- a positive deficiency or theory-separation result robust to the strongest
  legitimate class enlargement; and
- an unchanged no-refit transfer.

## 8. Grade and novelty

The exact polarity, deficiency, minimax floor, data-processing relation, and
decision lattice are standard or direct consequences of standard theory.
Relevant foundations include:

- David Blackwell,
  [*Equivalent Comparisons of
  Experiments*](https://doi.org/10.1214/aoms/1177729032); and
- Anna Jenčová,
  [*Comparison of quantum channels and statistical
  experiments*](https://arxiv.org/abs/1601.06370).

Dynamic Unity earns a scoped Grade-4 typed necessity/non-unification result:
controlled statistical confidence does not collapse theory separation,
record reconstruction, interface selection, and capability into one object.

It earns no new law of probability or physics, no record ontology, no
Grade-5 remainder, no prediction, no paper claim, and no hardware result.

## 9. Reproducibility

No new local research model was admitted. The result is exact and reuses
already executed specimens. Regression is by the existing unchanged probes:

```bash
python3 tests/du_capability_indexed_north_star_probe.py
python3 tests/du_distributed_physical_collision_probe.py
python3 tests/du_operational_theory_landscape_probe.py
```

Those probes validate their original finite fixtures. They do not promote the
present synthesis beyond its scoped grade.
