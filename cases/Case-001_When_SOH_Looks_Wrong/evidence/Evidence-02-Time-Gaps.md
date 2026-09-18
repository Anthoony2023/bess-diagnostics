
# Evidence 02 — Time Gap Before Regeneration Events

## Purpose
Determine whether capacity regeneration events are preceded by extended rest / non-discharge periods. No causal conclusion yet.

## Source
- B0005.mat cycle[].time (YYYY-MM-DD HH:MM:SS)
- Discharge Index mapped to original cycle record Index
- Capacity unit TBD, as per Evidence 01

## Regeneration Events Analyzed
5 main events: Discharge Index 18, 30, 89, 149, 166

### Summary Table

| Regen # (Discharge idx) | Original cycle record | Regen Timestamp | Capacity (unit TBD) | Δ Prev discharge → Regen | Δ Prev impedance → Regen | Δ Regen → Next discharge | Prev type before regen |
|---|---|---|---|---|---|---|---|
| 18 (18) | 38 | 2008-04-05 22:46:35 | 1.8565 | 4:07:10 | N/A (no impedance before) | 12 days 22:23:44 | Charge |
| 30 (30) | 85 | 2008-04-22 15:33:49 | 1.6058 | 1 day 13:18:47 | 1 day 12:06:51 | 4:52:29 | Charge |
| 89 (89) | 312 | 2008-05-09 12:25:07 | 1.6058 | 1 day 9:31:18 | 0:31:57 | 8:03:02 | Impedance |
| 149 (149) | 544 | 2008-05-23 12:13:16 | 1.5523 | 15:13:26 | 0:32:06 | 8:01:13 | Impedance |
| 166 (166) | 611 | 2008-05-27 15:52:41 | 1.4237 | 19:31:37 | 15:24:46 | 4:53:01 | Impedance |

### Detailed Sequences
See evidence image: B0005_Regeneration_Events_Full_Sequence_and_Time_Gaps.png

- **#18**: Pre = Charge (19:46:36 → 22:46:35 = 3:00:00), but previous discharge was 4:07:10 before. After regen, 12 days gap to next discharge (41: 2008-04-18 21:10:19) — suggests long rest after regen as well.
- **#30**: Clear impedance → charge → charge → regen. Prev impedance 82 at 2008-04-21 03:26:58 → regen 85 gap 1d 12:06:51. Prev discharge gap 1d 13:18:47.
- **#89**: Largest jump +0.0913 (1.5145 → 1.6058). Sequence: discharge pre 309 → impedance 310 (0:52:20) → impedance 311 (1d 8:07:01) → regen 312 (0:31:57). Prev impedance gap only 31min, but prev discharge gap 1d 9:31:18.
- **#149**: Impedance 541 → charge 542 (0:32:05) → impedance 543 (13:20:26) → regen 544 (0:32:06). Prev impedance gap 32 min, prev discharge gap 15:13:26.
- **#166**: Impedance 608 → charge 609 (0:32:11) → impedance 610 (2:46:22) → regen 611 (15:24:46). This one has longest impedance→regen gap 15h 24m.

## Observation (No causal claim)
- All 5 regen events are preceded by gaps significantly longer than typical discharge→charge→discharge cadence (~2-4 hours in normal cycles).
- Prev discharge → Regen: 4h to 19.5h, plus 2 cases >1 day.
- Prev impedance → Regen: ranges from 0:31:57 to 15:24:46, with 3 cases ~30 min but after longer impedance-charge-impedance clusters.
- After regen, next discharge gaps are also extended: 4h to 12 days.
- Pattern: regeneration discharge appears after a cluster containing impedance measurements and/or extended idle time, not immediately after a standard discharge-charge cycle.

## Remaining Uncertainty
- Why longer gaps exist: test protocol pause, scheduled impedance day, or ambient recovery — TBD, not concluded.
- Correlation with Re/Rct not analyzed yet (Evidence 03 planned).
- Whether gap duration correlates with jump magnitude: insufficient sample, not concluded.

## BESS Relevance
If field SOH is sampled after irregular rest / diagnostic intervals, capacity may appear to increase. Time gap must be logged alongside SOH estimate to avoid false "recovery" interpretation.

## Files
- evidence/B0005_Regeneration_Events_Full_Sequence_and_Time_Gaps.png (source image)
- evidence/time_gaps.csv (optional export of this table)
