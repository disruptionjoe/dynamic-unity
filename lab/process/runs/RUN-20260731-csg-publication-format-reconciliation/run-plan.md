---
artifact_type: run_plan
run_id: RUN-20260731-csg-publication-format-reconciliation
owner_id: dynamic-unity
run_type: progress
mode: execute
lane_id: "7"
status: complete
created: 2026-07-31
starting_revision: 89d1b28e156c
---

# CSG publication-format reconciliation

## Objective

Reconcile Dynamic Unity's sole mutable publication state to the trusted
Drafting Factory and Zenodo outcome for `DU-PAPER-013`, while preserving the
source theorem, evidence grade, and all scientific boundaries unchanged.

## Cold-start contract

- **Purpose and North Star:** make physical reality intelligible as one
  evidence-accountable whole; the North Star remains open and no scientific
  flagship is activated by this publication reconciliation.
- **Evidence boundary:** the CSG paper remains a scoped Grade-4 classical
  asymptotic theorem conditional on a supplied coupling-tail class. Publication
  and typesetting do not promote its scientific grade.
- **Current program:** no scientific flagship is executable; the only stale
  WIP is the publication program still marked prepared after the trusted
  Zenodo posting.
- **Completed evidence:** source proof, collision, hostile hardening, and 18
  deterministic controls remain frozen at `30aaf36`.
- **Lane/channel:** Lane 7 / CH-PAPER, maximum Grade 4. Strongest absorber is
  standard regular-variation and discrete-saddle analysis; cheapest kill is a
  proof gap or exact prior-art absorber.
- **Stop:** make no theorem, hypothesis, citation, or source-evidence change.
- **Durable output:** one exact `CURRENT-RESEARCH.yaml` state correction and
  this receipt.
- **Dependencies:** Drafting Factory and Zenodo outcome are external custody
  evidence for publication status only, not scientific evidence.
- **Local-model/hardware:** not applicable.

## Authorized change

1. Mark `DU-PAPER-013-HARDENING` complete with no active publication WIP.
2. Record Zenodo v0.2.0 and the typesetting-only v0.2.1 correction path under
   Drafting Factory custody.
3. Clear `prepared_publication_program_id`.
4. Increment the sole mutable state revision and validate governance.

## Completion

- `CURRENT-RESEARCH.yaml` advanced from revision `143` to `144`.
- `DU-PAPER-013-HARDENING` is complete with no execution or publication WIP.
- Zenodo v0.2.1 is public at <https://zenodo.org/records/21724178> under
  concept DOI `10.5281/zenodo.21719900`.
- Drafting Factory custody records the original v0.2.0 publication and the
  typesetting-only v0.2.1 correction. The scientific theorem, hypotheses,
  evidence grade, source revision, and reproducibility controls are unchanged.
- The public record uses the compiled PDF as its default preview and retains
  TeX and Markdown as source artifacts.

## Verification

- Zenodo public record and API: published, version `0.2.1`, Joseph Hernandez,
  Independent Researcher, Preprint, CC BY 4.0, repository URL present.
- Public PDF SHA-256 equals the local packaged PDF SHA-256:
  `e311f37b568ba85170a7479ae482de7fcc61f7da9dd2ecdae01f9a2a7c4b9707`.
- Draft 2020-12 JSON Schema validation: **PASS**.
- `CURRENT-RESEARCH.yaml` semantic-governance probe: **PASS 37/37**;
  5,997 cold-start words against the 6,000-word ceiling.
- Governance-selection CSG probe: **PASS**; its scientific artifact is
  unchanged by this publication reconciliation.
- `git diff --check`: **PASS**.
