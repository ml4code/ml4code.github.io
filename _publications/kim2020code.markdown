---
layout: publication
title: "Code Prediction by Feeding Trees to Transformers"
authors: Seohyun Kim, Jinman Zhao, Yuchi Tian, Satish Chandra
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2003.13848"}
   - {name: "Code", url: "https://github.com/facebookresearch/code-prediction-transformer"}
tags: ["autocomplete"]
---
In this paper, we describe how to leverage Transformer, a recent neural architecture for learning from sequential data (such as text), for code completion. As in the realm of natural language processing, Transformers surpass the prediction accuracy achievable by RNNs; we provide an experimental confirmation of this over a Python dataset.

Furthermore, we show that the way to obtain even better accuracy from Transformers is to expose the syntactic structure of code, which is easily recovered by parsing, to the neural network. This works significantly better than presenting the code as a linear token sequence, which is how Transformers were originally intended to be used.

To accomplish this, we propose a novel enhancement to the self-attention mechanism of the Transformer. We enable the mechanism to learn weights---that is, how much to focus on each preceding token in the input---not only on the basis of a token's value, but also on the basis of the spatial relationships, as in their positions in the abstract syntax tree, between each pair of tokens.

We provide comprehensive experimental evaluation of our proposal, along with alternative design choices, on a standard Python dataset, as well as on a Python corpus internal to Facebook. 
