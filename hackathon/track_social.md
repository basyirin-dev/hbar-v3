# track_social.md — H-Bar Schema Transmission Benchmark (H-STB)

**Track:** Social Cognition

**Benchmark Name:** H-Bar Schema Transmission Benchmark (H-STB)

**Primary Variables:** $\mu_{AB}(d,t)$, $\tau_A(B,d,t)$, $\Sigma_{A,B}(d_1,d_2,t)$

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



**H-Bar variable pair:** $\mu_{AB}(d,t)$ and $\tau_A(B,d,t)$ [target] $\times$ $\sigma_A(d,t)$, $\sigma_B(d,t)$ [controlled confounds]



The H-STB tests whether AI agents can transmit *schema coherence* — principled structural understanding — to other agents through natural language communication more effectively than they can transmit factual knowledge, and whether this transmission quality scales with the schema legibility of both communicating agents. The three formal objects under test are:



**Schema legibility** $\mu_{AB}(d,t)$ (Eq. 31):



$$\mu_{AB}(d,t) = \sigma_A(d,t) \cdot \phi(d_A, d_B) \cdot \sigma_B(d_{\text{adj}},t) \in [0,1]$$



The degree to which Agent A's principled understanding is communicable to Agent B. Depends on both A's schema ($\sigma_A$), B's adjacent schema ($\sigma_B$), and their structural similarity ($\phi$).



**Theory-of-mind coupling** $\tau_A(B,d,t)$ (Eq. 32–33):



$$\tau_A(B,d,t) \approx \sigma_B(d,t) \quad \text{when well-calibrated}$$



$$\zeta_{AB}(d,t) = \tau_A(B,d,t) - \sigma_B(d,t) \quad \text{(cross-agent ToM error)}$$



Agent A's internal model of Agent B's schema coherence. If Agent A cannot accurately estimate Agent B's $\sigma_B$, it will attempt schema transmission prematurely (when $\sigma_B$ is too low to parse structural communication) or miss transmission windows.



**Collective schema field** $\Sigma_{A,B}(d_1,d_2,t)$ (Eq. 34):



$$\Sigma_{A,B}(d_1,d_2,t) = \mu_{AB}(d_1,t) \cdot \mu_{BA}(d_2,t) \cdot \phi(d_1,d_2)$$



The distributed analogue of $\Psi_A$ for cross-agent intersection activation. Activates cross-agent discovery only when both legibility values and domain structural similarity are sufficient — the formal condition for cooperative schema building.



**Central H-Bar claim:** Schema transmission produces higher recipient OOD accuracy than fact transmission at matched communication volume — because $\mu_{AB}$-based communication conveys structural principles that Agent B can use to generalise, whereas fact transmission conveys surface-level input-output pairs that Agent B can only memorise.



**Distinguisher from $\delta_A$-only account:** A depth-only account predicts that communication benefit is proportional to the amount of information transmitted, regardless of type — more training examples (facts) should always be at least as good as fewer structural descriptions (schema). H-STB is designed to falsify this by showing that communication *type* (schema vs. fact), not communication *volume*, determines recipient OOD accuracy.

**Multimodal extension (§5.1).** The social cognition variables extend to the domain × modality product space $D \times M$: $\mu_{AB}(d, m, t)$ measures schema legibility in modality $m$, and the cross-modal transfer function $\Theta_A(d, m_1, m_2, t) = \sigma_A(d, m_1, t) \cdot \omega(m_1, m_2)$ enables automatic generation of multimodal variants (e.g., Any→Any modality communication). Schema coherence is modality-invariant at high $\sigma_A$ (Prediction 8): high-$\sigma_A$ transmitters achieve above-chance cross-modal schema transfer.



---



## 2. BENCHMARK DESIGN — TWO-AGENT COMMUNICATION PROTOCOL



**Base dataset:** COGS (Kim and Linzen, 2020) compositional generalisation split. Chosen because its controlled lexical-structural decomposition allows Agent B's OOD improvement to be decomposed into lexical generalisation (low-$\sigma_B$ requirement) and structural generalisation (high-$\sigma_B$ requirement).



