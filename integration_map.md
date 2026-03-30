# integration_map.md

| Variable | Introduced | Interacts With | Coupling Mechanism | Equation | Consistency Verified |
|---|---|---|---|---|---|
| αA(d,t) | V2.0 | σA(d,t), R_A^{surface}(d,t) | Gates σA growth via multiplicative term in ODE 28; eroded by surface-reward pressure via ODE 29 | 28, 29, A.4 | NO |
| R_A^{surface}(d,t) | V2.0 | αA(d,t) | Surface-reward pressure — erodes attentional fidelity via $ζ_α · R_A^{surface} · α_A$ term in ODE 29. Formal definition: $1 - H(Y\|S)/H(Y)$ (Eq. 29a). Proxy: $1 - \hat{α}_A = 1 - \text{Acc}_{OOD\text{-struct}}/\text{Acc}_{ID}$ (Eq. 29b). Calibration procedure in Appendix A.4. | 29, 29a, 29b, A.4 | YES |
| ΞA^P(t) | V2.0 | δ_A^{relative}(d*,t) | Planning relaxes toward (1 − δ_A^{rel}); rigid when depth low, relaxed near frontier. Eq. 36a (bifurcation-aware step). | 36, 36a, A.6 | YES |
| ΞA^I(t) | V2.0 | σA(d*,t), σ_critical | Inhibition: 0.9 below σ_critical, 0.4 above. Step function at bifurcation connects V1.0 σ_critical to V2.0 executive control. Eq. 36b. | 36, 36b, A.6 | YES |
| ΞA^F(t) | V2.0 | |M_A(t)|, Ψ_A^{max}(t) | Flexibility: 0.3 when |M_A|<2 and Ψ=0; 0.9 otherwise. Grows with mastery and intersection activity. Eq. 36c. | 36, 36c, A.6 | YES |
| M̂A(d,t) | V2.0 | σA(d,t), Ω_AI | Self-model of schema coherence; ζA = M̂A - σA. Nagumo boundedness proven (§4.4.2). Steady-state: M̂A* = σA/(1 + Ω_AI/Π_7) ≤ σA (Eq. 39a). Overconfidence transient; underconfidence at equilibrium under sustained Ω_AI. | 39, 39a, A.5 | YES |
| ζA(d,t) | V2.0 | M̂A, σA, PA(d,t), αA, Ω_AI | Calibration error; distorts principled practice. Derived ODE (Eq. 38a): restoring force (−ν_M ζ_A) opposes overconfidence; AI bypass terms inflate ζ_A. Bounded in [−1,1] by Nagumo on M̂A. | 38, 38a, A.5a | YES |
| μAB(d,t) | V2.0 | σA, σB, ϕ | Schema legibility: A's σA readable by B | A.x | NO |
| τA(B,d,t) | V2.0 | σB(d,t) | A's model of B's schema; ζAB = τA - σB | A.x | NO |
| ΣA,B(d1,d2,t) | V2.0 | μAB, μBA, ϕ | Collective schema field (cross-agent ΨA) | A.x | NO |
| ΘA(d,m1,m2,t) | V3.0 | σA(d,m,t), ω(m1,m2) | Cross-modal schema transfer | A.x | NO |
| ω(m1,m2) | V3.0 | ΘA | Modal structural similarity coefficient | A.x | NO |
| VA(B,f,t) | V3.0 | CI, FD, DG, RA | Benchmark validity composite | A.x | NO |
| CI(B,f) | V3.0 | VA | Construct isolation score | A.x | NO |
| FD(B) | V3.0 | VA | Format diversity score | A.x | NO |
| DG(B) | V3.0 | VA | Difficulty gradient score | A.x | NO |
| RA(B,f,t) | V3.0+ | VA | Reliability function | A.13 | NO |
| HB(B) | V3.0+ | Submission protocol | Human baseline specification | A.x | NO |
| λc eff = λc·(1−γσ·σA) | V1.0 (resolved Issue #4) | σA, λc, rA | Schema-mediated decay reduction; three-mechanism architecture (engagement/schema/frontier) | 7, 12, A.1 | YES |
| rA(d,t) | V1.0 | τA (elapsed time) | Engagement decay — purely temporal, no σA dependence | 8 | YES |
