#!/usr/bin/env Rscript
# Round-1 review revision analyses (Revision Roadmap RR1-RR4, RR10-RR12).
# Run from project_R/ AFTER run_all.R:   Rscript run_revision.R
# Adds resampling inference that replaces HAC-over-scales and nominal-N standard errors.
suppressPackageStartupMessages(library(stats))
source("R/dcca.R")
set.seed(20260924)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 499
DATA <- "data/vn_indices_merged_filled.csv"
TF <- c("1D", "M30", "H1", "H4")
W_REAL <- 1316288 / 1928303
CRISIS <- list(c("2018-01-01", "2018-12-31"), c("2020-01-01", "2020-06-30"), c("2022-04-01", "2022-11-30"))
CALM   <- list(c("2016-01-01", "2017-12-31"), c("2023-01-01", "2024-12-31"))
say <- function(...) cat(format(Sys.time(), "[%H:%M:%S] "), ..., "\n", sep = "")
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)

raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
# RR12: the "filled" file forward-fills only USDVND; index columns are identical to the raw inner join
rawu <- read.csv("data/vn_indices_merged_raw.csv", stringsAsFactors = FALSE)
res_fill <- data.frame(same_rows = nrow(raw) == nrow(rawu),
                       index_cols_identical = isTRUE(all.equal(raw[, c("VN30", "VN100", "VNINDEX")], rawu[, c("VN30", "VN100", "VNINDEX")])),
                       usdvnd_na_in_raw = sum(is.na(rawu$USDVND)))
wcsv(res_fill, "R1_filled_file_check.csv")

load_tf <- function(tf) {
  d <- raw[raw$timeframe == tf, ]; d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
  r <- data.frame(date = as.Date(d$dt[-1]))
  for (c in c("VN30", "VN100", "VNINDEX")) r[[c]] <- diff(log(d[[c]]))
  r$Pcap <- (r$VN100 - W_REAL * r$VN30) / (1 - W_REAL)
  w_heur <- cor(r$VN30, r$VN100)
  r$Pheur <- (r$VN100 - w_heur * r$VN30) / (1 - w_heur)
  r$Pratio <- r$VN100 - r$VN30
  r$Pres <- unname(residuals(lm(r$VN100 ~ r$VN30)))
  r
}
R <- setNames(lapply(TF, load_tf), TF)
SREL <- setNames(read.csv(file.path(OUT, "03_reliability_smax.csv"))$s_rel, TF)
BPD <- sapply(R, function(d) median(table(d$date)))            # bars per trading day
LBLOCK <- setNames(pmax(10, round(20 * BPD)), TF)              # mean block length ~ 20 trading days

# stationary bootstrap (Politis-Romano) index generator
sb_index <- function(n, L) {
  idx <- integer(n); i <- 1
  while (i <= n) { start <- sample.int(n, 1); len <- rgeom(1, 1 / L) + 1
    take <- ((start - 1 + 0:(len - 1)) %% n) + 1; k <- min(len, n - i + 1)
    idx[i:(i + k - 1)] <- take[1:k]; i <- i + k }
  idx
}
curve_stats <- function(d, p, s_rel) {
  cv <- dcca_curve(d[[p[1]]], d[[p[2]]], order = 1, n_scales = 30)
  rel <- cv$s <= s_rel
  sl <- function(m) unname(coef(lm(cv$rho_dcca[m] ~ log(cv$s[m])))[2])
  c(avg_rel = mean(cv$rho_dcca[rel]), slope_full = sl(rep(TRUE, nrow(cv))), slope_rel = sl(rel))
}
ci <- function(x) quantile(x, c(.025, .975), na.rm = TRUE, names = FALSE)

