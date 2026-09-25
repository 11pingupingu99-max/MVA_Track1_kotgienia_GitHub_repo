# Controlled-data deletion plan

**Hackathon close:** 2026-10-24 23:59 UTC  
**Deletion deadline (30 days after close):** **2026-11-23 23:59 UTC**

This plan applies to systems under the participant's control. It follows the organizer clarification that the genome-carrying material must be deleted while scientific findings/code may be retained.

## DELETE by the deadline

- source VCF, BAM and CRAM files and their index files;
- controlled source clinical files supplied with the challenge (conservative deletion even though HPO findings may be retained);
- any copy, subset, slice or reformat of those files;
- filtered/annotated genome-scale variant or genotype tables and private parquet/CSV intermediates;
- caches, temporary files and notebook/runtime state containing genotype-scale patient data;
- stored prompts/logs under participant control containing pasted blocks of controlled variant data (none are expected for ChatGPT in this project because private data were not provided to ChatGPT);
- any model weights, embeddings or fine-tunes trained directly on raw genomic data (none are expected in this Track 1 workflow);
- controlled copies in local machines, Colab runtimes, cloud instances, Google Drive/private project storage, private repositories and other participant-controlled storage.

## KEEP

- ranked candidate submission list;
- HPO terms;
- gene/pathway rankings and mechanism analyses that do not reconstruct genome-scale genotypes;
- sanitized code, reports, public evidence artifacts and leaderboard/submission records.

## Completion record

After deletion, perform a second search for `.vcf`, `.vcf.gz`, `.bam`, `.cram`, index files and private genotype-scale tables across all controlled storage. Record the completion date and environments checked. Then email **RarediseaserealkidMVAhackathon2026@synapse.org** confirming deletion.

Status: `PENDING - execute after Hackathon close and no later than 2026-11-23 23:59 UTC`.
