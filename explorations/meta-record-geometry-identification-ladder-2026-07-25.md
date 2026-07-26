---
title: "Meta-record geometry identification ladder"
status: completed_scoped_reconstruction_and_nonidentification_control
doc_type: exact_finite_theorem_boundary_and_next_physical_contract
created: 2026-07-25
run_id: RUN-20260725-215502-meta-record-geometry-identification
authority: "Joe direct chat: 'Do another swing' followed by 'Not papers'"
claim_grade: "EXACT FINITE KNOWN-MATHEMATICS CONTROL / SCALAR RECORD-TIME RECONSTRUCTION / NO PROPER TIME, METRIC, ONTOLOGY, OR NEW PHYSICS"
probe: "../tests/du_meta_record_geometry_identification_probe.py"
artifact: "../tests/artifacts/du_meta_record_geometry_identification_result.json"
---

# Meta-Record Geometry Identification Ladder

## Result in plain English

This swing answers the first part of `HC-DU-038` and sharply narrows the next
one.

A certified record network can tell us that one record can precede or reach
another and can retain who acquired what through which route. That is already
more than a list of terminal outcomes. But it does **not**, by itself, tell us:

- how much time passed;
- how elapsed time was divided between intermediate events;
- what spacetime dimension the events inhabit;
- what metric or physical scale applies;
- what a clock measures along a worldline; or
- whether different routes accumulated different proper times.

Adding calibrated duration differences to the immediate record-transfer edges
does recover one exact object:

> A single scalar record-time assignment exists exactly when the signed
> duration around every undirected loop is zero.

When it exists, the assignment is unique up to one arbitrary additive origin
per disconnected component. The number of independent consistency conditions
is exactly

\[
|E|-|V|+c,
\]

where \(c\) is the number of weakly connected components.

This result is useful, but its boundary matters more than its algebra:

> The recovered scalar is a route-independent clock potential. It is not
> automatically relativistic proper time, simultaneity, Lorentzian distance,
> dimension, curvature, or a spacetime metric.

Indeed, proper time is generally path-dependent. A nonzero loop discrepancy
could be clock calibration, transport, route, or provenance failure; it could
also be the wrong demand because the edge quantities are path durations rather
than differences of one global potential. Calling such a discrepancy
“curvature” would be an overclaim.

The next geometry swing is therefore not “extract a metric from a DAG.” It is:

> Add independently calibrated volume/density and path-indexed local-clock
> structure to the certified order, then determine which geometric candidates
> remain observationally equivalent on held-out comparisons.

The executable control passes `21/21`.

## Frozen object

Let

\[
\Gamma_R=(V,E,\preceq,\pi)
\]

be a finite authenticated meta-record object:

- \(V\) contains certified record events;
- \(E\) is the directed Hasse-cover relation for admitted operational
  precedence or record acquisition;
- \(\preceq\) is the transitive closure of \(E\); and
- \(\pi\) carries frozen identity and provenance labels.

None of the following is contained in this base object:

- duration or timestamp;
- event density or physical volume;
- a manifold;
- spacetime dimension;
- a Lorentzian metric;
- a foliation or inertial frame;
- proper time; or
- a sampling law that turns record count into volume.

This separation is noncircular. `Gamma_R` may represent a physically supplied
precedence relation, but it may not silently import the temporal or geometric
object that `HC-DU-038` is meant to reconstruct.

## The identification ladder

| Level | Supplied object | What it can earn | What remains open |
|---|---|---|---|
| `G0` | Terminal values only | Outcome agreement | Order, provenance, time, geometry |
| `G1` | Authenticated reachability and provenance | A finite causal/operational order on the recorded events | Scale, local elapsed allocation, dimension, metric, proper time |
| `G2` | `G1` plus calibrated cover-edge differences | One scalar record-time potential when the cochain is exact | Path-dependent clock time, simultaneity convention, dimension, metric, curvature |
| `G3` | `G2` plus an independently calibrated sampling/volume law and path-indexed local-clock/reference data | A candidate statistical geometric reconstruction up to declared gauge | Uniqueness, continuum limit, physical selection, held-out prediction |
| `G4` | `G3` plus implementation-complete formation, access, uncertainty, and held-out interventions | A possible physical reconstruction or finite remainder | Ontological priority still requires a separate argument |

The present swing earns exact results only at `G1` and `G2`. `G3` and `G4`
are execution contracts, not conclusions.

## Theorem A — order-only nonidentification

For the declared finite object `Gamma_R`, authenticated order and provenance
alone do not generally identify temporal scale, local elapsed-time allocation,
ambient spacetime dimension, proper time, or metric geometry.

### Proof by minimal controls

Take the three-event chain

\[
0\prec1\prec2.
\]

