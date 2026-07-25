---
title: "Conservation to certified record: oriented-reference necessity and selector closure"
status: completed_scoped_interface_necessity_no_go
doc_type: physical_model_no_go_capability_slice_and_collision_audit
created: 2026-07-25
run_id: RUN-20260725-140945-conservation-certified-record
authority: "Joe direct chat: All right, go ahead and run that."
claim_grade: "EXACT FINITE U(1)-CONSERVING MODEL / STANDARD WAY-ASYMMETRY SPECIALIZATION / NO NEW PHYSICS, THEOREM ID, OR PREDICTION"
probe: "../tests/du_conservation_certified_record_probe.py"
artifact: "../tests/artifacts/du_conservation_certified_record_result.json"
---

# Conservation to Certified Record

## Result in plain English

This swing closes the current instrument-selector loop instead of extending
it.

A real conservation law does meaningful work. It restricts which joint
measurements are physically implementable. A bounded asymmetry resource also
does meaningful work. It determines how accurately a measurement that breaks
that symmetry can be implemented.

But those two ingredients do **not** choose one record axis.

The missing ingredient is an **oriented physical reference**. In the exact
model here, the apparatus contains a phase reference. Rotating that reference
by ninety degrees changes an \(X\)-recording instrument into a \(Y\)-recording
instrument even though all of the following stay fixed:

- the additive conservation law;
- the symmetric measurement processor;
- apparatus dimension;
- charge probabilities;
- mean charge and charge variance;
- purity;
- quantum Fisher information for the symmetry;
- trace-asymmetry magnitude;
- pointer and archive dimensions; and
- interaction and decoder resource counts.

So the sharp conclusion is:

> Conservation constrains the feasible measurement class. Asymmetry magnitude
> prices accuracy. The oriented reference state programs the record axis.
> Complete tomography identifies the resulting instrument, but does not
> explain why that oriented reference or coupling was physically selected.

That is an Interface-Necessity No-Go for the attempted selector:

> Any apparatus budget that identifies symmetry-related reference states
> selects at most a measurement orbit, not one instrument within the orbit.

The minimal extra physical structure is now explicit:

1. an oriented reference token or an equivalent symmetry-breaking
   preparation;
2. a fixed symmetric processor or coupling architecture;
3. a pointer and durable archive boundary;
4. a decoder and action task; and
5. selective-map access when the continuation matters.

The result is useful for Dynamic Unity, but its physics is occupied. It is a
finite \(U(1)\) specialization of the Wigner--Araki--Yanase theorem, quantum
reference frames, asymmetry resource theory, no-programming, constrained
state discrimination, interferometry, and quantum-instrument tomography.

The selector branch should therefore stop. The next paper-closing work should
take one independently calibrated physical instrument as an explicit premise
and ask whether its complete causal records are interventionally sufficient.
It should not run another fitted QND or finite-reference selector.

The executable passes `21/21`.

## The physical model

### Additive conservation

Let the source \(S\) and apparatus reference \(R\) be qubits with charges

\[
N_S=|1\rangle\langle1|,
\qquad
N_R=|1\rangle\langle1|.
\]

The joint conserved quantity is

\[
N_{\mathrm{tot}}
=N_S\otimes I+I\otimes N_R.
\]

The apparatus reference is

\[
\rho_R(\alpha,v)
=
\frac12
\begin{pmatrix}
1 & v e^{-i\alpha}\\
v e^{i\alpha} & 1
\end{pmatrix},
\qquad 0\leq v\leq1.
\]

Here \(v\) is the reference visibility or asymmetry magnitude and \(\alpha\)
is its orientation.

### A charge-conserving record instrument

The joint PVM separates the total-charge-zero and total-charge-two sectors:

\[
P_0=|00\rangle\langle00|,
\qquad
P_2=|11\rangle\langle11|.
\]

Inside the total-charge-one sector it resolves

\[
\begin{aligned}
|\chi_+(\beta)\rangle
&=\cos\beta\,|10\rangle+\sin\beta\,|01\rangle,\\
|\chi_-(\beta)\rangle
&=-\sin\beta\,|10\rangle+\cos\beta\,|01\rangle.
\end{aligned}
\]

