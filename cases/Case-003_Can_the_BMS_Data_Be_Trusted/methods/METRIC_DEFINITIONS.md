# Metric definitions

## `actual_abs_over_command_abs`

`reported abs_throughput_MWh / reported command_abs_MWh`

The reported intended calculation is `sum(|P_actual| dt) / sum(|P_setpoint| dt)` on jointly valid intervals. The public table exposes the energy totals but not the row-level mask or a joint-support audit. The package checker verifies the quotient only. Interpret it as an annual aggregate observed-energy ratio, not independent proof of dynamic tracking or identical integration support. It falls from about 0.9745 in 2022 to 0.9522 in 2024.

## `tracking_ratio_projected`

`sum(P_actual * sign(P_setpoint) dt) / sum(|P_setpoint| dt)`

Used in the common-condition slow-ramp table. Opposite-sign response reduces the numerator. The result is interpreted only inside the observed operating envelope.

## Tracking support

`hours` is the integrated valid duration in each direction/setpoint bin after the common-condition and slow-ramp filters. The public table exposes this value rather than imposing a post-hoc universal support threshold.

The 2023 and 2024 discharge 450-700 kW rows have about 27 s and 26 s of support and are explicitly treated as sparse/non-representative.

## `matched_support_hours`

For each fine setpoint/SOC/temperature operating-condition cell:

`w_cell = min(hours_2022, hours_2024)`

The published band support is `sum(w_cell)`.

It is a common-support weighting quantity, not contiguous experimental duration.

## `common_cells`

Count of common **operating-condition bins** retained in both years. This field does not refer to physical battery cells.

## Residual AC/DC ratios

Within each common fine cell:

- `ac_tracking_ratio = sum(P_AC dt) / sum(P_setpoint dt)`
- `dc_to_setpoint_ratio = sum(P_DC dt) / sum(P_setpoint dt)`
- `ac_over_dc_ratio = sum(P_AC dt) / sum(P_DC dt)`

Band-level values are weighted averages of cell-level ratios using common-support weights; they are not ratios of band-level integrated totals. AC/DC above 1 is an unresolved consistency flag. Possible checks include scaling, bias, timing, electrical boundary, transients, and aggregation, without assigning a proven cause. No ratio in this table is a validated round-trip efficiency or direct battery-loss measure.

## `mean_cell_voltage_V`

Time-weighted BMS string voltage divided by the active series-cell count used by the analysis. For the published 2022-vs-2024 residual comparison, the normalization is 300 cells in 2022 and 299 cells in 2024. It is a derived normalization, not direct individual-cell voltage measurement.

## DCIR

`R_string = -dV/dI`

This is a five-sample pre/post apparent field string-path resistance at the BSC DC measurement boundary, not an isolated instantaneous cell resistance. The public DCIR series is common-condition filtered, not strictly distribution matched. The filter reduces obvious SOC/temperature/current-step confounding but does not equalize the full distributions across years.

## `common_R_vs_2018_pct`

A normalized **index**:

`100 * common_R_string_mohm_p50(year) / common_R_string_mohm_p50(2018)`

2018 therefore equals 100 by definition. Values above 100 are index levels, not percentage increases.

## Dimensional and support conventions

Power in kW multiplied by valid interval duration in seconds is divided by 3600 for kWh, and by a further 1000 for MWh. Absolute throughput includes both charge and discharge magnitudes; it is not usable capacity, net export, or revenue.

`calendar_year_fraction_pct = 100 * screened_valid_power_hours / calendar_year_hours`, using 8784 hours for a leap year and 8760 otherwise. Partial-year records retain the full-calendar denominator. This is data coverage, not hardware availability.

The ratios of `slow_common_condition_hours` to `valid_pq_command_hours` describe selection support within the reported valid PQ-command set. The public table does not expose every mask used to build that denominator, which must not be relabeled as total PQ-mode hours or all-calendar time.

`common_event_C_rate_p50`, the secondary MAE fields, and the secondary percentage diagnostics are included in the published tables. Their complete implementation conventions are not exposed; see [evidence availability](../REPRODUCIBILITY.md). No additional headline conclusion is based on these fields.
