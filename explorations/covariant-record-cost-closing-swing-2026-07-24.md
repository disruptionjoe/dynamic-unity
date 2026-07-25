---
title: "Covariant records are not free: an exact noisy record–disturbance–support package"
status: completed_closing_swing
doc_type: technical_research_note_spine
created: 2026-07-24
paper_candidate: DU-PAPER-003
predecessor: explorations/covariant-archive-boundary-swing-2026-07-24.md
claim_grade: "EXACT SCOPED MATHEMATICAL THEOREMS / KNOWN COMPONENT STRUCTURE / CLOCK-QCA CONJUNCTION SEARCH-INCOMPLETE"
publication_verdict: NARROW
banked: false
seeded: false
---

# Covariant records are not free

## Bottom line

The `HC-DU-031B/C` exact pure-pointer equality has a clean, tight mixed/noisy
extension and a support consequence:

1. A binary controlled nondemolition recorder with one
   source-independent blank environment obeys

   \[
   D_R^2\leq 4\delta(1-\delta),
   \qquad
   \delta=\frac{1-|\gamma|}{2}.
   \]

   Here \(D_R\) is half trace distance between the two accessible record
   states, \(\gamma\) is the surviving source coherence, and \(\delta\) is
   half diamond distance between the induced dephasing channel and its
   phase-aligned unitary target.

2. If the two conditional accessible record states factor over \(m\)
   independently accessible fragments, with local distinguishabilities
   \(D_k\), then

   \[
   \delta\geq
   \frac{1-\prod_{k=1}^m\sqrt{1-D_k^2}}{2}.
   \]

   If every fragment has \(D_k\geq d\), then

   \[
   \delta\geq\frac{1-(1-d^2)^{m/2}}{2}.
   \]

3. Independently of the source-coherence calculation, a \(K\)-dimensional
   archive that decodes one of \(N\) uniformly distributed histories with
   average error \(p\) obeys the noisy support bound

   \[
   \log_2 K\geq
   \log_2N-h_2(p)-p\log_2(N-1).
   \]

The first two bounds are tight. They survive mixed blank states and arbitrary
noisy archive postprocessing. The product bound does **not** survive
correlated fanout; the executable gives an exact counterexample. The entire
record–disturbance bound fails if the “blank” environment was already
correlated with the history; a fixed-oracle counterexample makes that
assumption explicit.

These are useful closing results, but the honest paper verdict is:

```text
NARROW
```

The binary curve is an exact controlled-recorder specialization of established
visibility/distinguishability and channel information–disturbance structure.
The fragment and support statements are direct fidelity-multiplicativity and
Holevo–Fano consequences. The possible paper contribution is consequently
the **conjunction** with the exact Clock-QCA covariant construction,
inert-ancilla nonselection theorem, archive-operation taxonomy, and graded
boundary result—not a newly discovered universal information law.

## 1. Frozen contract and norm conventions

### 1.1 Source history sector

Let the source history sector be

\[
\mathcal H_H=\operatorname{span}\{|0\rangle,|1\rangle\}.
\]

Let \(E\) begin in one density operator \(\sigma_E\), independent of the
source history. It may be mixed. A controlled nondemolition interaction is

\[
W
=|0\rangle\!\langle0|\otimes U_0
+|1\rangle\!\langle1|\otimes U_1,
\]

where \(U_0,U_1\) are unitaries on \(E\). “Nondemolition” means that the
declared history populations are retained while the environment can acquire
history information. It does not mean that source coherences are unchanged.

After the interaction, an arbitrary fixed quantum channel
\(\Lambda:E\rightarrow R\) represents loss, noise, compression, export, or
restricted archive access. The two accessible record states are

\[
\omega_i
=\Lambda\!\left(U_i\sigma_EU_i^\dagger\right).
\]

The theorem does not allow:

- a different \(\sigma_E\) for each source history;
- an initially source-correlated oracle;
- a history-dependent side channel outside \(W\);
- a decoder or archive map refit per tested history; or
- an interface chosen after seeing the outcome.

