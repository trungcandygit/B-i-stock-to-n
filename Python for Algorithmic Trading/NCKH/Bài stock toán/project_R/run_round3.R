#!/usr/bin/env Rscript
# Round-3 analyses responding to the Stage-3 five-seat review (Iter 24).
# Run from project_R/ AFTER run_all.R, run_revision.R and run_round2.R:   Rscript run_round3.R
#   R14 sensitivity of the decomposition (floor, share, sensitivity, rho_econ) to the weight w
#   R15 bootstrap of ordering-free (Shapley) attribution, like-for-like gap, true lower bound,
#       and scale-invariance tests of the floor and of kappa (slopes on ln s)
#   R16 true minimum of the nested coefficient over rho_econ in [-1, 1]
#   R17 floor contour over (w, amplitude ratio) -> Fig. 5
#   R18 out-of-sample evaluation of correlation inputs for portfolio variance (QLIKE, MSE, Diebold-Mariano)
#   R19 Forbes-Rigobon regime regressions (slope, residual variance)
#   R20 minimum-variance hedge effectiveness of VN30 for the mid-cap component
suppressPackageStartupMessages({ library(ggplot2); library(sandwich) })
source("R/dcca.R")
set.seed(20261010)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 499
DATA <- "../project/data/vn_indices_merged_filled.csv"
TF <- c("1D", "M30", "H1", "H4")
W <- 1316288 / 1928303
CRISIS <- list(c("2018-01-01", "2018-12-31"), c("2020-01-01", "2020-06-30"), c("2022-04-01", "2022-11-30"))
CALM   <- list(c("2016-01-01", "2017-12-31"), c("2023-01-01", "2024-12-31"))
say <- function(...) cat(format(Sys.time(), "[%H:%M:%S] "), ..., "\n", sep = "")
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)
ci <- function(x) quantile(x, c(.025, .975), na.rm = TRUE, names = FALSE)

raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
load_tf <- function(tf) {
  d <- raw[raw$timeframe == tf, ]; d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
  r <- data.frame(date = as.Date(d$dt[-1]))
  for (c in c("VN30", "VN100", "VNINDEX")) r[[c]] <- diff(log(d[[c]]))
  r$Pcap <- (r$VN100 - W * r$VN30) / (1 - W)
  r
}
R <- setNames(lapply(TF, load_tf), TF)
SREL <- setNames(read.csv(file.path(OUT, "03_reliability_smax.csv"))$s_rel, TF)
BPD <- sapply(R, function(d) median(table(d$date)))
LBLOCK <- setNames(pmax(10, round(20 * BPD)), TF)
sb_index <- function(n, L) {
  idx <- integer(n); i <- 1
  while (i <= n) { start <- sample.int(n, 1); len <- rgeom(1, 1 / L) + 1
    take <- ((start - 1 + 0:(len - 1)) %% n) + 1; k <- min(len, n - i + 1)
    idx[i:(i + k - 1)] <- take[1:k]; i <- i + k }
  idx
}

# A = VN30, M = mid-cap proxy with weight w; B = w A + (1 - w) M holds by construction
dcca_AM <- function(A, M, s_values) {
  PA <- cumulative_profile(A); PM <- cumulative_profile(M)
  out <- lapply(s_values, function(s) {
    Q <- detrend_basis(s, 1)
    ra <- detrended_boxes(PA, s, 1, Q); rm <- detrended_boxes(PM, s, 1, Q)
    faa <- mean(rowSums(ra * ra) / s); fmm <- mean(rowSums(rm * rm) / s); fam <- mean(rowSums(ra * rm) / s)
    c(s = s, F_A = sqrt(faa), F_M = sqrt(fmm), r_AM = fam / sqrt(faa * fmm))
  })
  as.data.frame(do.call(rbind, out))
}
decomp_w <- function(cv, w) {
  k <- (1 - w) * cv$F_M / (w * cv$F_A); r <- cv$r_AM; D <- 1 + k^2 + 2 * k * r
  g <- (1 + k * r) / sqrt(D); fl <- 1 / sqrt(1 + k^2)
  data.frame(s = cv$s, kappa = k, rho_econ = r, rho_nested = g, floor = fl, mech_share = fl / g,
             sensitivity = k^2 * (k + r) / D^1.5,
             shapley_overlap = 0.5 * (fl + g - r), shapley_econ = 0.5 * (r + g - fl),
             gap_like = g - r, true_min = ifelse(k < 1, sqrt(1 - k^2), NA_real_))
}
slope_ln <- function(y, s) unname(coef(lm(y ~ log(s)))[2])

