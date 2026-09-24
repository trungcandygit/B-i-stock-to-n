# Iterative Loop Mode Protocol (Autonomous Section Convergence)

> An iterative workflow protocol for drafting, refining, and polishing manuscript sections until they pass all mechanical, semantic, and econometric gates.

---

## 1. The 4-Phase Iterative Convergence Loop

```
[Phase 1: Draft / Ingestion]
           │
           ▼
[Phase 2: Mechanical Gate Pass] ──(Fails)──► [Fix Regex / Banned Markers]
           │ (Passes)
           ▼
[Phase 3: Semantic & Logic Pass] ──(Fails)──► [Restructure Narrative / Ground Claims]
           │ (Passes)
           ▼
[Phase 4: Red-Team Stress Test] ──(Fails)──► [Strengthen Identification / Bounds]
           │ (Passes)
           ▼
      [CONVERGED]
```

---

## 2. Phase Execution Details

### Phase 1: Draft / Ingestion
- Ingest raw empirical findings, estimation logs, and rough author notes.
- Establish the section's controlling claim using the **What → Why → So-What** heading convention.
- Expand fully to capture all necessary econometric details, parameter definitions, and intuition.

### Phase 2: Mechanical & Anti-AI Gate
- Execute the mechanical audit:
  1. Grep for em-dashes (`---`, `—`, `–`).
  2. Grep for banned AI vocabulary (`delve`, `testament`, `underscores`, etc.).
  3. Grep for throat-clearing sentence openers.
  4. Compute passive voice ratio (< 15%).
- **Rule**: Every single hit must be rewritten before moving to Phase 3.

### Phase 3: Semantic & Econometric Gate
- Verify Definition-Before-Use: Ensure all variables and constructs are defined prior to their argumentative use.
- Verify Grounding: Confirm that every coefficient, standard error, and claim is grounded in an actual table or citation.
- Ensure sentence cadence variety: Mix short punchy declarative sentences with compound analytical proofs.
- Verify table and math notation: `booktabs` formatting, displayed equation punctuation, operator typesetting.

### Phase 4: Red-Team Adversarial Stress Test
- Adopt the fresh-referee persona.
- Challenge the primary empirical assertion of the section:
  - Can an unobserved factor explain the result?
  - Is the economic magnitude meaningful?
  - Is the mechanism convincingly isolated from competing channels?
- If vulnerabilities are found, insert preemptive counter-arguments or additional sensitivity estimates.

### Convergence Criteria
A section is declared **CONVERGED** and ready for publication assembly when:
1. Mechanical Gate grep score is exactly **0 violations**.
2. Passive voice is strictly below **15%**.
3. All 120 checklist items applicable to the section are marked verified.
4. No ungrounded empirical assertions remain.