The scalar assignments

\[
\tau=(0,1,4)
\quad\text{and}\quad
\tau'=(0,2,4)
\]

have the same order and the same endpoint elapsed value \(4\), but allocate
different durations to the two cover edges. Thus one endpoint clock
comparison does not identify the local allocation.

For any \(a>0\) and \(b\),

\[
\widetilde{\tau}=a\tau+b
\]

preserves the order while changing scale whenever \(a\neq1\). Order therefore
does not supply a physical unit.

Finally, place the three events at

\[
(t,\mathbf 0),\qquad t\in\{0,1,2\},
\]

in flat Minkowski spaces of dimensions \(2\), \(3\), and \(4\). Their strict
timelike relation is identical. This one finite record order therefore does
not identify its ambient dimension, much less a unique metric.

These are existence countermodels. They do not claim that every finite order
is compatible with every dimension or that causal order carries no geometric
information under stronger continuum assumptions.

## Theorem B — exact scalar record-time criterion

Give every directed cover edge \(e=(u,v)\in E\) a calibrated rational
difference \(w_e\). A scalar record-time potential

\[
\tau:V\rightarrow\mathbb Q
\]

satisfying

\[
w_{uv}=\tau(v)-\tau(u)
\]

exists if and only if the signed sum of \(w\) around every cycle in the
underlying undirected graph is zero.

If it exists, it is unique up to one additive constant on each weakly
connected component.

### Proof

Choose any orientation for the vertex-edge incidence matrix \(B\). The edge
differences induced by a vertex potential are

\[
w=B^\mathsf{T}\tau.
\]

Every cycle vector \(z\) lies in \(\ker B\). Hence a necessary condition is

\[
z^\mathsf{T}w
=z^\mathsf{T}B^\mathsf{T}\tau
=(Bz)^\mathsf{T}\tau
=0.
\]

Conversely, choose one root in each weak component and assign it time zero.
Propagate candidate times along a spanning forest. Every nonforest edge closes
one independent cycle. Zero circulation on that cycle makes its propagated
endpoint value agree with the forest assignment. The resulting \(\tau\)
satisfies every edge equation.

