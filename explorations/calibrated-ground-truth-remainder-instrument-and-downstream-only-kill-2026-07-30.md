---
title: "Calibrated ground-truth remainder instrument and downstream-only kill"
status: banked_scoped_result
doc_type: exploration_result
created: 2026-07-30
claim_id: HC-DU-167
run_id: RUN-20260730-140913-calibrated-remainder-instrument
evidence_grade: 4
---

# Calibrated ground-truth remainder instrument

## Executive result

The proposed game-world control is useful, but its first conjecture is false.

What remains unreconstructed is not, in general, “the downstream-only part of
the world.” It is exactly the structure that varies inside the equivalence
classes induced by the frozen action--observation interface.

Two smallest controls decide the point:

- a render coordinate is causally downstream-only but becomes exactly
  reconstructible as soon as looking is part of the certified record; and
- a remote collision coordinate is genuinely action-modifiable in the full
  world but remains completely unreconstructible while remote interaction is
  outside the admitted action envelope.

The game world therefore calibrates Dynamic Unity's reconstruction method. It
does not supply a model of physical reality.

Disposition:

```text
CALIBRATED_REMAINDER_INSTRUMENT_BUILT
+ DOWNSTREAM_ONLY_CONJECTURE_KILLED
+ ACTION_OBSERVATION_FIBRE_CRITERION_SELECTED
+ STRUCTURAL_AND_SAMPLING_UNCERTAINTY_SEPARATED
+ DUAL_MESH_BINDING_FAILURE_PRESERVED
+ NO_PHYSICS_REOPENER
+ NO_READY_SUCCESSOR
```

## 1. Why this is a real instrument

A physical reconstruction problem never gives us the complete world state.
That creates a persistent ambiguity: did a method find a real remainder, or
did the investigator omit a relevant record, action, boundary, or source
variable?

A completely specified finite game world removes that ambiguity. We know:

- every world state;
- every admitted action;
- every returned observation;
- every hidden coordinate;
- every pair of worlds the record identifies; and
- every held-out target on which those worlds disagree.

The arena is therefore a calibration standard for the method, in the same
sense that a synthetic signal with known ground truth calibrates an estimator.
The transfer is methodological, not ontological.

## 2. Frozen finite world

Let

\[
W=\{0,1\}^5
\]

with coordinates

\[
w=(r,c_{\rm near},c_{\rm remote},n,s),
\]

where:

- \(r\) is a visible render distinction;
- \(c_{\rm near}\) is a near collision response;
- \(c_{\rm remote}\) is a remote collision state that an admitted remote
  action can read and toggle;
- \(n\) is an NPC navigation-policy distinction; and
- \(s\) is an authority/reconciliation distinction.

For an action envelope \(A\), let

\[
S_A:W\longrightarrow\mathcal Y_A
\]

be the complete ordered action--observation signature. Define

