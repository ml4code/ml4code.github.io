---
layout: publication
title: "RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation"
authors: Fengji Zhang, Bei Chen, Yue Zhang, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, Weizhu Chen
conference:
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2303.12570"}
   - {name: "Code", url: "https://github.com/microsoft/CodeT/tree/main/RepoCoder"}
tags: ["completion", "Transformer", "retrieval"]
---
The task of repository-level code completion is to continue writing the unfinished code based on a broader context of the repository. While for automated code completion tools, it is difficult to utilize the useful information scattered in different files. We propose RepoCoder, a simple, generic, and effective framework to address the challenge. It streamlines the repository-level code completion process by incorporating a similarity-based retriever and a pre-trained code language model, which allows for the effective utilization of repository-level information for code completion and grants the ability to generate code at various levels of granularity. Furthermore, RepoCoder utilizes a novel iterative retrieval-generation paradigm that bridges the gap between retrieval context and the intended completion target. We also propose a new benchmark RepoEval, which consists of the latest and high-quality real-world repositories covering line, API invocation, and function body completion scenarios. We test the performance of RepoCoder by using various combinations of code retrievers and generators. Experimental results indicate that RepoCoder significantly improves the zero-shot code completion baseline by over 10% in all settings and consistently outperforms the vanilla retrieval-augmented code completion approach. Furthermore, we validate the effectiveness of RepoCoder through comprehensive analysis, providing valuable insights for future research. 
