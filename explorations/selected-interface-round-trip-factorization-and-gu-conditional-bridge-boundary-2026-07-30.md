---
title: "Selected-interface round-trip factorization and GU conditional bridge boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-181
run_id: RUN-20260731-022601-selected-interface-round-trip-gate
work_id: SELECTED-INTERFACE-ROUND-TRIP-GATE
action_id: SELECTED-INTERFACE-ROUND-TRIP-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_1
supporting_lanes:
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-SYN
  - CH-MODEL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# Selected-interface round-trip factorization and GU conditional bridge boundary

## Executive return

```text
SELECTION-OR-DESCENT-ROUND-TRIP-BOUNDARY
+ CROSS-INTERFACE-AMBIGUITY-OBSTRUCTION
+ SELECTED-INTERFACE-FACTORIZATION-THEOREM
+ PHYSICAL-SELECTION-DOES-NOT-IMPLY-IDENTIFIABILITY
+ LAW-IDENTIFIABILITY-DOES-NOT-IMPLY-EVENT-CERTIFICATION
+ RETAINED-INTERFACE-TAG-IS-RECORD-ENLARGEMENT
+ GAUGE-DESCENT-REQUIRED
+ GU-FLAG-SELECTION-AND-CROSS-FLAG-DESCENT-BOTH-UNBUILT
+ DU-COMPLETE-MATERIAL-INSTRUMENT-UNBUILT
+ CONDITIONAL-GU-TO-DU-CLOSED-LOOP-ARCHITECTURE
+ STANDARD-STATISTICAL-EXPERIMENT-ABSORPTION
+ NO-PHYSICAL-GU-DU-ROUND-TRIP-YET
+ NO-READY-SUCCESSOR
```

The proposed closed loop

```text
GU physical geometry
-> physical instrument
-> formed records
-> DU reconstruction
-> recovered GU geometry
```

is coherent, but it contains several logically independent gates. The
central result of this swing is:

> An exact record-only round trip requires either a target-blind physical
> selection of the operative interface followed by target factorization
> through its record law, or a proof that the target already descends across
> the entire unselected interface family. Conditional decoders that work
> only after the interface is named do not suffice.

This corrects an overstatement in the motivating synthesis. A dynamically
selected complex--Cartan flag would be a strong bridge, but it is not
logically necessary for every observer-accessible target. If the complete
physical instrument and reconstruction are independent of which admissible
flag is used, the flag is a nuisance or gauge direction for that target.
That cross-flag descent must be proved; it cannot be inferred from covariance
or from the existence of several compatible flags.

The present repositories close neither route. GU RB5 proves that its current
coarse Clifford-plane field does not own the full flag and that its exact
spectral \(H,Q\) constructions are planted controls rather than source-owned
selectors. It has not shown that the prospective low-energy group,
polarization, majorant, apparatus response, or observer-accessible geometry
is invariant across the remaining flag family. Dynamic Unity has physically
formed detector-event, persistent spatial, and oriented-response positives,
but no one source selects their complete material instrument, archive,
provenance, access, and target-sufficient response packet.

The component mathematics is absorbed by factorization, sufficient
statistics, identifiability, comparison of statistical experiments, and
data processing. The value for Dynamic Unity is the typed admission boundary
and the exact allocation of the GU and DU obligations—not a new mathematical
theorem or new physics.

## 1. Frozen objects

First quotient every transformation already declared gauge. Let

\[
\overline M=M/G
\]

be the admitted physical completion class. Let

\[
T:\overline M\longrightarrow Y
\]

be one observer-accessible physical target fixed before the record
construction.

Let \(I\) be an admitted family of interfaces. After all required typed
adapters have been supplied, each interface \(i\in I\) gives a record law

\[
K_i:\overline M\longrightarrow\Delta(R)
\]

on one declared record alphabet \(R\). Equality of record laws means exact
equality as probability measures, not equality of one observed sample or one
summary statistic.

The formulation already imposes four nontrivial duties:

1. the target and record laws must descend through the physical gauge
   quotient;
2. the interfaces must have a common typed record codomain, or explicit
   target-independent adapters into one;
3. the target must be fixed independently of the record equivalence; and
4. access to a record law must not be confused with access to one realized
   record.

If any duty fails, the round trip is not yet a function on the declared
physical objects.

## 2. Fixed-interface factorization

### Theorem 1 — law-level decoder criterion

For one fixed interface \(i\), an exact decoder

\[
D_i:K_i(\overline M)\longrightarrow Y
\]

satisfying

\[
D_i\circ K_i=T
\tag{1}
\]

exists iff

\[
\ker K_i\subseteq\ker T.
\tag{2}
\]

