---
layout: publication
title: "OCoR: An Overlapping-Aware Code Retriever"
authors: Qihao Zhu, Zeyu Sun, Xiran Liang, Yingfei Xiong, Lu Zhang
conference: ASE
year: 2020
additional_links:
  - { name: "ArXiV", url: "https://arxiv.org/abs/2008.05201" }
tags: ["search"]
---

Code retrieval helps developers reuse the code snippet in the open-source projects. Given a natural language description, code retrieval aims to search for the most relevant code among a set of code. Existing state-of-the-art approaches apply neural networks to code retrieval. However, these approaches still fail to capture an important feature: overlaps. The overlaps between different names used by different people indicate that two different names may be potentially related (e.g., "message" and "msg"), and the overlaps between identifiers in code and words in natural language descriptions indicate that the code snippet and the description may potentially be related. To address these problems, we propose a novel neural architecture named OCoR, where we introduce two specifically-designed components to capture overlaps: the first embeds identifiers by character to capture the overlaps between identifiers, and the second introduces a novel overlap matrix to represent the degrees of overlaps between each natural language word and each identifier.
The evaluation was conducted on two established datasets. The experimental results show that OCoR significantly outperforms the existing state-of-the-art approaches and achieves 13.1% to 22.3% improvements. Moreover, we also conducted several in-depth experiments to help understand the performance of different components in OCoR.
