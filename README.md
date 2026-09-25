# MVA Hackathon 2026 — Track 1 (`kotgienia`)

Privacy-filtered, reproducible code and submission artifacts for **Track 1 — Variant Prediction**.

This repository and its participant-created submission artifacts are released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license; see `LICENSE`.

## Frozen result

Top research pair: **BUB1B L737* + N1002K**. The pair remained rank 1 after removal of the curated MVA-gene prior. Phase remains unresolved and N1002K remains a VUS pending direct functional evidence.

## Submission files

- `submission/kotgienia_mva-mechanism-first.csv` — frozen 7-row competition CSV.
- `submission/kotgienia_track1_report.md` — final Track 1 methods/report, v1.2.0 content with current AI-assistance disclosure.

## Reproduce the submitted CSV

```bash
python scripts/build_submission.py
python scripts/validate_submission.py
```

The first command regenerates the submission from the frozen public config. The second validates row count, schema, EPCR range/order and the frozen top pair.

## Repository structure

- `notebooks/` — sanitized Track 1 analytical notebooks; outputs, execution history and Colab user metadata removed.
- `config/` — frozen public submission state.
- `scripts/` — deterministic submission builder and validator.
- `evidence/` — public assertion-level correction/audit artifact.
- `docs/` — environment, reproducibility, privacy and AI-assistance notes.
- `submission/` — files intended for the Hackathon Track 1 form.


## Environment and model dependencies

Install the pinned reference environment with `pip install -r requirements.txt`. The pins are a 2026-09-25 reproduction lock, not a claim that the original Colab runtime was historically frozen package-for-package.

Why `torch` and `transformers` are present: **NB04B uses the public `facebook/esm2_t30_150M_UR50D` ESM2 model** to compute masked-marginal amino-acid scores during a BUBR1-specific predictor-calibration audit. That branch is supporting mechanism analysis and does not create the frozen Track 1 ranking. `alphagenome` is used only in NB04C for an orthogonal RNA/cis-regulatory mechanism audit.

## Privacy

No raw patient WGS/VCF, genotype-scale private tables, identifiers, credentials, private blinding keys, or Google Drive file IDs are included. See `docs/REPRODUCIBILITY_AND_PRIVACY.md`.

## AI assistance

**OpenAI ChatGPT** (Plus) was used for **code review and literature evaluation** on sanitized/public project materials. No private patient data were provided to or read by ChatGPT.

Google DeepMind **AlphaGenome** was used through the official API/client in NB04C for an **orthogonal RNA/cis-regulatory mechanism audit** of the two already-public BUB1B candidate variants (L737* and N1002K). No raw WGS/VCF, genome-wide genotype table, sample identifier, or private genotype dataset was sent to AlphaGenome. This branch was used for mechanism triage only and **did not determine or alter the frozen Track 1 ranking**.

**ESM2** NB04B used the public Hugging Face model `facebook/esm2_t30_150M_UR50D` locally through `torch`/`transformers` to calculate masked-marginal amino-acid scores for predictor calibration. It operated on the public canonical BUBR1 protein sequence and the public comparator/target substitutions, not on the private genome.
