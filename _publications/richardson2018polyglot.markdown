---
layout: publication
title: "Polyglot Semantic Parsing in APIs"
authors: Kyle Richardson, Jonathan Berant, Jonas Kuhn
conference: NAACL
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1803.06966"}
tags: ["bimodal", "API"]
---
Traditional approaches to semantic parsing (SP) work by training individual models for each available parallel dataset of text-meaning pairs. In this paper, we explore the idea of polyglot semantic translation, or learning semantic parsing models that are trained on multiple datasets and natural languages. In particular, we focus on translating text to code signature representations using the software component datasets of Richardson and Kuhn (2017a,b). The advantage of such models is that they can be used for parsing a wide variety of input natural languages and output programming languages, or mixed input languages, using a single unified model. To facilitate modeling of this type, we develop a novel graph-based decoding framework that achieves state-of-the-art performance on the above datasets, and apply this method to two other benchmark SP tasks.
