---
title: "Aharonov--Casher charge-parity-selected fluxoid transition rule and signed-writer obstruction"
status: banked_scoped_physical_transition_rule_selection_result
doc_type: exact_response_quotient_transition_graph_and_writer_no_section
created: 2026-09-02
claim_id: HC-DU-225
run_id: RUN-20260902-aharonov-casher-charge-selected-fluxoid-transition-rule
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

`HC-DU-223` found a natural electric-charge response, and `HC-DU-224` found a
topology-selected fluxoid material record. The apparent next move was to join
them with a physical charge-to-fluxoid writer. The Aharonov--Casher effect
provides a real standard-physics coupling, but it reveals that the initial
question was typed too narrowly.

In a symmetric two-path superconducting circuit, charge on an island changes
the relative phase of two fluxon-tunnelling paths. For integer charge `q` in
units of the electron charge, the single-phase-slip amplitude has the frozen
form

\[
A_{\rm SPS}(q)=a+(-1)^q b.
\tag{1}
\]

When `a=b`, odd charge cancels single-fluxon tunnelling. Double slips remain,
so the fluxoid transition graph splits into even and odd winding components.
For even charge, single slips reconnect those components. The electric source
therefore selects the admissible transition graph—and hence whether fluxoid
parity is protected—without selecting which winding value is actually stored.

This is a physical coupling between the two preceding results, but not their
complete handoff:

- it retains charge only modulo `2e`, not total signed charge;
- it selects a transition rule, not a unique endpoint record;
- exact protection requires a symmetric coherent two-path circuit;
- a one-shot endpoint gives overlapping evidence rather than a two-sided
  zero-error charge certificate; and
- a time-reversal-invariant charge source cannot choose a nonzero signed
  winding without a time-odd bias or orientation.

The new Dynamic Unity distinction is:

```text
source selects record value
  != source selects record transition/admissibility rule.
```

The second is physically real and may be more fundamental for capability and
regional-finality architectures, but it does not satisfy the first by renaming.

The disposition is:

```text
AHARONOV_CASHER_PHYSICAL_COUPLING_FOUND
+ CHARGE_PARITY_SELECTS_TRANSITION_RULE
+ FLUXOID_PARITY_PROTECTION_IS_CONDITIONAL
+ FULL_CHARGE_IS_QUOTIENTED_AWAY
+ TRANSITION_RULE_IS_NOT_RECORD_VALUE
+ ONE_ENDPOINT_IS_NOT_ZERO_ERROR_CHARGE_CERTIFICATE
+ TIME_REVERSAL_FORBIDS_UNBIASED_SIGNED_WRITE
+ SYMMETRY_AND_ORIENTATION_REMAIN_ANTECEDENTS
+ NO_COMPLETE_HC-DU-223-TO-224_HANDOFF
+ NO_READY_SUCCESSOR
```

# 1. The physical chain and its types

The source-side quantity inherited from `HC-DU-223` is total electric charge.
The material record inherited from `HC-DU-224` is a fluxoid winding sector.
The Aharonov--Casher bridge is neither an equality nor a classical copy:

```text
enclosed island charge
  -> relative quantum phase between coherent fluxon paths
  -> single-phase-slip interference amplitude
  -> allowed transition graph on fluxoid sectors
  -> conditional retention/protection of fluxoid parity.
```

Five objects must remain separate:

| object | type | what it determines |
|---|---|---|
| total charge `Q` | source response | electric charge before quotient |
| `Q mod 2e` | topological/interference quotient | the charge parity seen by the symmetric circuit |
| phase-slip amplitude/rate | latent physical response | how readily the circuit moves between fluxoid sectors |
| transition graph | admissibility/capability structure | which winding changes are physically enabled |
| realized fluxoid endpoint | material record value | which sector the actual history occupies after an interaction |

The coupling can select rows two through four without fixing row five.

# 2. Aharonov--Casher interference as the selected coupling

For two coherent fluxon paths around a charged island, the relative
Aharonov--Casher phase is periodic in enclosed charge. Restricting to integral
electron-charge sectors yields the relative sign `(-1)^q`. If the two path
amplitudes are `a` and `b`, equation (1) gives the net single-slip amplitude and

\[
\Gamma_{\rm SPS}(q)\propto
\left|a+(-1)^q b\right|^2.
\tag{2}
\]

At the symmetric point `a=b`:

\[
\Gamma_{\rm SPS}(q)
\propto
\begin{cases}
4a^2,&q\text{ even},\\
0,&q\text{ odd}.
\end{cases}
\tag{3}
\]

This is not an analyst-chosen decoder. Once the superconducting circuit,
coherent paths, island charge coupling, and symmetric operating point are
frozen, the Hamiltonian supplies the phase and interference response. Pop et
al. measured the multi-path interference pattern; Bell et al. observed
charge-controlled suppression of fluxon tunnelling; and the bifluxon device
used the odd-charge point to protect fluxon parity.

