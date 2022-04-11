---
layout: publication
title: "Abstract Syntax Networks for Code Generation and Semantic Parsing"
authors: Maxim Rabinovich, Mitchell Stern, Dan Klein
conference: ACL
year: 2017
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1704.07535"}
tags: ["code generation", "grammar"]
---
Tasks like code generation and semantic parsing require mapping unstructured (or partially structured) inputs to well-formed, executable outputs. We introduce abstract syntax networks, a modeling framework for these problems. The outputs are represented as abstract syntax trees (ASTs) and constructed by a decoder with a dynamically-determined modular structure paralleling the structure of the output tree. On the benchmark Hearthstone dataset for code generation, our model obtains 79.2 BLEU and 22.7% exact match accuracy, compared to previous state-of-the-art values of 67.1 and 6.1%. Furthermore, we perform competitively on the Atis, Jobs, and Geo semantic parsing datasets with no task-specific engineering. 
