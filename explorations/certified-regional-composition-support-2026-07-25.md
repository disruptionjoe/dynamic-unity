---
title: "Certified regional composition support — typed defects, recursive bounds, and refinement counterexample"
status: completed_exact_control
doc_type: exploration_and_executed_support_result
created: 2026-07-25
run_id: RUN-20260725-100452-record-formation-certified-composition
claim_grade: "EXACT FINITE TYPED COMPOSITION CONTROLS / COMPONENT MATHEMATICS KNOWN / PHYSICAL REGIONAL COMPOSITION OPEN"
banked: false
seeded: false
---

# Certified regional composition support

## Result in plain English

Once record interfaces have been independently formed, recursive regional
composition cannot be summarized by one “finality” number. It needs three
separately typed receipts:

\[
\mathcal D=(\iota_T,\Omega_{\mathcal C},\alpha_U),
\]

where:

- \(\iota_T\) measures whether two alleged copies are identical at the
  declared type \(T\);
- \(\Omega_{\mathcal C}\) records whether all context marginals admit one
  global extension, or carries the obstruction when they do not; and
- \(\alpha_U\) measures whether the exported certificate preserves the
  declared upper-layer action \(U\).

Identity and action errors obey tight triangle bounds. Marginal compatibility
does not: it must be recomputed on the entire glued cover. Exact agreement on
every overlap can coexist with failure of a global composite.

The deterministic probe passes `22/22` checks:

- [probe](../tests/du_recursive_record_composition_probe.py)
- [artifact](../tests/artifacts/du_recursive_record_composition_result.json)

This is downstream composition mathematics. It does not physically select a
region, interface, observer, cover, or record law.

## 1. Weakest warranted overlap identity

Let \(O\) be a finite set of record occurrences. Let \(E\) be an independently
formed equivalence relation supplied by provenance or a frozen interface. For
each required identity type \(t\), let

\[
\sigma_t:O\rightarrow Z_t
\]

be a predeclared signature, such as outcome effect, instrument, multi-time
history, provenance, or supported upper action. Define

\[
E_T=E\cap\bigcap_{t\in T}\ker\sigma_t.
\]

**Maximal typed-identity theorem.** \(E_T\) is the unique greatest equivalence
relation contained in \(E\) that is sound for every type in \(T\).

The proof is immediate: kernels and their intersections are equivalence
relations; every other sound relation inside \(E\) is contained in every
kernel and hence in \(E_T\). The probe verifies the universal property across
all 15 partitions of a four-occurrence fixture.

“Weakest warranted” therefore means:

1. require only the identity type needed by the next composition; then
2. take the greatest quotient licensed by independent evidence at that type.

Two records may be effect-identical while differing as instruments, histories,
or action resources. The theorem filters a supplied \(E\); it cannot make a
desired overlap identity become physically formed.

For typed binary responses \(p_0,\ldots,p_n\), total variation gives

\[
\iota(p_0,p_n)\leq\sum_j\iota(p_j,p_{j+1}).
\]

The probe saturates this at \(0,\frac14,\frac12\). Common stochastic
postprocessing contracts the discrepancy, and inserting a zero-defect relay
preserves the bound.

## 2. Global compatibility is not pairwise compatibility

For an acyclic cover \(AB,BC\) whose \(B\) marginals agree, an exact global
extension is

\[
p(a,b,c)=
\begin{cases}
\dfrac{p_{AB}(a,b)p_{BC}(b,c)}{p_B(b)},&p_B(b)>0,\\
0,&p_B(b)=0.
\end{cases}
\]

Thus a join tree supports exact recursive gluing.

A three-cycle gives the decisive counterexample. Take deterministic pair
records

\[
A=B,\qquad B=C,\qquad C\neq A,
\]

each with uniform one-variable marginals. Every pair distribution is valid,
sharp, and agrees exactly on every overlap, yet no global assignment exists.
Overlap identity licenses the gluing question; it does not answer it.

This is standard marginal/descent/contextuality terrain, not new physics. Its
value here is architectural: a regional-composition receipt must retain a
full-cover extension result or obstruction rather than infer globality from
pairwise certificates.

## 3. Benign subdivision refutes a naive scalar defect

For deterministic odd parity data on an \(n\)-cycle, the exact
\(L_\infty\) distance to the even-parity polytope is

\[
\delta_\infty=\frac1n.
\]

