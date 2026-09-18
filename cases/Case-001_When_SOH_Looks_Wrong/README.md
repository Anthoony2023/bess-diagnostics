# Case-001 When SOH Looks Wrong - B0005

Status: Evidence collected - Capacity fade observed, regeneration events identified, root cause not yet concluded.

## Technical question
Can I trust a battery health estimate when the underlying data may contain structural or quality issues?

## Current dataset
DS-001 — NASA PCoE B0005

## Current evidence base (Day 2)
- Discharge records: 168, max 1.8565, min 1.2875, first 1.8565, last 1.3251, fade 28.6%
- Plot: B0005 Capacity Fade (0-167) with regeneration at ~18, 30, 89, 149, 166
- Largest regeneration: index 89, 1.5145 -> 1.6058 (+0.0913)
- Largest drops after regeneration: 89->90 -0.0420, 30->31 -0.0211, 120->121 -0.0209

## Data quality context (from Atlas 001)
- Total records 616: charge 170 / discharge 168 / impedance 278
- Charge sample counts 5-3900 mean ~3183 total ~541k
- Discharge sample counts 179-371 mean ~299 total ~50k
- Impedance fixed 48 points (Sense_current, Battery_current, Re, Rct etc.)
- Time field exists for charge/discharge, sampling regularity TBD
- Capacity unit TBD, SOH/EOL definition TBD

## Evidence
- evidence/capacity_fade.png

## Engineering analysis
Capacity is measured as 1x1 scalar in discharge records. Fade is not monotonic. Regeneration events are observed after impedance records, suggesting rest/recovery effect rather than true healing.

## Alternative explanations
- Rest after impedance measurement
- Temperature variation (ambient observed 24°C but not verified per record)
- Measurement condition change
- Cause not yet determined - requires time-gap analysis

## Engineering judgment
An apparent increase in SOH (if defined as capacity) does not necessarily mean battery healed. It may reflect measurement artifact / rest. Treating every SOH increase as anomaly in BESS would cause false alarms.

## Important boundary
This case does NOT yet conclude that the B0005 SOH is wrong. Purpose is to determine what the data can legitimately support before interpreting health/degradation.

## Planned structure
- Technical question
- Data required
- Data quality checks
- Evidence
- Engineering analysis
- Alternative explanations
- Engineering judgment
- Remaining uncertainty

## Remaining uncertainty / Next steps
- [ ] Time gap before each regeneration (parse time field to hours)
- [ ] Correlation of Re/Rct with regeneration
- [ ] Verify NASA documentation for documented regeneration

## BESS Relevance
Low direct BESS system relevance, high methodological benchmark value for distinguishing measurement artifact vs real degradation in field SOH estimation.
