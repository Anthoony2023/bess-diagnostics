# BESS Diagnostics

## Battery Data Analytics Lab

BESS Diagnostics is a long-term engineering-focused workspace for analyzing public battery and BESS datasets.

> **Before deciding what is wrong, determine whether the data supports the conclusion.**

Core workflow:

**Battery Data → Data Quality → Engineering Analysis → Engineering Judgment**

Python is used for computation and evidence generation. AI is used to support interpretation and engineering judgment.

## Project principles

- Public datasets are used as technical proof-of-capability and methodological benchmarks.
- Dataset inspection comes before modeling.
- Evidence, observations, hypotheses, and engineering conclusions are kept separate.
- Large raw datasets are not committed to GitHub.
- GitHub stores knowledge, metadata, analysis code, and reproducible findings.
- Colab/Jupyter is the analysis laboratory; GitHub is the durable knowledge base.

## Current work

### DS-001 — NASA PCoE B0005

Day 1 focuses only on data inventory and structural inspection.

No SOH, degradation, anomaly, or ML conclusion is made at this stage.

See:

- `atlas/Dataset_Atlas.xlsx`
- `datasets/DS-001_B0005/README.md`
- `inspections/DS-001_B0005/inspection.md`
- `inspections/DS-001_B0005/evidence.md`
- `cases/Case-001_When_SOH_Looks_Wrong/README.md`
