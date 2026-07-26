---
title: "CFS self-adjointization ambiguity and representation-robust selection"
status: "exact finite cross-repository no-go application; 10/10 attribution control; no physical promotion"
doc_type: exploration
created: 2026-07-26
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_6
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-MODEL
---

# CFS self-adjointization ambiguity and DU attribution

## Plain-English result

The follow-up swing successfully built a finite causal-action comparison of
the two GU branches. One natural representation made the action choose the
stable branch.

That still was not enough.

Another representation preserved all the information, obeyed the same
symmetry and trace rules, and used the same causal action—but made the action
choose the pathological branch.

For Dynamic Unity, this establishes a reusable rule:

> A physical action does not earn selection credit until its verdict is
> robust across the admitted faithful representations, or physical dynamics
> independently selects one representation.

The result is stronger than W245's missing-contract stop: the contract can be
completed mathematically and still fail to identify a physical selector.

## 1. The exact rival class

The GU-owned construction embeds each branch generator \(H\) through

\[
\Phi_\lambda(H)
=
cI_4+
\begin{pmatrix}
0&H+\lambda H^\dagger\\
H^\dagger+\lambda H&0
\end{pmatrix}.
\]

For \(\lambda\neq\pm1\), the map is faithful:

\[
H=
\frac{T-\lambda T^\dagger}{1-\lambda^2},
\qquad
T=H+\lambda H^\dagger.
\]

It is unitary-equivariant and gives every support point the same:

- Hilbert dimension;
- spin dimension;
- local trace;
- signature bound;
- measure weights;
- boundedness ceiling; and
- causal Lagrangian.

Nevertheless, the exact action margins are

\[
\delta_{7/10}
=
\mathcal S(\rho_{-,7/10})
-
\mathcal S(\rho_{+,7/10})
=\frac{1517}{5000}>0,
\]

while

\[
\delta_{9/10}
=
\mathcal S(\rho_{-,9/10})
-
\mathcal S(\rho_{+,9/10})
=-\frac{43}{200}<0.
\]

The first encoding favors the stable branch. The second favors the
pathological branch.

## 2. Representation-robust selection rule

For a physically justified faithful representation class
\(\mathfrak R\), define

\[
\delta_\Phi
=
\mathcal S(\rho_{\Phi,-})
-
\mathcal S(\rho_{\Phi,+}) .
\]

Classify:

- `ROBUST_GOOD_SELECTOR` if every admitted
  \(\delta_\Phi>0\), with a positive margin;
- `ROBUST_BAD_SELECTOR` if every admitted
  \(\delta_\Phi<0\), with a negative margin;
- `REPRESENTATION_SENSITIVE_NO_SELECTOR` if both signs occur;
- `OPEN_ZERO_MARGIN` if an admitted margin is zero; and
- `INCOMPLETE_REPRESENTATION_CLASS` if the rival class is empty or unfrozen.

For the W246 class:

\[
\{\delta_{7/10},\delta_{9/10}\}
\]

contains both signs. The result is
`REPRESENTATION_SENSITIVE_NO_SELECTOR`.

## 3. Why this is not ordinary gauge dependence

The CFS causal action is invariant under a common unitary change of basis, and
the probe verifies that control.

The ambiguity arises earlier: how a Krein generator becomes an ordinary
self-adjoint CFS operator point. The parameter \(\lambda\) changes the
relative physical weight assigned to Hermitian and anti-Hermitian components.
Both maps retain the original generator, but they do not define the same
physical completion.

Calling that choice “gauge” would be incorrect because the held-out action
ordering changes. A physical theory must:

1. derive the local-correlation map;
2. identify an invariant quotient on which the action factors; or
3. admit the choice as additional supplied physical structure.

## 4. Law and record attribution

Suppose a future physical rule independently derives
\(\Phi_{7/10}\). Then the resulting branch preference is a **conditional
law-level selector**. The credit belongs to the rule selecting the map plus
the causal action.

It gives no automatic credit to:

- records;
- observer access;
- archives;
- regional certificates;
- layered finality; or
- record-created reality.

Only after the physical representation and law are fixed should DU compare
the lawful target diameter before records with the diameter on a nonempty,
formed-record fibre.

## 5. Exact executable receipt

`tests/du_cfs_selector_representation_robustness_probe.py` passes `10/10`
checks and writes
`tests/artifacts/du_cfs_selector_representation_robustness_result.json`.

It verifies:

- both exact action tuples;
- the opposite singleton verdicts;
- the joint representation-sensitive verdict;
- zero-margin and empty-class fail-closed behavior;
- conditional law attribution when a physical map rule is supplied; and
- zero record credit while the record interface remains unselected.

This is finite exact bookkeeping and a cross-repository attribution control,
not a physical theorem about CFS, GU, baryogenesis, records, or the universe.

## 6. Consequence for the North Star

DU's reconstruction question must be asked after two earlier invariance gates:

\[
\text{physical representation}
\longrightarrow
\text{lawful completion class}
\longrightarrow
\text{formed record}
\longrightarrow
\text{held-out target}.
\]

If the physical representation is unfixed and changes which completion is
lawful, record sufficiency is premature. The “physical remainder” may be only
a representation remainder.

This applies beyond the GU/CFS case:

- Hilbert/Stinespring lifts;
- gauge fixing and observer frames;
- effective field variables;
- coarse-grained causal graphs;
- database schemas and provenance quotients; and
- learned latent-state models.

In each case, a selector must either factor through the admitted
representation quotient or explain physically why one representation is
privileged.

## 7. Stop and reopener

No more local encoding tournaments are warranted. The exact sign reversal has
already supplied the decision.

Reopen only when GU/CFS provides:

1. a physical wave-evaluation/local-correlation map;
2. an invariant excluding one faithful encoding without using the target
   branch;
3. a robust ordering over that physically justified class; and then
4. an independently formed record interface capable of reducing a still-open
   lawful target fibre.

No external hardware is relevant to this boundary.

Ownership: GU owns the matrices, embeddings, causal-action calculation, and
finite no-go in
`../../gu-formalization/explorations/W246-cfs-self-adjointization-selector-ambiguity-2026-07-26.md`.
DU owns only the representation-robust selection and record-attribution rule.
