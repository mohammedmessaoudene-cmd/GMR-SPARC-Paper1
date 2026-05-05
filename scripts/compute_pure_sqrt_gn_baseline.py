from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
metrics = ROOT / "tables" / "pure_sqrt_baseline_metrics.csv"
if not metrics.exists():
    raise SystemExit(f"Missing recovered diagnostic table: {metrics}")

df = pd.read_csv(metrics)
print("EXECUTED_RECOVERED_INPUTS")
print(df.to_csv(index=False))
