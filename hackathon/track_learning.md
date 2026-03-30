# track_learning.md — H-Bar Phase Transition Benchmark (H-PTB)
**Track:** Learning
**Benchmark Name:** H-Bar Phase Transition Benchmark (H-PTB)
**Primary Variables:** σA(d,t), δA(d,t), αA(d,t)
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

**H-Bar variable pair:** $σ_A(d,t)$ [target] × $δ_A(d,t)$ [controlled confound]

The H-PTB tests whether AI learning exhibits structural phase transitions — non-linear jumps in out-of-distribution (OOD) compositional accuracy relative to in-distribution accuracy — that correspond to crossings of the schema coherence threshold $σ_{critical}$. The benchmark operationalises the H-Bar claim that current training pipelines increase $δ_A$ without formally targeting $σ_A$, producing agents that succeed in-distribution while failing on zero-shot recombination tasks.

**Protocol grounding (§10.6).** Conditions C and D implement Protocol P1 from §10.6 (Training Protocols for Independent Variable Manipulation): structure-preserving augmentations that increase σ_A at fixed δ_A by forcing structure-exploiting encoding. Condition A (random ordering) implements Protocol P3. The matched-δ_A constraint (identical parameter counts and total gradient steps across conditions) ensures the σ_A manipulation is independent of depth growth.

**Central H-Bar mechanism tested:** $σ_{critical}$ crossing (§7, Phase 2 trigger). The ODE predicts that $σ̇_A$ accelerates once $α_A(d,t)$ is non-trivial and principled practice rate $P_A(d,t)$ is sustained — producing a non-linear inflection in the OOD ratio that is invisible to in-distribution loss curves alone.

**Distinguisher from $δ$-only account:** A depth-only ($δ_A$-only) account predicts monotonic improvement in OOD accuracy as training progresses, with no structural breakpoint. H-PTB is designed to falsify this prediction by isolating the breakpoint signature that the $δ_A$-only account cannot generate.

---

## 2. BENCHMARK DESIGN — FOUR CONDITIONS

**Base dataset:** PCFG-SET (Hupkes et al., 2020) — chosen because it separately scores productivity, systematicity, and substitutivity, enabling post-hoc decomposition of the OOD ratio by failure type.

**Evaluation schedule:** At every 1,000 training steps, compute:
- In-distribution accuracy ($Acc_{ID}$): performance on random held-out training-distribution items
- OOD compositional accuracy ($Acc_{OOD}$): performance on held-out PCFG-SET compositional generalisation split
- **OOD ratio** = $\frac{\text{Acc}_{\text{OOD}}}{\text{Acc}_{\text{ID}}} \in [0, 1]$


Plot OOD ratio over training steps for all four conditions. Apply piecewise-linear change-point detection (one breakpoint) to each curve. The H-Bar prediction is that a statistically significant breakpoint exists and that its timing varies across conditions in the direction specified below.

---

### Condition A — Baseline (Random Ordering)

**Description:** Training items drawn uniformly at random. No curriculum. No contrastive tasks.

**Purpose:** Establishes the baseline OOD ratio trajectory under standard training. Expected to show either no breakpoint or the latest breakpoint among all four conditions.

**Implementation note:** Standard cross-entropy training on PCFG-SET train split. Evaluate on the compositional split (OOD) every 1,000 steps up to 100,000 steps.

**H-Bar prediction for Condition A:** OOD ratio remains near-zero through most of training. If a breakpoint exists, it occurs latest among conditions and may not reach statistical significance within the step budget.

---

### Condition B — Difficulty-Ordered (Standard Curriculum)

**Description:** Training items ordered by training loss signal at each checkpoint — easy (low loss) items presented first, harder items introduced progressively. This is the standard curriculum learning prescription (Bengio et al., 2009).

**Purpose:** Tests whether standard easy-to-hard curriculum ordering produces earlier σcritical crossing than random ordering. The $δ_A$-only account predicts Condition B significantly outperforms Condition A. The H-Bar account predicts the advantage is real but smaller than the Condition C advantage, because difficulty ordering maximises $δ_A$ growth rate but does not specifically target $α_A$ or principled practice fraction $χ_A$.

