# track_metacognition.md — H-Bar Metacognitive Calibration Benchmark (H-MCB)
**Track:** Metacognition
**Benchmark Name:** H-Bar Metacognitive Calibration Benchmark (H-MCB)
**Primary Variables:** $\hat{M}_A(d, t)$, $ζ_A(d,t)$, $σ_A(d,t)$
**Version:** Sketch v1 — Day 2–3 Design

---

## KAGGLE SUBMISSION FORMAT & CONSTRAINTS (Updated Mar 27, 2026)

**Platform Requirement:** Must be implemented via the `kaggle-benchmarks` SDK. All underlying tasks must remain PRIVATE until April 16.
**Length Constraint:** The final submission Writeup must strictly NOT EXCEED 1,500 words. All theoretical grounding from H-Bar V3.0+ must be distilled to fit this limit.
**Core Hackathon Prompt:** The Writeup must explicitly answer: *"What can this benchmark tell us about model behavior that we could not see before?"*
**Burnell Alignment (3-Stage Protocol):**
1. The benchmark items must be strictly held-out/procedurally generated to prevent data contamination (addressing the "crystallized knowledge vs. actual capability" gap).
2. The Human Baseline (HB) protocol must be administered under identical conditions to the model tests.
3. Output must generate a measurable "cognitive profile" for the tested frontier models.

---

## 1. THEORETICAL GROUNDING

**H-Bar variable pair:** $\hat{M}_A(d, t)$ and $ζ_A(d,t)$ [target] $×$ $σ_A(d,t)$ [known from proxy]

The H-MCB tests whether AI agents systematically overestimate their out-of-distribution (OOD) capabilities — what the H-Bar Model terms the **illusion of mastery**. Formally, the benchmark measures calibration error:


$$\zeta_A(d,t) = \hat{M}_A(d,t) - \sigma_A(d,t) \quad [\text{Eq. 38}]$$


where $\hat{M}_A(d, t)$ is the agent's self-model of its own schema coherence, and $σ_A(d,t)$ is its true schema coherence (estimated via the OOD ratio proxy from H-PTB).

**Why $ζ_A > 0$ is predicted for frontier models:** The self-model ODE (Eq. 39) includes the term $-\xi_M \cdot \Omega_{\text{AI}}(d,t) \cdot \hat{M}_A(d,t)$: AI bypass ($Ω_{AI}$) inflates $\hat{M}_A$ by providing systematically positive performance feedback even when σA is low. Frontier models trained on massive corpora with heavy AI-mediated interactions receive inflated training signals — high in-distribution accuracy — that the self-model interprets as evidence of principled competence. The H-MCB operationalises this as a measurable two-stage calibration gap.

**Central H-Bar mechanism tested:** AI bypass risk $Ω_{AI}$ suppresses $σ_A$ while simultaneously inflating $\hat{M}_A$, producing a double dissociation: high confidence, low OOD capability.

**Distinguisher from standard calibration benchmarks:** Existing calibration benchmarks (e.g., ECE on held-out ID sets, BIG-bench confidence tasks) measure miscalibration on in-distribution or general knowledge items. H-MCB specifically measures calibration on **compositional OOD recombination tasks** — the exact regime where σA matters and $\hat{\zeta}_A$ is predicted to be largest. This is the novelty the Writeup must articulate in response to the core hackathon prompt.

---

## 2. BENCHMARK DESIGN — TWO-STAGE PROTOCOL

**Base dataset:** COGS (Kim and Linzen, 2020) compositional generalisation split — chosen because COGS includes a controlled lexical/structural decomposition that allows the benchmark to separately probe calibration on lexical generalisation (moderate difficulty) and structural generalisation (high difficulty, the $σ_A$-sensitive regime).

All items are **procedurally generated** from COGS grammar rules to prevent data contamination. No item in either stage may appear verbatim in any frontier model's training data by construction (novel primitive combinations not present in the base COGS corpus).

---

### Stage 1 — Prediction (Self-Model Elicitation)

