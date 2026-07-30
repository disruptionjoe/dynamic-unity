---
title: "Reversible-pointer CSL quadratic-kernel degeneracy and breathing-contrast repair"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-158
run_id: RUN-20260730-092634-reversible-pointer-kernel-degeneracy
work_id: ANOMALY-CSL-PATH-KERNEL-ATTRIBUTION
action_id: RPCSL-02-QUADRATIC-KERNEL-DEGENERACY-GATE
owner_repo: dynamic-unity
maximum_grade: 4
---

# Reversible-pointer CSL quadratic-kernel attribution gate

## Executive return

```text
POINTLIKE CSL AND THREE ORDINARY LOSS CLASSES SHARE ONE PATH KERNEL
+ FORCE-AMPLITUDE SCANS CANNOT ATTRIBUTE THE LOSS
+ SOURCE-OFF VISIBILITY DOES NOT ESTIMATE A PATH-CORRELATED COEFFICIENT
+ FINITE-WIDTH BREATHING SUPPLIES A CONDITIONAL RANK-RESTORING CONTROL
+ MASS/CHARGE COUPLING CONTRAST SUPPLIES A SECOND CONDITIONAL REPAIR
+ EXACT CSL SEPARATION NONLINEARITY IS TOO SMALL IN THE PROPOSED REGIME
+ STANDARD FILTER-FUNCTION AND EXPERIMENTAL-DESIGN ABSORPTION
+ NO OBSERVED RESULT, CSL EVIDENCE, SELECTED APPARATUS, HARDWARE ACTION,
   NEW DU LAW, OR READY SUCCESSOR
```

`HC-DU-157` left the attribution question in abstract form:

\[
y=\lambda K(r_c)+B\theta,
\qquad
K(r_c)\notin\operatorname{col}(B)
\]

is required to identify a CSL contribution at fixed \(r_c\). This run
instantiates \(K\) and part of \(B\) from the proposal's own equations.

The result is both a no-go and a repair.

In the pointlike small-separation model, CSL, residual-gas decoherence,
blackbody decoherence, and intra-shot white electric-field phase noise are
all proportional to the same statistic

\[
I_D=\int_0^\tau D^2(t)\,dt.
\]

Varying the force, frequency, or path while keeping the pointer and nuisance
coefficients fixed changes only that one column. No amount of exact data from
that scan can say which mechanism supplied the loss.

The proposal's finite-width correction prevents this from killing the whole
route. It multiplies the CSL integrand by a known breathing factor that is
absent from those three ordinary-loss approximations. Two otherwise matched
preparations with different breathing factors restore rank against a single
shared \(I_D\) nuisance. The cleanest candidate is therefore not “use a
larger force.” It is:

> Hold the trajectory and apparatus fixed, vary the prepared pointer width,
> independently measure that width, and test whether the loss follows the
> CSL finite-width response rather than the shared quadratic path response.

This is a conditional assay design, not a selected implementation or evidence
for CSL. Width-dependent endpoint errors and every additional nuisance
response must still be frozen and independently controlled.

## 1. Scope and source status

