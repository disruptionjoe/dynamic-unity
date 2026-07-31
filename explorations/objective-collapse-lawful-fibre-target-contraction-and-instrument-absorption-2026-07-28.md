---
title: "Objective-collapse lawful-fibre target contraction and instrument absorption"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-082
run_id: RUN-20260728-140136-objective-collapse-lawful-fibre-target
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260728-140136-objective-collapse-lawful-fibre-target/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-140136-objective-collapse-lawful-fibre-target/run-receipt.md"
owner_repo: dynamic-unity
---

# Objective-collapse lawful-fibre target contraction and instrument absorption

## Executive result

Swing 3 returns:

```text
chairman_return:
  LAW_ONLY_ABSORPTION

typed_scope:
  LAW_PLUS_SUPPLIED_INSTRUMENT_DETERMINES_CONDITIONAL_KERNEL

operational_effect:
  RECORD_CAN_STRICTLY_REDUCE_SITUATED_PREDICTION_RISK

realized_history:
  SAME_RECORD_DIFFERENT_FUTURE_RESPONSE_REMAINS

universal_sufficiency:
  OUTCOME_LABEL_NOT_A_UNIVERSAL_SUFFICIENT_STATISTIC

dynamic_unity_excess:
  NONE_BEYOND_GRW_AND_GENERIC_INSTRUMENT_FORMALISM
```

In plain English:

> Reading a formed GRW outcome can genuinely help an observer predict a later
> response. It selects the appropriate conditional branch instead of leaving
> the observer with the unconditional mixture. But this is not a new
> Dynamic Unity record law. Once the initial state and both supplied
> experiments are fixed, the standard GRW law of superoperators already
> calculates the joint distribution, the conditional post-experiment state,
> and every later outcome probability. The record tells the observer which
> already-defined conditional kernel applies; it does not add a new physical
> selection principle.

The result is nevertheless not “nothing.” It establishes three exact
boundaries:

1. a non-copying outcome record can strictly lower prediction risk;
2. it does not determine the later realized stochastic event; and
3. the outcome symbol is sufficient only relative to the frozen preparation,
   instrument, downstream action, and access boundary.

Because standard GRW formalism supplies the whole positive result, the
objective-collapse campaign stops here under its pre-registered rule.

## 1. Frozen types

Keep the Swing-2 qualifier unchanged:

\[
\Theta_o
=
(L_{\rm GRW},PO_o,A_1,\zeta_o,X_A),
\qquad
o\in\{f,m\}.
\]

Here:

- \(L_{\rm GRW}\) is the collapse dynamics;
- \(PO_o\) is the flash or matter-density primitive ontology;
- \(A_1\) is the supplied first apparatus and interaction;
- \(\zeta_o\) maps the ontology-native late pattern to outcome \(Z\);
- \(X_A\) is the supplied bounded readout coupling.

Also freeze:

- initial system density matrix \(\rho\);
- first-experiment outcome maps \(\{\mathcal C_z\}\);
- post-record intervention/evolution \(\mathcal S\);
- later apparatus with outcome maps \(\{\mathcal D_t\}\);
- response alphabet \(t\in\{0,1\}\);
- zero-one prediction loss; and
- no access to the complete flash history, environment, controller, or
  target-specific hidden channel.

The target is the distribution of \(T\), a later apparatus response. It is
not the first pointer value and is not a provenance question.

## 2. The source already contains the sequential theorem

Goldstein, Tumulka, and Zanghì's GRW formalism associates a POVM and a family
of completely positive superoperators with every supplied experiment. It
also treats consecutive experiments and conditional density matrices.

For the first experiment:

\[
p_z=\Pr(Z=z)=\operatorname{tr}\mathcal C_z(\rho),
\]

and, for \(p_z>0\), the conditional post-experiment state is:

\[
\rho_z
=
\frac{\mathcal C_z(\rho)}
{\operatorname{tr}\mathcal C_z(\rho)}.
\]

For a fixed intervening evolution \(\mathcal S\) and second experiment:

\[
\Pr(Z=z,T=t)
=
\operatorname{tr}
\left[
\mathcal D_t\mathcal S\mathcal C_z(\rho)
\right],
\tag{1}
\]

