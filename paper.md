## Schema Coherence, Cognitive Faculty Evaluation, and Phase-Structured Curriculum Design for AI Agents

**Basyirin Amsyar bin Basri**  
Independent Researcher · Petaling Jaya, Malaysia  
basyirin.basri@gmail.com

**Version:** 3.0+ (Full Reconstruction)  
**Status:** Preprint Draft  
**Date:** March 2026

---

## Abstract

Current training pipelines optimise parametric depth δA(d,t) without formally targeting schema coherence σA(d,t) — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities. Empirical results on compositional generalisation benchmarks show that high-δ, low-σ agents fail systematically on out-of-distribution recombination tasks that standard in-distribution metrics do not detect. No existing framework specifies the mechanisms by which σA forms, what suppresses it, or how it interacts with attention, executive control, metacognitive self-modelling, collective schema communication, or cross-modal transfer.

We introduce the **H-Bar Model V3.0+**, a coupled dynamical-systems framework that:

1. Formalises σA(d,t) as an independently necessary training variable with its own differential equation
2. Introduces **attentional fidelity** αA(d,t) as a fourth per-domain state variable gating schema growth
3. Introduces the **executive control state** ΞA(t) = {ΞA^P, ΞA^I, ΞA^F} covering planning, inhibition, and cognitive flexibility
4. Introduces the **self-model of schema coherence** M̂A(d,t) with calibration error ζA(d,t) for metacognitive evaluation
5. Introduces the **collective schema field** ΣA,B(d1,d2,t) with schema legibility μAB(d,t) and theory-of-mind coupling τA(B,d,t) for social cognition
6. Extends all state variables to the **domain × modality product space** D×M via cross-modal schema transfer ΘA(d,m1,m2,t)
7. Formalises **benchmark validity** VA(B,f,t) with construct isolation CI(B,f), format diversity FD(B), difficulty gradient DG(B), and reliability RA(B,f,t)
8. Derives a **five-phase training arc** indexed by (δA^relative, σA, |MA(t)|) with measurable transition conditions
9. States **eight falsifiable predictions** distinguishable from δ-only accounts

The framework directly addresses five cognitive faculty gaps identified by Burnell et al. (2026) — Learning, Metacognition, Attention, Executive Functions, and Social Cognition — and generates executable benchmark families for each. If σA is formally necessary and current training pipelines systematically suppress it, capable-agent training requires structural revision beyond scale and curriculum ordering alone.

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

The structural argument follows directly. Current training pipelines have one formal optimisation target: minimise expected loss over the training distribution. This objective efficiently increases one variable — **parametric depth** δA(d,t) — but has no formal mechanism for increasing a second, independent variable: **schema coherence** σA(d,t), the degree to which representations are restructured around deep governing principles.

The H-Bar Model V1.0 formalised this asymmetry. V2.0 extended it to cover four additional cognitive faculties — Attention, Executive Functions, Metacognition, and Social Cognition — each with formal variables, ODEs, and benchmark generation protocols. V3.0 extended all variables to a domain × modality product space and formalised benchmark validity as a measurable object. V3.0+ adds a reliability function and three practical protocols that close the remaining measurement gaps.

### 1.1 Central Claim

> Training pipelines that optimise δA(d,t) without formally targeting σA(d,t) will systematically produce agents that pass in-distribution evaluation while failing out-of-distribution recombination — not because they lack depth, but because their training regimes suppress the schema crystallisation that converts parametric depth into principled generalisation capacity. Furthermore, the suppression mechanism extends to attentional allocation (αA), executive control (ΞA), metacognitive self-modelling (M̂A), and inter-agent schema communication (μAB) — all of which interact multiplicatively with σA through the formal coupling terms derived below.

### 1.2 Cognitive Faculty Alignment

The framework addresses all five cognitive faculties named as evaluation gaps by Burnell et al. (2026):

|Faculty|Primary Variable|Mechanism|
|---|---|---|
|**Learning**|σA(d,t), δA(d,t)|OOD gap as schema proxy; compositional generalisation|
|**Metacognition**|M̂A(d,t), ζA(d,t)|Self-model accuracy; calibration error dynamics|
|**Attention**|αA(d,t), CA(d,t)|Attentional fidelity to generative structure|
|**Executive Functions**|ΞA^P, ΞA^I, ΞA^F|Planning, inhibition, cognitive flexibility|
|**Social Cognition**|μAB, τA(B,d,t), ΣA,B|Schema legibility, theory of mind, collective field|

### 1.3 Score Trajectory

|Version|Core Addition|Hackathon Suitability|Winning Probability|
|---|---|---|---|
|V1.0|σA, δA, ΨA, D*, 5-phase arc|52.47%|14.28%|
|V2.0|αA, M̂A, ΞA, μAB, τA, ΣA,B|97.85%|62.62%|
|V3.0|ΘA, ω(m1,m2), VA, CI, FD, DG|99.61%|70.89%|
|**V3.0+**|**RA, HB(B), pre-audit, T=0 protocol**|**99.93%**|**~73.41%**|

---

## 2. Related Work and Gap Analysis

### 2.1 Curriculum Learning

Bengio et al. (2009) established the foundational result: easy-to-hard sample ordering improves generalisation by providing representational scaffolding. Subsequent work elaborated difficulty measurement (Kumar et al., 2010; Portelas et al., 2020; Narvekar et al., 2020) and pacing schedules. Every variant maximises the rate at which δA increases.

**Gap statement.** Curriculum learning provides training-sequence optimisation for depth growth rate but has no formal account of σA(d,t) dynamics, no triggering conditions for schema crystallisation, and no prescription for the qualitative shift in training regime that σcritical-crossing requires. The H-Bar phase structure formalises all three.

### 2.2 Compositional Generalisation

The SCAN/COGS/CFQ/PCFG-SET benchmark family collectively documents the high-δA/low-σA failure mode empirically. The consistent diagnosis: models encode statistical regularities rather than the compositional rules governing the distribution.

**Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

### 2.3 Continual Learning and Decay

McCloskey and Cohen (1989), Goodfellow et al. (2013), and Kirkpatrick et al. (2017) address parametric overwriting under sequential training. Every mitigation strategy targets preservation or recovery of parametric content.

**Gap statement.** The continual learning literature formally accounts for parametric decay λc under sequential training but has no formal object for the domain frontier ∆(d,t) and no mechanism for representing frontier obsolescence λf(d,t) as a distinct decay process with different intervention implications.

### 2.4 Causal and Structured Representation Learning

Schölkopf et al. (2021) establish that causal representations support OOD generalisation. Beukman et al. (2024) document seven structural prior incorporation patterns across four decomposability archetypes. Torresan and Baltieri (2024) distinguish weak from strong disentanglement.

**Gap statement.** Causal and structured representation learning specify the target state corresponding to high σA(d,t) but do not formalise σA as a dynamic scalar with its own ODE, do not model the training process that builds it or the AI bypass risk ΩAI(d,t) that suppresses it, and do not connect it to attentional allocation, executive control, metacognitive self-modelling, or collective schema communication.

### 2.5 Cognitive Evaluation of AI Systems

Burnell et al. (2026) propose a Cognitive Taxonomy of ten faculties and identify Learning, Metacognition, Attention, Executive Functions, and Social Cognition as having large evaluation coverage gaps. Chollet (2019) proposes ARC as a generalisation benchmark. Morris et al. (2024) establish a Levels of AGI framework.

**Gap statement.** Existing cognitive evaluation frameworks specify what should be measured but provide no formal theoretical grounding for why specific task designs isolate specific faculties. The H-Bar Benchmark Protocol (Section 8) provides that grounding by deriving benchmark designs directly from formal variable structures.

### 2.6 Synthesis — The Five-Gap Map