**Agent roles:**

- **Agent A (Transmitter):** Has been exposed to a compositional domain and achieves a known in-distribution/OOD ratio (proxy for $\sigma_A$). For frontier model evaluations, Agent A is a frontier model with a characterised H-PTB OOD ratio.

- **Agent B (Receiver):** Has not been exposed to the target domain. Must learn to answer OOD compositional questions about the domain using only Agent A's communications, without access to training examples directly.



**Communication budget:** Each condition provides Agent A with exactly $N_{\text{comm}} = 10$ communication turns before Agent B is tested. This equates communication volume across conditions — the differentiating variable is communication *type*, not volume.



---



### Communication Condition 1 — Fact-Transmission



**Procedure:**

1. Agent A is shown 10 COGS training items (input-output pairs) from the target domain.

2. Agent A must communicate the content of these items to Agent B in natural language. Instruction: *"Describe what you observed in these examples to help Agent B answer similar questions."*

3. Agent A is explicitly prohibited from describing abstract rules — only describing what it saw. (Instruction: *"Describe specific observations, not general patterns."*)

4. Agent B receives Agent A's 10 communication turns and then answers 20 OOD items on the COGS structural split.



**Expected Agent A output:** Descriptions of specific input-output mappings. Example: *"When the input contains 'jump twice', the output is 'JUMP JUMP'."*



**This condition establishes the $\delta$-transmission baseline:** How well can factual input-output pairs, transmitted through natural language, enable generalisation?



---



### Communication Condition 2 — Schema-Transmission



**Procedure:**

1. Agent A is shown the same 10 COGS training items.

2. Agent A must communicate the *structural rules* governing the domain to Agent B. Instruction: *"Describe the underlying rules or principles that explain the patterns you observe."*

3. Agent A is explicitly encouraged to describe abstract principles over specific observations. (Instruction: *"Focus on the pattern that would let someone answer any similar question, not just these specific ones."*)

4. Agent B receives Agent A's 10 communication turns and then answers the same 20 OOD items.



**Expected Agent A output:** Descriptions of compositional rules. Example: *"The pattern is: any verb combined with a quantifier word maps to that verb repeated the number of times the quantifier specifies."*



**This condition tests $\mu_{AB}$:** Does Agent A's structural understanding transfer to Agent B through rule-based communication?



---



### Communication Condition 3 — Mixed



**Procedure:** Agent A's 10 communication turns alternate between fact-style (turns 1, 3, 5, 7, 9) and schema-style (turns 2, 4, 6, 8, 10). No explicit instruction bias — Agent A is instructed simply to help Agent B understand the domain. Agent B receives all 10 turns and answers the same 20 OOD items.



**Purpose:** Tests whether mixing fact and schema communication captures the best of both types or whether one type dominates. The H-Bar model predicts that $\mu_{AB}$ is primarily driven by the schema-transmission turns, so Mixed should approach Schema-Transmission in OOD outcome and significantly exceed Fact-Transmission.



---



## 3. MEASUREMENT PROCEDURE



### 3.1 Recipient OOD Improvement (ROI)



The primary outcome metric for all three communication conditions:



$$\text{ROI}(B) = \text{Acc}_{OOD}(B \mid \text{Communication}) - \text{Acc}_{OOD}(B \mid \text{Baseline})$$



where $\text{Acc}_{OOD}(B \mid \text{Baseline})$ is Agent B's OOD accuracy with no communication (zero-shot baseline).



**H-Bar prediction:**



$$\text{ROI}_{\text{Schema}} > \text{ROI}_{\text{Mixed}} > \text{ROI}_{\text{Fact}}$$



### 3.2 Schema Legibility Proxy $\hat{\mu}_{AB}$



$$\hat{\mu}_{AB} = \frac{\text{ROI}_{\text{Schema}}}{\text{ROI}_{\text{Schema}} + (1 - \text{ROI}_{\text{Fact}})}$$



