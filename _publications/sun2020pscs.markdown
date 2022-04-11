---
layout: publication
title: "PSCS: A Path-based Neural Model for Semantic Code Search"
authors: Zhensu Sun, Yan Liu, Chen Yang, Yu Qian
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2008.03042"}
tags: ["grammar", "search"]
---
To obtain code snippets for reuse, programmers prefer to search for related documents, e.g., blogs or Q&A, instead of code itself. The major reason is due to the semantic diversity and mismatch between queries and code snippets. Deep learning models have been proposed to address this challenge. Compared with approaches using information retrieval techniques, deep learning models do not suffer from the information loss caused by refining user intention into keywords. However, the performance of previous works is not satisfactory because they ignore the importance of code structure. When the semantics of code (e.g., identifier names, APIs) are ambiguous, code structure may be the only feature for the model to utilize. In that case, previous works relearn the structural information from lexical tokens of code, which is extremely difficult for a model without any domain knowledge. In this work, we propose PSCS, a path-based neural model for semantic code search. Our model encodes both the semantics and structures of code represented by AST paths. We train and evaluate our model over 330k-19k query-function pairs, respectively. The evaluation results demonstrate that PSCS achieves a SuccessRate of 47.6% and a Mean Reciprocal Rank (MRR) of 30.4% when considering the top-10 results with a match. The proposed approach significantly outperforms both DeepCS, the first approach that applies deep learning to code search task, and CARLCS, a state-of-the-art approach that introduces a co-attentive representation learning model on the basis of DeepCS. The importance of code structure is demonstrated with an ablation study on code features, which enlightens model design for further studies. 
