---
layout: publication
title: "Compiler-based graph representations for deep learning models of code"
authors: Alexander Brauckmann, Andres Goens, Sebastian Ertel, Jeronimo Castrillon
conference: CC
year: 2020
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/doi/abs/10.1145/3377555.3377894"}
tags: ["representation", "compilation", "optimization", "GNN"]
---
In natural language processing, novel methods in deep learning, like recurrent neural networks (RNNs) on sequences of words, have been very successful. These methods have also been used recently for tasks in compiler optimization, like heterogeneous mapping of OpenCL kernels or predicting thread coarsening factors for optimal execution times. In contrast to natural languages, programming languages usually have a well-defined structure. This structure is what enables compilers to reason about programs on the foundations of graphs, such as abstract syntax trees (ASTs) or control-data flow graphs (CDFGs).
In this paper, we argue that we should use these graph structures instead of word sequences for learning compiler optimization tasks. To this end we apply recently proposed graph neural networks (GNNs) for learning predictive compiler tasks on two representations based on ASTs and CDFGs. Experimental results show how these representations improve upon the accuracy of the state-of-the-art in the task of heterogeneous OpenCL mapping, while providing orders of magnitude faster inference times, which are crucial for compiler optimizations. When testing on benchmark suites not included for training, our graph-based methods significantly outperform the state-of-the art by 12 percentage points in terms of accuracy, and are the only ones to perform better than a random mapping. When testing on the task of predicting thread coarsening factors, we expose current limitations of deep learning in compilers. We show how all of the deep learning approaches proposed so far, including our graph-based models, fail to produce an overall speedup with their predictions.
