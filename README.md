# bess-diagnostics

> Bridging the lab-to-field gap in battery and BESS health diagnostics.

**Before deciding what is wrong, determine whether the data supports the conclusion.**

[Cases](#cases) | [Decision relevance](#decision-relevance) | [Evidence and reproducibility](#evidence-and-reproducibility)

## What is this repo?

Independent public-data case studies examining what battery measurements can support before they are used to judge health or make asset decisions.

The focus is not a state-of-health (SOH) number in isolation. It is the evidence behind it: signal validity, measurement context, change relative to a documented baseline, and the uncertainty that remains.

**Core approach:** `Data` → `Context` → `Analysis` → `Engineering Decision`

The cases progress from laboratory-cell observations to telemetry from an operating battery energy storage system (BESS). The aim is to make diagnostic conclusions traceable and useful for operational investigation, maintenance prioritization, and technical due diligence.

For operating BESS diagnostics, start with **[Case-003](cases/Case-003_Can_the_BMS_Data_Be_Trusted/)**. Cases 001 and 002 establish the measurement-context foundation.

## Cases

### [Case-001: When SOH Looks Wrong](cases/Case-001_When_SOH_Looks_Wrong/)

**Dataset:** NASA PCoE B0005 - laboratory lithium-ion cell.

**Question:** Does a short-term increase in measured capacity mean that a battery has recovered?

**Finding:** The analyzed capacity record contains upward excursions within an overall declining trend. The timing and impedance evidence do not establish a single physical cause for those excursions.

**Decision relevance:** Check measurement history and persistence before treating an isolated capacity change as recovery or accelerated degradation. This is a laboratory observation, not a field BESS performance validation.

[Case and evidence](cases/Case-001_When_SOH_Looks_Wrong/) | [One-page PDF](cases/Case-001_When_SOH_Looks_Wrong/docs/Case-001_One_Pager_External.pdf)

### [Case-002: Why Single-Point SOH Is Questioned in the Field](cases/Case-002_Why_Single_Point_SOH_Is_Questioned/)

**Dataset:** NASA PCoE B0005 / B0006 / B0007 / B0018 - laboratory lithium-ion cells.

**Question:** How do cell identity, elapsed rest time, and measurement history affect the interpretation of a health-related signal?

**Finding:** Observed voltage rebound differs across the analyzed cells and varies with rest time and the aging sequence. A longitudinal view adds context, but neither a rebound value nor a smoother trend establishes ground-truth SOH.

**Decision relevance:** Examine each cell's baseline and measurement conditions before comparing absolute values or inferring degradation. The case demonstrates the need for diagnostic context, not a universal rebound-to-SOH conversion.

[Case and evidence](cases/Case-002_Why_Single_Point_SOH_Is_Questioned/) | [Technical brief PDF](cases/Case-002_Why_Single_Point_SOH_Is_Questioned/Case-002-V5-0-Final-Letter.pdf)

### [Case-003: Can the BMS Data Be Trusted?](cases/Case-003_Can_the_BMS_Data_Be_Trusted/)

**Dataset:** M5BAT Pb1 / Exide1 - operating flooded lead-acid storage unit; BMS and converter telemetry, 2017-2025, with partial years and variable usable coverage.

**Question:** How can telemetry defects, recorded command changes, and battery-health signals be separated?

**Finding:** The audit identifies a power-unit inconsistency and counter spikes consistent with word-swap artifacts. From 2022 to 2024, observed absolute AC throughput fell **78.0%**, while recorded command energy fell **77.4%**. Separately, a common-condition-filtered apparent field string-path resistance indicator rose about **15.1%**.

**Decision relevance:** Separate signal validation, dispatch/limit review, and battery-health verification before drawing maintenance or replacement conclusions. Throughput decline is not a direct capacity-loss measurement; the resistance indicator is not a strictly condition-matched aging estimate. Neither result identifies a unique root cause or rules out concurrent degradation.

[Case and evidence](cases/Case-003_Can_the_BMS_Data_Be_Trusted/) | [Technical brief PDF](cases/Case-003_Can_the_BMS_Data_Be_Trusted/Case-003_Technical_Brief.pdf) | [Methods](cases/Case-003_Can_the_BMS_Data_Be_Trusted/methods/METHODS.md)

## Engineering approach

| Step | Questions to resolve |
|---|---|
| **Validate the signals** | Are units, signs, timestamps, counter behavior, coverage, and cross-signal checks consistent enough for the intended use? |
| **Establish comparison context** | Are temperature, state of charge, load, rest time, measurement boundary, and operating mode sufficiently comparable? |
| **Interpret change over time** | Is a change persistent relative to a documented baseline? Could changing conditions, sensor behavior, or operating limits explain it? |
| **Bound the conclusion** | What support and uncertainty are visible, which causes remain unresolved, and what evidence is needed before acting? |

A point estimate can be useful when its definition, conditions, and limitations are explicit. A baseline-relative trend adds temporal context, but does not automatically remove measurement bias or operating-condition differences.

## Decision relevance

The commercial relevance is **technical due diligence**: make health and performance assumptions inspectable before they influence operational or asset decisions.

| Use case | How the diagnostic workflow can inform it |
|---|---|
| **Operations and maintenance** | Prioritize signal checks, supervisory-limit review, and targeted health verification rather than treating every anomaly as a battery fault. |
| **Asset valuation** | Identify which health or performance assumptions are supported and what additional capacity, capability, or operating evidence is needed. |
| **Insurance risk assessment** | Make the evidence and limitations behind reported health or performance claims explicit for further technical review. |

These are intended decision-support applications, not demonstrations of asset pricing, underwriting outcomes, avoided replacement costs, or verified site recovery.

## Evidence and reproducibility

Each case distinguishes **observations**, **engineering interpretation**, and **unresolved questions**. Available figures, derived tables, metric definitions, and analysis artifacts are linked within the case directories.

Python scripts support published checks where provided. [Case-003's reproducibility statement](cases/Case-003_Can_the_BMS_Data_Be_Trusted/REPRODUCIBILITY.md) explains what its validation script checks and what remains unavailable. Summary arithmetic and file-integrity checks do not reproduce the original time-series analysis.

The cases span different data sources and chemistries; they are **not a common-method, cross-dataset validation benchmark**. Laboratory observations and lead-acid operating thresholds should not be transferred directly to lithium-ion BESS. Discussing uncertainty sources is also not equivalent to publishing a calibrated uncertainty model.

These studies do not certify SOH, predict remaining useful life, or authorize protection-setting or return-to-service decisions.

## Repository map

```text
atlas/       Dataset index and project map
cases/       Case narratives, supporting evidence, and technical briefs
methods/     Shared diagnostic method notes
notebooks/   Analysis notebook workspace
```

Artifact availability and reproduction scope are case-specific.

## Data sources and licensing

**NASA laboratory data:** [NASA PCoE Li-ion Battery Aging Datasets](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets).

**M5BAT field data:** [RWTH dataset record](https://publications.rwth-aachen.de/record/1038622), DOI [10.18154/RWTH-2026-06637](https://doi.org/10.18154/RWTH-2026-06637). Full attribution and analysis-specific details are provided in Case-003.

Repository code and documentation are covered separately by [LICENSE-CODE](LICENSE-CODE) and [LICENSE-DOCS](LICENSE-DOCS). Third-party datasets retain their source attribution and licensing terms. No endorsement by the dataset providers or system operator is implied.

---

**Anthony Chou, Ph.D.** | Battery & BESS Engineering

[BESS Diagnostics](https://bessdiag.com/) | [LinkedIn](https://www.linkedin.com/in/anthony-chou-tw67/)
