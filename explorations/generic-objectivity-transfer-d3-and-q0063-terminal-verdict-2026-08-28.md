---
title: "D3 generic-objectivity transfer and Q-0063 terminal verdict"
status: banked_result
doc_type: discriminator_execution_and_terminal_verdict
created: 2026-08-28
owner_repo: dynamic-unity
run_id: RUN-20260828-224429-q0063-d3-terminal
campaign: DU-Q0063-DECOHERENCE-NULL-AUDIT-LAYER-CONFRONTATION
claim_id: HC-DU-200
authority: "Joe direct chat, 2026-08-28: Do a big wave go"
claim_grade: >-
  SCOPED GRADE 4 NONIMPLICATION / GENERIC-OBJECTIVITY TRANSFER BOUNDARY /
  STANDARD QUANTUM-INFORMATION CONTENT / NO NEW PHYSICS, MECHANISM,
  PREDICTION, PROVENANCE, FINALITY LAW, OR ONTOLOGY
lane_channel: "Lane 5 primary; Lanes 3, 4, and 7 supporting; CH-COLLIDE, CH-FORMAL"
perspective_scope: regional_public
referent_status: operational
formation_status: disclosure
---

# D3 generic-objectivity transfer and Q-0063 terminal verdict

## 1. Decision returned

The frozen D3 transfer **fails at named assumptions**.

```text
GENERIC_OBJECTIVITY_TRANSFER_FAILS
+ OUTCOME_ACCESS_NOT_FORCED
+ SPECIFIED_ACCESSIBLE_FRAGMENTS_NOT_FORCED
+ FRAGMENT_INDEPENDENCE_NOT_FORCED
+ PLATEAU_AUDIT_CO-VANISHING_NOT_FORCED
+ PHYSICAL_RATE_NOT_SUPPLIED
+ D2_FINITE_SCALE_BOUNDS_VACUOUS
= AUDIT_LAYER_NONVACUOUS_AND_STRONGLY_ABSORBED
```

This is a result about the scope of the absorber. It is not positive evidence
for a new Dynamic Unity mechanism. The positive physical content remains
standard strong-Quantum-Darwinism and Spectrum-Broadcast-Structure physics.

## 2. Frozen question and exact objects

D3 asked whether the Brandão--Piani--Horodecki (BPH) generic-objectivity
theorems and the Qi--Ranard strengthening imply that failure of the D2 audit
conditions vanishes with the same parameter and at the same rate as flattening
of a Quantum-Darwinism mutual-information plateau, uniformly over physically
accessible fragments and at physical scales.

The comparison keeps the objects separate:

| Object | Typed role |
|---|---|
| `Lambda: D(A) -> D(B_1 tensor ... tensor B_n)` | supplied multi-output quantum channel |
| `Lambda_R` | reduced channel to an output region `R` |
| measure-and-prepare approximation | approximate classicality of locally accessible channel information |
| `I(S:F)=H(S)` | raw Quantum-Darwinism plateau condition |
| local distinguishability / Holevo access / zero discord | D2 access audit |
| `I(F_i:F_j | pointer)=0` | strong fragment-independence audit |
| physically accessible fragment class | observer-and-apparatus-selected subset, not a uniform combinatorial count |
| physical rate | time-, Hamiltonian-, coupling-, geometry-, and detector-dependent convergence |

The D2 load-bearing witness is W1 only after adjudication: an exact
finite-time central-spin branching state with `N=2` and `N=4` has
`I(S:F)=H(S)` while perfect local distinguishability fails, S:F discord is
strictly positive, and the accessible Holevo information lies below the
plateau by a finite margin. The W2 independence witness is not used in the
terminal verdict because the adjudication struck it from the declared model
class.

## 3. What the genericity theorems actually establish

### 3.1 Brandão--Piani--Horodecki

BPH Theorem 1 considers an arbitrary finite-dimensional input `A` and an
arbitrary multi-output CPTP map. For at least a `(1-delta)` fraction of the
single output factors, the reduced channel is close in diamond norm to a
measure-and-prepare channel using one POVM independent of the selected output:

```text
||Lambda_j - E_j||_diamond
  <= [27 ln(2) d_A^6 log(d_A) / (n delta^3)]^(1/3).
```

Its Theorem 2 gives the analogous statement for most fixed-size output
subsets. This is a strong generic **objectivity-of-observables** statement.
The paper explicitly states that Theorem 1 says nothing by itself about
objectivity of outcomes. Full outcome availability is introduced later as an
additional guessing-probability assumption.