The lower bound follows from the violated odd-set functional: changing each
of \(n\) edge expectations by at most \(\varepsilon\) can repair the violation
by at most \(n\varepsilon\). The upper bound is achieved by mixing the \(n\)
even vectors obtained by flipping one edge at a time.

Now subdivide one edge of the inconsistent triangle by inserting an inert
deterministic relay. The global-extension verdict, solution count, and
\(\mathbb Z_2\) obstruction are unchanged, but the raw scalar changes from
\(1/3\) to \(1/4\).

Therefore an unweighted per-edge scalar is not natural under benign
refinement. Recursive composition should transport one of:

- the obstruction class;
- the full primal/dual extension receipt; or
- a weighted quantity proved natural under the declared refinement map.

Otherwise the measured “regional defect” can be an artifact of diagram
subdivision rather than physical structure.

## 4. Action certificates need not disclose histories

Let a history \(h\in H\) be mapped to a certificate \(c=f(h)\), and let an
upper action be \(u:H\to A\). The action survives the interface exactly when
there is a \(\bar u\) such that

\[
u=\bar u\circ f.
\]

Equivalently, \(u\) is constant on every certificate fiber. This separates:

- certificate content;
- supported action;
- underlying history; and
- disclosure or identification of that history.

The finite control uses eight three-bit histories. An inner certificate
retains parity plus one tag and has fibers of size two; an outer certificate
retains parity alone and has fibers of size four. Neither identifies a
history. Parity-dependent action factors exactly through both layers, while
a hidden-bit action has unavoidable error \(1/2\).

For two approximate action interfaces,

\[
\alpha_{U_2\circ U_1}\leq\alpha_{U_1}+\alpha_{U_2},
\]

and the probe gives a tight \(\frac14+\frac14=\frac12\) example.

This is functional non-disclosure, not zero-knowledge security. No simulator,
adversary class, leakage bound, or cryptographic soundness claim is supplied.
Its role is to prevent Dynamic Unity from equating “certificate sufficient
for an action” with “history exported or ontically identified.”

## 5. Why the defect must stay vector-valued

Finite product fixtures realize every zero/nonzero pattern of
\((\iota_T,\Omega_{\mathcal C},\alpha_U)\). None of the coordinates determines
the others:

- exact identity can accompany a global marginal obstruction;
- a global marginal can exist while the certificate loses the upper action;
- action can be preserved without disclosing the underlying history; and
- approximate identity need not imply either marginal failure or action loss.

Identity and action are path-subadditive. Marginal compatibility is a
full-cover property. Collapsing these into one scalar loses the composition
law the scalar is supposed to summarize.

## 6. Quantum-strength bridge and novelty grade

The construction does **not** strengthen probability-level Local
Orthogonality and does not exclude the almost-quantum set. Formed interfaces
plus typed overlap identity do not by themselves imply pairwise-to-global
instrument compatibility.

For general POVMs or instruments, pairwise compatibility can fail to extend
globally—the relevant Specker terrain. For finite sharp PVMs on a common
Hilbert space, pairwise commutation already yields a joint spectral measure;
that case is absorbed by standard theory. Any stronger Dynamic Unity bridge
would have to derive, rather than assume, the common-system identity and the
needed sharpness, repeatability, nondisturbance, or instrument structure.

Known component mathematics includes equivalence kernels, total-variation
bounds, join-tree gluing, marginal obstructions, parity polytopes,
cohomological/contextual descriptions, action sufficiency, zero-knowledge
distinctions, and QEC logical-access distinctions.

The useful Dynamic Unity increment is the combined typed contract:

1. maximal safe identity inside independently formed evidence;
2. nonlocal full-cover marginal receipt;
3. recursive action-factorization receipt;
4. explicit history-nondisclosure type; and
5. a sharp inert-refinement counterexample to naive scalar naturality.

That synthesis is an exact program control, not yet a novel theorem claim or
physical regional-composition law.

## Recommended integration

- Support `HC-DU-035C`, `H-CCR-16`, and `CONCEPT-DU-011` at exact
  finite-control grade.
- Preserve the three-coordinate defect rather than introduce a scalar
  finality score.
- Make inert-subdivision naturality a mandatory check.
- Type certificate content separately from history disclosure.
- Keep the almost-quantum/Specker/PVM bridge as an absorber gate.
- Add no physical claim, prediction, ontology, or paper priority from this
  control alone.
