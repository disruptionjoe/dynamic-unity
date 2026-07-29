# Regional cycle records: exact gluing deficit, cross-region repair, and layered remainder

**Date:** 2026-07-29
**Run:** `RUN-20260729-133113-regional-cycle-record-gluing`
**Claim:** `HC-DU-124`
**Status:** **BANKED — SCOPED GRADE 4 EXACT REGIONAL-GLUING NECESSITY THEOREM / STANDARD MAYER--VIETORIS MATHEMATICS / NO PUBLIC-FINALITY, INTERFACE-SELECTION, RESOURCE-LAW, OR EMPIRICAL PROMOTION**

## Plain-English result

Two regions may each possess every loop fact internal to that region and still
fail to determine the loop facts of the combined network.

The reason is precise. Suppose the two connected regions overlap in \(k\)
disconnected pieces. A loop can leave one overlap piece through region \(A\)
and return through region \(B\). Neither region's internal loop record sees
that cross-region loop. There are exactly \(k-1\) independent missing loop
values.

Therefore:

- a connected overlap makes compatible complete local cycle records determine
  the complete global cycle record uniquely;
- an overlap with \(k\) connected components leaves exactly
  \(|G|^{k-1}\) possible global cycle records;
- \(k-1\) cross-region loop values are necessary and sufficient to complete
  the global cycle record; and
- even after that repair, the complete physical dressed-edge state is still
  not reconstructed. The \(|G|^{|V|-1}\) physical coboundary remainder from
  `HC-DU-123` survives.

The important variable is the number of connected overlap components, not the
number of shared vertices or edges.

## Why this question matters to Dynamic Unity

`HC-DU-121` constructs a finite-Abelian matter-completed Wilson-record
instrument. `HC-DU-122` shows that one complete cycle record determines every
closed response but not an open-line response. `HC-DU-123` generalizes that
result to an arbitrary connected finite graph:

\[
\text{complete cycle record}=[y]\in H^1(\Gamma;G),
\]

with an affine physical coboundary fibre of size
\(|G|^{|V|-1}\).

The next regional-finality question is not whether a complete global record
has a remainder. It is whether independently complete regional records even
determine that global record.

This distinction is essential:

```text
complete within every region
    does not automatically mean
complete for the union.
```

`HC-DU-124` computes the exact obstruction and keeps it separate from the
physical remainder that remains after global gluing succeeds.

## Frozen arena

Let:

1. \(\Gamma=(V,E)\) be a finite connected graph;
2. \(\Gamma=A\cup B\), where \(A\) and \(B\) are connected subgraphs;
3. \(I=A\cap B\) be nonempty and have \(k\geq1\) connected components;
4. \(G\) be a nontrivial finite Abelian group;
5. regular-representation matter make each dressed edge
   \(y_e\in G\) a physical gauge-invariant coordinate; and
6. each region form its complete local cycle class,
   \([y|_A]\in H^1(A;G)\) and \([y|_B]\in H^1(B;G)\).

The local records are **compatible** when their restrictions agree on every
cycle in \(I\). Any pair obtained by restricting one global edge
configuration is automatically compatible.

The cover, matter, local record instruments, association, provenance,
acquisition, observer access, and allowed action class are supplied. Nothing
in the theorem physically selects them.

## Theorem 1 — exact regional gluing deficit

Let

\[
r:H^1(\Gamma;G)\longrightarrow
H^1(A;G)\oplus H^1(B;G)
\]

be restriction to the two regions.

Then

\[
\ker r
\cong
H^0(I;G)/\Delta G
\cong
G^{k-1}.
\]

Consequently, every compatible pair of complete local cycle records has
exactly

\[
|G|^{k-1}
\]

global cycle-class completions.

### Proof

The cohomological Mayer--Vietoris exact sequence contains

\[
H^0(A;G)\oplus H^0(B;G)
\longrightarrow
H^0(I;G)
\xrightarrow{\delta}
H^1(\Gamma;G)
\xrightarrow{r}
H^1(A;G)\oplus H^1(B;G).
\]

Because \(A\) and \(B\) are connected,

\[
H^0(A;G)\cong G,\qquad H^0(B;G)\cong G.
\]

Because \(I\) has \(k\) connected components,

\[
H^0(I;G)\cong G^k.
\]

The first map changes all \(k\) component values by one common difference,
so its image is the diagonal subgroup

\[
\Delta G=\{(g,\ldots,g):g\in G\}.
\]

Exactness gives

\[
\ker r=\operatorname{im}\delta
\cong G^k/\Delta G
\cong G^{k-1}.
\]

The next segment of the sequence is

\[
H^1(\Gamma;G)
\xrightarrow{r}
H^1(A;G)\oplus H^1(B;G)
\longrightarrow H^1(I;G)
\longrightarrow H^2(\Gamma;G).
\]

A graph has no two-cells, so \(H^2(\Gamma;G)=0\). Therefore every compatible
local pair is in the image of \(r\), and every such fibre is a coset of
\(\ker r\). It consequently has exactly \(|G|^{k-1}\) elements. \(\square\)

### Immediate consequences

