# Case-002: Why Single-Point SOH Is Questioned in the Field

## Final v5.0 — Evidence-Separated Version

### One-line Summary

Field SOH is an indirect estimate made under multiple sources of uncertainty. 
When the battery system cannot be opened or individual cells cannot be directly tested, 
an isolated SOH value can be difficult to interpret without its measurement context, 
longitudinal trend, and uncertainty.

---

# 1. Engineering Question

Why can a single-point field SOH estimate be difficult to trust?

The question is not simply whether the SOH algorithm is accurate.

In field operation, battery health may have to be inferred indirectly while the system
remains assembled and operational. The measurement can therefore be affected by
cell-to-cell variation, operating conditions, rest time, temperature representation,
sensor characteristics, and measurement methodology.

This case separates:

1. What the NASA dataset directly shows
2. What comes from field engineering observation
3. What can reasonably be inferred but is not yet directly validated
4. Broader industry discussion

---

# 2. NASA Data Evidence

## Dataset

NASA Battery Dataset:

- B0005
- B0006
- B0007
- B0018

B0005 is the primary cell used in Case-001. The additional cells are used here to
examine whether the observed behavior is consistent across different cells.

---

## Evidence A — Aging-Related Rebound Trend

### Observation

For B0005, rebound magnitude increases over the analyzed aging period.

Approximate observed values:

- Earlier state: ~35 mV
- Later state: ~85 mV

This represents approximately 2.4× growth in rebound magnitude.

### What the data supports

The B0005 data shows an overall increase in rebound magnitude as the cell ages,
while individual measurements fluctuate around the overall trajectory.

### What the data does NOT prove

The dataset does not by itself prove that rebound is equivalent to impedance,
nor that a specific rebound value corresponds to a specific SOH value.

---

## Evidence B — Cell-to-Cell Variation

### Observation

Different cells show different initial rebound values under the analyzed conditions:

| Cell | Initial rebound |
|------|----------------:|
| B0005 | ~35 mV |
| B0006 | ~45 mV |
| B0007 | ~32 mV |

Observed spread:

**13 mV**

### What the data supports

Cells with the same nominal model can exhibit different measured rebound values.

### Interpretation

This demonstrates why absolute rebound values should be interpreted carefully
when comparing different cells.

### Important limitation

The available evidence does not establish that B0005, B0006, and B0007 represent
different manufacturing batches.

Therefore this case uses:

**Cell-to-cell variation**

rather than:

**Batch variation**

---

## Evidence C — Rest-Time Dependence

### Observation

For the analyzed measurements:

- 5 min: ~25 mV
- 30 min: ~40 mV
- 60 min: ~45 mV

The increase is substantially larger during the earlier part of the rest period.

Approximate comparison:

- 5 → 30 min: ~1.6×
- 30 → 60 min: smaller additional increase

### What the data supports

Rebound magnitude depends on elapsed rest time.

The observed relationship is not well represented by a simple linear relationship
over the tested rest intervals.

### What the data does NOT prove

This does not establish a universal 5-minute-to-30-minute conversion formula.

A field correction model would require additional calibration data.

---

## Evidence D — Single Measurements vs. Observed Trend

### Observation

Individual rebound measurements can move substantially between consecutive observations.

Example:

**38 → 45 → 36 mV**

while a 5-cycle moving average produces a smoother representation of the observed
trajectory.

### What the data supports

Single-point measurements contain short-term variation.

A moving average can make the longer-term trajectory easier to observe.

### Important distinction

A smoother curve is not automatically a more accurate measurement.

The moving average does not itself prove that measurement error has been removed,
nor does it establish the true SOH.

The value of the trend is that it provides additional temporal context.

---

# 3. Field Engineering Observations

The following observations come from field engineering experience and are not
directly validated by the NASA single-cell laboratory dataset.

## 3.1 Cell-Level Impedance Is Difficult to Measure in the Field

Battery health is strongly related to impedance behavior, but accurately measuring
impedance for every individual cell is difficult once cells are assembled into a
battery system.

In many field situations, the system cannot simply be opened and each cell removed
for a controlled impedance measurement.

---

## 3.2 Voltage Rebound Is a Practical Observable

After discharge, battery voltage can rebound during the subsequent rest period.

