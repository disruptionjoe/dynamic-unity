---
title: "Center-screening regional finality and first-leak localization"
status: completed_scoped_result
doc_type: theorem_collision_and_exact_controls
created: 2026-07-26
hypothesis_id: HC-DU-035D
run_id: RUN-20260726-154509-center-screening-regional-finality
authority: "Joe direct chat: proceed with the third large swing of the five-swing Dynamic Unity campaign"
claim_grade: "EXACT FINITE-DIMENSIONAL CENTER-SCREENING, COMPOSITION, FIRST-LEAK, AND QUANTITATIVE WITNESS THEOREM / KNOWN OPERATOR-ALGEBRA, PROCESS-MEMORY, AND LUMPABILITY MATHEMATICS / NO PHYSICAL REGIONALIZATION, UNIVERSAL FINALITY, OR NEW PHYSICS"
run_plan: "../lab/process/runs/RUN-20260726-154509-center-screening-regional-finality/run-plan.md"
probe: "../tests/du_center_screening_regional_finality_probe.py"
artifact: "../tests/artifacts/du_center_screening_regional_finality_result.json"
---

# Center-screening regional finality

## Result in plain English

This swing gives layered regional finality a precise quantum meaning.

A public record does not have to destroy every hidden quantum degree of
freedom in order to be final. The quantum state inside a recorded sector can
remain fully present. What matters is whether any admitted future operation
can convert that hidden state back into a later public record.

The exact boundary is:

> A layered public record is screened from its noncommutative fibres when
> every complete selective future map pulls the next public center into the
> current public center.

When that condition holds at every layer:

- the public records form an autonomous classical stochastic process;
- arbitrary retained quantum fibres cannot affect any future public record;
- sequential, parallel, and public-record-adaptive composition remain safe;
  and
- the fibres may persist without being destroyed.

When it fails, there is a first map where a future public question pulls back
to a noncentral effect. That map localizes the leak. Two states with the same
public record but different within-sector state then give a finite
same-record/different-future-record witness.

The smallest genuinely quantum control is sharp:

- region A and region B have the same public sector bits in both cases;
- region A's hidden fibre is either \(|+\rangle\) or \(|-\rangle\);
- those fibre states have identical computational-basis populations;
- a standard unitary controlled in the fibre \(X\) basis converts the phase
  distinction into region B's next public sector; and
- the later public records differ with probability gap \(1\).

This is ordinary quantum mechanics, not a proposed deviation. It proves that
public finality cannot be inferred from a stable archive alone while an
admitted coherent recoupling remains possible.

The converse is equally important. A center-preserving regional update leaves
the two orthogonal fibre states intact but screens them from every public
outcome in the declared future action class. Finality is therefore causal
screening, not necessarily physical erasure.

## What this adds beyond `HC-DU-033D`

`HC-DU-033D` established the one-layer boundary:

- the center is the finest action-internal nondisturbing sharp record;
- central complete joint effects make that record autonomous; and
- noncommutative blocks retain a capability-relative remainder.

This swing proves the recursive consequence. It asks what happens when
regional centers are promoted, merged, hardened, and used as nodes at the
next layer while their noncommutative fibres remain.

The answer is a composition and localization theorem:

```text
selective center preservation at every layer
    -> screened autonomous public process under all finite composition;

future public dependence on a fibre
    -> first noncentral pullback
    -> finite same-center witness at that exact layer.
```

It also adds a quantitative leakage margin and the aggregate-versus-selective
counterexample required by `HC-DU-036H`.

## Frozen layered object

At each layer \(k\), let

\[
\mathcal A_k
\subseteq
B(\mathcal H_k)
\]

be a finite-dimensional action algebra with center

\[
Z_k=Z(\mathcal A_k).
\]

Let \(\{z^k_q\}\) be its minimal central projectors. The formed public record
at layer \(k\) is the spectrum of \(Z_k\). The noncommutative matrix blocks of
\(\mathcal A_k\) remain explicit fibres over those public labels.

For several independent input regions,

\[
\mathcal A_{\mathrm{in}}
=
\bigotimes_i\mathcal A_i,
\qquad
Z(\mathcal A_{\mathrm{in}})
=
\bigotimes_i Z(\mathcal A_i).
\]

Freeze a complete selective regional instrument
\(\{\mathcal J_\alpha\}\), where \(\alpha\) retains every acquisition stratum,
route, response, validity flag, provenance field, and reset-relevant branch
required by the physical contract. Its Heisenberg adjoint is typed as

\[
\mathcal J_\alpha^*:
\mathcal A_{k+1}
\longrightarrow
\mathcal A_k.
\]

