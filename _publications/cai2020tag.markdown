---
layout: publication
title: "TAG : Type Auxiliary Guiding for Code Comment Generation"
authors: Ruichu Cai, Zhihao Liang, Boyan Xu, Zijian Li, Yuexing Hao, Yao Chen
conference: ACL
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.02835"}
tags: ["bimodal", "documentation"]
---
Existing leading code comment generation approaches with the structure-to-sequence framework ignores the type information of the interpretation of the code, e.g., operator, string, etc. However, introducing the type information into the existing framework is non-trivial due to the hierarchical dependence among the type information. In order to address the issues above, we propose a Type Auxiliary Guiding encoder-decoder framework for the code comment generation task which considers the source code as an N-ary tree with type information associated with each node. Specifically, our framework is featured with a Type-associated Encoder and a Type-restricted Decoder which enables adaptive summarization of the source code. We further propose a hierarchical reinforcement learning method to resolve the training difficulties of our proposed framework. Extensive evaluations demonstrate the state-of-the-art performance of our framework with both the auto-evaluated metrics and case studies. 
