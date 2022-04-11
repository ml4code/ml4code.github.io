---
layout: publication
title: Code Completion with Neural Attention and Pointer Networks
authors: Jian Li, Yue Wang, Michael R. Lyu, Irwin King
conference: 
year: 2017
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1711.09573"}
tags: ["language model", "autocomplete"]
---
Intelligent code completion has become an essential tool to accelerate modern software development. To facilitate effective code completion for dynamically-typed programming languages, we apply neural language models by learning from large codebases, and investigate the effectiveness of attention mechanism on the code completion task. However, standard neural language models even with attention mechanism cannot correctly predict out-of-vocabulary (OoV) words thus restrict the code completion performance. In this paper, inspired by the prevalence of locally repeated terms in program source code, and the recently proposed pointer networks which can reproduce words from local context, we propose a pointer mixture network for better predicting OoV words in code completion. Based on the context, the pointer mixture network learns to either generate a within-vocabulary word through an RNN component, or copy an OoV word from local context through a pointer component. Experiments on two benchmarked datasets demonstrate the effectiveness of our attention mechanism and pointer mixture network on the code completion task. 