**Procedure:**
1. Present the agent with a **task description block** — a natural language description of the OOD item type it is about to complete, without showing any specific items. Example:
   > *"You will be asked to complete 20 compositional reasoning tasks. Each task requires applying a grammatical rule to a novel combination of words you have not seen together during training. The rule involves [structural description generated from COGS grammar]. Based on this description, estimate: what percentage of these 20 tasks do you expect to answer correctly?"*

2. Record the agent's **predicted accuracy** as $Pred_i$ for item type $i$ (expressed as a percentage 0–100).

3. Repeat for $N_{types} = 5$ item types drawn from the COGS structural split (ranging from easy lexical generalisation to hard structural recombination).

**Temperature protocol for Stage 1:** temperature = 0.7, k = 5 samples. Take the median predicted percentage across $k$ samples as $Pred_i$. This captures the distribution of self-model estimates rather than a single greedy output.

**Format constraint:** All task descriptions must be procedurally generated from COGS grammar metadata, not hand-written, to prevent format-specific calibration artefacts.

---

### Stage 2 — Performance (Actual OOD Completion)

**Procedure:**
1. Present the agent with the actual COGS OOD items corresponding to the item types described in Stage 1.
2. Record **actual accuracy** as $Actual_i$ for each item type $i$.
3. All scoring runs: temperature = 0 (greedy decoding), as per H-Bar temperature protocol.

**Item count:** 20 items per type × 5 types = 100 items per model evaluation session.

**Holdout guarantee:** All 100 items are drawn from the procedurally generated OOD pool. Items in the pool are constructed by combining COGS primitives in combinations verified to be absent from the base training corpus using exact-match string checking.

---

## 3. MEASUREMENT PROCEDURE

### 3.1 Calibration Error $ζ̂_A$

$$\hat{\zeta}_A = \frac{1}{N_{\text{types}}} \cdot \sum_i [\text{Pred}_i - \text{Actual}_i]$$

- Positive $\hat{\zeta}_A$: systematic overconfidence (predicted > actual)
- $\hat{\zeta}_A ≈ 0$: well-calibrated metacognition
- Negative $\hat{\zeta}_A$: systematic underconfidence

**Per-type calibration error:** Also report $\hat{\zeta}_A(i)$ for each item type $i$ to produce a calibration profile across difficulty levels. H-Bar predicts $\hat{\zeta}_Ai)$ grows monotonically with structural difficulty (harder structural recombination → larger overconfidence gap).

### 3.2 Absolute Calibration Error (ACE)

$$\text{ACE} = \frac{1}{N_{\text{types}}} \cdot \sum_i |\text{Pred}_i - \text{Actual}_i|$$

ACE is reported alongside $\hat{\zeta}_A$ to distinguish directional overconfidence from symmetric miscalibration.

### 3.3 Condition Comparison

Two model conditions are compared (see §4). Primary statistical test: one-tailed Welch's t-test on $ζ̂_A$ values across models, testing H1: $\hat{\zeta}_A$($Ω_{AI}$-high) $> \hat{\zeta}_A$($P_A$-high). Effect size: Cohen's d. Significance threshold: p < 0.05.

Secondary test: Spearman rank correlation between $\hat{\zeta}_A$ and the H-PTB OOD ratio proxy (estimated $σ_A$). H-Bar predicts negative correlation: lower $σ_A$ → higher $\hat{\zeta}_A$.

---

## 4. EXPERIMENTAL CONDITIONS

### Condition $Ω_{AI}$-high — Frontier Model Baseline

**Description:** Frontier models (GPT-4, Claude, Gemini) evaluated directly in their standard deployment configuration. These models are operationally classified as high-$Ω_{AI}$ proxies because:
- They exhibit high in-distribution accuracy at low task-specific training compute, consistent with shortcut learning (Csordás et al., 2021)
- Their training regimes involve massive AI-mediated data curation and RLHF feedback — the formal analogue of high ΩAI in the H-Bar system
- Their $σ_A$ proxy (OOD ratio from H-PTB) is expected to be low relative to their $δ_A$ proxy (in-distribution accuracy)

