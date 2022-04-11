---
layout: publication
title: "Unsupervised Learning of General-Purpose Embeddings for Code Changes"
authors: Mikhail Pravilov, Egor Bogomolov, Yaroslav Golubev, Timofey Bryksin
conference: 
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.02087"}
tags: ["edit", "representation"]
---
Applying machine learning to tasks that operate with code changes requires their numerical representation. In this work, we propose an approach for obtaining such representations during pre-training and evaluate them on two different downstream tasks - applying changes to code and commit message generation. During pre-training, the model learns to apply the given code change in a correct way. This task requires only code changes themselves, which makes it unsupervised. In the task of applying code changes, our model outperforms baseline models by 5.9 percentage points in accuracy. As for the commit message generation, our model demonstrated the same results as supervised models trained for this specific task, which indicates that it can encode code changes well and can be improved in the future by pre-training on a larger dataset of easily gathered code changes. 
