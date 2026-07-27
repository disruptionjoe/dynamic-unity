# 3+1 Law-Filtered Record-Assisted Reconstruction and the Causal-Exterior Remainder

## Status

```text
N5-RS-P3 COMPLETE
HC-DU-052
LAWFUL_SAME_RECORD_DIFFERENT_TARGET
CAUSAL_EXTERIOR / OPEN-BOUNDARY ATTRIBUTION
KNOWN GENERAL-RELATIVITY AND HYPERBOLIC-PDE MATHEMATICS
NO NEW PHYSICS, ONTOLOGY, PREDICTION, PAPER, CFS, HARDWARE, OR EXTERNAL ACTION
```

This swing executes the first `3+1` law-filtered inverse problem selected by
`N5-RS-P2`. It asks whether the Einstein--matter law and the strongest local
record available before a target event determine that target, or whether an
exact lawful, nongauge, same-record/different-target direction remains.

The answer is:

> A lawful target-changing remainder survives, but its first and smallest
> instance is incoming radiative data outside the record region's causal
> domain. It is ordinary missing characteristic-boundary information, not a
> new record-relative physical effect.

That clean attribution is the result. Any stronger Dynamic Unity remainder
must now survive after the incoming characteristic boundary has been closed.

## 1. Frozen contract

### Physical class

Work in linearized `3+1` Einstein--matter theory about a weak-field globally
hyperbolic background:

\[
G^{(1)}_{\mu\nu}[h]=8\pi G\,\delta T_{\mu\nu},
\qquad
\nabla^\mu\delta T_{\mu\nu}=0,
\]

modulo linearized diffeomorphisms. The finite admitted solution class is

\[
m(a,b,c,p_+,p_\times)
=
a\,s_1+b\,s_2+c\,v+p_+w_+ +p_\times w_\times .
\]

Here:

- \(s_1,s_2\) are two fixed lawful scalar matter/source-response solutions;
- \(v\) is one fixed lawful divergence-free matter-current/vector response;
- \(w_+,w_\times\) are independent vacuum transverse-traceless radiative
  solutions; and
- the five coefficients are bounded to a small linearized neighborhood.

The radiative characteristic data are chosen so that \(w_+\) and
\(w_\times\) vanish throughout the entire past record region \(O_R\), but
their gauge-invariant Weyl response is nonzero in a later target region
\(O_T\). Standard finite propagation and characteristic-Cauchy existence
make this a lawful solution class. No arbitrary off-shell conformal
deformation is admitted.

### Gauge

The comparison is made in the solution space modulo linearized
diffeomorphisms. The two radiative witnesses are nongauge because their
linearized Weyl tensors are nonzero in \(O_T\); linearized curvature on a flat
background is gauge invariant.

### Observer, record, and resources

The observer is a supplied material worldtube contained in \(O_R\). The
frozen finite resource contract admits two scalar response channels and one
vector/current channel, all jointly realizable in the classical linearized
fixture. It admits no channel outside \(O_R\) and no future-correlated oracle.

The finite exact regression summary is

\[
R(m)=
\left(
a+b,\;
\frac14a+\frac12b,\;
c
\right).
\]

Its scalar rows are the previously controlled two-source/two-clock response;
the third row records the admitted vector/current mode. They reconstruct
\(a,b,c\) exactly:

\[
a=2R_0-4R_1,\qquad
b=4R_1-R_0,\qquad
c=R_2.
\]

The numerical response weights are inherited supplied controls, not
Einstein-selected detector coefficients. Any nonsingular three-channel local
response block would play the same positive-control role. The radiative
remainder does not depend on those particular weights.

This is the greatest interface in the declared finite instrument family, but
it is not being claimed as uniquely selected by Einstein--matter dynamics.
The stronger causal statement is interface-independent within the locality
contract: because \(w_+\) and \(w_\times\) vanish on all of \(O_R\), every
physically local archive formed there is constant in \((p_+,p_\times)\).
Enlarging or changing a local detector inside \(O_R\) cannot repair that
causal separation.

Interface grade:

```text
observer worldtube: SUPPLIED
record region O_R: SUPPLIED
local archive mechanism: SUPPLIED, TARGET-INDEPENDENT
finite response summary R: SUPPLIED REGRESSION PROJECTION
incoming characteristic boundary: OMITTED BY THE FROZEN LOCAL CONTRACT
```

### Held-out target

The target is the two-polarization gauge-invariant radiative response in
\(O_T\), normalized in the finite class as

\[
T(m)=(p_+,p_\times).
\]

It can be read as a two-axis optical/gradiometric response or as two declared
linearized-Weyl components. It is not a coordinate component of \(h\).

## 2. Exact rank result

In coordinates \((a,b,c,p_+,p_\times)\),

\[
DR=
\begin{pmatrix}
1&1&0&0&0\\
\tfrac14&\tfrac12&0&0&0\\
0&0&1&0&0
\end{pmatrix},
\qquad
DT=
\begin{pmatrix}
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}.
\]

Therefore

\[
\operatorname{rank}(DR)=3,\qquad
\operatorname{rank}
\begin{pmatrix}
DR\\DT
\end{pmatrix}
=5,
\]

and the record-null solution tangent has dimension two:

\[
\ker DR
=
\operatorname{span}
\left\{
e_+=(0,0,0,1,0),
e_\times=(0,0,0,0,1)
\right\}.
\]

