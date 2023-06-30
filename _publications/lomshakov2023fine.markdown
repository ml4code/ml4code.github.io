---
layout: publication
title: Fine-Tuning Large Language Models for Answering Programming Questions with Code Snippets
authors: V. Lomshakov, S. Kovalchuk, M. Omelchenko, S. Nikolenko, A. Aliev
conference: ICCS
year: 2023
additional_links:
   - {name: "LNCS", url: "https://link.springer.com/chapter/10.1007/978-3-031-36021-3_15"}
   - {name: "Papers with Code ", url: "https://paperswithcode.com/paper/fine-tuning-large-language-models-for"}
tags: ["program synthesis", "question answering", "large language models"]
---
We study the ability of pretrained large language models (LLM) to answer questions from online question answering fora such as Stack Overflow. We consider question-answer pairs where the main part of the answer consists of source code. On two benchmark datasets — CoNaLa and a newly collected dataset based on Stack Overflow — we investigate how a closed-book question answering system can be improved by fine-tuning the LLM for the downstream task, prompt engineering, and data preprocessing. We use publicly available autoregressive language models such as GPT-Neo, CodeGen, and PanGu-Coder, and after the proposed fine-tuning achieve a BLEU score of 0.4432 on the CoNaLa test set, significantly exceeding previous state of the art for this task.