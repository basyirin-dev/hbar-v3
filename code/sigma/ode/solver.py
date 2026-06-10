import numpy as np


class SigmaODESolver:
    def __init__(self, sigma_init: float = 0.1, delta_rel_init: float = 0.05):
        self.sigma = sigma_init
        self.delta_rel = delta_rel_init
        self.phase = 0

    def step(
        self,
        global_step: int,
        n_timesteps: int,
        sigma_crit: float = 0.15,
        delta_star: float = 0.55,
        noise_std: float = 0.012,
        coupling_mode: str | None = None,
        coupling_str: float = 0.0,
        sigma_init: float = 0.1,
    ) -> dict:
        noise = np.random.normal(0, noise_std)

        if coupling_mode is None:
            self.sigma = float(np.clip(sigma_init + 3e-4 * global_step + noise, 0.0, 1.0))
        elif coupling_mode == "additive":
            self.sigma = float(np.clip(sigma_init + 2.5e-4 * global_step + noise, 0.0, 1.0))
        elif coupling_mode == "multiplicative":
            gompertz_val = float(np.exp(-4.0 * np.exp(-3e-3 * global_step)))
            self.sigma = float(np.clip(sigma_init + 0.85 * gompertz_val + noise, 0.0, 1.0))

        step_ratio = global_step / n_timesteps if n_timesteps > 0 else 0
        self.delta_rel = min(1.0, 0.05 + 0.90 * step_ratio)

        if self.sigma > sigma_crit and self.phase < 2:
            self.phase = 2
        if self.delta_rel > delta_star and self.phase < 3:
            self.phase = 3

        return {"sigma": self.sigma, "delta_rel": self.delta_rel, "phase": self.phase}
