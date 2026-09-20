# bess-diagnostics

> Public battery and BESS data, analyzed from an engineering rather than purely algorithmic perspective.

**"Before deciding what is wrong, determine whether the data supports the conclusion."**

---

## What is this repo?

Field battery diagnostics requires inferring battery and system health from indirect measurements collected while the system remains in operation. A single SOH value can hide important measurement context, operating conditions, and underlying physical relaxation.

This repository explores these diagnostic challenges through public battery and BESS datasets.

**Core approach:** `Data` → `Context` → `Analysis` → `Engineering Decision`

The goal is not simply to produce another health estimate, but to determine what the available data can — and cannot — support before making operational or maintenance decisions.

---

## Cases

### [Case-001: When SOH Looks Wrong](./cases/Case-001_When_SOH_Looks_Wrong)
- **Dataset:** NASA PCoE B0005
- **Question:** Can a single capacity measurement be trusted as a direct indicator of battery degradation?
- **Focus:** Capacity trend, measurement timing, relaxation behavior, and operating context.
- **Finding:** Capacity measurements can show short-term upward excursions within an overall declining trend. Measurement context and persistence matter when interpreting apparent health changes.
- **Artifacts:** [Case Folder](./cases/Case-001_When_SOH_Looks_Wrong) · [One-Pager PDF](./cases/Case-001_When_SOH_Looks_Wrong/docs/Case-001_One_Pager_External.pdf)

### [Case-002: Why Single-Point SOH Is Questioned in the Field](./cases/Case-002_Why_Single_Point_SOH_Is_Questioned)
- **Dataset:** NASA PCoE B0005 / B0006 / B0007 / B0018
- **Question:** Why can a field SOH estimate be questioned even when the underlying algorithm appears reasonable?
- **Focus:** Cell-to-cell variation, rest-time dependence, and longitudinal behavior.
- **Data Evidence:**
  - Different cells show different initial rebound values under identical test conditions.
  - Rebound changes with rest time and is non-linear across observed intervals.
  - Individual measurements contain short-term noise, whereas longitudinal data provides necessary temporal context.
- **Finding:** Field SOH must be interpreted together with measurement context, longitudinal trends, and uncertainty sources.
- **Artifacts:** [Case Folder](./cases/Case-002_Why_Single_Point_SOH_Is_Questioned) · [Technical Brief PDF](./cases/Case-002_Why_Single_Point_SOH_Is_Questioned/Case-002-V5-0-Final-Letter.pdf)

---

## Engineering Perspective

Field battery diagnostics involves several interacting sources of uncertainty:

- Cell-specific baseline differences and manufacturing variation
- Measurement conditions and post-load rest/relaxation time
- Temperature fluctuations and field operating limits
- Sensor accuracy, noise, and sampling rate synchronization
- Limited observability of internal electrochemical states
- Uncertainty propagation in derived health metrics (SOH/RUL)

The practical engineering question is therefore not only:
> *"What is the estimated SOH?"*

but more importantly:
> **"How much confidence does the available data support for that SOH estimate?"**

*Note: Detailed diagnostic thresholds, proprietary correction models, and customer-specific workflows are intentionally omitted from these public case studies.*

---

## Repo Map

```text
atlas/       - Dataset index and project map
cases/       - Technical case studies and supporting evidence
methods/     - Reusable diagnostic methodologies and metrics
notebooks/   - Reproducible data analysis notebooks