Primary source: [Brandão, Piani, and Horodecki, *Generic emergence of
classical features in quantum Darwinism*](https://arxiv.org/abs/1310.8640),
Nature Communications 6, 7908 (2015).

### 3.2 Qi--Ranard

Qi--Ranard replaces BPH's growing exceptional fraction with one excluded
"quantum Markov blanket" `Q`. For any fixed output-region size and tolerance,
every region `R` disjoint from `Q` has a reduced channel close to a
measure-and-prepare channel using a common measurement. One stated bound is

```text
|Q| <= 2 d_A^6 ln(d_A) |R| / epsilon^2.
```

The result is substantially stronger about where locally accessible quantum
information can reside. It still permits regions outside `Q` to carry no
information about `A`, leaves the output factorization supplied, and does not
derive a physical observer's accessible region, outcome distinguishability,
record provenance, or a time-dependent formation law. The authors explicitly
list the dynamics that make information locally available and the tightness
and many-body physical scaling of their bounds as future work.

Primary source: [Qi and Ranard, *Emergent classicality in general multipartite
states and channels*](https://arxiv.org/abs/2001.01507), Quantum 5, 555
(2021).

## 4. Transfer matrix

| Frozen seam | Exact theorem reach | Transfer verdict |
|---|---|---|
| Common observable | A common POVM exists for the approximating channels. | **Succeeds**, but only for observable classicality. |
| Outcome access | Prepared states may be indistinguishable; no information need be locally available. | **Fails at outcome/observable seam.** |
| Specified accessible fragments | BPH counts most supplied factors/subsets; Qi--Ranard excludes a selected `Q`. Neither identifies the fragments a physical observer can access. | **Fails at accessible-fragment quantifier.** |
| Fragment independence | Approximate separability or conditional shielding of `A` from `R` does not imply strong conditional independence among the actual record fragments. | **Fails at independence seam.** |
| Provenance | The channel approximation does not identify the occurrence, source, lineage, archive, or reset history represented by the output. | **Silent; no transfer.** |
| Plateau/audit co-vanishing | The bounds depend on dimensions, region sizes, subset counts, and tolerance, not mutual-information plateau flatness or residual system coherence. | **Fails at co-occurrence-rate seam.** |
| Physical rates and scales | No Hamiltonian, interaction time, coupling, geometry, detector bandwidth, or observer-access rate enters the general theorem. | **Fails at rate/scale seam.** |

The failure is not a technicality. BPH proves that locally distributable
information is generically classical in type. D2 asks whether a raw plateau
certifies that a particular accessible fragment actually contains a
distinguishable record. Those are different implications.

## 5. Finite-scale collision with D2

The published bounds do not adjudicate the executed `N=2`--`4` witness.

- For BPH at `d_A=2` and `n=2` or `4`, the displayed diamond-norm upper bound
  is larger than the maximum useful channel-distance scale for every
  nontrivial `delta`; it is quantitatively vacuous there.
- For Qi--Ranard at `d_A=2`, the displayed blanket guarantee is
  `|Q| <= 128 ln(2) |R| / epsilon^2`. For `epsilon <= 1`, the guaranteed
  upper bound already exceeds both finite environments. The theorem may admit
  a smaller optimized blanket for a particular channel, but the general bound
  does not force one.
- Neither bound is a function of the D2 plateau margin, Holevo deficit,
  fragment overlap, or residual coherence. Therefore no theorem-to-witness
  inequality co-vanishes with the plateau in the frozen arena.

This establishes the preregistered D3 branch: **transfer fails at named
assumptions**, including the decisive co-occurrence-rate seam.

## 6. Terminal Q-0063 verdict

The three executed discriminators now compose as follows:

1. **D1:** available time-resolved decoherence data exclude the proposed
   critical-threshold and quorum-jump mechanisms at measured scales. The
   confluence leg remained data-silent; it did not license a new mechanism.
2. **D2:** the strong bookkeeping null is false in the frozen finite arena.
   Raw plateau and independently accessible classical record content are
   empirically different observables. After adjudication, W1 alone carries
   that result; independence and provenance were not established.
3. **D3:** generic-objectivity theorems do not turn D2's accessible-fragment
   audit into an automatic consequence of plateau flatness at physical rates.

The campaign therefore closes with:

> A Quantum-Darwinism mutual-information plateau is not by itself a
> certificate that a specified observer-accessible fragment contains a
> distinguishable classical record. Generic measure-and-prepare structure
> does not repair that implication. An access audit remains logically and
> operationally necessary in the declared class.

This earns **scoped Grade 4** as an exact nonimplication and necessity result:
the stronger accessible-record conclusion requires an additional audit beyond
the raw plateau. It earns **no DU novelty** because strong Quantum Darwinism,
SBS, discord/Holevo decompositions, and generic channel classicality absorb
all physical components.

The campaign establishes no provenance audit, fragment-independence law,
regional finality mechanism, consensus threshold, source issuance, new
dynamics, empirical anomaly, or Grade-5 remainder. `D6` is closed as
superseded by its target mismatch. `D7` is closed unexecuted; a future
confluence experiment would require a new dated two-sided contract rather
than extending this completed campaign.

## 7. North-Star consequence and reopener

The result sharpens the North Star without selecting a successor:

```text
redundant correlation
  != locally accessible classical information
  != provenance-bearing formed record
  != public final record
  != action-enabling fact
```

The Q-0063 line reopens only if a new dated contract supplies one of:

1. a theorem binding plateau flatness to access, independence, and provenance
   uniformly over a physically selected observer-accessible fragment class,
   with a physical convergence rate; or
2. a finite experiment in which a frozen raw plateau and a separately frozen
   audit packet yield a nonabsorbed operational consequence.

Neither the parked GU receiver nor the four-dimensional QFT and infrared
quantum-gravity charters satisfies this reopener. No hardware or provider is
needed or authorized.

## 8. Sources and reproducibility

- Frozen campaign: `decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md`.
- D1 execution: `classicality-transition-functional-form-d1-literature-check-2026-08-03.md`.
- D2 execution and exact witness: `qd-sbs-audit-gap-witness-d2-execution-2026-08-03.md`,
  `../tests/du_qd_sbs_audit_gap_witness_probe.py`, and
  `../tests/artifacts/du_qd_sbs_audit_gap_witness_result.json`.
- Independent adjudication: `wave3-adjudication-d1-d2-2026-08-03.md`.
- BPH primary source: <https://arxiv.org/abs/1310.8640>.
- Qi--Ranard primary source: <https://arxiv.org/abs/2001.01507>.

No numerical fit, simulation, data reanalysis, or external hardware was used
for D3. The exact theorem statements and bounds were reconstructed from the
primary papers; the existing D2 exact probe remains the finite witness.
