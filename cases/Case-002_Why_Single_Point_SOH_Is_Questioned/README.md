# Case-002: Why Single-Point SOH Is Questioned in the Field

> **Final v5.0 — Evidence-Separated Version**  
> *Independent BESS Diagnostics & Performance Analysis by Anthony Chou, Ph.D.*

**[Technical Brief PDF](./Case-002-V5-0-Final-Letter.pdf)** · **[bessdiag.com](https://bessdiag.com)** · **[LinkedIn](https://linkedin.com/in/anthony-chou-tw671)**

---

### One-line Summary

Field SOH is an indirect estimate made under multiple sources of uncertainty. When the battery system cannot be opened or individual cells cannot be directly tested, an isolated SOH value can be difficult to interpret without its measurement context, longitudinal trend, and uncertainty.

---

# 1. Engineering Question

Why can a single-point field SOH estimate be difficult to trust?

The question is not simply whether the SOH algorithm is accurate.

In field operation, battery health may have to be inferred indirectly while the system remains assembled and operational. The measurement can therefore be affected by cell-to-cell variation, operating conditions, rest time, temperature representation, sensor characteristics, and measurement methodology.

This case explicitly separates:

1. **What the NASA dataset directly shows**
2. **What comes from field engineering observation**
3. **What can reasonably be inferred but is not yet directly validated**
4. **Broader industry discussion**

---

# 2. NASA Data Evidence

## Dataset
NASA Battery Dataset: **B0005, B0006, B0007, B0018**  
*B0005 is the primary cell used in Case-001. Additional cells examine behavior consistency across different units.*

---

## Evidence A — Aging-Related Rebound Trend

### Observation
For B0005, rebound magnitude increases over the analyzed aging period:
- **Earlier state:** ~35 mV
- **Later state:** ~85 mV
- **Observed Growth:** ~2.4× increase in rebound magnitude.

### What the data supports
The B0005 data shows an overall increase in rebound magnitude as the cell ages, while individual measurements fluctuate around the overall trajectory.

### What the data does NOT prove
The dataset does not by itself prove that rebound is equivalent to impedance, nor that a specific rebound value corresponds to a specific SOH value.

---

## Evidence B — Cell-to-Cell Variation

### Observation
Different cells show different initial rebound values under analyzed conditions:

| Cell | Initial Rebound |
| :--- | :--- |
| **B0005** | ~35 mV |
| **B0006** | ~45 mV |
| **B0007** | ~32 mV |

*Observed Spread:* **13 mV**

### What the data supports
Cells with the same nominal model can exhibit different measured rebound values.

### Interpretation & Limitation
Demonstrates why absolute rebound values should be interpreted carefully across different cells. The available evidence does not establish different manufacturing batches; hence this case uses **Cell-to-cell variation** rather than batch variation.

---

## Evidence C — Rest-Time Dependence

### Observation
Rebound magnitude vs. elapsed rest duration:
- **5 min:** ~25 mV
- **30 min:** ~40 mV
- **60 min:** ~45 mV

*Growth Comparison:* **5 → 30 min (~1.6×)** vs. **30 → 60 min (smaller additional increase)**.

### What the data supports
Rebound magnitude depends on elapsed rest time and is non-linear across tested intervals.

### What the data does NOT prove
Does not establish a universal 5-minute-to-30-minute conversion formula. Field correction models require additional empirical calibration data.

---

## Evidence D — Single Measurements vs. Observed Trend

### Observation
Individual rebound measurements move substantially between consecutive observations (e.g., **38 → 45 → 36 mV**), while a 5-cycle moving average produces a smoother trajectory.

### What the data supports & Distinction
Single-point measurements contain short-term variation. A moving average provides temporal context, but a smoother curve does not automatically prove measurement error removal or true SOH ground truth.

---

# 3. Field Engineering Observations

*Observations derived from field engineering experience, distinct from single-cell laboratory datasets:*

* **3.1 Cell-Level Impedance Is Difficult to Measure in the Field:** System cannot be easily disassembled for controlled individual cell impedance tests.
* **3.2 Voltage Rebound Is a Practical Observable:** Post-discharge rebound offers useful signals over time but should not be equated directly to measured impedance.
* **3.3 Field Baselines Are Better Established Per Cell/System:** Relative change over time against cell-specific baselines is more reliable than absolute global thresholds.
* **3.4 Rest Time Is an Operational Compromise:** Extended rest periods conflict with BESS system availability; a 20–30 minute window is a practical engineering compromise.
* **3.5 Temperature Sensor Representativeness:** Limited sensors across a rack/cabinet introduce spatial temperature uncertainty for deep-seated cells.
* **3.6 Measurement Instrumentation Uncertainty:** Sensor resolution, V/I synchronization, and sampling rates add noise to dynamic estimates.
* **3.7 Infeasibility of Full Retesting:** Operational BESS diagnostics must work with existing field telemetry rather than full laboratory re-screening.

---

# 4. Engineering Inferences

1. **Rebound = Indirect Health Signal:** Useful indicator, but `Rebound ≠ directly measured impedance`.
2. **Cell-Specific Baselines Over Fixed Thresholds:** Focus on `Baseline → Current Value → Relative Growth`.
3. **Empirical Correction for Short Rest:** Requires time-dependent lookup tables or regression models for short diagnostic windows.
4. **Temperature Representativeness Matters:** Temperature compensation must account for spatial sensor placement limitations.
5. **Field SOH Is a Multi-Uncertainty Problem:** Field SOH is an indirect inference, not an absolute ground-truth measurement.

---

# 5. Industry Discussion

Reporting an SOH estimate as a single scalar (e.g., `SOH = 85%`) hides critical measurement context, rest time, baseline definitions, and model assumptions. A transparent engineering representation is conceptually expressed as:

$$\text{SOH Estimate} = 85\% \pm \text{Uncertainty}$$

*Note: Numerical uncertainty bounds must stem from validated uncertainty modeling rather than arbitrary intervals.*

---

# 6. Cross-Validation — Self-Contradiction Check

| Claim | Evidence / Basis | Status | Interpretation |
| :--- | :--- | :--- | :--- |
| **Rebound related to aging** | B0005 aging trend | Supported with limitation | Do not equate rebound with impedance |
| **Older B0005 shows larger rebound** | 35 → 85 mV | NASA evidence | Self-comparison; points fluctuate |
| **Cell-to-cell initial variation** | 35 / 45 / 32 mV | NASA evidence | Avoid absolute cross-cell thresholds |
| **Rest-time dependence** | 25 / 40 / 45 mV | NASA evidence | Linear extrapolation is insufficient |
| **Short-rest empirical correction** | Rest behavior + field limits | Engineering inference | Requires calibration models |
| **Single measurement fluctuations** | Individual rebound points | NASA evidence | Fluctuation ≠ automatic sensor error |
| **Stacked field uncertainty** | Multiple field constraints | Engineering inference | Central engineering interpretation |

---

# 7. Implication for Asset Valuation

An informative asset-health assessment must include:
1. SOH Estimate
2. Historical Trend
3. Measurement Conditions & Rest Time
4. Data Quality & Sensor Accuracy
5. Model Assumptions & Uncertainty Range

---

# 8. BESS Diagnostics Positioning

```text
Lab baseline 
  → Cell-to-cell variation 
  → Limited field retesting 
  → Temperature representativeness 
  → Short diagnostic windows 
  → Non-linear rest-time effects 
  → Sensor / synchronization uncertainty 
  → Indirect health estimation 
  → Single-point SOH 
  → Incomplete engineering interpretation
