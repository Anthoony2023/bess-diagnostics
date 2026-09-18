# BESS Diagnostics

## Battery Data Analytics Lab

BESS Diagnostics is a long-term engineering-focused workspace for analyzing public battery and BESS datasets.

> **Before deciding what is wrong, determine whether the data supports the conclusion.**

Core workflow:

**Battery Data → Data Quality → Engineering Analysis → Engineering Judgment**

Python is used for computation and evidence generation. AI is used to support interpretation and engineering judgment.

Public site: [bessdiag.com](https://bessdiag.com)

## Project principles

- Public datasets are used as technical proof-of-capability and methodological benchmarks.
- Dataset inspection comes before modeling.
- Evidence, observations, hypotheses, and engineering conclusions are kept separate.
- Large raw datasets are not committed to GitHub.
- GitHub stores knowledge, metadata, analysis code, and reproducible findings.
- Colab/Jupyter is the analysis laboratory; GitHub is the durable knowledge base.

## Current work

### Done

**DS-001 Day 1 inspection** — NASA PCoE B0005 structure, inventory, and schemas. No model. No RUL.

**Case-001 — When SOH Looks Wrong** — A single capacity point is not the irreversible degradation state at that moment. Health = trend + measurement context.

- External one-pager: `cases/Case-001_When_SOH_Looks_Wrong/Case-001-One-Pager-External.pdf`
- Full write-up: `cases/Case-001_When_SOH_Looks_Wrong/README.md`
- Repro notebook: `notebooks/01_B0005_capacity_repro.py`

### Next

DS-002: apply the same inspection → evidence → judgment path on a second dataset closer to module or pack level.

Methods stay empty until a procedure has been tested on more than one dataset.

## See

- `atlas/Dataset_Atlas.xlsx`
- `datasets/DS-001_B0005/README.md`
- `inspections/DS-001_B0005/inspection.md`
- `inspections/DS-001_B0005/evidence.md`
- `cases/Case-001_When_SOH_Looks_Wrong/README.md`
- `notebooks/01_B0005_capacity_repro.py`