If \(k=1\), restriction is injective on global cycle classes. Compatible
complete local records uniquely determine the global cycle record.

If \(k>1\), the local records are globally incomplete even though neither is
missing any cycle internal to its own region.

This is not caused by a small overlap. Two shared vertices joined by a shared
edge give \(k=1\) and no deficit. The same two shared vertices with no shared
path give \(k=2\) and one missing \(G\)-valued loop fact.

## Theorem 2 — minimum cross-region repair

Choose one component \(I_0\) of \(I\) as a base. For every other component
\(I_j\):

1. choose a path in \(A\) from \(I_0\) to \(I_j\); and
2. return from \(I_j\) to \(I_0\) along a path in \(B\).

The concatenation is a cross-region cycle \(C_j\). The \(k-1\) values

\[
\langle C_j,y\rangle\in G
\]

together with the compatible local records uniquely determine the global
cycle class.

Under a contract in which each additional coordinate takes one value in
\(G\), \(k-1\) such coordinates are also necessary.

### Why the construction is sufficient

The cross cycles represent the \(k-1\) independent ways of comparing one
overlap component with the selected base component. Their classes span the
quotient of global cycles by cycles already internal to \(A\) or \(B\).
Their values therefore separate the \(G^{k-1}\) kernel of the restriction
map.

The path choices are coordinate choices. Replacing a chosen path changes a
cross cycle by cycles already recorded inside \(A\), \(B\), or \(I\), so it
does not change the completed global equivalence relation.

### Why the count is necessary

For a fixed compatible local pair there are \(|G|^{k-1}\) global cycle
classes. Fewer than \(k-1\) \(G\)-valued coordinates have fewer than
\(|G|^{k-1}\) possible joint values and cannot distinguish every completion.

This is an informational coordinate lower bound. It is not a communication,
latency, energy, entanglement, fault-tolerance, or cryptographic cost.

## Theorem 3 — regional cycle-rank identity

For a finite graph \(X\), write

\[
\beta_1(X)=|E_X|-|V_X|+\beta_0(X).
\]

Because \(A\) and \(B\) are connected while \(I\) has \(k\) components,

\[
\boxed{
\beta_1(\Gamma)
=
\beta_1(A)+\beta_1(B)-\beta_1(I)+(k-1)
}.
\]

The term \(k-1\) is precisely the rank of the cross-region cycle sector
missing from the local records after their common overlap cycles have been
identified.

The identity follows either from the dimensions in Mayer--Vietoris or
directly from inclusion--exclusion on vertices and edges.

## Theorem 4 — the layered physical fibre

`HC-DU-123` proves that every global cycle class contains

\[
|G|^{|V|-1}
\]

distinct physical dressed-edge basis configurations. These are
coboundary-related but are not gauge-equivalent after the charged matter
completion is retained.

Since one compatible local-record pair has \(|G|^{k-1}\) possible global
cycle classes, its complete physical fibre has

\[
\boxed{
|G|^{k-1}|G|^{|V|-1}
=
|G|^{|V|+k-2}
}
\]

basis configurations.

The two remainder layers have different meanings:

```text
compatible complete local cycle records
  + k-1 cross-region cycle values
      = complete global cycle record
  + |V|-1 spanning-tree dressed-edge values
      = complete dressed-edge basis state.
```

Thus:

- the first layer is a **regional gluing deficit**;
- the second is the **physical open-path/coboundary remainder** already
  identified by `HC-DU-123`; and
- repairing the first layer does not repair the second.

Under the same \(G\)-valued-coordinate contract, completing the physical
state from a fixed local-record pair requires at least

\[
(k-1)+(|V|-1)=|V|+k-2
\]

additional coordinates. Cross-cycle values plus the dressed edges of any
global spanning tree attain this count.

Again, neither the cross paths nor the spanning tree is preferred physical
structure. They are decoder coordinates, and physically acquiring them is a
separate problem.

## Exact controls

The deterministic regression exhausts all dressed-edge assignments for five
finite covers.

| Cover | \(G\) | Overlap | Global classes per local record | Physical states per local record |
|---|---:|---:|---:|---:|
| Two triangles sharing one vertex | \(\mathbb Z_2\) | \(k=1\) | \(1\) | \(2^4=16\) |
| Two paths forming one cycle | \(\mathbb Z_3\) | \(k=2\) | \(3\) | \(3^4=81\) |
| Two trees sharing three terminals | \(\mathbb Z_2\) | \(k=3\) | \(4\) | \(2^8=256\) |
| Cyclic overlap plus one isolated overlap vertex | \(\mathbb Z_2^2\) | \(k=2\) | \(4\) | \(4^6=4096\) |
| Two squares sharing one edge | \(\mathbb Z_3\) | \(k=1\) | \(1\) | \(3^5=243\) |

The second and fifth controls each have two shared vertices. The disconnected
overlap in the second leaves three global completions; the connected overlap
in the fifth leaves one. This isolates connectivity from overlap
cardinality.

The cyclic-overlap control verifies that internal overlap cycles are retained
as compatibility conditions rather than being incorrectly counted as new
cross-region facts.

## What is genuinely learned