Every \(P_j\) commutes with \(N_{\mathrm{tot}}\). At
\(\beta=\pi/4\), this is the balanced two-mode interference basis.

The formation isometry is not a bare POVM:

\[
V
=\sum_{j\in\{0,+,-,2\}}
P_j\otimes|j\rangle_P\otimes|j\rangle_A.
\]

It writes the joint result first to a four-label pointer and then to a
four-label durable archive. The pointer and archive labels are charge
degenerate. The probe checks

\[
V^\dagger V=I
\quad\text{and}\quad
(N_{\mathrm{tot}}\otimes I_P\otimes I_A)V
=VN_{\mathrm{tot}}
\]

to machine precision. Thus the formed record is compatible with the declared
additive conservation law.

## Exact induced instrument

At the balanced setting, tracing out the calibrated apparatus reference gives
the source effects

\[
\begin{aligned}
E_0&=\frac12|0\rangle\langle0|,\\
E_+&=\frac14(I+vX_\alpha),\\
E_-&=\frac14(I-vX_\alpha),\\
E_2&=\frac12|1\rangle\langle1|,
\end{aligned}
\]

where

\[
X_\alpha=\cos\alpha\,X+\sin\alpha\,Y.
\]

The \(+\) and \(-\) outcomes carry equatorial sign information. The \(0\)
and \(2\) outcomes reveal only the total-charge boundary sector and are
inconclusive for the equatorial sign task.

For the equiprobable source states

\[
|\pm_\phi\rangle
=\frac{|0\rangle\pm e^{i\phi}|1\rangle}{\sqrt2},
\]

and archive sign-flip probability \(q<1/2\), the accessible total-variation
distinguishability is exactly

\[
\boxed{
D_{\mathrm{access}}
=
\frac12(1-2q)v
\left|\sin(2\beta)\cos(\phi-\alpha)\right|
}.
\]

The optimal forced-guess success is therefore

\[
\boxed{
P_{\mathrm{guess}}
=
\frac12
+\frac14(1-2q)v
\left|\sin(2\beta)\cos(\phi-\alpha)\right|
}.
\]

At perfect alignment, perfect visibility, balanced interference, and a
noiseless archive:

\[
D_{\mathrm{access}}=\frac12,
\qquad
P_{\mathrm{guess}}=\frac34.
\]

If the decoder may abstain on \(0,2\), the conclusive coverage is \(1/2\) and
the conditional success is \(1\).

For the \(U(1)\)-twirled reference \(v=0\), forced-guess success returns to
\(1/2\). The resource-enabled capability is strict but ordinary.

## Robustness receipt

The run froze the perturbation ball

\[
\begin{aligned}
v&\in[0.8,1],\\
|\phi-\alpha|&\leq0.2,\\
|\beta-\pi/4|&\leq0.1,\\
q&\in[0,0.1].
\end{aligned}
\]

Every point obeys

\[
D_{\mathrm{access}}
\geq
\frac12(1-2q_{\max})v_{\min}
\cos(2b_{\max})\cos(\delta_{\max})
=0.307369759040\ldots
\]

The boundary attains that lower bound. A fixed-seed `1000`-case off-grid
stress test has maximum analytic-versus-matrix error
`2.776e-16`; its smallest sampled margin above the bound is
`1.158e-02`.

This is robustness of the frozen physical instrument. It is not robustness
of an independently derived law choosing the apparatus orientation.

## Complete instrument tomography

Outcome probabilities alone would be too weak because they do not determine
the post-measurement continuation.

For each archive outcome \(j\), the probe constructs the selective source map

\[
\mathcal I_j(\rho_S)
=
\operatorname{Tr}_R
\left[
P_j(\rho_S\otimes\rho_R)P_j
\right].
\]

It then reconstructs the full Choi matrix of each \(\mathcal I_j\) by linear
inversion from the informationally complete source preparations

\[
|0\rangle,\quad |1\rangle,\quad |+\rangle,\quad |+i\rangle.
\]

All four maps are completely positive, their effects sum to the identity,
and the maximum reconstructed-versus-model Choi error is
`7.850e-17`.

This is exact synthetic tomography of the declared model, not laboratory
data and not self-calibrating gate-set tomography. A real implementation must
add SPAM, drift, detector, leakage, finite-shot, and gauge controls.

