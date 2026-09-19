# bess-diagnostics

> Public battery and BESS data, analyzed from an engineering rather than purely algorithmic perspective.

**Before deciding what is wrong, determine whether the data supports the conclusion.**

## What is this repo?

BESS diagnostics often requires inferring battery and system health from indirect measurements collected while the system remains in operation.

A single SOH value can hide important measurement context, operating conditions, and uncertainty.

This repository explores these problems through public battery and BESS datasets.

**Core approach: Data → Context → Analysis → Engineering Decision**

The goal is not simply to produce another health estimate, but to understand what the available data can — and cannot — support.

## Cases

### Case-001: When SOH Looks Wrong

- **Dataset:** NASA PCoE B0005
- **Question:** Can a single capacity measurement be trusted as a direct indicator of battery degradation?
- **Focus:** Capacity trend, measurement timing, impedance behavior, and operating context
- **Finding:** Capacity measurements can show short-term upward excursions within an overall declining trend. Measurement context matters when interpreting apparent health changes.

### Case-002: Why Single-Point SOH Is Questioned in the Field

- **Dataset:** NASA PCoE B0005 / B0006 / B0007 / B0018
- **Question:** Why can a field SOH estimate be questioned even when the underlying algorithm appears reasonable?
- **Focus:** Cell-to-cell variation, measurement timing, rest-time dependence, and longitudinal behavior
- **Data evidence:**
  - Different cells show different initial rebound values under the available test conditions.
  - B0005 shows an increase in rebound over the observed aging sequence.
  - Rebound changes with rest time and is not well represented by a simple linear relationship over the observed intervals.
  - Individual measurements show short-term variation, while a longitudinal view provides additional temporal context.
- **Finding:** Field SOH should be interpreted together with measurement context, longitudinal behavior, and uncertainty sources.

## Engineering Perspective

Field battery diagnostics may involve several interacting sources of uncertainty:

- Cell-specific baseline differences
- Measurement conditions and rest time
- Temperature and operating conditions
- Sensor accuracy and sampling characteristics
- Timing and signal synchronization
- Limited observability of internal battery state
- Uncertainty in interpreting derived health indicators

The practical engineering question is therefore not only:

> What is the SOH?

but also:

> **How much confidence does the available data support for that SOH estimate?**

Detailed diagnostic methods, correction models, thresholds, and customer-specific workflows are intentionally not published as part of these public case studies.

## Repo Map

```text
atlas/       - Dataset and project map
cases/       - Technical case studies and supporting evidence
methods/     - Reusable analysis methods
notebooks/   - Reproducible analysis notebooks
