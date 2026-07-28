---
title: "Finite-time infrared-memory typed-record reopener audit"
status: completed_scoped_reopener_audit
doc_type: primary_source_scope_audit_partial_selection_classification_and_gate_disposition
created: 2026-07-28
claim_id: HC-DU-068
work_id: IR-MEMORY-TYPED-RECORD-REOPENER-AUDIT
program_id: CCR-FINITE-TIME-IR-MEMORY-SELECTOR
run_id: RUN-20260728-070346-ir-memory-reopener-audit
claim_grade: "SCOPED GRADE-4 REOPENER DISPOSITION + GRADE-3 PARTIAL PHYSICAL TYPING / COMPONENT PHYSICS ABSORBED"
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Finite-time infrared-memory typed-record reopener audit

## Executive verdict

The 2026 source packet warrants reopening and completing the **audit**, but it
does not satisfy Dynamic Unity's parked infrared-memory **scientific
reopener**.

The exact disposition is:

```text
PARTIAL_PHYSICAL_TYPING
```

The sources establish more than the previously parked asymptotic sketch:

1. QED and perturbative-gravity dynamics form long-range soft structure tied
   to scattering.
2. Within a supplied constant-time/asymptotic frame, retained time dependence
   plus rotational symmetry conditionally selects the gauge-fixing part of a
   Faddeev--Kulish dressing.
3. Finite detector resolution remains in observable inclusive statistics and
   in the hard-sector reduced state.
4. Local QFT causality is weaker than physical operation realizability, and a
   broad class of diagonal Weyl instruments has an explicit realizability
   route.

But the packet still does not select a finite operational record:

- Oertel's “finite-time detector” is defined on fixed constant-\(t\) surfaces
  while its memory result still takes \(L\to\infty\),
  \(\omega_0\to0\), and \(t\to\infty\) in a coupled asymptotic limit.
- The rotational selector acts only after a time direction and rotational
  subgroup have been supplied.
- Fukuyama's detector resolution \(\omega_{\max}\) is a physical apparatus
  parameter, not a value selected by QED. It therefore indexes a family of
  observer quotients.
- Neither paper selects a detector worldtube, bounded observation window,
  access algebra, blank archive, provenance-bearing write, decoder, action
  class, or certification/finality rule.
- No independently frozen held-out hard-process target and no inverse
  reconstruction theorem are supplied.
- The Fewster--Verch results constrain which supplied instruments are
  realizable; they do not select one instrument.

The likely physical picture is consequently typed but split:

```text
gauge dynamics
    -> soft memory carrier

supplied asymptotic frame + rotational symmetry
    -> conditionally selected dressing component

supplied detector/worldtube/window/resolution/instrument
    -> observable record quotient

supplied observer actions and target
    -> reconstruction or first-leak question
```

This is a useful mixed result. Physics selects more of the **carrier** than
Dynamic Unity had previously credited, while the operational **record
interface** remains supplied.

## 1. Frozen primary-source packet

### Oertel

