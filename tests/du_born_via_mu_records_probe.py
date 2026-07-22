#!/usr/bin/env python3
"""DU cheap kill: does the mu-weight of decoherent record-histories reproduce |psi|^2
on a two-outcome toy WITHOUT re-importing the Born measure?

THE BET (dynamic-tension-reframe-sweep Bet #1, Class-A Born leg). The sigma-council
killed sigma on the measurement problem for supplying "no non-circular measure." DU's
answer: |psi|^2 weights = the mu-measure of decoherent record-histories, where mu is the
reversal-cost / impossibility measure (TI DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE H0):
a single measure on transformations of a shared record, decomposable into two INDEPENDENT
sources -- thermodynamic (Landauer) and computational-irreducibility cost. mu is a measure,
which is EXACTLY the type sigma lacked. The pre-registered kill: is mu genuinely non-circular,
or does it only land on |psi|^2 by smuggling |psi|^2 into the cost definition? Two outcomes,
both lethal (matches non-circularly = PASS, big; reproduces only by importing Born = FAIL).

THE TOY. A qubit |psi> = alpha|0> + beta|1>, |alpha|^2 + |beta|^2 = 1. The occurred outcome
is copied redundantly into an R-qubit environment (record-finality flow / quantum-Darwinism
redundancy): branch 0 record = 0^R, branch 1 record = 1^R. mu is computed TWO independent,
AMPLITUDE-FREE ways on the record string, exactly per the DRIVING-HYPOTHESIS two-source spec:
  (i)  Landauer / graph-erasure cost: erasing an R-bit record costs R*ln2 (thermodynamic).
  (ii) computational-irreducibility proxy: the reversible-work / algorithmic cost to un-write
       (compress + re-derive) the record string. For a uniform string it scales with R.
Then a mu-WEIGHT is read off by three natural non-circular rules and compared to |alpha|^2:
  (A) linear normalize   w_i = mu_i / sum(mu)
  (B) Boltzmann          w_i ~ exp(-mu_i)      (max-caliber / least reversal-cost)
  (C) inverse            w_i ~ 1/mu_i

THE SENSITIVITY (positive) CONTROL. A probe that can only ever output "not Born" is rigged.
So we also run the condition under which the toy WOULD reproduce Born non-circularly: if the
physical record redundancy were itself set to R_i ~ |alpha_i|^2 by the dynamics, linear-
normalize recovers |alpha|^2 (error -> 0). This proves the probe is SENSITIVE -- it detects
Born whenever the amplitude enters the physical record. The whole question then reduces to a
single physical fact: does decoherence make R_i proportional to |alpha_i|^2? It does not --
the occurred branch is copied regardless of its amplitude; the amplitude sets the coefficient
in rho (via the Born trace), not the record redundancy. That is the non-circular hook's
absence, made explicit.

THE CIRCULAR ROUTE, EXHIBITED. The one mu that hits Born exactly is the surprisal cost
mu_i = -ln|alpha_i|^2 (Boltzmann then gives w_i = |alpha_i|^2, error 0). We run it to SHOW it
works -- and to show it literally contains |alpha_i|^2 in the cost definition. Reproduction by
this route is Born-importing, not Born-deriving. Same for the envariance/multiplicity route:
equal-cost fine records reproduce Born iff the multiplicity m_i is set ~ |alpha_i|^2, i.e. the
Born measure is the multiplicity input.

This is a finite toy SIGNATURE, not a proof about all decoherence models. What it does,
honestly: (a) show the non-circular two-source mu is SYMMETRIC between outcomes and so yields
uniform 1/2 weights, missing |alpha|^2 by |p-0.5|; (b) show the probe CAN reproduce Born (the
sensitivity control) so the failure is informative, not rigged; (c) localize EXACTLY where
Born re-enters on the two routes that do reproduce it (the cost definition; the multiplicity).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

LN2 = math.log(2.0)


# ---------------------------------------------------------------------------
# The record-finality flow: the occurred outcome is copied redundantly into the
# environment (quantum-Darwinism redundancy). The record of outcome i is the bit
# string i repeated R_i times. CRUCIALLY, standard decoherence copies WHICHEVER
# outcome occurred with a redundancy set by the coupling/time, NOT by the amplitude:
# both branches get equally good records. So the default is R_0 = R_1 = R.
# ---------------------------------------------------------------------------
def record_redundancies(R: int, amplitude_free: bool, p0: float) -> tuple[int, int]:
    """Return (R_0, R_1), the environment redundancy of each branch's record.

    amplitude_free=True  -> R_0 = R_1 = R  (physical decoherence: symmetric copying).
    amplitude_free=False -> R_i ~ |alpha_i|^2  (the SENSITIVITY CONTROL precondition:
                            amplitude feeds the physical record; NOT what decoherence does).
    """
    if amplitude_free:
        return R, R
    # Sensitivity control: let the physical record carry the amplitude non-circularly.
    total = 2 * R
    R0 = max(1, round(total * p0))
    R1 = max(1, round(total * (1.0 - p0)))
    return R0, R1


def mu_landauer(R_i: int) -> float:
    """Source (i): thermodynamic / Landauer erasure cost of an R_i-bit record (units kT)."""
    return R_i * LN2


def mu_comp_irreducibility(R_i: int) -> float:
    """Source (ii): computational-irreducibility proxy -- the reversible-work / algorithmic
    cost to un-write a uniform R_i-bit record. Compress (O(log R_i) description) then re-derive
    by R_i deterministic steps: the irreducible re-derivation work scales with R_i. For a
    uniform string the two branches are related by a bit-flip symmetry, so this is SYMMETRIC in
    the outcome label -- it depends on R_i, never on which symbol or on the amplitude."""
    return R_i * 1.0  # one irreducible step per recorded atom; symbol-independent


def two_source_mu(R_i: int) -> dict[str, float]:
    """The single mu with its two independent sources, per DRIVING-HYPOTHESIS H0."""
    a = mu_landauer(R_i)
    b = mu_comp_irreducibility(R_i)
    return {"landauer": a, "comp_irreducibility": b, "mu_total": a + b}


# ---------------------------------------------------------------------------
# mu-weight rules (non-circular): read a probability weight off the two mu values.
# ---------------------------------------------------------------------------
def weights_linear(mu0: float, mu1: float) -> tuple[float, float]:
    s = mu0 + mu1
    return (mu0 / s, mu1 / s) if s > 0 else (0.5, 0.5)


def weights_boltzmann(mu0: float, mu1: float) -> tuple[float, float]:
    e0, e1 = math.exp(-mu0), math.exp(-mu1)
    s = e0 + e1
    return (e0 / s, e1 / s)


def weights_inverse(mu0: float, mu1: float) -> tuple[float, float]:
    i0, i1 = 1.0 / mu0, 1.0 / mu1
    s = i0 + i1
    return (i0 / s, i1 / s)


def scan(p0_grid: list[float], R: int) -> dict[str, Any]:
    """Run every route across a scan of |alpha|^2 = p0; report max |w0 - p0| per route."""
    rows: list[dict[str, Any]] = []
    max_err = {
        "noncirc_linear": 0.0,
        "noncirc_boltzmann": 0.0,
        "noncirc_inverse": 0.0,
        "control_amplitude_in_record_linear": 0.0,
        "circular_surprisal_boltzmann": 0.0,
        "envariance_noncirc_equal_multiplicity": 0.0,
        "envariance_circular_born_multiplicity": 0.0,
    }
    for p0 in p0_grid:
        p1 = 1.0 - p0
        born = (p0, p1)

        # --- Route 1: NON-CIRCULAR two-source mu on the physical (symmetric) record. ---
        R0, R1 = record_redundancies(R, amplitude_free=True, p0=p0)
        m0, m1 = two_source_mu(R0)["mu_total"], two_source_mu(R1)["mu_total"]
        nc_lin = weights_linear(m0, m1)
        nc_bol = weights_boltzmann(m0, m1)
        nc_inv = weights_inverse(m0, m1)

        # --- SENSITIVITY CONTROL: amplitude enters the physical record (R_i ~ |alpha_i|^2). ---
        cR0, cR1 = record_redundancies(R, amplitude_free=False, p0=p0)
        cm0, cm1 = two_source_mu(cR0)["mu_total"], two_source_mu(cR1)["mu_total"]
        ctrl_lin = weights_linear(cm0, cm1)

        # --- CIRCULAR ROUTE: surprisal cost mu_i = -ln|alpha_i|^2 (contains |alpha_i|^2). ---
        smu0, smu1 = -math.log(p0), -math.log(p1)
        circ_bol = weights_boltzmann(smu0, smu1)  # = (p0, p1) exactly

        # --- ENVARIANCE / MULTIPLICITY: equal-cost fine records, count = multiplicity. ---
        M = 1000
        env_equal = weights_linear(1.0, 1.0)          # equal multiplicity -> 1/2
        mult0, mult1 = max(1, round(M * p0)), max(1, round(M * p1))
        env_born = weights_linear(mult0, mult1)       # multiplicity ~ |alpha|^2 -> Born

        max_err["noncirc_linear"] = max(max_err["noncirc_linear"], abs(nc_lin[0] - p0))
        max_err["noncirc_boltzmann"] = max(max_err["noncirc_boltzmann"], abs(nc_bol[0] - p0))
        max_err["noncirc_inverse"] = max(max_err["noncirc_inverse"], abs(nc_inv[0] - p0))
        max_err["control_amplitude_in_record_linear"] = max(
            max_err["control_amplitude_in_record_linear"], abs(ctrl_lin[0] - p0))
        max_err["circular_surprisal_boltzmann"] = max(
            max_err["circular_surprisal_boltzmann"], abs(circ_bol[0] - p0))
        max_err["envariance_noncirc_equal_multiplicity"] = max(
            max_err["envariance_noncirc_equal_multiplicity"], abs(env_equal[0] - p0))
        max_err["envariance_circular_born_multiplicity"] = max(
            max_err["envariance_circular_born_multiplicity"], abs(env_born[0] - p0))

        rows.append({
            "born_p0": round(p0, 4),
            "record_redundancy_R0_R1_physical": [R0, R1],
            "mu0_mu1_physical": [round(m0, 4), round(m1, 4)],
            "noncirc_linear_w0": round(nc_lin[0], 4),
            "noncirc_boltzmann_w0": round(nc_bol[0], 4),
            "noncirc_inverse_w0": round(nc_inv[0], 4),
            "control_record_carries_amplitude_w0": round(ctrl_lin[0], 4),
            "circular_surprisal_w0": round(circ_bol[0], 4),
            "envariance_equal_mult_w0": round(env_equal[0], 4),
            "envariance_born_mult_w0": round(env_born[0], 4),
        })
    return {"rows": rows, "max_abs_error_vs_born": {k: round(v, 6) for k, v in max_err.items()}}


def run_fixture() -> dict[str, Any]:
    p0_grid = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    R = 8
    s = scan(p0_grid, R)
    err = s["max_abs_error_vs_born"]
    tol = 1e-9

    noncirc_reproduces_born = (
        err["noncirc_linear"] < 1e-3
        and err["noncirc_boltzmann"] < 1e-3
        and err["noncirc_inverse"] < 1e-3
    )
    control_is_sensitive = err["control_amplitude_in_record_linear"] < 0.05
    circular_route_hits_born = err["circular_surprisal_boltzmann"] < tol
    envariance_needs_born_multiplicity = (
        err["envariance_noncirc_equal_multiplicity"] > 0.3
        and err["envariance_circular_born_multiplicity"] < 0.02
    )

    born_leg = "PASS" if noncirc_reproduces_born else "FAIL"

    return {
        "fixture_id": "du_born_via_mu_records_probe",
        "question": "Does the mu-weight of decoherent record-histories reproduce |psi|^2 on a "
        "two-outcome toy WITHOUT re-importing the Born measure? (Bet #1, Class-A Born leg; the "
        "pre-registered cheap kill.)",
        "kind": "finite_two_outcome_signature_not_a_proof_about_all_decoherence",
        "claim_status_change": "none",

        "scan": s,

        "noncircular_two_source_mu_reproduces_born": noncirc_reproduces_born,
        "sensitivity_control_can_reproduce_born_when_amplitude_enters_record": control_is_sensitive,
        "circular_surprisal_cost_hits_born_exactly": circular_route_hits_born,
        "envariance_reproduces_born_only_with_born_valued_multiplicity":
            envariance_needs_born_multiplicity,

        "diagnosis": {
            "why_noncircular_misses": (
                "The two-source mu (Landauer R*ln2 + computational-irreducibility R) is a "
                "function of the record redundancy R_i ONLY, and physical decoherence copies "
                "the occurred outcome symmetrically (R_0 = R_1). So mu_0 = mu_1 for every "
                "|alpha|^2, every non-circular weight rule gives 1/2, and the error is exactly "
                "|p0 - 0.5| -- maximal at the extremes. mu is the right TYPE (a measure) but "
                "SYMMETRIC in the outcome label; |alpha|^2 lives in rho's diagonal (a Born-trace "
                "quantity), not in the record string."
            ),
            "where_born_re_enters_on_the_routes_that_hit_it": (
                "(1) Surprisal cost mu_i = -ln|alpha_i|^2 reproduces Born under Boltzmann "
                "EXACTLY -- because |alpha_i|^2 is written into the cost. (2) Envariance/"
                "multiplicity reproduces Born iff the fine-record multiplicity m_i ~ |alpha_i|^2 "
                "-- because the Born measure IS the multiplicity input. Both are Born-importing, "
                "not Born-deriving."
            ),
            "the_missing_noncircular_hook": (
                "Born would follow non-circularly IF the dynamics set the physical record "
                "redundancy R_i ~ |alpha_i|^2 (the sensitivity control shows linear-normalize "
                "then recovers |alpha|^2). Standard decoherence does NOT do this: redundancy is "
                "set by the system-environment coupling and time, identical for both branches. "
                "No built DU object makes R_i ~ |alpha_i|^2 without invoking the Born trace."
            ),
        },

        "born_leg_verdict": born_leg,
        "verdict": (
            "FAIL (honest): the non-circular two-source mu does NOT reproduce |psi|^2 -- it is "
            "symmetric in the outcome and yields uniform 1/2, missing Born by |p-0.5|. The only "
            "mu that lands on |psi|^2 does so by importing |alpha|^2 into the cost (surprisal) "
            "or into the multiplicity (envariance). mu is confirmed to be the RIGHT TYPE (a "
            "measure -- exactly what sigma/tau lacked), but as a Born DERIVATION it currently "
            "smuggles Born in. This kills the strong 'mu grounds Born non-circularly' claim at "
            "toy grade; it leaves intact the weaker, honest claim that DU supplies a measure-"
            "typed object where the static data supplied none. Class-relative, not a wall: the "
            "named flip is a built DU mechanism forcing R_i ~ |alpha_i|^2 (or an equivalent "
            "record-native measure) WITHOUT the Born trace -- unbuilt, and it must beat the "
            "circularity that sank every route here."
        ),
        "honest_scope": (
            "A finite two-outcome SIGNATURE, not a theorem over all decoherence models or all "
            "mu constructions. It shows the SPECIFIC two-source mu named in the DRIVING-"
            "HYPOTHESIS is outcome-symmetric on the canonical redundancy record and therefore "
            "non-circularly Born-blind, and it localizes where the reproducing routes import "
            "Born. A genuinely different, still-non-circular mu is not excluded -- it is "
            "exactly the unbuilt object the PASS branch would require."
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
        default=Path("tests/artifacts/du_born_via_mu_records_probe_result.json"),
    )
    args = parser.parse_args()
    result = run_fixture()
    write_json(result, args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
