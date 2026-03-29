## TIER 1A
- **ISSUE #4 [RESOLVED — Variant E, 2026-03-30]:** The parametric decay term $\lambda_c$ incorrectly references $\sigma_A$ via the rehearsal engagement rate $r_A$, which is defined in Equation 8 using only elapsed time. Resolved by restructuring §3.3 into a three-mechanism decay architecture (engagement decay / schema-mediated decay reduction / frontier obsolescence). Equation 7 revised to include $(1 - \gamma_\sigma \cdot \sigma_A)$ factor matching Appendix A.1. Equation 12 updated for consistency.
- **ISSUE #5 [RESOLVED — Variant E, 2026-03-30]:** The attentional fidelity ODE relies on surface-reward pressure which currently lacks a formal definition or measurement procedure. Resolved by adding formal definition (Eq. 29a: $R_A^{\text{surface}} = 1 - H(Y|S)/H(Y)$), proxy identification (Eq. 29b: $R_A^{\text{surface}} \approx 1 - \hat{\alpha}_A$), calibration procedure (Appendix A.4 with three-condition battery), updated §4.1.5 benchmark table to reference formal definition, and updated integration_map.md.
- **ISSUE #6 [RESOLVED — Variant D, 2026-03-30]:** The optimal sub-state values for the executive control ODE are not formally defined for each of the five training phases. Resolved by adding bifurcation-aware step functions (Eqs. 36a–36c): $P^*$ as piecewise linear function of $δ_A^{relative}$, $I^*$ as step function at $σ_{critical}$ (0.9 below, 0.4 above), $F^*$ as threshold function of $|M_A|$ and $Ψ_A^{max}$. Links V1.0 $σ_{critical}$ bifurcation to V2.0 executive control. Updated Appendix A.6 and integration_map.md.
- **ISSUE #23 [HACKATHON PRIORITY]:** The metacognitive self-model ODE lacks a formal guarantee that values remain bounded when distorted by the AI bypass term.
- **ISSUE #22 [HACKATHON PRIORITY]:** The benchmark reliability function can theoretically return negative values when the coefficient of variation exceeds one, violating the requirement for bounded validity.

## TIER 1B
- **ISSUE #1:** The primary definition of schema coherence relies on rhetorical cognitive psychology vocabulary rather than rigorous mathematical grounding.
- **ISSUE #2:** The paper treats the latent variable $\sigma_A$ as an operative state variable throughout the framework without providing a formalized computational proxy independent of downstream benchmark results.
- **ISSUE #3:** The distinctions provided in the Excess column of the $\sigma_A$ mapping table are based on temporal dynamics rather than a categorical difference in representational content.

