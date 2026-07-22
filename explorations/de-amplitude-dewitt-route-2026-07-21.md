---
title: "Lane 1.3 pre-registered swing: can the (9,5)/gimmel DeWitt-fiber measure DERIVE phi = 1/(3 Omega_L)^2 natively, beating the Sorkin import and the de Sitter relabel?"
status: active_research
doc_type: exploration
lane: "1.3 (the native DE amplitude)"
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (Lane 1.3 pre-registered swing; the distinctness-bank attempt)"
posture: "open exploration; native derivation IS the prize here but not the only standard; honesty bites at the banking gate; adversaries are terrain to beat, not gates. Sovereign self-verification: cross-repo material (gu-formalization W145/W146, the gimmel/DeWitt ledger, PRED-NORM-RANK) is INGESTED and RE-VERIFIED here, never adopted on that repo's say-so."
runnable: tests/de_amplitude_dewitt_route_probe.py
probe_exit: "0 (44/44 checks pass; deterministic; numpy + stdlib; ~1 s)"
verdict: "CONFIRMS-IMPORT (with one weak-PARTIAL sliver on the '3'); neither trap beaten; PRED-NORM-RANK / RESOLVED_NO_GO stands"
grade: "exploration / banking-gate honest negative. COMPUTED (deterministic, this swing): the target algebra 1/sqrt(phi)=3 Omega_L; the exact de Sitter identity 1/sqrt(N_4)=pi/S_dS; the actual (9,5)/gimmel DeWitt supermetric built as a 10x10 Gram matrix (signature (6,4), G_GU(g,g)=-4, G_DW(g,g)=-12, ratio 3); the sqrt(N) law surviving any local reweight; the fiber-volume Weyl weight (nonzero); the native factor menu {sqrt2,sqrt7,sqrt13,...} all missing 2.054; the two coincident '3'-functions at d=4. INGESTED + RE-VERIFIED: gu-formalization W145/W146, gimmel-dewitt-normalization-ledger, PRED-NORM-RANK, de-amplitude-audit, lost-predictions-recovery. No canon / claim-status / posture movement; the Krein SIGN is external sigma and was NOT touched."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Lane 1.3 -- the native DE-amplitude swing (DeWitt-fiber route)

**Bottom line up front. The (9,5)/gimmel DeWitt-fiber measure does NOT derive
`phi = 1/(3 Omega_L)^2` natively. It beats neither trap.** The de Sitter relabel
(trap b) is untouched because the fiber measure never enters the magnitude; the
Sorkin `1/sqrt(N)` import (trap a) is untouched because the DeWitt supermetric is
*ultralocal* and therefore *additive*, so a fiber reweight can only rescale `N`
by a constant, not change the `sqrt(N)` law. The one number the fiber would have
to supply -- the amplitude factor `3 Omega_L = 2.054` -- is (i) not a scale
invariant of the measure, (ii) not in the native discrete menu the measure/spectrum
actually offers, and (iii) built on `Omega_L`, a *dynamical, epoch-dependent*
cosmological ratio that no static kinematic measure on `Met(X4)` can output.

**Grade: CONFIRMS-IMPORT** -- the honest negative that keeps PRED-NORM-RANK /
RESOLVED_NO_GO. One weak-PARTIAL sliver is logged (the "3" has a genuine native
echo), but it is a `d=4` coincidence, not a derivation, and it is not the
load-bearing factor. This does not fold Lane 1.3; it *sharpens* it -- Section 8
names the one reopening condition that survives.

Receipt: `tests/de_amplitude_dewitt_route_probe.py`, deterministic, numpy +
stdlib, **run 2026-07-21, exit 0, 44/44 checks pass.** The probe is a
disproof-or-confirm instrument, not a fit: Section 7 of the probe carries
positive controls showing that a *genuine* native factor `= 3 Omega_L` WOULD
register (7.1-7.2) and that the one scale-invariant native route (a same-space
measure ratio) does cancel the Weyl weight (7.3) -- so a "CONFIRMS-IMPORT" here
is a real negative, not a rigged one.