The antecedents remain load-bearing. Charge alone does not create two coherent
paths or make their amplitudes equal. The circuit and preparation select the
arena in which charge parity has this consequence.

# 3. The source selects a transition graph

Let winding sectors be indexed by integers `n`. A single phase slip connects

\[
n\longleftrightarrow n\pm1,
\tag{4}
\]

while a double slip connects

\[
n\longleftrightarrow n\pm2.
\tag{5}
\]

When single slips are admitted, the transition graph is connected: even and
odd winding sectors can interconvert. When odd island charge cancels single
slips while double slips remain, the graph has two components, classified by
fluxoid parity.

Thus charge parity changes more than a numerical rate. At the ideal symmetric
point it changes the connectivity of the admissible state-transition space.
It selects whether the material record has a protected `Z2` sector.

This has a direct Dynamic Unity interpretation:

> A physical subsystem can change another subsystem's record finality by
> selecting its allowed transition class, without writing or learning the
> record's value.

“Finality” remains conditional here. Imperfect path symmetry, quasiparticle
events, higher processes, environmental noise, and finite time all limit the
protection. The result is a selected transition rule under a frozen physical
packet, not global or permanent finality.

# 4. What survives the charge quotient

Equation (2) is periodic. In the integral-charge control, every even charge has
the same symmetric single-slip response and every odd charge has the same
response. Therefore charge parity factors through the response, while total
signed charge does not:

\[
Q\longmapsto Q\bmod 2e
\longmapsto \Gamma_{\rm SPS}
\longmapsto \text{transition graph}.
\tag{6}

Charges `0`, `2e`, and `-2e` are identified by this bridge. No downstream
fluxoid observation can recover their distinction if the only coupling is
equation (2).

This means the Aharonov--Casher bridge cannot preserve the full target of
`HC-DU-223`. It is nevertheless target-sufficient for the narrower source
target `charge parity` when both paths are present and their response rates are
distinct.

The lesson is not that the bridge failed. It selected its own natural quotient.
The error would be demanding full charge after accepting a coupling that
physically responds only to charge modulo `2e`.

# 5. Transition rule is not endpoint record

A transition kernel can depend on charge parity while any one realized output
remains ambiguous. The exact finite control starts in winding zero and uses an
illustrative one-step law supported on:

```text
even charge: {0, -2, -1, +1, +2}
odd charge:  {0, -2, +2}.
```

The supports overlap. Observing a parity-changing endpoint `+/-1` certifies
that single-slip dynamics was active in the frozen ideal model, so it is a
one-sided certificate for the unprotected/even-charge class. Observing `0` or
`+/-2` does not distinguish the classes.

For the uniform-support control, total variation is `2/5` and the optimal
equal-prior one-shot classification error is `3/10`. Those numbers are not a
device prediction; they are an exact witness that different transition laws
need not make a single endpoint sufficient.

Repeated trials, spectroscopy, continuous monitoring, or a controlled pulse
can improve inference. Each adds a process record, instrument, timing contract,
or controller. It does not retroactively turn the uncontrolled endpoint into a
zero-error certificate.

# 6. Coherence and symmetry are parts of the interface

The coupling disappears if the circuit supplies only one path. Setting `b=0`
in equation (1) makes the rate independent of charge parity. Two physical paths
and their coherent recombination are therefore necessary for the
Aharonov--Casher discriminator.

Exact parity protection requires more: `a=b`. If `a` and `b` are both nonzero
but unequal, even and odd charge still produce different rates, so charge
information remains. Yet the odd-charge amplitude no longer vanishes, single
slips reconnect the graph, and fluxoid parity is no longer exact.

This yields a hierarchy:

```text
one path
  -> no charge-parity response

two coherent unequal paths
  -> charge-parity-sensitive transition rates

two coherent equal paths at the odd-charge point
  -> exact destructive interference
  -> single-slip selection rule
  -> fluxoid-parity protection.
```

The path architecture, coherence, and symmetry are not mere implementation
details. They determine which record-level claim is true.

# 7. Time-reversal obstruction to a signed writer

Electric charge is even under time reversal. Persistent current and signed
winding are odd. Let the source quotient be charge parity `P={0,1}` with
trivial time-reversal action, and let the nonzero signed target branches be
`N={-1,+1}` with time reversal `n -> -n`.

Any time-reversal-equivariant deterministic writer `W:P->N` would have to obey

\[
W(p)= -W(p)
\tag{7}
\]

for each `p`. No element of `N` satisfies this equation. Therefore no such
writer exists.

If winding zero is admitted, an equivariant charge-only rule may select zero,
but it still cannot select a nonzero signed branch. A time-odd datum—magnetic
flux bias, current direction, oriented drive, or equivalent physical
reference—is required. Once an orientation `b in {-1,+1}` is added, a map such
as

\[
W(p,b)=b(-1)^p
\tag{8}

is time-reversal equivariant when `b -> -b`.

Equation (8) demonstrates possibility, not autonomous derivation. It exposes
the exact extra datum instead of hiding it inside a “charge-to-flux writer.”

# 8. Primary-source collision

The physical bridge and its qualifications are established in the
superconducting-circuit literature:

1. Friedman and Averin, *Aharonov--Casher-Effect Suppression of Macroscopic
   Tunneling of Magnetic Flux* (2002), derived charge-controlled destructive
   interference of flux tunnelling:
   <https://arxiv.org/abs/cond-mat/0109544>.
2. Pop et al., *Experimental Demonstration of Aharonov--Casher Interference in
   a Josephson Junction Circuit* (2012), measured fluxon interference around
   charged superconducting islands:
   <https://doi.org/10.1103/PhysRevB.85.094503>.
3. Bell et al., *Spectroscopic Evidence of the Aharonov--Casher Effect in a
   Cooper Pair Box* (2016), observed charge-controlled spectral oscillations
   and near-complete suppression of single-fluxon tunnelling at odd electron
   charge: <https://doi.org/10.1103/PhysRevLett.116.107002>.
4. Kalashnikov et al., *Bifluxon: Fluxon-Parity-Protected Superconducting
   Qubit* (2020), used odd island charge and circuit symmetry to preserve
   fluxon parity and demonstrated enhanced lifetime:
   <https://doi.org/10.1103/PRXQuantum.1.010307>.

These sources absorb the physical effect. None is being presented as a new DU
prediction. Dynamic Unity's contribution is the typed location of the effect
inside the source--response--transition-rule--record--certificate chain.

# 9. Relation to prior results

The wave composes three banked boundaries.

- `HC-DU-223`: total electric charge is exactly recoverable from electric Gauss
  flux, but that constraint witness is not a material archive.
- `HC-DU-224`: fluxoid winding is a material record before readout and phase
  slips are its erasure gate.
- `HC-DU-225`: island charge changes the amplitude of that erasure/transition
  mechanism. At the protected point, charge parity changes the connectivity of
  the fluxoid transition graph.

The composition is therefore:

```text
electric charge response
  -> charge-parity quotient
  -> Aharonov--Casher phase
  -> phase-slip selection rule
  -> fluxoid-parity protection.
```

It is not:

```text
exact total electric charge
  -> unique signed fluxoid value with full provenance.
```

This is not a semantic disappointment. It shows the real coupling acts on the
record's admissibility dynamics rather than copying the source value.

# 10. Absorbers, novelty, and grade

The components are absorbed by Aharonov--Casher interference,
charge--phase duality, superconducting-circuit quantization, coherent quantum
phase slips, bifluxon selection rules, protected-qubit engineering, Markov
kernels, binary hypothesis testing, and elementary equivariant no-section
reasoning.

No new circuit effect, charge--flux duality, or prediction is claimed. The
scoped Dynamic Unity result is:

> A source response may physically select a material record's transition graph
> and protection class without selecting its value. In the Aharonov--Casher
> bridge, the selected source quotient is charge parity; exact protection
> additionally requires coherent path symmetry, and time-reversal covariance
> forbids an unbiased deterministic signed writer.

This earns scoped Grade 4 for physical transition-rule selection, exact
factorization/first-leak localization, and the signed-writer obstruction. It
earns no new physics, empirical excess, complete handoff, source issuance,
observer selection, public finality, or Grade-5 remainder.

# 11. North-Star consequence and reopener

The North-Star search should no longer treat every physical interface as a
value-copying map. It must admit at least three distinct source effects:

1. selecting a response value;
2. selecting the material record coordinate; and
3. selecting the record's admissible transition or protection rule.

Known physics now supplies positive controls for all three in partial form.
The unresolved object is their target-preserving composition with provenance.

Reopen only with one of:

1. a physical packet in which a natural source response determines a material
   record value, not merely its transition rule, under a precommitted protocol;
2. a process record that reconstructs charge parity or total charge with a
   declared finite error and preserves causal lineage;
3. an action-derived reason for the coherent two-path symmetry and time-odd
   orientation rather than an engineered setting; or
4. a finite no-refit remainder after the complete source, transition, record,
   access, and consumer packet is frozen.

No candidate is activated by this result alone. Remain `NO_READY_SUCCESSOR`.

# 12. Exact validation

`tests/du_aharonov_casher_charge_fluxoid_transition_rule_probe.py` returns
`13/13`. It verifies:

- symmetric charge-parity interference and full-charge loss;
- connected versus two-component fluxoid transition graphs;
- loss of exact protection under path deletion or asymmetry;
- overlapping one-shot endpoint laws and one-sided certification;
- total-variation and optimal-error controls; and
- the time-reversal no-section plus oriented positive control.

The artifact is
`tests/artifacts/du_aharonov_casher_charge_fluxoid_transition_rule_result.json`.
