---
layout: publication
title: "CoTexT: Multi-task Learning with Code-Text Transformer"
authors: Long Phan, Hieu Tran, Daniel Le, Hieu Nguyen, James Anibal, Alec Peltekian, Yanfang Ye
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.08645"}
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.5.pdf"}
tags: ["Transformer"]
---
We present CoTexT, a transformer-based architecture encoder-decoder pre-trained model that learns the representative context between natural language (NL) and programming language (PL) through multi-task learning. CoTexT is pre-trained, in self-supervised fashion, based on large programming language corpus to learn general-purpose understanding and code-text generation supporting downstream NL-PL task such as code summarizing/documentation, code generation, defect detection, code debugging, etc. We train CoTexT on different combination of available PL corpus including both "bimodal" and "unimodal" data where the former is the combinations of both natural texts and their corresponding code snippets in an input sequence and the latter is merely code snippets. We evaluate multi-task learning CoTexT on different generation and classification tasks on CodeXGLUE and it achieves state-of-the-art on all downstream tasks. 
