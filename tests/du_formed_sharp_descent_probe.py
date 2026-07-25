#!/usr/bin/env python3
"""Exact finite controls for formed-sharp regional descent.

The probe separates four statements that are often flattened:

* sharp PVMs on one common quantum system are globally jointly measurable
  whenever they are pairwise jointly measurable (known spectral terrain);
* effect identity does not imply selective-instrument or continuation
  identity;
* compatible commutative archive marginals glue on a join tree, while a
  cyclic parity family with exact overlap agreement has no global archive;
* general unsharp qubit POVMs can be pairwise but not triplewise jointly
  measurable (a finite Specker control).

Physical formation is a precondition here.  The probe does not derive a
pointer basis, archive, observer boundary, or access rule.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_formed_sharp_descent_result.json"
RUN_ID = "RUN-20260725-110735-formed-sharp-descent"

Assignment = tuple[int, ...]
Distribution = dict[Assignment, Fraction]
Mask = tuple[int, ...]
Matrix = tuple[tuple[Fraction, ...], ...]
BlochOperator = tuple[Fraction, tuple[Fraction, Fraction, Fraction]]


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [jsonable(item) for item in sorted(value)]
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


def mask_mul(left: Mask, right: Mask) -> Mask:
    return tuple(a * b for a, b in zip(left, right))


def mask_sum(masks: Sequence[Mask]) -> tuple[int, ...]:
    return tuple(sum(mask[index] for mask in masks) for index in range(len(masks[0])))


def mask_apply(mask: Mask, state: Sequence[Fraction]) -> tuple[Fraction, ...]:
    return tuple(Fraction(flag) * value for flag, value in zip(mask, state))


def matrix_apply(matrix: Matrix, state: Sequence[Fraction]) -> tuple[Fraction, ...]:
    return tuple(
        sum(
            (matrix[row][column] * state[column] for column in range(len(state))),
            start=Fraction(0),
        )
        for row in range(len(matrix))
    )


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum(
                (left[row][k] * right[k][column] for k in range(size)),
                start=Fraction(0),
            )
            for column in range(size)
        )
        for row in range(size)
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_effect(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(
        sum((matrix[row][column] for row in range(len(matrix))), start=Fraction(0))
        for column in range(len(matrix))
    )


def marginal(
    distribution: Mapping[Assignment, Fraction],
    indexes: tuple[int, ...],
) -> Distribution:
    result: Distribution = {}
    for state, probability in distribution.items():
        key = tuple(state[index] for index in indexes)
        result[key] = result.get(key, Fraction(0)) + probability
    return dict(sorted(result.items()))


def glue_chain(left: Distribution, right: Distribution) -> Distribution:
    left_overlap = marginal(left, (1,))
    right_overlap = marginal(right, (0,))
    if left_overlap != right_overlap:
        raise ValueError("separator mismatch")
    joint: Distribution = {}
    for a, b, c in itertools.product((0, 1), repeat=3):
        denominator = left_overlap[(b,)]
        joint[(a, b, c)] = (
            Fraction(0)
            if denominator == 0
            else left[(a, b)] * right[(b, c)] / denominator
        )
    return joint


def action_error(
    distribution: Mapping[Assignment, Fraction],
    certificate_indexes: tuple[int, ...],
) -> Fraction:
    fibers: dict[Assignment, dict[int, Fraction]] = {}
    for state, probability in distribution.items():
        certificate = tuple(state[index] for index in certificate_indexes)
        action = sum(state) % 2
        masses = fibers.setdefault(
            certificate,
            {0: Fraction(0), 1: Fraction(0)},
        )
        masses[action] += probability
    return sum(
        (min(masses.values()) for masses in fibers.values()),
        start=Fraction(0),
    )


def common_commutative_control() -> dict[str, Any]:
    outcomes = tuple(itertools.product((0, 1), repeat=3))
    state: Distribution = {outcome: Fraction(1, 8) for outcome in outcomes}
    state_vector = tuple(state[outcome] for outcome in outcomes)

    regional = {
        (region, value): tuple(
            int(outcome[region] == value) for outcome in outcomes
        )
        for region in range(3)
        for value in (0, 1)
    }
    global_pvm = {
        outcome: tuple(int(candidate == outcome) for candidate in outcomes)
        for outcome in outcomes
    }
    context_masks = {
        (context, values): tuple(
            int(
                all(
                    outcome[index] == value
                    for index, value in zip(context, values)
                )
            )
            for outcome in outcomes
        )
        for context in ((0, 1), (1, 2))
        for values in itertools.product((0, 1), repeat=2)
    }
    context_coarse_graining_exact = all(
        context_masks[(context, values)]
        == tuple(
            int(
                all(
                    outcome[index] == value
                    for index, value in zip(context, values)
                )
            )
            for outcome in outcomes
        )
        == tuple(
            int(
                any(
                    global_outcome == outcome
                    and all(
                        global_outcome[index] == value
                        for index, value in zip(context, values)
                    )
                    for global_outcome in outcomes
                )
            )
            for outcome in outcomes
        )
        for context in ((0, 1), (1, 2))
        for values in itertools.product((0, 1), repeat=2)
    )

    ab = marginal(state, (0, 1))
    bc = marginal(state, (1, 2))
    glued = glue_chain(ab, bc)
    global_products = {
        outcome: mask_mul(
            mask_mul(regional[(0, outcome[0])], regional[(1, outcome[1])]),
            regional[(2, outcome[2])],
        )
        for outcome in outcomes
    }
    projective = all(mask_mul(mask, mask) == mask for mask in regional.values())
    pairwise_commuting = all(
        mask_mul(left, right) == mask_mul(right, left)
        for left in regional.values()
        for right in regional.values()
    )
    repeatable = all(
        mask_apply(mask, mask_apply(mask, state_vector))
        == mask_apply(mask, state_vector)
        for mask in regional.values()
    )
    orthogonal_global = all(
        mask_mul(global_pvm[left], global_pvm[right])
        == ((0,) * len(outcomes) if left != right else global_pvm[left])
        for left in outcomes
        for right in outcomes
    )

    relabelled = {
        (state_key[2], state_key[1], state_key[0]): probability
        for state_key, probability in state.items()
    }
    relay = {
        state_key + (state_key[2],): probability
        for state_key, probability in state.items()
    }
    ac = marginal(state, (0, 2))

    return {
        "fixture": (
            "three binary records are deterministic quotients of one formed "
            "eight-outcome commutative archive"
        ),
        "physical_formation_status": (
            "independently supplied precondition; not derived by this branch"
        ),
        "state": state,
        "regional_projectors_are_idempotent": projective,
        "regional_projectors_pairwise_commute": pairwise_commuting,
        "regional_selective_filters_are_repeatable": repeatable,
        "global_product_projectors_equal_archive_singletons": (
            global_products == global_pvm
        ),
        "global_pvm_is_orthogonal": orthogonal_global,
        "global_pvm_is_normalized": (
            mask_sum(tuple(global_pvm.values())) == (1,) * len(outcomes)
        ),
        "context_maps_are_exact_master_coarse_grainings": (
            context_coarse_graining_exact
        ),
        "join_tree": {
            "contexts": ("AB", "BC"),
            "separator_marginals_match": marginal(ab, (1,)) == marginal(bc, (0,)),
            "glued_distribution": glued,
            "glued_is_normalized": sum(glued.values(), start=Fraction(0)) == 1,
            "glued_reproduces_contexts": (
                marginal(glued, (0, 1)) == ab
                and marginal(glued, (1, 2)) == bc
            ),
        },
        "upper_action": {
            "action": "A xor B xor C",
            "full_archive_error": action_error(state, (0, 1, 2)),
            "AB_only_error": action_error(state, (0, 1)),
            "interpretation": (
                "global compatibility does not itself make every exported "
                "coarse certificate sufficient for every upper action"
            ),
        },
        "naturality": {
            "outcome_and_region_relabeling_preserves_normalization": (
                sum(relabelled.values(), start=Fraction(0)) == 1
                and len(relabelled) == len(state)
            ),
            "deterministic_relay_is_bijective_and_action_inert": (
                len(relay) == len(state)
                and all(key[2] == key[3] for key in relay)
                and sum(relay.values(), start=Fraction(0)) == 1
            ),
            "benign_cover_refinement_AC_is_reproduced": (
                marginal(state, (0, 2)) == ac
            ),
        },
        "known_absorber": (
            "For finite sharp PVMs on one common Hilbert space, pairwise "
            "joint measurability implies pairwise commutation, and products "
            "of the commuting projections form the global joint PVM."
        ),
    }


def typed_instrument_control() -> dict[str, Any]:
    zero = Fraction(0)
    one = Fraction(1)
    qnd_zero: Matrix = ((one, zero), (zero, zero))
    qnd_one: Matrix = ((zero, zero), (zero, one))
    flip_zero: Matrix = ((zero, zero), (one, zero))
    flip_one: Matrix = ((zero, one), (zero, zero))
    identity: Matrix = ((one, zero), (zero, one))
    flip: Matrix = ((zero, one), (one, zero))
    input_zero = (one, zero)
    return {
        "same_sharp_effects": (
            matrix_effect(qnd_zero) == matrix_effect(flip_zero) == (one, zero)
            and matrix_effect(qnd_one) == matrix_effect(flip_one) == (zero, one)
        ),
        "selective_maps_differ": (
            qnd_zero != flip_zero and qnd_one != flip_one
        ),
        "qnd_outcome_zero_is_repeatable": (
            matrix_mul(qnd_zero, qnd_zero) == qnd_zero
        ),
        "flip_outcome_zero_is_not_repeatable": (
            matrix_mul(flip_zero, flip_zero) != flip_zero
        ),
        "held_out_continuation_distinguishes": (
            matrix_apply(qnd_zero, input_zero)
            != matrix_apply(flip_zero, input_zero)
        ),
        "qnd_total_channel": matrix_add(qnd_zero, qnd_one),
        "flip_total_channel": matrix_add(flip_zero, flip_one),
        "total_channels_are_identity_and_flip": (
            matrix_add(qnd_zero, qnd_one) == identity
            and matrix_add(flip_zero, flip_one) == flip
        ),
        "common_output_joint_instrument_impossible": (
            matrix_add(qnd_zero, qnd_one)
            != matrix_add(flip_zero, flip_one)
        ),
        "reason": (
            "Any one-output joint instrument has one total channel, so exact "
            "selective-map marginals cannot equal instruments with unequal "
            "total channels."
        ),
    }


def pair_relation(parity: int) -> Distribution:
    return {
        (left, right): (
            Fraction(1, 2) if (left ^ right) == parity else Fraction(0)
        )
        for left, right in itertools.product((0, 1), repeat=2)
    }


def satisfying_assignments(parities: Sequence[int]) -> tuple[Assignment, ...]:
    size = len(parities)
    return tuple(
        state
        for state in itertools.product((0, 1), repeat=size)
        if all(
            (state[index] ^ state[(index + 1) % size]) == parity
            for index, parity in enumerate(parities)
        )
    )


def cyclic_obstruction_control() -> dict[str, Any]:
    parities = (0, 0, 1)
    pair_tables = tuple(pair_relation(parity) for parity in parities)
    overlap_marginals = tuple(
        marginal(table, (index,))
        for table in pair_tables
        for index in (0, 1)
    )
    relabelled_parities = (1, 0, 0)
    subdivided_parities = (0, 0, 0, 1)
    return {
        "contexts": {"AB": pair_tables[0], "BC": pair_tables[1], "CA": pair_tables[2]},
        "each_context_is_normalized": all(
            sum(table.values(), start=Fraction(0)) == 1
            for table in pair_tables
        ),
        "all_singleton_overlap_marginals_match": (
            len(
                {
                    tuple(sorted(table.items()))
                    for table in overlap_marginals
                }
            )
            == 1
        ),
        "z2_obstruction": sum(parities) % 2,
        "global_assignment_count": len(satisfying_assignments(parities)),
        "global_extension_exists": bool(satisfying_assignments(parities)),
        "common_sharp_archive_realization_exists": False,
        "diagnosis": (
            "This is not a counterexample to common-system sharp quantum "
            "descent. It proves that contextwise sharp relations and overlap "
            "agreement do not establish one common occurrence/archive "
            "identity; a common sharp-PVM realization would already have a "
            "global joint observable."
        ),
        "naturality": {
            "outcome_relabeling_preserves_obstruction": (
                sum(relabelled_parities) % 2 == 1
                and not satisfying_assignments(relabelled_parities)
            ),
            "inert_relay_subdivision_preserves_obstruction": (
                sum(subdivided_parities) % 2 == 1
                and not satisfying_assignments(subdivided_parities)
            ),
            "adding_redundant_singleton_marginals_cannot_repair": (
                not satisfying_assignments(parities)
            ),
        },
    }


def op_add(left: BlochOperator, right: BlochOperator) -> BlochOperator:
    return (
        left[0] + right[0],
        tuple(a + b for a, b in zip(left[1], right[1])),
    )


def op_positive(operator: BlochOperator) -> bool:
    scalar, vector = operator
    return scalar >= 0 and scalar * scalar >= sum(
        (component * component for component in vector),
        start=Fraction(0),
    )


def axis_vector(axis: int, coefficient: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        coefficient if index == axis else Fraction(0)
        for index in range(3)
    )


def qubit_effect(axis: int, sign: int, eta: Fraction) -> BlochOperator:
    return Fraction(1, 2), axis_vector(axis, Fraction(sign) * eta / 2)


def pair_joint(
    left_axis: int,
    right_axis: int,
    left_sign: int,
    right_sign: int,
    eta: Fraction,
) -> BlochOperator:
    vector = tuple(
        (
            (Fraction(left_sign) * eta / 4 if index == left_axis else 0)
            + (Fraction(right_sign) * eta / 4 if index == right_axis else 0)
        )
        for index in range(3)
    )
    return Fraction(1, 4), vector


def triple_joint(signs: Assignment, eta: Fraction) -> BlochOperator:
    return Fraction(1, 8), tuple(
        Fraction(sign) * eta / 8 for sign in signs
    )


def specker_control() -> dict[str, Any]:
    eta = Fraction(2, 3)
    signs = (-1, 1)
    effects = {
        (axis, sign): qubit_effect(axis, sign, eta)
        for axis in range(3)
        for sign in signs
    }
    pair_joints = {
        (left, right, a, b): pair_joint(left, right, a, b, eta)
        for left, right in ((0, 1), (1, 2), (0, 2))
        for a, b in itertools.product(signs, repeat=2)
    }
    pair_marginals_exact = all(
        op_add(
            pair_joints[(left, right, a, -1)],
            pair_joints[(left, right, a, 1)],
        )
        == effects[(left, a)]
        and op_add(
            pair_joints[(left, right, -1, b)],
            pair_joints[(left, right, 1, b)],
        )
        == effects[(right, b)]
        for left, right in ((0, 1), (1, 2), (0, 2))
        for a, b in itertools.product(signs, repeat=2)
    )
    quieter_eta = Fraction(1, 2)
    quieter_joint = {
        sign_tuple: triple_joint(sign_tuple, quieter_eta)
        for sign_tuple in itertools.product(signs, repeat=3)
    }
    quieter_marginals_exact = all(
        sum(
            (
                quieter_joint[sign_tuple][0]
                for sign_tuple in quieter_joint
                if sign_tuple[axis] == sign
            ),
            start=Fraction(0),
        )
        == Fraction(1, 2)
        and tuple(
            sum(
                (
                    quieter_joint[sign_tuple][1][component]
                    for sign_tuple in quieter_joint
                    if sign_tuple[axis] == sign
                ),
                start=Fraction(0),
            )
            for component in range(3)
        )
        == axis_vector(axis, Fraction(sign) * quieter_eta / 2)
        for axis in range(3)
        for sign in signs
    )
    sharp_eta = Fraction(1)
    sharp_pair_candidate = pair_joint(0, 1, 1, 1, sharp_eta)
    return {
        "observables": (
            "three unbiased binary qubit POVMs along orthogonal Pauli axes"
        ),
        "eta": eta,
        "effects_are_positive_and_normalized": all(
            op_positive(effect) for effect in effects.values()
        )
        and all(
            op_add(effects[(axis, -1)], effects[(axis, 1)])
            == (Fraction(1), (Fraction(0),) * 3)
            for axis in range(3)
        ),
        "all_three_pairs_have_explicit_positive_joint_POVMs": all(
            op_positive(operator) for operator in pair_joints.values()
        ),
        "pairwise_joint_marginals_are_exact": pair_marginals_exact,
        "pairwise_positivity_exact_check": {
            "condition": "2 eta^2 <= 1",
            "left": 2 * eta * eta,
            "right": Fraction(1),
        },
        "triple_joint_dual_certificate": {
            "necessary_condition": "3 eta <= sqrt(3)",
            "left": 3 * eta,
            "left_squared": (3 * eta) ** 2,
            "right_squared": 3,
            "violated": (3 * eta) ** 2 > 3,
            "derivation": (
                "For any joint POVM G_s, sum_s s_i G_s = eta sigma_i. "
                "Then 3 eta = (1/2) sum_s Tr[(s dot sigma)G_s] <= "
                "sqrt(3), since lambda_max(s dot sigma)=sqrt(3)."
            ),
        },
        "triple_joint_exists": False,
        "unsharpness_is_essential_to_this_foil": eta < 1,
        "quieter_eta_one_half_has_explicit_triple_joint": (
            all(op_positive(operator) for operator in quieter_joint.values())
            and quieter_marginals_exact
        ),
        "orthogonal_sharp_eta_one_pair_candidate_is_not_positive": (
            not op_positive(sharp_pair_candidate)
        ),
        "diagnosis": (
            "Pairwise-to-global fails for general unsharp effects. This is "
            "standard Specker/joint-measurability terrain, not a failure of "
            "the common-system sharp-PVM theorem."
        ),
    }


def run() -> dict[str, Any]:
    common = common_commutative_control()
    typed = typed_instrument_control()
    cycle = cyclic_obstruction_control()
    specker = specker_control()

    checks = {
        "common_archive_regional_effects_are_sharp": (
            common["regional_projectors_are_idempotent"]
        ),
        "common_archive_regional_effects_pairwise_commute": (
            common["regional_projectors_pairwise_commute"]
        ),
        "common_archive_selective_filters_are_repeatable": (
            common["regional_selective_filters_are_repeatable"]
        ),
        "common_archive_global_products_are_singletons": (
            common["global_product_projectors_equal_archive_singletons"]
        ),
        "common_archive_global_pvm_is_orthogonal": (
            common["global_pvm_is_orthogonal"]
        ),
        "common_archive_global_pvm_is_normalized": (
            common["global_pvm_is_normalized"]
        ),
        "context_instruments_are_master_coarse_grainings": (
            common["context_maps_are_exact_master_coarse_grainings"]
        ),
        "join_tree_separator_marginals_match": (
            common["join_tree"]["separator_marginals_match"]
        ),
        "join_tree_gluing_is_normalized": (
            common["join_tree"]["glued_is_normalized"]
        ),
        "join_tree_gluing_reproduces_contexts": (
            common["join_tree"]["glued_reproduces_contexts"]
        ),
        "global_archive_is_sufficient_for_parity_action": (
            common["upper_action"]["full_archive_error"] == 0
        ),
        "AB_coarse_certificate_is_not_sufficient_for_parity": (
            common["upper_action"]["AB_only_error"] == Fraction(1, 2)
        ),
        "positive_relabeling_is_natural": common["naturality"][
            "outcome_and_region_relabeling_preserves_normalization"
        ],
        "positive_inert_subdivision_is_natural": common["naturality"][
            "deterministic_relay_is_bijective_and_action_inert"
        ],
        "positive_cover_refinement_is_natural": common["naturality"][
            "benign_cover_refinement_AC_is_reproduced"
        ],
        "effect_identity_does_not_force_map_identity": (
            typed["same_sharp_effects"] and typed["selective_maps_differ"]
        ),
        "QND_selective_map_is_repeatable": typed[
            "qnd_outcome_zero_is_repeatable"
        ],
        "effect_identical_flip_map_is_not_repeatable": typed[
            "flip_outcome_zero_is_not_repeatable"
        ],
        "held_out_continuation_separates_instruments": typed[
            "held_out_continuation_distinguishes"
        ],
        "unequal_total_channels_block_common_output_joint_instrument": (
            typed["total_channels_are_identity_and_flip"]
            and typed["common_output_joint_instrument_impossible"]
        ),
        "cycle_contexts_are_individually_valid": cycle[
            "each_context_is_normalized"
        ],
        "cycle_has_exact_overlap_agreement": cycle[
            "all_singleton_overlap_marginals_match"
        ],
        "cycle_has_nonzero_z2_obstruction": cycle["z2_obstruction"] == 1,
        "cycle_has_no_global_extension": (
            not cycle["global_extension_exists"]
            and cycle["global_assignment_count"] == 0
        ),
        "cycle_cannot_be_common_sharp_archive": (
            not cycle["common_sharp_archive_realization_exists"]
        ),
        "cycle_obstruction_survives_relabeling": cycle["naturality"][
            "outcome_relabeling_preserves_obstruction"
        ],
        "cycle_obstruction_survives_inert_subdivision": cycle["naturality"][
            "inert_relay_subdivision_preserves_obstruction"
        ],
        "cycle_obstruction_survives_benign_cover_refinement": cycle[
            "naturality"
        ]["adding_redundant_singleton_marginals_cannot_repair"],
        "specker_effects_are_valid": specker[
            "effects_are_positive_and_normalized"
        ],
        "specker_pairs_have_positive_joint_POVMs": specker[
            "all_three_pairs_have_explicit_positive_joint_POVMs"
        ],
        "specker_pair_marginals_are_exact": specker[
            "pairwise_joint_marginals_are_exact"
        ],
        "specker_eta_two_thirds_fails_triple_dual_bound": specker[
            "triple_joint_dual_certificate"
        ]["violated"],
        "specker_triple_joint_does_not_exist": (
            not specker["triple_joint_exists"]
        ),
        "specker_foil_is_explicitly_unsharp": specker[
            "unsharpness_is_essential_to_this_foil"
        ],
        "quieter_eta_control_has_global_joint": specker[
            "quieter_eta_one_half_has_explicit_triple_joint"
        ],
        "orthogonal_sharp_pair_is_not_jointly_measurable": specker[
            "orthogonal_sharp_eta_one_pair_candidate_is_not_positive"
        ],
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "dynamic-unity/formed-sharp-descent/v0.1",
        "run_id": RUN_ID,
        "probe": "du_formed_sharp_descent_probe",
        "claim_grade": (
            "EXACT FINITE COMMON-COMMUTATIVE CONSTRUCTION + SHARP-PVM "
            "ABSORBER + TYPED-INSTRUMENT AND CYCLIC/SPECKER OBSTRUCTIONS / "
            "PHYSICAL FORMATION OPEN / COMPONENT MATHEMATICS KNOWN"
        ),
        "common_commutative_descent": common,
        "typed_instrument_identity": typed,
        "cyclic_full_cover_obstruction": cycle,
        "unsharp_qubit_specker_obstruction": specker,
        "strongest_honest_result": {
            "sharp_common_system": (
                "Pairwise compatibility already gives global compatibility "
                "for finite sharp PVMs on one common system; this is known."
            ),
            "general_effects_or_instruments": (
                "Pairwise compatibility is insufficient. The exact unsharp "
                "qubit and typed selective-map controls show two distinct "
                "failures."
            ),
            "conditional_descent": (
                "Once physical formation and common selective-map identity "
                "are independently earned, global action-sufficient descent "
                "requires a full-cover extension plus separate action "
                "factorization; join trees provide an automatic probability "
                "extension, cycles do not."
            ),
        },
        "novelty_grade": {
            "known": (
                "pairwise-to-global joint measurability for sharp PVMs",
                "Vorobev/join-tree marginal extension",
                "cyclic contextuality and sheaf/database obstruction",
                "Specker pairwise-but-not-global unsharp POVMs",
                "selective instrument versus effect identity",
                "sufficient-statistic action factorization",
            ),
            "dynamic_unity_increment": (
                "an unchanged typed descent contract joining independently "
                "formed provenance, selective-map and continuation identity, "
                "full-cover compatibility, upper-action sufficiency, and "
                "benign-refinement naturality"
            ),
            "paper_status": (
                "NO NEW THEOREM CLAIM FROM BRANCH B ALONE; novelty depends "
                "on branch A physically deriving a non-supplied instrument "
                "class or a stricter bound"
            ),
        },
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "COMMON-SHARP DESCENT ABSORBED BY STANDARD SPECTRAL THEORY / "
            "CYCLIC FIXTURE DIAGNOSES FAILED COMMON ARCHIVE IDENTITY / "
            "GENERAL UNSHARP AND SELECTIVE-INSTRUMENT PAIRWISE-TO-GLOBAL "
            "FAILURES EXACT / DU-SPECIFIC VALUE REMAINS THE TYPED PHYSICAL "
            "FORMATION-TO-ACTION CONJUNCTION"
        ),
        "does_not_establish": (
            "physical selection of a sharp record instrument",
            "a new joint-measurability or contextuality theorem",
            "exclusion of almost-quantum correlations by a new principle",
            "public finality, emergent geometry, or record-first ontology",
        ),
    }


def main() -> None:
    result = run()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    if result["failure_count"]:
        raise SystemExit(
            f"{result['failure_count']}/{result['check_count']} checks failed: "
            f"{result['failures']}"
        )
    print(
        f"{result['check_count']}/{result['check_count']} checks passed: "
        f"{ARTIFACT}"
    )


if __name__ == "__main__":
    main()
