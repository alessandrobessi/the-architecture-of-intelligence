# Chapter 14 — Inference and Text Generation

> **Part:** The Transformer · **Concept Level:** Level 4 · **Prerequisites:** Chapter 6 (prediction), Chapter 12 (transformer blocks)
> **New concepts introduced:** Inference, Sampling

---

## 1. Opening Question

> *Once a model has all this training baked in, what actually happens, step by step, when it generates a response to your prompt?*

## 2. Real-World Story

A medical student spends years in school: studying, practicing, getting
things wrong, being corrected, adjusting — precisely the training loop
from Chapter 9, repeated across an enormous number of cases. Then, on the
day of the licensing exam, something changes. The studying is over. The
student can't look anything up, can't revise their underlying knowledge
mid-exam, can't get corrected and try again. They simply apply everything
they've learned, in the moment, to whatever specific questions appear on
the page in front of them.

The knowledge itself is now fixed — nothing about the exam changes what
the student actually knows. What varies, question to question, is only
how that fixed knowledge gets applied to each specific case. A trained
language model works the same way once training ends: its parameters are
frozen, and every response is that fixed knowledge being applied, fresh,
to whatever specific prompt just arrived.

## 3. Worked Example

Take the prompt "The weather today is" and run it through a trained
model three separate times. Chapter 6 already established that the model
computes a probability distribution over every possible next token — but
it did not specify how one specific token actually gets chosen from that
distribution each time.

If the model always took the single highest-probability token, all three
runs would produce the identical continuation — perhaps "The weather
today is nice," every single time, which is accurate but monotonous, and
prone to visibly looping in longer generations ("nice. The weather today
is nice. The weather today is nice..."). Instead, a model can sample
somewhat randomly among the likely candidates, weighted by their
probability — so the three runs might produce "sunny," "cold," and
"perfect for a walk." None of these is wrong. They're three different,
individually reasonable draws from the same underlying distribution.

## 4. Core Intuition

**Inference** is the process of actually running a trained model to
produce output, using its fixed, already-learned parameters — as opposed
to training (Chapter 9), where those parameters are still being adjusted.
Once training ends, the parameters are frozen; inference is simply
computing forward through the network — embeddings (Chapter 5), attention
and refinement through transformer blocks (Chapters 11–12), and a
next-token probability distribution (Chapter 6) — using those fixed
values, one token at a time.

**Sampling** is the specific method used to actually pick one token from
that predicted probability distribution at each step. The options range
from always taking the single most likely token (deterministic, safe, but
repetitive) to sampling more broadly among likely candidates (more varied
and natural-feeling, at some risk of an occasional odd choice).

## 5. Technical Explanation

A control commonly called **temperature** adjusts how sharply or broadly
sampling draws from the predicted distribution. Low temperature
concentrates almost all the choice on the single most likely token or a
small handful of top candidates — closer to always picking the top
answer. High temperature spreads the choice more evenly across a wider
range of plausible candidates, including some riskier ones, producing
more varied but occasionally less careful output. Related techniques
often called **top-k** or **nucleus sampling** restrict the random choice
to only the most plausible handful of candidates in the first place,
rather than the model's entire vocabulary — preventing an implausible
token from being selected purely by chance, even at higher temperatures.

None of this changes the probabilities the trained network actually
computed. It changes only how one specific token gets chosen from an
already-computed distribution — the same distinction as a weather
forecast (Chapter 6's own analogy) computing a 70% chance of rain, versus
the separate question of what you personally decide to do about it.

## 6. Common Misconceptions

> **Misconception:** "The model is still learning or improving while I chat with it."
> **Why it's wrong:** Unless a system is specifically built to retrain on conversations (unusual, and typically a separate process), inference uses frozen parameters — nothing about a conversation changes the model's underlying trained knowledge.
> **Correct intuition:** What grows during a conversation is the context available to the model (Chapter 16), not the model's trained parameters themselves.
> **Analogy:** A doctor taking your case history during an exam isn't relearning medicine — they're applying fixed training to new, specific information.

> **Misconception:** "Since it's the same model and the same prompt, it should give the exact same answer every time."
> **Why it's wrong:** Unless sampling is explicitly configured to always pick the top choice, controlled randomness is part of the design — repeating the same prompt can, and often does, yield different, still-reasonable responses.
> **Correct intuition:** Identical inputs can produce different outputs by design, because sampling deliberately introduces choice among plausible candidates rather than always taking the single most likely one.
> **Analogy:** Asking three different (equally excellent) writers to finish the same sentence naturally produces three different, all-reasonable endings.

## 7. Practical Implications

This is exactly what a "temperature" slider or setting in an AI tool or
API controls directly. It also explains a genuine, recurring business and
engineering distinction: training is an enormous, largely one-time cost
per model, while inference is a smaller cost paid again every single time
anyone actually uses the model — a distinction that shows up constantly
in discussions of AI infrastructure costs, and one that becomes
especially important once Chapter 20 covers making inference cheaper and
faster.

## 8. Key Takeaway

**Inference is running a trained, frozen model to produce output; sampling is the deliberately controllable randomness in how a specific token gets chosen from the model's predicted probabilities.**

## 9. One-Page Summary

- Inference is using a trained model's fixed parameters to produce output — as opposed to training, where parameters are still being adjusted.
- Sampling is the method for choosing one actual token from the model's predicted probability distribution at each step.
- Temperature controls how narrowly or broadly sampling draws from that distribution; top-k/nucleus sampling restricts choices to the most plausible candidates.
- None of this changes the underlying probabilities the network computed — only how a token gets selected from them.
- Identical prompts can produce different, equally valid outputs by design, because of this controlled randomness.
- Training is a large, mostly one-time cost; inference is a smaller, recurring cost paid every time the model is used.

## 10. Further Reading

- Search for "temperature sampling" and "nucleus sampling" (top-p sampling) for the formal names of the techniques described in this chapter.

## 11. The Next Obvious Question

> *If the model is just sampling plausible-sounding tokens, what happens when "plausible-sounding" and "actually true" come apart?*

---

**Glossary terms added this chapter:** Inference, Sampling, Temperature, Top-k / nucleus sampling → append to `/glossary.md`
**Misconceptions logged this chapter:** "the model keeps learning during conversation"; "same prompt should always give the same answer" → append to `/misconceptions.md`
**Concept-graph entries checked off:** Level 4 — Inference, Sampling, both at Ch. 14
