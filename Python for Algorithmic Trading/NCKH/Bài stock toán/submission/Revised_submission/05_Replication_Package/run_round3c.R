#!/usr/bin/env Rscript
# Round-3c analyses (Iter 24): Fig. 1 unshaded volatility spikes, lead-lag cross-autocorrelations between tiers.
# Run from project_R/ AFTER run_round3b.R:   Rscript run_round3c.R
#   R27 drawdown and volatility statistics of the 2021 and 2025 episodes that are not shaded in Fig. 1
#   R28 lead-lag cross-autocorrelations corr(A_{t-1}, M_t) and corr(M_{t-1}, A_t), with block bootstrap
source("R/dcca.R")
set.seed(20261012)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 999
DATA <- "data/vn_indices_merged_filled.csv"
W <- 1316288 / 1928303
wcsv <- function(d, f) write.csv(d, file.path(OUT, f), row.names = FALSE)
ci <- function(x) quantile(x, c(.025, .975), na.rm = TRUE, names = FALSE)
raw <- read.csv(DATA, stringsAsFactors = FALSE)
raw$dt <- as.POSIXct(raw$time, origin = "1970-01-01", tz = "UTC")
load_tf <- function(tf) {
  d <- raw[raw$timeframe == tf, ]; d <- d[order(d$dt), ]; d <- d[!duplicated(d$dt), ]
  r <- data.frame(date = as.Date(d$dt[-1]), same_day = as.Date(d$dt[-1]) == as.Date(d$dt[-nrow(d)]), VNINDEX_level = d$VNINDEX[-1])
  for (c in c("VN30", "VN100", "VNINDEX")) r[[c]] <- diff(log(d[[c]]))
  r$Pcap <- (r$VN100 - W * r$VN30) / (1 - W)
  r
}
d1 <- load_tf("1D")
sb_index <- function(n, L) {
  idx <- integer(n); i <- 1
  while (i <= n) { start <- sample.int(n, 1); len <- rgeom(1, 1 / L) + 1
    take <- ((start - 1 + 0:(len - 1)) %% n) + 1; k <- min(len, n - i + 1)
    idx[i:(i + k - 1)] <- take[1:k]; i <- i + k }
  idx
}

# ---------------------------------------------------------------- R27 unshaded episodes in Fig. 1
roll_sd <- function(x, w) { mp <- max(5, w %/% 2)
  sapply(seq_along(x), function(i) { lo <- max(1, i - w + 1); if (i - lo + 1 < mp) NA else sd(x[lo:i]) }) }
rv <- roll_sd(d1$VNINDEX, 20) * sqrt(252) * 100
q75 <- quantile(rv, .75, na.rm = TRUE)
episode <- function(a, b) { m <- d1$date >= as.Date(a) & d1$date <= as.Date(b); lv <- d1$VNINDEX_level[m]
  dd <- min(lv / cummax(lv) - 1) * 100
  data.frame(start = a, end = b, trading_days = sum(m), max_drawdown_pct = dd, share_top_quartile_vol = mean(rv[m] > q75, na.rm = TRUE),
             peak_vol_ann_pct = max(rv[m], na.rm = TRUE), date_of_peak_vol = as.character(d1$date[m][which.max(rv[m])])) }
wcsv(rbind(episode("2021-01-01", "2021-12-31"), episode("2025-03-01", "2025-06-30")), "R27_unshaded_episodes.csv")

# ---------------------------------------------------------------- R28 lead-lag between tiers
# lagged pairs are formed first (within the same trading day at intraday frequencies), then resampled in blocks
lag_pairs <- function(d, intraday) { n <- nrow(d); ok <- if (intraday) d$date[-1] == d$date[-n] & d$same_day[-1] else rep(TRUE, n - 1)
  data.frame(A_lag = d$VN30[-n][ok], M_now = d$Pcap[-1][ok], M_lag = d$Pcap[-n][ok], A_now = d$VN30[-1][ok]) }
leadlag <- function(p) c(lead_A_on_M = cor(p$A_lag, p$M_now), lead_M_on_A = cor(p$M_lag, p$A_now))
r28 <- list()
for (tf in c("1D", "M30", "H1")) {
  d <- if (tf == "1D") d1 else load_tf(tf)
  p <- lag_pairs(d, tf != "1D"); bpd <- median(table(d$date)); L <- max(10, round(20 * bpd))
  pt <- leadlag(p)
  bs <- replicate(B, leadlag(p[sb_index(nrow(p), L), ]))
  dif <- bs[1, ] - bs[2, ]
  r28[[tf]] <- data.frame(timeframe = tf, n_pairs = nrow(p), lead_VN30_on_Pcap = pt[[1]], ci_lo_1 = ci(bs[1, ])[1], ci_hi_1 = ci(bs[1, ])[2],
    lead_Pcap_on_VN30 = pt[[2]], ci_lo_2 = ci(bs[2, ])[1], ci_hi_2 = ci(bs[2, ])[2],
    asymmetry = pt[[1]] - pt[[2]], asym_ci_lo = ci(dif)[1], asym_ci_hi = ci(dif)[2])
}
wcsv(do.call(rbind, r28), "R28_lead_lag_tiers.csv")
cat("done\n")
