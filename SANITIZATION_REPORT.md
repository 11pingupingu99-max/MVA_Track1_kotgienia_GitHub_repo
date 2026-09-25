# Sanitization report

Release target: Track 1 public repository for HF user `kotgienia`.

Checks performed:

- stripped all Jupyter cell metadata, execution history, output IDs and outputs;
- retained only minimal non-identifying Python kernelspec/language metadata;
- replaced the original absolute Google Drive project root with a configurable `MVA_ROOT` placeholder;
- excluded Track 2 notebooks/artifacts from this Track 1 repository;
- excluded internal source-Drive-ID/provenance files from the previous release candidate;
- scanned text/code for Google Drive URLs, account-specific Drive roots, credential-like assignments and embedded secrets;
- normalized text files to UTF-8/LF;
- generated SHA-256 manifests;
- packaged ZIP entries with deterministic timestamps and permissions;
- generated a PDF report and removed document-information/XMP metadata (no author, creator, producer or creation-date fields remain);
- added a full CC BY 4.0 `LICENSE`, pinned reference dependencies, controlled-data deletion plan, AlphaGenome/ESM2 disclosure and explicit NB01B count provenance.

Private case data are not included. References in code/documentation to controlled inputs describe required inputs only. The organizer deletion-confirmation email is intentionally present in `notes/DELETION_PLAN.md`.

## Verification result

**PASS.** Strict release scan found no account-specific Google Drive paths/URLs, Google Drive file IDs, Colab execution metadata (`executionInfo`, `outputId`, `displayName`, `user_tz`), or literal embedded secrets. All 13 public notebooks have zero outputs, zero execution counts and empty cell metadata. The final PDF has no document metadata dictionary fields.
