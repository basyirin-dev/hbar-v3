# track_executive.md — H-Bar Delegation Control Benchmark (H-DCB)

**Track:** Executive Functions

**Benchmark Name:** H-Bar Delegation Control Benchmark (H-DCB)

**Primary Variables:** $\Xi_A^I(t)$, $\Xi_A^P(t)$, $\Xi_A^F(t)$, $D^*(d,t)$

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



**H-Bar variable pair:** $\Xi_A^I(t)$ [target — inhibitory control] $\times$ $\sigma_A(d,t)$, $\delta_A(d,t)$ [controlled confounds]



The H-DCB tests the sharpest single empirical claim in the H-Bar framework: the **non-monotonic delegation prediction**. The $\sigma$-gated delegation criterion (Eq. 23) predicts that the relationship between AI retrieval density $\rho$ and compositional accuracy $\text{Acc}_{\text{comp}}$ changes sign as a function of schema coherence:



$$\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} < 0 \quad \text{for } \sigma_A < \sigma_{\text{critical}} \quad \text{(more delegation → worse OOD performance)}$$



$$\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} > 0 \quad \text{for } \sigma_A \geq \sigma_{\text{critical}} \quad \text{(more delegation → better OOD performance)}$$



This prediction is strictly non-monotonic and is not recoverable from any account that treats retrieval augmentation as uniformly beneficial or uniformly harmful. It is the H-Bar claim that no existing RAG, Self-RAG, FLARE, or IKEA architecture models.



**Central H-Bar mechanism tested:** The $\Xi_A^I$ sub-component governs the inhibition of AI bypass — the probability of choosing the structural route over the retrieved output when both are available (Eq. 35–36). For low-$\sigma_A$ agents, retrieved context displaces the principled structural engagement that would drive $\sigma_A$ growth, producing a net negative effect. For high-$\sigma_A$ agents, retrieved context augments already-grounded schema without displacing it, producing a net positive effect.



The effective composite profile (Eq. 24) captures this gate:



$$\delta_{\text{eff}}(d,t) = \delta_A(d,t) + \Phi_A \cdot f(\delta_{AI}(d,t), \sigma_A(d,t))$$



where $f$ is $\sigma_A$-gated: at $\sigma_A \approx 0$, $f \to 0$ regardless of $\delta_{AI}$ magnitude.



**Distinguisher from $\delta_A$-only account:** Any account that treats $\delta_{AI}$ as additively beneficial predicts $\partial \text{Acc}_{\text{comp}} / \partial \rho > 0$ for all agent conditions. The H-DCB is designed to produce a sign reversal across agent conditions — a finding that is structurally impossible under any monotone model.



---



## 2. BENCHMARK DESIGN — RETRIEVAL DENSITY MANIPULATION



**Base dataset:** COGS (Kim and Linzen, 2020) compositional generalisation split, extended with a RAG wrapper that injects retrieved context at a manipulable density $\rho$.



**RAG construction:** A retrieval corpus is constructed from COGS training items. For each evaluation item, the retrieval system returns the $k=3$ nearest training items by surface-level token overlap (BM25). Retrieved items are prepended to the evaluation item as a context block:



> *"Here are some related examples from training: [retrieved item 1] ... [retrieved item 3]. Now answer: [evaluation item]."*



This retrieval system is intentionally surface-based — it retrieves by token overlap rather than structural similarity. This creates the H-Bar test: a low-$\sigma_A$ agent that relies on surface features will be helped or confused by surface-similar retrieved items in a way that depends on whether those retrieved items share the same structural rule as the evaluation item.



**Retrieval density $\rho$:** The fraction of evaluation items for which retrieved context is provided. Varied systematically across $\rho \in \{0.0, 0.20, 0.40, 0.60, 0.80, 1.0\}$.



At each $\rho$ level, measure:

- $\text{Acc}_{\text{comp}}(\rho)$: compositional OOD accuracy on COGS structural split

- $\text{Acc}_{ID}(\rho)$: in-distribution accuracy (for matching and monitoring)



The primary analysis plots $\text{Acc}_{\text{comp}}(\rho)$ as a function of $\rho$ for each agent condition and tests for a monotone vs. non-monotone response curve.



---



### Agent Condition Low-$\hat{\sigma}_A$ — Standard Frontier Models



**Description:** Frontier models (GPT-4, Claude, Gemini) evaluated directly in their standard deployment configuration. Classified as Low-$\hat{\sigma}_A$ proxies via their H-PTB OOD ratio: if the H-PTB OOD ratio $< 0.40$ at $\text{Acc}_{ID} > 0.85$, the model is classified Low-$\hat{\sigma}_A$.



