#!/usr/bin/env Rscript
# Round-2 revision analyses (desk-reject + external reviewer report, Iter 24).
# Run from project_R/ AFTER run_all.R and run_revision.R:   Rscript run_round2.R
#   R8  exact overlap decomposition of the nested DCCA coefficient (Proposition 1), with block bootstrap
#   R9  Holm and Benjamini-Hochberg adjustment of the scaling-slope tests (from R2)
#   R10 effect sizes (Cohen's q) for the nested-minus-purged gap
#   R11 lower-tail dependence coefficients (daily)
#   R12 DMCA coefficient as an alternative multiscale estimator
#   R13 sensitivity of the gap interval to the bootstrap block length
#   Fig2 with pointwise 95% bootstrap bands; Fig4 decomposition map
suppressPackageStartupMessages(library(ggplot2))
source("R/dcca.R")
set.seed(20261007)
OUT <- "outputs"; args <- commandArgs(TRUE); B <- if (length(args)) as.integer(args[1]) else 499
DATA <- "../project/data/vn_indices_merged_filled.csv"
TF <- c("1D", "M30", "H1", "H4")
W <- 1316288 / 1928303
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

# ---------------------------------------------------------------- multivariate DCCA on a common scale grid
SER <- c("VN30", "VN100", "VNINDEX", "Pcap")
dcca_multi <- function(d, s_values) {
  P <- lapply(SER, function(v) cumulative_profile(d[[v]])); names(P) <- SER
  out <- lapply(s_values, function(s) {
    Q <- detrend_basis(s, 1)
    Rb <- lapply(P, function(p) detrended_boxes(p, s, 1, Q))
    cv <- function(a, b) mean(rowSums(Rb[[a]] * Rb[[b]]) / s)
    F2 <- sapply(SER, function(a) cv(a, a))
    c(s = s, F_A = sqrt(F2[["VN30"]]), F_M = sqrt(F2[["Pcap"]]), F_B = sqrt(F2[["VN100"]]),
      r_AM = cv("VN30", "Pcap") / sqrt(F2[["VN30"]] * F2[["Pcap"]]),
      r_AB = cv("VN30", "VN100") / sqrt(F2[["VN30"]] * F2[["VN100"]]),
      r_AI = cv("VN30", "VNINDEX") / sqrt(F2[["VN30"]] * F2[["VNINDEX"]]),
      r_BI = cv("VN100", "VNINDEX") / sqrt(F2[["VN100"]] * F2[["VNINDEX"]]))
  })
  as.data.frame(do.call(rbind, out))
}
# Proposition 1: rho_AB(s) = (1 + kappa rho_AM) / sqrt(1 + kappa^2 + 2 kappa rho_AM), kappa = (1-w) F_M / (w F_A)
decomp <- function(cv) {
  k <- (1 - W) * cv$F_M / (W * cv$F_A); r <- cv$r_AM; D <- 1 + k^2 + 2 * k * r
  g <- (1 + k * r) / sqrt(D); floor0 <- 1 / sqrt(1 + k^2)
  data.frame(s = cv$s, kappa = k, rho_econ = r, rho_nested = cv$r_AB, rho_implied = g,
             identity_error = abs(g - cv$r_AB), floor = floor0, mech_share = floor0 / g,
             sensitivity = k^2 * (k + r) / D^1.5, floor_minus_econ = floor0 - r)
}
summ <- function(dd, srel) { m <- dd$s <= srel; colMeans(dd[m, c("kappa", "rho_econ", "rho_nested", "floor", "mech_share", "sensitivity", "floor_minus_econ")]) }

