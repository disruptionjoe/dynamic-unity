---
title: "Holonomy-to-handoff return map, faithful action, and soldering boundary"
status: banked_scoped_composition_theorem_and_distinct_target_obstruction
doc_type: exact_composition_theorem_counterexample_and_type_refinement
created: 2026-09-01
claim_id: HC-DU-220
run_id: RUN-20260901-holonomy-to-handoff-return-map-and-soldering-boundary
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

This wave composes two banked Dynamic Unity results without identifying their
objects by notation:

- `HC-DU-207`: a signed physical action selects a gauge orbit and its `Z2`
  loop holonomy, but not an observer, material record, consumer, or ruler;
- `HC-DU-219`: autonomous writer--record--consumer dynamics forms a stable
  matched handoff, but stability and spectrum leave an anchored end-to-end
  parity free.

The composition produces a real positive theorem and a sharp remaining
obstruction:

```text
HOLONOMY_SELECTS_SAME_FIBRE_RETURN_PARITY
+ DISTINCT_TARGET_REQUIRES_SOLDERING
+ FAITHFUL_IDENTITY_PRESERVING_Z2_ACTION_IS_UNIQUE
+ UNTYPED_ALIGNMENT_HAS_NO_CANONICAL_SECTION
+ HANDOFF_PARITY_DERIVED_ONLY_AFTER_FIBRE_IDENTITY_OR_SOLDERING
+ MATERIAL_RECORD_INTERFACE_STILL_UNSELECTED
+ NO_READY_SUCCESSOR
```

In plain language:

> If information is transported around a physical loop and returns to the
> same carrier, the loop holonomy already determines whether it returns with
> the same or opposite sign. There is no further parity choice. But if the
> result is handed to a different physical system with its own independent
> sign convention, holonomy alone does not say how the two systems are
> aligned. One physical bridge between their fibres is still needed.

This corrects the broadest reading of `HC-DU-219`. The residual bit is not
universal. It disappears for a same-fibre return or for a target carrying an
independently established faithful identity-preserving action of the same
`Z2`. It survives for a genuinely distinct unsoldered target.

The component mathematics is standard principal-bundle/torsor and
representation theory. Dynamic Unity's contribution is the typed composition
and the exact location of the remaining North-Star burden. No new physics is
claimed.

# 1. Frozen signed transport

Take the signed four-cycle from `HC-DU-207`, with edge transports

\[
 \sigma_e\in\{-1,+1\}.
\]

At each vertex, a local change of coordinate `eta_v in {+1,-1}` acts by

\[
 \sigma_{uv}\mapsto\eta_u\sigma_{uv}\eta_v.
\tag{1}
\]

The loop product

\[
 W:=\prod_{e\in C_4}\sigma_e
\tag{2}
\]

is gauge invariant. All sixteen edge assignments form two gauge orbits of
eight, classified by `W=+1` and `W=-1`.

The exact question is not whether both `W` and the autonomous handoff parity
`h` happen to use the printed labels `+1` and `-1`. It is whether the physical
types provide a map between them.

# 2. Same-fibre return theorem

Let `F_0` be the binary fibre at a chosen base vertex. Transport a source
state `S in F_0` once around the complete cycle. Successive edge transport
gives

\[
 T
 =\left(\prod_e\sigma_e\right)S
 =WS.
\tag{3}
\]

## Theorem 1 — holonomy derives return parity

For a closed-loop return into the same physical fibre, the end-to-end handoff
parity is exactly

\[
 h=TS^{-1}=W.
\tag{4}
\]

No independent alignment sign is required.

## Proof

Equation (3) is the definition of composed parallel transport. A vertex gauge
change conjugates the return map by the base-fibre coordinate change. In the
abelian `Z2` case the conjugation is trivial, so `W` and the relative parity
`TS^{-1}` are unchanged. Because source and target are two stages of the same
fibre, the identity map at zero transport is already typed; there is no
independent target translation to choose. `square`

This is the exact sense in which holonomy can supply the bit left open by
`HC-DU-219`. The answer is structural rather than numerical: the output is a
return map on the same carrier.

# 3. Autonomous handoff transfer

Insert (4) into the binary autonomous chain. Choose any internal record gauge
`a in {+1,-1}` and derive the consumer sign

\[
 b=aW.
\tag{5}
\]

Then

\[
 ab=W,
\]

and the autonomous corrections

\[
 R\leftarrow aS,
 \qquad
 T\leftarrow bR
\]

converge from every initial `(R,T)` and every asynchronous schedule to

\[
 (R_*,T_*)=(aS,WS).
\tag{6}
\]

Changing `a` relabels the internal record and co-transforms `b`; it changes no
complete response. Unlike the original `HC-DU-219` family, no independent
handoff-parity parameter was added. The loop transport supplied it.

This remains conditional on the signed connection/action. It does not explain
why nature chose that connection or its holonomy.

# 4. Distinct-target soldering obstruction

Now let `Q` be a separate binary target fibre with an independent coordinate
convention. A source-to-target soldering is a bijection

\[
 j_c:F_0\to Q,
 \qquad
 j_c(S)=cS,
 \qquad c\in\{-1,+1\}.
\tag{7}
\]

