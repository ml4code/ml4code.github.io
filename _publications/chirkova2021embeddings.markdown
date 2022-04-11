---
layout: publication
title: "On the Embeddings of Variables in Recurrent Neural Networks for Source Code"
authors: Nadezhda Chirkova
conference: NAACL
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2010.12693"}
   - {name: "Code", url: "https://github.com/nadiinchi/dynamic_embeddings"}
tags: ["autocomplete"]
---
Source code processing heavily relies on the methods widely used in natural language processing (NLP), but involves specifics that need to be taken into account to achieve higher quality. An example of this specificity is that the semantics of a variable is defined not only by its name but also by the contexts in which the variable occurs. In this work, we develop dynamic embeddings, a recurrent mechanism that adjusts the learned semantics of the variable when it obtains more information about the variable’s role in the program. We show that using the proposed dynamic embeddings significantly improves the performance of the recurrent neural network, in code completion and bug fixing tasks. 