dec_rows <- list(); dec_curve <- list(); band_rows <- list(); boot_keep <- list()
for (tf in TF) {
  d <- R[[tf]]; n <- nrow(d); s_values <- scale_range(n, order = 1, n_scales = 30)
  cv <- dcca_multi(d, s_values); dd <- decomp(cv)
  dec_curve[[tf]] <- cbind(timeframe = tf, dd, reliable = dd$s <= SREL[tf])
  pt <- summ(dd, SREL[tf])
  say(tf, ": decomposition bootstrap (B=", B, ")")
  bs <- replicate(B, { cvb <- dcca_multi(d[sb_index(n, LBLOCK[tf]), ], s_values)
    c(summ(decomp(cvb), SREL[tf]), cvb$r_AI, cvb$r_AB, cvb$r_BI, cvb$r_AM) })
  ns <- length(s_values); k0 <- length(pt)
  for (j in seq_len(k0)) {
    x <- bs[j, ]; nm <- names(pt)[j]
    dec_rows[[length(dec_rows) + 1]] <- data.frame(timeframe = tf, stat = nm, estimate = pt[[j]],
      ci_lo = ci(x)[1], ci_hi = ci(x)[2], boot_se = sd(x),
      p_one_sided = switch(nm, mech_share = mean(x <= 0.5), floor_minus_econ = mean(x <= 0), NA_real_))
  }
  # pointwise bands for Fig. 2
  lab <- c("VN30-VNINDEX", "VN30-VN100", "VN100-VNINDEX", "Pcap-VN30")
  est <- list(cv$r_AI, cv$r_AB, cv$r_BI, cv$r_AM)
  for (p in 1:4) {
    rows <- k0 + (p - 1) * ns + seq_len(ns)
    band_rows[[length(band_rows) + 1]] <- data.frame(timeframe = tf, pair = lab[p], s = s_values, rho = est[[p]],
      lo = apply(bs[rows, , drop = FALSE], 1, function(z) ci(z)[1]),
      hi = apply(bs[rows, , drop = FALSE], 1, function(z) ci(z)[2]), reliable = s_values <= SREL[tf])
  }
  # Cohen's q (Fisher z) for the nested-minus-purged gap on reliable-range averages
  rel <- s_values <= SREL[tf]
  avg <- function(v) mean(v[rel])
  q_pt <- atanh(mean(c(avg(cv$r_AI), avg(cv$r_AB), avg(cv$r_BI)))) - atanh(avg(cv$r_AM))
  q_bs <- apply(bs, 2, function(z) { a <- function(p) mean(z[k0 + (p - 1) * ns + which(rel)]); atanh(mean(c(a(1), a(2), a(3)))) - atanh(a(4)) })
  boot_keep[[tf]] <- data.frame(timeframe = tf, cohen_q = q_pt, ci_lo = ci(q_bs)[1], ci_hi = ci(q_bs)[2])
}
wcsv(do.call(rbind, dec_rows), "R8_overlap_decomposition.csv")
wcsv(do.call(rbind, dec_curve), "R8b_overlap_decomposition_by_scale.csv")
bands <- do.call(rbind, band_rows); wcsv(bands, "R8c_dcca_bootstrap_bands.csv")
wcsv(do.call(rbind, boot_keep), "R10_effect_size_cohen_q.csv")

# Pearson special case (whole sample, no detrending), all frequencies
pear <- do.call(rbind, lapply(TF, function(tf) { d <- R[[tf]]
  k <- (1 - W) * sd(d$Pcap) / (W * sd(d$VN30)); r <- cor(d$VN30, d$Pcap); D <- 1 + k^2 + 2 * k * r
  data.frame(timeframe = tf, kappa = k, rho_econ = r, rho_nested = cor(d$VN30, d$VN100),
             rho_implied = (1 + k * r) / sqrt(D), floor = 1 / sqrt(1 + k^2), mech_share = (1 / sqrt(1 + k^2)) / ((1 + k * r) / sqrt(D)),
             sensitivity = k^2 * (k + r) / D^1.5) }))
wcsv(pear, "R8d_overlap_decomposition_pearson.csv")

# ---------------------------------------------------------------- R9 multiple-testing adjustment of slope tests
r2 <- read.csv(file.path(OUT, "R2_bootstrap_dcca.csv"))
sl <- r2[r2$stat %in% c("slope_full", "slope_rel"), ]
sl$p_holm <- NA_real_; sl$p_bh <- NA_real_
for (st in unique(sl$stat)) { m <- sl$stat == st
  sl$p_holm[m] <- p.adjust(sl$p_two_sided[m], "holm"); sl$p_bh[m] <- p.adjust(sl$p_two_sided[m], "BH") }
