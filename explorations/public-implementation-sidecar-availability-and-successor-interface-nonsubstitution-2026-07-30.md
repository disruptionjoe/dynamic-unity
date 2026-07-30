---
title: "Public implementation-sidecar availability and successor-interface non-substitution"
status: banked_scoped_result
doc_type: exploration_result
created: 2026-07-30
claim_id: HC-DU-171
run_id: RUN-20260730-161103-public-sidecar-availability-audit
evidence_grade: 4
---

# The remaining QEC implementation sidecar is an external-custody dependency

## Executive result

A bounded audit found no overlooked public implementation sidecar for the
Riverlane/Rigetti real-time QEC experiment.

The audit covered:

- the final Nature Communications article and its 13-page supplement;
- the single Zenodo record version and all 18 deposited files;
- the official public-repository inventories of Riverlane and Rigetti;
- source scans of the five Riverlane repositories whose names, dates, or
  descriptions made them plausible candidates; and
- the later QECi standard and open QECIPHY implementation.

The final article points to the Zenodo data deposit but has no code-availability
statement. The supplement describes the proprietary-assembly workflow and
prototype compiler but contains no embedded file. Zenodo contains HDF5, CSV,
and text data only. No exact experiment program, compiler source, assembly,
binary, firmware, configuration digest, per-attempt control log, or archive
lineage was found on the frozen public surfaces.

This closes a local-search ambiguity:

```text
possibly overlooked public artifact  -> bounded search complete
remaining exact sidecar               -> external custody
later open generic interface          -> useful future platform
                                      -> not a historical repair
```

Disposition:

```text
BOUNDED_PUBLIC_SIDECAR_SEARCH_COMPLETE
+ NO_EXACT_EXECUTABLE_OR_LINEAGE_SIDECAR_FOUND
+ EXTERNAL_CUSTODY_DEPENDENCY_CONFIRMED
+ LATER_OPEN_INTERFACE_NOT_HISTORICAL_REPAIR
+ PUBLIC_SEARCH_STOP
+ NO_READY_SUCCESSOR
```

This is a scoped Grade-4 evidence-availability and necessity boundary. It is
not proof that no private artifact exists, proof of global internet absence,
an evaluation of the experiment, a physical remainder, or new physics.

## 1. Frozen public surfaces

### 1.1 Final article and supplement

