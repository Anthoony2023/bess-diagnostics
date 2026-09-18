# DS-001 — NASA PCoE B0005

## Dataset identity

- **Dataset:** NASA PCoE B0005
- **Level:** Single cell
- **Application:** Battery aging / degradation research
- **Primary record types:** Charge, discharge, impedance
- **Local inspection file:** `B0005.mat`
- **Repository role:** Battery-level methodological benchmark

## Source

NASA Prognostics Center of Excellence dataset.

NASA landing page:

https://ti.arc.nasa.gov/c/6/

The B0005 MATLAB file used for the Day 1 inspection was retrieved from a GitLab mirror:

https://labinfo.ing.he-arc.ch/ticc/16TICc19/nasa-battery-dataset/-/blob/614f3518915079a5182655cadc3492973ac90d6c/data/BatteryAgingARC-FY08Q4/B0005.mat

## Day 1 scope

The first inspection is limited to:

1. File retrieval and loading
2. Top-level structure
3. Record inventory
4. Record schemas
5. Sample-count statistics
6. Time-field presence and basic observations
7. Identification of unresolved questions

No downstream SOH, degradation, anomaly, or ML conclusion is made in Day 1.

## Initial classification

### Best for

- Li-ion single-cell degradation / SOH / RUL benchmark
- CC-CV charge analysis
- Capacity fade tracking

### Poor fit for

- BESS system diagnostics
- BMS / PCS timestamp alignment
- Multi-cell imbalance analysis

### Limitations observed from dataset scope

- Laboratory single-cell data
- Ambient temperature observed at 24°C in inspected records
- No system controller logs
- No AC-side data

These limitations describe the inspected dataset scope and should not be generalized beyond the available records.