## Scoped no-go — asymmetry amount does not select orientation

Compare

\[
\rho_R(0,1)=|+_x\rangle\langle+_x|
\]

with

\[
\rho_R(\pi/2,1)=|+_y\rangle\langle+_y|.
\]

The two reference states are related by the \(U(1)\) symmetry action. They
therefore have the same value under every symmetry-invariant resource
measure. The probe explicitly verifies equality of:

- charge mean \(1/2\);
- charge variance \(1/4\);
- purity \(1\);
- phase quantum Fisher information \(1\); and
- trace distance from the \(U(1)\)-twirled state \(1/2\).

The symmetric processor is unchanged. Nevertheless,

\[
\rho_R(0,1)
\longmapsto
E_\pm=\frac14(I\pm X),
\]

while

\[
\rho_R(\pi/2,1)
\longmapsto
E_\pm=\frac14(I\pm Y).
\]

For an \(X\)-sign source task, the first reference gives forced-guess success
\(3/4\), while the second gives \(1/2\), despite identical scalar resource
budgets.

Therefore:

> A conservation law plus a symmetry-invariant apparatus resource budget
> cannot select a unique measurement orientation. It selects, at most, the
> orbit of measurements programmable by equally resourced, symmetry-related
> reference states.

Specifying the full oriented reference state resolves the ambiguity, but that
is exactly the additional physical premise the attempted selector was meant
to derive.

## The reference is a charged resource, not free finality

The strict capability delta does not come from the fact that an archive
becomes stable.

For the equiprobable source ensemble, the nonselective formed measurement
twirls the one-qubit reference:

\[
\rho_R(0,1)\longmapsto I/2.
\]

Its trace-asymmetry resource falls by \(1/2\). Archive noise then independently
reduces the observer-visible distinction:

\[
D_{\mathrm{archive}}=(1-2q)D_{\mathrm{pointer}}.
\]

The correct causal account is:

```text
oriented reference resource
    + symmetric charge-conserving processor
    + pointer/archive formation
    + decoder quality
    -> bounded sign-discrimination capability
```

This does **not** establish:

- a finality--capability law;
- a record-first ontology;
- public or regional finality;
- observer-created physical reality;
- new collapse dynamics;
- a selected microscopic apparatus; or
- a physical prediction beyond standard quantum theory.

It instead demonstrates the normalization discipline `HC-DU-037` requires:
the capability gain disappears when the oriented reference resource is
omitted, twirled, or misaligned.

## Primary-literature collision

The collision is decisive.

### Wigner--Araki--Yanase and quantitative bounds

