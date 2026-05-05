from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
metrics = ROOT / "tables" / "local_Spsi_variant_metrics.csv"
radial = ROOT / "tables" / "local_Spsi_variant_radial_predictions.csv"
if not metrics.exists():
    raise SystemExit(f"Missing recovered diagnostic table: {metrics}")

print("EXECUTED_RECOVERED_INPUTS")
print(pd.read_csv(metrics).to_csv(index=False))
if radial.exists():
    print(f"radial_predictions={radial}")