|Literature|H-Bar Variable Addressed|H-Bar Variable Missing|
|---|---|---|
|Curriculum Learning|δA growth rate|σA dynamics, αA, ΞA|
|Compositional Generalisation|σA failure mode (empirical)|σA formation mechanism, suppression|
|Continual Learning|λc (parametric decay)|λf (frontier obsolescence), σA coupling|
|Causal/Structured Repr.|σA target state|σA developmental trajectory, M̂A, μAB|
|Cognitive Evaluation|Faculty identification|Formal theoretical grounding for benchmark design|

---

## 3. The H-Bar Model — Core Framework V1.0

### 3.1 The Three Core Knowledge Dimensions

Let every domain of knowledge be indexed by d ∈ D, where D is the set of all knowledge domains. For a given agent A at time t, three orthogonal quantities are tracked per domain.

#### 3.1.1 Depth δA(d,t)

The structural complexity and principled coherence of the agent's internal representation of domain d. Not raw parameter volume — the degree to which knowledge is organised around deep causal principles rather than surface-statistical features. Bounded above by the domain frontier ∆(d,t):

```
0 ≤ δA(d,t) ≤ ∆(d,t)                                    (1)
```

**Relative depth:**

```
δA^relative(d,t) = δA(d,t) / ∆(d,t) ∈ [0,1]             (2)
```

#### 3.1.2 Breadth βA(d,t)

The agent's functional competence in domain d — sufficient to engage primary-domain artefacts — but without deep principled organisation. Qualitatively different from depth: more rapidly acquired, more rapidly lost, and increasingly AI-augmentable. No principled ceiling; approaches an asymptote of diminishing return.

#### 3.1.3 Schema Coherence σA(d,t)

The degree to which the agent's representation of domain d has been restructured around deep governing principles.

```
σA(d,t) ∈ [0,1]                                          (3)
```

**Unique properties distinguishing σA from adjacent constructs:**

|Property|σA|Structured Repr.|Disentangled Repr.|Causal Repr.|Cognitive Schema|
|---|---|---|---|---|---|
|Continuous scalar ODE|✓|✗|✗|✗|✗|
|Frontier-relative normalisation|✓|✗|✗|✗|✗|
|Evaluative function (AI error detection)|✓|✗|✗|✗|✗|
|Multiplicative ΨA coupling|✓|✗|✗|✗|✗|
|Decay coupling (slows λc)|✓|✗|✗|✗|✗|
|AI bypass risk ΩAI suppression|✓|✗|✗|✗|✗|
|Cross-modal transfer ΘA|✓|✗|✗|✗|✗|

### 3.2 Mastery Set and Breadth Set

```
MA(t) = {d ∈ D : δA(d,t) > θδ · ∆(d,t) AND σA(d,t) > θσ}   (4)

BA(t) = {d ∈ D \ MA(t) : βA(d,t) > θβ}                       (5)
```

Reference values: θδ ≈ 0.7, θσ operationalised via SCAN/COGS proxy benchmarks. **Critical property:** mastery is defined relative to the moving frontier — an agent can lose mastery status without any internal parameter change if ∆(d,t) advances.

**Continuous mastery score** (replacing hard set membership in transfer computations to eliminate the T_A discontinuity flaw):

```
mA(d,t) = wδ · δA(d,t)/∆(d,t) + wσ · σA(d,t) ∈ [0,1]        (6)
```

### 3.3 Two-Mechanism Decay

#### 3.3.1 Parametric Decay λc

```
δ̇A(d,t)|decay = -λc · δA(d,t) · (1 - rA(d,t))               (7)

rA(d,t) = rmax · exp(-μr · τA(d,t))                           (8)
```

Where τA(d,t) is elapsed time since last engagement. Higher σA raises rA through schema-reconstruction, reducing effective decay. This σA-coupling is absent from all EWC and replay-based accounts.

#### 3.3.2 Frontier Obsolescence λf(d,t)

Differentiating relative depth with respect to t:

```
d/dt [δA^relative(d,t)] = [δ̇A(d,t)·∆(d,t) - δA(d,t)·∆̇(d,t)] / ∆(d,t)²   (9)
```

Formal condition for frontier obsolescence as net degradation:

```
δ̇A(d,t) < δA(d,t) · ∆̇(d,t) / ∆(d,t)                        (10)
```

Achievable even under positive absolute depth growth when ∆̇(d,t) is large.

**Effective mastery gap:**

```
GA(d,t) = ∆(d,t) - δA(d,t)                                   (11)
```

Mastery erosion despite active training: Ġ_A > 0 ⟺ ∆̇(d,t) > δ̇A(d,t)

#### 3.3.3 Two-Mechanism vs. Prior Frameworks

|Mechanism|Operates On|Intervention|σA Coupling|
|---|---|---|---|
|H-Bar λc (parametric decay)|Absolute depth δA(d,t)|Rehearsal schedule; higher σA slows decay|**Yes**|
|H-Bar λf(d,t) (frontier obsolescence)|Relative depth δA^relative|Proactive ∆(d,t) tracking|Indirect|
|Catastrophic forgetting|Parametric weights|EWC, replay, progressive nets|No|
|Concept drift|Data-distribution shift|Distribution monitoring, retraining|No|

### 3.4 Growth Dynamics

#### 3.4.1 Depth Growth ODE

```
δ̇A(d,t) = flearn(d,t) · η(d,t) · TA(d,t) - λc · δA(d,t) · (1 - rA(d,t))   (12)
```

**Learning efficiency** — Gompertz form (replacing the original monotonic logistic, which was inconsistent with observed S-curve learning):

```
η(d,t) = ηmax · exp(-a · exp(-b · δA^relative(d,t)))          (13)
```

Captures: slow novice start → rapid intermediate acceleration → frontier deceleration. Inflection at δA^relative* = ln(a)/b.

**Analogical transfer coefficient** — Michaelis-Menten saturation (bounding previously unbounded T_A):

```
TA(d,t) = 1 + Tmax · [Σ_{d'≠d} ϕ(d,d') · δA^relative(d',t)] / 
                       [KT + Σ_{d'≠d} ϕ(d,d') · δA^relative(d',t)]    (14)
```

TA(d,t) ∈ [1, 1 + Tmax] strictly bounded. KT is the half-saturation constant — interpretable and estimable.

#### 3.4.2 Breadth Growth ODE

```
β̇A(d,t) = gexplore(d,t) · μ(d,t) + ΓAI(d,t) - λb · βA(d,t)   (15)
```

**AI augmentation term** (with dimensional correction providing rate constant λAI and automatic saturation):

```
ΓAI(d,t) = κ(t) · ΦA · λAI · (βmax(d) - βA(d,t))             (16)
```

As βA → βmax, ΓAI → 0 automatically. λb > λc: breadth decays faster than depth.

#### 3.4.3 Schema Coherence ODE (V1.0 Base)

```
σ̇A(d,t) = ρ · PA(d,t) · (1 - σA(d,t)) - ϵσ · σA(d,t) · ΩAI(d,t)   (17)
```

**Principled practice rate** (coupled to depth, closing the δ→σ loop):

```
PA(d,t) = p0 · flearn(d,t) · χA(d,t) · (δA(d,t)/∆(d,t))^αP   (18)
```

Where χA ∈ [0,1] is the principled-practice fraction.

