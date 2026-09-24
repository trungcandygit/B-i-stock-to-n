from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def slope_regression(s_values: np.ndarray, rho_values: np.ndarray) -> dict:
    s_values = np.asarray(s_values, dtype=float)
    rho_values = np.asarray(rho_values, dtype=float)
    mask = np.isfinite(s_values) & np.isfinite(rho_values) & (s_values > 0)
    log_s, rho = np.log(s_values[mask]), rho_values[mask]
    if mask.sum() < 3:
        return {"slope": np.nan, "intercept": np.nan, "se_slope": np.nan,
                "t_stat": np.nan, "p_value": np.nan, "r_squared": np.nan, "n": int(mask.sum())}
    res = stats.linregress(log_s, rho)
    return {
        "slope": res.slope, "intercept": res.intercept, "se_slope": res.stderr,
        "t_stat": res.slope / res.stderr if res.stderr > 0 else np.nan,
        "p_value": res.pvalue, "r_squared": res.rvalue ** 2, "n": int(mask.sum()),
        "significant_5pct": bool(res.pvalue < 0.05),
    }


def slope_regression_table(dcca_curves_df: pd.DataFrame, group_cols=("timeframe", "pair_x", "pair_y", "order"),
                            s_col: str = "s", rho_col: str = "rho_dcca",
                            reliable_only_col: str | None = None) -> pd.DataFrame:
    rows = []
    for keys, g in dcca_curves_df.groupby(list(group_cols)):
        keys = keys if isinstance(keys, tuple) else (keys,)
        row = dict(zip(group_cols, keys))
        row.update({f"full_range_{k}": v for k, v in slope_regression(g[s_col].values, g[rho_col].values).items()})
        if reliable_only_col is not None and reliable_only_col in g.columns:
            g_rel = g[g[reliable_only_col]]
            row.update({f"reliable_only_{k}": v for k, v in
                        slope_regression(g_rel[s_col].values, g_rel[rho_col].values).items()})
        rows.append(row)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys

    sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
    from src.data_loader import load_all_timeframes
    from src.dcca_core import compute_dcca_curve

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/vn_indices_merged_filled.csv"
    ls = load_all_timeframes(data_path)["1D"]
    x, y = ls.returns["VN30"].values, ls.returns["VNINDEX"].values
    curve = compute_dcca_curve(x, y, order=1, n_scales=30).to_frame()
    print(slope_regression(curve["s"].values, curve["rho_dcca"].values))
