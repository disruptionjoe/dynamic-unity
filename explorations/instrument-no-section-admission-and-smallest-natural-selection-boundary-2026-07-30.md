---
title: "Instrument no-section admission and smallest natural-selection boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-159
run_id: RUN-20260730-110700-instrument-no-section-admission
work_id: MPA-01-INSTRUMENT-NO-SECTION-ADMISSION
action_id: MPA-01-INSTRUMENT-NO-SECTION-ADMISSION
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Instrument no-section admission

## Executive return

```text
PARTIAL_SELECTION_FRONTIER
+ KNOWN_RESULT_ABSORPTION
+ OBSERVER_INDEX_EXTERNALLY_SUPPLIED
```

The literal universal no-section conjecture is false. Every channel or
multi-time process admits a natural **trivial** instrument: retain one outcome,
or toss a process-independent coin and attach its label while applying the
original process. This construction respects representation changes and
mixtures, and it composes under product outcome alphabets. Therefore no theorem
can say that a process admits no natural instrument section at all.

The surviving result is narrower and physically more useful:

> A bare quantum process does not universally select an informative,
> nondisturbing, materially formed record interface. On a unitary channel,
> every compatible instrument is only a process-independent coin toss.
> Nonunitary channels can admit nontrivial mathematical decompositions, and
> one covariant Choi-spectral construction is available, but it fails affine
> and compositional selection and still supplies no sampler, actual outcome,
> archive, provenance, access boundary, or observer index.

The component mathematics is known: quantum instruments, Choi extremality,
no-information-without-disturbance, quantum combs/process tensors, and
categorical classical structures absorb it. Dynamic Unity's earned increment
is the exact selection frontier and the correction of `SEED-DU-MPA-02`:

```text
process
  -> formal instrument section
  -> informative instrument
  -> physical sampler
  -> realized outcome
  -> material archive and provenance
  -> observer access and action envelope
```

The first arrow always has trivial solutions. Some processes support
nontrivial solutions. None of that alone closes the later arrows.

## 1. Frozen types

Let \(\mathsf{Chan}(A,B)\) be the finite-dimensional completely positive
trace-preserving maps

\[
\Phi:\mathcal L(\mathcal H_A)\longrightarrow\mathcal L(\mathcal H_B).
\]

For a finite outcome set \(X\), an \(X\)-instrument over \(\Phi\) is a family

\[
\mathcal I=\{\Phi_x\}_{x\in X}
\]

of completely positive, trace-nonincreasing maps satisfying

\[
\sum_{x\in X}\Phi_x=\Phi.
\]

The forgetful map

\[
\Sigma_X:\mathsf{Instr}_X(A,B)\longrightarrow\mathsf{Chan}(A,B)
\]

erases the outcome label and sums the operations. A section assigns an
instrument to every channel:

\[
s_X:\mathsf{Chan}(A,B)\longrightarrow\mathsf{Instr}_X(A,B),
\qquad
\Sigma_Xs_X=\operatorname{id}.
\]

The action tests representation covariance, convex mixtures, and sequential
composition. It does **not** identify an instrument with:

- the physical dilation or monitoring apparatus implementing it;
- a stochastic sampler;
- the sampled outcome of one run;
- a blank-to-written material carrier;
- occurrence and source provenance;
- reset and retention behavior; or
- the observer's access, action, resource, and reliability envelope.

Those are different fibres over the same formal instrument.

## 2. The universal trivial-section theorem

### Proposition 1

For every probability vector \(p=(p_x)_{x\in X}\), the assignment

\[
s_p(\Phi)_x=p_x\Phi
\tag{1}
\]

is a section of \(\Sigma_X\).

### Proof

Each \(p_x\Phi\) is completely positive and trace-nonincreasing, and

\[
\sum_xp_x\Phi=\Phi.
\]

For reversible input/output representation changes \(\alpha,\beta\),

\[
s_p(\beta\Phi\alpha)_x
=\beta\,s_p(\Phi)_x\,\alpha.
\]

For a convex mixture,

\[
s_p(t\Phi+(1-t)\Psi)_x
=t\,s_p(\Phi)_x+(1-t)\,s_p(\Psi)_x.
\]

Sequentially composing \(s_p(\Phi)\) and \(s_q(\Psi)\) gives the product-label
instrument

\[
(x,y)\longmapsto p_xq_y\,\Psi\Phi
=s_{p\otimes q}(\Psi\Phi)_{(x,y)}.
\]

Thus the family is covariant, affine, and compositional when outcome
alphabets compose by product. The singleton case is the simplest section.
The same proof applies to a quantum comb or other multi-time process cone:
the positive components \(p_xW\) obey the same linear normalization
constraints and sum to \(W\). A one-slot channel is also a subcase of any
claimed universal multi-time selector.

### Meaning

