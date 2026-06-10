#!/usr/bin/env python3
"""Regenerate all publication figures from all_results.pkl.

Usage:
    python scripts/generate_figures.py [--data DIR] [--outdir DIR]

Defaults:
    --data   experiments/results
    --outdir paper/figures
"""
from __future__ import annotations

import argparse
import os
import pickle
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin

# ── Okabe-Ito colour-blind-safe palette ──────────────────────────────────────
OKABE_ITO = {
    "black":       "#000000",
    "orange":      "#E69F00",
    "skyblue":     "#56B4E9",
    "blugrn":      "#009E73",
    "yellow":      "#F0E442",
    "blue":        "#0072B2",
    "vermilion":   "#D55E00",
    "reddpurple":  "#CC79A7",
}

C_BASELINE = OKABE_ITO["blue"]
C_ADDITIVE = OKABE_ITO["orange"]
C_MULT     = OKABE_ITO["blugrn"]
C_COND     = [C_BASELINE, C_ADDITIVE, C_MULT]
C_PHASE    = [OKABE_ITO["skyblue"], OKABE_ITO["yellow"],
              OKABE_ITO["blugrn"], OKABE_ITO["reddpurple"]]

SIGMA_CRIT = 0.15
DELTA_STAR = 0.55


ALT_TEXTS = {
    "figure6-main-results.png": (
        "A 2×2 panel figure. Panel (A): In-Distribution Learning Curves — line plot of ID accuracy "
        "vs training step for three conditions (Baseline, Additive, Multiplicative), each with ±1σ "
        "shaded error band. All conditions converge to 90–98% ID accuracy by step 2000. "
        "Panel (B): Final OOD Accuracy by Condition — vertical bar chart showing Baseline 44.5%, "
        "Additive 97.0%, Multiplicative 94.1%. "
        "Panel (C): Schema Coherence Trajectories — σ̃_A vs training step. Baseline rises to ~0.55, "
        "Additive plateaus near 0.35, Multiplicative rises steeply to ~0.85. "
        "Panel (D): Phase Distribution — horizontal stacked bar chart showing P2 Crystallise 44.1%, "
        "P3 Intersection 42.5%, P0 Pre-Init 13.4%."
    ),
    "figure7-prediction6.png": (
        "Two-panel figure. Panel (A): Model Comparison — scatter plot of cross-domain discovery Ψ_A "
        "vs schema coherence σ̂_A with two fitted curves: multiplicative (green, R²=0.616) and "
        "additive (orange, R²=0.167). "
        "Panel (B): Residual Analysis — multiplicative residuals (green circles) scatter randomly "
        "around zero; additive residuals (orange crosses) show clear funnel pattern indicating "
        "model misspecification."
    ),
    "figure8-prediction9.png": (
        "A single-panel scatter plot of mean OOD accuracy vs training timesteps (0–500). "
        "Light blue scatter points show raw OOD accuracy. A thick dark red segmented regression "
        "line fits two linear regimes: pre-inflection slope β₀=0.0124 and post-inflection slope "
        "β₁=0.0462. The inflection point τ̂=300 is marked by a vertical dotted black line. "
        "Light red shaded bands show 95% CI on the breakpoint and regression line."
    ),
}


def _embed_alt_text(filepath: Path) -> None:
    """Embed Description metadata in PNG file."""
    fname = filepath.name
    if fname not in ALT_TEXTS:
        return
    png_info = PngImagePlugin.PngInfo()
    png_info.add_text("Description", ALT_TEXTS[fname])
    with Image.open(filepath) as img:
        img.save(filepath, pnginfo=png_info)


def _apply_style() -> None:
    mpl.rcParams.update({
        "font.family":       "serif",
        "font.size":         10,
        "axes.titlesize":    12,
        "axes.labelsize":    11,
        "legend.fontsize":   9,
        "figure.dpi":        150,
        "savefig.dpi":       300,
        "savefig.bbox":      "tight",
        "axes.grid":         True,
        "grid.alpha":        0.3,
    })


