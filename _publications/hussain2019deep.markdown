---
layout: publication
title: "Deep Transfer Learning for Source Code Modeling"
authors: Yasir Hussain, Zhiqiu Huang, Yu Zhou, Senzhang Wang
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.05493"}
tags: ["pretraining"]
---
In recent years, deep learning models have shown great potential in source code modeling and analysis. Generally, deep learning-based approaches are problem-specific and data-hungry. A challenging issue of these approaches is that they require training from starch for a different related problem. In this work, we propose a transfer learning-based approach that significantly improves the performance of deep learning-based source code models. In contrast to traditional learning paradigms, transfer learning can transfer the knowledge learned in solving one problem into another related problem. First, we present two recurrent neural network-based models RNN and GRU for the purpose of transfer learning in the domain of source code modeling. Next, via transfer learning, these pre-trained (RNN and GRU) models are used as feature extractors. Then, these extracted features are combined into attention learner for different downstream tasks. The attention learner leverages from the learned knowledge of pre-trained models and fine-tunes them for a specific downstream task. We evaluate the performance of the proposed approach with extensive experiments with the source code suggestion task. The results indicate that the proposed approach outperforms the state-of-the-art models in terms of accuracy, precision, recall, and F-measure without training the models from scratch.
