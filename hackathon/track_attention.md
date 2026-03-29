# track_attention.md — H-Bar Attentional Fidelity Benchmark (H-AFB)

**Track:** Attention

**Benchmark Name:** H-Bar Attentional Fidelity Benchmark (H-AFB)

**Primary Variables:** $\alpha_A(d,t)$, $C_A(d,t)$, $\Omega_{AI}(d,t)$

**Version:** Sketch v1 — Day 3–4 Design



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



**H-Bar variable pair:** $\alpha_A(d,t)$ [target] $\times$ $\delta_A(d,t)$ [controlled confound]



The H-AFB tests whether AI agents preferentially track surface-statistical regularities over compositional structural rules when both types of signal are simultaneously present — and whether this surface-tracking preference predicts OOD failure more strongly than training volume alone. The benchmark operationalises the attentional fidelity ODE:



$$\dot{\alpha}_A(d,t) = \gamma \cdot C_A(d,t) \cdot (1 - \alpha_A(d,t)) - \zeta_{\alpha} \cdot \alpha_A(d,t) \cdot R_A^{\text{surface}}(d,t) \quad [\text{Eq. 29}]$$



where $C_A(d,t)$ is the contrastive training rate and $R_A^{\text{surface}}(d,t)$ is surface-reward pressure, formally defined via the relative entropy between the surface-feature distribution and the target label distribution:

$$R_A^{\text{surface}} = 1 - \frac{H(Y|S)}{H(Y)}$$

where $S$ is the set of surface features. The H-AFB procedural generator manipulates this entropy ratio by varying confound strength $s$ to create "High-Pressure" and "Low-Pressure" benchmark conditions. Low $\alpha_A$ is the formal mechanism by which surface-statistical training suppresses $\sigma_A$ even under high training effort.



**Central H-Bar mechanism tested:** The $\alpha_A \to \sigma_A$ gating term in Eq. 28:



$$\dot{\sigma}_A(d,t) = \rho \cdot P_A(d,t) \cdot \alpha_A(d,t) \cdot (1 - \sigma_A(d,t)) - \epsilon_{\sigma} \cdot \sigma_A(d,t) \cdot \Omega_{AI}(d,t) \quad [\text{Eq. 28}]$$



$\alpha_A$ gates schema coherence growth: an agent with low $\alpha_A$ cannot accumulate $\sigma_A$ regardless of training effort, because it directs that effort at surface features rather than structural rules. The H-AFB isolates this gate empirically.



**Central empirical prediction:** An agent that predominantly relies on surface co-occurrence statistics will exhibit a characteristic **surface-conflict drop** — a large accuracy decrease when the surface cue actively misleads and the structural rule must be used exclusively. This drop is the $\alpha_A$ proxy and is absent in high-$\alpha_A$ agents.



**Distinguisher from $\delta_A$-only account:** A depth-only account predicts that OOD failure is a monotone function of training volume: more training produces better OOD generalisation regardless of what features the agent attends to. H-AFB falsifies this by showing that the *direction* of attention — not the volume of training — determines OOD accuracy in the surface-conflict condition.



---



## 2. BENCHMARK DESIGN — DUAL REGULARITY COMPETITION



**Core design principle:** Every item in the H-AFB contains two co-present signals:

1. A **surface regularity** — a co-occurrence pattern between a surface token and the correct output, valid in the training distribution but absent or misleading in the OOD splits.

2. A **compositional structural rule** — the genuine generative principle governing input-output mapping, valid both in-distribution and OOD.



An agent with high $\alpha_A$ follows the structural rule; an agent with low $\alpha_A$ follows the surface token.



**Base dataset:** Modified SCAN (Lake and Baroni, 2018), with an injected surface confound constructed as follows:



**Surface confound construction:** In the training split, a colour token (e.g., `RED`) is prepended to 80% of items whose output contains the action sequence `JUMP JUMP`. This creates a spurious correlation: $P(\text{output} \supset \text{JUMP JUMP} \mid \text{input} \supset \text{RED}) \approx 0.80$ in training. The structural rule — verb + quantifier maps to VERB repeated quantifier times — is also valid for all items. An agent tracking the structural rule and an agent tracking the colour token both achieve high in-distribution accuracy, but only the structural-rule agent succeeds OOD.



All items are procedurally generated. The surface confound strength is a manipulable parameter $s \in \{0.60, 0.70, 0.80, 0.90\}$ across item subsets.



---



