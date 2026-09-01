---
title: "Action-selected holonomy, material-record interface ambiguity, and computation-first stop"
status: banked_scoped_interface_nonselection_result
doc_type: theorem_obstruction_and_exact_standard_quantum_control
created: 2026-08-31
claim_id: HC-DU-208
run_id: RUN-20260831-action-selected-holonomy-material-record-gate
program_id: DU-COMPUTATION-FIRST-CLOSED-TRANSITION-SUBSTRATE
action_id: CTS-A3-ACTION-SELECTED-HOLONOMY-MATERIAL-RECORD-GATE
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
portfolio_return: ACTION_SELECTED_HOLONOMY_INTERFACE_AMBIGUITY
observer_index_return: OBSERVER_INDEX_REMAINS_SUPPLIED
---

# Executive result

`HC-DU-207` found a genuine positive boundary: one frozen source action can
select a relational transport orbit, `Z2` holonomy, response spectrum, and
two coarse spectral bands before any observer or record is named. The present
gate asks whether that selected invariant also selects its physical sampling,
retention, access, and use.

It does not, even under the strongest favorable standard-quantum reading.

> A Hamiltonian can canonically select a spectral PVM while failing to select
> a quantum instrument, blank-to-written pointer coupling, archive, observer
> access route, or record-conditioned continuation.

On the unchanged four-site frustrated oscillator, the two action-selected
bands are each two-dimensional. There are two exact, repeatable,
energy-preserving instruments with:

- the same source Hamiltonian and negative holonomy;
- the same low/high effects and therefore the same Born law for every input;
- the same material pointer values and pointer probabilities;
- the same exact energy distribution; but
- orthogonal conditional future states for one low-band input.

The difference is a unitary twist inside the exactly degenerate low band. It
commutes with the source Hamiltonian and leaves the selected record value
unchanged. A later coupling can independently leave the archive sealed or
copy it to an observer, and can independently ignore the archive or use it to
control a target.

The preregistered return is therefore:

```text
ACTION_SELECTED_HOLONOMY_INTERFACE_AMBIGUITY
+ LATENT_RESPONSE_ONLY_ABSORBED
+ OBSERVER_INDEX_REMAINS_SUPPLIED
```

This is scoped Grade 4: an exact nonimplication in the frozen source class,
not a universal no-go. Spectral measurement, Lüders instruments, QND
measurement, unitary freedom in degenerate eigenspaces, Naimark--Stinespring
dilation, and controlled quantum operations absorb all component
mathematics. There is no new physics or empirical excess.

# 1. Frozen antecedent and strongest favorable grant

Keep the exact `HC-DU-207` frustrated action

\[
S_\sigma(q)=\frac12\sum_{(u,v)}(q_u-\sigma_{uv}q_v)^2,
\qquad
\prod_{e\in C_4}\sigma_e=-1.
\]

Its signed Laplacian is `L_-`. Add the same unit mass term and use the standard
quadratic oscillator Hamiltonian

\[
H=\frac12p^Tp+\frac12q^T(I+L_-)q.
\]

On the one-excitation normal-mode sector, the relevant Hamiltonian is

\[
\Omega=(I+L_-)^{1/2}.
\]

The stiffness eigenvalues are

\[
3-\sqrt2,\;3-\sqrt2,\;3+\sqrt2,\;3+\sqrt2,
\]

and the one-excitation frequencies are their positive square roots. Let
`P_low` and `P_high` be the spectral projectors onto the two distinct
eigenvalues.

This gate grants the positive case as much as the action can honestly earn:

> The functional calculus of the source Hamiltonian canonically selects the
> low/high PVM as an invariant response decomposition.

That is stronger than merely choosing a convenient observable after seeing
the target. It still does not identify a sampled outcome or material record.

# 2. Spectral PVM does not select an instrument

## Theorem 1 — degenerate spectral-instrument ambiguity

Let

\[
H=\sum_a E_aP_a
\]

be a finite Hamiltonian and suppose one eigenspace `P_b H` has dimension at
least two. For every family of unitaries `U_a` satisfying

\[
U_aP_a=P_aU_aP_a,
\]

the operations

\[
\mathcal I_a(\rho)=U_aP_a\rho P_aU_a^\dagger
\]

form a repeatable quantum instrument for the same spectral PVM. Its effects
are

\[
K_a^\dagger K_a=P_a,
\qquad K_a=U_aP_a.
\]

Consequently every such instrument has the same outcome probability

\[
\Pr(a\mid\rho)=\operatorname{tr}(P_a\rho)
\]

for every input state. Every conditional output remains inside its recorded
eigenspace, and every `U_a` commutes with `H` on that sector, so the complete
energy distribution is unchanged.

If `dim(P_b H)>=2`, choose orthogonal vectors `|psi>` and `|phi>` in the
`b`-eigenspace and one `U_b` with

\[
U_b|\psi\rangle=|\phi\rangle.
\]

The Lüders instrument `K_b=P_b` and the twisted instrument
`K'_b=U_bP_b` then return the same certain record value `b`, but their
conditional future states are orthogonal. Therefore the Hamiltonian and its
spectral PVM do not select a unique instrument or continuation. `square`

