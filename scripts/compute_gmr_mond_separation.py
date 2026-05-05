from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
factor = ROOT / "tables" / "sin_alpha_Srad_by_galaxy.csv"
comparison = ROOT / "tables" / "recovered_model_metric_comparison.csv"
for path in [factor, comparison]:
    if not path.exists():
        raise SystemExit(f"Missing recovered diagnostic table: {path}")

factor_df = pd.read_csv(factor)
comparison_df = pd.read_csv(comparison)
print("EXECUTED_RECOVERED_INPUTS")
print("sin_alpha_Srad_by_galaxy_head")
print(factor_df.head(10).to_csv(index=False))
print("model_metric_comparison")
print(comparison_df.to_csv(index=False))
