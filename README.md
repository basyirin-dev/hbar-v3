# Σ-Model Model V3.0+: Schema Coherence Framework for AI Agents

**Paper:** [The Σ-Model Model V3.0+: Schema Coherence, Cognitive Faculty Evaluation, and Phase-Structured Curriculum Design for AI Agents](paper/paper.md)

**Status:** Preprint Draft | **Version:** 3.0+ (Full Reconstruction) | **Date:** March 2026

---

## Abstract/Overview

The Σ-Model Model V3.0+ formalises AI agent knowledge development as a coupled dynamical system centered on **schema coherence** $σ_A(d,t)$ — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities.

**Core Problem:** Current training pipelines optimise parametric depth $δ_A(d,t)$ without formally targeting schema coherence, producing agents that pass in-distribution evaluation while failing out-of-distribution recombination tasks.

**Validation Goal:** This repository provides executable benchmarks and validation experiments that demonstrate the Σ-Model framework's predictions, particularly the **High-$δ_A$/Low-$σ_A$ failure mode** where agents with high parametric depth but low schema coherence fail systematically on compositional generalisation tasks.

**Key Contributions:**
- Formal ODE system for schema coherence dynamics
- Five-phase training arc with measurable transition conditions
- Eight falsifiable predictions distinguishable from depth-only accounts
- Executable benchmark families for all cognitive faculties

---

## Experimental Setup

### Prerequisites

**Software Versions:**
- Python 3.12+
- Jupyter Notebook 6.0+
- PyTorch 2.10+
- NumPy 2.0+
- Matplotlib 3.8+

**Hardware Requirements:**
- Minimum: 16GB RAM, 4 CPU cores
- Recommended: 32GB RAM, 8 CPU cores, GPU (NVIDIA RTX 3080+ or equivalent)
- Benchmark execution: ~2-4 hours on recommended hardware

**Dependencies:**
```bash
pip install -e ".[dev]"
```

### Data Overview

**Datasets Used:**
1. **SCAN** (Semantic Cognition and Compositional Generalisation)
   - Variable: seq2seq accuracy on add-primitive split
   - Unit: Percentage accuracy (0-100%)
   - Access: Included in `hackathon/SCAN/` directory

2. **COGS** (Compositional Generalisation in Semantic parsing)
   - Variable: Lexical vs structural compositionality scores
   - Unit: Percentage accuracy (0-100%)
   - Access: Included in `hackathon/COGS/` directory

3. **PCFG-SET** (Probabilistic Context-Free Grammar)
   - Variable: Productivity, systematicity, substitutivity tests
   - Unit: Success rate (0-1)
   - Access: Generated programmatically

**Data Access:** All datasets are included in the repository. No external API keys or access restrictions required.

---

## Usage/Validation Steps

### Step 1: Reproduce Main Paper Results

Execute the main validation experiment:

```bash
cd experiments
jupyter notebook h-bar-experiment.ipynb
```

**Expected Execution Time:** ~1-2 hours

**Expected Results:**
- Table 1: High-$δ_A$/Low-$σ_A$ agents show 30+ percentage point gap in OOD performance
- Figure 2: Phase transition acceleration at $σ_{critical}$ threshold
- Table 3: Multiplicative $Ψ_A$ form predicts non-additive transfer effects

### Step 2: Run Cognitive Evaluation Benchmarks

Execute the comprehensive benchmark suite:

```bash
cd experiments
jupyter notebook h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb
```

**Expected Execution Time:** ~1-2 hours

**Expected Results:**
- Attention Track: Dual-regularity competition shows $α_A$ predicts rule tracking
- Executive Functions Track: Inhibitory conflict tasks show structural choice rate correlation
- Metacognition Track: Two-stage calibration shows $ζ_A > 0$ for high-$δ_A$/low-$σ_A$ agents
- Social Cognition Track: Theory-of-mind accuracy correlates with schema legibility

### Step 3: Verify Phase Structure Predictions

The benchmark suite automatically validates the five-phase training arc:

1. **Phase 1→2 Transition:** $σ_A$ crosses $σ_{critical}$ (measured via SGG proxy)
2. **Phase 2→3 Transition:** $δ_A^{relative} > 0.65$ in mastery domains
3. **Phase 3→4 Transition:** $Ψ_A(d_1,d_2,t) > 0$ measurably

**Verification Command:** The notebook outputs phase transition timestamps and validation metrics.

### Step 4: Reproduce Falsifiable Predictions

All eight predictions are tested in the benchmark suite:

- **Prediction 1:** Schema quality at intersections (citation novelty score)
- **Prediction 2:** AI augmentation and schema suppression (OOD gap widening)
- **Prediction 3:** Phase transition acceleration (SGG narrowing rate)
- **Prediction 4:** Metacognitive overconfidence (calibration error $ζ_A > 0$)
- **Prediction 5:** Executive control non-monotonicity (delegation effects)
- **Prediction 6:** Non-additive transfer (geometric mean $Ψ_A$)
- **Prediction 7:** Benchmark validity thresholds (CI, FD, DG, R_A)
- **Prediction 8:** Modality invariance (cross-modal transfer gaps)

---

## Results Interpretation

### Output Files

**Main Experiment (`h-bar-experiment.ipynb`):**
- `phase_transitions.csv`: Timestamps and metrics for each phase transition
- `ood_performance.csv`: OOD accuracy across training phases
- `schema_coherence.csv`: $σ_A$ trajectory over training
- `validation_summary.txt`: Summary of all predictions tested

