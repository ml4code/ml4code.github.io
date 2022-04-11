---
layout: publication
title: "Associating Natural Language Comment and Source Code Entities"
authors: Sheena Panthaplackel, Milos Gligoric, Raymond J. Mooney, Junyi Jessy Li
conference: AAAI
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1912.06728"}
tags: ["dataset", "bimodal"]
---
Comments are an integral part of software development; they are natural language descriptions associated with source code elements. Understanding explicit associations can be useful in improving code comprehensibility and maintaining the consistency between code and comments. As an initial step towards this larger goal, we address the task of associating entities in Javadoc comments with elements in Java source code. We propose an approach for automatically extracting supervised data using revision histories of open source projects and present a manually annotated evaluation dataset for this task. We develop a binary classifier and a sequence labeling model by crafting a rich feature set which encompasses various aspects of code, comments, and the relationships between them. Experiments show that our systems outperform several baselines learning from the proposed supervision. 