---

## 1. The exact target, restated so the traps are visible

Route (ii) (the causal-set volume-conjugate route,
`gu-formalization/explorations/W146-...`, `W145-...`, recovered in
`lost-predictions-recovery-2026-07-21.md`) reaches the observed dark-energy
magnitude through the ported **Sorkin everpresent law**
`Lambda l_p^2 ~ +/- 1/sqrt(N)`, with `N` = the measured 4-volume in Planck units.
Numerically (re-verified, probe Sec 1):

- `N_4 = (R_H/l_p)^4 = 5.21e243`, `sqrt(N_4) = 7.22e121`;
- **predicted** `Lambda l_p^2 = 1/sqrt(N_4) = 1.385e-122`;
- **observed** `Lambda l_p^2 = 3 Omega_L (l_p/R_H)^2 = 2.845e-122`;
- **residual = observed/predicted = 3 Omega_L = 2.054** (exact, probe 1.6).

To make the match exact you replace `N_4` by a "measured-record count"
`N_meas = phi * N_4`, so `1/sqrt(N_meas) = (1/sqrt(phi)) * 1/sqrt(N_4)`, and
matching forces `1/sqrt(phi) = 3 Omega_L`, i.e.

> **`phi = 1/(3 Omega_L)^2 = 0.237`** (probe 0.2-0.3).

So `phi` and "the amplitude factor `3 Omega_L`" are **one number seen two ways**.
The prize is: does the DeWitt-fiber measure DERIVE that factor? The two traps
that must both fall:

- **Trap (a) -- the imported `1/sqrt(N)` law.** The `sqrt` is Sorkin's Poisson
  number-variance, not GU's. W145 verified the leading term is a pure port.
- **Trap (b) -- the de Sitter relabel.** `1/sqrt(N_4) = pi/S_dS` *exactly* (probe
  2.2), so the magnitude coincides with Gibbons-Hawking `Lambda ~ 1/S_dS`; the
  substrate story earns **no novelty from the magnitude** (W145 sec 0.5, W146 sec 2.3).

A native win requires the DeWitt-fiber measure to supply `3 Omega_L` *and* to do
so in a way that is not just relabeling `S_dS` and not just re-importing Sorkin's
`sqrt`.

## 2. The actual measure (re-verified, not assumed)

From the gimmel/DeWitt normalization ledger
(`gu-formalization/explorations/gimmel-dewitt-normalization-ledger-2026-07-20.md`),
the vertical fiber over `(x,g)` is `W = Sym^2(T*_x X)` (dim 10 for `d=4`), with

```
G_lambda(S,T) = tr(g^-1 S g^-1 T) - lambda tr_g(S) tr_g(T),   tr_g(S) = tr(g^-1 S).
```

`lambda_GU = 1/2` (source-native trace reversal), `lambda_DW = 1` (conventional
DeWitt comparison). I built this as an explicit `10x10` Gram matrix on a
Lorentzian base `g = diag(-1,1,1,1)` (probe Sec 3) and re-verified the ledger:

- pure-trace direction `G_lambda(g,g) = d - lambda d^2`: **`G_GU = -4`, `G_DW = -12`**
  (probe 3.1-3.2), ratio **3** (probe 3.3);
- fiber signature on the Lorentzian locus is **(6,4)** for both `lambda` (probe 3.4),
  so `(3,1)_base + (6,4)_fiber = (9,5)`, `4 + 10 = 14` -- the Y14 decomposition.

This is the real object, not a planted normalization. Everything below is a
property of *this* measure.

## 3. Trap (b) survives: the fiber never enters the magnitude

