# Rare Disease, Real Kid: MVA Hackathon 2026 — Track 1 Final Report v1.2.0

**Hugging Face username:** `kotgienia`

## Variant-pair prediction from 5.0 million WGS records to one robust BUB1B pair

**Frozen submission CSV:** unchanged from v1.1.0.  
**Rank 1:** `BUB1B` L737* + N1002K.  
**Interpretation:** leading research pair, not a resolved molecular diagnosis.

## 1. Result in one paragraph

The pipeline started from **5,012,204 WGS VCF records** and processed the genome locally with **Ensembl VEP 116, GRCh38, offline**. Transcript/gene expansion produced **6,608,298 allele–gene rows** spanning 5,010,482 unique carried alleles and 40,804 represented genes. The exact counting formulas and frozen values are preserved in `evidence/NB01B_COUNT_PROVENANCE_v1_0_0.json`; the sanitized notebook retains the counting code but intentionally strips execution outputs. Consequence, rarity, genotype quality, phenotype context and same-gene two-hit logic reduced this to **856 plausible variants in the pair pool**, from which **458 candidate pairs** were constructed. `BUB1B` L737* + N1002K ranked **#1 with the curated MVA prior and #1 after removing that prior**, showing that the result was not produced merely by seeding BUB1B. The final competition file contains **7 rows**, with the BUB1B pair first.

`5,012,204 VCF records → 6,608,298 allele–gene rows → 856 pair-pool variants → 458 candidate pairs → BUB1B rank 1 → 7 submitted rows`

## 2. Phenotype entered the ranking explicitly

Eight HPO terms were recovered locally from the supplied clinical phenotype document without exporting the full narrative:

- `HP:0000121` — Nephrocalcinosis
- `HP:0001508` — Failure to thrive
- `HP:0001518` — Small for gestational age
- `HP:0001622` — Premature birth
- `HP:0002859` — Rhabdomyosarcoma
- `HP:0003202` — Skeletal muscle atrophy
- `HP:0004322` — Short stature
- `HP:0200067` — Recurrent spontaneous abortion

The phenotype component was calculated independently of the manual MVA-gene prior. HPO gene annotations were propagated through the HPO ancestor graph and compared with the eight case terms using an information-content/Resnik-style best-match score. `BUB1B` received an HPO gene score of **0.233693**. A separate MVA prior was then added for established/reported MVA genes (`BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1`) but was not a filter: any gene could outrank the MVA genes through phenotype and variant evidence.

As a falsification test, the MVA prior was removed after pair construction. The leading L737*/N1002K pair remained **rank 1**, with pair score **5.379271** before removal and **4.029271** after removal.

## 3. Why L737* + N1002K won

The top pair combines:

- a severe `stop_gained` allele, L737*;
- a rare missense allele, N1002K;
- strong technical support at both loci;
- same-gene recessive compatibility;
- phenotype support for `BUB1B`;
- robustness to deletion of the curated MVA prior.

N1002K remains a VUS. Its pathogenicity and molecular mechanism are not assumed from its computational scores. The rank reflects evidence that this is the most informative pair to test, not a clinical pathogenicity verdict.

## 4. Phasing was attempted and quantitatively bounded

The target alleles are **10,911 bp apart**.

The initial VCF-level phase audit found both variants as simple heterozygotes but no shared interpretable `PGT/PID` block. A later local read-backed phase attempt identified only **three heterozygous variants across the 10,911-bp interval**: the two target alleles plus one intervening heterozygous site. The two gaps required to bridge the targets were **6,769 bp** and **4,142 bp**. Both exceeded the effective read-pair span available from the library, so no molecule/read-pair chain connected the alleles. No common `PGT/PID` phase block bridged them.

Therefore the correct state is:

**`PHASE_UNRESOLVED`**

This is not missing analysis. It is a measured information limit of the available short-read data. The highest-value next experiment is parental genotyping/Sanger of the two BUB1B loci.

## 5. Confidence calibration and EPCR

The rank-1 submission uses **EPCR = 0.78**, deliberately below a near-certain value such as 0.95.

