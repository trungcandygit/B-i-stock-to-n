"""Round-2 manuscript: load every number from the R outputs (no hand-typed results)."""
import csv, os, re
OUT = os.environ.get('R2_OUT') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'outputs')
TF = ['1D', 'M30', 'H1', 'H4']
TFNAME = {'1D': 'Daily (1D)', 'M30': '30-minute (M30)', 'H1': '1-hour (H1)', 'H4': '4-hour (H4)'}


def rows(name):
    with open(os.path.join(OUT, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def f(x, d=3):
    """Fixed decimals with a typographic minus sign."""
    s = f'{float(x):,.{d}f}'
    return s.replace('-', '−')


def pct(x, d=1):
    return f(x, d)


def rng(vals, d=3, sep='–'):
    v = [float(x) for x in vals]
    return f'{f(min(v), d)}{sep}{f(max(v), d)}'


def ci(lo, hi, d=3):
    return f'[{f(lo, d)}, {f(hi, d)}]'


def nint(x):
    return f'{int(round(float(x))):,}'


# ---------------------------------------------------------------- tables
DESC = {(r['index'], r['freq']): r for r in rows('01_descriptive_stats.csv')}
AVG = {(r['panel'], r['timeframe']): r for r in rows('02_table2_average_dcca.csv')}
REL = {r['timeframe']: r for r in rows('03_reliability_smax.csv')}
OLS = {r['timeframe']: r for r in rows('04_proxy_regression.csv')}
PROXY = {r['timeframe']: r for r in rows('05_proxy_comparison.csv')}
CRISIS = rows('11_crisis_episode_diagnostics.csv')
R2 = {(r['timeframe'], r['pair'], r['stat']): r for r in rows('R2_bootstrap_dcca.csv')}
FR = {(r['panel'], r['pair']): r for r in rows('R3_forbes_rigobon_pearson_bootstrap.csv')}
RE = {(r['panel'], r['pair'], r['regime']): r for r in rows('R4_portfolio_error_pearson.csv')}
WS = rows('R5_table7_with_pearson_regimes.csv')
GARCH = {r['timeframe']: r for r in rows('R6_reliability_garch_t.csv')}
SURR = {(r['timeframe'], r['pair']): r for r in rows('R7_mfdcca_shuffle_surrogate.csv')}
MFW = {(r['timeframe'], r['pair']): r for r in rows('09_mfdcca_width.csv')}
DEC = {(r['timeframe'], r['stat']): r for r in rows('R8_overlap_decomposition.csv')}
DECS = rows('R8b_overlap_decomposition_by_scale.csv')
PEAR = {r['timeframe']: r for r in rows('R8d_overlap_decomposition_pearson.csv')}
MT = {(r['timeframe'], r['pair'], r['stat']): r for r in rows('R9_slope_tests_multiplicity.csv')}
Q = {r['timeframe']: r for r in rows('R10_effect_size_cohen_q.csv')}
TAIL = {(r['pair'], r['u']): r for r in rows('R11_lower_tail_dependence.csv')}
DMCA = {(r['timeframe'], r['pair']): r for r in rows('R12_dmca_robustness.csv')}
BLK = rows('R13_block_length_sensitivity.csv')


def scalars():
    """Parse the str() dump of the run_all.R scalar list."""
    txt = open(os.path.join(OUT, 'scalars.txt'), encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'\$ (\w+)\s*:\s*(?:Named )?(?:num|int) (?:\[[^\]]*\] )?([-\d.e ]+)', txt):
        out[m.group(1)] = [float(v) for v in m.group(2).split()]
    return out


SC = scalars()
_dc = rows('06_dcca_curves.csv')
DETREND = [sum(float(r['rho_dcca']) for r in _dc if r['timeframe'] == '1D' and r['pair'] == 'VN30-VNINDEX' and r['order'] == str(m) and r['reliable'] == 'TRUE')
           / sum(1 for r in _dc if r['timeframe'] == '1D' and r['pair'] == 'VN30-VNINDEX' and r['order'] == str(m) and r['reliable'] == 'TRUE') for m in (1, 2, 3)]
HQ = rows('08_mfdcca_hq.csv')
NESTED = ['VN30-VNINDEX', 'VN30-VN100', 'VN100-VNINDEX']