\[
\Pr(T=t\mid Z=z)
=
\operatorname{tr}
\left[
\mathcal D_t\mathcal S(\rho_z)
\right].
\tag{2}
\]

Marginalizing gives:

\[
\Pr(T=t)
=
\sum_z
\operatorname{tr}
\left[
\mathcal D_t\mathcal S\mathcal C_z(\rho)
\right].
\tag{3}
\]

Equations (1)--(3) are the whole record-to-target calculation. They are
already consequences of the GRW experiment formalism once the experiment is
supplied. Dynamic Unity did not derive a new collapse prediction.

This also fixes an ambiguity in the phrase “law only”:

```text
bare collapse law
  -> does not select the apparatus or calibration;

collapse law + supplied experiment
  -> determines the joint and conditional operational kernels;

realized accessible outcome Z
  -> tells the situated observer which conditional kernel applies.
```

Calling the first line sufficient would overattribute interface selection to
the law. Calling the third line physically empty would erase the genuine
observer-relative information gain. The correct verdict is
**law-plus-supplied-instrument absorption**.

## 3. Exact non-copying positive control

The smallest exact control uses a two-state system. It tests the logic of the
instrument result; it is not claimed as a microscopic numerical solution of a
specific GRW apparatus.

Prepare:

\[
\rho=|+\rangle\langle+|.
\]

Let the first supplied instrument have:

\[
\mathcal C_z(X)=P_zXP_z,
\qquad
P_z=|z\rangle\langle z|,
\qquad
z\in\{0,1\}.
\]

Then:

\[
\Pr(Z=0)=\Pr(Z=1)=\frac12,
\qquad
\rho_z=|z\rangle\langle z|.
\]

Apply the fixed nontrivial intervention:

\[
R_y(\pi/3)
\]

and read a separate later \(Z\)-basis pointer \(T\). The result is:

\[
\Pr(T=Z\mid Z)=\cos^2(\pi/6)=\frac34,
\]

\[
\Pr(T\neq Z\mid Z)=\frac14.
\]

Without reading \(Z\), \(T\) is uniform. Therefore:

\[
\mathcal R_{\rm no\ record}^{*}=\frac12,
\qquad
\mathcal R_{\rm record}^{*}=\frac14
\]

under zero-one loss. The record strictly halves the Bayes error. It also
carries:

\[
I(Z;T)
=
1-h_2(1/4)
\approx0.188722
\]

bits about the later response.

This target is not a copy of the first outcome: even after \(Z\) is known,
the later response remains stochastic with error \(1/4\).

## 4. Why prediction improves without exact reconstruction

There are two different target questions.

### Predictive target

The observer wants the conditional distribution of \(T\). When the kernels
\(\Pr(T\mid Z=z)\) differ across \(z\), learning \(Z\) can strictly improve a
proper score or decision risk. The positive control proves this can occur.

### Realized-history target

The observer wants the actual later value \(T(m)\) on an individual lawful
history \(m\). In the positive control:

\[
H(T\mid Z)=h_2(1/4)>0.
\]

Thus every record fibre with nonzero probability contains lawful histories
with the same \(Z\) and different \(T\). The record contracts predictive
uncertainty but does not make the future event a constant of the record
fibre.

Consequently:

```text
strict risk contraction
  != exact realized-target reconstruction
  != provenance reconstruction
  != interface selection.
```

This is why the formal return is not
`RECORD_ASSISTED_TARGET_RECONSTRUCTION`.

## 5. Exact sufficiency boundary

Let \(h\) range over admitted hidden histories or preparations that produce
the same accessible outcome \(z\), and let \(\sigma_{z,h}\) be the retained
conditional system state at the start of the downstream action.

For a declared future action/effect class \(\mathcal A\), outcome \(z\) is a
sufficient statistic exactly when:

