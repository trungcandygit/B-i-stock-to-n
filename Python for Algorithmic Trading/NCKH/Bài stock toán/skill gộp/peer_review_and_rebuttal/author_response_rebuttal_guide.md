# Author Response & Rebuttal Protocol (Responding to Reviewers)

> How to convert a "Revise & Resubmit" (R&R) into an unconditional Acceptance.
> Synthesizes top journal rebuttal practices, ChatResponse frameworks, and academic diplomacy.

---

## 1. The 4 Golden Rules of Author Responses

### Rule 1: Gratitude, Humility & Respect
- Never insult, patronize, or fight emotionally with a reviewer.
- Even when a reviewer completely misread a section or proposed an impossible test, begin with courtesy:
  - *"We thank the reviewer for this perceptive observation. We agree that our original exposition was insufficiently clear on this point, and we have rewritten Section 3.2 to make this explicit."*
- If the reviewer was confused, it is **your fault as the writer** for not being crystal clear.

### Rule 2: Complete & Point-by-Point Transparency
- Every single comment, bullet, or sub-question from every reviewer MUST receive an individual, explicit, numbered response.
- Never bundle three distinct critiques into a single vague hand-waving answer.

### Rule 3: Direct Answer First, Then Evidence
- Never bury the answer in a 3-page methodological preamble.
- Lead immediately with the bottom line:
  - *"We agree with the reviewer and have re-estimated all baseline models using wild cluster bootstrapped standard errors. As reported in the new Table 4 (reproduced below), all main coefficients remain statistically significant at the 1% level."*

### Rule 4: Show the Exact Textual Diff
- Always quote the exact new text added to the revised manuscript, complete with section and page numbers:
  - *"In response to this comment, we have added the following paragraph on page 14 of the revised manuscript:"*
  - Follow with an indented quote or LaTeX diff snippet.

---

## 2. Canonical Point-by-Point Response Matrix

Format each reviewer comment using this exact structural template:

```markdown
### Response to Reviewer #1, Comment 3:

> **Reviewer Comment**:
> *"The authors claim that the surge in cross-asset correlation is driven by institutional liquidity hoarding. However, this could simply reflect correlated macroeconomic news updates. The authors need to rule out this fundamental information channel."*

**Author Response**:
We thank the reviewer for raising this critical point regarding the distinction between fundamental information updates and non-fundamental liquidity contagion. We agree that ruling out synchronous cash-flow news is essential for establishing our mechanism.

To address this concern directly, we have conducted two new empirical tests:
1. **Controlling for Macroeconomic News Surprises**: We merged tick-level data from scheduled State Bank of Vietnam policy announcements and macroeconomic release dates. As reported in the newly added Column (4) of Table 5, controlling for unexpected interest rate and exchange rate shocks does not attenuate the estimated correlation surge ($\hat{\beta} = 0.212$, SE = 0.046 vs. baseline $0.218$).
2. **High vs. Low Institutional Ownership Sub-Samples**: If the effect were driven by common macroeconomic news, it should appear equally across all equities. However, when we partition the sample by institutional ownership share, the correlation surge is concentrated almost entirely in high-institutional-ownership pairs ($p < 0.001$), consistent with fire-sale and liquidity-hoarding models.

**Changes in the Revised Manuscript**:
We have expanded Section 4.3 ("Testing Alternative Mechanisms") on pages 18–19 and added the new Table 5 to report these results. Specifically, we have added the following text:

> *"To distinguish our liquidity-preservation mechanism from synchronous macroeconomic cash-flow updates, we examine whether scheduled monetary policy releases account for the correlation breakdown. As reported in Table 5, Column (4), controlling for macro surprise shocks leaves the estimated co-movement parameter virtually unchanged ($\hat{\beta} = 0.212$, SE = 0.046). Furthermore, the effect is disproportionately concentrated among equities with high institutional ownership (Column 5), corroborating the hypothesis that institutional rebalancing—rather than broad news sentiment—underpins the contagion."*
```

---

## 3. How to Handle Unfair or Impossible Reviewer Demands

When a reviewer asks for data that does not exist, or demands a methodological test that violates econometric principles:

1. **Acknowledge the intellectual merit of the idea**:
   - *"We appreciate the reviewer's insightful suggestion to explore tick-level OTC derivatives transactions..."*
2. **Explain the physical/institutional constraint neutrally without being defensive**:
   - *"Unfortunately, centralized reporting of OTC derivatives was not mandated by regulatory authorities during our 2018–2024 sample period, rendering complete transaction records publicly unavailable for empirical research."*
3. **Provide the closest feasible empirical proxy or simulation**:
   - *"To address the core spirit of the reviewer's comment within the bounds of available data, we instead exploit exchange-traded index futures data as a proxy for derivatives hedging pressure..."*
4. **Add the constraint to the limitations / future work section**:
   - *"We have added an explicit discussion of this data boundary in Section 6 (page 28) as an important priority for future research once regulatory disclosures expand."*
