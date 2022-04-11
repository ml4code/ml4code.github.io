---
layout: publication
title: "Learning Programmatic Idioms for Scalable Semantic Parsing"
authors: Srinivasan Iyer, Alvin Cheung, Luke Zettlemoyer
conference: 
year: 2019
tags: ["pattern mining", "code generation", "grammar"]
---
Programmers typically organize executable source code using high-level coding patterns or idiomatic structures such as nested loops, exception handlers and recursive blocks, rather than as individual code tokens. In contrast, state of the art semantic parsers still map natural language instructions to source code by building the code syntax tree one node at a time. In this paper, we introduce an iterative method to extract code idioms from large source code corpora by repeatedly collapsing most-frequent depth-2 subtrees of their syntax trees, and we train semantic parsers to apply these idioms during decoding. We apply this idiom-based code generation to a recent context-dependent semantic parsing task, and improve the state of the art by 2.2% BLEU score while reducing training time by more than 50%. This improved speed enables us to scale up the model by training on an extended training set that is 5x times larger, to further move up the state of the art by an additional 2.3% BLEU and 0.9% exact match. 
