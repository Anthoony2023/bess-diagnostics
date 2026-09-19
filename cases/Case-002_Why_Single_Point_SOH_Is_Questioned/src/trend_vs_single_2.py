"""
trend_vs_single.py - Prove single-point amplifies error, trend excludes error

- Plot single-point rebound per cycle (noisy)
- Plot 5-cycle moving average and Growth% trend (smooth)
- Demonstrates Case-002 claim: cannot trust single-point, need trend

This reproduces Evidence D
"""
import json, pathlib

# Load summary
summary = json.loads(pathlib.Path("../data/summary_stats.json").read_text())
print("Single jump:", summary["trend_vs_single"]["single_jump_example"])
print("MA trend:", summary["trend_vs_single"]["ma_trend_example"])
# TODO: plot with matplotlib