# ---------------------------------------------------------------- R14 weight sensitivity
W_GRID <- c(0.60, 0.65, W, 0.72, 0.75)
r14 <- do.call(rbind, lapply(c("1D", "M30"), function(tf) { d <- R[[tf]]; s_values <- scale_range(nrow(d), order = 1, n_scales = 30)
  do.call(rbind, lapply(W_GRID, function(w) {
    M <- (d$VN100 - w * d$VN30) / (1 - w)
    dd <- decomp_w(dcca_AM(d$VN30, M, s_values), w); rel <- dd$s <= SREL[tf]
    kp <- (1 - w) * sd(M) / (w * sd(d$VN30)); rp <- cor(d$VN30, M); Dp <- 1 + kp^2 + 2 * kp * rp
    data.frame(timeframe = tf, w = w, kappa = mean(dd$kappa[rel]), rho_econ = mean(dd$rho_econ[rel]),
               floor = mean(dd$floor[rel]), mech_share = mean(dd$mech_share[rel]), sensitivity = mean(dd$sensitivity[rel]),
               shapley_overlap_share = mean(dd$shapley_overlap[rel] / dd$rho_nested[rel]),
               pearson_floor = 1 / sqrt(1 + kp^2), pearson_rho_econ = rp,
               pearson_share = (1 / sqrt(1 + kp^2)) / ((1 + kp * rp) / sqrt(Dp)))
  })) }))
wcsv(r14, "R14_weight_sensitivity_decomposition.csv")

# ---------------------------------------------------------------- R15 + R16 bootstrap of attribution and scale invariance
stats_of <- function(d, s_values, tf) {
  dd <- decomp_w(dcca_AM(d$VN30, d$Pcap, s_values), W); rel <- dd$s <= SREL[tf]
  c(floor = mean(dd$floor[rel]), rho_econ = mean(dd$rho_econ[rel]), rho_nested = mean(dd$rho_nested[rel]),
    shapley_overlap = mean(dd$shapley_overlap[rel]), shapley_econ = mean(dd$shapley_econ[rel]),
    shapley_overlap_share = mean(dd$shapley_overlap[rel] / dd$rho_nested[rel]),
    econ_share = mean(dd$rho_econ[rel] / dd$rho_nested[rel]),
    gap_like = mean(dd$gap_like[rel]), true_min = mean(dd$true_min[rel]),
    floor_slope = slope_ln(dd$floor[rel], dd$s[rel]), kappa_slope = slope_ln(dd$kappa[rel], dd$s[rel]),
    econ_slope = slope_ln(dd$rho_econ[rel], dd$s[rel]),
    floor_range = diff(range(dd$floor[rel])))
}
r15 <- list()
for (tf in TF) {
  d <- R[[tf]]; n <- nrow(d); s_values <- scale_range(n, order = 1, n_scales = 30)
  pt <- stats_of(d, s_values, tf)
  say(tf, ": attribution bootstrap (B=", B, ")")
  bs <- replicate(B, stats_of(d[sb_index(n, LBLOCK[tf]), ], s_values, tf))
  for (k in names(pt)) {
    x <- bs[k, ]; kk <- sum(x <= 0); ku <- sum(x >= 0)
    r15[[length(r15) + 1]] <- data.frame(timeframe = tf, stat = k, estimate = pt[[k]], ci_lo = ci(x)[1], ci_hi = ci(x)[2],
      boot_se = sd(x), p_two_sided_boot = min(1, 2 * (min(kk, ku) + 1) / (B + 1)))
  }
}
r15 <- do.call(rbind, r15)
sl <- r15$stat %in% c("floor_slope", "kappa_slope", "econ_slope")
r15$p_holm <- NA_real_
for (st in c("floor_slope", "kappa_slope", "econ_slope")) { m <- r15$stat == st; r15$p_holm[m] <- p.adjust(r15$p_two_sided_boot[m], "holm") }
wcsv(r15, "R15_attribution_and_scale_invariance.csv")

r16 <- do.call(rbind, lapply(TF, function(tf) { k <- r15$estimate[r15$timeframe == tf & r15$stat == "floor"]
  kap <- sqrt(1 / k^2 - 1)
  data.frame(timeframe = tf, kappa_from_floor = kap, floor = k, true_min = sqrt(1 - kap^2), argmin_rho_econ = -kap) }))
wcsv(r16, "R16_true_lower_bound.csv")