sl$family_size <- ave(sl$p_two_sided, sl$stat, FUN = length)
wcsv(sl[, c("timeframe", "pair", "stat", "estimate", "ci_lo", "ci_hi", "p_two_sided", "p_holm", "p_bh", "family_size")], "R9_slope_tests_multiplicity.csv")

# ---------------------------------------------------------------- R11 lower-tail dependence (daily)
d1 <- R[["1D"]]
tail_dep <- function(x, y, u) mean(x <= quantile(x, u) & y <= quantile(y, u)) / u
TP <- list(c("VN30", "VN100"), c("VN30", "VNINDEX"), c("VN100", "VNINDEX"), c("Pcap", "VN30"))
td <- do.call(rbind, lapply(TP, function(p) do.call(rbind, lapply(c(0.05, 0.10), function(u) {
  pt <- tail_dep(d1[[p[1]]], d1[[p[2]]], u)
  bs <- replicate(B, { i <- sb_index(nrow(d1), LBLOCK["1D"]); tail_dep(d1[[p[1]]][i], d1[[p[2]]][i], u) })
  data.frame(pair = paste(p, collapse = "-"), u = u, lambda_L = pt, ci_lo = ci(bs)[1], ci_hi = ci(bs)[2])
}))))
wcsv(td, "R11_lower_tail_dependence.csv")

# ---------------------------------------------------------------- R12 DMCA coefficient (centred moving average)
dmca_rho <- function(x, y, lam) {
  px <- cumulative_profile(x); py <- cumulative_profile(y); h <- rep(1 / lam, lam)
  ex <- px - stats::filter(px, h, sides = 2); ey <- py - stats::filter(py, h, sides = 2)
  ok <- !is.na(ex) & !is.na(ey); sum(ex[ok] * ey[ok]) / sqrt(sum(ex[ok]^2) * sum(ey[ok]^2))
}
DP <- list(c("VN30", "VNINDEX"), c("VN30", "VN100"), c("VN100", "VNINDEX"), c("Pcap", "VN30"))
dm <- do.call(rbind, lapply(TF, function(tf) { d <- R[[tf]]
  lams <- unique(scale_range(nrow(d), n_scales = 30)); lams <- lams[lams <= SREL[tf]]; lams <- unique(lams + (lams %% 2 == 0))
  do.call(rbind, lapply(DP, function(p) data.frame(timeframe = tf, pair = paste(p, collapse = "-"),
    rho_dmca_avg = mean(sapply(lams, function(l) dmca_rho(d[[p[1]]], d[[p[2]]], l))), n_windows = length(lams)))) }))
dm$gap_vs_nested_mean <- NA_real_
for (tf in TF) { m <- dm$timeframe == tf
  dm$gap_vs_nested_mean[m & dm$pair == "Pcap-VN30"] <- mean(dm$rho_dmca_avg[m & dm$pair != "Pcap-VN30"]) - dm$rho_dmca_avg[m & dm$pair == "Pcap-VN30"] }
wcsv(dm, "R12_dmca_robustness.csv")

# ---------------------------------------------------------------- R13 block-length sensitivity (daily gap)
avg_rel <- function(d, p, srel) { cv <- dcca_curve(d[[p[1]]], d[[p[2]]]); mean(cv$rho_dcca[cv$s <= srel]) }
gap_fun <- function(d) mean(sapply(DP[1:3], function(p) avg_rel(d, p, SREL["1D"]))) - avg_rel(d, DP[[4]], SREL["1D"])
g0 <- gap_fun(d1)
bl <- do.call(rbind, lapply(c(5, 10, 20, 40, 60), function(L) {
  bs <- replicate(B, gap_fun(d1[sb_index(nrow(d1), L), ]))
  data.frame(block_length_days = L, gap = g0, ci_lo = ci(bs)[1], ci_hi = ci(bs)[2]) }))
wcsv(bl, "R13_block_length_sensitivity.csv")

# ---------------------------------------------------------------- figures
th <- theme_bw(base_size = 9, base_family = "sans") +
  theme(panel.grid.minor = element_blank(), legend.position = "bottom", legend.title = element_blank(),
        strip.background = element_rect(fill = "grey95"))
