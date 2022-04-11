---
layout: publication
title: "Deep Graph Matching and Searching for Semantic Code Retrieval"
authors: Xiang Ling, Lingfei Wu, Saizhuo Wang, Gaoning Pan, Tengfei Ma, Fangli Xu, Alex X. Liu, Chunming Wu, Shouling Ji
conference: TKDD
year: 2020
additional_links:
  - { name: "ArXiV", url: "https://arxiv.org/abs/2010.12908" }
tags: ["search", "GNN"]
---

Code retrieval is to find the code snippet from a large corpus of source code repositories that highly matches the query of natural language description. Recent work mainly uses natural language processing techniques to process both query texts (i.e., human natural language) and code snippets (i.e., machine programming language), however neglecting the deep structured features of query texts and source codes, both of which contain rich semantic information. In this paper, we propose an end-to-end deep graph matching and searching (DGMS) model based on graph neural networks for the task of semantic code retrieval. To this end, we first represent both natural language query texts and programming language code snippets with the unified graph-structured data, and then use the proposed graph matching and searching model to retrieve the best matching code snippet. In particular, DGMS not only captures more structural information for individual query texts or code snippets but also learns the fine-grained similarity between them by cross-attention based semantic matching operations. We evaluate the proposed DGMS model on two public code retrieval datasets with two representative programming languages (i.e., Java and Python). Experiment results demonstrate that DGMS significantly outperforms state-of-the-art baseline models by a large margin on both datasets. Moreover, our extensive ablation studies systematically investigate and illustrate the impact of each part of DGMS.
