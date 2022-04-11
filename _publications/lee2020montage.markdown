---
layout: publication
title: "Montage: A Neural Network Language Model-Guided JavaScript Engine Fuzzer"
authors: Suyoung Lee, HyungSeok Han, Sang Kil Cha, Sooel Son
conference: USENIX
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2001.04107"}
tags: ["fuzzing", "language model"]
---
JavaScript (JS) engine vulnerabilities pose significant security threats affecting billions of web browsers. While fuzzing is a prevalent technique for finding such vulnerabilities, there have been few studies that leverage the recent advances in neural network language models (NNLMs). In this paper, we present Montage, the first NNLM-guided fuzzer for finding JS engine vulnerabilities. The key aspect of our technique is to transform a JS abstract syntax tree (AST) into a sequence of AST subtrees that can directly train prevailing NNLMs. We demonstrate that Montage is capable of generating valid JS tests, and show that it outperforms previous studies in terms of finding vulnerabilities. Montage found 37 real-world bugs, including three CVEs, in the latest JS engines, demonstrating its efficacy in finding JS engine bugs. 
