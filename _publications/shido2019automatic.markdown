---
layout: publication
title: "Automatic Source Code Summarization with Extended Tree-LSTM"
authors: Yusuke Shido, Yasuaki Kobayashi, Akihiro Yamamoto, Atsushi Miyamoto, Tadayuki Matsumura
conference: International Joint Conference on Neural Networks
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1906.08094"}
   - {name: "Dataset", url: "https://github.com/xing-hu/DeepCom"}
   - {name: "code", url: "https://github.com/sh1doy/summarization_tf"}
tags: ["summarization", "grammar"]
---
Neural machine translation models are used to automatically generate a document from given source code since this can be regarded as a machine translation task. Source code summarization is one of the components for automatic document generation, which generates a summary in natural language from given source code. This suggests that techniques used in neural machine translation, such as Long Short-Term Memory (LSTM), can be used for source code summarization. However, there is a considerable difference between source code and natural language: Source code is essentially structured, having loops and conditional branching, etc. Therefore, there is some obstacle to apply known machine translation models to source code.Abstract syntax trees (ASTs) capture these structural properties and play an important role in recent machine learning studies on source code. Tree-LSTM is proposed as a generalization of LSTMs for tree-structured data. However, there is a critical issue when applying it to ASTs: It cannot handle a tree that contains nodes having an arbitrary number of children and their order simultaneously, which ASTs generally have such nodes. To address this issue, we propose an extension of Tree-LSTM, which we call Multi-way Tree-LSTM and apply it for source code summarization. As a result of computational experiments, our proposal achieved better results when compared with several state-of-the-art techniques.
