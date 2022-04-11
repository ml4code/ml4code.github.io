---
layout: publication
title: "Learning Semantic Program Embeddings with Graph Interval Neural Network"
authors: Yu Wang, Fengjuan Gao, Linzhang Wang, Ke Wang
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.09997"}
tags: ["GNN", "defect"]
---
Learning distributed representations of source code has been a challenging task for machine learning models. Earlier works treated programs as text so that natural language methods can be readily applied. Unfortunately, such approaches do not capitalize on the rich structural information possessed by source code. Of late, Graph Neural Network (GNN) was proposed to learn embeddings of programs from their graph representations. Due to the homogeneous and expensive message-passing procedure, GNN can suffer from precision issues, especially when dealing with programs rendered into large graphs. In this paper, we present a new graph neural architecture, called Graph Interval Neural Network (GINN), to tackle the weaknesses of the existing GNN. Unlike the standard GNN, GINN generalizes from a curated graph representation obtained through an abstraction method designed to aid models to learn. In particular, GINN focuses exclusively on intervals for mining the feature representation of a program, furthermore, GINN operates on a hierarchy of intervals for scaling the learning to large graphs. We evaluate GINN for two popular downstream applications: variable misuse prediction and method name prediction. Results show in both cases GINN outperforms the state-of-the-art models by a comfortable margin. We have also created a neural bug detector based on GINN to catch null pointer deference bugs in Java code. While learning from the same 9,000 methods extracted from 64 projects, GINN-based bug detector significantly outperforms GNN-based bug detector on 13 unseen test projects. Next, we deploy our trained GINN-based bug detector and Facebook Infer to scan the codebase of 20 highly starred projects on GitHub. Through our manual inspection, we confirm 38 bugs out of 102 warnings raised by GINN-based bug detector compared to 34 bugs out of 129 warnings for Facebook Infer. 
