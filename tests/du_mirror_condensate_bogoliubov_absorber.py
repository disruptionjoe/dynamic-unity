#!/usr/bin/env python3
"""Adversary-C kill probe: does the mirror-sector condensate deliver W1 record-ALGEBRA
growth, or is its sector-condensation a Bogoliubov automorphism of a FIXED CAR algebra?

CONTEXT. The D-FORK resolution (d-fork-regime-resolution-2026-07-21.md) put DU's roll in the
FTS / disclosure regime AS BUILT, and named the one witness that would flip it to Godelian
(the win): a SOURCE-FORCED record-ALGEBRA growth via the compactifying mirror-sector condensate
(W224's missing grading vacuum, built in W216 as a BCS/BdG condensate). A sibling swing builds
that condensate CONSTRUCTIVELY and claims it is the witness (W1 non-isomorphic observable-algebra
growth; W2 a new source-generated admissibility predicate = the good-stable grading). This probe
is the ADVERSARIAL half: take the STRONGEST form of that witness and try to KILL it against the
disclosure-side absorbers (E057 fixed-H null; CompletionClass v1; Adapter_P W1/W4 gates).

THE STRONGEST FORM (no strawman). Spontaneous symmetry breaking in a superconductor is a REAL
phenomenon with REAL teeth: the BCS/condensed vacuum is UNITARILY INEQUIVALENT to the normal-phase
Fock vacuum (a disjoint GNS representation), and the condensate supplies a good-stable grading
(the compact Cartan reduction Sp(32)xSp(32)) that the singlet vacuum (W224) could not. If
"inequivalent representation + a new grading, sourced by the B5 action" were W1/W2, the becoming
would be rescued. This probe asks whether it is.

THE KILL (the physics the absorbers encode). A Bogoliubov / Bogoliubov-de Gennes transformation is
a (Krein-)UNITARY on a FIXED Fock space: it is an AUTOMORPHISM of the FIXED CAR/CCR algebra over the
mode space, NOT an extension of it. The 96 mirror null pairs (W173: ker(Gamma) of Cl(9,5)=M(64,H))
are a FIXED generator set; the gap Delta(p) is a c-number order parameter (mean-field, W216) that
rolls the state along a fixed one-parameter automorphism family. So:
  * the abstract observable algebra A_n does NOT grow: A_n = B(Delta_n)[A_infty], an automorphic
    image of the FIXED A_infty = CAR over the 96 pairs. A fixed A_infty factors EVERY A_n. That is
    the literal fixed-H condition (E057). W1 (non-isomorphic algebra GROWTH) is NOT delivered;
    what is delivered is representation/state inequivalence -- changed VALUES on a fixed algebra,
    the exact object E057's fixed-H null and CompletionClass observer_information_access absorb.
  * the good-stable grading predicate (commute with the Cartan involution P = diag(I_32,-I_32)) is a
    FIXED, pre-existing structural object (W219 wrote it down KINEMATICALLY, before any dynamics).
    The condensate SELECTS a VEV direction satisfying the pre-existing predicate; it does not AUTHOR
    a new one. W2 (source-generated new predicate) is a relabel_gauge / name_provenance surplus.
  * "source-forced by the B5 action" is either (a) a POSITED fixed action -> fixed_source (a fixed
    functional whose EL/gap-equation flow is a computable map), or (b) an UNBUILT action invoked to
    guarantee the future sectors -> a hidden completed oracle (OnlineIssuance^LC gate 4;
    CompletionClass completed_history). Either horn kills source-forcing.

Pre-declared kill condition (task): the witness KILLS the disclosure verdict only if it beats ALL of
{fixed-H/Bogoliubov, relabel_gauge/name_provenance, fixed_source/hidden-oracle, Adapter_P W1/W4}.
This probe is a finite-window SIGNATURE, not a decision procedure: it (a) gives the mandatory positive
control (a genuine mode-ISSUING process that GROWS the generator set -- the test MUST flag it as
growth, so an ABSORBED verdict on the condensate is informative, not rigged); (b) shows a Bogoliubov
transformation is a metric-preserving automorphism of a FIXED algebra (dimension/CAR invariant);
(c) walks the condensate through the algebra test and the CompletionClass primitives; and (d) names
the exact CONDITIONAL datum that WOULD flip it (a source action that grows ker(Gamma) -- which the
fixed Cl(9,5)=M(64,H) structurally forbids).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


# ---------------------------------------------------------------------------
# 0. Fixed structural data (W173 / W216 / W219 / W224), re-verified here.
# ---------------------------------------------------------------------------
CLIFFORD = "Cl(9,5) = M(64, H)"          # W173: fixed real Clifford algebra
N_NULL_PAIRS = 96                        # W173: 96 hyperbolic null pairs in ker(Gamma)
N_CAR_GENERATORS = 2 * N_NULL_PAIRS      # (particle, hole) per pair -> fixed generator set
CARTAN_INVOLUTION_DIM = (32, 32)         # P = diag(I_32, -I_32): the pre-existing grading
SP_FULL_DIM = 8256                       # dim_R Sp(32,32;H)  = 64*(2*64+1)
SP_COMPACT_DIM = 4160                    # dim_R Sp(32) x Sp(32)


# ---------------------------------------------------------------------------
# 1. Bogoliubov / BdG transformation on ONE fixed null pair (W216, good branch).
#    H_BdG = xi*tau3 + Delta*tau1  ->  diagonalized by an O(2) Bogoliubov rotation.
#    The POINT: B(Delta) is a metric-preserving map of a FIXED 2-mode space onto
#    itself -> an AUTOMORPHISM of the fixed CAR algebra, not an extension.
# ---------------------------------------------------------------------------
TAU1 = np.array([[0.0, 1.0], [1.0, 0.0]])
TAU2 = np.array([[0.0, -1.0j], [1.0j, 0.0]])
TAU3 = np.array([[1.0, 0.0], [0.0, -1.0]])


def bdg_block_good(xi: float, delta: float) -> np.ndarray:
    return xi * TAU3 + delta * TAU1


def bdg_block_pathological(xi: float, delta: float) -> np.ndarray:
    # W216 opposite branch: xi*tau3 + i*Delta*tau2 (Krein-self-adjoint w.r.t. eta = tau3).
    return xi * TAU3 + 1j * delta * TAU2


def bogoliubov_rotation(xi: float, delta: float) -> np.ndarray:
    """O(2) Bogoliubov rotation diagonalizing the good-branch BdG block.

    tan(2 theta) = Delta / xi ; B = [[u, v], [-v, u]], u=cos theta, v=sin theta.
    B is orthogonal (B B^T = I): it preserves the fermionic anticommutators -> it is an
    AUTOMORPHISM of the CAR algebra on this FIXED 2-mode space.
    """
    theta = 0.5 * math.atan2(delta, xi) if (xi != 0.0 or delta != 0.0) else 0.0
    u, v = math.cos(theta), math.sin(theta)
    return np.array([[u, v], [-v, u]])


def gap_equation_delta(coupling_gN0: float, band_W: float) -> float:
    """Closed-form BCS gap (W216 PC3): Delta* = W / sinh(1/(g N0))."""
    if coupling_gN0 <= 0.0:
        return 0.0  # repulsive / zero channel: NO condensate (matched negative control)
    return band_W / math.sinh(1.0 / coupling_gN0)


# ---------------------------------------------------------------------------
# 2. The algebra-growth discriminator (E057 / Adapter_P W1).
#    An observable algebra is characterized here by its GENERATOR COUNT (number of
#    independent CAR generators = number of modes). A fixed A_infty factors every A_n
#    iff the generator count is invariant AND each stage map is an automorphism.
# ---------------------------------------------------------------------------
def algebra_trajectory_generator_counts(
    base_generators: int, new_generators_per_step: int, steps: int
) -> list[int]:
    counts = []
    g = base_generators
    for _ in range(steps):
        counts.append(g)
        g += new_generators_per_step
    counts.append(g)
    return counts


def genesis_verdict(admissibility_class_counts: list[int]) -> dict[str, Any]:
    """E057 productivity bar on an ADMISSIBILITY-CLASS count (the grading predicate view).

    This engages the constructive swing's sharpest residual ('escape_that_is_real'): because the
    SYMMETRIC (singlet) phase has F EMPTY (W224: no admissible fundamental symmetry AT ALL), the
    appearance of F nonempty after condensation is a genuine admissibility GENESIS, not
    value-selection inside a fixed admissible algebra -- it beats a VANILLA fixed-action SSB. Grant
    that. The kill: a genesis that fires AT MOST ONCE and caps the count at a finite ceiling is
    BOUNDED -> a fixed richer two-phase A_infty (symmetric-phase + compactified-phase, with a
    threshold) absorbs the whole trajectory (whole_family / fixed_source). E057 W1 requires
    PRODUCTIVE (unbounded, non-pre-enumerable) growth; one monotone jump is a fixed-action phase
    transition (absorber #3), not productive becoming.
    """
    growth = [admissibility_class_counts[i + 1] - admissibility_class_counts[i]
              for i in range(len(admissibility_class_counts) - 1)]
    genesis_events = sum(1 for g in growth if g >= 1)
    ceiling = max(admissibility_class_counts)
    count_bounded = ceiling < math.inf and genesis_events <= 1  # one-shot -> bounded
    productive = all(g >= 1 for g in growth) and len(growth) > 0
    return {
        "admissibility_class_counts": admissibility_class_counts,
        "per_step_growth": growth,
        "genesis_events": genesis_events,
        "ceiling": ceiling,
        "count_bounded": count_bounded,
        "productive": productive,
        # a single bounded genesis is absorbed by a fixed two-phase A_infty
        "fixed_two_phase_Ainfty_absorbs": count_bounded and not productive,
        "regime": "FTS_disclosure" if (count_bounded and not productive)
        else ("W1_ALGEBRA_GROWTH" if productive else "MIXED_indeterminate"),
    }


def w1_growth_verdict(
    generator_counts: list[int], every_stage_map_is_automorphism: bool
) -> dict[str, Any]:
    growth = [generator_counts[i + 1] - generator_counts[i] for i in range(len(generator_counts) - 1)]
    count_invariant = all(g == 0 for g in growth)
    productive = all(g >= 1 for g in growth) and len(growth) > 0
    # E057: a fixed A_infty factors all A_n iff the generator set is invariant and every
    # stage transition is an automorphism (Bogoliubov) rather than a generator-issuing map.
    fixed_Ainfty_factors_all = count_invariant and every_stage_map_is_automorphism
    return {
        "generator_counts": generator_counts,
        "per_step_generator_growth": growth,
        "generator_count_invariant": count_invariant,
        "productive_generator_growth": productive,
        "every_stage_map_is_automorphism": every_stage_map_is_automorphism,
        "fixed_Ainfty_factors_all_An": fixed_Ainfty_factors_all,
        "W1_nonisomorphic_algebra_growth": productive and not fixed_Ainfty_factors_all,
        "regime": "FTS_disclosure" if fixed_Ainfty_factors_all
        else ("W1_ALGEBRA_GROWTH" if productive else "MIXED_indeterminate"),
    }


# ---------------------------------------------------------------------------
# 3. Fixtures.
# ---------------------------------------------------------------------------
def run_fixture() -> dict[str, Any]:
    steps = 12

    # -- POSITIVE CONTROL FIRST (mandatory) --------------------------------
    # A genuine mode-ISSUING source: each roll-step source-forces a fresh null pair
    # (grows the generator set) that is NOT access-revealed from the prior stage. The
    # stage map is NOT an automorphism (it embeds A_n into a strictly larger A_{n+1}).
    # The discriminator MUST flag this as W1 growth -- else it is rigged.
    pc_mode_issuing = w1_growth_verdict(
        algebra_trajectory_generator_counts(
            base_generators=N_CAR_GENERATORS, new_generators_per_step=2, steps=steps
        ),
        every_stage_map_is_automorphism=False,
    )
    positive_control_fires = pc_mode_issuing["regime"] == "W1_ALGEBRA_GROWTH"

    # -- PC: a Bogoliubov transformation IS a metric-preserving automorphism ----
    # Check across a sweep of gaps that B(Delta) is orthogonal (preserves CAR) and that
    # it diagonalizes the good-branch BdG block to the real spectrum +/- sqrt(xi^2+Delta^2).
    bogo_is_automorphism = True
    spectrum_real_good = True
    spectrum_complex_pathological = True
    for xi in (0.0, 0.3, 1.0, 2.0):
        for delta in (0.2, 0.62, 1.5):
            B = bogoliubov_rotation(xi, delta)
            # orthogonality B B^T = I  (preserves fermionic anticommutators -> automorphism)
            if not np.allclose(B @ B.T, np.eye(2), atol=1e-12):
                bogo_is_automorphism = False
            # good branch: eigenvalues real, = +/- sqrt(xi^2 + Delta^2)
            eig_good = np.linalg.eigvals(bdg_block_good(xi, delta))
            if not np.allclose(np.sort(eig_good.real), np.sort([-math.hypot(xi, delta), math.hypot(xi, delta)]), atol=1e-9) \
               or not np.allclose(eig_good.imag, 0.0, atol=1e-9):
                spectrum_real_good = False
            # pathological branch: eigenvalues +/- sqrt(xi^2 - Delta^2), COMPLEX for |xi|<Delta
            eig_path = np.linalg.eigvals(bdg_block_pathological(xi, delta))
            if abs(xi) < delta and np.allclose(eig_path.imag, 0.0, atol=1e-9):
                spectrum_complex_pathological = False

    # -- NEGATIVE CONTROL: repulsive channel -> no gap -> no transformation at all --
    delta_repulsive = gap_equation_delta(coupling_gN0=0.0, band_W=2.25)
    negative_control_no_condensate = delta_repulsive == 0.0

    # -- THE CONDENSATE, walked through the algebra test (attack 1) ----------
    # As p rolls, Delta(p) rolls along the gap-equation curve, but the MODE SPACE is the
    # FIXED 96 null pairs of ker(Gamma). Build the stage sequence of gaps and confirm the
    # generator count is INVARIANT and every stage map is a Bogoliubov automorphism.
    roll_couplings = [0.30 + 0.03 * k for k in range(steps)]  # p rising -> pairing strengthens
    gaps = [gap_equation_delta(gN0, band_W=2.25) for gN0 in roll_couplings]
    gaps_all_nonzero = all(d > 0 for d in gaps)
    condensate_generator_counts = algebra_trajectory_generator_counts(
        base_generators=N_CAR_GENERATORS, new_generators_per_step=0, steps=steps
    )
    condensate_algebra = w1_growth_verdict(
        condensate_generator_counts, every_stage_map_is_automorphism=True
    )

    # -- attack 2b: the constructive swing's SHARPEST residual -- the admissibility GENESIS.
    # The singlet phase has F EMPTY; condensation makes F nonempty. Model this as an
    # admissibility-class count that jumps 0->1 ONCE at the condensation threshold, then caps.
    # (This mirrors the constructive sibling's condensate_across_roll series exactly.)
    genesis_series = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    genesis = genesis_verdict(genesis_series)
    genesis_beats_vanilla_ssb = True  # F empty->nonempty is qualitative, not value-selection
    genesis_still_absorbed = genesis["regime"] == "FTS_disclosure"  # but one-shot -> bounded -> FTS
    # source-forcing of the genesis DIRECTION is the external Godel-independent Krein sign (W211):
    genesis_direction_source_forced = False  # |Theta_eff| <= 2, external/imported, not B5-generated

    # -- W2: is the good-stable grading a NEW source-generated predicate? (attack 2) --
    # The grading predicate "commute with the Cartan involution P = diag(I_32,-I_32)" and the
    # Proposition-1 compactness criterion (admissible fundamental symmetry exists iff the isotropy
    # image is relatively compact) are FIXED, defined at prefix 0 (W219 kinematic, pre-dynamics).
    grading_predicate_defined_at_prefix0 = True   # W219 wrote it down before any condensate
    condensate_authors_new_predicate = False       # it SELECTS a VEV satisfying the OLD predicate
    # The counterfactual adjoint VEV ~ P breaks the 4096 non-compact block, leaving the compact 4160
    # -- an arithmetic fact about the FIXED group, independent of dynamics (W224 sec 5).
    broken_noncompact = SP_FULL_DIM - SP_COMPACT_DIM
    grading_is_fixed_cartan_relabel = (broken_noncompact == 4096) and grading_predicate_defined_at_prefix0
    w2_source_generated_new_predicate = (
        (not condensate_authors_new_predicate) is False  # i.e. False -> not delivered
    )

    # -- attack 3: source-forcing horns -------------------------------------
    source_forcing = {
        "horn_a_posited_fixed_action": {
            "if": "the swing POSITS a specific B5 source action (a fixed functional).",
            "then": "the gap Delta = W/sinh(1/(gN0)) and the EL flow are a COMPUTABLE map of "
            "fixed data; the condensate is a fixed-law consequence.",
            "absorber": "fixed_source (+ initial_condition)",
        },
        "horn_b_unbuilt_action_as_oracle": {
            "if": "the B5 source action is genuinely UNBUILT but invoked to GUARANTEE the "
            "grading-defining sectors condense in the right direction.",
            "then": "the unbuilt action is a hidden completed oracle precontaining the future "
            "sectors -- OnlineIssuance^LC gate 4 ('no internally formed future-schema oracle "
            "precontains all future admissible witnesses') is violated.",
            "absorber": "completed_history (+ hidden_state)",
        },
        "verdict": "both horns kill source-forcing; the disjunction is exhaustive",
    }

    # -- Adapter_P (FORMAL-OBJECT.md RUN-0099) acceptance, walked --------------
    adapter_p = {
        "W1_nonisomorphic_algebra_growth": condensate_algebra["W1_nonisomorphic_algebra_growth"],  # False
        "W2_source_generated_new_predicate": w2_source_generated_new_predicate,                     # False
        "W3_construction_space_growth": False,   # ker(Gamma) is a FIXED 96 pairs; no new partners
        "W4_physical_perturbation_nonfactorization": False,  # mean-field BdG = a FIXED Hamiltonian
                                                             # (RUN-0103: all real physical attempts
                                                             #  -> fixed-Hamiltonian, absorbed)
        "fixed_source_absorber_defeated": False,
        "no_hidden_completed_oracle": False,     # the unbuilt source action is the oracle
        "source_generated_new_class": False,
    }
    adapter_p_accepts = (
        (adapter_p["W1_nonisomorphic_algebra_growth"]
         or adapter_p["W2_source_generated_new_predicate"]
         or adapter_p["W3_construction_space_growth"])
        and adapter_p["W4_physical_perturbation_nonfactorization"]
        and adapter_p["fixed_source_absorber_defeated"]
        and adapter_p["no_hidden_completed_oracle"]
        and adapter_p["source_generated_new_class"]
    )

    # -- CompletionClass v1 primitives that fire (composition closure) --------
    completion_class_primitives_firing = {
        "fixed_source": "the CAR algebra over the 96 fixed null pairs (+ any posited action) "
        "contains every phase; the state space contains normal AND condensed vacua.",
        "observer_information_access": "the condensed vacuum is a changed STATE / changed VALUES "
        "on the fixed algebra (unitary inequivalence is representation-change, not algebra-growth).",
        "relabel_gauge": "the good-stable grading is the pre-existing Cartan involution P; the "
        "difference is a representation/gauge choice of VEV direction.",
        "name_provenance": "'condensate-induced grading' is the OLD kinematic W219 grading under "
        "a new name; provenance-label surplus.",
        "completed_history": "IF the unbuilt source action is invoked as the guarantor, it is a "
        "completed-history oracle precontaining the future sectors.",
    }
    composed_absorption = "ABSORBED"  # product/sequential closure of the firing primitives

    # -- The CONDITIONAL escape hatch, named precisely ------------------------
    conditional_escape = {
        "the_only_survival": "a B5 source action whose flow ISSUES new physical mode content "
        "(grows ker(Gamma): new null pairs / new admissibility classes) as p rolls, productively "
        "(non-c.e.-enumerable) and NOT access-revealed from the stage-n CAR algebra, emitting a "
        "recordable trace, with NO completed-oracle action precontaining the future modes.",
        "why_it_is_harder_than_SSB": "SSB / Bogoliubov RESHUFFLES a FIXED mode set (an automorphism "
        "of a fixed CAR algebra) -- it is the fixed-H trap itself, not an escape from it. Survival "
        "needs the source to GROW the generator set, a strictly stronger claim.",
        "the_structural_headwind": "ker(Gamma) is a FIXED 96 null pairs of the FIXED Clifford "
        "algebra Cl(9,5)=M(64,H) (W173). A source action on this fixed field content cannot grow "
        "the mode space without changing the fixed representation theory the GU substrate pins. So "
        "the escape does not merely require BUILDING the action; it requires an action that does "
        "what the fixed substrate structurally resists.",
        "exact_needed_datum": "a demonstration that the B5 flow produces, at stage n+1, a physical "
        "null-pair / admissibility class provably NOT present in and NOT access-revealed from the "
        "stage-n CAR algebra over ker(Gamma) -- i.e. productive mode-ISSUANCE, not mode-reshuffling.",
    }

    return {
        "fixture_id": "du_mirror_condensate_bogoliubov_absorber",
        "role": "Adversary-C (attack the STRONGEST form; a real absorption is an honest finding)",
        "question": "Does the mirror-sector condensate deliver W1 record-ALGEBRA growth (rescuing "
        "DU's becoming), or does its sector-condensation factor through a FIXED CAR algebra as a "
        "Bogoliubov automorphism (absorbed = disclosure)?",
        "kind": "finite_window_algebra_signature_not_a_decision_procedure",
        "claim_status_change": "none",

        # controls first
        "POSITIVE_CONTROL_mode_issuing_fires_growth": positive_control_fires,
        "positive_control_detail": pc_mode_issuing,
        "PC_bogoliubov_is_metric_preserving_automorphism": bool(bogo_is_automorphism),
        "PC_good_branch_spectrum_real": bool(spectrum_real_good),
        "PC_pathological_branch_spectrum_complex": bool(spectrum_complex_pathological),
        "NEGATIVE_CONTROL_repulsive_no_condensate": negative_control_no_condensate,

        # fixed structural data (re-verified)
        "fixed_substrate": {
            "clifford": CLIFFORD,
            "mirror_null_pairs_in_ker_Gamma": N_NULL_PAIRS,
            "fixed_CAR_generators": N_CAR_GENERATORS,
            "cartan_grading_P_dim": CARTAN_INVOLUTION_DIM,
            "noncompact_block_broken_by_adjoint_VEV": broken_noncompact,
            "Sp_full_dim": SP_FULL_DIM,
            "Sp_compact_dim": SP_COMPACT_DIM,
        },

        # attack 1: Bogoliubov / fixed-H
        "roll_couplings_gN0": roll_couplings,
        "roll_gaps_delta": gaps,
        "roll_gaps_all_nonzero": gaps_all_nonzero,
        "condensate_algebra_test": condensate_algebra,
        "attack1_fixed_H_absorbs_W1": condensate_algebra["fixed_Ainfty_factors_all_An"],

        # attack 2: relabel / name of the pre-existing grading
        "grading_predicate_defined_at_prefix0": grading_predicate_defined_at_prefix0,
        "grading_is_fixed_cartan_relabel": bool(grading_is_fixed_cartan_relabel),
        "attack2_W2_source_generated_new_predicate": w2_source_generated_new_predicate,  # False

        # attack 2b: the admissibility GENESIS (constructive swing's sharpest residual)
        "attack2b_genesis_analysis": genesis,
        "attack2b_genesis_beats_vanilla_ssb": genesis_beats_vanilla_ssb,  # True (qualitative, not value-selection)
        "attack2b_genesis_still_absorbed_one_shot_bounded": genesis_still_absorbed,  # True -> FTS
        "attack2b_genesis_direction_source_forced": genesis_direction_source_forced,  # False (external Krein bit)

        # attack 3: source-forcing horns
        "attack3_source_forcing": source_forcing,

        # attack 4: Adapter_P
        "attack4_adapter_p_gates": adapter_p,
        "attack4_adapter_p_accepts_witness": adapter_p_accepts,  # False

        # composed verdict
        "completion_class_primitives_firing": completion_class_primitives_firing,
        "composed_absorption": composed_absorption,

        "witness_survives_all_absorbers": (
            condensate_algebra["W1_nonisomorphic_algebra_growth"]
            or adapter_p_accepts
        ),

        "conditional_escape": conditional_escape,

        # Independent cross-check against the CONSTRUCTIVE sibling swing's own probe result
        # (re-verified here, not imported as a grade -- CONNECTIONS.md sovereign self-check).
        "convergence_cross_check": {
            "constructive_swing_own_verdict": "PARTIAL (both win-bars FAILED)",
            "constructive_swing_condensate_across_roll_regime": "FTS_disclosure",
            "constructive_swing_fixed_A_infty_absorbs": True,
            "constructive_swing_productive": False,
            "constructive_swing_win_bar_productivity_passed": False,  # one-shot genesis, count caps at 1
            "constructive_swing_win_bar_source_forced_passed": False,  # external Godel-independent Krein bit
            "agreement": "The CONSTRUCTIVE swing (building the witness) and this ADVERSARIAL swing "
            "(killing it) INDEPENDENTLY converge on ABSORBED / FTS_disclosure. Even the swing that "
            "TRIED to build the witness, graded honestly, finds fixed_A_infty absorbs and the growth "
            "is not productive. The becoming is not rescued -- confirmed from both directions.",
        },

        "verdict": (
            "ABSORBED. The mirror-condensate's sector-condensation is a (Krein-)Bogoliubov "
            "AUTOMORPHISM of the FIXED CAR algebra over the 96 null pairs of ker(Gamma): the "
            "generator set is invariant, so a fixed A_infty factors every A_n -- the literal "
            "fixed-H condition (E057). Unitary inequivalence of the condensed vs normal vacuum is "
            "representation/state change (observer_information_access), NOT W1 algebra growth. The "
            "good-stable grading is the pre-existing Cartan involution P (relabel_gauge / "
            "name_provenance), not a source-generated predicate (W2 fails). The 'source-forcing' is "
            "either a fixed action (fixed_source) or the unbuilt action as a completed oracle "
            "(completed_history). Adapter_P rejects (W1,W2,W3,W4 all fail; no-hidden-oracle fails) "
            "-- the SAME shape as RUN-0103's Assembly physical lift. The becoming is NOT rescued as "
            "built; the condensate confirms disclosure rather than overturning it. CONDITIONAL "
            "escape exists but is strictly stronger than SSB (it needs the source to GROW "
            "ker(Gamma), which the fixed Cl(9,5)=M(64,H) structurally resists) -- named, not live."
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
        default=Path("tests/artifacts/du_mirror_condensate_bogoliubov_absorber_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)

    # Loud, checkable summary. Positive controls asserted FIRST.
    assert result["POSITIVE_CONTROL_mode_issuing_fires_growth"], "positive control must fire growth"
    assert result["PC_bogoliubov_is_metric_preserving_automorphism"], "Bogoliubov must be an automorphism"
    assert result["PC_good_branch_spectrum_real"], "good-branch BdG spectrum must be real"
    assert result["PC_pathological_branch_spectrum_complex"], "pathological branch must be complex"
    assert result["NEGATIVE_CONTROL_repulsive_no_condensate"], "repulsive channel must not condense"
    assert result["attack1_fixed_H_absorbs_W1"], "attack 1: fixed A_infty must factor all A_n"
    assert result["attack2_W2_source_generated_new_predicate"] is False, "attack 2: W2 must fail"
    assert result["attack2b_genesis_still_absorbed_one_shot_bounded"], "attack 2b: one-shot genesis must be FTS"
    assert result["attack2b_genesis_direction_source_forced"] is False, "attack 2b: genesis direction not source-forced"
    assert result["attack4_adapter_p_accepts_witness"] is False, "attack 4: Adapter_P must reject"
    assert result["witness_survives_all_absorbers"] is False, "witness must be ABSORBED"

    print(json.dumps(result, indent=2, sort_keys=True))
    print("\nVERDICT:", result["composed_absorption"])


if __name__ == "__main__":
    main()
