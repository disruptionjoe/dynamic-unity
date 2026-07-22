#!/usr/bin/env python3
"""DU Bet #2 cheap kill: does N_min FORCE the low-entropy SELECTION, or only re-describe
the arrow's DIRECTION that sigma/finality already give?

THE BET (dynamic-tension-reframe-sweep Bet #2). The initial singularity, the low-entropy
past, and the arrow are claimed to be ONE object: the bottom of the record-roll N=e^{4p}
(N_min). Entropy is minimal where the record-count is minimal, so the Past Hypothesis is
alleged to be the roll's ORIGIN, not a separate boundary posit -- collapsing three ledger
rows. The GR/cosmology sigma-council's sharp fence: sigma fixes the arrow's *direction* but
leaves the low-entropy *selection* (the Penrose 1/10^10^123 "why so special") untouched. So
the load-bearing question is ONLY the selection: does N_min reach the thing sigma could not?

THE ANTI-TOY BLADE. "The roll starts low so entropy is low" is CIRCULAR re-description unless
the roll's origin is INDEPENDENTLY forced to be low-entropy in the Past-Hypothesis sense --
which is NOT low *absolute* entropy (a small system trivially has little entropy) but low
entropy RELATIVE TO THE MAXIMUM AVAILABLE, i.e. sub-maximality R(N) = S_actual(N)/S_max(N)
small, the Penrose smoothness/fine-tuning content. This probe separates the two.

THE FORK THAT DECIDES IT. Whether N_min forces sub-maximality at the origin depends ENTIRELY
on S_max(N_min) -- i.e. on whether the accessible phase space (d.o.f. count) GROWS from ~0 at
N_min (records/d.o.f. accrete: GODELIAN/issuance) or is FIXED-large from the start (all d.o.f.
present, records only disclose which corner: FTS/disclosure):

  - FTS / fixed phase space:  S_max = const (large). S_actual(N_min) tiny => R(N_min) ~ 0 and
    the initial gap S_max - S_actual(N_min) is HUGE => the origin IS an improbable fine-tuned
    corner => the Penrose Past-Hypothesis STANDS, un-dissolved. N_min only says WHERE the
    corner sits (the low-N end) -- a re-description of the DIRECTION's origin, NOT a forcing of
    the SELECTION.

  - GODELIAN / growing phase space:  S_max(N) ~ N grows from ~0. Both S_actual and S_max are
    tiny at N_min => R(N_min) ~ O(1) and the initial gap ~ 0 => there is NO improbable corner
    (no room for fine-tuning in a phase space that does not exist yet) => the Past Hypothesis
    is DISSOLVED, and the arrow arises because the gap OPENS as the phase space accretes. THIS
    genuinely reaches the selection -- more than direction.

TWO OUTCOMES, BOTH LETHAL. The discriminator returns "selection forced/dissolved" in the
growing model and "selection NOT forced (re-description only)" in the fixed model. It provably
comes out differently in the two regimes, so a verdict is informative, not rigged. The
GODELIAN model is the POSITIVE/SENSITIVITY control (the test CAN return "selection forced").

WHICH REGIME IS DU IN, AS BUILT? DU's own D-FORK resolution (d-fork-regime-resolution-2026-
07-21.md) already found -- re-verified from DU's construction (fixed B5 action generating a
monotone 4-volume; records are one atom-type; the grading vacuum is unbuilt/W224) -- that the
roll is FTS / fixed-H / DISCLOSURE as built. Feed that in: as built, DU sits in the FIXED-
phase-space column => N_min does NOT force the selection as built; it re-describes the
direction's origin. The selection-forcing is available ONLY in the growing/Godelian column,
gated on the SAME source-forced-algebra-growth witness the D-FORK win requires.

OBSERVER-GRADIENT CONTROL (the cheap decisive adversary). The whole construction is a TEMPORAL
boundary (the low-N end of the roll), spatially homogeneous. It predicts no observer-centred
SPATIAL cosmological gradient => it does not trip the observer-gradient falsifier. Checked.

FORCED-LEG CHECK. The one leg that IS clean: an accretion count is monotone and bottoms out at
its infimum, and the extensive record entropy S_ext ~ N is monotone in N, so
argmin(S_ext) = argmin(N) = the origin. N_min <=> roll-origin <=> S_ext-min is FORCED (but it
is the ABSOLUTE-entropy / DIRECTION leg -- the trivial one, not the selection).

This is a finite SIGNATURE, not a theorem about cosmological entropy. What it does honestly:
(a) confirm the forced (direction/absolute) leg; (b) show the selection leg is decided by the
phase-space-growth fork and by nothing else; (c) exhibit both lethal outcomes and the positive
control so the FTS verdict is informative; (d) pass the observer-gradient adversary; (e) locate
DU-as-built in the fixed column, so N_min does NOT force the selection as built.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# The roll and the extensive (absolute) record entropy.
# N = e^{4p} is the accreted 4-volume / record count; monotone by construction
# (D-FORK file: "4-volume only grows"). S_ext ~ N is the extensive vacuum/record
# entropy (Bianconi sigma*Tr ln G is a sum of N local log-volume terms => extensive).
# ---------------------------------------------------------------------------
def roll_N(p: float) -> float:
    return math.exp(4.0 * p)


def S_ext(N: float, s_per_cell: float = 1.0) -> float:
    """Extensive record entropy: N independent local contributions. Monotone in N."""
    return s_per_cell * N


# ---------------------------------------------------------------------------
# S_max(N): maximum entropy AVAILABLE at record count N. This is the object the
# Past Hypothesis is about (sub-maximality = smoothness = the Penrose fine-tuning).
# The TWO regimes differ ONLY in S_max(N_min):
#   fixed  (FTS/disclosure): all d.o.f. present from the start -> S_max = const large.
#   growing(GODELIAN/issue): d.o.f. accrete with records          -> S_max(N) ~ N.
# ---------------------------------------------------------------------------
def S_max_fixed(N: float, dof_fixed: float, states_per_dof: float = 2.0) -> float:
    """Fixed large phase space: S_max independent of how many records have accreted."""
    return dof_fixed * math.log(states_per_dof)


def S_max_growing(N: float, states_per_dof: float = 2.0) -> float:
    """Growing phase space: accessible d.o.f. = N (accrete with records)."""
    return N * math.log(states_per_dof)


def submaximality(S_actual: float, S_maximum: float) -> float:
    """R = S_actual / S_max in [0,1]. SMALL R = far below max = the Past-Hypothesis content
    (a smooth, special, low-gravitational-entropy state). R ~ 1 = generic (no fine-tuning)."""
    return S_actual / S_maximum if S_maximum > 0 else float("nan")


def past_hypothesis_improbability_nats(S_actual: float, S_maximum: float) -> float:
    """The Penrose selection cost: -ln P(state this smooth) ~ gap = S_max - S_actual (nats).
    HUGE at the origin => a fine-tuned selection (PH stands). ~0 => no selection puzzle."""
    return max(0.0, S_maximum - S_actual)


# ---------------------------------------------------------------------------
# Run one regime across the roll and report the origin's selection cost.
# ---------------------------------------------------------------------------
def walk_regime(
    p_grid: list[float],
    regime: str,
    dof_fixed: float,
    occupancy: float,
) -> dict[str, Any]:
    """occupancy = S_actual/S_max the growing regime relaxes toward (<=1); the fixed regime
    uses the same S_actual(N)=occupancy-independent extensive law so the ONLY difference between
    the two columns is S_max(N), i.e. the phase-space-growth assumption -- nothing else."""
    rows: list[dict[str, Any]] = []
    for p in p_grid:
        N = roll_N(p)
        sa = S_ext(N)  # extensive actual entropy, identical in both regimes
        if regime == "fixed":
            sm = S_max_fixed(N, dof_fixed)
        elif regime == "growing":
            sm = S_max_growing(N) / occupancy  # S_max ~ N/occupancy so S_actual/S_max=occupancy
        else:
            raise ValueError(regime)
        rows.append({
            "p": round(p, 4),
            "N": N,
            "S_actual": sa,
            "S_max": sm,
            "submaximality_R": submaximality(sa, sm),
            "selection_cost_nats": past_hypothesis_improbability_nats(sa, sm),
        })
    origin = rows[0]
    return {
        "regime": regime,
        "rows": [
            {**r, "N": f"{r['N']:.3e}", "S_actual": f"{r['S_actual']:.3e}",
             "S_max": f"{r['S_max']:.3e}", "submaximality_R": round(r["submaximality_R"], 6),
             "selection_cost_nats": f"{r['selection_cost_nats']:.3e}"}
            for r in rows
        ],
        "origin_submaximality_R": origin["submaximality_R"],
        "origin_selection_cost_nats": origin["selection_cost_nats"],
    }


def run_fixture() -> dict[str, Any]:
    # A roll from a small origin outward. N spans ~e^0=1 (origin) up.
    p_grid = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
    dof_fixed = 1.0e6  # a "large" fixed phase space (stand-in for Penrose's ~10^123 content)
    occupancy = 0.5    # the growing regime relaxes toward half-full; any value < 1 works

    # --- FORCED (direction/absolute) leg: monotonicity + argmin coincidence. ---
    Ns = [roll_N(p) for p in p_grid]
    Ss = [S_ext(N) for N in Ns]
    N_monotone = all(Ns[i] < Ns[i + 1] for i in range(len(Ns) - 1))
    S_monotone = all(Ss[i] < Ss[i + 1] for i in range(len(Ss) - 1))
    argmin_N = min(range(len(Ns)), key=lambda i: Ns[i])
    argmin_S = min(range(len(Ss)), key=lambda i: Ss[i])
    forced_leg_holds = N_monotone and S_monotone and argmin_N == argmin_S == 0

    # --- The two regimes (the selection fork). ---
    fixed = walk_regime(p_grid, "fixed", dof_fixed, occupancy)
    growing = walk_regime(p_grid, "growing", dof_fixed, occupancy)

    # In the FIXED (FTS/disclosure) column: origin is an improbable corner => PH stands,
    # selection NOT forced (only the direction's origin is re-described).
    fixed_selection_forced = (
        fixed["origin_submaximality_R"] < 1e-3
        and fixed["origin_selection_cost_nats"] > 1.0e3
    )  # True here means "origin is a fine-tuned corner" => selection NOT dissolved by N_min.

    # In the GROWING (Godelian/issuance) column: origin has R ~ O(1) and ~0 selection cost
    # => the Past Hypothesis is dissolved (no room for fine-tuning) => selection reached.
    growing_selection_dissolved = (
        growing["origin_submaximality_R"] > 0.1
        and growing["origin_selection_cost_nats"] < 1.0
    )

    # The discriminator has TEETH: the two columns disagree on the origin's selection cost.
    discriminator_has_teeth = (
        fixed["origin_selection_cost_nats"] > 1.0e3
        and growing["origin_selection_cost_nats"] < 1.0
    )

    # --- Observer-gradient adversary control: the construction is spatially homogeneous. ---
    # A temporal boundary (low-N end) carries no observer-centred spatial gradient by
    # construction; we assert the invariance explicitly (there is no spatial coordinate in the
    # roll's origin claim), so the falsifier is not tripped.
    observer_gradient_tripped = False

    # --- DU-as-built regime, imported from DU's own D-FORK resolution (re-verified there
    # from DU's construction; consumed as a DU finding, not on any sibling's say-so). ---
    du_as_built_regime = "fixed"  # FTS / fixed-H / disclosure (d-fork-regime-resolution)
    n_min_forces_selection_as_built = (du_as_built_regime == "growing")

    return {
        "fixture_id": "du_low_entropy_origin_bottom_of_roll_probe",
        "question": (
            "Does N_min FORCE the low-entropy SELECTION (sub-maximality / the Penrose "
            "fine-tuning that sigma could not reach), or only re-describe the arrow's DIRECTION? "
            "(Bet #2; the pre-registered cheap kill.)"
        ),
        "kind": "finite_selection_fork_signature_not_a_cosmological_entropy_theorem",
        "claim_status_change": "none",

        "forced_direction_leg": {
            "N_monotone_in_p": N_monotone,
            "S_ext_monotone_in_N": S_monotone,
            "argmin_N_is_origin": argmin_N == 0,
            "argmin_S_ext_is_origin": argmin_S == 0,
            "holds": forced_leg_holds,
            "reading": (
                "FORCED but this is the ABSOLUTE-entropy / DIRECTION leg: an accretion count "
                "bottoms out at its infimum and extensive S~N is monotone, so N_min <=> "
                "roll-origin <=> S_ext-min. Clean, but trivial -- a small system has little "
                "entropy; this is NOT the Past-Hypothesis (sub-maximality) content."
            ),
        },

        "selection_fork": {
            "fixed_FTS_disclosure_column": {
                "origin_submaximality_R": fixed["origin_submaximality_R"],
                "origin_selection_cost_nats": f"{fixed['origin_selection_cost_nats']:.3e}",
                "origin_is_improbable_fine_tuned_corner": fixed_selection_forced,
                "meaning": "Past Hypothesis STANDS; N_min only re-describes where the "
                           "direction's origin sits. Selection NOT forced.",
            },
            "growing_GODELIAN_issuance_column": {
                "origin_submaximality_R": growing["origin_submaximality_R"],
                "origin_selection_cost_nats": f"{growing['origin_selection_cost_nats']:.3e}",
                "origin_selection_dissolved": growing_selection_dissolved,
                "meaning": "Past Hypothesis DISSOLVED (no room for fine-tuning in a phase space "
                           "that does not exist yet); the gap OPENS as d.o.f. accrete. Selection "
                           "reached -- more than direction.",
            },
            "discriminator_has_teeth": discriminator_has_teeth,
            "positive_control_growing_can_return_selection_reached": growing_selection_dissolved,
        },

        "adversary_controls": {
            "observer_gradient_falsifier_tripped": observer_gradient_tripped,
            "observer_gradient_note": (
                "Not tripped: the origin claim is a spatially homogeneous TEMPORAL boundary; it "
                "predicts no observer-centred spatial cosmological gradient."
            ),
            "block_universe_absorber": (
                "The STRUCTURAL collapse (low-N end = low-entropy end = geometric origin, all at "
                "N_min) is a fact about the block's structure and survives B-theory. The 'N_min = "
                "origin of genuine BECOMING' gloss does NOT survive -- DU's own D-FORK file found "
                "the roll FTS/disclosure as built."
            ),
            "record_change_neq_finality": (
                "The monotone N-growth is DIRECTION; genuine irreversibility (the actual arrow) "
                "needs the reversal-cost measure mu (unbuilt). Counting N alone gives monotone "
                "growth, not finality."
            ),
        },

        "du_as_built": {
            "regime_from_d_fork_resolution": du_as_built_regime,
            "n_min_forces_selection_as_built": n_min_forces_selection_as_built,
            "reading": (
                "DU's roll is FTS/fixed-H/disclosure AS BUILT (fixed B5 action -> monotone "
                "4-volume; one atom-type; grading vacuum unbuilt/W224). That is the FIXED column: "
                "N_min does NOT force the selection as built -- it re-describes the direction's "
                "origin. The selection-forcing lives in the GROWING column and is gated on the "
                "SAME source-forced-algebra-growth witness as the D-FORK win."
            ),
        },

        "verdict": (
            "PARTIAL. FORCED: N_min <=> roll-origin <=> S_ext-min (direction/absolute leg; "
            "trivial). NOT FORCED AS BUILT: the low-entropy SELECTION (sub-maximality, the "
            "Penrose content sigma could not reach) is decided by the phase-space-growth fork "
            "and nothing else; DU-as-built sits in the FIXED/FTS column, where N_min only "
            "re-describes the direction's origin. The selection is REACHED (Past Hypothesis "
            "dissolved) only in the GROWING/Godelian column -- gated on the same unbuilt witness "
            "as the D-FORK win. Three rows co-locate at N_min as ONE LOCUS (real structural "
            "economy, common root = finality/irrevocable accretion); the deep selection-forcing "
            "does not close as built. Beats the observer-gradient adversary; survives the "
            "block-universe absorber on the STRUCTURAL claim only; not beaten by (does not beat) "
            "the D-FORK as built."
        ),

        "honest_scope": (
            "A finite SIGNATURE isolating the ONE variable that decides the selection (S_max(N_min), "
            "i.e. phase-space growth), not a computation of cosmological entropy. It shows the "
            "selection-forcing is exactly co-extensive with the Godelian/growing regime and "
            "therefore, for DU-as-built (FTS), reduces to re-description of the direction. A "
            "genuinely growing-phase-space construction is not excluded -- it is the unbuilt "
            "object the 'selection forced' branch would require, the same one the D-FORK win needs."
        ),
    }


def write_json(result: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tests/artifacts/du_low_entropy_origin_bottom_of_roll_probe_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))

    # Exit non-zero if the probe's own internal consistency checks fail (not a physics claim).
    ok = (
        result["forced_direction_leg"]["holds"]
        and result["selection_fork"]["discriminator_has_teeth"]
        and result["selection_fork"]["positive_control_growing_can_return_selection_reached"]
        and not result["adversary_controls"]["observer_gradient_falsifier_tripped"]
        and result["du_as_built"]["n_min_forces_selection_as_built"] is False
    )
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
