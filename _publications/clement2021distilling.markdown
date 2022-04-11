---
layout: publication
title: "Distilling Transformers for Neural Cross-Domain Search"
authors: Colin B. Clement, Chen Wu, Dawn Drain, Neel Sundaresan
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.03322"}
tags: ["search", "Transformer"]
---
Pre-trained transformers have recently clinched top spots in the gamut of natural language tasks and pioneered solutions to software engineering tasks. Even information retrieval has not been immune to the charm of the transformer, though their large size and cost is generally a barrier to deployment. While there has been much work in streamlining, caching, and modifying transformer architectures for production, here we explore a new direction: distilling a large pre-trained translation model into a lightweight bi-encoder which can be efficiently cached and queried. We argue from a probabilistic perspective that sequence-to-sequence models are a conceptually ideal---albeit highly impractical---retriever. We derive a new distillation objective, implementing it as a data augmentation scheme. Using natural language source code search as a case study for cross-domain search, we demonstrate the validity of this idea by significantly improving upon the current leader of the CodeSearchNet challenge, a recent natural language code search benchmark. 
