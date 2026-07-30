---
title: "Hybrid quantum measurement: finite-time capacity and thermodynamic nonimplication"
status: banked_scoped_result
date: 2026-07-29
claim_id: HC-DU-141
run_id: RUN-20260729-213813-hybrid-measurement-capacity-positive-control
primary_lane: lane_4
supporting_lanes:
  - lane_3
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
---

# Hybrid quantum measurement: finite-time capacity and thermodynamic nonimplication

## Result in one paragraph

The finite-time hybrid measurement law supplies a genuine calculational
positive control once its apparatus packet is frozen. For a uniformly blank
binary pointer and measurement-eigenstate inputs, its exact solution is a
binary symmetric channel with crossover
\(q(t)=e^{-\gamma t}/2\), capacity
\(C(t)=1-h_2(q(t))\), and readout-success odds
\(O_{\rm read}(t)=2e^{\gamma t}-1\). Hence
\(C=1-h_2(1/(1+O_{\rm read}))\) in this packet. That does **not** make
Norton's \(\Delta S=k_{\rm B}\log O\) follow. The hybrid process has a
one-way pointer relaxation: its finite error is the probability that the
pointer has not yet relaxed, not the probability that a thermal fluctuation
reverted a completed state. A reversible two-rate repair separates
thermodynamic bias \(O_{\rm th}=\alpha/\beta\) from kinetic depth
\((\alpha+\beta)t\); finite-time capacity depends on both. Standard
stochastic thermodynamics does contain the missing port-shaped structure—a
probability current paired with a log-ratio affinity—but neither cited
construction selects the adapter identifying that pair with the quantum port
and Norton odds. The paper also models only the ex-ante distribution, not one
actual ex-post record. The result therefore validates the typed ladder as a
calculation, while leaving physical record formation and thermodynamic
realization open.

## 1. What the correction gets right

“Probability, not energy” is too coarse. The quantities are not alternatives.
For a thermodynamic process satisfying Norton's Boltzmann conditions,

\[
O_{\rm th}=\frac{W_2}{W_1}
=\exp\!\left(\frac{\Delta S}{k_{\rm B}}\right),
\qquad
\Delta S=k_{\rm B}\log O_{\rm th}.
\]

Thus dimensionless dynamic odds and thermodynamic entropy are invertible
coordinates on the same **thermodynamically realized bias**. If a temperature
is also fixed, \(T\Delta S\) has energy units. This is a cleaner statement
than making energy or information primary.

But three guards remain load-bearing:

1. the relation applies to the dynamic probabilities of the declared
   thermodynamic completion/reversion process, not every quantity called a
   probability;
2. a logarithm changes multiplicative odds into additive entropy—it is not a
   unit conversion or a linear identity; and
3. Born-probability flow, readout error, and thermodynamic forward/reverse
   odds require an explicit physical adapter before they can be identified.