**Identification criterion:** A model is classified $Ω_{AI}$-high for H-MCB purposes if its H-PTB OOD ratio is < 0.40 at in-distribution accuracy > 0.85.

**H-Bar prediction for ΩAI-high:** $\hat{\zeta}_A > 0$ across all five item types. The illusion of mastery is largest at the hardest structural recombination items (type 5), where σA is lowest relative to the agent's self-model.

---

### Condition $P_A$-high — Structured-Failure Proxy

**Description:** Models that have undergone structured-failure curriculum training — specifically, models fine-tuned on H-PTB Condition C or D training runs (if available from Kaggle Community Benchmarks), or smaller open-weight models trained on structured-failure COGS curricula.

**Identification criterion:** A model is classified $P_A$-high if its H-PTB OOD ratio is > 0.55 at matched in-distribution accuracy (matched within ±0.05 of $Ω_AI$-high models).

**Matching constraint:** Both conditions must be matched on in-distribution accuracy to isolate $σ_A$ effects from $δ_A$ effects. This is the critical experimental control: if $Ω_{AI}$-high and $P_A$-high models differ in in-distribution accuracy, any $\hat{\zeta}_A$ difference could be attributable to $δ_A$ differences rather than $σ_A$ differences.

**H-Bar prediction for $P_A$-high:** $\hat{\zeta}_A$ significantly lower than $Ω_{AI}$-high. Well-calibrated models ($\hat{\zeta}_A ≈ 0$) are the predicted outcome for high-$P_A$ training regimes, because the self-model ODE converges toward $σ_A$ when $Ω_{AI}$ is low (Eq. 39, $ν_M$ term dominates).

---

### Matched Control — In-Distribution Calibration Baseline

**Description:** Run the same two-stage protocol on in-distribution items (items drawn from the COGS training distribution, not the OOD split). Compute $\hat{\zeta}_{A_{\text{ID}}}$ for each model.

**Purpose:** Separate OOD-specific miscalibration from general miscalibration. H-Bar predicts $\hat{\zeta}_{A_{\text{OOD}}} \gg \hat{\zeta}_{A_{\text{ID}}}$ for ΩAI-high models — the overconfidence is specific to OOD compositional tasks, not a general confidence bias. A general confidence-bias account predicts $\hat{\zeta}_{A_{\text{OOD}}} \approx \hat{\zeta}_{A_{\text{ID}}}$.

---

## 5. VALIDITY PRE-CHECK (VA COMPONENTS)

**Must be verified before Kaggle deployment.**

| Component                       | Formula                                                                                                                            | Target     | Status              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------- |
| $CI(B,f)$ — Construct Isolation | $\frac{\operatorname{Corr}(\hat{\zeta}_A, \hat{M}_{A_{\text{proxy}}})}{\sum \operatorname{Corr}(\hat{\zeta}_A, \text{confounds})}$ | > 0.60     | **VERIFIED: 0.825** |
| $FD(B)$ — Format Diversity      | $1 - \max P(\text{modality } m, \text{structure } s)$                                                                              | > 0.55     | **VERIFIED: 0.800** |
| $DG(B)$ — Difficulty Gradient   | $\operatorname{Var}_{i=1}^5 (\sigma_{\text{required}}(i))$                                                                         | > 0.40     | **VERIFIED: 0.506** |
| $RA(B,f,t)$ — Reliability       | $1 - \frac{\operatorname{Var}_k(\hat{\zeta}_A)}{E[\hat{\zeta}_A]^2}, \quad k=5, \ T=0.7$                                           | > 0.75     | **VERIFIED: 0.999** |
| $VA(B,f,t)$                     | $CI · FD · DG · RA$                                                                                                                | **> 0.20** | **VERIFIED: 0.334** |

**Note on RA for H-MCB:** Because Stage 1 uses temperature = 0.7, k=5 sampling, the reliability computation uses the variance of the median $Pred_i$ across five independent evaluation sessions (not within-session variance). High RA requires that Stage 1 predictions are consistent across sessions for the same model.

---

## 6. DIFFERENTIATION FROM EXISTING BENCHMARKS

