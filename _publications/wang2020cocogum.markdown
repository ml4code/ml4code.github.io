---
layout: publication
title: "CoCoGUM: Contextual Code Summarization with Multi-Relational GNN on UMLs"
authors: Yanlin Wang, Lun Du, Ensheng Shi, Yuxuan Hu, Shi Han, Dongmei Zhang 
conference:
year: 2020
additional_links:
   - {name: "TR", url: "https://www.microsoft.com/en-us/research/publication/cocogum-contextual-code-summarization-with-multi-relational-gnn-on-umls/"}
tags: ["summarization"]
---
Code summaries are short natural language (NL) descriptions of code snippets that help developers better understand and maintain source code. Due to the pivotal role of code summaries in software development and maintenance, there is a surge of works on automatic code summarization to reduce the heavy burdens of developers. However, contemporary approaches only leverage the information within the boundary of the method being summarized (i.e., local context), and ignore that using broader context could assist with code summarization. In this paper, we explore two global context information, namely intra-class and inter-class context information, and propose the model CoCoGUM: Contextual Code Summarization with Multi-Relational Graph Neural Networks on UMLs. CoCoGUM first incorporates class names as the intra-class context, which is further fed to a Transformer-based sentence embedding model to extract the class lexical embeddings. Then, relevant Unified Modeling Language (UML) class diagrams are extracted as inter-class context and we use a Multi-Relational Graph Neural Network (MR-GNN) to encode the class relational embeddings. Class lexical embeddings and class relational embeddings, together with the outputs from code token encoder and AST encoder, are passed to the decoder armed with a two-level attention mechanism to generate high-quality context-aware code summaries. We conduct extensive experiments to evaluate our approach and compare it with other automatic code summarization models. The experimental results show that CoCoGUM outperforms state-of-the-art methods.
