# Case-002 — Why Single-Point SOH Is Questioned in the Field

> **Field SOH is an indirect estimate made under multiple sources of uncertainty.**
> A single SOH value should therefore be interpreted together with its measurement
> context, longitudinal trend, and uncertainty.

---

## 1. Engineering Question

### Why can a single-point field SOH estimate be difficult to trust?

The problem is not simply whether the SOH algorithm is accurate.

In field operation, the battery system may remain assembled and operational while
internal battery health has to be inferred indirectly.

The resulting estimate can be affected by:

- Cell-to-cell variation
- Aging state
- Rest time
- Temperature
- Sensor characteristics
- Voltage/current synchronization
- Sampling characteristics
- Measurement methodology
- Limited ability to retest individual cells

This case separates the evidence into four levels:

1. **NASA Data Evidence** — directly observed in the analyzed NASA dataset
2. **Field Engineering Observations** — based on practical field experience
3. **Engineering Inference** — reasonable conclusions derived from the evidence
4. **Industry Discussion** — broader questions that require additional validation

---

# 2. Dataset

### NASA Battery Dataset

Cells analyzed in this case:

- B0005
- B0006
- B0007
- B0018

B0005 is also the primary dataset used in:

**Case-001 — When SOH Looks Wrong**

The additional cells are used here to examine whether the observed measurement
behavior is also present across different cells.

> The NASA dataset is a laboratory single-cell dataset. It is used here as a
> methodological reference, not as a direct representation of a complete field BESS.

---

# 3. NASA Data Evidence

## Evidence A — Aging-Related Rebound Trend

### Observation

For B0005, rebound magnitude increases over the analyzed aging period.

Approximate observed values:

- Earlier state: ~35 mV
- Later state: ~85 mV

This corresponds to approximately 2.4× growth in the analyzed measurements.

### What the data supports

The B0005 data shows an overall increase in rebound magnitude as the cell ages,
while individual measurements fluctuate around the longer-term trajectory.

### What this does not prove

The dataset does not establish that rebound is equivalent to directly measured
impedance, nor does it establish a universal mapping between rebound and SOH.

---

## Evidence B — Cell-to-Cell Variation

### Observation

Different cells show different initial rebound values under the analyzed conditions:

| Cell | Initial rebound |
|---|---:|
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

### Terminology

This case uses:

**Cell-to-cell variation**

rather than:

**Batch variation**

because the available evidence does not establish that B0005, B0006, and B0007
represent different manufacturing batches.

---

## Evidence C — Rest-Time Dependence

### Observation

For the analyzed measurements:

| Rest time | Rebound |
|---|---:|
| 5 min | ~25 mV |
| 30 min | ~40 mV |
| 60 min | ~45 mV |

The increase is substantially larger during the earlier part of the rest period.

Approximate comparison:

- 5 → 30 min: ~1.6×
- 30 → 60 min: smaller additional increase

### What the data supports

Rebound magnitude depends on elapsed rest time.

The observed relationship is not well represented by a simple linear relationship
over the tested rest intervals.

### What this does not prove

The dataset does not establish a universal 5-minute-to-30-minute conversion formula.

A field correction model would require additional calibration data.

---

## Evidence D — Single Measurements vs. Observed Trend

### Observation

Individual rebound measurements can move substantially between consecutive observations.

Example:

**38 → 45 → 36 mV**

while a 5-cycle moving average provides a smoother representation of the observed
trajectory.

### What the data supports

Single-point measurements contain short-term variation.

A moving average can make the longer-term trajectory easier to observe.

### Important distinction

A smoother curve is not automatically a more accurate measurement.

The moving average does not itself prove that measurement error has been removed,
nor does it establish the true SOH.

Its value here is that it provides additional temporal context.

---

# 4. Evidence and Figures

The case evidence is organized in the `evidence/` directory.

### Evidence A
**Old → New rebound behavior**

Shows the longitudinal rebound behavior of B0005.

### Evidence B
**Cell-to-cell variation**