Those exclusions are load-bearing, not housekeeping.

### 1.2 Conventions

State distinguishability is

\[
D(\rho,\tau)=\frac12\|\rho-\tau\|_1.
\]

Channel distance is

\[
\delta_\diamond(\Phi,\Psi)
=\frac12\|\Phi-\Psi\|_\diamond.
\]

Fidelity is the **root fidelity**

\[
F(\rho,\tau)
=\left\|\sqrt{\rho}\sqrt{\tau}\right\|_1,
\]

not its square. With this convention,

\[
D(\rho,\tau)\leq\sqrt{1-F(\rho,\tau)^2}.
\]

The equal-prior optimal binary discrimination success is

\[
P_{\rm succ}=\frac{1+D}{2}.
\]

## 2. Exact mixed/noisy binary theorem

### Theorem 1 — noisy controlled-record tradeoff

Define the source coherence multiplier

\[
\gamma
=\operatorname{Tr}\!\left(U_0\sigma_EU_1^\dagger\right),
\qquad
v=|\gamma|.
\]

Tracing the environment maps the source density matrix as

\[
\begin{pmatrix}
\rho_{00}&\rho_{01}\\
\rho_{10}&\rho_{11}
\end{pmatrix}
\longmapsto
\begin{pmatrix}
\rho_{00}&\gamma\rho_{01}\\
\gamma^*\rho_{10}&\rho_{11}
\end{pmatrix}.
\]

Let

\[
\delta=\frac{1-v}{2}.
\]

Equivalently, \(\delta\) is half diamond distance between this source channel
and the diagonal unitary channel with the same known phase as \(\gamma\).
For the `HC-DU-031C` Clock-QCA pointer fixture,
\(\gamma=\cos\theta\geq0\), so the target is the already frozen identity
channel and no phase refit occurs.

For every fixed archive channel \(\Lambda\),

\[
\boxed{
D(\omega_0,\omega_1)^2\leq4\delta(1-\delta).
}
\]

Equivalently,

\[
D(\omega_0,\omega_1)\leq\sqrt{1-v^2},
\]

and an observed record of distinguishability \(D_R\) requires

\[
\boxed{
\delta\geq
\frac{1-\sqrt{1-D_R^2}}{2}.
}
\]

### Proof

Choose a purification \(|\Sigma\rangle_{EF}\) of \(\sigma_E\). Then

\[
(U_i\otimes I_F)|\Sigma\rangle
\]

is a purification of

\[
\rho_i^E=U_i\sigma_EU_i^\dagger.
\]

The absolute overlap of these two particular purifications is \(v\).
Uhlmann’s theorem maximizes over purifications, hence

\[
v\leq F(\rho_0^E,\rho_1^E).
\]

Fidelity is monotone upward under a quantum channel, so

\[
F(\rho_0^E,\rho_1^E)
\leq F(\omega_0,\omega_1).
\]

The upper Fuchs–van de Graaf inequality gives

\[
D(\omega_0,\omega_1)
\leq\sqrt{1-F(\omega_0,\omega_1)^2}
\leq\sqrt{1-v^2}.
\]

Substituting \(v=1-2\delta\) yields

\[
1-v^2
=1-(1-2\delta)^2
=4\delta(1-\delta).
\]

It remains to justify the channel-distance interpretation of \(\delta\).
After the known diagonal phase is equalized, the source channel is the qubit
dephasing channel

\[
\mathcal N_v(\rho)
=\frac{1+v}{2}\rho
+\frac{1-v}{2}Z\rho Z.
\]

Set \(q=(1-v)/2\). Convexity gives

\[
\frac12\|\mathcal N_v-\mathrm{id}\|_\diamond\leq q,
\]

