# Reader-Testing Protocol

This is the structured version of `ROADMAP.md`'s Milestone 3 ("external
reader test: 5+ target readers"). It exists so that running the test is a
matter of following a script, not designing one from scratch under time
pressure with an actual reader sitting across from you.

**This protocol does not require a build step or code to run.** It's a
methodology document plus a question bank (`questions.md`). What it does
require is you, actually recruiting 5+ non-technical target readers (see
`blueprint.md`'s "Audience" section) and sitting through the sessions —
that part can't be delegated.

## Who to recruit

5+ readers matching `blueprint.md`'s stated audience: managers,
consultants, product leaders, founders, sales professionals, executives,
students, lifelong learners. Deliberately exclude people with an ML/CS
background for this round — the book's entire promise is legibility
*without* that background, so testing on readers who already have it will
under-detect real confusion.

## What to measure, per chapter, per reader

Five dimensions, scored 0–2 unless noted (0 = no, 1 = partial, 2 = yes):

1. **Comprehension** — can they explain the chapter's core concept in
   their own words, unaided, right after reading?
2. **Transfer** — can they apply the concept to a *new* example you give
   them, not one from the chapter?
3. **Misconception resistance** — when you ask the chapter's own logged
   misconception as a leading question (see `misconceptions.md`), do they
   correctly reject it, or do they fall back into it?
4. **Retention** — ask the comprehension question again, unprompted, one
   week later, with no re-reading in between.
5. **Reading experience** — not scored; a free-text note on *where*
   attention visibly dropped (a specific paragraph, a diagram that didn't
   parse, a term used before its explanation landed).

`questions.md` has the exact comprehension/transfer/misconception prompts
for all 10 written chapters (1–10), pulled directly from each chapter's own
logged misconceptions so this protocol stays in sync with the manuscript
rather than drifting into a separate, parallel set of questions.

## How to run a session

1. Reader reads one chapter, at their own pace, with no help from you.
2. Immediately after: ask the comprehension question. Don't hint. Score it.
3. Ask the transfer question. Score it.
4. Ask the misconception-resistance question(s) as neutral, leading
   questions — don't tip off that you're testing for a specific wrong
   answer. Score it.
5. Ask, informally: "was there any point where you felt lost, bored, or
   unsure what a term meant?" Write down whatever they say verbatim — don't
   paraphrase it into your own words yet.
6. Move to the next chapter, or stop for the day — don't run all 10
   chapters in one sitting; fatigue will contaminate the reading-experience
   signal for later chapters.
7. One week later, cold: ask the comprehension question again for every
   chapter they read, with no re-reading allowed beforehand. Score
   retention.

## Scoring sheet template

Copy this table per reader (e.g. `testing/results/reader-1.md` — this
`results/` subfolder is intentionally not created yet; make it when you
have actual sessions to log, so an empty scaffold doesn't imply data that
doesn't exist):

| Chapter | Comprehension | Transfer | Misconception resistance | Retention (1wk) | Reading-experience notes |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

## What to do with the results

- Any concept scoring low on **comprehension** across multiple readers:
  the explanation itself needs rework — likely too fast, or missing an
  intermediate step.
- Low **transfer**, high comprehension: the reader can repeat the chapter's
  own example but hasn't generalized the underlying idea — usually fixed by
  adding a second example or a "predict what happens" prompt (see the one
  already added to Chapter 5, §6, as a template for this pattern).
- Low **misconception resistance** despite the chapter directly addressing
  it: the misconception block isn't landing — consider moving it earlier,
  or strengthening the analogy.
- Low **retention** despite good same-day comprehension: the chapter may be
  memorable in the moment but not sticky — often fixed by a sharper
  canonical diagram or a punchier one-sentence takeaway (template §8).
- Recurring "lost/bored" reports at the same *point* across multiple
  readers, independent of chapter: a structural problem (pacing, template
  rigidity) rather than a content problem in that one chapter — cross-check
  against the "chapters feel compressed" and "template rhythm" concerns
  already logged in `ROADMAP.md`.

Feed concrete findings back into the relevant chapter file directly, and
log the revision in `CHANGELOG.md`, the same way any other correction is
tracked.