# ---------------------------------------------------------------- R17 floor contour (analytical) -> Fig. 5
d1 <- R[["1D"]]
ratio_hose <- sd(d1$Pcap) / sd(d1$VN30)
grid <- expand.grid(w = seq(0.30, 0.95, by = 0.005), ratio = seq(0.50, 2.00, by = 0.01))
grid$floor <- 1 / sqrt(1 + ((1 - grid$w) * grid$ratio / grid$w)^2)
wcsv(data.frame(w = W, amplitude_ratio_daily_sd = ratio_hose, floor = 1 / sqrt(1 + ((1 - W) * ratio_hose / W)^2)), "R17_floor_contour_hose_point.csv")
th <- theme_bw(base_size = 9, base_family = "sans") + theme(panel.grid.minor = element_blank())
g5 <- ggplot(grid, aes(w, ratio, z = floor)) +
  geom_contour(breaks = c(0.5, 0.6, 0.7, 0.8, 0.9, 0.95), colour = "black", linewidth = 0.35) +
  geom_text(data = data.frame(w = c(0.36, 0.47, 0.56, 0.68, 0.81, 0.89), ratio = 1.85,
                              lab = c("0.5", "0.6", "0.7", "0.8", "0.9", "0.95")),
            aes(w, ratio, label = lab), inherit.aes = FALSE, size = 2.6) +
  geom_point(data = data.frame(w = W, ratio = ratio_hose), aes(w, ratio), inherit.aes = FALSE, shape = 17, size = 2.4) +
  annotate("text", x = W + 0.012, y = ratio_hose - 0.07, label = "VN30 in VN100", hjust = 0, size = 2.6) +
  labs(x = "Weight of the child index in the parent, w", y = expression("Relative volatility of the remainder, " * sigma[M] / sigma[A])) + th
ggsave(file.path(OUT, "figures", "fig5_floor_contour.png"), g5, width = 5, height = 3.8, dpi = 600, device = png, type = "cairo")
ggsave(file.path(OUT, "figures", "Fig5.eps"), g5, width = 5, height = 3.8, device = cairo_ps)

# ---------------------------------------------------------------- R18 out-of-sample portfolio-variance evaluation (daily)
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
SPLIT <- as.Date("2023-01-01")
est <- d1$date < SPLIT; ev <- !est
ewma_cov <- function(x, y, lam = 0.94, init_n = 60) {   # one-step-ahead RiskMetrics forecasts
  n <- length(x); vx <- vy <- cxy <- numeric(n)
  vx[1] <- var(x[1:init_n]); vy[1] <- var(y[1:init_n]); cxy[1] <- cov(x[1:init_n], y[1:init_n])
  for (t in 2:n) { vx[t] <- lam * vx[t - 1] + (1 - lam) * x[t - 1]^2; vy[t] <- lam * vy[t - 1] + (1 - lam) * y[t - 1]^2
    cxy[t] <- lam * cxy[t - 1] + (1 - lam) * x[t - 1] * y[t - 1] }
  list(vx = vx, vy = vy, r = cxy / sqrt(vx * vy))
}
roll_sd_lag <- function(x, w = 20) { n <- length(x); out <- rep(NA_real_, n)
  for (t in (w + 1):n) out[t] <- sd(x[(t - w):(t - 1)]); out }        # uses information up to t - 1 only
OOS_PAIRS <- list(c("Pcap", "VN30"), c("VN30", "VN100"), c("VN30", "VNINDEX"), c("VN100", "VNINDEX"))
rv_lag <- roll_sd_lag(d1$VNINDEX)
qs <- quantile(rv_lag[est], c(.25, .75), na.rm = TRUE)                # thresholds fixed in the estimation window
reg_lab <- ifelse(rv_lag < qs[1], "low", ifelse(rv_lag > qs[2], "high", "mid"))
qlike <- function(h, r2) log(h) + r2 / h
dm_test <- function(l1, l2) { dd <- l1 - l2; f <- lm(dd ~ 1); se <- sqrt(NeweyWest(f, lag = 5, prewhite = FALSE)[1, 1])
  c(mean_diff = mean(dd), t = mean(dd) / se, p = 2 * pnorm(-abs(mean(dd) / se))) }