When it exists, \(D_i\) is unique on \(K_i(\overline M)\).

### Proof

If (1) holds, equal record laws have equal decoded targets, proving (2).
Conversely, define

\[
D_i(K_i(m))=T(m).
\]

Condition (2) makes the definition independent of the representative.
Every element of \(K_i(\overline M)\) has a representative, and uniqueness
on the image is immediate. \(\square\)

This is ordinary factorization mathematics. It says nothing about why
interface \(i\) was physically used, whether its record was formed or
retained, or whether an observer can estimate the complete law.

## 3. Cross-interface ambiguity

Define

\[
F:I\times\overline M\longrightarrow\Delta(R),
\qquad
F(i,m)=K_i(m),
\]

and lift the target by

\[
\widetilde T(i,m)=T(m).
\]

### Theorem 2 — untagged family decoder criterion

One decoder

\[
D:F(I\times\overline M)\longrightarrow Y
\]

works without receiving an interface label iff

\[
\ker F\subseteq\ker\widetilde T.
\tag{3}
\]

Equivalently,

\[
K_i(m)=K_j(m')
\quad\Longrightarrow\quad
T(m)=T(m')
\tag{4}
\]

for every \(i,j,m,m'\).

The proof is Theorem 1 applied to \(F\) and \(\widetilde T\).

### Smallest counterexample

Take:

\[
\overline M=\{0,1\},
\qquad
T(m)=m,
\qquad
I=\{\mathrm{direct},\mathrm{flip}\}.
\]

Let

\[
K_{\mathrm{direct}}(m)=\delta_m,
\qquad
K_{\mathrm{flip}}(m)=\delta_{1-m}.
\]

Each named interface is perfectly invertible. Nevertheless,

\[
K_{\mathrm{direct}}(0)
=
K_{\mathrm{flip}}(1)
=
\delta_0
\]

while \(T(0)\ne T(1)\). No record-only decoder can know whether the same law
means target zero under the direct interface or target one under the flipped
interface.

Enlarging the packet to

\[
\big(i,K_i(m)\big)
\]

repairs the finite example. The repair is not free: it retains interface
identity as an additional provenance coordinate. A physical theory must form
and preserve that coordinate or independently select the interface.

## 4. Selection or descent

Suppose the physical dynamics supplies a target-blind selector

\[
s:\overline M\longrightarrow I.
\]

The selected record-law map is

\[
K_s(m)=K_{s(m)}(m).
\]

Theorem 1 then gives:

\[
\exists D_s,\quad D_sK_s=T
\quad\Longleftrightarrow\quad
\ker K_s\subseteq\ker T.
\tag{5}
\]

Physical selection and target reconstruction remain independent:

- a selected constant record law fails (5);
- an informative selected law may pass (5);
- an unselected family may already pass the stronger cross-interface
  condition (4); and
- individually invertible interfaces may fail (4).

This yields two honest routes:

### Route A — selection

Physics selects \(s\) without using \(T\), and the selected law satisfies
(5).

### Route B — descent

No unique \(s\) is required for the declared target because the complete
family satisfies (4). Interface variation is operationally irrelevant to
that target.

The routes may both hold. If neither holds, the round trip is interface
relative rather than physical at the declared record-only level.

Calling every unselected interface direction “gauge” would be premature.
Gauge status is earned only after the target, dynamics, record laws,
interventions, and capabilities descend through the proposed quotient.

## 5. Law identification is not an event certificate

An exact law-level decoder receives the full probability law \(K_s(m)\).
One realized historical event supplies an outcome \(r\in R\).

### Theorem 3 — event-level zero-error criterion

A deterministic decoder

\[
d:R\longrightarrow Y
\]

satisfies

\[
K_s(m)\big(d^{-1}(T(m))\big)=1
\tag{6}
\]

for every \(m\) iff the supports associated with distinct target classes are
disjoint:

\[
T(m)\ne T(m')
\quad\Longrightarrow\quad
\operatorname{supp}K_s(m)
\cap
\operatorname{supp}K_s(m')
=\varnothing.
\tag{7}
\]

### Proof

If one outcome \(r\) lies in the support of two different target classes,
\(d(r)\) cannot equal both targets, so (6) fails. Conversely, if the target
support unions are disjoint, assign each supported outcome to its unique
target class; define \(d\) arbitrarily outside the union. \(\square\)

Distinct but overlapping laws can satisfy Theorem 1 while failing Theorem 3.
For the finite control

\[
K(0)=(4/5,1/5),
\qquad
K(1)=(1/5,4/5),
\]

the laws are different and therefore identify the target at the law level,
but their supports coincide. Equal-prior optimal one-shot error is

\[
P_{\rm err}^{\star}
=
\frac{1-\operatorname{TV}(K(0),K(1))}{2}
=
\frac15.
\]

Repeated preparation may estimate the law increasingly well. It does not
make one unrepeated historical event an exact certificate.

## 6. Downstream processing

Let \(C:R\rightsquigarrow R'\) be one common stochastic readout channel.
Then:

\[
K_s(m)=K_s(m')
\quad\Longrightarrow\quad
C_*K_s(m)=C_*K_s(m'),
\tag{8}
\]

and

\[
\operatorname{TV}\big(C_*K_s(m),C_*K_s(m')\big)
\le
\operatorname{TV}\big(K_s(m),K_s(m')\big).
\tag{9}
\]

Thus common downstream amplification, digitization, coarse-graining, or
decoding cannot repair equal upstream laws. It can expose, preserve, or lose
an already present distinction. Adding an interface tag, reference system,
or calibration source is a different operation because it enlarges the
packet.

## 7. Conditional GU application

The current GU source revision is
`gu-formalization@c144ab0`. Its RB5 result states:

- the explicit coarse soldering field is a local unframed
  Clifford-plane orbit;
- it cannot equivariantly determine the full
  \((P_W,J,t,\Omega_{\mathbb C})\) flag;
- conditional spectral formulas can recover \(P_W\) and \(J\) from
  admissible \(H,Q\);
- the tested \(H,Q\) deliberately encode the target; and
- no source-owned target-blind map to them, eligible stationary background,
  or physical gauge/BV Hessian has been constructed.

See
`../gu-formalization/explorations/rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md`.

Typed into the present theorem, the prospective flag is an interface or
interface-defining antecedent. GU currently has neither:

1. a source-owned selector \(s\) establishing Route A; nor
2. a theorem that all admissible flag choices give the same complete
   observer-accessible target through the instrument, establishing Route B.

This matters for the proposed phase-space lift. Low-energy symmetry,
quantization polarization, and a positive majorant are three separately
typed targets. If they vary across admissible flags, physical flag selection
is necessary for those targets. If the complete outputs descend across the
flag family, the unselected directions may be irrelevant or gauge at that
scope. The descent must be tested separately for each target.

Dynamic Unity does not infer that either route will work. GU remains a
conditional input and recovery target.

## 8. Dynamic Unity application

Dynamic Unity's detector ladder currently supplies partial interfaces:

- `HC-DU-178`: material event formation and retention in a bubble chamber;
- `HC-DU-179`: persistent material spatial provenance in nuclear emulsion;
  and
- `HC-DU-180`: physical but generally transient, bounded-error track
  orientation in gaseous TPC response.

No one source-pinned theory currently selects:

- a complete event/path association;
- exact or explicitly bounded orientation for the target event;
- event time and source provenance;
- a persistent archive;
- observer access and action semantics; and
- a target-sufficient full response law.

DU therefore stops before a complete \(K_s\) is available. The new round-trip
theorem cannot turn the partial platforms into one instrument by
concatenating their virtues.

## 9. Strongest absorber and surviving value

David Blackwell's comparison of statistical experiments already treats
experiments as probability-law families and compares their information
through stochastic transformations:
[Blackwell, “Equivalent Comparisons of Experiments”
(1953)](https://doi.org/10.1214/aoms/1177729032).
Sufficient-statistic factorization, identifiability, inverse problems,
Markov kernels, support separation, binary testing, and data processing
absorb every mathematical component used here.

The result is not novel mathematics. Its project-specific value is:

1. preventing a named GU flag from being silently supplied to the inverse
   map;
2. preserving the overlooked cross-flag descent alternative;
3. distinguishing exact access to a law from one-event certification;
4. locating GU and DU at different upstream gates; and
5. specifying the exact conjunction a future physical closed loop must earn.

## 10. Disposition

The integrated picture remains a coherent conditional architecture:

```text
source-owned action and stationary physical class
-> selected flag OR target descent across the flag family
-> selected physical instrument and retained record packet
-> law-level target factorization
-> event-level certificate or declared finite error
-> observer access and action
-> no-refit GU-to-DU reconstruction.
```

It is not yet a theory of nature or an executable successor.

The highest-information future joint test is not to assume the flag and
decode through it. It is to compare:

```text
target-blind action-selected flag
versus
cross-flag target descent.
```

That comparison belongs upstream in GU. Dynamic Unity's independent
highest-information need remains a physical source that joins retained
material provenance, polarity, event association, archive/access selection,
and a target-sufficient response law.

Wave 3 remains ineligible. No new physics, remainder, prediction, paper, or
successor is promoted.

