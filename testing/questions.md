# Reader-Testing Question Bank — Chapters 1–10

See `README.md` in this directory for how to run a session and score
these. Misconception-resistance prompts are paired with the `ID` from
`misconceptions.md` so a scoring gap can be traced directly back to a
specific chapter passage.

## Chapter 1 — Why AI Suddenly Changed

- **Comprehension:** "In your own words, why did AI chatbots suddenly get
  so much better around 2022?"
- **Transfer:** "A headline claims a new AI breakthrough happened because
  of 'a completely new kind of chip.' What would you want to know before
  deciding whether that explains it?"
- **Misconception resistance** (`ai-consciousness-overnight`): "Do you
  think the AI became conscious, or started truly understanding language,
  overnight?"
- **Misconception resistance** (`ai-vs-bigger-chatbot`): "Is a modern
  chatbot just a bigger version of an old 2016 customer-service bot?"

## Chapter 2 — What Is Information?

- **Comprehension:** "What does it actually mean for a computer to 'know'
  or 'read' something?"
- **Transfer:** "A friend says a 100-page report gave them 'a lot of
  information.' Is that necessarily true?"
- **Misconception resistance** (`computation-implies-understanding`):
  "Does a computer that processes your message understand what it means?"
- **Misconception resistance** (`more-data-equals-more-information`):
  "Does more data always mean more information?"

## Chapter 3 — Characters, Words and Tokens

- **Comprehension:** "What is a 'token,' and how is it different from a
  word?"
- **Transfer:** "Why might an AI company charge a different price for the
  exact same sentence written in English versus another language?"
- **Misconception resistance** (`model-reads-letter-by-letter`): "Does the
  model read text one letter at a time, like sounding out a word?"
- **Misconception resistance** (`token-always-one-word`): "Is a token
  always exactly one whole word?"

## Chapter 4 — Compressing Language

- **Comprehension:** "Why can a short sentence carry a lot of meaning?"
- **Transfer:** "Here's an old telegram: 'ARRIVE TUES STOP.' Explain why
  the missing words don't hurt understanding."
- **Misconception resistance** (`compression-loses-meaning`): "Does
  compressing language always lose meaning, the way a blurry photo loses
  detail?"
- **Misconception resistance** (`context-is-just-topic`): "Is 'context'
  just the general topic of a conversation?"

## Chapter 5 — Meaning as Geometry

- **Comprehension:** "What is an embedding?"
- **Transfer:** "Would 'physician' and 'doctor' end up close together or
  far apart on this map? Why?"
- **Transfer (chapter's own thought experiment):** "Would 'hot' be closer
  to 'cold,' or closer to 'sandwich'? Why?" (Correct answer: closer to
  "cold" — same grammatical slot, i.e. similar *use*, not similar
  *meaning*. If the reader says "sandwich," they're reasoning about
  meaning-as-agreement, not meaning-as-use — flag as a live
  misconception-resistance failure even though it's phrased as transfer.)
- **Misconception resistance** (`embeddings-store-definitions`): "Does the
  model store a dictionary definition for each word?"
- **Misconception resistance** (`embedding-is-permanent-meaning`): "Is a
  word's embedding exactly the same no matter what sentence it appears
  in?"

## Chapter 6 — Predicting the Next Token

- **Comprehension:** "How does a model decide what word to write next?"
- **Transfer:** "Does the model plan out its whole answer before it starts
  writing the first word?"
- **Misconception resistance** (`model-plans-whole-sentence`): same
  question as transfer, above — score both from one answer.
- **Misconception resistance** (`prediction-is-lookup`): "Is the model
  looking up your exact question in a giant table of memorized answers?"

## Chapter 7 — Why Statistics Are Not Enough

- **Comprehension:** "Why doesn't a simple word-counting table work as
  well as a neural network?"
- **Transfer:** "If we collected 100x more text for a counting table,
  would that fix the problem?"
- **Misconception resistance** (`bigger-counting-table-works`): same
  question as transfer, above.
- **Misconception resistance** (`ai-is-bigger-counting-table`): "Is modern
  AI just a much bigger version of this same counting approach?"

## Chapter 8 — Neural Networks Without Mathematics

- **Comprehension:** "What is a neural network, in your own words?"
- **Transfer:** "Is a modern AI model literally simulating a human brain?"
- **Misconception resistance** (`nn-simulates-brain`): same question as
  transfer, above.
- **Misconception resistance** (`more-parameters-more-understanding`): "If
  Model A has ten times more parameters than Model B, is Model A
  automatically better?"
- **New probe (post-review addition):** "Is a language model literally
  just a long stack of identical layers, all doing the same thing?" —
  correct answer should reference the chapter's added boundary paragraph
  distinguishing this generic network from the transformer (Part III).

## Chapter 9 — Learning From Examples

- **Comprehension:** "How does a neural network learn the right values for
  its parameters?"
- **Transfer:** "If a model's loss keeps going down during training, does
  that mean it's getting smarter in every sense?"
- **Misconception resistance** (`training-is-memorization`): "Does
  training just make the model memorize its training examples, like a
  stored database?"
- **Misconception resistance** (`lower-loss-is-more-intelligence`): same
  question as transfer, above.

## Chapter 10 — Scaling Laws

- **Comprehension:** "What's a scaling law, in your own words?"
- **Transfer:** "Is a bigger AI model always the better choice for a given
  task?"
- **Misconception resistance** (`scaling-laws-unlimited`): "Can you just
  keep scaling a model up forever with no limit?"
- **Misconception resistance** (`bigger-model-always-better`): same
  question as transfer, above.
- **New probe (post-review addition):** "When people say the loss-vs-compute
  chart is 'a straight line,' does that mean loss drops by the same fixed
  amount every time you double the compute?" — correct answer should
  reflect that both axes are scaled in multiples of ten, not that loss
  falls linearly on an ordinary chart.
