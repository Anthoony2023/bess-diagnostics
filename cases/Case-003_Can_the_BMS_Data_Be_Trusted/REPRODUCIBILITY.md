# Reproducibility and evidence availability

## What is available

This case publishes derived CSV tables, selected counter excerpts, figures, an analysis specification, and metric definitions. It supports inspection of the reported findings and consistency checks across the published summaries. It is **not a complete raw-data reproduction environment**: the source time series and the original analysis pipeline are not included.

The annual observed-energy ratio can be recalculated from the published totals. Agreement with that quotient does not establish an identical underlying valid-time mask. Projected tracking is defined separately for the selected operating envelope; neither metric establishes capability outside the observed conditions.

## Check the published package

From this case directory, run Python 3.10 or newer:

```bash
python scripts/validate_package.py
```

No third-party packages or raw-data download are required. The command is read-only by default and returns a nonzero exit status on failure. It checks:

- MANIFEST file sizes and SHA-256 hashes, local Markdown file links, and evidence-table targets;
- CSV schemas, annual energy arithmetic, tracking support, DCIR summary consistency, and residual aggregation;
- the four published counter word-swap equalities and the presence of the PDF and figure file signatures.

These checks assess **published-summary consistency and file integrity**, not raw-sample validity, calibration, causal attribution, PDF appearance, external website availability, or operational readiness. The script does not re-create the figures or perform the original time-series analysis.

`MANIFEST.csv` covers the distributed files other than itself. Hashes detect changes; they do not independently authenticate the underlying measurements. Readers modifying a local copy can regenerate its manifest with `python scripts/validate_package.py --write-manifest`; this updates the integrity baseline, not the scientific validation status.

## Evidence needed for fuller reproduction

| Item | Published here | Additional evidence needed |
|---|---|---|
| Counter excerpts | Annual source file, UTC time-of-day, and pre/spike/post values | Full UTC dates or complete searchable event windows |
| Unit-validation summaries | Yearly errors and sign agreement | Exact active-power cutoff, range/sentinel masks, and original implementation |
| Annual energy and support | Energy totals and selected support summaries | Joint-validity masks, denominator construction, and raw sample counts |
| Broad-bin secondary diagnostics | MAE and percentage fields | Exact weighting, thresholds, and bin-boundary conventions; the headline conclusions do not depend on these secondary fields |
| Fine common-bin residuals | Band summaries, bin widths, minimum support, and weighting definition | Fine-cell rows, bin origins/edge conventions, and sample masks |
| DCIR events | Annual and direction summaries; event specification | Event table, timestamp convention, accepted/rejected counts, SOC/temperature/current-step distributions, and original implementation |
| Series-cell cutoff | Analysis normalization cutoff `2023-08-10T00:00:00Z` | Operational record confirming the exact bypass time; the codebook identifies the 2023 300-to-299 change, not its precise timestamp |
| C-rate covariate | `common_event_C_rate_p50` | Nominal Ah denominator and event-current definition |
| Causality and business outcomes | Diagnostic hypotheses and evidence requests | Maintenance, dispatch, and limit records; controlled health evidence; separately measured operational or financial outcomes |

Support hours are not independent event counts, P25/P75 are not confidence intervals, and matching timestamps does not establish sensor calibration or zero measurement latency. The partial counter locators and incomplete implementation conventions limit raw-data reproducibility even when every package check passes.

## Sources and attribution

**Dataset.** S. Zurmuehlen, L. Koltermann, and D. U. Sauer (2026), *M5BAT Large-Scale Battery Storage System: Dataset for Battery Unit Pb1 2017-2025*. [RWTH dataset record](https://publications.rwth-aachen.de/record/1038622), DOI [10.18154/RWTH-2026-06637](https://doi.org/10.18154/RWTH-2026-06637). The record labels the source dataset **CC BY 4.0**.

**Codebook.** [Description_File.pdf](https://publications.rwth-aachen.de/record/1038622/files/Description_File.pdf), generated 2026-07-09. Relevant sections cover BMS power/sign/series-cell notes (page 2), cabinet-air temperature (page 3), PQ-mode (page 4), and the BSC DC measurement boundary (page 5). Source-export energy reconstruction and this case's integration are not assumed to be identical implementations.

**Accompanying publication.** S. Zurmuehlen, L. Koltermann, and D. U. Sauer, *Operational Degradation of Flooded Lead-Acid Storage Under Frequency Containment Reserve: Long-Term Evidence from a Hybrid Multi-Technology BESS*, Energies 19(17), 4141 (2026). DOI [10.3390/en19174141](https://doi.org/10.3390/en19174141). Its conclusions are separate from this case's evidence claims.

The CSVs contain analysis-derived summaries and selected excerpts rather than the complete source dataset. Source-data attribution is distinct from the authorship of this case's analysis, text, and figures. No endorsement by the dataset authors or the system operator is implied.
