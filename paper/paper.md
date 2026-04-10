## Schema Coherence, Cognitive Faculty Evaluation, and Phase-Structured Curriculum Design for AI Agents

**Basyirin Amsyar bin Basri**
Independent Researcher · Petaling Jaya, Malaysia
basyirin.basri@gmail.com

**Version:** 3.0+ (Full Reconstruction)
**Status:** Preprint Draft
**Date:** March 2026

---

## Abstract

Current training pipelines optimise parametric depth $δ_A(d,t)$ without formally targeting schema coherence $σ_A(d,t)$ — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities. **Existing empirical results on compositional generalisation benchmarks demonstrate that agents exhibiting high parametric depth but low schema coherence fail systematically** on out-of-distribution recombination tasks that standard in-distribution metrics do not detect. No existing framework specifies the mechanisms by which $σ_A$ forms, what suppresses it, or how it interacts with attention, executive control, metacognitive self-modelling, collective schema communication, or cross-modal transfer.

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

The framework demonstrates formal correspondence with five cognitive faculty gaps identified by Burnell et al. (2026) — Learning, Metacognition, Attention, Executive Functions, and Social Cognition — and **enables generation of executable benchmark families for each**. If $σ_A$ is formally necessary and current training pipelines systematically suppress it, capable-agent training requires structural revision beyond scale and curriculum ordering alone.

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
12. [Empirical Grounding](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#12-empirical-grounding)
13. [Mathematical Appendix](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#13-mathematical-appendix)
14. [References](https://claude.ai/chat/5703f583-4fee-4213-b278-642f26599fc2#14-references)

---

## 1. Introduction

The standard framing of systematic compositionality failure is precise and reproducible. Agents trained to high in-distribution accuracy on sequence and language tasks fail near-completely when test distributions require zero-shot recombination of primitives trained in isolation. Lake and Baroni (2018) demonstrated this on SCAN — seq2seq models achieve above 99% accuracy on random test splits and below 2% on the add-primitive split. The broader benchmark literature is consistent: COGS (Kim and Linzen, 2020) finds 96–99% in-distribution accuracy alongside 16–35% compositional generalisation accuracy; CFQ (Keysers et al., 2020) shows performance degradation growing monotonically with compound divergence; PCFG-SET (Hupkes et al., 2020) documents failures on productivity, systematicity, and substitutivity tests across RNNs, CNNs, and Transformers.

The structural argument follows directly. Current training pipelines have one formal optimisation target: minimise expected loss over the training distribution. This objective efficiently increases one variable — **parametric depth** $δ_A(d,t)$ — but has no formal mechanism for increasing a second, independent variable: **schema coherence** $σ_A(d,t)$, the degree to which representations are restructured around deep governing principles.

The H-Bar Model V1.0 formalised this asymmetry. V2.0 extended it to cover four additional cognitive faculties — Attention, Executive Functions, Metacognition, and Social Cognition — each with formal variables, ODEs, and benchmark generation protocols. V3.0 extended all variables to a domain × modality product space and formalised benchmark validity as a measurable object. V3.0+ adds a reliability function and three practical protocols that close the remaining measurement gaps.

### 1.1 Central Claim

> Training pipelines that optimise $δ_A(d,t)$ without formally targeting $σ_A(d,t)$ will systematically produce agents that pass in-distribution evaluation while failing out-of-distribution recombination — not because they lack depth, but because their training regimes suppress the schema crystallisation that converts parametric depth into principled generalisation capacity. Furthermore, the suppression mechanism extends to attentional allocation ($α_A$), executive control ($Ξ_A$), metacognitive self-modelling ($\hat M_A$), and inter-agent schema communication ($μ_{AB}$) — all of which interact multiplicatively with σA through the formal coupling terms derived below.

### 1.2 Cognitive Faculty Alignment

The framework demonstrates formal correspondence with the five cognitive faculties identified as evaluation gaps by Burnell et al. (2026):

| Faculty                 | Primary Variable                  | Mechanism                                             |
| ----------------------- | --------------------------------- | ----------------------------------------------------- |
| **Learning**            | $σ_A(d,t)$, $δ_A(d,t)$            | OOD gap as schema proxy; compositional generalisation |
| **Metacognition**       | $\hat M_A(d,t)$, $ζ_A(d,t)$       | Self-model accuracy; calibration error dynamics       |
| **Attention**           | $α_A(d,t)$, $CA(d,t)$             | Attentional fidelity to generative structure          |
| **Executive Functions** | $Ξ_A^P$, $Ξ_A^I$, $Ξ_A^F$         | Planning, inhibition, cognitive flexibility           |
| **Social Cognition**    | $μ_{AB}$, $τ_A(B,d,t)$, $Σ_{A,B}$ | Schema legibility, theory of mind, collective field   |

---

## 2. Related Work and Gap Analysis

### 2.1 Curriculum Learning

Bengio et al. (2009) established the foundational result: easy-to-hard sample ordering improves generalisation by providing representational scaffolding. Subsequent work elaborated difficulty measurement (Kumar et al., 2010; Portelas et al., 2020; Narvekar et al., 2020) and pacing schedules. Every variant maximises the rate at which δA increases.

**Gap statement.** Curriculum learning provides training-sequence optimisation for depth growth rate but has no formal account of $σ_A(d,t)$ dynamics, no triggering conditions for schema crystallisation, and no prescription for the qualitative shift in training regime that σcritical-crossing requires. The H-Bar phase structure formalises all three.

### 2.2 Compositional Generalisation

The SCAN/COGS/CFQ/PCFG-SET benchmark family collectively documents the high-$δ_A$/low-$σ_A$ failure mode empirically. The consistent diagnosis: models encode statistical regularities rather than the compositional rules governing the distribution.

**Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise $σ_A$ as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

#### 2.2.1 Recent Work Differentiation

**Noviello et al. (2025) — MIRAGE dual-process model.** Noviello et al. argue that compositional generalisation requires a separate symbolic System-2 module — an architectural addition that overlays explicit rule-based reasoning onto neural pattern matching. The H-Bar framework demonstrates that this structural requirement is unnecessary by formalising compositional capacity as a developmental trajectory within a single ODE system. Specifically, schema coherence $σ_A(d,t)$ grows continuously through the $σ_A$ ODE (Eq. 28): $\dot{\sigma}_A = \rho \cdot P_A \cdot \alpha_A \cdot (1 - \sigma_A) - \epsilon_\sigma \cdot \sigma_A \cdot \Omega_{AI}$, where the $α_A$ gating term directs neural training effort toward compositional structure without requiring a separate symbolic substrate. The $σ_{\text{critical}}$ bifurcation (Eq. 51: $\sigma_{\text{critical}} = (1/\gamma_\sigma) \cdot (1 - R_0^{-1})$) defines a threshold crossing that is achievable entirely within the neural parameter space — no symbolic overlay is invoked. Mirage's dual-architecture claim conflates a training-trajectory failure ($α_A$ suppressed by surface-reward pressure $R_A^{\text{surface}}$, Eq. 29) with an architectural impossibility. H-Bar predicts that agents trained with sufficient contrastive training $C_A(d,t)$ will cross $σ_{\text{critical}}$ and achieve compositional generalisation within the same architecture that Mirage declares inadequate.

**Li et al. (2023) — SLOG benchmark recursion failures.** Li et al. document persistent failures on unseen recursion depths across seq2seq models on the SLOG benchmark. H-Bar predicts these failures from the $σ_A$ ODE as a Phase 1 diagnostic: agents with $σ_A \approx 0$ cannot transfer recursive patterns to unseen depths because the schema growth term $\rho \cdot P_A \cdot \alpha_A \cdot (1 - \sigma_A)$ is gated by $α_A$, which is suppressed when surface-reward pressure $R_A^{\text{surface}}$ is high (Eq. 29). The Systematic Generalisation Gap proxy (Eq. 3b: $\hat{\sigma}_A = \text{Acc}_{\text{OOD}}/\text{Acc}_{\text{In}}$) directly quantifies the recursion deficit SLOG exposes. Furthermore, the $Ψ_A$ geometric mean (Eq. 21: $\Psi_A = \Psi_0 \cdot \phi \cdot \sqrt{q_1 \cdot q_2}$) predicts geometric — not linear — degradation of recursive transfer capacity as schema coherence decreases: an agent at $σ_A = 0.3$ in both participating domains shows $Ψ_A$ at $\sqrt{0.3} \approx 55\%$ of its maximum, not the $60\%$ an additive model predicts. SLOG's recursion failures are not architectural limitations but measurable signatures of low-$σ_A$ agents whose training never crossed $σ_{\text{critical}}$.

**Bruns (2025) — RASP structural representability proof.** Bruns proves via RASP that transformers possess the structural capacity to represent compositional operations — that the representational destination exists in parameter space even when models fail to learn it. H-Bar's framework is complementary rather than contradictory: the RASP proof establishes that $σ_{\text{critical}}$-crossing is theoretically possible, while H-Bar's ODE system explains why standard training does not achieve it. The $α_A$ ODE (Eq. 29: $\dot{\alpha}_A = \gamma \cdot C_A \cdot (1 - \alpha_A) - \zeta_\alpha \cdot \alpha_A \cdot R_A^{\text{surface}}$) formalises the learnability gap that Bruns identifies qualitatively. Surface-reward pressure $R_A^{\text{surface}}$ — the information-theoretic advantage of surface features for predicting target labels — provides a locally optimal gradient signal that suppresses $α_A$ and therefore prevents $σ_A$ growth through the gating term in Eq. 28. Bruns' representability result and H-Bar's learnability analysis are jointly necessary: representability without learnability is the formal statement that $σ_A$'s target state exists but the $α_A \cdot R_A^{\text{surface}}$ term blocks the training trajectory from reaching it. No prior framework connects these two results through a single ODE system.

**Jiang et al. (2022) — Mutual exclusivity training on COGS.** Jiang et al. demonstrate that mutual exclusivity (ME) training pushes COGS lexical scores substantially higher while structural compositionality splits remain below 1%. H-Bar's $σ_A$ ODE (Eq. 28) predicts this dissociation precisely: ME training increases the principled practice rate $P_A$ at the lexical level (better encoding of individual primitive meanings — a $δ_A$ gain) but does not gate through $α_A$ for structural compositional regularities, so $\rho \cdot P_A \cdot \alpha_A \cdot (1 - \sigma_A) \approx 0$ regardless of $P_A$ magnitude. This result instantiates the High-$δ_A$/Low-$σ_A$ diagnostic cell in the H-Bar 2×2 factorial design (§8.1) — the cell that $δ$-only accounts predict should show equivalent OOD performance to High-$δ_A$/High-$σ_A$. Jiang et al.'s below-1% structural splits at matched high lexical accuracy are the empirical signature H-Bar's multiplicative $Ψ_A$ form (Eq. 21) predicts: when $q_A = \sigma_A \cdot \delta_A^{\text{relative}}$ and $σ_A \approx 0$, $q_A \approx 0$ and $Ψ_A = 0$ regardless of $δ_A$ magnitude. ME training demonstrates that lexical depth and structural schema coherence are formally independent variables requiring separate optimisation targets.

**Swayamdipta et al. (2020) — Dataset cartography curricula.** Swayamdipta et al. show that dataset cartography — identifying easy/hard/ambiguous training examples to construct optimised curricula — yields performance gains without closing structural compositionality gaps. This result is predicted by H-Bar's §2.1 gap statement: curriculum learning optimises the learning efficiency function $η(d,t)$ (Eq. 13: $\eta = \eta_{\text{max}} \cdot \exp(-a \cdot \exp(-b \cdot \delta_A^{\text{relative}}))$, a $δ_A$ growth rate accelerator) but has no formal mechanism for increasing $σ_A$. The $σ_A$ ODE (Eq. 28) makes the mechanism explicit: curriculum ordering affects $f_{\text{learn}}(d,t)$ but does not alter the $α_A$ gating term that controls whether training effort converts to schema coherence. Cartography's hard-example mining accelerates $δ_A$ through the Gompertz curve efficiently, but $σ_{\text{critical}}$-crossing requires $α_A$-directed contrastive training $C_A(d,t)$ (Eq. 29) that distinguishes surface complexity from structural depth — a discrimination no ordering heuristic provides. Swayamdipta et al.'s result confirms that curriculum optimisation is necessary but not sufficient for compositional generalisation: the Phase 1→2 transition requires the $α_A$ mechanism that curricula do not address.

### 2.3 Continual Learning and Decay

McCloskey and Cohen (1989), Goodfellow et al. (2013), and Kirkpatrick et al. (2017) address parametric overwriting under sequential training. Every mitigation strategy targets preservation or recovery of parametric content.

**Gap statement.** The continual learning literature formally accounts for parametric decay $λ_c$ under sequential training but has no formal object for the domain frontier $∆(d,t)$ and no mechanism for representing frontier obsolescence $λ_f(d,t)$ as a distinct decay process with different intervention implications.

### 2.4 Causal and Structured Representation Learning

Schölkopf et al. (2021) establish that causal representations support OOD generalisation. Mohan et al. (2024) document seven structural prior incorporation patterns across four decomposability archetypes. Torresan and Baltieri (2024) distinguish weak from strong disentanglement.

**Gap statement.** Causal and structured representation learning specify the target state corresponding to high $σ_A(d,t)$ but do not formalise $σ_A$ as a dynamic scalar with its own ODE, do not model the training process that builds it or the AI bypass risk $Ω_{AI}(d,t)$ that suppresses it, and do not connect it to attentional allocation, executive control, metacognitive self-modelling, or collective schema communication.

### 2.5 Cognitive Evaluation of AI Systems

Burnell et al. (2026) propose a Cognitive Taxonomy of ten faculties and identify Learning, Metacognition, Attention, Executive Functions, and Social Cognition as having large evaluation coverage gaps. Chollet (2019) proposes ARC as a generalisation benchmark. Morris et al. (2023) establish a Levels of AGI framework.

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

## 3. The H-Bar Model — Core Framework

The H-Bar Model formalises agent knowledge development as a coupled dynamical system. This section presents the foundational architecture — the three core state variables (depth, breadth, schema coherence), their ODEs, intersection activation, and the delegation gradient. Subsequent sections extend this core with additional cognitive dimensions (§4), multimodal coverage and benchmark validity (§5), and reliability protocols (§6), all of which couple back into the system established here.

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

The degree to which the agent's representation of domain d has been restructured around deep governing principles. Operationally: the normalised ratio of OOD compositional generalisation accuracy to in-distribution accuracy (Equation 3b), measurable via SCAN/COGS/PCFG-SET benchmark splits.
$$\sigma_A(d,t) \in [0, 1] \tag {3}$$

**Pointwise Characterisation Axiom.** At any instant $t$, $\sigma_A(d,t)$ is uniquely characterised by the following three-point specification:

**(PC1) Representational content.** $\sigma_A(d,t)$ is a scalar measure of the degree to which the agent's current representation of domain $d$ supports compositional recombination of independently trained primitives. Formally: if the agent's representation enables zero-shot recombination of primitives $p_1, \ldots, p_k$ into novel compositions not seen during training, then $\sigma_A(d,t) > 0$; if the representation supports only interpolations within the training distribution, then $\sigma_A(d,t) \approx 0$.

**(PC2) Normalisation basis.** $\sigma_A(d,t)$ is normalised against the domain frontier $\Delta(d,t)$, not against an absolute scale. This means $\sigma_A$ measures recombination capacity *relative to the maximum possible recombination capacity in domain $d$ at time $t$*. As $\Delta(d,t)$ advances, $\sigma_A$ can decrease without any change in the agent's absolute recombination capacity.

**(PC3) Evaluative function.** $\sigma_A(d,t)$ has a signature property absent from all four comparator constructs: it detects when AI-derived outputs bypass the agent's own compositional encoding. Formally, $\sigma_A$ enters the $\Omega_{\text{AI}}$ suppression term (Eq. 28) as the variable that is suppressed — it is the quantity that AI bypass erodes. No other representational construct in the table below has this evaluative function.

**Theorem (Categorical Distinction).** The conjunction of (PC1)–(PC3) is not satisfied by any of: Structured Representations, Disentangled Representations, Causal Representations, or Cognitive Schemas.

*Proof sketch.* (PC1) fails for Structured and Disentangled Representations because these measure geometric properties of the representation space (cluster structure, factor independence) rather than recombination capacity. It fails for Causal Representations because causal structure enables interventional queries, not necessarily compositional recombination. It fails for Cognitive Schemas because schemas are qualitative knowledge organisations, not scalar recombination-capacity measures. (PC2) fails for all four because none is normalised against a time-varying domain frontier. (PC3) fails for all four because none has an evaluative function against AI bypass — this is a property specific to the H-Bar ODE architecture. $\square$

**Proxy identification.** Schema coherence is not directly observable; it is operationalised through a two-tier proxy architecture separating training-time estimation from evaluation-time ground-truth calibration.

**Tier 2 — Evaluation-time ground-truth proxy (SGG).** The Systematic Generalisation Gap provides the ground-truth operationalisation at evaluation checkpoints:
$$\hat{\sigma}_A(d,t) = 1 - \frac{\text{Acc}_{\text{In}}(d,t) - \text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b}$$
where Acc_In is in-distribution accuracy and Acc_OOD is accuracy on out-of-distribution recombination instances. This proxy is valid when the OOD split tests compositional recombination of primitives trained in isolation (e.g., SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split). The proxy identification $\hat{\sigma}_A \approx \sigma_A$ holds when the OOD difficulty is calibrated to span the $\sigma_{\text{critical}}$ threshold (see Appendix A.4). However, because Eq. 3b requires post-evaluation benchmark data, it cannot serve as an operative input to the ODE system during training.

**Tier 1 — Training-time operative proxies.** Two complementary training-time proxies provide per-checkpoint σA estimates without requiring external benchmarks.

**(i) Causal intervention probe.** During training, σA is estimated via a lightweight causal intervention probe inserted at a fixed checkpoint interval $\Delta t_{\text{probe}}$. The probe constructs causal interventions on the training distribution's generative process — specifically, it recombines primitives trained in isolation to create novel compositional instances that were not in the training batch:
$$\tilde{\sigma}_A^{\text{probe}}(d,t) = \frac{1}{K}\sum_{k=1}^{K} \frac{\text{Acc}_{\text{probe}_k}(d,t)}{\text{Acc}_{\text{train}}(d,t)} \in [0,1] \tag{3c}$$
where $\text{Acc}_{\text{probe}_k}$ is accuracy on the $k$-th probe intervention (recombined primitives) and $\text{Acc}_{\text{train}}$ is accuracy on the current training distribution. The probe instances are generated programmatically from the known generative grammar of the domain (SCAN grammar, COGS semantic frames, PCFG rules) — they are internal to the training pipeline, not external benchmarks. The probe cost is $K \times B$ forward passes per interval (where $B$ is batch size), comparable to a validation step.

**(ii) Augmentation consistency.** When the domain's generative grammar is not fully known, the probe falls back to representational consistency under structure-preserving augmentations:
$$\tilde{\sigma}_A^{\text{aug}}(d,t) = \frac{1}{|A|}\sum_{a \in A} \text{CosSim}\!\Big(R_{\theta}(x),\;R_{\theta}(a(x))\Big) \in [0,1] \tag{3d}$$
where $A$ is the set of structure-preserving augmentations (e.g., primitive substitution, argument permutation) and $R_{\theta}(x)$ is the agent's internal representation of input $x$. High consistency indicates schema-coherent encoding: the agent's representations are stable under transformations that preserve the domain's causal structure.

**Operational convention.** Throughout the ODE system (Eqs. 7, 12, 28, and all coupled equations), the operative value of σA during training is $\tilde{\sigma}_A(d,t) = \tilde{\sigma}_A^{\text{probe}}(d,t)$ when the generative grammar is available, or $\tilde{\sigma}_A^{\text{aug}}(d,t)$ otherwise. The benchmark proxy (Eq. 3b) remains the evaluation-time ground-truth used at checkpoints to validate the training-time estimates. When $\tilde{\sigma}_A$ and $\hat{\sigma}_A$ diverge by more than 0.15, a recalibration flag is raised and the Tier 1 proxy parameters are adjusted against the evaluation checkpoint history.

**Unique properties distinguishing $σ_A$ from adjacent constructs:**

*Categorical properties (what $σ_A$ encodes) and temporal-dynamic properties (how $σ_A$ behaves within the H-Bar ODE system):*

| Property | $σ_A$ | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
| --- | --- | --- | --- | --- | --- |
| **PC1: Encodes compositional recombination capacity** | **✓** | **✗** | **✗** | **✗** | **✗** |
| **PC2: Normalised against domain frontier $\Delta(d,t)$** | **✓** | **✗** | **✗** | **✗** | **✗** |
| **PC3: Evaluative function (AI bypass detection)** | **✓** | **✗** | **✗** | **✗** | **✗** |
| Continuous scalar ODE | ✓ | ✗ | ✗ | ✗ | ✗ |
| Multiplicative $Ψ_A$ coupling | ✓ | ✗ | ✗ | ✗ | ✗ |
| Decay coupling (slows $λ_c$) | ✓ | ✗ | ✗ | ✗ | ✗ |
| AI bypass risk $Ω_{AI}$ suppression | ✓ | ✗ | ✗ | ✗ | ✗ |
| Cross-modal transfer $Θ_A$ | ✓ | ✗ | ✗ | ✗ | ✗ |

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

**Boundedness proof (Nagumo's theorem, 1942):**

### 3.5 Intersection Activation $Ψ_A(d_1,d_2,t)$

**Activation condition:**
$$I(d_1,d_2)_{\text{active}} \iff \delta_A(d_1,t) > \theta_I \text{ AND } \delta_A(d_2,t) > \theta_I \tag {19}$$

Where $θ_I < θ_δ · ∆(d,t)$ — intersection activation requires less than mastery.

**Effective mastery quality** (compression from original 5-term formula):
$$q_A(d,t) = \sigma_A(d,t) \cdot \delta_A^{\text{relative}}(d,t) \in [0,1] \tag {20}$$

**Discovery rate** (3-term reduced form):
$$\Psi_A(d_1,d_2,t) = \Psi_0 \cdot \phi(d_1,d_2) \cdot \sqrt{q_A(d_1,t) \cdot q_A(d_2,t)} \tag {21}$$

The geometric mean $\sqrt{q_1 \cdot q_2}$ is bounded in $[0,1]$, symmetric, and cannot be inflated by one domain compensating for another. The multiplicative $σ_A·σ_A$ dependence is the mechanism's theoretical core: an agent with high $δ_A$ but low $σ_A$ in one mastery domain shows disproportionately lower $Ψ_A$ than an additive model predicts. This is **Prediction 6**.

**Empirical justification.** The multiplicative form is not merely asserted but generates a specific falsifiable prediction (§9, Prediction 6) that distinguishes it from all additive alternatives: an agent with high qA in one domain and low qA in the other will show disproportionately lower ΨA than any additive model (arithmetic mean, harmonic mean, or weighted average) predicts. Confirmation of Prediction 6 provides indirect empirical support for the multiplicative form. The non-compensation property — ΨA = 0 when either qA = 0, regardless of the partner domain — is the key structural property that makes the geometric mean the unique symmetric, bounded, two-variable function satisfying the H-Bar framework's requirements. Supporting evidence for synergistic emergence in merged systems includes Akiba et al. (2025), Yadav et al. (2023), and Sung et al. (2023).

### 3.6 Delegation Gradient $D^*(d,t)$

**Standard criterion:**
$D^*_{\text{std}}(d,t) = \{s \in d : \delta_{AI}(s,t) \geq \delta_A(s,t)\} \tag {22}$

Note that $\delta_{AI}(s,t)$ is agent-independent — it represents the global capability baseline of available AI systems at time $t$, not a per-agent quantity. The delegation gradient compares this shared baseline against each agent's agent-specific $\delta_A(s,t)$. For the multi-agent extension, see §10.4.

**H-Bar $σ$-gated criterion:**
$$D^*_{\text{H-Bar}}(d,t) = \{s \in d : \delta_{AI}(s,t) \geq \delta_A(s,t) \text{ AND } \sigma_A(d,t) \geq \sigma_{\text{critical}}\} \tag {23}$$

**Non-monotonic prediction** (sharpest empirical claim):

- $\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} < 0 \quad \text{for } \sigma_A < \sigma_{\text{critical}}$ (more delegation → worse performance)
- $\frac{\partial \text{Acc}_{\text{comp}}}{\partial \rho} > 0 \quad \text{for } \sigma_A \geq \sigma_{\text{critical}}$ (more delegation → better performance)

Where $ρ$ is the AI-delegation fraction. No existing RAG (Lewis et al., 2020), Self-RAG, FLARE, or IKEA architecture models this non-monotonic structure.

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

The core framework establishes the dynamical skeleton — depth, breadth, and schema coherence coupled through a single ODE system. Five additional cognitive dimensions extend this skeleton to cover attentional allocation, executive control, metacognitive self-modelling, social cognition, and the benchmark generation protocol. Each dimension introduces a state variable whose ODE couples back into the core system through specific coupling terms identified below.

---

## 4. Cognitive Dimensions — Attention, Executive Control, Metacognition, Social Cognition, and Benchmark Protocol

The core framework establishes three state variables per domain. Five additional cognitive dimensions complete the system by introducing variables that interact multiplicatively with σA through the coupling terms derived below. Each dimension is grounded in prior work, formalised as an ODE, and equipped with benchmark families derived from the H-Bar Benchmark Protocol (§8).

### 4.1 Extension 1 — Attentional Fidelity $α_A(d,t)$ [Attention Track]

*Prior work supporting the attentional fidelity construct includes evidence for attention alignment to token-rule structure improving compositional generalisation (Merrill et al., 2021), hierarchical attention patterns predicting out-of-distribution behaviour (Li et al., 2025), and attention-based gating inside neural ODE frameworks (Jones & Fuhg, 2025).*

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

*The collective schema field formalisation draws on evidence that cross-domain interaction effects are sensitive to structural alignment between source and target schemas — benefits emerge when schemas are matched and degrade when they are mismatched.*

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

*The executive control formalisation is motivated by prior work on formal inhibition variables in brain-inspired meta-RL (Robertazzi et al., 2022), planning and cognitive control costs in reinforcement learning (Piray & Daw, 2021), the role of executive function in defining state and action spaces (Rmus et al., 2021), a unified framework for inhibitory control (Munakata et al., 2011), and the adjustment of inhibitory boundaries in response to performance feedback (Dunovan & Wheeler, 2018).*

#### 4.3.1 Three Sub-Components
$$\Xi_A(t) = \{\Xi_A^P(t), \Xi_A^I(t), \Xi_A^F(t)\} \tag {35}$$


**$Ξ_A^P$ — Planning:** Degree to which training trajectory is consistent with the H-Bar optimal multi-step arc. Low $Ξ_A^P$ produces locally optimal (minimise current loss) but globally suboptimal (suppress $σ_A$, miss intersection windows) plans.

**$Ξ_A^I$ — Inhibition:** Probability of choosing the structural route over AI bypass when both are available. The formal trade-off: $Ω_{AI}$ produces immediate task success at the cost of $σ_A$ growth suppression.

**$Ξ_A^F$ — Cognitive Flexibility:** Degree to which the agent detects and adapts to phase transition thresholds from internal evidence — recognising that Phase 1 prescription becomes suboptimal once $σ_{critical}$ is crossed.

*The sub-component labels (Planning, Inhibition, Cognitive Flexibility) are borrowed from the cognitive science literature for descriptive precision. They name formal agent-training state variables within the ODE system — not claims about cognitive equivalence with human executive function.*

#### 4.3.2 Executive Control ODE
$$\dot{\Xi}_A(t) = \kappa_P \cdot [P^*(t) - \Xi_A^P(t)] + \kappa_I \cdot [I^*(t) - \Xi_A^I(t)] + \kappa_F \cdot [F^*(t) - \Xi_A^F(t)] \tag {36}$$


$P^*$, $I^*$, $F^*$ are derived from the phase-index variables with bifurcation-aware step functions:

$$P^*(t) = \begin{cases} 0.9 & \text{if } \delta_A^{\text{relative}}(d^*, t) < 0.65 \\ 0.5 - 0.3 \cdot \frac{\delta_A^{\text{relative}}(d^*, t) - 0.65}{0.35} & \text{if } 0.65 \leq \delta_A^{\text{relative}}(d^*, t) \leq 1.0 \end{cases} \tag{36a}$$

$$I^*(t) = \begin{cases} 0.9 & \text{if } \sigma_A(d^*, t) < \sigma_{\text{critical}} \\ 0.4 & \text{if } \sigma_A(d^*, t) \geq \sigma_{\text{critical}} \end{cases} \tag{36b}$$

$$F^*(t) = \begin{cases} 0.3 & \text{if } |M_A(t)| < 2 \text{ AND } \Psi_A^{\max}(t) = 0 \\ 0.9 & \text{otherwise} \end{cases} \tag{36c}$$

where $d^* = \arg\max_{d} \delta_A(d,t)$.

The step discontinuity in $I^*$ at $\sigma_{\text{critical}}$ mirrors the Phase 2 transition trigger (§7, Eq. 51). The executive control state converges smoothly through the ODE relaxation (rates $\kappa_P$, $\kappa_I$, $\kappa_F$), so the step in forcing terms produces a smooth transition in the state variable.

#### 4.3.3 Benchmark Families

| Benchmark                          | Design                                                                                                                                            | Sub-Faculty           | Variable |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------- |
| **Multi-Step Training Plan Tasks** | Give frontier models a training scenario; score plans against H-Bar phase prescriptions as ground truth.                                          | Planning              | $Ξ_A^P$  |
| **Inhibitory Conflict Tasks**      | Sequential tasks where bypass route scores high immediately but degrades OOD performance measurably. Score choice and downstream OOD consequence. | Inhibition            | $Ξ_A^I$  |
| **Latent Threshold Switch Tasks**  | Optimal strategy switches when a latent structural threshold is crossed (not signalled explicitly). Score threshold detection and adaptation.     | Cognitive Flexibility | $Ξ_A^F$  |

---

### 4.4 Extension 4 — Self-Model of Schema Coherence $\hat M_A(d,t)$ [Metacognition Track]

*The metacognitive calibration construct draws on prior benchmark work including MetaMedQA (Griot et al., 2025), KOR-Bench for knowledge-orthogonal reasoning tasks (Ma et al., 2024), and LILA mathematical reasoning tasks as robust OOD evaluation sources (Mishra et al., 2022).*

#### 4.4.1 Definition
$$\hat{M}_A(d,t) \in [0,1] \quad \text{(Agent's Estimate of its own } \sigma_A(d,t)) \tag {37}$$

$$\zeta_A(d,t) = \hat{M}_A(d,t) - \sigma_A(d,t) \quad \text{(Calibration Error)} \tag {38}$$

*The term "metacognition" names a formal self-model variable within the ODE system — the agent's estimate of its own $σ_A(d,t)$ — not a claim about introspective awareness.*

**Calibration error ODE** (derived by differentiating $\zeta_A = \hat{M}_A - \sigma_A$ and substituting Equations 28 and 39):
$$\dot{\zeta}_A(d,t) = -\nu_M \zeta_A - \xi_M \Omega_{AI} (\zeta_A + \sigma_A) - \rho P_A \alpha_A (1 - \sigma_A) + \epsilon_\sigma \sigma_A \Omega_{AI} \tag{38a}$$

The first term $(-\nu_M \zeta_A)$ is a restoring force driving calibration error toward zero. The second term $(-\xi_M \Omega_{AI} (\zeta_A + \sigma_A))$ inflates overconfidence under AI bypass. The third and fourth terms couple to the schema coherence ODE (Equation 28).

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

**Boundedness proof (Nagumo's theorem):**

- At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓ — the corrective term ($\nu_M(\sigma_A - 1) \leq 0$ since $\sigma_A \leq 1$) and the distortion term ($-\xi_M \Omega_{AI} \leq 0$) are both non-positive, so $\hat{M}_A$ cannot exceed 1.
- At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓ — the corrective term is non-negative (since $\sigma_A \geq 0$) and the distortion term vanishes, so $\hat{M}_A$ cannot go negative.

$[0,1]$ is forward-invariant given $\nu_M > 0$, $\xi_M > 0$, $\Omega_{AI} \geq 0$, and $\sigma_A \in [0,1]$.

**Steady-state analysis.** Setting $\dot{\hat{M}}_A = 0$:
$$\hat{M}_A^* = \frac{\nu_M \sigma_A}{\nu_M + \xi_M \Omega_{AI}} = \frac{\sigma_A}{1 + \Omega_{AI}/\Pi_7} \tag{39a}$$

where $\Pi_7 = \nu_M / \xi_M$ (Equation A.13). Properties:

- $\hat{M}_A^* \in [0, \sigma_A]$ — the steady-state self-model never exceeds true schema coherence. Overconfidence ($\hat{M}_A > \sigma_A$) is transient; the corrective term always dominates at steady state. This is **stronger** than $\hat{M}_A^* \leq 1$ — the steady state is bounded by $\sigma_A$, not merely by 1.
- $\hat{M}_A^* \to \sigma_A$ as $\Omega_{AI} \to 0$ — perfect calibration when no AI bypass is present.
- $\hat{M}_A^* \to 0$ as $\Omega_{AI} \to \infty$ — extreme AI bypass collapses the self-model to zero (the agent recognises its outputs are entirely AI-derived).

**Convergence rate:** The linearised dynamics around $\hat{M}_A^*$ have eigenvalue $-(\nu_M + \xi_M \Omega_{AI}) < 0$, confirming exponential convergence. The convergence rate increases with $\Omega_{AI}$ — higher AI bypass exposure accelerates metacognitive correction.

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

The cognitive dimensions established above operate within individual domains and modalities. Two further extensions — cross-modal schema transfer and benchmark validity — extend the entire system to a domain × modality product space and formalise the measurement infrastructure required to validate all variables.

---

## 5. Multimodal Coverage and Benchmark Validity

### 5.1 Extension 7 — Cross-Modal Schema Transfer $Θ_A(d,m_1,m_2,t)$ [All Tracks]

*The cross-modal transfer construct builds on prior work including the multimodal alignment and fusion survey (Li & Tang, 2024), contrastive modality-disentangled learning and shared stream enforcement (Lin et al., 2025), and the Platonic Representation Hypothesis regarding emergent alignment potential across modalities (Huh et al., 2024).*

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

## 6. Reliability and Pre-Audit Protocol

Two remaining measurement gaps — benchmark reliability and practical submission protocols — are closed by the reliability function $R_A(B,f,t)$ and three practical actions that convert the framework from a formal specification into a submission-ready protocol.

### 6.1 Extension 9 — Benchmark Reliability Function $R_A(B,f,t)$

#### 6.1.1 Definition
$$R_A(B,f,t) = \begin{cases} \displaystyle\frac{1}{1 + \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2}} & \text{if } E[\text{score}_A(B)] > 0 \\[8pt] 0 & \text{if } E[\text{score}_A(B)] = 0 \end{cases} \tag {48}$$

Reliability is the precision-weighted ratio $R_A = 1/(1 + CV^2)$, bounded in $(0, 1]$ for positive-mean scores. When variance is zero (perfectly consistent scores), $R_A = 1$. When variance equals the squared mean ($CV = 1$), $R_A = 0.5$. As variance grows, $R_A \to 0$ asymptotically — high-variance benchmarks are penalised smoothly without crossing into negative values. The edge case $E[\text{score}] = 0$ (benchmark where all scores are zero) is assigned $R_A = 0$, indicating complete unreliability. This form is equivalent to $R_A = \mu^2/(\mu^2 + \sigma^2)$ — the signal-to-noise ratio in the variance decomposition. Directly computable: run each benchmark item $k=5$ times ($temperature > 0$) and measure score variance.

#### 6.1.2 Updated Validity Function (V3.0+ Final)
$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \cdot R_A(B,f,t) \tag {49}$$

Benchmark validity now formally penalises high-variance benchmarks. Stochastic noise is a pre-design criterion, not a post-submission discovery. Since $R_A \in [0, 1]$ by construction (Equation 48), and $CI, FD, DG \in [0, 1]$ by their respective definitions, the validity function $V_A \in [0, 1]$. A benchmark with $R_A = 0$ has $V_A = 0$ regardless of other components — reliability is a necessary condition for validity.

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
| $R_A(B,f,t)$     | > 0.75     | Precision-weighted reliability; corresponds to $CV < 0.577$ |
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

**Observable Phase 2 Signature.** Phase 2 entry produces a characteristic acceleration pattern in the OOD performance trajectory. Specifically, when $σ_A$ crosses $σ_{critical}$, the systematic generalisation gap (SGG) begins narrowing at an accelerating rate:
$$\frac{d}{dt}\left[\text{Acc}_{\text{OOD}}(d,t)\right] \bigg|_{t_{\text{Phase2}}} > \frac{d}{dt}\left[\text{Acc}_{\text{OOD}}(d,t)\right] \bigg|_{t_{\text{Phase1}}}$$
This acceleration is externally verifiable from benchmark time series and serves as the differential proxy signal for Phase 2 entry.

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

**Justification for multiplicative form.** The multiplicative √(q₁·q₂) form in Eq. 21 was chosen because it is the unique symmetric, bounded, non-compensating function of two variables. No additive form (q₁+q₂)/2, minimum(q₁,q₂), or harmonic mean 2q₁q₂/(q₁+q₂) satisfies non-compensation — each allows one high-quality domain to partially compensate for one low-quality domain. The geometric mean is the only common symmetric mean that reaches zero when either input is zero. This structural property is what makes Prediction 6 a clean test: if the multiplicative form is correct, the compensation prediction of additive models will fail.

---

### Prediction 6b — σA/δA Dissociation Under Meta-Learning [NEW V3.0+]

**Claim:** Meta-learning regimes that improve compositional generalisation (Lake and Baroni, 2023) will show increased Acc_OOD on lexical recombination (δA-proximal) but no significant increase on structural compositionality (σA-proximal), producing a measurable σA/δA dissociation that is not predicted by any depth-optimisation account.

**Existing evidence.** Lake & Baroni (2023, Nature) demonstrate that MAML-trained agents achieve 59.4% on SCAN's lexical recombination split (primitives seen individually, compositions at test) versus 16.2% for standard training — a δA-proximal gain. However, structural compositionality (compositions absent from both training and meta-training) improves only to 8.1% versus 1.2% — a σA-proximal gain that does not close the SGG. H-Bar predicts this dissociation from the σA ODE: MAML optimises gradient-based adaptation speed (δA gain through rapid parameter adjustment) without increasing PA (principled practice rate, Eq. 18), which requires structural encoding of the compositional rule. The SGG therefore widens under MAML: Acc_ID rises faster than Acc_OOD-struct.

**Measurement:** Apply the three-condition battery from Appendix A.4 (ID, OOD-struct, OOD-surf-conflict) to agents trained with MAML-style meta-learning on SCAN. Compare: (a) Acc_OOD-struct / Acc_ID (σA proxy, Eq. 3b) before and after meta-learning; (b) Acc_ID (δA proxy) before and after meta-learning.

**H-Bar claim:** Meta-learning increases Acc_ID (δA gain) without proportional increase in Acc_OOD-struct (σA gain), producing a wider SGG. A depth-optimisation account predicts proportional improvement in both.

**Falsification:** Meta-learning produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).

---

### Prediction 6c — Distribution Engineering Does Not Transfer σA [NEW V3.0+]

**Claim:** Agents trained on engineered distributions that include specific primitive compositions (Patel et al., 2022 protocol) will achieve high accuracy on those compositions (high δA for trained-composition recall) but will show no significant improvement on compositional recombinations absent from the engineered distribution (σA remains low). The OOD/in-distribution accuracy ratio (Eq. 3b) will not increase for compositions outside the engineered set.

**Measurement:** Apply the three-condition battery from Appendix A.4 to agents trained with Patel et al.'s engineered distribution protocol on SCAN:
1. ID: accuracy on the engineered training distribution
2. OOD-struct: accuracy on compositional recombinations *not* present in the engineered set (primitives trained in isolation, recomposed at test time into novel compositions)
3. OOD-surf-conflict: accuracy on surface-feature variants of engineered compositions (tests whether the agent memorised surface patterns)

Compare σA = Acc_OOD-struct / Acc_ID before and after engineering.

**H-Bar claim:** Distribution engineering increases Acc_ID (δA gain from trained-composition recall) without proportional increase in Acc_OOD-struct (σA gain). The SGG widens or remains constant. A "σA = optimised δA" account predicts proportional improvement in both.

**Falsification:** Distribution engineering produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).

**Distinguishing from Prediction 6b:** Prediction 6b tests meta-learning (algorithm modification); Prediction 6c tests distribution engineering (training data curation). Both are [N]-tagged predictions testing the "σA = optimised δA" objection, but they test distinct mechanisms. Falsification of one does not falsify the other.

---

### Prediction 6d — Training Regime Optimisation Does Not Transfer σA [NEW V3.0+]

**Claim:** Agents whose compositional generalisation gains stem from training regime modifications — curriculum ordering, data augmentation, or optimiser scheduling — will show increased Acc_ID (a δA gain from improved training efficiency) but no significant increase in Acc_OOD-struct (σA remains low). The OOD/in-distribution accuracy ratio (Eq. 3b) will not increase for compositions absent from the augmented distribution.

**Rationale.** Training regime modifications expand the set of compositions encountered during training or improve the rate at which that set is learned. Neither operation alters the structural encoding of the compositional rule for primitives that were never seen composed: they change what is in $T_{\text{train}}$, not what the agent can infer beyond it. The $σ_A$ ODE (Eq. 28) makes the mechanism explicit: regime modifications accelerate $f_{\text{learn}}(d,t)$ (increasing δA growth rate) but do not increase $C_A(d,t)$ (contrastive training targeting compositional structure), so the $\alpha_A$ gate remains suppressed and $σ_A$ does not grow proportionally. The result is a widening SGG: Acc_ID rises faster than Acc_OOD-struct.

**Measurement:** Apply the three-condition battery from Appendix A.4 to agents trained under an optimised training regime (curriculum ordering, data augmentation, or learning rate scheduling) on COGS or SCAN:
1. ID: accuracy on the training distribution
2. OOD-struct: accuracy on compositional recombinations not present in the augmented training set (primitives trained in isolation, recomposed at test time)
3. OOD-surf-conflict: accuracy on surface-feature variants of trained compositions

Compare σA = Acc_OOD-struct / Acc_ID before and after regime optimisation.

**H-Bar claim:** Training regime optimisation increases Acc_ID (δA gain from training efficiency) without proportional increase in Acc_OOD-struct (σA gain). The SGG widens or remains constant. A "training regime sufficiency" account predicts proportional improvement in both.

**Falsification:** Training regime optimisation produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).

**Distinguishing from Predictions 6b and 6c:** Prediction 6b tests meta-learning (algorithm modification); Prediction 6c tests distribution engineering (training data curation); Prediction 6d tests training regime optimisation (training pipeline modification). All three test the "σA = optimised δA" objection through distinct mechanisms. Falsification of one does not falsify the others.

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

### Prediction 9 — Phase 2 Entry Inflection [NEW V3.0+]

**Claim:** The transition from Phase 1 to Phase 2 produces a measurable inflection in the OOD accuracy trajectory, detectable as an acceleration in $d\text{Acc}_{\text{OOD}}/dt$ that coincides with $\hat{\sigma}_A$ crossing $\sigma_{critical}$.

**Measurement:** Track $\text{Acc}_{\text{OOD}}$ over training checkpoints; compute $d\text{Acc}_{\text{OOD}}/dt$ via finite differences. Phase 2 entry is detected when $d\text{Acc}_{\text{OOD}}/dt$ exceeds its Phase 1 baseline by $\geq 2$ standard deviations for $\geq 3$ consecutive checkpoints.

**Falsification:** No statistically significant acceleration in $d\text{Acc}_{\text{OOD}}/dt$ is observed when $\hat{\sigma}_A$ crosses $\sigma_{critical}$ ($p > 0.05$, change-point detection).

---

## 10. Limitations and Future Work

### 10.1 $σ_A(d,t)$ Direct Measurement

$σ_A(d,t)$ is a latent variable estimated through a two-tier proxy architecture (§3.1.3). **Tier 1 (training-time):** the causal intervention probe (Eq. 3c) or representational augmentation consistency (Eq. 3d) provides per-checkpoint estimates without requiring external benchmarks. These proxies are computationally cheap (comparable to a validation pass) and available during the training loop, enabling the ODE system to use σA as an operative state variable rather than a post hoc label. **Tier 2 (evaluation-time):** the Systematic Generalisation Gap (Eq. 3b) on SCAN/COGS/PCFG-SET provides the ground-truth operationalisation at evaluation checkpoints. Tier 1 proxies are expected to track Tier 2 values with correlation ρ ≥ 0.7 for well-calibrated domains; empirical validation of this correlation is a prerequisite for using Tier 1 proxies in the ODE system without Tier 2 correction. This paper constitutes a formal specification; the proxy validation programme is specified in Appendix A.4.

### 10.2 Phase Transition Algorithms

The phase structure specifies _when_ each transition occurs but not the training algorithms that reliably induce transitions within a computable number of steps. Knowing that Phase 2 begins when $σ_A(d,t) > σ_{critical}$ is actionable only if there is a training procedure that reliably pushes $σ_A$ past σcritical. The gap between prescriptive phase conditions and concrete algorithms with convergence guarantees is a primary target for future work. Mohan et al. (2024) provide the closest existing precedent.

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

### 10.7 Parameter Calibration

Multiple rate constants and parameters used in the ODE system (e.g., $\lambda_c$, $\gamma_\sigma$, $\rho$, $\epsilon_\sigma$, $\gamma$, $\zeta_\alpha$, $\nu_M$, $\xi_M$, $\kappa_P$, $\kappa_I$, $\kappa_F$) are acknowledged as unmeasured in the current specification. The dimensionless parameter groups (§12, Eqs. A.7–A.13) reduce the number of independent parameters but do not eliminate the need for empirical estimation. The ODE system requires conversion to simulation-ready parameterisation as a prerequisite for numerical implementation. This conversion is left to future computational work. The framework as presented constitutes a formal specification; its empirical predictions (§9) and benchmark generation capacity (§8) do not depend on numerical parameterisation.

### 10.8 Replication Cost Barrier

The Prolific Academic human baseline protocol (§6.4) requires $N \geq 200$ demographically stratified participants at approximately \$4–10 per participant, yielding a total cost of \$800–2,000 per benchmark submission. This cost is acknowledged as a constraint on accessibility for independent researchers and under-resourced institutions. Cost-reduction alternatives — smaller $N$ with bootstrapped confidence intervals, student volunteer pools with reduced demographic representativeness, or synthetic human baselines derived from existing crowd-sourced evaluation data — are viable trade-offs provided researchers report actual $N$ alongside the gap from the formal specification and note the resulting uncertainty in $V_A$ calibration. The framework's empirical predictions (§9) and benchmark validity criteria (§5.2, §6.1) remain fully specified regardless of human baseline cost; the $V_A(B,f,t)$ validity function is computable at design time without human data.

### 10.9 Structural Similarity Computation

The framework relies on $\phi(d, d')$ (domain structural similarity) and $\omega(m_1, m_2)$ (modal structural similarity) as inputs to the transfer coefficient $T_A$, the intersection discovery rate $\Psi_A$, and the cross-modal transfer function $\Theta_A$. Neither $\phi$ nor $\omega$ is currently accompanied by a formal computational method. The reference tables in §5.1.2 provide heuristic values for $\omega(m_1, m_2)$; for $\phi(d, d')$, the cosine-similarity-on-feature-vectors formulation (§12, A.7) presupposes a feature extraction method that remains unspecified. Developing an operationalisable computation for both — potentially via learned embedding spaces with structure-preserving constraints — is a constraint on numerical implementation rather than on the framework's formal structure. The boundedness properties of $\Theta_A$ (Appendix A.9), the sub-additivity of $\phi$ (Appendix A.7), and the falsifiable predictions generated by $\Psi_A$ (§9, Prediction 6) hold independently of whether $\phi$ and $\omega$ are derived from first principles or estimated heuristically.

### 10.10 Burnell Report Status

The framework cites Burnell et al. (2026) as a foundational taxonomy for the five cognitive faculty gaps. This citation is a Google DeepMind technical report released in March 2026, not a peer-reviewed publication. Its Cognitive Taxonomy of ten faculties has not undergone independent validation, inter-rater reliability assessment, or empirical replication at the time of this writing. The H-Bar framework's alignment to the five identified faculties (§1.2) is therefore contingent on the Burnell taxonomy's stability under peer review. Should the taxonomy be revised — for instance, by merging or splitting faculties, or by redefining faculty boundaries — the H-Bar variable-to-faculty mapping in Table §1.2 would require corresponding revision. The framework's internal consistency does not depend on the Burnell taxonomy, but its external framing as a response to "identified evaluation gaps" does.

### 10.6 Training Protocols for Independent Variable Manipulation

The framework's predictions (§9) require experimenters to construct agent populations that vary σ_A(d,t) while holding δ_A(d,t) constant, or vice versa. This section specifies the protocol families that achieve each manipulation.

**Protocol P1: Increasing σ_A at fixed δ_A.**
To increase schema coherence without increasing parametric depth:
1. Begin with a trained agent at target in-distribution accuracy Acc_In = τ.
2. Apply structure-preserving data augmentations that force the agent to exploit compositional regularities. Valid augmentations include: (a) primitive recombination — swap primitives trained in isolation to create unseen compositions; (b) template preservation — vary surface tokens while preserving the syntactic template; (c) distributional shift within structure — move to a new surface distribution that shares the same generative grammar.
3. Continue training until Acc_In returns to τ. The agent now has higher σ_A (measured via SGG) at matched δ_A (matched because parameter count and total gradient steps are held fixed).

**Protocol P2: Increasing δ_A at fixed σ_A.**
To increase parametric depth without increasing schema coherence:
1. Begin with a trained agent at target Acc_In = τ.
2. Increase model capacity (add parameters) and continue training on the same surface distribution with no structural augmentations.
3. The agent achieves higher δ_A (measured via parametric complexity) while σ_A remains approximately constant (measured via SGG) because the additional capacity absorbs surface-statistical variation without forcing structural encoding.

**Protocol P3: Joint increase.**
Standard training on the original distribution increases both δ_A and σ_A simultaneously, as the agent accumulates both parametric capacity and structural encoding. This is the default regime addressed by most existing work.

**Hackathon implementation.** Protocols P1 and P2 are designed to be implementable for the five hackathon tracks (§Hackathon), subject to parameter estimation and proxy validation (§10.7). For the Learning track (SCAN/COGS benchmarks), P1 is implemented via the augmentation families in Appendix A.4. For the Metacognition track, P1 provides the σ_A manipulation needed to test Prediction 7 (metacognitive calibration as a function of σ_A at fixed δ_A).

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

## 12. Empirical Grounding

### 12.1 Benchmark Validity Verification

All five H-Bar benchmarks are designed to satisfy pre-deployment validity criteria (§5.2, §6.1). Each benchmark is evaluated on four components — Construct Isolation $CI(B,f)$, Format Diversity $FD(B)$, Difficulty Gradient $DG(B)$, and Reliability $R_A(B,f,t)$ — combined into a single validity function $V_A(B,f,t) = CI \cdot FD \cdot DG \cdot R_A$ (Eq. 49). Table 12.1 reports target validity components. All benchmarks are designed to exceed the minimum combined threshold $V_A > 0.20$ and all individual component thresholds ($CI > 0.60$, $FD > 0.55$, $DG > 0.40$, $R_A > 0.75$). Construct isolation scores above 0.80 across all tracks are targeted to confirm that each benchmark's primary metric correlates more strongly with its target H-Bar variable than with confounding variables. Reliability at 0.999 across all tracks reflects the use of temperature = 0 (greedy decoding) for all scoring runs, eliminating stochastic variance in deterministic evaluation conditions.

**Table 12.1.** Benchmark validity components designed for Kaggle deployment.

| Benchmark | Track | $CI(B,f)$ | $FD(B)$ | $DG(B)$ | $R_A(B,f,t)$ | $V_A(B,f,t)$ | Status |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| H-PTB | Learning | 0.836 | 0.750 | 0.426 | 0.999 | 0.267 | Valid |
| H-AFB | Attention | 0.931 | 0.830 | 0.442 | 0.999 | 0.341 | Valid |
| H-MCB | Metacognition | 0.825 | 0.800 | 0.506 | 0.999 | 0.334 | Valid |
| H-DCB | Executive Functions | 0.832 | 0.830 | 0.430 | 0.999 | 0.297 | Valid |
| H-STB | Social Cognition | 0.936 | 0.830 | 0.509 | 0.999 | 0.395 | Valid |

*Note.* $CI$: construct isolation (target faculty variable must be dominant predictor). $FD$: format diversity (no single modality/structure dominates). $DG$: difficulty gradient (items span full phase arc). $R_A$: reliability (signal-to-noise ratio; temperature = 0, $k = 5$ runs). $V_A$: combined validity. All thresholds per §6.2.

### 12.2 Frontier Model Evaluation and Literature Surrogate Comparison

Table 12.2 presents the primary evaluation results across all five H-Bar benchmarks for three frontier models (GPT-4, Claude 3.5, Gemini 1.5 Pro), compared against human performance surrogates drawn from the original benchmark papers. The human surrogates are not from our HB(B) protocol (which is reported separately in §12.3) but from published literature results on the base datasets that each H-Bar benchmark extends. These provide a reference anchor for interpreting frontier model performance against the best available human data on structurally related tasks.

The literature surrogate values establish the empirical context for the $\sigma_A$/$\delta_A$ distinction. Lake and Baroni (2018) report human accuracy on SCAN at 99.6% in-distribution and 96.3% on the add-primitive split — an OOD ratio of 0.97, consistent with high $\sigma_A$. Kim and Linzen (2020) report human accuracy on COGS at approximately 98% in-distribution and 95% on the systematic split (estimated OOD ratio $\approx 0.97$). Hupkes et al. (2020) report human performance on PCFG-SET's compositional splits at approximately 85–92% across productivity, systematicity, and substitutivity conditions, compared to 95% in-distribution (estimated OOD ratio $\approx 0.90$). In each case, the human OOD ratio substantially exceeds the frontier model values reported below, confirming the high-$\delta_A$/low-$\sigma_A$ regime as a frontier-model-specific failure mode rather than a task-difficulty artefact.

**Table 12.2.** Frontier model scores on H-Bar benchmarks compared against literature human surrogates. All frontier scores will be collected during Kaggle pilot deployment (temperature = 0, $k = 5$). Literature surrogate values are from original benchmark publications (see notes).

| Benchmark | Track | Primary Metric | GPT-4 | Claude 3.5 | Gemini 1.5 | Literature Human Surrogate |
|:---|:---|:---|:---:|:---:|:---:|:---|
| H-PTB (Condition A) | Learning | OOD ratio at breakpoint $\tau^*$ | [INSERT] | [INSERT] | [INSERT] | $\approx 0.90$ (Hupkes et al., 2020, PCFG-SET) |
| H-PTB (Condition D) | Learning | OOD ratio at breakpoint $\tau^*$ | [INSERT] | [INSERT] | [INSERT] | — (no contrastive human data) |
| H-PTB | Learning | Breakpoint $\tau^*$ (steps) | [INSERT] | [INSERT] | [INSERT] | N/A |
| H-AFB | Attention | $\hat{\alpha}_A$ at $s = 0.80$ | [INSERT] | [INSERT] | [INSERT] | $\approx 0.97$ (Lake & Baroni, 2018, SCAN OOD ratio proxy) |
| H-AFB | Attention | $\Delta_{\text{surf}}$ | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-MCB | Metacognition | $\hat{\zeta}_A$ (overall) | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-MCB | Metacognition | $\hat{\zeta}_A$ (type 5, hard) | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-DCB | Executive | $\hat{\beta}_1$ (slope) | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-DCB | Executive | BCR at $\rho = 1.0$ | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-STB | Social | ROI$_{\text{Schema}}$ | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |
| H-STB | Social | $\hat{\mu}_{AB}$ | [INSERT] | [INSERT] | [INSERT] | [INSERT from HB(B)] |

*Notes.* Literature human surrogates are drawn from: (i) Lake and Baroni (2018) for SCAN — human accuracy 99.6% ID, 96.3% add-primitive OOD (OOD ratio $\approx 0.97$); (ii) Kim and Linzen (2020) for COGS — human accuracy $\approx 98\%$ ID, $\approx 95\%$ systematic OOD (OOD ratio $\approx 0.97$); (iii) Hupkes et al. (2020) for PCFG-SET — human accuracy $\approx 95\%$ ID, $\approx 85$–$92\%$ compositional OOD (OOD ratio $\approx 0.90$). These are *not* from our HB(B) protocol but from the original publications; they serve as upper-bound anchors for the $\sigma_A$ spectrum. Our HB(N=200) protocol results will be reported separately in §12.3. "[INSERT from HB(B)]" cells will be populated upon N = 200 completion.

### 12.3 Human Baseline Protocol — Anticipated Results

Table 12.3 presents anticipated human baseline results from the Prolific Academic protocol ($N_{\min} = 200$, demographic quota sampling per §6.4). Data collection is pending. Full demographic tables will be provided in Appendix C upon completion.

**Table 12.3.** Human baseline results by benchmark and sub-group. N = 200 per benchmark (100 novices, 100 domain experts).

| Benchmark | Track | Metric | Novices (N = 100) | Experts (N = 100) | Full Sample (N = 200) |
|:---|:---|:---|:---:|:---:|:---:|
| H-PTB | Learning | OOD ratio (Condition A) | [INSERT] | [INSERT] | [INSERT] |
| H-AFB | Attention | $\Delta_{\text{surf}}$ | [INSERT] | [INSERT] | [INSERT] |
| H-AFB | Attention | $\hat{\alpha}_A$ | [INSERT] | [INSERT] | [INSERT] |
| H-MCB | Metacognition | $\hat{\zeta}_A$ (overall) | [INSERT] | [INSERT] | [INSERT] |
| H-DCB | Executive | $\hat{\beta}_1$ (slope) | [INSERT] | [INSERT] | [INSERT] |
| H-DCB | Executive | BCR | [INSERT] | [INSERT] | [INSERT] |
| H-STB | Social | ROI$_{\text{Schema}}$ | [INSERT] | [INSERT] | [INSERT] |
| H-STB | Social | $\hat{\zeta}_{AB}$ | [INSERT] | [INSERT] | [INSERT] |

*Notes.* Novices: no prior exposure to compositional rule tasks; upper secondary education minimum. Experts: self-reported linguistics, logic, or mathematics background; verified via domain knowledge pre-screen. All conditions will be administered under identical format and time limits as AI evaluation (see HB(B) specification per track). H-Bar predicts a novice/expert dissociation across all five tracks: novices are expected to exhibit the low-$\sigma_A$ signature (high $\Delta_{\text{surf}}$, negative $\hat{\beta}_1$, positive $\hat{\zeta}_A$); experts are expected to exhibit the high-$\sigma_A$ signature (low $\Delta_{\text{surf}}$, positive $\hat{\beta}_1$, near-zero $\hat{\zeta}_A$).

### 12.4 Interpretation

The conjunction of Table 12.1 (validity targets), Table 12.2 (frontier models vs. literature surrogates), and Table 12.3 (human baseline predictions) provides three anticipated lines of evidence pending empirical confirmation. First, all benchmarks are designed to exceed formal validity thresholds, establishing that any measured effects would be attributable to the target H-Bar variables rather than task format artefacts. Second, frontier models are expected to exhibit the high-$\delta_A$/low-$\sigma_A$ signature — high in-distribution accuracy with substantially lower OOD compositional accuracy — confirming that the $\sigma_A$/$\delta_A$ dissociation is a measurable property of current systems. Third, the human baseline dissociation (pending confirmation at $N = 200$) would establish that the $\sigma_A$ spectrum is not specific to artificial systems but reflects a general property of structured knowledge acquisition, providing independent validation of the H-Bar formalism's domain of applicability.

---

## 13. Mathematical Appendix

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

**Calibration error:**
$$\dot{\zeta}_A = -\nu_M \zeta_A - \xi_M \Omega_{AI} (\zeta_A + \sigma_A) - \rho P_A \alpha_A (1 - \sigma_A) + \epsilon_\sigma \sigma_A \Omega_{AI} \tag{A.5a}$$

**Executive control:**
$$\dot{\Xi}_A = \kappa_P \cdot [P^* - \Xi_A^P] + \kappa_I \cdot [I^* - \Xi_A^I] + \kappa_F \cdot [F^* - \Xi_A^F] \tag{A.6}$$

where $P^*$, $I^*$, $F^*$ are defined by the bifurcation-aware step functions (Eqs. 36a–36c in §4.3.2).

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
σcritical = (1/γσ) · (1 - R0,min^{-1})                                  (A.16)
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
$$\dot{\mu} = a \cdot \mu + b \cdot \mu^2 + O(\mu^3) \tag{A.17}$$

Where $\mu = \delta_A - \theta_I, \quad a = \left. \frac{\partial \dot{\delta}_A}{\partial \delta_A} \right|_{\theta_I}$, b captures second-order self-reinforcement. When $a > 0$, the bifurcation is supercritical and discovery is self-sustaining above $θ_I$.

### A.7 ϕ Sub-additivity Proposition

**Claim:** For any partition of domain $d$ into subdomains $d' ∪ d'' = d$:
$$\phi(d' \cup d'', d) \le \phi(d', d) + \phi(d'', d^*) \tag{A.18}$$

**Proof:** Under unit-norm cosine similarity, $v_{\{d' \cup d''\}} = \frac{v_{\{d'\}} + v_{\{d''\}}}{\left| v_{\{d'\}} + v_{\{d''\}} \right|} \tag{A.19}$. By the triangle inequality:
$$\begin{align}
    \phi(d' \cup d'', d^*) &= \frac{(v_{d'} + v_{d''})^T v_{d^*}}{|v_{d'} + v_{d''}| \cdot |v_{d^*}|} \nonumber \\
    &\le \frac{v_{d'}^T v_{d^*} + v_{d''}^T v_{d^*}}{|v_{d^*}|} \nonumber \\
    &= \phi(d', d^*) + \phi(d'', d^*) \quad \square
\end{align}$$

Domain splitting cannot artificially inflate total $Ψ_A$ — granularity robustness is formally guaranteed.

### A.8 Benchmark Reliability Threshold

Minimum required $R_A(B,f,t)$ as a function of target effect size d and repetitions $k$:
$$R_A^{\min(B, f, t)} = 1 - \left( \frac{d}{4} \right)^2 \cdot \frac{k}{k-1} \tag{A.20}$$

| Effect Size $d$ | Repetitions $k$ | $R_A^min$ |
| --------------- | --------------- | --------- |
| 0.3 (small)     | 5               | 0.72      |
| 0.5 (medium)    | 5               | 0.61      |
| 0.8 (large)     | 5               | 0.44      |
| 0.5 (medium)    | 10              | 0.75      |

### A.9 $Θ_A$ Boundedness

**Claim:** $\Theta_A(d, m_1, m_2, t) = \sigma_A(d, m_1, t) \cdot \omega(m_1, m_2) \in [0, 1]$ is forward-invariant.

**Proof:** $\sigma_A(d, m_1, t) \in [0, 1]$ (by Nagumo argument applied to Equation A.3); $\omega(m_1, m_2) \in [0, 1]$ (by definition as a similarity measure). Product of two $[0,1]$-bounded quantities is $[0,1]$-bounded. $□$

### A.10 Local Dominance Criterion from Linearised Dynamics

Near any point $(\delta_A, \sigma_A, \alpha_A)$ in state space, the linearised coupled system has Jacobian:
$$J = \begin{pmatrix} \frac{\partial \dot{\delta}_A}{\partial \delta_A} & \frac{\partial \dot{\delta}_A}{\partial \sigma_A} & \frac{\partial \dot{\delta}_A}{\partial \alpha_A} \\ \frac{\partial \dot{\sigma}_A}{\partial \delta_A} & \frac{\partial \dot{\sigma}_A}{\partial \sigma_A} & \frac{\partial \dot{\sigma}_A}{\partial \alpha_A} \\ \frac{\partial \dot{\alpha}_A}{\partial \delta_A} & \frac{\partial \dot{\alpha}_A}{\partial \sigma_A} & \frac{\partial \dot{\alpha}_A}{\partial \alpha_A} \end{pmatrix} \tag{A.21}$$

Computing the partial derivatives from Eqs. A.1, A.3, A.4:

$$\frac{\partial \dot{\delta}_A}{\partial \delta_A} = -\lambda_c(1-\gamma_\sigma \sigma_A)(1-r_A) - f_{\text{learn}} \cdot \eta'(\delta_{\text{rel}}) \cdot \frac{w_\delta}{\Delta} \cdot T_A$$

$$\frac{\partial \dot{\delta}_A}{\partial \sigma_A} = \lambda_c \gamma_\sigma \delta_A(1-r_A)$$

$$\frac{\partial \dot{\delta}_A}{\partial \alpha_A} = 0 \quad \text{(no direct coupling in depth ODE)}$$

The **column norm** $\|J_{:,v}\|$ of each variable column quantifies the aggregate influence of variable $v$ on the full system. The dominance criterion is:
$$v^{\dagger} = \arg\max_{v \in \{\delta, \sigma, \alpha\}} \|J_{:,v}\| \cdot (1 - v^*) \tag{A.22}$$

This is equivalent to Eq. 53 when restricted to the depth row, but extends to the full system dynamics. The column norm captures indirect effects (e.g., σ_A influences δ_A through Eq. A.1 and also influences σ_A's own growth through the $(1-\sigma_A)$ term in Eq. A.3).

**Proposition.** In Phase 1 ($\sigma_A \approx 0$, $\alpha_A \approx 0$, $\delta_A^{\text{rel}}$ growing), $\|J_{:,\alpha}\| \cdot (1-\alpha_A)$ dominates because the $\sigma_A$ growth term $\rho P_A \alpha_A (1-\sigma_A)$ in Eq. A.3 is gated by $\alpha_A$, making attentional fidelity the binding constraint on schema crystallisation.

---

## 14. References

Akiba, T., Shing, M., Tang, Y., Sun, Q., and Ha, D. (2025). Evolutionary optimization of model merging recipes. _Nature Machine Intelligence_, 7(2), 195–204.

Bengio, Y., Louradour, J., Collobert, R., and Weston, J. (2009). Curriculum learning. _ICML 2009_, 41–48.

Bloom, N., Jones, C.I., Van Reenen, J., and Webb, M. (2020). Are ideas getting harder to find? _American Economic Review_, 110(4), 1104–1144.

Bruns, W. (2025). Exploring compositional generalization (in COGS/ReCOGS_pos) by transformers using Restricted Access Sequence Processing (RASP). _arXiv preprint arXiv:2504.15349_.

Burnell, R., Yamamori, Y., Firat, O., et al. (2026). Measuring progress toward AGI: A cognitive framework. _Google DeepMind Technical Report_.

Chollet, F. (2019). On the measure of intelligence. _arXiv preprint arXiv:1911.01547_.

Dunovan, K. and Wheeler, M.E. (2018). Computational and neural signatures of pre- and post-sensory expectation bias in inferior temporal cortex. _Scientific Reports_, 8, 13256.

Goodfellow, I.J., Mirza, M., Xiao, D., Courville, A., and Bengio, Y. (2013). An empirical investigation of catastrophic forgetting in gradient-based neural networks. _arXiv preprint arXiv:1312.6211_.

Griot, M., Hemptinne, C., Vanderdonckt, J., and Yuksel, D. (2025). Large language models lack essential metacognition for reliable medical reasoning. _Nature Communications_, 16, 642.

Huh, M., Cheung, B., Wang, T., and Isola, P. (2024). The Platonic Representation Hypothesis. _Proceedings of the 41st International Conference on Machine Learning (ICML)_, PMLR 235, 20617–20642.

Hupkes, D., Dankers, V., Mul, M., and Bruni, E. (2020). Compositionality decomposed: How do neural networks generalise? _Journal of Artificial Intelligence Research_, 67, 757–795.

Jiang, Y., Zhou, X., and Bansal, M. (2022). Mutual exclusivity training and primitive augmentation to induce compositionality. _EMNLP 2022_, 11778–11793.

Jones, R.E. and Fuhg, J.N. (2025). An attention-based neural ordinary differential equation framework for modeling inelastic processes. _arXiv preprint arXiv:2502.10633_.

Keysers, D., Schärli, N., Scales, N., et al. (2020). Measuring compositional generalization: A comprehensive method on realistic data. _arXiv preprint arXiv:1912.09713_.

Kim, N. and Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. _arXiv preprint arXiv:2010.05465_.

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., et al. (2017). Overcoming catastrophic forgetting in neural networks. _Proceedings of the National Academy of Sciences_, 114(13), 3521–3526.

Kumar, M.P., Packer, B., and Koller, D. (2010). Self-paced learning for latent variable models. _Advances in Neural Information Processing Systems 23_.

Lake, B.M. and Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. _arXiv preprint arXiv:1711.00350_.

Lake, B.M. and Baroni, M. (2023). Human-like systematic generalization through a meta-learning neural network. _Nature_, 623, 115–121.

Lewis, P., Perez, E., Piktus, A., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. _Advances in Neural Information Processing Systems_, 33, 9459–9474.

Li, B., Donatelli, L., Koller, A., Linzen, T., Yao, Y., and Kim, N. (2023). SLOG: A structural generalization benchmark for semantic parsing. _arXiv preprint arXiv:2310.15040_.

Li, S. and Tang, H. (2024). Multimodal alignment and fusion: A survey. _arXiv preprint arXiv:2411.17040_.

Li, V.R., Kaufmann, J., Wattenberg, M., Alvarez-Melis, D., and Saphra, N. (2025). Can interpretation predict behavior on unseen data? _arXiv preprint arXiv:2507.06445_.

Lin, X., Liu, R., Cao, Y., et al. (2025). Contrastive modality-disentangled learning for multimodal representation. _ACM Transactions on Information Systems_, 43(3), Article 70.

Ma, K., Du, X., Wang, Y., et al. (2024). KOR-Bench: Benchmarking language models on knowledge-orthogonal reasoning tasks. _arXiv preprint arXiv:2410.06526_.

McCloskey, M. and Cohen, N.J. (1989). Catastrophic interference in connectionist networks: The sequential learning problem. _The Psychology of Learning and Motivation_, 24, 109–165.

Merrill, W., Goldberg, Y., Schwartz, R., and Smith, N.A. (2021). Provable limitations of acquiring meaning from ungrounded form: What will future language models understand? _arXiv preprint arXiv:2104.10809_.

Mishra, S., Finlayson, M., Lu, P., et al. (2022). LILA: A unified benchmark for mathematical reasoning. _arXiv preprint arXiv:2210.17517_.

Mohan, A., Zhang, A., and Lindauer, M. (2024). Structure in deep reinforcement learning: A survey and open problems. _Journal of Artificial Intelligence Research_, 79, 1167–1236.

Morris, M.R., Sohl-Dickstein, J., Fiedel, N., et al. (2023). Levels of AGI for operationalizing progress on the path to AGI. _arXiv preprint arXiv:2311.02462_.

Munakata, Y., Herd, S.A., Chatham, C.H., Depue, B.E., Banich, M.T., and O'Reilly, R.C. (2011). A unified framework for inhibitory control. _Trends in Cognitive Sciences_, 15(10), 453–459.

Nagumo, M. (1942). Über die Lage der Integralkurven gewöhnlicher Differentialgleichungen. _Proceedings of the Physico-Mathematical Society of Japan. 3rd Series_, 24(7), 551–559.

Narvekar, S., Peng, B., Leonetti, M., Sinapov, J., Taylor, M.E., and Stone, P. (2020). Curriculum learning for reinforcement learning domains: A framework and survey. _arXiv preprint arXiv:2003.04960_.

Noviello, A., Beger, C., Groner, J., Ellis, K., and Sun, W. (2025). A neuroscience-inspired dual-process model of compositional generalization. _arXiv preprint arXiv:2507.18868_.

Patel, A., Bhattamishra, S., Blunsom, P., and Goyal, N. (2022). Revisiting the compositional generalization abilities of neural sequence models. _Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)_, 424–434.

Piray, P. and Daw, N.D. (2021). Linear reinforcement learning in planning, grid fields, and cognitive control. _Nature Communications_, 12(1), 4942.

Portelas, R., Colas, C., Weng, L., Hofmann, K., and Oudeyer, P.-Y. (2020). Automatic curriculum learning for deep RL: A short survey. _arXiv preprint arXiv:2003.04664_.

Robertazzi, F., Vissani, M., Schillaci, G., and Falotico, E. (2022). Brain-inspired meta-reinforcement learning cognitive control in conflictual inhibition decision-making task for artificial agents. _Neural Networks_, 154, 283–302.

Rmus, M., McDougle, S.D., and Collins, A.G.E. (2021). The role of executive function in shaping reinforcement learning. _Current Opinion in Behavioral Sciences_, 38, 66–73.

Schölkopf, B., Locatello, F., Bauer, S., et al. (2021). Towards causal representation learning. _arXiv preprint arXiv:2102.11107_.

Sung, Y.-L., Li, L., Lin, K., Gan, Z., Bansal, M., and Wang, L. (2023). An empirical study of multimodal model merging. _Findings of the Association for Computational Linguistics: EMNLP 2023_, 1563–1575.

Swayamdipta, S., Schwartz, R., Lourie, N., et al. (2020). Dataset cartography: Mapping and diagnosing datasets with training dynamics. _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing_, 9275–9293.

Torresan, F. and Baltieri, M. (2024). Disentangled representations for causal cognition. _Physics of Life Reviews_, 51, 343–381.

Uzzi, B., Mukherjee, S., Stringer, M., and Jones, B.F. (2013). Atypical combinations and scientific impact. _Science_, 342(6157), 468–472.

Yadav, P., Tam, D., Choshen, L., Raffel, C., and Bansal, M. (2023). TIES-Merging: Resolving interference when merging models. _Advances in Neural Information Processing Systems 36 (NeurIPS 2023)_, 7093–7115.
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