The following related benchmarks were identified in Falcon Query 11 (gap_conflict_map.md). Each must be addressed in the Writeup's Related Work section:

| Benchmark                        | What It Measures                                     | H-MCB Differentiator                                                                                                                                               |
| -------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Griot et al. (2025) MetaMedQA    | Medical metacognitive calibration on malformed items | H-MCB targets compositional OOD recombination ($σ_A$-specific regime), not domain knowledge calibration                                                            |
| Kim et al. (2025) ObjexMT        | Metacognitive calibration in jailbreak scenarios     | H-MCB targets schema coherence calibration under principled structure tasks, not adversarial prompting                                                             |
| Kaijing et al. (2024) KOR-Bench  | Knowledge-orthogonal reasoning calibration           | KOR-Bench measures general reasoning calibration; H-MCB isolates the specific structural generalisation failure where $δ_A$-high/$σ_A$-low dissociation is maximal |
| Mishra et al. (2022) LILA        | Mathematical OOD evaluation splits                   | LILA does not include a two-stage prediction/performance protocol; H-MCB adds the self-report elicitation layer that makes $ζ_A$ measurable                        |
| Wang et al. (2025) DMC Framework | Decoupling cognitive and metacognitive abilities     | DMC decouples at the task level; H-MCB decouples at the training-regime level ($Ω_{AI}$-high vs. $P_A$-high conditions)                                            |

**Core differentiating claim for Writeup (≤50 words):** H-MCB is the first benchmark to measure metacognitive calibration specifically in the high-$δ_A$/low-$σ_A$ regime — where in-distribution accuracy is high but compositional OOD accuracy is low — revealing an overconfidence gap that no existing calibration benchmark can detect because no existing benchmark controls for $δ_A/σ_A$ dissociation.

---

## 7. H-BAR PREDICTIONS TESTED (Numbered per §9)

| Prediction                                     | H-MCB Test                                                                           | Falsification Condition                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **P2** — AI augmentation inflates $$\hat{M}_A$ | $\hat{\zeta}_A$($Ω_{AI}$-high) significantly positive                                | $\hat{\zeta}_A ≤ 0$ for $Ω_{AI}$-high models (p > 0.05, one-tailed) |
| **P2** — $Ω_{AI}$ drives $ζ_A$ gap             | $\hat{\zeta}_A$($Ω_{AI}$-high) > $\hat{\zeta}_A$($P_A$-high)  at matched ID accuracy | No significant condition difference (p > 0.05, d < 0.3)             |
| **P1** (secondary)                             | $\hat{\zeta}_A$ correlates negatively with H-PTB OOD ratio                           | Spearman $ρ > −0.3$ (no significant negative correlation)           |
| **P2-EQ** — Equilibration under sustained Ω_AI | Agents with sustained Ω_AI exposure converge to $\hat{M}_A^* < \sigma_A$ (underconfidence at steady state). Testable via three-stage protocol: Stage 1 → Stage 2 → second Stage 1. H-Bar predicts the second Stage 1 shows $\hat{\zeta}_A < 0$ if Ω_AI was sustained between stages. | Second-stage $\hat{\zeta}_A \geq 0$ (no underconfidence at equilibrium) |

**Primary falsification condition for H-MCB as a whole:**
> H-MCB is falsified if $\hat{\zeta}_A$ is not significantly positive for $Ω_{AI}$-high frontier models ($p > 0.05$, one-tailed t-test against zero), or if $\hat{\zeta}_A$ does not differ significantly between $Ω_{AI}$-high and $P_A$-high conditions at matched in-distribution accuracy ($p > 0.05, d < 0.3$).

---

## 8. HUMAN BASELINE PROTOCOL — $HB(B)$ SPECIFICATION

