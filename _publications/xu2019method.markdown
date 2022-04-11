---
layout: publication
title: "Method name suggestion with hierarchical attention networks"
authors: Sihan Xu, Sen Zhang, Weijing Wang, Xinya Cao, Chenkai Guo, Jing Xu.
conference: PEPM
year: 2019
tags: ["naming"]
---
Method Rename has been a widely used refactoring operation that improves program comprehension and maintenance. Descriptive method names that summarize functionalities of source code can facilitate program comprehension. Much research has been done to suggest method names through source code summarization. However, unlike natural language, a code snippet consists of basic blocks organized by complicated structures. In this work, we observe a hierarchical structure --- tokens form basic blocks and basic blocks form a code snippet. Based on this observation, we exploit a hierarchical attention network to learn the representation of methods. Specifically, we apply two-level attention mechanism to learn the importance of each token in a basic block and that of a basic block in a method respectively. We evaluated our approach on 10 open source repositories and compared it against three state-of-the-art approaches. The results on these open-source data show the superiority of our hierarchical attention networks in terms of effectiveness.
