---
layout: publication
title: "Topical: Learning Repository Embeddings from Source Code using Attention"
authors: Agathe Lherondelle, Yash Satsangi, Fran Silavong, Shaltiel Eloul, Sean Moran
conference: Arxiv
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/pdf/2208.09495.pdf"}
tags: ["representation", "topic modelling"]
---
Machine learning on source code (MLOnCode) promises to transform how software is delivered. By mining the context and relationship between software artefacts, MLOnCode
augments the software developer’s capabilities with code autogeneration, code recommendation, code auto-tagging and other data-driven enhancements. For many of these tasks a script level
representation of code is sufficient, however, in many cases a repository level representation that takes into account various dependencies and repository structure is imperative, for example,
auto-tagging repositories with topics or auto-documentation of repository code etc. Existing methods for computing repository level representations suffer from (a) reliance on natural language
documentation of code (for example, README files) (b) naive aggregation of method/script-level representation, for example, by concatenation or averaging. This paper introduces Topical a
deep neural network to generate repository level embeddings of publicly available GitHub code repositories directly from source code. Topical incorporates an attention mechanism that projects the source code, the full dependency graph and the
script level textual information into a dense repository-level representation. To compute the repository-level representations, Topical is trained to predict the topics associated with a repository, on a dataset of publicly available GitHub repositories that
were crawled along with their ground truth topic tags. Our experiments show that the embeddings computed by Topical are able to outperform multiple baselines, including baselines
that naively combine the method-level representations through averaging or concatenation at the task of repository auto-tagging. Furthermore, we show that Topical’s attention mechanism outperforms naive aggregation methods when computing repositorylevel representations from script-level representation generated
by existing methods. Topical is a lightweight framework for computing repository-level representation of code repositories that scales efficiently with the number of topics and dataset size.