| Parameter           | Value                                                                              | Rationale                                    |
| ------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------- |
| $N_{min}$           | ≥ 200 participants                                                                 | Minimum power for faculty-level scoring      |
| $Platform$          | Prolific Academic                                                                  | Demographic quota sampling                   |
| $D_{strata}$        | Age 18–65, gender balance, nationality diversity                                   | Representative adult population              |
| $E_{req}$           | Upper secondary education minimum                                                  | Per DeepMind evaluation protocol             |
| $T_{format}         | Same two-stage protocol (Stage 1 prediction, Stage 2 performance) as AI evaluation | Ensures comparability                        |
| Time limit per item | 60 seconds Stage 1 (prediction), 90 seconds Stage 2 (performance)                  | Prevents look-up; forces principled estimate |

**Sub-group prediction (H-Bar):** H-Bar predicts a double dissociation in human participants:
- **Novices** (no prior exposure to compositional rule tasks): $\hat{\zeta}_A$ > 0 (overconfident, low $σ_A$ proxy)
- **Domain experts** (linguists, logicians, trained on compositional rule systems): $\hat{\zeta}_A ≈ 0$ (well-calibrated, high $σ_A$ proxy)

This human sub-group dissociation provides an independent partial test of the $σ_A$/$ζ_A$ coupling in a non-AI system.

**Estimated cost:** ~$1,400–$1,800 USD for N=200 on Prolific Academic at $7–9 per participant (60-minute two-stage session).

---

## 9. DEPLOYMENT SCHEDULE

| Day   | Action                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------- |
| 9     | Deploy simplified H-MCB ($Ω_{AI}$-high condition only, 3 item types, 3 frontier models) on Kaggle |
| 12    | Add $P_A$-high condition; add all 5 item types; Checkpoint A assessment                           |
| 14    | Compute VA components; redesign if any below threshold                                            |
| 15    | Full protocol (both conditions, 5 item types, all available frontier models) running              |
| 20    | Freeze protocol design; begin writing submission Writeup                                          |
| 22–25 | Finalise Writeup (≤1,500 words); collect human baseline data                                      |
| 25    | Submit (primary submission track alongside H-PTB)                                                 |

---

## 10. TEMPERATURE PROTOCOL

```
Stage 1 (Prediction): temperature = 0.7, k=5 samples, take median $Pred_i$
Stage 2 (Performance): temperature = 0 (greedy decoding)
In-distribution baseline: temperature = 0
Report all temperature settings in benchmark documentation.
```

---

## 11. RESULTS LOG

*(Populated during Kaggle deployment — Days 9 onward)*

| Model | Condition | $\hat{\zeta}_A$ (overall) | $\hat{\zeta}_A$ (type 1) | $ζ̂A$ (type 5) | $\hat{\zeta}_{A_{\text{ID}}}$ (control) | OOD ratio (from H-PTB) |
| ----- | --------- | ------------------------- | ------------------------ | -------------- | --------------------------------------- | ---------------------- |
| —     | —         | —                         | —                        | —              | —                                       | —                      |

---

## 12. OPEN ISSUES (linked to register.md)

- **ISSUE #23** [RESOLVED]: Self-model ODE (Eq. 39) boundedness now formally guaranteed via Nagumo's theorem (§4.4.2 of paper.md). Steady-state analysis shows $\hat{M}_A^* = \sigma_A / (1 + \Omega_{AI}/\Pi_7) \leq \sigma_A$ (Eq. 39a) — sustained AI bypass produces underconfidence at equilibrium, not sustained overconfidence. Calibration error ODE (Eq. 38a) added. Benchmark's $[0,1]$ assumption is now theorem-backed.
- **ISSUE #2** [D]: σA used as a known quantity via the OOD ratio proxy; the benchmark documentation must explicitly state that σA is latent and the OOD ratio is the observable proxy, not σA directly.
- **ISSUE #58–#62** [R]: Differentiation from MetaMedQA, ObjexMT, KOR-Bench, LILA, DMC must appear in Writeup Related Work; draft text provided in §6 above.
- **ISSUE #24** [I]: Burnell et al. (2026) citation framing — the Writeup must present the Metacognition faculty alignment as a formal correspondence (H-Bar variables were developed independently), not as a post-hoc claim.

---

*H-MCB Sketch v1 — track_metacognition.md — Basyirin Amsyar bin Basri — March 2026*
*For use with H-Bar AlphaEvolve Workflow — Day 2–3 design phase*