r18 <- list()
for (p in OOS_PAIRS) {
  x <- d1[[p[1]]]; y <- d1[[p[2]]]; e <- ewma_cov(x, y)
  rp <- 0.5 * x + 0.5 * y; r2 <- rp^2
  rho_static <- cor(x[est], y[est])
  rho_reg <- sapply(c("low", "mid", "high"), function(g) { m <- est & reg_lab == g & !is.na(reg_lab); cor(x[m], y[m]) })
  ok <- ev & !is.na(reg_lab)
  hv <- function(rho) 0.25 * e$vx + 0.25 * e$vy + 0.5 * sqrt(e$vx * e$vy) * rho
  H <- list(static = hv(rep(rho_static, nrow(d1))), ewma = hv(e$r),
            regime = hv(ifelse(is.na(reg_lab), NA, rho_reg[reg_lab])))
  L <- lapply(H, function(h) qlike(h[ok], r2[ok])); M <- lapply(H, function(h) (r2[ok] - h[ok])^2 * 1e8)
  for (m in names(H)) r18[[length(r18) + 1]] <- data.frame(pair = paste(p, collapse = "-"), method = m, n_eval = sum(ok),
      mean_qlike = mean(L[[m]]), mean_mse_x1e8 = mean(M[[m]]),
      bias_ratio = mean(r2[ok]) / mean(H[[m]][ok]))
  for (m in c("ewma", "regime")) { t1 <- dm_test(L$static, L[[m]]); t2 <- dm_test(M$static, M[[m]])
    r18[[length(r18) + 1]] <- data.frame(pair = paste(p, collapse = "-"), method = paste0("DM_static_vs_", m), n_eval = sum(ok),
      mean_qlike = t1[["mean_diff"]], mean_mse_x1e8 = t2[["mean_diff"]], bias_ratio = NA_real_,
      dm_t_qlike = t1[["t"]], dm_p_qlike = t1[["p"]], dm_t_mse = t2[["t"]], dm_p_mse = t2[["p"]]) }
}
r18 <- do.call(rbind, lapply(r18, function(z) { for (k in c("dm_t_qlike", "dm_p_qlike", "dm_t_mse", "dm_p_mse")) if (is.null(z[[k]])) z[[k]] <- NA_real_; z }))
wcsv(r18, "R18_out_of_sample_portfolio_variance.csv")
wcsv(data.frame(split_date = SPLIT, n_est = sum(est), n_eval = sum(ev), q25 = qs[1], q75 = qs[2],
                share_eval_low = mean(reg_lab[ev] == "low", na.rm = TRUE), share_eval_high = mean(reg_lab[ev] == "high", na.rm = TRUE)),
     "R18b_oos_design.csv")

# ---------------------------------------------------------------- R19 Forbes-Rigobon regime regressions
roll_sd <- function(x, w) { mp <- max(5, w %/% 2)
  sapply(seq_along(x), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
rv <- roll_sd(d1$VNINDEX, 20); q <- quantile(rv, c(.25, .75), na.rm = TRUE)
REG <- list(A = list(low = in_periods(d1$date, CALM), high = in_periods(d1$date, CRISIS)),
            B = list(low = !is.na(rv) & rv < q[1], high = !is.na(rv) & rv > q[2]))
r19 <- do.call(rbind, lapply(c("A", "B"), function(pan) do.call(rbind, lapply(c("low", "high"), function(g) {
  sub <- d1[REG[[pan]][[g]], ]; f <- lm(Pcap ~ VN30, data = sub)
  data.frame(panel = pan, regime = g, n = nrow(sub), beta = unname(coef(f)[2]), resid_var = var(residuals(f)),
             var_VN30 = var(sub$VN30), var_Pcap = var(sub$Pcap), signal_to_noise = unname(coef(f)[2])^2 * var(sub$VN30) / var(residuals(f)))
}))))
wcsv(r19, "R19_forbes_rigobon_regressions.csv")

# ---------------------------------------------------------------- R20 hedge effectiveness
he <- function(sub) cor(sub$Pcap, sub$VN30)^2
bs_full <- replicate(B, he(d1[sb_index(nrow(d1), 20), ]))
r20 <- rbind(data.frame(sample = "full", n = nrow(d1), hedge_effectiveness = he(d1), ci_lo = ci(bs_full)[1], ci_hi = ci(bs_full)[2]),
             do.call(rbind, lapply(c("A", "B"), function(pan) do.call(rbind, lapply(c("low", "high"), function(g) {
               sub <- d1[REG[[pan]][[g]], ]; bs <- replicate(B, he(sub[sb_index(nrow(sub), 20), ]))
               data.frame(sample = paste(pan, g, sep = "_"), n = nrow(sub), hedge_effectiveness = he(sub), ci_lo = ci(bs)[1], ci_hi = ci(bs)[2]) })))))
wcsv(r20, "R20_hedge_effectiveness.csv")
say("done")
