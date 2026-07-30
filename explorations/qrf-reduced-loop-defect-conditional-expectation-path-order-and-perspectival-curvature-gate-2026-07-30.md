---
title: "QRF reduced-loop defect, conditional-expectation path order, and perspectival-curvature gate"
status: completed_scoped_result
doc_type: exact_loop_closure_theorem_channel_controls_and_curvature_admission_boundary
created: 2026-07-30
hypothesis_id: HC-DU-155
run_id: RUN-20260730-080556-qrf-reduced-loop-curvature-gate
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_4
  - lane_5
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 exact reduced-loop closure and noncommuting-access boundary; Grade 5 only for a physically selected complete loop whose invariant excess survives full-lineage, representation, refinement, and standard-quantum controls."
probe: "../tests/du_qrf_reduced_loop_curvature_gate_probe.py"
artifact: "../tests/artifacts/du_qrf_reduced_loop_curvature_gate_result.json"
---

# QRF reduced-loop defect and perspectival-curvature gate

## Executive result

The swing returned:

```text
FULL_REVERSIBLE_FRAME_TRANSFORMATION_AND_REDUCED_ACCESS_CHANNEL_ARE_DIFFERENT_OBJECTS
+ FULL_FORWARD_RETURN_CAN_CLOSE_EXACTLY
+ INTERMEDIATE_DISCARD_AND_FRESH_REASSIGNMENT_CAN_BREAK_REDUCED_LOOP_CLOSURE
+ THE_REDUCED_LOOP_DEFECT_IS_EXACTLY_THE_DISCARDED_LINEAGE_TERM
+ LOOP_CLOSURE_CAN_HOLD_ON_ONE_OBSERVABLE_ALGEBRA_WHILE_FAILING_ON_THE_FULL_STATE
+ TRACE_PRESERVING_CONDITIONAL_EXPECTATIONS_COMPOSE_PATH_INDEPENDENTLY WHEN THEY COMMUTE
+ NONCOMMUTING_QUBIT_REDUCTIONS GIVE AN EXACT ORDER_EFFECT
+ THE_ORDER_EFFECT IS INVARIANT UNDER JOINT REPRESENTATION CHANGE
+ REDUCED_LOOP_DEFECT_OR_ORDER_EFFECT_ALONE IS NOT PERSPECTIVAL_CURVATURE
+ STANDARD_CHANNEL_RECOVERY_CONDITIONAL_EXPECTATION_AND_QUANTUM_ERASURE_THEORY_ABSORB_THE_MATHEMATICS
+ A GENUINE CURVATURE CANDIDATE MUST SURVIVE COMPLETE_LINEAGE_AND_SAME_PROTOCOL_CONTROLS
+ NO_SELECTED_INTERFACE_NEW_PHYSICS_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

In plain terms:

> Returning to the same perspective is not the same experiment if information
> was thrown away on the outward trip and a fresh blank system was silently
> substituted on the return.

The complete reversible transformation may close exactly while the reduced
observer description does not. That failure is ordinary information loss,
not evidence that perspective space itself has curvature.

There is a second ordinary source of apparent curvature. Two access
reductions onto noncommuting quantum observable algebras can give different
answers in different orders. This is a real operational order effect, but
the two orders are different physical protocols. It becomes a curvature
candidate only if the same complete physical loop, with the same retained
lineage and covariantly transformed readout, has a nontrivial invariant
residue that standard quantum channel theory cannot absorb.

This narrows rather than eliminates Dynamic Unity's high-ceiling
perspectival-curvature idea.

## 1. Source and absorber map

Three primary-source results establish the relevant background:

1. Luppi, Kabel, Giacomini, and Smirne define
   [reduced QRF channels](https://arxiv.org/abs/2607.05578) by transforming a
   complete system and then tracing the old reference and environmental
   degrees declared inaccessible. Their map is a channel, not generally an
   invertible frame transformation on one fixed subsystem.
2. Carette, Głowacki, and Loveridge define
   [operational QRF transformations](https://arxiv.org/abs/2303.14002) on
   operational-equivalence classes and show that invertibility depends on
   the final frame's localizability.
3. Ballesteros, Giacomini, and Gubitosi exhibit a
   [group structure for one class of full dynamical QRF
   transformations](https://arxiv.org/abs/2012.15769).

These sources do not conflict. They concern different typed objects:

| object | type | invertibility status |
|---|---|---|
| complete QRF transformation | reversible transformation on a complete constrained or relational packet | may form a group/groupoid or be invertible under declared conditions |
| operational transformation on equivalence classes | map between frame-relative operational state classes | invertible under the source's localizability condition |
| reduced QRF channel | transform, then discard inaccessible degrees | CPTP; generally noninvertible |
| record handoff | preservation of a chosen observable or block through the reduced channel | may survive even if the whole channel is noninvertible |
| formed/certified record | physical write, provenance, retention, access, and rival-exclusion packet | not selected by the QRF maps alone |

The strongest mathematical absorbers are therefore:

- Stinespring dilation;
- data processing and channel recoverability;
- conditional expectations and commuting squares;
- quantum erasure and retained which-path information; and
- covariance of complete state--channel--readout descriptions.

The Dynamic Unity contribution is not new channel mathematics. It is the
typed theorem and hostile gate preventing ordinary access loss from being
promoted to physical perspectival curvature.

## 2. Exact reduced-loop closure theorem

### 2.1 Typed packet

Let:

- \(J_A\) assign an accessible \(A\)-description to a complete packet;
- \(R_A\) reduce a complete packet to \(A\)'s accessible description;
- \(J_B\) and \(R_B\) do the same for \(B\);
- \(R_AJ_A=\mathrm{id}_A\) and \(R_BJ_B=\mathrm{id}_B\);
- \(\mathcal U=\operatorname{Ad}_U\) be an invertible complete
  \(A\)-to-\(B\) transformation; and
- \(\mathcal U^{-1}=\operatorname{Ad}_{U^\dagger}\).

The reduced handoffs are

\[
Q_{A\to B}=R_B\mathcal UJ_A,
\qquad
Q_{B\to A}=R_A\mathcal U^{-1}J_B.
\tag{1}
\]

The complete transformation closes:

\[
\mathcal U^{-1}\mathcal U=\mathrm{id}.
\tag{2}
\]

The reduced loop need not:

\[
L_A=Q_{B\to A}Q_{A\to B}.
\tag{3}
\]

### 2.2 Theorem

On the admitted input span,

\[
L_A-\mathrm{id}_A
=
R_A\mathcal U^{-1}
\bigl(J_BR_B-\mathrm{id}\bigr)
\mathcal UJ_A.
\tag{4}
\]

Therefore the reduced loop closes exactly iff

\[
R_A\mathcal U^{-1}
\bigl(J_BR_B-\mathrm{id}\bigr)
\mathcal UJ_A=0.
\tag{5}
\]

### Proof

Using \(R_AJ_A=\mathrm{id}_A\) and
\(\mathcal U^{-1}\mathcal U=\mathrm{id}\),

\[
\begin{aligned}
L_A-\mathrm{id}_A
&=
R_A\mathcal U^{-1}J_BR_B\mathcal UJ_A
-R_AJ_A\\
&=
R_A\mathcal U^{-1}J_BR_B\mathcal UJ_A
-R_A\mathcal U^{-1}\mathcal UJ_A\\
&=
R_A\mathcal U^{-1}
\bigl(J_BR_B-\mathrm{id}\bigr)
\mathcal UJ_A.
\end{aligned}
\]

Equation (5) follows immediately. \(\square\)

### 2.3 Interpretation

The map

\[
P_B=J_BR_B
\tag{6}
\]

is idempotent:

\[
P_B^2=J_B(R_BJ_B)R_B=P_B.
\tag{7}
\]

It is the operation “retain what \(B\) can access, discard the rest, then
fill the missing packet with \(B\)'s declared assignment.” The loop defect is
exactly the part removed by \(P_B\), transported back to \(A\) and tested by
\(R_A\).

A strong sufficient condition for closure is

\[
P_B\mathcal UJ_A=\mathcal UJ_A:
\tag{8}
\]

the outward image already lies entirely in the reconstructible assigned
packet. This is not necessary. Information may be discarded yet remain
invisible to the returning \(A\)-access map.

This distinction matters:

```text
full lineage retained
  -> complete reversible loop can close

