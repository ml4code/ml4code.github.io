---
layout: publication
title: "Improving Code Search with Co-Attentive Representation Learning"
authors: Jianhang Shuai, Ling Xu, Chao Liu, Meng Yan, Xin Xia, Yan Lei
conference: ICPC
year: 2020
additional_links:
  - { name: "ACM", url: "https://dl.acm.org/doi/abs/10.1145/3387904.3389269" }
tags: ["search"]
---

Searching and reusing existing code from a large-scale codebase, e.g, GitHub, can help developers complete a programming task efficiently. Recently, Gu et al. proposed a deep learning-based model (i.e., DeepCS), which significantly outperformed prior models. The DeepCS embedded codebase and natural language queries into vectors by two LSTM (long and short-term memory) models separately, and returned developers the code with higher similarity to a code search query. However, such embedding method learned two isolated representations for code and query but ignored their internal semantic correlations. As a result, the learned isolated representations of code and query may limit the effectiveness of code search.

To address the aforementioned issue, we propose a co-attentive representation learning model, i.e., Co-Attentive Representation Learning Code Search-CNN (CARLCS-CNN). CARLCS-CNN learns interdependent representations for the embedded code and query with a co-attention mechanism. Generally, such mechanism learns a correlation matrix between embedded code and query, and co-attends their semantic relationship via row/column-wise max-pooling. In this way, the semantic correlation between code and query can directly affect their individual representations. We evaluate the effectiveness of CARLCS-CNN on Gu et al.'s dataset with 10k queries. Experimental results show that the proposed CARLCS-CNN model significantly outperforms DeepCS by 26.72% in terms of MRR (mean reciprocal rank). Additionally, CARLCS-CNN is five times faster than DeepCS in model training and four times in testing.
