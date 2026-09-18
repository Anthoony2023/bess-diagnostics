# DS-001 — B0005 Evidence Log

Evidence records are kept separate from interpretation.

| Evidence ID | Category | Evidence |
|---|---|---|
| E001-001 | File | B0005.mat downloaded successfully; HTTP 200; application/octet-stream; approximately 15.96 MB. |
| E001-002 | Structure | Top-level variable B0005 is a NumPy array with shape `(1,1)`. |
| E001-003 | Structure | Unwrapped cycle array has shape `(1,616)` with fields `type`, `ambient_temperature`, `time`, `data`. |
| E001-004 | Inventory | 616 records: 170 charge, 168 discharge, 278 impedance. |
| E001-005 | Schema | Charge records share one consistent field schema. |
| E001-006 | Schema | Discharge records share one consistent field schema. |
| E001-007 | Schema | Impedance records share one consistent field schema. |
| E001-008 | Statistics | Charge sample counts observed from 5 to 3900; mean approximately 3183; total approximately 541k points. |
| E001-009 | Statistics | Discharge sample counts observed from 179 to 371; mean approximately 299; total approximately 50k points. |
| E001-010 | Statistics | Impedance records contain 48 points each. |
| E001-011 | Time | Time exists in charge and discharge records and matches the number of time-series samples. |
| E001-012 | Time | Observed Time differences are not uniformly 1 second. |
| E001-013 | Capacity | Capacity exists in discharge records as a 1x1 float64 value. |
| E001-014 | Observation | Some charge records contain extremely few samples; minimum observed is 5; cause is not determined. |

## Evidence discipline

An evidence item records what was observed in the data or inspection process.

It is not, by itself, an explanation or engineering conclusion.