because half diamond distance between the identity and \(Z\)-unitary channel
is one. The input \(|+\rangle\) attains \(q\): its output is the mixture
\((1-q)|+\rangle\langle+|+q|-\rangle\langle-|\), at trace distance \(q\)
from \(|+\rangle\langle+|\). Thus

\[
\frac12\|\mathcal N_v-\mathrm{id}\|_\diamond
=q=\frac{1-v}{2}=\delta.
\]

This proves the claim. \(\square\)

### Tightness

Take a pure blank environment and

\[
|r_0\rangle=|0\rangle,\qquad
|r_1\rangle
=\cos\theta|0\rangle+\sin\theta|1\rangle.
\]

With no archive noise,

\[
v=|\cos\theta|,
\qquad
D_R=|\sin\theta|,
\qquad
D_R^2=4\delta(1-\delta).
\]

The executable checks 33 angles from \(0\) through \(\pi/2\), with maximum
equality error below \(3\times10^{-10}\).

### Operational form

If binary record error is

\[
p_e=\frac{1-D_R}{2},
\]

then

\[
\delta\geq
\frac12-\sqrt{p_e(1-p_e)}.
\]

At the endpoints:

| Accessible record | \(D_R\) | Required \(\delta\) |
|---|---:|---:|
| uninformative | \(0\) | \(0\) |
| perfect binary record | \(1\) | \(1/2\) |

The maximum \(\delta=1/2\) here is not the maximum distance between arbitrary
channels. It is the maximum distance reached within the frozen
population-preserving dephasing family.

## 3. Independent-fragment theorem

The previous theorem prices one accessible record state. Public or redundant
records require another distinction: are the fragments conditionally
independent, or are they correlated shares of one record?

### Theorem 2 — independent redundancy budget

Under the hypotheses of Theorem 1, suppose the two accessible conditional
record states factor over the declared archive fragments:

\[
\omega_i
=\bigotimes_{k=1}^m\omega_i^{(k)}.
\]

Define

\[
D_k=D\!\left(\omega_0^{(k)},\omega_1^{(k)}\right).
\]

Then

\[
\boxed{
\delta\geq
\frac{1-\prod_{k=1}^m\sqrt{1-D_k^2}}{2}.
}
\]

If every fragment satisfies \(D_k\geq d>0\), then

\[
\boxed{
\delta\geq
\frac{1-(1-d^2)^{m/2}}{2}.
}
\]

For a source-disturbance ceiling
\(\delta\leq\bar\delta<1/2\), the number of such fragments is bounded by

\[
\boxed{
m
\leq
\frac{2\ln(1-2\bar\delta)}
{\ln(1-d^2)}.
}
\]

Both logarithms are negative, so the ratio is positive.

### Proof

Theorem 1’s purification argument and fidelity monotonicity give

\[
v\leq F(\omega_0,\omega_1).
\]

Root fidelity is multiplicative on tensor products:

\[
F(\omega_0,\omega_1)
=\prod_{k=1}^m
F\!\left(\omega_0^{(k)},\omega_1^{(k)}\right).
\]

For each fragment, Fuchs–van de Graaf implies

\[
F\!\left(\omega_0^{(k)},\omega_1^{(k)}\right)
\leq\sqrt{1-D_k^2}.
\]

Therefore

\[
1-2\delta=v
\leq\prod_{k=1}^m\sqrt{1-D_k^2}.
\]

Rearrangement proves the first result. Substituting \(D_k\geq d\) proves the
uniform result. Solving the uniform result for \(m\) proves the final bound.
\(\square\)

### Tightness and support

For each fragment choose pure conditional states with overlap

\[
\langle r_0^{(k)}|r_1^{(k)}\rangle
=\sqrt{1-D_k^2}.
\]

The conditional product construction has

\[
v=\prod_k\sqrt{1-D_k^2}
\]

and saturates the theorem.

If the \(m\) fragments are genuinely disjoint tensor factors and each has
\(D_k>0\), each factor has Hilbert-space dimension at least two. The declared
archive support therefore has

