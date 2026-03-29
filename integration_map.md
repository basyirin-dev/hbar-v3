# integration_map.md

| Variable | Introduced | Interacts With | Coupling Mechanism | Equation | Consistency Verified |
|---|---|---|---|---|---|
| αA(d,t) | V2.0 | σA(d,t) | Gates σA growth via multiplicative term in ODE | A.3 (updated) | NO |
| ΞA^P(t) | V2.0 | flearn(d,t), D*(d,t) | Modulates training effort allocation across phases | A.x | NO |
| ΞA^I(t) | V2.0 | ΩAI(d,t) | Inhibitory control over AI bypass risk | A.x | NO |
| ΞA^F(t) | V2.0 | Phase transition detection | Cognitive flexibility for σ-critical crossing | A.x | NO |
| M̂A(d,t) | V2.0 | σA(d,t) | Self-model of schema coherence; ζA = M̂A - σA | A.x | NO |
| ζA(d,t) | V2.0 | M̂A, PA(d,t) | Calibration error; distorts principled practice | A.x | NO |
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
