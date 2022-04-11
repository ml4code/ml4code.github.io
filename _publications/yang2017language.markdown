---
layout: publication
title: A Language Model for Statements of Software Code
authors: Yixiao Yang, Yu Jiang, Ming Gu, Jiaguang Sun, Jian Gao, Han Liu
conference: ASE
year: 2017
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/citation.cfm?id=3155647"}
tags: ["language model"]
---
Building language models for source code enables a large set of improvements on traditional software engineering tasks. One promising application is automatic code completion. State-of-the-art techniques capture code regularities at token level with lexical information. Such language models are more suitable for predicting short token sequences, but become less effective with respect to long statement level predictions. In this paper, we have proposed PCC to optimize the token level based language modeling. Specifically, PCC introduced an intermediate representation (IR) for source code, which puts tokens into groups using lexeme and variable relative order. In this way, PCC is able to handle long token sequences, i.e., group sequences, to suggest a complete statement with the precise synthesizer. Further more, PCC employed a fuzzy matching technique which combined genetic and longest common sub-sequence algorithms to make the prediction more accurate. We have implemented a code completion plugin for Eclipse and evaluated it on open-source Java projects. The results have demonstrated the potential of PCC in generating precise long statement level predictions. In 30%-60% of the cases, it can correctly suggest the complete statement with only six candidates, and 40%-90% of the cases with ten candidates. 
