---
title: "Action-equivalent decoder certificates, resource-timing split, and held-out status-join boundary"
status: banked_scoped_result
doc_type: exploration_result
created: 2026-07-30
claim_id: HC-DU-169
run_id: RUN-20260730-144047-action-resource-finality-quotient-audit
evidence_grade: 4
---

# Action finality is not resource finality

## Executive result

Riverlane/Rigetti's real-time QEC packet contains a small but unusually clean
example of layered finality in an actual physical control system.

The source defines three retained decoder states:

```text
DASR = 0 or 2  -> no logical error detected -> no conditional X
DASR = 1       -> logical error detected    -> conditional X
```

Thus `DASR=0` and `DASR=2` are equivalent for the downstream action. But they
are not equivalent for the retained completion-time coordinate. At every
tested round from 3 through 9, status 2 takes systematically longer than
status 0.

The same split was not detected in the later qubit response after stratifying
by round and pre-feedback qubit state. The action quotient is therefore:

- insufficient for the retained resource/timing coordinate in the discovery
  packet;
- not shown to be insufficient for the declared downstream binary response;
  and
- untestable in the independent 300,000-row timing file because that file
  omits decoder status and row identity.

Disposition:

```text
ACTION_QUOTIENT_RESOURCE_DISTINCTION
+ NO_DETECTED_ACTION_QUOTIENT_RESPONSE_DISTINCTION
+ HELDOUT_SCHEMA_CANNOT_TEST_ACTION_QUOTIENT
+ KNOWN_CONTROL_THEORY_ABSORPTION
+ NO_IMPLEMENTATION_COMPLETE_REOPENER
+ NO_READY_SUCCESSOR
```

This is a scoped Grade-4 factorization boundary with a source-pinned empirical
witness. It is not a causal decoder-status effect, population law, novel
control theorem, physical remainder, or new physics.

## 1. Frozen sources

