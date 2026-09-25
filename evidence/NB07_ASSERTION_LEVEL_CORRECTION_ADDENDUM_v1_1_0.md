# NB07 assertion-level correction addendum v1.1.0

**Date:** 2026-09-23  
**Scope:** final source delta only; no new genome-wide analysis; frozen Track 1 ranking and frozen F0 primary design unchanged.

## R814H — condition-aware correction

`BUB1B NM_001211.6:c.2441G>A (p.Arg814His)`, VariationID 6764, cannot be summarized by the VCV aggregate alone.

- MVA1-specific ClinVar RCV `RCV000007160.24`: **Pathogenic/Likely pathogenic**, 4 submissions, multiple submitters, no conflicts, last evaluated 2025-06-04.
- Premature chromatid separation trait has a separate condition record. The heterozygous-carrier/trait context is not equivalent to biallelic MVA1.
- Therefore the VCV-level conflict partly reflects **condition aggregation**, not a simple P-vs-B dispute about MVA1.

Methodological implication: for recessive genes in which carrier phenotypes have their own condition records, VCV-only filtering can misclassify the evidence landscape. Final reporting must use `VCV → condition-specific RCV → SCV`.

Control implication: R814H is **not promoted into the frozen primary 11**. MVA1 assertions share clinical literature and some explicitly invoke PMID 20516114, the functional study used as the project’s circularity guardrail. Because independence from shared case/functional evidence is not clean enough for primary assay calibration, R814H is frozen as a **pathogenic-missense sensitivity/expansion control only**.

## Q467H — explicit mechanism-mismatch exclusion

`BUB1B NM_001211.6:c.1401G>T (p.Gln467His)`, VariationID 2503511, St. Jude Molecular Pathology `SCV003928079.1`, is reported Likely Pathogenic for MVA1. Assertion-level review indicates that the variant lies at the **last nucleotide of exon 10**, with predicted native donor loss and submitter internal RNA evidence supporting a splice defect.

This disqualifies Q467H from the BUB1B **cDNA protein-function validation panel**: cDNA complementation bypasses native pre-mRNA splicing and would encode Gln467His directly. A WT-like result in that assay would not contradict a splice-mediated pathogenic mechanism and could create a false “benign” assay control. Q467H is therefore an **explicit exclusion**, not a pending control.

## Privacy correction

The prior deep-research cookbook was internally inconsistent: it said non-public case alleles should not be sent to third-party endpoints but also gave remote commands containing `c.3006T>G`. Those commands are withdrawn for the case allele.

Final rule:
- no raw VCF or private genotype table to external annotation services;
- no additional remote Mutalyzer / Ensembl VEP REST / hosted SpliceAI calls for case allele `c.3006T>G`;
- any further normalization/reannotation of `c.3006T>G` must be local/offline;
- previously performed AlphaGenome use of selected case coordinates/alleles is disclosed explicitly rather than re-labelled as public-only.

## Frozen state after correction

- Track 1 ranking: unchanged.
- Primary F0V 11 controls: unchanged.
- R814H: sensitivity/expansion P/LP missense control only.
- Q467H: excluded from cDNA protein-function calibration.
- N1002K: holdout, VUS, no PS3/BS3.
- Highest-value secondary discriminator: abundance-matched N1002K.
- Function-limited secondary branch: kinetochore BUBR1 → pKARD/PP2A-B56 → alignment/SAC → missegregation.
- Computational phase remains closed; no NB08.

## Source anchors

- ClinVar R814H / MVA1: https://www.ncbi.nlm.nih.gov/clinvar/RCV000007160.24/
- ClinVar R814H / Premature chromatid separation trait: https://www.ncbi.nlm.nih.gov/clinvar/RCV000007161.16/
- ClinVar VariationID 6764: https://www.ncbi.nlm.nih.gov/clinvar/variation/6764/
- Suijkerbuijk 2010: PMID 20516114
- Frozen audit SHA256: `efe69d9e9d30a11fd9494f5bb69fdb55ae2873784a11417d8d960471d3714c72`
