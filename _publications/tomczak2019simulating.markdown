---
layout: publication
title: "Simulating Execution Time of Tensor Programs using Graph Neural Networks"
authors: Jakub M. Tomczak, Romain Lepert, Auke Wiggers
conference: Representation Learning on Graphs and Manifolds at ICLR
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1904.11876"}
tags: ["GNN"]
---
Optimizing the execution time of tensor program, e.g., a convolution, involves finding its optimal configuration. Searching the configuration space exhaustively is typically infeasible in practice. In line with recent research using TVM, we propose to learn a surrogate model to overcome this issue. The model is trained on an acyclic graph called an abstract syntax tree, and utilizes a graph convolutional network to exploit structure in the graph. We claim that a learnable graph-based data processing is a strong competitor to heuristic-based feature extraction. We present a new dataset of graphs corresponding to configurations and their execution time for various tensor programs. We provide baselines for a runtime prediction task. 
