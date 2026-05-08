from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
metrics = pd.read_csv(ROOT / "tables" / "recovered_model_metric_comparison.csv")

wanted = [
    ("Pure sqrt(g_N) baseline", "full_175", 40.241),
    ("GMR recovered", "full_175", 40.554),
    ("Pure sqrt(g_N) baseline", "non_calibration_151", 41.329),
    ("GMR recovered", "non_calibration_151", 41.870),
]

rows = []
for model, subset, expected_round3 in wanted:
    row = metrics[(metrics["model"].eq(model)) & (metrics["subset"].eq(subset))].iloc[0]
    value = float(row["equal_weight_rmse_kms"])
    rows.append({
        "model": model,
        "subset": subset,
        "equal_weight_rmse_kms": value,
        "rounded_for_note": round(value, 3),
        "expected_in_note": expected_round3,
        "pass": abs(round(value, 3) - expected_round3) < 1e-9,
    })

out = ROOT / "outputs"
out.mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv(out / "rnaas_note_metrics_v46.csv", index=False, lineterminator="\n")
print(pd.DataFrame(rows).to_string(index=False))
if not all(r["pass"] for r in rows):
    raise SystemExit("Metric mismatch")