Norton's current analysis emphasizes exactly the first guard by separating
dynamic thermal occupation probabilities from static uncertainty over memory
values:
[Norton, “Too Good to Be True”](https://doi.org/10.1017/psa.2026.10221).

## 2. The frozen hybrid packet

Krhač, Schuller, and Stramigioli define an exactly solvable finite-dimensional
quantum--classical hybrid implementation of projective measurement:
[“Hybrid Schrödinger-Liouville and projective dynamics”](https://arxiv.org/abs/2504.05532).

For a supplied measurement

\[
M=\sum_zm_zP_z
\]

and classical pointer space \(Z\), the implementation

\[
\dot\rho(z,t)
=
\gamma\!\left(P_z\hat\rho(t)P_z-\rho(z,t)\right)
\]

has the exact solution

\[
\rho(z,t)
=
e^{-\gamma t}\rho(z,0)
+
(1-e^{-\gamma t})P_z\hat\rho(0)P_z
\]

and induced pointer probabilities

\[
p(z,t)
=
e^{-\gamma t}p(z,0)
+
(1-e^{-\gamma t})
\operatorname{tr}\!\left(P_z\hat\rho(0)\right).
\]

The present positive control freezes:

- binary source \(X\in\{0,1\}\), uniform;
- eigenstate encoding \(\hat\rho_x=P_x\);
- binary pointer \(Y\in\{0,1\}\);
- blank pointer law \(p(y,0)=1/2\);
- supplied \(M\), \(P_x\), \(\gamma>0\), and read time \(t\); and
- success \(Y=X\).

These choices are intentionally strong. The question is whether the ladder
can carry an exact calculation once the missing interfaces are supplied, not
whether the dynamics selected those interfaces.

## 3. Exact finite-time channel and capacity

Let

\[
a=e^{-\gamma t}.
\]

For source value \(x\),

\[
\Pr(Y=x\mid X=x)
=
\frac a2+(1-a)
=
1-\frac a2
\]

and

\[
\Pr(Y\ne x\mid X=x)
=
\frac a2.
\]

The induced classical channel is therefore a binary symmetric channel with
crossover

\[
q(t)=\frac12e^{-\gamma t}.
\]

Its Shannon capacity in bits is

\[
C(t)
=
1-h_2\!\left(\frac12e^{-\gamma t}\right),
\]

where

\[
h_2(q)=-q\log_2q-(1-q)\log_2(1-q).
\]

The uniform source attains the capacity. It also saturates the corresponding
binary Fano relation:

\[
H(X\mid Y)=h_2(q),
\qquad
I(X;Y)=1-h_2(q).
\]

This is an exact conditional Grade-3 reconstruction result inside the frozen
packet: the pointer reconstructs the binary source label with error \(q(t)\).
It is also a positive control for `HC-DU-136`: after the physical packet has
been supplied, its conditional law yields a concrete accessible capacity and
resolution bound without fitting.

### Boundary checks

\[
t=0:
\quad
q=\frac12,\quad C=0;
\]

\[
t\to\infty:
\quad
q\to0,\quad C\to1.
\]

No numerical model is needed.

## 4. The exact packet-relative odds relation

The readout-success odds are

\[
O_{\rm read}(t)
=
\frac{1-q(t)}{q(t)}
=
2e^{\gamma t}-1.
\]

Therefore

\[
q=\frac1{1+O_{\rm read}}
\]

and

\[
C(O_{\rm read})
=
1-h_2\!\left(\frac1{1+O_{\rm read}}\right).
\]

This is a legitimate relation because the source, apparatus, pointer, read
time, success event, and access map are all frozen. It refutes the stronger
claim that probability variables can never be composed.

It does **not** reverse `HC-DU-140`. The relation is packet-relative. Changing
the alphabet, encoding, pointer initialization, measurement, readout, or
success semantics changes it.

## 5. Why the Norton inference fails in the original packet

For an eigenstate input, the pointer equation is

\[
\dot p_{\rm correct}
=
\gamma(1-p_{\rm correct}),
\qquad
\dot p_{\rm wrong}
=
-\gamma p_{\rm wrong}.
\]

This is a one-way continuous-time relaxation:

\[
\text{wrong}
\xrightarrow{\ \gamma\ }
\text{correct},
\qquad
\text{correct}
\not\longrightarrow
\text{wrong}.
\]

At finite time, \(q(t)\) is the probability that the initially blank pointer
has not yet reached the correct state. It is not the probability that a
fluctuation took a completed pointer back to the wrong state.

This gives an exact contradiction to the naive identification:

- the finite readout odds are
  \(O_{\rm read}(t)=2e^{\gamma t}-1<\infty\);
- the forward/reverse **rate** odds of the one-way generator are
  \(\gamma/0=\infty\); and
- a finite Norton entropy cannot simultaneously be the logarithm of both.

The hybrid equation also contains no temperature, heat, work, bath,
free-energy landscape, local detailed balance, or thermodynamic
entropy-production functional. It therefore cannot derive
\(\Delta S=k_{\rm B}\log O_{\rm read}\).

One may impose

\[
\Delta S
=
k_{\rm B}\log(2e^{\gamma t}-1)
\]

as an additional thermodynamic realization. That is a conditional adapter,
not a consequence of the hybrid dynamics.

## 6. The reversible repair exposes two independent coordinates

The smallest thermodynamically interpretable repair gives the pointer both a
forward rate \(\alpha>0\) and a reverse rate \(\beta>0\):

\[
\text{wrong}
\mathop{\rightleftarrows}^{\alpha}_{\beta}
\text{correct}.
\]

Define

\[
r=\alpha+\beta,
\qquad
O_{\rm th}=\frac{\alpha}{\beta}\ge1.
\]

Starting from the same uniform blank pointer,

\[
q(t)
=
\frac1{1+O_{\rm th}}
+
\left(
\frac12-\frac1{1+O_{\rm th}}
\right)e^{-rt}.
\]

The finite-time capacity is therefore

\[
C(t;O_{\rm th},r)
=
1-h_2\!\left[
\frac1{1+O_{\rm th}}
+
\left(
\frac12-\frac1{1+O_{\rm th}}
\right)e^{-rt}
\right].
\]

This is the most useful positive result of the swing:

> thermodynamic reliability bias and kinetic/protocol depth are separate
> coordinates.

If local detailed balance identifies

\[
\Delta S=k_{\rm B}\log O_{\rm th},
\]

then

\[
q(t)
=
\frac1{1+e^{\Delta S/k_{\rm B}}}
+
\left(
\frac12-\frac1{1+e^{\Delta S/k_{\rm B}}}
\right)e^{-rt}.
\]

At zero bias,

\[
O_{\rm th}=1
\quad\Longrightarrow\quad
q(t)=\frac12,\quad C(t)=0
\]

for every time: the pointer diffuses both ways and fixes no source
distinction.

At infinite time,

\[
C_\infty(\Delta S)
=
1-h_2\!\left(
\frac1{1+e^{\Delta S/k_{\rm B}}}
\right).
\]

At finite time, the entropy bias does not determine capacity without the
kinetic depth \(rt\). Conversely, the original hybrid model is the singular
\(O_{\rm th}\to\infty\) limit:

\[
q(t)\to\frac12e^{-rt}.
\]

It gets perfect asymptotic reliability by eliminating reversion entirely,
not by deriving a finite thermodynamic cost.

This two-rate specimen explains why a depth-and-reliability contract has the
right shape. It does not establish a universal law for arbitrary protocols.

## 7. Does the logarithmic odds have port structure?

There is a standard, exact host for that idea in stochastic thermodynamics.
For a reversible Markov edge with probabilities \(p_i,p_j\) and rates
\(k_{ij},k_{ji}\), define the probability current

\[
J_{ij}
=
p_i k_{ij}-p_j k_{ji}
\]

and log-ratio force

\[
A_{ij}
=
\log\frac{p_i k_{ij}}{p_j k_{ji}}.
\]

Their product contributes to entropy production:

\[
\frac{\dot S_{\rm prod}}{k_{\rm B}}
=
\sum_{i<j}J_{ij}A_{ij}
\ge0.
\]

In network form this becomes the familiar current--affinity pairing of
stochastic thermodynamics. A current multiplied by a log-odds-like conjugate
force is therefore not an unknown mathematical structure. See, for example,
the review and extension in
[Raghu and Neri, “Effective Affinity for Generic Currents in Markov Processes”](https://doi.org/10.1007/s10955-025-03433-w).

But this does not weld the two motivating theories:

- Krhač's quantum port is Hilbert-space-valued and its scalar pairing tracks
  Born-probability redistribution under unitary coupling;
- Norton's \(\log O\) is a finite thermodynamic bias for a declared
  completion/reversion process;
- the Markov current--affinity product requires reversible transition rates,
  path or state probabilities, and thermodynamic consistency; and
- the exact hybrid implementation is unidirectional and supplies no such
  thermodynamic typing.

The honest conclusion is:

> a port-shaped composition is available in mature stochastic
> thermodynamics, but an independently derived adapter from the quantum port
> to that Markov current--affinity pair is still missing.

So the abstract structure is known; its physical identification in this DU
chain remains open.

## 8. The actual-record boundary remains

The hybrid paper explicitly restricts itself to the ex-ante part of
measurement. Its state contains:

- the mixed quantum state;
- the classical pointer probability distribution; and
- the conditional collapsed states associated with possible pointer values.

It does not model the ex-post selection of the actually observed value.
Consequently the positive control still does not select:

- one actual pointer write;
- retention or blank-to-written formation;
- source provenance;
- observer access;
- rival-excluding certification;
- public finality; or
- an action-enabling archive.

Sampling \(Y\) from the derived distribution creates a stochastic outcome in
an enlarged model. It does not prove that the published hybrid dynamics
physically selected that ex-post mechanism.

## 9. Typed theorem and status

### HC-DU-141 — finite-time hybrid capacity and thermodynamic nonimplication

For the frozen binary eigenstate/uniform-pointer packet:

\[
q(t)=\frac12e^{-\gamma t},
\qquad
C(t)=1-h_2(q(t)),
\qquad
O_{\rm read}(t)=\frac{1-q(t)}{q(t)}.
\]

Thus a finite-time hybrid measurement law can conditionally determine an
observer-accessible channel capacity after the complete interface packet is
supplied.

It does not determine a Norton thermodynamic entropy. In the original
one-way dynamics, readout failure is incomplete relaxation rather than
thermal reversion. In the smallest reversible two-rate repair, finite-time
capacity depends independently on thermodynamic bias \(O_{\rm th}\) and
kinetic depth \(rt\). Norton's logarithmic relation enters only after local
detailed balance or another thermodynamic realization is supplied.

### Grade

- **Scoped Grade 4:** exact channel derivation, exact one-way/reversion
  nonidentity, and exact two-coordinate thermodynamic repair.
- **Conditional Grade 3:** binary source reconstruction and capacity after
  the apparatus, source, pointer, read time, and access map are supplied.
- **Not earned:** a selected apparatus, actual record, thermodynamic cost law,
  universal port law, empirical excess, prediction, new physics, or Grade 5
  remainder.

### Strongest absorbers

- binary symmetric channel capacity and Fano equality;
- finite-duration hybrid/open-system measurement;
- continuous-time Markov relaxation;
- local detailed balance and stochastic thermodynamics; and
- Schnakenberg current--affinity structure.

### Cheapest kill

The exact hybrid generator has a zero reverse rate and no thermodynamic
parameters. Its finite pointer error cannot be the reversion probability in
a finite Norton odds ratio.

### Reopener

Require one physical model to select, without refit:

1. the quantum subsystem decomposition and measurement coupling;
2. reversible pointer dynamics or another explicit completion/reversion
   process;
3. the thermodynamic bath, state space, and local-detailed-balance map;
4. one actual retained outcome with provenance and observer access; and
5. the source, decoder, task, resources, and held-out target.

Only then ask whether its quantum probability current, thermodynamic affinity,
formed record, and accessible capacity obey a mechanism-specific law.

## 10. Portfolio disposition

The typed ladder has crossed an important threshold: it can now carry an exact
finite-time calculation. The calculation also shows precisely why the current
candidate does not satisfy the physical-interface reopener.

The branch therefore remains parked:

```text
EXACT_HYBRID_BINARY_CHANNEL
+ EXACT_FINITE_TIME_CAPACITY
+ PACKET_RELATIVE_READOUT_ODDS_RELATION
+ PROBABILITY_CURRENT_LOG_AFFINITY_HOST_IS_KNOWN
+ READOUT_FAILURE_IS_NOT_THERMAL_REVERSION
+ RELIABILITY_BIAS_AND_KINETIC_DEPTH_ARE_INDEPENDENT
+ EX_ANTE_DISTRIBUTION_IS_NOT_AN_ACTUAL_RECORD
+ NO_THERMODYNAMIC_COST_DERIVATION
+ NO_READY_SUCCESSOR
```

No simulation, hardware, provider, publication, or prediction is warranted.
