---
layout: publication
title: "Multi-Modal Attention Network Learning for Semantic Source Code Retrieval"
authors: Yao Wan, Jingdong Shu, Yulei Sui, Guandong Xu, Zhou Zhao, Jian Wu, Philip S. Yu
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1909.13516"}
tags: ["search"]
---
Code retrieval techniques and tools have been playing a key role in facilitating software developers to retrieve existing code fragments from available open-source repositories given a user query. Despite the existing efforts in improving the effectiveness of code retrieval, there are still two main issues hindering them from being used to accurately retrieve satisfiable code fragments from large-scale repositories when answering complicated queries. First, the existing approaches only consider shallow features of source code such as method names and code tokens, but ignoring structured features such as abstract syntax trees (ASTs) and control-flow graphs (CFGs) of source code, which contains rich and well-defined semantics of source code. Second, although the deep learning-based approach performs well on the representation of source code, it lacks the explainability, making it hard to interpret the retrieval results and almost impossible to understand which features of source code contribute more to the final results.

To tackle the two aforementioned issues, this paper proposes MMAN, a novel Multi-Modal Attention Network for semantic source code retrieval. A comprehensive multi-modal representation is developed for representing unstructured and structured features of source code, with one LSTM for the sequential tokens of code, a Tree-LSTM for the AST of code and a GGNN (Gated Graph Neural Network) for the CFG of code. Furthermore, a multi-modal attention fusion layer is applied to assign weights to different parts of each modality of source code and then integrate them into a single hybrid representation. Comprehensive experiments and analysis on a large-scale real-world dataset show that our proposed model can accurately retrieve code snippets and outperforms the state-of-the-art methods. 
