---
layout: publication
title: Generative Code Modeling with Graphs
authors: M. Brockscmidt, M. Allamanis A. L. Gaunt, O. Polozov
conference: "ICLR"
year: 2019
bibkey: brockschmidt2019generative
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1805.08490"}
   - {name: "OpenReview", url: "https://openreview.net/forum?id=Bke4KsA5FX"}
   - {name: "Code", url: "https://github.com/Microsoft/graph-based-code-modelling"}
tags: ["grammar", "generation", "GNN"]
---
Generative models forsource code are an interesting structured prediction problem, requiring to reason about both hard syntactic and semantic constraints as well as about natural, likely programs. We present a novel model for this problem that uses a graph to represent the intermediate state of the generated output. Our model generates code by interleaving grammar-driven expansion steps with graph augmentation and neural message passing steps. An experimental evaluation shows that our new model can generate semantically meaningful expressions, outperforming a range of strong baselines.
