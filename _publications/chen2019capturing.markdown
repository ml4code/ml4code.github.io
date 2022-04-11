---
layout: publication
title: "Capturing source code semantics via tree-based convolution over API-enhanced AST"
authors: Long Chen, Wei Ye, Shikun Zhang
conference: Computing Frontiers
year: 2019
tags: ["grammar", "representation"]
---
When deep learning meets big code, a key question is how to efficiently learn a distributed representation for source code that can capture its semantics effectively. We propose to use tree-based convolution over API-enhanced AST. To demonstrate the effectiveness of our approach, we apply it to detect semantic clones---code fragments with similar semantics but dissimilar syntax. Experiment results show that our approach outperforms an existing state-of-the-art approach that uses tree-based LSTM, with an increase of 0.39 and 0.12 in F1-score on OJClone and BigCloneBench respectively. We further propose architectures that incorporate our approach for code search and code summarization.