\[
w\sim_Aw'
\quad\Longleftrightarrow\quad
S_A(w)=S_A(w').
\]

The exact structural remainder relative to \(A\) is the variation left inside
the fibres of \(S_A\). A target \(T\) is reconstructible exactly when it is
constant on every such fibre.

## 3. Calibrated remainder theorem

### Theorem

For a finite world class \(W\), frozen action--observation signature \(S_A\),
and target \(T\), the following are equivalent:

1. there exists a decoder \(d\) such that \(T=d\circ S_A\);
2. \(S_A(w)=S_A(w')\) implies \(T(w)=T(w')\); and
3. \(\ker S_A\subseteq\ker T\).

If \(A\subseteq B\) and \(S_B\) retains the complete \(A\)-signature, then
\(\sim_B\) refines \(\sim_A\). Consequently, action or observation enlargement
can only shrink the exact structural remainder inside the unchanged world
class.

### Proof

If \(T=d\circ S_A\), equal signatures have equal targets. Conversely, if
\(T\) is constant on each signature fibre, define \(d(y)\) as the common
target value on \(S_A^{-1}(y)\). This is well-defined on the image of \(S_A\).
The kernel statement is the same condition written as an equivalence
relation. For \(A\subseteq B\), equality of the retained \(B\)-signature
implies equality of its \(A\)-projection, so every \(B\)-fibre lies inside one
\(A\)-fibre.

This is the finite factorization theorem already native to Dynamic Unity.
The new value is calibration: source access makes every fibre and
target-changing twin exactly auditable.

## 4. Exact calibration curve

The 32 worlds give:

| action--observation envelope | equivalence classes | largest fibre | unresolved coordinates |
|---|---:|---:|---|
| near collision only | 2 | 16 | render, remote collision, nav policy, authority |
| plus visual observation | 4 | 8 | remote collision, nav policy, authority |
| plus NPC observation | 8 | 4 | remote collision, authority |
| plus remote interaction | 16 | 2 | authority |
| plus authority conflict | 32 | 1 | none |

The curve is exact. It does not estimate the remainder from samples; it
enumerates it from the known source.

## 5. Downstream-only is not the criterion

The tempting conjecture was:

> The reconstruction remainder is exactly the causally downstream-only
> structure.

It fails in both directions.

### Downstream-only need not remain

The render bit changes the visual observation and receives no update from the
agent. It is downstream-only in this finite causal model. Once `look` is in
the certified action--observation record, however, the render bit is constant
on every fibre. It is reconstructed exactly.

Thus downstream-only is not sufficient for remainder membership.

### Action-coupled structure can remain

The remote collision bit has a genuine admitted intervention in the complete
model: `toggle_remote` reads its prior value and changes its state. Yet before
that action belongs to the observer's envelope, both remote-collision values
occur inside every relevant fibre.

Thus being physically action-coupled somewhere in the full model is not
sufficient for present reconstruction.

The correct criterion is query-relative:

\[
\text{remainder}(A,T)
\quad\text{is determined by}\quad
\ker S_A\not\subseteq\ker T,
\]

not by a context-free causal label attached to the target.

## 6. Samples are not actions

Three repetitions of the same deterministic near-collision query induce
exactly the same partition as one query. More samples can reduce statistical
uncertainty in a noisy implementation. They cannot split worlds whose entire
declared response laws are identical.

This distinguishes:

- **sampling uncertainty:** insufficient observations of a distinguishable
  response law; and
- **structural nonidentifiability:** equality of the complete frozen response
  signature.

Only a new discriminating action, observation, or physical premise can repair
the second.

## 7. The dual-mesh lesson survives

Authenticating a render value does not bind an independently variable
collision value. Two worlds can carry the same signed render coordinate and
opposite collision responses.

This is not a claim that physics has two meshes. It is an exact control for a
general implication failure:

```text
AUTHENTICATED REPRESENTATION
    -/-> ACTION-SURFACE FACTORIZATION
```

A repair must either prove that action response factors through the certified
representation or add a separately formed binding record.

## 8. What the instrument is good for

The calibrated arena can test whether a proposed DU method:

1. returns the correct equivalence fibres when source truth is known;
2. distinguishes insufficient sampling from structural nonidentifiability;
3. detects a target-changing twin rather than reporting a fitted decoder;
4. updates monotonically when the same world class receives more access;
5. notices when a purported “refinement” actually changes the world or
   occurrence contract; and
6. keeps representation provenance separate from action provenance.

Future calibration worlds can add noise, stochastic policies, partial
observability, adaptive experiments, compression, provenance, and multiple
agents. Those are extensions of the instrument, not current scientific
successors.

## 9. Absorption and novelty

The mathematics is absorbed by finite sufficient statistics, controlled
observability, automata minimization and Myhill--Nerode equivalence,
probabilistic bisimulation, POMDP state identification, and active system
identification.

Dynamic Unity's contribution here is not a new equivalence theorem. It is the
typed use of a source-known world to calibrate reconstruction-remainder
claims while preserving record, action, provenance, contract, and transfer
boundaries.

That is useful methodology at scoped Grade 4. It is not new physics.

## 10. North-Star disposition

The run improves DU's instrument stack but does not reopen the parked
physical campaign. Nature does not expose a source file, and the finite
world's action envelope is supplied rather than physically selected.

The implementation-complete physical reopener remains unchanged. The next
physical result must still supply a source-pinned material packet with joined
attempt lineage, hidden-environment scope, retention, provenance, access, and
reset semantics, then test factorization and minimality without refitting.

No scientific successor is selected.

## Reproducibility

Run:

```bash
python3 tests/du_calibrated_remainder_instrument_probe.py --write-artifact
```

The probe enumerates all 32 worlds, computes every fibre in the five nested
action envelopes, verifies the exact calibration curve, checks refinement
monotonicity and repetition invariance, and executes the two
causal-direction counterexamples and dual-mesh control.
