---
layout: publication
title: "Understanding Neural Code Intelligence Through Program Simplification"
authors: Md Rafiqul Islam Rabin, Vincent J. Hellendoorn, Mohammad Amin Alipour
conference: ESEC/FSE
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.03353"}
   - {name: "code", url: "https://github.com/mdrafiqulrabin/SIVAND"}
tags: ["interpretability", "refactoring", "information extraction"]
---
A wide range of code intelligence (CI) tools, powered by deep neural networks, have been developed recently to improve programming productivity and perform program analysis. To reliably use such tools, developers often need to reason about the behavior of the underlying models and the factors that affect them. This is especially challenging for tools backed by deep neural networks. Various methods have tried to reduce this opacity in the vein of "transparent/interpretable-AI". However, these approaches are often specific to a particular set of network architectures, even requiring access to the network's parameters. This makes them difficult to use for the average programmer, which hinders the reliable adoption of neural CI systems. In this paper, we propose a simple, model-agnostic approach to identify critical input features for models in CI systems, by drawing on software debugging research, specifically delta debugging. Our approach, SIVAND, uses simplification techniques that reduce the size of input programs of a CI model while preserving the predictions of the model. We show that this approach yields remarkably small outputs and is broadly applicable across many model architectures and problem domains. We find that the models in our experiments often rely heavily on just a few syntactic features in input programs. We believe that SIVAND's extracted features may help understand neural CI systems' predictions and learned behavior.
