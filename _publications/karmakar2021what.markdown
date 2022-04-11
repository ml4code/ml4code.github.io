---
layout: publication
title: "What do pre-trained code models know about code?"
authors: Anjan Karmakar, Romain Robbes
conference: 
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.11308"}
tags: ["Transformer"]
---
Pre-trained models of code built on the transformer architecture have performed well on software engineering (SE) tasks such as predictive code generation, code summarization, among others. However, whether the vector representations from these pre-trained models comprehensively encode characteristics of source code well enough to be applicable to a broad spectrum of downstream tasks remains an open question.

One way to investigate this is with diagnostic tasks called probes. In this paper, we construct four probing tasks (probing for surface-level, syntactic, structural, and semantic information) for pre-trained code models. We show how probes can be used to identify whether models are deficient in (understanding) certain code properties, characterize different model layers, and get insight into the model sample-efficiency.

We probe four models that vary in their expected knowledge of code properties: BERT (pre-trained on English), CodeBERT and CodeBERTa (pre-trained on source code, and natural language documentation), and GraphCodeBERT (pre-trained on source code with dataflow). While GraphCodeBERT performs more consistently overall, we find that BERT performs surprisingly well on some code tasks, which calls for further investigation. 
