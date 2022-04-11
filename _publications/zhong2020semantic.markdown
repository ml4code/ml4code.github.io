---
layout: publication
title: "Semantic Scaffolds for Pseudocode-to-Code Generation"
authors: Ruiqi Zhong, Mitchell Stern, Dan Klein
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.05927"}
tags: ["code generation", "synthesis"]
---
We propose a method for program generation based on semantic scaffolds, lightweight structures representing the high-level semantic and syntactic composition of a program. By first searching over plausible scaffolds then using these as constraints for a beam search over programs, we achieve better coverage of the search space when compared with existing techniques. We apply our hierarchical search method to the SPoC dataset for pseudocode-to-code generation, in which we are given line-level natural language pseudocode annotations and aim to produce a program satisfying execution-based test cases. By using semantic scaffolds during inference, we achieve a 10% absolute improvement in top-100 accuracy over the previous state-of-the-art. Additionally, we require only 11 candidates to reach the top-3000 performance of the previous best approach when tested against unseen problems, demonstrating a substantial improvement in efficiency. 
