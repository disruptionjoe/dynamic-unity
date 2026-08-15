# Phenomenon-to-Capability Atlas lab

`atlas-v0.1.json` is the frozen machine-readable bundle for the completed,
non-routing six-specimen pilot. It separates immutable source bindings from
Dynamic Unity–owned overlays and is validated against
`../../specs/phenomenon-capability-atlas-v0.1.schema.json` plus semantic and
hostile-mutation checks in
`../../tests/du_phenomenon_capability_atlas_probe.py`.

The bundle is not an exhaustive phenomena catalog and has no executable
continuation. `../../CURRENT-RESEARCH.yaml` remains the sole routing authority.
Do not edit v0.1 in place after publication; create a new schema/bundle version
with an explicit denominator and migration rule.

The additive v0.2 first-run release is frozen by `release-v0.2.json`. Its
denominator-agnostic card instance is
`cards-v0.2/du-xenon-s1-s2.json`; its source-first comparison is
`reviews/xenon-s1-s2-independent-remap-v0.2.json`; and its cross-repository
vertical specimen is
`compositions/gu-record-capability-first-run-v0.2.json`. The release contains
one remapped existing card only. It neither changes the v0.1 six-card
denominator nor authorizes a seventh phenomenon.

The four v0.2 schemas live in `../../specs/`. The deterministic, stdlib-only
validator and hostile controls are in
`../../tests/du_phenomenon_capability_atlas_v02_probe.py`. Passing establishes
schema, binding, review, composition, and declaration consistency only; it does
not independently validate the source physics or move any source grade.
