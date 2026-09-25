# Environment notes

- Genome build: GRCh38.
- Variant annotation: Ensembl VEP 116, run locally/offline for the controlled WGS branch.
- Python notebooks were developed in a Colab-compatible Python 3 environment.
- `requirements.txt` is a **reference reproduction lock prepared on 2026-09-25**. The original Colab runtimes were not preserved as a forensic `pip freeze`, so the file must not be interpreted as a byte-exact historical environment capture.
- `torch` + `transformers` are required by NB04B because it uses the public `facebook/esm2_t30_150M_UR50D` ESM2 masked-language model for a BUBR1-specific predictor-calibration audit. This supporting branch does not determine the frozen Track 1 ranking.
- `alphagenome==0.9.0` is included for NB04C, an orthogonal RNA/cis-regulatory mechanism audit using the Google DeepMind AlphaGenome API.
- Set `MVA_ROOT` to an authorized local/project root before running notebooks that expect controlled inputs.
