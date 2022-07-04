---
layout: publication
title: "Learning code summarization from a small and local dataset"
authors: Toufique Ahmed, Premkumar Devanbu
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2206.00804"}
tags: ["Transformer", "summarization"]
---
Foundation models (e.g., CodeBERT, GraphCodeBERT, CodeT5) work well for many software engineering tasks. These models are pre-trained (using self-supervision) with billions of code tokens, and then fine-tuned with hundreds of thousands of labeled examples, typically drawn from many projects. However, software phenomena can be very project-specific. Vocabulary, and other phenomena vary substantially with each project. Thus, training on project-specific data, and testing on the same project, is a promising idea. This hypothesis has to be evaluated carefully, e.g., in a time-series setting, to prevent training-test leakage. We compare several models and training approaches, including same-project training, cross-project training, training a model especially designed to be sample efficient (and thus prima facie well-suited for learning in a limited-sample same-project setting) and a maximalist hybrid approach, fine-tuning first on many projects in many languages and then training on the same-project. We find that the maximalist hybrid setting provides consistent, substantial gains over the state-of-the-art, on many different projects in both Java and Python.