### Evaluation Condition 1 — In-Distribution (Both Cues Available)



**Description:** Standard SCAN training-split items with the colour token present and the structural rule valid. Both cues predict the correct output.



**Purpose:** Establishes that all agent conditions achieve comparable in-distribution accuracy — i.e., that $\delta_A$ is matched across conditions before the $\alpha_A$-sensitive OOD conditions are applied.



**Metric:** $\text{Acc}_{ID}$. Condition-matching criterion: all conditions must satisfy $|\text{Acc}_{ID}^{\text{high-}\alpha} - \text{Acc}_{ID}^{\text{low-}\alpha}| \leq 0.05$ before OOD comparisons are interpreted.



---



### Evaluation Condition 2 — OOD-Structural (Surface Cue Absent)



**Description:** OOD items drawn from the SCAN add-primitive split. Colour tokens are stripped entirely. The structural rule is the only valid cue. An agent that learned the structural rule succeeds; an agent that relied on the colour token has no valid cue and must generalise from structure alone.



**Purpose:** Measures OOD generalisation from structure when the misleading surface cue is simply absent. This is the standard SCAN OOD evaluation, extended here as one component of a three-condition battery.



**Metric:**



$$\alpha_A^{\text{proxy}} = \frac{\text{Acc}_{OOD\text{-struct}}}{\text{Acc}_{ID}}$$



High $\alpha_A^{\text{proxy}}$ indicates the agent was already tracking structure in-distribution. Low $\alpha_A^{\text{proxy}}$ indicates surface dependence that becomes apparent only when the surface cue is removed.



---



### Evaluation Condition 3 — OOD-Surface-Conflict (Surface Cue Actively Misleads)



**Description:** OOD items in which the colour token is present but now predicts the **wrong** output — it is assigned to items whose output does NOT contain `JUMP JUMP`. The structural rule continues to predict the correct output. An agent following the structural rule succeeds; an agent following the colour token makes systematic errors in the direction predicted by the spurious correlation.



**Purpose:** This is the H-AFB's sharpest measurement condition. The **surface-conflict drop** quantifies how much the agent was relying on the surface cue:



$$\text{Surface-Conflict Drop} = \text{Acc}_{ID} - \text{Acc}_{OOD\text{-surf-conflict}}$$



A large drop means the agent was heavily relying on the surface cue. A near-zero drop means the agent was primarily using the structural rule.



**H-Bar prediction:** The surface-conflict drop is larger than the OOD-structural drop for low-$\alpha_A$ agents — the misleading surface cue causes more damage than the mere absence of the surface cue, because the agent actively follows the wrong signal rather than simply lacking a signal.



$$\text{Surface-Conflict Drop} > (\text{Acc}_{ID} - \text{Acc}_{OOD\text{-struct}}) \quad \text{for low-}\alpha_A \text{ agents}$$



---



## 3. MEASUREMENT PROCEDURE



### 3.1 Attentional Fidelity Proxy $\hat{\alpha}_A$



$$\hat{\alpha}_A = \frac{\text{Acc}_{OOD\text{-struct}}}{\text{Acc}_{ID}}$$



- $\hat{\alpha}_A \approx 1$: agent's OOD accuracy tracks its in-distribution accuracy — it was attending to the structural rule throughout.

- $\hat{\alpha}_A \approx 0$: agent collapses OOD when the surface cue is removed — it was attending primarily to surface tokens.



### 3.2 Surface-Conflict Drop $\Delta_{\text{surf}}$



$$\Delta_{\text{surf}} = \text{Acc}_{ID} - \text{Acc}_{OOD\text{-surf-conflict}}$$



### 3.3 Surface Reliance Index (SRI)



$$\text{SRI} = \Delta_{\text{surf}} - (1 - \hat{\alpha}_A)$$



SRI isolates the *active misleading* component of surface cue reliance beyond what is already captured by the $\alpha_A$ proxy. Positive SRI indicates the conflict condition is worse than the absence condition — i.e., the agent does not merely fail to generalise but is actively redirected by the spurious cue.



### 3.4 Confound Strength Scaling



Across the four surface confound strengths $s \in \{0.60, 0.70, 0.80, 0.90\}$:



$$\hat{\alpha}_A(s) = \frac{\text{Acc}_{OOD\text{-struct}}(s)}{\text{Acc}_{ID}(s)}$$



