---
title: "Central record-interface selection theorem, formation certificate, and no-go"
status: completed_scoped_result
doc_type: theorem_and_collision_audit
created: 2026-07-24
authority: "Joe direct chat: do another heavy swing"
claim_grade: "EXACT FINITE ABELIAN SPECIALIZATION PLUS MATCHED PAULI CONTROL / KNOWN COMPONENT MATHEMATICS / NEW DU DEPENDENCY RESULT / NO NOVEL-PHYSICS PROMOTION"
run_plan: "../lab/process/runs/RUN-20260724-225324-central-record-interface-selection/run-plan.md"
probe: "../tests/du_central_record_interface_selection_probe.py"
artifact: "../tests/artifacts/du_central_record_interface_selection_result.json"
---

# Central record-interface selection

## Result in plain English

A dynamically stable classical label and coherently accessible environmental
evidence of that label are different things.

In the finite random-unitary class studied here, the dynamics canonically
selects a *center*: the coarsest classical sector labels that commute with all
of the active dynamics. But this alone does not mean that any environment,
observer, or archive can read those labels. A second, access-relative
certificate is required: the complementary environment states associated
with different sectors must be distinguishable under the declared environment
operation algebra.

The sharp positive case is a uniform finite abelian twirl. It does both:

1. it selects the center of the fixed algebra; and
2. its coherently accessible branch environment carries an exactly readable
   character-sector code.

If a sector has internal multiplicity, that internal state remains fully
quantum. The channel records the sector without selecting a basis inside it.
This gives a precise finite picture of one quantum-to-classical interface:

> the dynamics selects only a central sector; whether that sector becomes
> readable depends on the environment access algebra, while the complete
> underlying state can remain quantum.

This is a useful Dynamic Unity dependency result, not a new quantum theorem or
a derivation of the physical channel.

## Frozen class

Let \(G\) be a finite abelian group and let \(U:G\to\mathcal U(\mathcal H)\)
be a finite-dimensional unitary representation. Freeze nonnegative weights
\(w_g\) summing to one and define the Heisenberg channel

\[
\Phi^*(A)=\sum_{g\in G}w_g U_g^\dagger A U_g.
\]

The corresponding explicitly frozen branch-environment isometry is

\[
V|\psi\rangle
  =\sum_{g\in G}\sqrt{w_g}\,U_g|\psi\rangle\otimes|g\rangle_E.
\]

The environment basis is only a dilation coordinate. All record statements
below are expressed through inner products or trace distances and therefore
survive a common environment-unitary change of basis.

Because \(G\) is abelian,

\[
\mathcal H=\bigoplus_{\chi\in\widehat G}\mathbb C^{m_\chi},
\qquad
U_g|_{\chi}=\chi(g)I_{m_\chi},
\]

after omitting unrepresented characters. The principal statement assumes the
positive-weight support generates \(G\). The executable classifier also
handles nongenerating support by merging characters with identical
restrictions to the active support.

## Theorem 1 — fixed-algebra selection

For positive weights on the declared support,

\[
\operatorname{Fix}(\Phi^*)
=\{A:[A,U_g]=0\text{ for every }g\text{ in the support}\}.
\]

If that support generates \(G\), then

\[
\operatorname{Fix}(\Phi^*)
\cong\bigoplus_{\chi\in\widehat G}M_{m_\chi},
\]

and its center is

\[
Z(\operatorname{Fix}(\Phi^*))
\cong\bigoplus_{\chi\in\widehat G}\mathbb C I_{m_\chi}.
\]

Thus the dynamics selects one canonical classical projector \(P_\chi\) per
represented character sector. It does not in general select a complete
classical basis.

### Proof

Equip operators with the Hilbert--Schmidt norm. Every unitary conjugate
\(U_g^\dagger A U_g\) has the same norm as \(A\). If
\(\Phi^*(A)=A\), then the norm of a positive convex combination of those
equal-norm vectors equals their common norm. Strict convexity therefore
forces every positive-weight conjugate to equal \(A\). Hence \(A\) commutes
with each active \(U_g\). The converse is immediate.

For a finite abelian representation, inequivalent characters are distinct
simultaneous eigensectors. The commutant contains every operator within one
multiplicity sector and no operator between distinct character sectors,
giving the direct sum of full matrix blocks. The center of that algebra is
scalar on each block. \(\square\)

This proof is deliberately restricted to random-unitary channels. Fixed
points need not equal a Kraus commutant for arbitrary quantum operations.

## Theorem 2 — environment-formation certificate

For any normalized state \(|\psi_\chi\rangle\) in character sector \(\chi\),
the isometry factors as

