# 3+1 Causally Closed Noninjective Transfer and First Recoupling

## Status

```text
N5-RS-P4 COMPLETE
HC-DU-053
STRICT_NONINJECTIVE_TRANSFER_WITH_INTERIOR_FIRST_RECOUPLING
KNOWN FACTORIZATION, OBSERVABILITY, AND GENERAL-RELATIVISTIC WAVE-TRANSPORT MATHEMATICS
NO NEW PHYSICS, ONTOLOGY, PREDICTION, PAPER, CFS, HARDWARE, OR EXTERNAL ACTION
```

This swing closes the causal-exterior loophole found by `HC-DU-052`. It puts
the complete incoming variable family of a frozen two-polarization
gravitational-wave packet sector inside the completion class, admits no later
exterior input, and asks whether a strictly compressed record can still
predict a held-out physical response.

The answer has two parts:

> Yes. A scalar record of the packet's beam-normalized intensity can predict a
> later polarization-insensitive response while discarding the polarization
> orientation. The law transports the value but does not select it, so this is
> strict noninjective record assistance rather than law-only closure.

> No such record is sufficient for every capability. An orientation-sensitive
> action reopens distinctions inside the intensity fibre, and a one-component
> record fails as soon as lawful interior transport recouples the hidden
> polarization into the measured axis.

Thus causal closure removes omitted outside inputs, but does not itself imply
record sufficiency. The exact boundary is target- and capability-relative
factorization through the record.

## 1. Frozen contract

### Causally closed physical sector

Take a compact causal tube inside a globally hyperbolic `3+1` background and
restrict the incoming characteristic data to one high-frequency
transverse-traceless packet with two real polarization coefficients:

\[
x=(p_+,p_\times)\in[-1,1]^2.
\]

Both coefficients are inside the frozen completion class. No additional
incoming packet, source, matter impulse, controller state, or exterior
boundary variable is admitted after the incoming cut. This is complete for
the declared two-mode packet sector, not for unrestricted general
relativity.

At leading geometric-optics order, gravitational-wave polarization is
parallel transported along the ray while the squared amplitude changes with
the beam cross-section. Absorb the separately calibrated scalar focusing
factor into the amplitude normalization. The remaining polarization
transport is an orthogonal map \(U\) on the two-dimensional polarization
space. Two exact specimens are

\[
U_0=
\begin{pmatrix}
1&0\\0&1
\end{pmatrix},
\qquad
U_\theta=
\begin{pmatrix}
\frac35&\frac45\\[2pt]
-\frac45&\frac35
\end{pmatrix}.
\]

Both have \(U^\mathsf TU=I\) and determinant one. \(U_0\) is the aligned
flat/parallel-transport control. \(U_\theta\) is an exact rational
relative-orientation/holonomy control. Input and output screen frames are
fixed by supplied material orientation references, so an oriented detector
response is operational rather than a free coordinate relabeling. The exact
rational angle is an admitted transfer control, not a derivation of a unique
curved background.

This use of geometric optics follows the standard result that gravitational
waves propagate on null rays with parallel-transported polarization and
beam-area-dependent amplitude:

