---
run_id: RUN-20260729-072609-reciprocal-crosslink-self-calibration-gate
status: completed
started_at: 2026-07-29T07:26:09-05:00
completed_at: 2026-07-29T07:31:25-05:00
repository: dynamic-unity
work_id: CCR-RECIPROCAL-CROSSLINK-SELF-CALIBRATION-GATE
claim_id: HC-DU-108
state_revision: 59
---

# Run receipt

## Outcome

Banked a conditional Grade-3 self-calibrated event reconstruction up to
declared gauge and scoped Grade-4 reciprocity, latency, scale, and provenance
necessity boundaries.

For honest stationary unit-rate clocks and reciprocal unit-speed propagation,
the directed timestamp record

\[
p_{ij}=d_{ij}+b_j-b_i
\]

and its reverse recover

\[
d_{ij}=\frac{p_{ij}+p_{ji}}2,
\qquad
b_j-b_i=\frac{p_{ij}-p_{ji}}2.
\]

The complete distance matrix of four affinely independent detectors
reconstructs their spatial constellation up to Euclidean isometry. Connected
offset differences reconstruct the clocks up to one common time-origin
shift. Applying those recovered values to the held-out event readings
reproduces the `HC-DU-107` arrival packet in the selected gauge, so its
uniform event-localization margin transfers unchanged.

The regular-tetrahedron control has squared edge length eight and anchored
Gram matrix

\[
\begin{pmatrix}
8&4&4\\
4&8&4\\
4&4&8
\end{pmatrix},
\]

of rank three.

The exact hostile controls identify what remains supplied.

1. With directed delays,
   \[
   p_{ij}=a_{ij}+b_j-b_i
   \]
   is invariant under
   \[
   b_i'=b_i+c_i,\qquad a_{ij}'=a_{ij}+c_i-c_j.
   \]
   Clock offset and path asymmetry are nonidentifiable.
2. Unknown transmit/receive or pairwise hardware latency contaminates both
   range and offset and can absorb a changed spatial distance.
3. An unknown common clock rate is exactly confounded with spatial scale.
4. Authentication certifies message origin and integrity, not timestamp
   truth, physical clock state, path reciprocity, or absence of a delay
   attack.

The result closes a real part of the supplied-scaffold objection: numerical
detector positions and relative clock offsets can arise from finite
crosslink records. It does not physically select the nodes, clocks,
reciprocal law, hardware boundary, rate unit, or protocol. It also selects no
preferred foliation; the reconstructed clock frame is an operational
coordinate gauge inside the frozen stationary model.

## Literature collision

- Autolocated relativistic positioning already uses cross-broadcast proper
  times to recover emitter trajectories and metric information on the
  constellation.
- Clock-rigidity and TOA/TDOA self-calibration theory already establish joint
  position-clock recovery up to translation, rotation, offset, and scale
  gauges under bidirectional timestamp assumptions.
- NIST two-way time transfer documents cancellation under reciprocal paths
  and the remaining equipment, propagation, and Sagnac corrections.
- Network Time Security documents that authenticated synchronization packets
  can still be delayed asymmetrically and that cryptography does not remove
  the induced timing error.

Dynamic Unity claims the typed composition and boundary, not new positioning,
clock, rigidity, synchronization, cryptographic, or distance-geometry
mathematics.

## Disposition

- `HC-DU-108` is recorded in the concept and counter-assumptive registers.
- The quantum-foundations orientation surface now distinguishes
  self-calibrated geometry up to gauge from physical selection of
  reciprocity, latency, and scale.
- The candidate class is narrowed to a source-formed nonlinear interaction
  event with reciprocal clock-rigid self-calibrating crosslinks, bounded
  latency/asymmetry, complete provenance/acquisition, and no-refit regional
  geometry transfer.
- `CURRENT-RESEARCH.yaml` advances to revision 59.
- Dynamic Unity remains quiescent with no selected successor.
- No paper, prediction, experiment, provider, hardware, or external contact
  was activated.

## Validation

- `du_reciprocal_crosslink_self_calibration_probe.py`: **PASS** — reciprocal
  range/offset recovery, exact full-rank tetrahedral Gram control, event
  composition up to common time origin, directed-delay clock gauge,
  hardware-latency/range confounding, and clock-rate/scale confounding.
- `du_agent_orientation_contract_probe.py`: **PASS**, 37/37 checks, 265
  unique counter-assumptive rows, 38 stable links, and 5,981/6,000
  cold-start words.
- `du_hypothesis_efficient_approach_registry_probe.py`: **PASS**, 10/10.
- `du_near_term_swing_approach_atlas_probe.py`: **PASS**, 16/16.
- Direct PyYAML/JSON authority and artifact assertions: **PASS** at revision
  59 with no active scientific program, executable action, or selected
  successor.
- Python compilation and `git diff --check`: **PASS**.
