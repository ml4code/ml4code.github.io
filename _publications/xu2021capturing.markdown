---
layout: publication
title: "Capturing Structural Locality in Non-parametric Language Models"
authors: Frank F. Xu, Junxian He, Graham Neubig, Vincent J. Hellendoorn
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2110.02870"}
tags: ["language model"]
---
Structural locality is a ubiquitous feature of real-world datasets, wherein data points are organized into local hierarchies. Some examples include topical clusters in text or project hierarchies in source code repositories. In this paper, we explore utilizing this structural locality within non-parametric language models, which generate sequences that reference retrieved examples from an external source. We propose a simple yet effective approach for adding locality information into such models by adding learned parameters that improve the likelihood of retrieving examples from local neighborhoods. Experiments on two different domains, Java source code and Wikipedia text, demonstrate that locality features improve model efficacy over models without access to these features, with interesting differences. We also perform an analysis of how and where locality features contribute to improved performance and why the traditionally used contextual similarity metrics alone are not enough to grasp the locality structure. 
