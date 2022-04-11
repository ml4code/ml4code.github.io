---
layout: publication
title: "CoSQA: 20,000+ Web Queries for Code Search and Question Answering"
authors: Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan
conference: ACL
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.13239"}
   - {name: "Code", url: "https://github.com/Jun-jie-Huang/CoCLR"}
tags: ["dataset", "search"]
---
Finding codes given natural language query is beneficial to the productivity of software developers.
Future progress towards better semantic matching between query and code requires richer supervised training resources.
To remedy this, we introduce the CoSQA dataset. It includes 20,604 labels for pairs of natural language queries and codes,
each annotated by at least 3 human annotators. We further introduce a contrastive learning method dubbed CoCLR to enhance query-code matching, which works as a data augmenter to bring more artificially generated training instances. We show that evaluated on CodeXGLUE with the same CodeBERT model, training on CoSQA improves the accuracy of code question answering by 5.1%, and incorporating CoCLR brings a further improvement of 10.5%. 
