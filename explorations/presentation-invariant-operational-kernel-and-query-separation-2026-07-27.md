---
title: "Presentation-invariant operational kernel and object-query separation"
date: 2026-07-27
status: banked
work_id: N5-CCR-BS-P3-KERNEL
claim_id: HC-DU-059
claim_grade: "GRADE 4 — SCOPED FACTORIZATION, COMPRESSION, AND CONTRACT-DEPENDENCE THEOREM; MATHEMATICAL CORE ABSORBED"
maximum_grade: "grade 4; no new physics, ontology, physical remainder, prediction, or unique field basis"
primary_returns:
  - REDUNDANT_OR_DERIVABLE_FIELD
  - CONTRACT_DEPENDENT_MINIMALITY
  - ABSORBED_SCHEMA_ONLY
observer_index_return: OBSERVER_INDEX_DERIVABLE_FROM_ACCESS_ACTION
position_4_gate: CLOSED_NO_TRANSFERABLE_NOVEL_DELTA
portfolio_return: NORTH_STAR_PORTFOLIO_RESET
preferred_foliation_status: "off; not assumed, tested, or reopened"
hardware_status: "not needed"
---

# Presentation-invariant operational kernel and object-query separation

## Plain-English result

The seven-part `HC-DU-058` bundle is a useful checklist, but it is **not a
uniquely minimal set of physical ingredients**.

Three corrections decide the question.

1. What is invariant is not the number or names of fields. It is the
   **partition of admissible physical histories into cases that no declared
   observer action can distinguish**. Lossless repackaging can turn two
   individually necessary coordinates into one informative coordinate and
   one constant coordinate without changing any operational fact.
2. A held-out target cannot serve both as physical input and as the question
   used to test whether the input is sufficient. If the complete process
   already determines the target, the target field is redundant. If it does
   not, the target belongs outside the bundle as an adjudication query.
3. “Finality/fault contract” likewise mixes a supplied rule with a derived
   verdict. A physically carried finality certificate belongs in the formed
   record or process. The rival/fault rule used to judge it is an external
   query. The verdict is calculated from the two.

The strongest corrected architecture is therefore:

```text
fixed antecedent contract
    model/completion class + gauge/equivalence
    + representation category + occurrence identity

physical/interface description
    complete process + formed record/provenance
    + observer-operational contract(access, actions, resources)

external adjudication query
    target family + equivalence/tolerance
    + rival/fault/finality rule

derived result
    reconstruction/finality/remainder verdict
```

This is a real correction to Dynamic Unity's formal discipline. It is not a
new theorem of mathematics or a new law of physics.

## 1. Frozen type contract

Let:

- \(X\) be one frozen admissible completion or occurrence class;
- \(G\) be the declared gauge/representation equivalence already absorbed
  into \(X\), or carried explicitly when needed;
- \(\omega_i:X\to Y_i\) be typed fields;
- \(\Omega=(\omega_1,\ldots,\omega_n):X\to\prod_iY_i\) be their joint
  signature; and
- \(\mathcal T=\{\tau_\alpha:X\to Z_\alpha\}\) be the fixed family of
  observer-accessible held-out questions.

For any map \(u\), define its kernel equivalence

\[
\ker(u)=\{(x,x')\in X^2:u(x)=u(x')\}.
\]

For a family of maps, use the intersection of their kernels. Thus

\[
\ker(\Omega)=\bigcap_i\ker(\omega_i),
\qquad
\ker(\mathcal T)=\bigcap_\alpha\ker(\tau_\alpha).
\]

This is a set-level statement. Stochastic and quantum versions replace
point-valued output by equality of the complete admitted response kernel or
process-tensor statistics. The model class, admissible instruments, resource
contract, and equality tolerance must be frozen before applying it.

## 2. Operational-kernel theorem

### Theorem 1 — target-relative sufficiency

Every target in \(\mathcal T\) factors through \(\Omega\) if and only if

\[
\ker(\Omega)\subseteq\ker(\mathcal T).
\]

### Proof

If \(\tau_\alpha=d_\alpha\circ\Omega\), equal \(\Omega\)-values imply equal
\(\tau_\alpha\)-values, so the kernel inclusion follows.

Conversely, if each target is constant on every \(\Omega\)-fibre, define
\(d_\alpha\) on \(\operatorname{im}\Omega\) by

