---
title: "D1 executed: the functional form of the classicality transition — time-resolved decoherence data against the three layer-D mechanism signatures"
status: exploration
doc_type: discriminator_results_note
created: 2026-08-03
owner_repo: dynamic-unity
authority: "Joe direct chat: D1 execution authorization, 2026-08-03 (literature check only; no commit authorized in-session; no routing change)"
preregistration: >-
  explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md,
  section 3, discriminator D1. The pass/fail table there is frozen and is the
  sole verdict authority for this note. No verdict below departs from it.
claim_grade: "EXECUTED DISCRIMINATOR / LITERATURE COLLISION (CH-COLLIDE) / VERDICTS FROM THE FROZEN TABLE ONLY / NO GRADE MOVEMENT, NO BANKING DECISION, NON-ROUTING"
banked: false
routing_note: >-
  This note routes nothing. CURRENT-RESEARCH.yaml remains the sole mutable
  authority for priority, WIP, execution, stops, and reopeners. Campaign
  continuation (D2 next per the plan's decision tree) is Joe's decision
  through that file.
lane_channel: "Lane 5 primary (Lanes 3, 4 supporting); CH-COLLIDE"
inputs:
  - explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md (frozen protocol and verdict table)
  - joe-thinking-wiki map/explorations/q0063-eliminative-case-battery.md (signature wording; assistant-constructed, unratified; consumed as scoping input only)
  - explorations/external-mergeable-sector-theorem-spine-and-taf-record-typing-absorption-2026-08-03.md (Wave 1a companion)
  - primary literature reconstructed at execution (section 2; full citations in Provenance)
---

# D1 executed: the functional form of the classicality transition — literature check

## 0. What this note is

This is the dated results note for discriminator D1 of the Q-0063
decoherence-null confrontation campaign (Wave 1b plan, 2026-08-03). D1 asks
whether existing time-resolved decoherence data already settles the
functional form of the classicality transition — distinguishing the null's
signature (pure exponential decoherence at a system-specific timescale) from
the three preregistered layer-D mechanism signatures:

| Mechanism | Preregistered signature (battery wording, frozen by the plan) |
|---|---|
| None — decoherence only (the null) | exponential suppression of off-diagonal terms with a characteristic time |
| Metastable threshold | tipping point with critical exponents; finite-size scaling; universality classes across microscopically unrelated systems |
| BFT quorum | discrete jump at a participation fraction, not a smooth threshold |
| CRDT merge | no threshold; monotone convergence with order-independence — the classical outcome should not depend on the sequence in which environment fragments decohere |

The frozen verdict table (quoted from the preregistration, binding here):

> - If two or more independent platforms resolve the transition with
>   sufficient resolution to *exclude* the three mechanism signatures at
>   measured scales → layer D closes on "none" in those regimes; the null
>   survives D1; the mechanism trio loses its empirical target in existing
>   data; DU may continue only through D2/D3 (audit-content route), not
>   through mechanism signatures.
> - If any dataset shows a reproducible deviation matching one preregistered
>   mechanism signature → null wounded; that mechanism becomes the campaign
>   focus (route to D6 for hardening).
> - If the data cannot discriminate (regime or resolution limits) → layer D
>   stays open; record the exact missing measurement; burden moves to D6.

Per the plan: exclusion here closes layer-D mechanisms but does **not**
close DU — the audit route (D2/D3) remains; a detected signature wounds the
null. Work below is published data and published curves only; no new
computation beyond reading fitted forms and stated agreements from primary
sources. Three coordinates: scope regional/public; status epistemic (a
reading of published evidence); formation disclosure only.

## 1. Corpus reconstructed from primary sources

The plan's pins were named from memory and required primary-source
reconstruction at execution. All pins reconstructed and confirmed; none
required correction. Corpus actually consulted:

| Platform | Environment / fragments | Transition observable and resolution | Source |
|---|---|---|---|
| Microwave cavity QED cat states (Brune/Haroche line) | natural photon loss into cavity environment | two-atom correlation signal vs atom delay, 30–250 microseconds, cat sizes n-bar = 3.3 and 5.1, two phase splittings | Brune et al., PRL 77, 4887 (1996); curve details via Raimond and Haroche, Seminaire Poincare 2, 25–64 (2005) |
| Same, full state tomography | same | time-resolved Wigner-function "movies" in 4 ms windows across the full transition (interference term gone by ~50 ms); off-diagonal coherence fitted vs time | Deleglise et al., Nature 455, 510 (2008); arXiv:0809.1064 |
| Macromolecule interferometry, collisional (Arndt–Hornberger line) | background-gas collisions (strong fragments: one collision resolves the path) | Talbot–Lau fringe visibility vs gas pressure, 1e-7 to 1e-6 mbar, ~30% visibility down to noise floor | Hornberger et al., PRL 90, 160401 (2003); Arndt, Gerlich, Hornberger review, arXiv:2101.08216 |
| Macromolecule interferometry, thermal | emitted thermal photons (weak fragments: wavelength >> path separation) | visibility vs heating power / internal temperature, 47% to 0% across ~1500–3000 K | Hackermuller et al., Nature 427, 711 (2004); review arXiv:2101.08216 |
| Macromolecule frontier | residual (decoherence subdominant) | 25 kDa / up to 2000-atom interference, visibility 25 +/- 3% | Fein et al., Nat. Phys. 15, 1242 (2019) |
| Trapped-ion motional cats, engineered reservoirs | engineered amplitude and phase reservoirs plus natural heating noise | fringe contrast vs applied noise variance and vs wait time, for a family of superposition sizes Delta-alpha | Myatt et al., Nature 403, 269 (2000); Turchette et al., PRA 62, 053807 (2000) |
| Superconducting-cavity cats | single-photon loss, monitored | repeated QND parity measurement resolving individual photon-jump events in time; 100-photon-scale cats | Sun et al., Nature 511, 444 (2014); Vlastakis et al., Science 342, 607 (2013) |
| Fragment-resolved redundancy (quantum Darwinism line) | engineered multi-fragment environments (photonic cluster states, NV nuclear spins, superconducting qubits) | mutual information vs environment-fragment size | Ciampini et al., PRA 98, 020101(R) (2018); Unden et al., PRL 123, 140402 (2019); Chen et al., Sci. Bull. 64, 580 (2019); superconducting: arXiv:2504.00781, Sci. Adv. (2025) |
| Non-Markovian control (scope check for the merge leg) | engineered environment memory | coherence revivals under information backflow | Liu et al., Nat. Phys. 7, 931 (2011) |

Key reconstructed statements, quoted at source grade:

- Brune 1996 (via Raimond 2005, pp. 51–52): the two-atom correlation decays
  as "the product of a decaying exponential by a cosine function of time";
  the rate is the cavity damping rate multiplied by the squared phase-space
  distance of the cat components (1/T_D = 2 kappa n-bar sin^2 Phi_0); "the
  agreement with the theoretical model is excellent. Most strikingly,
  decoherence proceeds at a faster rate when the distance between cat state
  components increases," with "similar agreement" across n-bar = 3.3 and
  5.1.
- Deleglise 2008 (arXiv:0809.1064, p. 4): "A common exponential fit yields
  a decoherence time T_d = 17 +/- 3 ms. A simple analytical model of
  decoherence predicts T_d = 2T_c/d^2 = 22 ms at T = 0 K, reduced to T_d =
  19.5 ms when including thermal" photons. The transition is watched, not
  inferred: snapshots in 4 ms windows show the interference feature decay
  smoothly to zero by ~50 ms while the classical components persist.
- Hornberger 2003 (via arXiv:2101.08216, Fig. 4 caption and section II):
  visibility vs pressure is "in excellent agreement with the expected
  exponential loss of contrast"; "the exponential decay indicates that each
  collision leads to a complete loss of coherence," with the effective
  cross-section quantitatively matching the calculated van der Waals
  scattering value.
- Hackermuller 2004 (via arXiv:2101.08216, section II.2): "Very good
  agreement was found between the predictions of decoherence theory and the
  experimental observation ... the internal temperature needs to exceed
  1500 K before sizeable decoherence could be observed, growing gradually
  and with the expected functional dependence when the temperature was
  increased."
- Turchette 2000 (PRA 62, 053807, abstract and section V.A): "We confirm
  the theoretically well-known scaling laws that predict that the
  decoherence rate of superposition states scales with the square of the
  'size' of the state." "Decay curves were recorded for a variety of
  superposition sizes |Delta-alpha|, and all the data agree with a single
  exponential," with decay constant proportional to |Delta-alpha|^2. For
  natural heating noise the decoherence-derived rate (7.5 +/- 0.7
  quanta/ms) agrees reasonably with the independently measured heating rate
  (5.7 +/- 1 quanta/ms). For the engineered phase reservoir "there is no
  simple universal scaling law for the functional form," and the
  one-parameter theory curves match the data.
- Fein 2019: interference of functionalized oligoporphyrins beyond 25 kDa
  with visibility 25 +/- 3%; collisional and thermal decoherence estimated
  subdominant; the result constrains objective-collapse parameter space —
  i.e., no excess decoherence observed at the measured scale.
- Quantum Darwinism line: mutual information vs fragment size shows the
  smooth rapid rise to a redundancy plateau on photonic (2018, 2019), NV
  (2019), and superconducting (2025) platforms; the superconducting
  experiment reports "saturation of quantum mutual information" with no
  threshold structure.

## 2. Signature 1 — finite-size critical scaling: EXCLUDED at measured scales

What the signature requires: non-analytic behavior in a control parameter
(tipping point), finite-size scaling collapse, and shared critical
exponents across microscopically unrelated systems.

What the data show, on four independent platforms:

1. Time dependence is exponential through the resolved transition (Brune
   correlation decay; Deleglise coherence fit; Turchette contrast decay;
   collisional visibility exponential in the collision-number variable) —
   not power-law, not scaling-collapse form.
2. The size dependence of the rate is smooth and analytic — quadratic in
   the separation (kappa D^2 in cavity QED, |Delta-alpha|^2 in the ion
   trap), linear in pressure in the collisional line — and is
   quantitatively the null's own prediction with coefficients fixed by
   independently measured platform constants (cavity damping time,
   measured heating rate, calculated scattering cross-section). There is
   no free mechanism dial and no non-analyticity at any measured size.
3. Universality across platforms — the signature's distinctive content —
   is absent in exactly the way decoherence theory requires: each
   platform's rate is set by its own microphysics, and Turchette's phase
   reservoir explicitly has "no simple universal scaling law for the
   functional form" while still matching one-parameter theory. Nothing
   resembling shared exponents across microscopically unrelated systems
   appears anywhere in the corpus.

Resolution honesty: the cavity-QED and ion-trap curves resolve the
transition itself (multiple time/noise points through the decay at several
sizes), and the molecule lines resolve the full visibility transition over
a decade of pressure and a factor ~2 of temperature. This meets the
frozen table's "sufficient resolution" condition for this signature: a
tipping point with critical exponents inside the measured regimes would
have produced curve shapes these datasets could not have fit with
single-exponential, analytically size-scaled forms.

**Verdict (frozen table, first branch, applied to this signature):
excluded at measured scales on two or more independent platforms.**

## 3. Signature 2 — discrete participation jump (quorum): EXCLUDED at measured scales

What the signature requires: classicality onset as a discrete jump at a
participation fraction of the environment, not a smooth threshold.

What the data show, in the three regimes that bracket the observable:

1. Strong-fragment regime (collisional decoherence): each collision fully
   resolves the path, and visibility falls exponentially from the very
   first collision (exponential in pressure over the full measured
   decade). A quorum of N >= 2 fragments would produce a flat-then-drop
   threshold shape (no visibility loss until the quorum accumulates);
   this is excluded by the measured pure exponential. The degenerate
   quorum-of-one case is empirically identical to the null's
   single-collision prediction in this regime — recorded as a degeneracy,
   not a detection: it carries no distinguishable mechanism content, which
   is exactly what "loses its empirical target" means in the frozen table.
2. Weak-fragment regime (thermal decoherence): each emitted photon carries
   only partial which-path information, so many fragments must accumulate
   — the regime where a participation jump would be most visible. The
   measured onset is gradual, "with the expected functional dependence,"
   quantitatively matching continuous accumulation of partial resolving
   power (including spectral distribution, radiative cooling, and
   emission-position dependence) with no jump anywhere in the 1500–3000 K
   transition window.
3. Fragment-resolved regime (quantum Darwinism experiments): mutual
   information versus fragment size — the participation observable
   directly — rises smoothly to the redundancy plateau on photonic, NV,
   and superconducting platforms. No discrete participation threshold is
   reported on any of them.

Honesty note on discrete events: the individual quantum jumps resolved by
QND parity tracking (Sun 2014) are the null's own elementary loss events —
single-fragment emissions — not a participation quorum; the coherence
functional under their statistics decays smoothly at the expected rate.
Discreteness of environment fragments is not discreteness of the
classicality transition.

**Verdict (frozen table, first branch, applied to this signature):
excluded at measured scales on two or more independent platforms.**

## 4. Signature 3 — order-independent monotone convergence (merge): SILENT

What the signature requires: no threshold; monotone convergence; and the
distinctive leg — the classical outcome independent of the sequence in
which environment fragments decohere.

Why the data cannot discriminate:

1. Wrong observable for the distinctive leg. No publication-grade
   experiment in this corpus (or found in the sweep) varies the order of
   environment-fragment interactions at matched total coupling and
   compares the resulting record. Order-dependence is studied in the
   collision-model literature as theory and programmable simulation, not
   as a measured property of a natural classicality transition.
2. The monotonicity leg is non-discriminating. Monotone decay in the
   measured Markovian regimes is equally the null's prediction, so its
   observation (everywhere in section 1's corpus) separates nothing; and
   in engineered-memory regimes, standard open-system theory itself
   predicts and experiment confirms non-monotone revivals (Liu 2011), so
   "strict monotone convergence" cannot even be posed as a mechanism
   signature without first scoping it against environment memory — a
   scoping the preregistered battery wording does not supply.

Exact missing measurement (recorded per the frozen table's third branch):
a single decohering system coupled sequentially to distinguishable,
individually addressable environment fragments with mutually
non-commuting couplings, where the fragment order is permuted between
otherwise identical runs at matched total interaction strength, and the
resulting pointer record / coherence functional is compared across
orders. The nearest existing capabilities are the fragment-resolved
circuit-QED Darwinism setup (arXiv:2504.00781) and photonic cluster-state
environments (Ciampini 2018; Chen 2019), none of which has published an
order-permutation protocol.

**Verdict (frozen table, third branch, applied to this signature): the
data cannot discriminate; layer D stays open on this signature; the exact
missing measurement is recorded above; burden moves to D6.** Observation
recorded without altering any frozen table: D6 as designed is the
finite-size-scaling reanalysis (order parameter and scaling family), which
does not by itself discharge a confluence-shaped burden; within the
campaign's own structure the matching theory-side splitter is D7, and the
empirical version is the missing measurement above. Disposition of that
mismatch is a Joe decision through the live authority.

## 5. Deviation sweep — the null is not wounded

Searched for any reproducible published deviation matching a preregistered
signature in these experimental lines. None found. What the sweep did
find, recorded for honesty:

- Known anomalies in these platforms are rate-magnitude or technical, not
  functional-form: ion-trap "anomalous heating" is an imperfectly
  understood noise *source* whose induced decoherence nevertheless decays
  exponentially with the measured heating rate (Turchette 2000);
  day-to-day rate variations and calibration systematics are declared as
  such by the experimenters; early-apparatus contrast deficits are
  attributed and modeled.
- Collapse-model searches — which are precisely hunts for excess,
  mechanism-bearing deviation from decoherence theory — report bounds,
  not detections, at the measured scales (Fein 2019 and the
  interferometry line generally).
- The null's step-6 zero-anomaly prediction therefore survives contact
  with the full reconstructed corpus.

**No dataset triggers the frozen table's second branch.**

## 6. Composite verdict and what it licenses

Per signature, from the frozen table only:

| Signature | Verdict | Branch |
|---|---|---|
| Finite-size critical scaling (metastable threshold) | EXCLUDED at measured scales, >= 2 independent platforms | first |
| Discrete participation jump (quorum) | EXCLUDED at measured scales, >= 2 independent platforms | first |
| Order-independent monotone convergence (merge) | SILENT — wrong observable / non-discriminating leg; missing measurement recorded; burden moves to D6 | third |

Composite, stated with the table's own semantics:

- **The null survives D1 unwounded.** No mechanism signature was detected
  anywhere in the corpus.
- **Layer D closes on "none" for the critical-scaling and quorum
  mechanisms in the measured regimes.** Those two mechanisms lose their
  empirical target in existing data. The full first-branch closure of the
  trio is *not* claimed: the merge leg is silence, not exclusion, and
  silence is not a verdict on the mechanism — it gates D6.
- **DU is not closed by this result.** Per the preregistration, DU may
  continue only through D2/D3 (audit-content route), not through mechanism
  signatures in existing data. Per the plan's decision tree, the next
  discriminator is D2 (the QD/SBS audit-gap witness).
- Scope guard: all exclusions hold at measured scales only — cat sizes of
  order 3–100 photons, molecules to 25 kDa / 2000 atoms, ion motional
  superpositions of a few phonon-scale separations, fragment-resolved
  environments of order ten addressable fragments. Nothing here
  extrapolates the exclusions to unmeasured macroscopic regimes, and
  nothing here converts the null's survival into evidence against DU's
  audit-layer question, which is typed independently (D2/D3).

D1 has returned a preregistered verdict; under the campaign's stop rules
its box is closed. This note is the "one dated exploration per executed
discriminator" the plan requires.

## 7. Preregistration discipline audit

- Pass/fail preceded computation: the verdict table was frozen in the
  2026-08-03 plan before any literature contact under this discriminator;
  no table was amended during execution; the D6/D7 mismatch observation in
  section 4 is recorded outside the tables and changes nothing.
- No interface refit: the signatures were taken verbatim from the frozen
  plan (battery wording); no signature was reshaped to fit the data.
- Absorber-first: every positive statement in sections 2–5 is the null's
  own content (decoherence theory, QD, open-system response); no
  DU-distinctive wording is used anywhere in the verdicts.
- Two-sidedness honored in execution: the discriminator could have wounded
  the null (branch two was live; section 5 is the evidence it was actually
  hunted).

## Not established

This note establishes no DU claim and moves no grade. The layer
decomposition and signature table originate in an assistant-constructed,
unratified battery; this execution consumed the plan's frozen restatement
of them, not the battery's authority. Two load-bearing quotes (Brune 1996
curve behavior; Hornberger/Hackermuller figure-level statements) were
reconstructed through experimenter-authored secondary sources (Raimond
2005; Arndt–Gerlich–Hornberger 2021) rather than the paywalled primary
PDFs; the primary bibliographic pins themselves were verified. The corpus
sweep may have missed platforms; absence from this sweep is not evidence
of absence from the literature. The SILENT verdict on the merge signature
is a statement about the current publication-grade corpus, not a proof
that no such data exist. Banking, campaign continuation, commit, and any
routing consequence are Joe's decisions through CURRENT-RESEARCH.yaml.

## Provenance

Preregistration and internal:

- `explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md` (frozen D1 protocol and verdict table)
- `joe-thinking-wiki#map/explorations/q0063-eliminative-case-battery.md` (signature wording; unratified input)
- `explorations/external-mergeable-sector-theorem-spine-and-taf-record-typing-absorption-2026-08-03.md` (Wave 1a companion)

External, reconstructed at execution:

- M. Brune, E. Hagley, J. Dreyer, X. Maitre, A. Maali, C. Wunderlich,
  J.-M. Raimond, S. Haroche, "Observing the Progressive Decoherence of the
  'Meter' in a Quantum Measurement," Phys. Rev. Lett. 77, 4887 (1996).
- S. Deleglise, I. Dotsenko, C. Sayrin, J. Bernu, M. Brune, J.-M. Raimond,
  S. Haroche, "Reconstruction of non-classical cavity field states with
  snapshots of their decoherence," Nature 455, 510 (2008); arXiv:0809.1064.
- J.-M. Raimond, S. Haroche, "Monitoring the Decoherence of Mesoscopic
  Quantum Superpositions in a Cavity," Seminaire Poincare 2, 25–64 (2005).
- K. Hornberger, S. Uttenthaler, B. Brezger, L. Hackermuller, M. Arndt,
  A. Zeilinger, "Collisional Decoherence Observed in Matter Wave
  Interferometry," Phys. Rev. Lett. 90, 160401 (2003).
- L. Hackermuller, K. Hornberger, B. Brezger, A. Zeilinger, M. Arndt,
  "Decoherence of matter waves by thermal emission of radiation," Nature
  427, 711 (2004).
- M. Arndt, S. Gerlich, K. Hornberger, "Experimental decoherence in
  molecule interferometry," arXiv:2101.08216 (2021).
- Y. Y. Fein, P. Geyer, P. Zwick, F. Kialka, S. Pedalino, M. Mayor,
  S. Gerlich, M. Arndt, "Quantum superposition of molecules beyond 25 kDa,"
  Nat. Phys. 15, 1242 (2019).
- C. J. Myatt, B. E. King, Q. A. Turchette, C. A. Sackett, D. Kielpinski,
  W. M. Itano, C. Monroe, D. J. Wineland, "Decoherence of quantum
  superpositions through coupling to engineered reservoirs," Nature 403,
  269 (2000).
- Q. A. Turchette, C. J. Myatt, B. E. King, C. A. Sackett, D. Kielpinski,
  W. M. Itano, C. Monroe, D. J. Wineland, "Decoherence and decay of
  motional quantum states of a trapped atom coupled to engineered
  reservoirs," Phys. Rev. A 62, 053807 (2000).
- L. Sun et al., "Tracking photon jumps with repeated quantum
  non-demolition parity measurements," Nature 511, 444 (2014).
- B. Vlastakis et al., "Deterministically Encoding Quantum Information
  Using 100-Photon Schrodinger Cat States," Science 342, 607 (2013).
- M. A. Ciampini, G. Pinna, P. Mataloni, M. Paternostro, "Experimental
  signature of quantum Darwinism in photonic cluster states," Phys. Rev. A
  98, 020101(R) (2018).
- T. Unden, D. Louzon, M. Zwolak, W. H. Zurek, F. Jelezko, "Revealing the
  Emergence of Classicality Using Nitrogen-Vacancy Centers," Phys. Rev.
  Lett. 123, 140402 (2019); arXiv:1809.10456.
- M.-C. Chen et al., "Emergence of classical objectivity of quantum
  Darwinism in a photonic quantum simulator," Sci. Bull. 64, 580 (2019).
- "Observation of quantum Darwinism and the origin of classicality with
  superconducting circuits," Sci. Adv. (2025); arXiv:2504.00781.
- B.-H. Liu et al., "Experimental control of the transition from Markovian
  to non-Markovian dynamics of open quantum systems," Nat. Phys. 7, 931
  (2011).

This note creates no claim promotion, prediction, paper posture, register
edit, routing change, or cross-repository authorization.
