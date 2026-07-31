---
title: "Finite-time trapped detector: process-dilation nonidentification and interface-expansion necessity"
status: explored
doc_type: governed_research_swing
created: 2026-07-31
claim_id: HC-DU-196
claim_status_change: none
disposition: FINITE_CHANNEL_DERIVED_DETECTOR_ONLY_DILATION_ATTRIBUTION_CLOSED_INTERFACE_EXPANSION_REQUIRED
---

# Finite-time trapped-detector process boundary

## Result

The finite-time continuation of the harmonic-trap detector closes cleanly in
its smallest resonant sector. Under the rotating-wave approximation, the
source interaction

\[
(a^\dagger-a)\otimes(\chi^{\dagger2}-\chi^2)
\]

couples only

\[
|2\rangle_D|0\rangle_M
\longleftrightarrow
|0\rangle_D|1\rangle_M
\]

at $\omega\simeq2\omega_0$. The exact two-state evolution gives a bounded
finite transition probability, a completely positive trace-preserving
amplitude-damping channel on the detector, and a complementary channel on the
mediator. No squared Dirac distribution is needed.

This earns two positive results and one hard stop:

1. **Finite channel:** the trapped proposal can be turned into an exact finite
   detector process in the resonant block.
2. **Hidden-resource reconstruction:** complete detector tomography can infer
   a minimum dilation or memory dimension and can detect single-mode revival,
   excluding random-unitary and irreversible Markov-semigroup rivals.
3. **Dilation nonidentification:** detector-only data—including two gaps,
   coherence-sensitive inputs, and arbitrary multi-time detector
   interventions—cannot select the physical identity of two implementations
   with the same detector process tensor. A single no-refit non-gravitational
   quantum-ancilla family reproduces the whole finite detector surface.

The strongest exact statement is therefore:

> A complete operational process reconstructs implementation-invariant
> resource requirements, not the physical identity of its dilation. Any
> property that varies inside the realization fibre requires an independently
> selected interface that does not factor through the original detector
> process.

That expanded interface need not literally measure a graviton. It may be a
mediator-facing instrument, an independently typed remote receiver, or a
source-to-receiver provenance channel. But merely adding more detector
tomography cannot do the job.

This is a scoped Grade-4 factorization and necessity result. The mathematics is
standard Stinespring/process-tensor structure instantiated on the gravitational
source; DU's contribution is the typed attribution boundary. No Grade-5
prediction or active successor is earned.

## Cold-start contract

- **Purpose / North Star:** determine what physical antecedents and interfaces
  make observer-accessible records sufficient for reconstructing a physical
  source rather than only its reduced response.
- **Current state:** the scientific portfolio remains quiescent. `HC-DU-195`
  supplied the exact finite-time reopener. This swing does not change
  `CURRENT-RESEARCH.yaml`.
- **Bounded question:** does the finite trapped-detector process contain any
  detector-only statistic that selects gravitational field mediation over a
  frozen direct quantum dilation?
- **Perspective / status:** the detector and candidate mediator are ontic
  systems within each realization; detector outcomes are epistemic evidence;
  dilation identity remains a physical question not fixed by that evidence.
- **Lanes / channels:** Lane 1 with Lanes 2, 3, 4, 6, and 7 support;
  `CH-FORMAL`, `CH-MODEL`, `CH-COLLIDE`, and `CH-EMPIRICAL`.
- **Maximum grade:** scoped Grade 4. Grade 5 needs one source-pinned expanded
  interface whose finite record separates the complete admitted realization
  class without refitting.
- **Strongest absorber:** Stinespring dilation, complementary-channel theory,
  quantum combs, process tensors, and open-system identification.
- **Cheapest kill:** one non-gravitational memory system with the same complete
  detector process across all frozen controls.
- **Hardware:** unavailable and unnecessary. The finite block and factorization
  theorem decide the research routing locally.

## Local Model Learning Gate

| Field | Frozen answer |
|---|---|
| Question | Does a finite detector channel or two-gap process identify its physical mediator? |
| Research-only baseline | Stinespring and process tensors say channels/processes have memory realizations, but the exact trapped-detector channel and its retained invariants had not been reconstructed in DU. |
| Local learning delta | Locate which finite observables exclude narrow rivals, which resource facts survive realization changes, and whether the direct rival closes detector-only attribution. |
| Generated, not encoded | The transition, revival, Kraus rank, complementary information flow, and two-gap equality are computed from the frozen two-state Hamiltonian block. |
| Pre-hardware checkpoint | Exact finite channel plus one explicit no-refit realization collision. |
| Decision changed | If a detector-only statistic survives, continue detector design; if none survives, stop adding detector tomography and require interface expansion. |
| Minimal build | One two-state exchange block, detector/complementary channels, two gaps, and a spanning input set. |
| Stop / hardware boundary | Stop after exact process equality or separation. Hardware is ineligible until an expanded physical interface has a locally discriminating contract. |

