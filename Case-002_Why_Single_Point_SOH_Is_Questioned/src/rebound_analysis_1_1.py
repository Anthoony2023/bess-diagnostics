"""
rebound_analysis.py - Extract rebound vs rest time and Growth%

Usage:
python rebound_analysis.py --cells B0005 B0006 B0007 B0018

Logic:
- For each discharge cycle, detect end-of-discharge voltage V_end
- Measure V_after_rest at 5min, 10min, 20min, 30min, 60min
- Rebound = V_after_rest - V_end
- Growth% = (Rebound_current - Rebound_new) / Rebound_new * 100%
- Self-baseline: Rebound_new = average of first 5 cycles
- Output: CSV and figures for evidence

This reproduces Evidence A, B, C
"""
import argparse

def extract_rebound(cell_data, rest_minutes=[5,10,20,30,60]):
    # placeholder - implement with actual NASA .mat parsing
    # Use scipy.io.loadmat, find discharge cycles, extract voltage
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cells", nargs="+", default=["B0005","B0006","B0007","B0018"])
    args = parser.parse_args()
    print(f"Analyzing {args.cells} for rebound growth and batch variation...")
    # TODO: implement
