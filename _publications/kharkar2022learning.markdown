---
layout: publication
title: "Learning to Reduce False Positives in Analytic Bug Detectors"
authors: Anant Kharkar, Roshanak Zilouchian Moghaddam, Matthew Jin, Xiaoyu Liu, Xin Shi, Colin Clement, Neel Sundaresan
conference: ICSE
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2203.09907"}
tags: ["Transformer", "static analysis"]
---
Due to increasingly complex software design and rapid iterative development, code defects and security vulnerabilities are prevalent in modern software. In response, programmers rely on static analysis tools to regularly scan their codebases and find potential bugs. In order to maximize coverage, however, these tools generally tend to report a significant number of false positives, requiring developers to manually verify each warning. To address this problem, we propose a Transformer-based learning approach to identify false positive bug warnings. We demonstrate that our models can improve the precision of static analysis by 17.5%. In addition, we validated the generalizability of this approach across two major bug types: null dereference and resource leak. 