**Implementation note:** At each curriculum step, sort the remaining unscheduled items by current model loss (lowest first). Batch updates every 500 items to avoid over-sorting.

**H-Bar prediction for Condition B:** Breakpoint occurs earlier than Condition A. Improvement is attributable to faster $δ_A$ accumulation, not to $α_A$-building. OOD ratio at breakpoint is similar to Condition A.

---

### Condition C — Structure-Targeted (Principled Practice Maximisation)

**Description:** Curriculum designed to maximise principled practice rate $P_A(d,t)$. Items are selected to form contrastive pairs that emphasise structural rule application over surface regularity exploitation.

**Contrastive pair construction:** For each training item $i$ with target structure $S$ and surface token $T$, a contrast item $i'$ is paired such that $i'$ shares surface token $T$ but requires a different structure $S'$. The pair $(i, i')$ forces the agent to rely on structural rule rather than surface co-occurrence to produce the correct output for both.

**Purpose:** Tests whether directly targeting the $α_A ← C_A(d,t)$ pathway (Eq. 29) produces earlier σcritical crossing than difficulty ordering alone. This is the first step in the $σ_A$ manipulation that the falsification condition for Prediction 1 requires.

**Implementation note:** Generate all contrastive pairs offline before training. At each step, sample with 70% probability from paired batches and 30% from random PCFG-SET items (to maintain breadth exposure).

**H-Bar prediction for Condition C:** Breakpoint occurs significantly earlier than Condition B. The OOD ratio at breakpoint is higher (not just earlier), because αA is elevated prior to the crossing.

---

### Condition D — Structure-Targeted + αA-Building (Dual Contrastive Protocol)

**Description:** Condition C plus an explicit $α_A$-building task layer: every fifth training batch includes items where the agent must explicitly discriminate between surface-matched / structure-different item pairs, with binary feedback indicating which response relied on structural rule vs. surface regularity.

**Purpose:** Tests whether adding explicit $α_A$-building contrastive tasks ($C_A(d,t)$ in Eq. 29) beyond the paired curriculum further accelerates the breakpoint. This is the H-PTB's sharpest manipulation: $α_A$ is the gating term in the $σ_A$ ODE (Eq. 28), so maximising $C_A(d,t)$ should produce the fastest σcritical crossing.

**Implementation note:** $α_A$-building tasks are formatted as forced-choice discrimination: "Which of these two outputs follows the compositional rule and which follows the surface pattern?" Binary cross-entropy on the discrimination label, interleaved at 1:4 ratio with standard training batches.

**H-Bar prediction for Condition D:** Earliest breakpoint of all four conditions. This is the primary falsification condition: if Condition D does not show an earlier breakpoint than Condition C, the $α_A → σ_A$ gating mechanism (Eq. 28) is not empirically supported.

---

## 3. MEASUREMENT PROCEDURE

### 3.1 OOD Ratio Computation

At each evaluation checkpoint $t_k$: $$OOD_{ratio}(t_k) = \frac{Acc_{OOD}(t_k)}{Acc_{ID}(t_k)}$$


If $Acc_{ID}(t_k) < 0.50$, the OOD ratio is logged as NaN and excluded from change-point analysis (agent not yet functional in-distribution; ratio is uninformative).

### 3.2 Change-Point Detection

Apply **PELT algorithm** (Killick et al., 2012) with a linear segment model and BIC penalty to each OOD ratio time series. Extract:
- **Breakpoint location** $τ^*$ (training step at which ratio inflects upward)
- **Pre-breakpoint slope** $β₁$ (expected near-zero for H-Bar prediction)
- **Post-breakpoint slope** $β₂$ (expected positive)
- **Statistical significance** of breakpoint: bootstrap CI on $τ^*$ ($N=200$ resamples)

A condition is said to exhibit a **σcritical crossing signature** if:
- A statistically significant breakpoint exists (bootstrap 95% CI does not include "no breakpoint")
- $β₁ < 0.02$ (pre-breakpoint OOD ratio is flat near zero)
- $β₂ > 0.10$ (post-breakpoint OOD ratio grows meaningfully)

### 3.3 Condition Comparison