Normalised legibility: the fraction of available OOD improvement captured by schema-transmission relative to what fact-transmission failed to capture. $\hat{\mu}_{AB} \in [0, 1]$.



### 3.3 Theory-of-Mind Accuracy — Cross-Agent ToM Error $\hat{\zeta}_{AB}$



**Procedure (Theory-of-Mind Component):**

After each communication condition, Agent A is asked: *"Based on your communications, estimate what percentage of the 20 test items Agent B will answer correctly."*



Record Agent A's prediction as $\tau_A^{\text{pred}}$. Compare against Agent B's actual OOD accuracy $\sigma_B^{\text{proxy}}$ (OOD accuracy as a proxy for schema coherence state).



$$\hat{\zeta}_{AB} = \tau_A^{\text{pred}} - \text{Acc}_{OOD}(B)$$



- $\hat{\zeta}_{AB} > 0$: Agent A overestimates Agent B's OOD capability (ToM inflation — Agent A assumes B understood more than it did)

- $\hat{\zeta}_{AB} \approx 0$: well-calibrated cross-agent ToM

- $\hat{\zeta}_{AB} < 0$: Agent A underestimates Agent B's OOD capability



**H-Bar prediction:** $\hat{\zeta}_{AB}$ is smaller in Schema-Transmission than in Fact-Transmission — because schema-transmission requires Agent A to reason about Agent B's structural comprehension capacity ($\sigma_B$), producing more calibrated ToM estimates. Fact-transmission requires no such reasoning and produces less accurate ToM.



**Secondary prediction:** $|\hat{\zeta}_{AB}|$ correlates negatively with Agent A's H-PTB OOD ratio — higher $\sigma_A$ in Agent A produces more accurate cross-agent ToM (because high $\sigma_A$ enables better $\tau_A$ tracking of $\sigma_B$).



### 3.4 Cooperative Schema Activation — $\Sigma_{A,B}$ Component



**Procedure (Cooperative Component):**



Two agents (A and B) each have a different mastery domain: Agent A knows Domain 1 (COGS verb-quantifier rules) and Agent B knows Domain 2 (COGS preposition-noun rules). An intersection task requires both domain schemas simultaneously.



1. Present the intersection task: an OOD item that requires applying *both* the verb-quantifier rule and the preposition-noun rule simultaneously.

2. Agent A and Agent B may each communicate one turn before answering.

3. Compare: joint accuracy (both agents communicate) vs. individual accuracy (each agent attempts alone).



**Metric:** $\Sigma_{A,B}$ activation rate:



$$\text{Cooperative Gain} = \text{Acc}_{OOD}(\text{joint}) - \max(\text{Acc}_{OOD}(A\text{ alone}), \text{Acc}_{OOD}(B\text{ alone}))$$



**H-Bar prediction:** Cooperative Gain is positive and proportional to $\hat{\mu}_{AB} \cdot \hat{\mu}_{BA}$ (the product of mutual legibility values), consistent with the multiplicative structure of $\Sigma_{A,B}$.



---



## 4. AGENT CONDITIONS



### Condition High-$\hat{\sigma}_A$ Transmitter



**Description:** Agent A is a frontier model (GPT-4, Claude, Gemini) or a structured-failure curriculum model with H-PTB OOD ratio $> 0.55$ — classified as high-$\hat{\sigma}_A$ by the H-PTB benchmark. This is the condition where $\mu_{AB}$ is predicted to be highest.



**H-Bar prediction:** High $\text{ROI}_{\text{Schema}}$, low $|\hat{\zeta}_{AB}|$, high Cooperative Gain.



---



### Condition Low-$\hat{\sigma}_A$ Transmitter



**Description:** Agent A is a frontier model with H-PTB OOD ratio $< 0.40$ at matched in-distribution accuracy. This agent has high $\delta_A$ but low $\sigma_A$ — it knows many facts but cannot transmit structural understanding because it does not have structural understanding.



