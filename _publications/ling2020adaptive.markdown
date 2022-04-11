---
layout: publication
title: "Adaptive Deep Code Search"
authors: Chunyang Ling, Zeqi Lin, Yanzhen Zou, Bing Xie
conference: ICPC
year: 2020
additional_links:
  - { name: "ACM", url: "https://dl.acm.org/doi/abs/10.1145/3387904.3389278" }
tags: ["search"]
---

Searching code in a large-scale codebase using natural language queries is a common practice during software development. Deep learning-based code search methods demonstrate superior performance if models are trained with large amount of text-code pairs. However, few deep code search models can be easily transferred from one codebase to another. It can be very costly to prepare training data for a new codebase and re-train an appropriate deep learning model. In this paper, we propose AdaCS, an adaptive deep code search method that can be trained once and transferred to new codebases. AdaCS decomposes the learning process into embedding domain-specific words and matching general syntactic patterns. Firstly, an unsupervised word embedding technique is used to construct a matching matrix to represent the lexical similarities. Then, a recurrent neural network is used to capture latent syntactic patterns from these matching matrices in a supervised way. As the supervised task learns general syntactic patterns that exist across domains, AdaCS is transferable to new codebases. Experimental results show that: when extended to new software projects never seen in the training data, AdaCS is more robust and significantly outperforms state-of-the-art deep code search methods.
