#!/usr/bin/env Rscript
# Round-3b analyses responding to the methodology seat (R1) of the Stage-3 review (Iter 24).
# Run from project_R/ AFTER run_round3.R:   Rscript run_round3b.R
#   R21 decomposition with the weight drawn inside each bootstrap replicate, w ~ U(0.60, 0.75)
#   R22 hypothesis-defined test family for H3 (broad-market pairs), studentized p-values, TOST for VN30-VN100
#   R23 intraday robustness: first bar of each day (overnight return + opening auction) removed
#   R24 block-length sensitivity of the gap at the 30-minute frequency
#   R25 Forbes-Rigobon with VN30-based volatility regimes and across the weight grid
#   R26 Gaussian-copula benchmark for the lower-tail dependence coefficients
source("R/dcca.R")
set.seed(20261011)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 499
DATA <- "data/vn_indices_merged_filled.csv"
TF <- c("1D", "M30", "H1", "H4")
W <- 1316288 / 1928303
CRISIS <- list(c("2018-01-01", "2018-12-31"), c("2020-01-01", "2020-06-30"), c("2022-04-01", "2022-11-30"))
CALM   <- list(c("2016-01-01", "2017-12-31"), c("2023-01-01", "2024-12-31"))
say <- function(...) cat(format(Sys.time(), "[%H:%M:%S] "), ..., "\n", sep = "")
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)
ci <- function(x, a = .05) quantile(x, c(a / 2, 1 - a / 2), na.rm = TRUE, names = FALSE)

raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
load_tf <- function(tf) {
  d <- raw[raw$timeframe == tf, ]; d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
  r <- data.frame(dt = d$dt[-1], date = as.Date(d$dt[-1]), prev_date = as.Date(d$dt[-nrow(d)]))
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
avg_rel <- function(x, y, s_values, srel) { cv <- dcca_curve(x, y, s_values = s_values); mean(cv$rho_dcca[cv$s <= srel]) }

# ---------------------------------------------------------------- R21 weight drawn inside each replicate
decomp_stats <- function(A, M, w, s_values, srel) {
  PA <- cumulative_profile(A); PM <- cumulative_profile(M); res <- NULL
  for (s in s_values[s_values <= srel]) {
    Q <- detrend_basis(s, 1); ra <- detrended_boxes(PA, s, 1, Q); rm <- detrended_boxes(PM, s, 1, Q)
    faa <- mean(rowSums(ra * ra) / s); fmm <- mean(rowSums(rm * rm) / s); fam <- mean(rowSums(ra * rm) / s)
    k <- (1 - w) * sqrt(fmm) / (w * sqrt(faa)); r <- fam / sqrt(faa * fmm); D <- 1 + k^2 + 2 * k * r
    g <- (1 + k * r) / sqrt(D); fl <- 1 / sqrt(1 + k^2)
    res <- rbind(res, c(floor = fl, rho_econ = r, mech_share = fl / g, sensitivity = k^2 * (k + r) / D^1.5,
                        shapley_overlap_share = 0.5 * (fl + g - r) / g))
  }
  colMeans(res)
}
r21 <- list()
for (tf in c("1D", "M30")) {
  d <- R[[tf]]; n <- nrow(d); s_values <- scale_range(n, order = 1, n_scales = 30)
  say(tf, ": weight-uncertainty bootstrap (B=", B, ")")
  bs <- replicate(B, { i <- sb_index(n, LBLOCK[tf]); w <- runif(1, 0.60, 0.75)
    A <- d$VN30[i]; M <- (d$VN100[i] - w * A) / (1 - w); decomp_stats(A, M, w, s_values, SREL[tf]) })
  pt <- decomp_stats(d$VN30, d$Pcap, W, s_values, SREL[tf])
  for (k in rownames(bs)) r21[[length(r21) + 1]] <- data.frame(timeframe = tf, stat = k, estimate_at_baseline_w = pt[[k]],
    ci_lo = ci(bs[k, ])[1], ci_hi = ci(bs[k, ])[2], boot_se = sd(bs[k, ]))
}
wcsv(do.call(rbind, r21), "R21_weight_uncertainty_bootstrap.csv")

# ---------------------------------------------------------------- R22 hypothesis-defined family, studentized p, TOST
r9 <- read.csv(file.path(OUT, "R9_slope_tests_multiplicity.csv"))
r2 <- read.csv(file.path(OUT, "R2_bootstrap_dcca.csv"))
rel <- merge(r9[r9$stat == "slope_rel", ], r2[r2$stat == "slope_rel", c("timeframe", "pair", "boot_se")], by = c("timeframe", "pair"))
rel$z <- rel$estimate / rel$boot_se; rel$p_studentized <- 2 * pnorm(-abs(rel$z))
fam <- rel$pair %in% c("VN30-VNINDEX", "VN100-VNINDEX")
rel$h3_family <- fam
rel$p_boot_holm_h3 <- NA_real_; rel$p_boot_bh_h3 <- NA_real_; rel$p_stud_holm_h3 <- NA_real_; rel$p_stud_bh_h3 <- NA_real_
rel$p_boot_holm_h3[fam] <- p.adjust(rel$p_boot[fam], "holm"); rel$p_boot_bh_h3[fam] <- p.adjust(rel$p_boot[fam], "BH")
rel$p_stud_holm_h3[fam] <- p.adjust(rel$p_studentized[fam], "holm"); rel$p_stud_bh_h3[fam] <- p.adjust(rel$p_studentized[fam], "BH")
rel$p_stud_holm_all <- p.adjust(rel$p_studentized, "holm"); rel$p_stud_bh_all <- p.adjust(rel$p_studentized, "BH")
# TOST for VN30-VN100: equivalence margin of 0.001 per unit of ln(s), i.e. a change of about 0.0045 in the
# coefficient over the reliable M30 range; 90% normal interval from the bootstrap standard error
MARGIN <- 0.001
rel$tost_lo90 <- rel$estimate - qnorm(.95) * rel$boot_se; rel$tost_hi90 <- rel$estimate + qnorm(.95) * rel$boot_se
rel$tost_equivalent <- rel$tost_lo90 > -MARGIN & rel$tost_hi90 < MARGIN
rel$tost_p <- pmax(pnorm((rel$estimate - MARGIN) / rel$boot_se), 1 - pnorm((rel$estimate + MARGIN) / rel$boot_se))
wcsv(rel[order(rel$timeframe, rel$pair), ], "R22_h3_family_studentized_tost.csv")

# ---------------------------------------------------------------- R23 drop the first bar of each day (intraday)
NESTED <- list(c("VN30", "VNINDEX"), c("VN30", "VN100"), c("VN100", "VNINDEX"))
r23 <- list()
for (tf in c("M30", "H1")) {
  d <- R[[tf]]; keep <- d$date == d$prev_date; dd <- d[keep, ]
  share_var <- 1 - var(d$VN30[keep]) * sum(keep) / (var(d$VN30) * nrow(d))
  s_values <- scale_range(nrow(dd), order = 1, n_scales = 30)
  nest <- mean(sapply(NESTED, function(p) avg_rel(dd[[p[1]]], dd[[p[2]]], s_values, SREL[tf])))
  pc <- avg_rel(dd$Pcap, dd$VN30, s_values, SREL[tf])
  say(tf, ": first-bar-removed gap bootstrap (B=199)")
  bs <- replicate(199, { i <- sb_index(nrow(dd), LBLOCK[tf]); x <- dd[i, ]
    mean(sapply(NESTED, function(p) avg_rel(x[[p[1]]], x[[p[2]]], s_values, SREL[tf]))) - avg_rel(x$Pcap, x$VN30, s_values, SREL[tf]) })
  sl <- sapply(c(NESTED, list(c("Pcap", "VN30"))), function(p) { cv <- dcca_curve(dd[[p[1]]], dd[[p[2]]], s_values = s_values); m <- cv$s <= SREL[tf]
    unname(coef(lm(cv$rho_dcca[m] ~ log(cv$s[m])))[2]) })
  r23[[tf]] <- data.frame(timeframe = tf, n_kept = nrow(dd), n_dropped = sum(!keep), share_of_bars_dropped = mean(!keep),
    share_of_VN30_sq_return_in_first_bar = sum(d$VN30[!keep]^2) / sum(d$VN30^2),
    nested_mean = nest, pcap_vn30 = pc, gap = nest - pc, gap_ci_lo = ci(bs)[1], gap_ci_hi = ci(bs)[2],
    slope_VN30_VNINDEX = sl[1], slope_VN30_VN100 = sl[2], slope_VN100_VNINDEX = sl[3], slope_Pcap_VN30 = sl[4])
}
wcsv(do.call(rbind, r23), "R23_intraday_first_bar_removed.csv")

# ---------------------------------------------------------------- R24 block-length sensitivity at M30
d <- R[["M30"]]; s_values <- scale_range(nrow(d), order = 1, n_scales = 30)
g0 <- mean(sapply(NESTED, function(p) avg_rel(d[[p[1]]], d[[p[2]]], s_values, SREL["M30"]))) - avg_rel(d$Pcap, d$VN30, s_values, SREL["M30"])
r24 <- do.call(rbind, lapply(c(5, 40), function(L) { say("M30 block length ", L, " days (B=199)")
  bs <- replicate(199, { i <- sb_index(nrow(d), L * BPD["M30"]); x <- d[i, ]
    mean(sapply(NESTED, function(p) avg_rel(x[[p[1]]], x[[p[2]]], s_values, SREL["M30"]))) - avg_rel(x$Pcap, x$VN30, s_values, SREL["M30"]) })
  data.frame(timeframe = "M30", block_length_days = L, block_length_bars = L * BPD["M30"], gap = g0, ci_lo = ci(bs)[1], ci_hi = ci(bs)[2]) }))
wcsv(r24, "R24_block_length_sensitivity_M30.csv")

# ---------------------------------------------------------------- R25 Forbes-Rigobon: VN30-based regimes and weight grid
d1 <- R[["1D"]]
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
roll_sd <- function(x, w) { mp <- max(5, w %/% 2)
  sapply(seq_along(x), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
rv30 <- roll_sd(d1$VN30, 20); q30 <- quantile(rv30, c(.25, .75), na.rm = TRUE)
REG30 <- list(low = !is.na(rv30) & rv30 < q30[1], high = !is.na(rv30) & rv30 > q30[2])
REGA <- list(low = in_periods(d1$date, CALM), high = in_periods(d1$date, CRISIS))
fr_point <- function(lo, hi) { rl <- cor(lo$M, lo$VN30); rh <- cor(hi$M, hi$VN30)
  dl <- var(hi$VN30) / var(lo$VN30) - 1; rs <- rh / sqrt(1 + dl * (1 - rh^2)); c(rho_low = rl, rho_high = rh, delta = dl, rho_star = rs, diff = rs - rl) }
r25 <- list()
for (w in c(0.60, 0.65, W, 0.72, 0.75)) for (def in c("chronological", "VN30_quartiles")) {
  x <- d1; x$M <- (x$VN100 - w * x$VN30) / (1 - w); RG <- if (def == "chronological") REGA else REG30
  lo <- x[RG$low, ]; hi <- x[RG$high, ]; pt <- fr_point(lo, hi)
  bs <- replicate(999, fr_point(lo[sb_index(nrow(lo), 20), ], hi[sb_index(nrow(hi), 20), ]))
  cen <- bs["diff", ] - mean(bs["diff", ])
  r25[[length(r25) + 1]] <- data.frame(w = w, regimes = def, n_low = nrow(lo), n_high = nrow(hi), t(pt),
    ci_lo = ci(bs["diff", ])[1], ci_hi = ci(bs["diff", ])[2], p_one_sided = mean(cen >= pt["diff"]))
}
wcsv(do.call(rbind, r25), "R25_forbes_rigobon_vn30_regimes_weight_grid.csv")

# ---------------------------------------------------------------- R26 Gaussian-copula benchmark for tail dependence
tail_dep <- function(x, y, u) mean(x <= quantile(x, u) & y <= quantile(y, u)) / u
TP <- list(c("VN30", "VN100"), c("VN30", "VNINDEX"), c("VN100", "VNINDEX"), c("Pcap", "VN30"))
nsim <- 1e6; z1 <- rnorm(nsim); z2 <- rnorm(nsim)
r26 <- do.call(rbind, lapply(TP, function(p) { rho <- cor(d1[[p[1]]], d1[[p[2]]]); y <- rho * z1 + sqrt(1 - rho^2) * z2
  do.call(rbind, lapply(c(0.05, 0.10), function(u) data.frame(pair = paste(p, collapse = "-"), u = u, pearson = rho,
    lambda_L_empirical = tail_dep(d1[[p[1]]], d1[[p[2]]], u), lambda_L_gaussian_copula = tail_dep(z1, y, u)))) }))
wcsv(r26, "R26_tail_dependence_gaussian_benchmark.csv")
say("done")
