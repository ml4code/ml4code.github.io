---
layout: publication
title: "Learning to Represent Programs with Heterogeneous Graphs"
authors: Wenhan Wang, Kechi Zhang, Ge Li, Zhi Jin
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2012.04188"}
tags: ["GNN", "summarization"]
---
Program source code contains complex structure information, which can be represented in structured data forms like trees or graphs. To acquire the structural information in source code, most existing researches use abstract syntax trees (AST). A group of works add additional edges to ASTs to convert source code into graphs and use graph neural networks to learn representations for program graphs. Although these works provide additional control or data flow information to ASTs for downstream tasks, they neglect an important aspect of structure information in AST itself: the different types of nodes and edges. In ASTs, different nodes contain different kinds of information like variables or control flow, and the relation between a node and all its children can also be different.

To address the information of node and edge types, we bring the idea of heterogeneous graphs to learning on source code and present a new formula of building heterogeneous program graphs from ASTs with additional type information for nodes and edges. We use the ASDL grammar of programming language to define the node and edge types of program graphs. Then we use heterogeneous graph neural networks to learn on these graphs. We evaluate our approach on two tasks: code comment generation and method naming. Both tasks require reasoning on the semantics of complete code snippets. Experiment results show that our approach outperforms baseline models, including homogeneous graph-based models, showing that leveraging the type information of nodes and edges in program graphs can help in learning program semantics. 
