# Public evidence index

Each principal claim below links to the evidence included in this case. The tables are derived summaries, not complete raw-sample exports.

| ID | Claim | Evidence | Scope |
|---|---|---|---|
| E01 | BMS DC power is numerically kW-scale despite the source W label | [Power/V-I validation](../data/power_vi_unit_validation_2017_2025.csv) | Cross-register consistency; not independent calibration |
| E02 | Four cumulative-energy excerpts satisfy temporary 16-bit word-swap arithmetic | [Counter excerpts](counter_anomaly_examples.csv) | Partial source locator: annual file and UTC time-of-day, without full UTC date |
| E03 | Observed throughput decline accompanies lower recorded command energy | [Operating profile](../data/operating_profile_2022_2024.csv), [Figure 1](../figures/figure_01_dispatch_vs_throughput.png) | Does not identify why commands declined or quantify capacity loss |
| E04 | Selected-envelope tracking does not decline comparably to annual throughput | [Tracking bins](../data/matched_tracking_common_condition_slow_ramp_2022_2024.csv), [Support](../data/matched_tracking_support_2022_2024.csv) | Common-condition slow-ramp subset; sparse high-power rows are not representative |
| E05 | A smaller discharge-side AC/DC/setpoint discrepancy remains in common operating bins | [Residual comparison](../data/residual_discharge_decomposition_2022_2024.csv), [Definitions](../methods/METRIC_DEFINITIONS.md) | Common-support weighting; unresolved AC/DC consistency prevents direct efficiency or battery-loss attribution |
| E06 | Common-condition-filtered apparent BSC-side string-path resistance rises from 2022 to 2024 | [DCIR summaries](../data/dcir_summary_2017_2025.csv), [Direction check](../data/dcir_direction_check_2017_2025.csv), [Figure 2](../figures/figure_02_common_condition_dcir.png) | Filtering is not strict distribution matching; no direct capacity-loss estimate |
| E07 | Usable-data coverage differs materially across historical BMS/BSC records | [Coverage and quality](../data/coverage_quality_2017_2025.csv) | Data coverage, not hardware availability |

The [evidence matrix](evidence_matrix.csv) separates supported conclusions from unsupported interpretations. The [signal-trust table](data_trust_table.csv) maps each signal to its analytical use and caveat.

The original time series is available from the dataset cited in the [README](../README.md). See [reproducibility and evidence availability](../REPRODUCIBILITY.md) for the distinction between checking these summaries and reproducing the raw-data analysis.
