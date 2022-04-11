---
layout: publication
title: "Energy-Based Models for Code Generation under Compilability Constraints"
authors: Tomasz Korbak, Hady Elsahar, Marc Dymetman, Germán Kruszewski
conference: ACL
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.04985"}
tags: ["code generation"]
---
Neural language models can be successfully trained on source code, leading to applications such as code completion. However, their versatile autoregressive self-supervision objective overlooks important global sequence-level features that are present in the data such as syntactic correctness or compilability. In this work, we pose the problem of learning to generate compilable code as constraint satisfaction. We define an Energy-Based Model (EBM) representing a pre-trained generative model with an imposed constraint of generating only compilable sequences. We then use the KL-Adaptive Distributional Policy Gradient algorithm (Khalifa et al., 2021) to train a generative model approximating the EBM. We conduct experiments showing that our proposed approach is able to improve compilability rates without sacrificing diversity and complexity of the generated samples. 