The discovery source is the 5.6 MB
`fast_feedback_raw_data.h5` packet already audited by `HC-DU-168`, from the
[version-2 Zenodo record](https://zenodo.org/records/15364358):

```text
MD5     3b2503a80f2b92916660489e2f07e880
SHA256  dd2a3d48e86ea81094b44439fb58a3d9788757e26799bd4ee7497eb94798ed08
```

The Zenodo description explicitly states that the first decoder-register
column is the logical correction and that values 0 and 2 both mean no logical
error, while value 1 means that the decoder detected a logical error.

The [primary paper](https://arxiv.org/abs/2410.05202) describes the physical
chain: classified measurements are passed across the control system to the
FPGA decoder; the decoded result is written to registers and communicated to
a gate sequencer; a conditional \(X\) is applied; and the qubit is measured
after a fixed delay. It separately analyzes decoder and control latency.

The intended held-out source is
`decoder_timings_each_repetition.csv`:

```text
MD5     ec6e10f742b7c29627dad8ff9a97a592
SHA256  8f23b21a27004381734fefeef80e5326e0a67c391212fcb792950cf9b51bd324
```

It contains 300,000 timing rows, 100,000 each for rounds 9, 17, and 25.

Neither raw external file is committed. Hashes, audit code, and compact
derived results are durable.

## 2. The elementary quotient criterion

Let:

- \(D\) be a retained certificate state;
- \(a:D\to A\) be the control action selected by that certificate; and
- \(K_Z(\cdot\mid d)\) be the conditional law of another coordinate \(Z\).

The action quotient identifies

\[
d\sim_a d'
\quad\Longleftrightarrow\quad
a(d)=a(d').
\]

The quotient is sufficient for \(Z\) exactly when there is a kernel
\(\overline K_Z\) satisfying

\[
K_Z(\cdot\mid d)
=
\overline K_Z(\cdot\mid a(d)).
\]

Equivalently,

\[
a(d)=a(d')
\Longrightarrow
K_Z(\cdot\mid d)=K_Z(\cdot\mid d').
\]

This is the ordinary factorization criterion for a sufficient statistic. If
one same-action pair has different \(Z\)-laws, action equivalence is too
coarse for \(Z\). Nothing in the criterion is distinctively quantum or new.

For the source-defined branch,

\[
a(0)=a(2)=\text{no }X,
\qquad
a(1)=X.
\]

The audit asks whether the \(0/2\) fibre is also a fibre of the retained time
and response coordinates.

## 3. Discovery-packet timing split

The HDF5 `time` field has no unit attribute. It is therefore reported in its
retained counter units rather than cast into microseconds.

For each round, the probability-of-superiority column is

\[
\Pr(T_2>T_0)+\tfrac12\Pr(T_2=T_0)
\]

over the empirical rows.

| rounds | \(n_0\) | \(n_2\) | median \(T_0\) | median \(T_2\) | gap | superiority | KS distance |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 188 | 703 | 431 | 671 | 240 | 0.911 | 0.689 |
| 4 | 172 | 719 | 599 | 863 | 264 | 0.861 | 0.594 |
| 5 | 169 | 717 | 771 | 1091 | 320 | 0.865 | 0.634 |
| 6 | 174 | 699 | 1043 | 1347 | 304 | 0.765 | 0.403 |
| 7 | 199 | 672 | 1257 | 1609 | 352 | 0.815 | 0.497 |
| 8 | 200 | 653 | 1534 | 1838 | 304 | 0.743 | 0.362 |
| 9 | 208 | 647 | 1722 | 2078 | 356 | 0.728 | 0.376 |

All seven within-round comparisons have:

- a positive median gap;
- probability of superiority above 0.70; and
- empirical Kolmogorov--Smirnov distance above 0.35.

The retained empirical timing kernel therefore does not factor through the
source-defined action quotient.

This does not identify why the statuses differ. The status may encode a
different decoder path, internal stopping condition, syndrome class, or
another implementation detail. Those explanations remain outside the public
packet. The result is predictive and architectural, not causal.

## 4. Downstream response audit

Let:

- \(X_{\rm pre}\) be qubit 50's final QEC measurement;
- \(Y\) be its later measurement; and
- \(a(D)=\mathbf1[D=1]\).

The source-defined no-refit response failure is

\[
E
=
\mathbf1\!\left[
Y\ne X_{\rm pre}\oplus a(D)
\right].
\]

Across rounds 3 through 9:

| status | failures | rows | raw rate |
|---:|---:|---:|---:|
| `DASR=0` | 487 | 1,310 | 0.372 |
| `DASR=2` | 1,700 | 4,810 | 0.353 |

A Cochran--Mantel--Haenszel score stratified by round and
\(X_{\rm pre}\) gives

```text
z = 1.509
two-sided normal p = 0.131
```

The frozen five-percent test therefore detects no response split.

That is not evidence that the response laws are equal. The test is finite,
observational, and conditions on only retained fields. It says the strong
timing split does not automatically become a detected split in this binary
response coordinate.

## 5. Held-out replication boundary

The independent timing CSV has exactly three columns:

```text
rounds, cycles, time_per_round
```

It has:

- no `DASR` or decoder-result field;
- no action field;
- no shot or repetition identifier joining it back to another archive; and
- no response.

Therefore its 300,000 rows cannot test

\[
P(T\mid DASR=0)
\quad\text{versus}\quad
P(T\mid DASR=2).
\]

This is not a failed replication and not a null result. It is an exact schema
kill:

```text
HELDOUT_SCHEMA_CANNOT_TEST_ACTION_QUOTIENT
```

The minimum completing sidecar is small: retain the decoder status beside
each timing row, or retain a stable row identifier that joins timing to the
decoder-register packet. More timing samples without that join do not answer
the question.

## 6. What “layered finality” earns here

This apparatus supports at least four different quotients:

| layer | equivalence question |
|---|---|
| certificate finality | Which decoder states have been retained? |
| action finality | Which states authorize the same physical control branch? |
| resource/timing finality | Which states have the same completion-time law? |
| response finality | Which states have the same downstream response law under the frozen local-state contract? |

The packet gives an exact warning:

> A quotient can be final for one capability while still erasing distinctions
> relevant to latency, cost, provenance, or another action class.

This is the physically typed version of Dynamic Unity's
observer/action/resource relativity rule. It is not subjective: every layer
is an objective relation among a physical controller, retained fields,
declared action, and measured consequence.

It also clarifies the distributed-systems analogy. A node may possess enough
certificate information to choose the same branch while lacking enough
lineage to predict when the branch becomes available. Action agreement,
latency agreement, provenance agreement, and public finality are different
contracts. No FLP, CAP, BFT, or consensus theorem transfers merely from that
structural resemblance.

## 7. Absorption and novelty

The mathematical criterion is absorbed by:

- sufficient statistics and kernel factorization;
- Markov lumpability;
- state minimization for automata and controllers; and
- ordinary feedback-control and QEC latency analysis.

The paper already studies decoder timing and physical feedback. Dynamic
Unity's scoped contribution is the typed cross-coordinate audit:

1. use the source's own action equivalence;
2. test whether it preserves another retained coordinate;
3. distinguish timing/resource sufficiency from response sufficiency; and
4. expose the exact field missing from the held-out archive.

No novel general theorem or new physical effect is claimed.

## 8. Consequence for the North Star

The result strengthens one methodological premise of layered regional
finality: there need not be one globally sufficient “record.” Sufficiency is
indexed by the action, target coordinate, resources, and retained lineage.

It does not satisfy the flagship's implementation-complete reopener. The
packet still lacks the all-attempt census, controller implementation,
complete archive/reset semantics, and hidden-environment scope named by
`HC-DU-168`.

The flagship therefore remains parked. No successor is ready.

## Reproducibility

Run:

```bash
uv run --with h5py python \
  tests/du_action_resource_finality_quotient_audit.py \
  --fast-source /path/to/fast_feedback_raw_data.h5 \
  --timing-source /path/to/decoder_timings_each_repetition.csv \
  --write-artifact
```
