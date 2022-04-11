---
layout: publication
title: "Towards Learning Representations of Binary Executable Files for Security Tasks"
authors: Shushan Arakelyan, Sima Arasteh, Christophe Hauser, Erik Kline, Aram Galstyan
conference: AAAI
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2002.03388"}
tags: ["GNN", "representation"]
---
Tackling binary analysis problems has traditionally implied manually defining rules and heuristics. As an alternative, we are suggesting using machine learning models for learning distributed representations of binaries that can be applicable for a number of downstream tasks. We construct a computational graph from the binary executable and use it with a graph convolutional neural network to learn a high dimensional representation of the program. We show the versatility of this approach by using our representations to solve two semantically different binary analysis tasks -- algorithm classification and vulnerability discovery. We compare the proposed approach to our own strong baseline as well as published results and demonstrate improvement on the state of the art methods for both tasks. 