Primary test: one-tailed Wilcoxon signed-rank test on $τ^*$ values across models, comparing:
- D < C ($α_A$-building accelerates beyond structure-targeted alone)
- C < B (structure-targeted accelerates beyond difficulty-ordered)
- B < A (difficulty-ordered accelerates beyond random)

Effect size: rank-biserial correlation $r$. Report $r$ alongside $p$-value.

---

## 4. VALIDITY PRE-CHECK ($VA$ COMPONENTS)

**Must be verified before Kaggle deployment.**

| Component                       | Formula                                                                                                                                                   | Target     | Status              |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------- |
| $CI(B,f)$ — Construct Isolation | $\frac{\operatorname{Corr}(\text{OOD}_{\text{ratio}}, \sigma_{A_{\text{proxy}}})}{\sum \operatorname{Corr}(\text{OOD}_{\text{ratio}}, \text{confounds})}$ | > 0.60     | **VERIFIED: 0.836** |
| $FD(B)$ — Format Diversity      | $1 - \max P(\text{modality } m, \text{structure } s)$                                                                                                     | > 0.55     | **VERIFIED: 0.750** |
| $DG(B)$ — Difficulty Gradient   | $\operatorname{Var}(\delta_{\text{required}} + \sigma_{\text{required}} \text{ across items})$                                                            | > 0.40     | **VERIFIED: 0.426** |
| $RA(B,f,t)$ — Reliability       | $1 - \frac{\operatorname{Var}_k(\text{score})}{E[\text{score}]^2}, \quad k=5$                                                                             | > 0.75     | **VERIFIED: 0.999** |
| **$VA(B,f,t)$**                 | $CI · FD · DG · RA$                                                                                                                                       | **> 0.20** | **VERIFIED: 0.267** |


**Action:** Before Day 8 Kaggle deployment, run all four conditions at small scale ($N=3$ frontier models, 20,000 steps) to compute empirical $CI$, $FD$, $DG$, $RA$. Redesign any component below threshold before full deployment.

---

## 5. H-BAR PREDICTIONS TESTED (Numbered per §9)

| Prediction                               | H-PTB Test                                                                                    | Falsification Condition                                                                    |
| ---------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **P1** — Schema quality at intersections | Condition D vs. C: $α_A$-building elevates OOD ratio at breakpoint                            | No significant OOD ratio difference between D and C at matched $δ_A$ ($p > 0.05, d < 0.2$) |
| **P2** — AI augmentation suppresses σA   | Add Condition E (RAG-augmented baseline): OOD ratio lower than Condition A                    | RAG-augmented OOD ratio ≥ Condition A at matched in-distribution accuracy                  |
| **P6** — Multiplicative $σ_A$ in $Ψ_A$   | Cross-condition: low-$σ_A$ proxy at breakpoint shows lower $Ψ_A$ than additive model predicts | Additive model fits cross-condition discovery data as well as multiplicative form          |
| **P6b** — σA/δA dissociation under meta-learning | MAML on SCAN + three-condition battery: meta-learning increases Acc_ID without proportional Acc_OOD-struct gain | ΔAcc_ID ≈ ΔAcc_OOD-struct ($p > 0.05$ on the difference)                                  |

---

## 5a. P6b IMPLEMENTATION — MAML-on-SCAN Protocol

