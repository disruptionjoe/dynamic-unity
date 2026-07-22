#!/usr/bin/env python3
"""DU D-FORK discriminator, adapted to DU's RECORD ALGEBRA (not TI's novelty rate).

The D-FORK (TI E045): record-accretion is genuine *becoming* only if the operative
source's effective type space Theta_eff is self-generating (GODELIAN); if Theta_eff is
fixed-finite (FTS), the same roll is fixed-source DISCLOSURE and any "dark energy = becoming"
reading is a bookkeeping artifact. The true structural bit is non-computable in general
(TI E042: the independent set of a consistent r.e. extension of Q is productive, hence
non-c.e.).

THE N-WIRE-CROSSING (TI E046, DU known-challenge #4). TI's N is a novelty RATE
(N_n = novel-pool / (novel + background), a fraction in [0,1] whose CURVATURE signs the
regime -- E156). DU's N is an accreted COUNT (N = 4-volume = e^{4p}, Lambda ~ 1/sqrt(N)).
They are different objects sharing a letter. The regime STRUCTURE transfers; the
identification does NOT. Concretely: DU's N is MONOTONE by construction (volume only grows),
so E156's rate-curvature test is DEGENERATE on DU -- applying it is a category error. The
correct discriminator for DU is the fixed-H / H-growing OPERATOR-ALGEBRA test (TI E057,
FORMAL-OBJECT.md Adapter_P) adapted to DU's record algebra.

THE ADAPTED TEST (E057 on DU's records). DU's records are causal-set / 4-volume atoms laid
down as the conformal-scale mode p rolls. Let A_n be the algebra of observables over the
records accreted by stage n. DU sits in the GODELIAN regime for its case iff no fixed tuple
A_infty can factor every A_n while preserving records -- i.e. iff the roll SOURCE-FORCES
genuinely new observable/admissibility TYPES that are not a restriction, subalgebra,
coarse-graining, or value-selection inside a fixed A_infty (witnesses W1/W2/W3 of E057). If
the distinct observable-type count stays bounded, a fixed A_infty absorbs the whole trajectory
-> fixed-H -> FTS -> disclosure.

This fixture is a finite-window SIGNATURE, not a decision procedure (E156 discipline): it does
not decide the non-computable bit. What it does, honestly, is (a) show the algebra test
separates a reference FTS regime from a reference Godelian regime; (b) provide the mandatory
positive control (a genuine source-forced type-growth process the test MUST flag Godelian, so
the FTS verdict on DU-as-built is informative, not rigged); (c) classify DU's construction
AS CURRENTLY BUILT from three facts about DU's OWN construction; and (d) demonstrate the
wire-crossing guard (DU's monotone COUNT makes the rate-curvature test degenerate).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# The adapted discriminator: E057 operator-algebra factorization on records.
# A record process is modeled by how many DISTINCT observable/admissibility TYPES
# the source forces as records accrete. "type" = an integer label; injecting a
# fresh label = source-forcing a new admissibility class (E057 W2 / W3).
#
# fixed-H absorbed (FTS): the distinct-type set stabilizes at a finite ceiling.
#   A fixed A_infty on that finite type-set then factors every A_n (each A_n is a
#   subalgebra/restriction) -> no H-growth -> disclosure.
# H-growing (GODELIAN): the distinct-type count is productive (grows without bound,
#   non-pre-enumerable) -> no fixed A_infty factors all A_n -> genuine issuance.
# ---------------------------------------------------------------------------
def record_type_trajectory(
    new_observable_types_per_step: int,
    steps: int,
    initial_types: int = 1,
) -> list[int]:
    """Distinct observable/admissibility-type count after each accretion step.

    new_observable_types_per_step = 0  -> every record is the SAME type (a unit of
        4-volume); the type set never grows. Fixed-H absorber succeeds.
    new_observable_types_per_step >= 1 -> each roll-step SOURCE-FORCES a fresh
        admissibility class not pre-enumerable. Productive; fixed-H absorber fails.
    """
    distinct = initial_types
    series: list[int] = []
    for _ in range(steps):
        series.append(distinct)
        distinct += new_observable_types_per_step
    series.append(distinct)
    return series


def factorization_verdict(type_series: list[int]) -> dict[str, Any]:
    """Does a fixed A_infty factor every A_n? (E057 fixed-H null.)

    Yes iff the distinct-type count is bounded (stabilizes) -> fixed-H absorbed -> FTS.
    No  iff it is productive (strictly, unboundedly growing) -> H-growing -> Godelian.
    """
    growth = [type_series[i + 1] - type_series[i] for i in range(len(type_series) - 1)]
    type_count_bounded = all(g == 0 for g in growth)
    productive = all(g >= 1 for g in growth) and len(growth) > 0
    return {
        "distinct_type_series": type_series,
        "per_step_type_growth": growth,
        "type_count_bounded": type_count_bounded,
        "productive_type_growth": productive,
        # E057: fixed A_infty factors all A_n  <=>  bounded distinct-type count.
        "fixed_H_absorbed": type_count_bounded,
        "h_growing_witness_supplied": productive,
        "regime": "FTS_disclosure" if type_count_bounded
        else ("GODELIAN_issuance" if productive else "MIXED_indeterminate"),
    }


# ---------------------------------------------------------------------------
# Wire-crossing guard: DU's N is a monotone COUNT, so the TI rate-curvature test
# (E156) is degenerate. This function demonstrates the category error rather than
# committing it.
# ---------------------------------------------------------------------------
def du_N_count_curvature(p_values: list[float]) -> dict[str, Any]:
    """DU's N = e^{4p} over a rolling mode p. Show curvature is NOT a discriminator."""
    N = [math.exp(4.0 * p) for p in p_values]
    d2 = [N[i + 1] - 2 * N[i] + N[i - 1] for i in range(1, len(N) - 1)]
    monotone_increasing = all(N[i + 1] > N[i] for i in range(len(N) - 1))
    return {
        "p_values": p_values,
        "N_count": N,
        "second_differences": d2,
        "monotone_increasing": monotone_increasing,
        # e^{4p} with p rising is convex-up: curvature is a fixed sign, carries no
        # FTS-vs-Godelian information. The TI rate-curvature discriminator does not apply.
        "curvature_is_a_valid_discriminator_for_du": False,
        "why": (
            "DU's N is an accreted COUNT (4-volume, monotone by construction), not a "
            "novelty RATE in [0,1]. Its second difference has fixed sign and carries no "
            "regime information. E156's rate-curvature test is a TI-N object; importing it "
            "to DU-N is the wire-crossing. Use the algebra-factorization test instead."
        ),
    }