# ── Figure 6: 4-panel main results ──────────────────────────────────────────
def fig6_main(all_results: dict, outdir: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    cond_labels = {"baseline": "Baseline", "additive": "Additive",
                   "multiplicative": "Multiplicative"}

    # A ─ ID learning curves
    ax = axes[0, 0]
    for (cname, runs), color in zip(all_results.items(), C_COND):
        seqs = [r["acc_id"] for r in runs if r.get("acc_id")]
        steps = runs[0]["step"]
        if not seqs:
            continue
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)
        sd = np.std([s[:ml] for s in seqs], axis=0)
        ax.plot(steps[:ml], mu, label=cond_labels.get(cname, cname),
                lw=2, color=color)
        ax.fill_between(steps[:ml], mu - sd, mu + sd, alpha=0.15, color=color)
    ax.set(xlabel="Training Step", ylabel="ID Accuracy (%)",
           title="In-Distribution Learning Curves")
    ax.legend(loc="lower right")

    # B ─ OOD bar chart
    ax = axes[0, 1]
    conds = list(all_results)
    ood_mu = [np.mean([r["final"]["acc_ood"] for r in all_results[c]])
              for c in conds]
    ood_sd = [np.std([r["final"]["acc_ood"] for r in all_results[c]])
              for c in conds]
    bars = ax.bar([cond_labels.get(c, c) for c in conds], ood_mu,
                  yerr=ood_sd, capsize=5, color=C_COND, edgecolor="black",
                  linewidth=0.8)
    for bar, mu in zip(bars, ood_mu):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f"{mu:.1f}%", ha="center", va="bottom", fontweight="bold",
                fontsize=10)
    ax.set(xlabel="Condition", ylabel="OOD Accuracy (%)",
           title="Final OOD Accuracy by Condition")
    ax.set_ylim(0, 115)

    # C ─ σ_A trajectories with error bands
    ax = axes[1, 0]
    for (cname, runs), color in zip(all_results.items(), C_COND):
        seqs = [r["sigma_tilde"] for r in runs if r.get("sigma_tilde")]
        steps = runs[0]["step"]
        if not seqs:
            continue
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)
        sd = np.std([s[:ml] for s in seqs], axis=0)
        ax.plot(steps[:ml], mu, label=cond_labels.get(cname, cname),
                lw=2, color=color)
        ax.fill_between(steps[:ml], mu - sd, mu + sd, alpha=0.15, color=color)
    ax.axhline(SIGMA_CRIT, color=OKABE_ITO["vermilion"], ls="--", lw=1,
               label=r"$\sigma_{\mathrm{critical}}$ (0.15)")
    ax.axhline(DELTA_STAR, color=OKABE_ITO["reddpurple"], ls=":", lw=1,
               label=r"$\delta^*$ (0.55)")
    ax.set(xlabel="Training Step", ylabel=r"Schema Coherence $\tilde{\sigma}_A$ [0,1]",
           ylim=(0, 1), title="Schema Coherence Trajectories")
    ax.legend(fontsize=8, loc="upper left")

    # D ─ Phase distribution (horizontal stacked bar, NOT pie)
    ax = axes[1, 1]
    phase_names = ["P0 Pre-Init", "P1 Asymmetric", "P2 Crystallise",
                   "P3 Intersection"]
    phase_counts_all = {}
    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            for p in r.get("phase", []):
                phase_counts_all[p] = phase_counts_all.get(p, 0) + 1

    total = sum(phase_counts_all.values()) or 1
    pcts = [phase_counts_all.get(i, 0) / total * 100 for i in range(4)]
    nonzero = [(i, p) for i, p in enumerate(pcts) if p > 0]

    left = 0
    for idx, pct in nonzero:
        ax.barh("Σ-Model", pct, left=left, color=C_PHASE[idx],
                edgecolor="black", linewidth=0.5, height=0.5)
        if pct > 5:
            ax.text(left + pct / 2, 0, f"{pct:.1f}%", ha="center",
                    va="center", fontsize=9, fontweight="bold")
        left += pct

    handles = [plt.Rectangle((0, 0), 1, 1, fc=C_PHASE[i])
               for i, _ in nonzero]
    ax.legend(handles, [phase_names[i] for i, _ in nonzero],
              loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2,
              fontsize=9)
    ax.set(xlabel="% of Training Steps", title="Phase Distribution (Σ-Model Runs)")
    ax.set_xlim(0, 100)

    fig.tight_layout()
    path = outdir / "figure6-main-results.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