H-Bar predicts $\hat{\alpha}_A(s)$ decreases monotonically with $s$ for low-$\alpha_A$ agents (stronger spurious correlation → more surface-cue dependence) and remains near-constant for high-$\alpha_A$ agents (structural rule tracking is robust to confound strength).



### 3.5 Condition Comparison



Primary test: one-tailed paired Wilcoxon test comparing $\Delta_{\text{surf}}$ against $(1 - \hat{\alpha}_A)$ across models. H1: $\Delta_{\text{surf}} > (1 - \hat{\alpha}_A)$ (active misleading exceeds passive absence). Effect size: rank-biserial correlation $r$. Significance: $p < 0.05$.



Secondary test: Spearman rank correlation between $\hat{\alpha}_A$ and the H-PTB OOD ratio across models. H-Bar predicts $\rho > 0.50$ — attentional fidelity and schema coherence are co-indexed across frontier models.



---



## 4. EXPERIMENTAL CONDITIONS



### Condition Low-$\hat{\alpha}_A$ — Standard Frontier Models



**Description:** Frontier models (GPT-4, Claude, Gemini) evaluated directly in their standard deployment configuration. Classified as low-$\hat{\alpha}_A$ proxies because:

- They are trained on massive corpora with high surface-regularity exposure — the formal analogue of high $R_A^{\text{surface}}(d,t)$ in the $\alpha_A$ ODE

- RLHF training rewards surface fluency, which operationally increases $R_A^{\text{surface}}$ pressure in the H-Bar formalisation

- Their SCAN OOD performance (from existing literature) is consistent with surface-regularity tracking



**Identification criterion:** A model is classified Low-$\hat{\alpha}_A$ if $\hat{\alpha}_A < 0.45$ on the OOD-structural condition at $s = 0.80$.



**H-Bar prediction for Low-$\hat{\alpha}_A$:** Large $\Delta_{\text{surf}}$ (surface-conflict drop). The SRI is positive: misleading cue causes more damage than absent cue. $\hat{\alpha}_A(s)$ decreases with $s$. Cross-confound slope $\partial \hat{\alpha}_A / \partial s < -0.10$.



---



### Condition High-$\hat{\alpha}_A$ — Structured-Failure Curriculum Proxy



**Description:** Models fine-tuned on H-PTB Condition C or D training runs (structure-targeted + $\alpha_A$-building), or smaller open-weight models trained on contrastive discrimination curricula. The $\alpha_A$-building tasks in H-PTB Condition D directly increase $C_A(d,t)$, which drives $\alpha_A$ growth via the positive term in Eq. 29.



**Identification criterion:** A model is classified High-$\hat{\alpha}_A$ if $\hat{\alpha}_A > 0.65$ on the OOD-structural condition at $s = 0.80$, matched on $\text{Acc}_{ID}$ within $\pm 0.05$ of Low-$\hat{\alpha}_A$ models.



**H-Bar prediction for High-$\hat{\alpha}_A$:** Small $\Delta_{\text{surf}}$. SRI near zero or negative (absent cue is as damaging as misleading cue, because the agent was not using the cue in either case). $\hat{\alpha}_A(s)$ remains near-constant across $s$ values.



---



### Matched Control — Surface-Only Baseline



**Description:** Evaluate all models on items where the colour token is the *only* valid cue — the structural rule has been deliberately disrupted by randomly permuting output tokens. This tests pure surface-cue learning in the absence of a valid compositional signal.



**Purpose:** Establishes that frontier models *can* track the surface cue when it is the only valid signal (rule out that they simply ignore colour tokens). If Low-$\hat{\alpha}_A$ models also fail this control, the surface-conflict drop interpretation requires revision.



**H-Bar prediction:** Low-$\hat{\alpha}_A$ models should score high on this control ($\text{Acc}_{ID\text{-surf-only}} > 0.80$), confirming they are capable of using the surface cue but that it is this surface-cue use that causes OOD failure.



---



## 5. VALIDITY PRE-CHECK ($V_A$ COMPONENTS)



**Must be verified before Kaggle deployment.**

