---
layout: publication
title: "Co-Training for Commit Classification"
authors: Jian Yi, David Lee, Hai Leong Chieu
conference: EMNLP WNUT
year: 2021
additional_links:
   - {name: "website", url: "https://aclanthology.org/2021.wnut-1.43/"}
   - {name: "code", url: "https://github.com/davidleejy/wnut21-cotrain"}
tags: ["Transformer", "bimodal", "defect"]
---
Commits in version control systems (e.g. Git) track changes in a software project. Commits comprise noisy user-generated natural language and code patches. Automatic commit classification (CC) has been used to determine the type of code maintenance activities performed, as well as to detect bug fixes in code repositories. Much prior work occurs in the fully-supervised setting – a setting that can be a stretch in resource-scarce situations presenting difficulties in labeling commits. In this paper, we apply co-training, a semi-supervised learning method, to take advantage of the two views available – the commit message (natural language) and the code changes (programming language) – to improve commit classification.
