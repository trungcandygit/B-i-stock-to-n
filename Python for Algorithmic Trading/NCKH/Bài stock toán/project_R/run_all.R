#!/usr/bin/env Rscript
# Full replication of every number, table and figure in the manuscript
# "Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam".
# Run from project_R/:   Rscript run_all.R
# Packages: sandwich, ggplot2 (R >= 4.3).
suppressPackageStartupMessages({ library(sandwich); library(ggplot2) })
source("R/dcca.R")
OUT <- "outputs"; dir.create(OUT, showWarnings = FALSE); dir.create(file.path(OUT, "figures"), showWarnings = FALSE)
DATA <- "../project/data/vn_indices_merged_filled.csv"
TF <- c("1D", "M30", "H1", "H4")
W_REAL <- 1316288 / 1928303        # VN30 / VN100 free-float cap, HOSE factsheet 31 May 2024
SYNC <- as.Date(c("2017-01-03", "2024-12-09"))
CRISIS <- list(c("2018-01-01", "2018-12-31"), c("2020-01-01", "2020-06-30"), c("2022-04-01", "2022-11-30"))
CALM   <- list(c("2016-01-01", "2017-12-31"), c("2023-01-01", "2024-12-31"))
res <- list()                      # scalar results quoted in the text
say <- function(...) cat(format(Sys.time(), "[%H:%M:%S] "), ..., "\n", sep = "")
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)

# ---------------------------------------------------------------- data
raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
load_tf <- function(tf) {
  d <- raw[raw$timeframe == tf, ]
  d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
  r <- data.frame(dt = d$dt[-1], date = as.Date(d$dt[-1]))
  for (c in c("VN30", "VN100", "VNINDEX")) r[[c]] <- diff(log(d[[c]]))
  p30 <- d$VN30; p100 <- d$VN100
  fit <- lm(r$VN100 ~ r$VN30)
  a <- coef(fit)[1]; b <- coef(fit)[2]
  w_heur <- cor(r$VN30, r$VN100)                          # = beta * sd30 / sd100
  r$Pcap  <- (r$VN100 - W_REAL * r$VN30) / (1 - W_REAL)
  r$Pheur <- (r$VN100 - w_heur * r$VN30) / (1 - w_heur)
  r$Pratio <- diff(log(p100 / p30))                        # = R100 - R30
  r$Pres  <- unname(residuals(fit))
  attr(r, "ols") <- data.frame(timeframe = tf, alpha = a, beta = b, r_squared = summary(fit)$r.squared,
                               n = nrow(r), w_heur = w_heur, one_minus_w_heur = 1 - w_heur,
                               amplification_heur = 1 / (1 - w_heur), row.names = NULL)
  r
}
R <- setNames(lapply(TF, load_tf), TF)
ols <- do.call(rbind, lapply(R, attr, "ols")); wcsv(ols, "04_proxy_regression.csv")
PAIRS <- list(c("VN30", "VNINDEX"), c("VN30", "VN100"), c("VN100", "VNINDEX"),
              c("Pcap", "VN30"), c("Pheur", "VN30"), c("Pratio", "VN30"), c("Pres", "VN30"))
pname <- function(p) paste(p, collapse = "-")
NESTED <- c("VN30-VNINDEX", "VN30-VN100", "VN100-VNINDEX")
for (tf in TF) say(tf, ": N=", nrow(R[[tf]]), " ", format(min(R[[tf]]$date)), " .. ", format(max(R[[tf]]$date)))

