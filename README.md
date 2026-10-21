# FP4 stochastic rounding numerical artifact

Version 0.1.0 is a curated supporting artifact for the working manuscript
**Bit-Exact FP4 Stochastic Rounding — Correction Elimination and Precision Boundaries**.
It is an artifact version, not a submission, acceptance, DOI or publication-priority claim.

The supported scalar contract is finite BF16 input, group size 32,
`s = RN32(amax/6)` with nearest-even rounding and gradual underflow, the
unchanged zero fallback `2^-42`, E2M1, and a fixed 32-bit probability lattice.
Virtual nearest-even precision ranges from 35 to 64 significant bits with
binary64 exponent range. The retained evidence gives normal-scale boundary
45 and full-domain boundary 49, with legal failures at 44 and 48.
These are analytic reductions plus complete finite certificates; no pure
symbolic theorem, proof-assistant check or native 45/49 kernel is claimed.

## Start here

With an existing Python 3.9 or newer, from this directory:

```text
python tools/verify_artifact.py
```

This command verifies file bytes, reference closure, JSON/CSV readability and
Python syntax without importing numerical modules, running a certificate,
installing dependencies, contacting a service or using a GPU. Read
[REPRODUCTION.md](docs/REPRODUCTION.md) before optional numerical verification.
No numerical verifier or historical experiment was replayed to prepare this version.

## Contents

| Path | Evidence and scope |
|---|---|
| `normal45/` | Complete 2,814-branch certificate, 236 recorded coarse candidates, written reduction, unchanged verifier, historical fixed checks and algebra review |
| `subnormal49/` | Complete 4,656-branch certificate, one relaxed survivor, written reconstruction exclusion and unchanged verifier |
| `independent_r49/` | Frozen non-blind direct-j branch summary, historical results and comparison; no new enumeration |
| `witnesses/necessity_witnesses.json` | Selected legal b32 failures at p44 and p48, including both threshold values |
| `performance/historical_nvl_performance.csv` | All 72 retained NVL summary rows, including unfavorable strong-baseline comparisons |
| `historical_cpu/main_result.json` | Original 532,701,120-pair report, historical and not replayed here |
| `source_semantics/` | Historical scalar source bridge under stated primitive semantics; underlying CUDA bodies are not redistributed |
| `PROVENANCE.json` | Byte identities and the explicit witness-record selection |

See [SCIENTIFIC_SCOPE.md](docs/SCIENTIFIC_SCOPE.md),
[HISTORICAL_PERFORMANCE.md](docs/HISTORICAL_PERFORMANCE.md),
[EVIDENCE_STATUS.json](docs/EVIDENCE_STATUS.json), and
[OMISSIONS.json](docs/OMISSIONS.json).

Historical prose is preserved with its original date and evidence scope.
References within that prose to original directories, files, run outputs or
code do not imply that those materials are present here. The content table,
manifest and omissions register define this version's actual contents.

## What the result does not establish

The strongest scalar FP64 baseline A-double-prime is faster than D1 on ordinary
and Gaussian conditions in the historical sessions. A gain over corrected
integer B is not a public-library win, proof of a hardware requirement or a
runtime-causality result. Native GPU execution artifacts are unavailable in
this package. Closest-theory derivability and publication novelty remain open.
A separately prepared independent normal checker remains unexecuted and is
not bundled; the retained normal review covers algebra and supplied eta cases.

No manuscript PDF/DOCX, private history, operational archive records,
credentials, private machine identifiers, third-party full texts, CUDA/Philox
implementation snapshots, weights, text inputs or raw model arrays are included.
No open-source reuse license is selected for this initial artifact candidate;
read [LICENSE_STATUS.md](LICENSE_STATUS.md).