If \(\tau\) and \(\tau'\) induce the same \(w\), then

\[
B^\mathsf{T}(\tau-\tau')=0.
\]

The kernel consists exactly of functions constant on each weak component, so
the only remaining gauge is one additive origin per component. Since
\(\operatorname{rank}B=|V|-c\), the independent cycle-obstruction space has
dimension

\[
|E|-\operatorname{rank}B=|E|-|V|+c.
\]

This is standard finite graph linear algebra, used here as an exact typing
boundary rather than claimed as a new mathematical theorem.

## Exact diamond and hostile mutation

The probe uses the cover

\[
0\to1,\quad0\to2,\quad1\to3,\quad2\to3
\]

with

\[
\tau=(0,1,2,4).
\]

The edge differences are

\[
w_{01}=1,\quad w_{02}=2,\quad w_{13}=3,\quad w_{23}=2.
\]

The one independent signed loop has circulation

\[
1+3-2-2=0,
\]

so the potential reconstructs exactly.

Changing only \(w_{23}\) from \(2\) to \(3\) makes the circulation \(-1\).
No scalar potential then satisfies every edge. This rejects one **global
route-independent scalar clock model**. It does not, without further physical
calibration, reject standard quantum theory or relativity, and it does not
establish curvature.

## Theorem C — benign subdivision naturality

Replace one cover edge

\[
u\xrightarrow{w}v
\]

by a relay

\[
u\xrightarrow{a}r\xrightarrow{b}v,
\qquad a+b=w.
\]

Then:

1. reachability between the original vertices is unchanged;
2. every original-vertex potential difference is unchanged;
3. exactness of the edge cochain is unchanged;
4. the cycle-space dimension is unchanged; and
5. relay subdivisions compose.

The extension is constructive:

\[
\tau(r)=\tau(u)+a.
\]

Conversely, restricting any potential on the subdivided graph to the original
vertices reconstructs the replaced difference because \(a+b=w\). Exactness is
therefore preserved in both directions.

The subdivision adds one vertex and one edge, so

\[
(|E|+1)-(|V|+1)+c=|E|-|V|+c.
\]

Raw node count, edge count, interval cardinality, and hop length therefore
change under a representation-only refinement. They cannot be physical scale
observables unless the inserted relay carries additional latency, energy,
storage, noise, authentication, clock, control, or other charged physical
structure. A nonadditive split changes the contract and is not gauge.

## The important negative result

The exact potential test is deliberately weaker than a geometry theorem.

Two different physical semantics must not be conflated:

1. **Clock-offset or coordinate-potential differences.** Edge values are
   expected to be differences of one scalar. Zero cycle circulation is the
   right consistency condition.
2. **Path-indexed accumulated durations.** Edge values are local clock
   increments along different histories or worldlines. Different paths
   between two events may legitimately have different totals. Forcing them
   into one scalar would erase precisely the proper-time information needed
   for relativistic reconstruction.

This exposes a concrete correction to the earlier Dynamic Unity language:

> `Gamma_R` does not become geometric merely by acquiring weights. The
> physical semantics of each weight—and whether it is a potential difference,
> path functional, volume element, or comparison-channel output—must be
> independently calibrated.

## Collision with established geometry

This result does not compete with the known continuum reconstruction
theorems.

- Hawking, King, and McCarthy showed that suitable causal structure can
  determine causal, differential, and conformal structure
  ([Journal of Mathematical Physics, 1976](https://doi.org/10.1063/1.522874)).
- Malament sharpened the relation between timelike curves, topology, and
  conformal structure for suitably distinguishing spacetimes
  ([Journal of Mathematical Physics, 1977](https://doi.org/10.1063/1.523436)).
- The causal-set program explicitly combines local finiteness with causal
  order rather than treating order alone as a complete metric
  ([Bombelli et al., 1987](https://doi.org/10.1103/PhysRevLett.59.521)).
- At finite sprinkling density, comparisons of Lorentzian geometries are
  statistical and resolve only down to a finite volume scale
  ([Bombelli, 2000](https://arxiv.org/abs/gr-qc/0002053)).

The correct boundary is therefore:

- order can carry substantial conformal/topological information under strong
  continuum hypotheses;
- a finite record-order sample generally underidentifies its ambient
  realization;
- conformal scale or volume requires additional structure;
- event count becomes volume only through a calibrated physical sampling or
  density law; and
- Dynamic Unity's exact finite cochain result is ordinary graph
  cohomology/synchronization mathematics.

What is useful to Dynamic Unity is the combined **identification ladder** and
the refusal to confuse its levels.

## Next physical reconstruction contract

The next `HC-DU-038` swing should freeze one physically interpreted fixture
with four separate data types:

1. **Order/provenance:** authenticated event identities and reachability.
2. **Sampling/volume:** an independently justified map from formed record
   events to physical volume, with density and selection uncertainty.
3. **Local clocks:** path-indexed clock readings, redshift or transport
   comparisons, calibration covariance, and explicit worldline identity.
4. **Reference/access structure:** which comparisons are physically
   available to which observer or region, with latency, noise, energy, and
   authentication charged.

Then construct at least two geometrically nonisomorphic candidates that match
all training meta-records. Reveal the data types sequentially and reserve
held-out interval-volume, clock-comparison, and reference-transport
observables.

The verdicts are:

- `ORDER_ONLY_NONIDENTIFIED`;
- `SCALAR_RECORD_TIME_RECONSTRUCTED`;
- `GEOMETRY_CLASS_RECONSTRUCTED_UP_TO_GAUGE`;
- `FINITE_GEOMETRIC_REMAINDER`;
- `INCOMPLETE_PHYSICAL_CONTRACT`.

The first specimen should be small enough for exact or certified numerical
inference. Scaling is allowed only after the smallest rival pair is separated
or proven indistinguishable.

## Stops and reopeners

Stop if:

- the metric, manifold, dimension, density, clock, or frame is inserted into
  the record definition and then “reconstructed”;
- raw relay, hop, or event counts are treated as physical lengths or volumes;
- path-dependent proper time is forced into a global scalar potential;
- a loop residual is called curvature before calibration and provenance nulls
  are excluded;
- a finite causal order is claimed to erase the established continuum
  causal-reconstruction literature; or
- representation or reconstruction is promoted to record fundamentality.

Reopen physical geometry only with:

- independently calibrated density/volume evidence;
- path-indexed local clock and comparison records;
- an explicit gauge and refinement category;
- nonisometric matched controls;
- held-out geometric observables; and
- implementation-complete formation, provenance, access, and uncertainty.

## Reproducibility

From the repository root:

```bash
python3 tests/du_meta_record_geometry_identification_probe.py
```

The probe uses exact rational arithmetic. It checks the order-only
countermodels, incidence rank, cycle obstruction, potential recovery,
additive-origin gauge, relabeling naturality, disconnected-component origins,
exact and mutated diamonds, one and two composed subdivisions, a nonadditive
physical relay, and the no-cycle tree control.
The machine-readable artifact is
`tests/artifacts/du_meta_record_geometry_identification_result.json`.

Passing establishes the scoped finite claims above. It establishes no physical
geometry, proper time, ontology, theorem novelty, new law, or paper verdict.
