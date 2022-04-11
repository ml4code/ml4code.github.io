---
layout: publication
title: "On the Generalizability of Neural Program Analyzers with respect to Semantic-Preserving Program Transformations"
authors: Md. Rafiqul Islam Rabin, Nghi D. Q. Bui, Yijun Yu, Lingxiao Jiang, Mohammad Amin Alipour
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2008.01566"}
tags: ["adversarial", "GNN", "grammar"]
---
With the prevalence of publicly available source code repositories to train deep neural network models, neural program analyzers can do well in source code analysis tasks such as predicting method names in given programs that cannot be easily done by traditional program analyzers. Although such analyzers have been tested on various existing datasets, the extent in which they generalize to unforeseen source code is largely unknown. Since it is impossible to test neural program analyzers on all unforeseen programs, in this paper, we propose to evaluate the generalizability of neural program analyzers with respect to semantic-preserving transformations: a generalizable neural program analyzer should perform equally well on programs that are of the same semantics but of different lexical appearances and syntactical structures. More specifically, we compare the results of various neural program analyzers for the method name prediction task on programs before and after automated semantic-preserving transformations. We use three Java datasets of different sizes and three state-of-the-art neural network models for code, namely code2vec, code2seq, and Gated Graph Neural Networks (GGNN), to build nine such neural program analyzers for evaluation. Our results show that even with small semantically preserving changes to the programs, these neural program analyzers often fail to generalize their performance. Our results also suggest that neural program analyzers based on data and control dependencies in programs generalize better than neural program analyzers based only on abstract syntax trees. On the positive side, we observe that as the size of training dataset grows and diversifies the generalizability of correct predictions produced by the analyzers can be improved too. 