- Sam Dolan,
  [Geometrical optics for scalar, electromagnetic and gravitational waves in
  curved spacetime](https://arxiv.org/abs/1806.08617).

The characteristic closure continues to rely on the standard
Einstein-equation Cauchy/characteristic framework cited by `HC-DU-052`:

- Friedrich and Rendall,
  [The Cauchy Problem for the Einstein
  Equations](https://arxiv.org/abs/gr-qc/0002074);
- Hilditch, Valiente Kroon, and Zhao,
  [Revisiting the characteristic initial value problem for the vacuum
  Einstein field equations](https://arxiv.org/abs/1911.00047); and
- Mars and Sánchez-Pérez,
  [Double Null Data and the Characteristic Problem in General
  Relativity](https://arxiv.org/abs/2205.15267).

### Observer, record, target, and resources

The primary record is the scalar beam-normalized quadratic intensity

\[
r_I(x)=p_+^2+p_\times^2.
\]

A supplied probe-limit test-body instrument writes this scalar into a local
archive before the later target interaction. The record is fixed before the
held-out target is evaluated and is insensitive to polarization orientation.
Its physical formation coupling and material orientation are supplied, not
selected by the Einstein equations. Backreaction and a microscopic archive
model are outside the frozen response sector.

The primary held-out target is a downstream polarization-insensitive
quadratic response, normalized as

\[
T_I(x)=\|Ux\|^2.
\]

It may be read as a calibrated downstream flux or energy-response statistic
inside the geometric-optics approximation. The exact claim is only about the
frozen response functional, not a universal local gravitational-energy
density.

The preregistered capability enlargement adds an oriented signed response

\[
T_+(x)=P Ux,\qquad P=(1,0).
\]

The strongest repair grants the full incoming archive

\[
B(x)=(p_+,p_\times).
\]

Interface grades:

```text
two-polarization incoming class: PHYSICALLY ADMITTED, FINITE SECTOR
transport U: SUPPLIED LAWFUL BACKGROUND PROPAGATOR
material orientation references: SUPPLIED
quadratic record instrument: SUPPLIED, TARGET-INDEPENDENT, PROBE-LIMIT
record archive: CONDITIONALLY FORMED BY THE SUPPLIED INSTRUMENT
held-out targets: FROZEN BEFORE DECODING
full incoming archive: RESOURCE-EXPANDED INJECTIVE CONTROL
```

No local research model was admitted. The result was derived analytically;
the Python artifact is only a proportional exact regression certificate
under the reproducibility exception in `LMLG-01`.

## 2. General transfer theorem

Let \(X\) be a completion class, \(r:X\to Q\) a record fixed independently of
the target, \(U:X\to X'\) lawful evolution through the causally closed
domain, and \(t:X'\to Y\) a held-out target. A common decoder
\(d:Q\to Y\) satisfying

\[
t\circ U=d\circ r
\]

exists exactly when

\[
r(x)=r(x')
\Longrightarrow
t(Ux)=t(Ux')
\quad\text{for every }x,x'\in X.
\]

Equivalently, the record equivalence refines the pulled-back target
equivalence. The transfer is **strictly noninjective** when \(r\) is not
injective while \(t\circ U\) is nonconstant.

For finite linear maps \(R,U,P\), the condition reduces to

\[
\ker R\subseteq\ker(PU),
\]

or

\[
\operatorname{rank}
\begin{pmatrix}
R\\PU
\end{pmatrix}
=\operatorname{rank}R.
\]

If \(H\) spans a record-hidden complement, the first hidden-to-visible
recoupling is the first admitted transport for which

\[
P U H\ne0.
\]

This is known factorization, sufficient-statistic, observability, and
controlled-lumpability mathematics. Within DU it is the causally closed
physical specialization of the existing `HC-DU-035D`, `HC-DU-036H`, and
`HC-DU-039C` kernel/fibre spine. The increment is not a new component theorem;
it is the closed-boundary attribution and the unchanged physical specimen.

## 3. Strict noninjective transfer

Orthogonality gives

\[
T_I(x)=\|Ux\|^2=\|x\|^2=r_I(x)
\]

for both \(U_0\) and \(U_\theta\). The same decoder

\[
d(q)=q
\]

works without refitting.

On the admitted square, the law-only target ranges from zero to two. The
Einstein transport law therefore does not close its value:

\[
\operatorname{diam}T_I(X)=2.
\]

After conditioning on the record, its target diameter is zero:

\[
\operatorname{diam}T_I(r_I^{-1}(q))=0.
\]

The record is strictly noninjective. For example,

\[
x=(1,0),\qquad x'=(0,1)
\]

are different physical polarization states with the same record
\(r_I=1\). Indeed every nonzero record fibre contains an orientation family.

The classification is therefore:

```text
STRICT_RECORD_RECONSTRUCTION
```

It is not `LAW_ONLY_CLOSURE`: the law preserves the intensity but does not
choose which intensity the incoming packet has. The record supplies that
missing lawful value. It is not tomography: polarization orientation remains
unreconstructed.

This is a conditional positive result for the **transfer** leg of
`H-CCR-17`. It does not close the harder physical-selection and formation
legs because the test-body instrument and archive are supplied.

## 4. Capability-relative interior remainder

The same intensity record does not reconstruct an oriented signed response.
For example,

\[
x=(1,0),\qquad x'=(-1,0)
\]

have the same intensity record, while under \(U_\theta\)

\[
T_+(x)=\frac35,\qquad
T_+(x')=-\frac35.
\]

Both completions use the same complete incoming variable family and the same
closed lawful propagation. Nothing arrives from outside after the boundary.
The failure is an interior, target-relative remainder:

```text
CAPABILITY_RELATIVE_REMAINDER
```

This is not a new gravitational effect. The record discarded orientation,
and the enlarged action asks for orientation.

## 5. Exact first-recoupling control

To distinguish immediate capability enlargement from dynamical recoupling,
freeze the linear one-component record

\[
r_+(x)=Px=p_+.
\]

Its hidden direction is \(H=(0,1)^\mathsf T\).

Under aligned transport,

\[
P U_0 H=0,
\]

so the later plus response factors through the record. The record has rank
one on a two-dimensional completion class, the law-only target diameter is
two, and the record-conditioned target diameter is zero:

```text
STRICT_RECORD_RECONSTRUCTION
```

Under the rational polarization rotation,

\[
P U_\theta=
\begin{pmatrix}
\frac35&\frac45
\end{pmatrix},
\qquad
P U_\theta H=\frac45.
\]

The cross-polarized witness \(x=(0,1)\) has record zero and future oriented
response \(4/5\). On the admitted square,

\[
\operatorname{diam}T_+(X)=\frac{14}{5},
\qquad
\operatorname{diam}T_+(r_+^{-1}(q))=\frac85.
\]

The exact return is:

```text
SAME_RECORD_DIFFERENT_TARGET
FIRST INTERIOR RECOUPLING
```

Replacing the old record row by \(P U_\theta\) would make the target factor,
but that is a target-specific interface change unless independent physics
selects the back-propagated detector orientation. It receives no
reconstruction credit here.

## 6. Strong controls

| Control | Return | Why |
|---|---|---|
| Fix all incoming amplitudes | `LAW_ONLY_CLOSURE` | The completion class has been collapsed before records. |
| Quadratic intensity record, quadratic downstream response | `STRICT_RECORD_RECONSTRUCTION` | Nonzero law-only diameter; same decoder; strict orientation compression. |
| Intensity record, oriented response | `CAPABILITY_RELATIVE_REMAINDER` | Orientation varies inside every nonzero intensity fibre. |
| Plus record, aligned plus response | `STRICT_RECORD_RECONSTRUCTION` | The hidden cross direction remains target-null. |
| Plus record, rotated plus response | `SAME_RECORD_DIFFERENT_TARGET` | Interior transport recouples the hidden cross direction. |
| Full two-polarization archive | `INJECTIVE_TOMOGRAPHY` | Rank two on a two-dimensional packet sector. |
| Back-propagated target row | `TARGET_CODED_INTERFACE_REFIT` | The interface changes with the held-out target/transport. |
| Unspecified additional packet or boundary mode | `INCOMPLETE_CONTRACT` | Causal closure has not actually been established. |

## 7. What changed

### Learned

1. Causal closure and record sufficiency are different conditions.
2. Strict noninjective physical transfer is possible under ordinary general
   relativity in a frozen finite sector; no exotic record ontology is needed.
3. A conservation or transport law can supply the decoder without supplying
   the incoming value. A prior record can therefore do real predictive work
   even when the target is lawfully conserved.
4. Sufficiency is indexed by the held-out target and capability envelope. A
   record may close downstream energy response while leaving polarization
   sign and orientation fully open.
5. The first interior failure is exactly the first record-hidden direction
   that lawful transport makes target-visible.
6. The transfer part of the North Star is no longer merely aspirational.
   The remaining high-value burden is independent physical selection and
   formation of the compressed record, plus transfer beyond a supplied
   finite response sector.

### Not learned

- Records do not thereby create physical reality.
- The Einstein equations do not select the detector, orientation reference,
  archive, decoder, target, or capability envelope.
- No theorem for unrestricted general relativity is claimed.
- The quadratic response is not asserted to be a universal local
  gravitational energy density.
- The result does not establish a novel physical remainder, modified gravity,
  CFS correction, empirical prediction, or hardware requirement.
- A target-relative compressed statistic is not a reconstruction of the full
  source state.

## 8. Consequence for the next swing

`N5-RS-P4` closes positively and adversely at once. The next and final
position of the prepared sequence is now executable:

```text
N5-RS-P5
Cross-Arena Dynamic Sufficiency and Formation Non-Unification
```

Apply the unchanged transfer criterion to:

1. this causally closed gravitational-wave specimen; and
2. the completed metastable host.

Search for either a common theorem or the smallest typed failure. The leading
candidate theorem is:

> A record is final for a frozen future action family exactly when every
> pulled-back future action is constant on its fibres; the first failure is
> the first hidden-to-visible recoupling.

The leading non-unification is upstream: the gravitational-wave archive is a
supplied physical instrument, while the metastable host selects only a
terminal operational quotient and not an accessible historical archive.
`N5-RS-P5` should determine whether the transfer theorem is already fully
absorbed by `HC-DU-035D/036H` and whether physical formation—not transfer—is
the unique remaining cross-arena obstruction. Do not add CFS, another host,
simulation, or hardware.

## 9. Reproducibility

The exact rational certificate is preserved by:

```bash
python3 tests/du_3plus1_closed_noninjective_transfer_probe.py
```

The probe checks orthogonality, strict noninjectivity, law-only and
record-conditioned target diameters, linear factorization, first recoupling,
capability enlargement, target-coded refit, and injective-tomography
controls. It is a regression artifact after the analytic result, not a
research model or independent proof of the physical approximation.
