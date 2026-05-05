from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "tables" / "canonical_per_galaxy_metrics.csv")

def eq_rms(series):
    x = np.asarray(series, dtype=float)
    return float(np.sqrt(np.mean(x * x)))

models = {
    "GMR": "rmse_c4_4_kms",
    "Baryons": "rmse_baryon_kms",
    "MOND": "rmse_mond_kms",
    "NFW": "rmse_nfw_kms",
    "ISO": "rmse_iso_kms",
    "Burkert": "rmse_burkert_kms",
}

rows = []
for sample, sdf in [("full_175", df), ("heldout_151", df[df["subset"].eq("external_151")])]:
    for model, col in models.items():
        weights = np.asarray(sdf["n_points"], dtype=float)
        vals = np.asarray(sdf[col], dtype=float)
        nobs = float(np.sqrt(np.sum(weights * vals * vals) / np.sum(weights)))
        rows.append({
            "sample": sample,
            "model": model,
            "equal_weight_rmse": round(eq_rms(sdf[col]), 6),
            "nobs_weighted_rmse": round(nobs, 6),
        })

extra = pd.read_csv(ROOT / "tables" / "recovered_model_metric_comparison.csv")
out_dir = ROOT / "outputs"
out_dir.mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv(out_dir / "recomputed_metrics.csv", index=False, lineterminator="\n")
extra.to_csv(out_dir / "recovered_baseline_metrics.csv", index=False, lineterminator="\n")
print(pd.DataFrame(rows).to_string(index=False))
print("Wrote outputs/recomputed_metrics.csv")
print("Wrote outputs/recovered_baseline_metrics.csv")
