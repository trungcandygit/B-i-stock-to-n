# Core DCCA / MF-DCCA routines (R port of project/src/dcca_core.py and mfdcca.py).
# Conventions kept identical to the original Python pipeline:
#   * profile = cumsum(x - mean(x))
#   * 2 * floor(N/s) boxes (forward + backward partition)
#   * local polynomial detrending of order m on a box index rescaled to [-1, 1]
#   * rho_DCCA(s) = F2_DCCA(s) / (F_DFA,x(s) * F_DFA,y(s))

scale_range <- function(n, order = 1, n_scales = 30, s_min = NULL, s_max = NULL) {
  if (is.null(s_min)) s_min <- max(order + 2, 5)
  if (is.null(s_max)) s_max <- max(s_min + 1, n %/% 4)
  raw <- sort(unique(as.integer(round(10^seq(log10(s_min), log10(s_max), length.out = n_scales)))))
  raw[raw >= s_min & raw <= s_max]
}

cumulative_profile <- function(x) cumsum(x - mean(x))

split_boxes <- function(profile, s) {
  n <- length(profile); ns <- n %/% s
  if (ns < 1) return(matrix(numeric(0), 0, s))
  fwd <- matrix(profile[seq_len(ns * s)], nrow = ns, byrow = TRUE)
  bwd <- matrix(profile[(n - ns * s + 1):n], nrow = ns, byrow = TRUE)
  rbind(fwd, bwd)
}

detrend_basis <- function(s, order) {
  k <- 0:(s - 1)
  if (s > 1) k <- 2 * (k / (s - 1)) - 1
  A <- outer(k, 0:order, `^`)
  qr.Q(qr(A))
}

detrended_boxes <- function(profile, s, order, Q = NULL) {
  B <- split_boxes(profile, s)
  if (nrow(B) == 0) return(B)
  if (is.null(Q)) Q <- detrend_basis(s, order)
  B - (B %*% Q) %*% t(Q)
}

local_fluctuations <- function(px, py, s, order) {
  Q <- detrend_basis(s, order)
  rx <- detrended_boxes(px, s, order, Q)
  ry <- detrended_boxes(py, s, order, Q)
  list(fxy = rowSums(rx * ry) / s, fxx = rowSums(rx^2) / s, fyy = rowSums(ry^2) / s)
}

dcca_curve <- function(x, y, s_values = NULL, order = 1, n_scales = 30) {
  stopifnot(length(x) == length(y))
  n <- length(x)
  if (is.null(s_values)) s_values <- scale_range(n, order = order, n_scales = n_scales)
  px <- cumulative_profile(x); py <- cumulative_profile(y)
  out <- lapply(s_values, function(s) {
    lf <- local_fluctuations(px, py, s, order)
    Fxy2 <- mean(lf$fxy); Fxx <- sqrt(mean(lf$fxx)); Fyy <- sqrt(mean(lf$fyy))
    c(s = s, n_boxes = length(lf$fxy), F_xy2 = Fxy2, F_xx = Fxx, F_yy = Fyy,
      rho_dcca = if (Fxx > 0 && Fyy > 0) Fxy2 / (Fxx * Fyy) else NA_real_)
  })
  as.data.frame(do.call(rbind, out))
}

# ---------------------------------------------------------------- MF-DCCA
Q_DEFAULT <- c(-5:-1, 1:5)

q_average <- function(v, q, abs_signed = FALSE) {
  if (abs_signed) v <- abs(v)
  v <- v[v > 0]
  if (!length(v)) return(NA_real_)
  if (q == 0) return(exp((if (abs_signed) 0.25 else 0.5) * mean(log(v))))
  mean(v^(q / 2))^(1 / q)
}

