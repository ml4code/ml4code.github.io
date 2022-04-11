---
layout: publication
title: "Learning Scalable and Precise Representation of Program Semantics"
authors: Ke Wang
conference:
year: 2019
tags: ["representation", "dynamic"]
---
Neural program embedding has shown potential in aiding the analysis of large-scale, complicated software. Newly proposed deep neural architectures pride themselves on learning program semantics rather than superficial syntactic features. However, by considering the source code only, the vast majority of neural networks do not capture a deep, precise representation of program semantics. In this paper, we present \dypro, a novel deep neural network that learns from program execution traces. Compared to the prior dynamic models, not only is \dypro capable of generalizing across multiple executions for learning a program's dynamic semantics in its entirety, but \dypro is also more efficient when dealing with programs yielding long execution traces. For evaluation, we task \dypro with semantic classification (i.e. categorizing programs based on their semantics) and compared it against two prominent static models: Gated Graph Neural Network and TreeLSTM. We find that \dypro achieves the highest prediction accuracy among all models. To further reveal the capacity of all aforementioned deep neural architectures, we examine if the models can learn to detect deeper semantic properties of a program. In particular given a task of recognizing loop invariants, we show \dypro beats all static models by a wide margin. 