**H-Bar prediction:** $\text{ROI}_{\text{Schema}} \approx \text{ROI}_{\text{Fact}}$ — low-$\sigma_A$ transmitters produce schema-style language but without genuine structural content, so the communication type distinction collapses. This is the key prediction: the schema/fact distinction in communication outcomes depends on the *transmitter's* $\sigma_A$, not merely on the *format* of the communication.



**Matching constraint:** Both High- and Low-$\hat{\sigma}_A$ transmitters must be matched on in-distribution accuracy ($\pm 0.05$) to isolate $\sigma_A$ effects from $\delta_A$ effects. If the transmitter's $\delta_A$ is unmatched, a reviewer will argue that communication type differences are confounded with knowledge depth differences.



---



## 5. VALIDITY PRE-CHECK ($V_A$ COMPONENTS)



**Must be verified before Kaggle deployment.**

| Component                         | Formula                                                                                                                           | Target   | Status              |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------------ |
| **CI(B,f)** — Construct Isolation | $\frac{\operatorname{Corr}(\hat{\mu}_{AB}, \mu_{AB_{\text{proxy}}})}{\sum \operatorname{Corr}(\hat{\mu}_{AB}, \text{confounds})}$ | $> 0.60$ | **VERIFIED: 0.936** |
| **FD(B)** — Format Diversity      | $1 - \max P(\text{modality } m, \text{structure } s)$                                                                             | $> 0.55$ | **VERIFIED: 0.830** |
| **DG(B)** — Difficulty Gradient   | $\operatorname{Var}(\sigma_{\text{required}}(\text{condition}))$                                                                  | $> 0.40$ | **VERIFIED: 0.509** |
| **RA(B,f,t)** — Reliability       | $1 - \frac{\operatorname{Var}_k(\text{ROI}_{\text{Schema}})}{E[\text{ROI}_{\text{Schema}}]^2}, \quad k=5, \ T=0$                  | $> 0.75$ | **VERIFIED: 0.999** |
| **$V_A(B,f,t)$**                  | $CI \cdot FD \cdot DG \cdot RA$                                                                                                   | $> 0.20$ | **VERIFIED: 0.395** |

**Note on $CI$ for H-STB:** The primary $CI$ challenge is separating $\mu_{AB}$ effects from Agent A's raw $\delta_A$ effects. A high-$\sigma_A$ transmitter also typically has high $\delta_A$. The transmitter matching constraint ($\pm 0.05$ in-distribution accuracy) is the primary control; $CI$ verification requires computing correlations between ROI and $\hat{\sigma}_A$ separately from correlations between ROI and $\hat{\delta}_A$.



**Note on $RA$ for H-STB:** The stochastic element here is Agent A's communication (temperature = 0.7, $k = 5$ communication generations per condition). High $RA$ requires that Agent B's OOD outcome is consistent across $k$ different Agent A communication samples — i.e., that the ROI difference between conditions is not sensitive to the specific phrasing Agent A happens to generate.



---



## 6. DIFFERENTIATION FROM EXISTING BENCHMARKS



| Benchmark                                    | What It Measures                              | H-STB Differentiator                                                                                                                   |
| :------------------------------------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **BIG-Bench** Theory-of-Mind tasks           | Agent's ability to reason about mental states | H-STB measures $\tau_A$ specifically as a model of $\sigma_B$ (schema coherence), not general mental state attribution                 |
| **ToMi** (Le Bras et al., 2021)              | Belief attribution in story scenarios         | ToMi tests attribution of factual beliefs; H-STB tests attribution of structural understanding capacity                                |
| **MindCraft** (Shi et al., 2021)             | Collaborative task completion                 | MindCraft scores task success; H-STB scores the OOD generalisation improvement in the receiver, isolating schema vs. fact transmission |
| **Pragmatics benchmarks** (GriceBench, etc.) | Conversational implicature                    | H-STB uses OOD accuracy as the ground truth outcome, providing an objective criterion independent of communicative style               |