Compares the initial rebound values of B0005, B0006, and B0007.

### Evidence C
**Rest-time dependence**

Compares rebound measurements at different rest intervals.

### Evidence D
**Single-point vs. observed trend**

Compares individual measurements with a 5-cycle moving average.

> Figure filenames may vary as the evidence set is refined. The evidence directory
> is the source of record for the current figures.

---

# 5. Field Engineering Observations

The following observations come from field engineering experience.

They are **not directly validated by the NASA single-cell laboratory dataset**.

The detailed 11-point field observations are documented here:

**[11 Field Engineering Observations](docs/field-observations-11-points_2.md)**

The main observations are summarized below.

### 5.1 Cell-Level Impedance Is Difficult to Measure in the Field

Battery health is strongly related to impedance behavior, but accurately measuring
impedance for every individual cell is difficult once cells are assembled into a
battery system.

In many field situations, the system cannot simply be opened and each cell removed
for a controlled impedance measurement.

---

### 5.2 Voltage Rebound Is a Practical Observable

After discharge, battery voltage can rebound during the subsequent rest period.

For the same cell, changes in rebound behavior over time may provide useful
information about changes in battery condition.

However:

> **Rebound is not equivalent to directly measured impedance.**

---

### 5.3 Field Baselines Are Better Established Per Cell or Per System

Because different cells can have different initial characteristics, applying one
absolute threshold to every cell can be difficult to interpret.

A practical field approach is to establish a baseline for the individual cell,
module, rack, or system and monitor relative change over time.

---

### 5.4 Rest Time Is an Operational Compromise

Longer rest periods provide more opportunity for voltage relaxation to develop.

Laboratory testing can use extended rest periods more easily than an operating BESS.

In field operation, however, shutting down equipment for a long diagnostic test has
an operational cost.

Diagnostic duration therefore represents a trade-off between measurement quality
and system availability.

A 20–30 minute diagnostic window is an engineering operating assumption in this
case, not a universal requirement.

---

### 5.5 Temperature Measurements May Not Represent Every Cell

In an assembled module or battery bank, temperature sensors are generally not
located on every cell.

A sensor near one location may therefore not represent cells located elsewhere in
the battery system.

Temperature compensation based on limited sensor coverage can consequently carry
spatial uncertainty.

---

### 5.6 Measurement Instrumentation Adds Uncertainty

Dynamic battery measurements are affected by factors such as:

- Sensor accuracy
- Voltage/current synchronization
- Sampling rate
- Measurement resolution
- Measurement timing

These factors can affect estimates derived from dynamic voltage/current behavior.

---

### 5.7 Full Retesting of Every Cell Is Often Impractical

In an operating energy-storage system, removing and fully retesting every cell may
be impractical because of:

- Time
- Labor
- System availability
- Cost

Field diagnostics therefore often have to work with the data already available from
the operating system.

---

# 6. Engineering Inferences

The following conclusions are reasonable engineering inferences from the NASA
observations combined with the field constraints above.

They are **not direct experimental conclusions from the NASA dataset**.

---

## 6.1 Rebound May Be Used as an Indirect Health Indicator

The observed relationship between rebound behavior and aging makes rebound a
potential indirect indicator of battery condition.

However:

> **Rebound ≠ directly measured impedance.**

A field diagnostic method should therefore treat rebound as an indirect signal
rather than as a direct impedance measurement.

---

## 6.2 Cell-Specific Baselines May Be More Informative Than Absolute Thresholds

The observed cell-to-cell variation means that two cells can have different initial
rebound values.

Therefore, a practical diagnostic method may benefit from tracking each cell
against its own baseline rather than applying one absolute threshold to all cells.

Conceptually:

**Baseline → Current value → Relative Growth**

can provide more context than:

**Current value → Fixed threshold**

This is an engineering methodology, not a universal diagnostic rule established
by the NASA dataset.

---

## 6.3 Short-Rest Measurements May Require Empirical Correction

The NASA data shows that rebound depends strongly on rest time and that the observed
change is not well represented by a simple linear relationship across the tested
intervals.

