"""Round 4: second proofreading + stop-slop pass on residual findings (automated checks.py + manual read),
gated by academic-paper checks."""
import os
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/edit_common.py').read())
E('Firstly, we quantify', 'Firstly, we quantify', 'First, we quantify', 'enumerator consistency')
E('Secondly, we provide', 'Secondly, we provide', 'Second, we provide', 'enumerator consistency')
E('Thirdly, we quantify', 'Thirdly, we quantify', 'Third, we quantify', 'enumerator consistency')
E('Both profiles are subsequently', 'Both profiles are subsequently partitioned', 'Both profiles are then partitioned', 'SS adverb')
T('The analysis evaluates four trading frequencies', 'The analysis covers four trading frequencies: 30-minute (M30), 1-hour (H1), 4-hour (H4) and daily (1D). We synchronize the index series by exact inner joins on timestamps and compute log returns as below; no index price is filled or interpolated:', 'PR 5.1 we-voice; PR 5.2 present tense')
T('Regime dependence is evaluated under two', 'We evaluate regime dependence under two definitions based on the 20-day rolling standard deviation of VNINDEX returns (Fig. 1).', 'PR 5.1 we-voice')
E('To separate multiscale dynamics', 'commodity baskets, and cross-border assets', 'commodity baskets and cross-border assets', 'PR 5.4 serial-comma consistency (house style: none)')
E('Abstract:', 'Risk models that use these correlations conflate', 'Risk models built on index-level correlations therefore conflate', 'clarity: antecedent')
T('The empirical research design operates', 'We use two sample tiers.', 'SS inflated')
E('Within each segment, we fit', 'representing linear DCCA) and compute', 'representing linear DCCA) and compute', 'noop-check')
save(S + '/round4_edits.md')
