---
layout: publication
title: Learning to Represent Programs with Graphs
authors: Miltiadis Allamanis, Marc Brockschmidt, Mahmoud Khademi
conference: "ICLR"
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1711.00740"}
   - {name: "GGNN Code", url: "https://github.com/Microsoft/gated-graph-neural-network-samples"}
   - {name: "Data", url: "https://aka.ms/iclr18-prog-graphs-dataset"}
tags: ["naming", "GNN", "representation", "variable misuse", "defect"]
---
Learning tasks on source code (i.e., formal languages) have been considered recently, but most work has tried to transfer natural language methods and does not capitalize on the unique opportunities offered by code's known syntax. For example, long-range dependencies induced by using the same variable or function in distant locations are often not considered. We propose to use graphs to represent both the syntactic and semantic structure of code and use graph-based deep learning methods to learn to reason over program structures.

In this work, we present how to construct graphs from source code and how to scale Gated Graph Neural Networks training to such large graphs. We evaluate our method on two tasks: VarNaming, in which a network attempts to predict the name of a variable given its usage, and VarMisuse, in which the network learns to reason about selecting the correct variable that should be used at a given program location. Our comparison to methods that use less structured program representations shows the advantages of modeling known structure, and suggests that our models learn to infer meaningful names and to solve the VarMisuse task in many cases. Additionally, our testing showed that VarMisuse identifies a number of bugs in mature open-source projects. 
