import numpy as np


def sigma_critical(gamma_sigma: float, r0_min: float) -> float:
    """Compute the Phase 1→2 bifurcation threshold for schema coherence.

    Maps to: Eq. ~70 in manuscript.tex (sigma_critical derivation, Proposition 4.1).

    Args:
        gamma_sigma: Schema-mediated decay protection [0, 1].
        r0_min: Minimum basic schema reproduction number (R_0 = rho * P_A * alpha_A / epsilon_sigma * Omega_SL).

    Returns:
        sigma_critical: Threshold value in [0, 1]; crossing this triggers Phase 2 entry.
    """
    return (1.0 / gamma_sigma) * (1.0 - r0_min ** (-1))


def sigma_ode(
    sigma: float,
    rho: float,
    p_a: float,
    alpha_a: float,
    epsilon_sigma: float,
    omega_ai: float,
) -> float:
    """Compute the schema coherence ODE right-hand side (d sigma_A / dt).

    Maps to: Eq. 28 in manuscript.tex (sigma_A ODE with alpha_A gating).
    Growth term: rho * P_A * alpha_A * (1 - sigma_A).
    Decay term: epsilon_sigma * sigma_A * Omega_SL.

    Args:
        sigma: Current schema coherence [0, 1].
        rho: Schema growth rate constant.
        p_a: Principled structure availability (P_A).
        alpha_a: Attentional fidelity [0, 1].
        epsilon_sigma: Shortcut suppression coefficient.
        omega_ai: Shortcut-learning pressure (Omega_SL).

    Returns:
        Time derivative d sigma_A / dt (unbounded float, should be clipped to [0,1]).
    """
    growth = rho * p_a * alpha_a * (1.0 - sigma)
    decay = epsilon_sigma * sigma * omega_ai
    return growth - decay


def delta_ode(
    delta: float,
    delta_rel: float,
    f_learn: float,
    eta: float,
    t_a: float,
    lambda_c: float,
    gamma_sigma: float,
    sigma: float,
    r_a: float,
) -> float:
    """Compute the parametric depth ODE right-hand side (d delta_A / dt).

    Maps to: Eq. 15 in manuscript.tex (depth ODE with schema-mediated decay reduction).
    Growth: f_learn * eta * T_A.
    Decay: lambda_c * (1 - gamma_sigma * sigma) * delta_A * (1 - r_A).

    Args:
        delta: Current parametric depth.
        delta_rel: Relative depth (fraction of frontier achieved), used by Gompertz eta.
        f_learn: Learning function value.
        eta: Learning efficiency (Gompertz form).
        t_a: Time-on-task (T_A).
        lambda_c: Parametric decay rate.
        gamma_sigma: Schema-mediated decay protection [0, 1].
        sigma: Schema coherence [0, 1].
        r_a: Retrieval practice indicator [0, 1].

    Returns:
        Time derivative d delta_A / dt.
    """
    decay_mod = lambda_c * (1.0 - gamma_sigma * sigma)
    return f_learn * eta * t_a - decay_mod * delta * (1.0 - r_a)


def psi_geometric(sigma_1: float, sigma_2: float, psi_0: float = 1.0, phi: float = 1.0) -> float:
    return psi_0 * phi * np.sqrt(sigma_1 * sigma_2)


def gompertz(step: int, a: float = -4.0, b: float = -3e-3) -> float:
    return float(np.exp(a * np.exp(b * step)))


def phase_transition(
    sigma: float, delta_rel: float, phase: int,
    sigma_crit: float, delta_star: float,
) -> int:
    new_phase = phase
    if sigma > sigma_crit and phase < 2:
        new_phase = 2
    if delta_rel > delta_star and phase < 3:
        new_phase = 3
    return new_phase


def additive_coupling(task_loss: float, sigma: float, coupling_strength: float) -> float:
    return task_loss * (1.0 + coupling_strength * (1.0 - sigma))


def multiplicative_coupling(task_loss: float, sigma: float, coupling_strength: float) -> float:
    return task_loss * (1.0 + coupling_strength * sigma)
