---
title: "Source-pinned sequential-readout coupling response rank and strong-pump boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-161
run_id: RUN-20260730-114651-source-pinned-coupling-rank
work_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
action_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Source-pinned coupling response rank

## Executive return

```text
MATERIAL_RESPONSE_RANK
+ SINGLE_OUTPUT_NONIDENTIFIABILITY
+ LAW_ONLY_EXPLANATION
+ KNOWN_RESULT_ABSORPTION
+ STRONG_COUPLING_NO_REFIT_FAILURE
```

Dynamic Unity now has one source-pinned physical realization of the abstract
coupling/readout frontier from `HC-DU-160`.

Peronnin, Marković, Ficheux, and Huard physically separate a superconducting
qubit measurement into probe preparation, dispersive interaction,
pump-controlled transfer through a Josephson ring modulator, and amplified
readout. Their apparatus is a Nb-on-Si coplanar-waveguide device with
Al/AlOx/Al Josephson elements, a long-lived readout mode, a lossy buffer mode,
and a tunable beam-splitter coupling. See
["Sequential dispersive measurement of a superconducting
qubit"](https://arxiv.org/abs/1904.04635), *Physical Review Letters* 124,
180502 (2020).

The exact scoped result is:

> In the source's calibrated two-mode model, a response packet containing
> residual readout-population slope plus the phase-calibrated slope and
> curvature of the buffer output locally identifies the pump coupling \(g\)
> against the readout and buffer loss rates whenever \(g\ne0\). Its Jacobian
> determinant is \(g/2\).

The equally important negative is:

> One terminal reset fraction, emitted-energy total, or readout fidelity
> cannot identify the coupling against an admitted loss coefficient. Distinct
> coupling/loss pairs give exactly the same terminal response.

The source itself reports the physical boundary. At strong pump, its
no-free-parameter two-mode description develops discrepancies that can be
fit by changing effective \(g\) and \(\kappa_b\); the authors identify
conversion into unmonitored parasitic modes as a possible explanation.
Therefore the low-pump rank result cannot be transferred to strong pump by
refitting.

This is standard circuit-QED and system-identification physics, not a new
physical law. The useful Dynamic Unity advance is a source-pinned minimum:

```text
prepared internal probe
+ calibrated coupling
+ residual-population response
+ phase-resolved output response
+ fixed timing/gain/loss contract
```

That packet identifies a physical coupling coordinate. It is not yet a
complete formed record: the response arms are calibrated in matched runs,
not joined into one provenance-complete attempt history. Swing 4 is not
activated here.

## 1. Why this platform qualifies

`HC-DU-160` found that a formal instrument depends jointly on coupling and
readout algebra. Swing 3 required one of those coordinates to be physically
instantiated without surveying platforms or importing a held-out target.

The Peronnin platform supplies:

| typed object | source realization |
|---|---|
| system | superconducting transmon qubit |
| probe | high-\(Q\) readout resonator |
| interaction | dispersive qubit–readout coupling |
| controllable transfer | JRM-mediated readout–buffer beam splitter |
| monitored port | lossy buffer resonator and output transmission line |
| internal response | residual readout-mode photon population |
| output response | calibrated complex released-mode amplitude |
| readout functional | weighted integral of the voltage trace |

The device material is fixed. The varied coordinate is not a material species;
it is a materially embodied, pump-controlled coupling. This is admitted
because Swing 2 explicitly returned coupling as a frontier coordinate. The
result does not establish a general “material-substitution law.”

The source's effective beam-splitter Hamiltonian is

\[
H_{\rm bs}
=
\hbar\left(gb^\dagger r+g^*br^\dagger\right),
\tag{1}
\]

where \(g=pg_3\) is proportional to the pump amplitude. The readout and buffer
field amplitudes obey

\[
\dot r=-ig^*b-\frac{\kappa_r}{2}r,
\qquad
\dot b=-igr-\frac{\kappa_b}{2}b.
\tag{2}
\]

These are standard quantum-Langevin/coupled-mode equations. The source
independently calibrates the intrinsic readout decay, buffer response,
coupling-versus-pump curve, residual photon population, and complex output
trace.

## 2. Frozen local identification contract

Choose the center of the symmetric pump pulse and a phase convention such
that

\[
g>0,\qquad \dot g=0.
\]

Prepare

\[
r(0)=A\ne0,\qquad b(0)=0.
\tag{3}
\]

The following are held fixed or independently calibrated:

- \(A\), its phase, and the buffer-output normalization;
- \(\kappa_r\) and \(\kappa_b\);
- pump envelope, phase, amplitude scale, and time origin;
- detunings and the selected magnetic-flux point;
- qubit preparation;
- dispersive/Kerr parameters admitted in the release arm;
- detector gain, phase, DC offset, and efficiency; and
- the declared two-mode completion.

Without these conditions, the rank below is a coordinate calculation rather
than a no-refit physical identification.

Define three normalized local responses:

\[
y_1
=
\frac{d}{dt}\frac{|r(t)|^2}{|A|^2}\bigg|_{0},
\tag{4}
\]

\[
y_2
=
i\frac{\dot b(0)}{A},
\tag{5}
\]

and

\[
y_3
=
-i\frac{\ddot b(0)}{A}.
\tag{6}
\]

The source does not measure these as one simultaneous single-run packet.
It supplies the necessary response types through matched residual-population
and complex-output calibration arms. This is enough for the present
mechanism-identification question and not enough for Swing 4's record packet.

## 3. Exact response-rank theorem

From (2) and (3),

\[
\dot r(0)=-\frac{\kappa_r}{2}A,
\qquad
\dot b(0)=-igA.
\tag{7}
\]

Because \(\dot g(0)=0\),

\[
\ddot b(0)
=
\frac{i}{2}gA(\kappa_r+\kappa_b).
\tag{8}
\]

Equations (4)--(6) are therefore

\[
y_1=-\kappa_r,
\qquad
y_2=g,
\qquad
y_3=\frac{g}{2}(\kappa_r+\kappa_b).
\tag{9}
\]

### Proposition 1 — scoped coupling identifiability

For parameters

\[
\theta=(g,\kappa_r,\kappa_b),
\]

the Jacobian is

\[
J
=
\frac{\partial(y_1,y_2,y_3)}
     {\partial(g,\kappa_r,\kappa_b)}
=
\begin{pmatrix}
0 & -1 & 0\\
1 & 0 & 0\\
\frac{\kappa_r+\kappa_b}{2} & \frac g2 & \frac g2
\end{pmatrix}.
\tag{10}
\]

Its determinant is

\[
\det J=\frac g2.
\tag{11}
\]

Thus \(J\) has full rank whenever \(g\ne0\). In particular,

\[
\partial_g y
\notin
\operatorname{span}
\{\partial_{\kappa_r}y,\partial_{\kappa_b}y\}.
\tag{12}
\]

This is exactly the Swing-3 response-rank criterion. The coupling creates a
phase-resolved transfer response that cannot be reproduced by changing only
the two declared damping rates.

### What the theorem needs

If the output gain is an unknown per-condition parameter, then \(y_2\) and
\(y_3\) acquire the same unknown scale and \(g\) becomes confounded with it.
If the pump time origin or phase may be refit, the local derivatives are not
the same response coordinates. The source's calibration procedures make
these quantities physically meaningful, but Dynamic Unity must keep their
lineage in the eventual packet rather than treating them as free numerical
normalizations.

## 4. Exact one-output nonidentifiability

The positive result requires multiple response types. It cannot be replaced
by one endpoint number.

In the weak-coupling, fast-buffer reduction, adiabatic elimination gives the
readout population decay rate

\[
\Gamma
=
\kappa_r+\frac{4g^2}{\kappa_b}+\kappa_p,
\tag{13}
\]

where \(\kappa_p\) is an admitted unmonitored loss. A terminal residual
population is

\[
R(T)=e^{-\Gamma T}.
\tag{14}
\]

At fixed

\[
\kappa_b=40,\qquad \kappa_r=\frac1{10},
\]

the two parameter pairs

\[
(g,\kappa_p)=\left(1,\frac9{10}\right)
\]

and

\[
(g,\kappa_p)=\left(2,\frac35\right)
\]

both give

\[
\Gamma=\frac{11}{10}.
\]

They therefore give the same \(R(T)\) for every \(T\), while

\[
\frac{4g}{\kappa_b}\in\left\{\frac1{10},\frac15\right\}
\]

keeps both inside the conservative low-coupling scope.

This is not a noise or sample-size problem. In a one-dimensional response
space, the nonzero derivatives of \(R(T)\) with respect to \(g\) and
\(\kappa_p\) are necessarily collinear. More endpoint precision does not add
the missing response direction.

Consequently:

- reset fraction alone does not identify the release mechanism;
- total emitted energy alone does not identify its path or monitored port;
- readout fidelity combines preparation, state change, histogram overlap,
  decay, and detection effects; and
- a single scalar cannot certify that missing energy entered the intended
  output rather than an unmonitored mode.

## 5. Strong-pump no-refit boundary

The source reports two distinct validity boundaries:

1. the reflection-based conversion-rate expression faithfully reproduces
   measurements only for small pump power,
   \(4|g|/\kappa_b<0.7\); and
2. the two-mode release dynamics reproduces residual-population and output
   traces over a wider reported range, approximately
   \(4|g_{\max}|/\kappa_b<1.6\).

The main operating values reported in the source give

\[
\frac{4|g_{\max}|}{\kappa_b}
=
\frac{4(7.2)}{21}
=
\frac{48}{35}
\approx1.37.
\]

That point lies inside the reported release-model range but outside the
strict reflection-calibration range. It is not used as the exact no-refit
positive here.

At the strongest pumps, the measured readout mode empties faster than the
calibrated two-mode model predicts. The source can fit the behavior by
changing effective \(g_{\max}\) and effective \(\kappa_b\), and notes that the
effective increase in \(\kappa_b\) may represent conversion into extra
unmonitored modes.

For Dynamic Unity, that is a typed boundary:

```text
better terminal emptying
  !=
identified intended transfer
  !=
complete monitored record
```

The strong-pump points fail no-refit transfer until the additional modes are
measured or independently bounded. Faster apparent reset is not evidence that
the selected record interface became more complete.

## 6. Selected-versus-supplied ledger

| object | status |
|---|---|
| physical platform and materials | source-pinned |
| readout/buffer mode split | source architecture |
| JRM beam-splitter coupling law | source-derived standard model |
| pump amplitude and envelope | controlled/supplied |
| \(g\)-versus-pump calibration | source-measured in scoped regime |
| \(\kappa_r,\kappa_b\) | source-calibrated |
| residual readout response | source-measured in matched calibration arm |
| complex output response | source-measured with calibrated weight function |
| three-response rank | derived exactly |
| one-output coupling/loss twins | exact counterexample |
| detector gain, phase, time zero, action class | supplied/frozen |
| parasitic-mode completion at strong pump | unselected/incomplete |
| one-run joined attempt lineage | absent |
| actual outcome and durable archive | not adjudicated here |
| observer access and certification | supplied |
| anomalous response or new law | absent |

## 7. Absorber audit

The mathematical positive is not novel. Passive linear quantum-system
identification already asks which internal parameters can be reconstructed
from controlled inputs and measured outputs. Minimal systems are identifiable
only up to their admitted mode equivalences, and transfer-function
identification depends on controllability/observability. See
[Guta and Yamamoto](https://arxiv.org/abs/1303.3771).

The source paper itself performs coupling calibration, residual-mode
measurement, output-trace comparison, and parameter-regime validation.
Classical linear-system identifiability, quantum input-output theory,
observability rank, and Fisher/design methods absorb the rest.

Dynamic Unity's contribution is therefore not the determinant in isolation.
It is the campaign-level typing:

- the abstract coupling coordinate from `HC-DU-160` has one physical
  realization;
- the least informative endpoint is exactly insufficient;
- a calibrated multi-response packet is sufficient at the declared scope;
- strong-pump model repair is completion refitting, not inherited
  identification; and
- physical mechanism identification still precedes record formation,
  provenance, and observer access.

## 8. Campaign disposition

The pre-registered return is:

```text
MATERIAL_RESPONSE_RANK
+ SINGLE_OUTPUT_NONIDENTIFIABILITY
+ LAW_ONLY_EXPLANATION
+ KNOWN_RESULT_ABSORPTION
+ STRONG_COUPLING_NO_REFIT_FAILURE
```

Swing 3 is complete at scoped Grade 4. It establishes a source-pinned
coupling-response coordinate under standard physics. It does not establish
new physics, an observer-selected interface, or a complete record.

Swing 4 is scientifically eligible on the same platform. Its exact task is
to determine whether the sequential measurement supplies a joined
blank-to-written, one-run, retained, provenance-bearing, accessible,
resettable record with a held-out action consequence—or only several
separately calibrated response arms. Swing 4 remains inactive until separate
authorization.

## Reproducibility

The exact rank and endpoint-twin controls are in:

```text
tests/du_source_pinned_coupling_response_rank_probe.py
tests/artifacts/du_source_pinned_coupling_response_rank_result.json
```

Passing proves only the local Jacobian and one-output counterexample in the
frozen two-mode model. It establishes no complete record packet, physical
selector, anomalous response, empirical result, new law, or new physics.
