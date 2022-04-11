---
layout: publication
title: "TranS^3: A Transformer-based Framework for Unifying Code Summarization and Code Search"
authors: Wenhua Wang, Yuqun Zhang, Zhengran Zeng, Guandong Xu
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2003.03238"}
tags: ["search", "documentation"]
---
Code summarization and code search have been widely adopted in sofwaredevelopmentandmaintenance. However, fewstudieshave explored the efcacy of unifying them. In this paper, we propose TranS^3 , a transformer-based framework to integrate code summarization with code search. Specifcally, for code summarization,TranS^3 enables an actor-critic network, where in the actor network, we encode the collected code snippets via transformer- and tree-transformer-based encoder and decode the given code snippet to generate its comment. Meanwhile, we iteratively tune the actor network via the feedback from the critic network for enhancing the quality of the generated comments. Furthermore, we import the generated comments to code search for enhancing its accuracy. To evaluatetheefectivenessof TranS^3 , we conduct a set of experimental studies and case studies where the experimental results suggest that TranS^3 can signifcantly outperform multiple state-of-the-art approaches in both code summarization and code search and the study results further strengthen the efcacy of TranS^3 from the developers' points of view. 