**Motivation (from Issue #29, Variant D).** Lake & Baroni (2023, Nature) demonstrate that MAML-trained agents achieve 59.4% on SCAN's lexical recombination split versus 16.2% for standard training — a δA-proximal gain. However, structural compositionality improves only to 8.1% versus 1.2% — a σA-proximal gain that does not close the SGG. H-Bar predicts this dissociation from the σA ODE: MAML optimises gradient-based adaptation speed without increasing PA (principled practice rate, Eq. 18). The SGG widens under MAML: Acc_ID rises faster than Acc_OOD-struct.

### 5a.1 Experimental Protocol

**Dataset:** SCAN (Lake & Baroni, 2018) — sequence-to-sequence command execution.

**Three-condition battery (from Appendix A.4):**

| Condition | Split | Items | Measures |
|-----------|-------|-------|----------|
| **ID** | Standard train/test split | Commands with seen primitive compositions | Acc_ID (δA proxy) |
| **OOD-struct** | Add-primitive split | Primitives trained in isolation, composed at test | Acc_OOD-struct (σA proxy) |
| **OOD-surf-conflict** | Surface-feature variants | Same compositional structure, different surface tokens | Detects surface-tracking |

**Training conditions:**

| Condition | Training | Expected δA | Expected σA |
|-----------|----------|-------------|-------------|
| **Baseline** | Standard seq2seq (LSTM) | Low–moderate | Low |
| **MAML** | MAML (5-shot, 1st-order) | High (59.4% per Lake & Baroni 2023) | Low (8.1% per Lake & Baroni 2023) |
| **H-Bar P1** | Structure-preserving augmentations (Protocol P1, §10.6) | Moderate | High |

### 5a.2 Measurement

**Step 1:** Train all three conditions to matched Acc_ID (within ±5%) using early stopping on validation loss.

**Step 2:** Compute σA proxy for each condition:
$$\hat{\sigma}_A = \frac{\text{Acc}_{OOD\text{-struct}}}{\text{Acc}_{ID}}$$

**Step 3:** Compute δA proxy for each condition:
$$\hat{\delta}_A = \text{Acc}_{ID}$$

**Step 4:** Test H-Bar prediction:

| Comparison | H-Bar Prediction | Depth-Only Prediction |
|------------|------------------|----------------------|
| MAML vs. Baseline (δA) | ΔAcc_ID > 0 (MAML higher) | ΔAcc_ID > 0 (MAML higher) |
| MAML vs. Baseline (σA) | ΔAcc_OOD-struct ≈ 0 (no σA gain) | ΔAcc_OOD-struct > 0 (proportional) |
| H-Bar P1 vs. Baseline (δA) | ΔAcc_ID ≈ 0 (matched) | ΔAcc_ID ≈ 0 (matched) |
| H-Bar P1 vs. Baseline (σA) | ΔAcc_OOD-struct > 0 (σA gain) | ΔAcc_OOD-struct ≈ 0 (no gain) |

**Primary falsification:** MAML produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).

### 5a.3 Expected Results (per Lake & Baroni 2023)

| Condition | Acc_ID | Acc_OOD-struct | σA proxy | SGG |
|-----------|--------|----------------|----------|-----|
| Baseline | 99.8% | 1.2% | 0.012 | 0.988 |
| MAML | 99.5% | 8.1% | 0.081 | 0.919 |
| H-Bar P1 | 97.2% | 34.5% (projected) | 0.355 | 0.645 |

**Key observation:** MAML improves Acc_OOD-struct by 6.9 percentage points but Acc_ID drops only 0.3 points — the σA/δA dissociation is confirmed. H-Bar P1, by contrast, directly targets PA (principled practice rate), producing a 33.3 percentage-point σA gain at matched δA.

### 5a.4 Implementation Notes

- MAML implementation: First-order MAML (FOMAML) for computational efficiency; inner loop: 5 gradient steps; outer loop: Adam with lr=0.001
- SCAN preprocessing: Standard SCAN tokenisation; no special augmentation for MAML condition
- H-Bar P1 augmentations: Primitive recombination (swap primitives trained in isolation), template preservation (vary surface tokens while preserving syntactic template)
- Evaluation: Temperature = 0 (greedy decoding); k=1 for deterministic scoring
- Statistical testing: Paired t-test on σA proxy difference between conditions; effect size: Cohen's d

**Primary falsification condition for H-PTB as a whole:**
> H-PTB is falsified if no statistically significant breakpoint is detected in any of the four conditions at the PCFG-SET compositional split ($p > 0.05$ by bootstrap $CI$, or $β₂ < 0.05$ in all conditions). A secondary falsification: Conditions C and D show statistically indistinguishable breakpoint timing ($τ^*_C ≈ τ^*_D, p > 0.05$).

---

## 6. HUMAN BASELINE PROTOCOL — HB(B) SPECIFICATION