\[
\dim\mathcal H_R\geq2^m.
\]

This is a support/rank statement. It is **not** an energy, entropy, latency,
work, or spacetime-volume law. A physical cost law needs an autonomous
emission/interface model and resource Hamiltonian.

## 4. General noisy archive-dimension bound

The independent-fragment theorem concerns redundant access to one binary
distinction. A different archive task is to recover one of many possible
histories or counts.

### Theorem 3 — Holevo–Fano record-support bound

Let \(X\) be uniform on \(N\) histories. Let \(\{\rho_x\}\) be their record
states on a \(K\)-dimensional archive. Freeze one POVM and decoder producing
\(\widehat X\), and suppose

\[
\Pr[\widehat X\neq X]\leq p.
\]

Then

\[
\boxed{
\log_2 K
\geq
\log_2N-h_2(p)-p\log_2(N-1).
}
\]

If the archive consists of \(m\) cells of local dimension at most \(q\),
then

\[
m\geq
\frac{
\log_2N-h_2(p)-p\log_2(N-1)
}{\log_2q}.
\]

### Proof

Fano’s inequality gives

\[
H(X|\widehat X)
\leq h_2(p)+p\log_2(N-1).
\]

Because \(X\) is uniform,

\[
I(X:\widehat X)
\geq
\log_2N-h_2(p)-p\log_2(N-1).
\]

The Holevo bound gives

\[
I(X:\widehat X)\leq\chi(\{1/N,\rho_x\}).
\]

Finally,

\[
\chi\leq S\!\left(\frac1N\sum_x\rho_x\right)
\leq\log_2K.
\]

Combining the inequalities proves the result. \(\square\)

### What this does and does not price

- Perfectly distinguishing elapsed counts \(0,\ldots,T\) has \(N=T+1\), so
  \(K\geq T+1\). A compact binary counter needs at least
  \(\lceil\log_2(T+1)\rceil\) qubits.
- Perfectly distinguishing every binary event history of length \(T\) has
  \(N=2^T\), so \(K\geq2^T\), or at least \(T\) qubits.
- A unary append-only spatial archive can cost \(T\) cells even for elapsed
  count, but append-only locality is an additional physical constraint, not a
  consequence of the dimension theorem.
- The theorem uses one declared prior and one fixed decoder. A concentrated
  prior, per-target decoder refit, or a weaker task changes the bound.

The executable’s exact endpoints include:

| Task | \(N\) | \(p\) | Lower-bound bits | Binary cells |
|---|---:|---:|---:|---:|
| elapsed labels | \(257\) | \(0\) | \(8.0056\) | \(9\) |
| elapsed labels | \(257\) | \(0.01\) | \(7.8448\) | \(8\) |
| arbitrary 32-bit histories | \(2^{32}\) | \(0\) | \(32\) | \(32\) |
| arbitrary 32-bit histories | \(2^{32}\) | \(0.01\) | \(31.5992\) | \(32\) |

## 5. Exact counterexamples and necessity of assumptions

### 5.1 Correlated fanout defeats the product inference

Start with the `HC-DU-031C` conditional pointer states

\[
|a_0\rangle=|0\rangle,\qquad
|a_1\rangle
=\cos\theta|0\rangle+\sin\theta|1\rangle,
\]

then CNOT-fan out the pointer basis to \(m\) blank cells and lose the pointer.
The archive states are

\[
\omega_0=|0\cdots0\rangle\langle0\cdots0|,
\]

\[
\omega_1
=\cos^2\theta|0\cdots0\rangle\langle0\cdots0|
+\sin^2\theta|1\cdots1\rangle\langle1\cdots1|.
\]

Each individual fragment has

\[
D_k=\sin^2\theta,
\]

but the joint state is correlated, not
\(\bigotimes_k\omega_i^{(k)}\).

At \(\theta=\pi/3\) and \(m=3\):

\[
\delta=0.25,\qquad D_k=0.75.
\]

Incorrectly applying the product formula would demand

