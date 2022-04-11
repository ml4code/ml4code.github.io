---
layout: publication
title: "SCELMo: Source Code Embeddings from Language Models"
authors: Rafael-Michael Karampatsis, Charles Sutton
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.13214"}
tags: ["pretraining", "defect"]
---
Continuous embeddings of tokens in computer programs have been used to support a variety of software development tools, including readability, code search, and program repair. Contextual embeddings are common in natural language processing but have not been previously applied in software engineering. We introduce a new set of deep contextualized word representations for computer programs based on language models. We train a set of embeddings using the ELMo (embeddings from language models) framework of Peters et al (2018). We investigate whether these embeddings are effective when fine-tuned for the downstream task of bug detection. We show that even a low-dimensional embedding trained on a relatively small corpus of programs can improve a state-of-the-art machine learning system for bug detection. 
