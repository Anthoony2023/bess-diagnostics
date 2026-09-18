# DS-001 — B0005 Day 1 Data Inspection

## Objective

Determine the actual structure of the dataset before making any engineering assumptions.

## File verification

- File: `B0005.mat`
- HTTP status: 200
- Content-Type: `application/octet-stream`
- Downloaded size: approximately 15.96 MB
- Loaded successfully with `scipy.io.loadmat`

## Top-level structure

The MATLAB file contains:

- `B0005`: NumPy array
- Shape: `(1, 1)`

After unwrapping, the `cycle` array has:

- Shape: `(1, 616)`
- Fields:
  - `type`
  - `ambient_temperature`
  - `time`
  - `data`

## Record inventory

| Record type | Count |
|---|---:|
| Charge | 170 |
| Discharge | 168 |
| Impedance | 278 |
| **Total** | **616** |

The 616 entries are records in the cycle array. They should not automatically be interpreted as 616 normal engineering battery cycles because impedance records are included.

## Record schemas

### Charge

Fields:

- `Voltage_measured`
- `Current_measured`
- `Temperature_measured`
- `Current_charge`
- `Voltage_charge`
- `Time`

Exactly one schema was observed across the inspected charge records.

### Discharge

Fields:

- `Voltage_measured`
- `Current_measured`
- `Temperature_measured`
- `Current_load`
- `Voltage_load`
- `Time`
- `Capacity`

Exactly one schema was observed across the inspected discharge records.

### Impedance

Fields:

- `Sense_current`
- `Battery_current`
- `Current_ratio`
- `Battery_impedance`
- `Rectified_Impedance`
- `Re`
- `Rct`

Exactly one schema was observed across the inspected impedance records.

## Sample-count observations

### Charge

- Minimum: 5 samples
- Maximum: 3900 samples
- Mean: approximately 3183 samples
- Total: approximately 541k points

### Discharge

- Minimum: 179 samples
- Maximum: 371 samples
- Mean: approximately 299 samples
- Total: approximately 50k points

### Impedance

- 48 points per impedance record

## Time field

`Time` is present in charge and discharge records and has the same sample count as the measured time-series channels.

Observed `Time` differences are not uniformly 1 second.

The sampling regularity has therefore not yet been characterized.

## Short charge records

Some charge records contain extremely few samples.

The minimum observed charge-record sample count is 5.

At this stage, the cause is **not determined**.

Do not infer end-of-life causation from this observation alone.

## Current Day 1 conclusion

The dataset structure is sufficiently understood to proceed to a more focused technical question, but several metadata and interpretation questions remain unresolved.

Day 1 does not establish:

- Capacity units
- Time units
- Sampling regularity
- A formal SOH definition
- An EOL definition
- The cause of extremely short charge records

See `evidence.md` for traceable observations.
