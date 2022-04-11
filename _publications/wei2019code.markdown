---
layout: publication
title: "Code Generation as a Dual Task of Code Summarization"
authors: Bolin Wei, Ge Li, Xin Xia, Zhiyi Fu, Zhi Jin
conference: NeurIPS
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.05923"}
tags: ["code generation", "summarization"]
---
Code summarization (CS) and code generation (CG) are two crucial tasks in the field of automatic software development. Various neural network-based approaches are proposed to solve these two tasks separately. However, there exists a specific intuitive correlation between CS and CG, which have not been exploited in previous work. In this paper, we apply the relations between two tasks to improve the performance of both tasks. In other words, exploiting the duality between the two tasks, we propose a dual training framework to train the two tasks simultaneously. In this framework, we consider the dualities on probability and attention weights, and design corresponding regularization terms to constrain the duality. We evaluate our approach on two datasets collected from GitHub, and experimental results show that our dual framework can improve the performance of CS and CG tasks over baselines. 