Equation (1) attaches a label statistically independent of every process
input. It carries no information about which state, history, interaction, or
source occurred. It is a formal section, not a record-selection mechanism.

This proposition kills the literal reading of an “Instrument No-Section
Theorem.” A viable theorem must include an information, formation, provenance,
or materiality requirement. Merely asking for a section is too weak.

## 3. Exact informative obstruction on unitary channels

### Definition — informative instrument

An instrument is informative on an admitted state family \(\mathcal S\) when
there exist \(\rho,\sigma\in\mathcal S\) and an outcome \(x\) such that

\[
\operatorname{tr}\Phi_x(\rho)
\ne
\operatorname{tr}\Phi_x(\sigma).
\tag{2}
\]

Equivalently, its outcome law is not a process-independent coin toss on
\(\mathcal S\).

### Proposition 2 — unitary refinement obstruction

Let

\[
\Phi_U(\rho)=U\rho U^\dagger
\]

be a unitary channel. Every instrument \(\{\Phi_x\}\) satisfying

\[
\sum_x\Phi_x=\Phi_U
\]

has the form

\[
\Phi_x=p_x\Phi_U
\]

for one probability vector \(p\). It is therefore uninformative on every
input-state family.

### Proof

The Choi operator of a unitary channel is rank one:

\[
J(\Phi_U)=|U\rangle\!\rangle\langle\!\langle U|.
\]

For each completely positive component,

\[
0\le J(\Phi_x)\le J(\Phi_U).
\]

A positive operator dominated by a rank-one positive operator has support in
the same one-dimensional subspace. Hence

\[
J(\Phi_x)=p_xJ(\Phi_U)
\]

with \(p_x\ge0\). Trace preservation of the sum gives \(\sum_xp_x=1\), and
the Choi isomorphism yields \(\Phi_x=p_x\Phi_U\).

### Corollary

No universal assignment over a process class containing unitary channels can
select an informative instrument for every process while leaving the unitary
channel unchanged.

This is the exact smallest quantum obstruction. It does not say that
measurement is impossible. It says that acquiring information requires a
change in the admitted process, an added output/environment, a restricted
commuting state family, or another physical antecedent.

The classical positive control is important. On a supplied classical sample
space, the identity channel can copy a classical label into an outcome while
leaving the original label unchanged. The difference is not “records versus
no records.” It is that classical distinguishability/copyability structure has
already been supplied.

## 4. Covariance alone does not produce a no-section theorem

The hostile result above should not be overgeneralized. A nonunitary channel
can have a canonical-looking instrument decomposition.

Let

\[
J(\Phi)=\sum_{\lambda>0}\lambda P_\lambda
\]

be the spectral-projector decomposition of the Choi operator, grouped by
distinct nonzero eigenvalues. Define completely positive maps
\(\Phi_\lambda\) by

\[
J(\Phi_\lambda)=\lambda P_\lambda.
\tag{3}
\]

Because \(0\le\lambda P_\lambda\le J(\Phi)\), each component is
trace-nonincreasing, and their sum is \(\Phi\). Under unitary input/output
representation changes, the Choi operator and its spectral projectors
transform together. Equation (3) therefore gives a covariant mathematical
instrument.

This construction prevents a false conclusion:

> Symmetry covariance alone does not forbid every nontrivial channel-to-
> instrument rule.

But the construction is not affine. The smallest witness is a state-
preparation channel. The pure output states

\[
\rho_0=|0\rangle\langle0|,
\qquad
\rho_1=|1\rangle\langle1|
\]

each have one nonzero spectral block. Their equal mixture

\[
\frac12(\rho_0+\rho_1)=\frac12I
\]

has one degenerate spectral block when equal eigenvalues are grouped, whereas
mixing the two pure-state instruments retains two preparation-labelled
components. Spectral selection therefore does not commute with convex mixing.
Nor does a spectral decomposition of \(J(\Psi\Phi)\) generally equal the
sequential composition of the spectral decompositions of \(J(\Phi)\) and
\(J(\Psi)\).

Even where (3) is mathematically defined, it supplies no physical reason that
an environment should measure that spectral label, no sampler, and no material
archive. It is a representation-level decomposition.

## 5. Why multi-time structure does not repair selection

Quantum combs and process tensors enlarge an endpoint channel to a complete
operational object indexed by intervention slots. That matters: it prevents a
base-time or endpoint map from masquerading as a complete history.

It does not reverse the typing direction. A comb describes the probabilities
generated **when a tester or sequence of instruments is inserted**. The comb
does not thereby select that tester. Likewise, an operational Markov condition
can quantify memory relative to all admitted interventions without selecting
which apparatus forms, retains, and exposes those interventions and outcomes.

This reproduces, rather than closes, the boundary in `HC-DU-137`:

> Once an action family and physical interface are supplied, a coarsest
> future-response quotient can be canonical. The process does not thereby
> select the physical interface or action family that defines the quotient.

