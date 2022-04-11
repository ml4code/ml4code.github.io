---
layout: publication
title: "A Neural Approach to Decompiled Identifier Renaming"
authors: Jeremy Lacomis, Pengcheng Yin, Edward J. Schwartz, Miltiadis Allamanis, Claire Le Goues, Graham Neubig, Bogdan Vasilescu
conference: ASE
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1909.09029"}
   - {name: "Code and Data", url: "https://github.com/pcyin/dire"}
tags: ["deobfuscation", "naming", "compilation"]
---
The decompiler is one of the most common tools for examining binaries without corresponding source code. It transforms binaries into high-level code, reversing the compilation process. However, compilation loses information contained within the original source code (e.g. structure, type information, and variable names). Semantically meaningful variable names are known to increase code understandability, but they generally cannot be recovered by decompilers. We propose the Decompiled Identifier Renaming Engine (DIRE), a novel probabilistic technique for variable name recovery that uses both lexical and structural information. We also present a technique for generating corpora suitable for training and evaluating models of decompiled code renaming, which we use to create a corpus of 164,632 unique x86-64 binaries generated from C projects mined from GitHub. Our results show that on this corpus DIRE can predict variable names identical to the names in the original source code up to 74.3% of the time.
