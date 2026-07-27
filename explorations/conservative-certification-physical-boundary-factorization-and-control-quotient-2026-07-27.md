---
title: "Conservative certification, physical-boundary factorization, and control-quotient sufficiency"
status: complete__scoped_theorem_package__known_mathematics_absorbed
doc_type: research_result
created: 2026-07-27
authority: "Joe direct chat: Go"
sequence_id: N5-PF
work_id: N5-PF-P2
hypothesis_id: HC-DU-055
assumption_version: EXACTLY_COMPENSATED_PREFERRED_FOLIATION
assumption_status: "HELD CONDITIONAL PREMISE / NO EVIDENTIARY GRADE"
maximum_grade: "SCOPED DETERMINISTIC, STOCHASTIC-KERNEL, AND QUANTUM-PROCESS NECESSITY PACKAGE"
mathematical_novelty: "ABSORBED BY QUOTIENT FACTORIZATION, STOCHASTIC POSTPROCESSING, AND QUANTUM PROCESS LINEARITY"
new_physics: false
claim_status_change: "HC-DU-055 banked at scoped theorem-package grade"
prediction_state_change: none
paper_state_change: none
hardware_state_change: none
next_position: N5-PF-P3
---

# Conservative certification, physical-boundary factorization, and control-quotient sufficiency

## Executive result

A certificate can change what a system is permitted or able to do without
changing the source law and without introducing a new physical force. The
causal path is:

```text
formed record
    -> physical certificate carrier and verifier
    -> semantic verdict
    -> policy/controller state
    -> physical boundary input
    -> response.
```

Once the complete pre-response history \(X\) and complete physical boundary
input \(B\) are held fixed, changing only the semantic certificate label
\(C\) cannot change the response unless one of four things happened:

1. \(X\) or \(B\) was incomplete;
2. the compared occurrences were not the same physical occurrences;
3. the process was changed so that \(C\) became a new physical input; or
4. reproducibility failed.

The more useful negative result is that a declared control label \(U\) need
not be complete. Two controls can share a convenient label while differing in
route, timing, controller memory, carrier phase, hysteresis, reset state, or
quantum instrument. Exact deterministic, stochastic, and quantum witnesses
all exhibit that failure.

The theorem package is useful but mathematically absorbed. It does not
establish a certificate force, new quantum mechanics, new physical law, or
grade-5 remainder.

Position 2 returns:

```text
CONSERVATIVE_CERTIFICATION_THEOREM
PHYSICAL_BOUNDARY_FACTORIZATION
DECLARED_CONTROL_SUFFICIENCY_IFF_VALID_POSTPROCESSING
CAPABILITY_WITHOUT_SOURCE_CHANGE
EXACT_EXTRA_BOUNDARY_STATE_WITNESSES
NO_COUNTEREXAMPLE_TO_CONSERVATIVITY_AFTER_COMPLETE_MATCH
MATHEMATICAL_CORE_FULLY_ABSORBED
FOLIATION_INERT
```

## 1. Frozen typed contract

Let:

- \(X\) be the complete admitted pre-response state and history of the
  response system and its retained environment;
- \(R\) be the physically formed source record;
- \(K\) be the complete certificate carrier, verifier, and controller state;
- \(C=\gamma(R,K)\) be the semantic certificate verdict;
- \(P\) be the policy mapping verdicts to physical action families;
- \(B\) be the complete physical boundary input from the
  certificate/controller apparatus into the response system, including the
  selected operation and every admitted side channel;
- \(U=q(B)\) be a declared control label or channel, potentially lossy;
- \(Y\) be the held-out response; and
- \(L\) be the matched resource, reset, route, and occurrence ledger.

Two distinct questions must remain separate:

\[
Y\perp C\mid X,B
\tag{semantic inertness}
\]

and

\[
Y\perp B\mid X,U.
\tag{declared-control sufficiency}
\]

The first is conservative after physical completeness is earned. The second
is a substantive quotient test and often fails.

## 2. Deterministic theorem package

### Theorem 2.1 — semantic inertness after a complete physical match

Let the response process be

\[
G:X\times B\longrightarrow Y.
\]

Let \(C\) be any semantic label attached to the same physical realization.
Then the extended response