The version of record is
[Caune et al., “Demonstrating real-time and low-latency quantum error
correction with superconducting qubits”](https://doi.org/10.1038/s41467-026-73331-6),
Nature Communications 17, 7383 (2026).

The article's data-availability statement points only to Zenodo concept DOI
`10.5281/zenodo.13961129`. No code-availability section appears. Its methods
state that:

- pyQuil programs were compiled into program binaries with waveforms and
  proprietary assembly;
- a prototype compiler injected the real-time-decoding instructions; and
- production translation-stack features were authored for the integration.

Thus experiment-specific software existed. Description of its role is not
release of its identity or contents.

The final supplementary PDF is pinned by:

```text
SHA256  e5f2ef9eabd2831d85daa74569cf95175d114a97c2a127e41d9e32f2c9f2cd95
pages   13
embedded files   none
```

Visual and text inspection confirms the same descriptive workflow recovered
by `HC-DU-170`: proprietary assembly, decoder setup, buffering, packet
formation, polling, and conditional feedback. It provides no code link or
executable attachment.

### 1.2 Zenodo

The concept DOI resolves to concrete record `15364358`, updated
2025-05-08. The exact 18-file inventory consists of:

- four raw HDF5 packets;
- decoder-timing and figure CSVs; and
- logical-error, defect-rate, and timing text files.

It contains no source-code, Quil/QASM, assembly, binary, bitstream, firmware,
configuration, program-digest, controller-log, attempt-census, or
archive-lineage member. The already audited
`fast_feedback_raw_data.h5` remains pinned by MD5
`3b2503a80f2b92916660489e2f07e880`.

### 1.3 Official public repositories

At the frozen audit time, Riverlane exposed 13 public repositories and Rigetti
59. Their official name/description inventories contain no exact paper title,
arXiv identifier, dataset filename, experiment companion, or prototype
compiler.

Five Riverlane repositories were source-scanned because they were the
plausible interface, QEC, data, or post-paper candidates:

```text
QHAL                    e61b9b80e5a54f277cb65854f62a51c23981ec62
QStone                  3aa26d5b45ecf282438d5d4eb68b84dae1574aeb
soft_information_models 25f493206c210d53a954539859d76b6d7ca3db79
qeciphy                 a88289e25f1511ffc75959478799632eea2123b7
ACID                    801b2ab41d2ee2a6f78f8b7624335c003b2bb81b
```

No exact paper identifier, title, HDF5 filename, Ankaa-2 companion,
Collision-Clustering implementation, or prototype compiler appeared in that
bounded scan. The remaining Riverlane repository names and descriptions are
plainly unrelated educational, chemistry, chip-verification, or historical
projects. The Collision-Clustering paper and article citation expose the
algorithm and hardware-performance description, not this experiment's
decoder image or compiler.

This is a bounded primary-surface result. It must not be restated as
“the files do not exist anywhere.”

## 2. QECi/QECIPHY is a future platform, not a retroactive sidecar

Riverlane introduced
[QECi](https://www.riverlane.com/get-qec-ready/qeci) on 2025-03-06. It defines
data formats, runtime states, parameters, and communication conventions for
control-system/QEC-stack interoperability. Riverlane lists Rigetti as an
adopter.

The open
[QECIPHY repository](https://github.com/riverlane/qeciphy) was created on
2025-10-11. It implements a generic FPGA-to-FPGA physical layer with an
AXI4-Stream interface, link management, packet error checks, status, and
fault signals.

That is valuable to Dynamic Unity in a different role:

- it is a candidate future co-design surface for preserving message, status,
  error, reset, and attempt lineage;
- it shows that more implementation-visible QEC experiments are practical;
  and
- it may reduce the cost of a future implementation-complete packet.

It does not identify the historical Ankaa-2 proprietary program, FPGA image,
controller state, or archive. No source-pinned mapping, contemporaneous
digest, or replay certificate connects the open successor to the 2024
experiment.

## 3. Successor-interface non-substitution

Let:

- \(i\in\mathcal I_{\mathrm{hist}}\) be a historical implementation;
- \(p(i)\) be its retained passport;
- \(q(i)\) be the view exposed through a later generic interface; and
- \(T(i)\) be the held-out implementation target.

Suppose two historical implementations satisfy

\[
q(i_0)=q(i_1),\qquad T(i_0)\ne T(i_1).
\]

Then a later artifact implementing \(q\) cannot make \(T\) constant on the
historical fibre. Repair requires a source-pinned identity map or certificate
\(m\) such that

\[
(p(i),m)\quad\text{identifies the historical target class.}
\]

Functional compatibility with a successor protocol is insufficient. This is
ordinary provenance, software-supply-chain identity, and reproducibility
mathematics applied to Dynamic Unity's implementation fibre; it is not a new
general theorem.

The compact control preserves one later interface view while changing the
historical executable identity, route state, and held-out actuation target.
It therefore proves only the logical nonimplication:

```text
later interface compatibility
  != contemporaneous historical implementation identity
  != historical event lineage
```

## 4. What changes for the North Star

The main scientific target does not reopen.

`HC-DU-168` established a strong returned-shot physical packet.
`HC-DU-169` separated action from resource/timing finality.
`HC-DU-170` recovered the descriptive controller workflow and made
implementation completeness target/fault-relative.
`HC-DU-171` now establishes that the remaining exact lineage is not recoverable
from the bounded public release surfaces.

The result is useful because it prevents two kinds of wasted work:

1. repeated searches for the same absent public sidecar; and
2. treating a later open protocol as if it retroactively supplied the
   historical experiment's provenance.

The public QEC specimen is exhausted at its honest ceiling. Further progress on
this specimen requires new custody, not more local inference.

## 5. Exact stop and reopener

Stop public searching after this audit. Do not:

- infer proprietary program state;
- reconstruct a plausible compiler and call it the historical one;
- run more simulations of the known returned-shot kernel;
- substitute QECi/QECIPHY compatibility for event identity; or
- contact authors, laboratories, providers, or hardware owners without new
  authorization.

Reopen only if one of these changes:

1. an author or institution releases an experiment-specific executable,
   configuration, control-log, attempt-census, or archive-lineage artifact;
2. a source-pinned digest/mapping connects a later open implementation to the
   historical run; or
3. a future co-designed experiment provides the frozen
   target/fault/environment-complete passport required by `HC-DU-170`.

## 6. Grade and absorbers

- **Grade:** scoped Grade 4 for a source-pinned availability closure,
  external-custody boundary, and historical non-substitution necessity.
- **Strongest absorbers:** reproducible-build identity, software bills of
  materials, event sourcing, database provenance, fault diagnosis, and
  experimental reproducibility.
- **Not earned:** private or global absence, fraud or defect inference,
  physical remainder, unique material archive, ontology, law, prediction, or
  new physics.

## Durable regression

`tests/du_public_sidecar_availability_audit.py` pins the public metadata,
supplement hash, archive inventory, relevant repository commits, bounded
source scan, and successor non-substitution twin. Raw external files and
repository clones are not committed.
