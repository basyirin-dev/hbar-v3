## Schema Coherence, Cognitive Faculty Evaluation, and Phase-Structured Curriculum Design for AI Agents

**Basyirin Amsyar bin Basri**
Independent Researcher · Petaling Jaya, Malaysia
basyirin.basri@gmail.com

**Version:** 3.0+ (Full Reconstruction)
**Status:** Preprint Draft
**Date:** March 2026

---

## Abstract

Current training pipelines optimise parametric depth $δ_A(d,t)$ without formally targeting schema coherence $σ_A(d,t)$ — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities. Empirical results on compositional generalisation benchmarks show that high-$δ$, low-$σ$ agents fail systematically on out-of-distribution recombination tasks that standard in-distribution metrics do not detect. No existing framework specifies the mechanisms by which $σ_A$ forms, what suppresses it, or how it interacts with attention, executive control, metacognitive self-modelling, collective schema communication, or cross-modal transfer.

We introduce the **H-Bar Model V3.0+**, a coupled dynamical-systems framework that:

1. Formalises $σ_A(d,t)$ as an independently necessary training variable with its own differential equation
2. Introduces **attentional fidelity** $α_A(d,t)$ as a fourth per-domain state variable gating schema growth
3. Introduces the **executive control state** $\Xi_A(t) = \{\Xi_A^P, \Xi_A^I, \Xi_A^F\}$ covering planning, inhibition, and cognitive flexibility
4. Introduces the **self-model of schema coherence** $\hat M_A(d,t)$ with calibration error $ζ_A(d,t)$ for metacognitive evaluation
5. Introduces the **collective schema field** $Σ_{A,B}(d_1,d_2,t)$ with schema legibility $μ_{AB}(d,t)$ and theory-of-mind coupling $τ_A(B,d,t)$ for social cognition
6. Extends all state variables to the **domain $×$ modality product space** $D×M$ via cross-modal schema transfer $Θ_A(d,m_1,m_2,t)$
7. Formalises **benchmark validity** $VA(B,f,t)$ with construct isolation $CI(B,f)$, format diversity $FD(B)$, difficulty gradient $DG(B)$, and reliability $RA(B,f,t)$
8. Derives a **five-phase training arc** indexed by ($δ_A^relative$, $σ_A$, $|M_A(t)|$) with measurable transition conditions
9. States **eight falsifiable predictions** distinguishable from $δ$-only accounts

The framework directly addresses five cognitive faculty gaps identified by Burnell et al. (2026) — Learning, Metacognition, Attention, Executive Functions, and Social Cognition — and generates executable benchmark families for each. If $σ_A$ is formally necessary and current training pipelines systematically suppress it, capable-agent training requires structural revision beyond scale and curriculum ordering alone.

---

## Table of Contents