\[
d_\alpha(\Omega(x))=\tau_\alpha(x).
\]

Kernel inclusion makes this definition independent of the chosen
representative. Hence \(\tau_\alpha=d_\alpha\circ\Omega\). \(\square\)

### Consequence

There is no target-independent notion of a complete record or complete
operational description. Completeness is always relative to:

- an admitted completion class;
- an observer/action/resource envelope;
- a target family; and
- a declared equality or error contract.

This sharpens, rather than changes, the fibre criterion already used
throughout Dynamic Unity.

## 3. Derivability and redundancy

Write \(\Omega_{-i}\) for the joint signature with field \(i\) removed.

### Theorem 2 — field derivability

Field \(\omega_i\) is naturally derivable from the other named fields on the
frozen domain exactly when

\[
\ker(\Omega_{-i})\subseteq\ker(\omega_i).
\]

It is logically independent of the other named fields exactly when there is
a witness pair \(x,x'\) such that

\[
\Omega_{-i}(x)=\Omega_{-i}(x'),
\qquad
\omega_i(x)\ne\omega_i(x').
\]

Field derivability is stronger than target-relative redundancy. Field \(i\)
is redundant only for target family \(\mathcal T\) when

\[
\ker(\Omega_{-i})\subseteq\ker(\mathcal T),
\]

even if \(\omega_i\) is not reconstructible.

These distinctions prevent three common overclaims:

1. “not derivable” does not mean “needed for this target”;
2. “needed for this target” does not mean “fundamental”; and
3. “every named field has a witness” does not make the naming
   representation-invariant.

## 4. The exact presentation counterexample

Let

\[
X=\{(0,0),(0,1),(1,0),(1,1)\}
\]

and let

\[
\omega_1(x,y)=x,\qquad \omega_2(x,y)=y.
\]

Neither named field derives the other. Both are individually necessary for
the identity signature.

Now define

\[
\zeta_1(x,y)=(x,y),\qquad \zeta_2(x,y)=0.
\]

Then

\[
\ker(\omega_1,\omega_2)=\ker(\zeta_1,\zeta_2),
\]

but \(\zeta_2\) is constant and therefore redundant. No operational
distinction changed; only the field presentation changed.

Even after forbidding a constant dummy coordinate, the named basis remains
nonunique. The invertible recoding

\[
\eta_1(x,y)=x,\qquad \eta_2(x,y)=x\oplus y
\]

preserves the joint kernel and leaves both coordinates independent. It does
not preserve their names or interpretations.

Therefore:

> Coordinate count and coordinate-wise minimality are not invariant under
> arbitrary lossless representation changes. Minimality becomes meaningful
> only after the field types and admissible type-preserving transformations
> are frozen.

The exact executable certificate is
[`tests/du_kernel_minimality_probe.py`](../tests/du_kernel_minimality_probe.py);
its checked output is
[`du_kernel_minimality_result.json`](../tests/artifacts/du_kernel_minimality_result.json).

## 5. The canonical target-relative object

For the frozen target family, define operational equivalence

\[
x\sim_{\mathcal T}x'
\quad\Longleftrightarrow\quad
\tau_\alpha(x)=\tau_\alpha(x')
\ \text{for every }\alpha.
\]

Then

\[
X/{\sim_{\mathcal T}}
\]

is the coarsest exact target-sufficient quotient. Every exact
target-sufficient signature refines it, and any two concrete encodings of
this quotient differ only by a lossless relabeling of quotient classes.

This quotient is the presentation-invariant **operational kernel** that the
seven-field checklist was trying to protect.

It does not by itself establish that:

- the quotient is physically formed as a record;
- nature selects one encoding, archive, or access route;
- the query family is complete for all future capabilities; or
- the quotient is fundamental ontology.

Those are separate Dynamic Unity questions.

## 6. Object-query separation

The original bundle was

\[
\Omega=(\mathcal P,r,a,f,c,h,t),
\]

where:

- \(\mathcal P\) is the complete multi-time process;
- \(r\) is formed record and provenance;
- \(a\) is access and admissible intervention structure;
- \(f\) is finality under a rival/fault contract;
- \(c\) is the capability/action envelope;
- \(h\) is resource accounting; and
- \(t\) is the held-out target.

### 6.1 The target is derived or external

`HC-DU-058` already states that an observer-accessible target contained in
the complete process signature descends whenever the process descends.
Therefore exactly one of two cases holds:

1. **Readout case.** \(t=d\circ\mathcal P\). Then adding \(t\) to the
   physical bundle does not refine its fibres. It is derivable.
2. **Held-out case.** No such decoder exists. Then \(t\) is the question
   testing whether the physical/interface bundle is complete. Putting it
   inside that bundle would assume the answer.

The explicit target remains valuable in an audit ledger. It should not be
counted as an independent physical coordinate.

### 6.2 Finality splits into carrier, rule, and verdict

The same correction applies to \(f\):

- a physical certificate, archive state, or irreversible response belongs
  in \(r\) or \(\mathcal P\);
- a physically instantiated noise, failure, or adversary mechanism belongs
  in \(\mathcal P\) or the observer/resource contract;
- the rival class, fault model, tolerance, horizon, and policy are supplied
  adjudication parameters when they specify what is being certified against;
  and
- the finality verdict is derived by evaluating the physical state under
  that rule.

If two systems carry the same physical certificate but are judged under
different fault models, the different verdict does not prove a different
physical state. If the certificate changes future dynamics, that physical
feedback belongs in the process and record descriptions.

### 6.3 Observer indexing is operational

Dynamic Unity defines an observer by the physical role specifying:

- accessible records and provenance;
- admissible interventions;
- available actions and risks;
- resource boundaries; and
- meaningful target questions.

The first four live in the observer-operational contract

\[
O=(a,c,h),
\]

while the target family remains the external query. A separate personal
identity token can vary without changing any declared operational result. It
is metadata unless a physical difference carried by that token changes
\(\mathcal P\), \(r\), \(a\), \(c\), or \(h\).

Return:

```text
OBSERVER_INDEX_DERIVABLE_FROM_ACCESS_ACTION
```

This means derivable from the **typed operational role**, including its
resource boundary. It does not mean consciousness or personal identity is
reduced to one access bit.

## 7. Field-by-field witness-reuse audit

The existing evidence decides the roles without seven new fixtures.

| Candidate field | Reused exact witness | What is earned | Disposition |
|---|---|---|---|
| complete process \(\mathcal P\) | `HC-DU-055`'s same lossy control label with identity-versus-\(Z\) phase-sensitive held-out response | A lossy record/control label does not derive the complete process | role-distinct when the process type excludes the missing response |
| formed record/provenance \(r\) | `HC-DU-054`'s accessible-versus-hidden archive routing with the same claimed host/source antecedent | Host dynamics need not select the accessible formed interface | independent if \(\mathcal P\) omits typed record formation; a projection if it includes it |
| access/interventions \(a\) | `HC-DU-054/056`'s accessible/hidden sidecar and route/action staircases | Equal retained values can support different intervention surfaces | retain inside the observer-operational contract |
| finality/fault \(f\) | `HC-DU-055/057`'s separation of carrier, physical feedback, fault model, protocol, and verdict | Finality is not one intrinsic field | split physical carrier from external rule and derived verdict |
| capability/actions \(c\) | `HC-DU-054/056`'s first capability enlargement reopening a previously sufficient fibre | Sufficiency is action-relative | retain inside the observer-operational contract |
| resources \(h\) | `HC-DU-054`'s stronger full-access/tomographic repair and matched-resource boundary | Enlarged resources can change the admitted response class without changing the old record | retain as a typed contract parameter; it may refine action typing |
| held-out target \(t\) | `HC-DU-058`'s complete-process descent statement | The target is either a process readout or an external test | remove from the independent physical basis |

This matrix proves **role separation**, not a universal coordinate basis.
Whether \(r\) is a projection of \(\mathcal P\), or \(h\) is included in the
type of \(c\), depends on the model category. That is the exact
contract-dependence result.

## 8. Corrected compact contract

The smallest honest role decomposition is:

\[
A_0=(X,G,\mathsf{Rep},\mathsf{Occ}),
\]

where \(A_0\) freezes the completion class, gauge/equivalence, admissible
representation maps, and occurrence identity;

\[
D=(\mathcal P,r,O),\qquad O=(a,c,h),
\]

where \(D\) describes the physical process, formed interface, and
observer-operational role; and

\[
Q=(\Phi,\mathcal T),
\]

where \(\Phi\) is the rival/fault/finality adjudication rule and
\(\mathcal T\) is the held-out target family.

The verdict is

\[
V=\operatorname{Eval}(A_0,D;Q).
\]

This decomposition is recommended because it prevents circular tests. It is
**not** claimed to be a uniquely minimal universal field basis. Inside a
frozen category, fields may be split or combined when the type contract
permits it. The invariant is the joint response equivalence they induce.

## 9. Strongest absorber collision

The mathematical content is occupied from several directions:

1. **Sufficient statistics.** Minimal sufficiency is relative to an
   experiment and decision/parameter family, and concrete minimal statistics
   are identified only up to lossless transformation. Bahadur's abstract
   treatment also shows that minimal sufficient statistics need not exist in
   unrestricted settings.
2. **Minimal realization.** Kalman's realization theory identifies the
   controllable and observable part of a linear system from fixed
   input/output behavior, only up to similarity—not a uniquely named state
   coordinate basis.
3. **Database dependencies.** Armstrong-style functional dependencies decide
   when an attribute follows from others after a schema and dependency theory
   are fixed. Covers and presentations need not be unique.
4. **Category theory.** A product or universal object is characterized up to
   the relevant isomorphism, not by one privileged set of coordinate names.
5. **Dynamic Unity's own earlier results.** Fibre factorization,
   response-equivalence selection, capability refinement, and
   implementation-versus-state sufficiency already supply the application
   machinery.

Primary references:

- R. E. Kalman, [“Mathematical Description of Linear Dynamical
  Systems”](https://doi.org/10.1137/0301010) (1963).
- R. R. Bahadur, [“Sufficiency and Statistical Decision
  Functions”](https://doi.org/10.1214/aoms/1177728715) (1954).
- W. W. Armstrong, [“Dependency Structures of Data Base
  Relationships”](https://dblp.org/rec/conf/ifip/Armstrong74) (1974).
- Saunders Mac Lane, [*Categories for the Working
  Mathematician*](https://books.google.com/books?id=gfI-BAAAQBAJ).

Return:

```text
ABSORBED_SCHEMA_ONLY
```

That return applies to any claim that Dynamic Unity has discovered a unique
seven-coordinate mathematical basis. It does not erase the scientific need
to freeze complete process, formation, access, action, resource, and query
roles before making reconstruction claims.

## 10. Exact verdict

```text
HC-DU-059

REDUNDANT_OR_DERIVABLE_FIELD
  held-out target is derived from the complete process or belongs outside
  the physical input bundle

CONTRACT_DEPENDENT_MINIMALITY
  record-versus-process and resource-versus-action separations depend on
  the frozen typed model category

ABSORBED_SCHEMA_ONLY
  joint-kernel and minimal-quotient mathematics is established

OBSERVER_INDEX_DERIVABLE_FROM_ACCESS_ACTION
  no extra observer-token coordinate is needed beyond the typed
  observer-operational role

PRESENTATION_INVARIANT_SURVIVOR
  the joint operational response kernel / target-relative quotient
```

No all-seven-equal physical counterexample was needed. The claim of a
uniquely minimal seven-field basis is already killed by one derivable field
and by exact representation dependence.

## 11. North-Star consequence

Dynamic Unity should ask:

> Relative to a frozen physical completion class and an independently
> declared observer/action/resource/query contract, what is the coarsest
> response-equivalence quotient that preserves every admitted
> observer-accessible result; is that quotient physically formed and
> selected as a record; and does any finite result remain outside it?

This is sharper than asking whether seven named fields are minimal.

It preserves the program's highest-ceiling question:

> Does a physically selected certified causal record network reconstruct
> everything an observer can experience and do, or leave a finite physical
> remainder?

## 12. Routing decision

Position 4 does not open. The surviving invariant is valuable formal hygiene,
but its mathematics is fully absorbed and supplies no nontrivial unchanged
delta to test in a second arena.

The sequence therefore routes directly to:

```text
NORTH_STAR_PORTFOLIO_RESET
```

That reset must consume the corrected object/query architecture. It must not
reopen preferred foliation, construct another record host, promote a paper,
or infer new physics from this theorem.

## 13. Non-promotions

This swing does not:

- derive a physical record or observer;
- prove records create reality;
- establish a unique ontology or state basis;
- find a physical remainder;
- create a new law, dynamics, coefficient, or prediction;
- reopen preferred foliation;
- create a paper candidate;
- require simulation, hardware, provider access, or external collaboration;
  or
- change another repository.
