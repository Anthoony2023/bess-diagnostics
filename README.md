# bess-diagnostics

> Not selling a more accurate algorithm. Explaining why single-point SOH is always questioned - and how to present it with trend + error bands.

## What is this repo?

In the field, BESS cannot be disassembled. You have to infer internal health while the system is operating, with measurement uncertainties. A single-point SOH 85% amplifies all errors. Only a trend over time with uncertainty breakdown can exclude errors.

**Core thesis: Don't present a single point. Present trend + error bands.**

Lab cherry-picked baseline → No field retest → Representative temp sensor → Short-rest extrapolation (non-linear) → Single-point SOH without uncertainty → Questioned accuracy

## Cases

### Case-001: When SOH Looks Wrong (Single Cell)
- **Dataset:** DS-001 B0005
- **Question:** Why does using absolute 50mV threshold cause misjudgment?
- **Method:** Same cell self-comparison, self-baseline Growth%
- **Conclusion:** Batch variation exists. Use growth rate, not absolute value.

### Case-002: Why Single-Point SOH is Always Questioned (4 Cells Cross-Validation)
- **Dataset:** DS-002 B0005 / B0006 / B0007 / B0018
- **Question:** Why is field SOH always questioned by insurance and finance?
- **11 Field Observations:** See `cases/Case-002_Why_Single_Point_SOH_Is_Questioned/docs/field-observations-11-points_2.md`
- **Data Evidence:**
  - Batch variation: Same model, new cell rebound diff 13mV (35 vs 45 vs 32mV)
  - Old > New: Same cell 35mV -> 85mV (2.4x)
  - Rest time effect: 5min 25mV vs 30min 40mV (1.6-1.8x, non-linear)
  - Single vs Trend: Single jumps 38->45->36mV, 5-cycle MA smooth increase
- **Conclusion:** Field errors are stacked (Batch + time compromise + representative temp + sync). Single-point amplifies errors.

## Repo Map

```
atlas/ - Project map and case index
cases/ - Complete case packages (docs + evidence figures + src)
methods/ - Reusable methods (Growth%, extrapolation)
notebooks/ - Reproducible Jupyter notebooks
```

## How to Reproduce Case-002

1. Download NASA Battery Dataset B0005/B0006/B0007/B0018
2. `pip install numpy matplotlib scipy`
3. `python cases/Case-002_Why_Single_Point_SOH_Is_Questioned/src/rebound_analysis.py`
4. `python cases/Case-002_Why_Single_Point_SOH_Is_Questioned/src/trend_vs_single.py`
5. Figures will be generated in `evidence/`

## License

- **Code** (`src/`, `methods/`, `notebooks/`): MIT License - See `LICENSE-CODE`
- **Documentation & Articles** (`cases/*/docs/`, `README.md`, `atlas/`): CC BY-NC-ND 4.0 - See `LICENSE-DOCS`

## Let's Connect

I provide independent technical consulting on BESS asset valuation and diagnostic strategies.

If you are an asset owner, insurer, or operator facing questions about SOH accuracy, valuation gaps, or diagnostic strategy, let's talk.

**Connect via LinkedIn or email for consulting inquiries.**

*Author: Anthony Chou | 20 years field engineering experience | Based in Cypress, TX, US | Focus: BESS field diagnostics*