\[
V|\psi_\chi\rangle
=|\psi_\chi\rangle\otimes|e_\chi\rangle,
\qquad
|e_\chi\rangle
=\sum_g\sqrt{w_g}\chi(g)|g\rangle.
\]

The environment state is independent of the internal multiplicity state.
For two sectors,

\[
\lambda_{\chi\psi}
=\langle e_\psi|e_\chi\rangle
=\sum_g w_g\,\overline{\psi(g)}\chi(g).
\]

The same \(\lambda_{\chi\psi}\) multiplies system coherence between those
sectors. Since the two conditional environment states are pure, their trace
distance obeys

\[
D_{\chi\psi}^2=1-|\lambda_{\chi\psi}|^2.
\]

Therefore

\[
D_{\chi\psi}^2+|\lambda_{\chi\psi}|^2=1.
\]

For uniform weights on the full group, character orthogonality gives

\[
\lambda_{\chi\psi}=\delta_{\chi\psi}.
\]

The environment then records the center label exactly while learning nothing
about the quantum state inside a multiplicity block.

For \(n\) conditionally independent fragments, the overlap becomes
\(\lambda_{\chi\psi}^n\), so

\[
D_{\chi\psi,n}^2=1-|\lambda_{\chi\psi}|^{2n}.
\]

This is access-relative formation and amplification of one sector label under
the declared coherent environment algebra. It is not yet a stable classical
pointer, redundant public objectivity, authentication, common knowledge, or
Byzantine finality.

### Access-algebra qualification

The word “record” here is explicitly relative to full coherent access to the
branch environment. Every sector state \(|e_\chi\rangle\) has the same
branch-basis population distribution \(w_g\); the sector label resides in
relative phases. If the environment is dephased in the \(|g\rangle\) basis
before decoding, every conditional state becomes

\[
\sum_g w_g|g\rangle\langle g|,
\]

and all sector trace distances collapse to zero.

For the uniform \(\mathbb Z_2^k\) case, the normalized Walsh character
transform maps the coherent environment states exactly to orthogonal label
states:

\[
|e_\chi\rangle\longmapsto|\chi\rangle.
\]

The probe checks both sides: the coherent decoder returns the identity label
kernel, while branch-basis dephasing erases every distinction. Thus the
positive result establishes a perfectly distinguishable quantum sector code
and a concrete route to a readable pointer *if* coherent environment control
is available. It does not establish that such control is natural, cheap,
stable, redundant, or public.

## Corollary — internal-basis nonselection

Suppose \(m_\chi>1\). Every unitary acting only inside the \(\chi\) block
commutes with the channel and leaves \(P_\chi\) fixed. Those same rotations
move rank-one projectors inside the block.

Consequently, no selector that depends only on the frozen channel and is
natural under all channel automorphisms can choose a unique rank-one
resolution inside that sector. Such a choice requires additional dynamics,
an access restriction, a measurement coupling, or another independently
declared structure.

This is the exact place where the finite model keeps quantum state after a
central sector has become coherently readable.

## Why one certificate is insufficient

The hostile controls separate fixedness from formation.

| Dynamics | Fixed algebra | Center | Environment evidence | Verdict |
|---|---:|---:|---:|---|
| identity on a qubit | \(M_2\) | scalars | none | no nontrivial classical label |
| deterministic \(Z\) unitary | diagonal algebra | two sectors | conditional environment states differ only by global phase | fixed center, no formed record |
| biased \(I/Z\) twirl, weights \(3/4,1/4\) | diagonal algebra | two sectors | \(D^2=3/4\) | same center, partial record |
| uniform \(I/Z\) twirl | diagonal algebra | two sectors | \(D=1\) | exact coherently decodable bit |
| uniform collective parity twirl | \(M_2\oplus M_2\) | two sectors | exact parity code | readable parity plus quantum multiplicity |
| uniform \(\mathbb Z_2^2\) twirl | diagonal algebra on four characters | four sectors | exact four-way code | exact coherent four-valued readout |

The decisive counterexample is deterministic \(Z\): it has the same
two-sector fixed center as ordinary dephasing, but its minimal one-dimensional
environment contains no distinguishable record. A fixed or noiseless algebra
is therefore not a record-formation certificate.

## Exact fragility and the approximate successor

Consider the qubit channel

\[
\Phi_\epsilon^*
=\left(\frac12-\epsilon\right)\operatorname{id}
+\frac12\operatorname{Ad}_Z
+\epsilon\operatorname{Ad}_X,
\qquad 0<\epsilon<\frac12.
\]