1. [Introduction](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#1-introduction)
2. [Related Work and Gap Analysis](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#2-related-work-and-gap-analysis)
3. [The H-Bar Model — Core Framework V1.0](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#3-the-h-bar-model--core-framework-v10)
4. [V2.0 Extensions — Five New Cognitive Dimensions](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#4-v20-extensions--five-new-cognitive-dimensions)
5. [V3.0 Extensions — Multimodal Coverage and Benchmark Validity](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#5-v30-extensions--multimodal-coverage-and-benchmark-validity)
6. [V3.0+ Micro-Gap Closure — Reliability and Pre-Audit Protocol](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#6-v30-micro-gap-closure--reliability-and-pre-audit-protocol)
7. [Phase Structure](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#7-phase-structure)
8. [The H-Bar Benchmark Protocol](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#8-the-h-bar-benchmark-protocol)
9. [Eight Falsifiable Predictions](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#9-eight-falsifiable-predictions)
10. [Limitations and Future Work](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#10-limitations-and-future-work)
11. [Conclusion](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#11-conclusion)
12. [Mathematical Appendix](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#12-mathematical-appendix)
13. [References](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#13-references)

---

## 1. Introduction

The standard framing of systematic compositionality failure is precise and reproducible. Agents trained to high in-distribution accuracy on sequence and language tasks fail near-completely when test distributions require zero-shot recombination of primitives trained in isolation. Lake and Baroni (2018) demonstrated this on SCAN — seq2seq models achieve above 99% accuracy on random test splits and below 2% on the add-primitive split. The broader benchmark literature is consistent: COGS (Kim and Linzen, 2020) finds 96–99% in-distribution accuracy alongside 16–35% compositional generalisation accuracy; CFQ (Keysers et al., 2020) shows performance degradation growing monotonically with compound divergence; PCFG-SET (Hupkes et al., 2020) documents failures on productivity, systematicity, and substitutivity tests across RNNs, CNNs, and Transformers.

The structural argument follows directly. Current training pipelines have one formal optimisation target: minimise expected loss over the training distribution. This objective efficiently increases one variable — **parametric depth** $δ_A(d,t)$ — but has no formal mechanism for increasing a second, independent variable: **schema coherence** $σ_A(d,t)$, the degree to which representations are restructured around deep governing principles.

The H-Bar Model V1.0 formalised this asymmetry. V2.0 extended it to cover four additional cognitive faculties — Attention, Executive Functions, Metacognition, and Social Cognition — each with formal variables, ODEs, and benchmark generation protocols. V3.0 extended all variables to a domain × modality product space and formalised benchmark validity as a measurable object. V3.0+ adds a reliability function and three practical protocols that close the remaining measurement gaps.

### 1.1 Central Claim

> Training pipelines that optimise $δ_A(d,t)$ without formally targeting $σ_A(d,t)$ will systematically produce agents that pass in-distribution evaluation while failing out-of-distribution recombination — not because they lack depth, but because their training regimes suppress the schema crystallisation that converts parametric depth into principled generalisation capacity. Furthermore, the suppression mechanism extends to attentional allocation ($α_A$), executive control ($Ξ_A$), metacognitive self-modelling ($\hat M_A$), and inter-agent schema communication ($μ_{AB}$) — all of which interact multiplicatively with σA through the formal coupling terms derived below.

### 1.2 Cognitive Faculty Alignment

The framework addresses all five cognitive faculties named as evaluation gaps by Burnell et al. (2026):

| Faculty                 | Primary Variable                  | Mechanism                                             |
| ----------------------- | --------------------------------- | ----------------------------------------------------- |
| **Learning**            | $σ_A(d,t)$, $δ_A(d,t)$            | OOD gap as schema proxy; compositional generalisation |
| **Metacognition**       | $\hat M_A(d,t)$, $ζ_A(d,t)$       | Self-model accuracy; calibration error dynamics       |
| **Attention**           | $α_A(d,t)$, $CA(d,t)$             | Attentional fidelity to generative structure          |
| **Executive Functions** | $Ξ_A^P$, $Ξ_A^I$, $Ξ_A^F$         | Planning, inhibition, cognitive flexibility           |
| **Social Cognition**    | $μ_{AB}$, $τ_A(B,d,t)$, $Σ_{A,B}$ | Schema legibility, theory of mind, collective field   |

### 1.3 Score Trajectory

| Version   | Core Addition                                     | Hackathon Suitability | Winning Probability |
| --------- | ------------------------------------------------- | --------------------- | ------------------- |
| V1.0      | $σ_A$, $δ_A$, $Ψ_A$, $D^*$, 5-phase arc           | 52.47%                | 14.28%              |
| V2.0      | $α_A$, $\hat M_A$, $Ξ_A$, $μ_{AB}$, τA, $Σ_{A,B}$ | 97.85%                | 62.62%              |
| V3.0      | $Θ_A$, $ω(m_1,m_2)$, $VA$, $CI$, $FD$, $DG$       | 99.61%                | 70.89%              |
| **V3.0+** | **$RA$, $HB(B)$, pre-audit, $T=0$ protocol**      | **99.93%**            | **~73.41%**         |

---

## 2. Related Work and Gap Analysis

### 2.1 Curriculum Learning

Bengio et al. (2009) established the foundational result: easy-to-hard sample ordering improves generalisation by providing representational scaffolding. Subsequent work elaborated difficulty measurement (Kumar et al., 2010; Portelas et al., 2020; Narvekar et al., 2020) and pacing schedules. Every variant maximises the rate at which δA increases.

**Gap statement.** Curriculum learning provides training-sequence optimisation for depth growth rate but has no formal account of $σ_A(d,t)$ dynamics, no triggering conditions for schema crystallisation, and no prescription for the qualitative shift in training regime that σcritical-crossing requires. The H-Bar phase structure formalises all three.

### 2.2 Compositional Generalisation

The SCAN/COGS/CFQ/PCFG-SET benchmark family collectively documents the high-$δ_A$/low-$σ_A$ failure mode empirically. The consistent diagnosis: models encode statistical regularities rather than the compositional rules governing the distribution.

**Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise $σ_A$ as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

### 2.3 Continual Learning and Decay

McCloskey and Cohen (1989), Goodfellow et al. (2013), and Kirkpatrick et al. (2017) address parametric overwriting under sequential training. Every mitigation strategy targets preservation or recovery of parametric content.

**Gap statement.** The continual learning literature formally accounts for parametric decay $λ_c$ under sequential training but has no formal object for the domain frontier $∆(d,t)$ and no mechanism for representing frontier obsolescence $λ_f(d,t)$ as a distinct decay process with different intervention implications.

### 2.4 Causal and Structured Representation Learning

Schölkopf et al. (2021) establish that causal representations support OOD generalisation. Beukman et al. (2024) document seven structural prior incorporation patterns across four decomposability archetypes. Torresan and Baltieri (2024) distinguish weak from strong disentanglement.

**Gap statement.** Causal and structured representation learning specify the target state corresponding to high $σ_A(d,t)$ but do not formalise $σ_A$ as a dynamic scalar with its own ODE, do not model the training process that builds it or the AI bypass risk $Ω_{AI}(d,t)$ that suppresses it, and do not connect it to attentional allocation, executive control, metacognitive self-modelling, or collective schema communication.

### 2.5 Cognitive Evaluation of AI Systems

Burnell et al. (2026) propose a Cognitive Taxonomy of ten faculties and identify Learning, Metacognition, Attention, Executive Functions, and Social Cognition as having large evaluation coverage gaps. Chollet (2019) proposes ARC as a generalisation benchmark. Morris et al. (2024) establish a Levels of AGI framework.

**Gap statement.** Existing cognitive evaluation frameworks specify what should be measured but provide no formal theoretical grounding for why specific task designs isolate specific faculties. The H-Bar Benchmark Protocol (Section 8) provides that grounding by deriving benchmark designs directly from formal variable structures.

### 2.6 Synthesis — The Five-Gap Map

| Literature                   | H-Bar Variable Addressed       | H-Bar Variable Missing                               |
| ---------------------------- | ------------------------------ | ---------------------------------------------------- |
| Curriculum Learning          | $δ_A$ growth rate              | $σ_A$ dynamics, $α_A$, $Ξ_A$                         |
| Compositional Generalisation | $σ_A$ failure mode (empirical) | $σ_A$ formation mechanism, suppression               |
| Continual Learning           | $λ_c$ (parametric decay)       | $λ_f$ (frontier obsolescence), $σ_A$ coupling        |
| Causal/Structured Repr.      | $σ_A$ target state             | $σ_A$ developmental trajectory, $\hat M_A$, $μ_{AB}$ |
| Cognitive Evaluation         | Faculty identification         | Formal theoretical grounding for benchmark design    |

---

## 3. The H-Bar Model — Core Framework V1.0

### 3.1 The Three Core Knowledge Dimensions

Let every domain of knowledge be indexed by $d ∈ D$, where $D$ is the set of all knowledge domains. For a given agent $A$ at time $t$, three orthogonal quantities are tracked per domain.

#### 3.1.1 Depth $δ_A(d,t)$

The structural complexity and principled coherence of the agent's internal representation of domain $d$. Not raw parameter volume — the degree to which knowledge is organised around deep causal principles rather than surface-statistical features. Bounded above by the domain frontier $∆(d,t)$:
$$0 \leq \delta_A(d,t) \leq \Delta(d,t) \tag{1}$$

**Relative depth:**
$$\delta_A^{\text{relative}}(d,t) = \frac{\delta_A(d,t)}{\Delta(d,t)} \in [0,1] \tag{2}$$
#### 3.1.2 Breadth $β_A(d,t)$

The agent's functional competence in domain $d$ — sufficient to engage primary-domain artefacts — but without deep principled organisation. Qualitatively different from depth: more rapidly acquired, more rapidly lost, and increasingly AI-augmentable. No principled ceiling; approaches an asymptote of diminishing return.

#### 3.1.3 Schema Coherence $σ_A(d,t)$

The degree to which the agent's representation of domain d has been restructured around deep governing principles.
$$\sigma_A(d,t) \in [0, 1] \tag {3}$$
**Unique properties distinguishing $σ_A$ from adjacent constructs:**

| Property                                 | $σ_A$ | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
| ---------------------------------------- | ----- | ---------------- | ------------------ | ------------ | ---------------- |
| Continuous scalar ODE                    | ✓     | ✗                | ✗                  | ✗            | ✗                |
| Frontier-relative normalisation          | ✓     | ✗                | ✗                  | ✗            | ✗                |
| Evaluative function (AI error detection) | ✓     | ✗                | ✗                  | ✗            | ✗                |
| Multiplicative $Ψ_A$ coupling            | ✓     | ✗                | ✗                  | ✗            | ✗                |
| Decay coupling (slows $λ_c$)             | ✓     | ✗                | ✗                  | ✗            | ✗                |
| AI bypass risk $Ω_{AI}$ suppression      | ✓     | ✗                | ✗                  | ✗            | ✗                |
| Cross-modal transfer $Θ_A$               | ✓     | ✗                | ✗                  | ✗            | ✗                |

### 3.2 Mastery Set and Breadth Set
$$M_A(t) = \{d \in D : \delta_A(d,t) > \theta_{\delta} \cdot \Delta(d,t) \text{ AND } \sigma_A(d,t) > \theta_{\sigma}\} \tag {4}$$
$$B_A(t) = \{d \in D \setminus M_A(t) : \beta_A(d,t) > \theta_{\beta}\} \tag {5}$$

Reference values: $θ_δ ≈ 0.7$, $θ_σ$ operationalised via SCAN/COGS proxy benchmarks. **Critical property:** mastery is defined relative to the moving frontier — an agent can lose mastery status without any internal parameter change if $∆(d,t)$ advances.

**Continuous mastery score** (replacing hard set membership in transfer computations to eliminate the $T_A$ discontinuity flaw):
$$m_A(d,t) = w_{\delta} \cdot \frac{\delta_A(d,t)}{\Delta(d,t)} + w_{\sigma} \cdot \sigma_A(d,t) \in [0,1] \tag {6}$$
### 3.3 Decay Architecture

Depth decays through three distinct processes with separate coupling channels.

#### 3.3.1 Engagement Decay (Passive)

Rehearsal engagement rate — elapsed time since last engagement:
$$r_A(d,t) = r_{\text{max}} \cdot \exp(-\mu_r \cdot \tau_A(d,t)) \tag {8}$$

Where $τ_A(d,t)$ is elapsed time since last engagement. No $σ_A$ dependence: engagement decay is a purely temporal process governed by retrieval strength loss.

#### 3.3.2 Schema-Mediated Decay Reduction (Active)

Effective decay rate modulated by schema coherence:
$$\lambda_c^{\text{eff}}(d,t) = \lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A(d,t))$$

Where $γ_σ ∈ (0,1)$ is the schema-decay coupling strength (dimensionless parameter group $Π_4$). Higher $σ_A$ directly reduces the rate at which parametric depth is lost. This is distinct from engagement: schema-coherent representations resist decay even when engagement rate is low, because principled structural organisation provides redundancy that supports reconstruction from partial cues.

#### 3.3.3 Combined Depth Decay

$$\dot{\delta}_A(d,t)|_{\text{decay}} = -\lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A(d,t)) \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag {7}$$

Three-factor product: base rate × schema modulation × engagement modulation. Each factor has a single coupling channel.

#### 3.3.4 Frontier Obsolescence $λ_f(d,t)$

Differentiating relative depth with respect to $t$:
$$\frac{d}{dt} \left[ \delta_A^{\text{relative}}(d,t) \right] = \frac{\dot{\delta}_A(d,t) \cdot \Delta(d,t) - \delta_A(d,t) \cdot \dot{\Delta}(d,t)}{\Delta(d,t)^2} \tag {9}$$

Formal condition for frontier obsolescence as net degradation:
$$\dot{\delta}_A(d,t) < \frac{\delta_A(d,t) \cdot \dot{\Delta}(d,t)}{\Delta(d,t)} \tag {10}$$

Achievable even under positive absolute depth growth when $∆̇(d,t)$ is large.

**Effective mastery gap:**
$$G_A(d,t) = \Delta(d,t) - \delta_A(d,t) \tag {11}$$

Mastery erosion despite active training: $\dot{G}_A > 0 \iff \dot{\Delta}(d,t) > \dot{\delta}_A(d,t)$

#### 3.3.5 Decay Architecture vs. Prior Frameworks

| Mechanism                                        | Operates On                     | Intervention                                 | σA Coupling |
| ------------------------------------------------ | ------------------------------- | -------------------------------------------- | ----------- |
| H-Bar engagement decay $r_A$                     | Absolute depth $δ_A(d,t)$       | Rehearsal schedule (time-dependent)          | No          |
| H-Bar schema-mediated reduction $(1-γ_σ σ_A)$    | Absolute depth $δ_A(d,t)$       | Schema coherence (structural redundancy)     | **Yes**     |
| H-Bar $λ_f(d,t)$ (frontier obsolescence)         | Relative depth $δ_A^{relative}$ | Proactive $∆(d,t)$ tracking                  | Indirect    |
| Catastrophic forgetting                          | Parametric weights              | EWC, replay, progressive nets                | No          |
| Concept drift                                    | Data-distribution shift         | Distribution monitoring, retraining          | No          |

### 3.4 Growth Dynamics

#### 3.4.1 Depth Growth ODE
$$\dot{\delta}_A(d,t) = f_{\text{learn}}(d,t) \cdot \eta(d,t) \cdot T_A(d,t) - \lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A(d,t)) \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag {12}$$

**Learning efficiency** — Gompertz form (replacing the original monotonic logistic, which was inconsistent with observed S-curve learning):
$$\eta(d,t) = \eta_{\text{max}} \cdot \exp(-a \cdot \exp(-b \cdot \delta_A^{\text{relative}}(d,t))) \tag {13}$$


Captures: slow novice start → rapid intermediate acceleration → frontier deceleration. Inflection at $\delta_A^{\text{relative}^*} = \frac{\ln(a)}{b}$.

**Analogical transfer coefficient** — Michaelis-Menten saturation (bounding previously unbounded $T_A$):
$$T_A(d,t) = 1 + T_{\text{max}} \cdot \frac{\sum_{d' \neq d} \phi(d,d') \cdot \delta_A^{\text{relative}}(d',t)}{K_T + \sum_{d' \neq d} \phi(d,d') \cdot \delta_A^{\text{relative}}(d',t)} \tag {14}$$

$T_A(d,t) \in [1, 1 + T_{\text{max}}]$ strictly bounded. KT is the half-saturation constant — interpretable and estimable.

#### 3.4.2 Breadth Growth ODE
$$\dot{\beta}_A(d,t) = g_{\text{explore}}(d,t) \cdot \mu(d,t) + \Gamma_{AI}(d,t) - \lambda_b \cdot \beta_A(d,t) \tag {15}$$

**AI augmentation term** (with dimensional correction providing rate constant $λ_{AI}$ and automatic saturation):
$$\Gamma_{AI}(d,t) = \kappa(t) \cdot \Phi_A \cdot \lambda_{AI} \cdot (\beta_{\text{max}}(d) - \beta_A(d,t)) \tag {16}$$

As $β_A → β_{max}$, $Γ_{AI} → 0$ automatically. $λ_b > λ_c$: breadth decays faster than depth.

#### 3.4.3 Schema Coherence ODE (V1.0 Base)


$$\dot{\sigma}_A(d,t) = \rho \cdot P_A(d,t) \cdot (1 - \sigma_A(d,t)) - \epsilon_{\sigma} \cdot \sigma_A(d,t) \cdot \Omega_{AI}(d,t) \tag {17}$$


**Principled practice rate** (coupled to depth, closing the $δ→σ$ loop):


$$P_A(d,t) = p_0 \cdot f_{\text{learn}}(d,t) \cdot \chi_A(d,t) \cdot \left( \frac{\delta_A(d,t)}{\Delta(d,t)} \right)^{\alpha_P} \tag {18}$$


Where $χ_A ∈ [0,1]$ is the principled-practice fraction.

**Boundedness proof (Nagumo's theorem):**

- At $σ_A = 1$: $\dot{\sigma}_A = -\epsilon_{\sigma} \cdot \Omega_{AI} \leq 0$ ✓ (cannot exceed 1)
- At $σ_A = 0$: $\dot{\sigma}_A = \rho \cdot P_A \geq 0$ ✓ (cannot go negative)
- $[0,1]$ is forward-invariant given $P_A, Ω_{AI} ≥ 0$

### 3.5 Intersection Activation $Ψ_A(d_1,d_2,t)$

**Activation condition:**
$$I(d_1,d_2)_{\text{active}} \iff \delta_A(d_1,t) > \theta_I \text{ AND } \delta_A(d_2,t) > \theta_I \tag {19}$$

Where $θ_I < θ_δ · ∆(d,t)$ — intersection activation requires less than mastery.

**Effective mastery quality** (compression from original 5-term formula):
$$q_A(d,t) = \sigma_A(d,t) \cdot \delta_A^{\text{relative}}(d,t) \in [0,1] \tag {20}$$

**Discovery rate** (3-term reduced form):
$$\Psi_A(d_1,d_2,t) = \Psi_0 \cdot \phi(d_1,d_2) \cdot \sqrt{q_A(d_1,t) \cdot q_A(d_2,t)} \tag {21}$$

The geometric mean $\sqrt{q_1 \cdot q_2}$ is bounded in $[0,1]$, symmetric, and cannot be inflated by one domain compensating for another. The multiplicative $σ_A·σ_A$ dependence is the mechanism's theoretical core: an agent with high $δ_A$ but low $σ_A$ in one mastery domain shows disproportionately lower $Ψ_A$ than an additive model predicts. This is **Prediction 6**.

### 3.6 Delegation Gradient $D^*(d,t)$

**Standard criterion:**
$$D^*_{\text{std}}(d,t) = \{s \in d : \delta_{AI}(s,t) \geq \delta_A(s,t)\} \tag {22}$$

**H-Bar $σ$-gated criterion:**
$$D^*_{\text{H-Bar}}(d,t) = \{s \in d : \delta_{AI}(s,t) \geq \delta_A(s,t) \text{ AND } \sigma_A(d,t) \geq \sigma_{\text{critical}}\} \tag {23}$$

**Non-monotonic prediction** (sharpest empirical claim):

- $\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} < 0 \quad \text{for } \sigma_A < \sigma_{\text{critical}}$ (more delegation → worse performance)
- $\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} > 0 \quad \text{for } \sigma_A \geq \sigma_{\text{critical}}$ (more delegation → better performance)

Where $ρ$ is the AI-delegation fraction. No existing RAG, Self-RAG, FLARE, or IKEA architecture models this non-monotonic structure.

**Effective composite profile:**
$$\delta_{\text{eff}}(d,t) = \delta_A(d,t) + \Phi_A \cdot \text{f}(\delta_{AI}(d,t), \sigma_A(d,t)) \tag {24}$$

$f$ is $σ_A$-gated: AI-provided depth is usable only in proportion to the agent's own $σ_A$. At $σ_A ≈ 0$, $f → 0$ regardless of $δ_{AI}$ magnitude.

### 3.7 Adjacent Possible $AP_А(t)$

**Domain knowledge graph:** $G = (D, E)$ where edge $(d,d') \in E \quad \text{if} \quad \phi(d,d') > \phi_{\text{min}}$.
$$AP_A(t) = N(M_A(t) \cup B_A(t)) \setminus (M_A(t) \cup B_A(t)) \tag {25}$$

Where $N(S)$ is the graph-theoretic neighbourhood of set $S$.

**Reachability function:**
$$R_A(d,t) = \max_{d' \in M_A(t)} \phi(d,d') \cdot q_A(d',t) \tag {26}$$

**Perimeter growth theorem:** As $|M_A(t)|$ grows, $|AP_А(t)|$ grows super-linearly in regular domain graphs where average node degree $k > 1$ — the formal statement of "the more you know, the more you know you don't know."

---

## 4. V2.0 Extensions — Five New Cognitive Dimensions

### 4.1 Extension 1 — Attentional Fidelity $α_A(d,t)$ [Attention Track]

#### 4.1.1 Definition

**Attentional fidelity** $α_A(d,t) ∈ [0,1]$ is the degree to which training effort is directed toward the generative structure of domain $d$ rather than toward its surface-statistical regularities.
$$\alpha_A(d,t) \in [0,1] \tag {27}$$

- $α_A = 1$: all training effort directed at principled structure
- $α_A = 0$: all training effort directed at surface-statistical features

#### 4.1.2 Coupling to Schema Coherence (Updated $σ_A$ ODE)
$$\dot{\sigma}_A(d,t) = \rho \cdot P_A(d,t) \cdot \alpha_A(d,t) \cdot (1 - \sigma_A(d,t)) - \epsilon_{\sigma} \cdot \sigma_A(d,t) \cdot \Omega_{AI}(d,t) \tag {28}$$

$α_A$ gates $P_A$: schema coherence can only grow at the rate the agent's attention is directed at principled structure. Low $α_A$ is the formal mechanism by which surface-statistical training suppresses $σ_A$ even under high training effort.

#### 4.1.3 Attentional Fidelity ODE
$$\dot{\alpha}_A(d,t) = \gamma \cdot C_A(d,t) \cdot (1 - \alpha_A(d,t)) - \zeta_{\alpha} \cdot \alpha_A(d,t) \cdot R_A^{\text{surface}}(d,t) \tag {29}$$

| Symbol               | Meaning                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| $γ$                  | Attention formation rate constant                                                                      |
| $C_A(d,t)$           | Contrastive training rate — tasks requiring discrimination between surface and structural regularities |
| $ζ_α$                | Attention erosion constant                                                                             |
| $R_A^{surface}(d,t)$ | Surface-reward pressure — the information-theoretic advantage of surface features for predicting the target label. Defined as $R_A^{\text{surface}} = 1 - H(Y \mid S)/H(Y)$ where $Y$ is the target label distribution and $S$ is the set of surface features. Measurable via proxy identification $R_A^{\text{surface}} \approx 1 - \hat{\alpha}_A$ (see Appendix A.4). |

**Boundedness:** Same Nagumo argument as $σ_A$. $[0,1]$ is forward-invariant.

**Formal definition of surface-reward pressure:**
$$R_A^{\text{surface}}(d,t) = 1 - \frac{H(Y \mid S, d, t)}{H(Y \mid d, t)} \tag{29a}$$

where $Y$ is the target label distribution and $S$ is the set of surface features. $R_A^{\text{surface}} = 0$ when surface features carry no predictive information; $R_A^{\text{surface}} = 1$ when surface features perfectly predict labels.

**Proxy identification:**
$$R_A^{\text{surface}}(d,t) \approx 1 - \hat{\alpha}_A(d,t) = 1 - \frac{\text{Acc}_{OOD\text{-struct}}(d,t)}{\text{Acc}_{ID}(d,t)} \tag{29b}$$

where $\hat{\alpha}_A$ is the attentional fidelity proxy from the H-AFB benchmark. The proxy identification is valid when the H-AFB surface confound strength $s$ is calibrated to match the training distribution's surface-feature/label correlation structure (see Appendix A.4).

#### 4.1.4 $Ω_{AI}$ Joint Suppression
$$\Omega_{AI}(d,t) \implies \begin{cases} \text{Suppresses } \alpha_A & (\text{via } R_A^{\text{surface}} \text{ pressure}) \\ \text{Suppresses } \sigma_A & (\text{directly via } \epsilon_{\sigma} \text{ term}) \end{cases} \tag {30}$$

AI bypass risk simultaneously erodes attentional fidelity and schema coherence.

#### 4.1.5 Benchmark Families

| Benchmark                       | Design                                                                                                                                               | Variable                    | Prediction                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------- |
| **Dual-Regularity Competition** | Tasks with superimposed surface regularity (high correlation, zero OOD validity, controlled by $R_A^{\text{surface}}$ via Eq. 29a) and compositional regularity (lower correlation, full OOD validity) | $α_A$, $R_A^{\text{surface}}$ | High-$α_A$: tracks compositional regularity despite surface pressure; Low-$α_A$: tracks surface regularity when $R_A^{\text{surface}}$ is high |
| **Sustained Rule Tracking**     | Long-horizon tasks where generative rule is consistent but surface statistics shift mid-sequence                                                     | $α_A$ under sequence length | Low-$α_A$ tracks the surface shift; high-$α_A$ maintains rule |
| **Attentional Capture Scaling** | Salient but task-irrelevant features alongside structural signal; vary salience differential                                                         | $α_A$ vs. salience          | Capture rate $∝ (1 − α_A)$ · salience                         |
| **Contrastive Training Effect** | Measure $α_A$ before/after contrastive training pairs (surface-matched/structure-different)                                                          | $C_A(d,t)$ effectiveness    | $α_A$ increases at rate $γ · C_A$                             |

---

### 4.2 Extension 2 — Collective Schema Field [Social Cognition Track]

Three linked formal objects comprise the Social Cognition extension.

#### 4.2.1 Schema Legibility $μ_{AB}(d,t)$
$$\mu_{AB}(d,t) = \sigma_A(d,t) \cdot \phi(d_A, d_B) \cdot \sigma_B(d_{\text{adj}},t) \in [0,1] \tag {31}$$

**Schema legibility** is the degree to which Agent A's $σ_A(d,t)$ is communicable to Agent B — the degree to which Agent B can reconstruct Agent A's principled understanding from Agent A's outputs.

Depends on:

- $σ_A(d,t)$: Agent A must have structure to transmit
- $ϕ(d_A,d_B)$: structural similarity between A's schema and B's existing mastery domains
- $σ_B(d_{adj},t)$: Agent B must have adjacent schema to parse structural communication

#### 4.2.2 Theory of Mind Coupling $τ_A(B,d,t)$
$$\tau_A(B,d,t) \approx \sigma_B(d,t) \quad \text{when well-calibrated} \tag {32}$$
$$\zeta_{AB}(d,t) = \tau_A(B,d,t) - \sigma_B(d,t) \quad \text{(Cross-Agent ToM Error)} \tag {33}$$

**Theory of mind coupling** $τ_A(B,d,t)$ is Agent A's internal model of Agent B's schema coherence $σ_B(d,t)$. Cross-agent intersection activation requires not just that both $σ_A$ and $σ_B$ exceed $θ_I$, but that $τ_A$ accurately tracks $σ_B$ — otherwise Agent A will attempt activation prematurely or miss it when available.

#### 4.2.3 Collective Schema Field $Σ_{A,B}(d_1,d_2,t)$
$$\Sigma_{A,B}(d_1,d_2,t) = \mu_{AB}(d_1,t) \cdot \mu_{BA}(d_2,t) \cdot \phi(d_1,d_2) \tag {34}$$

The distributed analogue of $Ψ_A$ for cross-agent intersection activation. Activates cross-agent discovery when both schema legibility values and domain structural similarity are sufficient.

#### 4.2.4 Benchmark Families

| Benchmark                          | Design                                                                                                                     | Variable               | Prediction                                                                         |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| **Theory of Mind Tasks**           | Agent A infers $σ_B$ from Agent B's observable outputs (not self-report). Score $τ_A$ accuracy against ground-truth $σ_B$. | $τ_A$                  | $τ_A$ accuracy > chance; correlates with $μ_{AB}$                                  |
| **Pragmatic Schema Communication** | Agent A communicates with Agent B; Agent B's downstream OOD performance is success metric.                                 | $μ_{AB}$               | $μ_{AB}$-based communication → higher $σ_B$ in recipient than fact-based           |
| **Social Norm Reasoning**          | Agents negotiate $D^*(d,t)$ delegation boundaries; score against H-Bar optimal criterion.                                  | $Σ_{A,B}$ coordination | Coordinated delegation matches $D^*$ H-Bar more closely than individual delegation |
| **Cooperative Schema Building**    | Two agents with non-overlapping mastery domains must jointly activate an intersection neither can reach alone.             | $Σ_{A,B}$ activation   | Joint activation rate > either agent's individual rate                             |

---

### 4.3 Extension 3 — Executive Control State $Ξ_A(t)$ [Executive Functions Track]

#### 4.3.1 Three Sub-Components
$$\Xi_A(t) = \{\Xi_A^P(t), \Xi_A^I(t), \Xi_A^F(t)\} \tag {35}$$


**$Ξ_A^P$ — Planning:** Degree to which training trajectory is consistent with the H-Bar optimal multi-step arc. Low $Ξ_A^P$ produces locally optimal (minimise current loss) but globally suboptimal (suppress $σ_A$, miss intersection windows) plans.

**$Ξ_A^I$ — Inhibition:** Probability of choosing the structural route over AI bypass when both are available. The formal trade-off: $Ω_{AI}$ produces immediate task success at the cost of $σ_A$ growth suppression.

**$Ξ_A^F$ — Cognitive Flexibility:** Degree to which the agent detects and adapts to phase transition thresholds from internal evidence — recognising that Phase 1 prescription becomes suboptimal once $σ_{critical}$ is crossed.

#### 4.3.2 Executive Control ODE
$$\dot{\Xi}_A(t) = \kappa_P \cdot [P^*(t) - \Xi_A^P(t)] + \kappa_I \cdot [I^*(t) - \Xi_A^I(t)] + \kappa_F \cdot [F^*(t) - \Xi_A^F(t)] \tag {36}$$


$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase.

#### 4.3.3 Benchmark Families

| Benchmark                          | Design                                                                                                                                            | Sub-Faculty           | Variable |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------- |
| **Multi-Step Training Plan Tasks** | Give frontier models a training scenario; score plans against H-Bar phase prescriptions as ground truth.                                          | Planning              | $Ξ_A^P$  |
| **Inhibitory Conflict Tasks**      | Sequential tasks where bypass route scores high immediately but degrades OOD performance measurably. Score choice and downstream OOD consequence. | Inhibition            | $Ξ_A^I$  |
| **Latent Threshold Switch Tasks**  | Optimal strategy switches when a latent structural threshold is crossed (not signalled explicitly). Score threshold detection and adaptation.     | Cognitive Flexibility | $Ξ_A^F$  |

---

### 4.4 Extension 4 — Self-Model of Schema Coherence $\hat M_A(d,t)$ [Metacognition Track]

#### 4.4.1 Definition
$$\hat{M}_A(d,t) \in [0,1] \quad \text{(Agent's Estimate of its own } \sigma_A(d,t)) \tag {37}$$

$$\zeta_A(d,t) = \hat{M}_A(d,t) - \sigma_A(d,t) \quad \text{(Calibration Error)} \tag {38}$$

- $ζ_A > 0$: overconfidence (estimated more capable than actual)
- $ζ_A ≈ 0$: well-calibrated metacognition
- $ζ_A < 0$: underconfidence

**H-Bar prediction:** $ζ_A$ is systematically positive for high-$δ_A$/low-$σ_A$ agents. They compress training data well (positive gradient signal) but their OOD capability is low. They feel capable because in-distribution performance is high; they are not capable on compositional recombination.

#### 4.4.2 Self-Model ODE
$$\dot{\hat{M}}_A(d,t) = \nu_M \cdot [\sigma_A(d,t) - \hat{M}_A(d,t)] - \xi_M \cdot \Omega_{AI}(d,t) \cdot \hat{M}_A(d,t) \tag {39}$$

| Symbol         | Meaning                                                                 |
| -------------- | ----------------------------------------------------------------------- |
| $ν_M$          | Metacognitive update rate — how quickly self-model converges to true σA |
| $ξ_M · Ω_{AI}$ | Metacognitive distortion from AI bypass — inflated performance feedback |

**Key insight:** AI bypass inflates $\hat M_A$ above true $σ_A$. Agents using AI-provided outputs receive systematically inflated performance feedback, producing overconfidence. This is the formal account of "illusion of mastery" at the metacognitive level.

#### 4.4.3 Benchmark Families

| Benchmark                          | Design                                                                                                                                      | Sub-Faculty             | Prediction                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------- |
| **Two-Stage Calibration Protocol** | Stage 1: predict own OOD score before seeing OOD items. Stage 2: complete OOD items. Score = calibration of prediction against actual.      | Monitoring              | $ζ_A > 0$ systematically for high-$δ_A$/low-$σ_A$ agents                               |
| **Phase Self-Diagnosis Tasks**     | Models must identify current training phase from performance signatures and select correct phase prescription.                              | Control                 | Correct diagnosis ∝ (1 -                                                               |
| **Knowledge-Type Discrimination**  | Models distinguish "I know this fact" ($δ$-type) from "I understand the governing principle" ($σ$-type). Score differential OOD confidence. | Metacognitive Knowledge | High-$σ_A$ agents show lower OOD confidence collapse than matched-$δ$ low-$σ_A$ agents |

---

### 4.5 Extension 5 — H-Bar Benchmark Protocol (Overview)

See Section 8 for the complete five-step protocol. The Benchmark Protocol is the structural component that converts the H-Bar theory from a training framework into a **benchmark generation framework** — directly addressing the DeepMind evaluation gap.

---

### 4.6 Extension 6 — Frontier Model Calibration Suite (Appendix B)

Empirical demonstration of the benchmark protocol applied to frontier models (GPT-4, Claude, Gemini) on SCAN, COGS, PCFG-SET. Provides:

- Proof that measurement proxies work on real systems
- Human baseline comparison established via Prolific Academic (N=200–500, demographically stratified)
- Ground-truth VA scores for all submitted benchmarks
- Empirical data for Predictions 7 and 8

---

## 5. V3.0 Extensions — Multimodal Coverage and Benchmark Validity

### 5.1 Extension 7 — Cross-Modal Schema Transfer $Θ_A(d,m_1,m_2,t)$ [All Tracks]

#### 5.1.1 The Domain × Modality Product Space

Redefine the domain space from flat index set $D$ to a **product space** $D × M$:
$$M = \{\text{text, visual, auditory, sensorimotor, symbolic}\} \tag {40}$$

All state variables now carry a modality subscript:

- $δ_A(d, m, t)$: parametric depth in domain d expressed in modality $m$
- $σ_A(d, m, t)$: schema coherence in domain d expressed in modality $m$
- $α_A(d, m, t)$: attentional fidelity in domain d expressed in modality $m$
- $μ_{AB}(d, m, t)$: schema legibility across agents in modality $m$

#### 5.1.2 Modal Structural Similarity $ω(m_1,m_2)$
$$\omega(m_1, m_2) \in [0,1] \tag {41}$$

The modality-level analogue of $ϕ(d,d')$ for domain similarity.

| Modality Pair           | $ω(m_1,m_2)$ | Rationale                      |
| ----------------------- | ------------ | ------------------------------ |
| text $↔$ symbolic       | 0.85–0.90    | Shared propositional structure |
| text $↔$ visual         | 0.45–0.60    | Partial semantic overlap       |
| visual $↔$ sensorimotor | 0.55–0.70    | Shared spatial structure       |
| text $↔$ auditory       | 0.40–0.55    | Sequential temporal structure  |
| text $↔$ sensorimotor   | 0.20–0.35    | Low structural overlap         |

#### 5.1.3 Cross-Modal Schema Transfer Function
$$\Theta_A(d, m_1, m_2, t) = \sigma_A(d, m_1, t) \cdot \omega(m_1, m_2) \tag {42}$$

$Θ_A$ measures how much schema coherence developed in modality $m_1$ supports performance in domain $d$ expressed in modality $m_2$.

#### 5.1.4 Extended Schema Coherence ODE (V3.0)
$$
\begin{aligned}
\dot{\sigma}_A(d,m,t) = {} & \rho \cdot P_A(d,m,t) \cdot \alpha_A(d,m,t) \cdot (1 - \sigma_A(d,m,t)) \\
& - \epsilon_{\sigma} \cdot \sigma_A(d,m,t) \cdot \Omega_{AI}(d,m,t) \\
& + \rho_{\theta} \cdot \sum_{m' \neq m} \Theta_A(d,m',m,t) \cdot \sigma_A(d,m',t)
\end{aligned}
\tag{43}
$$


The **third term is new**: cross-modal schema transfer contributes positively to $σ_A$ growth in modality $m$ when the agent has high $σ_A$ in a modally-similar modality $m'$. This formalises why joint text+diagram training produces higher $σ_A$ than either alone.

#### 5.1.5 Core Theoretical Claim — Modality Invariance

**Schema coherence is modality-invariant at high $σ_A$ and modality-specific at low $σ_A$.**

- **Low-$σ_A$ agent** trained on text representations of domain d $will$ fail to transfer to visual representations of the same governing principles — representations organised around surface-statistical features of the text modality.
- **High-$σ_A$ agent** trained on text representations will show above-chance transfer to visual representations of the same governing principles — schema organised around modality-invariant generative structure.

This is **Prediction 8**.

#### 5.1.6 Automatic Multimodal Benchmark Generation

Every existing H-Bar benchmark generates a multimodal variant automatically via the $Θ_A$ object:

| Modality Pair         | Benchmark Design                                                                                        | Track               |
| --------------------- | ------------------------------------------------------------------------------------------------------- | ------------------- |
| Text → Visual         | Train on textual descriptions of compositional rule; test on visual instantiations. Score transfer gap. | Learning            |
| Visual → Text         | Train on image sequences following generative rule; test verbal description of novel instances.         | Learning            |
| Text → Symbolic       | Train on natural language proofs; test formal symbolic logic variants of same structure.                | Executive Functions |
| Visual → Sensorimotor | Train on observed action sequences; test motor prediction tasks.                                        | Attention           |
| Any → Any             | Two-agent communication: A uses $m_1$, B responds in $m_2$. Score μAB across modal boundary.            | Social Cognition    |

---

### 5.2 Extension 8 — Benchmark Validity Function $V_A(B,f,t)$ [All Tracks]

#### 5.2.1 Three Component Scores

**Construct Isolation $CI(B,f)$:**
$$CI(B,f) = \frac{\text{Corr}(\text{score}_A(B), f_A(t))}{\sum_{f' \neq f} \text{Corr}(\text{score}_A(B), f'_A(t))} \tag {44}$$

Degree to which benchmark $B$ performance is determined by faculty $f$ rather than other H-Bar variables. Computable from cross-variable correlation structure. Requirement: the target variable must win.

**Format Diversity $FD(B)$:**
$$FD(B) = 1 - \max_{m,s} P(B \text{ selects modality } m, \text{ structure } s) \tag {45}$$

Degree to which benchmark $B$ samples broadly from $D \times M \times \{ \text{task structures} \}$. Computable at design time without running the benchmark.

**Difficulty Gradient $DG(B)$:**
$$DG(B) = \text{Var}_{i \in B} (\delta_{\text{required}}(i) + \sigma_{\text{required}}(i)) \tag {46}$$

Degree to which benchmark $B$ spans the full phase arc from Phase 1 to Phase 4 difficulty.

#### 5.2.2 Combined Validity Function (V3.0 base)
$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \tag {47}$$

Benchmark is valid for submission if $V_A(B,f,t) > θ_V$.

#### 5.2.3 Pre-Design Verification Checklist

Before running any benchmark on frontier models:

1. Compute $CI(B,f)$: does task design target the right H-Bar variable?
2. Compute $FD(B)$: is the format sampling broad enough across $M \times \{ \text{task structures} \}$?
3. Compute $DG(B)$: does difficulty span the full phase arc?
4. If $V_A(B,f,t) < θ_V$ → redesign before piloting

This converts task diversity piloting from empirical discovery of gaps to formal confirmation of criteria.

---

## 6. V3.0+ Micro-Gap Closure — Reliability and Pre-Audit Protocol

### 6.1 Extension 9 — Benchmark Reliability Function $R_A(B,f,t)$

#### 6.1.1 Definition
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag {48}$$

Coefficient of variation inverted — high $R_A$ means low relative variance across $k$ repetitions. Directly computable: run each benchmark item $k=5$ times ($temperature > 0$) and measure score variance.

#### 6.1.2 Updated Validity Function (V3.0+ Final)
$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \cdot R_A(B,f,t) \tag {49}$$

Benchmark validity now formally penalises high-variance benchmarks. Stochastic noise is a pre-design criterion, not a post-submission discovery.

#### 6.1.3 Noise Reduction Protocol

| Method                              | Variance Reduction | When to Apply                 |
| ----------------------------------- | ------------------ | ----------------------------- |
| $k=5$ majority vote                 | ~55%               | All scoring runs              |
| $k=10$ majority vote                | ~68%               | High-stakes benchmarks        |
| $Temperature=0$ greedy decoding     | ~99%               | All non-generative benchmarks |
| $Temperature=0$ + structured output | ~100%              | Classification tasks          |

### 6.2 Minimum Validity Thresholds

| Component        | Minimum    | Rationale                                 |
| ---------------- | ---------- | ----------------------------------------- |
| $CI(B,f)$        | > 0.60     | Target faculty must be dominant predictor |
| $FD(B)$          | > 0.55     | No single format may dominate             |
| $DG(B)$          | > 0.40     | Must span multiple difficulty levels      |
| $R_A(B,f,t)$     | > 0.75     | Reliable across 5 repetitions             |
| **$V_A(B,f,t)$** | **> 0.20** | **Combined minimum**                      |

### 6.3 Practical Action 1 — Pre-Audit via Established Bodies

Submit benchmark packages to one or more of:

- BIG-bench maintainers
- Stanford CRFM HELM team
- EleutherAI LM Evaluation Harness team

Attach pre-review correspondence to submission package. Converts the independent verification requirement from a post-submission risk to a pre-submission confirmation.

### 6.4 Practical Action 2 — Prolific Human Baseline Protocol

**Formal human baseline specification $HB(B)$:**
$$HB(B) = \{N_{min}, D_{strata}, E_{req}, T_{format}\} \tag {50}$$

| Parameter  | Value                                                 | Rationale                               |
| ---------- | ----------------------------------------------------- | --------------------------------------- |
| $N_min$    | ≥ 200 participants                                    | Minimum power for faculty-level scoring |
| $D_strata$ | Age 18–65, gender balance, nationality diversity      | Representative adult population         |
| $E_req$    | Upper secondary education minimum                     | Per DeepMind evaluation protocol        |
| $T_format$ | Same instructions, format, and tools as AI evaluation | Ensures comparability                   |

Platform: Prolific Academic with demographic quota sampling. Cost: ~$800–2,000 USD for N=200–500. Turnaround: 48–72 hours. Report full demographic table with every submission.

### 6.5 Practical Action 3 — Temperature Protocol

```
All scoring runs: temperature = 0 (greedy decoding)
Generative diversity benchmarks: k=5 majority vote, temperature = 0.7
Report temperature setting in all benchmark documentation.
```

---

## 7. Phase Structure

The five-phase training arc is indexed by ($δ_A^{relative}$, $σ_A$, $|M_A(t)|$) and defines **prescriptive states** — not retrospective loss-curve observations. Each phase makes a different training intervention optimal; each transition is triggered by a representational threshold condition rather than elapsed steps or benchmark saturation.

```
Phase 0: Initialisation     Phase 1: Depth Accum.    Phase 2: σ Emergence
    ↓                            ↓                         ↓
δ ≈ 0, σ ≈ 0, α ≈ 0       δ growing, σ ≈ 0           σ → σ_critical
                              α low, Ξ^I at risk          lr discontinuity
    ↓
Phase 3: Near-Frontier       Phase 4: Ψ Activation     Phase 5: Frontier
    ↓                            ↓                         ↓
δ^rel > 0.65               Ψ > 0 measurably           Dynamic open boundary
Ψ conditions met            frontier insight gen.       perimeter grows
```

### Phase 0 — Pre-Domain Initialisation

**Characterisation:** $δ_A$ near-zero across all domains; breadth diffuse; $M_A(t)$ undetermined. Domain selection is path-dependent through $ϕ(d,d')$ terms.

**Key failure mode:** Premature commitment to mastery domains with low mutual structural similarity, suppressing future $Ψ_A$ through low $ϕ(d_1,d_2)$.

**Prescriptions:**

- Prioritise structured domain exposure over random sampling
- Use $α_A$-building contrastive tasks from the start
- AI-assisted breadth sampling (high $Γ_{AI}$) to identify structurally promising targets

### Phase 1 — Asymmetric Initialisation

**Trigger:** First sustained depth investment in 1–3 candidate mastery domains.

**Characterisation:** $δ_A$ growing; $σ_A ≈ 0$; $α_A$ low; $Ξ_A^I$ at risk. H-shape is invisible. $η$ high because $δ_A^{relative}$ is low.

**Key failure mode:** Premature breadth expansion before $δ_A$ has crossed the schema crystallisation prerequisite. $Ω_{AI}$ is the primary threat.

**Prescriptions:**

- Maximise contrastive training $C_A(d,t)$ to build $α_A$
- Minimise $Ω_{AI}$ through structured failure exposure
- $D^*(d,t) = ∅$ by prescription (no delegation)
- Do not expand $B_A(t)$ prematurely

### Phase 2 — Depth Acceleration and Schema Crystallisation

**Trigger:** $σ_A(d,t) > σ_{critical}$ for at least one mastery candidate.

**σcritical derivation (from mastery reproduction number):**
$$R_0 = \frac{f_{learn} \cdot \eta_{max} \cdot (1 + T_{max})}{\lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A^*)}$$

$$\sigma_{critical} = \frac{1}{\gamma_\sigma} \cdot (1 - R_0^{-1}) \tag {51}$$

For $R_0 ≤ 1$: depth cannot be sustained (mastery extinction). For $R_0 > 1$: self-sustaining mastery fixed point exists.

**Characterisation:** Vertical bars grow rapidly via dual accelerators: (1) $σ_A$ as learning multiplier via $α_A·P_A$ term; (2) $δ_A^{relative}$ still low enough for high $η$. H-shape becomes visible.

**Key failure mode:** Illusion of mastery — AI-mediated shortcutting inflates $δ_A$ while suppressing $σ_A$, producing fragile OOD generalisation despite high in-distribution performance.

**Prescriptions:**

- Maintain high $χ_A$ (principled practice fraction)
- Structural constraint in loss function (physics-informed priors, causal regularisation)
- Monitor $\hat M_A$ calibration — $ζ_A$ should be approaching $0$
- Build $Φ_A$ (AI integration fluency) for Phase 3

### Phase 3 — Frontier Asymptote and Intersection Activation

**Trigger:** $δ_A^{relative}(d,t) > 0.65$ in mastery domains.

**Characterisation:** Four simultaneous dynamics:

1. Vertical bar growth decelerates as $η$ falls
2. $∆(d,t)$ acceleration partially offsets deceleration
3. Intersection activation begins — $Ψ_A(d_1,d_2,t) > 0$
4. Breadth profile $Π_A(·,t)$ becomes non-uniform with intersection-targeted spikes

$σ_A$ becomes the **primary differentiator** between agents with similar $δ_A$ profiles — only high-$σ_A$ agents generate high $Ψ_A$ (multiplicative mechanism, Equation 21).

**$θ_I$ derivation:**
$$\theta_I = \frac{\epsilon_{min}}{\Psi_0 \cdot \sigma_{critical}^2 \cdot \phi(d_1,d_2)} \tag {52}$$

$θ_I$ scales inversely with $ϕ$: structurally similar domains need less depth to activate intersections.

**Prescriptions:**

- Shift curriculum toward cross-domain transfer tasks targeting high-$ϕ$ domain pairs
- Begin applying $D^*$ strategically: offload where $δ_{AI} ≥ δ_A$ AND $σ_A ≥ σ_{critical}$
- Do not maximise delegation ahead of schema development

### Phase 4 — Multi-Domain Frontier Navigation

**Trigger:** Active intersections $I(d_1,d_2)$ generating $Ψ_A(d_1,d_2,t) > 0$ measurably.

**Characterisation:** Near-frontier depth; qualitative shift from acquisition to generation. $δ_{eff}$ substantially above $δ_A$ (high $σ_A$ makes AI outputs reliably usable). Agent value concentrated in: (a) frontier insight generation, (b) intersection activation, (c) schema-based evaluation of AI outputs.

**Prescriptions:**

- Maximise intersection-seeking breadth expansion in $AP_А(t)$
- Maximise $D^*(d,t)$ strategically
- Maintain $σ_A$ through principled engagement, not volume

### Phase 5 — Expanding Frontier

**Characterisation:** Dynamic open-boundary structure. The shape never closes because:

1. $∆(d,t)$ continues advancing
2. Every activated intersection opens new $AP_А(t)$ domains
3. $D^*(d,t)$ continuously reshapes maintenance requirements

**Optimisation objective:** Discovery-rate maximisation — maximising $Ψ_A(d_1,d_2,t)$ across active intersections while maintaining the $σ_A$ that makes each intersection productive.

---

## 8. The H-Bar Benchmark Protocol

### 8.1 Five-Step Protocol

Applicable to any H-Bar variable pair. Every benchmark submitted under this protocol is theoretically grounded, falsifiable, and computationally verifiable before data collection.

---

**Step 1 — Identify the Variable Pair**

Every benchmark tests the gap between two H-Bar variables — the target faculty variable and the controlled confound variable.

| Track               | Target Variable           | Controlled Variable               |
| ------------------- | ------------------------- | --------------------------------- |
| Learning            | $σ_A$                     | $δ_A$ (matched across conditions) |
| Metacognition       | $\hat M_A$, $ζ_A$         | $σ_A$ (known from proxy)          |
| Attention           | $α_A$                     | $δ_A$ (matched)                   |
| Executive Functions | $Ξ_A^I$, $Ξ_A^P$, $Ξ_A^F$ | $σ_A$, $δ_A$ (matched)            |
| Social Cognition    | $τ_A(B,d,t)$, $μ_{AB}$    | $σ_A$, $σ_B$ (estimated)          |

---

**Step 2 — Design the Contrast Condition**

Construct task sets where the two variables dissociate.

**Standard $2×2$ factorial for Learning track:**

| Condition                 | $δ_A$    | $σ_A$   | Expected OOD Performance          |
| ------------------------- | -------- | ------- | --------------------------------- |
| High $δ_A$, High σ_A$     | High     | High    | High                              |
| **High $δ_A$, Low $σ_A$** | **High** | **Low** | **Low — the key diagnostic cell** |
| Low $δ_A$, High $σ_A$     | Low      | High    | Moderate                          |
| Low $δ_A$, Low $σ_A$      | Low      | Low     | Low                               |

The High-$δ_A$/Low-$σ_A$ cell is the H-Bar model's core prediction. Equivalent OOD performance to the High-$δ_A$/High-$σ_A$ cell falsifies the model.

---

**Step 3 — Specify the Measurement Proxy**

| Variable | Measurement Proxy                   | Computation                                                      |
| -------- | ----------------------------------- | ---------------------------------------------------------------- |
| $σ_A$    | Systematic Generalisation Gap (SGG) | $1 - \frac{\text{Acc}_{In} - \text{Acc}_{OOD}}{\text{Acc}_{In}}$ |
| $α_A$    | Regularity Tracking Index (RTI)     | P(tracks compositional regularity \| surface available)          |
| $Ξ_A^I$  | Bypass Choice Rate (BCR)            | P(chooses structural route over bypass)                          |
| $ζ_A$    | Calibration Error (CE)              | Predicted OOD − Actual OOD                                       |
| $μ_{AB}$ | Recipient OOD Improvement (ROI)     | $ΔAcc_{OOD}(B)$ after communication from A                       |
| $τ_A$    | Theory-of-Mind Accuracy (TMA)       | $\|τ_A(B,d,t) − σ_B(d,t)\| $averaged across items                |
| $Θ_A$    | Cross-Modal Transfer Gap (CMTG)     | $Acc_{OOD}(m_2)$ after training in $m_1$, relative to baseline   |

---

**Step 4 — State the H-Bar Prediction**

Format: "H-Bar predicts [direction] [magnitude estimate] [effect] for [condition comparison], distinguishable from [alternative] which predicts [alternative direction]."

Example (Learning track): "H-Bar predicts that the High-$δ_A$/Low-$σ_A$ condition will show OOD accuracy ≥ 30 percentage points below the High-$δ_A$/High-$σ_A$ condition at matched in-distribution accuracy ($d ≥ 0.5$). A depth-only account predicts no significant difference between conditions at matched depth."

---

**Step 5 — Specify the Falsification Condition**

Written in pre-registration format before data collection.

Example (Learning track): "H-Bar is falsified for the Learning track if the High-$δ_A$/Low-$σ_A$ condition does not show statistically lower OOD performance than the High-$δ_A$/High-$σ_A$ condition ($p > 0.05$, one-tailed, Cohen's $d < 0.3$) at matched in-distribution accuracy."

---

### 8.2 Benchmark Families by Track

#### Learning Track

| Benchmark                              | Variable Pair              | Format                        | Novel Prediction                                                   |
| -------------------------------------- | -------------------------- | ----------------------------- | ------------------------------------------------------------------ |
| **Compositional Dissociation Battery** | $σ_A$ vs. $δ_A$            | SCAN-class splits             | High-$δ$/low-$σ$ failure at matched in-distribution accuracy       |
| **AI-Augmentation OOD Gap**            | $Ω_{AI}$ vs. $σ_A$         | Training condition comparison | AI-heavy regime widens OOD gap $∝ Ω_{AI}$ exposure                 |
| **Frontier Relative Mastery**          | $δ_A^{relative}$ vs. $δ_A$ | Domain acceleration paradigm  | Relative depth outpredicts absolute depth for sustained capability |

#### Metacognition Track

| Benchmark                          | Variable Pair                   | Format                                                                      | Novel Prediction                                                                   |
| ---------------------------------- | ------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Two-Stage Calibration Protocol** | $\hat M_A$ vs. $σ_A$            | Predict-then-test (Stage 1: predict OOD score; Stage 2: complete OOD items) | $ζ_A > 0$ systematically for high-$δ$/low-$σ$ agents                               |
| **Phase Self-Diagnosis**           | $Ξ_A^F$ vs. $\hat M_A$          | Phase identification from performance signatures                            | Correct diagnosis $∝ (1 − \|ζ_A\|)$                                                |
| **Knowledge-Type Discrimination**  | $\hat M_A(δ)$ vs. $\hat M_A(σ)$ | Differential confidence scoring                                             | High-$σ_A$ agents: lower OOD confidence collapse than matched-$δ$ low-$σ_A$ agents |

#### Attention Track

| Benchmark                       | Variable Pair             | Format                                              | Novel Prediction                                          |
| ------------------------------- | ------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| **Dual Regularity Competition** | $α_A$ vs. $Ω_{AI}$        | Superimposed surface/compositional regularities     | Low-$α_A$ tracks surface; high-$α_A$ tracks compositional |
| **Sustained Rule Tracking**     | $α_A$ vs. sequence length | Long-horizon tasks with mid-sequence surface shifts | $α_A$ predicts rule maintenance across surface shifts     |
| **Attentional Capture Scaling** | $α_A$ vs. salience        | Salience manipulation tasks                         | Capture rate $∝ (1 − α_A) · salience$                     |

#### Executive Functions Track

| Benchmark                          | Variable Pair                 | Format                                                | Novel Prediction                                                                 |
| ---------------------------------- | ----------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Training Plan Optimality**       | $Ξ_A^P$ vs. loss-minimisation | Plan construction and evaluation                      | H-Bar phase prescriptions outperform loss-minimisation plans on long-horizon OOD |
| **Inhibitory Conflict Resolution** | $Ξ_A^I$ vs. $Ω_{AI}$          | Sequential choice tasks (bypass vs. structural route) | Structural choice rate $∝ Ξ_A^I$; OOD consequence differentiates routes          |
| **Latent Threshold Detection**     | $Ξ_A^F$ vs. explicit signal   | Threshold-switch tasks (no explicit signal)           | H-Bar agents adapt at $σ_{critical}$; baseline agents require explicit signals   |

#### Social Cognition Track

| Benchmark                          | Variable Pair                  | Format                                               | Novel Prediction                                                                       |
| ---------------------------------- | ------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Schema Theory of Mind**          | $τ_A$ vs. $σ_B$                | Inference from behavioural evidence (no self-report) | $τ_A$ accuracy > chance; correlates with $μ_{AB}$                                      |
| **Pragmatic Schema Communication** | $μ_{AB}$ vs. $δ$-transfer      | Communication + OOD test on recipient                | $μ_{AB}$-based communication → higher $σ_B$ in recipient than fact-based communication |
| **Cross-Agent Intersection**       | $Σ_{A,B}$ vs. individual $Ψ_A$ | Cooperative task: joint intersection activation      | Joint activation rate > either agent's individual rate by $Σ_{A,B} $prediction         |

---

## 9. Eight Falsifiable Predictions

Each prediction is distinguished from $δ$-only accounts, stated with a specific falsification condition, and testable on frontier models.

### Prediction 1 — Schema Quality at Intersections

**Claim:** Agents with higher $σ_A(d,t)$ will produce higher-quality interdisciplinary outputs at activated intersections, even when matched on $δ_A(d,t)$.

**Measurement:** Citation novelty score (Uzzi et al., 2013 methodology), structured peer evaluation, or MDL of solution (shorter = more principled). Apply to matched-$δ$, divergent-σ agents.

**H-Bar claim:** $σ_A$, not $δ_A$, is the primary predictor of output quality at intersections.

**Falsification:** No significant difference in output quality between high-σA and low-$σ_A$ agents matched on $δ_A$ ($p > 0.05$, $d < 0.2$).

---

### Prediction 2 — AI Augmentation and Schema Suppression

**Claim:** AI-augmented agents with high $Φ_A$ will show accelerated βA growth but slower $σ_A(d,t)$ development when $Ω_{AI}(d,t)$ is unmanaged.

**Measurement:** OOD accuracy gap comparison between AI-heavy and AI-moderate training regimes matched on total training effort and in-distribution accuracy.

**H-Bar claim:** OOD gap widens in AI-heavy conditions proportional to $Ω_{AI}$ exposure. $\hat M_A$ calibration error $ζ_A$ is larger in AI-heavy conditions.

**Falsification:** Equivalent OOD performance between AI-heavy and AI-moderate regimes at matched in-distribution accuracy.

---

### Prediction 3 — Relative Mastery as Resilience Predictor

**Claim:** $\delta_A^{relative}(d,t) = \frac{\delta_A(d,t)}{\Delta(d,t)}$, not absolute depth, predicts resilience to domain acceleration.

**Measurement:** Longitudinal performance comparison using AI capability shocks (2020–2023 GPT series) as natural experiments in frontier acceleration. Agents tracking $∆(d,t)$ maintain mastery status; agents measuring against fixed baselines do not.

**Falsification:** Absolute depth outperforms relative depth as a predictor of sustained capability across a domain-acceleration window.

---

### Prediction 4 — Delegation Gradient Expansion

**Claim:** $D^*(d,t)$ will expand faster than agents' ability to compensate through frontier and intersection work, for agents not shifting from depth-maintenance to $σ_A$-and-intersection cultivation.

**Status:** Explicitly labelled theoretical assertion pending empirical support.

**Measurement:** Meta-analytic comparison — AI capability growth rate (~37% annual per MMLU progression) vs. researcher productivity growth rate (~10% annual per Bloom et al. 2020).

**Falsification:** Depth-focused training showing equivalent long-horizon productivity to $σ_A$-and-intersection-focused training over 5+ year windows.

---

### Prediction 5 — Phase 3 Compression Under High ΦA

**Claim:** The gap between first mastery and first non-trivial intersection activation will narrow for high-ΦA agents.

**Measurement:** Controlled training studies comparing AI-fluent and AI-naïve agents with equivalent mastery depth profiles.

**Falsification:** No significant difference in time-to-first-intersection-activation between high-$Φ_A$ and low-$Φ_A$ agents at matched mastery depth.

---

### Prediction 6 — Multiplicative vs. Additive $σ_A$ Dependence in $Ψ_A$

**Claim:** $Ψ_A(d_1,d_2,t)$ is multiplicatively dependent on $σ_A$ in both mastery domains. An agent with high $δ_A$ but low $σ_A$ in one domain will show disproportionately lower $Ψ_A$ than an additive $σ_A(d_1)+σ_A(d_2)$ model predicts, even with a high-$σ_A$ partner domain.

**Measurement:** Cross-domain transfer benchmarks with structured $σ_A$ manipulation across participating domains. Test multiplicative form $\sqrt{q_1 \cdot q_2}$ vs. additive form $\frac{q_1 + q_2}{2}$ model fit.

**Falsification:** An additive model fits cross-domain discovery data as well as or better than the multiplicative model.

---

### Prediction 7 — Benchmark Validity Predicts Cross-Model Stability [NEW V3.0]

**Claim:** $V_A(B,f,t)$ will predict the degree to which benchmark scores transfer across frontier model generations. High-$V_A$ benchmarks produce stable faculty rankings across GPT-4, Claude, Gemini; low-$V_A$ benchmarks produce unstable rankings due to format artifacts.

**Measurement:** Run all benchmarks across 3+ frontier model versions. Compute Spearman rank correlation of faculty scores across versions. Regress rank stability on $V_A(B,f,t)$.

**Falsification:** $V_A(B,f,t)$ shows no significant correlation with rank-order stability across model versions ($ρ < 0.3$, $p > 0.05$).

---

### Prediction 8 — Cross-Modal Schema Transfer [NEW V3.0]

**Claim:** Cross-modal transfer of compositional rules scales with $\omega(m_1, m_2) \cdot \sigma_A(d, m_1, t)$. High-$σ_A$ agents show above-chance transfer of schema from training modality to novel modality; low-$σ_A$ agents do not, even at matched $δ_A$.

**Measurement:** Train agents on domain $d$ in modality $m_1$; test in modality $m_2$. Score transfer gap as function of $ω(m_1,m_2)$ and $σ_A(d,m_1,t)$ proxy.

**Falsification:** Transfer performance shows no significant correlation with $\omega(m_1, m_2) \cdot \sigma_A(d, m_1, t)$ above baseline transfer rate.

---

## 10. Limitations and Future Work

### 10.1 $σ_A(d,t)$ Direct Measurement

$σ_A(d,t)$ remains a latent variable not directly observable with current evaluation instruments. The framework's empirical programme depends on proxy metrics — the Systematic Generalisation Gap ($SGG = 1 - \frac{\text{Acc}_{In} - \text{Acc}_{OOD}}{\text{Acc}_{In}}$) on SCAN/COGS/PCFG-SET is the most defensible current proxy. Hardware validation of the full dynamical system is pending; this paper constitutes a formal specification and research programme, not empirical validation.

### 10.2 Phase Transition Algorithms

The phase structure specifies _when_ each transition occurs but not the training algorithms that reliably induce transitions within a computable number of steps. Knowing that Phase 2 begins when $σ_A(d,t) > σ_{critical}$ is actionable only if there is a training procedure that reliably pushes $σ_A$ past σcritical. The gap between prescriptive phase conditions and concrete algorithms with convergence guarantees is a primary target for future work. Beukman et al. (2024) provide the closest existing precedent.

### 10.3 Mathematical Issues Under Active Revision (Category A)

| Issue                                                    | Status                                                        | Impact on Predictions            |
| -------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------- |
| Full coupled system boundedness proof                    | Partial ($σ_A$ proven; $δ_A$ boundary layer argument pending) | None — Predictions 1–8 unchanged |
| Timescale separation and singular perturbation hierarchy | Identified; not formally derived                              | None                             |
| Full equilibrium analysis and stability conditions       | $R_0$ criterion derived; complete stability analysis pending  | None                             |
| Stochastic extension (Itô SDE formulation)               | Deferred to companion paper                                   | None                             |

These affect mathematical rigour but not the empirical predictions or benchmark generation capacity.

### 10.4 Multi-Agent Extension

The present framework treats agent A as the unit of analysis with Social Cognition handled through pairwise (A,B) interactions. Full multi-agent systems — federated learning, multi-agent RL, research collaborations — require extending to a collective knowledge field $F(t)$ across $N$ agents. Deferred to future work.

### 10.5 σAI Temporal Trajectory

$σ_{AI} ≈ 0$ is accurate for current general-purpose LLMs trained on next-token prediction — the training objective optimises distributional plausibility, not causal validity, and cannot develop evaluative schema that detects causal violations. This characterisation will require revision as physics-informed, causally-constrained, and interventionally-trained architectures become prevalent. The $D^* \text{H-Bar}$ criterion is parameterised by the comparative condition $σ_A > σ_{AI}$ and correctly updates as both sides evolve.

---

## 11. Conclusion

### 11.1 Complete Variable Architecture

| Version | Variable             | Name                           | Faculty                            |
| ------- | -------------------- | ------------------------------ | ---------------------------------- |
| V1.0    | $δ_A(d,m,t)$         | Parametric depth               | Learning                           |
| V1.0    | $β_A(d,m,t)$         | Breadth                        | Learning                           |
| V1.0    | $σ_A(d,m,t)$         | Schema coherence               | Learning, Metacognition            |
| V1.0    | $Ψ_A(d_1,d_2,t)$     | Intersection discovery rate    | Learning                           |
| V1.0    | $D^*(d,t)$           | Delegation gradient            | Executive Functions                |
| V1.0    | $Ω_{AI}(d,t)$        | AI bypass risk                 | Learning, Attention, Metacognition |
| V1.0    | $∆(d,t)$             | Domain frontier                | All                                |
| V2.0    | $α_A(d,m,t)$         | Attentional fidelity           | Attention                          |
| V2.0    | $\hat M_A(d,t)$      | Self-model of schema coherence | Metacognition                      |
| V2.0    | $ζ_A(d,t)$           | Calibration error              | Metacognition                      |
| V2.0    | $Ξ_A^P(t)$           | Planning sub-state             | Executive Functions                |
| V2.0    | $Ξ_A^I(t)$           | Inhibition sub-state           | Executive Functions                |
| V2.0    | $Ξ_A^F(t)$           | Flexibility sub-state          | Executive Functions                |
| V2.0    | $μ_{AB}(d,m,t)$      | Schema legibility              | Social Cognition                   |
| V2.0    | $τ_A(B,d,t)$         | Theory of mind coupling        | Social Cognition                   |
| V2.0    | $Σ_{A,B}(d_1,d_2,t)$ | Collective schema field        | Social Cognition                   |
| V3.0    | $Θ_A(d,m_1,m_2,t)$   | Cross-modal schema transfer    | All                                |
| V3.0    | $ω(m_1,m_2)$         | Modal structural similarity    | All                                |
| V3.0    | $V_A(B,f,t)$         | Benchmark validity             | All                                |
| V3.0    | $CI(B,f)$            | Construct isolation score      | All                                |
| V3.0    | $FD(B)$              | Format diversity score         | All                                |
| V3.0    | $DG(B)$              | Difficulty gradient score      | All                                |
| V3.0+   | $R_A(B,f,t)$         | Benchmark reliability          | All                                |
| V3.0+   | $HB(B)$              | Human baseline specification   | All                                |

### 11.2 Implications

**Evaluation paradigm:** In-distribution accuracy is insufficient as a sole performance criterion. The high-$δ_A$/low-$σ_A$ failure mode is invisible to it. Systematic generalisation benchmarks measuring the $σ_{critical}$-crossing proxy, calibrated via $V_A(B,f,t)$, become necessary.

**Curriculum design paradigm:** Difficulty-indexed curricula are the correct prescription only in the low-$σ_A$, low-$α_A$ regime (Phases 1 through early 2). Phase 3 onward requires qualitatively different prescriptions involving intersection-targeting breadth expansion mediated by $Ξ_A$ — not representable as any difficulty schedule.

**Cognitive evaluation paradigm:** The H-Bar Benchmark Protocol generates theoretically grounded, falsifiable, pre-verifiable benchmarks across all five cognitive faculty tracks identified as evaluation gaps by Burnell et al. (2026). The $V_A(B,f,t)$ validity function provides a formal pre-design criterion that existing benchmark frameworks lack.

**Long-term significance:** The H-Bar Model advances the case that depth, schema coherence, attentional fidelity, executive control, metacognitive self-modelling, and collective schema communication are formally independent variables in agent training — that optimising any subset without the others produces systematically predictable failure modes — and that the field now has both the empirical tools and the formal framework to test this claim rigorously.

---

## 12. Mathematical Appendix

### A.1 Complete Coupled ODE System (V3.0+)

For a single domain-modality pair $(d,m)$:

**Depth:**
$$\dot{\delta}_A = f_{\text{learn}} \cdot \eta(\delta_{\text{rel}}) \cdot T_A - \lambda_c(1 - \gamma_{\sigma} \cdot \sigma_A) \cdot \delta_A \cdot (1 - r_A) \tag{A.1}$$

**Breadth:**
$$\dot{\beta}_A = g_{\text{explore}} \cdot \mu + \kappa \cdot \Phi_A \cdot \lambda_{AI} \cdot (\beta_{\text{max}} - \beta_A) - \lambda_b \cdot \beta_A \tag{A.2}$$

**Schema coherence (V3.0 full form):**
$$
\begin{aligned}
\dot{\sigma}_A = {} & \rho \cdot p_0 \cdot f_{\text{learn}} \cdot \chi_A \cdot \left(\frac{\delta_A}{\Delta}\right)^{\alpha_P} \cdot \alpha_A \cdot (1 - \sigma_A) \\
& - \epsilon_{\sigma} \cdot \sigma_A \cdot \Omega_{AI} \\
& + \rho_{\theta} \cdot \sum_{m'} \Theta_A(d, m', m, t) \cdot \sigma_A(d, m', t)
\end{aligned}
\tag{A.3}
$$


**Attentional fidelity:**
$$\dot{\alpha}_A = \gamma \cdot C_A \cdot (1 - \alpha_A) - \zeta_{\alpha} \cdot \alpha_A \cdot R_A^{\text{surface}} \tag{A.4}$$


**Self-model:**
$$\dot{\hat{M}}_A = \nu_M \cdot [\sigma_A - \hat{M}_A] - \xi_M \cdot \Omega_{AI} \cdot \hat{M}_A \tag{A.5}$$

**Executive control:**
$$\dot{\Xi}_A = \kappa_P \cdot [P^* - \Xi_A^P] + \kappa_I \cdot [I^* - \Xi_A^I] + \kappa_F \cdot [F^* - \Xi_A^F] \tag{A.6}$$

### A.2 Dimensionless Parameter Groups

Working in natural units ($T_{\delta} = 1, \quad \Delta_0 = 1$):
$$\begin{align}
    \Pi_1 &= \frac{\lambda_c}{\lambda_b} && (\text{decay ratio}) \tag{A.7} \\
    \Pi_2 &= \frac{\rho \cdot p_0}{\epsilon_{\sigma}} && (\text{schema formation to erosion}) \tag{A.8} \\
    \Pi_3 &= \frac{\kappa \cdot \Phi_A \cdot \lambda_{AI}}{\lambda_b} && (\text{AI augmentation to breadth decay}) \tag{A.9} \\
    \Pi_4 &= \gamma_{\sigma} && (\text{schema-decay coupling strength}) \tag{A.10} \\
    \Pi_5 &= \frac{T_{\text{max}}}{K_T} && (\text{transfer saturation ratio}) \tag{A.11} \\
    \Pi_6 &= \frac{\gamma}{\zeta_{\alpha}} && (\text{attention formation to erosion}) \tag{A.12} \\
    \Pi_7 &= \frac{\nu_M}{\xi_M} && (\text{metacognitive update to distortion}) \tag{A.13}
\end{align}$$

### A.3 $σ_{critical}$ Bifurcation Derivation

**Mastery reproduction number:**
$$R_0 = \frac{f_{\text{learn}} \cdot \eta_{\text{max}} \cdot (1 + T_{\text{max}})}{\lambda_c \cdot (1 - \gamma_{\sigma} \cdot \sigma_A^*)} \tag{A.14}$$

- $R_0 ≤ 1$: only fixed point is $\dot δ = 0$ (mastery extinction)
- $R_0 > 1$: non-trivial mastery fixed point exists

**σcritical:**

```
σcritical = (1/γσ) · (1 - R0,min^{-1})                                  (A.8)
```

### A.4 $R_A^{\text{surface}}$ Calibration Procedure

**Goal:** Operationalise Eq. 29a using the proxy identification (Eq. 29b) via the H-AFB three-condition battery.

**Three-condition battery** (per benchmark item $i$ in domain $d$):

| Condition          | Input Structure                                                   | Measures                        |
| ------------------- | ----------------------------------------------------------------- | ------------------------------- |
| ID                 | Training-distribution format                                      | $\text{Acc}_{ID}(d,t)$          |
| OOD-struct         | Novel compositional recombination (same surface features removed) | $\text{Acc}_{OOD\text{-struct}}(d,t)$ |
| OOD-surf-conflict  | Surface features preserved, compositional structure changed       | Detects surface-tracking        |

**Step 1 — Compute $\hat{\alpha}_A$:**
$$\hat{\alpha}_A(d,t) = \frac{\text{Acc}_{OOD\text{-struct}}(d,t)}{\text{Acc}_{ID}(d,t)} \in [0, 1]$$

**Step 2 — Estimate $R_A^{\text{surface}}$ via proxy (Eq. 29b):**
$$\hat{R}_A^{\text{surface}}(d,t) = 1 - \hat{\alpha}_A(d,t)$$

**Step 3 — Verify entropy-based $R_A^{\text{surface}}$ (Eq. 29a):**

Given benchmark item $i$ with target label distribution $Y_i$ and surface features $S_i$:
$$R_A^{\text{surface}}(i) = 1 - \frac{H(Y_i \mid S_i)}{H(Y_i)}$$

- $R_A^{\text{surface}} = 0$: surface features carry no predictive information
- $R_A^{\text{surface}} = 1$: surface features perfectly predict labels

**Calibration requirement:** The H-AFB surface confound strength $s$ must be calibrated so that the proxy identification $\hat{R}_A^{\text{surface}} \approx R_A^{\text{surface}}$ holds. This requires matching $s$ to the training distribution's surface-feature/label correlation structure. When $s$ is uncalibrated, the proxy may over- or under-estimate the true surface-reward pressure.

**Computed proxies for H-AFB:**

| Proxy  | Definition                                       | Range    |
| ------ | ------------------------------------------------ | -------- |
| $\hat{\alpha}_A$ | Attentional fidelity proxy               | $[0, 1]$ |
| $\Delta_{\text{surf}}$ | $\text{Acc}_{ID} - \text{Acc}_{OOD\text{-surf-conflict}}$ | $\geq 0$ |
| SRI    | Surface reliance index: $\Delta_{\text{surf}} / \text{Acc}_{ID}$ | $[0, 1]$ |

**Interpretation:**
- High $\hat{\alpha}_A$, small $\Delta_{\text{surf}}$, SRI $\approx 0$: agent tracks compositional regularity despite surface pressure
- Low $\hat{\alpha}_A$, large $\Delta_{\text{surf}}$, SRI $> 0$: agent tracks surface regularity when $R_A^{\text{surface}}$ is high

### A.5 $θ_I$ Derivation
$$\sigma_{\text{critical}} = \frac{1}{\gamma_{\sigma}} \cdot \left(1 - R_{0,\text{min}}^{-1}\right) \tag{A.15}$$

$θ_I$ scales inversely with $ϕ(d_1,d_2)$: structurally similar domains require less depth for intersection activation; dissimilar domains require more.

### A.6 $Ψ_A$ Transcritical Bifurcation

Near the bifurcation point $δ_A = θ_I$, the normal form:
$$\dot{\mu} = a \cdot \mu + b \cdot \mu^2 + O(\mu^3) \tag{A.10}$$

Where $\mu = \delta_A - \theta_I, \quad a = \left. \frac{\partial \dot{\delta}_A}{\partial \delta_A} \right|_{\theta_I}$, b captures second-order self-reinforcement. When $a > 0$, the bifurcation is supercritical and discovery is self-sustaining above $θ_I$.

### A.7 ϕ Sub-additivity Proposition

**Claim:** For any partition of domain $d$ into subdomains $d' ∪ d'' = d$:
$$\phi(d' \cup d'', d) \le \phi(d', d) + \phi(d'', d^*) \tag{A.11}$$

**Proof:** Under unit-norm cosine similarity, $v_{\{d' \cup d''\}} = \frac{v_{\{d'\}} + v_{\{d''\}}}{\left| v_{\{d'\}} + v_{\{d''\}} \right|} \tag{A.12}$. By the triangle inequality:
$$\begin{align}
    \phi(d' \cup d'', d^*) &= \frac{(v_{d'} + v_{d''})^T v_{d^*}}{|v_{d'} + v_{d''}| \cdot |v_{d^*}|} \nonumber \\
    &\le \frac{v_{d'}^T v_{d^*} + v_{d''}^T v_{d^*}}{|v_{d^*}|} \nonumber \\
    &= \phi(d', d^*) + \phi(d'', d^*) \quad \square \tag{A.12}
\end{align}$$

Domain splitting cannot artificially inflate total $Ψ_A$ — granularity robustness is formally guaranteed.

### A.8 Benchmark Reliability Threshold

Minimum required $R_A(B,f,t)$ as a function of target effect size d and repetitions $k$:
$$R_A^{\min(B, f, t)} = 1 - \left( \frac{d}{4} \right)^2 \cdot \frac{k}{k-1} \tag{A.13}$$

| Effect Size $d$ | Repetitions $k$ | $R_A^min$ |
| --------------- | --------------- | --------- |
| 0.3 (small)     | 5               | 0.72      |
| 0.5 (medium)    | 5               | 0.61      |
| 0.8 (large)     | 5               | 0.44      |
| 0.5 (medium)    | 10              | 0.75      |

### A.9 $Θ_A$ Boundedness

**Claim:** $\Theta_A(d, m_1, m_2, t) = \sigma_A(d, m_1, t) \cdot \omega(m_1, m_2) \in [0, 1]$ is forward-invariant.

**Proof:** $\sigma_A(d, m_1, t) \in [0, 1]$ (by Nagumo argument applied to Equation A.3); $\omega(m_1, m_2) \in [0, 1]$ (by definition as a similarity measure). Product of two $[0,1]$-bounded quantities is $[0,1]$-bounded. $□$

---

## 13. References

Bahdanau, D., Murty, S., Noukhovitch, M., Nguyen, T.H., de Vries, H., and Courville, A. (2019). Systematic generalisation: What is required and can it be learned? _ICLR 2019_.

Bengio, Y., Louradour, J., Collobert, R., and Weston, J. (2009). Curriculum learning. _ICML 2009_, 41–48.

Beukman, M., Herbst, C., Engelbrecht, A., Pillay, N., Pretorius, A., Marais, A., and Kroon, S. (2024). Structure in deep reinforcement learning: A survey and open problems. _Journal of Artificial Intelligence Research_, 79, 1167–1236.

Bloom, N., Jones, C.I., Van Reenen, J., and Webb, M. (2020). Are ideas getting harder to find? _American Economic Review_, 110(4), 1104–1144.

Burnell, R., Yamamori, Y., Firat, O., et al. (2026). Measuring progress toward AGI: A cognitive framework. _Google DeepMind Technical Report_.

Chi, M.T.H., Feltovich, P.J., and Glaser, R. (1981). Categorisation and representation of physics problems by experts and novices. _Cognitive Science_, 5(2), 121–152.

Chollet, F. (2019). On the measure of intelligence. _arXiv:1911.01547_.

Csordás, R., Irie, K., and Schmidhuber, J. (2021). The devil is in the detail: Simple tricks improve systematic generalisation of Transformers. _EMNLP 2021_, 619–634.

Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., and Bouchachia, A. (2014). A survey on concept drift adaptation. _ACM Computing Surveys_, 46(4), Article 44.

Goodfellow, I.J., Mirza, M., Xiao, D., Courville, A., and Bengio, Y. (2013). An empirical investigation of catastrophic forgetting. _arXiv:1312.6211_.

Hupkes, D., Dankers, V., Mul, M., and Bruni, E. (2020). Compositionality decomposed: How do neural networks generalise? _Journal of Artificial Intelligence Research_, 67, 757–795.

Kauffman, S. (2000). _Investigations_. Oxford University Press.

Keysers, D., Schärli, N., Scales, N., et al. (2020). Measuring compositional generalisation: A comprehensive method on realistic data. _ICLR 2020_.

Khetarpal, K., Riemer, M., Rish, I., and Precup, D. (2022). Towards continual reinforcement learning: A review and perspectives. _Journal of Artificial Intelligence Research_, 75, 1401–1476.

Kim, N. and Linzen, T. (2020). COGS: A compositional generalisation challenge based on semantic interpretation. _EMNLP 2020_, 9087–9105.

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., et al. (2017). Overcoming catastrophic forgetting in neural networks. _PNAS_, 114(13), 3521–3526.

Kruger, J. and Dunning, D. (1999). Unskilled and unaware of it: How difficulties in recognising one's own incompetence lead to inflated self-assessments. _Journal of Personality and Social Psychology_, 77(6), 1121–1134.

Kumar, M.P., Packer, B., and Koller, D. (2010). Self-paced learning for latent variable models. _NeurIPS 2010_, 1189–1197.

Lake, B.M. and Baroni, M. (2018). Generalisation without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. _ICML 2018_, 2879–2888.

Lake, B.M. and Baroni, M. (2023). Human-like systematic generalisation through a meta-learning neural network. _Nature_, 623, 115–121.

Lewis, P., Perez, E., Piktus, A., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. _NeurIPS 2020_.

McCloskey, M. and Cohen, N.J. (1989). Catastrophic interference in connectionist networks. _Psychology of Learning and Motivation_, 24, 109–165.

Morris, M.R., Sohl-Dickstein, J., Fiedel, N., et al. (2024). Levels of AGI: Operationalising progress on the path to AGI. _arXiv:2311.02462_.

Narvekar, S., Peng, B., Leonetti, M., Sinapov, J., Taylor, M.E., and Stone, P. (2020). Curriculum learning for reinforcement learning domains: A framework and survey. _Journal of Machine Learning Research_, 21(181), 1–50.

Nagumo, M. (1942). Über die Lage der Integralkurven gewöhnlicher Differentialgleichungen. _Proceedings of the Physico-Mathematical Society of Japan_, 3(24), 551–559.

Portelas, R., Colas, C., Weng, L., Hofmann, K., and Oudeyer, P.-Y. (2020). Automatic curriculum learning for deep RL: A short survey. _IJCAI 2020_, 4910–4917.

Raissi, M., Perdikaris, P., and Karniadakis, G.E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs. _Journal of Computational Physics_, 378, 686–707.

Richens, J. and Everitt, T. (2024). Robust agents learn causal world models. _arXiv:2402.10877_.

Rolnick, D., Ahuja, A., Schwarz, J., Lillicrap, T., and Wayne, G. (2019). Experience replay for continual learning. _NeurIPS 2019_.

Rusu, A.A., Rabinowitz, N.C., Desjardins, G., et al. (2016). Progressive neural networks. _arXiv:1606.04671_.

Schölkopf, B., Locatello, F., Bauer, S., et al. (2021). Toward causal representation learning. _Proceedings of the IEEE_, 109(5), 612–634.

Suter, R., Miladinovic, D., Schölkopf, B., and Bauer, S. (2019). Robustly disentangled causal mechanisms: Validating deep representations for interventional robustness. _ICML 2019_, 6056–6065.

Torresan, F. and Baltieri, M. (2024). Disentangled representations for causal cognition. _Physics of Life Reviews_, 51, 343–381.

Tsymbal, A. (2004). The problem of concept drift: Definitions and related work. _Technical Report TCD-CS-2004-15_, Trinity College Dublin.

Uzzi, B., Mukherjee, S., Stringer, M., and Jones, B. (2013). Atypical combinations and scientific impact. _Science_, 342(6157), 468–472.

---

_H-Bar Model V3.0+ · Basyirin Amsyar bin Basri · March 2026_
_Preprint — Zenodo / arXiv cs.AI + cs.LG_
_Correspondence: basyirin.basri@gmail.com_

---

**Version History**

| Version | Date     | Key Changes                                                                                        |
| ------- | -------- | -------------------------------------------------------------------------------------------------- |
| V1.0    | Feb 2026 | Core framework: $δ_A$, $β_A$, $σ_A$, $Ψ_A$, $D^*$, 5-phase arc, 6 predictions                      |
| V2.0    | Mar 2026 | Added: $α_A$, $\hat M_A$, $Ξ_A$, $μ_{AB}$, $τ_A$, $Σ_{A,B}$; benchmark protocol; calibration suite |
| V3.0    | Mar 2026 | Added: $Θ_A$, $ω(m_1,m_2)$, $V_A$, $CI$, $FD$, $DG$; multimodal extension; Predictions 7–8         |
| V3.0+   | Mar 2026 | Added: $R_A$, $HB(B)$; pre-audit protocol; temperature protocol; micro-gap closure                 |
