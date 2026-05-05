# Reproduce

Run from the package root:

```powershell
python scripts/check_repository_integrity.py
python scripts/recompute_metrics.py
python scripts/check_repository_integrity.py
```

LaTeX PDFs can be regenerated with `python scripts/compile_latex_from_root.py` when a local LaTeX distribution with AASTeX support is available.
