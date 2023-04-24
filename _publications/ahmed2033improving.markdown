---
layout: publication
title: "Improving Few-Shot Prompts with Relevant Static Analysis Products"
authors: Toufique Ahmed, Kunal Suresh Pai, Premkumar Devanbu, Earl T. Barr
conference: 
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2304.06815"}
tags: ["summarization", "Transformer"]
---
Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. We are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously have a collection of semantics facts in mind when working on coding tasks. Mostly these are shallow, simple facts arising from a quick read. For a function, examples of facts might include parameter and local variable names, return expressions, simple pre- and post-conditions, and basic control and data flow, etc.

One might assume that the powerful multi-layer architecture of transformer-style LLMs makes them inherently capable of doing this simple level of "code analysis" and extracting such information, implicitly, while processing code: but are they, really? If they aren't, could explicitly adding this information help? Our goal here is to investigate this question, using the code summarization task and evaluate whether automatically augmenting an LLM's prompt with semantic facts explicitly, actually helps.

Prior work shows that LLM performance on code summarization benefits from few-shot samples drawn either from the same-project or from examples found via information retrieval methods (such as BM25). While summarization performance has steadily increased since the early days, there is still room for improvement: LLM performance on code summarization still lags its performance on natural-language tasks like translation and text summarization.

We find that adding semantic facts actually does help! This approach improves performance in several different settings suggested by prior work, including for two different Large Language Models. In most cases, improvement nears or exceeds 2 BLEU; for the PHP language in the challenging CodeSearchNet dataset, this augmentation actually yields performance surpassing 30 BLEU. 
