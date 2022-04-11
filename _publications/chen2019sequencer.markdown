---
layout: publication
title: "SequenceR: Sequence-to-Sequence Learning for End-to-End Program Repair"
authors: Zimin Chen, Steve Kommrusch, Michele Tufano, Louis-Noël Pouchet, Denys Poshyvanyk, Martin Monperrus
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1901.01808"}
tags: ["repair", "code generation"]
---
This paper presents a novel end-to-end approach to program repair based on sequence-to-sequence learning. We devise, implement, and evaluate a system, called SequenceR, for fixing bugs based on sequence-to-sequence learning on source code. This approach uses the copy mechanism to overcome the unlimited vocabulary problem that occurs with big code. Our system is data-driven; we train it on 35,578 commits, carefully curated from open-source repositories. We evaluate it on 4,711 independent real bug fixes, as well on the Defects4J benchmark used in program repair research. SequenceR is able to perfectly predict the fixed line for 950/4711 testing samples. It captures a wide range of repair operators without any domain-specific top-down design.