[Ozawa (2002)](https://arxiv.org/abs/quant-ph/0112154) extended the
conservation-law limitation from repeatable or nondisturbing measurements to
general measurement accuracy and supplied a quantitative apparatus-variance
bound. The present result is not a stronger universal bound.

### Asymmetry resources and no-programming

[Marvian and Spekkens
(2012)](https://arxiv.org/abs/1212.3378) showed that WAY restrictions can be
understood through the resource theory of asymmetry and the no-programming
theorem. The apparatus state is a program encoding which symmetry-related
measurement is implemented. Exact implementation requires a perfectly
asymmetric reference.

That account already contains the central Dynamic Unity verdict: an
asymmetry resource does not merely have an amount; its group orbit carries
the orientation information that programs the target observable.

### The explicit \(U(1)\) qubit construction

[Ahmadi, Jennings, and Rudolph
(2013)](https://doi.org/10.1088/1367-2630/15/1/013057) explicitly treated
\(U(1)\)-constrained measurement of the qubit \(|+\rangle,|-\rangle\) basis,
decomposed the apparatus into asymmetry and charge subsystems, and constructed
finite reference-state discrimination models. The present one-qubit
reference is the \(M=1\) edge of that occupied construction class, augmented
with DU's explicit pointer/archive, perturbation, tomography, and capability
typing.

### Current general bounds and physical interferometry

[Hokkyo and Tajima
(2026)](https://arxiv.org/abs/2607.09075) derive quantitative WAY bounds for
general unitary and antiunitary symmetries using the distinguishability of
symmetry-related apparatus program states. This further blocks novelty for a
general “asymmetry selects the record” theorem.

[Piccione et al.
(2024)](https://arxiv.org/abs/2404.12910) give an experimentally motivated
interferometric measurement under total-energy conservation and analyze how
meter resources and dynamics control error. Interferometric physicalization
is therefore an available platform route, not a distinct DU prediction.

### Complete instrument characterization

[Stricker et al.
(2022)](https://arxiv.org/abs/2110.06954) give and experimentally implement
a general quantum-instrument characterization method that includes both
classical outcomes and post-measurement states. DU's insistence on selective
maps rather than POVMs alone is correct but not novel.

### Collision verdict

| Component | Status |
|---|---|
| conservation restricts asymmetric measurement | established |
| apparatus asymmetry prices accuracy | established |
| apparatus state programs the oriented observable | established |
| finite \(U(1)\) reference construction | established |
| interferometric physical implementation route | established |
| full selective-instrument characterization | established |
| explicit pointer/archive/resource/capability typing | useful DU integration |
| independent DU rule selecting the orientation | absent |

The conjunction is a valuable program control and paper module. It is not a
standalone new physics or measurement-theory paper.

## What this changes in Dynamic Unity

### `HC-DU-033`

The parent remains open in its universal wording, but this attempted route is
closed:

> Additive conservation plus a calibrated scalar apparatus-asymmetry budget
> does not select a unique record instrument.

The earned minimal-structure classification is:

\[
\text{conservation}
+\text{oriented reference}
+\text{processor}
+\text{pointer/archive}
+\text{decoder/action}
+\text{selective access}.
\]

Dynamic Unity should no longer spend a concentrated swing trying to recover a
unique record axis from conservation and asymmetry amount alone.

### `HC-DU-037`

The downstream slice is a positive normalization control:

- aligned reference: forced-guess success \(3/4\);
- twirled reference: \(1/2\);
- equally asymmetric quarter-turn reference on the frozen \(X\) task:
  \(1/2\);
- aligned conclusive coverage: \(1/2\);
- aligned conditional success: \(1\); and
- archive flips multiply distinguishability by \(1-2q\).

This is ordinary reference-resource-enabled capability. It does not support
the stronger finality--capability law.

### Paper route

Do not create a new paper opportunity.

- Merge the no-go and physical interface passport into `DU-PAPER-007`,
  **Interventional Record Sufficiency**.
- Use the capability accounting as a hostile control for `DU-PAPER-010`,
  **Finality, Capability, and Coherent Optionality**.
- Keep `DU-PAPER-012`, **Certified Causal Reality**, at dependency-program
  grade.

The next high-value paper swing is not another interface selector. It is an
implementation-complete physical arm for `DU-PAPER-007`:

1. choose a real calibrated quantum process instrument;
2. retain reference, route, environment, controller, detector, and invalid
   ports;
3. reconstruct the complete selective instrument with uncertainty;
4. freeze the candidate record and admissible physical refinements before the
   verdict;
5. run factorization or return a finite separating intervention;
6. add a finite-shot witness and strongest implementation-complete null; and
7. report factorization, minimal refinement, candidate remainder, or
   incomplete contract without ontological inflation.

## Branch disposition

```text
LABORATORY-COMPATIBLE U(1) MODEL: BUILT
ADDITIVE CONSERVATION: EXACT
FORMED POINTER AND ARCHIVE: EXACT
SELECTIVE-INSTRUMENT TOMOGRAPHY: EXACT SYNTHETIC
PERTURBATION-BALL ROBUSTNESS: EXACT
CAPABILITY SLICE: EXACT AND RESOURCE-ACCOUNTED
UNIQUE AXIS FROM CONSERVATION + ASYMMETRY AMOUNT: NO
ORIENTED REFERENCE NECESSARY: YES, IN THE DECLARED CLASS
PRIMARY-LITERATURE COLLISION: ABSORBED
NEW PHYSICS / THEOREM ID / PREDICTION / PAPER SEED: NO
FURTHER FINITE SELECTOR FITTING: STOP
NEXT CONCENTRATED TARGET: IMPLEMENTATION-COMPLETE PHYSICAL INTERVENTIONAL SUFFICIENCY
```
