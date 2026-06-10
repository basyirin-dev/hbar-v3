# Failure Manifest

Experiments and code paths that did not produce valid scientific results,
preserved for reproducibility and to prevent repeated dead ends.

| Artifact | Failure Mode | Root Cause | Date |
|----------|-------------|------------|------|
| `experiments/kaggle-pilot-optimised.ipynb` | Systematic OOD accuracy drop (−7pp vs manuscript) | `batch_first=True` missing from `nn.Transformer` in Cell 2; model received `(B,S,d)` but expected `(S,B,d)` | 2026-06-10 |
| `scripts/benchmark_pilot.py` | Cannot execute — Kaggle P100 (sm_60) incompatible with PyTorch ≥2.10; hardcoded comparison table is manual recording, not computed result | PyTorch ≥2.10 dropped SM 6.x GPU support; script was written for earlier PyTorch version | 2026-06-10 |
| `archive/new_results_b64.tar.gz` | Multiplicative OOD = 87.4% vs manuscript 94.08% (systematic drift) | Same `batch_first` bug as kaggle-pilot-optimised notebook | 2026-06-10 |
| `archive/results_smoke.tar.gz` | Underpowered (B=8, n=1 per condition) — insufficient for statistical inference | Exploratory scaffolding, not designed for valid hypothesis testing | 2026-06-10 |

## Key Takeaway

The canonical experiment is `experiments/h-bar-experiment.ipynb`, which reproduces
all manuscript values exactly (verified 15/15 PASS, see `paper/manuscript.tex` §10).
All failed experiments share a common pattern: they were optimisation attempts that
inadvertently changed model configuration while trying to improve throughput.