lab_tf <- c("1D" = "(a) Daily (1D)", "M30" = "(b) 30-minute (M30)", "H1" = "(c) 1-hour (H1)", "H4" = "(d) 4-hour (H4)")
PAIR_LEV <- c("VN30-VN100", "VN30-VNINDEX", "VN100-VNINDEX", "Pcap-VN30")
PAIR_LAB <- list("VN30-VN100", "VN30-VNINDEX", "VN100-VNINDEX", expression(P[cap]*"-VN30"))
bands$pair <- factor(bands$pair, levels = PAIR_LEV)
bands$panel <- factor(lab_tf[bands$timeframe], levels = lab_tf)
vl <- data.frame(panel = factor(lab_tf[TF], levels = lab_tf), s = SREL[TF])
g2 <- ggplot(bands, aes(s, rho, linetype = pair, shape = pair)) +
  geom_ribbon(aes(ymin = lo, ymax = hi, group = pair), fill = "grey60", alpha = 0.30, colour = NA, show.legend = FALSE) +
  geom_line(linewidth = .4) + geom_point(size = 1) +
  geom_vline(data = vl, aes(xintercept = s), linetype = "dotted") + scale_x_log10() +
  scale_linetype_discrete(labels = PAIR_LAB) + scale_shape_discrete(labels = PAIR_LAB) +
  facet_wrap(~panel, ncol = 2, scales = "free_x") + labs(x = "Timescale s (bars, log scale)", y = expression(rho[DCCA](s))) + th
ggsave(file.path(OUT, "figures", "fig2_dcca_curves.png"), g2, width = 6.5, height = 5, dpi = 600, device = png, type = "cairo")
ggsave(file.path(OUT, "figures", "Fig2.eps"), g2, width = 6.5, height = 5, device = cairo_ps)

# Fig. 4: implied nested correlation as a function of the economic correlation (Proposition 1)
dec <- do.call(rbind, dec_rows)
kap <- setNames(dec$estimate[dec$stat == "kappa"], TF)
grid <- do.call(rbind, lapply(TF, function(tf) { r <- seq(-0.5, 1, by = 0.01); k <- kap[[tf]]
  data.frame(timeframe = tf, rho_econ = r, rho_nested = (1 + k * r) / sqrt(1 + k^2 + 2 * k * r)) }))
obs <- data.frame(timeframe = TF, rho_econ = dec$estimate[dec$stat == "rho_econ"], rho_nested = dec$estimate[dec$stat == "rho_nested"])
grid$timeframe <- factor(grid$timeframe, levels = TF); obs$timeframe <- factor(obs$timeframe, levels = TF)
fl <- data.frame(y = dec$estimate[dec$stat == "floor" & dec$timeframe == "1D"])
g4 <- ggplot(grid, aes(rho_econ, rho_nested, linetype = timeframe)) + geom_line() +
  geom_abline(slope = 1, intercept = 0, colour = "grey50", linetype = "dotted") +
  geom_hline(data = fl, aes(yintercept = y), colour = "grey40", linetype = "longdash", linewidth = .3) +
  geom_vline(xintercept = 0, colour = "grey40", linewidth = .3) +
  geom_point(data = obs, aes(shape = timeframe), size = 2) +
  coord_cartesian(xlim = c(-0.5, 1), ylim = c(-0.5, 1)) +
  labs(x = expression("Economic correlation " * rho[DCCA](P[cap] * "," ~ VN30)),
       y = expression("Nested correlation " * rho[DCCA](VN30 * "," ~ VN100)), linetype = NULL, shape = NULL) + th
ggsave(file.path(OUT, "figures", "fig4_overlap_decomposition.png"), g4, width = 5, height = 4, dpi = 600, device = png, type = "cairo")
ggsave(file.path(OUT, "figures", "Fig4.eps"), g4, width = 5, height = 4, device = cairo_ps)

writeLines(c(capture.output(sessionInfo()), "", paste("CPU:", system("lscpu | grep 'Model name' | sed 's/.*: *//'", intern = TRUE)),
             paste("Cores:", parallel::detectCores())), file.path(OUT, "R_session_info.txt"))
say("done")