The obstruction is stronger than ordinary measurement disturbance. Both
instruments are:

- normalized;
- repeatable at the band level;
- exactly energy preserving;
- covariant with the spectral decomposition; and
- identical on all outcome statistics.

The missing datum is the physical operation inside the degenerate sector.

# 3. A pointer dilation does not repair selection

For orthonormal pointer states `|a>_A`, define

\[
V_U=\sum_a U_aP_a\otimes|a\rangle_A.
\]

Then

\[
V_U^\dagger V_U=I.
\]

Each `V_U` is an exact isometry from the source into source plus a
blank-to-written two-state pointer. All choices have the same pointer law,
but their conditional source continuations can differ.

This proves two distinct points:

1. a formal material writer can be added without inconsistency; and
2. the source action does not choose which writer dilation is physical.

Naimark--Stinespring extension guarantees that such isometries can be
embedded in unitary apparatus dynamics. That theorem supplies existence, not
selection. Calling one extension “the measurement” would refit the interface
forbidden by `CTS-A3`.

# 4. Access and use remain separate physical couplings

Once the pointer contains a sharp low/high value, at least two further forks
remain exact.

## Access fork

Let an observer bit begin blank. One continuation leaves it uncoupled; another
copies the pointer value to it. The source Hamiltonian, pointer state, and
holonomy are identical, while the observer's accessible state differs
orthogonally on the high branch.

Therefore:

```text
formed pointer
  != physically selected observer access.
```

## Consumer fork

Let a target bit begin blank. One continuation ignores the pointer; another
applies a pointer-controlled flip. Again the source and retained archive are
unchanged, while the target response differs orthogonally.

Therefore:

```text
formed pointer and retained value
  != physically selected action-enabling use.
```

This is the `HC-DU-205` consumer-freedom theorem applied to a newly
action-selected invariant. The new result is upstream: even the instrument
that writes the selected invariant remains plural.

# 5. Complete material-handoff passport

| Field | CTS-A3 disposition |
|---|---|
| Source action and signed transport | Conditionally selected by the frozen model |
| `Z2` holonomy and response spectrum | Selected up to gauge |
| Low/high spectral PVM | Selected by functional calculus |
| Sampler / quantum instrument | Not selected; two exact QND realizations |
| Material carrier and blank | Supplied |
| Write coupling | Supplied |
| Occurrence and source provenance | Conditional on the supplied coupling and epoch |
| Archive retention and reset | Supplied |
| Observer/access boundary and route | Supplied |
| Consumer and matched continuation | Not selected |
| Resource and reliability horizon | Supplied |
| Rival-excluding certificate and public finality | Absent |
| Absolute ruler | Absent, as in `HC-DU-207` |

The strongest positive chain is now exact:

```text
source action
  -> transport gauge orbit
  -> holonomy
  -> response spectrum
  -> canonical spectral PVM
```

The unsupported cast is also exact:

```text
canonical spectral PVM
  -/-> sampled outcome
  -/-> selected material writer
  -/-> occurrence provenance
  -/-> observer access
  -/-> selected consumer
  -/-> public finality.
```

# 6. Relation to prior results

This is not a repetition of the earlier boundaries.

- `HC-DU-159` proves that a bare process does not universally select an
  informative, nondisturbing, materially formed interface.
- `HC-DU-205` proves that a fixed formed record algebra does not select its
  downstream consumer.
- `HC-DU-207` proves that a source action can select relational holonomy and a
  spectral response before it selects a record.
- `HC-DU-208` now joins them: even when the action supplies a canonical,
  holonomy-sensitive PVM, the instrument, material implementation, access,
  and use remain unselected.

The join matters because it closes the tempting repair “perhaps the newly
action-selected invariant automatically becomes the record.” It does not.

# 7. Grade, absorption, and stop

## What is earned

- a scoped theorem that an exactly degenerate spectral response admits
  inequivalent repeatable energy-preserving instruments with identical PVM;
- an exact same-action/same-record/different-continuation witness;
- a complete material-handoff passport locating every surviving supplied
  field; and
- a standard-quantum transfer using the unchanged `HC-DU-207` source.

## What is not earned

- a universal instrument no-section theorem;
- a proof that every action-selected invariant fails to select a record;
- a material record produced without a supplied apparatus;
- observer derivation, provenance, certification, regional/public finality,
  metric, or ruler;
- empirical excess, a novel physical law, or a paper claim.

## Strongest absorbers

The theorem's components are standard spectral and instrument theory. The
Dynamic Unity increment is the typed location of the exact first leak in the
computation-first campaign, not novel component mathematics.

## Campaign disposition

`CTS-A3` meets its cheapest kill. The holonomy remains a latent physical
response invariant until an instrument and archive are supplied. The
computation-first campaign has now extracted its useful positive result and
closed its promised material-record bridge test.

No successor is selected. Reopen only with a genuinely different
source-pinned action, constraint, or stable interaction that selects a
complete writer--consumer--access--provenance--resource orbit, or produces a
finite no-refit remainder. Another graph, PVM, pointer, Wilson loop, QND
instrument, or consumer variant does not satisfy that reopener.