# ---------------------------------------------------------------- Table 1 descriptive statistics
skw <- function(x) { m <- mean(x); mean((x - m)^3) / mean((x - m)^2)^1.5 }
krt <- function(x) { m <- mean(x); mean((x - m)^4) / mean((x - m)^2)^2 }
desc <- do.call(rbind, lapply(c("VN30", "VN100", "VNINDEX", "Pcap"), function(v) do.call(rbind, lapply(TF, function(tf) {
  x <- R[[tf]][[v]]; n <- length(x); S <- skw(x); K <- krt(x)
  data.frame(index = v, freq = tf, n = n, first = min(R[[tf]]$date), last = max(R[[tf]]$date),
             mean = mean(x), median = median(x), sd = sd(x), min = min(x), max = max(x),
             skew = S, kurtosis = K, jb = n / 6 * (S^2 + (K - 3)^2 / 4))
}))))
wcsv(desc, "01_descriptive_stats.csv")

# ---------------------------------------------------------------- Table 3 reliability thresholds (white-noise MC)
say("Monte Carlo reliability thresholds")
rel <- do.call(rbind, lapply(TF, function(tf) {
  n <- nrow(R[[tf]]); z <- reliable_smax(n, n_repeats = 167)
  wcsv(cbind(timeframe = tf, z$curve), paste0("03_reliability_curve_", tf, ".csv"))
  data.frame(timeframe = tf, n = n, s_rel = z$s_max, first_violation = z$first_violation, n_sims = z$n_sims)
}))
wcsv(rel, "03_reliability_smax.csv"); print(rel)
SREL <- setNames(rel$s_rel, rel$timeframe)

# ---------------------------------------------------------------- DCCA curves (m = 1, 2, 3)
say("DCCA curves")
curve_of <- function(d, p, order = 1, n_scales = 30) dcca_curve(d[[p[1]]], d[[p[2]]], order = order, n_scales = n_scales)
dc <- do.call(rbind, lapply(TF, function(tf) do.call(rbind, lapply(PAIRS, function(p) do.call(rbind, lapply(1:3, function(m) {
  cv <- curve_of(R[[tf]], p, m); cbind(timeframe = tf, pair = pname(p), order = m, cv, reliable = cv$s <= SREL[tf])
}))))))
wcsv(dc, "06_dcca_curves.csv")
dc1 <- dc[dc$order == 1, ]

# ---------------------------------------------------------------- Table 2 average DCCA (Panel A sync window, Panel B full)
avg_tab <- function(sample) do.call(rbind, lapply(TF, function(tf) {
  d <- R[[tf]]; if (sample == "A") d <- d[d$date >= SYNC[1] & d$date <= SYNC[2], ]
  rho <- sapply(PAIRS[1:4], function(p) { cv <- curve_of(d, p); mean(cv$rho_dcca[cv$s <= SREL[tf]]) })
  names(rho) <- sapply(PAIRS[1:4], pname)
  data.frame(panel = sample, timeframe = tf, n = nrow(d), first = min(d$date), last = max(d$date),
             nested_mean = mean(rho[NESTED]), t(rho), gap = mean(rho[NESTED]) - rho["Pcap-VN30"], check.names = FALSE)
}))
tab2 <- rbind(avg_tab("A"), avg_tab("B")); wcsv(tab2, "02_table2_average_dcca.csv"); print(tab2)

# detrending-order sensitivity, VN30-VNINDEX daily (reliable range)
ord <- sapply(1:3, function(m) { z <- dc[dc$timeframe == "1D" & dc$pair == "VN30-VNINDEX" & dc$order == m, ]; mean(z$rho_dcca[z$reliable]) })
res$detrend_order_rho <- ord

# proxy diagnostics
pc <- do.call(rbind, lapply(TF, function(tf) { d <- R[[tf]]; cm <- cor(d[, c("Pcap", "Pheur", "Pratio", "Pres")])
  data.frame(timeframe = tf, pcap_vs_alt_min = min(cm["Pcap", -1]), pcap_vs_alt_max = max(cm["Pcap", -1]),
             alt_min = min(cm[2:4, 2:4][upper.tri(cm[2:4, 2:4])]), alt_max = max(cm[2:4, 2:4][upper.tri(cm[2:4, 2:4])]),
             sd_Pcap = sd(d$Pcap), sd_Pheur = sd(d$Pheur)) }))
