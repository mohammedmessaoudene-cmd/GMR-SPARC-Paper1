from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "REPRODUCE.md",
    "METHOD_FILES.md",
    "MANIFEST.csv",
    "CITATION.cff",
    "LICENSE",
    "DATA_LICENSE.md",
    "requirements.txt",
    "APJ_GMR_PAPER1_MANUSCRIPT_V55_REFEREE.tex",
    "APJ_GMR_PAPER1_SUPPLEMENT_V55_REFEREE.tex",
    "source_csv/full_radial_invariants.csv",
    "source_csv/all_galaxy_radial_predictions.csv",
    "tables/canonical_per_galaxy_metrics.csv",
    "tables/calibration_24_subset.csv",
    "tables/nobs_weighted_rmse.csv",
    "tables/leverage_by_galaxy.csv",
    "tables/rar_binning_spec.csv",
    "tables/pure_sqrt_baseline_metrics.csv",
    "tables/local_Spsi_variant_metrics.csv",
    "tables/sin_alpha_Srad_by_galaxy.csv",
    "scripts/recompute_metrics.py",
    "scripts/check_repository_integrity.py",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("MISSING")
    print("\n".join(missing))
    sys.exit(2)

bad_tokens = [
    "Table " + "??",
    "V" + "49",
    "V" + "50",
    "D:" + "\\IGV_2",
    "local " + "harness",
    "curated but " + "not sanitized",
    "primary descriptive " + "endpoint",
    "not ready for journal " + "upload",
    "missing-input " + "gate",
    "author-task " + "execution",
    "v" + "49-micro-patch-after-v38",
    "MOND is below " + "GMR",
    "GMR outperforms " + "sqrt",
    "superior to " + "square-root",
    "beats " + "square-root",
    "demonstrates GMR " + "superiority",
    "dSph " + "solved",
    "EFE " + "solved",
    "dark sector " + "closure",

]
public_suffixes = {".tex", ".md", ".csv", ".json", ".py", ".cff"}
hits = []
for path in ROOT.rglob("*"):
    if path.name in {
        "MANIFEST.csv",
        "V55_PUBLIC_PROSE_GREP_AFTER.csv",
        "V55_FALSE_POSITIVE_GREP_REPORT.csv",
        "V55_FINAL_QA_REPORT.md",
        "V55_VISUAL_QA_REPORT.md",
    }:
        continue
    if not path.is_file():
        continue
    if path.suffix.lower() not in public_suffixes:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for token in bad_tokens:
        if token in text:
            hits.append(f"{path.relative_to(ROOT)}:{token}")
if hits:
    print("STALE_TOKENS")
    print("\n".join(hits[:100]))
    sys.exit(3)
print("Repository integrity check PASS")