## TIER 2
- **ISSUE #9:** The failure to distinguish H-Bar’s structural gap from reported meta-learning and training optimizations allows the reviewer to argue $\sigma$ is merely a proxy for well-optimized $\delta$.
- **ISSUE #10 [HACKATHON PRIORITY]:** The empirical prediction requires matching agents on $\delta_A$ while varying $\sigma_A$ but does not specify a protocol to independently increase schema coherence without increasing depth.
- **ISSUE #28:** The gap statement must address how engineered training distributions allow standard seq2seq models to achieve near-perfect one-shot primitive generalization on SCAN as reported by Patel et al. (2022).
- **ISSUE #29:** The framework must engage with the finding from Lake & Baroni (2023) that meta-learning improves lexical compositionality while structural gaps persist.
- **ISSUE #30:** The novelty defense must address Han & Pad’o (2024) demonstrating that gains in transformer compositional generalization often stem from training regimes rather than structural solutions.
- **ISSUE #31:** The paper must differentiate the structural $\sigma_A$ gap from the Mirage model's symbolic System-2 requirement for solving compositionality as noted by Noviello et al. (2025).
- **ISSUE #32:** The gap statements must incorporate the SLOG benchmark results from Li et al. (2023) which foreground persistent failures on unseen recursion.
- **ISSUE #33:** The framework must address Bruns (2025) which uses RASP to prove structural representability exists in transformers even when learnability fails.
- **ISSUE #34:** The paper must acknowledge that mutual exclusivity training pushed COGS lexical scores higher while structural splits remained below 1% in Jiang et al. (2022).
- **ISSUE #35:** The novelty defense needs to address how dataset cartography curricula yield gains without closing structural compositionality gaps as observed by .Ince et al. (2023).
- **ISSUE #36:** The gap statement should note that large pretrained models still exhibit lag on deeper recursion and unseen structures according to Zhou et al. (2023).
- **ISSUE #7:** The Phase 2 transition is triggered by an unobservable latent variable and lacks a formalized differential proxy signal for external verification.
- **ISSUE #8:** The paper lacks a mathematical criterion such as sensitivity analysis to demonstrate which growth-limiting variable is dominant at any given threshold.
- **ISSUE #11:** The multiplicative dependence for intersection discovery is asserted without a first-principles derivation showing why a product is necessary over a non-linear sum.
- **ISSUE #12:** The paper claims empirical motivation from model-merging for its discovery rate mechanism but provides no citations to support the synergistic emergence claim.
- **ISSUE #37:** Add a citation to Lu et al. (2024) to support the claim that merged models exhibit emergent capabilities that surpass individual parent contributions.
- **ISSUE #38:** Cite Akiba et al. (2024) regarding evolutionary model merging recipes that yield emergent cross-domain skills.
- **ISSUE #39:** Provide citation for Yadav et al. (2024) establishing that merging capable experts systematically improves zero-shot generalization.
- **ISSUE #40:** Cite Sung et al. (2023) as evidence for synergistic multimodal cross-task model merging.
- **ISSUE #41:** Cite Liu et al. (2025) to document that low-quality source domains can suppress target performance in multi-agent RL.
- **ISSUE #42:** Cite Guo et al. (2022) to support the existence of interaction-sensitive effects in cross-domain recommendation systems.
- **ISSUE #43:** Cite Serrano et al. (2024) to acknowledge review evidence that poorly matched sources harm cross-domain learning.
- **ISSUE #44:** Cite Sui et al. (2024) to support the $\alpha_A$ motivation regarding the separation of causal from shortcut features in attention.
- **ISSUE #45:** Cite Oren et al. (2020) to ground the claim that attention alignment to token-rule structure improves compositional generalization.
- **ISSUE #46:** Provide citation for Li et al. (2025) showing that hierarchical attention patterns predict behavior on unseen OOD data.
- **ISSUE #47:** Cite Liao et al. (2025) as precedent for using attention sharpness to ensure weights favor invariant structural components.
- **ISSUE #48:** Cite Jones & Fuhg (2025) as a precedent for attention-based gating inside a neural ODE framework.
- **ISSUE #49:** Cite Robertazzi et al. (2022) as motivation for formal inhibition variables in brain-inspired meta-RL.
- **ISSUE #50:** Cite Piray & Daw (2021) to ground the formal modeling of planning and cognitive control costs in RL.
- **ISSUE #51:** Cite Rmus et al. (2020) regarding the role of executive function in defining state and action spaces for reinforcement learning.
- **ISSUE #52:** Provide citation for Nair et al. (2023) which models response inhibition as a meta-parameter in unified cognitive architectures.
- **ISSUE #53:** Cite Dunovan et al. (2017) regarding the adjustment of inhibitory boundaries in response to performance feedback.
- **ISSUE #54:** Cite Wenxuan et al. (2024) to support the $\Theta_A$ motivation concerning the measurement of modality knowledge discrepancy.
- **ISSUE #55:** Cite the multimodal alignment and fusion survey by Li & Tang (2024) as prior work for cross-modal transfer logic.
- **ISSUE #56:** Cite Lin et al. (2025) for their work on contrastive modality-disentangled learning and shared stream enforcement.
- **ISSUE #57:** Cite Lu et al. (2025) regarding the Platonic Representation Hypothesis and the emergent alignment potential across modalities.
- **ISSUE #58:** Add a citation to Griot et al. (2025) regarding the MetaMedQA benchmark to support the novelty of the H-MCB calibration protocol.
- **ISSUE #59:** Cite Kim et al. (2025) concerning the ObjexMT benchmark and its treatment of jailbreak scenarios in metacognitive calibration.
- **ISSUE #60:** Provide a citation for Kaijing et al. (2024) establishing KOR-Bench as a relevant precedent for knowledge-orthogonal reasoning tasks.
- **ISSUE #61:** Cite Mishra et al. (2022) regarding LILA mathematical reasoning tasks as an existing source for robust out-of-distribution evaluation splits.
- **ISSUE #62:** Add a citation to the DMC framework by Wang et al. (2025) to ground the formal decoupling of cognitive and metacognitive abilities.

## TIER 3
- **ISSUE #26:** The hyper-precise hackathon suitability percentages are provided without any disclosed methodology or statistical derivation.
- **ISSUE #27:** The claim of a 73.41% winning probability is entirely unsupported and lacks academic foundation.
- **ISSUE #13:** The definition of AI depth is ambiguous as to whether it represents a global state-of-the-art benchmark or a specific system instance available to the agent.
- **ISSUE #14:** The mechanism by which an agent strategically redirects effort away from delegatable tasks lacks formalization within the system ODEs.
- **ISSUE #15:** The use of anthropomorphic labels for the executive control sub-components imports psychological baggage that exceeds the formal agent-training state variables.
- **ISSUE #16:** Concluding prescriptions for curriculum design and human interaction drift into advisory language for practitioners rather than staying within the formal scope.
- **ISSUE #17:** Multiple rate constants and parameters used in the ODE system are currently neither operationalized nor measurable, rendering the full system non-simulatable.
- **ISSUE #18:** The substantial financial and resource barrier created by the requirement for 200 Prolific Academic participants is not acknowledged as a limitation for replication.
- **ISSUE #19:** The lack of a formal computational method for calculating domain structural similarity and modal structural similarity is a major missing limitation.
- **ISSUE #20:** Explicitly labeling section headers with version layers makes the paper read as a sequential assembly of research phases rather than a unified theory.
- **ISSUE #21:** The abstract is heavily weighted toward V1.0 mechanisms and fails to proportionately present the framework extensions as a synthesized whole.
- **ISSUE #24:** Mapping V3.0+ variables directly to the Burnell et al. faculties appears post-hoc and opportunistic given the report's release date.
- **ISSUE #25:** The framework cites the Burnell report as a foundational taxonomy without acknowledging its status as an unvalidated technical report released in March 2026.