\[
\widetilde G(x,b,c)=G(x,b)
\]

is constant on every fixed-\((x,b)\) certificate fibre.

Conversely, a proposed map

\[
H:X\times B\times C\longrightarrow Y
\]

descends through the projection

\[
\pi(x,b,c)=(x,b)
\]

if and only if

\[
\ker\pi\subseteq\ker H.
\]

Therefore a reproducible \(C\)-dependent response at fixed \(X,B\) is not a
counterexample to ordinary physical causation. It is evidence that the
physical contract was incomplete, the occurrences were mismatched, or the
dynamics/ontology was enlarged so that \(C\) is itself a physical input.

This result is deliberately close to definitional. Its scientific use is as a
completeness and attribution discipline, not as new mathematics.

### Theorem 2.2 — deterministic control-quotient criterion

Let

\[
F:X\times B\longrightarrow Y,
\qquad
q:B\longrightarrow U.
\]

A unique decoder on the image,

\[
\overline F:X\times q(B)\longrightarrow Y,
\]

exists with

\[
F=\overline F\circ(\mathrm{id}_X,q)
\]

if and only if

\[
\ker(\mathrm{id}_X,q)\subseteq\ker F.
\]

Equivalently,

\[
x=x',\ q(b)=q(b')
\Longrightarrow
F(x,b)=F(x',b').
\]

The smallest deterministic witness fixes \(X\), assigns the same declared
label `ACT` to physical operations `IDENTITY` and `FLIP`, and observes
different \(Y\). The label failed; the complete physical boundary did not.

## 3. Stochastic theorem package

Fix \(x\). Let:

- \(M_x(y\mid b)\) be the physical response channel from boundary input to
  response;
- \(Q(u\mid b)\) be the declared-control channel; and
- \(T_x(y\mid u)\) be a candidate stochastic decoder.

### Theorem 3.1 — operational stochastic postprocessing

The response channel is reproducible from the declared-control channel by a
valid stochastic postprocessing if and only if a nonnegative row-stochastic
\(T_x\) exists such that

\[
M_x=QT_x.
\]

This is a finite linear-feasibility problem. Column-space membership or a
signed solution is not sufficient: positivity and normalization are
load-bearing.

The exact positive control is

\[
Q=
\begin{pmatrix}
3/4&1/4\\
1/4&3/4
\end{pmatrix},
\qquad
T=
\begin{pmatrix}
4/5&1/5\\
1/5&4/5
\end{pmatrix},
\]

which gives

\[
M=QT=
\begin{pmatrix}
13/20&7/20\\
7/20&13/20
\end{pmatrix}.
\]

Two exact obstructions are retained:

1. If the rows of \(Q\) are equal while the rows of \(M\) differ, no \(T\)
   can exist.
2. With the invertible \(Q\) above and \(M=I\), the unique linear solution is

   \[
   T=Q^{-1}M=
   \begin{pmatrix}
   3/2&-1/2\\
   -1/2&3/2
   \end{pmatrix}.
   \]

   Its rows sum to one, but its negative entries make it physically invalid.

### Important scope correction

The equation \(M=QT\) proves channel simulation or Blackwell-style
postprocessing. It does **not**, by itself, prove conditional independence in
an already existing joint experiment. To claim

\[
Y\perp B\mid X,U
\]

for the actual process, one must freeze the joint kernel and prove

\[
J_x(u,y\mid b)=Q(u\mid b)T_x(y\mid u).
\]

Marginal response factorization alone leaves correlations between \(U\) and
\(Y\) underdetermined. This distinction prevents a channel-level repair from
being misreported as a complete causal-process result.

