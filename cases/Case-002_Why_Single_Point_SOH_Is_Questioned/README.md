# Case-002: Why Single-Point SOH is Always Questioned

> 4-Cell cross-validation: B0005 / B0006 / B0007 / B0018

## Question
Why is field SOH always questioned by insurance and finance?

## Why this case matters
Single-point SOH 85% amplifies all field errors. Only trend + error bands can survive technical due diligence.

## Dataset
- NASA Battery Dataset: B0005, B0006, B0007, B0018
- Source: https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/
- Note: .mat files must be downloaded separately, not in repo

## Evidence Summary

**Batch variation (same model, new cells):**
- B0005: 35mV, B0006: 45mV, B0007: 32mV → diff 13mV

**Aging effect (old > new, same cell):**
- B0005: 35mV (new) -> 85mV (aged) = 2.4x

**Rest time effect (non-linear):**
- 5min: 25mV vs 30min: 40mV = 1.6-1.8x, non-linear extrapolation fails

**Single vs Trend:**
- Single: 38 -> 45 -> 36mV (jumpy, questioned)
- 5-cycle MA: smooth increasing trend (credible)

## Field Observations
See `docs/field-observations-11-points_2.md` for 11 stacked error sources.

## Conclusion
Field errors are stacked: Batch variation + time compromise + representative temp sensor + sync error. Single-point amplifies errors. Present trend + error bands.

## How to Reproduce
1. Download B0005/B0006/B0007/B0018 .mat files
2. `pip install numpy matplotlib scipy`
3. `python src/rebound_analysis.py`
4. `python src/trend_vs_single.py`
5. Figures -> `evidence/`

## Contents