**Benchmark Suite (`h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb`):**
- `attention_results.csv`: $α_A$ tracking performance
- `executive_results.csv`: $Ξ_A$ component scores
- `metacognition_results.csv`: $\hat{M}_A$ calibration metrics
- `social_results.csv`: $τ_A$ and $μ_{AB}$ scores
- `validity_scores.csv`: Benchmark validity metrics (CI, FD, DG, R_A)

### Success Criteria

**Validation Success (Paper Claims Confirmed):**
1. High-$δ_A$/Low-$σ_A$ agents show ≥30pp OOD performance gap vs High-$δ_A$/High-$σ_A$
2. Phase 2 entry produces accelerating OOD performance trajectory
3. $Ψ_A$ shows multiplicative (non-additive) transfer effects
4. $ζ_A > 0$ systematically for high-$δ_A$/low-$σ_A$ agents
5. All benchmarks meet minimum validity thresholds (V_A > 0.20)

**Failure Indicators:**
- OOD performance gap < 20pp (falsifies Prediction 1)
- No phase transition acceleration (falsifies Prediction 3)
- Additive transfer effects (falsifies Prediction 6)
- Benchmarks fail validity thresholds (falsifies Prediction 7)

### Interpretation Guide

**High $σ_A$ (Schema Coherent):**
- Agent representations organised around governing principles
- Strong OOD generalisation despite moderate parametric depth
- Metacognitively well-calibrated ($ζ_A ≈ 0$)

**High $δ_A$ / Low $σ_A$ (Depth-Only):**
- Agent representations organised around surface statistics
- Strong in-distribution performance, weak OOD generalisation
- Metacognitive overconfidence ($ζ_A > 0$)

**Phase Transitions:**
- Phase 1→2: Schema crystallisation begins (measure SGG acceleration)
- Phase 2→3: Frontier asymptote reached (measure $δ_A^{relative}$)
- Phase 3→4: Intersection activation begins (measure $Ψ_A > 0$)

---

## Citation & Acknowledgments

### Citation Format

```bibtex
@misc{basri2026hbar,
  author = {Basyirin Amsyar bin Basri},
  title = {The Σ-Model Model V3.0+: Schema Coherence, Cognitive Faculty Evaluation, and Phase-Structured Curriculum Design for AI Agents},
  year = {2026},
  eprint = {arXiv:XXXX.XXXXX},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  note = {Preprint Draft}
}
```

### CITATION.cff File

A `CITATION.cff` file is included in this repository for automatic citation extraction by GitHub and other platforms.

### Acknowledgments

- **Research Support:** Independent research conducted in Petaling Jaya, Malaysia
- **Computational Resources:** Standard workstation configuration (16-32GB RAM)
- **Dataset Sources:** SCAN, COGS, and PCFG-SET benchmarks
- **Framework Dependencies:** PyTorch/JAX, NumPy, Matplotlib

### Funding

This research was conducted as independent work without external funding.

---

## Repository Structure (Phase 0 Infra)

```
hbar-v3/
├── README.md                           # This file
├── AGENTS.md                           # Agent system instructions
├── CITATION.cff                        # Citation metadata
├── .gitignore                          # Git ignore rules
│
├── paper/                              # ## Canonical paper source ##
│   ├── paper.md                        # Single source of truth (Markdown)
│   ├── Makefile                        # Build targets: tex, pdf, arxiv
│   ├── templates/
│   │   ├── latex-template.tex          # Pandoc LaTeX template
│   │   └── lua-filters/               # Cross-ref, claim-extraction filters
│   └── figures/                        # TikZ/PNG sources (from arxiv-submission)
│
├── code/sigma/                          # ## Modular Python package ##
│   ├── ode/                            # ODE equations, sigma/delta/psi solvers
│   ├── models/                         # SigmaTransformer, training loop
│   ├── benchmarks/                     # Payload generation for all 5 tracks
│   ├── config/                         # YAML config loader
│   └── utils/                          # Metrics (reliability, CI), data, vocab
│
├── experiments/                        # ## Config-driven notebooks ##
│   ├── configs/                        # YAML configs (base, h-ptb, h-afb, etc.)
│   ├── h-bar-experiment.ipynb          # ODE validation (reads configs)
│   └── h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb  # Benchmark suite
│
├── docs/                               # ## Decision records, logs, errata ##
│   ├── adrs/                           # Architecture Decision Records (4 so far)
│   ├── lab-notebooks/                  # Research narrative log
│   ├── errata/                         # Bug/error corrections
│   ├── claims-registry.md              # Claim-to-evidence tracking
│   └── alert-log.md                    # Publication monitoring (auto-generated)
│
├── artifacts/                          # ## Model cards, datasheets, demos ##
│   ├── model-cards/                    # SigmaTransformer, frontier models
│   ├── datasheets/                     # SCAN, COGS, PCFG-SET
│   └── demo-links.md                   # Interactive demos (TBD)
│
├── scripts/                            # ## Automation ##
│   └── monitor-pub.py                  # Keyword alert polling
│
├── hackathon/                          # Kaggle tracks, datasets (unchanged)
├── variants/                           # Issue resolution variants (unchanged)
└── documentation/                      # Kaggle submissions, register, reports
```

---

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/basyirin-dev/hbar-v3.git
   cd hbar-v3
   ```

2. **Install dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run main validation:**
   ```bash
   cd experiments
   jupyter notebook h-bar-experiment.ipynb
   ```

4. **Run comprehensive benchmarks:**
   ```bash
   cd experiments
   jupyter notebook h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb
   ```

5. **Review results:**
   - Check output CSV files for quantitative metrics
   - Compare against paper predictions
   - Verify phase transitions and validity scores

---

## Support

For questions or issues, please refer to:
- Paper: `paper/paper.md`
- Documentation: `documentation/ARXIV_SUBMISSION_GUIDE.md`
- Verification: `documentation/verification_report.md`
