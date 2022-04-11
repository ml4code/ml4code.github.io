---
layout: publication
title: "Gated Graph Sequence Neural Networks"
authors: Yujia Li, Daniel Tarlow, Marc Brockschmidt, Richard Zemel
conference: ICLR
year: 2016
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1511.05493"}
tags: ["GNN", "program analysis"]
---
Graph-structured data appears frequently in domains including chemistry, natural
language semantics, social networks, and knowledge bases. In this work, we study
feature learning techniques for graph-structured inputs. Our starting point is previous work on Graph Neural Networks (Scarselli et al., 2009), which we modify
to use gated recurrent units and modern optimization techniques and then extend
to output sequences. The result is a flexible and broadly useful class of neural network models that has favorable inductive biases relative to purely sequence-based
models (e.g., LSTMs) when the problem is graph-structured. We demonstrate the
capabilities on some simple AI (bAbI) and graph algorithm learning tasks. We
then show it achieves state-of-the-art performance on a problem from program
verification, in which subgraphs need to be described as abstract data structures.

