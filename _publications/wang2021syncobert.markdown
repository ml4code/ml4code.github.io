---
layout: publication
title: "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation"
authors: Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.04556"}
tags: ["pretraining"]
---
Code representation learning, which aims to encode the semantics of source code into distributed vectors, plays an important role in recent deep-learning-based models for code intelligence. Recently, many pre-trained language models for source code (e.g., CuBERT and CodeBERT) have been proposed to model the context of code and serve as a basis for downstream code intelligence tasks such as code search, code clone detection, and program translation. Current approaches typically consider the source code as a plain sequence of tokens, or inject the structure information (e.g., AST and data-flow) into the sequential model pre-training. To further explore the properties of programming languages, this paper proposes SynCoBERT, a syntax-guided multi-modal contrastive pre-training approach for better code representations. Specially, we design two novel pre-training objectives originating from the symbolic and syntactic properties of source code, i.e., Identifier Prediction (IP) and AST Edge Prediction (TEP), which are designed to predict identifiers, and edges between two nodes of AST, respectively. Meanwhile, to exploit the complementary information in semantically equivalent modalities (i.e., code, comment, AST) of the code, we propose a multi-modal contrastive learning strategy to maximize the mutual information among different modalities. Extensive experiments on four downstream tasks related to code intelligence show that SynCoBERT advances the state-of-the-art with the same pre-training corpus and model size.