---
layout: publication
title: "Sequence Model Design for Code Completion in the Modern IDE"
authors: Gareth Ari Aye, Gail E. Kaiser
conference: Optional
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.05249"}
tags: ["autocomplete"]
---
Code completion plays a prominent role in modern integrated development environments (IDEs). Machine learning has become ubiquitous in analogous natural language writing and search software, surfacing more relevant autocompletions and search suggestions in fewer keystrokes. Prior research has reported training high-accuracy, deep neural networks for modeling source code, but little attention has been given to the practical constraints imposed by interactive developer tools. In particular, neural language models for source code modeling like the one described in Maybe Deep Neural Networks are the Best Choice for Modeling Source Code are framed around code completion, but only report accuracy of next-token prediction. However, in order for a language model (LM) to work well within real-world code completion systems, it must also always make suggestions that produce valid code that typechecks to support code completion's role in correctness-checking; return instantaneous results to help programmers code more efficiently in fewer keystrokes; and be small enough to fit comfortably on disk and in memory on developer workstations, since virtually all modern IDEs run locally and support offline usage. To meet these additional requirements, we propose a novel design for predicting top-k next tokens that combines static analysis' ability to enumerate all valid keywords and in-scope identifiers with the ability of a language model to place a probability distribution over them. Our model mixes character-level input representation with token output to represent out-of-vocabulary (OOV) tokens meaningfully and minimize prediction latency. OOV tokens can be predicted through detection of local repetition common in software. This design achieves state-of-art accuracy in source code modeling and fits the constraints imposed by real-world code completion implementations in modern IDEs. 