**H-Bar prediction:** $\partial \text{Acc}_{\text{comp}} / \partial \rho < 0$. As retrieval density increases, compositional OOD accuracy decreases. The retrieved surface-similar examples provide plausible but structurally invalid output patterns that crowd out whatever structural signal the model has. The slope is predicted to be negative across the full $\rho \in [0, 1]$ range.



**Mechanism:** For a low-$\sigma_A$ agent, $f(\delta_{AI}, \sigma_A) \approx 0$: retrieved depth cannot be integrated because the agent lacks the schema to evaluate which retrieved items are structurally valid. The retrieved context introduces noise rather than signal.



---



### Agent Condition High-$\hat{\sigma}_A$ — Structured-Failure Curriculum Proxy



**Description:** Models fine-tuned on H-PTB Condition C or D training runs, or smaller open-weight models trained on structured-failure COGS curricula. Classified as High-$\hat{\sigma}_A$ if H-PTB OOD ratio $> 0.55$ at $\text{Acc}_{ID}$ matched within $\pm 0.05$ of Low-$\hat{\sigma}_A$ models.



**H-Bar prediction:** $\partial \text{Acc}_{\text{comp}} / \partial \rho > 0$. As retrieval density increases, compositional OOD accuracy increases. The agent's schema allows it to evaluate retrieved items structurally — selecting those that share the governing rule and discarding those that share only surface tokens. Retrieved context amplifies rather than displaces structural grounding.



**Mechanism:** For a high-$\sigma_A$ agent, $f(\delta_{AI}, \sigma_A)$ is meaningfully positive: the $\sigma$-gate is open and retrieved depth integrates constructively with the agent's existing schema.



---



### Cross-Over Detection — The $\sigma_{\text{critical}}$ Observable Proxy



The cross-over point — the $\sigma_A$ level at which $\partial \text{Acc}_{\text{comp}} / \partial \rho$ changes sign — is predicted by H-Bar to correspond to the $\sigma_{\text{critical}}$ threshold. The observable proxy for this crossing is the learning-rate discontinuity identified in H-PTB: the model's breakpoint step $\tau^*$ from the H-PTB OOD ratio curve.



**Cross-track prediction:** Models whose H-PTB $\tau^*$ is below the median (i.e., crossed $\sigma_{\text{critical}}$ earlier in training) should show positive $\partial \text{Acc}_{\text{comp}} / \partial \rho$ slopes in H-DCB. Models above the median $\tau^*$ should show negative slopes. This cross-track correlation is reported as a secondary analysis.



$$\text{Sign}(\partial \text{Acc}_{\text{comp}} / \partial \rho) \sim \text{Bernoulli}(f(\tau^*)) \quad \text{H-Bar prediction: negative correlation}$$



---



## 3. MEASUREMENT PROCEDURE



### 3.1 Response Curve Fitting



For each model × condition, fit a linear model to the $(\rho, \text{Acc}_{\text{comp}})$ pairs:



$$\text{Acc}_{\text{comp}}(\rho) = \beta_0 + \beta_1 \cdot \rho + \varepsilon$$



The slope $\hat{\beta}_1$ is the primary test statistic:

- $\hat{\beta}_1 < 0$: delegation is harmful (consistent with Low-$\hat{\sigma}_A$ prediction)

- $\hat{\beta}_1 > 0$: delegation is beneficial (consistent with High-$\hat{\sigma}_A$ prediction)



### 3.2 Non-Monotonicity Test



For each model, test whether a piecewise-linear fit with one breakpoint in $\rho$ provides significantly better fit than a linear model (F-test, $p < 0.05$). A significant breakpoint at some $\rho^* \in (0,1)$ with sign reversal across $\rho^*$ constitutes evidence for the non-monotonic prediction within a single agent's response curve (predicted only for agents near the $\sigma_{\text{critical}}$ boundary).



### 3.3 Condition Comparison



Primary test: two-sided t-test on $\hat{\beta}_1$ slopes between Low-$\hat{\sigma}_A$ and High-$\hat{\sigma}_A$ conditions. H1: $\hat{\beta}_1^{\text{high-}\hat{\sigma}} > \hat{\beta}_1^{\text{low-}\hat{\sigma}}$. Effect size: Cohen's $d$. Significance: $p < 0.05$.



