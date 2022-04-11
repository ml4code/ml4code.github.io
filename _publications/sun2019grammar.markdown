---
layout: publication
title: "A Grammar-Based Structural CNN Decoder for Code Generation"
authors: Zeyu Sun, Qihao Zhu, Lili Mou, Yingfei Xiong, Ge Li, Lu Zhang
conference: AAAI
year: 2019
tags: ["code generation", "grammar"]
---
Code  generation  maps  a  program  description  to  executable
source code in a programming language. Existing approaches
mainly rely on a recurrent neural network (RNN) as the decoder. However, we find that a program contains significantly
more tokens than a natural language sentence, and thus it may
be inappropriate for RNN to capture such a long sequence. In
this paper, we propose a grammar-based structural convolutional neural network (CNN) for code generation. Our model
generates a program by predicting the grammar rules of the
programming language; we design several CNN modules, including the tree-based convolution and pre-order convolution,
whose information is further aggregated by dedicated attentive pooling layers. Experimental results on the HearthStone
benchmark dataset show that our CNN code generator significantly outperforms the previous state-of-the-art method by 5
percentage points; additional experiments on several semantic parsing tasks demonstrate the robustness of our model. We
also conduct in-depth ablation test to better understand each
component of our model.