**Admission:** `ADMIT_LOCAL_LEARNING_BUILD`. The output changes the next
research object before any external hardware.

## Exact finite resonant block

### Conditional reduction

In the subspace

\[
\mathcal H_{\rm ex}=\operatorname{span}
\{|2,0\rangle,|0,1\rangle\},
\]

write the rotating-frame Hamiltonian as

\[
H_{\rm ex}=
\begin{pmatrix}
\Delta/2 & g\\
g & -\Delta/2
\end{pmatrix},
\qquad
\Omega=\sqrt{g^2+\Delta^2/4}.
\]

Then

\[
U(T)=\cos(\Omega T)I
-i\frac{\sin(\Omega T)}{\Omega}H_{\rm ex}.
\]

Starting in $|2,0\rangle$, the exchange probability is

\[
\gamma(T,\Delta)
=\frac{g^2}{\Omega^2}\sin^2(\Omega T),
\qquad 0\le\gamma\le1.
\]

For weak coupling at fixed nonzero detuning,

\[
\gamma(T,\Delta)
=\frac{4g^2}{\Delta^2}
\sin^2\!\left(\frac{\Delta T}{2}\right)+O(g^4),
\]

which is precisely the finite sinc-squared window required by `HC-DU-195`.

This block is exact only after the rotating-wave and two-state restriction. The
full Hamiltonian retains counter-rotating sectors; a continuum field adds mode
density and may suppress recurrence. Those extensions change the numerical
channel, not the general dilation nonidentification theorem below.

### Detector channel

Let

\[
s=\cos(\Omega T)
-i\frac{\Delta}{2\Omega}\sin(\Omega T),
\qquad
e=-i\frac g\Omega\sin(\Omega T),
\]

so $|s|^2+|e|^2=1$ and $\gamma=|e|^2$. The isometry is

\[
V|0\rangle_D=|0,0\rangle_{DM},
\qquad
V|2\rangle_D=s|2,0\rangle+e|0,1\rangle.
\]

Tracing out $M$ gives

\[
K_0=|0\rangle\!\langle0|+s|2\rangle\!\langle2|,
\qquad
K_1=e|0\rangle\!\langle2|.
\]

This is a normalized finite amplitude-damping channel. For $0<\gamma<1$ its
two Kraus operators are linearly independent, so its Choi/Kraus rank is two.
Under a pure-environment unitary realization, detector tomography therefore
forces at least a two-dimensional environment. It does not say what that
environment physically is.

### Complementary channel and record migration

For detector input

\[
\rho=\begin{pmatrix}
\rho_{00}&\rho_{02}\\
\rho_{20}&\rho_{22}
\end{pmatrix},
\]

the mediator output is

\[
\widetilde{\mathcal A}(\rho)=
\begin{pmatrix}
\rho_{00}+|s|^2\rho_{22} & e^*\rho_{02}\\
e\rho_{20} & |e|^2\rho_{22}
\end{pmatrix}.
\]

At resonant full swap, $s=0$ and $|e|=1$. The detector is reset to
$|0\rangle$ for every input, while the complementary output contains the
complete input state up to a known phase. Apparent detector irreversibility is
therefore record migration in the global unitary model, not information
destruction.

This is relevant to DU's North Star: the detector record can reveal that hidden
memory is required while remaining insufficient to identify the system that
holds it.

## The process-dilation nonidentification theorem

### One-time form

Let $\Phi$ be the complete detector channel. If two physical candidates have
isometries $V_1$ and $V_2$ satisfying

\[
\operatorname{Tr}_{E_1}(V_1\rho V_1^\dagger)
=\operatorname{Tr}_{E_2}(V_2\rho V_2^\dagger)
=\Phi(\rho)
\]

for every detector input $\rho$, no detector-only preparation or measurement
distinguishes them. Minimal Stinespring dilations are unique only up to an
environment isometry. Applying $I_D\otimes W_E$ can change every named
mediator-basis record while leaving $\Phi$ unchanged.

The underlying structure is standard. Stinespring gives unitary dilations of
quantum channels; Kretschmann, Schlingemann, and Werner discuss their
representation and continuity:
[arXiv:quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009).

### Multi-time form

Let $\Upsilon_{k:0}$ be the complete detector process tensor. Every probability
for a sequence of detector instruments $\mathbf A_{k-1:0}$ is a contraction

\[
p(\mathbf x)=
\operatorname{Tr}
\left[\Upsilon_{k:0}\mathbf A_{k-1:0}^{T}\right].
\]

