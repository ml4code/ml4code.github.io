---
layout: publication
title: "funcGNN: A Graph Neural Network Approach to Program Similarity"
authors: Aravind Nair, Avijit Roy, Karl Meinke
conference: ESEM 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2007.13239"}
tags: ["GNN", "clone"]
---
Program similarity is a fundamental concept, central to the solution of software engineering tasks such as software plagiarism, clone identification, code refactoring and code search. Accurate similarity estimation between programs requires an in-depth understanding of their structure, semantics and flow. A control flow graph (CFG), is a graphical representation of a program which captures its logical control flow and hence its semantics. A common approach is to estimate program similarity by analysing CFGs using graph similarity measures, e.g. graph edit distance (GED). However, graph edit distance is an NP-hard problem and computationally expensive, making the application of graph similarity techniques to complex software programs impractical. This study intends to examine the effectiveness of graph neural networks to estimate program similarity, by analysing the associated control flow graphs. We introduce funcGNN, which is a graph neural network trained on labeled CFG pairs to predict the GED between unseen program pairs by utilizing an effective embedding vector. To our knowledge, this is the first time graph neural networks have been applied on labeled CFGs for estimating the similarity between high-level language programs. Results: We demonstrate the effectiveness of funcGNN to estimate the GED between programs and our experimental analysis demonstrates how it achieves a lower error rate (0.00194), with faster (23 times faster than the quickest traditional GED approximation method) and better scalability compared with the state of the art methods. funcGNN posses the inductive learning ability to infer program structure and generalise to unseen programs. The graph embedding of a program proposed by our methodology could be applied to several related software engineering problems (such as code plagiarism and clone identification) thus opening multiple research directions. 
