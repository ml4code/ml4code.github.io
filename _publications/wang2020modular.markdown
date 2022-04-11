---
layout: publication
title: "Modular Tree Network for Source Code Representation Learning"
authors: Wenhan Wang, Ge Li, Sijie Shen, Xin Xia, Zhi Jin
conference: TOSEM
year: 2020
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/doi/10.1145/3409331"}
tags: ["grammar", "representation"]
---
Learning representation for source code is a foundation of many program analysis tasks. In recent years, neural networks have already shown success in this area, but most existing models did not make full use of the unique structural information of programs. Although abstract syntax tree (AST)-based neural models can handle the tree structure in the source code, they cannot capture the richness of different types of substructure in programs. In this article, we propose a modular tree network that dynamically composes different neural network units into tree structures based on the input AST. Different from previous tree-structural neural network models, a modular tree network can capture the semantic differences between types of AST substructures. We evaluate our model on two tasks: program classification and code clone detection. Our model achieves the best performance compared with state-of-the-art approaches in both tasks, showing the advantage of leveraging more elaborate structure information of the source code.
