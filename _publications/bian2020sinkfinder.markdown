---
layout: publication
title: "SinkFinder: harvesting hundreds of unknown interesting function pairs with just one seed"
authors: Pan Bian, Bin Liang, Jianjun Huang, Wenchang Shi, Xidong Wang, Jian Zhang
conference: FSE
year: 2020
tags: ["program analysis"]
---
Mastering the knowledge about security-sensitive functions that can potentially result in bugs is valuable to detect them. However, identifying this kind of functions is not a trivial task. Introducing machine learning-based techniques to do the task is a natural choice. Unfortunately, the approach also requires considerable prior knowledge, e.g., sufficient labelled training samples. In practice, the requirement is often hard to meet.

In this paper, to solve the problem, we propose a novel and practical method called SinkFinder to automatically discover function pairs that we are interested in, which only requires very limited prior knowledge. SinkFinder first takes just one pair of well-known interesting functions as the initial seed to infer enough positive and negative training samples by means of sub-word word embedding. By using these samples, a support vector machine classifier is trained to identify more interesting function pairs. Finally, checkers equipped with the obtained knowledge can be easily developed to detect bugs in target systems. The experiments demonstrate that SinkFinder can successfully discover hundreds of interesting functions and detect dozens of previously unknown bugs from large-scale systems, such as Linux, OpenSSL and PostgreSQL.
