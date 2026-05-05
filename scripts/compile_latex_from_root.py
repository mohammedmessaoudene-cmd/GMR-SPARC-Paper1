from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
targets = [
    "APJ_GMR_PAPER1_MANUSCRIPT_V55_REFEREE.tex",
    "APJ_GMR_PAPER1_MANUSCRIPT_V55_CLEAN_PREVIEW.tex",
    "APJ_GMR_PAPER1_SUPPLEMENT_V55_REFEREE.tex",
    "APJ_GMR_PAPER1_SUPPLEMENT_V55_CLEAN_PREVIEW.tex",
]
for target in targets:
    subprocess.run(["pdflatex", "-interaction=nonstopmode", target], cwd=ROOT, check=True)
print("LaTeX compile pass completed")