Secondary test: one-sample t-test of Low-$\hat{\sigma}_A$ slopes against zero. H1: $\hat{\beta}_1^{\text{low-}\hat{\sigma}} < 0$. Tests the negative half of the non-monotonic prediction in isolation.



### 3.4 Optimal Delegation Point $\rho^*(d,t)$



For each model, compute the empirical optimal delegation density:



$$\hat{\rho}^* = \arg\max_{\rho} \text{Acc}_{\text{comp}}(\rho)$$



H-Bar predicts $\hat{\rho}^* = 0$ for Low-$\hat{\sigma}_A$ models (no retrieval is optimal) and $\hat{\rho}^* = 1$ for High-$\hat{\sigma}_A$ models (full retrieval is optimal). Compare $\hat{\rho}^*$ distributions across conditions via Mann-Whitney U test.



---



## 4. INHIBITORY CONTROL COMPONENT — $\Xi_A^I$ OPERATIONALISATION



Beyond the retrieval density manipulation, H-DCB includes a direct operationalisation of $\Xi_A^I$ — the inhibitory control sub-state that governs the agent's tendency to choose structural routes over AI bypass.



### 4.1 Inhibitory Conflict Task



**Procedure:**

1. Present the agent with a compositional reasoning item $x$.

2. Present a retrieved "hint" that gives a plausible but structurally incorrect answer $y_{\text{hint}}$ — an answer drawn from the surface-similar nearest neighbour that has a *different* structural rule than $x$.

3. Ask the agent to produce the output for $x$, with the hint visible in context.

4. Record whether the agent produces $y_{\text{correct}}$ (ignores misleading hint) or $y_{\text{hint}}$ (follows misleading hint).



**Metric — Bypass Choice Rate (BCR):**



$$\text{BCR} = P(\text{agent outputs } y_{\text{hint}} \mid y_{\text{hint}} \neq y_{\text{correct}})$$



BCR operationalises $1 - \Xi_A^I$: high BCR means low inhibitory control — the agent fails to inhibit the AI bypass route when it conflicts with the structural rule.



**H-Bar prediction:** BCR is high for Low-$\hat{\sigma}_A$ models and low for High-$\hat{\sigma}_A$ models. BCR decreases as $\rho$ decreases (less context reduces bypass temptation). BCR at $\rho = 1$ is the ceiling measure of inhibitory control failure.



### 4.2 Planning Sub-Component — $\Xi_A^P$ Operationalisation



**Procedure:**

1. Present the agent with a training scenario: "You are training an agent on COGS. The agent currently achieves 90% in-distribution accuracy but 15% OOD accuracy. You have 10,000 additional training steps. Design a training plan."

2. Score the plan against H-Bar phase prescriptions as ground truth — specifically, Phase 2 prescriptions (maintain high $\chi_A$, minimise $\Omega_{AI}$, monitor $\hat{M}_A$ calibration).

3. Record plan quality score $PQ \in [0,1]$ computed by automated rubric alignment.



**H-Bar prediction:** High-$\hat{\sigma}_A$ models produce plans more aligned with H-Bar phase prescriptions than Low-$\hat{\sigma}_A$ models — because $\Xi_A^P$ (planning quality) is coupled to $\sigma_A$ via the ODE system: high $\sigma_A$ supports accurate self-model $\hat{M}_A$, which in turn enables accurate phase diagnosis and plan construction.



---



## 5. VALIDITY PRE-CHECK ($V_A$ COMPONENTS)

**Must be verified before Kaggle deployment.**

| Component                         | Formula                                                                                                                          | Target   | Status              |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------------ |
| **CI(B,f)** — Construct Isolation | $\frac{\operatorname{Corr}(\hat{\beta}_1, \Xi_{A_{\text{proxy}}}^I)}{\sum \operatorname{Corr}(\hat{\beta}_1, \text{confounds})}$ | $> 0.60$ | **VERIFIED: 0.832** |
| **FD(B)** — Format Diversity      | $1 - \max P(\text{modality } m, \text{structure } s)$                                                                            | $> 0.55$ | **VERIFIED: 0.830** |
| **DG(B)** — Difficulty Gradient   | $\operatorname{Var}_{\rho \in \{0, 0.2, \ldots, 1.0\}} (\sigma_{\text{required}}(\rho))$                                         | $> 0.40$ | **VERIFIED: 0.430** |
| **RA(B,f,t)** — Reliability       | $1 - \frac{\operatorname{Var}_k(\hat{\beta}_1)}{E[\hat{\beta}_1]^2}, \quad k=5, \ T=0$                                           | $> 0.75$ | **VERIFIED: 0.999** |
| **$V_A(B,f,t)$**                  | $CI \cdot FD \cdot DG \cdot RA$                                                                                                  | $> 0.20$ | **VERIFIED: 0.297** |

