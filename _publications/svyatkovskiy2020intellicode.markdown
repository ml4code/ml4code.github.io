---
layout: publication
title: "IntelliCode Compose: Code Generation Using Transformer"
authors: Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu, Neel Sundaresan
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.08025"}
tags: ["autocomplete", "code generation", "synthesis", "language model", "pretraining"]
---
In software development through integrated development environments (IDEs), code completion is one of the most widely used features. Nevertheless, majority of integrated development environments only support completion of methods and APIs, or arguments.
In this paper, we introduce IntelliCode Compose − a general-purpose multilingual code completion tool which is capable of predicting sequences of code tokens of arbitrary types, generating up to entire lines of syntactically correct code. It leverages state-of-the-art generative transformer model trained on 1.2 billion lines of source code in Python, C#, JavaScript and TypeScript programming languages. IntelliCode Compose is deployed as a cloud-based web service. It makes use of client-side tree-based caching, efficient parallel implementation of the beam search decoder, and compute graph optimizations to meet edit-time completion suggestion requirements in the Visual Studio Code IDE and Azure Notebook.
Our best model yields an average edit similarity of 86.7% and a perplexity of 1.82 for Python programming language.