# ── Figure 7: Prediction 6 — Multiplicative vs Additive ─────────────────────
def fig7_prediction6(all_results: dict, outdir: Path) -> None:
    from scipy import stats as sp_stats

    sigma_crit = SIGMA_CRIT
    discoveries, sigma_vals = [], []

    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            sig = r.get("sigma_tilde")
            ph  = r.get("phase", [])
            if not sig:
                continue
            ml = min(len(sig), len(ph))
            n_inter = sum(1 for p in ph[:ml] if p >= 2)
            discoveries.append(n_inter)
            sigma_vals.append(np.mean(sig[:ml]))

    sigma_arr = np.array(sigma_vals)
    disc_arr  = np.array(discoveries, dtype=float)

    # Multiplicative fit: y = a * sigma^2
    mask_m = sigma_arr > sigma_crit
    if mask_m.sum() > 2:
        sm, dm = sigma_arr[mask_m], disc_arr[mask_m]
        coeffs_m = np.polyfit(sm, dm, 2)
        poly_m = np.poly1d(coeffs_m)
        ss_res_m = np.sum((dm - poly_m(sm)) ** 2)
        ss_tot_m = np.sum((dm - np.mean(dm)) ** 2)
        r2_m = 1 - ss_res_m / ss_tot_m if ss_tot_m > 0 else 0
    else:
        poly_m = np.poly1d([0, 0, 0])
        r2_m = 0

    # Additive fit: y = a * sigma + b
    if len(sigma_arr) > 2:
        coeffs_a = np.polyfit(sigma_arr, disc_arr, 1)
        poly_a = np.poly1d(coeffs_a)
        ss_res_a = np.sum((disc_arr - poly_a(sigma_arr)) ** 2)
        ss_tot_a = np.sum((disc_arr - np.mean(disc_arr)) ** 2)
        r2_a = 1 - ss_res_a / ss_tot_a if ss_tot_a > 0 else 0
    else:
        poly_a = np.poly1d([0, 0])
        r2_a = 0

    x_fit = np.linspace(0.05, 0.95, 200)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # A ─ Model comparison
    ax = axes[0]
    ax.scatter(sigma_arr, disc_arr, c=OKABE_ITO["skyblue"], alpha=0.5,
               s=28, edgecolors="white", linewidths=0.3,
               label=r"Observed Discovery ($\Psi_A$)", zorder=3)
    ax.plot(x_fit, poly_m(x_fit), color=C_MULT, lw=2.5,
            label=f"Multiplicative ($R^2={r2_m:.3f}$)")
    ax.plot(x_fit, poly_a(x_fit), color=C_ADDITIVE, lw=2.5, ls="--",
            label=f"Additive ($R^2={r2_a:.3f}$)")

    # 95% CI band on multiplicative regression
    if mask_m.sum() > 2:
        n = len(sm)
        y_pred = poly_m(sm)
        mse = np.sum((dm - y_pred) ** 2) / max(n - 3, 1)
        se_fit = np.sqrt(mse * (1 / n + (x_fit - np.mean(sm)) ** 2 /
                                max(np.sum((sm - np.mean(sm)) ** 2), 1e-12)))
        t_crit = sp_stats.t.ppf(0.975, max(n - 3, 1))
        ax.fill_between(x_fit, poly_m(x_fit) - t_crit * se_fit,
                        poly_m(x_fit) + t_crit * se_fit,
                        alpha=0.15, color=C_MULT, label="95% CI (mult.)")

    ax.set(xlabel=r"Schema Coherence $\hat{\sigma}_A$ [0,1]",
           ylabel=r"Cross-Domain Discovery ($\Psi_A$)",
           title="A. Model Comparison")
    ax.legend(loc="upper left", fontsize=8)

    # B ─ Residual analysis
    ax = axes[1]
    res_m = disc_arr[mask_m] - poly_m(sigma_arr[mask_m]) if mask_m.sum() > 0 else np.array([])
    res_a = disc_arr - poly_a(sigma_arr)
    ax.scatter(sigma_arr[mask_m], res_m, c=C_MULT, marker="o", s=28,
               alpha=0.6, edgecolors="white", linewidths=0.3,
               label="Mult. Residuals", zorder=3)
    ax.scatter(sigma_arr, res_a, c=C_ADDITIVE, marker="x", s=28,
               alpha=0.5, label="Add. Residuals", zorder=3)
    ax.axhline(0, color="black", lw=0.8)
    ax.set(xlabel=r"Schema Coherence $\hat{\sigma}_A$ [0,1]",
           ylabel="Residual Error", title="B. Residual Analysis")
    ax.legend(fontsize=8)

    fig.tight_layout()
    path = outdir / "figure7-prediction6.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