For the same cell, changes in rebound behavior over time may provide useful
information about changes in battery condition.

However, rebound should not be treated as identical to directly measured impedance.

---

## 3.3 Field Baselines Are Better Established Per Cell or Per System

Because different cells can have different initial characteristics, an absolute
threshold applied identically to every cell may be difficult to interpret.

A practical field approach is to establish a baseline for the individual cell,
module, rack, or system and monitor relative change over time.

---

## 3.4 Rest Time Is an Operational Compromise

Longer rest periods generally provide more opportunity for voltage relaxation to
develop.

In laboratory testing, extended rest periods may be practical.

In an operating BESS, however, shutting down equipment for a long diagnostic test
has an operational cost.

Therefore, field diagnostics may require a compromise between diagnostic quality
and system availability.

A 20–30 minute diagnostic window is an engineering operating assumption in this
case, not a universal requirement.

---

## 3.5 Temperature Measurements May Not Represent Every Cell

In an assembled module or battery bank, temperature sensors are generally not
located on every cell.

A sensor near the cabinet entrance, for example, may not represent the temperature
of cells deeper inside the battery system.

Therefore, temperature compensation based on a limited number of sensors can carry
spatial uncertainty.

---

## 3.6 Measurement Instrumentation Adds Uncertainty

Dynamic battery measurements are affected by factors such as:

- Sensor accuracy
- Voltage/current synchronization
- Sampling rate
- Measurement resolution
- Measurement timing

These factors can affect estimates derived from dynamic voltage/current behavior.

---

## 3.7 Full Retesting of Every Cell Is Often Impractical

In an operating energy-storage system, removing and fully retesting every cell may
be impractical because of time, labor, system availability, and cost constraints.

Consequently, field diagnostics often have to work with the data already available
from the operating system.

---

# 4. Engineering Inferences

The following conclusions are reasonable engineering inferences from the NASA
observations combined with the field constraints above. They are not direct
experimental conclusions from the NASA dataset.

---

## 4.1 Rebound May Be Used as an Indirect Health Indicator

The observed relationship between rebound behavior and aging makes rebound a
potential indirect indicator of battery condition.

However:

> Rebound ≠ directly measured impedance.

A field diagnostic method should therefore treat rebound as an indirect signal
rather than a direct impedance measurement.

---

## 4.2 Cell-Specific Baselines May Be More Informative Than Absolute Thresholds

The observed cell-to-cell variation means that two cells can have different initial
rebound values.

Therefore, a practical diagnostic method may benefit from tracking each cell
against its own baseline rather than applying one absolute threshold to all cells.

For example:

**Baseline → Current value → Relative Growth**

can provide more context than:

**Current value → Fixed threshold**

This is an engineering methodology, not a claim that the NASA dataset establishes
a universal diagnostic threshold.

---

## 4.3 Short-Rest Measurements May Require Empirical Correction

The NASA data shows that rebound depends strongly on rest time and that the change
is not well represented by a simple linear relationship across the tested intervals.

Therefore, if a field system only provides a short diagnostic window, a practical
implementation may require:

- Time-dependent lookup tables
- Empirical calibration
- Regression models
- Other validated correction methods

The appropriate method cannot be selected from this dataset alone.

---

## 4.4 Temperature Compensation Requires Representative Temperature Data

If only a small number of temperature sensors are available, applying a temperature
correction to the entire battery based on one measurement may introduce uncertainty.

A practical field method therefore needs to consider both:

**temperature correction**

and

**temperature representativeness**.

---

## 4.5 Field SOH Is a Multi-Uncertainty Inference Problem

The combination of:

- Cell-to-cell variation
- Baseline differences
- Rest-time dependence
- Temperature uncertainty
- Sensor accuracy
- V/I synchronization
- Sampling characteristics
- Short-rest extrapolation
- Limited ability to retest individual cells

means that field SOH should be treated as an indirect inference rather than an
absolute ground-truth measurement.

This is the central engineering inference of this case.

---

# 5. Industry Discussion

SOH estimates can also be used in discussions involving asset condition,
warranty interpretation, insurance, financing, or asset valuation.

In those situations, the way an SOH estimate is reported can affect how much
information the number communicates.

A single value such as:

**SOH = 85%**

does not communicate:

- Measurement conditions
- Data quality
- Baseline definition
- Temperature
- Rest time
- Model assumptions
- Confidence or uncertainty
- Recent trend

A more transparent representation could be conceptually expressed as:

**SOH estimate = 85% ± uncertainty**

with the uncertainty accompanied by its sources and measurement context.

### Important limitation

The uncertainty range in such a presentation must come from a validated uncertainty
model or measurement analysis.

For example:

**85% ± 5%**

should not be presented as a statistically established interval unless the underlying
data and methodology support that interval.

This case does not provide evidence that specific companies or diagnostic platforms
intentionally select optimistic coefficients or hide uncertainty.

The broader industry question is therefore treated as a discussion point rather than
a demonstrated finding.

---

# 6. Cross-Validation — Self-Contradiction Check

| Claim | Evidence / Basis | Status | Interpretation |
|------|------|------|------|
| Rebound is related to battery condition | B0005 aging trend | Supported with limitation | Do not equate rebound with impedance |
| Older B0005 shows larger rebound | 35 → 85 mV | NASA evidence | Self-comparison; individual points still fluctuate |
| Different cells have different initial rebound | 35 / 45 / 32 mV | NASA evidence | Supports caution with absolute cross-cell thresholds |
| Rest time affects rebound | 25 / 40 / 45 mV | NASA evidence | Simple linear extrapolation is insufficient across tested intervals |
| Short-rest correction may be needed | Rest-time behavior + field constraint | Engineering inference | Requires additional calibration |
| Temperature may introduce uncertainty | Field measurement configuration | Field observation | Not demonstrated by NASA single-cell data |
| Single measurements fluctuate | Individual rebound observations | NASA evidence | Variation should not automatically be labeled measurement error |
| Moving average shows the longer-term trajectory more clearly | 5-cycle MA | NASA evidence + interpretation | Smoothing improves visualization, not necessarily accuracy |
| Trend provides more context than a single point | Longitudinal observations | Engineering inference | Does not mean trend automatically equals ground truth |
| Field SOH contains stacked uncertainties | Multiple field constraints | Engineering inference | Central engineering interpretation |
| SOH should include uncertainty/context | Measurement and reporting logic | Engineering inference | Requires validated uncertainty methodology for numerical bounds |
| Industry reporting can affect interpretation | Industry discussion | Discussion | No claim about intentional behavior by a specific company |

---

# 7. Implication for Asset Valuation

A single SOH number should not be interpreted without knowing how it was measured.

A more informative asset-health representation would include:

1. SOH estimate
2. Historical trend
3. Measurement conditions
4. Data quality
5. Model assumptions
6. Uncertainty range
7. Source of the uncertainty

For example:

> **SOH = 85% ± 5%**

is conceptually more informative than:

> **SOH = 85%**

but only if the ±5% uncertainty is supported by a valid methodology.

The purpose is not to make an SOH estimate look more conservative or more optimistic.

The purpose is to make the basis and limitations of the estimate visible.

---

# 8. BESS Diagnostics Positioning

The engineering problem can be summarized as:

**Lab baseline**
↓
**Cell-to-cell variation**
↓
**Limited field retesting**
↓
**Representative temperature measurements**
↓
**Short diagnostic windows**
↓
**Non-linear rest-time effects**
↓
**Sensor / synchronization / sampling uncertainty**
↓
**Indirect health estimation**
↓
**Single-point SOH**
↓
**Potentially incomplete engineering interpretation**

BESS Diagnostics focuses on making this uncertainty chain visible.

The objective is not simply to produce a more precise-looking SOH number.

The objective is to determine:

> **What does the available data actually support?**

---

# 9. Final Takeaway

A field SOH estimate is not simply an algorithm output.

It is an engineering inference made from measurements collected under real operating
constraints.

The NASA dataset demonstrates several important measurement behaviors:

- Cell-to-cell variation exists.
- Rebound changes with aging.
- Rest time affects rebound.
- Individual measurements fluctuate over time.

Field engineering adds further constraints involving temperature representation,
measurement instrumentation, diagnostic time, and the practical inability to retest
every cell.

Therefore:

> **A single SOH value should be interpreted together with its measurement context,
> longitudinal trend, and uncertainty.**

The goal of BESS Diagnostics is not to hide uncertainty behind a single number,
but to make the uncertainty understandable and actionable.
