# Changelog

## 2026-07-15

- Initial commit: project infrastructure (style guide, chapter template,
  glossary, misconception graph, concept dependency tracker, icon set) and
  the full Part I manuscript (chapters 1–5, "Information").
- Added root `README.md`, `LICENSE` (provisional, all-rights-reserved),
  `CONTRIBUTING.md`, `ROADMAP.md`, this changelog, GitHub issue templates,
  and a `references/` bibliography system.
- Amended `blueprint.md`: the Standard Chapter Template is now explicitly
  an editorial checklist rather than a mandatory set of reader-facing
  headings; Part V's table of contents was restructured around durable
  questions instead of named standards (Tool Calling and MCP merged into
  one chapter, "How Models Reach Into the World," with MCP taught inside it
  as the current connection standard). Total chapter count: 31 → 30.
- Chapter 1: softened claims about scale being "the" dominant driver of
  progress and added a note on the ongoing debate over measuring emergent
  abilities.
- Chapter 5: added an explicit distinction between a token's static,
  starting embedding (this chapter) and its contextual, attention-revised
  representation (Chapter 11), plus a new misconception entry, and reframed
  the country/capital geometry example as an illustrative pattern rather
  than a universal law.
- Added `concept-graph.yaml` as the machine-readable source of truth behind
  `concept-graph.md`.
- Added Part II manuscript (chapters 6–10, "Prediction"), with matching
  glossary/misconception/concept-graph/reference updates.
- Second review round: Chapter 8 now draws an explicit boundary between the
  generic layered network it describes and the transformer architecture
  Part III builds on top of it. Chapter 10 clarifies that the scaling-law
  "straight line" requires both axes scaled in equal ratios (not literal
  linear loss decay) and introduces "irreducible loss." Chapter 5 gained a
  "try it yourself" thought experiment (hot/cold/sandwich) reinforcing the
  similarity-vs-synonymy misconception. `style-guide.md`'s chapter-mechanics
  section was reworded to stop contradicting blueprint.md's amended
  template language. Added `testing/` — a ready-to-run reader-validation
  protocol and per-chapter question bank (comprehension, transfer,
  misconception resistance, retention), covering Milestone 3 of
  `ROADMAP.md`.