The magnitude `1/sqrt(N_4) = pi/S_dS` depends on the **4-volume count alone**.
A fiber reweight sends `N_4 -> phi N_4` and hence `Lambda -> (1/sqrt(phi)) Lambda`
-- an O(1) rescaling of an amplitude whose `10^-120` size is *still* the de Sitter
value `pi/S_dS` (probe 2.3, checked for `phi in {0.1, 0.237, 1, 4}`). The fiber
can only touch the O(1) factor, never the `120` orders. This is exactly W146
sec 2.5 part 2 ("the C-operator/fiber is IRRELEVANT to the everpresent
magnitude"), re-derived here from the measure itself. **Trap (b) is not beaten,
and structurally cannot be beaten by a reweight.**

## 4. Trap (a) survives: the DeWitt measure is ultralocal, hence additive

DeWitt's supermetric is **ultralocal** -- a pointwise algebraic form on
`Sym^2(T*_x X)` with no derivative couplings. An ultralocal measure is a
**product measure over base points**, so the record count is **additive** across
cells. Three consequences, all fatal to a native `phi`:

1. **The `sqrt(N)` law is untouched.** A per-cell reweight `phi` gives
   `1/sqrt(phi N) = (1/sqrt(phi)) N^{-1/2}`: the amplitude still scales as
   `N^{-1/2}` (probe 4.1 fits the exponent to `-0.5` across `N in [1e10, 1e243]`).
   The imported Sorkin law is reproduced, not replaced. To *beat* trap (a) you
   would need a **non-additive** count (correlated cells), which requires a
   non-ultralocal, derivative-coupled measure -- which the DeWitt supermetric is
   not, by definition.
2. **`phi` is defined by the target, not derived.** The prefactor the reweight
   introduces is *exactly* `1/sqrt(phi) = 3 Omega_L` (probe 4.2) -- i.e. writing
   `N_meas = phi N_4` is just renaming the residual. Unless something *else* fixes
   `phi` from the measure, this is circular.
3. **Information-geometry reading (the sharpest form).** `Lambda ~ 1/sqrt(N)` is
   the Cramer-Rao / standard-error scaling: Fisher information from `N` independent
   samples adds as `N I_1`, giving estimator error `~ 1/sqrt(N)`. The DeWitt
   metric *is* the natural (Fisher-type) information metric on `Met(X)` -- but
   because it is **ultralocal**, its information is **additive**, which is *precisely*
   what forces the `sqrt(N)` law with a constant prefactor. So the info-geometry
   lens does not rescue the count from additivity; it *explains why* the count is
   additive. Non-additivity would need statistical dependence the ultralocal
   measure does not carry.

## 5. `phi` is not a native invariant (the metrology crux)

The sharpest check the brief asked for: **is `phi` a real invariant, or a
coordinate/relabel artifact that dies under a frame sweep?** It dies.

A "fiber multiplicity per base cell" is a ratio of a **10-dim** fiber volume to a
**4-dim** base volume. The fiber-volume density `sqrt|det G_lambda|` is **not
scale-invariant**: under a Weyl/scale change `g -> alpha g`, each Gram entry
`G_ab ~ alpha^{-2}`, so `det(10x10) ~ alpha^{-20}` (probe 5.1, verified for
`alpha in {2,4,10}`), and the volume density carries **Weyl weight -10** (probe
5.2, nonzero). A nonzero weight means the fiber-to-base ratio depends on the
conformal frame -- it is not a native number. This is exactly the **rank-3
rescaling freedom** PRED-NORM-RANK proved leaves no native absolute value: `phi`
lives in the same free-scale ledger as `mu_DW`, and pinning it requires the
**imported B.5 cut scale** (`de-amplitude-audit-2026-07-20.md` sec 5).

The **one** native route that evades the metrology kill is a **ratio of two
measures on the same 10-dim fiber** (the scale cancels: probe 7.3 shows
`det G_GU / det G_DW = 1/3` is scale-invariant). That is the only scale-invariant
number the measure offers -- but (i) it needs the **interacting C-operator**,
whose existence is **H59-OPEN** (`W145` sec 5, YES-CONJECTURE/gated), so it cannot
be computed at current grade, and (ii) any *fixed* such ratio is a **static
geometric number**, which cannot be the **epoch-dependent** `Omega_L(t)` (probe 7.4).

## 6. `3 Omega_L = 2.054` is not on the native menu, and `Omega_L` is dynamical

Even setting the metrology kill aside, ask directly: does any native invariant
*equal* `3 Omega_L = 2.054`? The native amplitude factors GU actually possesses
(W145's subleading structure) are the **number-variance** `sqrt(c)` for the
`{2,7,13}`-smooth spectrum -- `{1.414, 2.646, 3.606}` -- plus discrete
signature/dimension data. Against `2.054` (probe Sec 6): **none lands within 2%**;
the closest is the naive integer `2` (gap 2.6%) and `sqrt(7) = 2.646` (gap 29%).
The count `c` that *would* be needed is `(3 Omega_L)^2 = 4.219` (probe 6.3) --
**not in `{2,7,13}`** (probe 6.4). Fishing the `{2,7,13}` combinatorics for `4.219`
is exactly the coincidence-hunt the anti-crank discipline forbids; I did not bank it.

The deeper reason it cannot be on any *static* menu: **`Omega_L = rho_L/rho_crit`
is a dynamical, present-epoch cosmological ratio** (the coincidence-problem
quantity; `Omega_L(a): 0 -> 1` over cosmic history). A kinematic measure on
`Met(X4)` is epoch-independent and cannot output today's `0.685`. And the
everpresent law with `N = 4-volume` already forces `Lambda ~ H^2`, i.e.
`Omega_L ~ const`; so committing to a *fixed* native `phi` would predict a
**constant `Omega_L` for all epochs** -- a different, observationally disfavored
physical claim (`Lambda ~ H^2` tracking DE), not the observed value. Either way,
not a native derivation of the number.

**The "3" (the weak-PARTIAL sliver, logged honestly).** The `3` in `3 Omega_L`
is the **Friedmann / critical-density factor** `(d-1)(d-2)/2 = 3` at `d=4` -- a
standard-physics import (it is *how* `Omega_L` is defined from `H_0`). The DeWitt
pure-trace ratio `G_DW/G_GU = 2(1-d)/(2-d)` *also* equals `3` at `d=4` (probe
3.3, 6.5). Tantalizing -- but the two are **different functions of `d`** (they
part ways at `d=3`: `4` vs `1`; and `d=5`: `2.67` vs `6`; probe 6.5c). So the
match is a **`d=4` coincidence, not an identity**; attributing "the 3" to the
DeWitt measure is unjustified. This is the only piece with any native echo, it is
coincidence-grade, and it is not the load-bearing factor (`Omega_L` is).

## 7. Persona council (inline, one worker; lenses, not evidence)

- **Mathematical Physicist.** The construction is honest: the real `10x10`
  supermetric, the `(6,4)` signature, `G(g,g)=d-lambda d^2` all reproduce the
  ledger. The load-bearing structural fact is ultralocality -> additivity ->
  `sqrt(N)` with a constant prefactor. There is no derivative coupling in
  `G_lambda` to make the count non-additive, so trap (a) is closed at the level of
  the measure's *type*, not just this evaluation.
- **Information Geometry.** I was the persona most likely to rescue this: `Lambda
  ~ 1/sqrt(N)` is Fisher/Cramer-Rao-flavored and the DeWitt metric *is* the
  information metric on `Met(X)`. But that cuts the other way -- Fisher information
  is additive over independent samples *because* the metric is ultralocal, which is
  what *produces* the `sqrt(N)` law. The fiber measure is not the lever that makes
  the count non-additive; it is the reason the count is additive. Verdict:
  reinforces CONFIRMS-IMPORT.
- **Metrology / Invariance (the decisive lens).** `phi` as a fiber-to-base ratio
  is **not** a frame invariant -- the fiber volume carries Weyl weight `-10` (probe
  5.2), so `phi` is coordinate/scale data, exactly PRED-NORM-RANK's free scale.
  The only invariant is a same-space measure ratio, which needs the unbuilt
  C-operator and is a *fixed* number, hence cannot be the epoch-dependent
  `Omega_L`. This is the frame sweep the brief asked for, and `phi` fails it.
- **Metabolic Scaling.** For the count to be genuinely sublinear/non-additive
  (the "is `mu` real or absorbed by counting?" question) you need a hierarchical /
  fractal network in the accretion. The ultralocal DeWitt measure has none -- it
  is pointwise, exponent 1, "absorbed by counting." Any non-additivity would have
  to come from the (unbuilt) GLOBAL->REGIONAL->INDIVIDUAL measurement gate, **not**
  the fiber measure. So the measure alone cannot supply it.
- **Cosmologist.** `3 Omega_L` decomposes into a geometric Friedmann `3` and a
  dynamical `Omega_L`. The `3` has a coincidental native echo; `Omega_L` is the
  present value of an evolving quantity and cannot fall out of static geometry.
  A fixed `phi` predicts `Omega_L = const` (tracking DE), disfavored. The route
  as posed cannot yield the observed number without importing the epoch.
- **Anti-crank / Adversary-C (mandatory banking seat).** The strongest form of
  the claim ("the `(9,5)` fiber measure supplies `phi`") is impossible at current
  grade for a structural reason, not a computational gap: the only scale-invariant
  native number is C-operator-gated (H59 open) and is static, while the target is
  frame-dependent-or-dynamical. Do **not** bank the `2 ~ 2.054` near-miss or any
  `{2,7,13}` combination hitting `4.219`; both are coincidence-grade. This is a
  clean negative, correctly graded.

Council synthesis: unanimous **CONFIRMS-IMPORT**. The Information-Geometry and
Metrology lenses -- the two with the best chance of a native win -- both actively
*explain the obstruction* rather than merely failing to find a route.

## 8. Honest outcome, and what survives

**CONFIRMS-IMPORT.** The amplitude genuinely cannot be made native from the
DeWitt-fiber measure at current grade. Both traps stand:

- trap (b): the fiber never enters the `10^-120` magnitude (`= pi/S_dS`);
- trap (a): the ultralocal measure is additive, reproducing Sorkin's `sqrt(N)`
  with only a constant reweight;
- `phi = 1/(3 Omega_L)^2` is not a native invariant (Weyl-weighted), not on the
  native discrete menu (`2.054 notin {sqrt2,sqrt7,sqrt13,...}`; `c=4.219 notin
  {2,7,13}`), and rests on the dynamical `Omega_L`.

This keeps `PRED-NORM-RANK / RESOLVED_NO_GO` intact and does **not** move canon,
claim status, or posture. The **Krein sign** was left untouched throughout: it is
the external `sigma` bit (known-challenge #7), the amplitude was the target, and
the amplitude is what came back import.

**The one reopening condition that survives** (named, not pursued here, so Lane
1.3 does not fold): the *only* scale-invariant native object the measure offers is
a **ratio of two fiber measures on the same 10-dim space** (probe 7.3). If (1) the
**interacting C-operator** is built (retires H59-OPEN), and (2) the promotable /
C-positive fiber measure to total fiber measure ratio is computed and *independently*
found `= 1/(3 Omega_L)^2`, and (3) that identification is shown to be a genuine
**prediction of `Omega_L`** rather than a static number tuned to today's value,
then the route reopens. All three are downstream of the same B5 / C-operator
bottleneck; none is available now. Until then the DE amplitude stays a pure import.

## 9. Boundary

New files only: this exploration and `tests/de_amplitude_dewitt_route_probe.py`.
No existing file edited; nothing committed or pushed (per instruction); nothing
external. Cross-repo material (gu-formalization W145/W146, gimmel/DeWitt ledger,
PRED-NORM-RANK, de-amplitude-audit, lost-predictions-recovery) was **ingested and
re-verified here** under DU's sovereign self-verification rule, consumed as source
and re-checked, never adopted on gu-formalization's say-so. No claim-status,
canon-verdict, LANE-STATE, or public-posture change. This is a banking-gate honest
negative, offered as a PROPOSAL for the lane, not self-banked; it invites hostile
re-verification.