The mathematics is standard. Mayer--Vietoris already supplies the gluing
sequence, and graph cohomology supplies the finite specialization. The
Dynamic Unity increment is the typed physical decomposition:

1. **regional completeness** — every internal cycle fact;
2. **overlap compatibility** — agreement on facts recorded by both regions;
3. **cross-region completion** — the \(k-1\) loop facts spanning disconnected
   overlap pieces;
4. **global cycle completeness** — all closed-chain responses; and
5. **physical state completeness** — the additional endpoint/open-path
   coordinates.

This shows exactly why "every region has finalized its own record" is not
enough to establish global finality. It also shows when that particular
obstruction disappears: compatible local cycle records glue uniquely when
the overlap is connected.

What remains open is more important physically:

- what dynamics selects the regions and their overlap;
- what forms and retains the local cycle records;
- what makes a cross-cycle value accessible and verifiable;
- what fault, adversary, provenance, and communication model makes it a
  certificate;
- whether the record is nondemolition;
- what resources formation and transfer require; and
- whether any comparable structure survives in continuum local quantum field
  theory.

## Absorbers and novelty boundary

The strongest mathematical absorber is the Mayer--Vietoris exact sequence;
see Allen Hatcher, [*Algebraic
Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).

The physical observable classes remain absorbed by:

- Beckman, Gottesman, Kitaev, and Preskill,
  [*Measurability of Wilson loop
  operators*](https://arxiv.org/abs/hep-th/0110205); and
- Gliozzi,
  [*The functional form of open Wilson
  lines*](https://arxiv.org/abs/hep-lat/0511039).

`HC-DU-124` does not claim new algebraic topology. Its scoped Grade-4 status
comes from proving an exact necessity and sufficiency boundary in the frozen
Dynamic Unity physical arena, not from mathematical novelty.

## Scope and non-promotions

This result does **not** establish:

- physical selection of the graph, regional cover, overlap, cycle basis,
  matter content, local record interface, cross paths, or spanning tree;
- formation, provenance, access, acquisition, authentication, trust, or
  verification of any record;
- Byzantine agreement, quorum finality, common knowledge, threshold
  cryptography, or consensus;
- a communication, latency, energy, entropy, entanglement, or disturbance
  law;
- full physical-state reconstruction from the global cycle record;
- transfer to disconnected regions, covers by three or more regions,
  non-Abelian groups, continuous groups, higher cell complexes, AQFT, or
  continuum QFT;
- empirical excess, a prediction, ontology priority, or new physics; or
- authorization for a paper, experiment, hardware, provider, publication,
  submission, contact, or sibling-repository change.

## Disposition

```text
CONNECTED_OVERLAP_MAKES_COMPATIBLE_LOCAL_CYCLE_RECORDS_GLOBALLY_UNIQUE
DISCONNECTED_OVERLAP_CREATES_EXACT_CROSS_REGION_GLUE_DEFICIT
GLUE_DEFICIT_IS_GROUP_ORDER_TO_OVERLAP_COMPONENTS_MINUS_ONE
OVERLAP_COMPONENT_COUNT_NOT_OVERLAP_SIZE_CONTROLS_THE_DEFICIT
K_MINUS_ONE_CROSS_CYCLE_COORDINATES_ARE_NECESSARY
K_MINUS_ONE_CROSS_CYCLE_COORDINATES_ARE_SUFFICIENT
REGIONAL_CYCLE_RANK_OBEYS_THE_MAYER_VIETORIS_IDENTITY
LOCAL_TO_GLOBAL_CYCLE_COMPLETION_STILL_LEAVES_PHYSICAL_COBBOUNDARY_REMAINDER
LOCAL_RECORD_FIBRE_SIZE_IS_GROUP_ORDER_TO_VERTICES_PLUS_COMPONENTS_MINUS_TWO
TOTAL_UNIVERSAL_REPAIR_NEEDS_VERTICES_PLUS_COMPONENTS_MINUS_TWO_GROUP_COORDINATES
REGIONAL_GLUE_IS_NOT_PUBLIC_FINALITY_WITHOUT_ACCESS_FAULT_AND_CERTIFICATION_TYPES
NO_RESOURCE_LAW_INTERFACE_SELECTION_OR_EMPIRICAL_EXCESS
NO_READY_SUCCESSOR
```

## Reopeners

1. Extend the theorem to a finite good cover with three or more regions and
   identify the Čech nerve and higher compatibility obstructions.
2. Move from graphs to finite two-complexes, separating \(H^1\) gluing from
   curvature and \(H^2\).
3. Construct a physical protocol that forms the local and cross-cycle
   records under one unchanged causal, resource, and disturbance contract.
4. Add an explicit fault/adversary model and test whether any topological
   gluing coordinate becomes a genuine public-finality certificate.
5. Identify the non-Abelian or operator-algebraic analogue without assuming
   that group-valued coordinate counting survives.

## Regression

Run:

```bash
python3 tests/du_regional_cycle_record_gluing_probe.py
```

The deterministic artifact is
`tests/artifacts/du_regional_cycle_record_gluing_result.json` and reports
`17/17` exact checks over five finite regional covers.