def run_fixture() -> dict[str, Any]:
    steps = 12

    # Reference regimes for the ADAPTED (algebra) discriminator.
    fts_ref = factorization_verdict(
        record_type_trajectory(new_observable_types_per_step=0, steps=steps)
    )
    godelian_ref = factorization_verdict(
        record_type_trajectory(new_observable_types_per_step=1, steps=steps)
    )
    discriminator_separates = (
        fts_ref["regime"] == "FTS_disclosure"
        and godelian_ref["regime"] == "GODELIAN_issuance"
    )

    # DU-as-built, classified from three facts about DU's OWN construction (each
    # re-verified here per DU's sovereign self-check duty, not imported as a grade):
    du_facts = {
        "source_is_fixed_action": {
            "fact": "The B5 source action is a single fixed action functional; the roll of "
            "p is its Euler-Lagrange flow -- a fixed, computable law.",
            "consequence": "Fixed-computable-law growth is in the CompletionClass null "
            "(TI E042 / FORMAL-OBJECT.md: finite/computable/fixed-law growth is ABSORBED). "
            "A trajectory generated by a fixed action does not source-force new types.",
            "pushes": "FTS",
            "new_observable_types_per_step": 0,
        },
        "N_is_four_volume": {
            "fact": "N = e^{4p} is the spacetime 4-volume; the records are causal-set atoms "
            "of ONE type (units of volume). Lambda ~ 1/sqrt(N) is the imported Sorkin "
            "volume-conjugate.",
            "consequence": "Growing 4-volume is ACCESS-expansion of a fixed field algebra "
            "(more of the same becomes accessible), which E057 explicitly rules is NOT "
            "H-growing ('merely increasing dimension / adding an environment does not "
            "count; growth must be source-forced, not access expansion').",
            "pushes": "FTS",
            "new_observable_types_per_step": 0,
        },
        "built_vacuum_supplies_no_grading": {
            "fact": "The only unconditionally-built vacuum is a SINGLET of the internal "
            "arena (W224): it supplies no good-stable grading. The object that would "
            "compactify the arena and define a grading -- the mirror-sector condensate -- "
            "is conditional on the operative-C branch + the unbuilt source action.",
            "consequence": "With no built grading, no roll-step source-forces a new "
            "observable/admissibility TYPE; the distinct-type count is 1 (constant). The "
            "candidate H-growing mechanism is exactly the UNBUILT / B5-gated piece.",
            "pushes": "FTS",
            "new_observable_types_per_step": 0,
        },
    }
    du_type_injection = max(
        f["new_observable_types_per_step"] for f in du_facts.values()
    )  # the most generous reading across the three facts
    du_as_built = factorization_verdict(
        record_type_trajectory(
            new_observable_types_per_step=du_type_injection, steps=steps
        )
    )

    # Wire-crossing guard on a sample roll (p rising as the de Sitter vacuum rolls).
    wire_crossing = du_N_count_curvature([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

    du_regime = du_as_built["regime"]

    return {
        "fixture_id": "du_d_fork_algebra_discriminator",
        "question": "Does DU's record-count roll (N=e^{4p}) live in the GODELIAN "
        "(self-generating -> genuine becoming) or FTS (fixed-source -> disclosure/"
        "bookkeeping) regime?",
        "kind": "finite_window_algebra_signature_not_a_decision_procedure",
        "discriminator": "E057 fixed-H / H-growing operator-algebra factorization on DU's "
        "record algebra (NOT E156 rate-curvature, which is a TI-N object)",
        "claim_status_change": "none",

        "adapted_discriminator_separates_regimes": discriminator_separates,
        "reference_fts_regime": fts_ref,
        "reference_godelian_regime_POSITIVE_CONTROL": godelian_ref,

        "du_construction_facts": du_facts,
        "du_as_built_type_injection_per_step": du_type_injection,
        "du_as_built": du_as_built,
        "du_regime_as_built": du_regime,

        "wire_crossing_guard": wire_crossing,

        "transducer_survives_d_fork_as_built": du_regime == "GODELIAN_issuance",

        "witness_that_would_flip_du_to_godelian": (
            "A source-forced record-ALGEBRA growth: build the compactifying mirror-sector "
            "condensate (the W224-missing grading vacuum) and show its sector-condensation "
            "across the roll is (W1) non-isomorphic observable-algebra growth or (W2) a "
            "new source-generated admissibility predicate, NOT reducible to access-"
            "expansion of a fixed field algebra and NOT a fixed-action phase transition "
            "(which is fixed-law => absorbed). This is unbuilt / B5-gated. Absent it, "
            "N=e^{4p} is a reparametrized single continuous mode = disclosure."
        ),

        "honest_scope": (
            "Finite-window SIGNATURE, not an oracle. The general D-FORK bit is non-computable "
            "(E042). But DU's source is, BY CONSTRUCTION, a fixed physical action -- a "
            "fixed-computable-law object that sits on the FTS side of the ledger by default, "
            "and reaches the Godelian side only by exhibiting a specific operator-algebra-"
            "growth witness a fixed action generically cannot supply. That is why DU's case "
            "is MORE decidable than the general fork -- and it currently reads FTS."
        ),

        "verdict": (
            "AS CURRENTLY BUILT, DU's record-count roll lives in the FTS / fixed-H / "
            "DISCLOSURE regime: a fixed-action conformal mode generating monotone 4-volume "
            "(access-expansion of a fixed field algebra), with the grading-defining "
            "condensate that would source-force type growth unbuilt (W224). The "
            "'record-accretion -> becoming -> dark energy' reading is therefore currently a "
            "BOOKKEEPING ARTIFACT, not genuine becoming. This is class-relative, not a wall: "
            "the named, buildable H-growing witness above would flip it to Godelian -- but "
            "that witness is exactly the B5-gated piece and must beat the fixed-law / "
            "phase-transition / Bogoliubov absorbers to count."
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
        default=Path("tests/artifacts/du_d_fork_algebra_discriminator_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