Brett Oertel,
[“Finite-time memory detectors and fully constraining Faddeev--Kulish
dressings in QED and gravity”](https://arxiv.org/abs/2605.06774),
arXiv:2605.06774v1, submitted 7 May 2026.

The paper treats massive scalar QED and a massive scalar coupled to
perturbative quantum gravity. Its central result is a time-dependent
Faddeev--Kulish construction in which the gauge-fixing function is fixed by a
unique rotationally invariant choice and the resulting dressed states
reproduce classical electromagnetic and gravitational memory.

### Fukuyama

Takeshi Fukuyama,
[“Detector Resolution and Observable Infrared Memory in
QED”](https://arxiv.org/abs/2606.08879),
arXiv:2606.08879v1, submitted 7 June 2026.

The paper emphasizes that the unphysical infrared regulator cancels while the
physical detector resolution \(\omega_{\max}\) remains in inclusive
observables. It proposes using this scale to divide observed from unresolved
soft modes and traces the latter out of the hard-sector density matrix.

### Mandrysch--Simmons--Navascués

Jan Mandrysch, Robin Simmons, and Miguel Navascués,
[“Causality and realizability of local operations in quantum field
theory”](https://arxiv.org/abs/2607.12976),
arXiv:2607.12976v1, submitted 14 July 2026.

The paper proves that causal QFT operations and Fewster--Verch-realizable
operations are not the same class. It gives causal channels that cannot be
approximated by Fewster--Verch schemes, shows network implementability is
undecidable for a countable Weyl-channel class under its assumptions, and
proves a broad diagonal-Weyl/random-displacement class realizable.

All three are current preprints. This audit treats their stated mathematics as
source claims at its exact scope; it does not promote peer-review status or
extend their results beyond the declared models.

## 2. What “finite-time” selects—and what it does not

Oertel keeps the factor

\[
\exp\!\left(it\,\frac{p\!\cdot\!k}{\omega_p}\right)
\]

in the dressing. The factor is often dropped when only asymptotic
\(S\)-matrix elements are needed, but Oertel shows that it contributes to the
subleading memory calculation. The memory probe frequency is tied to time by

\[
\omega_0
=
\frac{2\pi\omega_p}{t\,p\!\cdot\!\widehat y}.
\]

Within the chosen frame this relation is supported independently by
large-gauge-charge conservation. The QED and gravity gauge-fixing functions
are then fixed by the unique rotationally invariant null direction

\[
q_\mu(k)=(1,-\widehat{\mathbf k}).
\]

This earns a real conditional selector:

> Given the fixed constant-time scattering representation, the dressing
> constraints, the retained \(t\)-dependence, and the selected rotation
> subgroup, the gauge-fixing component is not freely chosen.

It is not yet a frame-free physical record selector:

1. The decomposition \(k=(\omega_k,\mathbf k)\), constant-\(t\) surfaces, and
   “rotationally invariant” subgroup already supply a timelike direction.
2. The construction still contains an arbitrary smoothing function
   \(\varphi(k,p)\), constrained to equal one near \(k=0\) and decay at high
   momentum. The zero-mode memory may be insensitive to this freedom, but the
   full dressing is not literally a single parameter-free object.
3. The detector sends the field to future null infinity
   (\(L\to\infty\)), probes the zero mode
   (\(\omega_0\to0\)), and couples that limit to \(t\to\infty\).
4. Oertel explicitly describes the construction as a step toward Fock spaces
   at finite distance, not as the completed finite-distance detector theory.

Thus:

```text
defined on a finite-t surface with retained time dependence
    !=
available to a bounded observer at finite distance and duration.
```

The title's “finite-time” is technically meaningful, but it does not by
itself fire Dynamic Unity's finite-access gate.

## 3. Selected/supplied/fitted ledger

| Component | Source status | Dynamic Unity classification | Consequence |
|---|---|---|---|
| Massive scalar QED / scalar perturbative-gravity action | Fixed model premise | `EXTERNALLY_SUPPLIED` | Defines the arena; not selected by the memory result |
| In/out scattering process and amplitudes | Calculated under the action and prepared states | `DERIVED_AFTER_SELECTION` relative to supplied preparations | Physical process exists, but no observer record follows automatically |
| Soft \(p/(p\cdot k)\) factor | Required by infrared dynamics | `DYNAMICALLY_SELECTED` within the fixed theory | Genuine physical carrier/dressing structure |
| Retained \(t\)-dependent exponential | Derived in asymptotic dynamics and required for subleading memory | `DYNAMICALLY_SELECTED` within the fixed representation | Stronger than a timeless asymptotic label |
| Constant-\(t\) slicing and asymptotic rest frame | Used by the canonical construction | `EXTERNALLY_SUPPLIED` | The rotation selector is conditional on this structure |
| Gauge-fixing \(c_\mu,c_{\mu\nu}\) / \(q_\mu\) | Unique under the declared rotational symmetry and constraints | `SYMMETRY_SELECTED` after the frame is supplied | Real partial selection, not full interface selection |
| Smoothing function \(\varphi\) | Any admissible function with specified IR/UV behavior | `EXTERNALLY_SUPPLIED`; likely IR-irrelevant to the zero mode | Blocks a literal claim that every dressing detail is selected |
| Memory operator | Defined to probe the classical soft-memory zero mode | `EXTERNALLY_SUPPLIED` observable, then validated | Dynamics predicts its value; dynamics does not choose that it is the observer's record |
| \(L\to\infty,\omega_0\to0,t\to\infty\) limits | Integral parts of the calculation | `DERIVED_AFTER_SELECTION`, but asymptotic | No bounded access theorem |
| Detector resolution \(\omega_{\max}\) | Survives in observable cross sections | `EXTERNALLY_SUPPLIED` physical apparatus parameter | Selects a family \(R_{\omega_{\max}}\), not one record |
| Hard/soft trace split at \(\omega_{\max}\) | Proposed operational coarse graining | `EXTERNALLY_SUPPLIED` split, with derived reduced state | Makes access typing explicit but does not select the boundary |
| Soft overlap \(D_{ij}(\omega_{\max})\) | Derived after the split and dressing are fixed | `DERIVED_AFTER_SELECTION` | Resolution-relative information diagnostic |
| Blank state, write epoch, and retained provenance | Not supplied | missing | Correlation with an out state is not yet a provenance-bearing archive |
| Local algebra / spacetime region | AQFT supplies a net relative to a chosen region and state/sector | `DERIVED_AFTER_SELECTION` from supplied region/state | Locality constrains admissible access but does not select the observer region |
| QFT instrument | Fewster--Verch realization uses probe theory, probe state, coupling, and POVM | `EXTERNALLY_SUPPLIED`, then realizability-tested | Realizability is not selection |
| Observer decoder, actions, horizon, and resources | Not supplied | missing | No operational certificate or capability claim |
| Held-out hard-process target | Not frozen | missing | No reconstruction or first-leak theorem |
| Public finality / rival-excluding certification | Not supplied | missing | Memory is not promoted to public final fact |

## 4. Resolution dependence is physical typing, not a selector

For a chosen detector resolution \(\omega_{\max}\), Fukuyama defines

\[
\rho_{\mathrm{hard}}(\omega_{\max})
=
\operatorname{Tr}_{\omega<\omega_{\max}}
|\Psi\rangle\langle\Psi|
\]

and the corresponding soft overlap

\[
D_{ij}(\omega_{\max})
=
\langle\gamma_j|\gamma_i\rangle_{\mathrm{soft}}.
\]

This is directly useful to Dynamic Unity because it makes the observer
quotient explicit. It also closes the proposed shortcut:

> QED determines observables conditional on detector resolution; it does not
> choose the detector resolution or thereby select one observer-accessible
> record equivalence.

Formally, let \(\Theta\) denote the admissible detector contract—worldtube,
duration, angular response, frequency resolution, local algebra, instrument,
and decoder. The source packet supplies a family

\[
R_\Theta:\mathcal C\longrightarrow\mathcal Q_\Theta.
\]

If the physical antecedent admits more than one \(\Theta\) and supplies no
selector

\[
s:\mathcal C_{\mathrm{antecedent}}\longrightarrow\Theta,
\]

then it does not select one operational record map \(R\). This is the
source-specific instance of the existing `HC-DU-033F/054/063` interface
factorization boundary. It is not new general mathematics.

### Printed-overlap caution

Fukuyama defines \(B_{ij}\) from the integral of
\(|f_i-f_j|^2\), hence \(B_{ij}\ge0\), but Eq. (17) as printed gives

\[
D_{ij}^{\mathrm{obs}}
\simeq
\exp\!\left[
-\frac12 B_{ij}\ln\frac{\omega_{\max}}{m}
+i\Phi_{ij}
\right].
\]

In the ordinary soft regime \(\omega_{\max}<m\), the printed real exponent is
positive and the magnitude exceeds one, which is incompatible with its
interpretation as a normalized-state overlap unless a scale convention or
sign not stated in the three-page paper changes the reading. The qualitative
resolution-dependence claim is standard and survives this issue; the exact
normalization/sign should not carry a Dynamic Unity theorem without
correction or independent derivation.

## 5. Target-leakage audit

Oertel presents two routes together:

1. retain the full time dependence, enforce large-gauge-charge conservation,
   and choose the unique rotationally invariant gauge-fixing function; and
2. require exact reproduction of the classical memory result for all
   scattering states.

The paper explicitly argues that route 1 can select the relevant dressing
without first using the memory result. Dynamic Unity therefore does **not**
classify the entire result as target-fitted.

The separation must remain explicit:

```text
independent selector:
  time dependence + constraints + supplied frame + rotational symmetry

held-out check:
  classical memory reproduction
```

If a later DU proof instead defines “correct dressing” by reproduction of the
classical memory target and then cites that reproduction as confirmation,
`TARGET_LEAKAGE` fires. The current source offers an avoidable leakage risk,
not a demonstrated unavoidable circularity.

The more important missing target is different. Classical memory is the
forward observable being reproduced. Neither Oertel nor Fukuyama freezes a
hard-process target \(T\) and proves either

\[
T=t\circ R_\Theta
\]

on a nonempty physical completion class or an explicit
same-record/different-\(T\) witness. The inverse Dynamic Unity question is
therefore unasked, not answered negatively.

## 6. Local-QFT realizability is a filter, not the missing dynamics

Mandrysch--Simmons--Navascués sharply improves the future operational gate:

- Einstein causality alone admits mathematical channels that cannot be
  approximated by Fewster--Verch measurement schemes.
- A broad diagonal Weyl/random-displacement class is Fewster--Verch
  realizable and supports nondemolition quadrature measurements.
- General network implementability is undecidable for the paper's countable
  Weyl-channel class under the split-property assumptions.

Consequently a future finite memory instrument should use one of two exact
routes:

1. provide an explicit Fewster--Verch realization as a positive witness; or
2. prove a declared obstruction or separating inequality for the candidate.

It should not launch an unconstrained search for a universal realizability
classifier.

Even a positive realization still begins with a probe theory, probe state,
localized coupling, and probe POVM. It proves that a proposed interface can
be physically implemented. It does not prove that the source dynamics
selects that interface.

```text
causal
    !=
locally realizable
    !=
dynamically selected
    !=
formed provenance-bearing record
    !=
observer-accessible final fact.
```

## 7. Activation-gate decision

| Gate | Result | Reason |
|---|---|---|
| At least one nontrivial record-interface component independently selected | **Partial / insufficient** | A dressing component is conditionally selected, but no detector, archive, access map, or complete interface is |
| Bounded observer-access contract without replacing the source by a freely supplied detector | **Fail** | The detector remains asymptotic; finite resolution is detector supplied |
| Independently held-out hard-process or future-response target after freezing the interface | **Fail** | No inverse target or completion fibre is part of the source results |

The next four proposed swings are therefore **not activated**.

## 8. Earned result and grade

`HC-DU-068` earns:

- a scoped Grade-4 disposition of the exact parked reopener;
- a Grade-3 partial-physical-typing classification of the source packet;
- a sharper separation of carrier, dressing, detector quotient, formed
  record, access, and target reconstruction;
- one exact source-specific instance of interface nonselection; and
- a bounded positive class for any future local-QFT realization witness.

It does not earn:

- a universal theorem against infrared records;
- a finite-distance or finite-duration memory detector;
- an independently selected observer, resolution, instrument, archive,
  decoder, or action class;
- a hard-process reconstruction theorem;
- a same-record/different-target physical remainder;
- public finality, new dynamics, new prediction, paper, model, experiment,
  hardware, or provider work; or
- activation of `H-CCR-17`.

The component physics is absorbed by infrared-safe scattering, asymptotic
symmetry and memory, detector-relative coarse graining, AQFT measurement
theory, and existing Dynamic Unity interface-selection mathematics.

## 9. Stop and exact reopener

### Stop

Do not:

- infer bounded access from the phrase “finite-time”;
- call a soft cloud, asymptotic charge, or memory eigenvalue a certified
  observer record;
- treat \(\omega_{\max}\) as selected by QED;
- use a realizable supplied instrument as evidence of endogenous selection;
- use classical-memory matching both to select and validate a dressing;
- build an infrared toy or seek external hardware; or
- run dressing naturality, formation, reconstruction, or QED-to-gravity
  transfer as committed follow-on swings.

### Reopen

Reopen only with one source or construction that simultaneously provides:

1. a finite detector worldtube, observation duration, frequency/angular
   resolution, and local instrument with an explicit positive
   Fewster--Verch-style realization or equally strong physical implementation
   witness;
2. an independent physical selector or naturality theorem for that detector
   class and observer-access quotient;
3. a blank-to-written occurrence and retained provenance/archive map;
4. a nonempty physical completion fibre and independently frozen held-out
   hard-process or future-response target;
5. a law-only baseline and proof of record-conditioned target contraction or
   an exact same-record/different-target witness; and
6. gauge, frame, dressing, and resolution changes typed as invariances,
   observer indices, or genuine interface changes rather than silently
   refitted.

Until then the portfolio returns:

```text
HC-DU-068: complete
IR_MEMORY_CARRIER: physically formed in the frozen source classes
FK_GAUGE_FIXING_COMPONENT: conditionally symmetry-selected
FINITE_OPERATIONAL_RECORD_INTERFACE: not selected
HARD_PROCESS_RECONSTRUCTION: not tested
H-CCR-17: not reopened
LOCAL_MODEL: not warranted
EXTERNAL_HARDWARE: not relevant
NEXT_SCIENTIFIC_ACTION: unselected
```