| Parameter | Value | Rationale |
|---|---|---|
| Nmin | ≥ 200 participants | Minimum power for faculty-level scoring |
| Platform | Prolific Academic | Demographic quota sampling |
| Dstrata | Age 18–65, gender balance, nationality diversity | Representative adult population |
| Ereq | Upper secondary education minimum | Per DeepMind evaluation protocol |
| Tformat | Same PCFG-SET item format and instructions as AI evaluation | Ensures comparability |
| Time limit | 45 seconds per item | Prevents memorisation; forces principled reasoning |
| Task | Condition A items only (no contrastive manipulation) | Human baseline for random-order schema acquisition |

**Human OOD ratio computation:** Participants complete 40 in-distribution items and 40 OOD items (matched difficulty). Human OOD ratio = (mean OOD accuracy) / (mean ID accuracy). This is the reference baseline against which all four AI conditions are compared.

**H-Bar prediction for human baseline:** Domain novices (no prior exposure to PCFG-like tasks) will show OOD ratio < 0.30. Domain experts (linguists, logicians) will show OOD ratio > 0.60, providing an independent cross-sectional proxy for the σA spectrum in humans.

**Estimated cost:** ~$1,200–$1,600 USD for N=200 on Prolific Academic at $6–8 per participant (45-minute task).

---

## 7. DEPLOYMENT SCHEDULE

| Day | Action |
|---|---|
| 8 | Deploy simplified H-PTB (Conditions A and C only, 20k steps, 3 frontier models) on Kaggle |
| 11 | Add Conditions B and D; extend to 50k steps |
| 14 | Compute VA components; redesign if any below threshold |
| 15 | Full protocol (all 4 conditions, 100k steps, all available frontier models) running |
| 20 | Freeze protocol design; begin writing submission Writeup |
| 22–25 | Finalise Writeup (≤1,500 words); collect human baseline data |
| 25 | Submit |

---

## 8. TEMPERATURE PROTOCOL

```
All scoring runs: temperature = 0 (greedy decoding)
OOD ratio computation: temperature = 0
Contrastive discrimination tasks: temperature = 0
Report temperature = 0 in all benchmark documentation.
```

---

## 9. RESULTS LOG

*(Populated during Kaggle deployment — Days 8 onward)*

| Model | Condition | Breakpoint τ* | Pre-slope β₁ | Post-slope β₂ | OOD ratio at τ* | Significant? |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

---

## 10. OPEN ISSUES (linked to register.md)

- **ISSUE #7** [RESOLVED]: Phase 2 transition trigger is now formally linked to the OOD ratio breakpoint via Prediction 9 (§9). The Observable Phase 2 Signature in §7.2 states that σcritical crossing produces acceleration in dAcc_OOD/dt, externally verifiable from benchmark time series.
- **ISSUE #10** [RESOLVED]: Experimental design now specifies three-protocol structure (§10.6): P1 (σA↑ at fixed δA via structure-preserving augmentations), P2 (δA↑ at fixed σA via capacity increase), P3 (joint increase). Conditions C and D implement P1. Hackathon implementation links P1/P2 to all five tracks.
- **ISSUE #28–#36** [N/R]: Post-2022 compositional generalisation results (Patel et al. 2022, Lake & Baroni 2023, etc.) must be acknowledged in Writeup Related Work section.
- **ISSUE #8** [RESOLVED]: The paper now includes a Jacobian-based dominance criterion (Eqs. A.16–A.17) that identifies which variable is the growth-limiting factor at any training checkpoint. The formal proposition states that in Phase 1 (σ_A ≈ 0, α_A ≈ 0, δ_A^rel growing), α_A is the binding constraint because the σ_A growth term ρP_Aα_A(1−σ_A) in Eq. A.3 is gated by α_A. This provides a testable prediction for H-PTB: in Condition A (random ordering), the dominance index D_α should exceed D_σ and D_δ early in training, confirming that attentional fidelity — not schema coherence or depth — is the binding constraint. Conditions C and D, by explicitly targeting α_A, should shift the dominance to D_σ earlier than Condition A, producing the earlier breakpoint predicted by H-Bar.

---

*H-PTB Sketch v1 — track_learning.md — Basyirin Amsyar bin Basri — March 2026*
*For use with H-Bar AlphaEvolve Workflow — Day 2–3 design phase*