Both directions are lawful and nongauge, while

\[
DT(e_+)=(1,0),\qquad DT(e_\times)=(0,1).
\]

On a normalized coefficient box \(p_+,p_\times\in[-1,1]\), both the
law-only and record-conditioned target diameters are nonzero; coordinatewise
they remain \(2\). The record removes no part of the incoming-radiation
uncertainty.

The primary return is exactly:

```text
LAWFUL_SAME_RECORD_DIFFERENT_TARGET
```

The smallest witness needs only one polarization:

\[
m(0,0,0,0,0)
\quad\hbox{and}\quad
m(0,0,0,\epsilon,0)
\]

have identical complete local histories in \(O_R\) and different future
targets in \(O_T\).

## 3. Positive and hostile controls

### Control A — strict record assistance exists in the same framework

Restrict the target to any nonconstant scalar/vector combination of
\((a,b,c)\). The Einstein law admits several such source amplitudes, while
the joined local response \(R\) reconstructs all three. This is strict
record-assisted reconstruction inside the finite source sector; it is not
law-only closure.

### Control B — no incoming radiation closes the radiative target

Add the independently stated boundary condition

\[
p_+=p_\times=0.
\]

Then \(T=0\) before records are consulted:

```text
LAW_ONLY_TARGET_CLOSURE
```

This is completion/source-class narrowing. It must not be credited to the
record.

### Control C — characteristic tomography closes the radiative target

Add the full incoming characteristic archive

\[
B=(p_+,p_\times).
\]

Then \((R,B)\) has rank five and reconstructs the complete finite
coefficient vector. This is resource-expanded, injective characteristic
tomography. It is not strict compression by the original local record.

### Control D — the earlier compact conformal vacuum mode

The prior compactly supported conformal vacuum direction is already killed
by the `3+1` trace-free linearized Einstein equation. That was
`LAW_ONLY_TARGET_CLOSURE`. The present tensor direction was selected
specifically to avoid rerunning that closed sector.

## 4. What is and is not learned

### Learned

1. Einstein--matter dynamics alone does not turn a local past record into a
   complete predictor of future geometry on an open domain.
2. A complete local record cannot contain causally exterior incoming
   characteristic data merely by being made more detailed.
3. Law-only closure, local record assistance, and boundary-data tomography
   all occur in the same typed framework and receive different credit.
4. The first lawful same-record/different-target vector is not exotic. It is
   a standard incoming radiative degree of freedom.
5. Future DU remainder claims must close or explicitly condition on the
   target's incoming characteristic boundary before they can count as
   evidence for something beyond ordinary causal incompleteness.

### Not learned

- Records do not thereby create physical reality.
- Records are not shown to reconstruct all observer-accessible physics.
- The witness is not a new GR theorem or a deviation from GR.
- The result does not select the observer, apparatus, archive, or access
  boundary.
- It does not support CFS, layered finality, a preferred foliation, a
  substrate ontology, or external hardware.
- It is not a physical remainder after complete causal closure.

The exact type is:

```text
CAUSAL-EXTERIOR REMAINDER
!=
CAUSALLY-CLOSED INTERIOR REMAINDER
```

## 5. Absorbers and literature boundary

The component result is absorbed by standard hyperbolic domain-of-dependence
and characteristic initial-value theory:

- Friedrich and Rendall,
  [The Cauchy Problem for the Einstein
  Equations](https://arxiv.org/abs/gr-qc/0002074);
- Hilditch, Valiente Kroon, and Zhao,
  [Revisiting the characteristic initial value problem for the vacuum
  Einstein field equations](https://arxiv.org/abs/1911.00047); and
- Mars and Sánchez-Pérez,
  [Double Null Data and the Characteristic Problem in General
  Relativity](https://arxiv.org/abs/2205.15267).

Gauge-invariant local-observable and inverse-problem comparisons include:

- Khavkine,
  [Local and gauge invariant observables in
  gravity](https://arxiv.org/abs/1503.03754); and
- Kurylev, Lassas, Oksanen, and Uhlmann,
  [Inverse problem for Einstein-scalar field
  equations](https://arxiv.org/abs/1406.4776).

The DU increment is the attribution protocol: measure law-only diameter
first, quotient gauge, distinguish local record refinement from
characteristic completion, and refuse to call an open-boundary degree of
freedom a novel record-relative physical remainder.

## 6. Consequence for the next swing

The highest-information successor is:

```text
N5-RS-P4
Causally Closed Interior Reconstruction and Noninjective Transfer
```

Put a complete incoming-characteristic variable family for a compact causal
diamond inside the frozen completion contract, exclude omitted exterior
support, keep a nonzero lawful interior solution class, and seek one of:

1. strict noninjective record-assisted held-out transfer;
2. an exact nongauge interior same-record/different-target witness; or
3. proof that the chosen target is already fixed by the closed law and
   boundary contract.

Do not add CFS, a fitted detector, simulation, or hardware before that exact
interior decision. If every candidate target is closed only by directly
recording its complete characteristic data, return
`INJECTIVE_TOMOGRAPHY_ONLY`.

## 7. Reproducibility

The analytic rank certificate is preserved by:

```bash
python3 tests/du_3plus1_lawful_causal_remainder_probe.py
```

The probe uses exact rational arithmetic. It is a regression check for the
finite response matrices and controls, not a spacetime simulation or
independent proof of the cited hyperbolic existence results.
