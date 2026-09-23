# Methods

**Scope.** This document describes the analysis specification associated with the published summaries. The original raw-analysis code and full event-level outputs are not included, so the specification cannot be independently checked against an executable implementation from this package alone. See [reproducibility and evidence availability](../REPRODUCIBILITY.md).

## Analysis scope

This is a **case study with public derived evidence**, not a turnkey reproduction package. The multi-gigabyte raw dataset is not redistributed here. Public CSVs expose the principal derived results, selected counter excerpts, and operating support. Metric definitions and unexposed implementation details are documented separately.

## Analysis discipline

1. Preserve raw source files and the original codebook.
2. Validate timestamps, units, signs, and physical consistency before using a signal analytically.
3. Evaluate coverage and valid-data support separately by year and stream.
4. Prefer power integration for throughput when cumulative counters show reconstruction anomalies.
5. Separate recorded command changes from observed output changes.
6. Restrict tracking conclusions to the operating envelope actually observed.
7. Treat common-condition filtering as filtering, not as strict distribution matching.
8. State explicitly what each metric does **not** prove.

## Power-unit validation

BMS DC power was compared with:

`P_VI_kW = voltage_bat_V_bms * current_A_bms / 1000`

Only finite, non-sentinel, active-power observations were used. This is a cross-register physical-consistency check, not an independent instrument calibration.

## Throughput integration and gap handling

Energy is integrated using a **right-endpoint rectangular rule**. For row `i`:

`dt_i = t_i - t_(i-1)`

`E_i_kWh = P_i_kW * dt_i_seconds / 3600`

The unsigned throughput term uses `abs(P_i_kW)`; charge and discharge are separated by the sign convention. Divide kWh by 1000 for MWh.

Rules:

- timestamp must be finite;
- valid interval: `0 < dt <= 5 s`;
- duplicate/non-positive intervals are excluded;
- if `dt > 5 s`, that interval contributes **zero** energy;
- the interval is not shortened or replaced with 5 s;
- annual processing starts without cross-year carry, so the first row of each annual file contributes zero duration;
- signal-specific finite/range masks are applied before integration.

The yearly coverage/quality table is published in `data/coverage_quality_2017_2025.csv`. These metrics describe usable data time, not hardware availability.

## PQ-mode flag naming

The source field used in operating-profile and tracking analyses is:

- derived name: `flag_fcr_active_bsc`
- source register: `x_BSC_Opmode_PQ`

The source codebook states that it represents **PQ-regulation mode** and is predominantly associated with FCR, but is not an exclusive FCR indicator. Public outputs therefore use **PQ-mode active hours**.

## Operating-profile comparison

Actual AC power and recorded supervisory setpoint are integrated over their valid observed intervals. The public annual ratio is the quotient of the reported absolute-energy totals. The original specification describes jointly valid intervals for the ratio, but the public summary contains no row-level integration mask or joint-support audit that can independently verify this. It is therefore used as an aggregate operating indicator, not a dynamic-tracking performance test.

The 2022-2024 comparison shows that actual throughput and recorded command energy decline together. Throughput alone does **not establish** an equivalent capacity-loss percentage, does not exclude concurrent degradation, and does **not** identify why the upstream command itself declined.

Possible upstream causes such as derating, SOC protection, availability logic, or dispatch policy are not resolved by this case.

## Exact timestamp pairing

For analyses that pair annual BMS and BSC files, the files first must have equal row counts and then paired rows are checked for exact timestamp equality. `paired_timestamp_mismatch_rows = 0` therefore describes the paired records used by the analysis. It does **not** prove that neither source has missing samples relative to an external clock, nor does it establish zero physical sensor latency.

## Common-condition slow-ramp tracking

The published table `data/matched_tracking_common_condition_slow_ramp_2022_2024.csv` uses:

- BMS/BSC exact timestamp pairing within the paired annual files;
- SOC 55-65%;
- **battery-cabinet air temperature** 20-25 C;
- source PQ-mode flag = 1;
- `|setpoint ramp| <= 5 kW/s`;
- command bins from 50 to 700 kW;
- charge and discharge separately.

`tracking_ratio_projected` is:

`integral(P_actual * sign(P_setpoint) dt) / integral(|P_setpoint| dt)`

This is a command-following metric, not efficiency. The table exposes hours for every bin so sparse bins can be identified directly. In particular, the 450-700 kW discharge rows in 2023 and 2024 contain only about 27 s and 26 s and are not used as representative high-power evidence.

## Fine common-cell residual comparison

The 2022-vs-2024 discharge residual uses common operating-condition cells defined by:

- setpoint: 25 kW bins;
- SOC: 2% bins;
- battery-cabinet air temperature: 1 C bins;
- broad range: SOC 55-65%, temperature 20-25 C;
- slow-ramp criterion: `<= 5 kW/s`;
- each fine cell must have at least **0.05 h in each year**.

