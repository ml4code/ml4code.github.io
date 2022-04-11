---
layout: publication
title: "Using GGNN to recommend log statement level"
authors: Mingzhe Li, Jianrui Pei, Jin He, Kevin Song, Frank Che, Yongfeng Huang, Chitai Wang
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1912.05097"}
tags: ["GNN", "logging"]
---
In software engineering, log statement is an important part because programmers can't access to users' program and they can only rely on log message to find the root of bugs. The mechanism of "log level" allows developers and users to specify the appropriate amount of logs to print during the execution of the software. And 26\% of the log statement modification is to modify the level. We tried to use ML method to predict the suitable level of log statement. The specific model is GGNN(gated graph neural network) and we have drawn lessons from Microsoft's research. In this work, we apply Graph Neural Networks to predict the usage of log statement level of some open source java projects from github. Given the good performance of GGNN in this task, we are confident that GGNN is an excellent choice for processing source code. We envision this model can play an important role in applying AI/ML technique for Software Development Life Cycle more broadly.