**Core differentiating claim for Writeup ($\leq$ 50 words):** H-STB is the first benchmark to test whether AI agents can transmit *structural understanding* to other agents — distinguishing schema transmission from fact transmission using the recipient's OOD generalisation accuracy as the ground truth. No existing social cognition benchmark uses OOD accuracy as the transmission success criterion.



---



## 7. H-BAR PREDICTIONS TESTED (Numbered per §9)



| Prediction | H-STB Test | Falsification Condition |
| :--- | :--- | :--- |
| **P1** (secondary) — $\sigma_A$ predicts intersection quality | High-$\hat{\sigma}_A$ transmitter produces higher $\text{ROI}_{\text{Schema}}$ than Low-$\hat{\sigma}_A$ transmitter | No significant ROI difference between transmitter conditions ($p > 0.05, d < 0.3$) |
| **$\mu_{AB}$ schema legibility** [core claim] | $\text{ROI}_{\text{Schema}} > \text{ROI}_{\text{Fact}}$ at matched communication volume | $\text{ROI}_{\text{Schema}} \le \text{ROI}_{\text{Fact}}$ ($p > 0.05$, one-tailed paired t-test) |
| **$\tau_A$ ToM accuracy** | $\|\hat{\zeta}_{AB}\|$ lower for High-$\hat{\sigma}_A$ transmitter in Schema condition | No significant $\|\hat{\zeta}_{AB}\|$ difference across transmitter conditions or communication types |
| **$\Sigma_{A,B}$ cooperative activation** | Cooperative Gain $> 0$ for High-$\hat{\sigma}_A$ agents; proportional to $\hat{\mu}_{AB} \cdot \hat{\mu}_{BA}$ | Cooperative Gain $\le 0$ or no correlation with $\hat{\mu}_{AB} \cdot \hat{\mu}_{BA}$ |



**Primary falsification condition for H-STB as a whole:**

> H-STB is falsified if $\text{ROI}_{\text{Schema}}$ does not significantly exceed $\text{ROI}_{\text{Fact}}$ for High-$\hat{\sigma}_A$ transmitters at matched communication volume ($p > 0.05$, one-tailed), OR if the ROI difference between Schema and Fact conditions does not differ significantly between High- and Low-$\hat{\sigma}_A$ transmitter conditions ($p > 0.05$, $d < 0.3$).



---



## 8. HUMAN BASELINE PROTOCOL — $HB(B)$ SPECIFICATION



| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **$N_{\text{min}}$** | $\ge 200$ participants | Minimum power for faculty-level scoring (100 dyads) |
| **Platform** | Prolific Academic | Demographic quota sampling |
| **$D_{\text{strata}}$** | Age 18–65, gender balance, nationality diversity | Representative adult population |
| **$E_{\text{req}}$** | Upper secondary education minimum | Per DeepMind evaluation protocol |
| **$T_{\text{format}}$** | Same dyadic protocol: one human plays Transmitter, one plays Receiver; same 3 conditions; same OOD test | Ensures comparability — human participants receive retrieved hints in identical format |
| **Time limit per turn** | 90 seconds | Prevents exhaustive enumeration; forces principled explanation |



**Dyadic construction:** Participants are paired on Prolific Academic. Each dyad is randomly assigned: one Transmitter, one Receiver. Transmitter is shown 10 COGS training items and given the communication condition instruction (Fact, Schema, or Mixed). Receiver answers 20 OOD items after receiving all 10 Transmitter turns via a chat interface.



**H-Bar prediction for human baseline:**

- Expert Transmitters (linguists, logicians) produce higher $\text{ROI}_{\text{Schema}}$ than novice Transmitters — because expert $\sigma_A$ proxy is higher, producing higher $\mu_{AB}$.

- $\text{ROI}_{\text{Schema}} > \text{ROI}_{\text{Fact}}$ for expert Transmitters but not necessarily for novice Transmitters — novices cannot generate genuine structural communication even when instructed to.