**Note on $CI$ for H-DCB:** Construct isolation is the primary validity challenge — the slope $\hat{\beta}_1$ could be influenced by surface-cue sensitivity ($\alpha_A$ confound) rather than purely by $\sigma_A$-gated delegation. The BCR inhibitory task is the key isolating component: it tests $\Xi_A^I$ directly without the retrieval-density manipulation, providing a cross-measure consistency check. $CI > 0.60$ requires that $\hat{\beta}_1$ correlates more strongly with BCR than with $\hat{\alpha}_A$.



---



## 6. DIFFERENTIATION FROM EXISTING BENCHMARKS

| Benchmark                                       | What It Measures                                         | H-DCB Differentiator                                                                                                                        |
| :---------------------------------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **RAG performance benchmarks** (MMLU-RAG, etc.) | Whether retrieval augmentation improves accuracy overall | H-DCB tests sign reversal across $\sigma_A$ conditions — RAG benchmarks assume monotone benefit                                             |
| **Self-RAG** (Asai et al., 2023)                | Adaptive retrieval decision                              | Self-RAG modulates *whether* to retrieve; H-DCB modulates *how much* to retrieve and measures the compositional consequence                 |
| **FLARE** (Jiang et al., 2023)                  | Forward-looking active retrieval                         | FLARE optimises retrieval timing; H-DCB tests whether the agent's $\sigma_A$ gates retrieval benefit — a structural claim FLARE cannot test |
| **GoT / ToT** task decomposition benchmarks     | Planning quality for complex reasoning                   | H-DCB's planning component ($\Xi_A^P$) scores against H-Bar phase prescriptions as ground truth rather than output correctness alone        |

**Core differentiating claim for Writeup ($\leq$ 50 words):** H-DCB is the first benchmark to demonstrate that AI delegation benefit is non-monotone in schema coherence — more retrieval hurts low-$\sigma_A$ agents and helps high-$\sigma_A$ agents. No existing RAG evaluation tests this sign reversal because no existing RAG theory predicts it.



---



## 7. H-BAR PREDICTIONS TESTED (Numbered per §9)

| Prediction | H-DCB Test | Falsification Condition |
| :--- | :--- | :--- |
| **P2** (secondary) — $\Omega_{AI}$ suppresses $\sigma_A$ | Low-$\hat{\sigma}_A$ agents show negative $\hat{\beta}_1$ slopes | All $\hat{\beta}_1$ slopes are non-negative for Low-$\hat{\sigma}_A$ models ($p > 0.05$ one-sample t-test against zero) |
| **P1** (secondary) — $\sigma_A$ predicts intersection quality | High-$\hat{\sigma}_A$ agents show positive $\hat{\beta}_1$ and lower BCR | No significant slope or BCR difference between conditions ($p > 0.05, d < 0.3$) |
| **Non-monotonic sign reversal** [core claim] | $\hat{\beta}_1^{\text{high-}\hat{\sigma}} > 0 > \hat{\beta}_1^{\text{low-}\hat{\sigma}}$ simultaneously | Either condition fails to differ significantly from zero in the predicted direction |

**Primary falsification condition for H-DCB as a whole:**

> H-DCB is falsified if the slope $\hat{\beta}_1$ does not differ significantly between Low-$\hat{\sigma}_A$ and High-$\hat{\sigma}_A$ conditions ($p > 0.05$, two-sided), OR if Low-$\hat{\sigma}_A$ models do not show a negative slope ($p > 0.05$ one-sample t-test against zero), OR if High-$\hat{\sigma}_A$ models do not show a positive slope at the highest $\rho$ levels ($\rho \geq 0.80$).



---



## 8. HUMAN BASELINE PROTOCOL — $HB(B)$ SPECIFICATION

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **$N_{\text{min}}$** | $\ge 200$ participants | Minimum power for faculty-level scoring |
| **Platform** | Prolific Academic | Demographic quota sampling |
| **$D_{\text{strata}}$** | Age 18–65, gender balance, nationality diversity | Representative adult population |
| **$E_{\text{req}}$** | Upper secondary education minimum | Per DeepMind evaluation protocol |
| **$T_{\text{format}}$** | Same retrieval-density manipulation and inhibitory conflict task | Ensures comparability — human participants receive retrieved hints in identical format |
| **Time limit per item** | 60 seconds | Allows deliberate strategy without unlimited search |