If a physical pullback leaves \(\mathcal A_k\) entirely, the action algebra
was not closed under the admitted dynamics. That is an interface/action-class
failure before the center-screening question, not a successful regional
quotient.

## Definition — selective center screening

A selective map \(\mathcal J_\alpha\) screens the public center when

\[
\mathcal J_\alpha^*(Z_{k+1})
\subseteq
Z_k.
\]

Equivalently, for every next public label \(q'\),

\[
E_{\alpha,q'}
=
\mathcal J_\alpha^*(z^{k+1}_{q'})
\in
Z_k.
\]

These are the complete event-and-next-record effects. Testing only the
nonselective sum \(\sum_\alpha\mathcal J_\alpha\) is weaker.

## Theorem 1 — regional center descent

The following are equivalent:

1. every complete selective event/next-record probability depends on the
   input state only through its current central record;
2. every \(\mathcal J_\alpha^*(z^{k+1}_{q'})\) lies in \(Z_k\); and
3. there is a well-defined subnormalized classical kernel

   \[
   K(\alpha,q'\mid q)
   \]

   on the central labels such that every physical state in current sector
   \(q\) induces the same complete row.

### Proof

If the effect is central, it has a unique expansion

\[
\mathcal J_\alpha^*(z^{k+1}_{q'})
=
\sum_q K(\alpha,q'\mid q)z^k_q.
\]

A normalized state supported in sector \(q\) assigns that cell probability
\(K(\alpha,q'\mid q)\), independent of the noncommutative fibre state.
Summing over \(\alpha,q'\) gives the normalization appropriate to the
declared selective instrument.

Conversely, suppose the expectation of
\(E_{\alpha,q'}\) is constant over every normalized state in one central
block. The compression

\[
z^k_qE_{\alpha,q'}z^k_q
\]

must be scalar on that block; otherwise two eigenstates give different
probabilities. Since the effect belongs to \(\mathcal A_k\), scalarity on
every minimal central block is exactly membership in \(Z_k\). \(\square\)

This is the operator-algebra regional specialization of `HC-DU-036H`.

## Theorem 2 — sequential, parallel, and adaptive closure

Selectively center-screening maps close under:

1. sequential composition;
2. tensor-product composition of independent regions; and
3. policies that choose the next admitted map using only the retained public
   record and prior public selective outcomes.

### Sequential proof

Let

\[
\mathcal J_\alpha^*(Z_{k+1})\subseteq Z_k
\]

and

\[
\mathcal K_\beta^*(Z_{k+2})\subseteq Z_{k+1}.
\]

Then

\[
(\mathcal K_\beta\circ\mathcal J_\alpha)^*
=
\mathcal J_\alpha^*\circ\mathcal K_\beta^*
\]

maps \(Z_{k+2}\) into \(Z_k\).

### Parallel proof

The product center is spanned by tensors
\(z_1\otimes\cdots\otimes z_n\). The tensor-product pullback sends each such
element to

\[
\mathcal J_1^*(z_1)\otimes\cdots\otimes\mathcal J_n^*(z_n),
\]

which lies in the product input center.

### Adaptive proof

Condition on any retained public trace. The selected next map is
center-screening by assumption. Induction therefore gives a classical
controlled kernel for every finite public trace and every policy measurable
with respect to that trace. \(\square\)

### Screening theorem

Two physical states agreeing on the current center give identical
probabilities for every finite public-record experiment constructed from the
declared selectively center-screening maps. Their noncommutative fibres may
remain different, orthogonal, entangled, or otherwise physically present.

This is operational duality for the frozen public action class. It is not
microscopic state identity.

## Theorem 3 — first-leak localization

Fix one selective future branch and one final public central effect
\(z^L_{q_L}\). Pull it backward:

\[
E_L=z^L_{q_L},
\qquad
E_k=\mathcal J_k^*(E_{k+1}).
\]

If the final public probability depends on a hidden fibre at an earlier
layer, then \(E_0\notin Z_0\). Because \(E_L\in Z_L\), there is a latest layer
\(k\) in the backward sequence for which

\[
E_{k+1}\in Z_{k+1},
\qquad
E_k\notin Z_k.
\]

The map \(\mathcal J_k\) is the first center leak seen from the public future.
Two states in one current central block separate \(E_k\), and therefore
separate the declared future public event.

This localizes the failure to one map. It prevents blaming an entire regional
network, record ontology, or quantum theory when one supplied coupling or
retained route is responsible.

## Theorem 4 — exact leakage margin

Let \(E=E^\dagger\in\mathcal A_k\) be any pulled-back future public effect.
For current central sector \(q\), define

\[
L_q(E)
=
\lambda_{\max}
\left(E|_{z_q\mathcal H_k}\right)
-
\lambda_{\min}
\left(E|_{z_q\mathcal H_k}\right).
\]

Then

\[
L_q(E)
=
\max_{\rho,\sigma:\ \rho=z_q\rho z_q,\ \sigma=z_q\sigma z_q}
\left|
\operatorname{tr}\!\left((\rho-\sigma)E\right)
\right|.
\]

Consequently,

\[
L(E)=\max_qL_q(E)
\]

is the largest same-definite-public-record probability gap, and

\[
L(E)=2\,\operatorname{dist}_{\infty}(E,Z_k).
\]

The maximizing states are eigenstates of the largest and smallest eigenvalues
inside the offending block. Therefore every noncentral future public effect
has an exact finite witness. No search over arbitrary histories is required.

## The two-region exact specimen

Each region carries:

\[
\mathcal A_i
\cong
\mathbb C^2_{\mathrm{sector}}
\otimes
M_2(\mathbb C)_{\mathrm{fibre}}.
\]

The public center records the sector bit. The fibre remains quantum.

### Positive coupling — public center controls public center

A CNOT from region A's sector to region B's sector is a permutation of the
four central labels. Its pullback maps every next central projector to a
current central projector. Fibre states are irrelevant to the public update.

Two orthogonal fibre states remain orthogonal after the coupling, so the
positive result is screening rather than destruction.

### Population leak

A CNOT from region A's fibre \(Z\)-value to region B's public sector sends two
states with the same old public record to opposite new public records. The
pulled-back public effect is noncentral inside the old sector. The exact
probability margin is \(1\).

This is the classical hidden-state form of the failure.

### Coherent phase leak

Define the standard unitary

\[
U_X
=
P_+^{(f_A)}\otimes I_{s_B}
+
P_-^{(f_A)}\otimes X_{s_B},
\]

with identity on the other degrees of freedom. Here

\[
P_\pm=\frac{I\pm X}{2}.
\]

Prepare the same public sectors in both cases and choose fibre state
\(|+\rangle\) or \(|-\rangle\). These states have identical \(Z\)-basis
populations. Yet \(U_X\) leaves B's public sector unchanged for
\(|+\rangle\) and flips it for \(|-\rangle\).

Thus:

\[
\text{same formed regional center}
+
\text{same fibre populations}
+
\text{different fibre phase}
\longrightarrow
\text{opposite later public record}.
\]

This is a genuinely quantum version of the leak, but it is completely
predicted by standard unitary quantum mechanics.

### Screening by physical destruction

Dephasing the fibre in the \(Z\) basis sends both \(|+\rangle\) and
\(|-\rangle\) to \(I/2\). The later \(U_X\) assay then gives identical public
records.

This is a valid repair, but it is not free. It physically destroys coherent
optionality. Center screening by a restricted future action class and
screening by irreversible/noisy destruction are different mechanisms and
must carry different resource receipts.

## Aggregate preservation is not selective finality

Measure the hidden fibre in the \(X\) basis and retain route
\(\alpha\in\{+,-\}\). The two route Kraus operators are the fibre projectors
\(P_+\) and \(P_-\).

The nonselective channel preserves every public central projector exactly:

\[
\sum_\alpha
P_\alpha z_qP_\alpha
=z_q.
\]

But each complete selective cell

\[
P_\alpha z_qP_\alpha
=z_qP_\alpha
\]

is noncentral. The retained route distinguishes \(|+\rangle\) from
\(|-\rangle\) with certainty.

Therefore:

```text
aggregate public-center preservation
    != complete selective center screening
    != HC-DU-036H autonomous public record.
```

Discarding a route can make the coarse process look final. If the route,
controller, environment, or correlated memory remains physically accessible
or can later recouple, it belongs in the complete contract.

## Exact controls

The regression probe passes `29/29` with exact rational matrices.

| Control | Exact result |
|---|---|
| regional center | four orthogonal projectors for two public bits |
| public-only CNOT | unitary and center-screening |
| sequential public-only composition | remains center-screening |
| fibre-population CNOT | same old center, opposite new center, margin \(1\) |
| fibre-phase controlled unitary | same old center and same \(Z\) populations, opposite new center, margin \(1\) |
| first-leak trace | final effect central; its first hostile pullback noncentral |
| public-only screening | orthogonal fibres persist while public records agree |
| later hostile recoupling | retained fibre re-enters the public record |
| \(Z\)-dephasing | hostile phase pair becomes identical before recoupling |
| aggregate \(X\)-route measurement | nonselective center preserved, selective cells noncentral |
| common permutation conjugation | safe/leaking verdicts and margin unchanged |
| authenticated distributed shadow | public-only transition descends; hidden-local-state hook fails |

The executable is regression after direct proof. It generates no simulated
physics claim and requires no hardware.

## Distributed-systems comparison

The same exact quotient schema applies to an authenticated distributed
process:

- public certificate bits play the role of the center;
- local replica, mempool, scheduler, or metastable state plays the role of a
  hidden fibre;
- a safe public transition depends only on the certified state; and
- a hidden hook that later changes the public certificate proves the earlier
  certificate was not a sufficient state for that transition class.

That is ordinary abstraction refinement and lumpability. It is not a claim
that validators are qubits.

The quantum specimen adds one structure absent from the binary distributed
shadow: two fibres can have the same public record and the same declared
classical populations while differing only by phase, and a coherent coupling
can convert that phase into a public outcome. This identifies the exact
quantum delta without inventing nonstandard quantum dynamics.

## Perspectival-curvature correction

If every regional reconciliation map is selectively center-screening, hidden
fibre holonomy cannot secretly alter a later public fact. Any path or
order-dependent public result is already represented in the induced
classical kernels on the centers.

Therefore a proposed “perspectival curvature of public facts” has three honest
possibilities:

1. ordinary path dependence already visible in the public center process;
2. a first noncentral fibre-to-center coupling;
3. an omitted selective route, occurrence-identity lift, or provenance field.

Closed-loop order dependence alone is not evidence of new quantum geometry.
A novel curvature claim must survive this center-screening decomposition.

## Strongest collision

The mathematical components are occupied:

| Component | Strong collision | Disposition |
|---|---|---|
| CP maps with a stable commutative algebra restrict to a classical Markov operator | Bardet, [*Quantum extensions of dynamical systems and of Markov semigroups*](https://arxiv.org/abs/1509.04849) | direct known terrain |
| operationally detectable quantum memory and causal-break criteria | Pollock et al., [*Operational Markov Condition for Quantum Processes*](https://arxiv.org/abs/1801.09811) | known process-memory terrain |
| information-preserving algebras and noiseless subsystems | Blume-Kohout et al., [*The structure of preserved information in quantum processes*](https://arxiv.org/abs/0705.4282) | known operator-algebra terrain |
| correctable/private algebras and complementary channels | Kribs et al., [*Quantum Complementarity and Operator Structures*](https://arxiv.org/abs/1811.10425) | known OAQEC terrain |
| recursive quotient and finite witnesses | controlled lumpability/probabilistic bisimulation and `HC-DU-036H` | known process terrain |
| regional compatibility and action sufficiency | `HC-DU-035C` plus marginal/join-tree/contextuality theory | existing DU control stack over known components |

The direct theorem is not claimed as new mathematics. The Dynamic Unity
advance is the integrated interpretation and acceptance contract:

```text
formed center
    != destroyed fibre
    != screened fibre
    != selectively autonomous public process
    != physically selected regional finality.
```

## North-Star consequence

This result makes the three North-Star outcomes sharper.

### Record-first reconstruction

It holds for the public regional process relative to a selectively
center-screening future action class. Every public trace and public-adaptive
capability factors through the centers.

### Operational duality

It can hold while noncommutative fibres remain physically present. If no
admitted future action can expose them through a public record, the fibre and
record descriptions are operationally equivalent for that class.

### Physics-first remainder

A first noncentral pullback supplies the exact finite witness. The coherent
two-region fixture realizes margin \(1\), but only relative to its declared
action class. It is not yet an irreducible remainder against every physically
legitimate completion or boundary enlargement.

### Finality is action-class-relative

Adding a new noncentral future operation after the verdict changes the action
contract. It does not show that a previously proved finality theorem failed
inside its old scope. Conversely, omitting an already physically available
recoupling to obtain finality is an inadmissible restriction.

## Decision and next move

The verdict is:

```text
KNOWN_MATHEMATICS__CENTER_SCREENING_FINALITY_AND_FIRST_LEAK_EXACT
```

Do not spend another swing on a supplied marginal cover, contextuality
triangle, fitted PVM, or scalar finality score.

The fourth campaign swing should now take the screened public regional
process as the input to time/geometry reconstruction while retaining one
explicit fibre-leak foil:

1. freeze identical certified public causal networks;
2. let one completion satisfy selective center screening and another contain
   the smallest admitted first-leak coupling;
3. ask which effective clock, geometry, or capability targets factor through
   the public network in both;
4. separate public-kernel reconstruction from targets already fixed by the
   law; and
5. return either a common reconstruction theorem or a finite
   same-public-network/different-physical-target witness.

The parallel physical burden remains unchanged: independently derive or
justify the regional action algebras, boundaries, couplings, archives, and
future action class in a real arena.

No external hardware is needed or implicated.