The primary specimen remains Peter Renkel,
["Testing Continuous Spontaneous Localization by Coherently Simulating a
Measurement with a Nanoparticle"](https://arxiv.org/abs/2606.22707),
arXiv:2606.22707v4, revised July 21, 2026.

The source is an experimental proposal. It reports projected sensitivity, not
data. Its apparatus, force source, particle, initial preparation, loss model,
calibration strategy, and access interface are supplied.

The proportionality results below are exact **inside the source's declared
pointlike or small-separation approximations**. They are not universal
theorems about every CSL experiment, every environmental spectrum, or every
spatial decoherence law.

## 2. The source's response columns

For the harmonic trajectory,

\[
D(t)=\frac{F}{m\omega^2}(1-\cos\omega t),
\qquad
\tau=\frac{2\pi}{\omega},
\]

the source gives

\[
I_D
=
\int_0^\tau D^2(t)\,dt
=
\frac{3\pi F^2}{m^2\omega^5}.
\]

### Pointlike small-separation CSL

\[
\Lambda_{\rm CSL}^{(0)}
=
\lambda\frac{m^2}{4m_0^2r_c^2}I_D.
\]

### Small-separation gas and blackbody loss

The proposal writes the two environmental terms as

\[
\Lambda_{\rm gas}=\eta_{\rm gas}I_D,
\qquad
\Lambda_{\rm bb}=\eta_{\rm bb}I_D.
\]

The coefficients encode the relevant environmental resolution and scattering
physics. Treating them as known numerical budgets is not the same as
identifying them from Ramsey visibility.

### Intra-shot white electric-field phase noise

For

\[
\langle\delta E(t)\delta E(t')\rangle
=
\frac{S_E}{2}\delta(t-t'),
\]

the phase

\[
\delta\phi_E
=
\frac{q}{\hbar}\int_0^\tau\delta E(t)D(t)\,dt
\]

gives

\[
\Lambda_E^{\rm intra}
=
\frac{q^2S_E}{4\hbar^2}I_D.
\]

Thus, on a fixed pointer and in the declared pointlike model,

\[
y_i
=
I_{D,i}
\left[
\lambda\frac{m^2}{4m_0^2r_c^2}
+\eta_{\rm gas}
+\eta_{\rm bb}
+\frac{q^2S_E}{4\hbar^2}
\right]
+y_i^{\rm other}.
\]

The four displayed response columns are collinear.

## 3. Quadratic-path attribution theorem

### Theorem 1 — pointlike path-only rank obstruction

Fix \(m,q,r_c\) and the coefficients
\(\eta_{\rm gas},\eta_{\rm bb},S_E\). For any finite or infinite family of
controlled paths \(D_i(t)\) admitted by the pointlike small-separation model,
the design columns for:

1. CSL amplitude \(\lambda\);
2. residual-gas loss;
3. blackbody loss; and
4. white electric-field phase noise

all lie in

\[
\operatorname{span}\{(I_{D,1},\ldots,I_{D,n})^\mathsf T\}.
\]

The displayed sub-design therefore has rank at most one.

### Proof

Each exponent is a configuration-independent scalar coefficient times
\(I_{D,i}\). Every column is therefore proportional to the same vector
\((I_{D,i})_i\). Additional exact observations change the precision of the
sum coefficient but cannot increase the design rank. \(\square\)

### Corollary 1 — force and pointlike frequency scans do not attribute

For the harmonic family,

\[
I_D=\frac{3\pi F^2}{m^2\omega^5}.
\]

Varying \(F\), \(\omega\), or both changes the common response vector but does
not separate its coefficients in the pointlike model. The often-quoted
\(F^2\omega^{-5}\) scaling is therefore not CSL-specific in this admitted
nuisance class.

### Corollary 2 — source-off visibility is not enough

With the branch-dependent force off, \(D(t)=0\) and hence \(I_D=0\). The
source-off Ramsey arm can estimate \(V_0\) and force-independent losses, but
its visibility contains no information about a coefficient multiplying
\(I_D\). Independent electric-field, pressure, temperature, scattering, and
attempt-lineage measurements may bound those coefficients; the source-off
visibility alone does not.

This does not contradict the proposal's statement that electric fields can
be monitored in situ. It types that monitoring as an additional measurement
interface rather than crediting it to the Ramsey visibility automatically.

## 4. Why the finite-width model keeps the route alive

For an isotropic Gaussian pointer, the source's exact CSL rate is

\[
\Gamma_{\rm CSL}^{3D}(t)
=
\lambda\frac{m^2}{m_0^2}
\left(1+\frac{\sigma^2(t)}{r_c^2}\right)^{-3/2}
\left[
1-\exp\!\left(
-\frac{D^2(t)}{4[r_c^2+\sigma^2(t)]}
\right)
\right].
\]

In the small-separation regime this becomes

\[
\Lambda_{\rm CSL}
=
\lambda\frac{m^2}{4m_0^2r_c^2}I_{DG}(r_c),
\]

where

\[
I_{DG}(r_c)
=
\int_0^\tau
D^2(t)
\left[1+\frac{\sigma^2(t)}{r_c^2}\right]^{-5/2}dt
=I_D S_{\rm br}(r_c).
\]

The width \(\sigma(t)\) is set by the prepared thermal state and the tight-to-
weak-trap evolution. It is independent of the controlled force \(F\).

### Corollary 3 — force-amplitude scans remain exactly degenerate

At fixed \(m,\omega,\omega_0,T,r_c\), changing only \(F\) multiplies both
\(I_D\) and \(I_{DG}\) by \(F^2\). The breathing factor \(S_{\rm br}\) remains
constant. Consequently a force-amplitude scan still gives a CSL column
proportional to every shared \(I_D\) nuisance column.

The finite-width correction does not rescue that scan.

### Theorem 2 — breathing-contrast rank repair

For configurations \(i=1,2\), suppose the declared ordinary nuisance is one
shared coefficient times \(I_{D,i}\), while CSL has response
\(I_{D,i}S_i\), where \(S_i=S_{{\rm br},i}(r_c)\). Then

\[
\det
\begin{pmatrix}
I_{D,1}S_1&I_{D,1}\\
I_{D,2}S_2&I_{D,2}
\end{pmatrix}
=
I_{D,1}I_{D,2}(S_1-S_2).
\]

For nonzero paths, CSL amplitude at fixed \(r_c\) and the shared nuisance
coefficient are locally identifiable exactly when

\[
S_1\ne S_2.
\]

The source itself reports, at \(r_c=100\,{\rm nm}\),

\[
S_{\rm br}=4.82\times10^{-2}
\]

for its baseline weak-trap frequency and

\[
S_{\rm br}=2.41\times10^{-2}
\]

for its aggressive frequency. These values prove that the finite-width
response can supply a noncollinear direction. They do **not** by themselves
form a no-refit experiment: the paper associates the two operating points
with different source demands, and the technical-noise spectrum and
apparatus transfer functions must remain common or be independently
calibrated.

### Smallest cleaner implementation

The least-retyping version is to hold \(D(t)\), \(m\), \(q\), the weak trap,
force source, and environment fixed, while changing the prepared width
through the initial tight-trap preparation, for example \(\omega_0\).

That leaves \(I_D\) fixed while changing \(I_{DG}\). It therefore separates
CSL from the source's width-independent \(I_D\) nuisance columns at fixed
\(r_c\).

This control does not make the assay complete. Initial width also changes
the sensitivity to endpoint displacement and momentum mismatch. Those
responses must be measured or included as additional frozen columns. If an
arbitrary width-dependent nuisance is admitted after the data, it can absorb
the CSL column and the repair disappears.

## 5. A second repair: mass-density versus charge coupling

In the pointlike model, consider matched nonzero paths while varying the
physical coupling coordinates. The relevant CSL and white-electric columns
are

\[
K_{{\rm CSL},i}\propto m_i^2I_{D,i},
\qquad
K_{E,i}\propto q_i^2I_{D,i}.
\]

For two configurations,

\[
\det
\begin{pmatrix}
m_1^2I_{D,1}&q_1^2I_{D,1}\\
m_2^2I_{D,2}&q_2^2I_{D,2}
\end{pmatrix}
=
I_{D,1}I_{D,2}
(m_1^2q_2^2-m_2^2q_1^2).
\]

### Theorem 3 — coupling-coordinate rank condition

For nonzero matched paths, pointlike CSL and white electric-field loss are
separable through this two-configuration design exactly when

\[
m_1^2q_2^2\ne m_2^2q_1^2.
\]

Equivalently, the mass-to-charge ratio must change.

This is a conditional design theorem, not an immediate recommendation. In the
source's dipole realization, changing \(q\) changes the force unless the
dipole moment or distance is adjusted. Changing the particle can also change
gas, blackbody, trapping, and geometry coefficients. The realized path and
all those nuisance transfers must be matched or measured. This repair is
therefore more apparatus-sensitive than the preparation-width contrast.

## 6. The nonlinear CSL shape is not the cheap repair here

One might leave the quadratic regime and distinguish CSL through

\[
1-e^{-x},
\qquad
x=\frac{D^2}{4(r_c^2+\sigma^2)}.
\]

The relative difference from the quadratic approximation \(x\) is

\[
\delta(x)
=
1-\frac{1-e^{-x}}{x}.
\]

For \(x\ge0\),

\[
0\le x-(1-e^{-x})\le\frac{x^2}{2},
\]

so

\[
0\le\delta(x)\le\frac{x}{2}
\le
\frac{D_{\max}^2}{8r_c^2}.
\]

At the source's \(r_c=100\,{\rm nm}\):

- baseline \(D_{\max}=0.50\,{\rm nm}\) gives
  \(\delta\le3.125\times10^{-6}\);
- aggressive \(D_{\max}=2.0\,{\rm nm}\) gives
  \(\delta\le5.0\times10^{-5}\).

The finite width makes these bounds smaller. Thus the exact separation
nonlinearity is present but supplies at most a few-parts-per-million to
few-parts-in-\(10^5\) response departure in the proposed operating regime.
It is not the local low-cost attribution lever. A \(D\sim r_c\) redesign
would be a materially different experiment and ordinary environmental
coherence functions could also become nonquadratic.

## 7. Best no-refit response-surface sequence

The source-specific hierarchy is now:

1. **Do not rely on force amplitude.** It changes the common quadratic column.
2. **First use a preparation-width contrast at a matched trajectory.** This
   changes the finite-width CSL factor without intentionally changing
   \(I_D\), charge, mass, source, or interaction time.
3. **Measure width and endpoint mismatch independently.** Otherwise a
   width-dependent technical loss absorbs the new column.
4. **Use an unchanged-source frequency scan only after its noise spectra and
   transfer functions are frozen.** It can vary \(S_{\rm br}\), but it also
   changes duration and filter functions.
5. **Use mass/charge contrast as a stronger but more retyping-prone control.**
6. **Treat \(D\sim r_c\) nonlinearity as a redesign, not a free extra scan.**
7. **For more nuisance columns, require the full rank condition from
   `HC-DU-157`.** Two configurations only solve the one-shared-nuisance case.

At \(\lambda=0\), \(r_c\) remains unidentifiable. A multi-width scan can
identify or constrain \(\lambda\) at a fixed \(r_c\); joint
\((\lambda,r_c)\) inference still requires the two CSL Jacobian directions
to add two ranks beyond the complete nuisance design.

## 8. What Dynamic Unity learned

The important correction is not “CSL is indistinguishable from noise.” It is:

> Path dependence is not enough for provenance. A candidate law needs a
> response coordinate that ordinary admitted mechanisms cannot share.

The source's finite-width suppression, initially treated mainly as a loss of
sensitivity, can become an attribution resource when deliberately varied.
That is the positive design insight.

The negative result is equally concrete. Increasing force or collecting more
points along the same quadratic response surface never creates provenance.
Precision cannot repair missing rank.

This advances the North Star indirectly. It shows how a physical response can
be real and history-dependent while the accessible statistic still fails to
certify which dynamics produced it. It also supplies a disciplined route from
an aggregate response to a rival-excluding certificate:

```text
formed visibility statistic
  -> frozen multi-configuration response surface
  -> independently measured nuisance coordinates
  -> rank against declared rival class
  -> conditional theory-class certificate.
```

It does not select the apparatus, pointer, observer boundary, archive, or
access interface. It therefore does not meet the parked physical-interface
reopener and does not activate a scientific successor.

## 9. Absorption, grade, and stop

The mathematics is absorbed by standard filter-function decoherence,
small-separation environmental expansions, CSL response theory,
nuisance-parameter identifiability, and experimental design.

The Dynamic Unity value is the source-pinned integration:

- it instantiates the abstract attribution quotient from `HC-DU-157`;
- identifies the exact scan that cannot work;
- identifies the smallest response coordinate that can restore rank in the
  source's own finite-width model; and
- prevents a projected loss budget from being mistaken for an acquired
  provenance certificate.

Maximum earned grade is scoped Grade 4. No simulation was needed; the primary
equations and exact determinants decide the gate. No hardware action,
apparatus search, prediction promotion, or paper activation is authorized.
