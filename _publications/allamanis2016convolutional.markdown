---
layout: publication
title: A Convolutional Attention Network for Extreme Summarization of Source Code
authors: Miltiadis Allamanis, Hao Peng, Charles Sutton
conference: ICML
year: 2016
additional_links:
   - {name: "website", url: "http://groups.inf.ed.ac.uk/cup/codeattention/"}
   - {name: "code", url: "https://github.com/mast-group/convolutional-attention"}
   - {name: "proceedings", url: "http://jmlr.org/proceedings/papers/v48/allamanis16.pdf"}
   - {name: "presentation video", url: "http://techtalks.tv/talks/a-convolutional-attention-network-for-extreme-summarization-of-source-code/62461/"}
   - {name: "GitXiV", url: "http://gitxiv.com/posts/A6HFFyK7CmNLaSjG7/a-convolutional-attention-network-for-extreme-summarization"}
tags: ["naming", "summarization"]
---
Attention mechanisms in neural networks have proved useful for problems in which
the input and output do not have fixed dimension. Often there exist features that
are locally translation invariant and would be valuable for directing the model’s attention,
but previous attentional architectures are not constructed to learn such features specifically.
We introduce an attentional neural network that employs convolution on the input tokens to detect
local time-invariant and long-range topical attention features in a context-dependent way. We
apply this architecture to the problem of extreme summarization of source code snippets into short,
descriptive function name-like summaries. Using those features, the model sequentially generates a
summary by marginalizing over two attention mechanisms: one that predicts the next summary token based 
n the attention weights of the input tokens and another that is able to copy a code token as-is directly
into the summary. We demonstrate our convolutional attention neural network’s performance on 10 popular Java
projects showing that it achieves better performance compared to previous attentional mechanisms.