wcsv(pc, "05_proxy_comparison.csv")
alt_rho <- sapply(TF, function(tf) { z <- dc1[dc1$timeframe == tf & dc1$pair %in% c("Pheur-VN30", "Pratio-VN30", "Pres-VN30") & dc1$reliable, ]
  sapply(split(z$rho_dcca, z$pair), mean) })
res$alt_proxy_mean_rho_range <- range(alt_rho)

# Jensen term bound (daily): 0.5 * [w s30^2 + (1-w) smid^2 - s100^2], smid = sd(Pcap)
d1 <- R[["1D"]]
res$jensen_delta <- 0.5 * (W_REAL * var(d1$VN30) + (1 - W_REAL) * var(d1$Pcap) - var(d1$VN100))

# ---------------------------------------------------------------- MF-DCCA
say("MF-DCCA")
mf <- do.call(rbind, lapply(TF, function(tf) do.call(rbind, lapply(PAIRS, function(p) {
  z <- mfdcca(R[[tf]][[p[1]]], R[[tf]][[p[2]]]); cbind(timeframe = tf, pair = pname(p), z) }))))
wcsv(mf, "08_mfdcca_hq.csv")
mfw <- do.call(rbind, lapply(split(mf, list(mf$timeframe, mf$pair), drop = TRUE), function(z)
  data.frame(timeframe = z$timeframe[1], pair = z$pair[1], dh_xy = z$lambda_xy[z$q == -5] - z$lambda_xy[z$q == 5],
             h2_x = z$h_x[z$q == 2], h2_y = z$h_y[z$q == 2])))
wcsv(mfw, "09_mfdcca_width.csv")
spec <- do.call(rbind, lapply(split(mf[mf$timeframe == "1D", ], mf$pair[mf$timeframe == "1D"]), function(z)
  cbind(pair = z$pair[1], multifractal_spectrum(z$q, z$lambda_xy))))
wcsv(spec, "09b_mfdcca_spectrum_1D.csv")

