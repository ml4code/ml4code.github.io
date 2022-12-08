---
layout: publication
title: Exploring Representation-Level Augmentation for Code Search
authors: Haochen Li, Chunyan Miao, Cyril Leung, Yanxian Huang, Yuan Huang, Hongyu Zhang, Yanlin Wang
conference: EMNLP
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2210.12285"}
   - {name: "code", url: "https://github.com/Alex-HaochenLi/RACS"}
tags: ["search", "Transformer"]
---
Code search, which aims at retrieving the most relevant code fragment for a given natural language query, is a common activity in software development practice. Recently, contrastive learning is widely used in code search research, where many data augmentation approaches for source code (e.g., semantic-preserving program transformation) are proposed to learn better representations.  However, these augmentations are at the raw-data level, which requires additional code analysis in the preprocessing stage and additional training costs in the training stage. In this paper, we explore augmentation methods that augment data (both code and query) at representation level which does not require additional data processing and training, and based on this we propose a general format of representation-level augmentation that unifies existing methods. Then, we propose three new augmentation methods (linear extrapolation, binary interpolation, and Gaussian scaling) based on the general format. Furthermore, we theoretically analyze the advantages of the proposed augmentation methods over traditional contrastive learning methods on code search. We experimentally evaluate the proposed representation-level augmentation methods with state-of-the-art code search models on a large-scale public dataset consisting of six programming languages. The experimental results show that our approach can consistently boost the performance of the studied code search models.