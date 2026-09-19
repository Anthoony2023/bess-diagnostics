# Case-002: Why Single-Point SOH is Always Questioned in the Field
## Final v4.2 - Generic / Neutral Version

### One-line Summary
Field SOH is not inaccurate because the algorithm is bad. It is questioned because the system cannot be opened, you have to guess internal health while operating with stacked uncertainties. Single-point amplifies errors, only trend over time can exclude errors.

### Engineering Reality - 11 Field Observations

1.  **Health essence:** Higher impedance = less healthy. Simple in theory, but accurate impedance per cell cannot be measured in field.
2.  **Rebound phenomenon:** After discharge, voltage rebounds. Same cell self-comparison: older tends to rebound more, but absolute value varies per cell.
3.  **Baseline:** Cannot use absolute value across cells. Need self-baseline Growth% as fingerprint.
4.  **Time compromise:** Longer rest = more accurate, overnight best. Field compromise 20-30 min is reasonable balance.
5.  **Short-rest extrapolation:** If only 5 min available in field, need to extrapolate 5 min -> 30 min equivalent rebound, needs tables/models.
6.  **Non-linear extrapolation:** Lab is 24C constant current, field is varying temp/current, so extrapolation is not linear.
7.  **Data source:** Cell maker data only represents one batch/model, not all cells have same material/process/conditions. Batch variation exists.
8.  **No retest:** Energy storage operators have no time/cost to retest all cells, so use maker ideal data as baseline.
9.  **Temperature representative points:** After assembling into module/Battery Bank, temp sensors only at representative key locations, not per cell. 32C at door cannot represent 45C in middle.
10. **Measurement uncertainty:** Sensor accuracy, V/I synchronization, sampling rate cause dynamic impedance dV/dI error.
11. **Industry reality (NEUTRAL):** When SOH is used for asset valuation discussions with insurance and finance, there is a structural incentive in SaaS predictive diagnostic platforms and reporting practices to select optimistic coefficients and hide uncertainty bands, presenting only a single-point SOH 85%. This is why field verifications are often questioned - not because of a specific company, but because of industry-wide reporting incentives. Generic platforms face the same questioning structure.

### Data Evidence - 4 Cells Cross-Validation (NASA Battery Dataset)

- B0005 (Case-001 main), B0006, B0007, B0018 as 4 cells for Case-002 validation
- Evidence A - Old > New: B0005 35mV -> 85mV (2.4x growth)
- Evidence B - Batch variation: New cells B0005 35mV vs B0006 45mV vs B0007 32mV (13mV diff, same condition)
- Evidence C - Rest time effect: Same cell same SOH, 5min 25mV vs 30min 40mV vs 60min 45mV, ratio 1.6-1.8x, non-linear (fast early, slow later)
- Evidence D - Single-point vs Trend: Single points jump 38->45->36mV, 5-cycle moving average smooth 2%->3%->5% growth

Limit: Temperature representative point error not visible in single-cell chamber data, marked as Field Observation, which is exactly Lab-to-Field Gap.

### Cross-Validation - Self-Contradiction Check

| Claim | Evidence | Consistent? | Note |
|-------|----------|-------------|------|
| Rebound = proxy of impedance | EIS 0.08->0.16Ohm vs dV/dI noisy | Yes | Don't write rebound = impedance |
| Old > New | 35->85mV same cell | Yes, with note: self-comparison, exclude temp variation, trend up but single point jumps | Add but clause |
| Absolute varies -> use Growth% | 35 vs 45 vs 32mV | Yes, proves cannot use absolute threshold | If wrote 50mV threshold, self-contradict |
| Longer rest more accurate, 5min extrapolate | 5min 25 vs 30min 40mV, 1.6-1.8x | Yes | Don't claim 5min as accurate as 30min |
| Temp rep point cannot represent each cell | No lab data, field physics | No counter-evidence, but mark as Field Observation | Don't use NASA to prove field temp error |
| Trend > single-point | Single jump vs MA smooth | Yes, directly proves single amplifies error | If give single SOH 85%, contradict |
| Questioned accuracy due to stacked errors + reporting | Industry structure inference | Logical consistent, marked as Discussion, generic: SaaS predictive diagnostic platforms | No specific company targeted |

Conclusion: No self-contradiction if written as open discussion with uncertainty bands.

### Implication for Asset Valuation

- Should not be single-point SOH number
- Should be trend over time + uncertainty breakdown
- When presented as 85% +/-5% with source breakdown, 78% field verification is within range = professional, not misjudgment
- When presented as single 85% hiding bands, 78% verification feels like overestimation

### BESS Diagnostics Positioning

Not selling more accurate algorithm, selling transparency of how inaccuracy stacks:

Lab cherry-picked baseline -> No field retest -> Representative temp sensor -> Short-rest extrapolation with non-linear compensation -> Single-point SOH without uncertainty -> Questioned accuracy
