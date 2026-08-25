# Step A — Content Integrity Change List (APPLIED & VERIFIED)

Canonical master: `WeForgeWeb_Client_Growth_Kit_System.pdf` + `growth_kit.html`
Scope of Step A: verify rendered PDF vs HTML source, check numbering/sequencing/consistency/duplicated frameworks/unsupported claims/credibility risks, and list exactly what to correct / soften / remove / preserve. Step A changes have been applied to `generate_growth_kit_pdf.py`, rendered to `growth_kit.html`, and compiled into `WeForgeWeb_Client_Growth_Kit_System.pdf`.

---

## A. Verification Result (PDF vs HTML source)

- PDF = 7 pages. Footer correctly labels each page "Page X of 7" (no page-number errors).
- The PDF was rendered from `growth_kit.html`. Confirmed: every key marker (pillars, funnels, claims, North Star, 6 questions, 5-asset protocol, 70/20/10 rule, industry matrix, CTA) is present in the HTML, and page-by-page extracted PDF text matches the HTML body sections. Content is in sync; no silent drift.
- **FALSE POSITIVE — DO NOT "FIX":** Prior `visual-audit.md` flagged a CRITICAL misnumbering on page 4 (claims "1, 4, 2, 3, 5, 6"). Both the raw PDF text extraction and two independent visual reads show the six questions are correctly numbered **1–6 in order**. There is no numbering bug. Do not waste effort on a non-existent fix.

---

## B. Numbering & Sequencing — real issues

- B1: No actual numbering errors found anywhere in the PDF.
- B2 (sequencing, structural): Page 1 is overloaded — it functions as cover + executive summary + four-pillar list + 3-step cycle + scope bullets + differentiators + quote + CTA simultaneously. This is a content-sequencing problem, not a numbering bug. Resolution (move scope/differentiators off page 1) is a structural decision — flagged here, executed in Step B.

---

## C. Duplicated Frameworks (consolidation candidates)

- C1 — Four pillars listed TWICE:
  - Page 1: "ANG 4 NA PANGUNAHING HALIGI" → Foundation / Attention / Trust Hub / Flywheel
  - Page 2: "ANG APAT NA HALIGI NG ATING CONNECTED LEAD ENGINE" → Online Foundation / Targeted Reach / Decision Engine / Asset Flywheel
  - Same concept, slightly different labels. → Keep Page 1 as the canonical pillar list; Page 2 should REFERENCE it, not re-list it.
- C2 — Three funnel representations:
  - Page 1: "ANG 3-STEP REVENUE GENERATION CYCLE"
  - Page 2: "ANG PIPELINE ECONOMICS MATRIX (100 → 40 → 20 → 8-12)"
  - Page 6: "STAGE 1–5" funnel tracking
  - → Make Page 6's Stage 1–5 the canonical funnel. Page 1's cycle and Page 2's matrix become subordinate illustrations or are cut.
- C3 — "Connected system" definition on Page 1, then a 5-component re-statement on Page 2. → Page 2 should build on Page 1 with a bridge sentence ("as introduced on the cover…").
- C4 — Foundation premise on Page 1 (pillar 1) and again on Page 3 (Step 1 intro). → Trim Page 3's re-explanation; assume the reader already knows foundation matters.
- C5 — Boosting criteria on Page 5 overlap ad formats on Page 3 (before/after, location, CTA). → Add a one-line bridge on Page 5 so it reads as a selection filter on Page 3's formats, not repetition.
- C6 — Contact info repeated in every footer + Page 1 CTA + Page 7 CTA. → Decide now: Page 7 becomes the single dominant contact moment; footer repetition is reduced (visual execution in Step B, but the decision is made here).

---

## D. Unsupported / Risky Numeric & Outcome Claims

Disposition key: SOFTEN = rewrite to directional language (no invented proof). SOURCE = keep only if a real citation/source is supplied. CONFIRM = verify against actual delivery capability. CORRECT = rephrase for clarity (not a claim fix).

