# Case-001 — When SOH Looks Wrong

Status: Completed — Evidence collected and engineering interpretation established.

## Technical Question

Can a single capacity measurement be trusted as a direct indicator of battery degradation?

## Dataset

DS-001 — NASA PCoE B0005

## Engineering Context

Battery health is often represented by capacity or an SOH estimate. 
However, a measured capacity value can depend on the battery's recent operating and measurement history.

This case examines whether short-term changes in measured capacity should automatically be interpreted as changes in the underlying degradation state.

---

## Evidence 01 — Capacity Trend

B0005 contains 168 discharge records.

Observed discharge capacity:

- First: 1.8565 (unit TBD)
- Last: 1.3251 (unit TBD)
- Overall decline: approximately 28.6%

The capacity trend is not monotonic.

Five prominent upward excursions were identified at:

- Discharge Index 18
- Discharge Index 30
- Discharge Index 89
- Discharge Index 149
- Discharge Index 166

The largest observed increase was:

- Before: 1.5145
- After: 1.6058
- Increase: +0.0913

The upward excursions are followed by subsequent capacity decreases.

Evidence:
- `evidence/capacity_fade_final.png`

---

## Evidence 02 — Measurement Time Context

The five regeneration events do not share a single consistent time-gap pattern.

Previous discharge → regeneration gaps range from approximately:

- 4 hours
- to more than 1 day

Previous impedance → regeneration gaps range from:

- approximately 32 minutes
- to more than 15 hours
- with one event having no preceding impedance record

The next discharge after regeneration also occurs after variable time intervals.

Therefore, the observed capacity increases cannot be attributed to one simple, repeatable timing pattern based on the current evidence.

Evidence:
- `evidence/Evidence-02-Time-Gaps.md`
- `evidence/regeneration_sequence.png`

---

## Evidence 03 — Impedance Behavior

B0005 contains 278 impedance records.

All impedance timestamps are strictly increasing:

- Records: 278
- Time intervals: 277
- Non-positive intervals: 0

However, the interval between impedance measurements is highly non-uniform:

- Minimum: 1:20:28
- Median: approximately 3.34 hours
- Mean: approximately 3.38 hours
- Maximum: 3 days 2:46:18

Multiple multi-hour and multi-day gaps are present.

Re and Rct both show an overall increase between early and late measurements, but neither parameter is monotonic.

Observed first-to-last change:

- Re: +12.02%
- Rct: +7.68%

These observations demonstrate changing impedance behavior over the experiment, but do not by themselves establish the cause of individual capacity regeneration events.

---

## Evidence 04 — Ambient Temperature

Ambient temperature was controlled at 24°C during the identified regeneration events. No ambient-temperature variation was observed that could explain the events.

---

## Engineering Analysis

The B0005 dataset shows two behaviors occurring at different time scales:

### Long-term behavior

Measured discharge capacity shows a clear overall decline.

### Short-term behavior

Individual capacity measurements can temporarily increase substantially before declining again.

The data therefore demonstrate that:

> A measured capacity value is not necessarily equivalent to the underlying irreversible degradation state at that moment.

The observed regeneration behavior is consistent with the practical engineering experience that battery measurements can be affected by recent rest, operating history, and measurement conditions.

However, this case does not attempt to prove a single physical mechanism for every regeneration event.

---

## Engineering Judgment

Battery health should be interpreted from the temporal trend and measurement context rather than from isolated capacity observations.

In particular:

> **Do not automatically interpret every upward SOH/capacity movement as battery recovery, and do not automatically interpret every downward movement as accelerated degradation.**

For BESS diagnostics, the measurement context should be considered together with the health estimate.

Relevant context can include:

- Time since previous discharge
- Time since previous charge
- Rest duration
- Diagnostic/impedance measurement history
- Operating condition
- Temperature
- Measurement protocol

---

## BESS Relevance

B0005 is a single-cell laboratory dataset and does not directly represent a complete BESS.

Its value for BESS diagnostics is methodological.

The case demonstrates an important diagnostic principle:

> **Before deciding what is wrong, determine whether the data supports the conclusion.**

A BESS monitoring system that treats every single-point SOH estimate as an independent indication of degradation may generate false interpretations when measurement context changes.

A more robust approach is to evaluate:

- Temporal trend
- Measurement context
- Data quality
- Operating conditions
- Persistence of the observed change

before declaring a degradation event.

---

## What This Case Does NOT Prove

This case does not prove that:

- every regeneration event is caused by impedance measurement
- every regeneration event is caused by rest
- capacity recovery is caused by one specific electrochemical mechanism
- Re/Rct changes directly cause capacity changes
- the same magnitude of regeneration will occur in BESS field data

Those questions require additional experimental evidence and/or datasets with appropriate operating-state information.

---

## Final Takeaway

The important finding is not that B0005 contains a particular type of regeneration.

The important finding is:

> **Battery health should be interpreted from trend and measurement context, not from an isolated absolute value.**

This is the primary engineering lesson of Case-001.
