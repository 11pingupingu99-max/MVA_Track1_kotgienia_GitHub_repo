# NB01B count provenance v1.0.0

The public notebook intentionally has execution outputs stripped for privacy/metadata hygiene, so these frozen summary counts are persisted separately with their exact counting semantics.

| Metric | Frozen value | Counting trace |
|---|---:|---|
| input VCF records | 5,012,204 | NB01A preflight value consumed by NB01B |
| carried allele-gene rows | 6,608,298 | `len(variants)` after carried-allele parsing and VEP transcript/gene expansion |
| unique carried alleles | 5,010,482 | `variants["variant_key"].nunique()` |
| represented genes | 40,804 | `variants["gene"].replace("", np.nan).nunique()` |
| pair-pool variants | 856 | frozen NB01B run |
| candidate pairs | 458 | frozen NB01B run |

The sanitized NB01B notebook now assigns these metrics to named variables, asserts the frozen expanded-table values, prints them on rerun, and persists `n_unique_carried_alleles` and `n_represented_genes` alongside `n_carried_allele_gene_rows` in `NB01B_HANDOFF.json`. No genome-scale patient table is included in this repository.
