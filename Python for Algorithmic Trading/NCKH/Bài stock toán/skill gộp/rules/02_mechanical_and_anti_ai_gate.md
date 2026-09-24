# Mechanical & Anti-AI Slop Gate (The Greppable Audit)

> The exhaustive, non-negotiable gate for mechanically detectable writing defects. Combines Wikipedia's "Signs of AI Writing", Top-5 Journal Referee AI-Detection Standards, and Lab Mechanical Audits.
> **Every hit must be eliminated or explicitly justified. Never submit text without passing this gate.**

---

## 1. Part A: Strictly Banned AI Vocabulary

These words immediately trigger the referee's mental alarm that the text was LLM-generated or uncurated. Eliminate them on sight.

| Banned AI Marker | Recommended Human Academic Replacement | Rationale |
| :--- | :--- | :--- |
| `delve / delve into` | *examine, analyze, investigate, test, evaluate* | The #1 diagnostic sign of ChatGPT output. |
| `testament to` | *reflects, demonstrates, indicates, corroborates* | Hype clichéd phrase; empty editorializing. |
| `underscores / underpins` | *shows, highlights, confirms, supports* | Overused rhetorical filler. |
| `pivotal / crucial role` | *key, primary, essential, central* | Excessive superlative; ungrounded importance. |
| `beacon / tapestry / kaleidoscope` | *framework, model, pattern, structure* | Figurative fluff strictly prohibited in academic papers. |
| `paramount` | *important, critical, necessary* | Pseudo-intellectual decoration. |
| `multifaceted / multi-layered` | *complex, diverse, having N components* | Vague filler replacing specific empirical dimensions. |
| `nuanced / nuanced understanding`| *detailed, distinct, context-dependent* | Pretentious hedge. State the exact nuance instead. |
| `shed light on` | *explain, clarify, reveal, estimate* | Cliché metaphor. |
| `foster / vibrant` | *encourage, promote, generate, active* | Promotional PR tone, not scientific writing. |
| `realm / landscape / tapestry` | *field, market, setting, domain, literature* | Empty poetic imagery. |
| `navigate / navigate the complexities`| *address, solve, manage, handle* | Overly dramatic metaphor. |
| `interplay / seamless interplay` | *interaction, correlation, feedback, link* | Vague hand-waving instead of modeled mechanism. |
| `meticulous / relentlessly` | *careful, systematic, comprehensive* | Self-congratulatory praise; let the results speak. |
| `embark on / journey` | *begin, initiate, undertake, execute* | Inappropriate narrative dramatization. |
| `commendable / burgeoning` | *growing, expanding, emerging* | Evaluative editorializing. |
| `revolutionize / game-changer` | *improve, alter, modify, shift* | Unsubstantiated Silicon Valley marketing hype. |
| `quintessential / symbiotic` | *standard, characteristic, joint, coupled* | Strained academic jargon. |
| `bespoke / tailored` | *custom, specific, designed for* | Commercial software buzzword. |
| `leverage (as a verb)` | *use, exploit, apply, employ* | Jargon; use "use" or "exploit". |
| `utilize` | *use* | "Use" is shorter, cleaner, and more forceful. |
| `a myriad of` | *many, numerous, several* | Florid archaic filler. |

---

## 2. Part B: Strictly Banned Structural & Stylistic Patterns

### M1. Em-dashes (`---`, `—`, `–` used as punctuation) — STRICTLY BANNED
- **Rule**: Em-dashes are the single highest-correlation machine writing tell in scientific prose. Replace every single em-dash with a comma, colon, parentheses, or a new sentence.
- ✗ *Wrong*: `The estimated coefficient --- although statistically significant --- is economically small.`
- ✓ *Right*: `The estimated coefficient, although statistically significant, is economically small.`
- ✓ *Right*: `The estimated coefficient is economically small, despite being statistically significant.`
- *Exception*: Only allowed in verbatim quotations from external authors.

### M2. Rhetorical Negation / Antithesis — BANNED AS DECORATION
- **Rule**: Ban contrastive formulas like `X, not Y`, `not X but Y`, `X rather than Y`, `not only X but also Y`.
- **The Keep-vs-Cut Test**: If the sentence loses factual information when rewritten positively, keep it. If it is mere rhetorical ornamentation, cut it.
- ✗ *Wrong*: `Our contribution is empirical, not theoretical.`
- ✓ *Right*: `We focus on empirical identification.`
- ✗ *Wrong*: `This paper is not in competition with standard GARCH models, but rather extends them.`
- ✓ *Right*: `Our specification extends the standard GARCH model by incorporating regime shifts.`

