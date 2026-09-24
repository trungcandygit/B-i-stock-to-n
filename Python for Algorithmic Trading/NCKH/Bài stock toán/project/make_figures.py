"""Ve 3 hinh tu du lieu that trong nckh_dcca_results.db, dung cho bai bao DCCA/MF-DCCA.
Khong tinh toan lai gi ca - chi doc lai bang ket qua da co san va ve lai."""
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

DB = "outputs_v2/nckh_dcca_results.db"
OUT = "figures"

# Palette de phan biet duoc, khong dung do-xanh la lam nguon chinh
COLORS = {
    "VN30-VNINDEX": "#1b4f8c",
    "VN30-VN100": "#4f8cc9",
    "VN100-VNINDEX": "#8fb8e0",
    "weighted_real-VN30": "#c9622a",
}

plt.rcParams.update({
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

conn = sqlite3.connect(DB)

# ---------- Hinh 4.1: duong cong rho_DCCA(s) tai M30, bac detrend m=1 ----------
fig, ax = plt.subplots(figsize=(6.5, 4.3))

pairs = [
    ("VN30", "VNINDEX", "VN30-VNINDEX"),
    ("VN30", "VN100", "VN30-VN100"),
    ("VN100", "VNINDEX", "VN100-VNINDEX"),
    ("MID_CAP_PROXY_weighted_real", "VN30", "weighted_real-VN30"),
]
for px, py, label in pairs:
    df = pd.read_sql(
        "SELECT s, rho_dcca, reliable FROM dcca_curves "
        "WHERE timeframe='M30' AND [order]=1 AND pair_x=? AND pair_y=? ORDER BY s",
        conn, params=(px, py),
    )
    ax.plot(df["s"], df["rho_dcca"], marker="o", markersize=3, linewidth=1.6,
            label=label, color=COLORS[label])

ax.axvline(217, color="gray", linestyle="--", linewidth=1)
ax.text(230, 0.05, "s_max = 217", va="bottom", ha="left", fontsize=9, color="gray")
ax.set_xscale("log")
ax.set_xlabel("Thang thời gian s (số nến M30, thang log)")
ax.set_ylabel(r"$\rho_{DCCA}(s)$")
ax.set_title("Hình 4.1 — Tương quan DCCA theo thang thời gian,\nkhung M30 (bậc detrend m=1)", fontsize=12)
ax.set_ylim(-0.1, 1.05)
ax.legend(loc="lower right", frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig(f"{OUT}/hinh_4_1_dcca_curves_m30.png", dpi=300)
plt.close(fig)

# ---------- Hinh 4.2: weighted_real-VN30 theo che do bien dong, tat ca timeframe ----------
fig, axes = plt.subplots(1, 4, figsize=(12.5, 3.6), sharey=True)
timeframes = ["1D", "M30", "H1", "H4"]
regime_colors = {"low": "#4f8cc9", "mid": "#c9a53a", "high": "#c9622a"}
regime_labels = {"low": "Biến động thấp", "mid": "Biến động trung bình", "high": "Biến động cao"}

for ax, tf in zip(axes, timeframes):
    for regime in ["low", "mid", "high"]:
        df = pd.read_sql(
            "SELECT s, rho_dcca FROM regime_dcca_curves "
            "WHERE timeframe=? AND pair_x='MID_CAP_PROXY_weighted_real' AND pair_y='VN30' "
            "AND regime=? ORDER BY s",
            conn, params=(tf, regime),
        )
        if len(df) == 0:
            continue
        ax.plot(df["s"], df["rho_dcca"], marker="o", markersize=2.5, linewidth=1.4,
                label=regime_labels[regime], color=regime_colors[regime])
    ax.set_xscale("log")
    ax.set_title(tf, fontsize=11)
    ax.set_xlabel("s")

axes[0].set_ylabel(r"$\rho_{DCCA}(s)$" + "\n(weighted_real – VN30)")
axes[0].set_ylim(0.3, 1.0)
axes[-1].legend(loc="lower right", frameon=False, fontsize=8)
fig.suptitle("Hình 4.2 — Tương quan weighted_real–VN30 theo chế độ biến động, 4 khung giao dịch", y=1.03)
fig.tight_layout()
fig.savefig(f"{OUT}/hinh_4_2_regime_weighted_real.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------- Hinh 5.1: sai so phuong sai danh muc, weighted_real, 1D ----------
df = pd.read_sql(
    "SELECT regime, sigma_p2_static, sigma_p2_true, pct_error_variance FROM portfolio_risk_regime_comparison "
    "WHERE timeframe='1D' AND pair_x='MID_CAP_PROXY_weighted_real' AND pair_y='VN30' AND w1=0.5",
    conn,
)
df["regime_vi"] = df["regime"].map({"low": "Biến động thấp", "mid": "Biến động trung bình", "high": "Biến động cao"})

fig, ax = plt.subplots(figsize=(6, 4))
x = range(len(df))
width = 0.35
ax.bar([i - width/2 for i in x], df["sigma_p2_static"], width, label=r"$\sigma^2_{static}$ (Pearson tĩnh, 1D toàn mẫu)", color="#8fb8e0")
ax.bar([i + width/2 for i in x], df["sigma_p2_true"], width, label=r"$\sigma^2_{true}$ ($\rho_{DCCA}(s)$ theo chế độ)", color="#c9622a")
for i, row in df.iterrows():
    ax.text(i, max(row["sigma_p2_static"], row["sigma_p2_true"]) * 1.03,
            f"{row['pct_error_variance']:+.2f}%", ha="center", fontsize=9)
ax.set_xticks(list(x))
ax.set_xticklabels(df["regime_vi"])
ax.set_ylabel(r"Phương sai danh mục 50/50 $\sigma_p^2$")
ax.set_title("Hình 5.1 — Sai số phương sai danh mục Markowitz\n(cặp weighted_real–VN30, khung 1D)")
ax.legend(loc="upper left", frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig(f"{OUT}/hinh_5_1_portfolio_error.png", dpi=300)
plt.close(fig)

conn.close()
print("Da ve xong 3 hinh trong thu muc figures/")