lineage discarded but irrelevant to A's returned algebra
  -> selected facts can still close

lineage discarded and relevant after return
  -> reduced loop defect
```

## 3. Algebra-relative loop closure

Let \(\mathcal A_A\) be the chosen observable algebra whose records or facts
are meant to survive the loop. Full state recovery is unnecessary. The exact
condition is

\[
L_A^\dagger(a)
=
Q_{A\to B}^\dagger Q_{B\to A}^\dagger(a)
=a
\qquad
\forall a\in\mathcal A_A.
\tag{9}
\]

This is the compositional version of the `HC-DU-153` handoff distinction.
A chosen outcome block may survive a reduced reference change even while
other coherences or correlations do not.

It also explains the `HC-DU-154` result. The outcome algebra can be copied
and returned faithfully while reference-position coherence survives only if
no position-branch information remains in the discarded packet.

For the full matrix algebra on all states, a CPTP left inverse makes the
forward channel reversible on that state class. On equal finite dimensions,
full-state reversible channels are unitary. Nonunitary reduced QRF channels
can therefore close only on a restricted state family or observable
algebra, not as universally invertible frame changes.

The correct layered-finality object is consequently not one scalar. It is a
family of preserved algebras or response quotients indexed to the physical
handoff and access contract.

## 4. Exact retained-versus-discarded-lineage control

Use a system qubit \(S\), a carrier qubit \(E\), and the controlled-NOT

\[
U|s,e\rangle=|s,e\oplus s\rangle.
\tag{10}
\]

Since \(U^2=I\), the complete outward-and-return transformation closes
exactly.

Start with

\[
\rho_S=|+\rangle\!\langle+|,
\qquad
\rho_E=|0\rangle\!\langle0|.
\tag{11}
\]

After the first \(U\), \(E\) carries perfect \(Z\)-branch information.

### Retain the same carrier

Apply the inverse \(U\) to the same joint state:

\[
U^\dagger U(\rho_S\otimes\rho_E)UU^\dagger
=
\rho_S\otimes\rho_E.
\tag{12}
\]

The accessible state returns exactly to \(|+\rangle\).

### Discard and silently refresh the carrier

Trace \(E\) after the outward step:

\[
R_E\!\left(
U(\rho_S\otimes|0\rangle\!\langle0|)U^\dagger
\right)
=\frac I2.
\tag{13}
\]

Attach a fresh \(|0\rangle_E\), apply the nominal inverse, and reduce again.
The answer remains

\[
\rho'_S=\frac I2.
\tag{14}
\]

The \(X{+}\) probability changed from \(1\) to \(1/2\), and the trace
distance from the original state is \(1/2\).

Nothing curved. The return protocol lacked the carrier needed to reverse the
outward operation. The exact probe verifies Equation (4) on all four basis
operators of \(M_2\): the entire reduced-loop defect equals the discarded
lineage term.

## 5. Exact path-order control

### 5.1 Conditional expectations

On a qubit Bloch vector \(r\), complete dephasing in the basis with unit axis
\(a\) is

\[
\mathcal D_a:r\longmapsto (a\cdot r)a.
\tag{15}
\]

It is the trace-preserving conditional expectation onto

\[
\operatorname{span}\{I,a\cdot\sigma\}.
\tag{16}
\]

In Bloch coordinates its linear part is the rank-one projector

\[
P_a=aa^{\mathsf T}.
\tag{17}
\]

Two such reductions commute exactly when their rank-one projectors commute.
For unit vectors this occurs when the axes are parallel/antiparallel or
orthogonal. In the commuting case, the order-independent composition is the
conditional expectation onto the common retained algebra. This is the
finite trace-preserving form of the commuting-square condition.

### 5.2 Noncommuting exact fixture

Take

\[
a=(0,0,1),
\qquad
b=\left(\frac35,0,\frac45\right),
\qquad
r=a.
\tag{18}
\]

Then

\[
\begin{aligned}
\mathcal D_b\mathcal D_a(r)
&=
\left(\frac{12}{25},0,\frac{16}{25}\right),\\
\mathcal D_a\mathcal D_b(r)
&=
\left(0,0,\frac{16}{25}\right).
\end{aligned}
\tag{19}
\]

An \(X{+}\) readout differs by

\[
\Delta p=\frac6{25},
\tag{20}
\]

and the two outputs have trace distance

\[
D_{\rm tr}=\frac6{25}.
\tag{21}
\]

The Bloch-map commutator is

\[
[P_b,P_a]
=
\begin{pmatrix}
0&0&12/25\\
0&0&0\\
-12/25&0&0
\end{pmatrix}.
\tag{22}
\]

The effect is real and measurable. It is also completely standard quantum
mechanics. “Reduce in algebra \(A\), then \(B\)” and “reduce in \(B\), then
\(A\)” are different physical protocols when the reductions do not commute.

The probe rotates the input, both axes, both channels, and the readout
together. All probabilities remain unchanged. The order effect is
representation covariant; it is not an artifact of choosing \(X\) and \(Z\)
labels. But covariance does not turn it into new physics.

## 6. Curvature admission gate

Dynamic Unity's earlier **perspectival curvature** conjecture asked whether a
closed loop of mutually consistent perspective transformations could have a
measurable holonomy.

This swing identifies two large standard-physics absorbers:

### Absorber A — access-loss defect

\[
\text{full loop closes}
\quad\text{but}\quad
\text{intermediate reduction discards return-relevant lineage}.
\]

The reduced defect is Equation (4).

### Absorber B — noncommuting protocol order

\[
\mathcal E_2\mathcal E_1
\ne
\mathcal E_1\mathcal E_2.
\]

The two paths are different interventions or coarse-graining orders. Their
difference is not a holonomy of one unchanged complete experiment.

### Minimum surviving curvature candidate

A future claim may enter the physical-curvature class only if it supplies all
of the following:

1. **Selected objects:** the reference systems, full transformation maps,
   assignments, access reductions, record algebras, and path composition are
   selected by one physical packet rather than chosen after the result.
2. **A genuinely closed full loop:** the composed complete path represents
   return to the same physical frame/process up to the declared gauge, not a
   nontrivial group commutator renamed as closure.
3. **Complete lineage control:** every carrier discarded on one path is
   retained, reset, or matched on the rival path; Equation (4) is measured or
   shown to vanish.
4. **Same-protocol control:** path alternatives differ only in the proposed
   geometric/perspectival variable, not in the order of noncommuting
   measurements, traces, controllers, or resets.
5. **Covariant readout:** state, dynamics, reference, and measurement are
   transformed together.
6. **Refinement invariance:** benign subdivision, relay insertion, relabeling,
   and dilation choice do not change the result.
7. **Standard-QM null:** conditional expectations, channel memory,
   decoherence, ordinary phase, and open-system dynamics cannot reproduce the
   held-out statistic under the same packet.
8. **Finite no-refit consequence:** one frozen loop predicts a nonzero
   probability, phase, resource, or capability difference on a held-out
   configuration.

Without all eight, the honest label is:

```text
ACCESS_RELATIVE_LOOP_DEFECT
```

or

```text
NONCOMMUTING_REDUCTION_ORDER_EFFECT
```

not perspectival curvature.

## 7. Relation to distributed and consensus architectures

There is one exact transferable structure and one forbidden analogy.

The exact structure is:

> Idempotent access reductions compose path independently when the relevant
> conditional expectations commute.

This has the same algebraic design goal as order-independent replicated
merge: repeated local reductions should not make the joined result depend on
the reconciliation route. The statement transfers only when the physical
maps genuinely are the same idempotent conditional expectations and the
composition contract is frozen.

The forbidden shortcut is:

> “Quantum noncommutativity is Byzantine disagreement” or “a nonzero
> commutator is regional-finality curvature.”

No fault model, adversary, threshold, authentication protocol, common
knowledge rule, or public certificate follows from Equation (22). The result
only says that quantum access restrictions can be noncommuting and therefore
order sensitive.

For Dynamic Unity, this yields a sharper regional-finality requirement:

```text
selected local interfaces
  -> selected access/reduction maps
  -> commuting-square or explicit ordered-composition law
  -> complete lineage preservation/recovery
  -> only then test regional holonomy or public finality
