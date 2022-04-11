---
layout: publication
title: "Bag-of-Words Baselines for Semantic Code Search"
authors: Xinyu Zhang, Ji Xin, Andrew Yates, Jimmy Lin
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.10.pdf"}
tags: ["search"]
---
The task of semantic code search is to retrieve code snippets from a source code corpus based on an information need expressed in natural language. The semantic gap between natural language and programming languages has for long been regarded as one of the most significant obstacles to the effectiveness of keyword-based information retrieval (IR) methods. It is a common assumption that “traditional” bag-of-words IR methods are poorly suited for semantic code search: our work empirically investigates this assumption. Specifically, we examine the effectiveness of two traditional IR methods, namely BM25 and RM3, on the CodeSearchNet Corpus, which consists of natural language queries paired with relevant code snippets. We find that the two keyword-based methods outperform several pre-BERT neural models. We also compare several code-specific data pre-processing strategies and find that specialized tokenization improves effectiveness.