Therefore, if a field system only provides a short diagnostic window, a practical
implementation may require:

- Time-dependent lookup tables
- Empirical calibration
- Regression models
- Other validated correction methods

The appropriate method cannot be selected from this dataset alone.

---

## 6.4 Temperature Compensation Requires Representative Temperature Data

If only a limited number of temperature sensors are available, applying a
temperature correction to the entire battery based on one measurement may introduce
uncertainty.

A practical field method therefore needs to consider both:

**Temperature correction**

and

**Temperature representativeness.**

---

## 6.5 Field SOH Is a Multi-Uncertainty Inference Problem

The combination of:

- Cell-to-cell variation
- Baseline differences
- Rest-time dependence
- Temperature uncertainty
- Sensor accuracy
- Voltage/current synchronization
- Sampling characteristics
- Short-rest extrapolation
- Limited ability to retest individual cells

means that field SOH should be treated as an indirect inference rather than an
absolute ground-truth measurement.

This is the central engineering inference of this case.

---

# 7. Cross-Validation — Self-Contradiction Check

| Claim | Evidence / Basis | Status | Interpretation |
|---|---|---|---|
| Rebound is related to battery condition | B0005 aging trend | Supported with limitation | Do not equate rebound with impedance |
| Older B0005 shows larger rebound | 35 → 85 mV | NASA evidence | Self-comparison; individual points still fluctuate |
| Different cells have different initial rebound | 35 / 45 / 32 mV | NASA evidence | Supports caution with absolute cross-cell thresholds |
| Rest time affects rebound | 25 / 40 / 45 mV | NASA evidence | Simple linear extrapolation is insufficient across tested intervals |
| Short-rest correction may be needed | Rest-time behavior + field constraint | Engineering inference | Requires additional calibration |
| Temperature may introduce uncertainty | Field measurement configuration | Field observation | Not demonstrated by NASA single-cell data |
| Single measurements fluctuate | Individual rebound observations | NASA evidence | Variation should not automatically be labeled measurement error |
| Moving average shows the longer-term trajectory more clearly | 5-cycle moving average | NASA evidence + interpretation | Smoothing improves visualization, not necessarily accuracy |
| Trend provides more context than a single point | Longitudinal observations | Engineering inference | Does not mean trend automatically equals ground truth |
| Field SOH contains stacked uncertainties | Multiple field constraints | Engineering inference | Central engineering interpretation |
| SOH should include uncertainty/context | Measurement and reporting logic | Engineering inference | Numerical uncertainty requires a validated methodology |
| Industry reporting can affect interpretation | Industry discussion | Discussion | Requires evidence beyond this dataset |

---

# 8. Implication for Asset Valuation

A single SOH number should not be interpreted without understanding how it was
measured.

A more informative asset-health representation could include:

1. SOH estimate
2. Historical trend
3. Measurement conditions
4. Data quality
5. Model assumptions
6. Uncertainty range
7. Sources of uncertainty

For example:

> **SOH = 85% ± uncertainty**

is conceptually more informative than:

> **SOH = 85%**

provided that the uncertainty is supported by a valid methodology.

The purpose is not to make an SOH estimate look more conservative or more optimistic.

The purpose is to make the basis and limitations of the estimate visible.

---

# 9. Reproduction and Execution

## Current status

The evidence in this case was developed from the NASA battery data using Python
analysis.

The repository contains analysis scripts under `src/`.

### Current scripts

- `src/rebound_analysis.py`
- `src/trend_vs_single.py`

### Important reproducibility note

`trend_vs_single.py` currently loads summary information and prints selected values.
It does **not yet contain the complete plotting implementation** used to generate
the Evidence D figure.

Therefore, it should currently be treated as an analysis placeholder rather than
a complete one-command reproduction script.

The repository will be updated when the plotting and data-generation pipeline is
fully reproducible.

### Required analysis environment

The analysis uses standard Python scientific-computing tools, including:

```text
Python
NumPy
SciPy
Matplotlib