## 6. Classical structure is an antecedent, not a free consequence

Categorical quantum mechanics makes the copyability issue exact. Coecke,
Pavlovic, and Vicary prove that special commutative dagger-Frobenius structures
in finite-dimensional Hilbert spaces correspond to orthonormal bases; their
comultiplication copies exactly the selected basis vectors.

Thus a copying/archive algebra can be formalized without coordinates, but it
is still additional structure. Choosing the Frobenius structure is choosing
which data are classical and copyable. A bare Hilbert space or channel does
not supply one preferred choice.

This gives a useful candidate coordinate for the next selection-frontier
question:

```text
selected classical/copyable algebra
  != selected instrument
  != selected physical sampler
  != selected material archive
```

## 7. Absorber collision

The exact components are mature.

- D'Ariano, Perinotti, and Tosini define tests as collections of operations
  summing to a channel and connect incompatibility to information extraction
  without disturbance:
  [arXiv:2204.07956](https://arxiv.org/abs/2204.07956).
- Heinosaari, Leppäjärvi, and Plávala characterize quantum observables that
  provide no information without disturbance as trivial coin-toss
  observables, while showing the exact statement is theory-class dependent in
  general probabilistic theories:
  [arXiv:1808.07376](https://arxiv.org/abs/1808.07376).
- Coecke, Pavlovic, and Vicary identify copy/delete classical structures with
  orthogonal bases:
  [arXiv:0810.0812](https://arxiv.org/abs/0810.0812).
- Chiribella, D'Ariano, and Perinotti separate quantum combs from the
  transformations and testers applied to them:
  [arXiv:0904.4483](https://arxiv.org/abs/0904.4483).
- Pollock et al. state an operational multi-time Markov condition that accounts
  for all detectable memory effects:
  [arXiv:1801.09811](https://arxiv.org/abs/1801.09811).

Accordingly:

```text
NEW UNIVERSAL QUANTUM NO-SECTION THEOREM: NO
NEW QUANTUM INFORMATION THEOREM: NO
EXACT DU SELECTION-CONTRACT CORRECTION: YES
SCOPED GRADE-4 CLASSIFICATION: YES
NEW PHYSICS OR EMPIRICAL EXCESS: NO
```

## 8. Smallest surviving selection frontier

The action identifies five independently variable coordinates:

1. **Information:** does the outcome law distinguish admitted inputs or
   histories?
2. **Disturbance and process extension:** what system, environment, or output
   changes are admitted to acquire it?
3. **Classical structure:** which observable, copyable algebra, outcome
   alphabet, or coarse graining is physically distinguished?
4. **Material realization:** what coupling, sampler, blank-to-written carrier,
   retention, reset, and provenance path implement the formal instrument?
5. **Observer access:** which actions, resources, reliability contract, and
   horizon make the archive usable?

A later physical-selection theorem must establish constancy of at least one
of these coordinates on a declared antecedent fibre. A no-section theorem
must say which coordinate has no natural section and under which morphisms.
Neither may use the held-out reconstruction target to define its answer.

## 9. Observer-index disposition

```text
OBSERVER_INDEX_EXTERNALLY_SUPPLIED
```

The unitary refinement theorem is observer-independent and needs no observer
index. But the **complete packet asked for by the campaign** includes access,
admissible actions, resources, reliability, and a horizon. None of the formal
sections or obstructions above selects that packet. Calling the observer
irrelevant would therefore answer a smaller question than the one activated.

## 10. Campaign disposition

`SEED-DU-MPA-02` is corrected:

> There is no universal target-blind assignment of an **informative,
> nondisturbing, complete material record packet** to every quantum process.
> The formal forgetful map from instruments to processes does have trivial
> natural sections, and some processes admit nontrivial representation-level
> sections.

The Grade-4 credit is for the exact scoped classification and killed
overstatement, not for novelty in quantum information. Swing 2 is not
executed here. If directly authorized, its information-dense task is now
clear: order the five frontier coordinates by counterfactual necessity and
find the weakest physical antecedent that selects a nontrivial coordinate
without silently supplying the rest.

## Final status

**BANKED SCOPED RESULT / LITERAL UNIVERSAL NO-SECTION CONJECTURE REFUTED /
TRIVIAL NATURAL SECTIONS PROVED / UNITARY INFORMATIVE-REFINEMENT OBSTRUCTION
PROVED / COVARIANT NONAFFINE CHOI-SPECTRAL SECTION CONSTRUCTED / COMPLETE
MATERIAL PACKET AND OBSERVER INDEX UNSELECTED / KNOWN QUANTUM-INFORMATION AND
CATEGORICAL ABSORPTION / NO NEW PHYSICS, PREDICTION, OR PAPER CLAIM /
SWING 2 NOT ACTIVATED.**
