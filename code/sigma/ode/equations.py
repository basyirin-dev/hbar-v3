import numpy as np


def sigma_critical(gamma_sigma: float, r0_min: float) -> float:
    return (1.0 / gamma_sigma) * (1.0 - r0_min ** (-1))


def sigma_ode(
    sigma: float,
    rho: float,
    p_a: float,
    alpha_a: float,
    epsilon_sigma: float,
    omega_ai: float,
) -> float:
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
