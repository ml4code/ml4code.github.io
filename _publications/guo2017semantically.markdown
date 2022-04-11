---
layout: publication
title: "Semantically enhanced software traceability using deep learning techniques"
authors: Jin Guo, Jinghui Cheng, Jane Cleland-Huang
conference: ICSE
year: 2017
tags: ["traceability", "representation"]
---
In most safety-critical domains the need for traceability is prescribed by certifying bodies. Trace links are generally created among requirements, design, source code, test cases and other artifacts; however, creating such links manually is time consuming and error prone. Automated solutions use information retrieval and machine learning techniques to generate trace links; however, current techniques fail to understand semantics of the software artifacts or to integrate domain knowledge into the tracing process and therefore tend to deliver imprecise and inaccurate results. In this paper, we present a solution that uses deep learning to incorporate requirements artifact semantics and domain knowledge into the tracing solution. We propose a tracing network architecture that utilizes Word Embedding and Recurrent Neural Network (RNN) models to generate trace links. Word embedding learns word vectors that represent knowledge of the domain corpus and RNN uses these word vectors to learn the sentence semantics of requirements artifacts. We trained 360 different configurations of the tracing network using existing trace links in the Positive Train Control domain and identified the Bidirectional Gated Recurrent Unit (BI-GRU) as the best model for the tracing task. BI-GRU significantly out-performed state-of-the-art tracing methods including the Vector Space Model and Latent Semantic Indexing.
