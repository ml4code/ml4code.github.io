---
layout: publication
title: "Learning Program Semantics with Code Representations: An Empirical Study"
authors: Jing Kai Siow, Shangqing Liu, Xiaofei Xie, Guozhu Meng, Yang Liu
conference: SANER
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2203.11790"}
tags: ["representation"]
---
Program semantics learning is the core and fundamental for various code intelligent tasks e.g., vulnerability detection, clone detection. A considerable amount of existing works propose diverse approaches to learn the program semantics for different tasks and these works have achieved state-of-the-art performance. However, currently, a comprehensive and systematic study on evaluating different program representation techniques across diverse tasks is still missed.

From this starting point, in this paper, we conduct an empirical study to evaluate different program representation techniques. Specifically, we categorize current mainstream code representation techniques into four categories i.e., Feature-based, Sequence-based, Tree-based, and Graph-based program representation technique and evaluate its performance on three diverse and popular code intelligent tasks i.e., {Code Classification}, Vulnerability Detection, and Clone Detection on the public released benchmark. We further design three {research questions (RQs)} and conduct a comprehensive analysis to investigate the performance. By the extensive experimental results, we conclude that (1) The graph-based representation is superior to the other selected techniques across these tasks. (2) Compared with the node type information used in tree-based and graph-based representations, the node textual information is more critical to learning the program semantics. (3) Different tasks require the task-specific semantics to achieve their highest performance, however combining various program semantics from different dimensions such as control dependency, data dependency can still produce promising results. 
