# AI and external model assistance disclosure

## OpenAI ChatGPT

OpenAI ChatGPT (Plus) was used for **code review and literature evaluation** on sanitized/public project materials. **No private patient data, raw WGS/VCF, private genotype tables, or private identifiers were provided to or read by ChatGPT.**

## Google DeepMind AlphaGenome

Google DeepMind **AlphaGenome** was used through the official API/client in NB04C for an **orthogonal RNA/cis-regulatory mechanism audit** of the two already-public BUB1B candidate variants (L737* and N1002K). No raw WGS/VCF, genome-wide genotype table, sample identifier, or private genotype dataset was sent to AlphaGenome. This branch was used for mechanism triage only and **did not determine or alter the frozen Track 1 ranking**.

## ESM2

NB04B used the public Hugging Face model `facebook/esm2_t30_150M_UR50D` locally through `torch`/`transformers` to calculate masked-marginal amino-acid scores for predictor calibration. It operated on the public canonical BUBR1 protein sequence and the public comparator/target substitutions, not on the private genome.
