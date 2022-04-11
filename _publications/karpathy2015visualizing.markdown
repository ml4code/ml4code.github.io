---
layout: publication
title: "Visualizing and Understanding Recurrent Networks"
authors: Andrej Karpathy, Justin Johnson, Li Fei-Fei
conference:
year: 2015
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1506.02078"}
tags: ["language model", "code generation"]
---
Recurrent Neural Networks (RNNs), and specifically a variant with Long Short-Term Memory (LSTM), are enjoying renewed interest as a result of successful
applications in a wide range of machine learning problems that involve sequential
data. However, while LSTMs provide exceptional results in practice, the source
of their performance and their limitations remain rather poorly understood. Using character-level language models as an interpretable testbed, we aim to bridge
this gap by providing an analysis of their representations, predictions and error
types. In particular, our experiments reveal the existence of interpretable cells that
keep track of long-range dependencies such as line lengths, quotes and brackets.
Moreover, our comparative analysis with finite horizon n-gram models traces the
source of the LSTM improvements to long-range structural dependencies. Finally,
we provide analysis of the remaining errors and suggests areas for further study.


