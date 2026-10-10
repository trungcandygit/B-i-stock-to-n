#!/usr/bin/env Rscript
# Round-3d analyses (Iter 25): items left open by the editorial synthesis (06_editorial_synthesis.md).
# Run from project_R/ AFTER run_round3c.R:   Rscript run_round3d.R
#   R29 single-factor contagion test (Corsetti, Pericoli and Sbracia 2005 logic): change in the VN30 loading
#       and in the idiosyncratic variance of P_cap between calm and crisis regimes, three regime definitions  [RR-16b]
#   R30 decomposition of the scaling slope of the nested coefficient into its kappa and rho_AM channels      [RR-21]
#   R31 materiality of the portfolio-variance misstatement: sampling error of the regime variance and
#       relative errors with the static correlation re-estimated in each replicate (joint resampling)       [RR-17, RR-29a]
source("R/dcca.R")
set.seed(20261013)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 999
DATA <- "../project/data/vn_indices_merged_filled.csv"
W <- 1316288 / 1928303
CRISIS <- list(c("2018-01-01", "2018-12-31"), c("2020-01-01", "2020-06-30"), c("2022-04-01", "2022-11-30"))
CALM   <- list(c("2016-01-01", "2017-12-31"), c("2023-01-01", "2024-12-31"))
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)
ci <- function(x) quantile(x, c(.025, .975), na.rm = TRUE, names = FALSE)
raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
d <- raw[raw$timeframe == "1D", ]; d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
d1 <- data.frame(date = as.Date(d$dt[-1]))
for (c in c("VN30", "VN100", "VNINDEX")) d1[[c]] <- diff(log(d[[c]]))
d1$Pcap <- (d1$VN100 - W * d1$VN30) / (1 - W)
sb_index <- function(n, L) {
  idx <- integer(n); i <- 1
  while (i <= n) { start <- sample.int(n, 1); len <- rgeom(1, 1 / L) + 1
    take <- ((start - 1 + 0:(len - 1)) %% n) + 1; k <- min(len, n - i + 1)
    idx[i:(i + k - 1)] <- take[1:k]; i <- i + k }
  idx
}
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
roll_sd <- function(x, w) { mp <- max(5, w %/% 2)
  sapply(seq_along(x), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
rvI <- roll_sd(d1$VNINDEX, 20); qI <- quantile(rvI, c(.25, .75), na.rm = TRUE)
rv3 <- roll_sd(d1$VN30, 20);    q3 <- quantile(rv3, c(.25, .75), na.rm = TRUE)
REG <- list(A = list(low = in_periods(d1$date, CALM), high = in_periods(d1$date, CRISIS)),
            B = list(low = !is.na(rvI) & rvI < qI[1], high = !is.na(rvI) & rvI > qI[2]),
            C = list(low = !is.na(rv3) & rv3 < q3[1], high = !is.na(rv3) & rv3 > q3[2]))

# ---------------------------------------------------------------- R29 single-factor contagion test
# P_cap = a + beta VN30 + e. Under no contagion beta is constant across regimes; a rise in correlation can come
# from a rise in Var(VN30) alone. Contagion in the factor-model sense is a rise in beta.
fac <- function(sub) { f <- lm.fit(cbind(1, sub$VN30), sub$Pcap); c(beta = f$coefficients[[2]], ev = var(f$residuals)) }
r29 <- do.call(rbind, lapply(names(REG), function(pan) {
  lo <- d1[REG[[pan]]$low, ]; hi <- d1[REG[[pan]]$high, ]
  pl <- fac(lo); ph <- fac(hi)
  bs <- replicate(B, { a <- fac(lo[sb_index(nrow(lo), 20), ]); b <- fac(hi[sb_index(nrow(hi), 20), ])
    c(b[["beta"]] - a[["beta"]], log(b[["ev"]] / a[["ev"]])) })
  db <- ph[["beta"]] - pl[["beta"]]; dv <- log(ph[["ev"]] / pl[["ev"]])
  data.frame(panel = pan, n_low = nrow(lo), n_high = nrow(hi), beta_low = pl[["beta"]], beta_high = ph[["beta"]],
             d_beta = db, d_beta_ci_lo = ci(bs[1, ])[1], d_beta_ci_hi = ci(bs[1, ])[2], d_beta_se = sd(bs[1, ]),
             p_d_beta = 2 * pnorm(-abs(db / sd(bs[1, ]))),
             idio_var_ratio = exp(dv), idio_ratio_ci_lo = exp(ci(bs[2, ])[1]), idio_ratio_ci_hi = exp(ci(bs[2, ])[2]),
             p_idio = 2 * pnorm(-abs(dv / sd(bs[2, ]))))
}))
wcsv(r29, "R29_factor_model_contagion_test.csv")

# ---------------------------------------------------------------- R30 slope channels of the nested coefficient
# d rho_AB / d ln s = (d g / d rho_AM) * d rho_AM / d ln s + (d g / d kappa) * d kappa / d ln s,
# with d g / d rho_AM = kappa^2 (kappa + rho) / D^1.5 and d g / d kappa = -kappa (1 - rho^2) / D^1.5.
bys <- read.csv(file.path(OUT, "R8b_overlap_decomposition_by_scale.csv"))
r30 <- do.call(rbind, lapply(unique(bys$timeframe), function(tf) {
  x <- bys[bys$timeframe == tf & bys$reliable, ]; ls <- log(x$s)
  D <- 1 + x$kappa^2 + 2 * x$kappa * x$rho_econ
  g_r <- mean(x$kappa^2 * (x$kappa + x$rho_econ) / D^1.5); g_k <- mean(-x$kappa * (1 - x$rho_econ^2) / D^1.5)
  sl <- function(v) unname(coef(lm(v ~ ls))[2])
  s_r <- sl(x$rho_econ); s_k <- sl(x$kappa)
  data.frame(timeframe = tf, n_scales = nrow(x), slope_rho_nested_obs = sl(x$rho_nested), slope_rho_econ = s_r, slope_kappa = s_k,
             dg_drho = g_r, dg_dkappa = g_k, channel_rho = g_r * s_r, channel_kappa = g_k * s_k,
             slope_implied_linear = g_r * s_r + g_k * s_k, damping_factor = g_r)
}))
wcsv(r30, "R30_slope_channels.csv")

# ---------------------------------------------------------------- R31 materiality and joint resampling of the static correlation
PAIRS <- list(c("VN30", "VNINDEX"), c("VN30", "VN100"), c("VN100", "VNINDEX"), c("Pcap", "VN30"))
pv <- function(s1, s2, r) 0.25 * s1^2 + 0.25 * s2^2 + 0.5 * s1 * s2 * r
re_of <- function(x, lab, p) { rs <- cor(x[[p[1]]], x[[p[2]]]); sub <- x[lab, ]
  s1 <- sd(sub[[p[1]]]); s2 <- sd(sub[[p[2]]]); rr <- cor(sub[[p[1]]], sub[[p[2]]])
  c(re = 100 * (pv(s1, s2, rs) - pv(s1, s2, rr)) / pv(s1, s2, rr), pv = pv(s1, s2, rr)) }
r31 <- list()
for (pan in c("A", "B")) for (g in c("low", "high")) {
  lab <- REG[[pan]][[g]]; ok <- !is.na(lab)
  for (p in PAIRS) {
    pt <- re_of(d1, lab, p)
    bs <- replicate(B, { i <- sb_index(nrow(d1), 20); x <- d1[i, ]; li <- lab[i]; li[is.na(li)] <- FALSE; re_of(x, li, p) })
    sub <- d1[lab, ]
    bv <- replicate(B, { y <- sub[sb_index(nrow(sub), 20), ]; pv(sd(y[[p[1]]]), sd(y[[p[2]]]), cor(y[[p[1]]], y[[p[2]]])) })
    r31[[length(r31) + 1]] <- data.frame(panel = pan, regime = g, pair = paste(p, collapse = "-"), RE_pct = pt[["re"]],
      RE_joint_ci_lo = ci(bs[1, ])[1], RE_joint_ci_hi = ci(bs[1, ])[2],
      regime_var_rel_se_pct = 100 * sd(bv) / pt[["pv"]], RE_over_se = abs(pt[["re"]]) / (100 * sd(bv) / pt[["pv"]]))
  }
}
r31 <- do.call(rbind, r31)
wcsv(r31, "R31_materiality_joint_resampling.csv")


# ---------------------------------------------------------------- R32 intraday bar schedule (bar opening times, local time)  [RR-15c]
loc <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "Asia/Ho_Chi_Minh")
r32 <- do.call(rbind, lapply(c("M30", "H1", "H4"), function(tf) { m <- raw$timeframe == tf
  tb <- table(format(loc[m], "%H:%M"))
  data.frame(timeframe = tf, bar_open_times = paste(names(tb), collapse = " "), median_bars_per_day = median(table(as.Date(loc[m], tz = "Asia/Ho_Chi_Minh")))) }))
wcsv(r32, "R32_intraday_bar_schedule.csv")
# ---------------------------------------------------------------- R33 practitioner recipe: decomposition from index-level inputs only  [RR-30]
# inputs: w, sd(A), sd(B), cor(A, B) of daily returns (Pearson, full sample); no constituent data needed
sA <- sd(d1$VN30); sB <- sd(d1$VN100); rAB <- cor(d1$VN30, d1$VN100)
sM <- sqrt(sB^2 - 2 * W * rAB * sA * sB + W^2 * sA^2) / (1 - W)
k <- (1 - W) * sM / (W * sA)
rAM <- (rAB * sB - W * sA) / ((1 - W) * sM)
D <- 1 + k^2 + 2 * k * rAM
wcsv(data.frame(w = W, sd_VN30 = sA, sd_VN100 = sB, rho_AB = rAB, sd_M = sM, sd_Pcap_direct = sd(d1$Pcap), kappa = k,
                benchmark = 1 / sqrt(1 + k^2), lower_bound = sqrt(1 - k^2), rho_AM = rAM, rho_AM_direct = cor(d1$VN30, d1$Pcap),
                sensitivity = k^2 * (k + rAM) / D^1.5, inverse_sensitivity = D^1.5 / (k^2 * (k + rAM)),
                share_condition_kappa_max = sqrt(3), amplitude_ratio_max = sqrt(3) * W / (1 - W)), "R33_practitioner_recipe.csv")
cat("done\n")
