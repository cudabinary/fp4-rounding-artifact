# Reproduction levels

## Executed for this candidate: file and structure verification only

```text
python tools/verify_artifact.py
```

Expected status: `PASS_ARTIFACT_IDENTITY_AND_STRUCTURE`.
This reads the public manifest, hashes all artifact files, parses JSON/CSV and
Python ASTs, and checks recorded row counts. It does not execute mathematical
or stochastic-rounding functions. Content identity does not prove correctness.

## Optional certificate checks: instructions, not a new run receipt

In a separate disposable copy, using an already available Python 3.9+:

```text
python tools/verify_artifact.py
python normal45/normal45_certificate_verifier.py
python subnormal49/certificate_verifier.py
```

The verifier sources are byte-identical to the retained research sources.
Their historical expected statuses are `PASS_COMPLETE_NORMAL45_REDUCED_CERTIFICATE`
and `PASS_COMPLETE_REDUCED_CERTIFICATE`. Their mathematical coverage still
depends on the respective written reductions. This packaging task does not
claim to have replayed either check or independently replicated their results.

The original per-study payload manifests also bound private or omitted files.
Those manifests are deliberately absent. The unchanged verifier's optional
per-study hashing block therefore does not run; use the root manifest command
first to check the actual public inputs. This is a packaging boundary, not
a silent claim of identity for excluded historical files.

The independent R49 directory contains historical records and branch summaries.
The direct-j enumerator and original every-j ledger are not included, so this
candidate provides no fresh direct-j enumeration recipe or full-ledger identity
claim. No independent normal enumeration is bundled or executed.

## Historical GPU and original large CPU campaign

No verified fresh-machine native-GPU reproduction recipe is supplied. Exact
executed cubins, loaded-symbol bindings, compiler logs, full harness and native
arrays are missing. A substitute build would be a new experiment, not recovery
of the old execution. The NVL CSV contains already-computed estimates, not
raw timing samples for a new bootstrap. SXM observations are separate.

The original 532,701,120-pair CPU report is retained as a historical report.
Its exact archived scale-bit input, complete harness and environment are not
distributed here. There is no command in this package to replay that campaign.
No dependency installation, GPU query, compile, timing or resampling is part
of the quickstart.
