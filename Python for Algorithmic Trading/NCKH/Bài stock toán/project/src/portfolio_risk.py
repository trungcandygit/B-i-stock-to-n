from __future__ import annotations

import numpy as np
import pandas as pd


def portfolio_variance(w1: float, sigma1: float, sigma2: float, rho: float) -> float:
    w2 = 1 - w1
    return (w1 ** 2) * sigma1 ** 2 + (w2 ** 2) * sigma2 ** 2 + 2 * w1 * w2 * sigma1 * sigma2 * rho


def min_variance_weights(sigma1: float, sigma2: float, rho: float,
                          long_only: bool = True) -> dict:
    denom = sigma1 ** 2 + sigma2 ** 2 - 2 * rho * sigma1 * sigma2
    if abs(denom) < 1e-14:
        return {"w1": np.nan, "w2": np.nan, "clipped": True,
                "warning": "Near-perfect multicollinearity (denom~0): sigma1≈sigma2 and rho≈1"}
    w1_raw = (sigma2 ** 2 - rho * sigma1 * sigma2) / denom
    clipped = not (0 <= w1_raw <= 1)
    w1 = float(np.clip(w1_raw, 0, 1)) if long_only else w1_raw
    return {"w1": w1, "w2": 1 - w1, "w1_raw": w1_raw, "clipped": clipped}


def compare_static_vs_dcca(sigma1: float, sigma2: float, rho_static: float,
                            rho_true: float, w1: float = 0.5) -> dict:
    var_static = portfolio_variance(w1, sigma1, sigma2, rho_static)
    var_true = portfolio_variance(w1, sigma1, sigma2, rho_true)
    pct_error = 100.0 * (var_static - var_true) / var_true if var_true != 0 else np.nan
    return {
        "w1": w1, "sigma1": sigma1, "sigma2": sigma2,
        "rho_static": rho_static, "rho_true": rho_true,
        "sigma_p2_static": var_static, "sigma_p2_true": var_true,
        "pct_error_variance": pct_error,
        "pct_error_vol": 100.0 * (np.sqrt(var_static) - np.sqrt(var_true)) / np.sqrt(var_true),
    }


def risk_table_over_scales(dcca_curve_df: pd.DataFrame, sigma1: float, sigma2: float,
                            rho_static: float, w1: float = 0.5) -> pd.DataFrame:
    rows = []
    for _, r in dcca_curve_df.iterrows():
        s, rho_s = r["s"], r["rho_dcca"]
        if not np.isfinite(rho_s):
            continue
        cmp_fixed = compare_static_vs_dcca(sigma1, sigma2, rho_static, rho_s, w1=w1)
        mv = min_variance_weights(sigma1, sigma2, rho_s)
        var_mv_true = portfolio_variance(mv["w1"], sigma1, sigma2, rho_s) if np.isfinite(mv["w1"]) else np.nan
        mv_static = min_variance_weights(sigma1, sigma2, rho_static)
        var_mv_static_weight_true_rho = (
            portfolio_variance(mv_static["w1"], sigma1, sigma2, rho_s)
            if np.isfinite(mv_static["w1"]) else np.nan
        )
        rows.append({
            "s": s, "rho_dcca": rho_s, "rho_static": rho_static,
            "sigma_p2_5050_static": cmp_fixed["sigma_p2_static"],
            "sigma_p2_5050_true": cmp_fixed["sigma_p2_true"],
            "pct_error_5050": cmp_fixed["pct_error_variance"],
            "w1_minvar_true": mv["w1"], "sigma_p2_minvar_true": var_mv_true,
            "w1_minvar_static": mv_static["w1"],
            "sigma_p2_minvar_using_static_weight": var_mv_static_weight_true_rho,
            "minvar_weight_clipped": mv["clipped"],
        })
    return pd.DataFrame(rows)


def regime_risk_comparison(regime_sigma: dict[str, tuple[float, float]],
                            regime_rho_dcca: dict[str, float], rho_static: float,
                            w1: float = 0.5) -> pd.DataFrame:
    rows = []
    for regime, (s1, s2) in regime_sigma.items():
        if regime not in regime_rho_dcca or not np.isfinite(regime_rho_dcca[regime]):
            continue
        cmp = compare_static_vs_dcca(s1, s2, rho_static, regime_rho_dcca[regime], w1=w1)
        cmp["regime"] = regime
        rows.append(cmp)
    return pd.DataFrame(rows).set_index("regime")


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes
    from src.dcca_core import compute_dcca_curve

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    ls = load_all_timeframes(data_path)["1D"]
    x = ls.returns["VN30"].values
    y = ls.returns["VNINDEX"].values
    sigma1, sigma2 = x.std(ddof=1), y.std(ddof=1)
    rho_static = np.corrcoef(x, y)[0, 1]

    curve = compute_dcca_curve(x, y, order=1, n_scales=20).to_frame()
    table = risk_table_over_scales(curve, sigma1, sigma2, rho_static)
    print(table.round(6))
