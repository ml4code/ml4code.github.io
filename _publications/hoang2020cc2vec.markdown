---
layout: publication
title: "CC2Vec: Distributed Representations of Code Changes"
authors: Thong Hoang, Hong Jin Kang, Julia Lawall, David Lo
conference: ICSE
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2003.05620"}
   - {name: "code", url: "https://github.com/CC2Vec/CC2Vec"}
tags: ["edit"]
---
Existing work on software patches often use features specific to a single task. These works often rely on manually identified features, and human effort is required to identify these features for each task. In this work, we propose CC2Vec, a neural network model that learns a representation of code changes guided by their accompanying log messages, which represent the semantic intent of the code changes. CC2Vec models the hierarchical structure of a code change with the help of the attention mechanism and uses multiple comparison functions to identify the differences between the removed and added code.

To evaluate if CC2Vec can produce a distributed representation of code changes that is general and useful for multiple tasks on software patches, we use the vectors produced by CC2Vec for three tasks: log message generation, bug fixing patch identification, and just-in-time defect prediction. In all tasks, the models using CC2Vec outperform the state-of-the-art techniques.
