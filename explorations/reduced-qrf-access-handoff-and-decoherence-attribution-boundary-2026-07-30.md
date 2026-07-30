---
title: "Reduced QRF access handoff and decoherence-attribution boundary"
status: completed_scoped_result
doc_type: primary_source_collision_exact_handoff_control_and_attribution_boundary
created: 2026-07-30
hypothesis_id: HC-DU-153
run_id: RUN-20260730-064834-qrf-access-attribution-handoff
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 imported necessity theorem, exact access-handoff control, and environment/reference attribution nonidentifiability; Grade 5 only after a physically selected formed-record interface yields no-refit excess over standard quantum theory"
probe: "../tests/du_qrf_access_attribution_handoff_probe.py"
artifact: "../tests/artifacts/du_qrf_access_attribution_handoff_result.json"
---

# Reduced QRF access handoff and decoherence-attribution boundary

## Executive result

The swing returned:

```text
PHYSICAL_QUANTUM_REFERENCE_AND_ACCESS_REDUCTION_ARE_EXPLICIT
+ REDUCED_QRF_MAP_IS_CPTP_AFTER_A_DECLARED_PARTIAL_TRACE
+ BLOCK_PRESERVATION_ALONE_DOES_NOT_PRESERVE_POPULATIONS_IN_TIME
+ DYNAMIC_COMPATIBILITY_IFF_UNIFORM_FACTORIZED_POPULATION_PRESERVATION
+ THIS_IS_AN_EXACT_CANDIDATE_HANDOFF_CONDITION_NOT_A_FORMED_RECORD_THEOREM
+ LOCAL_COHERENCE_EQUALS_ENVIRONMENT_FACTOR_TIMES_REFERENCE_FACTOR
+ LOCAL_DECOHERENCE_RATE_EQUALS_ENVIRONMENT_RATE_PLUS_REFERENCE_RATE
+ ONE_COMPLETE_LOCAL_RAMSEY_CURVE_DOES_NOT_IDENTIFY_THAT_SPLIT
+ TWO_UNCALIBRATED_LOCAL_REFERENCES_RETAIN_A_COMMON_MODE_GAUGE
+ INDEPENDENT_REFERENCE_CALIBRATION_OR_SOURCE_SELECTIVE_VARIATION_RESTORES_RANK
+ THE_ACCESS_BOUNDARY_PVMS_ASSIGNMENT_AND_REFERENCE_PROTOCOL_REMAIN_SUPPLIED
+ SAME_EXPERIMENT_REDESCRIBED_IS_INVARIANT
+ DIFFERENT_LOCAL_PHASE_STANDARDS_DEFINE_DIFFERENT_EXPERIMENTS
+ STANDARD_QRF_OPEN_SYSTEM_AND_IDENTIFIABILITY_THEORY_ABSORB_THE_MATHEMATICS
+ NO_NEW_PHYSICS_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

Luppi, Kabel, Giacomini, and Smirne's
[Reduced Quantum-Reference-Frame Channels for Open Quantum
Systems](https://arxiv.org/abs/2607.05578) gives Dynamic Unity a much better
mathematical specimen for an **access-relative handoff** than an informal
observer analogy. The reference is a physical quantum system. Changing
reference reshuffles the subsystem description, and tracing degrees that are
inaccessible in the new description produces a reduced CPTP channel.

The source proves a necessary-and-sufficient condition for a chosen block
population to remain constant through this handoff. In Dynamic Unity
language, this is the right *shape* for a fact-preserving transfer rule:
kinematic agreement of the block labels is insufficient; the pulled-back
output effects must also be dynamically compatible with the inaccessible
conditional evolution.

It is not yet a theorem about formed, certified, or final records. The source
fixes the system/reference/environment factors, QRF transformation, access
boundary, input assignment, PVMs, and Ramsey protocol. It derives what follows
from that packet but does not select the packet from dynamics.

The paper also provides an unusually clean attribution boundary. In its
Hamiltonian-symmetric regime,

\[
\rho^{(B)}_{nm}(t)=F_{nm}(t)\rho^{(A)}_{nm}(t),
\tag{1}
\]

so a local observer tied to reference \(B\) infers

\[
\gamma^{(B)}_{nm}(t)
=\gamma^{(A)}_{nm}(t)+\gamma^{\mathrm{fr}}_{nm}(t).
\tag{2}
\]

A complete local Ramsey visibility curve determines the product in Equation
(1), not the two factors. The source itself correctly requires independent
control or calibration of the reference. The exact fixture below turns that
statement into the smallest rank certificate and shows that comparing two
uncalibrated references is still insufficient for an absolute split.

This is useful and physically substantive known science. It is not excess
content over quantum theory, a selected record interface, or a new Dynamic
Unity prediction.

## 1. Exact source passport

The primary source's central reduced channel is

\[
\mathcal Q[\rho]
=\operatorname{Tr}_{AE}
\!\left[
  \hat S_{A\rightarrow B}\rho\hat S_{A\rightarrow B}^{\dagger}
\right],
\tag{3}
\]

where \(S\) is the target system, \(A\) and \(B\) are old and new physical
reference systems, and \(E\) is an environment. The output retains only \(S\)
relative to \(B\); \(A\) and \(E\) are declared inaccessible and traced out.

| Object | Source status | Dynamic Unity reading |
|---|---|---|
| Hilbert factors \(S,B,E\) relative to \(A\) | supplied | subsystem typing, not selected ontology |
| symmetry group and representation \(V_{SE}(g)\) | supplied by the model | physical covariance packet |
| QRF unitary \(\hat S_{A\to B}\) | constructed within that packet | selected by the chosen QRF model, not by arbitrary dynamics |
| accessible algebra “only observables on \(S\)” | explicitly assumed | physical access boundary remains supplied |
| reduced channel \(\mathcal Q\) | derived by unitary conjugation and partial trace | exact access-reduction map |
| system-only dynamics \(\Lambda_t\) | defined only after a fixed factorized assignment | preparation-dependent, not canonical |
| input and output PVMs | fixed; may be motivated by energy, pointer, or symmetry | candidate fact coordinates remain supplied |
| controlled dephasing propagator | supplied physical dynamics | lawful conditional evolution |
| compatibility commutator | derived | exact preservation criterion |
| reference distribution \(p_t(g)\) | induced by a supplied/evolving reference state | physical nuisance or resource |
| Ramsey pulses and local phase standard | operationally specified | measurement/interface packet |
| gravity-motivated environment | supplied case study | comparator, not observed intrinsic gravity signal |
| blank-to-written event, archive, provenance, access certificate | not constructed | no formed record or finality theorem |

The source is unusually explicit about several of these boundaries:

- \(\mathcal Q\) acts on the joint input and is not a dynamical map on \(S\)
  alone.
- A system-only CPTP map requires a factorized initial assignment.
- The PVMs are formally arbitrary, and the transformed Hamiltonian need not
  define a canonical local Hamiltonian after the subsystem reshuffle.
- “Only \(S\) is accessible” is the premise that licenses the partial trace.

That makes the paper a strong typed input to Dynamic Unity and prevents the
common overreading that a reduced state has selected its own observer or
record interface.

## 2. Exact access-handoff theorem

### 2.1 Published theorem

Let the old-frame controlled dynamics be

\[
U^{(A)}(t)=\sum_m P_m^{(A)}\otimes U_m^{(A)}(t).
\tag{4}
\]

Suppose the reduced QRF channel is block preserving:

\[
\mathcal Q^\dagger(\widetilde P_n^{(B)})
=\sum_m P_m^{(A)}\otimes\Pi_{nm}^{(A)}.
\tag{5}
\]

For nondegenerate blocks and all factorized initial preparations, Luppi et
al.'s Theorem 4.2 proves

\[
p_n^{(B)}(t)=p_n^{(B)}(0)\quad\forall n,t
\quad\Longleftrightarrow\quad
[\Pi_{nm}^{(A)},U_m^{(A)}(t)]=0\quad\forall n,m,t.
\tag{6}
\]

For time-dependent output effects, the corresponding condition is

\[
U_m^\dagger(t)\Pi_{nm}(t)U_m(t)=\Pi_{nm}(0).
\tag{7}
\]

The universal quantifier over factorized inaccessible preparations matters.
For one fixed preparation, constancy can occur accidentally and compatibility
need not follow.

### 2.2 Dynamic Unity interpretation

Equation (6) is an exact **handoff criterion**:

> A chosen block-valued fact survives a physical reference/access change for
> every admitted factorized preparation exactly when the target block effect,
> pulled back to the old description, is invariant under each corresponding
> inaccessible conditional evolution.

This is sharper than “the observers agree” and stronger than kinematic block
preservation. It separates:

1. identifying which input coherences are irrelevant to an output block;
2. keeping that output population fixed while inaccessible degrees evolve;
3. selecting the PVM as a physical record;
4. forming and archiving an actual outcome; and
5. certifying it for another agent.

Only the first two are proved here.

### 2.3 Smallest exact control

The source's \(\mathbb Z_2\) example gives

\[
\Pi_{00}=|0\rangle\!\langle0|_B\otimes I_E.
\tag{8}
\]

Take the system initially in input block \(m=0\) and \(B\) in
\(|0\rangle\). If the conditional inaccessible evolution flips the reference,
\(U_0=X_B\), then

\[
[\Pi_{00},X_B]\ne0,\qquad
p_0^{(B)}:1\longmapsto0.
\tag{9}
\]

The channel remains block preserving; population preservation fails because
dynamical compatibility fails.

For the commuting control \(U_0=Z_B\),

\[
[\Pi_{00},Z_B]=0,\qquad
p_0^{(B)}:1\longmapsto1.
\tag{10}
\]

The exact regression preserves both cases. This is not a simulation of a
laboratory QRF; it is the smallest finite witness for why the dynamical
condition is load bearing.

## 3. Environment/reference attribution theorem

### 3.1 Product and additive-rate forms

In the paper's classical-misalignment, Hamiltonian-symmetric regime, the
environmental coherence factor and frame factor multiply. Wherever neither
factor vanishes,

\[
\begin{aligned}
c_{\mathrm{local}}(t)
  &=F_{\mathrm{ref}}(t)c_{\mathrm{env}}(t),\\
\gamma_{\mathrm{local}}(t)
  &=-\frac{d}{dt}\log|c_{\mathrm{local}}(t)|\\
  &=\gamma_{\mathrm{env}}(t)+\gamma_{\mathrm{ref}}(t).
\end{aligned}
\tag{11}
\]

Therefore a local visibility record has the source-sensitivity row

\[
A_{\mathrm{local}}=\begin{bmatrix}1&1\end{bmatrix},
\qquad
\ker A_{\mathrm{local}}
=\operatorname{span}\{(1,-1)\}.
\tag{12}
\]

For example,

\[
(\gamma_{\mathrm{env}},\gamma_{\mathrm{ref}})
=(2,3)
\quad\text{and}\quad
(4,1)
\tag{13}
\]

both give

\[
\mathcal V(t)=\mathcal V(0)e^{-5t}
\tag{14}
\]

for every \(t\). More samples of the same curve improve precision but not
source rank.

The functional version is the same: whenever admissibility is preserved, a
nonzero factor \(h(t)\) can be moved between
\(c_{\mathrm{env}}\) and \(F_{\mathrm{ref}}\) without changing their product.
The claim is scoped to the model class in which both refactorized terms remain
valid physical coherence factors.

### 3.2 Why two uncalibrated references are not enough

Suppose the same environment is measured using two uncalibrated local phase
standards:

\[
\begin{bmatrix}
\gamma_1\\
\gamma_2
\end{bmatrix}
=
\begin{bmatrix}
1&1&0\\
1&0&1
\end{bmatrix}
\begin{bmatrix}
\gamma_{\mathrm{env}}\\
\gamma_{\mathrm{ref},1}\\
\gamma_{\mathrm{ref},2}
\end{bmatrix}.
\tag{15}
\]

The matrix has rank two and null direction

\[
(-1,1,1).
\tag{16}
\]

The comparison identifies the relative degradation of the standards, not the
absolute environmental contribution. “Use another observer” is not by itself
an attribution repair.

An independent characterization of one reference adds the row
\([0,1]\) to \([1,1]\). The resulting determinant is one, so both source
coordinates are identified. Equivalent repairs include:

- a stabilized reference whose residual contribution is independently
  bounded;
- a controlled variation of reference diffusion with a calibrated response;
  or
- a parameter intervention known to affect the environment but not the
  reference.

These are physical first-leak rows, not reinterpretations of the same local
trace.

### 3.3 Gravity-motivated warning

In the paper's harmonic-oscillator example,

\[
\gamma_{nm}^{(B)}(t)
=(n-m)^2\Omega^2\dot\chi_{\mathrm{grav}}(t)
+\frac{(n-m)^2}{2}\frac{d\sigma_\theta^2(t)}{dt}.
\tag{17}
\]

Both terms have the same quadratic energy-gap dependence. Observing that
scaling therefore does not uniquely identify gravitational decoherence. The
paper names independent reference calibration and environment-selective
parameter changes as the repair. Dynamic Unity should treat this as a
permanent attribution control for any phase-reference-based gravity signal.

## 4. Same description versus different procedure

The source makes a distinction that should remain explicit throughout
Dynamic Unity:

- If Alice and Bob describe the **same physical Ramsey interferometer**, both
  the state and measurement transform under the QRF change and the outcome
  statistics remain invariant.
- If Alice and Bob each run a **local Ramsey experiment tied to their own
  physical phase standard**, they implement different operational procedures
  and may infer different decoherence rates.

This is not subjectivism and not an inconsistency in the global physics. The
reference is a physical part of the measurement packet. The local rate is
relational to that packet.

It also sharpens `HC-DU-149`. That result established that a complete
state--dynamics--readout tuple must transform together. `HC-DU-153` adds a
source-native case where two physically different local readouts can produce
different reduced rates and identifies the exact reference-calibration row
needed to attribute the difference.

## 5. What this changes for Dynamic Unity

### 5.1 Earned update

Dynamic Unity now has a primary-source quantum theorem with the exact
architectural form it had been seeking for regional or observer-relative
handoff:

\[
\text{kinematic block preservation}
+\text{dynamical compatibility}
\Longleftrightarrow
\text{uniform population survival}.
\tag{18}
\]

That is a valuable bridge between the repo's distributed-systems intuition
and orthodox quantum theory. A locally stable block label need not remain
stable after an access/reference transition. The hidden conditional dynamics
must respect the pulled-back output effect.

The result also supports a precise physical—not cognitive—reading of
observer indexing. What an observer can measure depends on a physical
reference and an accessible algebra. The complete experiment remains
consistent across descriptions.

### 5.2 What remains unearned

The source does not establish that:

- its PVM blocks are formed records;
- dynamics selects one PVM, factorization, or access boundary;
- population constancy is archival finality;
- a QRF change creates facts;
- regional finality is a fundamental layer of physics;
- reference-induced decoherence is new physics;
- local rate differences reveal a physical remainder; or
- any result exceeds standard quantum mechanics.

The imported theorem and DU adapter are therefore a scoped Grade-4
necessity/nonidentifiability result with low novelty debt, not a blockbuster.

### 5.3 Exact reopener

A scientific successor exists only if one physical model supplies, without
target-dependent refitting:

1. a dynamically selected subsystem/reference decomposition;
2. a selected accessible algebra and input/output block algebra;
3. blank-to-written formation and a retained archive;
4. the reduced QRF map and admitted inaccessible preparation class;
5. compatibility or a measured failure of it;
6. independent reference calibration;
7. a held-out target or cross-reference transfer; and
8. excess over the corresponding standard-QM channel model.

Until then, further QRF toy construction would reproduce known channel
theory. No current program reopen rule is met, so no successor, hardware
path, prediction, or paper is activated.

## 6. Grade and disposition

| Dimension | Disposition |
|---|---|
| Mathematical correctness | exact in the source theorem and finite fixture |
| Physicality | physical QRF/open-system model, conditional on supplied typing |
| DU novelty | typed synthesis and two-reference rank guard; mathematics absorbed |
| Evidence grade | scoped Grade 4 necessity/nonidentifiability |
| Excess over QM | none |
| Record selection | absent |
| Hardware need | none |
| Portfolio effect | bank result; remain quiescent |

## 7. Exact local evidence

Run:

```bash
python3 tests/du_qrf_access_attribution_handoff_probe.py --write-artifact
```

The regression checks:

- the \(\mathbb Z_2\) output effect is a projector and completes a POVM;
- a noncommuting conditional reference flip changes the output population;
- a commuting conditional phase preserves it;
- one local-rate row has rank one and null direction \((1,-1)\);
- two factorization twins have the same complete exponential visibility;
- two uncalibrated references retain the common-mode null
  \((-1,1,1)\); and
- an independent reference-calibration row restores full rank.

Passing establishes none of the unearned claims in Section 5.2.
