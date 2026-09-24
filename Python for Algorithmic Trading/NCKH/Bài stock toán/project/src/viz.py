from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({
    "figure.dpi": 100,
    "savefig.dpi": 300,
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.grid": True,
    "grid.alpha": 0.3,
})


def _save(fig, out_path: str | Path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_dcca_curve_with_ci(curve_df: pd.DataFrame, ci_df: pd.DataFrame | None,
                             title: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    s = curve_df["s"].values
    rho = curve_df["rho_dcca"].values
    ax.plot(s, rho, "o-", color="#1f77b4", label=r"$\rho_{DCCA}(s)$", markersize=4)
    if ci_df is not None and not ci_df.empty:
        ci = ci_df.reindex(s)
        ax.fill_between(s, ci["ci_lower"].values, ci["ci_upper"].values,
                         color="#1f77b4", alpha=0.2, label="95% bootstrap confidence interval")
    ax.set_xscale("log")
    ax.set_xlabel("Time scale s (log scale, number of bars)")
    ax.set_ylabel(r"$\rho_{DCCA}(s)$")
    ax.set_title(title)
    ax.axhline(0, color="gray", lw=0.8, ls="--")
    ax.legend(loc="best")
    _save(fig, out_path)


def plot_mfdcca_heatmap(rho_frame: pd.DataFrame, title: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(8, 6))
    data = rho_frame.values
    im = ax.imshow(data, aspect="auto", cmap="RdBu_r", vmin=-1, vmax=1,
                    extent=[rho_frame.columns.min(), rho_frame.columns.max(),
                            np.log10(rho_frame.index.max()), np.log10(rho_frame.index.min())])
    ax.set_xlabel("q order (multifractal)")
    ax.set_ylabel(r"$\log_{10}(s)$")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label=r"$\rho_{DCCA}(s,q)$")
    _save(fig, out_path)


def plot_regime_comparison(regime_curves: dict[str, pd.DataFrame], title: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    colors = {"low": "#2ca02c", "mid": "#7f7f7f", "high": "#d62728"}
    labels = {"low": "Low volatility (Q1)", "mid": "Mid", "high": "High volatility (Q4)"}
    for regime, df in regime_curves.items():
        if df.empty:
            continue
        ax.plot(df["s"], df["rho_dcca"], "o-", color=colors.get(regime, None),
                label=labels.get(regime, regime), markersize=4)
    ax.set_xscale("log")
    ax.set_xlabel("Time scale s (log scale)")
    ax.set_ylabel(r"$\rho_{DCCA}(s)$")
    ax.set_title(title)
    ax.legend(loc="best")
    _save(fig, out_path)


def plot_portfolio_variance_comparison(risk_df: pd.DataFrame, title: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(risk_df["s"], risk_df["sigma_p2_5050_static"], "s--", color="gray",
             label=r"$\sigma_p^2$ using static $\rho$ (full-sample Pearson)")
    ax.plot(risk_df["s"], risk_df["sigma_p2_5050_true"], "o-", color="#d62728",
             label=r"$\sigma_p^2(s)$ using $\rho_{DCCA}(s)$")
    ax.set_xscale("log")
    ax.set_xlabel("Time scale s (log scale)")
    ax.set_ylabel(r"Portfolio variance $\sigma_p^2$")
    ax.set_title(title)
    ax.legend(loc="best")
    _save(fig, out_path)


def plot_price_and_regime(prices: pd.Series, regime: pd.Series, title: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(prices.index, prices.values, color="black", lw=0.8)
    colors = {"low": "#2ca02c", "high": "#d62728"}
    for reg, color in colors.items():
        mask = regime == reg
        ax.fill_between(prices.index, prices.min(), prices.max(), where=mask.reindex(prices.index, fill_value=False),
                         color=color, alpha=0.12, step="mid")
    ax.set_title(title)
    ax.set_ylabel("Close price")
    ax.set_xlabel("Time")
    _save(fig, out_path)


def plot_sensitivity_lines(sens_df: pd.DataFrame, title: str, ylabel: str, out_path: str | Path):
    fig, ax = plt.subplots(figsize=(7, 5))
    for col in sens_df.columns:
        ax.plot(sens_df.index, sens_df[col], "o-", label=str(col), markersize=4)
    ax.set_xscale("log")
    ax.set_xlabel("Time scale s (log scale)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best")
    _save(fig, out_path)