### M3. Editorializing Closers & Promotional Sum-ups — BANNED
- **Rule**: Never end a paragraph with a generic cheerleader sentence telling the reader how important the finding is.
- ✗ *Banned*: *"This finding is a testament to the resilience of decentralized markets."*
- ✗ *Banned*: *"These insights are of paramount importance for policymakers and practitioners alike."*
- ✗ *Banned*: *"Ultimately, this paves the way for a deeper and more vibrant understanding of asset pricing."*
- ✓ *Rule*: State the empirical fact, quantify the confidence interval, and stop.

### M4. Throat-Clearing Sentence Openers — BANNED
Do not begin sentences with generic transitional crutches unless an explicit logical pivot is occurring:
- `Moreover,` / `Furthermore,` / `Additionally,`
- `Notably,` / `Importantly,` / `Crucially,`
- `Indeed,` / `In turn,` / `That said,`
- `It is worth noting that...` / `It should be noted that...`
- **Correction**: Start directly with the subject and verb:
  - ✗ *Wrong*: `Notably, we find that the coefficient on liquidity drops to zero.`
  - ✓ *Right*: `The coefficient on liquidity drops to zero.`

### M5. Vacuous Intensifiers & Fluff
Delete these uninformative adverbs and phrases:
`in effect`, `at its core`, `in essence`, `truly`, `genuinely`, `fundamentally` (when used as filler), `actually`, `in fact`, `precisely because`, `seamlessly`, `armed with`.

### M6. Uniform Cadence & Robotic Rule-of-Three
- **Robotic Cadence**: LLMs naturally generate sentences of identical length (consistently 20–25 words per sentence), creating a monotonous, numbing rhythm.
- **Enforce Human Cadence Variety**:
  - Mix short, declarative sentences (6–12 words) for core claims.
  - Follow with medium-length analytical explanations (16–26 words).
  - Use compound structured sentences (30+ words) for rigorous mathematical derivations or multi-step econometric procedures.
- **Rule-of-Three Ban**: Avoid parallel triplets of synonyms:
  - ✗ *Wrong*: `The proposed model ensures stability, reliability, and robustness.`
  - ✓ *Right*: `The model maintains convergence across all baseline configurations.`

### M7. Passive Voice Limit (< 15%)
Academic papers in economics and finance should be assertive and direct:
- ✗ *Wrong*: `In Table 3, the impact of monetary shocks is evaluated by us.`
- ✓ *Right*: `Table 3 reports estimates of the impact of monetary shocks.`
- Limit passive voice constructions strictly to under 15% of all verbs in the manuscript.

### M8. Nominalization Piles (Verb-Smothering)
Replace noun phrases built from smothered verbs with their active verbal roots:
- `conduct an evaluation of` → **evaluate**
- `perform an estimation of` → **estimate**
- `make an assumption that` → **assume that**
- `provide a demonstration of` → **demonstrate**
- `is indicative of the fact that` → **indicates that**

---

## 3. Part C: Greppable Audit Command Suite

Run this bash command against your LaTeX manuscript (`sections/` or `.tex` files) before any submission or milestone:

```bash
# 1. Check for banned em-dashes
grep -rnE "(---|—| – )" *.tex sections/*.tex

# 2. Check for banned AI buzzwords
grep -rinE "\b(delve|testament|underscores|underpins|pivotal|beacon|tapestry|paramount|multifaceted|nuanced|shed light on|foster|vibrant|realm|interplay|meticulous|relentless|burgeoning|revolutionize|game-changer|quintessential|symbiotic|bespoke|utilize)\b" *.tex sections/*.tex

# 3. Check for throat-clearing openers
grep -rnE "^(Moreover|Furthermore|Additionally|Notably|Importantly|Crucially|Indeed|It is worth noting that|It should be noted that)\b" *.tex sections/*.tex

# 4. Check for vacuous intensifiers
grep -rinE "\b(at its core|in essence|truly|genuinely|in effect|seamlessly|armed with)\b" *.tex sections/*.tex

# 5. Check for nominalization piles
grep -rinE "\b(conduct an (investigation|analysis|evaluation)|perform an estimation|is indicative of)\b" *.tex sections/*.tex
```