Why 0.78:
- the pair is rank-stable with and without the MVA prior;
- L737* is a credible loss-of-function anchor;
- N1002K remains a VUS;
- cis/trans phase is unresolved;
- no direct N1002K functional assay exists yet.

EPCR therefore expresses strong confidence that this is the **best pair to test**, while preserving material uncertainty about whether it is truly causal.

## 6. Why all submitted rows are primary, not secondary

The final CSV contains no `secondary` finding.

This is intentional. Nephrocalcinosis created a plausible phenotype mismatch, so a separate frozen **30-gene nephrolithiasis/nephrocalcinosis coding/splice screen** was performed. It produced **0 coding/splice candidates after the preregistered filters**. That negative screen does not prove nephrocalcinosis is caused by MVA, and it does not exclude CNV/SV, deep-intronic/regulatory, mtDNA or acquired/prematurity-related explanations. It does mean there is no evidence-backed second monogenic coding/splice finding to submit as `secondary`.

The remaining rows in Track 1 are lower-confidence **primary-cause fallback pairs**, not claims of additional diagnoses.

## 7. Assertion-aware source verification — relevant to interpretation, not ranking

A final ClinVar audit did not change the Track 1 ordering, but it prevented two interpretation errors.

For `BUB1B` R814H, the VCV aggregate is conflicting because it combines condition-specific assertions. The MVA1 RCV is Pathogenic/Likely pathogenic with multiple submitters and no conflicts, whereas a Likely benign assertion belongs to the distinct *Premature chromatid separation trait*. This demonstrates why recessive-disease interpretation should descend from VCV to disease-specific RCV and SCV context.

For Q467H, a Likely pathogenic MVA1 submission is mechanistically splice-mediated: the change affects the last nucleotide of an exon and the submitter reports RNA evidence of splice disruption. A cDNA complementation assay would bypass that disease mechanism. This matters for the downstream functional study, but it is not used to retroactively tune the Track 1 rank.

Full assay-control curation and drug-rescue design are therefore reported in **Track 2**, not expanded here.

## 8. What the result means now

**Supported:** L737* + N1002K is the strongest research candidate pair in this WGS analysis.  
**Unresolved:** phase and direct N1002K function.  
**Next cheapest decisive test:** genotype both variants in both biological parents.

Different parental origin would support trans configuration. Same-parent inheritance would support cis and would reopen the second-allele search. Neither outcome should be guessed from the present short-read data.

## 9. Reproducibility and privacy

- Ensembl VEP 116 used locally/offline on GRCh38.
- Raw WGS, sample identifiers and genotype-scale intermediate tables remain private.
- Public artifacts contain only sanitized results needed to reproduce the analytical logic.
- The non-ClinVar case allele `c.3006T>G` is not sent to additional remote variant-annotation endpoints.

## 10. AI and external-model disclosure

**OpenAI ChatGPT (Plus)** was used for **code review and literature evaluation** on sanitized/public project materials. **No private patient data, raw WGS/VCF, private genotype tables, or private identifiers were provided to or read by ChatGPT. Improve the model for everyone: Off**

**Google DeepMind AlphaGenome** was used through the official API/client in NB04C for an orthogonal RNA/cis-regulatory mechanism audit of the two already-public BUB1B candidate variants, L737* and N1002K. No raw WGS/VCF, genome-wide genotype table, sample identifier, or private genotype dataset was sent to AlphaGenome. The AlphaGenome branch did not determine or alter the frozen Track 1 ranking.

NB04B also used the public `facebook/esm2_t30_150M_UR50D` **ESM2** model locally through `torch`/`transformers` for BUBR1 predictor calibration on the public canonical protein sequence and public substitutions.

The final submitted predictions and analytical artifacts remain independently auditable in this repository.

## Conclusion

The central Track 1 result is quantitative and robust:

**5,012,204 records → 458 candidate pairs → one BUB1B pair that remains rank 1 after removal of the MVA prior.**

The remaining uncertainty is not hidden inside the rank. It is localized to two experimentally resolvable questions: **phase and N1002K function**.
