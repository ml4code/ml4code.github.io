---
layout: publication
title: "Open Vocabulary Learning on Source Code with a Graph-Structured Cache"
authors: Milan Cvitkovic, Badal Singh, Anima Anandkumar
conference:
year: 2018
bibkey: cvitkovic2018open.markdown
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1810.08305"}
tags: ["GNN", "variable misuse", "defect", "representation"]
---
Machine learning models that take computer program source code as input typically use Natural Language Processing (NLP) techniques. However, a major challenge is that code is written using an open, rapidly changing vocabulary due to, e.g., the coinage of new variable and method names. Reasoning over such a vocabulary is not something for which most NLP methods are designed. We introduce a Graph-Structured Cache to address this problem; this cache contains a node for each new word the model encounters with edges connecting each word to its occurrences in the code. We find that combining this graph-structured cache strategy with recent Graph-Neural-Network-based models for supervised learning on code improves the models' performance on a code completion task and a variable naming task --- with over 100% relative improvement on the latter --- at the cost of a moderate increase in computation time.