The mathematical absorber is the comparison/postprocessing order of
statistical experiments, classically associated with
[Blackwell's comparison of experiments](https://digicoll.lib.berkeley.edu/record/112749).
Dynamic Unity's contribution here is the typed separation among certificate
meaning, physical boundary, declared control, actual joint process, and
capability—not a new Blackwell theorem.

## 4. Quantum-process theorem package

A quantum treatment cannot replace the boundary input with hidden classical
values. Let \(\mathcal W\) be a frozen process tensor or quantum comb and let
\(J_b\) be the Choi operator of the complete inserted instrument associated
with physical boundary choice \(b\).

### Theorem 4.1 — semantic equivalence

If two semantic labels insert the same complete instrument,

\[
J_b=J_{b'},
\]

then every response obtained by linking that instrument to the same process
tensor is identical. This is linearity of the process link, not a new
physical principle.

### Theorem 4.2 — deterministic quantum control-class criterion

For a declared class map \(q:B\to U\), that class is sufficient for the
selected complete response if and only if

\[
\mathcal W\star(J_b-J_{b'})=0
\qquad
\text{whenever }q(b)=q(b').
\]

If every admissible future tester is included, the same condition must hold
for the complete output process, not only one terminal probability.

The exact qubit witness declares both \(I\) and \(Z\) to be
`POPULATION_PRESERVING`. On input

\[
|+\rangle=(|0\rangle+|1\rangle)/\sqrt2,
\]

both operations leave computational-basis populations at \(1/2,1/2\), but an
\(X\)-basis readout gives

\[
\Pr(+\mid I)=1,
\qquad
\Pr(+\mid Z)=0.
\]

The classical label erased a phase-sensitive instrument difference. This is
not a certificate-only effect.

The primary absorbers are:

- [Pollock et al.'s process-tensor framework](https://arxiv.org/abs/1512.00589)
  for arbitrary memory-bearing multi-time quantum processes;
- [Chiribella, D'Ariano, and Perinotti's supermap realization theorem](https://arxiv.org/abs/0804.0180);
  and
- the [quantum-comb/link-product framework](https://arxiv.org/abs/0904.4483).

The DU-specific discipline is to require the complete instrument, retained
memory, occurrence identity, and capability envelope before calling two
controls “the same.”

## 5. Capability without source change

Let a verifier produce:

```text
FAIL -> safe actions {WAIT}
PASS -> safe actions {WAIT, RELEASE}.
```

This is a strict capability change. It can occur while the source dynamics
remain fixed:

```text
same source law
    -> different formed evidence
    -> different verified verdict
    -> different policy state
    -> NO_SIGNAL versus RELEASE_SIGNAL
    -> different safe action set.
```

The certificate matters. Its meaning is not epiphenomenal. But what couples
to the response system is the physical verifier/controller/boundary process.
This is the conservative bridge between records and capability:

> certification changes capability by changing which physical controls are
> warranted and executed, not by adding a semantic force to the equations of
> motion.

If a proposed certificate changes \(Y\) with \(X\) and complete \(B\) fixed,
the conservative theory has a crisp response: audit the omitted boundary
state, occurrence identity, or modified dynamics.

## 6. Hostile-case attribution

| apparent residual | first typed diagnosis | what must be matched |
|---|---|---|
| controller remembers an earlier certificate | incomplete \(X\) or \(B\) | controller and retained-environment memory |
| same control travels through different routes | incomplete \(B\) | carrier, route, timing, phase, attenuation, side channels |
| response depends on prior operations | incomplete \(X\) or \(B\) | hysteresis and full multi-time instrument |
| accepted shots come from different attempts | occurrence mismatch | attempt identity, selection, rejection, reset, and lineage |
| certificate label enters the response law directly | modified dynamics or ontology | state the new coupling and its empirical excess |
| “same quantum action” hides \(I\) versus \(Z\) | lossy \(U\) | complete Choi/instrument description |

No hostile case produced a counterexample to semantic conservativity after a
complete physical match. Several produced exact counterexamples to declared
control sufficiency.

## 7. Preferred-foliation collision

The complete theorem package depends on causal maps and factorization, not on
a simultaneity convention.

Consider the partial order:

```text
record --------\
                -> certify -> act -> respond
controller ----/
ready
```

The two linear extensions

```text
record, controller-ready, certify, act, respond
controller-ready, record, certify, act, respond
```

give the same complete state and response. A preferred leaf can choose one
ordering, while the causal-partial-order representation retains only the
parent relations. Forgetting the privileged ordering changes none of the
factorization results.

If preferred tick phase reaches the response, it is a physical field in
\(B\). That either exposes an unmatched boundary input or leaves the exactly
compensated branch. It is not evidence that semantic certificates exert a
force.

Return:

```text
FOLIATION_INERT
```

## 8. What was and was not learned

### Earned

1. The certificate-force question and control-sufficiency question are
   different.
2. Semantic inertness after a complete physical match has one unchanged
   deterministic, stochastic-process, and quantum-process grammar.
3. A convenient control label can erase exactly the physical information
   needed for prediction.
4. Positivity separates a physical stochastic decoder from a merely signed
   linear solution.
5. Marginal channel postprocessing is weaker than conditional independence
   in the actual joint process.
6. Certification can strictly enlarge safe capability through ordinary
   physical feedback with no source-law change.
7. The result is branch-invariant under the matched
   preferred-leaf/causal-partial-order comparison.

### Not earned

- a certificate-only physical force;
- a new law of nature;
- a new quotient, Blackwell, supermap, comb, or process-tensor theorem;
- a proof that any particular proposed boundary \(B\) is physically complete;
- an observer-independent ontology;
- a grade-5 physical remainder;
- a prediction or hardware result; or
- a paper promotion.

## 9. Why the result matters despite absorption

The result removes a tempting but low-value frontier: searching for a
semantic certificate to exert an extra physical force. It also exposes the
real open dependency.

Saying “condition on the complete boundary \(B\)” is scientifically useful
only if \(B\) is selected independently of the response one wants to explain.
Otherwise omitted variables can always be added after the fact until
factorization becomes true.

The next problem is therefore not another control witness. It is:

> What independently motivated physical antecedent selects the complete
> response-relevant feedback boundary—or at least its equivalence class under
> every frozen future action—without target coding?

This is sharper than demanding raw point-identification of every microscopic
carrier detail. Let

\[
b\sim_{\mathcal A}b'
\]

when all responses in the frozen future action/tester family
\(\mathcal A\) agree for \(b,b'\). Position 3 should ask whether the physical
antecedent selects:

\[
[B]_{\mathcal A}=B/{\sim_{\mathcal A}},
\]

not necessarily one microscopic \(B\). A positive orbit/class selector would
be enough for operational completeness; a relocation pair that crosses these
classes would be the exact obstruction.

## 10. Position-3 handoff

Activate:

```text
N5-PF-P3
Complete Physical Feedback-Boundary Selection or Response-Equivalence Obstruction
```

### Decision

Given an independently fixed physical antecedent \(A\), is the complete
feedback boundary constant on the \(A\)-fibre up to the full admitted
response-equivalence relation?

Formally, seek:

\[
A(m)=A(m')
\Longrightarrow
B(m)\sim_{\mathcal A}B(m').
\]

### Efficient approach

1. Freeze the future action/tester family \(\mathcal A\) before choosing the
   boundary.
2. Define the coarsest response-equivalence class of physical boundary
   implementations.
3. Reuse existing carrier/verifier/controller/route/reset specimens rather
   than building a new host.
4. Hold source, formed record, certificate content, resources, and observable
   response law fixed while varying route and access implementation.
5. Search first for an exact relocation pair that crosses
   \(B/{\sim_{\mathcal A}}\).
6. If one exists, identify the smallest additional target-independent
   physical premise that closes it.
7. Carry the preferred-leaf/partial-order control; expect the foliation to
   remain inert unless a tick-dependent boundary field is made accessible.

### Predeclared returns

```text
PHYSICAL_ANTECEDENT_SELECTS_RESPONSE_EQUIVALENCE_CLASS
PARTIAL_OR_ORBIT_BOUNDARY_SELECTION
FEEDBACK_BOUNDARY_RELOCATION_OBSTRUCTION
CAPABILITY_DEPENDENT_FIRST_LEAK
TARGET_CODED_REPAIR
FOLIATION_INERT
INCOMPLETE_CONTRACT
```

No new host, simulation, hardware, provider action, or paper is warranted
before this exact selection test.

## 11. Exact regression

The local regression is:

- [`du_conservative_certification_feedback_probe.py`](../tests/du_conservative_certification_feedback_probe.py)
- [`du_conservative_certification_feedback_result.json`](../tests/artifacts/du_conservative_certification_feedback_result.json)

It passes `24/24` exact checks. The artifact is regression coverage for the
analytic theorem package and hostile witnesses. It is not independent
scientific evidence.