\[
\delta\geq0.355310475\ldots,
\]

which is false. This does not refute Theorem 2; it kills the attempt to infer
independent evidence from local accessibility alone. Repeated CNOT fanout is
correlated redundancy, not fresh independent recording.

The base Theorem 1 remains valid:

\[
D_R=0.75
<\sqrt{1-0.5^2}
=0.866025\ldots.
\]

### 5.2 A pre-correlated oracle defeats the blank-record inference

Suppose an environment already contains a perfectly distinguishable history
label before the tested interaction. Let the source do nothing. Then one can
have

\[
\delta=0,\qquad D_R=1.
\]

This violates the displayed curve if it is falsely treated as fresh recording.
It is outside Theorem 1 because there is no single source-independent blank
\(\sigma_E\).

This is the physical version of the fixed-oracle control: “the source was
fixed beforehand” is not enough. One must exclude a source already
pre-correlated with the complete history being read.

### 5.3 Reversible erasure is not thermodynamic payment

A joint unitary can return the archive evidence to the source and restore the
coherence if it erases the accessible record at the same time. The theorem
prices simultaneous accessible information and source coherence. It does not
derive irreversible work, heat, entropy production, or a time arrow.

### 5.4 Large support is not evidence

An arbitrarily large archive can carry identical states for all histories.
Dimension is a capacity constraint, not a certificate that the capacity was
used, accessed, authenticated, or finalized.

## 6. Clock-QCA corollary

The `HC-DU-031B/C` host supplies one exact nontrivial specimen:

1. the `q`-transparent pointer lift is a complete finite local unitary;
2. the canonical rectangular-patch Clock-QCA covariance square closes;
3. a one-gate two-history sector has
   \(\gamma=\cos\theta\geq0\);
4. the frozen source target is therefore the identity channel, with
   \[
   \delta_\diamond
   =\frac12\|\mathcal N_{\cos\theta}-\mathrm{id}\|_\diamond
   =\frac{1-\cos\theta}{2};
   \]
5. the pure pointer saturates Theorem 1;
6. \(m\) fresh product cells saturate Theorem 2; and
7. CNOT fanout supplies the exact correlated counterexample.

The covariance theorem and the record-cost theorem constrain different
things:

- source-sense covariance **admits** the pointer interaction;
- inert-ancilla closure proves that it does not **select** the interaction;
- Theorems 1–3 price the information produced once a controlled interface and
  task are frozen; and
- none of those theorems dynamically selects the pointer basis, archive
  boundary, emission law, or resource Hamiltonian.

There is no covariance loophole in the information bound, but there is also
no information-theoretic derivation of the covariant recorder law.

## 7. Relation to known results

### Englert complementarity

For the pure two-path endpoint, Theorem 1 is exactly the established
visibility/which-way relation:

\[
V^2+D^2=1.
\]

Mixed records and noisy access yield the inequality. This curve is not a
novelty claim.

### KSW continuity and information–disturbance

Kretschmann–Schlingemann–Werner establish general continuity and
information–disturbance relations between a channel and complementary
environment channels. Their general conclusion has square-root continuity:
a channel close to a unitary has a complement close to constant.

Theorem 1 is narrower and sharper only because the controlled nondemolition
binary structure freezes the complete source channel to one dephasing
parameter:

\[
D_R\leq2\sqrt{\delta(1-\delta)}
=2\sqrt{\delta}+O(\delta^{3/2}),
\]

or

\[
\delta\geq\frac{D_R^2}{4}+O(D_R^4).
\]

It supplies an exact tight curve and explicit norm convention for this class.
It does not supersede the general KSW theorem.

### Holevo, Fano, and environmental-record work

The archive-dimension theorem is the standard Holevo–Fano communication
bound applied to a history archive. The independent-fragment result is a
direct root-fidelity product corollary. Environmental redundancy,
objectivity, and spectrum-broadcast structure contain much more developed
record-proliferation machinery. Dynamic Unity must not present these
components as new.