There are exactly two such bijections. The induced target response is

\[
 T=j_c(WS)=cWS,
 \qquad
 h=cW.
\tag{8}
\]

An independent target relabeling `T -> -T` exchanges `j_+` and `j_-`. It fixes
neither.

## Theorem 2 — no canonical unsoldered cross-target handoff

If the antecedent admits the independent target relabeling and supplies no
source-target soldering, no equivariant selector can choose one of the two
bijections in (7). For either loop holonomy, the admissible target parity set
remains

\[
 \{-1,+1\}.
\tag{9}
\]

## Proof

The target relabeling belongs to the antecedent's stabilizer and acts freely
on the two candidate bijections. The stabilizer fixed-point set is empty.
`HC-DU-207`'s fixed-point necessity criterion therefore forbids a covariant
unique selector. Direct enumeration gives the same result. `square`

This is not merely a naming problem when `Q` is a physically distinct system.
The missing `j` is the physical rule saying how a source orientation acts on
the target carrier. Calling both fibres `Z2` does not install that rule.

# 5. Typed group repair

The obstruction changes if the fibres are not merely unpointed two-element
torsors. Suppose they are physically typed multiplicative `Z2` groups and the
bridge must be a group homomorphism.

There are exactly two homomorphisms

\[
 f:\mathbb Z_2\to\mathbb Z_2:
\]

1. the trivial map, sending both elements to the identity; and
2. the identity/sign map, sending the nontrivial element to the nontrivial
   element.

Only the second is faithful. Therefore:

## Theorem 3 — unique faithful identity-preserving action

An identity-preserving, faithful `Z2` action on a physically pointed binary
target is unique. It sends

\[
 +1\mapsto+1,
 \qquad
 -1\mapsto-1.
\tag{10}
\]

The alternative bijection `f(W)=-W` is not a group homomorphism because it
sends the identity to the nonidentity. Equivalently, it makes trivial
holonomy flip the target and violates the preregistered no-effect condition.

Thus a physical law can close the parity gap without a separately fitted sign
if it independently establishes all three premises:

1. source holonomy and target response are actions of the same typed group;
2. trivial holonomy acts trivially; and
3. the target response is faithful rather than blind to holonomy.

Those premises must be fixed before the target data. They are exactly what an
unpointed target torsor lacks.

# 6. The geometry of the remaining gap

The result distinguishes three cases that earlier DU language could blur:

| Physical arrangement | What transport selects | Remaining burden |
|---|---|---|
| Closed loop, return to the same fibre | Holonomy and end-to-end parity | No extra parity; still no record/archive |
| Same bundle, distinct point, physically fixed path | Connection transport along that path | Path/route and endpoint access must be physical |
| Distinct independently relabelable target system | Nothing beyond an orbit of two alignments | Select a soldering/intertwiner or target representation |

“Soldering” is used here in the general typed sense of a physical
identification or intertwiner between carriers. This theorem does not identify
it with a tetrad, GU's `shiab`, a detector calibration, or any other particular
geometric object.

The North-Star search is therefore narrower than “find a selector bit.” Ask:

> Are the record and consumer stages returns or transports inside one
> physically selected bundle, or are they distinct systems whose carriers need
> an independently selected intertwiner?

That question can often be answered from the architecture before any large
simulation or experiment.

# 7. What the composition does not select

Even the positive same-fibre theorem supplies only a response relation. It
does not produce:

- a blank physical archive;
- a write event and causal provenance;
- retention or reset semantics;
- an observer access route;
- a downstream action/resource contract;
- public certification or regional finality; or
- a locked target that distinguishes a physical remainder.

A loop-return variable can be response-visible without being a record. The
complete handoff gate from `HC-DU-218` remains intact.

# 8. Grade, novelty, and absorbers

The wave earns scoped Grade 4 for:

1. exact composition of the `HC-DU-207` holonomy and `HC-DU-219` autonomous
   handoff models;
2. a same-fibre positive derivation of handoff parity;
3. an exact distinct-target no-section/soldering obstruction;
4. the unique faithful identity-preserving `Z2` action repair; and
5. a sharper type-level North-Star reopener.

The component results are absorbed by standard holonomy, torsor,
representation, gauge, signed-graph, and equivariant-selector mathematics.
The work establishes no physical `Z2` substrate, GU bridge, empirical excess,
new field equation, material record interface, source issuance, finite
remainder, or new physics.

# 9. Exact reopener

Do not add another bare sign-coupling toy. Reopen only with a physical
candidate that declares whether its handoff is:

1. a same-fibre return;
2. same-bundle transport along a physically selected path; or
3. an inter-system transfer with a candidate soldering/intertwiner.

For case 3, require the action to derive or dynamically select the bridge,
survive deletion and independent target relabeling, and preserve a locked
held-out response without refit. A complete record claim must additionally
supply the material archive, provenance, access, consumer, reset, and resource
packet.

No current DU candidate clears those obligations, so the portfolio remains
`no_ready`.

# 10. Reproduction

Run:

```bash
python3 tests/du_holonomy_handoff_soldering_boundary_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_holonomy_handoff_soldering_boundary_result.json` and reports
`15/15` checks.