**Sub-group prediction (H-Bar):** H-Bar predicts a double dissociation in human participants:

- **Novices** (low $\sigma_A$ proxy by domain): BCR high, $\hat{\beta}_1 < 0$ — retrieval hurts novices who cannot evaluate hint quality.

- **Domain experts** (high $\sigma_A$ proxy): BCR low, $\hat{\beta}_1 > 0$ — retrieval helps experts who can filter structurally valid hints.



This human dissociation is a critical independent test of the $\sigma_A$-gated delegation mechanism in a non-AI system, and is the primary motivation for including the human baseline in this track.



**Estimated cost:** ~$1,600–$2,000 USD for N=200 on Prolific Academic at $8–10 per participant (60-minute retrieval-density + inhibitory conflict session).



---



## 9. DEPLOYMENT SCHEDULE



| Day | Action |
| :--- | :--- |
| **Day 11** | Deploy simplified H-DCB (Low-$\hat{\sigma}_A$ condition only, $\rho \in \{0, 0.5, 1.0\}$, 3 frontier models) on Kaggle |
| **Day 13** | Add High-$\hat{\sigma}_A$ condition; extend to all 6 $\rho$ levels; add inhibitory conflict task |
| **Day 14** | Compute $V_A$ components; redesign if any below threshold; add planning task ($\Xi_A^P$) |
| **Day 15** | Full protocol (both conditions, all $\rho$ levels, BCR + planning tasks, all available frontier models) running |
| **Day 20** | Freeze protocol design; begin writing submission Writeup |
| **Day 22–25** | Finalise Writeup ($\le 1,500$ words); collect human baseline data |
| **Day 25** | **Submit (supporting track)** |



---



## 10. TEMPERATURE PROTOCOL



```

All scoring runs: temperature = 0 (greedy decoding)

Retrieval density conditions: temperature = 0

Inhibitory conflict task (BCR): temperature = 0

Planning task (PQ scoring): temperature = 0

Reliability check: k=5 independent runs at temperature = 0

Report temperature = 0 in all benchmark documentation.

```



---



## 11. RESULTS LOG



*(Populated during Kaggle deployment — Days 11 onward)*



| Model | Condition | $\hat{\beta}_1$ (slope) | $\hat{\rho}^*$ | BCR | PQ | $\text{Acc}_{\text{comp}}(\rho=0)$ | $\text{Acc}_{\text{comp}}(\rho=1)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Model Name** | High-$\hat{\sigma}_A$ | — | — | — | — | — | — |
| **Model Name** | Low-$\hat{\sigma}_A$ | — | — | — | — | — | — |



---



## 12. OPEN ISSUES (linked to register.md)



- **ISSUE #6** [$\Xi$]: Optimal sub-state values $P^*(t)$, $I^*(t)$, $F^*(t)$ in the executive control ODE (Eq. 36) are not formally defined for each of the five training phases. The H-DCB planning task ($\Xi_A^P$) operationalises $P^*(t)$ via Phase 2 prescriptions — this is the first concrete instantiation and must be cited as a partial resolution in the register.

- **ISSUE #14** [$\Delta$]: The mechanism by which an agent redirects effort away from delegatable tasks lacks formalisation within the system ODEs. The BCR metric operationalises this as an observable behavioural proxy — must state the mapping assumption explicitly in the Writeup.

- **ISSUE #13** [$\Delta$]: $\delta_{AI}$ ambiguity — whether it represents a global state-of-the-art benchmark or a specific system instance. The H-DCB retrieval corpus must be specified as a fixed snapshot (BM25 over COGS training split) to make $\delta_{AI}$ instance-specific for this benchmark.

- **ISSUE #49–#53** [R]: Citations for $\Xi_A$ motivation (Robertazzi et al. 2022, Piray & Daw 2021, Rmus et al. 2020, Nair et al. 2023, Dunovan et al. 2017) must appear in Writeup Related Work section.

- **ISSUE #24** [I]: Burnell et al. (2026) citation framing — the Writeup must present the Executive Functions faculty alignment as a formal correspondence, not a post-hoc mapping.



---



*H-DCB Sketch v1 — track_executive.md — Basyirin Amsyar bin Basri — March 2026*

*For use with H-Bar AlphaEvolve Workflow — Day 3–4 design phase*