| # | Location | Current text | Disposition | Recommended wording |
|---|----------|--------------|-------------|---------------------|
| D1 | P1 REVENUE FOCUS | "Pinapataas ang closing rate ng 2x-3x." | SOFTEN | "Makabuluhang pagtaas sa closing rate ng estimates." |
| D2 | P1 FULL-FUNNEL STACK | "Google Maps Top 3 Ranking." | SOFTEN (never guarantee ranking) | "Google Maps local search visibility." |
| D3 | P2 DISCONNECTED TRAP | "70% ng nag-inquire ay nawawala dahil walang structured value nurturing." | SOFTEN or SOURCE | "Maraming inquiries ang nawawala…" (directional) — unless a real source is supplied. |
| D4 | P4 REVIEW FLYWHEEL | "15+ verified reviews ay nakakakuha ng hanggang 3x mas maraming tawag sa Google Maps." | SOFTEN or SOURCE | "Ang complete at active na profile ay nakakakuha ng mas maraming tawag." |
| D5 | P6 DATA-DRIVEN | "Google Search ay nagbibigay ng 75% closing rate sa high-ticket services…" | CORRECT (label as hypothetical) | "Halimbawa, kung mapansin nating ang Google Search ay nagbibigay ng mataas na closing rate…" — clearly an example, not a guarantee. |
| D6 | P1 01. TURNKEY | "Buong deployment sa loob ng 7-14 araw." | CONFIRM | Verify against real delivery; else soften to "mabilisang deployment." |

Items that are FINE and should stay (service standards/descriptions, not outcome claims):
- "Sub-3s Lead Capture Website" / "Load time below 3.0 seconds on 4G" (technical target — keep)
- "100% Ownership" (positioning — keep, verify accurate)
- "Weekly Metrics" / "Daily tracking" (service description — keep)
- "Hyper-Local FB Paid Ads" (service description — keep)

---

## E. Items to PRESERVE (locked — do not alter)

- Connected-system thesis (Page 1 one-sentence Tagalog definition).
- Bilingual Taglish voice throughout.
- Wrong-vs-right follow-up comparison + Template A/B/C (Page 6).
- The 6 website questions (Page 4) — content AND correct 1–6 numbering.
- 5-asset capture protocol (Page 5).
- 70/20/10 ad budget rule (Page 5).
- Stage 1–5 funnel (Page 6) — promote to canonical funnel.
- North Star: "Qualified Leads & Closed Projects" (Page 2).
- Clarity/Proof/Speed triad for closing rate (Page 2).
- Semantic color logic (red=risk, green=right, orange=warning, blue=trust) — visual, Step B.
- De-emphasized footer metadata — visual, Step B.

---

## F. PROPOSED CHANGE LIST (summary for approval)

CORRECT (wording / clarity):
- F1: P6 — rephrase the 75% figure as a clearly hypothetical example (D5).
- F2: P2 — add a bridge so the connected-system expansion builds on Page 1 instead of re-introducing (C3).
- F3: P5 — add a one-line bridge linking boosting criteria to Page 3 ad formats (C5).

SOFTEN (claims needing support):
- F4: P1 — 2x-3x closing rate → directional (D1).
- F5: P1 — Top 3 Ranking → local search visibility (D2).
- F6: P2 — 70% lost inquiries → directional unless sourced (D3).
- F7: P4 — 15+ reviews = 3x calls → directional unless sourced (D4).
- F8: P1 — 7-14 days → confirm or soften (D6).

REMOVE / CONSOLIDATE (content duplication):
- F9: P2 — remove duplicate four-pillar block; replace with reference to Page 1 (C1).
- F10: P1/P2 — reduce to ONE canonical funnel (Stage 1–5); treat 3-step cycle & pipeline matrix as subordinate or cut (C2).
- F11: P3 — trim foundation re-explanation intro (C4).
- F12: Footer/CTA — make Page 7 the singular CTA moment (decision now; visual reduction in Step B) (C6).

PRESERVE (do not touch):
- F13: all items in section E.

DO NOT "FIX" (false positive):
- Page 4 six-question numbering is correct (1–6). No change.

---

## Open decision needed from user (affects D3, D4, D6)

For D3 (70% lost inquiries), D4 (15+ reviews = 3x calls), and D6 (7-14 days): does a real, defensible source or actual delivery record exist?
- If YES → keep the claim and add a quiet source/citation note (do not invent one).
- If NO or unsure → soften per the recommended wording above.