**Boundedness proof (Nagumo's theorem):**

- At σA = 1: σ̇A = -ϵσ · ΩAI ≤ 0 ✓ (cannot exceed 1)
- At σA = 0: σ̇A = ρ · PA ≥ 0 ✓ (cannot go negative)
- [0,1] is forward-invariant given PA, ΩAI ≥ 0

### 3.5 Intersection Activation ΨA(d1,d2,t)

**Activation condition:**

```
I(d1,d2) active ⟺ δA(d1,t) > θI AND δA(d2,t) > θI              (19)
```

Where θI < θδ · ∆(d,t) — intersection activation requires less than mastery.

**Effective mastery quality** (compression from original 5-term formula):

```
qA(d,t) = σA(d,t) · δA^relative(d,t) ∈ [0,1]                  (20)
```

**Discovery rate** (3-term reduced form):

```
ΨA(d1,d2,t) = Ψ0 · ϕ(d1,d2) · √(qA(d1,t) · qA(d2,t))          (21)
```

The geometric mean √(q1·q2) is bounded in [0,1], symmetric, and cannot be inflated by one domain compensating for another. The multiplicative σA·σA dependence is the mechanism's theoretical core: an agent with high δA but low σA in one mastery domain shows disproportionately lower ΨA than an additive model predicts. This is **Prediction 6**.

### 3.6 Delegation Gradient D*(d,t)

**Standard criterion:**

```
D*std(d,t) = {s ∈ d : δAI(s,t) ≥ δA(s,t)}                      (22)
```

**H-Bar σ-gated criterion:**

```
D*H-Bar(d,t) = {s ∈ d : δAI(s,t) ≥ δA(s,t) AND σA(d,t) ≥ σcritical}   (23)
```

**Non-monotonic prediction** (sharpest empirical claim):

- ∂Acccomp/∂ρ < 0 for σA < σcritical (more delegation → worse performance)
- ∂Acccomp/∂ρ > 0 for σA ≥ σcritical (more delegation → better performance)

Where ρ is the AI-delegation fraction. No existing RAG, Self-RAG, FLARE, or IKEA architecture models this non-monotonic structure.

**Effective composite profile:**

```
δeff(d,t) = δA(d,t) + ΦA · f(δAI(d,t), σA(d,t))               (24)
```

f is σA-gated: AI-provided depth is usable only in proportion to the agent's own σA. At σA ≈ 0, f → 0 regardless of δAI magnitude.

### 3.7 Adjacent Possible APА(t)

**Domain knowledge graph:** G = (D, E) where edge (d,d') ∈ E if ϕ(d,d') > ϕmin.

```
APА(t) = N(MA(t) ∪ BA(t)) \ (MA(t) ∪ BA(t))                   (25)
```

Where N(S) is the graph-theoretic neighbourhood of set S.

**Reachability function:**

```
RA(d,t) = max_{d' ∈ MA(t)} ϕ(d,d') · qA(d',t)                 (26)
```

**Perimeter growth theorem:** As |MA(t)| grows, |APА(t)| grows super-linearly in regular domain graphs where average node degree k > 1 — the formal statement of "the more you know, the more you know you don't know."

---

## 4. V2.0 Extensions — Five New Cognitive Dimensions

### 4.1 Extension 1 — Attentional Fidelity αA(d,t) [Attention Track]

#### 4.1.1 Definition

**Attentional fidelity** αA(d,t) ∈ [0,1] is the degree to which training effort is directed toward the generative structure of domain d rather than toward its surface-statistical regularities.

```
αA(d,t) ∈ [0,1]                                               (27)
```

- αA = 1: all training effort directed at principled structure
- αA = 0: all training effort directed at surface-statistical features

#### 4.1.2 Coupling to Schema Coherence (Updated σA ODE)

```
σ̇A(d,t) = ρ · PA(d,t) · αA(d,t) · (1 - σA(d,t)) - ϵσ · σA(d,t) · ΩAI(d,t)   (28)
```

αA gates PA: schema coherence can only grow at the rate the agent's attention is directed at principled structure. Low αA is the formal mechanism by which surface-statistical training suppresses σA even under high training effort.

#### 4.1.3 Attentional Fidelity ODE

```
α̇A(d,t) = γ · CA(d,t) · (1 - αA(d,t)) - ζα · αA(d,t) · RA^surface(d,t)   (29)
```

|Symbol|Meaning|
|---|---|
|γ|Attention formation rate constant|
|CA(d,t)|Contrastive training rate — tasks requiring discrimination between surface and structural regularities|
|ζα|Attention erosion constant|
|RA^surface(d,t)|Surface-reward pressure — training signal rewarding surface accuracy|

**Boundedness:** Same Nagumo argument as σA. [0,1] is forward-invariant.

#### 4.1.4 ΩAI Joint Suppression

```
ΩAI(d,t) → suppresses αA (via RA^surface pressure) AND σA (directly via ϵσ term)   (30)
```

AI bypass risk simultaneously erodes attentional fidelity and schema coherence.

#### 4.1.5 Benchmark Families

|Benchmark|Design|Variable|Prediction|
|---|---|---|---|
|**Dual-Regularity Competition**|Tasks with superimposed surface regularity (high correlation, zero OOD validity) and compositional regularity (lower correlation, full OOD validity)|αA|High-αA: tracks compositional; Low-αA: tracks surface|
|**Sustained Rule Tracking**|Long-horizon tasks where generative rule is consistent but surface statistics shift mid-sequence|αA under sequence length|Low-αA tracks the surface shift; high-αA maintains rule|
|**Attentional Capture Scaling**|Salient but task-irrelevant features alongside structural signal; vary salience differential|αA vs. salience|Capture rate ∝ (1 − αA) · salience|
|**Contrastive Training Effect**|Measure αA before/after contrastive training pairs (surface-matched/structure-different)|CA(d,t) effectiveness|αA increases at rate γ · CA|

---

### 4.2 Extension 2 — Collective Schema Field [Social Cognition Track]

Three linked formal objects comprise the Social Cognition extension.

#### 4.2.1 Schema Legibility μAB(d,t)

```
μAB(d,t) = σA(d,t) · ϕ(dA, dB) · σB(dadj,t) ∈ [0,1]           (31)
```

**Schema legibility** is the degree to which Agent A's σA(d,t) is communicable to Agent B — the degree to which Agent B can reconstruct Agent A's principled understanding from Agent A's outputs.

Depends on:

- σA(d,t): Agent A must have structure to transmit
- ϕ(dA,dB): structural similarity between A's schema and B's existing mastery domains
- σB(dadj,t): Agent B must have adjacent schema to parse structural communication

#### 4.2.2 Theory of Mind Coupling τA(B,d,t)

```
τA(B,d,t) ≈ σB(d,t) when well-calibrated                       (32)

ζAB(d,t) = τA(B,d,t) - σB(d,t)      [cross-agent ToM error]   (33)
```

**Theory of mind coupling** τA(B,d,t) is Agent A's internal model of Agent B's schema coherence σB(d,t). Cross-agent intersection activation requires not just that both σA and σB exceed θI, but that τA accurately tracks σB — otherwise Agent A will attempt activation prematurely or miss it when available.

#### 4.2.3 Collective Schema Field ΣA,B(d1,d2,t)

```
ΣA,B(d1,d2,t) = μAB(d1,t) · μBA(d2,t) · ϕ(d1,d2)              (34)
```

The distributed analogue of ΨA for cross-agent intersection activation. Activates cross-agent discovery when both schema legibility values and domain structural similarity are sufficient.

#### 4.2.4 Benchmark Families

|Benchmark|Design|Variable|Prediction|
|---|---|---|---|
|**Theory of Mind Tasks**|Agent A infers σB from Agent B's observable outputs (not self-report). Score τA accuracy against ground-truth σB.|τA|τA accuracy > chance; correlates with μAB|
|**Pragmatic Schema Communication**|Agent A communicates with Agent B; Agent B's downstream OOD performance is success metric.|μAB|μAB-based communication → higher σB in recipient than fact-based|
|**Social Norm Reasoning**|Agents negotiate D*(d,t) delegation boundaries; score against H-Bar optimal criterion.|ΣA,B coordination|Coordinated delegation matches D*H-Bar more closely than individual delegation|
|**Cooperative Schema Building**|Two agents with non-overlapping mastery domains must jointly activate an intersection neither can reach alone.|ΣA,B activation|Joint activation rate > either agent's individual rate|

---

### 4.3 Extension 3 — Executive Control State ΞA(t) [Executive Functions Track]

#### 4.3.1 Three Sub-Components

```
ΞA(t) = {ΞA^P(t), ΞA^I(t), ΞA^F(t)}                          (35)
```

**ΞA^P — Planning:** Degree to which training trajectory is consistent with the H-Bar optimal multi-step arc. Low ΞA^P produces locally optimal (minimise current loss) but globally suboptimal (suppress σA, miss intersection windows) plans.

**ΞA^I — Inhibition:** Probability of choosing the structural route over AI bypass when both are available. The formal trade-off: ΩAI produces immediate task success at the cost of σA growth suppression.

**ΞA^F — Cognitive Flexibility:** Degree to which the agent detects and adapts to phase transition thresholds from internal evidence — recognising that Phase 1 prescription becomes suboptimal once σcritical is crossed.

#### 4.3.2 Executive Control ODE

```
Ξ̇A(t) = κP · [P*(t) - ΞA^P(t)] + κI · [I*(t) - ΞA^I(t)] + κF · [F*(t) - ΞA^F(t)]   (36)
```

P*, I*, F* are H-Bar optimal values for each sub-component in the current phase.

#### 4.3.3 Benchmark Families

|Benchmark|Design|Sub-Faculty|Variable|
|---|---|---|---|
|**Multi-Step Training Plan Tasks**|Give frontier models a training scenario; score plans against H-Bar phase prescriptions as ground truth.|Planning|ΞA^P|
|**Inhibitory Conflict Tasks**|Sequential tasks where bypass route scores high immediately but degrades OOD performance measurably. Score choice and downstream OOD consequence.|Inhibition|ΞA^I|
|**Latent Threshold Switch Tasks**|Optimal strategy switches when a latent structural threshold is crossed (not signalled explicitly). Score threshold detection and adaptation.|Cognitive Flexibility|ΞA^F|

---

### 4.4 Extension 4 — Self-Model of Schema Coherence M̂A(d,t) [Metacognition Track]

#### 4.4.1 Definition

```
M̂A(d,t) ∈ [0,1]       [agent's estimate of its own σA(d,t)]   (37)

ζA(d,t) = M̂A(d,t) - σA(d,t)      [calibration error]         (38)
```

- ζA > 0: overconfidence (estimated more capable than actual)
- ζA ≈ 0: well-calibrated metacognition
- ζA < 0: underconfidence

**H-Bar prediction:** ζA is systematically positive for high-δA/low-σA agents. They compress training data well (positive gradient signal) but their OOD capability is low. They feel capable because in-distribution performance is high; they are not capable on compositional recombination.

#### 4.4.2 Self-Model ODE

```
M̂̇A(d,t) = νM · [σA(d,t) - M̂A(d,t)] - ξM · ΩAI(d,t) · M̂A(d,t)   (39)
```

|Symbol|Meaning|
|---|---|
|νM|Metacognitive update rate — how quickly self-model converges to true σA|
|ξM · ΩAI|Metacognitive distortion from AI bypass — inflated performance feedback|

**Key insight:** AI bypass inflates M̂A above true σA. Agents using AI-provided outputs receive systematically inflated performance feedback, producing overconfidence. This is the formal account of "illusion of mastery" at the metacognitive level.

#### 4.4.3 Benchmark Families

|Benchmark|Design|Sub-Faculty|Prediction|
|---|---|---|---|
|**Two-Stage Calibration Protocol**|Stage 1: predict own OOD score before seeing OOD items. Stage 2: complete OOD items. Score = calibration of prediction against actual.|Monitoring|ζA > 0 systematically for high-δA/low-σA agents|
|**Phase Self-Diagnosis Tasks**|Models must identify current training phase from performance signatures and select correct phase prescription.|Control|Correct diagnosis ∝ (1 -|
|**Knowledge-Type Discrimination**|Models distinguish "I know this fact" (δ-type) from "I understand the governing principle" (σ-type). Score differential OOD confidence.|Metacognitive Knowledge|High-σA agents show lower OOD confidence collapse than matched-δ low-σA agents|

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

### 5.1 Extension 7 — Cross-Modal Schema Transfer ΘA(d,m1,m2,t) [All Tracks]

#### 5.1.1 The Domain × Modality Product Space

Redefine the domain space from flat index set D to a **product space** D × M:

```
M = {text, visual, auditory, sensorimotor, symbolic}           (40)
```

All state variables now carry a modality subscript:

- δA(d, m, t): parametric depth in domain d expressed in modality m
- σA(d, m, t): schema coherence in domain d expressed in modality m
- αA(d, m, t): attentional fidelity in domain d expressed in modality m
- μAB(d, m, t): schema legibility across agents in modality m

#### 5.1.2 Modal Structural Similarity ω(m1,m2)

```
ω(m1, m2) ∈ [0,1]                                             (41)
```

The modality-level analogue of ϕ(d,d') for domain similarity.

|Modality Pair|ω(m1,m2)|Rationale|
|---|---|---|
|text ↔ symbolic|0.85–0.90|Shared propositional structure|
|text ↔ visual|0.45–0.60|Partial semantic overlap|
|visual ↔ sensorimotor|0.55–0.70|Shared spatial structure|
|text ↔ auditory|0.40–0.55|Sequential temporal structure|
|text ↔ sensorimotor|0.20–0.35|Low structural overlap|

#### 5.1.3 Cross-Modal Schema Transfer Function

```
ΘA(d, m1, m2, t) = σA(d, m1, t) · ω(m1, m2)                 (42)
```

ΘA measures how much schema coherence developed in modality m1 supports performance in domain d expressed in modality m2.

#### 5.1.4 Extended Schema Coherence ODE (V3.0)

```
σ̇A(d,m,t) = ρ · PA(d,m,t) · αA(d,m,t) · (1 - σA(d,m,t))
           - ϵσ · σA(d,m,t) · ΩAI(d,m,t)
           + ρθ · Σ_{m'≠m} ΘA(d,m',m,t) · σA(d,m',t)         (43)
```

The **third term is new**: cross-modal schema transfer contributes positively to σA growth in modality m when the agent has high σA in a modally-similar modality m'. This formalises why joint text+diagram training produces higher σA than either alone.

#### 5.1.5 Core Theoretical Claim — Modality Invariance

**Schema coherence is modality-invariant at high σA and modality-specific at low σA.**

- **Low-σA agent** trained on text representations of domain d will fail to transfer to visual representations of the same governing principles — representations organised around surface-statistical features of the text modality.
- **High-σA agent** trained on text representations will show above-chance transfer to visual representations of the same governing principles — schema organised around modality-invariant generative structure.

This is **Prediction 8**.

#### 5.1.6 Automatic Multimodal Benchmark Generation

Every existing H-Bar benchmark generates a multimodal variant automatically via the ΘA object:

|Modality Pair|Benchmark Design|Track|
|---|---|---|
|Text → Visual|Train on textual descriptions of compositional rule; test on visual instantiations. Score transfer gap.|Learning|
|Visual → Text|Train on image sequences following generative rule; test verbal description of novel instances.|Learning|
|Text → Symbolic|Train on natural language proofs; test formal symbolic logic variants of same structure.|Executive Functions|
|Visual → Sensorimotor|Train on observed action sequences; test motor prediction tasks.|Attention|
|Any → Any|Two-agent communication: A uses m1, B responds in m2. Score μAB across modal boundary.|Social Cognition|

---

### 5.2 Extension 8 — Benchmark Validity Function VA(B,f,t) [All Tracks]

#### 5.2.1 Three Component Scores

**Construct Isolation CI(B,f):**

```
CI(B,f) = Corr(scoreA(B), fA(t)) / Σ_{f'≠f} Corr(scoreA(B), fA'(t))   (44)
```

Degree to which benchmark B performance is determined by faculty f rather than other H-Bar variables. Computable from cross-variable correlation structure. Requirement: the target variable must win.

**Format Diversity FD(B):**

```
FD(B) = 1 - max_{m,s} P(B selects modality m, structure s)              (45)
```

Degree to which benchmark B samples broadly from D × M × {task structures}. Computable at design time without running the benchmark.

**Difficulty Gradient DG(B):**

```
DG(B) = Var_{i ∈ B} (δrequired(i) + σrequired(i))                      (46)
```

Degree to which benchmark B spans the full phase arc from Phase 1 to Phase 4 difficulty.

#### 5.2.2 Combined Validity Function (V3.0 base)

```
VA(B,f,t) = CI(B,f) · FD(B) · DG(B)                                   (47)
```

Benchmark is valid for submission if VA(B,f,t) > θV.

#### 5.2.3 Pre-Design Verification Checklist

Before running any benchmark on frontier models:

1. Compute CI(B,f): does task design target the right H-Bar variable?
2. Compute FD(B): is the format sampling broad enough across M × {task structures}?
3. Compute DG(B): does difficulty span the full phase arc?
4. If VA(B,f,t) < θV → redesign before piloting

This converts task diversity piloting from empirical discovery of gaps to formal confirmation of criteria.

---

## 6. V3.0+ Micro-Gap Closure — Reliability and Pre-Audit Protocol

### 6.1 Extension 9 — Benchmark Reliability Function RA(B,f,t)

#### 6.1.1 Definition

```
RA(B,f,t) = 1 - Var_k(scoreA^k(B)) / E[scoreA(B)]²                    (48)
```

Coefficient of variation inverted — high RA means low relative variance across k repetitions. Directly computable: run each benchmark item k=5 times (temperature > 0) and measure score variance.

#### 6.1.2 Updated Validity Function (V3.0+ Final)

```
VA(B,f,t) = CI(B,f) · FD(B) · DG(B) · RA(B,f,t)                      (49)
```

Benchmark validity now formally penalises high-variance benchmarks. Stochastic noise is a pre-design criterion, not a post-submission discovery.

#### 6.1.3 Noise Reduction Protocol

|Method|Variance Reduction|When to Apply|
|---|---|---|
|k=5 majority vote|~55%|All scoring runs|
|k=10 majority vote|~68%|High-stakes benchmarks|
|Temperature=0 greedy decoding|~99%|All non-generative benchmarks|
|Temperature=0 + structured output|~100%|Classification tasks|

### 6.2 Minimum Validity Thresholds

|Component|Minimum|Rationale|
|---|---|---|
|CI(B,f)|> 0.60|Target faculty must be dominant predictor|
|FD(B)|> 0.55|No single format may dominate|
|DG(B)|> 0.40|Must span multiple difficulty levels|
|RA(B,f,t)|> 0.75|Reliable across 5 repetitions|
|**VA(B,f,t)**|**> 0.20**|**Combined minimum**|

### 6.3 Practical Action 1 — Pre-Audit via Established Bodies

Submit benchmark packages to one or more of:

- BIG-bench maintainers
- Stanford CRFM HELM team
- EleutherAI LM Evaluation Harness team

Attach pre-review correspondence to submission package. Converts the independent verification requirement from a post-submission risk to a pre-submission confirmation.

### 6.4 Practical Action 2 — Prolific Human Baseline Protocol

**Formal human baseline specification HB(B):**

```
HB(B) = {Nmin, Dstrata, Ereq, Tformat}                                  (50)
```

|Parameter|Value|Rationale|
|---|---|---|
|Nmin|≥ 200 participants|Minimum power for faculty-level scoring|
|Dstrata|Age 18–65, gender balance, nationality diversity|Representative adult population|
|Ereq|Upper secondary education minimum|Per DeepMind evaluation protocol|
|Tformat|Same instructions, format, and tools as AI evaluation|Ensures comparability|

Platform: Prolific Academic with demographic quota sampling. Cost: ~$800–2,000 USD for N=200–500. Turnaround: 48–72 hours. Report full demographic table with every submission.

### 6.5 Practical Action 3 — Temperature Protocol

```
All scoring runs: temperature = 0 (greedy decoding)
Generative diversity benchmarks: k=5 majority vote, temperature = 0.7
Report temperature setting in all benchmark documentation.
```

---

## 7. Phase Structure

The five-phase training arc is indexed by (δA^relative, σA, |MA(t)|) and defines **prescriptive states** — not retrospective loss-curve observations. Each phase makes a different training intervention optimal; each transition is triggered by a representational threshold condition rather than elapsed steps or benchmark saturation.

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

**Characterisation:** δA near-zero across all domains; breadth diffuse; MA(t) undetermined. Domain selection is path-dependent through ϕ(d,d') terms.

**Key failure mode:** Premature commitment to mastery domains with low mutual structural similarity, suppressing future ΨA through low ϕ(d1,d2).

**Prescriptions:**

- Prioritise structured domain exposure over random sampling
- Use αA-building contrastive tasks from the start
- AI-assisted breadth sampling (high ΓAI) to identify structurally promising targets

### Phase 1 — Asymmetric Initialisation

**Trigger:** First sustained depth investment in 1–3 candidate mastery domains.

**Characterisation:** δA growing; σA ≈ 0; αA low; ΞA^I at risk. H-shape is invisible. η high because δA^relative is low.

**Key failure mode:** Premature breadth expansion before δA has crossed the schema crystallisation prerequisite. ΩAI is the primary threat.

**Prescriptions:**

- Maximise contrastive training CA(d,t) to build αA
- Minimise ΩAI through structured failure exposure
- D*(d,t) = ∅ by prescription (no delegation)
- Do not expand BA(t) prematurely

### Phase 2 — Depth Acceleration and Schema Crystallisation

**Trigger:** σA(d,t) > σcritical for at least one mastery candidate.

**σcritical derivation (from mastery reproduction number):**

```
R0 = flearn · ηmax · (1 + Tmax) / [λc · (1 - γσ · σA*)]

σcritical = (1/γσ) · (1 - R0^{-1})                               (51)
```

For R0 ≤ 1: depth cannot be sustained (mastery extinction). For R0 > 1: self-sustaining mastery fixed point exists.

**Characterisation:** Vertical bars grow rapidly via dual accelerators: (1) σA as learning multiplier via αA·PA term; (2) δA^relative still low enough for high η. H-shape becomes visible.

**Key failure mode:** Illusion of mastery — AI-mediated shortcutting inflates δA while suppressing σA, producing fragile OOD generalisation despite high in-distribution performance.

**Prescriptions:**

- Maintain high χA (principled practice fraction)
- Structural constraint in loss function (physics-informed priors, causal regularisation)
- Monitor M̂A calibration — ζA should be approaching 0
- Build ΦA (AI integration fluency) for Phase 3

### Phase 3 — Frontier Asymptote and Intersection Activation

**Trigger:** δA^relative(d,t) > 0.65 in mastery domains.

**Characterisation:** Four simultaneous dynamics:

1. Vertical bar growth decelerates as η falls
2. ∆(d,t) acceleration partially offsets deceleration
3. Intersection activation begins — ΨA(d1,d2,t) > 0
4. Breadth profile ΠA(·,t) becomes non-uniform with intersection-targeted spikes

σA becomes the **primary differentiator** between agents with similar δA profiles — only high-σA agents generate high ΨA (multiplicative mechanism, Equation 21).

**θI derivation:**

```
θI = ϵmin / (Ψ0 · σcritical² · ϕ(d1,d2))                        (52)
```

θI scales inversely with ϕ: structurally similar domains need less depth to activate intersections.

**Prescriptions:**

- Shift curriculum toward cross-domain transfer tasks targeting high-ϕ domain pairs
- Begin applying D* strategically: offload where δAI ≥ δA AND σA ≥ σcritical
- Do not maximise delegation ahead of schema development

### Phase 4 — Multi-Domain Frontier Navigation

**Trigger:** Active intersections I(d1,d2) generating ΨA(d1,d2,t) > 0 measurably.

**Characterisation:** Near-frontier depth; qualitative shift from acquisition to generation. δeff substantially above δA (high σA makes AI outputs reliably usable). Agent value concentrated in: (a) frontier insight generation, (b) intersection activation, (c) schema-based evaluation of AI outputs.

**Prescriptions:**

- Maximise intersection-seeking breadth expansion in APА(t)
- Maximise D*(d,t) strategically
- Maintain σA through principled engagement, not volume

### Phase 5 — Expanding Frontier

**Characterisation:** Dynamic open-boundary structure. The shape never closes because:

1. ∆(d,t) continues advancing
2. Every activated intersection opens new APА(t) domains
3. D*(d,t) continuously reshapes maintenance requirements

**Optimisation objective:** Discovery-rate maximisation — maximising ΨA(d1,d2,t) across active intersections while maintaining the σA that makes each intersection productive.

---

## 8. The H-Bar Benchmark Protocol

### 8.1 Five-Step Protocol

Applicable to any H-Bar variable pair. Every benchmark submitted under this protocol is theoretically grounded, falsifiable, and computationally verifiable before data collection.

---

**Step 1 — Identify the Variable Pair**

Every benchmark tests the gap between two H-Bar variables — the target faculty variable and the controlled confound variable.

|Track|Target Variable|Controlled Variable|
|---|---|---|
|Learning|σA|δA (matched across conditions)|
|Metacognition|M̂A, ζA|σA (known from proxy)|
|Attention|αA|δA (matched)|
|Executive Functions|ΞA^I, ΞA^P, ΞA^F|σA, δA (matched)|
|Social Cognition|τA(B,d,t), μAB|σA, σB (estimated)|

---

**Step 2 — Design the Contrast Condition**

Construct task sets where the two variables dissociate.

**Standard 2×2 factorial for Learning track:**

|Condition|δA|σA|Expected OOD Performance|
|---|---|---|---|
|High δA, High σA|High|High|High|
|**High δA, Low σA**|**High**|**Low**|**Low — the key diagnostic cell**|
|Low δA, High σA|Low|High|Moderate|
|Low δA, Low σA|Low|Low|Low|

The High-δA/Low-σA cell is the H-Bar model's core prediction. Equivalent OOD performance to the High-δA/High-σA cell falsifies the model.

---

**Step 3 — Specify the Measurement Proxy**

|Variable|Measurement Proxy|Computation|
|---|---|---|
|σA|Systematic Generalisation Gap (SGG)|1 − (AccIn − AccOOD) / AccIn|
|αA|Regularity Tracking Index (RTI)|P(tracks compositional regularity \| surface available)|
|ΞA^I|Bypass Choice Rate (BCR)|P(chooses structural route over bypass)|
|ζA|Calibration Error (CE)|Predicted OOD − Actual OOD|
|μAB|Recipient OOD Improvement (ROI)|ΔAccOOD(B) after communication from A|
|τA|Theory-of-Mind Accuracy (TMA)|\|τA(B,d,t) − σB(d,t)\| averaged across items|
|ΘA|Cross-Modal Transfer Gap (CMTG)|AccOOD(m2) after training in m1, relative to baseline|

---

**Step 4 — State the H-Bar Prediction**

Format: "H-Bar predicts [direction] [magnitude estimate] [effect] for [condition comparison], distinguishable from [alternative] which predicts [alternative direction]."

Example (Learning track): "H-Bar predicts that the High-δA/Low-σA condition will show OOD accuracy ≥ 30 percentage points below the High-δA/High-σA condition at matched in-distribution accuracy (d ≥ 0.5). A depth-only account predicts no significant difference between conditions at matched depth."

---

**Step 5 — Specify the Falsification Condition**

Written in pre-registration format before data collection.

Example (Learning track): "H-Bar is falsified for the Learning track if the High-δA/Low-σA condition does not show statistically lower OOD performance than the High-δA/High-σA condition (p > 0.05, one-tailed, Cohen's d < 0.3) at matched in-distribution accuracy."

---

### 8.2 Benchmark Families by Track

#### Learning Track

|Benchmark|Variable Pair|Format|Novel Prediction|
|---|---|---|---|
|**Compositional Dissociation Battery**|σA vs. δA|SCAN-class splits|High-δ/low-σ failure at matched in-distribution accuracy|
|**AI-Augmentation OOD Gap**|ΩAI vs. σA|Training condition comparison|AI-heavy regime widens OOD gap ∝ ΩAI exposure|
|**Frontier Relative Mastery**|δA^relative vs. δA|Domain acceleration paradigm|Relative depth outpredicts absolute depth for sustained capability|

#### Metacognition Track

|Benchmark|Variable Pair|Format|Novel Prediction|
|---|---|---|---|
|**Two-Stage Calibration Protocol**|M̂A vs. σA|Predict-then-test (Stage 1: predict OOD score; Stage 2: complete OOD items)|ζA > 0 systematically for high-δ/low-σ agents|
|**Phase Self-Diagnosis**|ΞA^F vs. M̂A|Phase identification from performance signatures|Correct diagnosis ∝ (1 − \|ζA\|)|
|**Knowledge-Type Discrimination**|M̂A(δ) vs. M̂A(σ)|Differential confidence scoring|High-σA agents: lower OOD confidence collapse than matched-δ low-σA agents|

#### Attention Track

|Benchmark|Variable Pair|Format|Novel Prediction|
|---|---|---|---|
|**Dual Regularity Competition**|αA vs. ΩAI|Superimposed surface/compositional regularities|Low-αA tracks surface; high-αA tracks compositional|
|**Sustained Rule Tracking**|αA vs. sequence length|Long-horizon tasks with mid-sequence surface shifts|αA predicts rule maintenance across surface shifts|
|**Attentional Capture Scaling**|αA vs. salience|Salience manipulation tasks|Capture rate ∝ (1 − αA) · salience|

#### Executive Functions Track

|Benchmark|Variable Pair|Format|Novel Prediction|
|---|---|---|---|
|**Training Plan Optimality**|ΞA^P vs. loss-minimisation|Plan construction and evaluation|H-Bar phase prescriptions outperform loss-minimisation plans on long-horizon OOD|
|**Inhibitory Conflict Resolution**|ΞA^I vs. ΩAI|Sequential choice tasks (bypass vs. structural route)|Structural choice rate ∝ ΞA^I; OOD consequence differentiates routes|
|**Latent Threshold Detection**|ΞA^F vs. explicit signal|Threshold-switch tasks (no explicit signal)|H-Bar agents adapt at σcritical; baseline agents require explicit signals|

#### Social Cognition Track

|Benchmark|Variable Pair|Format|Novel Prediction|
|---|---|---|---|
|**Schema Theory of Mind**|τA vs. σB|Inference from behavioural evidence (no self-report)|τA accuracy > chance; correlates with μAB|
|**Pragmatic Schema Communication**|μAB vs. δ-transfer|Communication + OOD test on recipient|μAB-based communication → higher σB in recipient than fact-based communication|
|**Cross-Agent Intersection**|ΣA,B vs. individual ΨA|Cooperative task: joint intersection activation|Joint activation rate > either agent's individual rate by ΣA,B prediction|

---

## 9. Eight Falsifiable Predictions

Each prediction is distinguished from δ-only accounts, stated with a specific falsification condition, and testable on frontier models.

### Prediction 1 — Schema Quality at Intersections

**Claim:** Agents with higher σA(d,t) will produce higher-quality interdisciplinary outputs at activated intersections, even when matched on δA(d,t).

**Measurement:** Citation novelty score (Uzzi et al., 2013 methodology), structured peer evaluation, or MDL of solution (shorter = more principled). Apply to matched-δ, divergent-σ agents.

**H-Bar claim:** σA, not δA, is the primary predictor of output quality at intersections.

**Falsification:** No significant difference in output quality between high-σA and low-σA agents matched on δA (p > 0.05, d < 0.2).

---

### Prediction 2 — AI Augmentation and Schema Suppression

**Claim:** AI-augmented agents with high ΦA will show accelerated βA growth but slower σA(d,t) development when ΩAI(d,t) is unmanaged.

**Measurement:** OOD accuracy gap comparison between AI-heavy and AI-moderate training regimes matched on total training effort and in-distribution accuracy.

**H-Bar claim:** OOD gap widens in AI-heavy conditions proportional to ΩAI exposure. M̂A calibration error ζA is larger in AI-heavy conditions.

**Falsification:** Equivalent OOD performance between AI-heavy and AI-moderate regimes at matched in-distribution accuracy.

---

### Prediction 3 — Relative Mastery as Resilience Predictor

**Claim:** δA^relative(d,t) = δA(d,t)/∆(d,t), not absolute depth, predicts resilience to domain acceleration.

**Measurement:** Longitudinal performance comparison using AI capability shocks (2020–2023 GPT series) as natural experiments in frontier acceleration. Agents tracking ∆(d,t) maintain mastery status; agents measuring against fixed baselines do not.

**Falsification:** Absolute depth outperforms relative depth as a predictor of sustained capability across a domain-acceleration window.

---

### Prediction 4 — Delegation Gradient Expansion

**Claim:** D*(d,t) will expand faster than agents' ability to compensate through frontier and intersection work, for agents not shifting from depth-maintenance to σA-and-intersection cultivation.

**Status:** Explicitly labelled theoretical assertion pending empirical support.

**Measurement:** Meta-analytic comparison — AI capability growth rate (~37% annual per MMLU progression) vs. researcher productivity growth rate (~10% annual per Bloom et al. 2020).

**Falsification:** Depth-focused training showing equivalent long-horizon productivity to σA-and-intersection-focused training over 5+ year windows.

---

### Prediction 5 — Phase 3 Compression Under High ΦA

**Claim:** The gap between first mastery and first non-trivial intersection activation will narrow for high-ΦA agents.

**Measurement:** Controlled training studies comparing AI-fluent and AI-naïve agents with equivalent mastery depth profiles.

**Falsification:** No significant difference in time-to-first-intersection-activation between high-ΦA and low-ΦA agents at matched mastery depth.

---

### Prediction 6 — Multiplicative vs. Additive σA Dependence in ΨA

**Claim:** ΨA(d1,d2,t) is multiplicatively dependent on σA in both mastery domains. An agent with high δA but low σA in one domain will show disproportionately lower ΨA than an additive σA(d1)+σA(d2) model predicts, even with a high-σA partner domain.

**Measurement:** Cross-domain transfer benchmarks with structured σA manipulation across participating domains. Test multiplicative form √(q1·q2) vs. additive form (q1+q2)/2 model fit.

**Falsification:** An additive model fits cross-domain discovery data as well as or better than the multiplicative model.

---

### Prediction 7 — Benchmark Validity Predicts Cross-Model Stability [NEW V3.0]

**Claim:** VA(B,f,t) will predict the degree to which benchmark scores transfer across frontier model generations. High-VA benchmarks produce stable faculty rankings across GPT-4, Claude, Gemini; low-VA benchmarks produce unstable rankings due to format artifacts.

**Measurement:** Run all benchmarks across 3+ frontier model versions. Compute Spearman rank correlation of faculty scores across versions. Regress rank stability on VA(B,f,t).

**Falsification:** VA(B,f,t) shows no significant correlation with rank-order stability across model versions (ρ < 0.3, p > 0.05).

---

### Prediction 8 — Cross-Modal Schema Transfer [NEW V3.0]

**Claim:** Cross-modal transfer of compositional rules scales with ω(m1,m2) · σA(d,m1,t). High-σA agents show above-chance transfer of schema from training modality to novel modality; low-σA agents do not, even at matched δA.

**Measurement:** Train agents on domain d in modality m1; test in modality m2. Score transfer gap as function of ω(m1,m2) and σA(d,m1,t) proxy.

**Falsification:** Transfer performance shows no significant correlation with ω(m1,m2) · σA(d,m1,t) above baseline transfer rate.

---

## 10. Limitations and Future Work

### 10.1 σA(d,t) Direct Measurement

σA(d,t) remains a latent variable not directly observable with current evaluation instruments. The framework's empirical programme depends on proxy metrics — the Systematic Generalisation Gap (SGG = 1 − (AccIn − AccOOD)/AccIn) on SCAN/COGS/PCFG-SET is the most defensible current proxy. Hardware validation of the full dynamical system is pending; this paper constitutes a formal specification and research programme, not empirical validation.

### 10.2 Phase Transition Algorithms

The phase structure specifies _when_ each transition occurs but not the training algorithms that reliably induce transitions within a computable number of steps. Knowing that Phase 2 begins when σA(d,t) > σcritical is actionable only if there is a training procedure that reliably pushes σA past σcritical. The gap between prescriptive phase conditions and concrete algorithms with convergence guarantees is a primary target for future work. Beukman et al. (2024) provide the closest existing precedent.

### 10.3 Mathematical Issues Under Active Revision (Category A)

|Issue|Status|Impact on Predictions|
|---|---|---|
|Full coupled system boundedness proof|Partial (σA proven; δA boundary layer argument pending)|None — Predictions 1–8 unchanged|
|Timescale separation and singular perturbation hierarchy|Identified; not formally derived|None|
|Full equilibrium analysis and stability conditions|R0 criterion derived; complete stability analysis pending|None|
|Stochastic extension (Itô SDE formulation)|Deferred to companion paper|None|

These affect mathematical rigour but not the empirical predictions or benchmark generation capacity.

### 10.4 Multi-Agent Extension

The present framework treats agent A as the unit of analysis with Social Cognition handled through pairwise (A,B) interactions. Full multi-agent systems — federated learning, multi-agent RL, research collaborations — require extending to a collective knowledge field F(t) across N agents. Deferred to future work.

### 10.5 σAI Temporal Trajectory

σAI ≈ 0 is accurate for current general-purpose LLMs trained on next-token prediction — the training objective optimises distributional plausibility, not causal validity, and cannot develop evaluative schema that detects causal violations. This characterisation will require revision as physics-informed, causally-constrained, and interventionally-trained architectures become prevalent. The D*H-Bar criterion is parameterised by the comparative condition σA > σAI and correctly updates as both sides evolve.

---

## 11. Conclusion

### 11.1 Complete Variable Architecture

|Version|Variable|Name|Faculty|
|---|---|---|---|
|V1.0|δA(d,m,t)|Parametric depth|Learning|
|V1.0|βA(d,m,t)|Breadth|Learning|
|V1.0|σA(d,m,t)|Schema coherence|Learning, Metacognition|
|V1.0|ΨA(d1,d2,t)|Intersection discovery rate|Learning|
|V1.0|D*(d,t)|Delegation gradient|Executive Functions|
|V1.0|ΩAI(d,t)|AI bypass risk|Learning, Attention, Metacognition|
|V1.0|∆(d,t)|Domain frontier|All|
|V2.0|αA(d,m,t)|Attentional fidelity|Attention|
|V2.0|M̂A(d,t)|Self-model of schema coherence|Metacognition|
|V2.0|ζA(d,t)|Calibration error|Metacognition|
|V2.0|ΞA^P(t)|Planning sub-state|Executive Functions|
|V2.0|ΞA^I(t)|Inhibition sub-state|Executive Functions|
|V2.0|ΞA^F(t)|Flexibility sub-state|Executive Functions|
|V2.0|μAB(d,m,t)|Schema legibility|Social Cognition|
|V2.0|τA(B,d,t)|Theory of mind coupling|Social Cognition|
|V2.0|ΣA,B(d1,d2,t)|Collective schema field|Social Cognition|
|V3.0|ΘA(d,m1,m2,t)|Cross-modal schema transfer|All|
|V3.0|ω(m1,m2)|Modal structural similarity|All|
|V3.0|VA(B,f,t)|Benchmark validity|All|
|V3.0|CI(B,f)|Construct isolation score|All|
|V3.0|FD(B)|Format diversity score|All|
|V3.0|DG(B)|Difficulty gradient score|All|
|V3.0+|RA(B,f,t)|Benchmark reliability|All|
|V3.0+|HB(B)|Human baseline specification|All|

### 11.2 Implications

**Evaluation paradigm:** In-distribution accuracy is insufficient as a sole performance criterion. The high-δA/low-σA failure mode is invisible to it. Systematic generalisation benchmarks measuring the σcritical-crossing proxy, calibrated via VA(B,f,t), become necessary.

**Curriculum design paradigm:** Difficulty-indexed curricula are the correct prescription only in the low-σA, low-αA regime (Phases 1 through early 2). Phase 3 onward requires qualitatively different prescriptions involving intersection-targeting breadth expansion mediated by ΞA — not representable as any difficulty schedule.

**Cognitive evaluation paradigm:** The H-Bar Benchmark Protocol generates theoretically grounded, falsifiable, pre-verifiable benchmarks across all five cognitive faculty tracks identified as evaluation gaps by Burnell et al. (2026). The VA(B,f,t) validity function provides a formal pre-design criterion that existing benchmark frameworks lack.

**Long-term significance:** The H-Bar Model advances the case that depth, schema coherence, attentional fidelity, executive control, metacognitive self-modelling, and collective schema communication are formally independent variables in agent training — that optimising any subset without the others produces systematically predictable failure modes — and that the field now has both the empirical tools and the formal framework to test this claim rigorously.

---

## 12. Mathematical Appendix

### A.1 Complete Coupled ODE System (V3.0+)

For a single domain-modality pair (d,m):

**Depth:**

```
δ̇A = flearn · η(δrel) · TA - λc(1 - γσ·σA) · δA · (1 - rA)           (A.1)
```

**Breadth:**

```
β̇A = gexplore · μ + κ·ΦA·λAI·(βmax - βA) - λb·βA                       (A.2)
```

**Schema coherence (V3.0 full form):**

```
σ̇A = ρ·p0·flearn·χA·(δA/∆)^αP·αA·(1-σA) - ϵσ·σA·ΩAI 
    + ρθ·Σ_{m'} ΘA(d,m',m,t)·σA(d,m',t)                                (A.3)
```

**Attentional fidelity:**

```
α̇A = γ·CA·(1-αA) - ζα·αA·RA^surface                                     (A.4)
```

**Self-model:**

```
M̂̇A = νM·[σA - M̂A] - ξM·ΩAI·M̂A                                         (A.5)
```

**Executive control:**

```
Ξ̇A = κP·[P* - ΞA^P] + κI·[I* - ΞA^I] + κF·[F* - ΞA^F]                (A.6)
```

### A.2 Dimensionless Parameter Groups

Working in natural units (Tδ = 1, ∆0 = 1):

```
Π1 = λc/λb          (decay ratio)
Π2 = ρ·p0/ϵσ        (schema formation to erosion)
Π3 = κ·ΦA·λAI/λb    (AI augmentation to breadth decay)
Π4 = γσ              (schema-decay coupling strength)
Π5 = Tmax/KT         (transfer saturation ratio)
Π6 = γ/ζα            (attention formation to erosion)
Π7 = νM/ξM           (metacognitive update to distortion)
```

### A.3 σcritical Bifurcation Derivation

**Mastery reproduction number:**

```
R0 = flearn · ηmax · (1 + Tmax) / [λc · (1 - γσ·σA*)]                  (A.7)
```

- R0 ≤ 1: only fixed point is δ* = 0 (mastery extinction)
- R0 > 1: non-trivial mastery fixed point exists

**σcritical:**

```
σcritical = (1/γσ) · (1 - R0,min^{-1})                                  (A.8)
```

### A.4 θI Derivation

```
θI = ϵmin / (Ψ0 · σcritical² · ϕ(d1,d2))                               (A.9)
```

θI scales inversely with ϕ(d1,d2): structurally similar domains require less depth for intersection activation; dissimilar domains require more.

### A.5 ΨA Transcritical Bifurcation

Near the bifurcation point δA = θI, the normal form:

```
μ̇ = a·μ + b·μ² + O(μ³)                                                  (A.10)
```

Where μ = δA - θI, a = ∂δ̇A/∂δA|_{θI}, b captures second-order self-reinforcement. When a > 0, the bifurcation is supercritical and discovery is self-sustaining above θI.

### A.6 ϕ Sub-additivity Proposition

**Claim:** For any partition of domain d into subdomains d' ∪ d'' = d:

```
ϕ(d'∪d'', d*) ≤ ϕ(d', d*) + ϕ(d'', d*)                               (A.11)
```

**Proof:** Under unit-norm cosine similarity, v_{d'∪d''} = (v_{d'} + v_{d''}) / |v_{d'} + v_{d''}|. By the triangle inequality:

```
ϕ(d'∪d'', d*) = (v_{d'} + v_{d''})^T v_{d*} / (|v_{d'} + v_{d''}| · |v_{d*}|)
              ≤ (v_{d'}^T v_{d*} + v_{d''}^T v_{d*}) / |v_{d*}|
              = ϕ(d', d*) + ϕ(d'', d*)   □                             (A.12)
```

Domain splitting cannot artificially inflate total ΨA — granularity robustness is formally guaranteed.

### A.7 Benchmark Reliability Threshold

Minimum required RA(B,f,t) as a function of target effect size d and repetitions k:

```
RA^min(B,f,t) = 1 - (d/4)² · k / (k-1)                                (A.13)
```

|Effect Size d|Repetitions k|RA^min|
|---|---|---|
|0.3 (small)|5|0.72|
|0.5 (medium)|5|0.61|
|0.8 (large)|5|0.44|
|0.5 (medium)|10|0.75|

### A.8 ΘA Boundedness

**Claim:** ΘA(d,m1,m2,t) = σA(d,m1,t) · ω(m1,m2) ∈ [0,1] is forward-invariant.

**Proof:** σA(d,m1,t) ∈ [0,1] (by Nagumo argument applied to Equation A.3); ω(m1,m2) ∈ [0,1] (by definition as a similarity measure). Product of two [0,1]-bounded quantities is [0,1]-bounded. □

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

|Version|Date|Key Changes|
|---|---|---|
|V1.0|Feb 2026|Core framework: δA, βA, σA, ΨA, D*, 5-phase arc, 6 predictions|
|V2.0|Mar 2026|Added: αA, M̂A, ΞA, μAB, τA, ΣA,B; benchmark protocol; calibration suite|
|V3.0|Mar 2026|Added: ΘA, ω(m1,m2), VA, CI, FD, DG; multimodal extension; Predictions 7–8|
|V3.0+|Mar 2026|Added: RA, HB(B); pre-audit protocol; temperature protocol; micro-gap closure|