---
layout: publication
title: "Model-Agnostic Syntactical Information for Pre-Trained Programming Language Models"
authors: Iman Saberi, Fateme H. Fard
conference: MSR
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2303.06233"}
tags: ["Transformer", "repair", "summarization"]
---
Pre-trained Programming Language Models (PPLMs) achieved many recent states of the art results for many code-related software engineering tasks. Though some studies use data flow or propose tree-based models that utilize Abstract Syntax Tree (AST), most PPLMs do not fully utilize the rich syntactical information in source code. Still, the input is considered a sequence of tokens. There are two issues; the first is computational inefficiency due to the quadratic relationship between input length and attention complexity. Second, any syntactical information, when needed as an extra input to the current PPLMs, requires the model to be pre-trained from scratch, wasting all the computational resources already used for pre-training the current models. In this work, we propose Named Entity Recognition (NER) adapters, lightweight modules that can be inserted into Transformer blocks to learn type information extracted from the AST. These adapters can be used with current PPLMs such as CodeBERT, GraphCodeBERT, and CodeT5. We train the NER adapters using a novel Token Type Classification objective function (TTC). We insert our proposed work in CodeBERT, building CodeBERTER, and evaluate the performance on two tasks of code refinement and code summarization. CodeBERTER improves the accuracy of code refinement from 16.4 to 17.8 while using 20% of training parameter budget compared to the fully fine-tuning approach, and the BLEU score of code summarization from 14.75 to 15.90 while reducing 77% of training parameters compared to the fully fine-tuning approach.