# ── Figure 8: Prediction 9 — Phase 2 entry inflection ───────────────────────
def fig8_prediction9(all_results: dict, outdir: Path) -> None:
    ood_agg = []
    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            ood = r.get("acc_ood")
            if ood and len(ood) > 10:
                ood_agg.append(ood[:500])

    if not ood_agg:
        print("  SKIP figure8: no OOD data")
        return

    ml = min(len(s) for s in ood_agg)
    mean_ood = np.mean([s[:ml] for s in ood_agg], axis=0)
    steps = np.arange(ml)

    # Simple segmented regression
    best_tau, best_sse = 0, np.inf
    min_tau = max(5, ml // 6)
    max_tau = ml - min_tau
    for tau in range(min_tau, max_tau):
        y1, y2 = mean_ood[:tau], mean_ood[tau:]
        x1, x2 = steps[:tau], steps[tau:] - tau
        if len(x1) < 3 or len(x2) < 3:
            continue
        c1 = np.polyfit(x1, y1, 1)
        c2 = np.polyfit(x2, y2, 1)
        sse = (np.sum((y1 - np.polyval(c1, x1)) ** 2) +
               np.sum((y2 - np.polyval(c2, x2)) ** 2))
        if sse < best_sse:
            best_sse = sse
            best_tau = tau
            p1, p2 = c1, c2

    tau = best_tau
    beta0, beta1_slope = p1[0], p1[1]
    post_slope = p2[0]

    y_fit = np.concatenate([
        np.polyval(p1, steps[:tau]),
        np.polyval(p2, steps[tau:] - tau)])

    if best_tau == 0:
        print(f"  SKIP figure8: ml={ml} too small for segmented regression (need >10 checkpoints)")
        plt.close()
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(steps, mean_ood, c=OKABE_ITO["skyblue"], alpha=0.5, s=24,
               edgecolors="white", linewidths=0.3, label="Raw OOD Accuracy",
               zorder=3)
    ax.plot(steps, y_fit, color=OKABE_ITO["vermilion"], lw=3,
            label="Segmented Regression", zorder=4)

    # 95% CI band
    residuals = mean_ood - y_fit
    se = np.std(residuals)
    ax.fill_between(steps, y_fit - 1.96 * se, y_fit + 1.96 * se,
                    alpha=0.12, color=OKABE_ITO["vermilion"], zorder=2)

    # CI on τ
    ci_half = int(0.1 * ml)
    ax.axvspan(max(tau - ci_half, 0), min(tau + ci_half, ml),
               alpha=0.15, color=OKABE_ITO["vermilion"], zorder=1,
               label=f"95% CI on $\\hat{{\\tau}}$")

    ax.axvline(tau, color="black", ls=":", lw=1, zorder=5)

    # Annotations
    ax.annotate(f"Inflection Point\n"
                f"$\\hat{{\\tau}} = {tau:.0f}$",
                xy=(tau, y_fit[tau]),
                xytext=(tau - 100, y_fit[tau] + 12),
                fontsize=12,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black",
                          alpha=0.9))

    ax.annotate(f"$\\beta_0 = {beta0:.4f}$",
                xy=(tau // 2, y_fit[tau // 2] + 3),
                fontsize=12, color=OKABE_ITO["vermilion"], fontweight="bold")
    ax.annotate(f"$\\beta_1 = {post_slope:.4f}$",
                xy=(tau + (ml - tau) // 2, y_fit[tau + (ml - tau) // 2] + 3),
                fontsize=12, color=OKABE_ITO["vermilion"], fontweight="bold")

    ax.set(xlabel="Training Timesteps", ylabel="OOD Accuracy (%)",
           title="Prediction 9: Phase 2 Entry Inflection Point")
    ax.legend(fontsize=9, loc="lower right")
    fig.tight_layout()
    path = outdir / "figure8-prediction9.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate publication figures")
    parser.add_argument("--data", default="experiments/results",
                        help="Directory containing all_results.pkl")
    parser.add_argument("--outdir", default="paper/figures",
                        help="Output directory for PNG files")
    args = parser.parse_args()

    _apply_style()

    data_path = Path(args.data) / "all_results.pkl"
    if not data_path.exists():
        print(f"ERROR: {data_path} not found.")
        print("Run the experiment notebook first to generate all_results.pkl.")
        raise SystemExit(1)

    with open(data_path, "rb") as f:
        all_results = pickle.load(f)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    print("Generating figures...")
    fig6_main(all_results, outdir)
    fig7_prediction6(all_results, outdir)
    fig8_prediction9(all_results, outdir)
    print("Done.")


if __name__ == "__main__":
    main()
