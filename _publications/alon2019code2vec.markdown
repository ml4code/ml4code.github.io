---
layout: publication
title: "code2vec: Learning Distributed Representations of Code"
authors: Uri Alon, Omer Levy, Eran Yahav
conference: POPL
year: 2019
additional_links:
   - {name: "Code", url: "https://github.com/tech-srl/code2vec"}
tags: ["naming", "summarization", "representation"]
---
We present a neural model for representing snippets of code as continuous distributed vectors ("code embeddings").
 The main idea is to represent a code snippet as a single fixed-length
code vector, which can be used to
predict semantic properties of the snippet. To this end, code is first decomposed to a collection of paths in its
abstract syntax tree. Then, the network learns the atomic representation of each path while
simultaneously
learning how to aggregate a set of them.

We demonstrate the effectiveness of our approach by using it to predict a method’s name from the vector
representation of its body. We evaluate our approach by training a model on a dataset of 12M methods. We
show that code vectors trained on this dataset can predict method names from files that were unobserved
during training. Furthermore, we show that our model learns useful method name vectors that capture
semantic similarities, combinations, and analogies.

A comparison of our approach to previous techniques over the same dataset shows an improvement of
more than 75%, making it the first to successfully predict method names based on a large, cross-project
corpus. Our trained model, visualizations and vector similarities are available as an interactive online demo at
http://code2vec.org. The code, data and trained models are available at
https://github.com/tech-srl/code2vec.