If two realizations induce the same $\Upsilon_{k:0}$, every detector-only
multi-time experiment agrees. Pollock et al. establish the operationally
complete multi-time framework:
[arXiv:1512.00589](https://arxiv.org/abs/1512.00589). Quantum-comb realization
theorems show that admissible networks have memory-channel implementations:
[arXiv:0904.4483](https://arxiv.org/abs/0904.4483).

Therefore two gaps, coherence tomography, causal breaks, and intermediate
detector interventions help reconstruct $\Upsilon$ and its memory/resource
invariants. They cannot select a physical property not constant on the
realization fibre of $\Upsilon$.

### DU factorization form

Let $\mathfrak R(\Upsilon)$ be the admitted physical realizations of one
detector process and let $m:\mathfrak R(\Upsilon)\to\mathcal M$ name a mediator
property. Detector-only reconstruction of $m$ exists exactly when

\[
m(R_1)=m(R_2)
\quad\text{for all }R_1,R_2\in\mathfrak R(\Upsilon).
\]

An explicit gravitational-mode realization and an isomorphic
non-gravitational quantum ancilla have the same detector process but different
mediator labels. Physical mediator identity is therefore not constant on that
fibre.

This is not a claim that any carefully constrained direct-action theory can
match any gravitational experiment. It says an unrestricted implementation
label cannot be reconstructed from the marginal process it was defined to
leave unchanged.

## What detector-only work still learns

The stop is on attribution, not on all useful inference.

### Rival classes excluded

- Nonunitality excludes classical random-Hamiltonian mixtures.
- Ordered upward/downward asymmetry excludes real stationary commuting-force
  models in the frozen class.
- Single-mode transfer followed by revival excludes a time-homogeneous
  irreversible amplitude-damping semigroup.
- Multi-time instruments can detect memory and lower-bound a minimal memory
  resource.

### Properties not selected

- whether the memory is a gravitational mode, another field, an engineered
  ancilla, or a direct nonlocal kernel;
- a preferred basis or ontology for the environment;
- source provenance; and
- the physical location, propagation law, or universal coupling of the hidden
  memory.

At two independently fixed gaps, one direct-ancilla family with the same
predeclared coupling law reproduces the complete detector channels without
after-result fitting. Two gaps defeat narrower classical-equilibrium models;
they do not defeat dilation equivalence.

## The required interface expansion

To distinguish two realizations that share the original detector process, the
experiment must expose a port outside that marginal. Formally, seek extended
processes $\widetilde\Upsilon_1$ and $\widetilde\Upsilon_2$ such that

\[
\operatorname{Tr}_{B}\widetilde\Upsilon_1
=\operatorname{Tr}_{B}\widetilde\Upsilon_2
=\Upsilon_D,
\qquad
\widetilde\Upsilon_1\ne\widetilde\Upsilon_2,
\]

and a physically selected instrument on the new port $B$ that separates them.

Candidate ports include:

1. an independently calibrated receiver for the emitted excitation;
2. a second spatially separated detector with a frozen propagation and
   polarization response;
3. a source-deletion/source-substitution surface that tests the same coupling
   law without refit; or
4. a mediator-facing observable selected by the source theory rather than by
   the desired conclusion.

Interface expansion is necessary within the realization-equivalent class; it
is not sufficient for gravitational attribution. The expanded record must
also carry material lineage, exclude ordinary cross-talk and direct
source--receiver action, and survive finite error.

## Exact local fixture

`tests/du_finite_time_trapped_detector_dilation_probe.py` verifies twelve
controls:

1. exact unitarity of the finite exchange block;
2. bounded finite transition probability;
3. recovery of the weak-coupling sinc-squared window;
4. trace preservation of the detector channel;
5. retained nonunitality;
6. complete detector-channel equality for a direct ancilla;
7. minimal pure-environment dimension two from Kraus rank;
8. one no-refit direct family matching two gaps;
9. complementary mediator information gain;
10. complete record migration at full swap;
11. environment-isometry freedom at fixed detector channel; and
12. single-mode revival excluding only a memoryless semigroup.

All twelve pass.

## Updated reopener

Do not add more detector-only controls merely to identify the mediator. Reopen
with the smallest independently selected expanded port and a frozen rival
table:

```text
trapped source/detector
  -> finite detector process
  -> independently typed receiver or mediator port
  -> joined attempt-level record
  -> gravitational-field / direct-action / cross-talk tournament
```

The highest-information next swing is a primary-source tournament for the
smallest physically realizable expanded port. It should compare a remote
receiver, emitted-radiation channel, and spatial two-detector correlation
against direct quantum action and ordinary material coupling before any local
build. If no source supplies the port and lineage, bank an interface-selection
obstruction and stop this arena. If one does, derive its finite extended
process locally before considering hardware.

## Disposition

**`FINITE_CHANNEL_DERIVED_DETECTOR_ONLY_DILATION_ATTRIBUTION_CLOSED_INTERFACE_EXPANSION_REQUIRED`**

Keep the portfolio quiescent. The finite detector process is now understood;
the live uncertainty has moved to physical interface expansion and provenance.
No observed effect, new law, hardware action, successor, or later-wave
activation is earned.