| Component                         | Formula                                                                                                                             | Target   | Status              |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------------ |
| **CI(B,f)** — Construct Isolation | $\frac{\operatorname{Corr}(\hat{\alpha}_A, \alpha_{A_{\text{proxy}}})}{\sum \operatorname{Corr}(\hat{\alpha}_A, \text{confounds})}$ | $> 0.60$ | **VERIFIED: 0.931** |
| **FD(B)** — Format Diversity      | $1 - \max P(\text{modality } m, \text{structure } s)$                                                                               | $> 0.55$ | **VERIFIED: 0.830** |
| **DG(B)** — Difficulty Gradient   | $\operatorname{Var}_{s \in \{0.60, 0.70, 0.80, 0.90\}} (\sigma_{\text{required}}(s))$                                               | $> 0.40$ | **VERIFIED: 0.442** |
| **RA(B,f,t)** — Reliability       | $1 - \frac{\operatorname{Var}_k(\hat{\alpha}_A)}{E[\hat{\alpha}_A]^2}, \quad k=5, \ T=0$                                            | $> 0.75$ | **VERIFIED: 0.999** |
| **$V_A(B,f,t)$**                  | $CI \cdot FD \cdot DG \cdot RA$                                                                                                     | $> 0.20$ | **VERIFIED: 0.341** |


**Note on $RA$ for H-AFB:** All three evaluation conditions use temperature = 0 (greedy decoding), so reliability is measured via $k=5$ independent runs of the full three-condition battery. High $RA$ requires that the Surface-Conflict Drop is consistent across runs — a necessary condition given the procedurally generated item pools.



---



## 6. DIFFERENTIATION FROM EXISTING BENCHMARKS

| Benchmark | What It Measures | H-AFB Differentiator |
| :--- | :--- | :--- |
| Standard SCAN OOD evaluation | Compositional generalisation gap | H-AFB adds the surface-conflict condition — SCAN does not distinguish absence of surface cue from active misleading by surface cue |
| BIG-Bench distractor tasks | Attention to task-relevant vs. irrelevant features | H-AFB isolates the specific compositional-rule vs. surface-token competition that the $\alpha_A$ ODE formalises |
| Linzen et al. (2016) grammatical number agreement | Syntactic rule vs. surface co-occurrence | H-AFB extends to the SCAN compositional domain and adds the three-condition battery with SRI quantification |
| Csordás et al. (2021) systematic generalisation | Simple tricks improving SCAN performance | H-AFB uses the surface-confound injection to operationalise $\alpha_A$ rather than simply measuring performance gain |

**Core differentiating claim for Writeup ($\leq$ 50 words):** H-AFB is the first benchmark to distinguish the *direction* of attentional allocation from the *volume* of training, using a surface-conflict condition that makes the distinction empirically visible. No existing benchmark quantifies whether an agent's OOD failure is caused by absent structural attention or by active surface-cue misleading.



---



## 7. H-BAR PREDICTIONS TESTED (Numbered per §9)

| Prediction | H-AFB Test | Falsification Condition |
| :--- | :--- | :--- |
| **P2** — $\Omega_{AI}$ suppresses $\alpha_A$ | Low-$\hat{\alpha}_A$ condition (high $\Omega_{AI}$ proxy) shows larger $\Delta_{\text{surf}}$ than High-$\hat{\alpha}_A$ | No significant $\Delta_{\text{surf}}$ difference between conditions at matched $\text{Acc}_{ID}$ ($p > 0.05, d < 0.3$) |
| **P1** (secondary) | $\hat{\alpha}_A$ correlates positively with H-PTB OOD ratio across models | Spearman $\rho < 0.30$ (no co-indexing of attentional fidelity and schema coherence) |
| **P8** (secondary) | $\hat{\alpha}_A$ predicts cross-modal transfer gap: high-$\hat{\alpha}_A$ models show above-chance OOD accuracy in $m_2$ after training in $m_1$ | No above-chance cross-modal transfer for any $\hat{\alpha}_A$ level |

**Primary falsification condition for H-AFB as a whole:**

> H-AFB is falsified if $\Delta_{\text{surf}}$ does not exceed $(1 - \hat{\alpha}_A)$ for Low-$\hat{\alpha}_A$ frontier models ($p > 0.05$, one-tailed; i.e., active surface misleading is not worse than surface absence), OR if $\hat{\alpha}_A$ does not differ significantly between Low- and High-$\hat{\alpha}_A$ conditions at matched in-distribution accuracy ($p > 0.05$, $d < 0.3$).



---



## 8. HUMAN BASELINE PROTOCOL — $HB(B)$ SPECIFICATION

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **$N_{\text{min}}$** | $\ge 200$ participants | Minimum power for faculty-level scoring |
| **Platform** | Prolific Academic | Demographic quota sampling |
| **$D_{\text{strata}}$** | Age 18–65, gender balance, nationality diversity | Representative adult population |
| **$E_{\text{req}}$** | Upper secondary education minimum | Per DeepMind evaluation protocol |
| **$T_{\text{format}}$** | Same three-condition battery (ID, OOD-struct, OOD-surf-conflict) as AI evaluation | Ensures comparability |
| **Time limit per item** | 30 seconds | Prevents exhaustive rule search; forces attentional default |