# ---------------------------------------------------------------- RR1 + RR3: bootstrap DCCA averages, gap, slopes
PAIRS_MAIN <- list(c("VN30", "VNINDEX"), c("VN30", "VN100"), c("VN100", "VNINDEX"), c("Pcap", "VN30"))
PAIRS_ALT <- list(c("Pheur", "VN30"), c("Pratio", "VN30"), c("Pres", "VN30"))
pn <- function(p) paste(p, collapse = "-")
boot_rows <- list()
for (tf in TF) {
  d <- R[[tf]]; n <- nrow(d); pairs <- if (tf == "M30") c(PAIRS_MAIN, PAIRS_ALT) else PAIRS_MAIN
  point <- sapply(pairs, function(p) curve_stats(d, p, SREL[tf]))
  colnames(point) <- sapply(pairs, pn)
  say(tf, ": bootstrap (B=", B, ", mean block length ", LBLOCK[tf], " bars)")
  bs <- replicate(B, { db <- d[sb_index(n, LBLOCK[tf]), ]; sapply(pairs, function(p) curve_stats(db, p, SREL[tf])) })
  for (j in seq_along(pairs)) {
    for (k in rownames(point)) {
      x <- bs[k, j, ]
      boot_rows[[length(boot_rows) + 1]] <- data.frame(timeframe = tf, pair = pn(pairs[[j]]), stat = k, estimate = point[k, j],
        ci_lo = ci(x)[1], ci_hi = ci(x)[2], boot_se = sd(x), p_two_sided = 2 * min(mean(x <= 0), mean(x >= 0)))
    }
  }
  nested <- colMeans(bs["avg_rel", 1:3, , drop = FALSE]); gap <- nested - bs["avg_rel", 4, ]
  boot_rows[[length(boot_rows) + 1]] <- data.frame(timeframe = tf, pair = "nested_mean-minus-Pcap", stat = "gap",
    estimate = mean(point["avg_rel", 1:3]) - point["avg_rel", 4], ci_lo = ci(gap)[1], ci_hi = ci(gap)[2], boot_se = sd(gap),
    p_two_sided = 2 * min(mean(gap <= 0), mean(gap >= 0)))
}
bt <- do.call(rbind, boot_rows); wcsv(bt, "R2_bootstrap_dcca.csv")
print(bt[bt$pair %in% c("Pcap-VN30", "nested_mean-minus-Pcap"), ])