At \(\epsilon=0\), the exact fixed algebra is the two-dimensional diagonal
algebra. For every positive \(\epsilon\), however small, the active \(X\) and
\(Z\) generate a scalar commutant, so the exact fixed algebra collapses to
\(\mathbb C I\).

This does not mean the record disappears operationally at infinitesimal
\(\epsilon\). In fact the former \(Z\) observable becomes an approximate
fixed point with eigenvalue \(1-2\epsilon\). It means exact algebra selection
is structurally too brittle to be the final physical criterion.

### First approximate finite-time separation

The probe also solves the qubit Pauli benchmark needed to avoid stopping at
that warning. For

\[
\Phi(\rho)=
w_I\rho+w_XX\rho X+w_YY\rho Y+w_ZZ\rho Z,
\]

the Pauli observables are eigenoperators. In particular,

\[
\lambda_Z=w_I-w_X-w_Y+w_Z.
\]

Two \(Z\)-basis inputs retain system trace distance
\(|\lambda_Z|^n\) after \(n\) uses. With equal priors, a final system-only
\(Z\) readout therefore has Helstrom error

\[
p_{\mathrm{sys},n}=\frac{1-|\lambda_Z|^n}{2}.
\]

For the canonical Pauli-branch complement, the environment trace distance
between those same one-use inputs is

\[
D_E=2\left(\sqrt{w_Iw_Z}+\sqrt{w_Xw_Y}\right).
\]

To see this, condition on a \(Z\)-basis input. The \(I/Z\) branches occupy one
common system-output sector and the \(X/Y\) branches the orthogonal flipped
sector. In each environment block the two conditional rank-one operators
differ only in the sign of their off-diagonal term, contributing
\(2\sqrt{w_Iw_Z}\) and \(2\sqrt{w_Xw_Y}\) respectively to the half trace
norm. Orthogonality of the blocks makes the contributions add.

The probe constructs three channels with:

- the same scalar exact fixed algebra;
- the same \(|\lambda_Z|=3/4\);
- the same one-use system error \(1/8\); and
- the same four-use signal \(81/256\);

but with

\[
D_E^2\in\left\{0,\frac34,1\right\}.
\]

Thus even after exact fixed points are replaced by a finite-time stability
score, the score and exact fixed-algebra type do not determine whether the
accessible complement forms no record, a partial record, or a perfect record.
Conversely, the perfect-environment member has no exact nontrivial fixed
algebra. Approximate stability and environment formation are operationally
separate axes.

### Theorem 3 — Pauli stability--formation rectangle

The trio is not exceptional. Fix any desired one-use \(Z\)-stability
\(s\in(0,1)\) and any environment distinguishability \(d\in[0,1]\). Set

\[
a=\frac{1+s}{2},\qquad b=\frac{1-s}{2},\qquad
r=\frac{1-\sqrt{1-d^2}}{2},
\]

and choose

\[
(w_I,w_X,w_Y,w_Z)
=\bigl(ar,br,b(1-r),a(1-r)\bigr).
\]

Then

\[
\lambda_Z=(w_I+w_Z)-(w_X+w_Y)=a-b=s
\]

and

\[
D_E
=2(a+b)\sqrt{r(1-r)}
=2\sqrt{r(1-r)}
=d.
\]

For \(d=0\), the active \(Y\) and \(Z\) branches already have scalar
commutant. For \(0<d\leq1\), at least two noncommuting Pauli branches remain
active, so the fixed algebra is also scalar. Therefore:

> For every \(0<s<1\), the full environment-record interval
> \(0\leq D_E\leq1\) is attainable by qubit Pauli channels with the same
> scalar exact fixed algebra and the same one-use \(Z\)-stability \(s\).

At any fixed horizon \(n\), the system-only stability is \(s^n\), so the same
full formation interval remains available. The probe checks the constructive
rectangle exactly on three stability values and four split values.

The rectangle uses the full coherent complementary algebra. Under
branch-diagonal access, every member instead has \(D_E=0\), because Pauli
branch probabilities are input-independent. This already identifies access
algebra as load-bearing, but the all-or-nothing restriction does not yet
derive a stable classical pointer or a useful intermediate physical bound.

This rules out any nontrivial universal law of the form
\(D_E=f(s)\), or a one-sided bound sharper than \(0\leq D_E\leq1\), from
fixed-algebra type and one approximate stability coordinate alone. In the
construction, stability depends only on the total no-flip versus flip weight
\((a,b)\), whereas formation depends on how each total is coherently split
between branch alternatives with the same system output.

This is still a finite Pauli-channel specialization. A physically useful
successor must add independently justified structure that can shrink the
rectangle. It should freeze:

- an operational time horizon;
- an approximation tolerance;
- a spectral or mixing gap;
- environment distinguishability and access;
- locality and resource constraints; and
- an adversarial perturbation class.

It should determine whether nondemolition structure, full-channel disturbance,
locality, energy, access, or another charged condition creates a nontrivial
stability--formation bound without fitting the condition or basis after seeing
the result.

## Naturality and gauge controls

A rational orthogonal conjugation

\[
W=\begin{pmatrix}3/5&4/5\\-4/5&3/5\end{pmatrix}
\]

maps \(Z\), its selected projectors, and the entire channel into a rotated
coordinate description. The exact fixed dimension remains two and the
rotated projectors remain fixed. The selection is therefore relative to the
physical channel, not to the computational coordinates used by the probe.

A common permutation of environment branches preserves the complete Gram
matrix \(\langle e_\psi|e_\chi\rangle\), hence all conditional trace
distances. The environment record is not an artifact of a branch-name
convention.

## What this changes for Dynamic Unity

### A sharper interface object

The minimum useful record-interface object in this class is not just an
algebra. It is the pair

\[
\left(
  Z(\operatorname{Fix}(\Phi^*)),
  \{\rho^E_\chi\}_{\chi}
\right),
\]

with two separately checked receipts:

1. a **selection/stability receipt** for the exact center or a declared
   finite-time approximate observable; and
2. a **formation/access receipt** naming the environment operation algebra
   under which its conditional states are distinguishable.

Calling the first receipt a record silently assumes the second. Calling the
second receipt classical without the first may merely identify transient
state discrimination. Calling coherent complementary evidence a classical
record without freezing its decoder and dephasing tolerance is also an
interface refit.

### The quantum-to-classical capability boundary

In the collective-parity fixture, an observer with access to the environment
can identify parity without resolving or destroying the internal
two-dimensional state inside either parity sector. Access therefore enlarges
the observer's executable task set only for the central label. It does not
provide arbitrary access to the full quantum state.

This is the exact finite version of the architectural intuition that a
leaderless or metastable substrate may retain rich local state while a
hardening layer exposes only a smaller certified fact. The analogy is useful
at the typed level—center label, witness, access, and task—but it supplies no
physical identity between quantum channels and distributed consensus.

### Clock-QCA correction

The source Clock-QCA evolution by itself has no nontrivial complementary
environment that forms an elapsed-record label. Conserved or fixed
observables of the source unitary do not repair that absence. The earlier
pointer/archive construction supplied the missing coupling and environment,
and this result now states exactly what that addition must certify:

- which central sector the added channel stabilizes; and
- whether its complement actually carries distinguishable evidence.

Thus the Clock-QCA result remains:

> source covariance admits record couplings; it does not select or form one.

The current theorem classifies what a successful added interface would look
like. It does not derive that interface from the source law.

## Measurable tests exposed by the theorem

These are benchmark predictions of the declared channel class, not proposed
new physics.

1. **Across-sector versus within-sector tomography.** Prepare two states from
   different character sectors and two orthogonal states inside one
   multiplicity sector. The environment should distinguish the first pair
   according to \(D_{\chi\psi}\) and be identical for the second pair.
2. **Bias sweep.** Change only the random-unitary weights. The exact fixed
   center remains unchanged while environment distinguishability follows the
   Fourier coefficient
   \(\sum_gw_g\overline{\psi(g)}\chi(g)\).
3. **Fragment amplification.** With independent fragments, the squared trace
   distance should follow \(1-|\lambda|^{2n}\). For the biased qubit example
   with \(|\lambda|=1/2\), four fragments are the minimum needed to exceed
   \(D^2=0.99\).
4. **Noncommuting leakage.** Add a small \(X\) branch to a \(Z\)-record
   channel. The exact center disappears at any nonzero rate, while the
   finite-time \(Z\) memory decays continuously with factor
   \(1-2\epsilon\) per application.
5. **Coordinate control.** Conjugate the complete preparation, channel, and
   readout together. All sector dimensions and distinguishabilities should
   remain invariant while the projector matrices rotate.
6. **Matched-stability/complement sweep.** Hold the scalar fixed-algebra type
   and \(|\lambda_Z|\) fixed across the three Pauli fixtures. Environment
   tomography must still return \(D_E^2=0,3/4,1\). This is the falsifier for
   collapsing approximate stability and formation into one number.
7. **Rectangle sweep.** Choose any fixed \(0<s<1\), vary
   \(r\in[0,1/2]\) in the constructive Pauli family, and verify that the
   system signal remains \(s^n\) while \(D_E=2\sqrt{r(1-r)}\) spans the full
   unit interval.