For each common cell, energy terms are time integrals over the same valid rows:

- `ac_tracking_ratio = sum(P_AC dt) / sum(P_setpoint dt)`
- `dc_to_setpoint_ratio = sum(P_DC dt) / sum(P_setpoint dt)`
- `ac_over_dc_ratio = sum(P_AC dt) / sum(P_DC dt)`

The reported band summary is a weighted average of cell-level ratios using:

`weight = min(hours_2022, hours_2024)`

`matched_support_hours` is the sum of those common-support weights. It is not contiguous experimental time.

`common_cells` means common **operating-condition bins**, not physical battery cells.

`mean_cell_voltage_V` is computed from time-weighted **BMS string voltage divided by the active series-cell count**. The residual comparison uses 300 cells for 2022 and 299 cells for 2024.

`ac_over_dc_ratio > 1` is treated as an unresolved measurement/tracking consistency issue. Channel scaling or bias, latency, measurement boundaries, transients, and aggregation are candidate checks, not established explanations. No efficiency or direct battery-loss inference is made. A below-unity ratio alone is also insufficient validation. Weighted averages of cell-level ratios need not satisfy the algebraic identity between ratios of band-level totals.

## Field DCIR event definition

Field DCIR uses the **BSC-side DC channels**:

- `voltage_bat_V_bsc` / source `w_U_DC_Batt`: DC battery voltage measured at the inverter DC input;
- `current_A_bsc` / source `i_I_DC_Batt`: DC battery current measured at the inverter DC input.

The source codebook distinguishes this measurement point from the BMS battery-pole measurement. Consequently, this metric is an apparent string-path voltage/current response at the stated boundary, not isolated cell-internal ohmic resistance. Five-sample averaging can include polarization, connection/cable, and measurement-response effects; no unique contribution is identified here.

The temperature covariate `temperature_degC_bsc` / `i_T_Batt` is a **single-point battery-cabinet air temperature** relayed through the BSC, not a cell-temperature measurement.

A candidate transition occurs when the sign of current changes between adjacent samples. For each candidate:

1. take the **five samples immediately before** and **five immediately after** the transition;
2. require all 10 timestamps to be finite and exactly consecutive at **1-second spacing**;
3. require all current, voltage, and cabinet-temperature samples to be finite;
4. compute arithmetic means of pre-transition current/voltage and post-transition current/voltage;
5. require mean pre/post current to remain opposite in sign;
6. require `|dI| >= 10 A`;
7. calculate `R_string = -dV/dI`, where `dV = mean(V_post) - mean(V_pre)` and `dI = mean(I_post) - mean(I_pre)`, because positive current denotes discharge;
8. retain only finite positive `0 < R_string < 2 ohm` events;
9. de-duplicate batch-overlap duplicates by `(event_timestamp_UTC, direction)`.

Per-cell resistance normalization is reported as **per event timestamp**, using this analysis configuration:

- 300 series cells before `2023-08-10T00:00:00Z`;
- 299 series cells from that timestamp onward.

The codebook confirms 300 series cells and a 2023 bypass to 299. The exact cutoff is an analysis configuration; an operational record confirming that cutover time is not included. This qualification affects the provenance of per-cell normalization, not the arithmetic of the headline string-DCIR change.

Exact-timestamp BMS SOC is attached without interpolation.

The published annual DCIR summary then applies a **common-condition filter**:

- SOC 50-70%;
- cabinet-air temperature 15-30 C;
- `|dI|` 50-500 A.

This is not a distribution-matched or pair-matched aging estimate. Events can occupy different distributions within those bands in different years. P25/P75 are event-distribution quartiles, not confidence intervals.

`common_R_vs_2018_pct` is an **index with 2018 = 100**, not a percentage increase from the baseline.

## Counter evidence scope

`evidence/counter_anomaly_examples.csv` publishes source annual Parquet filenames, UTC time-of-day, and the pre/spike/post values for four examples. The numerical word-swap relationship can be independently checked from the table.

The public package does **not** contain the full UTC date for those four excerpts. They are therefore arithmetic-verifiable examples with partial source locators, not complete raw-window reproduction coordinates.

## Interpretation boundaries

This case does not equate:

- annual throughput decline with capacity loss;
- lower recorded command energy with a known upstream causal mechanism;
- tracking inside the selected envelope with full-range capability;
- command tracking with electrochemical SOH;
- AC/DC ratios with round-trip efficiency;
- common-condition filtering with strict distribution matching;
- field DCIR with laboratory HPPC resistance;
- resistance rise with an identical percentage of capacity loss or a unique degradation mechanism.
