# Concept Dependency Tracker

Checklist over the 9-level Concept Dependency Graph in blueprint.md. A
concept is checked off once the chapter that introduces it is written. No
concept may be used in prose before its own checkbox (or an earlier level's)
is checked.

**This file is generated from [`concept-graph.yaml`](concept-graph.yaml) —
do not hand-edit it.** Run `python3 scripts/generate_concept_graph_md.py`
after any change to the YAML and commit both files together.

## Level 0 — Information, Symbols, Computation, Probability (intuition)

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Information | ✅ written | Ch. 2 | — | 1 | [link](book/part-1-information/02-what-is-information.md) |
| Symbols | ✅ written | Ch. 2 | — | 0 | [link](book/part-1-information/02-what-is-information.md) |
| Computation | ✅ written | Ch. 2 | symbols | 1 | [link](book/part-1-information/02-what-is-information.md) |
| Probability (intuition) | ✅ written | Ch. 2 | information | 0 | [link](book/part-1-information/02-what-is-information.md) |

## Level 1 — Characters, Words, Tokens, Tokenization, Compression, Context

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Characters | ✅ written | Ch. 3 | symbols | 0 | [link](book/part-1-information/03-characters-words-tokens.md) |
| Words | ✅ written | Ch. 3 | characters | 0 | [link](book/part-1-information/03-characters-words-tokens.md) |
| Tokens | ✅ written | Ch. 3 | characters, words | 1 | [link](book/part-1-information/03-characters-words-tokens.md) |
| Tokenization | ✅ written | Ch. 3 | tokens | 1 | [link](book/part-1-information/03-characters-words-tokens.md) |
| Compression | ✅ written | Ch. 4 | information, probability-intuition, tokenization | 1 | [link](book/part-1-information/04-compressing-language.md) |
| Context | ✅ written | Ch. 4 | tokens | 1 | [link](book/part-1-information/04-compressing-language.md) |

## Level 2 — Embeddings, Vector spaces, Similarity, Semantic geometry

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Embeddings | ✅ written | Ch. 5 | tokens, context | 2 | [link](book/part-1-information/05-meaning-as-geometry.md) |
| Vector spaces | ✅ written | Ch. 5 | embeddings | 0 | [link](book/part-1-information/05-meaning-as-geometry.md) |
| Similarity | ✅ written | Ch. 5 | vector-spaces | 1 | [link](book/part-1-information/05-meaning-as-geometry.md) |
| Semantic geometry | ✅ written | Ch. 5 | similarity | 0 | [link](book/part-1-information/05-meaning-as-geometry.md) |

## Level 3 — Prediction, Neural networks, Parameters, Learning, Training, Loss, Scaling laws

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Prediction | ✅ written | Ch. 6 | probability-intuition, embeddings | 2 | [link](book/part-2-prediction/06-predicting-the-next-token.md) |
| Neural networks | ✅ written | Ch. 8 | prediction | 2 | [link](book/part-2-prediction/08-neural-networks-without-mathematics.md) |
| Parameters | ✅ written | Ch. 8 | neural-networks | 1 | [link](book/part-2-prediction/08-neural-networks-without-mathematics.md) |
| Learning | ✅ written | Ch. 9 | neural-networks, parameters | 1 | [link](book/part-2-prediction/09-learning-from-examples.md) |
| Training | ✅ written | Ch. 9 | learning | 1 | [link](book/part-2-prediction/09-learning-from-examples.md) |
| Loss | ✅ written | Ch. 9 | training | 1 | [link](book/part-2-prediction/09-learning-from-examples.md) |
| Scaling laws | ✅ written | Ch. 10 | parameters, training, loss | 2 | [link](book/part-2-prediction/10-scaling-laws.md) |

## Level 4 — Attention, Positional encoding, Transformer blocks, Inference, Sampling

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Attention | ✅ written | Ch. 11 | embeddings, context, similarity | 2 | [link](book/part-3-the-transformer/11-the-attention-revolution.md) |
| Causal masking | ✅ written | Ch. 11 | attention | 1 | [link](book/part-3-the-transformer/11-the-attention-revolution.md) |
| Attention heads (multi-head attention) | ✅ written | Ch. 11 | attention | 0 | [link](book/part-3-the-transformer/11-the-attention-revolution.md) |
| Positional encoding | ✅ written | Ch. 11 | attention | 1 | [link](book/part-3-the-transformer/11-the-attention-revolution.md) |
| Transformer blocks | ✅ written | Ch. 12 | attention, causal-masking, positional-encoding, neural-networks | 2 | [link](book/part-3-the-transformer/12-building-a-transformer.md) |
| Inference | ✅ written | Ch. 14 | transformer-blocks | 1 | [link](book/part-3-the-transformer/14-inference-and-text-generation.md) |
| Sampling | ✅ written | Ch. 14 | inference, probability-intuition | 1 | [link](book/part-3-the-transformer/14-inference-and-text-generation.md) |

## Level 5 — Hallucinations, Fine-tuning, Alignment, Context windows, Memory

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Hallucinations | ✅ written | Ch. 15 | inference, sampling, training | 2 | [link](book/part-3-the-transformer/15-why-models-hallucinate.md) |
| Fine-tuning | ✅ written | Ch. 19 | training, parameters | 1 | [link](book/part-4-building-useful-ai/19-fine-tuning-and-alignment.md) |
| Alignment | ✅ written | Ch. 19 | fine-tuning | 1 | [link](book/part-4-building-useful-ai/19-fine-tuning-and-alignment.md) |
| Context windows | ✅ written | Ch. 16 | context, inference | 1 | [link](book/part-4-building-useful-ai/16-context-windows-and-memory.md) |
| Memory | ✅ written | Ch. 16 | context-windows | 1 | [link](book/part-4-building-useful-ai/16-context-windows-and-memory.md) |

## Level 6 — Retrieval, Vector databases, RAG, Tool calling, MCP, AI agents

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Retrieval | ✅ written | Ch. 17 | similarity, context-windows | 1 | [link](book/part-4-building-useful-ai/17-semantic-retrieval-and-vector-databases.md) |
| Vector databases | ✅ written | Ch. 17 | embeddings, similarity, retrieval | 1 | [link](book/part-4-building-useful-ai/17-semantic-retrieval-and-vector-databases.md) |
| Retrieval-Augmented Generation (RAG) | ✅ written | Ch. 18 | retrieval, context-windows, inference | 2 | [link](book/part-4-building-useful-ai/18-retrieval-augmented-generation.md) |
| Tool calling | ✅ written | Ch. 21 | inference, context-windows | 2 | [link](book/part-5-ai-systems/21-how-models-reach-into-the-world.md) |
| Model Context Protocol (MCP) | ✅ written | Ch. 21 | tool-calling | 1 | [link](book/part-5-ai-systems/21-how-models-reach-into-the-world.md) |
| AI agents | ✅ written | Ch. 22 | tool-calling, memory, inference | 3 | [link](book/part-5-ai-systems/22-from-single-calls-to-agents.md) |

## Level 7 — Reasoning models, Multimodality, Mixture of Experts, Quantization, Efficient inference

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Reasoning models | ✅ written | Ch. 23 | inference, sampling, training | 3 | [link](book/part-5-ai-systems/23-thinking-longer-not-just-faster.md) |
| Multimodality | ✅ written | Ch. 24 | tokens, embeddings, transformer-blocks | 4 | [link](book/part-5-ai-systems/24-one-model-many-senses.md) |
| Mixture of Experts | ✅ written | Ch. 25 | transformer-blocks, parameters | 3 | [link](book/part-5-ai-systems/25-many-experts-one-model.md) |
| Quantization | ✅ written | Ch. 20 | parameters | 1 | [link](book/part-4-building-useful-ai/20-quantization-and-efficient-models.md) |
| Efficient inference | ✅ written | Ch. 20 | inference, quantization | 1 | [link](book/part-4-building-useful-ai/20-quantization-and-efficient-models.md) |
| KV cache | ✅ written | Ch. 20 | attention, inference | 0 | [link](book/part-4-building-useful-ai/20-quantization-and-efficient-models.md) |

## Level 8 — Evaluation, Observability, Security, Safety, AI engineering

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Evaluation | ✅ written | Ch. 26 | hallucinations, training | 3 | [link](book/part-6-the-future/26-evaluating-ai-systems.md) |
| Observability | ✅ written | Ch. 27 | evaluation, ai-agents | 2 | [link](book/part-6-the-future/27-ai-engineering-and-observability.md) |
| Security | ✅ written | Ch. 28 | tool-calling, ai-agents | 2 | [link](book/part-6-the-future/28-security-and-safety.md) |
| Safety | ✅ written | Ch. 28 | alignment, security | 1 | [link](book/part-6-the-future/28-security-and-safety.md) |
| AI engineering | ✅ written | Ch. 27 | evaluation, observability, retrieval, ai-agents | 1 | [link](book/part-6-the-future/27-ai-engineering-and-observability.md) |