```

## 8. What changed

### Earned

- the exact reduced-loop closure identity;
- a full-loop-positive/reduced-loop-negative qubit control;
- proof that the defect is precisely the discarded-lineage term;
- an algebra-relative loop-closure condition;
- an exact noncommuting conditional-expectation order effect;
- covariant representation control;
- a scoped commuting-square criterion for path-independent layered handoff;
  and
- a pre-registered physical admission gate for perspectival curvature.

### Not earned

- a physical QRF loop realizing the finite controls;
- a selected frame, factorization, assignment, access map, record algebra,
  archive, or certificate;
- a proof that perspectival curvature is impossible;
- a nonzero physical holonomy beyond standard quantum theory;
- a layered-finality dynamics or consensus law;
- a new prediction, hardware path, or paper; or
- a selected scientific successor.

The top-voted curvature idea remains open only in its stronger form. The
easy version—path dependence of reduced descriptions—is absorbed.

## 9. Portfolio disposition

`HC-DU-155` is a supporting Grade-4 boundary for the parked physical
reliability and regional-finality work. It does not satisfy any current
reopen rule because every interface and access reduction in the theorem is
supplied.

The exact reopener is:

> One physically selected three-reference or three-region packet with a
> complete full-loop transformation, matched retained lineage, covariant
> readout, benign-refinement invariance, and a no-refit loop statistic not
> reproduced by standard quantum channels.

Until that exists:

- do not search larger QRF loops numerically;
- do not call reduced-state order effects curvature;
- do not infer a regional consensus law;
- do not design hardware; and
- retain `NO_READY_SUCCESSOR`.

## 10. Reproducibility

Run:

```bash
python3 tests/du_qrf_reduced_loop_curvature_gate_probe.py
```

The exact regression checks:

- \(U^2=I\);
- retained-lineage loop closure;
- discard-and-refresh loop failure;
- the map identity in Equation (4) on a basis of \(M_2\);
- the exact \(6/25\) noncommuting-reduction order effect;
- commuting positive controls; and
- joint representation covariance.
