# MVA NB05A3 — F0 split-assay implementation freeze v1.0.2

Status: **IMPLEMENTATION_ARCHITECTURE_FROZEN_AWAITING_F0_DATA**

## Correction from v1.0.1
The project previously used an overly strict statement that fewer than 11 *interpretable* controls automatically fails the Moderate gate.
ClinGen SVI instead frames Moderate around at least 11 total mixed P/LP + B/LB validation controls and explicitly models a scenario in which one control has an indeterminate readout while Moderate remains supportable. v1.0.2 corrects this distinction.

## F0V — ClinGen assay-validation layer
- Cell model: **U2OS**
- Architecture: endogenous BUBR1 depletion + RNAi-resistant BUBR1 complementation
- Literature anchor: **Suijkerbuijk et al. 2010, PMID 20516114**
- Primary endpoint: chromosome missegregation per completed division
- Mechanistic endpoint: spindle-assembly-checkpoint response
- Secondary: chromosome alignment
- 11 independent validation controls: 6 B/LB missense + 5 P/LP truncating
- N1002K remains held out until control-only calibration is frozen
- No PS3/BS3 is assigned now
- cDNA complementation does not validate truncation-driven RNA/NMD effects

## F0M — disease-context mechanism layer
- Cell model: **hTERT-RPE1**
- Endogenous isogenic allelic series
- Five original genotype arms retained
- Primary endpoint unchanged
- Mechanism classes unchanged: ABUNDANCE_LIMITED / FUNCTION_LIMITED / AMBIGUOUS
- Compound-state interpretation remains phase-dependent

## Next gate
No result-bearing NB05B should be created before real F0V/F0M observations exist.
