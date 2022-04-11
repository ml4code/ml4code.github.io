---
layout: publication
title: "Learning to Mine Aligned Code and Natural Language Pairs from Stack Overflow"
authors: Pengcheng Yin, B. Deng, E. Chen, B. Vasilescu, Graham Neubig
conference: MSR
year: 2018
additional_links:
   - {name: "data", url: "https://conala-corpus.github.io/"}
tags: ["dataset"]
---
For tasks like code synthesis from natural language, code retrieval, and code summarization, data-driven models have shown great promise. However, creating these models require parallel data between natural language (NL) and code with fine-grained alignments. Stack Overflow (SO) is a promising source to create such a data set: the questions are diverse and most of them have corresponding answers with high-quality code snippets. However, existing heuristic methods (e.g., pairing the title of a post with the code in the accepted answer) are limited both in their coverage and the correctness of the NL-code pairs obtained. In this paper, we propose a novel method to mine high-quality aligned data from SO using two sets of features: hand-crafted features considering the structure of the extracted snippets, and correspondence features obtained by training a probabilistic model to capture the correlation between NL and code using neural networks. These features are fed into a classifier that determines the quality of mined NL-code pairs. Experiments using Python and Java as test beds show that the proposed method greatly expands coverage and accuracy over existing mining methods, even when using only a small number of labeled examples. Further, we find that reasonable results are achieved even when training the classifier on one language and testing on another, showing promise for scaling NL-code mining to a wide variety of programming languages beyond those for which we are able to annotate data. 

