---
title: "Feedback-Boundary Response-Equivalence Selection and Capability Refinement"
status: banked_scoped_result
date: 2026-07-27
work_id: N5-PF-P3
claim_id: HC-DU-056
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_7
  - lane_A
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
maximum_grade: "scoped necessity/obstruction theorem with exact finite response-partition controls; known mathematics; no endogenous complete interface, new physics, prediction, ontology, or paper"
assumption_posture: "Exactly compensated continuous preferred foliation remains an ungraded conditional premise and is inert."
---

# Feedback-Boundary Response-Equivalence Selection and Capability Refinement

## Result in plain English

A physical theory does **not** need to pick one microscopic wire, controller,
Hamiltonian logarithm, or hidden dilation in order to determine everything an
observer can later experience and do. It only needs to pick one class of
implementations that behave identically under the observer's complete admitted
future actions.

That weaker target is exact:

> A physical antecedent selects the feedback boundary up to an admitted future
> action family exactly when every two implementations allowed by the same
> antecedent have the same complete future-response signature.

The important qualification is that the class depends on capability. Adding a
new action or tester can split a class that was previously final.

The two existing Dynamic Unity specimens show the same staircase:

```text
material Z3 gauge boundary
    source-only response
        -> orientation-sensitive pointer/control response
        -> intermediate-time formation-path response

closed metastable host
    endpoint/next reduced response
        -> archive-access occurrence response
        -> next-cycle reset-memory response
```

At each first rung, the weak physical antecedent selects a response class. At
the next rung, a previously hidden field becomes operational. Adding a material
orientation, archive route, formation path, or complete reset lineage can close
the corresponding class, but the existing source/host dynamics do not derive
those fields. They are physical contract completion unless independently
selected.

The strongest current verdict is therefore:

```text
PARTIAL_OR_ORBIT_BOUNDARY_SELECTION
FEEDBACK_BOUNDARY_RELOCATION_OBSTRUCTION
CAPABILITY_DEPENDENT_FIRST_LEAK
RESET_REQUIRES_COMPLETE_FUTURE_READABLE_MEMORY
CURRENT_COMPLETE_INTERFACE_NOT_ENDOGENOUSLY_SELECTED
MATHEMATICAL_CORE_FULLY_ABSORBED
FOLIATION_INERT
```

This is progress because it removes an unnecessarily strong demand for
microscopic uniqueness while making the actual remaining demand precise.

## 1. Frozen typed contract

Let:

- \(M\) be a class of physical implementations;
- \(A:M\to\mathsf A\) be an independently motivated physical antecedent;
- \(B:M\to\mathsf B\) be the complete feedback boundary implementation;
- \(\mathcal A\) be a frozen family of future actions or testers;
- \(Y_a\) be the response space for action \(a\in\mathcal A\); and
- \(\Sigma_{\mathcal A}:\mathsf B\to
  \prod_{a\in\mathcal A}\mathsf P(Y_a)\) be the complete response signature,
  deterministic responses included as point measures.

Define boundary response-equivalence by:

\[
b\sim_{\mathcal A}b'
\quad\Longleftrightarrow\quad
\Sigma_{\mathcal A}(b)=\Sigma_{\mathcal A}(b').
\]

This definition does not say that two implementations are physically
identical. It says that the frozen observer/action/resource contract has no
admitted operation that separates them.

The sought selector is:

\[
\bar B_{\mathcal A}:
\operatorname{im}A
\longrightarrow
\mathsf B/{\sim_{\mathcal A}}
\]

such that:

\[
\bar B_{\mathcal A}(A(m))=[B(m)]_{\mathcal A}.
\]

This is the exact Position-3 question. It is weaker than selecting \(B(m)\)
microscopically and stronger than merely showing that one supplied \(B\)
works.

## 2. Response-class selector theorem

### Theorem

The selector \(\bar B_{\mathcal A}\) exists exactly when:

\[
\ker A
\subseteq
\ker(\Sigma_{\mathcal A}\circ B).
\]

When it exists, it is unique on \(\operatorname{im}A\).

### Proof

If the selector exists and \(A(m)=A(m')\), then:

\[
[B(m)]_{\mathcal A}
=
\bar B_{\mathcal A}(A(m))
=
\bar B_{\mathcal A}(A(m'))
=
[B(m')]_{\mathcal A}.
\]

Therefore the response signatures agree.

Conversely, suppose response signatures agree on every antecedent fibre.
Define:

\[
\bar B_{\mathcal A}(\alpha)
=
[B(m)]_{\mathcal A}
\]

for any \(m\) with \(A(m)=\alpha\). Fibre constancy makes this well-defined.
The defining equation fixes its value at every \(\alpha\in\operatorname{im}A\),
so it is unique there. \(\square\)

### Why this matters

Demanding:

\[
A(m)=A(m')
\Longrightarrow
B(m)=B(m')
\]

would reject harmless microscopic plurality. The correct North-Star demand is
only equality in the operational quotient. Conversely, merely exhibiting one
working boundary does not establish the kernel inclusion across the antecedent
fibre.

## 3. Capability-refinement law

Let:

\[
\mathcal A_0\subseteq\mathcal A_1.
\]

Then:

\[
\sim_{\mathcal A_1}
\ \subseteq\
\sim_{\mathcal A_0}.
\]

The richer action family can only refine the response partition; it cannot
merge classes already separated by an older action.

Consequences:

1. Selection for \(\mathcal A_1\) implies selection for
   \(\mathcal A_0\).
2. Selection for \(\mathcal A_0\) need not survive
   \(\mathcal A_1\).
3. Failure for \(\mathcal A_0\) persists under every enlargement containing
   \(\mathcal A_0\).
4. A “first leak” is the first added action whose response is nonconstant on
   one current antecedent fibre.

This is the feedback-boundary version of Dynamic Unity's existing
capability-indexed finality rule. It is not a new order-theoretic theorem.

## 4. Exact repair criterion

Let \(P:M\to\mathsf P\) be a proposed additional physical premise. The repaired
antecedent \((A,P)\) selects the response class exactly when:

\[
\ker(A,P)
\subseteq
\ker(\Sigma_{\mathcal A}\circ B).
\]

The formal coarsest exact repair is the response-class label itself:

\[
P_{\min}(m)
=
\Sigma_{\mathcal A}(B(m)).
\]

That observation is mathematically useful and scientifically dangerous. If
\(P_{\min}\) is inserted only after seeing the future responses, it is
action-coded repair, not physical selection.

A repair earns physical credit only when:

1. its field is motivated and fixed independently of the desired response;
2. a physical law, initial/boundary condition, material structure, or
   intervention fixes it;
3. occurrence identity and resources are frozen;
4. it is not re-fit after capability enlargement; and
5. it closes the antecedent fibre without importing the target row.

## 5. Material `Z3` gauge-boundary application

This application reuses `HC-DU-040D`; it does not construct a new detector.

### Existing physical antecedent

The frozen gauge model plus:

- locality;
- exact QND source preservation;
- one minimal qutrit pointer; and
- additive record semantics

selects the controlled-add/subtract orbit:

\[
W_\pm
=
\sum_{f\in\mathbb Z_3}
\Pi_f\otimes S_P^{\pm f}.
\]

The gauge law does not select the pointer orientation.

### Three nested action families

#### \(\mathcal A_{\mathrm{source}}\)

The action family observes only the source flux sectors after the QND write.
Both \(W_+\) and \(W_-\) preserve the same source state. The antecedent selects
one response class even though it leaves a two-member implementation orbit.

This is a genuine positive:

```text
RAW IMPLEMENTATION PLURAL
RESPONSE CLASS SELECTED
```

#### \(\mathcal A_{\mathrm{pointer}}\)

Add one fixed pointer/controller convention. For source sector \(f=1\):

\[
W_+:\ 1\mapsto1,
\qquad
W_-:\ 1\mapsto2
\quad(\bmod 3).
\]

The orientation orbit splits. A material arrow, charge convention, or
calibrated pointer ordering selects one endpoint response class, but that
asymmetry is a supplied apparatus resource rather than a consequence of
Gauss law.

#### \(\mathcal A_{\mathrm{path}}\)

Add an admitted intermediate-time detector action. `HC-DU-040D` already proves
that:

\[
H_Q
=
H_0+\frac{2\pi}{\tau}Q
\]

can produce the same final write for different gauge-compatible projectors
\(Q\), while an intermediate action not commuting with \(Q\) distinguishes
the paths.

Material orientation therefore selects the final instrument response but not
the full multi-time process class. Fixing the oriented control schedule or
Hamiltonian path closes this finite class; the remaining inaccessible
dilation label can remain plural if every admitted tester annihilates its
difference.

### Gauge verdict

```text
gauge/QND/additivity
    -> source-response orbit selected

+ material orientation
    -> endpoint pointer/control response selected

+ physical path/control schedule
    -> admitted multi-time response class selected

microscopic dilation identity
    -> not required when tester-invisible
```

The source law selects only the first response orbit. It does not endogenously
select the complete feedback boundary.

## 6. Metastable host and reset-lineage application

This application reuses `HC-DU-043..046/054`.

### Existing physical antecedent

Freeze:

- the same host generator;
- the same write/turnover roles;
- the same terminal matter endpoint;
- the same reduced next-step law;
- the same reset command or semantic reset certificate; and
- total environmental retention.

Vary:

- whether the occurrence token is routed to an accessible archive or hidden
  reservoir; and
- whether a future-readable memory mode is physically reset or retains the
  prior epoch.

### Three nested action families

#### \(\mathcal A_{\mathrm{endpoint}}\)

The terminal matter state predicts the frozen next reduced-matter law in every
route/reset completion. The host antecedent selects this restricted response
class.

#### \(\mathcal A_{\mathrm{occurrence}}\)

Add a history/occurrence query at the declared archive port. The visible route
returns the retained `WRITE` fact; the hidden route returns no accessible
token. Archive relocation now crosses response classes.

Specifying the route closes this query, but the host generator does not choose
the observer boundary or archive access.

#### \(\mathcal A_{\mathrm{next\ cycle}}\)

Add one action capable of coupling to retained controller/environment memory
on the next cycle. A system-only reset command can leave:

```text
same matter endpoint
same reset label
same route
different future-readable memory
different next-cycle response.
```

The reset label therefore does not select the physical reset class.

### Reset completeness corollary

Let \(E\) be the memory outside the system-only reset surface. A reset premise
selects the future response class exactly when every two memory states left
compatible by the premise are equivalent under every admitted future action:

\[
\ker(A,\text{reset premise})
\subseteq
\ker\Sigma_{\mathcal A}.
\]

Equivalently:

> A complete reset need not identify every microscopic environmental state.
> It must fix every future-readable memory degree of freedom modulo future
> response-equivalence.

This is the minimum correct statement. “Reset every atom” is too strong.
“Issue a reset command” is too weak.

### Host verdict

```text
host endpoint
    -> reduced next-law response selected

+ archive route/access
    -> occurrence-query response selected

+ complete future-readable reset lineage
    -> repeated-cycle response class selected

future-invisible microstructure
    -> need not be selected
```

Again, the original host selects only a restricted class.

## 7. Preferred-foliation control

The held series premise remains an exactly compensated continuous preferred
foliation. The exact control uses two different linear extensions:

```text
source -> orientation -> reset -> control -> response
reset  -> orientation -> source -> control -> response
```

Source, orientation, and reset are independent causal parents of control.
Both extensions give the same complete boundary and response.

Therefore:

```text
FOLIATION_INERT
```

The selector theorem depends on physical causal parents and response
signatures, not privileged ranks among spacelike or otherwise independent
events. If a leaf rank changes the response, it has become an accessible
boundary variable and the model has left exact compensation.

## 8. Strongest prior-art collision

The mathematical core is already established in several native languages:

- behavioral systems and bisimulation identify systems by their possible
  externally relevant trajectories rather than one internal representation;
  Tabuada gives a general controller-synthesis treatment of bisimulation
  equivalence across multiple system classes
  ([primary source](https://arxiv.org/abs/0706.0929));
- quantum combs represent multi-step networks and quantum testers represent
  the procedures that discriminate them; the response-class object is a
  restricted operational quotient of that framework
  ([primary source](https://arxiv.org/abs/0904.4483));
- process tensors are designed to encode arbitrary multi-time responses under
  experimentally chosen interventions, including detectable memory effects
  ([primary source](https://arxiv.org/abs/1512.00589));
- the material gauge specimen's regional-center and boundary-mode caveats are
  standard gauge-theory terrain
  ([Casini--Huerta--Rosabal](https://arxiv.org/abs/1312.1183);
  [Riello](https://arxiv.org/abs/2010.15894)).

Thus the theorem is not novel mathematics and is not a new quantum or control
law.

The Dynamic Unity contribution at this grade is the typed placement:

1. physical antecedent selection and target transfer are separate fibre tests;
2. microscopic uniqueness is not required;
3. action-envelope growth refines the required selected class;
4. archive routing and reset lineage are physical boundary variables exactly
   when future actions can read them; and
5. an operational quotient is not automatically a formed material record.

## 9. Exact regression

The regression:

- checks the selector theorem and raw-identity positive control;
- realizes response-partition counts \(1\to2\to4\) in both specimens;
- verifies the orientation, path, route, and reset first leaks;
- verifies that future-invisible microscopic tags remain operationally
  irrelevant;
- rejects a semantic reset certificate as a physical reset selector; and
- preserves every verdict under the matched linear-extension control.

It passes:

```text
21 / 21
```

See:

- [probe](../tests/du_feedback_boundary_selection_probe.py);
- [artifact](../tests/artifacts/du_feedback_boundary_selection_result.json).

The probe is an exact partition regression for already derived relations. It
is not a simulation or an independent physical experiment.

## 10. What is earned

| Result | Grade/status |
|---|---|
| Response-class selector iff kernel inclusion | exact scoped theorem; known factorization mathematics |
| Capability enlargement refines response-equivalence | exact scoped theorem; known monotonicity |
| Microscopic identity is unnecessary | exact positive control |
| Gauge law/QND/additivity selects source-only response orbit | conditional reuse of `HC-DU-040D` |
| Material orientation selects final pointer/control class | conditional physical premise; supplied |
| Intermediate tester splits endpoint-identical formation paths | exact existing witness; known multi-time distinction |
| Host endpoint selects reduced next-law class | exact existing positive control |
| Occurrence action exposes archive relocation | exact existing witness |
| Next-cycle action exposes incomplete reset | exact finite witness |
| Complete reset fixes all future-readable memory modulo behavior | exact scoped necessity statement |
| Existing antecedent endogenously selects complete interface | **not earned** |
| New physical law, prediction, ontology, or paper | **not earned** |
| Preferred foliation changes the verdict | **no; inert** |

## 11. Counter-assumptive findings

Three durable corrections follow:

1. A physical antecedent need not select microscopic implementation identity;
   response-class selection is sufficient.
2. Selection at one capability envelope does not automatically survive a
   richer action family.
3. A reset command or certificate does not establish complete reset; every
   future-readable memory class must be fixed or screened.

These are added as `NI-DU-93..95`.

## 12. Position-4 handoff

Position 3 is complete. It does not justify another apparatus or archive build.
It does sharpen the next hostile audit.

Activate:

```text
N5-PF-P4
Regional Finality and Excess-Content Hostile Audit
```

The three candidates remain:

1. a finality-rate bound distinct from \(c\);
2. complementarity derived from physical record mergeability; and
3. universal critical exponents for decoherence/finality thresholds.

For each candidate, Position 4 must now freeze:

- the complete physical adapter;
- the response-equivalence class it claims to select;
- the action/capability envelope;
- the matched standard-physics null;
- the first route/reset/orientation field that could reopen the class; and
- the retreat cost if no excess content survives.

Position 4 is worth running precisely because it is a kill-or-residual audit,
not another attempt to manufacture a record host. Position 5 remains
conditional.

## 13. Final verdict

The exact question was not:

> Does physics uniquely specify every microscopic implementation?

It was:

> Does the independently motivated physical antecedent constrain all allowed
> implementations to one complete future-response class?

For the reused Dynamic Unity specimens:

```text
YES
    for restricted source/endpoint action families

NO
    after orientation, formation-path, occurrence-access, or reset-memory
    capabilities are admitted

CONDITIONALLY YES
    after those physical fields are explicitly fixed, even while
    future-invisible microstructure remains plural

NOT ENDOGENOUSLY YES
    because the current source/host antecedents do not derive the additional
    orientation, route, path, access, or reset-lineage premises
```

That is the scoped Position-3 result.