# ---------------------------------------------------------------- RR2: Pearson-consistent Forbes-Rigobon with bootstrap
d1 <- R[["1D"]]
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
roll_sd <- function(x, w) { mp <- max(5, w %/% 2)
  sapply(seq_along(x), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
rv <- roll_sd(d1$VNINDEX, 20); q <- quantile(rv, c(.25, .75), na.rm = TRUE)
REG <- list(A = list(low = in_periods(d1$date, CALM), high = in_periods(d1$date, CRISIS)),
            B = list(low = !is.na(rv) & rv < q[1], high = !is.na(rv) & rv > q[2]))
fr_point <- function(lo, hi, p) {
  rl <- cor(lo[[p[1]]], lo[[p[2]]]); rh <- cor(hi[[p[1]]], hi[[p[2]]])
  dl <- var(hi$VN30) / var(lo$VN30) - 1; rs <- rh / sqrt(1 + dl * (1 - rh^2))
  c(rho_low = rl, rho_high = rh, delta = dl, rho_star = rs, diff = rs - rl)
}
fr_rows <- list()
for (pan in c("A", "B")) for (p in PAIRS_MAIN) {
  lo <- d1[REG[[pan]]$low, ]; hi <- d1[REG[[pan]]$high, ]
  pt <- fr_point(lo, hi, p)
  bs <- replicate(1999, fr_point(lo[sb_index(nrow(lo), 20), ], hi[sb_index(nrow(hi), 20), ], p))
  se <- sd(bs["diff", ]); cen <- bs["diff", ] - mean(bs["diff", ])
  fr_rows[[length(fr_rows) + 1]] <- data.frame(panel = pan, pair = pn(p), n_low = nrow(lo), n_high = nrow(hi), t(pt),
    ci_lo = ci(bs["diff", ])[1], ci_hi = ci(bs["diff", ])[2], boot_se = se,
    p_one_sided = mean(cen >= pt["diff"]), power_at_0.05 = 1 - pnorm(qnorm(.95) - 0.05 / se))
}
fr <- do.call(rbind, fr_rows); wcsv(fr, "R3_forbes_rigobon_pearson_bootstrap.csv"); print(fr)

# ---------------------------------------------------------------- RR4: portfolio variance error, one estimator, regime sigmas
pv <- function(s1, s2, r) 0.25 * s1^2 + 0.25 * s2^2 + 0.5 * s1 * s2 * r
re_point <- function(sub, p, rs) { s1 <- sd(sub[[p[1]]]); s2 <- sd(sub[[p[2]]]); rr <- cor(sub[[p[1]]], sub[[p[2]]])
  100 * (pv(s1, s2, rs) - pv(s1, s2, rr)) / pv(s1, s2, rr) }
re_rows <- list()
for (pan in c("A", "B")) for (p in PAIRS_MAIN) {
  rs <- cor(d1[[p[1]]], d1[[p[2]]])
  for (g in c("low", "high")) { sub <- d1[REG[[pan]][[g]], ]
    pt <- re_point(sub, p, rs); bs <- replicate(1999, re_point(sub[sb_index(nrow(sub), 20), ], p, rs))
    re_rows[[length(re_rows) + 1]] <- data.frame(panel = pan, pair = pn(p), regime = g, rho_static = rs,
      rho_regime = cor(sub[[p[1]]], sub[[p[2]]]), RE_pct = pt, ci_lo = ci(bs)[1], ci_hi = ci(bs)[2]) }
}
re <- do.call(rbind, re_rows); wcsv(re, "R4_portfolio_error_pearson.csv"); print(re)

# ---------------------------------------------------------------- Table 7 regime columns, Pearson (consistent with RR2)
t7 <- read.csv(file.path(OUT, "07_table7_weight_sensitivity.csv"))
t7$rho_low_pearson <- sapply(t7$w, function(w) { x <- (d1$VN100 - w * d1$VN30) / (1 - w); cor(x[REG$A$low], d1$VN30[REG$A$low]) })
t7$rho_high_pearson <- sapply(t7$w, function(w) { x <- (d1$VN100 - w * d1$VN30) / (1 - w); cor(x[REG$A$high], d1$VN30[REG$A$high]) })
wcsv(t7, "R5_table7_with_pearson_regimes.csv")

# ---------------------------------------------------------------- RR10: reliability thresholds under heavy-tailed GARCH surrogates
garch_t_pair <- function(n, rho0, nu = 5, omega = 1e-6, a = 0.08, b = 0.90) {
  z1 <- rnorm(n); z2 <- rho0 * z1 + sqrt(1 - rho0^2) * rnorm(n)
  w <- sqrt(rchisq(n, nu) / (nu - 2)); u1 <- z1 / w; u2 <- z2 / w          # common-mixing multivariate t
  s2 <- numeric(n); s2[1] <- omega / (1 - a - b); e <- numeric(n)
  for (t in 1:n) { if (t > 1) s2[t] <- omega + a * e[t - 1]^2 + b * s2[t - 1]; e[t] <- sqrt(s2[t]) * u1[t] }
  list(x = e, y = sqrt(s2) * u2)
}
smax_garch <- function(n, reps = 50) {
  s <- scale_range(n, 1, 40); worst <- rep(0, length(s))
  for (rho0 in c(-0.3, 0, 0.3, 0.5, 0.7, 0.9)) {
    err <- rowMeans(sapply(1:reps, function(r) { g <- garch_t_pair(n, rho0); abs(dcca_curve(g$x, g$y, s_values = s)$rho_dcca - rho0) }))
    worst <- pmax(worst, err) }
  viol <- s[worst > 0.05]; if (!length(viol)) max(s) else max(c(min(s), s[s < min(viol)]))
}
say("GARCH-t reliability")
rel_g <- data.frame(timeframe = TF, n = sapply(R, nrow), s_rel_gaussian = SREL, s_rel_garch_t = sapply(R, function(d) smax_garch(nrow(d))))
# Table 2 averages recomputed over the more conservative of the two ranges
rel_g$pcap_avg_conservative <- sapply(TF, function(tf) { cv <- dcca_curve(R[[tf]]$Pcap, R[[tf]]$VN30)
  mean(cv$rho_dcca[cv$s <= min(rel_g$s_rel_gaussian[rel_g$timeframe == tf], rel_g$s_rel_garch_t[rel_g$timeframe == tf])]) })
rel_g$nested_avg_conservative <- sapply(TF, function(tf) { sr <- min(rel_g$s_rel_gaussian[rel_g$timeframe == tf], rel_g$s_rel_garch_t[rel_g$timeframe == tf])
  mean(sapply(PAIRS_MAIN[1:3], function(p) { cv <- dcca_curve(R[[tf]][[p[1]]], R[[tf]][[p[2]]]); mean(cv$rho_dcca[cv$s <= sr]) })) })
wcsv(rel_g, "R6_reliability_garch_t.csv"); print(rel_g)

# ---------------------------------------------------------------- RR11: shuffled surrogate for the generalized-exponent range
say("MF-DCCA surrogates")
dh <- function(x, y) { z <- mfdcca(x, y); z$lambda_xy[z$q == -5] - z$lambda_xy[z$q == 5] }
sur <- do.call(rbind, lapply(TF, function(tf) do.call(rbind, lapply(PAIRS_MAIN, function(p) {
  d <- R[[tf]]; obs <- dh(d[[p[1]]], d[[p[2]]])
  s <- replicate(100, { i <- sample.int(nrow(d)); dh(d[[p[1]]][i], d[[p[2]]][i]) })
  data.frame(timeframe = tf, pair = pn(p), dh_obs = obs, dh_shuffled_mean = mean(s), dh_shuffled_q95 = quantile(s, .95, names = FALSE),
             exceeds_q95 = obs > quantile(s, .95)) }))))
wcsv(sur, "R7_mfdcca_shuffle_surrogate.csv"); print(sur)
say("DONE")
