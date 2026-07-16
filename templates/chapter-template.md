<!--
This is the shipped house style (dissolved-prose convention), not a
drafting scaffold. Every chapter must still substantively cover the same
11 elements it always did — completeness is mandatory, the reader-facing
presentation is free (blueprint.md's "Standard Chapter Template"
section). The 11 elements, for reference (§ numbers below are used only
by style-guide.md and internal notes to refer to an element by number —
they are never literal headers in a chapter's body):

  1. Opening question       6. Common misconceptions
  2. Real-world story        7. Practical implications
  3. Worked example          8. Key takeaway
  4. Core intuition          9. One-page summary
  5. Technical explanation  10. Further reading
                             11. The next obvious question

Below is the actual reader-facing shape every chapter follows.
-->

# [Chapter Title]

**Part:** [Part Name]

**Concept Level:** [Level X, per concept-graph.md]

**Prerequisites:** [prior chapters/concepts required]

**New concepts introduced:** [comma-separated list — must also be added to glossary.md / misconceptions.md / concept-graph.md]

---

*[§1 — the one question this chapter exists to answer, in plain language, no jargon. Unheaded and italicized: this is the chapter's literal opening line.]*

[§2/§3 — a concrete, non-technical real-world story that motivates the question, before any terminology appears, flowing directly into a second, fully-written-out worked example that reinforces the same core idea from a different angle. The worked example is never a recap of the story, and never a diagram (style-guide.md §1; blueprint.md's "No Diagrams" section) — walk through it step by step in prose, the way you'd explain it out loud to someone.

§4/§5 — core intuition (plain-language explanation, one new idea only, grounded in the story/example above) and technical explanation (precise, technically correct — rigor without implementation detail; no code, no math/formulas) continue as the same flow of prose, no headers between them.

§6 — where a common misconception belongs, weave it into the narrative at the point a reader is most likely to actually hold it: "you might expect X — that's not quite right, because Y," carrying its analogy along in the same passage, instead of setting it apart as its own labeled block. Still mirror each one as its own row in misconceptions.md, regardless of how it's woven into the prose.

§7 — practical implications (why this matters when the reader meets this concept in a product announcement, engineering blog, or conversation) likewise flow as prose, usually near the chapter's end, rather than a separately labeled section.]

**[§8 — one bolded, memorable sentence, standalone near the chapter's end — the single idea a reader should carry out of this chapter if they remember nothing else. Not a paragraph, not a diagram.]**

**In short:**

- [§9 — bullet recap, 5–8 bullets max]

**Go further:**

- [§10 — optional external references]

*[§11 — the question this chapter's answer naturally provokes. Unheaded and italicized: this is the chapter's literal closing line, and must express the same idea as the next chapter's opening question (§1).]*

---

**Glossary terms added this chapter:** [term1, term2, ...] → append to `/glossary.md`

**Misconceptions logged this chapter:** [...] → append to `/misconceptions.md`

**Concept-graph entries checked off:** [...] → update `/concept-graph.md`
