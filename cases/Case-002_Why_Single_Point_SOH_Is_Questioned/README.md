# Case-002: Why Single-Point SOH Is Questioned in the Field

> **Data-First Version**
>
> *Independent BESS Diagnostics & Performance Analysis by Anthony Chou, Ph.D.*

**[Technical Brief PDF](./Case-002-V5-0-Final-Letter.pdf)** ·
**[BESS Diagnostics](https://bessdiag.com)** ·
**[LinkedIn](https://www.linkedin.com/in/anthony-chou-tw67/)**

---

## One-line Summary

A single SOH-related measurement can look different depending on the cell, the measurement sequence, and the elapsed rest time.

This case examines what the public data shows before applying additional engineering assumptions.

---

# 1. Engineering Question

### What changes when we look at a single battery-health-related measurement instead of its context over time?

This case does not attempt to establish a universal SOH method.

Instead, it examines several observable patterns in publicly available NASA battery data:

1. How rebound changes over an observed aging sequence
2. How rebound differs between cells
3. How rebound changes with elapsed rest time
4. How individual measurements compare with a longitudinal view

The analysis intentionally separates **observed data** from **engineering interpretation**.

---

# 2. NASA Data Evidence

## Dataset

NASA Battery Dataset: **B0005, B0006, B0007, B0018**

B0005 is the primary cell used in the analysis. Additional cells are examined to compare observed rebound behavior across different units.

---

## Evidence A — Rebound Over the Observed Aging Sequence

### Observation

For B0005:

- **Earlier observation:** ~35 mV
- **Later observation:** ~85 mV
- **Observed change:** ~2.4× increase

Individual observations fluctuate around the overall trajectory.

### What the data shows

The rebound magnitude is not constant throughout the observed B0005 sequence.

The dataset shows an overall increase while individual measurements continue to vary.

### What this does not establish

The data alone does not establish that rebound is equivalent to impedance or that a particular rebound value corresponds directly to a specific SOH value.

---

## Evidence B — Cell-to-Cell Variation

### Observation

Initial rebound values differ across the analyzed cells:

| Cell | Initial Rebound |
| :--- | ---: |
| **B0005** | ~35 mV |
| **B0006** | ~45 mV |
| **B0007** | ~32 mV |

**Observed spread: ~13 mV**

### What the data shows

The same type of measurement does not produce the same initial value across these cells.

The available dataset does not establish that the cells came from different manufacturing batches.

### What this does not establish

The data does not establish why these initial values differ.

---

## Evidence C — Rebound vs. Rest Time

### Observation

Observed rebound values increase with elapsed rest time:

| Rest Time | Rebound |
| :--- | ---: |
| 5 min | ~25 mV |
| 30 min | ~40 mV |
| 60 min | ~45 mV |

The increase between 5 and 30 minutes is larger than the additional increase between 30 and 60 minutes.

### What the data shows

The observed rebound value changes with elapsed rest time.

Across the tested intervals, the relationship is not well represented by a simple linear increase.

### What this does not establish

The available observations do not establish a universal conversion between rest time and rebound.

---

## Evidence D — Individual Measurements vs. Longitudinal View

### Observation

Individual rebound measurements can change substantially between consecutive observations.

Example:

**38 → 45 → 36 mV**

A 5-cycle moving average produces a smoother trajectory.

### What the data shows

Individual measurements contain short-term variation.

A longitudinal view provides additional temporal context that is not visible from one isolated measurement.

### What this does not establish

A smoother curve does not by itself establish measurement accuracy, remove measurement error, or represent ground-truth SOH.

---

# 3. What We Can Observe Across the Dataset

The four observations above show three different dimensions of variation:

### 1. Across time

B0005 rebound changes substantially over the observed sequence.

### 2. Across cells

Different cells show different observed initial rebound values.

### 3. Across measurement conditions

The observed rebound changes with elapsed rest time.

These effects can be observed directly before introducing an additional SOH model or correction method.

---

# 4. What the Data Does Not Tell Us

The available public data does **not**, by itself, answer all of the following questions:

- What rebound value corresponds to a specific SOH?
- What portion of the variation comes from impedance?
- What portion comes from measurement conditions?
- What rest-time correction should be applied in the field?
- Whether the same relationship applies to BESS modules or racks
- Whether the same behavior applies across different battery chemistries
- What uncertainty interval should be assigned to an SOH estimate

Those questions require additional data, validation, or engineering assumptions.

---

# 5. Engineering Interpretation

The immediate observation is simple:

> **The number changes depending on what we are comparing.**

A value viewed by itself contains less information than the same value viewed together with:

- its previous observations,
- the cell being measured,
- and the measurement conditions represented in the dataset.

This case therefore does not propose a new SOH algorithm.

It demonstrates why the **context surrounding a measurement can materially change how that measurement should be interpreted.**

---

# 6. Implication for BESS Diagnostics

The NASA dataset is a laboratory battery dataset, not a field BESS dataset.

Its value for this case is therefore not to reproduce a complete BESS diagnostic workflow.

Instead, it provides a controlled example of a broader diagnostic question:

> **Before interpreting a health-related number, what else in the data changes with that number?**

That question becomes more important when measurements are collected from an operating system rather than from a controlled laboratory test.

---

# 7. Core Takeaway

> **A single measurement is an observation.  
> Its meaning depends on the context in which it was obtained.**

This case starts with the data before applying a diagnostic model.

**Data → Context → Analysis → Engineering Decision**

---

## Evidence Boundary

This case intentionally distinguishes between:

- **Observed:** directly supported by the analyzed public dataset
- **Not established:** questions that cannot be answered from the available data alone
- **Engineering interpretation:** conclusions drawn from the observed patterns without claiming a universal model

No universal SOH algorithm, correction model, threshold, or uncertainty model is proposed in this public case.

---

## Reproducibility

The analysis uses publicly available NASA battery datasets.

Raw datasets are not stored in this repository.

Supporting figures and analysis artifacts are provided in the case directory where available.

---

## About

**Anthony Chou, Ph.D.**

Battery & BESS Engineering | Diagnostics | Performance | Degradation

Houston, Texas, USA

- Website: https://bessdiag.com/
- LinkedIn: https://www.linkedin.com/in/anthony-chou-tw67/
- GitHub: https://github.com/Anthoony2023/bess-diagnostics

---

**BESS Diagnostics**

*Before deciding what is wrong, determine whether the data supports the conclusion.*
