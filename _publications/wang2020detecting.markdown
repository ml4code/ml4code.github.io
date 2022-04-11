---
layout: publication
title: Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree
authors: Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin
conference: IEEE International Conference on Software Analysis, Evolution, and Reengineering
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2002.08653"}
tags: ["clone", "GNN"]
---

Code clones are semantically similar code fragments pairs that are syntactically similar or different. Detection of code clones can help to reduce the cost of software maintenance and prevent bugs. Numerous approaches of detecting code clones have been proposed previously, but most of them focus on detecting syntactic clones and do not work well on semantic clones with different syntactic features. To detect semantic clones, researchers have tried to adopt deep learning for code clone detection to automatically learn latent semantic features from data. Especially, to leverage grammar information, several approaches used abstract syntax trees (AST) as input and achieved significant progress on code clone benchmarks in various programming languages. However, these AST-based approaches still can not fully leverage the structural information of code fragments, especially semantic information such as control flow and data flow. To leverage control and data flow information, in this paper, we build a graph representation of programs called flow-augmented abstract syntax tree (FA-AST). We construct FA-AST by augmenting original ASTs with explicit control and data flow edges. Then we apply two different types of graph neural networks (GNN) on FA-AST to measure the similarity of code pairs. As far as we have concerned, we are the first to apply graph neural networks on the domain of code clone detection. We apply our FA-AST and graph neural networks on two Java datasets: Google Code Jam and BigCloneBench. Our approach outperforms the state-of-the-art approaches on both Google Code Jam and BigCloneBench tasks.