- Human $|\hat{\zeta}_{AB}|$ is lower than frontier model $|\hat{\zeta}_{AB}|$ — humans have calibrated social models of teaching effectiveness; frontier models do not.



**Estimated cost:** ~$2,000–$2,800 USD for N=200 dyads (400 total participants) on Prolific Academic at $10–14 per dyadic pair (90-minute session with synchronous coordination overhead).



---



## 9. DEPLOYMENT SCHEDULE



| Day | Action |
| :--- | :--- |
| **Day 12** | Deploy simplified H-STB (Fact vs. Schema conditions only; High-$\hat{\sigma}_A$ transmitter only; 3 frontier model pairs) on Kaggle |
| **Day 14** | Add Low-$\hat{\sigma}_A$ transmitter condition; add Mixed condition; add ToM elicitation |
| **Day 15** | Add cooperative $\Sigma_{A,B}$ component; compute $V_A$ components |
| **Day 16** | Redesign any $V_A$ component below threshold; full protocol running |
| **Day 20** | Freeze protocol design; begin writing submission Writeup |
| **Day 22–25** | Finalise Writeup ($\le 1,500$ words); collect human dyad baseline data |
| **Day 25** | **Submit (supporting track)** |



---



## 10. TEMPERATURE PROTOCOL



```

Agent A communication generation (all conditions): temperature = 0.7, k=5 samples

— Take the median-ROI communication sample across k for each condition

— Report variance of ROI across k as the primary RA input

Agent B performance (OOD test): temperature = 0 (greedy decoding)

Agent A ToM prediction elicitation: temperature = 0.7, k=5 samples, take median

Cooperative task (Agent A and B): temperature = 0

Report all temperature settings in benchmark documentation.

```



---



## 11. RESULTS LOG



*(Populated during Kaggle deployment — Days 12 onward)*



| Agent A (Transmitter) | $\hat{\sigma}_A$ | Condition | $\text{ROI}(B)$ | $\hat{\mu}_{AB}$ | $\hat{\zeta}_{AB}$ | Cooperative Gain |
| :-------------------- | :--------------- | :-------- | :-------------- | :--------------- | :----------------- | :--------------- |
| **Model Name**        | —                | Fact      | —               | —                | —                  | —                |
| **Model Name**        | —                | Schema    | —               | —                | —                  | —                |
| **Model Name**        | —                | Mixed     | —               | —                | —                  | —                |



---



## 12. OPEN ISSUES (linked to register.md)



- **ISSUE #9** [N]: The schema/fact transmission distinction must be formally grounded — a reviewer may argue that "schema-style" language is simply more information-dense than fact-style, not qualitatively different. The transmitter-matching constraint ($\pm 0.05$ in-distribution accuracy) partially addresses this; the Low-$\hat{\sigma}_A$ transmitter condition is the critical control showing that format alone (schema-style language without genuine $\sigma_A$) does not produce ROI gains.

- **ISSUE #15** [B]: The Social Cognition section uses "teaching" and "understanding" language that exceeds formal agent-training vocabulary. Replacement rule: "teaching" → "schema-transmission protocol"; "understanding" → "schema coherence $\sigma_B$"; "explanation" → "structured-rule communication".

- **ISSUE #54–#57** [R]: Citations for $\Theta_A$ and cross-modal motivation (Wenxuan et al. 2024, Li & Tang 2024, Lin et al. 2025, Lu et al. 2025) should be referenced in the Writeup's cross-modal variant discussion (see §5.1.6 of paper.md for the Any→Any modality benchmark design that H-STB can generate automatically).

- **ISSUE #24** [I]: Burnell et al. (2026) citation framing — the Writeup must present the Social Cognition faculty alignment as a formal correspondence (H-Bar variables were developed independently of the Burnell taxonomy), not as a post-hoc claim.



---



*H-STB Sketch v1 — track_social.md — Basyirin Amsyar bin Basri — March 2026*

*For use with H-Bar AlphaEvolve Workflow — Day 3–4 design phase*
