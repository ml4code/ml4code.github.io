---
layout: publication
title: Disentangled Code Representation Learning for Multiple Programming Languages
authors: Jingfeng Zhang, Haiwen Hong, Yin Zhang, Yao Wan, Ye Liu, Yulei Sui
conference: ACL
year: 2021
additional_links:
   - {name: "Proceedings", url: "https://aclanthology.org/2021.findings-acl.391/"}
tags: ["representation"]
---
Developing effective distributed representations of source code is fundamental yet challenging for many software engineering tasks such as code clone detection, code search, code translation and transformation. However, current code embedding approaches that represent the semantic and syntax of code in a mixed way are less interpretable and the resulting embedding can not be easily generalized across programming languages. In this paper, we propose a disentangled code representation learning approach to separate the semantic from the syntax of source code under a multi-programming-language setting, obtaining better interpretability and generalizability. Specially, we design three losses dedicated to the characteristics of source code to enforce the disentanglement effectively. We conduct comprehensive experiments on a real-world dataset composed of programming exercises implemented by multiple solutions that are semantically identical but grammatically distinguished. The experimental results validate the superiority of our proposed disentangled code representation, compared to several baselines, across three types of downstream tasks, i.e., code clone detection, code translation, and code-to-code search.