# ---------------------------------------------------------------- regimes
roll_sd <- function(x, w) { mp <- max(5, w %/% 2); n <- length(x)
  sapply(seq_len(n), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
eq_window <- function(d) max(5, round(20 * median(table(d$date))))
regime_rho <- function(d, mask, p, target) {
  sub <- d[mask, ]; cv <- dcca_curve(sub[[p[1]]], sub[[p[2]]], order = 1, n_scales = 15)
  i <- which.min(abs(cv$s - target)); list(rho = cv$rho_dcca[i], s = cv$s[i], n = nrow(sub))
}
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
fr <- function(rl, rh, dlt, nh, nl) { rs <- rh / sqrt(1 + dlt * (1 - rh^2))
  se <- sqrt((1 - rs^2)^2 / nh + (1 - rl^2)^2 / nl); t <- (rs - rl) / se
  c(rho_star = rs, se = se, t = t, p_one_sided = 1 - pnorm(t)) }

REG <- list()
for (tf in TF) {
  d <- R[[tf]]; w <- eq_window(d); rv <- roll_sd(d$VNINDEX, w)
  q <- quantile(rv, c(.25, .75), na.rm = TRUE, type = 7)
  lab <- ifelse(is.na(rv), NA, ifelse(rv < q[1], "low", ifelse(rv > q[2], "high", "mid")))
  REG[[tf]] <- list(window = w, rv = rv, q = q, low = !is.na(lab) & lab == "low", high = !is.na(lab) & lab == "high")
}
chron <- list(high = in_periods(d1$date, CRISIS), low = in_periods(d1$date, CALM))
res$n_crisis_days <- sum(chron$high); res$n_calm_days <- sum(chron$low)
# crisis-episode diagnostics: peak-to-trough drawdown of VNINDEX and share of days in the top-quartile volatility regime
px1 <- raw[raw$timeframe == "1D", ]; px1 <- px1[order(px1$dt), ]; px1$date <- as.Date(px1$dt)
ep <- do.call(rbind, lapply(c(CRISIS, list(c("2025-03-01", "2025-06-30"))), function(p) {
  z <- px1[px1$date >= as.Date(p[1]) & px1$date <= as.Date(p[2]), ]
  dd <- min(z$VNINDEX / cummax(z$VNINDEX) - 1)
  m <- d1$date >= as.Date(p[1]) & d1$date <= as.Date(p[2])
  data.frame(start = p[1], end = p[2], trading_days = sum(m), max_drawdown_pct = 100 * dd,
             share_high_vol_days = mean(REG[["1D"]]$high[m]), peak_vol_ann_pct = 100 * sqrt(252) * max(REG[["1D"]]$rv[m], na.rm = TRUE))
}))
wcsv(ep, "11_crisis_episode_diagnostics.csv"); print(ep)
res$vol_quartiles_ann_pct <- 100 * sqrt(252) * REG[["1D"]]$q

fr_rows <- list()
for (panel in c("A", "B")) for (p in PAIRS) {
  m <- if (panel == "A") chron else REG[["1D"]]
  lo <- regime_rho(d1, m$low, p, 20); hi <- regime_rho(d1, m$high, p, 20)
  dlt <- var(d1$VN30[m$high]) / var(d1$VN30[m$low]) - 1
  fr_rows[[length(fr_rows) + 1]] <- data.frame(panel = panel, pair = pname(p), rho_low = lo$rho, rho_high = hi$rho,
    s_used = lo$s, n_low = lo$n, n_high = hi$n, delta = dlt, t(fr(lo$rho, hi$rho, dlt, hi$n, lo$n)))
}
tab4 <- do.call(rbind, fr_rows); wcsv(tab4, "10_table4_forbes_rigobon.csv"); print(tab4[tab4$pair == "Pcap-VN30", ])

# ---------------------------------------------------------------- portfolio relative variance error
re_fun <- function(rs, rr, s1, s2) (rs - rr) / (0.5 * (s1 / s2 + s2 / s1) + rr)
pf <- do.call(rbind, lapply(c("A", "B"), function(panel) do.call(rbind, lapply(PAIRS[1:4], function(p) {
  s1 <- sd(d1[[p[1]]]); s2 <- sd(d1[[p[2]]]); rs <- cor(d1[[p[1]]], d1[[p[2]]])
  z <- tab4[tab4$panel == panel & tab4$pair == pname(p), ]
  data.frame(panel = panel, pair = pname(p), sigma1 = s1, sigma2 = s2, ratio = s1 / s2, adj = 0.5 * (s1 / s2 + s2 / s1),
             rho_static = rs, rho_low = z$rho_low, rho_high = z$rho_high,
             RE_low = 100 * re_fun(rs, z$rho_low, s1, s2), RE_high = 100 * re_fun(rs, z$rho_high, s1, s2),
             RE_low_eqvol = 100 * re_fun(rs, z$rho_low, 1, 1), RE_high_eqvol = 100 * re_fun(rs, z$rho_high, 1, 1))
}))))
wcsv(pf, "14_portfolio_relative_error.csv"); print(pf)
# maximum |RE| for nested cash pairs across frequencies (rolling-quartile regimes, own-frequency static rho)
pfx <- do.call(rbind, lapply(TF, function(tf) { d <- R[[tf]]; do.call(rbind, lapply(PAIRS[1:3], function(p) {
  rs <- cor(d[[p[1]]], d[[p[2]]]); s1 <- sd(d[[p[1]]]); s2 <- sd(d[[p[2]]])
  do.call(rbind, lapply(c("low", "high"), function(g) { rr <- regime_rho(d, REG[[tf]][[g]], p, REG[[tf]]$window)$rho
    data.frame(timeframe = tf, pair = pname(p), regime = g, rho_static = rs, rho_regime = rr, RE = 100 * re_fun(rs, rr, s1, s2)) })) })) }))
wcsv(pfx, "14b_portfolio_nested_all_frequencies.csv")

# ---------------------------------------------------------------- Tables 5-6 scaling regressions (M30, HAC)
sc <- do.call(rbind, lapply(TF, function(tf) do.call(rbind, lapply(PAIRS, function(p) {
  z <- dc1[dc1$timeframe == tf & dc1$pair == pname(p), ]
  rbind(cbind(timeframe = tf, pair = pname(p), range = "full", scale_regression(z$s, z$rho_dcca)),
        cbind(timeframe = tf, pair = pname(p), range = "reliable", scale_regression(z$s[z$reliable], z$rho_dcca[z$reliable])))
}))))
wcsv(sc, "20_scale_regressions_hac.csv"); print(sc[sc$timeframe == "M30", c("pair", "range", "intercept", "slope", "hac_se_slope", "p_slope", "r_squared", "n")])
res$m30_scale_grid <- range(dc1$s[dc1$timeframe == "M30" & dc1$pair == "VN30-VNINDEX"])

# ---------------------------------------------------------------- Table 7 weight sensitivity
say("weight sensitivity")
w_grid <- c(0.60, 0.65, W_REAL, 0.72, 0.75)
t7 <- do.call(rbind, lapply(w_grid, function(w) {
  mk <- function(d) { d$Pw <- (d$VN100 - w * d$VN30) / (1 - w); d }
  a <- mk(d1); m30 <- mk(R[["M30"]])
  cv <- dcca_curve(a$Pw, a$VN30); rho_mean <- mean(cv$rho_dcca[cv$s <= SREL["1D"]])
  cvm <- dcca_curve(m30$Pw, m30$VN30); slope <- scale_regression(cvm$s, cvm$rho_dcca)
  lo <- regime_rho(a, chron$low, c("Pw", "VN30"), 20)$rho; hi <- regime_rho(a, chron$high, c("Pw", "VN30"), 20)$rho
  nested <- tab2$nested_mean[tab2$panel == "B" & tab2$timeframe == "1D"]
  data.frame(w = w, rho_mean_1D = rho_mean, gap_vs_nested = nested - rho_mean, slope_M30 = slope$slope,
             p_slope = slope$p_slope, rho_low = lo, rho_high = hi, tightening = hi - lo)
}))
wcsv(t7, "07_table7_weight_sensitivity.csv"); print(t7)

# ---------------------------------------------------------------- figures (ggplot2)
say("figures")
theme_paper <- theme_bw(base_size = 9, base_family = "sans") +
  theme(panel.grid.minor = element_blank(), legend.position = "bottom", legend.title = element_blank(),
        strip.background = element_rect(fill = "grey95"))
# Figure 1: rolling volatility (annualized %, 20-day) with quartile thresholds and crisis shading
f1 <- data.frame(date = d1$date, vol = 100 * sqrt(252) * REG[["1D"]]$rv)
shade <- data.frame(start = as.Date(sapply(CRISIS, `[`, 1)), end = as.Date(sapply(CRISIS, `[`, 2)),
                    lab = c("2018 margin\ncontraction", "2020 COVID-19\nshock", "2022 bond-market\nfreeze"))
ytop <- max(f1$vol, na.rm = TRUE)
g1 <- ggplot(f1, aes(date, vol)) +
  geom_rect(data = shade, aes(xmin = start, xmax = end, ymin = -Inf, ymax = Inf), inherit.aes = FALSE, fill = "grey82", alpha = .7) +
  geom_line(linewidth = .35) +
  geom_hline(yintercept = 100 * sqrt(252) * REG[["1D"]]$q, linetype = c("dashed", "dotted")) +
  annotate("text", x = shade$start + (shade$end - shade$start) / 2, y = ytop * c(1.10, 1.22, 1.10), label = shade$lab,
           size = 2.5, family = "sans", lineheight = .85) +
  scale_y_continuous(limits = c(0, ytop * 1.3), expand = c(0, 0)) + scale_x_date(date_breaks = "2 years", date_labels = "%Y") +
  labs(x = NULL, y = "20-day rolling volatility (annualized, %)") + theme_paper
ggsave(file.path(OUT, "figures", "fig1_volatility_regimes.png"), g1, width = 6.5, height = 3.2, dpi = 600)
ggsave(file.path(OUT, "figures", "Fig1.eps"), g1, width = 6.5, height = 3.2, device = cairo_ps)
# Figure 2: multiscale DCCA curves, four panels
lab_tf <- c("1D" = "(a) Daily (1D)", "M30" = "(b) 30-minute (M30)", "H1" = "(c) 1-hour (H1)", "H4" = "(d) 4-hour (H4)")
PAIR_LEV <- c("VN30-VN100", "VN30-VNINDEX", "VN100-VNINDEX", "Pcap-VN30")
PAIR_LAB <- list("VN30-VN100", "VN30-VNINDEX", "VN100-VNINDEX", expression(P[cap]*"-VN30"))
f2 <- dc1[dc1$pair %in% PAIR_LEV, ]; f2$panel <- factor(lab_tf[f2$timeframe], levels = lab_tf)
f2$pair <- factor(f2$pair, levels = PAIR_LEV)
vl <- data.frame(panel = factor(lab_tf[names(SREL)], levels = lab_tf), s = SREL)
g2 <- ggplot(f2, aes(s, rho_dcca, linetype = pair, shape = pair)) + geom_line(linewidth = .4) + geom_point(size = 1) +
  geom_vline(data = vl, aes(xintercept = s), linetype = "dotted") + scale_x_log10() +
  scale_linetype_discrete(labels = PAIR_LAB) + scale_shape_discrete(labels = PAIR_LAB) +
  facet_wrap(~panel, ncol = 2, scales = "free_x") + labs(x = "Timescale s (bars, log scale)", y = expression(rho[DCCA](s))) + theme_paper
ggsave(file.path(OUT, "figures", "fig2_dcca_curves.png"), g2, width = 6.5, height = 5, dpi = 600)
ggsave(file.path(OUT, "figures", "Fig2.eps"), g2, width = 6.5, height = 5, device = cairo_ps)
# Figure 3: MF-DCCA spectra and generalized exponents (daily), one shared legend
sp <- spec[spec$pair %in% PAIR_LEV, ]
f3 <- rbind(data.frame(pair = sp$pair, x = sp$alpha, y = sp$f_alpha, panel = "(a)~Singularity~spectrum~f(alpha)"),
            data.frame(pair = sp$pair, x = sp$q, y = sp$h, panel = "(b)~Generalized~exponent~h[xy](q)"))
f3$pair <- factor(f3$pair, levels = PAIR_LEV)
g3 <- ggplot(f3, aes(x, y, linetype = pair, shape = pair)) + geom_line(linewidth = .4) + geom_point(size = 1.2) +
  facet_wrap(~panel, ncol = 2, scales = "free", labeller = label_parsed) + scale_linetype_discrete(labels = PAIR_LAB) + scale_shape_discrete(labels = PAIR_LAB) +
  labs(x = expression(alpha~"(panel a)"~~"or"~~q~"(panel b)"), y = NULL) + theme_paper
ggsave(file.path(OUT, "figures", "fig3_mfdcca.png"), g3, width = 6.5, height = 3.4, dpi = 600)
ggsave(file.path(OUT, "figures", "Fig3.eps"), g3, width = 6.5, height = 3.4, device = cairo_ps)

saveRDS(res, file.path(OUT, "scalars.rds"))
sink(file.path(OUT, "scalars.txt")); str(res); sink()
say("DONE")
