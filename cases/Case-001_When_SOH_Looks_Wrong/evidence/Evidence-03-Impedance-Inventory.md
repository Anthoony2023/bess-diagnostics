
# Evidence 03 — Impedance Inventory (Re / Rct)

## Purpose
Build basic inventory of 278 impedance records from B0005.mat. No correlation or causal claim yet.

## Source
- B0005.mat cycle[type=impedance]
- Fields: Re (Ohm) shape (1,1) -> float(data['Re'][0][0]), Rct shape (1,1) -> float(data['Rct'][0][0])
- global_idx range: 40 to 614
- impedance_idx: 0-277

## Inventory Summary
- Total records: 278
- Time field parsing: failed (shows 1970-01-01), use global_idx as sequence order instead (time gap evidence already in Evidence 02)
- Units: Ohm? TBD, keep as "Ohm - unit TBD"

| Metric | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|---|---|---|---|---|---|---|---|---|
| Re | 278 | 0.054245 | 0.005490 | 0.043559 | 0.049161 | 0.055850 | 0.058815 | 0.063516 |
| Rct | 278 | 0.077340 | 0.006367 | 0.064883 | 0.071511 | 0.077487 | 0.082563 | 0.089757 |

## Visual Evidence
See evidence image: B0005_Re_Rct_Inventory_278_records.png

- **Re (top, blue):**
  - Starts ~0.044-0.047 (idx 0-40)
  - Gradual increase to ~0.049-0.050 by idx 100
  - Step increase at idx ~109 (0.050 -> 0.055)
  - Plateau ~0.056-0.060 from idx 110-214
  - Drop at idx ~214-215: 0.063 -> ~0.053 (drop ~0.01)
  - Recovery to ~0.055-0.061 from idx 215-277, final point drop to 0.050

- **Rct (bottom, orange):**
  - Starts ~0.068-0.076 (idx 0-40), highly variable
  - Relatively flat ~0.068-0.074 up to idx ~105
  - Increase after idx ~109: rises to ~0.075-0.083
  - Continued increase to ~0.083-0.089 by idx 212
  - Drop at idx ~213-214: 0.089 -> ~0.075 (drop ~0.014)
  - Recovery to ~0.075-0.089 from idx 214-277

## Observation (No causal claim)
- Both Re and Rct show long-term upward trend with intermediate step changes, not monotonic.
- Re increase: ~45% (0.0436 -> 0.0635), Rct increase: ~38% (0.0649 -> 0.0898) over 278 records.
- Both metrics exhibit sharp drops around impedance_idx ~214 (global_idx ~ around 540-550 region), coinciding temporally with regeneration #149/#166 period (to be verified in next step, not concluded here).
- Rct shows higher cycle-to-cycle variability (zigzag pattern) compared to Re, especially after idx 110.
- No impedance records missing: 278 records continuous across global_idx 40-614, interleaved with charge/discharge per Evidence 02.

## Remaining Uncertainty
- Time field parsing issue (all 1970-01-01) — need to fix pd.to_datetime format or use cycle time string directly; for now use global_idx ordering.
- Whether Re/Rct drops correspond to capacity regeneration events: not analyzed yet (next step is to align Evidence 02 timestamps with this inventory).
- Physical meaning of Re/Rct units and measurement conditions: TBD from NASA documentation.

## BESS Relevance
Impedance growth (Re, Rct) is typical aging indicator. Non-monotonic behavior and drops observed here mean single-point impedance measurement may not reflect true aging trend if taken after rest/regeneration periods. Need to log measurement history, not just last value.

## Files
- evidence/B0005_Re_Rct_Inventory_278_records.png
- evidence/B0005_impedance_inventory.csv (impedance_idx, global_idx, time, Re, Rct)
