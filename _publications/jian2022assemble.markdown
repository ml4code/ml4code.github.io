---
layout: publication
title: Assemble Foundation Models for Automatic Code Summarization
authors: Jian Gu, Pasquale Salza, Harald C. Gall
conference: SANER
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2201.05222"}
   - {name: "code", url: "https://github.com/jianguda/afm4acs"}
tags: ["summarization", "documentation", "language model"]
---
Automatic code summarization is beneficial to software development and maintenance since it reduces the burden of manual tasks. Currently, artificial intelligence is undergoing a paradigm shift. The foundation models pretrained on massive data and finetuned to downstream tasks surpass specially customized models. This trend inspired us to consider reusing foundation models instead of learning from scratch. Based on this, we propose a flexible and robust approach for automatic code summarization based on neural networks. We assemble available foundation models, such as CodeBERT and GPT-2, into a single model named AdaMo. Moreover, we utilize Gaussian noise as the simulation of contextual information to optimize the latent representation. Furthermore, we introduce two adaptive schemes from the perspective of knowledge transfer, namely continuous pretraining and intermediate finetuning, and design intermediate stage tasks for general sequence-to-sequence learning. Finally, we evaluate AdaMo against a benchmark dataset for code summarization, by comparing it with state-of-the-art models.
