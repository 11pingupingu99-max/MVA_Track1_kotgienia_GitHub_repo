# Reproducibility and privacy

This repository is the public, privacy-filtered Track 1 release for the **Rare Disease, Real Kid: MVA Hackathon 2026** submission by HF user `kotgienia`.

## Data boundary

The repository does **not** contain raw WGS/VCF, BAM/CRAM, genotype-scale private tables, patient identifiers, private blinding keys, credentials, tokens, or Google Drive file IDs. `PROBAND01` is the project pseudonym used in the competition submission.

Core genome analysis was performed locally/offline on controlled case data. Public notebooks retain analytical code but not patient-level inputs or execution outputs. Private-data paths in code are logical placeholders only; the original account-specific Drive root has been removed and replaced by the `MVA_ROOT` environment variable with a non-functional placeholder default.

## AI and external model boundary

OpenAI ChatGPT (Plus) was limited to code review and literature evaluation on sanitized/public materials and did not receive or read controlled patient data. Google DeepMind AlphaGenome was used only on the two already-public named BUB1B candidate variants for an orthogonal RNA-mechanism audit; it did not receive raw WGS/VCF or genome-scale genotype data. ESM2 in NB04B ran on the public BUBR1 protein sequence and public substitutions. See `docs/AI_ASSISTANCE_DISCLOSURE.md`.

## Reproduction layers

1. **Competition-file reproduction:** `python scripts/build_submission.py` regenerates the frozen 7-row CSV from `config/frozen_track1_candidates.json`.
2. **Schema validation:** `python scripts/validate_submission.py` checks the current Track 1 field constraints, EPCR range/order, row count, and frozen top pair.
3. **Full case-analysis reproduction:** requires authorized access to the controlled WGS inputs and external resources described in the notebooks; those data are intentionally not distributed here.
