---
layout: publication
title: "Modeling Functional Similarity in Source Code with Graph-Based Siamese Networks"
authors: Nikita Mehrotra, Navdha Agarwal, Piyush Gupta, Saket Anand, David Lo, Rahul Purandare
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2011.11228"}
tags: ["clone", "GNN"]
---
Code clones are duplicate code fragments that share (nearly) similar syntax or semantics. Code clone detection plays an important role in software maintenance, code refactoring, and reuse. A substantial amount of research has been conducted in the past to detect clones. A majority of these approaches use lexical and syntactic information to detect clones. However, only a few of them target semantic clones. Recently, motivated by the success of deep learning models in other fields, including natural language processing and computer vision, researchers have attempted to adopt deep learning techniques to detect code clones. These approaches use lexical information (tokens) and(or) syntactic structures like abstract syntax trees (ASTs) to detect code clones. However, they do not make sufficient use of the available structural and semantic information hence, limiting their capabilities.

This paper addresses the problem of semantic code clone detection using program dependency graphs and geometric neural networks, leveraging the structured syntactic and semantic information. We have developed a prototype tool HOLMES, based on our novel approach, and empirically evaluated it on popular code clone benchmarks. Our results show that HOLMES performs considerably better than the other state-of-the-art tool, TBCCD. We also evaluated HOLMES on unseen projects and performed cross dataset experiments to assess the generalizability of HOLMES. Our results affirm that HOLMES outperforms TBCCD since most of the pairs that HOLMES detected were either undetected or suboptimally reported by TBCCD. 