\[
\operatorname{tr}
\left[E(\sigma_{z,h}-\sigma_{z,h'})\right]
=0
\]

for every \(h,h'\) with outcome \(z\) and every \(E\in\mathcal A\).

If \(\mathcal A\) is tomographically complete, this reduces to:

\[
\sigma_{z,h}=\sigma_{z,h'}
\quad
\text{for all admitted }h,h'.
\tag{4}
\]

The necessity of (4) is exact. If:

\[
\Delta=\sigma_{z,h}-\sigma_{z,h'}\neq0,
\]

then the projector onto the positive spectral subspace of \(\Delta\) is an
effect whose response probabilities differ. The two histories have the same
outcome record but a different held-out target law.

For one frozen \(\rho\), instrument, and action contract, the normalized
state \(\rho_z\) in equation (2) is sufficient for operational prediction.
But the symbol \(z\) is not universally sufficient across:

- different admitted initial preparations;
- different instruments sharing an outcome alphabet;
- coarse outcomes hiding operationally accessible sub-branches;
- enlarged access to an environment or archive carrying branch information;
  or
- enlarged action classes that distinguish previously equivalent states.

Repairing such a failure by adding the hidden branch, environment, or
apparatus internals is an access/resource enlargement or contract retyping,
not a free record refinement.

## 6. Lawful-fibre translation

Let:

\[
\mathcal F_{\rm law}(a)
\]

contain the histories compatible with the supplied preparation, GRW theory,
apparatus, and downstream action before reading \(Z\). Let:

\[
\mathcal F_{\rm rec}(a,z)
\]

also fix the accessible outcome.

Then:

- the law-plus-instrument packet fixes the measure on both fibres;
- reading \(z\) replaces the mixture in (3) with the conditional kernel in
  (2);
- predictive risk may strictly contract;
- realized \(T\) need not become constant;
- formation provenance remains unidentified by `HC-DU-081`; and
- enlarging the admitted history/access class can reveal the exact first
  leak in Section 5.

Thus the record is operationally useful while the claimed new physical
reconstruction is absorbed.

## 7. Cross-ontology scope

GRWm and GRWf share the operational GRW outcome formalism in their common
domain. Therefore equations (1)--(3) transfer at the calibrated outcome
level without identifying their raw primitive ontologies.

What transfers:

- the joint outcome law;
- the conditional post-experiment density matrix used operationally; and
- the later response distribution.

What does not transfer as a common object:

- a matter-density pattern and a flash set;
- formation provenance;
- an ontology-native retained archive; or
- a selected observer boundary.

A separate cross-ontology swing would therefore repeat a source-stated
operational equivalence while the raw-interface nonidentity is already banked
in `HC-DU-080` and `HC-DU-081`.

## 8. Warrant and grade

### Warrant

- `STANDARD`: the GRW POVM/superoperator and consecutive-experiment
  formalism.
- `DERIVED`: the exact two-state control, risk calculation, and
  action-indexed sufficiency criterion.
- `PROJECT_NATIVE`: the law/interface/access/fibre typing and campaign stop.
- `NOT_EARNED`: new collapse prediction, endogenous interface selection,
  exact future-event reconstruction, provenance, or ontological priority.

### Grade

```text
Grade 4:
  scoped action-indexed outcome-sufficiency boundary
  and exact same-outcome/different-target criterion

Grade 3:
  conditional operational target-kernel reconstruction

Grade 0:
  Dynamic Unity empirical excess, endogenous interface selection,
  provenance reconstruction, exact stochastic-future reconstruction,
  and ontology preference.
```

The Grade-3 result is fully absorbed as scientific novelty by standard GRW
and generic instrument theory. The Grade-4 boundary is useful repository
discipline, not a claim of new mathematics.

## 9. Campaign disposition

The campaign's later, stricter Swing-2 rule said to stop if the GRW outcome
formalism already supplied the complete lawful-fibre result. That condition
is met.

```text
objective-collapse campaign: STOPPED COMPLETE
Swing 4: NOT ACTIVATED
Swing 5: NOT ACTIVATED
reason: STANDARD FORMALISM ABSORBS THE OPERATIONAL POSITIVE
reopen only if:
  a physical mechanism selects the interface/access contract, or
  a held-out response differs from the frozen GRW instrument prediction,
  without refitting ontology, apparatus, calibration, or access.
```

No simulation or hardware is warranted. The repository returns to
whole-portfolio successor selection with no preselected scientific action.

## Primary source

- Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì,
  [The Quantum Formalism and the GRW
  Formalism](https://arxiv.org/abs/0710.0885).

Supporting ontology and accessibility sources remain pinned in `HC-DU-080`
and `HC-DU-081`.
