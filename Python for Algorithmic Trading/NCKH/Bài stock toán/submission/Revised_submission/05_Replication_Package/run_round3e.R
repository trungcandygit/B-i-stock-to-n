#!/usr/bin/env Rscript
# Round-3e analyses (Iter 25, Stage 4'): items from the independent Stage 3' re-review (07_rereview_stage3prime.md).
# Run from project_R/ AFTER run_round3d.R:   Rscript run_round3e.R
#   R34 reliable-range slopes with bootstrap CIs and studentized p for full data, first bar removed, first and last bar
#       removed (M30, H1), and full data at 1D and H4; slope difference broad-market minus VN30-VN100 in the same replicates
#   R35 slope block-length sensitivity at M30 (5 and 40 trading days)
#   R36 like-for-like gap (VN30-VN100 minus P_cap-VN30) with the weight drawn inside each replicate, all frequencies
#   R37 Forbes-Rigobon and factor-loading tests with 2021 added to the chronological crisis episodes
source("R/dcca.R")
set.seed(20261014)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 199
DATA <- "data/vn_indices_merged_filled.csv"
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
  n <- nrow(d); dd <- as.Date(d$dt)
  r <- data.frame(date = dd[-1], first_bar = dd[-1] != dd[-n], last_bar = c(dd[-c(1, 2)] != dd[-c(1, n)], TRUE))
  for (c in c("VN30", "VN100", "VNINDEX")) r[[c]] <- diff(log(d[[c]]))
  r$Pcap <- (r$VN100 - W * r$VN30) / (1 - W)
  r
}
R <- setNames(lapply(TF, load_tf), TF)
SREL <- setNames(read.csv(file.path(OUT, "03_reliability_smax.csv"))$s_rel, TF)
BPD <- sapply(R, function(d) median(table(d$date)))
sb_index <- function(n, L) {
  idx <- integer(n); i <- 1
  while (i <= n) { start <- sample.int(n, 1); len <- rgeom(1, 1 / L) + 1
    take <- ((start - 1 + 0:(len - 1)) %% n) + 1; k <- min(len, n - i + 1)
    idx[i:(i + k - 1)] <- take[1:k]; i <- i + k }
  idx
}
PAIRS <- list(c("VN30", "VNINDEX"), c("VN100", "VNINDEX"), c("VN30", "VN100"), c("Pcap", "VN30"))
PN <- sapply(PAIRS, paste, collapse = "-")
slopes <- function(x, s_rel_values) sapply(PAIRS, function(p) {
  cv <- dcca_curve(x[[p[1]]], x[[p[2]]], s_values = s_rel_values); unname(coef(lm(cv$rho_dcca ~ log(cv$s)))[2]) })

# ---------------------------------------------------------------- R34 trimmed-bar slopes with inference, slope differences
r34 <- list()
VARIANTS <- list("1D" = "full", "M30" = c("full", "drop_first", "drop_first_last"), "H1" = c("full", "drop_first", "drop_first_last"), "H4" = "full")
for (tf in TF) for (v in VARIANTS[[tf]]) {
  d <- R[[tf]]
  keep <- switch(v, full = rep(TRUE, nrow(d)), drop_first = !d$first_bar, drop_first_last = !d$first_bar & !d$last_bar)
  x <- d[keep, ]; n <- nrow(x)
  sv <- scale_range(n, order = 1, n_scales = 30); sv <- sv[sv <= SREL[tf]]
  L <- max(10, round(20 * median(table(x$date))))
  say(tf, " ", v, ": slope bootstrap (B=", B, ", ", length(sv), " scales)")
  pt <- slopes(x, sv)
  bs <- replicate(B, slopes(x[sb_index(n, L), ], sv))
  dif_pt <- pt[1:2] - pt[3]; dif_bs <- bs[1:2, , drop = FALSE] - matrix(bs[3, ], 2, B, byrow = TRUE)
  for (j in 1:4) { se <- sd(bs[j, ])
    r34[[length(r34) + 1]] <- data.frame(timeframe = tf, variant = v, n = n, stat = "slope", pair = PN[j], estimate = pt[j],
      ci_lo = ci(bs[j, ])[1], ci_hi = ci(bs[j, ])[2], boot_se = se, p_studentized = 2 * pnorm(-abs(pt[j] / se))) }
  for (j in 1:2) { se <- sd(dif_bs[j, ])
    r34[[length(r34) + 1]] <- data.frame(timeframe = tf, variant = v, n = n, stat = "slope_minus_VN30-VN100", pair = PN[j], estimate = dif_pt[j],
      ci_lo = ci(dif_bs[j, ])[1], ci_hi = ci(dif_bs[j, ])[2], boot_se = se, p_studentized = 2 * pnorm(-abs(dif_pt[j] / se))) }
}
r34 <- do.call(rbind, r34)
wcsv(r34, "R34_trimmed_slopes_and_differences.csv")

