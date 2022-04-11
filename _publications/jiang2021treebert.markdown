---
layout: publication
title: "TreeBERT: A Tree-Based Pre-Trained Model for Programming Language"
authors: Xue Jiang, Zhuoran Zheng, Chen Lyu, Liang Li, Lei Lyu
conference: UAI
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.12485"}
tags: ["grammar", "Transformer"]
---
Source code can be parsed into the abstract syntax tree (AST) based on defined syntax rules. However, in pre-training, little work has considered the incorporation of tree structure into the learning process. In this paper, we present TreeBERT, a tree-based pre-trained model for improving programming language-oriented generation tasks. To utilize tree structure, TreeBERT represents the AST corresponding to the code as a set of composition paths and introduces node position embedding. The model is trained by tree masked language modeling (TMLM) and node order prediction (NOP) with a hybrid objective. TMLM uses a novel masking strategy designed according to the tree's characteristics to help the model understand the AST and infer the missing semantics of the AST. With NOP, TreeBERT extracts the syntactical structure by learning the order constraints of nodes in AST. We pre-trained TreeBERT on datasets covering multiple programming languages. On code summarization and code documentation tasks, TreeBERT outperforms other pre-trained models and state-of-the-art models designed for these tasks. Furthermore, TreeBERT performs well when transferred to the pre-trained unseen programming language. 
