---
layout: publication
title: "Neural-Network Guided Expression Transformation"
authors: Romain Edelmann, Viktor Kunčak
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1902.02194"}
tags: ["optimization", "grammar"]
---
Optimizing compilers, as well as other translator systems, often work by rewriting expressions according to equivalence preserving rules. Given an input expression and its optimized form, finding the sequence of rules that were applied is a non-trivial task. Most of the time, the tools provide no proof, of any kind, of the equivalence between the original expression and its optimized form. In this work, we propose to reconstruct proofs of equivalence of simple mathematical expressions, after the fact, by finding paths of equivalence preserving transformations between expressions. We propose to find those sequences of transformations using a search algorithm, guided by a neural network heuristic. Using a Tree-LSTM recursive neural network, we learn a distributed representation of expressions where the Manhattan distance between vectors approximately corresponds to the rewrite distance between expressions. We then show how the neural network can be efficiently used to search for transformation paths, leading to substantial gain in speed compared to an uninformed exhaustive search. In one of our experiments, our neural-network guided search algorithm is able to solve more instances with a 2 seconds timeout per instance than breadth-first search does with a 5 minutes timeout per instance.
