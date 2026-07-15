# Chapter 15 — Why Models Hallucinate

> **Part:** The Transformer · **Concept Level:** Level 5 · **Prerequisites:** Chapter 9 (training), Chapter 14 (inference, sampling)
> **New concepts introduced:** Hallucinations

---

## 1. Opening Question

> *If the model is just sampling plausible-sounding tokens, what happens when "plausible-sounding" and "actually true" come apart?*

## 2. Real-World Story

In 2023, a lawyer submitted a legal brief citing several past court
cases to support his argument. The citations looked completely
legitimate: proper formatting, plausible party names, plausible courts
and years. The problem was that the cases didn't exist. He had used an AI
chatbot to help research the brief, and it had generated citations that
looked exactly like real legal citations — because it had learned,
extremely well, what real legal citations look like — without those
specific cases ever having existed.

The system wasn't lying, in the sense of intending to deceive. It was
doing precisely what Chapter 6 described: producing a highly plausible
continuation of text, given the patterns in its training data. In this
case, "plausible-sounding legal citation" and "citation of a real case"
had quietly come apart, and nothing in the generation process itself
flagged the difference.

## 3. Worked Example

Ask a model to produce a citation for a specific, narrow legal question.
It has, across enormous amounts of legal text, thoroughly learned the
*pattern* a citation takes: party name, "v.," another party name, court,
year, volume and page number, all in a familiar, recognizable format.
Producing a token sequence that matches this pattern fluently is exactly
what next-token prediction (Chapter 6) is built to do well — it doesn't
require this specific case to be real, only that the sequence be
statistically consistent with what citations generally look like.

Nothing in the training objective from Chapter 9 directly rewards "and
also, verify this specific case actually exists in the real world" as a
separate step. The model was trained to predict likely next tokens given
patterns in text, not to cross-check every generated claim against an
external record of what's real. For extremely common, heavily-repeated
facts, this rarely matters, because the true fact is also the
overwhelmingly likely continuation. For a rare, specific, or nonexistent
case, the model still has to produce *something* — and what it produces
is a plausible-looking fabrication, not a flagged gap.

## 4. Core Intuition

A **hallucination** is fluent, confident, plausible-sounding output that
is nonetheless factually wrong or entirely fabricated — not because the
model is lying (it has no intention, and nothing resembling a separate
"belief" it's concealing), but because next-token prediction (Chapter 6)
optimizes for statistical plausibility given training-data patterns, not
for correspondence with truth about the actual world. A model has no
built-in mechanism that checks "is this actually true" as something
separate from "does this sound like the kind of thing that's usually said
here."

## 5. Technical Explanation

Connect this directly back to training (Chapter 9): the training
objective rewards predicting the next token accurately *relative to the
training text*, not relative to ground truth about reality. For
well-represented, heavily-repeated facts — "the capital of France is
Paris" — this distinction rarely bites, because the correct fact is also
the overwhelmingly common continuation across virtually all relevant
training text, so statistical plausibility and truth line up.

For rare, obscure, or entirely nonexistent facts — a specific, uncommon
court case, a specific minor historical date, a citation for a paper that
doesn't exist — the alignment between "statistically plausible" and
"actually true" breaks down, but the model still must produce *some*
continuation (Chapter 14's sampling still has to select a token). Unless
it has been specifically trained or aligned (Chapter 13's preview,
Chapter 19's full treatment) to prefer expressing uncertainty or
declining to answer in exactly these situations, it fills the gap with a
fluent, confident-sounding fabrication rather than a flagged absence.

## 6. Common Misconceptions

> **Misconception:** "Hallucination is a rare bug that will simply get fixed as models improve."
> **Why it's wrong:** It's less a discrete defect than a structural tension between "always produce a fluent, confident continuation" and "only state things that are true" — a tension inherent to how next-token prediction works, not a simple coding error.
> **Correct intuition:** Mitigations exist and genuinely help (better alignment, retrieval-augmentation in Chapters 17–18, improved calibration of uncertainty), but treat hallucination as an ongoing tradeoff to manage, not a bug awaiting a final patch.
> **Analogy:** A student trained their whole life to always give a confident-sounding answer on every exam question will keep bluffing convincingly on the questions they don't actually know, even after years of additional coaching — the tendency has to be specifically retrained, not merely reduced by getting generally smarter.

> **Misconception:** "The model knows it's making something up and is choosing to deceive."
> **Why it's wrong:** There's no separate module tracking "what I actually know is true" apart from "what token comes next" — it's the same fluent generation process whether the content happens to be accurate or fabricated, and the confidence of the phrasing doesn't reliably track any internal certainty, because there isn't a distinct "certainty" signal being consulted.
> **Correct intuition:** Confident phrasing and factual accuracy are produced by the same process but aren't causally linked — one doesn't guarantee the other.
> **Analogy:** A fluent public speaker can sound equally confident whether reciting a well-verified fact or a half-remembered detail — confidence of delivery and accuracy of content are simply different things.

## 7. Practical Implications

This is precisely why giving a model access to real source documents to
draw from — retrieval-augmented generation, covered in Chapters 17–18 —
is such a widely used mitigation: it gives the model something concrete
to ground its answer in, rather than relying purely on trained-in
patterns for rare or specific facts. It's also the direct reason
practitioners are consistently told to verify AI-generated facts and
citations, especially for anything rare, specific, or high-stakes, and
why hallucination rates differ noticeably between well-represented common
knowledge and obscure or narrow topics.

## 8. Key Takeaway

**Hallucination isn't the model lying — it's fluent, confident next-token prediction continuing exactly as designed, in a case where statistical plausibility and factual truth have quietly come apart.**

## 9. One-Page Summary

- A hallucination is fluent, plausible-sounding output that is factually wrong or fabricated, without any intention to deceive.
- Next-token prediction (Chapter 6) optimizes for statistical plausibility relative to training text, not for truth about the real world.
- For common, heavily-repeated facts, plausibility and truth usually align; for rare or nonexistent facts, they can come apart.
- The model has no built-in mechanism separating "sounds right" from "is actually true" unless specifically trained to flag uncertainty.
- Retrieval-augmented generation (Chapters 17–18) is a major practical mitigation, giving the model real source material to ground answers in.
- Hallucination is best treated as an ongoing, manageable tradeoff rather than a simple bug awaiting a final fix.

## 10. Further Reading

- Search for documented cases of AI-generated fake legal citations (including the case referenced in this chapter) for real, verifiable examples of this failure mode in practice.

## 11. The Next Obvious Question

> *If a model's own trained-in knowledge can run out or go stale, how can it be given a bigger, more reliable memory to draw from?*

---

**Glossary terms added this chapter:** Hallucination → append to `/glossary.md`
**Misconceptions logged this chapter:** "hallucination is a rare bug that will get fixed"; "the model knows it's making things up" → append to `/misconceptions.md`
**Concept-graph entries checked off:** Level 5 — Hallucinations, at Ch. 15 (closes Part III)
