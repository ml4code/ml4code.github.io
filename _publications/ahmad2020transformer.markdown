---
layout: publication
title: "A Transformer-based Approach for Source Code Summarization"
authors: Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray, Kai-Wei Chang
conference: ACL
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.00653"}
   - {name: "Code", url: "https://github.com/wasiahmad/NeuralCodeSum"}
tags: ["summarization"]
---
Generating a readable summary that describes the functionality of a program is known as source code summarization. In this task, learning code representation by modeling the pairwise relationship between code tokens to capture their long-range dependencies is crucial. To learn code representation for summarization, we explore the Transformer model that uses a self-attention mechanism and has shown to be effective in capturing long-range dependencies. In this work, we show that despite the approach is simple, it outperforms the state-of-the-art techniques by a significant margin. We perform extensive analysis and ablation studies that reveal several important findings, e.g., the absolute encoding of source code tokens' position hinders, while relative encoding significantly improves the summarization performance. We have made our code publicly available to facilitate future research. 
