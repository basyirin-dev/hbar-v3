# Σ-Model V3.0+: Schema Coherence Framework for AI Agents

**Paper:** The Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20714248.svg)](https://doi.org/10.5281/zenodo.20714248)

**Status:** Preprint (preparing for peer review) | **Version:** 3.0+ (Full Reconstruction)

---

## Quick Start

### One-Command Docker Setup

```bash
docker build -t sigma-model . && docker run --rm -it sigma-model python scripts/mre_sigma.py
```

### Minimal Reproducible Example

```bash
pip install -e .
python scripts/mre_sigma.py
```

Expected output: `✅ ALL CHECKS PASSED` (runtime ~0.5s CPU).

### Run the Test Suite

```bash
PYTHONPATH=code:$PYTHONPATH pytest tests/ -q
```

Expected: **31 passed** in ~2s.

---

## Abstract

The Σ-Model V3.0+ formalises AI agent knowledge development as a coupled dynamical system centered on **schema coherence** $\sigma_A(d,t)$ — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities.

**Core Problem:** Current training pipelines optimise parametric depth $\delta_A(d,t)$ without formally targeting schema coherence, producing agents that pass in-distribution evaluation while failing out-of-distribution recombination tasks.

**Key Contributions:**
- Formal ODE system for schema coherence dynamics (Eqs. 15–28)
- Five-phase training arc with measurable transition conditions (Prop. 3.2–3.4)
- Nine falsifiable predictions distinguishable from depth-only accounts (§9)
- Executable benchmark families for all cognitive faculties (§10)

---

## Reproducing Results

### Hardware Requirements

- **Minimum:** 16GB RAM, 4 CPU cores
- **Recommended:** 32GB RAM, 8 CPU cores, GPU (NVIDIA RTX 3080+ or equivalent)
- **Benchmark execution:** ~2–4 hours on recommended hardware

See [HARDWARE.md](HARDWARE.md) for detailed specifications and VRAM audit.

### Setup

```bash
# Create virtual environment (Python ≥3.12)
python -m venv venv && source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Validation Experiments

```bash
# ODE validation experiment (canonical notebook)
cd experiments
jupyter nbconvert --to notebook --execute h-bar-experiment.ipynb

# Cognitive evaluation benchmark suite
jupyter nbconvert --to notebook --execute h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb
```

### Smoke Test

```bash
PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py
```

---

## Repository Structure

| Path | Contents |
|------|----------|
| `paper/manuscript.tex` | Main manuscript (tmlr, 48 pages) |
| `code/sigma/` | Python package (ODE, models, config, benchmarks) |
| `experiments/` | Jupyter notebooks and YAML configs |
| `scripts/` | Smoke test, MRE, reproducibility scripts |
| `hackathon/` | Track definitions and dataset archives |
| `docs/` | Claims registry, issue register |
| `tests/` | Pytest test suite (31 tests) |

---

## Citation

```bibtex
@misc{basyirin-amsyar2026sigma,
  title={The {$\Sigma$}-Model: Schema-Coherence Suppression as the Origin of
         Compositional Generalisation Failure},
  author={{Basyirin Amsyar Basri}},
  howpublished={Preprint},
  doi={10.5281/zenodo.20714248},
  year={2026}
}
```

## License

MIT