8. **Access-algebra switch.** Hold the uniform twirl and environment state
   fixed. Coherent Walsh decoding must identify the sector perfectly;
   branch-basis dephasing before the same decoder must reduce the sector
   distinguishability to zero.

## Prior-art collision audit

The broad mathematics is occupied:

| Component | Strong collision | Disposition |
|---|---|---|
| preserved information as fixed-point/matrix-algebra structure; noiseless subsystems and pointer bases | Blume-Kohout, Ng, Poulin, and Viola, [*The structure of preserved information in quantum processes*](https://arxiv.org/abs/0705.4282) and [*Information preserving structures*](https://arxiv.org/abs/1006.1358) | known terrain |
| hybrid classical/quantum information carried by operator algebras | Bény, Kempf, and Kribs, [*Quantum Error Correction of Observables*](https://arxiv.org/abs/0705.1574) | known terrain |
| correctable/private operator algebras and complementary-channel structure | Kribs et al., [*Quantum Complementarity and Operator Structures*](https://arxiv.org/abs/1811.10425) | known terrain |
| environment monitoring and pointer selection in decoherence | Schlosshauer, [*Quantum Decoherence*](https://arxiv.org/abs/1911.06282) | known terrain |
| uniqueness conditions for observables leaving redundant environmental imprints | Fu, [*Uniqueness of the Observable Leaving Redundant Imprints...*](https://arxiv.org/abs/2010.14131) | known terrain; stronger objectivity claims require its conditions |
| classicality and broadcasting limits | Barnum et al., [*A generalized no-broadcasting theorem*](https://arxiv.org/abs/0707.0620); Piani, Horodecki, and Horodecki, [*No-local-broadcasting theorem for quantum correlations*](https://arxiv.org/abs/0707.0848) | blocks promotion from one environment record to public classicality |
| fixed point versus operation-element commutant | Arias, Gheondea, and Gudder, [*Fixed points of quantum operations*](https://doi.org/10.1063/1.1519669) | warns against generalizing the random-unitary proof to arbitrary channels |
| fixed-point algebras and mixed-unitary constructions | Kribs et al., [*Operator Algebra Generalization of a Theorem of Watrous and Mixed Unitary Quantum Channels*](https://arxiv.org/abs/2306.04077) | contemporary direct collision |

Finite-group character orthogonality and the block decomposition are standard
representation theory. The exact complementarity formula is a pure-state
distinguishability specialization. None is presented as novel.

The defensible contribution of this swing is programmatic and architectural:
it closes one finite subcase of the exogenous-interface question, proves that
fixed-algebra selection and environment formation are logically independent,
adds a matched finite-time counterexample after exactness fails, and
solves the full qubit Pauli stability--formation rectangle. It thereby moves
the next failure point to the additional physical conditions required to
shrink that rectangle. That is substantial progress for `HC-DU-033`, but not
a standalone publication claim at the present grade.

## Disposition

This swing returns:

```text
FINITE ABELIAN CENTRAL-RECORD INTERFACE CLASSIFIED
FIXED CENTER != FORMED RECORD
UNIFORM FULL-GROUP TWIRL SELECTS THE CENTER AND CARRIES A COHERENTLY READABLE SECTOR CODE
QUANTUM MULTIPLICITY SURVIVES INSIDE COHERENTLY READABLE CENTRAL SECTORS
FINER INTERNAL BASIS UNSELECTED
BRANCH-BASIS DEPHASING ERASES THE SECTOR CODE BEFORE DECODING
EXACT CENTER STRUCTURALLY FRAGILE TO NONCOMMUTING PERTURBATIONS
MATCHED APPROXIMATE STABILITY DOES NOT DETERMINE ENVIRONMENT FORMATION
FULL QUBIT PAULI STABILITY--FORMATION RECTANGLE CONSTRUCTED
COMPONENT MATHEMATICS KNOWN
PHYSICAL CHANNEL, CUT, OBSERVER, PUBLIC FINALITY, TIME, GEOMETRY AND ONTOLOGY OPEN
```

No claim, prediction, ontology, or paper seed is promoted. The immediate
foundational successor is to identify the minimal independently justified
physical condition—nondemolition structure, full-channel disturbance,
locality, energy, access, or a charged resource—that shrinks the Pauli
rectangle and supports a nontrivial bound. A physical implementation should
be attempted only when the channel and accessible complement arise from an
independently motivated instrument rather than a fitted dephasing model.

## Reproducibility

`tests/du_central_record_interface_selection_probe.py` passes `33/33` exact
checks and writes
`tests/artifacts/du_central_record_interface_selection_result.json`.
