---
layout: publication
title: "Summarizing Source Code using a Neural Attention Model"
authors: Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, Luke Zettlemoyer
conference: ACL
year: 2016
tags: ["summarization", "bimodal"]
---
High quality source code is often paired
with high level summaries of the computation it performs, for example in code
documentation or in descriptions posted
in online forums. Such summaries are
extremely useful for applications such as
code search but are expensive to manually
author, hence only done for a small fraction of all code that is produced. In this
paper, we present the first completely data-driven approach for generating high level
summaries of source code. Our model,
CODE-NN , uses Long Short Term Memory (LSTM) networks with attention to
produce sentences that describe C# code
snippets and SQL queries. CODE-NN
is trained on a new corpus that is automatically collected from StackOverflow,
which we release. Experiments demonstrate strong performance on two tasks:
(1) code summarization, where we establish the first end-to-end learning results
and outperform strong baselines, and (2)
code retrieval, where our learned model
improves the state of the art on a recently
introduced C# benchmark by a large margin.