The literature question that remains is whether the **combined**
Clock-QCA package has a paper-distinct theorem:

```text
exact source covariance
+ arbitrary-active-sector nonselection
+ controlled-recorder quantitative cost
+ correlated-versus-independent archive taxonomy
+ finite noisy support bound
+ graded boundary relocation.
```

## 8. Finite falsifiers

The claims are mathematically killable by any finite instance of the
following form:

| ID | Finite falsifier |
|---|---|
| `CR-COST-F1` | A binary controlled unitary with one source-independent \(\sigma_E\) and fixed archive channel has \(D_R^2>4\delta(1-\delta)\). |
| `CR-COST-F2` | A conditionally product accessible record has \(\delta<[1-\prod_k\sqrt{1-D_k^2}]/2\). |
| `CR-COST-F3` | A fixed decoder on a \(K\)-dimensional archive beats the Holevo–Fano dimension bound for the declared uniform ensemble. |
| `CR-COST-F4` | The Clock-QCA pointer fixture has a half-diamond distance other than \((1-\cos\theta)/2\) under the frozen identity target. |
| `CR-COST-F5` | A pure product recorder fails to saturate either of the first two bounds. |

The following findings would **not** falsify the theorems; they would show an
assumption was not physically satisfied:

- a pre-correlated oracle with \(\delta=0,D_R=1\);
- a correlated GHZ/CNOT archive violating the independent product formula;
- a per-instance decoder that changes the task;
- a source interaction that changes history populations; or
- an archive whose record arrives through an undeclared side channel.

## 9. Executable receipt

The deterministic probe is:

```text
tests/du_covariant_record_cost_closing_probe.py
```

Its artifact is:

```text
tests/artifacts/du_covariant_record_cost_closing_result.json
```

It checks:

- 96 mixed-environment, random-unitary, noisy-access cases;
- exact fidelity and data-processing inequalities;
- the \(|+\rangle\) half-diamond witness;
- 33 tight pure-pointer angles;
- three tight product-fragment families;
- four uniform redundancy budgets;
- the correlated three-fragment fanout counterexample;
- the pre-correlated-oracle counterexample;
- perfect and noisy support-bound examples; and
- the useless random-guess endpoint.

Result:

```text
12/12 checks passed
```

The executable is a regression and falsifier search over finite fixtures. The
proofs above, not the sample count, carry the mathematical warrant.

## 10. Publication decision

### What advanced

`DU-PAPER-003` now has:

- an explicit half-diamond norm convention;
- a tight mixed/noisy binary theorem;
- an exact inverse disturbance lower bound from accessible record quality;
- a tight independent-fragment/redundancy budget;
- a noisy support/rank lower bound;
- exact counterexamples marking the independence and blank-source boundaries;
- a direct KSW comparison; and
- deterministic evidence.

### What did not advance

This swing did not:

- naturalize the archive interface;
- select a recorder law from covariance;
- derive an irreversible or thermodynamic archive cost;
- establish a universal record law;
- produce continuum Lorentz covariance;
- identify an observer or proper time; or
- prove that the combined package is literature-distinct.

### Verdict

```text
NARROW
```

The exact curve alone is absorbed by known complementarity and general
information–disturbance theory. The product and support consequences are
useful and paper-shaping, but their ingredients are established. A defensible
manuscript must center the Clock-QCA-specific
construction/nonselection/quantitative-cost conjunction and must survive the
independent primary-literature collision.

Upgrade to `GO` only if that collision finds no prior package with the same
conjunction or if a further locality/covariance theorem makes one of the
support bounds genuinely stronger than generic quantum information.

Downgrade to `PIVOT` if reversible/history QCA or covariant-channel literature
already contains:

1. the same `q`-transparent active-sector closure/nonselection result;
2. the same finite pointer/archive construction; and
3. the same operational cost and boundary classification.

No claim is banked and no paper is promoted by this note.