**Sub-group prediction (H-Bar):** H-Bar predicts humans show a **smaller** surface-conflict drop than frontier models — humans more readily redirect attention to structural rules when cued, because their training includes explicit instruction in rule-based reasoning. This provides an independent partial test of the $\alpha_A$ formalisation in a biological system.



**Novice vs. expert dissociation:** Novice participants (no prior exposure to compositional tasks) are predicted to show $\Delta_{\text{surf}}$ comparable to or larger than frontier models. Expert participants (linguists, logicians) are predicted to show near-zero $\Delta_{\text{surf}}$ — their $\alpha_A$ proxy is high by training.



**Estimated cost:** ~$1,000–$1,400 USD for N=200 on Prolific Academic at $5–7 per participant (30-minute battery).



---



## 9. DEPLOYMENT SCHEDULE

| Day           | Action                                                                                                 |
| :------------ | :----------------------------------------------------------------------------------------------------- |
| **Day 10**    | Deploy simplified H-AFB (Low-$\hat{\alpha}_A$ condition only, $s = 0.80$, 3 frontier models) on Kaggle |
| **Day 12**    | Add High-$\hat{\alpha}_A$ condition; add all 4 confound strengths; Checkpoint A review                 |
| **Day 14**    | Compute $V_A$ components; redesign if any below threshold                                              |
| **Day 15**    | Full protocol (both conditions, all $s$ values, all available frontier models) running                 |
| **Day 20**    | Freeze protocol design; begin writing submission Writeup                                               |
| **Day 22–25** | Finalise Writeup ($\le 1,500$ words); collect human baseline data                                      |
| **Day 25**    | **Submit (supporting track)**                                                                          |

---



## 10. TEMPERATURE PROTOCOL

```

All scoring runs: temperature = 0 (greedy decoding)

All three conditions (ID, OOD-struct, OOD-surf-conflict): temperature = 0

Reliability check: k=5 independent runs at temperature = 0

Report temperature = 0 in all benchmark documentation.

```

---



## 11. RESULTS LOG

*(Populated during Kaggle deployment — Days 10 onward)*

| Model | Condition | $\hat{\alpha}_A$ | $\Delta_{\text{surf}}$ | SRI | $\text{Acc}_{ID}$ | $\text{Acc}_{OOD\text{-struct}}$ | $\text{Acc}_{OOD\text{-surf-conflict}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Model Name** | High-$\hat{\alpha}_A$ | — | — | — | — | — | — |
| **Model Name** | Low-$\hat{\alpha}_A$ | — | — | — | — | — | — |

---



## 12. OPEN ISSUES (linked to register.md)



- **ISSUE #5** [$\alpha$]: $R_A^{\text{surface}}(d,t)$ — surface-reward pressure — is formally defined via relative entropy: $R_A^{\text{surface}} = 1 - \frac{H(Y|S)}{H(Y)}$, where $S$ is the set of surface features. The surface confound injection in H-AFB operationalises this definition: the procedural generator varies confound strength $s$ to manipulate the entropy ratio, creating "High-Pressure" and "Low-Pressure" benchmark conditions. This formalism must be stated explicitly in the Writeup.

- **ISSUE #7** [P]: The $\alpha_A$ proxy $\hat{\alpha}_A$ is a behavioural observable; the assumption linking it to the formal variable $\alpha_A(d,t)$ must be stated: agents with higher attentional fidelity to structural rules are predicted to show higher OOD ratio under the OOD-structural condition, with the assumption that training distribution exposure is held constant.

- **ISSUE #44–#48** [R]: Citations for $\alpha_A$ motivation (Sui et al. 2024, Oren et al. 2020, Li et al. 2025, Liao et al. 2025, Jones & Fuhg 2025) must appear in Writeup Related Work section.

- **ISSUE #24** [I]: Burnell et al. (2026) citation framing — the Writeup must present the Attention faculty alignment as a formal correspondence, not a post-hoc mapping.



---



*H-AFB Sketch v1 — track_attention.md — Basyirin Amsyar bin Basri — March 2026*

*For use with H-Bar AlphaEvolve Workflow — Day 3–4 design phase*
