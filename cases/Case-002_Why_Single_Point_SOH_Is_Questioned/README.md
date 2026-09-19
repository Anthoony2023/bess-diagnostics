# Case-002 — Why Single-Point SOH Is Questioned in the Field

> A public case study on interpreting battery health estimates under real-world measurement uncertainty.

## Engineering Question

Why can a field SOH estimate be questioned even when the underlying algorithm appears reasonable?

The challenge is not simply calculating SOH.

It is determining **how much confidence the available data actually supports**.

---

## Dataset

NASA PCoE Battery Dataset

Cells used for cross-cell analysis:

- B0005
- B0006
- B0007
- B0018

Source:

https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/

The raw `.mat` files are not stored in this repository.

---

# What the Data Shows

## Evidence A — Aging-Related Rebound Trend

For B0005, voltage rebound after discharge generally increases over the observed aging sequence.

Representative observations show rebound values increasing from approximately:

**35 mV → 85 mV**

Individual measurements still show short-term variation.

This demonstrates that the observed signal contains both:

- an underlying longitudinal change
- measurement-to-measurement variation

The result should therefore not be interpreted from a single observation alone.

---

## Evidence B — Cell-to-Cell Variation

Initial rebound measurements differ between cells under the available test conditions.

Representative values:

- B0005: ~35 mV
- B0006: ~45 mV
- B0007: ~32 mV

The observed spread is approximately 13 mV.

This is an important distinction for field diagnostics:

> An absolute threshold that is meaningful for one cell is not automatically transferable to another cell.

Cell-specific baseline and longitudinal behavior can provide additional context.

---

## Evidence C — Rest-Time Dependence

The observed rebound changes with the time allowed after discharge.

Representative B0005 observations include approximately:

- 5 min: ~25 mV
- 30 min: ~40 mV
- 60 min: ~45 mV

The change is not well represented by a simple linear relationship over these intervals.

This matters because field measurements are often constrained by operational availability.

A measurement taken after a short rest period should therefore be interpreted in the context of the measurement protocol rather than compared directly with a longer-rest reference.

---

## Evidence D — Single Measurements vs. Longitudinal Trend

Individual rebound measurements show short-term variation.

A moving-average representation provides a smoother view of the observed longitudinal behavior.

This does **not** mean that smoothing automatically makes an estimate more accurate.

Instead, it demonstrates an important diagnostic principle:

> A single measurement provides limited temporal context; a sequence of measurements provides additional information about the underlying behavior.

---

# Why Field SOH Is Difficult

The laboratory signal itself is only part of the problem.

In a field BESS, an SOH estimate may depend on multiple layers of uncertainty, including:

### Baseline uncertainty

Cells are not necessarily identical even when they share the same nominal model.

### Measurement-context uncertainty

Rest time, operating condition, temperature, current, and measurement procedure can affect the observed response.

### Observability limitations

The internal state of a battery cannot always be measured directly while the system remains in normal operation.

### Measurement uncertainty

Sensor accuracy, sampling characteristics, timing, and signal synchronization can affect derived health indicators.

### Interpretation uncertainty

An observed change in a health indicator does not automatically identify the physical cause of that change.

These factors can interact rather than appearing independently.

---

# Engineering Approach

Field SOH should be treated as an **inference problem**, rather than as a direct measurement.

The diagnostic process therefore considers:

- cell-specific baseline
- measurement conditions
- temporal behavior
- available operating context
- data quality
- uncertainty sources

before assigning confidence to an SOH estimate.

The objective is not simply to produce another SOH number.

It is to determine:

> **What does the available data support, and what does it not support?**

---

# Implication for BESS Diagnostics

For asset or operational decisions, a single SOH value can hide important context.

A more useful diagnostic view considers:

**SOH estimate + measurement context + longitudinal behavior + uncertainty**

rather than treating the SOH number as an isolated ground truth.

The exact uncertainty model, correction method, thresholds, and customer-specific diagnostic workflow depend on the available system data and are outside the scope of this public case study.

---

# Limitations

This case uses laboratory single-cell data.

It does not directly reproduce:

- multi-cell BESS operation
- module-level thermal gradients
- BMS / EMS / PCS interactions
- field sensor placement
- real-world communication timing
- operational constraints of an installed energy-storage system

Field engineering observations are therefore presented as engineering context, not as conclusions proven by the NASA dataset.

---

# Engineering Takeaway

A field SOH estimate should be interpreted together with its:

**measurement context, longitudinal behavior, and uncertainty sources.**

The practical challenge is not only calculating SOH.

It is determining **how much confidence the available data supports**.

---

# Reproduction

The repository contains supporting analysis material for the case.

The NASA `.mat` files are not included in the repository.

Current analysis scripts are maintained as supporting work and may not reproduce every figure in the case automatically.

---

# Repository Structure

```text
Case-002_Why_Single_Point_SOH_Is_Questioned/
│
├── README.md
│
├── docs/
│   └── field-observations-11-points_2.md
│
├── evidence/
│   └── Supporting figures and analysis outputs
│
└── src/
    ├── rebound_analysis.py
    └── trend_vs_single.py
