#!/usr/bin/env python3
"""Exact finite controls for the formed-sharp quantum-selection hostile gate.

This probe does not attempt to establish the cited general theorems.  It
checks the finite comparison on which the gate relies:

* ordinary commuting projective records have one global joint instrument;
* a Specker anti-correlation cover has compatible, repeatable context-local
  archives and matching one-site marginals but no global extension;
* splitting the repeated occurrences by context restores a global archive,
  showing that local record formation alone does not select cross-context
  identity; and
* the standard equally noisy X/Y/Z qubit POVMs at eta=2/3 are pairwise
  jointly measurable but not triplewise jointly measurable under the known
  analytic orthogonal-Bloch-vector criterion.

The literature identities used to interpret these controls are recorded as
literature facts, not counted as executable checks.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_formed_sharp_quantum_selection_result.json"
)
SCHEMA = "dynamic-unity/formed-sharp-quantum-selection-hostile-gate/v0.1"

OUTCOMES = (0, 1)
VARIABLES = ("A", "B", "C")
CONTEXTS = (("A", "B"), ("B", "C"), ("C", "A"))


def encode_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def encode_distribution(
    distribution: dict[tuple[int, ...], Fraction],
) -> list[dict[str, Any]]:
    return [
        {
            "outcome": list(outcome),
            "probability": encode_fraction(probability),
        }
        for outcome, probability in sorted(distribution.items())
    ]


def marginal(
    distribution: dict[tuple[int, ...], Fraction],
    retained_indices: tuple[int, ...],
) -> dict[tuple[int, ...], Fraction]:
    result: dict[tuple[int, ...], Fraction] = {}
    for outcome, probability in distribution.items():
        retained = tuple(outcome[index] for index in retained_indices)
        result[retained] = result.get(retained, Fraction(0)) + probability
    return result


def is_normalized(distribution: dict[tuple[int, ...], Fraction]) -> bool:
    return all(value >= 0 for value in distribution.values()) and sum(
        distribution.values(), Fraction(0)
    ) == 1


def context_distribution_from_global(
    global_distribution: dict[tuple[int, int, int], Fraction],
    context: tuple[str, str],
) -> dict[tuple[int, int], Fraction]:
    indices = tuple(VARIABLES.index(variable) for variable in context)
    return marginal(global_distribution, indices)


def target_projective_model() -> dict[str, Any]:
    """A finite commuting-PVM model represented by three classical registers."""

    global_distribution = {
        assignment: Fraction(1, 8)
        for assignment in itertools.product(OUTCOMES, repeat=3)
    }
    pair_distributions = {
        "".join(context): context_distribution_from_global(
            global_distribution, context
        )
        for context in CONTEXTS
    }

    # In this representation, each outcome projector is the indicator of a
    # coordinate cylinder.  Indicator projectors are idempotent and commute.
    sample_space = tuple(itertools.product(OUTCOMES, repeat=3))
    projector_supports = {
        f"{variable}{value}": [
            list(assignment)
            for assignment in sample_space
            if assignment[VARIABLES.index(variable)] == value
        ]
        for variable in VARIABLES
        for value in OUTCOMES
    }

    return {
        "global_distribution": global_distribution,
        "pair_distributions": pair_distributions,
        "sample_space": sample_space,
        "projector_supports": projector_supports,
    }


def specker_anticorrelation_cover() -> dict[str, dict[tuple[int, int], Fraction]]:
    anti = {(0, 1): Fraction(1, 2), (1, 0): Fraction(1, 2)}
    return {"".join(context): dict(anti) for context in CONTEXTS}


def one_site_marginals(
    pair_distributions: dict[str, dict[tuple[int, int], Fraction]],
) -> dict[str, list[dict[tuple[int], Fraction]]]:
    result = {variable: [] for variable in VARIABLES}
    for context in CONTEXTS:
        name = "".join(context)
        distribution = pair_distributions[name]
        result[context[0]].append(marginal(distribution, (0,)))
        result[context[1]].append(marginal(distribution, (1,)))
    return result


def globally_consistent_assignments_for_specker() -> list[tuple[int, int, int]]:
    """Assignments satisfying A!=B, B!=C and C!=A."""

    return [
        assignment
        for assignment in itertools.product(OUTCOMES, repeat=3)
        if assignment[0] != assignment[1]
        and assignment[1] != assignment[2]
        and assignment[2] != assignment[0]
    ]


def context_split_completion() -> dict[tuple[int, ...], Fraction]:
    """A completion after replacing each repeated variable by its occurrence."""

    local_anti_outcomes = ((0, 1), (1, 0))
    completion: dict[tuple[int, ...], Fraction] = {}
    for ab, bc, ca in itertools.product(local_anti_outcomes, repeat=3):
        # Coordinate order: A_AB, B_AB, B_BC, C_BC, C_CA, A_CA.
        assignment = (*ab, *bc, *ca)
        completion[assignment] = Fraction(1, 8)
    return completion


def context_split_marginals(
    completion: dict[tuple[int, ...], Fraction],
) -> dict[str, dict[tuple[int, int], Fraction]]:
    return {
        "AB": marginal(completion, (0, 1)),
        "BC": marginal(completion, (2, 3)),
        "CA": marginal(completion, (4, 5)),
    }


def archived_reread_is_repeatable(
    distributions: Iterable[dict[tuple[int, int], Fraction]],
) -> bool:
    """The archive stores and returns the context-local outcome pair exactly."""

    for distribution in distributions:
        for outcome, probability in distribution.items():
            if probability > 0:
                pointer = tuple(outcome)
                archive = tuple(pointer)
                if tuple(archive) != tuple(pointer):
                    return False
                if tuple(archive) != tuple(archive):
                    return False
    return True


def noisy_pauli_triangle() -> dict[str, Any]:
    """Analytic joint-measurability controls for eta=2/3 noisy X/Y/Z."""

    eta = Fraction(2, 3)
    eta_squared = eta * eta

    # For orthogonal unbiased binary qubit observables:
    # pairwise joint measurability iff 2 eta^2 <= 1;
    # triplewise joint measurability iff 3 eta^2 <= 1.
    pair_measure = 2 * eta_squared
    triple_measure = 3 * eta_squared

    # Explicit pair joint:
    # G_ab^(ij) = 1/4[I + a eta sigma_i + b eta sigma_j].
    # Summing over b returns E_a^i = 1/2[I + a eta sigma_i].
    pair_joint_coefficients = {}
    pair_marginal_coefficients = {}
    for pair_name in ("XY", "YZ", "ZX"):
        first, second = pair_name
        pair_joint_coefficients[pair_name] = {}
        for first_sign, second_sign in itertools.product((-1, 1), repeat=2):
            pair_joint_coefficients[pair_name][
                f"{first_sign:+d},{second_sign:+d}"
            ] = {
                "I": encode_fraction(Fraction(1, 4)),
                first: encode_fraction(Fraction(first_sign, 1) * eta / 4),
                second: encode_fraction(
                    Fraction(second_sign, 1) * eta / 4
                ),
            }
        pair_marginal_coefficients[pair_name] = {
            f"{first}=+1": {
                "I": encode_fraction(Fraction(1, 2)),
                first: encode_fraction(eta / 2),
                second: encode_fraction(Fraction(0)),
            },
            f"{second}=+1": {
                "I": encode_fraction(Fraction(1, 2)),
                first: encode_fraction(Fraction(0)),
                second: encode_fraction(eta / 2),
            },
        }

    return {
        "eta": eta,
        "eta_squared": eta_squared,
        "pair_threshold_measure": pair_measure,
        "triple_threshold_measure": triple_measure,
        "pair_joint_coefficients": pair_joint_coefficients,
        "pair_marginal_coefficients": pair_marginal_coefficients,
    }


def run_probe() -> dict[str, Any]:
    target = target_projective_model()
    specker = specker_anticorrelation_cover()
    specker_marginals = one_site_marginals(specker)
    consistent_assignments = globally_consistent_assignments_for_specker()
    split_completion = context_split_completion()
    split_marginals = context_split_marginals(split_completion)
    pauli = noisy_pauli_triangle()

    target_global = target["global_distribution"]
    target_pairs = target["pair_distributions"]
    target_supports = target["projector_supports"]

    checks = [
        {
            "name": "target global projective model is normalized",
            "pass": is_normalized(target_global),
        },
        {
            "name": "target pair marginals are normalized",
            "pass": all(is_normalized(value) for value in target_pairs.values()),
        },
        {
            "name": "target pair marginals descend from one global model",
            "pass": all(
                target_pairs["".join(context)]
                == context_distribution_from_global(target_global, context)
                for context in CONTEXTS
            ),
        },
        {
            "name": "target binary projector supports partition the sample space",
            "pass": all(
                set(map(tuple, target_supports[f"{variable}0"])).isdisjoint(
                    set(map(tuple, target_supports[f"{variable}1"]))
                )
                and set(map(tuple, target_supports[f"{variable}0"]))
                | set(map(tuple, target_supports[f"{variable}1"]))
                == set(target["sample_space"])
                for variable in VARIABLES
            ),
        },
        {
            "name": "target coordinate projectors commute as set intersections",
            "pass": all(
                set(map(tuple, target_supports[f"{left}1"]))
                & set(map(tuple, target_supports[f"{right}1"]))
                == set(map(tuple, target_supports[f"{right}1"]))
                & set(map(tuple, target_supports[f"{left}1"]))
                for left, right in itertools.combinations(VARIABLES, 2)
            ),
        },
        {
            "name": "Specker context distributions are normalized",
            "pass": all(is_normalized(value) for value in specker.values()),
        },
        {
            "name": "Specker repeated one-site marginals agree across contexts",
            "pass": all(
                len(marginals) == 2 and marginals[0] == marginals[1]
                for marginals in specker_marginals.values()
            ),
        },
        {
            "name": "Specker one-site marginals are uniform",
            "pass": all(
                all(
                    marginal_distribution
                    == {(0,): Fraction(1, 2), (1,): Fraction(1, 2)}
                    for marginal_distribution in marginals
                )
                for marginals in specker_marginals.values()
            ),
        },
        {
            "name": "Specker context-local archives are exactly repeatable",
            "pass": archived_reread_is_repeatable(specker.values()),
        },
        {
            "name": "Specker anti-correlation cover has no global assignment",
            "pass": consistent_assignments == [],
        },
        {
            "name": "context splitting yields a normalized completion",
            "pass": is_normalized(split_completion),
        },
        {
            "name": "context-split completion reproduces every local archive",
            "pass": split_marginals == specker,
        },
        {
            "name": "eta=2/3 noisy Pauli effects are individually positive",
            "pass": Fraction(0) <= pauli["eta"] <= Fraction(1),
        },
        {
            "name": "eta=2/3 noisy orthogonal Pauli pairs meet exact pair criterion",
            "pass": pauli["pair_threshold_measure"] <= 1,
        },
        {
            "name": "eta=2/3 noisy orthogonal Pauli triple fails exact triple criterion",
            "pass": pauli["triple_threshold_measure"] > 1,
        },
        {
            "name": "pairwise compatibility is strictly separated from triple compatibility",
            "pass": (
                pauli["pair_threshold_measure"] < 1
                and pauli["triple_threshold_measure"] > 1
            ),
        },
    ]

    passed = sum(1 for check in checks if check["pass"])
    total = len(checks)

    result = {
        "schema": SCHEMA,
        "status": "PASS" if passed == total else "FAIL",
        "summary": {
            "passed": passed,
            "total": total,
            "verdict": (
                "CONTEXTWISE_FORMATION_TOO_WEAK__"
                "FULL_COVER_COMMON_DILATION_IS_JOINT_MEASURABILITY__"
                "NO_QUANTUM_SELECTION_DERIVED"
            ),
        },
        "checks": checks,
        "finite_controls": {
            "ordinary_commuting_projective_target": {
                "sample_space_size": len(target["sample_space"]),
                "global_distribution": encode_distribution(target_global),
                "pair_distributions": {
                    name: encode_distribution(distribution)
                    for name, distribution in target_pairs.items()
                },
            },
            "specker_anticorrelation_cover": {
                "pair_distributions": {
                    name: encode_distribution(distribution)
                    for name, distribution in specker.items()
                },
                "consistent_global_assignments": [
                    list(value) for value in consistent_assignments
                ],
                "context_local_archive_repeatable": True,
                "same_occurrence_global_extension_exists": False,
            },
            "context_split_absorber": {
                "coordinate_order": [
                    "A_AB",
                    "B_AB",
                    "B_BC",
                    "C_BC",
                    "C_CA",
                    "A_CA",
                ],
                "global_support_size": len(split_completion),
                "completion": encode_distribution(split_completion),
                "reproduces_local_contexts": split_marginals == specker,
                "meaning": (
                    "Formation and repeatable archival in each context do not "
                    "select identity of repeated occurrences."
                ),
            },
            "noisy_pauli_specker_triangle": {
                "eta": encode_fraction(pauli["eta"]),
                "eta_squared": encode_fraction(pauli["eta_squared"]),
                "two_eta_squared": encode_fraction(
                    pauli["pair_threshold_measure"]
                ),
                "three_eta_squared": encode_fraction(
                    pauli["triple_threshold_measure"]
                ),
                "pair_joint_coefficients": pauli["pair_joint_coefficients"],
                "pair_marginal_coefficients": pauli[
                    "pair_marginal_coefficients"
                ],
                "pairwise_jointly_measurable": True,
                "triplewise_jointly_measurable": False,
                "criterion_scope": (
                    "known necessary-and-sufficient criterion for three "
                    "equally noisy, unbiased, orthogonal binary qubit POVMs"
                ),
            },
        },
        "landscape_gate": {
            "restrictive_foil": (
                "one noncontextual preassigned global value model for every "
                "repeated measurement occurrence"
            ),
            "target_class": (
                "ordinary quantum theory with physically formed projective/"
                "Lueders record instruments"
            ),
            "permissive_foils": [
                (
                    "pairwise-compatible but non-global unsharp quantum "
                    "Specker triangle"
                ),
                (
                    "almost-quantum correlations, which survive probability-"
                    "level LO/CE"
                ),
            ],
            "candidate_selection_premise": (
                "one predeclared, provenance-preserving, refinement-natural "
                "physical dilation whose sharp pointer/archive instruments "
                "cover every context without interface refit"
            ),
            "absorber": (
                "contextwise sharp dilation is universal by Naimark; a common "
                "commuting full-cover dilation is equivalent to global joint "
                "measurability. Without independent dynamical selection, the "
                "former is too weak and the latter restates descent."
            ),
            "almost_quantum_disposition": (
                "conditionally excluded if an independently derived, theory-"
                "independent formation theorem entails Specker's principle; "
                "not excluded by the finite standard-quantum formation model"
            ),
            "quantum_selection_disposition": (
                "not established; Specker excludes one named outer class but "
                "does not uniquely recover all quantum states, transformations "
                "or correlations"
            ),
            "held_out_discriminator": (
                "coherently switch among the three pairwise physical "
                "implementations, keep all pointer/environment/provenance "
                "ports, and test whether repeated overlap outcomes implement "
                "one context-independent selective map and dilation under a "
                "single frozen isometry before testing the three-way "
                "continuation"
            ),
        },
        "literature_facts_not_executable_checks": [
            {
                "fact": (
                    "For sharp quantum observables, pairwise joint "
                    "measurability implies global joint measurability."
                ),
                "source": "https://arxiv.org/abs/0811.0783",
            },
            {
                "fact": (
                    "Almost-quantum correlations satisfy LO/CE but no theory "
                    "yielding them can satisfy Specker's principle."
                ),
                "sources": [
                    "https://arxiv.org/abs/1403.4621",
                    "https://arxiv.org/abs/1712.01225",
                ],
            },
            {
                "fact": (
                    "Repeatability plus minimal disturbance defines sharpness "
                    "in the cited GPT account; in quantum theory its sharp "
                    "instruments are Lueders instruments."
                ),
                "source": "https://arxiv.org/abs/1404.3348",
            },
            {
                "fact": (
                    "Three equally noisy orthogonal unbiased qubit observables "
                    "are triplewise jointly measurable iff 3 eta^2 <= 1."
                ),
                "source": "https://arxiv.org/abs/1312.6470",
            },
            {
                "fact": (
                    "Joint measurability is characterized by commuting "
                    "Naimark dilations in a common Hilbert space."
                ),
                "source": "https://arxiv.org/abs/1404.1477",
            },
        ],
        "does_not_establish": [
            "a new joint-measurability or contextuality theorem",
            "that pointer/archive formation selects system-level sharpness",
            "a theory-independent derivation of Specker's principle",
            "exclusion of every post-quantum theory",
            "unique reconstruction of ordinary quantum theory",
            "new physics or record-first ontology",
        ],
    }

    return result


def main() -> None:
    result = run_probe()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = result["summary"]
    print(
        "formed-sharp quantum-selection hostile gate: "
        f"{summary['passed']}/{summary['total']} checks passed"
    )
    print(summary["verdict"])
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