mfdcca <- function(x, y, s_values = NULL, q_values = Q_DEFAULT, order = 1, n_scales = 24) {
  n <- length(x)
  if (is.null(s_values)) s_values <- scale_range(n, order = order, n_scales = n_scales)
  px <- cumulative_profile(x); py <- cumulative_profile(y)
  Fxy <- Fxx <- Fyy <- matrix(NA_real_, length(s_values), length(q_values))
  for (i in seq_along(s_values)) {
    lf <- local_fluctuations(px, py, s_values[i], order)
    for (j in seq_along(q_values)) {
      Fxy[i, j] <- q_average(lf$fxy, q_values[j], abs_signed = TRUE)
      Fxx[i, j] <- q_average(lf$fxx, q_values[j])
      Fyy[i, j] <- q_average(lf$fyy, q_values[j])
    }
  }
  slope_of <- function(F) apply(F, 2, function(col) {
    m <- is.finite(col) & col > 0
    if (sum(m) < 3) NA_real_ else unname(coef(lm(log(col[m]) ~ log(s_values[m])))[2])
  })
  data.frame(q = q_values, lambda_xy = slope_of(Fxy), h_x = slope_of(Fxx), h_y = slope_of(Fyy))
}

# numpy.gradient equivalent (second-order interior, first-order edges, non-uniform grid)
np_gradient <- function(f, x) {
  n <- length(f); g <- numeric(n)
  g[1] <- (f[2] - f[1]) / (x[2] - x[1])
  g[n] <- (f[n] - f[n - 1]) / (x[n] - x[n - 1])
  for (i in 2:(n - 1)) {
    hs <- x[i] - x[i - 1]; hd <- x[i + 1] - x[i]
    g[i] <- (hs^2 * f[i + 1] + (hd^2 - hs^2) * f[i] - hd^2 * f[i - 1]) / (hs * hd * (hd + hs))
  }
  g
}

multifractal_spectrum <- function(q, h) {
  tau <- q * h - 1
  alpha <- np_gradient(tau, q)
  data.frame(q = q, h = h, tau = tau, alpha = alpha, f_alpha = q * alpha - tau)
}

# ---------------------------------------------------------------- reliability (white-noise MC)
white_noise_error_curve <- function(rho0, n, order = 1, n_scales = 40, seed = 1) {
  set.seed(seed)
  z1 <- rnorm(n); z2 <- rnorm(n)
  x <- z1; y <- rho0 * z1 + sqrt(1 - rho0^2) * z2
  cv <- dcca_curve(x, y, order = order, n_scales = n_scales)
  data.frame(s = cv$s, abs_error = abs(cv$rho_dcca - rho0))
}

reliable_smax <- function(n, threshold = 0.05, order = 1, n_scales = 40,
                          rho0_values = c(-0.3, 0, 0.3, 0.5, 0.7, 0.9), n_repeats = 8, seed = 42) {
  curves <- list()
  for (i in seq_along(rho0_values)) {
    reps <- sapply(seq_len(n_repeats), function(r)
      white_noise_error_curve(rho0_values[i], n, order, n_scales, seed + 1000 * (i - 1) + (r - 1))$abs_error)
    curves[[i]] <- rowMeans(reps)
  }
  s <- scale_range(n, order = order, n_scales = n_scales)
  worst <- do.call(pmax, curves)
  viol <- s[worst > threshold]
  s_max <- if (!length(viol)) max(s) else { below <- s[s < min(viol)]; if (length(below)) max(below) else min(s) }
  list(s_max = s_max, first_violation = if (length(viol)) min(viol) else NA,
       curve = data.frame(s = s, worst_case_abs_error = worst),
       n_sims = length(rho0_values) * n_repeats)
}

# ---------------------------------------------------------------- scaling regression with Newey-West HAC
scale_regression <- function(s, rho, lag = 3) {
  ok <- is.finite(s) & is.finite(rho) & s > 0
  d <- data.frame(rho = rho[ok], ls = log(s[ok]))
  fit <- lm(rho ~ ls, data = d)
  V <- sandwich::NeweyWest(fit, lag = lag, prewhite = FALSE, adjust = FALSE)
  se <- sqrt(diag(V)); b <- coef(fit)
  tval <- b / se; df <- nrow(d) - 2
  data.frame(intercept = b[1], slope = b[2], hac_se_intercept = se[1], hac_se_slope = se[2],
             t_slope = tval[2], p_slope = 2 * pt(-abs(tval[2]), df),
             p_intercept = 2 * pt(-abs(tval[1]), df),
             r_squared = summary(fit)$r.squared, n = nrow(d), row.names = NULL)
}