# ---------------------------------------------------------------- R35 slope block-length sensitivity at M30
d <- R[["M30"]]; sv <- scale_range(nrow(d), order = 1, n_scales = 30); sv <- sv[sv <= SREL["M30"]]
pt <- slopes(d, sv)
r35 <- do.call(rbind, lapply(c(5, 40), function(Ld) { say("M30 slopes, block ", Ld, " days")
  bs <- replicate(B, slopes(d[sb_index(nrow(d), Ld * BPD["M30"]), ], sv))
  data.frame(timeframe = "M30", block_length_days = Ld, pair = PN, estimate = pt, ci_lo = apply(bs, 1, function(z) ci(z)[1]),
             ci_hi = apply(bs, 1, function(z) ci(z)[2]), boot_se = apply(bs, 1, sd), p_studentized = 2 * pnorm(-abs(pt / apply(bs, 1, sd)))) }))
wcsv(r35, "R35_slope_block_length_M30.csv")

# ---------------------------------------------------------------- R36 like-for-like gap under weight uncertainty
gap_like <- function(A, Bx, w, sv) { M <- (Bx - w * A) / (1 - w)
  mean(dcca_curve(A, Bx, s_values = sv)$rho_dcca) - mean(dcca_curve(A, M, s_values = sv)$rho_dcca) }
r36 <- do.call(rbind, lapply(TF, function(tf) { d <- R[[tf]]; n <- nrow(d)
  sv <- scale_range(n, order = 1, n_scales = 30); sv <- sv[sv <= SREL[tf]]; L <- max(10, round(20 * BPD[tf]))
  say(tf, ": like-for-like gap with weight uncertainty (B=", 2 * B + 1, ")")
  bs <- replicate(2 * B + 1, { i <- sb_index(n, L); gap_like(d$VN30[i], d$VN100[i], runif(1, 0.60, 0.75), sv) })
  data.frame(timeframe = tf, gap_at_factsheet_w = gap_like(d$VN30, d$VN100, W, sv), ci_lo = ci(bs)[1], ci_hi = ci(bs)[2],
             boot_se = sd(bs), share_above_0.05 = mean(bs > 0.05)) }))
wcsv(r36, "R36_like_for_like_gap_weight_uncertainty.csv")

# ---------------------------------------------------------------- R37 2021 counted as a crisis episode
d1 <- R[["1D"]]
in_periods <- function(dates, P) Reduce(`|`, lapply(P, function(p) dates >= as.Date(p[1]) & dates <= as.Date(p[2])))
fac <- function(sub) { f <- lm.fit(cbind(1, sub$VN30), sub$Pcap); c(beta = f$coefficients[[2]], ev = var(f$residuals)) }
fr_point <- function(lo, hi) { rl <- cor(lo$Pcap, lo$VN30); rh <- cor(hi$Pcap, hi$VN30)
  dl <- var(hi$VN30) / var(lo$VN30) - 1; rh / sqrt(1 + dl * (1 - rh^2)) - rl }
r37 <- do.call(rbind, lapply(list(base = CRISIS, with_2021 = c(CRISIS, list(c("2021-01-01", "2021-12-31")))), function(P) {
  lo <- d1[in_periods(d1$date, CALM), ]; hi <- d1[in_periods(d1$date, P), ]
  bs <- replicate(5 * B + 4, { a <- lo[sb_index(nrow(lo), 20), ]; b <- hi[sb_index(nrow(hi), 20), ]
    c(fr_point(a, b), fac(b)[["beta"]] - fac(a)[["beta"]]) })
  fd <- fr_point(lo, hi); db <- fac(hi)[["beta"]] - fac(lo)[["beta"]]
  data.frame(n_crisis = nrow(hi), fr_diff = fd, fr_ci_lo = ci(bs[1, ])[1], fr_ci_hi = ci(bs[1, ])[2],
             fr_p_one_sided = mean(bs[1, ] - mean(bs[1, ]) >= fd),   # re-centred convention, as in R3
             d_beta = db, d_beta_ci_lo = ci(bs[2, ])[1], d_beta_ci_hi = ci(bs[2, ])[2], p_d_beta = 2 * pnorm(-abs(db / sd(bs[2, ])))) }))
r37 <- cbind(episodes = c("2018, 2020, 2022", "2018, 2020, 2021, 2022"), r37)
wcsv(r37, "R37_crisis_definition_with_2021.csv")
cat("done\n")
